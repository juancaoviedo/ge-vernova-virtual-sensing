# GE Vernova Virtual Sensing — Interview Prep

## What This Is

A focused, time-boxed interview-preparation project for Juan Carlos Oviedo Cepeda's
application to the **Senior Software Engineer & Scientist – Virtual Sensing and
Decentralized Grid Operations** role at GE Vernova (CTO org, reporting to the
Electrification Chief Architect; West Melbourne, hybrid; req R5043890). It turns the
gathered source material (the lab director's patents, IEC 61850, IntelliGrid
architecture, the job description, and Juan's CV) into study notes, predicted Q&A and
talking points, system-design drills, and small hands-on demos — so Juan can walk into
the interview able to (1) reframe his existing edge/DER work in GE Vernova's language and
(2) speak credibly to the specific gaps the role names.

## Core Value

Juan walks into the interview able to connect his real experience to this role's exact
requirements — and to the director's own patented work — with confidence and specifics.
Everything else is secondary to that.

## Requirements

### Validated

<!-- Shipped and confirmed valuable. -->

- [x] Deep-read of the director's six-patent AGMS family (parent + Logistician, Asset Portfolio, Operation Loop ★GRANTED/GE Vernova, Scout Command, Data Management) → one consolidated rehearsal deck with per-patent summary + connection + architecture-level question, a ~90s family pitch, and the "one assembly line = my stack" master narrative — *Validated in Phase 3: Director's Patents Deep-Read*
- [x] Grid protocol & software-stack study notes (STK-01..05): field-to-cloud protocol tier map (SCADA/DNP3/PMU-C37.118/IEC 61850/LoRa), IEC 61850 deep note (GOOSE/SV/MMS + XCBR/MMXU/CSWI/PTOC/PDIS logical nodes), NATS/MQTT/Kafka + K3s/K8s positioning, Prometheus/PromQL/kube-prometheus-stack, and a whiteboard-able four-tier reference architecture (ASCII + Mermaid + narration + AGMS overlay) — *Validated in Phase 4: Protocols, Stack & Architecture* (oral/whiteboard rehearsal tracked in 04-HUMAN-UAT.md)
- [x] Federated architectures & edge-security study notes (FED-01/02) + a NumPy teaching demo: federated-vs-distributed (no central coordinator), FedAvg/FedProx + non-IID/client-drift, Byzantine robustness (Krum / coordinate-wise median + gossip-vs-central), and an awareness-depth edge-security note (OTA integrity / TPM attestation / SPIFFE-SPIRE, each tied to a grid threat). The demo runs from scratch in NumPy and shows plain FedAvg corrupted by a poisoned client while FedProx/Krum/median resist. Closes the Phase-4 STK-05 "fog/federated" tier with light AGMS ties — *Validated in Phase 5: Federated Architectures & Security*
- [x] Integrated, offline-first HTML study site assembled into `/docs` (GitHub Pages-ready): a card-grid hub (with per-page sticky TOC) tying together the AGMS architecture/patents research pages + an annotated draw.io diagram, all 16 Phase 1–5 study notes converted to HTML with offline MathJax-rendered equations, and a demos page explaining each of the 3 hands-on demos (EKF, DC-power-flow WLS/bad-data, federated) with embedded key-function code + inline results. Built by a re-runnable `docs/build_site.py`; `noindex`/`robots.txt`/`.nojekyll` for unlisted sharing; `PUBLISH.md` deploy guide; build-time `validate_links()` gate (24 pages, 0 broken links). Offline math + full offline navigation human-verified — *Validated in Phase 7: Integrated HTML Study Site*
- [x] Interview-delivery synthesis pack (BRG-01..03, QNA-01..03), **phone-screen-first**: six `notes/` deliverables — `PHONE-SCREEN.md` (jargon-free round-1 HR pack: ≤90 s pitch, fit narrative, TN-visa/relocation/comp logistics scripts, HR question set), `REFRAME.md` (two-layer vocabulary bridges + tiered outcome-first OSED pitch), `STAR-STORIES.md` (four JD-mapped STAR stories incl. SI-MAPPER→AGMS-scouts differentiator citing GRANTED US 12,596,341 B2), `QUESTION-BANK.md` (26 JD-bullet question pairs + 12 differentiator-weighted domain Qs + consolidated bank by round), `SYSTEM-DESIGN-DRILLS.md` (500-node pipeline + close-the-loop sim→field), and `REHEARSAL-TRACKER.md` (flashcards + 7-day protocol + weakest-item flags). 12/12 must-haves verified; oral rehearsal tracked in 06-HUMAN-UAT.md — *Validated in Phase 6: Synthesis, Drills & Mock Interview*

### Active

<!-- Current scope. Building toward these. -->

- [ ] Distilled study notes for each high-priority gap area
- [x] Predicted interview questions with strong, personalized answers (STAR stories from Juan's CV) — *done in Phase 6 (STAR-STORIES.md + QUESTION-BANK.md)*
- [x] A "reframe" map translating Juan's existing work (OSED, HEMS, DER control) into GE Vernova's virtual-sensing / decentralized-grid vocabulary — *done in Phase 6 (REFRAME.md two-layer bridges)*
- [ ] Kalman filter & state-estimation primer grounded in a grid virtual-sensing example
- [ ] Grid domain & protocol notes: SCADA, PMUs, DNP3, LoRa, IEC 61850, IEEE 2030.5
- [x] Federated architectures / federated learning framing — *done in Phase 5 (FED-01/02 notes + NumPy demo)*
- [ ] Streaming-stack notes covering Kafka/NATS, Pulsar (vs. Juan's MQTT/Pub-Sub experience)
- [ ] 1–2 hands-on mini-demos (e.g., Kalman filter inferring a grid parameter; MQTT→edge pipeline)
- [x] System-design drills for edge/virtual-sensing/decentralized-grid scenarios — *done in Phase 6 (SYSTEM-DESIGN-DRILLS.md: 500-node pipeline + close-the-loop)*
- [x] Mock-interview question bank (technical + behavioral + domain) — *done in Phase 6 (QUESTION-BANK.md + REHEARSAL-TRACKER.md)*
- [ ] An expandable mechanism to ingest additional source documents Juan adds later and fold them into the study set

### Out of Scope

<!-- Explicit boundaries. Includes reasoning to prevent re-adding. -->

- Learning Go or Rust — JD says "Python, Go, **or** Rust"; Juan's Python + TypeScript already satisfies it.
- Building a production system — this is interview prep; demos are illustrative, not deliverable software.
- Generic software-engineering review — Juan is a strong, senior engineer; prep targets *this role's* specifics, not fundamentals.
- Deep EMT-tool mastery (PSCAD/RTDS/Opal-RT) — preferred-only; covered at awareness level, not hands-on, given the <1-week runway.

## Context

**Candidate background (from CV — Juan Carlos Oviedo Cepeda, PhD EE):**
- 9 yrs research, 5 yrs full-stack, 3 yrs cloud-edge, 1 yr agentic systems.
- Hydro-Québec / IREQ Research Scientist (2021–present): architected the **OSED** hybrid
  cloud-edge platform for grid services (dynamic tariffs, distributed control) — Python,
  Kubernetes, Docker, MQTT, FastAPI, InfluxDB, TimescaleDB, ML, convex optimization,
  control, CI/CD, Grafana. Edge ML for building thermal state + controllable-load
  management responding to grid needs. HEMS PoC; microgrid dynamic tariffs (−21% cost);
  Building Intelligence & Predictive Control open-source libs (CVXPY, gRPC, Redis,
  Modbus, Zigbee). Agentic AI: SI-MAPPER (CV→ontology, ASHRAE 223P), IoT-as-context for
  GenAI, IoT control API → MCP server. Big-data analysis (Databricks, PySpark, billions
  of points across substations). Led Hydro-Québec into Linux Foundation Energy.
- Founder, Contexto (2025–present): Azure ML MLOps entity resolution; multi-tenant AI
  video SaaS (GCP, Next.js, Stripe, CopilotKit); Next.js artifact-graph portfolio.
- Adjunct Professor, UQTR: co-directs 3 PhD students (flexibility markets, clustering,
  DLMP pricing). 30+ papers.
- PhD EE (honored thesis) + B.S. EE (top 3.4%), Universidad Industrial de Santander.
  Stanford Convex Optimization, Yale Game Theory, MIT courses, IEEE BCTE blockchain
  winner (top 10 global).

**Strengths that map directly to the role** (reframe, don't re-study): edge-native
real-time control across edge nodes; DERs/buildings as autonomous grid assets; ML on the
edge; MPC & convex optimization; IoT protocols (MQTT, Modbus, BACnet, OpenADR, Zigbee);
K8s/gRPC/InfluxDB/TimescaleDB/Grafana; agentic AI, knowledge graphs, MCP; open-source
culture fit.

**Source material gathered** (in `docs/`): the director's patent family — three distinct
patents (WO 2023/064623 adaptive-power *parent* + asset-portfolio & data-management
*continuations*; `patent_ocr.pdf` is the OCR'd duplicate of data-management, not a 4th).
They describe an Autonomous Grid Management System (AGMS) with AI "scouts" — directly
relevant to Juan's agentic-AI work. Also: IEC 61850-3, IntelliGrid (PDF + crawled mirror
under `summaries/`), Orbit patent search export, the job description.

**Gap analysis (priority order, drives the roadmap):**
1. 🔴 Kalman filters & state estimation — named in JD; Juan has Least Squares/MPC, not Kalman by name.
2. 🔴 Transmission-side virtual sensing — voltage stability, phase angles, line temperature, asset health (Juan's sensing is building/DER/distribution side).
3. 🔴 Director's patents (AGMS family, 3 patents) — deep-read to speak to the lab's actual work; the "scouts" architecture maps onto Juan's agentic-AI / MCP work.
4. 🟠 SCADA, PMUs, DNP3, LoRa — grid-specific protocols Juan hasn't used (has MQTT/Modbus).
5. 🟠 Federated architectures / federated learning — JD's "federated, no central coordination" framing.
6. 🟠 Streaming: Kafka/NATS, Pulsar — Juan uses MQTT + Pub/Sub.
7. 🟡 IEC 61850 / IEEE 2030.5 standards (has docs); EMT tools & OpenFMB/Modelica (awareness only).

## Constraints

- **Timeline**: Crash prep — interview expected within ~1 week of 2026-06-13. Prioritize highest-yield material; depth where it differentiates, awareness elsewhere.
- **Format**: Deliverables are study notes/summaries, Q&A + talking points, system-design drills, and small hands-on demos.
- **Scope discipline**: Target *this role's* named gaps and the director's work; reframe existing strengths rather than re-studying them.
- **Expandability**: Juan will add more source documents after kickoff; the plan must accommodate ingesting them into the study set.

## Key Decisions

<!-- Decisions that constrain future work. Add throughout project lifecycle. -->

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Identify gaps from Juan's CV rather than self-assessment | More objective; also reveals what was sent in the application | — Pending |
| Skip Go/Rust | JD accepts Python/Go/Rust (OR); Python+TS already qualifies | — Pending |
| Prioritize Kalman/state estimation, T&D virtual sensing, and director's patents | Highest-severity gaps + biggest differentiator under a 1-week runway | — Pending |
| Include an expandable "ingest more documents" phase | Juan will add material beyond the patents | — Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-06-25 — Phase 9 (Measurement System / Observability Layer) complete: the config-driven measurement layer between System 1 and the future System 2 estimator. A new additive `measure` runner (`measure.py`) + `measure_config.py` read System 1 / 8.1 ground truth from InfluxDB (the 96-step `state` day OR the 40-step `fault_event` scenario, one config flip), apply a node-voltage sensor model across the measurement-class taxonomy (SCADA / μPMU / AMI / DER / zero-injection / pseudo) under two placement scenarios (`well_observed` real-only redundancy ≈1.05 > 1.0; `realistic_sparse` ≈0.58 < 1.0 → ≥1.0 with pseudo), corrupt it with three switchable noise models (gaussian / gaussian_outliers / instrument), sample it in `snapshot` or `multirate_async` mode (per-class native-step decimation), and write z + assumed σ + re-published topology/phase metadata to a dedicated `measurements` bucket (tagged by experiment + scenario) — scoring oracle kept SEPARATE (no `true_value` field). The fault case honours the `energised` tag (dead buses 8–17 produce no live measurement; bus 17 μPMU goes dark). Two auto-provisioned Grafana dashboards (day + fault). Deterministic (seeded). 5/5 plans, verification 21/21 must-haves, 52 tests pass; code review found 3 "blockers" — CR-02 (hash()→hashlib determinism) and CR-03 (zero_inj absolute σ to avoid 1/σ²=∞) fixed, CR-01 (readers return list) a verified false positive; plus a per-snapshot redundancy bug found and fixed during UAT. Purely additive — System 1's day, the 8.1 fault scenario, and their buckets/dashboards are untouched. One human-UAT item open (visual Grafana panel render; dashboards confirmed loaded + data present via API). Next build: System 2 (the virtual-sensing state estimator that consumes the `measurements` bucket). Earlier (2026-06-24) — Phase 8.1 (System 1 Fault & Reconfiguration Scenario) complete: a separate, re-runnable quasi-steady-state fault/reconfiguration dataset on the System 1 IEEE 33-bus model, replicating the article's Section-8 fault → isolate → tie-restore sequence as a 40-step, 3-block (13 pre_fault / 7 faulted_isolated / 20 restored) quasi-static walk frozen at the evening peak. A new additive `fault-sim` runner (`fault_sim.py`) faults line idx 7, de-energises buses 8–17 (in-zone DG out + OLTC tap pinned during isolation), closes tie idx 34 to back-feed the zone radially (restored vmin ≈ 0.997 pu, clean ≥0.95), and writes full per-entity state + a new `event` measurement (phase tag, faulted line, tie state, dead-bus list) to a dedicated `fault_event` bucket with explicit `energised` flags and continuous before→0→after zero-fill series. A second auto-provisioned Grafana dashboard ("IEEE 33-Bus — Fault & Reconfiguration", 8 panels) renders the event. Purely additive — `sim.py`, the `state`/`profiles` buckets, and the original dashboard are byte-unchanged. 4/4 plans, verification 12/12, deterministic; code review found 1 blocker + 4 warnings (all fixed, incl. an sgen `energised`-tag schema-parity fix for the System-2 forward contract). One human-UAT item open (visual Grafana render). Next build: the Measurement System (Phase 9) → System 2 estimator. Earlier (2026-06-23) — Phase 8 (IEEE 33-Bus DER Measurement Source) complete: the first hands-on build — "System 1", a re-runnable ground-truth measurement source. Enhanced IEEE 33-bus radial network (4 renewable DG, 2 RPC capacitors, feeder OLTC) in PandaPower, driven through a 96-step (15-min) high-DER day (2017-06-07) whose solar/wind/load profiles are ingested once from the OPSD 15-min DE set into InfluxDB, full power-flow state captured per step and persisted to InfluxDB, visualized on a provisioned Grafana dashboard — all via Docker Compose + uv, reproducible from a README runbook. 5/5 plans, verification 7/7. Post-UAT fixes (from Juan's dashboard review): made the OLTC tap functional (pandapower-3.x tap_changer_type bug) with line-drop-compensation regulation (tap now switches −1..−4, day vmin 0.985); set realistic line ampacity (loadings 0.4–31%); corrected Grafana MW units. System 2 (the virtual-sensing estimator that consumes this dataset) is the next build. Earlier (2026-06-16) — Phase 6 (Synthesis, Drills & Mock Interview) complete: the interview-delivery synthesis pack, reframed **phone-screen-first** after Juan flagged that round 1 is a non-technical HR phone screen. Six `notes/` deliverables — PHONE-SCREEN.md (round-1 HR pack: ≤90 s pitch, fit narrative, TN-visa/relocation/comp logistics scripts, HR question set), REFRAME.md (two-layer vocabulary bridges + tiered outcome-first OSED pitch), STAR-STORIES.md (four JD-mapped STAR stories incl. the SI-MAPPER→AGMS-scouts differentiator citing GRANTED US 12,596,341 B2), QUESTION-BANK.md (26 JD-bullet question pairs + 12 differentiator-weighted domain Qs + consolidated bank by round), SYSTEM-DESIGN-DRILLS.md (500-node pipeline + close-the-loop sim→field), REHEARSAL-TRACKER.md (flashcards + 7-day protocol + weakest-item flags). Verifier: 12/12 must-haves verified, status human_needed — the remaining items are oral-rehearsal performance checks (Juan must run the REHEARSAL-TRACKER aloud), tracked in 06-HUMAN-UAT.md. Phases 0 and 1 (Document Ingestion; Kalman formal phase) remain not-started, though Phase 1 note material exists from quick task 260615-7dc.*
