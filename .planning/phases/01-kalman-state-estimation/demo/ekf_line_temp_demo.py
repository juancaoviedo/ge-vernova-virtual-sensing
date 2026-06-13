"""
ekf_line_temp_demo.py
---------------------
From-scratch Extended Kalman Filter (EKF) estimating conductor temperature
from simulated current + weather telemetry using the IEEE 738 thermal ODE.

This is the KAL-04 hands-on demo for interview preparation.

Dependencies: numpy, scipy, matplotlib  (from-scratch; no external KF library needed)
Run:          python3 ekf_line_temp_demo.py
Output:       ekf_line_temp.png (three-subplot figure, saved beside this script)
              Console: temperature / ampacity readout

Drake ACSR conductor constants used throughout:
  mCp     = 534.0 J/(m·°C)   heat capacity per unit length
  R25     = 7.28e-5 Ω/m       DC resistance at 25°C
  alpha_R = 0.00403 /°C       temperature coefficient of resistance
  D       = 0.0281 m          outer diameter
  eps     = 0.5               emissivity
  alpha_s = 0.5               solar absorptivity
  Qse     = 900.0 W/m²        solar irradiance

Measurement architecture (architecture 3 from KAL-04 design):
  h(Tc) = R25 * (1 + alpha_R * (Tc - 25))   [apparent resistance, Ω/m]
  H     = R25 * alpha_R                       [measurement Jacobian, scalar]
  This is realistic: infer Tc from voltage-drop / current measurement pair.
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')   # non-interactive backend — works without a display
import matplotlib.pyplot as plt
from scipy.stats import chi2


# ---------------------------------------------------------------------------
# Drake ACSR physical constants
# ---------------------------------------------------------------------------
MCP = 534.0        # J/(m·°C)  heat capacity per unit length
R25 = 7.28e-5      # Ω/m       DC resistance at 25°C
ALPHA_R = 0.00403  # /°C       temperature coefficient of resistance
D = 0.0281         # m         conductor outer diameter
EPS = 0.5          # —         emissivity
ALPHA_S = 0.5      # —         solar absorptivity
QSE = 900.0        # W/m²      solar irradiance (broadside, midday, simplified)
RHO_F = 1.20       # kg/m³     air density at ~50°C film temperature


# ---------------------------------------------------------------------------
# IEEE 738 thermal model  —  right-hand side of mCp * dTc/dt = qi+qs-qc-qr
# ---------------------------------------------------------------------------

def ieee738_rhs(t, Tc, I, Ta, v_wind=0.0):
    """Right-hand side of the IEEE 738 conductor thermal balance ODE.

    mCp * dTc/dt = qi + qs - qc - qr

    Parameters
    ----------
    t      : float  time (unused; present for solve_ivp compatibility)
    Tc     : float  conductor temperature, °C
    I      : float  line current, A
    Ta     : float  ambient temperature, °C
    v_wind : float  wind speed m/s (unused; natural-convection model only)

    Returns
    -------
    dTc_dt : float  rate of change of conductor temperature, °C/s
    """
    # Resistance at current temperature  R(Tc) = R25 * [1 + alpha_R * (Tc-25)]
    R_Tc = R25 * (1.0 + ALPHA_R * (Tc - 25.0))

    # Resistive (Joule) heating  qi = I² R(Tc)  [W/m]
    qi = I**2 * R_Tc

    # Solar heat gain (simplified: broadside sun, no angle correction)  [W/m]
    qs = ALPHA_S * QSE * D

    # Natural convection cooling  [W/m]
    # qc = 0.0205 * rho_f^0.5 * D_mm^0.75 * (Tc-Ta)^1.25
    # Guard against negative (Tc < Ta) to avoid domain error in fractional power
    delta_T = max(Tc - Ta, 0.0)
    qc = 0.0205 * RHO_F**0.5 * (D * 1000.0)**0.75 * delta_T**1.25

    # Radiative cooling  [W/m]  (Stefan-Boltzmann form from IEEE 738)
    qr = 0.0178 * D * EPS * ((Tc + 273.0)**4 - (Ta + 273.0)**4) / 1e8

    return (qi + qs - qc - qr) / MCP


# ---------------------------------------------------------------------------
# Process Jacobian  A = df/dTc  (analytic)
# ---------------------------------------------------------------------------

def _process_jacobian(Tc, I, Ta, dt=1.0):
    """Analytic Jacobian of the Euler-discretised process model.

    f(Tc) = Tc + dt * ieee738_rhs(Tc)
    A = df/dTc = 1 + (dt/mCp) * [I² dR/dTc - dqc/dTc - dqr/dTc]
    """
    # d(qi)/d(Tc) = I² * R25 * alpha_R
    dqi_dTc = I**2 * R25 * ALPHA_R

    # d(qc)/d(Tc) = 0.0205 * rho_f^0.5 * D_mm^0.75 * 1.25 * (Tc-Ta)^0.25
    # Small floor avoids zero raised to fractional power
    delta_T = max(Tc - Ta, 0.1)
    dqc_dTc = 0.0205 * RHO_F**0.5 * (D * 1000.0)**0.75 * 1.25 * delta_T**0.25

    # d(qr)/d(Tc) = 4 * 0.0178 * D * eps * (Tc+273)^3 / 1e8
    dqr_dTc = 4.0 * 0.0178 * D * EPS * (Tc + 273.0)**3 / 1e8

    return 1.0 + (dt / MCP) * (dqi_dTc - dqc_dTc - dqr_dTc)


# ---------------------------------------------------------------------------
# EKF  —  one predict-update cycle
# ---------------------------------------------------------------------------

def ekf_step(Tc_hat, P, I, Ta, z_meas, Q, R_noise, dt=1.0):
    """One EKF predict-update cycle (scalar state).

    State       : Tc (°C)
    Inputs      : I (A), Ta (°C)
    Measurement : z = apparent resistance R_meas = R25*(1+alpha_R*(Tc-25))  [Ω/m]

    Parameters
    ----------
    Tc_hat  : float  prior state estimate (°C)
    P       : float  prior state covariance (°C²)
    I       : float  current (A)
    Ta      : float  ambient temperature (°C)
    z_meas  : float  measured apparent resistance (Ω/m)
    Q       : float  process noise variance (°C²/step)
    R_noise : float  measurement noise variance ((Ω/m)²)
    dt      : float  time step (s)

    Returns
    -------
    Tc_post : float  updated state estimate
    P_post  : float  updated covariance
    innov   : float  innovation  y_k = z_meas - z_pred
    S       : float  innovation covariance
    """
    # === PREDICT ===
    rhs = ieee738_rhs(0.0, Tc_hat, I, Ta)
    Tc_pred = Tc_hat + dt * rhs              # Euler step

    A = _process_jacobian(Tc_hat, I, Ta, dt)
    P_pred = A**2 * P + Q                    # scalar covariance propagation

    # === UPDATE ===
    # Measurement Jacobian: H = d/dTc [R25*(1+alpha_R*(Tc-25))] = R25*alpha_R
    H = R25 * ALPHA_R                        # constant scalar ≈ 2.93e-7 Ω/(m·°C)

    z_pred = R25 * (1.0 + ALPHA_R * (Tc_pred - 25.0))
    innov = z_meas - z_pred                  # innovation y_k

    S = H**2 * P_pred + R_noise              # innovation covariance
    K = H * P_pred / S                       # Kalman gain

    Tc_post = Tc_pred + K * innov
    P_post = (1.0 - K * H) * P_pred         # standard form

    return Tc_post, P_post, innov, S


# ---------------------------------------------------------------------------
# Normalized Innovation Squared (NIS) divergence check
# ---------------------------------------------------------------------------

def nis_check(innov, S, confidence=0.95):
    """Return (NIS, is_diverging) for a scalar measurement.

    NIS = innov² / S ~ chi²(1) under a healthy, well-tuned filter.
    If NIS > chi2.ppf(0.95, df=1) = 3.84, the filter may be diverging.
    """
    NIS = innov**2 / S
    threshold = chi2.ppf(confidence, df=1)
    return NIS, bool(NIS > threshold)


# ---------------------------------------------------------------------------
# IEEE 738 steady-state ampacity (Dynamic Line Rating)
# ---------------------------------------------------------------------------

def ieee738_ampacity(Tc_max, Ta):
    """Compute DLR ampacity: max current (A) to keep conductor <= Tc_max.

    Solves  I_max² * R(Tc_max) = qc(Tc_max) + qr(Tc_max) - qs
    (natural convection, simplified solar model).
    """
    R_max = R25 * (1.0 + ALPHA_R * (Tc_max - 25.0))

    delta_T = max(Tc_max - Ta, 0.0)
    qc = 0.0205 * RHO_F**0.5 * (D * 1000.0)**0.75 * delta_T**1.25
    qr = 0.0178 * D * EPS * ((Tc_max + 273.0)**4 - (Ta + 273.0)**4) / 1e8
    qs = ALPHA_S * QSE * D                   # simplified solar

    available = max(qc + qr - qs, 0.0)      # heat balance available for resistive heating
    return np.sqrt(available / R_max)


# ---------------------------------------------------------------------------
# Main demo: simulation + EKF loop + plot
# ---------------------------------------------------------------------------

def run_demo():
    """Simulate conductor temperature ground truth, run EKF, plot and save PNG."""
    np.random.seed(42)

    dt = 1.0         # 1-second time step
    T_sim = 3600     # 1-hour simulation
    t = np.arange(0.0, T_sim, dt)
    N = len(t)

    # Scenario: current ramps from 400 A to 600 A over the hour
    I_profile = np.linspace(400.0, 600.0, N)
    Ta = 30.0        # °C  constant ambient temperature

    # ---- Simulate true conductor temperature (Euler integration) ----
    Tc_true = np.zeros(N)
    Tc_true[0] = 35.0   # °C  initial true temperature
    for k in range(N - 1):
        Tc_true[k + 1] = Tc_true[k] + dt * ieee738_rhs(0.0, Tc_true[k], I_profile[k], Ta)

    # ---- Generate noisy apparent-resistance measurements ----
    R_noise_std = 5e-8    # Ω/m  (≈ 0.07% of R25 — realistic PMU-grade CT accuracy)
    R_meas = (R25 * (1.0 + ALPHA_R * (Tc_true - 25.0))
              + np.random.normal(0.0, R_noise_std, N))

    # ---- EKF parameters ----
    Q = 0.05                      # °C²/step  process noise (model uncertainty: wind gusts, etc.)
    R_meas_var = R_noise_std**2   # (Ω/m)²    measurement noise variance

    # ---- Storage ----
    Tc_ekf = np.zeros(N)
    P_ekf = np.zeros(N)
    innov_seq = np.zeros(N)
    nis_seq = np.zeros(N)

    Tc_ekf[0] = 40.0    # °C  wrong initial guess (true is 35°C — testing convergence)
    P_ekf[0] = 100.0    # °C²  high initial uncertainty (±10°C)

    # ---- EKF loop ----
    divergence_count = 0
    for k in range(N - 1):
        Tc_ekf[k + 1], P_ekf[k + 1], innov_seq[k + 1], S = ekf_step(
            Tc_ekf[k], P_ekf[k], I_profile[k], Ta,
            R_meas[k + 1], Q, R_meas_var, dt
        )
        nis_val, is_div = nis_check(innov_seq[k + 1], S)
        nis_seq[k + 1] = nis_val
        if is_div:
            divergence_count += 1

    # ---- Console readout ----
    Tc_final_ekf = Tc_ekf[-1]
    Tc_final_true = Tc_true[-1]
    sigma_final = np.sqrt(max(P_ekf[-1], 0.0))
    I_max_dlr = ieee738_ampacity(Tc_max=75.0, Ta=Ta)

    print("=" * 62)
    print("  IEEE 738 EKF — Conductor Temperature & Dynamic Line Rating")
    print("=" * 62)
    print(f"  Simulation duration       : {T_sim / 60:.0f} min")
    print(f"  Current range             : {I_profile[0]:.0f} – {I_profile[-1]:.0f} A")
    print()
    print(f"  Final true Tc             : {Tc_final_true:.2f} °C")
    print(f"  EKF estimate              : {Tc_final_ekf:.2f} °C  (±{2*sigma_final:.2f} °C, 2σ)")
    print(f"  EKF estimation error      : {abs(Tc_final_ekf - Tc_final_true):.3f} °C")
    print()
    print(f"  DLR ampacity (Tc≤75°C)   : {I_max_dlr:.0f} A  [Dynamic Line Rating]")
    print(f"  Applied current at t=1h   : {I_profile[-1]:.0f} A")
    headroom = I_max_dlr - I_profile[-1]
    if headroom >= 0:
        print(f"  DLR headroom              : {headroom:.0f} A remaining before thermal limit")
    else:
        print(f"  ** WARNING: current exceeds DLR ampacity by {-headroom:.0f} A **")
    print()
    print(f"  NIS divergence alerts     : {divergence_count} / {N} steps "
          f"({100*divergence_count/N:.1f}%)  [expect ~5% at 95th pct threshold]")
    print("=" * 62)
    print()

    # ---- Three-subplot figure ----
    sigma_ekf = np.sqrt(np.maximum(P_ekf, 0.0))   # guard negative P from numerical noise

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 9), sharex=True)
    fig.suptitle(
        "IEEE 738 EKF — Conductor Temperature Estimation (Drake ACSR)",
        fontsize=13, fontweight='bold'
    )

    # Subplot 1: True Tc vs EKF estimate with ±2σ uncertainty band
    ax1.plot(t / 60.0, Tc_true, color='black', linewidth=1.5, label='True Tc')
    ax1.plot(t / 60.0, Tc_ekf, color='red', linewidth=1.5, linestyle='--', label='EKF estimate')
    ax1.fill_between(
        t / 60.0,
        Tc_ekf - 2.0 * sigma_ekf,
        Tc_ekf + 2.0 * sigma_ekf,
        alpha=0.25, color='red', label='±2σ band'
    )
    ax1.axhline(75.0, color='darkorange', linestyle=':', linewidth=1.0, label='75°C thermal limit')
    ax1.set_ylabel('Conductor Temp (°C)')
    ax1.legend(loc='upper left', fontsize=9)
    ax1.grid(True, alpha=0.3)

    # Subplot 2: Innovation sequence (should be zero-mean for healthy filter)
    ax2.plot(t / 60.0, innov_seq, color='steelblue', linewidth=0.8, alpha=0.7)
    ax2.axhline(0, color='k', linestyle='--', linewidth=1.0)   # zero reference line
    ax2.set_ylabel('Innovation (Ω/m)')
    ax2.grid(True, alpha=0.3)

    # Subplot 3: Uncertainty σ over time (shows filter convergence)
    ax3.plot(t / 60.0, sigma_ekf, color='green', linewidth=1.2)
    ax3.set_ylabel('Uncertainty σ (°C)')
    ax3.set_xlabel('Time (min)')
    ax3.grid(True, alpha=0.3)

    plt.tight_layout()

    # Save PNG beside this script regardless of the caller's cwd
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(script_dir, 'ekf_line_temp.png')
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    print(f"Saved {out_path}")


if __name__ == '__main__':
    run_demo()
