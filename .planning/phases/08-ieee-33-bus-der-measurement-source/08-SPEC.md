# Phase 8: IEEE 33-Bus DER Measurement Source — Specification

**Created:** 2026-06-22
**Ambiguity score:** 0.13 (gate: ≤ 0.20)
**Requirements:** 7 locked

## Goal

Build **System 1** — a re-runnable "ground-truth" measurement source: the radial, balanced
enhanced IEEE 33-bus distribution network with renewable DER (per `ieee33.pdf` / `case33.xlsx`)
modeled in PandaPower, driven through a **96-step (15-minute resolution) day** by solar+wind+load
profiles that are **ingested once from the open-power-system-data 15-minute dataset and stored in a
local InfluxDB** (the simulation then reads its profiles directly from InfluxDB — never re-fetching),
with the **complete power-flow state captured at every step**, persisted back to InfluxDB (Docker
Compose), and visualized through a provisioned **Grafana** dashboard. The virtual-sensing estimator
(System 2) is explicitly a later phase; this phase only produces the truth.

## Background

The repo is currently a study-notes/research project — it has **no power-systems code, no Docker, and
no pandapower** (only doc-build scripts under `docs/` and three NumPy teaching demos under
`docs/demos/`). This is the first hands-on build phase.

Source material is in hand and inspected:
- **`.planning/research/articles/ieee33.pdf`** — Dolatabadi, Ghorbanian, Siano, Hatziargyriou,
  *"An Enhanced IEEE 33 Bus Benchmark Test System for Distribution System Studies,"* IEEE TPWRS 2020.
  12.66 kV, 100 MVA base; 33 buses; slack at bus 1; 32 fixed + 3 switchable (tie) branches
  (33: 21–8, 34: 12–22, 35: 25–29); 4 DG units at buses **18/22/25/33**; RPC shunt capacitors at
  bus **18 (0.4 MVAr)** and **33 (0.6 MVAr)** in the radial config; OLTC (0.95–1.05) + phase shifter
  (±5°) at the feeder (branch 1); voltage band **0.95–1.05 p.u.**; total demand **3.715 MW + 2.3 MVAr**.
  The article states bus *loads are unchanged from Baran & Wu*, so pandapower's built-in
  `case33bw` supplies the correct loads.
- **`.planning/research/articles/case33.xlsx`** — full bus/branch/generator/cost tables plus a 24-point
  hourly load-scaling array and a 24-point renewable array (reference data; the dynamic profiles come
  from the 15-minute open dataset below, not these arrays).
- **open-power-system-data `time_series` (15-min)** — the article's cited profile source (ref [34]).
  **Reachability verified 2026-06-22:** `datapackage.json` and
  `time_series_15min_singleindex.csv` both return HTTP 200 (CSV ≈ 107 MB, `text/csv`). The **DE
  (Germany)** zone carries a complete 15-min triple plus pre-normalized capacity factors:
  `DE_load_actual_entsoe_transparency`, `DE_solar_generation_actual` + `DE_solar_profile` (0–1),
  `DE_wind_generation_actual` + `DE_wind_profile` (0–1). One representative day = 96 × 15-min steps.
- **Reference repo** `github.com/Chinmaya-J-Jena/der_load_flow_IEEE33bus` (cloned, read) — a useful
  **pattern** for the pandapower build (`pn.case33bw()`, `pp.create_sgen(..., type="PV")`, a manual
  quasi-static loop calling `pp.runpp(algorithm="nr", calculate_voltage_angles=True)`). It uses the
  *original* Baran & Wu case with the author's *own* DER placement (PV 14/31, BESS, EV) and *synthetic*
  profiles — so it is a skeleton reference only; canonical data comes from the article/xlsx.

Note: article bus N = pandapower index **N−1** (0-indexed), confirmed by the reference repo.

## Requirements

1. **Enhanced IEEE 33-bus model (radial, balanced)**: A PandaPower model of the article's radial
   enhanced benchmark builds and solves from a single Python entry point.
   - Current: no pandapower model exists anywhere in the repo
   - Target: a builder produces the radial balanced net — `case33bw` base loads; tie-lines 33/34/35
     **open**; 4 renewable DG `sgen` at buses **18/22/25/33**; RPC shunt capacitors at **18 (0.4 MVAr)**
     and **33 (0.6 MVAr)**; feeder **OLTC + phase shifter** at the substation (branch 1) — and a
     Newton-Raphson power flow converges
   - Acceptance: `pp.runpp` converges on the built net; total load ≈ 3.715 MW + 2.3 MVAr; all 33 buses
     present; a single command builds + solves with no exception

2. **Feeder OLTC + phase-shifter regulation**: The substation regulator is modeled and active each step.
   - Current: no transformer/tap control modeled
   - Target: an on-load tap changer (tap range 0.95–1.05) and a phase shifter (±5°) at the feeder
     regulate feeder voltage at every step; the resulting **tap position and phase-shift angle are part
     of the captured state**
   - Acceptance: the net contains a regulating feeder transformer; across the 96-step run the tap
     position is recorded per step and stays within 0.95–1.05; solved feeder-side voltage tracks the
     regulation target

3. **One-time profile ingestion from the 15-min open dataset into InfluxDB**: The solar/wind/load profiles
   are fetched once and stored in InfluxDB; the simulation never fetches them again at runtime.
   - Current: no profiles exist; the OPSD 15-min dataset lives only on the remote endpoint
   - Target: an ingestion step fetches the **open-power-system-data 15-min** dataset, extracts **one
     representative day** of the **DE** zone (`DE_load_actual_entsoe_transparency`, `DE_solar_profile`,
     `DE_wind_profile` — or the `*_generation_actual` columns normalized), producing 96 × 15-min
     normalized (load, solar, wind) values, and **writes them to InfluxDB** (a dedicated profiles
     measurement/bucket). The step is idempotent (skip/refresh if already present).
     **No interpolation or synthetic fallback** — if the endpoint is unreachable, the step **halts and
     notifies the user** (the user will source the file and provide it) rather than substituting data.
   - Acceptance: after ingestion, InfluxDB holds **96** timestamped (load, solar, wind) profile points for
     the day; an unreachable-endpoint run exits non-zero with a clear "dataset unreachable — provide the
     file" message and writes **no** substitute data

4. **96-step driver that reads profiles from InfluxDB (batch)**: A batch runner sweeps the day using the
   profiles already stored in InfluxDB.
   - Current: no simulation loop exists
   - Target: a runner **reads the 96-step (load, solar, wind) profiles from InfluxDB** (not from the
     network, not from the xlsx); per step it scales loads by the load profile, sets each DG `sgen`
     active power from its solar/wind profile (**solar** drives a subset of DG buses, **wind** the
     complementary subset — e.g. solar→{18,22}, wind→{25,33}; exact split is a plan-phase detail), lets
     the OLTC regulate, runs `pp.runpp`, and captures state; each step carries the profile's 15-min
     timestamp across one day; the run is re-runnable and deterministic
   - Acceptance: with profiles present in InfluxDB, one command runs all 96 steps to completion producing
     96 timestamped snapshots; the runner performs **no network fetch** of profile data; re-running yields
     identical snapshots

5. **Full ground-truth state captured per step**: Each snapshot is the complete power-flow state.
   - Current: nothing is captured
   - Target: each of the 96 snapshots stores — per bus: `vm_pu`, `va_degree`; per in-service line:
     P/Q at both ends, `loading_percent`, line losses; slack/ext_grid P/Q feed-in; each DG `sgen` P/Q;
     OLTC tap position + phase-shift angle; system scalars: total load, total generation, total losses,
     Vmin, Vmax
   - Acceptance: a snapshot contains every bus (33) and every in-service line; on converged steps there
     are no NaNs; all enumerated fields are present

6. **Local InfluxDB persistence (Docker Compose)**: All snapshots land in a queryable local time-series DB.
   - Current: no Docker, no InfluxDB
   - Target: a `docker-compose.yml` starts **InfluxDB 2.x (OSS)** locally; the runner writes all 96
     snapshots as timestamped points (measurements keyed by entity id/type), at 15-min spacing
   - Acceptance: after a run, an InfluxDB query returns a **96-point** time-series for a chosen variable
     (e.g. bus 18 `vm_pu`); `docker compose up` + run results in populated buckets

7. **Grafana dashboard + reproducible runbook**: Variable evolution is visible out-of-the-box and the
   whole stack is documented.
   - Current: none
   - Target: Docker Compose also starts **Grafana**, auto-provisioned with an InfluxDB datasource and a
     **prebuilt dashboard** (panels for bus-voltage profile/envelope, line loadings, total losses, DG
     solar/wind output, slack feed-in, OLTC tap); a README documents prerequisites, `docker compose up`,
     running the 96-step sim, where data lands, and how to open InfluxDB Data Explorer + Grafana; deps
     are pinned
   - Acceptance: Grafana opens in a browser and the provisioned dashboard renders the 96-step evolution
     of the listed variables **without manual setup**; following the README from a clean state brings up
     the stack and reproduces the 96-snapshot dataset

## Boundaries

**In scope:**
- Radial, balanced positive-sequence enhanced IEEE 33-bus model from the article data
- 4 renewable DG (solar+wind mix) at buses 18/22/25/33 + RPC shunt capacitors at 18 & 33
- Feeder OLTC + phase-shifter regulation at the substation
- One-time ingestion of the open-power-system-data 15-min profiles (DE zone) into InfluxDB; the
  simulation reads its 96-step load+solar+wind profiles from InfluxDB at runtime
- Batch 96-step quasi-static time-series with the profiles' 15-min timestamps
- Full ground-truth power-flow state capture per step
- Local InfluxDB 2.x persistence (profiles **and** state snapshots) via Docker Compose
- Provisioned Grafana dashboard for visualization
- README runbook + pinned dependencies

**Out of scope:**
- Any synthetic or xlsx-interpolated profile fallback — explicitly rejected; if the dataset can't be
  fetched the phase halts and asks the user for the file
- Virtual-sensing / state-estimation module (System 2) — explicitly a later phase; this phase only
  produces ground truth
- Measurement-selection / sensor-noise "capture" layer (the reduced sensor subset) — belongs to the
  virtual-sensing phase that consumes this data
- True-vs-estimated state comparison / error metrics — requires System 2, later phase
- Unbalanced three-phase model — balanced positive-sequence chosen for this phase (much larger build)
- Meshed configuration — radial chosen (tie-lines stay open)
- BESS / EV assets — not specified by the article; excluded to stay faithful (the reference repo's
  additions, not the benchmark's)
- Real-time wall-clock streaming loop — batch chosen; a live/accelerated loop is deferred
- PSS/E (or other tool) cross-validation — not required; validate against the article's published
  power-flow results instead

## Constraints

- **PandaPower** balanced `runpp` (Newton-Raphson, `calculate_voltage_angles=True`) on Python 3.12;
  pinned deps (pandapower, numpy, pandas, influxdb-client).
- **Docker + Docker Compose** available locally (InfluxDB 2.x + Grafana containers).
- Base **100 MVA / 12.66 kV**; voltage band **0.95–1.05 p.u.**; article bus N = pandapower index N−1.
- The 15-min open dataset requires network for the **one-time ingestion only** (reachability verified
  2026-06-22). There is **no fallback**: if the endpoint is unreachable the ingestion **halts and
  notifies the user** — it must never substitute synthetic or xlsx-interpolated data. Once ingested, the
  profiles live in InfluxDB and the simulation runs fully offline against them.
- **Determinism:** identical inputs must yield identical 96 snapshots (no wall-clock randomness; any
  stochastic element seeded).
- Modeling the OLTC means the ground-truth state depends on the regulator — accepted; tap/angle are
  captured as state so the dependence is observable.
- Repo convention: work proceeds under the GSD workflow; no git worktrees (main tree only).

## Acceptance Criteria

- [ ] `docker compose up` starts InfluxDB 2.x and Grafana locally
- [ ] One command builds the radial balanced enhanced IEEE 33-bus net and `pp.runpp` converges
- [ ] The model contains DG `sgen` at buses 18/22/25/33, RPC shunt capacitors at 18 & 33, and a feeder OLTC + phase shifter
- [ ] The 96-step batch run completes and writes 96 timestamped snapshots
- [ ] Each snapshot contains full state: all 33 bus `vm_pu`+`va_degree`, all in-service line P/Q+`loading_percent`, slack P/Q, DG P/Q, OLTC tap+angle, system losses & Vmin/Vmax
- [ ] Ingestion writes 96 timestamped (load, solar, wind) profile points (DE 15-min) into InfluxDB; the simulation reads profiles **from InfluxDB** and performs no profile fetch at run time
- [ ] If the dataset endpoint is unreachable, ingestion exits non-zero, notifies the user, and writes no substitute data (no synthetic/xlsx fallback)
- [ ] Solar drives a subset of DG buses and wind the complementary subset
- [ ] An InfluxDB query returns a 96-point time-series for a chosen variable (e.g. bus 18 `vm_pu`)
- [ ] A provisioned Grafana dashboard renders the 96-step evolution of the key variables without manual setup
- [ ] Re-running the simulation produces identical snapshots (deterministic)
- [ ] Following the README from a clean state brings up the stack and reproduces the 96-snapshot dataset

## Ambiguity Report

| Dimension          | Score | Min  | Status | Notes                                                        |
|--------------------|-------|------|--------|--------------------------------------------------------------|
| Goal Clarity       | 0.90  | 0.75 | ✓      | Radial / balanced / batch / 96×15-min / full-state→Influx    |
| Boundary Clarity   | 0.88  | 0.70 | ✓      | Virtual sensing, measurement-noise, BESS/EV, meshed excluded |
| Constraint Clarity | 0.82  | 0.65 | ✓      | Dataset + offline fallback; OLTC; pinned deps; determinism   |
| Acceptance Criteria| 0.85  | 0.70 | ✓      | 10 pass/fail checks incl. Grafana dashboard render           |
| **Ambiguity**      | 0.13  | ≤0.20| ✓      |                                                              |

Status: ✓ = met minimum, ⚠ = below minimum (planner treats as assumption)

## Interview Log

| Round | Perspective     | Question summary                          | Decision locked                                                  |
|-------|-----------------|-------------------------------------------|------------------------------------------------------------------|
| 1     | Researcher      | Which topology — radial/meshed/both?      | **Radial only** (tie-lines open, RPCs at 18/33)                  |
| 1     | Researcher      | Balanced vs unbalanced three-phase?       | **Balanced positive-sequence** (pandapower `runpp`)             |
| 1     | Researcher      | What does "run continuously" mean?        | **Batch run** with simulated timestamps (re-runnable)           |
| 2     | Simplifier      | Which DER/assets — article vs +BESS/EV?   | **Article-faithful**: 4 DG + 2 RPC only (no BESS/EV)            |
| 2     | Boundary Keeper | Profile source — interp/15-min/synthetic? | **15-min open dataset**; cadence → **15-min = 96 steps/day**     |
| 2     | Boundary Keeper | Persist full state or also measurements?  | **Full ground-truth state only** (measurement layer = later)    |
| 3     | Seed Closer     | DER energy source — solar/wind/generic?   | **Solar + wind mix** across DG buses                            |
| 3     | Seed Closer     | InfluxDB done-bar — UI/Grafana/storage?   | **InfluxDB + prebuilt Grafana dashboard**                       |
| 3     | Seed Closer     | Model feeder OLTC or simple slack?        | **Model OLTC + phase-shifter regulation** (tap captured)        |
| 3.5   | User directive  | Fallback vs ingest-to-InfluxDB?           | **No fallback**: ingest OPSD 15-min → InfluxDB once; sim reads from InfluxDB; halt+notify if unreachable (reachability verified) |

---

*Phase: 08-ieee-33-bus-der-measurement-source*
*Spec created: 2026-06-22*
*Next step: /gsd-discuss-phase 8 — implementation decisions (InfluxDB schema/version & buckets for profiles vs state, OPSD representative-day selection & DE normalization, OLTC mechanism in pandapower, solar/wind bus split, file layout)*
