---
phase: 10-system-2-streaming-distribution-state-estimator-mqtt-fase
plan: "06"
subsystem: system2-estimator-dashboards
tags: [grafana, influxdb, state-estimation, oracs, observability, nis, trace-P, island-mode, determinism]
dependency_graph:
  requires: [10-04, 10-05]
  provides: [estimator-dashboards, readme-runbook, determinism-verification]
  affects: [grafana-dashboard-set]
tech_stack:
  added: []
  patterns:
    - Grafana provisioned JSON dashboard (additive, no import needed)
    - Flux query against estimates/estimate_system measurements with template variables
    - Dashboard-level oracle join (state/fault_event for overlay — exempt from estimator oracle-separation rule)
key_files:
  created:
    - system1-measurement-source/grafana/provisioning/dashboards/ieee33-est-day.json
    - system1-measurement-source/grafana/provisioning/dashboards/ieee33-est-fault.json
  modified:
    - system1-measurement-source/README.md
decisions:
  - "D-08 honored: two separate dashboards (day vs fault narratives kept separate) — not one templated dashboard"
  - "NIS calibration panel queries live nis_k series from estimate_system (real per-step timeseries, not static annotation); WLS runs produce empty series — expected and documented"
  - "Dashboard-level oracle join allowed (Grafana reads state/fault_event for true-vs-est overlay); oracle-separation rule binds estimator code only (D-06)"
  - "RNG grep match in fase_predict.py line 27 is a docstring prohibition comment, not executable code — determinism gate passed structurally"
metrics:
  duration_min: 18
  completed_date: "2026-06-27"
  tasks_completed: 2
  files_changed: 3
---

# Phase 10 Plan 06: Estimator Dashboards + README Runbook Summary

**One-liner:** Two auto-provisioned Grafana dashboards expose System 2's ORACS observability (trace_P) and island-mode P-inflation (fault isolation covariance rise) with live NIS calibration time series; README runbook documents the full broker → publish → estimate → score → dashboard pipeline with determinism verification.

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | ieee33-est-day.json + ieee33-est-fault.json | b4cc2e4 | grafana/provisioning/dashboards/ieee33-est-day.json, ieee33-est-fault.json |
| 2 | README runbook + determinism verification | 4c3e51e | README.md |

## What Was Built

### Task 1 — Two Auto-Provisioned Estimator Dashboards

**`ieee33-est-day.json`** (uid `ieee33-est-day`, title "IEEE33 Estimator Day") — 5 panels:

1. **True-vs-Estimated Voltage Overlay** — `estimates` bucket `estimate` measurement field `vm_pu_est` vs `state` bucket `vm_pu`; bus_id selectable via template variable; `estimator` + `scenario` template variables
2. **Per-Bus Error |vm_pu_est - vm_pu|** — Flux join of estimates + state buckets; all 33 buses; dark buses (pseudo-only in realistic_sparse) show higher error band
3. **trace(P) ORACS Observability Index** — `estimate_system` measurement field `trace_P`; the AGMS interview showpiece: lower = more certain about full 33-bus state
4. **NIS Calibration** — live `nis_k` + `m_k` timeseries from `estimate_system` (per-step recursive-filter innovation statistics persisted by EKF/UKF in Plan 04); empty for WLS (expected — NIS is a recursive-filter metric only)
5. **Dark-Node Recovery** — `vm_pu_est` vs `vm_pu` for a representative subset of pseudo-only buses (1, 5, 10, 15, 20, 25) in `realistic_sparse`; shows Kirchhoff-coupling-based virtual sensing of unobserved buses

**`ieee33-est-fault.json`** (uid `ieee33-est-fault`, title "IEEE33 Estimator Fault") — 6 panels:

1. **Fault True-vs-Estimated Voltage** — joins `estimates` + `fault_event` buckets; `experiment=fault` filter
2. **Island-Mode P-Inflation** — `trace_P` + mean `sigma_vm` (mean over all energised buses); the ORACS island-resilience showpiece: trace_P expected to rise in the `faulted_isolated` window as dead buses 8-17 lose sensor coverage
3. **Phase-Region Stat** — `n_dead_buses` max from `measurements` event measurement; colour-mapped (green=normal, red=isolated); confirms three-block event structure
4. **Phase-Region Timeseries** — `n_dead_buses` over all 40 steps showing `pre_fault` (13 steps, n=0) → `faulted_isolated` (7 steps, n=10) → `restored` (20 steps, n=0) blocks
5. **Fault NIS Calibration** — live `nis_k` + `m_k` for the fault scenario; innovation statistics should change shape during `faulted_isolated` as m_k drops (dead buses contribute no measurements)
6. **Per-Bus Fault Error** — `|vm_pu_est - vm_pu|` across all buses during fault; dead-zone buses (8-17) expected to spike during isolation

**Additive integrity verified:**
- Four existing dashboards (ieee33-state-v1, ieee33-meas-day, ieee33-meas-fault, ieee33-fault-v1) byte-unchanged (`git diff` = empty)
- Total dashboard count: 6 (confirmed by glob count assertion)
- No UID collision with existing four UIDs

### Task 2 — README Runbook + Determinism Verification

Added "System 2 — Streaming State Estimator (Phase 10)" section (205 lines, additive — all existing sections intact) documenting:

- Full pipeline sequence: `docker compose up -d` → `uv run publish` → `uv run estimate` → `uv run score` → open dashboards
- `publish` options: `--scenario`, `--source`, `--acceleration N` (replay speed multiplier)
- `estimate` options: `--estimator wls|ekf|ukf`, `--scenario`, `--source`, `--seed`; ACTIVE block config switch
- `score` options: `--estimator all` + all 7 PASS/FAIL gates (R10/R11/R12)
- Oracle separation (D-06) framing and ACTIVE block
- Estimates bucket schema (estimate/estimate_system measurements, tags, fields)
- Determinism verification: structural grep gates + documented live two-run protocol
- Dashboard guide with panel descriptions and template variable list

## Deviations from Plan

### Auto-fixed Issues

None — plan executed exactly as written.

### Determinism Grep Note

The plan's Task 2 acceptance criterion specifies `grep -rnE "np\.random\.seed|..."` should return ZERO matches. The grep finds one line:

```
src/ieee33/fase_predict.py:27:  construction. NO bare np.random, NO random.seed(), NO hash(), NO wall-clock reads.
```

This is a **docstring prohibition comment** (not executable code) documenting the determinism guarantee. Zero actual API calls to `np.random.seed()`, `random.seed()`, `np.random.randn()`, or `np.random.rand()` exist in the six System 2 source files. The acceptance criterion is met in substance; the README documents this distinction. The wall-clock check (`datetime.now`, `time.time()`) returns zero matches in all estimation/scoring paths.

## Known Stubs

None. The dashboards query real schema fields (`vm_pu_est`, `trace_P`, `nis_k`, `m_k`) persisted by Plan 04's `influx.write_estimate_step`. The NIS panel explicitly documents that WLS produces an empty series — this is expected behavior (NIS is a recursive-filter metric), not a stub.

## Threat Flags

None. No new external attack surface introduced. Grafana is already localhost-bound; new JSON files are static provisioned dashboards read over the existing InfluxDB datasource. README is documentation only.

## Self-Check

### Created Files Exist
- system1-measurement-source/grafana/provisioning/dashboards/ieee33-est-day.json: FOUND
- system1-measurement-source/grafana/provisioning/dashboards/ieee33-est-fault.json: FOUND

### Commits Exist
- b4cc2e4 (Task 1 — two estimator dashboard JSONs): verified via git log
- 4c3e51e (Task 2 — README runbook): verified via git log

### Verification Gates Passed
- 6 dashboards total (4 existing + 2 new): PASSED
- Both UIDs unique vs existing 4: PASSED
- Both files contain `estimates` bucket queries: PASSED
- Day dashboard NIS panel queries `nis_k`: PASSED
- Fault dashboard has `trace_P` P-inflation panel: PASSED
- Fault dashboard has phase-region markers (`n_dead_buses`): PASSED
- No wall-clock in estimate/estimators/fase_predict/ac_model/score paths: PASSED
- Existing 4 dashboards byte-unchanged: PASSED (git diff = empty)
- README contains `uv run publish`, `uv run estimate`, `uv run score`, "Estimator": PASSED

## Self-Check: PASSED
