---
phase: 09-measurement-system-observability-layer-configurable-sensor-m
plan: "01"
subsystem: measurement-config
tags: [python, influxdb, ieee33, measurement-layer, observability, sensor-model, pure-constants]

requires:
  - phase: 08-ieee-33-bus-der-measurement-source
    provides: System 1 ground-truth (state bucket + 96-step day simulation)
  - phase: 08.1-system-1-fault-and-reconfiguration-scenario
    provides: fault_event bucket schema (bus/line/sgen/event + energised tag) locked by D-01..D-03

provides:
  - "measure_config.py: single source of all measurement-layer constants (CLASS_SIGMA, CADENCE, SCENARIOS, ACTIVE, QUANT_LSB, schema vocabulary)"
  - "measure script entry point registered in pyproject.toml (ieee33.measure:main)"

affects:
  - "09-02 (Plan 02): influx.py writer extension — reads MEAS_QUANTITIES, MEASUREMENTS_BUCKET from here"
  - "09-03 (Plan 03): measure.py runner — imports ACTIVE, CLASS_SIGMA, CADENCE, SCENARIOS"
  - "09-04 (Plan 04): Grafana dashboards — scenario names from SCENARIOS keys"
  - "09-05 (Plan 05): tests — import all constants, assert exact D-04/D-05/D-11/D-14 values"

tech-stack:
  added: []
  patterns:
    - "pure-constants module pattern (no I/O side effects, no imports beyond stdlib, docstring declares 'pure constants')"
    - "ACTIVE-block primary-switch pattern: one dict with all experiment knobs + inline option comments"
    - "Decision-cited inline comments: every constant has D-NN reference matching CONTEXT.md decisions"
    - "Oracle-separation contract: MEASUREMENTS_BUCKET schema explicitly excludes true_value (SPEC R9/D-06)"

key-files:
  created:
    - system1-measurement-source/src/ieee33/measure_config.py
  modified:
    - system1-measurement-source/pyproject.toml

key-decisions:
  - "D-04 values locked: realistic_sparse SCADA=[0], PMU=[17,24,30], DER=[17,21,24,32], AMI=[3,6,9,12,15,18,21,24,28,31], zero_inj=[]"
  - "D-05 values locked: well_observed SCADA=[0], PMU=[0,4,8,13,17,21,24,28,32], DER=[17,21,24,32], AMI=[1,2,3,6,7,9,11,12,14,15,16,18,19,22,23,26,27,30,31], zero_inj=[2,19]"
  - "D-06 oracle separation: ACTIVE/SCENARIOS/schema vocabulary all declare NO true_value field in measurements bucket"
  - "D-09 ACTIVE block as primary switch: all 6 keys with inline option comments; CLI overrides overlay in Plan 03"
  - "D-11 sigma values locked: pmu.va_degree=0.0003 rad (absolute, not fraction); pseudo=0.30; zero_inj=1e-4"
  - "D-14 cadences locked: day ami=4, fault scada=2, fault ami=10 (all others =1)"

patterns-established:
  - "Pure-constants module: no imports, no I/O, only typed dict constants with section headers and D-NN comments"
  - "ACTIVE block: primary experiment switch with 6 keys and inline valid-options comments for each"

requirements-completed: [R1, R2, R3, R4, R5, R8]

duration: 2min
completed: "2026-06-25"
---

# Phase 9 Plan 01: Measurement Config Summary

**Pure-constants `measure_config.py` with locked D-04/D-05/D-11/D-14 values (CLASS_SIGMA, CADENCE, SCENARIOS, QUANT_LSB, ACTIVE) and `measure` uv script registered — contracts module for all downstream Phase 9 plans**

## Performance

- **Duration:** 2 min
- **Started:** 2026-06-25T06:49:42Z
- **Completed:** 2026-06-25T06:51:52Z
- **Tasks:** 2
- **Files modified:** 2

## Accomplishments

- Created `measure_config.py` (274 lines) as a pure-constants module with zero imports — no `os`, no `dotenv`, no `np.random`, no `datetime` — imports cleanly as `from ieee33 import measure_config as mc`
- All locked decision values present and assertion-verified: CLASS_SIGMA (D-11), CADENCE (D-14), SCENARIOS (D-04/D-05), ACTIVE (D-09), QUANT_LSB (D-13), noise defaults (D-12), schema vocabulary (D-06)
- `measure = "ieee33.measure:main"` registered in `pyproject.toml [project.scripts]` alongside the 4 existing entries (ingest/sim/validate/fault-sim), column-aligned; `tomllib` parse verified all 5 entries present

## Task Commits

1. **Task 1: Create measure_config.py** - `e9b75de` (feat)
2. **Task 2: Register measure script entry point** - `88d2f83` (feat)

## Files Created/Modified

- `system1-measurement-source/src/ieee33/measure_config.py` — pure-constants measurement-layer config: CLASS_SIGMA, CADENCE, SCENARIOS (realistic_sparse + well_observed), QUANT_LSB, noise defaults, schema vocabulary (MEAS_MEASUREMENT/CLASSES/QUANTITIES/MEASUREMENTS_BUCKET), ACTIVE block
- `system1-measurement-source/pyproject.toml` — added `measure = "ieee33.measure:main"` to `[project.scripts]`

## Decisions Made

- AMI list for `well_observed` computed as: all load buses 1..32 MINUS held-out `{5,10,20,25,29}` MINUS PMU-covered `{0,4,8,13,17,21,24,28,32}` = `[1,2,3,6,7,9,11,12,14,15,16,18,19,22,23,26,27,30,31]` (19 buses, explicit list for greppability per D-05)
- `pmu.va_degree` comment explicitly states "ABSOLUTE radians, not a fraction" to prevent misinterpretation by downstream consumers
- `CADENCE["day"]["ami"] = 4` with comment "every 4th step → 1-hour AMI cycle" for clarity
- Oracle separation documented as a `CRITICAL` block in the schema vocabulary section (not just a code comment)

## Deviations from Plan

None — plan executed exactly as written. The AMI bus list derivation for `well_observed` was within "Claude's Discretion" (D-05) and matched the stated criteria.

## Issues Encountered

None. The automated verification (`uv run python -c "..."`) passed on first run. The acceptance-criteria grep for "no forbidden imports" matched docstring text (not actual imports); confirmed clean via AST inspection.

## Known Stubs

None — this is a pure-constants module. All values are complete and greppable. No placeholder text.

## Threat Flags

None — this plan adds only a pure-constants module and a toml script line. No I/O, no network, no new trust boundary (T-09-01/T-09-02 both accepted per plan threat model).

## Next Phase Readiness

- `measure_config.py` is the contracts module for all downstream Phase 9 plans
- Plan 02 can now add `write_meas_step` to `influx.py` importing `MEASUREMENTS_BUCKET` from here
- Plan 03 can implement `measure.py` runner importing `ACTIVE`, `CLASS_SIGMA`, `CADENCE`, `SCENARIOS`
- Plan 05 tests can assert exact constant values against D-04/D-05/D-11/D-14 locked decisions
- `uv run measure` will resolve once Plan 03 delivers `ieee33/measure.py`

---
*Phase: 09-measurement-system-observability-layer-configurable-sensor-m*
*Completed: 2026-06-25*
