# DSSE-01: The Under-Observability Problem & the Information-Sourcing Reframe

**For:** Oral rehearsal — speak the contrast table and the information-budget model aloud;
you must be able to deliver the transmission vs. distribution contrast in under 2 minutes.
**Purpose:** Establish the foundational framing for all four DSSE notes: distribution state
estimation is a severe under-observability problem, not a well-instrumented redundancy problem.
The solution is not better batch algebra — it is **information sourcing**: finding, modeling,
and honestly characterizing every scrap of side-information the grid offers, then fusing it
through a recursive estimator.

---

## <3-min say-aloud version

> "Transmission state estimation is a solved problem because redundancy comes from **space**:
> you have more measurements than states, the Jacobian $H$ has full column rank, WLS converges,
> and chi-squared bad-data detection works cleanly. Distribution is the hard, unsolved problem,
> and it is where this role lives.
>
> A typical distribution feeder has hundreds to a thousand nodes. States are per-node voltage
> magnitude and angle — or in the FASE formulation, per-node load injection — times three for
> three-phase unbalance. Real-time telemetry: feeder-head SCADA (one reading for the whole
> feeder), a handful of smart inverter self-reports, and AMI meters that arrive 15 minutes late.
> That is $m \ll n$ — severely under-determined. The gain matrix $G = H^\top W H$ is singular. There
> is no unique WLS solution. And because almost every real measurement is critical —
> remove any one and that part of the feeder goes unobservable — the chi-squared bad-data
> detection test has no redundancy to work with. The leverage/critical-measurement trap is the
> **normal operating condition** in distribution, not an edge case.
>
> So the job is not to solve a well-posed inverse problem — it is to **manufacture observability**
> from every information source available: network topology (Kirchhoff coupling), zero-injection
> constraints at known-passive nodes, conductor parameters, load cyclicality, ML forecasts, smart-
> inverter self-reports, delayed AMI. Each source goes into the filter with an honest covariance.
> DER penetration is both the problem and the solution: bidirectional volatile flows make the
> physics harder, but every smart inverter, battery, and EVSE is a new telemetry point."

---

<!-- greppable tag: under-observability -->

## 1. The Distribution Under-Observability Diagnosis

**What the state is.** A three-phase distribution feeder with $n$ buses has up to $6n$ state
variables: real and imaginary voltage (or magnitude/angle) at each phase at each node. In
simplified single-phase form: $2n$ states (magnitude + angle per node).

**What the measurements are.** In a typical feeder:
- **Head SCADA** — one three-phase power measurement at the substation (fast, reliable, but
  covers the entire feeder with one equation)
- **Smart inverter self-reports** — a handful of buses with DER, reporting their own terminal
  $P$, $Q$, $V$ (fast, but only at DER-instrumented buses)
- **AMI smart meters** — 15-minute interval averages, delayed minutes-to-hours, covering
  most residential loads but with coarse time resolution

Result: $m \ll n$. For a 100-node feeder, you might have $m = 5$–10 real-time measurements
against $n = 200$ state variables. **The gain matrix $G = H^\top W H$ is rank-deficient.**

**The WLS failure mode.** Attempting classical Gauss-Newton WLS:
$$\Delta x = G^{-1} H^\top W [z - h(\hat x)]$$
fails at the very first step: $G$ is singular, $G^{-1}$ does not exist, the normal equations
have infinitely many solutions. There is no unique operating-point estimate. This is not a
numerical issue — it is a fundamental absence of information.

---

<!-- greppable tag: critical measurement trap normal -->

## 2. The Critical-Measurement Trap as the Normal Condition

In transmission SE, **leverage measurements** (measurements whose removal renders part of the
network unobservable) are exceptional and must be identified and flagged. The chi-squared and
LNR bad-data tests work for the non-leverage measurements — they have redundancy.

In distribution SE, **nearly every real measurement is a leverage measurement.** Remove the
one feeder-head SCADA reading and the entire feeder is unobservable. Remove an inverter self-
report and that bus goes dark. The consequences:

1. **Chi-squared test has no degrees of freedom.** $J(\hat x) \sim \chi^2(m-n)$ requires
   $m > n$. With $m \ll n$, $m - n < 0$ — the test is undefined. There is no "residual
   distribution" to compare against.
2. **LNR test is structurally blind.** The normalized residual for a leverage measurement is
   near zero *by construction*, because the estimator fits the estimate entirely to that reading
   — there is nothing to contradict it. A corrupted leverage measurement gives a wrong-but-
   consistent estimate that passes every check.
3. **You cannot detect bad data by statistical redundancy because there is no statistical
   redundancy.**

What replaces bad-data detection in distribution?
- **Innovation / NIS monitoring over time** (is the sequential residual white and zero-mean?)
- **Cross-source consistency checks** (do AMI, inverter, and head tell a consistent story
  when they overlap?)
- **Robust pseudo-measurement priors** (don't let an overconfident prior become a de-facto
  leverage measurement at scale — see DSSE-03)

**Interview sentence:** "In distribution, the leverage/critical-measurement trap is the normal
operating condition, not an exception. Chi-squared bad-data detection mostly fails because there
is no redundancy — nearly every real measurement is critical. What replaces it is NIS monitoring
over time and cross-source consistency checks."

---

## 3. The Transmission vs. Distribution Contrast Table

| Dimension | Transmission SE | Distribution SE (DSSE) |
|-----------|----------------|----------------------|
| Measurement count | $m > n$ (over-determined) | $m \ll n$ (under-determined) |
| Gain matrix $G = H^\top WH$ | Full rank, invertible | Singular or near-singular |
| WLS unique solution | Yes | No (without additional priors/constraints) |
| Bad-data detection | Chi-squared / LNR works (has redundancy) | Mostly fails — no redundancy |
| Critical-measurement (leverage) trap | Exceptional; flagged and managed | **Standard operating condition** |
| Redundancy source | Space (dense sensors) | Time (temporal priors + recursion) |
| What fills the observability gap | More sensors | Topology priors + forecasts + zero-injections + ML |
| Filter structure | Often batch WLS (snapshot) | Recursive Kalman / FASE (borrows from time) |
| Comms gap behavior | Batch SE stops cold | Recursive filter inflates $P$ honestly, keeps running |
| Island-mode safety | Requires full measurement set | Recursive structure preserves estimate in island mode |

---

## 4. The Energy-Transition Double-Edge

DER penetration changes distribution SE in two directions simultaneously:

**Makes physics harder:**
- Bidirectional flows (net load can be negative during PV overvoltage events)
- Volatile, weather-coupled injections (PV output correlated with irradiance; EV charging
  correlated with time-of-day and events)
- Larger process uncertainty $Q$ — the diurnal profile is less predictable when DER is large
- Near-limit operation: 0.95–1.05 pu voltage corridor is violated by rooftop solar overvoltage
  at unmetered nodes — exactly the AGMS Worked Example 2 scenario

**Instruments the grid:**
- Every smart inverter is a real-time measurement point ($P$, $Q$, $V$ at its terminal)
- EV chargers (OCPP/MQTT) report load events
- Batteries (IEEE 1547 / 2030.5) self-report their state and can be queried
- AMI rollout extends metering to nearly every end-point (albeit at low rate)
- Grid-edge compute (FADs, gateways) enables local processing of that telemetry

**The virtual-sensing engineer's job:** net this out positive. Use the new instrumentation to
compensate for the harder physics. The AGMS Inspector scout on a FAD does exactly this: it
fuses the local DER telemetry with topology priors and temporal forecasts to maintain an
estimate even as the physics gets more volatile.

---

## 5. The Information-Budget Mental Model

For any under-instrumented distribution node, the state estimate is assembled from a budget:

| Information Source | Where it enters | Covariance |
|-------------------|----------------|-----------|
| Direct real-time measurement (inverter, μPMU) | Measurement $z$ with small $R$ | Small $R$ (high trust) |
| Feeder-head SCADA | Measurement $z$ via Kirchhoff $h(x)$ | Moderate $R$; broad coupling |
| Zero-injection constraint at known-passive node | Virtual measurement $z=0$, $R\to 0$ | Near-zero $R$ (hard constraint) |
| Network topology (who connects to whom) | Defines $H$ structure — Kirchhoff coupling lets head flow inform dark nodes | Structural (not stochastic) |
| Load cyclicality / diurnal profile | Process model `Bu` term (FASE predict step) | $Q$ = forecast uncertainty, time-indexed |
| ML load/PV forecast | Pseudo-measurement with calibrated covariance | $R_{pseudo}$ from forecast error archive |
| AMI (delayed, 15-min) | Low-rate measurement, applied with large $R$ | Large $R$ (noisy, stale) |
| EV charger telemetry (OCPP) | Event-driven measurement when present | Moderate $R$; absent between sessions |

The Kalman gain $K$ weights each source by its inverse covariance. High-quality, recent
inverter telemetry pulls hard; stale AMI pulls softly. The filter is the accountant; you
supply the line items with honest covariances.

**Interview sentence:** "The distribution information budget is topology coupling plus
zero-injection constraints plus temporal prior plus ML pseudo-measurements plus delayed AMI —
the filter weights each by its honest covariance. There is no single source that makes the node
observable; observability comes from the aggregate."

---

## 6. Why Recursion Beats Batch for Distribution

Classical transmission SE is a batch snapshot: gather all SCADA readings for one scan, solve
the WLS system, produce an estimate, discard, repeat. This works because measurement density
is high enough that each scan is independently observable.

Distribution uses a **recursive Kalman / FASE** structure because:

1. **Measurements arrive at different rates.** Inverter reports come every few seconds; AMI
   comes every 15 minutes; head SCADA is somewhere in between. The recursive filter handles
   this natively: run the predict step for each time gap, apply the update step on arrival.
2. **The prior from the previous step is itself an information source.** With $m \ll n$, the
   prior covariance $P_{k-1}$ contributes to the current-step observability — the history is
   informative in a way it never is in the transmission batch case.
3. **Comms gaps do not kill the estimate.** When measurements drop, the recursive predict step
   continues: $\hat x$ advances with the diurnal forecast and $P$ inflates honestly. The AGMS
   Asset Portfolio Manager 1300 sees $P$ growing and responds. The system degrades gracefully
   rather than failing hard.
4. **Island-mode safety.** The Inspector scout on a FAD can keep producing estimates even when
   the WAN is down. This is not an afterthought — it is the entire resilience bet of the AGMS
   architecture, and it falls out of the recursive filter's structure itself.

**Interview sentence:** "Batch WLS stops cold when the data feed breaks. The recursive Kalman
filter inflates $P$ honestly and keeps running — that is why island-mode safety falls out of
the filter's structure in AGMS."

---

## → Bridge to Juan's Work

<!-- greppable tag: Bridge to your work -->

| DSSE concept | Juan's work |
|-------------|------------|
| Information-sourcing problem | HEMS edge-ML: I source and fuse load/PV forecasts from multiple signals to produce calibrated probabilistic estimates — the same "find and characterize every source" discipline |
| Temporal prior / recursion | OSED edge runtime: recursive state propagation between measurements is how the HEMS MPC maintains a live building thermal state estimate even when some sensors drop |
| Topology prior (zero-injections, Kirchhoff $H$ structure) | SI-MAPPER ontology graph: encodes the structural constraints that define $H$ and identify zero-injection nodes |
| AMI vs. real-time fusion | My baseline-consumption analysis across billions of substation data points: the detect-and-correct loop for corrupted low-rate aggregate readings |

---

## Quick-Recall Card (Recite Before the Interview)

1. **Distribution states:** per-node $V$, $\theta$ (or injection $P$, $Q$) × 3 phases × $n$ nodes. States = hundreds to thousands.
2. **Distribution measurements:** feeder head + a few inverters + delayed AMI = $m \ll n$. $G$ singular.
3. **Under-determined result:** WLS has no unique solution without additional priors. Cannot even begin without augmentation.
4. **Bad-data detection:** chi-squared requires $m > n$ (degrees of freedom). LNR is blind to leverage measurements. Both mostly fail in distribution.
5. **Leverage/critical trap is normal:** remove any real-time sensor and a section goes unobservable. This is the default condition, not an edge case.
6. **Energy-transition double-edge:** DER = harder physics + more telemetry. Net out positive with virtual sensing.
7. **Information budget:** topology coupling + zero-injections + temporal prior + ML forecasts + AMI — each with honest $R$.
8. **Recursion beats batch:** multi-rate arrival, prior is informative, comms gaps handled gracefully, island-mode safe.
9. **Covariance = observability:** $P$ growing = ORACS Observability degrading; AGMS Asset Portfolio Manager 1300 gates on it.
10. **My bridge:** information-sourcing discipline from HEMS forecasting + SI-MAPPER topology + OSED runtime + baseline-error analysis.

---

*Sources: Monticelli, "State Estimation in Electric Power Systems" (1999) — classical SE, observability, bad-data; Abur & Expósito, "Power System State Estimation" (2004) — LNR, residual covariance; Dehghanpour et al., "A Survey on State Estimation Techniques and Challenges in Smart Distribution Systems" (IEEE Trans. Smart Grid, 2019) — DSSE under-observability, pseudo-measurements; AGMS patent (Director; Inspector scout, ORACS Observability, Asset Portfolio Manager 1300, island-mode resilience); GE Vernova JD R5043890 (virtual sensing, distribution, federated); 02-RESEARCH.md verified equations.*
