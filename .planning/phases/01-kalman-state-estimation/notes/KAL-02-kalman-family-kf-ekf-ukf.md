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

```
x_k = F x_{k-1} + B u_k + w_k       (process model;  w_k ~ N(0, Q))
z_k = H x_k + v_k                    (measurement model;  v_k ~ N(0, R))
```

- `x_k` = state vector at time k
- `F` = state transition matrix (physics: how the state evolves one step)
- `B` = control input matrix; `u_k` = known input (e.g., load dispatch)
- `Q` = process noise covariance (uncertainty in the model)
- `H` = measurement matrix (which linear combination of states you observe)
- `R` = measurement noise covariance (sensor uncertainty)

### Predict Step

```
x̂_{k|k-1} = F x̂_{k-1|k-1} + B u_k          (predicted state mean)
P_{k|k-1}  = F P_{k-1|k-1} Fᵀ + Q           (predicted state covariance)
```

"Predicted" means: we have not yet seen measurement z_k. We propagate our best estimate
forward using the dynamics model. P grows because the model adds uncertainty (Q).

### Update Step

```
y_k  = z_k − H x̂_{k|k-1}                    (innovation = actual − predicted measurement)
S_k  = H P_{k|k-1} Hᵀ + R                   (innovation covariance)
K_k  = P_{k|k-1} Hᵀ S_k⁻¹                   (Kalman gain)
x̂_{k|k} = x̂_{k|k-1} + K_k y_k             (updated state estimate)
P_{k|k}  = (I − K_k H) P_{k|k-1}            (updated state covariance)
```

### Kalman Gain Intuition

K_k balances two sources of information:

- If **R is large** (noisy sensor) → S is large → K is small → trust the model more, move
  only a little toward the measurement.
- If **P is large** (model is uncertain) → K is large → trust the sensor more, move a lot
  toward the measurement.
- Perfect sensor (R → 0): K → H⁻¹, x̂ → z (ignore model entirely).
- Perfect model (Q → 0, P → 0): K → 0, x̂ stays at prediction (ignore sensor).

**Interview sentence:** "Kalman gain is the auto-tuned weight that decides, at each step,
whether to trust the physics model more or the sensor more. It is derived from their
relative uncertainties P and R."

---

## 2. Extended Kalman Filter (EKF)

Use EKF when f(·) or h(·) is **nonlinear**. The EKF linearizes these functions at each
step using a first-order Taylor expansion — i.e., it computes Jacobian matrices.

### Nonlinear State-Space

```
x_{k+1} = f(x_k, u_k) + w_k          (nonlinear process model)
z_k     = h(x_k) + v_k               (nonlinear measurement model)
```

f and h are arbitrary differentiable functions. For grid dynamic state estimation, f might be
the swing equation; h might be the AC power-flow equations.

### EKF Predict Step

```
x̂_{k+1|k} = f(x̂_{k|k}, u_k)              (propagate state through nonlinear f)
A_k = ∂f/∂x |_{x̂_{k|k}}                   (Jacobian of f — the process Jacobian)
P_{k+1|k} = A_k P_{k|k} A_kᵀ + Q          (propagate covariance using linearized A)
```

**What the Jacobian A does:** The true nonlinear f curves away from a straight line; A is
the best linear approximation at the current point. Covariance (uncertainty ellipsoid) is
propagated using that linear approximation.

### EKF Update Step

```
H_k = ∂h/∂x |_{x̂_{k+1|k}}                 (Jacobian of h — the measurement Jacobian)
y_k = z_k − h(x̂_{k+1|k})                  (innovation using true nonlinear h)
S_k = H_k P_{k+1|k} H_kᵀ + R              (innovation covariance)
K_k = P_{k+1|k} H_kᵀ S_k⁻¹               (Kalman gain)
x̂_{k+1|k+1} = x̂_{k+1|k} + K_k y_k       (updated state)
P_{k+1|k+1} = (I − K_k H_k) P_{k+1|k}    (updated covariance)
```

Same structure as the linear KF update, but H is now the Jacobian of h rather than a
constant matrix.

### When EKF Fails

This is a common interview probe — know these failure modes:

1. **Highly nonlinear model:** If f or h has strong curvature, the first-order Jacobian
   approximation is poor. The filter may diverge (state estimate drifts away from truth).

2. **Ill-conditioned Jacobian near voltage collapse:** Power-flow Jacobians become
   near-singular near the stability limit (large phase angle differences, nose curve tip).
   A_k or H_k can have very large entries, making P propagation numerically unstable.

3. **Positive-feedback divergence:** As P grows (model drifts), the linearization point x̂
   moves away from the true state, making the Jacobian computed at x̂ an even worse
   approximation of f at the true x. This worsens the estimate further — a runaway loop.

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
distribution exactly. After propagation through the true nonlinear f, the recombined
statistics are accurate to **third order** (vs. first order for EKF). No Jacobian derivation
required.

### Sigma Point Generation

For an n-dimensional state x̂ with covariance P, generate **2n + 1** sigma points:

```
χ₀ = x̂
χᵢ = x̂ + (√((n + λ) P))ᵢ        for i = 1 … n
χ_{n+i} = x̂ − (√((n + λ) P))ᵢ   for i = 1 … n

λ = α²(n + κ) − n               (composite scaling parameter)
```

`(√((n + λ) P))ᵢ` means the i-th column of the matrix square root, scaled by √(n + λ).

### UKF Parameters (alpha, beta, kappa)

- **α (alpha):** Controls the spread of sigma points around the mean. Typical: 0.001 to 0.1.
  Larger α → wider spread → captures more of the nonlinearity, but also brings in
  higher-order errors (can cause P to lose positive-definiteness for highly non-Gaussian).
- **β (beta):** Encodes prior knowledge of the state distribution shape. β = 2 is optimal
  for Gaussian distributions (minimizes the 4th-order error term).
- **κ (kappa):** Secondary scaling. Common choices: κ = 0 or κ = 3 − n.

**Interview sentence:** "Alpha controls how far you spread sigma points from the mean. Beta
= 2 is optimal for Gaussian priors. Kappa is usually set to zero or three minus n."

### UKF Predict Step

```
Propagate each sigma point through f: χ̃ᵢ = f(χᵢ, u)
x̂_{k+1|k} = Σ Wᵢᵐ χ̃ᵢ              (weighted mean of propagated points)
P_{k+1|k}  = Σ Wᵢᶜ (χ̃ᵢ − x̂)(χ̃ᵢ − x̂)ᵀ + Q  (weighted covariance + process noise)
```

Weights Wᵢᵐ (mean) and Wᵢᶜ (covariance) are determined by α, β, κ. The zeroth sigma point
(the mean itself) gets higher weight; the symmetric pairs get equal weight.

### UKF Update Step

```
Propagate sigma points through h: γᵢ = h(χ̃ᵢ)
ẑ_{k+1|k} = Σ Wᵢᵐ γᵢ               (predicted measurement mean)
Pzz = Σ Wᵢᶜ (γᵢ − ẑ)(γᵢ − ẑ)ᵀ + R  (innovation covariance)
Pxz = Σ Wᵢᶜ (χ̃ᵢ − x̂)(γᵢ − ẑ)ᵀ     (cross-covariance state-measurement)
K   = Pxz Pzz⁻¹                      (Kalman gain)
x̂_{k+1|k+1} = x̂_{k+1|k} + K (z_{k+1} − ẑ_{k+1|k})
P_{k+1|k+1} = P_{k+1|k} − K Pzz Kᵀ
```

The cross-covariance Pxz replaces the H^T product in the linear KF gain formula. No Jacobian
anywhere.

---

## 4. EKF vs UKF Decision Table

<!-- greppable tag: EKF UKF decision -->

| Property | EKF | UKF |
|----------|-----|-----|
| Approach | Jacobian linearization (1st-order Taylor) | Sigma-point propagation (3rd-order accurate) |
| Accuracy | Good for mildly nonlinear | Better for moderately-to-highly nonlinear |
| Jacobian needed | Yes — must derive analytically | No |
| Compute cost | Lower (one matrix multiply per step) | Higher (2n+1 sigma propagations per step) |
| Grid use case | Conductor temperature (IEEE 738 EKF), linear-ish voltage estimation | Generator rotor angle DSE, highly nonlinear power-flow near voltage limits |
| Failure mode | Ill-conditioned Jacobian near voltage collapse | Sigma points may lose positive-definiteness of P for large n or extreme nonlinearity |

### When to Choose: The Three-Way Decision

**EKF:** System is mildly nonlinear, Jacobian is analytically tractable, and compute budget
is tight. Example: IEEE 738 conductor temperature EKF — the ODE is mildly nonlinear in Tc,
the Jacobian A = ∂f/∂Tc is a scalar, easy to compute.

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

`Q` = **process noise covariance** — how uncertain you are about your own model.
`R` = **measurement noise covariance** — how uncertain you are about your sensors.

**Physical interpretation for IEEE 738 EKF:**

- **Q** reflects uncertainty in the IEEE 738 model: unknown wind gusts not captured by the
  anemometer, conductor aging, span-to-span variation. Large Q → filter updates faster on
  measurements (trusts the model less).
- **R** reflects current transformer accuracy and the resistance-inference noise chain:
  CT accuracy class 0.2 means 0.2% error on rated current, giving R ≈ (0.002 × I_rated)².

**Initialization strategy:**

1. Start from physics priors: R from sensor datasheet specs.
2. Estimate Q from model residuals: run the model open-loop against known-truth segments,
   measure variance of the residual.
3. Tune iteratively: if the innovation sequence shows growing variance, Q is too small
   (model is drifting, filter is not tracking). If the filter is sluggish, R is too large
   relative to Q.

### The Q = 0 Trap (Pitfall 4 from Research)

Setting Q = 0 means "my model is perfect." The covariance P converges to zero over time.
The Kalman gain K → 0. The filter stops updating on measurements entirely — it just runs
open-loop. Any model drift accumulates without correction.

**Always initialize Q > 0**, even if only a tiny amount, to keep the filter responsive.

### Innovation Sequence and Divergence Detection

The **innovation sequence** is the time series of measurement residuals:

```
y_k = z_k − h(x̂_{k|k-1})
```

Under a well-tuned, non-diverging filter, `{y_k}` must be:

1. **Zero-mean** (no systematic bias in the estimate)
2. **White** (no autocorrelation — consecutive innovations are independent)
3. **Gaussian** with covariance `S_k = H P_{k|k-1} Hᵀ + R`

Monitoring the innovation sequence is the primary diagnostic for filter health.

### Normalized Innovation Squared (NIS) — Chi-Squared Test

Compute the **NIS** at each step:

```
NIS_k = yᵢᵀ S_k⁻¹ y_k
```

Under a correctly-tuned filter, `NIS_k ~ χ²(m)` where m = measurement dimension.

If `NIS_k` consistently exceeds the 95th-percentile threshold (from `scipy.stats.chi2.ppf(0.95, df=m)`),
the filter is diverging or has been hit with a bad measurement.

**Practical response to divergence:**

- **Isolated spike:** Gate the update (skip measurement update that step), log for investigation.
- **Sustained divergence:** Check sensor failure, check for model mismatch (topology change,
  conductor aging), increase Q to make filter more responsive, or reinitialize P.

**Interview sentence:** "I always plot the innovation sequence as a diagnostic subplot. If
it drifts from zero mean or if NIS consistently exceeds the chi-squared 95th percentile,
that tells me either my model is wrong or a sensor has failed — and the pattern of the drift
tells me which."

### Adaptive Tuning (Sage-Husa — Awareness Level)

For production systems where Q or R may change (e.g., a sensor ages), the Sage-Husa
algorithm estimates R online from empirical innovation statistics:

```
R̂_k = (1 − d_k) R̂_{k-1} + d_k [y_k yᵢᵀ − H_k P_{k|k-1} H_kᵀ]
```

where d_k is a forgetting factor. This closes the loop: the filter observes the actual
innovation covariance and adjusts R to match. Know this exists; the detail matters less
than the principle.

---

## Connection to KAL-03 (Worked Example)

Everything in this file is realized in the IEEE 738 conductor temperature EKF (KAL-03):

- f(Tc, u) = the discretized IEEE 738 ODE (process model)
- h(Tc) = R₂₅[1 + α_R(Tc − 25)] — resistance as a function of temperature (measurement model)
- A = ∂f/∂Tc — scalar Jacobian from the ODE linearization
- H = ∂h/∂Tc = R₂₅ × α_R — scalar measurement Jacobian (a constant)
- Q = model uncertainty from wind + aging (≈ 0.01–0.1 °C²/step)
- R = CT accuracy (≈ (0.002 × I_rated)² in current units, then propagated through h)

The scalar state makes the matrix equations collapse to scalars, which makes the worked
example easy to trace step by step. All the same logic applies for vector-state grid DSE.

---

## Quick-Recall Card (Recite Before the Interview)

**Linear KF:**
- Predict: x̂_{k|k-1} = F x̂ + B u; P_{k|k-1} = F P Fᵀ + Q
- Update: y = z − H x̂; S = H P Hᵀ + R; K = P Hᵀ S⁻¹; x̂ += K y; P = (I−KH)P

**EKF:**
- Same as KF but replace F with A = ∂f/∂x (process Jacobian) and H with ∂h/∂x (measurement Jacobian)
- Predict propagates x̂ through true f; covariance propagates through linear A
- Fails when f/h is highly nonlinear → ill-conditioned Jacobian → divergence

**UKF:**
- Generate 2n+1 sigma points around x̂ using √((n+λ)P)
- Propagate sigma points through true f and h (no Jacobian needed)
- Recombine weighted sigma points to get mean and covariance
- α controls spread; β=2 optimal for Gaussian; λ = α²(n+κ)−n

**Decision:** EKF for mildly nonlinear (line temp, EKF Jacobian tractable). UKF for strongly
nonlinear (rotor angle DSE, near voltage collapse). Particle filter for non-Gaussian.

**Divergence detection:** NIS_k = yᵀ S⁻¹ y ~ χ²(m). Sustained NIS > threshold = diverging.
Check: sensor failure, model mismatch, Q too small.

**Q/R trap:** Q=0 → K→0 → filter goes deaf. Always set Q>0.

---

*Sources: Welch & Bishop, Edinburgh CVonline EKF formulation; filterpy ReadTheDocs UKF equations;
Stone Soup UKF tutorial; arXiv 2012.06069 (power system DSE with EKF/UKF); 01-RESEARCH.md verified equations*
