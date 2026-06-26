"""
estimate.py
-----------
System 2 streaming AC state estimator for the IEEE 33-bus observability study.
Subscribes to MQTT measurements and the retained netmodel/current topology,
assembles per-snapshot z vectors, and drives the selected estimator (wls|ekf|ukf).
Writes (x_hat, P, trace_P) to the 'estimates' InfluxDB bucket.

ORACLE SEPARATION: this module NEVER reads oracle buckets (state or fault_event).
Only measurements (via MQTT) + netmodel/current (via MQTT) + profiles (InfluxDB) are read.
Verified by grep: zero references to oracle read helpers or bucket constants in this file.

Run:  uv run estimate [--scenario ...] [--source ...] [--estimator wls|ekf|ukf] [--seed ...]
"""

import argparse
import hashlib
import json
import sys
import threading

import numpy as np
import paho.mqtt.client as mqtt
from influxdb_client.client.write_api import SYNCHRONOUS

import ieee33.estimate_config as ec
from ieee33 import ac_model, config, influx
from ieee33.estimators import EKFEstimator, RankDeficientError, UKFEstimator, WLSEstimator
from ieee33.fase_predict import FASEPredictor
from ieee33.network import build_enhanced_33bus


# ---------------------------------------------------------------------------
# CLI argument parsing (mirror measure.py lines 200-260)
# ---------------------------------------------------------------------------

def _parse_args():
    p = argparse.ArgumentParser(
        description="IEEE 33-bus AC state estimator runner — MQTT subscriber + FASE estimator."
    )
    p.add_argument(
        "--scenario",
        choices=["well_observed", "realistic_sparse"],
        default=None,
        help="Sensor-placement scenario (default: estimate_config.ACTIVE['scenario'])",
    )
    p.add_argument(
        "--source",
        choices=["day", "fault"],
        default=None,
        help="Data source: 'day' = 96-step day, 'fault' = 40-step fault "
             "(default: estimate_config.ACTIVE['source'])",
    )
    p.add_argument(
        "--estimator",
        choices=["wls", "ekf", "ukf"],
        default=None,
        help="Estimator to run — ONE per invocation (D-02) "
             "(default: estimate_config.ACTIVE['estimator'])",
    )
    p.add_argument(
        "--seed",
        type=int,
        default=None,
        help="RNG seed for forecast-error determinism "
             "(default: estimate_config.ACTIVE['seed'])",
    )
    p.add_argument(
        "--acceleration",
        type=float,
        default=None,
        help="Ignored by estimate.py (publish-side only); accepted for API parity",
    )
    return p.parse_args()


def _merge_cfg(args) -> dict:
    """Merge estimate_config.ACTIVE with non-None CLI overrides.

    Config file (ACTIVE block) is the primary switch (mirrors measure.py).
    CLI overrides applied on top for sweep runs.
    """
    cfg = dict(ec.ACTIVE)
    for key in ("scenario", "source", "estimator", "seed", "acceleration"):
        val = getattr(args, key, None)
        if val is not None:
            cfg[key] = val
    return cfg


# ---------------------------------------------------------------------------
# Deterministic per-bus forecast seed (mirrors measure.py _instrument_bias)
# ---------------------------------------------------------------------------

def _forecast_seed(bus_id: int, seed: int) -> int:
    """Deterministic per-bus forecast-error seed using sha256.

    Mirror of measure.py _instrument_bias hash derivation (lines 89-115).
    ALWAYS sha256 — not hash() which is PYTHONHASHSEED-randomized.
    """
    digest = hashlib.sha256(f"forecast_err|bus{bus_id}|{seed}".encode()).digest()
    return int.from_bytes(digest[:4], "big")


# ---------------------------------------------------------------------------
# MQTT Snapshot Assembler
# ---------------------------------------------------------------------------

class MQTTSnapshotAssembler:
    """Subscribe to MQTT broker; gate meas processing until netmodel received.

    Implements the retained-message race guard (PATTERNS Pitfall 4):
    - Subscribe to ieee33/netmodel/current FIRST (in on_connect)
    - Gate meas accumulation until _current_netmodel is not None
    - Rebuild Ybus on every config_version bump; set topology_change_pending flag
    - Buffer meas messages by timestamp into _snapshot_buffer
    """

    def __init__(self):
        self._current_netmodel: dict | None = None
        self._config_version: int = -1
        self._topology_change_pending: bool = False
        self._snapshot_buffer: dict = {}    # ts_str -> {(cls, loc): payload}
        self._lock = threading.Lock()

        # Ybus state (set by on_message when netmodel arrives/changes)
        self._Ybus: np.ndarray | None = None
        self._new_ybus_ready: threading.Event = threading.Event()

        # Static params (injected at startup by estimate.py main)
        self._static_params = None
        self._base_z_ohm: float = 0.0
        self._Y_trafo_fixed: np.ndarray | None = None
        self._all_line_ids: set | None = None

    def set_static_params(self, params, base_z_ohm, Y_trafo_fixed, all_line_ids):
        """Inject static line params from extract_static_line_params (called once at startup)."""
        self._static_params = params
        self._base_z_ohm = base_z_ohm
        self._Y_trafo_fixed = Y_trafo_fixed
        self._all_line_ids = all_line_ids

    def on_connect(self, client, userdata, flags, rc):
        """Subscribe to netmodel/current FIRST; then subscribe to meas wildcard.

        Order matters: subscribe to the retained topic first so the retained
        message is delivered before any meas messages, satisfying the gate
        (PATTERNS Pitfall 4).
        """
        client.subscribe("ieee33/netmodel/current", qos=1)
        # Subscribe to all meas topics for any experiment/scenario
        client.subscribe("ieee33/#", qos=1)

    def on_message(self, client, userdata, msg):
        """Handle incoming MQTT messages.

        Defensive: json.loads with key-presence check; skip+log malformed payloads.
        Threat model: untrusted MQTT payloads → validate keys before indexing.
        """
        try:
            payload = json.loads(msg.payload.decode("utf-8"))
        except Exception as exc:
            print(f"[WARN] estimate.py: malformed payload on {msg.topic}: {exc}", file=sys.stderr)
            return

        if msg.topic == "ieee33/netmodel/current":
            self._handle_netmodel(payload)
        elif "/meas/" in msg.topic:
            self._handle_meas(payload)
        # event topic messages (ieee33/.../event) are intentionally ignored —
        # topology changes are read via netmodel/current (the authoritative source)

    def _handle_netmodel(self, payload: dict):
        """Process a netmodel/current payload; rebuild Ybus on version change."""
        required_keys = {"config_version", "in_service_lines"}
        if not required_keys.issubset(payload.keys()):
            print(
                f"[WARN] estimate.py: netmodel payload missing keys "
                f"(got {list(payload.keys())}); skipping",
                file=sys.stderr,
            )
            return

        version = int(payload["config_version"])
        with self._lock:
            if version != self._config_version:
                self._config_version = version
                self._current_netmodel = payload

                # Rebuild Ybus from streamed in-service line set (R4 version-aware)
                if self._static_params is not None:
                    in_service = ac_model.topology_to_inservice(payload, self._all_line_ids)
                    self._Ybus = ac_model.build_ybus_from_topology(
                        self._static_params,
                        in_service,
                        ec.N_BUS_TOTAL,
                        self._base_z_ohm,
                        self._Y_trafo_fixed,
                    )
                    # Flag topology change so innovation jump is NOT mis-flagged as bad data (R4)
                    self._topology_change_pending = True
                    self._new_ybus_ready.set()

    def _handle_meas(self, payload: dict):
        """Buffer one meas message into _snapshot_buffer keyed by timestamp."""
        # Defensive key-presence check (threat model: malformed payload)
        for key in ("timestamp", "class", "location", "value", "assumed_sigma", "quantity"):
            if key not in payload:
                print(
                    f"[WARN] estimate.py: meas payload missing key '{key}'; "
                    f"skipping (keys={list(payload.keys())})",
                    file=sys.stderr,
                )
                return

        # Gate: only buffer meas after netmodel is received (Pitfall 4)
        with self._lock:
            if self._current_netmodel is None:
                return   # drop this message; will receive it via replay anyway

            ts = payload["timestamp"]
            cls = payload["class"]
            loc = payload["location"]
            self._snapshot_buffer.setdefault(ts, {})
            self._snapshot_buffer[ts][(cls, loc)] = payload

    def get_ready_snapshots(self, max_age_count: int = 1):
        """Return sorted list of (ts, meas_dict) pairs ready for processing.

        In a replay (publish.py) workflow all messages for a snapshot arrive
        close together; after a brief settling period we drain completed snapshots.
        Here we return all timestamps that have at least one entry, leaving the
        most recent one (possibly still accumulating) in the buffer.

        Returns list of (ts_str, {(cls, loc): payload}) pairs sorted by ts_str.
        Removes returned entries from the buffer.
        """
        with self._lock:
            if self._current_netmodel is None:
                return []
            all_ts = sorted(self._snapshot_buffer.keys())
            if len(all_ts) <= max_age_count:
                return []
            # Return all but the last max_age_count (still arriving) timestamps
            ready_ts = all_ts[:-max_age_count]
            result = []
            for ts in ready_ts:
                result.append((ts, self._snapshot_buffer.pop(ts)))
            return result

    def drain_all(self):
        """Return all remaining buffered snapshots (called at shutdown)."""
        with self._lock:
            all_ts = sorted(self._snapshot_buffer.keys())
            result = []
            for ts in all_ts:
                result.append((ts, self._snapshot_buffer.pop(ts)))
            return result

    @property
    def Ybus(self):
        with self._lock:
            return self._Ybus

    @property
    def topology_change_pending(self):
        with self._lock:
            return self._topology_change_pending

    def clear_topology_change(self):
        with self._lock:
            self._topology_change_pending = False

    @property
    def dead_buses(self) -> list:
        """Return de-energised bus list from current netmodel (empty for day source)."""
        with self._lock:
            if self._current_netmodel is None:
                return []
            return list(self._current_netmodel.get("dead_buses", []))

    @property
    def netmodel_received(self) -> bool:
        with self._lock:
            return self._current_netmodel is not None


# ---------------------------------------------------------------------------
# Measurement list builder from snapshot buffer
# ---------------------------------------------------------------------------

def _build_meas_list_and_vectors(snap_msgs: dict):
    """Convert a snapshot's {(cls, loc): payload} dict into meas_list, z, R.

    Parameters
    ----------
    snap_msgs : dict {(cls_str, loc_str): payload_dict}
        One snapshot's measurement payloads in arbitrary order.

    Returns
    -------
    meas_list : list of (cls, quantity, bus_idx) tuples — fixed ordering
    z         : np.ndarray shape (m,)  measurement values
    R         : np.ndarray shape (m,m)  diagonal noise covariance (assumed_sigma²)

    Notes
    -----
    Ordering: sort by (cls, loc) for determinism (mirrors publish.py Flux sort).
    location is a bus index string — convert to int for bus_idx.
    """
    sorted_keys = sorted(snap_msgs.keys())   # (cls, loc) sorted lexicographically
    meas_list = []
    z_vals = []
    sigma_vals = []

    for (cls, loc) in sorted_keys:
        p = snap_msgs[(cls, loc)]
        quantity = str(p.get("quantity", ""))
        try:
            bus_idx = int(str(loc))
        except ValueError:
            # Non-integer location (e.g. line id) — skip; this estimator is bus-state only
            continue

        value = float(p.get("value", float("nan")))
        assumed_sigma = float(p.get("assumed_sigma", 1.0))

        if not (
            isinstance(value, float) and value == value  # NaN check
            and assumed_sigma > 0
            and quantity
        ):
            continue

        meas_list.append((cls, quantity, bus_idx))
        z_vals.append(value)
        sigma_vals.append(assumed_sigma)

    if not meas_list:
        return [], np.array([]), np.empty((0, 0))

    z = np.array(z_vals)
    R = np.diag(np.array(sigma_vals) ** 2)
    return meas_list, z, R


def _injection_meas_list(meas_list):
    """Extract injection-type measurements from meas_list for FASE sensitivity."""
    inj_quantities = {"p_inj_mw", "q_inj_mvar", "p_mw", "q_mvar"}
    return [(cls, qty, bus) for cls, qty, bus in meas_list if qty in inj_quantities]


# ---------------------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------------------

def main():
    import time as _time

    args = _parse_args()
    cfg = _merge_cfg(args)

    scenario    = cfg["scenario"]
    source      = cfg["source"]
    estimator_name = cfg["estimator"]
    seed        = int(cfg["seed"])

    # experiment tag = source name (Day 9 convention mirrors publish.py)
    experiment = source

    print(f"\nIEEE 33-bus AC State Estimator (System 2)")
    print(f"  scenario   : {scenario}")
    print(f"  source     : {source}")
    print(f"  experiment : {experiment}")
    print(f"  estimator  : {estimator_name}  (D-02: one per run, tagged in estimates bucket)")
    print(f"  seed       : {seed}")

    # ---- startup: build network + extract static params ----
    print("\nBuilding IEEE 33-bus network and verifying AC model ...")
    net, _trafo_idx = build_enhanced_33bus()

    # Startup verification gate (SPEC R3 — three gates)
    print("  Running verify_model ...")
    ac_model.verify_model(net)

    params, base_z_ohm, ppci = ac_model.extract_static_line_params(net)
    Y_trafo_fixed = ac_model.compute_trafo_fixed(params, base_z_ohm, ppci)
    all_line_ids = set(net.line.index)
    n_bus_est = ec.N_FREE_STATES // 2 + 1   # 33: buses 0..32 (66 state entries)
    # N_FREE_STATES = 64 = 2*(33-1) ... state vector is 66 entries (2*33 buses)
    n_state = ec.N_FREE_STATES + 2   # 66: interleaved [|V|_0, theta_0, ..., |V|_32, theta_32]

    # ---- InfluxDB setup ----
    print(f"\nConnecting to InfluxDB at {config.INFLUXDB_URL} ...")
    client = influx.get_client()
    influx.wait_for_influx()
    influx.ensure_bucket(client, ec.ESTIMATES_BUCKET)
    write_api = client.write_api(write_options=SYNCHRONOUS)

    # ---- read profiles at startup (D-06: allowed, not oracle) ----
    print("\nReading profiles from InfluxDB ...")
    prof_df = influx.read_profiles(client)
    print(f"  Loaded {len(prof_df)} profile steps")

    # ---- seeded RNG (determinism norm; mirrors measure.py line 687) ----
    rng = np.random.default_rng(seed)   # single instance, before any loop

    # ---- instantiate estimator (D-02: ONE per run, selected by --estimator) ----
    if estimator_name == "wls":
        estimator = WLSEstimator(n=n_state)
    elif estimator_name == "ekf":
        estimator = EKFEstimator(n=n_state)
    else:
        estimator = UKFEstimator(n=n_state)

    # ---- FASE predictor (uses profiles) ----
    fase_predictor = FASEPredictor(prof_df, cfg, rng, n_bus_est)

    # ---- MQTT subscriber + snapshot assembler ----
    assembler = MQTTSnapshotAssembler()
    assembler.set_static_params(params, base_z_ohm, Y_trafo_fixed, all_line_ids)

    mqtt_client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
    mqtt_client.on_connect = assembler.on_connect
    mqtt_client.on_message = assembler.on_message

    print(f"\nConnecting to MQTT broker at 127.0.0.1:1883 ...")
    mqtt_client.connect("127.0.0.1", 1883, keepalive=60)
    mqtt_client.loop_start()

    issues: list[str] = []

    # ---- console table header (mirrors measure.py lines 711-715) ----
    print(f"\n{'Step':>4}  {'UTC Time':<24}  {'Est':>5}  {'trP':>12}  {'nis_k':>10}  {'RMSE-proxy':>10}")
    print("-" * 80)

    step_idx = 0
    x_prev = None
    max_steps = 200   # safety cap (96-step day + 40-step fault with margin)
    poll_interval_s = 0.1   # main loop poll interval

    # Wait for netmodel before starting main loop (counter-based, no wall-clock read)
    # 600 iterations × 0.05 s = 30 s timeout
    print("  Waiting for netmodel/current from broker ...")
    _wait_iters = 0
    _wait_limit = 600  # 30 s at 0.05 s sleep
    while not assembler.netmodel_received:
        if _wait_iters >= _wait_limit:
            print(
                "[ERROR] estimate.py: did not receive netmodel/current within 30s. "
                "Is publish.py running?",
                file=sys.stderr,
            )
            issues.append("Timed out waiting for netmodel/current")
            break
        _time.sleep(0.05)
        _wait_iters += 1

    if assembler.netmodel_received:
        print("  netmodel/current received — starting estimation loop")

    # ---- main estimation loop ----
    # Poll for completed snapshots; process in timestamp order
    # Stop when no new messages arrive for a settling period
    idle_count = 0
    idle_limit = 50   # ~5 s at 0.1 s poll interval without new data -> drain + exit

    while step_idx < max_steps:
        __import__("time").sleep(poll_interval_s)

        ready = assembler.get_ready_snapshots(max_age_count=1)
        if not ready:
            idle_count += 1
            if idle_count >= idle_limit:
                # Drain any remaining snapshots and exit
                ready = assembler.drain_all()
                if ready:
                    idle_count = 0   # reset — process remaining
                else:
                    break   # truly idle; all data consumed
        else:
            idle_count = 0

        for ts_str, snap_msgs in ready:
            if step_idx >= max_steps:
                break

            # ---- topology change flag handling (R4) ----
            is_topology_change = assembler.topology_change_pending
            if is_topology_change:
                assembler.clear_topology_change()

            Ybus = assembler.Ybus
            if Ybus is None:
                issues.append(f"Step {step_idx}: Ybus is None (netmodel not yet received)")
                continue

            # ---- dead-bus mask (R12) ----
            dead_buses = set(assembler.dead_buses)
            energised_mask = np.ones(n_bus_est, dtype=bool)
            for db in dead_buses:
                if 0 <= db < n_bus_est:
                    energised_mask[db] = False

            # ---- build meas_list, z, R ----
            meas_list, z, R = _build_meas_list_and_vectors(snap_msgs)

            if len(meas_list) == 0:
                print(f"{step_idx:>4}  {ts_str[:24]:<24}  -- (no valid meas in snapshot)")
                step_idx += 1
                continue

            # ---- closures binding current Ybus (thread-safe snapshot) ----
            _Ybus_snap = Ybus
            _ml_snap = meas_list

            def h_fn(xv, _Y=_Ybus_snap, _ml=_ml_snap):
                return ac_model.h_func(xv, _Y, _ml)

            def H_fn(xv, _Y=_Ybus_snap, _ml=_ml_snap):
                return ac_model.jacobian_H(xv, _Y, _ml)

            # ---- FASE predict (EKF/UKF only; WLS is a no-op) ----
            if x_prev is None:
                x_prev = estimator.x.copy()

            if estimator_name in ("ekf", "ukf"):
                # Build injection-only meas subset for FASE sensitivity
                inj_ml = _injection_meas_list(meas_list)
                if inj_ml:
                    # Weight matrix for injection meas (diagonal 1/sigma^2)
                    sigma_inj = np.array([
                        float(snap_msgs[(cls, str(bus))].get("assumed_sigma", 1.0))
                        for cls, _, bus in inj_ml
                        if (cls, str(bus)) in snap_msgs
                    ])
                    # Fallback: use uniform weights if sigma extraction fails shape-wise
                    if len(sigma_inj) != len(inj_ml):
                        sigma_inj = np.ones(len(inj_ml))
                    W_inj = np.diag(1.0 / sigma_inj ** 2)
                    S = ac_model.fase_sensitivity(x_prev, _Ybus_snap, inj_ml, W_inj)
                else:
                    S = np.zeros((n_state, 0))

                x_minus, Q = fase_predictor.predict(
                    step_k=step_idx,
                    x_prev=x_prev,
                    S=S,
                )
                # Inject FASE-computed prior (x_minus, Q) directly into estimator.
                # FASEPredictor encapsulates the AR(1) logic and returns the full
                # (x_minus, Q) pair — we set the estimator's internal prior directly
                # rather than re-decomposing Q back into (delta_p, S, Cov_eps) form.
                _apply_prior_to_estimator(estimator, estimator_name, x_minus, Q)

            # ---- update (fuse measurements) ----
            nis_k = None
            m_k = None
            try:
                if estimator_name == "wls":
                    estimator.update(z, R, h_fn, H_fn)
                    # WLS: no innovation sequence; NIS is not defined (D-02, R11)
                elif estimator_name == "ekf":
                    y_k, S_inn = estimator.update(z, R, h_fn, H_fn)
                    # R11: faithful per-step NIS via solve, NOT explicit inverse
                    nis_k = float(y_k @ np.linalg.solve(S_inn, y_k))
                    m_k = int(y_k.shape[0])
                else:  # ukf
                    y_k, Pzz = estimator.update(z, R, h_fn, H_fn)
                    # R11: faithful per-step NIS via solve, NOT explicit inverse
                    nis_k = float(y_k @ np.linalg.solve(Pzz, y_k))
                    m_k = int(y_k.shape[0])
            except RankDeficientError as exc:
                print(
                    f"[WARN] Step {step_idx}: RankDeficientError — {exc}; "
                    "skipping write for this snapshot",
                    file=sys.stderr,
                )
                step_idx += 1
                continue
            except np.linalg.LinAlgError as exc:
                print(
                    f"[WARN] Step {step_idx}: LinAlgError in estimator update — {exc}; "
                    "skipping write for this snapshot",
                    file=sys.stderr,
                )
                step_idx += 1
                continue

            x_hat = estimator.x
            P = estimator.P
            x_prev = x_hat.copy()

            # ---- console row: RMSE-proxy = sqrt(trace(P)/n_state) ----
            trace_P = float(np.trace(P))
            rmse_proxy = float(np.sqrt(abs(trace_P) / max(n_state, 1)))
            nis_str = f"{nis_k:>10.3f}" if nis_k is not None else "         —"
            topo_flag = " [TOPO]" if is_topology_change else ""
            print(
                f"{step_idx:>4}  {ts_str[:24]:<24}  {estimator_name:>5}  "
                f"{trace_P:>12.4f}  {nis_str}  {rmse_proxy:>10.6f}{topo_flag}"
            )

            # ---- parse timestamp for InfluxDB write ----
            ts_for_influx = _parse_ts(ts_str)

            # ---- write to estimates bucket ----
            influx.write_estimate_step(
                write_api=write_api,
                timestamp=ts_for_influx,
                x_hat=x_hat,
                P=P,
                scenario=scenario,
                experiment=experiment,
                estimator=estimator_name,
                energised_mask=energised_mask,
                nis_k=nis_k,
                m_k=m_k,
            )

            step_idx += 1

    # ---- graceful shutdown ----
    mqtt_client.loop_stop()
    mqtt_client.disconnect()

    # ---- fail-loud gate (mirror measure.py lines 896-902) ----
    if issues:
        print("--- ESTIMATE VALIDATION FAILED ---", file=sys.stderr)
        for issue in issues:
            print(f"  {issue}", file=sys.stderr)
        client.close()
        sys.exit(1)

    client.close()
    print(f"\nEstimate complete: {step_idx} snapshots written to '{ec.ESTIMATES_BUCKET}' bucket")
    print(f"  Estimator : {estimator_name}  Scenario: {scenario}  Source: {source}")


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _apply_prior_to_estimator(estimator, estimator_name: str, x_minus: np.ndarray, Q: np.ndarray):
    """Inject FASE-computed prior (x_minus, Q) directly into EKF/UKF internal state.

    FASEPredictor encapsulates the full AR(1) logic and returns (x_minus, Q).
    We set the estimator's prior directly rather than re-decomposing Q back
    into (delta_p, S, Cov_eps) form, which would require re-running the
    inverse — adding numerical error and defeating the purpose of the predictor.

    For EKF: sets _x = x_minus; _P = _P + Q (FASE covariance inflation rule).
    For UKF: sets _x = x_minus; updates _S_P from (_S_P @ _S_P.T + Q).
    """
    if estimator_name == "ekf":
        estimator._x = x_minus.copy()
        estimator._P = estimator._P + Q
    else:
        # UKF — update Cholesky factor
        from scipy.linalg import cholesky as _chol
        estimator._x = x_minus.copy()
        P_pred = estimator._S_P @ estimator._S_P.T + Q
        M = (P_pred + P_pred.T) / 2.0
        try:
            estimator._S_P = _chol(M, lower=True)
        except Exception:
            M_jit = M + np.eye(M.shape[0]) * 1e-8
            estimator._S_P = _chol((M_jit + M_jit.T) / 2.0, lower=True)


def _parse_ts(ts_str: str):
    """Parse an ISO 8601 timestamp string into a UTC-aware datetime.

    Handles both 'Z' suffix and '+00:00' offset forms (pandas Timestamp.isoformat).
    Returns a datetime usable as InfluxDB Point .time() argument.

    No wall-clock read: timestamps come EXCLUSIVELY from MQTT payloads (R13 determinism).
    """
    from datetime import datetime, timezone

    ts_str = ts_str.strip()
    # Normalize: replace Z suffix with +00:00 for fromisoformat (Python 3.11+: Z supported;
    # 3.10 and below need manual replacement)
    if ts_str.endswith("Z"):
        ts_str = ts_str[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(ts_str)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except ValueError:
        # Fallback: pandas Timestamp parsing (handles most ISO formats)
        import pandas as pd
        return pd.Timestamp(ts_str, tz="UTC").to_pydatetime()


if __name__ == "__main__":
    main()
