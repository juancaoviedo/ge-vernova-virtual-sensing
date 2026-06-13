# TVS-02: DC Power-Flow Angle Inference (P = Bθ, Linear WLS)

**For:** Oral rehearsal — speak each section aloud before the interview.
**Purpose:** Close the transmission angle-inference vocabulary gap so you can state the DC
power-flow approximation $P = B\theta$, explain the sparse-PMU coverage problem, and frame
phase-angle estimation as a weighted-least-squares problem — building directly on KAL-01
rather than re-deriving it.

> **This is the linear case of KAL-01.** KAL-01 already owns the WLS objective, the
> Gauss-Newton iteration, observability, and bad-data detection. In DC power flow the
> measurement function is *linear* in the bus angles, so KAL-01's Gauss-Newton **collapses to a
> single one-shot solve** — no iteration, no Jacobian re-evaluation. This note shows that
> collapse and the DC-specific machinery (the $\mathbf B$ matrix, the slack bus). It does **not**
> re-derive Gauss-Newton — see KAL-01 §3 for that.

---

## <3-min say-aloud version

> "In transmission you often care about the bus voltage angles, because real power flow is
> driven by angle differences. The DC power-flow approximation makes that exactly linear: assume
> flat voltage magnitudes near one per-unit, small angle differences so sine is its argument and
> cosine is one, and lossless lines so each branch admittance is just $1/x$, the susceptance.
> Under those assumptions the branch flow is $b_{ij}(\theta_i - \theta_j)$, and stacking every bus
> gives $P = B\theta$, where $B$ is the susceptance-weighted graph Laplacian of the network. $B$
> is singular because angles are only relative, so you pick a slack bus, set its angle to zero,
> and delete its row and column. Now the problem: PMUs measure angles directly, but PMU coverage
> is sparse and expensive, so most bus angles are unmeasured and have to be inferred. That is a
> state-estimation problem — and because the model $z = H\theta + e$ is linear, the
> Gauss-Newton estimator from KAL-01 collapses to one shot:
> $\hat\theta = (H^\top W H)^{-1} H^\top W z$. One solve, no iteration. Concretely, a 3-bus
> network with all susceptances $10$ and bus 1 as slack gives a reduced $B$ of
> $[[20,-10],[-10,20]]$ — and that is exactly the demo I built."

---

## 1. The DC Approximation Assumptions (Mental Model First)

Full AC power flow is nonlinear — that is why KAL-01 needed Gauss-Newton iteration. The **DC
power-flow approximation** trades a little accuracy for a fully *linear* model of real power, and
it is remarkably good on transmission networks because the three assumptions it makes are nearly
true there.

1. **Flat voltage magnitudes:** $V_i \approx 1.0$ p.u. at every bus. Transmission voltages are
   tightly regulated near nominal, so magnitude variation is second-order for *real* power.
2. **Small angle differences:** $\sin(\theta_i - \theta_j) \approx (\theta_i - \theta_j)$ and
   $\cos(\theta_i - \theta_j) \approx 1$. Across a healthy line the angle difference is a few
   degrees, where the small-angle approximation is excellent.
3. **Lossless lines:** resistance is negligible relative to reactance ($r \ll x$), so the branch
   admittance reduces to $1/x = b$, the **susceptance**.

**Result: real power flow becomes linear in the bus angles.** That linearity is the entire payoff
— it is what makes angle estimation a one-shot solve instead of an iteration.

**One-liner for the interview:** "DC power flow is the linearization of AC for real power — flat
voltages, small angles, lossless lines — and it makes power a linear function of bus angles,
which is what lets state estimation become a single matrix solve."

---

## 2. The $P = B\theta$ Derivation

**Branch flow.** Under the DC assumptions, the real power flowing from bus $i$ to bus $j$ on a line
of reactance $x_{ij}$ is proportional to the angle difference, with the susceptance as the constant:

$$P_{ij} = b_{ij}\,(\theta_i - \theta_j), \qquad b_{ij} = \frac{1}{x_{ij}}$$

**Bus injection.** The net real power injected at a bus is the sum of the flows leaving it on its
incident lines. Stacking that relation over every bus gives the compact matrix form:

$$\mathbf{P} = \mathbf{B}\,\boldsymbol{\theta}$$

where $\mathbf P$ is the vector of bus power injections, $\boldsymbol\theta$ the vector of bus
angles, and $\mathbf B$ is the **DC Bbus matrix** — a **susceptance-weighted graph Laplacian** of
the network:

$$B_{ii} = \sum_{k\in\mathcal{N}(i)} b_{ik}, \qquad B_{ij} = \begin{cases} -b_{ij} & i\neq j,\ i\text{ connected to } j \\ 0 & i\neq j,\ \text{not connected}\end{cases}$$

The diagonal of $B$ sums the susceptances of all lines touching a bus; each off-diagonal is the
negative susceptance of the line between two buses (zero if they are not directly connected). It
is exactly the Laplacian of the network graph with edges weighted by susceptance.

**The slack / reference bus.** $\mathbf B$ as written is **singular** — every row sums to zero,
because power injections are unchanged if you add a constant to *all* angles. Angles only matter
*relative* to a reference. So you pick one bus as the **slack** (reference) bus, fix
$\theta_{slack} = 0$, and **delete its row and column** from $\mathbf B$. The remaining **reduced
$B$ matrix** is nonsingular and the reduced system $B_{red}\,\theta = P$ is solvable for the
non-slack angles.

**Interview sentence:** "$P = B\theta$ where $B$ is the susceptance-weighted graph Laplacian. It's
singular because angles are relative, so you ground a slack bus at zero and delete its row and
column to get a solvable reduced system."

---

## 3. The Sparse-PMU Observability Gap (Awareness)

State this crisply — the deep PMU / IEEE C37.118 protocol treatment is Phase 4, not here.

A **PMU** (phasor measurement unit) measures bus voltage *phasors* — magnitude *and angle*,
time-synchronized to GPS — and line-current phasors, directly. If a PMU sat on every bus, the
angles would be measured outright and there would be little to estimate.

In reality, **PMU coverage is sparse and expensive.** Utilities instrument a subset of buses, so
**most bus angles are unmeasured** and must be **inferred** from the measurements that do exist —
the line flows, injections, and the PMU readings you have. Inferring the full angle vector from a
partial, redundant measurement set is precisely a **state-estimation problem on angles**, which
is the subject of the next section.

**Awareness sentence:** "PMUs give you angles directly, but coverage is sparse and costly, so most
bus angles are unmeasured — you infer the full angle state from the measurements you do have,
which is a state-estimation problem."

---

## 4. Angle Estimation as Linear WLS — The KAL-01 Link

Here is where TVS-02 cashes in KAL-01. The measurement model for DC angle estimation is **linear**:

$$z = H\theta + e, \qquad e \sim \mathcal N(0, R)$$

where each row of $H$ is the linear sensitivity of a measured quantity (a line flow or a bus
injection) to the angle vector — and those sensitivities are just susceptances. Compare this to
KAL-01's nonlinear $z = h(x) + e$: because $h(\theta) = H\theta$ is now **linear**, the Jacobian
$H$ is **constant**, so KAL-01's Gauss-Newton iteration **collapses to a one-shot solve**:

$$\hat{\boldsymbol\theta} = (H^\top W H)^{-1} H^\top W\, z, \qquad W = R^{-1}$$

This is the *same normal-equations form* as KAL-01 §3 — gain matrix $G = H^\top W H$, correction
driven by $H^\top W z$ — but with $H$ no longer re-linearized at each step. There is nothing to
iterate: one matrix solve gives the best weighted-least-squares angle estimate.

**Say this explicitly:** *"DC state estimation is the linear case of the WLS / Gauss-Newton
estimator from KAL-01 — one iteration, no Jacobian re-evaluation. The nonlinear AC version needs
Gauss-Newton; the DC version is a single solve because the measurement model is linear in
angles."*

**Interview sentence:** "Angle inference is weighted least squares: $z = H\theta + e$ with $H$
made of susceptances. Since it's linear, the KAL-01 Gauss-Newton iteration collapses to
$\hat\theta = (H^\top W H)^{-1} H^\top W z$ — one shot, no iteration."

---

## 5. The 3-Bus Worked Numbers (These Drive the Demo)

A concrete network makes the whole chain memorable — and these exact numbers drive the Plan-03
demo, so the note and the code line up.

**Network.** Three buses, lines $1\text{–}2$, $1\text{–}3$, $2\text{–}3$, with equal susceptances
$b_{12} = b_{13} = b_{23} = 10$ p.u. (reactances $x = 0.1$ p.u. each — round numbers for clean
arithmetic). Choose **bus 1 as slack**, $\theta_1 = 0$. The state is then the two non-slack angles
$[\theta_2, \theta_3]$ ($n = 2$).

**Reduced $B$.** Delete row/column 1. Each remaining diagonal sums the two susceptances incident
to that bus ($b_{12} + b_{23} = 20$ at bus 2; $b_{13} + b_{23} = 20$ at bus 3), and the
off-diagonal is $-b_{23} = -10$:

$$B_{red} = \begin{bmatrix} b_{12}+b_{23} & -b_{23}\\ -b_{23} & b_{13}+b_{23}\end{bmatrix} = \begin{bmatrix} 20 & -10\\ -10 & 20\end{bmatrix}$$

**Loads and ground-truth angles.** Take bus injections $P_2 = -1.0$ and $P_3 = -0.5$ p.u. (both
loads). The ground-truth angles solve the reduced system:

$$B_{red}\,\boldsymbol\theta = \mathbf P, \qquad \begin{bmatrix} 20 & -10\\ -10 & 20\end{bmatrix}\begin{bmatrix}\theta_2\\\theta_3\end{bmatrix} = \begin{bmatrix}-1.0\\-0.5\end{bmatrix}$$

which gives $\boldsymbol\theta \approx [-0.0833,\ -0.0667]$ rad (verify in code — the demo solves
this exactly). From these true angles the demo generates a redundant set of noisy line-flow and
injection measurements, then runs the linear WLS solve above — making this 3-bus case the
concrete, defensible whiteboard story for both $P = B\theta$ and the one-shot WLS estimate.

**Interview sentence:** "For a 3-bus network with all susceptances $10$ and bus 1 as slack, the
reduced $B$ is $[[20,-10],[-10,20]]$; with loads $-1.0$ and $-0.5$ the true angles come out around
$-0.083$ and $-0.067$ radians — and that's exactly the demo I built."

---

## → Bridge to your work

<!-- greppable tag: Bridge to your work -->

The strongest analog is **inferring an unmeasured full state from sparse, redundant sensors via
weighted least squares** — exactly the shape of your OSED thermal estimator and SI-MAPPER.

> **"Sparse PMU angle inference is the same shape as my OSED thermal estimator — too few direct
> sensors, so you infer the full state vector from a redundant set via weighted least squares."**

| DC Angle State Estimation | OSED / SI-MAPPER Inference |
|---------------------------|----------------------------|
| State = bus voltage angles $\boldsymbol\theta$ (mostly unmeasured) | State = building thermal state $[T_\text{zone}, \ldots]$ (not directly sensed) |
| Measurements = sparse PMU + line-flow / injection readings | Measurements = sparse, redundant BMS sensor readings |
| Linear model $z = H\theta + e$, $H$ from susceptances | (Near-)linear sensor model $y = Cx + e$, $C$ from the RC thermal model |
| Solve: $\hat\theta = (H^\top W H)^{-1} H^\top W z$ (one shot) | Solve: weighted-least-squares / convex objective over $x$ |
| SI-MAPPER analog: infer structured state where direct labels are absent | Infer ontology / structured state from images via redundant cues |

The common structure: the quantity you actually want is **unmeasured or only sparsely measured**,
so you infer the **full state vector** from a **redundant** set of available, noisy measurements by
**weighted least squares**. The grid version is the cleanest because DC makes it perfectly linear —
one solve — but the OSED thermal estimator is the same inference problem in the building domain.

**How to say this in the interview:**

> "Sparse PMU angle inference is structurally the same as my OSED building thermal estimator. In
> both you can't measure the state you care about everywhere — bus angles on the grid, zone
> thermal state in a building — so you infer the full state vector from a redundant set of sensors
> by weighted least squares. The DC power-flow case is the linear, one-shot version of the
> Gauss-Newton estimator: $\hat\theta = (H^\top W H)^{-1} H^\top W z$. I've already built this kind
> of redundant-sensor state inference in OSED, and SI-MAPPER does the same when it infers
> structured state where direct labels are absent."

---

## Quick-Recall Card (Recite Before the Interview)

1. **DC assumptions:** flat $V \approx 1.0$ p.u.; small angles ($\sin \approx \cdot$, $\cos \approx 1$); lossless ($r \ll x$, $b = 1/x$). → real power linear in angles.
2. **Branch flow:** $P_{ij} = b_{ij}(\theta_i - \theta_j)$, $b_{ij} = 1/x_{ij}$.
3. **Stacked:** $\mathbf P = \mathbf B\boldsymbol\theta$; $\mathbf B$ = susceptance-weighted graph Laplacian: $B_{ii} = \sum_k b_{ik}$, $B_{ij} = -b_{ij}$.
4. **Slack bus:** $\mathbf B$ singular (angles relative) → fix $\theta_{slack} = 0$, delete its row/column → reduced $B$ solvable.
5. **Sparse-PMU gap (awareness):** PMUs measure angles directly but coverage is sparse → most angles inferred → state-estimation problem.
6. **Linear WLS = KAL-01 collapsed:** $z = H\theta + e$ linear → $\hat\theta = (H^\top W H)^{-1} H^\top W z$, one shot, no Gauss-Newton iteration.
7. **3-bus:** $b = 10$ all lines, slack = bus 1; $B_{red} = [[20,-10],[-10,20]]$; loads $-1.0/-0.5$ → $\theta \approx [-0.083, -0.067]$ rad (verify in code).
8. **My bridge:** sparse angle inference IS my OSED thermal estimator — infer the full state from redundant sensors via weighted least squares.

---

*Sources: Abur & Expósito, "Power System State Estimation: Theory and Implementation" (2004), DC/linear SE chapter; KAL-01-wls-state-estimation.md §3 (WLS normal equations, Gauss-Newton — the linear case of which this is); 02-RESEARCH.md §TVS-02 verified equations and 3-bus worked numbers; CV — OSED building thermal estimator, SI-MAPPER structured-state inference.*
