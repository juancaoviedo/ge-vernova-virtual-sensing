# TVS-03: Observability & Bad-Data Detection

**For:** Oral rehearsal — speak each section aloud before the interview.
**Purpose:** Own the observability and bad-data vocabulary — Jacobian-rank observability, the
chi-squared detection test, normalized-residual identification, and the leverage-measurement
blind spot — so you can answer "how do you know your state estimate is trustworthy?" with the
exact production machinery, not generalities.

---

> **This note specializes KAL-01 §4 to the linear DC case.** KAL-01 already owns the WLS
> objective, the chi-squared test, the largest-normalized-residual (LNR) test, and the leverage
> trap for the nonlinear AC estimator. Here the measurement model is **linear** ($z = H\theta + e$,
> from TVS-02's DC power flow), so the Jacobian $H$ is *constant* — no relinearization. Everything
> below is the same residual machinery, just with a fixed $H$. **Do not re-derive WLS** — it is
> the one-shot solve $\hat\theta = (H^\top W H)^{-1}H^\top W z$ from TVS-02.

## 1. Observability via the Measurement Jacobian Rank

**Mental model first.** Observability asks one question: *is the measurement set rich enough to
pin down every state uniquely?* If two different state vectors could produce the same
measurements, you cannot tell them apart — the grid is unobservable.

The system is **numerically observable** iff the gain (information) matrix

$$G = H^\top W H$$

is nonsingular — equivalently, iff $H$ has **full column rank**:

$$\operatorname{rank}(H) = n \qquad (n = \text{number of states})$$

If $\operatorname{rank}(H) < n$, the gain matrix is singular, the normal equations have no unique
solution, and you have **unobservable states or islands** — buses (or whole regions) that no
combination of measurements can determine. The control center flags these and falls back to
pseudo-measurements (historical/forecast injections) or skips the region.

**The practical check is one line:**

```python
observable = numpy.linalg.matrix_rank(H) == n   # full column rank?
```

**Topological vs. numerical observability.** *Topological* observability is a graph argument —
does a spanning tree of measured branches reach every bus? *Numerical* observability is the
actual rank of $H$ at the operating point (it can fail even when the graph looks fine, e.g. when
measurements are linearly dependent). Name both; **the rank test is the operational one** you run.

**Interview sentence:** "Observability is whether the Jacobian $H$ has full column rank — whether
the measurements are independent enough to uniquely pin down every angle. In the linear DC case I
literally check `numpy.linalg.matrix_rank(H) == n`."

---

## 2. Chi-Squared Detection — "Is There Bad Data?"

**Mental model first.** Because there is **redundancy** ($m$ measurements, $n$ states, $m > n$),
the residuals carry information. If every sensor is clean, the weighted residual cost is small and
statistically predictable. If one is grossly wrong, the cost spikes. The chi-squared test turns
that into a hypothesis test.

After the WLS solve, the weighted residual cost

$$J(\hat\theta) = r^\top W r, \qquad r = z - H\hat\theta$$

follows a **chi-squared distribution** with $m - n$ degrees of freedom ($m$ measurements minus
$n$ states = degrees of redundancy).

**Detection rule:** if

$$J(\hat\theta) > \chi^2_{(m-n,\,1-\alpha)} \qquad (\text{e.g. } \alpha = 0.05,\ 95\%\ \text{confidence})$$

then **at least one measurement is bad**.

The critical caveat: **chi-squared tells you THAT bad data exists — not WHICH measurement is the
culprit.** It is a detector, not an identifier. That is the next section's job.

In code the threshold is `scipy.stats.chi2.ppf(0.95, df=m-n)` — auditable, no hard-coded table.

---

## 3. Largest-Normalized-Residual ($r^N$) Identification — "Which One?"

**Mental model first.** Raw residuals are not directly comparable: a measurement that the
estimator leans on heavily will *always* have a small residual, so you must **normalize by each
measurement's expected residual spread** before ranking. That spread is the residual covariance.

**Residual covariance:**

$$\Omega = R - H\,(H^\top W H)^{-1} H^\top = R - H\,G^{-1}H^\top$$

(Equivalently the residual-sensitivity matrix $S = I - H G^{-1} H^\top W$ maps measurement errors
to residuals via $r = S\,e$.)

**Normalized residual** for each measurement $i$:

$$r_i^N = \frac{|r_i|}{\sqrt{\Omega_{ii}}}$$

**Identification rule:** the measurement with the **largest $r_i^N$ above a threshold ≈ 3** (3σ) is
the prime suspect. Remove it, **re-run WLS**, and re-test with chi-squared. Repeat until the
chi-squared test passes (no bad data remains).

**Encode the division of labor explicitly (the classic pitfall):**

| Test | Question it answers |
|------|---------------------|
| Chi-squared on $J(\hat\theta)$ | **"Is there bad data?"** (detection) |
| Largest normalized residual $r_i^N$ | **"Which measurement?"** (identification) |

Conflating these is the standard mistake — chi-squared **never** names the culprit; the
normalized-residual test does.

**Interview sentence:** "Chi-squared detects that something is wrong; the largest-normalized-residual
test, with $\Omega = R - HG^{-1}H^\top$ and threshold around three sigma, identifies which one,
then you drop it and re-solve."

---

## 4. The Critical Limitation — Leverage Measurements (Awareness, but Interview Gold)

This is the trap interviewers who have *built* state estimators will probe.

**Leverage measurements** sit at buses whose observability depends **entirely** on them — remove
the measurement and the bus goes unobservable. Because the estimator has no independent reading to
contradict it, it fits that measurement essentially perfectly: its residual is **structurally
near-zero**. So a **gross error in a leverage measurement is invisible to the $r^N$ test** — you
get a *wrong-but-consistent* estimate that passes every check.

A second failure mode: **multiple interacting + conforming bad data**. When two corrupted
measurements agree with each other, their errors mask one another and the single-largest-$r^N$
test can be fooled.

The fix is structural, not algorithmic: **redundant measurement placement at critical buses** so
no single reading has unchecked leverage.

**Interview sentence (lifted from KAL-01, reworded):** "The normalized-residual test has a
structural blind spot — leverage measurements at sparsely instrumented buses have near-zero
residuals even when corrupted, because the estimator has no independent measurement to contradict
them. That is the key limitation of chi-squared bad-data detection, and it is why critical buses
need redundant measurement placement."

---

## <3-min say-aloud version

> "Bad-data handling has three layers. First, **observability**: can the measurements even pin
> down the state? That's whether the Jacobian $H$ has full column rank — in the linear DC case I
> just check `matrix_rank(H) == n`; if it's short, I have unobservable islands. Second,
> **detection**: after the weighted-least-squares solve, the weighted residual cost $J = r^\top W r$
> is chi-squared with $m$ minus $n$ degrees of freedom. If it exceeds the 95% threshold, there's
> bad data — but chi-squared only tells me *that* something's wrong, not *which*. Third,
> **identification**: I normalize each residual by its own covariance, $r_i^N = |r_i|/\sqrt{\Omega_{ii}}$
> with $\Omega = R - HG^{-1}H^\top$, and the biggest one above about three sigma is the culprit —
> drop it, re-solve, re-test. The catch I always flag is **leverage measurements**: at a bus that
> depends entirely on one reading, the residual is near-zero even when that reading is corrupt, so
> the test is blind to it — which is exactly why you place redundant measurements at critical buses."

---

## → Bridge to your work

> **"Bad-data detection at substation scale is literally what I did analyzing baseline-estimation
> errors across billions of data points from multiple substations — finding the corrupted or
> anomalous measurements that throw off the estimate is the chi-squared / normalized-residual
> problem in production."**

| Power-System Bad-Data Detection | My substation-scale error analysis (CV) |
|---------------------------------|------------------------------------------|
| Detect: $J(\hat\theta) > \chi^2_{(m-n,0.95)}$ | Detect: aggregate error metrics flag a substation/feeder out of statistical bounds |
| Identify: largest $r_i^N$ above 3σ | Identify: pinpoint the corrupted/anomalous points driving the baseline error |
| Re-solve after removing the bad reading | Re-estimate the baseline with the bad points excluded |
| Leverage blind spot → place redundant sensors | Coverage gaps → some sites have too little redundancy to validate |

This is the **strongest bridge in the phase**: the CV line "*Analyzed errors in baseline
consumption estimation by processing billions of data points across multiple substations*" **is**
bad-data detection — the same detect-then-identify-then-re-estimate loop, at production scale on
real grid telemetry.

**How to say this in the interview:**

> "I have run exactly this loop in production, just at a much larger scale: I analyzed baseline
> consumption-estimation errors across billions of data points from multiple substations. The work
> was finding the corrupted and anomalous measurements that were throwing off the baseline — which
> is precisely the chi-squared-detect, normalized-residual-identify, re-estimate pipeline of grid
> bad-data detection. So observability and bad-data handling aren't new vocabulary for me; they're
> the formal name for data-quality work I've already shipped at substation scale."

---

## Quick-Recall Card (Recite Before the Interview)

1. **Observability:** $H$ full column rank ⟺ $G = H^\top W H$ nonsingular ⟺ `matrix_rank(H) == n`; else unobservable islands. Topological (graph) vs numerical (rank) — rank is operational.
2. **DC specialization:** $H$ is *constant* (linear DC), so the WLS solve is one-shot — no relinearization (this is KAL-01 §4 in the linear case).
3. **Chi-squared detection:** $J(\hat\theta) = r^\top W r \sim \chi^2(m-n)$; if $J > \chi^2_{(m-n,0.95)}$, bad data exists. Answers **"is there bad data?"**, not which.
4. **Normalized residual:** $r_i^N = |r_i|/\sqrt{\Omega_{ii}}$, $\Omega = R - HG^{-1}H^\top$; largest above ≈3σ is the suspect → remove, re-solve, re-test. Answers **"which one?"**
5. **Division of labor:** χ² detects; $r^N$ identifies. Never conflate them.
6. **Leverage-measurement trap:** near-zero residual even when corrupt → invisible to $r^N$; interacting+conforming bad data also defeats single-$r^N$ → place redundant measurements at critical buses.
7. **My bridge:** analyzing baseline-estimation errors across billions of points from multiple substations IS bad-data detection at scale — the strongest bridge in the phase.

---

*Sources: Abur & Expósito, "Power System State Estimation" Ch. 5 (Network Observability) & Ch. 6 (Bad Data Detection); KAL-01 §4 (chi-squared / LNR / leverage trap); CV (substation-scale baseline-error analysis).*
