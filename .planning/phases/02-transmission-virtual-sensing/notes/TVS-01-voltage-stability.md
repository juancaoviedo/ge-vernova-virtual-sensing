# TVS-01: Voltage Stability Monitoring

**For:** Oral rehearsal — speak each section aloud before the interview.
**Purpose:** Close the transmission-side voltage-stability vocabulary gap so you can explain
P-V collapse, the Thevenin-equivalent voltage-stability index from PMU data, and the
operating-margin concept with specifics — without defaulting to distribution-side framing.

---

## <3-min say-aloud version

> "Every load bus sees the rest of the grid as a Thevenin source — a voltage $E_{Thev}$ behind
> an impedance $Z_{Thev}$. From local PMU voltage and current phasors you can estimate that
> Thevenin impedance in real time. Now picture the P-V curve: as you draw more power from the
> bus, its voltage sags, and the curve bends back at a nose — the maximum-loadability point.
> Maximum power transfer, that nose, happens exactly when the load impedance magnitude drops to
> equal the Thevenin impedance: $|Z_{load}| = |Z_{Thev}|$. So the ratio
> $\mathrm{VSI} = |Z_{Thev}|/|Z_{load}|$ is a voltage-stability index that runs from zero at light
> load to one at collapse, and the gap to one — $1 - \mathrm{VSI}$ — is your operating margin: how
> much more load the bus can absorb before voltage collapse. Beyond the nose there's no
> steady-state solution at all; mathematically the power-flow Jacobian goes singular. The one
> caveat is that this single-port Thevenin reduction is approximate in multi-load systems where
> loads vary together — but as a local, PMU-driven early-warning index it's the standard tool."

---

## 1. The P-V (Nose) Curve and the Collapse Mechanism (Mental Model First)

Voltage stability is not about frequency or rotor angles — it is about whether a bus can keep
its voltage up while the grid pulls power through it. The mental picture is a single load bus
fed through a transmission impedance.

Plot the bus voltage $V$ on the vertical axis against the load power $P$ drawn at that bus on
the horizontal axis. As load $P$ rises, the voltage $V$ sags — that is normal. But the curve
does not fall forever in a straight line: it **bends back on itself at a nose**, the point of
**maximum loadability**. That nose is the most power the bus can possibly absorb.

$$\text{Nose of the P-V curve} \;=\; \text{maximum-loadability point} \;=\; \text{voltage-collapse boundary}$$

**Beyond the nose there is no steady-state solution.** Try to draw more power than the nose
allows and the power-flow equations have no real answer — physically, the voltage runs away
downward and the bus collapses. This is **voltage collapse**, and it is a different failure
mode from a thermal overload or a frequency excursion.

The crisp mathematical signature: **the nose is the point where the power-flow Jacobian becomes
singular.** As you approach maximum loadability the Jacobian's determinant goes to zero, so the
sensitivity of voltage to power blows up — a tiny additional load produces an unbounded voltage
drop. That singularity is the formal definition of the loadability limit.

**One-liner for the interview:** "Voltage collapse is the nose of the P-V curve — the maximum
power a bus can absorb. Past it there's no steady-state solution, and that's exactly where the
power-flow Jacobian goes singular."

---

## 2. The Thevenin-Equivalent VSI from Local PMU Data (The Must-Know)

This is the section to own. It turns the abstract nose-curve idea into a number you can compute
in real time from one bus's PMU.

**Step 1 — Reduce the grid to a Thevenin equivalent.** From the perspective of a single load
bus, the entire rest of the network — every generator, line, and other load — collapses to a
**Thevenin equivalent**: an ideal source $E_{Thev}$ behind a series impedance $Z_{Thev}$. That is
just Thevenin's theorem applied to the grid seen from one port.

**Step 2 — Estimate $E_{Thev}$ and $Z_{Thev}$ from PMU phasors.** A PMU at the bus streams
time-synchronized voltage and current phasors $(\tilde V, \tilde I)$. Over a short window of
consecutive PMU snapshots you fit the two unknowns of the Thevenin equivalent by **least
squares** — each snapshot gives a $\tilde V = E_{Thev} - Z_{Thev}\,\tilde I$ relation, and a
window of them over-determines $E_{Thev}$ and $Z_{Thev}$. (Note the structural echo of WLS from
KAL-01: redundant noisy measurements, solve for the few parameters that best explain them.)

**Step 3 — The collapse criterion (maximum power transfer).** From circuit theory, the maximum
power deliverable to the load through $Z_{Thev}$ occurs when the load impedance magnitude equals
the Thevenin impedance magnitude:

$$|Z_{load}| = |Z_{Thev}| \quad\Longrightarrow\quad \text{at the nose / collapse point}$$

That is the impedance-matching condition — the same maximum-power-transfer result from
elementary circuits, here repurposed as the voltage-collapse boundary.

**Step 4 — Define the index.** Form the ratio of the two impedance magnitudes:

$$\mathrm{VSI} = \frac{|Z_{Thev}|}{|Z_{load}|}, \qquad \mathrm{VSI}\in[0,1]:\ 0=\text{no load},\ 1=\text{collapse}$$

At light load the load impedance is huge, so $\mathrm{VSI} \approx 0$ — comfortably stable. As load
grows, $|Z_{load}|$ shrinks toward $|Z_{Thev}|$ and $\mathrm{VSI}$ climbs toward $1$. When it hits
$1$ the impedances match and you are at the nose — collapse. The whole index is computable from
**local** PMU data, which is why it scales: every PMU-instrumented bus can watch its own
$\mathrm{VSI}$ without a full network model.

**Interview sentence:** "The Thevenin VSI is a max-power-transfer index — estimate the Thevenin
impedance the load bus sees from local PMU phasors, and when the load impedance magnitude drops
to match it, $\mathrm{VSI}$ hits one and you're at voltage collapse."

---

## 3. The Operating / Loadability Margin

The VSI is most useful not as a binary alarm but as a **continuous headroom number**.

The **operating margin** (loadability margin) is the distance from the current operating point
to the nose — how much *additional* power the bus can absorb before collapse. In the
impedance-matching index it reads directly off the gap to one:

$$\text{margin} \;\approx\; 1 - \mathrm{VSI}$$

A bus at $\mathrm{VSI} = 0.4$ has a comfortable $0.6$ of headroom; a bus at $\mathrm{VSI} = 0.95$ is
five percent from collapse and demands attention. Operators (and automated schemes) watch this
margin as a **real-time early-warning signal**: it is the "how close are we to the edge" number,
expressed equivalently as additional MW absorbable before the nose.

The key conceptual move — and the one that makes the bridge below land — is that you are
**estimating a hard physical limit, measuring your distance to it, and acting before you cross
it.** That is the whole job: not staying at a fixed setpoint, but tracking headroom to a moving
limit.

**Interview sentence:** "The margin is just $1 - \mathrm{VSI}$ — the live headroom to the
voltage-collapse limit. It turns the index into an actionable early-warning number, not just a
pass/fail flag."

---

## 4. Known Limitation (Awareness)

State this to show you know where the tool breaks, but do not derive it.

The single-port Thevenin reduction is **approximate for multi-load systems**. The clean
$|Z_{load}| = |Z_{Thev}|$ collapse criterion assumes the load bus can be isolated behind one
Thevenin equivalent. When **multiple loads vary together** — coordinated load growth across a
region — that single-port reduction no longer captures the true collapse surface, and pure
impedance-match indices can be optimistic or pessimistic. Production schemes handle this with
multi-port or wide-area variants; the local PMU index is the fast, scalable first line, not the
last word.

**Awareness sentence:** "The caveat is multi-load systems — a single-port Thevenin equivalent is
approximate when several loads ramp together, so the local impedance-match index is a fast
early-warning indicator, not a full multi-bus collapse model."

---

## → Bridge to your work

<!-- greppable tag: Bridge to your work -->

The strongest analog is **margin-to-constraint monitoring** — exactly what you built into HEMS.

> **"My HEMS PoC manages total household consumption to respect grid power limits — it tracks
> headroom to a hard limit and acts before breaching it. That is structurally identical to the
> voltage-stability operating margin: estimate the limit, watch the distance to it, act before
> you cross it."**

| Power-System Voltage Stability | OSED / HEMS Margin Monitoring |
|--------------------------------|-------------------------------|
| Hard limit = voltage-collapse nose (max loadability) | Hard limit = contracted grid power cap for the household |
| Limit estimated from local PMU phasors → $Z_{Thev}$ | Limit known from the grid-service contract / signal |
| Live headroom = $1 - \mathrm{VSI}$ (distance to nose) | Live headroom = cap − current total consumption |
| Action: shed load / inject reactive power before collapse | Action: curtail / shift controllable loads before breaching cap |
| Driver: real-time PMU stream | Driver: real-time BMS / metering stream at the edge |

The shape is the same in both domains: a physical or contractual limit, a continuously estimated
distance to it, and a control action triggered before the distance hits zero. The grid version
estimates the limit itself from phasors; the HEMS version is handed the limit but solves the
identical "stay below the edge with margin to spare" control problem.

**How to say this in the interview:**

> "The voltage-stability margin is the same headroom-to-a-physical-limit signal I built into my
> HEMS. In HEMS I manage total household consumption to respect a grid power limit — I track the
> distance to a hard cap and act before breaching it. The voltage-collapse margin is the same
> pattern at the transmission level: estimate the collapse limit from PMU data, watch
> $1 - \mathrm{VSI}$, and act before it reaches zero. I've already implemented margin-to-constraint
> control; here the only new piece is estimating the limit from phasors instead of being given
> it."

---

## Quick-Recall Card (Recite Before the Interview)

1. **P-V nose curve:** plot $V$ vs $P$; the curve bends back at the nose = maximum loadability. Past the nose there is **no steady-state solution** = voltage collapse.
2. **Collapse = Jacobian singular:** the nose is where the power-flow Jacobian becomes singular (voltage sensitivity to power blows up).
3. **Thevenin reduction:** each load bus sees the grid as $E_{Thev}$ behind $Z_{Thev}$; estimate both from a window of local PMU phasors $(\tilde V, \tilde I)$ by least squares.
4. **Collapse criterion:** $|Z_{load}| = |Z_{Thev}|$ — maximum power transfer / impedance matching.
5. **Index:** $\mathrm{VSI} = |Z_{Thev}|/|Z_{load}| \in [0,1]$ — $0$ at no load, $1$ at collapse.
6. **Operating margin:** $\approx 1 - \mathrm{VSI}$ — live headroom to the nose, the early-warning number.
7. **Limitation (awareness):** single-port Thevenin is approximate for multi-load systems where loads vary together.
8. **My bridge:** the voltage-stability margin IS HEMS margin-to-constraint monitoring — estimate the limit, watch the distance, act before you cross it.

---

*Sources: Vu/Begovic/Novosel VIP impedance-matching method; OSTI 1572408, ScienceDirect S2352467718300067, IET GTD Pourbagher 2022 (Thevenin VSI, $|Z_{load}|=|Z_{Thev}|$ collapse, VSI 0→1, Jacobian singularity, multi-load limitation); 02-RESEARCH.md §TVS-01 verified equations; CV — HEMS PoC (household consumption vs grid power limits).*
