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
