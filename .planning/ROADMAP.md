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
- [ ] **Phase 2: Transmission Virtual Sensing** - Close Gap 2: acquire fluent T&D vocabulary covering voltage stability, phase angles, observability, bad-data detection, and asset health
- [x] **Phase 3: Director's Patents Deep-Read** - Close Gap 3 (highest differentiation): deep-read all six AGMS-family patents and prepare one connection and one question per patent (completed 2026-06-13)
- [x] **Phase 4: Protocols, Stack & Architecture** - Close Gaps 4, 6, 7: grid protocol stack (SCADA/DNP3/PMU/IEC 61850) plus NATS/Kafka/K3s/Prometheus positioning (completed 2026-06-14)
- [ ] **Phase 5: Federated Architectures & Security** - Close Gap 5: distinguish federated from distributed, master FedAvg/FedProx/Krum, and frame edge security
- [ ] **Phase 6: Synthesis, Drills & Mock Interview** - Convert all knowledge to deliverable interview answers: vocabulary bridges, OSED pitch, STAR stories, system-design drills, timed Q&A rehearsal

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

### Phase 2: Transmission Virtual Sensing
**Goal**: Juan can discuss voltage stability monitoring, phase-angle inference, observability analysis, bad-data detection, and asset-health estimation in T&D vocabulary without defaulting to distribution-side analogies
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
- [ ] 05-01-PLAN.md — FED-01 federated-vs-distributed (FedAvg/FedProx/non-IID) + FED-02 byzantine-robustness (Krum/coord-median/gossip-vs-central) explain-why notes
- [ ] 05-02-PLAN.md — FED-03 edge-security awareness note (OTA integrity / TPM attestation / SPIFFE-SPIRE, each tied to a grid threat)
- [ ] 05-03-PLAN.md — NumPy-only FedAvg/FedProx/Krum/coord-median teaching demo + README

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
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 0 → 1 → 2 → 3 → 4 → 5 → 6

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 0. Document Ingestion | 0/TBD | Not started | - |
| 1. Kalman & State Estimation | 0/3 | Not started | - |
| 2. Transmission Virtual Sensing | 0/3 | Not started | - |
| 3. Director's Patents Deep-Read | 1/1 | Complete    | 2026-06-13 |
| 4. Protocols, Stack & Architecture | 3/3 | Complete   | 2026-06-14 |
| 5. Federated Architectures & Security | 0/3 | Planned | - |
| 6. Synthesis, Drills & Mock Interview | 0/TBD | Not started | - |
</content>
