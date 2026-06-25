"""
test_measure_determinism.py
---------------------------
Plan 05 / Phase 9 acceptance-gate tests for the measurement-layer runner.

Tests cover:
  Static (always runnable, no InfluxDB required):
    - test_no_unseeded_randomness: greps measure.py for forbidden RNG tokens
    - test_no_true_value_field: greps measure.py + influx.py for oracle-separation violation
    - test_meas_schema_vocab: asserts locked D-04/D-05/D-11 values in measure_config

  Integration (skipped if InfluxDB unreachable — Docker-guarded):
    - test_determinism: two same-config runs produce byte-identical meas values (R10)
    - test_multirate_cadence: AMI == 24 timestamps in multirate_async / 96 in snapshot (D-14)
    - test_dead_bus_gate: zero meas points for bus 17 in faulted_isolated phase (D-03)

Run (all tests including integration, requires Docker stack + pre-populated buckets):
    cd system1-measurement-source && uv run python -m pytest tests/test_measure_determinism.py -v

Run (static tests only, no Docker needed):
    cd system1-measurement-source && uv run python -m pytest tests/test_measure_determinism.py \\
        -k "not determinism and not cadence and not dead_bus" -v
"""

import inspect
import os
import pathlib
import pytest


# ---------------------------------------------------------------------------
# InfluxDB reachability helper (Docker-guard for integration tests)
# ---------------------------------------------------------------------------

def _influx_available() -> bool:
    """Return True if the local Docker InfluxDB stack is reachable.

    Tries to import and instantiate the client from influx.get_client(),
    then pings the /ping endpoint.  Returns False on any error — this lets
    all integration tests skip cleanly in CI without Docker.
    """
    try:
        from ieee33 import influx
        client = influx.get_client()
        health = client.ping()
        client.close()
        return bool(health)
    except Exception:
        return False


_INFLUX_SKIP = pytest.mark.skipif(
    not _influx_available(),
    reason="InfluxDB not reachable — Docker stack not running. "
           "Run 'docker compose up -d && uv run sim && uv run fault-sim' first.",
)


# ---------------------------------------------------------------------------
# Helper: path to src/ files
# ---------------------------------------------------------------------------

def _src_text(filename: str) -> str:
    """Read and return the source text of a file in src/ieee33/."""
    repo_root = pathlib.Path(__file__).parent.parent
    fpath = repo_root / "src" / "ieee33" / filename
    return fpath.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Static test 1: no unseeded randomness in measure.py (D-10 / AC-10)
# ---------------------------------------------------------------------------

def test_no_unseeded_randomness():
    """measure.py must use ONLY np.random.default_rng — no legacy RNG APIs.

    Forbidden tokens (each indicates a non-deterministic or unseeded call):
      - datetime.now     (wallclock; breaks reproducibility)
      - time.time        (wallclock)
      - random.random    (stdlib random, not seeded per-run)
      - np.random.seed   (legacy global-state seed API)
      - np.random.rand   (legacy draw on global state)
      - np.random.randn  (legacy draw on global state)

    Required token:
      - default_rng      (new NumPy Generator API: stream-reproducible, seed-per-run)
    """
    src = _src_text("measure.py")

    forbidden = [
        "datetime.now",
        "time.time",
        "random.random(",
        "np.random.seed",
        "np.random.rand(",
        "np.random.randn(",
    ]
    for token in forbidden:
        assert token not in src, (
            f"Forbidden token '{token}' found in measure.py — "
            "violates determinism contract (D-10 / SPEC R10)"
        )

    assert "default_rng" in src, (
        "measure.py must use np.random.default_rng(seed) for deterministic noise — "
        "not found in source (D-10 / SPEC R10)"
    )


# ---------------------------------------------------------------------------
# Static test 2: no true_value field anywhere (SPEC R9 / D-06 oracle separation)
# ---------------------------------------------------------------------------

def test_no_true_value_field():
    """Neither measure.py nor influx.py must reference .field(\"true_value\").

    The true (ground-truth) value must stay in the state/fault_event buckets.
    The measurements bucket must NEVER receive a true_value field (SPEC R9 / D-06):
    System 2 must not be able to peek at truth, and the scoring oracle (System 3)
    must compare estimate vs truth independently.
    """
    measure_src = _src_text("measure.py")
    influx_src  = _src_text("influx.py")

    # The contract is that NO code writes .field("true_value", ...) or
    # .field('true_value', ...) to any InfluxDB point in the measurement path.
    forbidden_pattern = '.field("true_value"'
    forbidden_pattern2 = ".field('true_value'"

    assert forbidden_pattern  not in measure_src, (
        f"Oracle violation: '{forbidden_pattern}' found in measure.py (SPEC R9 / D-06)"
    )
    assert forbidden_pattern2 not in measure_src, (
        f"Oracle violation: '{forbidden_pattern2}' found in measure.py (SPEC R9 / D-06)"
    )
    assert forbidden_pattern  not in influx_src, (
        f"Oracle violation: '{forbidden_pattern}' found in influx.py (SPEC R9 / D-06)"
    )
    assert forbidden_pattern2 not in influx_src, (
        f"Oracle violation: '{forbidden_pattern2}' found in influx.py (SPEC R9 / D-06)"
    )


# ---------------------------------------------------------------------------
# Static test 3: measure_config locked schema vocabulary (D-04/D-05/D-11)
# ---------------------------------------------------------------------------

def test_meas_schema_vocab():
    """measure_config must contain the locked D-04/D-05/D-11 constant values.

    Asserts the following locked decisions are present in the config:
      - CLASS_SIGMA: pseudo σ == 0.30 (D-11 large sigma for load-forecast pseudo)
      - CLASS_SIGMA: pmu va_degree σ == 0.0003 (D-11 GPS-disciplined absolute radians)
      - CADENCE: day AMI == 4 (D-14: hourly AMI during 15-min day steps)
      - CADENCE: fault AMI == 10 (D-14: AMI blind during 30-s window)
      - CADENCE: fault SCADA == 2 (D-14: 6-s SCADA scan rate)
      - SCENARIOS: realistic_sparse pmu buses == {17, 24, 30} (D-04)
      - SCENARIOS: well_observed zero_inj buses == [2, 19] (D-05)
      - MEAS_CLASSES and MEAS_QUANTITIES: correct vocabulary (D-06)
    """
    from ieee33 import measure_config as mc

    # D-11: pseudo sigma (large, 30% — last-resort load forecast)
    assert mc.CLASS_SIGMA["pseudo"]["p_inj_mw"] == pytest.approx(0.30), (
        f"D-11: pseudo p_inj_mw sigma should be 0.30, got {mc.CLASS_SIGMA['pseudo']['p_inj_mw']}"
    )
    assert mc.CLASS_SIGMA["pseudo"]["q_inj_mvar"] == pytest.approx(0.30), (
        f"D-11: pseudo q_inj_mvar sigma should be 0.30, got {mc.CLASS_SIGMA['pseudo']['q_inj_mvar']}"
    )

    # D-11: pmu angle sigma (absolute radians, GPS-disciplined)
    assert mc.CLASS_SIGMA["pmu"]["va_degree"] == pytest.approx(0.0003), (
        f"D-11: pmu va_degree sigma should be 0.0003, got {mc.CLASS_SIGMA['pmu']['va_degree']}"
    )

    # D-14: cadence table — day AMI
    assert mc.CADENCE["day"]["ami"] == 4, (
        f"D-14: day AMI cadence should be 4 (hourly), got {mc.CADENCE['day']['ami']}"
    )
    # D-14: cadence table — fault AMI (essentially blind during 2-min event)
    assert mc.CADENCE["fault"]["ami"] == 10, (
        f"D-14: fault AMI cadence should be 10, got {mc.CADENCE['fault']['ami']}"
    )
    # D-14: cadence table — fault SCADA (6-s scan rate)
    assert mc.CADENCE["fault"]["scada"] == 2, (
        f"D-14: fault SCADA cadence should be 2 (6-s scan rate), got {mc.CADENCE['fault']['scada']}"
    )

    # D-04: realistic_sparse PMU buses {17, 24, 30}
    assert set(mc.SCENARIOS["realistic_sparse"]["pmu"]) == {17, 24, 30}, (
        f"D-04: realistic_sparse pmu buses should be {{17, 24, 30}}, "
        f"got {mc.SCENARIOS['realistic_sparse']['pmu']}"
    )

    # D-05: well_observed zero_inj buses [2, 19]
    assert set(mc.SCENARIOS["well_observed"]["zero_inj"]) == {2, 19}, (
        f"D-05: well_observed zero_inj buses should be {{2, 19}}, "
        f"got {mc.SCENARIOS['well_observed']['zero_inj']}"
    )

    # D-06: MEAS_CLASSES vocabulary
    expected_classes = {"scada", "pmu", "ami", "der", "pseudo", "zero_inj"}
    assert set(mc.MEAS_CLASSES) == expected_classes, (
        f"D-06: MEAS_CLASSES {set(mc.MEAS_CLASSES)} != expected {expected_classes}"
    )

    # D-06: MEAS_QUANTITIES vocabulary
    expected_quantities = {"vm_pu", "va_degree", "p_inj_mw", "q_inj_mvar", "p_mw", "q_mvar"}
    assert set(mc.MEAS_QUANTITIES) == expected_quantities, (
        f"D-06: MEAS_QUANTITIES {set(mc.MEAS_QUANTITIES)} != expected {expected_quantities}"
    )

    # D-08: ACTIVE block must have the five required keys
    required_active_keys = {"scenario", "source", "sampling", "noise", "seed"}
    assert required_active_keys.issubset(mc.ACTIVE.keys()), (
        f"D-09: ACTIVE block missing keys: {required_active_keys - set(mc.ACTIVE.keys())}"
    )


# ---------------------------------------------------------------------------
# Integration test 1: byte-identical determinism (R10 / D-10)
# ---------------------------------------------------------------------------

@_INFLUX_SKIP
def test_determinism():
    """Two same-config runs must produce byte-identical meas values in InfluxDB.

    Protocol:
      1. Run measure.main() with a fixed cfg (scenario=realistic_sparse, source=day,
         sampling=snapshot, noise=gaussian, seed=42).
      2. Query all (timestamp, location, quantity, value) tuples from the meas measurement.
      3. Re-run measure.main() with the SAME cfg.
      4. Query again — assert the sorted tuples are identical.

    This proves: seeded RNG + deterministic iteration order + overwrite-in-place keying
    produces byte-identical output on every run (SPEC R10 / D-10).
    """
    from ieee33 import influx, measure_config as mc
    from ieee33.measure import main as measure_main
    import sys

    cfg_overrides = [
        "--scenario", "realistic_sparse",
        "--source",   "day",
        "--sampling", "snapshot",
        "--noise",    "gaussian",
        "--seed",     "42",
    ]

    def run_and_query():
        """Invoke measure.main() and return sorted meas tuples from InfluxDB."""
        # Temporarily override sys.argv so _parse_args() picks up our cfg
        orig_argv = sys.argv[:]
        sys.argv = ["measure"] + cfg_overrides
        try:
            measure_main()
        finally:
            sys.argv = orig_argv

        # Query all meas points for this scenario/experiment/day
        client = influx.get_client()
        flux = (
            'from(bucket: "measurements")\n'
            '  |> range(start: 2017-06-07T00:00:00Z, stop: 2017-06-07T23:59:59Z)\n'
            '  |> filter(fn: (r) => r._measurement == "meas")\n'
            '  |> filter(fn: (r) => r._field == "value")\n'
            '  |> filter(fn: (r) => r.scenario == "realistic_sparse")\n'
            '  |> filter(fn: (r) => r.experiment == "day")\n'
            '  |> sort(columns: ["_time", "location", "quantity"])'
        )
        df = client.query_api().query_data_frame(flux)
        client.close()
        if df is None or (hasattr(df, "__len__") and len(df) == 0):
            return []
        # Build sorted tuples: (time_str, location, quantity, value)
        rows = []
        for _, row in df.iterrows():
            rows.append((
                str(row["_time"]),
                str(row.get("location", "")),
                str(row.get("quantity", "")),
                float(row["_value"]),
            ))
        return sorted(rows)

    tuples_run1 = run_and_query()
    assert len(tuples_run1) > 0, (
        "Run 1 returned 0 meas points — ensure 'uv run sim' has populated the state bucket"
    )

    tuples_run2 = run_and_query()
    assert len(tuples_run2) > 0, "Run 2 returned 0 meas points"

    assert tuples_run1 == tuples_run2, (
        f"Determinism FAILED: run 1 and run 2 differ. "
        f"First mismatch: {next((a,b) for a,b in zip(tuples_run1,tuples_run2) if a!=b)}"
    )


# ---------------------------------------------------------------------------
# Integration test 2: multirate cadence counts (D-14)
# ---------------------------------------------------------------------------

@_INFLUX_SKIP
def test_multirate_cadence():
    """Multirate AMI appears at 24 timestamps (96/4) in multirate_async; 96 in snapshot.

    Protocol:
      1. Run measure.main() with sampling=multirate_async, source=day, scenario=realistic_sparse.
      2. Query distinct _time values for class=ami in measurements bucket.
         Expected: 24 (96 steps / cadence 4 = 1-hour AMI reads).
      3. Re-run with sampling=snapshot.
         Expected: 96 (all steps, snapshot mode).
      4. For μPMU in multirate_async: expected 96 (cadence=1, every step).
    """
    import sys
    from ieee33 import influx, measure_config as mc
    from ieee33.measure import main as measure_main

    def run_measure(sampling: str):
        orig_argv = sys.argv[:]
        sys.argv = [
            "measure",
            "--scenario", "realistic_sparse",
            "--source",   "day",
            "--sampling", sampling,
            "--noise",    "gaussian",
            "--seed",     "42",
        ]
        try:
            measure_main()
        finally:
            sys.argv = orig_argv

    def count_distinct_times(cls: str) -> int:
        """Count distinct _time values for the given class in the measurements bucket (day)."""
        client = influx.get_client()
        flux = (
            'from(bucket: "measurements")\n'
            '  |> range(start: 2017-06-07T00:00:00Z, stop: 2017-06-07T23:59:59Z)\n'
            '  |> filter(fn: (r) => r._measurement == "meas")\n'
            '  |> filter(fn: (r) => r._field == "value")\n'
            f'  |> filter(fn: (r) => r.class == "{cls}")\n'
            '  |> filter(fn: (r) => r.scenario == "realistic_sparse")\n'
            '  |> filter(fn: (r) => r.experiment == "day")\n'
            '  |> distinct(column: "_time")\n'
            '  |> count()'
        )
        df = client.query_api().query_data_frame(flux)
        client.close()
        if df is None or (hasattr(df, "__len__") and len(df) == 0):
            return 0
        return int(df.iloc[0]["_value"])

    # --- multirate_async: AMI every 4 steps → 24 distinct timestamps ---
    run_measure("multirate_async")
    ami_times_multi = count_distinct_times("ami")
    assert ami_times_multi == 24, (
        f"D-14 multirate_async: AMI should appear at 24 timestamps (96/4=24), "
        f"got {ami_times_multi}"
    )

    # --- multirate_async: μPMU every step → 96 distinct timestamps ---
    pmu_times_multi = count_distinct_times("pmu")
    assert pmu_times_multi == 96, (
        f"D-14 multirate_async: PMU should appear at 96 timestamps (cadence=1), "
        f"got {pmu_times_multi}"
    )

    # --- snapshot: AMI every step → 96 distinct timestamps ---
    run_measure("snapshot")
    ami_times_snap = count_distinct_times("ami")
    assert ami_times_snap == 96, (
        f"D-14 snapshot: AMI should appear at 96 timestamps, got {ami_times_snap}"
    )


# ---------------------------------------------------------------------------
# Integration test 3: dead-bus gate (D-03) — bus 17 dark during isolation
# ---------------------------------------------------------------------------

@_INFLUX_SKIP
def test_dead_bus_gate():
    """Zero meas points for bus 17 during faulted_isolated phase (D-03).

    Protocol:
      1. Run measure.main() with source=fault, scenario=realistic_sparse.
      2. Query meas points with location=="17" AND phase=="faulted_isolated".
      3. Assert count == 0.

    Physics: bus 17 is inside the dead zone (buses 8-17, energised=0) during
    faulted_isolated. The D-03 gate in the measurement layer must suppress ALL
    measurements (real + pseudo) for any bus with energised="0".
    μPMU and DER telemetry at bus 17 go dark — this is the deliberate observability
    stress test for System 2.
    """
    import sys
    from ieee33 import influx
    from ieee33.measure import main as measure_main

    # Run measure with fault source
    orig_argv = sys.argv[:]
    sys.argv = [
        "measure",
        "--scenario", "realistic_sparse",
        "--source",   "fault",
        "--sampling", "snapshot",
        "--noise",    "gaussian",
        "--seed",     "42",
    ]
    try:
        measure_main()
    finally:
        sys.argv = orig_argv

    # Query meas points for bus 17 during faulted_isolated
    client = influx.get_client()
    flux = (
        'from(bucket: "measurements")\n'
        '  |> range(start: 2017-06-07T17:59:00Z, stop: 2017-06-07T18:03:00Z)\n'
        '  |> filter(fn: (r) => r._measurement == "meas")\n'
        '  |> filter(fn: (r) => r._field == "value")\n'
        '  |> filter(fn: (r) => r.location == "17")\n'
        '  |> filter(fn: (r) => r.phase == "faulted_isolated")\n'
        '  |> count()'
    )
    df = client.query_api().query_data_frame(flux)
    client.close()

    count = 0
    if df is not None and hasattr(df, "__len__") and len(df) > 0:
        count = int(df.iloc[0]["_value"])

    assert count == 0, (
        f"D-03 gate FAILED: {count} meas point(s) found for bus 17 during faulted_isolated. "
        "The energised=0 gate must suppress ALL measurements for dead buses."
    )
