---
phase: 09-measurement-system-observability-layer-configurable-sensor-m
verified: 2026-06-25T00:00:00Z
status: human_needed
score: 21/21 must-haves verified
overrides_applied: 0
human_verification:
  - test: "Open Grafana at http://localhost:3000. Confirm four dashboards are listed: 'IEEE33 DER State — 2017-06-07 High-DER DE Day', 'IEEE 33-Bus — Fault & Reconfiguration', 'IEEE 33-Bus Observed Measurements — Day', and 'IEEE 33-Bus Observed Measurements — Fault'."
    expected: "All four dashboards appear in the Grafana home/search list. No manual import required."
    why_human: "Grafana panel rendering (auto-provisioning pickup, visible panel content) cannot be confirmed programmatically — only JSON parse validity was machine-verifiable."
  - test: "Open 'IEEE 33-Bus Observed Measurements — Day'. Verify: (a) the observed bus-voltage time-series renders across all 96 steps, (b) the true state series from the 'state' bucket is overlaid for visual comparison, (c) the per-class measurement counts stat panel shows non-zero counts for scada/pmu/ami/der/pseudo, (d) the observed-vs-pseudo footprint panel shows which buses are real vs pseudo."
    expected: "All four panel types render with data. No 'No data' placeholders."
    why_human: "Panel rendering against live InfluxDB data with correct Flux queries requires browser verification."
  - test: "Open 'IEEE 33-Bus Observed Measurements — Fault'. Verify: (a) observed voltages across 40 steps render with a μPMU-bus-17 dropout visible during the isolation window, (b) the dead-bus-count panel rises to 10 during faulted_isolated, (c) the phase marker panel distinguishes pre_fault / faulted_isolated / restored regions, (d) the observed-vs-pseudo footprint changes at isolation onset."
    expected: "All five panel types render with data. Bus 17 dropout is visible in the voltage panel."
    why_human: "Temporal gap visibility (bus 17 dropout during isolation) requires visual inspection in a browser."
---

# Phase 9: Measurement System (Observability Layer) Verification Report

**Phase Goal:** A config-driven measurement layer in system1-measurement-source/ that reads System 1 / 8.1 ground truth from InfluxDB (the 96-step `state` day OR the 40-step `fault_event` scenario), applies a selectable sensor model (placement + measurement class) + selectable noise + configured sampling cadence, and writes z + assumed σ + topology/phase metadata to a new `measurements` bucket (tagged by experiment + scenario), with two provisioned Grafana dashboards. Node-voltage formulation; scoring oracle kept separate; streaming out of scope.

**Verified:** 2026-06-25T00:00:00Z
**Status:** human_needed
**Re-verification:** No — initial verification

## Goal Achievement

### Observable Truths

All truths verified against the actual codebase and confirmed by live behavioral spot-checks (Docker stack was up, measurements bucket populated).

| #  | Truth | Status | Evidence |
|----|-------|--------|----------|
| 1  | D-04: realistic_sparse SCADA bus 0 / μPMU {17,24,30} / DER {17,21,24,32} / AMI {3,6,9,12,15,18,21,24,28,31} / pseudo=rest declared in measure_config.SCENARIOS | VERIFIED | `uv run python -c "from ieee33 import measure_config as mc; assert mc.SCENARIOS['realistic_sparse']['pmu']==[17,24,30]"` → passes |
| 2  | D-05: well_observed SCADA bus 0 / μPMU {0,4,8,13,17,21,24,28,32} / DER {17,21,24,32} / AMI ~80% load buses / zero_inj {2,19} declared in measure_config.SCENARIOS | VERIFIED | `assert mc.SCENARIOS['well_observed']['zero_inj']==[2,19]` and `assert 0 in mc.SCENARIOS['well_observed']['pmu']` → passes |
| 3  | D-06: meas-point tag/field contract (class/quantity/location/scenario/experiment/phase; value+assumed_sigma; no true_value) documented in measure_config; quantity vocabulary enumerated | VERIFIED | `grep -q "no.*true_value\|true_value.*field\|scoring" measure_config.py` → oracle sep documented; MEAS_QUANTITIES defined |
| 4  | D-08: measure_config.py exists in src/ieee33/ with CLASS_SIGMA, CADENCE, SCENARIOS, ACTIVE; 274 lines | VERIFIED | File exists; `wc -l` = 274; all required blocks present |
| 5  | D-09: ACTIVE block is the primary switch with keys scenario/source/sampling/noise/seed/assumed_sigma_scale | VERIFIED | `assert mc.ACTIVE['scenario'] in ('well_observed','realistic_sparse')` → passes; all six keys confirmed |
| 6  | D-11: per-class sigma table matches SCADA |V|0.005 P,Q 0.02 / μPMU |V|0.001 angle 0.0003 / AMI 0.03 / DER 0.015 / pseudo 0.30 / zero_inj 1e-4 | VERIFIED | `assert mc.CLASS_SIGMA['pseudo']['p_inj_mw']==0.30 and mc.CLASS_SIGMA['pmu']['va_degree']==0.0003` → passes |
| 7  | D-14: CADENCE table declares day {ami:4, rest:1} and fault {scada:2, ami:10, rest:1} | VERIFIED | `assert mc.CADENCE['day']['ami']==4 and mc.CADENCE['fault']['ami']==10 and mc.CADENCE['fault']['scada']==2` → passes |
| 8  | D-01: fault_event reader matches write_fault_step contract — bucket fault_event, event measurement with tag phase and fields faulted_line_id/tie_closed/tie_id/n_dead_buses/dead_buses | VERIFIED | `read_fault_event` present in influx.py; queries `_measurement=="event"` with `phase` in pivot rowKey |
| 9  | D-02: fault bus reader places energised TAG in Flux pivot rowKey so it returns as string column compared as == '1' | VERIFIED | `grep 'rowKey.*energised' influx.py` → 2 matches; code comment: "compare energised == '1' as a STRING" |
| 10 | D-06: write_meas helper writes Point('meas') with tags class/quantity/location/scenario/experiment(+phase) and fields value+assumed_sigma ONLY — never a true_value field | VERIFIED | `grep '\.field.*true_value' influx.py` → no output; line-protocol assertion prints `writers OK` |
| 11 | D-07: event re-publisher writes Point('event') into measurements bucket adding scenario+experiment tags; tie_id always cast int | VERIFIED | `grep 'tie_id.*int(' influx.py` → line 874; `build_event_point` confirmed |
| 12 | D-10: new helpers reuse get_client/wait_for_influx/ensure_bucket; measurements bucket created via ensure_bucket | VERIFIED | `influx.ensure_bucket(client, mc.MEASUREMENTS_BUCKET)` at measure.py line 654 |
| 13 | D-02: runner reads energised tag as string, builds live/dead bus sets from energised == '1' | VERIFIED | measure.py line 725-730: `live_bus_ids = {bus_id for (si, bus_id), eng in energised_by_step_bus.items() if si == step_idx and eng == "1"}` |
| 14 | D-03: during faulted_isolated no live sensor measurement AND no pseudo-measurement for any energised='0' bus (bus 17 dark) | VERIFIED | measure.py line 768-770: `if bus_id in dead_bus_ids: continue`; live run confirms "Dead buses (fault ISO): 10 ([8..17])" |
| 15 | D-04/D-05: scenario sensor placement sourced from measure_config.SCENARIOS | VERIFIED | `grep -n "SCENARIOS\[" measure.py` → line 605; runner reads `scenario_def = mc.SCENARIOS[cfg["scenario"]]` |
| 16 | D-08/D-10: measure.py exists with main() entry point; reads ground truth via Plan-02 Flux readers | VERIFIED | `grep -c "def _parse_args\|def _merge_cfg\|def _build_day_lookup\|def _build_fault_lookup\|def get_true_value\|def main\|def run" measure.py` = 6; scaffold OK |
| 17 | D-12: gaussian_outliers adds gross error on fraction f=0.03 with magnitude ~15·σ | VERIFIED | `assert 'OUTLIER_FRACTION' in src and 'OUTLIER_SPIKE_MULT' in src`; noise OK assertion passes |
| 18 | D-13: instrument applies per-sensor seed-derived bias (~+0.5%), quantization to per-class LSB, AR(1) (ρ≈0.7); CR-02 (hashlib) and CR-03 (zero_inj absolute sigma) both fixed | VERIFIED | hashlib.sha256 at line 112; zero_inj absolute sigma gate at line 792; instrument quantization confirmed: `assert abs(round(q/lsb)*lsb - q) < 1e-9` passes |
| 19 | D-14: multirate_async decimates per class — confirmed by live run: AMI count 480 vs snapshot 1920 (= 96/4 × 10 buses × 2 quantities) | VERIFIED | Live `uv run measure --sampling multirate_async` output: ami=480 (= snapshot 1920 / cadence 4) |
| 20 | D-15: each run prints per-class counts, pseudo count, observed-vs-dead bus counts, redundancy = total ÷ (2·(N_energised−1)) real-only and with-pseudo | VERIFIED | Live output shows full footprint report; well_observed real-only = 1.047 (>1.0); realistic_sparse real-only = 0.578 (<1.0), with-pseudo = 1.172 (≥1.0) — all three SPEC R3 gates pass |
| 21 | D-16: two auto-provisioned dashboards ieee33-meas-day.json and ieee33-meas-fault.json with correct UIDs, 4 distinct total UIDs, measurements bucket referenced, n_dead_buses in fault dashboard | VERIFIED | `d['uid']=='ieee33-meas-day'`, `f['uid']=='ieee33-meas-fault'`, `len(uids)==4`, `'n_dead_buses' in json.dumps(f)` → all pass; existing dashboards byte-unchanged (git diff = empty) |

**Score:** 21/21 truths verified

### Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| `system1-measurement-source/src/ieee33/measure_config.py` | Pure-constants module with CLASS_SIGMA, CADENCE, SCENARIOS, ACTIVE, QUANT_LSB | VERIFIED | 274 lines; all blocks present; 47 D-NN decision citations |
| `system1-measurement-source/pyproject.toml` | `measure = "ieee33.measure:main"` entry point registered | VERIFIED | `tomllib` parse confirms 5 scripts including measure |
| `system1-measurement-source/src/ieee33/influx.py` | 5 Flux readers + 3 writer helpers added (additive) | VERIFIED | `grep -c "def read_state_bus\|def read_state_sgen\|def read_fault_bus\|def read_fault_sgen\|def read_fault_event"` = 5; 3 writers present |
| `system1-measurement-source/src/ieee33/measure.py` | 985-line runner with main(), apply_noise, InstrumentState, topology re-publish, footprint report | VERIFIED | 985 lines; all Plan 03+04 acceptance commands pass |
| `system1-measurement-source/grafana/provisioning/dashboards/ieee33-meas-day.json` | Day observed-states dashboard (uid ieee33-meas-day) | VERIFIED | `d['uid']=='ieee33-meas-day'`, id=None, references measurements bucket and ieee33-influxdb |
| `system1-measurement-source/grafana/provisioning/dashboards/ieee33-meas-fault.json` | Fault observed-states dashboard (uid ieee33-meas-fault) | VERIFIED | `f['uid']=='ieee33-meas-fault'`, id=None, references n_dead_buses and measurements bucket |
| `system1-measurement-source/tests/test_measure_determinism.py` | 6 tests — 3 static + 3 Docker-guarded integration | VERIFIED | 6 `def test_` functions; `_influx_available` skip guard present; all 52 tests pass (11.66s) |
| `system1-measurement-source/README.md` | Measurement-layer runbook section | VERIFIED | Contains `uv run measure`, `measure_config`, `ieee33-meas-day` / dashboard names |

### Key Link Verification

| From | To | Via | Status | Details |
|------|----|-----|--------|---------|
| `pyproject.toml [project.scripts]` | `ieee33.measure:main` | `uv run measure` | WIRED | Script entry confirmed by tomllib parse |
| `influx.read_fault_bus` | `fault_event bucket bus` | Flux pivot with energised in rowKey | WIRED | Line 657: `pivot(rowKey: ["_time", "bus_id", "energised"], ...)` |
| `influx.write_meas_points` | `measurements bucket` | `write_api.write bucket=MEASUREMENTS_BUCKET` | WIRED | `write_meas_points(..., bucket=str)` at influx.py line 881 |
| `measure.main` | `influx.read_state_bus / read_fault_bus` | source=day\|fault branch | WIRED | Lines 298 (day), 427 (fault) |
| `measure sensor loop` | `measure_config.SCENARIOS` | per-class bus assignment lookup | WIRED | `scenario_def = mc.SCENARIOS[cfg["scenario"]]` at line 605 |
| `measure energised gate` | `dead-bus skip` | `energised == '1'` check | WIRED | Lines 727-732 build live_bus_ids; line 769 `if bus_id in dead_bus_ids: continue` |
| `measure noise dispatch` | `gaussian / gaussian_outliers / instrument` | `cfg['noise']` branch in apply_noise | WIRED | `apply_noise` dispatches on noise_model argument; all three branches confirmed |
| `measure cadence gate` | `measure_config.CADENCE` | `step_idx % cadence` | WIRED | Line 762: `step_idx % mc.CADENCE[experiment][cls] != 0` |
| `measure topology re-publish` | `measurements event measurement` | `influx.build_event_point` | WIRED | Lines 859 (fault) and 872 (day steady_state) |
| `ieee33-meas-day.json panel` | `measurements bucket meas points` | Flux filter _measurement==meas | WIRED | "measurements" in json.dumps(d) = True; 14 references to ieee33-influxdb datasource |
| `test_measure_determinism` | `measurements bucket values` | two-run byte-identical compare | WIRED | test_determinism function present and Docker-guarded; 52 tests pass |

### Data-Flow Trace (Level 4)

| Artifact | Data Variable | Source | Produces Real Data | Status |
|----------|---------------|--------|--------------------|--------|
| `measure.py` | `lookup` (true values per bus/step) | `influx.read_state_bus` + `read_state_sgen` + `read_profiles` (day) OR `influx.read_fault_bus` + `read_fault_sgen` (fault) | Yes — Flux pivot queries against live InfluxDB; RuntimeError raised if bucket empty | FLOWING |
| `measure.py` | `points` (meas Point list) | true_val from lookup → apply_noise → build_meas_point | Yes — seeded noise applied to real ground-truth; live run produced 7200 pts (day snapshot) | FLOWING |
| `ieee33-meas-day.json` | observed voltages panel | Flux query against `measurements` bucket; experiment=="day", quantity=="vm_pu" | Yes — confirmed by live run populating the bucket | FLOWING (machine-confirmed; visual rendering is human item) |
| `ieee33-meas-fault.json` | dead-bus-count panel | Flux query on `event` measurement field `n_dead_buses`, experiment=="fault" | Yes — live fault run wrote 2846 pts including event re-publish per snapshot | FLOWING (machine-confirmed; visual rendering is human item) |

### Behavioral Spot-Checks

| Behavior | Command | Result | Status |
|----------|---------|--------|--------|
| realistic_sparse/day real-only redundancy < 1.0 | `uv run measure --scenario realistic_sparse --source day --sampling snapshot --noise gaussian` | Real-only redundancy: 0.578; With-pseudo: 1.172 | PASS |
| well_observed/day real-only redundancy > 1.0 | `uv run measure --scenario well_observed --source day --sampling snapshot --noise gaussian` | Real-only redundancy: 1.047; 7776 pts written | PASS |
| fault source produces 40-step output, dead buses [8..17] | `uv run measure --scenario realistic_sparse --source fault --sampling snapshot --noise gaussian` | 40 steps confirmed (scada=120/3/1=40); Dead buses: 10 ([8..17]) | PASS |
| multirate_async AMI decimation (cadence 4) | `uv run measure --scenario realistic_sparse --source day --sampling multirate_async --noise gaussian` | ami=480 = 1920/4 (vs snapshot) | PASS |
| noise OK (gaussian near-true; instrument on LSB grid) | `uv run python -c "apply_noise('gaussian',...)"` | abs(v-1.0)<0.1; abs(round(q/lsb)*lsb-q)<1e-9 | PASS |
| 52 tests pass | `uv run python -m pytest tests/ -q` | 52 passed, 6 warnings in 11.66s | PASS |
| 3 static tests pass (no Docker needed) | `pytest tests/test_measure_determinism.py::test_no_unseeded_randomness ...` | 3 passed in 0.31s | PASS |

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|-------------|------------|-------------|--------|----------|
| R1 (measurement-config) | Plan 01 | Config exposes all knobs; any valid combination runs | SATISFIED | ACTIVE dict with 6 keys; all CLI overrides wired; live runs confirm multiple combos work |
| R2 (sensor-class taxonomy) | Plan 01+03 | Each class emits correct node-voltage quantities; every point has {type,location,value,assumed_sigma,class,timestamp} | SATISFIED | CLASS_SIGMA keys confirmed per class; build_meas_point wires all fields; no true_value |
| R3 (two scenarios) | Plan 01+03+04 | well_observed real > 1.0; realistic_sparse real < 1.0, ≥ 1.0 with pseudo | SATISFIED | Live runs: well_observed 1.047; realistic_sparse 0.578 / 1.172 |
| R4 (three noise models) | Plan 04 | gaussian/gaussian_outliers/instrument statistically distinguishable; assumed_sigma independent | SATISFIED | apply_noise dispatches all 3; InstrumentState + hashlib bias; quantization confirmed |
| R5 (two sampling modes) | Plan 04 | snapshot emits every class every step; multirate_async per-class decimation | SATISFIED | multirate AMI=480 vs snapshot AMI=1920; cadence gate at line 762 |
| R6 (dual data source) | Plan 02+03 | source=day → 96 timestamps; source=fault → 40 timestamps; one flag switches | SATISFIED | Confirmed by spot-checks and arithmetic from counts |
| R7 (topology metadata) | Plan 03+04 | fault: event fields re-published; dead buses emit no live measurement; restored buses reappear | SATISFIED | build_event_point called per-snapshot; energised gate excludes dead buses; dead_buses=[8..17] in report |
| R8 (measurements bucket) | Plan 02+03 | Dedicated measurements bucket; multi-experiment coexistence; source buckets untouched | SATISFIED | ensure_bucket(client, mc.MEASUREMENTS_BUCKET) called; no write to STATE_BUCKET/FAULT_EVENT_BUCKET in measure.py |
| R9 (oracle separation) | Plan 02+04 | No true_value field in measurements; no estimate-vs-truth error metric | SATISFIED | `grep '\.field.*true_value' influx.py measure.py` → no output; test_no_true_value_field passes |
| R10 (determinism) | Plan 04+05 | Same config → byte-identical values; no unseeded randomness | SATISFIED | hashlib.sha256 for bias seed; test_no_unseeded_randomness passes; test_determinism present (Docker-guarded) |
| R11 (two dashboards) | Plan 05 | Grafana shows original dashboards plus two new ones; auto-provisioned from clean start | SATISFIED (machine portion); HUMAN NEEDED (rendering) | 4 distinct UIDs confirmed; JSON parse OK; existing dashboards byte-unchanged; visual rendering needs human |
| R12 (runbook + footprint) | Plan 05 | README documents run + dashboards; each run prints footprint with redundancy | SATISFIED | README has uv run measure / measure_config / dashboard names; live runs print full footprint report |

### Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|------|------|---------|----------|--------|
| None found | — | No TODO/FIXME/placeholder comments, no empty returns, no unseeded randomness, no true_value field writes | — | — |

Note: `get_true_value` function name contains "true_value" but is an internal helper computing the ground-truth scalar for noise application — it does NOT write a true_value InfluxDB field. This is NOT a stub or anti-pattern.

### Human Verification Required

#### 1. Four Grafana Dashboards Visible in UI

**Test:** Navigate to http://localhost:3000 (credentials: admin/admin or anonymous per docker-compose). Open the search/home panel and confirm four dashboards are listed.

**Expected:** Dashboard list contains all four titles: "IEEE33 DER State — 2017-06-07 High-DER DE Day", "IEEE 33-Bus — Fault & Reconfiguration", "IEEE 33-Bus Observed Measurements — Day", "IEEE 33-Bus Observed Measurements — Fault". No manual import required.

**Why human:** Grafana auto-provisioning pickup and title display require browser verification. Machine-verified: both JSON files parse cleanly, UIDs are distinct, the provisioning `default.yml` auto-loads all JSONs in the dashboards/ directory with `updateIntervalSeconds: 30`.

#### 2. Observed Measurements — Day Dashboard Renders Correctly

**Test:** Open "IEEE 33-Bus Observed Measurements — Day". Set time range to 2017-06-07.

**Expected:** (a) Observed bus-voltage time-series renders across all 96 steps. (b) True `state` bucket series is overlaid as reference. (c) Per-class measurement counts stat panel shows non-zero values for scada/pmu/ami/der/pseudo. (d) Observed-vs-pseudo footprint panel distinguishes real vs pseudo buses.

**Why human:** Panel content and overlay rendering require browser inspection. Machine-verified: Flux queries reference `measurements` bucket with `_measurement=="meas"`, and the overlay panel queries the `state` bucket.

#### 3. Observed Measurements — Fault Dashboard Renders with Bus-17 Dropout

**Test:** Open "IEEE 33-Bus Observed Measurements — Fault". Set time range to the 4-minute fault window (2017-06-07T17:59:00Z..2017-06-07T18:03:00Z).

**Expected:** (a) Observed voltages across 40 steps show a visible dropout at μPMU bus 17 during the faulted_isolated window (~steps 13–19). (b) Dead-bus-count panel rises to 10 during isolation. (c) Phase marker distinguishes pre_fault / faulted_isolated / restored. (d) Observed-vs-pseudo footprint changes at isolation onset.

**Why human:** Temporal gap visibility (bus 17 dropout) and phase-region coloring require visual inspection. Machine-verified: dead buses [8..17] confirmed in live fault run; n_dead_buses field present in dashboard JSON.

### Gaps Summary

No blocking gaps. All 21 must-haves are verified and all 12 SPEC acceptance criteria are machine-satisfied. The single remaining item is the RESIDUAL human checkpoint established in Plan 05 Task 3 (checkpoint:human-verify gate:blocking) — visual confirmation that the two new Grafana dashboards render correctly in a browser.

This is explicitly NOT a gap introduced by verification. It was anticipated in the plan design: Plan 05 is marked `autonomous: false` specifically because of this human checkpoint.

---

_Verified: 2026-06-25T00:00:00Z_
_Verifier: Claude (gsd-verifier)_
