# Roadmap: GE Vernova Virtual Sensing — Interview Prep

## Overview

A 7-day crash sprint transforming Juan's gathered source material into interview-ready
knowledge. The sequence front-loads disqualifying gaps (Kalman/state estimation,
transmission virtual sensing, director's patents), builds outward to stack and federated
architecture, and finishes with synthesis and timed mock-interview drills. Every study
deliverable maps to exactly one phase; no requirement is orphaned.

## Phases

**Phase Numbering:**
- Integer phases (0–6): Planned study phases in execution order
- Decimal phases: Urgent insertions if needed (created via /gsd-insert-phase)

- [ ] **Phase 0: Document Ingestion** - Establish the repeatable mechanism for ingesting source documents into the study set so new material can be folded in throughout the sprint
- [ ] **Phase 1: Kalman & State Estimation** - Close Gap 1 (disqualifying): build EKF/UKF depth plus a working Python demo, anchored to the IEEE 738 DLR bridge story
- [ ] **Phase 2: Distribution Virtual Sensing** - Close Gap 2: distribution system state estimation (DSSE) under severe under-observability — the information-sourcing/fusion view, pseudo-measurements, forecasting-aided (Kalman) estimation, and virtual sensing as the ORACS observability index
- [x] **Phase 3: Director's Patents Deep-Read** - Close Gap 3 (highest differentiation): deep-read all six AGMS-family patents and prepare one connection and one question per patent (completed 2026-06-13)
- [x] **Phase 4: Protocols, Stack & Architecture** - Close Gaps 4, 6, 7: grid protocol stack (SCADA/DNP3/PMU/IEC 61850) plus NATS/Kafka/K3s/Prometheus positioning (completed 2026-06-14)
- [x] **Phase 5: Federated Architectures & Security** - Close Gap 5: distinguish federated from distributed, master FedAvg/FedProx/Krum, and frame edge security (completed 2026-06-14)
- [x] **Phase 6: Synthesis, Drills & Mock Interview** - Convert all knowledge to deliverable interview answers: vocabulary bridges, OSED pitch, STAR stories, system-design drills, timed Q&A rehearsal (completed 2026-06-16)
- [x] **Phase 7: Integrated HTML Study Site** - Consolidate all phase study notes and research HTML/diagram assets into one navigable HTML study site: AGMS architecture (patents), study notes, and demo explanations/references (completed 2026-06-15)
- [ ] **Phase 8: IEEE 33-Bus DER Measurement Source** - Build the re-runnable "ground-truth" System 1: radial balanced IEEE 33-bus network with renewable DER (solar+wind) + RPCs + feeder OLTC in PandaPower, driven by a 96-step (15-min) day whose profiles are ingested once from the open-power-system-data set into InfluxDB, with every full power-flow snapshot persisted to local InfluxDB and shown on a Grafana dashboard (Docker Compose) — infrastructure only, no virtual-sensing module yet (see 08-SPEC.md)

## Phase Details

### Phase 0: Document Ingestion
**Goal**: A repeatable document-ingestion mechanism exists so Juan can add source files at any point during the sprint and have them summarized and integrated into the relevant study notes
**Depends on**: Nothing (first phase)
**Requirements**: DOC-01
**Success Criteria** (what must be TRUE):
  1. Juan can drop a new PDF or text document into the project and run a defined command or workflow to produce a summary folded into the study set
  2. The mechanism is documented well enough to use without re-reading instructions each time
  3. At least one source document already in docs/ has been processed through the mechanism as a smoke test
**Plans**: TBD

### Phase 1: Kalman & State Estimation
**Goal**: Juan can explain the WLS → EKF → UKF progression fluently, work through the IEEE 738 line-temperature EKF example numerically, and demonstrate a running Python EKF mini-demo
**Depends on**: Phase 0
**Requirements**: KAL-01, KAL-02, KAL-03, KAL-04
**Success Criteria** (what must be TRUE):
  1. Juan can verbally explain WLS / Gauss-Newton power-system state estimation (objective function, iteration) in plain language without notes
  2. Juan can describe the KF predict/update equations, the EKF Jacobian linearization, and UKF sigma-point strategy — and say when to choose each
  3. Juan can map the IEEE 738 conductor thermal ODE to the EKF predict step, naming Q and R, explaining the innovation sequence, and describing divergence detection
  4. The Python EKF mini-demo runs and outputs a time-series ampacity estimate from simulated current + weather telemetry
**Plans**: 3 plans
- [x] 01-01-PLAN.md — KAL-01 WLS/Gauss-Newton notes + KAL-02 Kalman family (KF/EKF/UKF) notes
- [x] 01-02-PLAN.md — KAL-03 worked IEEE 738 line-temperature EKF example + building-RC bridge
- [x] 01-03-PLAN.md — KAL-04 from-scratch Python EKF mini-demo + README

### Phase 2: Distribution Virtual Sensing
**Goal**: Juan can explain distribution system state estimation (DSSE) under severe under-observability — the information-sourcing/fusion view, pseudo-measurements, forecasting-aided (Kalman/FASE) estimation, μPMUs, and how virtual sensing produces the ORACS observability index — in distribution vocabulary, invoking transmission state estimation only as explicit contrast
**Depends on**: Phase 1
**Requirements**: TVS-01, TVS-02, TVS-03, TVS-04
**Success Criteria** (what must be TRUE):
  1. Juan can explain P-V curve collapse, Thevenin-equivalent VSI from PMU data, and the operating margin concept — aloud, in under 3 minutes
  2. Juan can state the DC power-flow approximation (P = Bθ), describe the sparse PMU coverage problem, and frame angle inference as a WLS problem
  3. Juan can explain the chi-squared bad-data test, normalized residuals, leverage measurements as the critical limitation, and Jacobian rank as the observability check
  4. Juan can describe transformer hot-spot estimation (IEEE C57.91 ODE), DGA indicator gases, Dynamic Line Rating as a virtual-sensing product, and RUL framing — and explicitly connect each to an OSED analog
**Plans**: 3 plans
- [x] 02-01-PLAN.md — TVS-01 voltage-stability + TVS-02 DC power-flow angle-WLS notes
- [x] 02-02-PLAN.md — TVS-03 observability + bad-data + TVS-04 asset-health notes
- [x] 02-03-PLAN.md — 3-bus DC power-flow WLS + chi-squared bad-data detection demo

### Phase 3: Director's Patents Deep-Read
**Goal**: Juan has read all six director patents in the AGMS family, can articulate what each solves, and can make one concrete connection per patent to his own work and ask one sharp architecture-level question per patent in the interview
**Depends on**: Phase 2
**Requirements**: PAT-01, PAT-02, PAT-03
**Note**: REQUIREMENTS.md ("three patents") and the prior Goal text ("four … OCR") are stale; per CONTEXT.md D-01/D-02 the family is **six** distinct AGMS patents (`ocr.md` is the OCR duplicate of data-management, not a separate patent). Operation Loop Formation (US 12,596,341 B2) is GRANTED and assigned to GE Vernova — the keystone talking point.
**Success Criteria** (what must be TRUE):
  1. Juan can summarize each of the six AGMS patents (adaptive power / parent, logistician module, asset portfolio, operation loop formation ★, scout command, data management) in 2–3 sentences, identifying the core technical claim
  2. Juan can name one concrete parallel between each patent and his OSED / HEMS / SI-MAPPER work, phrased as a spoken connection — plus a closing unified "one assembly line = my stack" master narrative
  3. Juan has one prepared, director-directed, architecture-level question per patent that demonstrates understanding and invites a follow-on conversation — plus a ~90-second whole-family pitch
**Plans**: 1 plan
- [x] 03-01-PLAN.md — One consolidated AGMS patent rehearsal deck (six patents in pipeline order: summary + connection + question each; ~90s family pitch; closing master narrative)

### Phase 4: Protocols, Stack & Architecture
**Goal**: Juan can navigate the full grid protocol stack in conversation, justify stack choices (NATS vs. MQTT vs. Kafka, K3s vs. K8s, Prometheus vs. InfluxDB), and draw a four-tier reference architecture from memory
**Depends on**: Phase 3
**Requirements**: STK-01, STK-02, STK-03, STK-04, STK-05
**Success Criteria** (what must be TRUE):
  1. Juan can place SCADA, DNP3, PMU/C37.118, IEC 61850, and LoRa in the correct tier of the field-to-cloud stack and state one key property of each
  2. Juan can describe IEC 61850 GOOSE vs. SV vs. MMS, the three-tier hierarchy, and at least three logical node names without notes
  3. Juan can justify NATS JetStream vs. MQTT (and vs. Kafka) for the substation edge use case, and state the three key K3s-vs-K8s distinctions (air-gap, memory, etcd/SQLite)
  4. Juan can explain the Prometheus pull model vs. InfluxDB push, name a PromQL query, and say what kube-prometheus-stack adds
  5. Juan can draw and narrate the four-tier reference architecture (field → edge → fog/federated → cloud) on a whiteboard, including control-latency tiers and key components at each level
**Plans**: 3 plans
- [x] 04-01-PLAN.md — STK-01 grid protocol stack tier-map + STK-02 IEC 61850 (GOOSE/SV/MMS, logical nodes) notes
- [x] 04-02-PLAN.md — STK-03 NATS/MQTT/Kafka + K3s/K8s messaging-orchestration + STK-04 Prometheus/PromQL observability notes
- [x] 04-03-PLAN.md — STK-05 standalone four-tier reference-architecture doc (ASCII + Mermaid + narration + AGMS overlay)

### Phase 5: Federated Architectures & Security
**Goal**: Juan can precisely distinguish federated from distributed, explain FedAvg and FedProx, name the non-IID / client-drift failure mode, articulate Byzantine robustness, and frame edge security beyond "just TLS"
**Depends on**: Phase 4
**Requirements**: FED-01, FED-02
**Success Criteria** (what must be TRUE):
  1. Juan can state the "no central coordinator" constraint that distinguishes federated from distributed, explain FedAvg weight aggregation, and articulate why FedProx proximal regularization is needed when substations have non-IID load profiles
  2. Juan can explain coordinate-wise median / Krum Byzantine robustness, describe how gradient poisoning is detected, and name the gossip-vs-central-aggregation tradeoff
  3. Juan can describe OTA update integrity, TPM attestation, and SPIFFE/SPIRE PKI for edge identity — and connect each to a concrete grid threat
**Plans**: 3 plans
- [x] 05-01-PLAN.md — FED-01 federated-vs-distributed (FedAvg/FedProx/non-IID) + FED-02 byzantine-robustness (Krum/coord-median/gossip-vs-central) explain-why notes
- [x] 05-02-PLAN.md — FED-03 edge-security awareness note (OTA integrity / TPM attestation / SPIFFE-SPIRE, each tied to a grid threat)
- [x] 05-03-PLAN.md — NumPy-only FedAvg/FedProx/Krum/coord-median teaching demo + README

### Phase 6: Synthesis, Drills & Mock Interview
**Goal**: All accumulated knowledge is deliverable as verbal interview answers under pressure — vocabulary bridges rehearsed, OSED pitch in GE Vernova language, STAR stories mapped to JD lines, system-design drills walked through, and the full tough-question bank answered aloud
**Depends on**: Phase 5
**Requirements**: BRG-01, BRG-02, BRG-03, QNA-01, QNA-02, QNA-03
**Success Criteria** (what must be TRUE):
  1. The vocabulary-bridge table is complete and Juan can deliver each bridge sentence (OSED → GE Vernova analog) within 10 seconds of being prompted with the left-hand term
  2. Juan can deliver a 10-minute OSED project explanation using GE Vernova vocabulary, opening with deployed outcome, without reverting to PhD or distribution-side framing
  3. All three STAR stories (OSED build, HEMS PoC, big-data substation analysis) are written, mapped to JD lines, and rehearsed aloud to a 2-minute target each
  4. Juan can walk through at least two full system-design scenarios (including "500-node virtual sensing pipeline") using K3s, NATS, EKF engine, federated aggregator, and GitOps fleet management
  5. Juan has answered all 12 tough domain questions aloud, timed, and can identify the 2–3 questions that need additional rehearsal before the interview
**Plans**: 6 plans
- [x] 06-01-PLAN.md — PHONE-SCREEN.md: round-1 HR phone-screen pack (≤90 s pitch, fit narrative, TN/relocation/comp logistics, HR question set)
- [x] 06-02-PLAN.md — REFRAME.md: two-layer vocabulary bridges (Layer A plain / Layer B technical) + tiered OSED pitch
- [x] 06-03-PLAN.md — STAR-STORIES.md: four STAR stories (OSED, HEMS, big-data, SI-MAPPER→AGMS scouts), two versions each, JD-mapped
- [x] 06-04-PLAN.md — QUESTION-BANK.md: JD-bullet generator + 12 differentiator-weighted domain Qs + consolidated by-round bank
- [x] 06-05-PLAN.md — SYSTEM-DESIGN-DRILLS.md: two whiteboard drills (500-node pipeline; close-the-loop digital-twin → field validation)
- [x] 06-06-PLAN.md — REHEARSAL-TRACKER.md: flashcard tracker + written active-recall/spaced-repetition rehearsal protocol

### Phase 7: Integrated HTML Study Site
**Goal**: All study notes produced across the phases plus the research-stage HTML/diagram assets are consolidated into a single, navigable HTML study site — AGMS architecture (the patents), the study notes, and the demos (what each demo is, why it was built, and references) — so Juan can revise everything in one place
**Depends on**: Phase 6
**Requirements**: HTML-01, HTML-02, HTML-03, HTML-04, HTML-05, HTML-06, HTML-07 (defined in 07-SPEC.md)
**Success Criteria** (what must be TRUE):
  1. A single HTML entry point renders the AGMS architecture section (patent-derived), built from the existing patents research assets (AGMS-architecture.drawio/.svg/.png/.pdf)
  2. All phase study notes (Markdown across .planning/phases/*) are converted to HTML and reachable from a single navigation
  3. Each hands-on demo has a section explaining what it is, why it was created, and references/links to its code and README
  4. The site opens locally in a browser with working internal navigation between architecture, notes, and demos
**Plans**: 4 plans
  - [x] 07-01-PLAN.md — Build foundation: venv, build_site.py, shared CSS, vendored MathJax, convert all 15 notes (HTML-03, HTML-04)
  - [x] 07-02-PLAN.md — Architecture integration: copy research trio + sources + diagram, rewrite cross-links, diagram viewer (HTML-02)
  - [x] 07-03-PLAN.md — Card-grid hub + demos page with embedded key code and inline results (HTML-01, HTML-05)
  - [x] 07-04-PLAN.md — Publish-readiness: .nojekyll, robots/noindex, link-validation pass, PUBLISH.md, offline smoke check (HTML-06, HTML-07)

### Phase 8: IEEE 33-Bus DER Measurement Source
**Goal**: A re-runnable "ground-truth" measurement source exists — the radial, balanced enhanced IEEE 33-bus network with renewable DER (solar+wind at buses 18/22/25/33), RPC shunts at 18/33, and a feeder OLTC + phase shifter (per `.planning/research/articles/ieee33.pdf` / `case33.xlsx`) modeled in PandaPower, driven through a 96-step (15-minute) day whose load+solar+wind profiles are ingested once from the open-power-system-data 15-min set into InfluxDB and read back from there at run time, with the full power-flow state registered at every step, persisted to local InfluxDB, and visualized via a provisioned Grafana dashboard. This is **System 1** (the measurement source) in a two-system design; **System 2** (the virtual-sensing module that estimates state from the measurements) is explicitly OUT OF SCOPE and handled in a later phase. Decisions are locked in `08-SPEC.md` (ambiguity 0.13).
**Depends on**: Phase 7
**Requirements**: SPEC-1..SPEC-7 (locked in 08-SPEC.md)
**Success Criteria** (what must be TRUE):
  1. A PandaPower model of the radial balanced enhanced IEEE 33-bus system — renewable DG `sgen` at 18/22/25/33, RPC shunts at 18 (0.4 MVAr) & 33 (0.6 MVAr), feeder OLTC + phase shifter — runs a converging Newton-Raphson power flow from a single Python entry point
  2. The 15-min open-power-system-data profiles (DE load/solar/wind) are ingested once into InfluxDB (96 points/day); if the source is unreachable the step halts and notifies (no synthetic/xlsx fallback)
  3. A 96-step batch driver reads the profiles from InfluxDB (solar→subset, wind→subset of DG buses), runs one power flow per step, and captures the full system state at each step
  4. Each snapshot's full power-flow state (bus |V|/angle, line P/Q & loading, slack feed-in, DER output, OLTC tap, losses) is written to local InfluxDB started via Docker Compose
  5. A provisioned Grafana dashboard renders the 96-step evolution of the key variables without manual setup
  6. The runner is deterministic, repeatable, and documented (README) so the measurement set regenerates on demand
**Plans**: 5 plans
- [x] 08-01-PLAN.md — Scaffold (uv project + config) + infra-only Docker Compose (InfluxDB 2.9.1 + Grafana 11.6.15) + pin TARGET_DATE/DG-scaling (Wave 1)
- [x] 08-02-PLAN.md — pandapower enhanced IEEE 33-bus builder (DG + RPC shunts + series feeder OLTC) + Baran & Wu base-case validation (Wave 2)
- [x] 08-03-PLAN.md — InfluxDB helpers + one-time OPSD profile ingest (96 points; halt+notify, no fallback) + programmatic state bucket (Wave 2)
- [x] 08-04-PLAN.md — 96-step driver: read profiles from InfluxDB, OLTC-regulated power flow per step, full-state capture, persist + determinism check (Wave 3)
- [x] 08-05-PLAN.md — Grafana auto-provisioning (Flux datasource + SPEC-panel dashboard) + Makefile + README runbook + end-to-end human-verify checkpoint (Wave 4)

## Progress

**Execution Order:**
Phases execute in numeric order: 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 0. Document Ingestion | 0/TBD | Not started | - |
| 1. Kalman & State Estimation | 0/3 | Not started | - |
| 2. Distribution Virtual Sensing | 0/3 | Not started | - |
| 3. Director's Patents Deep-Read | 1/1 | Complete    | 2026-06-13 |
| 4. Protocols, Stack & Architecture | 3/3 | Complete   | 2026-06-14 |
| 5. Federated Architectures & Security | 3/3 | Complete   | 2026-06-14 |
| 6. Synthesis, Drills & Mock Interview | 6/6 | Complete    | 2026-06-16 |
| 7. Integrated HTML Study Site | 4/4 | Complete    | 2026-06-15 |
| 8. IEEE 33-Bus DER Measurement Source | 5/5 | Complete    | 2026-06-23 |

### Phase 08.1: System 1 fault and reconfiguration scenario (INSERTED)

**Goal:** Produce a separate, re-runnable, quasi-steady-state fault-and-reconfiguration dataset on the existing System 1 IEEE 33-bus model — replicating the article's Section-8 fault → isolate → tie-restore sequence as a 40-step (2-min @ 3-s), three-block window (pre_fault → faulted_isolated → restored) frozen at the evening-peak operating point, with full power-flow state plus topology/event metadata per snapshot, persisted to a dedicated `fault_event` InfluxDB bucket and its own provisioned Grafana dashboard — to stress-test the future System 2 estimator.
**Requirements**: SPEC-1..SPEC-10 (see 08.1-SPEC.md); decisions D-01..D-18 (see 08.1-CONTEXT.md)
**Depends on:** Phase 8
**Plans:** 2/4 plans executed

Plans:
- [x] 08.1-01-PLAN.md — Additive data-contract layer: fault constants + fault_event bucket in config.py, write_fault_step() in influx.py, fault-sim entry in pyproject.toml
- [x] 08.1-02-PLAN.md — The fault_sim.py runner: frozen evening-peak op-point, 40-step 3-block walk, fault/isolate/tie-restore, validation + determinism gates, console table
- [ ] 08.1-03-PLAN.md — Auto-provisioned Grafana dashboard ieee33-fault-event.json (SPEC-8 minimums + 4 D-13 extras) over the fault_event bucket
- [ ] 08.1-04-PLAN.md — README runbook (uv run fault-sim) + qualitative article-comparison note (SPEC-10)

### Phase 9: Measurement System (Observability Layer)

**Goal:** Build the **measurement layer** between System 1 (ground-truth behaviour) and the future System 2 (state estimator). It reads System 1's full ground-truth state from InfluxDB, applies a **config-driven sensor model** (which buses/lines are instrumented, with what measurement class), corrupts it with **config-selectable noise**, samples it at the configured **cadence**, and writes the resulting measurement set (`z` + assumed σ + topology/switch metadata + phase tag) to a **new dedicated `measurements` InfluxDB bucket** tagged by experiment + scenario — plus provisioned Grafana dashboards of the observed states. Its job is to **destroy information realistically** (manufacture under-observability), not pass state through faithfully — that is what makes virtual sensing necessary. This is the "Measurement System" in Juan's multi-system design: System 1 (behaviour) → **Measurement System (P9)** → System 2 (estimator) → System 3 (self-healing). Interview tie: the AGMS perception edge — Inspector scouts streaming observations as POV frames.

**Depends on:** Phase 8 (System 1 `state` bucket / 96-step day) **and Phase 8.1** (the `fault_event` bucket + its topology/event metadata schema — **must be frozen first; hard schema dependency**, schema still being finalized via /gsd-discuss-phase 8.1)
**Requirements**: TBD (run /gsd-spec-phase 9)

**Locked design decisions (from 2026-06-24 discussion):**
- **State formulation = NODE-VOLTAGE** (V magnitude + angle); branch-current is awareness-only. Matches all study material + ORACS-covariance framing, handles PMU angles + topology change cleanly, and pandapower ground truth is already node-voltage.
- **Config-driven knobs** (measurement-config, separate from System 1 config):
  - **(a) Sensor placement** — 2 presets: `well_observed` (feeder-head SCADA + DER telemetry + several μPMUs + broad AMI; redundancy > 1) and `realistic_sparse` (feeder-head SCADA + DER + 2–3 μPMUs + AMI on ~30% of loads, rest pseudo; redundancy borderline — **headline scenario**).
  - **(b) Experiment / data source** — switch between the **static day** (`state` bucket, 96 steps) and the **failure scenario** (`fault_event` bucket, 40 steps).
  - **(c) Sampling mode** — **both** built & fully functional: `snapshot` (one consistent set per timestamp) and `multirate_async` (per-class cadence: PMU fast / SCADA medium / AMI slow → patchwork of differently-aged measurements, FASE-ready).
  - **(d) Noise model** — 3 switchable: `gaussian` (white per-class %σ), `gaussian_outliers` (Gaussian + sparse gross errors → exercises bad-data detection), `instrument` (quantization + systematic bias + mild temporal correlation).
- **Measurement-class taxonomy** = design space: SCADA, μPMU (|V|+angle), AMI, DER telemetry, **zero-injection virtual** (P=Q=0 near-exact, very high weight — IEEE-33 has few natural ones, designate some), **pseudo-measurements** (load-forecast at unmetered buses, large σ; the System 1 load **profile** is the natural pseudo mean). Each measurement: `{type, location, value=true+noise, assumed_sigma, class, timestamp}`.
- **True σ vs assumed σ separable** in config (default equal) → enables later robustness-to-mis-specified-noise testing.
- **Topology/switch metadata published alongside z** (in-service status + phase tag + dead-bus set). Static day = fixed/known topology; failure case = propagate 8.1's `fault_event` metadata.
- **Scoring oracle kept SEPARATE** — measurement layer emits only `z` + topology + σ; ground truth stays in `state`/`fault_event` for later System-2-vs-System-1 comparison.
- **Grafana**: provisioned dashboards over `measurements` showing observed states — one for the static full-day scenario, one for the failure scenario (true-vs-measured overlay; observed-vs-pseudo footprint).
- **Determinism**: seeded noise. Reuse `system1-measurement-source/` repo, `uv`, the Docker InfluxDB+Grafana stack, `influx.py` helpers.

**Out of scope:** System 2 (estimator), System 3 (self-healing loop), live streaming transport (NATS / MQTT / C37.118-over-UDP — optional later afterthought), any change to System 1's day or the fault scenario physics.

**Plans:** 0 plans

Plans:
- [ ] TBD (run /gsd-spec-phase 9, then /gsd-plan-phase 9 to break down)
