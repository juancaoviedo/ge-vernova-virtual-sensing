---
phase: 03-director-s-patents-deep-read
plan: 01
subsystem: interview-prep / patent-rehearsal
tags: [patents, AGMS, rehearsal-deck, editorial]
dependency_graph:
  requires:
    - .planning/research/patents/INDEX.md
    - .planning/research/patents/adaptive-power.md
    - .planning/research/patents/logistician-module.md
    - .planning/research/patents/asset-portfolio.md
    - .planning/research/patents/operation-loop.md
    - .planning/research/patents/scout-command.md
    - .planning/research/patents/data-management.md
  provides:
    - .planning/phases/03-director-s-patents-deep-read/notes/AGMS-patent-rehearsal-deck.md
  affects:
    - Phase 6 (synthesis/drill) — deck is the raw material for BRG-01..03 vocabulary bridge and OSED pitch
tech_stack:
  added: []
  patterns:
    - Oral-rehearsal performance layer distinct from reference layer
    - Pipeline-order (assembly line) as mnemonic structure for six-patent family
    - Three-level deliverable per patent: summary (spoken track) + connection + director question
key_files:
  created:
    - .planning/phases/03-director-s-patents-deep-read/notes/AGMS-patent-rehearsal-deck.md
  modified: []
decisions:
  - D-03 honored: one consolidated deck, no per-patent files
  - D-04 honored: INDEX.md and AGMS-architecture.md untouched
  - D-05 honored: pipeline order Parent → Logistician → Asset Portfolio → Operation Loop ★ → Scout Command → Data Management
  - D-09 honored: all questions are architecture-level; no claim-number quoting in questions (claim 3 named only in Patent 4 My Connection, which is allowed)
  - Distinctness rule applied: CVXPY/MPC as primary connection only in Operation Loop section
metrics:
  duration_minutes: 12
  completed: 2026-06-13
  tasks_completed: 1
  files_created: 1
---

# Phase 3 Plan 1: AGMS Patent Rehearsal Deck Summary

**One-liner:** Single consolidated oral-rehearsal deck distilling six AGMS patents into spoken
summaries, distinct OSED/HEMS/SI-MAPPER connections, and architecture-level director questions
— ordered as the formation assembly line with US 12,596,341 B2 (Operation Loop Formation,
GRANTED, GE Vernova) flagged as the keystone.

---

## What Was Built

One markdown study document at:
`.planning/phases/03-director-s-patents-deep-read/notes/AGMS-patent-rehearsal-deck.md`

The deck contains:

- `## The Assembly Line at a Glance` — pipeline mnemonic in formation order with one-liner owners
- `## The ~90-Second Pitch` — whole-family spoken narrative derived from INDEX.md master narrative
- Six `## Patent N:` sections in pipeline order, each with:
  - `### Summary` — 2-3 sentence spoken track (PAT-01)
  - `### My Connection` — one distinct first-person connection to OSED/HEMS/SI-MAPPER work (PAT-02)
  - `### Question for the Director` — architecture-level blockquoted question (PAT-03)
- `## Closing: The Master Narrative` — the unified "one assembly line = my stack" spoken block
- `## Quick-Reference Cheat Sheet` — 8-term glossary condensed from INDEX.md

**Total length:** 316 lines (well above the 120-line minimum).

---

## Acceptance Criteria Results

All automated grep checks PASS:

| Check | Result |
|-------|--------|
| File exists | PASS |
| Exactly 6 `## Patent N:` headings | PASS (6) |
| Pipeline order (Parent → Logistician → Asset Portfolio → Operation Loop → Scout → Data) | PASS |
| 6 `### Summary` blocks | PASS |
| 6 `### My Connection` blocks | PASS |
| 6 `### Question for the Director` blocks | PASS |
| `12,596,341` present | PASS |
| `GRANTED` present | PASS |
| `★` marker present | PASS |
| `## The ~90-Second Pitch` heading present | PASS |
| `Master Narrative` heading present | PASS |
| `assembly line` phrase present | PASS |
| INDEX.md and AGMS-architecture.md unmodified | PASS (git status --porcelain empty) |
| Only one file in notes/ | PASS |
| CVXPY as primary in at most Operation Loop connection | PASS |

---

## Deviations from Plan

None — plan executed exactly as written.

All source material lifted and refined from the six per-patent files and INDEX.md. No new
research invented. No per-patent deck files created. Reference docs (INDEX.md,
AGMS-architecture.md) untouched.

---

## Commits

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Author consolidated AGMS patent rehearsal deck | 4ff34e4 | `.planning/phases/03-director-s-patents-deep-read/notes/AGMS-patent-rehearsal-deck.md` |

---

## Threat Flags

None — this deliverable is a static internal markdown study document with no runtime, network
surface, user input, or secrets.

## Self-Check: PASSED

- File exists: CONFIRMED `.planning/phases/03-director-s-patents-deep-read/notes/AGMS-patent-rehearsal-deck.md`
- Commit 4ff34e4 exists: CONFIRMED
- All automated verify checks: PASS
- Reference docs INDEX.md, AGMS-architecture.md: unmodified (empty git status --porcelain)
