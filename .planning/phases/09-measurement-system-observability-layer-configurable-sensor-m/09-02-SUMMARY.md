---
phase: 09-measurement-system-observability-layer-configurable-sensor-m
plan: "02"
subsystem: influx-readers-writers
tags: [influxdb, flux, readers, writers, tdd, schema-contract]
dependency_graph:
  requires: [09-01]
  provides: [read_state_bus, read_state_sgen, read_fault_bus, read_fault_sgen, read_fault_event, build_meas_point, build_event_point, write_meas_points]
  affects: [09-03-measure-runner, system2-estimator]
tech_stack:
  added: []
  patterns: [flux-pivot-with-rowkey, influxdb-additive-helpers, tdd-red-green]
key_files:
  created:
    - system1-measurement-source/tests/test_influx_readers_writers.py
  modified:
    - system1-measurement-source/src/ieee33/influx.py
decisions:
  - "Readers follow read_profiles Flux pivot pattern exactly — one bulk query per source, guard None return"
  - "energised placed in pivot rowKey for all fault_event readers (bus + sgen), surfaces as string column"
  - "build_meas_point phase tag is conditional (added only when phase is not None)"
  - "build_event_point dead_buses accepts both iterable and pre-formatted string for flexibility"
  - "write_meas_points keeps bucket as default parameter 'measurements', stays independent of measure_config"
metrics:
  duration: 3 min
  completed: "2026-06-25"
  tasks: 2
  files_modified: 2
---

# Phase 9 Plan 02: Influx.py Reader/Writer Helpers Summary

InfluxDB reader functions (5) and writer helpers (3) appended to `influx.py` — additive, no existing function modified — providing the full schema-contract layer for the Phase 9 measurement runner.

## What Was Built

Five Flux reader functions and three writer helpers were appended to `system1-measurement-source/src/ieee33/influx.py`. All are additive — the five original functions (`get_client`, `wait_for_influx`, `ensure_bucket`, `read_profiles`, `write_state_step`, `write_fault_step`) are byte-unchanged.

### Task 1: Flux Readers (five functions)

| Function | Bucket | Measurement | Key columns |
|----------|--------|-------------|-------------|
| `read_state_bus` | `state` | `bus` | `_time, bus_id, vm_pu, va_degree` |
| `read_state_sgen` | `state` | `sgen` | `_time, sgen_id, p_mw, q_mvar` |
| `read_fault_bus` | `fault_event` | `bus` | `_time, bus_id, energised, vm_pu, va_degree, p_mw, q_mvar` |
| `read_fault_sgen` | `fault_event` | `sgen` | `_time, sgen_id, energised, p_mw, q_mvar` |
| `read_fault_event` | `fault_event` | `event` | `_time, phase, faulted_line_id, tie_closed, tie_id, n_dead_buses, dead_buses` |

Each reader:
- Mirrors `read_profiles` Flux pivot pattern (range → filter → pivot → sort)
- Guards `if df is None` and raises `RuntimeError` naming the prerequisite run (`uv run sim` / `uv run fault-sim`)
- Does NOT assert a fixed row count (fault has 40 steps × variable energised buses)

**Critical Pitfall 1 compliance:** `read_fault_bus` and `read_fault_sgen` place `energised` in the Flux `rowKey` list (`rowKey: ["_time", "bus_id", "energised"]`), so it surfaces as a string column (`"1"`/`"0"`) in the result DataFrame — not a missing or incorrectly typed field.

### Task 2: Writer Helpers (three functions)

| Function | Purpose |
|----------|---------|
| `build_meas_point` | Constructs `Point("meas")` with D-06 tags/fields; NO `true_value` |
| `build_event_point` | Constructs `Point("event")` for topology re-publish into `measurements` |
| `write_meas_points` | Bulk-writes a pre-built list of Points via `write_api.write()` |

**Critical D-06 compliance:** `build_meas_point` never sets `.field("true_value", ...)` — the scoring oracle stays separate. Fields are `value` and `assumed_sigma` only.

**Critical Pitfall 2 compliance:** `build_event_point` always casts `tie_id` via `int(tie_id)` — mirrors `write_fault_step` line 529 to prevent InfluxDB int/float type conflict across snapshots.

**D-07 compliance:** `build_event_point` accepts `scenario` and `experiment` as additional tags, extending the original `fault_event` event measurement schema for the `measurements` bucket.

## Test Coverage

12 tests written via TDD (RED → GREEN):
- 5 reader presence + interface tests
- 4 writer Point construction + tag/field content tests
- 3 source-level compliance tests (no `true_value` field, `int()` on `tie_id`, `energised` in `rowKey`)

## Deviations from Plan

None — plan executed exactly as written. Both tasks implemented in the same GREEN commit since the test file covered all 8 functions jointly (required functions from Task 2 were tested alongside Task 1 tests).

## Known Stubs

None. This plan adds library helpers only — no data-flow stubs; no placeholder values.

## Threat Flags

None. No new network endpoints, auth paths, or schema changes at trust boundaries introduced (threat analysis from plan's threat_model section confirms T-09-03/04/05 all have `accept` disposition with local-only scope).

## Self-Check

Files exist:
- `system1-measurement-source/tests/test_influx_readers_writers.py` — created
- `system1-measurement-source/src/ieee33/influx.py` — modified (8 functions appended)

Commits:
- `accd775` — test(09-02): TDD RED tests
- `1e01706` — feat(09-02): GREEN implementation

## Self-Check: PASSED
