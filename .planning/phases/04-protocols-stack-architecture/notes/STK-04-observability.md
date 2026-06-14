# STK-04: Observability — Prometheus, PromQL & kube-prometheus-stack

**For:** Oral rehearsal — speak each section aloud before the interview.
**Purpose:** Explain the Prometheus pull model vs InfluxDB push, recite a concrete PromQL
query, and name what kube-prometheus-stack adds (all five bundled components) — so you can
answer observability architecture questions with the specific stack name and a real query,
not just "Prometheus plus Grafana."

---

## 1. Pull vs Push Mental Model

**The single most important conceptual shift:** Prometheus does not receive metrics — it
goes out and *fetches* them. This is the opposite of how InfluxDB works.

| Dimension | Prometheus (gap) | InfluxDB (Juan has) |
|-----------|------------------|---------------------|
| Ingest model | **Pull** — Prometheus scrapes `/metrics` endpoints on a schedule | **Push** — services write to InfluxDB via API/line protocol |
| Query language | **PromQL** | Flux / InfluxQL |
| K8s integration | **Native** — ServiceMonitor CRDs, automatic pod discovery | Manual wiring |
| Alert rules | **Native** — alerting rules in Prometheus + Alertmanager | External (Kapacitor / Grafana alerts) |
| Default retention | 15 days (short; not a long-term store) | Configurable (long-term) |
| Cardinality | Sensitive to high-cardinality labels | Higher tolerance |

### The Pull Model's Key Implication

Services do not need to know where to send metrics. They expose a `/metrics` HTTP endpoint
(e.g., FastAPI with `prometheus_client`). Prometheus finds those endpoints via Kubernetes
service discovery — specifically, by watching **ServiceMonitor** custom resources — and
scrapes them on a configurable schedule (default: 15 seconds).

This is precisely why Prometheus integrates so naturally with Kubernetes: **pod IPs change
constantly** (pods restart, scale up/down, roll out). With a push model, every service
would need to know the current address of the metrics receiver. With Prometheus, the
services don't care — they just expose `/metrics`, and Prometheus discovers them through
the K8s API.

**Say aloud:** "Prometheus doesn't receive metrics — it scrapes them. Services just expose
a `/metrics` endpoint. Prometheus uses a ServiceMonitor CRD to discover them in K8s
automatically. That's why it fits Kubernetes — pod IPs change; the pull model abstracts
that away."

---

## 2. kube-prometheus-stack — The Named Gap

CLAUDE.md's Category 4 never names **kube-prometheus-stack** — this is the specific gap
the plan fills. In interviews, saying "I'd install Prometheus and Grafana and wire them
together" signals you don't know the production-standard distribution.

**The production answer:** `kube-prometheus-stack` is a single Helm chart (current stable
chart version ~86.2.3) that bundles **five components** pre-wired and ready to deploy.

### The Five Components (Pitfall 5: Never Say "Just Prometheus + Grafana")

1. **Prometheus Operator** — A Kubernetes controller that watches for `ServiceMonitor`
   and `PodMonitor` CRDs and auto-configures Prometheus scrape targets. You do NOT
   hand-edit `prometheus.yml`. You create a `ServiceMonitor` custom resource that points
   at your service, and the Operator rewrites the Prometheus config automatically.

2. **node-exporter** — A DaemonSet deployed on every K3s/K8s node. Exposes Linux host
   metrics (CPU utilization, memory, disk I/O, network throughput) as `/metrics`. This
   is how you see node-level resource usage in Grafana dashboards.

3. **kube-state-metrics** — Queries the Kubernetes API server and exposes Kubernetes
   object states as metrics: pod running/pending/failed, deployment replica counts,
   PersistentVolumeClaim status, etc. Without this, Prometheus only sees what's inside
   pods, not what K8s *thinks* the cluster state is.

4. **Grafana** — Visualization layer; comes pre-loaded with Kubernetes dashboards. Reads
   from Prometheus using PromQL queries. This is the part Juan already knows from OSED —
   the shift is that Grafana here reads via PromQL rather than InfluxQL/Flux.

5. **Alertmanager** — Receives firing alerts from Prometheus alerting rules and routes
   them to PagerDuty, Slack, email, or webhook. Handles deduplication, grouping, and
   silencing. This is what InfluxDB + Kapacitor handled in push-model stacks.

### The Interview Sentence (Say This Verbatim)

> "Instead of installing Prometheus, Grafana, and the exporters separately and wiring them
> together, kube-prometheus-stack is a single Helm chart that delivers Prometheus Operator,
> node-exporter, kube-state-metrics, Grafana, and Alertmanager pre-wired. The Operator
> pattern means you define what to scrape with a ServiceMonitor CRD and the Operator
> manages Prometheus config automatically."

### Memory Aid for the Five Components

**"PnKGA"** — Prometheus Operator, node-exporter, kube-state-metrics, Grafana, Alertmanager.
Or: "Operator finds targets, node-exporter reports the host, kube-state-metrics reports the
cluster, Grafana shows both, Alertmanager pages you."

---

## 3. A Recitable PromQL Query

### The Primary Query (Learn This Verbatim)

```promql
rate(container_cpu_usage_seconds_total{namespace="virtual-sensing"}[5m])
```

**What it does:** Computes the per-second CPU usage rate averaged over the last 5 minutes
for all containers in the `virtual-sensing` namespace.

**Why `rate()` is required:** `container_cpu_usage_seconds_total` is a **cumulative
counter** — it counts CPU seconds consumed since the container started. A raw counter is
not useful for "current CPU usage." The `rate()` function computes the per-second increase
over the specified time window, which gives you CPU utilization as a rate.

**Anatomy of the query:**
- `container_cpu_usage_seconds_total` — the metric name (from cAdvisor, bundled with K8s)
- `{namespace="virtual-sensing"}` — label matcher: filter to only the virtual-sensing namespace
- `[5m]` — time window: look back 5 minutes to compute the rate
- `rate(...)` — converts the counter to a per-second rate

**Say aloud:** "Rate of container CPU usage, filtered to the virtual-sensing namespace,
averaged over a 5-minute window. Rate is required because the metric is a cumulative counter."

### Additional Awareness Queries

```promql
# Memory working set in bytes, grouped by pod (for EKF pods)
sum(container_memory_working_set_bytes{pod=~"ekf-.*"}) by (pod)
```

```promql
# Count of ready pods in the namespace (from kube-state-metrics)
kube_pod_status_ready{condition="true", namespace="virtual-sensing"}
```

```promql
# Alert: node-exporter scrape target is down (0 = down)
up{job="node-exporter"} == 0
```

### PromQL Building Blocks to Name

| Building Block | Syntax | When to Use |
|----------------|--------|-------------|
| Rate of counter | `rate(counter[window])` | Convert cumulative counter to per-second rate |
| Aggregate by label | `sum(...) by (label)` | Group instances by a label (e.g., sum by pod) |
| Exact label match | `{label="value"}` | Filter to specific value |
| Regex label match | `{label=~"pattern"}` | Filter with regex (e.g., `pod=~"ekf-.*"`) |
| Negative match | `{label!="value"}` or `{label!~"pattern"}` | Exclude by label |
| Heartbeat metric | `up` | 0 = Prometheus cannot scrape the target; built-in health check |

---

## 4. Where Observability Runs in the Architecture

Prometheus runs at **both** edge and cloud:

- **Edge (K3s node):** A Prometheus instance scrapes the local node-exporter, the
  kube-state-metrics for the local K3s node, and the virtual-sensing FastAPI service's
  `/metrics` endpoint. This gives sub-second latency local observability without WAN.
- **Cloud:** A centralized Prometheus (or Thanos/Mimir for long-term storage) scrapes
  aggregated metrics from all edge nodes, or receives federation from edge Prometheus
  instances. Grafana is centralized here, with PromQL dashboards across the fleet.

(Full tier placement is covered in STK-05's four-tier reference architecture.)

---

## <3-min say-aloud version

> "Observability: the key mental model shift is pull vs push. I ran InfluxDB in OSED on a
> push model — services write to InfluxDB. Prometheus inverts that: services expose a
> `/metrics` endpoint, Prometheus scrapes them. The advantage for K8s is that pod IPs
> change constantly — with pull, services just expose their endpoint and Prometheus finds
> them through a ServiceMonitor CRD. No reconfiguration when pods restart.
>
> For deployment, I wouldn't install Prometheus and Grafana separately. The production
> standard is kube-prometheus-stack — a single Helm chart that bundles five components
> pre-wired: Prometheus Operator, node-exporter, kube-state-metrics, Grafana, and
> Alertmanager. The Operator watches ServiceMonitor CRDs and auto-configures scrape
> targets — you never touch prometheus.yml.
>
> For a recitable query: `rate(container_cpu_usage_seconds_total{namespace="virtual-sensing"}[5m])`
> — that's the per-second CPU rate for all containers in the virtual-sensing namespace,
> averaged over 5 minutes. Rate is required because the underlying metric is a cumulative
> counter. For alerting: `up{job="node-exporter"} == 0` means the node-exporter scrape
> target is unreachable — that's your node-down alert."

---

## → Bridge to your work

> **InfluxDB + Grafana (Juan has) → Prometheus + PromQL:** "Prometheus pull-scrapes K8s
> pods; Grafana visualizes via PromQL. I ran the push-model version — InfluxDB + Grafana —
> in OSED. Prometheus inverts the data flow with native K8s service discovery, and
> kube-prometheus-stack gives me the whole stack — Operator, exporters, Grafana,
> Alertmanager — in one Helm install."

| My existing stack (OSED) | GE Vernova stack | The difference |
|--------------------------|------------------|----------------|
| InfluxDB (push: services write) | Prometheus (pull: scrapes `/metrics`) | Inverted data flow; Prometheus discovers targets via K8s |
| InfluxQL / Flux queries | PromQL | `rate()`, `sum() by ()`, label matchers |
| Grafana (reads InfluxDB) | Grafana (reads Prometheus via PromQL) | Same Grafana; different data source + query language |
| Grafana alerts / Kapacitor | Alertmanager (bundled in kube-prometheus-stack) | Native Prometheus alerting rules + Alertmanager routing |
| Manual wiring of components | kube-prometheus-stack (single Helm chart) | Pre-wired: Operator + 4 components in one install |

**How to say this in the interview:**

> "I ran InfluxDB + Grafana in OSED on a push model — services write to InfluxDB, Grafana
> queries with InfluxQL. Prometheus inverts that to a pull/scrape model with native K8s
> service discovery, which fits Kubernetes much better because pod IPs change dynamically.
> The production deployment is kube-prometheus-stack — a single Helm chart that gives me
> Prometheus Operator, node-exporter, kube-state-metrics, Grafana, and Alertmanager
> pre-wired. The Grafana piece I already know well; the Operator and ServiceMonitor CRD
> pattern are the operational upgrade."

---

## Quick-Recall Card (Recite Before the Interview)

1. **Pull vs push:** Prometheus scrapes `/metrics` on a schedule; InfluxDB receives writes from services. Pull fits K8s because pod IPs change — services expose the endpoint, Prometheus discovers via ServiceMonitor.
2. **kube-prometheus-stack — the chart name:** Single Helm chart, current version ~86.2.3. Bundles **five** components:
   - **Prometheus Operator** — watches ServiceMonitor CRDs, auto-configures scrape targets
   - **node-exporter** — DaemonSet; Linux host metrics (CPU/mem/disk/net)
   - **kube-state-metrics** — K8s object states (pod/replica/PVC status)
   - **Grafana** — visualization, pre-loaded K8s dashboards
   - **Alertmanager** — alert routing to PagerDuty/Slack/email/webhook
3. **The recitable query:** `rate(container_cpu_usage_seconds_total{namespace="virtual-sensing"}[5m])` — per-second CPU rate for virtual-sensing namespace, 5-minute window. `rate()` is required because the metric is a cumulative counter.
4. **Down-node alert:** `up{job="node-exporter"} == 0` — Prometheus's own scrape health; 0 = target unreachable.
5. **PromQL building blocks:** `rate(counter[window])`, `sum(...) by (label)`, label matchers `=`, `!=`, `=~`, `!~`, and `up` heartbeat.
6. **Pitfall:** Never say "Prometheus + Grafana." Say "kube-prometheus-stack — five components, one Helm chart: Operator, node-exporter, kube-state-metrics, Grafana, Alertmanager."
7. **My bridge:** InfluxDB + Grafana push-model (OSED) → Prometheus pull-model + kube-prometheus-stack (same Grafana, different data source, Operator-managed, native K8s service discovery).

---

*Sources: Prometheus docs (prometheus.io — pull model, PromQL rate() semantics, ServiceMonitor CRD, alerting rules); ArtifactHub kube-prometheus-stack 86.2.3 (artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack — bundled components confirmed); CLAUDE.md Category 4 (Prometheus vs InfluxDB comparison table, PromQL snippets); Juan's CV (OSED: InfluxDB + Grafana + TimescaleDB for edge observability).*
