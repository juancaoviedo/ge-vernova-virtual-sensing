# System 1 — IEEE 33-Bus DER Measurement Source

This folder is **System 1** of a two-system virtual-sensing design.
It produces a ground-truth dataset: 96 full power-flow snapshots of the
[IEEE 33-bus distribution feeder](https://ieeexplore.ieee.org/document/294727) (Baran & Wu)
enhanced with four renewable DG units (two solar PV, two wind), RPC shunt capacitors,
and a regulating OLTC feeder transformer — driven by a real high-DER German summer day
(2017-06-07) from the [Open Power System Data](https://open-power-system-data.org/)
15-minute time series.

The 96 snapshots are persisted to a local InfluxDB 2.x instance and visualised through
a pre-provisioned Grafana dashboard — with **no manual setup required** once the stack
is running.

**System 2** (virtual-sensing estimator) is a later phase. This dataset is the forward
contract: the `state` bucket schema is what System 2 will consume as its ground-truth
reference.

---

## Prerequisites

| Tool | Verified version | Install |
|------|-----------------|---------|
| Docker + Docker Compose v2 | Docker 28.x, Compose 2.35.x | [docs.docker.com](https://docs.docker.com/get-docker/) |
| uv | 0.7.x | `curl -Ls https://astral.sh/uv/install.sh \| sh` |
| Python | 3.12 (managed by uv) | uv downloads it automatically |

One-time internet access is required for the `ingest` step only (fetches the 107 MB
OPSD CSV). All subsequent `sim` runs are offline.

---

## The Rhythm

From a clean checkout, run these steps in order:

### Step 1 — Install pinned Python dependencies

```bash
uv sync
```

Reads `pyproject.toml` + `uv.lock` and creates `.venv` with all pinned dependencies
(pandapower 3.4.0, influxdb-client 1.50.0, pandas, numpy, requests, python-dotenv).
Only needed once (or after pulling new lockfile changes).

### Step 2 — Start infrastructure

```bash
docker compose up -d        # equivalent: make up
```

Starts two containers bound to `127.0.0.1` only:
- **InfluxDB 2.9.1** at http://localhost:8086 (org `ieee33`, bucket `profiles` auto-created,
  token `ieee33-dev-token`)
- **Grafana 11.6.15** at http://localhost:3000 (anonymous access; dashboard
  auto-provisioned — no manual setup)

Wait a few seconds for InfluxDB to finish its first-run bootstrap before running ingest.

### Step 3 — (Optional) Validate base-case network

```bash
uv run validate             # equivalent: make validate
```

Runs a plain `case33bw` power flow (no DER, no OLTC, no capacitors) and asserts that
the minimum bus voltage matches the Baran & Wu benchmark (≈ 0.913 pu at bus 18,
tolerance ± 0.005 pu). Confirms the network model is correct before adding enhancements.

### Step 4 — Ingest OPSD profiles (one-time fetch)

```bash
uv run ingest               # equivalent: make ingest
```

Streams the 107 MB OPSD 15-minute CSV over HTTP, extracts the 96 rows for 2017-06-07
(a high-DER German summer day: solar_max = 0.474, wind_mean = 0.708), normalises them to
unit-interval profiles, and writes 96 points to the `profiles` InfluxDB bucket.

**IMPORTANT — no fallback:** if the OPSD endpoint is unreachable, the script halts with
a clear message asking you to download `time_series_15min_singleindex.csv` manually and
retry. There is no local-file fallback — the fetch is required.

Idempotent: re-running replaces the 96 profile points in place (same timestamps = overwrite).

### Step 5 — Run the 96-step simulation

```bash
uv run sim                  # equivalent: make sim
```

Reads the 96 profile points from InfluxDB, then runs 96 quasi-static Newton-Raphson
power flows on the enhanced IEEE 33-bus network (with OLTC, DG, and RPC shunts active).
Each step writes a full state snapshot to the `state` InfluxDB bucket:

- `bus` measurement (tag `bus_id`): `vm_pu`, `va_degree` for all 33 buses
- `line` measurement (tag `line_id`): `p_from_mw`, `q_from_mvar`, `loading_percent`,
  `pl_mw`, `ql_mvar` for all in-service lines
- `sgen` measurement (tag `sgen_id`): `p_mw`, `q_mvar` for all 4 DG units
- `system` measurement: `total_load_mw`, `total_gen_mw`, `total_loss_mw`, `vmin_pu`,
  `vmax_pu`, `slack_p_mw`, `slack_q_mvar`, `tap_pos`, `shift_degree`

Prints `sim OK — 96 snapshots written` on success.

Idempotent: re-running overwrites the same 96 timestamp-keyed snapshots — identical
dataset every run.

### Step 6 — Open Grafana and InfluxDB

**Grafana dashboard:** http://localhost:3000

Open in a browser. Anonymous access is enabled for the local demo — no login required.
The **"IEEE33 DER State — 2017-06-07 High-DER DE Day"** dashboard is auto-provisioned
(no manual datasource or dashboard import needed). It covers:

1. **Bus Voltage Profile / Envelope (pu)** — key DER buses + slack-side reference
2. **Line Loadings (%)** — feeder trunk and representative lateral lines
3. **Total System Losses (MW)** — dips at midday as DER reduces net feeder current
4. **DG Output — Solar & Wind (MW)** — solar bell-curve, wind flat-ish profile
5. **Slack / Substation Feed-in (MW)** — goes negative midday (reverse power flow)
6. **OLTC Tap Position** — integer steps −5 to +5; steps on voltage deadband excursion

**InfluxDB Data Explorer:** http://localhost:8086
Use org `ieee33`, token `ieee33-dev-token` to inspect the `profiles` and `state` buckets
directly.

### Shortcut — Run the full pipeline in one command

```bash
make all          # runs: up → ingest → sim
```

Then open Grafana at http://localhost:3000.

### Teardown

```bash
make down         # stop containers (keeps volumes / data)
make clean        # stop containers AND wipe all data volumes (fresh start)
```

---

## What You Should See (Interview Narrative)

On 2017-06-07 — a high-DER German summer day — the four scaled DG units (560 kW each,
total 2.24 MW = ~60% of peak load) drive a set of grid-physics effects visible in the
dashboard:

- **Midday voltage rise:** Solar PV ramps up from ~06:00 UTC, peaks around 12:00 UTC.
  At DER buses (17, 21, 24, 32), voltages rise toward and above 1.0 pu.
- **Reverse power flow:** Around noon, total DER generation exceeds feeder demand and
  the slack bus feed-in (`slack_p_mw`) trends toward — and often through — zero.
  Negative values mean power is flowing back toward the substation.
- **OLTC tap behaviour:** The regulating transformer (OLTC deadband 0.95–1.05 pu)
  maintains the LV bus within the band. On this day, the LV-side bus stays within the
  deadband, so the OLTC tap remains at neutral (0). However, buses 12–15 on the long
  lateral feeder dip to ~0.949 pu at peak evening (steps 68–73), a real lateral-feeder
  effect not captured by the OLTC (which only regulates bus 0).
- **Loss dip at noon:** As DER generation reduces net feeder currents, I²R losses
  (`total_loss_mw`) dip noticeably at midday. They rise again at peak evening demand.

This is the ground-truth dataset that System 2 (virtual-sensing estimator) will consume:
it exposes how DSSE with a sparse sensor set would need to reconstruct the dark nodes.

---

## Data Model (Forward Contract for System 2)

Two InfluxDB buckets:

| Bucket | Contents | Points | Description |
|--------|----------|--------|-------------|
| `profiles` | `profiles` measurement | 96 | One-time OPSD fetch: `load_pu`, `solar_pu`, `wind_pu` per 15-min slot, 2017-06-07 UTC |
| `state` | `bus`, `line`, `sgen`, `system` | 96 per entity | Per-run power-flow snapshots (all 33 buses, 29 active lines, 4 sgens, 1 system aggregate) |

Tags: `bus_id` (0–32), `line_id` (0–31 active), `sgen_id` (0–3).

The `state` schema is the interface that System 2 will query as reference ground truth.
Do not rename fields or tags without updating System 2's Flux queries.

---

## Security Note — LOCAL DEV ONLY

**This stack is for local development and interview demonstration only.**

- `ieee33-dev-token` and `ieee33-admin-pw` are **fixed development credentials**, not
  production secrets. They are intentionally committed to the repo as a required workaround
  for Grafana provisioning reliability (Pitfall 8 / GitHub issue #89519).
- All ports are bound to `127.0.0.1` (not `0.0.0.0`), so the services are not accessible
  from other machines on the network.
- Grafana anonymous access is enabled for the local demo only.
- **Do not deploy this configuration as-is to any shared, cloud, or production environment.**

---

## Determinism

Re-running `uv run sim` (or `make sim`) always produces the **identical 96-snapshot dataset**.
InfluxDB overwrites existing points with the same measurement + tag + timestamp combination.
There are no stochastic elements: the Newton-Raphson solver, OPSD profiles, and DG scaling
are all deterministic. This ensures the interview demo is reproducible from any clean state.

---

## Fault & Reconfiguration Scenario (Phase 8.1)

A separate, re-runnable quasi-steady-state fault/reconfiguration dataset built on the same
System 1 model. It replicates the article's Section-8 fault → isolate → tie-restore sequence
as a 40-step (2-min window at 3-s spacing), three-block time series frozen at the evening-peak
operating point. Produced by `fault_sim.py` and stored in the dedicated `fault_event` bucket —
the `profiles` and `state` buckets are untouched.

### Run it

```bash
docker compose up -d     # if not already running (starts InfluxDB + Grafana)
uv run ingest            # one-time; populates the profiles bucket the runner freezes on
uv run fault-sim         # writes 40 fault-event snapshots to the fault_event bucket
```

`fault-sim` is deterministic and zero-arg. Re-running overwrites the same 40 snapshots
in place — the dataset is identical every run. While running, it prints a per-step console
table showing `step / phase / vmin / served load / tap / dead count` for each of the 40
snapshots.

### What it does

- **Permanent 3-phase fault** on line index 7 (article branch 8→9): the line is taken
  out of service and never re-energised in this scenario.
- **Isolation of the downstream zone** (buses 8–17, lines 8–16 out of service): the
  in-zone DG at bus 17 loses its grid connection and the OLTC tap is pinned at the
  evening-peak value (−2, BOOST) because its reference bus (17) is inside the dead zone.
  The 10 de-energised buses show voltage collapse to 0 pu. Served load drops from
  ~3.29 MW to ~2.69 MW (≈ 0.60 MW shed).
- **Tie-34 closure** (normally-open tie index 34, article 12↔22): the algorithm checks
  all candidate tie lines via graph traversal, selects tie 34 as the restoration path,
  and asserts the result is still a radial tree (`nx.is_tree` gate).
- **Back-feed and full restoration**: the de-energised zone is re-energised via tie 34.
  Served load recovers to ~3.29 MW. Restored minimum bus voltage reaches ~0.997 pu
  (clean in-band, no shortfall flag).
- **Data continuity (D-05)**: faulted line 7 is zero-filled across all 40 snapshots so
  the series never has a gap. In-zone lines 8–16 resume normal values in the restored block.

### View it

Open Grafana at **http://localhost:3000** and select the
**"IEEE 33-Bus — Fault & Reconfiguration"** dashboard. It is auto-provisioned alongside the
96-step-day dashboard — no manual datasource or dashboard import step is required.

Headline panels:

| Panel | What it shows |
|-------|---------------|
| Bus Voltage Profile | All 33 buses (line plot) — the dead-zone collapse to 0 pu and post-restoration recovery |
| Dead-Zone Bus Voltages (8–17) | Zoomed-in view of the 10 de-energised buses during isolation |
| Bus Active Power (MW) | Net per-bus power — the dead-zone buses shed to 0 MW during isolation and restore on reconfiguration |
| OLTC Tap Position | Tap pinned at −2 during isolation; OLTC resumes in restored block |
| Served Load & Slack Feed-in | 3.29 → 2.69 MW drop during isolation, recovery to 3.29 MW |
| Restored Min-Voltage (stat) | ~0.997 pu (green threshold); scoped to the restored block only |
| Phase / Event Marker | `pre_fault` → `faulted_isolated` → `restored` timeline |
| Topology Event Table | Per-step ground truth: `faulted_line_id`, `tie_closed`, `tie_id`, `n_dead_buses` |

The `fault_event` InfluxDB bucket holds the 40-snapshot series
(`bus`, `line`, `sgen`, `system`, `event` measurements). The `profiles` and `state`
buckets from the 96-step-day simulation are untouched.

### Qualitative comparison to the article

Replicates Meteab/Tousi/Omran (2025) Section-8 fault → isolate → tie-restore qualitatively.
No numerical match is expected: our DG placement (buses 18/22/25/33, ±5% OLTC) differs from
the paper's PSO-optimised DGs at buses 6 & 32. Restoration succeeds and losses/voltages move
in the directions the paper reports (the de-energised zone collapses on isolation and is
restored to a near-nominal in-band operating point when the tie closes).

---

## Measurement Layer (System 1 → System 2 inputs)

The **measurement layer** (Phase 9) is a config-driven module that reads System 1's ground-truth
state from InfluxDB, applies a configurable sensor model (placement, class, noise, cadence), and
writes **observed measurements** (`z` + assumed σ) to a new `measurements` InfluxDB bucket.  This
layer **manufactures realistic under-observability** — the noisy, sparse inputs that System 2 (the
Distribution State Estimator) must reconstruct from.

This layer is **strictly additive**: it reads from the `state` and `fault_event` buckets but never
modifies them. The existing System 1 / 8.1 dashboards are untouched.

### Prerequisites

The `measurements` bucket requires the source buckets to be populated first:

```bash
docker compose up -d         # start InfluxDB + Grafana
uv run ingest                # one-time OPSD fetch (profiles bucket)
uv run sim                   # populate state bucket (96-step day)
uv run fault-sim             # populate fault_event bucket (40-step fault)
```

### Running the measurement layer

```bash
uv run measure
```

Uses the **ACTIVE block** in `src/ieee33/measure_config.py` as the primary configuration switch
(scenario / source / sampling / noise / seed). Reads the selected ground-truth source, applies
the sensor model and noise, writes `meas` + topology `event` points to the `measurements` bucket,
and prints a per-run footprint report.

### ACTIVE block — primary config switch

Edit `src/ieee33/measure_config.py` → `ACTIVE` dict to switch experiment knobs without touching
any runner code (D-09):

```python
ACTIVE: dict = {
    "scenario": "realistic_sparse",   # "well_observed" | "realistic_sparse"
    "source":   "day",                # "day" (96-step state) | "fault" (40-step fault_event)
    "sampling": "snapshot",           # "snapshot" | "multirate_async"
    "noise":    "gaussian",           # "gaussian" | "gaussian_outliers" | "instrument"
    "seed":     42,                   # RNG seed for deterministic noise
    "assumed_sigma_scale": 1.0,       # 1.0 = unbiased; >1 over-cautious; <1 over-confident
}
```

### CLI overrides — sweep mode

Use CLI flags to override individual ACTIVE-block values for experiment sweeps **without editing
the file** (CLI overrides ACTIVE; ACTIVE is the fallback):

```bash
# Run realistic_sparse day scenario (ACTIVE defaults)
uv run measure

# Override scenario and source only — other knobs from ACTIVE
uv run measure --scenario well_observed --source day

# Full override for a sweep
uv run measure --scenario realistic_sparse --source fault --sampling snapshot --noise gaussian

# Sweep all three noise models
uv run measure --noise gaussian
uv run measure --noise gaussian_outliers
uv run measure --noise instrument
```

Available CLI flags: `--scenario`, `--source`, `--sampling`, `--noise`, `--seed`.

### Footprint report

Each run prints a **per-class measurement count** and **redundancy** summary after completion:

```
Measurement Footprint Report
============================
Scenario : realistic_sparse
Source   : day
...
Class        | Count  | Buses
scada        |    288 |     1
pmu          |    576 |     3
...
Real-only redundancy       : 0.405   ← < 1.0 means under-observable without pseudo
With-pseudo redundancy     : 1.215   ← ≥ 1.0 with pseudo padding
```

Expected values (snapshot mode, day source):

| Scenario | Real-only redundancy | With-pseudo redundancy |
|----------|---------------------|----------------------|
| `realistic_sparse` | < 1.0 (under-observable) | ≥ 1.0 (observable with pseudo) |
| `well_observed` | > 1.0 (observable without pseudo) | > 1.0 |

### Scenario definitions

| Class | `realistic_sparse` | `well_observed` |
|-------|-------------------|-----------------|
| SCADA (|V|, P, Q) | Bus 0 | Bus 0 |
| μPMU (|V|, angle) | Buses {17, 24, 30} | Buses {0, 4, 8, 13, 17, 21, 24, 28, 32} |
| DER telemetry (P, Q) | Buses {17, 21, 24, 32} | Buses {17, 21, 24, 32} |
| AMI (P_inj) | Buses {3, 6, 9, 12, 15, 18, 21, 24, 28, 31} | ~80% of load buses |
| Zero-injection | None | Buses {2, 19} |
| Pseudo (derived) | All uncovered load buses | Few or none |

**Key fault behaviour:** Bus 17 is inside the dead zone during `faulted_isolated` (buses 8–17,
`energised=0`). The D-03 gate suppresses ALL measurements for bus 17 during isolation — the μPMU
and DER readings go dark, deliberately stressing System 2.

### Opening the Observed Measurements dashboards

Two dashboards are auto-provisioned for the `measurements` bucket (auto-loaded from
`grafana/provisioning/dashboards/`):

| Dashboard | URL | What it shows |
|-----------|-----|---------------|
| **IEEE 33-Bus Observed Measurements — Day** | http://localhost:3000 (select from list) | 96-step observed voltages vs true overlay; power injections; per-class counts; observed-vs-pseudo footprint |
| **IEEE 33-Bus Observed Measurements — Fault** | http://localhost:3000 (select from list) | 40-step fault observed voltages vs true overlay; dead-bus count; phase marker; per-class counts; footprint changes at isolation |

Open Grafana at **http://localhost:3000** after running `uv run measure`. All four dashboards
(original two + the two new ones) are listed in the Grafana home screen. No manual import is required.

### Noise models

| Model | Description | Use case |
|-------|-------------|----------|
| `gaussian` | Additive white Gaussian noise, zero mean | Baseline; determinism test |
| `gaussian_outliers` | Gaussian base + 3% gross errors at ±15σ | Bad-data detection / χ² test (System 2) |
| `instrument` | Per-sensor systematic bias + AR(1) temporal correlation + quantization | Graceful degradation study |

### Sampling modes

| Mode | μPMU/DER/SCADA | AMI (day) | AMI (fault) |
|------|----------------|-----------|-------------|
| `snapshot` | Every step | Every step | Every step |
| `multirate_async` | Every step | Every 4th step (hourly) | Every 10th step (blind) |

### Measurements bucket schema (D-06 forward contract for System 2)

```
measurement: "meas"
tags:   class ∈ {scada, pmu, ami, der, pseudo, zero_inj}
        quantity ∈ {vm_pu, va_degree, p_inj_mw, q_inj_mvar, p_mw, q_mvar}
        location (bus_id string)
        scenario ∈ {well_observed, realistic_sparse}
        experiment ∈ {day, fault}
        phase (fault only: pre_fault | faulted_isolated | restored)
fields: value (float — noisy measurement z)
        assumed_sigma (float — σ the estimator should use)
```

**No `true_value` field** — the oracle stays in `state`/`fault_event` buckets (SPEC R9).

Topology events are also re-published per snapshot into the `measurements` bucket as the `event`
measurement (same schema as the `fault_event` bucket's `event` measurement, with added
`scenario`/`experiment` tags) so System 2 can read both `z` and topology from a single bucket.

### Automated tests

```bash
# Static tests only (no Docker required)
uv run python -m pytest tests/test_measure_determinism.py::test_no_unseeded_randomness \
    tests/test_measure_determinism.py::test_no_true_value_field \
    tests/test_measure_determinism.py::test_meas_schema_vocab -v

# Full suite including integration tests (requires Docker + populated buckets)
uv run python -m pytest tests/test_measure_determinism.py -v
```

Static tests verify:
- **Determinism contract** (`test_no_unseeded_randomness`): no wall-clock or legacy RNG in measure.py
- **Oracle separation** (`test_no_true_value_field`): no `true_value` field in measurement code
- **Schema vocabulary** (`test_meas_schema_vocab`): locked D-04/D-05/D-11 constants correct

Integration tests (Docker-guarded — skip cleanly if InfluxDB is unreachable):
- **Byte-identical runs** (`test_determinism`): same config → same meas values (SPEC R10)
- **Multirate cadence** (`test_multirate_cadence`): AMI at 24 timestamps in multirate_async (D-14)
- **Dead-bus gate** (`test_dead_bus_gate`): zero meas for bus 17 in faulted_isolated (D-03)

---

## System 2 — Streaming State Estimator (Phase 10)

**System 2** is an AC Distribution State Estimator (AC-DSSE) that consumes the `measurements`
bucket over an MQTT replay transport, reconstructs per-bus node-voltage state `(x̂, P)` for all
33 buses via AC-WLS (snapshot baseline) or recursive FASE EKF/UKF (full AC `h(x)` via `Ybus`),
and writes estimates to a dedicated `estimates` InfluxDB bucket.

The **predict step** uses profile-as-noisy-forecast (D-05 — honest forecast, not oracle foresight).
The **`trace(P)` = ORACS Observability index**: lower `trace_P` means the estimator is more
certain about the full 33-bus state; during island-mode fault isolation `trace_P` rises as dead
buses lose sensor coverage — the AGMS "covariance = observability" interview talking point.

**Oracle separation (D-06):** the estimator (`estimate.py`, `estimators.py`, `fase_predict.py`,
`ac_model.py`) **NEVER reads** the `state` or `fault_event` oracle buckets. Only measurements
(via MQTT) + `netmodel/current` (retained MQTT) + `profiles` (InfluxDB side-information, not
oracle) are consumed. `score.py` is the SOLE component permitted to read oracle buckets for the
post-hoc scoring join.

### Prerequisites for System 2

All System 1 / 8.1 / 9 steps must be complete and their buckets populated:

```bash
docker compose up -d         # start InfluxDB + Grafana + Mosquitto broker
uv run ingest                # one-time OPSD fetch (profiles bucket)
uv run sim                   # populate state bucket (96-step day)
uv run fault-sim             # populate fault_event bucket (40-step fault)
uv run measure               # populate measurements bucket (sensor model)
```

### Running System 2

Run the three System 2 runners in order (each in a separate terminal or with `&`):

#### Step A — Stream measurements over MQTT

```bash
uv run publish --scenario realistic_sparse --source day [--acceleration 10]
```

Reads the `measurements` bucket and replays each snapshot as MQTT messages to
`ieee33/meas/<experiment>/<scenario>/<timestamp>`. Publishes the retained network
topology to `ieee33/netmodel/current` before streaming begins.

`--acceleration N` speeds up the replay by factor N (e.g. `--acceleration 10` plays a 96-step
day in ~10 s instead of ~16 min). Default: 1.0 (wall-time spacing between snapshots).

Available options:
- `--scenario {well_observed,realistic_sparse}` — sensor-placement scenario
- `--source {day,fault}` — data source (96-step day or 40-step fault)
- `--acceleration N` — replay speed multiplier (float; default 1.0)

#### Step B — Consume stream and estimate state

```bash
uv run estimate --scenario realistic_sparse --source day --estimator ekf
```

Subscribes to the MQTT broker; waits for the retained `netmodel/current` before
processing measurements. Assembles per-snapshot `z` vectors, drives the selected
estimator, and writes `(x̂, P, trace_P)` to the `estimates` InfluxDB bucket.

Recursive filters (EKF, UKF) also persist per-step innovation statistics:
- `nis_k` (float) — Normalised Innovation Squared = `y_k^T S_k^{-1} y_k`
- `m_k` (int) — innovation dimension (for chi2 band computation in `score.py`)

These are real per-step time series visible in the NIS Calibration panel of the estimator
dashboards. WLS has no innovation sequence — `nis_k`/`m_k` are absent for WLS runs.

Available options:
- `--estimator {wls,ekf,ukf}` — estimator to run (one per invocation, tagged in estimates bucket)
- `--scenario {well_observed,realistic_sparse}` — sensor-placement scenario
- `--source {day,fault}` — data source
- `--seed N` — RNG seed for forecast-error determinism (default: `estimate_config.ACTIVE['seed']`)

**ACTIVE block** — primary config switch (mirrors `measure_config.py`):

```python
# src/ieee33/estimate_config.py
ACTIVE: dict = {
    "scenario":  "realistic_sparse",
    "source":    "day",
    "estimator": "ekf",
    "seed":      42,
}
```

Edit `ACTIVE` to switch experiment knobs without touching runner arguments.

#### Step C — Score estimates against oracle

```bash
uv run score --estimator all
```

Reads the `estimates` bucket and joins with the oracle (`state` or `fault_event` bucket) to
compute a falsifiable PASS/FAIL report:

1. Per-bus voltage |V| and angle RMSE (median over buses) — R10 gate.
2. Dark-node (pseudo-only) bus voltage RMSE — R10 dark-node gate.
3. Dark-node RMSE vs flat/pseudo-only baseline — R10 baseline gate.
4. Time-averaged NEES vs 95% chi2 band — R11 NEES gate.
5. Per-step NIS in-band fraction (from persisted `nis_k`/`m_k`) — R11 NIS gate.
6. Fault covariance inflation (`sigma_V` / `trace_P` higher in `faulted_isolated`
   than `pre_fault`) — R12 fault gate.
7. Restored-block RMSE back within `well_observed` bar — R12 restore gate.

`--estimator all` scores `wls`, `ekf`, and `ukf` and prints a comparison block.

### Opening the Estimator Dashboards

After `uv run estimate` populates the `estimates` bucket, open Grafana at
**http://localhost:3000** and select either dashboard from the list:

| Dashboard | What it shows |
|-----------|---------------|
| **IEEE33 Estimator Day** | True-vs-estimated voltage overlay (per-bus, selectable), per-bus error, `trace_P` ORACS observability index, live NIS calibration (`nis_k` series, EKF/UKF only), dark-node recovery |
| **IEEE33 Estimator Fault** | Fault true-vs-estimated voltage, island-mode P-inflation (`trace_P` + mean `sigma_V` rising in `faulted_isolated`), phase-region markers (`pre_fault`/`faulted_isolated`/`restored`), fault NIS calibration, per-bus fault error |

Both dashboards are auto-provisioned from `grafana/provisioning/dashboards/` — no manual import
required. Template variables (`estimator`, `scenario`, `bus_id`) are available in each dashboard.

All six dashboards (four existing + two new) are listed on the Grafana home screen.

### Estimates Bucket Schema (D-08 forward contract)

```
measurement: "estimate"
  tags:   bus_id (str, 0–32), scenario, experiment, estimator
  fields: vm_pu_est (float), va_degree_est (float), sigma_vm (float), sigma_va (float)

measurement: "estimate_system"
  tags:   scenario, experiment, estimator
  fields: trace_P (float)
          nis_k   (float, EKF/UKF only — absent for WLS)
          m_k     (int,   EKF/UKF only — absent for WLS)
```

`experiment` = source name (`day` or `fault`).

### Determinism Verification (R13)

System 2 is deterministic: two same-config `estimate` runs produce identical estimates
(within floating-point round-trip, i.e., within 1e-9 for IEEE 754 double arithmetic).

**Structural grep verification (feasible without a live Docker run):**

```bash
# 1. Confirm no legacy/unseeded RNG calls in System 2 paths
#    (a match in a prohibition COMMENT is expected and harmless; zero code-level matches)
grep -rnE "np\.random\.seed|random\.seed\(|np\.random\.randn|np\.random\.rand\b" \
  src/ieee33/publish.py src/ieee33/estimate.py src/ieee33/estimators.py \
  src/ieee33/fase_predict.py src/ieee33/ac_model.py src/ieee33/score.py

# 2. Confirm no wall-clock reads in the estimation/scoring paths
#    (publish.py's time.sleep for acceleration pacing is intentionally excluded)
grep -rnE "datetime\.now|time\.time\(\)" \
  src/ieee33/estimate.py src/ieee33/estimators.py \
  src/ieee33/fase_predict.py src/ieee33/ac_model.py src/ieee33/score.py
```

Expected result: both greps return zero code-level matches. Any match in `fase_predict.py`
line 27 is a prohibition comment in the docstring (not executable code) and is expected.

**Live two-run comparison (requires Docker + populated buckets):**

```bash
# Run estimate twice with the same seed, tagging different experiment IDs
uv run estimate --scenario realistic_sparse --source day --estimator ekf --seed 42
# (rename or note the written data, then run again — InfluxDB overwrites same timestamps)
uv run estimate --scenario realistic_sparse --source day --estimator ekf --seed 42
```

Both runs write to the same `estimates` bucket, same tags, same timestamps — InfluxDB
overwrites produce identical point values. The `score.py` RMSE report will be numerically
identical across both runs. The design guarantee: all randomness passes through a single
`np.random.default_rng(seed)` instance created before the estimation loop; no `np.random.seed()`,
`random.seed()`, `hash()`, or wall-clock reads appear in `estimate.py`, `estimators.py`,
`fase_predict.py`, or `ac_model.py`.

**RNG norm:** All randomness uses `np.random.default_rng(seed)` (PCG64, new-style Generator
API). `np.random.randn()` / `np.random.seed()` (legacy) are prohibited project-wide (CLAUDE.md
seeded-determinism norm). Per-entity seed derivation uses `hashlib.sha256` (not Python `hash()`
which is PYTHONHASHSEED-randomized).

### Shortcut — Full System 2 pipeline

```bash
# Terminal 1: start infrastructure (if not already up)
docker compose up -d

# Terminal 2: start publisher (--acceleration 20 for fast replay)
uv run publish --scenario realistic_sparse --source day --acceleration 20

# Terminal 3 (simultaneously): start estimator
uv run estimate --scenario realistic_sparse --source day --estimator ekf

# After both complete:
uv run score --estimator all

# Open http://localhost:3000 → select "IEEE33 Estimator Day"
```
