"""
test_noise_models_cadence.py
----------------------------
TDD tests for Plan 04 Task 1: three noise models + multirate cadence gate in measure.py.

Tests verify:
- InstrumentState class + ar1_term method + _instrument_bias function present
- apply_noise dispatches to gaussian / gaussian_outliers / instrument
- gaussian model: output near true value with correct std
- gaussian_outliers: base gaussian + gross errors on ~3% of draws
- instrument: quantized output lands on LSB grid; bias + AR(1) correlation
- multirate cadence gate: step_idx % CADENCE[experiment][cls] == 0 gate
- RNG draw order determinism (same seed = same output)
- assumed_sigma is independent of noise model (never fed to noise gen)

Run: cd system1-measurement-source && uv run python -m pytest tests/test_noise_models_cadence.py -v
"""

import inspect
import math

import numpy as np
import pytest


# ---------------------------------------------------------------------------
# Existence / structure tests (RED: will fail before Task 1 implementation)
# ---------------------------------------------------------------------------

def test_instrument_state_class_exists():
    """InstrumentState class must be defined in measure.py."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    assert "class InstrumentState" in src, "InstrumentState class missing from measure.py"


def test_apply_noise_function_exists():
    """apply_noise function must be defined in measure.py."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    assert "def apply_noise" in src, "apply_noise function missing from measure.py"


def test_instrument_bias_function_exists():
    """_instrument_bias function must be defined in measure.py."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    assert "def _instrument_bias" in src, "_instrument_bias function missing from measure.py"


def test_noise_model_dispatch_references():
    """apply_noise must reference OUTLIER_FRACTION, OUTLIER_SPIKE_MULT, and AR1/rho."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    assert "OUTLIER_FRACTION" in src, "OUTLIER_FRACTION reference missing (D-12)"
    assert "OUTLIER_SPIKE_MULT" in src, "OUTLIER_SPIKE_MULT reference missing (D-12)"
    assert "INSTRUMENT_AR1_RHO" in src or "ar1_term" in src, (
        "AR(1) implementation missing (D-13): expected INSTRUMENT_AR1_RHO or ar1_term"
    )
    assert "QUANT_LSB" in src, "QUANT_LSB reference missing (D-13 quantization)"


def test_cadence_gate_reference():
    """Multirate cadence gate must reference CADENCE in measure.py."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    assert "CADENCE" in src, "CADENCE table reference missing (D-14)"
    # The gate should be a modulo check (step_idx % ... != 0 or == 0)
    assert "% " in src or "%" in src, "No modulo operator found (cadence gate pattern)"


# ---------------------------------------------------------------------------
# InstrumentState behaviour tests
# ---------------------------------------------------------------------------

def test_instrument_state_ar1_convergence():
    """ar1_term must return AR(1) correlated noise with mean ~0 and ρ≈0.7 over many draws."""
    from ieee33.measure import InstrumentState
    rng = np.random.default_rng(42)
    ist = InstrumentState(0.7)
    sigma = 0.1
    n = 2000
    values = [ist.ar1_term("test_sensor", sigma, rng) for _ in range(n)]
    # Mean should be near zero (AR(1) with zero-mean white noise)
    assert abs(np.mean(values)) < 0.05 * sigma * 10, (
        f"AR(1) mean {np.mean(values):.6f} unexpectedly far from 0"
    )
    # Autocorrelation at lag-1 should be close to rho=0.7
    arr = np.array(values)
    ac = np.corrcoef(arr[:-1], arr[1:])[0, 1]
    assert 0.55 < ac < 0.85, (
        f"AR(1) lag-1 autocorrelation {ac:.3f} not near ρ=0.7"
    )


def test_instrument_bias_deterministic():
    """_instrument_bias must return identical float for same (sensor_key, seed)."""
    from ieee33.measure import _instrument_bias
    b1 = _instrument_bias("scada_0_vm_pu", 42)
    b2 = _instrument_bias("scada_0_vm_pu", 42)
    assert b1 == b2, "_instrument_bias is not deterministic for same inputs"


def test_instrument_bias_sensor_specific():
    """_instrument_bias must return different values for different sensor keys."""
    from ieee33.measure import _instrument_bias
    b1 = _instrument_bias("scada_0_vm_pu", 42)
    b2 = _instrument_bias("pmu_4_vm_pu", 42)
    assert b1 != b2, "_instrument_bias returns same value for different sensors"


# ---------------------------------------------------------------------------
# apply_noise dispatch tests
# ---------------------------------------------------------------------------

def test_apply_noise_gaussian_near_true():
    """gaussian model: result should be within 5σ of true value."""
    from ieee33.measure import InstrumentState, apply_noise
    rng = np.random.default_rng(1)
    ist = InstrumentState(0.7)
    true_val = 1.0
    true_sigma = 0.005
    v = apply_noise("gaussian", "scada", 0, "vm_pu", true_val, true_sigma, rng, ist, 42)
    assert abs(v - true_val) < 5 * true_sigma, (
        f"gaussian: |{v:.6f} - {true_val}| = {abs(v-true_val):.6f} > 5σ={5*true_sigma}"
    )


def test_apply_noise_gaussian_outliers_base_usually_near_true():
    """gaussian_outliers: most draws should be near true value (outlier rate ≈ 3%)."""
    from ieee33.measure import InstrumentState, apply_noise
    rng = np.random.default_rng(99)
    ist = InstrumentState(0.7)
    true_val = 1.0
    true_sigma = 0.005
    n = 1000
    values = [
        apply_noise("gaussian_outliers", "scada", 0, "vm_pu", true_val, true_sigma, rng, ist, 42)
        for _ in range(n)
    ]
    # Count gross errors (|v - true| > 5σ)
    n_outliers = sum(1 for v in values if abs(v - true_val) > 5 * true_sigma)
    outlier_rate = n_outliers / n
    # Should be around 3% (D-12: f=0.03), allow 0.5%–8% range for n=1000
    assert 0.005 <= outlier_rate <= 0.08, (
        f"gaussian_outliers outlier rate {outlier_rate:.3f} not near 3% (D-12 f=0.03)"
    )


def test_apply_noise_outliers_spike_magnitude():
    """gaussian_outliers gross errors must have magnitude ~15σ (D-12)."""
    from ieee33.measure import InstrumentState, apply_noise
    rng = np.random.default_rng(7)
    ist = InstrumentState(0.7)
    true_val = 1.0
    true_sigma = 0.1   # larger sigma so spike is more visible
    n = 5000
    values = [
        apply_noise("gaussian_outliers", "scada", 0, "vm_pu", true_val, true_sigma, rng, ist, 42)
        for _ in range(n)
    ]
    gross_errors = [abs(v - true_val) for v in values if abs(v - true_val) > 5 * true_sigma]
    assert len(gross_errors) > 0, "No gross errors found in 5000 draws (expected ~3%)"
    # Gross error magnitude should be near 15σ
    avg_spike = np.mean(gross_errors)
    assert 10 * true_sigma < avg_spike < 20 * true_sigma, (
        f"Avg spike magnitude {avg_spike:.3f} not near 15σ={15*true_sigma} (D-12)"
    )


def test_apply_noise_instrument_quantized():
    """instrument model: output must land exactly on LSB grid."""
    from ieee33 import measure_config as mc
    from ieee33.measure import InstrumentState, apply_noise
    rng = np.random.default_rng(1)
    ist = InstrumentState(0.7)
    true_val = 1.0
    true_sigma = mc.CLASS_SIGMA["scada"]["vm_pu"] * abs(true_val)
    lsb = mc.QUANT_LSB["scada"]["vm_pu"]
    q = apply_noise("instrument", "scada", 0, "vm_pu", true_val, true_sigma, rng, ist, 42)
    # Check: q is an integer multiple of lsb (within floating-point tolerance)
    remainder = abs(round(q / lsb) * lsb - q)
    assert remainder < 1e-9, (
        f"instrument output {q:.8f} not on LSB grid (lsb={lsb}, remainder={remainder:.2e})"
    )


def test_apply_noise_instrument_multiple_sensors_quantized():
    """instrument model: multiple sensors all land on their respective LSB grids."""
    from ieee33 import measure_config as mc
    from ieee33.measure import InstrumentState, apply_noise

    test_cases = [
        ("scada", 0, "vm_pu", 1.0),
        ("scada", 0, "p_inj_mw", 2.5),
        ("pmu", 4, "vm_pu", 0.98),
        ("ami", 3, "p_inj_mw", 1.2),
    ]
    rng = np.random.default_rng(123)
    ist = InstrumentState(0.7)

    for cls, bus, qty, tv in test_cases:
        true_sigma = mc.CLASS_SIGMA[cls][qty] * abs(tv) if qty != "va_degree" else mc.CLASS_SIGMA[cls][qty]
        lsb = mc.QUANT_LSB[cls][qty]
        q = apply_noise("instrument", cls, bus, qty, tv, true_sigma, rng, ist, 42)
        remainder = abs(round(q / lsb) * lsb - q)
        assert remainder < 1e-9, (
            f"instrument {cls}/{qty}: output {q:.8f} not on LSB grid (lsb={lsb})"
        )


def test_apply_noise_assumed_sigma_independent():
    """assumed_sigma is computed by caller (true_sigma * scale), never by apply_noise itself."""
    # apply_noise only receives true_sigma and uses it for generation
    # This test verifies apply_noise signature does NOT accept assumed_sigma
    from ieee33.measure import apply_noise
    sig = inspect.signature(apply_noise)
    param_names = list(sig.parameters.keys())
    assert "assumed_sigma" not in param_names, (
        "apply_noise must NOT receive assumed_sigma — it only generates with true_sigma (SPEC R9)"
    )


# ---------------------------------------------------------------------------
# Determinism tests
# ---------------------------------------------------------------------------

def test_apply_noise_deterministic_same_seed():
    """Two runs with same seed must return byte-identical values."""
    from ieee33.measure import InstrumentState, apply_noise

    def run_sequence(seed):
        rng = np.random.default_rng(seed)
        ist = InstrumentState(0.7)
        results = []
        for model in ("gaussian", "gaussian_outliers", "instrument"):
            v = apply_noise(model, "scada", 0, "vm_pu", 1.0, 0.005, rng, ist, seed)
            results.append(v)
        return results

    r1 = run_sequence(42)
    r2 = run_sequence(42)
    assert r1 == r2, f"Runs with same seed produce different values: {r1} vs {r2}"


def test_apply_noise_different_seeds_differ():
    """Different seeds must produce different noise values."""
    from ieee33.measure import InstrumentState, apply_noise
    rng1 = np.random.default_rng(42)
    rng2 = np.random.default_rng(99)
    ist1 = InstrumentState(0.7)
    ist2 = InstrumentState(0.7)
    v1 = apply_noise("gaussian", "scada", 0, "vm_pu", 1.0, 0.005, rng1, ist1, 42)
    v2 = apply_noise("gaussian", "scada", 0, "vm_pu", 1.0, 0.005, rng2, ist2, 99)
    assert v1 != v2, "Different seeds returned same value (extremely unlikely)"


# ---------------------------------------------------------------------------
# Cadence gate tests
# ---------------------------------------------------------------------------

def test_cadence_table_structure():
    """CADENCE must have 'day' and 'fault' keys with correct per-class entries."""
    from ieee33 import measure_config as mc
    assert "day" in mc.CADENCE, "CADENCE missing 'day' key"
    assert "fault" in mc.CADENCE, "CADENCE missing 'fault' key"
    # D-14: AMI cadence = 4 for day, 10 for fault
    assert mc.CADENCE["day"]["ami"] == 4, f"D-14: day AMI cadence should be 4, got {mc.CADENCE['day']['ami']}"
    assert mc.CADENCE["fault"]["ami"] == 10, f"D-14: fault AMI cadence should be 10, got {mc.CADENCE['fault']['ami']}"
    assert mc.CADENCE["fault"]["scada"] == 2, f"D-14: fault SCADA cadence should be 2, got {mc.CADENCE['fault']['scada']}"


def test_cadence_gate_pattern_in_source():
    """Cadence gate must implement step_idx % CADENCE[experiment][cls] != 0 pattern."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    # Must have: step_idx % ... CADENCE ... != 0 (or == 0 with continue)
    # Accept any % pattern referencing CADENCE
    has_cadence_gate = (
        ("CADENCE[" in src and "%" in src) or
        ("cadence" in src.lower() and "%" in src)
    )
    assert has_cadence_gate, (
        "No cadence gate pattern found: expected 'step_idx % CADENCE[experiment][cls]' "
        "or equivalent in measure.py"
    )


def test_multirate_async_stub_removed():
    """The Plan 03 placeholder 'pass  # TODO(Plan 04): cadence gate' must be replaced."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    assert "TODO(Plan 04): cadence gate" not in src, (
        "Plan 03 cadence-gate TODO placeholder still present — Plan 04 must replace it"
    )
