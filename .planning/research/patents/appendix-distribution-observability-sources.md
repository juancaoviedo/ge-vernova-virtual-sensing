# Appendix — Distribution-Level State-Information Sources for Virtual Sensing

## Purpose & ORACS Framing

This appendix is the source-side companion to the AGMS patent walkthrough. The AGMS
formation pipeline can only form an operation loop out of assets it can actually
**see** and **reach** — the first two of the five ORACS operational indexes the
Asset Portfolio Manager verifies (WO 2024/211758, para [0209]):

- **Observability** — *can we see this asset's / node's state?* → what it measures, and what part of the system state it reveals.
- **Reachability** — *can we communicate with / command it?* → the protocol and comms path that contacts it.

The virtual-sensing module exists precisely because, on a real distribution feeder,
**observability is sparse**: the number of direct measurements is far smaller than the
number of states (complex nodal voltages on every node, flows on every branch). The
module's job is to **reconstruct the full state** from whatever heterogeneous subset of
sources a given feeder happens to expose — exactly the under-observability gap named in
the parent patent's worked example ("*one sensor is offline (fails observability) … or
AGMS leans on virtual sensing to estimate the missing state*").

So the right way to scope a deployment is **not** "which sensors do I install" but
**"given the sources this feeder already has, where do I place the module and what does
it fuse?"** This appendix first enumerates *every* state-information source that exists
at the distribution level — exhaustively, across 14 tiers — then classifies that universe
four ways to drive the deployment proposal.

> **Scope note.** Not every feeder has every source. The inventory is the *universe of
> possibility*; the classifications (especially the feeder archetypes) are where the
> realism lives. Each source is tagged by what it **observes** and how you **reach** it —
> the ORACS observability/reachability pair.

## How to Read This Inventory

Each tier is a table with three columns:

- **Source** — the device, system, or data feed.
- **Observes (state)** — the physical quantity / network state it contributes to reconstruction.
- **Reach (protocol)** — how the module contacts it (the ORACS reachability answer).

Tiers run top-down through the grid: substation head → feeder/line → high-resolution
phasor → metering edge → DER → then the model, statistical, enterprise, environmental,
event, condition, comms, protocol, and non-utility layers that surround the electrical
measurements.

## Tier 1 — Substation Measurement & Automation

The richest, most reliable observability point; the electrical **head** of every feeder
and the natural reference (slack) node for state estimation.

| Source | Observes (state) | Reach (protocol) |
|---|---|---|
| RTUs (Remote Terminal Units) | Aggregated analog/digital points at the substation | DNP3, IEC 60870-5-101/104 |
| IEDs / protective relays (SEL, ABB, GE Multilin) | V, I, P, Q, frequency, breaker status, fault current, oscillography | IEC 61850 (MMS/GOOSE), DNP3, Modbus |
| Bay / feeder controllers | Per-feeder V, I, P, Q, power factor | IEC 61850, DNP3 |
| Substation SCADA / automation system | All station analogs + status, consolidated | DNP3, IEC 61850, OPC-UA |
| Bus voltage & frequency measurement | Substation bus &#124;V&#124;, f (reference node) | IEC 61850, DNP3 |
| Power-transformer monitors | LTC tap position, oil/winding temp, DGA, loading | IEC 61850, Modbus, OPC-UA |
| Breaker / recloser status & counters | Open/closed, trip counts, wear | DNP3, IEC 61850 GOOSE |
| Digital Fault Recorders (DFR) | High-res fault waveforms | COMTRADE files, FTP |
| Sequence-of-Events Recorders (SER) | Time-tagged event ordering | DNP3, file pull |
| Merging units (IEC 61850 process bus) | Digitized Sampled Values (SV) of I/V | IEC 61850-9-2 SV |
| Station DC / battery monitors | DC-bus health (sustainability input) | Modbus, DNP3 |

## Tier 2 — Feeder & Distribution-Line Field Devices

The mid-feeder layer — sparse today, and the biggest growth area for observability.

| Source | Observes (state) | Reach (protocol) |
|---|---|---|
| Line-post / line-mounted sensors (Sentient, Lindsey, Sensus) | Line current, voltage, conductor temp, sometimes phase angle | RF mesh, cellular, DNP3 |
| Faulted Circuit Indicators (FCIs) / fault-passage indicators | Fault passed / didn't (fault-location narrowing) | RF, cellular, LoRa |
| Reclosers + recloser controls (SEL-651, G&W, S&C) | V, I, P, Q, status, trip/lockout | DNP3, IEC 61850 |
| Automated switches / tie switches | Open/closed (real-time topology), sometimes metering | DNP3, IEC 61850 GOOSE |
| Sectionalizers | Count/operate state | DNP3 |
| Capacitor-bank controllers | In/out status, local V/VAR, neutral current | DNP3, IEEE 2030.5 |
| Voltage-regulator controllers (step regulators) | Tap position, regulated voltage, load current | DNP3, Modbus |
| Pad-mount switchgear / sensored elbows | Cable-section V/I, status | DNP3, RF |
| Distribution line monitors / PQ line sensors | Waveform, sag/swell, harmonics mid-feeder | cellular, MQTT |
| Dynamic Line Rating (DLR) / conductor-temp sensors | Conductor temp, sag, ampacity headroom | RF, cellular |

## Tier 3 — High-Resolution / Phasor Measurement

Where **angle** observability comes from — enables Kalman/observer-based estimation
(Phase 01) and turns a feeder from barely-observable to well-conditioned.

| Source | Observes (state) | Reach (protocol) |
|---|---|---|
| PMUs (transmission-grade) | Synchrophasors: &#124;V&#124;∠θ, &#124;I&#124;∠θ, f, ROCOF (GPS-timed) | IEEE C37.118.2 |
| **Micro-PMUs / D-PMUs** (distribution) | High-precision *small* voltage-angle differences across feeders | C37.118, IEEE 2664 |
| PDCs (Phasor Data Concentrators) | Time-aligned multi-PMU streams | C37.118, IEEE 1344 |
| Point-on-wave / continuous waveform sensors | Full waveform capture (sub-cycle events) | proprietary, MQTT |
| Power-quality meters (ION, SEL, Fluke) | Harmonics, flicker, sag/swell, unbalance | Modbus, DNP3, OPC-UA |

## Tier 4 — Advanced Metering Infrastructure (AMI)

The single largest observability multiplier at the grid edge — millions of nodal
voltage and energy points, one per service transformer / customer.

| Source | Observes (state) | Reach (protocol) |
|---|---|---|
| AMI smart meters (Itron, L&G, Sensus) | Interval kWh, kW, **service voltage**, sometimes Q/PF | RF mesh / cellular FAN → head-end |
| Meter voltage telemetry | Nodal &#124;V&#124; at the customer (dense voltage observability) | AMI head-end → MDMS |
| Last-gasp / power-down notifications | Outage detection / topology truth | AMI FAN |
| AMI head-end system | Consolidated meter reads | vendor API, MultiSpeak |
| Meter Data Management System (MDMS) | Validated, time-aligned interval data | MultiSpeak, CIM, SQL/API |
| C&I interval / revenue meters | High-accuracy P, Q at large loads | DNP3, Modbus, OPC-UA |
| Submeters / net meters | Behind-meter generation & sub-load split | Modbus, IEEE 2030.5 |

## Tier 5 — Distributed Energy Resources (DER) Telemetry

Two-way-flow sources — simultaneously **observation points** and **controllable assets**
(they score on all five ORACS indexes, not just observability).

| Source | Observes (state) | Reach (protocol) |
|---|---|---|
| Smart inverters (IEEE 1547-2018) | P, Q, V, status, ride-through state | **IEEE 2030.5**, SunSpec Modbus |
| PV-plant telemetry | DC/AC output, irradiance, availability | Modbus, 2030.5, SunSpec |
| Battery storage (BESS) | SoC, P, Q, thermal, cycle state | Modbus, 2030.5, DNP3 |
| EV chargers / EVSE | Charging load, session, V2G capability | OCPP, 2030.5, OpenADR |
| Microgrid controllers | Island status, net interchange, local dispatch | DNP3, 2030.5 |
| DERMS | Aggregated DER state + control headroom | CIM, 2030.5, vendor API |
| VPP / aggregator platforms | Third-party fleet DER visibility | OpenADR, REST API |
| Building EMS / HEMS | Behind-meter load & flexibility | BACnet, MQTT, 2030.5 |

## Tier 6 — Topology & Network-Model Data

Not a sensor, but **mandatory** for state reconstruction: DSSE is undefined without the
connectivity model — this is the skeleton the measurements hang on, and it is itself an
observability artifact (you must *know the graph* before you can estimate states on it).

| Source | Provides | Reach (protocol) |
|---|---|---|
| GIS (Geographic Information System) | As-built connectivity, asset locations, phasing | CIM (IEC 61968/61970), Esri API |
| CIM network model | Nodes, branches, impedances, ratings | IEC 61970/61968 CIM/XML |
| Real-time switch/recloser/tie status | Live topology (radial config of the moment) | DNP3, SCADA |
| Phase-identification data | Which phase each segment/customer is on | analytics + GIS |
| Line/cable impedance & length parameters | Z for the power-flow equations | GIS, planning model |
| Transformer ratings / impedances / connections | Branch parameters, Δ/Y | EAM, GIS |
| Customer↔transformer↔phase mapping | Load aggregation to nodes | CIS + GIS + analytics |
| Planning models (OpenDSS, CYME, Synergi, Milsoft) | Validated offline network + base loads | file export, API |

## Tier 7 — Pseudo-Measurements & Derived / Statistical Inputs

What fills the **unobservable** nodes — low-weight inputs central to DSSE math. This is
the gap the virtual-sensing module is built to close.

| Source | Provides | Reach (protocol) |
|---|---|---|
| Historical load profiles per customer class | Estimated nodal load shapes (residential/commercial/industrial) | data warehouse |
| Billing / CIS energy allocation | Energy → estimated nodal load | CIS, SQL |
| Load-research statistical estimates | Class-average demand with variance | analytics |
| Transformer-level load from aggregated AMI | Estimated load behind each service transformer | MDMS rollup |
| Weather-driven load & solar forecasts | Nodal demand / PV nowcast | forecast API |
| Zero-injection / virtual measurements | Known-zero injection at no-load/no-gen nodes (near-exact constraint) | derived from model |
| Prior state estimate / forecast | The predict step of a Kalman filter (Phase 01) | internal |

## Tier 8 — Control-Center & Enterprise Data Systems

The integration layer — where field data is fused, stored, and served. In AGMS terms,
this is the **asset database + POV-file plane** (Data Management patent, WO 2024/211800).

| System | Role in state reconstruction |
|---|---|
| ADMS (Advanced Distribution Management System) | Hosts DSSE; integrates SCADA + OMS + DMS |
| OMS (Outage Management System) | Outage extent → topology / load truth |
| Distribution SCADA master | Real-time analog/status acquisition |
| Historian (AVEVA / OSIsoft PI) | Time-series archive of all telemetry |
| GIS / CIM model server | Connectivity & parameters (Tier 6) |
| MDMS / AMI head-end | Meter data (Tier 4) |
| DERMS / forecasting engines | DER state + forecasts (Tiers 5, 7) |
| EAM / asset management | Ratings, condition, maintenance state |

## Tier 9 — Environmental / Exogenous Data

Drives load, generation, and thermal limits — improves both observability and the
pseudo-measurement priors.

| Source | Observes (state) | Reach (protocol) |
|---|---|---|
| Weather stations | Temp, wind, humidity, irradiance → load, solar, DLR | API, MQTT |
| Weather forecast services | Forward load / solar drivers | NWS + commercial API |
| Satellite / sky-imager irradiance | Solar nowcasting | commercial API |
| Lightning detection networks | Fault correlation / cause | API |
| Wildfire / vegetation / fuel-moisture data | Risk & de-rating context | API |
| GNSS / GPS time | Synchrophasor & Sampled-Values time-sync | 1-PPS, IRIG-B, PTP |
| Geomagnetic data | GIC on transformers | API |

## Tier 10 — Protection & Event / Fault Data

Event-triggered observability — sparse in time, very high information when it fires.

| Source | Observes (state) | Reach (protocol) |
|---|---|---|
| Relay event records / oscillography | Fault waveforms, pickup/trip | COMTRADE, file pull |
| Fault current magnitude & direction | Directional fault detection | DNP3, IEC 61850 |
| Travelling-wave fault locators | Precise fault distance | proprietary, file |
| Arc-flash / incipient-fault detectors | Pre-failure signatures | proprietary |
| Sequence-of-events (SER) | Precise event ordering | DNP3, file |

## Tier 11 — Asset-Condition / Non-Electrical Sensing

Feeds the *sustainability* and *stability* ORACS indexes — health, not just electrical state.

| Source | Observes (state) | Reach (protocol) |
|---|---|---|
| Transformer monitors | DGA, oil/winding temp, acoustic, partial discharge | IEC 61850, Modbus |
| Cable / switchgear PD monitors | Partial-discharge / incipient insulation failure | proprietary, Modbus |
| Thermal imaging (fixed + drone) | Hot-spot detection | image pipeline |
| Acoustic / vibration sensors | Mechanical degradation | IoT, MQTT |
| Conductor tilt / sag / galloping sensors | Mechanical line state | RF, cellular |
| Pole-tilt / structural sensors | Structural integrity | LoRa, cellular |
| LiDAR & aerial/satellite imagery | Vegetation, sag, encroachment | batch / file |

## Tier 12 — Field Communications / IoT Substrate

You cannot observe what you cannot reach — this is **how** every tier above is contacted,
and it *is* the ORACS reachability layer made physical.

| Source | Role |
|---|---|
| Field Area Network: RF mesh (Itron / L&G / Sensus) | AMI + DA backhaul |
| Private LTE / public LTE / 5G | DA device + DER backhaul |
| Fiber | Substation + critical-asset backhaul (lowest latency) |
| Power-line carrier (PLC) / BPL | Legacy line communications |
| LoRaWAN | Long-range, low-power field sensors |
| Cellular IoT (NB-IoT, LTE-M) | Battery field sensors |
| DA gateways / field routers / **edge compute nodes** | The FAD / "operating cell" host where a virtual-sensing scout actually runs |

## Tier 13 — Protocols (the Contact Vocabulary)

The ORACS reachability answer ultimately reduces to *"which of these does the asset speak,
and can the module talk it?"*

```
DNP3                       SCADA / DA field telemetry
IEC 61850 (MMS/GOOSE/SV)   substation automation + process bus
IEC 60870-5-101/104        European SCADA telemetry
IEEE C37.118               synchrophasor streaming (PMU/µPMU)
IEEE 2030.5 / SEP2         DER monitoring & control
SunSpec Modbus             inverter register model
Modbus RTU/TCP             generic industrial devices
OpenADR                    demand response
OCPP                       EV charging
OPC-UA                     historian / SCADA integration
MQTT                       IoT / edge messaging
MultiSpeak                 utility application integration
ICCP / TASE.2              control-center to control-center
CIM (IEC 61968/61970)      network-model & data exchange
BACnet                     building systems (behind-meter)
```

## Tier 14 — Non-Utility / Proxy / Crowdsourced Data

Low-trust, high-coverage observability of last resort — useful when the electrical
sources are dark.

| Source | Observes (state) | Reach (protocol) |
|---|---|---|
| Customer outage reports (IVR, app, call center) | Outage extent / location | CRM, OMS |
| Smart-home / IoT device status | Indirect outage signal | vendor API |
| EV telematics | Third-party charging behavior | aggregator API |
| Social media / crowdsourced outage maps | Coarse event location | scraping, API |
| Traffic / occupancy proxies | Load-pattern inference | API |

---

## Classification 1 — Observability-Tier Prioritization

Rank the source *classes* by **state-reconstruction leverage per unit of cost/effort** —
the question a deployment must answer first. The lever is not "install more sensors"; it
is "harvest the observability you already have before buying hardware."

| Source class | Reconstruction leverage | Typical availability today | Marginal cost to add | Priority |
|---|---|---|---|---|
| Substation head (Tier 1) | **Anchor** — pins the reference node + feeder-head injection | Present on virtually every feeder | — (already there) | **A — assume present** |
| Topology / CIM model (Tier 6) | **Prerequisite** — no estimation without the graph | Present (GIS), quality varies | low (data quality work) | **A — must-have** |
| AMI voltage (Tier 4) | Very high — dense nodal &#124;V&#124; across the feeder | Widespread & growing | low (data already collected) | **A — harvest first** |
| DER smart-inverter telemetry (Tier 5) | High & growing — observes the volatile injections | Medium (rising fast with 1547/2030.5) | low–medium (integration) | **B — high-yield** |
| Pseudo-measurements (Tier 7) | Low per-point but **free** and fills every unobservable node | Always derivable | ~zero | **A — always include** |
| Feeder line sensors / reclosers (Tier 2) | Medium-high — mid-feeder flow/voltage | Sparse | medium–high (hardware) | **B — selective** |
| µPMU / D-PMU (Tier 3) | **Highest per sensor** — direct angle observability | Rare | high (hardware + comms) | **C — targeted** |
| Environmental (Tier 9) | Improves priors (load/solar/thermal) | Available | low | **B — cheap uplift** |
| Asset-condition (Tier 11) | Feeds sustainability/stability, not nodal state | Variable | medium | **C — health, not state** |

**Rule of thumb for the proposal:** the cheapest observability gains come from *data you
already own* — AMI voltage, DER inverter telemetry, and a clean topology model — fused
with free pseudo-measurements. New hardware (line sensors, µPMUs) is a **targeted**
investment to fix specific ill-conditioned pockets the data-harvest can't reach.

## Classification 2 — Mapping to DSSE Measurement Classes

A state estimator does not care *what* a source is, only *which measurement class* it
contributes. Every source above collapses into one of six classes, each with a distinct
treatment in the estimator (measurement function `h(x)`, weight `1/σ²` in `R`).

| DSSE class | Form in the estimator | Weight / covariance | Latency | Fed by tiers |
|---|---|---|---|---|
| **Real (direct) measurements** | P, Q, &#124;V&#124;, &#124;I&#124; → nonlinear `h(x)`, WLS/EKF | High (small σ) | sub-second | 1, 2 |
| **Synchrophasor measurements** | &#124;V&#124;∠θ, &#124;I&#124;∠θ — *linear* in rectangular coords | Highest (smallest σ); gives angle observability | ms (C37.118) | 3 |
| **AMI measurements** | Nodal &#124;V&#124;, interval kWh → energy/voltage pseudo-real | Medium-high but **latent** (time-aligned) | minutes–hours | 4 |
| **Virtual measurements** | Zero-injection at no-load/no-gen nodes | Near-exact (σ→0; treated as equality constraint) | static | 6, 7 |
| **Pseudo-measurements** | Forecast/billing load injections | **Low (large σ)** — fills unobservable nodes so the system is solvable | static/forecast | 5, 7, 9 |
| **Topology & parameters** | Connectivity, Z, switch status, phasing | Structural — defines `h(x)` itself, not a measurement | event/static | 6 |

**Why this matters for virtual sensing:** a feeder is *unobservable* by the classical
criterion (measurements ≪ states). DSSE becomes solvable only by adding **pseudo-measurements**
(large σ) to reach redundancy ≥ 1, then letting the **real / PMU / AMI** measurements pull
the estimate toward truth and the **virtual zero-injection** constraints tighten it. The
virtual-sensing module *is* the engine that fuses these classes (Phase 01 EKF/UKF, Phase 02
FASE/WLS) — this classification is the contract between the source inventory and that engine.

## Classification 3 — Deployment Placement by ORACS Reachability

Where the virtual-sensing module physically **runs** is dictated by *which sources it can
reach in time* — the ORACS reachability index applied to the module itself. Three
candidate placements, mapped to what each can actually contact:

| Placement | Reaches in real time | Runs | ORACS property |
|---|---|---|---|
| **Substation-edge compute** (FAD at the substation, RTU/IED-adjacent) | Tiers 1–3 over substation LAN (IEC 61850, DNP3, C37.118); local Tier 2 over FAN | Per-feeder DSSE at SCADA cadence | **Island-capable** — survives WAN loss; default placement |
| **Feeder / field FAD** (pole-top, DA gateway, operating cell) | Local Tier 2 + nearby Tier 5 DER over FAN/cellular | Localized sub-state estimation for a feeder section | **Most survivable** — runs cut off from substation; deep-feeder observability |
| **ADMS / cloud tier** | Tiers 4 (AMI/MDMS, latent), 6/8 (model, historian), aggregated 5 | System-wide DSSE across feeders | **Not survivable, not real-time** — coordination & backfill, not control-loop |

**Source → placement reachability matrix:**

| Source tier | Substation edge | Field FAD | ADMS / cloud |
|---|---|---|---|
| 1 Substation | ✓ real-time | partial | ✓ (latent) |
| 2 Feeder/line | ✓ (FAN) | ✓ local | ✓ (latent) |
| 3 Phasor/µPMU | ✓ (C37.118) | partial | ✓ (PDC) |
| 4 AMI | ✗ (head-end only) | ✗ | ✓ |
| 5 DER | partial (FAN) | ✓ local | ✓ (DERMS) |
| 6 Topology/model | cached | cached | ✓ source |
| 7 Pseudo | computed locally | computed locally | ✓ source |

**Proposal takeaway:** put the **real-time DSSE at the substation edge** (it reaches the
high-value Tiers 1–3 and stays alive in island mode — the AGMS resilience property),
optionally push **localized estimation to field FADs** for deep-feeder/DER-dense
sections, and use the **ADMS/cloud tier for cross-feeder coordination and AMI backfill**
(the slow, latent sources). This mirrors the AGMS operating-cell hierarchy directly:
edge decides and acts; cloud coordinates and remembers.

## Classification 4 — Feeder Archetypes

Which sources a feeder *actually* has depends on its type. Three representative archetypes
bound the realistic deployment space.

| Dimension | **Rural / long radial** | **Suburban / DER-heavy** | **Urban / networked** |
|---|---|---|---|
| Substation head (Tier 1) | ✓ | ✓ | ✓ |
| Line sensors / reclosers (Tier 2) | few / none | some reclosers + caps/regs | reclosers, automated switches |
| Phasor (Tier 3) | none | rare | occasional µPMU + PQ meters |
| AMI (Tier 4) | sparse | **dense** | **dense** |
| DER (Tier 5) | minimal | **heavy** (rooftop PV, EV, BESS) | moderate (commercial PV, storage) |
| Comms (Tier 12) | weak (cellular/RF) | good (RF mesh + cellular) | strong (fiber) |
| Topology (Tier 6) | simple radial, long | radial, branching | **meshed / secondary network** |
| **Observability level** | very poor | medium but **volatile** | better but **topology-complex** |
| **Dominant gap** | almost no field data → blind | bidirectional, fast-changing injections | non-radial estimation, cable visibility |
| **Virtual-sensing role** | heavy reliance on pseudo-measurements + a few anchors | fuse AMI + DER telemetry to track voltage rise | handle meshed topology + dense data |
| **Where it runs** | substation edge only (no field compute) | substation edge + selective field FADs | substation edge with strong compute |
| **Flagship use case** | estimate the unmeasured middle of a long feeder | hold voltage in band under rooftop-solar reverse flow | observe a networked secondary grid |

**Reading the archetypes:** the rural feeder is the *hardest observability problem and the
clearest virtual-sensing win* — there is almost nothing to measure, so the estimator leans
on pseudo-measurements anchored by the substation head. The suburban DER-heavy feeder is
the *highest-value control problem* (the patent's voltage-control worked example) — the
sources exist (dense AMI + smart-inverter telemetry) but the state is volatile, so fusion
quality dominates. The urban networked feeder has the *best data but the hardest model*
(non-radial topology), shifting the difficulty from observability to estimator formulation.

## Synthesis — From Inventory to Deployment Proposal

Putting the four classifications together gives the spine of the deployment proposal:

1. **Harvest before installing** (Classification 1) — start from AMI voltage, DER
   telemetry, topology, and free pseudo-measurements; reserve new hardware (line sensors,
   µPMUs) for ill-conditioned pockets.
2. **Fuse by measurement class, not by device** (Classification 2) — the module's
   contract is the six DSSE classes; any new source plugs in by declaring its class,
   `h(x)`, and σ.
3. **Place the module where reachability holds** (Classification 3) — real-time DSSE at
   the substation edge (island-capable), localized estimation on field FADs, coordination
   in the ADMS/cloud tier — the AGMS operating-cell hierarchy.
4. **Size to the feeder archetype** (Classification 4) — rural leans on pseudo-measurements,
   suburban on AMI+DER fusion, urban on topology-aware estimation.

This is the same "verify observability → place the asset → simulate → run" discipline the
Asset Portfolio Manager and the granted Operation Loop Formation patent encode — applied to
the **virtual-sensing module itself** as the asset whose observability and reachability
determine where and how it deploys.
