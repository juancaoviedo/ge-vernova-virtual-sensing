"""
estimate_config.py
------------------
All estimator knobs for the IEEE 33-bus System 2 state estimator.
This module is **pure constants — no I/O side effects** (no load_dotenv, no file reads,
no datetime.now, no np.random). Downstream modules (estimate.py, score.py) import from here;
no constant is duplicated elsewhere.

Forward contract: every Plan runner imports ACTIVE and the relevant constant tables
from this single source of truth. The ACTIVE block is the PRIMARY switch: edit it
to change experiment without touching runner code.

Dependencies: stdlib only (no third-party imports)
Run:          imported — not executed directly
"""

# ---------------------------------------------------------------------------
# ACTIVE BLOCK — edit this to switch experiments without touching runner code
# ---------------------------------------------------------------------------
ACTIVE: dict = {
    "scenario":     "realistic_sparse",   # "well_observed" | "realistic_sparse"
    "source":       "day",                # "day" (96-step) | "fault" (40-step)
    "estimator":    "ukf",                # "wls" | "ekf" | "ukf"  (D-02: one per run)
    "seed":         42,                   # RNG seed for forecast-error determinism
    "acceleration": 1.0,                  # wall-clock playback compression (publish only)
    # FASE predict knobs (D-07 / D-09):
    "forecast_sigma_frac":     0.05,      # legacy per-bus σ (kept for backward reference); D-09 splits load/DER
    "forecast_ar1_rho":        0.3,       # AR(1) correlation coefficient ρ for load error (D-09)
    "forecast_load_sigma_frac": 0.04,     # D-09: load AR(1) marginal σ ≈ 4% of scheduled load (band: 3–5%)
    "forecast_der_sigma_frac":  0.22,     # D-09: DER σ ≈ 22% of DER contribution (band: 15–30%)
    "forecast_der_skew":        3.0,      # D-09: skewnorm shape parameter for DER error (right-skewed, larger)
    "q_floor_scale":       1e-8,          # Q_floor = q_floor_scale * I (Open Q2 default: σ_pmu² ~ 1e-6; 1e-8 conservative)
    "predict_mode":        "fase",        # "fase" | "persistence" (D-04 A/B foil)
}

# ---------------------------------------------------------------------------
# Output bucket name (additive to config.py — estimator output target)
# ---------------------------------------------------------------------------
ESTIMATES_BUCKET: str = "estimates"   # SPEC R8: vm_pu_est, va_degree_est, sigma_vm, sigma_va, trace_P

# ---------------------------------------------------------------------------
# Forecast-over-MQTT topic + DER power-factor knob (D-09)
#
# FORECAST_TOPIC_TMPL: the external forecast publisher (forecast.py) publishes
#   per-bus injection forecasts here; the estimator subscribes in 10-10.
#   Format: ieee33/{experiment}/{scenario}/forecast  (e.g. ieee33/day/well_observed/forecast)
#
# FORECAST_DER_POWER_FACTOR: unity pf = DER exports only active power (q_mvar=0),
#   matching network.py sgen q_mvar=0.0 at all four DER buses.  Set < 1.0 to
#   model DER reactive support (future extension); at 1.0 q_fcst for DER buses = 0.
# ---------------------------------------------------------------------------
FORECAST_TOPIC_TMPL:       str   = "ieee33/{experiment}/{scenario}/forecast"   # D-09 topic contract
FORECAST_DER_POWER_FACTOR: float = 1.0    # D-09: unity pf (DER q=0); < 1.0 for reactive support

# ---------------------------------------------------------------------------
# UKF sigma-point parameters (RESEARCH.md Pattern 7 / Van der Merwe & Wan 2001)
#
# Lambda = alpha^2 * (n + kappa) - n  (n=N_FREE_STATES=64)
# alpha = 1e-3  →  lambda ≈ -63.9936  (standard for Gaussian priors; keeps
#                  sigma points close to the mean — appropriate for 64-state
#                  distribution-voltage estimation where deviations are small)
# beta  = 2.0   →  optimal for Gaussian prior distributions
# kappa = 0.0   →  secondary scaling set to zero (standard for continuous state)
#
# Note: if UKF diverges in test, try alpha=0.1 (widens sigma cloud) before
# adjusting beta/kappa (RESEARCH.md Assumption A2).
# ---------------------------------------------------------------------------
UKF_ALPHA: float = 1e-3   # primary spread parameter
UKF_BETA:  float = 2.0    # prior distribution parameter (Gaussian optimal)
UKF_KAPPA: float = 0.0    # secondary scaling (zero = standard choice)

# ---------------------------------------------------------------------------
# AC-WLS Gauss-Newton iteration knobs (RESEARCH.md Pattern 5)
#
# Max 20 iterations is sufficient for distribution networks with voltages
# near 1.0 pu (flat start convergence in ≤5 iterations typically).
# Tolerance 1e-6 on ||dx|| matches standard WLS DSSE practice.
# ---------------------------------------------------------------------------
GAUSS_NEWTON_MAX_ITER: int   = 20    # maximum Gauss-Newton iterations per snapshot
GAUSS_NEWTON_TOL:      float = 1e-6  # convergence tolerance on ||dx||_2

# ---------------------------------------------------------------------------
# NEES/NIS covariance calibration (SPEC R11)
#
# NEES_CONFIDENCE = 0.95 → 95% chi2 acceptance band.
# For N=96, n=64: expected band ≈ [61.76, 66.28] (RESEARCH.md Pattern 8).
# N_FREE_STATES = 64: D-11 convention — buses 1..32 (32 non-reference buses × 2
#   = 64 free states). Bus 0 = electrical feeder-head reference (regulated |V|₀,
#   θ₀ = 0, FIXED — NOT an estimated state). Bus 33 = numerical slack fixed
#   inside Ybus (HV ext_grid). State vector: x = [|V|₁,θ₁,...,|V|₃₂,θ₃₂]
#   (64 entries; state index s ↔ pandapower bus s+1).
# N_BUS_TOTAL = 34: build_enhanced_33bus() inserts HV ext_grid bus at index 33
#   → Ybus from _pd2ppc is 34×34 (not 33×33). Any code initializing at 33 will
#   fail the Ybus shape assertion. This constant encodes that landmine explicitly.
# ---------------------------------------------------------------------------
NEES_CONFIDENCE: float = 0.95   # chi2 band confidence level for NEES/NIS scoring
N_FREE_STATES:   int   = 64     # free state dim = 2×32 (buses 1..32; bus 0 fixed reference, bus 33 slack in Ybus)
N_BUS_TOTAL:     int   = 34     # total buses in enhanced net (33 distribution + 1 HV ext_grid)
