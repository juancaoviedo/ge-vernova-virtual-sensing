"""
fase_predict.py
---------------
FASE predict step for the IEEE 33-bus System 2 state estimator.

Provides:
  - FASEPredictor : forecast-driven sensitivity predictor with Q assembly

**Oracle separation (D-06):**
  This module reads NO external data — it NEVER imports, reads, or references the
  'state' bucket, the 'fault_event' bucket, the profiles DataFrame, or any oracle data.
  Forecast Δp and Cov(ε) arrive from the caller (the external forecast stream,
  wired in 10-09/10-10), not from any internal read.
  Verified by grep: zero executable references to oracle bucket names or oracle read helpers.

Predict recipe (D-10, supersedes D-05):
  External forecast publisher (10-09) supplies, per step k:
    delta_p  : Δp = [ΔP₁..ΔP₃₂, ΔQ₁..ΔQ₃₂]  shape (64,)  per-bus injection change
    cov_eps  : Cov(ε)  shape (64,64)  forecast error covariance

  FASEPredictor.predict(x_prev, S, delta_p, cov_eps) computes:
    x⁻ = x_prev + S @ delta_p          (FASE mean propagation)
    Q  = S @ cov_eps @ S.T + Q_floor   (FASE process noise)

Persistence foil (D-04):
  mode == "persistence": delta_p := 0 → x⁻ = x_prev; Q = Q_floor * RW_SCALE.
  Both FASE and persistence sit behind the same .predict() interface.

Determinism guarantee:
  All randomness (if any) passes through the single `rng` object
  (np.random.Generator) passed at construction. NO bare np.random, NO
  random.seed(), NO hash(), NO wall-clock reads. The rng parameter is retained
  for API parity and future use; it is NOT used internally to fabricate a
  forecast (the forecast Δp arrives externally from the forecast publisher).

No I/O: no MQTT, no InfluxDB reads, no profiles DataFrame reads.
Dependencies: numpy
"""

import numpy as np


# ---------------------------------------------------------------------------
# Random-walk scale factor for persistence foil
# ---------------------------------------------------------------------------
_RW_SCALE: float = 100.0  # persistence foil Q = Q_floor * RW_SCALE (honestly wider)


class FASEPredictor:
    """Forecast-driven FASE predict step + persistence foil.

    Both modes implement the same interface:
        predict(x_prev, S, delta_p, cov_eps) -> (x_minus, Q)

    Parameters
    ----------
    cfg      : dict  must contain:
                 q_floor_scale  (float, default 1e-8)
                 predict_mode   (str, "fase" | "persistence")
    rng      : np.random.Generator  single seeded instance (default_rng(seed)); NEVER create here.
                 Retained for API parity / future use; not currently used internally.
    n_bus    : int  number of estimated buses (32 for IEEE 33-bus D-11: buses 1..32)

    Oracle separation:
        This class NEVER reads 'state', 'fault_event', the profiles DataFrame, or any oracle bucket.
        Forecast Δp and Cov(ε) arrive from the caller (external forecast publisher).
    """

    def __init__(self, cfg: dict, rng, n_bus: int):
        q_floor_scale: float = float(cfg.get("q_floor_scale", 1e-8))
        self.mode: str = str(cfg.get("predict_mode", "fase"))
        self.rng = rng           # retained for API parity; not used internally
        self.n_bus = n_bus
        self.n_state = n_bus * 2  # interleaved polar: |V|_1, theta_1, ..., |V|_32, theta_32

        # Process noise floor (diagonal, shared between fase and persistence)
        self.q_floor = np.eye(self.n_state) * q_floor_scale

    def predict(self, x_prev: np.ndarray, S: np.ndarray,
                delta_p: np.ndarray, cov_eps: np.ndarray):
        """Return (x_hat_minus, Q) for the current step.

        Parameters
        ----------
        x_prev   : np.ndarray  shape (n_state,)     x̂_{k-1} (previous posterior estimate)
        S        : np.ndarray  shape (n_state, n_inj)  sensitivity matrix ∂x/∂p
                               from injection_sensitivity(x_prev, Ybus).
                               For this 32-bus model: n_inj = 64; S.shape == (64, 64).
        delta_p  : np.ndarray  shape (n_inj,)  per-bus injection change
                               Δp = [ΔP₁..ΔP₃₂, ΔQ₁..ΔQ₃₂] (stacked, NOT interleaved).
                               Supplied by the external forecast publisher (10-09).
        cov_eps  : np.ndarray  shape (n_inj, n_inj)  forecast error covariance.
                               Supplied by the external forecast publisher (10-09).

        Returns
        -------
        x_minus : np.ndarray  shape (n_state,)   predicted state prior x̂ₖ⁻
        Q       : np.ndarray  shape (n_state, n_state)  process noise covariance

        Dimension guard:
            Asserts delta_p.shape[0] == S.shape[1] and cov_eps.shape == (S.shape[1], S.shape[1]).
            This is the structural guardrail that makes bug #2 (S.cols=26 vs delta_p.len=33)
            impossible — a mismatch raises AssertionError immediately.

        Oracle separation:
            Reads ONLY the arguments supplied by the caller.
            NEVER reads 'state', 'fault_event', the profiles DataFrame, or any external source.
        """
        # Dimension consistency guard — the exact check that would have caught bug #2
        n_inj = S.shape[1]
        assert delta_p.shape[0] == n_inj, (
            f"FASEPredictor.predict: dimension mismatch — "
            f"delta_p.shape[0]={delta_p.shape[0]} != S.shape[1]={n_inj}. "
            f"Δp must be in the INJECTION space (n_inj={n_inj}), not in measurement space. "
            f"(Bug #2 guard, D-10)"
        )
        assert cov_eps.shape == (n_inj, n_inj), (
            f"FASEPredictor.predict: cov_eps.shape={cov_eps.shape} != ({n_inj}, {n_inj}). "
            f"cov_eps must be square and match the injection space dimension."
        )

        if self.mode == "persistence":
            return self._predict_persistence(x_prev)
        return self._predict_fase(x_prev, S, delta_p, cov_eps)

    def _predict_persistence(self, x_prev: np.ndarray):
        """Persistence foil (D-04): x_minus = x_prev, Q = Q_floor * RW_SCALE.

        No forecast Δ is applied. The process noise is intentionally wider than
        FASE to represent that the persistence prior is less informative.
        """
        x_minus = x_prev.copy()
        Q = self.q_floor * _RW_SCALE
        return x_minus, Q

    def _predict_fase(self, x_prev: np.ndarray, S: np.ndarray,
                      delta_p: np.ndarray, cov_eps: np.ndarray):
        """FASE primary path (D-10):
            x_minus = x_prev + S @ delta_p
            Q = S @ cov_eps @ S.T + Q_floor

        delta_p and cov_eps are supplied externally by the forecast publisher (10-09).
        This method performs ONLY the sensitivity propagation — no forecast generation.
        """
        # FASE mean propagation
        x_minus = x_prev + S @ delta_p

        # FASE process noise
        Q = S @ cov_eps @ S.T + self.q_floor

        return x_minus, Q
