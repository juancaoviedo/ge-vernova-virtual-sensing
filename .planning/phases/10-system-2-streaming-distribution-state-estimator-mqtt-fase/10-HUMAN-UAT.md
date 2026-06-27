---
status: partial
phase: 10-system-2-streaming-distribution-state-estimator-mqtt-fase
source: [10-VERIFICATION.md]
started: 2026-06-26
updated: 2026-06-26
---

## Current Test

[awaiting live end-to-end pipeline run]

## Tests

These three acceptance bars are wired and structurally verified in `score.py`, but their
numeric values require a live `docker compose up` → `publish` → `estimate` (×3) → `score`
run against the Phase-9 `measurements` data. Run sequence (from `system1-measurement-source/`):

```bash
docker compose up -d                      # InfluxDB + Grafana + Mosquitto (localhost-bound)
# Ensure Phase-9 measurements exist in InfluxDB (if not: uv run sim / fault-sim / measure first)
uv run publish  --scenario realistic_sparse --source day                    # terminal A (replay)
uv run estimate --scenario realistic_sparse --source day --estimator ukf    # terminal B (and ekf, wls)
uv run estimate --scenario realistic_sparse --source day --estimator ekf
uv run estimate --scenario realistic_sparse --source day --estimator wls
uv run score    --scenario realistic_sparse --source day --estimator all    # prints PASS/FAIL, exits non-zero on miss
# Repeat publish/estimate/score with --source fault for R12.
```

### 1. R10 — accuracy thresholds (live numeric values)
expected: `well_observed` median per-bus voltage RMSE < 0.005 pu AND median angle RMSE < 0.1°;
`realistic_sparse` dark-node (pseudo-only) voltage RMSE < 0.02 pu AND ≤ 50% of the flat/pseudo-only
baseline. `score` reports each PASS/FAIL and exits non-zero on any miss.
result: [pending live run]

### 2. R11 — covariance calibration (NEES/NIS, live)
expected: time-averaged NEES inside the 95% χ² band [61.76, 66.28] (n=64, N=96); per-step NIS
in-band fraction ≥ 90% (recursive filters EKF/UKF; WLS reports N/A). NIS read from the faithful
persisted `nis_k`/`m_k` series. (Note: NEES uses a documented diagonal-P approximation — a lower
bound — accepted to avoid full-P InfluxDB write overhead.)
result: [pending live run]

### 3. R12 — fault island-mode P-inflation (live, --source fault)
expected: mean σ_V / `trace_P` higher in `faulted_isolated` than `pre_fault`; no estimate emitted for
de-energised buses 8–17 during isolation; every energised bus estimated every step; `restored`-block
RMSE returns within the `well_observed` bar across the 3 `config_version` transitions.
result: [pending live run]

## Summary

total: 3
passed: 0
issues: 0
pending: 3
skipped: 0
blocked: 0

## Gaps
