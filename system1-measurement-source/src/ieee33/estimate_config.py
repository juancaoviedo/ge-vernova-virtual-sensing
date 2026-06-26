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
    # FASE predict knobs (D-07):
    "forecast_sigma_frac": 0.05,          # per-bus σ ≈ 5% of scheduled load
    "forecast_ar1_rho":    0.3,           # AR(1) correlation coefficient ρ
    "q_floor_scale":       1e-8,          # Q_floor = q_floor_scale * I (Open Q2 default: σ_pmu² ~ 1e-6; 1e-8 conservative)
    "predict_mode":        "fase",        # "fase" | "persistence" (D-04 A/B foil)
}

# ---------------------------------------------------------------------------
# Output bucket name (additive to config.py — estimator output target)
# ---------------------------------------------------------------------------
ESTIMATES_BUCKET: str = "estimates"   # SPEC R8: vm_pu_est, va_degree_est, sigma_vm, sigma_va, trace_P

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
# N_FREE_STATES = 64: from 34-bus network (RESEARCH.md Pitfall 1 + Landmine 1)
#   Buses 0..33 (34 total); distribution buses 0..32 (33 buses) contribute
#   2 states each = 66 entries; minus 2 for slack (θ₃₃=0 fixed, |V|₃₃ known)
#   = 64 free states. State vector: x = [|V|₀,θ₀,...,|V|₃₂,θ₃₂] (64 entries).
# N_BUS_TOTAL = 34: build_enhanced_33bus() inserts HV ext_grid bus at index 33
#   → Ybus from _pd2ppc is 34×34 (not 33×33). Any code initializing at 33 will
#   fail the Ybus shape assertion. This constant encodes that landmine explicitly.
# ---------------------------------------------------------------------------
NEES_CONFIDENCE: float = 0.95   # chi2 band confidence level for NEES/NIS scoring
N_FREE_STATES:   int   = 64     # free state dimension = 2×32 (buses 0..32 minus slack bus 33)
N_BUS_TOTAL:     int   = 34     # total buses in enhanced net (33 distribution + 1 HV ext_grid)
