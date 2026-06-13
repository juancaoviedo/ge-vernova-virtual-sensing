<!-- GSD:project-start source:PROJECT.md -->
## Project

**GE Vernova Virtual Sensing — Interview Prep**

A focused, time-boxed interview-preparation project for Juan Carlos Oviedo Cepeda's
application to the **Senior Software Engineer & Scientist – Virtual Sensing and
Decentralized Grid Operations** role at GE Vernova (CTO org, reporting to the
Electrification Chief Architect; West Melbourne, hybrid; req R5043890). It turns the
gathered source material (the lab director's patents, IEC 61850, IntelliGrid
architecture, the job description, and Juan's CV) into study notes, predicted Q&A and
talking points, system-design drills, and small hands-on demos — so Juan can walk into
the interview able to (1) reframe his existing edge/DER work in GE Vernova's language and
(2) speak credibly to the specific gaps the role names.

**Core Value:** Juan walks into the interview able to connect his real experience to this role's exact
requirements — and to the director's own patented work — with confidence and specifics.
Everything else is secondary to that.

### Constraints

- **Timeline**: Crash prep — interview expected within ~1 week of 2026-06-13. Prioritize highest-yield material; depth where it differentiates, awareness elsewhere.
- **Format**: Deliverables are study notes/summaries, Q&A + talking points, system-design drills, and small hands-on demos.
- **Scope discipline**: Target *this role's* named gaps and the director's work; reframe existing strengths rather than re-studying them.
- **Expandability**: Juan will add more source documents after kickoff; the plan must accommodate ingesting them into the study set.
<!-- GSD:project-end -->

<!-- GSD:stack-start source:research/STACK.md -->
## Technology Stack

## Purpose of This Document
## Category 1: Streaming & Messaging (Gap: Kafka, NATS, Pulsar vs. Juan's MQTT)
### Mental Model First: What Juan Already Has vs. What He Needs
### NATS + JetStream (HIGH PRIORITY — matches JD's "NATS" and edge context exactly)
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
### Apache Kafka (MEDIUM PRIORITY — named in JD but over-engineered for edge)
| Dimension | Kafka | NATS JetStream |
|-----------|-------|----------------|
| Throughput ceiling | Millions msgs/sec | ~10M msgs/sec (lower overhead) |
| Edge deployment | NOT suitable (8 cores, 64–128 GB RAM) | Yes (single binary, Pi-class) |
| Minimum footprint | Significant (JVM + disk) | ~512 MB RAM |
| Durability | Excellent (log-based) | Good (JetStream) |
| Ecosystem | Enormous (connectors, Schema Registry, Flink) | Growing |
| Learning curve | High | Lower |
### Apache Pulsar (LOW PRIORITY — named in JD but less field-dominant than Kafka/NATS)
| Dimension | Kafka | Pulsar |
|-----------|-------|--------|
| Architecture | Broker = log storage | Broker + BookKeeper (separate) |
| Multi-tenancy | Needs external tooling | Native (namespaces, tenants) |
| Geo-replication | Add-on (MirrorMaker) | Built-in |
| Edge suitability | Poor | Poor (also heavy) |
| Maturity/ecosystem | Larger | Smaller (13K stars vs Kafka's 27K) |
### MQTT (Juan's strength — reframe, don't re-study)
## Category 2: Edge Orchestration (Gap: K3s vs. Juan's full Kubernetes)
### K3s (HIGH PRIORITY)
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
## Category 3: Grid Protocols (Gap: DNP3, SCADA, PMUs vs. Juan's Modbus/MQTT)
### Mental Model: The Grid Protocol Stack
### SCADA (HIGH AWARENESS)
- **RTUs / IEDs** (Remote Terminal Units / Intelligent Electronic Devices): field hardware
- **SCADA Master / Control Center software**: aggregates RTU data, provides operator HMI,
- **Historian**: time-series database optimized for SCADA data (OSIsoft PI is dominant;
- **OPC-UA**: the modern middleware protocol connecting SCADA to historians and analytics.
### DNP3 (HIGH AWARENESS)
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
### PMUs — Phasor Measurement Units (HIGH AWARENESS)
- **Synchrophasor**: phasor measurement with a GPS timestamp — allows comparing phase
- **PDC (Phasor Data Concentrator)**: aggregates synchrophasor streams from many PMUs.
- **IEEE C37.118**: the communication standard for synchrophasor data. Protocol between
- **WAMS (Wide-Area Monitoring System)**: the network of PMUs + PDCs providing real-time
### LoRa / LoRaWAN (LOW-MEDIUM PRIORITY)
- Range: 2–15 km line-of-sight, 1–3 km urban.
- Data rate: 0.3–50 kbps (very low throughput, but long battery life).
- Power: battery-operated for 5–10 years.
- Topology: end-device → gateway → network server → application server.
- Remote pole-top sensors (line temperature, sag monitoring).
- Distribution circuit sensors in rural areas.
- Fault indicator sensors that don't justify fiber/cellular.
| Dimension | Zigbee (Juan has) | LoRa/LoRaWAN (gap) |
|-----------|-------------------|---------------------|
| Range | 10–100 m mesh | 2–15 km |
| Data rate | 250 kbps | 0.3–50 kbps |
| Power | Mains or battery (short) | Battery (years) |
| Topology | Mesh | Star-of-stars |
| Use case | Building automation | Wide-area field sensing |
### IEC 61850 (MEDIUM AWARENESS — preferred qualification)
- **GOOSE** (Generic Object Oriented Substation Event): <4 ms peer-to-peer Ethernet
- **Sampled Values (SV)**: high-speed digitized current/voltage streams on the process bus.
- **MMS** (Manufacturing Message Specification): for supervisory SCADA-layer communication.
- **CIM** (Common Information Model): data model for whole-grid network topology
## Category 4: Observability (Gap: Prometheus vs. Juan's Grafana-only usage)
### Prometheus (HIGH PRIORITY)
# Rate of messages processed per second (last 5m window)
# CPU usage across all K3s nodes
# Alert: if edge node offline (no scrape for 5m)
- `node_exporter` — Linux host metrics (CPU, memory, disk, network)
- `kube-state-metrics` — K3s/K8s object states (pods running/pending/failed)
- `nats_exporter` — NATS JetStream metrics
- Custom `/metrics` endpoint in the virtual-sensing FastAPI service
| Dimension | InfluxDB (Juan has) | Prometheus (gap) |
|-----------|---------------------|------------------|
| Ingest model | Push (services write) | Pull (Prometheus scrapes) |
| Query language | Flux / InfluxQL | PromQL |
| Retention | Long-term (configurable) | Short (15 days default) |
| K8s integration | Manual | Automatic service discovery |
| Alert rules | External (Kapacitor/Grafana) | Native (alerting rules) |
| Cardinality | Higher tolerance | Sensitive to high-cardinality labels |
## Category 5: Federated Architectures & Federated Learning (Gap)
### Federated Data Pipelines (HIGH PRIORITY — named in JD)
- Each K3s substation node runs its own virtual-sensing inference.
- Local decisions (e.g., reactive power compensation) are made without awaiting cloud round-trip.
- Aggregated outputs (state estimates, anomaly flags) are published to NATS JetStream,
- The cloud never sees raw sensor streams — only processed features/decisions.
### Federated Learning (MEDIUM PRIORITY — implied by JD's "federated control frameworks")
| Framework | Language | Strengths | Maturity |
|-----------|----------|-----------|----------|
| **Flower (flwr)** | Python | Framework-agnostic (PyTorch, TF, sklearn), edge-native, active | HIGH (v1.25 as of 2025) |
| PySyft (OpenMined) | Python | Privacy-preserving (SMPC, HE focus) | MEDIUM |
| FedML | Python | Research-focused, large ecosystem | MEDIUM |
| OpenFL (Intel) | Python | Enterprise, healthcare focus | MEDIUM |
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
## Recommended Python Libraries to Recognize (Not Build, Just Know)
# NATS client
# DNP3 Python binding (OpenDNP3)
# Prometheus instrumentation for FastAPI
# Federated learning
# IEC 61850 (awareness; typically vendor SDKs or libiec61850 C binding)
# No standard Python package; libiec61850 is the OSS reference implementation
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
<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->
## Conventions

Conventions not yet established. Will populate as patterns emerge during development.
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->
## Architecture

Architecture not yet mapped. Follow existing patterns found in the codebase.
<!-- GSD:architecture-end -->

<!-- GSD:skills-start source:skills/ -->
## Project Skills

No project skills found. Add skills to any of: `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, `.github/skills/`, or `.codex/skills/` with a `SKILL.md` index file.
<!-- GSD:skills-end -->

<!-- GSD:workflow-start source:GSD defaults -->
## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:
- `/gsd-quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd-debug` for investigation and bug fixing
- `/gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->



<!-- GSD:profile-start -->
## Developer Profile

> Profile not yet configured. Run `/gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
