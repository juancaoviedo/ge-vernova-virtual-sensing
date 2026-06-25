# Phase 9: Measurement System (Observability Layer) - Context

**Gathered:** 2026-06-25
**Status:** Ready for planning

<domain>
## Phase Boundary

A **config-driven measurement layer** added to `system1-measurement-source/` that reads System 1 /
8.1 ground-truth state from InfluxDB (the 96-step `state` day **or** the 40-step `fault_event`
scenario), applies a selectable **sensor model** (placement + measurement class), corrupts it with
selectable **noise**, samples it at the configured **cadence**, and writes `z` + assumed σ +
topology/phase metadata to a new **`measurements`** bucket (tagged by experiment + scenario), with
two provisioned Grafana dashboards. It **manufactures realistic under-observability** — the inputs
the future System 2 estimator reconstructs from. State formulation target = **node-voltage**.

</domain>

<spec_lock>
## Requirements (locked via SPEC.md)

**12 requirements are locked.** See `09-SPEC.md` for full requirements, boundaries, and acceptance criteria.

Downstream agents MUST read `09-SPEC.md` before planning or implementing. Requirements are not duplicated here.

**In scope (from SPEC.md):** new measurement-layer module + `uv` runner inside `system1-measurement-source/`;
measurement-config (scenario / source / sampling / noise + seed + true/assumed σ); measurement-class
taxonomy (SCADA, μPMU, AMI, DER, zero-injection, pseudo) with node-voltage quantities; two placement
scenarios (`well_observed`, `realistic_sparse`); three noise models (`gaussian`, `gaussian_outliers`,
`instrument`); two sampling modes (`snapshot`, `multirate_async`); reading both `state` and
`fault_event`; topology/switch metadata propagation; new `measurements` bucket (tagged by experiment +
scenario); two provisioned Grafana dashboards; determinism, README runbook, per-run footprint report.

**Out of scope (from SPEC.md):** System 2 (estimator); System 3 (self-healing); estimate-vs-truth
scoring/accuracy dashboards; live streaming transport (NATS/MQTT/C37.118-over-UDP); any change to
System 1's day, the 8.1 fault physics, or their `profiles`/`state`/`fault_event` buckets and existing
dashboards; branch-current formulation; Jacobian-rank/covariance observability computation.

</spec_lock>

<decisions>
## Implementation Decisions

### 8.1 schema verification (the hard dependency — RESOLVED)
- **D-01:** The implemented `write_fault_step` ([influx.py:345](../../../system1-measurement-source/src/ieee33/influx.py))
  **matches the frozen 8.1 design with zero meaningful drift.** Confirmed real contract: bucket
  `fault_event`; `bus`/`line`/`sgen`/`system` byte-identical to `state`; `event` measurement with tag
  `phase` and fields `faulted_line_id`, `tie_closed`, `tie_id` (int, **−1 when open**), `n_dead_buses`,
  `dead_buses` (comma-joined sorted string). Fault line idx **7**, dead buses **8–17**, restore tie
  **34** (selected, no fallback). Phase tags: `pre_fault` / `faulted_isolated` / `restored`. Window 40
  steps (13/7/20), 3 s, anchored at evening-peak step 72.
- **D-02:** **`energised` is an InfluxDB TAG** (string `"1"`/`"0"`) on `bus`/`line`/`sgen` points — NOT
  a field. Dead-zone entities are **present-but-zero-filled every snapshot** (vm_pu=0, va_degree=0,
  p/q=0, energised=`"0"`), not absent. Phase 9 reader determines observability from this tag.
- **D-03:** During isolation the measurement layer emits **NO live sensor measurement** for any
  `energised="0"` entity (a sensor on a dead bus reads nothing) — and **no pseudo-measurement** for a
  dead bus (its load is 0/de-energised). The dead-zone's only presence in `measurements` is via the
  re-published topology event. (Note: bus 17 = a μPMU candidate AND a DG sgen, sits *inside* the dead
  zone, so it goes dark during isolation — a realistic, deliberate stress on System 2.)

### Sensor-bus assignments per scenario (the observability knob)
*(pandapower 0-indexed: bus 0 = feeder-head/substation LV bus, no load; loads on buses 1–32; DG sgens
at 17/21/24/32; RPC shunts at 17/32. Planner finalizes exact membership — these are the locked intent
+ the redundancy targets that govern them. States counted as 2·(N_energised−1): slack |V|+angle known.)*
- **D-04 — `realistic_sparse` (headline, redundancy borderline):**
  - SCADA: bus 0 → `P_inj, Q_inj, |V|`
  - μPMU: buses {17, 24, 30} → `|V|, angle` (17 inside dead zone → lost in fault; 24 at a wind DG; 30 healthy lateral)
  - DER telemetry: buses {17, 21, 24, 32} → `P, Q`
  - AMI (~30% of loads, ~10 buses): {3, 6, 9, 12, 15, 18, 21, 24, 28, 31} → `P_inj`
  - pseudo: every remaining load bus not covered above → `P_inj, Q_inj` (large σ)
  - Target: **real-only redundancy < 1.0** (under-observable); **≥ 1.0 only after pseudo padding**
- **D-05 — `well_observed` (redundancy > 1.0 without pseudo):**
  - SCADA: bus 0 → `P_inj, Q_inj, |V|`
  - μPMU: buses {0, 4, 8, 13, 17, 21, 24, 28, 32} (9) → `|V|, angle`
  - DER telemetry: {17, 21, 24, 32} → `P, Q`
  - AMI (~80% of loads): all load buses except a small held-out set → `P_inj` (+`Q_inj`)
  - zero-injection (virtual): designate ~2 junction buses (e.g. {2, 19}) → `P=0, Q=0` (very high weight)
  - Target: **real-measurement redundancy > 1.0** (observable without pseudo)

### `measurements` bucket schema (forward contract for System 2)
- **D-06:** One **generic `meas` measurement point per sensor reading**. Tags: `class`
  ∈ {scada,pmu,ami,der,pseudo,zero_inj}; `quantity` ∈ {vm_pu,va_degree,p_inj_mw,q_inj_mvar,p_mw,q_mvar};
  `location` (bus or line id); `scenario` ∈ {well_observed,realistic_sparse}; `experiment`
  ∈ {day,fault}; plus `phase` (fault only). Fields: `value` (noisy reading) and `assumed_sigma`.
  **No `true_value` field** (scoring oracle stays separate per SPEC R9).
- **D-07:** Topology is re-published per snapshot into the **same `event` measurement name** used by
  8.1 (tag `phase`; fields `faulted_line_id`, `tie_closed`, `tie_id`, `n_dead_buses`, `dead_buses`),
  additionally tagged `scenario`/`experiment`, so System 2 reads `z` and topology from one bucket. For
  `experiment=day` the event records the fixed/known topology (no fault, all ties open).

### Config + module structure
- **D-08:** New modules in `src/ieee33/`: `measure.py` (runner) + `measure_config.py` (named scenario
  dicts, noise profiles, sampling cadences, and an `ACTIVE` selection block). New `[project.scripts]`
  entry `measure = "ieee33.measure:main"` → `uv run measure`.
- **D-09:** **Config file is the primary switch** (per user emphasis): edit `measure_config.py`'s
  `ACTIVE` block to set scenario/source/sampling/noise/seed. **Also** accept CLI overrides
  (`--scenario --source --sampling --noise --seed`) defaulting to the config values, to enable
  experiment sweeps without editing the file.
- **D-10:** Reuse `influx.get_client/wait_for_influx/ensure_bucket`; new bucket `measurements` created
  via `ensure_bucket`. Read ground truth from `state` (day) / `fault_event` (fault) with Flux pivot
  queries mirroring `read_profiles`'s pattern. Deterministic overwrite-in-place (measurement+tags+ts).

### Noise parameters (defaults; all tunable in config; true σ = assumed σ by default)
- **D-11 — per-class σ (fraction of measured value unless noted):** SCADA |V| 0.005 / P,Q 0.02;
  μPMU |V| 0.001 / angle 0.0003 rad; AMI P(,Q) 0.03; DER P,Q 0.015; pseudo P,Q **0.30**;
  zero-injection 1e-4 (near-exact).
- **D-12 — `gaussian_outliers`:** base Gaussian + gross errors on a fraction `f=0.03` of measurements,
  spike magnitude ≈ 15·σ with random sign (exercises bad-data detection / Phase-2 χ² machinery).
- **D-13 — `instrument`:** per-class quantization (LSB), a fixed per-sensor systematic bias
  (~+0.5% of value, seed-derived so it's reproducible), and AR(1) temporal correlation (ρ≈0.7) on the
  random term. Non-catastrophic but non-ideal; shows graceful degradation.

### Sampling cadences (multirate = per-class decimation of native steps)
- **D-14:** `snapshot` = every class at every timestamp. `multirate_async` defaults — **day** (96×15min):
  μPMU/DER/SCADA every step, AMI every 4 steps (hourly); pseudo every step (forecast always available).
  **fault** (40×3s): μPMU/DER every step, SCADA every 2 steps, AMI every 10 steps; pseudo every step.

### Footprint report + redundancy
- **D-15:** Each run prints a per-class measurement count, the pseudo count, observed-vs-dead bus
  counts, and **redundancy = total_measurements ÷ (2·(N_energised−1))** (real-only and with-pseudo).
  This is a measurement-count footprint only — Jacobian/covariance observability is System 2's job.

### Dashboards
- **D-16:** Two auto-provisioned dashboards over `measurements` (additive to the existing two):
  `ieee33-meas-day.json` and `ieee33-meas-fault.json`. Panels: observed bus-voltage measurements
  (with the true `state`/`fault_event` series overlaid for visual context), the observed-vs-pseudo
  footprint (which buses are really measured vs pseudo), per-class measurement counts, and — for the
  fault dashboard — a phase-region marker + dead-bus count. Existing System 1 / 8.1 dashboards untouched.

### Claude's Discretion
- Exact AMI/μPMU bus membership within the stated targets, exact ACTIVE-block field names, Flux query
  details, dashboard panel layout, and the precise quantization LSBs are planner/executor details
  within the locked intent above.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Phase 9 spec (locked)
- `.planning/phases/09-measurement-system-observability-layer-configurable-sensor-m/09-SPEC.md` — 12 locked requirements, boundaries, acceptance criteria. MUST read before planning.

### Phase 8.1 forward contract (the data this phase consumes)
- `system1-measurement-source/src/ieee33/influx.py` §`write_fault_step` (≈L345-527) — the REAL `fault_event` schema (bus/line/sgen/system + `event` + `energised` tag). The reader MUST match these exact measurement/tag/field names.
- `system1-measurement-source/src/ieee33/config.py` — `FAULT_*` constants (FAULT_LINE_IDX=7, FAULT_DEAD_BUS_IDX=8..17, FAULT_TIE_IDX=34, FAULT_PHASE_*), `FAULT_EVENT_BUCKET="fault_event"`, `STATE_BUCKET="state"`, DG/RPC/tie/OLTC consts, InfluxDB connection.
- `.planning/phases/08.1-system-1-fault-and-reconfiguration-scenario/08.1-CONTEXT.md` — 8.1 design decisions D-01..D-18 (schema rationale, zero-fill, energised flag).

### System 1 code to reuse
- `system1-measurement-source/src/ieee33/influx.py` — `get_client`, `wait_for_influx`, `ensure_bucket`, `read_profiles` (Flux pivot pattern), `write_state_step` (the per-entity `state` schema to read).
- `system1-measurement-source/src/ieee33/sim.py` / `fault_sim.py` — runner + console-table + determinism patterns to mirror (do NOT modify).
- `system1-measurement-source/pyproject.toml` — `[project.scripts]` (add `measure`); deps.
- `system1-measurement-source/grafana/provisioning/dashboards/default.yml` + `ieee33-state.json` + `ieee33-fault-event.json` — auto-provisioning pattern + dashboards to leave unchanged (add two new JSONs).
- `system1-measurement-source/docker-compose.yml` — InfluxDB 2.9.1 + Grafana 11.6.15 stack.

### Study-material grounding (measurement-class taxonomy / DSSE)
- `.planning/phases/02-distribution-virtual-sensing/` notes — DSSE side-information taxonomy, pseudo-measurements, χ²/normalized-residual bad-data test (the `gaussian_outliers` story), observability framing.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `influx.get_client` / `wait_for_influx` / `ensure_bucket` — connection + new-bucket creation, reuse as-is.
- `influx.read_profiles` — Flux pivot → DataFrame pattern to copy for reading `state`/`fault_event`.
- `config.py` constants — feeder-head bus, DG/RPC buses, fault constants, bucket names, InfluxDB conn.
- `sim.py` / `fault_sim.py` — deterministic per-step runner + console footprint table + overwrite-in-place write pattern.

### Established Patterns
- **Article-N = pandapower idx N-1** (0-indexed) — keep for any bus/line references.
- Per-entity InfluxDB schema with string tags; deterministic overwrite-in-place (measurement+tags+ts).
- `uv` project, Python 3.12, `[project.scripts]` entry points; Docker InfluxDB+Grafana auto-provisioning.
- Seeded determinism is a hard project norm (sim.py/fault_sim.py both deterministic).

### Integration Points
- New `measure.py` + `measure_config.py` modules; new `measure` script; new `measurements` bucket; two
  new Grafana JSONs. All additive — System 1's day, the 8.1 fault scenario, and their buckets/dashboards
  are untouched (verifiable by `git`/`grep`).

</code_context>

<specifics>
## Specific Ideas

- User's headline framing: the measurement layer must support BOTH operating regimes via one config
  flip (static `day` ↔ `fault`) — the SAME sensor/noise/sampling pipeline applies to both.
- User wants the noise model genuinely switchable to study its effect on estimation — hence three
  models, with `gaussian_outliers` explicitly tied to bad-data detection.
- Streaming (NATS / C37.118-over-UDP) is an explicit afterthought: "we will just read from Influx" —
  build InfluxDB persistence now; a streaming adapter can sit on top later without touching the sensor
  model.
- Interview tie (light): this layer is the AGMS perception edge — Inspector scouts streaming
  observations as POV frames to the estimator.

</specifics>

<deferred>
## Deferred Ideas

- **Live streaming transport** (NATS / MQTT / C37.118-over-UDP) reading from the `measurements` bucket
  and feeding System 2 — explicitly later/optional (SPEC out-of-scope).
- **System 2 (state estimator)** and the **estimate-vs-truth comparison dashboard** — the next phases.
- **Jacobian-rank / covariance-based observability index** (ORACS observability) — a System 2 output,
  not this phase's footprint report.

</deferred>

---

*Phase: 09-measurement-system-observability-layer-configurable-sensor-m*
*Context gathered: 2026-06-25*
