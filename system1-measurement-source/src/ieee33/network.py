"""
network.py
----------
Pure library module that builds the enhanced IEEE 33-bus PandaPower network
described in Dolatabadi et al. (2020) — four renewable DG sources (solar/wind),
two RPC shunt capacitors, and a regulating feeder transformer (OLTC + phase
shifter) inserted in series at the substation.

Exposes a single public function:

    build_enhanced_33bus() -> (net, trafo_idx)

where `net` is a converging pandapowerNet and `trafo_idx` is the integer index
of the feeder OLTC transformer.  The caller is responsible for running
`pp.runpp(net, run_control=True, calculate_voltage_angles=True)` after calling
this function.

Dependencies: pandapower 3.4.0 (includes pandapower.control), ieee33.config
Run:          imported — not executed directly (NO __main__ block; PATTERNS line 84)
Effect:       Returns a built pandapowerNet ready for power-flow simulation.
              No I/O, no side effects, no prints.
"""

import pandapower as pp
import pandapower.networks as pn
from pandapower.control.basic_controller import Controller
from ieee33 import config


class FeederTapControl(Controller):
    """Line-drop-compensation OLTC controller for the feeder transformer.

    Regulates a DOWNSTREAM reference bus (config.OLTC_REF_BUS) into the band
    [vm_lower_pu, vm_upper_pu] by stepping the transformer tap, instead of the
    transformer's own LV bus.  This is why the OLTC actually switches across the
    day: the LV bus (bus 0) is adjacent to the stiff slack and barely moves, so a
    bus-0 regulator never taps; a downstream reference swings with load/DER, so the
    tap boosts at evening peak and backs off under midday DER.

    Tap direction: on this transformer a MORE NEGATIVE tap_pos RAISES voltage
    (boost), confirmed empirically (tap_pos=-4 → bus0≈1.036; +4 → ≈0.955).  So to
    raise a sagging reference bus we DECREMENT tap_pos, and to lower an
    over-voltage reference we INCREMENT it.  Requires net.trafo.tap_changer_type
    set (pandapower 3.x leaves it NaN, which makes the tap inert).
    """

    def __init__(self, net, trafo_idx, controlled_bus, vm_lower_pu, vm_upper_pu, **kwargs):
        super().__init__(net, **kwargs)
        self.tid = trafo_idx
        self.cb = controlled_bus
        self.lo = vm_lower_pu
        self.hi = vm_upper_pu
        self.tmin = int(net.trafo.at[trafo_idx, "tap_min"])
        self.tmax = int(net.trafo.at[trafo_idx, "tap_max"])

    def is_converged(self, net):
        # Not converged until a power-flow result exists for the controlled bus.
        if not hasattr(net, "res_bus") or len(net.res_bus) == 0 \
                or self.cb not in net.res_bus.index:
            return False
        vm = net.res_bus.at[self.cb, "vm_pu"]
        tap = int(net.trafo.at[self.tid, "tap_pos"])
        # Below band and able to boost (tap can still go more negative) → act.
        if vm < self.lo and tap > self.tmin:
            return False
        # Above band and able to buck (tap can still go more positive) → act.
        if vm > self.hi and tap < self.tmax:
            return False
        return True

    def control_step(self, net):
        vm = net.res_bus.at[self.cb, "vm_pu"]
        tap = int(net.trafo.at[self.tid, "tap_pos"])
        if vm < self.lo:
            tap -= 1   # boost (more negative tap raises voltage)
        elif vm > self.hi:
            tap += 1   # buck
        net.trafo.at[self.tid, "tap_pos"] = max(self.tmin, min(self.tmax, tap))


def build_enhanced_33bus() -> tuple[pp.pandapowerNet, int]:
    """Build and return the enhanced IEEE 33-bus network (radial, balanced).

    Network topology:
    - Base: pn.case33bw() — 33 buses (indices 0..32), 32 distribution lines,
      ext_grid (slack) at bus 0, all base loads set to Baran & Wu peak values.
      NOTE: article bus N = pandapower index N-1 (0-indexed everywhere below).
    - Tie-lines (pandapower line indices 32, 33, 34) forced open → radial topology.
    - Feeder OLTC transformer inserted IN SERIES: a new HV bus is created, the
      ext_grid is moved to it, and a 2-winding transformer connects HV → bus 0.
      tap_changer_type is set to "Ratio" (REQUIRED in pandapower 3.x — otherwise the
      tap is inert).  A FeederTapControl (line-drop compensation) regulates a
      DOWNSTREAM reference bus (config.OLTC_REF_BUS) into [0.99, 1.01] pu so the tap
      actively switches across the day.  PITFALL 2: do NOT leave ext_grid at bus 0
      and add the trafo elsewhere — the OLTC must be between the source and bus 0.
    - Line ratings: case33bw ships max_i_ka=99999 (placeholder); replaced with a
      nominal feeder ampacity (config.LINE_MAX_I_KA) so loading_percent is meaningful.
    - 4 DG sgens at buses 17/21 (solar) and 24/32 (wind); p_mw set to the scaled
      effective nameplate (0.56 MW each per D-04).  A p_mw_nameplate column is
      added so the simulation loop can scale by a 0–1 profile without recomputing
      the nameplate.
    - 2 RPC shunt capacitors at buses 17 and 32; q_mvar < 0 (capacitive convention
      in pandapower: negative q_mvar generates reactive power).  PITFALL sign:
      +0.4 MVAr would be INDUCTIVE (absorbs Q); use config.RPC_SHUNTS which
      already encodes the correct negative values.

    Returns
    -------
    net : pp.pandapowerNet
        Fully assembled enhanced IEEE 33-bus network, not yet run.
    trafo_idx : int
        Integer index of the feeder OLTC transformer in net.trafo.
    """

    # ---- 1. Load Baran & Wu base case ----
    # case33bw: 33 buses (0..32), 32 lines (0..31), ext_grid at bus 0.
    # NOTE: pandapower 3.x also includes 3 tie-lines (indices 32/33/34) as
    # out-of-service — we enforce this explicitly below regardless of default.
    net = pn.case33bw()

    # ---- 2. Enforce radial topology: open tie-lines ----
    # RESEARCH Open Q #3 resolved: force in_service=False even if already False,
    # so the topology contract is explicit and not reliant on case33bw defaults.
    net.line.loc[config.TIE_LINE_IDX, "in_service"] = False

    # ---- 2b. Set realistic line thermal ratings ----
    # case33bw ships max_i_ka=99999 (placeholder) on every line → loading_percent ≈ 0.
    # Apply a nominal 12.66 kV feeder ampacity so loading_percent is meaningful.
    # This affects loading_percent ONLY — the power-flow solution is unchanged.
    net.line["max_i_ka"] = config.LINE_MAX_I_KA

    # ---- 3. Assert base load totals match article peak demand (SPEC-1 acceptance) ----
    # case33bw loads are already at Baran & Wu peak; assert before any scaling.
    total_p = net.load["p_mw"].sum()
    total_q = net.load["q_mvar"].sum()
    assert abs(total_p - config.PEAK_LOAD_MW) < 0.05, (
        f"Base load mismatch: got {total_p:.4f} MW, expected {config.PEAK_LOAD_MW} MW "
        f"(tol 0.05 MW) — check case33bw version"
    )
    assert abs(total_q - config.PEAK_LOAD_MVAR) < 0.1, (
        f"Base reactive load mismatch: got {total_q:.4f} MVAr, expected "
        f"{config.PEAK_LOAD_MVAR} MVAr (tol 0.1 MVAr) — check case33bw version"
    )

    # ---- 4. Insert OLTC transformer IN SERIES at the substation ----
    # PITFALL 2: create a new HV bus, move ext_grid to it, then create the
    # transformer from HV → bus 0.  This puts the OLTC in the power path.
    # Both sides are 12.66 kV so the transformer is a voltage-ratio ≈ 1 regulator.
    hv_bus = pp.create_bus(net, vn_kv=12.66, name="feeder_hv")
    # Move the slack source to the new HV bus
    net.ext_grid.bus = hv_bus

    trafo_idx = pp.create_transformer_from_parameters(
        net,
        hv_bus=hv_bus,
        lv_bus=0,                       # article bus 1 = pandapower index 0
        sn_mva=config.TRAFO_SN_MVA,     # 10.0 MVA feeder rating
        vn_hv_kv=12.66,
        vn_lv_kv=12.66,
        vkr_percent=config.TRAFO_VKR_PERCENT,  # 0.5 %
        vk_percent=config.TRAFO_VK_PERCENT,    # 4.0 %
        pfe_kw=0.0,
        i0_percent=0.0,
        shift_degree=config.SHIFT_DEGREE,       # 0.0 deg baseline; captured as state each step
        tap_side="hv",
        tap_neutral=config.TAP_NEUTRAL,         # 0 → ratio 1.0 at neutral
        tap_min=config.TAP_MIN,                 # -5 → 0.95 pu lower limit
        tap_max=config.TAP_MAX,                 # +5 → 1.05 pu upper limit
        tap_step_percent=config.TAP_STEP_PERCENT,  # 1.0 % per step
        tap_pos=0,                              # start at neutral
        name="feeder_OLTC",
    )

    # CRITICAL (pandapower 3.x): the tap is INERT unless tap_changer_type is set.
    # create_transformer_from_parameters leaves it NaN, so changing tap_pos has ZERO
    # effect on the power flow. "Ratio" = standard OLTC voltage-ratio tap changer.
    net.trafo.at[trafo_idx, "tap_changer_type"] = config.TAP_CHANGER_TYPE

    # ---- 5. Attach line-drop-compensation OLTC controller ----
    # Runs inside pp.runpp(run_control=True).  Regulates a DOWNSTREAM reference bus
    # (config.OLTC_REF_BUS, the end of the main trunk) into [0.99, 1.01] pu — NOT the
    # trafo LV bus.  The LV bus sits next to the stiff slack and barely moves, so a
    # bus-0 regulator never taps; a downstream reference swings with load/DER, so the
    # tap boosts at evening peak and backs off under midday DER (visible daily
    # switching) and lifts the sagging laterals above 0.95 pu.
    FeederTapControl(
        net,
        trafo_idx=trafo_idx,
        controlled_bus=config.OLTC_REF_BUS,   # idx 17 = article bus 18 (end of main trunk)
        vm_lower_pu=config.OLTC_VM_LOWER_PU,  # 0.99 pu
        vm_upper_pu=config.OLTC_VM_UPPER_PU,  # 1.01 pu
    )

    # ---- 6. Add DG sgens: solar at buses 17, 21; wind at buses 24, 32 ----
    # PITFALL 1: article bus N → pandapower index N-1.
    #   Article bus 18 → idx 17 (solar); bus 22 → idx 21 (solar)
    #   Article bus 25 → idx 24 (wind);  bus 33 → idx 32 (wind)
    # p_mw = DG_EFFECTIVE_MW = 0.56 MW (D-04 deliberate deviation; see config.py comment).
    # q_mvar=0 (unity power factor baseline; reactive dispatch is a future extension).
    for b in config.SOLAR_BUSES:
        pp.create_sgen(
            net,
            bus=b,
            p_mw=config.DG_EFFECTIVE_MW,
            q_mvar=0.0,
            type="PV",
            name=f"solar_b{b + 1}",    # b+1 to restore article bus number in name
        )
    for b in config.WIND_BUSES:
        pp.create_sgen(
            net,
            bus=b,
            p_mw=config.DG_EFFECTIVE_MW,
            q_mvar=0.0,
            type="WP",
            name=f"wind_b{b + 1}",
        )

    # Record the per-unit nameplate so the sim loop can scale by a 0–1 profile:
    #   net.sgen.loc[mask, "p_mw"] = net.sgen.loc[mask, "p_mw_nameplate"] * profile_pu
    net.sgen["p_mw_nameplate"] = net.sgen["p_mw"]

    # ---- 7. Add RPC shunt capacitors ----
    # PITFALL sign: capacitive = NEGATIVE q_mvar in pandapower (generates reactive power).
    # config.RPC_SHUNTS = {17: -0.4, 32: -0.6} — already negative (capacitive).
    for bus, qmvar in config.RPC_SHUNTS.items():
        pp.create_shunt(
            net,
            bus=bus,
            q_mvar=qmvar,      # capacitive: negative q_mvar generates Q
            p_mw=0.0,
            name=f"cap_b{bus + 1}",
        )

    # ---- 8. Return the assembled network ----
    return net, trafo_idx
