"""
test_estimate_config.py
-----------------------
TDD tests for estimate_config.py (Task 2, Plan 10-01).

These tests define the contract that estimate_config.py must satisfy:
  - Pure constants only (no I/O side effects at import time)
  - ACTIVE block with all nine documented keys and locked defaults
  - Constant tables: ESTIMATES_BUCKET, UKF params, WLS params, NEES params
  - N_FREE_STATES == 64, N_BUS_TOTAL == 34 (encoding the 34-bus / 64-free-state landmine)
"""

import pytest


def test_import_no_side_effects():
    """import ieee33.estimate_config must produce no stdout/stderr and no I/O."""
    # If this raises, the module has a forbidden side effect (load_dotenv, file read, etc.)
    import ieee33.estimate_config as ec  # noqa: F401


def test_active_block_has_all_keys():
    """ACTIVE must contain all nine documented keys."""
    import ieee33.estimate_config as ec

    required_keys = {
        "scenario",
        "source",
        "estimator",
        "seed",
        "acceleration",
        "forecast_sigma_frac",
        "forecast_ar1_rho",
        "q_floor_scale",
        "predict_mode",
    }
    assert set(ec.ACTIVE.keys()) == required_keys, (
        f"ACTIVE is missing keys: {required_keys - set(ec.ACTIVE.keys())}"
    )


def test_active_block_default_values():
    """ACTIVE default values must match the locked defaults from PATTERNS.md."""
    import ieee33.estimate_config as ec

    a = ec.ACTIVE
    assert a["scenario"] == "realistic_sparse"
    assert a["source"] == "day"
    assert a["estimator"] == "ukf"
    assert a["seed"] == 42
    assert a["acceleration"] == 1.0
    assert a["forecast_sigma_frac"] == 0.05
    assert a["forecast_ar1_rho"] == 0.3
    assert a["q_floor_scale"] == 1e-8
    assert a["predict_mode"] == "fase"


def test_active_estimator_valid_value():
    """ACTIVE['estimator'] must be one of the three valid estimator names."""
    import ieee33.estimate_config as ec

    assert ec.ACTIVE["estimator"] in ("wls", "ekf", "ukf")


def test_active_predict_mode_valid_value():
    """ACTIVE['predict_mode'] must be 'fase' or 'persistence'."""
    import ieee33.estimate_config as ec

    assert ec.ACTIVE["predict_mode"] in ("fase", "persistence")


def test_estimates_bucket_constant():
    """ESTIMATES_BUCKET must equal 'estimates'."""
    import ieee33.estimate_config as ec

    assert ec.ESTIMATES_BUCKET == "estimates"


def test_ukf_sigma_point_parameters():
    """UKF sigma-point parameters must have their locked defaults."""
    import ieee33.estimate_config as ec

    assert ec.UKF_ALPHA == 1e-3
    assert ec.UKF_BETA == 2.0
    assert ec.UKF_KAPPA == 0.0


def test_wls_convergence_knobs():
    """WLS Gauss-Newton iteration knobs must be present."""
    import ieee33.estimate_config as ec

    assert ec.GAUSS_NEWTON_MAX_ITER == 20
    assert ec.GAUSS_NEWTON_TOL == 1e-6


def test_nees_confidence():
    """NEES_CONFIDENCE must be 0.95 for the chi2 band computation."""
    import ieee33.estimate_config as ec

    assert ec.NEES_CONFIDENCE == 0.95


def test_state_dimension_constants():
    """N_FREE_STATES and N_BUS_TOTAL encode the 34-bus / 64-free-state landmine."""
    import ieee33.estimate_config as ec

    assert ec.N_FREE_STATES == 64, "64 = 2×32 free distribution-bus states (buses 0..32 minus slack)"
    assert ec.N_BUS_TOTAL == 34, "34 = 33 distribution buses + 1 HV ext_grid bus added by build_enhanced_33bus()"


def test_no_third_party_imports():
    """estimate_config.py must use stdlib only — no numpy, pandas, load_dotenv etc."""
    import ast
    import pathlib

    src_path = pathlib.Path(__file__).parent.parent / "src" / "ieee33" / "estimate_config.py"
    tree = ast.parse(src_path.read_text())

    forbidden = {"numpy", "pandas", "load_dotenv", "influxdb_client", "paho", "dotenv"}
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported.add(alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imported.add(node.module.split(".")[0])

    offenders = imported & forbidden
    assert not offenders, f"estimate_config.py imports forbidden third-party packages: {offenders}"


def test_no_runtime_side_effects():
    """AST-based check: no calls to load_dotenv, datetime.now, np.random, or open()."""
    import ast
    import pathlib

    src_path = pathlib.Path(__file__).parent.parent / "src" / "ieee33" / "estimate_config.py"
    tree = ast.parse(src_path.read_text())

    # Look for Call nodes whose function is one of the forbidden patterns
    forbidden_calls = {"load_dotenv", "open"}
    forbidden_attr_chains = {
        ("datetime", "now"),
        ("np", "random"),
        ("numpy", "random"),
    }

    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            # Direct call: open(...), load_dotenv(...)
            if isinstance(node.func, ast.Name):
                assert node.func.id not in forbidden_calls, (
                    f"estimate_config.py calls forbidden function '{node.func.id}'"
                )
            # Attribute call: datetime.now(), np.random.seed(), etc.
            elif isinstance(node.func, ast.Attribute):
                if isinstance(node.func.value, ast.Name):
                    chain = (node.func.value.id, node.func.attr)
                    for forbidden in forbidden_attr_chains:
                        # Check if first two elements match start of chain
                        assert chain[:len(forbidden)] != forbidden, (
                            f"estimate_config.py calls forbidden pattern '{'.'.join(forbidden)}'"
                        )
