# Appendix — From Devices to Network State: the Virtual Sensing Module

## Purpose & How This Connects to the First Appendix

The companion appendix —
[Distribution-Level State-Information Sources](appendix-distribution-observability-sources.html) —
enumerated the *inputs*: every device, sensor, system, and protocol that can observe a
distribution (or transmission) grid, tagged by ORACS observability and reachability. **This
appendix is the other half: how those inputs become the *state of the network*** through the
virtual-sensing module the job description asks for — *"infer critical power grid parameters
(voltage stability, phase angles, line temperature, asset health) from limited edge sensor
data … using Kalman filters, state estimation."*

It is a **working design**, not a finished one: the architecture spine is settled, but three
decisions are deliberately left **open** (see [Open Decisions](#open-decisions)) because they
depend on the target feeder and hardware and should be made per deployment.

> **One sentence:** the module reconstructs one latent object — the complex nodal voltage
> state of the network — from a sparse, multi-rate, partly-untrustworthy mix of real
> measurements, model constraints, and forecasts, and emits that state **plus its
> uncertainty**, which is exactly the ORACS *observability index* and the prerequisite for
> the ORACS *dispatchability of DERs/microgrid*.

## The Object We Reconstruct, and the Four Outputs

The **state** is `x = {|V|∠θ}` — complex voltage at every node (per-phase for distribution;
see [D1](#open-decisions)). Once `x` is known with the network model, everything else is a
derived computation. The JD's four named virtual sensors are *outputs* of `x`, not separate
estimators:

| JD target | Reconstructed from |
|---|---|
| **Phase angles** | µPMU where present (direct); everywhere else θ is a *solved state variable* — "virtual phasors" from Kirchhoff + magnitudes |
| **Voltage stability** | the reconstructed `|V|` profile + sensitivities (dV/dQ, P-V/Q-V margins) |
| **Line temperature** | line current + ambient weather → an IEEE-738 thermal EKF (a second, small estimator) |
| **Asset health** | condition signals (DGA, PD) fused with loading *from* the state estimate → prognostics |

Three of the four are *derived from `x`*, not measured. That is the whole point of "virtual"
sensing. **Scope note:** the machinery is the same for transmission and distribution (the
patents are T&D-general), but transmission is already well-observed — the module earns its
keep at the **distribution / DER edge**, where most of the state must be reconstructed from
priors.

## Module 1 & 2 — Load and DER Forecasting (the predict step *and* the pseudo-measurements)

Two forecasting modules supply what the sensors don't directly give: a **load** forecaster
and a **DER-generation** forecaster. They are essential, but their role is widely
mis-stated, so three corrections matter:

- **Zero-injection nodes are NOT forecast.** A junction with no load and no generation is
  *known* to inject zero. It enters the estimator as a **virtual measurement with near-zero
  variance — the HIGHEST weight in the problem** (effectively an equality constraint), not a
  low-weight pseudo-measurement. Keep three buckets distinct: *real measurements*,
  *virtual/zero-injection (high weight)*, *pseudo-measurements (low weight)*.
- **The forecaster's *inputs* are not pseudo-measurements.** AMI, DER-inverter telemetry, and
  line/PQ sensors are **real measurements** wherever they exist (medium–high weight). The
  forecaster *learns* from their history, but at runtime a node *with* telemetry uses the
  measurement; only a node *without* telemetry uses the forecast as its pseudo-measurement.
  The pseudo-measurement fills the **gaps between** real sensors.
- **"Low weight" is true for the pseudo-measurement role — and misleading.** In a
  forecasting-aided estimator the forecast is also the **predict step**: the state-transition
  model that propagates `x̂(t|t-1)` between sparse real updates. That is the *prior mean of the
  whole state* — the backbone of the recursive filter, not a low-weight afterthought. So each
  forecaster does **double duty**: (a) low-weight pseudo-measurements at unmeasured nodes;
  (b) the high-value predict step for *every* node.

**Net-injection subtlety.** AMI meters *net* power (load − behind-meter PV), so "load" and
"DER" partly collapse into one observed **net injection** with invisible PV inside — handled
explicitly in [Thread B](#thread-b-behind-meter-net-injection-disaggregation).

### So should we even build the forecasters? Yes — but right-size them.

The "low weight ⇒ low value" intuition is the trap. Build them, because:

1. **Without pseudo-measurements the network is *unobservable* — there is no solution at all.**
   A low-weight measurement that is the *only* thing constraining a node is what makes the
   gain matrix non-singular. Low weight ≠ low importance.
2. **The forecast *is* the predict step** — its quality sets tracking quality between real
   measurements.

But because the pseudo-measurement weight is low (σ of roughly 20–50%), the estimator does
**not** need a high-accuracy forecast. Start simple (persistence / historical load-shape +
clear-sky PV); graduate to heavy ML only if residuals demand it. The forecaster's *value
scales with how under-observed the feeder is* — everything on a rural feeder, marginal on a
dense-AMI urban one.

## Module 3 — Real-Time Topology (query it; don't rebuild it)

State estimation is undefined without the as-operated connectivity model, and it must be
**real-time** (switching changes the radial configuration constantly). The right move is to
**consume** the model, not read raw SCADA:

- The **ADMS** (Advanced Distribution Management System) already owns as-operated topology via
  its **topology processor / network model service**, exposed over **CIM (IEC 61968/61970)**
  or a vendor API. The big hook: **GE Vernova's own GridOS / ADMS (PowerOn)** is exactly this
  — the module consumes *their* network model. (Others: Schneider EcoStruxure ADMS, Hitachi
  Network Manager, Siemens Spectrum Power, Oracle, Survalent, OSI monarch.)
- **ETAP Real-Time** can be a real-time SE/load-flow source where it's deployed; **CYME /
  CYMDIST** is primarily the *validated offline* model you initialize from, not the real-time
  authority.
- **Edge / island-mode nuance:** when the WAN to the ADMS drops, the cell can't query the
  central model. So the edge module keeps a **cached network model** and tracks *local* switch
  changes in real time via **IEC 61850 GOOSE / DNP3** at the substation, applying them to the
  cache. ADMS = authoritative base model (when connected); local GOOSE/DNP3 = real-time delta
  (always). This is the AGMS "operating cell survives loss of WAN" pattern made concrete.

## Module 4 — The Estimator: Kalman/FASE, not WLS-snapshot

### Why a traditional WLS snapshot is insufficient

Classical Weighted Least Squares SE is a *static snapshot*: take one batch of (assumed
simultaneous) measurements, minimize weighted residuals, solve for `x`. It breaks at the edge
three ways:

1. **Under-observability** — at any single instant there aren't enough real measurements; the
   gain matrix is singular without heavy pseudo-measurements, and a one-shot solve discards
   all temporal information.
2. **Asynchrony / multi-rate** — PMU at ms, SCADA at seconds, AMI every 15 min. WLS has no
   principled way to fuse measurements taken at *different times*; freezing a "snapshot" and
   pretending they're simultaneous is wrong exactly when the state moves fast (DER ramps,
   clouds).
3. **No prediction** — WLS can't propagate state through a gap. When a feeder goes quiet it
   has nothing.

WLS isn't discarded — it's the **update math** embedded inside the recursive filter.

### What Kalman/FASE adds

Kalman = the WLS update **plus** a time model:

- **Predict step** — propagate the state with a transition model + process noise `Q`. In
  **FASE (Forecasting-Aided State Estimation)** that transition model is the load/DER forecast
  (Modules 1 & 2). This is why the forecasters are the engine, not an accessory.
- **Update step** — when a measurement arrives, correct the prior. This *is* the WLS math
  (same `h(x)`, same `R` weighting).

### Multi-rate fusion — why it's critical and how it's achieved

Because edge data is inherently multi-rate, the estimator is **asynchronous by construction**:
run **predict** on a clock (propagate from the forecast), and fire an **update** *whenever any
measurement arrives*, using only that source's rows of `H` and `R`. A PMU corrects the state
ms-by-ms; SCADA every few seconds; AMI applies a slow correction every 15 min; a DER inverter
whenever it reports. Between arrivals the forecast propagates the state, so an estimate always
exists and is always current. A snapshot estimator would either **waste the fast PMU data** or
**stall waiting on the slow AMI** — multi-rate fusion lets each source contribute at its native
cadence.

### One coupled estimator — not a bank of per-signal filters

The single most important architectural point:

- The state `x` is the **whole network's nodal voltages**, and **one coupled estimator** runs
  over all of it. Each incoming measurement updates the *coupled* state through the network
  model — a measurement at node A informs node B via the admittance matrix (Kirchhoff). That
  cross-coupling **is the value**. Filtering each signal independently and feeding "clean"
  signals to a power flow would destroy the coupling and the model constraints that make
  virtual sensing work. **The Kalman filter *is* the network-wide state estimator; it is not a
  pre-filter in front of a power flow.**
- **Where the power flow lives:** inside the measurement function `h(x)`. The nonlinear
  `P,Q = f(V,θ)` relations and the `Ybus` admittance matrix *are* `h(x)`; the EKF linearizes
  them via the Jacobian `H` (or the UKF samples sigma points). You are **not** "running a power
  flow then Kalman-filtering its output" — the filter's measurement model *embeds* the
  power-flow equations. The right mental model is **a continuous solver for the power-flow
  state that updates when measurements arrive** — the estimate is always current (continuous),
  corrections are event-driven (on arrival).
- **Do you pre-filter each signal with its own Kalman? Generally no.** What you need before a
  measurement enters the update is **validation/gating** (range checks, rate-of-change limits,
  stuck-sensor/flatline detection, timestamp + quality flags, unit/scaling) — that is
  measurement *validation*, not a state estimator. After the update, do **residual-based
  bad-data detection** (chi-square test on normalized residuals) to catch liars that passed the
  gate. Per-signal *denoising* is a narrow exception for a specifically noisy/fast channel (a
  raw PMU/waveform stream) and is used cautiously — over-smoothing adds latency, hides real
  dynamics, and corrupts the noise statistics `R`. **Default: raw measurement → validation gate
  → single network-wide SE update → residual χ² check.** Not a filter bank.

### The stack, in one picture

```
forecast (load + DER)  ──►  PREDICT  x̂(t|t-1)        ← FASE: the forecast IS the transition model
                                  │
incoming measurements ──► validate/gate ──► UPDATE ──► x̂(t|t)   ← WLS math inside; h(x) = power-flow eqns
   (PMU ms / SCADA s / AMI 15min / DER)        │
                                          residual χ² bad-data check
                                                  │
                                          x̂ + covariance ──► voltage stability · angles · line temp · health
                                                              └─ covariance = ORACS observability index
                                                                 → enables safe DER/microgrid dispatchability
```

## Three Deep Threads (and how each touches the architecture)

### Thread A — Filter core (EKF vs UKF vs EnKF) and the state formulation underneath it

The filter choice sits *downstream* of a bigger one: the **state formulation**. Distribution
is three-phase and unbalanced (single-phase laterals, untransposed lines, mutual coupling), so
the honest state is **per-phase complex voltages** (~3× the state), and there is a second
choice — **node-voltage** (polar `|V|,θ`) vs **branch-current** (BCSE), the latter often
better-conditioned for *radial* feeders. Then the core:

- **EKF** — Jacobian linearization; cheapest, but needs an analytic/numeric `H` (painful for
  three-phase `h`) and degrades when far from the operating point — i.e. under low
  observability, its worst case.
- **UKF** — no Jacobian; push `2n+1` sigma points through the true `h(x)`. Robust far from the
  operating point (the low-observability regime), at ~`2n+1` evaluations of `h` per step. Use a
  square-root UKF for stability. Sensible **default for distribution.**
- **EnKF** — Monte-Carlo ensemble; scales to very large networks, parallelizes well, handles
  mild non-Gaussianity; sampling-error in the covariance. For scale.
- Corner case: where PMUs make `h` **linear** in rectangular coordinates → a plain linear KF,
  cheap and optimal, over the PMU-observable subset.

**Architecture impact:** commit to a **3-phase per-phase state** (modifies A1 — see
[D1](#open-decisions)); make the **filter a pluggable core** behind a stable predict/update
interface (refines A3); and note that filter × state-size × edge-compute are now one linked
choice driven by feeder archetype (couples to A9).

### Thread B — Behind-meter net-injection disaggregation

AMI meters **net** power (load − behind-meter PV). Treat net reads as load and you
under-estimate gross load and stay **blind to the PV that is actually driving the voltage
rise** — the exact quantity the voltage-stability target and the AGMS DER-dispatchability story
depend on. Disaggregation recovers the two hidden components (gross load, gross PV) from the
one observed net + side information (irradiance/weather, PV nameplate from interconnection
records, time-of-day, nearby metered PV as a reference). It shares its PV physics with the
Module-2 DER forecaster, so they should be one block.

**Architecture impact:** adds a **DER/PV estimation block (A10)** doing double duty — forecast
(predict input) *and* current disaggregation (update pseudo-measurement) — upgrading Module 2;
optionally grows the state if disaggregation is done by **state augmentation** (see
[D2](#open-decisions)); splits A5's "DER pseudo-measurement" into gross-load and gross-PV.

### Thread C — Federated / multi-area DSSE

You never run one giant estimator for a whole utility. Partition by substation/feeder: each
**edge cell** estimates its own area, and areas are stitched at boundaries (tie-lines, shared
buses) into a coherent system estimate. This maps almost one-to-one onto the patents:
operating cell = estimation area, federation = multi-area coordination, scout-master =
coordinator, island mode = an area running on stale boundary conditions when cut off. Two
families: **hierarchical** (local estimators + a coordinator reconciles boundaries) and
**peer-to-peer** (neighbors exchange only boundary-bus estimates + covariance and iterate to
consensus via ADMM / consensus+innovation / gossip). Peer-to-peer shares boundary state, never
raw measurements — matching the patent's POV "no raw data leaves the cell," and surviving WAN
loss.

**Architecture impact:** clarifies A1 ("one coupled estimator" was always *per area*); adds the
**federation layer (A11)** — a boundary-state exchange interface + a coordination mode (see
[D3](#open-decisions)); adds a **graceful-degradation spec** (on WAN/neighbor loss, use
last-known boundary conditions as priors with inflated covariance and keep running — island
mode); makes the observability index **per-cell**, assembled into the system view. Optional
extra layer: **federated *learning*** of the forecasters across cells (share model weights, not
load data) — the JD's "federated data pipelines," tied to Phase 5.

## Running Architecture Spec (A1–A11)

| # | Element | Status |
|---|---|---|
| **A1** | State = nodal voltages, **3-phase per-phase**; one coupled estimator *per area* | spine + open [D1] |
| **A2** | Predict step = load+DER forecast (FASE); process noise from forecast uncertainty | spine |
| **A3** | Update step = WLS math; power flow embedded in `h(x)`; **pluggable filter core** (EKF/UKF/EnKF) | spine, core deferred |
| **A4** | Multi-rate asynchronous: predict on a clock, update on each measurement arrival | spine |
| **A5** | Inputs = real measurements + zero-injection (high-weight virtual) + pseudo-measurements (low-weight forecasts) | spine |
| **A6** | Validation/gating in; residual χ² bad-data out; no per-signal Kalman bank | spine |
| **A7** | Topology from ADMS/CIM (GridOS) + local GOOSE/DNP3 deltas, cached for island mode | spine |
| **A8** | Output = x̂ + covariance; covariance = ORACS observability index; enables DER dispatchability | spine |
| **A9** | Placement = substation edge, island-capable; compute coupled to filter × state size | spine |
| **A10** | **DER/PV estimation block** — forecast + behind-meter disaggregation | new (Thread B) |
| **A11** | **Federation layer** — boundary-state exchange + island degradation; per-cell observability | new (Thread C) |

## Open Decisions

These three are **deliberately left open** — they are real forks that depend on the target
feeder (archetype), the available hardware, and the deployment posture, and committing too
early would over-fit the design. Each should be decided per deployment, not globally.

### D1 — State formulation: three-phase **node-voltage** vs **branch-current**

- **Node-voltage (polar `|V|,θ`)** — the textbook formulation; natural for mixed
  meshed/radial networks and for voltage-centric outputs (voltage stability); Jacobian is
  standard.
- **Branch-current (BCSE)** — state is branch currents; often **better-conditioned for radial
  distribution** and reduces some nonlinearity, but is awkward where the network meshes and for
  direct voltage outputs.
- **Why open:** the choice is driven by feeder archetype (radial rural vs meshed urban) and
  interacts with the filter core (Thread A) and edge compute. **Highest-leverage decision** —
  it shapes `h(x)`, the Jacobian, observability conditioning, and the compute footprint.

### D2 — Disaggregation placement: **pre-SE pseudo-measurement** vs **in-filter state augmentation**

- **Pre-SE** — a standalone disaggregator turns one net measurement into two pseudo-measurements
  (gross load, gross PV) feeding the pseudo layer. Cleaner separation, simpler estimator,
  weaker coupling to real anchors.
- **State augmentation** — add per-node DER output as extra *states* the filter estimates
  jointly, using network coupling + weather as drivers and real inverter telemetry as anchors.
  More principled and accurate where anchors exist, but **grows the state** (couples back to D1
  and edge compute) and needs enough anchors to be observable.
- **Why open:** depends on DER density and how much real inverter telemetry exists to anchor the
  augmented states.

### D3 — Federation mode: **hierarchical** vs **peer-to-peer**

- **Hierarchical** — local estimators + a cloud/ADMS coordinator reconciles boundaries.
  Simpler to reason about and converge, but depends on the coordinator being reachable.
- **Peer-to-peer (consensus)** — neighbors exchange boundary estimates and iterate (ADMM /
  consensus+innovation / gossip); no central coordinator; shares boundary state not raw data;
  **survives WAN loss** and matches the AGMS federated-cell / island-mode model.
- **Why open:** a trade between convergence simplicity (hierarchical) and resilience +
  patent-alignment (peer-to-peer). The AGMS architecture leans peer-to-peer, but a first
  deployment may start hierarchical for tractability.

> **What is NOT open:** the spine — FASE predict + multi-rate asynchronous update, one coupled
> network-wide estimator with the power flow embedded in `h(x)`, validation-in / χ²-out,
> topology from ADMS + local deltas, and output = state + covariance = ORACS observability
> index. The three open decisions tune *how* the spine is realized for a given feeder; they do
> not change the spine.

## Where This Leaves the Deployment Proposal

This appendix + the companion
[device inventory](appendix-distribution-observability-sources.html) together give the two
halves of the virtual-sensing deployment proposal: **what we can observe** (devices →
measurement classes) and **how it becomes state** (devices → estimator → ORACS observability
index → safe DER dispatchability). The remaining proposal work is to instantiate this against a
specific feeder archetype and resolve D1–D3 for that case.
