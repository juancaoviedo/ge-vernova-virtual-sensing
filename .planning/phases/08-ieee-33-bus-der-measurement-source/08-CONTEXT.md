# Phase 8: IEEE 33-Bus DER Measurement Source - Context

**Gathered:** 2026-06-22
**Status:** Ready for planning

<domain>
## Phase Boundary

Build **System 1** — a re-runnable "ground-truth" measurement source. The enhanced IEEE
33-bus radial, balanced distribution network (renewable DER + RPC shunt capacitors + feeder
OLTC/phase-shifter) is modeled in **PandaPower**, driven through a **96-step (15-min) day**
whose solar/wind/load profiles are **ingested once** from the open-power-system-data 15-min
dataset into **InfluxDB**, with the **complete power-flow state captured at every step**,
persisted to InfluxDB, and visualized through a **provisioned Grafana dashboard** — all via
**Docker Compose** with a step-by-step **README runbook**.

This phase produces *only the truth*. The virtual-sensing estimator (System 2), the
measurement-noise / sensor-subset layer, and any true-vs-estimated error metrics are
explicitly later phases.

</domain>

<spec_lock>
## Requirements (locked via SPEC.md)

**7 requirements are locked.** See `08-SPEC.md` for full requirements, boundaries, and
acceptance criteria. Downstream agents MUST read `08-SPEC.md` before planning or
implementing. Requirements are not duplicated here.

**In scope (from SPEC.md):**
- Radial, balanced positive-sequence enhanced IEEE 33-bus model from the article data
- 4 renewable DG (solar+wind mix) at buses 18/22/25/33 + RPC shunt capacitors at 18 & 33
- Feeder OLTC + phase-shifter regulation at the substation
- One-time ingestion of the OPSD 15-min profiles (DE zone) into InfluxDB; the simulation
  reads its 96-step load+solar+wind profiles from InfluxDB at runtime
- Batch 96-step quasi-static time-series with the profiles' 15-min timestamps
- Full ground-truth power-flow state capture per step
- Local InfluxDB 2.x persistence (profiles **and** state snapshots) via Docker Compose
- Provisioned Grafana dashboard for visualization
- README runbook + pinned dependencies

**Out of scope (from SPEC.md):**
- Any synthetic or xlsx-interpolated profile fallback — explicitly rejected; if the dataset
  can't be fetched the phase halts and asks the user for the file
- Virtual-sensing / state-estimation module (System 2) — later phase
- Measurement-selection / sensor-noise "capture" layer — later phase
- True-vs-estimated state comparison / error metrics — requires System 2
- Unbalanced three-phase model; meshed configuration; BESS / EV assets; real-time
  wall-clock streaming loop; PSS/E cross-validation

</spec_lock>

<decisions>
## Implementation Decisions

### DER Day & Profiles
- **D-01:** Model a **high-DER sunny+breezy DE day** (strong midday solar + decent wind) —
  chosen to surface interview-grade physics: midday voltage rise at DER buses, reverse power
  flow toward the substation, active OLTC tapping, and a noon loss reduction.
- **D-02:** Scale each DG by the pre-normalized `DE_solar_profile` / `DE_wind_profile` (0–1)
  columns × its nameplate; scale loads by a peak-normalized `DE_load_actual_entsoe_transparency`
  curve. (Use the `*_generation_actual` columns normalized by capacity only if the profile
  columns are unusable.)
- **D-03:** Anchor the article's **3.715 MW total demand as the daily PEAK load** — so the
  feeder is most stressed at peak and DER relief is clearly visible at midday.

### DG Split & Sizing
- **D-04:** Sizing = **faithful to case33.xlsx / article nameplates** as the baseline. If
  total DG is too small to produce visible midday reverse flow / voltage rise on the chosen
  day, scale all DG **uniformly** to ~60–70% of the 3.715 MW peak. Any scaling is documented
  as an explicit, deliberate deviation (benchmark proportions preserved).
- **D-05:** Energy split = **solar drives buses 18 & 22; wind drives buses 25 & 33** (SPEC
  default).

### InfluxDB & Persistence
- **D-06:** **Two buckets** — `profiles` (one-time ingest of the 96-step load/solar/wind) and
  `state` (per-run power-flow snapshots). Separate retention/lifecycle for the one-time
  profiles vs the re-runnable snapshots.
- **D-07:** State schema = **per-entity-type measurements** (`bus`, `line`, `sgen`, `system`)
  with `bus_id` / `line_id` **tags**; fields = the state variables enumerated in SPEC req 5.
  This makes "bus 18 `vm_pu` across 96 steps" a single tag-filtered query and feeds the Grafana
  panels cleanly.
- **D-08:** Snapshots carry the chosen day's **real OPSD datetimes** (00:00–23:45, 15-min).
  Re-runs write identical measurement+tag+timestamp points → InfluxDB **overwrites in place**
  → deterministic, no duplicates. Grafana shows the real source date.

### Project Layout, Tooling & Orchestration
- **D-09:** New **dedicated top-level folder** for System 1, fully separate from `docs/`.
- **D-10:** Python managed by **uv (Astral)** — `pyproject.toml` + `uv.lock` for pinned,
  reproducible deps (pandapower, numpy, pandas, influxdb-client). The sim runs on the **host**
  via `uv run`.
- **D-11:** **Docker Compose deploys infrastructure only** (InfluxDB 2.x + Grafana). The sim
  is **not** containerized — it runs on the host and talks to the containers over localhost
  ports / env config.
- **D-12:** **README documents a clear step-by-step execution "rhythm"** — an ordered runbook:
  `uv sync` → `docker compose up` → ingest profiles → run the 96-step sim → open
  Grafana/InfluxDB.
- **D-13:** Grafana ships the **SPEC panel set** (bus-voltage profile/envelope, line loadings,
  total losses, DG solar/wind output, slack feed-in, OLTC tap), auto-provisioned with the
  InfluxDB datasource — no manual setup.

### Validation
- **D-14:** **Quantitative validation against published results** — the plain `case33bw` base
  case (no DER/caps/OLTC) reproduces the known **Baran & Wu solution (min voltage ≈ 0.913 pu
  at bus 18)** within tolerance as a correctness anchor; then the enhanced net asserts
  `pp.runpp` convergence **every step** and all 33 buses inside **0.95–1.05** across the 96
  steps.

### OPSD Day Selection
- **D-15:** The concrete DE day is selected **once** via a one-time data inspection (high solar
  capacity factor + decent wind) and **hard-coded as a config constant**; ingest extracts
  exactly that recorded day on every run (reproducible).

### Determinism
- **D-16:** **No stochastic elements** — fixed day, fixed profiles read from InfluxDB,
  deterministic Newton-Raphson power flow. Identical inputs → identical 96 snapshots. Any
  future stochastic element MUST be seeded.

### Claude's Discretion
The user explicitly delegated these to the researcher/planner:
- **OLTC / phase-shifter pandapower mechanism** (the user said "you decide"). *Recommended
  starting point:* a regulating feeder transformer at the head with pandapower
  `DiscreteTapControl` (or `ContinuousTapControl`) run via `pp.runpp(run_control=True)`; the
  phase shifter set to a scheduled `shift_degree` and captured. **Hard constraints (SPEC):**
  tap position + shift angle captured as state; tap within 0.95–1.05; feeder-secondary
  regulated near 1.0 pu. The planner may refine the exact controller/topology.
- **Orchestration mechanism** (the user said "you decide"). *Recommended:* uv-run entry points
  (e.g. `ingest`, `sim`) + a `Makefile`/`justfile` wrapping the full sequence, so the README
  rhythm maps to a few targets. Infra stays in Compose, sim on host via uv.
- Folder name, exact uv entry-point names, validation tolerances, and snapshot
  write-batching/perf are left to the planner.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Phase spec (read first)
- `.planning/phases/08-ieee-33-bus-der-measurement-source/08-SPEC.md` — **Locked
  requirements, boundaries, acceptance criteria. MUST read before planning/implementing.**

### Network model data (canonical, authoritative)
- `.planning/research/articles/ieee33.pdf` — Dolatabadi, Ghorbanian, Siano, Hatziargyriou,
  *"An Enhanced IEEE 33 Bus Benchmark Test System for Distribution System Studies,"* IEEE
  TPWRS 2020. Source of: 12.66 kV / 100 MVA base; slack at bus 1; tie-lines 33/34/35 open
  (radial); 4 DG at buses 18/22/25/33; RPC shunt caps at 18 (0.4 MVAr) & 33 (0.6 MVAr); feeder
  OLTC (0.95–1.05) + phase shifter (±5°); voltage band 0.95–1.05 p.u.; total demand
  3.715 MW + 2.3 MVAr; loads unchanged from Baran & Wu (so pandapower `case33bw` supplies
  correct loads). **Note: article bus N = pandapower index N−1 (0-indexed).**
- `.planning/research/articles/case33.xlsx` — full bus/branch/generator/cost tables + 24-pt
  hourly load-scaling and renewable arrays. **Primary source for DG nameplate ratings (D-04).**
  (The dynamic profiles come from the OPSD 15-min set, not these arrays.)

### Profile data source (external; one-time fetch only)
- open-power-system-data `time_series` (15-min), DE zone — `datapackage.json` +
  `time_series_15min_singleindex.csv` (≈107 MB) at
  `https://data.open-power-system-data.org/time_series/`. Columns:
  `DE_load_actual_entsoe_transparency`, `DE_solar_generation_actual` + `DE_solar_profile`
  (0–1), `DE_wind_generation_actual` + `DE_wind_profile` (0–1). One representative day =
  96 × 15-min steps. **Reachability verified 2026-06-22.** No fallback — halt + notify if
  unreachable (SPEC req 3).

### Build pattern (skeleton reference only — NOT canonical data)
- `github.com/Chinmaya-J-Jena/der_load_flow_IEEE33bus` — pandapower build pattern
  (`pn.case33bw()`, `pp.create_sgen(..., type="PV")`, manual quasi-static loop calling
  `pp.runpp(algorithm="nr", calculate_voltage_angles=True)`). Uses the *original* Baran & Wu
  case with the author's own DER placement and synthetic profiles → pattern only; canonical
  data comes from the article/xlsx above.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `docs/demos/*.py` (`dc_powerflow_baddata_demo.py`, `ekf_line_temp_demo.py`,
  `fedavg_fedprox_krum_demo.py`) — the repo's Python script style precedent (self-contained,
  NumPy + matplotlib PNG output). These are **teaching demos, not pandapower** — System 1 code
  is greenfield, but matching the "single self-contained, re-runnable script" ethos is a fit.
- `docs/build_site.py` — established "single entry point, re-runnable, with a validation gate"
  pattern. Mirror that ethos for the sim runner (one command builds+solves; validation asserts
  correctness).

### Established Patterns
- Repo is currently study-notes only — **no power-systems code, no Docker, no pandapower**.
  This is the first hands-on build phase, so System 1 establishes new conventions (a dedicated
  folder, uv tooling, Docker Compose) rather than extending existing ones.

### Integration Points
- **None today** — System 1 is an isolated new top-level folder. The **InfluxDB `state`
  bucket schema (D-07) is the forward contract**: the future virtual-sensing estimator
  (System 2, later phase) will consume these ground-truth snapshots. Design the schema to be
  queryable per-entity over time so System 2 can pull a reduced sensor subset later.

</code_context>

<specifics>
## Specific Ideas

- **High-DER day** explicitly chosen for its interview narrative: "watch the feeder ride
  through a sunny, breezy day — midday PV pushes voltage up and power back toward the
  substation, the OLTC taps to hold the band, losses dip at noon."
- **uv** (not pip/poetry) is the user's explicit tooling choice for reproducible Python envs.
- **Docker Compose for infra, sim on host** — explicit separation the user asked for.
- **README "rhythm"** — the user wants the runbook to read as a clear, ordered cadence of
  steps anyone can follow from a clean checkout.
- **Baran & Wu min voltage ≈ 0.913 pu at bus 18** is the concrete correctness anchor for the
  base-case validation (D-14).

</specifics>

<deferred>
## Deferred Ideas

- **Virtual-sensing estimator (System 2)** — the whole point this dataset feeds, but explicitly
  a later phase (SPEC out-of-scope).
- **Measurement-noise / reduced-sensor "capture" layer** — belongs to the System 2 phase that
  consumes this data.
- **True-vs-estimated error metrics / observability index (ORACS)** — requires System 2.
- **Aggressive DG sizing for strong reverse flow** (considered under DG sizing) — we chose
  faithful-scaled-if-needed (D-04); revisit only if System 2 needs more dynamic range.
- **Two-regime cloud-transient day** (considered under DER day) — rejected for this clean
  baseline; could become a future *dataset variant* to stress-test System 2 under volatility.
- **Containerizing the sim itself / adding a sim service to Compose** — deliberately not done
  (D-11, sim runs on host via uv); could be added later for full one-command reproducibility.
- **Unbalanced 3-phase model, meshed config, BESS/EV, real-time streaming loop** — all SPEC
  out-of-scope; noted so they aren't re-litigated.

</deferred>

---

*Phase: 8-ieee-33-bus-der-measurement-source*
*Context gathered: 2026-06-22*
