"""
fase_predict.py
---------------
FASE predict step for the IEEE 33-bus System 2 state estimator.

Provides:
  - FASEPredictor : profile-as-noisy-forecast predictor with AR(1) seeded error + Q assembly

**Oracle separation (D-06):**
  This module reads ONLY the injected `prof_df` (profiles DataFrame) — it NEVER imports,
  reads, or references the 'state' bucket, the 'fault_event' bucket, or any oracle data.
  Verified by grep: zero references to oracle bucket names or oracle read helpers.

Forecast recipe (D-05):
  1. Read nodal load injection at step k from prof_df (p_sched).
  2. Degrade with a seeded AR(1) forecast-error process ε (σ ≈ 5% of scheduled load, ρ ≈ 0.3).
  3. Compute Δp = p_fcst(k) - p_fcst(k-1)  (zeros on first step).
  4. x̂ₖ⁻ = x̂ₖ₋₁ + S·Δp_fcst
  5. Qₖ  = S·Cov(ε)·Sᵀ + Q_floor

Persistence foil (D-04):
  mode == "persistence": x̂ₖ⁻ = x̂ₖ₋₁ (no forecast Δ), Q = Q_floor * RW_SCALE.
  Both FASE and persistence sit behind the same .predict() interface.

Determinism guarantee:
  All randomness passes through the single `rng` object (np.random.Generator) passed at
  construction. NO bare np.random, NO random.seed(), NO hash(), NO wall-clock reads.
  Two FASEPredictor instances built with the same seed/cfg produce identical sequences.

AR(1) process (mirror of measure.py InstrumentState.ar1_term):
  white   = rng.normal(0, sigma_frac * sqrt(1 - rho^2), n_bus)
  ar1_prev = rho * ar1_prev + white      ← stationary, marginal std ≈ sigma_frac
  p_fcst  = p_sched * (1 + ar1_prev)    ← per-bus degraded forecast

No I/O: no MQTT, no InfluxDB reads. The caller (estimate.py) provides the pre-fetched prof_df.

Dependencies: numpy, pandas
"""

import numpy as np


# ---------------------------------------------------------------------------
# Random-walk scale factor for persistence foil
# ---------------------------------------------------------------------------
_RW_SCALE: float = 100.0  # persistence foil Q = Q_floor * RW_SCALE (honestly wider)


class FASEPredictor:
    """Profile-as-noisy-forecast predict step + persistence foil.

    Both modes implement the same interface:
        predict(step_k, x_prev, S) -> (x_minus, Q)

    Parameters
    ----------
    prof_df  : pd.DataFrame  shape (n_steps, *)  must have column 'load_pu'
    cfg      : dict  must contain:
                 forecast_sigma_frac (float, default 0.05)
                 forecast_ar1_rho    (float, default 0.3)
                 q_floor_scale       (float, default 1e-8)
                 predict_mode        (str, "fase" | "persistence")
    rng      : np.random.Generator  single seeded instance (default_rng(seed)); NEVER create here
    n_bus    : int  number of distribution buses (state dim = n_bus * 2)

    Oracle separation:
        This class NEVER reads 'state', 'fault_event', or any oracle bucket.
        Only prof_df (profiles) is read, and only at predict() time (not I/O).
    """

    def __init__(self, prof_df, cfg: dict, rng, n_bus: int):
        self.prof_df = prof_df
        self.sigma_frac: float = float(cfg.get("forecast_sigma_frac", 0.05))
        self.rho: float = float(cfg.get("forecast_ar1_rho", 0.3))
        q_floor_scale: float = float(cfg.get("q_floor_scale", 1e-8))
        self.mode: str = str(cfg.get("predict_mode", "fase"))
        self.rng = rng
        self.n_bus = n_bus
        self.n_state = n_bus * 2  # interleaved polar: |V|_0, theta_0, ..., |V|_{n-1}, theta_{n-1}

        # Process noise floor (diagonal, shared between fase and persistence)
        self.q_floor = np.eye(self.n_state) * q_floor_scale

        # AR(1) persistent state: per-bus
        self._ar1_prev = np.zeros(n_bus)

        # Previous forecast value (for computing Δp = p_fcst(k) - p_fcst(k-1))
        self._p_fcst_prev: np.ndarray | None = None

    def predict(self, step_k: int, x_prev: np.ndarray, S: np.ndarray):
        """Return (x_hat_minus, Q) for step k.

        Parameters
        ----------
        step_k : int  current step index (0-based, indexes into prof_df)
        x_prev : np.ndarray  shape (n_state,)  x̂_{k-1} (previous posterior estimate)
        S      : np.ndarray  shape (n_state, n_inj)  sensitivity matrix ∂x/∂p

        Returns
        -------
        x_minus : np.ndarray  shape (n_state,)  predicted state prior x̂ₖ⁻
        Q       : np.ndarray  shape (n_state, n_state)  process noise covariance

        Oracle separation:
            Reads ONLY prof_df['load_pu'] at step_k.
            NEVER reads 'state', 'fault_event', or any external oracle source.
        """
        if self.mode == "persistence":
            return self._predict_persistence(x_prev)
        return self._predict_fase(step_k, x_prev, S)

    def _predict_persistence(self, x_prev: np.ndarray):
        """Persistence foil (D-04): x_minus = x_prev, Q = Q_floor * RW_SCALE.

        No forecast Δ is applied. The process noise is intentionally wider than
        FASE to represent that the persistence prior is less informative.
        """
        x_minus = x_prev.copy()
        Q = self.q_floor * _RW_SCALE
        return x_minus, Q

    def _predict_fase(self, step_k: int, x_prev: np.ndarray, S: np.ndarray):
        """FASE primary path (D-05):
            1. Read p_sched from prof_df at step_k.
            2. Apply seeded AR(1) forecast error.
            3. Compute Δp = p_fcst(k) - p_fcst(k-1).
            4. x_minus = x_prev + S @ Δp.
            5. Q = S @ Cov(ε) @ S.T + Q_floor.

        AR(1) process (mirrors measure.py InstrumentState.ar1_term):
            white = rng.normal(0, sigma_frac * sqrt(1 - rho^2), n_bus)
            ar1_prev = rho * ar1_prev + white   (stationary; marginal std ≈ sigma_frac)
            p_fcst = p_sched * (1 + ar1_prev)
        """
        # Read scheduled load at step_k
        p_sched = float(self.prof_df.iloc[step_k]["load_pu"])

        # AR(1) forecast error — mirrors InstrumentState.ar1_term in measure.py
        # white noise scaled so marginal std of the AR(1) process ≈ sigma_frac
        white = self.rng.normal(
            0.0,
            self.sigma_frac * (1.0 - self.rho ** 2) ** 0.5,
            size=self.n_bus,
        )
        self._ar1_prev = self.rho * self._ar1_prev + white

        # Per-bus degraded forecast: p_sched * (1 + AR(1) error)
        p_fcst = p_sched * (1.0 + self._ar1_prev)

        # Δp = p_fcst(k) - p_fcst(k-1); zero-vector on the first step
        if self._p_fcst_prev is None:
            delta_p = np.zeros(self.n_bus)
        else:
            delta_p = p_fcst - self._p_fcst_prev
        self._p_fcst_prev = p_fcst

        # x_minus = x_prev + S @ delta_p  (FASE mean propagation)
        x_minus = x_prev + S @ delta_p

        # Q = S @ Cov(ε) @ S.T + Q_floor
        # Cov(ε) = diag((sigma_frac * |p_fcst|)^2)  (per-bus forecast error variance)
        cov_eps = np.diag((self.sigma_frac * np.abs(p_fcst)) ** 2)
        Q = S @ cov_eps @ S.T + self.q_floor

        return x_minus, Q
