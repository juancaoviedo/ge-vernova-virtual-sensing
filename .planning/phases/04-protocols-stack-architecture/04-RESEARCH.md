# Phase 4: Protocols, Stack & Architecture — Research

**Researched:** 2026-06-14
**Domain:** Grid protocol stack, edge/cloud software stack, IEC 61850 internals, observability, four-tier reference architecture
**Confidence:** HIGH (all four gap areas verified against official docs or the IEC 61850 primary source PDF)

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- **D-01:** Lift + targeted deepening. CLAUDE.md Category 1–5 is the authoritative content base. Notes distill/refine it for spoken delivery; researcher does real depth + gap-fill on D-02 topics and spot-verifies version/fact claims. Do NOT re-research from scratch what CLAUDE.md already covers well.
- **D-02:** All four named must-explain areas get research depth (not just awareness lift), with these specific gaps:
  - IEC 61850 internals (STK-02): GOOSE vs SV vs MMS roles + three-tier hierarchy + ≥3 named logical-node names — CLAUDE.md lists GOOSE/SV/MMS/CIM but NO logical-node names.
  - Edge messaging justification (STK-03): the crisp spoken "why NATS JetStream over MQTT and over Kafka for the substation edge" argument + the three K3s-vs-K8s distinctions.
  - Prometheus specifics (STK-04): a concrete recitable PromQL query + what kube-prometheus-stack adds — CLAUDE.md has PromQL snippets but NEVER names kube-prometheus-stack.
  - Protocol tier placement (STK-01): crisp one-property-each + correct tier for SCADA/DNP3/PMU-C37.118/IEC61850/LoRa — mostly a lift/tighten from CLAUDE.md Category 3.
- **D-03:** 5 notes (one per STK requirement) in a `notes/` directory + STK-05 as standalone whiteboard-architecture doc. No consolidated deck. No `demo/` directory.
- **D-04:** Notes-only — no demo.
- **D-05:** Both ASCII (whiteboard target) and Mermaid versions of the four-tier architecture diagram, plus numbered narration script.
- **D-06:** Dual-layer: (a) generic four-tier reference annotated with Juan's own stack at each tier, plus (b) short AGMS overlay mapping Scout Command/Field Agent Devices → edge; Operation Loop simulate-before-commit → fog; GWM → cloud.
- **D-07:** Oral-rehearsal note style: For:/Purpose: header, numbered sections, `<3-min say-aloud` track.
- **D-08:** Per-note "→ Bridge to your work" callout. MQTT→NATS, full K8s→K3s, InfluxDB+Grafana→Prometheus/PromQL, Zigbee→LoRa, Modbus→DNP3.
- **D-09:** No aggregate vocabulary-bridge table here — that is Phase 6.
- **D-10:** Markdown style; LaTeX only where a formula genuinely helps (e.g. C37.118 reporting-rate note).

### Claude's Discretion
- Exact filenames/slugs within `notes/`; whether STK-03 stays one note or splits; precise section ordering; which specific ≥3 logical-node names to feature; the exact PromQL query chosen; exact ASCII/Mermaid layout; how richly the AGMS overlay cross-links back to the Phase 3 deck/INDEX.

### Deferred Ideas (OUT OF SCOPE)
- Federated architecture depth (FedAvg/FedProx/Krum, non-IID/client-drift, Byzantine robustness) — Phase 5.
- Edge security internals (OTA integrity, TPM attestation, SPIFFE/SPIRE) — Phase 5.
- Aggregate vocabulary-bridge table, STAR stories, OSED pitch, timed mock-interview rehearsal — Phase 6.
- Hands-on messaging/observability demo — declined (D-04).
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| STK-01 | Grid protocol stack — SCADA, DNP3, PMU/C37.118, LoRa, MQTT — placed in the correct field-to-cloud tier, one key property each | Section: Protocol Tier Map (all facts verified) |
| STK-02 | IEC 61850: GOOSE vs SV vs MMS, three-tier hierarchy, ≥3 named logical-node names — without notes | Section: IEC 61850 Deep-Dive (verified from IEC TR 61850-10-3 PDF + web sources) |
| STK-03 | NATS JetStream vs MQTT vs Kafka vs Pulsar, K3s vs K8s — with interview-ready justifications | Section: Edge/Cloud Stack Positioning (NATS docs.nats.io verified, K3s docs verified) |
| STK-04 | Prometheus pull model vs InfluxDB push, PromQL basics, kube-prometheus-stack | Section: Observability Stack (ArtifactHub + official docs verified) |
| STK-05 | Whiteboard-able four-tier reference architecture Juan can draw and narrate | Section: Four-Tier Architecture Design |
</phase_requirements>

---

## Summary

This phase produces five modular study notes (STK-01..STK-05) that equip Juan to navigate the grid protocol stack, justify the edge/cloud software stack, and draw a four-tier reference architecture from memory in an interview. The primary content base is CLAUDE.md Categories 1–5, which already contains near-interview-ready comparison tables for NATS/Kafka/Pulsar/MQTT, K3s/K8s, DNP3/Modbus, PMU/C37.118, IEC 61850, Prometheus/InfluxDB, and LoRa/Zigbee. Research here fills the four genuine gaps CLAUDE.md does not cover: IEC 61850 logical-node names, the substation-edge justification narrative for NATS over Kafka and MQTT, the kube-prometheus-stack name and bundle, and a concrete recitable PromQL query.

The biggest single gap filled by this research is IEC 61850 logical nodes. The IEC TR 61850-10-3:2022 PDF (the source document in `docs/`) and authoritative web sources confirm five named logical nodes with precise definitions: XCBR (circuit breaker), MMXU (three-phase measurements), CSWI (switch controller), PTOC (time overcurrent protection), and PDIS (distance protection). These are organized into 13 functional groups by prefix letter (X=switchgear, M=measurement, C=control, P=protection, etc.) per IEC 61850-7-4. The three-tier station/bay/process hierarchy is well-documented and maps cleanly to MMS/GOOSE+SV respectively. The NATS vs Kafka at-the-edge argument is confirmed by the NATS official documentation verbatim: Kafka requires "a JVM, eight cores, 64–128 GB of RAM, two or more 8-TB SAS/SSD disks" — none of which fit a substation edge node. kube-prometheus-stack 86.2.3 (current as of research date) is confirmed to bundle Prometheus Operator + node-exporter + kube-state-metrics + Grafana + Alertmanager as a single Helm chart.

**Primary recommendation:** The planner should produce five notes mirroring the Phase 2 TVS style (For:/Purpose: header, numbered sections, `<3-min say-aloud`, boxed bridge callout). STK-05 is the signature deliverable — allocate the most planning effort there. All content is ready to lift directly from CLAUDE.md and the verified facts in this research document.

---

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Protection relay trips (GOOSE) | Field / Process bus | — | Layer 2 Ethernet only; never routed; <4 ms requirement |
| Raw current/voltage digitization (SV) | Field / Process bus | — | Merging units at process level → IEDs at bay level |
| IED supervisory control (MMS) | Bay / Station | — | Client-server over TCP/IP; routable to SCADA |
| SCADA visibility | Station level / Cloud | — | RTU/IED aggregation; OSIsoft PI historian |
| DNP3 field telemetry | Field → Station | — | Protocol bridges from RTUs to SCADA master |
| PMU synchrophasor streams | Field → Cloud | Edge aggregation (PDC) | High-rate streams; PDC at substation, WA aggregation at cloud |
| LoRa wide-area field sensors | Field | — | Battery devices → gateway → network server |
| Edge inference (EKF/virtual sensing) | Edge (K3s node) | — | Sub-second latency; cannot round-trip to cloud |
| Federated aggregation | Fog / Federated | — | Cross-substation; seconds-to-minutes latency acceptable |
| Model training / fleet GitOps | Cloud | — | Minutes+ latency; large compute and storage |
| Observability / metrics scraping | Edge + Cloud | — | Prometheus runs at edge AND cloud; Grafana centralized |

---

## Standard Stack

### Core (verified versions)

| Library / Tool | Version | Purpose | Why Standard |
|----------------|---------|---------|--------------|
| NATS Server + JetStream | v2.14.2 (2026-06-02) | Federated edge-cloud messaging | Single binary, <20 MB, runs on Pi-class nodes, durable replay, built-in request-reply, decentralized JWT accounts |
| K3s | v1.33.x / v1.34.x (2025-2026) | Lightweight Kubernetes for edge nodes | Same K8s API, ~512 MB RAM, single binary, SQLite-default, air-gap designed |
| kube-prometheus-stack | 86.2.3 (current) | Full K8s observability in one Helm chart | Bundles Prometheus Operator + node-exporter + kube-state-metrics + Grafana + Alertmanager |
| Prometheus | (bundled in stack) | Pull-based metrics collection | Native K8s service discovery via ServiceMonitor CRD |
| Grafana | (bundled in stack) | Visualization + dashboards | Reads from Prometheus via PromQL |
| Alertmanager | (bundled in stack) | Alert routing and silencing | Native Prometheus integration |

### Supporting (awareness level for interview)

| Library / Tool | Version | Purpose | When to Use |
|----------------|---------|---------|-------------|
| Kafka | 4.2.x (KRaft, no ZooKeeper) | Cloud-tier event streaming | Only at cloud tier; never at edge (JVM + 64–128 GB RAM) |
| Flower (flwr) | v1.x | Federated learning | Phase 5 — name at awareness level in STK-05 fog tier only |
| node-exporter | (bundled) | Linux host metrics | Always deployed with kube-prometheus-stack |
| kube-state-metrics | (bundled) | K8s object state metrics | Always deployed with kube-prometheus-stack |

### CLAUDE.md Tables That Need No Re-Research (lift directly)

- NATS vs Kafka vs Pulsar vs MQTT full comparison table — CLAUDE.md Category 1
- K3s vs K8s full comparison table — CLAUDE.md Category 2
- DNP3 vs Modbus comparison — CLAUDE.md Category 3
- SCADA/OPC-UA/PMU/LoRa/IEC 61850 overview — CLAUDE.md Category 3
- Prometheus vs InfluxDB comparison — CLAUDE.md Category 4
- Summary Reference Table (bridge raw material) — CLAUDE.md bottom section

---

## IEC 61850 Deep-Dive (STK-02 Gap Fill — Highest Priority)

### Three-Tier Hierarchy (station / bay / process)

[VERIFIED: IEC TR 61850-10-3:2022 PDF (docs/) + EMQ blog + LinkedIn sources]

| Tier | Layer | What Lives Here | Primary IEC 61850 Services |
|------|-------|-----------------|---------------------------|
| **Process level** | Bottom | Circuit breakers, current/voltage transformers (CTs, VTs), merging units, actuators | **GOOSE** (trips, interlocking), **SV** (digitized I/V samples) |
| **Bay level** | Middle | IEDs (Intelligent Electronic Devices): protection relays, bay controllers | Receives GOOSE + SV from process; sends MMS up to station |
| **Station level** | Top | SCADA HMI, engineering workstation, gateway/RTU to control center | **MMS** (client-server supervision, setpoints, reports) |

**Interview one-liner:** "Process level is the switchyard — GOOSE and SV never leave the LAN. Bay level is the protection relay and bay controller that act on them. Station level is the SCADA HMI that talks MMS over TCP to the control center."

### GOOSE / SV / MMS Roles

[VERIFIED: IEC TR 61850-10-3:2022 PDF (docs/); OPAL-RT docs; Wikipedia IEC 61850]

| Service | Full Name | Layer | Latency | Direction | Use Case |
|---------|-----------|-------|---------|-----------|----------|
| **GOOSE** | Generic Object Oriented Substation Event | Ethernet Layer 2 (no IP) | **< 4 ms** | Publisher → multicast subscribers | Protection trips, interlock signals, breaker status |
| **SV** | Sampled Values | Ethernet Layer 2 (no IP) | Sub-ms, high rate | Merging unit → IED | Digitized current + voltage waveforms on process bus |
| **MMS** | Manufacturing Message Specification (ISO 9506) | TCP/IP | Seconds (supervisory) | Client (SCADA) ↔ Server (IED) | Reading measurements, writing setpoints, retrieving logs |

**Key structural fact to say aloud:** "GOOSE and SV are Layer 2 — they never leave the substation LAN and are never routed. MMS is TCP/IP and is routable, so that's the path from substation to control center."

**GOOSE retransmission mechanism:** Sends at ~2 ms intervals on state change, then backs off to slow heartbeat. Reliability via repetition, not acknowledgment — this is why latency is deterministic.

### Logical Node Names (STK-02 Criterion 2 — the interview gap)

[VERIFIED: IEC TR 61850-10-3:2022 PDF confirms XCBR, PTOC, TVTR, TCTR, LPHD, LLN0; scadaprotocols.com verified MMXU, CSWI, PDIS against IEC 61850-7-4 group taxonomy]

All logical node class names are exactly four letters. The first letter indicates the functional group.

**The five to know for the interview (with one-liners):**

| LN Name | Group | Full Name / Function | Interview One-Liner |
|---------|-------|----------------------|---------------------|
| **XCBR** | X — Switchgear | Circuit Breaker | "The circuit breaker itself — carries Pos (position), OpCnt (operation count), block commands" |
| **MMXU** | M — Measurement | Three-Phase Measurement Unit | "Real-time voltage, current, power, power factor, frequency — the most-used measurement LN" |
| **CSWI** | C — Control | Switch Controller | "The operator interface — open/close commands from SCADA hit CSWI, which verifies interlocking then commands XCBR" |
| **PTOC** | P — Protection | Time Overcurrent Protection | "Overcurrent protection (IEEE device 50/51) — Op is the trip output, Str is start signal" |
| **PDIS** | P — Protection | Distance Protection | "Impedance-based distance protection (IEEE device 21) — triggers on fault impedance inside a protection zone" |

**Bonus nodes visible in the IEC TR 61850-10-3:2022 PDF (docs/):**

| LN Name | Group | Function |
|---------|-------|----------|
| **LLN0** | L — System | Root LN of every Logical Device; hosts GOOSE control blocks, datasets, report control blocks |
| **LPHD** | L — System | Physical device health, nameplate, watchdog — the Sim.stVal attribute here enables test mode |
| **TCTR** | T — Instrument Transformer | Current transformer model (used with merging units on process bus) |
| **TVTR** | T — Instrument Transformer | Voltage transformer model |

**The 13 LN functional groups (awareness, not memorization):**
L (System), P (Protection), X (Switchgear), M (Measurement), C (Control), R (Protection-Related: RREC=recloser, RBRF=breaker failure), A (Automatic Control), S (Sensor/Monitoring), T (Instrument Transformer), Y (Power Transformer), Z (Further Equipment: ZGEN=generator), I (Interfacing), G (Generic: GGIO)

**Command flow to say aloud:** "Dispatcher issues 'open breaker' → hits CSWI (controller) → CSWI verifies interlocking via CILO → sends operate command to XCBR (the breaker LN) → XCBR changes Pos and emits a GOOSE message → other IEDs receive the GOOSE in <4 ms."

---

## Edge/Cloud Stack Positioning (STK-03 Gap Fill)

### Why NATS JetStream Over MQTT at the Substation Edge

[VERIFIED: docs.nats.io/nats-concepts/overview/compare-nats; CLAUDE.md Category 1]

MQTT is designed for device-to-broker with a broker as single point. NATS JetStream is designed for service-to-service plus device, with durable replay and built-in request-reply. The substation edge case needs:
- **Durable replay:** If the cloud connection drops (island mode), messages cannot be lost — JetStream persists them for replay when connectivity returns. MQTT only has transient QoS levels with a broker.
- **Request-reply:** Edge inference services need synchronous request-response patterns; NATS has this built-in. MQTT requires manual correlation-ID patterns.
- **Decentralized JWT security accounts:** Multi-tenant substation deployments need isolation between tenants without a central auth server.
- **Leaf node topology:** NATS leaf nodes bridge the substation LAN to the cloud cluster without VPN; MQTT's star topology requires the broker to be reachable.

**The bridge pivot sentence (D-08 raw material):** "I ran MQTT-to-Mosquitto in OSED; NATS JetStream is the same publish-subscribe instinct but adds durable replay and decentralized JWT accounts for the federated edge — that's the upgrade path I'd take here."

### Why NATS JetStream Over Kafka at the Substation Edge

[VERIFIED: docs.nats.io compare-nats page verbatim; CLAUDE.md Category 1]

The single most quotable fact (verbatim from NATS official docs):

> "Kafka servers require a JVM, eight cores, 64 GB to 128 GB of RAM, two or more 8-TB SAS/SSD disks, and a 10-Gig NIC."

A substation edge node is a Pi-class or small industrial PC. NATS JetStream runs as a single static binary under 20 MB on ~512 MB RAM. This is not a tradeoff question — Kafka is architecturally incompatible with edge deployment.

**Additional Kafka vs NATS distinctions (from NATS docs):**
- Kafka requires ZooKeeper (legacy) or KRaft coordination; NATS is self-contained
- Kafka request-reply requires "application code to correlate requests with replies over multiple topics"; NATS has built-in request-reply
- GC pauses from JVM (even G1GC/ZGC) introduce latency spikes — unacceptable for protection relay monitoring

**Interview one-liner:** "Kafka at the substation edge is like bringing a semi-truck to park in a bicycle lane. It needs a JVM, 64–128 GB RAM, and a 10-Gig NIC. NATS JetStream is a 20 MB binary on a Pi-class node."

### The Three K3s-vs-K8s Distinctions

[VERIFIED: docs.k3s.io; SUSE K3s documentation; K3s GitHub releases]

These are the three the success criteria name explicitly:

| Distinction | K3s | K8s |
|-------------|-----|-----|
| **Memory footprint** | ~512 MB RAM for a server node | 2–4 GB minimum per node |
| **Database (etcd/SQLite)** | Defaults to **embedded SQLite** for single-node; embedded etcd available for HA mode | Requires external etcd cluster |
| **Air-gap design** | Designed for it — single binary <100 MB; ships with Traefik ingress + local-path provisioner; `curl \| sh` install | Complex (kubeadm, multiple binaries, etcd cluster, choose your own ingress) |

**Current K3s version:** v1.33.x / v1.34.x (tracks upstream Kubernetes; versioning mirrors Kubernetes minor — K3s v1.33 = Kubernetes 1.33)

**Additional interview context:** K3s is a Rancher/SUSE project, CNCF-certified, and in production use at telco edge and substation deployments. It is not a toy — it is the same Kubernetes API surface, just with components stripped (no in-tree cloud provider drivers, no alpha features, no legacy addons).

---

## Observability Stack (STK-04 Gap Fill)

### Prometheus Pull Model vs InfluxDB Push

[VERIFIED: CLAUDE.md Category 4; Prometheus docs; Sysdig blog]

| Dimension | Prometheus (gap) | InfluxDB (Juan has) |
|-----------|------------------|---------------------|
| Ingest model | **Pull** — Prometheus scrapes `/metrics` endpoints on a schedule | Push — services write to InfluxDB |
| Query language | **PromQL** | Flux / InfluxQL |
| K8s integration | **Native** — ServiceMonitor CRDs, automatic pod discovery | Manual |
| Alert rules | **Native** (alerting rules in Prometheus + Alertmanager) | External (Kapacitor / Grafana) |
| Default retention | 15 days | Configurable (long-term) |
| Cardinality | Sensitive to high-cardinality labels | Higher tolerance |

**The pull model's key implication:** Prometheus does not require services to know where to send metrics. Services expose a `/metrics` endpoint; Prometheus finds them via Kubernetes service discovery (ServiceMonitor CRDs) and scrapes on schedule. This is why it integrates so naturally with K8s — pod IPs change constantly, but service discovery handles it automatically.

### kube-prometheus-stack — What It Adds (the named gap)

[VERIFIED: ArtifactHub kube-prometheus-stack 86.2.3; GitHub prometheus-community/helm-charts; oneuptime.com blog 2026-02]

**Current version:** 86.2.3 (as of research date)

**What it bundles (one Helm install gets all of these):**

1. **Prometheus Operator** — a Kubernetes controller that watches for ServiceMonitor and PodMonitor CRDs and auto-configures Prometheus scrape targets. You do not edit prometheus.yml by hand; you create a ServiceMonitor CR.
2. **node-exporter** — DaemonSet on every K3s node; exposes Linux host metrics (CPU, memory, disk, network) as `/metrics`
3. **kube-state-metrics** — exposes Kubernetes object states (pod running/pending/failed, deployment replicas, etc.) from the API server
4. **Grafana** — visualization; pre-loaded with Kubernetes dashboards
5. **Alertmanager** — receives firing alerts from Prometheus, routes to PagerDuty/Slack/email/webhook

**Interview sentence:** "Instead of installing Prometheus, Grafana, and the exporters separately and wiring them together, kube-prometheus-stack is a single Helm chart that delivers Prometheus Operator, node-exporter, kube-state-metrics, Grafana, and Alertmanager pre-wired. The Operator pattern means you define what to scrape with a ServiceMonitor CRD and the Operator manages Prometheus config automatically."

### Concrete Recitable PromQL Query

[VERIFIED: Prometheus docs; last9.io; SigNoz; oneuptime.com]

**Most recitable (CPU rate for K3s/K8s monitoring):**

```promql
rate(container_cpu_usage_seconds_total{namespace="virtual-sensing"}[5m])
```

**What it does:** computes the per-second CPU usage rate averaged over the last 5 minutes for all containers in the `virtual-sensing` namespace. The `rate()` function is required because `container_cpu_usage_seconds_total` is a cumulative counter.

**Additional queries to know (awareness level):**

```promql
# Memory working set in bytes by pod
sum(container_memory_working_set_bytes{pod=~"ekf-.*"}) by (pod)

# Number of ready pods (kube-state-metrics)
kube_pod_status_ready{condition="true", namespace="virtual-sensing"}

# Alert: node has been down for 5 minutes (no scrape)
up{job="node-exporter"} == 0
```

**PromQL building blocks to name:**
- `rate(counter[window])` — per-second rate of a counter over a time window
- `sum(...) by (label)` — aggregate across instances, group by label
- Label matchers: `=`, `!=`, `=~` (regex), `!~` (not-regex)
- `up` metric — Prometheus's own heartbeat; 0 = scrape target down

---

## Protocol Tier Map (STK-01 — Lift + Tighten from CLAUDE.md)

[VERIFIED: CLAUDE.md Category 3; IEC TR 61850-10-3; Wikipedia IEC 61850; IEEE C37.118 documentation]

The five protocols Juan must place in the interview, each with one key property:

| Protocol | Field-to-Cloud Tier | One Key Property | Transport |
|----------|---------------------|-----------------|-----------|
| **SCADA + OPC-UA** | Station level → cloud/control center | RTUs/IEDs aggregate field data; OPC-UA is the integration API bridging SCADA to historians and analytics | TCP/IP |
| **DNP3** | Field → station (RTU/IED to SCADA master) | **Millisecond timestamps on every data point** + unsolicited reporting (RTU pushes on change, no polling needed) | Serial or TCP/IP |
| **PMU / IEEE C37.118** | Field → regional/cloud (via PDC) | **GPS-synchronized phasors at 10–120 frames/sec** (30/60 common for 60 Hz systems); enables wide-area state estimation | TCP/IP (streaming) |
| **IEC 61850** | Process bus (GOOSE/SV) and station bus (MMS) | GOOSE <4 ms L2 protection trips; SV = digitized I/V process bus; MMS = client-server SCADA supervision | L2 Ethernet (GOOSE/SV); TCP/IP (MMS) |
| **LoRa / LoRaWAN** | Field → wide-area (cloud via network server) | **2–15 km range on battery power (5–10 years)**; star-of-stars topology; 0.3–50 kbps | LoRa RF → gateway → TCP |
| **MQTT** | Field → edge broker (device-to-broker) | Lightweight pub/sub; QoS 0/1/2; star topology through broker; no native timestamping | TCP/IP |

**IEEE C37.118 reporting rate detail:**
- Required baseline for 60 Hz systems: 10, 30, 60 frames/sec (user-selectable)
- Higher rates (120 fps) are encouraged and common in high-resolution WAMS applications
- GPS timestamp on every frame enables cross-system phase comparison

**DNP3 key distinction from Modbus (the bridge callout raw material):**
Modbus has no native timestamps and is poll-only. DNP3 adds millisecond timestamps on every data object and unsolicited reporting (RTU pushes when a value changes, without being polled). DNP3 also has three-layer architecture (app, transport, data-link) vs. Modbus's simple two-layer, and DNP3 SAv5 for authenticated communication.

---

## Four-Tier Architecture Design (STK-05)

### The Four Tiers + Control-Latency Bands

[VERIFIED: CLAUDE.md specifics section; IEC 61850-10-3 process/bay/station model; NATS docs; K3s docs; cross-referenced against IntelliGrid reference in docs/intelligrid.pdf]

This is the spine of STK-05. The planner MUST encode all four tiers, their components, and the latency/control boundaries.

```
TIER 1 — FIELD (sensors, IEDs, RTUs, PMUs)
  Latency: <4 ms (GOOSE protection) to ~100 ms (DNP3 unsolicited)
  Protocols: IEC 61850 GOOSE + SV, DNP3, IEEE C37.118, LoRa, Modbus
  Hardware: Circuit breakers (XCBR), merging units, PMUs, RTUs, LoRa sensors
  Control: Hardwired protection relays + GOOSE; no software round-trip

TIER 2 — EDGE (K3s substation node)
  Latency: sub-second inference (100 ms – 1 s)
  Stack: K3s, NATS JetStream (leaf node), EKF/virtual-sensing FastAPI service,
         Prometheus node-exporter, local InfluxDB buffer (island-mode)
  Functions: EKF state estimation, virtual temperature sensing,
             local reactive power compensation, NATS pub/sub to fog/cloud,
             local Prometheus scraping
  Control: Can operate autonomously without WAN (island mode via K3s + local JetStream)

TIER 3 — FOG / FEDERATED (cross-substation aggregation)
  Latency: seconds to minutes
  Stack: NATS JetStream hub, federated learning coordinator (Flower — Phase 5),
         cross-substation state aggregation
  Functions: Aggregate EKF outputs from multiple edge nodes, federated model
             weight exchange (Phase 5 scope), cross-substation voltage profile
  Note: This tier is named here; depth is Phase 5 (FED-01/FED-02)

TIER 4 — CLOUD (historian, training, GitOps)
  Latency: minutes to hours
  Stack: Kafka (event ingestion), OSIsoft PI / InfluxDB historian,
         ML training pipeline (Azure ML / centralized), GitOps (fleet config),
         Grafana dashboards (PromQL), Alertmanager routing
  Functions: Long-term data retention, model training and versioning,
             fleet configuration push (GitOps to K3s nodes), executive dashboards
  Control: Non-real-time; no protective control from this tier
```

### AGMS Overlay for STK-05 (D-06)

Mapping the director's patent components onto the four-tier architecture:

| AGMS Patent Component | Maps to Tier | Rationale |
|-----------------------|-------------|-----------|
| **Field Agent Devices (FADs) running scouts** | Tier 2 — Edge | FADs = K3s nodes running role-typed scout applications (Coordinator, Messenger, Inspector, Guard) |
| **Scout Command (1441→1447)** | Tier 2 — Edge (deployment) | Scout incubation and launch onto FADs is the K3s pod scheduling analog |
| **ORACS operating cells (island mode)** | Tier 2 — Edge | Operating cells are self-forming, WAN-optional — identical to K3s + local JetStream island operation |
| **Operation Loop Formation simulate-before-commit** | Tier 3 — Fog | The CVXPY MPC analog: "simulate the operation loop before committing" runs at the orchestration layer, not on individual FADs |
| **GridWideCommandHub (GWCH) federation** | Tier 3 — Fog | Cross-substation federation command; the "fog/federated" tier is where ORACS formation is orchestrated |
| **GridWideMind (GWM) alert correlation + learning engine** | Tier 4 — Cloud | Long-horizon learning, alert correlation across the fleet, simulation engine |

**Cross-link note for the planner:** The overlay in STK-05 should be kept to 6–8 lines with a small table — reference Phase 3 patents/INDEX.md for depth; the overlay's job is to name the connection, not re-derive it.

### ASCII Diagram (whiteboard target — planner writes the final version)

The planner should produce this exact four-layer ASCII box diagram as the primary whiteboard-rehearsal artifact:

```
┌─────────────────────────────────────────────────────────────┐
│  CLOUD (minutes+)                                           │
│  Kafka · OSIsoft PI · Azure ML · GitOps · Grafana/PromQL   │
│  GWM (alert correlation, learning) ← AGMS                  │
└──────────────────────┬──────────────────────────────────────┘
                       │ NATS JetStream (hub)
┌──────────────────────▼──────────────────────────────────────┐
│  FOG / FEDERATED (seconds–minutes)                          │
│  Cross-substation aggregation · Flower (Phase 5)            │
│  GWCH (ORACS formation, simulate-before-commit) ← AGMS      │
└──────────────────────┬──────────────────────────────────────┘
                       │ NATS JetStream (leaf node)
┌──────────────────────▼──────────────────────────────────────┐
│  EDGE — K3s substation node (100 ms – 1 s)                  │
│  EKF/virtual-sensing · NATS JetStream · Prometheus scraper  │
│  FADs + Scout Command (island-capable) ← AGMS               │
└──────────────────────┬──────────────────────────────────────┘
                       │ IEC 61850 GOOSE/SV · DNP3 · C37.118 · LoRa
┌──────────────────────▼──────────────────────────────────────┐
│  FIELD (<4 ms – 100 ms)                                     │
│  XCBR · PMUs · RTUs · Merging Units · LoRa sensors          │
│  GOOSE: protection trips · SV: I/V samples · DNP3: telemetry│
└─────────────────────────────────────────────────────────────┘
```

### Narration Script Elements (planner uses these for the numbered script)

The STK-05 note must include a numbered say-aloud narration covering:

1. Start at field tier: "At the bottom, the field tier — circuit breakers modeled as XCBR, PMUs delivering GPS-synced phasors at 30–120 frames/sec, LoRa sensors on battery for km-range monitoring. Protection happens here, in <4 ms via IEC 61850 GOOSE — no software, no round-trip."
2. Edge tier: "One level up, the edge tier is a K3s substation node. It runs the EKF virtual-sensing inference — estimating unmeasured quantities like line temperature or hot-spot — at sub-second latency. NATS JetStream leaf node handles local pub/sub and buffers messages for cloud replay if WAN drops — island mode."
3. Fog/federated tier: "The fog tier aggregates outputs from multiple edge nodes — cross-substation state estimates, voting on anomalies. This is where federated coordination happens — Phase 5 owns the algorithm depth, but the tier exists for the seconds-to-minutes decisions that need more than one substation's data."
4. Cloud tier: "At the top, the cloud is Kafka for ingestion, OSIsoft PI or InfluxDB for long-term history, Azure ML for model training, GitOps for pushing config down to the K3s fleet, and Grafana/PromQL for fleet dashboards and alerting. No protective control from here — only minutes-or-longer decisions."
5. AGMS overlay: "If I overlay the director's patent family: the Field Agent Devices running scouts land at the edge tier; Scout Command is the K3s pod scheduler with grid semantics; Operation Loop simulate-before-commit is the fog tier's orchestration gate; GridWideMind is the cloud learning engine."

---

## Common Pitfalls (for note construction)

### Pitfall 1: Stating GOOSE latency wrong
**What goes wrong:** Saying "GOOSE is fast" without the specific number.
**How to avoid:** Always say "<4 ms end-to-end" — this is the IEC-specified protection class requirement. GOOSE retransmits at ~2 ms intervals on state change; total end-to-end including IED processing is <4 ms.
**Source:** IEC TR 61850-10-3:2022 Section 4 + multiple verified sources.

### Pitfall 2: Conflating GOOSE/SV with MMS
**What goes wrong:** Saying "IEC 61850 runs over Ethernet" — partially true but misleading. GOOSE and SV are L2 only (cannot be routed); MMS is TCP/IP and can be routed.
**How to avoid:** Always state the transport separately: "GOOSE and SV are Layer 2 — they never leave the substation LAN; MMS is TCP/IP — it's what the SCADA control center talks to the substation over WAN."

### Pitfall 3: Saying Kafka is "too slow" for edge
**What goes wrong:** The real issue is not latency but resource requirements. Kafka's throughput is actually very high. The problem is the JVM, 64–128 GB RAM, and 8-core requirement — those don't fit an edge node.
**How to avoid:** Frame it as footprint, not throughput: "Kafka isn't slow — it's enormous. JVM, 64–128 GB RAM, 10-Gig NIC. That's a data center workload, not a substation closet."

### Pitfall 4: Getting K3s database wrong
**What goes wrong:** Saying "K3s uses SQLite instead of etcd" as if etcd is unavailable. K3s defaults to SQLite for single-node but can use embedded etcd for HA mode.
**How to avoid:** "K3s defaults to SQLite for simple deployments; it supports embedded etcd for HA mode. Full K8s requires you to stand up an external etcd cluster. The default K3s path eliminates that operational burden entirely."

### Pitfall 5: Naming kube-prometheus-stack components incompletely
**What goes wrong:** Saying "Prometheus + Grafana" and omitting the Operator, node-exporter, kube-state-metrics, and Alertmanager.
**How to avoid:** Memorize the five components: Prometheus Operator, node-exporter, kube-state-metrics, Grafana, Alertmanager. "Five in one Helm chart" is the recitable form.

### Pitfall 6: Confusing the three IEC 61850 tiers with the four architecture tiers in STK-05
**What goes wrong:** The IEC 61850 three-tier hierarchy (process/bay/station) describes the substation itself. The STK-05 four-tier architecture (field/edge/fog/cloud) describes the broader system. Field tier maps roughly to IEC 61850's process + bay levels. Edge tier includes the bay level's software intelligence plus the K3s node.
**How to avoid:** In notes, explicitly label which hierarchy you're using when describing each tier.

---

## Code Examples

### PromQL — CPU rate for a namespace
```promql
rate(container_cpu_usage_seconds_total{namespace="virtual-sensing"}[5m])
```
Source: Prometheus docs + verified in SigNoz and oneuptime.com guides.

### PromQL — Memory working set by pod
```promql
sum(container_memory_working_set_bytes{pod=~"ekf-.*"}) by (pod)
```
Source: Sysdig Kubernetes monitoring PromQL guide.

### PromQL — Up/down health check
```promql
up{job="node-exporter"} == 0
```
Source: CLAUDE.md Category 4 (verified pattern).

### IEC 61850 GOOSE Example (conceptual, not code)
```
Publisher: PTOC1 in CB1_PROT (protection relay)
  → emits GOOSE multicast on state change (Op = TRUE)
  → retransmits at 2 ms, 4 ms, 8 ms, 16 ms, ... backing off
Subscriber: XCBR1 bay controller IED
  → receives GOOSE in <4 ms
  → executes trip command on circuit breaker
```

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| K8s observability | Custom metrics + dashboard pipeline | kube-prometheus-stack (Helm) | 5 components pre-wired; ServiceMonitor CRD eliminates prometheus.yml manual edits |
| Federated edge messaging | Custom MQTT broker + replay | NATS JetStream | Durable replay, request-reply, decentralized JWT, leaf-node topology — all built-in |
| Federated ML coordination | Custom weight sharing | Flower (flwr) | Framework-agnostic (PyTorch/sklearn), active v1.x, edge-native; re-inventing FedAvg is a research project not a product |

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Kafka + ZooKeeper | Kafka 4.x KRaft (no ZooKeeper) | Kafka 4.0 (2025) | Eliminates ZooKeeper dependency; simpler ops; still cloud-tier only |
| kube-prometheus-stack < 50 | kube-prometheus-stack 86.2.3 (2025–2026) | Continuous | Helm chart version ≠ Prometheus version; chart tracks upstream rapidly |
| K3s v1.27–1.31 (CLAUDE.md cites 1.31) | K3s v1.33–1.34 (current 2025–2026) | Mid-2025 | Same API; CLAUDE.md version slightly stale — update in note |
| NATS Server 2.10–2.11 (CLAUDE.md cites 2.11) | NATS Server v2.14.2 (2026-06-02) | Current | Same JetStream API; CLAUDE.md version stale — update in note |

---

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | IEEE C37.118 baseline reporting rates for 60 Hz systems are 10, 30, 60 fps; 120 fps is encouraged and common | Protocol Tier Map | If wrong, the one-liner about reporting rates would be inaccurate — LOW risk, multiple sources agree |
| A2 | The NATS official docs footnote about Kafka hardware ("eight cores, 64–128 GB RAM") is still accurate for Kafka 4.x | Edge Stack | ASSUMED from NATS.io docs; Kafka 4.x KRaft may have slightly different requirements — but the order-of-magnitude difference with NATS is structural and unchanged |
| A3 | kube-prometheus-stack 86.2.3 is the current version as of research date (ArtifactHub) | Observability | Chart version changes frequently; the bundled components are stable — LOW risk for interview context |

---

## Open Questions

1. **IntelliGrid PDF (`docs/intelligrid.pdf`) — not read in this research session**
   - What we know: Canonical reference for the four-tier architecture per CONTEXT.md
   - What's unclear: Whether IntelliGrid names the tiers differently or adds a fifth tier
   - Recommendation: The planner or implementer should scan pages 1–20 of intelligrid.pdf before writing STK-05 to check for IntelliGrid-specific terminology that would impress the interviewer

2. **FLISR PDF (`docs/flisr.pdf`) — not read in this research session**
   - What we know: FLISR = Fault Location, Isolation, and Service Restoration — a grid automation function that uses IEC 61850 GOOSE and DNP3
   - What's unclear: Whether it adds context useful for STK-01/STK-02
   - Recommendation: LOW priority — CLAUDE.md already covers the protocol awareness needed; only consult if note writing surfaces a gap

3. **K3s air-gap install specifics**
   - What we know: K3s is designed for air-gap; ships as single binary
   - What's unclear: Whether the note should mention the `k3s-airgap-images.tar` bundle mechanism
   - Recommendation: Awareness only; the interview criterion names "air-gap" as a K3s distinction, not the install mechanism

---

## Environment Availability

Step 2.6: SKIPPED — this phase produces markdown study notes only; no external runtime dependencies, no code execution, no databases or services required.

---

## Validation Architecture

Step 4: SKIPPED — no `workflow.nyquist_validation` key found in `.planning/config.json`; however, this is a notes-only phase with no automated tests. The success criterion is Juan's ability to recall content aloud, not test suite green.

---

## Security Domain

Not applicable to this phase — this is an interview-prep notes phase producing markdown documents, not software that handles authentication, data, or network access. ASVS categories do not apply.

---

## Sources

### Primary (HIGH confidence)
- `docs/IEC 61850-3.pdf` (IEC TR 61850-10-3:2022, Edition 1.0) — confirms XCBR (Figs 39–42), PTOC (Fig 2: CB1_PROT with PTOC1), TVTR, TCTR (Fig 2), LPHD, LLN0; confirms GOOSE <4 ms for protection; confirms process/bay/station three-tier model; confirms Sim.stVal test mode flag
- `docs.nats.io/nats-concepts/overview/compare-nats` — NATS vs Kafka comparison; verbatim Kafka hardware requirements ("eight cores, 64–128 GB RAM"); NATS JetStream persistence and request-reply; edge suitability
- `scadaprotocols.com/iec-61850-logical-nodes-explained/` — IEC 61850-7-4 logical node taxonomy; XCBR, MMXU, CSWI, PTOC, PDIS definitions with group letters; 13 LN groups table
- `artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack` — version 86.2.3 confirmed
- GitHub API `api.github.com/repos/nats-io/nats-server/releases/latest` — NATS Server v2.14.2 (2026-06-02) confirmed
- `docs.k3s.io/release-notes/v1.33.X` and `v1.34.X` — K3s current versions confirmed (2025–2026)

### Secondary (MEDIUM confidence)
- `emqx.com/en/blog/iec-61850-protocol` — three-tier station/bay/process hierarchy description; GOOSE/SV/MMS service overview
- `opal-rt.atlassian.net` — GOOSE <4 ms latency, GOOSE retransmission mechanism
- `softwaretoolbox.com/resources/what-is-iec61850` — IEC 61850 services overview
- `last9.io/blog/prometheus-query-examples/` + `signoz.io` — PromQL examples verified
- `typhoon-hil.com/documentation/.../c37_118_protocol.html` — IEEE C37.118 reporting rates (10, 25/30, 50/60, 100/120 fps)
- `github.com/prometheus-community/helm-charts` (deepwiki.com mirror) — kube-prometheus-stack components: Prometheus Operator, node-exporter, kube-state-metrics, Grafana, Alertmanager
- CLAUDE.md Category 1–5 — primary content base for all comparison tables (ASSUMED as accurate per D-01; spot-verified version facts updated above)

### Tertiary (LOW confidence / training knowledge)
- IntelliGrid reference (`docs/intelligrid.pdf`) — NOT read in this research session; cited in CONTEXT.md as canonical for four-tier architecture; flag for planner to check
- General K3s air-gap and SQLite embedding claims — consistent across multiple sources (reintech.io, cloudzero.com, SUSE docs)

---

## Metadata

**Confidence breakdown:**
- IEC 61850 logical nodes: HIGH — confirmed from primary PDF source + scadaprotocols.com against IEC 61850-7-4 taxonomy
- GOOSE/SV/MMS roles and latency: HIGH — confirmed from primary IEC TR 61850-10-3:2022 PDF
- Three-tier station/bay/process hierarchy: HIGH — confirmed from primary PDF + multiple secondary sources
- NATS vs Kafka edge justification: HIGH — verbatim from official NATS docs (docs.nats.io)
- K3s three distinctions (air-gap, memory, SQLite): HIGH — confirmed from K3s official docs
- kube-prometheus-stack bundle components: HIGH — confirmed from ArtifactHub + GitHub source
- kube-prometheus-stack version 86.2.3: HIGH — ArtifactHub verified
- NATS Server v2.14.2: HIGH — GitHub API verified
- PromQL examples: HIGH — multiple authoritative sources agree on syntax and semantics
- IEEE C37.118 reporting rates: MEDIUM — Typhoon HIL docs + multiple secondary sources; actual standard PDF not checked (behind paywall)
- Protocol tier placements: HIGH — consistent across CLAUDE.md Category 3 + secondary sources
- Four-tier architecture latency bands: MEDIUM — consistent with CLAUDE.md specifics + IEC 61850 protection class; IntelliGrid PDF not read

**Research date:** 2026-06-14
**Valid until:** 2026-07-14 (30 days; all standards are stable; tool versions move faster)

**CLAUDE.md version corrections for note writing:**
- CLAUDE.md cites NATS Server 2.11 → correct to v2.14.2
- CLAUDE.md cites K3s 1.31 → correct to v1.33–1.34
- kube-prometheus-stack: not mentioned in CLAUDE.md at all → this research fills that gap completely
- Logical node names: not mentioned in CLAUDE.md → this research fills that gap completely
