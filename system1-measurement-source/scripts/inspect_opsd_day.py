"""
inspect_opsd_day.py
-------------------
One-time data-inspection script that scans the open-power-system-data 15-minute
singleindex CSV for German (DE) summer days with high solar capacity factor and
decent wind. Prints the top candidate days ranked by combined solar+wind quality,
then recommends the single best day for use as TARGET_DATE in config.py.

Dependencies: pandas, requests, numpy
Run:          uv run python scripts/inspect_opsd_day.py
Effect:       Prints candidate high-DER days and a single recommended TARGET_DATE.
              Does NOT write files or modify any database.
              Halts non-zero if the OPSD endpoint is unreachable.
"""

import sys
import requests
import pandas as pd

OPSD_URL = (
    "https://data.open-power-system-data.org/time_series/2020-10-06/"
    "time_series_15min_singleindex.csv"
)
COLS = [
    "utc_timestamp",
    "DE_load_actual_entsoe_transparency",
    "DE_solar_profile",
    "DE_wind_profile",
]

# Summer months (June, July, August) in years with reliable DE coverage
SUMMER_MONTHS = {6, 7, 8}
YEAR_RANGE = range(2017, 2020)  # 2017-2019 inclusive
MIN_WIND_MEAN = 0.3             # minimum daily mean wind profile to qualify
N_STEPS = 96                    # exactly 96 rows per day (15-min cadence)


def check_opsd_reachable() -> None:
    """HEAD-check the OPSD endpoint; exit non-zero with clear message if unreachable."""
    print(f"Checking OPSD endpoint reachability: {OPSD_URL}")
    try:
        resp = requests.head(OPSD_URL, timeout=20)
        resp.raise_for_status()
        print(f"  -> HTTP {resp.status_code} OK")
    except Exception as exc:
        print(
            f"\nERROR: OPSD dataset unreachable ({exc}).\n"
            "Download time_series_15min_singleindex.csv manually from:\n"
            "  https://data.open-power-system-data.org/time_series/\n"
            "and re-run this script with the local file path.",
            file=sys.stderr,
        )
        sys.exit(1)


def stream_summer_days() -> pd.DataFrame:
    """Chunked-read OPSD CSV; accumulate DE summer-day rows from 2017-2019."""
    print("Streaming OPSD CSV (chunked read, usecols filter)…")
    accumulated: list[pd.DataFrame] = []
    chunks_read = 0

    for chunk in pd.read_csv(
        OPSD_URL,
        usecols=COLS,
        parse_dates=["utc_timestamp"],
        chunksize=50_000,
    ):
        chunks_read += 1
        # Filter to DE summer months in the target year range
        ts = chunk["utc_timestamp"]
        mask = (
            ts.dt.year.isin(YEAR_RANGE)
            & ts.dt.month.isin(SUMMER_MONTHS)
        )
        subset = chunk[mask]
        if len(subset) > 0:
            accumulated.append(subset)

        # Early exit: once we've passed 2019-08-31 we're done
        if len(chunk) > 0:
            last_ts = ts.iloc[-1]
            if last_ts.year > 2019 and last_ts.month > 8:
                break

    print(f"  -> Read {chunks_read} chunks; accumulated {sum(len(d) for d in accumulated)} summer rows")
    if not accumulated:
        print("ERROR: No summer 2017-2019 rows found in dataset.", file=sys.stderr)
        sys.exit(1)

    df = pd.concat(accumulated, ignore_index=True)
    df = df.sort_values("utc_timestamp").reset_index(drop=True)
    return df


def compute_day_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group by calendar date and compute per-day statistics.
    Returns rows where: count==96, zero NaN in all three columns.
    """
    df["date"] = df["utc_timestamp"].dt.date.astype(str)

    stats = (
        df.groupby("date")
        .agg(
            row_count=("utc_timestamp", "count"),
            solar_mean=("DE_solar_profile", "mean"),
            solar_max=("DE_solar_profile", "max"),
            wind_mean=("DE_wind_profile", "mean"),
            wind_max=("DE_wind_profile", "max"),
            load_nan=("DE_load_actual_entsoe_transparency", lambda x: x.isna().sum()),
            solar_nan=("DE_solar_profile", lambda x: x.isna().sum()),
            wind_nan=("DE_wind_profile", lambda x: x.isna().sum()),
        )
        .reset_index()
    )

    # Quality filter: exactly 96 rows, zero NaN in all three columns
    stats["total_nan"] = stats["load_nan"] + stats["solar_nan"] + stats["wind_nan"]
    quality = stats[
        (stats["row_count"] == N_STEPS)
        & (stats["total_nan"] == 0)
        & (stats["wind_mean"] >= MIN_WIND_MEAN)
    ].copy()

    # Composite rank score: weight solar heavily (interview narrative is sunny+breezy day)
    quality["score"] = quality["solar_mean"] * 0.7 + quality["wind_mean"] * 0.3
    quality = quality.sort_values("score", ascending=False).reset_index(drop=True)
    return quality


def main() -> None:
    check_opsd_reachable()
    df = stream_summer_days()
    candidates = compute_day_stats(df)

    if len(candidates) == 0:
        print(
            "\nERROR: No qualifying summer days found (96 rows, zero NaN, wind_mean >= 0.3).",
            file=sys.stderr,
        )
        sys.exit(1)

    top_n = candidates.head(10)
    print("\n" + "=" * 72)
    print("  TOP CANDIDATE HIGH-DER DE SUMMER DAYS (2017-2019)")
    print("  Criteria: 96 rows, zero NaN, wind_mean >= 0.30")
    print("  Score = solar_mean * 0.70 + wind_mean * 0.30")
    print("=" * 72)
    print(f"{'Rank':<5} {'Date':<12} {'solar_mean':>10} {'solar_max':>10} {'wind_mean':>10} {'wind_max':>10} {'score':>8}")
    print("-" * 72)
    for rank, row in top_n.iterrows():
        print(
            f"{rank + 1:<5} {row['date']:<12} "
            f"{row['solar_mean']:>10.4f} {row['solar_max']:>10.4f} "
            f"{row['wind_mean']:>10.4f} {row['wind_max']:>10.4f} "
            f"{row['score']:>8.4f}"
        )

    best = candidates.iloc[0]
    print("\n" + "=" * 72)
    print(f"  RECOMMENDED TARGET_DATE = \"{best['date']}\"")
    print(f"  solar_mean={best['solar_mean']:.4f}  wind_mean={best['wind_mean']:.4f}  score={best['score']:.4f}")
    print("  -> Hard-code this value in src/ieee33/config.py as TARGET_DATE")
    print("=" * 72 + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nFATAL: {exc}", file=sys.stderr)
        sys.exit(1)
