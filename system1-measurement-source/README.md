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
| Bus Voltage Envelope | All 33 buses — the dead-zone collapse to 0 pu and post-restoration recovery |
| Dead-Zone Bus Voltages (8–17) | Zoomed-in view of the 10 de-energised buses during isolation |
| OLTC Tap Position | Tap pinned at −2 during isolation; OLTC resumes in restored block |
| Served Load & Slack Feed-in | 3.29 → 2.69 MW drop during isolation, recovery to 3.29 MW |
| Dead-Bus Count | 0 → 10 → 0 pulse shape over the three blocks |
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
