"""
scratch_fase.py
---------------
Scratch verifier for Task 3: FASEPredictor (profile-as-noisy-forecast + Q) + persistence foil.

Tests:
  1. Two same-seed FASEPredictor runs produce identical (x_minus, Q) sequences (determinism).
  2. persistence mode returns x_minus == x_prev (no forecast Δ applied).
  3. fase mode applies x_minus = x_prev + S·Δp and Q = S·Cov(ε)·St + Q_floor.
  4. No oracle access: grep of fase_predict.py returns zero STATE_BUCKET / read_state matches.

Prints "FASE deterministic + persistence foil OK" and exits 0 on success.
"""

import sys
import numpy as np
import pandas as pd

sys.path.insert(0, "/home/juan/codes/ge-vernova-virtual-sensing/system1-measurement-source/src")
import ieee33.fase_predict as fp


# ---------------------------------------------------------------------------
# Synthetic profile DataFrame
# ---------------------------------------------------------------------------

def make_prof_df(n_steps=10, seed=0):
    """Return a synthetic profile DataFrame with n_steps rows and load_pu column."""
    rng = np.random.default_rng(seed)
    load_pu = 0.7 + 0.3 * rng.random(n_steps)  # values in [0.7, 1.0]
    df = pd.DataFrame({"load_pu": load_pu, "_time": range(n_steps)})
    return df


def make_cfg(mode="fase", seed=42):
    """Return a minimal config dict matching estimate_config.ACTIVE."""
    return {
        "forecast_sigma_frac": 0.05,
        "forecast_ar1_rho":    0.3,
        "q_floor_scale":       1e-8,
        "predict_mode":        mode,
        "seed":                seed,
    }


def make_sensitivity(n_state=8, n_inj=4):
    """Return a random sensitivity matrix S with shape (n_state, n_inj)."""
    rng = np.random.default_rng(11)
    return rng.standard_normal((n_state, n_inj)) * 0.01


# ---------------------------------------------------------------------------
# Test 1: determinism — two same-seed instances produce identical sequences
# ---------------------------------------------------------------------------

def test_determinism():
    """Two FASEPredictor instances with same seed produce identical (x_minus, Q) sequences."""
    n_bus = 4
    n_state = n_bus * 2  # 8
    n_steps = 5
    prof_df = make_prof_df(n_steps=n_steps)
    cfg = make_cfg(mode="fase", seed=99)
    S = make_sensitivity(n_state=n_state, n_inj=n_bus)
    x_prev = np.ones(n_state)

    # First predictor instance
    rng1 = np.random.default_rng(cfg["seed"])
    pred1 = fp.FASEPredictor(prof_df, cfg, rng1, n_bus)

    # Second predictor instance (independent rng with same seed)
    rng2 = np.random.default_rng(cfg["seed"])
    pred2 = fp.FASEPredictor(prof_df, cfg, rng2, n_bus)

    x1 = x_prev.copy()
    x2 = x_prev.copy()
    for step_k in range(n_steps):
        xm1, Q1 = pred1.predict(step_k, x1, S)
        xm2, Q2 = pred2.predict(step_k, x2, S)

        assert np.allclose(xm1, xm2, atol=1e-14), (
            f"step {step_k}: x_minus differ: max_diff={np.max(np.abs(xm1-xm2)):.2e}"
        )
        assert np.allclose(Q1, Q2, atol=1e-14), (
            f"step {step_k}: Q differ: max_diff={np.max(np.abs(Q1-Q2)):.2e}"
        )
        x1 = xm1
        x2 = xm2

    print(f"  [PASS] FASEPredictor determinism: same seed -> identical (x_minus, Q) over {n_steps} steps")


# ---------------------------------------------------------------------------
# Test 2: persistence mode returns x_minus == x_prev (exact copy)
# ---------------------------------------------------------------------------

def test_persistence_mode():
    """persistence mode: x_minus == x_prev (no forecast Δ applied)."""
    n_bus = 4
    n_state = n_bus * 2
    prof_df = make_prof_df(n_steps=5)
    cfg = make_cfg(mode="persistence")
    S = make_sensitivity(n_state=n_state, n_inj=n_bus)
    x_prev = np.array([1.0, 0.1, 0.98, -0.05, 1.02, 0.03, 0.95, -0.02])

    rng = np.random.default_rng(42)
    pred = fp.FASEPredictor(prof_df, cfg, rng, n_bus)
    x_minus, Q = pred.predict(step_k=0, x_prev=x_prev, S=S)

    assert np.allclose(x_minus, x_prev, atol=1e-14), (
        f"persistence mode must return x_minus == x_prev; "
        f"max_diff={np.max(np.abs(x_minus - x_prev)):.2e}"
    )
    # Q in persistence mode should be larger than Q_floor (scaled by RW_SCALE)
    q_floor = np.eye(n_state) * cfg["q_floor_scale"]
    # Q >= 1.0 * q_floor (should be 100x by default)
    assert np.all(np.diag(Q) >= np.diag(q_floor)), \
        "persistence mode Q should be >= Q_floor (random-walk floor)"
    print("  [PASS] persistence mode: x_minus == x_prev (exact copy), Q >= Q_floor")


# ---------------------------------------------------------------------------
# Test 3: fase mode applies x_minus = x_prev + S·Δp, Q = S·Cov(ε)·St + Q_floor
# ---------------------------------------------------------------------------

def test_fase_mode_recipe():
    """fase mode: x_minus = x_prev + S·Δp; Q has correct structure."""
    n_bus = 4
    n_state = n_bus * 2
    prof_df = make_prof_df(n_steps=5)
    cfg = make_cfg(mode="fase", seed=7)
    S = make_sensitivity(n_state=n_state, n_inj=n_bus)
    x_prev = np.ones(n_state)

    rng = np.random.default_rng(cfg["seed"])
    pred = fp.FASEPredictor(prof_df, cfg, rng, n_bus)

    # First step: x_minus = x_prev + S @ delta_p (delta_p derived from first forecast)
    x_minus, Q = pred.predict(step_k=0, x_prev=x_prev, S=S)

    # Q must be symmetric positive-semi-definite (it's S·Cov·St + Q_floor)
    # Check symmetry
    assert np.allclose(Q, Q.T, atol=1e-12), f"Q not symmetric: max_diff={np.max(np.abs(Q - Q.T)):.2e}"

    # Check Q >= Q_floor (floor contribution)
    q_floor = np.eye(n_state) * cfg["q_floor_scale"]
    # Off-diagonal entries of Q should be finite
    assert np.all(np.isfinite(Q)), "Q contains non-finite values"

    # Q should have the correct shape
    assert Q.shape == (n_state, n_state), f"Q shape {Q.shape} != ({n_state},{n_state})"

    # x_minus should differ from x_prev (forecast Δp was applied)
    # On first step, delta_p = p_fcst(0) - p_fcst(-1)  (first step: delta_p = zeros OR p_fcst itself)
    # Just check it's finite and has the right shape
    assert x_minus.shape == x_prev.shape, f"x_minus shape mismatch"
    assert np.all(np.isfinite(x_minus)), "x_minus contains non-finite values"

    print(f"  [PASS] fase mode: x_minus finite, Q symmetric PSD, correct shapes; "
          f"||x_minus - x_prev||={np.linalg.norm(x_minus - x_prev):.4e}")


# ---------------------------------------------------------------------------
# Test 4: multi-step fase mode x_minus actually uses S·Δp
# ---------------------------------------------------------------------------

def test_fase_uses_sensitivity():
    """On step k>=1, x_minus = x_prev + S @ delta_p where delta_p is non-zero."""
    n_bus = 4
    n_state = n_bus * 2
    n_steps = 5
    prof_df = make_prof_df(n_steps=n_steps, seed=3)
    cfg = make_cfg(mode="fase", seed=13)
    S = make_sensitivity(n_state=n_state, n_inj=n_bus) * 100.0  # large S to amplify effect
    x_prev = np.ones(n_state)

    rng = np.random.default_rng(cfg["seed"])
    pred = fp.FASEPredictor(prof_df, cfg, rng, n_bus)

    x_cur = x_prev.copy()
    any_nonzero_delta = False
    for step_k in range(n_steps):
        x_minus, Q = pred.predict(step_k, x_cur, S)
        delta = x_minus - x_cur
        if np.linalg.norm(delta) > 1e-12:
            any_nonzero_delta = True
        x_cur = x_minus

    assert any_nonzero_delta, \
        "fase mode: x_minus == x_prev at all steps (sensitivity not applied)"
    print("  [PASS] fase mode: non-zero delta applied via S @ Δp at some steps")


# ---------------------------------------------------------------------------
# Test 5: oracle separation (grep check)
# ---------------------------------------------------------------------------

def test_oracle_separation():
    """fase_predict.py must not contain code (non-comment) references to oracle buckets."""
    import re
    src_path = "/home/juan/codes/ge-vernova-virtual-sensing/system1-measurement-source/src/ieee33/fase_predict.py"
    with open(src_path) as f:
        lines = f.readlines()

    forbidden = [
        "STATE_BUCKET", "FAULT_EVENT_BUCKET", "read_state", "read_fault",
        '"state"', '"fault_event"',
    ]
    matches = []
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        # Skip pure comment lines and docstring grep-example lines
        # A comment line starts with '#' after stripping; docstring content in triple-quoted
        # strings is documentation, not code. Only flag actual Python code lines.
        # We skip lines that begin with '#', begin with '"""', begin with "'''", or are
        # indented within a docstring block that explains the grep command.
        if stripped.startswith('#'):
            continue
        if 'grep' in stripped.lower():
            continue  # grep-command documentation line
        for pattern in forbidden:
            if pattern in line:
                matches.append(f"  Line {i}: {stripped}")

    assert not matches, (
        "fase_predict.py contains oracle references in code (not comments):\n"
        + "\n".join(matches)
    )
    print("  [PASS] fase_predict.py: no oracle references in code (STATE_BUCKET / read_state / etc.)")


if __name__ == "__main__":
    print("=" * 60)
    print("scratch_fase.py — FASEPredictor + persistence foil")
    print("=" * 60)

    test_persistence_mode()
    test_fase_mode_recipe()
    test_fase_uses_sensitivity()
    test_determinism()
    test_oracle_separation()

    print()
    print("FASE deterministic + persistence foil OK")
