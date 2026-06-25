# Phase 9: Measurement System (Observability Layer) - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-25
**Phase:** 09-measurement-system-observability-layer-configurable-sensor-m
**Areas discussed:** 8.1 schema verification, Sensor-bus assignments, measurements bucket schema, Config + module structure, Noise parameters, Sampling cadences, Dashboards

> Requirements were locked by `09-SPEC.md` (12 reqs, ambiguity 0.17). Discussion covered HOW only.
> The user declined the per-area selection menu and directed Claude to decide all areas with
> recommendations (consistent with accepting every prior recommendation). Decisions below are
> Claude's, grounded in the implemented 8.1 code and the locked SPEC.

---

## 8.1 schema verification (the hard dependency)

| Option | Description | Selected |
|--------|-------------|----------|
| Verify implemented `fault_event` writer vs frozen design | Read real `write_fault_step` + config consts | ✓ |
| Trust the frozen 08.1-CONTEXT design as-is | Risk: drift during implementation | |

**User's choice:** (Claude action per user instruction.) Verified — zero meaningful drift. Refinement
captured: `energised` is a TAG (string), dead buses are present-but-zero-filled, not absent.
**Notes:** Tie 34 was selected (no fallback). Bus 17 (μPMU candidate + DG) is inside the dead zone.

---

## Sensor-bus assignments per scenario

| Option | Description | Selected |
|--------|-------------|----------|
| Concrete bus lists hitting SPEC redundancy targets | realistic_sparse real-only <1 → ≥1 w/ pseudo; well_observed real >1 | ✓ |
| Leave all placement to planner | Too loose; redundancy targets need anchoring | |

**User's choice:** (Claude decided.) realistic_sparse = SCADA bus 0 + μPMU {17,24,30} + DER {17,21,24,32}
+ AMI {3,6,9,12,15,18,21,24,28,31} + pseudo rest. well_observed = SCADA bus 0 + μPMU 9-bus spread +
broad AMI + zero-injection {2,19}.
**Notes:** Exact membership = planner discretion within the targets.

---

## measurements bucket schema

| Option | Description | Selected |
|--------|-------------|----------|
| Generic `meas` point per reading | tags class/quantity/location/scenario/experiment(/phase); fields value, assumed_sigma | ✓ |
| Per-quantity measurements mirroring bus/line | More like System 1 but rigid for mixed classes | |

**User's choice:** (Claude decided.) Generic `meas` + re-published `event` topology measurement; no
`true_value` field (scoring oracle separate).
**Notes:** One bucket holds z + σ + topology for System 2.

---

## Config + module structure

| Option | Description | Selected |
|--------|-------------|----------|
| `measure_config.py` ACTIVE block + CLI overrides | Config-file primary switch, flags for sweeps | ✓ |
| Config file only (no flags) | Simpler but no batch sweeps | |
| CLI flags only | Contradicts user's "switch in a config file" | |

**User's choice:** (Claude decided.) `measure.py` + `measure_config.py`; `uv run measure`; config file
primary, CLI overrides optional.
**Notes:** User emphasized switching via a configuration file.

---

## Noise parameters

| Option | Description | Selected |
|--------|-------------|----------|
| Concrete per-class σ + outlier/instrument params | SCADA/μPMU/AMI/DER/pseudo/zero-inj defaults; f=0.03 15σ; AR(1) ρ=0.7 | ✓ |
| Single global σ | Unrealistic across classes | |

**User's choice:** (Claude decided.) Per-class σ table; gaussian_outliers f=0.03/15σ; instrument
quantization+bias+AR(1). true σ = assumed σ by default (separable).
**Notes:** Goal is to measure each noise model's effect on estimation.

---

## Sampling cadences

| Option | Description | Selected |
|--------|-------------|----------|
| Per-class decimation of native steps | day: AMI/4; fault: SCADA/2, AMI/10; PMU/DER every step | ✓ |
| Wall-clock-rate emulation | Needs artificial upsampling of 15-min day | |

**User's choice:** (Claude decided, consistent with the earlier spec-phase answer.)
**Notes:** snapshot = all classes every step.

---

## Dashboards

| Option | Description | Selected |
|--------|-------------|----------|
| Two new dashboards (day, fault) over measurements | observed states + true overlay + observed-vs-pseudo footprint | ✓ |
| One combined dashboard | Harder to read across regimes | |

**User's choice:** (Claude decided.) `ieee33-meas-day.json` + `ieee33-meas-fault.json`; existing
dashboards untouched.
**Notes:** —

---

## Claude's Discretion

- Exact AMI/μPMU bus membership within targets, ACTIVE-block field names, Flux query details, dashboard
  panel layout, quantization LSBs — planner/executor details within the locked intent.

## Deferred Ideas

- Live streaming transport (NATS / C37.118-over-UDP) over the `measurements` bucket — later/optional.
- System 2 (estimator) + estimate-vs-truth comparison dashboard — next phases.
- Jacobian/covariance observability index (ORACS observability) — a System 2 output.
