---
phase: 04-protocols-stack-architecture
plan: "03"
subsystem: study-notes
tags: [architecture, whiteboard, four-tier, agms-overlay, iec-61850, k3s, nats, iekf, prometheus]
dependency_graph:
  requires:
    - .planning/phases/04-protocols-stack-architecture/04-RESEARCH.md
    - .planning/research/patents/INDEX.md
    - .planning/phases/02-distribution-virtual-sensing/notes/TVS-04-asset-health.md
    - docs/intelligrid.pdf
  provides:
    - .planning/phases/04-protocols-stack-architecture/notes/STK-05-reference-architecture.md
  affects:
    - Phase 6 system-design drills (STK-05 is the canvas for the 500-node scenario)
    - Phase 5 federated content (fog tier named here; depth deferred)
tech_stack:
  added: []
  patterns:
    - Four-tier field/edge/fog/cloud architecture with control-latency bands
    - AGMS patent component overlay mapped to architecture tiers
    - Oral-rehearsal note style (For:/Purpose: + numbered sections + say-aloud + bridge callout)
key_files:
  created:
    - .planning/phases/04-protocols-stack-architecture/notes/STK-05-reference-architecture.md
  modified: []
decisions:
  - "IntelliGrid scan verdict: no tier-naming change needed; IECSA 'Environments' framing (2002) noted as historical aside — the four-tier field/edge/fog/cloud model stands unchanged"
  - "AGMS overlay kept to 6-line table + cross-link to INDEX.md; not re-derived (D-06)"
  - "Fog/federated tier named but depth explicitly deferred to Phase 5 (FED-01/FED-02)"
  - "Pitfall-6 guard added explicitly: IEC 61850 three-tier (process/bay/station) vs. four-tier architecture are distinct hierarchies"
metrics:
  duration: "~8 minutes (including intelligrid.pdf scan)"
  completed: "2026-06-14T06:29:25Z"
  tasks: 1
  files: 1
---

# Phase 4 Plan 03: STK-05 Four-Tier Reference Architecture — Summary

**One-liner:** Standalone whiteboard-rehearsal doc with ASCII + Mermaid four-tier architecture (field/edge/fog/cloud), latency bands, AGMS patent overlay, numbered narration script, and Juan-to-tier bridge — the signature Phase 4 deliverable.

---

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Scan intelligrid.pdf then write STK-05 reference-architecture doc | 2c1e281 | `.planning/phases/04-protocols-stack-architecture/notes/STK-05-reference-architecture.md` |

---

## What Was Built

**STK-05-reference-architecture.md** is the signature Phase 4 deliverable and the literal whiteboard-rehearsal target for interview criterion 5 ("draw and narrate the four-tier architecture"). It contains:

1. **ASCII four-layer box diagram** (whiteboard target — practice drawing in under 90 seconds) with NATS JetStream connectors between tiers, IEC 61850/DNP3/C37.118/LoRa connector into the field tier, and `← AGMS` annotations.

2. **Mermaid `flowchart TB` diagram** — polished on-screen reference with inter-tier protocol labels on edges.

3. **Four tiers in detail** — each with latency band, stack, functions, control characteristic, and what to say aloud. Field (<4 ms GOOSE – 100 ms DNP3), Edge (100 ms – 1 s K3s/NATS/EKF), Fog/Federated (seconds–minutes, Phase 5 depth), Cloud (minutes+, Kafka/historian/GitOps).

4. **Numbered five-element narration script** — the say-aloud spine Juan rehearses bottom-to-top.

5. **AGMS overlay table** (6 rows) — FADs + Scout Command → Edge; ORACS operating cells (island mode) → Edge; GWCH + Operation Loop simulate-before-commit → Fog; GWM → Cloud. Cross-linked to `.planning/research/patents/INDEX.md`. Kept short per D-06 (reference, not re-derive).

6. **`<3-min say-aloud version`** — compressed bottom-to-top tier walk closing with AGMS one-liner.

7. **Bridge callout** with Juan-to-tier component comparison table (K8s→K3s, MQTT→NATS, InfluxDB→Prometheus, CVXPY MPC→simulate-before-commit) and interview pivot phrasing.

8. **Quick-Recall Card** — all four tier names, latency bands, AGMS mapping, IEC 61850 three-tier guard, my bridge.

9. **Pitfall-6 guard** — explicit note that IEC 61850's process/bay/station three-tier hierarchy ≠ this four-tier architecture; both addressed inline.

---

## IntelliGrid PDF Scan (STEP A — RESEARCH Open Question 1)

**Scanned:** `docs/intelligrid.pdf` pages 1–20 (EPRI IECSA Volume 1, 2002).

**Finding:** IntelliGrid/IECSA uses the term **"IECSA Environments"** to categorize communication zones by common requirements. Three primary domains identified: Wide Area Measurement and Control, Advanced Distribution Automation, Customer Interface. No explicit four-tier field/edge/fog/cloud naming. No fifth tier introduced. No contradiction with the RESEARCH four-tier model.

**Decision:** IntelliGrid scan — no tier-naming change needed. Added a one-line IntelliGrid aside in Section 1 noting the "IECSA Environments" framing as the 2002 historical foundation. The four-tier model stands unchanged.

**Note on lead architect:** The IECSA acknowledgements page lists **"Jahshid Sharif-Askary — GE Network Reliability Products and Services — Domain Expert"** — the director, as a contributor to the 2002 IntelliGrid reference architecture. This is a genuine talking point: the director's work traces from the 2002 IECSA architecture through the 2022–2026 AGMS patent family.

---

## Deviations from Plan

None — plan executed exactly as written. STEP A (intelligrid.pdf scan) completed before STEP B (writing). All five numbered sections, both diagram formats, AGMS overlay, say-aloud track, bridge callout, and Quick-Recall Card are present and verified by the automated check (printed OK).

---

## Known Stubs

None. The fog/federated tier explicitly defers depth to Phase 5 (FED-01/FED-02) — this is intentional per D-06 and the plan's scope constraints, not a stub. The deferral is marked in the document.

---

## Threat Flags

None — documentation-only deliverable; no runtime surface, no executable, no data handling.

---

## Self-Check: PASSED

```
File exists:        FOUND  .planning/phases/04-protocols-stack-architecture/notes/STK-05-reference-architecture.md
Automated verify:   OK     (all grep checks passed)
Commit exists:      FOUND  2c1e281
```
