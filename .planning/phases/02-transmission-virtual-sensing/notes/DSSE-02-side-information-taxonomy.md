# DSSE-02: The Side-Information Taxonomy — Mapping Every Source Into the Estimator

**For:** Oral rehearsal — speak through the taxonomy table top-to-bottom; you must be able to
explain where each source enters the filter (measurement vs. process model vs. structural
constraint vs. learned prior) without notes.
**Purpose:** The organizing framework for distribution virtual sensing. Every source of
side-information the grid offers can be cast into exactly one of four estimator roles. Knowing
this taxonomy cold lets you answer "how would you handle [X] data source?" for any source the
interviewer names — because you can immediately say where it enters and with what covariance.

---

## <3-min say-aloud version

> "The classic state estimation curriculum treats the measurement set as given and asks how to
> solve the WLS problem. In distribution virtual sensing, **the measurement set is the design
> choice**. Every piece of information the grid offers — a topological constraint, a historical
> load profile, a smart inverter's self-report, a delayed AMI reading, an ML forecast — can be
> cast into the estimator in one of four ways: as a **measurement** $z$ with noise covariance $R$,
> as a **process model** input (the $F$ or $Bu$ term), as a **hard structural constraint** (a
> virtual measurement with $R \to 0$), or as a **learned prior** that calibrates $Q$ and $R$
> from the historical archive.
>
> The taxonomy is the discipline. Network topology defines the $H$ matrix — Kirchhoff coupling is
> what lets the feeder-head measurement carry information downstream to unmetered nodes. Known-
> passive nodes contribute zero-injection virtual measurements that are essentially free information.
> Load cyclicality enters as the FASE process model — a year of archived 8 a.m. Tuesdays
> constrains tomorrow's 8 a.m. DER sources (smart inverters, batteries, EVSEs) are simultaneously
> sensors and actuators — they self-report their terminal $P$, $Q$, $V$, giving you measurement
> points the feeder never had before DER penetration.
>
> The crucial discipline: every source must enter with an **honest covariance**. An overconfident
> pseudo-measurement — an ML forecast whose uncertainty is underestimated — becomes a de-facto
> leverage measurement at scale: a belief the filter trusts blindly, invisible to bad-data
> detection. The taxonomy is not just about where each source enters; it is about assigning the
> right $R$ so the filter knows how much to trust it."

---

<!-- greppable tag: side-information taxonomy -->

## 1. The Four Estimator Roles

Every information source falls into one of four categories:

| Role | What it is | How it enters the estimator |
|------|-----------|----------------------------|
| **Measurement** $z$ | Direct or indirect observation with noise | Update step: $y = z - h(\hat x)$; weighted by $R^{-1}$ |
| **Process model** ($F$, $Bu$, $Q$) | How state evolves; known input; model uncertainty | Predict step: $\hat x \leftarrow F\hat x + Bu$; $P \leftarrow FPF^\top + Q$ |
| **Structural constraint** | Hard physical fact (zero injection, flow balance) | Virtual measurement: $z = 0$ with $R \to 0$ (near-infinite weight) |
| **Learned prior** | Historical archive indexed by context | Calibrates $Q$, $R$, $Bu$ (the `v` ramp vector) for each time slot |

Most grid information sources contribute to more than one role across time. The discipline is
knowing which role is primary and what covariance to assign.

---

## 2. The Full Side-Information Taxonomy Table

| Source | What it is, physically | Where it enters the estimator | Covariance / notes |
|--------|----------------------|------------------------------|-------------------|
| **Network topology** (who connects to whom) | Radial graph of lines and buses | Defines the structure of $H$ — Kirchhoff coupling lets the head SCADA measurement carry information downstream to unmetered dark nodes | Structural; $H$ entries are susceptances / line parameters |
| **Known injecting vs. passive nodes** | Which buses have DER vs. pure consumers | Zero-injection nodes → near-zero-$R$ **virtual measurements** ($z=0$); passive nodes → load-sign constraint (one-sided prior); DER nodes → injection can reverse | $R_{zero\text{-}inj} \to 0$ (hard fact, not a sensor guess) |
| **Conductor / line parameters, ratings** | Line impedances (resistance, reactance), thermal ratings | The *parameters* of $h(x)$ and the power-flow model; recovering them (line parameter estimation) shrinks $Q$; also unlocks IEEE 738 / C57.91 asset-health virtual sensors | Distribution params are fuzzy → LinDistFlow + absorb error into $Q$ |
| **Power-flow equations** | Kirchhoff coupling between buses | The hard constraints $h(x)$ tying measured and unmeasured nodes in the update step; what lets one head measurement observe multiple downstream nodes | Distribution PF is less accurate (unbalanced, high $R/X$) than transmission |
| **Load cyclicality / repeating profiles** | Diurnal/weekly seasonality in load | **Process model $F$, known input $Bu$** (FASE backbone): $\hat x \leftarrow \hat x + v\,\Delta t$ where $v$ = diurnal ramp vector; a year of 8 a.m. Tuesdays constrains tomorrow's 8 a.m. | $Q$ = uncertainty in the forecast; also time-indexed |
| **Historical predictions + actuals + noise, indexed by time** | The archive of past estimates, measurements, and residuals per time-of-day / season / weather | **Learned, time-varying $Q$ and $R$**, conditioned on context; calibrated pseudo-measurement covariances | Source of the Learning Engine calibration requests in AGMS |
| **Smart meters (AMI)** | Slow (15-min interval avg), dense, delayed | Low-rate measurement channel; anchors load pseudo-measurements with real energy data; bounds long-term drift | $R_{ami}$ large (stale + noisy); apply to the interval it describes, not "now" |
| **EV chargers** | Real-time, event-driven, large load steps | High-rate measurement when charging (OCPP / MQTT telemetry); absent between sessions | $R_{EV}$ moderate; temporal pattern (evening peak) enters $Bu$ |
| **Batteries / smart inverters** | Self-reporting actuators (IEEE 1547 / IEEE 2030.5) | **Sensor + actuator**: inverter knows its own terminal $P$, $Q$, $V$; DER adds measurement points for free; self-report is a direct measurement $z = P_{inv}$ | $R_{inv}$ small (factory-calibrated; direct self-measurement) |
| **Multi-rate asynchronous arrival** | Different comm frequencies across sources | Native KF strength — **update on arrival with each source's own $R$; run predict between each arrival** | Not a source itself; a fusion pattern that handles heterogeneous rates |
| **ML load/PV/DER forecasts** | Learned priors from edge-ML models | High-quality **pseudo-measurements with calibrated covariance** — Juan's HEMS/Building-Intelligence forecasting work is exactly this | $R_{pseudo}$ from forecast error archive; calibrated covariance is the critical discipline |

---

## 3. Walking Through Each Source (Oral Practice)

Practice saying one sentence per source. Then practice explaining where it enters:

**Network topology:** "The graph defines the $H$ matrix. Kirchhoff coupling is how the head flow
carries information about nodes it doesn't directly observe — the core mechanism of distribution
virtual sensing."

**Zero-injection constraints:** "If I know a bus is a pure load node with no DER, its net
injection is near zero at high time resolution. I add a virtual measurement $z = 0$ with $R \to 0$.
That is real information, not a sensor guess, and it is essentially free — no hardware needed."

**Conductor parameters:** "Line impedances parameterize the power-flow model. Fuzzy parameters
(distribution feeders are less well-characterized than transmission) absorb into larger $Q$, not
into wrong $H$ entries."

**Load cyclicality:** "A year of historical load at 14:30 on weekdays tells me a lot about
tomorrow's 14:30 load. That enters as the `Bu` term — the known diurnal ramp in the FASE predict
step. This is the temporal-prior half of FASE."

**Historical archive:** "The archive lets me condition $Q$ and $R$ on time-of-day and weather.
At 8 a.m. on a cold winter Monday, load variance is higher than at 2 a.m. Saturday. The filter
should know that. AGMS's Learning Engine maintains this conditioned archive."

**AMI:** "Slow, dense, delayed. Its job is to bound long-term drift and to feed the Learning
Engine recalibration. It must be applied to the interval it describes, not bluntly to 'now'."

**EV chargers:** "Event-driven measurement when connected (OCPP). The temporal pattern — evening
charging peak — is learnable and enters $Bu$. Between sessions, no measurement, so the uncertainty
from that bus grows."

**Smart inverters / batteries:** "These are the most valuable new source. They self-report $P$,
$Q$, $V$ at their own terminal — a direct measurement with small $R$. They are simultaneously
measurement points and actuators. DER penetration adds measurement density for free."

**Multi-rate asynchronous fusion:** "The KF handles this natively. Run the predict step for
every time gap, apply the update step on each measurement arrival with that source's $R$. No
synchronization needed."

**ML forecasts:** "My HEMS edge-ML models produce calibrated probabilistic forecasts —
mean and variance for load and PV. These are pseudo-measurements: $z = \hat P_{forecast}$,
$R_{pseudo} = \sigma_{forecast}^2$. The calibration of $R_{pseudo}$ is the critical discipline."

---

## 4. The Honest Covariance Discipline (Why This Is the Hard Part)

Getting the taxonomy right is necessary but not sufficient. The dangerous failure mode is
**over-confident pseudo-measurements** — pseudo-measurements whose $R$ is set too small.

When $R_{pseudo}$ is too small, the filter trusts the pseudo-measurement blindly. It becomes a
de-facto leverage measurement: if the ML forecast is wrong, the filter cannot correct itself
because the fake "certainty" suppresses the Kalman gain for everything else. This is the
**critical-measurement trap replicated at scale** — except now it's a model belief rather than
a sensor reading.

The calibration chain:
1. Run ML forecasts on historical data; archive predicted value vs. actual.
2. Estimate the empirical distribution of forecast errors per time slot, season, weather context.
3. Set $R_{pseudo}$ from the empirical variance (not from model confidence scores, which are
   systematically overconfident).
4. Update periodically as the model evolves (Learning Engine calibration loop).

**Interview sentence:** "An overconfident pseudo-measurement is the critical-measurement trap at
scale — the filter trusts it blindly and can't self-correct. Honest calibration of $R_{pseudo}$
from the empirical forecast-error archive is the most important discipline in pseudo-measurement
design."

---

## 5. The Four Categories Summary (Quick Mental Map)

| Category | Sources | Key property |
|----------|---------|-------------|
| **Structural priors** | Topology, zero-injections, conductor params | Define $H$; hard constraints; free information from physics |
| **Temporal priors** | Load cyclicality, historical archive, ML forecasts | Enter as `Bu` or pseudo-measurements; the FASE backbone |
| **Heterogeneous measurements** | Head SCADA, inverter, AMI, EV charger, μPMU | The direct measurement $z$ set; each with its own $R$ and rate |
| **Learned priors** | Historical predictions + actuals + noise archive | Calibrate $Q$, $R$, $v$; the Learning Engine's input |

This four-category taxonomy is the answer to: "How do you handle distribution under-
observability?" — you source information across all four categories and fuse it through the
recursive filter with honest covariances.

---

## → Bridge to Juan's Work

<!-- greppable tag: Bridge to your work -->

| DSSE taxonomy concept | Juan's work |
|----------------------|------------|
| ML load/PV forecasts as calibrated pseudo-measurements | HEMS / Building Intelligence edge-ML forecasting — produces mean + variance estimates; the calibration discipline (empirical error archive) is already part of my workflow |
| SI-MAPPER topology prior | Ontology graph encodes the graph structure that defines $H$ and identifies zero-injection nodes |
| Multi-rate asynchronous fusion | OSED edge runtime handles multiple sensor streams at different rates — the same predict/update pattern |
| Historical archive → time-indexed $Q$, $R$ | The baseline-consumption analysis across billions of substation data points is the calibration of $R$ for the AMI channel at production scale |

**One-liner for the interview:** "Every information source the grid offers maps to one of four
estimator roles: measurement, process-model input, structural constraint, or learned prior. My
HEMS forecasting is already the temporal-prior role; SI-MAPPER is the structural prior; OSED
is the multi-rate fusion substrate."

---

## Quick-Recall Card (Recite Before the Interview)

1. **Four roles:** measurement ($z$, $R$); process model ($F$, $Bu$, $Q$); structural constraint ($R \to 0$); learned prior (calibrates $Q$, $R$, $v$).
2. **Topology:** defines $H$ → Kirchhoff coupling → head SCADA informs dark nodes.
3. **Zero-injection:** near-zero $R$ virtual measurement at known-passive nodes — free information.
4. **Cyclicality:** enters as `Bu` = $v\,\Delta t$ in the FASE predict step — the temporal prior.
5. **Historical archive:** conditions $Q$, $R$ on time-of-day/season/weather — the Learning Engine's input.
6. **AMI:** slow, dense, delayed; anchors drift; apply to the interval it describes, not "now"; feeds recalibration.
7. **Smart inverters (IEEE 1547/2030.5):** sensor + actuator; self-report $P$, $Q$, $V$; small $R$; the most valuable new DER telemetry source.
8. **EV chargers:** event-driven (OCPP/MQTT); temporal pattern enters $Bu$; absent between sessions.
9. **Multi-rate:** update on arrival with each source's own $R$; predict between arrivals — KF handles natively.
10. **ML forecasts:** pseudo-measurements; $R_{pseudo}$ from empirical error archive, NOT from model confidence; honest calibration = the hard part.
11. **Honest covariance discipline:** overconfident $R_{pseudo}$ → leverage trap at scale → filter goes deaf. Calibrate from the archive.
12. **Four-category summary:** structural priors + temporal priors + heterogeneous measurements + learned priors.

---

*Sources: Dehghanpour et al. (IEEE Trans. Smart Grid 2019) — DSSE pseudo-measurements, information
sources; Debs & Larson 1974 (FASE, augmented-load process model); IEEE 1547-2018 / IEEE 2030.5
(smart inverter self-reporting requirements); Open Charge Point Protocol (OCPP) 2.0 (EV charger
telemetry); AGMS patent (Director; Learning Engine calibration requests, ORACS Observability,
Inspector scout); GE Vernova JD R5043890 (virtual sensing, federated, distribution, phase angles,
smart inverters); KAL-03-fase-augmented-load-feeder-walk.md (worked example of this taxonomy
in action); 01-RESEARCH.md verified equations.*
