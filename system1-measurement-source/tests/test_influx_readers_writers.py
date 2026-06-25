"""
test_influx_readers_writers.py
------------------------------
TDD tests for the Phase 9 Plan 02 reader/writer helpers added to influx.py.

These tests verify the interface contract (function signatures present, correct
tags/fields in built Points, energised in rowKey) WITHOUT requiring a live
InfluxDB connection — all reader tests are import-and-inspect-level or use
offline Point construction.

Run: cd system1-measurement-source && uv run python -m pytest tests/ -v
"""

import inspect
from datetime import datetime, timezone

import pytest


def test_reader_functions_present():
    """All five reader functions must be present in influx.py."""
    from ieee33 import influx

    src = inspect.getsource(influx)
    assert "def read_state_bus" in src, "read_state_bus missing"
    assert "def read_state_sgen" in src, "read_state_sgen missing"
    assert "def read_fault_bus" in src, "read_fault_bus missing"
    assert "def read_fault_sgen" in src, "read_fault_sgen missing"
    assert "def read_fault_event" in src, "read_fault_event missing"


def test_energised_in_rowkey():
    """energised must appear in pivot rowKey for fault readers (Pitfall 1)."""
    from ieee33 import influx

    src = inspect.getsource(influx)
    # energised must be in a rowKey list in the source
    assert 'energised' in src, "energised not in influx.py at all"
    assert 'rowKey' in src, "rowKey not in influx.py at all"
    # The energised column must appear inside a rowKey list
    import re
    # Look for rowKey: [..., "energised", ...] or rowKey: ["_time", "bus_id", "energised"]
    matches = re.findall(r'rowKey.*?energised', src)
    assert matches, "energised not found in any rowKey context (Pitfall 1)"


def test_existing_functions_untouched():
    """Original five functions must still be present (additive constraint)."""
    from ieee33 import influx

    src = inspect.getsource(influx)
    assert "def read_profiles" in src
    assert "def write_state_step" in src
    assert "def write_fault_step" in src
    assert "def get_client" in src
    assert "def ensure_bucket" in src


def test_reader_error_messages_name_prerequisites():
    """RuntimeError messages in readers must name the prerequisite run commands."""
    from ieee33 import influx

    src = inspect.getsource(influx)
    # Both 'uv run sim' and 'uv run fault-sim' (or 'fault-sim') must appear
    # in the error messages so users know what to run
    assert "uv run sim" in src or "fault-sim" in src, (
        "Reader RuntimeError messages must name the prerequisite run command"
    )


def test_writer_functions_present():
    """Three writer helpers must be present in influx.py."""
    from ieee33 import influx

    src = inspect.getsource(influx)
    assert "def build_meas_point" in src, "build_meas_point missing"
    assert "def build_event_point" in src, "build_event_point missing"
    assert "def write_meas_points" in src, "write_meas_points missing"


def test_build_meas_point_no_true_value():
    """build_meas_point must NOT add a true_value field (D-06)."""
    from ieee33 import influx

    ts = datetime(2017, 6, 7, tzinfo=timezone.utc)
    p = influx.build_meas_point(
        cls="pmu",
        quantity="vm_pu",
        location=17,
        scenario="well_observed",
        experiment="fault",
        value=1.01,
        assumed_sigma=0.001,
        ts=ts,
        phase="faulted_isolated",
    )
    lp = p.to_line_protocol()
    assert "true_value" not in lp, f"true_value found in line protocol: {lp}"
    assert "value=" in lp, "value field missing"
    assert "assumed_sigma=" in lp, "assumed_sigma field missing"


def test_build_meas_point_tags():
    """build_meas_point must set correct tags (class, quantity, location, scenario, experiment)."""
    from ieee33 import influx

    ts = datetime(2017, 6, 7, tzinfo=timezone.utc)
    p = influx.build_meas_point(
        cls="scada",
        quantity="p_inj_mw",
        location=0,
        scenario="realistic_sparse",
        experiment="day",
        value=1.5,
        assumed_sigma=0.03,
        ts=ts,
    )
    lp = p.to_line_protocol()
    assert "meas," in lp, f"measurement name 'meas' missing: {lp}"
    assert "class=scada" in lp, f"class tag missing: {lp}"
    assert "quantity=p_inj_mw" in lp, f"quantity tag missing: {lp}"
    assert "location=0" in lp, f"location tag missing: {lp}"
    assert "scenario=realistic_sparse" in lp, f"scenario tag missing: {lp}"
    assert "experiment=day" in lp, f"experiment tag missing: {lp}"


def test_build_meas_point_phase_tag_conditional():
    """phase tag is present when phase is given, absent when phase=None."""
    from ieee33 import influx

    ts = datetime(2017, 6, 7, tzinfo=timezone.utc)
    # With phase
    p_with = influx.build_meas_point(
        cls="pmu", quantity="vm_pu", location=17,
        scenario="well_observed", experiment="fault",
        value=1.0, assumed_sigma=0.001, ts=ts, phase="pre_fault"
    )
    assert "phase=pre_fault" in p_with.to_line_protocol()

    # Without phase
    p_without = influx.build_meas_point(
        cls="pmu", quantity="vm_pu", location=17,
        scenario="well_observed", experiment="day",
        value=1.0, assumed_sigma=0.001, ts=ts
    )
    assert "phase=" not in p_without.to_line_protocol()


def test_build_event_point_tie_id_always_int():
    """build_event_point must write tie_id as int (Pitfall 2)."""
    from ieee33 import influx

    ts = datetime(2017, 6, 7, tzinfo=timezone.utc)
    # tie open → tie_id = -1 (int, not float)
    e = influx.build_event_point(
        scenario="day",
        experiment="day",
        phase="steady_state",
        faulted_line_id=-1,
        tie_closed=0,
        tie_id=-1,
        n_dead_buses=0,
        dead_buses="",
        ts=ts,
    )
    lp = e.to_line_protocol()
    # InfluxDB int fields end with 'i' in line protocol
    assert "tie_id=-1i" in lp, (
        f"tie_id must be int (-1i), got: {lp}"
    )


def test_build_event_point_tags():
    """build_event_point must have tags scenario, experiment, phase."""
    from ieee33 import influx

    ts = datetime(2017, 6, 7, tzinfo=timezone.utc)
    e = influx.build_event_point(
        scenario="well_observed",
        experiment="fault",
        phase="faulted_isolated",
        faulted_line_id=7,
        tie_closed=0,
        tie_id=-1,
        n_dead_buses=10,
        dead_buses="8,9,10,11,12,13,14,15,16,17",
        ts=ts,
    )
    lp = e.to_line_protocol()
    assert "event," in lp, f"event measurement missing: {lp}"
    assert "scenario=well_observed" in lp
    assert "experiment=fault" in lp
    assert "phase=faulted_isolated" in lp


def test_no_true_value_field_in_source():
    """influx.py must never define .field('true_value', ...) — hard contract (D-06)."""
    from ieee33 import influx

    src = inspect.getsource(influx)
    import re
    matches = re.findall(r'\.field\(["\']true_value["\']', src)
    assert not matches, (
        f"true_value field found in influx.py source — violates D-06: {matches}"
    )


def test_tie_id_int_cast_in_source():
    """build_event_point in source must cast tie_id via int() (Pitfall 2)."""
    from ieee33 import influx

    src = inspect.getsource(influx)
    import re
    # Must have int(...) somewhere near tie_id in build_event_point
    fn_src = src[src.find("def build_event_point"):]
    fn_src = fn_src[:fn_src.find("\ndef ", 5)]  # up to next def
    assert "int(" in fn_src and "tie_id" in fn_src, (
        "build_event_point must cast tie_id with int()"
    )
