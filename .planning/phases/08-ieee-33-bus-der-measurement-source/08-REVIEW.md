---
phase: 08-ieee-33-bus-der-measurement-source
reviewed: 2026-06-23T00:00:00Z
depth: deep
files_reviewed: 8
files_reviewed_list:
  - system1-measurement-source/src/ieee33/config.py
  - system1-measurement-source/src/ieee33/network.py
  - system1-measurement-source/src/ieee33/validate.py
  - system1-measurement-source/src/ieee33/influx.py
  - system1-measurement-source/src/ieee33/ingest.py
  - system1-measurement-source/src/ieee33/sim.py
  - system1-measurement-source/scripts/inspect_opsd_day.py
  - system1-measurement-source/docker-compose.yml
findings:
  critical: 1
  warning: 5
  info: 4
  total: 10
status: issues_found
---

# Phase 08: Code Review Report

**Reviewed:** 2026-06-23
**Depth:** deep (cross-file analysis, call chain tracing, InfluxDB schema verification)
**Files Reviewed:** 8
**Status:** issues_found

## Summary

Reviewed the complete Phase 08 IEEE 33-bus DER measurement source. The power-systems
modeling is sound: `case33bw` indexing (N-1), HV bus insertion, `DiscreteTapControl` with
`run_control=True`, capacitive shunt sign convention, and tap read from `net.trafo` (not
`res_trafo`) are all correct. The D-07 per-entity InfluxDB schema is consistent between
`influx.py` and the Grafana dashboard queries. The ingest halt+no-fallback contract is
correctly implemented.

One correctness bug warrants immediate attention: the state read-back gate in `sim.py`
uses an unbounded time range that would falsely fail (or silently pass with the wrong
count) if the `state` bucket contains points from a previous run at different timestamps.
Five warnings cover resource leak paths, a Makefile dependency gap, a fragile
`query_data_frame` return-type assumption, and an unhelpful error on org misconfiguration.
Four info items cover naming, a pandas idiom, and a logic quirk in validation.

The two documented known observations (OLTC tap neutral all day; buses 12-15 dipping to
~0.949 pu at peak evening) are correctly annotated in `sim.py` as non-fatal physics
results and are NOT flagged here.

---

## Critical Issues

### CR-01: State Read-Back Validation Uses Unbounded Range — Fails on Second TARGET_DATE

**File:** `system1-measurement-source/src/ieee33/sim.py:263`

**Issue:** The post-run SPEC-6 read-back gate queries `range(start: 0)` (from UNIX epoch)
rather than scoping to `TARGET_DATE`. InfluxDB overwrites points only when
`measurement + tag set + timestamp` are identical. If `TARGET_DATE` is ever changed and
`sim` is re-run without clearing the `state` bucket (i.e., without `make clean`), the
old 96 points (at the previous date's timestamps) persist alongside the new 96 points.
`len(rb_df)` then returns 192, the assertion `n_points != config.N_STEPS` triggers, and
`sim` exits 1 — a false failure. Conversely if only a partial previous run exists, the
count could be some other number and the gate gives a misleading result.

**Current code:**
```python
flux_readback = (
    f'from(bucket: "{config.STATE_BUCKET}")\n'
    f'  |> range(start: 0)\n'          # <-- unbounded: all time since epoch
    f'  |> filter(fn: (r) => r._measurement == "bus")\n'
    f'  |> filter(fn: (r) => r.bus_id == "17")\n'
    f'  |> filter(fn: (r) => r._field == "vm_pu")'
)
```

**Fix:** Scope the range to `TARGET_DATE` exactly as `read_profiles` and `count_profiles`
do:
```python
_start = f"{config.TARGET_DATE}T00:00:00Z"
_next  = (
    __import__("datetime").date.fromisoformat(config.TARGET_DATE)
    + __import__("datetime").timedelta(days=1)
).isoformat()
_stop  = f"{_next}T00:00:00Z"

flux_readback = (
    f'from(bucket: "{config.STATE_BUCKET}")\n'
    f'  |> range(start: {_start}, stop: {_stop})\n'
    f'  |> filter(fn: (r) => r._measurement == "bus")\n'
    f'  |> filter(fn: (r) => r.bus_id == "17")\n'
    f'  |> filter(fn: (r) => r._field == "vm_pu")'
)
```

---

## Warnings

### WR-01: InfluxDB Client Not Closed on OPSD Fetch Failure Path

**File:** `system1-measurement-source/src/ieee33/ingest.py:59-66` (leak site: line 142)

**Issue:** `main()` creates the InfluxDB client at line 142, then calls
`fetch_opsd_day()` at line 159. Inside `fetch_opsd_day`, if the OPSD endpoint is
unreachable (or if no rows are found for the date), the function calls `sys.exit(1)`
directly. `sys.exit()` raises `SystemExit` which derives from `BaseException`, not
`Exception`, so the `__main__` `except Exception` block does not catch it. The client is
never closed — its background flush thread and connection pool are leaked.

This is a local dev tool so the OS reclaims file descriptors on process exit, but the
`influxdb-client` documentation explicitly warns that the background batch processor can
drop buffered writes if the client is not closed cleanly. With `SYNCHRONOUS` mode the
write risk is absent, but the pattern sets a bad precedent if mode is ever changed.

**Fix:** Extract the fetch into a try/finally in `main()`, or use a context manager:
```python
client = influx.get_client()
try:
    influx.wait_for_influx()
    influx.ensure_bucket(client, config.PROFILES_BUCKET)
    influx.ensure_bucket(client, config.STATE_BUCKET)
    existing = influx.count_profiles(client)
    if existing == config.N_STEPS:
        print(f"profiles already present ({existing} points) — skipping fetch")
    else:
        df = fetch_opsd_day(config.TARGET_DATE)   # may sys.exit(1)
        write_api = client.write_api(write_options=SYNCHRONOUS)
        influx.write_profiles(write_api, df)
    n = influx.count_profiles(client)
    if n != config.N_STEPS:
        print(f"\n--- INGEST VALIDATION FAILED ---\n...", file=sys.stderr)
        sys.exit(1)
    print(f"ingest OK — {n} profile points ...")
finally:
    client.close()
```
(The `sys.exit(1)` inside `fetch_opsd_day` will still fire through the `finally` block,
cleanly closing the client first.)

---

### WR-02: InfluxDB Client Not Closed on RuntimeError / AssertionError Path in sim.py

**File:** `system1-measurement-source/src/ieee33/sim.py:127-141`

**Issue:** `main()` creates `client` at line 127. If `influx.read_profiles(client)` raises
`AssertionError` (fewer than 96 rows) or if the defensive `RuntimeError` at line 138 is
raised, execution jumps to the `__main__` `except Exception` handler at line 310 which
prints `FATAL:` and exits 1 — without calling `client.close()`. Same concern as WR-01:
SYNCHRONOUS mode mitigates write risk, but the resource leak is real.

**Fix:** Wrap the `main()` body in a `try/finally`:
```python
client = influx.get_client()
try:
    influx.wait_for_influx()
    influx.ensure_bucket(client, config.STATE_BUCKET)
    prof = influx.read_profiles(client)
    # ... rest of main ...
    client.close()
except Exception:
    client.close()
    raise
```
Or equivalently move the `try/finally` to the `__main__` block and close the client
there, passing it as a parameter.

---

### WR-03: `make sim` Has No `ingest` Dependency — Fails with Opaque Error

**File:** `system1-measurement-source/Makefile:16-17`

**Issue:** The `sim` target depends on `up` (starts Docker Compose) but not on `ingest`.
Running `make sim` on a clean checkout proceeds to call `uv run sim`, which calls
`influx.read_profiles()`, which asserts 96 rows and raises:
```
AssertionError: read_profiles: expected exactly 96 rows for TARGET_DATE=2017-06-07, got 0.
Run 'uv run ingest' first to populate the profiles bucket.
```
The error message is informative, but the failure is preventable. The `all` target
correctly orders `ingest` before `sim` (`all: up ingest sim`), but a developer running
`make sim` directly skips that guard.

**Fix:**
```makefile
sim: ingest
	uv run sim
```
(Since `ingest` already depends on `up`, this transitively pulls in the Docker stack.)

---

### WR-04: `query_data_frame` List Return Type Makes Row-Count Assertion Fragile

**File:** `system1-measurement-source/src/ieee33/influx.py:174-180`

**Issue:** `influxdb_client.QueryApi.query_data_frame()` returns:
- A single `pandas.DataFrame` when the query produces one table (current happy path).
- A `list[DataFrame]` when the query produces multiple tables.
- An empty `DataFrame` (not `None`) when the query returns no results.

The `read_profiles()` function relies on the pivot query producing a single table (true
now because the `profiles` measurement has no tags). If tags are ever added (e.g., a
`source` tag for tracking data provenance), the function silently returns a `list`, and
`len(df)` counts DataFrames rather than rows. The assertion `n == config.N_STEPS` (96)
would then compare e.g. `3 == 96` and raise with a misleading message.

The `sim.py` read-back at line 269-270 has the same pattern (`rb_df` check uses
`if rb_df is not None else 0`; an empty DataFrame is not `None` so this guard is
always False and adds no protection).

**Fix:** Normalise the return value before checking length:
```python
import pandas as pd

df = client.query_api().query_data_frame(flux)
if isinstance(df, list):
    df = pd.concat(df, ignore_index=True) if df else pd.DataFrame()
n = len(df)
```
Apply the same pattern to the `rb_df` read-back in `sim.py`.

---

### WR-05: `ensure_bucket` Raises Unhelpful `IndexError` on Org Misconfiguration

**File:** `system1-measurement-source/src/ieee33/influx.py:91-94`

**Issue:** When the bucket does not exist, `ensure_bucket` resolves the org ID with:
```python
org_id = client.organizations_api().find_organizations(
    org=config.INFLUXDB_ORG
)[0].id
```
If `INFLUXDB_ORG` is wrong (e.g., `.env` missing or mis-typed), `find_organizations`
returns an empty list and `[0]` raises `IndexError: list index out of range`. This
propagates as a fatal exception with a message that gives no hint about the root cause
(wrong org name vs. auth failure vs. InfluxDB not ready).

**Fix:**
```python
orgs = client.organizations_api().find_organizations(org=config.INFLUXDB_ORG)
if not orgs:
    raise RuntimeError(
        f"InfluxDB org '{config.INFLUXDB_ORG}' not found — "
        "check INFLUXDB_ORG in .env and that InfluxDB init completed."
    )
org_id = orgs[0].id
```

---

## Info

### IN-01: `net.ext_grid.bus = hv_bus` Uses Discouraged Pandas Attribute Assignment

**File:** `system1-measurement-source/src/ieee33/network.py:90`

**Issue:** `net.ext_grid.bus = hv_bus` modifies the `bus` column via pandas attribute
assignment. This works for a single-row DataFrame (case33bw has one ext_grid) but is
flagged by pandas documentation as potentially unreliable in copy-on-write contexts
(pandas 2.0+ has CoW semantics in development). It silently sets ALL rows in the `bus`
column, not just row 0.

**Fix:** Use explicit label-based assignment:
```python
net.ext_grid.loc[:, "bus"] = hv_bus
```

---

### IN-02: `vmin_series` / `vmax_series` Variable Names Are Misleading Scalars

**File:** `system1-measurement-source/src/ieee33/sim.py:293-294`

**Issue:**
```python
vmin_series = state["system_dict"]["vmin_pu"]  # last step value (scalar)
vmax_series = state["system_dict"]["vmax_pu"]  # last step value (scalar)
```
These are plain floats (the final step's vmin/vmax), not pandas Series. The name
`vmin_series` implies a time-indexed collection and is confusing to a reader. The inline
comment acknowledges this ("last step value (scalar)") but the name contradicts it.

**Fix:**
```python
last_vmin = state["system_dict"]["vmin_pu"]
last_vmax = state["system_dict"]["vmax_pu"]
```

---

### IN-03: `inspect_opsd_day.py` Early Exit Condition Uses Wrong Logical Operator

**File:** `system1-measurement-source/scripts/inspect_opsd_day.py:82`

**Issue:**
```python
if last_ts.year > 2019 and last_ts.month > 8:
    break
```
The stated intent (comment: "once we've passed 2019-08-31 we're done") requires exiting
as soon as the chunk passes into year 2020. With `and`, the condition is `True` only
when `year > 2019` AND `month > 8` simultaneously — meaning 2020 January through August
chunks are not exited, adding ~8 months of unnecessary reads from the 107 MB CSV.
Functional correctness is unaffected (the year filter in `ts.dt.year.isin(YEAR_RANGE)`
prevents these rows from being accumulated), but it wastes I/O.

**Fix:**
```python
if last_ts.year > 2019:
    break
```

---

### IN-04: Gate 1 in `validate.py` Masks Bus-Location Failure When Value Is Also Wrong

**File:** `system1-measurement-source/src/ieee33/validate.py:53-64`

**Issue:** The Gate 1 logic checks voltage value first, then bus location via `elif`:
```python
if abs(vm_min - config.BARANWU_VMIN_PU) >= config.BARANWU_TOL:
    failures.append("Gate 1 FAILED: vm_min=... value wrong")
elif vm_min_bus != config.BARANWU_VMIN_BUS:
    failures.append("Gate 1 FAILED: vm_min at wrong bus")
```
If both the value is wrong AND the bus is wrong (e.g., the network model has a bug that
shifts the minimum to a completely different lateral), only the value failure is reported.
The bus-location diagnostic is silently skipped. This is not a correctness issue in the
gate's pass/fail outcome, but it makes failure diagnosis harder.

**Fix:** Report both conditions independently:
```python
if abs(vm_min - config.BARANWU_VMIN_PU) >= config.BARANWU_TOL:
    failures.append(
        f"Gate 1 FAILED: vm_min={vm_min:.4f} pu, expected "
        f"{config.BARANWU_VMIN_PU:.3f} ± {config.BARANWU_TOL} pu"
    )
if vm_min_bus != config.BARANWU_VMIN_BUS:
    failures.append(
        f"Gate 1 FAILED: vm_min at pp_bus={vm_min_bus} "
        f"(article bus {vm_min_bus + 1}), expected pp_bus={config.BARANWU_VMIN_BUS}"
    )
```

---

_Reviewed: 2026-06-23_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: deep_
