# KAL-01: Virtual Sensing & the Kalman Filter as a Fusion Engine

**For:** Oral rehearsal — speak each section aloud before the interview.
**Purpose:** Establish *why* the Kalman filter exists in this role. The filter is not the point;
the hard, valuable problem is **manufacturing observability for under-measured distribution nodes**
by finding and fusing every available source of side-information. State estimation is reframed as
an **information-sourcing-and-fusion problem**.

---

## <3-min say-aloud version

> "Virtual sensing is the job of manufacturing a state estimate at a node where you have no direct
> sensor — and crucially, delivering that estimate *with a calibrated uncertainty*. The Kalman filter
> is the vessel you pour information into; the real engineering problem is sourcing the information
> in the first place.
>
> Transmission state estimation works because redundancy comes from **space**: you have more
> measurements than states, the Jacobian has full column rank, WLS converges, and chi-squared
> bad-data detection gives you a pass/fail. Distribution is the opposite: hundreds to thousands of
> nodes, but real-time telemetry might be just the feeder head plus a handful of inverters and
> delayed AMI — you are severely under-determined. The gain matrix $G = H^\top W H$ is **singular**;
> there is no unique WLS solution. Classical snapshot SE cannot even start.
>
> So the job shifts: instead of batch-solving a redundant measurement soup, you *accumulate* every
> scrap of information the grid offers — topology coupling, zero-injection constraints, forecasts,
> ML priors, smart-inverter self-reports, delayed AMI — and you fuse them through a **recursive
> filter** that borrows information across time as well as space. The prior from two minutes ago is
> itself an information source; so is the physics model; so is the Kirchhoff constraint that ties
> an unmetered node to its metered neighbors.
>
> The deliverable is not just a number but a **posterior covariance** — and that covariance is the
> ORACS Observability index in the AGMS architecture. It gates every downstream decision. When
> observability degrades — comms drops, a sensor fails — the covariance inflates, and AGMS sees
> it immediately. Because the filter is recursive and local, it keeps running **in island mode when
> the WAN is down**. That is the resilience bet the AGMS Inspector-scout architecture is built on,
> and it falls out of the filter's structure itself."

---

<!-- greppable tag: virtual sensing reframe -->

## 1. The Central Reframe — Filter as Vessel, Information as the Job

The standard ML/controls framing of the Kalman filter emphasizes the algorithm: predict,
innovate, update. That framing is correct but misleading for this role. Here the filter is the
*easy part*. The hard engineering problem is:

**How do you manufacture enough information to make an under-observed distribution node
estimable in the first place?**

Every source of side-information — network topology, zero-injection constraints, diurnal load
profiles, ML forecasts, smart-inverter telemetry, delayed AMI, physical line parameters — is a
piece of observability. The filter fuses them by weighting each by its inverse covariance. Your
job as a virtual-sensing engineer is to find, model, and honestly characterize *every one of
those sources*, then hand them to the filter in the right form.

**Interview sentence:** "I think of the Kalman filter as the accounting engine; the real work is
auditing every information source the grid offers, assigning it an honest covariance, and casting
it as either a measurement, a process prior, or a structural constraint."

---

<!-- greppable tag: transmission vs distribution observability -->

## 2. Transmission (Redundancy from Space) vs. Distribution (Under-Observability)

Understanding this contrast precisely is what separates a transmission-SE practitioner from a
distribution virtual-sensing engineer. The role is the latter.

### Transmission: the happy case

A large transmission network is instrumented with SCADA meters, PMUs, and voltage sensors. The
measurement count $m$ **exceeds** the state count $n$:

$$m > n \quad\Longrightarrow\quad G = H^\top W H \text{ is full-rank and invertible}$$

The WLS objective has a unique minimum:

$$J(x) = [z - h(x)]^\top W\,[z - h(x)], \qquad W = R^{-1}$$

Gauss-Newton iteration (linearize $H$, form $G$, solve $\Delta x = G^{-1} H^\top W [z - h(\hat x)]$,
update $\hat x$) converges in 2–4 iterations. After convergence, the weighted residual cost
$J(\hat x) \sim \chi^2(m-n)$, giving a clean bad-data detection test, and the largest-normalized-residual
(LNR) test $r_i^N = |r_i|/\sqrt{\Omega_{ii}}$ identifies the culprit.

**The critical-measurement trap (awareness):** a leverage measurement at a sparsely instrumented
bus has near-zero normalized residual even when corrupted — the estimator has no independent
reading to contradict it. This is the main failure mode of chi-squared bad-data detection. But on
a well-instrumented transmission network, leverage measurements are the exception.

### Distribution: the hard case (the role's actual domain)

A distribution feeder has hundreds to thousands of nodes. Real-time telemetry might be:
- One feeder-head SCADA flow (fast)
- A handful of smart-inverter self-reports (fast but sparse)
- AMI reads at 15-minute intervals, delayed by minutes-to-hours

That gives $m \ll n$. The gain matrix $G = H^\top W H$ is **rank-deficient / singular**. WLS has no
unique solution. The chi-squared test requires $(m - n) > 0$ degrees of freedom — there are none.
**Bad-data detection mostly fails because almost every real measurement is critical** — the
leverage/critical-measurement trap is the *normal condition*, not an edge case.

| Dimension | Transmission | Distribution |
|-----------|-------------|-------------|
| Measurement count | $m > n$ (over-determined) | $m \ll n$ (under-determined) |
| Gain matrix $G = H^\top W H$ | Full rank, invertible | Singular or near-singular |
| WLS solution | Unique | Does not exist without additional priors |
| Bad-data detection | Chi-squared / LNR works (has redundancy) | Mostly fails (no redundancy; leverage is normal) |
| Critical-measurement trap | Exceptional | Standard operating condition |
| What fills the observability gap | More sensors (space) | Priors + forecasts + topology + time |

**The energy-transition double-edge.** DER penetration makes the physics harder (bidirectional,
volatile, weather-coupled flow → larger process uncertainty $Q$) while simultaneously
*instrumenting* the grid (every smart inverter, battery, EVSE, and AMI meter is a new
telemetry source). Distribution virtual sensing must net this out positive.

---

## 3. The Information-Budget Mental Model

For any unmetered distribution node, the state estimate is built from a **budget** of information
sources. Each source contributes via its own covariance:

$$\underbrace{\text{estimate at node}}_{\hat x_i,\;P_i} = \underbrace{\text{direct measurement}}_{\text{if any, small }R} + \underbrace{\text{physical coupling}}_{\text{topology + power flow}} + \underbrace{\text{zero-injection constraints}}_{\text{virtual measurement, }R\to0} + \underbrace{\text{temporal prior}}_{\text{forecast/FASE}} + \underbrace{\text{learned prior}}_{\text{ML pseudo-measurement}}$$

The Kalman gain $K$ automatically weights each by its inverse covariance. A high-confidence
ML forecast (small $R_{pseudo}$) pulls the estimate strongly; a stale AMI reading (large $R_{ami}$)
pulls weakly. The filter is the accountant; you supply the line items.

**The compact WLS recap (frame as the static baseline that fails under distribution sparsity,
motivating the recursive/dynamic approach that borrows information across time):**

$$J(x) = [z - h(x)]^\top W\,[z - h(x)], \qquad W = R^{-1}$$

$$G = H^\top W H, \qquad \Delta x = G^{-1} H^\top W\,[z - h(\hat x)], \qquad \hat x \leftarrow \hat x + \Delta x$$

WLS gives the best static snapshot when $G$ is invertible. When it is not — the distribution
case — you need the recursive Kalman structure that **borrows information across time**: the prior
from the last step is itself a measurement with covariance $P_{k|k-1}$.

**Interview sentence:** "WLS gives you the best static snapshot; Kalman-based distribution SE
gives you a running film with uncertainty quantification at every frame, and the prior from two
minutes ago is itself an information source."

---

## 4. Deliverable = Estimate + Calibrated Covariance = ORACS Observability Index

The virtual-sensing estimator does not just produce a number $\hat x$. It produces a **posterior
distribution** $\mathcal N(\hat x, P)$. The covariance $P$ is the formal statement of how much the
filter knows. This is not a secondary output; it *is* the primary engineering deliverable.

In the AGMS architecture (the director's patent), the posterior covariance maps directly to the
**ORACS Observability index** that the **Asset Portfolio Manager** (module 1300) gates on. The
pipeline:

1. Inspector scout $s_i$ on a Field Agent Device (FAD) runs the local virtual-sensing filter.
2. Posterior covariance $P$ is published to the Grid Operating Cell (inter-ORACS).
3. Asset Portfolio Manager 1300 reads $P$ and computes the Observability index.
4. If observability is sufficient: the continuous voltage-control **CaCSM** (Worked Example 2 in
   the patent — rooftop-solar overvoltage at unmetered nodes, no fault/alarm, only virtual
   sensing knows) is armed.
5. The estimate $(\hat x, P)$ seeds **simulate-before-commit** (patent claim 3) before any
   control action is dispatched.
6. The **Learning Engine** sees the innovation sequence and issues a calibration request to
   refine $Q$, $R$, and the pseudo-measurement priors.

**Recursive structure = island-mode safety.** Because the filter carries its own state and
propagates forward with the process model, it keeps producing estimates (with growing, honestly-
reported uncertainty) even when all external measurements drop. A centralized batch WLS stops
cold when the data feed breaks. The Inspector scout continues — it just inflates $P$, which AGMS
interprets as degraded observability rather than a system failure.

**Interview sentence:** "The posterior covariance is not a footnote — it IS the ORACS Observability
index that the AGMS Asset Portfolio Manager gates on, and the recursive structure is what keeps
the Inspector scout alive in island mode when the WAN drops."

---

## 5. Bridges to Juan's Work

<!-- greppable tag: Bridge to your work -->

| AGMS / Virtual Sensing Concept | Juan's Work |
|-------------------------------|------------|
| Calibrated pseudo-measurement / temporal prior generator | Edge-ML load/PV forecasting in HEMS / Building Intelligence — produces calibrated probabilistic forecasts that enter the filter as pseudo-measurements |
| Topology / structural prior (who connects to whom, zero-injections) | SI-MAPPER ontology graph — inferring structured topology from heterogeneous signals |
| Inspector-scout substrate (FAD edge runtime) | OSED edge runtime — the physical platform the scout runs on |
| Simulate-before-commit consumer | CVXPY MPC in OSED/HEMS — takes state + covariance as inputs; MPC is the "commit" step that the estimate seeds |

**How to say this in the interview:**

> "Every component of the AGMS virtual-sensing stack maps to something I've built. My HEMS
> edge-ML forecasting is the temporal prior generator — it produces calibrated probabilistic
> load/PV forecasts that enter the filter as pseudo-measurements with known covariance. My
> SI-MAPPER ontology graph is the structural prior — it encodes topology and zero-injection
> constraints. OSED is the FAD substrate the Inspector scout runs on. And my CVXPY MPC is the
> simulate-before-commit step: it takes the posterior estimate and covariance, propagates them
> forward, and only dispatches commands when the constraint-satisfaction probability is high
> enough. I haven't operated these in a GE Vernova context, but the building blocks are the same."

---

## 6. The Reframe in Three Sentences (Use to Open Any Answer)

Memorize these three sentences as the opening for any virtual-sensing question:

1. "Virtual sensing is manufacturing observability for under-measured nodes — the filter is just
   the accounting engine."
2. "The real engineering problem is sourcing, modeling, and honestly characterizing every
   information source the grid offers."
3. "The deliverable is a posterior covariance, not just a number — that covariance IS the
   observability index downstream systems gate on."

---

## Quick-Recall Card (Recite Before the Interview)

1. **The reframe:** filter = vessel; the job = manufacturing observability from side-information.
2. **Transmission:** $m > n$, $G$ invertible, WLS works, chi-squared / LNR bad-data detection works.
3. **Distribution:** $m \ll n$, $G$ singular, WLS unsolvable without priors; bad-data detection mostly fails because leverage is normal.
4. **The double-edge:** DER = harder physics (volatile, bidirectional) + more telemetry (smart inverters, EVSEs, AMI) — net it out positive.
5. **Information budget:** direct measurement + topology coupling + zero-injection constraints + temporal prior + learned prior — filter weights each by $R^{-1}$.
6. **WLS recap:** $J(x) = [z-h(x)]^\top W[z-h(x)]$; $G = H^\top WH$; $\Delta x = G^{-1}H^\top W[z-h(\hat x)]$. Fails when $G$ is singular.
7. **Deliverable:** $\hat x$ AND $P$ — the covariance IS the ORACS Observability index.
8. **AGMS pipeline:** Inspector scout $s_i$ → posterior $P$ → Asset Portfolio Manager 1300 → CaCSM voltage control → simulate-before-commit → Learning Engine calibration.
9. **Island-mode safety:** recursive structure keeps producing estimates (with inflating $P$) when WAN drops; centralized batch WLS stops cold.
10. **My bridges:** HEMS forecasts = temporal prior; SI-MAPPER = structural prior; OSED = FAD substrate; CVXPY MPC = simulate-before-commit.

---

*Sources: arXiv 2502.18229 (JuliaGrid WLS); ResearchGate 329665834 (WLS framework); AGMS patent
(Director; Inspector scout s_i, ORACS Observability, Asset Portfolio Manager 1300,
simulate-before-commit, Learning Engine); GE Vernova JD R5043890 (virtual sensing, federated,
distribution); 01-RESEARCH.md verified equations.*
