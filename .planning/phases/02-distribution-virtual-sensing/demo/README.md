# TVS-02/03: 3-Bus DC Power-Flow Bad-Data Detection Demo

A self-contained weighted-least-squares (WLS) state estimator for a 3-bus DC
power-flow network that infers bus voltage angles from a redundant measurement
set, then **detects and removes a single corrupted measurement** using the
chi-squared test and the largest normalized residual — the textbook TVS-02 +
TVS-03 illustration, built from scratch in NumPy.

---

## What It Demonstrates

The script builds a **from-scratch DC state estimator** (numpy/scipy only — no
power-flow or state-estimation library) that:

1. Builds a **3-bus DC network** (lines 1-2, 1-3, 2-3; susceptances `b = 10` p.u.;
   slack = bus 1, `theta_1 = 0`) and solves the reduced power flow `B_red @ theta = P`
   for the ground-truth angles (`P = Bθ`, the susceptance Laplacian).
2. Estimates the two voltage angles via **one-shot linear WLS** from `m = 5`
   redundant measurements `[inj@2, inj@3, flow 1->2, flow 1->3, flow 2->3]` —
   the DC collapse of Phase 1's KAL-01 Gauss-Newton machinery (`h(θ) = Hθ` is
   linear, so the iteration is a single normal-equations solve).
3. Injects **one gross error** (+15σ) on the line-flow 2→3 measurement.
4. Runs the **chi-squared test** on the weighted residual cost `J = rᵀWr` to answer
   *"is there bad data?"* — `J = 176.7` far exceeds the `χ²(0.95, df=3) = 7.815`
   threshold, so bad data is flagged.
5. Computes the **largest normalized residual** `rN = |r| / sqrt(Ω_ii)` (with
   `Ω = R − H G⁻¹ Hᵀ`) to answer *"which one?"* — measurement #5 has `rN = 13.2`,
   identifying the corrupted measurement.
6. **Removes** the flagged measurement and **re-solves** (`df → 2`): `J = 1.8`
   now sits below threshold and the angles return to within `7e-4` rad of truth.

The output is a two-panel PNG (`dc_powerflow_baddata.png`):

- **Panel 1:** bar chart of normalized residuals with the 3σ identification line
  and the flagged measurement highlighted in red.
- **Panel 2:** true vs estimated angles, before and after bad-data removal.

---

## Prerequisites

Only standard scientific Python packages required — all already installed:

```
numpy      (1.26.4+)
scipy      (1.11.4+)
matplotlib (3.6.3+)
```

No power-flow library (no `pandapower` / `PYPOWER`) is needed. The point is to
**show the WLS math** — the estimator is ~80 lines of numpy linear algebra.

---

## How to Run

```bash
cd .planning/phases/02-distribution-virtual-sensing/demo
python3 dc_powerflow_baddata_demo.py
```

**Expected console output:**
```
==============================================================
  3-Bus DC State Estimation — Bad-Data Detection (chi2 + rN)
==============================================================
  States (angles)           : theta_2, theta_3  (n = 2)
  Measurements              : 5  -> redundancy df = 3
  Corrupted measurement     : #5 (flow 2->3), +15 sigma

  --- Solve #1 (with bad data) ---
  chi2 threshold (95%, df=3) : 7.815
  J(theta_hat)              : 176.711   -> BAD DATA DETECTED
  Flagged measurement       : #5 (flow 2->3), rN = 13.23  (others < 7.11)
  Estimated angles          : [-0.0824, -0.0685] rad

  --- Solve #2 (suspect removed) ---
  chi2 threshold (95%, df=2) : 5.991
  J(theta_hat)              : 1.797   -> CLEAN (below threshold)
  Re-solved angles          : [-0.0836, -0.0673] rad
  True angles               : [-0.0833, -0.0667] rad
  Angle error (before/after): 0.0020 -> 0.0007 rad
==============================================================

Saved .../demo/dc_powerflow_baddata.png
```

**Expected output file:** `dc_powerflow_baddata.png` (two-panel figure, saved in this directory)

---

## Interview Talking Points

**Talking point 1 — the one-line "I built this" story:**

> "I built a 3-bus DC state estimator that detects and removes a corrupted
> measurement via chi-squared + largest-normalized-residual — the textbook
> TVS-02 + TVS-03 illustration, built from scratch in NumPy. It's the linear
> special case of the same WLS/Gauss-Newton estimator from my Kalman demo:
> because the DC measurement model `h(θ) = Hθ` is linear, the iteration
> collapses to a single normal-equations solve."

**Talking point 2 — detection vs. identification is a real division of labor:**

> "These are two distinct questions and two distinct tools. The chi-squared test
> on the weighted residual cost `J = rᵀWr` answers *'is there bad data anywhere?'*
> — here `J = 176.7` blows past the `χ²(0.95, df=3) = 7.8` threshold. But χ² does
> **not** tell you which measurement is wrong. For that you need the **normalized
> residuals** `rN = |r| / sqrt(Ω_ii)`, where `Ω = R − H G⁻¹ Hᵀ` is the residual
> covariance. The largest `rN` (13.2 on measurement 5) names the culprit. Remove
> it, re-solve, and `J` drops to 1.8 — below the new threshold — with the angles
> back within `7e-4` rad of truth."

**Talking point 3 — redundancy is what makes the test work:**

> "The detection power comes entirely from redundancy: `m = 5` measurements for
> `n = 2` states gives `df = 3` degrees of freedom. With too little redundancy
> the χ² test is weak and removing a bad point barely moves `J`. That's why a
> real SE system over-instruments — and it's exactly where PMU phasors help: more
> direct, high-rate measurements raise the redundancy and sharpen bad-data
> detection. The math here is identical whether the measurements come from SCADA
> RTUs at 4-second scans or from PMUs at 30-120 Hz."

---

## Key Implementation Details

| Component | Implementation choice | Reason |
|-----------|----------------------|--------|
| WLS solve | One-shot `np.linalg.solve(G, HᵀWz)` | DC model `h(θ)=Hθ` is linear — Gauss-Newton collapses to a single solve (no iteration) |
| Detection gate | `scipy.stats.chi2.ppf(0.95, m-n)` | Correct 95th-percentile threshold on `J ~ χ²(m-n)`; not hard-coded |
| Identification | Normalized residual `Ω = R − H G⁻¹ Hᵀ` | Residual-covariance form (Abur & Expósito); `argmax(rN)` names the bad point |
| Observability | `np.linalg.matrix_rank(H) == n` assert | Full column rank guarantees the state is observable from the measurements |
| Library policy | from-scratch NumPy/SciPy, no power-flow lib | The point is to **show** the WLS + bad-data math, not call a black box |

---

## Files

```
demo/
├── dc_powerflow_baddata_demo.py   — self-contained DC WLS + bad-data script (run this)
├── dc_powerflow_baddata.png       — two-panel output figure (generated)
└── README.md                      — this file
```
