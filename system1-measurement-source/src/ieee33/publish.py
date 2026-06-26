"""
publish.py
----------
Replay publisher for the IEEE 33-bus System 2 observability study.
Reads measurements + event points for a chosen (scenario, source) from
InfluxDB in deterministic order (sorted by timestamp, class, location),
and publishes each as an MQTT message to the Mosquitto broker.

Also publishes the network topology config to the RETAINED versioned topic
ieee33/netmodel/current before any measurement messages.  A late-subscribing
client receives the retained config immediately upon subscribe.

Determinism note: Flux queries sorted by (_time, class, location); same
config produces identical publish order.  Acceleration factor compresses
wall-clock; no wall-clock reads in deterministic payload paths.

Run:  uv run publish [--scenario ...] [--source ...] [--seed ...] [--acceleration ...]
"""

import argparse
import json
import sys
import time

import numpy as np
import paho.mqtt.client as mqtt

import ieee33.estimate_config as ec
from ieee33 import config, influx

# ---------------------------------------------------------------------------
# Fault topology constants (mirrors Phase 8.1 definitions)
# ---------------------------------------------------------------------------
_FAULT_LINE_IDX   = 7              # faulted distribution line (pandapower line index)
_FAULT_DEAD_BUSES = list(range(8, 18))  # buses 8..17 de-energised when line 7 faults
_TIE_LINE_IDX     = 34            # tie line (pandapower index 34) closed on restore

# Distribution lines in steady-state (lines 0..31; tie lines 32-34 are open)
_DAY_IN_SERVICE   = list(range(32))   # 32 distribution lines always in service for day


# ---------------------------------------------------------------------------
# CLI argument parsing (mirror measure.py lines 200-260)
# ---------------------------------------------------------------------------

def _parse_args():
    p = argparse.ArgumentParser(
        description="IEEE 33-bus replay publisher — reads measurements, emits MQTT."
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
        help="Data source: 'day' = 96-step day experiment, "
             "'fault' = 40-step fault experiment "
             "(default: estimate_config.ACTIVE['source'])",
    )
    p.add_argument(
        "--seed",
        type=int,
        default=None,
        help="RNG seed (default: estimate_config.ACTIVE['seed'])",
    )
    p.add_argument(
        "--acceleration",
        type=float,
        default=None,
        help="Wall-clock playback compression factor "
             "(default: estimate_config.ACTIVE['acceleration'])",
    )
    return p.parse_args()


def _merge_cfg(args) -> dict:
    """Merge estimate_config.ACTIVE with non-None CLI overrides.

    Config file (ACTIVE block) is the primary switch (mirrors measure.py).
    CLI overrides are applied on top for sweep runs.

    Args:
        args: Parsed argparse.Namespace from _parse_args().

    Returns:
        cfg dict with all ACTIVE keys; CLI values override where provided.
    """
    cfg = dict(ec.ACTIVE)   # start from the config file
    for key in ("scenario", "source", "seed", "acceleration"):
        val = getattr(args, key, None)
        if val is not None:
            cfg[key] = val
    return cfg


# ---------------------------------------------------------------------------
# Netmodel topology config builders
# ---------------------------------------------------------------------------

def _build_day_netmodel(ts_iso: str) -> dict:
    """Return the single steady-state netmodel config for source=day.

    One config, version=0: all 32 distribution lines in service,
    no tie closed, no dead buses, phase='steady_state'.
    """
    return {
        "config_version": 0,
        "in_service_lines": _DAY_IN_SERVICE,
        "tie_closed": False,
        "tie_id": -1,
        "dead_buses": [],
        "phase": "steady_state",
        "timestamp": ts_iso,
    }


def _fault_netmodel_for_phase(phase: str, ts_iso: str, config_version: int) -> dict:
    """Return the netmodel config for a given fault phase.

    Three phases with distinct config_versions:
      pre_fault (v0):           all 32 lines in service, no tie, no dead buses
      faulted_isolated (v1):    line 7 removed, buses 8-17 dead
      restored (v2):            line 7 still out, tie 34 closed, no dead buses
    """
    if phase == "pre_fault":
        return {
            "config_version": config_version,
            "in_service_lines": _DAY_IN_SERVICE,    # lines 0..31
            "tie_closed": False,
            "tie_id": -1,
            "dead_buses": [],
            "phase": phase,
            "timestamp": ts_iso,
        }
    elif phase == "faulted_isolated":
        in_service = [idx for idx in _DAY_IN_SERVICE if idx != _FAULT_LINE_IDX]
        return {
            "config_version": config_version,
            "in_service_lines": in_service,
            "tie_closed": False,
            "tie_id": -1,
            "dead_buses": _FAULT_DEAD_BUSES,
            "phase": phase,
            "timestamp": ts_iso,
        }
    elif phase == "restored":
        in_service = [idx for idx in _DAY_IN_SERVICE if idx != _FAULT_LINE_IDX]
        return {
            "config_version": config_version,
            "in_service_lines": in_service,
            "tie_closed": True,
            "tie_id": _TIE_LINE_IDX,
            "dead_buses": [],
            "phase": phase,
            "timestamp": ts_iso,
        }
    else:
        # Fallback: treat unknown phases as steady_state topology
        return {
            "config_version": config_version,
            "in_service_lines": _DAY_IN_SERVICE,
            "tie_closed": False,
            "tie_id": -1,
            "dead_buses": [],
            "phase": phase,
            "timestamp": ts_iso,
        }


# ---------------------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------------------

def main():
    args = _parse_args()
    cfg  = _merge_cfg(args)

    scenario    = cfg["scenario"]
    source      = cfg["source"]
    acceleration = float(cfg["acceleration"])
    seed        = cfg["seed"]

    # experiment tag in the measurements bucket matches source name (Phase 9 convention)
    experiment = source   # "day" or "fault"

    print(f"\nIEEE 33-bus MQTT Replay Publisher")
    print(f"  scenario    : {scenario}")
    print(f"  source      : {source}")
    print(f"  experiment  : {experiment}")
    print(f"  acceleration: {acceleration}x")
    print(f"  seed        : {seed}")

    # ---- seeded RNG (determinism norm; publisher is otherwise deterministic) ----
    # Publisher payloads come from InfluxDB and ordering is fixed — RNG is
    # present for future use (e.g., jitter injection) and to satisfy the norm.
    rng = np.random.default_rng(seed)  # noqa: F841 — kept for future extensions

    # ---- connect to InfluxDB ----
    print(f"\nConnecting to InfluxDB at {config.INFLUXDB_URL} ...")
    client = influx.get_client()
    influx.wait_for_influx()
    # No ensure_bucket: measurements bucket pre-exists (Phase 9 wrote it)

    # ---- read measurements from bucket ----
    print(f"\nReading measurements (scenario={scenario}, experiment={experiment}) ...")
    meas_df = influx.read_measurements(client, scenario, experiment)
    print(f"  Loaded {len(meas_df)} meas rows from bucket")

    # ---- read event points for this experiment ----
    # Event points are also in the measurements bucket (Phase 9 D-07 re-publish)
    # We query them separately to build per-step event payloads.
    event_df = _read_events(client, scenario, experiment)
    print(f"  Loaded {len(event_df)} event rows from bucket")

    # ---- group meas rows by timestamp ----
    # _time is already the InfluxDB timestamp; convert to ISO string for payload
    if "_time" not in meas_df.columns:
        raise RuntimeError(
            "read_measurements returned DataFrame without '_time' column. "
            "Check Flux pivot rowKey configuration."
        )
    timestamps = sorted(meas_df["_time"].unique())
    n_steps = len(timestamps)
    print(f"  Found {n_steps} snapshots")

    if n_steps == 0:
        issues = [f"No measurement snapshots found for scenario={scenario}, experiment={experiment}"]
        print("--- PUBLISH VALIDATION FAILED ---", file=sys.stderr)
        for issue in issues:
            print(f"  {issue}", file=sys.stderr)
        client.close()
        sys.exit(1)

    # Estimate step duration (for acceleration sleep)
    if n_steps > 1:
        t0 = timestamps[0]
        t1 = timestamps[1]
        dt_ns = float(t1.value - t0.value)   # pandas Timestamp.value = ns
        step_duration_s = dt_ns / 1e9
    else:
        step_duration_s = 1.0   # fallback

    # ---- paho MQTT client ----
    print(f"\nConnecting to MQTT broker at 127.0.0.1:1883 ...")
    mqtt_client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
    mqtt_client.connect("127.0.0.1", 1883, keepalive=60)
    mqtt_client.loop_start()

    issues: list[str] = []

    # ---- STEP 1: publish retained netmodel/current BEFORE any meas ----
    # For source=day: one config, version=0 (steady-state topology)
    # For source=fault: publish pre_fault config first; republish on topology change below
    first_ts_iso = _ts_to_iso(timestamps[0])
    if source == "day":
        netmodel = _build_day_netmodel(first_ts_iso)
        _publish_netmodel(mqtt_client, netmodel)
        current_config_version = 0
    else:
        # Fault: determine initial phase from event data
        first_phase = _phase_for_step(event_df, timestamps[0])
        netmodel = _fault_netmodel_for_phase(first_phase, first_ts_iso, config_version=0)
        _publish_netmodel(mqtt_client, netmodel)
        current_config_version = 0
        _last_published_phase = first_phase

    # ---- STEP 2: console table header ----
    print(f"\n{'Step':>4}  {'UTC Time':<20}  {'Msgs':>5}  {'Config':>8}")
    print("-" * 62)

    # ---- STEP 3: publish meas + event in per-step order ----
    for step_idx, ts in enumerate(timestamps):
        ts_iso = _ts_to_iso(ts)

        # ---- fault: republish netmodel on topology phase change ----
        if source == "fault":
            phase = _phase_for_step(event_df, ts)
            if phase != _last_published_phase:
                current_config_version += 1
                netmodel = _fault_netmodel_for_phase(phase, ts_iso, current_config_version)
                _publish_netmodel(mqtt_client, netmodel)
                _last_published_phase = phase

        # ---- collect meas rows for this timestamp ----
        snap = meas_df[meas_df["_time"] == ts]

        # snap is already sorted by (class, location) from the Flux sort — confirm
        # and group for deterministic publish order: (class, location)
        n_msgs = 0

        # Publish meas points in fixed order (already sorted by Flux: _time, class, location)
        for _, row in snap.iterrows():
            cls      = str(row.get("class", ""))
            location = str(row.get("location", ""))
            quantity = str(row.get("quantity", ""))
            value    = float(row.get("value", float("nan")))
            assumed_sigma = float(row.get("assumed_sigma", float("nan")))

            # Build phase field (None for day; string for fault)
            phase_tag = str(row.get("phase", "")) if source == "fault" and "phase" in row.index else None
            if phase_tag == "nan" or phase_tag == "":
                phase_tag = None

            payload = {
                "value":         value,
                "assumed_sigma": assumed_sigma,
                "quantity":      quantity,
                "class":         cls,
                "location":      location,
                "experiment":    experiment,
                "scenario":      scenario,
                "phase":         phase_tag if phase_tag else ("steady_state" if source == "day" else ""),
                "timestamp":     ts_iso,
            }

            topic = f"ieee33/{experiment}/{scenario}/meas/{cls}/{location}"
            mqtt_client.publish(topic, json.dumps(payload), qos=1, retain=False)
            n_msgs += 1

        # Publish one event message per snapshot
        event_payload = _build_event_payload(event_df, ts, experiment, scenario, ts_iso, source)
        event_topic = f"ieee33/{experiment}/{scenario}/event"
        mqtt_client.publish(event_topic, json.dumps(event_payload), qos=1, retain=False)
        n_msgs += 1

        # Console row
        print(
            f"{step_idx:>4}  {str(ts)[:19]:<20}  {n_msgs:>5}  v{current_config_version:>6}"
        )

        # Acceleration sleep — BETWEEN snapshots only (Pitfall 8: no sleep within snapshot)
        # time.sleep is the ONLY wall-clock call; payloads use InfluxDB timestamps only
        if acceleration > 0 and step_idx < n_steps - 1:
            time.sleep(step_duration_s / acceleration)

    # ---- fail-loud gate (mirror measure.py lines 896-902) ----
    if issues:
        print("--- PUBLISH VALIDATION FAILED ---", file=sys.stderr)
        for issue in issues:
            print(f"  {issue}", file=sys.stderr)
        mqtt_client.loop_stop()
        mqtt_client.disconnect()
        client.close()
        sys.exit(1)

    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    client.close()

    print(f"\nPublish complete: {n_steps} snapshots, {len(meas_df)} meas messages")
    print(f"  Netmodel configs published: {current_config_version + 1} version(s)")


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _publish_netmodel(mqtt_client, netmodel: dict) -> None:
    """Publish the topology config to ieee33/netmodel/current with retain=True."""
    mqtt_client.publish(
        "ieee33/netmodel/current",
        json.dumps(netmodel),
        qos=1,
        retain=True,
    )


def _ts_to_iso(ts) -> str:
    """Convert a pandas Timestamp to ISO 8601 string (UTC)."""
    try:
        return ts.isoformat()
    except AttributeError:
        return str(ts)


def _read_events(client, scenario: str, experiment: str):
    """Read event points from the measurements bucket for (scenario, experiment).

    Event points (measurement="event") are written by Phase 9 measure.py (D-07)
    alongside meas points.  They carry fault topology metadata per snapshot.

    For source=day: all events have phase="steady_state" and faulted_line_id=-1.
    For source=fault: phases are pre_fault / faulted_isolated / restored.

    Returns a pandas.DataFrame or empty DataFrame if none found.
    """
    from datetime import date as _date, timedelta as _td

    start = f"{config.TARGET_DATE}T00:00:00Z"
    next_day = (_date.fromisoformat(config.TARGET_DATE) + _td(days=1)).isoformat()
    stop = f"{next_day}T00:00:00Z"

    # phase is a TAG on event points — must be in rowKey (mirrors read_fault_event pattern)
    flux = (
        f'from(bucket: "{config.MEASUREMENTS_BUCKET}")\n'
        f'  |> range(start: {start}, stop: {stop})\n'
        f'  |> filter(fn: (r) => r._measurement == "event")\n'
        f'  |> filter(fn: (r) => r.scenario == "{scenario}")\n'
        f'  |> filter(fn: (r) => r.experiment == "{experiment}")\n'
        f'  |> pivot(rowKey: ["_time", "phase", "scenario", "experiment"], '
        f'columnKey: ["_field"], valueColumn: "_value")\n'
        f'  |> sort(columns: ["_time"])'
    )
    try:
        df = client.query_api().query_data_frame(flux)
        if df is None or (hasattr(df, "__len__") and len(df) == 0):
            return _empty_event_df()
        return df
    except Exception:
        return _empty_event_df()


def _empty_event_df():
    """Return an empty DataFrame with expected event columns."""
    import pandas as pd

    return pd.DataFrame(columns=[
        "_time", "phase", "scenario", "experiment",
        "faulted_line_id", "tie_closed", "tie_id", "n_dead_buses", "dead_buses",
    ])


def _phase_for_step(event_df, ts) -> str:
    """Return the fault phase for a given timestamp from the event DataFrame."""
    if event_df is None or len(event_df) == 0:
        return "steady_state"
    snap = event_df[event_df["_time"] == ts]
    if len(snap) == 0:
        # Fall back to the most recent event before this ts
        past = event_df[event_df["_time"] <= ts]
        if len(past) > 0:
            snap = past.iloc[[-1]]
        else:
            return "steady_state"
    phase_val = snap.iloc[0].get("phase", "steady_state")
    if phase_val is None or str(phase_val) in ("", "nan"):
        return "steady_state"
    return str(phase_val)


def _build_event_payload(
    event_df, ts, experiment: str, scenario: str, ts_iso: str, source: str
) -> dict:
    """Build the event payload dict for a given timestamp.

    Mirrors Phase 9's event point schema (P9 event fields).
    """
    if event_df is None or len(event_df) == 0:
        return _steady_state_event(experiment, scenario, ts_iso)

    snap = event_df[event_df["_time"] == ts]
    if len(snap) == 0:
        past = event_df[event_df["_time"] <= ts]
        if len(past) > 0:
            snap = past.iloc[[-1]]
        else:
            return _steady_state_event(experiment, scenario, ts_iso)

    row = snap.iloc[0]

    def _safe_int(val, default=-1):
        try:
            return int(val)
        except (TypeError, ValueError):
            return default

    def _safe_str(val, default=""):
        if val is None or (isinstance(val, float) and str(val) == "nan"):
            return default
        return str(val)

    faulted_line_id = _safe_int(row.get("faulted_line_id", -1))
    tie_closed      = _safe_int(row.get("tie_closed", 0))
    tie_id          = _safe_int(row.get("tie_id", -1))
    n_dead_buses    = _safe_int(row.get("n_dead_buses", 0))
    dead_buses_str  = _safe_str(row.get("dead_buses", ""))

    # Parse dead_buses from comma-joined string to list of ints
    if dead_buses_str:
        try:
            dead_buses = [int(b) for b in dead_buses_str.split(",") if b.strip()]
        except ValueError:
            dead_buses = []
    else:
        dead_buses = []

    phase = _safe_str(row.get("phase", "steady_state"), default="steady_state")

    return {
        "faulted_line_id": faulted_line_id,
        "tie_closed":      bool(tie_closed),
        "tie_id":          tie_id,
        "n_dead_buses":    n_dead_buses,
        "dead_buses":      dead_buses,
        "phase":           phase,
        "experiment":      experiment,
        "scenario":        scenario,
        "timestamp":       ts_iso,
    }


def _steady_state_event(experiment: str, scenario: str, ts_iso: str) -> dict:
    """Return a steady-state (no fault) event payload."""
    return {
        "faulted_line_id": -1,
        "tie_closed":      False,
        "tie_id":          -1,
        "n_dead_buses":    0,
        "dead_buses":      [],
        "phase":           "steady_state",
        "experiment":      experiment,
        "scenario":        scenario,
        "timestamp":       ts_iso,
    }
