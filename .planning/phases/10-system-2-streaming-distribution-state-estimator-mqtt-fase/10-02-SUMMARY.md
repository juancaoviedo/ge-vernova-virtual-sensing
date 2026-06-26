---
phase: 10-system-2-streaming-distribution-state-estimator-mqtt-fase
plan: "02"
subsystem: ac-measurement-model
tags: [ybus, h-function, jacobian, fase-sensitivity, dsse, power-systems]
dependency_graph:
  requires:
    - system1-measurement-source/src/ieee33/network.py  # build_enhanced_33bus static params
    - pandapower._pd2ppc + makeYbus                     # reference Ybus extraction
  provides:
    - system1-measurement-source/src/ieee33/ac_model.py # Ybus builder + h(x) + H + S + verify_model
  affects:
    - estimate.py (Plan 03/04) — imports ac_model for estimator predict/update
    - estimators.py (Plan 05) — uses h_func, jacobian_H, fase_sensitivity
tech_stack:
  added:
    - pandapower._pd2ppc (private 3.x API, 2-tuple return)
    - pandapower.pypower.makeYbus (3-tuple: Ybus_sparse, Yf, Yt)
    - Bergen & Vittal polar Jacobian formulas (DSSE standard)
  patterns:
    - Y_trafo_fixed addend: Yr - Y_lines_only (trafo pi-model + shunt capacitors)
    - Weighted pseudoinverse S = (Hinj^T W Hinj)^{-1} Hinj^T W (FASE sensitivity)
    - Central-difference FD verification at eps=1e-6 (verify_jacobian)
key_files:
  created:
    - system1-measurement-source/src/ieee33/ac_model.py   # 558 lines, pure compute
  modified: []
decisions:
  - "Y_trafo_fixed = Yr - Y_lines_only captures trafo pi-model + RPC shunt caps (buses 17/32) as one fixed addend — both are topology-invariant, simplifies topology variation to distribution lines only"
  - "Bergen & Vittal off-diagonal theta signs: dP_i/dT_j = +G_ij sin - B_ij cos; dQ_i/dT_j = -G_ij cos + B_ij sin (RESEARCH.md had opposite signs — deviation Rule 1 bug fix)"
  - "makeYbus returns 3-tuple (Ybus_sparse, Yf, Yt) — unpack [0] and call .toarray() to get dense ndarray"
  - "FASE sensitivity: weighted pseudoinverse with injection-only rows (per Open Q1 resolution); W_inj=None falls back to unweighted pinv(H_inj)"
metrics:
  duration: "~35 min"
  completed: "2026-06-26"
  tasks_completed: 2
  files_created: 1
  commits: 1
---

# Phase 10 Plan 02: AC Measurement Model Summary

Pure-compute AC measurement model for the IEEE 33-bus System 2 state estimator: 34x34 Ybus from streamed topology, h(x)/H/S, FASE sensitivity, and a startup gate that prints all three SPEC R3 errors.

## What Was Built

`system1-measurement-source/src/ieee33/ac_model.py` — 558 lines, no I/O, no MQTT, no InfluxDB.

### Task 1: Ybus-from-topology builder (SPEC R3 Gate 1)

- `extract_static_line_params(net)`: calls `_pd2ppc(net)` (pandapower 3.x private API, 2-tuple), extracts per-line static impedance params (`r_total_ohm`, `x_total_ohm`, `b_total_pu=0`), returns `(params, base_z_ohm, ppci)`.
- `compute_trafo_fixed(params, base_z_ohm, ppci)`: precomputes the fixed Ybus addend = `Yr - Y_lines_only`. This captures both the trafo pi-model (HV bus 33 -> LV bus 0) and the RPC shunt capacitors at buses 17 and 32 (encoded as ppci bus shunts). Both are topology-invariant, so only distribution lines change per topology message.
- `build_ybus_from_topology(static_line_params, in_service_line_ids, n_bus, base_z_ohm, Y_trafo_fixed_mat)`: assembles the 34x34 Ybus from in-service lines + fixed addend.
- `reference_ybus(ppci)`: unpacks makeYbus 3-tuple correctly (`Ybus_sp, _, _ = makeYbus(...)`), calls `.toarray()`.
- `topology_to_inservice(netmodel_payload, all_line_ids)`: maps netmodel/current MQTT payload to in-service set (closes tie if `tie_closed=True`).

**Verified:** Gate 1 error = 1.72e-11 < 1e-9 (SPEC R3). Faulted (line 7 out) and restored (tie 34 in) topologies change exactly 4 Ybus entries each (the 2×2 block for the affected endpoint buses).

### Task 2: h(x), Jacobian H, FASE sensitivity S, verify_model()

- `h_func(x, Ybus, meas_list)`: implements all measurement classes (vm_pu identity pickoff, va_degree with 180/pi conversion, P/Q injection via full AC equations including slack bus 33 contribution fixed at V=1, theta=0). Sign convention: positive injection = net consumption (load convention, per P9 measure.py).
- `jacobian_H(x, Ybus, meas_list)`: analytic polar Jacobian. Bergen & Vittal formulas (verified correct vs FD):
  - `dP_i/dT_j (j!=i) = |Vi||Vj|(G_ij sin(Tij) - B_ij cos(Tij))`
  - `dQ_i/dT_j (j!=i) = |Vi||Vj|(-G_ij cos(Tij) + B_ij sin(Tij))`
  - Diagonal terms: standard `-Q_i - Vi^2 B_ii` and `P_i - Vi^2 G_ii`.
- `verify_jacobian(h_fn, H_fn, x, tol=1e-5)`: central-difference check at eps=1e-6.
- `fase_sensitivity(x, Ybus, inj_meas_list, W_inj)`: weighted pseudoinverse `S = (Hinj^T W_inj Hinj)^{-1} Hinj^T W_inj`; falls back to `pinv(H_inj)` when W_inj=None.
- `verify_model(net)`: orchestrates all three gates; `main()` prints results.

**Verified:** Gate 2 pickoff err=0.00e+00 < 1e-6; Gate 3 FD err=3.35e-09 < 1e-5.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] RESEARCH.md off-diagonal theta Jacobian signs were inverted**
- **Found during:** Task 2 implementation — FD check returned error 1.47e+02
- **Issue:** RESEARCH.md Pattern 4 listed `dP_i/dT_j = |Vi||Vj|(-G_ij sin + B_ij cos)` and `dQ_i/dT_j = |Vi||Vj|(G_ij cos + B_ij sin)`. The correct Bergen & Vittal formulas (from first principles: d/dT_j[cos(T_i-T_j)] = +sin(T_i-T_j) because d(-T_j)/dT_j = -1 twice) give the opposite signs.
- **Fix:** Changed off-diagonal theta terms to `G_ij*sin(Tij) - B_ij*cos(Tij)` (P row) and `-G_ij*cos(Tij) + B_ij*sin(Tij)` (Q row). FD error dropped from 1.47e+02 to 3.35e-09.
- **Files modified:** `system1-measurement-source/src/ieee33/ac_model.py`
- **Commit:** a7e755c

**2. [Rule 1 - Bug] makeYbus returns 3-tuple, not a single matrix**
- **Found during:** Task 1 testing — `Yr.shape` raised AttributeError on a tuple
- **Issue:** PATTERNS.md showed `Ybus_ref = makeYbus(...)` as a single return value. In pandapower, `makeYbus` returns `(Ybus, Yf, Yt)` (bus, from-branch, to-branch admittance matrices).
- **Fix:** Unpacked as `Ybus_sp, _, _ = makeYbus(...)` and called `.toarray()` on the sparse result.
- **Files modified:** `system1-measurement-source/src/ieee33/ac_model.py`
- **Commit:** a7e755c

**3. [Rule 2 - Missing functionality] Y_trafo_fixed includes RPC shunt capacitors**
- **Found during:** Task 1 — Y_diff after subtracting only line contributions had 100 nonzero entries instead of expected 4 (trafo block)
- **Issue:** The ppci bus shunts (RPC capacitors at buses 17/32) are baked into the reference Ybus diagonal. These are fixed network elements (not topology-variable).
- **Fix:** `compute_trafo_fixed = Yr - Y_lines_only` captures all fixed addends (trafo + shunts) in one matrix. topology variation only affects distribution lines, which is the correct model.
- **Files modified:** `system1-measurement-source/src/ieee33/ac_model.py`
- **Commit:** a7e755c

## Known Stubs

None. The module is pure compute with no placeholder values.

## Threat Flags

None — `ac_model.py` is pure local compute with no network endpoints, no untrusted input, and no external calls.

## Self-Check: PASSED

- FOUND: `system1-measurement-source/src/ieee33/ac_model.py` (558 lines)
- FOUND: commit a7e755c
- `uv run python -m ieee33.ac_model` prints: Gate 1 err=1.72e-11, Gate 2 err=0.00e+00, Gate 3 err=3.35e-09 — all PASSED
