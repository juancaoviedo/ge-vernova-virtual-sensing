# Phase 4: Protocols, Stack & Architecture - Context

**Gathered:** 2026-06-13
**Status:** Ready for planning

<domain>
## Phase Boundary

Produce study material that makes Juan **fluent in the grid protocol stack, the edge/cloud
software stack, and the end-to-end reference architecture** — so he can navigate them in
conversation and draw the architecture from memory in the interview (STK-01..05):

- **STK-01** — Grid protocol stack: SCADA, DNP3, PMU/C37.118, IEC 61850, LoRa (and MQTT) placed in the correct field-to-cloud tier, one key property each.
- **STK-02** — IEC 61850: GOOSE vs. SV vs. MMS, the three-tier hierarchy, and ≥3 named logical-node names — without notes.
- **STK-03** — Edge/cloud stack positioning: NATS JetStream vs. MQTT vs. Kafka (vs. Pulsar), and the three K3s-vs-K8s distinctions (air-gap, memory, etcd/SQLite), with interview-ready justifications.
- **STK-04** — Observability: Prometheus pull model vs. InfluxDB push, a recitable PromQL query, and what kube-prometheus-stack adds.
- **STK-05** — A whiteboard-able **four-tier reference architecture** (field → edge → fog/federated → cloud) Juan can draw and narrate, including control-latency tiers and key components per layer.

**Out of scope (belongs to other phases):** federated architecture / FedAvg-FedProx-Krum +
edge security internals (Phase 5 — referenced at awareness level only here, e.g. the
"fog/federated" tier names the concept but Phase 5 owns its depth); the aggregate
vocabulary-bridge table + STAR stories + OSED pitch + timed mock-interview rehearsal loop
(Phase 6). This phase produces **reference/rehearsal notes + one standalone architecture
doc** — no aggregate rehearsal artifact, no demo.

</domain>

<decisions>
## Implementation Decisions

### Source strategy (all STK)
- **D-01:** **Lift + targeted deepening.** Treat **CLAUDE.md "Category 1–5"** as the authoritative content base (it already holds near-interview-ready comparison tables for NATS/Kafka/Pulsar/MQTT, K3s/K8s, DNP3/Modbus, PMU/C37.118, IEC 61850, Prometheus/InfluxDB, LoRa/Zigbee, and the Summary Reference Table). Notes distill/refine it for **spoken delivery**; the researcher does **real depth + gap-fill** on the topics in D-02 and spot-verifies version/fact claims. Do **not** re-research from scratch what CLAUDE.md already covers well.
- **D-02:** **All four named-must-explain areas get research depth** (not just awareness lift), with these specific gaps flagged because CLAUDE.md does NOT currently cover them:
  - **IEC 61850 internals** (STK-02): GOOSE vs. SV vs. MMS roles + three-tier hierarchy + **≥3 named logical-node names** (e.g. XCBR, MMXU, CSWI, PTOC) — CLAUDE.md lists GOOSE/SV/MMS/CIM but **no logical-node names**. This is the criterion-2 gap.
  - **Edge messaging justification** (STK-03): the crisp spoken "**why NATS JetStream over MQTT and over Kafka for the substation edge**" argument + the three K3s-vs-K8s distinctions. Tables exist; the *justification narrative* needs sharpening.
  - **Prometheus specifics** (STK-04): a concrete recitable **PromQL query** + **what kube-prometheus-stack adds** (operator, bundled exporters, Grafana, Alertmanager) — CLAUDE.md has PromQL snippets but **never names kube-prometheus-stack**. Criterion-4 gap.
  - **Protocol tier placement** (STK-01): crisp one-property-each + correct tier for SCADA/DNP3/PMU-C37.118/IEC61850/LoRa — mostly a **lift/tighten** from CLAUDE.md Category 3 (lowest net-new research need of the four).

### Deliverable shape (all STK)
- **D-03:** **5 notes (one per requirement) in a `notes/` directory + STK-05 as its own standalone whiteboard-architecture doc.** Layout: `notes/STK-01-protocol-stack.md`, `notes/STK-02-iec-61850.md`, `notes/STK-03-messaging-orchestration.md`, `notes/STK-04-observability.md`, and a dedicated `notes/STK-05-reference-architecture.md` (or equivalent) treated as the signature "draw it from memory" artifact. Follows the Phase 1–2 `notes/` convention; modular so each topic can be drilled in isolation. **No consolidated single deck** (that was Phase 3's pattern, not this one). **No `demo/` directory.**

### Hands-on demo (all STK)
- **D-04 [informational]:** **Notes-only — no demo.** (Scope-exclusion guardrail — no covering plan task by design; plans must NOT create a `demo/` dir.) Protocols and stack-positioning are conversational/architectural, not numerical (unlike the Phase 1 EKF and Phase 2 power-flow demos). Time is better spent on IEC 61850 depth and the whiteboard architecture; Juan already has real K8s/MQTT/Grafana **production** experience to cite as the "I've built this" credibility.

### Architecture diagram (STK-05)
- **D-05:** **Both diagram formats.** An **ASCII** box/layer diagram is the primary whiteboard-rehearsal target (it mirrors what Juan will physically draw — the study artifact *is* the rehearsal target), **plus a Mermaid** version for a polished on-screen reference. Pair the diagram with a **numbered narration script** (control-latency tiers + key components per layer) so STK-05 satisfies the "draw AND narrate" success criterion.
- **D-06:** **Dual-layer grounding.** The architecture doc carries (a) a **clean generic** field → edge → fog/federated → cloud reference annotated with **Juan's own stack** at each tier (K3s, NATS JetStream, EKF engine, Prometheus) — this is what criterion 5 literally tests — **and** (b) a short **AGMS overlay** mapping the director's patent components onto the same tiers (e.g. Scout Command / Field Agent Devices → edge; Operation Loop *simulate-before-commit* → fog/federated; GWM/cloud aggregation → cloud). This makes STK-05 do double duty as a Phase-3 patent-connection power move. Keep the overlay *short* — it references, not re-derives, Phase 3 depth.

### Conventions carried forward (from Phases 1–2 — non-negotiable, not re-discussed)
- **D-07:** **Oral-rehearsal note style.** Each note opens with the **For: / Purpose:** header, uses numbered sections, and is written for speak-aloud recall. Each note carries a tight **"<3-min say-aloud"** talk-track hitting its criterion's named points (per Phase 2 D-06).
- **D-08:** **Per-note "→ Bridge to your work" callout.** Each note ends with a boxed 1–2 sentence bridge mapping the concept to Juan's concrete experience — **MQTT → NATS**, **full K8s → K3s**, **InfluxDB+Grafana → Prometheus/PromQL**, **Zigbee → LoRa**, **Modbus → DNP3** — phrased as a ready interview pivot (per Phase 2 D-04). CLAUDE.md's Summary Reference Table ("Compare To (Juan has)" + "Interview One-Liner" columns) is the raw material.
- **D-09 [informational]:** **No aggregate vocabulary-bridge table and no timed-drill / Q&A rehearsal loop here** — those are **Phase 6** (BRG-01..03, QNA-01..03). (Scope-exclusion guardrail — no covering plan task by design; plans enforce the exclusion.) Per-note bridges + say-aloud tracks feed Phase 6 without duplicating it now.
- **D-10:** **Markdown style** per project convention — prose + tables carry most of this phase (it is positioning/architecture, largely non-equation); use LaTeX-in-markdown only where a formula genuinely helps (e.g. a C37.118 reporting-rate note). Mirror Phase 2's note structure.

### Claude's Discretion
- Exact filenames/slugs within `notes/`; whether STK-03 stays one note or splits messaging from orchestration if it grows unwieldy; precise section ordering within each note and whether the "<3-min say-aloud" track sits at top or bottom; which specific ≥3 logical-node names to feature; the exact PromQL query chosen; exact ASCII/Mermaid layout and how richly the AGMS overlay cross-links back to the Phase 3 deck/INDEX.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

ROADMAP.md declares no explicit "Canonical refs" line for Phase 4. The references below were
accumulated from CLAUDE.md (the primary content base for this phase), REQUIREMENTS.md, the
`docs/` source material, and the Phase 1–3 artifacts whose conventions this phase follows.

### Primary content base (lift & refine from THESE first — D-01)
- `CLAUDE.md` — **the authoritative content base.** "Category 1: Streaming & Messaging" (NATS/Kafka/Pulsar/MQTT tables → STK-03), "Category 2: Edge Orchestration" (K3s-vs-K8s → STK-03), "Category 3: Grid Protocols" (SCADA/DNP3/PMU/C37.118/IEC 61850/LoRa → STK-01, STK-02), "Category 4: Observability" (Prometheus/InfluxDB/PromQL → STK-04), the "Summary Reference Table" (the bridge raw material → D-08), "What NOT to Over-Invest In", and "Recommended Python Libraries to Recognize". The notes distill/tighten these for spoken delivery.

### Source material in `docs/`
- `docs/job-requirements.md` — the JD; the vocabulary target and the named tools (NATS, Kafka, Pulsar, K3s, Prometheus, DNP3, IEC 61850) Juan must speak to.
- `docs/Juan Carlos Oviedo Cepeda - 2026.pdf` — Juan's CV; source of the MQTT / Kubernetes / InfluxDB-Grafana / Zigbee / Modbus experience anchoring every "→ Bridge to your work" callout (D-08).
- `docs/IEC 61850-3.pdf` — substation/IEC 61850 context for STK-02 depth.
- `docs/intelligrid.pdf` — IntelliGrid reference architecture; grounding for the STK-05 four-tier reference architecture.
- `docs/orbit.pdf`, `docs/flisr.pdf` — additional grid-context source material (consult if relevant to tier placement / architecture).

### Standards referenced by requirements (cite, don't reproduce)
- **IEEE C37.118** — synchrophasor / PMU data standard (STK-01 PMU tier + reporting-rate property).
- **IEC 61850** — substation automation standard (STK-02: GOOSE, SV, MMS, logical nodes, three-tier hierarchy).
- **DNP3** — utility SCADA protocol (STK-01 tier + timestamp/unsolicited-reporting property).

### Phase 3 patent material (for the STK-05 AGMS overlay — D-06)
- `.planning/research/patents/INDEX.md` — AGMS component map + the connection table; source for mapping Scout Command / Operation Loop / GWM onto architecture tiers. Keep the overlay short — reference, don't re-derive.
- `.planning/phases/03-director-s-patents-deep-read/03-01-PLAN.md` and the resulting rehearsal deck — the existing patent-connection layer the overlay cross-links to.

### Phase convention references (note style — D-07/D-08/D-10)
- `.planning/phases/02-distribution-virtual-sensing/notes/TVS-04-asset-health.md` (and siblings) — established note style: For:/Purpose: header, numbered sections, "<3-min say-aloud" track, boxed "→ Bridge to your work" callout. Phase 4 mirrors this.
- `.planning/phases/02-distribution-virtual-sensing/02-CONTEXT.md` — the D-04/D-06/D-09/D-10 convention decisions carried forward here.
- `.planning/phases/01-kalman-state-estimation/notes/KAL-02-kalman-family-kf-ekf-ukf.md` — canonical note-style reference.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **CLAUDE.md Category 1–5 tables** — the single biggest reusable asset; ~80% of this phase's comparison content already exists in interview-ready table form. Notes lift and tighten rather than author from scratch (D-01).
- **CLAUDE.md "Summary Reference Table"** — already maps each gap tool to "Compare To (Juan has)" + a one-liner; direct raw material for the per-note "→ Bridge to your work" callouts (D-08).
- **Phase 1–2 `notes/` layout + note header style** — the For:/Purpose:, numbered-section, say-aloud, bridge-callout pattern is established and reused (D-07/D-08).

### Established Patterns
- **`notes/` per-requirement file split** (Phases 1–2) — followed here (D-03), departing from Phase 3's single-consolidated-deck pattern.
- **No `demo/` this phase** (D-04) — departs from Phases 1–2 which each had a Python demo; this phase is notes-only.
- **Markdown + selective LaTeX** — prose/tables carry it; equations only where they help (D-10).

### Integration Points
- Phase 4 notes feed **Phase 6**: per-note "→ Bridge to your work" callouts and "<3-min say-aloud" tracks become raw material for the aggregate vocabulary-bridge table (BRG-01..03) and system-design drills (QNA — e.g. the "500-node virtual sensing pipeline" scenario draws directly on STK-05's four-tier architecture). Keep them in a form Phase 6 can lift directly.
- STK-05's AGMS overlay **references Phase 3** (patent connections) — keep cross-links so the two reinforce rather than duplicate.

</code_context>

<specifics>
## Specific Ideas

- **STK-05 is the signature deliverable.** The doc's spine is the four tiers — **field** (sensors/IEDs/RTUs/PMUs; DNP3, C37.118, IEC 61850 GOOSE/SV) → **edge** (K3s nodes running EKF/virtual-sensing inference; NATS JetStream; <4 ms–to–seconds control) → **fog/federated** (cross-substation aggregation, federated decisions — Phase 5's territory, named only) → **cloud** (long-term historian, model training, fleet GitOps). Annotate control-latency tiers per layer. ASCII = whiteboard target; Mermaid = polished reference; numbered narration script = the "narrate it" half.
- **Bridge callouts read as interview pivots**, e.g. "I ran MQTT-to-Mosquitto in OSED; NATS JetStream is the same publish/subscribe instinct but adds durable replay and decentralized JWT accounts for the federated edge — that's the upgrade path I'd take here."
- **Lead with the gap-fills Juan can't fake**: the 3 logical-node names, the kube-prometheus-stack name, and the crisp "NATS over Kafka at the edge because Kafka needs a JVM + 64–128 GB and NATS runs on a Pi-class node" one-liner — these are the highest-yield, most-likely-asked specifics.

</specifics>

<deferred>
## Deferred Ideas

- **Federated architecture depth** (FedAvg/FedProx/Krum, non-IID/client-drift, Byzantine robustness, gossip-vs-central) and **edge security** (OTA integrity, TPM attestation, SPIFFE/SPIRE) — **Phase 5**. The STK-05 "fog/federated" tier names the concept only.
- **Aggregate vocabulary-bridge table** (tool → Juan's-tool analog → pivot sentence) — **Phase 6** (BRG-01..03). Per-note callouts here feed it.
- **System-design drills** (e.g. "500-node virtual sensing pipeline") and **timed Q&A / mock-interview rehearsal** — **Phase 6** (QNA-01..03). STK-05's architecture is the canvas these drills draw on.
- **A hands-on messaging/observability demo** (NATS pub/sub, FastAPI /metrics + PromQL) — considered and **declined** for this phase (D-04). Could be revisited as optional Phase 6 reinforcement if time allows, but not planned.

None beyond the above — discussion stayed within phase scope.

</deferred>

---

*Phase: 4-Protocols, Stack & Architecture*
*Context gathered: 2026-06-13*
