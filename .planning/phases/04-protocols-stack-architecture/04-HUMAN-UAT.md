---
status: partial
phase: 04-protocols-stack-architecture
source: [04-VERIFICATION.md]
started: 2026-06-14
updated: 2026-06-14
---

## Current Test

[awaiting human testing — oral rehearsal by Juan]

## Tests

### 1. STK-01 protocol tier walk
expected: Juan names each protocol (SCADA, DNP3, PMU/C37.118, IEC 61850, LoRa, MQTT) and its one key property from memory, in the correct field-to-cloud tier, plus the two bridge sentences (Modbus→DNP3, Zigbee→LoRa).
result: [pending]

### 2. STK-02 logical-node cold recall
expected: Asked cold "name three IEC 61850 logical nodes," Juan gives ≥3 of XCBR/MMXU/CSWI/PTOC/PDIS with a one-line role each, and states the GOOSE/SV/MMS split — without notes (criterion 2).
result: [pending]

### 3. STK-03 stack-justification recitation
expected: Juan justifies NATS JetStream vs MQTT vs Kafka for the substation edge (incl. the Kafka hardware quote / bicycle-lane one-liner) and the three K3s-vs-K8s distinctions (air-gap, memory, etcd/SQLite) without prompting.
result: [pending]

### 4. STK-05 whiteboard draw-and-narrate
expected: On paper/whiteboard, Juan draws the four-tier architecture (field→edge→fog/federated→cloud) in ~90 seconds and narrates it in ~3 minutes, including control-latency tiers per layer and the AGMS patent overlay as the closing power move.
result: [pending]

## Summary

total: 4
passed: 0
issues: 0
pending: 4
skipped: 0
blocked: 0

## Gaps
