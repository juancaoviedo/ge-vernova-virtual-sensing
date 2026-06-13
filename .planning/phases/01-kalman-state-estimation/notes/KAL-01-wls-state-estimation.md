# KAL-01: WLS / Gauss-Newton Power-System State Estimation

**For:** Oral rehearsal — speak each section aloud before the interview.
**Purpose:** Close the vocabulary gap on state estimation so you can engage the interviewer's
questions on Kalman, WLS, and observability with specifics, not generalities.

---

## 1. What WLS State Estimation Is (Mental Model First)

The grid is running right now. Thousands of sensors — SCADA meters, PMUs, current
transformers — are feeding the control center with noisy, redundant readings. None of them
directly tells you the exact voltage or phase angle at every bus. **State estimation is the
algorithm that takes that noisy, redundant sensor soup and produces the single best consistent
picture of what the grid is actually doing.**

The state vector captures everything you need to know:

$$x = [V_1,\, \theta_1,\, V_2,\, \theta_2,\, \ldots,\, V_n,\, \theta_n]$$

Voltage magnitude $V_i$ and phase angle $\theta_i$ at every one of $n$ buses. Once you know $x$, you can
compute every power flow, every current injection — the full operating point falls out of the
AC power-flow equations.

The **measurement model** relates the hidden state to what sensors actually report:

$$z = h(x) + e$$

- $z$ = vector of $m$ measurements (bus voltages, real/reactive power flows, current magnitudes)
- $h(x)$ = the nonlinear AC power-flow equations mapping state to observables
- $e$ = measurement errors: $e \sim \mathcal{N}(0, R)$, Gaussian with covariance $R$

$R$ is diagonal: each sensor has its own noise variance. A high-accuracy PMU gets a small $R$ entry;
a legacy SCADA meter with loose calibration gets a large one.

**One-liner for the interview:** "State estimation answers: given all these noisy, redundant
SCADA readings, what is the most consistent operating point that best explains all of them?"

---

## 2. The WLS Objective Function

We want the estimate $\hat{x}$ that minimizes the **weighted sum of squared residuals**:

$$J(x) = [z - h(x)]^\top W\, [z - h(x)]$$

where $W = R^{-1}$ — the weight matrix is the inverse of the noise covariance. A more trustworthy
sensor (small $R_{ii}$) gets higher weight $W_{ii} = 1/R_{ii}$; a noisy legacy meter gets low weight.

This is exactly **least squares** with per-measurement trust. When all sensors are equally
trusted ($W = I$), it collapses to ordinary least squares. The WLS version is what every
production energy management system (EMS) runs.

**Key intuition:** You are not minimizing the number of wrong measurements — you are minimizing
the energy of the residuals in a space where trustworthy sensors pull harder.

---

## 3. The Gauss-Newton Iteration (How You Actually Solve It)

$h(x)$ is nonlinear (AC power flow involves sines and cosines of phase angles). So $J(x)$ has no
closed-form minimum. We solve iteratively using Gauss-Newton:

**At each iteration, starting from current estimate $\hat{x}$:**

**Step 1 — Linearize.** Compute the Jacobian of $h$ at the current estimate:

$$H = \frac{\partial h}{\partial x}\bigg|_{\hat{x}}$$

$H$ has shape $m \times 2n$ ($m$ measurements, $2n$ states). Each row says: "how does measurement $i$ change
when state $j$ changes by a tiny amount?"

**Step 2 — Form the gain matrix (information matrix):**

$$G = H^\top W H$$

$G$ is $2n \times 2n$. It captures how much information the current measurements give you about each
state variable. A well-conditioned $G$ means the grid is observable.

**Step 3 — Compute the state correction:**

$$\Delta x = G^{-1} H^\top W\, [z - h(\hat{x})]$$

The bracketed term $[z - h(\hat{x})]$ is the current residual — the gap between what we measured
and what our current estimate predicts. We correct the estimate to close that gap, weighted
by sensor trust.

**Step 4 — Update and check convergence:**

$$\hat{x} \leftarrow \hat{x} + \Delta x$$

Repeat until $\|\Delta x\| < \text{tolerance}$. In practice, a well-initialized power-system SE converges in
**2–4 iterations**. The operating point from the previous scan is almost always a good starting
point, so convergence is fast.

---

## 4. Interview Vocabulary (The Terms You Must Own)

### Observability

The grid is **observable** when $H$ has full column rank — there are enough independent
measurements to uniquely determine all state variables. In graph terms: every bus must have
at least one incident measurement (voltage or a power flow on a connected branch).

If a portion of the grid has no measurements (and no measured branches connecting it to the
rest), it forms an **unobservable island** — SE cannot determine those bus voltages. The EMS
flags this and either uses historical data or skips that region.

**Interview sentence:** "Observability is about whether the Jacobian $H$ has full column rank —
whether the measurement set is rich enough to uniquely pin down every state variable."

### Residuals

After WLS converges, the **residuals** are:

$$r = z - h(\hat{x})$$

Small residuals across the board = the estimate is consistent with all measurements. A large
residual on one measurement flags a potential bad sensor.

### Bad-Data Detection: Chi-Squared Test

After convergence, the weighted residual sum $J(\hat{x}) = r^\top W r$ follows a **chi-squared
distribution** with $m - n$ degrees of freedom ($m$ measurements minus $n$ states = degrees of
redundancy). If:

$$J(\hat{x}) > \chi^2_{\text{threshold}}(m - n,\; 0.95)$$

...at least one measurement is bad. The **Largest Normalized Residual (LNR) test** then
identifies the culprit: compute $r_i / \sqrt{\Omega_{ii}}$ for each measurement $i$ (where $\Omega_{ii}$ is the
diagonal of the residual covariance matrix); the measurement with the largest normalized
residual is the prime suspect. Remove it and re-run SE.

### The Critical Limitation: Leverage Measurements

Here is the trap that interviewers who have built real SE systems will probe:

**Leverage measurements** are measurements at buses that, if removed, would render that bus
(or a subsection of the grid) unobservable. Because the SE solution depends entirely on
them, their normalized residual is always near zero — even when the measurement is corrupted.

Think about it: if a bus voltage measurement is the *only* thing anchoring that bus, the SE
will fit its estimate to that reading no matter what. A bad reading does not create a large
residual; it just gives you a wrong state estimate that looks perfectly consistent.

**Interview sentence:** "The LNR test has a structural blind spot: leverage measurements at
sparsely instrumented buses have near-zero normalized residuals even when corrupted, because
the estimator has no independent measurement to contradict them. That is the key limitation
of chi-squared bad-data detection, and it motivates redundant measurement placement at
critical buses."

---

## 5. Static vs. Dynamic State Estimation

**WLS is a snapshot estimator.** It processes one scan of SCADA data — typically a 4-second
update cycle — and produces one operating-point estimate. There is no memory of the previous
scan; each solve is independent.

This is fine for slowly-varying transmission conditions but becomes limiting when:

- You have **PMU data** at 30–120 Hz and want to track rapid transients
- You want to estimate dynamic variables (generator rotor angles, frequencies) that evolve
  between SCADA scans
- You need to predict the state one step ahead (e.g., for model-predictive control or DLR)

**Dynamic state estimation** (KF/EKF/UKF-based) adds a **time dimension**: a predict step
propagates the state estimate forward using a physics model, then an update step corrects it
with incoming measurements. This is what KAL-02 covers.

**Transition sentence:** "WLS gives you the best static snapshot; Kalman-based dynamic SE
gives you a running film with uncertainty quantification at every frame."

---

## 6. OSED Bridge: The Convex Optimization Connection

<!-- greppable tag: WLS convex -->

This is the link that makes your experience directly relevant and differentiates you from
candidates who learned SE from a textbook:

> **"OSED's convex optimization formulates a quadratic objective over building state variables
> from sensor measurements — same minimize-weighted-squared-residuals logic, just swapping
> AC power-flow for an RC thermal model."**

Unpacking the structural isomorphism:

| Power-System WLS | OSED Convex Optimization |
|-----------------|--------------------------|
| State vector $x = [V,\, \theta]$ per bus | State vector $= [T_\text{zone},\, P_\text{HVAC},\, \ldots]$ per building |
| Measurement model $z = h(x) + e$ | Sensor model $y = Cx + e$ |
| Objective: $\min [z-h(x)]^\top W [z-h(x)]$ | Objective: $\min [y-Cx]^\top R^{-1} [y-Cx] + \text{regularization}$ |
| Nonlinear $h$ → Gauss-Newton | Linear $C$ → closed-form or CVXPY |
| Measurement noise $R$ from sensor specs | Noise $R$ from building sensor calibration |
| Observable = $H$ full column rank | Observable = $C$ full column rank |

The mathematical logic — minimize weighted squared residuals to get the best consistent
estimate from redundant noisy sensors — is identical. The grid version is more complex because
$h(x)$ is nonlinear (requires Gauss-Newton iteration), while the building version is linear
(RC thermal model), so it solves in one shot with CVXPY.

**How to say this in the interview:**

> "I have implemented the WLS objective in a different physical domain: OSED's building thermal
> state estimator minimizes a weighted least-squares objective over zone temperatures and HVAC
> states using building management system sensor readings. The math is structurally identical
> to power-system WLS. The difference is that my measurement function $h(x)$ is linear in
> building temperatures — the RC thermal model is linear — whereas the grid version is
> nonlinear in voltage angles, which is why it needs Gauss-Newton iteration instead of a
> closed-form solve."

---

## Quick-Recall Card (Recite Before the Interview)

1. **State vector:** $x = [V,\, \theta]$ per bus — WLS finds the best consistent $x$.
2. **Measurement model:** $z = h(x) + e$; $h$ is nonlinear AC power flow; $e \sim \mathcal{N}(0, R)$.
3. **Objective:** minimize $J(x) = [z - h(x)]^\top R^{-1} [z - h(x)]$.
4. **Gauss-Newton:** linearize $H = \partial h/\partial x$ → gain $G = H^\top W H$ → correction $\Delta x = G^{-1} H^\top W [z - h(\hat{x})]$ → iterate 2–4 times.
5. **Observability:** $H$ full column rank; unobservable islands if buses have no incident measurements.
6. **Bad data:** $J(\hat{x}) \sim \chi^2(m-n)$; LNR test finds the suspect measurement.
7. **Leverage measurement trap:** near-zero normalized residual even when corrupted — structural blind spot of LNR.
8. **Static vs. dynamic:** WLS = 4-second snapshot; KF/EKF = running estimate with time propagation.
9. **My bridge:** OSED convex optimization IS structurally WLS — same minimize-weighted-residuals logic, linear RC model instead of nonlinear AC power flow.

---

*Sources: arXiv 2502.18229 (JuliaGrid WLS); ResearchGate 329665834 (WLS framework); 01-RESEARCH.md verified equations*
