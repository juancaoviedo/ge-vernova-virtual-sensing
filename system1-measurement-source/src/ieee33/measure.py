"""
measure.py
----------
Config-driven measurement-layer runner for the IEEE 33-bus observability study.
Reads System 1 ground truth (either the 96-step ``state`` day or the 40-step
``fault_event`` scenario) from InfluxDB, applies a sensor model (placement +
measurement class), corrupts values with one of three seeded noise models
(gaussian / gaussian_outliers / instrument), and writes ``meas`` + topology
``event`` points to the ``measurements`` bucket.

Determinism note: a single ``np.random.default_rng(seed)`` is created in
``main()`` before the loop; no wallclock reads (no wall-clock functions,
no ``time`` module in runner logic), no legacy RNG seed API.
Iteration order is fixed: sensors iterated in sorted class order then
sorted bus_id order within each snapshot.  Two consecutive runs with
identical config produce byte-identical InfluxDB values (overwrite-in-place
keying: same measurement+tags+timestamp overwrites silently).

This module does NOT modify the ``state``, ``fault_event``, or ``profiles``
buckets owned by System 1 / Phase 8.1 — it is strictly additive.  Existing
System 1 / 8.1 Grafana dashboards are untouched.

Dependencies: numpy, influxdb-client, pandas, python-dotenv, pandapower (read-only)
Run:          uv run measure  [--scenario ...] [--source ...] [--sampling ...]
              [--noise ...] [--seed ...]
Effect:       Writes meas + event points to the InfluxDB 'measurements' bucket.
              Exits 0 on success, 1 on validation failure.
"""

import sys
import argparse
from datetime import timezone

import numpy as np
from influxdb_client.client.write_api import SYNCHRONOUS

from ieee33 import config
from ieee33 import influx
from ieee33 import measure_config as mc
from ieee33.network import build_enhanced_33bus


# ---------------------------------------------------------------------------
# Instrument noise model helpers (D-13)
# ---------------------------------------------------------------------------

class InstrumentState:
    """Persistent per-sensor AR(1) state for the instrument noise model (D-13).

    Holds the rho coefficient and a per-sensor memory of the previous AR(1)
    term.  A single instance is created in main() before the step loop and
    passed into apply_noise on every call.

    AR(1) recursion:
        white = rng.normal(0, true_sigma * sqrt(1 - rho^2))
        ar1   = rho * prev[sensor_key] + white
    This gives a stationary process with std ≈ true_sigma and lag-1
    autocorrelation ≈ rho.  The sqrt(1-rho^2) scaling preserves the
    marginal variance equal to true_sigma^2.

    Attributes:
        rho (float): AR(1) coefficient (D-13: 0.7).
        _ar_prev (dict): {sensor_key: float} — previous AR(1) term per sensor.
    """

    def __init__(self, rho: float = 0.7) -> None:
        self.rho = rho
        self._ar_prev: dict[str, float] = {}

    def ar1_term(self, sensor_key: str, true_sigma: float, rng) -> float:
        """Return the AR(1) noise component for this sensor, update prev state.

        Args:
            sensor_key: Unique string key for this sensor (e.g. "scada_0_vm_pu").
            true_sigma: True noise std for this reading (used for white noise).
            rng:        The seeded numpy Generator (single instance for the run).

        Returns:
            Float AR(1) noise sample.  Internally updates _ar_prev[sensor_key].
        """
        white = rng.normal(0.0, true_sigma * (1.0 - self.rho ** 2) ** 0.5)
        prev  = self._ar_prev.get(sensor_key, 0.0)
        ar1   = self.rho * prev + white
        self._ar_prev[sensor_key] = ar1
        return ar1


def _instrument_bias(sensor_key: str, seed: int) -> float:
    """Return a deterministic per-sensor fixed bias (D-13 INSTRUMENT_BIAS_SCALE).

    Derives a unique bias for each sensor from a hash of (sensor_key, seed).
    This makes the bias:
      - Fixed for a given sensor across all steps (systematic error)
      - Reproducible: same (sensor_key, seed) always returns same float
      - Independent across sensors: different keys → different biases

    The bias is applied as: raw = true_val + bias * abs(true_val)
    so it represents a fractional systematic error (~+0.5% of value).

    Args:
        sensor_key: Unique string key for this sensor (e.g. "scada_0_vm_pu").
        seed:       The experiment seed from cfg["seed"].

    Returns:
        Float bias coefficient (D-13: drawn from N(0, INSTRUMENT_BIAS_SCALE)).
    """
    bias_rng = np.random.default_rng(hash((sensor_key, seed)) & 0xFFFFFFFF)
    return bias_rng.normal(0.0, mc.INSTRUMENT_BIAS_SCALE)


def apply_noise(
    noise_model: str,
    cls: str,
    bus: int,
    quantity: str,
    true_val: float,
    true_sigma: float,
    rng,
    instr_state: InstrumentState,
    seed: int,
) -> float:
    """Apply the selected noise model and return the noisy measurement value.

    Dispatches to one of three models (D-12, D-13):
      - "gaussian":           additive white Gaussian noise, zero mean, std=true_sigma
      - "gaussian_outliers":  gaussian base + gross errors on fraction f=OUTLIER_FRACTION
                              of measurements at magnitude OUTLIER_SPIKE_MULT*sigma
      - "instrument":         per-sensor fixed bias + AR(1) temporal correlation +
                              quantization to the per-class LSB grid

    IMPORTANT — RNG draw order (Pitfall 5 / T-09-09):
      Each model draws from rng in a fixed sequence per call.  The caller
      iterates sensors in sorted(class) then sorted(bus_id) order so that the
      RNG stream is deterministic across runs with the same seed.  apply_noise
      ALWAYS draws from rng in the same order for a given model:
        - gaussian:          one draw (normal)
        - gaussian_outliers: two draws (normal + random) or two draws (normal + choice)
        - instrument:        one draw inside ar1_term (normal) — bias RNG is independent

    The assumed_sigma (the σ the estimator uses) is computed by the CALLER as
    true_sigma * cfg["assumed_sigma_scale"] and written to the meas Point as a
    separate field.  It is NEVER fed into this function (SPEC R9 / D-06).

    Args:
        noise_model:  "gaussian" | "gaussian_outliers" | "instrument"
        cls:          Measurement class (e.g. "scada", "pmu")
        bus:          Bus id (int)
        quantity:     Quantity name (e.g. "vm_pu", "p_inj_mw")
        true_val:     Ground-truth value
        true_sigma:   True noise std (fraction × |value| for most classes;
                      absolute for pmu va_degree)
        rng:          Seeded numpy Generator (single instance for the run)
        instr_state:  InstrumentState holding AR(1) prev per sensor (for "instrument")
        seed:         Experiment seed (for per-sensor bias derivation)

    Returns:
        Noisy float measurement value.
    """
    if noise_model == "gaussian":
        noise = rng.normal(0.0, true_sigma) if true_sigma > 0.0 else 0.0
        return true_val + noise

    elif noise_model == "gaussian_outliers":
        # Base gaussian draw (always happens to keep RNG stream consistent)
        noise = rng.normal(0.0, true_sigma) if true_sigma > 0.0 else 0.0
        # D-12: replace noise with gross error on OUTLIER_FRACTION of measurements
        if rng.random() < mc.OUTLIER_FRACTION:
            sign = rng.choice([-1.0, 1.0])
            noise = sign * mc.OUTLIER_SPIKE_MULT * true_sigma
        return true_val + noise

    elif noise_model == "instrument":
        # D-13: per-sensor fixed bias + AR(1) temporal correlation + quantization
        sensor_key = f"{cls}_{bus}_{quantity}"
        bias       = _instrument_bias(sensor_key, seed)
        ar1        = instr_state.ar1_term(sensor_key, true_sigma, rng)
        raw        = true_val + bias * abs(true_val) + ar1
        lsb        = mc.QUANT_LSB[cls][quantity]
        quantized  = round(raw / lsb) * lsb
        return quantized

    else:
        raise ValueError(
            f"apply_noise: unknown noise_model '{noise_model}'. "
            "Expected 'gaussian', 'gaussian_outliers', or 'instrument'."
        )


# ---------------------------------------------------------------------------
# CLI argument parsing (D-09: config file is primary; CLI overrides for sweeps)
# ---------------------------------------------------------------------------

def _parse_args():
    """Parse optional CLI overrides for the five experiment knobs (D-09)."""
    p = argparse.ArgumentParser(
        description="IEEE 33-bus measurement layer runner — reads ground truth, "
                    "applies sensor model + noise, writes measurements bucket."
    )
    p.add_argument(
        "--scenario",
        choices=["well_observed", "realistic_sparse"],
        default=None,
        help="Sensor-placement scenario (default: measure_config.ACTIVE['scenario'])",
    )
    p.add_argument(
        "--source",
        choices=["day", "fault"],
        default=None,
        help="Ground-truth source: 'day' = 96-step state bucket, "
             "'fault' = 40-step fault_event bucket "
             "(default: measure_config.ACTIVE['source'])",
    )
    p.add_argument(
        "--sampling",
        choices=["snapshot", "multirate_async"],
        default=None,
        help="Sampling mode: 'snapshot' = all classes every step "
             "(default: measure_config.ACTIVE['sampling'])",
    )
    p.add_argument(
        "--noise",
        choices=["gaussian", "gaussian_outliers", "instrument"],
        default=None,
        help="Noise model (default: measure_config.ACTIVE['noise'])",
    )
    p.add_argument(
        "--seed",
        type=int,
        default=None,
        help="RNG seed for deterministic noise (default: measure_config.ACTIVE['seed'])",
    )
    return p.parse_args()


def _merge_cfg(args) -> dict:
    """Merge measure_config.ACTIVE with non-None CLI overrides.

    Config file (ACTIVE block) is the primary switch (D-09).  CLI overrides
    are applied on top for sweep runs.

    Args:
        args: Parsed argparse.Namespace from _parse_args().

    Returns:
        cfg dict with keys: scenario, source, sampling, noise, seed,
        assumed_sigma_scale.
    """
    cfg = dict(mc.ACTIVE)   # start from the config file
    for key in ("scenario", "source", "sampling", "noise", "seed"):
        val = getattr(args, key)
        if val is not None:
            cfg[key] = val   # CLI overrides file value
    return cfg


# ---------------------------------------------------------------------------
# Day-source lookup builder (source=day)
# ---------------------------------------------------------------------------

def _build_day_lookup(client, base_p_by_bus: dict, base_q_by_bus: dict):
    """Build per-(step, bus) true-value lookup for source=day.

    Reads three data sources:
      - read_state_bus  → vm_pu, va_degree per (step, bus)
      - read_state_sgen → p_mw, q_mvar per (step, sgen_id); used to build
                          sgen_lookup keyed (step, bus)
      - read_profiles   → load_pu, solar_pu, wind_pu per step; load_pu drives
                          the P_inj derivation

    P_inj derivation for source=day (Pitfall 6 — state bucket bus has only
    vm_pu/va_degree; no p_mw/q_mvar on bus points):
      load_p[bus] = base_p_by_bus[bus] * load_pu(step)  (0.0 if bus has no load)
      sgen_p[bus] = sum of p_mw for sgens at this bus at this step  (0.0 if none)
      P_inj[bus]  = load_p[bus] - sgen_p[bus]
    Sign convention: positive P_inj = net load consumption (matching fault_event
    res_bus convention: positive = net consumption).

    Args:
        client:          Active InfluxDBClient.
        base_p_by_bus:   dict {bus_id (int): base_p_mw (float)} from net.load.
        base_q_by_bus:   dict {bus_id (int): base_q_mvar (float)} from net.load.

    Returns:
        Tuple (timestamps, lookup, sgen_lookup):
          timestamps:   sorted list of UTC-aware datetimes (96 steps)
          lookup:       dict {(step_idx, bus_id): {vm_pu, va_degree,
                        p_inj_mw, q_inj_mvar}}
          sgen_lookup:  dict {(step_idx, bus_id): {p_mw, q_mvar}}
    """
    print("  Reading state bus data (vm_pu / va_degree) ...")
    bus_df = influx.read_state_bus(client).sort_values(["_time", "bus_id"]).reset_index(drop=True)

    print("  Reading state sgen data (p_mw / q_mvar) ...")
    sgen_df = influx.read_state_sgen(client).sort_values(["_time", "sgen_id"]).reset_index(drop=True)

    print("  Reading 96-step profiles (load_pu / solar_pu / wind_pu) ...")
    prof_df = influx.read_profiles(client).sort_values("_time").reset_index(drop=True)

    # ---- build sgen_id → bus_id map from the network (read-only) ----
    # This is called AFTER build_enhanced_33bus() in main(); re-use the same
    # mapping from config constants to avoid a second network build here.
    # sgen 0→bus 17, 1→bus 21, 2→bus 24, 3→bus 32 (verified via build_enhanced_33bus output).
    # We build the map directly from the global net built in main() — it is passed
    # in via the closure on base_p/q; here we read it from config constants instead.
    # SOLAR_BUSES = [17, 21]; WIND_BUSES = [24, 32]; sgen order follows config.
    # Map: sgen index → bus (0-indexed pandapower ids)
    _sgen_bus_map = {0: 17, 1: 21, 2: 24, 3: 32}   # matches build_enhanced_33bus sgen order

    # ---- sorted unique timestamps = the 96 step anchors ----
    timestamps_raw = sorted(bus_df["_time"].unique())
    timestamps = []
    for ts in timestamps_raw:
        if hasattr(ts, "to_pydatetime"):
            ts = ts.to_pydatetime()
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
        timestamps.append(ts)

    assert len(timestamps) == config.N_STEPS, (
        f"_build_day_lookup: expected {config.N_STEPS} bus timestamps, "
        f"got {len(timestamps)}. Run 'uv run sim' first."
    )

    # ---- build sgen_lookup: (step_idx, bus_id) → {p_mw, q_mvar} ----
    # sgen_id in the DataFrame is the string form of the pandapower sgen index.
    sgen_lookup: dict = {}
    sgen_ts_list = sorted(sgen_df["_time"].unique())
    for step_idx, ts_raw in enumerate(sgen_ts_list):
        snap = sgen_df[sgen_df["_time"] == ts_raw]
        for _, row in snap.iterrows():
            sgen_idx = int(row["sgen_id"])
            bus_id = _sgen_bus_map.get(sgen_idx)
            if bus_id is None:
                continue
            p_mw = float(row["p_mw"])
            q_mvar = float(row["q_mvar"])
            # Multiple sgens at the same bus would be summed; not the case here.
            if (step_idx, bus_id) not in sgen_lookup:
                sgen_lookup[(step_idx, bus_id)] = {"p_mw": 0.0, "q_mvar": 0.0}
            sgen_lookup[(step_idx, bus_id)]["p_mw"]   += p_mw
            sgen_lookup[(step_idx, bus_id)]["q_mvar"] += q_mvar

    # ---- build main lookup: (step_idx, bus_id) → {vm_pu, va_degree, p_inj_mw, q_inj_mvar} ----
    lookup: dict = {}
    bus_ts_list = sorted(bus_df["_time"].unique())
    for step_idx, ts_raw in enumerate(bus_ts_list):
        # load_pu for this step
        load_pu = float(prof_df.iloc[step_idx]["load_pu"])

        snap = bus_df[bus_df["_time"] == ts_raw]
        for _, row in snap.iterrows():
            bus_id = int(row["bus_id"])
            vm_pu    = float(row["vm_pu"])
            va_degree = float(row["va_degree"])

            # P_inj derivation (Pitfall 6 — no per-bus power in state bucket)
            # load_p[bus] = base_p_by_bus.get(bus, 0.0) * load_pu
            # sgen_p[bus] = sgen_lookup.get((step, bus), {}).get("p_mw", 0.0)
            # P_inj[bus]  = load_p - sgen_p  (positive = net consumption)
            base_p = base_p_by_bus.get(bus_id, 0.0)
            base_q = base_q_by_bus.get(bus_id, 0.0)
            load_p = base_p * load_pu
            load_q = base_q * load_pu
            sgen_entry = sgen_lookup.get((step_idx, bus_id), {})
            sgen_p = sgen_entry.get("p_mw",   0.0)
            sgen_q = sgen_entry.get("q_mvar", 0.0)
            p_inj_mw   = load_p - sgen_p
            q_inj_mvar = load_q - sgen_q

            lookup[(step_idx, bus_id)] = {
                "vm_pu":      vm_pu,
                "va_degree":  va_degree,
                "p_inj_mw":   p_inj_mw,
                "q_inj_mvar": q_inj_mvar,
            }

    n_expected = config.N_STEPS * 33   # 33 buses × 96 steps
    n_got = len(lookup)
    if n_got != n_expected:
        print(
            f"  WARNING: day lookup has {n_got} entries; expected {n_expected} "
            f"({config.N_STEPS} steps × 33 buses)."
        )

    return timestamps, lookup, sgen_lookup


# ---------------------------------------------------------------------------
# Fault-source lookup builder (source=fault)
# ---------------------------------------------------------------------------

def _build_fault_lookup(client):
    """Build per-(step, bus) true-value lookup for source=fault.

    Reads three data sources from the fault_event bucket:
      - read_fault_bus   → vm_pu, va_degree, p_mw, q_mvar, energised per (step, bus)
      - read_fault_sgen  → p_mw, q_mvar, energised per (step, sgen_id)
      - read_fault_event → phase, topology metadata per step

    P_inj for source=fault: use p_mw / q_mvar DIRECTLY from fault_event bus
    (pandapower res_bus convention: positive = net consumption/load).
    Sign convention documented here to match: positive = net consumption.

    energised is a STRING tag ("1" / "0") — compare as str, never as int.

    Args:
        client: Active InfluxDBClient.

    Returns:
        Tuple (timestamps, lookup, sgen_lookup, energised_by_step_bus, event_by_step):
          timestamps:            sorted list of UTC-aware datetimes (40 steps)
          lookup:                dict {(step_idx, bus_id): {vm_pu, va_degree,
                                 p_inj_mw, q_inj_mvar}}
          sgen_lookup:           dict {(step_idx, bus_id): {p_mw, q_mvar}}
          energised_by_step_bus: dict {(step_idx, bus_id): "1" or "0"}
          event_by_step:         dict {step_idx: {phase, faulted_line_id, tie_closed,
                                 tie_id, n_dead_buses, dead_buses}}
    """
    print("  Reading fault_event bus data ...")
    bus_df = influx.read_fault_bus(client).sort_values(["_time", "bus_id"]).reset_index(drop=True)

    print("  Reading fault_event sgen data ...")
    sgen_df = influx.read_fault_sgen(client).sort_values(["_time", "sgen_id"]).reset_index(drop=True)

    print("  Reading fault_event topology (event measurement) ...")
    event_df = influx.read_fault_event(client).sort_values("_time").reset_index(drop=True)

    _sgen_bus_map = {0: 17, 1: 21, 2: 24, 3: 32}

    # ---- sorted unique timestamps ----
    timestamps_raw = sorted(bus_df["_time"].unique())
    timestamps = []
    for ts in timestamps_raw:
        if hasattr(ts, "to_pydatetime"):
            ts = ts.to_pydatetime()
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
        timestamps.append(ts)

    assert len(timestamps) == config.FAULT_N_STEPS, (
        f"_build_fault_lookup: expected {config.FAULT_N_STEPS} bus timestamps, "
        f"got {len(timestamps)}. Run 'uv run fault-sim' first."
    )

    # ---- sgen_lookup and energised_by_step_bus from bus + sgen DataFrames ----
    sgen_lookup: dict = {}
    sgen_ts_list = sorted(sgen_df["_time"].unique())
    for step_idx, ts_raw in enumerate(sgen_ts_list):
        snap = sgen_df[sgen_df["_time"] == ts_raw]
        for _, row in snap.iterrows():
            sgen_idx = int(row["sgen_id"])
            bus_id = _sgen_bus_map.get(sgen_idx)
            if bus_id is None:
                continue
            if (step_idx, bus_id) not in sgen_lookup:
                sgen_lookup[(step_idx, bus_id)] = {"p_mw": 0.0, "q_mvar": 0.0}
            sgen_lookup[(step_idx, bus_id)]["p_mw"]   += float(row["p_mw"])
            sgen_lookup[(step_idx, bus_id)]["q_mvar"] += float(row["q_mvar"])

    lookup: dict = {}
    energised_by_step_bus: dict = {}
    bus_ts_list = sorted(bus_df["_time"].unique())
    for step_idx, ts_raw in enumerate(bus_ts_list):
        snap = bus_df[bus_df["_time"] == ts_raw]
        for _, row in snap.iterrows():
            bus_id   = int(row["bus_id"])
            energised = str(row["energised"])   # D-02: always string "1"/"0"
            vm_pu    = float(row["vm_pu"])
            va_degree = float(row["va_degree"])
            # P_inj for source=fault: use p_mw/q_mvar directly from res_bus
            # (pandapower convention: positive = net consumption; matches sign used for day)
            p_inj_mw   = float(row["p_mw"])
            q_inj_mvar = float(row["q_mvar"])

            lookup[(step_idx, bus_id)] = {
                "vm_pu":      vm_pu,
                "va_degree":  va_degree,
                "p_inj_mw":   p_inj_mw,
                "q_inj_mvar": q_inj_mvar,
            }
            energised_by_step_bus[(step_idx, bus_id)] = energised

    # ---- event_by_step from event DataFrame ----
    event_by_step: dict = {}
    event_ts_list = sorted(event_df["_time"].unique())
    for step_idx, ts_raw in enumerate(event_ts_list):
        snap = event_df[event_df["_time"] == ts_raw]
        if len(snap) == 0:
            continue
        row = snap.iloc[0]
        event_by_step[step_idx] = {
            "phase":           str(row["phase"]),
            "faulted_line_id": int(row["faulted_line_id"]),
            "tie_closed":      int(row["tie_closed"]),
            "tie_id":          int(row["tie_id"]),
            "n_dead_buses":    int(row["n_dead_buses"]),
            "dead_buses":      str(row["dead_buses"]),
        }

    return timestamps, lookup, sgen_lookup, energised_by_step_bus, event_by_step


# ---------------------------------------------------------------------------
# True-value extractor
# ---------------------------------------------------------------------------

def get_true_value(
    cls: str,
    quantity: str,
    step_idx: int,
    bus_id: int,
    lookup: dict,
    sgen_lookup: dict,
) -> float:
    """Return the ground-truth scalar for a given class + quantity at (step, bus).

    Mapping:
      scada  : vm_pu → lookup vm_pu
               p_inj_mw / q_inj_mvar → lookup p_inj_mw / q_inj_mvar
      pmu    : vm_pu → lookup vm_pu
               va_degree → lookup va_degree
      ami    : p_inj_mw / q_inj_mvar → lookup p_inj_mw / q_inj_mvar
      der    : p_mw → sgen_lookup p_mw (DER output, not net injection)
               q_mvar → sgen_lookup q_mvar
      pseudo : p_inj_mw / q_inj_mvar → lookup p_inj_mw / q_inj_mvar
      zero_inj: p_inj_mw / q_inj_mvar → 0.0 (virtual zero-injection; P≈Q≈0)

    Args:
        cls:        Measurement class string.
        quantity:   Quantity string (e.g., "vm_pu", "p_inj_mw").
        step_idx:   Step index (0-based).
        bus_id:     Pandapower bus index (int).
        lookup:     {(step_idx, bus_id): {vm_pu, va_degree, p_inj_mw, q_inj_mvar}}
        sgen_lookup:{(step_idx, bus_id): {p_mw, q_mvar}}

    Returns:
        Float ground-truth value.

    Raises:
        KeyError: If (step_idx, bus_id) is not in the relevant lookup.
        ValueError: If cls/quantity combination is not recognized.
    """
    if cls == "zero_inj":
        # Virtual zero-injection: true value is 0.0 by definition (near-zero
        # junction bus with no load; P=0, Q=0 high-weight virtual measurement).
        if quantity in ("p_inj_mw", "q_inj_mvar"):
            return 0.0
        raise ValueError(f"get_true_value: zero_inj has no quantity '{quantity}'")

    if cls == "der":
        # DER class reads sgen output (not net injection)
        if quantity in ("p_mw", "q_mvar"):
            entry = sgen_lookup.get((step_idx, bus_id), {"p_mw": 0.0, "q_mvar": 0.0})
            return entry[quantity]
        raise ValueError(f"get_true_value: der has no quantity '{quantity}'")

    # All other classes (scada, pmu, ami, pseudo) use the main lookup
    entry = lookup[(step_idx, bus_id)]
    if quantity == "vm_pu":
        if cls in ("scada", "pmu"):
            return entry["vm_pu"]
        raise ValueError(f"get_true_value: class '{cls}' does not emit vm_pu")
    elif quantity == "va_degree":
        if cls == "pmu":
            return entry["va_degree"]
        raise ValueError(f"get_true_value: class '{cls}' does not emit va_degree")
    elif quantity == "p_inj_mw":
        if cls in ("scada", "ami", "pseudo"):
            return entry["p_inj_mw"]
        raise ValueError(f"get_true_value: class '{cls}' does not emit p_inj_mw")
    elif quantity == "q_inj_mvar":
        if cls in ("scada", "ami", "pseudo"):
            return entry["q_inj_mvar"]
        raise ValueError(f"get_true_value: class '{cls}' does not emit q_inj_mvar")
    else:
        raise ValueError(
            f"get_true_value: unknown quantity '{quantity}' for class '{cls}'"
        )


# ---------------------------------------------------------------------------
# Pseudo-bus helper
# ---------------------------------------------------------------------------

def _pseudo_buses(scenario: str, load_bus_set: set) -> list:
    """Return sorted list of load buses NOT covered by any real sensor class.

    Pseudo class = every bus in load_bus_set that does not appear in
    SCENARIOS[scenario] under scada/pmu/ami/der/zero_inj.

    Args:
        scenario:     Scenario name ("well_observed" | "realistic_sparse").
        load_bus_set: Set of bus ids that carry a load (from net.load["bus"]).

    Returns:
        Sorted list of pseudo bus ids.
    """
    scenario_def = mc.SCENARIOS[scenario]
    covered: set = set()
    for cls_key in ("scada", "pmu", "ami", "der", "zero_inj"):
        covered.update(scenario_def.get(cls_key, []))
    return sorted(load_bus_set - covered)


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """Measurement runner: read ground truth, select sensors, apply noise, write measurements bucket."""

    # ---- parse CLI + merge with config file ----
    args = _parse_args()
    cfg  = _merge_cfg(args)

    print("IEEE 33-bus measurement layer")
    print("=" * 62)
    print(f"Resolved configuration:")
    print(f"  scenario          : {cfg['scenario']}")
    print(f"  source            : {cfg['source']}")
    print(f"  sampling          : {cfg['sampling']}")
    print(f"  noise             : {cfg['noise']}")
    print(f"  seed              : {cfg['seed']}")
    print(f"  assumed_sigma_scale: {cfg['assumed_sigma_scale']}")

    # ---- build network (read-only) to capture base loads by bus ----
    print("\nBuilding enhanced IEEE 33-bus network (read-only, no power flow) ...")
    net, _ = build_enhanced_33bus()
    # Map pandapower load bus index → base load (MW/MVAr)
    base_p_by_bus = dict(zip(
        net.load["bus"].astype(int),
        net.load["p_mw"].astype(float),
    ))
    base_q_by_bus = dict(zip(
        net.load["bus"].astype(int),
        net.load["q_mvar"].astype(float),
    ))
    # Buses with a load (used to derive pseudo set)
    load_bus_set = set(int(b) for b in net.load["bus"])
    n_load_buses = len(load_bus_set)
    print(f"  Load buses: {n_load_buses}  (ids: {sorted(load_bus_set)[:8]}...)")

    # ---- connect to InfluxDB + ensure measurements bucket ----
    print(f"\nConnecting to InfluxDB at {config.INFLUXDB_URL} ...")
    client = influx.get_client()
    influx.wait_for_influx()
    influx.ensure_bucket(client, mc.MEASUREMENTS_BUCKET)

    # ---- read ground truth from the selected source ----
    print(f"\nReading ground-truth data (source={cfg['source']}) ...")
    if cfg["source"] == "day":
        timestamps, lookup, sgen_lookup = _build_day_lookup(
            client, base_p_by_bus, base_q_by_bus
        )
        # For day source: all 33 buses are always energised (no energised tag in state bucket)
        energised_by_step_bus = None
        event_by_step        = None
        n_steps = len(timestamps)
    else:  # fault
        timestamps, lookup, sgen_lookup, energised_by_step_bus, event_by_step = (
            _build_fault_lookup(client)
        )
        n_steps = len(timestamps)

    print(f"  Ground truth loaded: {n_steps} snapshots, "
          f"{len(lookup)} bus-step entries, "
          f"{len(sgen_lookup)} sgen-step entries")

    # ---- compute pseudo bus list for this scenario ----
    pseudo_bus_list = _pseudo_buses(cfg["scenario"], load_bus_set)
    scenario_def    = mc.SCENARIOS[cfg["scenario"]]

    # ---- determine sorted real class list for this scenario ----
    real_classes = sorted(
        cls for cls in ("scada", "pmu", "ami", "der", "zero_inj")
        if scenario_def.get(cls)   # only classes with at least one assigned bus
    )

    # ---- single seeded RNG (D-10, Pitfall 5: created once, before the loop) ----
    rng = np.random.default_rng(cfg["seed"])

    # ---- instrument noise state (single instance, persistent across steps) ----
    instr_state = InstrumentState(mc.INSTRUMENT_AR1_RHO)

    # ---- write API (SYNCHRONOUS — prevents silent background-thread failures) ----
    write_api = client.write_api(write_options=SYNCHRONOUS)
    issues: list[str] = []

    # ---- accumulate per-class point counts for footprint report (Plan 04 expands) ----
    class_counts: dict[str, int] = {cls: 0 for cls in real_classes + ["pseudo", "zero_inj"]}

    # ---- console table header (mirrors fault_sim.py lines 334-338) ----
    print(
        f"\n{'Step':>4}  {'UTC Time':<20}  {'Real':>5}  {'Pseudo':>7}  "
        f"{'Dead':>5}  {'Pts':>6}"
    )
    print("-" * 62)

    # ---- per-snapshot loop ----
    for step_idx, ts in enumerate(timestamps):
        experiment = "day" if cfg["source"] == "day" else "fault"

        # -- determine live/dead bus sets --
        if cfg["source"] == "fault":
            # For fault source: use energised tag from fault_event (D-02)
            # D-02/D-03 energised gate: energised == "1" means live; anything
            # else (energised == "0") means dead — skip all measurements.
            live_bus_ids = {
                bus_id
                for (si, bus_id), eng in energised_by_step_bus.items()
                if si == step_idx and eng == "1"
            }
            dead_bus_ids = set(range(33)) - live_bus_ids
            phase = event_by_step[step_idx]["phase"] if event_by_step else None
        else:
            # For day source: all 33 buses are always energised
            dead_bus_ids = set()
            live_bus_ids = set(range(33))
            phase = None

        n_dead = len(dead_bus_ids)

        # -- cadence mode is checked per class inside the sensor loop below (D-14) --
        # In multirate_async mode each class is gated by step_idx % CADENCE[experiment][cls] != 0.
        # In snapshot mode all classes emit every step (gate is bypassed).
        _multirate = cfg["sampling"] == "multirate_async"

        # -- sensor iteration: sorted class order, sorted bus order (Pitfall 5: determinism) --
        points = []
        n_live_real = 0
        n_pseudo    = 0

        for cls in real_classes:
            # D-14 multirate cadence gate: skip this class at steps where it doesn't report
            if _multirate and step_idx % mc.CADENCE[experiment][cls] != 0:
                continue

            cls_quantities = list(mc.CLASS_SIGMA[cls].keys())
            assigned_buses = sorted(scenario_def.get(cls, []))
            for bus_id in assigned_buses:
                # D-03 energised gate: skip dead buses entirely (no measurement, no pseudo)
                if bus_id in dead_bus_ids:
                    continue
                # Verify bus-step entry exists; log issue and skip on KeyError
                for quantity in cls_quantities:
                    try:
                        true_val = get_true_value(
                            cls, quantity, step_idx, bus_id, lookup, sgen_lookup
                        )
                    except KeyError:
                        issues.append(
                            f"step {step_idx:02d}: missing lookup entry for "
                            f"cls={cls} qty={quantity} bus={bus_id}"
                        )
                        continue
                    except ValueError as ve:
                        issues.append(f"step {step_idx:02d}: {ve}")
                        continue

                    # Compute true sigma (fraction of |value| except pmu va_degree = absolute)
                    base_sigma = mc.CLASS_SIGMA[cls][quantity]
                    if cls == "pmu" and quantity == "va_degree":
                        true_sigma = base_sigma   # absolute radians (D-11: GPS-disciplined)
                    else:
                        true_sigma = base_sigma * abs(true_val)

                    assumed_sigma = true_sigma * cfg["assumed_sigma_scale"]

                    # Full three-model noise engine (D-12, D-13)
                    # assumed_sigma is kept separate — never fed into noise generation (SPEC R9)
                    value = apply_noise(
                        cfg["noise"], cls, bus_id, quantity,
                        true_val, true_sigma, rng, instr_state, cfg["seed"],
                    )

                    points.append(
                        influx.build_meas_point(
                            cls, quantity, str(bus_id),
                            cfg["scenario"], experiment, value, assumed_sigma, ts,
                            phase=phase,
                        )
                    )
                    n_live_real += 1
                    class_counts[cls] = class_counts.get(cls, 0) + 1

        # -- pseudo class: load buses not covered by any real class --
        # D-14: pseudo cadence = 1 for both day and fault (always emit)
        for bus_id in pseudo_bus_list:
            if bus_id in dead_bus_ids:
                continue   # D-03: no pseudo for dead bus
            for quantity in ("p_inj_mw", "q_inj_mvar"):
                try:
                    true_val = get_true_value(
                        "pseudo", quantity, step_idx, bus_id, lookup, sgen_lookup
                    )
                except KeyError:
                    issues.append(
                        f"step {step_idx:02d}: missing lookup entry for "
                        f"cls=pseudo qty={quantity} bus={bus_id}"
                    )
                    continue

                base_sigma = mc.CLASS_SIGMA["pseudo"][quantity]
                true_sigma = base_sigma * abs(true_val)
                assumed_sigma = true_sigma * cfg["assumed_sigma_scale"]

                # Full three-model noise engine — applies to pseudo class too
                value = apply_noise(
                    cfg["noise"], "pseudo", bus_id, quantity,
                    true_val, true_sigma, rng, instr_state, cfg["seed"],
                )

                points.append(
                    influx.build_meas_point(
                        "pseudo", quantity, str(bus_id),
                        cfg["scenario"], experiment, value, assumed_sigma, ts,
                        phase=phase,
                    )
                )
                n_pseudo += 1
                class_counts["pseudo"] = class_counts.get("pseudo", 0) + 1

        # -- TODO(Plan 04): topology event re-publish (build_event_point + append to points) --

        # -- write all points for this snapshot --
        if points:
            influx.write_meas_points(write_api, points, bucket=mc.MEASUREMENTS_BUCKET)

        # -- console row (mirrors fault_sim.py D-18 style) --
        n_pts = len(points)
        print(
            f"{step_idx:>4}  {str(ts)[:19]:<20}  {n_live_real:>5}  "
            f"{n_pseudo:>7}  {n_dead:>5}  {n_pts:>6}"
        )

    # ---- fail-loud gate (copy fault_sim.py lines 575-582 verbatim) ----
    if issues:
        print("--- SIM VALIDATION FAILED ---", file=sys.stderr)
        for issue in issues:
            print(f"  {issue}", file=sys.stderr)
        client.close()
        sys.exit(1)

    # ---- success summary ----
    total_real   = sum(v for k, v in class_counts.items() if k != "pseudo")
    total_pseudo = class_counts.get("pseudo", 0)
    total_pts    = total_real + total_pseudo
    print("\n" + "=" * 62)
    print(f"measure OK — {total_pts:,} points written to bucket '{mc.MEASUREMENTS_BUCKET}'")
    print(f"  scenario={cfg['scenario']}  source={cfg['source']}  "
          f"sampling={cfg['sampling']}  noise={cfg['noise']}  seed={cfg['seed']}")
    print(f"  real measurements : {total_real:,}")
    print(f"  pseudo measurements: {total_pseudo:,}")
    print(
        "\n  NOTE: footprint redundancy report, topology event re-publish, "
        "and multirate cadence gate are added in Plan 04."
    )

    client.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nFATAL: {exc}", file=sys.stderr)
        sys.exit(1)
