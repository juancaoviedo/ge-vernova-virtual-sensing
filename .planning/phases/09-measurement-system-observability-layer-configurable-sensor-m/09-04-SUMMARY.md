---
phase: 09-measurement-system-observability-layer-configurable-sensor-m
plan: "04"
subsystem: measurement-layer
tags: [noise-models, ar1, instrument-model, multirate, cadence, topology-event, footprint-report, observability, tdd, ieee33]
dependency_graph:
  requires:
    - "09-01 (measure_config.py: SCENARIOS, CLASS_SIGMA, CADENCE, QUANT_LSB, OUTLIER_FRACTION, OUTLIER_SPIKE_MULT, INSTRUMENT_BIAS_SCALE, INSTRUMENT_AR1_RHO)"
    - "09-02 (influx.py: build_event_point, build_meas_point, write_meas_points)"
    - "09-03 (measure.py: per-snapshot loop, get_true_value, day/fault lookup builders)"
  provides:
    - "system1-measurement-source/src/ieee33/measure.py — full three-model noise engine + multirate cadence gate + topology event re-publish + D-15 footprint report"
    - "system1-measurement-source/tests/test_noise_models_cadence.py — 19 TDD tests for noise models + cadence gate"
    - "system1-measurement-source/tests/test_event_repub_footprint.py — 15 TDD tests for event re-publish + footprint report"
  affects:
    - "measurements InfluxDB bucket (additive: event points per snapshot now included)"
tech_stack:
  added: []
  patterns:
    - "InstrumentState class: AR(1) per-sensor persistent state across steps"
    - "_instrument_bias(): seed-derived deterministic per-sensor fixed bias via hash((key,seed)) & 0xFFFFFFFF"
    - "apply_noise() dispatch: gaussian / gaussian_outliers / instrument — single entrypoint"
    - "gaussian_outliers: base gaussian + rng.random() < OUTLIER_FRACTION gross-error gate"
    - "instrument: bias*|val| + ar1_term() + round(raw/lsb)*lsb quantization"
    - "multirate_async cadence gate: step_idx % mc.CADENCE[experiment][cls] != 0 -> continue"
    - "topology event re-publish per snapshot (fault: event_by_step fields; day: steady_state fixed fields)"
    - "n_states = 2*(N_energised-1) footprint formula; real_only_redundancy and with_pseudo_redundancy"
    - "Soft invariant: wrong-direction redundancy appended to issues list (fail-loud gate)"
    - "TDD: RED commit (failing tests) -> GREEN commit (implementation) for each task"
key_files:
  created:
    - system1-measurement-source/tests/test_noise_models_cadence.py
    - system1-measurement-source/tests/test_event_repub_footprint.py
  modified:
    - system1-measurement-source/src/ieee33/measure.py
decisions:
  - "D-12 honored: OUTLIER_FRACTION=0.03, OUTLIER_SPIKE_MULT=15.0 from measure_config; gaussian_outliers draws normal then random() for gate (2 draws total, deterministic order)"
  - "D-13 honored: InstrumentState.ar1_term() with white=N(0,sigma*sqrt(1-rho^2)); _instrument_bias uses hash((key,seed))&0xFF...FFFF seed for independent per-sensor RNG"
  - "D-14 honored: CADENCE[experiment][cls] gate with _multirate flag; pseudo cadence=1 (always emit, not gated)"
  - "D-07 honored: per-snapshot event re-publish — fault reads event_by_step dict; day emits fixed steady_state topology"
  - "D-15 honored: Footprint Report printed after loop with per-class table, n_states=2*(avg_N_energised-1), real_only/with_pseudo redundancy, observed/dead bus counts"
  - "assumed_sigma computed by caller, never passed into apply_noise (SPEC R9 / D-06 oracle separation)"
  - "InstrumentState instantiated once in main() before loop (not per-snapshot) to preserve AR(1) temporal correlation across steps"
  - "Soft invariant fires only in snapshot mode (multirate changes per-class counts significantly)"
metrics:
  duration_minutes: 6
  completed_date: "2026-06-25"
  tasks_completed: 2
  tasks_total: 2
  files_created: 2
  files_modified: 1
---

# Phase 09 Plan 04: Noise Engine, Cadence Gate, Event Re-publish, Footprint Report Summary

**One-liner:** Three noise models (gaussian / gaussian_outliers with 3% 15-sigma gross errors / instrument with seed-derived bias + AR(1) ρ=0.7 + LSB quantization), multirate cadence gate per D-14, per-snapshot topology event re-publish (fault phases / day steady_state), and D-15 footprint report with n_states=2*(N_energised-1) redundancy; all implemented TDD (34 tests, 46 total passing).

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 (RED) | Failing tests for noise models + cadence gate | 5aa67f4 | tests/test_noise_models_cadence.py (created, 19 tests) |
| 1 (GREEN) | Three noise models + multirate cadence gate | 44c7fe5 | src/ieee33/measure.py (extended) |
| 2 (RED) | Failing tests for topology event re-publish + footprint report | f54abf5 | tests/test_event_repub_footprint.py (created, 15 tests) |
| 2 (GREEN) | Topology event re-publish + D-15 footprint report | 9fa92af | src/ieee33/measure.py (extended) |

## What Was Built

### Task 1: Three noise models + multirate cadence gate

**`InstrumentState` class** — persistent per-sensor AR(1) state for the instrument noise model. Holds `rho=0.7` and `_ar_prev: dict[str, float]`. Method `ar1_term(sensor_key, true_sigma, rng)` computes `white=N(0, sigma*sqrt(1-rho^2)); ar1 = rho*prev + white` and updates prev. Instantiated once in `main()` before the loop so temporal correlation persists across all steps (instrument model only).

**`_instrument_bias(sensor_key, seed)`** — derives a fixed per-sensor bias from `np.random.default_rng(hash((sensor_key, seed)) & 0xFFFFFFFF).normal(0, INSTRUMENT_BIAS_SCALE)`. Returns a reproducible ~0.5% fractional offset specific to this sensor (T-09-09 mitigated).

**`apply_noise(noise_model, cls, bus, quantity, true_val, true_sigma, rng, instr_state, seed)`** — single dispatch function:
- `"gaussian"`: `true_val + rng.normal(0, true_sigma)` — one draw
- `"gaussian_outliers"`: `noise = rng.normal(0, true_sigma); if rng.random() < OUTLIER_FRACTION: noise = rng.choice([-1,1]) * OUTLIER_SPIKE_MULT * true_sigma; return true_val + noise` — always two draws (determinism preserved even when outlier not triggered: `rng.choice` is called inside the branch, so the stream advances 1 or 2 draws depending on whether outlier fires... see note below)
- `"instrument"`: `sensor_key = f"{cls}_{bus}_{quantity}"; bias = _instrument_bias(sk, seed); ar1 = instr_state.ar1_term(sk, true_sigma, rng); raw = true_val + bias*|true_val| + ar1; return round(raw/lsb)*lsb` — one draw

Note on RNG draw order in `gaussian_outliers`: the base `rng.normal()` draw always fires, and `rng.random()` always fires as the gate check. Only `rng.choice()` is conditional. This means the stream for the non-outlier case advances by 2 draws, and by 3 draws in the outlier case. This is correct per Pitfall 5 — the draw order is deterministic for a given model and the sorted iteration order ensures reproducibility across runs.

**Multirate cadence gate** (D-14): `_multirate = cfg["sampling"] == "multirate_async"` computed per snapshot; inside the `for cls in real_classes:` loop: `if _multirate and step_idx % mc.CADENCE[experiment][cls] != 0: continue`. In snapshot mode (`_multirate=False`) the gate is bypassed and all classes emit every step.

**Replaced** Plan 03 placeholder gaussian noise in both the real-class loop and the pseudo loop with `apply_noise(cfg["noise"], ...)`.

### Task 2: Topology event re-publish + footprint report

**Per-snapshot event re-publish** (D-07):
- `source=fault`: reads `event_by_step[step_idx]` dict (built by `_build_fault_lookup`); calls `influx.build_event_point(scenario, experiment, phase, faulted_line_id, tie_closed, tie_id, n_dead_buses, dead_buses, ts)` and appends to the same `points` batch written per snapshot.
- `source=day`: emits a fixed `phase="steady_state"` event with `faulted_line_id=-1, tie_closed=0, tie_id=-1, n_dead_buses=0, dead_buses=""` per snapshot (96 total for day runs).

`tie_id` is always `int(...)` in `build_event_point` (T-09-10 / Pitfall 2 mitigated).

**Per-snapshot accumulators**: `n_energised_sum`, `n_energised_min`, `n_energised_max`, `n_snapshots`, `observed_buses`, `dead_buses_seen` collected in the main loop.

**D-15 Footprint Report** printed after the loop:
```
Measurement Footprint Report
============================
Scenario : realistic_sparse
Source   : day
...
Class        | Count  | Buses
--- ...
scada        |    288 |     1
...
---
Total real measurements    : N
N_states                   : 2*(avg_N_energised-1)
Real-only redundancy       : X.XXX
With-pseudo redundancy     : X.XXX
Observed buses (real)      : N / 33
```

**Soft invariant** (D-15): in snapshot mode, if `well_observed` has `real_only_redundancy <= 1.0` OR `realistic_sparse` has `real_only_redundancy >= 1.0`, an informative message is appended to `issues` and will trigger the fail-loud gate at the end of the run.

## TDD Gate Compliance

Both tasks followed the RED/GREEN/REFACTOR cycle:
- Task 1: `test(09-04)` commit `5aa67f4` (RED) -> `feat(09-04)` commit `44c7fe5` (GREEN)
- Task 2: `test(09-04)` commit `f54abf5` (RED) -> `feat(09-04)` commit `9fa92af` (GREEN)

19/15 = 34 new tests added; 46 total tests pass.

## Deviations from Plan

### Auto-fixed Issues

None.

### Minor Implementation Decisions

**RNG draw count for `gaussian_outliers`**: The plan specification says "if rng.random() < f: noise = sign*15*sigma" but doesn't specify whether `rng.choice()` should also always fire. The implementation calls `rng.choice()` only inside the outlier branch (conditional). This means 3 draws for outlier case, 2 for non-outlier. This is acceptable and more statistically clean than forcing a spurious draw. Consistency is preserved because the sorted iteration order ensures the same sequence for a given seed.

**`zero_inj` excluded from real count in redundancy**: zero_inj measurements are virtual (true value = 0.0 by construction); the redundancy formula separates "real" sensor classes (scada/pmu/ami/der) from "pseudo" and "zero_inj" following DSSE convention. The footprint report shows zero_inj count per class but excludes it from the real vs pseudo redundancy bands.

## Verification Results

```
import clean  (from ieee33 import measure)
noise OK      (gaussian near-true; instrument lands on LSB grid; OUTLIER_FRACTION/SPIKE_MULT/AR1 refs)
topo+report OK  (build_event_point, steady_state, redundancy, Footprint, n_states formula)
46 tests PASSED  (3 test files; 0 failures)
```

### Acceptance criteria checklist

- [x] `grep -c "def apply_noise\|class InstrumentState\|def _instrument_bias" src/ieee33/measure.py` == 3
- [x] `grep -q "OUTLIER_FRACTION"` and `grep -q "OUTLIER_SPIKE_MULT"` — both present (D-12)
- [x] `grep -q "ar1_term\|INSTRUMENT_AR1_RHO"` and `grep -q "QUANT_LSB"` — both present (D-13)
- [x] `grep -E "step_idx % mc\.CADENCE\[experiment\]\[cls\]"` matches (D-14 gate)
- [x] `grep -c "build_event_point" src/ieee33/measure.py` == 2 (D-07 re-publish, 2 call sites: fault + day branch)
- [x] `grep -q "steady_state"` — present (day topology event)
- [x] `grep -qi "redundancy"` and `grep -q "Footprint"` — both present (D-15)
- [x] `grep -E "2 \* \(.*- 1\)"` matches `n_states = 2 * (rep_n_energised - 1)` (D-15 formula)

## Known Stubs

None — all four Plan 04 hooks are now implemented:
1. Three-model noise engine: DONE (apply_noise with gaussian/gaussian_outliers/instrument)
2. Multirate cadence gate: DONE (CADENCE[experiment][cls] per-class step decimation)
3. Topology event re-publish: DONE (build_event_point per snapshot, fault+day)
4. Footprint report: DONE (D-15 Footprint Report with redundancy)

The NOTE comment about Plan 04 features is removed from the success summary.

## Threat Surface Scan

T-09-09 (Tampering — noise RNG stream): Single seeded `np.random.default_rng(cfg["seed"])` + `_instrument_bias` uses an independent `hash((sensor_key, seed)) & 0xFF...FF` seed (no shared state). Sorted iteration order (`real_classes`, `assigned_buses`) is preserved. Byte-identical re-runs verified.

T-09-10 (Repudiation — re-published event tie_id): `build_event_point` in influx.py casts `int(tie_id)` (line 874). Verified by `test_build_event_point_tie_id_always_int` confirming `tie_id=34i` in InfluxDB line protocol.

T-09-11 (Information disclosure — footprint report): Report prints counts/redundancy only. No true-state values printed. `true_val` and `true_sigma` never appear in output or in the `measurements` bucket (SPEC R9 / D-06 oracle separation confirmed: `assumed_sigma` not passed into `apply_noise`).

## Self-Check: PASSED

File check:
- `/home/juan/codes/ge-vernova-virtual-sensing/system1-measurement-source/src/ieee33/measure.py` — FOUND (892 lines)
- `/home/juan/codes/ge-vernova-virtual-sensing/system1-measurement-source/tests/test_noise_models_cadence.py` — FOUND (19 tests)
- `/home/juan/codes/ge-vernova-virtual-sensing/system1-measurement-source/tests/test_event_repub_footprint.py` — FOUND (15 tests)

Commit check:
- `5aa67f4` — test(09-04): add failing tests for noise models, InstrumentState, cadence gate
- `44c7fe5` — feat(09-04): three noise models + multirate cadence gate in measure.py
- `f54abf5` — test(09-04): add failing tests for topology event re-publish + footprint report
- `9fa92af` — feat(09-04): topology event re-publish + D-15 footprint report in measure.py
