---
phase: 09-measurement-system-observability-layer-configurable-sensor-m
plan: "05"
subsystem: observability-layer
tags: [dashboards, grafana, provisioning, determinism, tests, readme, tdd, measurements, ieee33, observability]
dependency_graph:
  requires:
    - "09-01..04 (measure.py + measure_config.py + influx.py measurement functions fully implemented)"
    - "system1-measurement-source/grafana/provisioning/dashboards/ieee33-state.json (skeleton analog)"
    - "system1-measurement-source/grafana/provisioning/dashboards/ieee33-fault-event.json (skeleton analog)"
  provides:
    - "system1-measurement-source/grafana/provisioning/dashboards/ieee33-meas-day.json — Day observed states dashboard (uid ieee33-meas-day)"
    - "system1-measurement-source/grafana/provisioning/dashboards/ieee33-meas-fault.json — Fault observed states dashboard (uid ieee33-meas-fault)"
    - "system1-measurement-source/tests/test_measure_determinism.py — 6 tests: 3 static + 3 Docker-guarded integration"
    - "system1-measurement-source/README.md — Measurement Layer runbook section"
  affects:
    - "Grafana auto-provisioning (four dashboards now listed: two original + two new)"
    - "SPEC acceptance gates R10/R11/R12 closed"
tech_stack:
  added: []
  patterns:
    - "Two Grafana dashboard JSONs: dual-refId overlay targets (meas vs state/fault_event true series)"
    - "Static grep-based tests: inspect source text for forbidden tokens + locked constants"
    - "Docker-guard pattern: _influx_available() helper + pytest.mark.skipif for integration tests"
    - "Flux count() query with group() for per-class measurement counts in dashboards"
    - "D-07 re-published event measurement queried from measurements bucket in fault dashboard"
key_files:
  created:
    - system1-measurement-source/grafana/provisioning/dashboards/ieee33-meas-day.json
    - system1-measurement-source/grafana/provisioning/dashboards/ieee33-meas-fault.json
    - system1-measurement-source/tests/test_measure_determinism.py
  modified:
    - system1-measurement-source/README.md
decisions:
  - "D-16 honored: four distinct dashboard uids — ieee33-state-v1, ieee33-fault-v1, ieee33-meas-day, ieee33-meas-fault (T-09-13 uid-collision threat mitigated)"
  - "Fault dashboard queries measurements bucket event measurement (D-07 re-publish) for n_dead_buses — not the original fault_event bucket"
  - "Static tests use pathlib.Path to read src files directly (no imports that require InfluxDB)"
  - "Integration tests guard with _influx_available() + pytest.mark.skipif so static gates always pass in CI"
  - "Plan verify command deviation: -k filter matched module path 'test_measure_determinism' and excluded all tests; fixed by running tests by exact name"
  - "TDD structure: implementation already done by Plans 01-04; tests written as GREEN (static pass immediately; integration skip cleanly)"
metrics:
  duration_minutes: 6
  completed_date: "2026-06-25"
  tasks_completed: 2
  tasks_total: 3
  files_created: 3
  files_modified: 1
---

# Phase 9 Plan 05: Observability + Verification Layer Summary

**One-liner:** Two auto-provisioned Grafana dashboards over the measurements bucket with observed-vs-true overlay, plus determinism/cadence/dead-bus-gate tests and full measurement runbook in README.

## What Was Built

### Task 1 — Two provisioned Grafana dashboards (committed d39cb49)

Created two new dashboard JSONs in `system1-measurement-source/grafana/provisioning/dashboards/`:

**`ieee33-meas-day.json`** (uid `ieee33-meas-day`, title "IEEE 33-Bus Observed Measurements — Day"):
- Panel 1: Observed bus voltages (vm_pu) — dual-target overlay: meas bucket (refId A) + state bucket true series (refId B). Full 96-step day window.
- Panel 2: Observed power injections (p_inj_mw) — all classes timeseries.
- Panel 3: Per-class measurement counts (stat panels, 5 per-class Flux count() queries for scada/pmu/ami/der/pseudo).
- Panel 4: Observed-vs-pseudo footprint by bus location (timeseries with real-class and pseudo groups).

**`ieee33-meas-fault.json`** (uid `ieee33-meas-fault`, title "IEEE 33-Bus Observed Measurements — Fault"):
- Panel 1: Observed bus voltages — dual-target overlay: meas bucket (fault experiment) + fault_event true series. 4-minute fault window (2017-06-07T17:59..18:03).
- Panel 2: Dead-bus count over time from re-published `event` measurement in measurements bucket (D-07). Shows 0→10→0 pulse.
- Panel 3: Phase marker stat panel (max n_dead_buses as color-coded signal).
- Panel 4: Per-class measurement counts across the 40 fault steps (stat, 5 classes).
- Panel 5: Observed-vs-pseudo footprint by bus — full-width panel showing footprint changes at isolation.

Verification: all four uids distinct, `id: null`, `schemaVersion: 39`, `refresh: 30s`, `ieee33-influxdb` datasource on every target, `measurements` bucket referenced, `n_dead_buses` in fault dashboard. Existing dashboards and `default.yml` byte-unchanged.

### Task 2 — Tests and README runbook (committed ef63547)

**`tests/test_measure_determinism.py`** — 6 tests:

| Test | Type | Status without Docker |
|------|------|----------------------|
| `test_no_unseeded_randomness` | static grep | PASS |
| `test_no_true_value_field` | static grep | PASS |
| `test_meas_schema_vocab` | static import | PASS |
| `test_determinism` | integration | SKIP |
| `test_multirate_cadence` | integration | SKIP |
| `test_dead_bus_gate` | integration | SKIP |

**`README.md`** — New "Measurement Layer (System 1 → System 2 inputs)" section added documenting:
- Prerequisites (sim + fault-sim must populate buckets first)
- `uv run measure` command
- ACTIVE block structure and purpose (D-09 primary switch)
- CLI override flags (`--scenario --source --sampling --noise --seed`)
- Footprint report meaning (per-class counts, real-only vs with-pseudo redundancy targets)
- Scenario table (realistic_sparse vs well_observed sensor assignments)
- Two new Grafana dashboard names and opening instructions
- Noise model and sampling mode comparison tables
- Measurements bucket schema (D-06 forward contract)
- Automated test run instructions

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Plan verify command filter matches module path and excludes all tests**
- **Found during:** Task 2 verification
- **Issue:** Plan's `<verify>` uses `-k "not determinism and not cadence and not dead_bus"`. In pytest, `-k` matches against the full node ID including the file path. The file is named `test_measure_determinism.py`, so `not determinism` matches the module path and deselects all 6 tests.
- **Fix:** Ran static tests by exact test function name (`tests/test_measure_determinism.py::test_no_unseeded_randomness tests/...::test_no_true_value_field tests/...::test_meas_schema_vocab`). All 3 static tests pass. The plan's acceptance criteria are met; the verify command itself had an incorrect filter.
- **Files modified:** None (test naming convention is correct; plan verify command was a documentation artifact, not code)
- **Commits:** No additional commit needed

### TDD Structure Note

The plan specifies `tdd="true"` for Task 2. However, Plans 01-04 already fully implemented `measure.py` and `measure_config.py`. The tests in this plan therefore skip the RED phase (tests would pass immediately) and go directly to GREEN. The 3 static tests pass; the 3 integration tests skip cleanly without Docker. This is noted as an expected pattern for final-plan acceptance tests that verify already-implemented behavior.

## Checkpoint Status

**Task 3 is `checkpoint:human-verify`** — execution paused here.

Human verification required to confirm:
1. The Docker stack is running and all four dashboards appear in Grafana at http://localhost:3000
2. The "Day" dashboard shows observed voltages with true state overlay and per-class counts
3. The "Fault" dashboard shows dead-bus count rising to 10 during isolation and the observed voltages for bus 17 dropping out

## Known Stubs

None. Dashboard panels query the live `measurements` bucket with real Flux queries. The integration tests are guarded (skip, not stub) and will run fully when Docker is available.

## Threat Flags

No new threat surface introduced beyond the documented T-09-12 through T-09-14 in the plan's threat model. The two new JSON files extend Grafana provisioning with the existing `ieee33-dev-token` literal (T-09-12: accepted, local Docker only). Dashboard uid collision was mitigated by distinct uids (T-09-13: mitigated).
