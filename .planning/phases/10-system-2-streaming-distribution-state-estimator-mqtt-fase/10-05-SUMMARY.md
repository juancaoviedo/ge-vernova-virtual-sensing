---
phase: 10-system-2-streaming-distribution-state-estimator-mqtt-fase
plan: "05"
subsystem: system2-scoring
tags: [scoring, oracle-separation, nees, nis, rmse, fault-analysis, influxdb, pandas]
dependency_graph:
  requires: [10-04]
  provides: [score-script, read_estimates-helper, read_estimate_system-helper]
  affects: [pyproject.toml-score-entry]
tech_stack:
  added: []
  patterns:
    - scipy.stats.chi2.ppf for NEES/NIS band derivation (not hardcoded)
    - faithful NIS via persisted nis_k/m_k (no diagonal-sigma proxy)
    - oracle separation boundary enforced by module import structure
key_files:
  created:
    - system1-measurement-source/src/ieee33/score.py
  modified:
    - system1-measurement-source/src/ieee33/influx.py
decisions:
  - WLS NIS reported as N/A — snapshot estimator has no innovation sequence
  - NEES band derived via chi2.ppf not hardcoded — self-documenting assertion
  - Dark-node baseline = flat-start 1.0 pu oracle RMSE (worst-case bound)
  - Diagonal-P approximation for NEES (only diagonal sigma persisted in InfluxDB)
  - Fault metrics gated on has_fault_data flag — gracefully skipped for day source
metrics:
  duration_min: 7
  completed_date: "2026-06-26"
  tasks_completed: 2
  files_modified: 2
---

# Phase 10 Plan 05: Scoring Harness Summary

**One-liner:** Oracle-separated PASS/FAIL scoring harness (RMSE + NEES + per-step NIS from persisted nis_k/m_k + fault inflation) with non-zero exit on any threshold miss.

## What Was Built

### Task 1: influx.read_estimates + read_estimate_system (additive)

Two new reader helpers added to `/system1-measurement-source/src/ieee33/influx.py`:

- **`read_estimates(client, scenario, experiment, estimator)`** — reads the `estimates` bucket, measurement `"estimate"`, filtered by scenario/experiment/estimator. `bus_id` in Flux `rowKey` (it is a TAG — mirrors `read_fault_bus` Pitfall 5 guard). Returns DataFrame sorted by `(_time, bus_id)` with fields `vm_pu_est`, `va_degree_est`, `sigma_vm`, `sigma_va`.

- **`read_estimate_system(client, scenario, experiment, estimator)`** — reads measurement `"estimate_system"`, filtered by scenario/experiment/estimator. Returns per-step `trace_P` plus `nis_k` / `m_k` when present (recursive EKF/UKF filters). Robust to `nis_k`/`m_k` absence for WLS runs — those columns appear as NaN rather than raising.

No existing influx.py helper was modified.

### Task 2: score.py — Oracle join + RMSE + NEES/NIS + fault, non-zero exit on FAIL

New file `/system1-measurement-source/src/ieee33/score.py` (994 lines):

**Oracle separation:** score.py is the SOLE component that calls `read_state_bus`/`read_fault_bus`. Grep across `estimate.py`, `estimators.py`, `fase_predict.py`, `ac_model.py` returns zero oracle reads (R9 enforced).

**CLI:** `--scenario`, `--source`, `--estimator {wls,ekf,ukf,all}` (default "all").

**R10 — RMSE gates:**
- Per-bus voltage |V| RMSE and angle RMSE computed via oracle join on `(_time, bus_id)`.
- Median over buses reported with `PASS` (< 0.005 pu voltage, < 0.1° angle) or `FAIL`.
- Dark-node (pseudo-only bus) RMSE reported with `PASS` (< 0.02 pu) or `FAIL`.
- Dark vs flat-start baseline ratio reported with `PASS` (<= 50%) or `FAIL`.
- Dark buses identified from `measure_config.SCENARIOS` — no InfluxDB read needed.

**R11 — Covariance calibration:**
- **NEES:** time-averaged NEES vs 95% chi² band computed via `scipy.stats.chi2.ppf` (NOT hardcoded). For n=64, N=96: band [61.76, 66.28] confirmed. P approximated as diagonal from persisted `sigma_vm`/`sigma_va` (only diagonal stored in InfluxDB).
- **NIS (faithful path):** reads persisted `nis_k`/`m_k` from `read_estimate_system`. Per-step chi²(m_k) band via `chi2.ppf([0.025, 0.975], m_k)`. In-band fraction PASS if >= 90%. WLS reports N/A (snapshot estimator — no innovation sequence, no nis_k persisted).

**R12 — Fault analysis:**
- Partitions steps by phase (`pre_fault`, `faulted_isolated`, `restored`) via `read_fault_event`.
- `sigma_V` (mean sigma_vm over energised buses) and `trace_P` both checked to be higher in `faulted_isolated` than `pre_fault` → PASS.
- Restored block RMSE (energised buses only, Pitfall 5: energised is STRING "1") checked < 0.005 pu → PASS.

**Fail-loud gate:** any threshold miss prints the failing metrics and `sys.exit(1)` (falsifiable).

**Multi-estimator comparison block:** when `--estimator all`, scores wls+ekf+ukf and prints a side-by-side comparison table; NIS column shows N/A for wls.

## Verification Results

### Live verification (automated gate checks):

```
read_estimates + read_estimate_system OK
read_estimate_system reads nis_k/m_k series
score.py structure OK
NEES band [61.76,66.28] matches [61.76,66.28]
per-step NIS band chi2(m=8) = [2.18,17.53] computed via chi2.ppf([0.025,0.975],m_k)
ORACLE SEPARATION OK — only score.py reads oracle
NEES band in score.py: [61.76,66.28] PASS
Dark buses (realistic_sparse): 19 buses
Dark buses (well_observed): 5 buses
All structural checks PASS
```

### Live vs structural validation

All verification was **structural** (no live InfluxDB data consumed) because the upstream data pipeline (measure → publish → estimate) was not re-run in this session. The score.py harness was validated for:

- Correct imports and function signatures
- NEES band derivation via scipy.stats.chi2.ppf (not hardcoded)
- Per-step NIS band computation via chi2.ppf([0.025,0.975], m_k)
- Oracle separation (grep zero oracle refs in estimator modules)
- Dark bus set derivation from measure_config.SCENARIOS
- All threshold logic and PASS/FAIL paths (unit-level function calls)
- `sys.exit(1)` on FAIL (code path verified by AST walk)

**NOT validated live:** actual RMSE/NEES/NIS numeric thresholds against real estimate data — those require the full pipeline (ingest → sim → measure → publish → estimate → score) to be running end-to-end. Document any actual run results as deferred: run `uv run score --estimator all` after `uv run estimate` populates the estimates bucket.

## Deviations from Plan

None — plan executed exactly as written. The additive constraint on influx.py was honored: zero existing helpers modified.

## Known Stubs

None — score.py reads faithfully from InfluxDB; no hardcoded placeholder data.

## Threat Flags

None — score.py is a local read-only consumer of local InfluxDB buckets. No new network surface introduced.

## Self-Check: PASSED

Files created:
- `/home/juan/codes/ge-vernova-virtual-sensing/system1-measurement-source/src/ieee33/score.py` — FOUND
- `/home/juan/codes/ge-vernova-virtual-sensing/.planning/phases/10-system-2-streaming-distribution-state-estimator-mqtt-fase/10-05-SUMMARY.md` — FOUND (this file)

Commits:
- `5fe91cf` feat(10-05): add read_estimates + read_estimate_system helpers to influx.py — FOUND
- `0d059d6` feat(10-05): add score.py — oracle join + RMSE + NEES/NIS + fault scoring harness — FOUND
