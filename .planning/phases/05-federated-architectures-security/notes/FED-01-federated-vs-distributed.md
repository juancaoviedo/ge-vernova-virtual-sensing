# FED-01: Federated vs Distributed — FedAvg, FedProx & Non-IID

**For:** Oral rehearsal — speak each section aloud before the interview.
**Purpose:** Precisely distinguish federated from distributed learning (the "no central coordinator" constraint), recite the FedAvg weighted-average aggregation rule and the FedProx proximal term, explain why non-IID substation load profiles cause client drift — and tie each to Juan's closest real work.

---

> **Depth strategy:** FULL/explain-why depth throughout — federated-vs-distributed distinction, FedAvg update rule, FedProx proximal term, and non-IID client drift are all criteria-named and interviewer-probed. No convergence-proof math (that ceiling is awareness-only per D-05).

## 1. Federated ≠ Distributed — The Crisp Distinction

**The one-liner:** "Distributed splits computation across workers with a coordinator owning all the data; federated has **no central coordinator owning the data** — each client trains locally and only **weights/gradients leave**, never raw training data."

| Property | Distributed (classic) | Federated |
|----------|-----------------------|-----------|
| Data location | Central store; workers fetch shards | Data stays permanently at each client |
| Coordinator role | Splits data, assigns work, knows everything | Aggregates updates; never sees raw data |
| What moves on the wire | Data shards | Model weights / gradient updates only |
| Privacy model | Trust the coordinator | Coordinator learns nothing about raw data |

**Common gotcha:** "Isn't Spark/MapReduce also federated?" — No. Spark splits a central dataset across workers; the driver owns the data. Federated learning starts from the premise that data **cannot** leave its origination point (regulatory, privacy, or operational reason).

**Grid grounding (concrete):** Each substation has a different load profile — industrial vs. residential feeders, different DER penetration, different climate zone — so their training data are inherently heterogeneous (non-IID). Sending raw PMU readings or load telemetry to a central server would expose commercially sensitive and security-critical operational data. Federated learning lets each substation train a local model and share only the weight delta.

---

## 2. FedAvg — Weighted-Average Aggregation

**Mental model first.** Each client runs several local SGD epochs on its own data, then the server averages their resulting models weighted by each client's sample count.

$$w_{t+1} = \sum_{k=1}^{K} \frac{n_k}{n} \, w_t^k$$

### Term-by-term

| Term | Name | Meaning |
|------|------|---------|
| $w_{t+1}$ | New global model | Weighted-average aggregate sent back to all clients for round $t+1$ |
| $n_k$ | Client $k$ sample count | Number of local training samples at client $k$ |
| $n$ | Total samples | $n = \sum_k n_k$; normalizes the weights to sum to 1 |
| $w_t^k$ | Client $k$ local model | Model at client $k$ after $E$ local SGD epochs from the global model $w_t$ |
| $K$ | Number of clients | Total clients participating in this round |

**The two-nested-loop structure:**

```
For each communication round t = 1, 2, ..., T:
    1. Server broadcasts w_t to sampled subset of clients
    2. Each sampled client k:
       a. Initialize local model from w_t
       b. Run E local SGD epochs on its own data D_k  →  produces w_t^k
       c. Send w_t^k (or delta w_t^k − w_t) back to server
    3. Server computes weighted average  →  w_{t+1}
```

**Why it is communication-efficient:** Clients do $E > 1$ local epochs per round (not just one gradient step). More local epochs = fewer communication rounds needed. But more local epochs also *increase client drift* under non-IID data — the FedProx motivation.

---

## 3. FedProx — The Fix for Non-IID Client Drift

**The one-liner:** FedProx = FedAvg + a proximal term in the *client's local objective* that penalizes drift from the global model.

Each client $k$ minimizes this modified objective instead of pure $F_k(w)$:

$$\min_{w} \; F_k(w) \;+\; \frac{\mu}{2}\lVert w - w_t \rVert^2$$

**What the proximal term does:**

- $\mu = 0$: reduces exactly to FedAvg — no proximal constraint.
- Small $\mu$ (e.g., 0.01): gentle anchor; clients still converge close to their local optimum.
- Large $\mu$ (e.g., 1.0): client barely moves from $w_t$ — underfits local data.
- Typical $\mu \in [0.01, 1.0]$ in practice; $\mu = 0.5$ is a common starting point for legible contrast.

**CRITICAL — where the proximal term lives:** The proximal term is in the **client's local optimization objective, NOT the server aggregation step.** Each client minimizes $F_k(w) + \frac{\mu}{2}\lVert w - w_t \rVert^2$ locally before sending anything to the server. The server's aggregation step ($w_{t+1} = \sum_k \frac{n_k}{n} w_t^k$) is identical to FedAvg. Misplacing this term on the aggregation step is a common pitfall.

**Non-IID substation framing:**

> "Every substation is non-IID by definition: feeder 1 is predominantly residential with evening peak, feeder 2 is industrial with daytime flat load, feeder 3 has 40% solar DER with midday export. Naive FedAvg over many local epochs lets each substation's model drift toward its own feeder's optimum; the weighted average then fails the substations with atypical load shapes. FedProx's proximal term forces each local update to stay within a trust region around the global model, so the aggregated result generalizes across the fleet."

---

## 4. → STK-05 / AGMS Connection

> **STK-05 loop:** The non-IID / FedProx material is the algorithm-depth behind the **STK-05 "fog/federated" tier** — Phase 4 named it; Phase 5 owns its depth. In that four-tier diagram, the fog/federated aggregator is the entity that receives $w_t^k$ updates from substation K3s edge nodes, runs FedAvg (or FedProx-constrained), and broadcasts $w_{t+1}$ back. Cross-reference: `.planning/phases/04-protocols-stack-architecture/notes/STK-05-reference-architecture.md`

> **AGMS tie:** Two AGMS patent analogs apply here. (a) **Scout Command** (US 12,596,341) — deploying scouts to FADs is *federated decisioning*: each FAD operates autonomously (island mode), sharing status commands via NATS, not raw sensor data. Each FAD is a "federated client" making local decisions; GWCH aggregates their status. (b) **Operation Loop** simulate-before-commit (US 12,596,341 B2 claim 3) — propose a formation, simulate the operation loop, *then* commit — the same "compute before acting" principle that makes FedProx safe to deploy: each local update is bounded before it enters the global average. Cross-reference: `.planning/research/patents/operation-loop.md`

---

## <3-min say-aloud version

> "Federated learning is not the same as distributed computing. In distributed, a coordinator owns all the data and ships shards to workers. In federated, there is **no central coordinator owning the data** — each substation trains locally on its own load telemetry, and only the weight delta leaves the node, never the raw PMU readings. The server aggregates those weights: $w_{t+1} = \sum_k \frac{n_k}{n} w_t^k$ — that's **FedAvg**, a weighted average by sample count. Now, substations are **non-IID by definition** — residential feeders, industrial feeders, high-DER feeders each have completely different load profiles. So if you run many local SGD epochs, each substation's model drifts toward its own local optimum, and averaging drifted models gives you a global model that fails everyone with an atypical load shape. That's **client drift**. **FedProx** fixes it by adding a proximal term, $+\frac{\mu}{2}\lVert w - w_t \rVert^2$, to the *client's* local objective — it penalizes the local model for straying too far from the global model $w_t$. The server's aggregation step is unchanged. $\mu = 0$ collapses back to FedAvg; larger $\mu$ keeps clients tethered to the global model at the cost of local fit. The result: the aggregated model generalizes across the whole substation fleet instead of being pulled toward the biggest or most extreme feeder."

---

## → Bridge to your work

> **"In OSED I ran distributed edge inference across DER nodes — no cloud round-trip for local decisions. I haven't run federated *learning* in production, but that's the natural next step: keep the local inference, add FedAvg so the fleet improves a shared model without ever shipping raw telemetry — and Krum so one bad node can't poison it."**

| Federated learning concept | Juan's CV analog (OSED / DER work) |
|----------------------------|------------------------------------|
| No central coordinator owns data | OSED: DER edge nodes make local control decisions without cloud round-trip |
| Weights/gradients leave, never raw data | MQTT telemetry fleet: aggregated metrics, not raw sensor dumps, flow to the platform |
| FedAvg global model | The "shared model" upgrade: fleet improves one virtual-sensing model without raw data movement |
| Non-IID substations | Heterogeneous DER sites (rooftop solar, BESS, EV charging) — already known to behave differently |
| K8s / K3s orchestration | Juan's K8s background → K3s substation edge nodes as FL clients |

Honest about the gap, but demonstrates the delta is concrete and implementable.

---

## Quick-Recall Card (Recite Before the Interview)

- **Federated vs distributed:** Distributed = coordinator owns data, ships shards. Federated = **no central coordinator owns data**, only weights/gradients leave each client. Spark/MapReduce is distributed, not federated.
- **FedAvg:** $w_{t+1} = \sum_{k=1}^{K} \frac{n_k}{n} w_t^k$ — weighted average by sample count. Clients run $E$ local epochs; server averages. Communication-efficient; fails under non-IID.
- **FedProx:** $+\frac{\mu}{2}\lVert w - w_t\rVert^2$ in the **client's local objective** (NOT server aggregation). $\mu = 0$ → FedAvg; larger $\mu$ → tighter anchor to global model.
- **Non-IID:** Different feeders/climates/DER mixes → each client drifts toward its local optimum under many local epochs → weighted average of drifted models fails atypical clients. FedProx is the standard treatment.
- **Grid grounding:** Substations are non-IID by definition (Ghosh & Mittal 2025 confirms on real substation equipment). Raw PMU data must not leave → federated is the correct architecture.

---

*Sources: McMahan et al. 2017 (FedAvg); Li et al. 2020 (FedProx); Ghosh & Mittal, Frontiers AI 2025 (substation non-IID); CV (OSED distributed edge inference)*
