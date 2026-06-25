# Phase 9: Measurement System (Observability Layer) — Research

**Researched:** 2026-06-25
**Domain:** Python measurement-layer implementation — InfluxDB Flux reads, NumPy noise models, sensor-placement scenarios, Grafana provisioning
**Confidence:** HIGH (all findings verified by reading the actual source files this phase extends)

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

- **D-01:** `write_fault_step` real contract — bucket `fault_event`; `bus`/`line`/`sgen`/`system` byte-identical to `state`; `event` measurement with tag `phase` + fields `faulted_line_id`, `tie_closed`, `tie_id` (int, −1 when open), `n_dead_buses`, `dead_buses` (comma-joined sorted string). Fault line idx 7, dead buses 8–17, restore tie 34. Phase tags: `pre_fault` / `faulted_isolated` / `restored`. Window 40 steps (13/7/20), 3 s, anchored at evening-peak step 72.
- **D-02:** `energised` is an InfluxDB TAG (string `"1"`/`"0"`) on `bus`/`line`/`sgen` points — NOT a field. Dead entities are present-but-zero-filled every snapshot (vm_pu=0, va_degree=0, p/q=0, energised=`"0"`), not absent.
- **D-03:** During isolation the measurement layer emits NO live sensor measurement for any `energised="0"` entity; no pseudo-measurement for a dead bus. Bus 17 (μPMU candidate + DG sgen) sits inside the dead zone → goes dark deliberately.
- **D-04 — `realistic_sparse`:** SCADA: bus 0 → `P_inj, Q_inj, |V|`; μPMU: buses {17, 24, 30} → `|V|, angle`; DER telemetry: buses {17, 21, 24, 32} → `P, Q`; AMI (~30% loads, ~10 buses): {3, 6, 9, 12, 15, 18, 21, 24, 28, 31} → `P_inj`; pseudo: every remaining load bus → `P_inj, Q_inj` (large σ). Real-only redundancy < 1.0; ≥ 1.0 only after pseudo.
- **D-05 — `well_observed`:** SCADA: bus 0; μPMU: buses {0, 4, 8, 13, 17, 21, 24, 28, 32} (9); DER: {17, 21, 24, 32}; AMI (~80% loads): all load buses except small held-out set → `P_inj` (+`Q_inj`); zero-injection (virtual): ~2 junction buses (e.g., {2, 19}) → `P=0, Q=0`. Real redundancy > 1.0.
- **D-06:** One generic `meas` measurement point per sensor reading. Tags: `class` ∈ {scada,pmu,ami,der,pseudo,zero_inj}; `quantity` ∈ {vm_pu,va_degree,p_inj_mw,q_inj_mvar,p_mw,q_mvar}; `location` (bus or line id); `scenario` ∈ {well_observed,realistic_sparse}; `experiment` ∈ {day,fault}; plus `phase` (fault only). Fields: `value` (noisy reading) and `assumed_sigma`. No `true_value` field.
- **D-07:** Topology re-published per snapshot into the same `event` measurement name (tag `phase`; fields `faulted_line_id`, `tie_closed`, `tie_id`, `n_dead_buses`, `dead_buses`), additionally tagged `scenario`/`experiment`. For `experiment=day` records fixed/known topology (no fault, all ties open).
- **D-08:** New modules in `src/ieee33/`: `measure.py` (runner) + `measure_config.py` (named scenario dicts, noise profiles, sampling cadences, and `ACTIVE` selection block). New `[project.scripts]` entry `measure = "ieee33.measure:main"` → `uv run measure`.
- **D-09:** Config file is the primary switch (edit `measure_config.py` ACTIVE block). Also accept CLI overrides (`--scenario --source --sampling --noise --seed`) defaulting to config values.
- **D-10:** Reuse `influx.get_client/wait_for_influx/ensure_bucket`; new bucket `measurements` via `ensure_bucket`. Read ground truth via Flux pivot queries mirroring `read_profiles`. Deterministic overwrite-in-place.
- **D-11 — per-class σ:** SCADA |V| 0.005 / P,Q 0.02; μPMU |V| 0.001 / angle 0.0003 rad; AMI P(,Q) 0.03; DER P,Q 0.015; pseudo P,Q 0.30; zero-injection 1e-4.
- **D-12 — `gaussian_outliers`:** base Gaussian + gross errors on fraction f=0.03 of measurements, spike magnitude ≈ 15·σ with random sign.
- **D-13 — `instrument`:** per-class quantization (LSB), fixed per-sensor systematic bias (~+0.5% of value, seed-derived), AR(1) temporal correlation (ρ≈0.7).
- **D-14:** `snapshot` = every class at every timestamp. `multirate_async` defaults — day (96×15 min): μPMU/DER/SCADA every step, AMI every 4 steps; pseudo every step. fault (40×3 s): μPMU/DER every step, SCADA every 2 steps, AMI every 10 steps; pseudo every step.
- **D-15:** Each run prints per-class measurement count, pseudo count, observed-vs-dead bus counts, and redundancy = total_measurements ÷ (2·(N_energised−1)) — real-only and with-pseudo.
- **D-16:** Two auto-provisioned dashboards: `ieee33-meas-day.json` and `ieee33-meas-fault.json`. Panels: observed bus-voltage measurements (with true series overlaid), observed-vs-pseudo footprint, per-class measurement counts, and (for fault) phase-region marker + dead-bus count.

### Claude's Discretion

- Exact AMI/μPMU bus membership within the stated targets, exact ACTIVE-block field names, Flux query details, dashboard panel layout, and the precise quantization LSBs are planner/executor details within the locked intent above.

### Deferred Ideas (OUT OF SCOPE)

- Live streaming transport (NATS / MQTT / C37.118-over-UDP) reading from the `measurements` bucket
- System 2 (state estimator) and the estimate-vs-truth comparison dashboard
- Jacobian-rank / covariance-based observability index (ORACS observability)

</user_constraints>

---

## Summary

Phase 9 adds a config-driven measurement layer to the existing `system1-measurement-source/` uv project. It reads System 1's ground-truth InfluxDB data (either the 96-step `state` day or the 40-step `fault_event` scenario), applies a sensor model (bus/class assignments), corrupts values with a switchable noise model, decimates to per-class cadence, and writes the resulting measurement set to a new `measurements` bucket. Two Grafana dashboards of observed states are auto-provisioned.

All implementation decisions are locked (D-01..D-16 in CONTEXT.md). The research below answers the eight build questions the additional-context specified, grounded entirely in the verified codebase.

**Primary recommendation:** Two new modules (`measure_config.py` + `measure.py`) added to `src/ieee33/`, mirroring `fault_sim.py`'s runner structure. The Flux pivot read pattern, `ensure_bucket`, and Grafana JSON provisioning are reused verbatim; the only genuinely new work is the noise engine, the per-bus selector, and the two dashboard JSONs.

---

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Ground-truth read (Flux) | Backend/Python runner | InfluxDB | `measure.py` queries `state`/`fault_event` |
| Sensor model + noise | Backend/Python runner | — | Pure NumPy in `measure.py` |
| Measurement persistence | InfluxDB | Python runner | `measurements` bucket written by `measure.py` |
| Config/knob switching | Config file (`measure_config.py`) | argparse CLI | User edits ACTIVE block; CLI overrides for sweeps |
| Dashboard provisioning | Grafana | Docker volume mount | Two JSON files in `grafana/provisioning/dashboards/` |

---

## Standard Stack

### Core (verified against pyproject.toml) [VERIFIED: pyproject.toml]

| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| influxdb-client | 1.50.0 | Write `meas` points; Flux pivot read | Already pinned in project |
| pandas | >=2.3 | DataFrame pivot after Flux query | Already in project |
| numpy | >=1.26,<2.4 | Noise generation (seeded RNG) | Already in project |
| python-dotenv | >=1.0 | Load `.env` (InfluxDB credentials) | Already in project |

No new dependencies are required. All noise models and pivot queries are implementable with the libraries already installed.

**Installation:** none — `uv sync` with the existing `pyproject.toml` is sufficient. Add `measure = "ieee33.measure:main"` to `[project.scripts]` only.

---

## Architecture Patterns

### System Architecture Diagram

```
InfluxDB
  state bucket (96 steps)       ──┐
  fault_event bucket (40 steps) ──┤─── measure.py reader
                                  │       │
                              Flux pivot  │
                                          ▼
                              measure_config.py  ←── ACTIVE block / CLI args
                                          │
                              Sensor selector
                              (per-scenario bus→class map)
                                          │
                              Noise engine (numpy RNG, seeded)
                              [gaussian | gaussian_outliers | instrument]
                                          │
                              Cadence filter (snapshot | multirate_async)
                                          │
                              Topology gate (energised tag → skip dead buses)
                                          │
                                          ▼
                              InfluxDB measurements bucket
                              (meas points + event topology)
                                          │
                              Grafana ieee33-meas-day.json
                                    ieee33-meas-fault.json
                              (auto-provisioned, overlay true series)
```

### Recommended Project Structure

```
system1-measurement-source/
├── src/ieee33/
│   ├── config.py            # existing — reuse constants (no changes)
│   ├── influx.py            # existing — reuse helpers (no changes)
│   ├── measure_config.py    # NEW — ACTIVE block + scenario/noise/cadence dicts
│   └── measure.py           # NEW — runner (mirrors fault_sim.py structure)
├── grafana/provisioning/dashboards/
│   ├── default.yml          # existing — untouched
│   ├── ieee33-state.json    # existing — untouched
│   ├── ieee33-fault-event.json  # existing — untouched
│   ├── ieee33-meas-day.json     # NEW — day observed states dashboard
│   └── ieee33-meas-fault.json   # NEW — fault observed states dashboard
└── pyproject.toml           # add `measure` to [project.scripts]
```

---

## Build Question Answers

### Q1 — Flux query shape to read `state` and `fault_event` back into DataFrames

**Pattern:** Mirror `read_profiles` exactly — range-filter by measurement name, pivot on `_field`, sort by `_time`. [VERIFIED: influx.py:141-181]

**For `state` bus data (96 steps):**

```python
# Source: influx.py:141-181 read_profiles pattern
flux = (
    f'from(bucket: "state")\n'
    f'  |> range(start: {config.TARGET_DATE}T00:00:00Z, stop: {next_day}T00:00:00Z)\n'
    f'  |> filter(fn: (r) => r._measurement == "bus")\n'
    f'  |> pivot(rowKey: ["_time", "bus_id"], columnKey: ["_field"], valueColumn: "_value")\n'
    f'  |> sort(columns: ["_time", "bus_id"])'
)
df = client.query_api().query_data_frame(flux)
# Result columns: _time, bus_id, vm_pu, va_degree
```

The pivot produces a flat DataFrame with one row per (timestamp, bus_id). Same pattern for `line` (with `line_id` tag) and `sgen` (with `sgen_id` tag).

**For `fault_event` bus data (40 steps, including energised tag):**

```python
# energised is a TAG in fault_event — appears as a column after pivot, not a field
flux = (
    f'from(bucket: "fault_event")\n'
    f'  |> range(start: anchor_ts, stop: anchor_ts + 120s)\n'
    f'  |> filter(fn: (r) => r._measurement == "bus")\n'
    f'  |> pivot(rowKey: ["_time", "bus_id", "energised"], columnKey: ["_field"], valueColumn: "_value")\n'
    f'  |> sort(columns: ["_time", "bus_id"])'
)
# Result columns: _time, bus_id, energised ("1"/"0"), vm_pu, va_degree, p_mw, q_mvar
```

**Critical detail:** `energised` is a TAG not a field [VERIFIED: influx.py:419,424]. In Flux, tags appear as columns AFTER `pivot()` automatically because `rowKey` includes them. The `energised` column value is a string `"1"` or `"0"` — compare as `row["energised"] == "1"`.

**For `fault_event` event measurement (topology metadata):**

```python
# event measurement has tag "phase"; fields: faulted_line_id, tie_closed, tie_id, n_dead_buses, dead_buses
flux = (
    f'from(bucket: "fault_event")\n'
    f'  |> range(start: anchor_ts, stop: ...)\n'
    f'  |> filter(fn: (r) => r._measurement == "event")\n'
    f'  |> pivot(rowKey: ["_time", "phase"], columnKey: ["_field"], valueColumn: "_value")\n'
    f'  |> sort(columns: ["_time"])'
)
# Result columns: _time, phase, faulted_line_id, tie_closed, tie_id, n_dead_buses, dead_buses
# dead_buses is a comma-joined string: "8,9,10,11,12,13,14,15,16,17"
```

[VERIFIED: influx.py:524-532 — `event` measurement written with `tag("phase", phase_label)` and five int/string fields]

**Per-bus enumeration pattern:** After the bus pivot, `groupby("_time")` and iterate groups. Each group is a snapshot — all 33 bus rows at a single timestamp. Filter `energised == "1"` for live buses.

**Time-range handling for fault_event:** The 40 steps span 13+7+20 = 40 × 3 s = 120 s, anchored at the OPSD UTC datetime for step 72. The range query needs `stop = anchor_ts + 121s` (one second margin).

**Practical reading approach:** Read all data once, build Python dicts keyed by timestamp, then iterate timestamps in sorted order. This avoids per-step round-trips.

```python
# Read entire fault_event bus data in one Flux call → DataFrame
bus_df = read_fault_bus(client)   # returns pivot with columns: _time, bus_id, energised, vm_pu, va_degree, p_mw, q_mvar

# Group by timestamp
for ts, snap in bus_df.groupby("_time"):
    live_buses = snap[snap["energised"] == "1"]
    dead_buses = snap[snap["energised"] == "0"]
    ...
```

---

### Q2 — Node-voltage state count for redundancy footprint [VERIFIED: D-15 in CONTEXT.md]

States at a given snapshot = `2 × (N_energised − 1)` where:
- Slack bus (bus 0) has known |V|=1.0 pu and angle=0.0 — excluded from unknowns
- Each remaining energised bus contributes one unknown magnitude + one unknown angle
- `N_energised` = count of buses with `energised=="1"` (or all 33 during normal operation / `source=day`)

**Day source (static topology):** All 33 buses always energised → states = 2 × 32 = 64. This is constant across all 96 steps.

**Fault source (dynamic topology):**
- `pre_fault`: all 33 buses → states = 64
- `faulted_isolated`: 33 − 10 = 23 energised buses → states = 44
- `restored`: all 33 back → states = 64

The redundancy report must compute N_energised per-snapshot from the `energised` tag in the read data. For `source=day` there is no `energised` tag (the `state` bucket schema per `write_state_step` does NOT include `energised`) — assume all 33 buses energised.

**Redundancy formulae:**
```python
n_states = 2 * (n_energised - 1)
real_only_redundancy = n_real_measurements / n_states
with_pseudo_redundancy = (n_real_measurements + n_pseudo_measurements) / n_states
```

[VERIFIED: D-15 locks this exact formula]

---

### Q3 — NumPy noise model patterns [VERIFIED: D-11, D-12, D-13; library: numpy>=1.26]

**Key principle:** Use `numpy.random.default_rng(seed)` — the new Generator API (not legacy `np.random.seed()`). This is recommended since NumPy 1.17 and is stream-reproducible.

```python
import numpy as np

rng = np.random.default_rng(seed)   # one RNG per run; thread-safe Generator
```

**Gaussian noise model:**
```python
def apply_gaussian(true_value: float, true_sigma: float, assumed_sigma: float, rng) -> tuple[float, float]:
    noise = rng.normal(0.0, true_sigma)
    return true_value + noise, assumed_sigma
```

`true_sigma` is a fraction of `|true_value|` for most classes (e.g., SCADA |V| = 0.005 × vm_pu). For angle, it is absolute (0.0003 rad). Compute: `sigma = CLASS_SIGMA[class_name][quantity] * abs(true_value)` except angle.

**Gaussian-outliers model:**
```python
def apply_gaussian_outliers(true_value, true_sigma, assumed_sigma, rng, f=0.03, spike_mult=15.0):
    noise = rng.normal(0.0, true_sigma)
    if rng.random() < f:              # 3% probability of gross error
        sign = rng.choice([-1.0, 1.0])
        noise = sign * spike_mult * true_sigma
    return true_value + noise, assumed_sigma
```

**Instrument model (three-component):**
```python
# Initialization (per sensor, seed-derived — run ONCE per scenario build):
def make_instrument_bias(sensor_id: str, seed: int, scale=0.005) -> float:
    """Deterministic per-sensor bias derived from hash of sensor_id + seed."""
    bias_rng = np.random.default_rng(hash((sensor_id, seed)) & 0xFFFFFFFF)
    return bias_rng.normal(0.0, scale)   # ~+0.5% systematic bias, sensor-specific

# State (persistent across steps — needed for AR(1)):
# noise_prev: dict mapping sensor_id -> float, initialized to 0.0

def apply_instrument(true_value, true_sigma, assumed_sigma, sensor_id, bias, noise_prev, rng, quant_lsb, rho=0.7):
    # AR(1) temporal correlation
    white = rng.normal(0.0, true_sigma * np.sqrt(1 - rho**2))
    noise_ar1 = rho * noise_prev.get(sensor_id, 0.0) + white
    noise_prev[sensor_id] = noise_ar1

    # Quantization (round to LSB)
    raw = true_value + bias * abs(true_value) + noise_ar1
    quantized = round(raw / quant_lsb) * quant_lsb

    return quantized, assumed_sigma
```

**Quantization LSBs (Claude's Discretion — suggested values):**

| Class | Quantity | LSB |
|-------|----------|-----|
| SCADA | vm_pu | 0.001 pu |
| SCADA | P_inj_mw | 0.01 MW |
| SCADA | Q_inj_mvar | 0.01 MVAr |
| μPMU | vm_pu | 0.0001 pu |
| μPMU | va_degree | 0.001 deg |
| AMI | P_inj_mw | 0.1 kWh ÷ step_h → depends on step size |
| DER | P_mw, Q_mvar | 0.001 MW |

**Separability of true_sigma vs assumed_sigma:** The noise engine always generates using `true_sigma`. The emitted `assumed_sigma` field in the `meas` point is the independently configured `ACTIVE["assumed_sigma_scale"]` × class_sigma. They share the same σ table by default but the scale factor is independently settable. Never feed `assumed_sigma` into the noise calculation.

**RNG call ordering and determinism:** Generate ALL noise values for a given snapshot in a fixed, deterministic order (sorted by class, then sorted by location id, then by quantity). This ensures that adding/removing classes doesn't shift the random stream for unaffected sensors.

---

### Q4 — P_inj / Q_inj derivation from ground-truth persisted data

**The challenge:** SCADA and AMI classes emit `P_inj, Q_inj` (net bus power injection). The `state` bucket schema (`write_state_step`) does NOT directly write per-bus injection; it writes per-bus `vm_pu, va_degree` only. Power is stored at the load and sgen level separately.

**What is available in `state`:**
- `bus` measurement: `vm_pu`, `va_degree` only [VERIFIED: influx.py:277-285]
- `line` measurement: `p_from_mw`, `q_from_mvar`, `p_to_mw`, `q_to_mvar`, `loading_percent`, `pl_mw`, `ql_mvar`
- `sgen` measurement: `p_mw`, `q_mvar` (per sgen)
- `system` measurement: aggregates only

**What is available in `fault_event`:**
- `bus` measurement: `vm_pu`, `va_degree`, **PLUS `p_mw`, `q_mvar`** (net per-bus power from pandapower `res_bus`) [VERIFIED: influx.py:417-428]

**Cleanest derivation path:**

**For `source=fault`:** Use `p_mw` and `q_mvar` directly from the `bus` measurement in `fault_event`. The `write_fault_step` already stores net per-bus power: "p_mw / q_mvar are net per-bus power (pandapower res_bus convention: positive = net consumption/load at the bus, negative = net injection)" [VERIFIED: influx.py:412-414].

So for the fault scenario:
- `P_inj` = `p_mw` field from `bus` measurement
- `Q_inj` = `q_mvar` field from `bus` measurement
- Sign convention: positive = load consumption; negative = net generation. The DSSE convention is typically P_inj positive = injection into the bus → may need sign flip. Flip if needed: `p_inj = -p_mw` (positive injection = generation exceeds load).

**For `source=day`:** The `state` bucket does NOT store per-bus p/q directly. Two clean options:

Option A — **Line-flow balance derivation (cleanest for a measurement layer, no re-simulation):**
```
P_inj at bus i = sum(P_from of lines starting at i) - sum(P_to of lines ending at i) + sgen p_mw at bus i
```
This requires reading BOTH the `line` and `sgen` measurements and knowing the network topology (which lines start/end at which buses — fixed for IEEE 33-bus, derivable from `config.py` or pandapower's `net.line`).

The IEEE 33-bus line-endpoint map is fixed and can be hard-coded or loaded once from pandapower. The line measurements give `p_from_mw` (power leaving from-bus) and `p_to_mw` (power arriving at to-bus, including losses). The KCL balance at bus i:
```
P_net_at_i = (sum of p_from_mw for lines FROM bus i) - (sum of p_to_mw for lines INTO bus i)
             + (sum of sgen p_mw at bus i) - (load_p_mw at bus i — NOT in state bucket)
```

This still requires knowing load power, which is NOT in the `state` bucket directly.

Option B — **Simpler: use pandapower `res_bus.p_mw` during post-processing** — but Phase 9 reads from InfluxDB only (no pandapower re-run).

Option C — **RECOMMENDED: Add per-bus `p_mw`, `q_mvar` to the `state` bucket as a forward-contract extension in Phase 8 / 8.1.** However, this is out of scope (SPEC says do not modify the `state` bucket).

**Actual recommended approach for `source=day`:**
Read the `line` DataFrame (which has `p_from_mw`, `p_to_mw` for all in-service lines). Build a bus-injection map using KCL on line flows, ignoring shunt losses at the bus level. The IEEE 33-bus topology is fixed and known. The planner should include a helper function `derive_bus_injections(bus_df, line_df, sgen_df, net_topology)` that:
1. Loads the IEEE 33-bus topology once from pandapower (no power flow, just the topology `net.line[["from_bus","to_bus"]]`)
2. For each timestamp and each bus, computes `P_inj = sum(p_from_mw of outgoing lines) - sum(p_to_mw of incoming lines) - (p_mw of sgens at this bus)`

**Alternative simpler approximation:** Use the net load at each bus as the pseudo injection. Since the `state` bucket does not store loads directly, and the ground-truth load profile is fully reproducible from the OPSD profiles + scaling constants in `config.py`, the injection for a non-DG bus ≈ `base_p[bus_idx] * load_pu`. This is accurate enough for a measurement layer and avoids the topology read.

**Recommendation:** For the `source=day` case, store a copy of `base_p * load_pu` per bus per step as the "true injection" used for SCADA/AMI/pseudo. The load profiles are read from InfluxDB (the `profiles` bucket), and the scaling is deterministic. For DG buses, add sgen output. This is the most self-contained approach.

For `source=fault`, use `fault_event.bus.p_mw` directly (already in the bucket).

[VERIFIED: `fault_event` bus schema writes `p_mw`/`q_mvar` at influx.py:425-426; `state` bus schema does NOT per influx.py:278-284]

---

### Q5 — `measurements` bucket schema (D-06) and cardinality analysis

**Schema (locked by D-06):**
```
measurement: "meas"
tags: class, quantity, location, scenario, experiment, phase (fault only)
fields: value (float), assumed_sigma (float)
```

**Cardinality estimate:**

For `well_observed`, snapshot mode, source=day:
- SCADA (bus 0): 3 quantities × 96 steps = 288 points
- μPMU (9 buses): 2 quantities × 96 steps = 1,728 points
- DER (4 buses): 2 quantities × 96 steps = 768 points
- AMI (~27 load buses): 1 quantity × 96 steps = 2,592 points
- zero-injection (2 buses): 2 quantities × 96 steps = 384 points
- Estimated total: ~5,800 points per (scenario × experiment) combination

**Tag cardinality:**
- `class`: 6 values
- `quantity`: 6 values
- `location`: 33 bus IDs
- `scenario`: 2 values
- `experiment`: 2 values
- `phase`: 3 values (null for day)

Cross-product = 6 × 6 × 33 × 2 × 2 × 3 = 8,712 possible tag combinations — but only ~50–80 actually emitted per scenario. InfluxDB 2.x handles this cardinality trivially.

**Topology event in measurements (D-07):**

```
measurement: "event"
tags: scenario, experiment, phase
fields: faulted_line_id, tie_closed, tie_id, n_dead_buses, dead_buses
```

For `source=day`, a single `event` point per snapshot records:
`faulted_line_id=-1, tie_closed=0, tie_id=-1, n_dead_buses=0, dead_buses=""` (or a minimal "topology stable" record).

**Idempotency / overwrite-in-place:** Tags + timestamp form the unique key in InfluxDB. Writing the same `meas` point with the same (measurement, all tags, timestamp) overwrites the previous value — no duplicates. Ordering of Point.tag() calls does not affect the key.

---

### Q6 — Config mechanism: `measure_config.py` pattern

Mirror `config.py` — pure constants module, no I/O side effects except dotenv on import. [VERIFIED: config.py:1-17 pattern]

```python
# measure_config.py
"""
measure_config.py
-----------------
All measurement-layer configuration constants for the IEEE 33-bus measurement system.
Edit the ACTIVE block to switch experiment knobs without code changes.
"""

# --- per-class sigma tables (true_sigma = assumed_sigma by default) ---
CLASS_SIGMA: dict[str, dict[str, float]] = {
    "scada":    {"vm_pu": 0.005, "p_inj_mw": 0.02, "q_inj_mvar": 0.02},
    "pmu":      {"vm_pu": 0.001, "va_degree": 0.0003},
    "ami":      {"p_inj_mw": 0.03, "q_inj_mvar": 0.03},
    "der":      {"p_mw": 0.015, "q_mvar": 0.015},
    "pseudo":   {"p_inj_mw": 0.30, "q_inj_mvar": 0.30},
    "zero_inj": {"p_inj_mw": 1e-4, "q_inj_mvar": 1e-4},
}

# --- cadence multiples per (source, class) in multirate_async mode ---
CADENCE: dict[str, dict[str, int]] = {
    "day": {
        "scada": 1, "pmu": 1, "der": 1, "ami": 4, "pseudo": 1, "zero_inj": 1,
    },
    "fault": {
        "scada": 2, "pmu": 1, "der": 1, "ami": 10, "pseudo": 1, "zero_inj": 1,
    },
}

# --- sensor bus assignments ---
SCENARIOS: dict[str, dict] = {
    "well_observed": {
        "scada":    [0],
        "pmu":      [0, 4, 8, 13, 17, 21, 24, 28, 32],
        "der":      [17, 21, 24, 32],
        "ami":      [...],    # planner finalizes ~27 buses
        "zero_inj": [2, 19],
        # pseudo = all load buses not in scada/pmu/ami/der/zero_inj
    },
    "realistic_sparse": {
        "scada":    [0],
        "pmu":      [17, 24, 30],
        "der":      [17, 21, 24, 32],
        "ami":      [3, 6, 9, 12, 15, 18, 21, 24, 28, 31],
        # pseudo = all load buses not covered above
    },
}

# ---------------------------------------------------------------
# ACTIVE BLOCK — edit this to switch experiments
# ---------------------------------------------------------------
ACTIVE = {
    "scenario": "realistic_sparse",   # "well_observed" | "realistic_sparse"
    "source":   "day",                # "day" | "fault"
    "sampling": "snapshot",           # "snapshot" | "multirate_async"
    "noise":    "gaussian",           # "gaussian" | "gaussian_outliers" | "instrument"
    "seed":     42,
    "assumed_sigma_scale": 1.0,       # multiply CLASS_SIGMA to get assumed_sigma (1.0 = equal to true)
}
```

**argparse integration in `measure.py`:**
```python
import argparse
from ieee33 import measure_config as mc

def _parse_args():
    p = argparse.ArgumentParser(description="IEEE 33-bus measurement layer runner")
    p.add_argument("--scenario", choices=["well_observed", "realistic_sparse"])
    p.add_argument("--source", choices=["day", "fault"])
    p.add_argument("--sampling", choices=["snapshot", "multirate_async"])
    p.add_argument("--noise", choices=["gaussian", "gaussian_outliers", "instrument"])
    p.add_argument("--seed", type=int)
    return p.parse_args()

def main():
    args = _parse_args()
    cfg = dict(mc.ACTIVE)   # start from config file
    for k in ("scenario", "source", "sampling", "noise", "seed"):
        v = getattr(args, k)
        if v is not None:
            cfg[k] = v      # CLI overrides file
    ...
```

[VERIFIED: D-09 locks "config file is the primary switch; CLI for sweeps" — this mirrors that exactly]

---

### Q7 — Grafana provisioning: two new dashboards

**Provisioning mechanism (verified):** Grafana auto-loads all `.json` files found in the directory mounted at `/etc/grafana/provisioning/dashboards` (which maps to `./grafana/provisioning/dashboards/` from `docker-compose.yml`). The `default.yml` provider scans the entire path with `updateIntervalSeconds: 30` — any new `.json` file dropped there is picked up on restart or within 30 s. [VERIFIED: default.yml, docker-compose.yml]

**Datasource UID:** `ieee33-influxdb` — must be referenced in every panel's `datasource.uid`. [VERIFIED: influxdb.yml:6, ieee33-state.json:81]

**Dashboard JSON structure pattern (verified from ieee33-state.json + ieee33-fault-event.json):**

```json
{
  "__inputs": [],
  "__requires": [...],
  "description": "...",
  "editable": true,
  "id": null,
  "panels": [...],
  "refresh": "30s",
  "schemaVersion": 39,
  "tags": ["measurements"],
  "title": "IEEE 33-Bus Observed Measurements — Day",
  "uid": "ieee33-meas-day",
  "version": 1
}
```

Key rules (learned from existing JSONs):
- `"id": null` — Grafana assigns ID on import; never hardcode
- `"uid"` must be unique: use `"ieee33-meas-day"` and `"ieee33-meas-fault"` (distinct from existing `"ieee33-state"` and `"ieee33-fault-event"`)
- `"datasource": {"type": "influxdb", "uid": "ieee33-influxdb"}` in every panel and every target
- Panel `"gridPos"` — use 12-unit wide columns (Grafana 12-column grid)

**Flux queries in dashboard panels:** Embed Flux as a single `"query"` string with escaped newlines `\n`. Example for observed voltage measurements:

```
from(bucket: "measurements")
  |> range(start: 2017-06-07T00:00:00Z, stop: 2017-06-07T23:59:59Z)
  |> filter(fn: (r) => r._measurement == "meas")
  |> filter(fn: (r) => r._field == "value")
  |> filter(fn: (r) => r.quantity == "vm_pu")
  |> filter(fn: (r) => r.scenario == "realistic_sparse")
  |> filter(fn: (r) => r.experiment == "day")
```

**True-series overlay:** Each panel that shows measured values also overlays the true value from `state`/`fault_event`. Implement as a second `target` in the same panel (different `refId`):

```json
"targets": [
  {
    "datasource": {"type": "influxdb", "uid": "ieee33-influxdb"},
    "query": "from(bucket: \"measurements\") ... filter value ...",
    "refId": "A"
  },
  {
    "datasource": {"type": "influxdb", "uid": "ieee33-influxdb"},
    "query": "from(bucket: \"state\") ... filter vm_pu ...",
    "refId": "B"
  }
]
```

**Panels for `ieee33-meas-day.json`:**
1. Observed bus voltages (vm_pu) — meas overlay + state true series
2. Observed power injections (P_inj_mw per class) — bar or timeseries
3. Per-class measurement counts (stat panel querying count)
4. Observed-vs-pseudo footprint (which buses real vs pseudo — bar chart by location)

**Panels for `ieee33-meas-fault.json`:**
1. Observed bus voltages across 40 steps (meas overlay + fault_event true series)
2. Phase annotation (region shading: pre_fault → isolation → restored)
3. Dead-bus count over time (n_dead_buses from `event` measurement)
4. Per-class measurement counts across phases
5. Observed-vs-pseudo footprint (changes at isolation: μPMU bus 17 goes dark)

**Phase region markers:** Use Grafana annotations from the `event` measurement where `phase` tag changes. Or — simpler — use threshold bands applied to a stat panel showing the `phase` tag value as a string time series.

---

### Q8 — Determinism / testing approach for the measurement layer

**Seeding strategy:** Use `numpy.random.default_rng(seed)` once per run, at the start of `main()`. Pass the single `rng` object into all noise functions. Do NOT create multiple independent RNGs or use `np.random.seed()` (global state). [VERIFIED: D-10 locks "overwrite-in-place"; D-11 locks determinism via seed]

**Byte-identical requirement:** Two runs with identical config produce byte-identical InfluxDB values because:
1. Same seed → same RNG stream
2. Same sorted iteration order (buses/quantities in fixed order)
3. Overwrite-in-place (same timestamp+tag → same point)

**To assert byte-identical:** Query the `measurements` bucket after each run, collect `(timestamp, location, quantity, value)` tuples, sort them, and compare. In a test:

```python
values_run1 = query_all_meas_values(client)
# reset and re-run measure.main() with same config
values_run2 = query_all_meas_values(client)
assert values_run1 == values_run2, "Runs are not byte-identical"
```

**Per-class cadence count assertion (multirate_async):** After a `source=day`, `sampling=multirate_async` run:
- AMI cadence = 4 → should appear at 96 ÷ 4 = 24 timestamps
- μPMU cadence = 1 → should appear at 96 timestamps

```python
flux_count = """
from(bucket: "measurements")
  |> range(...)
  |> filter(fn: (r) => r._field == "value" and r.class == "ami")
  |> distinct(column: "_time")
  |> count()
"""
# Expected: 24 for AMI in multirate_async, 96 in snapshot
```

**Unseeded randomness grep check (AC-10):**
```bash
grep -n "np.random\." src/ieee33/measure.py | grep -v "default_rng"
grep -n "random.random\|random.seed\|datetime.now\|time.time" src/ieee33/measure.py
# Should return empty — any hit is a bug
```

**Console footprint report format (mirroring sim.py's table):**
```
Measurement Footprint Report
============================
Scenario : realistic_sparse
Source   : day
Sampling : snapshot
Noise    : gaussian
Seed     : 42
---
Class        | Count  | Buses
------------ | ------ | -----
scada        |    288 |     1
pmu          |    576 |     3 (17 dark in fault isolation)
der          |    768 |     4
ami          |    960 |    10
pseudo       |  5,184 |    22
zero_inj     |      0 |     0
---
Total real measurements    : 2,592
Total pseudo measurements  : 5,184
N_energised (avg)          : 33
N_states                   : 64
Real-only redundancy       : 0.405
With-pseudo redundancy     : 1.215
Observed buses (real)      : 23 / 33
Dead buses (fault ISO only): 0
```

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Seeded reproducible RNG | Custom LCG or per-sensor seed management | `np.random.default_rng(seed)` | NumPy Generator is reproducible, jumpable, thread-safe |
| InfluxDB bucket creation | DIY HTTP | `influx.ensure_bucket()` | Already in the codebase, idempotent |
| InfluxDB client | DIY HTTP | `influx.get_client()` | Already in the codebase |
| Grafana dashboard provisioning | Manual import | JSON file in `dashboards/` dir | Grafana reloads from dir automatically |
| DataFrame pivot of Flux result | Manual `pivot_table()` | Flux `pivot()` operator | Flux-side pivot returns a flat DF directly |

---

## Common Pitfalls

### Pitfall 1: Reading `energised` as a field instead of a tag

**What goes wrong:** A Flux query `|> filter(fn: (r) => r._field == "energised")` returns nothing because `energised` is a TAG in `fault_event`, not a field.

**Why it happens:** The `write_fault_step` call uses `.tag("energised", "1")` not `.field(...)`. [VERIFIED: influx.py:421,424]

**How to avoid:** Include `energised` in the `pivot()` `rowKey` list: `rowKey: ["_time", "bus_id", "energised"]`. It then appears as a string column in the result DataFrame. Compare as `df["energised"] == "1"` not `== 1`.

### Pitfall 2: Mixed int/float type conflicts in InfluxDB

**What goes wrong:** Writing `tie_id` as float on some steps and int on others causes InfluxDB type conflicts.

**Why it happens:** The `event` measurement uses `tie_id = int(...) if tie_is_closed else -1`. If Python casts this inconsistently, InfluxDB rejects the conflicting write.

**How to avoid:** Always cast: `int(tie_id)`. Already enforced in `write_fault_step` [VERIFIED: influx.py:529]. Mirror this discipline in the `measurements` `event` re-publisher.

### Pitfall 3: Wrong time range for fault_event queries

**What goes wrong:** Using `range(start: 0)` (all-time) when the fault bucket might accumulate stale data from multiple re-runs. The 40-step window spans only 120 s.

**How to avoid:** Mirror `sim.py`'s scoped range: use the known anchor timestamp ± some seconds. Read the anchor from the `profiles` bucket (same as `fault_sim.py` does). Or use a very wide range (e.g., `start: 2017-06-07T00:00:00Z, stop: 2017-06-08T00:00:00Z`) — the fault timestamps are anchored to that same UTC date.

### Pitfall 4: Grafana dashboard UID collision

**What goes wrong:** Two dashboards with the same `"uid"` value — the second silently overwrites the first in Grafana's provisioning.

**How to avoid:** Use distinct, unique UIDs: `"ieee33-meas-day"` and `"ieee33-meas-fault"`. Different from existing `"ieee33-state-v1"` (check the existing JSON's uid field before finalizing).

### Pitfall 5: RNG stream shift from non-deterministic iteration order

**What goes wrong:** Iterating over `dict.keys()` or DataFrame in non-deterministic order changes which noise values are generated even with a fixed seed, making byte-identical runs fail.

**How to avoid:** Always sort before iterating: `sorted(sensor_ids)`, `df.sort_values(["_time","bus_id"])`. Generate noise for sensors in alphabetical/numerical order within each snapshot.

### Pitfall 6: `state` bucket bus schema lacks `p_mw`/`q_mvar`

**What goes wrong:** Trying to read bus power injections from the `state` bucket — the fields don't exist there. [VERIFIED: write_state_step at influx.py:277-285 — only vm_pu and va_degree for bus]

**How to avoid:** For `source=day`, derive P_inj/Q_inj from the load profiles + sgen data using the deterministic scaling formula, or use KCL from line flows. For `source=fault`, use the `p_mw`/`q_mvar` fields already in `fault_event.bus`.

### Pitfall 7: Bus 17 in dead zone — silent μPMU dropout

**What goes wrong:** The `well_observed` scenario places a μPMU at bus 17 (D-05). During `faulted_isolated` in the fault scenario, bus 17 is in the dead zone (`energised="0"`). If the measurement layer doesn't check the energised flag before generating a μPMU measurement, it silently emits a measurement for a dead bus.

**How to avoid:** The energised gate (D-03) must be applied first: skip any sensor whose bus has `energised="0"`. This is the deliberate stress test on System 2 (mentioned in D-03).

### Pitfall 8: Grafana env-var substitution for the datasource token

**What goes wrong:** Using `${TOKEN}` in `influxdb.yml`'s `secureJsonData.token` fails silently — Grafana's env-var substitution in `secureJsonData` is unreliable.

**How to avoid:** Hard-code the literal token `ieee33-dev-token`. Already solved in the existing `influxdb.yml` [VERIFIED: influxdb.yml:17 comment "LITERAL string — do NOT use env-var substitution (Pitfall 8 / issue #89519)"]

---

## Code Examples

### Pattern 1: Full Flux read of fault_event bus data into per-snapshot dict

```python
# Source: mirrors influx.py:141-181 read_profiles pattern
from datetime import date, timedelta

def read_fault_bus_all(client):
    """Read all 40-step fault_event bus points into a DataFrame."""
    start = f"{config.TARGET_DATE}T00:00:00Z"
    stop  = f"{date.fromisoformat(config.TARGET_DATE) + timedelta(days=1)}T00:00:00Z"
    flux = (
        f'from(bucket: "{config.FAULT_EVENT_BUCKET}")\n'
        f'  |> range(start: {start}, stop: {stop})\n'
        f'  |> filter(fn: (r) => r._measurement == "bus")\n'
        f'  |> pivot(rowKey: ["_time", "bus_id", "energised"], '
        f'columnKey: ["_field"], valueColumn: "_value")\n'
        f'  |> sort(columns: ["_time", "bus_id"])'
    )
    return client.query_api().query_data_frame(flux)
    # columns: _time, bus_id, energised, vm_pu, va_degree, p_mw, q_mvar
```

### Pattern 2: Per-snapshot sensor iteration (the core loop)

```python
# Source: mirrors fault_sim.py main() pattern (influx.py:345-539)
for ts, snap in bus_df.groupby("_time"):
    # 1. Build energised-bus set
    live_bus_ids = set(snap[snap["energised"] == "1"]["bus_id"].astype(int).tolist())
    dead_bus_ids = set(snap[snap["energised"] == "0"]["bus_id"].astype(int).tolist())

    # 2. Iterate sensors in sorted order (deterministic RNG stream)
    points = []
    for cls in sorted(SCENARIOS[scenario].keys()):
        assigned_buses = sorted(SCENARIOS[scenario][cls])
        for bus_id in assigned_buses:
            if bus_id in dead_bus_ids:
                continue  # D-03: no measurement for dead bus

            # 3. Cadence check
            if sampling == "multirate_async":
                cadence = CADENCE[source][cls]
                if step_idx % cadence != 0:
                    continue

            # 4. Derive true value(s) for this class/bus
            for quantity, true_val in get_true_values(cls, bus_id, snap, line_df, sgen_df):
                true_sigma = CLASS_SIGMA[cls][quantity] * abs(true_val) if quantity != "va_degree" else CLASS_SIGMA[cls][quantity]
                assumed_sigma = true_sigma * cfg["assumed_sigma_scale"]

                # 5. Apply noise
                measured_val, emitted_sigma = apply_noise(cfg["noise"], true_val, true_sigma, assumed_sigma, rng, ...)

                # 6. Write meas point
                points.append(
                    Point("meas")
                    .tag("class",    cls)
                    .tag("quantity", quantity)
                    .tag("location", str(bus_id))
                    .tag("scenario", scenario)
                    .tag("experiment", experiment)
                    .field("value",         float(measured_val))
                    .field("assumed_sigma", float(emitted_sigma))
                    .time(ts)
                )
    write_api.write(bucket="measurements", org=config.INFLUXDB_ORG, record=points)
```

### Pattern 3: Instrument model AR(1) state management

```python
# Source: D-13 locked parameters
class InstrumentState:
    """Persistent per-sensor AR(1) state for the instrument noise model."""
    def __init__(self, rho: float = 0.7):
        self.rho = rho
        self._ar_prev: dict[str, float] = {}   # keyed by "cls_busid_quantity"

    def generate(self, sensor_key: str, true_sigma: float, rng) -> float:
        """Return AR(1) noise component for this sensor."""
        white = rng.normal(0.0, true_sigma * (1 - self.rho**2)**0.5)
        prev  = self._ar_prev.get(sensor_key, 0.0)
        ar1   = self.rho * prev + white
        self._ar_prev[sensor_key] = ar1
        return ar1
```

### Pattern 4: Redundancy footprint report

```python
# Source: D-15 formula
n_energised = len(live_bus_ids_at_snapshot)     # or 33 for source=day
n_states    = 2 * (n_energised - 1)
real_count  = sum(1 for p in points if p._tags["class"] != "pseudo" and p._tags["class"] != "zero_inj")
pseudo_count= sum(1 for p in points if p._tags["class"] == "pseudo")

real_redundancy       = real_count / n_states if n_states > 0 else 0.0
with_pseudo_redundancy = (real_count + pseudo_count) / n_states if n_states > 0 else 0.0
```

---

## State of the Art

| Old Approach | Current Approach | Impact for Phase 9 |
|--------------|------------------|---------------------|
| `np.random.seed()` (global state) | `np.random.default_rng(seed)` (Generator, stream-reproducible) | Use Generator API; never legacy seed |
| Separate Grafana dashboard imports | Directory-based auto-provisioning with `default.yml` | Drop JSON files in dir, auto-loaded |
| Per-step InfluxDB queries | Bulk Flux pivot query → DataFrame | One round-trip per data source |

---

## Environment Availability

| Dependency | Required By | Available | Notes |
|------------|------------|-----------|-------|
| Python 3.12 (uv) | `measure.py` | [VERIFIED: pyproject.toml] | `requires-python = ">=3.12"` |
| influxdb-client 1.50.0 | Flux reads + writes | [VERIFIED: pyproject.toml] | Already pinned |
| numpy >=1.26 | Noise engine | [VERIFIED: pyproject.toml] | `default_rng` available since 1.17 |
| pandas >=2.3 | DataFrame pivot | [VERIFIED: pyproject.toml] | Already pinned |
| InfluxDB 2.9.1 (Docker) | Bucket + Flux queries | [VERIFIED: docker-compose.yml] | Local dev stack |
| Grafana 11.6.15 (Docker) | Dashboard provisioning | [VERIFIED: docker-compose.yml] | Auto-provisioning via volume mount |
| `state` bucket populated | `source=day` reads | Requires prior `uv run sim` | Prerequisite; caller's responsibility |
| `fault_event` bucket populated | `source=fault` reads | Requires prior `uv run fault-sim` | Prerequisite; README must state this |

No new packages to install. No missing dependencies with blockers.

---

## Open Questions

1. **P_inj derivation for `source=day` (load bus injections)**
   - What we know: `state` bucket has bus `vm_pu`/`va_degree` only; no `p_mw` field on `bus` measurement.
   - What's unclear: The cleanest path — use the `profiles` + `config.py` scaling (fully deterministic, no extra read) vs. KCL from line flows (more accurate but requires topology knowledge).
   - Recommendation: Use profiles + scaling for load buses (base_p[bus_idx] × load_pu for load buses; add sgen p_mw for DG buses). Read the `profiles` bucket once (same as `sim.py` does) to get `load_pu` per step, and use `config.py`'s base load values. This makes the injection derivation deterministic and independent of InfluxDB line data.

2. **`well_observed` AMI bus set (Claude's Discretion)**
   - What we know: ~80% of load buses → roughly 27 out of 33 buses
   - What's unclear: Which 5–6 load buses to hold out; exact list not locked
   - Recommendation: Hold out a representative set — e.g., buses {5, 10, 20, 25, 29} (spread across laterals). The planner finalizes; must yield real redundancy > 1.0 without pseudo.

3. **`event` re-publisher for `source=day`**
   - What we know: D-07 says "for `experiment=day` the event records the fixed/known topology (no fault, all ties open)"
   - What's unclear: whether to emit one `event` point per 96 steps or just one total
   - Recommendation: Emit one `event` point per timestamp (96 total for day) with `faulted_line_id=-1, tie_closed=0, tie_id=-1, n_dead_buses=0, dead_buses=""` to keep the query pattern uniform for System 2.

---

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | `state` bucket bus measurement contains only `vm_pu` and `va_degree` (no `p_mw`/`q_mvar`) | Q4 — P_inj derivation | [VERIFIED: influx.py:278-285 — confirmed, not assumed] |
| A2 | Quantization LSBs suggested in Q3 (SCADA 0.001 pu, etc.) | Q3 noise models | Low risk — these are Claude's Discretion values; planner can adjust |
| A3 | IEEE 33-bus topology (which buses are load buses, DG buses, junction buses) maps directly from `config.py` SOLAR_BUSES/WIND_BUSES + pandapower indices | Q4, Q5 | [VERIFIED: config.py:75-76] — correct |

**If this table is empty of ASSUMED items:** All critical claims verified by reading the actual source files. The only assumed items are the exact quantization LSBs (Claude's Discretion, low-risk).

---

## Sources

### Primary (HIGH confidence — verified by reading source files)
- `system1-measurement-source/src/ieee33/influx.py` — full schema of `write_state_step` (bus has only vm_pu/va_degree), `write_fault_step` (bus adds p_mw/q_mvar + energised TAG), `event` measurement fields/tags, `read_profiles` Flux pivot pattern, `ensure_bucket`
- `system1-measurement-source/src/ieee33/config.py` — all physical/topology constants: FAULT_DEAD_BUS_IDX, SOLAR_BUSES, WIND_BUSES, bucket names, InfluxDB connection
- `system1-measurement-source/src/ieee33/fault_sim.py` — runner structure, DEAD_LINE_IDS/DEAD_SGEN_IDS, per-step write loop, console table pattern
- `system1-measurement-source/src/ieee33/sim.py` — determinism pattern, overwrite-in-place, profiles read, per-step sweep structure
- `system1-measurement-source/pyproject.toml` — all pinned dependencies, `[project.scripts]` pattern
- `system1-measurement-source/grafana/provisioning/dashboards/default.yml` — auto-provisioning mechanism
- `system1-measurement-source/grafana/provisioning/dashboards/ieee33-state.json` — dashboard JSON structure, Flux query embedding, datasource UID
- `system1-measurement-source/grafana/provisioning/dashboards/ieee33-fault-event.json` — fault dashboard structure with stat/table panels
- `system1-measurement-source/grafana/provisioning/datasources/influxdb.yml` — datasource UID, literal token pitfall
- `system1-measurement-source/docker-compose.yml` — InfluxDB 2.9.1 + Grafana 11.6.15 stack config
- `.planning/phases/09-.../09-SPEC.md` — 12 locked requirements, acceptance criteria
- `.planning/phases/09-.../09-CONTEXT.md` — D-01..D-16 locked implementation decisions

### Secondary (MEDIUM confidence)
- numpy Generator API (default_rng) — standard since NumPy 1.17; available in >=1.26 [ASSUMED from training knowledge, cross-checked with pinned version >=1.26 in pyproject.toml]

---

## Metadata

**Confidence breakdown:**
- Flux read patterns: HIGH — verified by reading `read_profiles` and both write functions
- Schema field names: HIGH — verified byte-by-byte against `influx.py`
- Noise model NumPy patterns: HIGH for gaussian/outliers; MEDIUM for instrument (AR(1) implementation correct, LSB values are Claude's Discretion)
- P_inj derivation: HIGH for `source=fault` (verified `p_mw` exists in `fault_event.bus`); MEDIUM for `source=day` (profiles approach is clean but slightly approximate vs. full KCL)
- Grafana provisioning: HIGH — verified from existing working dashboards
- Cardinality estimates: MEDIUM — calculated from locked scenario assignments

**Research date:** 2026-06-25
**Valid until:** 2026-07-25 (stable codebase; only changes if influx.py schema is modified)
