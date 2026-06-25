---
phase: 09-measurement-system-observability-layer-configurable-sensor-m
plan: "03"
subsystem: measurement-layer
tags: [measurement-runner, sensor-model, observability, influxdb, numpy, ieee33]
dependency_graph:
  requires:
    - "09-01 (measure_config.py: SCENARIOS, CLASS_SIGMA, CADENCE, ACTIVE, MEASUREMENTS_BUCKET)"
    - "09-02 (influx.py: read_state_bus, read_state_sgen, read_fault_bus, read_fault_sgen, read_fault_event, read_profiles, build_meas_point, build_event_point, write_meas_points)"
    - "Phase 8 (state bucket populated by uv run sim)"
    - "Phase 8.1 (fault_event bucket populated by uv run fault-sim)"
  provides:
    - "system1-measurement-source/src/ieee33/measure.py — measurement runner with source switch, P_inj derivation, sensor selection, energised gate, snapshot writes"
  affects:
    - "measurements InfluxDB bucket (written, additive only)"
tech_stack:
  added: []
  patterns:
    - "source switch (day→state bucket / fault→fault_event bucket) via cfg['source']"
    - "P_inj derivation for day source: base_p[bus] * load_pu − sgen_p (Pitfall 6 mitigation)"
    - "energised == '1' gate (D-02/D-03): dead buses produce no meas or pseudo points"
    - "sorted class+bus iteration for deterministic RNG stream (Pitfall 5)"
    - "single np.random.default_rng(seed) before loop (SPEC R10)"
    - "pseudo = load buses not in any real-sensor class, per-scenario"
    - "PLACEHOLDER gaussian noise for Plan 03; Plan 04 adds instrument + outliers"
    - "write_meas_points SYNCHRONOUS per snapshot (overwrite-in-place keyed by tags+ts)"
key_files:
  created:
    - system1-measurement-source/src/ieee33/measure.py
  modified: []
decisions:
  - "D-09 honored: ACTIVE block is primary switch; CLI overrides for 5 knobs"
  - "D-02 honored: energised read as STRING tag via rowKey pivot; compared as == '1'"
  - "D-03 honored: energised gate skips dead buses for BOTH real and pseudo classes"
  - "D-04/D-05: sensor bus lists read from mc.SCENARIOS[scenario] per class"
  - "Pitfall 6 mitigated: day-source P_inj = base_p * load_pu − sgen_p (not from state bus)"
  - "Pitfall 5 mitigated: sorted(real_classes) then sorted(buses) before rng draw"
  - "Plan 04 hooks clearly marked: multirate cadence gate (pass) and event re-publish (TODO)"
metrics:
  duration_minutes: 6
  completed_date: "2026-06-25"
  tasks_completed: 2
  tasks_total: 2
  files_created: 1
  files_modified: 0
---

# Phase 09 Plan 03: Measurement Runner Data Path Summary

**One-liner:** `measure.py` snapshot-mode runner: source switch (day/fault), P_inj derivation via load-profile × base_p minus sgen, energised-gate dead-bus skip, SCENARIOS-driven sensor selection, seeded gaussian placeholder noise, SYNCHRONOUS per-snapshot writes to the measurements bucket.

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | measure.py scaffolding — CLI/config merge, client setup, source switch, true-value derivation | 65777e1 | src/ieee33/measure.py (created) |
| 2 | Per-snapshot sensor selection + energised gate + snapshot-mode meas writes | 65777e1 | src/ieee33/measure.py (extended, same commit) |

Note: Tasks 1 and 2 were committed in a single atomic commit because they build one module together; Task 1 provides the lookup builders and Task 2 provides the loop that calls them — splitting them would leave a non-runnable intermediate state.

## What Was Built

### measure.py (712 lines)

Six public/private functions required by plan:

1. `_parse_args()` — argparse with `--scenario / --source / --sampling / --noise / --seed`; all choices-validated; all default `None` so config file is primary switch.
2. `_merge_cfg(args)` — starts from `dict(mc.ACTIVE)`; overrides only non-None CLI values (D-09).
3. `_build_day_lookup(client, base_p_by_bus, base_q_by_bus)` — reads `read_state_bus` + `read_state_sgen` + `read_profiles`; derives `p_inj_mw = base_p * load_pu − sgen_p` per (step, bus); returns `(timestamps, lookup, sgen_lookup)`.
4. `_build_fault_lookup(client)` — reads `read_fault_bus` + `read_fault_sgen` + `read_fault_event`; `p_inj_mw = p_mw` directly from res_bus; retains `energised` string per (step, bus); returns `(timestamps, lookup, sgen_lookup, energised_by_step_bus, event_by_step)`.
5. `get_true_value(cls, quantity, step_idx, bus_id, lookup, sgen_lookup)` — maps each class+quantity to the correct scalar: scada/pmu vm_pu from lookup; pmu va_degree from lookup; scada/ami/pseudo p_inj_mw/q_inj_mvar from lookup; der p_mw/q_mvar from sgen_lookup; zero_inj always 0.0.
6. `main()` — wires everything: resolves cfg, builds net base loads (read-only), connects InfluxDB, reads ground truth via source switch, iterates sorted classes+buses per snapshot with energised gate and placeholder gaussian noise, writes via `write_meas_points`.

### Plan 04 hooks

Two clearly marked hooks left in place:
- `if cfg["sampling"] == "multirate_async": pass  # TODO(Plan 04): cadence gate`
- `# TODO(Plan 04): topology event re-publish (build_event_point + append to points)`

## Deviations from Plan

### Auto-fixed Issues

None.

### CLAUDE.md-driven Adjustments

None — plan followed exactly.

### Minor Wording Adjustments (determinism docstring)

The module docstring initially contained `datetime.now` and `time.time` literally (as part of "do NOT use these" warnings), which would cause the plan's `getsource` determinism grep check to fail. Adjusted docstring to avoid the literal substrings while preserving the same intent.

## Verification Results

```
scaffold OK   (getsource assert: default_rng, no wallclock, build_enhanced_33bus, all 5 functions)
loop OK       (getsource assert: default_rng, SYNCHRONOUS, energised, build_meas_point, write_meas_points, pseudo, sys.exit(1))
import clean  (from ieee33 import measure)
single seeded RNG: OK
energised gate: OK (D-03)
SCENARIOS used: OK (D-04/D-05)
```

### Acceptance criteria checklist

- [x] `grep -c "def _parse_args\|def _merge_cfg\|def _build_day_lookup\|def _build_fault_lookup\|def get_true_value\|def main"` → 6
- [x] `grep -n "p_inj\|base_p"` shows P_inj derivation (load - sgen) — line 227: `p_inj_mw = load_p - sgen_p`
- [x] `grep -c "datetime.now\|time.time\|np.random.seed"` → 0
- [x] `grep -q "default_rng"` — present at line 536
- [x] `grep -q 'np.random.default_rng(cfg["seed"])'` — FOUND
- [x] `grep -E "energised.*==.*['\"]1['\"]|!= ['\"]1['\"]"` — FOUND (live set built from eng == "1")
- [x] `grep -q "build_meas_point"` — FOUND
- [x] `grep -q "write_meas_points"` — FOUND
- [x] `grep -c "SYNCHRONOUS"` → 3 (import + write_api setup + comment)
- [x] `grep -q 'sys.exit(1)'` — FOUND

## Known Stubs

- **Noise hook:** gaussian noise only (Plan 03 scope). `gaussian_outliers` and `instrument` models are named in the `--noise` argparse choices but fall through to the same gaussian branch — Plan 04 will add the noise engine switch.
- **Multirate cadence gate:** `if cfg["sampling"] == "multirate_async": pass` — the cadence table from `measure_config.CADENCE` is imported but not used in Plan 03. Plan 04 adds the per-class step-decimation logic.
- **Topology event re-publish:** `build_event_point` is imported in `influx.py` but `measure.py` does not yet call it. The TODO comment is at line 649. Plan 04 adds this.
- **Footprint report:** per-class count summary is printed at the end but the full D-15 redundancy calculation (states = 2×(N_energised−1), real/pseudo redundancy) is deferred to Plan 04.

All stubs are intentional per the plan's interface contract: "Leave the clearly-marked noise hook + cadence-gate placeholder for plan 09-04."

## Threat Surface Scan

No new network endpoints, auth paths, file access patterns, or schema changes at trust boundaries introduced. `measure.py` writes only to the `measurements` bucket (additive; verified by grep: no write to STATE_BUCKET or FAULT_EVENT_BUCKET). CLI args are restricted by `argparse choices=[]` (T-09-06 mitigated). All InfluxDB I/O is local Docker only (T-09-07 accepted).

## Self-Check: PASSED

File check:
- `/home/juan/codes/ge-vernova-virtual-sensing/system1-measurement-source/src/ieee33/measure.py` — FOUND (712 lines)

Commit check:
- `65777e1` — FOUND (`feat(09-03): add measure.py — source switch, P_inj derivation, sensor selection, energised gate, snapshot writes`)
