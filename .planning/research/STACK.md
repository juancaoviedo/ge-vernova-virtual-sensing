# Stack Research — GE Vernova Virtual Sensing & Decentralized Grid Operations

**Domain:** Edge-native virtual sensing, decentralized grid operations, IIoT, federated ML
**Researched:** 2026-06-13
**Confidence:** HIGH (streaming/messaging, K3s, Prometheus) | MEDIUM (grid protocols, federated frameworks)

---

## Purpose of This Document

This is interview-prep study material for Juan, not a build spec. Each item answers:
"What is this, why does it matter for this role, how does it compare to what I already use,
and what's the one thing to say about it in an interview?"

Juan's existing strengths (Python, FastAPI, Kubernetes, MQTT, Modbus, BACnet, OpenADR,
InfluxDB, TimescaleDB, Grafana, gRPC, Redis, CVXPY, Azure ML, Databricks/PySpark) do NOT
need to be re-studied — they should be reframed in GE Vernova's language during interview.
This document focuses on the **named gaps** in the JD.

**One-week priority:** Kafka/NATS > K3s > DNP3/PMU/SCADA > Prometheus > Federated > LoRa/Pulsar

---

## Category 1: Streaming & Messaging (Gap: Kafka, NATS, Pulsar vs. Juan's MQTT)

### Mental Model First: What Juan Already Has vs. What He Needs

Juan uses **MQTT** (lightweight pub/sub for IoT devices, broker-mediated, fire-and-forget
by default, QoS 0/1/2). MQTT is a push-based device-to-cloud protocol designed for
constrained devices. It does not offer durable replay, horizontal stream processing, or
exactly-once semantics natively.

The JD adds **Kafka, NATS, and Pulsar** — these are distributed log/message-streaming
systems used for **service-to-service and edge-to-cloud data pipelines**, not device
communication. They layer *above* MQTT in the data path.

**Data path mental model:**
```
Field sensor
   → MQTT (device transport layer)
   → Edge broker / adapter
   → NATS or Kafka (stream backbone / federation)
   → Cloud aggregator / TSDB / ML pipeline
```

---

### NATS + JetStream (HIGH PRIORITY — matches JD's "NATS" and edge context exactly)

**What it is:** Ultra-lightweight, cloud-native messaging system. Single ~20 MB binary,
no JVM, no ZooKeeper. Core NATS is pure pub/sub (at-most-once). JetStream (persistence
layer, added in v2.2) adds durable streams, exactly-once delivery, key-value store, and
object store.

**Current version:** NATS Server 2.11 (late 2024–2025 release line). Actively maintained
by Synadia.

**Why it matters for this role:** NATS is the only mainstream messaging system designed
to run from Raspberry Pi edge node all the way to cloud supercluster using the **same
security context and subject namespace**. This is precisely the "distributed nodes
collaborate without central coordination" pattern the JD describes. JetStream's
store-and-forward mode lets an edge node buffer data locally during connectivity loss,
then replicate to the cloud when the link recovers — critical for grid edge deployments.

**Comparison to what Juan knows:**

| Dimension | MQTT (Juan has) | NATS/JetStream (gap) |
|-----------|-----------------|----------------------|
| Target user | Devices → broker | Services ↔ services + devices |
| Persistence | Optional (broker-side, short) | JetStream: durable log, replay |
| Edge footprint | Broker (Mosquitto ~1 MB) | Server binary ~20 MB, similar |
| Topology | Star (all through broker) | Leaf nodes + clusters: mesh |
| Exactly-once | No | Yes (JetStream) |
| Request-reply | Manual correlation | Built-in pattern |
| Security model | Username/password, TLS | Decentralized JWT accounts |
| Multi-tenancy | No | Yes (accounts = isolation) |

**Interview line:** "NATS gives us MQTT's edge-lightweight footprint plus Kafka-grade
durability and a leaf-node topology that lets each substation or field device run
autonomously and sync to the cloud without any central broker as a SPOF."

**What to study (1 hour):** NATS leaf node concept, JetStream streams vs. consumers,
how subject namespaces map to grid topology (e.g., `grid.substation.A.voltage`).

---

### Apache Kafka (MEDIUM PRIORITY — named in JD but over-engineered for edge)

**What it is:** Distributed, durable, append-only commit log. The industry standard for
high-throughput event streaming in data centers and cloud pipelines. Originally from
LinkedIn, now Apache project. As of v4.0 (March 2025), ZooKeeper is fully removed —
Kafka runs in KRaft (Raft-based) mode only. Current stable: **v4.2.0 (Feb 2026)**.

**Why it matters for this role:** Kafka is where edge-collected telemetry flows once it
reaches the cloud aggregation layer. In a GE Vernova architecture, Kafka likely handles
the stream from hundreds of substations into the ML pipeline, historian ingest, and
alerting. Juan needs to know Kafka's mental model (topics, partitions, consumer groups,
offsets) and where it lives in the pipeline.

**Comparison to NATS:**

| Dimension | Kafka | NATS JetStream |
|-----------|-------|----------------|
| Throughput ceiling | Millions msgs/sec | ~10M msgs/sec (lower overhead) |
| Edge deployment | NOT suitable (8 cores, 64–128 GB RAM) | Yes (single binary, Pi-class) |
| Minimum footprint | Significant (JVM + disk) | ~512 MB RAM |
| Durability | Excellent (log-based) | Good (JetStream) |
| Ecosystem | Enormous (connectors, Schema Registry, Flink) | Growing |
| Learning curve | High | Lower |

**Interview line:** "Kafka is the right choice at the cloud aggregation tier where you're
ingesting from hundreds of substations at high throughput and need rich connector
ecosystems. At the substation edge itself, Kafka is too heavy — that's where NATS or
a lightweight MQTT bridge wins."

**What to study (30 min):** Topic/partition/consumer-group mental model, how offsets
enable replay. Know that v4.x dropped ZooKeeper.

---

### Apache Pulsar (LOW PRIORITY — named in JD but less field-dominant than Kafka/NATS)

**What it is:** Multi-tenant, geo-replicated message streaming system. Originally from
Yahoo. Distinguishes itself by **separating the broker layer (compute) from BookKeeper
(storage)** — this allows independent scaling of compute vs. storage. Good for multi-cloud
or multi-region grid coordination scenarios.

**Why it matters for this role:** Pulsar was explicitly named in the JD alongside
Kafka/NATS. The separation-of-storage architecture is relevant when GE Vernova needs to
run a streaming backbone across multiple regions (e.g., a transmission system spanning
states) without coupling message throughput to storage growth.

**Comparison to Kafka:**

| Dimension | Kafka | Pulsar |
|-----------|-------|--------|
| Architecture | Broker = log storage | Broker + BookKeeper (separate) |
| Multi-tenancy | Needs external tooling | Native (namespaces, tenants) |
| Geo-replication | Add-on (MirrorMaker) | Built-in |
| Edge suitability | Poor | Poor (also heavy) |
| Maturity/ecosystem | Larger | Smaller (13K stars vs Kafka's 27K) |

**Interview line:** "Pulsar's separated storage layer is compelling for geo-distributed
grid control where you want to scale compute and storage independently, but for edge
nodes it's too heavy — same as Kafka."

**What to study (20 min):** Topic/subscription model (exclusive, shared, failover,
key-shared), tenant/namespace hierarchy.

---

### MQTT (Juan's strength — reframe, don't re-study)

MQTT remains the device-layer protocol here. In an interview, connect it up: "I've
shipped production MQTT pipelines for DER control and building automation. In a grid
context, I'd use MQTT at the IED/sensor layer and bridge to NATS or Kafka for the
federated pipeline tier."

---

## Category 2: Edge Orchestration (Gap: K3s vs. Juan's full Kubernetes)

### K3s (HIGH PRIORITY)

**What it is:** Certified Kubernetes distribution packaged as a single ~50 MB binary,
optimized for edge, ARM, IoT, and resource-constrained environments. Developed by Rancher
Labs (now SUSE). Removes cloud-provider integrations, legacy alpha APIs, and replaces
etcd with SQLite (default) or embedded etcd for HA. 100% upstream K8s API compatible.

**Current version:** K3s 1.31.x / 1.32.x (tracking upstream Kubernetes).

**Why it matters for this role:** The JD names "Kubernetes/K3s" together. K3s is what
you deploy to each substation gateway, field SCADA node, or edge compute device where
full K8s would be over-provisioned. Juan's existing K8s expertise transfers directly —
the API is identical, the difference is operational:

| Dimension | K8s (Juan has) | K3s (gap) |
|-----------|----------------|-----------|
| RAM minimum | ~2 GB per node | ~512 MB per node |
| etcd | External cluster required | Embedded (SQLite/etcd) |
| Container runtime | containerd, CRI-O | containerd (included) |
| Install | kubeadm / Helm | `curl | sh` single binary |
| ARM support | Limited | First-class (Pi, Jetson) |
| Ingress | Choose your own | Traefik included |
| Storage | External provisioner | Local-path provisioner included |
| Air-gap operation | Complex | Designed for it |
| HA | Full etcd cluster | K3s HA mode (embedded etcd) |

**Interview line:** "K3s is how I'd containerize the virtual-sensing stack at the
substation level — same Helm charts and Kubernetes manifests as cloud, but running on
a $50 SBC. The air-gap and offline-capable design matters when a substation loses WAN."

**What to study (1 hour):** K3s installation, k3sup tool for fleet provisioning,
how to run NATS leaf node + inference container on same K3s node, Helm deployment
to K3s cluster.

---

## Category 3: Grid Protocols (Gap: DNP3, SCADA, PMUs vs. Juan's Modbus/MQTT)

### Mental Model: The Grid Protocol Stack

```
Wide-Area / Transmission layer:
  PMU → IEEE C37.118 (synchrophasor data) → Phasor Data Concentrator (PDC)
  SCADA Master ← DNP3/IEC 61850 ← RTU/IED (at substation)

Distribution / Feeder layer:
  DER controller ← Modbus / DNP3 / IEEE 2030.5 ← inverter, meter, switch

Building / Device layer (Juan's domain):
  BMS ← Modbus / BACnet / Zigbee / MQTT ← thermostat, VFD, smart plug
```

Juan lives in the bottom layer. The JD wants him to work the top two.

---

### SCADA (HIGH AWARENESS)

**What it is:** Supervisory Control and Data Acquisition. Not a single protocol — it is
an *architecture* consisting of:
- **RTUs / IEDs** (Remote Terminal Units / Intelligent Electronic Devices): field hardware
  that reads sensors and operates breakers/switches.
- **SCADA Master / Control Center software**: aggregates RTU data, provides operator HMI,
  runs alarm management. Examples: GE's own iFIX/Cimplicity, OSIsoft PI (now AVEVA),
  Ignition (Inductive Automation), ABB System 800xA.
- **Historian**: time-series database optimized for SCADA data (OSIsoft PI is dominant;
  Ignition uses SQL; AVEVA). Juan's InfluxDB/TimescaleDB knowledge directly maps here.
- **OPC-UA**: the modern middleware protocol connecting SCADA to historians and analytics.
  Platform-independent, secure (TLS), information-model-aware. Replaces legacy OPC-DA.
  Critical to know: OPC-UA is to SCADA what REST/gRPC is to web APIs.

**Why it matters:** SCADA is the incumbent data source for virtual sensing — the JD says
"Integrate field data sources (SCADA, PMUs, DER controllers)." Juan's virtual-sensing
algorithm will consume SCADA telemetry as input.

**Interview line:** "SCADA gives us the supervisory visibility layer — RTU/IED readings
arriving via DNP3 or IEC 61850, aggregated in the historian, accessible via OPC-UA.
My virtual-sensing stack subscribes to those OPC-UA data feeds and treats SCADA telemetry
as one input stream alongside PMU synchrophasors and IoT sensor data."

---

### DNP3 (HIGH AWARENESS)

**What it is:** Distributed Network Protocol 3. Designed specifically for SCADA in
electric utility and water systems. Built for unreliable, low-bandwidth serial/radio
links between master and RTU. Key features that differentiate it from Modbus:

| Dimension | Modbus (Juan has) | DNP3 (gap) |
|-----------|-------------------|------------|
| Origin | Industrial automation (1979) | Electric utility (1990s) |
| Time stamping | Not native | Millisecond timestamps on every point |
| Unsolicited reporting | No (poll only) | Yes (RTU pushes on change) |
| Data types | Coils, registers (generic) | Analog input, binary input/output, counter, frozen counter |
| CRC / error check | Basic | Robust CRC per frame |
| Security | None native | DNP3 SAv5 (Secure Authentication v5) |
| Transport | Serial, Ethernet | Serial, TCP/IP, UDP |
| Layering | Simple (app/data-link) | Three-layer (transport, data-link, app) |

DNP3 is used in **thousands of substations** globally. When Juan's code talks to a
substation RTU or a distribution automation device, it will speak DNP3.

**Python library:** `dnp3-python` / `opendnp3` bindings. Know that DNP3 master <→ outstation
(not client/server like REST, not publisher/subscriber like MQTT).

**Interview line:** "DNP3 is the lingua franca for utility-to-substation telemetry —
I see it as Modbus with millisecond timestamps, unsolicited reporting, and utility-grade
security (SAv5). My SCADA integration layer would normalize DNP3 events alongside
Modbus registers and IEC 61850 GOOSE messages into a unified telemetry stream."

**What to study (2 hours):** DNP3 master/outstation model, object groups/variations
(Group 30 = analog input, Group 12 = CROB for binary output), unsolicited response mode,
integrity polls vs. event polls.

---

### PMUs — Phasor Measurement Units (HIGH AWARENESS)

**What it is:** Hardware device that measures voltage and current phasors (magnitude +
phase angle) synchronized to GPS time with microsecond accuracy. Reports at 30–120
samples/second (vs. SCADA's 1 sample every 2–4 seconds). PMUs are the **highest-fidelity
sensors** for transmission-grid state estimation.

**Key concepts:**
- **Synchrophasor**: phasor measurement with a GPS timestamp — allows comparing phase
  angles between substations thousands of miles apart.
- **PDC (Phasor Data Concentrator)**: aggregates synchrophasor streams from many PMUs.
  Software (e.g., OpenPDC, NASPI standards). Outputs IEEE C37.118 data frames.
- **IEEE C37.118**: the communication standard for synchrophasor data. Protocol between
  PMU and PDC.
- **WAMS (Wide-Area Monitoring System)**: the network of PMUs + PDCs providing real-time
  transmission grid visibility.

**Why it matters for virtual sensing:** The JD explicitly names "voltage stability, phase
angles" as parameters to infer. PMU data is the *ground truth* input (when available)
and the *validation benchmark* for virtual sensing (when sensors are sparse). Virtual
sensing infers PMU-quality measurements at unmonitored buses from partial PMU coverage.

**Relationship to Kalman filters:** State estimation on the grid traditionally uses
Weighted Least Squares (WLS). PMU data enables **dynamic state estimation** using Kalman
filters because PMU's high temporal resolution matches the Kalman prediction-update cycle.
This is the direct connection between Juan's Kalman filter gap and the PMU gap.

**Interview line:** "PMUs give us microsecond-synchronized synchrophasors at 30–120 Hz —
that's the data quality that enables Kalman-filter-based dynamic state estimation as
opposed to the slower WLS you'd run on SCADA-rate telemetry. Virtual sensing at
unmonitored buses is essentially running a Kalman estimator that fuses sparse PMU
coverage with physics-based models to produce synthetic synchrophasors."

**What to study (1 hour):** IEEE C37.118 frame format conceptually, what a synchrophasor
is (V∠θ), how PDC aggregates, how virtual PMUs work (software-defined PMU-equivalent
outputs from state estimator).

---

### LoRa / LoRaWAN (LOW-MEDIUM PRIORITY)

**What it is:** Long Range (LoRa) is a physical-layer radio modulation technique from
Semtech (chirp spread spectrum). LoRaWAN is the MAC/network layer built on top.
Key characteristics:
- Range: 2–15 km line-of-sight, 1–3 km urban.
- Data rate: 0.3–50 kbps (very low throughput, but long battery life).
- Power: battery-operated for 5–10 years.
- Topology: end-device → gateway → network server → application server.

**Current state:** Semtech Gen 4 (LR2021 transceiver, up to 2.6 Mbps) launched 2025.
LoRa Alliance governs the LoRaWAN spec.

**Why it matters for this role:** The JD lists "LoRa" alongside MQTT and DNP3 as
field protocols. LoRa fills the gap where power lines don't exist (no RS-485 for Modbus,
no Ethernet for DNP3 TCP), such as:
- Remote pole-top sensors (line temperature, sag monitoring).
- Distribution circuit sensors in rural areas.
- Fault indicator sensors that don't justify fiber/cellular.

**Comparison to what Juan knows:**

| Dimension | Zigbee (Juan has) | LoRa/LoRaWAN (gap) |
|-----------|-------------------|---------------------|
| Range | 10–100 m mesh | 2–15 km |
| Data rate | 250 kbps | 0.3–50 kbps |
| Power | Mains or battery (short) | Battery (years) |
| Topology | Mesh | Star-of-stars |
| Use case | Building automation | Wide-area field sensing |

**Interview line:** "LoRa is Zigbee's long-range cousin — you trade throughput for
kilometers of range and years of battery life. For remote distribution sensors where
there's no fiber or reliable cellular, LoRaWAN gives us a path to bring pole-top sag
sensors or fault indicators into the data pipeline without running copper."

**What to study (30 min):** LoRaWAN network architecture (end device, gateway, network
server), Class A/B/C device classes, how it bridges to MQTT (The Things Network pattern).

---

### IEC 61850 (MEDIUM AWARENESS — preferred qualification)

**What it is:** International standard for substation automation and communication.
Defines both a **data model** (Logical Nodes — e.g., MMXU for measurements, XCBR for
circuit breakers) and **communication services**:
- **GOOSE** (Generic Object Oriented Substation Event): <4 ms peer-to-peer Ethernet
  for protection/control (e.g., trip a breaker on fault detection). NOT routed over IP.
- **Sampled Values (SV)**: high-speed digitized current/voltage streams on the process bus.
- **MMS** (Manufacturing Message Specification): for supervisory SCADA-layer communication.
- **CIM** (Common Information Model): data model for whole-grid network topology
  (a superset of 61850).

**Interview line:** "IEC 61850 is the glue of modern substation automation — GOOSE handles
sub-4-millisecond protection trips at the Ethernet layer, Sampled Values replace analog
cabling with digitized process bus data, and MMS handles the supervisory SCADA
conversation. I've studied the standard and understand how logical nodes like MMXU and
XCBR map to the physical substation equipment."

---

## Category 4: Observability (Gap: Prometheus vs. Juan's Grafana-only usage)

### Prometheus (HIGH PRIORITY)

**What it is:** Open-source metrics collection and alerting system, CNCF graduated project.
Pull-based model: Prometheus server scrapes `/metrics` endpoints from targets at configured
intervals. Stores data in its own TSDB (short retention, typically 15 days). Works in
concert with Alertmanager (routing/deduplication of alerts) and Grafana (visualization).

Juan already uses **Grafana** with InfluxDB. The gap is Prometheus as the *metrics
collection layer* that feeds Grafana.

**Why it matters:** The JD names "observability stacks (Prometheus, Grafana)" together.
In a K3s/Kubernetes cluster, the standard stack is:
```
Pod/service → exposes /metrics (Prometheus format)
Prometheus   → scrapes targets, evaluates alert rules
Alertmanager → routes alerts (PagerDuty, Slack)
Grafana      → dashboards fed by Prometheus (PromQL queries)
```
This is distinct from Juan's InfluxDB path (where services write metrics, Grafana reads).
Prometheus's pull model is standard for Kubernetes because it auto-discovers pods via
service discovery — no code change needed in the monitored service.

**PromQL basics to know:**

```promql
# Rate of messages processed per second (last 5m window)
rate(kafka_consumer_records_consumed_total[5m])

# CPU usage across all K3s nodes
sum by (node) (rate(node_cpu_seconds_total{mode!="idle"}[1m]))

# Alert: if edge node offline (no scrape for 5m)
up{job="edge-sensor"} == 0
```

**Key exporters for this role:**
- `node_exporter` — Linux host metrics (CPU, memory, disk, network)
- `kube-state-metrics` — K3s/K8s object states (pods running/pending/failed)
- `nats_exporter` — NATS JetStream metrics
- Custom `/metrics` endpoint in the virtual-sensing FastAPI service

**Comparison to InfluxDB (Juan's existing approach):**

| Dimension | InfluxDB (Juan has) | Prometheus (gap) |
|-----------|---------------------|------------------|
| Ingest model | Push (services write) | Pull (Prometheus scrapes) |
| Query language | Flux / InfluxQL | PromQL |
| Retention | Long-term (configurable) | Short (15 days default) |
| K8s integration | Manual | Automatic service discovery |
| Alert rules | External (Kapacitor/Grafana) | Native (alerting rules) |
| Cardinality | Higher tolerance | Sensitive to high-cardinality labels |

**Interview line:** "I've run Grafana dashboards backed by InfluxDB for real-time grid
metrics. Prometheus adds the Kubernetes-native pull scraping layer — every pod advertises
a /metrics endpoint, Prometheus auto-discovers it via service discovery, and I get
cluster-wide observability for free. I'd use Prometheus for operational metrics
(latency, throughput, error rates) and keep InfluxDB/TimescaleDB for the long-term
physics telemetry (sensor readings, state estimates)."

**What to study (1 hour):** PromQL rate/increase/histogram functions, kube-prometheus-stack
Helm chart (the standard way to deploy on K3s), how to instrument a FastAPI app
(prometheus-fastapi-instrumentator library), recording rules for expensive queries.

---

## Category 5: Federated Architectures & Federated Learning (Gap)

### Federated Data Pipelines (HIGH PRIORITY — named in JD)

**What the JD means:** "Develop federated data pipelines that allow distributed nodes to
collaborate securely without central coordination."

This is **NOT** about federated learning (ML). It is about data architecture:

**Federated pipeline = each edge node (substation, field device) owns its data and
processing locally; nodes exchange only derived/aggregated data rather than raw telemetry
flowing to a central database.**

This maps directly to the grid context:
- Each K3s substation node runs its own virtual-sensing inference.
- Local decisions (e.g., reactive power compensation) are made without awaiting cloud round-trip.
- Aggregated outputs (state estimates, anomaly flags) are published to NATS JetStream,
  which replicates them up to cloud tier.
- The cloud never sees raw sensor streams — only processed features/decisions.

**Architecture pattern:**
```
Substation A (K3s node)
  ├── NATS leaf node (local messaging)
  ├── Virtual sensor container (inference)
  ├── InfluxDB edge (local buffer)
  └── Publishes: state estimate, anomaly flags

Substation B (K3s node)
  ├── same stack
  └── Publishes independently

Cloud aggregator
  ├── NATS core cluster (receives from leaf nodes)
  ├── Kafka (downstream analytics)
  └── Fleet observability (Prometheus federation)
```

**Interview line:** "Federated pipelines for me mean pushing the intelligence to
the substation node so it runs autonomously — local NATS for intra-node messaging,
K3s for orchestration, and JetStream store-and-forward for eventual cloud sync.
The cloud tier aggregates decisions and state estimates, not raw sensor data. That's
the latency and bandwidth win: a 30-Hz PMU stream stays local; only the 1-Hz state
estimate propagates up."

---

### Federated Learning (MEDIUM PRIORITY — implied by JD's "federated control frameworks")

**What it is:** A distributed ML training paradigm where:
1. Each edge node trains on its local data.
2. Only model weight updates (gradients or deltas) are sent to an aggregator.
3. Aggregator produces a global model (FedAvg algorithm most common).
4. Global model is pushed back to edge nodes.
5. Raw data never leaves the edge node — privacy-preserving by design.

**Why it matters for this role:** Virtual sensors at different substations may have
different data distributions. Federated learning allows improving the global model
without centralizing sensitive utility data.

**Frameworks to know:**

| Framework | Language | Strengths | Maturity |
|-----------|----------|-----------|----------|
| **Flower (flwr)** | Python | Framework-agnostic (PyTorch, TF, sklearn), edge-native, active | HIGH (v1.25 as of 2025) |
| PySyft (OpenMined) | Python | Privacy-preserving (SMPC, HE focus) | MEDIUM |
| FedML | Python | Research-focused, large ecosystem | MEDIUM |
| OpenFL (Intel) | Python | Enterprise, healthcare focus | MEDIUM |

**Recommendation:** Know **Flower** — it is the most practical, PyTorch-friendly, and
actively maintained framework. It directly supports the heterogeneous device landscape
(different hardware at each substation).

**Flower quickstart (know the API shape):**
```python
import flwr as fl

class VirtualSensorClient(fl.client.NumPyClient):
    def get_parameters(self, config): return model.get_weights()
    def fit(self, parameters, config):
        model.set_weights(parameters)
        model.fit(local_data)
        return model.get_weights(), len(local_data), {}
    def evaluate(self, parameters, config):
        model.set_weights(parameters)
        loss, accuracy = model.evaluate(local_test_data)
        return loss, len(local_test_data), {"accuracy": accuracy}

fl.client.start_numpy_client(server_address="aggregator:8080", client=VirtualSensorClient())
```

**Interview line:** "Flower gives us federated learning with the same PyTorch model code
I'd run centrally — each substation node trains on its local telemetry history, sends
weight deltas to a fleet aggregator, and we get a global virtual-sensor model without
moving a single raw measurement off-site. That's essential when utility data has
regulatory restrictions on leaving substations."

---

## Summary Reference Table (for quick interview recall)

| Gap Area | Tool / Concept | Compare To (Juan has) | Interview One-Liner |
|----------|---------------|----------------------|---------------------|
| Edge messaging | NATS JetStream | MQTT | MQTT for devices, NATS for federated edge-cloud pipelines |
| Cloud streaming | Kafka 4.2 | Pub/Sub | Kafka at the cloud tier; too heavy for edge |
| Cloud streaming | Apache Pulsar | Kafka | Pulsar when you need native geo-replication; similar edge limitation |
| Edge orchestration | K3s 1.31 | Kubernetes | Same API, 4x lighter, designed for air-gap field deployment |
| Grid telemetry | DNP3 | Modbus | Modbus without timestamps; DNP3 adds timestamps + unsolicited push |
| Grid visibility | SCADA + OPC-UA | InfluxDB + Grafana | SCADA is the supervisory layer; OPC-UA is its integration API |
| High-res sensors | PMU / C37.118 | InfluxDB time-series | PMU gives 120-Hz synchrophasors enabling Kalman-based state estimation |
| Wide-area IoT | LoRa/LoRaWAN | Zigbee | Zigbee indoors; LoRa for km-range field sensors |
| Observability | Prometheus | Grafana (InfluxDB) | Prometheus pull-scrapes K8s pods; Grafana visualizes via PromQL |
| Federated ML | Flower (flwr) | Azure ML centralized | Train at edge, share weights, never move raw sensor data |
| Grid standard | IEC 61850 | MQTT/Modbus | 61850 = GOOSE (<4ms protection) + MMS (SCADA) + Sampled Values |

---

## What NOT to Over-Invest In (Given 1-Week Runway)

| Avoid Deep-Diving | Reason | Awareness Level Sufficient |
|-------------------|--------|---------------------------|
| Pulsar internals | Kafka/NATS cover the JD; Pulsar is "also named" | Know the storage-separation architecture |
| EMT tools (PSCAD, RTDS, Opal-RT) | "Preferred" only; no hands-on expected | Know they're simulation tools for model validation |
| Go / Rust | JD says OR; Python + TS satisfies | Don't study |
| Deep Kafka ops (MirrorMaker, Schema Registry) | Cloud-tier concern; not edge | Know topics/partitions/offsets |
| LoRa RF engineering | Field-deployment detail; not software design | Know the use case and network architecture |
| IEC 61850 SCL/CID files | Config detail for substation engineers | Know GOOSE, SV, MMS roles |
| Federated learning math (FedProx, SCAFFOLD) | Research-level; Flower/FedAvg is enough | Know FedAvg conceptually |

---

## Recommended Python Libraries to Recognize (Not Build, Just Know)

```bash
# NATS client
pip install nats-py

# DNP3 Python binding (OpenDNP3)
pip install dnp3-python  # or pydnp3

# Prometheus instrumentation for FastAPI
pip install prometheus-fastapi-instrumentator prometheus-client

# Federated learning
pip install flwr  # Flower

# IEC 61850 (awareness; typically vendor SDKs or libiec61850 C binding)
# No standard Python package; libiec61850 is the OSS reference implementation
```

---

## Sources

- NATS docs (docs.nats.io/nats-concepts/overview/compare-nats) — NATS vs Kafka/MQTT feature table — HIGH confidence
- Bytewax blog (bytewax.io/blog/kafka-vs-pulsar-vs-nats) — Kafka/Pulsar/NATS performance comparison — MEDIUM confidence
- Apache Kafka release blog (kafka.apache.org) — Kafka 4.0 KRaft, 4.2.0 current stable — HIGH confidence
- NATS.io blog / GitHub releases — NATS Server 2.11, JetStream features — HIGH confidence
- Xylem/Xylem UK (xylem.com) — DNP3 vs Modbus comparison — MEDIUM confidence
- Wikipedia DNP3 article — Protocol overview — MEDIUM confidence
- PMU overview (tutorialspoint.com, ScienceDirect) — PMU architecture, IEEE C37.118 — MEDIUM confidence
- Flower framework docs (flower.ai) — v1.25 API, PyTorch integration — HIGH confidence
- OpenFMB.org — OpenFMB edge interoperability, DNP3/Modbus/2030.5 adapters — MEDIUM confidence
- CloudOptimo / SFEIR — K3s vs K8s resource comparison — MEDIUM confidence
- Prometheus docs / Logz.io blog — Prometheus pull model, K8s integration — HIGH confidence
- IEC 61850 overview (electricityforum.com, EMQ blog) — GOOSE, SV, MMS — MEDIUM confidence
- WebSearch: federated learning grid applications (arxiv.org papers, 2025) — MEDIUM confidence
- LoRa Alliance / Semtech Gen 4 blog — LoRaWAN use cases, Gen 4 specs — MEDIUM confidence

---

*Stack research for: GE Vernova Virtual Sensing & Decentralized Grid Operations (interview prep)*
*Researched: 2026-06-13*
