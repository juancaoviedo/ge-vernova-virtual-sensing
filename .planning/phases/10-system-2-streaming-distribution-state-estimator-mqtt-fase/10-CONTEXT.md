# Phase 10: System 2 — Streaming Distribution State Estimator (MQTT + FASE) - Context

**Gathered:** 2026-06-26
**Status:** Ready for planning

<domain>
## Phase Boundary

**System 2** — the distribution state estimator. It consumes the Phase-9 `measurements` (noisy,
sparse `z` + `assumed_sigma` + class/quantity/location/scenario/experiment/phase tags) over an **MQTT
stream**, plus a **retained, versioned network-topology config** on `ieee33/netmodel/current`, and
reconstructs the full node-voltage state `x = {|V|, θ}` at every energised bus (~64 states, bus 0 =
slack reference) **with a calibrated posterior covariance `P`**. Three estimators (AC-WLS snapshot
baseline, recursive EKF, recursive UKF) run behind one predict/update interface; `Ybus` is derived
from the streamed topology (never transported as a matrix). Output `(x̂, P)` + `trace_P` (= ORACS
observability index) lands in a new `estimates` bucket and is scored against the System 1 / 8.1
oracle by a **separate** harness that the estimators never read. Two regimes: `day` (observability
story) and `fault` (island-mode covariance inflation). Entirely additive to
`system1-measurement-source/`. Stage 3 of the build: System 1 → Measurement System (P9) → **System 2
(P10)** → System 3 (later).

</domain>

<spec_lock>
## Requirements (locked via SPEC.md)

**13 requirements are locked.** See `10-SPEC.md` for full requirements, boundaries, and acceptance criteria.

Downstream agents MUST read `10-SPEC.md` before planning or implementing. Requirements are not duplicated here.

**In scope (from SPEC.md):** Mosquitto broker added to docker-compose (localhost-bound, additive);
`publish` replay runner (`measurements` → MQTT, deterministic order, accelerable, day+fault); the
retained/versioned `ieee33/netmodel/current` topology topic (the seam System 3 reuses); AC measurement
model (`h(x)` per class + analytic Jacobian `H`) with `Ybus` **derived from streamed topology**;
`estimate` runner (MQTT subscriber for measurements + netmodel + snapshot assembler, version-aware
`Ybus` rebuild); three estimators (AC-WLS w/ χ²/LNR, recursive EKF, recursive UKF) behind one
interface; FASE predict = profile-as-noisy-forecast + `Q`, update-on-arrival, multirate-aware;
`estimates` InfluxDB bucket (`x̂, P, trace_P` tagged scenario/experiment/estimator); separate `score`
harness (RMSE, dark-node error, baseline comparison, NEES/NIS calibration); both regimes; determinism,
auto-provisioned Grafana estimator dashboard(s), README runbook; new `uv` scripts.

**Out of scope (from SPEC.md):** System 3 (self-healing/FLISR, CaCSM dispatch, simulate-before-commit,
the `netmodel/proposed` half); three-phase unbalanced state; branch-current (BCSE) formulation;
federated/multi-area DSSE; non-MQTT transports (C37.118-over-UDP, NATS, 2030.5); LinDistFlow linear-KF
as a deliverable; parameter/topology estimation (`Ybus`+connectivity are known inputs); ANY change to
System 1 / 8.1 / Phase 9 code, physics, buckets, or dashboards (additive only).

</spec_lock>

<decisions>
## Implementation Decisions

These are the HOW-to-implement choices made in discussion. They refine — never override — the 13
locked SPEC requirements and the ROADMAP's locked design decisions D1–D6.

### Runner & config ergonomics (mirrors Phase 9)
- **D-01:** **Three separate runners** — `publish` (InfluxDB→MQTT replay), `estimate` (subscribe +
  estimate), `score` (estimate-vs-oracle) — added as `[project.scripts]` entries
  (`publish`/`estimate`/`score` → `uv run …`), mirroring P9's `measure` pattern. The MQTT broker
  decouples `publish` from `estimate` (real async stream, per SPEC R2/R4 — NOT an in-process loop).
- **D-02:** **`estimate` runs ONE estimator per invocation**, selected by config/CLI
  `--estimator wls|ekf|ukf`. Each run tags its `estimates` output by the `estimator` tag so the three
  accumulate in the bucket and are directly comparable. (Rejected: an all-three-per-run fan-out — the
  per-estimator model keeps runs light, matches P9's one-experiment-per-run ergonomics, and isolates
  failures.)
- **D-03:** **New `estimate_config.py` with an `ACTIVE` block** mirroring `measure_config.py` (D-08/D-09
  of P9): config-file-first switch for `scenario / source / sampling / estimator / seed / acceleration`
  plus the forecast-error knobs (D-07), with **CLI overrides** (`--scenario --source --estimator --seed
  --acceleration …`) defaulting to the config values, to enable sweeps without editing the file.

### FASE predict step (the D4 "no-cheating" core)
- **D-04:** **Predict mean = sensitivity-propagated profile forecast (primary)**, with **random-walk
  persistence implemented as the A/B baseline foil behind the same predict interface.** The contrast
  ("forecast beats persistence at load ramps") is part of the deliverable, not just the primary path.
- **D-05:** **Forecast computation (primary path):** (1) read the scheduled nodal injections for step
  *k* from the **`profiles` bucket** — see D-06; (2) degrade into a forecast `p_fcst(k) =
  p_sched(k)·(1+ε)` with a seeded forecast error `ε`; (3) compute the injection change `Δp =
  p_fcst(k) − p_fcst(k−1)`; (4) map to a state change through the network sensitivity `S = ∂x/∂p`
  (inverse power-flow Jacobian, reuse the `H` from the measurement model evaluated at `x̂ₖ₋₁`):
  `x̂ₖ⁻ = x̂ₖ₋₁ + S·Δp_fcst`; (5) process noise `Qₖ = S·Cov(ε)·Sᵀ + Q_floor`, with `Q_floor` keeping
  `Q` positive-definite at flat load. Same `Qₖ` feeds the UKF. The estimator anticipates the
  morning/evening ramp and `Q` honestly widens on steep ramps.
- **D-06:** **Reading `profiles` is allowed and is NOT an oracle leak.** The `profiles` bucket holds
  the load/DER *schedule* (legitimate operator day-ahead side-information — "the forecast IS the
  transition model"). The oracle that stays forbidden to the estimator is **`state` / `fault_event`**
  (the realized voltages). This boundary must be documented and grep-checkable: estimator reads
  `measurements` (MQTT) + `netmodel/current` (MQTT) + `profiles` (forecast); it never reads
  `state`/`fault_event`. (Refines SPEC R9 / Constraint "estimators never read the oracle" — `profiles`
  is explicitly carved out as forecast input, distinct from the oracle answer.)
- **D-07:** **Forecast-error model = realistic day-ahead, config-tunable.** Default per-bus σ ≈ 5% of
  scheduled load, AR(1)-correlated (ρ tunable), **seed-derived** for determinism, exposed as knobs in
  `estimate_config.py` so the forecast-quality-vs-accuracy tradeoff can be studied. Defensible framing:
  "this mirrors real day-ahead load-forecast error." Must NOT reuse the realized truth (no peeking at
  `state`); the error is added on top of the *schedule*, so the predict is honestly imperfect even
  though the same profile generated the truth.

### Dashboards
- **D-08:** **Two auto-provisioned estimator dashboards**, mirroring P9's two-dashboard pattern,
  additive to the four existing dashboards:
  - `ieee33-est-day.json` — true-vs-estimated voltage overlay (per selectable bus), per-bus error
    heatmap, `trace_P` (ORACS observability index) timeseries, NEES/NIS calibration panel(s),
    dark-node recovery (pseudo-only buses) panel.
  - `ieee33-est-fault.json` — adds island-mode `P`-inflation (σ_V / `trace_P` rising in
    `faulted_isolated`) and the `pre_fault`/`faulted_isolated`/`restored` phase-region markers.
  (Rejected: a single combined dashboard with a template variable — two dashboards keep the
  day-observability and fault-island narratives cleanly separated, matching the existing convention.)

### Claude's Discretion (recommended, locked for downstream — adjust only with reason)
- **MQTT topic hierarchy & payload (extends the P9 tag taxonomy):**
  - measurements: `ieee33/{experiment}/{scenario}/meas/{class}/{location}`, JSON payload
    `{value, assumed_sigma, quantity, class, location, experiment, scenario, phase, timestamp}`
    (carries the exact P9 `meas` tag/field set — see P9 D-06).
  - topology re-publish: `ieee33/{experiment}/{scenario}/event`, payload = the P9 `event` fields
    (`faulted_line_id, tie_closed, tie_id, n_dead_buses, dead_buses, phase`).
  - **network config (the System 3 seam): `ieee33/netmodel/current`, RETAINED + versioned** — payload
    = authoritative switch-state (in-service line set + tie states + dead-bus set + `phase`) +
    monotonic `config_version` + timestamp. **NOT the raw `Ybus`.** One run = one (experiment,scenario)
    at a time, so the global `netmodel/current` topic is unambiguous; for `day` publish version 0 once
    (retained); for `fault` publish a new version per topology change
    (`pre_fault`→`faulted_isolated`→`restored`). (SPEC R2/R3 lock the topic + retained/versioned
    semantics; the exact JSON field names are executor detail within this shape.)
- **Topology→`Ybus` rebuild method:** apply the streamed in-service-line set + tie states to the
  **static** line/bus impedances from `build_enhanced_33bus()` and assemble `Ybus` directly (verified
  to < 1e-9 against the pandapower-extracted `Ybus` via `pd2ppc`/`makeYbus`, per SPEC R3 acceptance).
  A `config_version` bump triggers a rebuild and marks the step as a known topology change (so the
  innovation jump is not mis-flagged as bad data). Method (hand-built Y vs pandapower `makeYbus` on a
  rebuilt net) is the planner/executor's call — the equality test is the gate.
- **UKF parameterization:** square-root UKF (numerical stability per ROADMAP D1) with standard
  sigma-point params (α, β, κ) — researcher/planner to set sensible defaults; pluggable behind the
  same predict/update interface as the EKF.
- **AC-WLS bad-data machinery:** reuse the χ²/largest-normalized-residual approach from the existing
  DC bad-data demo (`dc_powerflow_baddata_demo.py`) lifted to the AC residuals.
- Exact `estimate_config.py` field names, Flux query details for reading `measurements`/`profiles`,
  Grafana panel layout, NEES/NIS band computation details, and the `Q_floor` magnitude are
  planner/executor details within the locked intent above.

### Gap-closure design — forecast-over-MQTT + correct sensitivity + 64-state (2026-07-01; SUPERSEDES the D-05/D-06 predict path)

Live UAT (`10-UAT.md`) found the D-05 predict path non-functional: `S` was built from the sparse
measurement Jacobian (columns = injection *measurements*) while `Δp` was per-bus, so `S·Δp` crashed
(bug #2); and the state was sized `66 = 2×33` (slack included), leaving WLS rank-deficient (bug #3).
These decisions replace the predict/forecast wiring. The "forecast IS the schedule + noise, oracle
stays separate" principle (D-06) is preserved. The measurement→state reconstruction (26 meas → 64
state) is unchanged and correct — it lives in the UPDATE step; these decisions only touch PREDICT.

- **D-09:** The forecast is an external MQTT stream from a new `forecast` publisher (supersedes the
  in-estimator scalar read of `profiles`). New `forecast.py` (sibling of `publish.py`; new
  `[project.scripts]` `forecast`) reconstructs the SCHEDULED per-bus injections from legal
  side-information ONLY — static per-bus nominal `(P_nom, Q_nom)` + `sgen`/DER placements from
  `build_enhanced_33bus()`, scaled by the `profiles` multipliers `load_pu`/`solar_pu`/`wind_pu` —
  then degrades them with seeded, per-class noise (load: AR(1) Gaussian σ≈3–5%; DER: larger skewed
  σ≈15–30%) and publishes, per step in deterministic accelerable order, the full per-bus injection
  forecast. Topic `ieee33/{experiment}/{scenario}/forecast`, one message per timestep carrying
  `{timestamp, step_k, p_fcst{bus}, q_fcst{bus}, sigma_p{bus}, sigma_q{bus}}`, QoS1, republished
  RETAINED as "latest" for late subscribers (mirrors `netmodel/current`). MUST be built from the
  SCHEDULE, NEVER the realized `state`/`fault_event` oracle — oracle separation stays grep-checkable.
- **D-10:** Correct FASE sensitivity `S = ∂x/∂p` over BUS INJECTIONS (fixes bug #2). New
  `ac_model.injection_sensitivity(x, Ybus)` builds `S` from the power-flow injection Jacobian
  `J_p = ∂[P;Q]/∂[θ;|V|]` over non-slack buses, `S = J_p⁻¹` reordered to the state layout — shape
  `(n_state × 2·n_nonslack)`, columns = bus injections, INDEPENDENT of the measurement set (the
  count 26 never appears in predict). The old measurement-Jacobian pseudoinverse (`fase_sensitivity`)
  is NO LONGER used for predict. `FASEPredictor.predict` consumes `Δp=[ΔP;ΔQ]` and `Cov(ε)` from the
  forecast stream (no longer reads `prof_df` / broadcasts a scalar): `x⁻ = x_prev + S·Δp`;
  `Q = S·Cov(ε)·Sᵀ + Q_floor`. Persistence foil (D-04) = `Δp:=0` behind the same interface.
- **D-11:** State vector is 64 = 2×32, slack bus 0 EXCLUDED (fixes bug #3), applied consistently in
  `ac_model` / `estimators` / `estimate`. Removes the two unobservable slack states (`|V|₀,θ₀`)
  that made WLS's `G=HᵀWH` rank-deficient on `well_observed`; `x`, `S`, `Δp` share the 64/32
  definition. Also re-audit the snapshot→`z`/`H` assembly so the full `well_observed` measurement
  set reaches `H` and `G` is full-rank WITHOUT pseudo (R5 real-only-observable expectation).

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Phase 10 spec (locked)
- `.planning/phases/10-system-2-streaming-distribution-state-estimator-mqtt-fase/10-SPEC.md` — 13
  locked requirements (R1–R13), boundaries, constraints, acceptance criteria. MUST read before planning.

### ROADMAP locked design decisions (D1–D6)
- `.planning/ROADMAP.md` §"Phase 10" — D1 (WLS + EKF→UKF estimators), D2 (full AC via `Ybus` inside
  `h(x)`), D3 (MQTT replay + indicative topic design), D4 (profile-as-noisy-forecast predict), D5
  (oracle kept separate), D6 (`estimates` output contract). The indicative 5–6-plan breakdown lives here.

### Phase 9 forward contract (the data + MQTT payload this phase consumes)
- `.planning/phases/09-measurement-system-observability-layer-configurable-sensor-m/09-CONTEXT.md` —
  P9 decisions, esp. **D-06** (`meas` point schema: tags `class/quantity/location/scenario/experiment/phase`,
  fields `value`+`assumed_sigma`, NO `true_value`) and **D-07** (`event` topology re-publish schema) —
  these define the MQTT payloads. Also D-02/D-03 (`energised` tag, dead-bus zero-fill, no live/pseudo
  meas for dead buses), D-04/D-05 (sensor-bus assignments per scenario), D-11..D-14 (noise/sampling).
- `.planning/phases/09-measurement-system-observability-layer-configurable-sensor-m/09-SPEC.md` — the
  `measurements` bucket contract System 2 reads from.

### Phase 8 / 8.1 oracle + topology contract
- `.planning/phases/08.1-system-1-fault-and-reconfiguration-scenario/08.1-CONTEXT.md` — fault topology
  facts the netmodel config encodes: FAULT_LINE_IDX=7, dead buses 8–17, restore tie idx 34, phases
  `pre_fault`/`faulted_isolated`/`restored`, 40-step window. (Oracle buckets `state`/`fault_event` —
  read ONLY by the `score` harness.)

### System code to reuse / extend (all additive — do NOT modify existing behaviour)
- `system1-measurement-source/src/ieee33/network.py` §`build_enhanced_33bus()` (L82-248) — the
  pandapower net + static line/bus impedances; source of `Ybus` (post-`runpp`/`pd2ppc`).
- `system1-measurement-source/src/ieee33/influx.py` — `get_client`/`wait_for_influx`/`ensure_bucket`
  (create `estimates` bucket), `read_profiles` (Flux pivot pattern — reuse to read the forecast
  schedule and the `measurements`), the locked `build_meas_point`/`build_event_point` schema.
- `system1-measurement-source/src/ieee33/measure.py` + `measure_config.py` — the runner +
  config-`ACTIVE`-block + CLI-override pattern to mirror for `estimate`/`estimate_config.py`.
- `system1-measurement-source/src/ieee33/sim.py` / `fault_sim.py` — deterministic runner + console
  footprint table patterns to mirror (do NOT modify).
- `system1-measurement-source/docker-compose.yml` — InfluxDB 2.9.1 + Grafana 11.6.15 stack
  (localhost-bound); add an `eclipse-mosquitto` service additively.
- `system1-measurement-source/grafana/provisioning/dashboards/` — auto-provisioning pattern; add two
  new estimator JSONs, leave the four existing dashboards untouched.
- `system1-measurement-source/pyproject.toml` — `[project.scripts]` (add `publish`/`estimate`/`score`);
  deps (add `paho-mqtt`, reuse `pandapower`/`numpy`/`influxdb-client`).
- The DC bad-data teaching demo (`dc_powerflow_baddata_demo.py`, referenced in SPEC Background) — the
  χ²/LNR machinery to lift into the AC-WLS estimator. *(Locate at plan time — not found at repo root
  during scout; confirm path.)*

### Study-material grounding (DSSE / FASE / observability theory)
- `.planning/phases/02-distribution-virtual-sensing/` notes — DSSE node-voltage formulation,
  pseudo-measurements, χ²/normalized-residual bad-data test, observability framing, FASE thesis.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `influx.get_client`/`wait_for_influx`/`ensure_bucket` — connection + `estimates` bucket creation.
- `influx.read_profiles` (Flux pivot → DataFrame) — copy for reading the forecast schedule and the
  `measurements`.
- `network.build_enhanced_33bus()` — pandapower net + static impedances → `Ybus` + the `H`/sensitivity
  `S` source.
- `measure.py` + `measure_config.py` — runner skeleton + `ACTIVE`-block/CLI-override config pattern.
- `sim.py`/`fault_sim.py` — deterministic per-step runner + console table patterns.

### Established Patterns
- **Config-file-first switch** with CLI overrides (P9 D-09) — carry into `estimate_config.py`.
- **Seeded determinism is a hard project norm** — `sim.py`/`fault_sim.py`/`measure.py` all deterministic;
  System 2 paths must have no unseeded `random`/`np.random`/wall-clock (SPEC R13).
- Per-entity InfluxDB schema with string tags; deterministic overwrite-in-place (measurement+tags+ts).
- Article-N = pandapower idx N-1 (0-indexed).
- `uv` / Python 3.12 / Docker InfluxDB+Grafana auto-provisioning.

### Integration Points
- New modules in `src/ieee33/`: a `publish` runner, an `estimate` runner + `estimate_config.py`, an AC
  measurement-model module (`h(x)`/`H`/`Ybus`-from-topology + sensitivity `S`), the three estimators
  behind one interface, a `score` harness; new `estimates` bucket; two new Grafana JSONs; an
  `eclipse-mosquitto` docker-compose service; new `paho-mqtt` dep; three new `[project.scripts]`.
- All additive — System 1's day, the 8.1 fault scenario, Phase 9's measurement layer, and their four
  buckets + four dashboards stay untouched (verifiable by `git`/`grep`).

</code_context>

<specifics>
## Specific Ideas

- The **forecast-beats-persistence contrast is a deliverable**, not incidental: random-walk persistence
  is implemented as the baseline foil behind the same predict interface so the FASE advantage is shown
  executably (D-04).
- The **`profiles`-is-forecast / `state`-is-oracle distinction** is the rhetorical centre of the
  "isn't that cheating?" interview answer — it must be documented and grep-checkable (D-06).
- `trace_P` / per-bus σ_V is framed as the **ORACS Observability index** the AGMS architecture gates
  on; the fault dashboard's `P`-inflation panel is the island-mode-resilience showpiece.
- `netmodel/current` is deliberately the **seam System 3 reuses** — design it cleanly now even though
  the `netmodel/proposed` / simulate-before-commit half is out of scope here.

</specifics>

<deferred>
## Deferred Ideas

- **System 3** (self-healing / FLISR loop, CaCSM volt/VAR dispatch, simulate-before-commit, the
  `netmodel/proposed` candidate channel + promotion logic) — next phase; `netmodel/current` is the seam.
- **Three-phase unbalanced state**, **branch-current (BCSE) formulation**, **federated/multi-area DSSE
  with boundary-state exchange** — talking points / possible later phases, not this build.
- **Non-MQTT transports** (real C37.118-over-UDP, NATS, IEEE 2030.5) — MQTT only here.
- **LinDistFlow linear-KF** as a deliverable — full AC is the chosen model; LinDistFlow is
  awareness-only (and the linear sensitivity `S` used in the predict step is the closest this phase
  gets to it).
- **Mis-specified-noise robustness study** (`assumed_sigma_scale ≠ 1.0`) and the **forecast-quality
  sweep** (varying the D-07 forecast-error σ) — the config knobs are built (D-03/D-07) but gating these
  studies is out of scope for this phase.

None of the above were in-scope detours — discussion stayed within the phase boundary.

</deferred>

---

*Phase: 10-system-2-streaming-distribution-state-estimator-mqtt-fase*
*Context gathered: 2026-06-26*
