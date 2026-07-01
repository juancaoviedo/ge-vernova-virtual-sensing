---
phase: 10-system-2-streaming-distribution-state-estimator-mqtt-fase
plan: "08"
subsystem: estimator
tags: [ac-model, fase, state-estimation, ieee33, numpy, jacobian, sensitivity, gap-closure]

requires:
  - phase: 10-system-2-streaming-distribution-state-estimator-mqtt-fase (plan 07)
    provides: 64-state (buses 1..32) ac_model/estimate/influx foundation — D-11 convention
provides:
  - injection_sensitivity(x, Ybus) in ac_model — S=∂x/∂p over bus injections, shape (64,64), measurement-count-free (D-10)
  - FASEPredictor.predict(x_prev, S, delta_p, cov_eps) — forecast-driven predict with dimension guard (bug #2 closed)
  - Persistence foil preserved: mode='persistence' sets Δp:=0 behind same interface (D-04)
  - estimate.py updated to new FASEPredictor signature + injection_sensitivity predict path
affects:
  - 10-09 (forecast publisher supplies Δp=[ΔP;ΔQ] over 32 non-slack buses, matching S column order)
  - 10-10 (wires MQTT forecast Δp/Cov(ε) into estimate.py predict call; replaces zero delta_p stub)

tech-stack:
  added: []
  patterns:
    - "injection_sensitivity: J_p=∂[P;Q]/∂[θ;|V|] assembled analytically; inverted to S; block→interleaved reorder"
    - "Δp column contract: [ΔP₁..ΔP₃₂, ΔQ₁..ΔQ₃₂] stacked (length 64 = 2×32 non-slack buses)"
    - "FASEPredictor.predict dimension guard: assert delta_p.shape[0]==S.shape[1] — catches bug #2 structurally"
    - "estimate.py TODO(10-10) marker: zero delta_p stub until forecast stream wired"

key-files:
  created: []
  modified:
    - system1-measurement-source/src/ieee33/ac_model.py
    - system1-measurement-source/src/ieee33/fase_predict.py
    - system1-measurement-source/src/ieee33/estimate.py

key-decisions:
  - "Column contract for Δp: [ΔP₁..ΔP₃₂, ΔQ₁..ΔQ₃₂] stacked (NOT interleaved) — documented in injection_sensitivity docstring as the 10-10 contract"
  - "J_p block layout: rows=[P;Q] stacked, cols=[θ;|V|] stacked (32×32 partitions); reordered rows only (cols already match stacked Δp)"
  - "estimate.py Rule-3 fix: FASEPredictor constructor and predict call updated to new signature; zero delta_p stub until 10-10 wires forecast MQTT"
  - "Old fase_sensitivity retained unchanged (backward compat) — dead for predict path per D-10"

requirements-completed: [R6, R7]

duration: ~30min
completed: 2026-07-01
---

# Phase 10 Plan 08: GAP CLOSURE Summary

**Injection-space sensitivity S=∂x/∂p(64,64) added via power-flow Jacobian inversion; FASEPredictor.predict rewritten to consume Δp/Cov(ε) from caller with dimension guard — bug #2 (S.cols=26 vs delta_p.len=33 matmul crash) structurally impossible**

## Performance

- **Duration:** ~30 min
- **Started:** 2026-07-01
- **Completed:** 2026-07-01T08:47:40Z
- **Tasks:** 2 of 2
- **Files modified:** 3 (ac_model.py, fase_predict.py, estimate.py)

## Accomplishments

- Added `injection_sensitivity(x, Ybus)` to `ac_model.py`: builds J_p = ∂[P;Q]/∂[θ;|V|] analytically over 32 non-slack buses (reusing existing `_p_inj`/`_q_inj` partial-derivative expressions), inverts J_p (pinv fallback for singular case), reorders from block to interleaved layout → S.shape=(64,64). The measurement count never enters this path.
- Documented column contract in the docstring: Δp = [ΔP₁..ΔP₃₂, ΔQ₁..ΔQ₃₂] (stacked, length 64). This is the binding contract for 10-10's Δp assembly.
- Rewrote `FASEPredictor`: removed `prof_df`, `_ar1_prev`, `_p_fcst_prev`, `sigma_frac`, `rho` from `__init__`; new `predict(x_prev, S, delta_p, cov_eps)` with up-front dimension asserts (`delta_p.shape[0]==S.shape[1]` and `cov_eps.shape==(n_inj,n_inj)`); FASE path `x⁻=x_prev+S@delta_p`, `Q=S@cov_eps@S.T+Q_floor`; persistence foil unchanged.
- Fixed `estimate.py` (Rule 3 blocking fix): updated `FASEPredictor` instantiation to drop `prof_df`; updated predict call to use `injection_sensitivity(x_prev, Ybus)` for S + zero delta_p stub until 10-10 wires forecast stream.

## Task Commits

1. **Task 1: Add ac_model.injection_sensitivity — S=∂x/∂p over bus injections (D-10)** — `7cb6bb5` (feat)
2. **Task 2: Rewrite FASEPredictor.predict to consume Δp/Cov(ε) from forecast (D-10/D-04)** — `5e50c3a` (fix)

## Files Created/Modified

- `system1-measurement-source/src/ieee33/ac_model.py` — Added `injection_sensitivity(x, Ybus, ref_vm)` (150 lines): J_p block assembly over 32 non-slack buses, np.linalg.inv with pinv fallback, block→interleaved row reorder, shape+finite assertions; old `fase_sensitivity` untouched
- `system1-measurement-source/src/ieee33/fase_predict.py` — Full rewrite of `FASEPredictor`: dropped prof_df/AR(1) state from `__init__`; new `predict(x_prev, S, delta_p, cov_eps)` with dimension guards; persistence foil unchanged; zero executable `prof_df` references
- `system1-measurement-source/src/ieee33/estimate.py` — Rule-3 fix: `FASEPredictor(cfg, rng, n_bus_est)` (was `(prof_df, cfg, rng, n_bus_est)`); predict loop now calls `injection_sensitivity(x_prev, Ybus)` for S + zero delta_p stub with TODO(10-10) marker

## Decisions Made

- **Column contract**: Δp = [ΔP₁..ΔP₃₂, ΔQ₁..ΔQ₃₂] stacked (length 64). The interleaved alternative was considered but rejected: stacked P/Q blocks align naturally with how J_p partitions are assembled ([P;Q] rows, [θ;|V|] cols) and make slice assignment to J_p sub-matrices simpler. This contract must be followed by 10-10's Δp assembly.
- **estimate.py Rule-3 fix included in this plan**: The broken `FASEPredictor(prof_df, ...)` constructor call was a blocking import error — fixing it here avoids leaving estimate.py non-functional between plans.
- **Zero delta_p stub in estimate.py**: Functional but sub-optimal; the persistence-equivalent prior runs without crashing. 10-10 replaces this with the real forecast Δp from MQTT.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] Fixed estimate.py FASEPredictor constructor and predict call signature**
- **Found during:** Task 2 completion
- **Issue:** `estimate.py` still used `FASEPredictor(prof_df, cfg, rng, n_bus_est)` which fails with TypeError after the Task 2 `__init__` rewrite. The predict call also used `predict(step_k=..., x_prev=..., S=...)` (old 3-arg form).
- **Fix:** Updated constructor to drop `prof_df`; replaced predict call with new 4-arg form using `injection_sensitivity` + zero delta_p stub + TODO(10-10) marker for forecast wiring.
- **Files modified:** `system1-measurement-source/src/ieee33/estimate.py`
- **Commit:** `5e50c3a`

## Verification Results

- `injection_sensitivity(x, Ybus).shape == (64, 64)` — PASS
- `S` is finite (no NaN/Inf at flat-start operating point) — PASS
- `FASEPredictor.predict(S=(64,64), delta_p=(64,), cov_eps=(64,64))` → returns `(64,)`, `(64,64)` — PASS
- Dimension guard: `predict(S=(64,26), delta_p=(33,), ...)` raises AssertionError immediately — PASS
- `grep prof_df src/ieee33/fase_predict.py` → 0 references — PASS
- Mandatory numerical gate: `x_prev + S @ delta_p` with Δp=[0.01×32, 0.005×32] → finite (64,) — PASS
- Persistence foil: mode='persistence' returns `xm == x_prev` and `Q == q_floor * 100.0` — PASS

## Known Stubs

- `estimate.py` predict loop: `delta_p = np.zeros(64)` (zero injection change) — intentional bridge until 10-10 wires the MQTT forecast stream. The estimator still runs (persistence-equivalent prior) but won't anticipate load ramps until the real Δp arrives. Tagged `# TODO(10-10)` in source.

## Threat Surface Scan

No new network endpoints, auth paths, file access patterns, or schema changes. Pure local compute. T-10-08-01 (Δp/S dimension mismatch) mitigated as planned by the `assert delta_p.shape[0] == S.shape[1]` guard in `FASEPredictor.predict`.

## Self-Check

- [x] `system1-measurement-source/src/ieee33/ac_model.py` exists and contains `def injection_sensitivity`
- [x] `system1-measurement-source/src/ieee33/fase_predict.py` exists and contains `def predict` (new 4-arg form)
- [x] `system1-measurement-source/src/ieee33/estimate.py` exists and updated
- [x] `10-08-SUMMARY.md` exists in plan directory
- [x] Commit 7cb6bb5 exists (Task 1: injection_sensitivity)
- [x] Commit 5e50c3a exists (Task 2: FASEPredictor rewrite + estimate.py fix)

## Self-Check: PASSED
