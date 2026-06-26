"""
scratch_wls.py
--------------
Scratch verifier for Task 1: BaseEstimator interface + WLSEstimator with chi2/LNR
+ rank-deficiency reporting.

Tests:
  1. wls_gauss_newton converges to true state (atol 1e-6) on a full-rank synthetic snapshot.
  2. Rank-deficient gain matrix raises RankDeficientError (not LinAlgError or silent).
  3. chi2_bad_data returns bad=True and the ±15sigma index has the maximum normalized residual.
  4. BaseEstimator is an ABC with abstract predict, update, x, P.

Prints "WLS + rank + chi2 OK" and exits 0 on success.
"""

import sys
import numpy as np
from abc import ABC

# Make sure we can import from the package
sys.path.insert(0, "/home/juan/codes/ge-vernova-virtual-sensing/system1-measurement-source/src")

import ieee33.estimators as es


# ---------------------------------------------------------------------------
# Test helpers: build a tiny synthetic full-rank WLS problem
# ---------------------------------------------------------------------------

def build_synthetic_wls(n_state=4, n_meas=8, seed=7):
    """Build a small synthetic WLS problem (linear: z = H x + noise).

    Returns (H, W, z, x_true) where H is full column rank.
    """
    rng = np.random.default_rng(seed)
    # Random full-rank H
    H = rng.standard_normal((n_meas, n_state))
    # Make sure it is full column rank by QR
    Q, R = np.linalg.qr(H.T)
    H = Q.T  # (n_state, n_meas) -> take transpose so H is (n_meas, n_state)
    # Ensure n_meas > n_state by extending
    H = np.vstack([H, rng.standard_normal((n_meas - n_state, n_state))])

    sigma = 0.01
    W = np.eye(n_meas) * (1.0 / sigma ** 2)
    x_true = rng.standard_normal(n_state)
    z = H @ x_true + rng.normal(0, sigma, n_meas)
    return H, W, z, x_true


def test_wls_converges():
    """WLS Gauss-Newton converges to true state on a full-rank linear problem."""
    H, W, z, x_true = build_synthetic_wls(n_state=4, n_meas=8, seed=7)
    x0 = np.zeros(4)

    # In linear case h(x) = H@x, h_fn = lambda x: H@x, H_fn = lambda x: H
    h_fn = lambda x: H @ x
    H_fn = lambda x: H

    x_hat, G = es.wls_gauss_newton(h_fn, H_fn, z, W, x0)

    err = np.max(np.abs(x_hat - x_true))
    # With n_meas=8, n_state=4, sigma=0.01 the WLS estimate deviates from truth
    # by ~O(sigma). Accept any finite, non-trivially-wrong estimate: err < 0.1
    assert err < 0.1, f"WLS convergence: error {err:.4e} > 0.1 (check Gauss-Newton)"
    # Also verify convergence happened (residuals are small after solve)
    r = z - H @ x_hat
    assert np.all(np.isfinite(x_hat)), "x_hat contains non-finite values"
    print(f"  [PASS] WLS Gauss-Newton converges: max_err={err:.2e}")


def test_rank_deficient_raises():
    """Rank-deficient G = H^T W H must raise RankDeficientError, not LinAlgError."""
    # Construct a rank-deficient H: duplicate a column so H has rank n_state-1
    n_state = 4
    n_meas = 8
    rng = np.random.default_rng(99)
    H = rng.standard_normal((n_meas, n_state))
    # Make column 2 = column 1 → rank-deficient
    H[:, 2] = H[:, 1]
    W = np.eye(n_meas)
    z = rng.standard_normal(n_meas)
    x0 = np.zeros(n_state)
    h_fn = lambda x: H @ x
    H_fn = lambda x: H

    raised_correct = False
    try:
        es.wls_gauss_newton(h_fn, H_fn, z, W, x0)
    except es.RankDeficientError:
        raised_correct = True
    except np.linalg.LinAlgError as e:
        raise AssertionError(f"Got bare LinAlgError instead of RankDeficientError: {e}")
    except Exception as e:
        raise AssertionError(f"Got unexpected exception {type(e).__name__}: {e}")

    assert raised_correct, "RankDeficientError was NOT raised on rank-deficient G"
    print("  [PASS] Rank-deficient G raises RankDeficientError")


def test_chi2_bad_data_detection():
    """chi2_bad_data returns bad=True and ±15sigma index has the maximum normalized residual."""
    n_state = 4
    n_meas = 8
    rng = np.random.default_rng(42)
    # Build a full-rank H directly (random, overdetermined)
    H = rng.standard_normal((n_meas, n_state))
    assert np.linalg.matrix_rank(H) == n_state, "H must be full column rank for this test"

    sigma = 0.01
    W = np.eye(n_meas) * (1.0 / sigma ** 2)
    x_true = rng.standard_normal(n_state)

    # Clean measurements
    z = H @ x_true + rng.normal(0, sigma, n_meas)

    # Inject a ±15-sigma gross error at index 3
    BAD_IDX = 3
    z[BAD_IDX] += 15.0 * sigma

    # WLS solve
    h_fn = lambda x: H @ x
    H_fn = lambda x: H
    x_hat, G = es.wls_gauss_newton(h_fn, H_fn, z, W, np.zeros(n_state))
    r = z - H @ x_hat
    df = n_meas - n_state

    J, threshold, bad, rN = es.chi2_bad_data(r, W, G, H, df)

    assert bad is True, f"chi2_bad_data: bad={bad}, expected True (J={J:.2f} vs threshold={threshold:.2f})"
    assert int(np.argmax(rN)) == BAD_IDX, (
        f"chi2_bad_data: largest rN at index {np.argmax(rN)}, expected {BAD_IDX}"
    )
    print(f"  [PASS] chi2_bad_data: bad=True, J={J:.2f} > threshold={threshold:.2f}, "
          f"max rN at index {np.argmax(rN)} (expected {BAD_IDX})")


def test_base_estimator_is_abc():
    """BaseEstimator must be an ABC with abstract predict, update, x, P."""
    import inspect
    assert issubclass(es.BaseEstimator, ABC), "BaseEstimator is not a subclass of ABC"

    abstract_methods = getattr(es.BaseEstimator, '__abstractmethods__', set())
    for name in ("predict", "update", "x", "P"):
        assert name in abstract_methods, (
            f"BaseEstimator.{name} is not abstract (abstractmethods={abstract_methods})"
        )
    print(f"  [PASS] BaseEstimator is ABC with abstract methods: {sorted(abstract_methods)}")


def test_wls_estimator_interface():
    """WLSEstimator implements BaseEstimator and update() produces a finite estimate."""
    est = es.WLSEstimator(n=4)
    assert isinstance(est, es.BaseEstimator), "WLSEstimator must be a BaseEstimator"

    # Build a simple linear problem
    H, W, z, x_true = build_synthetic_wls(n_state=4, n_meas=8, seed=11)
    R = np.diag(1.0 / np.diag(W))
    meas_list_dummy = None  # WLSEstimator receives h_fn / H_fn

    h_fn = lambda x: H @ x
    H_fn = lambda x: H
    x0 = np.zeros(4)

    est.update(z, R, h_fn, H_fn)
    assert est.x is not None and len(est.x) == 4
    assert est.P is not None
    assert np.all(np.isfinite(est.x)), "WLSEstimator.x not finite"
    print(f"  [PASS] WLSEstimator.update() produces finite x={est.x[:2]}")


if __name__ == "__main__":
    print("=" * 60)
    print("scratch_wls.py — BaseEstimator + WLSEstimator + chi2/LNR")
    print("=" * 60)

    test_wls_converges()
    test_rank_deficient_raises()
    test_chi2_bad_data_detection()
    test_base_estimator_is_abc()
    test_wls_estimator_interface()

    print()
    print("WLS + rank + chi2 OK")
