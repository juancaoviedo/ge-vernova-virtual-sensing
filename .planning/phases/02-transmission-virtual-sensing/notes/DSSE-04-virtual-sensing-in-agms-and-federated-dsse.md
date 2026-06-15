# DSSE-04: Virtual Sensing inside AGMS & Federated Multi-Area DSSE

**For:** Oral rehearsal — speak the AGMS architectural placement and the federated-DSSE pattern
aloud; you must be able to draw the Inspector-scout → ORACS → Asset Portfolio Manager → CaCSM
pipeline from memory.
**Purpose:** Connect the DSSE mechanics to the AGMS patent architecture and to the JD's
"federated, decentralized" framing. The virtual-sensing estimator is not a standalone algorithm —
it is the sensing layer of a complete real-time control architecture, and understanding where it
sits and what it feeds is what separates a systems-aware candidate from a signal-processing
specialist.

---

## <3-min say-aloud version

> "In AGMS, virtual sensing is the seeing capability of the entire architecture. The Director's
> patent describes a layered system: Field Agent Devices at the edge running Inspector scouts,
> ORACS cells coordinating a group of those FADs, and a GridWideMind / GridWideEye intelligence
> layer above. The virtual-sensing estimator — the DSSE / FASE filter we've been studying — runs
> as an **Inspector scout** on each FAD, locally, producing a posterior state estimate $(\hat x, P)$
> for that FAD's section of the feeder.
>
> The posterior covariance $P$ is what the Asset Portfolio Manager (module 1300) gates on. It
> computes the ORACS Observability index from $P$: how well does the current measurement set
> observe the feeder? If observability is sufficient — covariance below a threshold — the
> continuous voltage-control **CaCSM** is armed. In Worked Example 2 of the patent, rooftop solar
> causes overvoltage at an unmetered node during midday. No fault alarm fires. No human sees
> anything. The virtual sensor, running recursively on the FAD, knows — because it maps the
> posterior injection estimate through LinDistFlow and propagates the covariance, landing above
> the 1.05 pu ceiling with a confidence interval that triggers the CaCSM reactive power response.
>
> The federated structure is how this scales. Each FAD / ORACS cell estimates its sub-feeder
> independently, using local telemetry and local topology. Where two cells share a boundary node,
> they exchange only the **boundary-node posterior state** $(\hat x_{boundary}, P_{boundary})$ —
> not raw measurements, not full feeder models. This is federated DSSE: each cell estimates
> locally, shares posteriors at boundaries, and the full feeder state falls out of the composition.
> Raw measurements never cross the cell boundary. This satisfies both the JD's 'federated,
> no central coordination' requirement and the patent's 'self-forming federations' architecture."

---

## 1. AGMS Architectural Placement

### The Inspector Scout ($s_i$) on the Field Agent Device (FAD)

The DSSE / FASE filter runs as an **Inspector scout** $s_i$ on a **Field Agent Device** — a
grid-edge compute platform (substation gateway, DER controller, RTU with edge compute) that
hosts one or more scouts.

**What the Inspector scout does:**
- Ingests local telemetry: head SCADA from the ORACS gateway, inverter self-reports via
  IEEE 1547 / 2030.5, AMI from the utility AMI head-end, EV charger events via OCPP/MQTT
- Maintains the recursive FASE state $(\hat x, P)$ for its sub-feeder section
- Produces posterior estimates at each update cycle (which may differ by measurement channel)
- Publishes posterior state and covariance to the ORACS coordination layer

**Why locally on the FAD:**
- Reduces WAN bandwidth (posteriors, not raw streams)
- Keeps running in island mode when WAN connectivity drops
- Enables edge-local control (volt/VAR response without round-trip to cloud)
- Scales horizontally: add more FADs, not a bigger central server

---

## 2. The ORACS Observability Index and Asset Portfolio Manager 1300

**ORACS (Operating Region and Asset Control Scheme)** is the coordination cell in AGMS —
a logical group of FADs covering a section of the distribution network. Each ORACS maintains
a **GridWideMind / GridWideEye** view of its sub-network.

**The Observability index** is derived from the posterior covariance $P$ of the DSSE:

- High $P$ (large covariance) = poorly observed = low Observability index
- Low $P$ (tight posterior) = well observed = high Observability index
- The mapping is operationalized by the **Asset Portfolio Manager** (module 1300 in the patent)

**How 1300 uses it:**

1. Read current posterior covariance $P$ from each Inspector scout
2. Compute Observability index for each sub-feeder section
3. Gate downstream decisions:
   - If Observability index sufficient: arm the voltage-control **CaCSM** (see below)
   - If Observability index degraded (comms gap, sensor failure): AGMS enters a degraded-mode
     response — widen control margins, issue a sensor-health check, log for Learning Engine
4. Expose Observability index to GridWideMind for fleet-level situational awareness

**Interview sentence:** "The posterior covariance IS the ORACS Observability index — the filter's
uncertainty quantification maps directly to the AGMS gate for every downstream control action."

---

## 3. The CaCSM Voltage-Control Trigger (Worked Example 2 in the Patent)

**CaCSM** = Continuous-action Control-Scheme Module (the patent's name for the real-time
volt/VAR control loop triggered by virtual sensing). The scenario from Worked Example 2:

**Setup:** A residential distribution feeder with rooftop solar (PV) at several nodes. One node
with heavy PV is unmetered — no AMI, no inverter self-report (legacy system). At midday, cloud
cover lifts and PV output surges.

**Without virtual sensing:** No sensor at the unmetered node. No fault alarm fires (the
overvoltage is not extreme enough to trip protection relays). The voltage at that node rises
above 1.05 pu — a violation — but the SCADA operator sees only the feeder-head reading,
which looks normal. The violation persists, stressing grid equipment and potentially causing
customer-side issues.

**With virtual sensing (FASE on the FAD):**
1. Inspector scout $s_i$ maintains the FASE state $\hat x = [\hat P_1, \hat P_2, \ldots]$.
2. The inverter at bus 1 self-reports its output surge; the head SCADA shows load dropping
   (net flow toward substation reversing). The FASE filter attributes the excess generation
   to the unmetered PV node via Kirchhoff coupling.
3. Posterior injection $\hat P_{PV}$ goes strongly negative (generation); posterior voltage via
   LinDistFlow: $V_{PV} \approx 1.000 + |\hat P_{PV}| \times$ (sensitivity coefficient) → above 1.05 pu.
4. Propagated covariance: $\sigma_{V_{PV}}$ small enough that the upper $2\sigma$ bound is
   above 1.05 pu.
5. The Asset Portfolio Manager 1300 checks Observability index → sufficient → arms CaCSM.
6. CaCSM dispatches a reactive power absorption command to a nearby smart inverter with available
   capacity — via IEEE 1547 / 2030.5 interface.
7. Voltage restored without the operator ever knowing there was an issue.

**What this demonstrates:**
- Virtual sensing provides visibility where sensors do not exist
- The covariance is the gate — CaCSM only fires when observability is sufficient to act confidently
- The action is the **simulate-before-commit** step (patent claim 3): before dispatching, the
  ORACS runs a power-flow simulation from the posterior state and confirms the reactive injection
  will fix the overvoltage without creating violations elsewhere

**Interview sentence:** "Worked Example 2 is the money scenario — rooftop solar overvoltage at an
unmetered node, no alarm, only virtual sensing knows. The covariance gates the CaCSM. The simulate-
before-commit confirms the fix won't create new violations. This is the complete virtual-sensing
pipeline in action."

---

## 4. Simulate-Before-Commit (Patent Claim 3)

Before dispatching any control command (reactive power, load curtailment, DER setpoint change),
the AGMS architecture requires a **simulate-before-commit** step:

1. Take the current posterior $(\hat x, P)$ from the DSSE
2. Apply the proposed control action in a fast power-flow simulation
3. Check: does the simulated result satisfy all voltage, current, and thermal constraints, with
   probability exceeding a threshold (accounting for the state uncertainty $P$)?
4. If yes: dispatch the control command
5. If no: revise the control action, re-simulate, or escalate to the operator

**Connection to Juan's CVXPY MPC:** The CVXPY model-predictive control in OSED/HEMS is
structurally identical — take the current state estimate, propagate through the model (simulate),
find the optimal control action subject to constraints, dispatch. The grid version adds the
probabilistic safety check using $P$, which is exactly what MPC does with chance constraints.

**Interview sentence:** "Simulate-before-commit is model-predictive control with a probabilistic
safety gate derived from the posterior covariance. I've built that pipeline in CVXPY for building
control; the distribution grid version replaces the RC thermal model with LinDistFlow."

---

## 5. Federated Multi-Area DSSE

<!-- greppable tag: federated multi-area DSSE -->

**The problem:** A distribution feeder can span many kilometers and hundreds of nodes. Running
a single DSSE for the entire feeder would require all measurements to flow to one point, a large
$H$ matrix, and centralized processing — defeating island-mode safety and limiting scalability.

**The federated solution:** Partition the feeder into **operating cells**, each corresponding to
one ORACS. Each cell's Inspector scout estimates its local sub-feeder independently.

**Where cells meet: boundary-node state exchange**

At the boundary between two ORACS cells, there is a **shared boundary node** (typically a
substation bus or a switching node). The two adjacent cells' scouts publish their **posterior state
and covariance** at that boundary node:

$$(\hat x_{boundary}, P_{boundary})_A \quad\text{and}\quad (\hat x_{boundary}, P_{boundary})_B$$

These two posteriors are then fused (information-form KF combination, or Dempster-Shafer, or a
simple weighted combination) to produce a consistent boundary estimate. Each cell then updates
its internal state to be consistent with the agreed boundary condition.

**What does NOT cross the boundary:**
- Raw measurements from either cell's interior
- Full internal state of either cell
- The cell's $H$ matrix or topology model

Only the boundary posterior — a compressed, privacy-preserving summary. This is the
"decentralized, no central coordination" requirement in the JD, and the "self-forming federations"
pattern from the AGMS patent.

**Properties of federated DSSE:**

| Property | Why it matters |
|----------|---------------|
| No central data aggregation | WAN bandwidth: raw streams from hundreds of nodes not needed centrally |
| Island-mode safety preserved | Each cell keeps running if inter-cell comms drop; only boundary posteriors are affected |
| Horizontal scalability | Add ORACS cells; no central compute scaling |
| Privacy / cybersecurity | Raw telemetry does not cross cell boundaries — reduced attack surface |
| Consistency at boundaries | Shared posterior fusion ensures the two cells agree on the boundary-node state |

**Interview sentence:** "Federated DSSE means each ORACS cell estimates its sub-feeder locally and
only shares boundary-node posteriors with neighbors — raw measurements never cross the cell
boundary. It satisfies 'federated, no central coordination' and it's what makes island-mode safety
scale across a large distribution territory."

---

## 6. Asset-Health Awareness (Brief — Cross-Reference KAL-04)

Distribution transformer hot-spot (IEEE C57.91) and line temperature (IEEE 738, KAL-04) are the
**asset-health virtual sensors** — distinct from the network state-estimation problem above but
architecturally parallel: an unmeasured quantity (winding hot-spot, conductor temperature) is
inferred from telemetry (load current, ambient) via a physics ODE in a scalar EKF.

In the AGMS context:
- The scalar asset-health EKF runs as a separate Inspector scout (or a sub-module of the DSSE scout)
- Its posterior temperature estimate and covariance feed the Asset Portfolio Manager 1300
- 1300 computes Remaining Useful Life (RUL) and schedules maintenance / derating decisions

For the worked mechanics, see KAL-04 (IEEE 738 EKF) and the asset-health section of TVS-04.
**Do not re-derive here** — one paragraph reference is the correct depth.

---

## 7. Consolidated Bridges to Juan's Work

<!-- greppable tag: Bridge to your work -->

| AGMS / DSSE-04 concept | Juan's work | How to say it |
|----------------------|------------|--------------|
| Inspector scout on FAD (edge runtime) | OSED edge runtime | "OSED is the FAD substrate — edge compute, local state, runs in island mode. I've shipped edge-runtime inference at the building level; the distribution FAD is the same class of system." |
| Temporal prior / FASE `Bu` term | HEMS edge-ML load/PV forecasting | "My HEMS forecasting produces the calibrated probabilistic load/PV forecasts that would populate $v$ and calibrate time-indexed $Q$." |
| Simulate-before-commit (patent claim 3) | CVXPY MPC in OSED/HEMS | "CVXPY MPC is simulate-before-commit — propagate state, find optimal control action, dispatch only if constraints satisfied. The grid version adds LinDistFlow instead of RC thermal and a probabilistic safety gate from $P$." |
| Federated, no central coordination | SI-MAPPER distributed ontology inference | "SI-MAPPER infers structured state from distributed, heterogeneous signals without a central data pool — the same federated inference pattern." |
| Learning Engine calibration | Baseline-consumption error analysis (CV) | "My production analysis of baseline-estimation errors across billions of data points from multiple substations is the Learning Engine loop — detect residual patterns, recalibrate the prior model." |

---

## Quick-Recall Card (Recite Before the Interview)

1. **Inspector scout $s_i$:** DSSE/FASE filter running locally on the FAD; ingests local telemetry; produces $(\hat x, P)$ for its sub-feeder section.
2. **ORACS Observability index:** derived from posterior $P$; computed by Asset Portfolio Manager 1300; gates all downstream control.
3. **CaCSM trigger:** Observability sufficient AND $(\hat x, P)$ shows constraint near/past limit → dispatch reactive power, DER setpoint, etc.
4. **Worked Example 2:** unmetered rooftop-solar overvoltage; no alarm; only virtual sensing knows; CaCSM fixes it via reactive absorption at a neighboring inverter.
5. **Simulate-before-commit (claim 3):** take posterior $(\hat x, P)$, simulate proposed control action via LinDistFlow, check probabilistic constraint satisfaction before dispatching.
6. **Federated DSSE:** each ORACS cell estimates locally; only boundary-node posteriors exchanged; raw measurements never cross cell boundary.
7. **Federated properties:** no central aggregation; island-mode safe; horizontally scalable; reduced attack surface; boundary consistency from posterior fusion.
8. **Asset health (brief):** IEEE 738 (KAL-04) and C57.91 — scalar EKFs on the same FAD; posteriors feed 1300 for RUL/maintenance decisions. See KAL-04.
9. **Island-mode safety:** recursive structure keeps $(\hat x, P)$ flowing during WAN outage; $P$ inflates honestly; AGMS responds to degraded observability rather than data absence.
10. **My bridges:** OSED = FAD substrate; HEMS forecasting = temporal prior; CVXPY MPC = simulate-before-commit; SI-MAPPER = federated structural prior; baseline-error analysis = Learning Engine.

---

*Sources: AGMS patent (Director; Inspector scout s_i, Field Agent Device, ORACS, GridWideMind /
GridWideEye, Asset Portfolio Manager 1300, CaCSM, Worked Example 2 overvoltage, simulate-before-
commit claim 3, Learning Engine, self-forming federations); GE Vernova JD R5043890 (virtual
sensing, federated, decentralized, distribution, phase angles); KAL-03 (FASE feeder walk — the
worked example that feeds AGMS); KAL-04 (IEEE 738 asset-health EKF — the scalar companion);
IEEE 1547-2018 / IEEE 2030.5 (smart inverter control interfaces for CaCSM dispatch); LinDistFlow
(Baran & Wu 1989); 01-RESEARCH.md / 02-RESEARCH.md verified architecture notes.*
