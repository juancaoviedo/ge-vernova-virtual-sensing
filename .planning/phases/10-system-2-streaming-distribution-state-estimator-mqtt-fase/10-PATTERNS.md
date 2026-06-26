# Phase 10: System 2 — Streaming Distribution State Estimator (MQTT + FASE) - Pattern Map

**Mapped:** 2026-06-26
**Files analyzed:** 13 new/modified files
**Analogs found:** 11 / 13 (2 net-new with no codebase analog)

---

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `src/ieee33/publish.py` | runner/service | CRUD + event-driven (InfluxDB→MQTT) | `src/ieee33/measure.py` | role-match |
| `src/ieee33/estimate_config.py` | config | — | `src/ieee33/measure_config.py` | exact |
| `src/ieee33/estimate.py` | runner/service | event-driven (MQTT subscribe + write) | `src/ieee33/measure.py` | role-match |
| `src/ieee33/ac_model.py` | utility | transform (Ybus + h(x) + H) | `src/ieee33/network.py` | partial |
| `src/ieee33/estimators.py` | service | transform (WLS/EKF/UKF predict/update) | `.planning/phases/02-distribution-virtual-sensing/demo/dc_powerflow_baddata_demo.py` | partial |
| `src/ieee33/fase_predict.py` | service | transform (FASE predict + forecast) | `src/ieee33/measure.py` (AR(1) + InfluxDB read pattern) | partial |
| `src/ieee33/score.py` | utility/runner | CRUD (read oracle + estimates + report) | `src/ieee33/measure.py` (runner skeleton) | role-match |
| `src/ieee33/config.py` | config | — | `src/ieee33/config.py` (additive) | exact (additive) |
| `src/ieee33/influx.py` | utility | CRUD | `src/ieee33/influx.py` (additive helpers) | exact (additive) |
| `docker-compose.yml` | config | — | `system1-measurement-source/docker-compose.yml` | exact (additive) |
| `mosquitto/config/mosquitto.conf` | config | — | (no analog — first MQTT config in repo) | none |
| `grafana/provisioning/dashboards/ieee33-est-day.json` | config/dashboard | — | `grafana/provisioning/dashboards/ieee33-meas-day.json` | exact |
| `grafana/provisioning/dashboards/ieee33-est-fault.json` | config/dashboard | — | `grafana/provisioning/dashboards/ieee33-meas-fault.json` | exact |
| `pyproject.toml` | config | — | `system1-measurement-source/pyproject.toml` (additive) | exact (additive) |

---

## Pattern Assignments

### `src/ieee33/estimate_config.py` (config, pure constants)

**Analog:** `src/ieee33/measure_config.py`

This file is the highest-priority pattern copy: `measure_config.py` is the complete template.

**Module docstring pattern** (lines 1-16):
```python
"""
estimate_config.py
------------------
All estimator knobs for the IEEE 33-bus System 2 state estimator.
This module is **pure constants — no I/O side effects** (no load_dotenv, no file reads,
no datetime.now, no np.random). Downstream modules (estimate.py, score.py) import from here;
no constant is duplicated elsewhere.

Forward contract: every Plan runner imports ACTIVE and the relevant constant tables
from this single source of truth. The ACTIVE block is the PRIMARY switch: edit it
to change experiment without touching runner code.

Dependencies: stdlib only (no third-party imports)
Run:          imported — not executed directly
"""
```

**ACTIVE block pattern** (lines 266-274 of `measure_config.py`):
```python
# ---------------------------------------------------------------------------
# ACTIVE BLOCK — edit this to switch experiments without touching runner code
# ---------------------------------------------------------------------------
ACTIVE: dict = {
    "scenario":      "realistic_sparse",   # "well_observed" | "realistic_sparse"
    "source":        "day",                # "day" (96-step) | "fault" (40-step)
    "estimator":     "ukf",               # "wls" | "ekf" | "ukf"
    "seed":          42,                   # RNG seed for forecast-error determinism
    "acceleration":  1.0,                  # wall-clock playback compression (publish only)
    # FASE predict knobs (D-07):
    "forecast_sigma_frac": 0.05,           # per-bus σ ≈ 5% of scheduled load
    "forecast_ar1_rho":    0.3,            # AR(1) correlation coefficient ρ
    "q_floor_scale":       1e-8,           # Q_floor = q_floor_scale * I
    "predict_mode":        "fase",         # "fase" | "persistence" (A/B foil)
}
```

**Constants table pattern** — mirror `CLASS_SIGMA` / `CADENCE` / `SCENARIOS` / `MEASUREMENTS_BUCKET` structure from lines 33-257 of `measure_config.py`. For `estimate_config.py` the equivalent tables are:
- `ESTIMATES_BUCKET = "estimates"` — the output bucket name
- `UKF_ALPHA`, `UKF_BETA`, `UKF_KAPPA` — sigma-point params (α=1e-3, β=2.0, κ=0.0)
- `GAUSS_NEWTON_MAX_ITER`, `GAUSS_NEWTON_TOL` — WLS iteration knobs
- `NEES_CONFIDENCE` — 0.95 (for chi2 band computation in score.py)

---

### `src/ieee33/publish.py` (runner, InfluxDB→MQTT)

**Analog:** `src/ieee33/measure.py` (runner skeleton + CLI pattern)

**Module docstring pattern** (mirror `measure.py` lines 1-28):
```python
"""
publish.py
----------
Replay publisher for the IEEE 33-bus System 2 observability study.
Reads measurements + event points for a chosen (scenario, source) from
InfluxDB in deterministic order (sorted by timestamp, class, location),
and publishes each as an MQTT message to the Mosquitto broker.

Also publishes the network config to the RETAINED versioned topic
ieee33/netmodel/current before any measurement messages.

Determinism note: Flux queries sorted by (_time, class, location); same
config produces identical publish order.  Acceleration factor compresses
wall-clock; no wall-clock reads in deterministic paths.

Run:  uv run publish [--scenario ...] [--source ...] [--seed ...] [--acceleration ...]
"""
```

**CLI argument parsing pattern** (mirror `measure.py` lines 200-260 exactly):
```python
def _parse_args():
    p = argparse.ArgumentParser(
        description="IEEE 33-bus replay publisher — reads measurements, emits MQTT."
    )
    p.add_argument("--scenario", choices=["well_observed", "realistic_sparse"], default=None)
    p.add_argument("--source",   choices=["day", "fault"], default=None)
    p.add_argument("--seed",     type=int, default=None)
    p.add_argument("--acceleration", type=float, default=None)
    return p.parse_args()

def _merge_cfg(args) -> dict:
    cfg = dict(ec.ACTIVE)          # ec = estimate_config (mirrors mc.ACTIVE in measure.py)
    for key in ("scenario", "source", "seed", "acceleration"):
        val = getattr(args, key, None)
        if val is not None:
            cfg[key] = val
    return cfg
```

**InfluxDB connection + bucket pattern** (mirror `measure.py` lines 650-654):
```python
client = influx.get_client()
influx.wait_for_influx()
# publish.py reads from measurements; no ensure_bucket needed (bucket pre-exists)
```

**Flux read pattern for measurements** (extend `influx.read_fault_event` pivot style from `influx.py` lines 709-746):
```python
flux = (
    f'from(bucket: "measurements")\n'
    f'  |> range(start: {start}, stop: {stop})\n'
    f'  |> filter(fn: (r) => r._measurement == "meas")\n'
    f'  |> filter(fn: (r) => r.scenario == "{scenario}")\n'
    f'  |> filter(fn: (r) => r.experiment == "{experiment}")\n'
    f'  |> pivot(rowKey: ["_time", "class", "quantity", "location",\n'
    f'            "scenario", "experiment"], '
    f'     columnKey: ["_field"], valueColumn: "_value")\n'
    f'  |> sort(columns: ["_time", "class", "location"])'
)
```
Note: for fault source, add `"phase"` to `rowKey` (it is a TAG — mirror `read_fault_bus` Pitfall note in `influx.py` line 650-657).

**paho-mqtt publish pattern** (from RESEARCH.md Pattern 1, verified):
```python
import paho.mqtt.client as mqtt
import json, time

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
client.connect("127.0.0.1", 1883, keepalive=60)
client.loop_start()

# 1. Publish retained netmodel/current FIRST (before any meas)
config_payload = json.dumps({
    "config_version": 0,
    "in_service_lines": list(range(32)),
    "tie_closed": False,
    "tie_id": -1,
    "dead_buses": [],
    "phase": "steady_state",
    "timestamp": ts_iso,
})
client.publish("ieee33/netmodel/current", config_payload, qos=1, retain=True)

# 2. Publish meas in FIXED ORDER; sleep between snapshots (not within)
for ts, cls, loc, payload_dict in sorted_meas:
    topic = f"ieee33/{experiment}/{scenario}/meas/{cls}/{loc}"
    client.publish(topic, json.dumps(payload_dict), qos=1, retain=False)
# sleep cfg["step_duration_s"] / cfg["acceleration"] between snapshot boundaries

client.loop_stop()
client.disconnect()
```

**Console table pattern** (mirror `measure.py` lines 711-715 and `sim.py` lines 174-177):
```python
print(f"\n{'Step':>4}  {'UTC Time':<20}  {'Msgs':>5}  {'Config':>8}")
print("-" * 62)
# per step:
print(f"{step_idx:>4}  {str(ts)[:19]:<20}  {n_msgs:>5}  v{config_version:>6}")
```

**Fail-loud gate** (copy `measure.py` lines 896-902 verbatim):
```python
if issues:
    print("--- PUBLISH VALIDATION FAILED ---", file=sys.stderr)
    for issue in issues:
        print(f"  {issue}", file=sys.stderr)
    client.close()
    sys.exit(1)
```

---

### `src/ieee33/estimate.py` (runner, MQTT subscribe + estimate + write)

**Analog:** `src/ieee33/measure.py` (runner structure) + RESEARCH.md Pattern 2 (paho subscribe)

**Module docstring pattern** (mirror `measure.py` lines 1-28):
```python
"""
estimate.py
-----------
System 2 streaming AC state estimator for the IEEE 33-bus observability study.
Subscribes to MQTT measurements and the retained netmodel/current topology,
assembles per-snapshot z vectors, and drives the selected estimator (wls|ekf|ukf).
Writes (x_hat, P, trace_P) to the 'estimates' InfluxDB bucket.

ORACLE SEPARATION: this module NEVER reads the 'state' or 'fault_event' buckets.
Only measurements (via MQTT) + netmodel/current (via MQTT) + profiles (InfluxDB) are read.
Grep-checkable: grep -r 'state.*bucket\|fault_event' src/ieee33/estimate.py → zero results.

Run:  uv run estimate [--scenario ...] [--source ...] [--estimator wls|ekf|ukf] [--seed ...]
"""
```

**CLI args pattern** (mirror `measure.py` `_parse_args` / `_merge_cfg`):
```python
def _parse_args():
    p = argparse.ArgumentParser(description="IEEE 33-bus AC state estimator runner.")
    p.add_argument("--scenario",  choices=["well_observed", "realistic_sparse"], default=None)
    p.add_argument("--source",    choices=["day", "fault"], default=None)
    p.add_argument("--estimator", choices=["wls", "ekf", "ukf"], default=None)
    p.add_argument("--seed",      type=int, default=None)
    p.add_argument("--acceleration", type=float, default=None)
    return p.parse_args()
```

**InfluxDB setup** (mirror `measure.py` lines 650-654):
```python
client = influx.get_client()
influx.wait_for_influx()
influx.ensure_bucket(client, ec.ESTIMATES_BUCKET)   # "estimates"
write_api = client.write_api(write_options=SYNCHRONOUS)
```

**paho subscribe pattern** (RESEARCH.md Pattern 2, verified):
```python
class MQTTSnapshotAssembler:
    def __init__(self):
        self._current_netmodel = None
        self._config_version = -1
        self._snapshot_buffer = {}
        self._lock = threading.Lock()

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe("ieee33/netmodel/current", qos=1)
        # Gate: subscribe to meas topics AFTER netmodel received (Pitfall 4)

    def on_message(self, client, userdata, msg):
        payload = json.loads(msg.payload.decode())
        if msg.topic == "ieee33/netmodel/current":
            version = payload["config_version"]
            if version != self._config_version:
                self._config_version = version
                self._current_netmodel = payload
                # trigger Ybus rebuild in ac_model
        else:
            ts = payload["timestamp"]
            with self._lock:
                self._snapshot_buffer.setdefault(ts, {})
                self._snapshot_buffer[ts][(payload["class"], payload["location"])] = payload

mqtt_client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
mqtt_client.on_connect = assembler.on_connect
mqtt_client.on_message = assembler.on_message
mqtt_client.connect("127.0.0.1", 1883, keepalive=60)
mqtt_client.loop_start()
# ... main loop ...
mqtt_client.loop_stop()
mqtt_client.disconnect()
```

**Seeded RNG** (mirror `measure.py` line 687):
```python
rng = np.random.default_rng(cfg["seed"])   # single instance, before any loop
```

**Deterministic per-bus seed for forecast error** (mirror `measure.py` `_instrument_bias` lines 89-115):
```python
import hashlib

def _forecast_seed(bus_id: int, seed: int) -> int:
    """Deterministic per-bus forecast-error seed using sha256 (mirror of _instrument_bias)."""
    digest = hashlib.sha256(f"forecast_err|bus{bus_id}|{seed}".encode()).digest()
    return int.from_bytes(digest[:4], "big")
```

**Console table** (mirror `measure.py` lines 711-714 / `sim.py` lines 174-177):
```python
print(f"\n{'Step':>4}  {'UTC Time':<20}  {'Est':>6}  {'trP':>10}  {'RMSE':>8}")
print("-" * 62)
```

**Fail-loud gate** (copy `measure.py` lines 896-902 verbatim):
```python
if issues:
    print("--- ESTIMATE VALIDATION FAILED ---", file=sys.stderr)
    for issue in issues:
        print(f"  {issue}", file=sys.stderr)
    sys.exit(1)
```

---

### `src/ieee33/ac_model.py` (utility, Ybus builder + h(x) + H)

**Analog:** `src/ieee33/network.py` (static net params) + RESEARCH.md Pattern 3 + Pattern 4

**Ybus hand-build pattern** (RESEARCH.md Pattern 3, verified to < 4e-14):
```python
import numpy as np
from pandapower.pd2ppc import _pd2ppc   # CRITICAL: underscore, returns 2-tuple (Pitfall 2)
from pandapower.pypower.makeYbus import makeYbus

def extract_static_line_params(net) -> dict:
    """Extract per-line static impedance params from build_enhanced_33bus() net.
    Returns {line_idx: {from_bus, to_bus, r_total_ohm, x_total_ohm, b_total_pu}}.
    Call once at startup; pass to build_ybus_from_topology().
    """
    ppc, ppci = _pd2ppc(net)             # CRITICAL: _pd2ppc not pd2ppc (Pitfall 2)
    base_z_ohm = (net.bus["vn_kv"].iloc[0]**2 / ppci["baseMVA"]) * 1000  # base Z in ohms
    params = {}
    for idx in net.line.index:
        row = net.line.loc[idx]
        length_km = float(row["length_km"])
        params[idx] = {
            "from_bus": int(row["from_bus"]),
            "to_bus":   int(row["to_bus"]),
            "r_total_ohm": float(row["r_ohm_per_km"]) * length_km,
            "x_total_ohm": float(row["x_ohm_per_km"]) * length_km,
            "b_total_pu":  0.0,   # case33bw: no shunt capacitance on distribution lines
        }
    return params, base_z_ohm, ppci   # ppci kept for trafo fixed contribution + reference Ybus

def build_ybus_from_topology(static_line_params, in_service_line_ids, n_bus, base_z_ohm):
    """Rebuild Ybus from streamed in-service-line set. VERIFIED to < 4e-14 vs ppci Ybus."""
    Y = np.zeros((n_bus, n_bus), dtype=complex)
    for idx in in_service_line_ids:
        p = static_line_params[idx]
        i, j = p["from_bus"], p["to_bus"]
        z_pu = (p["r_total_ohm"] + 1j * p["x_total_ohm"]) / base_z_ohm
        y_series = 1.0 / z_pu
        b_shunt  = p.get("b_total_pu", 0.0)
        Y[i, j] -= y_series;  Y[j, i] -= y_series
        Y[i, i] += y_series + 0.5j * b_shunt
        Y[j, j] += y_series + 0.5j * b_shunt
    # Add trafo fixed contribution (precomputed from ppci at startup)
    # Y += Y_trafo_fixed
    return Y

# Verification gate (SPEC R3 acceptance):
# Ybus_ref = makeYbus(ppci["baseMVA"], ppci["bus"], ppci["branch"])
# assert np.max(np.abs(Y - Ybus_ref)) < 1e-9, "Ybus mismatch > 1e-9"
```

**CRITICAL — 34-bus landmine** (RESEARCH.md Pitfall 1):
- `build_enhanced_33bus()` creates a new HV bus at pandapower index 33 (moves ext_grid there)
- `_pd2ppc` returns a **34×34** Ybus
- State vector: `x = [|V|₀,θ₀, |V|₁,θ₁, ..., |V|₃₂,θ₃₂]` — 66 entries for buses 0..32
- Fixed: θ₃₃ = 0 (slack reference), |V|₃₃ known → **64 free states**
- The trafo (HV bus 33 → LV bus 0) contributes to Y[0,33], Y[33,0], Y[0,0], Y[33,33] — must be included as a fixed addend

**h(x) measurement function pattern** (RESEARCH.md Pattern 4):
```python
def h_func(x, Ybus, meas_list):
    """AC measurement function. x = [|V|₀,θ₀, |V|₁,θ₁, ..., |V|₃₂,θ₃₂] (64 states).
    meas_list: list of (cls, quantity, bus_idx) tuples in FIXED order.
    Returns z_pred vector aligned with meas_list.
    """
    n_bus_est = len(x) // 2   # 32 distribution buses (0..32 minus slack bus33)
    V = x[0::2]   # |V| at each bus
    T = x[1::2]   # θ at each bus (radians)
    G = Ybus.real;  B = Ybus.imag
    rows = []
    for cls, qty, bus_i in meas_list:
        if cls in ("scada", "pmu") and qty == "vm_pu":
            rows.append(V[bus_i])
        elif cls == "pmu" and qty == "va_degree":
            rows.append(T[bus_i] * 180.0 / np.pi)
        elif qty in ("p_inj_mw", "p_mw"):
            # P_i = |V_i| Σ_k |V_k| (G_ik cos(θ_i-θ_k) + B_ik sin(θ_i-θ_k))
            Vi = V[bus_i]
            P_i = Vi * sum(
                V[k] * (G[bus_i, k] * np.cos(T[bus_i]-T[k]) + B[bus_i, k] * np.sin(T[bus_i]-T[k]))
                for k in range(n_bus_est)
            )
            rows.append(P_i)
        # ... Q_inj similarly ...
    return np.array(rows)
```

**Finite-difference Jacobian verification** (RESEARCH.md Pattern 4):
```python
def verify_jacobian(h_fn, H_fn, x, tol=1e-5):
    eps = 1e-6
    n = len(x)
    H_analytic = H_fn(x)
    H_fd = np.zeros_like(H_analytic)
    for j in range(n):
        xf = x.copy(); xf[j] += eps
        xb = x.copy(); xb[j] -= eps
        H_fd[:, j] = (h_fn(xf) - h_fn(xb)) / (2 * eps)
    assert np.max(np.abs(H_analytic - H_fd)) < tol, \
        f"Jacobian FD check failed: max error = {np.max(np.abs(H_analytic - H_fd)):.2e}"
```

---

### `src/ieee33/estimators.py` (service, WLS + EKF + UKF behind one interface)

**Analog:** `.planning/phases/02-distribution-virtual-sensing/demo/dc_powerflow_baddata_demo.py` (WLS/chi2/LNR) + RESEARCH.md Patterns 5-7

**AC-WLS pattern** (lifted from `dc_powerflow_baddata_demo.py` `wls_solve` line 77-83):
```python
from scipy.stats import chi2 as chi2_dist
import numpy as np

def wls_gauss_newton(h_fn, H_fn, z, W, x0, max_iter=20, tol=1e-6):
    """AC WLS Gauss-Newton — AC lift of dc_powerflow_baddata_demo.wls_solve."""
    x = x0.copy()
    for _ in range(max_iter):
        r = z - h_fn(x)
        H = H_fn(x)
        G = H.T @ W @ H
        if np.linalg.matrix_rank(G) < G.shape[0]:
            raise RankDeficientError(
                "G = H^T W H is rank-deficient (system under-observable). "
                "Add pseudo measurements to achieve redundancy > 1.0."
            )
        dx = np.linalg.solve(G, H.T @ W @ r)
        x = x + dx
        if np.linalg.norm(dx) < tol:
            break
    return x, G

def chi2_bad_data(r, W, G, H, df, confidence=0.95):
    """AC bad-data detection — lifted from dc_powerflow_baddata_demo.py lines 86-98."""
    J = r @ W @ r
    threshold = chi2_dist.ppf(confidence, df)
    bad = bool(J > threshold)
    # LNR identification:
    Omega = np.diag(1.0 / np.diag(W)) - H @ np.linalg.inv(G) @ H.T
    # CAUTION: Omega diagonal can go negative at high leverage — clamp to abs
    rN = np.abs(r) / np.sqrt(np.abs(np.diag(Omega)))
    return J, threshold, bad, rN
```

**Estimator abstract interface** (from RESEARCH.md Pattern 6):
```python
from abc import ABC, abstractmethod

class BaseEstimator(ABC):
    @abstractmethod
    def predict(self, delta_p_fcst, S, Cov_eps): ...
    @abstractmethod
    def update(self, z, R, h_fn, H_fn): ...
    @property
    @abstractmethod
    def x(self): ...
    @property
    @abstractmethod
    def P(self): ...
```

**EKF pattern** (RESEARCH.md Pattern 6, Joseph form mandatory):
```python
class EKFEstimator(BaseEstimator):
    def __init__(self, n=64, Q_floor_scale=1e-8):
        self._x = np.ones(n)    # flat start: |V|=1.0, θ=0 (interleaved: x[2i]=|V_i|, x[2i+1]=θ_i)
        self._P = np.eye(n) * 0.01
        self.Q_floor = np.eye(n) * Q_floor_scale

    def predict(self, delta_p_fcst, S, Cov_eps):
        """FASE predict: x⁻ = x + S·Δp;  P⁻ = P + S·Cov(ε)·Sᵀ + Q_floor."""
        self._x = self._x + S @ delta_p_fcst
        Q = S @ Cov_eps @ S.T + self.Q_floor
        self._P = self._P + Q

    def update(self, z, R, h_fn, H_fn):
        H = H_fn(self._x)
        y = z - h_fn(self._x)
        S_inn = H @ self._P @ H.T + R
        K = self._P @ H.T @ np.linalg.solve(S_inn.T, np.eye(len(z))).T
        self._x = self._x + K @ y
        I_KH = np.eye(len(self._x)) - K @ H
        # Joseph form — MANDATORY for numerical stability over 96 steps (RESEARCH Pitfall 4)
        self._P = I_KH @ self._P @ I_KH.T + K @ R @ K.T
        return y, S_inn   # return for NIS computation
```

**sqrt-UKF pattern** (RESEARCH.md Pattern 7):
```python
from scipy.linalg import cholesky

class UKFEstimator(BaseEstimator):
    def __init__(self, n=64, alpha=1e-3, beta=2.0, kappa=0.0, Q_floor_scale=1e-8):
        self.n = n
        lam = alpha**2 * (n + kappa) - n
        self.lam = lam
        self.Wm = np.full(2*n+1, 1.0/(2*(n+lam))); self.Wm[0] = lam/(n+lam)
        self.Wc = self.Wm.copy(); self.Wc[0] += (1 - alpha**2 + beta)
        self._x = np.ones(n)
        self._S_P = np.eye(n) * 0.1   # Cholesky factor of P
        self.Q_floor = np.eye(n) * Q_floor_scale

    def predict(self, delta_p_fcst, S, Cov_eps):
        self._x = self._x + S @ delta_p_fcst
        Q = S @ Cov_eps @ S.T + self.Q_floor
        P_new = self._S_P @ self._S_P.T + Q
        # Symmetrize before cholesky — REQUIRED to avoid LinAlgError (RESEARCH anti-pattern)
        self._S_P = cholesky((P_new + P_new.T) / 2, lower=True)

    def update(self, z, R, h_fn):
        """UKF update — no Jacobian needed (key advantage over EKF for nonlinear h)."""
        scale = np.sqrt(self.n + self.lam)
        sigmas = np.vstack([
            self._x,
            *(self._x + scale * self._S_P[:, i] for i in range(self.n)),
            *(self._x - scale * self._S_P[:, i] for i in range(self.n)),
        ])
        Z = np.array([h_fn(s) for s in sigmas])
        z_hat = Z.T @ self.Wm
        Pzz = sum(self.Wc[i] * np.outer(Z[i]-z_hat, Z[i]-z_hat) for i in range(2*self.n+1)) + R
        Pxz = sum(self.Wc[i] * np.outer(sigmas[i]-self._x, Z[i]-z_hat) for i in range(2*self.n+1))
        K = Pxz @ np.linalg.inv(Pzz)
        y = z - z_hat
        self._x = self._x + K @ y
        P_new = self._S_P @ self._S_P.T - K @ Pzz @ K.T
        self._S_P = cholesky((P_new + P_new.T) / 2, lower=True)
        return y, Pzz
```

**WLSEstimator** wraps `wls_gauss_newton` per snapshot; it has no `predict` step (snapshot WLS solves independently). Its `update` equivalent is one Gauss-Newton solve per snapshot.

---

### `src/ieee33/fase_predict.py` (service, FASE predictor + persistence foil)

**Analog:** `src/ieee33/measure.py` (AR(1) InstrumentState + read_profiles pattern) + `src/ieee33/influx.py` `read_profiles`

**Read profiles at startup pattern** (mirror `measure.py` `_build_day_lookup` lines 267-305, `influx.read_profiles` lines 141-181):
```python
# At startup — read ALL 96 steps once (not per-step for latency)
prof_df = influx.read_profiles(client).sort_values("_time").reset_index(drop=True)
# prof_df has columns: _time, load_pu, solar_pu, wind_pu
```

**AR(1) forecast error pattern** (mirror `measure.py` `InstrumentState` lines 48-86):
```python
class FASEPredictor:
    """Profile-as-noisy-forecast predict + Q for EKF/UKF. Persistence foil behind same interface."""

    def __init__(self, prof_df, cfg, rng, n_bus):
        self.prof_df = prof_df
        self.sigma_frac = cfg["forecast_sigma_frac"]   # default 0.05 (5% of scheduled load)
        self.rho = cfg["forecast_ar1_rho"]             # default 0.3 AR(1) coefficient
        self.q_floor = np.eye(n_bus*2) * cfg["q_floor_scale"]
        self.mode = cfg["predict_mode"]                 # "fase" | "persistence"
        self.rng = rng
        self._ar1_prev = np.zeros(n_bus)               # per-bus AR(1) state
        self._p_fcst_prev = None                       # p_forecast at step k-1

    def predict(self, step_k, x_prev, S):
        """Return (x_hat_minus, Q) for step k.
        S = sensitivity matrix (∂x/∂p, from H injection rows at x_prev).
        """
        if self.mode == "persistence":
            # Random-walk foil: x⁻ = x_{k-1}, Q = Q_rw (large, config-tunable)
            return x_prev.copy(), self.q_floor * 100.0

        # FASE primary path (D-05):
        p_sched = float(self.prof_df.iloc[step_k]["load_pu"])  # scheduled injection
        # AR(1) seeded forecast error per bus (mirrors InstrumentState.ar1_term pattern)
        white = self.rng.normal(0.0, self.sigma_frac * (1 - self.rho**2)**0.5, size=len(self._ar1_prev))
        self._ar1_prev = self.rho * self._ar1_prev + white
        p_fcst = p_sched * (1.0 + self._ar1_prev)   # degraded per-bus forecast

        delta_p = (p_fcst - self._p_fcst_prev) if self._p_fcst_prev is not None else np.zeros_like(p_fcst)
        self._p_fcst_prev = p_fcst

        x_minus = x_prev + S @ delta_p
        Cov_eps = np.diag((self.sigma_frac * np.abs(p_fcst))**2)
        Q = S @ Cov_eps @ S.T + self.q_floor
        return x_minus, Q
```

---

### `src/ieee33/score.py` (runner, oracle scoring)

**Analog:** `src/ieee33/measure.py` (runner skeleton) + RESEARCH.md Pattern 8

**Oracle separation gate** — this module is the SOLE reader of `state`/`fault_event`. All imports must be grep-verified:
```python
# score.py — ONLY file that reads oracle buckets
# grep check: grep -r "state.*bucket\|fault_event" src/ieee33/estimate*.py → zero results
from ieee33 import influx   # reads state via read_state_bus / read_fault_bus
```

**CLI pattern** (mirror `measure.py`):
```python
def _parse_args():
    p = argparse.ArgumentParser(description="IEEE 33-bus state estimator scoring harness.")
    p.add_argument("--scenario",  choices=["well_observed", "realistic_sparse"], default=None)
    p.add_argument("--source",    choices=["day", "fault"], default=None)
    p.add_argument("--estimator", choices=["wls", "ekf", "ukf", "all"], default="all")
    return p.parse_args()
```

**NEES/NIS computation** (RESEARCH.md Pattern 8, `scipy.stats.chi2` confirmed available):
```python
from scipy.stats import chi2

def compute_nees(estimates, oracle_states, n_state=64, confidence=0.95):
    """NEES calibration check — time-averaged NEES vs 95% chi2 band."""
    N = len(estimates)
    nees_vals = [(x_hat - x_true) @ np.linalg.solve(P, (x_hat - x_true))
                 for (x_hat, P), x_true in zip(estimates, oracle_states)]
    nees_avg = np.mean(nees_vals)
    lo = chi2.ppf((1 - confidence)/2, N * n_state) / N
    hi = chi2.ppf((1 + confidence)/2, N * n_state) / N
    return nees_avg, lo, hi, lo <= nees_avg <= hi

def compute_nis_fraction(innovations, S_matrices, confidence=0.95):
    """NIS fraction — fraction of steps with in-band NIS."""
    in_band = 0
    for y, S in zip(innovations, S_matrices):
        m = len(y)
        nis_k = y @ np.linalg.solve(S, y)
        lo = chi2.ppf((1 - confidence)/2, m)
        hi = chi2.ppf((1 + confidence)/2, m)
        in_band += int(lo <= nis_k <= hi)
    return in_band / len(innovations)
```

**Report print pattern** (mirror `measure.py` lines 927-975 footprint report style):
```python
print("\n" + "=" * 62)
print("State Estimator Scoring Report")
print("=" * 62)
print(f"Scenario  : {cfg['scenario']}")
print(f"Source    : {cfg['source']}")
print(f"Estimator : {cfg['estimator']}")
print("---")
print(f"  Voltage RMSE (well_observed, median): {rmse_vm:.4f} pu  "
      f"{'PASS' if rmse_vm < 0.005 else 'FAIL'} (< 0.005 pu)")
print(f"  Angle RMSE  (well_observed, median): {rmse_va:.4f} deg "
      f"{'PASS' if rmse_va < 0.1 else 'FAIL'} (< 0.1 deg)")
print(f"  Dark-node RMSE (realistic_sparse):   {rmse_dark:.4f} pu  "
      f"{'PASS' if rmse_dark < 0.02 else 'FAIL'} (< 0.02 pu)")
print(f"  Dark-node vs baseline:               {dark_vs_base:.3f}  "
      f"{'PASS' if dark_vs_base <= 0.5 else 'FAIL'} (<= 50%)")
print(f"  NEES avg / band [{nees_lo:.2f}, {nees_hi:.2f}]: {nees_avg:.2f}  "
      f"{'PASS' if nees_pass else 'FAIL'}")
print(f"  NIS in-band fraction:                {nis_frac:.3f}  "
      f"{'PASS' if nis_frac >= 0.90 else 'FAIL'} (>= 90%)")
```

---

### `src/ieee33/config.py` (additive — ESTIMATES_BUCKET constant)

**Analog:** `src/ieee33/config.py` (additive only — do NOT modify existing constants)

Add at the end of the InfluxDB section (after line 221 of existing `config.py`):
```python
MEASUREMENTS_BUCKET = "measurements"   # already exists (locked Phase 9)
ESTIMATES_BUCKET    = "estimates"      # NEW Phase 10 — System 2 output bucket
```

---

### `src/ieee33/influx.py` (additive — new read/write helpers)

**Analog:** `src/ieee33/influx.py` (additive — mirror existing helper signatures)

**New `read_measurements` helper** (mirror `read_fault_event` pivot style, lines 709-746):
```python
def read_measurements(client: InfluxDBClient, scenario: str, experiment: str):
    """Read all meas points for (scenario, experiment) from measurements bucket.
    Mirror of read_fault_event pivot pattern. Returns DataFrame sorted by _time, class, location.
    """
    # ... same Flux pivot structure as read_fault_event ...
    # NOTE: for experiment="fault", include "phase" in rowKey (it is a TAG — Pitfall 5)
```

**New `write_estimate_step` helper** (mirror `write_state_step` lines 226-338):
```python
def write_estimate_step(write_api, timestamp, x_hat, P, scenario, experiment, estimator):
    """Write per-bus estimate + trace_P to estimates bucket.
    Schema (RESEARCH.md §estimates bucket Point schema):
    """
    points = []
    n_bus_est = len(x_hat) // 2
    for i in range(n_bus_est):
        vm_pu_est   = float(x_hat[2*i])
        va_deg_est  = float(x_hat[2*i+1] * 180.0 / np.pi)
        sigma_vm    = float(np.sqrt(abs(P[2*i, 2*i])))
        sigma_va    = float(np.sqrt(abs(P[2*i+1, 2*i+1])) * 180.0 / np.pi)
        points.append(
            Point("estimate")
            .tag("bus_id",    str(i))
            .tag("scenario",  scenario)
            .tag("experiment", experiment)
            .tag("estimator", estimator)
            .field("vm_pu_est",     vm_pu_est)
            .field("va_degree_est", va_deg_est)
            .field("sigma_vm",      sigma_vm)
            .field("sigma_va",      sigma_va)
            .time(timestamp)
        )
    points.append(
        Point("estimate_system")
        .tag("scenario",  scenario)
        .tag("experiment", experiment)
        .tag("estimator", estimator)
        .field("trace_P", float(np.trace(P)))
        .time(timestamp)
    )
    write_api.write(bucket=config.ESTIMATES_BUCKET, org=config.INFLUXDB_ORG, record=points)
```

---

### `docker-compose.yml` (additive — mosquitto service)

**Analog:** `system1-measurement-source/docker-compose.yml` (additive only)

**Pattern to copy from existing docker-compose.yml lines 1-42** — add new service additively:
```yaml
  mosquitto:
    image: eclipse-mosquitto:2.0
    ports:
      - "127.0.0.1:1883:1883"    # SECURITY: localhost only, not 0.0.0.0 (mirror influxdb binding)
    volumes:
      - ./mosquitto/config/mosquitto.conf:/mosquitto/config/mosquitto.conf
    restart: unless-stopped
    # No depends_on needed: publish.py and estimate.py wait for broker explicitly
```

Mirror the existing `127.0.0.1` localhost-binding convention (influxdb line 6, grafana line 26). No `healthcheck` block needed for Mosquitto (unlike influxdb which has init mode).

---

### `mosquitto/config/mosquitto.conf` (new file — no codebase analog)

No analog exists. Use the RESEARCH.md verified pattern exactly:
```ini
listener 1883 127.0.0.1
allow_anonymous true
persistence true
persistence_location /mosquitto/data/
log_dest stdout
```
Note: Mosquitto 2.0 requires the explicit `listener` directive (unlike 1.x where `bind_address` was used). `allow_anonymous true` is required alongside `listener` in Mosquitto 2.0 for unauthenticated local dev connections.

---

### `grafana/provisioning/dashboards/ieee33-est-day.json` (new dashboard)

**Analog:** `grafana/provisioning/dashboards/ieee33-meas-day.json`

**Top-level JSON skeleton** (copy lines 1-43 of `ieee33-meas-day.json`, modify `description`):
```json
{
  "__inputs": [],
  "__requires": [
    {"type": "grafana",   "id": "grafana",   "name": "Grafana",   "version": "11.0.0"},
    {"type": "datasource","id": "influxdb",  "name": "InfluxDB",  "version": "1.0.0"},
    {"type": "panel",     "id": "timeseries","name": "Time series","version": ""},
    {"type": "panel",     "id": "stat",      "name": "Stat",      "version": ""},
    {"type": "panel",     "id": "heatmap",   "name": "Heatmap",   "version": ""}
  ],
  "description": "IEEE 33-Bus State Estimates — Day: per-bus vm_pu_est vs true vm_pu overlay, per-bus error heatmap, trace_P (ORACS observability index) timeseries, NEES/NIS calibration panel, dark-node recovery panel.",
  "editable": true,
  "panels": [...],
  "schemaVersion": 38,
  "title": "IEEE33 Estimator Day",
  "uid": "ieee33-est-day"
}
```

**datasource reference pattern** (copy from `ieee33-meas-day.json` line 49-51 — every panel uses this):
```json
"datasource": {
  "type": "influxdb",
  "uid": "ieee33-influxdb"
}
```

**Flux panel query pattern** (mirror the Flux query style used in `ieee33-meas-day.json`):
```
from(bucket: "estimates")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r._measurement == "estimate")
  |> filter(fn: (r) => r.estimator == "${estimator}")
  |> filter(fn: (r) => r.scenario  == "${scenario}")
  |> filter(fn: (r) => r._field == "vm_pu_est")
  |> pivot(rowKey: ["_time", "bus_id"], columnKey: ["_field"], valueColumn: "_value")
```

**Panel gridPos pattern** (mirror `ieee33-meas-day.json` line 77 `{ "h": 9, "w": 12, "x": 0, "y": 0 }`): 2×2 grid of 12×9 panels.

`ieee33-est-fault.json` mirrors the same structure as `ieee33-meas-fault.json` (which adds phase-region annotation panels).

---

### `pyproject.toml` (additive — 3 new scripts + paho-mqtt already added)

**Analog:** `system1-measurement-source/pyproject.toml`

`paho-mqtt>=2.1.0` is **already present** in `pyproject.toml` line 14 (confirmed by file read). Add only the three new `[project.scripts]` entries:

```toml
[project.scripts]
ingest    = "ieee33.ingest:main"
sim       = "ieee33.sim:main"
validate  = "ieee33.validate:main"
fault-sim = "ieee33.fault_sim:main"
measure   = "ieee33.measure:main"
publish   = "ieee33.publish:main"    # NEW Phase 10
estimate  = "ieee33.estimate:main"   # NEW Phase 10
score     = "ieee33.score:main"      # NEW Phase 10
```

---

## Shared Patterns

### Seeded Deterministic RNG
**Source:** `src/ieee33/measure.py` line 687
**Apply to:** `publish.py`, `estimate.py`, `fase_predict.py`, `score.py`
```python
rng = np.random.default_rng(cfg["seed"])   # single instance, before any loop
# NEVER use: np.random.seed(), random.seed(), np.random.randn() (legacy API)
```

### Deterministic Per-Entity Seed Derivation
**Source:** `src/ieee33/measure.py` lines 89-115 (`_instrument_bias` using `hashlib.sha256`)
**Apply to:** `fase_predict.py` (per-bus forecast error seed), `estimate.py`
```python
digest = hashlib.sha256(f"{key}|{seed}".encode()).digest()
entity_seed = int.from_bytes(digest[:4], "big")
# ALWAYS sha256 (not hashlib.md5, not Python built-in hash() — PYTHONHASHSEED-randomized)
```

### InfluxDB Connection + Bucket Creation
**Source:** `src/ieee33/influx.py` lines 31-98 (`get_client`, `wait_for_influx`, `ensure_bucket`)
**Apply to:** `publish.py`, `estimate.py`, `score.py`
```python
client = influx.get_client()
influx.wait_for_influx()
influx.ensure_bucket(client, ec.ESTIMATES_BUCKET)
write_api = client.write_api(write_options=SYNCHRONOUS)
```

### Flux Pivot Pattern for TAG-columns
**Source:** `src/ieee33/influx.py` `read_fault_bus` lines 650-667
**Apply to:** `influx.read_measurements`, `influx.read_estimates` (new helpers in `score.py`)
```python
# Tags MUST appear in rowKey to surface as string columns after pivot
# energised in fault_event: rowKey: ["_time", "bus_id", "energised"]
# phase in meas fault: add "phase" to rowKey
```

### Per-Step Console Table
**Source:** `src/ieee33/sim.py` lines 174-177; `src/ieee33/measure.py` lines 711-715
**Apply to:** `publish.py`, `estimate.py`, `score.py`
```python
print(f"\n{'Step':>4}  {'UTC Time':<20}  {col1:>N}  {col2:>N}")
print("-" * 62)
# per step:
print(f"{step_idx:>4}  {str(ts)[:19]:<20}  {v1:>N}  {v2:>N}")
```

### Fail-Loud Gate
**Source:** `src/ieee33/measure.py` lines 896-902; `src/ieee33/sim.py` lines 256-260
**Apply to:** `publish.py`, `estimate.py`, `score.py`
```python
if issues:
    print("--- [RUNNER] VALIDATION FAILED ---", file=sys.stderr)
    for issue in issues:
        print(f"  {issue}", file=sys.stderr)
    client.close()
    sys.exit(1)
```

### SYNCHRONOUS write_api
**Source:** `src/ieee33/measure.py` line 693; `src/ieee33/sim.py` line 157
**Apply to:** `estimate.py` (writes to estimates bucket)
```python
from influxdb_client.client.write_api import SYNCHRONOUS
write_api = client.write_api(write_options=SYNCHRONOUS)
```

### Point Schema Pattern (tags first, fields second)
**Source:** `src/ieee33/influx.py` lines 800-813 (`build_meas_point`)
**Apply to:** `influx.write_estimate_step` (new helper)
```python
Point("estimate")
    .tag("bus_id",     str(bus_idx))    # string tags
    .tag("scenario",   scenario)
    .tag("experiment", experiment)
    .tag("estimator",  estimator_name)
    .field("vm_pu_est",     float(v))   # float fields
    .field("va_degree_est", float(a))
    .field("sigma_vm",      float(sv))
    .field("sigma_va",      float(sa))
    .time(timestamp)
```

### paho-mqtt Client Construction
**Source:** RESEARCH.md Pattern 3 (verified paho 2.1.0 source)
**Apply to:** `publish.py`, `estimate.py`
```python
import paho.mqtt.client as mqtt
# ALWAYS pass callback_api_version explicitly — prevents DeprecationWarning (Pitfall 3)
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
```

### Oracle Separation Boundary
**Source:** CONTEXT.md D-06; SPEC.md R9
**Apply to:** `estimate.py`, `fase_predict.py`, `estimators.py`, `ac_model.py` (must NOT import)
```
ALLOWED in estimator modules: measurements (MQTT), netmodel/current (MQTT), profiles (InfluxDB)
FORBIDDEN in estimator modules: state bucket, fault_event bucket
ENFORCED: grep -r 'STATE_BUCKET\|FAULT_EVENT_BUCKET\|"state"\|"fault_event"' src/ieee33/estimate*.py
          → zero results (score.py is the only allowed importer)
```

### `build_enhanced_33bus()` Read-Only Usage
**Source:** `src/ieee33/network.py` (confirmed `build_enhanced_33bus` is read-only)
**Apply to:** `ac_model.py`, `estimate.py`
```python
from ieee33.network import build_enhanced_33bus
net, trafo_idx = build_enhanced_33bus()
# Call ONCE at startup; net is used only for static param extraction
# NEVER call pp.runpp() inside the per-step estimator loop (RESEARCH anti-pattern)
```

---

## No Analog Found

| File | Role | Data Flow | Reason |
|------|------|-----------|--------|
| `mosquitto/config/mosquitto.conf` | config | — | First MQTT broker config in repo; no prior Mosquitto file |

Note: `estimators.py` has only a partial analog (`dc_powerflow_baddata_demo.py` provides the WLS/chi2/LNR scaffold but not the EKF/UKF). The EKF and UKF must be hand-rolled using the RESEARCH.md Patterns 6 and 7 as the primary reference. The `dc_powerflow_baddata_demo.py` functions (`wls_solve`, `chi2_test`, `normalized_residuals`) are lifted directly to AC residuals.

---

## Critical Landmines (for planner to cite in plan `truths`)

1. **34-bus Ybus** — `build_enhanced_33bus()` inserts HV bus at pandapower index 33. `_pd2ppc` returns a 34×34 Ybus. State vector is 64-dimensional (32 non-slack distribution buses × 2). Any code initializing the state at 66 (2×33) will fail Ybus shape assertions.

2. **`_pd2ppc` private API** — `from pandapower.pd2ppc import pd2ppc` raises ImportError in pandapower 3.x. Use `from pandapower.pd2ppc import _pd2ppc`; unpack `ppc, ppci = _pd2ppc(net)`.

3. **paho 2.x VERSION1 explicit** — `mqtt.Client()` without `callback_api_version` emits DeprecationWarning. Always: `mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)`.

4. **Retained message race** — `estimate.py` must gate snapshot processing on `self._current_netmodel is not None`. Subscribe to `netmodel/current` first; buffer meas messages until netmodel is received.

5. **energised is a TAG string** — In `fault_event` bucket, `energised` is a string tag (`"1"`/`"0"`), not a field. Must appear in Flux `rowKey`. Compare as string: `row["energised"] == "1"`, never `== 1`.

6. **Singular G at realistic_sparse real-only** — `np.linalg.solve(G, ...)` raises `LinAlgError` before pseudo padding. Check rank explicitly and raise `RankDeficientError` with a diagnostic (SPEC R5 requires this to be reported, not silently handled).

7. **Joseph form in EKF** — Standard `P = (I-KH)P` is numerically unsafe over 96 steps. Joseph form `P = (I-KH)P(I-KH)ᵀ + KRKᵀ` is mandatory.

8. **Symmetrize before cholesky** — `cholesky(P, lower=True)` raises `LinAlgError` if floating-point asymmetry accumulates. Always: `cholesky((P + P.T)/2, lower=True)`.

9. **sha256 not hash()** — Python built-in `hash()` is PYTHONHASHSEED-randomized across processes. Use `hashlib.sha256` for all deterministic per-entity seed derivation (mirrors `measure.py` line 112).

---

## Metadata

**Analog search scope:** `system1-measurement-source/src/ieee33/`, `system1-measurement-source/grafana/`, `system1-measurement-source/`, `.planning/phases/02-distribution-virtual-sensing/demo/`
**Files scanned:** 9 source files read in full; 4 partially read
**Pattern extraction date:** 2026-06-26
