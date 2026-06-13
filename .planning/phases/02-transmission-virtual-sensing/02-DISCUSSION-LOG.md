# Phase 2: Transmission Virtual Sensing - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-13
**Phase:** 2-transmission-virtual-sensing
**Areas discussed:** Hands-on demo, OSED-analog bridge, Aloud-delivery aids, Depth vs breadth

---

## Hands-on demo

| Option | Description | Selected |
|--------|-------------|----------|
| One small demo | ~80-line Python: 3-bus DC power-flow WLS angle estimation + chi-squared bad-data detection; reuses Phase 1 WLS code; backs TVS-02/03; notes lead | ✓ |
| Notes only | No demo; worked numbers inline; fastest, honors all-verbal criteria | |
| You decide | Let Claude pick on cost/benefit | |

**User's choice:** One small demo
**Notes:** Demo focused on TVS-02 (P = Bθ angle WLS) + TVS-03 (chi-squared / normalized-residual bad-data detection) — the most computable, WLS-reusing topics. Notes remain the primary deliverable.

---

## OSED-analog bridge

| Option | Description | Selected |
|--------|-------------|----------|
| Every note, end callout | Each of the 4 notes ends with a boxed "→ Bridge to your work" callout (OSED/HEMS/SI-MAPPER analog as interview pivot) | ✓ |
| Dedicated bridge file | Single cross-cutting BRIDGE note with a table; required callout only in TVS-04 | |
| Both | Per-note callouts + aggregate table | |

**User's choice:** Every note, end callout
**Notes:** Aggregate vocabulary-bridge table is owned by Phase 6 (BRG-01..03); not duplicated here.

---

## Aloud-delivery aids

| Option | Description | Selected |
|--------|-------------|----------|
| Per-note talk-track | Each note carries a tight "<3-min say-aloud version" hitting the criterion's named points | ✓ |
| Pure reference | Reference-only notes; all scripting/timing deferred to Phase 6 | |
| Talk-track + Q&A | Talk-track plus likely interviewer Q&A per note | |

**User's choice:** Per-note talk-track
**Notes:** Full mock-interview rehearsal, question bank, and timing drills stay in Phase 6.

---

## Depth vs breadth

| Option | Description | Selected |
|--------|-------------|----------|
| Deep where named, aware else | Full derivations + worked numbers only for criteria-named concepts; awareness level for DGA, leverage intuition, DLR productization, RUL framing | ✓ |
| Uniformly deep | Full math treatment of every concept | |
| Uniformly conceptual | Key equations only, no derivations/worked numbers anywhere | |

**User's choice:** Deep where named, aware else
**Notes:** Mirrors Phase 1's "depth where it differentiates" principle, respecting the <1-week runway.

---

## Claude's Discretion

- Note granularity defaulted (not asked): one file per requirement in `notes/`, TVS-04 kept as a single well-sectioned file unless it grows unwieldy.
- Section ordering within notes; demo bus topology and numbers; placement (top vs bottom) of the "<3-min say-aloud" track; whether to cheaply extend the demo to touch TVS-01.

## Deferred Ideas

- Aggregate vocabulary-bridge table → Phase 6 (BRG-01..03).
- Full Q&A / mock-interview drills and timing rehearsal → Phase 6.
- Deep PMU / IEC 61850 / C37.118 protocol treatment → Phase 4.
- Federated / multi-substation extension of the demo → Phase 5.
