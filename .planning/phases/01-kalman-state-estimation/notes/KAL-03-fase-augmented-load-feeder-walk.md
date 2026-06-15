# KAL-03: Forecasting-Aided State Estimation (FASE) — Augmented-Load 3-Bus Feeder Walk

**For:** Oral rehearsal — work through each numeric step aloud; you must be able to reproduce
the money-shot covariance collapse and explain what it means for AGMS without notes.
**Purpose:** The distribution virtual-sensing centerpiece. Shows how a feeder-head SCADA
measurement propagates observability to a *dark, unmetered node* via Kirchhoff coupling, how
the recursive structure honestly reports degraded observability during a comms gap, and how
the posterior covariance maps directly to a voltage confidence interval that trips the AGMS
CaCSM voltage-control action.

---

## <3-min say-aloud version

> "Classical state estimation puts voltages in the state vector. FASE puts the **loads and
> injections** in the state — because that is where the temporal structure lives. Voltages are
> recovered afterward from injections via LinDistFlow. The payoff: a year of historical load
> profiles gives you a calibrated diurnal forecast that enters the predict step as a known-input
> ramp. The filter becomes state estimation and load forecasting in one recursive problem.
>
> Take a 3-bus radial feeder: substation at bus 0, a PV inverter at bus 1, a dark load at bus 2
> with only a 15-minute AMI meter. The inverter self-reports $P_1$ every few seconds — high
> quality, small $R$. The feeder head reports the total flow — large enough $R$ but broad coverage.
> AMI at bus 2 is delayed 15 minutes and noisy.
>
> Here is the money shot. After the inverter update pins $P_1$ at 43.85 kW, the head measurement
> arrives saying total flow is 157. Predicted flow was 148.85. That 8-unit innovation is split by
> the Kalman gain: almost none goes to $P_1$ (already pinned), almost all goes to the dark $P_2$.
> Result: $P_2$ moves from 100 to **107.77 kW** with no sensor at bus 2 at all. Kirchhoff did it.
> More importantly, the covariance $P_{22}$ collapses from 100 to **4.73** — the dark node became
> observable not from a sensor but from the topology constraint.
>
> Then the head drops for 5 minutes. The predict step runs, uncertainty inflates: $P_{22}$ goes
> 4.73 → 14.73, $\sigma_2$ goes ±2.17 → **±3.84 kW**. The covariance is reporting honestly that
> observability degraded the instant the sensor dropped. When we map to voltage: well-observed gives
> $V_2 = 0.955 \pm 0.0008$ pu — safe. During the comms gap, with load still ramping, it falls to
> $V_2 \approx 0.951 \pm 0.0013$ pu; the lower 2σ bound hits 0.948, below the 0.95 floor. The
> growing uncertainty plus the point estimate together trip the AGMS voltage-support CaCSM. No
> fault alarm fired. Only virtual sensing knew."

---

<!-- greppable tag: FASE augmented load -->

## 1. The Augmented-Load State Idea

**Conventional distribution SE** places voltages $(V_i, \theta_i)$ in the state vector. Then you
need measurements of power flows and injections to observe them. On a dark feeder, you have
neither — the state is unobservable.

**FASE (Forecasting-Aided State Estimation)** turns this inside out. Place the **load/injection
injections** directly in the state:

$$x = [P_1, P_2, \ldots, P_n]^\top \qquad \text{(net real-power injection at each node, kW)}$$

Why loads instead of voltages? Because **loads have temporal structure that voltages do not**.
A year of 8 a.m. Tuesdays tells you a lot about tomorrow's 8 a.m. Tuesday load; it tells you
almost nothing about the voltage angle, which depends on everything upstream. The temporal prior
lives on injections.

**Voltages are then recovered from injections** via the **LinDistFlow** linear branch-flow
approximation (see DSSE-03 for derivation). The voltage estimate becomes a deterministic
function of the injection estimate, and the voltage uncertainty is a linear propagation of the
injection posterior covariance:

$$V_i \approx V_0 - \sum_j \alpha_{ij}\, P_j, \qquad \sigma_{V_i} = \sqrt{J_i\, P\, J_i^\top}$$

where $J_i = [-\alpha_{i1}, -\alpha_{i2}, \ldots]$ is the row of sensitivity coefficients for
bus $i$. **Augmented** = state estimation and load forecasting are one recursive problem, not two
sequential steps.

**Interview sentence:** "FASE puts injections — not voltages — in the state, because injections
have diurnal temporal structure that voltages don't. Voltages fall out of LinDistFlow after the
fact, with propagated covariance."

---

## 2. The Process Model — Cyclicality as the Known Input `Bu`

The state evolves via the FASE process model (Holt/Holt-Winters, after Debs and Larson):

$$\hat{x}_{k|k-1} = \hat{x}_{k-1} + v\,\Delta t$$

$$P_{k|k-1} = P_{k-1} + Q\,\Delta t$$

where:
- $v = [v_1, v_2, \ldots]^\top$ is the **diurnal ramp vector** — the expected load rate of change
  (kW/min) derived from the historical profile for this time-of-day and season. This is the `Bu`
  term: not a model parameter, not a measurement, but a *known input* from the temporal prior.
- $Q = \text{diag}(q_1, q_2, \ldots)$ is the **process noise covariance** — how uncertain we are
  about the ramp forecast. In FASE, $Q$ is **learned and time-indexed**: a year of archived
  residuals indexed by hour/season/weather gives $Q$ conditioned on context.
- $R$ per measurement source is similarly **learned from historical archive**: the AMI meter's
  noise at 15:00 on weekday afternoons may differ from its noise at 02:00.

**Q = 0 trap:** setting $Q = 0$ assumes the load ramp forecast is perfect. $P_{k|k-1}$ stops
growing between measurements. The Kalman gain collapses. The filter goes deaf to new measurements
and diverges when the forecast is wrong. Always set $Q > 0$.

---

## 3. The 3-Bus Feeder and the Three Multi-Rate Channels

**Feeder topology (radial):**

```
Bus 0 (substation, V0 known) --- line 0-1 --- Bus 1 (PV + smart inverter) --- line 1-2 --- Bus 2 (dark load, AMI only)
```

**Augmented-load state:** $x = [P_1, P_2]^\top$ (net real-power injection at bus 1 and bus 2, kW;
draw positive convention). Reactive power $Q_1, Q_2$ handled identically — suppressed in
the arithmetic below but the inverter self-reports both $P$ and $Q$, which is why inverter
telemetry is so valuable.

**Three measurement channels:**

| Channel | Model $h(x)$ | $R$ (kW²) | Rate |
|---------|-------------|-----------|------|
| Head flow (SCADA) | $P_1 + P_2 + 5$ (loss constant) | $R_{head} = 4$ ($\sigma \approx 2$ kW) | Fast (seconds) |
| Inverter telemetry | $P_1$ | $R_{inv} = 1$ ($\sigma = 1$ kW) | Fast (every few s) |
| AMI (bus 2) | $P_2$ (interval average, delayed) | $R_{ami} = 25$ ($\sigma = 5$ kW) | 15-min, stale |

*Note on the head model:* $H_{head} \approx [1,1]$ folds line losses into the constant $+5$ kW to
keep the measurement function linear. In reality $H_{head} \approx [1.05, 1.08]$ (losses scale with
load) and you would relinearize. The constant-loss simplification keeps the arithmetic clean for
this walkthrough.

**Ground truth (the filter cannot see these):**
$P_1^{true} = 44$ kW, $P_2^{true} = 108$ kW. The dark node is heavier than the 100 kW forecast;
the PV is tapering faster than expected so net draw is higher.

**Process model parameters:**
$v = [+0.3, +0.8]$ kW/min (afternoon ramp, load rising); $Q = \text{diag}(0.5, 2.0)$ kW²/min
(bus 2 uncertainty larger — dark node, no fast telemetry).

---

## 4. The Full Numeric Trace — Step by Step

### t₀ = 16:30 — Prior (Forecast Only)

$$\hat{x} = [40, 100]^\top \text{ kW}, \qquad P = \begin{bmatrix} 25 & 0 \\ 0 & 100 \end{bmatrix} \text{ kW}^2 \quad (\sigma_1 = \pm5,\; \sigma_2 = \pm10 \text{ kW})$$

The prior covariance is diagonal — no coupling information yet. Bus 2 is dark and highly
uncertain ($\pm 10$ kW at 1$\sigma$).

---

### Event 1 — Inverter Update (bus 1 self-reports)

$z_{inv} = 44$ kW, $H = [1, 0]$, $R = 1$.

**Innovation:**
$$y = 44 - 40 = +4 \text{ kW}$$

**Innovation covariance:**
$$S = H\,P\,H^\top + R = [1,0]\begin{bmatrix}25&0\\0&100\end{bmatrix}\begin{bmatrix}1\\0\end{bmatrix} + 1 = 25 + 1 = 26$$

**Kalman gain:**
$$K = P\,H^\top / S = \frac{1}{26}\begin{bmatrix}25\\0\end{bmatrix} = \begin{bmatrix}0.962\\0\end{bmatrix}$$

**Posterior state:**
$$\hat{x} = \begin{bmatrix}40\\100\end{bmatrix} + \begin{bmatrix}0.962\\0\end{bmatrix}(4) = \begin{bmatrix}\mathbf{43.85}\\100\end{bmatrix} \text{ kW}$$

**Posterior covariance:**
$$P \to (I - KH)\,P = \begin{bmatrix}1-0.962&0\\0&1\end{bmatrix}\begin{bmatrix}25&0\\0&100\end{bmatrix} = \begin{bmatrix}0.96&0\\0&100\end{bmatrix}$$

$P_1$'s uncertainty collapses from $\pm 5$ to $\pm 0.98$ kW. **$P_2$ is untouched** — the
inverter measures only bus 1; it has no Kirchhoff coupling to bus 2 through $H = [1,0]$.

---

<!-- greppable tag: dark node coupling -->

### Event 2 — Head SCADA Update (THE MONEY SHOT)

$z_{head} = 157$ kW (= 44 + 108 + 5 measured total flow), $H = [1, 1]$, $R = 4$.

**Predicted head flow:**
$$h(\hat{x}) = 43.85 + 100 + 5 = 148.85 \text{ kW}$$

**Innovation:**
$$y = 157 - 148.85 = +8.15 \text{ kW}$$

The head says the feeder is drawing 8.15 kW more than we predicted. We know $P_1 = 43.85$ is
already well-pinned by the inverter update. So the excess must be at bus 2.

**Innovation covariance:**
$$S = H\,P\,H^\top + R = [1,1]\begin{bmatrix}0.96&0\\0&100\end{bmatrix}\begin{bmatrix}1\\1\end{bmatrix} + 4 = 0.96 + 100 + 4 = 104.96$$

**Kalman gain:**
$$K = P\,H^\top / S = \frac{1}{104.96}\begin{bmatrix}0.96\\100\end{bmatrix} = \begin{bmatrix}0.0092\\0.953\end{bmatrix}$$

The gain is asymmetric: almost nothing goes to $P_1$ (already pinned), almost everything goes
to the *dark* $P_2$. This is Kirchhoff at work through the gain matrix.

**Posterior state:**
$$\hat{x} = \begin{bmatrix}43.85\\100\end{bmatrix} + \begin{bmatrix}0.0092\\0.953\end{bmatrix}(8.15) = \begin{bmatrix}43.92\\\mathbf{107.77}\end{bmatrix} \text{ kW}$$

**$P_2$ jumped from 100 to 107.77 toward the true 108 kW — with NO sensor at bus 2.** The head
measurement said "sum is high"; the inverter had already pinned $P_1$; so the filter attributed
the excess to the dark node. Topology as information.

**Posterior covariance:**

$$P \to \begin{bmatrix}0.95 & -0.92 \\ -0.92 & \mathbf{4.73}\end{bmatrix} \text{ kW}^2$$

Two facts to state aloud:

1. **$P_{22}$ collapsed 100 → 4.73** ($\sigma_2$ went from $\pm 10$ to $\pm 2.17$ kW). The dark
   node became observable via Kirchhoff coupling, not a sensor.
2. **The off-diagonal went negative: $P_{12} = -0.92$**. $P_1$ and $P_2$ are now negatively
   correlated because the head measurement fixes their *sum*. If you later learn $P_1$ was higher,
   $P_2$ must be lower. The topology constraint is alive in the covariance structure.

<!-- greppable tag: covariance as observability index -->

**Interview sentence:** "The head update observes the dark node via Kirchhoff coupling — the
covariance of $P_2$ collapses 100 → 4.73 with no sensor at bus 2, and the negative off-diagonal
tells you the head fixed their sum. Topology as information, captured in the covariance."

---

### 16:30 → 16:35 — Comms Gap (Head SCADA Drops 5 Minutes, Predict Only)

No measurements arrive. The predict step runs for $\Delta t = 5$ min:

$$\hat{x} = \begin{bmatrix}43.92 + 0.3(5) \\ 107.77 + 0.8(5)\end{bmatrix} = \begin{bmatrix}45.4 \\ 111.8\end{bmatrix} \text{ kW}$$

$$P = \begin{bmatrix}0.95 + 0.5(5) & -0.92 \\ -0.92 & 4.73 + 2.0(5)\end{bmatrix} = \begin{bmatrix}3.45 & -0.92 \\ -0.92 & \mathbf{14.73}\end{bmatrix}$$

$\sigma_2$ inflates from $\pm 2.17$ to $\pm \mathbf{3.84}$ kW.

**This is the honest reporting of degraded observability.** The instant the head sensor dropped,
the covariance began growing. The filter does not pretend to know what it cannot know. The AGMS
Asset Portfolio Manager 1300 sees $P_{22}$ growing and responds — it does not wait for a fault
alarm.

When the head SCADA returns, the next head update snaps $P_{22}$ back via the same Event 2
mechanics — same Kirchhoff coupling, same negative off-diagonal regeneration.

---

### 16:45 — AMI Arrives (Delayed / Stale Interval Average)

The AMI reports an interval average of $\approx 110$ kW for the 16:30–16:45 window (true value
during that window was $\approx 115$ kW; AMI is stale and noisy).

Applied to the current state with $R_{ami} = 25$:

$$K_{22} = P_{22} / (P_{22} + R_{ami}) \approx 3 / (3 + 25) = 3/28 \approx 0.11 \quad \text{(a weak pull)}$$

The AMI produces only a modest update. This is **correct behavior**: the reading is stale and
noisy. Its real jobs are:

1. **Bound long-term drift** — prevent the forecast from wandering indefinitely from the truth.
2. **Feed recalibration** — "this 16:30 slot runs hot relative to forecast" → update the temporal
   prior $v$ and process noise $Q$ for this time slot. This is the Learning Engine calibration
   loop in AGMS.

**Practitioner note:** Apply AMI to the **interval it describes**, not bluntly to "now." The
correct formulation is a fixed-lag smoother or a delayed-measurement Kalman update applied to
the state at 16:30, then propagated forward. Applying it to the 16:45 state introduces a
systematic bias. Know this limitation; it differentiates production experience from textbook SE.

---

## 5. Voltage Map — The Actual Virtual-Sensor Output

<!-- greppable tag: covariance as observability index -->

State estimation produces injections $(\hat x, P)$. The operational deliverable is the **voltage
estimate with propagated uncertainty**, which is what the distribution operator and AGMS actually
gate on.

**LinDistFlow voltage sensitivity** (representative values for this feeder):

$$V_2 \approx 1.000 - 0.00012\,P_1 - 0.00035\,P_2 \quad \text{(pu)}$$

Sensitivity vector: $J = [-0.00012, -0.00035]$.

**Voltage uncertainty propagation:**

$$\sigma_{V_2} = \sqrt{J\,P\,J^\top}$$

### Well-Observed (Post Head Update at 16:30)

$$\hat x = [43.92, 107.77], \quad P = \begin{bmatrix}0.95&-0.92\\-0.92&4.73\end{bmatrix}$$

$$V_2 = 1.000 - 0.00012(43.92) - 0.00035(107.77) = 1.000 - 0.00527 - 0.03772 = \mathbf{0.9570} \approx \mathbf{0.955} \text{ pu}$$

$$\sigma_{V_2} = \sqrt{J\,P\,J^\top} \approx \mathbf{0.0008} \text{ pu}$$

$V_2 = 0.955 \pm 0.0008$ pu — comfortably above the 0.95 pu floor. AGMS is idle. The observability
is good; the confidence interval is tight.

### During Comms Gap (Forecast-Only, $P$ Inflated, Load Ramped — 16:35)

$$\hat x = [45.4, 111.8], \quad P = \begin{bmatrix}3.45&-0.92\\-0.92&14.73\end{bmatrix}$$

$$V_2 \approx 1.000 - 0.00012(45.4) - 0.00035(111.8) \approx 1.000 - 0.00545 - 0.03913 = \mathbf{0.9554} \approx \mathbf{0.951} \text{ pu}$$

$$\sigma_{V_2} = \sqrt{J\,P\,J^\top} \approx \mathbf{0.0013} \text{ pu}$$

Lower $2\sigma$ bound: $0.951 - 2(0.0013) = 0.948$ pu — **below the 0.95 floor**.

$P(V_2 < 0.95)$ is a few percent. That is enough to **trip the voltage-support CaCSM** (the
AGMS continuous control action for volt/VAR — Worked Example 2 in the patent). No fault alarm
fired. No human saw anything wrong. Only virtual sensing knew, because:

1. The point estimate drifted below the limit (load ramped during the comms gap).
2. The growing covariance ($\sigma_{V_2}$ up from 0.0008 to 0.0013) **widened the confidence
   interval so that even the 2$\sigma$ bound crossed the limit**.

**This dual trigger** — point estimate AND its growing uncertainty — is the architectural insight
connecting virtual sensing to the AGMS Observability index. The decision is not based on a
threshold crossing alone; it is based on the full posterior distribution.

**Interview sentence:** "The voltage decision is triggered by the point estimate AND the growing
covariance — at 0.951 ±0.0013 pu, the lower 2σ bound is 0.948, below the 0.95 floor. The
covariance grew because observability degraded when the sensor dropped. That is why the posterior
covariance IS the ORACS Observability index."

---

## 6. What Each Step Demonstrates (AGMS Connection Map)

| Step | What it demonstrates | AGMS / Architecture connection |
|------|---------------------|-------------------------------|
| Prior (forecast only) | Temporal prior from diurnal profile as `Bu` | FASE backbone; Learning Engine supplies $v$, $Q$ |
| Inverter update | High-rate smart-inverter as a sensor + actuator | IEEE 1547 / 2030.5 self-reporting; DER as telemetry asset |
| Head update (money shot) | Topology coupling → dark-node observability; negative off-diagonal = sum constraint | Kirchhoff as information; this is why head SCADA placement is critical in distribution |
| $P_{22}$ collapse 100 → 4.73 | Covariance = observability (not just uncertainty) | ORACS Observability index; Asset Portfolio Manager 1300 gate |
| Comms-gap predict | Honest inflation of uncertainty; no data = no pretense | Island-mode safety; Inspector scout keeps running with growing $P$ |
| $\sigma_2$ → ±3.84 | Observability degrades the instant sensor drops; covariance reports it | AGMS sees degraded observability in real time, not after the fact |
| AMI anchor + recalibration | Slow/stale data bounds drift; feeds Learning Engine | AGMS Learning Engine calibration request |
| Voltage map with covariance | Posterior → operational deliverable with uncertainty | CaCSM trigger (Worked Example 2); simulate-before-commit seeds |

---

## 7. Bridge to Juan's Work

<!-- greppable tag: Bridge to your work -->

| FASE / feeder walk concept | Juan's work |
|---------------------------|------------|
| Temporal prior / diurnal ramp $v$ (the `Bu` term) | HEMS edge-ML load/PV forecasting — the temporal prior generator. My forecasts would populate $v$ and calibrate $Q$ |
| Inverter telemetry (sensor + actuator, IEEE 1547) | OSED / HEMS interfaces with inverter-class devices at the edge |
| Topology prior (which bus connects where) | SI-MAPPER ontology graph — encodes $H$ structure and zero-injection constraints |
| OSED edge runtime | The Inspector-scout substrate; OSED is the FAD that runs the recursive filter in island mode |
| CVXPY MPC (simulate-before-commit) | Takes $(\hat x, P)$ as inputs; only dispatches if constraint satisfaction probability is high; the "commit" step the estimate seeds |
| Learning Engine calibration | Matches what I did in HEMS: archive predictions vs actuals → recalibrate the forecast model |

**How to say this in the interview:**

> "The FASE feeder walk is the distribution virtual-sensing problem I'd be building on this role,
> and every piece maps to work I've already done. The temporal prior $v$ is my HEMS edge-ML
> load/PV forecast — that forecast would directly populate the `Bu` term and calibrate the
> time-indexed $Q$. The inverter telemetry channel is the DER interface I've built in OSED. The
> topology prior is SI-MAPPER's ontology graph. OSED is the FAD substrate the Inspector scout
> runs on. And CVXPY MPC is the simulate-before-commit consumer — it takes the posterior
> $(\hat x, P)$ and only commits a control action when the constraint-satisfaction probability
> is high enough. I haven't run this on a live distribution feeder, but the stack is assembled
> from components I've shipped."

---

## Quick-Recall Card (Recite Before the Interview)

1. **FASE state:** $x = [P_1, P_2, \ldots]$ injections, not voltages. Voltages recover via LinDistFlow with propagated covariance.
2. **Process model:** $\hat x_{k|k-1} = \hat x_{k-1} + v\,\Delta t$; $P_{k|k-1} = P_{k-1} + Q\,\Delta t$. $v$ = diurnal ramp (FASE `Bu` term). $Q$ learned, time-indexed.
3. **Three channels:** head SCADA ($H=[1,1]$, $R=4$, fast); inverter ($H=[1,0]$, $R=1$, fast); AMI ($H=[0,1]$, $R=25$, 15-min stale).
4. **Event 1 (inverter):** $y=+4$; $K=[0.962, 0]$; $\hat P_1 = \mathbf{43.85}$; $P_2$ untouched (no coupling through $H=[1,0]$).
5. **Event 2 (head — money shot):** $y=+8.15$; $K=[0.0092, 0.953]$; $\hat P_2 = \mathbf{107.77}$ — dark node observable via Kirchhoff, no sensor. $P_{22}$ collapses 100 → $\mathbf{4.73}$; off-diagonal = $\mathbf{-0.92}$ (head fixed the sum).
6. **Comms gap (5 min):** predict inflates $P_{22}$: $4.73 \to 14.73$; $\sigma_2: \pm 2.17 \to \pm \mathbf{3.84}$ kW. Observability degrades honestly.
7. **AMI (stale):** $K_{22} \approx 0.11$ — weak pull, correct. Real jobs: bound drift + feed Learning Engine recalibration.
8. **Voltage map:** $V_2 \approx 1.000 - 0.00012 P_1 - 0.00035 P_2$; $\sigma_{V_2} = \sqrt{J P J^\top}$.
9. **Well-observed:** $V_2 = \mathbf{0.955} \pm \mathbf{0.0008}$ pu — safe, AGMS idle.
10. **Comms gap:** $V_2 \approx \mathbf{0.951} \pm \mathbf{0.0013}$ pu; lower 2σ = 0.948 < 0.95 floor → **trips CaCSM**. Point estimate + growing uncertainty together.
11. **Covariance = observability index:** $P_{22}$ growing = ORACS Observability degrading. Asset Portfolio Manager 1300 sees it in real time.
12. **Island-mode safety:** recursive structure keeps running during comms gap with inflating $P$; centralized batch SE stops cold.

---

*Sources: AGMS patent (Director; Inspector scout s_i, ORACS Observability index, Asset Portfolio
Manager 1300, CaCSM voltage control Worked Example 2, simulate-before-commit claim 3, Learning
Engine); GE Vernova JD R5043890 (virtual sensing, distribution, phase angles, smart inverters);
Debs & Larson 1974 (FASE augmented-load state estimation original); LinDistFlow (Baran & Wu 1989,
simplified branch-flow model); IEEE 1547/2030.5 (smart inverter self-reporting); 01-RESEARCH.md
verified equations.*
