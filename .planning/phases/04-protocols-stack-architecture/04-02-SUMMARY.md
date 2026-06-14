---
phase: 04-protocols-stack-architecture
plan: "02"
subsystem: edge-stack-observability
tags: [NATS, JetStream, Kafka, MQTT, K3s, Kubernetes, Prometheus, PromQL, kube-prometheus-stack, observability, edge-messaging, interview-prep]
dependency_graph:
  requires: []
  provides: [STK-03, STK-04]
  affects: [STK-05, phase-05-federated, phase-06-synthesis]
tech_stack:
  added: []
  patterns:
    - NATS JetStream over MQTT for federated edge (durable replay, request-reply, JWT, leaf nodes)
    - NATS JetStream over Kafka at substation edge (footprint, not throughput)
    - K3s over full K8s at edge (memory, SQLite-default, air-gap design)
    - kube-prometheus-stack Helm chart (five components pre-wired)
    - PromQL rate() pattern for counter-based CPU metrics
key_files:
  created:
    - .planning/phases/04-protocols-stack-architecture/notes/STK-03-messaging-orchestration.md
    - .planning/phases/04-protocols-stack-architecture/notes/STK-04-observability.md
  modified: []
decisions:
  - "Version framing: use 'current stable' (v2.14.x / v1.33–1.34 / chart 86.2.3) rather than CLAUDE.md stale numbers (2.11 / 1.31)"
  - "Pitfall 3 pre-empt in STK-03: frame Kafka unsuitability as footprint, not throughput"
  - "Pitfall 4 pre-empt in STK-03: K3s 'defaults to SQLite; embedded etcd for HA' not 'no etcd'"
  - "Pitfall 5 pre-empt in STK-04: always name all five kube-prometheus-stack components, not 'Prometheus + Grafana'"
  - "<3-min say-aloud placed at note bottom (D-07: placement at Claude's discretion)"
metrics:
  duration: "~15 min"
  completed: "2026-06-14"
  tasks: 2
  files: 2
---

# Phase 4 Plan 02: Edge Messaging, Orchestration & Observability Study Notes Summary

**One-liner:** Two oral-rehearsal notes — STK-03 justifying NATS JetStream over MQTT (four reasons) and over Kafka (verbatim 64–128 GB RAM quote + bicycle-lane one-liner) plus three K3s-vs-K8s distinctions; STK-04 covering Prometheus pull model, all five kube-prometheus-stack components, and a recitable `rate(container_cpu_usage_seconds_total{namespace="virtual-sensing"}[5m])` PromQL query — both bridged to Juan's OSED MQTT/K8s/InfluxDB experience.

## What Was Built

### STK-03: Edge Messaging & Orchestration

`notes/STK-03-messaging-orchestration.md` covers:

- **Section 1 — Edge constraint mental model:** footprint drives the stack, not throughput; pre-empts "Kafka is slow" pitfall
- **Section 2 — NATS vs MQTT (four reasons):** durable replay for island mode, built-in request-reply, decentralized JWT accounts, leaf-node topology
- **Section 3 — NATS vs Kafka (verbatim quote):** "Kafka servers require a JVM, eight cores, 64 GB to 128 GB of RAM, two or more 8-TB SAS/SSD disks, and a 10-Gig NIC." Contrasted with NATS 20 MB binary on 512 MB RAM. Bicycle-lane interview one-liner. One-line Pulsar awareness only.
- **Section 4 — Three K3s distinctions:** memory (~512 MB vs 2–4 GB), database (SQLite-default/embedded-etcd vs external etcd cluster), air-gap design (single binary <100 MB, Traefik + local-path included)
- **MQTT→NATS and K8s→K3s bridge callouts** with verbatim interview pivot sentences
- **Quick-Recall Card** with all named facts including the Kafka hardware quote and the three K3s distinctions

### STK-04: Observability

`notes/STK-04-observability.md` covers:

- **Section 1 — Pull vs push mental model:** full comparison table (Prometheus vs InfluxDB across 6 dimensions); pull-model key implication (ServiceMonitor CRD, pod IPs change, Prometheus finds them)
- **Section 2 — kube-prometheus-stack (the named gap):** all five bundled components with roles — Prometheus Operator, node-exporter, kube-state-metrics, Grafana, Alertmanager — plus verbatim interview sentence
- **Section 3 — Recitable PromQL query:** `rate(container_cpu_usage_seconds_total{namespace="virtual-sensing"}[5m])` with explanation; three awareness queries; PromQL building-blocks table
- **Section 4 — Architecture placement:** Prometheus at both edge and cloud; Grafana centralized
- **InfluxDB+Grafana→Prometheus/PromQL bridge** with comparison table and interview pivot
- **Quick-Recall Card** with all five component names and the recitable query

## Deviations from Plan

None — plan executed exactly as written. All four numbered sections per note were covered; both notes follow the TVS-04 style exactly (For:/Purpose: header, numbered sections, <3-min say-aloud, boxed bridge callout, Quick-Recall Card, Sources line). Version corrections applied as directed (CLAUDE.md stale numbers not propagated; "current stable" framing used with verified numbers in parentheses).

## Known Stubs

None — both notes are complete reference/rehearsal documents. No data sources, mock data, or placeholder content.

## Threat Flags

None — documentation-only plan producing static markdown study notes. No runtime, network, or data-handling surface introduced.

## Self-Check: PASSED

- `STK-03-messaging-orchestration.md` exists and contains all required tokens (JetStream, MQTT, Kafka, 64, K3s, SQLite, air-gap, Bridge to your work, 3-min/say-aloud): FOUND
- `STK-04-observability.md` exists and contains all required tokens (kube-prometheus-stack, rate(container_cpu_usage_seconds_total, node-exporter, kube-state-metrics, Alertmanager, Operator, InfluxDB, Bridge to your work, 3-min/say-aloud): FOUND
- Task 1 commit 3dde10c: FOUND
- Task 2 commit 15975ed: FOUND
