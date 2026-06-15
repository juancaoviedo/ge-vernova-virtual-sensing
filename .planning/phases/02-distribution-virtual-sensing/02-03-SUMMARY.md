---
phase: 02-distribution-virtual-sensing
plan: 03
subsystem: demo
tags: [numpy, scipy, matplotlib, wls, state-estimation, dc-powerflow, bad-data-detection, chi-squared]

requires:
  - phase: 01-kalman-state-estimation
    provides: ekf_line_temp_demo.py scaffolding (Agg backend, seed 42, banner console block, script_dir+savefig, chi2.ppf) and KAL-01 WLS/Gauss-Newton machinery
  - phase: 02-distribution-virtual-sensing
    provides: TVS-02 (P=Bθ angle WLS) and TVS-03 (chi-squared + normalized-residual bad-data detection) notes that this demo concretizes
provides:
  - A from-scratch 3-bus DC power-flow WLS state estimator with chi-squared detection and largest-normalized-residual identification
  - A runnable hands-on demo + README + generated figure forming the "I built this state estimator" interview whiteboard story
affects: [phase-06-synthesis-drill, interview-talking-points]

tech-stack:
  added: []
  patterns:
    - "Linear DC WLS as one-shot normal-equations solve (np.linalg.solve(G, HᵀWz)) — the linear collapse of KAL-01's Gauss-Newton"
    - "Detection (chi-squared on J=rᵀWr) vs identification (largest rN, Ω=R−HG⁻¹Hᵀ) as explicit division of labor"

key-files:
  created:
    - .planning/phases/02-distribution-virtual-sensing/demo/dc_powerflow_baddata_demo.py
    - .planning/phases/02-distribution-virtual-sensing/demo/README.md
    - .planning/phases/02-distribution-virtual-sensing/demo/dc_powerflow_baddata.png
  modified: []

key-decisions:
  - "Injected a +15σ gross error (mid-range of the spec's 10-20σ window) — yields a clean rN=13.2 on the suspect, far above the 3σ line"
  - "Kept the demo strictly linear DC (no AC power flow, no pandapower/PYPOWER) per D-02/D-03 to show the WLS math directly"

patterns-established:
  - "Pattern 1: 3-bus DC state estimator demo mirrors Phase 1 demo/ layout exactly (script + README + generated PNG)"
  - "Pattern 2: bad-data flow = solve#1 → χ² flag → rN argmax → remove → solve#2 recovers truth"

requirements-completed: [TVS-02, TVS-03]

duration: 6min
completed: 2026-06-13
---

# Phase 2 Plan 03: 3-Bus DC Power-Flow Bad-Data Detection Demo Summary

**From-scratch NumPy/SciPy 3-bus DC WLS state estimator that injects a 15σ gross error on the line-flow 2→3 measurement, detects it via chi-squared (J=176.7 ≫ 7.815), identifies it via the largest normalized residual (rN=13.2 on measurement 5), removes it, and re-solves to within 7e-4 rad of the true angles.**

## Performance

- **Duration:** ~6 min
- **Started:** 2026-06-13T13:34:00Z
- **Completed:** 2026-06-13T13:37:00Z
- **Tasks:** 2
- **Files modified:** 3 created

## Accomplishments
- A ~210-line (incl. docstrings/plotting) from-scratch DC state estimator implementing the full TVS-02 + TVS-03 flow: B-matrix build, H-matrix sensitivities, one-shot WLS solve, χ² detection, normalized-residual identification, removal, re-solve.
- Script runs to completion (exit 0), prints the χ²/flagged-measurement/re-solved-angles banner readout, and writes the two-panel `dc_powerflow_baddata.png`.
- README mirrors Phase 1's demo/ section order with a real captured console-output block and the interview-value line.
- Numbers confirmed in code: θ_true ≈ [-0.0833, -0.0667] rad (matches RESEARCH §Demo A3); detection and identification both crisp.

## Task Commits

Each task was committed atomically:

1. **Task 1: Write the 3-bus DC power-flow WLS + bad-data detection demo script** - `c317e13` (feat)
2. **Task 2: Run the demo, generate the PNG, and write the demo README** - `34cafa0` (docs)

**Plan metadata:** committed separately with STATE/ROADMAP/REQUIREMENTS updates.

## Files Created/Modified
- `demo/dc_powerflow_baddata_demo.py` - From-scratch 3-bus DC WLS estimator with χ² + normalized-residual bad-data detection (named functions build_B_matrix/build_H/wls_solve/chi2_test/normalized_residuals/run_demo)
- `demo/README.md` - Demo README (What It Demonstrates / Prerequisites / How to Run with real console block / Interview Talking Points / Key Implementation Details / Files)
- `demo/dc_powerflow_baddata.png` - Generated two-panel figure: normalized-residual bar chart (3σ line, flagged bar) + true-vs-estimated angles before/after removal

## Decisions Made
- Injected +15σ (mid-range of the spec's 10-20σ window) for a clean, unambiguous detection result.
- Used a 2x2 reduced B-matrix and explicit H rows derived from susceptance sensitivities, keeping the math visible and from-scratch (no power-flow library), per CONTEXT D-02/D-03.

## Deviations from Plan

None - plan executed exactly as written. Both per-task automated verifications passed on first run; the script detected bad data and recovered the true angles without any adjustment to the measurement matrix, injected-error magnitude, or df.

## Issues Encountered
None. The demo ran correctly on the first execution with the spec's exact 3-bus numbers.

## User Setup Required
None - no external service configuration required. numpy/scipy/matplotlib are already installed.

## Next Phase Readiness
- Phase 2 (transmission-virtual-sensing) is now complete: 4 notes (TVS-01..04) + this hands-on demo.
- The demo gives Juan a concrete "I built a 3-bus state estimator" whiteboard story tying TVS-02 + TVS-03 together and bridging back to the Phase 1 Kalman/WLS work.
- No blockers. Ready for phase transition.

## Self-Check: PASSED

All created files verified present; both task commits (`c317e13`, `34cafa0`) found in git history.

---
*Phase: 02-distribution-virtual-sensing*
*Completed: 2026-06-13*
