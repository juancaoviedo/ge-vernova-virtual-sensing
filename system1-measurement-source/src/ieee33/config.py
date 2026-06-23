"""
config.py
---------
All physical, data, and infrastructure constants for the IEEE 33-bus DER measurement
source. This module is pure constants — no I/O side effects beyond loading the .env
file at import time via python-dotenv.

Downstream modules (ingest.py, sim.py, validate.py, network.py) import from here;
no constant is duplicated elsewhere.

Dependencies: python-dotenv
Run:          imported — not executed directly
Effect:       Exposes constants for OPSD data source, network topology, DG sizing,
              InfluxDB connection, and validation tolerances.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# OPSD profile data source (RESEARCH §Pattern 3, verified HTTP 200 2026-06-23)
# ---------------------------------------------------------------------------
OPSD_URL = (
    "https://data.open-power-system-data.org/time_series/2020-10-06/"
    "time_series_15min_singleindex.csv"
)

# D-15: TARGET_DATE — concrete DE day selected once via scripts/inspect_opsd_day.py
# Chosen: 2017-06-07 (DE summer; solar_max=0.474, wind_mean=0.708; 96 non-null rows; zero NaN)
# Criteria: high solar CF + wind_mean > 0.30 + exactly 96 rows + zero NaN across all three columns
# Re-run scripts/inspect_opsd_day.py to reproduce the selection rationale.
TARGET_DATE = "2017-06-07"   # D-15: high-DER DE day, 96 non-null rows, hard-coded

OPSD_COLS = [
    "utc_timestamp",
    "DE_load_actual_entsoe_transparency",
    "DE_solar_profile",
    "DE_wind_profile",
]
N_STEPS = 96                        # 96 × 15-min = one full day

# ---------------------------------------------------------------------------
# Load scaling anchor (D-03)
# ---------------------------------------------------------------------------
PEAK_LOAD_MW   = 3.715              # MW    article total demand anchored as daily PEAK (D-03)
PEAK_LOAD_MVAR = 2.3                # MVAr  article total reactive demand at peak

# ---------------------------------------------------------------------------
# DG nameplate and scaling (case33.xlsx generator data; D-04)
# Article bus N = pandapower index N-1 (0-indexed).
# ---------------------------------------------------------------------------
DG_NAMEPLATE_MW = 0.2               # MW    case33.xlsx: 200 kW per unit at buses 18/22/25/33

# D-04: DELIBERATE DEVIATION from article's 200 kW baseline.
# Raw nameplate total = 4 × 0.2 MW = 0.8 MW ≈ 21% of 3.715 MW peak — too small to
# produce visible midday reverse flow, voltage rise, or OLTC tapping (RESEARCH Pitfall 5).
# Scale factor 2.8 raises each unit to 0.56 MW; 4 × 0.56 = 2.24 MW ≈ 60% of peak.
# This surfaces the interview-grade physics: midday PV pushes voltage above 1.0 pu,
# power flows back toward the substation, the OLTC taps to hold the 0.95–1.05 band.
# Benchmark proportions are preserved (all four units scaled equally).
DG_SCALE_FACTOR = 2.8               # —     D-04: documented deliberate deviation (×2.8 from article nameplate)
DG_EFFECTIVE_MW = DG_NAMEPLATE_MW * DG_SCALE_FACTOR   # MW  = 0.56 MW per unit

# ---------------------------------------------------------------------------
# Solar/wind bus split (D-05)
# Pandapower 0-indexed: article bus N → index N-1
# Solar: article buses 18, 22 → pandapower indices 17, 21
# Wind:  article buses 25, 33 → pandapower indices 24, 32
# ---------------------------------------------------------------------------
SOLAR_BUSES = [17, 21]              # pandapower indices for solar DG (article buses 18, 22)
WIND_BUSES  = [24, 32]              # pandapower indices for wind DG  (article buses 25, 33)

# ---------------------------------------------------------------------------
# RPC shunt capacitors (case33.xlsx rows 40, 55; capacitive = NEGATIVE q_mvar in pandapower)
# Article bus 18 → idx 17: 0.4 MVAr capacitive
# Article bus 33 → idx 32: 0.6 MVAr capacitive
# ---------------------------------------------------------------------------
RPC_SHUNTS = {17: -0.4, 32: -0.6}  # {pp_bus_idx: q_mvar}  negative = capacitive (generates Q)

# ---------------------------------------------------------------------------
# Tie-lines (case33.xlsx rows 102-104; open for radial configuration)
# Article branches 33, 34, 35 → pandapower line indices 32, 33, 34
# ---------------------------------------------------------------------------
TIE_LINE_IDX = [32, 33, 34]        # pandapower line indices; in_service=False for radial

# ---------------------------------------------------------------------------
# Line thermal rating
# case33bw ships max_i_ka = 99999 (placeholder) on every line, so loading_percent
# comes out ≈ 0.0001 % (meaningless). Set a nominal 12.66 kV feeder conductor
# ampacity so loading_percent is realistic (trunk near the substation ≈ 40-50 % at
# peak, tapering toward the laterals). Affects loading_percent only — NOT the power
# flow solution (vm_pu / P / Q are unchanged by the rating).
# ---------------------------------------------------------------------------
LINE_MAX_I_KA = 0.4                 # kA   nominal feeder conductor ampacity (~400 A)

# ---------------------------------------------------------------------------
# Feeder transformer (OLTC + phase shifter) parameters
# Inserted between a new HV bus and bus 0; a line-drop-compensation controller
# (FeederTapControl in network.py) regulates a downstream reference bus.
# ---------------------------------------------------------------------------
TRAFO_SN_MVA        = 10.0          # MVA   feeder rating
TRAFO_VK_PERCENT    = 4.0           # %     short-circuit voltage
TRAFO_VKR_PERCENT   = 0.5           # %     resistive component
TAP_MIN             = -5            # —     minimum tap position (boost: −5 × 1% steps = +5% at LV)
TAP_MAX             =  5            # —     maximum tap position (buck:  +5 × 1% steps = −5% at LV)
TAP_STEP_PERCENT    = 1.0           # %     voltage change per tap step
TAP_NEUTRAL         = 0             # —     neutral tap position (ratio = 1.0)
SHIFT_DEGREE        = 0.0           # deg   scheduled phase-shift angle at baseline (±5° range)

# pandapower 3.x REQUIRES tap_changer_type to be set for the tap to affect the power
# flow. create_transformer_from_parameters leaves it NaN by default, which makes the
# tap INERT (changing tap_pos has zero effect on voltage). "Ratio" = standard OLTC
# voltage-ratio tap changer. (Found via the OLTC-never-tapped investigation.)
TAP_CHANGER_TYPE    = "Ratio"

# OLTC regulation strategy: line-drop compensation.
# case33bw is fed from a stiff slack, so bus 0 (the trafo LV bus, adjacent to the
# slack) barely moves (0.993-0.997 pu) — regulating it never moves the tap. Instead
# regulate a representative DOWNSTREAM main-trunk bus to ~1.0 pu, so the tap actively
# boosts at evening peak and backs off under midday DER → visible daily switching,
# and the sagging laterals are lifted above 0.95 pu. tap_changer/band tuned against
# the real 96-step day: tap ranges −1..−4, day vmin≈0.985, day vmax≈1.037.
OLTC_REF_BUS        = 17            # pandapower idx (article bus 18, end of main trunk) — regulated bus
OLTC_VM_LOWER_PU    = 0.99         # pu    regulate OLTC_REF_BUS into [0.99, 1.01] (1.0 ±1%)
OLTC_VM_UPPER_PU    = 1.01         # pu

# ---------------------------------------------------------------------------
# Validation constants (D-14)
# ---------------------------------------------------------------------------
BARANWU_VMIN_PU  = 0.913           # pu    Baran & Wu published min voltage (base case, no DER/caps/OLTC)
BARANWU_VMIN_BUS = 17              # —     pandapower index (article bus 18)
BARANWU_TOL      = 0.005           # pu    acceptable tolerance on Baran & Wu assertion
VBAND_LOW        = 0.95            # pu    voltage band lower limit (SPEC req 2)
VBAND_HIGH       = 1.05            # pu    voltage band upper limit (SPEC req 2)

# ---------------------------------------------------------------------------
# InfluxDB connection (loaded from .env; fall back to local dev defaults)
# ---------------------------------------------------------------------------
INFLUXDB_URL     = os.getenv("INFLUXDB_URL",   "http://localhost:8086")
INFLUXDB_TOKEN   = os.getenv("INFLUXDB_TOKEN", "ieee33-dev-token")
INFLUXDB_ORG     = os.getenv("INFLUXDB_ORG",   "ieee33")
PROFILES_BUCKET  = "profiles"                   # one-time ingest of 96-step load/solar/wind (D-06)
STATE_BUCKET     = "state"                      # per-run power-flow snapshots (D-06)
