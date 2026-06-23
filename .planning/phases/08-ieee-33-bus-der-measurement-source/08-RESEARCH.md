# Phase 8: IEEE 33-Bus DER Measurement Source — Research

**Researched:** 2026-06-23
**Domain:** Power-systems simulation (pandapower), time-series persistence (InfluxDB 2.x), containerised infrastructure (Docker Compose + Grafana), profile data ingestion (open-power-system-data), dependency management (uv)
**Confidence:** HIGH (pandapower, InfluxDB client, uv — Context7 + PyPI verified); MEDIUM (Grafana provisioning, OPSD column structure — official docs + live HTTP 200 verified); LOW (DG scaling decision, exact OPSD day — data inspection deferred to implementation)

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

- **D-01:** High-DER sunny+breezy DE day; midday physics observable (voltage rise, reverse power flow, OLTC tapping, noon loss dip).
- **D-02:** Scale each DG by `DE_solar_profile` / `DE_wind_profile` (0–1) × nameplate; load by peak-normalised `DE_load_actual_entsoe_transparency`. Use `*_generation_actual` / capacity only if profile columns unusable.
- **D-03:** Article's 3.715 MW = daily PEAK load (feeder most stressed at peak, DER relief visible at midday).
- **D-04:** DG sizing faithful to case33.xlsx nameplates as baseline (200 kW each = 800 kW total); scale uniformly to ~60–70% of peak if too small to produce visible midday effects — document deviation explicitly.
- **D-05:** Solar drives buses 18 & 22; wind drives buses 25 & 33.
- **D-06:** Two InfluxDB buckets — `profiles` (one-time ingest) and `state` (per-run snapshots).
- **D-07:** State schema: per-entity-type measurements (`bus`, `line`, `sgen`, `system`) with `bus_id` / `line_id` tags; fields from SPEC req 5.
- **D-08:** Snapshots carry real OPSD datetimes (00:00–23:45 UTC, 15-min); re-runs overwrite identical timestamp+tag points — deterministic.
- **D-09:** Dedicated top-level folder (System 1), separate from `docs/`.
- **D-10:** Python managed by uv — `pyproject.toml` + `uv.lock`; pandapower, numpy, pandas, influxdb-client pinned.
- **D-11:** Docker Compose deploys infrastructure only (InfluxDB + Grafana); sim runs on host via `uv run`.
- **D-12:** README runbook with ordered "rhythm": `uv sync` → `docker compose up` → ingest → sim → open Grafana/InfluxDB.
- **D-13:** Grafana ships the SPEC panel set, auto-provisioned with InfluxDB datasource — no manual setup.
- **D-14:** Quantitative validation: plain `case33bw` reproduces Baran & Wu min voltage ≈ 0.913 pu at bus 18; enhanced net asserts convergence + 0.95–1.05 band every step.
- **D-15:** Concrete DE day hard-coded as config constant after one-time data inspection; ingest always extracts that day.
- **D-16:** No stochastic elements; fixed day + fixed profiles + deterministic Newton-Raphson.

### Claude's Discretion
- Exact pandapower OLTC + phase-shifter mechanism (recommended starting point: DiscreteTapControl on a feeder transformer; phase shifter as scheduled `shift_degree`).
- Orchestration mechanism (recommended: uv entry points + Makefile wrapper).
- Folder name, entry-point names, validation tolerances, snapshot batching.

### Deferred Ideas (OUT OF SCOPE)
- Virtual-sensing / state-estimation module (System 2)
- Measurement-noise / sensor-subset layer
- True-vs-estimated error metrics / ORACS observability index
- Unbalanced 3-phase model, meshed configuration, BESS/EV, real-time streaming loop, PSS/E cross-validation
- Containerising the sim itself
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| REQ-1 | Enhanced IEEE 33-bus model builds and solves from single entry point | pandapower 3.4.0 `pn.case33bw()` + `create_sgen` + `create_shunt` + feeder trafo; `pp.runpp` confirmed |
| REQ-2 | Feeder OLTC + phase-shifter regulation; tap position and angle captured as state | `DiscreteTapControl` + `runpp(run_control=True)`; `net.trafo["tap_pos"]` post-run; `shift_degree` as input field |
| REQ-3 | One-time profile ingestion from OPSD 15-min dataset into InfluxDB; no fallback | OPSD CSV 200 OK at versioned URL; `requests` + pandas streaming; `influxdb-client` write_api SYNCHRONOUS |
| REQ-4 | 96-step driver reads profiles from InfluxDB (batch); no network fetch at runtime | Flux query via `query_api.query_data_frame`; loop over 96 rows; `pp.runpp` per step |
| REQ-5 | Full ground-truth state captured per step (bus, line, sgen, trafo, system scalars) | `net.res_bus`, `net.res_line`, `net.res_sgen`, `net.res_ext_grid`, `net.res_trafo`, `net.trafo["tap_pos"]` |
| REQ-6 | Local InfluxDB 2.x persistence via Docker Compose; 96-point query confirmed | InfluxDB 2.9.1 Docker image + `DOCKER_INFLUXDB_INIT_MODE=setup`; `influxdb-client` Point write |
| REQ-7 | Grafana dashboard + provisioned datasource + README runbook | Grafana 11.6 Docker; provisioning/datasources YAML; provisioning/dashboards YAML + JSON model |
</phase_requirements>

---

## Summary

This is the first code build phase in a previously study-notes-only repo. System 1 is a greenfield Python project that: (1) builds the enhanced IEEE 33-bus network in pandapower 3.4.0 with four renewable DG sources, two RPC shunt capacitors, and a regulating feeder transformer (OLTC + phase shifter); (2) ingests one representative day of DE-zone profiles from the open-power-system-data 15-minute CSV into InfluxDB; (3) runs 96 quasi-static power-flow steps using those profiles; and (4) persists the full state to InfluxDB and renders it through a pre-provisioned Grafana dashboard — all with pinned deps (uv) and a clear README runbook.

The main technical landmines are: (a) the OLTC cannot be on the existing `case33bw` ext_grid bus — it requires inserting a new HV bus and a feeder transformer between that bus and the rest of the network; (b) InfluxDB's first-run bootstrap via `DOCKER_INFLUXDB_INIT_*` environment variables must complete before the Python ingest script can write, so the startup order matters; (c) Grafana's `secureJsonData.token` field in provisioning YAML technically supports `${VAR}` substitution but has reported reliability issues — a safer pattern is to hard-code the same token that InfluxDB is initialised with into the YAML at provision time using an env-file; (d) the OPSD CSV is 107 MB and should be streamed/chunked with `pandas.read_csv(chunksize=...)` or `usecols=` to avoid memory pressure; (e) DG nameplates from case33.xlsx are 200 kW each (800 kW total = 21% of 3.715 MW peak), which is likely too small to produce visible midday voltage rise — a uniform scaling to ~560 kW each (~60% of peak) is the expected D-04 outcome, and must be documented as a deliberate deviation from the article's base figures.

**Primary recommendation:** Model the OLTC as a 2-winding feeder transformer with `DiscreteTapControl` (tap_neutral=0, tap_min=−5, tap_max=+5, tap_step_percent=1.0) driven by `pp.runpp(run_control=True)`; model the phase shifter as a scheduled constant `shift_degree` field on the same transformer (read back as captured state); run ingest and sim as uv entry points wrapped by a Makefile.

---

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Network model build (IEEE 33-bus) | Host Python (pandapower) | — | Power-flow solver runs on host via uv; containers are infra-only (D-11) |
| OLTC / tap regulation | Host Python (pandapower controller loop) | — | `DiscreteTapControl` is part of pandapower's host-side solver loop |
| Profile ingestion (OPSD) | Host Python (one-time script) | InfluxDB `profiles` bucket | Fetch + normalise on host; write to container DB |
| 96-step driver | Host Python (sim loop) | InfluxDB (read profiles, write state) | Driver reads from `profiles`, writes to `state` bucket |
| Ground-truth state persistence | InfluxDB 2.x container | — | All snapshots land in `state` bucket; forward contract for System 2 |
| Visualisation | Grafana container | InfluxDB (datasource) | Grafana queries `state` bucket via Flux; auto-provisioned |

---

## Standard Stack

### Core

| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| pandapower | 3.4.0 | Power-flow solver, network builder, tap controller | Canonical Python power-systems tool; `case33bw` built-in; `DiscreteTapControl` included |
| influxdb-client | 1.50.0 | Write/query InfluxDB 2.x from Python | Official client for InfluxDB 2.x OSS; SYNCHRONOUS write_api; Flux query_api |
| pandas | ≥2.3 (pandapower dep) | CSV streaming, profile normalisation, DataFrame writes | Required by pandapower; efficient chunked CSV parsing |
| numpy | ≥1.26,<2.4 | Numerical operations in power-flow loop | Required by pandapower |
| requests | latest stable | HTTP HEAD check for OPSD reachability | Lightweight; already in most envs |

### Supporting

| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| openpyxl | ≥3.1 | Read case33.xlsx for DG nameplate data (Wave 0 only) | One-time data inspection to confirm DG sizing |
| python-dotenv | latest | Load `.env` for INFLUXDB_URL / token in host sim | Keeps credentials out of source code |

### Infrastructure (Docker images — pinned)

| Image | Tag | Purpose |
|-------|-----|---------|
| influxdb | 2.9.1 | InfluxDB 2.x OSS time-series DB |
| grafana/grafana | 11.6.15 | Grafana dashboard server |

**Version verification (performed 2026-06-23):**
- `pandapower 3.4.0` — PyPI registry, latest stable [VERIFIED: pypi.org]
- `influxdb-client 1.50.0` — PyPI registry [VERIFIED: pypi.org]
- `influxdb:2.9.1` — Docker Hub, pushed 2026-06-11 [VERIFIED: hub.docker.com]
- `grafana/grafana:11.6.15` — Docker Hub, pushed 2026-06-03 [VERIFIED: hub.docker.com]

**Installation (pyproject.toml dependencies):**
```toml
[project]
name = "ieee33-measurement-source"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
  "pandapower==3.4.0",
  "influxdb-client==1.50.0",
  "pandas>=2.3",
  "numpy>=1.26,<2.4",
  "requests>=2.32",
  "python-dotenv>=1.0",
]

[project.scripts]
ingest   = "ieee33.ingest:main"
sim      = "ieee33.sim:main"
validate = "ieee33.validate:main"
```

**Note on pandapower `control` extras:** `DiscreteTapControl` and `ContinuousTapControl` are part of pandapower's base install. The `pandapower[control]` extra only adds `shapely` (for geo-based operations), which is NOT needed for tap control. Do not add the `control` extra — it adds unnecessary dependency weight. [VERIFIED: PyPI extras metadata]

---

## Architecture Patterns

### System Architecture Diagram

```
OPSD 15-min CSV (107 MB, HTTP)
        |
        | [one-time ingest; halt+notify if unreachable]
        v
  [Host: uv run ingest]
    pandas chunked read
    normalise load/solar/wind
        |
        v
InfluxDB 2.9.1 (Docker)
  bucket: profiles
  measurement: profiles
  tags: (none needed — single series per field)
  fields: load_pu, solar_pu, wind_pu
  96 rows, OPSD UTC timestamps
        |
        | [at runtime — batch query all 96 rows]
        v
  [Host: uv run sim]
    step 0..95:
      scale loads = base_load_mw * load_pu[t]
      set solar sgen p_mw = nameplate_solar * solar_pu[t]
      set wind  sgen p_mw = nameplate_wind  * wind_pu[t]
      pp.runpp(net, run_control=True)   <- DiscreteTapControl converges
      capture: res_bus, res_line, res_sgen,
               res_ext_grid, res_trafo,
               net.trafo["tap_pos"], net.trafo["shift_degree"]
        |
        v
InfluxDB 2.9.1 (Docker)
  bucket: state
  measurements: bus, line, sgen, system
  tags: bus_id / line_id / sgen_id
  fields: per SPEC req 5
  96 timestamped points per entity
        |
        | [Flux queries]
        v
Grafana 11.6.15 (Docker)
  datasource: influxdb (provisioned)
  dashboard: ieee33-state.json (provisioned)
  panels: voltage profile, line loadings,
          DG output, losses, OLTC tap, slack feed-in
```

### Recommended Project Structure

```
system1-measurement-source/     # D-09: top-level, separate from docs/
├── pyproject.toml              # uv project metadata + [project.scripts]
├── uv.lock                     # pinned dependency lockfile
├── .env.example                # template: INFLUXDB_URL, INFLUXDB_TOKEN, INFLUXDB_ORG
├── Makefile                    # targets: up, ingest, sim, validate, down, clean
├── docker-compose.yml          # influxdb + grafana services only
├── grafana/
│   ├── provisioning/
│   │   ├── datasources/
│   │   │   └── influxdb.yml    # InfluxDB Flux datasource
│   │   └── dashboards/
│   │       ├── default.yml     # dashboard provider config
│   │       └── ieee33-state.json  # prebuilt dashboard panels
│   └── grafana.ini             # optional: disable auth for local use
├── src/
│   └── ieee33/
│       ├── __init__.py
│       ├── config.py           # constants: OPSD_URL, TARGET_DATE, DG_NAMEPLATE_MW, INFLUXDB_*
│       ├── network.py          # build_enhanced_33bus() function
│       ├── ingest.py           # main() entry point: fetch OPSD, write profiles bucket
│       ├── sim.py              # main() entry point: read profiles, run 96 steps, write state
│       └── validate.py         # main() entry point: base-case Baran & Wu assertion
└── README.md                   # step-by-step runbook (D-12)
```

### Pattern 1: Building the Enhanced IEEE 33-Bus Network

**What:** Start from `pn.case33bw()`, insert a feeder transformer for OLTC, add DG sgens, add RPC shunts, open tie-lines.

**Key landmine — OLTC requires a separate transformer bus:**
`case33bw()` has `ext_grid` at bus index 0 and 32 lines connecting bus 0 through bus 32. There is NO transformer in the built-in case. To model the feeder OLTC, you must insert a two-winding transformer between a new "HV source" bus and the existing bus 0. The ext_grid then attaches to the new HV bus; the OLTC transformer drives bus 0.

```python
# Source: Context7 /e2niee/pandapower + case33.xlsx analysis
import pandapower as pp
import pandapower.networks as pn
import pandapower.control as ctrl

def build_enhanced_33bus() -> pp.pandapowerNet:
    # 1. Load Baran & Wu base (33 buses, 32 lines, ext_grid at idx 0)
    net = pn.case33bw()
    # net.bus: indices 0..32; net.ext_grid at bus 0 (1.0 pu slack)
    # NOTE: article bus N = pandapower index N-1

    # 2. Open tie-lines (branches 33, 34, 35 in article = indices 32, 33, 34 in net.line)
    #    case33bw already includes them as out-of-service (in_service=False) -- verify:
    #    if not, set: net.line.loc[[32, 33, 34], "in_service"] = False

    # 3. Insert feeder transformer for OLTC between a new HV bus and bus 0
    hv_bus = pp.create_bus(net, vn_kv=12.66, name="feeder_hv")
    # Move ext_grid from bus 0 to hv_bus
    net.ext_grid.bus = hv_bus

    trafo_idx = pp.create_transformer_from_parameters(
        net,
        hv_bus=hv_bus,
        lv_bus=0,              # article bus 1 = pandapower index 0
        sn_mva=10.0,           # 10 MVA feeder rating
        vn_hv_kv=12.66,
        vn_lv_kv=12.66,
        vkr_percent=0.5,       # typical distribution feeder
        vk_percent=4.0,
        pfe_kw=0.0,
        i0_percent=0.0,
        shift_degree=0.0,      # phase shifter scheduled value (±5° range, article)
        tap_side="hv",
        tap_neutral=0,
        tap_min=-5,
        tap_max=5,
        tap_step_percent=1.0,  # 1% per step → ±5% = 0.95..1.05 pu range
        tap_pos=0,             # start at neutral
        name="feeder_OLTC",
    )

    # 4. Attach DiscreteTapControl to hold LV side near 1.0 pu
    ctrl.DiscreteTapControl(
        net,
        element_index=trafo_idx,
        vm_lower_pu=0.95,
        vm_upper_pu=1.05,
        side="lv",
    )

    # 5. Add DG sgen (solar buses 18→idx17, 22→idx21; wind buses 25→idx24, 33→idx32)
    DG_MW = 0.56  # scaled nameplate; document deviation from article's 0.2 MW
    solar_buses = [17, 21]
    wind_buses  = [24, 32]
    for b in solar_buses:
        pp.create_sgen(net, bus=b, p_mw=DG_MW, q_mvar=0.0, type="PV", name=f"solar_b{b+1}")
    for b in wind_buses:
        pp.create_sgen(net, bus=b, p_mw=DG_MW, q_mvar=0.0, type="WP", name=f"wind_b{b+1}")

    # 6. RPC shunt capacitors (capacitive = negative q_mvar in pandapower)
    # Article bus 18 = idx 17: 0.4 MVAr cap; bus 33 = idx 32: 0.6 MVAr cap
    pp.create_shunt(net, bus=17, q_mvar=-0.4, p_mw=0.0, name="cap_b18")
    pp.create_shunt(net, bus=32, q_mvar=-0.6, p_mw=0.0, name="cap_b33")

    return net, trafo_idx
```

**Sign conventions verified:**
- Capacitive shunt: `q_mvar < 0` (generates reactive power) [VERIFIED: Context7 tutorial `create_shunt(net, bus3, q_mvar=-0.96, ...)`]
- sgen `p_mw > 0` = injecting active power into the bus

### Pattern 2: Running the 96-Step Loop with OLTC Control

```python
# Source: Context7 /e2niee/pandapower (runpp, run_control, DiscreteTapControl)
import pandapower as pp

def run_step(net, trafo_idx, load_pu, solar_pu, wind_pu, base_loads_mw, base_loads_mvar):
    """Scale loads and DGs, run power flow with tap control, return state dict."""
    # Scale all loads by load profile
    net.load["p_mw"]   = base_loads_mw   * load_pu
    net.load["q_mvar"] = base_loads_mvar * load_pu

    # Set solar DGs (sgen type="PV") by solar profile
    solar_mask = net.sgen["type"] == "PV"
    net.sgen.loc[solar_mask, "p_mw"] = net.sgen.loc[solar_mask, "p_mw_nameplate"] * solar_pu

    # Set wind DGs (sgen type="WP") by wind profile
    wind_mask = net.sgen["type"] == "WP"
    net.sgen.loc[wind_mask, "p_mw"] = net.sgen.loc[wind_mask, "p_mw_nameplate"] * wind_pu

    # Run power flow with OLTC controller active
    pp.runpp(net, algorithm="nr", calculate_voltage_angles=True, run_control=True)

    # Read state
    tap_pos     = net.trafo.at[trafo_idx, "tap_pos"]
    shift_deg   = net.trafo.at[trafo_idx, "shift_degree"]
    return {
        "res_bus":      net.res_bus,
        "res_line":     net.res_line,
        "res_sgen":     net.res_sgen,
        "res_ext_grid": net.res_ext_grid,
        "res_trafo":    net.res_trafo,
        "tap_pos":      tap_pos,
        "shift_degree": shift_deg,
    }
```

**Reading tap position:** `net.trafo["tap_pos"]` (not `net.res_trafo`) — tap position is an input field updated by the controller. `net.res_trafo` contains derived results (power flows, voltages, loading). [VERIFIED: Context7 `net.trafo["tap_pos"]` after DiscreteTapControl]

**Reading shift_degree:** `net.trafo["shift_degree"]` — this is the scheduled (fixed) phase angle set at build time. It is NOT changed by any controller in this phase; it is simply read back as part of the captured state each step.

### Pattern 3: OPSD Profile Ingestion

**Data source:** `https://data.open-power-system-data.org/time_series/2020-10-06/time_series_15min_singleindex.csv` [VERIFIED: HTTP 200, 2026-06-23]

**Confirmed DE columns available:** `DE_load_actual_entsoe_transparency`, `DE_solar_profile` (0–1 pre-normalised), `DE_wind_profile` (0–1 pre-normalised), `DE_solar_generation_actual`, `DE_wind_generation_actual` [VERIFIED: datapackage.json schema]

**Datetime format:** `utc_timestamp` column, ISO 8601 UTC (`2015-01-01T00:00:00Z`, 15-min steps) [VERIFIED: CSV header + first rows]

**Day selection strategy:** The CSV covers 2015-01-01 through ~2020-10-06. A German summer day with high solar capacity factor + decent onshore wind should be selected (e.g., June or July 2019). The concrete date is selected once by the researcher/planner via a data-inspection script and then hard-coded as `TARGET_DATE` in `config.py` (D-15). [ASSUMED — actual high-DER day must be identified by inspecting DE_solar_profile and DE_wind_profile values]

```python
# Source: Context7 + OPSD datapackage.json verified column names
import pandas as pd, requests, sys

OPSD_URL = "https://data.open-power-system-data.org/time_series/2020-10-06/time_series_15min_singleindex.csv"
TARGET_DATE = "2019-07-15"   # PLACEHOLDER: replace with actual inspection result
COLS = ["utc_timestamp", "DE_load_actual_entsoe_transparency",
        "DE_solar_profile", "DE_wind_profile"]

def fetch_opsd_day(target_date: str) -> pd.DataFrame:
    """Stream OPSD CSV, extract one 96-row day. Halts on unreachable endpoint."""
    try:
        resp = requests.head(OPSD_URL, timeout=15)
        resp.raise_for_status()
    except Exception as e:
        print(f"ERROR: OPSD dataset unreachable ({e}).\n"
              "Download time_series_15min_singleindex.csv manually and provide path.")
        sys.exit(1)

    chunks = []
    for chunk in pd.read_csv(OPSD_URL, usecols=COLS,
                             parse_dates=["utc_timestamp"],
                             chunksize=10_000):
        day_mask = chunk["utc_timestamp"].dt.date.astype(str) == target_date
        day_rows = chunk[day_mask]
        if len(day_rows) > 0:
            chunks.append(day_rows)
        # Stop after we have 96 rows
        if sum(len(c) for c in chunks) >= 96:
            break

    df = pd.concat(chunks).head(96).reset_index(drop=True)
    assert len(df) == 96, f"Expected 96 rows, got {len(df)}"

    # Peak-normalise load (D-03): 3.715 MW is daily peak
    load_peak = df["DE_load_actual_entsoe_transparency"].max()
    df["load_pu"] = df["DE_load_actual_entsoe_transparency"] / load_peak

    # solar_pu and wind_pu are already 0–1 pre-normalised in DE_solar_profile / DE_wind_profile
    df["solar_pu"] = df["DE_solar_profile"].fillna(0.0)
    df["wind_pu"]  = df["DE_wind_profile"].fillna(0.0)

    return df[["utc_timestamp", "load_pu", "solar_pu", "wind_pu"]]
```

**Memory:** chunked read avoids loading 107 MB into RAM in one shot. [CITED: pandas docs]

### Pattern 4: InfluxDB Write (SYNCHRONOUS)

```python
# Source: Context7 /influxdata/influxdb-client-python
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import timezone

def write_profiles(client, org, profiles_df):
    """Write 96-row profile DataFrame to 'profiles' bucket."""
    write_api = client.write_api(write_options=SYNCHRONOUS)
    points = []
    for _, row in profiles_df.iterrows():
        p = (Point("profiles")
             .field("load_pu",  float(row["load_pu"]))
             .field("solar_pu", float(row["solar_pu"]))
             .field("wind_pu",  float(row["wind_pu"]))
             .time(row["utc_timestamp"].to_pydatetime().replace(tzinfo=timezone.utc)))
        points.append(p)
    write_api.write(bucket="profiles", org=org, record=points)
```

**Idempotency (D-08):** Writing the same measurement + field + timestamp point overwrites the existing value in InfluxDB 2.x — no duplicate rows. Re-running ingest replaces the 96 profile points in place. [CITED: InfluxDB line protocol semantics]

**State bucket write pattern (per step):**

```python
def write_state_step(write_api, org, timestamp, bus_df, line_df, sgen_df, ext_grid_df, system_dict):
    """Write one 15-min snapshot to 'state' bucket."""
    points = []
    # bus measurement: tag bus_id; fields vm_pu, va_degree
    for idx, row in bus_df.iterrows():
        points.append(
            Point("bus")
            .tag("bus_id", str(idx))
            .field("vm_pu", float(row["vm_pu"]))
            .field("va_degree", float(row["va_degree"]))
            .time(timestamp)
        )
    # line measurement: tag line_id; fields p_from_mw, q_from_mvar, p_to_mw, q_to_mvar, loading_percent, pl_mw
    for idx, row in line_df.iterrows():
        points.append(
            Point("line")
            .tag("line_id", str(idx))
            .field("p_from_mw", float(row["p_from_mw"]))
            .field("q_from_mvar", float(row["q_from_mvar"]))
            .field("p_to_mw", float(row["p_to_mw"]))
            .field("q_to_mvar", float(row["q_to_mvar"]))
            .field("loading_percent", float(row["loading_percent"]))
            .field("pl_mw", float(row["pl_mw"]))
            .time(timestamp)
        )
    # sgen measurement: tag sgen_id
    # system measurement: system scalars
    write_api.write(bucket="state", org=org, record=points)
```

### Pattern 5: InfluxDB Docker Compose (first-run bootstrap)

```yaml
# Source: docs.influxdata.com/influxdb/v2/install/use-docker-compose/ [CITED]
services:
  influxdb:
    image: influxdb:2.9.1
    ports:
      - "8086:8086"
    environment:
      DOCKER_INFLUXDB_INIT_MODE: setup
      DOCKER_INFLUXDB_INIT_USERNAME: admin
      DOCKER_INFLUXDB_INIT_PASSWORD: adminpassword
      DOCKER_INFLUXDB_INIT_ORG: ieee33
      DOCKER_INFLUXDB_INIT_BUCKET: profiles      # creates ONLY this bucket initially
      DOCKER_INFLUXDB_INIT_ADMIN_TOKEN: ieee33-dev-token   # fixed token for provisioning
    volumes:
      - influxdb-data:/var/lib/influxdb2
      - influxdb-config:/etc/influxdb2

  grafana:
    image: grafana/grafana:11.6.15
    ports:
      - "3000:3000"
    environment:
      GF_SECURITY_ADMIN_PASSWORD: admin
      GF_AUTH_ANONYMOUS_ENABLED: "true"   # optional: no login for local use
    volumes:
      - ./grafana/provisioning:/etc/grafana/provisioning
      - grafana-data:/var/lib/grafana
    depends_on:
      - influxdb

volumes:
  influxdb-data:
  influxdb-config:
  grafana-data:
```

**Landmine — second bucket:** `DOCKER_INFLUXDB_INIT_BUCKET` creates only one bucket. The `state` bucket must be created programmatically by the ingest/sim script at startup using `buckets_api.create_bucket(bucket_name="state", org=...)` (idempotent: check existence first). [VERIFIED: influxdb-client BucketsApi pattern]

**Landmine — bootstrap order:** `DOCKER_INFLUXDB_INIT_MODE=setup` runs on the FIRST container start only. On subsequent `docker compose up`, InfluxDB starts with existing data. The `ieee33-dev-token` is persistent because it was set during init. Python scripts should wait for InfluxDB health (`/ping` endpoint) before writing. [CITED: InfluxDB Docker docs]

### Pattern 6: Grafana Provisioning (InfluxDB 2.x Flux datasource)

```yaml
# grafana/provisioning/datasources/influxdb.yml
# Source: grafana.com/docs/grafana/latest/datasources/influxdb/configure/ [CITED]
apiVersion: 1
datasources:
  - name: InfluxDB-IEEE33
    type: influxdb
    uid: ieee33-influxdb
    access: proxy
    url: http://influxdb:8086   # container-to-container (service name)
    jsonData:
      version: Flux
      organization: ieee33
      defaultBucket: state
      tlsSkipVerify: true
    secureJsonData:
      token: ieee33-dev-token   # matches DOCKER_INFLUXDB_INIT_ADMIN_TOKEN
    isDefault: true
```

**Landmine — `${VAR}` substitution reliability:** Grafana's env-var substitution in `secureJsonData` has reported issues (GitHub issue #89519). The reliable approach for a local dev stack is to hard-code the same known token string that InfluxDB is initialised with. Both Compose environment and the YAML use the same literal string `ieee33-dev-token`. This is acceptable for a local dev/demo stack. [CITED: github.com/grafana/grafana/issues/89519, community.grafana.com/t/provisioning-a-datasource-with-token]

**Dashboard provisioning config:**

```yaml
# grafana/provisioning/dashboards/default.yml
apiVersion: 1
providers:
  - name: IEEE33
    type: file
    updateIntervalSeconds: 30
    options:
      path: /etc/grafana/provisioning/dashboards
```

**Grafana `GF_PATHS_PROVISIONING`:** Default path inside the container is `/etc/grafana/provisioning`. Map the host's `./grafana/provisioning/` to that path. [CITED: Grafana docs]

### Pattern 7: uv Entry Points + Makefile

```toml
# pyproject.toml
[project.scripts]
ingest   = "ieee33.ingest:main"
sim      = "ieee33.sim:main"
validate = "ieee33.validate:main"
```

```makefile
# Makefile
.PHONY: up down ingest sim validate all clean

up:
	docker compose up -d

ingest: up
	uv run ingest

sim: up
	uv run sim

validate:
	uv run validate

all: up ingest sim

down:
	docker compose down

clean: down
	docker volume rm system1-measurement-source_influxdb-data ... 2>/dev/null || true
```

**Sim reads profiles from InfluxDB, not from network:** Runner calls `query_api.query_data_frame(flux)` to retrieve all 96 profile points at the start of execution, then loops over the in-memory DataFrame. This satisfies REQ-4 (no network fetch at runtime). [CITED: Context7 influxdb-client query_data_frame]

**96-step profile Flux query:**
```flux
from(bucket: "profiles")
  |> range(start: 2019-07-15T00:00:00Z, stop: 2019-07-16T00:00:00Z)
  |> filter(fn: (r) => r._measurement == "profiles")
  |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")
  |> sort(columns: ["_time"])
```

### Anti-Patterns to Avoid

- **Keeping ext_grid at bus 0 and adding OLTC as just a trafo in parallel:** The transformer must be in series between the source and the network. Ext_grid drives the HV bus; the OLTC transformer feeds bus 0.
- **Importing tie-lines as in-service:** case33bw may set tie-lines out-of-service already; verify and enforce `in_service=False` for line indices 32, 33, 34 (article branches 33, 34, 35).
- **Using `ContinuousTapControl` instead of `DiscreteTapControl`:** ContinuousTapControl models a floating-point tap position (useful for large-scale studies). DiscreteTapControl matches the physical OLTC behaviour (integer tap steps). Use DiscreteTapControl.
- **Writing all 96 state snapshots in a single InfluxDB batch at the end:** Memory pressure grows with 33 buses × 32 lines × 4 DGs × 96 steps. Write per-step or in small batches (e.g., 10 steps at a time).
- **Downloading the full 107 MB CSV repeatedly:** Fetch once, check profiles-bucket presence before re-fetching; if 96 rows already in bucket, skip download.
- **Setting `q_mvar=+0.4` for the capacitor shunts:** Positive q_mvar = inductive (absorbs reactive power). Capacitors need `q_mvar=-0.4` (generates reactive power). [VERIFIED: Context7 shunt tutorial]
- **Using `net.res_trafo["tap_pos"]`:** This column does not exist in res_trafo. Read tap position from `net.trafo.at[trafo_idx, "tap_pos"]` after each runpp call. [VERIFIED: Context7]

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| OLTC voltage regulation | Custom tap-stepping logic | `pandapower.control.DiscreteTapControl` | Handles deadband, hunting limit, multi-iteration convergence |
| Power flow | Custom Newton-Raphson | `pp.runpp(algorithm="nr")` | Validated against IEEE benchmark cases; handles ill-conditioned radial networks |
| InfluxDB write retries | Custom HTTP retry loop | `influxdb-client` WriteOptions (batching mode) or SYNCHRONOUS | Client handles retries and connection errors |
| Flux query construction | String concatenation | `query_api.query_data_frame(query)` with bind params | Type safety, escaping, result deserialization |
| Grafana datasource setup | Manual UI clicks | Provisioning YAML | Reproducible; works from clean state |
| CSV streaming | Manual HTTP byte-range | `pd.read_csv(url, usecols=..., chunksize=...)` | Pandas handles chunked HTTP streaming natively |

**Key insight:** Every "custom" solution here would reimplement edge cases that the libraries have already handled (radial-network convergence, controller hunting, time-series point deduplication). Use the libraries.

---

## Common Pitfalls

### Pitfall 1: Bus Index Off-By-One (Article vs. Pandapower)

**What goes wrong:** Using article bus number N directly as a pandapower bus index — connecting DG or shunt to the wrong bus.
**Why it happens:** The article uses 1-indexed bus numbers (bus 1 = slack); pandapower uses 0-indexed (bus 0 = slack).
**How to avoid:** Always subtract 1. Article bus 18 → `bus=17`, bus 22 → `bus=21`, bus 25 → `bus=24`, bus 33 → `bus=32`.
**Warning signs:** `pp.runpp` diverges; DGs appear at buses with wrong load magnitude; Baran & Wu base validation fails at wrong bus.

### Pitfall 2: OLTC Transformer Not in Series

**What goes wrong:** Ext_grid remains at bus 0 and a transformer is added in parallel (or to the wrong side); DiscreteTapControl runs but does nothing useful.
**Why it happens:** `case33bw()` puts the ext_grid at bus 0 with no transformer. It's not obvious that a new HV bus must be created to put the trafo in series.
**How to avoid:** After `pn.case33bw()`, (1) create a new HV bus, (2) move `net.ext_grid.bus = hv_bus`, (3) `create_transformer_from_parameters(hv_bus=hv_bus, lv_bus=0, ...)`.
**Warning signs:** The tap controller runs (no error) but bus voltages at bus 0 are not regulated; `net.res_bus.vm_pu[0]` stays at 1.0 regardless of loading.

### Pitfall 3: InfluxDB Init Token Bootstrapping Order

**What goes wrong:** Python script tries to write to InfluxDB before `DOCKER_INFLUXDB_INIT_MODE=setup` completes on first container start; gets connection refused or 401.
**Why it happens:** InfluxDB `setup` mode takes 5–20 seconds to initialise the internal database; the container's health check may not reflect this.
**How to avoid:** Add a readiness poll in the ingest/sim script: `GET /ping` returns HTTP 204 when InfluxDB is ready. Loop with 1-second sleep until 204.
**Warning signs:** `ConnectionRefusedError` or `InfluxDBError: 401` on first `docker compose up` + immediate `uv run ingest`.

### Pitfall 4: `state` Bucket Not Created Automatically

**What goes wrong:** `DOCKER_INFLUXDB_INIT_BUCKET=profiles` creates only the `profiles` bucket. Attempting to write to `state` bucket fails with "bucket not found".
**Why it happens:** The InfluxDB Docker init creates exactly one bucket by name.
**How to avoid:** The ingest or sim entry point creates the `state` bucket programmatically using `client.buckets_api().create_bucket(...)` with existence check before writing. [VERIFIED: Context7 BucketsApi]
**Warning signs:** `InfluxDBError: bucket 'state' not found` on first sim run.

### Pitfall 5: DG Nameplate Too Small for Visible Midday Effects

**What goes wrong:** Using raw article nameplates (200 kW each = 800 kW total = 21% of 3.715 MW peak) — midday DER injection barely moves bus voltages; no visible reverse power flow; OLTC never taps.
**Why it happens:** The article's baseline scenario uses conservative DG sizing; the "Very High" scenario uses 800 kW each = 3.2 MW total.
**How to avoid:** Per D-04, scale uniformly to ~60% of peak (≈560 kW each). Document in config.py as `DG_SCALE_FACTOR = 2.8  # scaled from article's 200 kW to 560 kW`. The validation step should confirm midday voltage rise and at least one OLTC tap event.
**Warning signs:** All 96 steps show OLTC tap_pos=0 (never moved); bus 18 vm_pu stays below 1.01 across entire day.

### Pitfall 6: Phase Shift Not Captured Correctly

**What goes wrong:** `shift_degree` read from `net.res_trafo` (doesn't exist) rather than `net.trafo`.
**Why it happens:** `res_trafo` contains only derived power-flow results (p_hv_mw, q_hv_mvar, loading_percent, vm_hv_pu, etc.) — NOT the tap position or shift angle.
**How to avoid:** Always read: `net.trafo.at[trafo_idx, "tap_pos"]` and `net.trafo.at[trafo_idx, "shift_degree"]`.
**Warning signs:** `KeyError: 'tap_pos'` when accessing `net.res_trafo`; shift_degree always appears as NaN in state snapshots.

### Pitfall 7: OPSD Day Has NaN Profile Values

**What goes wrong:** Selected day has `NaN` in `DE_solar_profile` or `DE_wind_profile` columns (missing data in the source).
**Why it happens:** OPSD data has gaps, particularly around DST transitions and early years (2015 data is sparse).
**How to avoid:** During day selection (Wave 0 data inspection), assert that the chosen day has exactly 96 non-null rows in all three profile columns (`DE_load_actual_entsoe_transparency`, `DE_solar_profile`, `DE_wind_profile`). Summer 2017–2019 generally has good DE coverage.
**Warning signs:** Ingest writes fewer than 96 points; some steps have solar_pu=0 even at noon.

### Pitfall 8: Grafana Token Provisioning Blank

**What goes wrong:** `secureJsonData.token: ${INFLUXDB_TOKEN}` resolves to blank; Grafana datasource test fails; dashboard panels show "No data".
**Why it happens:** Grafana's env-var substitution in `secureJsonData` is unreliable (known issue #89519).
**How to avoid:** Hard-code the token literal string `ieee33-dev-token` directly in the provisioning YAML. Use the same known fixed string in `DOCKER_INFLUXDB_INIT_ADMIN_TOKEN`. For production, use a secrets management approach; for this local demo, a literal string is acceptable.
**Warning signs:** Grafana Data Explorer shows "Unauthorized" when testing the datasource.

---

## Code Examples

### Flux Query: Bus 18 Voltage across 96 Steps

```flux
// Source: Context7 /influxdata/influxdb-client-python (query_data_frame pattern)
from(bucket: "state")
  |> range(start: 2019-07-15T00:00:00Z, stop: 2019-07-16T00:00:00Z)
  |> filter(fn: (r) => r._measurement == "bus")
  |> filter(fn: (r) => r.bus_id == "17")   // pandapower index 17 = article bus 18
  |> filter(fn: (r) => r._field == "vm_pu")
  |> sort(columns: ["_time"])
```

### Base-Case Validation (Baran & Wu anchor)

```python
# Source: Context7 /e2niee/pandapower + article/CONTEXT.md reference
import pandapower as pp, pandapower.networks as pn, numpy as np

def validate_base_case(tolerance_pu=0.005):
    """Assert case33bw (no DER/caps/OLTC) reproduces Baran & Wu min voltage."""
    net = pn.case33bw()
    pp.runpp(net, algorithm="nr", calculate_voltage_angles=True)
    vm_min = net.res_bus["vm_pu"].min()
    vm_min_bus = net.res_bus["vm_pu"].idxmin()  # should be 17 (article bus 18)
    assert abs(vm_min - 0.913) < tolerance_pu, (
        f"Baran & Wu validation FAILED: vm_min={vm_min:.4f} at bus {vm_min_bus}, "
        f"expected ~0.913 pu (tol {tolerance_pu})"
    )
    print(f"Base case OK: vm_min={vm_min:.4f} pu at pp_bus={vm_min_bus} (article bus {vm_min_bus+1})")
```

**Reference value:** Baran & Wu (1989) report minimum voltage ≈ 0.913 pu at bus 18 for the base 32-line radial configuration. [CITED: CONTEXT.md D-14 + SPEC.md Acceptance Criteria]

---

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| pandapower 2.x (kW units) | pandapower 3.x (MW units throughout) | v2.0 release | All power values in MW/MVAr; old kW snippets online are wrong |
| InfluxDB 1.x (database/measurement/series) | InfluxDB 2.x (org/bucket/measurement) | v2.0 release | Completely different auth (token vs username/password); different client library |
| `influxdb` PyPI package | `influxdb-client` PyPI package | InfluxDB 2.0 | Different import paths; `influxdb` does NOT work with InfluxDB 2.x |
| `tap_phase_shifter` bool in pandapower | `shift_degree` + `tap_step_degree` fields | Recent pandapower | `tap_phase_shifter` column was removed; use `shift_degree` |

**Deprecated / outdated:**
- `influxdb` Python package: for InfluxDB 1.x only — use `influxdb-client` for 2.x
- pandapower `tap_phase_shifter` boolean: removed — use `shift_degree` directly
- pandapower power units in kW (pre-2.0 tutorials): all API values are now in MW [CITED: Context7 update20.md]

---

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | Article's 200 kW DG nameplates are too small for visible midday effects; scaling to ~560 kW (D-04) will produce the intended physics | DG Split & Sizing | If 200 kW is actually sufficient, the documented deviation is unnecessary; mitigated by running validate step |
| A2 | A specific DE summer day (e.g., 2019-07-15) will have complete, non-null DE_solar_profile and DE_wind_profile coverage for all 96 steps | OPSD Profile Ingestion | Wrong day → NaN rows → ingest fails assertion; mitigated by data inspection in Wave 0 |
| A3 | `case33bw()` already sets tie-line switches 32, 33, 34 as `in_service=False`; no manual open needed | Network Build | If wrong, power flow will converge on meshed (not radial) topology, giving different voltages |
| A4 | The feeder transformer parameters (sn_mva=10, vk_percent=4.0) are reasonable approximations for a 12.66 kV distribution feeder at this scale | OLTC Pattern | Wrong impedance → power flow affects losses and voltage profiles; low risk since article doesn't specify trafo impedance |
| A5 | `shift_degree` = 0.0 (no phase angle shift) is the appropriate baseline for the phase shifter in normal operation | Phase Shifter | If the article expects a non-zero scheduled shift, the ground-truth state will differ; article doesn't specify a nominal shift value |

---

## Open Questions (RESOLVED at plan time)

> All three were resolved during `/gsd-plan-phase 8` and are reflected in the plans:
> 1. **TARGET_DATE** — RESOLVED: Plan 08-01 Task 3 runs `scripts/inspect_opsd_day.py` and pins the chosen high-DER day in `config.TARGET_DATE` (Wave 1) before any dependent plan runs.
> 2. **Feeder transformer impedance** — RESOLVED: adopted `sn_mva=10.0`, `vk_percent=4.0`, `vkr_percent=0.5` in `config.py`; the Baran & Wu base-case validation gate (Plan 08-02 Task 2) catches any impedance pathology (bus 0 must hold ≈1.0 pu).
> 3. **case33bw tie-lines** — RESOLVED: Plan 08-02 Task 1 explicitly forces the tie-lines (pandapower line idx 32/33/34) `in_service=False` regardless of the `pn.case33bw()` default, with a runtime assertion.

1. **Exact high-DER DE day for TARGET_DATE**
   - What we know: Dataset covers 2015–2020; DE summer months have highest solar CF
   - What's unclear: Which specific day has high DE_solar_profile + decent DE_wind_profile + no NaN gaps
   - Recommendation: Wave 0 task — run a quick Python inspection script to find max(DE_solar_profile.max_by_day) in summer 2017–2019, filter for wind_profile > 0.3 average, assert no NaN in both columns

2. **Feeder transformer impedance values**
   - What we know: Article specifies OLTC range (0.95–1.05) and phase shifter range (±5°) but NOT the trafo's R/X or sn_mva
   - What's unclear: Whether sn_mva=10 MVA and vk_percent=4% produce realistic feeder behaviour
   - Recommendation: Use typical 12.66 kV distribution values (sn_mva=5..10 MVA, vk_percent=4..6); validate that the base case33bw result is unaffected by the added trafo (base case runs with ext_grid at hv_bus and lv_bus 0 at 1.0 pu)

3. **Whether case33bw tie-lines are already open**
   - What we know: The article states tie-lines 33/34/35 are open in the radial configuration; the reference GitHub repo opens them manually
   - What's unclear: pandapower's `pn.case33bw()` source has not been directly verified in this session
   - Recommendation: Wave 0 task — after `net = pn.case33bw()`, assert `net.line.loc[[32,33,34], "in_service"].all() == False`; if False, force open

---

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Python 3.12 | uv project runtime | Yes | 3.12.3 | — |
| uv | Dependency management | Yes | 0.7.13 | — |
| Docker | InfluxDB + Grafana containers | Yes | 28.1.1 | — |
| Docker Compose v2 | `docker compose up` | Yes | v2.35.1 | — |
| GNU Make | Makefile targets | Yes | 4.3 | Run `uv run <cmd>` manually |
| pandapower | Power-flow solver | Not yet installed | 3.4.0 (to install) | — |
| influxdb-client | InfluxDB write/query | Not yet installed | 1.50.0 (to install) | — |
| OPSD 15-min CSV | Profile ingestion | HTTP 200 (verified) | 2020-10-06 snapshot | Halt + notify (no fallback per SPEC) |
| just (justfile) | Optional Makefile alternative | Not found | — | Use Makefile (make is available) |

**Missing dependencies with no fallback:**
- pandapower and influxdb-client: not yet installed — Wave 0 task: `uv sync` after pyproject.toml is created.

**Missing dependencies with fallback:**
- `just`: not installed; Makefile covers the same targets.

---

## Validation Architecture

> `workflow.nyquist_validation` is `false` in config.json — formal automated test framework is disabled. Validation is implemented as assertions within the `validate` entry point (D-14).

### Validation Strategy (D-14)

| Check | Command | Pass Condition |
|-------|---------|----------------|
| Baran & Wu base case | `uv run validate` | `min(net.res_bus.vm_pu)` ≈ 0.913 pu (within ±0.005) at pp_bus 17 |
| Enhanced net convergence | Sim loop per step | `pp.runpp` returns without `LoadflowNotConverged` exception for all 96 steps |
| Voltage band | Sim loop per step | All 33 buses: 0.95 ≤ vm_pu ≤ 1.05 on every converged step |
| Profile completeness | Ingest script | Exactly 96 rows written to `profiles` bucket; query returns 96 points |
| State completeness | Post-sim assertion | InfluxDB `state` bucket query for any bus_id returns exactly 96 points |
| OLTC activity | Post-sim assertion | At least one step has `tap_pos ≠ 0` (regulation is active; otherwise OLTC is passive/broken) |
| Midday DER effect | Post-sim check (visual) | bus 18 vm_pu peaks midday above off-peak value (expected voltage rise from solar injection) |

### Wave 0 Gaps (pre-implementation setup)

- [ ] `pyproject.toml` with correct dependencies + `[project.scripts]`
- [ ] `uv sync` run to generate `uv.lock`
- [ ] Data inspection script to identify TARGET_DATE (assert no NaN, assert high solar CF)
- [ ] Assertion in `network.py` build function: tie-lines 32/33/34 are open; total base load ≈ 3.715 MW
- [ ] Assertion: `case33bw()` base-case min voltage ≈ 0.913 pu passes before DER added

---

## Security Domain

> This phase has no authentication, network-facing services, or user inputs beyond a local Docker Compose stack for interview demo purposes. The InfluxDB token (`ieee33-dev-token`) is a fixed development credential, not a production secret. No ASVS controls apply. Security domain intentionally omitted for this local demo phase.

---

## Sources

### Primary (HIGH confidence)

- Context7 `/e2niee/pandapower` — DiscreteTapControl, ContinuousTapControl, create_transformer_from_parameters, create_shunt (q_mvar sign), runpp(run_control=True), res_bus/res_line/res_trafo columns, case33bw, run_control module
- Context7 `/influxdata/influxdb-client-python` — WriteApi SYNCHRONOUS, Point API, query_data_frame, BucketsApi, bucket creation
- Context7 `/astral-sh/uv` — pyproject.toml layout, [project.scripts], uv run
- PyPI registry — pandapower 3.4.0 (latest), influxdb-client 1.50.0 (latest), pandapower base deps vs extras [VERIFIED 2026-06-23]
- Docker Hub — influxdb:2.9.1 (2026-06-11), grafana/grafana:11.6.15 (2026-06-03) [VERIFIED 2026-06-23]
- OPSD datapackage.json HTTP 200 — exact DE column names in 15-min singleindex CSV [VERIFIED 2026-06-23]
- OPSD CSV HTTP 200 — datetime format, first rows confirming utc_timestamp ISO8601 [VERIFIED 2026-06-23]

### Secondary (MEDIUM confidence)

- grafana.com/docs/grafana/latest/datasources/influxdb/configure/ — InfluxDB 2.x Flux provisioning YAML structure (`version: Flux`, `organization`, `defaultBucket`, `secureJsonData.token`) [CITED 2026-06-23]
- docs.influxdata.com/influxdb/v2/install/use-docker-compose/ — `DOCKER_INFLUXDB_INIT_*` environment variable list and bootstrap behaviour [CITED 2026-06-23]
- case33.xlsx (direct inspection) — DG nameplates: 200 kW each, "Very High: Pmax 0.8 MW"; OLTC ±5%, phase shifter ±5°; tie-lines 33/34/35 linestatus=0 [VERIFIED 2026-06-23]

### Tertiary (LOW confidence)

- github.com/grafana/grafana issues #89519, community.grafana.com forums — Grafana secureJsonData env-var substitution reliability; recommend literal token [WebSearch]
- Baran & Wu (1989) min voltage ≈ 0.913 pu at bus 18 — cited in CONTEXT.md D-14 and SPEC.md; not re-verified in this session against primary source [ASSUMED from SPEC/CONTEXT]

---

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — all versions verified via PyPI registry and Docker Hub
- Architecture: HIGH — pandapower patterns verified via Context7; InfluxDB patterns verified via Context7 and official docs
- Pitfalls: MEDIUM-HIGH — most pitfalls derived from verified API behaviour; DG sizing pitfall is ASSUMED

**Research date:** 2026-06-23
**Valid until:** 2026-07-23 (30 days; pandapower and influxdb-client have stable APIs; Docker image tags are pinned)
