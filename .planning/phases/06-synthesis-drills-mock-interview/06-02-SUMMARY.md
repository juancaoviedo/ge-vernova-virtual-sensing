---
phase: 06-synthesis-drills-mock-interview
plan: "02"
subsystem: interview-prep
tags: [vocabulary-bridge, osed-pitch, reframe, brg-01, brg-02, phone-screen, layer-a, layer-b]
dependency_graph:
  requires: [phase-01-notes, phase-02-notes, phase-04-notes, phase-05-notes, 06-01-PHONE-SCREEN]
  provides: [BRG-01-bridge-table, BRG-02-tiered-pitch]
  affects: [REHEARSAL-TRACKER, QUESTION-BANK]
tech_stack:
  added: []
  patterns: [two-layer-bridge-table, tiered-pitch-outcome-first, D-16-extract-not-rederive]
key_files:
  created:
    - .planning/phases/06-synthesis-drills-mock-interview/notes/REFRAME.md
  modified: []
decisions:
  - D-06: Two-layer bridge table — Layer A plain HR translation (≤10 s, no LaTeX), Layer B technical T&D + tool bridges lifted from Phase 1–5 callouts
  - D-07: Tiered OSED pitch — ≤90 s plain / ~2–3 min plain / ~10 min technical; all open with the 21% deployed outcome; honest framing (OSED edge inference is an analog to production FL, not a production-FL claim)
  - D-15: For:/Purpose: header, screen tier jargon-free, LaTeX only in technical-round material
  - D-16: All Layer B bridges and pitch content extracted from existing Phase 1–5 notes — no new technical content authored
metrics:
  duration: ~30 min
  completed: "2026-06-16"
  tasks_completed: 2
  tasks_total: 2
  files_created: 1
  files_modified: 0
---

# Phase 6 Plan 02: Vocabulary Bridge Table & Tiered OSED Pitch (REFRAME.md) Summary

**One-liner:** Two-register vocabulary system (15 Layer-A HR translations + 13 Layer-B T&D tool bridges) and a three-tier OSED pitch (≤90 s / ~2–3 min / ~10 min), all outcome-first with the 21% deployed result, lifted from Phase 1–5 bridge callouts.

## What Was Built

`REFRAME.md` delivers two capabilities:

**BRG-01 — Vocabulary Bridge Table (two layers):**

- **Layer A (15 entries):** Plain-language HR translations covering every major term Juan uses — MQTT/K8s edge orchestration, EKF/state estimation, OSED, HEMS, federated learning, MPC, IEC 61850 GOOSE, ORACS/CaCSM, SI-MAPPER, DNP3, Prometheus, K3s, SPIFFE/SPIRE, posterior covariance/observability index, NATS JetStream. Each deliverable within ≤10 s (screen criterion). Zero LaTeX. Zero unexpanded acronyms.

- **Layer B (13 entries):** Technical T&D and tool bridges lifted directly from the "Bridge to your work" callouts in Phase 1–5 notes (D-16). Key bridges: MQTT→NATS JetStream (STK-03), K8s→K3s (STK-03), InfluxDB/Grafana→Prometheus/kube-prometheus-stack (STK-04), CVXPY MPC→simulate-before-commit/AGMS CaCSM (DSSE-04), HEMS forecasting→FASE temporal prior (KAL-01+DSSE-04), OSED edge runtime→FAD Inspector scout substrate (DSSE-04), Modbus→DNP3 (STK-01/CLAUDE.md), MQTT fleet→SPIFFE/SPIRE (FED-03), AMI/inverter self-reports→DSSE-02 side-information taxonomy.

**BRG-02 — Tiered OSED Pitch (three versions):**

- **Version 1 — ≤90 s (screen):** Four spoken bullet prompts; scripted opening hook anchored to the 21% deployed outcome; plain-language with GE Vernova mission alignment and differentiator hook (SI-MAPPER/AGMS patent). Zero LaTeX (Pitfall 5 compliant).

- **Version 2 — ~2–3 min (first technical touch):** Stack shape added (cloud tier / edge tier / telemetry layer / control layer) without math; federated inference pattern named; differentiator hook extended.

- **Version 3 — ~10 min (deep technical round):** Four-layer technical walk lifted from KAL-01 and DSSE-04 say-aloud tracks (D-16): (1) edge virtual sensing with information-budget framing and $G = H^\top W H$ singularity; (2) simulate-before-commit / CVXPY MPC connection; (3) federated edge pipeline with honest framing (OSED = architectural analog to production FL, not a production-FL claim — D-07 / T-06-03 mitigation); (4) AGMS patent component-by-component bridge table.

## Deviations from Plan

None — plan executed exactly as written. Both tasks (Layer A+B bridge table; tiered pitch) were authored in a single write to minimize context switches and keep the document internally consistent. All Layer B content extracted from named source notes; no new technical content derived (D-16 compliance).

## Threat Surface Scan

No new network endpoints, auth paths, file access patterns, or schema changes introduced. REFRAME.md lives under `.planning/` (private notes), not `docs/` (HTML site). T-06-03 (false production-FL claim) was explicitly mitigated in Version 3 of the tiered pitch with the "honest framing" paragraph. T-06-04 (information disclosure) is accepted — content is non-sensitive.

## Key Decisions Made

1. **Layer A expanded beyond the six seed examples** in 06-RESEARCH to cover 15 terms — the full set of terms Juan is likely to be prompted with on a phone screen. Plain-language analogies favor "what it does for the user" over "what it is technically."

2. **Layer B sources lifted in priority order:** DSSE-04 and KAL-01 bridges were most critical (Inspector scout / OSED / CVXPY MPC triple connection); STK-03 MQTT→NATS and K8s→K3s bridges were the clearest tool-gap connections.

3. **Version 3 honest framing placed at Layer 3 (federated edge pipeline):** The boundary statement ("OSED implements federated inference at the edge… I have not shipped a Flower-based federated gradient aggregation at scale") is precise and specific — it satisfies D-07 and the T-06-03 threat mitigation without underselling what was actually built.

4. **Component-by-component AGMS bridge table in Version 3:** Five-row table (Inspector scout / FASE prior / simulate-before-commit / self-forming federations / Learning Engine) maps each AGMS concept to a specific Juan deliverable — the strongest differentiator closing hook.

## Self-Check: PASSED

- REFRAME.md: FOUND at `.planning/phases/06-synthesis-drills-mock-interview/notes/REFRAME.md`
- Task 1 commit 7a1f69f: FOUND
- Layer A heading: present (1 match)
- Layer B heading: present (1 match)
- Table rows: 32 (requirement ≥ 8)
- NATS/K3s/Prometheus in Layer B: present
- For:/Purpose: headers: present
- Tiered OSED Pitch heading: present
- Version 1 / Version 2 / Version 3 headings: all present
- 21% in pitch section: 3 occurrences
- Version 1 LaTeX-free: confirmed (0 `$` characters in screen tier)
- Honest-framing ("analog") constraint: present in Version 3
