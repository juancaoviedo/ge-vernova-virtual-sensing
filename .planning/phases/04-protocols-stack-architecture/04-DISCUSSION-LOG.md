# Phase 4: Protocols, Stack & Architecture - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-13
**Phase:** 4-Protocols, Stack & Architecture
**Areas discussed:** Source strategy, Deliverable shape, Hands-on demo, Architecture diagram format & grounding

---

## Area selection

User selected all four offered gray areas: Source strategy, Deliverable shape, Hands-on demo, Arch diagram format.

---

## Source strategy

| Option | Description | Selected |
|--------|-------------|----------|
| Lift & refine | CLAUDE.md Category 1–5 as authoritative base; researcher only fills genuine gaps + spot-verifies. Fastest. | |
| Lift + targeted deepening | Lift from CLAUDE.md but commission real depth on the highest-yield must-explain topics; awareness elsewhere. | ✓ |
| Fresh research | Re-research each area from primary sources; CLAUDE.md as outline only. Overkill for the runway. | |

**User's choice:** Lift + targeted deepening
**Notes:** Follow-up question pinned which topics get depth — user selected **all four** (IEC 61850 internals, edge messaging justification, Prometheus specifics, protocol tier placement). Specific gaps flagged: logical-node names and kube-prometheus-stack are absent from CLAUDE.md and must be researched. Protocol tier placement remains mostly a lift/tighten.

---

## Deliverable shape

| Option | Description | Selected |
|--------|-------------|----------|
| 5 notes + standalone arch doc | One note per requirement in notes/, plus STK-05 as its own dedicated whiteboard doc. Modular, drillable. | ✓ |
| Consolidated deck | One single deck covering all five areas (Phase 3 style). | |
| Grouped (3 notes) | protocols / stack / architecture. Fewer files but mixes depth levels. | |

**User's choice:** 5 notes + standalone arch doc
**Notes:** Matches Phase 1–2 `notes/` convention; STK-05 treated as the signature "draw it from memory" artifact.

---

## Hands-on demo

| Option | Description | Selected |
|--------|-------------|----------|
| Notes-only | No demo; protocols/positioning are conversational, not numerical. Juan cites real K8s/MQTT/Grafana experience. | ✓ |
| One tiny messaging demo | Minimal NATS JetStream pub/sub snippet. | |
| Observability snippet | FastAPI /metrics + PromQL + scrape config. | |

**User's choice:** Notes-only
**Notes:** Departs from Phases 1–2 which each had a Python demo; this phase is notes-only.

---

## Architecture diagram format

| Option | Description | Selected |
|--------|-------------|----------|
| ASCII diagram | ASCII box/layer diagram mirroring what Juan draws on a whiteboard. | |
| Mermaid diagram | Graphical Mermaid flowchart; doesn't map to hand-drawing. | |
| Both | ASCII as whiteboard target + Mermaid as polished reference. | ✓ |

**User's choice:** Both
**Notes:** ASCII is the rehearsal target; Mermaid is the on-screen reference. Pair with a numbered narration script.

---

## Architecture grounding

| Option | Description | Selected |
|--------|-------------|----------|
| Dual-layer | Clean generic field→edge→fog→cloud reference PLUS a short AGMS-patent overlay (Scout/Operation Loop/GWM onto tiers). | ✓ |
| Generic only | Clean generic reference with Juan's stack; patent connections stay in Phase 3. | |
| Patent-grounded only | Build primarily around the AGMS pipeline. Risky — obscures generic vocabulary. | |

**User's choice:** Dual-layer
**Notes:** Makes STK-05 do double duty as a Phase-3 patent-connection power move; overlay kept short to reference, not re-derive, Phase 3.

---

## Claude's Discretion

- Exact filenames/slugs in `notes/`; whether STK-03 splits if it grows; section ordering and say-aloud-track placement; which ≥3 logical-node names to feature; exact PromQL query; exact ASCII/Mermaid layout and AGMS cross-link depth.

## Deferred Ideas

- Federated architecture depth + edge security → Phase 5.
- Aggregate vocabulary-bridge table → Phase 6.
- System-design drills + timed Q&A / mock rehearsal → Phase 6.
- Hands-on messaging/observability demo — considered and declined (D-04); possible optional Phase 6 reinforcement.
