# Grid Operations, Industry & the Role — A Study Companion

*A companion to the [AGMS architecture walkthrough](patents/AGMS-architecture.html) — the
grid-operations background, industry structure, device glossary, and role-fit analysis that grew out
of studying the patent family. Cross-references to "Part N" point to that walkthrough.*

> **What's in here.** Appendices A–F, relocated from the architecture walkthrough so the patent
> folder stays focused on the patents themselves. Companion reading: the
> [AGMS architecture walkthrough](patents/AGMS-architecture.html) (Parts 0–11) and the
> [patent index](patents/INDEX.html).

- **A** — how the grid is run today (operator, SCADA / ADMS / DERMS)
- **B** — how the industry is structured (utility vs. ISO vs. DSO)
- **C** — transmission (TSO) vs. distribution operations, side by side
- **D** — where the role fits (grid problems → the patents → your day-to-day)
- **E** — the device field glossary (transmission vs. distribution, with image links)
- **F** — the three meanings of "state"

---

## Appendix A — How the Grid Is Run Today (the Control-Room Operator, SCADA, ADMS, DERMS)

Part 0 says AGMS automates "the job a distribution control-room operator does today with
SCADA / ADMS / DERMS." This appendix unpacks that — the human role and the three incumbent
systems AGMS is designed to decentralize.

### Who this person is

A **distribution control-room operator** (a.k.a. distribution dispatcher / DSO desk operator)
runs the **medium-voltage distribution network** — the part of the grid *below* the substation,
roughly 4–35 kV, that carries power the "last mile" out to neighborhoods, homes, and businesses.

Do not confuse three different control rooms:

- **Transmission operator** — high-voltage bulk power (hundreds of kV), long-distance,
  balancing-authority / NERC world.
- **Generation dispatcher** — deciding which power plants run.
- **Distribution operator** — *this is the one AGMS is about* — keeping the wires that feed
  actual customers energized and within limits.

They typically watch **hundreds of feeders and dozens of substations** from a wall of screens
showing one-line diagrams.

### What the operator actually does

At its core it is a continuous loop: **monitor → detect a problem → decide a response → execute
switching → verify → restore/regulate.** Concretely, their responsibilities are:

1. **Monitoring network state.** Watching voltages, currents, power flows, and the open/closed
   status of every breaker and switch, plus a constant stream of equipment alarms.
2. **Outage response (the firefighting).** When a fault hits — tree on a line, lightning,
   equipment failure — they **locate** it, **isolate** it, **restore** as many customers as
   possible by **reconfiguring** the network (rerouting power from a healthy neighboring feeder),
   and **dispatch field crews** to the actual fault.
3. **Switching operations (safety-critical).** Planning and executing **switching orders** — the
   exact sequence of opening/closing devices — for maintenance and reconfiguration. They must
   guarantee a line is **de-energized and grounded** before a crew touches it (clearances,
   lockout/tagout) and avoid accidentally **back-feeding** a supposedly-dead line.
4. **Voltage/VAR management.** Keeping voltage within legal limits (in the US, ANSI C84.1 —
   roughly ±5%) by commanding **capacitor banks, voltage regulators, and transformer tap-changers
   (LTCs).**
5. **Managing two-way flow from DERs.** Rooftop solar, batteries, and EVs now push power
   *backwards* and make voltage rise mid-day — the operator increasingly has to coordinate or
   curtail them.
6. **Storm/emergency management.** Mass outages: prioritize restoration (hospitals first), juggle
   crews, coordinate mutual aid.

They are judged on **reliability metrics** regulators track — **SAIDI / SAIFI / CAIDI** (how often
customers lose power, and for how long).

**A day-in-the-life snapshot:** an alarm flags low voltage on Feeder 12. The operator checks the
one-line, sees a recloser tripped, cross-references customer outage calls, deduces the fault is
between switches B and C, writes a switching order to open B and C (isolating it), then closes a
tie-switch to pick up the downstream customers from Feeder 9 — *after* checking Feeder 9 won't
overload — and dispatches a crew to the faulted span. Minutes of human judgment, every time.

### The three tools they do it with

These are **layers**, not competitors — each sits on top of the last.

**SCADA — Supervisory Control And Data Acquisition** *(the senses and hands).* The foundation.
Field devices in substations (**RTUs / IEDs**) send back telemetry — measurements and device
status — over protocols like **DNP3**, and the operator can send commands the other way ("open
breaker 7"). SCADA is **remote eyes + remote control + alarming + a historian.** Crucially, **it
decides nothing** — it is a live window onto the grid and a remote control in the operator's hand.
The screens they watch (the **HMI**) are the SCADA front-end.

**ADMS — Advanced Distribution Management System** *(the decision-support brain for the wires).*
A software suite layered on SCADA that adds a **connectivity model of the whole distribution
network** plus analytics and applications, including **OMS** (Outage Management System — predicts
and locates outages from customer calls + smart-meter data + SCADA, tracks restoration, manages
crews) and **DMS apps** — power-flow analysis, **FLISR** (Fault Location, Isolation, Service
Restoration), **Volt/VAR Optimization (VVO/CVR)**, switching-order management, and "what-if" study
mode. So **ADMS ≈ SCADA + a network model + decision/optimization apps.** This is the layer that
*partly* automates the operator's job today — and **FLISR and VVO inside ADMS are the centralized
ancestors of what AGMS decentralizes.**

**DERMS — Distributed Energy Resource Management System** *(the manager for solar/batteries/EVs).*
The newest layer, built because ADMS was not designed for millions of small, behind-the-meter
resources. It **forecasts, monitors, dispatches, and curtails DERs** (smart inverters, storage,
EV chargers, virtual power plants), talking to them via standards like **IEEE 2030.5 / OpenADR**
or aggregator APIs, and ensures all that DER activity does not violate grid limits. It usually
integrates with the ADMS.

The stack, in one picture:

```
        Human operator  ── makes the final calls
              │
   ┌──────────┼───────────┐
 DERMS       ADMS        (study tools)
 (solar,   (model + FLISR,
  batt,     VVO, OMS —
  EV)       the wires brain)
   └──────────┬───────────┘
            SCADA  ── real-time data in / control commands out
              │
         RTUs / IEDs in the field  (DNP3, etc.)
```

### Why this connects back to AGMS

All of that intelligence today lives **in the central control center**, with a **human in the
loop**, and it **depends on the communications link** back to that center staying up. AGMS takes
the decision functions that ADMS and DERMS perform centrally — **FLISR, Volt/VAR, DER
coordination** — and pushes them **out to autonomous agents at the grid edge** that act locally,
in seconds, and keep working when the comms link drops. Same **monitor → decide → switch → restore
→ regulate** loop — done by distributed software instead of a person at a desk.

---

## Appendix B — How the Industry Is Structured (Utility vs. ISO vs. DSO — Who Operates What)

Appendix A described *what* a distribution operator does. This appendix answers the structural
questions: what "utility" actually means, who operates the distribution network in real life, and
why that work is still surprisingly manual.

### What "utility" actually means

There is no single tidy definition, because the industry is structured differently in different
places. The cleanest approach is to separate the **functions** from the **companies** — one company
may perform one function or several:

| Role | What it does | Serves end customers? | Examples |
|------|--------------|----------------------|----------|
| **Generator** | Makes the power | No | Vistra, NRG, plus utility-owned plants |
| **ISO / RTO** (North America) or **TSO** (Europe) | *Operates* the bulk transmission grid + runs the wholesale market | No | ERCOT, PJM, MISO, CAISO, NYISO; RTE (FR), National Grid ESO (GB) |
| **Transmission owner** | Owns the high-voltage lines | No | Often the same company as the distribution utility |
| **Distribution utility** ("wires company" / **DSO** / **LDC**) | Owns & operates the poles and wires that deliver to customers; runs distribution operations | Delivers (may not *sell* the energy) | Oncor, CenterPoint, Con Edison, Enedis (FR), UK Power Networks |
| **Retail electricity provider** | Sells the energy commodity; does billing | Yes (commercially) | Competitive retail providers in Texas |
| **Vertically integrated utility** | All of the above, in one regulated company | Yes | Duke Energy, Southern Co., Dominion, Hydro-Québec |

**How to use the word:** "utility" most precisely means **the regulated company that owns/operates
the wires and serves end customers** — either a *vertically integrated utility* (does everything) or
a *distribution utility* (just the wires). Colloquially, "the utility" = "your power company."

Two things it does **not** mean:

- An **ISO/RTO is not a utility** — it owns no wires and serves no customers; it is an independent
  grid and market operator.
- In **deregulated markets, generation and retail are often separate companies**, not "the utility."

### Sorting real entities into the right buckets

- **Duke Energy** → a **vertically integrated utility**: owns generation + transmission +
  distribution, serves customers, runs distribution operations.
- **Hydro-Québec** → a **vertically integrated public utility** (provincial crown corporation):
  generation (mostly hydro), transmission (its *TransÉnergie* division), and distribution
  (*Hydro-Québec Distribution*).
- **ERCOT** → **not a utility.** It is the **ISO** for most of Texas — it operates the *bulk
  transmission* grid and the market, and does **no** distribution. Distribution in Texas is done by
  separate "wires" utilities (TDUs) such as Oncor, CenterPoint, and AEP Texas.
- **CAISO, MISO, NYISO, PJM** → same category as ERCOT: **transmission and market operators, not
  utilities, no distribution.**

**The key correction:** the ISOs are the "transmission system operator that is present almost
everywhere." They are emphatically **not** distribution operators — so the instinct "TSOs are
everywhere, but is there really an active distribution operator?" is exactly the right question.

### Is distribution actively operated? (Yes — but it is a spectrum)

Separate two ideas:

- **The formal term "DSO"** is mostly **European** — a legally-defined, unbundled entity under EU
  rules (e.g., Enedis in France, the DNOs in Britain). In North America, "DSO" is a newer,
  aspirational term ("the utility of the future / DSO model"). By the formal label, not every utility
  has a "DSO."
- **The function of operating the distribution network** exists almost everywhere a utility owns
  distribution wires — *someone* must dispatch crews, execute switching, and manage outages. So
  essentially every distribution utility has a **distribution operations center** (sometimes its own
  Distribution Control Center, sometimes merged with the transmission control room or the
  outage/dispatch center).

But the **sophistication varies enormously**:

```
 MANUAL / REACTIVE  ───────────────────────────────►  AUTOMATED / PROACTIVE
 small rural co-op            mid-size municipal        large investor-owned utility
 - few dispatchers            - basic SCADA             - SCADA + full ADMS + DERMS
 - paper switching orders     - some remote control     - automated FLISR, VVO
 - "we know when              - growing automation      - AMI / smart meters everywhere
    customers call"                                      - DER management
```

In the US alone there are roughly **3,000 distribution utilities** — large investor-owned,
municipal, and rural cooperatives — sitting all along that line.

### How it really looks, physically

- A utility runs **one or a few control centers** (usually a primary plus a backup, for resilience);
  a large utility may consolidate into a handful of regional distribution operations centers.
- One operator does not cover "5–10 substations" — modern SCADA lets a single operator monitor a
  **large territory: dozens of substations and hundreds of feeders**, all remotely.
- A **substation** steps transmission voltage down to distribution voltage; from each substation
  several **feeders** (circuits) radiate out. A large utility may have **hundreds of substations and
  thousands of feeders.**
- On those feeders sit reclosers, sectionalizers, capacitor banks, regulators, and switches. **Some
  are remotely controllable via SCADA; many are not** — they are manual and need a crew. The
  remotely-controllable fraction is growing but is far from 100% on most systems.

### Why it is still so human

The distribution control room is surprisingly manual, for honest reasons:

1. **Distribution was historically "fit and forget."** Transmission has been heavily instrumented and
   automated for *decades*, because one transmission failure can black out millions. Distribution grew
   up **radial and "dumb"**: power flows one way, local devices (fuses, reclosers) handle faults
   *autonomously*, and the utility often only learned of an outage **when customers phoned in.**
2. **Scale and cost of instrumentation.** There are *thousands of times* more devices on distribution
   than on transmission, spread over enormous areas; sensoring and actuating all of it was never
   cost-justified.
3. **Safety and liability keep humans in the loop.** Switching energizes and de-energizes lines that
   field crews are physically touching. Utilities are deeply conservative about letting software do
   that autonomously — a wrong switch can kill someone — so a human verifies switching orders.
4. **Much of the "automation" that does exist is local, not central.** A recloser tripping and
   re-closing on its own is *protection*, not centralized operation; that has always been automated —
   just decentralized and dumb, not coordinated intelligence.

---

## Appendix C — Transmission (TSO) vs. Distribution Operations: A Side-by-Side

A common confusion is that transmission and distribution operations are "the same job at a
different voltage." They are not. They share a **SCADA foundation**, but they answer different
questions, use different tools, and worry about different physics. This appendix lays them next to
each other across the three axes that matter — **what they observe, what they control remotely, and
what happens automatically** — and then lists what is unique to each.

### The fundamental difference (why the two jobs diverge)

| | Transmission (TSO / ISO) | Distribution operations |
|---|---|---|
| Voltage | 69 kV – 765 kV (plus HVDC) | 4 – 35 kV primary; 120 / 240 V secondary |
| Topology | Meshed / networked — many parallel paths | Radial — mostly one path, reconfigurable |
| Geographic scope | Region / interconnection | Local service territory |
| A single failure… | can cascade and black out millions | usually affects one feeder / neighborhood |
| Defining job | Balance generation to load, hold frequency, keep the system N-1 secure, move bulk power within thermal limits, run the wholesale market | Deliver the last mile: restore outages, hold customer voltage, manage DER |
| Manages frequency? | **Yes** — its master responsibility | **No** — frequency is inherited from the transmission system |
| Core software | **EMS** (state estimation, contingency analysis, AGC, optimal power flow) | **ADMS / DMS** + OMS + DERMS |
| Real-time stakes | Seconds (stability, frequency) | Minutes (restoration); continuous (voltage) |

So to your framing: the TSO *is* largely about **power flow, transfer limits, thermal limits, and
balancing** — and **yes, it heavily manages voltage too** (reactive power and voltage stability are
core TSO functions). The distribution center is more about **restoring outages and holding local
voltage**, and increasingly **managing DER**. Both check voltage; only the TSO manages frequency.

### Axis 1 — What they OBSERVE (and with what)

| What they observe | Transmission (TSO / EMS) | Distribution (control center / ADMS) |
|---|---|---|
| Substation SCADA telemetry (MW, MVAR, volts, amps, breaker status) | Yes — dense, at essentially every substation and line | Yes — but mostly at the substation / feeder head; sparse further out the feeder |
| Frequency | Yes — the master system-wide signal it must regulate | No — frequency is inherited, not measured for control |
| State estimation (full network state from redundant measurements + model) | Yes — a core EMS function; the network is observable | Historically no — too few measurements; most of the feeder is unobservable → the gap virtual sensing fills |
| PMUs / synchrophasors (GPS-timed phasors, IEEE C37.118) feeding WAMS | Yes — wide-area visibility, oscillation and stability monitoring | Emerging only (micro-PMUs / D-PMUs); not yet standard |
| AMI / smart meters (customer voltage + consumption) | No | Yes — a distribution-unique source; millions of endpoints, but periodic, not control-grade real-time |
| Customer trouble calls / IVR | No | Yes — historically the primary way an outage is even detected |
| Line sensors / fault-current indicators (FCIs) | Some | Increasingly — to pinpoint fault location along a feeder |
| Line loadings vs. thermal ratings / congestion | Yes — continuously, drives redispatch | Yes, but informally — feeder loading vs. equipment ratings |
| DER telemetry, solar and load forecasts | Generation side, via the market | Yes, via DERMS — behind-the-meter DER output and forecasts |
| Tie-line / interchange metering, neighbor-control-center data (ICCP / TASE.2) | Yes — schedules power exchange between areas | Rare |

### Axis 2 — What they CONTROL remotely

| What they command remotely | Transmission (TSO) | Distribution (control center) |
|---|---|---|
| Breakers / line switches (reconfigure topology) | Yes — switch HV lines, reconfigure the mesh | Yes — feeder breakers, remote switches, and tie-switches to reroute power |
| Generation setpoints (MW dispatch, AGC, generator voltage / AVR) | Yes — the primary balancing lever | No — distribution does not dispatch generation |
| Transformer tap changers (OLTC / LTC) | Yes — on HV / EHV transformers | Yes — substation LTC plus feeder step voltage regulators |
| Shunt capacitor / reactor banks | Yes — transmission-scale reactive / voltage | Yes — substation and feeder capacitor banks |
| FACTS devices (SVC, STATCOM, series compensation, phase-shifting transformers) | Yes — continuous reactive and power-flow control | No — not used at distribution |
| HVDC converter setpoints | Yes, where HVDC links exist | No |
| Smart inverters / DER (curtail, power factor, reactive support) | Only utility-scale via market | Yes — via DERMS; the fast-growing new lever |
| Flexible / demand-response loads, EV chargers | Limited (wholesale DR) | Yes — via DERMS / demand response |
| Load shedding | Yes — emergency, system-wide | Yes — rotating outages / feeder shedding |

### Axis 3 — What is AUTOMATIC (local, no operator in the loop)

| Automatic mechanism | Transmission | Distribution |
|---|---|---|
| Protective relays trip breakers on a fault (milliseconds) | Yes — distance, differential, overcurrent | Yes — overcurrent relays |
| Fuses (melt and clear the fault) | Rare | Yes — the simplest, ubiquitous protection |
| Auto-reclosing after a transient fault | Sometimes | Yes — reclosers are central to distribution |
| Sectionalizers (open after N recloser operations) | No | Yes — distribution-specific |
| Automatic Generation Control (AGC) — continuous frequency balancing | Yes — centralized closed loop | No |
| Generator AVR / Power System Stabilizers (voltage, oscillation damping) | Yes | No |
| Special Protection / Remedial Action Schemes (SPS / RAS) | Yes — pre-engineered contingency responses | Rare |
| Under-frequency / under-voltage load shedding (UFLS / UVLS) | Yes — automatic last resort | Partially (UFLS relays on some feeders) |
| FACTS continuous voltage / VAR regulation | Yes | No |
| Local cap-bank and voltage-regulator controls (time / temperature / voltage / VAR) | Some | Yes — long-standing local autonomy |
| Smart-inverter autonomous Volt-VAR / Volt-Watt (IEEE 1547-2018) | No | Yes — newer, distribution-unique |
| Distributed FLISR / loop schemes (reclosers self-isolate and restore) | No | Yes — the decentralized self-healing AGMS generalizes |

### Unique to transmission (no real distribution equivalent)

- **Frequency regulation / AGC / balancing** — the defining transmission responsibility; distribution never touches it.
- **State estimation + contingency (N-1) analysis** — continuously simulating "what if any one element trips" to keep the system secure.
- **Stability analysis and damping** — transient, voltage, and oscillatory stability; Power System Stabilizers.
- **Wholesale market and congestion management** — Locational Marginal Pricing (LMP), interchange scheduling, transfer limits / Available Transfer Capability (ATC), transmission rights — the "contracts for how much power can flow" you intuited.
- **Bulk-power FACTS / HVDC / phase-shifting transformers / synchronous condensers.**
- **Black-start coordination** after a wide-area blackout.
- **Wide-area PMU / WAMS monitoring** (migrating toward distribution, but a transmission capability today).

### Unique to distribution (no real transmission equivalent)

- **AMI / smart meters and customer trouble calls** as observation sources.
- **OMS — Outage Management** at premise granularity: predicting/locating outages, crew dispatch, estimated time of restoration (ETOR).
- **Behind-the-meter DER coordination (DERMS)** and **smart-inverter Volt-VAR (IEEE 1547)** — managing millions of small resources.
- **Radial reconfiguration via tie-switches** and **FLISR** self-healing.
- **Conservation Voltage Reduction (CVR)** — deliberately lowering feeder voltage to cut load and energy.
- **The low-observability problem itself** — too many devices, too few sensors — which is precisely what creates the need for virtual sensing.

---

## Appendix D — Where the Role Fits: From Grid Problems → the Patents → Your Day-to-Day

Appendices A–C explained how the grid is run today and why distribution lags. This appendix closes
the loop: it states the underlying **problems** precisely, shows **how the AGMS patents solve each
one**, maps the **job description** onto that architecture, and from all of it infers **what you
would actually do day-to-day** and **what will be expected of you.**

> **Context for the inference.** The role — *Senior Software Engineer & Scientist, Virtual Sensing
> and Decentralized Grid Operations* (req R5043890), in GE Vernova's **CTO organization**, reporting
> to the **Electrification Chief Architect** — sits in a "startup-style, fast-moving" team building
> "the foundation for next-generation decentralized grid operations." On this project's working
> assumption, that Chief Architect is the author of the very patents mapped in this document — which
> means **you would be implementing this architecture alongside the person who invented it.**
> Everything below is inferred from the job description plus the AGMS map; treat it as a well-grounded
> prediction, not an official description.

### D.1 The problems, stated precisely

The grid is mid-transition, and distribution is where it hurts. Five concrete problems:

1. **The feeder went blind (loss of observability).** Rooftop solar, batteries, and EVs turned the
   once-passive feeder into an active, two-way circuit — but the utility still mostly measures it only
   at the substation head. You cannot see voltage, flow, or what a DER is doing mid-feeder. *(Appendix
   C, Axis 1: distribution has no state estimation because it has too few measurements.)*
2. **Events outrun humans and the central computer.** Two-way flows, fast inverter transients, and
   millions of devices produce situations that change in seconds — faster than an operator at a desk,
   or a round-trip to a central control center, can react.
3. **Centralized control is fragile.** All the intelligence lives in one control room and depends on
   the communications link staying up — precisely the thing a storm or cyberattack takes out first.
   The moment the link drops, the field is blind and powerless.
4. **The physics turned bidirectional and volatile.** Reverse power flow and midday solar push voltage
   *above* limits; protection designed for one-way flow miscoordinates; "hosting capacity" (how much
   DER a feeder can absorb) becomes a live constraint. These need continuous local coordination, not a
   daily switching plan.
5. **You cannot safely deploy control you have not validated.** Acting on the physical grid is
   irreversible and dangerous — a wrong command damages equipment or endangers crews. Any autonomous
   control must be validated against the physics *before* it touches a breaker.

### D.2 How the AGMS patents solve each problem

| Problem | The AGMS mechanism that answers it | Patent / part |
|---|---|---|
| 1 — Feeder is blind | The **ORACS observability index** makes "can we see this asset?" a first-class gate, and **GridWideEye / POV frames** distribute situational awareness — but it presumes the state *can* be obtained, which is where **virtual sensing** comes in | Asset Portfolio + Data Management; Parts 5, 8 |
| 2 — Events outrun central control | The **CaCSM** reasons a response and the **operating cell acts locally in seconds**, no round-trip required | Parent / Operation Loop; Parts 3, 4 |
| 3 — Centralized control is fragile | **Operating cells run in island mode**, self-form, and **transfer authority via federated transactions** when the center is gone | Parent / Scout Command; Part 7 |
| 4 — Bidirectional, volatile physics | **Operation loops** continuously coordinate the local resources (DER, caps, regulators) as an ORACS unit, recomputed as conditions change | Operation Loop Formation; Part 4 ③ |
| 5 — Cannot deploy unvalidated control | **Simulate-before-commit** is in the *granted claims* — the loop is simulated and validated before it executes | Operation Loop (claim 3); Parts 3, 8 |

In short: AGMS is the *answer* to those five problems — but it has one hard dependency. It can only
act on assets it can **observe**, and on plans it can **validate**. Those two dependencies — *make the
invisible feeder observable* and *validate control against the physics* — are exactly the two halves
of your job.

### D.3 How your role plugs into the architecture

The job description has three responsibility areas. Each maps cleanly onto a layer of the AGMS map:

| JD responsibility area | What it really is in AGMS terms | The layer it builds |
|---|---|---|
| **Edge Engineering & Data Pipelines** — edge-native components; federated pipelines with no central coordination; integrate SCADA / PMU / DER and DNP3 / Modbus / MQTT / LoRa | The **operating-cell runtime and the federated data plane** the scouts live on, plus the field-protocol ingestion that feeds observation | GWCH / operating cells + Data Management (Parts 2, 4 ⑤, 6) |
| **Virtual Sensing & Control** — infer voltage stability, phase angles, line temperature, asset health from limited sensors; Kalman filters, state estimation; adaptive edge control with minimal latency | The **observability layer ORACS depends on** — estimating the feeder state where there is no sensor — plus the local control logic each operation loop executes | The dependency under ORACS / GWM perception (Parts 5, 8); this is why the project's **Phase 1 is Kalman & state estimation** |
| **Simulation & Integration** — validate virtual sensors against physical models and field data; "close the loop" between simulation and the live grid; integrate digital twins | The **simulate-before-commit gate** made real, plus the calibration loop that keeps estimates honest against physics | CaCSM / operation-loop simulation (Parts 3, 8); EMT tools (PSCAD / RTDS / Opal-RT) are the "preferred" qualification here |

So the role is not "a bit of everything." It is precisely the **two hard dependencies of the AGMS
architecture** — observability (virtual sensing) and validation (close-the-loop simulation) — plus
the **edge substrate** both run on. You would be building the parts of the platform that make
autonomous operation *trustworthy*: it can see, and it has been checked.

### D.4 What you would actually do day-to-day (inferred)

Grounding the JD in concrete work, by theme:

**Build edge software (the largest share, Python-first).**

- Write edge-native services (Python; Go/Rust is "or", not required) that run on **K3s** at
  substations / field nodes — the runtime an operating cell's scouts would be.
- Stand up **federated data pipelines** with **NATS / Kafka** so nodes share state and decisions
  without a central broker; enforce message schemas and secure them (gRPC, tokens).
- Integrate field data: wire in **SCADA (DNP3), PMUs (C37.118), DER controllers (IEEE 2030.5),
  Modbus, MQTT, LoRa** as the observation inputs.
- Instrument everything with **Prometheus / Grafana**; persist time-series in **InfluxDB / TimescaleDB**.

**Develop virtual-sensing algorithms (the scientific core).**

- Implement estimators — **Kalman filters, state estimation, signal processing** — that infer
  **voltage stability, phase angles, line temperature, and asset health** from sparse edge measurements.
- Make them **adaptive and low-latency** so they run on edge hardware in real time.
- Continuously **calibrate** them against incoming data (the predict-observe-correct loop).

**Close the loop with simulation and the field (the validation core).**

- Work with **power-systems engineers** to validate your virtual sensors against **physical models**
  (EMT: PSCAD / RTDS / Opal-RT) and **real field data**.
- Integrate **digital twins** (OpenFMB, Modelica, graph-based models) so control is tested in
  simulation before it goes live — the literal "close the loop" the JD names.
- Likely **field-validation work** — deploying to real edge hardware, debugging against live grid
  behavior, iterating.

**Operate startup-style inside a big company.**

- Prototype fast, own components end-to-end, work directly with the architect and power engineers, and
  turn research ideas into deployed edge software in short cycles.

### D.5 What will be expected of you (the bar)

- **A genuine hybrid — physics + AI + distributed systems in one person.** The role's whole reason to
  exist is that virtual sensing needs all three: control theory to estimate state, ML to do it from
  sparse data, and edge / distributed engineering to run it in the field. That rare combination is the bar.
- **Hands-on senior IC ownership.** "High-impact, hands-on," "startup-style" — you own components end
  to end and ship, not just design.
- **Scientific rigor and production engineering together.** State estimation done right *and* deployed
  to resilient production edge — both, not either.
- **Comfort with ambiguity and pace** inside a CTO / advanced-development org that is building something new.
- **The credibility gaps to close** (from the project's gap analysis): fluency in **NATS / Kafka /
  Pulsar** (vs. your MQTT), **K3s** specifics (vs. full K8s), **DNP3 / SCADA / PMU** grid protocols
  (vs. Modbus / MQTT), **Prometheus** (vs. Grafana-only), **federated learning**, and **IEC 61850 /
  IEEE 2030.5** awareness. Your edge platform (OSED), SI-MAPPER asset model, HEMS edge ML, and CVXPY
  MPC solve-before-commit already cover the *shape* of every responsibility — the work is translating
  them into this stack and vocabulary (which is what the rest of this study set does).

### D.6 The synthesis (say this in the room)

> "The grid is going two-way and fast, and distribution can't see itself or react in time — and the
> central-control model breaks exactly when it's needed most. This architecture answers that with
> autonomous, self-healing field cells — but autonomy is only safe if the system can *see* the feeder
> and *validate* its actions first. That is precisely my role: I build the **virtual sensing** that
> makes the invisible feeder observable, the **close-the-loop simulation** that proves a control action
> before it touches the grid, and the **edge runtime** both of those run on. I've built the shape of
> all three already — an edge platform with local autonomy, an ML asset-intelligence layer, and a
> solve-before-commit control loop — just in buildings and DER instead of T&D. This role points those
> same skills at the architecture you patented."

---

## Appendix E — The Devices Themselves: A Field Glossary (Transmission vs. Distribution)

Appendix C named many devices across its three axes — *observe*, *control*, *automatic* — without
saying what each one actually **is**. This appendix is the field glossary: for each device, **what
it is, what it is for, and how it looks different on the transmission (TSO) side versus the
distribution (DSO) side.** Grouped by what the device does.

### E.1 Measurement and observation

| Device | What it is and its purpose | On transmission (TSO) | On distribution (DSO) |
|---|---|---|---|
| **Instrument transformers — CT / VT (PT)** | Current and voltage transformers that step the line's huge current and voltage down to safe, standard signals (e.g. 5 A, 120 V) that meters and relays can read — the actual *sensing element* behind almost every measurement | High-accuracy free-standing CTs and VTs at every substation; **CCVTs** (capacitor-coupled) at EHV; metering-grade for settlement | Smaller pole- or pad-mounted units, fewer of them; many points downstream have *no* instrument transformer at all — the root of low observability |
| **RTU — Remote Terminal Unit** | The substation's data-collection box: gathers all analog and status I/O and ships it to the control center over a SCADA protocol (DNP3) | At essentially every transmission substation — dense coverage | At distribution substations; **sparse to none** out on the feeders |
| **IED — Intelligent Electronic Device** | A microprocessor relay/meter that both *protects* and *reports* — measures, makes protection decisions, and publishes data, increasingly over **IEC 61850** | Many per substation, often on an IEC 61850 station / process bus | Growing at substations and inside smart reclosers; thin further out |
| **PMU — Phasor Measurement Unit (+ PDC)** | Measures **synchrophasors** — voltage/current magnitude *and phase angle*, GPS-time-stamped, 30–120 times per second — streamed to a **PDC** (concentrator); standard **IEEE C37.118**. Purpose: see the grid's dynamic state and angle spread in real time | Deployed across the bulk grid for **WAMS** — wide-area stability, oscillation detection, angle separation | **Micro-PMUs / D-PMUs** emerging; harder, because feeder angle differences are tiny and need far higher precision |
| **AMI smart meter** | The customer revenue meter, now two-way: reports consumption, **voltage at the premise**, and a "last-gasp" outage signal over mesh/cellular | None — transmission has no end customers | The biggest new distribution data source — millions of voltage/usage points, but periodic (minutes), not control-grade real-time |
| **Faulted-circuit indicator (FCI) / line sensor** | A clamp-on device that flags when fault current passed it (and increasingly streams current/temperature) to **locate** a fault along a circuit | Some; transmission leans on relay-based and traveling-wave fault location | Widely useful — pinpoints which feeder section faulted so crews don't patrol the whole line |
| **Dynamic line rating (DLR) sensors** | Sensors of conductor temperature/tension/sag plus weather to compute the line's *real-time* safe ampacity, instead of a fixed nameplate rating | Used to **squeeze more capacity** out of constrained corridors | Rare |

*Not a device, but worth noting:* **state estimation** and **forecasts** are *software* "virtual
instruments." Transmission state estimation reconstructs the full network state from redundant
measurements; distribution historically cannot run it for lack of measurements — the gap **virtual
sensing** is meant to close.

### E.2 Switching and protection

| Device | What it is and its purpose | On transmission | On distribution |
|---|---|---|---|
| **Circuit breaker** | A switch that can interrupt huge **fault** currents on command (from a relay) without destroying itself — the grid's primary "off switch" | Large SF6 or vacuum breakers at every substation, interrupting enormous fault currents | Smaller vacuum breakers at the substation feeder; downstream the job passes to reclosers |
| **Recloser** | A breaker *plus* a controller that **auto-recloses** after tripping — because most distribution faults (a branch brushing a line) are *temporary* and clear themselves | Some transmission lines auto-reclose, but cautiously | **Central to distribution** — trip-and-reclose with overcurrent settings; modern ones are IEDs and the building block of distributed FLISR |
| **Sectionalizer** | Not a fault interrupter — it **counts** the upstream recloser's trips and opens during a dead interval to isolate the faulted section | Not used | Distribution-specific; coordinates with reclosers and fuses |
| **Disconnect / load-break / tie switch** | Switches that isolate equipment or **reconfigure** the network; a *tie switch* (normally open) between two feeders can transfer load from one to the other | Big air-break **disconnectors** for isolation (usually opened de-energized) | Motor-operated **tie / sectionalizing switches** are the levers for reconfiguration and FLISR |
| **Fuse** | The simplest protection: a metal element that **melts** and clears on overcurrent — one-shot, no intelligence | Rare | Everywhere — on laterals and distribution transformers (fuse–recloser coordination) |
| **Protective relay** | The "brain" that watches CT/VT signals and **trips the breaker** in milliseconds on a fault; types include overcurrent (50/51), **distance/impedance (21)**, and **differential (87)** | **Distance + differential + pilot** (communication-assisted) schemes protect meshed lines and large transformers/buses | Mostly **overcurrent** and recloser controls; **directional** elements increasingly needed because DER feeds fault current backward |

### E.3 Voltage and reactive power

| Device | What it is and its purpose | On transmission | On distribution |
|---|---|---|---|
| **Power transformer + on-load tap changer (OLTC / LTC)** | Steps voltage between levels; the **tap changer** adjusts the turns ratio *under load* to hold output voltage steady | Large HV / EHV transformers with LTCs | The **substation LTC** sets the whole feeder's starting voltage |
| **Step voltage regulator** | An autotransformer with a tap changer placed *along a feeder* to boost or buck voltage as it sags with distance | Generally not needed (meshed, short electrical distances) | Distribution-specific — line regulators keep far-end customers in range |
| **Shunt capacitor bank** | Supplies **reactive power (VARs)** to hold voltage up under load; switched in and out | Large substation banks | Pole-mounted **switched caps** along feeders plus substation banks — a primary volt/VAR tool |
| **Shunt reactor** | The opposite — **absorbs** reactive power to pull voltage *down* on lightly-loaded long lines or cable | Common on EHV lines and long cables | Rare (occasionally with heavy underground cable) |
| **FACTS — SVC / STATCOM** | Power-electronic devices for **fast, continuous** reactive/voltage control; SVC = thyristor-switched caps/reactors, STATCOM = inverter-based and faster | At critical buses and near inverter-heavy or electrically weak areas | Not used (cost) — the **smart inverter** is distribution's distributed equivalent |
| **Series compensation** | Capacitors placed *in series* with a long line to cancel part of its impedance and raise transfer capability | Transmission only | Not used |
| **Phase-shifting transformer (PST)** | Injects a phase-angle shift to **steer real-power flow** between parallel paths | Transmission only — flow control | Not used (radial feeders have one path) |
| **Synchronous condenser** | A spinning machine (a generator with no fuel) providing reactive power, **inertia**, and short-circuit strength | Resurging near inverter-dominated regions for stability | Not used |

### E.4 Power conversion and the DER interface

| Device | What it is and its purpose | On transmission | On distribution |
|---|---|---|---|
| **HVDC converter** | Converts AC to DC and back to move bulk power over long distances or undersea, or to tie **asynchronous** grids, with precise fast power-flow control | Transmission only — point-to-point links and back-to-back ties | Not used |
| **Smart inverter** | The grid interface for PV and batteries — far more than a DC-to-AC converter: it can do **Volt-VAR, Volt-Watt**, and fault ride-through autonomously (**IEEE 1547-2018**) | Utility-scale plants, via the market | The DER workhorse and distribution's **distributed FACTS** — thousands of small, fast reactive sources |

### E.5 Generator and system control loops (mostly transmission)

These are control *systems*, not discrete field devices:

- **AGC (Automatic Generation Control)** — continuously nudges generators' MW output to hold system
  frequency and net interchange. Transmission / market; no distribution analog.
- **AVR (Automatic Voltage Regulator)** — adjusts a generator's excitation to hold its terminal
  voltage. Generation; the smart-inverter Volt-VAR function is the distributed echo of it.
- **Governor / primary frequency response** — a generator's built-in speed control that instantly
  arrests a frequency change. Generation / transmission.
- **PSS (Power System Stabilizer)** — adds a damping signal to the AVR to quell inter-area
  oscillations. Transmission.

### E.6 Controllable loads and distributed resources (mostly distribution)

- **DER + DERMS** — distributed energy resources (PV, storage, EV) plus the system that forecasts,
  dispatches, and curtails them. Distribution; only utility-scale DER shows up at transmission via
  the market.
- **Demand response / flexible loads / EV chargers** — loads that can be shifted or curtailed.
  Distribution (and wholesale DR programs at the market level).

### E.7 Automatic system-protection schemes

- **SPS / RAS (Special Protection / Remedial Action Schemes)** — pre-engineered automatic responses
  ("if line X trips, instantly shed generator Y") that keep the bulk system stable. Transmission;
  rare on distribution.
- **UFLS / UVLS (under-frequency / under-voltage load shedding)** — relays that automatically drop
  blocks of load to arrest a frequency or voltage collapse. *Decided by the bulk system, but the
  relays physically sit on distribution feeders* — a place where the two worlds meet.
- **Distributed FLISR / loop schemes** — reclosers and switches with peer logic that isolate a fault
  and restore power via an alternate path **without the control center**. Distribution; the
  decentralized self-healing that AGMS generalizes from fixed logic into *reasoning*. A published
  example (Koch-Ciobotaru et al., ICRERA 2014 — [`sources/flisr-distributed-fsm-2014.md`](sources/flisr-distributed-fsm-2014.html)) implements
  exactly this: the *same finite-state machine* on every breaker, cooperating via IEC 61850 **GOOSE**
  messages, in three phases — isolate downstream, search upstream for a tie breaker, then restore from
  a neighboring feeder.

### E.8 Quick visual reference (clickable — opens an image search)

The device names below link to an image search so you can see the real hardware in seconds. Where the
transmission and distribution versions look very different, both are linked.

**Measurement & observation:**
[instrument transformer (CT / VT)](https://www.google.com/search?tbm=isch&q=current+voltage+transformer+substation) ·
[RTU](https://www.google.com/search?tbm=isch&q=remote+terminal+unit+scada) ·
[protective relay / IED](https://www.google.com/search?tbm=isch&q=protective+relay+ied+substation) ·
[PMU](https://www.google.com/search?tbm=isch&q=phasor+measurement+unit) ·
[AMI smart meter](https://www.google.com/search?tbm=isch&q=smart+electricity+meter) ·
[faulted-circuit indicator](https://www.google.com/search?tbm=isch&q=faulted+circuit+indicator) ·
[dynamic line rating sensor](https://www.google.com/search?tbm=isch&q=dynamic+line+rating+sensor)

**Switching & protection:**
[HV circuit breaker (transmission)](https://www.google.com/search?tbm=isch&q=high+voltage+sf6+circuit+breaker+substation) ·
[distribution recloser](https://www.google.com/search?tbm=isch&q=distribution+recloser+pole) ·
[sectionalizer](https://www.google.com/search?tbm=isch&q=distribution+sectionalizer) ·
[disconnect / air-break switch](https://www.google.com/search?tbm=isch&q=air+break+disconnect+switch+substation) ·
[distribution fuse cutout](https://www.google.com/search?tbm=isch&q=distribution+fuse+cutout)

**Voltage & reactive power:**
[on-load tap changer](https://www.google.com/search?tbm=isch&q=on+load+tap+changer+transformer) ·
[feeder voltage regulator](https://www.google.com/search?tbm=isch&q=distribution+step+voltage+regulator) ·
[pole-mounted capacitor bank](https://www.google.com/search?tbm=isch&q=pole+mounted+capacitor+bank) ·
[substation capacitor bank](https://www.google.com/search?tbm=isch&q=substation+capacitor+bank) ·
[shunt reactor](https://www.google.com/search?tbm=isch&q=shunt+reactor+substation) ·
[SVC / STATCOM](https://www.google.com/search?tbm=isch&q=static+var+compensator+statcom) ·
[series capacitor (transmission)](https://www.google.com/search?tbm=isch&q=series+capacitor+bank+transmission) ·
[phase-shifting transformer](https://www.google.com/search?tbm=isch&q=phase+shifting+transformer) ·
[synchronous condenser](https://www.google.com/search?tbm=isch&q=synchronous+condenser)

**Power conversion & DER:**
[HVDC converter station](https://www.google.com/search?tbm=isch&q=hvdc+converter+station+valve+hall) ·
[solar smart inverter](https://www.google.com/search?tbm=isch&q=solar+inverter) ·
[EV charger](https://www.google.com/search?tbm=isch&q=ev+charging+station)

For deeper reading on any of these, the **Wikipedia** articles (e.g.
[Phasor measurement unit](https://en.wikipedia.org/wiki/Phasor_measurement_unit),
[Recloser](https://en.wikipedia.org/wiki/Recloser),
[Protective relay](https://en.wikipedia.org/wiki/Protective_relay),
[Tap changer](https://en.wikipedia.org/wiki/Tap_changer),
[Static synchronous compensator](https://en.wikipedia.org/wiki/Static_synchronous_compensator),
[HVDC](https://en.wikipedia.org/wiki/High-voltage_direct_current)) are a fast, photo-rich next step.

---

## Appendix F — The Three Meanings of "State" (and Why They Keep Colliding)

Almost every confusion about this architecture traces back to one overloaded word. **"State" is used
for three genuinely different objects**, and because they are all called "state," they appear circular
("measurements determine the state, but measurements also build the state machine, whose state the
measurements then determine…"). They are not circular — they are **three different things at three
different levels.** Name them apart and the whole picture snaps into focus.

| # | The "state" | What it really is | Discrete or continuous | How it is obtained | AGMS component | Its proper name |
|---|-------------|-------------------|------------------------|--------------------|----------------|-----------------|
| ① | **Physical state** | The grid's electrical condition: bus voltages, phase angles, currents, power flows, tap positions, frequency | **Continuous** — a vector of numbers (`x`) | **Virtual sensing / state estimation** from sparse measurements | The virtual-sensing layer feeding GWM's **Context Data (205)** | the **system state** / **state vector**; recovered by a **state estimator / observer** (Kalman filter) |
| ② | **Operating regime / mode** | Which *situation* we are in: normal, fault on feeder 15, overvoltage on feeder 25 | **Discrete** — one label from a small set | **Classifying** the physical state (plus raw alerts) | **Alert Correlation Engine (201)** raises it; **Context Construct Engine (210) + CAPs** classify and rank it | the **operating regime** / **mode**; via **mode detection / fault detection & diagnosis (FDD) / situational awareness** |
| ③ | **Plan step** | Which step of the chosen response we are executing: isolate, reconfigure, stabilize | **Discrete** — a node in *one* plan | The **CaCSM**, built from a learned template; current step picked by measurements meeting a transition condition | **CSM Builder (214)** builds it, **CSM Operator (213/1040)** runs it | the **control / execution state** of a **state machine**; a **procedure step** |

The trap is that ②, the regime, and ③, the plan step, are *also* "states" in plain English — but they
are a **label** and a **node in a graph**, respectively, while ① is a **vector of physical numbers.**
Three different mathematical objects wearing the same word.

### F.1 — ① The physical state (continuous; the state vector)

This is "what the grid is electrically doing right now": the voltages, angles, currents, flows, tap
positions, and frequency. It is a **continuous vector**, `x`. Because the feeder is sparsely measured,
you cannot read all of `x` directly — you **estimate** it from the few measurements you have. That
estimation *is* **virtual sensing**, and its formal name is **state estimation**; the algorithm that
does it is an **observer**, the canonical one being the **Kalman filter**. This runs **continuously,
always on** — it is the bedrock every other layer reads from. In AGMS, it is the layer the *job*
builds, feeding clean state into GWM. (This is why the JD names "Kalman filters, state estimation,"
and why Phase 1 of this project is exactly that.)

> Keyword: **state estimation.** When the interview says "state," in *this* layer it means the
> physical state vector — and your job is to estimate it.

### F.2 — ② The operating regime / mode (discrete; a label)

This is "what *kind* of situation we are in" — normal, a fault on feeder 15, a voltage violation on
feeder 25. It is **discrete**: one label drawn from a small set of regimes. Crucially, **it is computed
*from* ①** — you look at the estimated physical state (and the raw alerts) and **classify** it into a
regime. So ② is *downstream* of ①; it is not the same object, it is a *summary judgment* about ①.

Who computes it in AGMS:
- The **Alert Correlation Engine (201)** in GridWideMind detects that an abnormal condition exists and
  packages it as the **action stress frame** (vital attributes, severity, timestamp) — it *raises* the
  regime.
- GridArtificer's **Context Construct Engine (210)** runs the GA-Parser, decomposes the frame into
  context meta-objects, and builds **Contextual Abstraction Panels (CAPs)** ranked by the Learning
  Engine's relevancy — it *classifies and prioritizes* the regime. The highest-relevancy CAP is, in
  effect, "the dominant situation to act on."

Its proper names in the literature: **mode detection**, **fault detection and diagnosis (FDD)**,
**classification**, or operationally, **situational awareness**. (If you want the formal model for
"infer a hidden *discrete* mode from observations over time," that is a **Hidden Markov Model.**)

> Keyword: **regime / mode** — *not* "state." Say "operating regime" out loud to keep it distinct
> from ① and ③.

### F.3 — ③ The plan step (discrete; a node in the response state machine)

Once the regime is known, the system **selects and builds a response plan** for it — the **CaCSM**, a
**state machine** whose nodes are the steps (Isolate → Reconfigure → Stabilize → Restored). The
*template* for that machine is **learned over time** (a library of patterns); the *concrete* machine is
instantiated for this event. Then, as it runs, measurements determine **which step we are currently in**
and when a step's **transition condition** is met to advance.

Who does it in AGMS: the **CSM Builder (214)** assembles the machine from the best-matched learned
template (then simulates/calibrates it); the **CSM Operator (213/1040)** runs it, with a per-state
**Learning Engine Agent** watching for drift.

Its proper names: the **control state** or **execution state** of a **state machine**, or plainly a
**procedure step**. This is meaning-of-state most software engineers already hold (a Kubernetes pod's
`Running`, a workflow's current node).

> Keyword: **plan step** (or "CaCSM state") — a node in a procedure, *not* the physical state.

### F.4 — How the three connect (the part that looks circular but isn't)

The physical state ① is the **shared, continuous input**; ② and ③ are both *derived from* it but are
different *kinds* of object, produced at different moments:

```
        sparse field measurements (SCADA, PMU, AMI, line sensors)
                          │
                          ▼
        ┌──────────────────────────────────────────┐
        │  VIRTUAL SENSING / STATE ESTIMATION        │   ← continuous, always on
        └──────────────────────────────────────────┘
                          │ produces
                          ▼
        ① PHYSICAL STATE  x = (voltages, angles, currents, taps, f)   ← a continuous vector
                          │
            ┌─────────────┴──────────────────────────────┐
            │ classify (downstream of x)                   │ drive (downstream of x)
            ▼                                              ▼
   ② OPERATING REGIME / MODE                          ③ PLAN STEP  (a CaCSM node)
   "fault on feeder 3, section B"  (a label)          "currently: ISOLATE"
            │ selects + builds (once)                       ▲
            └────────────►  CaCSM state machine ────────────┘
                           built once from a learned template,
                           then driven by x toward its goal state
```

Read it as three jobs that all consume `x` but ask different questions:

- **②** asks *"what kind of situation is this?"* — once, when the regime changes — and uses the answer to
  **build** the plan. (Build is rare, event-triggered.)
- **③** asks *"which step am I on, and is the next transition's condition met?"* — continuously, after
  the plan exists — and uses the answer to **drive** the plan. (Drive is constant.)
- A supervisor keeps re-checking ② ("does this regime still hold?"); if it changes, ② re-fires and a
  **new** plan replaces the old one.

So `x` is never "building the machine and reading its state at the same instant." `x` continuously
*exists*; a *change* in `x`'s regime triggers a **one-time build** of a plan; thereafter `x` *drives*
that plan. Build-once, drive-continuously — different jobs on different floors.

### F.5 — The naming convention to adopt (so they never collide again)

Use three distinct phrases and never the bare word "state":

| Layer | Say this | Never just say | One-word cue |
|---|---|---|---|
| ① | **"physical state"** (or *state vector* / *system state*) | "state" | *estimate* |
| ② | **"operating regime"** (or *mode*) | "state" | *classify* |
| ③ | **"plan step"** (or *CaCSM state* / *procedure step*) | "state" | *execute* |

The sentence that ties them, said precisely:

> "Virtual sensing **estimates the physical state**; the system **classifies that into an operating
> regime**; the regime **selects a response plan whose steps** are then **driven by the physical
> state.** Three different 'states,' three different jobs."

---

## Appendix G — AGMS in Self-Adaptive-Systems Terms (MAPE-K → AWARE)

A useful way to *name* what AGMS is, for a software audience: it is a **self-adaptive (autonomic)
system** — one that adjusts its own behavior at runtime through a feedback loop. The canonical loop is
**MAPE-K**; the 2025 research frontier is **AWARE**. AGMS lines up almost exactly with the shift from the
first to the second. *(Source: Sanwouo, Quinton & Temple, "Breaking the Loop: AWARE is the New MAPE-K,"
FSE Companion '25 — [`sources/mapek-aware-2025.md`](sources/mapek-aware-2025.html).)*

### The two loops

**MAPE-K** (Kephart, IBM, ~2003): **M**onitor → **A**nalyze → **P**lan → **E**xecute, over a central
**K**nowledge base. Centralized, reactive, sequential, no built-in learning. **Today's grid control —
SCADA + ADMS / DERMS + a human operator — is essentially a centralized, reactive MAPE-K loop.**

**AWARE** = **A**ssess, **W**eigh, **A**ct, **R**eflect, **E**nrich: distributed, goal-driven AI agents
that perceive context, weigh options (and negotiate), act in a coordinated/distributed way, **reflect**
(continuous learning), and **enrich** shared knowledge. Distributed, proactive, learning.

### AGMS maps onto AWARE, not classic MAPE-K

| AWARE stage | AGMS embodiment |
|---|---|
| **Assess** — understand context, not just raw data | GWM alert correlation + GA context construction (CAPs); **virtual sensing** supplies the physical state |
| **Weigh** — formulate and evaluate options, simulate | CaCSM build: match a learned pattern → **simulate-before-commit** → promote |
| **Act** — distributed, coordinated execution | GWCH + scouts on operating cells, acting edge-locally |
| **Reflect** — continuous learning | Learning Engine Agents watching per-state variance, recalibrating |
| **Enrich** — update and share knowledge | Learning Engine updating the patterns DB; POV-mediated distributed knowledge |

And the limitations AWARE pins on MAPE-K are exactly the ones AGMS is built to fix:

| MAPE-K limitation | AGMS's answer |
|---|---|
| Centralized | Distributed operating cells + scouts; island-mode autonomy |
| Reactive only | Foresight Manager + simulate-before-commit (proactive) |
| Sequential, raw monitoring | Contextual perception (action stress frame → CAPs) first |
| No continuous learning | Learning Engine: pattern recognition + calibration |
| Centralized knowledge | POV files / patterns DB — distributable knowledge |

### Why this is worth carrying into the room

It lets you describe the architecture in **recognized software-engineering terms** rather than only the
patents' bespoke vocabulary: *"AGMS is a self-adaptive system — a distributed, learning evolution of the
MAPE-K loop, very much in the spirit of AWARE: scouts are the agents, the Foresight Manager is the
anticipation, the Learning Engine is the Reflect/Enrich, and simulate-before-commit is the option
evaluation in Weigh."*

---

## Quick links

- AGMS architecture walkthrough (Parts 0–11) → [AGMS-architecture.html](patents/AGMS-architecture.html)
- Patent index, family map + glossary → [INDEX.html](patents/INDEX.html)
