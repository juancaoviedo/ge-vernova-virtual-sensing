# TVS-04: Asset-Health Estimation

**For:** Oral rehearsal — speak each section aloud before the interview.
**Purpose:** Cover transformer/asset-health virtual sensing — the IEEE C57.91 hot-spot thermal
ODE (deep), Arrhenius loss-of-life, and DGA / Dynamic Line Rating / RUL (awareness) — so you can
explain how an unmeasured internal condition is *inferred* from telemetry and turned into a
maintenance decision, and tie each to work you have already built.

---

> **Depth strategy:** FULL/worked depth for the **IEEE C57.91 hot-spot ODE** and the **Arrhenius
> aging law** (criteria-named). **Awareness only** — crisp, no derivation — for **DGA**, **Dynamic
> Line Rating** productization, and **RUL** framing. The C57.91 display constants are tagged
> *"per IEEE C57.91-2011"*: the two-cascaded-first-order-rise **structure** is verified; precise
> exponent/constant placement differs between Clause 7 (exponential) and Annex G (detailed) models,
> so the structure is stated confidently and the constants are attributed to the standard.

## 1. IEEE C57.91 Transformer Thermal Model — The Physics (Deep)

**Mental model first.** You almost never measure the winding **hot-spot** temperature directly —
it is buried inside the windings under oil. But hot-spot temperature is what ages the insulation,
so it is the quantity that matters. C57.91 gives you a two-stage thermal model that **infers** it
from load current and ambient temperature: ambient → **top-oil** rise → **hot-spot** rise. Two
cascaded first-order ODEs, slow oil then fast winding.

**Top-oil temperature rise over ambient** (load-driven, slow):

$$\tau_{TO}\,\frac{d\,\Delta\theta_{TO}}{dt} = \Delta\theta_{TO,\,U}\left(\frac{K^2 R + 1}{R+1}\right)^{n} - \Delta\theta_{TO}$$

**Hot-spot (winding) temperature rise over top-oil** (load-driven, fast):

$$\tau_{w}\,\frac{d\,\Delta\theta_{HS}}{dt} = \Delta\theta_{HS,\,U}\,K^{2m} - \Delta\theta_{HS}$$

**Hot-spot temperature** (the inferred state you act on):

$$\theta_{HS} = \theta_{ambient} + \Delta\theta_{TO} + \Delta\theta_{HS}$$

### Term-by-term (à la KAL-03)

| Term | Name | Expression / role | Physical meaning |
|------|------|-------------------|------------------|
| $\theta_{HS}$ | Hot-spot temperature | $\theta_{ambient}+\Delta\theta_{TO}+\Delta\theta_{HS}$ | The **hidden state** — not directly measured; drives aging |
| $\Delta\theta_{TO}$ | Top-oil rise over ambient | first ODE | Bulk-oil heating; slow dynamics |
| $\Delta\theta_{HS}$ | Hot-spot rise over top-oil | second ODE | Winding gradient above the oil; fast dynamics |
| $K = I/I_{rated}$ | Per-unit load | input | The controllable driver — load current relative to rating |
| $R$ | Loss ratio | load-loss / no-load-loss | Shapes how load maps to top-oil rise |
| $\Delta\theta_{TO,U}$ | Ultimate top-oil rise | rated-load steady value | Asymptote of the top-oil rise |
| $\Delta\theta_{HS,U}$ | Ultimate hot-spot rise | rated-load steady value | Asymptote of the hot-spot gradient |

### Parameters (per IEEE C57.91-2011)

| Parameter | Symbol | Typical role | Units |
|-----------|--------|--------------|-------|
| Top-oil time constant | $\tau_{TO}$ | **hours-scale** ($\gg \tau_w$) | h |
| Winding time constant | $\tau_{w}$ | **minutes-scale** | min |
| Oil exponent | $n$ | cooling-mode dependent (e.g. ONAN/ONAF) | — |
| Winding exponent | $m$ | cooling-mode dependent | — |
| Loss ratio | $R$ | nameplate-derived | — |

**The key structural fact to say aloud:** $\tau_{TO} \gg \tau_w$ — the oil is a slow thermal mass
(hours), the winding gradient responds in minutes. A load step heats the windings quickly but the
oil bath lags. *Tag exact constants "per IEEE C57.91-2011"; the structure (two cascaded
first-order rises, load-driven, exponents $m,n$, $\tau_{TO}\gg\tau_w$) is the part you assert with
confidence.*

---

## 2. Aging / Loss-of-Life — Arrhenius (Deep)

**Mental model first.** Insulation does not fail at a load threshold — it fails from *cumulative
thermal aging*, and aging rate rises **exponentially** with hot-spot temperature. This is why
hot-spot estimation matters: a few extra degrees roughly doubles the aging rate.

Per-unit insulation life consumed follows an **Arrhenius** relation in absolute temperature:

$$\text{per-unit life} = A\,\exp\!\left(\frac{B}{\theta_{HS}+273}\right), \qquad A = 9.8\times10^{-18},\ \ B = 15000$$

(constants per IEEE C57.91-2011; $\theta_{HS}+273$ converts °C to kelvin).

**Equal-life loading:** the **hot-spot temperature — not the load directly — determines insulation
aging.** You can run above nameplate load on a cold day with *less* aging than nameplate load on a
hot day, because what ages the paper is $\theta_{HS}$, which depends on both load and ambient.

**Interview sentence:** "Aging is Arrhenius in the hot-spot temperature, $A\exp(B/(\theta_{HS}+273))$
with $A=9.8\times10^{-18}$, $B=15000$ — so a transformer's loss-of-life is governed by the
inferred hot-spot, which is exactly why you estimate it instead of just watching load."

---

## 3. Why This Is Virtual Sensing (Deep Framing)

The winding hot-spot is **not directly measurable** — it is inside the windings, under oil. So you
**infer** it from things you *can* measure (load current, ambient temperature) by integrating the
C57.91 ODE. That is the definition of virtual sensing: a physics model + available telemetry →
an estimate of the quantity that actually matters.

**This is identical in spirit to the IEEE 738 conductor-temperature EKF I already built in
Phase 1 (KAL-03 / KAL-04).** There, conductor temperature is the hidden state, inferred from
current + weather via the IEEE 738 thermal ODE in an EKF (`ekf_line_temp_demo.py`). C57.91 is the
**transformer analog of IEEE 738**: same pattern — unmeasured internal temperature, physics ODE,
inference from proxy telemetry. State this parallel explicitly: *"Transformer hot-spot estimation
via C57.91 is the same virtual-sensing pattern as the conductor-temperature EKF I built on IEEE
738 — different asset, identical structure."*

---

## 4. DGA — Dissolved Gas Analysis (Awareness)

Under thermal/electrical stress, transformer oil decomposes and releases **key gases**; the gas
*pattern* fingerprints the internal fault. **No derivation — recognize the associations:**

| Gas | Association |
|-----|-------------|
| H₂ | Partial discharge |
| CH₄ / C₂H₆ | Low-temperature thermal fault |
| C₂H₄ (ethylene) | High-temperature thermal / overheating |
| C₂H₂ (acetylene) | **Arcing — most severe** |
| CO / CO₂ | Cellulose / paper (insulation) degradation |

**Interpretation methods (name only):** Duval Triangle, Rogers Ratios, Key Gas method, IEC 60599.

**One line:** *"DGA is a virtual sensor for internal fault type — you infer what's failing inside a
sealed tank from the gas signature in the oil."*

---

## 5. Dynamic Line Rating (Awareness — Product Framing)

DLR computes a conductor's **real-time ampacity** from actual weather + the IEEE 738 thermal
balance, instead of a fixed conservative **static** rating. **I already built this** in the Phase 1
demo (`ieee738_ampacity` in `ekf_line_temp_demo.py`) — so I frame it as a virtual-sensing
**product**, not a derivation:

> Infer the unmeasured conductor temperature → unlock **10–30% more line capacity headroom** that a
> static rating leaves on the table.

Reference Phase 1 rather than re-deriving IEEE 738. The pitch: DLR turns a virtual temperature
estimate into deferred transmission capex.

---

## 6. Remaining Useful Life — RUL (Awareness — Framing Only)

RUL projects **cumulative damage forward** to a time-to-end-of-life. For a transformer, integrate
the Arrhenius loss-of-life over the operating history and extrapolate; for a conductor, annealing /
insulation wear. RUL is the **output that turns a virtual condition estimate into a
maintenance/replacement decision** — when to inspect, derate, or replace. Keep it conceptual: no
model here, just the decision framing.

---

## <3-min say-aloud version

> "Asset health is virtual sensing on infrastructure. Take a transformer: the thing that ages it is
> the **winding hot-spot temperature**, which you can't measure — it's buried under oil. So
> **IEEE C57.91** gives you two cascaded first-order ODEs — ambient to **top-oil** (slow, hours),
> top-oil to **hot-spot** (fast, minutes), both driven by per-unit load $K = I/I_{rated}$ — and you
> integrate them to *infer* $\theta_{HS}$. Why care? **Aging is Arrhenius in that hot-spot**,
> $A\exp(B/(\theta_{HS}+273))$, so a few degrees roughly doubles the aging rate — load alone doesn't
> tell you, hot-spot does. That's the **same pattern as the IEEE 738 conductor-temperature EKF I
> built** — unmeasured internal temperature, physics ODE, infer from proxy telemetry. The same
> conductor model also gives **Dynamic Line Rating**: real-time ampacity from weather, 10–30% more
> headroom than a static rating. **DGA** is the chemical version — gas signatures in the oil
> fingerprint the fault, acetylene meaning arcing. And **RUL** projects the cumulative damage
> forward into a replace-or-derate decision. All of it is: infer the quantity that matters from the
> telemetry you have, then act on it."

---

## → Bridge to your work

> **"Transformer hot-spot and DLR are the same virtual-sensing pattern as my OSED building thermal
> estimator — you can't measure the quantity that matters directly, so you infer it from a physics
> model plus available telemetry and act on the estimate."**

| Grid asset-health virtual sensing | My OSED / Building Intelligence work (CV) |
|-----------------------------------|--------------------------------------------|
| Hidden state: winding hot-spot / conductor temp | Hidden state: zone thermal state |
| Physics model: C57.91 / IEEE 738 thermal ODE | Physics model: RC thermal model |
| Telemetry: load current, ambient, weather | Telemetry: BMS sensors |
| Act on estimate: derate, DLR headroom, RUL decision | Act on estimate: predictive HVAC control |

You **can't** put a sensor where the quantity actually lives (inside windings, inside the
building's thermal mass), so you infer it from a physics model plus the telemetry you do have —
identical structure, different asset.

**How to say this in the interview:**

> "This is the same thing I built in OSED's building thermal estimator. I couldn't directly measure
> the full zone thermal state, so I inferred it from an RC physics model plus BMS sensor telemetry
> and ran predictive control on the estimate. Transformer hot-spot via C57.91 and Dynamic Line
> Rating via IEEE 738 are the grid version of exactly that pattern — and I already demoed the IEEE
> 738 conductor case as an EKF in Phase 1. So asset-health virtual sensing maps directly onto work
> I've shipped."

---

## Quick-Recall Card (Recite Before the Interview)

1. **C57.91 thermal model:** two cascaded first-order rises — top-oil over ambient (slow, $\tau_{TO}$ hours), hot-spot over top-oil (fast, $\tau_w$ minutes), both driven by $K = I/I_{rated}$; $\theta_{HS} = \theta_{ambient} + \Delta\theta_{TO} + \Delta\theta_{HS}$. $\tau_{TO} \gg \tau_w$.
2. **Drivers:** top-oil $\propto \left(\frac{K^2R+1}{R+1}\right)^{n}$, hot-spot $\propto K^{2m}$; exponents $m$ (winding), $n$ (oil), per IEEE C57.91-2011.
3. **Arrhenius aging:** per-unit life $= A\exp(B/(\theta_{HS}+273))$, $A=9.8\times10^{-18}$, $B=15000$. Equal-life loading — hot-spot, not load, ages insulation.
4. **Virtual sensing:** hot-spot is unmeasurable → infer from load + ambient via C57.91 ODE — same as the IEEE 738 conductor EKF I built (KAL-03/04).
5. **DGA (awareness):** H₂=PD, CH₄/C₂H₆=low-temp thermal, C₂H₄=overheating, C₂H₂=arcing (worst), CO/CO₂=paper; Duval/Rogers/Key Gas/IEC 60599.
6. **DLR (awareness):** real-time ampacity from weather + IEEE 738 → 10–30% more headroom vs static; I built `ieee738_ampacity` in Phase 1.
7. **RUL (awareness):** project cumulative damage (Arrhenius integral) forward → maintenance/replace decision.
8. **My bridge:** hot-spot / DLR = OSED building thermal estimator — infer the unmeasurable from a physics model + telemetry, act on the estimate.

---

*Sources: IEEE Std C57.91-2011 (transformer loading guide — top-oil/hot-spot thermal model, Arrhenius aging; major revision in progress, ed. expected 2025–2026); IEEE 738 / Phase 1 KAL-03–KAL-04 (`ekf_line_temp_demo.py`, conductor EKF + DLR); CV (OSED building thermal estimator, Building Intelligence & Predictive Control).*
