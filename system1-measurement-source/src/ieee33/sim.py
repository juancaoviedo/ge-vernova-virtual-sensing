"""
sim.py
------
Deterministic 96-step quasi-static power-flow driver for the enhanced IEEE 33-bus
DER measurement source.  Reads the day's solar/wind/load profiles from InfluxDB
ONCE at startup (no profile network fetch at runtime — SPEC-4), then sweeps all
96 steps, runs Newton-Raphson with OLTC regulation, captures the complete
ground-truth state per step, and persists every snapshot to the InfluxDB 'state'
bucket with the real OPSD UTC datetime as the timestamp.

Determinism note: fixed TARGET_DATE + fixed profiles (read from InfluxDB) +
deterministic Newton-Raphson (no np.random, no datetime.now(), no time.time())
→ identical 96 snapshots on every run.  Re-running overwrites points at the same
timestamp+tag keys (D-08, D-16).

Dependencies: pandapower, influxdb-client, pandas, numpy, python-dotenv
Run:          uv run sim
Effect:       Writes 96 full-state power-flow snapshots to InfluxDB 'state' bucket
              for TARGET_DATE.  Exits 0 on success, 1 on validation failure.
"""

import sys
from datetime import timezone

import pandapower as pp
from influxdb_client.client.write_api import SYNCHRONOUS

from ieee33 import config
from ieee33 import influx
from ieee33.network import build_enhanced_33bus


# ---------------------------------------------------------------------------
# Per-step runner
# ---------------------------------------------------------------------------

def run_step(net, trafo_idx, base_p, base_q, load_pu, solar_pu, wind_pu, forced_tap=None) -> dict:
    """Scale loads and DGs, run power flow with OLTC, return full state dict.

    Args:
        net:       pandapowerNet (modified in-place; call with the same net each step).
        trafo_idx: integer index of the OLTC transformer in net.trafo.
        base_p:    numpy array of base active load values (MW) — captured once at startup.
        base_q:    numpy array of base reactive load values (MVAr).
        load_pu:   float in [0, 1] — load profile scaling factor for this step.
        solar_pu:  float in [0, 1] — solar capacity-factor for this step.
        wind_pu:   float in [0, 1] — wind capacity-factor for this step.
        forced_tap: optional int — if set, the OLTC tap is PINNED to this position and the
                   line-drop controller is disabled for this step (a configured disturbance
                   event). If None, the controller regulates normally (run_control=True).

    Returns:
        dict with keys:
          res_bus, res_line_inservice, res_sgen, res_ext_grid, res_trafo,
          tap_pos, shift_degree, system_dict.
    """
    # ---- scale loads ----
    net.load["p_mw"]   = base_p * load_pu
    net.load["q_mvar"] = base_q * load_pu

    # ---- set DG by profile × nameplate ----
    solar_mask = net.sgen["type"] == "PV"
    net.sgen.loc[solar_mask, "p_mw"] = (
        net.sgen.loc[solar_mask, "p_mw_nameplate"] * solar_pu
    )
    wind_mask = net.sgen["type"] == "WP"
    net.sgen.loc[wind_mask, "p_mw"] = (
        net.sgen.loc[wind_mask, "p_mw_nameplate"] * wind_pu
    )

    # ---- power flow ----
    # Normal step: run_control=True lets FeederTapControl regulate the OLTC.
    # Disturbance event: pin the tap to forced_tap and disable control for this step,
    # injecting a sharp voltage discontinuity into the ground truth.
    if forced_tap is not None:
        net.trafo.at[trafo_idx, "tap_pos"] = int(forced_tap)
        pp.runpp(net, algorithm="nr", calculate_voltage_angles=True, run_control=False)
    else:
        pp.runpp(net, algorithm="nr", calculate_voltage_angles=True, run_control=True)

    # ---- read tap/shift from net.trafo (NOT res_trafo — Pitfall 6) ----
    tap_pos      = int(net.trafo.at[trafo_idx, "tap_pos"])
    shift_degree = float(net.trafo.at[trafo_idx, "shift_degree"])

    # ---- in-service lines only (tie-lines have NaN results; filter them) ----
    in_service_mask = net.line["in_service"]
    res_line_inservice = net.res_line[in_service_mask].copy()

    # ---- system-level scalars (SPEC-5) ----
    total_load_mw  = float(net.res_load["p_mw"].sum())
    total_gen_mw   = float(net.res_sgen["p_mw"].sum() + net.res_ext_grid["p_mw"].sum())
    total_loss_mw  = float(net.res_line["pl_mw"].sum() + net.res_trafo["pl_mw"].sum())
    vmin_pu        = float(net.res_bus["vm_pu"].min())
    vmax_pu        = float(net.res_bus["vm_pu"].max())
    slack_p_mw     = float(net.res_ext_grid["p_mw"].iloc[0])
    slack_q_mvar   = float(net.res_ext_grid["q_mvar"].iloc[0])

    system_dict = {
        "total_load_mw":  total_load_mw,
        "total_gen_mw":   total_gen_mw,
        "total_loss_mw":  total_loss_mw,
        "vmin_pu":        vmin_pu,
        "vmax_pu":        vmax_pu,
        "slack_p_mw":     slack_p_mw,
        "slack_q_mvar":   slack_q_mvar,
    }

    return {
        "res_bus":           net.res_bus.copy(),
        "res_line_inservice": res_line_inservice,
        "res_sgen":          net.res_sgen.copy(),
        "res_ext_grid":      net.res_ext_grid.copy(),
        "res_trafo":         net.res_trafo.copy(),
        "tap_pos":           tap_pos,
        "shift_degree":      shift_degree,
        "system_dict":       system_dict,
    }


# ---------------------------------------------------------------------------
# Main driver
# ---------------------------------------------------------------------------

def main() -> None:
    """96-step quasi-static driver: read profiles, sweep steps, write state bucket."""

    # ---- build network + capture base loads ----
    # Capture base load arrays BEFORE any profile scaling so they represent the
    # article's peak-demand values (case33bw default).
    print("Building enhanced IEEE 33-bus network …")
    net, trafo_idx = build_enhanced_33bus()
    base_p = net.load["p_mw"].copy().values    # numpy array, MW at peak
    base_q = net.load["q_mvar"].copy().values  # numpy array, MVAr at peak

    # ---- connect + read all 96 profiles from InfluxDB ONCE (no per-step network — SPEC-4) ----
    print(f"Connecting to InfluxDB at {config.INFLUXDB_URL} …")
    client = influx.get_client()
    influx.wait_for_influx()

    # Ensure the state bucket exists before writing (Pitfall 4)
    influx.ensure_bucket(client, config.STATE_BUCKET)

    print(f"Reading {config.N_STEPS}-step profiles for {config.TARGET_DATE} from InfluxDB …")
    prof = influx.read_profiles(client)

    # Defensive: assert profile count matches expectation
    if len(prof) != config.N_STEPS:
        raise RuntimeError(
            f"Expected {config.N_STEPS} profile rows for {config.TARGET_DATE}, "
            f"got {len(prof)}.  Run 'uv run ingest' first."
        )

    # Sort profiles by time (should already be sorted, but be explicit)
    prof = prof.sort_values("_time").reset_index(drop=True)

    # ---- set up write_api and validation state ----
    write_api = client.write_api(write_options=SYNCHRONOUS)
    issues = []              # hard failures: convergence, NaN — cause sys.exit(1)
    oob_observations = []    # soft observations: band violations — reported, not fatal
    converged_steps = 0
    max_tap_pos = 0          # track max |tap_pos| seen across the run; for OLTC-activity gate

    # ---- build step → forced-tap map from configured OLTC disturbance events ----
    forced_taps = {}
    for ev in getattr(config, "OLTC_EVENTS", []):
        for s in range(ev["start_step"], ev["end_step"]):
            forced_taps[s] = ev["tap_pos"]
    if forced_taps:
        print(f"OLTC disturbance events active at steps {sorted(forced_taps)} "
              f"(forced tap → {sorted(set(forced_taps.values()))}); controller overridden there.")

    # ---- 96-step sweep ----
    print(
        f"\n{'Step':>4}  {'UTC Time':<20}  {'Vmin':>6}  {'Vmax':>6}  "
        f"{'Tap':>4}  {'Loss MW':>8}"
    )
    print("-" * 62)

    for i, row in prof.iterrows():
        # ---- extract per-step profile values ----
        load_pu  = float(row["load_pu"])
        solar_pu = float(row["solar_pu"])
        wind_pu  = float(row["wind_pu"])

        # ---- real OPSD datetime as step timestamp (D-08) ----
        ts = row["_time"]
        if hasattr(ts, "to_pydatetime"):
            ts = ts.to_pydatetime()
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)

        # ---- run power flow (forced tap during a configured disturbance event) ----
        forced = forced_taps.get(i)
        state = run_step(net, trafo_idx, base_p, base_q, load_pu, solar_pu, wind_pu,
                         forced_tap=forced)

        # ---- per-step validation ----
        if not net.converged:
            issues.append(f"step {i:02d} ({ts}): power flow NOT converged")
        else:
            converged_steps += 1

        vmin = state["system_dict"]["vmin_pu"]
        vmax = state["system_dict"]["vmax_pu"]

        # NaN check on bus voltages
        if state["res_bus"]["vm_pu"].isna().any():
            issues.append(f"step {i:02d} ({ts}): NaN in bus vm_pu")

        # Voltage-band check: collect step indices with out-of-band buses (do not abort)
        oob_mask = (
            (state["res_bus"]["vm_pu"] < config.VBAND_LOW) |
            (state["res_bus"]["vm_pu"] > config.VBAND_HIGH)
        )
        oob_buses = list(state["res_bus"][oob_mask].index)
        if oob_buses:
            # With the line-drop-compensation OLTC (regulates a downstream reference
            # bus to ~1.0 pu) the day-wide vmin is ~0.985 pu, so this branch is not
            # expected to fire.  If it does, record it as an observation for the
            # summary (non-fatal) rather than aborting the run.
            evt_note = (f" — EXPECTED: forced OLTC disturbance event (tap={forced})"
                        if forced is not None else "")
            oob_observations.append(
                f"step {i:02d} ({ts}): buses {oob_buses} out of band "
                f"[{config.VBAND_LOW}, {config.VBAND_HIGH}] "
                f"(vmin={vmin:.4f}, vmax={vmax:.4f}){evt_note}"
            )

        # Track OLTC activity (Pitfall 5)
        tap = state["tap_pos"]
        if abs(tap) > max_tap_pos:
            max_tap_pos = abs(tap)

        # ---- write snapshot to state bucket (per-step — Anti-Pattern: no buffering all 96) ----
        influx.write_state_step(
            write_api,
            ts,
            state["res_bus"],
            state["res_line_inservice"],
            state["res_sgen"],
            state["res_ext_grid"],
            state["res_trafo"],
            state["tap_pos"],
            state["shift_degree"],
            state["system_dict"],
        )

        # ---- console readout (every step; mark forced-event steps) ----
        loss = state["system_dict"]["total_loss_mw"]
        evt_mark = " <EVENT" if forced is not None else ""
        print(
            f"{i:>4}  {str(ts)[:19]:<20}  {vmin:>6.4f}  {vmax:>6.4f}  "
            f"{tap:>4}  {loss:>8.4f}{evt_mark}"
        )

    # ---- post-run validation gate (D-14 + Pitfall 5) ----
    print("\n" + "=" * 62)

    # Assert convergence on every step
    if converged_steps < config.N_STEPS:
        issues.append(
            f"Only {converged_steps}/{config.N_STEPS} steps converged"
        )

    # OLTC-activity check (Pitfall 5).  The line-drop-compensation controller regulates
    # a downstream reference bus, so the tap is expected to switch across the day
    # (typically -1..-4 on this date).  If the tap never moves, that now signals a
    # regression (e.g. tap_changer_type unset → inert tap), so flag it as a hard issue.
    if max_tap_pos == 0:
        issues.append(
            "OLTC never tapped (max|tap_pos| == 0 across all 96 steps). The OLTC is "
            "expected to switch with the daily load/DER cycle. Check that "
            "net.trafo.tap_changer_type is set ('Ratio') and FeederTapControl is attached."
        )

    # Assert state bucket has exactly 96 points for bus 18 (SPEC-6 read-back)
    # Scope the read-back to TARGET_DATE (NOT range(start: 0)) so a re-run after a
    # TARGET_DATE change does not over-count stale points from a previous date and
    # raise a false assertion failure.
    flux_readback = (
        f'from(bucket: "{config.STATE_BUCKET}")\n'
        f'  |> range(start: {config.TARGET_DATE}T00:00:00Z, '
        f'stop: {config.TARGET_DATE}T23:59:59Z)\n'
        f'  |> filter(fn: (r) => r._measurement == "bus")\n'
        f'  |> filter(fn: (r) => r.bus_id == "17")\n'
        f'  |> filter(fn: (r) => r._field == "vm_pu")'
    )
    rb_df = client.query_api().query_data_frame(flux_readback)
    n_points = len(rb_df) if rb_df is not None else 0
    if n_points != config.N_STEPS:
        issues.append(
            f"State read-back: expected {config.N_STEPS} points for bus_id='17' vm_pu, "
            f"got {n_points} — write may have failed"
        )

    # ---- print voltage-band observations (non-fatal honest physics results) ----
    if oob_observations:
        print("\n--- VOLTAGE-BAND OBSERVATIONS (non-fatal, recorded for SUMMARY.md) ---")
        for obs in oob_observations:
            print(f"  {obs}")

    # ---- fail loud if any hard issues ----
    if issues:
        print("--- SIM VALIDATION FAILED ---", file=sys.stderr)
        for issue in issues:
            print(f"  {issue}", file=sys.stderr)
        client.close()
        sys.exit(1)

    # ---- success summary ----
    # Compute vmin/vmax range across all steps from the read-back data
    vmin_series = state["system_dict"]["vmin_pu"]  # last step value (scalar)
    vmax_series = state["system_dict"]["vmax_pu"]  # last step value (scalar)
    print(
        f"sim OK — {config.N_STEPS} snapshots written to bucket '{config.STATE_BUCKET}' "
        f"for {config.TARGET_DATE}; "
        f"last-step vmin={vmin_series:.4f} vmax={vmax_series:.4f}; "
        f"max|tap|={max_tap_pos}"
    )
    print(f"bus 18 vm_pu read-back: {n_points} points confirmed (SPEC-6)")

    # ---- close client ----
    client.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nFATAL: {exc}", file=sys.stderr)
        sys.exit(1)
