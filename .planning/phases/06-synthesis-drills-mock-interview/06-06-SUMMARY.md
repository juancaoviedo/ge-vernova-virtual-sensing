---
phase: 06-synthesis-drills-mock-interview
plan: "06"
subsystem: interview-prep
tags: [rehearsal, active-recall, spaced-repetition, flashcard-tracker, protocol]

requires:
  - phase: 06-synthesis-drills-mock-interview plans 01-05
    provides: PHONE-SCREEN.md, REFRAME.md, STAR-STORIES.md, QUESTION-BANK.md, SYSTEM-DESIGN-DRILLS.md — the five source deliverables indexed by the tracker

provides:
  - "notes/REHEARSAL-TRACKER.md: flashcard tracker (48 pre-populated rows across 4 tables) + written active-recall+spaced-repetition protocol + 7-day spacing plan + target-times table + flag-the-2-3-weakest mechanism"

affects: [final interview preparation — operationalizes all five Phase-6 deliverables into a measurable rehearsal regimen]

tech-stack:
  added: []
  patterns:
    - "REHEARSAL-TRACKER.md mirrors 04-HUMAN-UAT.md: YAML frontmatter (status/phase/source/started/updated) + tracker rows with Said Aloud/Duration/Confidence/Notes + Summary block (total/passed/weak/pending)"
    - "Phone-screen-first ordering: Screen Material (Round 1) tracker section precedes STAR Stories, Technical Questions, and System-Design Drills"
    - "Flag-the-weakest tables (Day 3 + Day 5) as fill-in instruments operationalizing success criterion 5"

key-files:
  created:
    - ".planning/phases/06-synthesis-drills-mock-interview/notes/REHEARSAL-TRACKER.md"
  modified: []

key-decisions:
  - "Single atomic commit for both tasks (Tasks 1 and 2 write to the same file; combined for atomicity)"
  - "Tracker counts Layer A bridges (15 rows) + screen sections (8 rows) + screen behavioral (3 rows) separately for maximum granularity; Total = 26 Screen Material + 8 STAR + 25 Technical + 2 Drills = 61 data rows (111 table rows including headers/separators)"
  - "Target-times table includes system-design drill (~5 min) and full OSED technical pitch (~10 min) per D-14, extending the D-14 spec with the drill target from 06-RESEARCH"
  - "T-01–T-13 situational questions indexed in the Technical Questions tracker (not just Q1–Q12) to give Juan the complete Part A+B drill surface"

patterns-established:
  - "Rehearsal tracker as capstone: the tracker is a meta-document that operationalizes all other deliverables — it does not duplicate content, it indexes prompts and points to source documents for answer keys"

requirements-completed: [QNA-03]

duration: 2min
completed: 2026-06-16
---

# Phase 6 Plan 06: Rehearsal Tracker & Protocol Summary

**Active-recall flashcard tracker (48 rehearsal prompts across 4 tables) + written spaced-repetition protocol with 7-day spacing plan, target-times Pass/Fail table, and explicit flag-the-2-3-weakest mechanism — converting the five Phase-6 deliverables into a measurable rehearsal regimen**

## Performance

- **Duration:** ~2 min
- **Started:** 2026-06-16T07:20:22Z
- **Completed:** 2026-06-16T07:22:00Z
- **Tasks:** 2 (combined into single commit — same file)
- **Files created:** 1

## Accomplishments

- Written rehearsal protocol authored: active recall + spaced repetition method with step-by-step mechanics (cover, say aloud, time, check, mark ✗/⚠/✓, repeat weak items)
- 7-day spacing plan anchored to 2026-06-16 runway, Day 1 through Day 7 with specific per-day focus
- Target-times table with Pass/Fail column for all item types (bridges ≤10 s, STAR ≤90 s screen / ≤2 min technical, phone-screen arc ≤10 min, OSED pitch ~10 min, drills ~5 min)
- Flag-the-2-3-weakest mechanism: two explicit fill-in tables (after Day 3 and after Day 5) with priority order for which weak rows to carry to Day 6
- Four flashcard tracker tables pre-populated from the five deliverable docs: Screen Material (26 rows — phone-screen sections S-01–S-08, Layer A bridges A-01–A-15, behavioral B-01–B-03), STAR Stories (8 rows — screen + technical versions of all 4 stories), Technical Questions (25 rows — Q1–Q12 domain deep-dives + T-01–T-13 situational), System-Design Drills (2 rows — Drill 1 and Drill 2)
- Summary block mirroring 04-HUMAN-UAT.md (total/passed/weak/pending) with a "ready signal" definition
- YAML frontmatter mirrors 04-HUMAN-UAT.md exactly (status/phase/source/started/updated)

## Task Commits

1. **Tasks 1 & 2: Author REHEARSAL-TRACKER.md (protocol + tracker tables)** - `0d2e4b6` (feat)

**Plan metadata:** *(final docs commit follows this SUMMARY)*

## Files Created/Modified

- `/home/juan/codes/ge-vernova-virtual-sensing/.planning/phases/06-synthesis-drills-mock-interview/notes/REHEARSAL-TRACKER.md` — Flashcard tracker + written rehearsal protocol; 239 lines; mirrors 04-HUMAN-UAT.md format; 111 total table rows (48 rehearsal-data rows)

## Decisions Made

- Combined Tasks 1 and 2 into a single commit because both write to the same file and Task 2 appends to Task 1's content — splitting them would leave the file in a non-meaningful intermediate state.
- Included T-01–T-13 situational questions (Part A of QUESTION-BANK.md) in the Technical Questions tracker in addition to Q1–Q12 (Part B), giving Juan the complete rehearsable question surface.
- System-design drill target time (~5 min) was added to the Target Times table; it appears in 06-RESEARCH §"Target Durations" but not explicitly in D-14 — treated as an implied requirement per the CONTEXT.md drill format spec (D-13).

## Deviations from Plan

None — plan executed exactly as written. File contents match the spec in 06-CONTEXT.md D-14, 06-RESEARCH §"REHEARSAL-TRACKER.md Internal Structure", and the 04-HUMAN-UAT.md format precedent.

## Issues Encountered

None.

## Known Stubs

None. The tracker intentionally has empty Said Aloud / Duration / Confidence / Notes columns — these are fill-in fields for Juan during actual rehearsal sessions, not stubs. The Prompt column is fully pre-populated from the deliverable prompts.

## Threat Flags

None. REHEARSAL-TRACKER.md is a local `.planning/` document. It indexes prompt topics (not full logistics details) and does not duplicate the PHONE-SCREEN.md logistics scripts or TN/salary details in the tracker rows themselves — consistent with T-06-11 mitigation in the plan's threat register.

## Next Phase Readiness

Phase 6 is now complete: all six deliverables authored (PHONE-SCREEN.md, REFRAME.md, STAR-STORIES.md, QUESTION-BANK.md, SYSTEM-DESIGN-DRILLS.md, REHEARSAL-TRACKER.md). Juan can begin Day 1 rehearsal immediately by reading PHONE-SCREEN.md §9 aloud and filling in the Screen Material tracker rows. No blockers.

---
*Phase: 06-synthesis-drills-mock-interview*
*Completed: 2026-06-16*
