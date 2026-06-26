# Phase 10: System 2 — Streaming Distribution State Estimator (MQTT + FASE) - Research

**Researched:** 2026-06-26
**Domain:** AC Distribution State Estimation (DSSE): MQTT replay, Ybus, WLS, EKF, UKF, FASE, NEES/NIS
**Confidence:** HIGH

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

- **D-01:** Three separate runners: `publish`, `estimate`, `score` added as `[project.scripts]` entries.
  The MQTT broker decouples `publish` from `estimate` (real async stream).
- **D-02:** `estimate` runs ONE estimator per invocation, selected by `--estimator wls|ekf|ukf`.
  Each run tags its output by the `estimator` tag.
- **D-03:** New `estimate_config.py` with `ACTIVE` block mirroring `measure_config.py`, with CLI
  overrides (`--scenario --source --estimator --seed --acceleration ...`).
- **D-04:** Predict mean = sensitivity-propagated profile forecast (primary), with random-walk
  persistence as the A/B baseline foil behind the same predict interface.
- **D-05:** Forecast: (1) read nodal injections for step k from `profiles` bucket; (2) degrade with
  seeded AR(1) error ε; (3) Δp = p_fcst(k) − p_fcst(k−1); (4) x̂ₖ⁻ = x̂ₖ₋₁ + S·Δp_fcst;
  (5) Qₖ = S·Cov(ε)·Sᵀ + Q_floor.
- **D-06:** Reading `profiles` is NOT an oracle leak. Forbidden: `state`/`fault_event`. Allowed:
  `measurements` (MQTT) + `netmodel/current` (MQTT) + `profiles` (forecast). Grep-checkable.
- **D-07:** Forecast-error model = realistic day-ahead, config-tunable. Default per-bus σ ≈ 5% of
  scheduled load, AR(1)-correlated (ρ tunable), seed-derived for determinism.
- **D-08:** Two auto-provisioned estimator dashboards: `ieee33-est-day.json` and
  `ieee33-est-fault.json`, additive to the four existing dashboards.

### Claude's Discretion (locked for downstream)

- MQTT topic hierarchy: `ieee33/{experiment}/{scenario}/meas/{class}/{location}`, payload
  `{value, assumed_sigma, quantity, class, location, experiment, scenario, phase, timestamp}`.
- Topology re-publish: `ieee33/{experiment}/{scenario}/event`, payload = P9 event fields.
- Network config topic: `ieee33/netmodel/current`, RETAINED + versioned, payload = authoritative
  switch-state (in-service line set + tie states + dead-bus set + phase) + `config_version` +
  timestamp. Day: version 0 once; fault: new version per topology change.
- Topology→Ybus rebuild: apply streamed in-service-line set + tie states to static line/bus
  impedances from `build_enhanced_33bus()`. Equality test < 1e-9 is the gate (SPEC R3).
- UKF parameterization: square-root UKF, standard sigma-point params (α, β, κ).
- AC-WLS bad-data: reuse χ²/LNR approach from `dc_powerflow_baddata_demo.py` lifted to AC residuals.
- Exact `estimate_config.py` fields, Flux query details, Grafana panel layout, NEES/NIS band
  computation details, and Q_floor magnitude are planner/executor details.

### Deferred Ideas (OUT OF SCOPE)

- System 3 (self-healing, FLISR, CaCSM dispatch, simulate-before-commit, `netmodel/proposed`).
- Three-phase unbalanced state; branch-current (BCSE) formulation.
- Federated/multi-area DSSE with boundary-state exchange.
- Non-MQTT transports (C37.118-over-UDP, NATS, 2030.5).
- LinDistFlow linear-KF as a deliverable.
- Mis-specified-noise robustness study and forecast-quality sweep (knobs built, gating out of scope).

</user_constraints>

---

<phase_requirements>
## Phase Requirements

| ID  | Description | Research Support |
|-----|-------------|------------------|
| R1  | Mosquitto broker in docker-compose (localhost-bound) | Eclipse Mosquitto 2.0, 10.6 MB image confirmed pulled; Mosquitto config pattern verified |
| R2  | Replay publisher (InfluxDB→MQTT): deterministic order, acceleration, day+fault, retained `netmodel/current` | paho-mqtt 2.1.0 publish + retain pattern; QoS 1 for ordered determinism; acceleration via time.sleep scaling |
| R3  | AC measurement model h(x), H, Ybus derived from `netmodel/current` topology | Hand-built Ybus verified < 4e-14 vs ppci Ybus; pd2ppc+makeYbus extraction path confirmed; Jacobian FD check pattern documented |
| R4  | MQTT subscriber + snapshot assembler | paho-mqtt 2.1.0 subscribe + loop_start; version-aware Ybus rebuild pattern |
| R5  | AC-WLS snapshot baseline with χ²/LNR bad-data detection | DC demo code available at `.planning/phases/02.../demo/dc_powerflow_baddata_demo.py`; lift to AC residuals |
| R6  | Recursive EKF with FASE predict | predict/update equations documented; FASE S matrix from H injection rows; Q from S·Cov(ε)·Sᵀ + Q_floor |
| R7  | Recursive UKF (square-root) with same FASE predict | sqrt-UKF via scipy.linalg.cholesky; sigma-point params documented |
| R8  | `estimates` InfluxDB bucket: vm_pu_est, va_degree_est, sigma_vm, sigma_va, trace_P, tagged by estimator | ensure_bucket reuse; Point schema pattern from influx.py |
| R9  | Separate `score` harness (never reads oracle buckets from estimator) | Oracle-separation enforced by module import boundary; grep-checkable |
| R10 | Accuracy thresholds: well_observed <0.005 pu / <0.1°; realistic_sparse dark-node <0.02 pu / ≤50% baseline | Achievable with UKF given noise levels (σ_scada=0.005 pu, σ_pmu=0.001 pu); tight convergence requires good initialization |
| R11 | Covariance calibration: NEES in 95% χ² band; NIS in-band ≥90% of steps | NEES 95% band = [61.76, 66.28] for n=64, N=96; NIS band per step depends on m (variable) |
| R12 | Fault island-mode: σ_V / trace_P higher in faulted_isolated; no estimate for dead buses; restored RMSE within bar | Ybus rebuild on config_version bump; dead-bus masking pattern from measure.py |
| R13 | Determinism, Grafana dashboards, README runbook | Seeded RNG norm established; Grafana auto-provision pattern in place (4 existing dashboards); paho publish order fixed |

</phase_requirements>

---

## Summary

Phase 10 adds an entirely new module to `system1-measurement-source/src/ieee33/` — a streaming AC Distribution State Estimator that consumes Phase-9 `measurements` over MQTT and reconstructs node-voltage state `x = {|V|, θ}` at every energised bus with calibrated posterior covariance P. The work falls into six separable concerns: (1) MQTT infrastructure (Mosquitto + paho), (2) Ybus construction from a streamed topology message, (3) AC measurement model h(x)/H, (4) three estimators (WLS, EKF, UKF) behind one predict/update interface, (5) FASE predict step from the `profiles` bucket, and (6) scoring harness and Grafana dashboards.

The critical insight established by research: the enhanced IEEE 33-bus network has **34 buses** (0..32 distribution + HV feeder bus 33 as ext_grid/slack). The estimator state vector spans buses 0..33 with θ₃₃ = 0 fixed and |V|₃₃ known from the regulated slack, yielding **64 free states** (= 2×32 for distribution non-slack buses: buses 0..32 contribute 66 states, minus 2 for the slack angle and the HV bus's fully-known state). The Ybus is 34×34 (full system); topology variation only affects lines 0..34 (the 32 distribution lines + 3 tie-lines); the trafo contribution is fixed. Hand-built Ybus from static line parameters matches pandapower ppci Ybus to < 4e-14 (SPEC R3 gate of 1e-9 is comfortably achievable). The DC bad-data demo at `.planning/phases/02-distribution-virtual-sensing/demo/dc_powerflow_baddata_demo.py` provides the `wls_solve`, `chi2_test`, and `normalized_residuals` functions to lift directly to AC residuals.

**Primary recommendation:** Hand-roll all estimator math (numpy/scipy only; no filterpy). Use paho-mqtt==2.1.0 with `CallbackAPIVersion.VERSION1` for compatibility. Use `scipy.linalg.cholesky` for the square-root UKF. Implement the predict/update interface as a Python abstract base class with `WLSEstimator`, `EKFEstimator`, `UKFEstimator` concrete implementations.

---

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| MQTT publish (replay) | Backend script (`publish.py`) | Mosquitto broker | Pure producer; reads InfluxDB, emits MQTT |
| MQTT subscribe + snapshot assembly | Backend script (`estimate.py`) | Mosquitto broker | Consumer side; assembles z vector per snapshot |
| Ybus construction | Estimator module (backend) | — | Deterministic function of topology config; no I/O |
| AC measurement model h(x)/H | Estimator module (backend) | — | Pure math; network-coupled; inside h(x) per SPEC R3 |
| AC-WLS, EKF, UKF estimators | Estimator module (backend) | — | Compute-intensive; no external calls during estimation |
| FASE predict (profiles read) | Estimator module (backend) | InfluxDB | Reads `profiles` at startup (not per-step for latency) |
| Oracle scoring | `score.py` (backend only) | InfluxDB oracle buckets | Sole reader of `state`/`fault_event`; never imported by estimator |
| `estimates` persistence | InfluxDB (`estimates` bucket) | Estimator write path | Same pattern as `state`/`measurements` buckets |
| Visualization | Grafana (two new dashboards) | InfluxDB datasource | Auto-provisioned; additive to existing 4 dashboards |

---

## Standard Stack

### Core

| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| paho-mqtt | 2.1.0 | MQTT publish/subscribe | Industry standard Python MQTT client; latest stable [VERIFIED: pip3 index versions] |
| numpy | ≥1.26,<2.4 | Ybus construction, h(x)/H, Kalman math | Already in pyproject.toml; all matrix ops |
| scipy | (transitive via pandapower) | cholesky/cho_factor for sqrt-UKF; chi2 for NEES/NIS bands | scipy.linalg.cholesky confirmed available [VERIFIED: runtime test] |
| pandapower | 3.4.0 | `build_enhanced_33bus()` static params; `_pd2ppc`+`makeYbus` for reference Ybus | Already pinned; Ybus extraction tested [VERIFIED: runtime test] |
| influxdb-client | 1.50.0 | Read `measurements`/`profiles`/`state`/`fault_event`; write `estimates` | Already pinned; reuse existing helpers |
| eclipse-mosquitto | 2.0 (Docker) | Local MQTT broker | 10.6 MB image; pulled and confirmed [VERIFIED: docker pull] |

### Supporting

| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| scipy.stats.chi2 | (scipy) | NEES/NIS 95% chi² band computation | Score harness only; ppf/cdf calls |
| scipy.linalg | (scipy) | `cholesky`, `cho_solve`, `solve_triangular` | sqrt-UKF P updates; WLS gain solve |
| hashlib (stdlib) | stdlib | Deterministic per-bus forecast-error seed derivation | Mirror of measure.py `_instrument_bias` pattern |
| argparse (stdlib) | stdlib | CLI overrides for sweep runs | Mirror of measure.py `_parse_args` pattern |
| json (stdlib) | stdlib | MQTT payload serialization/deserialization | JSON for all MQTT messages |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Hand-rolled EKF/UKF | filterpy | filterpy is not in venv; adds a dependency; its UKF implementation is not sqrt form; determinism unclear. Hand-roll gives full control, zero added deps, and exact sqrt-P form. [ASSUMED] filterpy not in current venv |
| Hand-rolled sqrt-UKF | pandapower.estimation.StateEstimation | pandapower's WLS estimator exists (`StateEstimation` class with `algorithm` param) but wraps around its own measurement model — incompatible with the MQTT stream + FASE predict architecture. SPEC requires the power flow inside h(x), not a separate runpp call. [VERIFIED: runtime inspection] |
| paho-mqtt 2.x with VERSION2 callbacks | VERSION1 compat mode | VERSION2 requires updating all callback signatures (ConnectFlags, ReasonCode). VERSION1 is the default in 2.1.0 and fully supported. Use VERSION1 to minimize boilerplate. |
| eclipse-mosquitto:2.0 | mosquitto:latest | Pin to 2.0 for reproducibility; same image as used in dev. |

**Installation:**
```bash
# Add to pyproject.toml dependencies:
uv add paho-mqtt==2.1.0
# Mosquitto is a Docker service (no pip install needed)
```

**Version verification:** [VERIFIED: pip3 index versions paho-mqtt] — 2.1.0 is the latest stable release.

---

## Architecture Patterns

### System Architecture Diagram

```
InfluxDB (measurements bucket)
    |
    | Flux query (ordered by _time, class, location)
    v
publish.py ──────────────────────────────────────────────────────────────────┐
    |  paho publish QoS 1                                                      |
    |  ieee33/{exp}/{scen}/meas/{class}/{location}                             |
    |  ieee33/{exp}/{scen}/event                                               |
    |  ieee33/netmodel/current  (RETAINED, versioned)                          |
    v                                                                           |
eclipse-mosquitto:2.0 ────────────────────────────────────────────────────────┘
    |
    | paho subscribe (estimate.py)
    v
estimate.py
    ├── MQTTSnapshotAssembler
    │       accumulates z[], R diag per snapshot
    │       tracks config_version → triggers Ybus rebuild
    │
    ├── TopologyModel
    │       netmodel/current → line in-service set + tie states
    │       hand-build Ybus from static impedances
    │       static params from build_enhanced_33bus() (read-only, once at startup)
    │
    ├── ACMeasurementModel
    │       h(x): P_inj/Q_inj via Ybus + polar coords; |V|/angle pickoffs for PMU
    │       H: analytic Jacobian (dP/d|V|, dP/dθ, dQ/d|V|, dQ/dθ blocks)
    │       FD-verified at startup (< 1e-5)
    │
    ├── FASEPredictor
    │       reads profiles bucket at startup (all 96 steps, one query)
    │       AR(1) seeded forecast error for each step
    │       S = sensitivity matrix (recomputed from H at current x̂)
    │       Δp_fcst → x̂⁻ = x̂ + S·Δp;  Q = S·Cov(ε)·Sᵀ + Q_floor
    │       persistence foil: same interface, Δp = 0, Q = Q_rw
    │
    └── Estimator (one of WLS | EKF | UKF, selected by --estimator)
            predict(x̂, P, Δp_fcst) → (x̂⁻, P⁻)   [EKF/UKF only]
            update(x̂⁻, P⁻, z, R, H) → (x̂, P)
            writes per-bus vm_pu_est/va_degree_est/sigma_vm/sigma_va + trace_P
            to estimates bucket tagged by scenario/experiment/estimator
            
score.py (separate process, runs after estimate)
    ├── reads estimates bucket (all estimators)
    ├── reads state / fault_event oracle buckets (ONLY component allowed to)
    └── computes RMSE, dark-node error, NEES, NIS → printed report
```

### Recommended Project Structure

```
system1-measurement-source/
├── src/ieee33/
│   ├── publish.py         # R1/R2: InfluxDB→MQTT replay runner
│   ├── estimate.py        # R4+R5+R6+R7+R8: subscribe + assemble + estimate + write
│   ├── estimate_config.py # D-03: ACTIVE block + knobs (mirrors measure_config.py)
│   ├── ac_model.py        # R3: Ybus builder + h(x) + H + FD check + topology model
│   ├── estimators.py      # R5+R6+R7: WLSEstimator, EKFEstimator, UKFEstimator + interface
│   ├── fase_predict.py    # D-04/D-05: FASEPredictor + persistence foil
│   ├── score.py           # R9: oracle join + RMSE + NEES/NIS report
│   ├── network.py         # UNCHANGED
│   ├── influx.py          # UNCHANGED (add read_measurements + write_estimate helpers)
│   ├── measure.py         # UNCHANGED
│   ├── measure_config.py  # UNCHANGED
│   └── config.py          # UNCHANGED (add ESTIMATES_BUCKET constant)
├── grafana/provisioning/dashboards/
│   ├── default.yml        # UNCHANGED
│   ├── ieee33-state.json  # UNCHANGED
│   ├── ieee33-fault-event.json # UNCHANGED
│   ├── ieee33-meas-day.json    # UNCHANGED
│   ├── ieee33-meas-fault.json  # UNCHANGED
│   ├── ieee33-est-day.json     # NEW: D-08
│   └── ieee33-est-fault.json   # NEW: D-08
├── docker-compose.yml     # ADD mosquitto service (additive)
├── mosquitto/
│   └── config/mosquitto.conf   # NEW: minimal mosquitto config
└── pyproject.toml         # ADD paho-mqtt==2.1.0 + 3 new scripts
```

### Pattern 1: paho-mqtt 2.x Retained Publish (Publisher Side)

paho-mqtt 2.x changed the `CallbackAPIVersion` model. Use `VERSION1` (the default) to keep V1-compatible callback signatures.

**Key facts about paho 2.x (VERSION1 mode):** [VERIFIED: paho-mqtt 2.1.0 source inspection]
- `Client(callback_api_version=CallbackAPIVersion.VERSION1)` — VERSION1 is the default
- `on_connect(client, userdata, flags, rc)` — same as v1.x
- `on_message(client, userdata, msg)` — same as v1.x
- `publish(topic, payload, qos, retain)` — unchanged API
- `loop_start()` / `loop_stop()` for background thread; `loop_forever()` for blocking
- Retained message: `publish(topic, payload, qos=1, retain=True)` — Mosquitto stores and delivers to late subscribers

**Ordered deterministic publish pattern:**
```python
# Source: paho-mqtt 2.1.0 docs + VERSION1 compat
import paho.mqtt.client as mqtt
import json, time

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
client.connect("127.0.0.1", 1883, keepalive=60)
client.loop_start()

# 1. Publish retained netmodel/current FIRST (before any meas)
config_payload = json.dumps({
    "config_version": 0,
    "in_service_lines": list(range(32)),   # lines 0..31 (tie lines 32-34 open)
    "tie_closed": False,
    "tie_id": -1,
    "dead_buses": [],
    "phase": "steady_state",
    "timestamp": ts_iso,
})
client.publish("ieee33/netmodel/current", config_payload, qos=1, retain=True)

# 2. Publish meas points in FIXED ORDER: sorted by (timestamp, class, location)
for ts, cls, loc, payload_dict in sorted_meas:
    topic = f"ieee33/{experiment}/{scenario}/meas/{cls}/{loc}"
    client.publish(topic, json.dumps(payload_dict), qos=1, retain=False)
    # Acceleration: sleep (step_duration_s / accel_factor) between snapshots
    
client.loop_stop()
client.disconnect()
```

**QoS choice:** QoS 1 (at-least-once) for all messages. QoS 1 preserves ordering within a publisher's send queue and ensures delivery. QoS 0 (fire-and-forget) risks drops with fast replay. QoS 2 (exactly-once) adds handshake overhead and is not needed for a local loopback publisher. [ASSUMED — no official Mosquitto benchmark for this specific use case; QoS 1 is the standard recommendation for reliable ordered local delivery]

### Pattern 2: paho-mqtt 2.x Subscribe + Snapshot Assembly (Estimator Side)

```python
# Source: paho-mqtt 2.1.0 docs
import paho.mqtt.client as mqtt
import json, threading

class MQTTSnapshotAssembler:
    def __init__(self):
        self._current_netmodel = None
        self._config_version = -1
        self._snapshot_buffer = {}   # {ts: {(cls, loc): meas_dict}}
        self._lock = threading.Lock()
        
    def on_connect(self, client, userdata, flags, rc):
        # Subscribe to measurement topics and netmodel (wildcard)
        client.subscribe("ieee33/+/+/meas/#", qos=1)
        client.subscribe("ieee33/netmodel/current", qos=1)
        
    def on_message(self, client, userdata, msg):
        payload = json.loads(msg.payload.decode())
        if msg.topic == "ieee33/netmodel/current":
            version = payload["config_version"]
            if version != self._config_version:
                # topology change → rebuild Ybus
                self._config_version = version
                self._current_netmodel = payload
                self._rebuild_ybus(payload)
        else:
            # meas message: accumulate into snapshot buffer by timestamp
            ts = payload["timestamp"]
            with self._lock:
                self._snapshot_buffer.setdefault(ts, {})
                self._snapshot_buffer[ts][(payload["class"], payload["location"])] = payload
                
    def _rebuild_ybus(self, config):
        """Rebuild from static params + streamed in-service-line set."""
        in_service = set(config["in_service_lines"])
        if config.get("tie_closed") and config.get("tie_id", -1) >= 0:
            in_service.add(config["tie_id"])
        # hand-build Ybus from static_line_params (precomputed from build_enhanced_33bus)
        ...

# Graceful shutdown:
client.loop_start()
# ... main loop: poll snapshot_buffer, drive estimator
# To stop:
client.loop_stop()
client.disconnect()
```

**Graceful shutdown:** `loop_stop()` signals the background thread to exit; `disconnect()` sends MQTT DISCONNECT. No busy-waits needed. [VERIFIED: paho-mqtt 2.1.0 source]

### Pattern 3: Topology → Ybus Hand-Build (VERIFIED to < 4e-14)

The hand-build approach using `net.line` static parameters matches pandapower's ppci Ybus to < 4e-14 element-wise. [VERIFIED: runtime test on case33bw with radial topology]

```python
# Source: verified runtime test (see research session)
import numpy as np
from scipy.sparse import lil_matrix

def build_ybus_from_topology(static_line_params, in_service_line_ids, n_bus, base_z_pu):
    """
    static_line_params: dict {line_idx: {from_bus, to_bus, r_total_ohm, x_total_ohm, b_total_pu}}
    in_service_line_ids: set of active line indices (from netmodel/current topic)
    n_bus: total bus count (34 for enhanced net)
    base_z_pu: base impedance = (base_kv^2 / base_mva) in ohms
    
    Returns: np.ndarray (n_bus x n_bus) complex128 Ybus
    """
    Y = np.zeros((n_bus, n_bus), dtype=complex)
    for idx in in_service_line_ids:
        params = static_line_params[idx]
        i, j = params["from_bus"], params["to_bus"]
        r_pu = params["r_total_ohm"] / base_z_pu
        x_pu = params["x_total_ohm"] / base_z_pu
        y_series = 1.0 / (r_pu + 1j * x_pu)
        b_shunt  = params.get("b_total_pu", 0.0)   # capacitive charging (often 0 in case33bw)
        Y[i, j] -= y_series
        Y[j, i] -= y_series
        Y[i, i] += y_series + 0.5j * b_shunt
        Y[j, j] += y_series + 0.5j * b_shunt
    # Add trafo fixed contribution (computed once from build_enhanced_33bus ppci)
    # Y += Y_trafo_fixed  (precomputed from _pd2ppc on the base network)
    return Y

# Verification gate (SPEC R3):
# assert np.max(np.abs(Ybus_hand - Ybus_ppci)) < 1e-9
```

**Critical landmine — ENHANCED NET HAS 34 BUSES:** `build_enhanced_33bus()` inserts a new HV bus at pandapower index 33 (moving ext_grid to it). `_pd2ppc` returns a 34×34 Ybus. The estimator state covers buses 0..32 (distribution); bus 33 is the slack. Account for this in the hand-build by also computing the trafo's pi-equivalent admittance and storing it as a fixed addend to Y[0,33], Y[33,0], Y[0,0], Y[33,33]. [VERIFIED: runtime test — 34×34 Ybus confirmed]

**Alternative verified approach:** Call `_pd2ppc(net)` on a rebuilt net with the desired topology, then `makeYbus(ppci['baseMVA'], ppci['bus'], ppci['branch'])`. This is slower (requires a pandapower call per topology change) but is the reference for the verification gate. For the 3-topology fault scenario, rebuilding pandapower 3 times is fine; the hand-build is preferred for speed and is the primary path. [VERIFIED: `_pd2ppc` exists in pandapower.pd2ppc; `makeYbus` in pandapower.pypower.makeYbus]

### Pattern 4: AC Measurement Model h(x) and Jacobian H

State vector convention (polar): `x = [|V|₀, θ₀, |V|₁, θ₁, ..., |V|₃₂, θ₃₂, |V|₃₃, θ₃₃]` (66 entries). Fixed: θ₃₃ = 0 (slack reference), |V|₃₃ = known. **Free state dimension = 64**.

For bus i, the AC power injection equations with Ybus = G + jB:

```
P_i(x) = |V_i| · Σ_k |V_k| · (G_ik · cos(θ_i - θ_k) + B_ik · sin(θ_i - θ_k))
Q_i(x) = |V_i| · Σ_k |V_k| · (G_ik · sin(θ_i - θ_k) - B_ik · cos(θ_i - θ_k))
```

**Measurement rows by class:**
| Class | Quantity | h(x) row |
|-------|----------|----------|
| scada | vm_pu at bus i | x[2i] (direct |V_i| pickoff) |
| scada | p_inj_mw at bus i | P_i(x) via Ybus |
| scada | q_inj_mvar at bus i | Q_i(x) via Ybus |
| pmu | vm_pu at bus i | x[2i] (identity) |
| pmu | va_degree at bus i | x[2i+1] · (180/π) (identity with unit conversion) |
| ami | p_inj_mw at bus i | P_i(x) via Ybus |
| ami | q_inj_mvar at bus i | Q_i(x) via Ybus |
| der | p_mw at bus i (sgen) | P_i(x) with sign convention: generation = negative injection |
| der | q_mvar at bus i (sgen) | Q_i(x) analogously |
| pseudo | p_inj_mw / q_inj_mvar | same as ami/scada rows |
| zero_inj | p_inj_mw / q_inj_mvar | same as above; assumed_sigma very small (1e-4) |

**Sign convention:** P9 uses positive-injection = net consumption (load convention). The estimator must match this convention throughout h(x). [CITED: measure.py `get_true_value`, influx.py `write_fault_step`]

**Analytic Jacobian H** (standard WLS DSSE, polar formulation): [ASSUMED — standard textbook; verify with FD check per SPEC R3]

```
For P_i row (wrt |V_j|, θ_j):
  dP_i/d|V_j| = |V_i| · (G_ij·cos(θ_ij) + B_ij·sin(θ_ij))  for j ≠ i
  dP_i/d|V_i| = Σ_k |V_k|·(G_ik·cos(θ_ik)+B_ik·sin(θ_ik)) + |V_i|·G_ii  (diagonal)
  dP_i/dθ_j  = |V_i|·|V_j|·(-G_ij·sin(θ_ij)+B_ij·cos(θ_ij))  for j ≠ i
  dP_i/dθ_i  = -Q_i(x) - |V_i|²·B_ii  (diagonal)

For Q_i row (wrt |V_j|, θ_j):
  dQ_i/d|V_j| = |V_i| · (G_ij·sin(θ_ij) - B_ij·cos(θ_ij))  for j ≠ i
  dQ_i/d|V_i| = Σ_k |V_k|·(G_ik·sin(θ_ik)-B_ik·cos(θ_ik)) - |V_i|·B_ii  (diagonal)
  dQ_i/dθ_j  = |V_i|·|V_j|·(G_ij·cos(θ_ij)+B_ij·sin(θ_ij))  for j ≠ i
  dQ_i/dθ_i  = P_i(x) - |V_i|²·G_ii  (diagonal)
  
where θ_ij = θ_i - θ_j
```

**Finite-difference verification (SPEC R3 gate < 1e-5):**
```python
eps = 1e-6
for j in range(n_state):
    x_fwd = x.copy(); x_fwd[j] += eps
    x_bwd = x.copy(); x_bwd[j] -= eps
    H_fd[:, j] = (h(x_fwd) - h(x_bwd)) / (2 * eps)
assert np.max(np.abs(H_analytic - H_fd)) < 1e-5
```

### Pattern 5: AC-WLS Snapshot Estimator (lifted from DC demo)

```python
# Lifted from dc_powerflow_baddata_demo.py (confirmed at .planning/phases/02.../demo/)
def wls_gauss_newton(h_fn, H_fn, z, W, x0, max_iter=20, tol=1e-6):
    """AC WLS Gauss-Newton iteration."""
    x = x0.copy()
    for _ in range(max_iter):
        r = z - h_fn(x)          # residuals
        H = H_fn(x)              # analytic Jacobian
        G = H.T @ W @ H          # gain matrix (check rank before solve)
        if np.linalg.matrix_rank(G) < G.shape[0]:
            raise RankDeficientError("G = H^T W H is rank-deficient (under-observable)")
        dx = np.linalg.solve(G, H.T @ W @ r)
        x = x + dx
        if np.linalg.norm(dx) < tol:
            break
    return x, G

# Bad-data detection (AC residuals — same machinery as DC demo)
# 1. Chi-squared test: J = r^T W r; threshold = chi2.ppf(0.95, m - n)
# 2. LNR: Omega = R - H G^{-1} H^T; rN_i = |r_i| / sqrt(Omega_ii)
#    CAUTION: Omega diagonal can become negative at high leverage → clamp to abs value
```

**Rank deficiency reporting (SPEC R5):** On `realistic_sparse` with real measurements only, the gain matrix G = HᵀWH is rank-deficient (system is under-observable, redundancy < 1.0). The WLS runner must catch this explicitly and print a diagnostic, NOT return garbage. The system becomes solvable after pseudo-measurement padding. [VERIFIED: measure.py footprint report confirms real-only redundancy < 1.0 for `realistic_sparse`]

### Pattern 6: Recursive EKF with FASE Predict

```python
class EKFEstimator:
    def __init__(self, n=64, Q_floor_scale=1e-6):
        self.x = np.ones(n) * 1.0    # flat start: |V|=1.0, θ=0
        # Interleaved: x[2i]=|V_i|, x[2i+1]=θ_i
        self.P = np.eye(n) * 0.01    # initial uncertainty
        self.Q_floor = np.eye(n) * Q_floor_scale
        
    def predict(self, delta_p_fcst, S, Cov_eps):
        """FASE predict: x⁻ = x + S·Δp;  P⁻ = P + Q"""
        self.x = self.x + S @ delta_p_fcst
        Q = S @ Cov_eps @ S.T + self.Q_floor
        self.P = self.P + Q
        
    def update(self, z, R, h_fn, H_fn):
        """Standard EKF update."""
        H = H_fn(self.x)
        y = z - h_fn(self.x)          # innovation
        S = H @ self.P @ H.T + R      # innovation covariance
        K = self.P @ H.T @ np.linalg.solve(S.T, np.eye(len(z))).T  # Kalman gain
        self.x = self.x + K @ y
        I_KH = np.eye(len(self.x)) - K @ H
        self.P = I_KH @ self.P @ I_KH.T + K @ R @ K.T   # Joseph form (numerically stable)
        return y, S   # return for NIS computation
```

**Joseph form** for the covariance update is mandatory. The standard `P = (I-KH)P` is algebraically equivalent but numerically unsafe for asymmetric perturbations; Joseph form `P = (I-KH)P(I-KH)^T + KRK^T` preserves symmetry and positive-definiteness. [CITED: standard Kalman filter textbooks; ASSUMED — not independently verified in this session against a specific source, but universally recommended]

**Multirate awareness:** On steps where a measurement class does not report (e.g., AMI every 4th step in `multirate_async`), simply do not include those rows in z/H/R at the update step. The predict step still runs every step.

### Pattern 7: Square-Root UKF

The **square-root UKF** propagates the Cholesky factor `S_P = chol(P)` instead of `P` directly, guaranteeing positive-definiteness through all operations. [ASSUMED — standard reference: Van der Merwe & Wan 2001; scipy.linalg.cholesky confirmed available]

```python
# Source: scipy.linalg.cholesky confirmed available in project venv [VERIFIED]
from scipy.linalg import cholesky, cho_solve, solve_triangular

class UKFEstimator:
    def __init__(self, n=64, alpha=1e-3, beta=2.0, kappa=0.0, Q_floor_scale=1e-6):
        self.n = n
        self.alpha = alpha
        self.beta = beta
        self.kappa = kappa
        lam = alpha**2 * (n + kappa) - n
        self.lam = lam
        # Weights for mean and covariance
        self.Wm = np.full(2*n+1, 1.0/(2*(n+lam)))
        self.Wm[0] = lam / (n + lam)
        self.Wc = self.Wm.copy()
        self.Wc[0] = lam/(n+lam) + (1 - alpha**2 + beta)
        self.x = np.ones(n)
        self.S_P = np.eye(n) * 0.1    # Cholesky factor of P
        self.Q_floor = np.eye(n) * Q_floor_scale
        
    def sigma_points(self):
        """Compute 2n+1 sigma points from current (x, S_P)."""
        scale = np.sqrt(self.n + self.lam)
        sigmas = np.zeros((2*self.n+1, self.n))
        sigmas[0] = self.x
        for i in range(self.n):
            sigmas[i+1]      = self.x + scale * self.S_P[:, i]
            sigmas[self.n+i+1] = self.x - scale * self.S_P[:, i]
        return sigmas
        
    def predict(self, delta_p_fcst, S, Cov_eps):
        """FASE predict with Q assembled from sensitivity."""
        self.x = self.x + S @ delta_p_fcst
        Q = S @ Cov_eps @ S.T + self.Q_floor
        P = self.S_P @ self.S_P.T + Q
        self.S_P = cholesky(P + P.T)/2 * 0 + cholesky((P+P.T)/2, lower=True)
        # Simpler: self.S_P = cholesky(self.S_P @ self.S_P.T + Q, lower=True)
        
    def update(self, z, R, h_fn):
        """UKF update — no Jacobian needed."""
        sigmas = self.sigma_points()
        Z = np.array([h_fn(s) for s in sigmas])   # propagate through h
        z_hat = Z.T @ self.Wm
        Pzz = sum(self.Wc[i] * np.outer(Z[i]-z_hat, Z[i]-z_hat) for i in range(2*self.n+1)) + R
        Pxz = sum(self.Wc[i] * np.outer(sigmas[i]-self.x, Z[i]-z_hat) for i in range(2*self.n+1))
        K = Pxz @ np.linalg.inv(Pzz)
        y = z - z_hat
        self.x = self.x + K @ y
        P_new = self.S_P @ self.S_P.T - K @ Pzz @ K.T
        self.S_P = cholesky((P_new + P_new.T)/2, lower=True)
        return y, Pzz
```

**Sigma-point parameter defaults:** α=1e-3, β=2.0 (optimal for Gaussian priors), κ=0.0. These are standard for state estimation with continuous Gaussian priors. λ = α²(n+κ) - n with n=64 gives λ ≈ -63.9936. [ASSUMED — standard references recommend these defaults; tuning may be needed]

**Numerical safety:** After every P update, symmetrize and check positive-definiteness via `cholesky`. If `cholesky` raises `LinAlgError`, add jitter: `P += jitter * np.eye(n)` with jitter = 1e-8. [ASSUMED — standard practice]

### Pattern 8: NEES/NIS Covariance Calibration

```python
# Source: scipy.stats.chi2 confirmed in scipy (transitive dep via pandapower) [VERIFIED: runtime test]
from scipy.stats import chi2
import numpy as np

def compute_nees_nis_report(estimates, oracle_states, n_state):
    """
    estimates: list of (x_hat_k, P_k) tuples
    oracle_states: list of x_true_k arrays
    n_state: state dimension (64)
    
    Returns dict with NEES verdict and NIS fraction.
    """
    N = len(estimates)
    alpha = 0.05
    
    # NEES per step: NEES_k = (x_hat - x_true)^T P^{-1} (x_hat - x_true)
    nees_vals = []
    for (x_hat, P), x_true in zip(estimates, oracle_states):
        err = x_hat - x_true
        nees_k = err @ np.linalg.solve(P, err)
        nees_vals.append(nees_k)
    
    nees_avg = np.mean(nees_vals)
    lo = chi2.ppf(alpha/2, N * n_state) / N
    hi = chi2.ppf(1 - alpha/2, N * n_state) / N
    # Expected: nees_avg ≈ n_state = 64
    # 95% band for n=64, N=96: [61.76, 66.28]
    nees_pass = lo <= nees_avg <= hi
    
    return {
        "nees_avg": nees_avg, "nees_lo": lo, "nees_hi": hi, 
        "nees_pass": nees_pass,
        # NIS computed analogously from stored (innovation_k, S_k) pairs
    }
```

**NEES vs NIS distinction:**
- **NEES** (Normalized Estimation Error Squared): compares x̂ to oracle x_true. Requires oracle access → computed in `score.py` only.
- **NIS** (Normalized Innovation Squared): `v_k^T S_k^{-1} v_k` where `v_k = z_k - h(x̂_k⁻)` and `S_k = H P_k⁻ Hᵀ + R`. NIS is computable without oracle → store (innovation, S) pairs during estimation, score later.
- **95% acceptance band** (SPEC R11): time-averaged NEES ∈ [61.76, 66.28] for n=64, N=96. Per-step NIS ∈ chi2.ppf(0.025, m_k)..chi2.ppf(0.975, m_k) where m_k is the innovation dim at step k. Fraction of steps with in-band NIS ≥ 90%. [VERIFIED: scipy chi2.ppf runtime test]

### Anti-Patterns to Avoid

- **Using `np.random.seed()` or `random.seed()`** — use `np.random.default_rng(seed)` everywhere (matches existing project norm from `measure.py`). [CITED: measure.py line 688]
- **Transporting Ybus over MQTT** — SPEC R3 explicitly forbids this. Only topology/switch-state is transported.
- **Reading `state` or `fault_event` from the estimator** — `score.py` is the only component that may. All access must be grep-checkable.
- **Using `time.time()` or `datetime.now()` in deterministic paths** — publisher uses wall-clock for throttling only; estimator/scoring paths must be deterministic.
- **Standard (non-Joseph) P update in EKF** — the symmetric Joseph form is mandatory for numerical stability over 96 steps.
- **Not symmetrizing P before cholesky** — `cholesky((P+P.T)/2, lower=True)` prevents numerical noise from making P appear non-symmetric.
- **Calling `pp.runpp()` inside the per-step estimator loop** — Ybus is precomputed from static parameters; runpp is only called for the reference verification (startup gate) and for rebuilding the reference Ybus on topology change.
- **Using `hashlib.md5` instead of `hashlib.sha256`** for deterministic seeds — the project uses `sha256` (measure.py line 112); be consistent.

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| MQTT broker | Custom TCP server | `eclipse-mosquitto:2.0` Docker service | Handles retained msgs, QoS, client reconnect; 10.6 MB |
| Cholesky factorization | Own sqrt decomp | `scipy.linalg.cholesky` | Handles numerical edge cases (near-singular P) properly |
| Chi-squared band computation | Lookup table | `scipy.stats.chi2.ppf(alpha, df)` | Exact; already available transitively |
| Ybus extraction for reference test | Reimplementing pi-equiv | `_pd2ppc` + `makeYbus` (pandapower internals) | Exact reference for the < 1e-9 gate; only needed at startup for verification |
| Gaussian noise generation | `random.gauss()` | `np.random.default_rng(seed).normal()` | Matches existing project seeded RNG pattern; `random.gauss` is non-deterministic across processes |

**Key insight:** The estimator math (h(x), H, predict/update) must be hand-rolled because it is tightly coupled to this network's state layout and the FASE predict architecture. However, all numerical primitives (cholesky, solve, chi2) come from scipy/numpy to avoid reimplementing fragile numerics.

---

## Common Pitfalls

### Pitfall 1: Enhanced Net Has 34 Buses, Not 33

**What goes wrong:** Code that initializes the state vector with dimension 66 (= 2×33) when the enhanced net has 34 buses (buses 0..32 = distribution + bus 33 = HV ext_grid). The Ybus from `_pd2ppc` is 34×34.
**Why it happens:** The SPEC says "33-bus feeder" and "~64 states"; assuming 33 buses gives 2×33-2 = 64 ✓, but the actual bus indices go 0..33 (34 buses).
**How to avoid:** State vector dimension = 64 = 2×32 free distribution-bus states (buses 0..32 minus slack). Bus 33 (HV) is the ext_grid slack: θ₃₃ = 0 (reference), |V|₃₃ = known regulated. The Ybus operates in 34-bus space; the estimator eliminates bus-33 rows/cols by fixing its state.
**Warning signs:** Ybus shape assertion fails: expected (34,34), got (33,33).

### Pitfall 2: pd2ppc Private API Changes

**What goes wrong:** Importing `from pandapower.pd2ppc import pd2ppc` fails with `ImportError: cannot import name 'pd2ppc'`.
**Why it happens:** In pandapower 3.x, the public `pd2ppc` function was replaced by `_pd2ppc` (underscore private). [VERIFIED: runtime test — ImportError confirmed on attempt; `_pd2ppc` works]
**How to avoid:** Use `from pandapower.pd2ppc import _pd2ppc` and unpack the 2-tuple: `ppc, ppci = _pd2ppc(net)`. Pass `ppci` (not `ppc`) to `makeYbus`. The numba warning about slow execution is harmless.
**Warning signs:** ImportError on `from pandapower.pd2ppc import pd2ppc`.

### Pitfall 3: paho-mqtt 2.x CallbackAPIVersion Deprecation Warning

**What goes wrong:** `mqtt.Client()` without `callback_api_version` prints a DeprecationWarning in paho 2.x about the default changing in a future version.
**Why it happens:** paho 2.x added `callback_api_version` as a required-intent parameter; the default is VERSION1 but with a warning.
**How to avoid:** Always pass `mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)` explicitly. [VERIFIED: paho-mqtt 2.1.0 source inspection]
**Warning signs:** DeprecationWarning at client construction.

### Pitfall 4: Retained Messages Delivered to Late Subscribers Immediately

**What goes wrong:** The `estimate` runner subscribes to `ieee33/netmodel/current` and starts processing meas messages before it has processed the retained netmodel config. If the Ybus is not initialized, the first snapshot produces garbage.
**Why it happens:** MQTT retained messages are delivered by the broker immediately on subscribe, but the `on_message` callback races with the subscriber's main loop.
**How to avoid:** The assembler must gate snapshot processing on `self._current_netmodel is not None`. The `estimate` runner subscribes to `netmodel/current` first, waits for the `on_message` callback to set `_current_netmodel`, then subscribes to meas topics. Or: subscribe to all topics but buffer meas messages until netmodel config is received.
**Warning signs:** First estimate has an all-zero or uninitialized Ybus.

### Pitfall 5: `energised` is an InfluxDB TAG, Not a Field

**What goes wrong:** Flux queries for the `fault_event` bucket miss the `energised` filter or read it as a field when it's a tag.
**Why it happens:** The `fault_event` schema sets `energised` as a TAG (`"1"`/`"0"` string). Flux `pivot` must include it in `rowKey` or it causes row multiplication. [CITED: influx.py `read_fault_bus` comments, D-02 in 09-CONTEXT.md]
**How to avoid:** The `score.py` harness reads `state` (no `energised` tag) and `fault_event` (has `energised` tag). Use the same `rowKey` pattern as `read_fault_bus`: `rowKey: ["_time", "bus_id", "energised"]`. Compare as string `"1"` not integer 1.
**Warning signs:** Duplicate rows in Flux result; energised appears as a column with unexpected values.

### Pitfall 6: Singular Gain Matrix G at realistic_sparse Real-Only

**What goes wrong:** `np.linalg.solve(G, ...)` raises `LinAlgError: Singular matrix` on the first WLS run with `realistic_sparse` and real measurements only.
**Why it happens:** Real-only redundancy < 1.0 → system is under-observable → G = HᵀWH is rank-deficient. [VERIFIED: measure.py footprint report confirms this]
**How to avoid:** Check rank before solve: `if np.linalg.matrix_rank(G) < G.shape[0]: raise RankDeficientError(...)`. The SPEC (R5) requires this to be reported, not silently handled. After adding pseudo rows, redundancy crosses 1.0 and G becomes full-rank.
**Warning signs:** `np.linalg.solve` raises LinAlgError on first WLS attempt; SPEC requires this to be caught and reported.

### Pitfall 7: FASE Sensitivity S — Two Valid Approaches

**What goes wrong:** Implementing S as the Moore-Penrose pseudoinverse of the full H gives a different result than the power-flow Jacobian inverse J_pf^{-1}, leading to poor predict accuracy.
**Why it happens:** S = ∂x/∂p is the sensitivity of state to injection, not the same as the WLS solution map.
**How to avoid:** S should be computed as the inverse (or pseudoinverse) of the **injection-only rows of H** evaluated at the current estimate, restricted to the injection-measurement block: `H_inj = H[injection_rows, :]`; then `S = H_inj^† = (H_inj^T H_inj)^{-1} H_inj^T` (if H_inj has full column rank). Alternatively: `S = pinv(H_inj)`. This is the linearized sensitivity of state to injection changes. Recompute S at each predict step using H evaluated at x̂_{k-1}. [ASSUMED — derived from FASE theory; verify numerically against a power-flow perturbation test]
**Warning signs:** Predict step produces voltage changes an order of magnitude too large or too small relative to the scheduled ramp.

### Pitfall 8: Acceleration Factor and Ordering Determinism

**What goes wrong:** With a fast acceleration factor, messages arrive at the subscriber out of timestamp order because paho's publish queue does not guarantee ordering across rapid publishes.
**Why it happens:** TCP streaming is ordered, but if the publisher issues many rapid publishes, the broker may interleave messages from different topic subscriptions.
**How to avoid:** Publish all messages for a single timestamp atomically (no sleep between messages within a snapshot); sleep only between snapshots. QoS 1 with a single connection guarantees in-order delivery within one connection's send queue. [ASSUMED — TCP ordering property; verify with a short test]
**Warning signs:** Snapshot assembler receives measurements from step k+1 before completing step k.

---

## Code Examples

### Mosquitto docker-compose service (R1)

```yaml
# Source: Mosquitto 2.0 documentation; verified image eclipse-mosquitto:2.0 available [VERIFIED: docker pull]
  mosquitto:
    image: eclipse-mosquitto:2.0
    ports:
      - "127.0.0.1:1883:1883"    # SECURITY: localhost only, not 0.0.0.0
    volumes:
      - ./mosquitto/config/mosquitto.conf:/mosquitto/config/mosquitto.conf
    restart: unless-stopped
```

```ini
# mosquitto/config/mosquitto.conf
listener 1883 127.0.0.1
allow_anonymous true
persistence true
persistence_location /mosquitto/data/
log_dest stdout
```

### Flux query for reading measurements bucket (reuse pattern from influx.py)

```python
# Source: influx.py read_fault_bus pattern [CITED: influx.py lines 651-667]
# For publish.py: read meas points from measurements bucket for a (scenario, source)
flux = (
    f'from(bucket: "measurements")\n'
    f'  |> range(start: {start}, stop: {stop})\n'
    f'  |> filter(fn: (r) => r._measurement == "meas")\n'
    f'  |> filter(fn: (r) => r.scenario == "{scenario}")\n'
    f'  |> filter(fn: (r) => r.experiment == "{experiment}")\n'
    f'  |> pivot(rowKey: ["_time", "class", "quantity", "location", "scenario", "experiment"], '
    f'     columnKey: ["_field"], valueColumn: "_value")\n'
    f'  |> sort(columns: ["_time", "class", "location"])'
)
```

**Important:** For fault source, `phase` is a TAG (not a field) on meas points and must be in `rowKey` if you need to read it. For the publisher, it is available as the `phase` column after pivot. [CITED: influx.py build_meas_point — `phase` is conditionally added as a tag]

### `estimates` bucket Point schema (R8)

```python
# Source: pattern from influx.py write_state_step [CITED: influx.py lines 277-285]
# Per-bus estimate point
Point("estimate")
    .tag("bus_id",    str(bus_idx))
    .tag("scenario",  scenario)
    .tag("experiment", experiment)
    .tag("estimator", estimator_name)   # "wls" | "ekf" | "ukf"
    .field("vm_pu_est",    float(vm_pu_est))
    .field("va_degree_est", float(va_degree_est))
    .field("sigma_vm",     float(sigma_vm))     # sqrt(P[2i, 2i])
    .field("sigma_va",     float(sigma_va))     # sqrt(P[2i+1, 2i+1]) * (180/pi)
    .time(timestamp)

# System-level trace_P point
Point("estimate_system")
    .tag("scenario",  scenario)
    .tag("experiment", experiment)
    .tag("estimator", estimator_name)
    .field("trace_P", float(np.trace(P)))   # ORACS observability index
    .time(timestamp)
```

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| paho-mqtt v1.x API | paho-mqtt 2.x with `CallbackAPIVersion` | paho 2.0 (2023) | Must pass `CallbackAPIVersion.VERSION1` explicitly or get DeprecationWarning |
| `pd2ppc` public function | `_pd2ppc` private (returns tuple) | pandapower 3.x | Must use `_pd2ppc` and unpack `(ppc, ppci)` |
| filterpy for UKF | hand-roll or scipy | N/A for this project | filterpy is not in venv; hand-roll preferred for control and determinism |
| Mosquitto 1.x | Mosquitto 2.0 | 2020 | Port 1883 listener config syntax changed; 2.0 requires explicit `listener` directive in mosquitto.conf |
| `pandapower.estimation.estimate()` | Custom AC-WLS | Always | pandapower's estimator uses its own measurement model (cannot inject MQTT stream or FASE predict) |

**Deprecated/outdated:**
- `from pandapower.pd2ppc import pd2ppc` (public): **ImportError in pandapower 3.x** — use `_pd2ppc` instead.
- `mqtt.Client()` without `callback_api_version`: deprecated in paho 2.x — pass `VERSION1` explicitly.
- `np.random.seed()` / `np.random.randn()` legacy API: project uses `np.random.default_rng(seed)`.

---

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | QoS 1 guarantees ordered delivery for a single-connection publisher to a local Mosquitto broker | Pattern 1 | Possible message reordering under high acceleration — add per-snapshot serial number or sort by (ts, class, loc) at the subscriber |
| A2 | Sigma-point defaults α=1e-3, β=2.0, κ=0.0 are suitable for 64-state voltage estimation | Pattern 7 | May need tuning if UKF diverges; start with α=0.1 if 1e-3 undersamples the sigma cloud |
| A3 | S = pinv(H_inj) is the correct FASE sensitivity matrix | Pattern 6 + Pitfall 7 | If S is wrong, the predict step will not beat persistence; verify against a linearized PF perturbation |
| A4 | Standard P = (I-KH)P in EKF is only wrong numerically, not mathematically | Pattern 6 | Joseph form is mandatory regardless; risk is divergence after 96 steps if numerical noise accumulates |
| A5 | filterpy is not in the project venv | Standard Stack | If it were available, it could provide UKF scaffolding; hand-roll is preferred regardless |
| A6 | `assumed_sigma` in the meas MQTT payload is the σ the estimator should use as R diagonal | AC Model (Pattern 4) | If the publisher sends `assumed_sigma` ≠ actual noise σ (`assumed_sigma_scale ≠ 1.0`), the filter will be miscalibrated intentionally; this is by design for robustness study |

---

## Open Questions (RESOLVED)

All three resolved during planning; the decisions are encoded in the PLAN.md files cited below.

1. **FASE sensitivity matrix S: pseudoinverse vs power-flow Jacobian inverse** — **RESOLVED (Plan 10-02):** weighted pseudoinverse `S = (H_injᵀ W_inj H_inj)⁻¹ H_injᵀ W_inj`, with `W_inj` from injection-sensor measurement noise. Links FASE prior quality to measurement quality.
   - What we know: S = ∂x/∂p; H_inj contains ∂p/∂x so S = H_inj⁻¹ conceptually.
   - Why: With m_inj > n (over-determined injection block), the weighted form is more principled than `pinv(H_inj)`.

2. **Q_floor magnitude** — **RESOLVED (Plan 10-01):** default `q_floor_scale = 1e-8` (·I, order of σ_pmu²), exposed as a config-tunable knob in `estimate_config.py`.
   - What we know: too small = P collapses at flat load (overconfident); too large = P inflates at steady state.
   - Diagnostic: trace_P should not collapse to < σ_pmu² after many steps.

3. **WLS initialization (flat start vs warm start)** — **RESOLVED (Plan 10-03):** flat start (`|V|=1.0 pu, θ=0`) for the WLS snapshot estimator; recursive EKF/UKF carry their own prior across steps.
   - What we know: Gauss-Newton can diverge from a poor starting point; flat start is standard for distribution networks with mild voltage deviations.
   - Note: OLTC-regulated + DER reverse flow keeps voltages near 1.0 pu (±0.05), so flat start is safe.

---

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Docker | Mosquitto broker | ✓ | 28.1.1 | None (Docker required) |
| eclipse-mosquitto:2.0 | R1 broker | ✓ | 2.0 (pulled) | — |
| paho-mqtt 2.1.0 | R2/R4 | ✓ (uv add applied) | 2.1.0 | — |
| pandapower 3.4.0 | Ybus extraction, network builder | ✓ | 3.4.0 [CITED: pyproject.toml] | — |
| numpy ≥1.26 | All matrix math | ✓ | in venv [CITED: pyproject.toml] | — |
| scipy (transitive) | cholesky, chi2 | ✓ [VERIFIED: runtime test] | — | — |
| InfluxDB 2.9.1 | All InfluxDB reads/writes | ✓ (docker compose) | 2.9.1 [CITED: docker-compose.yml] | — |
| Grafana 11.6.15 | Dashboards | ✓ (docker compose) | 11.6.15 [CITED: docker-compose.yml] | — |

No missing dependencies.

---

## Validation Architecture

Nyquist validation is DISABLED for this phase (`workflow.nyquist_validation` not found in config — **check `.planning/config.json`**). The SPEC already defines explicit acceptance criteria (RMSE, rank-deficiency detection, NEES/NIS bands) that are verified by the `score.py` harness rather than a unit test suite. The planner should map SPEC acceptance criteria to `score.py` assertions that exit non-zero on threshold miss.

---

## Security Domain

This is a local-dev interview-prep project. All services are localhost-bound. The SPEC states `security_enforcement` is not configured. Mosquitto is bound to `127.0.0.1:1883` only (no external exposure). No authentication required for local dev.

---

## Sources

### Primary (HIGH confidence)
- `system1-measurement-source/src/ieee33/network.py` — `build_enhanced_33bus()` full source; 34-bus layout; trafo HV bus confirmed [VERIFIED: file read + runtime test]
- `system1-measurement-source/src/ieee33/influx.py` — `build_meas_point`/`build_event_point` schema; `read_fault_bus` Flux pivot pattern; `ensure_bucket` [VERIFIED: file read]
- `system1-measurement-source/src/ieee33/measure.py` — runner skeleton; `_parse_args` + `_merge_cfg` CLI pattern; noise engine; sorted sensor iteration for determinism [VERIFIED: file read]
- `system1-measurement-source/src/ieee33/measure_config.py` — CLASS_SIGMA, CADENCE, SCENARIOS, ACTIVE block [VERIFIED: file read]
- `system1-measurement-source/pyproject.toml` — dep versions; existing scripts [VERIFIED: file read]
- `system1-measurement-source/docker-compose.yml` — InfluxDB 2.9.1, Grafana 11.6.15; service names [VERIFIED: file read]
- `.planning/phases/02-distribution-virtual-sensing/demo/dc_powerflow_baddata_demo.py` — `wls_solve`, `chi2_test`, `normalized_residuals` functions to lift [VERIFIED: file read; confirmed at path]
- Runtime tests: Ybus hand-build error = 4.02e-14 (< 1e-9 gate met); `_pd2ppc` 2-tuple return; 34-bus ppci; chi2 band values; scipy cholesky; paho-mqtt 2.1.0 VERSION1 API [VERIFIED: all runtime-tested in session]

### Secondary (MEDIUM confidence)
- paho-mqtt 2.1.0 source (`.venv/lib/python3.13/site-packages/paho/mqtt/client.py`) — VERSION1/VERSION2 enum, callback signatures, `CallbackAPIVersion` requirement [VERIFIED: grep of installed source]
- pandapower 3.4.0 pd2ppc module — `_pd2ppc` private function; return tuple signature [VERIFIED: grep + runtime test]
- eclipse-mosquitto:2.0 Docker image — pulled and confirmed [VERIFIED: docker pull + docker images]

### Tertiary (LOW confidence)
- FASE sensitivity matrix S = pinv(H_inj): derived from DSSE textbook knowledge; not independently verified against a power-flow perturbation test in this session [ASSUMED: A3]
- sigma-point parameter defaults (α=1e-3, β=2.0, κ=0.0): standard recommendation from Van der Merwe & Wan 2001; not tuned for 64-state distribution DSSE specifically [ASSUMED: A2]

---

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — all deps runtime-verified in project venv; paho 2.1.0, pandapower 3.4.0, scipy confirmed
- Architecture: HIGH — all integration points traced from existing code; 34-bus Ybus shape runtime-confirmed; patterns from existing modules verified
- Pitfalls: HIGH — all critical pitfalls discovered from runtime test failures (ImportError on pd2ppc, 34-bus surprise, etc.)
- Estimator math (FASE S, UKF params): MEDIUM — standard formulas cited but not numerically validated against a full run in this session

**Research date:** 2026-06-26
**Valid until:** 2026-07-26 (pandapower and paho APIs are stable; Mosquitto 2.0 is long-term stable)
