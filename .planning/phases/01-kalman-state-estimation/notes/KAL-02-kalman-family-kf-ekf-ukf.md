# KAL-02: Kalman Filter Family — KF, EKF, UKF

**For:** Oral rehearsal — speak the equations aloud; you must be able to recite the
predict-update cycle and name what each matrix means without looking at notes.
**Purpose:** Provide the exact mathematical progression you need to demonstrate Kalman
depth in the interview, including EKF Jacobians, UKF sigma points, a decision table,
and the Q/R tuning + divergence detection that separates practitioners from theorists.

---

## 1. Linear Kalman Filter (KF)

The Kalman Filter is the **optimal recursive estimator for linear-Gaussian systems**. Optimal
means minimum mean-squared error among all linear estimators when the noise is Gaussian and
the dynamics are linear. Two stages: **Predict** (extrapolate using the physics model) and
**Update** (correct with the new measurement).

### State-Space Model

$$\begin{aligned}
x_k &= F\, x_{k-1} + B\, u_k + w_k & &(w_k \sim \mathcal{N}(0, Q)) \\
z_k &= H\, x_k + v_k               & &(v_k \sim \mathcal{N}(0, R))
\end{aligned}$$

- $x_k$ = state vector at time $k$
- $F$ = state transition matrix (physics: how the state evolves one step)
- $B$ = control input matrix; $u_k$ = known input (e.g., load dispatch)
- $Q$ = process noise covariance (uncertainty in the model)
- $H$ = measurement matrix (which linear combination of states you observe)
- $R$ = measurement noise covariance (sensor uncertainty)

### Predict Step

$$\begin{aligned}
\hat{x}_{k|k-1} &= F\, \hat{x}_{k-1|k-1} + B\, u_k \\
P_{k|k-1}       &= F\, P_{k-1|k-1}\, F^\top + Q
\end{aligned}$$

"Predicted" means: we have not yet seen measurement $z_k$. We propagate our best estimate
forward using the dynamics model. $P$ grows because the model adds uncertainty ($Q$).

### Update Step

$$\begin{aligned}
y_k            &= z_k - H\, \hat{x}_{k|k-1} \\
S_k            &= H\, P_{k|k-1}\, H^\top + R \\
K_k            &= P_{k|k-1}\, H^\top S_k^{-1} \\
\hat{x}_{k|k}  &= \hat{x}_{k|k-1} + K_k\, y_k \\
P_{k|k}        &= (I - K_k H)\, P_{k|k-1}
\end{aligned}$$

The innovation $y_k$ is the actual measurement minus the predicted measurement.

### Kalman Gain Intuition

$K_k$ balances two sources of information:

- If **$R$ is large** (noisy sensor) → $S$ is large → $K$ is small → trust the model more, move
  only a little toward the measurement.
- If **$P$ is large** (model is uncertain) → $K$ is large → trust the sensor more, move a lot
  toward the measurement.
- Perfect sensor ($R \to 0$): $K \to H^{-1}$, $\hat{x} \to z$ (ignore model entirely).
- Perfect model ($Q \to 0$, $P \to 0$): $K \to 0$, $\hat{x}$ stays at prediction (ignore sensor).

**Interview sentence:** "Kalman gain is the auto-tuned weight that decides, at each step,
whether to trust the physics model more or the sensor more. It is derived from their
relative uncertainties $P$ and $R$."

---

## 2. Extended Kalman Filter (EKF)

Use EKF when $f(\cdot)$ or $h(\cdot)$ is **nonlinear**. The EKF linearizes these functions at each
step using a first-order Taylor expansion — i.e., it computes Jacobian matrices.

### Nonlinear State-Space

$$\begin{aligned}
x_{k+1} &= f(x_k, u_k) + w_k \\
z_k     &= h(x_k) + v_k
\end{aligned}$$

$f$ and $h$ are arbitrary differentiable functions. For grid dynamic state estimation, $f$ might be
the swing equation; $h$ might be the AC power-flow equations.

### EKF Predict Step

$$\begin{aligned}
\hat{x}_{k+1|k} &= f(\hat{x}_{k|k},\, u_k) \\
A_k             &= \frac{\partial f}{\partial x}\bigg|_{\hat{x}_{k|k}} \\
P_{k+1|k}       &= A_k\, P_{k|k}\, A_k^\top + Q
\end{aligned}$$

**What the Jacobian $A$ does:** The true nonlinear $f$ curves away from a straight line; $A$ is
the best linear approximation at the current point. Covariance (uncertainty ellipsoid) is
propagated using that linear approximation.

### EKF Update Step

$$\begin{aligned}
H_k               &= \frac{\partial h}{\partial x}\bigg|_{\hat{x}_{k+1|k}} \\
y_k               &= z_k - h(\hat{x}_{k+1|k}) \\
S_k               &= H_k\, P_{k+1|k}\, H_k^\top + R \\
K_k               &= P_{k+1|k}\, H_k^\top S_k^{-1} \\
\hat{x}_{k+1|k+1} &= \hat{x}_{k+1|k} + K_k\, y_k \\
P_{k+1|k+1}       &= (I - K_k H_k)\, P_{k+1|k}
\end{aligned}$$

Same structure as the linear KF update, but $H$ is now the Jacobian of $h$ rather than a
constant matrix. The innovation $y_k$ is computed using the true nonlinear $h$.

### When EKF Fails

This is a common interview probe — know these failure modes:

1. **Highly nonlinear model:** If $f$ or $h$ has strong curvature, the first-order Jacobian
   approximation is poor. The filter may diverge (state estimate drifts away from truth).

2. **Ill-conditioned Jacobian near voltage collapse:** Power-flow Jacobians become
   near-singular near the stability limit (large phase angle differences, nose curve tip).
   $A_k$ or $H_k$ can have very large entries, making $P$ propagation numerically unstable.

3. **Positive-feedback divergence:** As $P$ grows (model drifts), the linearization point $\hat{x}$
   moves away from the true state, making the Jacobian computed at $\hat{x}$ an even worse
   approximation of $f$ at the true $x$. This worsens the estimate further — a runaway loop.

**Interview sentence:** "EKF linearizes via Jacobian. When the system is strongly nonlinear,
the Jacobian is a poor local approximation, and the error compounds step-by-step until the
filter diverges. That is when you reach for the UKF."

---

## 3. Unscented Kalman Filter (UKF)

The UKF avoids Jacobian computation entirely. Instead of linearizing, it propagates a
carefully chosen set of deterministic sample points — called **sigma points** — through the
true nonlinear function. The propagated sigma points are then recombined to recover the
posterior mean and covariance.

**Why this is better:** The sigma-point set captures the mean and covariance of the prior
distribution exactly. After propagation through the true nonlinear $f$, the recombined
statistics are accurate to **third order** (vs. first order for EKF). No Jacobian derivation
required.

### Sigma Point Generation

For an $n$-dimensional state $\hat{x}$ with covariance $P$, generate $2n + 1$ sigma points:

$$\begin{aligned}
\chi_0    &= \hat{x} \\
\chi_i    &= \hat{x} + \left(\sqrt{(n + \lambda)\, P}\right)_i  & i &= 1,\ldots,n \\
\chi_{n+i}&= \hat{x} - \left(\sqrt{(n + \lambda)\, P}\right)_i  & i &= 1,\ldots,n
\end{aligned}$$

$$\lambda = \alpha^2(n + \kappa) - n \qquad \text{(composite scaling parameter)}$$

$\left(\sqrt{(n + \lambda)\, P}\right)_i$ means the $i$-th column of the matrix square root, scaled by $\sqrt{n + \lambda}$.

### UKF Parameters ($\alpha$, $\beta$, $\kappa$)

- **$\alpha$ (alpha):** Controls the spread of sigma points around the mean. Typical: 0.001 to 0.1.
  Larger $\alpha$ → wider spread → captures more of the nonlinearity, but also brings in
  higher-order errors (can cause $P$ to lose positive-definiteness for highly non-Gaussian).
- **$\beta$ (beta):** Encodes prior knowledge of the state distribution shape. $\beta = 2$ is optimal
  for Gaussian distributions (minimizes the 4th-order error term).
- **$\kappa$ (kappa):** Secondary scaling. Common choices: $\kappa = 0$ or $\kappa = 3 - n$.

**Interview sentence:** "Alpha controls how far you spread sigma points from the mean. Beta
= 2 is optimal for Gaussian priors. Kappa is usually set to zero or three minus $n$."

### UKF Predict Step

$$\begin{aligned}
\tilde{\chi}_i      &= f(\chi_i,\, u) \\
\hat{x}_{k+1|k}    &= \sum_i W_i^m\, \tilde{\chi}_i \\
P_{k+1|k}          &= \sum_i W_i^c\, (\tilde{\chi}_i - \hat{x})(\tilde{\chi}_i - \hat{x})^\top + Q
\end{aligned}$$

Weights $W_i^m$ (mean) and $W_i^c$ (covariance) are determined by $\alpha$, $\beta$, $\kappa$. The zeroth sigma point
(the mean itself) gets higher weight; the symmetric pairs get equal weight.

### UKF Update Step

$$\begin{aligned}
\gamma_i             &= h(\tilde{\chi}_i) \\
\hat{z}_{k+1|k}     &= \sum_i W_i^m\, \gamma_i \\
P_{zz}              &= \sum_i W_i^c\, (\gamma_i - \hat{z})(\gamma_i - \hat{z})^\top + R \\
P_{xz}              &= \sum_i W_i^c\, (\tilde{\chi}_i - \hat{x})(\gamma_i - \hat{z})^\top \\
K                   &= P_{xz}\, P_{zz}^{-1} \\
\hat{x}_{k+1|k+1}   &= \hat{x}_{k+1|k} + K\,(z_{k+1} - \hat{z}_{k+1|k}) \\
P_{k+1|k+1}         &= P_{k+1|k} - K\, P_{zz}\, K^\top
\end{aligned}$$

The cross-covariance $P_{xz}$ replaces the $H^\top$ product in the linear KF gain formula. No Jacobian
anywhere.

---

## 4. EKF vs UKF Decision Table

<!-- greppable tag: EKF UKF decision -->

| Property | EKF | UKF |
|----------|-----|-----|
| Approach | Jacobian linearization (1st-order Taylor) | Sigma-point propagation (3rd-order accurate) |
| Accuracy | Good for mildly nonlinear | Better for moderately-to-highly nonlinear |
| Jacobian needed | Yes — must derive analytically | No |
| Compute cost | Lower (one matrix multiply per step) | Higher ($2n+1$ sigma propagations per step) |
| Grid use case | Conductor temperature (IEEE 738 EKF), linear-ish voltage estimation | Generator rotor angle DSE, highly nonlinear power-flow near voltage limits |
| Failure mode | Ill-conditioned Jacobian near voltage collapse | Sigma points may lose positive-definiteness of $P$ for large $n$ or extreme nonlinearity |

### When to Choose: The Three-Way Decision

**EKF:** System is mildly nonlinear, Jacobian is analytically tractable, and compute budget
is tight. Example: IEEE 738 conductor temperature EKF — the ODE is mildly nonlinear in $T_c$,
the Jacobian $A = \partial f/\partial T_c$ is a scalar, easy to compute.

**UKF:** System is moderately-to-highly nonlinear or the Jacobian is hard to derive
analytically (e.g., multi-machine swing equations with complex coupling). Example: generator
rotor angle dynamic state estimation near voltage stability limits where EKF Jacobians become
ill-conditioned.

**Particle filter:** Non-Gaussian noise — e.g., after a fault with unknown fault type where
the noise distribution has heavy tails or multimodal structure. Particle filters make no
Gaussian assumption, but their computational cost scales with the number of particles (often
1,000–10,000 for decent accuracy in high-dimensional problems).

---

## 5. Q/R Tuning and Innovation Sequence / Divergence Detection

This section is what separates "I know the equations" from "I have built and debugged a
Kalman filter."

### Q and R: Physical Meaning

$Q$ = **process noise covariance** — how uncertain you are about your own model.
$R$ = **measurement noise covariance** — how uncertain you are about your sensors.

**Physical interpretation for IEEE 738 EKF:**

- **$Q$** reflects uncertainty in the IEEE 738 model: unknown wind gusts not captured by the
  anemometer, conductor aging, span-to-span variation. Large $Q$ → filter updates faster on
  measurements (trusts the model less).
- **$R$** reflects current transformer accuracy and the resistance-inference noise chain:
  CT accuracy class 0.2 means 0.2% error on rated current, giving $R \approx (0.002 \times I_\text{rated})^2$.

**Initialization strategy:**

1. Start from physics priors: $R$ from sensor datasheet specs.
2. Estimate $Q$ from model residuals: run the model open-loop against known-truth segments,
   measure variance of the residual.
3. Tune iteratively: if the innovation sequence shows growing variance, $Q$ is too small
   (model is drifting, filter is not tracking). If the filter is sluggish, $R$ is too large
   relative to $Q$.

### The Q = 0 Trap (Pitfall 4 from Research)

Setting $Q = 0$ means "my model is perfect." The covariance $P$ converges to zero over time.
The Kalman gain $K \to 0$. The filter stops updating on measurements entirely — it just runs
open-loop. Any model drift accumulates without correction.

**Always initialize $Q > 0$**, even if only a tiny amount, to keep the filter responsive.

### Innovation Sequence and Divergence Detection

The **innovation sequence** is the time series of measurement residuals:

$$y_k = z_k - h(\hat{x}_{k|k-1})$$

Under a well-tuned, non-diverging filter, $\{y_k\}$ must be:

1. **Zero-mean** (no systematic bias in the estimate)
2. **White** (no autocorrelation — consecutive innovations are independent)
3. **Gaussian** with covariance $S_k = H\, P_{k|k-1}\, H^\top + R$

Monitoring the innovation sequence is the primary diagnostic for filter health.

### Normalized Innovation Squared (NIS) — Chi-Squared Test

Compute the **NIS** at each step:

$$\text{NIS}_k = y_k^\top S_k^{-1} y_k$$

Under a correctly-tuned filter, $\text{NIS}_k \sim \chi^2(m)$ where $m$ = measurement dimension.

If $\text{NIS}_k$ consistently exceeds the 95th-percentile threshold (from `scipy.stats.chi2.ppf(0.95, df=m)`),
the filter is diverging or has been hit with a bad measurement.

**Practical response to divergence:**

- **Isolated spike:** Gate the update (skip measurement update that step), log for investigation.
- **Sustained divergence:** Check sensor failure, check for model mismatch (topology change,
  conductor aging), increase $Q$ to make filter more responsive, or reinitialize $P$.

**Interview sentence:** "I always plot the innovation sequence as a diagnostic subplot. If
it drifts from zero mean or if NIS consistently exceeds the chi-squared 95th percentile,
that tells me either my model is wrong or a sensor has failed — and the pattern of the drift
tells me which."

### Adaptive Tuning (Sage-Husa — Awareness Level)

For production systems where $Q$ or $R$ may change (e.g., a sensor ages), the Sage-Husa
algorithm estimates $R$ online from empirical innovation statistics:

$$\hat{R}_k = (1 - d_k)\, \hat{R}_{k-1} + d_k\, \bigl[y_k y_k^\top - H_k\, P_{k|k-1}\, H_k^\top\bigr]$$

where $d_k$ is a forgetting factor. This closes the loop: the filter observes the actual
innovation covariance and adjusts $R$ to match. Know this exists; the detail matters less
than the principle.

---

## Connection to KAL-03 (Worked Example)

Everything in this file is realized in the IEEE 738 conductor temperature EKF (KAL-03):

- $f(T_c, u)$ = the discretized IEEE 738 ODE (process model)
- $h(T_c) = R_{25}[1 + \alpha_R(T_c - 25)]$ — resistance as a function of temperature (measurement model)
- $A = \partial f/\partial T_c$ — scalar Jacobian from the ODE linearization
- $H = \partial h/\partial T_c = R_{25} \times \alpha_R$ — scalar measurement Jacobian (a constant)
- $Q$ = model uncertainty from wind + aging ($\approx 0.01$–$0.1\,{}^\circ\text{C}^2/\text{step}$)
- $R$ = CT accuracy ($\approx (0.002 \times I_\text{rated})^2$ in current units, then propagated through $h$)

The scalar state makes the matrix equations collapse to scalars, which makes the worked
example easy to trace step by step. All the same logic applies for vector-state grid DSE.

---

## Quick-Recall Card (Recite Before the Interview)

**Linear KF:**
- Predict: $\hat{x}_{k|k-1} = F\hat{x} + Bu$; $P_{k|k-1} = FPF^\top + Q$
- Update: $y = z - H\hat{x}$; $S = HPH^\top + R$; $K = PH^\top S^{-1}$; $\hat{x} \mathrel{+}= Ky$; $P = (I-KH)P$

**EKF:**
- Same as KF but replace $F$ with $A = \partial f/\partial x$ (process Jacobian) and $H$ with $\partial h/\partial x$ (measurement Jacobian)
- Predict propagates $\hat{x}$ through true $f$; covariance propagates through linear $A$
- Fails when $f$/$h$ is highly nonlinear → ill-conditioned Jacobian → divergence

**UKF:**
- Generate $2n+1$ sigma points around $\hat{x}$ using $\sqrt{(n+\lambda)P}$
- Propagate sigma points through true $f$ and $h$ (no Jacobian needed)
- Recombine weighted sigma points to get mean and covariance
- $\alpha$ controls spread; $\beta=2$ optimal for Gaussian; $\lambda = \alpha^2(n+\kappa)-n$

**Decision:** EKF for mildly nonlinear (line temp, EKF Jacobian tractable). UKF for strongly
nonlinear (rotor angle DSE, near voltage collapse). Particle filter for non-Gaussian.

**Divergence detection:** $\text{NIS}_k = y^\top S^{-1} y \sim \chi^2(m)$. Sustained NIS > threshold = diverging.
Check: sensor failure, model mismatch, $Q$ too small.

**Q/R trap:** $Q=0$ → $K\to0$ → filter goes deaf. Always set $Q>0$.

---

*Sources: Welch & Bishop, Edinburgh CVonline EKF formulation; filterpy ReadTheDocs UKF equations;
Stone Soup UKF tutorial; arXiv 2012.06069 (power system DSE with EKF/UKF); 01-RESEARCH.md verified equations*
