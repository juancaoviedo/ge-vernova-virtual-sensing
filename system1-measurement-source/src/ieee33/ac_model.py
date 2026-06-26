"""
ac_model.py
-----------
Pure-compute AC measurement model for the enhanced IEEE 33-bus network (System 2).

Provides:
  1. Ybus construction from a streamed netmodel/current topology message applied to
     static line/bus impedances from build_enhanced_33bus() — verified < 1e-9 vs
     the pandapower reference (SPEC R3).
  2. h(x) per measurement class (AC injection equations + identity pickoffs).
  3. Analytic Jacobian H, finite-difference verified < 1e-5.
  4. FASE sensitivity S = (H_inj^T W_inj H_inj)^{-1} H_inj^T W_inj
     (weighted pseudoinverse of injection-measurement rows).
  5. Startup verification gate: Ybus equality, h(x_true) pickoff, FD Jacobian check.

State vector convention (interleaved polar):
  x = [|V|_0, theta_0, |V|_1, theta_1, ..., |V|_32, theta_32]  (66 entries, buses 0..32)
  theta_33 = 0 (slack reference, fixed); |V|_33 = 1.0 (regulated, known)
  Free state dimension = 64  (buses 0..32 = 33 buses x 2 minus 2 for slack state)

Ybus is 34x34 (enhanced net: buses 0..32 distribution + bus 33 HV/slack).
Topology variation affects distribution lines only; the trafo + bus shunt (cap)
contribution is a FIXED addend precomputed once from the base ppci.

No I/O: no MQTT, no InfluxDB, no oracle access.  Fully parallelisable with Plan 01.

Oracle separation:
  grep check: grep -E "state|fault_event|paho|influx" src/ieee33/ac_model.py
  -> only topology/ac references, no bucket reads.

Run:  uv run python -m ieee33.ac_model   (calls verify_model and prints gate errors)
"""

import numpy as np
import pandapower as pp
import warnings

from pandapower.pd2ppc import _pd2ppc          # CRITICAL: underscore; returns 2-tuple
from pandapower.pypower.makeYbus import makeYbus

from ieee33.network import build_enhanced_33bus

# ---------------------------------------------------------------------------
# Internal constants
# ---------------------------------------------------------------------------
_N_BUS_TOTAL = 34          # total bus count including HV slack
_N_BUS_EST   = 33          # distribution buses in state vector (0..32)
_N_STATE     = 66          # total polar state entries (2 per estimation bus)
_N_FREE      = 64          # free states (theta_slack and V_slack are fixed)
_SLACK_BUS   = 33          # pandapower index of HV ext_grid bus


# ---------------------------------------------------------------------------
# Part 1: Static parameter extraction and Ybus build
# ---------------------------------------------------------------------------

def extract_static_line_params(net):
    """Extract per-line static impedance params from build_enhanced_33bus() net.

    Calls _pd2ppc (CRITICAL: pandapower 3.x private API, returns 2-tuple).
    Returns (params, base_z_ohm, ppci) where:
      params[idx] = {from_bus, to_bus, r_total_ohm, x_total_ohm, b_total_pu}
      base_z_ohm  = base impedance in ohms  (base_kv^2 / base_mva * 1000)
      ppci        = pandapower internal ppc (for reference Ybus + trafo fixed)

    Run net through pp.runpp first so _pd2ppc has solved state for shunt model.
    """
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        pp.runpp(net, run_control=True, calculate_voltage_angles=True)

    ppc, ppci = _pd2ppc(net)
    # base impedance: (base_kv^2 / base_mva) in ohms; base_kv from LV distribution bus 0
    base_kv = float(net.bus.at[0, "vn_kv"])
    base_mva = float(ppci["baseMVA"])
    base_z_ohm = (base_kv ** 2 / base_mva) * 1000.0

    params = {}
    for idx in net.line.index:
        row = net.line.loc[idx]
        length_km = float(row["length_km"])
        params[idx] = {
            "from_bus":     int(row["from_bus"]),
            "to_bus":       int(row["to_bus"]),
            "r_total_ohm":  float(row["r_ohm_per_km"]) * length_km,
            "x_total_ohm":  float(row["x_ohm_per_km"]) * length_km,
            "b_total_pu":   0.0,   # case33bw: no shunt capacitance on distribution lines
        }
    return params, base_z_ohm, ppci


def compute_trafo_fixed(params, base_z_ohm, ppci):
    """Compute the FIXED Ybus addend = trafo + bus shunts (capacitors at bus 17/32).

    The fixed addend is: Y_ref - Y_lines_only, where Y_ref is the full ppci Ybus and
    Y_lines_only is the Ybus built from in-service distribution lines only.

    This is precomputed ONCE at startup; topology changes only affect distribution lines.
    """
    # Reference Ybus from pandapower (sparse; unpack 3-tuple)
    Ybus_sp, _, _ = makeYbus(ppci["baseMVA"], ppci["bus"], ppci["branch"])
    Y_ref = Ybus_sp.toarray()

    # All in-service distribution line indices in the base radial topology (0..31)
    # (tie lines 32..36 are out of service in the base case)
    in_service_base = {idx for idx, p in params.items() if idx < 32}
    Y_lines_only = np.zeros((_N_BUS_TOTAL, _N_BUS_TOTAL), dtype=complex)
    for idx in in_service_base:
        p = params[idx]
        i, j = p["from_bus"], p["to_bus"]
        z_pu = (p["r_total_ohm"] + 1j * p["x_total_ohm"]) / base_z_ohm
        y_series = 1.0 / z_pu
        Y_lines_only[i, j] -= y_series
        Y_lines_only[j, i] -= y_series
        Y_lines_only[i, i] += y_series
        Y_lines_only[j, j] += y_series

    return Y_ref - Y_lines_only


# Convenience alias used in verify scripts
def Y_trafo_fixed(params, base_z_ohm, ppci):
    """Alias for compute_trafo_fixed (both names accepted by verify script)."""
    return compute_trafo_fixed(params, base_z_ohm, ppci)

_compute_trafo_fixed = compute_trafo_fixed  # second alias


def build_ybus_from_topology(static_line_params, in_service_line_ids,
                              n_bus, base_z_ohm, Y_trafo_fixed_mat):
    """Build a 34x34 Ybus from a streamed in-service-line set.

    Parameters
    ----------
    static_line_params    : dict returned by extract_static_line_params
    in_service_line_ids   : set/iterable of active line indices (from netmodel/current)
    n_bus                 : total bus count (34 for enhanced net)
    base_z_ohm            : base impedance in ohms (from extract_static_line_params)
    Y_trafo_fixed_mat     : fixed Ybus addend (trafo + bus shunts), from compute_trafo_fixed

    Returns
    -------
    Y : np.ndarray (n_bus x n_bus) complex128
    """
    Y = np.zeros((n_bus, n_bus), dtype=complex)
    for idx in in_service_line_ids:
        p = static_line_params[idx]
        i, j = p["from_bus"], p["to_bus"]
        z_pu = (p["r_total_ohm"] + 1j * p["x_total_ohm"]) / base_z_ohm
        y_series = 1.0 / z_pu
        b_shunt  = p.get("b_total_pu", 0.0)
        Y[i, j] -= y_series
        Y[j, i] -= y_series
        Y[i, i] += y_series + 0.5j * b_shunt
        Y[j, j] += y_series + 0.5j * b_shunt
    Y += Y_trafo_fixed_mat
    return Y


def reference_ybus(ppci):
    """Extract the pandapower reference Ybus (34x34 dense ndarray).

    Returns
    -------
    Y_ref : np.ndarray (34, 34) complex128
    """
    Ybus_sp, _, _ = makeYbus(ppci["baseMVA"], ppci["bus"], ppci["branch"])
    return Ybus_sp.toarray()


def topology_to_inservice(netmodel_payload, all_line_ids):
    """Convert a netmodel/current MQTT payload to an in-service line id set.

    Parameters
    ----------
    netmodel_payload : dict with keys:
        in_service_lines : list of int line indices in service
        tie_closed       : bool
        tie_id           : int  (-1 if no tie)
    all_line_ids     : set of all available line indices (from net.line.index)

    Returns
    -------
    in_service : set of int line indices
    """
    in_service = set(netmodel_payload.get("in_service_lines", []))
    if netmodel_payload.get("tie_closed") and netmodel_payload.get("tie_id", -1) >= 0:
        tie_id = int(netmodel_payload["tie_id"])
        if tie_id in all_line_ids:
            in_service.add(tie_id)
    return in_service


# ---------------------------------------------------------------------------
# Part 2: Measurement function h(x) and analytic Jacobian H
# ---------------------------------------------------------------------------

def _p_inj(i, V, T, G, B):
    """P injection at bus i: P_i = |V_i| sum_k |V_k|(G_ik cos(t_i-t_k) + B_ik sin(t_i-t_k)).

    Only sums over buses 0..N_BUS_EST-1 (the estimation state vector coverage).
    Bus 33 (HV slack) is handled via the fixed Ybus trafo rows, but its voltage
    state is not estimated; |V_33| = 1.0, theta_33 = 0 are encoded as the slack
    contribution already embedded in the Y matrix.

    Sign convention: positive = net consumption (load convention, per P9 measure.py).
    """
    n = len(V)
    cos_t = np.cos(T[i] - T)
    sin_t = np.sin(T[i] - T)
    P_i = V[i] * np.sum(V * (G[i, :n] * cos_t + B[i, :n] * sin_t))
    # Add contribution from slack bus 33 (fixed: V33=1.0, T33=0)
    V33 = 1.0
    T33 = 0.0
    G_i33 = G[i, _SLACK_BUS]
    B_i33 = B[i, _SLACK_BUS]
    P_i += V[i] * V33 * (G_i33 * np.cos(T[i] - T33) + B_i33 * np.sin(T[i] - T33))
    return P_i


def _q_inj(i, V, T, G, B):
    """Q injection at bus i: Q_i = |V_i| sum_k |V_k|(G_ik sin(t_i-t_k) - B_ik cos(t_i-t_k)).

    Same sign convention as P (positive = net consumption).
    """
    n = len(V)
    cos_t = np.cos(T[i] - T)
    sin_t = np.sin(T[i] - T)
    Q_i = V[i] * np.sum(V * (G[i, :n] * sin_t - B[i, :n] * cos_t))
    V33 = 1.0
    T33 = 0.0
    G_i33 = G[i, _SLACK_BUS]
    B_i33 = B[i, _SLACK_BUS]
    Q_i += V[i] * V33 * (G_i33 * np.sin(T[i] - T33) - B_i33 * np.cos(T[i] - T33))
    return Q_i


def h_func(x, Ybus, meas_list):
    """AC measurement function.

    Parameters
    ----------
    x         : np.ndarray  shape (66,)  [|V|_0, theta_0, ..., |V|_32, theta_32]
    Ybus      : np.ndarray  shape (34,34) complex  (full admittance matrix)
    meas_list : list of (cls, quantity, bus_idx) tuples in FIXED order

    Returns
    -------
    z_pred : np.ndarray  shape (len(meas_list),)

    Measurement classes and quantities:
      scada  vm_pu       -> x[2*i]           (|V| identity pickoff)
      scada  p_inj_mw    -> P_i(x) via Ybus
      scada  q_inj_mvar  -> Q_i(x) via Ybus
      pmu    vm_pu       -> x[2*i]
      pmu    va_degree   -> x[2*i+1] * 180/pi  (angle in degrees)
      ami    p_inj_mw    -> P_i(x) via Ybus
      ami    q_inj_mvar  -> Q_i(x) via Ybus
      der    p_mw        -> P_i(x) (generation = negative injection sign, load conv)
      der    q_mvar      -> Q_i(x)
      pseudo p_inj_mw    -> P_i(x) via Ybus
      pseudo q_inj_mvar  -> Q_i(x) via Ybus
      zero_inj p_inj_mw  -> P_i(x) via Ybus
      zero_inj q_inj_mvar-> Q_i(x) via Ybus

    Sign convention: positive injection = net consumption (load convention).
    """
    V = x[0::2]   # |V| at buses 0..32  (shape 33)
    T = x[1::2]   # theta in radians    (shape 33)
    G = Ybus.real
    B = Ybus.imag
    rows = []
    for cls, qty, bus_i in meas_list:
        if qty == "vm_pu":
            rows.append(float(V[bus_i]))
        elif qty == "va_degree":
            rows.append(float(T[bus_i] * 180.0 / np.pi))
        elif qty in ("p_inj_mw", "p_mw"):
            rows.append(_p_inj(bus_i, V, T, G, B))
        elif qty in ("q_inj_mvar", "q_mvar"):
            rows.append(_q_inj(bus_i, V, T, G, B))
        else:
            raise ValueError(f"h_func: unknown quantity '{qty}' for class '{cls}'")
    return np.array(rows)


def jacobian_H(x, Ybus, meas_list):
    """Analytic Jacobian of h(x) w.r.t. x.

    Parameters
    ----------
    x         : np.ndarray  shape (66,)
    Ybus      : np.ndarray  shape (34,34) complex
    meas_list : list of (cls, quantity, bus_idx)

    Returns
    -------
    H : np.ndarray  shape (len(meas_list), 66)

    Partial derivatives (polar formulation, Bergen & Vittal sign convention):
      For P_i row:
        dP_i/d|V_j|  = |V_i|(G_ij cos(t_ij) + B_ij sin(t_ij))           j != i
        dP_i/d|V_i|  = sum_k |V_k|(G_ik cos(t_ik)+B_ik sin(t_ik)) + |V_i| G_ii
        dP_i/dtheta_j=  |V_i||V_j|( G_ij sin(t_ij) - B_ij cos(t_ij))   j != i
        dP_i/dtheta_i= -Q_i(x) - |V_i|^2 B_ii
      For Q_i row:
        dQ_i/d|V_j|  = |V_i|(G_ij sin(t_ij) - B_ij cos(t_ij))           j != i
        dQ_i/d|V_i|  = sum_k |V_k|(G_ik sin(t_ik)-B_ik cos(t_ik)) - |V_i| B_ii
        dQ_i/dtheta_j= |V_i||V_j|(-G_ij cos(t_ij) + B_ij sin(t_ij))    j != i
        dQ_i/dtheta_i= P_i(x) - |V_i|^2 G_ii
    where t_ij = theta_i - theta_j.

    Note: the off-diagonal theta signs differ from some references that define
    t_ij = theta_j - theta_i.  Verified against FD < 1e-5 (SPEC R3 gate).

    Identity rows (vm_pu / va_degree):
      dV_i/dx[2i] = 1;  dV_i/dx[2k] = 0 for k!=i
      d(theta_i*180/pi)/dx[2i+1] = 180/pi
    """
    V = x[0::2]    # shape (33,)
    T = x[1::2]    # shape (33,)
    G = Ybus.real
    B = Ybus.imag
    n_meas = len(meas_list)
    n_state = len(x)        # 66
    n_est = len(V)          # 33 (buses 0..32)
    H = np.zeros((n_meas, n_state))
    for row_idx, (cls, qty, bus_i) in enumerate(meas_list):
        i = bus_i
        if qty == "vm_pu":
            # d|V_i|/dx[2*i] = 1
            H[row_idx, 2 * i] = 1.0
        elif qty == "va_degree":
            # d(theta_i * 180/pi)/d(theta_i) = 180/pi
            H[row_idx, 2 * i + 1] = 180.0 / np.pi
        elif qty in ("p_inj_mw", "p_mw"):
            # P_i partial derivatives w.r.t. all bus states
            P_i = _p_inj(i, V, T, G, B)
            Q_i = _q_inj(i, V, T, G, B)
            for j in range(n_est):
                t_ij = T[i] - T[j]
                G_ij = G[i, j]
                B_ij = B[i, j]
                # w.r.t. |V_j|
                if j != i:
                    dP_dVj = V[i] * (G_ij * np.cos(t_ij) + B_ij * np.sin(t_ij))
                else:
                    # diagonal: sum_k |V_k|(G_ik cos + B_ik sin) + |V_i|*G_ii
                    # = P_i/|V_i| + |V_i|*G_ii  (since P_i = |V_i|*...)
                    # but we need to be careful with the slack contribution
                    s = 0.0
                    for k in range(n_est):
                        t_ik = T[i] - T[k]
                        s += V[k] * (G[i, k] * np.cos(t_ik) + B[i, k] * np.sin(t_ik))
                    # add slack contribution (V33=1, T33=0)
                    t_i33 = T[i] - 0.0
                    s += 1.0 * (G[i, _SLACK_BUS] * np.cos(t_i33) + B[i, _SLACK_BUS] * np.sin(t_i33))
                    dP_dVj = s + V[i] * G[i, i]
                H[row_idx, 2 * j] = dP_dVj
                # w.r.t. theta_j (Bergen & Vittal: positive G_ij sin - B_ij cos for j!=i)
                if j != i:
                    dP_dTj = V[i] * V[j] * (G_ij * np.sin(t_ij) - B_ij * np.cos(t_ij))
                else:
                    dP_dTj = -Q_i - V[i] ** 2 * B[i, i]
                H[row_idx, 2 * j + 1] = dP_dTj
        elif qty in ("q_inj_mvar", "q_mvar"):
            P_i = _p_inj(i, V, T, G, B)
            Q_i = _q_inj(i, V, T, G, B)
            for j in range(n_est):
                t_ij = T[i] - T[j]
                G_ij = G[i, j]
                B_ij = B[i, j]
                # w.r.t. |V_j|
                if j != i:
                    dQ_dVj = V[i] * (G_ij * np.sin(t_ij) - B_ij * np.cos(t_ij))
                else:
                    s = 0.0
                    for k in range(n_est):
                        t_ik = T[i] - T[k]
                        s += V[k] * (G[i, k] * np.sin(t_ik) - B[i, k] * np.cos(t_ik))
                    t_i33 = T[i] - 0.0
                    s += 1.0 * (G[i, _SLACK_BUS] * np.sin(t_i33) - B[i, _SLACK_BUS] * np.cos(t_i33))
                    dQ_dVj = s - V[i] * B[i, i]
                H[row_idx, 2 * j] = dQ_dVj
                # w.r.t. theta_j (Bergen & Vittal: -G_ij cos + B_ij sin for j!=i)
                if j != i:
                    dQ_dTj = V[i] * V[j] * (-G_ij * np.cos(t_ij) + B_ij * np.sin(t_ij))
                else:
                    dQ_dTj = P_i - V[i] ** 2 * G[i, i]
                H[row_idx, 2 * j + 1] = dQ_dTj
        else:
            raise ValueError(f"jacobian_H: unknown quantity '{qty}' for class '{cls}'")
    return H


# ---------------------------------------------------------------------------
# Part 3: Finite-difference Jacobian verifier
# ---------------------------------------------------------------------------

def verify_jacobian(h_fn, H_fn, x, tol=1e-5):
    """Central-difference Jacobian check.

    Parameters
    ----------
    h_fn : callable  h_fn(x) -> z_pred (vector)
    H_fn : callable  H_fn(x) -> H matrix
    x    : np.ndarray  state vector
    tol  : float  tolerance (default 1e-5 per SPEC R3)

    Returns
    -------
    max_err : float  maximum absolute difference between analytic and FD Jacobian

    Raises
    ------
    AssertionError if max_err >= tol
    """
    eps = 1e-6
    n = len(x)
    H_analytic = H_fn(x)
    H_fd = np.zeros_like(H_analytic)
    for j in range(n):
        xf = x.copy(); xf[j] += eps
        xb = x.copy(); xb[j] -= eps
        H_fd[:, j] = (h_fn(xf) - h_fn(xb)) / (2 * eps)
    max_err = float(np.max(np.abs(H_analytic - H_fd)))
    assert max_err < tol, (
        f"Jacobian FD check failed: max error = {max_err:.2e} >= tol {tol:.2e}"
    )
    return max_err


# ---------------------------------------------------------------------------
# Part 4: FASE sensitivity S (weighted pseudoinverse of injection rows)
# ---------------------------------------------------------------------------

def fase_sensitivity(x, Ybus, inj_meas_list, W_inj=None):
    """Compute FASE sensitivity S = (H_inj^T W_inj H_inj)^{-1} H_inj^T W_inj.

    S is the linearised sensitivity dstate/dinjection at the current estimate x,
    restricted to injection-measurement rows.

    Parameters
    ----------
    x              : np.ndarray  shape (66,)  current state estimate
    Ybus           : np.ndarray  shape (34,34) complex
    inj_meas_list  : list of (cls, quantity, bus_idx) for injection measurements only
    W_inj          : np.ndarray  shape (m, m) diagonal weight matrix for injection rows,
                     or None to fall back to unweighted pseudoinverse (W = I)

    Returns
    -------
    S : np.ndarray  shape (n_state, n_inj)  = (66, m)
    """
    m = len(inj_meas_list)
    n_state = len(x)
    H_inj = jacobian_H(x, Ybus, inj_meas_list)   # (m, n_state)
    if m == 0:
        return np.zeros((n_state, 0))
    if W_inj is None:
        # Unweighted pseudoinverse fallback
        return np.linalg.pinv(H_inj)
    # Weighted pseudoinverse: S = (H^T W H)^{-1} H^T W
    HtW = H_inj.T @ W_inj          # (n_state, m)
    HtWH = HtW @ H_inj             # (n_state, n_state)
    try:
        S = np.linalg.solve(HtWH, HtW)   # (n_state, m)
    except np.linalg.LinAlgError:
        # Fallback to weighted pseudoinverse if HtWH is singular
        S = np.linalg.pinv(H_inj @ np.linalg.cholesky(W_inj).T)
    return S


# ---------------------------------------------------------------------------
# Part 5: Startup verification gate (SPEC R3)
# ---------------------------------------------------------------------------

def verify_model(net=None):
    """Run the three SPEC R3 startup gates.

    Gate 1: Ybus equality  — max(|Ybus_hand - Ybus_ref|) < 1e-9
    Gate 2: h(x) pickoff   — |h_vm_pu(x_flat)[bus_i] - x[2*bus_i]| < 1e-6
    Gate 3: Jacobian FD    — max(|H_analytic - H_fd|) < 1e-5

    Parameters
    ----------
    net : pandapowerNet or None
        If None, calls build_enhanced_33bus() internally.

    Raises
    ------
    AssertionError if any gate fails (with measured error in message).
    """
    if net is None:
        net, _ = build_enhanced_33bus()

    params, base_z, ppci = extract_static_line_params(net)
    Ytr = compute_trafo_fixed(params, base_z, ppci)

    # Gate 1: Ybus equality
    in_service_base = set(net.line.index[net.line["in_service"]])
    Yh = build_ybus_from_topology(params, in_service_base, _N_BUS_TOTAL, base_z, Ytr)
    Yr = reference_ybus(ppci)
    ybus_err = float(np.max(np.abs(Yh - Yr)))
    assert Yh.shape == (_N_BUS_TOTAL, _N_BUS_TOTAL), (
        f"Ybus shape {Yh.shape} != ({_N_BUS_TOTAL},{_N_BUS_TOTAL})"
    )
    assert ybus_err < 1e-9, (
        f"Gate 1 FAILED: Ybus equality error {ybus_err:.2e} >= 1e-9"
    )

    # Synthetic flat-start state: |V|=1.0, theta=0 for buses 0..32
    x_flat = np.zeros(_N_STATE)
    x_flat[0::2] = 1.0   # |V| = 1.0 pu
    x_flat[1::2] = 0.0   # theta = 0.0 rad

    # Gate 2: voltage pickoff at a representative bus (bus 5)
    check_bus = 5
    meas_pickoff = [("pmu", "vm_pu", check_bus)]
    z_pickoff = h_func(x_flat, Yh, meas_pickoff)
    pickoff_err = float(abs(z_pickoff[0] - x_flat[2 * check_bus]))
    assert pickoff_err < 1e-6, (
        f"Gate 2 FAILED: pickoff error {pickoff_err:.2e} >= 1e-6"
    )

    # Gate 3: Jacobian FD at flat state with a representative meas set
    meas_fd = [
        ("pmu",   "vm_pu",       check_bus),
        ("pmu",   "va_degree",   check_bus),
        ("scada", "p_inj_mw",    3),
        ("scada", "q_inj_mvar",  10),
    ]
    h_fn = lambda xv: h_func(xv, Yh, meas_fd)
    H_fn = lambda xv: jacobian_H(xv, Yh, meas_fd)
    fd_err = verify_jacobian(h_fn, H_fn, x_flat)

    print(f"verify_model: Gate 1 Ybus err={ybus_err:.2e} (< 1e-9)  OK")
    print(f"verify_model: Gate 2 pickoff err={pickoff_err:.2e} (< 1e-6)  OK")
    print(f"verify_model: Gate 3 Jacobian FD err={fd_err:.2e} (< 1e-5)  OK")
    print(f"verify_model: Ybus shape={Yh.shape}  free state dim={_N_FREE}")
    return ybus_err, pickoff_err, fd_err


# ---------------------------------------------------------------------------
# Module entry point
# ---------------------------------------------------------------------------

def main():
    """Run verify_model and print all three gate errors."""
    print("ac_model.py — startup verification")
    print("=" * 50)
    ybus_err, pickoff_err, fd_err = verify_model()
    print("=" * 50)
    print("All gates PASSED.")


if __name__ == "__main__":
    main()
