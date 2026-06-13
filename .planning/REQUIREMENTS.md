# Requirements: GE Vernova Virtual Sensing — Interview Prep

**Defined:** 2026-06-13
**Core Value:** Juan walks into the interview able to connect his real experience to this role's exact requirements — and to the director's own patented work — with confidence and specifics.

> These "requirements" are study/prep deliverables. Each is "Complete" when the material
> exists, is accurate, and Juan can deliver it aloud under interview pressure.

## v1 Requirements

### Kalman & State Estimation (KAL) — Gap 1 (disqualifying if shallow)

- [ ] **KAL-01**: Notes explaining WLS / Gauss-Newton power-system state estimation in plain, interview-ready language
- [ ] **KAL-02**: Notes on the Kalman family progression KF → EKF → UKF (predict/update, Jacobian, sigma points)
- [ ] **KAL-03**: Worked line-temperature EKF example mapping the IEEE 738 conductor ODE to the predict step (Q/R tuning, innovation sequence, divergence detection)
- [ ] **KAL-04**: Hands-on Python EKF mini-demo estimating line temperature from current + weather telemetry

### Transmission Virtual Sensing (TVS) — Gap 2 (T&D vocabulary)

- [ ] **TVS-01**: Notes on voltage stability monitoring — P-V curve, voltage collapse, Thevenin-equivalent VSI from PMU data
- [ ] **TVS-02**: Notes on phase-angle / power-flow inference — DC approximation (P = Bθ), sparse PMU coverage problem
- [ ] **TVS-03**: Notes on observability analysis and bad-data detection (chi-squared test, normalized residual, leverage measurements)
- [ ] **TVS-04**: Notes on asset-health estimation — transformer hot-spot (IEEE C57.91), Dynamic Line Rating as a virtual-sensing product, RUL framing

### Director's Patents (PAT) — Gap 3 (highest differentiation)

- [ ] **PAT-01**: Deep-read summary of each of the four patents (adaptive power, asset portfolio, data management, OCR)
- [ ] **PAT-02**: One concrete connection per patent linking it to Juan's OSED/HEMS/SI-MAPPER work
- [ ] **PAT-03**: One sharp question per patent Juan can ask the director that demonstrates understanding

### Stack, Protocols & Architecture (STK) — Gaps 4, 6, 7

- [ ] **STK-01**: Notes on the grid protocol stack — SCADA, DNP3, PMU/C37.118, LoRa, MQTT — and where each lives
- [ ] **STK-02**: Notes on IEC 61850 (GOOSE vs. SV vs. MMS, three-tier hierarchy, logical nodes) at the depth needed to discuss it
- [ ] **STK-03**: Notes positioning NATS/JetStream vs. MQTT vs. Kafka vs. Pulsar, and K3s vs. K8s, with interview-ready justifications
- [ ] **STK-04**: Notes on Prometheus pull model vs. InfluxDB push, PromQL basics, kube-prometheus-stack
- [ ] **STK-05**: A whiteboard-able four-tier reference architecture (field → edge → fog/federated → cloud) Juan can draw and narrate

### Federated Architectures & Security (FED) — Gap 5

- [ ] **FED-01**: Notes distinguishing federated from distributed (the "no central coordinator" constraint), FedAvg vs. FedProx, non-IID client drift
- [ ] **FED-02**: Notes on Byzantine robustness (Krum / coordinate-wise median) and edge security (OTA integrity, TPM attestation, SPIFFE/SPIRE PKI)

### Reframe & Narrative Bridges (BRG)

- [ ] **BRG-01**: A rehearsed vocabulary-bridge table translating each OSED/HEMS/SI-MAPPER concept to its T&D analog
- [ ] **BRG-02**: A 10-minute OSED project pitch rewritten in GE Vernova vocabulary, outcome-first
- [ ] **BRG-03**: Three STAR behavioral stories (OSED build, HEMS PoC, big-data substation analysis) mapped to JD lines

### Q&A, Drills & Mock Interview (QNA)

- [ ] **QNA-01**: The 12 tough domain questions with strong, personalized answer keys, rehearsed aloud
- [ ] **QNA-02**: At least two full system-design drill walkthroughs (e.g., "virtual sensing pipeline for 500 substation edge nodes")
- [ ] **QNA-03**: A consolidated mock-interview question bank (technical + domain + behavioral) for final-day rehearsal

### Document Ingestion (DOC) — expandable

- [ ] **DOC-01**: A repeatable mechanism to ingest additional source documents Juan adds later and fold them into the study set (summaries + integration into relevant notes/Q&A)

## v2 Requirements

Deferred — useful but not worth the runway before this interview.

### Deeper Tooling (DEEP)

- **DEEP-01**: Hands-on NATS JetStream leaf-node demo (beyond conceptual notes)
- **DEEP-02**: Deeper IEEE 2030.5 (SEP 2.0) study beyond awareness level
- **DEEP-03**: Hands-on federated-learning demo with Flower (flwr)

## Out of Scope

| Feature | Reason |
|---------|--------|
| Learning Go or Rust | JD accepts "Python, Go, **or** Rust"; Python + TypeScript already qualifies |
| Building a production system | This is interview prep; demos are illustrative only |
| Generic software-engineering review | Juan is senior; prep targets this role's specifics |
| Deep EMT-tool mastery (PSCAD/RTDS/Opal-RT) | Preferred-only; awareness level given 1-week runway; defer to on-the-job collaboration |
| GE GridOS internal specifics | Public docs limited; speak to the open-standard layer (CIM/OpenFMB/IEC 61850) instead |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| DOC-01 | Phase 0: Document Ingestion | Pending |
| KAL-01 | Phase 1: Kalman & State Estimation | Pending |
| KAL-02 | Phase 1: Kalman & State Estimation | Pending |
| KAL-03 | Phase 1: Kalman & State Estimation | Pending |
| KAL-04 | Phase 1: Kalman & State Estimation | Pending |
| TVS-01 | Phase 2: Transmission Virtual Sensing | Pending |
| TVS-02 | Phase 2: Transmission Virtual Sensing | Pending |
| TVS-03 | Phase 2: Transmission Virtual Sensing | Pending |
| TVS-04 | Phase 2: Transmission Virtual Sensing | Pending |
| PAT-01 | Phase 3: Director's Patents Deep-Read | Pending |
| PAT-02 | Phase 3: Director's Patents Deep-Read | Pending |
| PAT-03 | Phase 3: Director's Patents Deep-Read | Pending |
| STK-01 | Phase 4: Protocols, Stack & Architecture | Pending |
| STK-02 | Phase 4: Protocols, Stack & Architecture | Pending |
| STK-03 | Phase 4: Protocols, Stack & Architecture | Pending |
| STK-04 | Phase 4: Protocols, Stack & Architecture | Pending |
| STK-05 | Phase 4: Protocols, Stack & Architecture | Pending |
| FED-01 | Phase 5: Federated Architectures & Security | Pending |
| FED-02 | Phase 5: Federated Architectures & Security | Pending |
| BRG-01 | Phase 6: Synthesis, Drills & Mock Interview | Pending |
| BRG-02 | Phase 6: Synthesis, Drills & Mock Interview | Pending |
| BRG-03 | Phase 6: Synthesis, Drills & Mock Interview | Pending |
| QNA-01 | Phase 6: Synthesis, Drills & Mock Interview | Pending |
| QNA-02 | Phase 6: Synthesis, Drills & Mock Interview | Pending |
| QNA-03 | Phase 6: Synthesis, Drills & Mock Interview | Pending |

**Coverage:**
- v1 requirements: 25 total
- Mapped to phases: 25/25
- Unmapped: 0

---
*Requirements defined: 2026-06-13*
*Last updated: 2026-06-13 — traceability populated by roadmapper*
