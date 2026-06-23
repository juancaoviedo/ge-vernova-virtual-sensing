"""
influx.py
---------
Shared InfluxDB helpers for the IEEE 33-bus DER measurement source.

Provides: client factory, readiness poll, idempotent bucket creation,
profiles bucket read/count, profiles write, and the per-entity state-write
helper that encodes the D-07 schema (forward contract for System 2).

This is a LIBRARY module — no __main__ runner. Import from ingest.py and sim.py.

Dependencies: influxdb-client, pandas, requests
Run:          imported — not executed directly
Effect:       InfluxDB connection + bucket + read/write helpers shared by
              ingest.py and sim.py
"""

import time

import requests
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

from ieee33 import config


# ---------------------------------------------------------------------------
# Client factory
# ---------------------------------------------------------------------------

def get_client() -> InfluxDBClient:
    """Return a configured InfluxDBClient using config.py credentials."""
    return InfluxDBClient(
        url=config.INFLUXDB_URL,
        token=config.INFLUXDB_TOKEN,
        org=config.INFLUXDB_ORG,
    )


# ---------------------------------------------------------------------------
# Readiness poll (Pitfall 3 — bootstrap order)
# ---------------------------------------------------------------------------

def wait_for_influx(timeout_s: int = 60) -> None:
    """Poll GET {INFLUXDB_URL}/ping until HTTP 204 (or 200), then return.

    Guards the first-run ``docker compose up`` + immediate ingest scenario
    where InfluxDB init mode takes several seconds to complete.

    Args:
        timeout_s: Maximum seconds to wait before raising RuntimeError.

    Raises:
        RuntimeError: If InfluxDB does not become ready within timeout_s.
    """
    ping_url = f"{config.INFLUXDB_URL}/ping"
    deadline = time.time() + timeout_s
    last_err: Exception | None = None
    while time.time() < deadline:
        try:
            resp = requests.get(ping_url, timeout=5)
            if resp.status_code in (200, 204):
                print(f"InfluxDB ready at {config.INFLUXDB_URL}")
                return
        except Exception as exc:
            last_err = exc
        time.sleep(1)
    raise RuntimeError(
        f"InfluxDB did not become ready within {timeout_s}s "
        f"(url={config.INFLUXDB_URL}, last_error={last_err})"
    )


# ---------------------------------------------------------------------------
# Idempotent bucket creation (Pitfall 4 — state bucket not created by Docker init)
# ---------------------------------------------------------------------------

def ensure_bucket(client: InfluxDBClient, name: str) -> None:
    """Create bucket ``name`` in config.INFLUXDB_ORG if it does not exist.

    Idempotent: does nothing if the bucket already exists.
    The Docker init only creates the 'profiles' bucket; this function must be
    called for 'state' (and any other bucket) before first write (D-06).

    Args:
        client: Active InfluxDBClient.
        name:   Bucket name to create or verify.
    """
    buckets_api = client.buckets_api()
    if buckets_api.find_bucket_by_name(name) is None:
        org_id = client.organizations_api().find_organizations(
            org=config.INFLUXDB_ORG
        )[0].id
        buckets_api.create_bucket(bucket_name=name, org_id=org_id)
        print(f"bucket '{name}' created")
    else:
        print(f"bucket '{name}' ready")


# ---------------------------------------------------------------------------
# Profiles: write (ingest.py) and read/count (ingest.py idempotency + sim.py)
# ---------------------------------------------------------------------------

def write_profiles(write_api, df) -> None:
    """Write a 96-row profile DataFrame to the 'profiles' bucket.

    Each row produces one Point("profiles") with fields load_pu, solar_pu,
    wind_pu and a UTC timestamp taken from the utc_timestamp column.

    Idempotent per D-08: identical measurement+field+timestamp overwrites in
    place — re-running ingest replaces the 96 profile points without duplicates.

    Args:
        write_api: SYNCHRONOUS write_api from client.write_api(SYNCHRONOUS).
        df:        DataFrame with columns ['utc_timestamp', 'load_pu',
                   'solar_pu', 'wind_pu']. utc_timestamp must be UTC-aware or
                   tz-naive (treated as UTC).
    """
    from datetime import timezone as _tz

    points = []
    for _, row in df.iterrows():
        ts = row["utc_timestamp"].to_pydatetime()
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=_tz.utc)
        p = (
            Point("profiles")
            .field("load_pu",  float(row["load_pu"]))
            .field("solar_pu", float(row["solar_pu"]))
            .field("wind_pu",  float(row["wind_pu"]))
            .time(ts)
        )
        points.append(p)
    write_api.write(
        bucket=config.PROFILES_BUCKET,
        org=config.INFLUXDB_ORG,
        record=points,
    )


def read_profiles(client: InfluxDBClient):
    """Query all 96 profile points for TARGET_DATE from the profiles bucket.

    Executes a Flux pivot query so the returned DataFrame has columns
    [_time, load_pu, solar_pu, wind_pu] — the same layout the 96-step sim loop
    expects (RESEARCH §Pattern 7, lines 572-578).

    Asserts exactly config.N_STEPS (96) rows are returned.

    Args:
        client: Active InfluxDBClient.

    Returns:
        pandas.DataFrame with columns _time, load_pu, solar_pu, wind_pu.

    Raises:
        AssertionError: If the returned row count is not exactly 96.
    """
    start = f"{config.TARGET_DATE}T00:00:00Z"
    # Stop = next day
    from datetime import date as _date, timedelta as _td
    next_day = (
        _date.fromisoformat(config.TARGET_DATE) + _td(days=1)
    ).isoformat()
    stop = f"{next_day}T00:00:00Z"

    flux = (
        f'from(bucket: "{config.PROFILES_BUCKET}")\n'
        f'  |> range(start: {start}, stop: {stop})\n'
        f'  |> filter(fn: (r) => r._measurement == "profiles")\n'
        f'  |> pivot(rowKey: ["_time"], columnKey: ["_field"], valueColumn: "_value")\n'
        f'  |> sort(columns: ["_time"])'
    )
    df = client.query_api().query_data_frame(flux)
    n = len(df) if df is not None else 0
    assert n == config.N_STEPS, (
        f"read_profiles: expected exactly {config.N_STEPS} rows for "
        f"TARGET_DATE={config.TARGET_DATE}, got {n}. "
        "Run 'uv run ingest' first to populate the profiles bucket."
    )
    return df


def count_profiles(client: InfluxDBClient) -> int:
    """Return the number of profile rows in the profiles bucket for TARGET_DATE.

    Used by ingest.py for idempotency check and the SPEC-6 96-point
    acceptance gate.  Returns 0 if the bucket is empty or if any error occurs
    (so ingest proceeds to fetch rather than crashing on missing data).

    Args:
        client: Active InfluxDBClient.

    Returns:
        Row count (int). 96 means the profiles are fully present.
    """
    start = f"{config.TARGET_DATE}T00:00:00Z"
    from datetime import date as _date, timedelta as _td
    next_day = (
        _date.fromisoformat(config.TARGET_DATE) + _td(days=1)
    ).isoformat()
    stop = f"{next_day}T00:00:00Z"

    flux = (
        f'from(bucket: "{config.PROFILES_BUCKET}")\n'
        f'  |> range(start: {start}, stop: {stop})\n'
        f'  |> filter(fn: (r) => r._measurement == "profiles")\n'
        f'  |> filter(fn: (r) => r._field == "load_pu")\n'
        f'  |> count()'
    )
    try:
        tables = client.query_api().query(flux)
        total = 0
        for table in tables:
            for record in table.records:
                total += record.get_value()
        return total
    except Exception:
        return 0


# ---------------------------------------------------------------------------
# State-write helper — D-07 per-entity schema (forward contract for System 2)
# ---------------------------------------------------------------------------

def write_state_step(
    write_api,
    timestamp,
    res_bus,
    res_line,
    res_sgen,
    res_ext_grid,
    res_trafo,
    tap_pos,
    shift_degree,
    system_dict,
) -> None:
    """Write one 15-min power-flow snapshot to the 'state' bucket.

    D-07 schema — per-entity measurements with tags:
      measurement "bus"    tag bus_id   fields vm_pu, va_degree
      measurement "line"   tag line_id  fields p_from_mw, q_from_mvar,
                                               p_to_mw, q_to_mvar,
                                               loading_percent, pl_mw, ql_mvar
      measurement "sgen"   tag sgen_id  fields p_mw, q_mvar
      measurement "system" (no tag)     fields total_load_mw, total_gen_mw,
                                               total_loss_mw, vmin_pu, vmax_pu,
                                               slack_p_mw, slack_q_mvar,
                                               tap_pos, shift_degree

    All points carry the same UTC timestamp (the OPSD 15-min UTC datetime for
    the step).  Written to STATE_BUCKET, org=config.INFLUXDB_ORG, SYNCHRONOUS.

    Forward contract for System 2: all downstream queries that read the 'state'
    bucket depend on this exact field/tag naming.  Do not rename fields without
    updating System 2 Flux queries.

    Args:
        write_api:    SYNCHRONOUS write_api.
        timestamp:    datetime (UTC-aware) for this step.
        res_bus:      net.res_bus DataFrame (index = pandapower bus idx).
        res_line:     net.res_line DataFrame (index = pandapower line idx).
        res_sgen:     net.res_sgen DataFrame (index = pandapower sgen idx).
        res_ext_grid: net.res_ext_grid DataFrame.
        res_trafo:    net.res_trafo DataFrame (unused fields; kept for API
                      consistency).
        tap_pos:      int — feeder transformer tap position (from
                      net.trafo.at[trafo_idx, "tap_pos"]).
        shift_degree: float — scheduled phase-shift angle (from
                      net.trafo.at[trafo_idx, "shift_degree"]).
        system_dict:  dict with keys: total_load_mw, total_gen_mw,
                      total_loss_mw, vmin_pu, vmax_pu, slack_p_mw, slack_q_mvar.
    """
    points = []

    # ---- bus measurement: one point per bus (all 33 buses) ----
    for idx, row in res_bus.iterrows():
        points.append(
            Point("bus")
            .tag("bus_id", str(idx))
            .field("vm_pu",     float(row["vm_pu"]))
            .field("va_degree", float(row["va_degree"]))
            .time(timestamp)
        )

    # ---- line measurement: in-service lines only ----
    for idx, row in res_line.iterrows():
        # Skip NaN rows (out-of-service tie-lines have NaN results)
        if any(
            (row[f] != row[f])  # NaN check without import
            for f in ["p_from_mw", "q_from_mvar", "loading_percent"]
        ):
            continue
        points.append(
            Point("line")
            .tag("line_id", str(idx))
            .field("p_from_mw",      float(row["p_from_mw"]))
            .field("q_from_mvar",    float(row["q_from_mvar"]))
            .field("p_to_mw",        float(row["p_to_mw"]))
            .field("q_to_mvar",      float(row["q_to_mvar"]))
            .field("loading_percent", float(row["loading_percent"]))
            .field("pl_mw",          float(row["pl_mw"]))
            .field("ql_mvar",        float(row["ql_mvar"]))
            .time(timestamp)
        )

    # ---- sgen measurement: one point per sgen ----
    for idx, row in res_sgen.iterrows():
        points.append(
            Point("sgen")
            .tag("sgen_id", str(idx))
            .field("p_mw",   float(row["p_mw"]))
            .field("q_mvar", float(row["q_mvar"]))
            .time(timestamp)
        )

    # ---- system measurement: scalar aggregates + regulator state ----
    slack_p = float(res_ext_grid["p_mw"].iloc[0]) if len(res_ext_grid) > 0 else 0.0
    slack_q = float(res_ext_grid["q_mvar"].iloc[0]) if len(res_ext_grid) > 0 else 0.0
    points.append(
        Point("system")
        .field("total_load_mw",  float(system_dict["total_load_mw"]))
        .field("total_gen_mw",   float(system_dict["total_gen_mw"]))
        .field("total_loss_mw",  float(system_dict["total_loss_mw"]))
        .field("vmin_pu",        float(system_dict["vmin_pu"]))
        .field("vmax_pu",        float(system_dict["vmax_pu"]))
        .field("slack_p_mw",     slack_p)
        .field("slack_q_mvar",   slack_q)
        .field("tap_pos",        int(tap_pos))
        .field("shift_degree",   float(shift_degree))
        .time(timestamp)
    )

    write_api.write(
        bucket=config.STATE_BUCKET,
        org=config.INFLUXDB_ORG,
        record=points,
    )
