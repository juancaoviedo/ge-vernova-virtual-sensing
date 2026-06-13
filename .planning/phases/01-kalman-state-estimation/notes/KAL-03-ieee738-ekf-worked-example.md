# KAL-03: Line-Temperature EKF — IEEE 738 Worked Example

**Phase:** 01 — Kalman & State Estimation
**Deliverable:** KAL-03
**Purpose:** Interview-ready narration of the IEEE 738 conductor thermal ODE mapped to an EKF,
with actual numbers traced through one full predict-update step, Q/R tuning logic, innovation
monitoring, divergence detection, and the explicit building-RC isomorphism that connects Juan's
existing work to this domain.

---

## 1. The IEEE 738 Thermal ODE — The Physics

IEEE Standard 738 defines the transient thermal balance of a bare overhead conductor as:

```
mCp * dTc/dt = qi + qs - qc - qr
```

This is the **process model** — the system dynamics that the EKF predict step will encode. Each
term is a power per unit length (W/m):

| Term | Name | Expression | Physical Meaning |
|------|------|------------|-----------------|
| `Tc` | Conductor temperature (°C) | — | The **hidden state** — not directly measured |
| `mCp` | Thermal capacitance | ~534 J/(m·°C) for Drake ACSR | Thermal inertia; determines how fast Tc changes |
| `qi` | Resistive (Joule) heating | `I² · R(Tc)` | Current through the conductor's resistance generates heat — the dominant controllable term |
| `qs` | Solar heat gain | `α_s · Q_se · sin(θ) · D` | Sun shines on the conductor; not controllable, but measurable from irradiance sensors |
| `qc` | Convective cooling | `0.0205 · ρ_f^0.5 · D^0.75 · (Tc−Ta)^1.25` (natural convection) | Air removes heat; proportional to temperature difference, strongly dependent on wind |
| `qr` | Radiative cooling | `0.0178 · D · ε · [(Tc+273)⁴ − (Ta+273)⁴] / 100⁴` | Stefan-Boltzmann radiation; weaker than convection but non-negligible at high temperatures |

**Note on R(Tc):** Conductor resistance varies linearly with temperature:
```
R(Tc) = R25 * [1 + alpha_R * (Tc - 25)]
```
This is the nonlinearity that makes the system an EKF problem rather than a linear KF problem.
R(Tc) appears inside qi = I² · R(Tc), so the ODE is nonlinear in the state Tc.

### ACSR Drake Conductor Parameters (Worked Example Reference)

| Parameter | Symbol | Value | Units |
|-----------|--------|-------|-------|
| Outer diameter | D | 28.1 | mm (= 0.0281 m) |
| Thermal capacitance | mCp | 534 | J/(m·°C) |
| Resistance at 25°C | R25 | 7.28×10⁻⁵ | Ω/m |
| Resistance at 75°C | R75 | 8.69×10⁻⁵ | Ω/m |
| Temperature coefficient of resistance | alpha_R | 0.00403 | /°C |
| Solar absorptivity | alpha_s | 0.5 | — |
| Emissivity | ε | 0.5 | — |
| Maximum safe temperature (typical) | T_max | 75–100 | °C |

**Thermal time constant:** τ = mCp / UA_eff ≈ 10–15 minutes for Drake ACSR in moderate wind.
This is the same "RC time constant" as in a building thermal model — confirming the structural
analogy (see Section 7).

---

## 2. State-Space Mapping to the EKF

### State, Inputs, and Measurement

**State vector (scalar):**
```
x = [Tc]   (conductor temperature in °C)
```

**Control inputs (measured from SCADA/PMU/weather sensors, not estimated):**
```
u = [I, Ta, v_wind, qs]
    (current A, ambient temp °C, wind speed m/s, solar irradiance W/m²)
```

**Measurement model — Architecture 3 (resistance proxy, used in this example):**

If we measure voltage drop on a line segment and know the current I, we can back-calculate
the apparent resistance per unit length. Since R(Tc) = R25 · [1 + alpha_R · (Tc − 25)], the
measurement is a direct (noisy) function of the hidden state Tc:

```
h(Tc) = R25 * [1 + alpha_R * (Tc - 25)]
```

This is architecture 3: current from PMU + voltage drop → apparent resistance → infer Tc.

### Discretized Process Model (Euler, Δt = 1 s)

The predict function f(Tc, u) is the IEEE 738 ODE stepped forward by one second:

```
f(Tc, u) = Tc + (Δt / mCp) * [I²·R(Tc) - qc(Tc, Ta, v_wind) - qr(Tc, Ta) + qs]
```

Breaking down each sub-calculation:
- `R(Tc) = R25 * (1 + alpha_R * (Tc - 25))`  — resistance at current temperature
- `qi = I² * R(Tc)`  — Joule heating
- `qs = alpha_s * Q_se * D`  — solar (simplified: broadside, no angle correction)
- `qc = 0.0205 * rho_f^0.5 * D^0.75 * (Tc - Ta)^1.25`  — natural convection
- `qr = 0.0178 * D * eps * [(Tc+273)⁴ - (Ta+273)⁴] / 1e8`  — radiation

### EKF Jacobians

**Process Jacobian A = df/dTc** (needed to propagate covariance P through predict step):

```
A = df/dTc = 1 + (Δt/mCp) * [I²·(dR/dTc) - (dqc/dTc) - (dqr/dTc)]

where:
  dR/dTc    = R25 * alpha_R                                          (linear: ~2.94×10⁻⁷ Ω/(m·°C))
  dqc/dTc   = 0.0205 * rho_f^0.5 * D^0.75 * 1.25 * (Tc-Ta)^0.25   (natural convection: ~0.04 at (Tc-Ta)=20°C)
  dqr/dTc   = 4 * 0.0178 * D * eps * (Tc+273)³ / 1e8               (radiation: ~0.01 at 45°C)
```

WHY we compute A: In the EKF predict step, P_{pred} = A² · P_{prior} + Q. The Jacobian A
tells us how fast small temperature errors grow or shrink under the process dynamics. If A > 1,
errors amplify (unstable open-loop); if A < 1, errors shrink (stable without measurement).

**Measurement Jacobian H = dh/dTc** (needed to translate state uncertainty to measurement space):

```
H = d/dTc [R25 * (1 + alpha_R * (Tc - 25))]
  = R25 * alpha_R
  = 7.28e-5 * 0.00403
  ≈ 2.934×10⁻⁷ Ω/(m·°C)
```

H is a constant scalar — the measurement model is linear in Tc (even though the process model is
nonlinear). This is convenient: the update step behaves like a linear KF update.

---

## 3. Full Numeric Worked Example — One Predict-Update Step

**Scenario:** Drake ACSR on a 230 kV line. Load I = 500 A. Calm, sunny midday.

**Initial conditions:**
```
Tc_0  = 45°C   (prior estimate — conductor has been running a while)
Ta    = 25°C   (ambient)
v_wind ≈ 0     (natural convection only)
Q_solar = 900 W/m² (broadside sun)
```

**Prior covariance:**
```
P_prior = 4°C²    (±2°C uncertainty in our prior estimate)
```

---

### Step 3a: Heat Balance at Tc = 45°C (compute net heat input)

**Resistive heating qi:**
```
R_45 = R25 * [1 + alpha_R * (45 - 25)]
     = 7.28e-5 * [1 + 0.00403 * 20]
     = 7.28e-5 * 1.0806
     = 7.867e-5  Ω/m

qi = I² * R_45 = (500)² * 7.867e-5 = 250000 * 7.867e-5 = 19.67 W/m
```
WHY: The current squared times resistance gives the power dissipated as heat. At 500 A, this
is the dominant heat input — more than solar.

**Solar heat gain qs:**
```
qs = alpha_s * Q_se * sin(90°) * D
   = 0.5 * 900 * 1.0 * 0.0281
   = 12.65 W/m
```
WHY: Broadside sun at 90° gives maximum solar heating. alpha_s = 0.5 means the conductor
absorbs half the incident radiation (the rest is reflected).

**Convective cooling qc (natural convection, v_wind ≈ 0):**
```
qc = 0.0205 * rho_f^0.5 * D^0.75 * (Tc - Ta)^1.25

rho_f ≈ 1.20 kg/m³ (air at ~50°C film temperature)
D in mm for this formula: 28.1 mm

qc = 0.0205 * (1.20)^0.5 * (28.1)^0.75 * (45 - 25)^1.25
   = 0.0205 * 1.095 * 10.05 * 26.39
   ≈ 5.96 W/m
```
WHY: Natural convection is driven by the temperature difference (Tc - Ta). The exponent 1.25
(not 1.0) reflects the nonlinear buoyancy effect — hotter surfaces create stronger convective
plumes. This is the term that makes the Jacobian non-trivial.

**Radiative cooling qr:**
```
qr = 0.0178 * D * eps * [(Tc+273)⁴ - (Ta+273)⁴] / (100)⁴

   = 0.0178 * 0.0281 * 0.5 * [(318)⁴ - (298)⁴] / 1e8

   (318)⁴ = 1.0243e10,  (298)⁴ = 7.900e9

   = 0.0178 * 0.0281 * 0.5 * (1.0243e10 - 7.900e9) / 1e8
   = 0.0178 * 0.0281 * 0.5 * 2343 / 1
   ≈ 0.000250 * 2343 * 0.5 / 1
   ≈ 2.93 W/m
```
WHY: Stefan-Boltzmann radiation depends on the 4th power of absolute temperature (Kelvin).
At 45°C, radiation is weaker than convection but increases faster as Tc rises (T⁴ growth).

**Net heat input and temperature derivative:**
```
net = qi + qs - qc - qr
    = 19.67 + 12.65 - 5.96 - 2.93
    = 23.43 W/m

dTc/dt = net / mCp = 23.43 / 534 ≈ +0.044 °C/s
```
**Interpretation:** At 45°C with 500 A, the conductor is still heating up at 0.044°C/s.
It has not reached thermal equilibrium yet. This positive derivative drives the predict step
to push Tc upward.

---

### Step 3b: Steady-State Temperature and DLR

**What is the steady-state conductor temperature at 500 A?**

Set dTc/dt = 0 → solve qi + qs = qc + qr numerically → **Tc_ss ≈ 73°C**

This is close to the 75°C thermal limit — the conductor is operating near its ampacity
boundary. The small 2°C margin explains why DLR is critical here.

**Dynamic Line Rating (DLR) — what is the maximum current at this weather condition?**

Solve `I²_max * R(75°C) = qc(75°C) + qr(75°C) - qs` for I_max:
```
→ I_max ≈ 531 A
```

Compare to a typical static nameplate rating of ~900 A (computed under conservative worst-case
weather: 0.6 m/s wind, 40°C ambient). On this hot, calm day, the real-time DLR is **lower
than 531 A** for strict compliance at 75°C — which is far less than the 900 A static rating.

**CRITICAL CAVEAT — DLR can DECREASE capacity:**

The popular claim that "DLR gives 10–40% more capacity" applies on average across typical
operating conditions. On a hot, calm day like this scenario (35°C ambient, no wind), DLR may
give a rating LOWER than the static nameplate. The static nameplate was computed under
conservative weather; when actual weather is worse than conservative, DLR is lower, not higher.

**Interview answer:** "DLR gives an accurate real-time rating that can be higher OR lower than
the static rating. The capacity gain comes from cool, windy days. On a hot, calm afternoon,
DLR will correctly reduce the safe operating current — something a static rating would miss,
potentially allowing overloading and thermal damage."

---

### Step 3c: EKF Predict Step

**Input:** Tc_prior = 45°C, P_prior = 4°C²

**Predict Tc forward by Δt = 1 s:**
```
Tc_pred = f(45, u) = 45 + (1/534) * 23.43 = 45 + 0.04388 = 45.044°C
```

**Compute process Jacobian A at Tc = 45°C:**
```
A = 1 + (1/534) * [I²·dR/dTc - dqc/dTc - dqr/dTc]

dR/dTc   = R25 * alpha_R = 7.28e-5 * 0.00403 = 2.934e-7 Ω/(m·°C)
I²·dR/dTc = 250000 * 2.934e-7 = 0.07335 W/(m·°C)

dqc/dTc = 0.0205 * (1.20)^0.5 * (28.1)^0.75 * 1.25 * (45-25)^0.25
        ≈ 0.0205 * 1.095 * 10.05 * 1.25 * 2.115
        ≈ 0.0394 W/(m·°C)   (approximate)

dqr/dTc = 4 * 0.0178 * 0.0281 * 0.5 * (318)³ / 1e8
        = 4 * 0.0178 * 0.0281 * 0.5 * 3.215e7 / 1e8
        ≈ 0.0102 W/(m·°C)   (approximate)

A = 1 + (1/534) * [0.07335 - 0.0394 - 0.0102]
  = 1 + (1/534) * 0.02375
  = 1 + 0.0000445
  ≈ 1.0000445
```

A is very slightly greater than 1.0, indicating the thermal system is marginally unstable
without convective/radiative cooling damping — which is physically correct (heating wins
slightly at this operating point, driving Tc upward toward steady state at 73°C).

**Propagate covariance through predict step:**
```
Q = 0.01°C²/step  (process noise: low, model is trusted)

P_pred = A² * P_prior + Q
       = (1.0000445)² * 4.0 + 0.01
       ≈ 1.000089 * 4.0 + 0.01
       = 4.000356 + 0.01
       ≈ 4.026°C²
```

WHY P grew slightly: The Jacobian A ≈ 1.000 means covariance is nearly unchanged by the
dynamics. The +Q = +0.01 term reflects residual model uncertainty (unmodeled wind gusts,
conductor aging) that accumulates each step.

---

### Step 3d: EKF Update Step

**Measurement arrives:** A resistance monitor (or voltage/current measurement on a line segment)
reports the apparent resistance:

```
z_meas = 7.94e-5 Ω/m   (measured — slightly higher than predicted, suggesting Tc > 45°C)
```

**Predicted measurement from the model:**
```
z_pred = h(Tc_pred) = R25 * [1 + alpha_R * (Tc_pred - 25)]
       = 7.28e-5 * [1 + 0.00403 * (45.044 - 25)]
       = 7.28e-5 * [1 + 0.00403 * 20.044]
       = 7.28e-5 * 1.08078
       = 7.868e-5  Ω/m
```

**Innovation (the "surprise"):**
```
y = z_meas - z_pred = 7.94e-5 - 7.868e-5 = 0.072e-5 = 7.2e-7 Ω/m
```
WHY the innovation matters: y > 0 means the measured resistance is higher than our model
predicted. Higher resistance → higher actual Tc than our estimate. The EKF will use this
positive innovation to push Tc upward.

**Measurement Jacobian (constant scalar):**
```
H = R25 * alpha_R = 7.28e-5 * 0.00403 = 2.934e-7 Ω/(m·°C)
```

**Innovation covariance S:**
```
R_sensor = (1e-7)² = 1e-14  Ω²/m²   (sensor noise: ≈ 0.1 μΩ/m standard deviation)

S = H² * P_pred + R_sensor
  = (2.934e-7)² * 4.026 + 1e-14
  = 8.608e-14 * 4.026 + 1e-14
  = 3.466e-13 + 1e-14
  ≈ 3.57e-13  Ω²/m²
```

S combines the state uncertainty (how unsure we are about Tc, projected into measurement space
via H²P) with the measurement noise R. Large S → innovation y is expected to be large even
without model error; small S → any non-zero y is informative.

**Kalman gain K:**
```
K = H * P_pred / S
  = (2.934e-7 * 4.026) / 3.57e-13
  = 1.181e-6 / 3.57e-13
  ≈ 3.31×10⁶  °C/(Ω/m)
```
WHY K is large: P_pred >> R means we trust the measurement much more than the model at this
step. K converts a small resistance innovation (in Ω/m) to a large temperature correction
(in °C). The unit analysis: [°C/(Ω/m)] * [Ω/m] = [°C] — correct.

**Posterior state estimate:**
```
Tc_post = Tc_pred + K * y
        = 45.044 + 3.31e6 * 7.2e-7
        = 45.044 + 2.383
        ≈ 47.5°C
```
The measurement (higher apparent resistance) told us Tc is actually about 2.5°C warmer than
the model predicted. The filter incorporates this information, updating its estimate upward.

**Posterior covariance:**
```
P_post = (1 - K * H) * P_pred
       = (1 - 3.31e6 * 2.934e-7) * 4.026
       = (1 - 0.9712) * 4.026
       = 0.0288 * 4.026
       ≈ 0.116°C²    (approximately 0.09–0.12°C² depending on rounding)
```

The uncertainty dropped from P_prior = 4°C² (±2°C) to P_post ≈ 0.09–0.12°C² (±0.3°C).
**One measurement update reduced uncertainty by ~97%.** This dramatic reduction is the point
of the update step: the measurement was highly informative because H²P >> R, so K ≈ 1/H and
the filter relies almost entirely on the sensor this step.

---

### Step 3e: Summary of One Full Predict-Update Cycle

| Quantity | Before Predict | After Predict | After Update |
|----------|---------------|---------------|--------------|
| Tc estimate | 45.000°C | 45.044°C | 47.5°C |
| P (covariance) | 4.000°C² | 4.026°C² | ~0.09–0.12°C² |
| Uncertainty (±1σ) | ±2.00°C | ±2.01°C | ±0.30°C |

**Narrative for the interview:** "The model predicted the conductor would warm by 0.044°C in
one second. Our prior uncertainty stayed almost constant (4 → 4.026) because A ≈ 1 and Q is
small. Then a resistance measurement came in showing the conductor was actually at 7.94e-5 Ω/m
— higher than our predicted 7.87e-5 Ω/m. The innovation was positive. With a Kalman gain of
3.3 million °C/(Ω/m), the filter updated its estimate from 45.04 to 47.5°C and collapsed its
uncertainty from ±2°C down to ±0.3°C in a single step."

---

## 4. Q and R Tuning

The two noise covariance matrices are the EKF's "knobs." Getting them right determines whether
the filter tracks reality or diverges.

### Physical Interpretation

**Q — Process Noise Covariance (°C²/step):**

Q represents your uncertainty about the **process model** — i.e., all the things the IEEE 738
ODE does not capture:
- Unmodeled wind gusts: anemometer measures average wind speed, but a 1-second gust hitting
  the conductor provides extra convective cooling the model cannot predict.
- Conductor non-uniformity along the span: different sag, ice accumulation, surface condition.
- Parameter uncertainty: mCp and R25 may have drifted from nominal (aging, corrosion).
- Span-to-span variation: a lumped model uses a single Tc, but the conductor temperature
  varies spatially — the model represents an average.

A physically motivated Q initialization: wind speed uncertainty ±1 m/s → thermal impact
≈ 0.2°C/s → Q ≈ 0.04–0.1°C²/step.

**R — Measurement Noise Covariance (Ω²/m²):**

R represents your uncertainty about the **sensor**:
- Current transformer (CT) accuracy: Class 0.2 CT has ±0.2% error at rated current.
  At 500 A rated, σ_I ≈ 1 A → σ_qi ≈ 2 * I * R25 * σ_I ≈ 7.3e-8 Ω/m → R ≈ (7.3e-8)².
- Resistance inference noise: voltage measurement uncertainty compounds with current measurement.
- Typical R starting value: (1e-7)² = 1e-14 Ω²/m² (±0.1 μΩ/m standard deviation).

### Tuning Table

| Parameter | Physical Meaning | Recommended Start | Too Large → | Too Small → |
|-----------|-----------------|-------------------|-------------|-------------|
| Q | Model uncertainty: wind gusts, aging, non-uniformity | 0.01–0.1 °C²/step | Filter chases noisy measurements; Tc estimate is erratic | Filter ignores sensors; sticks to model even as it drifts — **divergence** |
| R | Sensor noise: CT accuracy + resistance inference error | (1e-7)² Ω²/m² ≈ 1e-14 | Filter is sluggish; slow to respond to real temperature changes | Filter over-trusts noisy measurements; noisy Tc estimate |
| P₀ | Initial state uncertainty | 100°C² (±10°C) | Filter quickly contracts toward measurement — fine | Over-confident initialization may refuse to correct early errors |

### The Q = 0 Trap

Setting Q = 0 means "I believe my model is perfect." The consequences:
- P_pred = A² · P_post converges toward zero over time (no Q injection to keep P nonzero).
- K → 0 as P → 0 (Kalman gain collapses).
- The filter stops updating its estimate from measurements.
- Eventually Tc_hat drifts from reality with no way to self-correct.

**Prevention:** Always initialize Q > 0 from physical reasoning. Even if the model is
excellent, some unmodeled variability always exists. Q = 0.01°C²/step is a reasonable lower
bound for IEEE 738 in a controlled substation environment.

### Adaptive Tuning (Sage-Husa — Awareness Level)

For production systems, Q and R can be estimated online from the innovation sequence itself:
```
R_hat_k = (1 - d_k) * R_hat_{k-1} + d_k * [y_k * y_k_T - H_k * P_{k|k-1} * H_k_T]
```
where d_k is a forgetting factor (typically 0.98–0.999). This lets the filter adapt to
changing sensor quality (e.g., degrading CT, changing weather station accuracy) without
manual re-tuning.

---

## 5. Innovation Sequence and Divergence Detection

### The Innovation Sequence

The innovation at each time step is:
```
y_k = z_k - h(x_hat_{k|k-1})   (measurement - predicted measurement)
```

Under a correctly functioning, well-tuned filter, the innovation sequence {y_k} must be:

1. **Zero-mean:** No systematic bias. If y_k has a persistent positive or negative offset,
   the model is wrong in a predictable direction (e.g., consistently underestimating Tc).
2. **White (uncorrelated):** Consecutive innovations should be independent. Autocorrelated
   innovations indicate the model is missing structure (e.g., a slow drift that the model
   cannot represent).
3. **Gaussian with covariance S_k:** The distribution should match the theoretical innovation
   covariance S_k = H · P_{k|k-1} · H_T + R.

If any of these three properties fail, the filter is diverging or misconfigured.

### NIS — Normalized Innovation Squared

The formal divergence test uses the Normalized Innovation Squared (NIS):
```
NIS_k = y_k^T * S_k^{-1} * y_k
```

Under a correct filter, NIS_k follows a chi-squared distribution with m degrees of freedom,
where m is the dimension of the measurement vector:
```
NIS_k ~ chi²(m)
```

For our scalar measurement case (m = 1):
```
threshold_95 = chi2.ppf(0.95, df=1) = 3.84
```

If NIS_k > 3.84, there is only a 5% chance this happened by chance. A persistent NIS above
the threshold signals a problem.

**Python implementation:**
```python
from scipy.stats import chi2

def check_nis(innov, S, confidence=0.95, m=1):
    """Check Normalized Innovation Squared against chi-squared gate."""
    NIS = (innov ** 2) / S      # scalar case: NIS = y² / S
    threshold = chi2.ppf(confidence, df=m)  # = 3.84 for m=1
    return NIS, NIS > threshold
```

### Worked NIS Calculation for Step 3

```
y = 7.2e-7 Ω/m
S ≈ 3.57e-13 Ω²/m²

NIS = y² / S = (7.2e-7)² / 3.57e-13 = 5.18e-13 / 3.57e-13 ≈ 1.45
```

NIS = 1.45 < 3.84 (the 95th-percentile threshold for df=1) → innovation is **statistically
consistent**. The measurement update in this step is accepted. The filter is behaving correctly.

### Practical Response to Divergence

| NIS Pattern | Diagnosis | Response |
|-------------|-----------|----------|
| Single isolated spike (NIS >> 3.84, then returns) | Bad measurement (CT fault, communication glitch) | Gate the update: reject this measurement, continue predicting |
| Sustained NIS > threshold (>5 consecutive) | Model mismatch OR sensor failure | (a) Check sensor health; (b) check for topology change (line reconfiguration); (c) increase Q to make filter more responsive; (d) reinitialize P |
| Innovation drifting away from zero mean | Systematic model bias | (a) Check conductor parameter table (aging); (b) check ambient weather input accuracy |
| Innovation autocorrelated | Missing model structure | Add model terms or increase Q to cover unmodeled dynamics |

**Interview narrative:** "I monitor the innovation sequence at each step. If the sequence drifts
from zero mean or NIS consistently exceeds the chi-squared threshold, that's a divergence flag.
My first question is whether the sensor failed or the model is wrong. In a grid context, a
sudden jump in NIS might mean a line reconfiguration that changed the line section we're
monitoring — the topology changed and my measurement model h(Tc) now applies to a different
physical section."

---

## 6. DLR Caveat — When DLR Decreases Capacity

**Critical interview point:** Dynamic Line Rating does NOT universally increase capacity.

**Why:** Static ampacity ratings are computed under conservative worst-case weather:
- Typical worst-case assumptions: 0.6 m/s perpendicular wind, 40°C ambient, full sun (900 W/m²)
- These assumptions ensure the static rating is safe under nearly all field conditions

**When DLR is LOWER than static:**
- Hot, calm day: Tc_ss at nominal current is higher than the static model assumed
- Low wind: Natural convection alone is much less effective than 0.6 m/s forced convection
- High ambient temperature: Less temperature gradient (Tc − Ta), weaker convective cooling

**Quantitative from our worked example:**
- At I = 500 A, 25°C ambient, calm: Tc_ss ≈ 73°C (nearly at limit)
- DLR I_max at 75°C limit ≈ 531 A
- Static nameplate under worst-case assumptions: ~900 A
- But on a 35°C ambient, calm day: DLR I_max < 531 A — conductor might already be at limit
  with far less than 900 A flowing

**Where DLR adds value:**
- Cool nights: ambient 15°C instead of 40°C → dramatic capacity increase
- Windy days: 5 m/s wind → convective cooling 3–5x higher than 0.6 m/s baseline
- Coastal/elevated locations with persistent wind: average DLR significantly above static

**One-liner for the interview:** "DLR is a real-time thermal truth, not a capacity uplift tool.
On bad weather days, it accurately reduces the safe rating — which static ratings would miss,
potentially allowing overloading. The 10–40% average capacity gain is a fleet-level statistic
across all weather conditions, not a guarantee for any given moment."

---

## 7. Building-RC <-> Conductor-ODE Isomorphism

This section makes the explicit connection between Juan's existing work (building thermal state
estimation in OSED) and the IEEE 738 DLR problem. This is the structural analogy that
differentiates this answer from any standard Kalman filter description.

### Side-by-Side ODE Comparison

**Building thermal RC model (Juan's OSED work):**
```
C · dT_building/dt = Q_HVAC - UA · (T_building - T_ambient)
```

**IEEE 738 conductor thermal model:**
```
mCp · dTc/dt = I²R(Tc) - qc(Tc, Ta, v_wind) - qr(Tc, Ta) + qs
```

Both are **first-order thermal systems** (approximately linear in the state near steady state).
Both have:
- A thermal capacitance term on the left (energy storage)
- A measurable/controllable heat source on the right (HVAC load vs. I²R)
- A temperature-dependent cooling term (UA loss vs. convection + radiation)
- A hidden temperature state we want to estimate

### Structural Mapping Table

| Building RC Parameter | Conductor ODE Parameter | Role in the EKF |
|-----------------------|------------------------|-----------------|
| C (thermal capacitance, J/°C) | mCp (heat capacity/m, J/(m·°C)) | Sets thermal time constant τ = C/UA or mCp/UA_eff; governs how fast the state changes |
| Q_HVAC (heat input, W) | I²·R(Tc) (resistive heating, W/m) | Controllable/measurable heat source; the primary driver of state change |
| UA·(T − Ta) (linear loss, W) | qc + qr (convective + radiative loss, W/m) | Heat loss to environment; nonlinear in T_conductor (stronger nonlinearity than building) |
| T_building (hidden state, °C) | Tc (conductor temp, °C) | The state we cannot measure directly; what the EKF estimates |
| T_ambient (measured input, °C) | Ta (ambient weather input, °C) | External disturbance that drives the cooling term |
| Sensor noise R (°C²) | PMU/CT resistance noise R (Ω²/m²) | Measurement uncertainty parameterized in the EKF update step |

### Time Constants

| System | Thermal Capacitance | Effective Conductance | Time Constant |
|--------|--------------------|-----------------------|---------------|
| Office building zone (medium) | C ~ 5×10⁶ J/°C | UA ~ 1000 W/°C | τ ~ 83 min |
| Drake ACSR conductor | mCp = 534 J/(m·°C) | UA_eff ~ 30 W/(m·°C) at moderate wind | τ ~ 18 min |
| Drake ACSR, high wind | mCp = 534 J/(m·°C) | UA_eff ~ 80 W/(m·°C) | τ ~ 7 min |

The conductor is faster than a building by 5–10x, but the EKF structure is identical.

### The Key Bridge Sentence

"My building thermal state estimator and the IEEE 738 DLR model share identical ODE structure:
a first-order thermal system where the hidden temperature state is driven by a measurable heat
source (HVAC load or I²R), cooled by an ambient-dependent loss term (UA loss or convection +
radiation), and corrupted by model uncertainty from unmodeled inputs. Swapping building RC
parameters for ACSR conductor parameters is a **parameter substitution, not a conceptual leap**.
The EKF predict-update cycle, the Q/R tuning logic, the innovation monitoring, and the
divergence detection procedure are the same in both applications. The only new element is the
specific physical interpretation of each parameter — mCp instead of C, I²R(Tc) instead of
Q_HVAC, and the four-term heat balance instead of the two-term RC equation."

### Interview Delivery

When the interviewer asks: "Have you worked with Kalman filters on power systems?"

**Answer structure:**
1. "Not directly on power systems, but I've implemented a thermal state estimator for buildings
   that shares identical mathematical structure with the IEEE 738 DLR problem."
2. Walk through the mapping table above (C↔mCp, Q_HVAC↔I²R, UA↔qc+qr).
3. "The EKF predict step discretizes the ODE in exactly the same way. The Q and R tuning
   reflects model uncertainty from unmodeled disturbances and sensor accuracy — same logic
   whether the disturbance is an occupancy spike or a wind gust."
4. Offer to trace the specific numbers (Section 3 above) to show the mechanics.

---

## 8. Quick-Reference Card (for Oral Review)

**The ODE:**
`mCp·dTc/dt = I²R(Tc) + qs - qc - qr`   (heating left → right = gain − loss)

**EKF state:** x = [Tc]; inputs u = [I, Ta, v_wind, qs]

**Key formulas:**
- R(Tc) = R25·[1 + 0.00403·(Tc − 25)]
- Predict: Tc_pred = Tc + (1/534)·net_heat
- Process Jacobian A = 1 + (1/534)·[I²·dR/dTc − dqc/dTc − dqr/dTc]
- Measurement: h(Tc) = R25·[1 + alpha_R·(Tc − 25)]  → H = R25·alpha_R = 2.934e-7 Ω/(m·°C)
- Innovation: y = z_meas − h(Tc_pred)
- Gain: K = H·P_pred / (H²·P_pred + R)   [scalar form]
- Update: Tc_post = Tc_pred + K·y;  P_post = (1 − K·H)·P_pred

**Q:** process noise — model uncertainty (wind, aging). Never zero. Start at 0.01–0.1°C²/step.
**R:** sensor noise — CT accuracy + resistance inference. Start at ~(1e-7)² Ω²/m².

**Innovation must be:** zero-mean, white, Gaussian with covariance S.

**NIS = y²/S ~ chi²(1); flag divergence if NIS > 3.84 (chi2.ppf(0.95, df=1)).**

**DLR caveat:** hot calm day → DLR LOWER than static nameplate. This is correct behavior.

**Bridge sentence:** "Swapping building RC parameters for ACSR conductor parameters is a
parameter substitution, not a conceptual leap."

---

## Sources

- IEEE Std 738-2006/2012 (paywalled; ODE structure from secondary sources)
- stevenblair/ieee738matlab GitHub — verified ODE implementation and ACSR Drake parameters
- Welch & Bishop, "An Introduction to the Kalman Filter" (Edinburgh CVonline) — EKF equations
- arxiv.org/abs/2012.06069 — EKF for power system dynamic state estimation
- arxiv.org/pdf/2106.10775 — covariance matching and chi-squared divergence detection
- arxiv.org/pdf/1702.00884 — adaptive Q/R update (Sage-Husa)
- 01-RESEARCH.md sections "IEEE 738 Thermal Model", "EKF for Line Temperature", "Innovation Sequence and Divergence Detection", "Common Pitfalls"
