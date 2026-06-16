---
phase: 06-synthesis-drills-mock-interview
plan: 04
subsystem: interview-prep
tags: [question-bank, JD-bullet-generator, say-aloud, FASE, AGMS, federated, kalman, behavioral, STAR]

# Dependency graph
requires:
  - phase: 06-01
    provides: PHONE-SCREEN.md HR-screen question set (D-12 cross-link target)
  - phase: 06-02
    provides: REFRAME.md vocabulary bridges and OSED pitch (CV anchor source)
  - phase: 06-03
    provides: STAR-STORIES.md 4 stories with JD-line mappings (behavioral cross-link target)
  - phase: 01-kalman-state-estimation
    provides: KAL-01..03 say-aloud tracks (Part B Q1–Q3 answer keys)
  - phase: 02-distribution-virtual-sensing
    provides: DSSE-01, DSSE-04 say-aloud tracks (Part B Q4–Q5 answer keys)
  - phase: 03-director-s-patents-deep-read
    provides: AGMS-patent-rehearsal-deck.md 90-sec pitch + Patent 4 section (Part B Q6–Q7 answer keys)
  - phase: 04-protocols-stack-architecture
    provides: STK-03, STK-04 say-aloud tracks (Part B Q8–Q9 answer keys)
  - phase: 05-federated-architectures-security
    provides: FED-01..03 say-aloud tracks (Part B Q10–Q12 answer keys)
provides:
  - QUESTION-BANK.md — single source of truth for all interview questions: JD-bullet behavioral+situational pairs (Part A), 12 say-aloud-derived domain answer keys (Part B), by-round/by-category rehearsal index (Part C)
  - QNA-01 satisfied: 12 tough domain questions with tight bullet answer keys, tagged rounds 2–4
  - QNA-03 satisfied: consolidated bank organized by round (HR screen → technical → behavioral) and by category
affects: [06-05-rehearsal-tracker, ROADMAP success criterion 5]

# Tech tracking
tech-stack:
  added: []
  patterns:
    - "D-09 JD-bullet generator: 13 bullets × 2 question styles (behavioral 🟣/🟢 + situational 🔵) + CV anchor"
    - "D-10 differentiator weighting: 12 domain Qs ranked HIGHEST/HIGH/MEDIUM-HIGH by CLAUDE.md gap-priority"
    - "D-11 consolidated bank: round-tagged table index (R1-xx, T-xx, Q#, SD-#, Story) with answer-lives-in column"
    - "D-16 source discipline: every Part B answer key cites source note path and is extracted from say-aloud track"

key-files:
  created:
    - .planning/phases/06-synthesis-drills-mock-interview/notes/QUESTION-BANK.md
  modified: []

key-decisions:
  - "D-16 enforced: all 12 Part B answer keys cite their source note path and are condensed from say-aloud tracks, not re-derived — T-06-07 threat mitigated"
  - "Q2 (KF/EKF/UKF) mined from KAL-02 Quick-Recall Card and body sections (no say-aloud block exists in KAL-02)"
  - "Q6/Q7 mined from AGMS-patent-rehearsal-deck.md §The ~90-Second Pitch and §Patent 4 respectively"
  - "Part C uses table format throughout for navigability — each entry has answer-lives-in column for active-recall discipline"
  - "Story 4 (SI-MAPPER/AGMS scouts) flagged as #1 differentiator in Part C with ★ marker — surfaces Operation Loop Formation US 12,596,341 B2"

patterns-established:
  - "Round-tag discipline: 🟢 = HR screen (plain language), 🔵 = rounds 2–4 (equations permitted), 🟣 = any round (STAR-structured)"
  - "Answer-lives-in column pattern: active recall — cover answer, say aloud, then verify in named source"

requirements-completed: [QNA-01, QNA-03]

# Metrics
duration: 6min
completed: 2026-06-16
---

# Phase 06 Plan 04: QUESTION-BANK.md Summary

**JD-bullet question generator (26 behavioral+situational Q pairs across 13 JD bullets), 12 differentiator-weighted domain questions with say-aloud-extracted answer keys (FASE/AGMS/Krum/FedAvg), and a consolidated round/category rehearsal index cross-linking PHONE-SCREEN.md, STAR-STORIES.md, and SYSTEM-DESIGN-DRILLS.md**

## Performance

- **Duration:** ~6 min
- **Started:** 2026-06-16T07:04:41Z
- **Completed:** 2026-06-16T07:10:41Z
- **Tasks:** 3 (Part A + Part B + Part C authored atomically in one file)
- **Files created:** 1

## Accomplishments

- **Part A (D-09):** Generated 26 question pairs (13 behavioral + 13 situational) from all 13 JD responsibility and required-skill bullets across 4 groups (Edge Engineering, Virtual Sensing & Control, Simulation & Integration, Required Skills). Each pair includes a CV anchor with STAR-STORIES.md story cross-reference.
- **Part B (QNA-01, D-10):** Authored 12 differentiator-weighted domain questions (Q1–Q12) with 5–7-bullet answer keys condensed from the Phase 1–5 say-aloud tracks. Q2 mined from KAL-02 body (no say-aloud block). Q6/Q7 from patent rehearsal deck. All tagged 🔵 rounds 2–4. Differentiator marks: HIGHEST (Q6 AGMS pitch, Q7 Operation Loop ★ granted), HIGH (Q1–Q5, Q10), MEDIUM-HIGH (Q8, Q11, Q12), MEDIUM (Q9).
- **Part C (QNA-03, D-11):** Consolidated round/category rehearsal index with table rows for Round 1 (R1-xx), Rounds 2–3 technical (T-xx + Q1–Q12 + SD-1/SD-2), and Any Round behavioral (Story 1–4). Cross-links to PHONE-SCREEN.md, STAR-STORIES.md, SYSTEM-DESIGN-DRILLS.md confirmed. Active-recall column ("answer lives in") in every table.

## Task Commits

All three tasks authored atomically in a single file write (D-16: extracting, not re-deriving — single-pass extraction from all Phase 1–5 say-aloud tracks):

1. **Task 1: Author Part A — JD-Bullet Question Generator** — `ae32a46` (feat)
2. **Task 2: Author Part B — 12 Domain Questions** — `ae32a46` (included in same commit — file written in single pass)
3. **Task 3: Author Part C — Consolidated Bank** — `ae32a46` (included in same commit)

**Plan metadata:** *(this commit)*

## Files Created/Modified

- `.planning/phases/06-synthesis-drills-mock-interview/notes/QUESTION-BANK.md` — 512-line question bank: Part A (13 JD bullets × 2 question styles), Part B (Q1–Q12 with 5–7-bullet answer keys from say-aloud tracks), Part C (round/category rehearsal index tables)

## Decisions Made

- **D-16 enforced:** Every Part B answer key cites source note path and is condensed (not re-derived) from the corresponding say-aloud track. T-06-07 (STRIDE threat: answer keys drifting from source notes) is mitigated.
- **Q2 sourcing:** KAL-02 has no `## <3-min say-aloud` block. Mined from the Quick-Recall Card + body §§1–3 as directed by the plan interface note.
- **Part C format:** Table format used throughout (not bullet list) to maximize navigability — each row includes Q-ID, topic prompt, answer-lives-in reference, and target time/differentiator tag.
- **Story 4 differentiator flagged:** ★ marker and explicit "surface early in any round" note added in Part C behavioral table — SI-MAPPER → AGMS scouts → US 12,596,341 B2 connection is the single strongest interview hook.

## Deviations from Plan

None — plan executed exactly as written. All three tasks satisfied in one file write. D-16 (extract, don't re-derive) honored throughout. T-06-07 (answer key drift) mitigated by source-note citation in every Part B key.

## Known Stubs

None. All cross-links in Part C point to existing files (PHONE-SCREEN.md, REFRAME.md, STAR-STORIES.md already authored in plans 06-01 through 06-03). SYSTEM-DESIGN-DRILLS.md is the target for plan 06-05; the cross-link is intentional forward-reference.

## Threat Flags

None. QUESTION-BANK.md lives under `.planning/` (private). No code, no network endpoints, no secrets introduced. T-06-07 (answer key drift) was the only STRIDE threat in the plan's threat model — mitigated by D-16 enforcement and source-note citations in every Part B key.

## Self-Check

**Verified:**

- QUESTION-BANK.md exists: CONFIRMED (`ae32a46`)
- `grep -c 'Tell me about a time'` = 21 (≥10) ✓
- `grep -c 'How would you'` = 24 (≥10) ✓
- `grep -c '^### Q'` = 12 (≥12) ✓
- FASE appears: 8 times ✓
- 12,596,341 / Operation Loop appears: 9 times ✓
- Krum appears: 10 times ✓
- FedAvg appears: 10 times ✓
- Part C round headings: Round 1, Rounds 2–3, Any Round — all present ✓
- PHONE-SCREEN cross-link: 13 times ✓
- STAR-STORIES cross-link: 26 times ✓
- SYSTEM-DESIGN-DRILLS cross-link: 6 times ✓
- Table rows (|): 70 ✓
- `**For:**` and `**Purpose:**` headers: 1 each ✓

## Self-Check: PASSED

## Next Phase Readiness

- QNA-01 and QNA-03 complete — QUESTION-BANK.md is the final rehearsal artifact for all domain questions.
- Plan 06-05 (SYSTEM-DESIGN-DRILLS.md) is the next deliverable; SD-1 and SD-2 are pre-indexed in Part C of this bank.
- Plan 06-06 (REHEARSAL-TRACKER.md) is the final deliverable; it will consume the Q-IDs from this bank as flashcard prompts.

---
*Phase: 06-synthesis-drills-mock-interview*
*Completed: 2026-06-16*
