---
phase: 09-measurement-system-observability-layer-configurable-sensor-m
reviewed: 2026-06-25T00:00:00Z
depth: standard
files_reviewed: 7
files_reviewed_list:
  - system1-measurement-source/src/ieee33/measure.py
  - system1-measurement-source/src/ieee33/measure_config.py
  - system1-measurement-source/src/ieee33/influx.py
  - system1-measurement-source/tests/test_measure_determinism.py
  - system1-measurement-source/tests/test_noise_models_cadence.py
  - system1-measurement-source/tests/test_event_repub_footprint.py
  - system1-measurement-source/tests/test_influx_readers_writers.py
findings:
  critical: 3
  warning: 3
  info: 2
  total: 8
status: issues_found
---

# Phase 09: Code Review Report

**Reviewed:** 2026-06-25
**Depth:** standard
**Files Reviewed:** 7
**Status:** issues_found

## Summary

The Phase 9 measurement layer is well-structured with clear separation of concerns, solid
documentation, and a thoughtful three-noise-model design. The oracle-separation contract
(no `true_value` in the measurements bucket) holds. The source switch, cadence gate, and
energised-bus gate logic are all correct at the algorithm level.

Three blockers were found:

1. All five Phase 9 InfluxDB reader functions will fail at runtime because the influxdb-client
   `query_data_frame()` returns a `List[DataFrame]` when the Flux query produces multiple tables
   (which it does whenever a tag is in the pivot `rowKey`). The callers in `measure.py` assume
   a single `DataFrame` and immediately call `.sort_values()` on the result.

2. The `_instrument_bias` function uses Python's built-in `hash()` on a string to derive
   per-sensor seeds. Python's hash randomization (`PYTHONHASHSEED`) means this produces
   different values in every new process, breaking the cross-run determinism guarantee that
   is a core SPEC requirement (R10 / D-10). The `test_instrument_bias_deterministic` test
   passes only because it calls the function twice within the same process — it does not
   catch the cross-run failure.

3. The zero-injection class computes `true_sigma = CLASS_SIGMA["zero_inj"][qty] * abs(0.0) = 0.0`
   and writes `assumed_sigma = 0.0` to InfluxDB. Any WLS estimator that divides by sigma
   (or computes weight = 1/sigma²) will divide by zero.

---

## Critical Issues

### CR-01: All Phase 9 Flux readers return `List[DataFrame]` — callers crash with `AttributeError`

**File:** `system1-measurement-source/src/ieee33/influx.py:578` (and lines 614, 661, 700, 741)
**Also:** `system1-measurement-source/src/ieee33/measure.py:291,294,420,423,426`

**Issue:** The influxdb-client `query_data_frame()` returns a `List[DataFrame]` whenever the
Flux response contains more than one table. A Flux `pivot()` operation retains tag columns in
the group key; it does not merge multiple tag-series into a single table. This means:

- `read_state_bus`: 33 distinct `bus_id` tag values → 33 Flux tables → `List[33 DataFrames]`
- `read_state_sgen`: 4 distinct `sgen_id` tag values → `List[4 DataFrames]`
- `read_fault_bus`: `bus_id` × `energised` → multiple groups → `List[DataFrames]`
- `read_fault_sgen`: same pattern with `sgen_id` × `energised`
- `read_fault_event`: 3 distinct `phase` tag values → `List[3 DataFrames]`

Every caller immediately chains `.sort_values(...)` on the return value:

```python
# measure.py line 291 — crashes with AttributeError: 'list' has no attribute 'sort_values'
bus_df = influx.read_state_bus(client).sort_values(["_time", "bus_id"]).reset_index(drop=True)
```

This is confirmed by `_to_data_frames` in the influxdb-client source (`_base.py`):
```python
if len(_dataFrames) == 1:
    return _dataFrames[0]   # single DataFrame
else:
    return _dataFrames       # list — NOT auto-concatenated
```

**Fix:** Each reader must concatenate the list before returning. Since `pandas` is already a
declared dependency (listed in `influx.py` header), add a safe helper and apply it in all five
readers:

```python
# Add near top of influx.py
import pandas as _pd

def _coerce_df(result) -> "_pd.DataFrame":
    """Concat list-of-DataFrames returned by query_data_frame with multiple tables."""
    if isinstance(result, list):
        return _pd.concat(result, ignore_index=True)
    return result
```

Then wrap each reader's return:
```python
# read_state_bus (and all other readers) — apply before returning
df = _coerce_df(client.query_api().query_data_frame(flux))
if df is None or len(df) == 0:
    raise RuntimeError(...)
return df
```

---

### CR-02: `_instrument_bias` uses Python `hash()` — non-deterministic across process restarts

**File:** `system1-measurement-source/src/ieee33/measure.py:107`

**Issue:** Python's `hash()` for string objects is randomized per-process by default since
Python 3.3 (`PYTHONHASHSEED`). Two separate `uv run measure` invocations produce different
`hash(("scada_0_vm_pu", 42))` values, so `_instrument_bias` returns different floats in each
process run. This breaks SPEC R10 / D-10 (determinism: "two consecutive runs with identical
config produce byte-identical InfluxDB values").

Verified empirically:
```
python3 -c "print(hash(('scada_0_vm_pu', 42)) & 0xFFFFFFFF)"  # Run 1: 1034829055
python3 -c "print(hash(('scada_0_vm_pu', 42)) & 0xFFFFFFFF)"  # Run 2: 3066382063
```

The `test_instrument_bias_deterministic` test does NOT catch this because it calls the function
twice within the same Python process, where `hash()` is stable.

**Fix:** Replace `hash()` with a deterministic byte-level hash. `hashlib.sha256` or an integer
accumulation over encoded bytes is the correct approach:

```python
import hashlib

def _instrument_bias(sensor_key: str, seed: int) -> float:
    # Deterministic across processes: SHA-256 on utf-8 bytes + seed bytes
    raw = f"{sensor_key}:{seed}".encode("utf-8")
    digest = int(hashlib.sha256(raw).hexdigest()[:8], 16)  # 32-bit from first 8 hex chars
    bias_rng = np.random.default_rng(digest)
    return bias_rng.normal(0.0, mc.INSTRUMENT_BIAS_SCALE)
```

Also add `import hashlib` at the top of `measure.py`.

---

### CR-03: `zero_inj` class always writes `assumed_sigma = 0.0` — causes divide-by-zero in WLS

**File:** `system1-measurement-source/src/ieee33/measure.py:780-787`

**Issue:** For the `zero_inj` class, `get_true_value` always returns `0.0`. The sigma
computation path (line 785) is:

```python
true_sigma = base_sigma * abs(true_val)   # = CLASS_SIGMA["zero_inj"][qty] * abs(0.0) = 0.0
assumed_sigma = true_sigma * cfg["assumed_sigma_scale"]  # = 0.0
```

`assumed_sigma = 0.0` is then written to the `measurements` bucket. Any WLS estimator
that computes weight `w = 1/sigma²` will divide by zero when it reads a `zero_inj`
measurement. The intent is a "near-exact" high-weight constraint, but a weight of infinity
is numerically destructive.

The comment in `measure_config.py` (CLASS_SIGMA table, line 56) gives `zero_inj` sigma values
of `1e-4`, but these are never used because the fractional scaling multiplies by `abs(0.0)`.

**Fix:** Add a `zero_inj` branch in the sigma computation to use the absolute (not fractional)
CLASS_SIGMA value, analogous to the `pmu.va_degree` special case:

```python
# measure.py lines 781-785 — replace the else branch:
base_sigma = mc.CLASS_SIGMA[cls][quantity]
if cls == "pmu" and quantity == "va_degree":
    true_sigma = base_sigma        # absolute: GPS-disciplined angle
elif cls == "zero_inj":
    true_sigma = base_sigma        # absolute: CLASS_SIGMA["zero_inj"][qty] = 1e-4
else:
    true_sigma = base_sigma * abs(true_val)  # fractional
```

---

## Warnings

### WR-01: Soft redundancy invariant appended to `issues` after the fail-loud gate — never printed

**File:** `system1-measurement-source/src/ieee33/measure.py:887-892,954-962`

**Issue:** The fail-loud gate at line 887 checks `if issues:` and calls `sys.exit(1)`. The
soft redundancy invariant checks (lines 954-962) then call `issues.append(...)`. Since
`sys.exit(1)` is only called when the gate fires (on write errors), the soft issues are
appended AFTER the gate and are never displayed or acted upon. The program prints
"measure OK" even when a wrong-direction redundancy scenario is detected. The `issues.append`
calls on lines 954-962 are effectively dead code.

**Fix:** Print soft invariant issues immediately, or add a second gate after the footprint
report:

```python
# After the footprint report section:
if issues:  # soft invariant violations
    print("\n--- SOFT INVARIANT WARNINGS ---", file=sys.stderr)
    for issue in issues:
        print(f"  {issue}", file=sys.stderr)
```

---

### WR-02: `well_observed` scenario assigns buses 2 and 19 to BOTH `ami` AND `zero_inj`

**File:** `system1-measurement-source/src/ieee33/measure_config.py:195-197`

**Issue:** Buses 2 and 19 appear in both the `ami` list and the `zero_inj` list of
`well_observed`. The result is that the measurements bucket gets two conflicting injection
measurements for each of these buses at every step:

- An AMI reading: `p_inj_mw ≈ actual_load` (noisy, sigma=3%)
- A zero-injection virtual: `p_inj_mw = 0.0` (with `assumed_sigma = 0.0` after CR-03 fix,
  or the present `assumed_sigma = 0.0` before fix)

Bus 2 and 19 in the IEEE 33-bus system are load buses (they carry loads from buses 2 and 19),
so claiming `p_inj = 0` is factually incorrect. A WLS estimator that receives both the AMI
reading and the zero-injection reading will be contradicted: high-weight virtual says zero,
AMI says otherwise.

If the intent is "zero-injection junction buses with no real load", buses 2 and 19 are wrong
choices — they appear in the `ami` list precisely because they have loads. Junction buses in
the IEEE 33-bus topology that have no load (like bus 0) would be more appropriate.

**Fix:** Either remove buses 2 and 19 from the `ami` list in `well_observed`, or choose
actual zero-injection nodes (buses that appear in the network without load entries) for the
`zero_inj` assignment. Cross-check against `net.load["bus"]` after calling
`build_enhanced_33bus()`.

---

### WR-03: `test_dead_bus_gate` can silently false-pass if fault timestamps lie outside the hardcoded query window

**File:** `system1-measurement-source/tests/test_measure_determinism.py:399-453`

**Issue:** The dead-bus gate test queries meas points in the fixed time window
`2017-06-07T17:59:00Z` to `2017-06-07T18:03:00Z`. If the fault scenario's `faulted_isolated`
phase timestamps do not fall within this 4-minute window, the query returns zero rows —
and `count = 0` makes the assertion pass (vacuously). This means the test gives a green
result even if the D-03 energised gate is completely absent from the code.

The test contains no guard assertion that at least one `faulted_isolated` point exists in the
measurements bucket (for non-dead buses) before concluding the gate works for bus 17.

**Fix:** Add a pre-condition assertion that verifies `faulted_isolated` points exist for some
other location (e.g., location="0") in the same time range:

```python
# Pre-condition: verify faulted_isolated points exist in this window (at least 1)
flux_check = (
    'from(bucket: "measurements")\n'
    '  |> range(start: 2017-06-07T17:59:00Z, stop: 2017-06-07T18:03:00Z)\n'
    '  |> filter(fn: (r) => r._measurement == "meas")\n'
    '  |> filter(fn: (r) => r._field == "value")\n'
    '  |> filter(fn: (r) => r.phase == "faulted_isolated")\n'
    '  |> count()'
)
df_check = client.query_api().query_data_frame(flux_check)
total_in_window = int(df_check.iloc[0]["_value"]) if df_check is not None and len(df_check) > 0 else 0
assert total_in_window > 0, (
    "Pre-condition failed: no faulted_isolated meas points found in the query window 17:59-18:03. "
    "The fault scenario may write at different timestamps — update the time range or check the fault sim."
)
```

---

## Info

### IN-01: AR(1) formula in `measure_config.py` docstring disagrees with implementation

**File:** `system1-measurement-source/src/ieee33/measure_config.py:213-215`

**Issue:** The comment for `INSTRUMENT_AR1_RHO` states the recursion as:

```
ε_t = ρ·ε_{t−1} + (1-ρ)·w_t,  where w_t ~ N(0, σ²)
```

This implies the white noise scale is `(1-ρ)·σ = 0.3·σ` for ρ=0.7.

The actual implementation in `InstrumentState.ar1_term` (measure.py line 81) uses:

```python
white = rng.normal(0.0, true_sigma * (1.0 - self.rho ** 2) ** 0.5)
```

which gives scale `√(1-ρ²)·σ ≈ 0.714·σ` — a factor of 2.38× larger. The implementation is
mathematically correct (it preserves the stationary marginal variance at `σ²`); the docstring
is wrong. A reader deriving the noise model from the docstring would get the wrong variance.

**Fix:** Update the docstring to match the implementation:

```python
#   INSTRUMENT_AR1_RHO: AR(1) temporal correlation coefficient ρ.
#     ε_t = ρ·ε_{t−1} + √(1-ρ²)·w_t,  where w_t ~ N(0, σ²).
#     The √(1-ρ²) scaling preserves marginal variance Var(ε_t) = σ².
```

---

### IN-02: Sgen step-index alignment is independent from bus step-index with no cross-validation

**File:** `system1-measurement-source/src/ieee33/measure.py:327-341` (also lines 447-458)

**Issue:** The `sgen_lookup` is built using `step_idx` derived from iterating
`sorted(sgen_df["_time"].unique())`. The `lookup` (bus data) uses `step_idx` from
`sorted(bus_df["_time"].unique())`. These two orderings are independent. If the sgen and bus
data ever have a different number of timestamps (e.g., after a partial resim or partial
re-ingest), the step indices will be misaligned: `sgen_lookup[(3, 17)]` would refer to the
sgen at timestamp T₃(sgen) which may not equal T₃(bus). There is no assertion that
`len(sgen_ts_list) == len(bus_ts_list)`.

**Fix:** Add a guard after building both lists:

```python
# After building sgen_ts_list and bus_ts_list in _build_day_lookup:
if len(sgen_ts_list) != len(bus_ts_list):
    raise RuntimeError(
        f"Timestamp count mismatch: {len(bus_ts_list)} bus timestamps vs "
        f"{len(sgen_ts_list)} sgen timestamps. Re-run 'uv run sim' to repopulate."
    )
```

---

_Reviewed: 2026-06-25_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: standard_
