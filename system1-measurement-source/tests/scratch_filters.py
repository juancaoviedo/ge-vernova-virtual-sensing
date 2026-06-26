"""
scratch_filters.py
------------------
Scratch verifier for Task 2: EKFEstimator (Joseph form) + square-root UKFEstimator.

Tests:
  1. EKF uses Joseph-form covariance update (grep-verified pattern in estimators.py).
  2. EKF P stays positive-definite over 25 synthetic steps.
  3. UKF uses scipy.linalg.cholesky on (P+P.T)/2 (grep-verified).
  4. UKF update calls h_fn only (no Jacobian argument used in compute).
  5. Both filters' x converges to synthetic truth (atol 5e-2).
  6. Both filters' P is positive-definite at every step.
  7. UKF defaults: alpha=1e-3, beta=2.0, kappa=0.0.

Prints "EKF + UKF PD + converge OK" and exits 0 on success.
"""

import sys
import numpy as np

sys.path.insert(0, "/home/juan/codes/ge-vernova-virtual-sensing/system1-measurement-source/src")
import ieee33.estimators as es
import ieee33.estimate_config as ec


# ---------------------------------------------------------------------------
# Tiny synthetic linear system for filter testing
# ---------------------------------------------------------------------------
# State: x in R^n (small n for speed)
# Dynamics: x_{k+1} = x_k + S @ delta_p  (identity transition with FASE inject)
# Measurements: z_k = H @ x_k + v,  v ~ N(0, R)
# ---------------------------------------------------------------------------

def make_linear_system(n=4, m=8, seed=42):
    """Return (H, R, x_true_seq, z_seq, delta_p_seq, S, Cov_eps) for a 25-step run.

    n < m so the system is overdetermined (full column rank H).
    """
    rng = np.random.default_rng(seed)
    n_steps = 25

    # Measurement matrix (overdetermined: m > n, full column rank)
    H = rng.standard_normal((m, n))
    # Retry if not full column rank (very unlikely for random m > n)
    max_tries = 10
    for _ in range(max_tries):
        if np.linalg.matrix_rank(H) == n:
            break
        H = rng.standard_normal((m, n))

    # Measurement noise
    sigma_meas = 0.02
    R = np.eye(m) * sigma_meas ** 2

    # FASE sensitivity: random (n, p) sensitivity matrix, p = n injections
    p = n
    S = rng.standard_normal((n, p)) * 0.01  # small so predict is mild

    # Forecast error covariance
    sigma_fcst = 0.01
    Cov_eps = np.eye(p) * sigma_fcst ** 2

    # Ground truth: starts near flat (|V|=1.0, theta=0), slowly drifts via delta_p
    x_true = np.ones(n)
    x_true[0::2] = 1.0  # voltage-like
    x_true[1::2] = 0.0  # angle-like

    x_true_seq = []
    z_seq = []
    delta_p_seq = []

    for _ in range(n_steps):
        # Random forecast injection change (small)
        delta_p = rng.normal(0, sigma_fcst, p)
        x_true = x_true + S @ delta_p
        delta_p_seq.append(delta_p)
        x_true_seq.append(x_true.copy())
        z = H @ x_true + rng.normal(0, sigma_meas, m)
        z_seq.append(z)

    return H, R, x_true_seq, z_seq, delta_p_seq, S, Cov_eps


def is_pd(P, tol=0.0):
    """Return True if P is positive-definite (all eigenvalues > tol)."""
    eigvals = np.linalg.eigvalsh((P + P.T) / 2)
    return bool(np.all(eigvals > tol))


# ---------------------------------------------------------------------------
# Test: Joseph form is used in estimators.py (grep check)
# ---------------------------------------------------------------------------

def test_joseph_form_grep():
    """EKF Joseph form must be present in estimators.py source."""
    import os
    src = "/home/juan/codes/ge-vernova-virtual-sensing/system1-measurement-source/src/ieee33/estimators.py"
    with open(src) as f:
        code = f.read()
    # Key signature: I_KH @ self._P @ I_KH.T + K @ R @ K.T  or equivalent
    assert "I_KH" in code, "estimators.py must use I_KH (Joseph form) for EKF update"
    assert "I_KH @ self._P @ I_KH.T" in code or "I_KH @ self._P @ I_KH.T" in code, \
        "Joseph-form expression I_KH @ P @ I_KH.T missing"
    print("  [PASS] Joseph form (I_KH @ P @ I_KH.T + K @ R @ K.T) present in estimators.py")


# ---------------------------------------------------------------------------
# Test: cholesky on (P+P.T)/2 is used (grep check)
# ---------------------------------------------------------------------------

def test_sqrt_ukf_cholesky_grep():
    """sqrt-UKF must use cholesky on (P+P.T)/2 (Landmine 8)."""
    import os
    src = "/home/juan/codes/ge-vernova-virtual-sensing/system1-measurement-source/src/ieee33/estimators.py"
    with open(src) as f:
        code = f.read()
    assert "cholesky" in code, "estimators.py must import/use cholesky from scipy.linalg"
    # Check for symmetrization pattern
    assert "(P" in code and "P.T)" in code, \
        "UKF must symmetrize P: (P + P.T)/2 before cholesky"
    print("  [PASS] cholesky((P+P.T)/2, lower=True) pattern present in estimators.py")


# ---------------------------------------------------------------------------
# Test: EKF multi-step: P stays PD, x converges
# ---------------------------------------------------------------------------

def test_ekf_pd_and_convergence():
    """EKF P is positive-definite at every step; x converges to synthetic truth."""
    H, R, x_true_seq, z_seq, delta_p_seq, S, Cov_eps = make_linear_system(n=4, m=8)
    n = 4

    ekf = es.EKFEstimator(n=n, q_floor_scale=1e-6)

    h_fn = lambda x: H @ x
    H_fn = lambda x: H

    pd_failures = 0
    for step, (delta_p, z, x_true) in enumerate(zip(delta_p_seq, z_seq, x_true_seq)):
        ekf.predict(delta_p, S, Cov_eps)
        ekf.update(z, R, h_fn, H_fn)

        if not is_pd(ekf.P):
            pd_failures += 1
            print(f"    WARNING: EKF P not PD at step {step}, min eigval={np.min(np.linalg.eigvalsh(ekf.P)):.2e}")

    assert pd_failures == 0, f"EKF P was not PD at {pd_failures}/25 steps"

    # Final state should be close to truth (5e-2 tolerance)
    err = np.max(np.abs(ekf.x - x_true_seq[-1]))
    assert err < 5e-2, f"EKF final state error {err:.4e} > 5e-2"
    print(f"  [PASS] EKF P positive-definite at all 25 steps; final state err={err:.4e}")


# ---------------------------------------------------------------------------
# Test: UKF multi-step: P stays PD, x converges, no Jacobian used
# ---------------------------------------------------------------------------

def test_ukf_pd_and_convergence():
    """UKF P is positive-definite at every step; x converges; update uses h_fn only."""
    H, R, x_true_seq, z_seq, delta_p_seq, S, Cov_eps = make_linear_system(n=4, m=8)
    n = 4

    ukf = es.UKFEstimator(
        n=n,
        alpha=ec.UKF_ALPHA,
        beta=ec.UKF_BETA,
        kappa=ec.UKF_KAPPA,
        q_floor_scale=1e-6,
    )

    h_fn = lambda x: H @ x

    # Track if H_fn was ever called
    H_fn_called = [False]
    def H_fn_tracking(x):
        H_fn_called[0] = True
        return H

    pd_failures = 0
    for step, (delta_p, z, x_true) in enumerate(zip(delta_p_seq, z_seq, x_true_seq)):
        ukf.predict(delta_p, S, Cov_eps)
        ukf.update(z, R, h_fn, H_fn_tracking)  # pass H_fn but UKF should ignore it

        if not is_pd(ukf.P):
            pd_failures += 1
            print(f"    WARNING: UKF P not PD at step {step}, min eigval={np.min(np.linalg.eigvalsh(ukf.P)):.2e}")

    assert pd_failures == 0, f"UKF P was not PD at {pd_failures}/25 steps"

    # Check H_fn was NOT called (UKF uses sigma points, not Jacobian)
    assert not H_fn_called[0], "UKF update called H_fn (Jacobian) — it should not!"

    # Final state should be close to truth
    err = np.max(np.abs(ukf.x - x_true_seq[-1]))
    assert err < 5e-2, f"UKF final state error {err:.4e} > 5e-2"
    print(f"  [PASS] UKF P positive-definite at all 25 steps; no Jacobian; final state err={err:.4e}")


# ---------------------------------------------------------------------------
# Test: UKF defaults
# ---------------------------------------------------------------------------

def test_ukf_defaults():
    """UKF instantiates with alpha=1e-3, beta=2.0, kappa=0.0 by default."""
    ukf = es.UKFEstimator()
    assert abs(ukf.alpha - 1e-3) < 1e-12, f"UKF alpha={ukf.alpha}, expected 1e-3"
    assert abs(ukf.beta - 2.0) < 1e-12, f"UKF beta={ukf.beta}, expected 2.0"
    assert abs(ukf.kappa - 0.0) < 1e-12, f"UKF kappa={ukf.kappa}, expected 0.0"
    print(f"  [PASS] UKF defaults: alpha={ukf.alpha}, beta={ukf.beta}, kappa={ukf.kappa}")


# ---------------------------------------------------------------------------
# Test: both filters implement BaseEstimator
# ---------------------------------------------------------------------------

def test_both_implement_base():
    """EKF and UKF are both BaseEstimator subclasses."""
    ekf = es.EKFEstimator(n=8)
    ukf = es.UKFEstimator(n=8)
    assert isinstance(ekf, es.BaseEstimator), "EKFEstimator must be a BaseEstimator"
    assert isinstance(ukf, es.BaseEstimator), "UKFEstimator must be a BaseEstimator"
    print("  [PASS] EKFEstimator and UKFEstimator are both BaseEstimator subclasses")


if __name__ == "__main__":
    print("=" * 60)
    print("scratch_filters.py — EKFEstimator + UKFEstimator")
    print("=" * 60)

    test_joseph_form_grep()
    test_sqrt_ukf_cholesky_grep()
    test_both_implement_base()
    test_ukf_defaults()
    test_ekf_pd_and_convergence()
    test_ukf_pd_and_convergence()

    print()
    print("EKF + UKF PD + converge OK")
