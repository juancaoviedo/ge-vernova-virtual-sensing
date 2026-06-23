"""
validate.py
-----------
Entry-point that runs two correctness gates for the IEEE 33-bus measurement source:

GATE 1 — Baran & Wu base-case anchor (D-14):
    Plain case33bw (no DER, no caps, no OLTC) must reproduce the published minimum
    voltage of ≈ 0.913 pu at pandapower bus 17 (article bus 18) within ±0.005 pu.
    This is the quantitative anchor ensuring the network model and impedances are
    correct before any enhancement is applied.

GATE 2 — Enhanced-net convergence + sanity gate:
    The fully enhanced net (DG + RPC shunts + OLTC) must converge at peak load
    (worst case, no DER scaling), with no NaN voltages, and OLTC tap within range.
    The 0.95–1.05 pu band is NOT required here — peak with unscaled DG at noon is
    the legitimate stress case; the per-step band gate lives in Plan 04.

Both gates accumulate failures for a consolidated fail-loud report.

Dependencies: pandapower, ieee33.config, ieee33.network
Run:          uv run validate
Effect:       Prints gate results to stdout; exits non-zero with details on failure.
"""

import sys

import pandapower as pp
import pandapower.networks as pn

from ieee33 import config
from ieee33.network import build_enhanced_33bus


def main() -> None:
    """Run both validation gates; exit 1 with detail on any failure."""

    failures: list[str] = []

    # ---- GATE 1: Baran & Wu base-case anchor (D-14) ----
    # Plain case33bw — no DER, no shunts, no OLTC transformer.
    # Published result: min voltage ≈ 0.913 pu at bus 18 (pandapower index 17).
    print("Gate 1: Baran & Wu base-case validation ...")
    try:
        net_bw = pn.case33bw()
        pp.runpp(net_bw, algorithm="nr", calculate_voltage_angles=True)
        if not net_bw.converged:
            failures.append("Gate 1 FAILED: case33bw base case did not converge")
        else:
            vm_min = float(net_bw.res_bus["vm_pu"].min())
            vm_min_bus = int(net_bw.res_bus["vm_pu"].idxmin())

            # Assert value is within tolerance of published Baran & Wu result
            if abs(vm_min - config.BARANWU_VMIN_PU) >= config.BARANWU_TOL:
                failures.append(
                    f"Gate 1 FAILED: vm_min={vm_min:.4f} pu at pp_bus={vm_min_bus} "
                    f"(article bus {vm_min_bus + 1}); expected "
                    f"{config.BARANWU_VMIN_PU:.3f} ± {config.BARANWU_TOL} pu"
                )
            elif vm_min_bus != config.BARANWU_VMIN_BUS:
                failures.append(
                    f"Gate 1 FAILED: vm_min at pp_bus={vm_min_bus} (article bus "
                    f"{vm_min_bus + 1}), expected pp_bus={config.BARANWU_VMIN_BUS} "
                    f"(article bus {config.BARANWU_VMIN_BUS + 1})"
                )
            else:
                print(
                    f"  Base case OK: vm_min={vm_min:.4f} pu at "
                    f"pp_bus={vm_min_bus} (article bus {vm_min_bus + 1})"
                )
    except Exception as exc:
        failures.append(f"Gate 1 FAILED with exception: {exc}")

    # ---- GATE 2: Enhanced-net convergence and tap-range sanity ----
    # Peak load (no DER profile scaling) is the most-stressed worst case.
    # We only require: converges, no NaN, tap within TAP_MIN..TAP_MAX.
    # The 0.95–1.05 band gate over the 96-step DER-driven run lives in Plan 04.
    print("Gate 2: Enhanced-net convergence and sanity ...")
    try:
        net_enh, trafo_idx = build_enhanced_33bus()
        pp.runpp(
            net_enh,
            algorithm="nr",
            calculate_voltage_angles=True,
            run_control=True,
        )

        if not net_enh.converged:
            failures.append("Gate 2 FAILED: enhanced net did not converge")
        else:
            nan_count = int(net_enh.res_bus["vm_pu"].isna().sum())
            if nan_count > 0:
                failures.append(
                    f"Gate 2 FAILED: {nan_count} NaN voltage(s) in res_bus"
                )
            else:
                vm_min_enh = float(net_enh.res_bus["vm_pu"].min())
                vm_max_enh = float(net_enh.res_bus["vm_pu"].max())
                # tap_pos is an input field (not in res_trafo) — read from net.trafo
                tap_pos = float(net_enh.trafo.at[trafo_idx, "tap_pos"])

                if tap_pos < config.TAP_MIN or tap_pos > config.TAP_MAX:
                    failures.append(
                        f"Gate 2 FAILED: tap_pos={tap_pos} outside "
                        f"[{config.TAP_MIN}, {config.TAP_MAX}]"
                    )
                else:
                    print(
                        f"  Enhanced net OK: converged, "
                        f"vm_min={vm_min_enh:.4f} pu, "
                        f"vm_max={vm_max_enh:.4f} pu, "
                        f"tap_pos={int(tap_pos)}"
                    )
    except Exception as exc:
        failures.append(f"Gate 2 FAILED with exception: {exc}")

    # ---- Final verdict ----
    if failures:
        print("\n--- VALIDATION FAILED ---", file=sys.stderr)
        for issue in failures:
            print(f"  {issue}", file=sys.stderr)
        sys.exit(1)

    print("VALIDATION OK")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nFATAL: {exc}", file=sys.stderr)
        sys.exit(1)
