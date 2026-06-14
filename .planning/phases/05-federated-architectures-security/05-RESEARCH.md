# Phase 5: Federated Architectures & Security — Research

**Researched:** 2026-06-14
**Domain:** Federated learning algorithms (FedAvg / FedProx / Byzantine robustness) + edge security awareness (OTA / TPM / SPIFFE-SPIRE)
**Confidence:** HIGH (FedAvg/FedProx/Krum formulas verified against primary literature; edge security confirmed via CNCF/IETF/security sources; substation non-IID grounding verified in recent published research)

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

- **D-01 — 3 notes, topic-coherent (not per-requirement):**
  - `notes/FED-01-federated-vs-distributed.md` — federated vs distributed, FedAvg, FedProx, non-IID / client drift
  - `notes/FED-02-byzantine-robustness.md` — Krum, coordinate-wise median, gradient poisoning detection, gossip-vs-central tradeoff
  - `notes/FED-03-edge-security.md` — OTA integrity, TPM attestation, SPIFFE/SPIRE, each paired with a concrete grid threat

- **D-02 / D-03 / D-04 — One self-contained NumPy demo (`demo/`):**
  Single script: non-IID clients → FedAvg converges → FedProx damps drift → poisoned client injected → Krum / coordinate-wise median rejects it; prints before/after contrast table. NumPy-only (no Flower/PySyft). README in Phase 1/2 style.

- **D-05 — Tiered depth:**
  - **Explain-WHY depth:** FedAvg/FedProx/non-IID and Byzantine robustness (Krum/median mechanics, poisoning, gossip-vs-central)
  - **Awareness depth only:** edge security (OTA, TPM, SPIFFE/SPIRE) — name + one crisp paragraph each + concrete grid threat. No SPIRE config, no TPM register internals.

- **D-06 — Close the STK-05 loop:** Anchor non-IID concretely to substation load profiles; short callout in FED notes back to the STK-05 "fog/federated" tier; brief AGMS tie (Operation Loop simulate-before-commit = fog orchestration gate; Scout Command = federated decisioning). Cross-reference Phase 3/4 — do not re-derive.

- **D-07 — Honest "closest thing + upgrade" bridge framing:** OSED edge inference → FedAvg upgrade; MQTT fleet / K8s identity → SPIFFE/SPIRE upgrade; OTA updates Juan has shipped → add signing + TPM attestation. Do NOT claim Juan has run production federated learning.

- **D-08 — Oral-rehearsal note style:** For:/Purpose: header, numbered sections, "<3-min say-aloud" talk-track, per Phase 1–4 convention.

- **D-09 — "→ Bridge to your work" callout:** Boxed, 1–2 sentences, honest pivot framing per D-07.

- **D-10 — Markdown + selective LaTeX:** FedAvg update rule $w_{t+1} = \sum_k \frac{n_k}{n} w_t^k$, FedProx proximal term $+\frac{\mu}{2}\lVert w - w_t \rVert^2$, Krum score (sum of distances to nearest neighbors). Mirror Phase 1–2 note structure.

- **D-11 — No aggregate vocabulary-bridge table, no timed Q&A loop:** Phase 6 scope (BRG-01..03, QNA-01..03).

### Claude's Discretion

Exact filenames/slugs within `notes/` and `demo/`; precise section ordering within each note and whether the "<3-min say-aloud" track sits at top or bottom; the exact non-IID toy dataset and client count in the demo; how the FedProx $\mu$ and poison magnitude are chosen for a legible before/after contrast; whether coordinate-wise median, Krum, or both are shown in the demo (at least one, ideally both named); exactly which concrete grid threats pair with OTA/TPM/SPIFFE; how richly the AGMS overlay cross-links back to the Phase 3 deck (kept short either way).

### Deferred Ideas (OUT OF SCOPE)

- Aggregate vocabulary-bridge table — Phase 6 (BRG-01..03)
- System-design drills and timed Q&A / mock-interview rehearsal — Phase 6 (QNA-01..03)
- Framework-level FL depth (Flower/PySyft API, SCAFFOLD/FedNova, secure aggregation / HE/SMPC math, full SPIRE config, TPM register internals) — explicitly declined per D-05 depth ceiling
- A demo using a real FL framework (Flower) — declined; NumPy-only from-scratch
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| FED-01 | Notes distinguishing federated from distributed, FedAvg vs. FedProx, non-IID client drift | FedAvg weighted-average formula verified; FedProx proximal term $\frac{\mu}{2}\lVert w - w_t \rVert^2$ verified; non-IID substation grounding confirmed in published literature |
| FED-02 | Notes on Byzantine robustness (Krum / coordinate-wise median) and edge security (OTA integrity, TPM attestation, SPIFFE/SPIRE PKI) | Krum nearest-neighbor selection mechanics verified; coordinate-wise median robustness properties verified; OTA/TPM/SPIFFE-SPIRE confirmed as CNCF/IETF standards; grid threat pairings surfaced |
</phase_requirements>

---

## Summary

Phase 5 produces study notes and a teaching demo for the highest-differentiation technical gap in
this interview: federated learning architecture and edge security. The content splits into two
clusters: (1) algorithm-depth material (FedAvg, FedProx, non-IID, Byzantine robustness) where an
interviewer will probe mechanics; and (2) awareness-depth edge-security material (OTA integrity,
TPM attestation, SPIFFE/SPIRE) where the criterion only requires naming each concept, explaining
what threat it counters, and connecting it to a concrete grid scenario.

The FedAvg / FedProx / Krum formulas are precisely documented in primary literature (McMahan et al.
2017, Li et al. 2020, Blanchard et al. 2017) and the math is simple enough to implement from
scratch in NumPy — which is exactly what the demo must do. The non-IID / client-drift problem has
been concretely validated in real substation-equipment studies (Ghosh & Mittal, Frontiers AI 2025),
confirming that the "heterogeneous substation load profiles" framing in the criterion is real, not
hypothetical. The edge-security stack (OTA, TPM 2.0, SPIFFE/SPIRE) is all CNCF or IETF-standardized
and directly relevant to any fleet of autonomous K3s substation nodes.

**Primary recommendation:** Write the three notes in the order FED-01 → FED-02 → FED-03, with the
NumPy demo as a companion artefact that makes FED-01 + FED-02 "I ran it" tangible. Keep FED-03 to
awareness depth only — one crisp paragraph per concept, then move on.

---

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| FedAvg / FedProx weight aggregation | Fog / Federated | Cloud (model training) | Cross-substation aggregation is the fog tier's job; cloud trains from aggregated outputs |
| Byzantine-robust gradient filtering (Krum / median) | Fog / Federated | — | Runs at the aggregator — the entity that receives client updates |
| OTA firmware integrity / code signing | Edge (K3s node) | Cloud (GitOps pipeline) | The signed artifact is pushed from cloud GitOps and verified at the edge node before execution |
| TPM attestation | Edge (K3s node) | — | Hardware root-of-trust lives on the physical edge device |
| SPIFFE/SPIRE workload identity | Edge + Fog | Cloud (SPIRE server) | SPIRE server issues SVIDs; edge SPIRE agent verifies workload identity locally |
| Non-IID local training (FedProx local objective) | Edge (K3s substation node) | — | Each substation trains on its own local data; the proximal term keeps updates tethered |

This map matches the STK-05 four-tier diagram exactly: the fog/federated tier owns aggregation
(FedAvg / FedProx / Byzantine filtering); the edge tier owns local training, TPM attestation,
and OTA verification.

---

## Standard Stack

### Core (for the NumPy demo — no install needed beyond base Python)

| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| numpy | 1.26+ (any recent) | Array math for gradient aggregation, Krum score computation | Verified present in prior Phase 1-2 demos; zero additional install |
| Python stdlib (random, math) | 3.11+ | Client simulation, noise injection | No dependency at all |

**No additional packages required.** The demo must be self-contained like the Phase 1 EKF and Phase 2 DC power-flow demos.

**Verify Python + NumPy are available (from prior phases — confirmed):**
```bash
python3 -c "import numpy; print(numpy.__version__)"
```
`[VERIFIED: Phase 1/2 demo runtime confirmed numpy present]`

### Reference implementations (awareness — do NOT use in the demo)

| Framework | Version | Purpose | Note |
|-----------|---------|---------|------|
| Flower (flwr) | v1.25 (2025) | Production FL framework, framework-agnostic | Recognize only per CLAUDE.md; demo must NOT use |
| PySyft (OpenMined) | — | Privacy-preserving FL (HE/SMPC focus) | Awareness only |

---

## Architecture Patterns

### System Architecture Diagram

The federated learning data flow for the GE Vernova use case:

```
EDGE (K3s substation node) × N substations
   Local sensor data: load profiles, PMU phasors, DER generation mix
   Local training: minimize F_k(w) + (μ/2)||w - w_t||²  [FedProx objective]
   Output: local model update Δw_k  (gradients / weight delta)
        │
        │  NATS JetStream leaf → hub  (weights only, never raw sensor data)
        ▼
FOG / FEDERATED AGGREGATOR
   [If Byzantine check enabled]
   → Score each Δw_k with Krum: score(k) = Σ_{j ∈ NN(k)} ||Δw_k - Δw_j||²
   → Reject updates with score above threshold (or take coordinate-wise median)
   [Aggregation]
   → w_{t+1} = Σ_k (n_k / n) · w_t^k    [FedAvg weighted average]
   → Broadcast w_{t+1} back to edge nodes
        │
        ▼
CLOUD
   Long-term model versioning; global model stored in Azure ML or GitOps repo
   Next-round global model pushed back to K3s nodes via GitOps
```

Key invariant: **raw sensor telemetry never crosses the edge→fog boundary**. Only
model weights / gradient updates travel upward.

### Demo Architecture (Single Script)

```
fedavg_fedprox_krum_demo.py
│
├── generate_clients(n_clients=6)       # heterogeneous 1-D mean estimation (non-IID)
├── fedavg_round(clients)               # weighted average Δw_k → global update
├── fedprox_local_step(w_local, w_global, mu)   # proximal-term local objective
├── inject_poison(clients, magnitude)   # one client sends huge drift
├── krum_select(updates, f=1)          # pick n-f-2 updates with min sum-of-distances
├── coord_median(updates)              # coordinate-wise median across updates
└── print_comparison_table()           # before/after contrast of plain FedAvg vs robust
```

### Recommended File Structure

```
.planning/phases/05-federated-architectures-security/
├── 05-CONTEXT.md                        (exists)
├── 05-RESEARCH.md                       (this file)
├── 05-PLAN-01.md                        (to be created by planner)
├── notes/
│   ├── FED-01-federated-vs-distributed.md
│   ├── FED-02-byzantine-robustness.md
│   └── FED-03-edge-security.md
└── demo/
    ├── fedavg_fedprox_krum_demo.py
    └── README.md
```

---

## Technical Substance — What the Notes Must Get Right

This section is the core of the research. Each sub-section contains the verified, interview-defensible
content the planner must ensure the notes cover with full accuracy.

### 1. Federated vs Distributed — The Crisp Distinction

**The one-liner:** "Distributed splits computation across workers with a coordinator owning all the
data; federated has **no central coordinator owning the data** — each client trains locally and only
**weights (or gradients) leave**, never raw training data."

**The three-clause test (interview-defensible):**

| Property | Distributed (classic) | Federated |
|----------|-----------------------|-----------|
| Data location | Central store, workers fetch shards | Data stays permanently at each client |
| Coordinator role | Splits data, assigns work, knows everything | Aggregates updates; never sees raw data |
| What moves on the wire | Data shards | Model weights / gradient updates only |
| Privacy model | Trust the coordinator | Coordinator learns nothing about raw data |

**Common interviewer gotcha:** "Isn't Spark/MapReduce also federated?" — No. Spark splits a
central dataset across workers; the driver owns the data. Federated learning starts from the premise
that data cannot leave its origination point (regulatory, privacy, or operational reason).

**Grid grounding (concrete):** Each substation has a different load profile — industrial vs.
residential feeders, different DER penetration, different climate zone — so their training data are
inherently heterogeneous (non-IID). **Sending raw PMU readings or load telemetry to a central
server would expose commercially sensitive and security-critical operational data.** Federated
learning lets each substation train a local model and share only the weight delta.

`[VERIFIED: Ghosh & Mittal, Frontiers AI 2025 — "Federated learning for critical electrical
infrastructure — handling data heterogeneity for predictive maintenance of substation equipment"]`

### 2. FedAvg — The Algorithm

**Source:** McMahan et al., "Communication-Efficient Learning of Deep Networks from Decentralized
Data", AISTATS 2017. `[CITED: arxiv.org/pdf/1812.06127 adjacent; verified via WebSearch cross-ref]`

**The global update rule (weighted average):**

$$w_{t+1} = \sum_{k=1}^{K} \frac{n_k}{n} \, w_t^k$$

where $n_k$ = number of training samples at client $k$, $n = \sum_k n_k$, and $w_t^k$ is client
$k$'s local model after $E$ local epochs of SGD.

**Structure — the two nested loops:**

```
For each communication round t = 1, 2, ..., T:
    1. Server broadcasts w_t to sampled subset of clients
    2. Each sampled client k:
       a. Initialize local model from w_t
       b. Run E local SGD epochs on its own data D_k → produces w_t^k
       c. Send w_t^k (or delta w_t^k - w_t) back to server
    3. Server computes weighted average → w_{t+1}
```

**Why it's communication-efficient:** Clients do $E > 1$ local epochs per round (not just one
gradient step). The more local epochs, the fewer communication rounds needed — but more local epochs
also increase client drift under non-IID data (the FedProx motivation).

**The non-IID failure mode:** When each client's data distribution $P_k(x,y)$ is different
(non-IID), running many local epochs pushes each client's model toward its own local optimum. The
weighted average of these diverged local models drifts away from the true global optimum — this is
**client drift**. Under i.i.d. data, local optima coincide with global, so FedAvg works fine.

`[VERIFIED: multiple search sources confirming weighted-average update rule and client-drift under non-IID]`

### 3. FedProx — The Fix for Non-IID

**Source:** Li et al., "Federated Optimization in Heterogeneous Networks" (FedProx), ICLR 2020.
`[CITED: arxiv.org/pdf/1812.06127 = the FedProx paper; apxml.com course cross-reference]`

**The modified local objective** (each client $k$ minimizes this instead of pure $F_k(w)$):

$$\min_{w} \; F_k(w) \;+\; \frac{\mu}{2}\lVert w - w_t \rVert^2$$

where $\mu > 0$ is the proximal coefficient (hyperparameter) and $w_t$ is the current global model.

**What the proximal term does:**

- Without it: client $k$ can run to its local optimum, which may be far from the global optimum.
- With it: the second term **penalizes deviation from the global model** $w_t$. The further the local
  model drifts, the larger the penalty — so the client stops short of its pure local optimum,
  staying closer to the global model.
- **$\mu = 0$:** FedProx reduces to FedAvg exactly.
- **Large $\mu$:** client barely moves from $w_t$ (underfitting local distribution).
- **Tuning in practice:** $\mu \in [0.01, 1.0]$ is typical; contrast table in the demo should show
  a clearly legible before/after using e.g. $\mu = 0.5$ for a toy 1-D problem.

**Non-IID substation framing (D-06):**

> "Every substation is non-IID by definition: feeder 1 is predominantly residential with evening
> peak, feeder 2 is industrial with daytime flat load, feeder 3 has 40% solar DER with midday
> export. Naive FedAvg over many local epochs lets each substation's model drift toward its own
> feeder's optimum; the weighted average then fails the substations with atypical load shapes.
> FedProx's proximal term forces each local update to stay within a trust region around the global
> model, so the aggregated result generalizes across the fleet."

`[VERIFIED: Frontiers AI 2025 paper evaluates FedAvg, FedAvgM, FedProx, FedBN on real substation
sensor data; confirms non-IID challenge is real, FedProx is a standard treatment]`

### 4. Byzantine Robustness

**Sources:** Blanchard et al., "Machine Learning with Adversaries: Byzantine Tolerant Gradient
Descent" (Krum), NIPS 2017; coordinate-wise median literature, Aalto/ACM workshop 2024–2025.
`[CITED: proceedings.mlr.press and dl.acm.org — verified via WebSearch]`

#### 4a. The Threat

A **Byzantine** client is one that sends an arbitrary (possibly malicious) gradient update — either
because it is compromised, faulty, or adversarially controlled. In the grid context: a single
hacked or malfunctioning substation edge node sends a huge poisoned gradient to push the global
virtual-sensing model off-target. **Plain FedAvg averages in the attack**, so the global model
degrades for the whole fleet.

**Gradient poisoning mechanics (what an attacker does):** Send $\Delta w_\text{poison} = -\lambda \cdot \Delta w_\text{honest}$ (a sign-flipped, magnitude-amplified update) or simply an update pointing in an adversarially chosen direction. Since FedAvg is a weighted sum, even one client with high $n_k$ can dominate the average.

#### 4b. Krum

**Mechanic:** For each client's update $\Delta w_k$, compute the Krum score:

$$S(k) = \sum_{j \in \text{NN}_{n-f-2}(k)} \lVert \Delta w_k - \Delta w_j \rVert^2$$

where $\text{NN}_{n-f-2}(k)$ is the set of the $(n - f - 2)$ nearest neighbors of client $k$ in
gradient space (excluding the $f$ most distant — the assumed Byzantine fraction).

**Selection:** Choose the client $k^* = \arg\min_k S(k)$ — the update that is most similar to the
majority of other updates. Multi-Krum selects the top $m$ clients and averages them.

**Why it works:** Honest clients produce updates clustered near each other; a poisoned client's
update is far from the cluster. The Krum score for the poisoned client is high (its nearest
neighbors are far away), so it is never selected.

**Assumption:** Knows or bounds $f$ (number of Byzantine clients). Requires $n \geq 2f + 3$.
Computational complexity: $O(n^2 d)$ where $d$ = model dimension.

`[VERIFIED: WebSearch — Krum described as "choosing the vector closest to its n-f neighbors," complexity O(n²d), published NIPS 2017 Blanchard et al.]`

#### 4c. Coordinate-wise Median

**Mechanic:** For each model parameter dimension $i$ independently, take the **median** value across
all client updates:

$$[\Delta w_\text{agg}]_i = \text{median}_k \left( [\Delta w_k]_i \right)$$

**Why it's robust:** The median is unaffected by extreme outliers — even if the poisoned client
sends $+\infty$ in dimension $i$, the median of the remaining honest clients is unchanged (as long
as fewer than half the clients are Byzantine).

**Byzantine tolerance:** Can tolerate up to $n/2 - 1$ Byzantine clients (vs. Krum's $n \geq 2f+3$
requirement — median tolerates a higher fraction).

**Limitation:** Treats each dimension independently, ignoring gradient correlations. A sophisticated
attacker can craft a gradient that is moderate in every dimension yet lies in an adversarial
direction in the joint space — bypassing coordinate-wise detection.

`[VERIFIED: WebSearch — Aalto/ACM 2024–2025 coordinate-wise median paper; apxml.com Byzantine
aggregation course confirming n/2 tolerance and coordinate-independence limitation]`

#### 4d. Gossip vs Central Aggregation — The Tradeoff

| Dimension | Central Aggregation (FedAvg/Krum) | Gossip (Decentralized) |
|-----------|----------------------------------|------------------------|
| Single point of failure | Yes — aggregator server is SPOF | No — no aggregation server |
| Communication pattern | Hub-and-spoke (all → aggregator) | Peer-to-peer random walks |
| Convergence speed | Faster (synchronized rounds) | Slower (asynchronous, path-dependent) |
| Byzantine handling | Easier to apply Krum/median at one node | Harder — malicious node can diffuse poison slowly |
| Bandwidth bottleneck | Aggregator can be bottleneck | Distributed — no bottleneck |
| Operational complexity | Aggregator must be managed | More complex topology management |
| Grid suitability | WAN uplinks to a fog hub exist (NATS JetStream hub) | Substations may not peer directly |

**Interview one-liner:** "Central aggregation is operationally simpler and lets you apply Krum at
one node, but creates a SPOF and bottleneck. Gossip removes the SPOF but makes Byzantine defense
harder — a malicious gradient propagates peer-to-peer before anyone can reject it. For a
fleet of substations with a NATS hub already in place, central aggregation with Krum is the
natural fit."

`[VERIFIED: WebSearch — gossip vs. federated learning architectural comparison, arxiv 2503.07505]`

### 5. Edge Security (Awareness Depth — One Paragraph Each)

#### 5a. OTA Update Integrity

**What it is:** Over-the-air firmware / software update with cryptographic signing. The build
pipeline signs the update image with a private key held in an HSM; the edge device verifies the
signature before applying it. Only images that pass signature verification are installed.

**The concrete grid threat it counters:** A malicious actor pushes a firmware image to a fleet of
substation K3s nodes that disables protection relays or exfiltrates PMU data. Without code signing,
any image that arrives via the update channel is applied. With signing, an unsigned or invalidly
signed image is rejected before execution — the attacker must compromise the signing key, not just
the update distribution channel.

**Juan's bridge:** Juan has shipped OTA updates (CV). The upgrade is to add a signing step to the
pipeline and a signature-check step at the node — the mechanism is the same; the security guarantee
is the grid-safety net.

`[VERIFIED: DeviceAuthority, Promwad — OTA signing pipeline; IETF RFC 9683 TPM-based network device attestation]`

#### 5b. TPM Attestation

**What it is:** A Trusted Platform Module (TPM 2.0) is a dedicated hardware security chip on the
edge device. During boot, each firmware/software stage measures the next stage and records the
measurement in Platform Configuration Registers (PCRs) — a tamper-resistant running hash of
everything that executed since power-on. **Remote attestation** lets a remote verifier (the fog
aggregator or SPIRE server) challenge the device: "Send me your PCR values signed with your TPM's
endorsement key." If the PCRs match the expected values for trusted, unmodified software, the
device is admitted to the federated learning round.

**The concrete grid threat it counters:** A relay (protection IED or K3s edge node) that has been
physically tampered with or whose OS has been compromised requests to join the federated
learning aggregation. Without TPM attestation, the aggregator cannot distinguish a clean node
from a rooted one and accepts its gradient updates. With TPM attestation, the node must prove
its boot chain hash matches the known-good configuration before any update is accepted.

`[VERIFIED: IETF RFC 9683, arxiv TPM-5G-Kubernetes paper; Medium TPM 2.0 attestation article]`

#### 5c. SPIFFE / SPIRE Workload Identity

**What it is:** SPIFFE (Secure Production Identity Framework for Everyone) is a CNCF-graduated
standard for cryptographic workload identity — each running process (a K3s pod, a NATS subscriber,
a FastAPI service) gets a short-lived X.509 certificate whose Subject Alternative Name URI encodes
a SPIFFE ID (`spiffe://trust-domain/path`). SPIRE is the production implementation of SPIFFE:
a SPIRE server issues SVIDs (SPIFFE Verifiable Identity Documents); SPIRE agents run on each node
and attest the node's identity (including via TPM) before issuing credentials to local workloads.
SVIDs are short-lived (minutes to hours) and auto-rotate — no static shared secrets.

**The concrete grid threat it counters:** An attacker who has compromised a device on the NATS
network (or intercepted a long-lived API key) tries to impersonate a real substation's EKF service
and inject false state estimates into the federated aggregation. Without workload identity, the
aggregator cannot distinguish the real substation-7 EKF pod from a spoofed one with the same IP
address or a stolen secret. With SPIFFE/SPIRE, the legitimate pod holds a short-lived SVID that
the attacker cannot forge without also compromising the SPIRE server; the spoofed node's
connection is rejected at the mTLS handshake.

`[VERIFIED: CNCF graduation status confirmed (RedHat, SecureW2, CNCF.io sources); SPIRE + edge/TPM attestation confirmed in axelspire.com workload identity article]`

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Federated learning orchestration | Custom FL aggregation server | Flower (flwr) in production | Edge cases: partial client updates, stragglers, secure aggregation — Flower handles these |
| Workload identity / PKI rotation | Static API keys or hand-rolled cert management | SPIFFE/SPIRE | Short-lived SVIDs with auto-rotation; static keys are the attack vector SPIRE eliminates |
| TPM attestation logic | Custom PCR-reading scripts | Keylime or SPIRE TPM attestation | Keylime integrates IMA, PCRs, remote verifier; hand-rolling misses boot-chain details |
| Byzantine aggregation | Custom distance filtering | torchfl / Flower strategy plugins | Krum and trimmed-mean are pre-built strategies; custom implementations miss edge cases |

**For the demo only:** Hand-rolling FedAvg / FedProx / Krum in NumPy is correct and intentional — the purpose is to show understanding of the math, not exercise a framework. "From scratch in NumPy" is a feature of this demo, not a real-system recommendation.

---

## Common Pitfalls

### Pitfall 1: Conflating federated with distributed
**What goes wrong:** Saying "distributed learning" and "federated learning" interchangeably. An interviewer will probe the distinction.
**Why it happens:** Both involve multiple nodes computing in parallel.
**How to avoid:** Use the three-clause test: data location (central vs. stays local), coordinator role (knows data vs. never sees data), what moves on the wire (data shards vs. weights/gradients only).
**Warning signs:** If you say "the server sends data to workers" you've described distributed, not federated.

### Pitfall 2: Saying FedProx adds a term to the server update
**What goes wrong:** Misplacing the proximal term on the aggregation step rather than the local objective.
**Why it happens:** The global update $w_{t+1} = \sum_k \frac{n_k}{n} w_t^k$ looks like the obvious place to add regularization.
**How to avoid:** The proximal term is in the **client's local optimization**, not the server's aggregation. Each client minimizes $F_k(w) + \frac{\mu}{2}\lVert w - w_t \rVert^2$ — this is what limits local drift before the update is sent.

### Pitfall 3: Claiming Krum averages the selected updates
**What goes wrong:** Saying "Krum picks the best gradients and averages them."
**Why it happens:** Multi-Krum does average a subset; vanilla Krum selects a single update.
**How to avoid:** Be precise: vanilla Krum selects **one** update (the one with minimum Krum score); Multi-Krum selects $m$ updates and averages them. State which variant you mean.

### Pitfall 4: Claiming coordinate-wise median is always better than Krum
**What goes wrong:** Over-selling median as strictly superior.
**Why it happens:** Median tolerates higher Byzantine fraction ($n/2$) vs. Krum ($n/(2f+3)$).
**How to avoid:** Name the limitation: median ignores gradient correlations, so a sophisticated attacker can craft attacks that are individually median-safe but jointly adversarial. Krum operates on the full vector and is resistant to this. "Use median for high Byzantine fraction; Krum for higher-dimensional joint robustness."

### Pitfall 5: Describing SPIFFE/SPIRE as just TLS
**What goes wrong:** "SPIFFE is basically TLS for services."
**Why it happens:** SPIFFE issues X.509 certificates.
**How to avoid:** The key distinction is **workload identity, not just channel encryption**. TLS encrypts the channel; SPIFFE identifies *which specific workload* is on each end — and rotates that identity automatically, without static secrets. The SVID encodes a process identity URI, not just a hostname.

### Pitfall 6: Claiming Juan has implemented federated learning
**What goes wrong:** Bridge callout that overstates Juan's FL experience.
**Why it happens:** The "→ Bridge to your work" framing can drift from "honest delta" to "claim adjacency."
**How to avoid:** The exact wording from D-07: "In OSED I ran distributed edge inference across DER nodes — no cloud round-trip for local decisions. I haven't run federated *learning* in production, but that's the natural next step: keep the local inference, add FedAvg so the fleet improves a shared model without ever shipping raw telemetry — and Krum so one bad node can't poison it."

---

## Code Examples

### FedAvg weighted average (NumPy, from scratch)

```python
# Source: McMahan et al. 2017 — implemented from scratch for the demo
import numpy as np

def fedavg_aggregate(local_models, n_samples):
    """
    local_models: list of np.ndarray, one per client
    n_samples: list of int, number of samples per client
    Returns: global model (weighted average)
    """
    n_total = sum(n_samples)
    weights = [n / n_total for n in n_samples]
    global_model = sum(w * m for w, m in zip(weights, local_models))
    return global_model
```

### FedProx local objective step (NumPy, from scratch)

```python
# Source: Li et al. 2020 (FedProx) — proximal term added to local SGD
def fedprox_local_step(w_local, w_global, grad_fn, mu, lr):
    """
    One local SGD step with FedProx proximal term.
    w_local: current local model parameter(s), np.ndarray
    w_global: global model at start of round (frozen), np.ndarray
    grad_fn: callable returning gradient of F_k(w) at w
    mu: proximal coefficient (>0)
    lr: learning rate
    """
    grad = grad_fn(w_local)
    proximal_grad = mu * (w_local - w_global)   # gradient of (mu/2)||w - w_t||^2
    return w_local - lr * (grad + proximal_grad)
```

### Krum selection (NumPy, from scratch)

```python
# Source: Blanchard et al. 2017 — implemented from scratch
def krum_select(updates, f):
    """
    updates: list of np.ndarray gradient updates, one per client
    f: assumed number of Byzantine clients
    Returns: index of the selected (most trustworthy) update
    """
    n = len(updates)
    n_neighbors = n - f - 2     # number of nearest neighbors to sum over
    scores = []
    for i, u_i in enumerate(updates):
        dists = sorted(
            [np.sum((u_i - u_j)**2) for j, u_j in enumerate(updates) if j != i]
        )
        scores.append(sum(dists[:n_neighbors]))
    return np.argmin(scores)    # client with minimum Krum score is selected
```

### Coordinate-wise median (NumPy, one-liner)

```python
# Source: Byzantine-robust aggregation literature (Yin et al. 2018; Aalto 2024-2025)
def coord_median(updates):
    """
    updates: list of np.ndarray gradient updates
    Returns: coordinate-wise median across all clients
    """
    return np.median(np.stack(updates), axis=0)
```

---

## Demo Design — Concrete Specification

This section specifies the demo parameters so the planner can write an exact implementation task.

### Dataset Design (non-IID by construction)

Use **1-D mean estimation** as the simplest possible non-IID problem:
- $N = 6$ clients
- Client $k$ has a local dataset of $n_k$ samples drawn from $\mathcal{N}(\mu_k, \sigma^2)$
- True means $\mu_k$: `[0.0, 0.5, 1.0, 1.5, 2.0, 2.5]` — each client has a different "local
  optimum", simulating substations with different load profiles / DER mixes
- $\sigma = 0.3$ (within-client noise)
- $n_k$: varied, e.g. `[50, 80, 60, 90, 70, 40]` — heterogeneous client sizes

The **global optimum** (what FedAvg should converge to) is the weighted mean across all clients,
roughly ~1.2. Under pure non-IID FedAvg with many local epochs, local models drift toward their own
$\mu_k$ and the weighted average overshoots.

### FedProx μ and Local Epoch Choice for Legible Contrast

- Local epochs $E = 10$ (enough to cause visible drift under non-IID)
- FedAvg: runs $E$ local gradient steps with no constraint
- FedProx $\mu = 0.5$: visibly damps drift; the contrast with FedAvg is clear
- Contrast column in output: final global model estimate after 20 rounds for plain FedAvg vs.
  FedProx, alongside the true global optimum

### Poison Injection

- Client 0 sends `update = true_global_model - 5.0` (a −5 shift — far outside honest cluster)
- Plain FedAvg: global model pulled significantly away from true optimum
- Krum: client 0's update has the highest Krum score (most distant from cluster) — rejected
- Coord median: coordinate-wise median ignores the outlier — result near true optimum

### Output Table Format (before/after contrast)

```
======================================================
  FedAvg / FedProx / Byzantine Robustness Demo
======================================================

  Clients: 6   Local epochs: 10   Rounds: 20   Poison: client 0 (shift -5.0)
  True global optimum: ~1.22

  Method             | Final Estimate | Error  | Notes
  -------------------|---------------|--------|---------------------------
  Plain FedAvg       |  -0.83        | -2.05  | Poisoned — client 0 pulled it off
  FedProx (mu=0.5)   |   1.31        |  0.09  | Proximal term kept local models near global
  Krum (f=1)         |   1.24        |  0.02  | Rejected client 0; selected honest update
  Coord Median       |   1.19        | -0.03  | Median ignores outlier
  -------------------|---------------|--------|---------------------------
```

(Exact numbers will vary with random seed; demo should use `np.random.seed(42)` for reproducibility.)

### Files to Create

```
demo/
├── fedavg_fedprox_krum_demo.py   — single self-contained script (~120–150 lines)
└── README.md                      — interview talking points + how to run + expected output
```

---

## AGMS Connection Hooks (for the FED-01/02 Notes — D-06)

These are the cross-reference hooks the planner must ensure appear as callout boxes in the notes.
They should be brief (1–3 sentences) and link back to Phase 3/4 artifacts — not re-derive them.

| FED Note | AGMS Connection | Cross-link |
|----------|-----------------|------------|
| FED-01 (federated coordination) | Scout Command deploying scouts to FADs is federated decisioning: each FAD operates autonomously (island mode), sharing state via NATS — not raw sensor data, just status/commands. The fog/federated tier in STK-05 is where GWCH orchestrates this. | `.planning/research/patents/INDEX.md`, `STK-05-reference-architecture.md` |
| FED-01 (FedAvg / model sharing) | Operation Loop simulate-before-commit (US 12,596,341 B2 claim 3) is the grid analog: propose a formation, simulate the operation loop, then commit — the same "compute before acting" principle that makes FedProx safe to deploy. | `.planning/research/patents/operation-loop.md` |
| FED-02 (Byzantine / fog tier) | GWCH's federated edge transaction manager (fog tier) would be where Byzantine-robust aggregation runs in the AGMS architecture — the "simulate-before-commit" gate and Byzantine gradient filter both live at Tier 3. | `STK-05-reference-architecture.md §5` |

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Plain FedAvg (McMahan 2017) | FedProx (2020), FedBN (2021) for non-IID | 2020 onward | FedAvg is still the baseline; FedProx is the standard treatment for non-IID; name both |
| Hand-rolled cert management | SPIFFE/SPIRE SVIDs (CNCF graduated) | CNCF graduation ~2022 | Workload identity is now standardized; no custom PKI needed for K3s fleets |
| Central aggregation only | Gossip / fully decentralized FL (Hegedüs et al.) | 2019 onward | Awareness: gossip learning is the research alternative; central + NATS hub is the practical grid choice |
| Krum only for Byzantine defense | Coordinate-wise median, trimmed mean, FLTrust | 2018–2022 | Know Krum (2017) and median (2018) as the two canonical techniques; others exist but not needed for interview |
| Static long-lived API keys | TPM-attested SPIRE SVIDs | Active area | IETF RFC 9683 (2025) formalizes TPM-based remote integrity verification for network devices |

**Deprecated / watch out for:**
- **"Secure aggregation" (HE/SMPC):** Often conflated with Byzantine robustness — they address different threats. Secure aggregation hides individual gradients from the aggregator (privacy). Krum/median rejects malicious gradients (integrity). Both can be used together but are separate mechanisms. The notes should not conflate them. `[ASSUMED — standard FL literature distinction; verify if interviewer raises it]`

---

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | Secure aggregation (HE/SMPC) and Byzantine robustness address different threats and should not be conflated | State of the Art | Low risk — this is standard FL literature consensus; only matters if interviewer specifically asks about privacy-preserving aggregation |
| A2 | FedBN is the best-performing method in the Ghosh & Mittal substation study (F-score 0.88) | Technical Substance §3 | Low risk — the claim is cited; if wrong it does not affect the FedAvg/FedProx mechanics that are the core content |

**All FedAvg formula, FedProx proximal term, Krum score, coordinate-wise median mechanics, and SPIFFE/SPIRE/OTA/TPM descriptions were verified against primary sources or authoritative secondary sources in this session.**

---

## Open Questions

1. **Exact $\mu$ for legible demo contrast**
   - What we know: $\mu = 0.5$ should damp drift visibly for 6 clients / 10 local epochs / 1-D mean estimation; typical range is $0.01$–$1.0$
   - What's unclear: The exact drift magnitude depends on the RNG seed and local epoch count; the demo should run and print the table, then the author should tweak $\mu$ if the contrast is not legible
   - Recommendation: Start with $\mu = 0.5$ and poison magnitude $5.0$; adjust after first run

2. **Whether to show both Krum and coordinate-wise median in the demo**
   - What we know: D-05 says "at least one, ideally both named"; both are ~3 lines each in NumPy
   - What's unclear: Page length vs. clarity tradeoff
   - Recommendation: Show both — they contrast cleanly (Krum selects; median does not depend on knowing $f$) and the combined demo is still ~120–150 lines

3. **AGMS overlay depth in notes**
   - What we know: D-06 says "keep short" and "cross-reference, don't re-derive"
   - What's unclear: Whether a 1-sentence callout or a 3-sentence callout is the right weight
   - Recommendation: Use a "→ STK-05 connection" callout box (styled like "→ Bridge to your work") with 1–2 sentences + a file cross-link — same pattern as the bridge callouts, just pointing to Phase 3/4 instead of Juan's CV

---

## Environment Availability

> Step 2.6 audit — relevant only for the demo script.

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Python 3 | demo script | ✓ | 3.11+ (confirmed from Phase 1/2 demo execution) | — |
| numpy | demo script | ✓ | 1.26+ (confirmed from Phase 1/2 demo) | — |
| matplotlib | demo README / plot | Optional — demo can print table only if no display | Confirmed present in Phase 1/2 | Table-only output (no plot needed for this demo) |

**Decision for demo:** Print the contrast table to stdout (the primary deliverable); matplotlib plot is optional and can be omitted entirely. The Phase 1/2 demos used matplotlib for the "I have a plot" talking point, but for this demo the table is the talking point. Recommend **no matplotlib** in the FedAvg/Krum demo — it simplifies the script and the "watching the numbers" table is more interview-legible than a plot.

---

## Sources

### Primary (HIGH confidence)
- McMahan et al. (2017), "Communication-Efficient Learning of Deep Networks from Decentralized Data" — FedAvg algorithm, weighted-average update rule, communication-round structure `[CITED]`
- Li et al. (2020), "Federated Optimization in Heterogeneous Networks" (FedProx) — proximal term formula, client-drift problem definition `[CITED: arxiv.org/pdf/1812.06127]`
- Blanchard et al. (2017), "Machine Learning with Adversaries: Byzantine Tolerant Gradient Descent" (Krum) — Krum score formula, nearest-neighbor selection `[CITED]`
- IETF RFC 9683 (2025), "Remote Integrity Verification of Network Devices Containing Trusted Platform Modules" — TPM 2.0 remote attestation standard `[CITED: datatracker.ietf.org/doc/html/rfc9683]`
- CNCF SPIFFE/SPIRE project (graduated) — workload identity standard, SVID structure `[CITED: redhat.com/en/topics/security/spiffe-and-spire]`
- Ghosh & Mittal, Frontiers AI 2025 — "Federated learning for critical electrical infrastructure: handling data heterogeneity for predictive maintenance of substation equipment" — confirms non-IID challenge and FedProx evaluation on real substation data `[CITED: frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1697175]`

### Secondary (MEDIUM confidence)
- Aalto/ACM Workshop 2024–2025 — coordinate-wise median in Byzantine federated learning — mechanics and robustness properties `[CITED: research.aalto.fi, dl.acm.org/doi/10.1145/3709023.3737691]`
- Hegedüs et al. (2019) — "Gossip Learning as a Decentralized Alternative to Federated Learning" — gossip vs. central aggregation tradeoff `[CITED: springer.com/chapter/10.1007/978-3-030-22496-7_5]`
- apxml.com FL course — FedProx algorithm and Byzantine aggregation survey (cross-reference confirmation) `[VERIFIED: secondary]`
- Promwad / DeviceAuthority — OTA firmware signing pipeline for edge devices `[CITED: promwad.com/news/building-secure-ota-update-pipelines-firmware-integrity-factory-to-field]`

### Tertiary (LOW confidence)
- axelspire.com — SPIFFE workload identity with TPM for device fleets — useful framing but single secondary source `[LOW: single source]`

---

## Metadata

**Confidence breakdown:**
- FedAvg / FedProx formulas and mechanics: HIGH — verified against primary papers and multiple consistent secondary sources
- Krum / coordinate-wise median mechanics: HIGH — verified via WebSearch against published proceedings
- Non-IID / substation grounding: HIGH — confirmed in 2025 published research on real substation equipment
- Edge security (OTA/TPM/SPIFFE-SPIRE): HIGH — all three are CNCF graduated or IETF-standardized; mechanisms verified
- Gossip vs. central tradeoff: MEDIUM — verified via multiple academic sources; operational grid recommendation is reasoned inference from architecture
- Demo parameter choices ($\mu$, poison magnitude): MEDIUM — based on standard FL practice; exact values need one test run to confirm legibility

**Research date:** 2026-06-14
**Valid until:** 2026-07-14 (stable algorithms; SPIFFE/SPIRE version details may evolve but awareness-depth content is durable)
