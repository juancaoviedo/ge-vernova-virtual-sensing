---
phase: 05-federated-architectures-security
plan: 03
subsystem: federated-learning
tags: [federated-learning, fedavg, fedprox, krum, byzantine-robustness, numpy, teaching-demo]

# Dependency graph
requires:
  - phase: 05-federated-architectures-security
    provides: FED-01 and FED-02 algorithm-depth notes and FED-03 edge-security note
provides:
  - "NumPy-only FedAvg/FedProx/Krum/coordinate-wise-median teaching demo script (runs clean, exits 0)"
  - "Before/after contrast table showing Byzantine robustness (poison corrupts FedAvg; Krum + median resist it)"
  - "Demo README in Phase 1/2 style with real captured output and 3 interview talking points"
  - "FED-01 + FED-02a 'I ran this from scratch' credibility anchor for interview"
affects: [06-synthesis-drills]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "NumPy-only teaching demo with stdout contrast table (no matplotlib)"
    - "Non-IID 1-D mean estimation as simplest federated learning vehicle"
    - "Phase 1/2 demo structure: module docstring + constants block + named helpers + run_demo() + if __name__"

key-files:
  created:
    - ".planning/phases/05-federated-architectures-security/demo/fedavg_fedprox_krum_demo.py"
    - ".planning/phases/05-federated-architectures-security/demo/README.md"
  modified: []

key-decisions:
  - "FedProx proximal term implemented in fedprox_local_step (client local objective), NOT in fedavg_aggregate — per Li et al. 2020 and RESEARCH Pitfall 2"
  - "Krum vanilla selects ONE honest update (argmin of Krum score); Multi-Krum was not needed for demo clarity"
  - "Coordinate-wise median uses np.median(np.stack(updates), axis=0) — one-liner robust to n/2-1 Byzantine clients"
  - "Demo uses honest honest-bridge talking point 3 verbatim per D-07: 'I haven't run federated learning in production'"
  - "mu=0.5 and poison_magnitude=5.0 produce legible contrast: FedAvg error -0.64, FedProx error +0.006, Krum +0.26, Median +0.04"

patterns-established:
  - "Demo-only from-scratch NumPy: FedAvg, FedProx, Krum, coord-median pattern for interview credibility"
  - "Phase 1/2 README section order applied: What It Demonstrates / Prerequisites / How to Run / Interview Talking Points / Key Implementation Details / Files"

requirements-completed: [FED-01, FED-02]

# Metrics
duration: 10min
completed: 2026-06-14
---

# Phase 5 Plan 03: FedAvg / FedProx / Byzantine Robustness Demo Summary

**NumPy-only FedAvg/FedProx/Krum/coord-median teaching demo with legible before/after contrast table showing plain FedAvg corrupted (error -0.63) while Krum and coordinate-wise median resist a poisoned client (errors +0.26 and +0.04)**

## Performance

- **Duration:** ~10 min
- **Started:** 2026-06-14T10:30:00Z
- **Completed:** 2026-06-14T10:40:54Z
- **Tasks:** 2
- **Files modified:** 2

## Accomplishments

- Self-contained `fedavg_fedprox_krum_demo.py` (215 lines, NumPy-only, seed 42) runs clean and exits 0
- Contrast table clearly shows all four methods: Plain FedAvg corrupted (-0.64 error), FedProx near-optimal (+0.006), Krum selects honest client (+0.26), coordinate-wise median near-optimal (+0.04)
- `README.md` in Phase 1/2 style with real captured console output, 3 talking points including verbatim D-07 honest bridge

## Task Commits

Each task was committed atomically:

1. **Task 1: fedavg_fedprox_krum_demo.py** - `a9b2915` (feat)
2. **Task 2: demo/README.md** - `5d6b8be` (docs)

**Plan metadata:** (this commit)

## Files Created/Modified

- `.planning/phases/05-federated-architectures-security/demo/fedavg_fedprox_krum_demo.py` — Self-contained NumPy demo: generate_clients, local_sgd, fedprox_local_step, fedavg_aggregate, krum_select, coord_median, inject_poison, run_demo
- `.planning/phases/05-federated-architectures-security/demo/README.md` — Phase 1/2 README style: What It Demonstrates, Prerequisites, How to Run (with real captured output), Interview Talking Points (3), Key Implementation Details table, Files

## Decisions Made

- **FedProx proximal term placement:** Implemented in `fedprox_local_step` (client local objective), not in `fedavg_aggregate` — this is the correct placement per Li et al. 2020 and guards against the most common interview pitfall (Pitfall 2 from RESEARCH)
- **Krum returns index, not averaged update:** Vanilla Krum selects ONE update (argmin of Krum score); the demo uses this correctly; Krum selected client 3 (true mean 1.5) — an honest client slightly above the global optimum, which is expected behavior
- **mu=0.5 + poison=5.0 is legible:** First run with these parameters produced a clearly legible contrast; no tuning iterations needed
- **No matplotlib:** stdout contrast table is the talking point; eliminates display dependency; matches CONTEXT D-04 and RESEARCH environment decision

## Deviations from Plan

None — plan executed exactly as written. The script ran successfully on the first attempt with mu=0.5 and poison_magnitude=5.0, producing a legible contrast table without requiring any parameter tuning.

## Issues Encountered

None. Script exits 0, all verification greps pass, contrast table is clearly legible.

## User Setup Required

None — no external service configuration required. NumPy is the only dependency (already installed from Phases 1-2).

## Next Phase Readiness

- FED-01 (FedAvg/FedProx/non-IID) and FED-02a (Byzantine robustness) are now tangible — "I ran this from scratch" credibility anchor is in place
- Phase 6 system-design drills (500-node pipeline, federated aggregator) can draw on the demo directly
- The three talking points (FedProx drift damping, Krum Byzantine rejection, honest bridge) feed Phase 6 BRG/QNA artifacts
- Phase 5 is now complete: 3 notes (FED-01, FED-02, FED-03) + 1 demo (FedAvg/FedProx/Krum)

## Self-Check: PASSED

- [x] `.planning/phases/05-federated-architectures-security/demo/fedavg_fedprox_krum_demo.py` — FOUND
- [x] `.planning/phases/05-federated-architectures-security/demo/README.md` — FOUND
- [x] commit `a9b2915` — FOUND (feat(05-03): add NumPy-only FedAvg/FedProx/Krum/coord-median teaching demo)
- [x] commit `5d6b8be` — FOUND (docs(05-03): add FedAvg/FedProx/Byzantine Robustness demo README)

---
*Phase: 05-federated-architectures-security*
*Completed: 2026-06-14*
