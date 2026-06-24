"""
fault_sim.py
------------
Deterministic 40-step fault-and-reconfiguration runner for the enhanced IEEE 33-bus
DER measurement source.  Freezes the evening-peak operating point (step 72 from the
96-step day profiles), then walks three ordered blocks:

    pre_fault      (13 steps): normal radial operation, line 7 energised.
    faulted_isolated (7 steps): line 7 + in-zone lines/buses/DG out of service;
                                OLTC tap pinned (D-12 — OLTC_REF_BUS=17 is in the dead zone).
    restored       (20 steps): tie 34 closed, in-zone re-energised, faulted line stays open.

Determinism note: anchor timestamp = OPSD UTC datetime for FAULT_EVENING_PEAK_STEP (step 72)
read from the profiles bucket; subsequent steps at +3s offsets.  No datetime.now(),
no np.random, no time.time() — identical 40 snapshots on every run.  Re-running overwrites
points at the same timestamp+tag keys (overwrite-in-place).

Dependencies: pandapower, pandapower.topology, networkx, influxdb-client, pandas, python-dotenv
Run:          uv run fault-sim
Effect:       Writes 40 fault-event power-flow snapshots to InfluxDB 'fault_event' bucket.
              Exits 0 on success, 1 on validation failure.
"""

import sys
from datetime import datetime, timezone, timedelta

import networkx as nx
import pandapower as pp
import pandapower.topology as ptop
from influxdb_client.client.write_api import SYNCHRONOUS

from ieee33 import config
from ieee33 import influx
from ieee33.network import build_enhanced_33bus


# ---------------------------------------------------------------------------
# Module-level dead-entity constants (verified against live model by planner)
# ---------------------------------------------------------------------------

# Dead lines during isolated block: faulted line 7 + in-zone lines 8..16
# case33bw line endpoints: 7: 7->8, 8: 8->9, 9: 9->10, 10: 10->11, 11: 11->12,
#                          12: 12->13, 13: 13->14, 14: 14->15, 15: 15->16, 16: 16->17
DEAD_LINE_IDS = [config.FAULT_LINE_IDX] + list(range(8, 17))  # [7,8,9,10,11,12,13,14,15,16]

# sgen 0 -> bus 17 (inside dead zone, D-11); sgens 1/2/3 are outside
DEAD_SGEN_IDS = [0]

# shunt 0 -> bus 17 (inside dead zone); shunt 1 -> bus 32 (healthy)
DEAD_SHUNT_IDS = [0]


# ---------------------------------------------------------------------------
# Dead-zone traversal (D-07)
# ---------------------------------------------------------------------------

def _compute_dead_buses(net) -> list[int]:
    """Compute dead-zone bus indices by graph traversal after opening the faulted line.

    Builds an nxgraph from the current in_service flags, finds the slack-connected
    component, and returns all bus indices NOT reachable from the slack bus.

    D-07 requirement: computed by traversal, not hardcoded.

    Args:
        net: pandapowerNet with FAULT_LINE_IDX already set in_service=False.

    Returns:
        Sorted list of dead (unreachable) bus indices.
    """
    g = ptop.create_nxgraph(net, respect_switches=True)
    slack = int(net.ext_grid.bus.iloc[0])
    reachable = nx.node_connected_component(g, slack)
    return sorted(set(int(b) for b in net.bus.index) - reachable)


# ---------------------------------------------------------------------------
# D-08: tie-selection for restoration
# ---------------------------------------------------------------------------

def _select_restore_tie(
    load_pu: float,
    solar_pu: float,
    wind_pu: float,
    base_p,
    base_q,
) -> tuple[int, float]:
    """Try each candidate tie in priority order; return (tie_idx, vmin_pu) for the first
    that gives a converged, radial restoration with energised-bus vmin >= 0.94 pu.

    The primary candidate is config.FAULT_TIE_IDX (34); remaining TIE_LINE_IDX values
    follow in order.  On the locked evening-peak operating point tie 34 yields ~0.9971,
    so the fallback path does NOT fire in practice — but it is implemented for honesty
    (D-08).

    Args:
        load_pu, solar_pu, wind_pu: frozen operating-point scaling factors.
        base_p, base_q: numpy arrays of base load values (captured once from net at build).

    Returns:
        (tie_idx, achieved_vmin_pu) for the selected tie.

    Raises:
        RuntimeError if no tie qualifies (hard failure — exits via issues list in main).
    """
    candidates = [config.FAULT_TIE_IDX] + [
        t for t in config.TIE_LINE_IDX if t != config.FAULT_TIE_IDX
    ]

    for tie_idx in candidates:
        try:
            # Build a fresh net to avoid mutating the main net
            probe_net, probe_trafo_idx = build_enhanced_33bus()

            # Scale to frozen operating point
            probe_net.load["p_mw"]   = base_p * load_pu
            probe_net.load["q_mvar"] = base_q * load_pu
            solar_mask = probe_net.sgen["type"] == "PV"
            probe_net.sgen.loc[solar_mask, "p_mw"] = (
                probe_net.sgen.loc[solar_mask, "p_mw_nameplate"] * solar_pu
            )
            wind_mask = probe_net.sgen["type"] == "WP"
            probe_net.sgen.loc[wind_mask, "p_mw"] = (
                probe_net.sgen.loc[wind_mask, "p_mw_nameplate"] * wind_pu
            )

            # Apply restored topology: faulted line OUT, dead-zone lines/buses/sgens IN,
            # candidate tie IN, other ties OUT
            probe_net.line.loc[config.TIE_LINE_IDX, "in_service"] = False
            probe_net.line.at[config.FAULT_LINE_IDX, "in_service"] = False
            for line_id in DEAD_LINE_IDS[1:]:   # in-zone lines (not the faulted line)
                probe_net.line.at[line_id, "in_service"] = True
            probe_net.bus.loc[config.FAULT_DEAD_BUS_IDX, "in_service"] = True
            for sgen_id in DEAD_SGEN_IDS:
                probe_net.sgen.at[sgen_id, "in_service"] = True
            for shunt_id in DEAD_SHUNT_IDS:
                probe_net.shunt.at[shunt_id, "in_service"] = True
            probe_net.line.at[tie_idx, "in_service"] = True

            pp.runpp(probe_net, algorithm="nr", calculate_voltage_angles=True, run_control=True)

            if not probe_net.converged:
                continue

            # Radiality check: the connected graph must be a tree
            g = ptop.create_nxgraph(probe_net, respect_switches=True)
            if not nx.is_tree(g):
                continue

            # Voltage check: all energised (in-service) buses must be >= 0.94 pu
            energised_vm = probe_net.res_bus["vm_pu"]
            if energised_vm.min() < 0.94:
                continue

            achieved_vmin = float(energised_vm.min())
            print(f"  Restore tie selected: line idx {tie_idx}, vmin={achieved_vmin:.4f} pu")
            return tie_idx, achieved_vmin

        except Exception:
            continue

    raise RuntimeError(
        "No candidate restore tie produced a converged, radial, >= 0.94 pu restoration."
    )


# ---------------------------------------------------------------------------
# Per-step runner (mirrors sim.run_step)
# ---------------------------------------------------------------------------

def run_fault_step(
    net,
    trafo_idx: int,
    base_p,
    base_q,
    load_pu: float,
    solar_pu: float,
    wind_pu: float,
    phase: str,
    peak_tap: int,
) -> dict:
    """Scale loads and DGs, run power flow, return full state dict.

    The operating point (load_pu, solar_pu, wind_pu) is FROZEN — identical across
    all 40 steps.  Only the topology (in_service flags) changes between blocks.

    D-12 OLTC pin: during faulted_isolated the OLTC_REF_BUS (17) is inside the dead
    zone, so the controller cannot regulate and would drive the tap to extremes chasing
    a missing reference.  Pin the tap to the pre-fault evening-peak position and disable
    control (run_control=False) for the entire isolated block.

    Args:
        net:        pandapowerNet (mutated in-place by block transitions in main()).
        trafo_idx:  integer index of the OLTC transformer in net.trafo.
        base_p:     numpy array of base active load values (MW).
        base_q:     numpy array of base reactive load values (MVAr).
        load_pu:    frozen load scaling factor.
        solar_pu:   frozen solar capacity factor.
        wind_pu:    frozen wind capacity factor.
        phase:      one of FAULT_PHASE_PRE, FAULT_PHASE_ISO, FAULT_PHASE_RST.
        peak_tap:   evening-peak tap position (captured from first pre_fault step, D-12).

    Returns:
        dict with keys: res_bus, res_line_inservice, res_sgen, res_ext_grid, res_trafo,
                        tap_pos, shift_degree, system_dict.
    """
    # ---- scale loads (frozen operating point) ----
    net.load["p_mw"]   = base_p * load_pu
    net.load["q_mvar"] = base_q * load_pu

    # ---- set DG by profile × nameplate (frozen operating point) ----
    solar_mask = net.sgen["type"] == "PV"
    net.sgen.loc[solar_mask, "p_mw"] = (
        net.sgen.loc[solar_mask, "p_mw_nameplate"] * solar_pu
    )
    wind_mask = net.sgen["type"] == "WP"
    net.sgen.loc[wind_mask, "p_mw"] = (
        net.sgen.loc[wind_mask, "p_mw_nameplate"] * wind_pu
    )

    # ---- power flow (D-12: pin tap during isolated block) ----
    if phase == config.FAULT_PHASE_ISO:
        net.trafo.at[trafo_idx, "tap_pos"] = int(peak_tap)
        pp.runpp(net, algorithm="nr", calculate_voltage_angles=True, run_control=False)
    else:
        pp.runpp(net, algorithm="nr", calculate_voltage_angles=True, run_control=True)

    # ---- read tap/shift from net.trafo (NOT res_trafo — Pitfall 6) ----
    tap_pos      = int(net.trafo.at[trafo_idx, "tap_pos"])
    shift_degree = float(net.trafo.at[trafo_idx, "shift_degree"])

    # ---- in-service lines only (tie-lines and dead-zone lines have NaN results) ----
    in_service_mask = net.line["in_service"]
    res_line_inservice = net.res_line[in_service_mask].copy()

    # ---- system-level scalars (mirrors sim.run_step lines 89-106) ----
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
        "res_bus":            net.res_bus.copy(),
        "res_line_inservice": res_line_inservice,
        "res_sgen":           net.res_sgen.copy(),
        "res_ext_grid":       net.res_ext_grid.copy(),
        "res_trafo":          net.res_trafo.copy(),
        "tap_pos":            tap_pos,
        "shift_degree":       shift_degree,
        "system_dict":        system_dict,
    }


# ---------------------------------------------------------------------------
# Main driver
# ---------------------------------------------------------------------------

def main() -> None:
    """40-step fault-and-reconfiguration driver: freeze op-point, walk blocks, write fault_event bucket."""

    # ---- build network + capture base loads ----
    print("Building enhanced IEEE 33-bus network ...")
    net, trafo_idx = build_enhanced_33bus()
    base_p = net.load["p_mw"].copy().values    # numpy array, MW at evening-peak
    base_q = net.load["q_mvar"].copy().values  # numpy array, MVAr at evening-peak

    # ---- connect to InfluxDB + ensure fault_event bucket ----
    print(f"Connecting to InfluxDB at {config.INFLUXDB_URL} ...")
    client = influx.get_client()
    influx.wait_for_influx()
    influx.ensure_bucket(client, config.FAULT_EVENT_BUCKET)

    # ---- read all 96 profiles ONCE; pick the evening-peak frozen operating point ----
    print(f"Reading 96-step profiles from InfluxDB (anchor step {config.FAULT_EVENING_PEAK_STEP}) ...")
    prof = influx.read_profiles(client).sort_values("_time").reset_index(drop=True)

    peak_row = prof.iloc[config.FAULT_EVENING_PEAK_STEP]
    load_pu  = float(peak_row["load_pu"])
    solar_pu = float(peak_row["solar_pu"])
    wind_pu  = float(peak_row["wind_pu"])

    # Deterministic anchor timestamp: OPSD UTC datetime for the evening-peak step
    anchor_ts = peak_row["_time"]
    if hasattr(anchor_ts, "to_pydatetime"):
        anchor_ts = anchor_ts.to_pydatetime()
    if anchor_ts.tzinfo is None:
        anchor_ts = anchor_ts.replace(tzinfo=timezone.utc)

    print(f"  Frozen op-point: load_pu={load_pu:.4f}, solar_pu={solar_pu:.4f}, wind_pu={wind_pu:.4f}")
    print(f"  Anchor timestamp: {anchor_ts.isoformat()}")

    # ---- select restore tie (D-08; primary = FAULT_TIE_IDX=34) ----
    print("Selecting restore tie (D-08) ...")
    chosen_tie, tie_vmin = _select_restore_tie(load_pu, solar_pu, wind_pu, base_p, base_q)

    # ---- build 40-step phase plan + deterministic timestamps ----
    phases = (
        [config.FAULT_PHASE_PRE] * config.FAULT_PRE_STEPS
        + [config.FAULT_PHASE_ISO] * config.FAULT_ISO_STEPS
        + [config.FAULT_PHASE_RST] * config.FAULT_RST_STEPS
    )
    assert len(phases) == config.FAULT_N_STEPS, (
        f"Phase list length {len(phases)} != {config.FAULT_N_STEPS}"
    )
    timestamps = [
        anchor_ts + timedelta(seconds=config.FAULT_STEP_S * i)
        for i in range(config.FAULT_N_STEPS)
    ]

    # ---- set up write_api and validation state ----
    write_api = client.write_api(write_options=SYNCHRONOUS)
    issues: list[str] = []

    # ---- console table header (D-18) ----
    print(
        f"\n{'Step':>4}  {'Phase':<18}  {'Vmin':>6}  {'Load MW':>8}  "
        f"{'Tap':>4}  {'Dead':>5}"
    )
    print("-" * 62)

    # ---- state trackers for post-loop gates ----
    peak_tap: int | None = None        # captured from first pre_fault step (D-12)
    iso_loads: list[float] = []        # served-load per isolated step (D-16 drop gate)
    rst_vmins: list[float] = []        # min energised vmin per restored step (D-16 band gate)
    dead_bus_set: list[int] = []       # dead buses (set once at isolation transition)

    # ---- ensure initial topology is consistent: all ties open, faulted line in ----
    net.line.loc[config.TIE_LINE_IDX, "in_service"] = False
    net.line.at[config.FAULT_LINE_IDX, "in_service"] = True
    for line_id in DEAD_LINE_IDS[1:]:
        net.line.at[line_id, "in_service"] = True
    for bus_id in config.FAULT_DEAD_BUS_IDX:
        net.bus.at[bus_id, "in_service"] = True
    for sgen_id in DEAD_SGEN_IDS:
        net.sgen.at[sgen_id, "in_service"] = True
    for shunt_id in DEAD_SHUNT_IDS:
        net.shunt.at[shunt_id, "in_service"] = True

    # ---- 40-step walk ----
    prev_phase: str | None = None

    for i, (phase, ts) in enumerate(zip(phases, timestamps)):

        # -- BLOCK TRANSITION: faulted_isolated (first ISO step) --
        if phase == config.FAULT_PHASE_ISO and prev_phase != config.FAULT_PHASE_ISO:
            # Isolate faulted line and dead-zone
            net.line.at[config.FAULT_LINE_IDX, "in_service"] = False
            for line_id in DEAD_LINE_IDS[1:]:
                net.line.at[line_id, "in_service"] = False
            for bus_id in config.FAULT_DEAD_BUS_IDX:
                net.bus.at[bus_id, "in_service"] = False
            for sgen_id in DEAD_SGEN_IDS:
                net.sgen.at[sgen_id, "in_service"] = False
            for shunt_id in DEAD_SHUNT_IDS:
                net.shunt.at[shunt_id, "in_service"] = False
            # All ties remain open (only the chosen restore tie closes in RST block)
            # Compute and assert dead-bus set (D-07)
            dead_bus_set = _compute_dead_buses(net)
            assert dead_bus_set == sorted(config.FAULT_DEAD_BUS_IDX), (
                f"Dead-bus traversal mismatch: got {dead_bus_set}, "
                f"expected {sorted(config.FAULT_DEAD_BUS_IDX)}"
            )

        # -- BLOCK TRANSITION: restored (first RST step) --
        if phase == config.FAULT_PHASE_RST and prev_phase != config.FAULT_PHASE_RST:
            # Re-energise in-zone lines (NOT the faulted line — stays open forever)
            for line_id in DEAD_LINE_IDS[1:]:
                net.line.at[line_id, "in_service"] = True
            for bus_id in config.FAULT_DEAD_BUS_IDX:
                net.bus.at[bus_id, "in_service"] = True
            for sgen_id in DEAD_SGEN_IDS:
                net.sgen.at[sgen_id, "in_service"] = True
            for shunt_id in DEAD_SHUNT_IDS:
                net.shunt.at[shunt_id, "in_service"] = True
            # Close the chosen restore tie; faulted line stays open
            net.line.at[config.FAULT_LINE_IDX, "in_service"] = False
            net.line.at[chosen_tie, "in_service"] = True
            dead_bus_set = []  # no dead buses in restored block

        # -- per-step write call: compute dead id sets for write_fault_step --
        if phase == config.FAULT_PHASE_PRE:
            dead_bus_ids  = []
            dead_line_ids = []
            dead_sgen_ids = []
            tie_is_closed = False
        elif phase == config.FAULT_PHASE_ISO:
            dead_bus_ids  = dead_bus_set
            dead_line_ids = DEAD_LINE_IDS
            dead_sgen_ids = DEAD_SGEN_IDS
            tie_is_closed = False
        else:  # FAULT_PHASE_RST
            dead_bus_ids  = []
            dead_line_ids = [config.FAULT_LINE_IDX]   # D-05: zero-fill faulted line in ALL restored steps
            dead_sgen_ids = []
            tie_is_closed = True

        # -- capture peak_tap from first pre_fault run --
        if i == 0:
            # Run the first pre_fault step to determine the evening-peak tap
            state = run_fault_step(
                net, trafo_idx, base_p, base_q, load_pu, solar_pu, wind_pu,
                phase=phase, peak_tap=0  # peak_tap not used in pre_fault
            )
            peak_tap = state["tap_pos"]
            print(f"  Evening-peak tap captured: {peak_tap} (BOOST if negative)")
        else:
            state = run_fault_step(
                net, trafo_idx, base_p, base_q, load_pu, solar_pu, wind_pu,
                phase=phase, peak_tap=peak_tap if peak_tap is not None else 0
            )

        # -- D-14: per-step convergence + NaN gate --
        if not net.converged:
            issues.append(f"step {i:02d} ({phase}): power flow NOT converged")

        energised_vm = net.res_bus["vm_pu"]
        if energised_vm.isna().any():
            issues.append(f"step {i:02d} ({phase}): NaN in energised bus vm_pu")

        # -- D-15: radiality check in restored block --
        if phase == config.FAULT_PHASE_RST:
            tie_in_service   = bool(net.line.at[chosen_tie, "in_service"])
            fault_in_service = bool(net.line.at[config.FAULT_LINE_IDX, "in_service"])
            if not (tie_in_service and not fault_in_service):
                issues.append(
                    f"step {i:02d}: radiality topology check failed "
                    f"(tie_in_service={tie_in_service}, fault_in_service={fault_in_service})"
                )
            else:
                g = ptop.create_nxgraph(net, respect_switches=True)
                if not nx.is_tree(g):
                    issues.append(f"step {i:02d}: radiality graph check failed (not a tree)")

        # -- track served-load and restored vmin for post-loop gates --
        served_load = state["system_dict"]["total_load_mw"]
        vmin        = state["system_dict"]["vmin_pu"]
        tap         = state["tap_pos"]
        n_dead      = len(dead_bus_ids)

        if phase == config.FAULT_PHASE_ISO:
            iso_loads.append(served_load)
        if phase == config.FAULT_PHASE_RST:
            rst_vmins.append(float(energised_vm.min()))

        # -- write snapshot to fault_event bucket --
        influx.write_fault_step(
            write_api, ts,
            state["res_bus"],
            state["res_line_inservice"],
            state["res_sgen"],
            state["res_ext_grid"],
            state["res_trafo"],
            state["tap_pos"],
            state["shift_degree"],
            state["system_dict"],
            phase, dead_bus_ids, dead_line_ids, dead_sgen_ids, tie_is_closed,
        )

        # -- D-18: console row --
        print(
            f"{i:>4}  {phase:<18}  {vmin:>6.4f}  {served_load:>8.4f}  "
            f"{tap:>4}  {n_dead:>5}"
        )

        prev_phase = phase

    # ---- post-loop gates ----
    print("\n" + "=" * 62)

    # D-16 served-load drop: any isolated step must have load < step-0 load
    step0_load = None
    # Re-read step 0 load from the profiles for comparison; use served_load from last pre_fault step
    # We know pre_fault served_load ~ 3.29 MW (planner verified); track via the iso_loads
    # The step-0 served-load is the pre_fault total; re-run is not needed — capture from loop
    # We need the actual pre_fault served_load. Let's track it:
    # (We already tracked iso_loads; use the pre_fault load as the reference — the planner
    #  confirmed pre_fault load ~ 3.29 MW and iso_loads drop by ~0.6 MW.)
    # We can verify by comparing iso_loads vs. our known pre_fault reference.
    # To get this reference cleanly: run a quick single-step probe at pre_fault topology.
    # But simpler: during the loop above we did not save pre_fault served_loads.
    # Solution: save them in a separate list:
    # NOTE: this post-loop block operates on data gathered above. The pre_fault served_load
    # was the load at any of steps 0..12. We don't have it stored — add a simple reference
    # via a re-run of run_fault_step at pre_fault topology is wasteful. The cleaner fix:
    # We already know from the planner: pre_fault load ~ 3.2922 MW, iso_loads ~ 2.6941 MW.
    # For the gate we compare iso_loads (collected above) against a pre_fault reference.
    # Let us do a quick single-step pre_fault reference run at the locked op-point:
    _probe_net, _probe_trafo_idx = build_enhanced_33bus()
    _probe_net.line.loc[config.TIE_LINE_IDX, "in_service"] = False
    _probe_net.line.at[config.FAULT_LINE_IDX, "in_service"] = True
    for _lid in DEAD_LINE_IDS[1:]:
        _probe_net.line.at[_lid, "in_service"] = True
    for _bid in config.FAULT_DEAD_BUS_IDX:
        _probe_net.bus.at[_bid, "in_service"] = True
    for _sid in DEAD_SGEN_IDS:
        _probe_net.sgen.at[_sid, "in_service"] = True
    for _shid in DEAD_SHUNT_IDS:
        _probe_net.shunt.at[_shid, "in_service"] = True
    pre_state = run_fault_step(
        _probe_net, _probe_trafo_idx, base_p, base_q, load_pu, solar_pu, wind_pu,
        phase=config.FAULT_PHASE_PRE, peak_tap=peak_tap if peak_tap is not None else 0
    )
    pre_served_load = pre_state["system_dict"]["total_load_mw"]

    if iso_loads and min(iso_loads) >= pre_served_load:
        issues.append(
            f"D-16 served-load drop FAILED: iso min={min(iso_loads):.4f} MW "
            f">= pre_fault={pre_served_load:.4f} MW (expected drop)"
        )
    else:
        print(
            f"D-16 served-load drop OK: iso_min={min(iso_loads) if iso_loads else 'N/A':.4f} MW "
            f"< pre_fault={pre_served_load:.4f} MW"
        )

    # D-16 restored voltage band
    shortfall_flag = False
    if rst_vmins:
        rst_min = min(rst_vmins)
        if rst_min >= 0.95:
            print(f"D-16 restored vmin OK (clean): {rst_min:.4f} pu >= 0.95")
        elif rst_min >= 0.94:
            shortfall_flag = True
            print(
                f"RESTORED-VOLTAGE SHORTFALL (informational): "
                f"min vmin={rst_min:.4f} pu in [0.94, 0.95) — "
                f"tie {chosen_tie} restores but stays below 0.95 band"
            )
        else:
            issues.append(
                f"D-16 restored vmin FAILED: {rst_min:.4f} pu < 0.94 (unacceptable)"
            )

    # D-17 read-back: assert exactly 40 bus_id="0" vm_pu points in fault_event
    anchor_start = anchor_ts.strftime("%Y-%m-%dT%H:%M:%SZ")
    anchor_stop  = (anchor_ts + timedelta(seconds=config.FAULT_STEP_S * config.FAULT_N_STEPS + 10)).strftime("%Y-%m-%dT%H:%M:%SZ")
    flux_readback = (
        f'from(bucket: "{config.FAULT_EVENT_BUCKET}")\n'
        f'  |> range(start: {anchor_start}, stop: {anchor_stop})\n'
        f'  |> filter(fn: (r) => r._measurement == "bus")\n'
        f'  |> filter(fn: (r) => r.bus_id == "0")\n'
        f'  |> filter(fn: (r) => r._field == "vm_pu")'
    )
    rb_df = client.query_api().query_data_frame(flux_readback)
    n_points = len(rb_df) if rb_df is not None else 0
    if n_points != config.FAULT_N_STEPS:
        issues.append(
            f"D-17 read-back FAILED: expected {config.FAULT_N_STEPS} points for bus_id='0' vm_pu, "
            f"got {n_points} — write may have failed"
        )
    else:
        print(f"D-17 read-back OK: {n_points} points confirmed for bus_id='0' vm_pu")

    # ---- fail-loud (copy sim.py lines 303-308 verbatim) ----
    if issues:
        print("--- SIM VALIDATION FAILED ---", file=sys.stderr)
        for issue in issues:
            print(f"  {issue}", file=sys.stderr)
        client.close()
        sys.exit(1)

    # ---- success summary ----
    rst_min_summary = min(rst_vmins) if rst_vmins else float("nan")
    print(
        f"fault-sim OK — 40 snapshots written to bucket '{config.FAULT_EVENT_BUCKET}'; "
        f"chosen_tie=line_{chosen_tie}; "
        f"restored_min_vmin={rst_min_summary:.4f} pu; "
        f"shortfall_flag={shortfall_flag}"
    )

    client.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nFATAL: {exc}", file=sys.stderr)
        sys.exit(1)
