---
phase: 10-system-2-streaming-distribution-state-estimator-mqtt-fase
plan: "07"
subsystem: estimator
tags: [ac-model, wls, state-estimation, ieee33, numpy, jacobian, ybus]

requires:
  - phase: 10-system-2-streaming-distribution-state-estimator-mqtt-fase (plans 01-06)
    provides: ac_model, estimators, estimate runner, estimate_config, influx writer already built
provides:
  - 64-state (buses 1..32, bus 0 fixed reference) h(x)/H in ac_model — D-11 convention
  - G = H^T W H confirmed (64,64) rank 64 on full well_observed set — bug #3 closed
  - estimate.py sizes state at 64 (N_FREE_STATES), n_bus_est at 32
  - write_estimate_step emits bus_id 1..32 matching score oracle range
affects:
  - 10-08 (injection_sensitivity + predict rewrite builds on 64/32 state)
  - 10-10 (forecast consumer wiring, WLS end-to-end test)

tech-stack:
  added: []
  patterns:
    - D-11 state convention: x=[|V|_1,θ_1,...,|V|_32,θ_32] (64 entries); bus 0 fixed reference (ref_vm,0); bus 33 slack fixed in Ybus
    - Jacobian H is (n_meas,64); partial derivatives w.r.t. free buses 1..32 only; fixed buses contribute to diagonal sums but have no H columns
    - Dead-bus mask maps db-1 and guards 1<=db<=32 (bus 0 cannot be dead — it is the reference)
    - bus_id tag in InfluxDB = state_index//2 + 1 to match score oracle (buses 1..32)

key-files:
  created: []
  modified:
    - system1-measurement-source/src/ieee33/ac_model.py
    - system1-measurement-source/src/ieee33/estimate.py
    - system1-measurement-source/src/ieee33/influx.py

key-decisions:
  - "D-11 applied consistently: state is 64 = 2x32 (buses 1..32); bus 0 excluded as electrical reference (regulated |V|_0, theta_0=0)"
  - "WLS rank gate in wls_gauss_newton retained unchanged (SPEC R5: raises RankDeficientError when G is rank-deficient)"
  - "bus_id InfluxDB tag changed from i to i+1 so emitted IDs are 1..32, aligning with score oracle"

patterns-established:
  - "64-state ac_model: V_est/T_est are length 32; bus_i lookups use bus_i-1; bus 0 handled as fixed pickoff/fixed addend in injection sums"

requirements-completed: [R5, R6, R7, R10]

duration: 35min
completed: 2026-07-01
---

# Phase 10 Plan 07: GAP CLOSURE Summary

**AC-WLS gain matrix G confirmed (64,64) rank 64 on well_observed by fixing state dim 66->64 (bus 0 excluded) and re-keying h(x)/H to D-11 convention across ac_model/estimate/influx — bug #3 closed**

## Performance

- **Duration:** ~35 min
- **Started:** 2026-07-01T00:00:00Z
- **Completed:** 2026-07-01T00:35:00Z
- **Tasks:** 2 of 2
- **Files modified:** 3

## Accomplishments

- Fixed bug #3 root cause (a): state dimension 66 -> 64 by excluding bus 0 (electrical reference) from the free state across ac_model, estimate.py, and influx.py
- Fixed bug #3 root cause (b): re-keyed h(x)/jacobian_H so that the full well_observed real measurement set reaches H and G = H^T W H is (64,64) rank 64 without pseudo-measurements
- Numerically asserted: G rank == 64 on 96-element well_observed meas set (|V|+P_inj+Q_inj at buses 1..32 at flat start)
- Updated write_estimate_step bus_id tag to emit 1..32, matching score oracle range

## Task Commits

1. **Task 1: Re-key ac_model state convention to 64=2x32 (buses 1..32), bus 0 as fixed reference** - `6ba2b7d` (fix)
2. **Task 2: Wire estimate.py + estimators + write_estimate_step to 64/32 state definition** - `d4f3a44` (fix)

## Files Created/Modified

- `system1-measurement-source/src/ieee33/ac_model.py` - Rewrote _N_EST_BUS=32/_N_FREE=64 constants; _p_inj/_q_inj take V_est/T_est (length 32); h_func/jacobian_H: 64-state bus_i-1 indexing, bus 0 as fixed pickoff; verify_model: x_flat length 64, H.shape[1]==64 assertion
- `system1-measurement-source/src/ieee33/estimate.py` - n_bus_est=N_FREE_STATES//2 (32), n_state=N_FREE_STATES (64); dead-bus mask guards 1<=db<=32 and maps db-1
- `system1-measurement-source/src/ieee33/influx.py` - write_estimate_step bus_id changed from str(i) to str(i+1) so emitted IDs are 1..32

## Decisions Made

- Bus 0 is the electrical feeder-head reference (regulated |V|_0 by OLTC, theta_0=0 fixed) — NOT an estimated state. This is the correct physical interpretation: the reference-bus voltage is a known/regulated boundary condition, not an unknown to solve for.
- WLS rank gate unchanged: still raises RankDeficientError on rank-deficient G. With the 64-state model and full well_observed set, G is rank 64 and the exception is never triggered on well_observed.
- Fixed buses (0 and 33) contribute to the off-diagonal sums in _p_inj/_q_inj and the diagonal dP/d|V_i| terms in jacobian_H, but their |V|/theta are not free states so no H columns correspond to them.

## Deviations from Plan

None - plan executed exactly as written. Both root causes (a) and (b) of bug #3 addressed as specified.

## Issues Encountered

None. The Jacobian finite-difference check passed at 3.35e-09 (well below 1e-5 tolerance), confirming the re-keyed Bergen & Vittal partial derivatives are correct.

## Threat Surface Scan

No new network endpoints, auth paths, file access patterns, or schema changes. Pure local compute refactor (state-dim correction). T-10-07-01 (bus_id alignment) and T-10-07-02 (G rank deficiency) both mitigated as planned.

## Known Stubs

None.

## Self-Check

- [x] `system1-measurement-source/src/ieee33/ac_model.py` exists and modified
- [x] `system1-measurement-source/src/ieee33/estimate.py` exists and modified
- [x] `system1-measurement-source/src/ieee33/influx.py` exists and modified
- [x] Commit 6ba2b7d exists (Task 1)
- [x] Commit d4f3a44 exists (Task 2)
- [x] `uv run python -m ieee33.ac_model` prints `free state dim=64`; all 3 gates pass
- [x] G = H^T W H is (64,64) rank 64 on well_observed — numerically asserted

## Self-Check: PASSED

## Next Phase Readiness

- Plans 10-08 (injection_sensitivity + predict rewrite) and 10-10 (forecast consumer wiring, WLS end-to-end) now have a correct 64/32 state foundation to build on
- EKF/UKF instantiate at n=64 (N_FREE_STATES flows through from estimate.py to estimator constructors)
- No blockers

---
*Phase: 10-system-2-streaming-distribution-state-estimator-mqtt-fase*
*Completed: 2026-07-01*
