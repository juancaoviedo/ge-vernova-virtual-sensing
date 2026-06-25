# Phase 9: Measurement System (Observability Layer) — Pattern Map

**Mapped:** 2026-06-25
**Files analyzed:** 7 new/modified files
**Analogs found:** 7 / 7

---

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `src/ieee33/measure_config.py` | config | transform | `src/ieee33/config.py` | exact |
| `src/ieee33/measure.py` | runner/service | CRUD + transform | `src/ieee33/fault_sim.py` | exact |
| `src/ieee33/influx.py` (writer addition) | library | CRUD | `influx.write_fault_step` / `write_state_step` | exact |
| `grafana/provisioning/dashboards/ieee33-meas-day.json` | config | — | `ieee33-state.json` | exact |
| `grafana/provisioning/dashboards/ieee33-meas-fault.json` | config | — | `ieee33-fault-event.json` | exact |
| `pyproject.toml` ([project.scripts] addition) | config | — | `pyproject.toml` existing entries | exact |
| `README.md` (new section) | docs | — | existing README structure | N/A |

---

## Pattern Assignments

### `src/ieee33/measure_config.py` (config, transform)

**Analog:** `system1-measurement-source/src/ieee33/config.py`

**Module docstring + import pattern** (lines 1–20):
```python
"""
config.py
---------
All physical, data, and infrastructure constants for the IEEE 33-bus DER measurement
source. This module is pure constants — no I/O side effects beyond loading the .env
file at import time via python-dotenv.
"""

import os
from dotenv import load_dotenv

load_dotenv()
```
Mirror exactly: `measure_config.py` is pure constants — no I/O, no imports beyond stdlib. No `load_dotenv()` call needed (no env-var reads; those are in `config.py`). Docstring should state it is "pure constants — no I/O side effects."

**Constants block pattern** (config.py lines 17–221):
```python
# ---------------------------------------------------------------------------
# Section header (UPPERCASE constant with comment)
# ---------------------------------------------------------------------------
CONSTANT_NAME = value      # inline rationale comment referencing D-NN or SPEC

# Multi-entry dicts use consistent indentation
DICT_CONST: dict[str, float] = {
    "key1": 0.005,   # per-item comment where non-obvious
    "key2": 0.02,
}
```
`measure_config.py` should follow this layout exactly: one `# ---` section per logical group (sigma table, cadence table, scenario bus assignments, ACTIVE block).

**ACTIVE block pattern** (from RESEARCH.md Q6, mirrors config.py style):
```python
# ---------------------------------------------------------------
# ACTIVE BLOCK — edit this to switch experiments without code changes
# ---------------------------------------------------------------
ACTIVE: dict = {
    "scenario": "realistic_sparse",   # "well_observed" | "realistic_sparse"
    "source":   "day",                # "day" | "fault"
    "sampling": "snapshot",           # "snapshot" | "multirate_async"
    "noise":    "gaussian",           # "gaussian" | "gaussian_outliers" | "instrument"
    "seed":     42,
    "assumed_sigma_scale": 1.0,       # multiply CLASS_SIGMA to get assumed_sigma (1.0 = equal to true)
}
```
Inline comments on every key are mandatory (mirrors config.py's inline comment discipline).

**Type annotation pattern** (config.py line 127):
```python
ACSR_CONDUCTORS = [
    # name            R_ohm_per_km   ampacity_kA
    ("Drake 795",       0.0827,        0.907),
    ...
]
```
For `CLASS_SIGMA`, `CADENCE`, and `SCENARIOS`, use `dict[str, dict[str, float]]` / `dict[str, dict[str, int]]` / `dict[str, dict]` type annotations inline (Python 3.12, no `from __future__ import annotations` needed).

---

### `src/ieee33/measure.py` (runner/service, CRUD + transform)

**Analog:** `system1-measurement-source/src/ieee33/fault_sim.py`

**Module docstring pattern** (fault_sim.py lines 1–22):
```python
"""
fault_sim.py
------------
Deterministic 40-step fault-and-reconfiguration runner ...

Determinism note: anchor timestamp = OPSD UTC datetime for FAULT_EVENING_PEAK_STEP (step 72)
read from the profiles bucket; subsequent steps at +3s offsets.  No datetime.now(),
no np.random, no time.time() — identical 40 snapshots on every run.  Re-running overwrites
points at the same timestamp+tag keys (overwrite-in-place).

Dependencies: pandapower, pandapower.topology, networkx, influxdb-client, pandas, python-dotenv
Run:          uv run fault-sim
Effect:       Writes 40 fault-event power-flow snapshots to InfluxDB 'fault_event' bucket.
              Exits 0 on success, 1 on validation failure.
"""
```
`measure.py` docstring must contain: `Determinism note:` paragraph, `Dependencies:`, `Run: uv run measure`, `Effect:` paragraph listing what it writes, and explicit statement that it does NOT modify `state`/`fault_event` buckets.

**Imports pattern** (fault_sim.py lines 24–34):
```python
import sys
from datetime import datetime, timezone, timedelta

import networkx as nx
import pandapower as pp
import pandapower.topology as ptop
from influxdb_client.client.write_api import SYNCHRONOUS

from ieee33 import config
from ieee33 import influx
from ieee33.network import build_enhanced_33bus
```
`measure.py` will not use pandapower/networkx. Its imports:
```python
import sys
import argparse
from datetime import date, timedelta, timezone

import numpy as np
from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS

from ieee33 import config
from ieee33 import influx
from ieee33 import measure_config as mc
```

**CLI override pattern** (derived from D-09 + fault_sim.py `main()` argument structure):
```python
def _parse_args():
    p = argparse.ArgumentParser(description="IEEE 33-bus measurement layer runner")
    p.add_argument("--scenario", choices=["well_observed", "realistic_sparse"])
    p.add_argument("--source",   choices=["day", "fault"])
    p.add_argument("--sampling", choices=["snapshot", "multirate_async"])
    p.add_argument("--noise",    choices=["gaussian", "gaussian_outliers", "instrument"])
    p.add_argument("--seed",     type=int)
    return p.parse_args()
```
Merge into `cfg` dict that starts from `mc.ACTIVE` and is overridden by non-None CLI values. Mirror `fault_sim.py`'s `main()` first-thing print pattern.

**Main function opening pattern** (fault_sim.py lines 277–310):
```python
def main() -> None:
    """40-step fault-and-reconfiguration driver: freeze op-point, walk blocks, write fault_event bucket."""

    # ---- build network + capture base loads ----
    print("Building enhanced IEEE 33-bus network ...")
    net, trafo_idx = build_enhanced_33bus()
    base_p = net.load["p_mw"].copy().values
    base_q = net.load["q_mvar"].copy().values

    # ---- connect to InfluxDB + ensure fault_event bucket ----
    print(f"Connecting to InfluxDB at {config.INFLUXDB_URL} ...")
    client = influx.get_client()
    influx.wait_for_influx()
    influx.ensure_bucket(client, config.FAULT_EVENT_BUCKET)

    # ---- read all 96 profiles ONCE ----
    print(f"Reading 96-step profiles from InfluxDB ...")
    prof = influx.read_profiles(client).sort_values("_time").reset_index(drop=True)
```
`measure.py` `main()` structure mirrors this exactly — start with print, get client, `wait_for_influx`, `ensure_bucket("measurements")`, then read ground-truth (profiles + state or fault_event depending on `cfg["source"]`).

**Per-step iteration pattern** (fault_sim.py lines 361–485 core loop):
```python
for i, (phase, ts) in enumerate(zip(phases, timestamps)):
    # -- BLOCK TRANSITION checks first --
    if phase == config.FAULT_PHASE_ISO and prev_phase != config.FAULT_PHASE_ISO:
        ...

    # -- per-step write call --
    influx.write_fault_step(write_api, ts, ...)

    # -- D-18: console row --
    print(f"{i:>4}  {phase:<18}  {vmin:>6.4f}  ...")

    prev_phase = phase
```
`measure.py` core loop:
```python
for step_idx, (ts, snap) in enumerate(sorted_snapshots):
    # 1. determine energised buses from snap (or assume all 33 for source=day)
    # 2. iterate sensors in sorted class order then sorted bus_id order (determinism)
    # 3. cadence gate (multirate_async: skip if step_idx % cadence != 0)
    # 4. energised gate (skip if bus in dead_bus_ids — D-03)
    # 5. derive true values; apply noise; emit Point("meas")
    # 6. re-publish topology event Point("event")
    # 7. bulk write_api.write(bucket="measurements", ...)
    # 8. console row: step_idx, ts, n_live_meas, n_pseudo, n_dead_buses
```
The `write_api.write(...)` call signature pattern (fault_sim.py line 466):
```python
influx.write_fault_step(
    write_api, ts,
    state["res_bus"],
    ...
    phase, dead_bus_ids, dead_line_ids, dead_sgen_ids, tie_is_closed,
)
```
For `measure.py`, the write call is inline `write_api.write(bucket="measurements", org=config.INFLUXDB_ORG, record=points)` — same bucket/org pattern.

**Console table header pattern** (fault_sim.py lines 334–338):
```python
print(
    f"\n{'Step':>4}  {'Phase':<18}  {'Vmin':>6}  {'Load MW':>8}  "
    f"{'Tap':>4}  {'Dead':>5}"
)
print("-" * 62)
```
`measure.py` console header (adapted):
```python
print(
    f"\n{'Step':>4}  {'UTC Time':<20}  {'Live':>5}  {'Pseudo':>7}  "
    f"{'Dead':>5}  {'Pts':>6}"
)
print("-" * 62)
```
Per-row: `f"{step_idx:>4}  {str(ts)[:19]:<20}  {n_live:>5}  {n_pseudo:>7}  {n_dead:>5}  {n_pts:>6}"`

**Post-run validation + fail-loud pattern** (fault_sim.py lines 575–582):
```python
if issues:
    print("--- SIM VALIDATION FAILED ---", file=sys.stderr)
    for issue in issues:
        print(f"  {issue}", file=sys.stderr)
    client.close()
    sys.exit(1)
```
Copy verbatim. Accumulate issues into a `list[str]` throughout the run; fail loud at the end.

**Module entry point pattern** (fault_sim.py lines 595–600):
```python
if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nFATAL: {exc}", file=sys.stderr)
        sys.exit(1)
```
Copy verbatim.

**Footprint report pattern** (mirrors fault_sim.py success summary + D-15 format from RESEARCH.md Q8):
```python
# After all steps complete:
print("\n" + "=" * 62)
print("Measurement Footprint Report")
print("============================")
print(f"Scenario : {cfg['scenario']}")
print(f"Source   : {cfg['source']}")
print(f"Sampling : {cfg['sampling']}")
print(f"Noise    : {cfg['noise']}")
print(f"Seed     : {cfg['seed']}")
print("---")
print(f"{'Class':<12} | {'Count':>6} | {'Buses':>5}")
print(f"{'---':<12}-+-{'---':>6}-+-{'---':>5}")
for cls, cnt, n_buses in per_class_rows:
    print(f"{cls:<12} | {cnt:>6} | {n_buses:>5}")
print("---")
print(f"Total real measurements    : {n_real:,}")
print(f"Total pseudo measurements  : {n_pseudo:,}")
print(f"N_energised (avg)          : {avg_n_energised:.0f}")
print(f"N_states                   : {n_states}")
print(f"Real-only redundancy       : {real_redundancy:.3f}")
print(f"With-pseudo redundancy     : {with_pseudo_redundancy:.3f}")
```

---

### `src/ieee33/influx.py` — `write_meas_step` addition (library, CRUD)

**Analog:** `influx.write_fault_step` (lines 345–539) and `write_state_step` (lines 226–338)

This is an additive function added to the end of the existing `influx.py`. Do NOT modify any existing function.

**Function signature pattern** (mirrors write_fault_step lines 345–361):
```python
def write_meas_step(
    write_api,
    points: list,
    bucket: str = "measurements",
) -> None:
    """Write a batch of pre-built meas/event Points to the measurements bucket.

    Called by measure.py after building all Point objects for a single snapshot.
    Points must be fully constructed (all tags + fields + timestamp set) before
    this call.  SYNCHRONOUS write; overwrites existing points at same tag+ts key.

    Args:
        write_api: SYNCHRONOUS write_api from client.write_api(SYNCHRONOUS).
        points:    List of influxdb_client.Point objects (meas + event).
        bucket:    Target bucket name (default "measurements").
    """
    write_api.write(
        bucket=bucket,
        org=config.INFLUXDB_ORG,
        record=points,
    )
```
Alternative: `measure.py` may call `write_api.write(...)` directly (as shown in RESEARCH.md Pattern 2). Either is valid — the key is mirroring the `bucket=..., org=config.INFLUXDB_ORG, record=points` pattern.

**`meas` Point construction pattern** (mirrors write_state_step bus loop lines 277–284):
```python
# Analog — write_state_step bus point:
Point("bus")
.tag("bus_id", str(idx))
.field("vm_pu",     float(row["vm_pu"]))
.field("va_degree", float(row["va_degree"]))
.time(timestamp)

# New — meas point (D-06 schema):
Point("meas")
.tag("class",      cls)            # "scada" | "pmu" | "ami" | "der" | "pseudo" | "zero_inj"
.tag("quantity",   quantity)       # "vm_pu" | "va_degree" | "p_inj_mw" | "q_inj_mvar" | "p_mw" | "q_mvar"
.tag("location",   str(bus_id))
.tag("scenario",   scenario)
.tag("experiment", experiment)     # "day" | "fault"
# .tag("phase", phase_label)       # only for experiment="fault"
.field("value",         float(measured_val))
.field("assumed_sigma", float(emitted_sigma))
.time(ts)
```
Never add `.field("true_value", ...)` — scoring oracle separation (SPEC R9, D-06).

**`event` re-publish Point construction pattern** (mirrors write_fault_step event section lines 523–533):
```python
# Analog — original event write:
Point("event")
.tag("phase", phase_label)
.field("faulted_line_id", int(config.FAULT_LINE_IDX))
.field("tie_closed",      int(tie_is_closed))
.field("tie_id",          int(config.FAULT_TIE_IDX) if tie_is_closed else -1)
.field("n_dead_buses",    int(len(dead_bus_ids)))
.field("dead_buses",      ",".join(str(b) for b in sorted(dead_bus_ids)))
.time(timestamp)

# New — re-published into measurements bucket with extra scenario/experiment tags:
Point("event")
.tag("phase",      phase_label)    # fault phases or "steady_state" for day
.tag("scenario",   scenario)
.tag("experiment", experiment)
.field("faulted_line_id", int(config.FAULT_LINE_IDX) if experiment == "fault" else -1)
.field("tie_closed",      int(tie_is_closed))
.field("tie_id",          int(config.FAULT_TIE_IDX) if tie_is_closed else -1)
.field("n_dead_buses",    int(len(dead_bus_ids)))
.field("dead_buses",      ",".join(str(b) for b in sorted(dead_bus_ids)))
.time(ts)
```
CRITICAL: `tie_id` must always be `int(...)` (never float) — mirrors line 529 of write_fault_step to avoid InfluxDB type conflicts (Pitfall 2 from RESEARCH.md).

**Flux read pattern for `state` bus data** (analog: `read_profiles` lines 141–181):
```python
# Analog — read_profiles:
flux = (
    f'from(bucket: "{config.PROFILES_BUCKET}")\n'
    f'  |> range(start: {start}, stop: {stop})\n'
    f'  |> filter(fn: (r) => r._measurement == "profiles")\n'
    f'  |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")\n'
    f'  |> sort(columns: ["_time"])'
)
df = client.query_api().query_data_frame(flux)

# New — read state bus data (vm_pu / va_degree only — no p_mw in state bucket):
flux = (
    f'from(bucket: "{config.STATE_BUCKET}")\n'
    f'  |> range(start: {start}, stop: {stop})\n'
    f'  |> filter(fn: (r) => r._measurement == "bus")\n'
    f'  |> pivot(rowKey: ["_time", "bus_id"], columnKey: ["_field"], valueColumn: "_value")\n'
    f'  |> sort(columns: ["_time", "bus_id"])'
)
# Columns: _time, bus_id, vm_pu, va_degree  (NO p_mw — Pitfall 6 from RESEARCH.md)
```

**Flux read pattern for `fault_event` bus data** (with energised tag in rowKey — Pitfall 1):
```python
# CRITICAL: energised is a TAG (not a field) → must appear in rowKey
flux = (
    f'from(bucket: "{config.FAULT_EVENT_BUCKET}")\n'
    f'  |> range(start: {start}, stop: {stop})\n'
    f'  |> filter(fn: (r) => r._measurement == "bus")\n'
    f'  |> pivot(rowKey: ["_time", "bus_id", "energised"], '
    f'columnKey: ["_field"], valueColumn: "_value")\n'
    f'  |> sort(columns: ["_time", "bus_id"])'
)
# Columns: _time, bus_id, energised ("1"/"0"), vm_pu, va_degree, p_mw, q_mvar
# Dead-bus gate: snap[snap["energised"] == "1"] (string comparison, not int)
```

---

### `grafana/provisioning/dashboards/ieee33-meas-day.json` (config, dashboard)

**Analog:** `ieee33-state.json` (lines 1–end)

**Top-level JSON skeleton** (ieee33-state.json lines 1–32):
```json
{
  "__inputs": [],
  "__requires": [
    { "type": "grafana",    "id": "grafana",    "name": "Grafana",    "version": "11.0.0" },
    { "type": "datasource", "id": "influxdb",   "name": "InfluxDB",   "version": "1.0.0" },
    { "type": "panel",      "id": "timeseries", "name": "Time series","version": "" }
  ],
  "annotations": { "list": [] },
  "description": "...",
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 1,
  "id": null,
  "links": [],
  "panels": [...],
  "refresh": "30s",
  "schemaVersion": 39,
  "tags": ["measurements"],
  "title": "IEEE 33-Bus Observed Measurements — Day",
  "uid": "ieee33-meas-day",
  "version": 1
}
```
Rules:
- `"id": null` — Grafana assigns on import; NEVER hardcode
- `"uid": "ieee33-meas-day"` — distinct from `"ieee33-state-v1"` (check existing state.json uid)
- `"schemaVersion": 39` — copy from existing dashboards
- `"refresh": "30s"` — copy from existing dashboards

**Datasource reference pattern** (ieee33-state.json line 81):
```json
"datasource": { "type": "influxdb", "uid": "ieee33-influxdb" }
```
Every panel and every `target` inside `targets[]` must carry this datasource object.

**Panel gridPos pattern** (ieee33-state.json line 65):
```json
"gridPos": { "h": 9, "w": 12, "x": 0, "y": 0 }
```
Use 12-column Grafana grid. Two side-by-side panels: left `x:0,w:12`, right `x:12,w:12`. Full-width: `x:0,w:24`.

**Timeseries panel target pattern with Flux** (ieee33-state.json lines 78–83):
```json
"targets": [
  {
    "datasource": { "type": "influxdb", "uid": "ieee33-influxdb" },
    "query": "from(bucket: \"measurements\")\n  |> range(start: 2017-06-07T00:00:00Z, stop: 2017-06-07T23:59:59Z)\n  |> filter(fn: (r) => r._measurement == \"meas\")\n  |> filter(fn: (r) => r._field == \"value\")\n  |> filter(fn: (r) => r.quantity == \"vm_pu\")\n  |> filter(fn: (r) => r.scenario == \"realistic_sparse\")\n  |> filter(fn: (r) => r.experiment == \"day\")",
    "refId": "A"
  },
  {
    "datasource": { "type": "influxdb", "uid": "ieee33-influxdb" },
    "query": "from(bucket: \"state\")\n  |> range(start: 2017-06-07T00:00:00Z, stop: 2017-06-07T23:59:59Z)\n  |> filter(fn: (r) => r._measurement == \"bus\")\n  |> filter(fn: (r) => r._field == \"vm_pu\")",
    "refId": "B"
  }
]
```
The two-`refId` dual-source pattern enables the true-vs-measured overlay (D-16).

**fieldConfig defaults pattern** (ieee33-state.json lines 40–62):
```json
"fieldConfig": {
  "defaults": {
    "color": { "mode": "palette-classic" },
    "custom": {
      "lineWidth": 2,
      "fillOpacity": 5,
      "showPoints": "never",
      "spanNulls": false
    },
    "thresholds": {
      "mode": "absolute",
      "steps": [
        { "color": "red",   "value": null },
        { "color": "green", "value": 0.95 },
        { "color": "red",   "value": 1.05 }
      ]
    },
    "unit": "short",
    "decimals": 4,
    "min": 0.90,
    "max": 1.10
  },
  "overrides": []
}
```

**stat panel type** (ieee33-fault-event.json `__requires` lines 26–29):
```json
{ "type": "panel", "id": "stat", "name": "Stat", "version": "" }
```
Add to `__requires` if using stat panels (e.g., for per-class measurement counts).

---

### `grafana/provisioning/dashboards/ieee33-meas-fault.json` (config, dashboard)

**Analog:** `ieee33-fault-event.json` (lines 1–end)

**Top-level skeleton** — same as `ieee33-meas-day.json` except:
```json
{
  "description": "IEEE 33-Bus Observed Measurements — Fault Scenario: 40-step event (pre_fault/faulted_isolated/restored). Shows observed measurements from the measurements bucket overlaid with fault_event ground truth. Panels: observed voltages (μPMU bus 17 goes dark during isolation), phase-region marker, dead-bus count, per-class measurement counts.",
  "title": "IEEE 33-Bus Observed Measurements — Fault",
  "uid": "ieee33-meas-fault"
}
```

**Phase-region marker pattern** (ieee33-fault-event.json — stat/table panel for phase metadata):
```json
{
  "datasource": { "type": "influxdb", "uid": "ieee33-influxdb" },
  "query": "from(bucket: \"measurements\")\n  |> range(start: 2017-06-07T17:59:00Z, stop: 2017-06-07T18:03:00Z)\n  |> filter(fn: (r) => r._measurement == \"event\")\n  |> filter(fn: (r) => r._field == \"n_dead_buses\")\n  |> filter(fn: (r) => r.scenario == \"realistic_sparse\")\n  |> filter(fn: (r) => r.experiment == \"fault\")",
  "refId": "A"
}
```
This queries the re-published `event` measurement in the `measurements` bucket (D-07) — not the original `fault_event` bucket.

**Fault dashboard time range** (ieee33-fault-event.json line 94 query):
```json
"query": "from(bucket: \"fault_event\")\n  |> range(start: 2017-06-07T17:59:00Z, stop: 2017-06-07T18:03:00Z)\n  ..."
```
Mirror this 4-minute window for the `measurements` bucket queries in `ieee33-meas-fault.json`.

---

### `pyproject.toml` — `[project.scripts]` addition (config)

**Analog:** `pyproject.toml` lines 16–20 (existing `[project.scripts]` block)

**Existing pattern:**
```toml
[project.scripts]
ingest    = "ieee33.ingest:main"
sim       = "ieee33.sim:main"
validate  = "ieee33.validate:main"
fault-sim = "ieee33.fault_sim:main"
```

**Addition (append one line, preserve alignment):**
```toml
[project.scripts]
ingest    = "ieee33.ingest:main"
sim       = "ieee33.sim:main"
validate  = "ieee33.validate:main"
fault-sim = "ieee33.fault_sim:main"
measure   = "ieee33.measure:main"
```
Entry point format: `<script-name> = "<package>.<module>:<function>"`. No other toml changes needed (no new dependencies).

---

## Shared Patterns

### InfluxDB client lifecycle
**Source:** `system1-measurement-source/src/ieee33/influx.py` lines 31–37, 44–71, 78–97
**Apply to:** `measure.py` `main()` opening

```python
# Client factory (influx.py:31-37)
client = influx.get_client()         # InfluxDBClient(url, token, org) from config

# Readiness poll (influx.py:44-71) — mandatory before first write
influx.wait_for_influx()             # polls /ping with 60s timeout

# Idempotent bucket creation (influx.py:78-97) — call for every new bucket
influx.ensure_bucket(client, "measurements")   # creates if absent, no-op if present

# Client teardown (sim.py:323, fault_sim.py:592)
client.close()                       # always at end of main(), including error paths
```

### Write API setup
**Source:** `system1-measurement-source/src/ieee33/sim.py` line 157; `fault_sim.py` line 330
**Apply to:** `measure.py` before the step loop

```python
write_api = client.write_api(write_options=SYNCHRONOUS)
```
SYNCHRONOUS is mandatory — prevents background-thread write failures from silently dropping points.

### Issues accumulation + fail-loud
**Source:** `system1-measurement-source/src/ieee33/fault_sim.py` lines 331, 575–582
**Apply to:** `measure.py` post-loop validation gate

```python
issues: list[str] = []
# ... accumulate: issues.append(f"step {i}: ...")
if issues:
    print("--- SIM VALIDATION FAILED ---", file=sys.stderr)
    for issue in issues:
        print(f"  {issue}", file=sys.stderr)
    client.close()
    sys.exit(1)
```

### Timestamp UTC-awareness
**Source:** `system1-measurement-source/src/ieee33/sim.py` lines 187–190
**Apply to:** `measure.py` when building timestamps from profile DataFrame rows

```python
ts = row["_time"]
if hasattr(ts, "to_pydatetime"):
    ts = ts.to_pydatetime()
if ts.tzinfo is None:
    ts = ts.replace(tzinfo=timezone.utc)
```
Apply identically when extracting `_time` from the Flux query result DataFrames.

### Deterministic RNG
**Source:** RESEARCH.md Q3 + Q8 (D-10, D-11); no direct analog in existing code
**Apply to:** `measure.py` noise engine; initialise once in `main()`, pass into all noise functions

```python
rng = np.random.default_rng(cfg["seed"])   # ONE rng per run, at main() start
# Never use np.random.seed() or np.random.<legacy>
# Never create multiple independent RNGs
# Sort iteration order before generating noise: sorted(bus_ids), sorted(class_names)
```

### Overwrite-in-place keyed write
**Source:** `system1-measurement-source/src/ieee33/influx.py` write_fault_step docstring (lines 345–410) and sim.py docstring line 14
**Apply to:** all `write_api.write(...)` calls in `measure.py`

InfluxDB unique key = (measurement name, all tags, timestamp). Writing the same `(meas, {class, quantity, location, scenario, experiment, [phase]}, ts)` twice overwrites silently — no duplicates. Two consecutive same-config runs produce byte-identical values (SPEC R10).

### Flux pivot: `query_data_frame` call
**Source:** `system1-measurement-source/src/ieee33/influx.py` lines 174, 288 (`read_profiles`, `count_profiles`)
**Apply to:** all Flux reads in `measure.py`

```python
df = client.query_api().query_data_frame(flux)
n = len(df) if df is not None else 0
```
Always guard for `None` return (empty bucket returns `None` in influxdb-client 1.50).

### date/timedelta imports for Flux range strings
**Source:** `system1-measurement-source/src/ieee33/influx.py` lines 161–165 inside `read_profiles`
**Apply to:** `measure.py` Flux read helpers

```python
from datetime import date as _date, timedelta as _td
next_day = (_date.fromisoformat(config.TARGET_DATE) + _td(days=1)).isoformat()
start = f"{config.TARGET_DATE}T00:00:00Z"
stop  = f"{next_day}T00:00:00Z"
```

---

## No Analog Found

All seven Phase 9 files have close analogs in the codebase. The following sub-components within `measure.py` have no existing analog and must follow RESEARCH.md patterns:

| Sub-component | Data Flow | Reason | Use Instead |
|---------------|-----------|--------|-------------|
| Gaussian noise engine | transform | No NumPy noise in codebase | RESEARCH.md Q3 Pattern (D-11) |
| `gaussian_outliers` model | transform | No outlier injection in codebase | RESEARCH.md Q3 D-12 pattern |
| `instrument` AR(1) model | transform | No temporal correlation in codebase | RESEARCH.md Q3 D-13 pattern + `InstrumentState` class |
| `multirate_async` cadence decimation | transform | No per-class step-decimation in codebase | RESEARCH.md Q5 D-14 |
| P_inj derivation for `source=day` | transform | `state` bucket has no `p_mw` on `bus` measurement | RESEARCH.md Q4: profiles+scaling approach |
| Redundancy footprint calculation | transform | No observability math in codebase | RESEARCH.md Q2 + D-15 formula |

---

## Metadata

**Analog search scope:** `system1-measurement-source/src/ieee33/` (all .py files), `grafana/provisioning/dashboards/` (all .json files), `pyproject.toml`
**Files read:** `sim.py`, `fault_sim.py`, `config.py`, `influx.py` (full 540 lines), `ieee33-state.json` (first 100 lines), `ieee33-fault-event.json` (first 120 lines), `default.yml`, `pyproject.toml`
**Pattern extraction date:** 2026-06-25
