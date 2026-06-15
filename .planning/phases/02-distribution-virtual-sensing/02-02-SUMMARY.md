---
phase: 02-distribution-virtual-sensing
plan: 02
subsystem: study-notes
tags: [observability, bad-data, chi-squared, normalized-residual, leverage, jacobian-rank, ieee-c57.91, transformer-hot-spot, arrhenius, dga, dlr, rul, virtual-sensing, latex-in-markdown]

requires:
  - phase: 01-kalman-state-estimation
    provides: KAL-01 WLS/χ²/LNR/leverage machinery (TVS-03 specializes its §4) and KAL-03 IEEE 738 worked-example term-table style + DLR demo (TVS-04 parallels)
provides:
  - "TVS-03 note: H-rank observability, chi-squared detection, normalized-residual identification (Ω = R − H G⁻¹ Hᵀ), leverage-measurement blind spot, substation-scale bridge"
  - "TVS-04 note: IEEE C57.91 top-oil/hot-spot ODEs (term tables), Arrhenius aging, virtual-sensing parallel to Phase 1 IEEE 738 EKF, DGA/DLR/RUL awareness, OSED bridge"
affects: [06-synthesis-drills, phase-6-bridge-table, mock-interview-qa]

tech-stack:
  added: []
  patterns:
    - "TVS notes mirror KAL-01 SP-1..SP-6 (For:/Purpose: header, numbered mental-model-first sections, <3-min say-aloud, boxed → Bridge to your work, Quick-Recall Card, Sources line)"
    - "Deep-where-named / awareness-elsewhere depth split (D-08) within a single note"
    - "C57.91 worked-example depth uses KAL-03 term-by-term + parameter tables"

key-files:
  created:
    - .planning/phases/02-distribution-virtual-sensing/notes/TVS-03-observability-bad-data.md
    - .planning/phases/02-distribution-virtual-sensing/notes/TVS-04-asset-health.md
  modified: []

key-decisions:
  - "C57.91 confirm pass (Open Question 1 / Pitfall 4 / A1): the two-cascaded-first-order-rise structure is asserted with confidence; exact exponent/time-constant placement varies between Clause 7 (exponential) and Annex G (detailed) models, so display constants are tagged 'per IEEE C57.91-2011' rather than asserting a possibly-wrong placement"
  - "TVS-03 opens by explicitly specializing KAL-01 §4 to the linear DC case (constant H, one-shot solve) — no WLS re-derivation (Pitfall 1)"
  - "<3-min say-aloud track placed at the bottom of each note (after deep sections, before the bridge), consistent within the phase"

patterns-established:
  - "Pattern: per-note boxed bridge (D-04) with blockquote + comparison table + 'How to say this in the interview' pivot — no aggregate bridge table (deferred to Phase 6, D-05)"
  - "Pattern: χ²-detects / rN-identifies division of labor encoded as an explicit two-row table (Pitfall 3)"

requirements-completed: [TVS-03, TVS-04]

duration: 6min
completed: 2026-06-13
---

# Phase 2 Plan 02: Observability/Bad-Data & Asset-Health Study Notes Summary

**Two equation-dense, say-aloud study notes: TVS-03 (Jacobian-rank observability, χ² detection, normalized-residual identification, the leverage blind spot, with the strongest substation-scale bridge in the phase) and TVS-04 (IEEE C57.91 hot-spot ODE deep, Arrhenius aging, DGA/DLR/RUL aware, parallel to the Phase 1 IEEE 738 EKF).**

## Performance

- **Duration:** ~6 min
- **Started:** 2026-06-13T17:26Z
- **Completed:** 2026-06-13T17:31Z
- **Tasks:** 2
- **Files modified:** 2 (both created)

## Accomplishments
- **TVS-03** delivers the full observability/bad-data machinery: numerical observability via `matrix_rank(H) == n` (topological vs numerical), χ² detection on $J(\hat\theta)=r^\top W r \sim \chi^2(m-n)$, normalized-residual identification with $\Omega = R - H G^{-1}H^\top$ and the ≈3σ threshold, the explicit χ²-detects/rN-identifies division of labor, and the leverage-measurement blind spot at awareness depth.
- **TVS-03 bridge** uses the phase's strongest analog — the CV's "billions of data points across multiple substations" baseline-error analysis IS bad-data detection at scale — rendered as a blockquote + comparison table + interview pivot.
- **TVS-04** covers the criteria-named C57.91 transformer thermal model deeply (top-oil + hot-spot first-order ODEs with KAL-03-style term/parameter tables, $\tau_{TO}\gg\tau_w$), Arrhenius loss-of-life ($A=9.8\times10^{-18}$, $B=15000$, equal-life loading), and the explicit virtual-sensing parallel to the Phase 1 IEEE 738 conductor EKF; DGA/DLR/RUL kept strictly at awareness.
- Both notes carry a `<3-min say-aloud` track, a `→ Bridge to your work` box (D-04), a Quick-Recall Card, and a Sources line — honoring D-04/05/06/07/08/09/10.

## Task Commits

Each task was committed atomically:

1. **Task 1: Write TVS-03 observability + bad-data note** - `044774e` (docs)
2. **Task 2: Write TVS-04 asset-health note** - `37c7b70` (docs)

**Plan metadata:** committed with this SUMMARY (docs)

## Files Created/Modified
- `.planning/phases/02-distribution-virtual-sensing/notes/TVS-03-observability-bad-data.md` - Deep observability/bad-data note (H-rank, χ², rN, leverage, substation bridge)
- `.planning/phases/02-distribution-virtual-sensing/notes/TVS-04-asset-health.md` - Asset-health note (C57.91 hot-spot ODE, Arrhenius, DGA/DLR/RUL awareness, OSED bridge)

## Decisions Made
- **C57.91 confirm pass outcome (rendering choice):** Per RESEARCH Open Question 1 / Pitfall 4 / Assumption A1, the two-cascaded-first-order-rise STRUCTURE (top-oil over ambient, slow $\tau_{TO}$; hot-spot over top-oil, fast $\tau_w$; load drive via $K=I/I_{rated}$ with oil exponent $n$ and winding exponent $m$) is verified and asserted confidently. The exact exponent/constant placement differs between C57.91 Clause 7 (exponential) and Annex G (detailed) models, so all display constants and parameters are tagged "per IEEE C57.91-2011" rather than asserting a single possibly-wrong placement. The Arrhenius aging law ($A=9.8\times10^{-18}$, $B=15000$) is the verified standard value. This is the lowest-risk, interview-defensible rendering for a transformer-savvy interviewer.
- **TVS-03 framed as KAL-01 §4 linear specialization** (constant $H$, one-shot solve) with an explicit no-re-derivation pointer — avoids Pitfall 1 / padding.
- Otherwise followed the plan as specified.

## Deviations from Plan

None - plan executed exactly as written. All equations drawn verbatim from 02-RESEARCH.md §TVS-03 / §TVS-04; structure mirrors KAL-01 (SP-1..SP-6) and KAL-03 (worked-example term tables) per 02-PATTERNS.md.

## Issues Encountered
- The plan's `<automated>` verify command greps for `'\chi^2'` using a single-quoted BRE pattern that does not match `\chi^2` on this grep build (the `^` mid-pattern interaction). Confirmed via `grep -F '\chi^2'` and a correctly-escaped BRE that the file **does** contain the literal `\chi^2` LaTeX — the acceptance criterion ("contains the LaTeX `\chi^2`") is satisfied; only the plan's literal grep string has a quoting quirk. All other tokens for both tasks matched directly. No content change required.

## User Setup Required
None - study notes are plain markdown + LaTeX, no external configuration.

## Next Phase Readiness
- Phase 2 success criteria 3 (observability/bad-data: χ², normalized residuals, leverage, Jacobian-rank) and 4 (asset health: C57.91 hot-spot, DGA, DLR product, RUL) are now covered by deliverable notes.
- Phase 2's third plan (02-03) covers the remaining deliverable — the 3-bus DC power-flow + χ²/rN bad-data NumPy demo (TVS-02/TVS-03 computational backing) — and is unblocked.
- Per-note bridge boxes (TVS-01..04) now feed Phase 6's aggregate vocabulary-bridge table (BRG-01..03) without duplication (D-05).

---
*Phase: 02-distribution-virtual-sensing*
*Completed: 2026-06-13*

## Self-Check: PASSED

- FOUND: notes/TVS-03-observability-bad-data.md
- FOUND: notes/TVS-04-asset-health.md
- FOUND: 02-02-SUMMARY.md
- FOUND commit: 044774e (Task 1 — TVS-03)
- FOUND commit: 37c7b70 (Task 2 — TVS-04)
