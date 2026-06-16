**For:** Behavioral interview preparation — HR phone screen (screen versions) and technical rounds 2–4 (Technical STAR versions).
**Purpose:** Give Juan four pressure-tested, outcome-first behavioral stories that prove the JD responsibility bullets (BRG-03, D-08). Each story has a plain-language screen version (≤90 s) and a ≤2-min technical STAR version (for later rounds), explicitly mapped to specific JD lines so the right story can be retrieved under a JD-bullet behavioral question. Story 4 establishes the single strongest "I already think like your lab" differentiator hook.

---

## How to Use

- **Round 1 (HR phone screen):** Use only the `### Screen version` for each story. Plain language, outcome-first, no jargon.
- **Rounds 2–4 (technical/behavioral):** Use the `### Technical STAR` version. Structured S → T → A → R with specific decisions and quantified results.
- **Retrieval under pressure:** See `### JD-line mapping` under each story — if the interviewer asks a JD-bullet behavioral question, find the story whose JD mapping matches, then deliver.
- **Time discipline:** Screen ≤90 s (say it aloud, time yourself). Technical ≤2 min (same check). If you run over, cut from Situation/Task first — never cut the Result.

---

## Story 1: OSED Build — Edge-Native Platform with 21% Energy Cost Reduction

*Honest framing (DSSE-03): OSED is a cloud-edge platform for buildings and DER — it is an analog to a distribution DSSE/FASE system (same architectural class), not a deployed grid DSSE. Frame it as the structural prototype; the distribution extension is the step Juan is taking by joining GE Vernova.*

---

### Screen version (plain, ≤90 s)

**Opening hook (outcome-first):** "I built and shipped a cloud-edge platform that cut isolated-community energy costs by 21%. Here is what that means in plain terms."

1. **Situation:** A remote community had no automated way to manage its power — everything was manual, wasteful, and expensive.
2. **My role:** I was the architect and lead builder — I designed the platform from scratch, chose every major technology, and shipped it to real hardware in the field.
3. **What I built:** Small computers installed in the field that read sensor data, make real-time decisions locally without waiting for a cloud round-trip, and coordinate with each other without a central coordinator telling them what to do.
4. **The hard part:** Getting these field computers to keep working when the network goes down, and to make safe, constraint-respecting decisions with only the data available locally — the same challenge GE Vernova faces at every substation.
5. **Result:** 21% reduction in energy costs for the community. Real hardware, real field deployment, not a lab demo.

---

### Technical STAR (≤2 min)

**S** — Isolated remote communities in Quebec had no automated grid-services platform; energy management was manual and reactive, with no edge-native intelligence or federated coordination between field nodes.

**T** — As the architect and lead engineer, I owned the end-to-end design and delivery of OSED (Optimal Smart Energy Distribution) — a cloud-edge platform for real-time energy-management services running directly on field hardware.

**A:**
- Designed a four-tier architecture: cloud tier for long-running optimization and model training; edge tier on field-deployed compute for local inference and control; MQTT-based telemetry layer with buffering for network-outage resilience; CVXPY model-predictive control layer that simulates the next time window, evaluates constraint satisfaction, and only dispatches when the posterior is reliable.
- Chose Kubernetes (now K3s at the distribution edge) for edge orchestration — same API across cloud and field nodes, GitOps-driven reconciliation, role-typed workloads (inference service, MQTT messenger, monitoring sidecar) that reconcile to desired state automatically.
- Built the virtual-sensing inference engine as an EKF-based state estimator fusing heterogeneous, asynchronous sources — smart meters, HVAC state, weather APIs, occupancy signals — producing a calibrated posterior state with explicit covariance (P) that gates every downstream control action.
- Honest framing: OSED implements federated *inference* at the edge — each site makes local decisions without a central round-trip; the production Flower-based federated gradient aggregation layer is the extension I would add at GE Vernova scale.

**R** — Deployed to real field hardware in isolated communities; achieved 21% reduction in community energy costs. The platform operates in island mode — field nodes keep running and making local decisions even when the WAN drops — demonstrating the disconnection-tolerant, no-central-coordination pattern the JD calls for.

---

### JD-line mapping

**Primary JD line:** "Build and deploy edge-native software components for decentralized operation, sensing, and control." — OSED is exactly this: a deployed, edge-native platform for decentralized grid-services operation with real field hardware.

**Secondary JD line:** "Develop federated data pipelines that allow distributed nodes to collaborate securely without central coordination." — Each OSED field node runs its own inference and control; aggregated outputs (state estimates, anomaly flags) flow to the cloud; raw sensor streams do not. This is the federated, no-central-coordination architecture.

**Retrieval trigger:** Any question invoking "edge-native," "decentralized operation," "federated pipelines," or "deploy software to field hardware" → use Story 1.

---

## Story 2: HEMS PoC — Whole-Home Load Management Respecting Grid Limits

---

### Screen version (plain, ≤90 s)

**Opening hook (outcome-first):** "I built a software system that manages a whole home's energy — heating, cooling, EV charging — automatically, while keeping the household within its grid connection limit in real time."

1. **Situation:** Residential buildings are becoming significant grid actors — with rooftop solar, battery storage, and EV chargers, a house can overwhelm its local grid connection if not managed.
2. **My role:** I designed and built the Home Energy Management System (HEMS) as a proof-of-concept running on real hardware — I did the control design, the machine-learning forecasting, and the real-time optimization.
3. **What I built:** A system that predicts what the house will need over the next few hours, then decides in real time how to schedule loads and storage to stay under the grid connection limit and minimize cost — like a smart brain for the house's energy.
4. **The hard part:** The decisions have to be made with incomplete information and under a hard real-time constraint — the software has to forecast, optimize, and dispatch in seconds.
5. **Result:** The system consistently respected the grid connection limit across all test scenarios while minimizing cost — proving the approach works on real hardware with real-time constraints.

---

### Technical STAR (≤2 min)

**S** — In the context of distributed energy resource (DER) proliferation, residential buildings with solar, storage, and EV chargers risk exceeding local grid connection limits without automated, real-time load coordination.

**T** — I designed and implemented the HEMS (Home Energy Management System) proof-of-concept — a real-time edge-intelligence system on physical hardware that forecasts demand, optimizes load scheduling, and dispatches control commands while satisfying grid connection constraints.

**A:**
- Built a probabilistic load/PV forecasting engine — time-series ML models producing calibrated forecasts with explicit uncertainty (the temporal prior in DSSE terms — these ARE the pseudo-measurements that enter the control loop with a known covariance R_pseudo, derived from the empirical forecast-error archive, not from the model's self-reported confidence).
- Implemented CVXPY-based model-predictive control: at each control step, propagate the current state estimate through the building thermal and electrical model, solve the constrained optimization (minimize cost subject to grid limit, thermal comfort bounds, battery state-of-charge limits), and dispatch only when the constraint-satisfaction probability is high enough given the posterior uncertainty.
- Applied Kalman filtering for real-time state estimation of building thermal state and battery state-of-charge — fusing heterogeneous sensor readings (smart meters, HVAC actuator state, environmental sensors) into a single posterior with calibrated covariance.
- Ran on real hardware with a real-time control loop — not a simulation.

**R** — HEMS PoC consistently respected the whole-home grid connection limit across all test scenarios, validating the control architecture on real hardware. Demonstrated the principle that adaptive edge intelligence with calibrated uncertainty and real-time optimization can manage DER aggregations safely within grid limits — which is the JD's "adaptive edge intelligence and control logic" requirement in a buildings context.

---

### JD-line mapping

**Primary JD line:** "Deploy adaptive edge intelligence and control logic to enable real-time grid insights with minimal latency." — HEMS is deployed adaptive edge intelligence: real-time, constraint-respecting, running locally on hardware.

**Secondary JD line:** "Apply control theory and signal processing techniques (e.g., Kalman filters, state estimation) to refine virtual sensor accuracy." — HEMS uses Kalman filtering for state estimation and CVXPY MPC for control — these are the exact techniques named in the JD.

**Retrieval trigger:** Any question invoking "control theory," "Kalman filters," "state estimation," "adaptive control," "real-time edge intelligence," or "DER management" → use Story 2.

---

## Story 3: Big-Data Substation Analysis — Billions of Points, Databricks/PySpark

---

### Screen version (plain, ≤90 s)

**Opening hook (outcome-first):** "I led an analysis of billions of data points from real utility substations to find systematic patterns of bad data and model error — at a scale that only distributed computing could handle."

1. **Situation:** Hydro-Québec had accumulated years of substation sensor data — hundreds of substations, multiple sensors per substation, sampled at high frequency. No one had analyzed it all at once.
2. **My role:** I designed and ran the distributed computing pipeline that processed this data — choosing the tools, writing the analysis code, and interpreting the results for the engineering team.
3. **What I found:** Systematic baseline-estimation errors that were invisible when you looked at one substation at a time — but unmistakable at scale. The pattern pointed to model calibration problems that affected grid monitoring accuracy across the fleet.
4. **The hard part:** Getting billions of points through a distributed compute cluster in a way that actually answered the right question — designing the analysis to detect subtle systematic errors, not just obvious outliers.
5. **Result:** Identified patterns that could not be seen from individual substations — and those findings fed directly into model recalibration work that improved monitoring accuracy across the substation fleet.

---

### Technical STAR (≤2 min)

**S** — Hydro-Québec's grid monitoring depended on baseline energy-consumption models calibrated from historical substation data. At individual-substation scale, model errors were not obviously detectable; at fleet scale, systematic bias patterns were hypothesized but unconfirmed.

**T** — I designed and executed a fleet-wide distributed data analysis pipeline to characterize baseline-model error distributions across all substations — to identify systematic calibration deficiencies invisible at single-substation granularity.

**A:**
- Built the analysis pipeline on Databricks / Apache PySpark — the only practical approach to processing billions of data points (multiple years × hundreds of substations × multiple sensors × sub-minute sampling) within a reasonable time and cost budget.
- Designed the analysis around residual monitoring: compare predicted baseline consumption to measured actuals across time-slots, seasons, temperature buckets, and substation archetypes to distinguish random sensor noise from systematic model bias.
- Applied the NIS-over-time discipline (innovation sequence analysis): if model residuals are not white and zero-mean — if they're consistently off in one direction or correlated over time — the model is wrong. This is the same diagnostic used in distribution DSSE to detect bad sensors and topology changes.
- Surfaced actionable patterns: specific substation archetypes and time-of-day windows where the baseline model was systematically overconfident — the same overconfident-R_pseudo trap that degrades Kalman filter performance in production DSSE.

**R** — Identified systematic baseline-model errors across the substation fleet that were invisible at individual-substation scale — findings that informed model recalibration work affecting monitoring accuracy across Hydro-Québec's grid. Demonstrated production-scale integration of field sensor data from hundreds of substations into a single analytical pipeline — which is precisely the "integrate field data sources" and "T&D applications" proof point the JD requires.

---

### JD-line mapping

**Primary JD line:** "Integrate field data sources (SCADA, PMUs, DER controllers) and industrial IoT protocols (LoRa, MQTT, DNP3, Modbus)." — Story 3 demonstrates production-scale integration of real utility field data from hundreds of substations — the closest analog to SCADA/PMU data integration in Juan's experience.

**Secondary JD line:** "Domain Expertise: Proven experience with federated architectures, resilient edge software, and Transmission & Distribution (T&D) applications." — This is direct T&D application experience: real Hydro-Québec substation data, production scale, fleet-wide analysis informing grid monitoring.

**Retrieval trigger:** Any question invoking "field data integration," "T&D experience," "SCADA/sensor data at scale," "data pipelines," or "domain expertise" → use Story 3.

---

## Story 4: SI-MAPPER / MCP / Agentic AI → AGMS Scouts (the Differentiator)

*This is the #1 differentiator story. The GRANTED Operation Loop Formation patent (US 12,596,341 B2, assigned to GE Vernova) describes an architecture that maps component-by-component to what Juan built in SI-MAPPER. Do not rush this story — let the patent connection land.*

---

### Screen version (plain, ≤90 s)

**Opening hook (outcome-first):** "I built AI agents that explore an unknown building or grid, map all the connected assets on their own, and reason about how everything is connected — without a human telling them the layout. Then I read the director's patents and realized I had built the same thing."

1. **Situation:** Buildings and grid sites have hundreds of connected sensors and devices, but no structured map of what they are or how they connect — humans have to trace it all manually, which takes weeks.
2. **My role:** I built SI-MAPPER — an agentic AI system that explores a site autonomously, maps the assets into a structured knowledge graph, and reasons about relationships between them — no human configuration required.
3. **The technology:** AI agents that communicate via the Model Context Protocol (MCP), discover assets by querying and reasoning, and build a machine-readable map using an industry-standard vocabulary (ASHRAE 223P). Think of it as the building's own operating system that understands what it is.
4. **The GE Vernova connection:** After reading the director's patents, I found a direct match: the AGMS "scouts" are autonomous field agents that do exactly this at the grid level — the DNA map in the patent is the same kind of typed, relationship-aware asset fingerprint I built. And the Operation Loop Formation patent — which is already granted and assigned to GE Vernova — describes a simulate-before-commit control gate that is exactly what my CVXPY optimization engine does.
5. **The one-liner:** "I built the components of your lab's own patented architecture — in a different domain. Coming here means applying them at grid scale."

---

### Technical STAR (≤2 min)

**S** — Building and DER automation requires structured, machine-readable understanding of site topology and asset relationships — but this information exists only as unstructured, heterogeneous signals and documents. Manual mapping is the bottleneck for any automated control or reasoning system.

**T** — I designed and built SI-MAPPER: an agentic-AI system that autonomously constructs a typed, relationship-aware knowledge graph of a building or DER site from unstructured signals, using the Model Context Protocol (MCP) for agent-to-tool communication and the ASHRAE 223P ontology as the structural vocabulary.

**A:**
- Built a multi-agent reasoning system using MCP — agents that query sensors, parse unstructured data, infer asset type and relationships, and populate a structured ontology graph — the same no-central-coordination, distributed-inference pattern the JD calls for.
- Used ASHRAE 223P as the "DNA map" — a typed ontology encoding asset roles, relationships, and behavioral expectations. This IS the DNA map in AGMS Patent 3 (Asset Portfolio Manager): a structured fingerprint so automated agents can reason about inter-asset dependencies without human configuration.
- The K3s scheduler I use to place role-typed workloads on edge nodes IS the Scout Incubator Manager (AGMS Patent 5 — Scout Command): check which role-typed agents are available for the DNA-specified requirements, clone or instantiate new agents when a role is unfilled, reconcile desired state continuously.
- The CVXPY MPC control gate in OSED — solve and feasibility-check before dispatching to actuators — IS the simulate-before-commit gate in AGMS Patent 4 (Operation Loop Formation, US 12,596,341 B2, GRANTED and assigned to GE Vernova). Claim 3 of that patent gates execution on a learning engine that simulates the formation plan before causing devices to execute. I built this gate in a buildings domain; the grid version replaces the RC thermal model with LinDistFlow.
- Cross-link: For full depth on these patent connections, see `.planning/phases/03-director-s-patents-deep-read/notes/AGMS-patent-rehearsal-deck.md` — the per-patent connection table and the master narrative.

**R** — SI-MAPPER demonstrates automated asset-graph construction with no human configuration — a capability that scales the speed of deploying autonomous control to new sites from weeks to minutes. The AGMS patent connection is not retrospective framing: the architectural choices (typed ontology, multi-agent MCP coordination, simulate-before-commit gate, K3s workload reconciliation) were made for the same engineering reasons that appear in GE Vernova's granted patent. Coming to GE Vernova means integrating these experiences into the T&D-scale version of exactly this architecture.

---

### JD-line mapping

**Primary JD line:** "Integrate AI/ML capabilities, federated control frameworks, and digital twins into next-generation grid platforms." — SI-MAPPER integrates agentic AI (MCP-based multi-agent reasoning), a federated structural-prior pattern (no central data pool), and a knowledge graph that functions as a lightweight digital twin of the asset topology.

**Secondary JD line:** "Bridge the gap between simulation environments and live grid operations to 'close the loop.'" — The CVXPY MPC simulate-before-commit gate IS this bridge: simulate (solve the constrained optimization), verify feasibility and constraint satisfaction, then commit to live actuation. This is the direct analog to the Operation Loop Formation patent's simulate-before-commit discipline.

**Patent differentiator line (for any technical round):** "I built the components of the architecture described in US 12,596,341 B2 — Operation Loop Formation, GRANTED and assigned to GE Vernova — in a buildings domain. The DNA map is my ASHRAE 223P knowledge graph. The Scout Incubator Manager is my K3s scheduler. The simulate-before-commit gate is my CVXPY MPC. I haven't operated them at T&D scale — but I understand the architecture from the inside."

**Retrieval trigger:** Any question invoking "AI/ML," "digital twins," "agentic AI," "federated control," "autonomous agents," "patents," "simulation-to-field gap," or "close the loop" → use Story 4.

---

*Sources: KAL-01 (virtual-sensing fusion engine / OSED edge runtime), DSSE-03 (pseudo-measurement honesty / R_pseudo calibration — honesty framing for Story 1 and Story 2), DSSE-04 (AGMS Inspector scout placement / federated DSSE / simulate-before-commit connection), STK-03 (MQTT→NATS + K8s→K3s), AGMS-patent-rehearsal-deck.md (Patent 3 DNA map / Patent 4 Operation Loop Formation GRANTED / Patent 5 Scout Incubator Manager / Master Narrative), docs/job-requirements.md (JD lines quoted directly), 06-CONTEXT.md D-08 (four stories, two versions each, JD-mapped), 06-RESEARCH.md §"STAR Method Best Practices" (timing, outcome-first, Pitfall 4 structure).*
