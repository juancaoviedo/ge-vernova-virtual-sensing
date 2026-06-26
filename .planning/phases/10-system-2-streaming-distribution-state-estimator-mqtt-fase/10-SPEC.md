# Phase 10: System 2 — Streaming Distribution State Estimator (MQTT + FASE) — Specification

**Created:** 2026-06-26
**Ambiguity score:** 0.12 (gate: ≤ 0.20)
**Requirements:** 13 locked

## Goal

Reconstruct the full node-voltage state of the enhanced IEEE 33-bus feeder — `x = {|V|, θ}` at
every bus (~64 states: 32 non-slack buses × 2, with bus 0 as the reference) **plus a calibrated
posterior covariance `P`** — from the noisy, sparse Phase-9 `measurements` consumed over an **MQTT
stream**, using three estimators (AC-WLS snapshot baseline, recursive EKF, recursive UKF), scored
against the System 1 / 8.1 ground-truth oracle. Success means: on `well_observed` the median bus
voltage RMSE reaches the SCADA noise floor; on `realistic_sparse` the dark (pseudo-only) nodes are
recovered materially better than the pseudo prior and a flat baseline; the posterior covariance is
statistically calibrated (NEES/NIS in the 95% χ² band); and during the fault scenario the filter
keeps producing estimates with honestly-inflating `P` when a zone goes dark (island-mode).

## Background

The repo's `system1-measurement-source/` package is the multi-system build. System 1 (Phase 8,
`sim.py`) produces the 96-step `state` bucket; Phase 8.1 (`fault_sim.py`) produces the 40-step
`fault_event` bucket; Phase 9 (`measure.py` + `measure_config.py`) produces the **`measurements`
bucket** — `meas` points carrying `{value (= true+noise), assumed_sigma}` fields and
`{class, quantity, location, scenario, experiment, phase}` tags, plus `event` points re-publishing
fault topology. The measurement schema (`build_meas_point` / `build_event_point` in `influx.py`) is
locked; noise is real (gaussian / gaussian_outliers / instrument, per-class σ); there is **no
`true_value` field** (oracle deliberately kept separate).

**Gap:** nothing that *estimates* state exists. Confirmed by scout — no MQTT/`paho`, no `Ybus`
extraction, no WLS/EKF/UKF, no `estimates` bucket, no scoring harness, no estimator dashboards. The
only estimation-adjacent code is `dc_powerflow_baddata_demo.py`, a linear **DC teaching demo** (not
the AC estimator). `network.py::build_enhanced_33bus()` builds the pandapower net from which `Ybus`
is extractable (post-`runpp` / `pd2ppc`); the docker-compose stack runs InfluxDB 2.9.1 + Grafana
11.6.15 (localhost-bound); pyproject scripts are `ingest/sim/validate/fault-sim/measure`. System 2
is entirely net-new, **additive** to `system1-measurement-source/`. This is the third stage of the
design: System 1 → Measurement System (P9) → **System 2 (estimator, P10)** → System 3 (later).

## Requirements

1. **MQTT broker in the local stack**: A Mosquitto broker runs alongside InfluxDB + Grafana.
   - Current: docker-compose has only `influxdb` and `grafana` services (localhost-bound)
   - Target: an `eclipse-mosquitto` service is added to `docker-compose.yml`, bound to `127.0.0.1`
     only, started by `docker compose up`; existing services and their config are unchanged
   - Acceptance: `docker compose up -d` starts a reachable MQTT broker on a localhost port; a test
     client can publish and subscribe; the InfluxDB/Grafana services and ports are untouched

2. **Replay publisher (InfluxDB → MQTT)**: A runner streams the stored measurements as MQTT messages.
   - Current: measurements exist only at rest in the `measurements` bucket; nothing publishes them
   - Target: a `publish` script reads the `meas` + `event` points for a chosen `(scenario, source)`
     from InfluxDB, **ordered deterministically** (by timestamp, then class, then bus id), and
     publishes each as an MQTT message (JSON payload carrying `value, assumed_sigma, class, quantity,
     location, experiment, scenario, phase, timestamp`) to a documented topic hierarchy; supports a
     configurable **acceleration factor** (wall-clock playback compression) for both `day` (96) and
     `fault` (40) sources
   - Acceptance: running `publish` for `(realistic_sparse, day)` emits exactly the number of `meas`
     messages present in the bucket for that tag set across 96 timestamps, in the fixed order, plus
     one `event` message per snapshot; switching `--source fault` streams the 40-step series

3. **AC measurement model (`h(x)`, `H`, `Ybus`)**: The estimator's measurement function embeds the
   AC power flow.
   - Current: no `Ybus` extraction and no measurement function exist
   - Target: a module builds `Ybus` and topology from `build_enhanced_33bus()` (parameters/topology
     are known side-information — no parameter estimation), and implements `h(x)` rows per class —
     `P_inj, Q_inj = f(V, θ, Ybus)` for scada/ami/der/pseudo/zero_inj; identity pickoffs for μPMU
     `vm_pu`/`va_degree` — plus the analytic Jacobian `H`; for `source=fault` it rebuilds `Ybus`
     from the published `event` topology (faulted line out, tie closed) per phase
   - Acceptance: evaluating `h(x_true)` at the oracle state reproduces the per-class measured
     quantities to within numerical tolerance (< 1e-6 for voltage pickoffs; injection residuals
     consistent with the known measurement noise, not model error); the Jacobian matches a
     finite-difference check to < 1e-5; a faulted-phase `Ybus` excludes the faulted line and
     includes the closed tie

4. **MQTT subscriber + snapshot assembler**: The estimator consumes the live stream.
   - Current: no subscriber exists
   - Target: an `estimate` runner subscribes to the broker, assembles each arriving measurement into
     the per-snapshot `z` vector, `R = diag(assumed_sigma²)`, and topology context (using the `event`
     message), and drives the estimators on arrival; in `multirate_async` data it processes whatever
     classes arrived at each step (patchwork), not a frozen full set
   - Acceptance: with `publish` running, the `estimate` runner receives and processes every published
     `meas`/`event` message (count matches), and produces a state estimate per snapshot for both
     `snapshot` and `multirate_async` sampling

5. **AC-WLS snapshot baseline (with bad-data detection)**: A per-timestamp Gauss-Newton estimator.
   - Current: only a linear DC demo exists (`dc_powerflow_baddata_demo.py`)
   - Target: an AC-WLS estimator solves each snapshot independently (form `G = HᵀWH`, Gauss-Newton
     iterate), with χ²/largest-normalized-residual bad-data detection; on `realistic_sparse`
     real-only it **reports the singular/rank-deficient gain matrix** and becomes solvable only after
     pseudo padding; on `gaussian_outliers` it flags injected gross errors
   - Acceptance: WLS converges on `well_observed`; on `realistic_sparse` real-measurements-only the
     run detects and reports rank deficiency (does not silently return garbage) and converges with
     pseudo padding; on `gaussian_outliers` the χ²/LNR test flags ≥1 of the injected ±15σ spikes

6. **Recursive EKF estimator (FASE)**: A recursive filter with a forecast-driven predict step.
   - Current: no recursive estimator exists
   - Target: an EKF runs predict (state propagated by the **profile-as-noisy-forecast** prior with
     process noise `Q` derived from forecast error — NOT perfect foresight) then update-on-arrival
     using `h(x)`/`H`; multirate-aware (uses only arrived classes' rows each step); carries `(x̂, P)`
     across snapshots
   - Acceptance: the EKF produces `(x̂, P)` for every snapshot of a full `day` run; its `well_observed`
     accuracy meets R10; `P` is finite and positive-definite at every step

7. **Recursive UKF estimator (FASE)**: A sigma-point filter behind the same predict/update interface.
   - Current: none
   - Target: a (square-root) UKF using the same forecast-driven predict and `h(x)` update, no
     Jacobian; pluggable behind the same interface as the EKF so they are directly comparable
   - Acceptance: the UKF produces `(x̂, P)` for a full `day` run; meets R10 on `well_observed`; on
     `realistic_sparse` the UKF's dark-node accuracy is **no worse than** the EKF's (robustness in the
     low-observability regime)

8. **`estimates` output bucket**: Estimator output is persisted with uncertainty.
   - Current: no `estimates` bucket exists
   - Target: a new `estimates` InfluxDB bucket (via `ensure_bucket`) holds per-snapshot per-bus
     `vm_pu_est`, `va_degree_est`, `sigma_vm`, `sigma_va`, and a system-level `trace_P`
     (= ORACS observability index), tagged by `scenario`, `experiment`, and `estimator`
     (`wls`|`ekf`|`ukf`); `state`/`fault_event`/`measurements`/`profiles` buckets are untouched
   - Acceptance: after runs of all three estimators on `(realistic_sparse, day)`, a query on
     `estimates` returns per-bus estimate+σ series distinguishable by the `estimator` tag; the four
     pre-existing buckets are unchanged

9. **Scoring harness (oracle kept separate)**: Estimate accuracy and calibration are measured.
   - Current: no scoring exists
   - Target: a separate `score` runner joins `estimates` against the `state`/`fault_event` oracle and
     computes — per-bus |V| and angle RMSE; worst-case error at dark/pseudo buses; the
     error-vs-observability comparison (`well_observed` vs `realistic_sparse`); a flat-start /
     pseudo-only baseline error; and covariance calibration (time-averaged NEES on the state and NIS
     on innovations vs the χ² acceptance band) — printing a report and (optionally) writing metrics.
     The **estimators themselves never read the oracle buckets** (only `measurements`/MQTT)
   - Acceptance: `grep`/inspection shows the estimator code never reads `state`/`fault_event`; the
     `score` report prints per-bus RMSE, dark-node error, baseline error, and NEES/NIS verdicts

10. **Accuracy acceptance thresholds (tiered, falsifiable)**: Numeric success bars vs the oracle.
    - Current: no estimator, no thresholds
    - Target: judged on the `day` source with `gaussian` noise (and `assumed_sigma_scale = 1.0`):
      - `well_observed`: median over buses of per-bus voltage RMSE **< 0.005 pu** (SCADA |V| floor),
        and median per-bus angle RMSE **< 0.1°**
      - `realistic_sparse`: at the dark (pseudo-only) buses, voltage RMSE **< 0.02 pu** AND
        **≤ 50%** of the flat/pseudo-only baseline voltage RMSE at those same buses
    - Acceptance: the `score` report shows all four thresholds met for the UKF (and the WLS/EKF
      `well_observed` voltage RMSE also < 0.005 pu); a threshold miss is reported as FAIL, not hidden

11. **Covariance calibration acceptance**: The reported uncertainty is statistically honest.
    - Current: none
    - Target: on `(well_observed, day, gaussian, assumed_sigma_scale=1.0)`, the recursive filters'
      time-averaged NEES lies within the two-sided 95% χ² bounds for the state dimension, and the
      per-step NIS lies within its 95% χ² band for **≥ 90%** of update steps
    - Acceptance: the `score` report prints the NEES average with its 95% bounds (PASS/FAIL) and the
      fraction of steps with in-band NIS (PASS if ≥ 90%)

12. **Two regimes incl. fault island-mode**: Both operating regimes are demonstrated.
    - Current: nothing consumes the fault scenario for estimation
    - Target: all three estimators run on `source=fault`; the estimator reads the published `event`
      topology, rebuilds `Ybus` per phase, emits **no state for de-energised buses** during
      `faulted_isolated`, and the mean posterior σ_V over the surviving observable region **increases
      from `pre_fault` to `faulted_isolated`** (P inflates) and recovers in `restored`; the filter
      produces an estimate every step with no crash/gap
    - Acceptance: the `score`/report shows σ_V (or `trace_P`) higher in `faulted_isolated` than
      `pre_fault`; every energised bus has an estimate at every fault step; `restored`-block voltage
      RMSE returns to within the `well_observed`/day-equivalent bar for the energised buses

13. **Determinism, dashboards, runbook**: Reproducible, visible, documented.
    - Current: none
    - Target: (a) **determinism** — with a fixed config (scenario/source/seed/acceleration) and the
      publisher's fixed emission order, two runs of a given estimator produce reproducible estimates
      (identical, or within 1e-9 tolerance from float ordering); no unseeded `random`/`np.random`/
      wall-clock in estimator/scoring paths; (b) **Grafana** — auto-provisioned dashboard(s) over
      `estimates` showing true-vs-estimated voltage overlay, per-bus error, and `trace_P`
      (observability index) incl. fault inflation, additive to existing dashboards; (c) **README** —
      documents the broker, `publish`/`estimate`/`score` runners, and how to open the dashboards
    - Acceptance: two consecutive same-config runs yield reproducible `estimates`; `grep` finds no
      unseeded randomness/wall-clock in System 2 paths; Grafana lists the existing dashboards **plus**
      the new estimator dashboard(s) rendering from a clean provisioned start; following the README
      from a clean checkout reproduces an `estimates` bucket and the dashboards

## Boundaries

**In scope:**
- Mosquitto broker added to the docker-compose stack (localhost-bound, additive)
- `publish` replay runner: `measurements` bucket → MQTT, deterministic order, accelerable, day+fault
- AC measurement model (`Ybus`, `h(x)` per class, analytic Jacobian `H`) from `build_enhanced_33bus()`
- `estimate` runner: MQTT subscriber + snapshot assembler driving the estimators on arrival
- Three estimators: AC-WLS snapshot (χ²/LNR), recursive EKF, recursive UKF — all behind one interface
- FASE predict step = profile-as-noisy-forecast (honest prior + `Q`), update-on-arrival, multirate-aware
- `estimates` InfluxDB bucket: `(x̂, P)` per bus + `trace_P`, tagged scenario/experiment/estimator
- Separate `score` harness: RMSE, dark-node error, baseline comparison, NEES/NIS calibration
- Both regimes (day observability story + fault island-mode covariance inflation), both scenarios
- Determinism, auto-provisioned Grafana estimator dashboard(s), README runbook
- New `uv` scripts (e.g. `publish`, `estimate`, `score`)

**Out of scope:**
- **System 3** (self-healing / FLISR loop, CaCSM volt/VAR dispatch, simulate-before-commit actuation)
  — later phase; this phase only *senses* state, it does not *act* on it
- **Three-phase unbalanced state** — ground truth is balanced positive-sequence; 3-phase is a talking
  point, not this build
- **Branch-current (BCSE) formulation** — node-voltage is locked; branch-current is awareness-only
- **Federated / multi-area DSSE** (boundary-state exchange, ADMM/consensus) — single-cell estimator
  only; federation is a later/talking-point concern
- **Non-MQTT transports** (real C37.118-over-UDP, NATS, IEEE 2030.5) — MQTT only
- **LinDistFlow linear-KF** as a deliverable — full AC is the chosen model; LinDistFlow is
  awareness-only
- **Parameter / topology estimation** — `Ybus` and connectivity are known inputs, not estimated
- **Any modification** to System 1 / 8.1 / Phase 9 code, physics, buckets, or dashboards — additive only

## Constraints

- **State formulation = node-voltage polar** (`|V|, θ`), bus 0 as slack reference (θ₀ = 0, |V₀| from
  SCADA/regulated); ~64 free states.
- **Measurement model = full AC via `Ybus`** built from `build_enhanced_33bus()`; the power flow lives
  **inside** `h(x)` (one coupled network-wide estimator, not a per-signal filter bank in front of a
  power flow).
- **Estimators never read the oracle** (`state`/`fault_event`); they consume only `measurements` (via
  MQTT). The `score` harness is the only component that reads both.
- **Determinism** is mandatory: seeded + deterministic publisher emission order → reproducible
  estimates (identical or within 1e-9); no unseeded `random`/`np.random`/wall-clock in System 2 paths.
- **Reuse** the existing stack: `uv`, Python 3.12, Docker InfluxDB 2.9.1 + Grafana 11.6.15; add
  Mosquitto; new code is additive to `system1-measurement-source/`. New deps pinned (`paho-mqtt`,
  reuse `pandapower`/`numpy`/`influxdb-client`).
- Acceptance thresholds (R10/R11) are judged on the `day` source with `gaussian` noise and
  `assumed_sigma_scale = 1.0` unless a requirement states otherwise; the separable `assumed_sigma`
  knob enables later mis-specified-noise robustness study (out of scope to gate here).

## Acceptance Criteria

- [ ] `docker compose up -d` starts a localhost-bound Mosquitto broker; InfluxDB/Grafana untouched
- [ ] `publish` streams the exact `meas`+`event` message counts for a `(scenario, source)` in fixed
      deterministic order; supports an acceleration factor and both `day` (96) and `fault` (40)
- [ ] AC measurement model: `h(x_true)` reproduces voltage pickoffs to < 1e-6 and the Jacobian
      matches finite-difference to < 1e-5; faulted-phase `Ybus` excludes the faulted line, includes
      the closed tie
- [ ] `estimate` runner consumes every published message (count matches) and produces a per-snapshot
      estimate for both `snapshot` and `multirate_async`
- [ ] AC-WLS converges on `well_observed`; reports rank deficiency on `realistic_sparse` real-only and
      converges with pseudo; flags ≥1 injected ±15σ spike under `gaussian_outliers`
- [ ] EKF and UKF each produce finite, positive-definite `(x̂, P)` for every snapshot of a full day run
- [ ] `well_observed`: median bus voltage RMSE < 0.005 pu and median angle RMSE < 0.1° (UKF; WLS/EKF
      also < 0.005 pu voltage)
- [ ] `realistic_sparse`: dark-node voltage RMSE < 0.02 pu AND ≤ 50% of the flat/pseudo-only baseline
- [ ] Covariance calibration: time-averaged NEES within 95% χ² bounds; NIS in-band for ≥ 90% of steps
- [ ] Fault: σ_V / `trace_P` higher in `faulted_isolated` than `pre_fault`; no estimate for dead buses
      during isolation; every energised bus estimated every step; `restored` RMSE back within bar
- [ ] Estimator code never reads `state`/`fault_event` (grep-verified); `score` prints RMSE + dark-node
      + baseline + NEES/NIS verdicts
- [ ] `estimates` bucket holds all three estimators' output distinguishable by tag; the four existing
      buckets unchanged
- [ ] Two consecutive same-config runs produce reproducible estimates; no unseeded randomness/wall-clock
      in System 2 paths
- [ ] Grafana shows existing dashboards plus the new estimator dashboard(s) (true-vs-est, error,
      `trace_P`) from a clean provisioned start; README reproduces the bucket + dashboards from clean

## Ambiguity Report

| Dimension          | Score | Min  | Status | Notes                                                                 |
|--------------------|-------|------|--------|-----------------------------------------------------------------------|
| Goal Clarity       | 0.90  | 0.75 | ✓      | Recreate node-voltage (x̂,P) from MQTT; WLS+EKF+UKF; AC Ybus; numeric bar |
| Boundary Clarity   | 0.92  | 0.70 | ✓      | System 3 / 3-phase / branch-current / federation / non-MQTT explicitly out |
| Constraint Clarity | 0.82  | 0.65 | ✓      | Node-voltage; AC h(x); oracle separation; ordered determinism; reuse stack |
| Acceptance Criteria| 0.85  | 0.70 | ✓      | Tiered RMSE + NEES/NIS calibration + all-3 estimators + live MQTT, falsifiable |
| **Ambiguity**      | 0.12  | ≤0.20| ✓      |                                                                       |

Status: ✓ = met minimum, ⚠ = below minimum (planner treats as assumption)

## Interview Log

| Round | Perspective              | Question summary                                  | Decision locked                                                              |
|-------|--------------------------|---------------------------------------------------|------------------------------------------------------------------------------|
| —     | Pre-spec design (D1–D6)  | Estimator family / model / transport / predict?   | WLS→recursive; full AC via Ybus; MQTT replay; profile-as-noisy-forecast; oracle separate; estimates bucket (locked in ROADMAP) |
| 1     | Researcher + Simplifier  | What numeric bar = "recreates the state"?         | **Tiered + calibration**: well_observed |V| RMSE < 0.005 pu; realistic_sparse dark-node < 0.02 pu & ≤ 50% of baseline; NEES/NIS in 95% χ² band |
| 1     | Simplifier               | Which estimators are acceptance-required?         | **All three** (WLS + EKF + UKF) implemented and scored — full three-way comparison |
| 1     | Boundary Keeper          | MQTT "done" bar + determinism under async?        | **Live replay** (estimator consumes MQTT, accelerable) + **ordered determinism** (fixed publish order + seed → reproducible) |

---

*Phase: 10-system-2-streaming-distribution-state-estimator-mqtt-fase*
*Spec created: 2026-06-26*
*Next step: /gsd-discuss-phase 10 — implementation decisions (topic schema, Ybus extraction method, predict-step Q model, sigma-point params, dashboard panels, script layout)*
