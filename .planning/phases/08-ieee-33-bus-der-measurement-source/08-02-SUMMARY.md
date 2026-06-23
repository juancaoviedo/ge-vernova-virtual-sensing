---
phase: 08-ieee-33-bus-der-measurement-source
plan: "02"
subsystem: system1-measurement-source
tags: [pandapower, ieee33-bus, DER, OLTC, validation, power-flow]
dependency_graph:
  requires: [08-01]
  provides: [network.py (build_enhanced_33bus), validate.py (uv run validate)]
  affects: [08-03 (sim.py imports build_enhanced_33bus), 08-04 (band gate references validate)]
tech_stack:
  added: []
  patterns:
    - "build_enhanced_33bus() pure builder returning (net, trafo_idx) tuple"
    - "OLTC-in-series: ext_grid moved to new hv_bus; trafo inserted hv_bus->bus_0"
    - "DiscreteTapControl on trafo_idx, side=lv, deadband 0.95-1.05 pu"
    - "p_mw_nameplate custom column on net.sgen for sim-loop profile scaling"
    - "fail-loud validate.py: accumulate failures list, exit 1 with detail"
key_files:
  created:
    - system1-measurement-source/src/ieee33/network.py
    - system1-measurement-source/src/ieee33/validate.py
  modified: []
decisions:
  - "OLTC inserted as series transformer between new feeder_hv bus and bus 0 (RESEARCH Pitfall 2)"
  - "p_mw_nameplate column added to net.sgen so sim loop can scale without re-deriving nameplate"
  - "validate.py Gate 2 does NOT require 0.95-1.05 band at peak with unscaled DG (legitimate worst case)"
  - "tap_pos read from net.trafo (not net.res_trafo) per RESEARCH Pitfall 6"
metrics:
  duration_seconds: 137
  completed_date: "2026-06-23"
  tasks_completed: 2
  files_created: 2
  files_modified: 0
---

# Phase 08 Plan 02: Enhanced IEEE 33-Bus Network Builder + Baran & Wu Validator Summary

**One-liner:** OLTC-in-series enhanced IEEE 33-bus PandaPower network (4 DG + 2 RPC shunts + DiscreteTapControl) with fail-loud Baran & Wu base-case anchor (0.9131 pu at bus 17 within ±0.005 tolerance).

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | build_enhanced_33bus() in network.py | 0d6537f | system1-measurement-source/src/ieee33/network.py |
| 2 | validate.py Baran & Wu anchor + enhanced-net gate | 88a12ef | system1-measurement-source/src/ieee33/validate.py |

## Verification Results

- `uv run validate` exits 0
- Gate 1: `Base case OK: vm_min=0.9131 pu at pp_bus=17 (article bus 18)` — within 0.005 tolerance of Baran & Wu 0.913 pu
- Gate 2: `Enhanced net OK: converged, vm_min=0.9632 pu, vm_max=1.0000 pu, tap_pos=0`
- Topology: tie-lines 32/33/34 open, 4 sgens at {17,21,24,32}, 2 negative-q shunts, 1 series feeder trafo, no NaN

## Decisions Made

- **OLTC-in-series architecture:** Following RESEARCH Pitfall 2, the ext_grid is moved from bus 0 to a new `feeder_hv` bus, and the transformer is created `hv_bus=feeder_hv, lv_bus=0`. This puts the OLTC in the power path so DiscreteTapControl can regulate bus 0 voltage.
- **p_mw_nameplate column:** Added `net.sgen["p_mw_nameplate"] = net.sgen["p_mw"]` after sgen creation so the sim loop (Plan 03) can scale by a 0–1 profile using `p_mw = p_mw_nameplate * profile_pu` without recalculating the nameplate value.
- **Gate 2 band relaxation:** Peak load with no DER scaling is the legitimate worst-case stress scenario; requiring 0.95–1.05 band here would be a false failure. The per-step band gate over the 96-step DER-driven run is deferred to Plan 04 per plan specification.
- **tap_pos read location:** Read from `net.trafo.at[trafo_idx, "tap_pos"]` (input field, updated by controller) not from `net.res_trafo` which has no tap_pos column (RESEARCH Pitfall 6 honored).

## Deviations from Plan

None — plan executed exactly as written.

## Known Stubs

None — both files are fully functional with no placeholder data, mock values, or TODO markers.

## Threat Surface Scan

No new network endpoints, auth paths, file access patterns, or schema changes introduced. Plan is pure host-side computation (no I/O, no DB, no user input).

## Self-Check: PASSED

- FOUND: system1-measurement-source/src/ieee33/network.py
- FOUND: system1-measurement-source/src/ieee33/validate.py
- FOUND: commit 0d6537f (feat(08-02): implement build_enhanced_33bus)
- FOUND: commit 88a12ef (feat(08-02): implement validate.py)
