# Phase 8: IEEE 33-Bus DER Measurement Source - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-22
**Phase:** 08-ieee-33-bus-der-measurement-source
**Areas discussed:** DER day & profiles, DG split & sizing, OLTC modeling, Influx/Grafana/layout, Validation strategy, OPSD day & timestamps, Sim execution & orchestration

Requirements were locked by `08-SPEC.md` (7 requirements, ambiguity 0.13) — the discussion
covered HOW-to-implement decisions only.

---

## DER Day & Profiles

| Option | Description | Selected |
|--------|-------------|----------|
| High-DER sunny+breezy day | DE day with strong midday solar + decent wind; shows voltage rise, reverse flow, OLTC tapping, midday loss dip | ✓ |
| Typical / average day | Median day; more representative but mild swings | |
| Two-regime day (cloud transients) | Intermittent cloud cover; fast transients, noisier baseline | |

**User's choice:** High-DER sunny+breezy day
**Notes:** Normalization mechanics defaulted (and not overridden): scale DG by the 0–1 profile
columns × nameplate; peak-normalize load with 3.715 MW anchored as the daily peak.

---

## DG Split & Sizing

| Option | Description | Selected |
|--------|-------------|----------|
| Article/xlsx nameplates (faithful) | Use published ratings verbatim; risk of weak DER effects | |
| Faithful, scaled up if needed | Start from xlsx; scale uniformly to ~60–70% of peak if too small; document deviation | ✓ |
| Sized for strong reverse flow | DG > local load for dramatic reverse flow; least faithful | |

**User's choice (sizing):** Faithful, scaled up if needed

| Option | Description | Selected |
|--------|-------------|----------|
| Solar 18,22 / wind 25,33 (SPEC default) | Spec's example split | ✓ |
| Solar on the larger DG buses | Maximize midday signal | |
| You decide | Planner picks | |

**User's choice (split):** Solar 18,22 / wind 25,33 (SPEC default)

---

## OLTC Modeling

| Option | Description | Selected |
|--------|-------------|----------|
| Built-in tap controller; phase shifter scheduled | DiscreteTapControl via run_control=True; phase shifter scheduled+captured | |
| Closed-loop tap AND phase angle | Custom controller regulating both; more realistic, more risk | |
| You decide | Planner picks the exact pandapower mechanism | ✓ |

**User's choice:** You decide
**Notes:** Captured as Claude's discretion. Recommended starting point recorded in CONTEXT.md
(built-in tap controller; phase shifter scheduled+captured). Hard SPEC constraints retained:
tap+angle captured as state, tap within 0.95–1.05, feeder regulated near 1.0 pu.

---

## Influx / Grafana / Layout

| Option | Description | Selected |
|--------|-------------|----------|
| Two buckets, per-entity measurements | `profiles` + `state` buckets; per-entity-type measurements with bus_id/line_id tags | ✓ |
| One bucket, separate measurements | Single bucket; simpler ops, less tidy separation | |
| You decide | Planner picks | |

**User's choice (schema):** Two buckets, per-entity measurements

| Option | Description | Selected |
|--------|-------------|----------|
| Top-level dir + requirements.txt | New folder; pinned requirements.txt | |
| src/ package + pyproject.toml | Installable package | |
| You decide | Planner picks | |
| **Other (free text)** | User-specified tooling directive | ✓ |

**User's choice (layout):** *Free text* — "Create a folder. Use UV package manager. Use docker
compose to deploy the infrastructure, like Influx and Grafana. Explain in a rhythmic how to
execute the system."
**Notes:** Interpreted and confirmed as: dedicated top-level folder; uv (Astral) for pinned
Python deps (pyproject.toml + uv.lock); Docker Compose deploys infra (Influx + Grafana) only,
sim runs on host via uv; README with a clear step-by-step execution rhythm.

---

## Validation Strategy

| Option | Description | Selected |
|--------|-------------|----------|
| Quantitative vs published + per-step asserts | case33bw base case reproduces Baran & Wu (~0.913 pu @ bus 18) within tolerance; enhanced net converges + stays in band every step | ✓ |
| Convergence + band only | Lighter; no comparison to published numbers | |
| You decide | Planner picks depth/tolerances | |

**User's choice:** Quantitative vs published + per-step asserts

---

## OPSD Day & Timestamps

| Option | Description | Selected |
|--------|-------------|----------|
| Pick once, hard-code date in config | Inspect once, record the chosen DE date as a config constant; ingest extracts exactly that day | ✓ |
| Programmatic selection rule | Compute best sunny+breezy day each run via a metric | |
| You decide | Planner picks | |

**User's choice (day selection):** Pick once, hard-code date in config

| Option | Description | Selected |
|--------|-------------|----------|
| Real OPSD datetimes of the chosen day | Snapshots carry the day's actual timestamps; re-runs overwrite in place | ✓ |
| Canonical synthetic date | Remap onto a fixed date decoupled from source | |
| You decide | Planner picks | |

**User's choice (timestamps):** Real OPSD datetimes of the chosen day

---

## Sim Execution & Orchestration

| Option | Description | Selected |
|--------|-------------|----------|
| uv entry points + Makefile wrapper | uv-run entry points + Makefile/justfile wrapping the full sequence | |
| Plain README commands only | Explicit commands listed in order; no wrapper | |
| You decide | Planner picks the orchestration mechanism | ✓ |

**User's choice:** You decide
**Notes:** Boundary confirmed (infra in Compose, sim on host via uv, ordered runbook).
Recommended mechanism recorded in CONTEXT.md (uv entry points + Makefile/justfile wrapper).

---

## Claude's Discretion

- OLTC / phase-shifter exact pandapower mechanism (recommended approach recorded).
- Run orchestration mechanism (uv entry points + Makefile/justfile recommended).
- Folder name, uv entry-point names, validation tolerances, snapshot write-batching/perf.

## Deferred Ideas

- Virtual-sensing estimator (System 2) — later phase.
- Measurement-noise / reduced-sensor capture layer — System 2 phase.
- True-vs-estimated error metrics / ORACS observability index — requires System 2.
- Aggressive DG sizing for strong reverse flow — revisit only if System 2 needs more range.
- Two-regime cloud-transient day — possible future dataset variant to stress-test System 2.
- Containerizing the sim itself — deliberately not done; could be added later.
- Unbalanced 3-phase, meshed config, BESS/EV, real-time streaming — SPEC out-of-scope.
