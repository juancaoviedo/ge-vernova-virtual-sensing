"""
test_event_repub_footprint.py
-----------------------------
TDD tests for Plan 04 Task 2: topology event re-publish + footprint report in measure.py.

Tests verify:
- build_event_point is called in measure.py (topology re-publish, D-07/D-01)
- 'steady_state' phase is referenced for day-source event (D-07)
- n_states = 2*(N_energised-1) formula is present (D-15)
- 'redundancy' and 'Footprint' strings present (footprint report, D-15)
- Per-class count accumulation and report printing (D-15 format)
- Soft invariant: wrong-direction redundancy surfaces in issues

Run: cd system1-measurement-source && uv run python -m pytest tests/test_event_repub_footprint.py -v
"""

import inspect
import re

import pytest


# ---------------------------------------------------------------------------
# Presence / structure tests (RED: will fail before Task 2 implementation)
# ---------------------------------------------------------------------------

def test_build_event_point_called_in_measure():
    """measure.py must call build_event_point (D-07 topology re-publish)."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    assert "build_event_point" in src, (
        "build_event_point not called in measure.py — D-07 re-publish missing"
    )


def test_steady_state_phase_for_day():
    """measure.py must reference 'steady_state' phase for day-source event points (D-07)."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    assert "steady_state" in src, (
        "'steady_state' phase reference missing from measure.py — D-07 day topology event"
    )


def test_n_states_formula_present():
    """n_states = 2*(N_energised-1) formula must appear in measure.py (D-15)."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    # Match: 2 * (something - 1) with flexible whitespace
    pattern = r"2\s*\*\s*\(\s*.+\s*-\s*1\s*\)"
    assert re.search(pattern, src), (
        "n_states = 2*(N_energised-1) formula not found in measure.py (D-15)"
    )


def test_redundancy_reference_in_measure():
    """measure.py must contain 'redundancy' (case-insensitive) for D-15 report."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    assert "redundancy" in src.lower(), (
        "'redundancy' reference missing from measure.py (D-15 footprint report)"
    )


def test_footprint_header_in_measure():
    """measure.py must print a 'Footprint' header (D-15 footprint report)."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    assert "Footprint" in src, (
        "'Footprint' print header missing from measure.py (D-15 report format)"
    )


def test_n_states_variable_present():
    """n_states variable must appear in measure.py (D-15)."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    assert "n_states" in src, (
        "'n_states' variable missing from measure.py (D-15)"
    )


def test_real_only_redundancy_variable():
    """real_only_redundancy (or equivalent) must appear in measure.py (D-15)."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    assert "real_only_redundancy" in src or "real_redundancy" in src, (
        "real_only_redundancy / real_redundancy missing from measure.py (D-15)"
    )


def test_with_pseudo_redundancy_variable():
    """with_pseudo_redundancy must appear in measure.py (D-15)."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    assert "with_pseudo_redundancy" in src or "pseudo_redundancy" in src, (
        "with_pseudo_redundancy variable missing from measure.py (D-15)"
    )


def test_per_class_count_accumulation():
    """class_counts dict must be used to accumulate and report per-class totals (D-15)."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    # class_counts should be tracked throughout and printed in the footprint report
    assert "class_counts" in src, (
        "'class_counts' accumulator missing from measure.py (D-15)"
    )


def test_n_real_n_pseudo_totals():
    """Total real and pseudo counts must appear as named variables (D-15)."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    # Accept total_real, n_real, or similar
    has_real = "total_real" in src or "n_real" in src
    has_pseudo = "total_pseudo" in src or "n_pseudo" in src
    assert has_real, "Total real measurement count missing from measure.py (D-15)"
    assert has_pseudo, "Total pseudo measurement count missing from measure.py (D-15)"


def test_soft_invariant_for_wrong_direction_redundancy():
    """Wrong-direction redundancy must surface in issues list (D-15 soft invariant)."""
    from ieee33 import measure as m
    src = inspect.getsource(m)
    # The soft invariant check should reference issues.append and a redundancy check
    has_issues_append = "issues.append" in src
    # Should mention 'well_observed' redundancy check or 'realistic_sparse'
    has_redundancy_check = (
        ("well_observed" in src and "real_only_redundancy" in src.replace("real_redundancy", "real_only_redundancy")) or
        ("realistic_sparse" in src and "redundancy" in src.lower())
    )
    assert has_issues_append, "issues.append call missing from measure.py"
    assert has_redundancy_check, (
        "Soft redundancy invariant check missing from measure.py (D-15): "
        "wrong-direction redundancy should append to issues"
    )


# ---------------------------------------------------------------------------
# build_event_point output contract tests
# ---------------------------------------------------------------------------

def test_build_event_point_day_fields():
    """build_event_point for day: faulted_line_id=-1, tie_closed=0, tie_id=-1."""
    from ieee33.influx import build_event_point
    from datetime import datetime, timezone
    ts = datetime(2017, 6, 7, 0, 0, 0, tzinfo=timezone.utc)

    pt = build_event_point(
        scenario="realistic_sparse",
        experiment="day",
        phase="steady_state",
        faulted_line_id=-1,
        tie_closed=0,
        tie_id=-1,
        n_dead_buses=0,
        dead_buses="",
        ts=ts,
    )
    # Verify tags and fields via Point internals
    from influxdb_client import Point
    line = pt.to_line_protocol()
    assert "steady_state" in line, f"phase=steady_state not in line: {line}"
    assert "faulted_line_id=-1i" in line, f"faulted_line_id=-1 not in line: {line}"
    assert "tie_closed=0i" in line, f"tie_closed=0 not in line: {line}"
    assert "tie_id=-1i" in line, f"tie_id=-1 not in line: {line}"
    assert "n_dead_buses=0i" in line, f"n_dead_buses=0 not in line: {line}"


def test_build_event_point_fault_fields():
    """build_event_point for fault: fields match the fault scenario values."""
    from ieee33.influx import build_event_point
    from ieee33 import config
    from datetime import datetime, timezone
    ts = datetime(2017, 6, 7, 18, 0, 0, tzinfo=timezone.utc)

    dead_buses = list(range(8, 18))  # buses 8-17

    pt = build_event_point(
        scenario="realistic_sparse",
        experiment="fault",
        phase="faulted_isolated",
        faulted_line_id=7,
        tie_closed=0,
        tie_id=-1,
        n_dead_buses=10,
        dead_buses=dead_buses,
        ts=ts,
    )
    line = pt.to_line_protocol()
    assert "faulted_isolated" in line, f"phase=faulted_isolated not in line: {line}"
    assert "faulted_line_id=7i" in line, f"faulted_line_id=7 not in line: {line}"
    assert "n_dead_buses=10i" in line, f"n_dead_buses=10 not in line: {line}"
    # dead_buses should be comma-joined sorted: "8,9,10,11,12,13,14,15,16,17"
    assert "8,9,10,11,12,13,14,15,16,17" in line, (
        f"dead_buses comma string missing in line: {line}"
    )


def test_build_event_point_tie_id_always_int():
    """build_event_point must write tie_id as int field (not float — Pitfall 2)."""
    from ieee33.influx import build_event_point
    from datetime import datetime, timezone
    ts = datetime(2017, 6, 7, 18, 0, 3, tzinfo=timezone.utc)

    pt = build_event_point(
        scenario="well_observed",
        experiment="fault",
        phase="restored",
        faulted_line_id=7,
        tie_closed=1,
        tie_id=34,
        n_dead_buses=0,
        dead_buses=[],
        ts=ts,
    )
    line = pt.to_line_protocol()
    # InfluxDB integer literal ends with 'i'; float has decimal point
    assert "tie_id=34i" in line, (
        f"tie_id must be an integer field (34i), got line: {line}"
    )


def test_event_point_scenario_experiment_tagged():
    """build_event_point must add scenario and experiment as tags."""
    from ieee33.influx import build_event_point
    from datetime import datetime, timezone
    ts = datetime(2017, 6, 7, 0, 0, 0, tzinfo=timezone.utc)

    pt = build_event_point(
        scenario="well_observed",
        experiment="day",
        phase="steady_state",
        faulted_line_id=-1,
        tie_closed=0,
        tie_id=-1,
        n_dead_buses=0,
        dead_buses="",
        ts=ts,
    )
    line = pt.to_line_protocol()
    assert "scenario=well_observed" in line, f"scenario tag missing: {line}"
    assert "experiment=day" in line, f"experiment tag missing: {line}"
