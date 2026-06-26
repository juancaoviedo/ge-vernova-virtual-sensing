# Phase 10: System 2 — Streaming Distribution State Estimator (MQTT + FASE) - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-26
**Phase:** 10-system-2-streaming-distribution-state-estimator-mqtt-fase
**Areas discussed:** Runner & config ergonomics, FASE predict-step forecast model, Forecast-error knob, Dashboards

> SPEC.md (13 locked requirements, ambiguity 0.11) + ROADMAP D1–D6 fixed the WHAT and the
> architecture. Per the user's standing preference, the "which areas to discuss" menu was skipped;
> Claude surfaced the genuine implementation gray areas with recommendations and asked only where the
> user's taste changes the result.

---

## Runner & config ergonomics

| Option | Description | Selected |
|--------|-------------|----------|
| Per-estimator + config block | Three scripts (publish/estimate/score) + estimate_config.py ACTIVE block; `estimate` runs ONE estimator per invocation (--estimator); CLI overrides. Mirrors P9. | ✓ |
| All three per run | Single `estimate` fans out to wls+ekf+ukf together, tagged by estimator. | |
| Per-estimator + auto-score | Per-estimator runs, `score` auto-runs after each `estimate`. | |

**User's choice:** Per-estimator + config block
**Notes:** Carries P9's config-file-first + CLI-override ergonomics (P9 D-08/D-09). MQTT broker keeps
publish/estimate genuinely decoupled (async stream, not in-process loop).

---

## FASE predict-step forecast model

(Re-asked after the user requested a concrete explanation of how the forecast mean is computed.
Claude explained the `profiles`-as-forecast mechanics, the oracle boundary, and the sensitivity
propagation `x̂ₖ⁻ = x̂ₖ₋₁ + S·Δp_fcst`, `Qₖ = S·Cov(ε)·Sᵀ + Q_floor`.)

| Option | Description | Selected |
|--------|-------------|----------|
| Sensitivity-propagated, baseline as foil | Option 1 primary (profile schedule → degrade with forecast error → propagate Δinjection through network sensitivity S) + random-walk persistence as the A/B baseline foil behind the same interface. | ✓ |
| Sensitivity-propagated only | Option 1 only, no baseline foil. | |
| Random-walk only | Persistence + fixed diagonal Q; abandons the FASE narrative. | |

**User's choice:** Sensitivity-propagated, baseline as foil
**Notes:** The forecast-beats-persistence contrast is a deliverable. The `profiles` bucket (load/DER
schedule) is legitimate operator forecast side-information and is explicitly NOT the oracle — `state`/
`fault_event` remain forbidden to the estimator. This is the answer to "isn't that cheating?".

---

## Forecast-error knob ("no cheating" honesty level)

| Option | Description | Selected |
|--------|-------------|----------|
| Realistic day-ahead, config-tunable | Per-bus σ ≈ 5% of scheduled load, AR(1)-correlated, seed-derived, exposed as a knob in estimate_config.py for a forecast-quality study. | ✓ |
| Fixed modest error, not tunable | Hard-code ~5%; one less config knob, no sensitivity study. | |

**User's choice:** Realistic day-ahead, config-tunable
**Notes:** Error added on top of the schedule (not the realized truth), so the predict is honestly
imperfect even though the same profile generated the truth. Seeded for determinism (SPEC R13).

---

## Dashboards

| Option | Description | Selected |
|--------|-------------|----------|
| Two: day + fault (mirror P9) | ieee33-est-day.json (true-vs-est overlay, per-bus error, trace_P, NEES/NIS, dark-node recovery) + ieee33-est-fault.json (adds island-mode P-inflation + phase markers). | ✓ |
| One combined dashboard | Single JSON with a scenario/source template variable. | |
| Two + calibration third | day + fault + a dedicated NEES/NIS calibration dashboard. | |

**User's choice:** Two: day + fault (mirror P9)
**Notes:** Mirrors P9's two-dashboard convention; keeps the day-observability and fault-island
narratives cleanly separated. Additive to the four existing dashboards.

---

## Claude's Discretion

Locked as recommendations in CONTEXT.md (not put to the user — technical detail within the SPEC's
locked intent): MQTT topic hierarchy & JSON payloads (extending the P9 tag taxonomy);
`ieee33/netmodel/current` retained/versioned config payload shape; topology→`Ybus` rebuild method
(verified < 1e-9 vs pandapower); square-root UKF sigma-point params (α,β,κ); reuse of the DC demo's
χ²/LNR bad-data machinery for AC-WLS; exact config field names, Flux queries, Grafana panel layout,
NEES/NIS band math, and `Q_floor` magnitude.

## Deferred Ideas

System 3 (self-healing / FLISR / CaCSM / `netmodel/proposed`); three-phase unbalanced state;
branch-current (BCSE); federated/multi-area DSSE; non-MQTT transports; LinDistFlow-KF as a deliverable;
mis-specified-noise robustness study (`assumed_sigma_scale ≠ 1.0`) and the forecast-quality sweep
(knobs built, gating out of scope).
