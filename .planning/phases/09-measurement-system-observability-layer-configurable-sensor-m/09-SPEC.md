# Phase 9: Measurement System (Observability Layer) — Specification

**Created:** 2026-06-24
**Ambiguity score:** 0.17 (gate: ≤ 0.20)
**Requirements:** 12 locked

## Goal

Build a **config-driven measurement layer** that reads System 1's full ground-truth state from
InfluxDB (the 96-step `state` day **or** the 40-step `fault_event` scenario), applies a selectable
**sensor model** (which buses/lines are instrumented, with what measurement class), corrupts it with
selectable **noise**, samples it at the configured **cadence**, and writes the resulting measurement
set — `z` + assumed σ + topology/switch metadata + phase tag — to a **new dedicated `measurements`
InfluxDB bucket** tagged by experiment + scenario, with two provisioned Grafana dashboards of the
observed states. Its purpose is to **manufacture realistic under-observability** (discard
information), producing the inputs the future System 2 estimator must reconstruct from.

## Background

System 1 (`system1-measurement-source/`, Phase 8, verified 7/7) is complete: `config.py` (DG buses,
RPC shunts, tie-lines, OLTC, bands, InfluxDB connection, `PROFILES_BUCKET`/`STATE_BUCKET`),
`network.py` (`build_enhanced_33bus()`), `sim.py` (96-step day → `state` bucket), `influx.py`
(`get_client`/`wait_for_influx`/`ensure_bucket` + the per-entity `write_state_step` D-07 schema:
`bus`/`line`/`sgen`/`system` measurements), a Docker stack (InfluxDB 2.9.1 + Grafana 11.6.15),
`uv` scripts (`ingest`/`sim`/`validate`), and one provisioned dashboard.

Phase 8.1 (in progress; **schema frozen** in `08.1-CONTEXT.md` D-01…D-06) adds the **`fault_event`
bucket**: the same `bus`/`line`/`sgen`/`system` schema (byte-identical) **plus** a new `event`
measurement (`faulted_line_id`, `tie_closed`, `tie_id`, `n_dead_buses`, `dead_buses` comma-string),
an indexed `phase` tag ∈ {`pre_fault`,`faulted_isolated`,`restored`}, and an `energised` 1/0 flag on
`bus`/`line` points (dead entities zero-filled for a continuous before→0→after series).

**Gap:** nothing today reads that ground truth and applies a sensor model. There is no measurement
layer, no `measurements` bucket, no measurement-config, and no measurement dashboards. The primary
deliverable is a new measurement-layer module + runner + config inside `system1-measurement-source/`
that does NOT exist yet. This is the **Measurement System** in Juan's design: System 1 (behaviour) →
**Measurement System (P9)** → System 2 (estimator) → System 3 (self-healing).

## Requirements

1. **Measurement-config (single source of switchable knobs)**: A dedicated measurement
   configuration controls all behaviour without code edits.
   - Current: only System 1's `config.py` exists (physical/infra constants); no measurement config
   - Target: a measurement-config exposes — `scenario` ∈ {`well_observed`,`realistic_sparse`},
     `source` ∈ {`day`(`state`),`fault`(`fault_event`)}, `sampling` ∈ {`snapshot`,`multirate_async`},
     `noise` ∈ {`gaussian`,`gaussian_outliers`,`instrument`}, an integer `seed`, and a
     `true_sigma`/`assumed_sigma` pair (default equal)
   - Acceptance: changing each knob and re-running changes only the corresponding behaviour; running
     all valid combinations produces a populated `measurements` bucket without code changes

2. **Sensor model / measurement-class taxonomy (node-voltage measurement vector)**: Each class emits
   the realistic per-class quantities suited to a node-voltage estimator.
   - Current: no sensor model; System 1 exposes the full true state to all
   - Target: SCADA → bus `P_inj,Q_inj,|V|` (feeder head); μPMU → `|V|,angle`; AMI → `P_inj` (+`Q_inj`)
     at metered loads; DER → `P,Q` at DG/sgen buses; pseudo → `P_inj,Q_inj` (forecast) at unmetered
     loads; zero-injection (virtual) → `P=0,Q=0` at designated buses
   - Acceptance: for a chosen scenario, a query on `measurements` shows each instrumented location
     carrying exactly its class's quantity set (e.g. a μPMU bus has `|V|`+`angle`; an AMI bus has
     `P_inj`; a pseudo bus has `P_inj,Q_inj`), and every measurement point carries `{type, location,
     value, assumed_sigma, class, timestamp}`

3. **Two sensor-placement scenarios (the observability knob)**: `well_observed` and `realistic_sparse`
   are concrete, fixed bus/line assignments with distinct redundancy.
   - Current: no scenarios exist
   - Target: `well_observed` = feeder-head SCADA + DER telemetry + several μPMUs + broad AMI →
     real-measurement redundancy (# real measurements ÷ # node-voltage states) **> 1.0** (observable
     without pseudo); `realistic_sparse` = feeder-head SCADA + DER + 2–3 μPMUs + AMI on ~30 % of loads,
     remaining loads pseudo → real-measurement redundancy **< 1.0** (under-observable), reaching
     **≥ 1.0 only after pseudo padding**
   - Acceptance: the run logs/report show real-measurement redundancy > 1.0 for `well_observed` and
     < 1.0 (real-only) rising to ≥ 1.0 (with pseudo) for `realistic_sparse`; the instrumented bus/line
     sets differ between the two scenarios

4. **Three switchable noise models**: `gaussian`, `gaussian_outliers`, `instrument`, with separable
   true vs assumed σ.
   - Current: no noise model
   - Target: `gaussian` = zero-mean white additive, per-class %σ; `gaussian_outliers` = Gaussian + a
     configurable small fraction of gross errors (large spikes); `instrument` = quantization +
     systematic bias + mild temporal correlation. The σ used to GENERATE noise (`true_sigma`) and the
     σ EMITTED as `assumed_sigma` (System 2's weight) are independently configurable
   - Acceptance: with `seed` fixed, each model produces a statistically distinguishable error
     distribution (e.g. `gaussian_outliers` has heavier tails / a detectable spike fraction;
     `instrument` shows a nonzero mean bias and step-to-step correlation); setting `assumed_sigma` ≠
     `true_sigma` changes only the emitted `assumed_sigma` field, not the noisy `value`

5. **Two sampling modes, both fully functional**: `snapshot` and `multirate_async`.
   - Current: no sampling logic
   - Target: `snapshot` = every instrumented class emits at every ground-truth timestamp (one
     consistent set per step); `multirate_async` = each class emits on a per-class step-multiple
     (decimation of the dataset's native steps), so consumers see a patchwork of differently-aged
     readings. Cadence multiples are config values (defaults — day: μPMU/DER/SCADA every step, AMI
     every 4 steps; fault: μPMU/DER every step, SCADA every 2 steps, AMI sparse)
   - Acceptance: in `snapshot` mode every class appears at all N timestamps; in `multirate_async`
     mode a class with cadence k appears only at every k-th timestamp (verifiable by counting points
     per class), and the set is otherwise identical

6. **Dual data source via one config flip**: the layer reads either the static day or the failure
   scenario.
   - Current: no reader; System 1's `state` and (8.1's) `fault_event` are written but never consumed
   - Target: `source=day` reads the 96-step `state` bucket; `source=fault` reads the 40-step
     `fault_event` bucket; the same sensor/noise/sampling pipeline applies to both
   - Acceptance: `source=day` yields measurements across 96 timestamps; `source=fault` yields
     measurements across 40 timestamps; switching the flag is the only change required

7. **Topology/switch metadata propagation (publish switch state alongside z)**: the failure case
   carries the topology context an estimator needs; dead buses produce no live measurements.
   - Current: System 1's `state` has no switch metadata (topology implicit); 8.1's `fault_event`
     carries `event` + `energised` + `phase`
   - Target: for `source=fault`, the layer reads 8.1's `event`/`energised`/`phase` and **re-publishes**
     into `measurements` the per-snapshot switch/line in-service status, the `phase` tag, and the
     dead-bus set; de-energised buses (`energised=0`) emit **no live sensor measurement** (a real
     sensor on a dead bus reads nothing). For `source=day` the (fixed, known) topology is recorded
   - Acceptance: in a `faulted_isolated` snapshot, `measurements` contains the topology metadata
     (faulted line, tie state, dead-bus set, `phase`) and contains **no** live `bus`/sensor
     measurement for any bus in the dead set; in a `restored` snapshot those buses reappear

8. **Dedicated `measurements` bucket, tagged by experiment + scenario**: output is isolated and
   multi-experiment-safe.
   - Current: only `profiles`/`state` (and 8.1's `fault_event`) buckets exist
   - Target: a new `measurements` bucket (created via `ensure_bucket`) holds measurement points tagged
     by `experiment` (e.g. `day`/`fault`) and `scenario` (`well_observed`/`realistic_sparse`) so
     multiple experiments coexist; `profiles`/`state`/`fault_event` and existing dashboards are
     untouched
   - Acceptance: after runs of ≥2 (experiment × scenario) combinations, all coexist in `measurements`
     distinguishable by tag; a query on `state` still returns the original 96-step day and on
     `fault_event` the 40-step series, both unchanged

9. **Scoring oracle kept separate**: the measurement layer emits inputs only.
   - Current: n/a
   - Target: `measurements` contains only `z` + `assumed_sigma` + topology/phase metadata — **no**
     ground-truth state passthrough and **no** error/accuracy scoring (true state remains in
     `state`/`fault_event` for a later System-2-vs-System-1 comparison built outside this phase)
   - Acceptance: `grep`/schema inspection of the `measurements` writer shows it never writes a
     true-state field nor computes an estimate-vs-truth error metric

10. **Determinism**: identical config + inputs reproduce identical measurements.
    - Current: n/a
    - Target: all randomness is seeded (`seed` in config); no wall-clock/`random()` without seeding
    - Acceptance: two consecutive runs with the same config produce byte-identical measurement values
      (overwrite-in-place, no duplicates); `grep` shows no unseeded `np.random`/`random`/`datetime.now`
      in the noise/sampling paths

11. **Two provisioned Grafana dashboards of observed states**: one per operating regime, auto-loaded.
    - Current: one provisioned dashboard (System 1's 96-step day) exists
    - Target: two new auto-provisioned dashboards over `measurements` — (a) **static full-day**
      observed states; (b) **failure** observed states — each showing the observed measurements
      (true-vs-measured overlay where the true series is available for context) and the
      **observed-vs-pseudo footprint** (which buses are really measured vs pseudo). Existing dashboards
      unchanged
    - Acceptance: Grafana lists the original dashboard(s) **plus** the two new ones; each renders its
      regime's measurements from a clean provisioned start with no manual setup

12. **Runbook + measurement-footprint report**: documented and self-describing.
    - Current: the System 1 README covers only `ingest`/`sim`/`validate`
    - Target: README documents how to run the measurement layer (the new `uv` script) and open its
      dashboards; each run prints a footprint report (count of measurements per class, real-measurement
      redundancy, pseudo count, # observed vs dead buses)
    - Acceptance: following the README from a clean state reproduces a populated `measurements` bucket
      and renders the dashboards; the printed report lists per-class counts + redundancy

## Boundaries

**In scope:**
- A new measurement-layer module + `uv` runner script inside `system1-measurement-source/`
- A measurement-config with the four switchable knobs (scenario / source / sampling / noise) + seed +
  true/assumed σ
- The measurement-class taxonomy (SCADA, μPMU, AMI, DER, zero-injection, pseudo) with node-voltage
  measurement quantities
- Two sensor-placement scenarios (`well_observed`, `realistic_sparse`)
- Three noise models (`gaussian`, `gaussian_outliers`, `instrument`)
- Two sampling modes (`snapshot`, `multirate_async`)
- Reading both `state` (day) and `fault_event` (failure) ground truth
- Topology/switch metadata propagation into the output
- A new `measurements` InfluxDB bucket (tagged by experiment + scenario)
- Two provisioned Grafana dashboards of observed states
- Determinism, README runbook, per-run footprint report

**Out of scope:**
- **System 2 (the state estimator itself)** — later phase; this phase produces only its inputs
- **System 3 (self-healing loop / switch decisions)** — later phase
- **Estimate-vs-truth scoring / accuracy dashboards** — belongs to the System-2 comparison phase
  (scoring oracle deliberately kept separate)
- **Live streaming transport (NATS / MQTT / C37.118-over-UDP)** — optional later afterthought; this
  phase persists to InfluxDB only
- **Any modification to System 1's day, the 8.1 fault scenario physics, or their
  `profiles`/`state`/`fault_event` buckets and existing dashboards** — additive only
- **Branch-current state formulation** — node-voltage chosen; branch-current is awareness-only
- **Observability via Jacobian-rank / covariance computation** — that is a System 2 output; this phase
  only reports a measurement-count redundancy footprint

## Constraints

- **State formulation = node-voltage** (V magnitude + angle); measurement quantities are chosen to
  suit it.
- **Hard schema dependency on Phase 8.1's `fault_event` writer.** This SPEC targets the frozen 8.1
  schema (D-01…D-06: `event` measurement fields, `phase` tag, `energised` flag). Before Phase 9
  *execution*, field names MUST be verified against the **implemented** `fault_event` writer (a rename
  during 8.1 implementation is a one-line reader change).
- Reuse System 1: `influx.py` helpers (`get_client`/`wait_for_influx`/`ensure_bucket`), `config.py`
  pattern, the Docker InfluxDB 2.9.1 + Grafana 11.6.15 stack, `uv`, Python 3.12. New code is additive
  to `system1-measurement-source/`.
- Determinism is mandatory (seeded noise; overwrite-in-place keyed writes).

## Acceptance Criteria

- [ ] A measurement-config exposes scenario / source / sampling / noise / seed / true-σ / assumed-σ;
      every valid combination runs without code edits
- [ ] Each sensor class emits its correct node-voltage quantities; every point carries
      `{type, location, value, assumed_sigma, class, timestamp}`
- [ ] `well_observed` real-measurement redundancy > 1.0; `realistic_sparse` real-only < 1.0 and ≥ 1.0
      after pseudo padding; the two scenarios' instrumented sets differ
- [ ] The three noise models are statistically distinguishable at a fixed seed; `assumed_sigma` is
      independently settable from `true_sigma`
- [ ] `snapshot` emits every class at every timestamp; `multirate_async` emits class-k only every k-th
      timestamp (verifiable by per-class counts)
- [ ] `source=day` produces 96-timestamp output; `source=fault` produces 40-timestamp output; one flag
      switches them
- [ ] For `source=fault`: topology metadata (faulted line, tie state, dead-bus set, `phase`) is in
      `measurements`, and dead-set buses carry no live sensor measurement during isolation
- [ ] The new `measurements` bucket holds ≥2 (experiment × scenario) runs distinguishable by tag;
      `state` and `fault_event` remain unchanged
- [ ] The `measurements` writer never writes true-state nor an estimate-vs-truth error metric
- [ ] Two consecutive same-config runs produce byte-identical measurements; no unseeded randomness in
      noise/sampling paths
- [ ] Grafana shows the original dashboard(s) plus two new auto-provisioned measurement dashboards
      (static day, failure), rendering from a clean start
- [ ] README documents the run + dashboards; each run prints a per-class footprint report with
      redundancy

## Ambiguity Report

| Dimension          | Score | Min  | Status | Notes                                                                 |
|--------------------|-------|------|--------|-----------------------------------------------------------------------|
| Goal Clarity       | 0.88  | 0.75 | ✓      | Layer + 4 knobs + node-voltage measurement vector + output all locked  |
| Boundary Clarity   | 0.88  | 0.70 | ✓      | Same-repo additive; System 2/3, scoring, streaming, branch-current out |
| Constraint Clarity | 0.80  | 0.65 | ✓      | Node-voltage; reuse stack; determinism; 8.1 schema dependency flagged  |
| Acceptance Criteria| 0.70  | 0.70 | ✓      | 12 pass/fail checks; redundancy + per-class counts make them testable  |
| **Ambiguity**      | 0.17  | ≤0.20| ✓      |                                                                       |

Status: ✓ = met minimum, ⚠ = below minimum (planner treats as assumption)

## Interview Log

| Round | Perspective        | Question summary                                   | Decision locked                                                        |
|-------|--------------------|---------------------------------------------------|-----------------------------------------------------------------------|
| —     | Pre-spec design    | State formulation: node-voltage vs branch-current?| **Node-voltage** (matches study material + ORACS, PMU angles, topology change; branch-current awareness-only) |
| —     | Pre-spec design    | Which knobs + presets?                             | scenario {well_observed, realistic_sparse} · source {day, fault} · sampling {snapshot, multirate_async} · noise {gaussian, gaussian_outliers, instrument} |
| —     | Pre-spec design    | Scoring oracle in or out?                          | **Out** — measurement layer emits z+σ+topology only; truth stays in state/fault_event |
| 1     | Researcher         | Where does the layer live?                         | **Same repo** (`system1-measurement-source/`), additive, reuse influx/config/Docker/Grafana |
| 1     | Researcher         | What quantities per sensor class (the z vector)?   | **Rich/realistic per class** (SCADA P/Q/|V|; μPMU |V|+angle; AMI P; DER P/Q; pseudo P/Q; zero-inj P=Q=0) |
| 1     | Researcher         | `multirate_async` semantics across 15-min vs 3-s?  | **Per-class decimation of native steps** (cadence = step-multiples; no wall-clock upsampling) |

---

*Phase: 09-measurement-system-observability-layer-configurable-sensor-m*
*Spec created: 2026-06-24*
*Next step: /gsd-discuss-phase 9 — implementation decisions (exact sensor-bus assignments per scenario, concrete per-class σ values + cadence multiples, measurements schema/field naming, dashboard panels, 8.1 field-name verification)*
