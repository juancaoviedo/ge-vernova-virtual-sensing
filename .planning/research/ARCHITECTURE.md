# Architecture Research: Decentralized Grid Operations & Edge Virtual Sensing

**Domain:** Edge-native virtual sensing and decentralized grid operations
**Researched:** 2026-06-13
**Confidence:** MEDIUM-HIGH (standards verified via official docs; GE Vernova internals inferred from JD + GridOS public material)

---

## Standard Architecture

### System Overview

The canonical architecture for decentralized grid / edge virtual sensing uses four tiers.
"North-south" data flows from field to cloud; "east-west" peer coordination happens at the
edge tier without central coordination.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  CLOUD / ENTERPRISE LAYER                                                   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │ Digital Twin │  │  Fleet Mgmt  │  │  Analytics / │  │  GridOS Data  │  │
│  │  (Modelica / │  │  (K8s fleet  │  │  ML training │  │  Fabric /     │  │
│  │   graph DB)  │  │   GitOps)    │  │  (offline)   │  │  historian    │  │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └───────┬───────┘  │
│         └─────────────────┴──────────────────┴──────────────────┘          │
│                                gRPC / Pulsar / Kafka                        │
└─────────────────────────────────────────────┬───────────────────────────────┘
                                              │  (intermittent WAN)
┌─────────────────────────────────────────────┴───────────────────────────────┐
│  REGIONAL / FOG LAYER   (optional; multi-site aggregation)                  │
│  ┌────────────────────────────────────────────────────────────────────┐     │
│  │  Federated Aggregator  —  model-weight sync, consensus, alerting   │     │
│  │  NATS JetStream cluster  |  time-series rollup (InfluxDB)          │     │
│  └──────────────────────┬─────────────────────────┬───────────────────┘     │
└─────────────────────────┼─────────────────────────┼───────────────────────  ┘
                          │   east-west NATS         │   east-west NATS
┌─────────────────────────┴─────────┐ ┌─────────────┴────────────────────────┐
│  EDGE NODE A (substation / feeder)│ │  EDGE NODE B (DER cluster / microgrid)│
│                                   │ │                                        │
│  ┌─────────┐  ┌─────────────────┐ │ │  ┌─────────┐  ┌─────────────────┐   │
│  │Protocol │  │ Virtual Sensing │ │ │  │Protocol │  │ Virtual Sensing │   │
│  │Adapter  │  │ Engine          │ │ │  │Adapter  │  │ Engine          │   │
│  │(DNP3 /  │  │ (Kalman / EKF / │ │ │  │(Modbus /│  │ (thermal /      │   │
│  │IEC61850 │  │  ML inference)  │ │ │  │Zigbee / │  │  load / DER     │   │
│  │/GOOSE)  │  └────────┬────────┘ │ │  │BACnet)  │  │  state est.)    │   │
│  └────┬────┘           │          │ │  └────┬────┘  └────────┬────────┘   │
│       └────────┬───────┘          │ │       └───────────┬────┘             │
│  ┌─────────────▼──────────────┐   │ │  ┌───────────────▼──────────────┐   │
│  │ Local NATS broker          │   │ │  │ Local NATS broker            │   │
│  │ + InfluxDB (short-term)    │   │ │  │ + InfluxDB (short-term)      │   │
│  │ + K3s (workload orch.)     │   │ │  │ + K3s (workload orch.)       │   │
│  └────────────────────────────┘   │ │  └──────────────────────────────┘   │
└───────────────────────────────────┘ └──────────────────────────────────────┘
         ▲                                      ▲
         │ IEC 61850 GOOSE/SV / DNP3            │ MQTT / Modbus / Zigbee / LoRa
┌────────┴──────────────────┐        ┌──────────┴───────────────────────────┐
│  FIELD / PROCESS LAYER    │        │  FIELD / PROCESS LAYER               │
│  IEDs, PMUs, breakers,    │        │  DER controllers, EV chargers,       │
│  transformers, SCADA RTUs │        │  smart meters, building BMS           │
└───────────────────────────┘        └──────────────────────────────────────┘
```

---

## Component Responsibilities

| Component | Layer | Responsibility | Typical Implementation |
|-----------|-------|----------------|------------------------|
| Protocol Adapter / IED Interface | Edge | Ingests field data from IEDs/RTUs; translates DNP3 / IEC 61850 GOOSE/MMS / Modbus / MQTT into internal bus messages | Python driver or C++ IED gateway; Neuron for IEC 61850 → MQTT bridge |
| Virtual Sensing Engine | Edge | Infers unmeasured grid parameters (voltage, phase angle, line temp, asset health) from sparse sensor data | Python: Kalman / EKF for linear state; ML (LSTM, physics-informed NN) for nonlinear; CVXPY for optimization |
| Local Message Bus | Edge | Low-latency pub/sub within the edge node; east-west peer messaging without cloud | NATS (leaf node or cluster); MQTT broker for device-tier |
| Local Time-Series Store | Edge | Short-horizon buffering; operates during WAN outage | InfluxDB (edge) or TimescaleDB |
| Edge Orchestrator | Edge | Container lifecycle, rolling updates, health checks | K3s (lightweight K8s); KubeEdge for cloud-edge sync |
| Federated Aggregator | Fog/Regional | Collects model-weight deltas (FL rounds) or consensus signals from peer edge nodes; no raw field data leaves edge | Custom FL server (Flower framework) or NATS JetStream stream |
| Digital Twin | Cloud | High-fidelity physics model continuously calibrated against field data; offline + HIL/SIL | Modelica / OpenFMB / graph DB (Neo4j); OPAL-RT real-time sim for HIL |
| Grid Data Fabric | Cloud | Federates historian data across sites; unified CIM/IEC 61850 schema | GE GridOS Data Fabric; InfluxDB cluster; dbt for model transformations |
| Fleet Management | Cloud | GitOps-driven config push, ML model versioning, PKI certificate rotation | ArgoCD + K3s fleet; SPIFFE/SPIRE for identity |
| Analytics & Model Training | Cloud | Offline ML training on aggregated (anonymized) data; model artifact store | Spark / Databricks; MLflow; Prometheus + Grafana |

---

## Field Protocol Integration

### Protocol Stack by Domain

| Protocol | Physical Layer | Rate | Grid Domain | Use Case |
|----------|---------------|------|-------------|----------|
| IEC 61850 GOOSE | Ethernet (L2, no IP) | < 4 ms | Substation bay → bay | Fast protection tripping, breaker status |
| IEC 61850 SV (Sampled Values) | Ethernet (L2) | 80–256 samples/cycle | Process level | CT/VT merging unit streams to IEDs |
| IEC 61850 MMS | TCP/IP | seconds | Station → SCADA | Configuration, logging, control commands |
| DNP3 | Serial / TCP | 1–60 s | Feeder RTU → SCADA | SCADA telemetry, status, control |
| Modbus RTU/TCP | Serial / TCP | seconds | Distribution equipment | Legacy sensors, inverters, meters |
| MQTT | TCP/IP | sub-second | Edge → cloud, DER → gateway | Telemetry, event-driven IIoT |
| IEEE 2030.5 (SEP 2.0) | HTTPS/TLS over TCP | minutes (poll) | Utility server ↔ DER/EV | DER enrollment, dispatch commands, demand response |
| LoRaWAN | Radio LPWAN | minutes | Wide-area sensors | Low-bandwidth remote sensing (line temp, fault indicators) |
| DNP3 Secure Auth v5 | Serial / TCP | seconds | Critical SCADA | Authenticated SCADA for cyber-hardened outstations |

### IEC 61850 Three-Tier Hierarchy (for interviews)

```
Station Level     │  HMI, gateway, SCADA integration — MMS over TCP/IP
──────────────────┼──────────────────────────────────────────────────
Bay Level         │  IEDs (protection relays, bay controllers)
                  │  GOOSE (L2 pub/sub, < 4 ms) for peer IED events
                  │  MMS for config/logging to station
──────────────────┼──────────────────────────────────────────────────
Process Level     │  Merging units, CT/VT sensors, switchgear actuators
                  │  Sampled Values (SV) streams to IEDs
```

**IEC 61850 Information Model path:** `Server → Logical Device → Logical Node → Data Object → Data Attribute`
Example: `SubstationA/XCBR1$ST$Pos$stVal` = breaker 1 position status.

### IEEE 2030.5 vs IEC 61850 Positioning

- **IEC 61850**: Substation internal (bay-to-bay, sub-ms to seconds); strong data model; GOOSE is L2 only, never routed over WAN.
- **IEEE 2030.5**: Utility-to-DER/EV over internet (HTTPS REST polling); PKI mandatory; DER enrollment + dispatch; California Rule 21 mandated for new inverters.
- In a full stack: 61850 governs the substation, 2030.5 governs the utility-to-prosumer edge.

---

## Virtual Sensing Engine — Internal Design

```
Field Measurements (sparse)
        │
        ▼
┌───────────────────────────┐
│  Measurement Preprocessor │  ← timestamp alignment, unit conversion,
│                           │    bad-data detection (chi-squared test)
└────────────┬──────────────┘
             │
             ▼
┌────────────────────────────────────────┐
│  State Estimator                        │
│                                        │
│  Option A: Weighted Least Squares (WLS)│  classical SCADA SE; batch
│  Option B: Extended Kalman Filter (EKF)│  dynamic, PMU-rate, handles
│            or Unscented KF (UKF)       │  nonlinear power flow equations
│  Option C: Physics-Informed Neural Net │  data-driven when model unknown
│            (PINN) + KF correction loop │
└────────────┬───────────────────────────┘
             │  estimated state vector [V, θ, P, Q, I, T_line, ...]
             ▼
┌───────────────────────────┐
│  Derived Virtual Sensors  │  ← voltage stability index, line temperature
│                           │    (Joule heating model), asset health score,
│                           │    harmonic distortion estimate
└────────────┬──────────────┘
             │
             ▼
┌───────────────────────────┐
│  Local NATS publish       │  → edge control logic
│                           │  → upstream telemetry (throttled)
└───────────────────────────┘
```

**Kalman filter position in the stack:** The EKF serves as the real-time correction layer —
prediction step uses the power flow model (Jacobian linearization), update step fuses new
PMU/SCADA measurements. Output covariance matrix quantifies estimation uncertainty, which
is propagated to control decisions (risk-aware dispatch).

---

## Federated / Decentralized Coordination Patterns

### Pattern 1: Federated Learning for Shared Model Improvement (No Raw Data Sharing)

```
Edge Node A          Edge Node B          Edge Node C
  local data           local data           local data
      │                    │                    │
  train local          train local          train local
  model delta          model delta          model delta
      │                    │                    │
      └──────────────┬─────┘────────────────────┘
                     ▼
             Federated Aggregator
             (FedAvg or FedProx)
                     │
             global model update
                     │
             ┌───────┴───────┐
          push to         push to
          Node A          Node B ...
```

**What:** Each edge node trains on local sensor data; only weight deltas (not raw measurements) are transmitted. Aggregator merges deltas into a global model (FedAvg).
**When to use:** Virtual sensing models that need diversity across sites without privacy/security exposure of raw field data.
**Trade-offs:** Communication rounds add latency; convergence slower than centralized; requires careful handling of non-IID data across substations.

### Pattern 2: Peer-to-Peer Edge Coordination (NATS East-West)

```
Edge Node A ──NATS subject: grid.area7.voltage.alert──► Edge Node B
Edge Node B ──NATS subject: grid.area7.control.shed ──► DER Controller
```

**What:** Edge nodes publish state and control signals to a shared NATS subject hierarchy. Peer nodes subscribe and react without routing through a central orchestrator.
**When to use:** Real-time coordination (island detection, voltage support, frequency response) where cloud-round-trip latency (100–500 ms) is unacceptable.
**Trade-offs:** Requires conflict resolution when multiple nodes issue competing control; needs a distributed consensus or priority scheme (e.g., primary/backup designations).

### Pattern 3: Hierarchical Droop + MPC (Decentralized Control with Optional Cloud Overlay)

```
Local droop control (ms response)      ← always-on at edge, no communication
    │
Regional MPC (100 ms – 1 s)            ← runs at fog/regional node
    │                                     optimizes setpoints across a cluster
Cloud optimization (minutes)           ← economic dispatch, schedule updates
```

**What:** Layered control with faster loops handled entirely at edge. Cloud injects setpoints but does not participate in real-time response.
**When to use:** Microgrids, DER clusters, feeder voltage management; islanded operation must remain stable without cloud.
**Trade-offs:** Setpoint conflict possible if cloud schedule is stale; requires bumpless transfer logic when cloud connectivity is restored.

### Pattern 4: OpenFMB Node Architecture

Each physical grid device is wrapped as an OpenFMB node with:
- **Profile**: data model derived from IEC 61850 Logical Nodes + IEC CIM
- **Transport**: NATS or MQTT (pluggable)
- **Identity**: SPIFFE/SPIRE mTLS certificate per node
- **Behavior**: autonomous local control; publishes status; subscribes to dispatch

This makes every DER, breaker, meter a first-class network citizen that can operate standalone and also participate in coordinated orchestration — the "distributing intelligence to the resilient edge" pattern GE Vernova names explicitly.

---

## Simulation-to-Field Closed Loop (Sim-to-Field)

### Validation Ladder

```
Level 0 — Offline Simulation
  PSCAD / RTDS / Opal-RT
  Pure physics model; no live data
  → validate algorithm correctness in controlled fault scenarios

Level 1 — Software-in-the-Loop (SIL)
  Virtual sensing algorithm runs against recorded field data
  (or SCADA/PMU playback)
  → validate inference accuracy against known ground truth

Level 2 — Hardware-in-the-Loop (HIL)
  Real controller / edge node hardware ↔ real-time simulator
  (Opal-RT as emulated grid; edge node as device under test)
  → validate latency, I/O, protocol behavior

Level 3 — Pilot Field Deployment
  Edge node installed at substation; shadow mode
  (virtual sensors run in parallel, not in control loop)
  → validate against field SCADA ground truth

Level 4 — Closed-Loop Field Operation
  Virtual sensor feeds live control decisions
  → continuous feedback: field residuals recalibrate digital twin
```

### Digital Twin Feedback Loop

```
Field ──(SCADA / PMU)──► Digital Twin calibration
                              │
                         residual error
                              │
                         Kalman gain update
                         or model re-parameterization
                              │
                         updated parameters ──► virtual sensing engine
```

The digital twin is not a static model — it drifts-corrects continuously. Modelica / OpenFMB profiles define the physics structure; graph databases (Neo4j, RDF) store the network topology; real-time simulators (Opal-RT) provide a live-running twin for HIL testing.

---

## Data Flow: Field to Edge to Coordination to Cloud

```
[Field Sensors / IEDs / DERs]
   │
   │  IEC 61850 GOOSE/SV (< 4 ms, L2)
   │  DNP3 / Modbus / MQTT / LoRa (seconds to minutes)
   ▼
[Protocol Adapter — Edge Node]
   │  normalizes to internal schema (CIM / OpenFMB profile)
   │  bad-data rejection, timestamp alignment
   ▼
[Local NATS broker — Edge Node]
   │  pub/sub fanout to local consumers
   ├──► Virtual Sensing Engine (Kalman / ML inference)
   │         │  inferred state vector (V, θ, I, T, health)
   │         ▼
   │    [Local Control Logic]
   │    (droop, MPC, demand response dispatch)
   │         │  control actuation → back to field devices
   │         ▼
   │    [InfluxDB edge store]  ← short-term buffer (hours to days)
   │
   └──► [Federated Aggregator — fog or cloud] (throttled, compressed)
              │  model-weight deltas (FL), aggregate KPIs, alarms
              ▼
        [Cloud Data Fabric / Digital Twin / Fleet Mgmt]
              │  long-term storage, retraining, GridOS dashboards
              ▼
        [Operations Center / SCADA EMS/DMS]
```

**Key latency budget:**
- Field event → GOOSE: < 4 ms
- GOOSE → local virtual sensor update: 10–50 ms
- Virtual sensor → local control actuation: 50–200 ms
- Edge → cloud telemetry: 1–30 s (non-critical path)
- Cloud model update → edge: minutes to hours (async)

---

## How Juan's OSED Platform Maps to This Architecture

This is the core reframe. OSED is a concrete implementation of the edge-native virtual-sensing pattern — the vocabulary differs, the structure matches.

| GE Vernova / JD Concept | Juan's OSED Equivalent | Translation Note |
|--------------------------|------------------------|------------------|
| Edge-native software components (K3s) | Docker + Kubernetes at Hydro-Québec edge nodes | Upgrade path: K3s for constrained hardware; principle identical |
| Federated data pipelines, no central coordination | Distributed MQTT broker topology + pub/sub control flow | OSED uses centralized MQTT today; federated = peer NATS leaf nodes; architectural step, not a rebuild |
| Virtual sensing algorithms | Edge ML for building thermal state estimation (thermal model + ML correction) | Same structure: physics model + data-driven correction = virtual sensor for unmeasured state |
| Kalman filter / state estimation | Least Squares MPC in OSED (implicit state estimation) | Gap: OSED uses WLS-family batch; KF adds dynamic propagation step. Mechanically very similar — different update timing |
| IEC 61850 IED integration | Modbus + BACnet + Zigbee in OSED (building/DER side) | Same adapter pattern; different protocol driver. IEC 61850 is the T&D substation equivalent of Modbus |
| PMU / SCADA integration | InfluxDB historian from Hydro-Québec SCADA (PySpark on billions of points) | OSED consumed SCADA outputs at analysis layer; gap is real-time PMU protocol integration at 30–120 Hz |
| Distributed optimization (cloud formulate / edge execute) | CVXPY convex optimization at cloud, control setpoints pushed to edge via MQTT | Exact match to the decentralized MPC pattern — this is a direct strength to name explicitly |
| DER controllers as grid assets | HEMS PoC, controllable loads, EV/storage dispatch in OSED | Identical concept; OSED proves the pattern at building/distribution level; GE Vernova extends to T&D |
| Sim-to-field closed loop | N/A (gap) | Closest: OSED validated against Hydro-Québec field data offline. HIL/SIL with PSCAD/RTDS is a genuine gap |
| Digital twin (Modelica / OpenFMB) | Knowledge graph + agentic SI-MAPPER (ontology from CV data) | Graph-based modeling is a direct skill; OpenFMB profiles are IEC 61850-derived — IEC 61850 docs in hand |
| IEEE 2030.5 / OpenADR | OpenADR in OSED for demand response | OpenADR is the predecessor/complement to 2030.5; direct bridging capability |
| Streaming: Kafka / NATS / Pulsar | MQTT + GCP Pub/Sub | MQTT = lightweight NATS equivalent; Kafka/Pulsar = higher-throughput, durable log; operational concept identical, scale differs |
| gRPC inter-service | gRPC in OSED (Building Intelligence lib) | Direct match |
| Observability: Prometheus + Grafana | Grafana dashboards in OSED | Direct match |

### Three-Sentence Interview Reframe

"My OSED platform at Hydro-Québec is a production hybrid cloud-edge system that does exactly what this role describes: edge ML infers building thermal state — a virtual sensor for an unmeasured physical quantity — and the cloud formulates optimization problems that are dispatched as setpoints executed locally. The MQTT/K8s/InfluxDB/gRPC stack I built is the distribution-side analog of the K3s/NATS/InfluxDB stack named in the JD. The concrete gap I'm closing is extending from building/DER virtual sensing to transmission-side parameter estimation using Kalman filters and PMU/SCADA feeds — which is why I want to join this team."

---

## Architectural Patterns to Follow

### Pattern: Adapter-Bus-Engine Separation

Keep protocol adapters, local message bus, and sensing/control engines as separate processes (separate K3s pods). Adapter owns all protocol-specific code; engine is pure domain logic; bus decouples them. This means swapping DNP3 for IEC 61850 only touches the adapter pod.

### Pattern: Store-and-Forward with Offline Resilience

Edge node must operate autonomously during WAN outage. Design: edge InfluxDB buffers all local data; NATS JetStream persists inter-node messages; control logic has no hard dependency on cloud reachability. Cloud sync resumes when WAN returns (store-and-forward).

### Pattern: Shadow Mode Before Closed Loop

Always deploy virtual sensors in parallel with ground-truth SCADA first. Log residuals. Only promote to closed-loop control after residual bounds are acceptable. This is the sim-to-field ladder step 3 → 4.

---

## Anti-Patterns to Avoid

### Anti-Pattern 1: Cloud-Dependent Real-Time Control

**What people do:** Route all control decisions through a centralized cloud optimizer; edge nodes are dumb data forwarders.
**Why it's wrong:** Any WAN interruption disables control; round-trip latency (100–500 ms) too slow for protection-grade response; single point of failure.
**Do this instead:** Edge runs local droop/MPC autonomously. Cloud provides updated setpoints on slower cycle. Edge applies last-known-good setpoint during outage.

### Anti-Pattern 2: Raw Data Exfiltration Instead of Edge Inference

**What people do:** Stream all raw PMU samples (30–120 Hz × many channels) to cloud for processing.
**Why it's wrong:** Bandwidth-prohibitive; privacy/security risk; defeats the purpose of edge intelligence.
**Do this instead:** Run Kalman / ML inference at edge; transmit compressed state estimates and anomaly events only.

### Anti-Pattern 3: Single Protocol Assumption

**What people do:** Design the protocol adapter assuming all field devices speak MQTT or all speak DNP3.
**Why it's wrong:** Real substations have IEC 61850 IEDs, legacy Modbus meters, LoRa sensors, and SCADA RTUs simultaneously.
**Do this instead:** Adapter layer as a plugin registry; each driver implements a common `MeasurementSource` interface; bus schema is protocol-neutral (CIM / OpenFMB profile).

### Anti-Pattern 4: Treating Digital Twin as a One-Time Build

**What people do:** Build a static Modelica model at project start; treat it as ground truth indefinitely.
**Why it's wrong:** Grid topology changes (new DERs, line upgrades); seasonal equipment parameters drift; model diverges from field reality.
**Do this instead:** Continuous calibration loop — field residuals (measured minus estimated) drive parameter update. Kalman filter's state covariance matrix is a natural mechanism for this.

---

## Integration Points

### External Services

| Service | Integration Pattern | Notes |
|---------|---------------------|-------|
| SCADA / EMS | DNP3 or IEC 61850 MMS client; InfluxDB historian poll | SCADA is the ground truth for SE validation; latency is seconds |
| PMUs | IEEE C37.118 over PDC (Phasor Data Concentrator) → internal bus | 30–120 Hz; requires GPS-synchronized timestamps (UTC microsecond) |
| DER Controllers | MQTT or Modbus or IEEE 2030.5 depending on vintage | Inverters post-2020: often 2030.5; legacy: Modbus |
| LoRa Sensors | LoRaWAN gateway → MQTT bridge → edge broker | Low-rate (minutes); useful for remote line temperature, fault indicators |
| EMT Simulators (PSCAD/RTDS/Opal-RT) | FMI/FMU model exchange; TCP/UDP I/O for HIL | Used in SIL/HIL stages; not in production control path |
| Cloud Data Lake | NATS → Kafka/Pulsar bridge or direct gRPC stream | Pulsar preferred for multi-tenant multi-region; Kafka acceptable |

### Internal Boundaries

| Boundary | Communication | Notes |
|----------|---------------|-------|
| Protocol Adapter ↔ Local Bus | NATS pub/sub (subject per data type) | Adapter publishes normalized measurements; bus routes to consumers |
| Virtual Sensing Engine ↔ Control Logic | NATS request-reply or shared InfluxDB measurement | Engine publishes state; control logic subscribes and issues setpoints |
| Edge Node ↔ Fog Aggregator | NATS leaf node or gRPC stream (WAN-tolerant) | Leaf node is NATS-native; gRPC for richer schema control |
| Fog Aggregator ↔ Cloud Twin | gRPC or Kafka topic per site | Batched model deltas; near-real-time alarms |
| Cloud Fleet Mgmt ↔ Edge Nodes | GitOps pull (ArgoCD) + SPIFFE/SPIRE certificate push | Edge pulls config; avoids inbound firewall holes |

---

## Scaling Considerations

| Scale | Architecture Adjustment |
|-------|--------------------------|
| 1–5 edge nodes | Single NATS cluster; monolithic edge service; InfluxDB single-node |
| 10–100 edge nodes | NATS JetStream cluster for durability; K3s fleet via GitOps; federated learning rounds become tractable |
| 100–10,000 nodes | NATS super-cluster (geo-distributed); Kafka/Pulsar for cloud ingestion at scale; horizontal InfluxDB (Cluster or IOx); federated learning with hierarchical aggregation |

**First bottleneck:** WAN bandwidth (raw data volume from field devices). Fix: edge inference before transmission.
**Second bottleneck:** NATS broker throughput at fog tier. Fix: partition by geographic area; separate subjects per region.

---

## Sources

- IEC 61850 architecture and GOOSE/MMS/SV: [EMQ IEC 61850 Protocol Guide](https://www.emqx.com/en/blog/iec-61850-protocol)
- OpenFMB edge node architecture: [OpenFMB Home](https://openfmb.org/); [SEPA OpenFMB article](https://sepapower.org/knowledge/openfmb-charts-new-paths/); [OSTI Microgrid Communications](https://www.osti.gov/servlets/purl/1885229)
- K3s + NATS for grid edge (ZTAG / Duke Energy pattern): [SUSE K3s + NATS](https://www.suse.com/c/k3s-and-nats-a-technology-stack-developers-love-to-use-at-the-edge/)
- IEEE 2030.5 DER protocol: [Codibly IEEE 2030.5 guide](https://codibly.com/blog/articles/the-role-of-ieee-2030-5-in-enabling-smart-grid-communication-bridging-technologies-and-utilities)
- Kalman filter + PMU/SCADA state estimation: [MDPI Energies — PMU/SCADA fusion SE](https://www.mdpi.com/1996-1073/17/11/2609)
- Digital twin / sim-to-field closed loop: [OPAL-RT Digital Twin Guide](https://www.opal-rt.com/blog/guide-to-digital-twin-applications-in-power-systems/)
- GE GridOS federated architecture: [GE Vernova GridOS](https://www.gevernova.com/software/products/gridos)
- Federated learning for grid: [NCBI Federated Learning in Critical Infrastructure](https://www.ncbi.nlm.nih.gov/books/NBK602372/)
- Self-healing microgrid coordination: [IowaState Networked Microgrids](https://wzy.ece.iastate.edu/CV/c118.pdf)
- DNP3 / protocol strategy: [Mikrodev IEC 61850 vs DNP3 vs IEC 60870](https://www.mikrodev.com/iec-61850-iec-60870-and-dnp3-strategic-protocol-selection-and-architecture-in-substation-scada-projects/)
- IntelliGrid (EPRI): [IEEE Xplore IntelliGrid + IEC 61850](https://ieeexplore.ieee.org/document/1668526/)

---

*Architecture research for: Decentralized Grid Operations & Edge Virtual Sensing*
*Researched: 2026-06-13*
