# FED-02: Byzantine Robustness — Krum, Coordinate-wise Median & Gossip

**For:** Oral rehearsal — speak each section aloud before the interview.
**Purpose:** Explain how a single compromised or faulty substation can poison the global virtual-sensing model, how Krum and coordinate-wise median reject malicious gradient updates, and the gossip-vs-central aggregation tradeoff — so you can defend the choice of aggregation strategy aloud under interview pressure.

---

> **Depth strategy:** Explain-why depth — Krum scoring mechanics, coordinate-wise median robustness, gradient-poisoning detection, and the gossip-vs-central tradeoff are all criteria-named. No secure-aggregation (HE/SMPC) math — that is a separate privacy mechanism, noted but not derived.

## 1. The Byzantine Threat

**Mental model first.** A Byzantine client is one that sends an arbitrary or malicious gradient update — either because it has been compromised, is faulty, or is adversarially controlled. Plain FedAvg averages in the attack: one bad substation can drag the global virtual-sensing model off-target for the entire fleet.

**Grid framing:** A single hacked or malfunctioning K3s substation edge node sends a huge poisoned gradient. FedAvg computes $w_{t+1} = \sum_k \frac{n_k}{n} w_t^k$ — the poisoned update enters the weighted sum directly. Even one client with a large $n_k$ can dominate the aggregate.

**Poisoning mechanic (what an attacker does):**

$$\Delta w_\text{poison} = -\lambda \cdot \Delta w_\text{honest}$$

A sign-flipped, magnitude-amplified update ($\lambda \gg 1$) pushes the global model in the opposite direction of the honest gradient. Alternatively, the attacker sends a direction-of-choice vector in an adversarially chosen direction. Either way, the honest weighted average is corrupted because FedAvg treats all client updates as trustworthy.

**Distinction to keep straight:** Byzantine robustness (rejecting malicious gradients — integrity) is a different concern from secure aggregation (hiding individual gradients from the server — privacy). Both can be used together but address orthogonal threats.

---

## 2. Krum — Select the Update Closest to the Crowd

**Mental model first.** Honest updates cluster near each other in gradient space; a poisoned update is far from the cluster. Krum scores each client by how close its update is to its nearest neighbors — the closest one is selected.

$$S(k) = \sum_{j \in \text{NN}_{n-f-2}(k)} \lVert \Delta w_k - \Delta w_j \rVert^2$$

where $\text{NN}_{n-f-2}(k)$ is the set of the $(n - f - 2)$ **nearest neighbors** of client $k$ in gradient space (the $(n - f - 2)$ most similar updates, excluding client $k$ itself).

**Selection:** $k^* = \arg\min_k S(k)$ — the client whose gradient update is most similar to the majority of other updates.

**Why it works:** Honest clients produce updates that point in roughly the same direction; their pairwise distances are small. A poisoned client's update is far from the cluster, so its sum-of-nearest-neighbor-distances is large — it is never the argmin.

**Multi-Krum variant:** Select the top $m$ clients with the lowest Krum scores, then average their updates. Multi-Krum is less aggressive than vanilla Krum (more throughput of information) while still rejecting the worst outliers.

**Assumptions and complexity:**
- Requires knowing or bounding $f$ (the number of Byzantine clients).
- Requires $n \geq 2f + 3$ clients total.
- Computational complexity: $O(n^2 d)$ where $d$ = model dimension.

### When Krum Fails

**Interview sentence:** "Vanilla Krum selects **one** update — the single client with the minimum Krum score — not an average. Multi-Krum selects $m$ and averages them; be precise about which variant you mean. Additionally, Krum requires a known or bounded $f$; if an attacker can exceed $f$ Byzantine clients, the guarantee breaks."

Be clear: saying "Krum picks the best gradients and averages them" is incorrect for vanilla Krum. The selection is a single argmin.

---

## 3. Coordinate-wise Median

**Mental model first.** Instead of selecting one update, take the median value of each model parameter dimension independently across all client updates.

$$[\Delta w_\text{agg}]_i = \text{median}_k \left( [\Delta w_k]_i \right)$$

For each parameter index $i$ (each dimension of the gradient vector), compute the median across all $K$ clients. The result is a coordinate-wise aggregation where extreme values in any dimension are ignored.

**Why it is robust:** The median is unaffected by extreme outliers. Even if the poisoned client sends $+\infty$ (or $-5\times$ the honest gradient) in dimension $i$, the median of the remaining honest clients is unchanged — as long as fewer than half the clients are Byzantine.

**Byzantine tolerance:** Can tolerate up to $n/2 - 1$ Byzantine clients — a higher fraction than Krum's $n \geq 2f + 3$ requirement.

**Does not require knowing $f$:** Unlike Krum, coordinate-wise median needs no assumption about the number of Byzantine clients.

### Limitation

Coordinate-wise median treats each parameter dimension independently, **ignoring gradient correlations**. A sophisticated attacker can craft an update that is moderate in every individual dimension yet lies in an adversarially chosen direction in the joint parameter space — bypassing coordinate-wise detection while still moving the model in a harmful direction.

**Interview sentence:** "Median for high Byzantine fraction; Krum for higher-dimensional joint robustness. Krum operates on the full gradient vector (nearest-neighbor distance), so it catches attacks that exploit correlations across dimensions. Median ignores correlations; Krum does not — but Krum needs a known $f$ and a larger fleet."

---

## 4. Gossip vs Central Aggregation — Decision Table

<!-- greppable tag: gossip central tradeoff -->

| Dimension | Central Aggregation (FedAvg / Krum) | Gossip (Decentralized) |
|-----------|-------------------------------------|------------------------|
| Single point of failure | Yes — aggregator server is SPOF | No — no aggregation server |
| Communication pattern | Hub-and-spoke (all clients → aggregator) | Peer-to-peer random walks |
| Convergence speed | Faster (synchronized rounds) | Slower (asynchronous, path-dependent) |
| Byzantine handling | Easier — apply Krum / median at one node | Harder — malicious gradient diffuses peer-to-peer before rejection |
| Bandwidth bottleneck | Aggregator can be bottleneck at scale | Distributed — no single bottleneck |
| Operational complexity | Aggregator must be managed / scaled | More complex topology management |
| Grid suitability | WAN uplinks to a fog hub exist (NATS JetStream hub) | Substations may not peer directly |

**Interview one-liner:** "Central aggregation is operationally simpler and lets you apply Krum or coordinate-wise median at one node, but creates a SPOF and bottleneck. Gossip removes the SPOF but makes Byzantine defense harder — a malicious gradient propagates peer-to-peer before anyone can reject it. For a fleet of substations with a NATS JetStream hub already in place, central aggregation with Krum is the natural fit."

---

## 5. → AGMS Connection

> **AGMS / STK-05 fog-tier tie (SHORT):** In the AGMS architecture, GWCH's federated edge transaction manager (Tier 3 in the STK-05 diagram) is exactly where Byzantine-robust aggregation would run. The **simulate-before-commit** gate from Operation Loop (US 12,596,341 B2) and the **Byzantine gradient filter** (Krum / coordinate-wise median) both live at the fog aggregation layer — the entity that receives client updates from substation edge nodes before propagating a new global model. Neither raw sensor data nor unvalidated gradients should pass through untested. Cross-reference: `.planning/phases/04-protocols-stack-architecture/notes/STK-05-reference-architecture.md §5`

---

## <3-min say-aloud version

> "Byzantine robustness is about what happens when one of your substation edge nodes sends a malicious or corrupted gradient update. With plain FedAvg, that one poisoned update enters the weighted average and drags the global model off-target for the whole fleet. **Krum** defends against this by scoring each client's update: $S(k) = \sum_{j \in \text{NN}_{n-f-2}(k)} \lVert \Delta w_k - \Delta w_j \rVert^2$ — sum of squared distances to its nearest neighbors. Honest updates cluster together, so their scores are low. The poisoned update is far from the cluster, so its score is high. Krum selects the **single** update with the minimum score — that's argmin, not an average; Multi-Krum averages a subset. **Coordinate-wise median** takes a different approach: for each parameter dimension independently, take the median across all clients. A poisoned value in dimension $i$ doesn't move the median as long as fewer than half the clients are Byzantine. Median tolerates a higher Byzantine fraction, but it ignores gradient correlations — a sophisticated attacker can construct an attack that is moderate in every dimension but adversarial in the joint space. For a NATS-connected substation fleet, **central aggregation with Krum** is the natural fit: one hub applies the filter before broadcasting the new global model — simpler operations, cleaner Byzantine defense, at the cost of the aggregator being a single point of failure."

---

## → Bridge to your work

> **"In OSED I ran distributed edge inference across DER nodes — no cloud round-trip for local decisions. I haven't built Byzantine-robust federated learning in production, but the upgrade path is concrete: add Krum or coordinate-wise median at the NATS aggregator so one compromised substation node cannot poison the shared virtual-sensing model for the rest of the fleet. The local inference architecture is already there; Byzantine robustness is the next layer."**

Juan's relevant experience maps to the honest delta:
- **OSED distributed edge inference** → already no central coordinator for local decisions; Krum is the Byzantine guard for the weight-aggregation step.
- **MQTT fleet / K8s identity** → already has device-level isolation; Krum at the aggregator is the model-level analog of that isolation.
- **Not claimed:** production Byzantine-robust FL — the framing is "I understand the upgrade, I could implement it."

---

## Quick-Recall Card (Recite Before the Interview)

**Threat:** One Byzantine client sends $\Delta w_\text{poison} = -\lambda \cdot \Delta w_\text{honest}$ — sign-flipped, amplified. FedAvg averages it in. One high-$n_k$ client can dominate the global model.

**Krum:** $S(k) = \sum_{j \in \text{NN}_{n-f-2}(k)} \lVert \Delta w_k - \Delta w_j \rVert^2$; select $k^* = \arg\min_k S(k)$. Vanilla Krum selects **ONE** update; Multi-Krum averages $m$. Requires $n \geq 2f + 3$; complexity $O(n^2 d)$.

**Coordinate-wise median:** $[\Delta w_\text{agg}]_i = \text{median}_k([\Delta w_k]_i)$ for each dimension $i$ independently. Tolerates up to $n/2 - 1$ Byzantine clients. No need to know $f$. Limitation: ignores gradient correlations — sophisticated joint-space attacks evade it.

**Gossip vs central:** Central = simpler, Krum-at-one-node, but SPOF + bottleneck. Gossip = no SPOF, but Byzantine poison diffuses P2P before rejection. For NATS-hub substation fleet → central + Krum.

**Distinction:** Byzantine robustness (integrity — reject malicious gradients) ≠ secure aggregation (privacy — hide gradients from server). Separate mechanisms; can be combined.

---

*Sources: Blanchard et al. 2017 (Krum); Yin et al. 2018 / Aalto-ACM 2024-25 (coordinate-wise median); Hegedüs et al. 2019 (gossip learning); CV (OSED distributed edge inference, MQTT fleet)*
