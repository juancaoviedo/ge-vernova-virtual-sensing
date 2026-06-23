"""
ingest.py
---------
One-time OPSD profile ingestion entry point for the IEEE 33-bus DER
measurement source.

Fetches the open-power-system-data 15-min DE zone time-series for
TARGET_DATE, peak-normalises the load profile, retains the pre-normalised
solar and wind capacity factors, and writes exactly 96 timestamped rows to
the InfluxDB 'profiles' bucket.

If the OPSD endpoint is unreachable the script exits non-zero with a clear
message instructing the user to provide the file manually.  NO substitute or
synthetic data is ever written (SPEC-3 locked boundary).

Dependencies: requests, pandas, influxdb-client, python-dotenv
Run:          uv run ingest  (after docker compose up -d)
Effect:       writes 96 profile rows (load_pu, solar_pu, wind_pu) to the
              InfluxDB 'profiles' bucket for config.TARGET_DATE; creates the
              'state' bucket programmatically (D-06).
"""

import sys

import pandas as pd
import requests
from influxdb_client.client.write_api import SYNCHRONOUS

from ieee33 import config
from ieee33 import influx


# ---------------------------------------------------------------------------
# OPSD fetch + normalise
# ---------------------------------------------------------------------------

def fetch_opsd_day(target_date: str) -> pd.DataFrame:
    """Stream OPSD CSV, extract one 96-row day, normalise, return DataFrame.

    Reachability check first (SPEC-3): if the endpoint is unreachable the
    function prints a clear "provide the file manually" message to stderr and
    calls sys.exit(1) — NO fallback, NO synthetic data.

    Pitfall 7 NaN guard: all three source columns must have ZERO NaN across
    the 96 rows; a NaN day means the wrong TARGET_DATE was pinned in config.

    Args:
        target_date: ISO date string matching config.TARGET_DATE, e.g.
                     "2017-06-07".

    Returns:
        DataFrame with columns ['utc_timestamp', 'load_pu', 'solar_pu',
        'wind_pu'] — exactly 96 rows.
    """
    # ---- Reachability check (SPEC-3 no-fallback halt) ----
    try:
        resp = requests.head(config.OPSD_URL, timeout=15)
        resp.raise_for_status()
    except Exception as exc:
        print(
            f"ERROR: OPSD dataset unreachable ({exc}).\n"
            "Download time_series_15min_singleindex.csv manually and provide it "
            "via a local file path — NO substitute data will be written.",
            file=sys.stderr,
        )
        sys.exit(1)

    # ---- Chunked read (107 MB CSV — avoid full load into RAM) ----
    chunks = []
    for chunk in pd.read_csv(
        config.OPSD_URL,
        usecols=config.OPSD_COLS,
        parse_dates=["utc_timestamp"],
        chunksize=10_000,
    ):
        day_mask = chunk["utc_timestamp"].dt.date.astype(str) == target_date
        day_rows = chunk[day_mask]
        if len(day_rows) > 0:
            chunks.append(day_rows)
        # Stop early once we have enough rows
        total = sum(len(c) for c in chunks)
        if total >= config.N_STEPS:
            break

    if not chunks:
        print(
            f"ERROR: No rows found for TARGET_DATE={target_date} in the OPSD CSV. "
            "Check that the date is within 2015-01-01..2020-10-06 and re-pin "
            "TARGET_DATE in config.py.",
            file=sys.stderr,
        )
        sys.exit(1)

    df = pd.concat(chunks).head(config.N_STEPS).reset_index(drop=True)
    assert len(df) == config.N_STEPS, (
        f"Expected {config.N_STEPS} rows for {target_date}, got {len(df)}"
    )

    # ---- Pitfall 7: NaN guard — no silent acceptance of gap days ----
    src_cols = [
        "DE_load_actual_entsoe_transparency",
        "DE_solar_profile",
        "DE_wind_profile",
    ]
    for col in src_cols:
        n_nan = df[col].isna().sum()
        if n_nan > 0:
            raise ValueError(
                f"OPSD column '{col}' has {n_nan} NaN value(s) for "
                f"TARGET_DATE={target_date}. This date has missing data — "
                "re-pin TARGET_DATE in config.py to a clean day "
                "(run scripts/inspect_opsd_day.py to find one)."
            )

    # ---- Normalise (D-02 / D-03) ----
    # load_pu: peak-normalise so daily max = 1.0 (article 3.715 MW is the physical anchor)
    load_peak = df["DE_load_actual_entsoe_transparency"].max()
    df["load_pu"] = df["DE_load_actual_entsoe_transparency"] / load_peak

    # solar_pu and wind_pu: already 0-1 pre-normalised capacity factors in OPSD
    df["solar_pu"] = df["DE_solar_profile"]
    df["wind_pu"] = df["DE_wind_profile"]

    return df[["utc_timestamp", "load_pu", "solar_pu", "wind_pu"]]


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """Fetch OPSD profiles once and write 96 points to the profiles bucket.

    Steps:
    1. Connect to InfluxDB and wait for it to be ready (Pitfall 3).
    2. Create profiles and state buckets if they do not exist (D-06/Pitfall 4).
    3. Idempotency check: if 96 profile points already present, skip fetch.
    4. Fetch + normalise + write 96 profile points (if not already present).
    5. Validation gate: assert exactly 96 points in the bucket (SPEC-3/SPEC-6).
    """
    # ---- Step 1: connect + wait for InfluxDB readiness ----
    client = influx.get_client()
    influx.wait_for_influx()

    # ---- Step 2: ensure both buckets exist (D-06) ----
    influx.ensure_bucket(client, config.PROFILES_BUCKET)
    influx.ensure_bucket(client, config.STATE_BUCKET)

    # ---- Step 3: idempotency check (D-08 / Anti-Pattern line 586) ----
    existing = influx.count_profiles(client)
    if existing == config.N_STEPS:
        print(
            f"profiles already present ({existing} points for "
            f"{config.TARGET_DATE}) — skipping fetch"
        )
    else:
        # ---- Step 4: fetch + write ----
        print(f"fetching OPSD 15-min profiles for TARGET_DATE={config.TARGET_DATE} ...")
        df = fetch_opsd_day(config.TARGET_DATE)
        print(f"  fetched {len(df)} rows; writing to bucket '{config.PROFILES_BUCKET}' ...")
        write_api = client.write_api(write_options=SYNCHRONOUS)
        influx.write_profiles(write_api, df)
        print("  write complete.")

    # ---- Step 5: validation gate (build_site.py ethos) ----
    n = influx.count_profiles(client)
    if n != config.N_STEPS:
        print(
            f"\n--- INGEST VALIDATION FAILED ---\n"
            f"expected {config.N_STEPS} profile points, found {n}",
            file=sys.stderr,
        )
        client.close()
        sys.exit(1)

    print(
        f"ingest OK — {n} profile points in bucket "
        f"'{config.PROFILES_BUCKET}' for {config.TARGET_DATE}"
    )
    client.close()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nFATAL: {exc}", file=sys.stderr)
        sys.exit(1)
