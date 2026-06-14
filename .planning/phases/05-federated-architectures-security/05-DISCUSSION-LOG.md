# Phase 5: Federated Architectures & Security - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-14
**Phase:** 5-Federated Architectures & Security
**Areas discussed:** Demo vs notes-only, Note file split, Depth calibration, Grid grounding & bridge

---

## Demo vs notes-only

| Option | Description | Selected |
|--------|-------------|----------|
| Tiny demo | ~50-line NumPy sim: non-IID FedAvg, FedProx damping drift, Krum/median rejecting poison | ✓ |
| Notes-only (like Phase 4) | Conversational only; save time for Byzantine/security depth | |
| Pseudo-code in notes | No runnable demo; embed FedAvg/FedProx/Krum pseudo-code blocks | |

**User's choice:** Tiny demo
**Notes:** FedAvg/FedProx/Krum are genuinely algorithmic (unlike Phase 4 protocols); a demo earns "I've actually run this" credibility on the differentiator gap and reuses Phase 1/2 demo muscle.

### Demo scope (follow-up)

| Option | Description | Selected |
|--------|-------------|----------|
| All three, one script | non-IID → FedAvg converges → FedProx reduces drift → poison injected → Krum/median rejects; before/after table | ✓ |
| FedAvg/FedProx only | Aggregation + non-IID drift (FED-01); Byzantine as notes only | |
| Krum/poisoning only | Just the poison-rejection punchline; FedAvg/FedProx as notes | |

**User's choice:** All three, one script
**Notes:** Single runnable artifact covers FED-01 + FED-02a; FED-03 edge security stays notes-only (not NumPy-demo-able).

---

## Note file split

| Option | Description | Selected |
|--------|-------------|----------|
| 3 notes | FED-01-federated-vs-distributed, FED-02-byzantine-robustness, FED-03-edge-security (split FED-02's two clusters) | ✓ |
| 2 notes (per-requirement) | FED-01 + FED-02 matching IDs; FED-02 carries both Byzantine + security | |

**User's choice:** 3 notes
**Notes:** FED-02 bundles two unrelated topic clusters; topic coherence beats strict ID-matching. Note count > requirement count accepted.

---

## Depth calibration

| Option | Description | Selected |
|--------|-------------|----------|
| Tiered: deep FL, aware security | Explain-why on FedAvg/FedProx/non-IID + Byzantine; awareness on OTA/TPM/SPIFFE (name + grid threat) | ✓ |
| Uniform depth | Equal explain-why depth incl. PKI/attestation internals | |

**User's choice:** Tiered: deep FL, aware security
**Notes:** Edge-security criterion only asks to "describe + connect to a grid threat" — no SPIRE config / TPM internals. Aligns with CLAUDE.md "What NOT to Over-Invest In."

---

## Grid grounding & bridge

### Bridge framing (FL is a genuine gap)

| Option | Description | Selected |
|--------|-------------|----------|
| Honest gap + upgrade path | "Closest thing I've built + the upgrade I'd make"; honest that FL wasn't run in production | ✓ |
| Claim adjacency | Frame edge/distributed work as effectively federated already | |
| Minimal bridges | Keep bridges short/generic; lean on the demo for credibility | |

**User's choice:** Honest gap + upgrade path
**Notes:** Juan has edge/distributed/MQTT/K8s/OTA but no production federated learning. Honest framing shows he grasps the delta and could implement it; "claim adjacency" rejected as risky if probed on the differentiator topic.

### STK-05 / AGMS grounding

| Option | Description | Selected |
|--------|-------------|----------|
| Close the loop, lightly | Anchor non-IID to substation load profiles; short callout that this is STK-05's fog/federated depth; brief AGMS tie | ✓ |
| Generic FL, no cross-links | Teach concepts standalone, no STK-05/AGMS wiring | |
| Heavy patent integration | Substantial AGMS-federated overlay per patent | |

**User's choice:** Close the loop, lightly
**Notes:** Cross-reference Phase 3/4, don't re-derive. Closes the STK-05 "fog/federated" tier Phase 4 deferred; brief Operation Loop / Scout Command tie as a low-cost differentiation power-move.

---

## Claude's Discretion

- Exact filenames/slugs within `notes/` and `demo/`; section ordering and placement of the "<3-min say-aloud" track.
- The non-IID toy dataset, client count, FedProx μ, and poison magnitude for a legible before/after contrast.
- Whether the demo shows coordinate-wise median, Krum, or both (at least one named).
- Which specific concrete grid threats pair with OTA / TPM / SPIFFE.
- How richly the AGMS overlay cross-links to the Phase 3 deck (kept short either way).

## Deferred Ideas

- Aggregate vocabulary-bridge table (BRG-01..03) — Phase 6.
- System-design drills ("500-node pipeline", federated aggregator) + timed Q&A / mock interview (QNA-01..03) — Phase 6.
- Framework-level FL depth (Flower/PySyft API, SCAFFOLD/FedNova, secure aggregation HE/SMPC, full SPIRE config, TPM internals) — declined (D-05 ceiling).
- A demo using a real FL framework (Flower) — declined; NumPy from-scratch keeps focus on the aggregation math.
