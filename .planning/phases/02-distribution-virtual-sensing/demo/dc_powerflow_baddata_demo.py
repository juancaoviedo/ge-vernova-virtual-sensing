"""
dc_powerflow_baddata_demo.py
----------------------------
From-scratch 3-bus DC power-flow weighted-least-squares (WLS) state estimator
that infers bus voltage angles from a redundant measurement set, then detects
and removes a single gross error via the chi-squared test (is there bad data?)
and the largest normalized residual (which measurement?).

This is the TVS-02 + TVS-03 hands-on demo for interview preparation — the
linear (DC) special case of the Phase-1 KAL-01 WLS/Gauss-Newton machinery:
because h(theta) = H @ theta is linear, the iteration collapses to a one-shot
normal-equations solve.

Dependencies: numpy, scipy, matplotlib  (from-scratch; no SE / power-flow library needed)
Run:          python3 dc_powerflow_baddata_demo.py
Output:       dc_powerflow_baddata.png (saved beside this script)
              Console: chi-squared / flagged-measurement / re-solved-angles readout

3-bus network constants used throughout:
  b12 = b13 = b23 = 10 p.u.   line susceptances (reactance x = 0.1 p.u. each)
  slack = bus 1, theta_1 = 0  reference; state = [theta_2, theta_3] (n = 2)
  loads P2 = -1.0, P3 = -0.5 p.u.  true bus injections
  m = 5 measurements [inj@2, inj@3, flow 1->2, flow 1->3, flow 2->3] -> df = m - n = 3
"""

import os
import numpy as np
import matplotlib
matplotlib.use('Agg')   # non-interactive backend — works without a display
import matplotlib.pyplot as plt
from scipy.stats import chi2


# ---------------------------------------------------------------------------
# 3-bus DC power-flow constants
# ---------------------------------------------------------------------------
B12 = 10.0    # p.u.   susceptance of line 1-2  (x = 0.1 p.u.)
B13 = 10.0    # p.u.   susceptance of line 1-3
B23 = 10.0    # p.u.   susceptance of line 2-3
P2 = -1.0     # p.u.   true power injection (load) at bus 2
P3 = -0.5     # p.u.   true power injection (load) at bus 3
SIGMA = 0.01  # p.u.   measurement noise standard deviation
SLACK_BUS = 1 # reference bus, theta_1 = 0 (rows/cols deleted from B)


def build_B_matrix():
    """Reduced bus susceptance matrix (slack row/col deleted) -> [[20,-10],[-10,20]].

    Full DC B-bus is the susceptance Laplacian; deleting the slack (bus 1)
    row and column leaves the reduced 2x2 system B_red @ [theta_2, theta_3] = [P2, P3].
    """
    B_red = np.array([[B12 + B23, -B23],
                      [-B23,       B13 + B23]])   # = [[20, -10], [-10, 20]]
    return B_red


def build_H():
    """m=5 x n=2 measurement matrix: sensitivity of each measurement to [theta_2, theta_3].

    Rows (linear DC, slack theta_1 = 0):
      0  injection @ bus 2 : P2 = b12*(t2-0) + b23*(t2-t3) = 20*t2 - 10*t3
      1  injection @ bus 3 : P3 = b13*(t3-0) + b23*(t3-t2) = -10*t2 + 20*t3
      2  flow 1->2         : b12*(t1-t2) = -10*t2
      3  flow 1->3         : b13*(t1-t3) = -10*t3
      4  flow 2->3         : b23*(t2-t3) = 10*t2 - 10*t3
    """
    H = np.array([
        [B12 + B23, -B23],        # injection @ bus 2
        [-B23,       B13 + B23],  # injection @ bus 3
        [-B12,       0.0],        # flow 1->2
        [0.0,       -B13],        # flow 1->3
        [B23,       -B23],        # flow 2->3
    ])
    return H


def wls_solve(H, W, z):
    """One-shot linear WLS (DC collapse of KAL-01's normal equations)."""
    G = H.T @ W @ H                          # gain / information matrix
    theta_hat = np.linalg.solve(G, H.T @ W @ z)
    r = z - H @ theta_hat                    # residuals
    J = r @ W @ r                            # weighted residual cost ~ chi2(m-n)
    return theta_hat, r, J, G


def chi2_test(J, df, confidence=0.95):
    """Detection: is there bad data? J > chi2.ppf(0.95, df) flags an inconsistency."""
    threshold = chi2.ppf(confidence, df)
    return threshold, bool(J > threshold)


def normalized_residuals(r, H, G, W):
    """Identification: largest normalized residual names the suspect measurement.

    Omega = R - H G^-1 H^T is the residual covariance; rN_i = |r_i| / sqrt(Omega_ii).
    """
    Omega = np.diag(1.0 / np.diag(W)) - H @ np.linalg.inv(G) @ H.T   # R - H G^-1 H^T
    rN = np.abs(r) / np.sqrt(np.diag(Omega))
    return rN


def run_demo():
    """Solve the 3-bus DC WLS, inject + detect + remove a gross error, plot and save PNG."""
    np.random.seed(42)

    MEAS_LABELS = ['inj@2', 'inj@3', 'flow 1->2', 'flow 1->3', 'flow 2->3']
    BAD_IDX = 4                       # corrupt measurement 5 (line flow 2->3)

    # ---- Ground truth: solve reduced DC power flow B_red @ theta = P ----
    B_red = build_B_matrix()
    theta_true = np.linalg.solve(B_red, np.array([P2, P3]))   # ~ [-0.0833, -0.0667] rad

    # ---- Build measurements: z = H @ theta_true + noise ----
    H = build_H()
    m, n = H.shape
    assert np.linalg.matrix_rank(H) == n, "H must be full column rank (observable)"
    W = np.diag(np.full(m, 1.0 / SIGMA**2))                   # W = R^-1
    z_clean = H @ theta_true
    z = z_clean + np.random.normal(0.0, SIGMA, m)

    # ---- Inject a gross error on measurement 5 (flow 2->3) ----
    z[BAD_IDX] += 15.0 * SIGMA                                # ~15-sigma gross error

    # ---- WLS solve #1 (with bad data) ----
    theta1, r1, J1, G1 = wls_solve(H, W, z)
    df1 = m - n
    thr1, bad1 = chi2_test(J1, df1)

    # ---- Identify the suspect via largest normalized residual ----
    rN = normalized_residuals(r1, H, G1, W)
    suspect = int(np.argmax(rN))

    # ---- Remove the flagged measurement and re-solve (WLS solve #2) ----
    keep = [i for i in range(m) if i != suspect]
    H2, z2, W2 = H[keep], z[keep], np.diag(np.diagonal(W)[keep])
    theta2, r2, J2, _ = wls_solve(H2, W2, z2)
    df2 = len(keep) - n
    thr2, bad2 = chi2_test(J2, df2)

    # ---- Console readout ----
    print("=" * 62)
    print("  3-Bus DC State Estimation — Bad-Data Detection (chi2 + rN)")
    print("=" * 62)
    print(f"  States (angles)           : theta_2, theta_3  (n = {n})")
    print(f"  Measurements              : {m}  -> redundancy df = {df1}")
    print(f"  Corrupted measurement     : #{BAD_IDX + 1} ({MEAS_LABELS[BAD_IDX]}), +15 sigma")
    print()
    print("  --- Solve #1 (with bad data) ---")
    print(f"  chi2 threshold (95%, df={df1}) : {thr1:.3f}")
    print(f"  J(theta_hat)              : {J1:.3f}   -> "
          f"{'BAD DATA DETECTED' if bad1 else 'no bad data'}")
    print(f"  Flagged measurement       : #{suspect + 1} ({MEAS_LABELS[suspect]}), "
          f"rN = {rN[suspect]:.2f}  (others < {np.partition(rN, -2)[-2]:.2f})")
    print(f"  Estimated angles          : "
          f"[{theta1[0]:+.4f}, {theta1[1]:+.4f}] rad")
    print()
    print("  --- Solve #2 (suspect removed) ---")
    print(f"  chi2 threshold (95%, df={df2}) : {thr2:.3f}")
    print(f"  J(theta_hat)              : {J2:.3f}   -> "
          f"{'bad data' if bad2 else 'CLEAN (below threshold)'}")
    print(f"  Re-solved angles          : "
          f"[{theta2[0]:+.4f}, {theta2[1]:+.4f}] rad")
    print(f"  True angles               : "
          f"[{theta_true[0]:+.4f}, {theta_true[1]:+.4f}] rad")
    err1 = np.linalg.norm(theta1 - theta_true)
    err2 = np.linalg.norm(theta2 - theta_true)
    print(f"  Angle error (before/after): {err1:.4f} -> {err2:.4f} rad")
    print("=" * 62)
    print()

    # ---- Two-panel figure ----
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(
        "3-Bus DC State Estimation — Bad-Data Detection (chi2 + largest rN)",
        fontsize=13, fontweight='bold'
    )

    # Panel 1: normalized residuals bar chart with 3-sigma line, flagged bar highlighted
    colors = ['crimson' if i == suspect else 'steelblue' for i in range(m)]
    ax1.bar(range(m), rN, color=colors)
    ax1.axhline(3.0, color='darkorange', linestyle='--', linewidth=1.2,
                label='3-sigma identification threshold')
    ax1.set_xticks(range(m))
    ax1.set_xticklabels(MEAS_LABELS, rotation=20, ha='right', fontsize=9)
    ax1.set_ylabel('Normalized residual  rN = |r| / sqrt(Omega_ii)')
    ax1.set_title('Identification: largest rN names the bad measurement')
    ax1.legend(loc='upper left', fontsize=9)
    ax1.grid(True, axis='y', alpha=0.3)

    # Panel 2: true vs estimated angles, before vs after removal
    x = np.arange(n)
    width = 0.25
    ax2.bar(x - width, theta_true, width, label='True', color='black')
    ax2.bar(x, theta1, width, label='Estimate (bad data)', color='crimson', alpha=0.8)
    ax2.bar(x + width, theta2, width, label='Estimate (after removal)', color='seagreen')
    ax2.set_xticks(x)
    ax2.set_xticklabels(['theta_2', 'theta_3'])
    ax2.set_ylabel('Voltage angle (rad)')
    ax2.set_title('State estimate recovers truth after removal')
    ax2.legend(loc='upper right', fontsize=9)
    ax2.grid(True, axis='y', alpha=0.3)

    plt.tight_layout()

    # Save PNG beside this script regardless of the caller's cwd
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(script_dir, 'dc_powerflow_baddata.png')
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    print(f"Saved {out_path}")


if __name__ == '__main__':
    run_demo()
