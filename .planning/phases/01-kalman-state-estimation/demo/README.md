# KAL-04: IEEE 738 EKF Line-Temperature Demo

A self-contained Extended Kalman Filter (EKF) that estimates overhead conductor
temperature from simulated current telemetry, demonstrating the core idea behind
**Dynamic Line Rating (DLR)** virtual sensing.

---

## What It Demonstrates

The script builds a **from-scratch EKF** (numpy/scipy only — no external KF library) that:

1. Simulates a Drake ACSR conductor heating up as current ramps from 400 A to 600 A over
   one hour, using the **IEEE 738 thermal ODE** as the physics engine.
2. Generates noisy apparent-resistance measurements (`z = R25*(1 + alpha_R*(Tc-25))`) that
   mimic what you can infer from a current + voltage-drop measurement pair on a line section.
3. Runs the EKF predict-update loop — the **IEEE 738 ODE is the predict step**; the
   resistance measurement model is the update step — to recover conductor temperature from
   the noisy signal.
4. Computes a **Dynamic Line Rating ampacity** at the estimated temperature, showing how
   many additional amperes of capacity (or how much overload) exists relative to the
   75°C thermal limit.
5. Monitors filter health via a **Normalized Innovation Squared (NIS) / chi-squared gate**
   to detect divergence automatically.

The output is a three-subplot PNG (`ekf_line_temp.png`) showing:

- **Panel 1:** True Tc vs EKF estimate with ±2σ uncertainty band and the 75°C limit line
- **Panel 2:** Innovation sequence `y_k = z_meas - z_pred` (should be zero-mean for a healthy filter)
- **Panel 3:** Posterior uncertainty σ over time (shows rapid convergence from ±10°C to <0.2°C)

---

## Prerequisites

Only standard scientific Python packages required — all already installed:

```
numpy   (1.26.4+)
scipy   (1.11.4+)
matplotlib (3.6.3+)
```

No external Kalman filter library is needed.  The EKF is implemented from scratch
in ~50 lines of numpy arithmetic to demonstrate understanding of the underlying
predict-update mechanics.

---

## How to Run

```bash
cd .planning/phases/01-kalman-state-estimation/demo
python3 ekf_line_temp_demo.py
```

**Expected console output:**
```
==============================================================
  IEEE 738 EKF — Conductor Temperature & Dynamic Line Rating
==============================================================
  Simulation duration       : 60 min
  Current range             : 400 – 600 A

  Final true Tc             : 85.44 °C
  EKF estimate              : 85.43 °C  (±0.29 °C, 2σ)
  EKF estimation error      : 0.007 °C

  DLR ampacity (Tc≤75°C)   : 470 A  [Dynamic Line Rating]
  Applied current at t=1h   : 600 A
  ** WARNING: current exceeds DLR ampacity by 130 A **

  NIS divergence alerts     : 11 / 3600 steps (0.3%)  [~5% expected at 95th pct]
==============================================================

Saved .../demo/ekf_line_temp.png
```

**Expected output file:** `ekf_line_temp.png` (three-subplot figure, saved in this directory)

---

## Interview Talking Points

**Talking point 1 — "From scratch" signals depth, not just library knowledge:**

> "I implemented this EKF from scratch in numpy rather than calling a library.  That forced
> me to derive the process Jacobian `A = df/dTc` analytically for the IEEE 738 ODE and to
> understand what `P`, `Q`, and `R` physically represent — not just what arguments to pass.
> If an interviewer asks 'why is Q non-zero?', the answer from this code is: because the
> wind speed I'm feeding the thermal model is measured at the substation anemometer, not at
> every tower — so there is genuine uncertainty in the model's convective cooling term, and
> Q quantifies it."

**Talking point 2 — The building thermal ODE and the IEEE 738 ODE are structurally identical:**

> "The thermal model I already use for OSED's building state estimation is
> `C·dT/dt = Q_HVAC - UA·(T-Ta)` — a first-order thermal ODE driven by a heat source and
> damped by an ambient-dependent loss.  The IEEE 738 conductor model is
> `mCp·dTc/dt = I²R(Tc) - qc - qr + qs` — exactly the same structure.  Swapping building
> RC parameters for Drake ACSR parameters is a parameter substitution, not a conceptual
> leap.  The same EKF predict-update logic, the same Q/R tuning intuition, and the same
> innovation-sequence diagnostics apply in both domains.  That's the bridge I can walk into
> this role already knowing."

**Talking point 3 — The innovation subplot is the filter's health monitor:**

> "The middle panel of the output plot shows the innovation sequence — `y_k = z_measured -
> z_predicted` at each step.  Under a well-tuned filter this should be zero-mean, white
> noise.  If it drifts from zero it tells you one of two things: either the model has
> drifted (e.g., conductor aging has changed R25, or a topology change invalidated the
> thermal model for this span), or a sensor has failed.  The NIS chi-squared gate I added
> flags individual steps where the innovation is statistically inconsistent with the
> predicted covariance S — in this 3,600-step run, only 11 steps trigger (0.3%, well below
> the expected 5% false-alarm rate), so the filter is healthy.  In a production DLR system
> you would wire that flag to an alert or a Q-inflation step to prevent divergence."

---

## Key Implementation Details

| Component | Implementation choice | Reason |
|-----------|----------------------|--------|
| `ieee738_rhs` | Euler ODE step in `ekf_step` | Simple and stable for this mildly nonlinear system; sufficient for 1-second dt |
| Process Jacobian `A` | Analytic derivation of `df/dTc` | More stable than finite-difference; derivable from the ODE analytically |
| Covariance update | Standard form `P_post = (1-KH)*P_pred` | Scalar state; numerically fine; Joseph form needed for multi-state EKF |
| Divergence gate | `scipy.stats.chi2.ppf(0.95, df=1)` | Correct 95th-percentile threshold for scalar measurement; not hard-coded |
| DLR ampacity | Analytic heat-balance inversion | Demonstrates the link from estimated Tc to an actionable grid dispatch value |

---

## Files

```
demo/
├── ekf_line_temp_demo.py   — self-contained EKF script (run this)
├── ekf_line_temp.png       — three-subplot output figure (generated)
└── README.md               — this file
```
