# STK-03: Edge Messaging & Orchestration — NATS/MQTT/Kafka, K3s/K8s

**For:** Oral rehearsal — speak each section aloud before the interview.
**Purpose:** Justify NATS JetStream over MQTT and over Kafka for the substation edge, and
state the three K3s-vs-K8s distinctions (memory, etcd/SQLite, air-gap) with interview-ready
one-liners — so you can answer "why this stack at the edge?" without notes.

---

## 1. The Edge Constraint Mental Model

The decision driver for the substation edge stack is **footprint**, not throughput. A
substation edge node is a Pi-class or small industrial PC — often in a metal cabinet in a
substation yard, air-gapped from corporate WAN, battery-backed, running on embedded hardware.
It cannot host a JVM. It cannot guarantee a 10-Gig NIC. It may need to operate in island
mode — disconnected from the cloud — for minutes or hours.

That single constraint rules out entire categories of software. Kafka, for example, is
not slow — it handles millions of messages per second. The problem is what it *requires*
(more on this in Section 3). The constraint shapes every stack choice that follows:
messaging, orchestration, and observability.

Pre-empt this pitfall in the interview: do NOT say "Kafka is too slow for the edge." Say
"Kafka isn't slow — it's enormous. That's a different problem."

---

## 2. NATS JetStream vs MQTT — Four Reasons for the Federated Edge

MQTT is designed for **device-to-broker**: a lightweight pub/sub protocol where every
device connects to a central broker (e.g., Mosquitto). It works well when the broker is
reliably reachable, when QoS levels suffice for delivery guarantees, and when you don't
need durability beyond the broker's in-memory queue.

At the substation edge, none of those assumptions hold cleanly. Four reasons NATS
JetStream is the better fit:

### Reason 1 — Durable Replay (Island Mode)

**MQTT:** QoS 0 is fire-and-forget. QoS 1/2 adds acknowledgment, but messages live
only in the broker's transient store. If the cloud WAN link drops, outbound messages
are gone.

**NATS JetStream:** Persists messages to disk in an append-only log. When WAN returns,
subscribers (cloud side) replay from the last acknowledged offset. No data is lost during
a network partition — this is the critical difference for island-mode operation.

### Reason 2 — Built-in Request-Reply

**MQTT:** There is no native request-reply. You build it manually: publish on topic A,
subscribe on topic B, correlate via a custom header. Every service must implement its own
correlation-ID logic.

**NATS:** Request-reply is a first-class primitive. `nc.Request("service.infer", payload)`
sends the message and blocks for a response — zero application-level plumbing. Edge
inference services (EKF, virtual-sensing FastAPI) need synchronous request-response; NATS
gives this out of the box.

### Reason 3 — Decentralized JWT Security Accounts

**MQTT:** Security is username/password or TLS client certs — flat, centralized. In a
multi-tenant substation (multiple utilities on shared infrastructure), you need isolation
between tenants without a central auth server reachable at all times.

**NATS:** Uses decentralized JWT accounts — each account is an isolated messaging
namespace, with credentials signed by an operator key. An edge node can authenticate
locally even without WAN connectivity. Multi-tenant isolation is structural, not
configuration-managed.

### Reason 4 — Leaf Node Topology

**MQTT:** Star topology — all traffic flows through the broker. The broker must be
reachable from both publisher and subscriber. At the substation edge, this means the
broker must be on the LAN (fine for local) but the cloud endpoint must poll or tunnel.

**NATS:** Leaf nodes bridge the substation LAN to a NATS hub cluster in the cloud without
a VPN. The leaf node connects outbound (firewall-friendly), replicates subjects selectively,
and operates locally if the hub is unreachable. This is the federated mesh model — edge
operates independently, then syncs when connectivity returns.

### NATS vs MQTT Summary

| Dimension | MQTT (Juan has) | NATS JetStream (gap) |
|-----------|-----------------|----------------------|
| Persistence | Optional; broker-side, transient | JetStream: durable log, disk-backed, replayable |
| Request-reply | Manual correlation-ID pattern | Built-in primitive |
| Security model | Username/password, TLS | Decentralized JWT accounts |
| Topology | Star (all through broker) | Leaf nodes + clusters: mesh |
| Island operation | Broker must be reachable | Leaf node operates disconnected, replays on reconnect |
| Exactly-once | No | Yes (JetStream) |
| Edge footprint | Mosquitto ~1 MB | NATS binary ~20 MB |
| Target users | Devices → broker | Services ↔ services + devices |

---

## 3. NATS JetStream vs Kafka — The Quote (Highest-Yield Specific)

This is the most recitable, most differentiating fact in the entire STK-03 note. Learn
it verbatim.

The NATS official documentation states:

> "Kafka servers require a JVM, eight cores, 64 GB to 128 GB of RAM, two or more
> 8-TB SAS/SSD disks, and a 10-Gig NIC."

A substation edge node is a Pi-class or small industrial PC. NATS JetStream runs as a
**single static binary under 20 MB on approximately 512 MB of RAM**. This is not a
performance tradeoff — it is an architectural incompatibility. Kafka is built for the
data center tier, not the substation closet.

### Three Kafka-vs-NATS Distinctions Beyond Footprint

1. **JVM GC pauses:** Even G1GC or ZGC can inject pauses of tens of milliseconds.
   At the edge, where virtual-sensing inference latency matters and protection monitoring
   is adjacent, latency spikes are unacceptable. NATS is a static Go binary — no garbage
   collector pauses of consequence.

2. **Coordination dependency:** Kafka 4.x uses KRaft (eliminating ZooKeeper), but still
   requires a controller quorum. NATS is fully self-contained — no external coordination
   process, single binary, single config file.

3. **Request-reply model:** Kafka requires application code to correlate requests with
   replies over multiple topics. NATS has built-in request-reply (same as Section 2,
   Reason 2 above).

### The Interview One-Liner

> "Kafka at the substation edge is like bringing a semi-truck to park in a bicycle lane
> — it needs a JVM, 64–128 GB RAM, and a 10-Gig NIC. NATS JetStream is a 20 MB binary
> on a Pi-class node."

Frame this as footprint, not speed. Kafka's throughput is exceptional. The problem is
what it takes to run it.

### One-Line Pulsar Awareness

Apache Pulsar (the third JD-named streaming system) shares Kafka's edge-unsuitability:
its separated storage-and-serving architecture (BookKeeper + broker) is similarly
data-center class. For the substation edge, both Kafka and Pulsar are ruled out by
footprint; NATS JetStream is the only production choice. (Do not deep-dive Pulsar
internals — awareness is sufficient.)

### NATS vs Kafka vs Pulsar Summary

| Dimension | NATS JetStream | Kafka | Pulsar |
|-----------|----------------|-------|--------|
| Edge deployment | Yes — single binary, Pi-class | No — JVM + 64–128 GB RAM | No — BookKeeper + broker |
| RAM minimum | ~512 MB | 64–128 GB (production) | High (data center class) |
| Coordination | None (self-contained) | KRaft controller quorum | BookKeeper ensemble |
| Edge verdict | **Edge-native** | Cloud-tier only | Cloud-tier only |

---

## 4. The Three K3s-vs-K8s Distinctions

These are the three the success criteria name explicitly. Know them by name:
**memory**, **etcd/SQLite**, **air-gap**.

| Distinction | K3s | Full K8s |
|-------------|-----|---------|
| **Memory footprint** | ~512 MB RAM for a server node | 2–4 GB minimum per node |
| **Database (etcd/SQLite)** | Defaults to **embedded SQLite** for single-node; **embedded etcd** available for HA mode | Requires an external etcd cluster |
| **Air-gap design** | Built for it — single binary <100 MB; ships with Traefik ingress + local-path provisioner; `curl \| sh` install | Complex: kubeadm, multiple binaries, external etcd, choose-your-own ingress |

### On the Database Distinction (Pitfall 4 Pre-Empt)

Do NOT say "K3s uses SQLite instead of etcd." Say: "K3s **defaults** to SQLite for
single-node deployments, eliminating the external etcd dependency entirely. For HA mode,
it switches to embedded etcd. Full K8s requires you to provision and operate an external
etcd cluster regardless."

This matters because it shows you understand K3s's HA path, not just its single-node
default.

### K3s Context (Frame It as Production-Grade)

K3s is a Rancher/SUSE project, CNCF-certified, and deployed in production at telco edge
and substation environments. It is not a toy Kubernetes. It provides the full Kubernetes
API surface — the same `kubectl` commands, the same manifests, the same Helm charts —
with components stripped (no in-tree cloud-provider drivers, no alpha features, no legacy
addons). Current stable: K3s v1.33/v1.34 (tracks upstream Kubernetes minor release cycle).

### K3s vs Full K8s Summary

| Dimension | K3s | Full K8s |
|-----------|-----|---------|
| RAM minimum | ~512 MB / server node | 2–4 GB / node |
| Database | SQLite default (single-node); embedded etcd (HA) | External etcd cluster required |
| Air-gap | Designed for it — single binary, bundled deps | Complex multi-component setup |
| Ingress | Traefik included | Choose and install separately |
| Local storage | local-path provisioner included | External provisioner required |
| Install | `curl \| sh` single binary | kubeadm + multiple steps |
| ARM support | First-class (Pi, Jetson) | Limited |
| K8s API parity | Full (same kubectl, manifests, Helm) | Full |
| Production use | Telco edge, substation, IoT | Cloud/datacenter |

---

## <3-min say-aloud version

> "The substation edge node is a Pi-class industrial PC — often air-gapped, running on
> limited RAM. That constraint, not throughput, decides the stack.
>
> For messaging: I'd use NATS JetStream over MQTT because of four things — durable replay
> (JetStream persists messages for replay when WAN returns; MQTT only has transient QoS
> levels), built-in request-reply (no manual correlation IDs), decentralized JWT accounts
> for multi-tenant isolation without a central auth server, and leaf-node topology that
> bridges the substation LAN to the cloud without a VPN.
>
> Over Kafka? The NATS docs say it directly: Kafka needs a JVM, eight cores, 64 to 128 GB
> of RAM, two 8-TB disks, and a 10-Gig NIC. That's a data center rack, not a substation
> closet. NATS JetStream runs in 20 MB on 512 MB of RAM. Kafka isn't slow — it's
> enormous. Pulsar has the same problem.
>
> For orchestration: K3s over full K8s for three reasons. Memory — K3s uses ~512 MB per
> node vs 2–4 GB for K8s. Database — K3s defaults to embedded SQLite for single-node,
> embedded etcd for HA; full K8s requires you to stand up an external etcd cluster. And
> air-gap design — K3s ships as a single binary under 100 MB with Traefik and local-path
> provisioner included, designed for disconnected environments. Same K8s API surface,
> same manifests and Helm charts, just 4x lighter and built for the field."

---

## → Bridge to your work

> **MQTT → NATS JetStream:** "I ran MQTT-to-Mosquitto in OSED for device telemetry
> in the building grid services platform. NATS JetStream is the same publish-subscribe
> instinct but adds durable replay and decentralized JWT accounts for the federated edge
> — that's the upgrade path I'd take here."

> **Full Kubernetes → K3s:** "I've shipped Kubernetes in production at OSED — same API,
> same manifests and Helm charts. K3s is the same interface at 4x lighter, with SQLite
> default and air-gap design built in. The operational delta is minimal for a K8s
> practitioner."

| My existing tool | Gap tool | The upgrade |
|------------------|----------|-------------|
| MQTT + Mosquitto (OSED) | NATS JetStream | Same pub/sub mental model + durable replay + request-reply + JWT + leaf nodes |
| Full Kubernetes (OSED) | K3s | Same API surface + 4x lighter memory + SQLite-default + air-gap design |

**How to say this in the interview:**

> "I built the OSED edge platform on Kubernetes with MQTT for telemetry and InfluxDB for
> time-series. In the GE Vernova stack, the direct analogs are K3s for orchestration —
> same API, 4x lighter, designed for the substation field environment — and NATS JetStream
> for messaging, which adds the durable replay and decentralized JWT accounts that MQTT
> doesn't give you. The mental model is the same; the upgrade is the edge-specific
> operational properties."

---

## Quick-Recall Card (Recite Before the Interview)

1. **Edge constraint:** Footprint, not throughput. Pi-class node, air-gapped, limited RAM. This rules out Kafka and Pulsar.
2. **NATS over MQTT — four reasons:** (a) durable replay for island mode, (b) built-in request-reply, (c) decentralized JWT accounts, (d) leaf-node topology to cloud without VPN.
3. **NATS over Kafka — the quote:** "Kafka needs a JVM, eight cores, 64–128 GB RAM, two 8-TB disks, a 10-Gig NIC." NATS JetStream = 20 MB binary on 512 MB RAM. Frame as footprint, not speed.
4. **Kafka interview one-liner:** "Kafka at the substation edge is like bringing a semi-truck to park in a bicycle lane."
5. **Pulsar (awareness only):** Same edge-unsuitability as Kafka — storage-separated architecture (BookKeeper + broker) is data-center class.
6. **K3s vs K8s — three distinctions:** (a) **Memory:** ~512 MB vs 2–4 GB. (b) **Database:** SQLite default (single-node) or embedded etcd (HA) — no external etcd cluster required. (c) **Air-gap:** single binary <100 MB, Traefik + local-path included, `curl | sh` install.
7. **K3s pitfall:** Don't say "no etcd." Say "SQLite default; embedded etcd for HA."
8. **My bridge:** MQTT → NATS (same pub/sub, add replay + JWT); full K8s → K3s (same API, 4x lighter, air-gap).

---

*Sources: docs.nats.io/nats-concepts/overview/compare-nats (NATS vs Kafka/MQTT feature comparison; Kafka hardware requirements verbatim); docs.k3s.io (K3s memory, SQLite/etcd, air-gap documentation); CLAUDE.md Categories 1–2 and Summary Reference Table (comparison tables, bridge raw material); Juan's CV (OSED platform: MQTT, Kubernetes, InfluxDB, Grafana at edge).*
