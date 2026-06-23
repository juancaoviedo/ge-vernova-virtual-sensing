---
phase: 08-ieee-33-bus-der-measurement-source
plan: "03"
subsystem: infra
tags: [influxdb, influxdb-client, opsd, pandas, time-series, docker, InfluxDB2, profiles, state-schema]

requires:
  - phase: 08-ieee-33-bus-der-measurement-source/01
    provides: config.py constants (OPSD_URL, TARGET_DATE, INFLUXDB_*, PROFILES_BUCKET, STATE_BUCKET, N_STEPS)

provides:
  - influx.py shared helpers: get_client, wait_for_influx, ensure_bucket, read_profiles, count_profiles, write_profiles, write_state_step
  - ingest.py entry point: one-time OPSD fetch → normalise → write 96 profile points to InfluxDB profiles bucket
  - Programmatic creation of the state bucket (D-06) — both buckets live and populated
  - D-07 forward contract: per-entity state schema (bus/line/sgen/system measurements with tags) encoded in write_state_step

affects:
  - 08-ieee-33-bus-der-measurement-source/04 (sim.py reads profiles via influx.read_profiles; writes state via influx.write_state_step)

tech-stack:
  added:
    - influxdb-client 1.50.0 — SYNCHRONOUS write_api, BucketsApi, query_api
    - requests (HEAD reachability check for OPSD endpoint)
    - pandas chunked CSV streaming (pd.read_csv chunksize=10_000 for 107 MB CSV)
  patterns:
    - Idempotent bucket creation via find_bucket_by_name + create_bucket (Pitfall 4)
    - Readiness poll via GET /ping before writing (Pitfall 3 bootstrap-order guard)
    - SYNCHRONOUS write_api with Point batch for deterministic InfluxDB writes
    - Fail-loud no-fallback halt: requests.head + sys.exit(1) on unreachable OPSD endpoint
    - Flux pivot query (rowKey _time, columnKey _field) for 96-row profile retrieval
    - D-07 per-entity-type measurements with bus_id/line_id tags for single-variable 96-point queries

key-files:
  created:
    - system1-measurement-source/src/ieee33/influx.py
    - system1-measurement-source/src/ieee33/ingest.py
  modified: []

key-decisions:
  - "influx.py is a library module only (no __main__) — shared by ingest.py and sim.py"
  - "count_profiles() uses a field-filter + count() Flux query returning 0 on error, not raising, so idempotency check in ingest.py never crashes on an empty bucket"
  - "write_state_step() skips NaN line rows inline (via != comparison) rather than importing pandas — avoids circular dependency and keeps the helper pure"
  - "wait_for_influx() polls /ping via requests (not influxdb-client.ping()) to avoid auth dependency before the setup mode completes"

patterns-established:
  - "influx.py pattern: shared DB helper library with client factory + readiness poll + idempotent bucket create + read/write helpers"
  - "Halt+notify pattern: any unreachable external data source triggers sys.exit(1) with 'provide manually' message — no synthetic fallback (SPEC-3)"

requirements-completed: [SPEC-3, SPEC-6]

duration: 20min
completed: 2026-06-23
---

# Phase 08 Plan 03: InfluxDB Helpers + OPSD Profile Ingest Summary

**OPSD 15-min DE profiles (96 points, 2017-06-07) ingested into InfluxDB profiles bucket; state bucket created programmatically; influx.py shared helper library encodes the D-07 forward-contract schema for System 2**

## Performance

- **Duration:** ~20 min
- **Started:** 2026-06-23T00:36:00Z
- **Completed:** 2026-06-23T00:56:18Z
- **Tasks:** 2
- **Files modified:** 2

## Accomplishments

- `influx.py` provides all 7 shared helpers: `get_client`, `wait_for_influx`, `ensure_bucket`, `read_profiles`, `count_profiles`, `write_profiles`, `write_state_step`
- `ingest.py` performs one-time OPSD 15-min fetch with chunked streaming, NaN guard, peak-normalisation, and writes exactly 96 timestamped profile points to InfluxDB — halts non-zero with no-fallback message if endpoint unreachable
- Both InfluxDB buckets (`profiles` + `state`) are live after `uv run ingest`; idempotent re-run confirmed (skips fetch, re-verifies 96 points)
- `write_state_step()` encodes the D-07 per-entity schema (bus/line/sgen/system measurements with bus_id/line_id tags) — Plan 04 sim.py can write state without defining its own schema

## Task Commits

1. **Task 1: influx.py — client factory, readiness poll, ensure_bucket, profiles read/write/count, state-write helpers** - `b13bac0` (feat)
2. **Task 2: ingest.py — one-time OPSD fetch → normalize → write 96 profile points** - `6e6495f` (feat)

**Plan metadata:** (forthcoming docs commit)

## Files Created/Modified

- `system1-measurement-source/src/ieee33/influx.py` — Shared InfluxDB helper library: client factory, readiness poll, idempotent bucket creation, Flux profiles query, state-write helper (D-07 schema forward contract)
- `system1-measurement-source/src/ieee33/ingest.py` — Entry point: OPSD HEAD check → chunked CSV read → NaN guard → normalise → write to profiles bucket; creates state bucket; idempotent; validation gate asserts 96 points

## Decisions Made

- `count_profiles()` returns 0 on any exception (rather than raising) so the idempotency check in `main()` works correctly on an empty or not-yet-initialised bucket — avoids "bucket not found" crash on first run before `ensure_bucket` is called
- `wait_for_influx()` uses `requests.GET /ping` instead of `InfluxDBClient.ping()` because the init-mode setup might reject authenticated calls until complete; raw HTTP avoids auth dependency
- NaN guard raises `ValueError` (not `sys.exit`) so it propagates up to the `if __name__=="__main__"` FATAL wrapper, giving a clean error message

## Deviations from Plan

None — plan executed exactly as written.

## Issues Encountered

None — Docker images pulled fresh (first run). InfluxDB init mode completed within the 60s timeout window of `wait_for_influx()`. OPSD endpoint returned HTTP 200 and the 107 MB CSV streamed successfully.

## Threat Surface Scan

No new network endpoints, auth paths, or schema changes beyond what the plan's threat model covers (T-08-07 through T-08-10 all mitigated as specified: HTTPS + row-count/NaN assertions, HEAD timeout + halt+notify, localhost-only token, idempotent overwrites).

## Known Stubs

None — all data paths are fully wired. `influx.read_profiles()` and `influx.write_state_step()` are complete contracts ready for Plan 04 sim.py consumption.

## Next Phase Readiness

- Plan 04 (sim.py) can call `influx.read_profiles(client)` to load 96 profile rows and `influx.write_state_step(...)` to persist each step's state snapshot
- InfluxDB container must be running (`docker compose up -d`) before sim.py executes
- The `profiles` bucket is populated with 96 DE 2017-06-07 rows; the `state` bucket exists and is empty (ready for sim writes)

## Self-Check: PASSED

- influx.py: FOUND at system1-measurement-source/src/ieee33/influx.py
- ingest.py: FOUND at system1-measurement-source/src/ieee33/ingest.py
- Commit b13bac0: FOUND (Task 1 — influx.py)
- Commit 6e6495f: FOUND (Task 2 — ingest.py)
- Live verification: `uv run ingest` wrote 96 profile points; idempotent re-run confirmed; state bucket exists

---

*Phase: 08-ieee-33-bus-der-measurement-source*
*Completed: 2026-06-23*
