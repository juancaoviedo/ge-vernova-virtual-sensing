**For:** Technical-round whiteboard rehearsal (rounds 2–4) — practice drawing each ASCII diagram from memory, then narrate it aloud.
**Purpose:** Walk two system designs from memory, demonstrating architecture fluency under interview pressure — satisfying QNA-02 and ROADMAP success criterion 4.

*Depth strategy: FULL depth for narration and justification; EMT tooling (Drill 2) at AWARENESS level only per CLAUDE.md depth ceiling — name the tools, do not claim hands-on depth. Both drills adapted from Phase 4 STK-05 and Phase 2 DSSE-04 (D-16: no new technical content).*

---

## Drill 1: 500-Node Virtual Sensing Pipeline

> Technical-round target: ~5 minutes end-to-end. The first 90 s draws the diagram; the next
> 3 min narrates bottom-to-top; the last 30 s lands the AGMS hook.

### Problem Statement

A utility operates 500 distribution substations across a regional territory. Most feeders are
under-observed — fewer than 60 % of nodes have real-time sensors. The engineering team needs a
virtual-sensing pipeline that (1) infers unmeasured node states at sub-second latency at each
substation, (2) aggregates model weight updates across the fleet without centralizing raw data,
and (3) pushes configuration changes and model updates to all 500 nodes reliably, even across
poor WAN links.

Design a four-tier architecture that meets these constraints.

### ASCII Whiteboard Diagram

*Draw this in ~90 seconds. Top-to-bottom, one tier per row.*

```
┌─────────────────────────────────────────────────────────────────────┐
│  CLOUD (minutes+)                                                   │
│  Kafka · OSIsoft PI / InfluxDB historian · Azure ML                 │
│  GitOps (Flux/ArgoCD) ──push config──► K3s fleet (500 nodes)       │
│  Grafana/PromQL · Alertmanager                                      │
│  GWM — alert correlation + learning engine  ← AGMS                 │
└──────────────────────────┬──────────────────────────────────────────┘
                           │ NATS JetStream (hub → cloud bridge)
┌──────────────────────────▼──────────────────────────────────────────┐
│  FOG / FEDERATED (seconds–minutes)                                  │
│  NATS JetStream hub · Cross-substation EKF aggregation             │
│  Flower federated aggregator — FedAvg weight exchange               │
│  GWCH (ORACS formation, simulate-before-commit)  ← AGMS            │
└──────────────────────────┬──────────────────────────────────────────┘
                           │ NATS JetStream (leaf node → hub)
┌──────────────────────────▼──────────────────────────────────────────┐
│  EDGE — K3s substation node ×500 (100 ms – 1 s)                    │
│  EKF virtual-sensing engine · NATS JetStream leaf · Prometheus      │
│  Island mode: local JetStream buffer sustains loop if WAN drops     │
│  FADs + Scout Command (grid-semantics pod scheduling)  ← AGMS      │
└──────────────────────────┬──────────────────────────────────────────┘
                           │ IEC 61850 GOOSE/SV · DNP3 · C37.118 · LoRa
┌──────────────────────────▼──────────────────────────────────────────┐
│  FIELD (<4 ms – 100 ms)                                             │
│  XCBR circuit breakers · PMUs (30–120 fps GPS-synced)              │
│  RTUs · Merging Units · LoRa sensors (km-range battery)            │
│  GOOSE: <4 ms protection · SV: I/V samples · DNP3: telemetry       │
└─────────────────────────────────────────────────────────────────────┘
```

### Narration Script

Narrate bottom-to-top. One spoken paragraph per tier with "why this component" justification.

**1. Field tier — the sensing layer:**

> "I start at the bottom — the field tier. Circuit breakers are modeled as XCBR. PMUs deliver
> GPS-synced phasors at 30 to 120 frames per second, which gives us synchrophasor data for
> observability. RTUs and merging units handle conventional SCADA telemetry. LoRa sensors cover
> pole-top and rural assets on battery for years at kilometer range. Protection happens here in
> under 4 milliseconds via IEC 61850 GOOSE — that is a Layer 2 Ethernet frame, it never leaves
> the substation LAN, and there is no software round-trip. GOOSE and Sampled Values cannot be
> routed; they are the hardwired protection boundary."

**2. Edge tier — the inference and island node:**

> "One level up, each of the 500 substations runs a K3s node. K3s is Kubernetes with a 512 MB
> footprint and a single binary install — it runs in a substation closet on commodity hardware,
> air-gapped if needed. On that node, the EKF virtual-sensing engine runs as a FastAPI pod: it
> ingests available measurements and estimates the unmeasured node states at sub-second latency —
> no round-trip to the cloud. NATS JetStream runs as a leaf node: it handles local pub/sub for
> the control loop and buffers all messages durably for cloud replay the moment WAN comes back.
> That is island mode — if the WAN drops, the inference and local control keep running. Prometheus
> scrapes the pod metrics natively from the K3s service-discovery registry."

**3. Fog tier — federated coordination:**

> "The fog tier is where the 500 edge nodes coordinate without centralizing raw data. A NATS
> JetStream hub aggregates their state estimates and event streams across substations — seconds
> to minutes decisions that need more than one substation's data. The Flower federated aggregator
> runs here: each K3s node trains a local EKF residual model on its own telemetry and sends only
> the weight update — not the raw PMU streams — to Flower's FedAvg aggregation step. The global
> model goes back to all 500 nodes next round. Raw substation telemetry never leaves the substation.
> This is the 'federated data pipeline, no central coordination' requirement from the JD."

**4. Cloud tier — historian, training, and GitOps:**

> "At the top, Kafka ingests the event stream from the fog tier — I keep Kafka here, not at the
> edge, because Kafka needs 64 to 128 GB RAM and a JVM; it is a semi-truck, not a bicycle for
> a substation closet. OSIsoft PI or InfluxDB stores long-term history. Azure ML handles model
> training and versioning. Grafana over PromQL gives fleet-wide dashboards; Alertmanager routes
> anomalies. And GitOps — Flux or ArgoCD — is how configuration and updated model weights get
> pushed declaratively to all 500 K3s nodes. One git commit triggers a sync to the entire fleet.
> No protective control comes from the cloud — only minutes-or-longer decisions reach this tier."

**5. AGMS overlay — the differentiation move:**

> "If I overlay the director's AGMS patent family: the Field Agent Devices running Inspector
> scouts land at the edge tier — that EKF engine IS the Inspector scout in the AGMS vocabulary.
> Scout Command is the K3s pod scheduler running with grid semantics. The Flower federated
> aggregator + NATS hub at the fog tier implements what the GWCH orchestrates in the patent —
> cross-substation coordination and the Operation Loop simulate-before-commit gate. That gate is
> in the allowed claims of the GRANTED patent, US 12,596,341 B2, assigned to GE Vernova.
> GridWideMind sits at the cloud tier as the learning and alert-correlation engine. The
> architecture is not just a good design choice — it is the blueprint the director already built
> and patented."

### Key Justification One-Liners

| Component | One-liner (say in ≤10 s) |
|-----------|--------------------------|
| **K3s** | "Same Kubernetes API, 4× lighter footprint — 512 MB RAM, single binary, air-gap native; the only orchestrator that runs in a substation closet." |
| **NATS JetStream** | "MQTT for devices, NATS for services — adds durable replay and island-mode buffer so the control loop keeps running when WAN drops." |
| **EKF engine** | "Estimates unmeasured node states at sub-second latency from available telemetry and a linearized grid model — virtual sensing without a physical sensor at every node." |
| **Flower federated aggregator** | "Train at edge, share weight deltas, never move raw PMU streams — satisfies 'federated, no central coordination' and keeps raw telemetry inside each substation." |
| **GitOps** | "Declarative fleet config: one git commit pushes a model or config update to all 500 K3s nodes via Flux/ArgoCD — no manual SSH, full audit trail, convergent desired-state enforcement." |

### AGMS Closing Hook

> "The director's AGMS patent family maps exactly onto this four-tier design:
>
> - **Edge (Tier 2):** Field Agent Devices running scouts (Coordinator, Messenger, Inspector, Guard)
>   → the K3s node is the FAD; the EKF pod is the Inspector scout; Scout Command is the K3s
>   scheduler with grid semantics (patent: Scout Command module 1441 → 1447).
> - **Fog (Tier 3):** GridWideCommandHub (GWCH) orchestrates ORACS formation and runs the
>   Operation Loop Formation simulate-before-commit gate — the GRANTED GE Vernova patent,
>   US 12,596,341 B2.
> - **Cloud (Tier 4):** GridWideMind (GWM) handles alert correlation and long-horizon learning —
>   directly the Azure ML + Alertmanager layer at the cloud tier.
>
> Interview one-liner: 'The patent family is a blueprint I have been building the components of —
> independently, in buildings and DER — with the same architectural DNA: edge runtime for scouts,
> pod scheduler as Scout Incubator, CVXPY MPC as the simulate-before-commit gate.'"

*Cross-reference: `.planning/research/patents/INDEX.md` (full AGMS component map); STK-05
(four-tier diagram origin); FED-01 (Flower/FedAvg depth).*

*Target time: ~5 minutes total — 90 s diagram, 3 min narration, 30 s AGMS hook.*

---

## Drill 2: Close the Loop — Simulation / Digital Twin → Field Validation

> Technical-round target: ~5 minutes end-to-end. The first 60–90 s draws the loop diagram;
> the next 3 min walks the 4-step close-the-loop narration; the last 30 s lands the AGMS
> patent hook.

### Problem Statement

A utility has deployed virtual sensors (EKF/FASE estimators) at 500 substations. Engineering
asks: how do you know the virtual sensor output is trustworthy? The JD requires that you
"validate virtual sensor performance against physical models and real-world field data" and
"bridge the gap between simulation environments and live grid operations to close the loop."

Design a validate-before-act loop that (1) baselines virtual sensor output against a physics
model, (2) detects divergence and triggers a field-validation request, and (3) feeds field
data back to retrain the model — completing a closed cycle from simulation to live grid control.

### ASCII Whiteboard Diagram

*Draw this loop in ~90 seconds. It is a cycle — draw it as a clockwise loop.*

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CLOSE-THE-LOOP CYCLE                             │
│                                                                     │
│  ┌────────────────────┐    baseline      ┌─────────────────────┐   │
│  │  EMT / Digital     │─────────────────►│  Virtual Sensor     │   │
│  │  Twin Model        │  (expected       │  (EKF/FASE output)  │   │
│  │  (PSCAD/RTDS/      │   state)         │  $(\hat x, P)$      │   │
│  │   Opal-RT)         │                  └──────────┬──────────┘   │
│  └────────────────────┘                             │               │
│           ▲                                         │ compare       │
│           │ retrain / recalibrate                   ▼               │
│           │                               ┌─────────────────────┐  │
│  ┌────────┴───────────┐   field data      │  Comparator         │  │
│  │  Field Validation  │◄──────────────────│  divergence > θ?    │  │
│  │  (physical sensor  │                   └──────────┬──────────┘  │
│  │   dispatch /       │                             │               │
│  │   additional       │      trigger field          │ YES           │
│  │   measurement)     │◄────validation request──────┘               │
│  └────────────────────┘                                             │
│           │                                                         │
│           │ validated data                                          │
│           └────────────────────────────────────────────────────────►│
│                                        feeds back to control logic  │
└─────────────────────────────────────────────────────────────────────┘
```

### Narration Script

Walk the 4 steps in sequence. Each step is one spoken paragraph.

**Step 1 — EMT / digital-twin model baseline (AWARENESS level):**

> "The loop starts with a physics model — what engineers call an EMT model or a digital twin.
> Tools like PSCAD, RTDS, or Opal-RT build high-fidelity electromagnetic transient models of the
> distribution network: every conductor, transformer, and DER represented with physics equations.
> I want to be clear about depth here — I know these tools at awareness level; the substation
> protection and power-systems engineers own this model. What matters architecturally is that this
> model gives us a trusted expected state for the feeder under known conditions. It is the
> ground truth reference against which we validate."

**Step 2 — Virtual sensor output vs. model output comparison:**

> "The virtual sensor — the EKF or FASE estimator running on the K3s edge node — produces a
> posterior state estimate and a covariance: $(\hat x, P)$. The comparator continuously checks
> the virtual sensor output against the model's expected state. Small, bounded differences within
> the posterior uncertainty band are fine — that is the filter working as intended. We are looking
> for systematic divergence: the virtual sensor consistently over- or under-estimating voltage at
> a node, or covariance inflating for no good reason. That divergence is the signal that something
> has changed — a new DER connection, a metering fault, a model parameter that is no longer
> accurate."

**Step 3 — Divergence triggers a field-validation request:**

> "When the comparator detects that divergence exceeds a threshold — let us say the residual is
> outside the 3-sigma confidence interval for more than N consecutive cycles — it generates a
> field-validation request. That is a concrete engineering action: dispatch a portable power
> quality meter, task a field crew to verify that substation's topology, or activate a PMU
> on a previously un-instrumented node temporarily. The virtual sensor's covariance tells us
> exactly which node's estimate is uncertain — the field crew goes to that specific location,
> not to the whole feeder. That is the efficiency gain: targeted validation, not blanket
> re-measurement."

**Step 4 — Field data retrains the model; the loop closes to live edge control:**

> "The field measurement comes back. It either confirms the virtual sensor was right — in which
> case we update confidence and continue — or it reveals a model error, in which case we
> recalibrate the prior: fix the line impedance, update the DER capacity assumption, adjust the
> load pseudo-measurement model. That recalibrated model goes back into the digital twin AND back
> into the EKF prior on the K3s edge node. The loop is now closed — we started from a simulation,
> validated against physical reality, and the live edge control is now better calibrated than
> before. This is exactly the JD phrase: 'bridge the gap between simulation environments and live
> grid operations.'"

### Key Justification One-Liners

| Design choice | One-liner (say in ≤10 s) |
|---------------|--------------------------|
| **Why validate-before-act** | "The virtual sensor's covariance tells you how much to trust the estimate — but it only bounds model-consistency error, not model-accuracy error. Field validation closes the accuracy gap." |
| **Why a digital twin as baseline** | "An EMT model gives us a trusted physical ground truth — it answers 'what should the sensor read?' so the comparator knows what 'wrong' looks like before any physical sensors are deployed." |
| **Why the loop must close to the edge** | "If recalibration stops at the cloud historian, the live edge control still runs on the old prior. The loop is only closed when the updated EKF prior reaches the K3s node and the inference improves where it matters — at sub-second latency, on the feeder." |
| **Why targeted field validation** | "The posterior covariance $P$ tells us exactly which nodes are uncertain. We dispatch a field crew to those nodes specifically — targeted validation is 10× cheaper than a full re-survey." |

### AGMS Closing Hook

> "The Operation Loop Formation patent — US 12,596,341 B2, GRANTED and assigned to GE Vernova
> — is the patent embodiment of this exact validate-before-act philosophy. Its core claim is the
> simulate-before-commit gate: before the AGMS dispatches any control command (reactive power
> injection, scout deployment, DER setpoint change), it takes the current DSSE posterior
> $(\hat x, P)$, runs a fast power-flow simulation, and checks that the proposed action satisfies
> all voltage, current, and thermal constraints — with probability accounting for the state
> uncertainty $P$ — before committing. The field-validation loop I just described IS the outer,
> slower version of that same gate: simulate (digital-twin baseline), compare (virtual sensor
> output), validate (field measurement), then commit (recalibrate and dispatch live control).
>
> Interview one-liner: 'Simulate-before-commit is model-predictive control with a probabilistic
> safety gate derived from the posterior covariance. I built that pipeline in CVXPY for building
> control; the distribution grid version replaces the RC thermal model with LinDistFlow and the
> digital twin. The Operation Loop patent is the formalization of the discipline I already apply
> in my own work.'"

*Cross-reference: DSSE-04 §4 (simulate-before-commit, patent claim 3); AGMS-patent-rehearsal-deck.md
(Operation Loop Formation, 90-s pitch, Assembly Line diagram); KAL-03 (FASE feeder walk — the
inner loop the digital twin validates against).*

*Target time: ~5 minutes total — 90 s loop diagram, 3 min 4-step walk, 30 s AGMS hook.*
