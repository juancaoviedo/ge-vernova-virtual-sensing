---
phase: 01-kalman-state-estimation
plan: 01
subsystem: study-notes
tags: [kalman, wls, state-estimation, interview-prep, grid]
dependency_graph:
  requires: [01-RESEARCH.md]
  provides: [KAL-01-wls-state-estimation.md, KAL-02-kalman-family-kf-ekf-ukf.md]
  affects: [01-02-PLAN.md, 01-03-PLAN.md]
tech_stack:
  added: []
  patterns: [oral-rehearsal-notes, mental-model-first, quick-recall-card]
key_files:
  created:
    - .planning/phases/01-kalman-state-estimation/notes/KAL-01-wls-state-estimation.md
    - .planning/phases/01-kalman-state-estimation/notes/KAL-02-kalman-family-kf-ekf-ukf.md
  modified: []
decisions:
  - "Drew equations verbatim from 01-RESEARCH.md (verified sources) rather than re-deriving"
  - "Added explicit greppable tag in KAL-01 (WLS convex) for link-verification"
  - "KAL-02 organized as linear KF -> EKF -> UKF progression with decision table before Q/R section for natural study flow"
metrics:
  duration_minutes: 18
  completed_date: "2026-06-13"
  tasks_completed: 2
  files_created: 2
---

# Phase 01 Plan 01: WLS / Gauss-Newton and Kalman Family Study Notes Summary

**One-liner:** WLS state estimation notes (observability, residuals, chi-squared bad-data, leverage measurement trap, OSED convex bridge) and KF/EKF/UKF notes (full predict-update equations, Jacobians, sigma points, EKF-vs-UKF decision table, Q/R tuning, NIS divergence detection).

---

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Write KAL-01 WLS / Gauss-Newton notes | 50c37f4 | .planning/phases/01-kalman-state-estimation/notes/KAL-01-wls-state-estimation.md |
| 2 | Write KAL-02 Kalman family (KF/EKF/UKF) notes | 7f681bb | .planning/phases/01-kalman-state-estimation/notes/KAL-02-kalman-family-kf-ekf-ukf.md |

---

## What Was Built

### KAL-01: WLS / Gauss-Newton Power-System State Estimation

A plain-English study note structured for oral rehearsal. Covers:

1. Mental model: state vector x = [V, θ] per bus; measurement model z = h(x) + e; WLS as
   "best consistent picture from noisy, redundant sensor soup"
2. WLS objective J(x) = [z−h(x)]ᵀ W [z−h(x)] with W = R⁻¹ and weight-from-trust intuition
3. Gauss-Newton in four steps (linearize H, form gain G = HᵀWH, compute Δx = G⁻¹HᵀW[z−h(x̂)],
   iterate until ‖Δx‖ < tol), with note that 2–4 iterations is typical
4. Interview vocabulary: observability (H full column rank), residuals, chi-squared bad-data
   test (J(x̂) ~ χ²(m−n)), LNR test, and the critical leverage measurement limitation
5. Static vs. dynamic SE bridge to KAL-02
6. Explicit OSED convex optimization bridge with structural isomorphism table and interview
   script to deliver it naturally

### KAL-02: Kalman Filter Family (KF, EKF, UKF)

A mathematically precise progression. Covers:

1. Linear KF: state-space model, Predict (x̂_{k|k-1}, P_{k|k-1}=FPFᵀ+Q), Update
   (innovation y, S=HPHᵀ+R, gain K=PHᵀS⁻¹, updated x̂ and P), Kalman gain intuition
2. EKF: nonlinear f and h; Predict via f(x̂) and process Jacobian A=∂f/∂x; Update via
   measurement Jacobian H=∂h/∂x; full equation block; three EKF failure modes
3. UKF: sigma-point generation (2n+1 points, λ=α²(n+κ)−n), alpha/beta/kappa parameter
   meanings, Predict via weighted sigma propagation through f, Update via cross-covariance
   Pxz; note that no Jacobian is needed anywhere
4. EKF-vs-UKF decision table (approach, accuracy, Jacobian, compute, grid use case, failure)
   and three-way decision narrative (EKF / UKF / particle filter)
5. Q/R tuning (Q=0 trap, initialization from physics priors), innovation sequence properties,
   NIS chi-squared divergence detection, Sage-Husa adaptive tuning at awareness level

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Equations verbatim from 01-RESEARCH.md | Research phase already verified equations against Edinburgh CVonline, filterpy docs, and arXiv papers; re-deriving would risk transcription errors |
| Mental-model-first structure | Plan directive; notes intended for oral rehearsal, not reading |
| KAL-02 decision table placed before Q/R section | Interviewers probe EKF-vs-UKF judgment before diving into tuning; table first gives the answer before the supporting detail |
| Quick-recall card at end of each note | Interview environment: need 30-second verbal summary available without re-reading the full note |

---

## Deviations from Plan

None — plan executed exactly as written. All six elements of KAL-01 and all five elements
of KAL-02 are covered in full.

---

## Known Stubs

None. Both notes are complete with all required content. No placeholders or TODOs.

---

## Threat Flags

N/A — static markdown study notes. No software, no network surface, no untrusted input.

---

## Self-Check: PASSED

Files exist:
- FOUND: .planning/phases/01-kalman-state-estimation/notes/KAL-01-wls-state-estimation.md
- FOUND: .planning/phases/01-kalman-state-estimation/notes/KAL-02-kalman-family-kf-ekf-ukf.md

Commits exist:
- FOUND: 50c37f4 — feat(01-01): write KAL-01 WLS / Gauss-Newton state estimation study notes
- FOUND: 7f681bb — feat(01-01): write KAL-02 Kalman family (KF/EKF/UKF) study notes

Acceptance criteria:
- KAL-01: contains "Gauss-Newton" (yes), "leverage" (yes), "WLS" and "convex" (yes)
- KAL-02: contains "sigma point" (yes), "Jacobian" (yes), "innovation" (yes)
- KAL-01 OSED bridge present (yes)
- KAL-02 EKF/UKF decision table present (yes)
