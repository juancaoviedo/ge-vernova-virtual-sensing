"""
estimators.py
-------------
Three state estimators behind one pluggable interface for the IEEE 33-bus System 2
AC Distribution State Estimator.

Provides:
  - RankDeficientError : exception raised when G = H^T W H is rank-deficient
  - BaseEstimator      : abstract base class with predict / update / x / P interface
  - wls_gauss_newton   : AC WLS Gauss-Newton iteration (lifted from dc_powerflow_baddata_demo.py)
  - chi2_bad_data      : chi-squared test + largest normalized residual (LNR) bad-data detection
  - WLSEstimator       : snapshot WLS (no recursive predict; each update is independent)
  - EKFEstimator       : recursive Extended Kalman Filter, FASE predict, Joseph-form P update
  - UKFEstimator       : square-root Unscented Kalman Filter, no Jacobian, FASE predict

Interface contract (D-02):
  - Every estimator exposes .predict(delta_p_fcst, S, Cov_eps) and .update(z, R, h_fn, H_fn)
  - WLSEstimator.predict is a no-op (snapshot WLS solves independently per snapshot)
  - EKFEstimator/UKFEstimator.predict integrates the FASE prior; .update uses the measurement model
  - .x returns the current state estimate (np.ndarray, shape (66,) for 64 free + 2 slack fixed)
  - .P returns the current posterior covariance (np.ndarray, shape (66,66))

EKF Landmine (PATTERNS Landmine 7):
  Joseph-form P update is MANDATORY: P = (I-KH)P(I-KH)^T + KRK^T
  Standard P = (I-KH)P is numerically unsafe over 96 steps.

UKF Landmine (PATTERNS Landmine 8):
  Symmetrize P before cholesky: cholesky((P+P.T)/2, lower=True)
  Floating-point asymmetry can make a positive-definite P appear non-symmetric.

Oracle separation:
  Zero references to oracle bucket names or oracle read helpers in this file.
  Verified by grep (see PATTERNS.md oracle_separation_boundary).

No I/O: no MQTT, no InfluxDB, no oracle access. Pure compute over in-memory arrays.
Dependencies: numpy, scipy
"""

import numpy as np
from abc import ABC, abstractmethod
from scipy.linalg import cholesky
from scipy.stats import chi2 as chi2_dist

from ieee33 import estimate_config as ec


# ---------------------------------------------------------------------------
# Exception
# ---------------------------------------------------------------------------

class RankDeficientError(Exception):
    """Raised when the gain matrix G = H^T W H is rank-deficient.

    This indicates the system is under-observable (measurement redundancy < 1.0).
    Do NOT catch and ignore — surface to caller for diagnosis.
    Resolution: add pseudo-measurements (zero-injection rows) to bring redundancy > 1.0.
    """


# ---------------------------------------------------------------------------
# Abstract base class
# ---------------------------------------------------------------------------

class BaseEstimator(ABC):
    """Abstract base for WLS, EKF, and UKF estimators.

    All three estimators share the same predict / update interface so the
    runner (estimate.py) can swap them with a single --estimator flag (D-02).

    Predict step:
        EKF/UKF: advance state mean and covariance using the FASE prior
                 (provided by FASEPredictor from fase_predict.py).
        WLS: no-op (each snapshot is solved independently from a flat start).

    Update step:
        All: fuse the current measurement vector z with the measurement model
             h_fn / H_fn evaluated at the current state estimate.
    """

    @abstractmethod
    def predict(self, delta_p_fcst: np.ndarray, S: np.ndarray, Cov_eps: np.ndarray) -> None:
        """Advance state prior using FASE sensitivity.

        Parameters
        ----------
        delta_p_fcst : np.ndarray shape (n_inj,)  change in forecast injections Δp
        S            : np.ndarray shape (n_state, n_inj)  sensitivity matrix ∂x/∂p
        Cov_eps      : np.ndarray shape (n_inj, n_inj)  covariance of forecast error
        """

    @abstractmethod
    def update(
        self,
        z: np.ndarray,
        R: np.ndarray,
        h_fn,
        H_fn,
    ):
        """Fuse measurement vector z with the measurement model.

        Parameters
        ----------
        z    : np.ndarray shape (m,)  measurement vector (aligned with meas_list)
        R    : np.ndarray shape (m,m)  measurement noise covariance
        h_fn : callable  h_fn(x) -> z_pred  (AC measurement function from ac_model)
        H_fn : callable  H_fn(x) -> H       (Jacobian from ac_model; WLS + EKF need it;
                                              UKF ignores H_fn but accepts the arg for API parity)
        """

    @property
    @abstractmethod
    def x(self) -> np.ndarray:
        """Current state estimate, shape (n_state,)."""

    @property
    @abstractmethod
    def P(self) -> np.ndarray:
        """Current posterior covariance, shape (n_state, n_state)."""


# ---------------------------------------------------------------------------
# Gauss-Newton WLS + bad-data detection (lifted from dc_powerflow_baddata_demo.py)
# ---------------------------------------------------------------------------

def wls_gauss_newton(h_fn, H_fn, z, W, x0, max_iter=None, tol=None):
    """AC WLS Gauss-Newton iteration.

    AC lift of dc_powerflow_baddata_demo.wls_solve.  Because h(x) is nonlinear
    in AC, we iterate: each step linearises around x, solves the normal equations,
    and updates x.  Converges in ≤5 iterations for distribution networks with
    voltages near 1.0 pu (flat-start safe).

    Parameters
    ----------
    h_fn    : callable  h_fn(x) -> z_pred, shape (m,)
    H_fn    : callable  H_fn(x) -> H matrix, shape (m, n_state)
    z       : np.ndarray (m,)  measurement vector
    W       : np.ndarray (m,m)  weight matrix = R^{-1}
    x0      : np.ndarray (n_state,)  initial state (flat start: |V|=1, theta=0)
    max_iter: int  maximum Gauss-Newton iterations (default: ec.GAUSS_NEWTON_MAX_ITER)
    tol     : float  convergence tolerance on ||dx||_2 (default: ec.GAUSS_NEWTON_TOL)

    Returns
    -------
    x : np.ndarray (n_state,)  converged state estimate
    G : np.ndarray (n_state, n_state)  gain matrix H^T W H (used for bad-data detection)

    Raises
    ------
    RankDeficientError if G = H^T W H is rank-deficient (under-observable system).
    """
    if max_iter is None:
        max_iter = ec.GAUSS_NEWTON_MAX_ITER
    if tol is None:
        tol = ec.GAUSS_NEWTON_TOL

    x = x0.copy()
    G = None
    for _ in range(max_iter):
        r = z - h_fn(x)          # residuals
        H = H_fn(x)              # analytic Jacobian
        G = H.T @ W @ H          # gain matrix
        if np.linalg.matrix_rank(G) < G.shape[0]:
            raise RankDeficientError(
                "G = H^T W H is rank-deficient (system under-observable). "
                "Add pseudo measurements to achieve redundancy > 1.0. "
                f"G shape={G.shape}, rank={np.linalg.matrix_rank(G)}"
            )
        dx = np.linalg.solve(G, H.T @ W @ r)
        x = x + dx
        if np.linalg.norm(dx) < tol:
            break
    return x, G


def chi2_bad_data(r, W, G, H, df, confidence=0.95):
    """Chi-squared + LNR bad-data detection.

    AC lift of dc_powerflow_baddata_demo.chi2_test + normalized_residuals.

    Parameters
    ----------
    r          : np.ndarray (m,)  residuals z - h(x_hat)
    W          : np.ndarray (m,m)  weight matrix R^{-1}
    G          : np.ndarray (n, n)  gain matrix H^T W H
    H          : np.ndarray (m, n)  Jacobian at x_hat
    df         : int  degrees of freedom (m - n)
    confidence : float  chi2 confidence level (default 0.95)

    Returns
    -------
    J         : float  weighted residual norm r^T W r
    threshold : float  chi2.ppf(confidence, df)
    bad       : bool   True if J > threshold
    rN        : np.ndarray (m,)  normalized residuals |r_i| / sqrt(|Omega_ii|)

    Notes
    -----
    Omega = R - H G^{-1} H^T is the residual covariance matrix.
    The diagonal of Omega can go negative at high leverage points (PATTERNS line 453).
    We clamp to abs(diag(Omega)) to avoid sqrt of negative values.
    """
    J = float(r @ W @ r)
    threshold = float(chi2_dist.ppf(confidence, df))
    bad = bool(J > threshold)

    # LNR identification: Omega = diag(1/W) - H G^{-1} H^T
    # Use R = diag(1 / diag(W)) (diagonal assumption)
    R_diag = 1.0 / np.diag(W)
    Omega = np.diag(R_diag) - H @ np.linalg.inv(G) @ H.T
    # Clamp to abs to handle high-leverage negative diagonal (PATTERNS Landmine)
    rN = np.abs(r) / np.sqrt(np.abs(np.diag(Omega)))
    return J, threshold, bad, rN


# ---------------------------------------------------------------------------
# WLSEstimator
# ---------------------------------------------------------------------------

class WLSEstimator(BaseEstimator):
    """Snapshot AC-WLS estimator (no recursive state; each update is independent).

    No predict step: WLS solves from a flat start (|V|=1.0 pu, theta=0) on every
    snapshot.  This is the baseline against which EKF/UKF are compared.

    .P is set to G^{-1} after each solve (approximate posterior covariance).
    """

    def __init__(self, n: int = ec.N_FREE_STATES, q_floor_scale: float = 1e-8):
        self.n = n
        self._x = np.zeros(n)
        self._P = np.eye(n)
        # flat start: interleaved |V|=1, theta=0
        self._x0 = np.zeros(n)
        self._x0[0::2] = 1.0  # |V| = 1.0 pu
        # q_floor_scale kept for interface parity (WLS does not use Q)
        self._q_floor_scale = q_floor_scale

    def predict(self, delta_p_fcst: np.ndarray, S: np.ndarray, Cov_eps: np.ndarray) -> None:
        """No-op: WLS solves independently from flat start each snapshot."""

    def update(self, z: np.ndarray, R: np.ndarray, h_fn, H_fn):
        """Run one Gauss-Newton solve from flat start; store x_hat and P = G^{-1}.

        Parameters
        ----------
        z    : np.ndarray (m,)
        R    : np.ndarray (m,m)  measurement noise covariance (diagonal expected)
        h_fn : callable  h_fn(x) -> z_pred
        H_fn : callable  H_fn(x) -> H

        Raises
        ------
        RankDeficientError if gain matrix is rank-deficient.
        """
        W = np.linalg.inv(R) if R.ndim == 2 else np.diag(1.0 / R)
        x_hat, G = wls_gauss_newton(
            h_fn, H_fn, z, W, self._x0,
            max_iter=ec.GAUSS_NEWTON_MAX_ITER,
            tol=ec.GAUSS_NEWTON_TOL,
        )
        self._x = x_hat
        try:
            self._P = np.linalg.inv(G)
        except np.linalg.LinAlgError:
            self._P = np.eye(self.n)

    @property
    def x(self) -> np.ndarray:
        return self._x

    @property
    def P(self) -> np.ndarray:
        return self._P


# ---------------------------------------------------------------------------
# EKFEstimator
# ---------------------------------------------------------------------------

class EKFEstimator(BaseEstimator):
    """Recursive Extended Kalman Filter with FASE predict step.

    FASE predict (D-05):
        x⁻ = x + S·Δp_fcst
        P⁻ = P + S·Cov(ε)·Sᵀ + Q_floor

    Joseph-form P update (MANDATORY — Landmine 7):
        K     = P H^T (H P H^T + R)^{-1}
        x_hat = x⁻ + K·y
        I_KH  = I - K·H
        P     = (I-KH) P (I-KH)^T + K R K^T   ← Joseph form, symmetric + PD
    """

    def __init__(self, n: int = ec.N_FREE_STATES, q_floor_scale: float = None):
        if q_floor_scale is None:
            q_floor_scale = ec.ACTIVE.get("q_floor_scale", 1e-8)
        self.n = n
        # flat start: interleaved |V|=1, theta=0 (distribution voltages near 1.0 pu)
        self._x = np.zeros(n)
        self._x[0::2] = 1.0
        self._P = np.eye(n) * 0.01
        self.Q_floor = np.eye(n) * q_floor_scale

    def predict(self, delta_p_fcst: np.ndarray, S: np.ndarray, Cov_eps: np.ndarray) -> None:
        """FASE predict: propagate mean and covariance using sensitivity matrix S.

        Parameters
        ----------
        delta_p_fcst : (n_inj,)   change in forecast injection at step k vs k-1
        S            : (n, n_inj) sensitivity dstate/dinjection from ac_model.fase_sensitivity
        Cov_eps      : (n_inj, n_inj) diagonal covariance of forecast error ε
        """
        self._x = self._x + S @ delta_p_fcst
        Q = S @ Cov_eps @ S.T + self.Q_floor
        self._P = self._P + Q

    def update(self, z: np.ndarray, R: np.ndarray, h_fn, H_fn):
        """EKF update with Joseph-form covariance.

        Parameters
        ----------
        z    : (m,)  measurement vector
        R    : (m,m)  measurement noise covariance
        h_fn : callable  h_fn(x) -> z_pred  (from ac_model)
        H_fn : callable  H_fn(x) -> H       (Jacobian from ac_model)

        Returns
        -------
        y     : np.ndarray (m,)  innovation z - h(x⁻)
        S_inn : np.ndarray (m,m)  innovation covariance H P H^T + R
        """
        H = H_fn(self._x)
        y = z - h_fn(self._x)          # innovation
        S_inn = H @ self._P @ H.T + R  # innovation covariance
        # Kalman gain: K = P H^T S_inn^{-1}
        K = self._P @ H.T @ np.linalg.solve(S_inn.T, np.eye(len(z))).T
        self._x = self._x + K @ y
        # Joseph form — MANDATORY (Landmine 7; standard form is numerically unsafe)
        I_KH = np.eye(self.n) - K @ H
        self._P = I_KH @ self._P @ I_KH.T + K @ R @ K.T
        return y, S_inn

    @property
    def x(self) -> np.ndarray:
        return self._x

    @property
    def P(self) -> np.ndarray:
        return self._P


# ---------------------------------------------------------------------------
# UKFEstimator (square-root form)
# ---------------------------------------------------------------------------

class UKFEstimator(BaseEstimator):
    """Recursive square-root Unscented Kalman Filter with FASE predict.

    Uses the Cholesky factor S_P of P instead of P directly to guarantee
    positive-definiteness through all operations (Landmine 8).

    No Jacobian: sigma points propagate through h_fn directly (key advantage
    over EKF for the nonlinear AC measurement model).

    Defaults: alpha=1e-3, beta=2.0, kappa=0.0  (Van der Merwe & Wan 2001).

    FASE predict:
        x⁻ = x + S·Δp_fcst
        P_new = S_P S_P^T + Q
        S_P = chol((P_new + P_new^T)/2, lower=True)   ← symmetrize THEN cholesky

    UKF update:
        Generate 2n+1 sigma points from (x, S_P)
        Propagate each through h_fn
        Form innovation covariances Pzz, Pxz
        K = Pxz @ inv(Pzz)
        P_new = S_P S_P^T - K Pzz K^T
        S_P = chol((P_new + P_new^T)/2, lower=True)   ← Landmine 8
    """

    def __init__(
        self,
        n: int = ec.N_FREE_STATES,
        alpha: float = ec.UKF_ALPHA,
        beta: float = ec.UKF_BETA,
        kappa: float = ec.UKF_KAPPA,
        q_floor_scale: float = None,
    ):
        if q_floor_scale is None:
            q_floor_scale = ec.ACTIVE.get("q_floor_scale", 1e-8)

        self.n = n
        self.alpha = alpha
        self.beta = beta
        self.kappa = kappa

        # Sigma-point lambda and weights
        lam = alpha ** 2 * (n + kappa) - n
        self.lam = lam

        # Mean weights
        self.Wm = np.full(2 * n + 1, 1.0 / (2.0 * (n + lam)))
        self.Wm[0] = lam / (n + lam)

        # Covariance weights
        self.Wc = self.Wm.copy()
        self.Wc[0] = lam / (n + lam) + (1.0 - alpha ** 2 + beta)

        # State: flat start (|V|=1, theta=0)
        self._x = np.zeros(n)
        self._x[0::2] = 1.0

        # Square-root of P (Cholesky factor: S_P S_P^T = P)
        self._S_P = np.eye(n) * 0.1   # initial P = 0.01 * I

        # Process noise floor
        self.Q_floor = np.eye(n) * q_floor_scale

    def _sigma_points(self):
        """Compute 2n+1 sigma points from (x, S_P).

        Returns
        -------
        sigmas : np.ndarray (2n+1, n)
        """
        scale = np.sqrt(self.n + self.lam)
        sigmas = np.empty((2 * self.n + 1, self.n))
        sigmas[0] = self._x
        for i in range(self.n):
            sigmas[i + 1] = self._x + scale * self._S_P[:, i]
            sigmas[self.n + i + 1] = self._x - scale * self._S_P[:, i]
        return sigmas

    def _safe_cholesky(self, M: np.ndarray, jitter: float = 1e-8) -> np.ndarray:
        """Cholesky with retry on jitter if M is near-singular.

        Always symmetrize before factoring (Landmine 8).
        """
        M_sym = (M + M.T) / 2.0
        try:
            return cholesky(M_sym, lower=True)
        except Exception:
            # Add small jitter and retry once
            M_jit = M_sym + np.eye(M_sym.shape[0]) * jitter
            return cholesky(M_jit, lower=True)

    def predict(self, delta_p_fcst: np.ndarray, S: np.ndarray, Cov_eps: np.ndarray) -> None:
        """FASE predict: propagate mean and Cholesky factor.

        Parameters
        ----------
        delta_p_fcst : (n_inj,)
        S            : (n, n_inj)
        Cov_eps      : (n_inj, n_inj)
        """
        self._x = self._x + S @ delta_p_fcst
        Q = S @ Cov_eps @ S.T + self.Q_floor
        P_pred = self._S_P @ self._S_P.T + Q
        self._S_P = self._safe_cholesky(P_pred)

    def update(self, z: np.ndarray, R: np.ndarray, h_fn, H_fn=None):
        """UKF update — no Jacobian needed.

        Parameters
        ----------
        z    : (m,)  measurement vector
        R    : (m,m)  measurement noise covariance
        h_fn : callable  h_fn(x) -> z_pred  (only h_fn used; H_fn ignored)
        H_fn : callable or None  (ignored; kept for API parity with EKF)

        Returns
        -------
        y   : np.ndarray (m,)  innovation z - z_hat
        Pzz : np.ndarray (m,m)  innovation covariance
        """
        sigmas = self._sigma_points()                       # (2n+1, n)
        Z = np.array([h_fn(s) for s in sigmas])            # (2n+1, m)

        # Predicted measurement mean
        z_hat = Z.T @ self.Wm                              # (m,)

        # Innovation and cross-covariance
        n2p1 = 2 * self.n + 1
        Pzz = R.copy()
        Pxz = np.zeros((self.n, len(z)))
        for i in range(n2p1):
            dz = Z[i] - z_hat
            dx = sigmas[i] - self._x
            Pzz += self.Wc[i] * np.outer(dz, dz)
            Pxz += self.Wc[i] * np.outer(dx, dz)

        K = Pxz @ np.linalg.inv(Pzz)
        y = z - z_hat
        self._x = self._x + K @ y

        P_old = self._S_P @ self._S_P.T
        P_new = P_old - K @ Pzz @ K.T
        self._S_P = self._safe_cholesky(P_new)

        return y, Pzz

    @property
    def x(self) -> np.ndarray:
        return self._x

    @property
    def P(self) -> np.ndarray:
        """Reconstruct P from Cholesky factor: P = S_P @ S_P^T."""
        return self._S_P @ self._S_P.T
