**For:** Final-day rehearsal before rounds 1–4 of the GE Vernova Senior Software Engineer & Scientist interview (req R5043890)
**Purpose:** Single source of truth for every interview question — Part A generates questions from JD responsibility bullets (D-09), Part B presents 12 differentiator-weighted domain questions with say-aloud-derived answer keys (QNA-01, D-10), Part C is the consolidated round-and-category rehearsal index (QNA-03, D-11).

---

> **Note style (D-15):** Round-tagged questions, oral-rehearsal format, selective LaTeX only in Part B technical answer keys (rounds 2–4 material). Screen material (Part A behavioral + Part C Round 1) is plain-language only — no equations, no acronyms a non-engineer wouldn't know.
>
> **Source discipline (D-16):** No new technical content. All answer keys are extracted and tightened from the Phase 1–5 say-aloud tracks. If an answer key cites a note path, that note is the source — verify before deviating.

---

## 0. How This Bank Works

### Round Tags

| Tag | Meaning | Audience |
|-----|---------|----------|
| 🟢 Round 1 (HR screen) | Plain-language; no jargon or equations | Non-technical HR screener |
| 🔵 Rounds 2–4 (Technical) | Domain depth; equations permitted in answer keys | Director, engineering panel |
| 🟣 Any round (Behavioral) | STAR-structured; plain screen version + technical STAR version available | HR screener or technical interviewer |

### Cross-Document Map

| Document | What lives there | Cross-reference |
|----------|-----------------|----------------|
| PHONE-SCREEN.md | Full round-1 logistics scripts (TN, relocation, comp, "tell me about yourself") | → Round 1 section of Part C |
| REFRAME.md | Vocabulary bridges (Layer A HR plain-language + Layer B technical tool bridges) | → All rounds: know your bridge for each JD term |
| STAR-STORIES.md | 4 STAR stories with screen + technical versions, JD-line mappings | → Behavioral Qs in Part A and Part C |
| SYSTEM-DESIGN-DRILLS.md | 2 system-design drills (ASCII whiteboard + narration) | → Rounds 3–4 in Part C |

---

## Part A — JD-Bullet Question Generator (D-09)

> Generated from the 13 JD bullets across 4 groups. Each bullet produces a behavioral question (🟣/🟢, screen-or-behavioral), a situational question (🔵, technical round), and a CV anchor.
>
> **How to use:** When the screener or interviewer asks a behavioral question, find the closest bullet below, note the CV anchor, and answer with the STAR story referenced. When a technical interviewer asks a situational question, use the situational framing plus the domain knowledge from Part B.

---

### Edge Engineering & Data Pipelines

#### Bullet 1: Build and deploy edge-native software components for decentralized operation, sensing, and control

**🟣 Behavioral:** Tell me about a time when you built and deployed software that had to run autonomously on field hardware, not in a central data center.

> **CV anchor:** OSED — built the cloud-edge platform that runs grid services on live Hydro-Québec field nodes; K8s-orchestrated, MQTT-connected, local ML inference, −21% energy-cost outcome. → See STAR-STORIES.md Story 1.

**🔵 Situational:** How would you architect a software component that must run edge-natively on a resource-constrained substation node, operate in island mode when WAN connectivity drops, and still coordinate with a cloud aggregator when it reconnects?

> **CV anchor:** OSED edge runtime (Python, FastAPI, K8s/K3s orchestration); NATS JetStream for durable replay in island mode (STK-03). Framing: K3s for orchestration (~512 MB RAM vs 2–4 GB for full K8s), NATS JetStream for messaging (persists messages to disk; replays on reconnect), local EKF inference, covariance-gated control dispatch.

---

#### Bullet 2: Develop federated data pipelines that allow distributed nodes to collaborate securely without central coordination

**🟣 Behavioral:** Tell me about a time when you designed a system where multiple distributed nodes had to exchange information without routing everything through a central server.

> **CV anchor:** OSED distributed edge inference — each DER node makes local control decisions without cloud round-trip. SI-MAPPER distributed ontology inference (heterogeneous signals, no central data pool). → See STAR-STORIES.md Story 4.

**🔵 Situational:** How would you design a federated data pipeline where each substation node processes its own telemetry locally and shares only lightweight summaries (not raw streams) with a regional aggregator?

> **CV anchor:** FED-01 federated architecture (weights not raw data; FedAvg aggregation); DSSE-04 federated DSSE (boundary-node posterior exchange, raw measurements never cross cell boundary); NATS JetStream leaf-node topology for edge-to-cloud relay without VPN.

---

#### Bullet 3: Integrate field data sources (SCADA, PMUs, DER controllers) and industrial IoT protocols (LoRa, MQTT, DNP3, Modbus)

**🟢 Behavioral:** Tell me about a time when you had to bring together data from several different field devices or protocols that were not designed to talk to each other.

> **CV anchor:** OSED — integrated MQTT, Modbus, BACnet, Zigbee, OpenADR across heterogeneous building/DER devices. Big-data substation analysis: billions of data points across substations via Databricks/PySpark. → See STAR-STORIES.md Story 3.

**🔵 Situational:** How would you approach integrating a SCADA head-end SCADA flow, PMU synchrophasor streams, and smart-inverter IEEE 2030.5 self-reports into a single distribution state estimation pipeline with honest uncertainty characterization for each source?

> **CV anchor:** DSSE-01 information-budget model (each source gets an honest covariance $R$; head SCADA via Kirchhoff $H$, inverter self-reports with small $R$, AMI with large $R$, delayed). KAL-03 multi-rate measurement fusion (three channels at different rates). Protocol bridge: Modbus → DNP3 (adds timestamps + unsolicited push); MQTT → NATS (adds durable replay); STK-01 protocol-stack awareness.

---

### Virtual Sensing & Control

#### Bullet 4: Develop and deploy robust virtual sensing algorithms to infer critical power grid parameters from limited edge sensor data

**🟣 Behavioral:** Tell me about a time when you built a system that had to infer or estimate a value at a location where you had no direct sensor.

> **CV anchor:** OSED/HEMS edge-ML load/PV forecasting — probabilistic inference of future load from historical patterns + current signals, used to drive MPC decisions at unmetered timepoints. → See STAR-STORIES.md Story 2.

**🔵 Situational:** How would you design a virtual sensing algorithm to estimate voltage at an unmetered distribution node using only the feeder-head SCADA flow, a handful of smart-inverter self-reports, and a delayed AMI reading, with calibrated uncertainty at each step?

> **CV anchor:** FASE / KAL-03 (augmented-load state, Kirchhoff coupling to dark node, $P_{22}$ collapses 100→4.73 via head update, no sensor at bus 2). DSSE-01 information-budget model. LinDistFlow voltage map with propagated covariance. The posterior covariance IS the ORACS Observability index.

---

#### Bullet 5: Deploy adaptive edge intelligence and control logic to enable real-time grid insights with minimal latency

**🟣 Behavioral:** Tell me about a time when you shipped machine learning or control logic to a field device where latency mattered.

> **CV anchor:** OSED/HEMS — local ML inference on edge hardware driving CVXPY MPC control decisions without cloud round-trip; real-time DER setpoint dispatch. −21% energy-cost outcome. → See STAR-STORIES.md Story 1.

**🔵 Situational:** How would you architect an edge intelligence system that runs a Kalman-based state estimator and a control dispatch loop on a K3s node, with sub-second latency from measurement arrival to control action, while remaining resilient to sensor dropouts?

> **CV anchor:** OSED edge runtime (local inference, K8s/K3s orchestration); KAL-03 recursive FASE filter (predict step runs during comms gap, $P$ inflates honestly — no hard failure); CVXPY MPC as simulate-before-commit step. NATS JetStream request-reply for zero-latency service invocation (built-in primitive vs MQTT manual correlation-ID).

---

#### Bullet 6: Apply control theory and signal processing techniques (e.g., Kalman filters, state estimation) to refine virtual sensor accuracy

**🟣 Behavioral:** Tell me about a time when you used a mathematical model to improve an estimate or a control decision that would not have been possible from raw sensor readings alone.

> **CV anchor:** HEMS MPC — CVXPY convex optimization using building thermal model + load forecasts to control DER setpoints (control theory in production). OSED ML-on-edge probabilistic estimation. → See STAR-STORIES.md Story 2.

**🔵 Situational:** Walk me through how a Kalman filter would improve the accuracy of a voltage estimate at a dark distribution node, compared to a simple point-in-time power-flow snapshot.

> **CV anchor:** KAL-01 (filter = vessel for information; WLS static snapshot fails when $G$ is singular; recursive filter borrows information across time — prior from 2 minutes ago is itself a source). KAL-02 (predict/update cycle; Kalman gain auto-weights model vs sensor by relative uncertainty). KAL-03 (money shot: $P_{22}$ 100→4.73 via topology coupling, not a sensor). Key framing: filter gives running film with calibrated uncertainty at every frame; WLS gives a static snapshot that fails for distribution.

---

### Simulation & Integration

#### Bullet 7: Collaborate with power systems engineers to validate virtual sensor performance against physical models and real-world field data

**🟣 Behavioral:** Tell me about a time when you worked with subject-matter experts from another discipline to validate that your software's outputs matched real-world behavior.

> **CV anchor:** OSED field deployment at Hydro-Québec — collaborated with power systems and field teams to validate edge ML outputs against metered data; big-data baseline-consumption analysis correcting for meter errors across substations. → See STAR-STORIES.md Story 3.

**🔵 Situational:** How would you set up a validation framework to confirm that your virtual sensing algorithm's voltage estimates are accurate — before trusting them to gate a real-time control action?

> **CV anchor:** DSSE-04 simulate-before-commit (patent claim 3): take posterior $(\hat x, P)$, simulate proposed control action via LinDistFlow, check probabilistic constraint satisfaction before dispatching. Innovation-sequence monitoring (NIS $\sim \chi^2$) as ongoing calibration check (KAL-02 §5). Cross-source consistency: do AMI, inverter, and head tell a consistent story when they overlap?

---

#### Bullet 8: Bridge the gap between simulation environments and live grid operations to "close the loop"

**🟣 Behavioral:** Tell me about a time when you had to take something that worked in a simulation or test environment and validate it in a real deployment.

> **CV anchor:** OSED — built the platform in simulation/test environment, then deployed to live field nodes at Hydro-Québec. HEMS PoC: validated simulated control decisions against field energy-meter readings. → See STAR-STORIES.md Story 1.

**🔵 Situational:** How would you design the "close the loop" validation pipeline — from EMT model baseline through virtual sensor output comparison through field data feedback — for a distribution virtual sensing system?

> **CV anchor:** DSSE-04 §4 simulate-before-commit; AGMS Operation Loop Formation patent (US 12,596,341 B2) — simulate-before-commit is the closed-loop gate. Drill 2 in SYSTEM-DESIGN-DRILLS.md covers this exact scenario: (1) EMT model baseline at awareness level, (2) virtual sensor vs model comparison, (3) divergence triggers field validation request, (4) field data retrains model — loop closes. AGMS tie: simulate-before-commit discipline is patented as the correct practice (granted, GE Vernova).

---

#### Bullet 9: Integrate AI/ML capabilities, federated control frameworks, and digital twins into next-generation grid platforms

**🟣 Behavioral:** Tell me about a time when you integrated AI or machine learning into a system that also had to operate in real time and coordinate with other distributed components.

> **CV anchor:** SI-MAPPER — agentic AI that infers structured ontology from CV signals, then routes IoT control via MCP server (LLM orchestration of physical actuators). OSED: ML inference + CVXPY optimization + K8s orchestration all integrated. → See STAR-STORIES.md Story 4 (the differentiator — maps to AGMS scouts).

**🔵 Situational:** How would you architect the integration layer between a virtual sensing AI/ML model, a federated training framework (e.g., Flower/FedAvg), and a digital twin simulation environment, so they form a closed-loop improvement cycle?

> **CV anchor:** FED-01 FedAvg (weights not raw data; fleet improves shared model); DSSE-04 federated DSSE + Learning Engine (innovation-sequence calibration closes the loop from field observations back to model parameters); AGMS Operation Loop Formation simulate-before-commit; AGMS Data Management POV file pattern (digital twin = role-filtered view). SI-MAPPER as the ontology/knowledge-graph layer.

---

### Required Skills

#### Bullet 10: Deep experience with Kubernetes/K3s, Kafka/NATS, MQTT, gRPC, and Pulsar

**🟣 Behavioral:** Tell me about a time when you had to choose between competing infrastructure options for a real-time edge system where resources were constrained.

> **CV anchor:** OSED — selected K8s + MQTT + InfluxDB for edge-native platform; made deliberate stack tradeoffs for latency and footprint. → See STAR-STORIES.md Story 1.

**🔵 Situational:** How would you justify the choice of K3s over full Kubernetes and NATS JetStream over Kafka for a 500-node substation fleet, where each edge node is a resource-constrained industrial PC?

> **CV anchor:** STK-03 say-aloud track — three K3s distinctions (memory ~512 MB vs 2–4 GB, SQLite default/embedded etcd, air-gap single binary); NATS over Kafka (NATS docs verbatim: Kafka needs JVM + 8 cores + 64–128 GB RAM + 10-Gig NIC; NATS is 20 MB binary); NATS over MQTT (durable replay for island mode, built-in request-reply, decentralized JWT accounts, leaf-node topology). "Kafka at the edge is like a semi-truck in a bicycle lane." See Q8 in Part B for the full answer key.

---

#### Bullet 11: Hands-on experience with InfluxDB/TimescaleDB and observability stacks (Prometheus, Grafana)

**🟣 Behavioral:** Tell me about a time when you set up monitoring for a production system and used it to catch a real problem.

> **CV anchor:** OSED — InfluxDB + Grafana for edge telemetry; monitoring caught latency spikes and sensor failures in deployed field nodes. TimescaleDB for time-series at substation scale.

**🔵 Situational:** How would you design the observability stack for a federated K3s fleet where each substation node runs its own EKF virtual-sensing service, and you need to detect node failures, degraded observability, and model drift from a central dashboard?

> **CV anchor:** STK-04 say-aloud track — pull vs push inversion (Prometheus scrapes `/metrics`; InfluxDB receives writes); kube-prometheus-stack (Prometheus Operator + node-exporter + kube-state-metrics + Grafana + Alertmanager in one Helm chart); recitable query: `rate(container_cpu_usage_seconds_total{namespace="virtual-sensing"}[5m])`; node-down alert: `up{job="node-exporter"} == 0`. Bridge: InfluxDB + Grafana (OSED) → Prometheus pull-scrape + ServiceMonitor CRD + kube-prometheus-stack. See Q9 in Part B.

---

#### Bullet 12: Proven experience with federated architectures, resilient edge software, and T&D applications

**🟣 Behavioral:** Tell me about a time when you built something that had to keep working even when part of the infrastructure it depended on was unavailable.

> **CV anchor:** OSED — edge nodes make local decisions when cloud connection drops; local ML inference + CVXPY MPC without WAN dependency; island-mode-by-design. → See STAR-STORIES.md Story 1.

**🔵 Situational:** What does "federated architecture" mean in the context of a distribution grid, and how does it differ from just having multiple servers that are distributed?

> **CV anchor:** FED-01 (federated = no central coordinator owns data; only weights/gradients leave each client, never raw training data; vs distributed = coordinator owns data and ships shards); DSSE-04 federated DSSE (each ORACS cell estimates locally, boundary-node posteriors exchanged, raw measurements never cross cell boundary); AGMS Scout Command (scouts self-form and execute without WAN round-trip). See Q10 in Part B.

---

#### Bullet 13: Experience developing and deploying AI/ML models in production environments

**🟣 Behavioral:** Tell me about a time when you deployed a machine learning model to a real production system — not just a demo — and it had to perform reliably over months.

> **CV anchor:** OSED — ML load/PV forecasting deployed on edge hardware at Hydro-Québec; months in production; −21% energy cost result from production ML. Contexto Azure ML MLOps pipeline (entity resolution, production). → See STAR-STORIES.md Story 1.

**🔵 Situational:** How would you approach deploying a federated virtual-sensing ML model across a 500-substation fleet, ensuring reliable updates, version control, and the ability to roll back if a new model degrades performance?

> **CV anchor:** K3s + GitOps (fleet management via ArgoCD/Flux for desired-state reconciliation — same manifest approach as OSED K8s); Flower (flwr) for federated aggregation; FED-02 Krum at the aggregator so one bad-model-update substation can't poison the fleet; kube-prometheus-stack for drift monitoring (NIS metric from EKF innovation sequence published to `/metrics`). See STAR-STORIES.md Story 4 for SI-MAPPER/MCP agentic AI connection to AGMS scouts.

---

## Part B — 12 Tough Domain Questions (rounds 2–4)

> 🔵 All questions in this section are tagged for technical rounds 2–4. Answer keys are condensed from the Phase 1–5 say-aloud tracks (D-16 — extracted, not re-derived). LaTeX is permitted where a formula aids recall. Each key is 5–7 bullets for fast oral rehearsal.
>
> **Source discipline:** Each answer key cites its source note path. Before the interview, read the original say-aloud track aloud at least once. Use these bullets as the compact recall prompt — the source note is the depth layer.

---

### Q1 — What is virtual sensing, and why is distribution harder than transmission?

🔵 Rounds 2–4 | Differentiator: HIGH | Source: KAL-01 `## <3-min say-aloud version`

**Answer key** (condensed from KAL-01 say-aloud):

- **Virtual sensing = manufacturing observability:** inferring state at an unmetered node and delivering that estimate with a calibrated uncertainty — the filter is the accounting engine; the hard job is sourcing information.
- **Transmission is easy (redundancy from space):** $m > n$, $G = H^\top WH$ full-rank, WLS converges, chi-squared/LNR bad-data detection works. More sensors = more observability.
- **Distribution is hard (under-observability):** hundreds to thousands of nodes, real-time telemetry = feeder head + a few inverters + delayed AMI → $m \ll n$, $G$ singular, WLS has no unique solution; bad-data detection mostly fails because **leverage trap is the normal condition**.
- **Energy-transition double-edge:** DER = harder physics (bidirectional, volatile) + more telemetry (every smart inverter, battery, EVSE, AMI meter is a new source) — net it out positive.
- **The filter fuses an information budget:** topology coupling + zero-injection constraints + temporal prior + ML pseudo-measurements + delayed AMI — each weighted by honest $R^{-1}$.
- **The deliverable is a posterior covariance, not just a number:** $P$ IS the ORACS Observability index that the AGMS Asset Portfolio Manager 1300 gates on.
- **Island-mode safety:** recursive structure keeps producing estimates (with inflating $P$) when WAN drops; centralized batch WLS stops cold.

---

### Q2 — Walk me through KF → EKF → UKF and when you'd choose each

🔵 Rounds 2–4 | Differentiator: HIGH | Source: KAL-02 Quick-Recall Card (no say-aloud block — mined from body)

**Answer key** (condensed from KAL-02 Quick-Recall Card and §1–3):

- **Linear KF (when system is linear-Gaussian):** Predict: $\hat x_{k|k-1} = F\hat x + Bu$; $P_{k|k-1} = FPF^\top + Q$. Update: $y = z - H\hat x$; $K = PH^\top(HPH^\top+R)^{-1}$; $\hat x \mathrel{+}= Ky$; $P = (I-KH)P$. Kalman gain auto-weights model vs sensor by relative uncertainty $P$/$R$.
- **EKF (mildly nonlinear):** Replace $F$ with Jacobian $A = \partial f/\partial x$ and $H$ with $\partial h/\partial x$ at each step (first-order Taylor linearization). Example: IEEE 738 conductor temperature EKF — scalar state, tractable Jacobian.
- **EKF failure modes:** Highly nonlinear $f$/$h$ → Jacobian is a poor local approximation → filter diverges. Ill-conditioned Jacobian near voltage collapse (large phase-angle differences). Positive-feedback divergence loop.
- **UKF (moderately-to-highly nonlinear):** Generate $2n+1$ sigma points around $\hat x$ via $\sqrt{(n+\lambda)P}$; propagate through true $f$/$h$ (no Jacobian); recombine weighted points — accurate to third order. $\alpha$ controls spread; $\beta=2$ optimal for Gaussian; $\lambda = \alpha^2(n+\kappa)-n$.
- **Decision rule:** EKF for mildly nonlinear + tractable Jacobian (line temperature, linear-ish voltage estimation). UKF for strongly nonlinear or Jacobian-hard (rotor-angle dynamic SE, near voltage-collapse). Particle filter for non-Gaussian noise (fault with unknown type, heavy tails).
- **Divergence detection:** $\text{NIS}_k = y^\top S^{-1} y \sim \chi^2(m)$. Sustained NIS > 95th-percentile threshold = diverging. Check: sensor failure, model mismatch, $Q$ too small.
- **Q = 0 trap:** $K \to 0$ → filter goes deaf. Always set $Q > 0$.

---

### Q3 — Explain FASE: how do you estimate a dark node with no sensor?

🔵 Rounds 2–4 | Differentiator: HIGH (differentiator) | Source: KAL-03 `## <3-min say-aloud version`

**Answer key** (condensed from KAL-03 say-aloud):

- **FASE puts loads in the state, not voltages:** $x = [P_1, P_2, \ldots]^\top$ — because injections have diurnal temporal structure that voltages don't. Voltages recover via LinDistFlow $V_i \approx V_0 - \sum_j \alpha_{ij} P_j$ with propagated covariance $\sigma_{V_i} = \sqrt{J P J^\top}$.
- **Process model is the diurnal ramp:** $\hat x_{k|k-1} = \hat x_{k-1} + v\,\Delta t$ where $v$ is the expected ramp (kW/min) from historical profiles — the `Bu` known-input term. $Q$ and $R$ are learned and time-indexed.
- **The money shot (Event 2 — head SCADA update):** After inverter pins $P_1 = 43.85$ kW ($P_2$ untouched, $K_2 = 0$), head reads 157 kW vs predicted 148.85. Innovation = +8.15 kW. Kalman gain: $K = [0.0092, 0.953]^\top$ — almost all goes to the *dark* $P_2$. Result: $\hat P_2 = 107.77$ kW with **no sensor at bus 2**. Kirchhoff routing via topology.
- **$P_{22}$ collapses 100 → 4.73:** The dark node became observable via topology coupling, not a sensor. Off-diagonal goes negative ($P_{12} = -0.92$) — head fixed their sum.
- **Comms gap predict:** 5 min, no data → $P_{22}$ inflates 4.73 → 14.73, $\sigma_2: \pm2.17 \to \pm3.84$ kW. Honest reporting of degraded observability.
- **Voltage map + CaCSM trigger:** Well-observed: $V_2 = 0.955 \pm 0.0008$ pu — safe. Comms gap: $V_2 \approx 0.951 \pm 0.0013$ pu, lower $2\sigma = 0.948 < 0.95$ floor → trips CaCSM. No fault alarm. Only virtual sensing knew.
- **Covariance = ORACS Observability index:** $P$ growing = AGMS sees degraded observability in real time, not after the fact.

---

### Q4 — What is under-observability and how do you source side information in distribution?

🔵 Rounds 2–4 | Differentiator: HIGH | Source: DSSE-01 `## <3-min say-aloud version`

**Answer key** (condensed from DSSE-01 say-aloud):

- **Under-observability in one sentence:** $m \ll n$ — the gain matrix $G = H^\top WH$ is singular, WLS has no unique solution, and the chi-squared bad-data detection test has no degrees of freedom to work with.
- **The leverage/critical-measurement trap is the normal condition:** Remove any real-time sensor and a section goes unobservable. Nearly every real measurement is a leverage measurement — chi-squared and LNR tests are structurally blind (LNR is near-zero *by construction* for leverage measurements).
- **What replaces bad-data detection:** Innovation/NIS monitoring over time (is the sequential residual white and zero-mean?); cross-source consistency checks (AMI, inverter, and head tell a consistent story?); robust pseudo-measurement covariances (don't let an overconfident prior become a de-facto leverage measurement).
- **Information budget (the sourcing strategy):** topology coupling (Kirchhoff coupling lets head flow inform dark nodes) + zero-injection constraints ($R \to 0$ virtual measurements) + temporal prior / diurnal profile (FASE `Bu` term) + ML pseudo-measurements (calibrated $R_{pseudo}$) + AMI (large $R$, stale, bounds long-term drift) + smart-inverter self-reports (small $R$, fast).
- **Energy-transition double-edge:** DER = harder physics (bidirectional, volatile) + more telemetry (every inverter, battery, EVSE is a new sensing point) — net it out positive.
- **Recursion beats batch:** Multi-rate arrival handled natively; prior from previous step is itself informative; comms gaps degrade gracefully (predict inflates $P$ honestly); island-mode safe.
- **My bridge:** HEMS forecasting is the temporal-prior discipline; SI-MAPPER is the topology-prior discipline; OSED edge runtime is the island-mode substrate.

---

### Q5 — How does virtual sensing sit inside the AGMS architecture?

🔵 Rounds 2–4 | Differentiator: HIGH (patent connection) | Source: DSSE-04 `## <3-min say-aloud version`

**Answer key** (condensed from DSSE-04 say-aloud):

- **Virtual sensing is the seeing capability of AGMS:** The DSSE/FASE filter runs as an Inspector scout ($s_i$) on each Field Agent Device (FAD), locally, producing posterior $(\hat x, P)$ for that FAD's section of the feeder.
- **ORACS Observability index:** The posterior covariance $P$ is what the Asset Portfolio Manager (module 1300) gates on. High $P$ = low observability = CaCSM not armed. Low $P$ = well-observed = CaCSM armed.
- **Worked Example 2 (the money scenario):** Rooftop solar overvoltage at an unmetered node at midday. No fault alarm fires. No human sees it. FASE on the FAD attributes the excess generation via Kirchhoff coupling → posterior voltage above 1.05 pu → CaCSM dispatches reactive power absorption → voltage restored. The covariance was the gate.
- **Simulate-before-commit (patent claim 3):** Before any control action: take $(\hat x, P)$, simulate via LinDistFlow, check probabilistic constraint satisfaction (accounting for $P$), then dispatch. Same discipline as CVXPY MPC.
- **Federated DSSE:** Each ORACS cell estimates its sub-feeder independently. At boundaries, adjacent cells exchange only boundary-node posteriors $(\hat x_{boundary}, P_{boundary})$ — raw measurements never cross. This satisfies "federated, no central coordination" and preserves island-mode safety per cell.
- **Why locally on the FAD:** Reduces WAN bandwidth; keeps running in island mode; enables edge-local control without round-trip; scales horizontally.
- **My bridges:** OSED = FAD substrate; HEMS forecasting = temporal prior generator; CVXPY MPC = simulate-before-commit; SI-MAPPER = federated structural prior.

---

### Q6 — Walk me through the AGMS patent family in 90 seconds

🔵 Rounds 2–4 | Differentiator: HIGHEST (differentiator) | Source: AGMS-patent-rehearsal-deck.md `## The ~90-Second Pitch`

**Answer key** (condensed from the ~90-Second Pitch):

- **One assembly line, six patents:** Parent defines the full architecture (detect alert → build CaCSM → deploy to field). Five continuations each own one stage.
- **The five stages in order:** Logistician = *which* assets/procure/audit. Portfolio Manager = *verify* each asset across 7 indexes (observability, reachability, adaptability, controllability, security, sustainability, stability). Operation Loop Formation ★ = *assemble + simulate* the ORACS loop (simulate-before-commit; GRANTED to GE Vernova). Scout Command = *deploy* role-typed scouts onto field hardware. Data Management = POV file system (role-filtered data view; ga-authenticationkey gate).
- **The granted patent (Operation Loop Formation US 12,596,341 B2):** Takes verified asset list, retrieves a behavioral DNA schema from history, builds per-asset meta objects, runs a full simulation in the Learning Engine, and only then causes execution. The simulate-before-commit discipline is in **claim 3** — never dispatch on an unvalidated plan.
- **The AGMS layered structure:** Field Agent Devices → Inspector scouts → ORACS coordination → GridWideMind/GridWideEye intelligence — the virtual-sensing DSSE filter runs at the FAD/Inspector scout level.
- **Key terms:** CaCSM = Contextual and Cognitive State Machine. DNA/schema = the behavioral fingerprint template. Meta object = per-asset constructed object. POV = role-filtered data view. ga-authenticationkey = security gate.
- **My connection:** OSED is the FAD runtime; K3s is the Scout Incubator Manager; SI-MAPPER is the DNA map; CVXPY MPC is the simulate-before-commit gate; Databricks pipeline is the alert-correlation data layer.

---

### Q7 — What is the Operation Loop Formation patent and why is it the granted one?

🔵 Rounds 2–4 | Differentiator: HIGHEST | Source: AGMS-patent-rehearsal-deck.md `## Patent 4: Operation Loop Formation`

**Answer key** (condensed from Patent 4 section):

- **US 12,596,341 B2 — GRANTED and assigned to GE Vernova Infrastructure Technology LLC:** This is live, enforceable IP of the hiring company. Patent number, assignee, and granted status are the first things to say.
- **What it does:** Formation Construct Module (1400) takes the verified formation plan and logistics list → retrieves a matching behavioral DNA schema from history → constructs per-asset meta objects (role + behavior encoded) → runs the full ORACS loop in a Learning Engine simulation → only then causes the network of devices to execute.
- **Simulate-before-commit (claim 3):** The learning engine simulates the formation plan against historical archives before the module commits to execution. "Never dispatch on an unvalidated plan" is the explicit discipline of this claim.
- **Why it is the keystone:** It is the only granted patent in the family. The parent and most continuations are applications (WO/US pub); this one has been examined, amended, and issued — it is law. It is also the most differentiated claim: simulate-before-commit as a patented software discipline for autonomous grid control.
- **My connection:** CVXPY MPC in OSED/HEMS is structurally identical to simulate-before-commit: solve (simulate) → feasibility-check → commit to actuators. The distribution grid version adds LinDistFlow instead of the RC thermal model and a probabilistic safety gate from $P$.
- **Good question to ask the director:** "When the ORACS cannot be fully validated in time — say a critical asset's health index is stale — does the formation construct module promote a partially-validated operation loop in a degraded/bounded-authority mode, or does it hold execution until simulation converges? Where is the line between simulate-before-commit and 'the grid needs an action right now'?"

---

### Q8 — Justify NATS JetStream vs MQTT vs Kafka for a substation edge node

🔵 Rounds 2–4 | Differentiator: MEDIUM-HIGH | Source: STK-03 `## <3-min say-aloud version`

**Answer key** (condensed from STK-03 say-aloud):

- **The edge constraint is footprint, not throughput:** A substation edge node is Pi-class or a small industrial PC — air-gapped, limited RAM. That rules out entire categories.
- **NATS over MQTT — four reasons:** (1) Durable replay: JetStream persists to disk; MQTT QoS is transient — data is gone if WAN drops. (2) Built-in request-reply: zero application-level correlation-ID plumbing. (3) Decentralized JWT accounts: multi-tenant isolation without a central auth server reachable at all times. (4) Leaf-node topology: bridges substation LAN to cloud hub without VPN.
- **NATS over Kafka — the verbatim quote:** The NATS docs say: "Kafka servers require a JVM, eight cores, 64 GB to 128 GB of RAM, two or more 8-TB SAS/SSD disks, and a 10-Gig NIC." NATS JetStream = single static binary under 20 MB on ~512 MB RAM. **"Kafka at the edge is like a semi-truck in a bicycle lane."** Frame as footprint, not speed — Kafka isn't slow, it's enormous.
- **Pulsar (awareness):** Same edge-unsuitability as Kafka — BookKeeper + broker is data-center class.
- **K3s over full K8s — three distinctions:** Memory (~512 MB vs 2–4 GB), database (SQLite default/embedded etcd vs external etcd cluster required), air-gap (single binary <100 MB, Traefik + local-path included, `curl | sh`).
- **My bridge:** MQTT → NATS (same pub/sub instinct + durable replay + JWT); full K8s → K3s (same API, 4x lighter, air-gap).

---

### Q9 — How would you observe a federated K3s fleet? What Prometheus tells you that InfluxDB doesn't

🔵 Rounds 2–4 | Differentiator: MEDIUM | Source: STK-04 `## <3-min say-aloud version`

**Answer key** (condensed from STK-04 say-aloud):

- **The key mental model shift — pull vs push:** InfluxDB receives writes from services (push); Prometheus scrapes `/metrics` endpoints (pull). The pull model fits Kubernetes because **pod IPs change constantly** — services just expose `/metrics` and Prometheus discovers them via the K8s API using a ServiceMonitor CRD. No reconfiguration when pods restart.
- **kube-prometheus-stack — the production answer (not just "Prometheus + Grafana"):** Single Helm chart bundling five components pre-wired: **Prometheus Operator** (watches ServiceMonitor CRDs, auto-configures scrape targets), **node-exporter** (DaemonSet; Linux host metrics), **kube-state-metrics** (K8s object states: pod/replica/PVC), **Grafana** (pre-loaded K8s dashboards), **Alertmanager** (routes alerts to PagerDuty/Slack/webhook).
- **Recitable PromQL query:** `rate(container_cpu_usage_seconds_total{namespace="virtual-sensing"}[5m])` — per-second CPU rate for virtual-sensing namespace, 5-minute window. `rate()` is required because the metric is a cumulative counter.
- **Node-down alert:** `up{job="node-exporter"} == 0` — Prometheus's own scrape health; 0 = target unreachable.
- **What Prometheus tells you that InfluxDB doesn't:** Native K8s service discovery (no manual wiring), Operator-managed scrape config (no editing prometheus.yml), native alerting rules in Prometheus + Alertmanager routing — and specifically for the virtual-sensing fleet: NIS from the EKF innovation sequence as a custom `/metrics` endpoint detects model drift per substation node without any central data collection.
- **My bridge:** InfluxDB + Grafana push-model (OSED) → Prometheus pull + kube-prometheus-stack (same Grafana, different data source, Operator-managed, native K8s discovery).

---

### Q10 — Distinguish federated from distributed learning; explain FedAvg

🔵 Rounds 2–4 | Differentiator: HIGH | Source: FED-01 `## <3-min say-aloud version`

**Answer key** (condensed from FED-01 say-aloud):

- **Federated ≠ distributed:** Distributed = coordinator owns all the data and ships shards to workers. Federated = **no central coordinator owns the data** — each substation trains locally on its own load telemetry; only weight deltas leave the node, never raw PMU readings. Spark/MapReduce is distributed, not federated — don't confuse them.
- **Why federated for substations:** Substation data is commercially sensitive + security-critical. Raw PMU/load readings must not leave the node (regulatory or operational). Federated learning is the architecture, not a choice.
- **FedAvg:** $w_{t+1} = \sum_{k=1}^{K} \frac{n_k}{n} w_t^k$ — weighted average by sample count. Two-nested-loop: server broadcasts $w_t$; each sampled client runs $E$ local SGD epochs → produces $w_t^k$; server averages.
- **Non-IID problem:** Substations are non-IID by definition (residential vs industrial feeders, different DER, different climate). Many local epochs → each node drifts toward its own local optimum → weighted average of drifted models fails atypical clients. This is client drift.
- **FedProx fix:** Add $+\frac{\mu}{2}\lVert w - w_t\rVert^2$ to the **client's local objective** (NOT the server aggregation step). $\mu = 0$ collapses to FedAvg; larger $\mu$ tethers clients to the global model. Proximal term lives client-side.
- **My bridge:** OSED runs distributed edge inference (no cloud round-trip for local decisions); federated learning is the natural upgrade — keep local inference, add FedAvg so the fleet improves a shared model, add Krum so one bad node can't poison it.

---

### Q11 — How does Krum make gradient aggregation Byzantine-robust?

🔵 Rounds 2–4 | Differentiator: MEDIUM-HIGH | Source: FED-02 `## <3-min say-aloud version`

**Answer key** (condensed from FED-02 say-aloud):

- **The Byzantine threat:** One compromised substation sends $\Delta w_\text{poison} = -\lambda \cdot \Delta w_\text{honest}$ (sign-flipped, amplified). FedAvg averages it in — one high-$n_k$ client can dominate the global model.
- **Krum scoring:** $S(k) = \sum_{j \in \text{NN}_{n-f-2}(k)} \lVert \Delta w_k - \Delta w_j \rVert^2$ — sum of squared distances to the $(n-f-2)$ nearest neighbors in gradient space. Honest updates cluster; poisoned update is far from the cluster → high score. Select $k^* = \arg\min_k S(k)$.
- **Precision:** Vanilla Krum selects **ONE** update (the single argmin). Multi-Krum averages the top $m$ lowest-score clients. Be exact about which variant — "Krum picks the best gradients and averages them" is wrong for vanilla.
- **Coordinate-wise median (alternative):** $[\Delta w_\text{agg}]_i = \text{median}_k([\Delta w_k]_i)$ for each parameter dimension independently. Tolerates up to $n/2 - 1$ Byzantine clients (higher fraction than Krum's $n \geq 2f+3$). Does not require knowing $f$. Limitation: ignores gradient correlations — sophisticated joint-space attacks can evade it.
- **Comparison:** Krum operates on the full gradient vector (catches correlation attacks); median is dimension-wise (ignores correlations but needs no $f$ estimate). For a NATS-hub substation fleet → central aggregation with Krum is the natural fit: one hub applies the filter before broadcasting the new global model.
- **Gossip vs central:** Central = Krum at one node, simpler ops, but SPOF. Gossip = no SPOF, but Byzantine poison propagates P2P before rejection. Central + Krum for the NATS-connected substation context.
- **Byzantine robustness ≠ secure aggregation:** Separate orthogonal mechanisms — robustness = reject malicious gradients (integrity); secure aggregation = hide gradients from server (privacy). Both can be stacked.

---

### Q12 — What does "edge security beyond TLS" mean? Name three mechanisms

🔵 Rounds 2–4 | Differentiator: MEDIUM-HIGH | Source: FED-03 `## <3-min say-aloud version`

**Answer key** (condensed from FED-03 say-aloud):

- **The framing:** TLS encrypts the wire. But before data flows through that pipe, three prior questions must be answered: Is the code genuine (OTA signing)? Did the hardware boot untampered (TPM attestation)? Is this workload who it claims to be (SPIFFE/SPIRE)?
- **OTA signing:** Build pipeline signs every firmware image with a key held in an HSM; edge node refuses to apply any image that doesn't pass signature verification. Attacker must own the signing key, not just the update channel — stops malicious firmware push bricking or weaponizing a substation fleet.
- **TPM attestation:** TPM 2.0 chip measures every boot stage into tamper-resistant PCRs. Before a node joins the federated aggregation, the aggregator challenges it: prove your PCR values match the known-good hash for unmodified trusted code. Hardware root-of-trust, not a password — stops a rooted relay from quietly poisoning the control loop.
- **SPIFFE/SPIRE workload identity:** Each K3s pod gets a short-lived X.509 SVID with a process-identity URI (`spiffe://trust-domain/path`), auto-rotating every few minutes. Not just TLS — SPIFFE identifies *which specific workload* is on each end of the channel. Stolen SVID expires before attacker can use it — stops a spoofed node impersonating a real IED at the mTLS handshake.
- **The stacking principle:** TLS encrypts the wire. OTA/TPM/SPIFFE each answer "should this node be trusted at all?" — prior to any data exchange. They stack, not substitute.
- **My bridge:** Juan has shipped OTA updates and run K8s MQTT device fleets. The deltas are concrete and honest: add image signing in the pipeline (OTA), add TPM-attested node admission to the aggregator, replace static API keys with SPIFFE/SPIRE short-lived SVIDs.

---

## Part C — Consolidated Bank (final-day rehearsal index)

> This is the union view (D-11): all questions organized by round and category. Use this as the **final-day rehearsal map** — pick your round, find the questions, and drill. Each entry references where the answer lives, not the answer itself (prevents re-reading instead of active recall).

---

### Round 1 — HR Screen

> **Source:** PHONE-SCREEN.md is the primary doc for this round. This section indexes the question prompts only; go to PHONE-SCREEN.md for the full scripted answers.
>
> **How to use:** Cover the answer, say it aloud, time yourself (≤90 s for "tell me about yourself"), then verify against PHONE-SCREEN.md. Cross-reference: STAR-STORIES.md screen versions for behavioral questions.

| # | Prompt | Answer Lives In | Target Time |
|---|--------|-----------------|-------------|
| R1-01 | Tell me about yourself | PHONE-SCREEN.md §1 | ≤90 s |
| R1-02 | Why this role / why GE Vernova? | PHONE-SCREEN.md §2 | ≤60 s |
| R1-03 | Why leave Hydro-Québec? | PHONE-SCREEN.md §3 | ≤60 s |
| R1-04 | Work authorization and relocation | PHONE-SCREEN.md §4 | ≤30 s |
| R1-05 | Salary expectations | PHONE-SCREEN.md §5 | ≤30 s |
| R1-06 | Strengths and weaknesses | PHONE-SCREEN.md §6 | ≤60 s |
| R1-07 | Notice period / availability | PHONE-SCREEN.md §8 | ≤15 s |
| R1-B1 | 🟢 Tell me about a time you built and deployed software on field hardware | Part A Bullet 1 behavioral + STAR-STORIES.md Story 1 | ≤90 s |
| R1-B2 | 🟢 Tell me about a time you integrated data from several different field devices | Part A Bullet 3 behavioral + STAR-STORIES.md Story 3 | ≤90 s |
| R1-B3 | 🟢 Tell me about a time you shipped ML to a production system | Part A Bullet 13 behavioral + STAR-STORIES.md Story 1 | ≤90 s |
| R1-B4 | 🟢 Tell me about a time you built something that kept working when infrastructure was unavailable | Part A Bullet 12 behavioral + STAR-STORIES.md Story 1 | ≤90 s |

> **Full screen-arc rehearsal:** PHONE-SCREEN.md `## 9. Say-Aloud Track` stitches R1-01 through R1-07 into a ~10-min full arc. Run it aloud end-to-end on Day 1 and Day 3.

---

### Rounds 2–3 — Technical / Domain

> **Source:** Part A situational questions (🔵) + Part B (Q1–Q12) + SYSTEM-DESIGN-DRILLS.md drills 1–2.
>
> **How to use:** Cover the answer key, say the answer aloud from memory, time yourself (~2–3 min per domain Q, ~5 min per drill), then verify against the answer key below. For drill narration, verify against SYSTEM-DESIGN-DRILLS.md.

#### Technical — JD Situational Questions (from Part A)

| # | Prompt | Answer In | Target Time |
|---|--------|-----------|-------------|
| T-01 | How would you architect a software component for island-mode substation edge? | Part A Bullet 1 situational | ~2 min |
| T-02 | How would you design a federated data pipeline (no central coordinator)? | Part A Bullet 2 situational | ~2 min |
| T-03 | How would you integrate SCADA, PMU, and inverter streams for DSSE? | Part A Bullet 3 situational | ~2 min |
| T-04 | How would you design a virtual sensing algorithm for an unmetered node? | Part A Bullet 4 situational | ~2 min |
| T-05 | How would you architect an edge intelligence system with sub-second latency? | Part A Bullet 5 situational | ~2 min |
| T-06 | How does a Kalman filter improve distribution voltage estimation over WLS? | Part A Bullet 6 situational | ~2 min |
| T-07 | How would you set up a validation framework for virtual sensor performance? | Part A Bullet 7 situational | ~2 min |
| T-08 | How would you design the "close the loop" simulation → field validation pipeline? | Part A Bullet 8 situational | ~2 min |
| T-09 | How would you architect the AI/ML + federated + digital twin integration? | Part A Bullet 9 situational | ~2 min |
| T-10 | How would you justify K3s over K8s and NATS over Kafka for a substation fleet? | Part A Bullet 10 situational | ~2 min |
| T-11 | How would you design the observability stack for a federated K3s fleet? | Part A Bullet 11 situational | ~2 min |
| T-12 | What is federated architecture vs distributed for distribution grids? | Part A Bullet 12 situational | ~2 min |
| T-13 | How would you deploy a federated virtual-sensing ML model across 500 substations? | Part A Bullet 13 situational | ~2 min |

#### Domain Deep-Dives (from Part B)

| Q# | Prompt | Answer In | Differentiator |
|----|--------|-----------|---------------|
| Q1 | What is virtual sensing and why is distribution harder than transmission? | Part B Q1 key | HIGH |
| Q2 | Walk me through KF → EKF → UKF and when you'd choose each | Part B Q2 key | HIGH |
| Q3 | Explain FASE: how do you estimate a dark node with no sensor? | Part B Q3 key | HIGH ★ |
| Q4 | What is under-observability and how do you source side information? | Part B Q4 key | HIGH |
| Q5 | How does virtual sensing sit inside the AGMS architecture? | Part B Q5 key | HIGH ★ |
| Q6 | Walk me through the AGMS patent family in 90 seconds | Part B Q6 key | HIGHEST ★ |
| Q7 | What is the Operation Loop Formation patent and why is it the granted one? | Part B Q7 key | HIGHEST ★ |
| Q8 | Justify NATS JetStream vs MQTT vs Kafka for a substation edge node | Part B Q8 key | MEDIUM-HIGH |
| Q9 | How would you observe a federated K3s fleet? What Prometheus tells you that InfluxDB doesn't | Part B Q9 key | MEDIUM |
| Q10 | Distinguish federated from distributed learning; explain FedAvg | Part B Q10 key | HIGH |
| Q11 | How does Krum make gradient aggregation Byzantine-robust? | Part B Q11 key | MEDIUM-HIGH |
| Q12 | What does "edge security beyond TLS" mean? Name three mechanisms | Part B Q12 key | MEDIUM-HIGH |

#### System-Design Drills

| Drill | Topic | Answer In | Target Time |
|-------|-------|-----------|-------------|
| SD-1 | Design a 500-node virtual sensing pipeline (K3s + NATS + EKF + federated + GitOps) | SYSTEM-DESIGN-DRILLS.md Drill 1 | ~5 min |
| SD-2 | Close the loop: simulation / digital twin → field validation | SYSTEM-DESIGN-DRILLS.md Drill 2 | ~5 min |

---

### Any Round — Behavioral

> **Source:** STAR-STORIES.md contains all four stories with screen versions (≤90 s, plain language) and technical STAR versions (≤2 min). Use the screen version for round 1; use the technical STAR for rounds 2–4. Vocabulary bridges (plain-language and technical) live in REFRAME.md.
>
> **How to use:** Say the story aloud without notes, then check the JD-line mapping in STAR-STORIES.md to confirm you hit the right evidence. Cross-reference PHONE-SCREEN.md for the plain-language screen arc.

| Story | Screen Prompt | Technical Prompt | Answer In | JD-Line Anchor |
|-------|--------------|-----------------|-----------|----------------|
| Story 1 | Tell me about yourself / Tell me about a time you built and deployed edge software | Walk me through the OSED platform architecture | STAR-STORIES.md Story 1 | JD Bullet 1 (edge-native software) + Bullet 5 (adaptive edge intelligence) |
| Story 2 | Tell me about a time you built a system that inferred a value with no direct sensor | Tell me about your HEMS PoC and how MPC gates on uncertain state | STAR-STORIES.md Story 2 | JD Bullet 4 (virtual sensing algorithms) + Bullet 6 (Kalman/state estimation) |
| Story 3 | Tell me about a time you worked with field data at large scale | Walk me through your substation data analysis work | STAR-STORIES.md Story 3 | JD Bullet 3 (integrate field data sources) + Bullet 7 (validate vs field data) |
| Story 4 ★ | Tell me about a time you built something that maps to AI agent orchestration | Tell me about SI-MAPPER and how it maps to the AGMS scout architecture | STAR-STORIES.md Story 4 | JD Bullet 9 (AI/ML + federated + digital twins) + Bullet 8 (bridge simulation to field) |

> ★ Story 4 is the **#1 differentiator** — SI-MAPPER/MCP agentic AI → AGMS scouts → Operation Loop Formation patent (US 12,596,341 B2, GRANTED to GE Vernova). Surface this early in any round.

---

### Vocabulary Bridges Quick-Reference (use before any round)

> Full bridge tables live in REFRAME.md. Use these one-liners as the last check before each round — ≤10 s per bridge.

| If they say… | You say… | In ≤10 s |
|-------------|---------|---------|
| "What is your experience with NATS or Kafka?" | "I've shipped MQTT in production; NATS JetStream is the same pub/sub mental model plus durable replay and decentralized JWT — the upgrade path I'd take here." | |
| "Tell me about K3s vs Kubernetes" | "I've shipped full Kubernetes in production; K3s is the same API 4x lighter, designed for air-gapped field environments." | |
| "Tell me about Prometheus vs InfluxDB" | "I shipped InfluxDB + Grafana push-model; Prometheus inverts to pull-scrape with native K8s service discovery — kube-prometheus-stack is the one-Helm-chart production path." | |
| "Virtual sensing / state estimation experience?" | "OSED HEMS edge ML is the temporal prior generator; SI-MAPPER is the structural prior; CVXPY MPC is the simulate-before-commit step." | |
| "Federated learning experience?" | "OSED runs distributed edge inference without cloud round-trip — federated learning is the natural next step with FedAvg weight aggregation and Krum robustness added." | |

> Full Layer A (HR plain-language) and Layer B (technical T&D analog) bridges: REFRAME.md.

---

*Last updated: 2026-06-16 | Phase 6, Plan 04 | Sources: KAL-01..03, DSSE-01, DSSE-04, AGMS-patent-rehearsal-deck.md, STK-03, STK-04, FED-01..03 (all say-aloud tracks); docs/job-requirements.md (JD bullets); PHONE-SCREEN.md, REFRAME.md, STAR-STORIES.md (Wave-1 cross-links)*
