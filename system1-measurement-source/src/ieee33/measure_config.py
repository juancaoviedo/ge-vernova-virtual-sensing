"""
measure_config.py
-----------------
All measurement-layer knobs for the IEEE 33-bus observability / sensor-model layer.
This module is **pure constants — no I/O side effects** (no load_dotenv, no file reads,
no datetime.now, no np.random). Downstream modules (measure.py) import from here;
no constant is duplicated elsewhere.

Forward contract: every Plan 03/04 runner and Plan 05 test imports CLASS_SIGMA, CADENCE,
SCENARIOS, ACTIVE, and QUANT_LSB from this single source of truth.  The ACTIVE block is
the PRIMARY switch (D-09): edit it to change experiment without touching runner code.

Dependencies: stdlib only (no third-party imports)
Run:          imported — not executed directly
Effect:       Exposes pure constants for the Phase 9 measurement-layer configuration.
"""

# ---------------------------------------------------------------------------
# Per-class noise sigma table (D-11)
#
# Values are FRACTION of |measured value| EXCEPT pmu.va_degree which is
# ABSOLUTE radians (GPS-disciplined PMU angle precision is independent of
# the angle magnitude).
#
# Mapping to DSSE taxonomy:
#   scada    — substation SCADA RTU metering (bus 0; telemetered P/Q/|V|)
#   pmu      — micro-PMU synchrophasor (|V| + angle, GPS-stamped)
#   ami      — advanced metering infrastructure (hourly AMI reads → P_inj)
#   der      — DER inverter telemetry (P/Q from smart-inverter registers)
#   pseudo   — load-forecast pseudo-measurements (large σ; last resort)
#   zero_inj — virtual zero-injection measurements at junction buses (near-exact)
# ---------------------------------------------------------------------------
CLASS_SIGMA: dict[str, dict[str, float]] = {
    "scada":    {
        "vm_pu":      0.005,   # D-11: 0.5% of |V| (RTU voltage transducer)
        "p_inj_mw":   0.02,    # D-11: 2% of P (revenue-grade CT/PT)
        "q_inj_mvar": 0.02,    # D-11: 2% of Q (revenue-grade CT/PT)
    },
    "pmu":      {
        "vm_pu":   0.001,      # D-11: 0.1% of |V| (micro-PMU accuracy class)
        "va_degree": 0.0003,   # D-11: 0.0003 rad ABSOLUTE (GPS-disciplined; ~0.017°)
    },
    "ami":      {
        "p_inj_mw":   0.03,   # D-11: 3% of P (residential/commercial smart meter)
        "q_inj_mvar": 0.03,   # D-11: 3% of Q
    },
    "der":      {
        "p_mw":   0.015,       # D-11: 1.5% of P (smart-inverter Modbus register)
        "q_mvar": 0.015,       # D-11: 1.5% of Q
    },
    "pseudo":   {
        "p_inj_mw":   0.30,   # D-11: 30% of P (load-forecast uncertainty; large σ by design)
        "q_inj_mvar": 0.30,   # D-11: 30% of Q
    },
    "zero_inj": {
        "p_inj_mw":   1e-4,   # D-11: near-exact (physical: P≈0 at unloaded junction bus)
        "q_inj_mvar": 1e-4,   # D-11: near-exact
    },
}

# ---------------------------------------------------------------------------
# Quantization LSBs — per-class, per-quantity (D-13 / RESEARCH Q3)
#
# LSB = least-significant-bit of the ADC / register resolution.  The instrument
# noise model quantizes the true value BEFORE adding the AR(1) random term.
# For snapshot and gaussian modes this table is informational only (unused).
# ---------------------------------------------------------------------------
QUANT_LSB: dict[str, dict[str, float]] = {
    "scada":    {
        "vm_pu":      0.001,   # 16-bit ADC over ±2 pu range ≈ 6×10⁻⁵; 0.001 matches SCADA display resolution
        "p_inj_mw":   0.01,
        "q_inj_mvar": 0.01,
    },
    "pmu":      {
        "vm_pu":   0.0001,     # 24-bit converter; 0.0001 pu matches IEC 61869-9 class 0.1
        "va_degree": 0.001,    # 0.001° ≈ 1.7×10⁻⁵ rad; matches typical FPGA accumulator
    },
    "ami":      {
        "p_inj_mw":   0.001,  # kWh meter: 1 Wh pulse → 0.001 kW at 15-min interval
        "q_inj_mvar": 0.001,
    },
    "der":      {
        "p_mw":   0.001,       # inverter Modbus: 1 W resolution → 0.001 MW
        "q_mvar": 0.001,
    },
    "pseudo":   {
        "p_inj_mw":   0.001,  # derived from load forecast; quantisation is notional
        "q_inj_mvar": 0.001,
    },
    "zero_inj": {
        "p_inj_mw":   0.001,  # virtual; quantisation notional (value is always ~0)
        "q_inj_mvar": 0.001,
    },
}

# ---------------------------------------------------------------------------
# Multirate cadence — per source, per class (D-14)
#
# cadence k: in multirate_async mode emit measurement only when
#   step_idx % k == 0
# So k=1 → every step; k=4 → every 4th step (hourly for 15-min day steps).
# In snapshot mode this table is IGNORED (all classes emit every step).
#
# day   source: 96 steps × 15 min = one full day
#   AMI every 4 steps = 1-hour AMI reads (realistic; actual AMI push is hourly)
#   Others every step = high-frequency telemetry + SCADA polling
#
# fault source: 40 steps × 3 s = 2-min fault/reconfiguration event
#   SCADA every 2 steps = 6-s SCADA scan rate (typical RTU polling)
#   AMI every 10 steps = AMI essentially blind to the 2-min event
#   Others every step = PMU/DER stream at 3-s granularity
# ---------------------------------------------------------------------------
CADENCE: dict[str, dict[str, int]] = {
    "day":   {
        "scada":    1,   # D-14: every step (SCADA 15-min telemetry)
        "pmu":      1,   # D-14: every step (PMU high-frequency)
        "der":      1,   # D-14: every step (inverter telemetry)
        "ami":      4,   # D-14: every 4th step → 1-hour AMI cycle
        "pseudo":   1,   # D-14: every step (forecast always available)
        "zero_inj": 1,   # D-14: every step (virtual; always present)
    },
    "fault": {
        "scada":    2,   # D-14: every 2nd step → 6-s SCADA scan rate
        "pmu":      1,   # D-14: every step (PMU 3-s stream)
        "der":      1,   # D-14: every step (inverter real-time)
        "ami":      10,  # D-14: every 10th step → AMI blind during 30-s window
        "pseudo":   1,   # D-14: every step
        "zero_inj": 1,   # D-14: every step
    },
}

# ---------------------------------------------------------------------------
# Sensor-bus assignments per scenario (D-04, D-05)
#
# Pandapower 0-indexed: bus 0 = feeder-head/slack (substation LV bus, no load).
# Loads on buses 1..32. DG sgens at 17, 21, 24, 32 (article buses 18, 22, 25, 33).
# Bus 17 is INSIDE the dead zone during the fault (D-03: goes dark on isolation).
#
# Quantity assignments per class:
#   scada    → vm_pu, p_inj_mw, q_inj_mvar
#   pmu      → vm_pu, va_degree
#   ami      → p_inj_mw  (Q_inj optionally available where marked)
#   der      → p_mw, q_mvar
#   pseudo   → p_inj_mw, q_inj_mvar  (derived at runtime = load buses not covered by real sensors)
#   zero_inj → p_inj_mw, q_inj_mvar  (virtual; value ≈ 0; very high weight)
# ---------------------------------------------------------------------------
SCENARIOS: dict[str, dict] = {

    # ------------------------------------------------------------------
    # realistic_sparse (D-04)
    # Real-only redundancy < 1.0 → system is UNDER-OBSERVABLE without pseudo.
    # Redundancy ≥ 1.0 only AFTER pseudo padding.
    # Designed to stress the System 2 estimator: limited telemetry, one PMU
    # in the dead zone (bus 17 goes dark during fault).
    # ------------------------------------------------------------------
    "realistic_sparse": {
        # D-04: feeder-head SCADA
        "scada":    [0],
        # D-04: 3 micro-PMUs — bus 17 (DG + dead-zone candidate), 24 (wind DG),
        #       30 (healthy lateral node)
        "pmu":      [17, 24, 30],
        # D-04: all 4 DER inverters report P, Q
        "der":      [17, 21, 24, 32],
        # D-04: ~30% of load buses (10 buses); selection covers main trunk + one lateral
        "ami":      [3, 6, 9, 12, 15, 18, 21, 24, 28, 31],
        # D-04: virtual zero-injection buses — none assigned in sparse scenario
        "zero_inj": [],
        # D-04: pseudo = all load buses 1..32 NOT covered by scada/pmu/ami/der/zero_inj
        #        (derived at runtime by measure.py; listed here for documentation)
        # pseudo_comment: "runtime-derived: every load bus 1..32 not in {pmu ∪ ami ∪ der ∪ zero_inj}",
    },

    # ------------------------------------------------------------------
    # well_observed (D-05)
    # Real-measurement redundancy > 1.0 WITHOUT pseudo — system is OBSERVABLE.
    # 9 micro-PMUs across the main trunk, ~80% AMI coverage, zero-injection
    # virtual measurements at junction buses.
    # AMI list: all load buses 1..32 EXCEPT held-out set {5,10,20,25,29}
    # AND except buses already carrying a μPMU {0,4,8,13,17,21,24,28,32}
    # (a PMU already provides vm_pu+va_degree; no duplicate AMI needed).
    # Explicit list so the config is greppable (not computed implicitly).
    # ------------------------------------------------------------------
    "well_observed": {
        # D-05: feeder-head SCADA
        "scada":    [0],
        # D-05: 9 micro-PMUs across the full main trunk
        "pmu":      [0, 4, 8, 13, 17, 21, 24, 28, 32],
        # D-05: all 4 DER inverters
        "der":      [17, 21, 24, 32],
        # D-05: ~80% AMI coverage (explicit list)
        # All load buses 1..32 MINUS held-out {5,10,20,25,29}
        #   MINUS PMU-covered {0,4,8,13,17,21,24,28,32}
        # Result: {1,2,3,6,7,9,11,12,14,15,16,18,19,22,23,26,27,30,31}
        # (buses not held-out and not PMU-covered)
        "ami": [1, 2, 3, 6, 7, 9, 11, 12, 14, 15, 16, 18, 19, 22, 23, 26, 27, 30, 31],
        # D-05: 2 virtual zero-injection buses at major junction nodes
        "zero_inj": [2, 19],
        # D-05: pseudo not needed (real redundancy > 1.0), but still available if requested
    },
}

# ---------------------------------------------------------------------------
# Noise model defaults (D-12, D-13)
#
# OUTLIER_FRACTION and OUTLIER_SPIKE_MULT govern the "gaussian_outliers" model (D-12):
#   on a random fraction f of measurements, replace the Gaussian noise sample with a
#   gross error of magnitude ~OUTLIER_SPIKE_MULT × σ (random sign).  Designed to
#   exercise bad-data detection / χ²-test machinery in System 2.
#
# INSTRUMENT_BIAS_SCALE and INSTRUMENT_AR1_RHO govern the "instrument" model (D-13):
#   INSTRUMENT_BIAS_SCALE: per-sensor systematic bias ≈ +bias_scale × |true_value|
#     (fixed per-run, seed-derived, reproducible — simulates instrument calibration drift).
#   INSTRUMENT_AR1_RHO: AR(1) temporal correlation coefficient ρ for the random term.
#     ε_t = ρ·ε_{t−1} + (1-ρ)·w_t, where w_t ~ N(0, σ²).  ρ=0.7 gives moderate
#     temporal autocorrelation (real RTU/PMU noise is correlated, not iid).
# ---------------------------------------------------------------------------
OUTLIER_FRACTION:     float = 0.03    # D-12: 3% of measurements are gross errors
OUTLIER_SPIKE_MULT:   float = 15.0   # D-12: gross error magnitude ≈ 15 × σ (random sign)
INSTRUMENT_BIAS_SCALE: float = 0.005  # D-13: per-sensor bias ≈ 0.5% of |value| (seed-derived)
INSTRUMENT_AR1_RHO:   float = 0.7    # D-13: AR(1) temporal correlation coefficient ρ

# ---------------------------------------------------------------------------
# Measurements bucket schema vocabulary (D-06 forward contract)
#
# System 2 (the estimator) reads from MEASUREMENTS_BUCKET and must match
# these exact tag/field names. This block is the binding interface contract.
#
# Tags on every meas point:
#   class      : one of MEAS_CLASSES
#   quantity   : one of MEAS_QUANTITIES
#   location   : bus_id (str)
#   scenario   : one of SCENARIOS keys ("well_observed" | "realistic_sparse")
#   experiment : "day" | "fault"
#   phase      : fault only ("pre_fault" | "faulted_isolated" | "restored")
#
# Fields on every meas point:
#   value         : float — noisy sensor reading (the observable z)
#   assumed_sigma : float — σ value the estimator should use for this reading
#
# CRITICAL — NO true_value FIELD:
#   The true (ground-truth) value lives only in the `state` / `fault_event`
#   buckets owned by System 1.  Keeping true_value OUT of `measurements` is a
#   hard contract (SPEC R9 / D-06): System 2 must not be able to "peek" at
#   truth, and the scoring oracle (System 3) must compare estimate vs truth
#   independently.  DO NOT add true_value to any Point written to this bucket.
# ---------------------------------------------------------------------------
MEAS_MEASUREMENT:  str       = "meas"
MEAS_CLASSES:      list[str] = ["scada", "pmu", "ami", "der", "pseudo", "zero_inj"]
MEAS_QUANTITIES:   list[str] = [
    "vm_pu",       # bus voltage magnitude [per-unit]
    "va_degree",   # bus voltage angle [degrees] — pmu only
    "p_inj_mw",    # bus net active power injection [MW] (+ = generation, − = load convention)
    "q_inj_mvar",  # bus net reactive power injection [MVAr]
    "p_mw",        # DER/sgen active output [MW]    (der class only)
    "q_mvar",      # DER/sgen reactive output [MVAr] (der class only)
]
MEASUREMENTS_BUCKET: str = "measurements"  # D-06: new InfluxDB bucket for Phase 9 output

# ---------------------------------------------------------------------------
# ACTIVE BLOCK — edit this to switch experiments without touching runner code (D-09)
#
# This dict is the PRIMARY config switch (user emphasis + D-09).  The measure.py
# runner loads ACTIVE at startup and can optionally override individual keys via
# CLI flags (--scenario, --source, --sampling, --noise, --seed) for sweep runs.
# ---------------------------------------------------------------------------
ACTIVE: dict = {
    "scenario": "realistic_sparse",   # "well_observed" | "realistic_sparse" (D-04/D-05)
    "source":   "day",                # "day" (96×15min state) | "fault" (40×3s fault_event)
    "sampling": "snapshot",           # "snapshot" (all classes every step) | "multirate_async" (D-14 cadences)
    "noise":    "gaussian",           # "gaussian" | "gaussian_outliers" (D-12) | "instrument" (D-13)
    "seed":     42,                   # RNG seed for deterministic noise (SPEC R10)
    "assumed_sigma_scale": 1.0,       # multiply CLASS_SIGMA to get assumed_sigma written to bucket
                                      # 1.0 = unbiased (estimator sees true σ); >1 = over-cautious; <1 = over-confident
}
