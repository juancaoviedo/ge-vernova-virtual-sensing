---
phase: 05-federated-architectures-security
plan: 01
subsystem: study-notes
tags: [federated-learning, FedAvg, FedProx, Byzantine-robustness, Krum, coordinate-wise-median, non-IID, gossip, aggregation]

# Dependency graph
requires:
  - phase: 04-protocols-stack-architecture
    provides: STK-05 four-tier reference architecture with fog/federated tier (cross-linked from both notes)
  - phase: 03-agms-patents
    provides: Operation Loop simulate-before-commit and Scout Command federated decisioning (AGMS tie in FED-01 and FED-02)
provides:
  - FED-01: explain-why note on federated vs distributed, FedAvg weighted-average aggregation, FedProx proximal term, non-IID client drift
  - FED-02: explain-why note on Byzantine robustness (Krum, coordinate-wise median), gradient poisoning detection, gossip-vs-central tradeoff
affects: [phase-06-bridges-and-qa, BRG-01, QNA-01]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - FedAvg weighted-average update rule (weighted by client sample count)
    - FedProx proximal term in client local objective to tether non-IID drift
    - Krum nearest-neighbor scoring for Byzantine-robust update selection
    - Coordinate-wise median for per-dimension outlier rejection

key-files:
  created:
    - .planning/phases/05-federated-architectures-security/notes/FED-01-federated-vs-distributed.md
    - .planning/phases/05-federated-architectures-security/notes/FED-02-byzantine-robustness.md
  modified: []

key-decisions:
  - "Proximal term in FedProx lives in the client local objective, NOT server aggregation (Pitfall 2) — explicitly stated in FED-01"
  - "Vanilla Krum selects ONE update (argmin); Multi-Krum averages m — explicit distinction per Pitfall 3 in FED-02"
  - "Honest bridge framing: OSED distributed edge inference cited as closest analog; no false claim of production FL (Pitfall 6 / D-07)"
  - "AGMS ties kept short (1-2 sentence callout boxes) — cross-reference Phase 3/4, not re-derive"
  - "STK-05 fog/federated tier explicitly closed: FED-01 and FED-02 supply the algorithm depth Phase 4 noted at awareness level"

patterns-established:
  - "FED notes follow TVS-04 structural template: For:/Purpose: header, Depth-strategy blockquote, numbered sections, <3-min say-aloud, bridge callout, Quick-Recall Card, Sources footer"
  - "AGMS tie appears as block-quoted callout section (same pattern as bridge callout, pointing to Phase 3/4 instead of CV)"
  - "gossip-vs-central decision table follows KAL-02 EKF/UKF table pattern with greppable HTML comment tag"

requirements-completed: [FED-01, FED-02]

# Metrics
duration: 3min
completed: 2026-06-14
---

# Phase 05 Plan 01: Federated Architectures & Security — Algorithm-Depth Notes Summary

**Two oral-rehearsal-ready explain-why notes covering FedAvg weighted averaging, FedProx proximal-term non-IID fix, Krum nearest-neighbor Byzantine rejection, and coordinate-wise median — all anchored to substation load profiles and the STK-05 fog/federated tier**

## Performance

- **Duration:** 3 min
- **Started:** 2026-06-14T10:28:22Z
- **Completed:** 2026-06-14T10:31:16Z
- **Tasks:** 2
- **Files created:** 2

## Accomplishments

- FED-01 note covers the federated-vs-distributed crisp distinction (three-clause test, Spark/MapReduce gotcha), FedAvg two-nested-loop structure with weighted-average LaTeX, and FedProx proximal term with explicit statement that it lives in the client local objective (not server aggregation — Pitfall 2 honored), plus verbatim non-IID substation framing from RESEARCH §3.
- FED-02 note covers Byzantine threat mechanics (sign-flipped gradient), Krum score formula with `\arg\min` selection and explicit vanilla-vs-Multi-Krum distinction (Pitfall 3 honored), coordinate-wise median formula with its gradient-correlation limitation (Pitfall 4 honored), and a 7-row gossip-vs-central decision table with greppable HTML comment tag.
- Both notes carry STK-05 cross-links, AGMS tie callouts (Operation Loop + Scout Command in FED-01; fog-tier aggregation in FED-02), honest bridge callouts per D-07 framing, `<3-min say-aloud` tracks, Quick-Recall Cards with inline LaTeX, and Sources footers — exactly matching the TVS-04 / KAL-02 structural templates.

## Task Commits

Each task was committed atomically:

1. **Task 1: FED-01-federated-vs-distributed.md** — `5aafe4c` (feat)
2. **Task 2: FED-02-byzantine-robustness.md** — `b6a13ff` (feat)

**Plan metadata:** (this commit — docs)

## Files Created/Modified

- `.planning/phases/05-federated-architectures-security/notes/FED-01-federated-vs-distributed.md` — 122 lines; federated-vs-distributed, FedAvg, FedProx, non-IID; section structure per TVS-04
- `.planning/phases/05-federated-architectures-security/notes/FED-02-byzantine-robustness.md` — 130 lines; Krum, coordinate-wise median, gossip-vs-central; section structure per KAL-02

## Decisions Made

- Proximal term in FedProx explicitly placed in client local objective (not server aggregation) per RESEARCH Pitfall 2 — this is the most common interview-trap mistake.
- Vanilla Krum described as argmin selection of ONE update; Multi-Krum clearly distinguished as the averaging variant per RESEARCH Pitfall 3.
- Honest bridge framing strictly observed: "I haven't run federated learning in production" verbatim from D-07 / RESEARCH Pitfall 6.
- AGMS ties kept as short callout boxes (1-2 sentences + cross-link) per D-06 "cross-reference, don't re-derive."
- D-11 guardrail confirmed: no aggregate vocabulary-bridge table and no timed Q&A loop appear in either note.

## Deviations from Plan

None — plan executed exactly as written. Both notes match acceptance criteria, LaTeX formula strings match exactly, structural template follows TVS-04 / KAL-02 analogs, and all automated verification checks pass.

## Issues Encountered

None. The `notes/` directory did not exist yet and was created before writing (expected first-file setup).

## Known Stubs

None. Both notes are complete oral-rehearsal artifacts with no placeholder content.

## Threat Flags

None. Static study notes; no network exposure, no secrets, no executable attack surface (per plan threat model).

## Next Phase Readiness

- FED-01 and FED-02 are ready to feed Phase 5 Plan 02 (FED-03 edge security note and demo).
- Both notes provide the `<3-min say-aloud` tracks and `→ Bridge to your work` callouts that Phase 6 (BRG/QNA) lifts directly for the aggregate vocabulary-bridge table and system-design drills.
- STK-05 fog/federated tier is now closed at explain-why depth (Phase 4 left it at awareness level).

---
*Phase: 05-federated-architectures-security*
*Completed: 2026-06-14*
