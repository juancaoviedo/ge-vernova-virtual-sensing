---
status: complete
phase: 10-system-2-streaming-distribution-state-estimator-mqtt-fase
source: [10-SUMMARY.md, 10-VERIFICATION.md, 10-HUMAN-UAT.md]
started: 2026-06-27
updated: 2026-06-27
---

## Current Test

[testing complete]

## Tests

Live end-to-end validation of the streaming pipeline (`docker compose up` → `publish` →
`estimate` → `score`) against the populated Phase-9 `measurements`/`profiles`/oracle buckets.
The structural verification (10-VERIFICATION.md, "12/13") passed unit "scratch" tests on
handcrafted inputs; this UAT exercised the **real MQTT-assembled pipeline** and found it does
not yet produce estimates. Three defects found (1 fixed, 2 open).

### 1. MQTT transport — broker unreachable by host clients (FIXED)
expected: `publish`/`estimate` (host-side paho clients) connect to the broker and exchange
the retained `netmodel/current` + live meas stream.
result: issue (FIXED)
severity: blocker
reported: "publish.py/estimate.py could not connect — every paho CONNECT was dropped before
CONNACK (broker never logged it); estimate timed out waiting for netmodel; publish silently
transmitted nothing (it never checks publish() return)."
root_cause: `mosquitto.conf` used `listener 1883 127.0.0.1`, binding only the container
loopback (`netstat` inside container: `tcp 127.0.0.1:1883 LISTEN`). Docker's
`127.0.0.1:1883:1883` forward routes host connections via the container **bridge IP**, where
nothing listened. In-container `mosquitto_pub -h 127.0.0.1` worked, masking the defect; the
executors never ran a host→broker round trip.
fix: bind `listener 1883 0.0.0.0` inside the container; localhost-only exposure preserved by
the compose `127.0.0.1:1883:1883` host binding (T-10-01 intact). Verified: host paho now
connects (rc=0), retained publish/read round-trips. Commit `19c0422`.

### 2. FASE predict `S @ delta_p` dimension mismatch — EKF/UKF crash on step 0 (OPEN)
expected: EKF and UKF run predict→update across all 96 day snapshots, producing (x̂,P).
result: issue
severity: blocker
reported: "ValueError: matmul mismatch (size 33 vs 26) at fase_predict.py:158
`x_minus = x_prev + S @ delta_p`."
root_cause: `estimate.py` builds `S = ac_model.fase_sensitivity(x_prev, Ybus, inj_ml, W_inj)`
with columns = number of injection **measurements** in the snapshot (e.g. 26 in well_observed),
but `fase_predict._predict_fase` builds `delta_p` with length `n_bus` (33). `S` (state×inj_meas)
and `delta_p` (per-bus) live in different spaces, so the product mismatches whenever
`len(inj_ml) != n_bus` (essentially always). Secondary smell: `delta_p` is derived from a
single scalar `prof_df.iloc[k]["load_pu"]` scaled by per-bus AR(1) noise, not a true per-bus
injection schedule — the forecast/sensitivity contract needs to be defined in one consistent
per-bus injection space (S = ∂x/∂p_bus, shape state×n_bus; delta_p per-bus).
artifacts: [system1-measurement-source/src/ieee33/fase_predict.py, system1-measurement-source/src/ieee33/estimate.py, system1-measurement-source/src/ieee33/ac_model.py]

### 3. WLS rank-deficient on `well_observed`; state dim 66 ≠ 64 (OPEN)
expected: AC-WLS converges on `well_observed` (R5) and meets < 0.005 pu (R10); writes estimates.
result: issue
severity: blocker
reported: "Every snapshot: `RankDeficientError — G shape=(66,66), rank=33`; estimate skips the
write, so the `estimates` bucket stays empty for WLS."
root_cause: two coupled problems. (a) **State dimension is 66 = 2×33**, inconsistent with
`ac_model`'s declared free dim **64 = 2×32** (verify_model prints `free state dim=64`) — the WLS
state indexing/slack handling includes an extra bus. (b) **Rank 33 of 66** means the assembled
measurement Jacobian constrains only half the states — `well_observed` is supposed to be fully
observable without pseudo padding, so either the snapshot assembler isn't delivering the full
measurement set (power injections/flows that constrain angles) to `h(x)/H`, or H is mis-built.
artifacts: [system1-measurement-source/src/ieee33/estimators.py, system1-measurement-source/src/ieee33/estimate.py, system1-measurement-source/src/ieee33/ac_model.py]

### 4. Downstream numeric acceptance R10/R11/R12 — unverifiable until #2/#3 fixed (BLOCKED)
expected: RMSE < 0.005 pu / dark-node < 0.02 pu; NEES in [61.76,66.28]; fault P-inflation.
result: blocked
blocked_by: prior-phase
reason: "No estimator currently writes to the `estimates` bucket (WLS rank-deficient; EKF/UKF
crash in FASE predict), so `score` has nothing to evaluate. Re-run after #2/#3 are fixed."

## Summary

total: 4
passed: 0
issues: 3
pending: 0
skipped: 0
blocked: 1

## Gaps

```yaml
- truth: "EKF and UKF produce (x̂,P) across all snapshots (R6/R7)"
  status: failed
  reason: "FASE predict S @ delta_p dimension mismatch (S cols = #injection-meas, delta_p = n_bus); crash at fase_predict.py:158 on step 0."
  severity: blocker
  test: 2
  artifacts: [system1-measurement-source/src/ieee33/fase_predict.py, system1-measurement-source/src/ieee33/estimate.py, system1-measurement-source/src/ieee33/ac_model.py]
  missing: ["consistent per-bus injection space for S=∂x/∂p_bus (state×n_bus) and delta_p (n_bus)"]
- truth: "AC-WLS converges and writes estimates on well_observed (R5/R10)"
  status: failed
  reason: "RankDeficientError every step; G shape (66,66) rank 33. State dim 66≠64 (slack/bus-index defect) and only half the states are constrained (measurement assembly or H defect)."
  severity: blocker
  test: 3
  artifacts: [system1-measurement-source/src/ieee33/estimators.py, system1-measurement-source/src/ieee33/estimate.py, system1-measurement-source/src/ieee33/ac_model.py]
  missing: ["state vector sized to 64 free states (2×32, slack excluded)", "full well_observed measurement set assembled into H so G is full-rank without pseudo"]
```
