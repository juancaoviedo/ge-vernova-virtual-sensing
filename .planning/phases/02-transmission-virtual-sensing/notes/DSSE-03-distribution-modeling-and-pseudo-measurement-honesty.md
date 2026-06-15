# DSSE-03: Distribution-Specific Modeling & the Pseudo-Measurement Honesty Problem

**For:** Oral rehearsal — speak the branch-current formulation and the pseudo-measurement
honesty argument aloud; these are the modeling decisions that separate distribution SE from
a textbook WLS exercise.
**Purpose:** Cover the three distribution-specific modeling choices (three-phase unbalanced /
radial / high R/X; branch-current formulation; LinDistFlow) and the pseudo-measurement
honesty problem that is the make-or-break for whether the DSSE is trustworthy in practice.
Salvage the observability rank test and chi-squared/LNR machinery — but state plainly why
they largely fail in distribution and what actually replaces them.

---

## <3-min say-aloud version

> "Distribution grids are structurally different from transmission in three ways that matter for
> state estimation. First, feeders are **radial** — no mesh, no loops, so you have a tree structure
> rather than a cycle-rich network. Second, lines are **unbalanced** (three phases with different
> loads on each) and have **high R/X ratios** — resistance is comparable to reactance, so the
> lossless and small-angle approximations that make DC power flow work on transmission are badly
> wrong on distribution. Third, **phase angles across short feeders are tiny** — fractions of a
> degree — so inferring angles from power flow is ill-conditioned. μPMUs / D-PMUs that measure
> angle directly with GPS synchronization are the solution, and they appear explicitly in the
> job description.
>
> For the power flow model, the **branch-current formulation** (Baran and Kelley) is better
> conditioned for radial feeders than the bus-injection formulation: work in branch currents along
> the tree rather than bus voltages, exploit the radial structure directly. Voltage recovery uses
> **LinDistFlow** — the linear branch-flow approximation that works well for radial, low-voltage
> feeders with high R/X.
>
> The critical practical issue is pseudo-measurements. Pseudo-measurements are what restore
> *solvability* to the under-determined DSSE — without them the gain matrix is singular. But
> restoring solvability is NOT the same as restoring information. A pseudo-measurement is a guess.
> The whole ballgame is honest, calibrated uncertainty on that guess. Assign a covariance that is
> too small and the pseudo-measurement becomes a leverage measurement at scale — the filter trusts
> it blindly, cannot self-correct, and silently produces wrong estimates. The residual is near-zero
> not because the estimate is right but because the filter has been told to believe it. This is the
> chi-squared blind spot generalized from a single sensor to an entire load model."

---

<!-- greppable tag: branch current Baran Kelley -->

## 1. Three-Phase Unbalanced, Radial, High R/X — Why Distribution Is Different

### Three-Phase Unbalanced

Transmission networks are balanced (or nearly so) — three phases carry equal loads, so single-
phase equivalent models work well. Distribution feeders are **intentionally unbalanced**: single-
phase laterals, asymmetric loading (residential loads connect to one phase), unequal conductor
geometries. A three-phase distribution DSSE must track per-phase voltage and injection separately:

$$x = [V_{a,1}, V_{b,1}, V_{c,1}, \theta_{a,1}, \theta_{b,1}, \theta_{c,1}, \ldots]^\top$$

State dimension: $6n$ for $n$ three-phase buses. Even more states; even more under-determined.

**Interview awareness:** If the interviewer asks about three-phase modeling, state: "Distribution
is inherently unbalanced and requires per-phase tracking. Single-phase equivalents lose the
inter-phase coupling that matters for voltage unbalance monitoring — a JD-mentioned concern."

### High R/X Ratio

Transmission lines: $r \ll x$ (reactance dominates). The DC power-flow approximation assumes
$r = 0$; losses are negligible. Works well on transmission.

Distribution lines: $r \approx x$ or $r > x$ (resistance is comparable to or dominates reactance).
The DC approximation fails:
- Real-power flow depends significantly on both resistance and angle
- Reactive power contributes substantially to voltage drops
- The lossless-line assumption produces large voltage-estimation errors

**Consequence for DSSE:** Cannot use $P = B\theta$ (the susceptance-Laplacian model). Must use
a formulation that handles resistance explicitly. The **branch-current** formulation and
**LinDistFlow** are the standard choices.

### Radial Topology

Distribution feeders are radial (tree-structured, no loops) for operational simplicity and fault
isolation. This is a structural property that can be exploited:
- The radial tree structure means there is a unique path from the substation to each node
- Branch currents flow one-directionally (toward the loads) in normal operation (reversed only
  by DER overvoltage events)
- The branch-current Baran-Kelley equations are simpler to set up than the bus-injection
  formulation for trees

---

## 2. The Branch-Current Formulation (Baran-Kelley)

For a radial feeder, work in **branch currents** $I_{branch}$ along the tree rather than bus
voltages $V$. The advantage: the radial structure means each branch current is uniquely
determined by the downstream load sum (no Kirchhoff-matrix inversion needed). The formulation
is better conditioned numerically for distribution.

**The LinDistFlow model (simplified branch-flow for radial feeders):**

For a branch from bus $i$ to bus $j$ with resistance $r_{ij}$ and reactance $x_{ij}$, carrying
real power $P_{ij}$ and reactive power $Q_{ij}$:

$$V_j^2 \approx V_i^2 - 2(r_{ij}\,P_{ij} + x_{ij}\,Q_{ij})$$

Linearizing around a flat voltage profile ($V \approx 1.0$ pu, $V^2 \approx 2V - 1$):

$$V_j \approx V_i - r_{ij}\,P_{ij} - x_{ij}\,Q_{ij}$$

This is **LinDistFlow** — a linear relationship between bus voltages and branch power flows,
holding for radial, low-voltage feeders where the nonlinear terms in $V^2$ are small. It is
the distribution analog of DC power flow, but it retains resistance (crucial for high-R/X feeders).

**Why this matters for DSSE:** LinDistFlow gives you a *linear* measurement model $h(x)$ for
the voltage-to-injection relationship. It allows a Kalman / FASE update step without EKF
Jacobian computation (the model is already linear) — trading some accuracy for tractability.
Model error from the linearization absorbs into a larger $Q$ in the process model.

**Interview sentence:** "LinDistFlow is the distribution analog of DC power flow — it's linear,
accounts for resistance (unlike DC power flow), and works well on radial feeders. Modeling error
from the linearization absorbs into $Q$, not into wrong $H$ entries."

---

<!-- greppable tag: microPMU angle -->

## 3. Phase Angles Are Hard in Distribution — μPMUs Are the Solution

In transmission, voltage angles span several degrees across a long line ($\theta_1 - \theta_2 \approx$
5–10°). The DC power-flow approximation gives small-angle sine $\approx$ argument — a good
approximation.

In distribution, the angle difference across a short, low-voltage feeder is tiny:
$\theta_1 - \theta_2 \approx 0.01$–0.1° in many cases. The consequences:

1. **Ill-conditioned angle estimation from power flow.** A 1% error in a measured power flow
   can produce a huge relative error in the inferred angle. The angle sensitivity $\partial P / \partial \theta$
   is high, so $\partial \theta / \partial P$ is tiny — small power measurement noise translates to
   large angle uncertainty.
2. **Reactive power / voltage coupling is dominant.** On high-R/X feeders, $V$ drops are driven
   more by $Q$ flows than by angle differences. Angle inference from voltage magnitudes is nearly
   impossible without angle measurements.

**μPMU / D-PMU solution:** Micro-Phasor Measurement Units deployed at distribution substations
and key feeder nodes measure **voltage phasor magnitude AND angle directly**, GPS-synchronized to
sub-microsecond accuracy. IEEE C37.118 protocol, adapted for distribution (D-PMU).

With μPMU measurements:
- Angles become direct observations $z = \theta$ rather than inferred quantities
- The ill-conditioning of angle estimation disappears
- Observability of the feeder is dramatically improved even with sparse μPMU placement

**Why this is in the JD:** "Phase angles" appears explicitly in the GE Vernova JD. The reason is
that distribution angle estimation is the hard problem, and μPMUs are the emerging solution —
understanding this positions you as distribution-aware, not just transmission-aware.

**Interview sentence:** "Phase angles across a short distribution feeder are tiny — fractions of
a degree — so inferring them from power flow is ill-conditioned. μPMUs measure angle directly
with GPS synchronization, which is why they appear in the JD as the key new sensing technology
for distribution observability."

---

<!-- greppable tag: pseudo-measurement honesty -->

## 4. Pseudo-Measurements Restore Solvability, Not Information

**What pseudo-measurements are:** When $m \ll n$ and $G$ is singular, you cannot solve the DSSE.
You inject **pseudo-measurements** — values for state variables derived not from sensors but from
load models, historical profiles, or ML forecasts — to make the system nominally over-determined.
The most common pseudo-measurement is a load estimate: "bus 42 is a residential node, typical
load at this time is 8 kW, uncertainty ±5 kW."

**The solvability/information distinction:**

> Pseudo-measurements restore SOLVABILITY, not INFORMATION.

Making the gain matrix $G$ full-rank via pseudo-measurements gives you a solution. It does NOT
give you ground-truth measurements. The solution is only as good as the pseudo-measurement
model — and that model is a guess, calibrated from historical data, subject to errors that no
sensor can detect in real time.

**The honest covariance is everything.** If you set $R_{pseudo}$ too small:
- The filter trusts the pseudo-measurement as if it were a direct sensor
- No measurement can contradict it (Kalman gain for real measurements shrinks)
- The filter produces a smooth, internally consistent estimate that is wrong in a systematic way
- Bad pseudo-measurements produce no innovation residual — they are invisible to chi-squared

This is the **critical-measurement trap generalized to load models**: one overconfident model
corrupting the entire feeder estimate, invisible to detection, because it has been assigned
near-zero $R$.

**The correct calibration chain:**
1. Run the load model on historical data; compare predicted to measured (from AMI when available)
2. Estimate empirical forecast-error distribution per time-slot, season, weather
3. Set $R_{pseudo}$ to the empirical variance (not the model's self-reported confidence)
4. Update as model evolves (Learning Engine calibration request in AGMS)

**Interview sentence:** "Pseudo-measurements restore solvability, not information. An overconfident
pseudo-measurement — too small $R_{pseudo}$ — becomes a leverage measurement at scale: the filter
trusts it blindly, and a systematic model error is invisible to chi-squared detection. Honest
calibration of $R_{pseudo}$ from the empirical forecast-error archive is the most important
discipline in distribution DSSE design."

---

## 5. Salvaging the Classic Observability / Bad-Data Machinery — What Still Works

The observability rank test and residual-based bad-data detection machinery from classical SE are
not useless in distribution — they need to be applied appropriately with awareness of their limits.

### Observability Rank Test (Still Useful)

The condition $\text{rank}(H) = n$ (or equivalently, $G = H^\top W H$ nonsingular) remains the
definition of observability. In DSSE:

- Use it to **assess before running** whether the augmented measurement set (real sensors +
  pseudo-measurements + zero-injections) is nominally full-rank
- Identify which nodes are still unobservable even with pseudo-measurements
- Guide μPMU / sensor placement to achieve full observability

$$\text{Observable (nominally)} \iff \text{rank}(H) = n$$

In Python: `numpy.linalg.matrix_rank(H) == n`. Note: with pseudo-measurements padded in, this
will often be true by construction — but "nominally observable" and "well-observed" are different
things. $\text{rank}(H) = n$ with $H$ rows from highly uncertain pseudo-measurements gives poor
estimates despite the rank condition passing.

### Residual Covariance (Still Definable)

$$\Omega = R - H\,G^{-1}\,H^\top$$

The diagonal $\Omega_{ii}$ is the expected residual variance for measurement $i$. The
normalized residual $r_i^N = |r_i| / \sqrt{\Omega_{ii}}$ is still formally definable.

### Why Chi-Squared / LNR Mostly Fails in Distribution

1. **No real redundancy.** With real sensors at $m < n$, there are no degrees of freedom. The
   chi-squared test requires $m - n > 0$.
2. **Pseudo-measurements are not independent sensors.** Padding with pseudo-measurements creates
   apparent redundancy, but a wrong pseudo-measurement is a biased prior, not a random measurement
   error. Chi-squared tests for random Gaussian errors — systematic model bias evades it.
3. **Near-zero residuals by design.** Leverage pseudo-measurements have near-zero residuals when
   the filter commits to them. A systematically wrong load model looks consistent.

### What Actually Works for Distribution Bad-Data / Quality Monitoring

| Technique | What it detects | When to use |
|-----------|----------------|-------------|
| **Innovation / NIS monitoring over time** ($y_k^\top S_k^{-1} y_k \sim \chi^2(m_k)$) | Filter diverging (model wrong, sensor failed, topology changed) | Continuously; sustained NIS > threshold = problem |
| **Cross-source consistency check** | AMI vs. pseudo-measurement vs. inverter tell conflicting stories | When AMI arrives; compare to filter prediction at that interval |
| **Prediction-error analysis** | ML forecasts consistently off in one direction | Offline; feeds Learning Engine recalibration |
| **Topology change detection** | Sudden jump in innovation after feeder reconfiguration | Monitor for NIS spikes; cross-reference with switching events |

**Interview sentence:** "Chi-squared bad-data detection relies on redundancy that distribution
doesn't have. What replaces it is NIS monitoring over time — if the sequential innovation is not
white and zero-mean, the model is wrong or a sensor failed — plus cross-source consistency when
multiple sources cover the same interval."

---

## 6. The DSSE Modeling Choice Decision Tree

When setting up a distribution DSSE, the key modeling decisions in order:

1. **Single-phase equivalent or three-phase?** → Three-phase for voltage unbalance monitoring;
   single-phase adequate for aggregate load estimation.
2. **Bus-injection (WLS) or branch-current (Baran-Kelley)?** → Branch-current for radial feeders;
   better conditioned, exploits tree structure.
3. **Full nonlinear power flow (EKF) or LinDistFlow (linear KF)?** → LinDistFlow for tractability
   on radial feeders; model error absorbs into $Q$.
4. **How many pseudo-measurements needed?** → Enough to nominally satisfy $\text{rank}(H) = n$;
   prioritize real sensors and zero-injections first; fill with ML pseudo-measurements last.
5. **How are $R_{pseudo}$ set?** → From empirical forecast-error archive, never from model self-
   confidence scores.
6. **μPMU placement?** → At feeder head and key junctions to anchor angle estimates; use
   observability analysis to identify highest-leverage placement.

---

## → Bridge to Juan's Work

<!-- greppable tag: Bridge to your work -->

| DSSE-03 concept | Juan's work |
|----------------|------------|
| LinDistFlow linear model | OSED uses linear RC thermal model — same tradeoff: linear approximation, absorb model error into noise covariance, tractable Kalman |
| Pseudo-measurement calibration from error archive | HEMS ML forecasting: I archive prediction vs. actual, estimate empirical forecast error distribution, and use it to set uncertainty in downstream models — exactly the $R_{pseudo}$ calibration chain |
| Innovation / NIS monitoring for bad-data | My baseline-consumption error analysis: I monitored residuals across billions of substation data points to detect corrupted readings — the same NIS-over-time discipline at production scale |
| Three-phase unbalance awareness | Not directly built, but SI-MAPPER's per-device ontology graph can represent per-phase topology — the structural prior extends naturally to three-phase |

---

## Quick-Recall Card (Recite Before the Interview)

1. **Three-phase unbalanced:** per-phase tracking; $6n$ states; single-phase equivalents lose inter-phase coupling.
2. **High R/X:** DC power flow fails (assumes $r=0$); use branch-current (Baran-Kelley) or LinDistFlow.
3. **Radial topology:** tree structure; branch-current formulation exploits it; better conditioned than bus-injection for distribution.
4. **LinDistFlow:** $V_j \approx V_i - r_{ij}P_{ij} - x_{ij}Q_{ij}$; linear; retains resistance; model error → larger $Q$.
5. **Phase angles in distribution:** tiny (fractions of a degree across short feeders); ill-conditioned to infer from power flow; μPMU / D-PMU measure angle directly with GPS — the key JD-mentioned sensing technology.
6. **Pseudo-measurements:** restore solvability, NOT information. The guess is not a measurement.
7. **Honest $R_{pseudo}$:** from empirical forecast-error archive; overconfident $R_{pseudo}$ → leverage trap at scale → filter goes deaf to real measurements.
8. **Observability rank test:** $\text{rank}(H) = n$ with pseudo-measurements padded ≠ well-observed. Use it for sensor placement guidance.
9. **Residual covariance:** $\Omega = R - HG^{-1}H^\top$; LNR = $|r_i|/\sqrt{\Omega_{ii}}$; formally definable but leverage residuals are near-zero even when wrong.
10. **Chi-squared / LNR in distribution:** mostly fails — no redundancy; pseudo-measurement bias evades Gaussian residual tests.
11. **What works:** NIS monitoring over time + cross-source consistency checks + offline prediction-error analysis feeding Learning Engine.

---

*Sources: Baran & Kelley, "Network reconfiguration in distribution systems for loss reduction and load balancing" (IEEE Trans. Power Delivery, 1989) — branch-current formulation and LinDistFlow; Kersting, "Distribution System Modeling and Analysis" (2012) — three-phase distribution modeling, high R/X; Monticelli, "State Estimation" (1999) — observability rank test, residual covariance; Abur & Expósito (2004) — LNR, leverage measurements; Von Meier et al., "Precision micro-synchrophasors for distribution systems" (IEEE Trans. Smart Grid, 2017) — μPMU / D-PMU; Dehghanpour et al. (IEEE Trans. Smart Grid, 2019) — pseudo-measurement methods; AGMS patent (Director; Learning Engine, ORACS Observability); GE Vernova JD R5043890 (phase angles, virtual sensing); 01-RESEARCH.md verified equations.*
