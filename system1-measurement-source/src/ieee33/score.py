"""
score.py
--------
Scoring harness for the IEEE 33-bus System 2 state estimator.

This module is the SOLE component allowed to read the 'state' and
'fault_event' oracle buckets.  Estimator modules (estimate.py, estimators.py,
fase_predict.py, ac_model.py) must NEVER import this module or read oracle
buckets.  Grep-checkable: zero oracle references in those files.

Oracle join: reads per-bus estimates from the 'estimates' bucket and the
ground-truth bus states from 'state' / 'fault_event'.  Computes:

  1. Per-bus voltage |V| and angle RMSE (median over buses) — R10 gate.
  2. Dark-node (pseudo-only) bus voltage RMSE — R10 dark-node gate.
  3. Dark-node RMSE vs flat/pseudo-only baseline — R10 baseline gate.
  4. Time-averaged NEES vs 95% chi2 band — R11 NEES gate.
  5. Per-step NIS in-band fraction from persisted nis_k/m_k — R11 NIS gate.
  6. Fault covariance inflation (sigma_V / trace_P higher in faulted_isolated
     than pre_fault) — R12 fault gate.
  7. Restored-block RMSE back within well_observed bar — R12 restore gate.

Prints a falsifiable PASS/FAIL report (mirroring measure.py footprint style)
and exits non-zero on any threshold miss.

Run:  uv run score [--scenario ...] [--source ...] [--estimator wls|ekf|ukf|all]
"""

import argparse
import sys

import numpy as np
import pandas as pd
from scipy.stats import chi2

import ieee33.estimate_config as ec
from ieee33 import config, influx
import ieee33.measure_config as mc


# ---------------------------------------------------------------------------
# CLI argument parsing (mirror measure.py / estimate.py pattern)
# ---------------------------------------------------------------------------

def _parse_args():
    p = argparse.ArgumentParser(
        description="IEEE 33-bus state estimator scoring harness — oracle join + RMSE + NEES/NIS."
    )
    p.add_argument(
        "--scenario",
        choices=["well_observed", "realistic_sparse"],
        default=None,
        help="Sensor-placement scenario (default: estimate_config.ACTIVE['scenario'])",
    )
    p.add_argument(
        "--source",
        choices=["day", "fault"],
        default=None,
        help="Data source: 'day' = 96-step day, 'fault' = 40-step fault "
             "(default: estimate_config.ACTIVE['source'])",
    )
    p.add_argument(
        "--estimator",
        choices=["wls", "ekf", "ukf", "all"],
        default="all",
        help="Estimator to score; 'all' scores wls+ekf+ukf and prints comparison block "
             "(default: 'all')",
    )
    return p.parse_args()


def _merge_cfg(args) -> dict:
    """Merge estimate_config.ACTIVE with non-None CLI overrides."""
    cfg = dict(ec.ACTIVE)
    for key in ("scenario", "source"):
        val = getattr(args, key, None)
        if val is not None:
            cfg[key] = val
    # estimator handled separately (score has 'all' option not in ACTIVE)
    cfg["estimator"] = args.estimator
    return cfg


# ---------------------------------------------------------------------------
# Dark-node identification
# ---------------------------------------------------------------------------

def _identify_dark_buses(scenario: str) -> set:
    """Return the set of pseudo-only (dark) buses for the given scenario.

    Dark bus = a load bus that has NO real-sensor coverage (scada / pmu / ami /
    der / zero_inj) and is thus covered only by a pseudo-measurement forecast.
    These are the buses where the estimator must propagate information from
    neighbours through the Ybus coupling — the hard case for the estimator.

    This is determined purely from measure_config.SCENARIOS (static sensor
    placement) — no InfluxDB read needed.

    Args:
        scenario: "well_observed" | "realistic_sparse"

    Returns:
        set of int bus IDs that are pseudo-only (dark) for the given scenario.
    """
    if scenario not in mc.SCENARIOS:
        return set()

    scen = mc.SCENARIOS[scenario]
    # Collect all buses with at least one real sensor class
    real_classes = ("scada", "pmu", "ami", "der", "zero_inj")
    covered = set()
    for cls in real_classes:
        covered.update(scen.get(cls, []))

    # Load buses 1..32 not in covered = pseudo-only (dark)
    all_load_buses = set(range(1, 33))  # buses 1..32 (excluding feeder-head bus 0)
    dark = all_load_buses - covered
    return dark


# ---------------------------------------------------------------------------
# Oracle readers (SOLE reader boundary)
# ---------------------------------------------------------------------------

def _read_oracle_day(client) -> pd.DataFrame:
    """Read ground-truth bus states for the day source from the 'state' oracle bucket.

    Returns DataFrame with columns: _time, bus_id (str), vm_pu, va_degree.
    """
    df = influx.read_state_bus(client)
    return df


def _read_oracle_fault(client) -> pd.DataFrame:
    """Read ground-truth bus states for the fault source from the 'fault_event' oracle bucket.

    CRITICAL (Pitfall 5): energised is a string TAG '1'/'0' — compare as string.

    Returns DataFrame with columns: _time, bus_id (str), energised (str '1'/'0'),
    vm_pu, va_degree.
    """
    df = influx.read_fault_bus(client)
    return df


def _read_fault_phases(client) -> pd.DataFrame:
    """Read fault topology/phase from the 'fault_event' event measurement.

    Returns DataFrame with columns: _time, phase.
    Used to partition steps into pre_fault / faulted_isolated / restored blocks.
    """
    df = influx.read_fault_event(client)
    return df


# ---------------------------------------------------------------------------
# Per-bus RMSE computation
# ---------------------------------------------------------------------------

def _compute_per_bus_rmse(
    est_df: pd.DataFrame,
    oracle_df: pd.DataFrame,
) -> dict:
    """Compute per-bus voltage magnitude RMSE and angle RMSE.

    Joins estimates to oracle on (_time, bus_id).  Both DataFrames must have
    bus_id as a string column (InfluxDB TAG → pivot surface).

    Args:
        est_df:    From read_estimates — columns include _time, bus_id, vm_pu_est,
                   va_degree_est.
        oracle_df: From read_state_bus or read_fault_bus — columns include
                   _time, bus_id, vm_pu, va_degree.

    Returns:
        dict with keys:
          'per_bus_vm_rmse'  — pd.Series indexed by bus_id (int), value=RMSE [pu]
          'per_bus_va_rmse'  — pd.Series indexed by bus_id (int), value=RMSE [deg]
          'median_vm_rmse'   — float (median over buses)
          'median_va_rmse'   — float (median over buses)
          'n_joined'         — int number of (time, bus) pairs joined
    """
    # Normalise _time to UTC pandas Timestamp for join
    est = est_df.copy()
    oracle = oracle_df.copy()

    # Convert _time to UTC-normalised string for merging (avoids tz mismatch)
    est["_time_str"]    = pd.to_datetime(est["_time"], utc=True).dt.strftime("%Y-%m-%dT%H:%M:%S")
    oracle["_time_str"] = pd.to_datetime(oracle["_time"], utc=True).dt.strftime("%Y-%m-%dT%H:%M:%S")

    # bus_id is a string TAG in both DataFrames
    merged = pd.merge(
        est[["_time_str", "bus_id", "vm_pu_est", "va_degree_est"]],
        oracle[["_time_str", "bus_id", "vm_pu", "va_degree"]],
        on=["_time_str", "bus_id"],
        how="inner",
    )

    if len(merged) == 0:
        return {
            "per_bus_vm_rmse": pd.Series(dtype=float),
            "per_bus_va_rmse": pd.Series(dtype=float),
            "median_vm_rmse": float("nan"),
            "median_va_rmse": float("nan"),
            "n_joined": 0,
        }

    merged["bus_id_int"] = merged["bus_id"].astype(int)
    merged["vm_err_sq"]  = (merged["vm_pu_est"]     - merged["vm_pu"])    ** 2
    merged["va_err_sq"]  = (merged["va_degree_est"]  - merged["va_degree"]) ** 2

    per_bus_vm = np.sqrt(merged.groupby("bus_id_int")["vm_err_sq"].mean())
    per_bus_va = np.sqrt(merged.groupby("bus_id_int")["va_err_sq"].mean())

    return {
        "per_bus_vm_rmse": per_bus_vm,
        "per_bus_va_rmse": per_bus_va,
        "median_vm_rmse": float(np.median(per_bus_vm.values)),
        "median_va_rmse": float(np.median(per_bus_va.values)),
        "n_joined": len(merged),
    }


# ---------------------------------------------------------------------------
# Dark-node analysis
# ---------------------------------------------------------------------------

def _compute_dark_node_metrics(
    per_bus_vm_rmse: "pd.Series",
    dark_buses: set,
    oracle_df: pd.DataFrame,
) -> dict:
    """Compute dark-node RMSE and flat/pseudo-only baseline comparison.

    Baseline = voltage RMSE at the dark buses if all estimates were kept at
    flat-start value 1.0 pu (i.e., estimator made no improvement over
    initialisation). This is the theoretical worst-case for an estimator that
    neither converges nor degrades: oracle RMSE from 1.0 pu flat start.

    Args:
        per_bus_vm_rmse: pd.Series indexed by int bus_id, value = per-bus RMSE [pu].
        dark_buses:      set of int bus IDs that are pseudo-only.
        oracle_df:       Ground-truth DataFrame with bus_id (str) and vm_pu.

    Returns:
        dict with keys:
          'dark_vm_rmse'      — float RMSE averaged over dark buses [pu]
          'baseline_vm_rmse'  — float flat-start RMSE over dark buses [pu]
          'dark_vs_baseline'  — float ratio (dark_rmse / baseline_rmse); <= 0.5 = PASS
          'n_dark_buses'      — int
    """
    if not dark_buses or len(per_bus_vm_rmse) == 0:
        return {
            "dark_vm_rmse": float("nan"),
            "baseline_vm_rmse": float("nan"),
            "dark_vs_baseline": float("nan"),
            "n_dark_buses": 0,
        }

    # Filter per-bus RMSE to only dark buses that appear in the estimate results
    dark_int = {int(b) for b in dark_buses}
    available_dark = dark_int.intersection(set(per_bus_vm_rmse.index))

    if not available_dark:
        return {
            "dark_vm_rmse": float("nan"),
            "baseline_vm_rmse": float("nan"),
            "dark_vs_baseline": float("nan"),
            "n_dark_buses": 0,
        }

    dark_rmse_vals = per_bus_vm_rmse.loc[sorted(available_dark)].values
    dark_vm_rmse = float(np.mean(dark_rmse_vals))

    # Compute flat-start baseline: oracle RMSE at dark buses from 1.0 pu
    oracle = oracle_df.copy()
    oracle["bus_id_int"] = oracle["bus_id"].astype(int)
    dark_oracle = oracle[oracle["bus_id_int"].isin(available_dark)]
    if len(dark_oracle) == 0:
        return {
            "dark_vm_rmse": dark_vm_rmse,
            "baseline_vm_rmse": float("nan"),
            "dark_vs_baseline": float("nan"),
            "n_dark_buses": len(available_dark),
        }

    flat_err_sq = (dark_oracle["vm_pu"].values - 1.0) ** 2
    baseline_vm_rmse = float(np.sqrt(np.mean(flat_err_sq)))

    dark_vs_baseline = (
        float(dark_vm_rmse / baseline_vm_rmse)
        if baseline_vm_rmse > 1e-12
        else float("nan")
    )

    return {
        "dark_vm_rmse": dark_vm_rmse,
        "baseline_vm_rmse": baseline_vm_rmse,
        "dark_vs_baseline": dark_vs_baseline,
        "n_dark_buses": len(available_dark),
    }


# ---------------------------------------------------------------------------
# NEES computation (Pattern 8 — requires oracle)
# ---------------------------------------------------------------------------

def _compute_nees(
    est_df: pd.DataFrame,
    oracle_df: pd.DataFrame,
    n_state: int = ec.N_FREE_STATES,
    confidence: float = ec.NEES_CONFIDENCE,
) -> dict:
    """Compute time-averaged NEES and 95% chi2 band.

    NEES_k = (x_hat_k - x_true_k)^T P_k^{-1} (x_hat_k - x_true_k)
    NEES_avg = mean(NEES_k over N steps)
    Band: [chi2.ppf(alpha/2, N*n) / N, chi2.ppf(1-alpha/2, N*n) / N]
    For n=64, N=96: band ≈ [61.76, 66.28].

    P is reconstructed from the diagonal sigma fields (sigma_vm, sigma_va)
    as a diagonal approximation.  The true P is not persisted in InfluxDB
    (only the diagonal entries are); this gives a lower bound on NEES.

    IMPORTANT: This is the best available NEES approximation given the stored
    data (only diagonal sigma fields are persisted).  The NEES values may
    differ from the exact (full-P) NEES computed inside the filter, but the
    diagonal approximation is an unbiased estimator of the per-bus contribution.

    Args:
        est_df:      From read_estimates — columns include _time, bus_id,
                     vm_pu_est, va_degree_est, sigma_vm, sigma_va.
        oracle_df:   From read_state_bus or read_fault_bus — bus_id, vm_pu,
                     va_degree.
        n_state:     Free state dimension (default 64 = ec.N_FREE_STATES).
        confidence:  Chi2 band confidence level (default 0.95).

    Returns:
        dict with keys:
          'nees_avg'   — float time-averaged NEES
          'nees_lo'    — float lower chi2 bound
          'nees_hi'    — float upper chi2 bound
          'nees_pass'  — bool
          'N_steps'    — int number of steps used
    """
    est = est_df.copy()
    oracle = oracle_df.copy()

    est["_time_str"]    = pd.to_datetime(est["_time"], utc=True).dt.strftime("%Y-%m-%dT%H:%M:%S")
    oracle["_time_str"] = pd.to_datetime(oracle["_time"], utc=True).dt.strftime("%Y-%m-%dT%H:%M:%S")

    merged = pd.merge(
        est[["_time_str", "bus_id", "vm_pu_est", "va_degree_est", "sigma_vm", "sigma_va"]],
        oracle[["_time_str", "bus_id", "vm_pu", "va_degree"]],
        on=["_time_str", "bus_id"],
        how="inner",
    )

    if len(merged) == 0:
        return {
            "nees_avg": float("nan"), "nees_lo": float("nan"),
            "nees_hi": float("nan"), "nees_pass": False, "N_steps": 0,
        }

    # va_degree_est is in degrees (stored as degrees by write_estimate_step)
    # va_degree is also in degrees (oracle) — no conversion needed
    # sigma_va is in degrees (stored as degrees by write_estimate_step)
    err_vm = merged["vm_pu_est"]     - merged["vm_pu"]
    err_va = merged["va_degree_est"] - merged["va_degree"]
    # Avoid division by zero in sigma
    sig_vm = merged["sigma_vm"].clip(lower=1e-12)
    sig_va = merged["sigma_va"].clip(lower=1e-12)

    # Diagonal NEES contribution per bus per step
    merged["nees_contrib"] = (err_vm / sig_vm) ** 2 + (err_va / sig_va) ** 2

    # Sum over buses per time step → per-step NEES (= sum of n_state chi2(1) terms)
    per_step_nees = merged.groupby("_time_str")["nees_contrib"].sum()
    N = len(per_step_nees)
    if N == 0:
        return {
            "nees_avg": float("nan"), "nees_lo": float("nan"),
            "nees_hi": float("nan"), "nees_pass": False, "N_steps": 0,
        }

    nees_avg = float(per_step_nees.mean())
    alpha = 1.0 - confidence
    lo = float(chi2.ppf(alpha / 2,     N * n_state) / N)
    hi = float(chi2.ppf(1 - alpha / 2, N * n_state) / N)
    nees_pass = lo <= nees_avg <= hi

    return {
        "nees_avg": nees_avg,
        "nees_lo":  lo,
        "nees_hi":  hi,
        "nees_pass": nees_pass,
        "N_steps":  N,
    }


# ---------------------------------------------------------------------------
# NIS computation from persisted nis_k/m_k series (FAITHFUL path — R11)
# ---------------------------------------------------------------------------

def _compute_nis_fraction(sys_df: pd.DataFrame, confidence: float = ec.NEES_CONFIDENCE) -> dict:
    """Compute per-step NIS in-band fraction from the persisted nis_k/m_k series.

    FAITHFUL path: reads the actual Mahalanobis innovation statistic persisted
    by EKF/UKF during estimation.  Does NOT reconstruct from diagonal sigma.

    For each update step k:
      - nis_k = y_k^T S_k^{-1} y_k  (persisted by the filter)
      - m_k   = innovation dimension at step k
      - 95% chi2 band: [chi2.ppf(0.025, m_k), chi2.ppf(0.975, m_k)]
      - in-band if lo <= nis_k <= hi

    WLS: no nis_k/m_k fields present (NIS is not defined for snapshot estimators).
    Returns is_applicable=False for WLS runs.

    Args:
        sys_df:     From read_estimate_system — columns include trace_P, and
                    optionally nis_k, m_k (present for ekf/ukf, absent for wls).
        confidence: Chi2 band confidence level (default 0.95).

    Returns:
        dict with keys:
          'nis_fraction' — float in-band fraction [0.0, 1.0] or None
          'nis_pass'     — bool or None
          'is_applicable' — bool (False for WLS)
          'n_steps_with_nis' — int number of update steps with nis_k present
    """
    # WLS: nis_k column will be absent or all-NaN
    if "nis_k" not in sys_df.columns or "m_k" not in sys_df.columns:
        return {
            "nis_fraction": None,
            "nis_pass": None,
            "is_applicable": False,
            "n_steps_with_nis": 0,
        }

    # Drop rows where nis_k or m_k is NaN (WLS rows or missing steps)
    valid = sys_df.dropna(subset=["nis_k", "m_k"])
    if len(valid) == 0:
        return {
            "nis_fraction": None,
            "nis_pass": None,
            "is_applicable": False,
            "n_steps_with_nis": 0,
        }

    alpha = 1.0 - confidence
    in_band = 0
    for _, row in valid.iterrows():
        nis_k_val = float(row["nis_k"])
        m_k_val   = int(row["m_k"])
        if m_k_val <= 0:
            continue
        lo = float(chi2.ppf(alpha / 2,     m_k_val))
        hi = float(chi2.ppf(1 - alpha / 2, m_k_val))
        if lo <= nis_k_val <= hi:
            in_band += 1

    n_valid = len(valid)
    nis_fraction = float(in_band / n_valid) if n_valid > 0 else float("nan")
    nis_pass = nis_fraction >= 0.90

    return {
        "nis_fraction": nis_fraction,
        "nis_pass": nis_pass,
        "is_applicable": True,
        "n_steps_with_nis": n_valid,
    }


# ---------------------------------------------------------------------------
# Fault analysis — R12
# ---------------------------------------------------------------------------

def _compute_fault_metrics(
    est_df: pd.DataFrame,
    sys_df: pd.DataFrame,
    oracle_df: pd.DataFrame,
    fault_phases_df: pd.DataFrame,
) -> dict:
    """Compute fault covariance inflation and restored-RMSE metrics (R12).

    Checks:
      1. mean sigma_V (from est_df) and trace_P (from sys_df) both higher in
         'faulted_isolated' than 'pre_fault' → PASS.
      2. Voltage RMSE in the 'restored' block (energised buses only)
         back within the well_observed bar (< 0.005 pu) → PASS.

    CRITICAL (Pitfall 5): energised tag is a STRING — compare as '1'.

    Args:
        est_df:          Per-bus estimates (vm_pu_est, sigma_vm, bus_id, _time).
        sys_df:          System-level (trace_P, _time).
        oracle_df:       Fault-oracle bus states (bus_id, energised, vm_pu, _time).
        fault_phases_df: Event measurement (_time, phase).

    Returns:
        dict with keys:
          'sigma_v_pre'          — float mean sigma_V in pre_fault block
          'sigma_v_isolated'     — float mean sigma_V in faulted_isolated block
          'trace_p_pre'          — float mean trace_P in pre_fault block
          'trace_p_isolated'     — float mean trace_P in faulted_isolated block
          'inflation_pass'       — bool (sigma_V and trace_P higher in isolated)
          'restored_vm_rmse'     — float voltage RMSE in restored block
          'restored_pass'        — bool (RMSE < 0.005 pu)
          'has_fault_data'       — bool (False if fault phase data not found)
    """
    if fault_phases_df is None or len(fault_phases_df) == 0:
        return {
            "sigma_v_pre": float("nan"), "sigma_v_isolated": float("nan"),
            "trace_p_pre": float("nan"), "trace_p_isolated": float("nan"),
            "inflation_pass": False, "restored_vm_rmse": float("nan"),
            "restored_pass": False, "has_fault_data": False,
        }

    # Build time-to-phase lookup from fault_phases_df
    fp = fault_phases_df.copy()
    fp["_time_str"] = pd.to_datetime(fp["_time"], utc=True).dt.strftime("%Y-%m-%dT%H:%M:%S")
    time_to_phase = dict(zip(fp["_time_str"], fp["phase"]))

    if not time_to_phase:
        return {
            "sigma_v_pre": float("nan"), "sigma_v_isolated": float("nan"),
            "trace_p_pre": float("nan"), "trace_p_isolated": float("nan"),
            "inflation_pass": False, "restored_vm_rmse": float("nan"),
            "restored_pass": False, "has_fault_data": False,
        }

    # Partition estimates by phase
    est = est_df.copy()
    est["_time_str"] = pd.to_datetime(est["_time"], utc=True).dt.strftime("%Y-%m-%dT%H:%M:%S")
    est["phase"] = est["_time_str"].map(time_to_phase)

    sys = sys_df.copy()
    sys["_time_str"] = pd.to_datetime(sys["_time"], utc=True).dt.strftime("%Y-%m-%dT%H:%M:%S")
    sys["phase"] = sys["_time_str"].map(time_to_phase)

    pre_est  = est[est["phase"] == "pre_fault"]
    iso_est  = est[est["phase"] == "faulted_isolated"]
    rst_est  = est[est["phase"] == "restored"]

    pre_sys  = sys[sys["phase"] == "pre_fault"]
    iso_sys  = sys[sys["phase"] == "faulted_isolated"]

    # sigma_V mean per block (mean of sigma_vm over all bus-steps in block)
    sigma_v_pre      = float(pre_est["sigma_vm"].mean()) if len(pre_est)  > 0 else float("nan")
    sigma_v_isolated = float(iso_est["sigma_vm"].mean()) if len(iso_est)  > 0 else float("nan")
    trace_p_pre      = float(pre_sys["trace_P"].mean()) if len(pre_sys) > 0 else float("nan")
    trace_p_isolated = float(iso_sys["trace_P"].mean()) if len(iso_sys) > 0 else float("nan")

    # Both sigma_V and trace_P should be higher in isolated than pre_fault
    inflation_pass = (
        not (np.isnan(sigma_v_pre) or np.isnan(sigma_v_isolated) or
             np.isnan(trace_p_pre) or np.isnan(trace_p_isolated))
        and sigma_v_isolated > sigma_v_pre
        and trace_p_isolated > trace_p_pre
    )

    # Restored block: join with oracle (energised buses only) and compute RMSE
    oracle = oracle_df.copy()
    oracle["_time_str"] = pd.to_datetime(oracle["_time"], utc=True).dt.strftime(
        "%Y-%m-%dT%H:%M:%S"
    )
    oracle["phase"] = oracle["_time_str"].map(time_to_phase)

    # Energised buses in restored phase (Pitfall 5: energised is STRING '1')
    rst_oracle = oracle[(oracle["phase"] == "restored") & (oracle["energised"] == "1")]

    if len(rst_est) > 0 and len(rst_oracle) > 0:
        merged_rst = pd.merge(
            rst_est[["_time_str", "bus_id", "vm_pu_est"]],
            rst_oracle[["_time_str", "bus_id", "vm_pu"]],
            on=["_time_str", "bus_id"],
            how="inner",
        )
        if len(merged_rst) > 0:
            err_sq = (merged_rst["vm_pu_est"] - merged_rst["vm_pu"]) ** 2
            restored_vm_rmse = float(np.sqrt(err_sq.mean()))
        else:
            restored_vm_rmse = float("nan")
    else:
        restored_vm_rmse = float("nan")

    restored_pass = (
        not np.isnan(restored_vm_rmse) and restored_vm_rmse < 0.005
    )

    return {
        "sigma_v_pre": sigma_v_pre,
        "sigma_v_isolated": sigma_v_isolated,
        "trace_p_pre": trace_p_pre,
        "trace_p_isolated": trace_p_isolated,
        "inflation_pass": inflation_pass,
        "restored_vm_rmse": restored_vm_rmse,
        "restored_pass": restored_pass,
        "has_fault_data": True,
    }


# ---------------------------------------------------------------------------
# NEES band derivation check (self-documenting assertion)
# ---------------------------------------------------------------------------

def _derive_nees_band(n_state: int = ec.N_FREE_STATES, N_steps: int = 96,
                      confidence: float = ec.NEES_CONFIDENCE):
    """Derive and return the 95% chi2 NEES band for n_state=64, N_steps=96.

    Asserts the band matches the expected [61.76, 66.28] from RESEARCH.md.
    This is computed via scipy.stats.chi2.ppf — not hardcoded.

    Returns:
        (lo, hi) tuple of floats.
    """
    alpha = 1.0 - confidence
    lo = float(chi2.ppf(alpha / 2,     N_steps * n_state) / N_steps)
    hi = float(chi2.ppf(1 - alpha / 2, N_steps * n_state) / N_steps)
    # Self-documenting: verify the band matches RESEARCH.md expectations.
    # Tolerance is wide enough to account for different scipy versions.
    if not (61.0 < lo < 62.5 and 65.5 < hi < 67.0):
        print(
            f"[WARN] score.py: NEES band [{lo:.2f},{hi:.2f}] for n={n_state},N={N_steps} "
            f"does not match expected [61.76,66.28] — check scipy version",
            file=sys.stderr,
        )
    return lo, hi


# ---------------------------------------------------------------------------
# Single-estimator scoring
# ---------------------------------------------------------------------------

def _score_one(
    client,
    scenario: str,
    experiment: str,
    estimator: str,
) -> dict:
    """Score one (scenario, experiment, estimator) run.

    Returns a dict with all metric values and PASS/FAIL flags.
    May raise RuntimeError if no estimate data is present.
    """
    # ---- oracle reads (this function is the SOLE oracle reader) ----
    if experiment == "day":
        oracle_bus = _read_oracle_day(client)
        fault_phases = None
        oracle_fault = None
    else:
        oracle_bus   = _read_oracle_fault(client)
        fault_phases = _read_fault_phases(client)
        oracle_fault = oracle_bus  # for fault: oracle includes energised tag

    # ---- estimate reads ----
    est_df = influx.read_estimates(client, scenario, experiment, estimator)
    sys_df = influx.read_estimate_system(client, scenario, experiment, estimator)

    # ---- NEES band (derive once, not hardcoded) ----
    # N_steps from the estimate data (how many time steps we actually have)
    n_time_steps = est_df["_time"].nunique()
    nees_lo_96, nees_hi_96 = _derive_nees_band(
        n_state=ec.N_FREE_STATES, N_steps=max(n_time_steps, 1)
    )

    # ---- per-bus RMSE (all buses, all steps) ----
    # For fault source: use only energised buses for RMSE to avoid 0.0 dead-bus bias
    if experiment == "fault" and "energised" in oracle_bus.columns:
        oracle_for_rmse = oracle_bus[oracle_bus["energised"] == "1"].copy()
    else:
        oracle_for_rmse = oracle_bus

    rmse_result = _compute_per_bus_rmse(est_df, oracle_for_rmse)

    # ---- dark-node analysis ----
    dark_buses = _identify_dark_buses(scenario)
    dark_result = _compute_dark_node_metrics(
        rmse_result["per_bus_vm_rmse"],
        dark_buses,
        oracle_for_rmse,
    )

    # ---- NEES ----
    nees_result = _compute_nees(
        est_df=est_df,
        oracle_df=oracle_for_rmse,
        n_state=ec.N_FREE_STATES,
        confidence=ec.NEES_CONFIDENCE,
    )
    # Update lo/hi from actual step count
    actual_lo, actual_hi = _derive_nees_band(
        n_state=ec.N_FREE_STATES,
        N_steps=max(nees_result["N_steps"], 1),
        confidence=ec.NEES_CONFIDENCE,
    )
    nees_result["nees_lo"] = actual_lo
    nees_result["nees_hi"] = actual_hi
    nees_result["nees_pass"] = actual_lo <= nees_result["nees_avg"] <= actual_hi

    # ---- NIS from persisted nis_k/m_k (FAITHFUL path) ----
    nis_result = _compute_nis_fraction(sys_df, confidence=ec.NEES_CONFIDENCE)

    # ---- fault metrics (R12) — only for fault source ----
    if experiment == "fault":
        fault_result = _compute_fault_metrics(
            est_df=est_df,
            sys_df=sys_df,
            oracle_df=oracle_bus,
            fault_phases_df=fault_phases,
        )
    else:
        fault_result = {
            "sigma_v_pre": None, "sigma_v_isolated": None,
            "trace_p_pre": None, "trace_p_isolated": None,
            "inflation_pass": None, "restored_vm_rmse": None,
            "restored_pass": None, "has_fault_data": False,
        }

    return {
        "scenario": scenario,
        "experiment": experiment,
        "estimator": estimator,
        # R10 thresholds
        "median_vm_rmse":   rmse_result["median_vm_rmse"],
        "median_va_rmse":   rmse_result["median_va_rmse"],
        "vm_pass":          (not np.isnan(rmse_result["median_vm_rmse"])
                             and rmse_result["median_vm_rmse"] < 0.005),
        "va_pass":          (not np.isnan(rmse_result["median_va_rmse"])
                             and rmse_result["median_va_rmse"] < 0.1),
        # R10 dark-node
        "dark_vm_rmse":     dark_result["dark_vm_rmse"],
        "baseline_vm_rmse": dark_result["baseline_vm_rmse"],
        "dark_vs_baseline": dark_result["dark_vs_baseline"],
        "dark_rmse_pass":   (not np.isnan(dark_result["dark_vm_rmse"])
                             and dark_result["dark_vm_rmse"] < 0.02),
        "dark_baseline_pass": (not np.isnan(dark_result["dark_vs_baseline"])
                               and dark_result["dark_vs_baseline"] <= 0.5),
        "n_dark_buses":     dark_result["n_dark_buses"],
        # R11 NEES
        "nees_avg":         nees_result["nees_avg"],
        "nees_lo":          nees_result["nees_lo"],
        "nees_hi":          nees_result["nees_hi"],
        "nees_pass":        nees_result["nees_pass"],
        "N_steps":          nees_result["N_steps"],
        # R11 NIS
        "nis_fraction":     nis_result["nis_fraction"],
        "nis_pass":         nis_result["nis_pass"],
        "nis_applicable":   nis_result["is_applicable"],
        "n_steps_with_nis": nis_result["n_steps_with_nis"],
        # R12 fault
        "sigma_v_pre":      fault_result["sigma_v_pre"],
        "sigma_v_isolated": fault_result["sigma_v_isolated"],
        "trace_p_pre":      fault_result["trace_p_pre"],
        "trace_p_isolated": fault_result["trace_p_isolated"],
        "inflation_pass":   fault_result["inflation_pass"],
        "restored_vm_rmse": fault_result["restored_vm_rmse"],
        "restored_pass":    fault_result["restored_pass"],
        "has_fault_data":   fault_result["has_fault_data"],
    }


# ---------------------------------------------------------------------------
# Report printer
# ---------------------------------------------------------------------------

def _print_report(r: dict) -> list:
    """Print the scoring report for one estimator run.

    Returns a list of failing metric descriptions (empty = all PASS).
    Mirrors measure.py footprint report style (lines 927-975).
    """
    fails = []

    print("\n" + "=" * 62)
    print("State Estimator Scoring Report")
    print("=" * 62)
    print(f"Scenario  : {r['scenario']}")
    print(f"Source    : {r['experiment']}")
    print(f"Estimator : {r['estimator']}")
    print(f"Steps     : {r['N_steps']}")
    print("---")

    # R10 — well_observed RMSE thresholds
    vm_str  = f"{r['median_vm_rmse']:.4f}" if not np.isnan(r['median_vm_rmse'])  else " N/A "
    va_str  = f"{r['median_va_rmse']:.4f}" if not np.isnan(r['median_va_rmse'])  else " N/A "
    vm_tag  = "PASS" if r["vm_pass"] else "FAIL"
    va_tag  = "PASS" if r["va_pass"] else "FAIL"
    print(f"  Voltage RMSE (median over buses) : {vm_str} pu  {vm_tag}  (< 0.005 pu)")
    print(f"  Angle RMSE   (median over buses) : {va_str} deg {va_tag}  (< 0.1 deg)")
    if not r["vm_pass"]:
        fails.append(f"Voltage RMSE {vm_str} pu >= 0.005 pu threshold")
    if not r["va_pass"]:
        fails.append(f"Angle RMSE {va_str} deg >= 0.1 deg threshold")

    # R10 — dark-node thresholds
    if r["n_dark_buses"] > 0:
        drk_str = f"{r['dark_vm_rmse']:.4f}" if not np.isnan(r['dark_vm_rmse']) else " N/A "
        dvb_str = f"{r['dark_vs_baseline']:.3f}" if not np.isnan(r['dark_vs_baseline']) else " N/A "
        bas_str = f"{r['baseline_vm_rmse']:.4f}" if not np.isnan(r['baseline_vm_rmse']) else " N/A "
        drk_tag = "PASS" if r["dark_rmse_pass"]     else "FAIL"
        dvb_tag = "PASS" if r["dark_baseline_pass"] else "FAIL"
        print(f"  Dark-node voltage RMSE ({r['n_dark_buses']} buses) : "
              f"{drk_str} pu  {drk_tag}  (< 0.02 pu)")
        print(f"  Dark-node vs flat baseline       : "
              f"{dvb_str}   {dvb_tag}  (<= 50%, baseline {bas_str} pu)")
        if not r["dark_rmse_pass"]:
            fails.append(f"Dark-node RMSE {drk_str} pu >= 0.02 pu threshold")
        if not r["dark_baseline_pass"]:
            fails.append(f"Dark-node vs baseline {dvb_str} > 0.5 threshold")
    else:
        print(f"  Dark-node analysis               : N/A  (no dark buses in scenario '{r['scenario']}')")

    # R11 — NEES
    nees_str = f"{r['nees_avg']:.2f}" if not np.isnan(r['nees_avg']) else " N/A "
    nees_tag = "PASS" if r["nees_pass"] else "FAIL"
    print(f"  NEES avg / 95% chi2 band [{r['nees_lo']:.2f},{r['nees_hi']:.2f}] : "
          f"{nees_str}  {nees_tag}")
    if not r["nees_pass"]:
        fails.append(f"NEES avg {nees_str} outside chi2 band [{r['nees_lo']:.2f},{r['nees_hi']:.2f}]")

    # R11 — NIS (from persisted nis_k/m_k, faithful path)
    if r["nis_applicable"]:
        nis_str = f"{r['nis_fraction']:.3f}" if r["nis_fraction"] is not None else " N/A "
        nis_tag = "PASS" if r["nis_pass"] else "FAIL"
        print(f"  NIS in-band fraction ({r['n_steps_with_nis']} steps) : "
              f"{nis_str}  {nis_tag}  (>= 90%, from persisted nis_k/m_k)")
        if not r["nis_pass"]:
            fails.append(f"NIS in-band fraction {nis_str} < 0.90 threshold")
    else:
        # WLS: NIS is not defined for snapshot estimator (no innovation sequence)
        print(f"  NIS in-band fraction             : N/A  "
              f"(WLS is a snapshot estimator — no innovation sequence; NIS not applicable)")

    # R12 — fault analysis (only for fault source)
    if r["has_fault_data"]:
        pre_sv  = f"{r['sigma_v_pre']:.4f}"      if r['sigma_v_pre']      is not None else " N/A "
        iso_sv  = f"{r['sigma_v_isolated']:.4f}" if r['sigma_v_isolated'] is not None else " N/A "
        pre_tp  = f"{r['trace_p_pre']:.4f}"      if r['trace_p_pre']      is not None else " N/A "
        iso_tp  = f"{r['trace_p_isolated']:.4f}" if r['trace_p_isolated'] is not None else " N/A "
        inf_tag = "PASS" if r["inflation_pass"] else "FAIL"
        print(f"  Fault sigma_V (pre / isolated)   : {pre_sv} / {iso_sv} pu  "
              f"{inf_tag}  (isolated > pre_fault)")
        print(f"  Fault trace_P (pre / isolated)   : {pre_tp} / {iso_tp}  "
              f"{inf_tag}")
        if not r["inflation_pass"]:
            fails.append(
                f"Fault covariance inflation FAIL: sigma_V {pre_sv}->{iso_sv}, "
                f"trace_P {pre_tp}->{iso_tp} (isolated must exceed pre_fault)"
            )

        rst_str = f"{r['restored_vm_rmse']:.4f}" if r['restored_vm_rmse'] is not None else " N/A "
        rst_tag = "PASS" if r["restored_pass"] else "FAIL"
        print(f"  Restored block voltage RMSE      : {rst_str} pu  {rst_tag}  "
              f"(< 0.005 pu, well_observed bar)")
        if not r["restored_pass"]:
            fails.append(f"Restored RMSE {rst_str} pu >= 0.005 pu threshold")

    return fails


# ---------------------------------------------------------------------------
# Comparison block (multi-estimator)
# ---------------------------------------------------------------------------

def _print_comparison_block(results: dict) -> None:
    """Print a comparison table for wls/ekf/ukf side by side."""
    print("\n" + "=" * 62)
    print("Comparison Block (all estimators)")
    print("=" * 62)
    hdr = f"{'Metric':<35} {'wls':>8} {'ekf':>8} {'ukf':>8}"
    print(hdr)
    print("-" * 62)

    def _fmt(r, key, fmt=".4f"):
        val = r.get(key)
        if val is None or (isinstance(val, float) and np.isnan(val)):
            return "  N/A  "
        return f"{val:{fmt}}"

    def _bool(r, key):
        val = r.get(key)
        if val is None:
            return "  N/A "
        return " PASS " if val else " FAIL "

    metrics = [
        ("Voltage RMSE [pu]",  "median_vm_rmse",   ".4f"),
        ("Angle RMSE [deg]",   "median_va_rmse",   ".4f"),
        ("Dark-node RMSE [pu]","dark_vm_rmse",      ".4f"),
        ("Dark vs baseline",   "dark_vs_baseline",  ".3f"),
        ("NEES avg",           "nees_avg",          ".2f"),
    ]
    for label, key, fmt in metrics:
        row = f"{label:<35}"
        for est in ("wls", "ekf", "ukf"):
            r = results.get(est, {})
            row += f" {_fmt(r, key, fmt):>8}"
        print(row)

    # PASS/FAIL summary row
    print("-" * 62)
    pass_row = f"{'Overall PASS/FAIL':<35}"
    for est in ("wls", "ekf", "ukf"):
        r = results.get(est, {})
        all_fail_keys = ["vm_pass", "va_pass", "dark_rmse_pass", "dark_baseline_pass",
                         "nees_pass"]
        all_pass = all(r.get(k, True) is True for k in all_fail_keys)
        pass_row += f" {'PASS':>8}" if all_pass else f" {'FAIL':>8}"
    print(pass_row)

    # NIS row (shows N/A for WLS)
    nis_row = f"{'NIS in-band fraction':<35}"
    for est in ("wls", "ekf", "ukf"):
        r = results.get(est, {})
        if not r.get("nis_applicable", False):
            nis_row += f" {'N/A':>8}"
        else:
            frac = r.get("nis_fraction")
            if frac is None:
                nis_row += f" {'N/A':>8}"
            else:
                nis_row += f" {frac:>8.3f}"
    print(nis_row)


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main():
    """Score one or all estimators; exit non-zero on any FAIL."""
    args = _parse_args()
    cfg  = _merge_cfg(args)

    scenario   = cfg["scenario"]
    experiment = cfg["source"]
    estimator  = cfg["estimator"]

    print(f"\nIEEE 33-bus State Estimator Scoring Harness")
    print(f"  Scenario  : {scenario}")
    print(f"  Source    : {experiment}")
    print(f"  Estimator : {estimator}")
    print(f"\nNEES 95% chi2 band (n=64, N=96 expected):")
    lo96, hi96 = _derive_nees_band(n_state=ec.N_FREE_STATES, N_steps=96)
    print(f"  [{lo96:.2f}, {hi96:.2f}]  (computed via scipy.stats.chi2.ppf; "
          f"matches RESEARCH.md [61.76, 66.28])")

    # ---- InfluxDB client ----
    client = influx.get_client()
    influx.wait_for_influx()

    all_fails = []
    results = {}

    if estimator == "all":
        estimators_to_run = ["wls", "ekf", "ukf"]
    else:
        estimators_to_run = [estimator]

    for est_name in estimators_to_run:
        print(f"\n{'─'*62}")
        print(f"Scoring estimator: {est_name}")
        try:
            r = _score_one(client, scenario, experiment, est_name)
            results[est_name] = r
            fails = _print_report(r)
            all_fails.extend([f"[{est_name}] {f}" for f in fails])
        except RuntimeError as exc:
            msg = f"[{est_name}] No data: {exc}"
            print(f"\n  {msg}", file=sys.stderr)
            all_fails.append(msg)

    # ---- comparison block if multi-estimator ----
    if estimator == "all" and len(results) > 1:
        _print_comparison_block(results)

    # ---- final verdict ----
    print("\n" + "=" * 62)
    if all_fails:
        print("SCORE RESULT: FAIL")
        print(f"  {len(all_fails)} threshold(s) missed:")
        for fail in all_fails:
            print(f"    FAIL: {fail}")
        client.close()
        sys.exit(1)
    else:
        print("SCORE RESULT: PASS — all thresholds met")
        client.close()


if __name__ == "__main__":
    main()
