# Project Research Summary

**Project:** GE Vernova Virtual Sensing & Decentralized Grid Operations — Interview Prep
**Domain:** Edge-native grid virtual sensing, decentralized operations, transmission-side state estimation
**Researched:** 2026-06-13
**Confidence:** HIGH (core grid physics, Kalman, protocols) | MEDIUM (GE Vernova internals, federated patterns)

---

## Executive Summary

This project prepares Juan Carlos Oviedo Cepeda for a Senior Software Engineer & Scientist
interview at GE Vernova (CTO org, Electrification Chief Architect's team) in approximately
one week. The role sits squarely at the intersection of edge ML, control theory, and power
systems — and Juan's OSED platform at Hydro-Québec already implements the same
architectural pattern (edge inference, federated control, real-time telemetry pipelines) at
the building/DER layer. The core prep task is not to learn a new discipline; it is to
**reframe proven work in transmission-grid vocabulary** and **close three named technical
gaps** (Kalman filters, transmission-side virtual sensing, and the director's patents).

The research confirms that GE Vernova's target architecture is a four-tier edge-native
system: field IEDs/PMUs → protocol-adapter edge node (K3s, NATS, Kalman engine) →
regional federated aggregator → cloud digital twin / GridOS. Juan's OSED maps to this
almost component-by-component: his buildings are their substations, his MQTT pipelines are
their NATS leaf nodes, his RC thermal estimator is their IEEE 738 conductor model, his
CVXPY optimization dispatch is their decentralized MPC. The highest-yield study moves are
therefore precision bridging (building the exact translation sentences) plus targeted depth
on EKF/UKF and transmission-specific quantities (voltage stability, phase angles, DLR).

The single highest-risk interview moment is being asked to "walk through a Kalman filter
applied to a grid problem" without sufficient EKF/UKF depth. The single highest-reward
moment is connecting the building RC thermal model to the IEEE 738 conductor temperature
ODE — an exact structural analogy that almost no candidate will have. The recommended
study sequence front-loads Kalman and DLR/phase-angle material, then builds outward to
protocols, federated patterns, and the director's patents, finishing with system-design
drills and behavioral story refinement.

---

## Key Findings

### Recommended Stack (from STACK.md)

Juan's existing stack (Python, FastAPI, Kubernetes, MQTT, Modbus, InfluxDB, TimescaleDB,
gRPC, Redis, CVXPY, Grafana, Databricks) already satisfies the role's core requirements.
The gaps are tooling-layer additions, not replacements. One-week priority order:
NATS/JetStream > K3s nuances > DNP3/PMU/SCADA concepts > Prometheus pull model >
Federated patterns > Pulsar awareness.

**Core technologies (gaps only — reframe, do not re-study the rest):**
- **NATS JetStream**: edge messaging backbone — MQTT for devices, NATS for federated
  substation-to-cloud pipelines; leaf-node topology enables autonomy during WAN outages.
- **K3s 1.31**: lightweight Kubernetes for substation edge nodes — identical API to Juan's
  existing K8s; key differences are air-gap operation, embedded SQLite/etcd, less than 512 MB RAM.
- **Apache Kafka 4.2**: cloud-tier stream aggregation from hundreds of substations; too
  heavy for edge (JVM), lives above NATS in the data path.
- **DNP3**: utility-SCADA protocol — Modbus with millisecond timestamps, unsolicited
  push, and SAv5 security; lingua franca for substation RTU communication.
- **PMUs / IEEE C37.118**: 30-120 Hz synchrophasor source; enables Kalman-based dynamic
  state estimation that SCADA's 4-second scan rate cannot support.
- **Prometheus**: K8s-native pull-scrape metrics layer feeding Juan's existing Grafana;
  adds automatic pod discovery that InfluxDB push model lacks.
- **Flower (flwr)**: federated learning framework; each substation trains locally, shares
  weight deltas only — no raw measurement leaves the utility fence.

### Knowledge Domain Map (from FEATURES.md)

**Table stakes — disqualifying if missing:**
- Power system state estimation (WLS / Gauss-Newton) — conceptual parent of all virtual
  sensing; Juan's least-squares MPC covers this with vocabulary translation.
- Kalman filter family (KF -> EKF -> UKF) — explicitly named in JD; Gap 1; needs hands-on.
- PMUs and synchrophasors — primary measurement source for transmission virtual sensing.
- Voltage stability monitoring (P-V curve, VSI, Thevenin equivalent from PMU data).
- Phase angle and power flow inference (DC approximation, sparse PMU coverage problem).
- Dynamic Line Rating — IEEE 738 ODE; the strongest bridge story to Juan's building RC model.
- Asset health estimation — transformer hot-spot (IEEE C57.91), RUL; edge ML pattern
  Juan already has; quick reframe.
- SCADA / DNP3 / LoRa / MQTT protocol stack — table stakes for "integrate field data."
- Edge-native decentralized architecture — K3s / NATS / InfluxDB; OSED IS this pattern.

**Differentiators — depth sets Juan apart:**
- Federated learning for grids (FedProx for non-IID data; Byzantine robustness via Krum).
- Signal processing for PMU waveforms (DFT to phasor, ROCOF, Kalman-based frequency estimation).
- Digital twins / OpenFMB / CIM graph — Juan's knowledge-graph work bridges here directly.
- Observability analysis and bad data detection (chi-squared test; leverage measurements).

**Awareness-only (one sentence each):**
- IEEE 2030.5 (SEP 2.0), EMT tools (PSCAD/RTDS/Opal-RT), TSO vs. DSO, particle filters,
  GNNs for grid SE, WAPC/UVLS/UFLS protection schemes.

### Architecture Approach (from ARCHITECTURE.md)

The canonical architecture is a four-tier edge-native system with strict north-south data
flow and east-west peer coordination at the edge tier — no central coordinator required in
real-time. Juan's OSED maps to this tier-for-tier; the vocabulary translation is the work.

**Major components:**
1. **Protocol Adapter (edge)** — ingests DNP3 / IEC 61850 GOOSE+MMS / Modbus / MQTT from
   field IEDs; normalizes to CIM/OpenFMB schema; Juan's BACnet/Modbus adapter is the analog.
2. **Virtual Sensing Engine (edge)** — EKF/UKF predict-update loop using AC power-flow
   equations or IEEE 738 thermal ODE as the physics model; outputs V, theta, T_line, health
   score; Juan's RC-thermal estimator in OSED is the structural analog.
3. **Local NATS broker + JetStream (edge)** — pub/sub fanout to control logic and uplink;
   store-and-forward during WAN outage; replaces Juan's MQTT broker for federated contexts.
4. **K3s orchestrator (edge)** — container lifecycle, rolling updates, air-gap capable;
   Juan's Kubernetes skills transfer directly; K3s = K8s on a diet.
5. **Federated Aggregator (fog/regional)** — collects model-weight deltas via Flower FedAvg;
   no raw measurements leave the substation; Juan's OSED privacy isolation is the pattern.
6. **Cloud Digital Twin + GridOS (cloud)** — Modelica / OpenFMB graph continuously
   calibrated by field residuals; Juan's SI-MAPPER knowledge-graph work is the bridge.
7. **Fleet Management (cloud)** — GitOps (ArgoCD) config push; SPIFFE/SPIRE PKI; analogous
   to Juan's Kubernetes CI/CD pipelines.

**Key architectural patterns to cite:**
- Adapter-Bus-Engine separation (swap protocol driver without touching sensing logic).
- Store-and-forward with offline resilience (edge operates autonomously during WAN loss).
- Shadow mode before closed loop (virtual sensor runs parallel to SCADA; validate residuals
  before promoting to control path) — the sim-to-field validation ladder.
- Three-tier control latency: protection (<4 ms, dedicated IEDs only), control-class
  (100 ms-1 s, edge K3s with PREEMPT_RT), advisory (seconds-minutes, standard software).

### Critical Pitfalls (from PITFALLS.md — top 6 for the interview)

1. **Kalman without depth** — saying "I'm familiar with Kalman" then failing EKF/UKF
   follow-ups. Avoid: know one worked grid example cold (line-temp EKF with IEEE 738 ODE);
   be ready to name Q, R, innovation sequence, and divergence detection.
2. **Distribution vocabulary in a transmission conversation** — launching into HEMS and
   HVAC Modbus when asked about PMU state estimation. Avoid: pre-build explicit vocabulary
   bridges; always anchor with "my work is distribution/DER side — here is the T&D analog."
3. **"Federated" = "distributed"** — missing the "no central coordinator" constraint and the
   non-IID / client-drift problem. Avoid: explain FedProx proximal regularization and
   coordinate-wise median (Krum) Byzantine robustness.
4. **Ignoring time synchronization** — proposing to resample PMU and SCADA without
   discussing GPS spoofing, 1 ms clock error = 21 degrees phase angle error, and
   cross-validation via SCADA-independent frequency readings.
5. **Virtual sensor topology overfitting** — describing ML validation only with held-out
   test accuracy; missing physics consistency checks, innovation sequence monitoring, and
   triggered re-calibration on topology change events.
6. **Cloud-software answer to hard-real-time question** — applying SLA/retry thinking to
   protection-class latency. Avoid: explicitly partition into the three-tier control model;
   never route trip logic through a Kubernetes pod.

---

## Strongest Reframe Bridges

These are the highest-leverage talking points. Prepare each as a two-sentence pivot.

| Juan's Work | GE Vernova Analog | Bridge Sentence |
|-------------|-------------------|-----------------|
| Building RC thermal model (C*dT/dt = Q - UA*(T-Tamb)) | IEEE 738 conductor thermal ODE (m*c*dT_c/dt = I^2*R - q_conv - q_rad + q_solar) | "My building thermal estimator and IEEE 738 DLR share identical ODE structure — first-order thermal system, hidden temperature state, physics predict + measurement update. I swap building parameters for ACSR conductor parameters." |
| OSED edge ML thermal state estimation | Virtual sensing engine (EKF on grid state) | "OSED infers building thermal state from noisy sensors plus a physics model — that IS a virtual sensor. The grid version uses the same predict-update structure with power-flow equations instead of an RC model." |
| MQTT pub/sub broker topology (OSED) | NATS leaf-node federated pipeline | "I've shipped production MQTT pipelines for DER control; NATS adds JetStream durability and leaf-node autonomy during WAN loss — the architectural step I'd take for substation-scale federation." |
| Convex optimization (CVXPY) cloud formulate / edge execute | Decentralized MPC for reactive power scheduling | "My OSED dispatch layer uses cloud convex optimization pushing setpoints executed locally — exactly the hierarchical MPC pattern the JD describes for substation Volt-VAR control." |
| SI-MAPPER knowledge graph (ASHRAE 223P ontology) | CIM graph (IEC 61968/61970) for grid topology | "CIM for power systems is the same ontology pattern I implemented in SI-MAPPER for buildings — graph nodes are buses/assets, edges are lines/transformers, same semantic modeling discipline." |
| HEMS / DER dispatch (OpenADR) | DER-grid interface (IEEE 2030.5, voltage support) | "My HEMS work used OpenADR for demand response dispatch; IEEE 2030.5 extends that to direct inverter control — I understand the model and can close the gap quickly." |
| Databricks/PySpark on billions of substation points | SCADA historian analytics / PMU data pipeline | "I've already processed Hydro-Quebec substation historian data at scale — the difference is adding 30 Hz PMU protocol integration upstream of the analytics layer." |
| K8s, gRPC, InfluxDB, Grafana (OSED) | K3s, gRPC, InfluxDB, Prometheus+Grafana (JD) | "Same stack; K3s is K8s on a diet for air-gapped field hardware; Prometheus adds the pull-scrape layer I've been handling with InfluxDB push — a one-sprint gap." |

---

## Implications for Roadmap (Suggested Study Phases)

### Phase 1: Kalman and State Estimation Foundation (Days 1-2)
**Rationale:** Gap 1; named explicitly in JD; disqualifying if shallow; unlocks all other
virtual sensing conversations; strongest bridge story (building RC -> IEEE 738 DLR) lives here.
**Delivers:** Can explain WLS -> EKF -> UKF progression; work through line-temperature
EKF example numerically; know Q/R tuning, innovation sequence, divergence detection.
**Study tasks:**
- WLS state estimation objective and Gauss-Newton iteration (1 hr reading)
- KF predict-update equations; EKF Jacobian; UKF sigma points (2 hr — go deep)
- IEEE 738 conductor thermal ODE -> map to EKF predict step (1 hr)
- Dynamic Line Rating: DLR product context, virtual sensing angle, ampacity output (1 hr)
- Kalman hands-on: implement EKF for line-temp estimation from current + weather (2 hr mini-demo)
**Pitfalls to avoid:** Pitfall 1 (shallow Kalman claim); Pitfall 9 (pure ML without physics)

### Phase 2: Distribution Virtual Sensing — The T&D Gap (Days 2-3)
**Rationale:** Gap 2; without this Juan speaks only distribution vocabulary in a T&D interview;
phase angle and voltage stability are the first two named targets in the JD.
**Delivers:** Fluent explanation of voltage stability (P-V curve, Thevenin VSI), phase angle
inference (DC power flow, sparse PMU coverage problem), and asset health (IEEE C57.91);
explicit vocabulary bridge table mapped and rehearsed.
**Study tasks:**
- P-V curve and voltage collapse; Thevenin equivalent VSI from PMU data (1.5 hr)
- DC power flow approximation: P = B*theta; sparse angle inference as WLS problem (1 hr)
- Observability analysis: Jacobian rank check; observable islands; pseudo-measurements (1 hr)
- Bad data detection: chi-squared test, normalized residual, leverage measurements (1 hr)
- Asset health: IEEE C57.91 transformer hot-spot ODE; DGA indicator gases; RUL framing (1 hr)
- Vocabulary bridge practice: for each OSED/HEMS concept, say the T&D analog aloud (1 hr)
**Pitfalls to avoid:** Pitfall 2 (distribution vocabulary in T&D conversation); Pitfall 10
(observability as hard mathematical constraint, not just sensor count)

### Phase 3: Director's Patents Deep-Read (Day 3)
**Rationale:** Gap 3; highest-differentiation signal; no other candidate will have done this;
enables directing the conversation toward the lab's own research agenda.
**Delivers:** One concrete connection per patent to Juan's own work; one question per patent
ready to ask; ability to say "in your adaptive-power patent, you handle X — I faced a parallel
challenge in OSED when..."
**Study tasks:**
- Read all four patents (adaptive power, asset portfolio, data management, OCR) (3-4 hr)
- Map each patent to a Juan OSED/HEMS analog (1 hr)
- Draft one question per patent that shows you understood it and connects to your work (1 hr)
**Pitfalls to avoid:** Trap D (unfamiliar with director's published work)

### Phase 4: Protocols, Stack, and Architecture (Days 4-5)
**Rationale:** Gaps 4, 6, 7; SCADA/PMU/DNP3 are "integrate field data sources" table stakes;
NATS/Kafka/K3s are the JD's named stack items; needs enough depth to answer stack-choice
questions credibly without over-investing in protocol internals.
**Delivers:** Can explain SCADA/PMU/DNP3/LoRa protocol stack and where each lives; can
justify NATS vs. MQTT vs. Kafka decision; K3s vs. K8s distinctions memorized.
**Study tasks:**
- Grid protocol stack mental model: field layer -> substation (DNP3/IEC 61850) -> SCADA ->
  PMU/C37.118 -> PDC (1.5 hr)
- DNP3: master/outstation model, object groups, unsolicited reporting (1 hr)
- IEC 61850: GOOSE vs. SV vs. MMS; three-tier hierarchy; Logical Node vocabulary (1 hr)
- PMU: C37.118 frame, GPS sync, PDC aggregation, virtual PMU concept (1 hr)
- NATS JetStream: leaf node, subject hierarchy, store-and-forward (1 hr + quick demo)
- K3s nuances vs. K8s: SQLite/etcd, air-gap, single binary, Helm compatibility (30 min)
- Prometheus: pull model vs. InfluxDB push; PromQL basics; kube-prometheus-stack (1 hr)
**Pitfalls to avoid:** Pitfall 6 (GOOSE vs. DNP3 confusion); Pitfall 7 (MQTT for everything)

### Phase 5: Federated Architectures and Security (Day 5)
**Rationale:** Gap 5; JD's "federated, no central coordination" is precise; non-IID and
Byzantine resilience questions will come if federated is claimed as a strength.
**Delivers:** Can distinguish federated from distributed; explain FedAvg vs. FedProx;
name the non-IID/client-drift failure mode; articulate Byzantine robustness (Krum).
**Study tasks:**
- FedAvg algorithm; Flower (flwr) API shape — know the NumPyClient pattern (1 hr)
- FedProx proximal regularization; client drift in grid context (substations have
  different load profiles — the non-IID problem) (1 hr)
- Byzantine robustness: coordinate-wise median / Krum; gossip vs. central aggregation (1 hr)
- Edge security: OTA update integrity, TPM attestation, SPIFFE/SPIRE PKI,
  gradient poisoning detection (1 hr)
**Pitfalls to avoid:** Pitfall 3 (federated = distributed); Pitfall 4 (GPS spoofing and
time sync); Pitfall 8 (edge security reduced to "just TLS")

### Phase 6: System Design Drills and Behavioral Story Refinement (Days 6-7)
**Rationale:** The interview's medium — all technical knowledge must be deliverable as
verbal answers under pressure; behavioral stories need GE Vernova vocabulary baked in.
**Delivers:** Fluent answers to all 12 tough questions from PITFALLS.md; OSED elevator
pitch in GE Vernova language; three STAR stories mapped to JD lines.
**Study tasks:**
- Work through the 12 tough interview questions (PITFALLS.md) aloud, timed (3 hr)
- Rehearse the OSED 10-minute explanation using GE Vernova vocabulary (Q7 structure) (1 hr)
- Draft STAR stories: OSED platform build, HEMS PoC, Databricks big-data analysis (1.5 hr)
- Rewrite each story to open with deployed outcome, not the research/PhD framing (1 hr)
- System design drill: "Design a virtual sensing pipeline for 500 substation edge nodes"
  — answer using K3s, NATS, EKF engine, federated aggregator, GitOps fleet (2 hr)
**Pitfalls to avoid:** Trap A (building vocabulary in T&D question); Trap B (shallow Kalman);
Trap C (leading with PhD rather than production impact); Pitfall 11 (cloud SLA vs. real-time)

---

## Day-by-Day Study Sequence

| Day | Morning (3-4 hr) | Afternoon (3-4 hr) | Evening (1 hr) |
|-----|------------------|--------------------|----------------|
| 1 | WLS state estimation + KF/EKF/UKF theory | IEEE 738 DLR -> EKF worked example | Write out bridge: RC model vs conductor ODE |
| 2 | Kalman mini-demo (Python EKF for line temp) | Voltage stability: P-V curve, Thevenin VSI | Observability + bad data detection |
| 3 | Phase angle inference + DC power flow | Director's patents (read 2) | Director's patents (read 2) + connection mapping |
| 4 | Patents: connections + questions drafted | DNP3 / IEC 61850 / PMU / LoRa protocols | NATS JetStream leaf-node + K3s nuances |
| 5 | Prometheus + Kafka positioning | Federated learning (FedAvg, FedProx, Krum) | Edge security (OTA, TPM, SPIFFE) |
| 6 | System design drills (x2 full scenarios) | Q7 OSED pitch in GE Vernova vocabulary | STAR stories drafted |
| 7 | Tough questions Q1-Q6 timed rehearsal | Tough questions Q7-Q12 timed rehearsal | Rest + light review of vocabulary bridges |

---

## Top Tough Questions to Be Ready For

Ordered by expected frequency and difficulty (full answer keys in PITFALLS.md):

1. **Q1** — Design a virtual sensor to estimate real-time line temperature from PMU current
   and weather telemetry. (The IEEE 738 EKF question — must answer with physics ODE, EKF
   predict/update, DLR output, failure modes.)
2. **Q3** — Explain the chi-squared test for bad data detection and its limitations.
   (Leverage measurements are the critical limitation most candidates miss.)
3. **Q2** — Federated node injects adversarial gradients — detect and mitigate without a
   central coordinator. (Krum / coordinate-wise median; TPM attestation; blast-radius isolation.)
4. **Q7** — 10 minutes, explain your most relevant project to the Chief Architect.
   (OSED in GE Vernova language; outcome-first; vocabulary bridges pre-loaded.)
5. **Q4** — Architect a decentralized pipeline for 500 edge nodes that operates during WAN
   outages. (NATS leaf nodes + JetStream; Kafka at aggregation tier; CRDT for config; mTLS.)
6. **Q10** — Physics-informed ML vs. pure data-driven for voltage stability margin.
   (PINNs; operator explainability; hybrid Kalman-predict + ML-update.)
7. **Q11** — 4 GB RAM / 2 cores: partition K3s agent, NATS, EKF at 30 Hz, and FL training.
   (SCHED_FIFO for EKF; SCHED_BATCH for FL; JetStream less than 50 MB; K3s hard limit 512 MB.)
8. **Q9** — What is Dynamic Line Rating and how would you implement it as a virtual sensor?
   (IEEE 738; EKF; static vs. dynamic capacity; wind sparsity failure mode; 10-40% gain.)

---

## Confidence Assessment

| Area | Confidence | Notes |
|------|------------|-------|
| Stack / Technology Gaps | HIGH | NATS/Kafka/K3s/Prometheus verified against official docs; DNP3 and PMU against IEEE standards and utility references |
| Knowledge Domain Map | HIGH | Core concepts (WLS, KF/EKF, PMU, DLR, VSI) verified against IEEE standards and academic papers (arXiv 2012.06069, IEEE C37.118, IEEE 738) |
| Architecture Approach | MEDIUM-HIGH | Four-tier pattern verified via IEC 61850, OpenFMB, GE GridOS public material; GE Vernova internal specifics inferred from JD + public patents |
| Pitfalls / Interview Q&A | HIGH | Failure modes verified against peer-reviewed sources; GPS spoofing against arXiv 2206.12440; FL adversarial against Frontiers AI 2025 |
| Director's Patents | MEDIUM | Patent documents in hand in docs/; GE Vernova lab context inferred; content needs direct reading in Phase 3 |

**Overall confidence:** HIGH for study direction and bridge stories; MEDIUM for GE Vernova-specific internal architecture details (not blocking — study material is sufficient for interview depth).

### Gaps to Address

- **Director's patents specifics**: require direct reading (docs are in `docs/`); content
  cannot be synthesized without reading them; this is Phase 3's entire focus.
- **Juan's Kalman hands-on experience**: the weakest gap — a mini-demo Python EKF
  implementation during Day 1-2 is critical to converting textbook knowledge to claimed
  experience. Do not skip.
- **Exact GE GridOS data model**: public documentation is limited; avoid specific claims
  about GridOS internals; speak to the open-standard layer (CIM, OpenFMB, IEC 61850)
  that GridOS sits on top of.
- **EMT tool HIL/SIL depth**: genuine gap; covered at awareness level per PROJECT.md
  scope decision; if asked, acknowledge "I'd collaborate with the power-systems modeling
  team for PSCAD validation while owning the algorithm and integration layer."

---

## Sources

### Primary (HIGH confidence)
- IEEE 738: Standard for Calculating the Current-Temperature Relationship of Bare Overhead Conductors
- IEEE C37.118.1: Standard for Synchrophasor Measurements for Power Systems
- ArXiv 2012.06069: "Power System Dynamic State Estimation Using Extended and Unscented Kalman Filters"
- GE Vernova Job Description R5043890 — docs/job-requirements.md
- NATS docs (docs.nats.io) — NATS vs. Kafka/MQTT comparison
- Apache Kafka release blog — v4.2.0 (Feb 2026), KRaft mode
- Flower framework docs (flower.ai) — v1.25 federated learning API
- Prometheus docs / kube-prometheus-stack — pull model, PromQL

### Secondary (MEDIUM confidence)
- IEC 61850 architecture: EMQ blog, OPAL-RT testing guide, MDPI Sensors 2021
- OpenFMB edge node architecture: ORNL microgrid communications, SEPA article
- GE GridOS public product pages — federated architecture inference
- PMU/SCADA fusion state estimation: MDPI Energies 17(11) 2024
- Federated learning for grids: Nature Comm. Engineering 2024, Frontiers AI 2025
- GPS spoofing of PMUs: arXiv 2206.12440; IEEE Xplore 9127471
- K3s vs. K8s: SUSE documentation, CloudOptimo comparison

### Tertiary (LOW confidence — awareness only)
- PSCAD/RTDS/Opal-RT: product pages; no hands-on access during prep
- GE Vernova lab-internal architecture specifics: inferred from JD + public patents only
- Director's patent technical content: to be read directly from docs/ during Phase 3

---
*Research completed: 2026-06-13*
*Ready for roadmap: yes*
