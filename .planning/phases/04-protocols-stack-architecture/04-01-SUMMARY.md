---
phase: 04-protocols-stack-architecture
plan: "01"
subsystem: study-notes
tags: [grid-protocols, iec-61850, dnp3, pmu, scada, lora, mqtt, interview-prep]
dependency_graph:
  requires: []
  provides:
    - STK-01-protocol-stack.md (six-protocol tier map with per-protocol property + transport)
    - STK-02-iec-61850.md (GOOSE/SV/MMS roles, three-tier hierarchy, five named logical nodes)
  affects:
    - Phase 6 bridge table (BRG-01..03) — per-note bridge callouts are the raw material
    - Phase 6 Q&A drills (QNA) — protocol stack vocabulary feeds system-design drills
tech_stack:
  added: []
  patterns:
    - "For:/Purpose: oral-rehearsal header (Phase 2 TVS convention)"
    - "Numbered mental-model-first sections"
    - "<3-min say-aloud blockquote track"
    - "Boxed → Bridge to your work callout (comparison table + interview pivot)"
    - "Quick-Recall Card numbered list"
key_files:
  created:
    - .planning/phases/04-protocols-stack-architecture/notes/STK-01-protocol-stack.md
    - .planning/phases/04-protocols-stack-architecture/notes/STK-02-iec-61850.md
  modified: []
decisions:
  - "All IEC 61850 logical-node facts drawn verbatim from 04-RESEARCH.md (verified against IEC TR 61850-10-3:2022 PDF + scadaprotocols.com)"
  - "STK-01 uses two bridges (Modbus→DNP3 + Zigbee→LoRa) per CONTEXT.md D-08 and PLAN task spec"
  - "STK-02 bridge frames MQTT pub/sub → GOOSE publish/multicast (same instinct, Layer-2 determinism is the delta)"
  - "Pitfall 6 guard added to STK-02 section 5: IEC 61850 three-tier vs STK-05 four-tier explicitly labelled"
  - "No SCL/CID config files covered (CLAUDE.md 'What NOT to Over-Invest In' exclusion)"
  - "No LaTeX used (no formula genuinely helps these protocol facts; prose + tables suffice per D-10)"
metrics:
  duration_minutes: 3
  completed_date: "2026-06-14"
  tasks_completed: 2
  files_created: 2
---

# Phase 4 Plan 1: Grid Protocol Stack Notes Summary

**One-liner:** Two oral-rehearsal study notes — STK-01 places six grid protocols in the correct
field-to-cloud tier with one key property each; STK-02 delivers IEC 61850 internals including
five named logical nodes (XCBR/MMXU/CSWI/PTOC/PDIS) with the GOOSE/SV/MMS Layer-2-vs-routable
split and the CSWI→XCBR→GOOSE command flow.

---

## What Was Built

### STK-01: Grid Protocol Stack — Field-to-Cloud Tier Map

`notes/STK-01-protocol-stack.md` — interview-ready six-protocol tier map:

- **Section 1:** Mental model — protocols exist because tiers have fundamentally different
  constraints (sub-4 ms protection vs. km-range battery sensing vs. cloud supervisory).
- **Section 2:** Six-row tier map table (SCADA+OPC-UA / DNP3 / PMU-C37.118 / IEC 61850 / LoRa / MQTT)
  with Field-to-Cloud Tier | One Key Property | Transport for each.
- **Section 3:** IEEE C37.118 reporting-rate detail — 10/30/60 fps baseline for 60 Hz, 120 fps for
  WAMS, GPS timestamp on every frame enabling cross-system phase comparison.
- **Section 4:** DNP3 vs. Modbus distinction table — timestamps + unsolicited push + three-layer
  architecture + DNP3 SAv5 vs. poll-only two-layer no-timestamp Modbus.
- **<3-min say-aloud:** Tier walk bottom-to-top (process-level GOOSE/SV → DNP3 telemetry → PMU
  phasors → LoRa battery sensors → MQTT edge broker → SCADA control center).
- **Bridge callouts:** Modbus→DNP3 ("timestamps + push") and Zigbee→LoRa ("km-range battery,
  star-of-stars") with interview pivot sentences.
- **Quick-Recall Card:** Nine numbered items covering all six protocols plus the bridge.

### STK-02: IEC 61850 — GOOSE / SV / MMS, Hierarchy & Logical Nodes

`notes/STK-02-iec-61850.md` — highest-yield gap-fill note for criterion 2:

- **Section 1:** Three-tier substation hierarchy table (process/bay/station) with components and
  primary IEC 61850 services per tier; verbatim interview one-liner.
- **Section 2:** GOOSE/SV/MMS roles table (Layer | Latency | Direction | Use Case); key structural
  fact verbatim (Layer-2 never leaves LAN vs. TCP/IP routable); GOOSE retransmission mechanism.
- **Section 3:** Five named logical nodes (XCBR/MMXU/CSWI/PTOC/PDIS) with group letter + full name
  + interview one-liner per node; four-letter rule; bonus nodes LLN0/LPHD/TCTR/TVTR; 13 LN
  functional groups at awareness level.
- **Section 4:** CSWI→XCBR→GOOSE command flow verbatim.
- **Section 5:** Pitfall guard — IEC 61850 three-tier substation hierarchy vs. STK-05 four-tier
  field/edge/fog/cloud system architecture.
- **<3-min say-aloud:** Three-tier walk + GOOSE/SV/MMS with Layer-2 call-out + all five LN names
  with one-liner each + command flow.
- **Bridge:** MQTT pub/sub → GOOSE publish/multicast (instinct shared; GOOSE is Layer-2 deterministic
  protection where MQTT is application-tier QoS; MMS = the routable supervisor I'd integrate).
- **Quick-Recall Card:** 13 numbered items covering all five LNs, GOOSE/SV/MMS triplet, Layer-2
  vs. routable distinction, command flow, pitfall guard, and bridge.

---

## Commits

| Task | Commit | Files |
|------|--------|-------|
| Task 1 — STK-01 tier map note | c84aa5e | notes/STK-01-protocol-stack.md (created) |
| Task 2 — STK-02 IEC 61850 note | e701327 | notes/STK-02-iec-61850.md (created) |

---

## Deviations from Plan

None — plan executed exactly as written. Both notes mirror the TVS-04-asset-health.md style
(For:/Purpose: header, numbered mental-model-first sections, `<3-min say-aloud` track, boxed
bridge callout, Quick-Recall Card, Sources line). All facts drawn verbatim from 04-RESEARCH.md
per D-01. No LaTeX used (no formula genuinely helps these protocol facts per D-10). SCL/CID
not covered per CLAUDE.md "What NOT to Over-Invest In".

---

## Known Stubs

None. Both notes are fully wired to their content source (04-RESEARCH.md facts + CLAUDE.md
Category 3 tables). No placeholder text or TODO items. No data sources deferred.

---

## Threat Flags

Not applicable — documentation-only plan producing static markdown study notes. No runtime,
network-facing, or executable artifacts produced.

---

## Self-Check: PASSED

Files exist:
- FOUND: .planning/phases/04-protocols-stack-architecture/notes/STK-01-protocol-stack.md
- FOUND: .planning/phases/04-protocols-stack-architecture/notes/STK-02-iec-61850.md

Commits exist:
- FOUND: c84aa5e — feat(04-01): write STK-01 grid protocol stack tier-map note
- FOUND: e701327 — feat(04-01): write STK-02 IEC 61850 deep note (GOOSE/SV/MMS, logical nodes)

Greppable tokens confirmed:
- STK-01: C37.118, DNP3, LoRa, GOOSE, Bridge to your work, say-aloud, For:, Purpose: — all present
- STK-02: XCBR, MMXU, CSWI, GOOSE, MMS, Sampled Values, <4 ms, Bridge to your work, say-aloud — all present
