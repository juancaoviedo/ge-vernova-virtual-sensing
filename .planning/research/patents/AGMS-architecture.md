# The AGMS Architecture — A Full, Conceptual Walkthrough

*The Adaptive (Power) Grid Management System invented by Jamshid Sharif-Askary
(the hiring lab director), as described across the six-patent family in this directory.*

> **How to read this document.** This is the "understand it deeply" companion to the
> per-patent summaries. It explains *what AGMS is, why it exists, how it works, and how
> the pieces connect* — at a conceptual level, in plain language, end to end. Reference
> numbers (e.g. `1400`) and object names (e.g. `gWFCll(id)`) appear in parentheses so you
> can cross-walk to the detailed files (`adaptive-power.md`, `asset-portfolio.md`,
> `logistician-module.md`, `operation-loop.md`, `scout-command.md`, `data-management.md`)
> — but you can read this top to bottom and ignore them and still get the whole picture.
> Where your own experience maps in, you'll see a **▶ Juan** note.

---

## Part 1 — The Big Idea

### The problem AGMS is built to solve

A modern power grid is being pushed into a regime classical control was never designed for.
Three things changed at once:

1. **The grid stopped being centralized and predictable.** Distributed energy resources
   (rooftop solar, batteries, EVs, microgrids) inject power *into* the edges of the network.
   Flow is now bidirectional, intermittent, and weather-coupled. The "plant in the middle,
   loads at the edge" model is gone.
2. **The threats became compound and fast.** Extreme weather, cyberattacks, and aging
   infrastructure now interact *simultaneously* across hundreds of geographically dispersed
   field devices. A storm doesn't cause one fault; it causes a cascade.
3. **The central-control assumption became a liability.** Classical SCADA/EMS depends on a
   continuous WAN link back to a central control center. When that link drops — exactly when
   you need it most, during the storm or the attack — the field goes blind and loses the
   authority to act. The network fragment becomes uncontrolled.

On top of that, traditional alert systems generate **alert storms**: thousands of individual
sensor exceedances with no ability to reason about them *together*. They tell you a hundred
things are wrong; they can't tell you what's *actually happening* or what to *do* about it.

### The core insight

AGMS answers all of this with one architectural bet:

> **Stop trying to run the grid from the center. Instead, build a system that continuously
> *understands* the grid's situation, *reasons* about it the way an expert operator would,
> *plans* a coordinated response, and then *dispatches autonomous software agents to the
> field* that can carry out that response — and keep operating even if the center goes dark.**

So AGMS is, in one sentence: **a decentralized, machine-learning-driven nervous system for
the grid that turns raw alerts into self-organizing, self-sustaining field operations.**

### The central metaphor (the model that makes everything click)

Think of AGMS as a **military command structure**, or equivalently a **biological organism**:

| Metaphor | AGMS reality |
|---|---|
| **Senses** (eyes, ears, nerves) | Field devices streaming telemetry; the alert-correlation engine |
| **Brain / strategist** | The reasoning layer that builds a *cognitive state machine* of how to respond |
| **Command HQ / logistics corps** | The orchestration layer that decides which assets, verifies them, assembles them into units, and deploys |
| **Field units / soldiers** | **Scouts** — lightweight software agents that run on field devices, take roles, coordinate, and act |
| **A self-contained platoon that can operate cut off from HQ** | An **operating cell** running in **island mode** without WAN |

Hold that metaphor. Every part below is one organ of this organism, and the *connections*
between them are the nerves and the chain of command.

---

## Part 2 — The Three Brains (the layered architecture)

The parent patent (`adaptive-power.md`) defines AGMS as three major modules stacked into a
**perceive → reason → command** pipeline. This is the top-level anatomy.

```
        ┌────────────────────────────────────────────────────────────┐
        │  GridWideMind (GWM)   — PERCEPTION & INTELLIGENCE           │
        │  "What is happening, and what has happened like it before?" │
        └───────────────┬────────────────────────────────────────────┘
                        │ action stress frame (the distilled situation)
        ┌───────────────▼────────────────────────────────────────────┐
        │  GridArtificer (GA)   — REASONING & DECISION                │
        │  "Build the cognitive state machine for how to respond."    │
        └───────────────┬────────────────────────────────────────────┘
                        │ validated CaCSM + command to begin formation
        ┌───────────────▼────────────────────────────────────────────┐
        │  GridWideCommandHub (GWCH) — ORCHESTRATION & EXECUTION      │
        │  "Assemble the assets, deploy the scouts, run the loop."    │
        └───────────────┬────────────────────────────────────────────┘
                        │ scouts launched
        ┌───────────────▼────────────────────────────────────────────┐
        │  Operating Cells (Field Agent Devices running Scouts)       │
        │  "Execute autonomously — even with no WAN."                 │
        └────────────────────────────────────────────────────────────┘
```

### 2.1 GridWideMind (GWM) — the perception/intelligence layer (ref 200/310)

GWM's job is to turn a chaos of raw signals into a single, clean understanding of the
situation. Its sub-engines:

- **Alert Correlation Engine** (201): the antidote to alert storms. It ingests multi-source
  alerts and *correlates* them — instead of "100 sensors tripped," it produces one structured
  object called an **action stress frame**: the *vital attributes* of the event (`va_n`), the
  *severity degrees* (`sd_n`), and a timestamp (`t_i`). This is the system's distilled answer
  to "what is happening right now."
- **Grid-Wide Decision Support** (202): an ML recommendation engine. It looks at the
  correlation plus historical patterns and proposes a response, attaching a **confidence
  degree**. If confidence is too low, it recirculates rather than acting on a guess.
- **Learning Engine** (203): the institutional memory. It does continuous pattern recognition,
  emits new pattern objects, and — crucially — supplies *historical context* to everything
  downstream. It is the component that says "we've seen something like this before, and here's
  what worked." It reappears in nearly every later stage.
- **Simulation Engine** (204): the "try it in your head before you do it" faculty. It runs
  provisional plans in simulation to validate them before they're allowed to go live.
- **Context Data store** (205): the labeled feature store — temporal experience, data/alert
  ownership, grid profile, resource view.

**▶ Juan:** GWM is the data-and-ML foundation — Databricks/PySpark substation analytics feed
the alert-correlation/decision side; an edge ML estimator (HEMS) is a Learning-Engine-shaped
component.

### 2.2 GridArtificer (GA) — the reasoning/state-machine layer (ref 210 / 315 / 960)

If GWM perceives, GA *thinks*. This is the conceptual heart of the whole invention, and it
deserves its own section (Part 3). At the architectural level, GA takes the action stress
frame and builds a **CaCSM** — a Contextual and Cognitive State Machine — which is the formal
"plan of how the grid should respond, expressed as a sequence of states." GA also guards every
interaction with a security check (the `ga-GateKeeper`, validating a `ga-authenticationkey`).

### 2.3 GridWideCommandHub (GWCH) — the orchestration/execution layer (ref 230/340/975)

Once GA has decided *how* to respond, GWCH makes it physically happen. Its top module, the
**Grid-Wide Federation Command** (975), is the general that issues marching orders to a
logistics corps of specialized managers — the **Logistician**, the **Asset Portfolio
Manager**, the **Formation Manager / Foresight Manager**, the **Scouts Command**, and the
**Federated Edge Transaction Manager**. The five continuation patents are essentially the
detailed blueprints of this corps. Part 4 is the whole story of how they work together.

**▶ Juan:** GWCH is an orchestration control plane — the same shape as the OSED FastAPI
control plane that turns abstract jobs into placed, monitored K3s workloads.

---

## Part 3 — The CaCSM: How the Grid "Thinks"

The single most important concept in the entire family is the **Contextual and Cognitive
State Machine (CaCSM)**. If you understand this, you understand the soul of the invention.

### What it is

A CaCSM is a **state machine that represents a grid response as a sequence of operational
states the grid should move through**, where each state knows its trigger, its required
behavior, and how to tell whether it's succeeding. "Contextual" because it's built from the
*context* of the current situation; "Cognitive" because it's matched, simulated, and
calibrated using learned experience rather than hand-coded rules.

Why a state machine? Because a grid response isn't a single action — it's a *process* that
unfolds: detect → isolate → reconfigure → stabilize → restore. A state machine is the natural
way to encode "do this, and when this condition is met, move to the next thing," with the
ability to branch, self-form, and reach a final goal state with a measurable performance index.

### How a CaCSM gets built (the cognitive assembly line inside GA)

This is a beautiful "draft → simulate → calibrate → promote" pipeline:

1. **Parse the situation into context.** The Context Construct Engine (210) runs the GA-Parser
   on the incoming action stress frame, breaking it into context meta-objects and grouping
   them.
2. **Rank the context into abstraction panels.** Related contexts are grouped into
   **Contextual Abstraction Panels (CAPs)** — each CAP is a coherent "slice" of the situation,
   ranked by a **relevancy index** (high / medium / low) computed by the Learning Engine. An
   *interdependency analyzer* figures out how the panels depend on each other. (Think: "of all
   the things going on, this cluster is the most important to address first.")
3. **Match a pattern.** The CSM Builder (214) takes the highest-relevancy CAP and asks the
   Learning Engine: "what's the best-matched historical state-machine pattern for this?" It
   retrieves that pattern and assembles a **Provisional CaCSM** — a draft state machine with a
   number of states, an initial state, triggers, functional composition, and a final goal state
   with a performance index.
4. **Simulate it.** The Provisional CaCSM is run through the Simulation Engine. Each state is
   *calibrated* — does this transition behave as expected? This is the **simulate-before-commit**
   gate, and it is everywhere in this architecture.
5. **Promote to production.** Once validated, the Production CaCSM_Builder promotes the draft to
   a **Production CaCSM**, and the **CSM Operator (213/1040)** is now allowed to *execute* it —
   but only after the `ga-GateKeeper` validates the security token.

### How a CaCSM gets executed

The CSM Operator runs the production state machine. Each state has a **Learning Engine Agent**
watching for variance — if reality drifts from the simulated expectation, it fires a
*calibration request* back to the Learning Engine (the system keeps learning *during*
execution). And critically: **the CSM Operator doesn't directly command field devices. It
drives the Grid-Wide Federation Command** — i.e., it kicks off the *formation pipeline* (Part 4)
that assembles real assets and deploys real scouts to carry out each state.

> **The key mental link:** the CaCSM decides *that an operation loop should exist and what
> states it cycles through*. The formation pipeline (next part) is what *physically builds and
> runs that loop* out of real grid assets and real software agents.

**▶ Juan:** the simulate-then-promote pattern is exactly **CVXPY MPC solve-before-commit** —
solve and feasibility-check the control problem, *then* command the actuators. The CaCSM
calibration loop is the predict-observe-recalibrate loop of an edge ML controller.

---

## Part 4 — The Formation Pipeline (how the five continuations compose)

This is the part most people miss, and it's the whole reason there are six patents. The five
continuation patents are **not five separate features — they are five sequential stages of one
assembly line** that turns an abstract CaCSM decision into running software on field hardware.

When the CSM Operator drives the Grid-Wide Federation Command (975), it fires a **preparation
alert** that flows down this line. Watch the object that gets passed at each handoff — that's
how the stages connect.

```
  CaCSM decides "form an operation loop"
        │  (preparation alert: for-id, context meta-object)
        ▼
 ① LOGISTICIAN (1023A)        — "WHICH assets, and get them"
        │  → provisional logistics list  gWFCll(id).p / gWFClf(id).p
        ▼
 ② ASSET PORTFOLIO MANAGER (1300) — "ARE they actually fit?"
        │  → verified logistics file  ORACS(id).lf
        ▼
 ③ OPERATION LOOP FORMATION (1400) — "WIRE them into an ORACS loop"   ★ GRANTED patent
        │  → per-asset meta objects + DNA map  (OC-meta-object)
        ▼
 ④ SCOUT COMMAND (1230 / 1441→1444→1445→1447) — "DEPLOY the software"
        │  → launch plan (time, load, origin, destination, asset-id) → scouts running
        ▼
   CSM OPERATOR (1040) runs the loop as a state-machine execution loop
        ▲
        └── DATA MANAGEMENT (POV files) feeds every stage its role-appropriate data view
```

Owners in four words: **Logistician = which / procure. Portfolio Manager = verify. Operation
Loop Formation = assemble + simulate. Scout Command = deploy.**

### ① Logistician — *which assets, and procure them* (`logistician-module.md`)

The CaCSM produces an abstract intent ("reconfigure this area"). It does **not** know which
concrete, real-world assets — which sensors, IEDs, DERs, compute nodes — are needed, or whether
they're available right now. The **Logistician Module (1023A)** is the logistics general
contractor that closes that gap:

1. **Match a template.** It takes the context meta-object and matches it against a *logistics-list
   historical archive* (via a Learning Engine) to retrieve a **federation command template** —
   a structured list of *tasks* and the *class requirements* each task needs (e.g. "needs an
   asset with observability index ≥ X, reachable, with control function").
2. **Select classes, then assets.** It selects asset *classes* that meet each task's
   requirements, then picks specific assets within each class based on their **real-time status**
   (assigned task, current load, availability).
3. **Procure from a marketplace.** A *logistic acquisition agent* (1280) goes to an asset
   marketplace and effectively "bids" for the best-matched available assets across the federation.
4. **Audit the list.** Before anything executes, a *portfolio auditor* (1278) checks the
   assembled list against the *combined* task requirements and loops back if there's a gap.
5. **Own the gaps, forever.** If, later in the pipeline, participating cells turn out to be
   missing pieces (inter-ORACS gap files, `iO-DNA.Mf.g`), those come *back* to the Logistician
   for resupply. It stays the standing owner of unmet logistics needs.

Output: a **provisional logistics list** (`gWFCll(id).p`) — concrete candidate assets, assigned
to tasks, procured but *not yet verified*.

**▶ Juan:** this is a domain-specific scheduler/orchestrator — turn an abstract job into a
concrete, audited set of placed resources, and reschedule when something's missing. That's the
OSED FastAPI control plane resolving a job into K3s workloads.

### ② Asset Portfolio Manager — *are they actually fit?* (`asset-portfolio.md`)

A procured asset isn't necessarily a *usable* asset — especially during a storm, when half the
field may be degraded. The **Asset Portfolio Manager (1300)** is the verification gate. For each
candidate asset it verifies the **operational indexes** — this is what **ORACS** actually means:

> **ORACS = Observability, Reachability, Adaptability, Controllability, Security**
> (the five core indexes; extended to **seven** for verification with **sustainability** and
> **stability**).

- **Observability** — can we actually see this asset's state?
- **Reachability** — can we communicate with / command it?
- **Adaptability** — can it reconfigure to the task we need?
- **Controllability** — can we actually drive its behavior?
- **Security** — is it trustworthy and defensible?
- (+ **Sustainability**, **Stability** for the full seven-index check.)

Any asset failing a threshold is excluded. The manager also runs an **ORACS operation
simulation** against the operation objectives, and routes assets through health/risk analytics
(asset health monitor 1310, performance analytics 1315). **Failed assets trigger a replacement
request back to the Logistician** — closing the loop between ① and ②.

Output: a **verified logistics file** (`ORACS(id).lf`) — assets cleared and fit for the loop.

> ⚠️ **Note on "ORACS":** an earlier note in this directory glossed ORACS as
> "Operation+Role+Asset+Context+Scouts." That backronym appears in **no patent** and was a
> mistake (now corrected). The patents' own abbreviation key (para [0209]) defines it as the
> operational-index set above.

**▶ Juan:** verifying observability/reachability/controllability before acting = the OSED
"is this node healthy and reachable before I dispatch a command?" gate; **virtual sensing**
(ML estimates where direct observability is missing) is literally an observability-index
booster.

### ③ Operation Loop Formation — *wire them into an ORACS loop* (`operation-loop.md`) ★ GRANTED

This is the **granted** patent (US 12,596,341 B2, assigned to **GE Vernova itself**). Its job
is the *assembly* step: take the verified assets and physically construct the **operation loop**
— an ORACS — that the CaCSM wants. The core module is the **formation construct module (1400)**:

1. **Retrieve a matching schema (DNA).** It compares the loop's tasks + logistics list against a
   *historical meta-object database* and pulls the best-matched **schema** — and the patent
   explicitly says **DNA = schema**: the unique organized structure that defines a loop's (or a
   scout's) cognitive processing and behavior. DNA encodes formation type, internal composition
   (asset classes, attributes, functions), interdependency/correlation indexes, the observability
   index, the DNA map, the scouts roster, and the launch plan.
2. **Build per-asset meta objects.** From the matched DNA + the formation plan, it constructs a
   **meta object** for each asset — the object that will actually *cause that asset to execute its
   task*. (A meta object is essentially a behavioral deployment descriptor for a field agent.)
3. **Analyze interdependency.** It maps how assets depend on each other (1-to-n, n-to-1, n-to-n),
   defines cascading requirements, and identifies the *critical asset* in each cascade — the one
   whose failure propagates.
4. **Simulate the loop before committing.** A learning/simulation engine runs the *provisional
   operation loop in simulation mode* to validate operability and correlation against history —
   **and this simulate-before-commit step is in the granted claims (claim 3).**
5. **Handle multi-cell loops.** For loops spanning operating cells, an inter-ORACS module computes
   coloration/interdependency and emits **logistic gap files** (`iO-DNA.Mf.g`) for missing pieces —
   which go back to the Logistician (①).

Output: the **OC-meta-object** — the constructed loop with per-asset meta objects, DNA map,
roster, and (after ④) the launch plan.

**▶ Juan:** the sharpest, most literal bridge in the whole family — "simulate the loop, then
cause execution" *is* CVXPY MPC solve-before-commit. And because this is **GE Vernova's own
granted IP**, it's the strongest "I read your actual patents" talking point you have.

### ④ Scout Command — *deploy the software onto the hardware* (`scout-command.md`)

A verified, assembled loop is still inert — it's a plan, not running processes. **Scout Command**
is the deployment/orchestration subsystem that stands up the actual software agents (**scouts**)
on the field devices. Its module chain:

- **Scout Command Liaison (1441)** receives the OC-meta-object and kicks off scout formation.
- **Scout Formation Processor (1444)** parses the host DNA map and the inter-cell DNA map to drive
  incubation.
- **Scout Incubator Manager (1445)** is the heart: it checks **scout availability** for the roles
  the DNA requires — `DNA.role(s_c, s_m, s_i, s_g)` = **Coordinator, Messenger, Inspector, Guard**
  — and reconciles desired-vs-actual: if a matching idle scout exists, update and assign it; if the
  match is busy, **clone** it; if no match exists, **incubate a brand-new scout** and train it.
  It can also **self-form** and re-supply scouts to fill gaps.
- **Scout Launch Manager (1447)** builds the **launch plan**: for each host and participant scout,
  *time, load, origin, destination, asset-id* — i.e. *what runs where, with what resources, when.*

Output: scouts **launched and running** on Field Agent Devices, and a readiness signal back up
the chain so the CSM Operator can begin executing the loop as a state machine.

**▶ Juan:** the Scout Incubator Manager is, functionally, a **Kubernetes/K3s scheduler with grid
semantics** — declarative desired state, availability check, instantiate-or-clone-or-create to
reconcile. And the **DNA map** that decides what to deploy where is exactly **SI-MAPPER**'s typed,
relationship-aware asset fingerprint. You can speak to both halves from production experience.

### ⑤ Data Management — *what each module is allowed to see* (`data-management.md`, cross-cutting)

This one isn't a stage in the line — it's the **data plane underneath the whole line**. The
problem: many modules need different slices of the same asset data, and you can't let everyone
query one shared database (contention, coupling, and role-inappropriate exposure — a security
problem). The **Data Management module** solves it with **Point of View (POV) files**:

- It is the **sole interface** to the asset database; no other module touches raw data.
- When a module asks for data, it sends a *POV file request* with its role/context.
- Data Management looks up a **patterns database** (schema templates that say "a module in *this*
  role should see *these* fields at *this* granularity"), with the Learning Engine picking the most
  relevant pattern, and assembles a **role-filtered view** — the POV file — just for that requester.
- Three view flavors: **viewConstructModule** (observability / situational awareness),
  **controlConstructModule** (the actuation/command view), **adminConstructModule** (inter-app
  coordination). The **GridWideEye** subsystem builds these into **PoV frames** for observability.

This is effectively **attribute-based access control expressed as data views** — and it's what lets
modules (and cells) stay decoupled enough to run independently, including offline.

**▶ Juan:** POV files = the OSED **FastAPI service layer** mediating all telemetry access +
**Grafana role-differentiated dashboards** over one InfluxDB/TimescaleDB backend. The patterns
database = the **SI-MAPPER ontology** encoding what's relevant per asset class.

---

## Part 5 — Operation Loops, ORACS, DNA, and Meta Objects (the vocabulary that ties it together)

A few concepts recur everywhere; pinning them down makes the whole architecture legible.

- **Operation loop / Operating cell / ORACS.** These are three views of the same thing. An
  **operation loop** is the *unit of work* the system forms; an **operating cell** is the
  *physical cluster of field devices* that runs it; **ORACS** is the *quality bar* it must meet
  (Observable, Reachable, Adaptable, Controllable, Secure). A loop has a **host** asset (the lead)
  and **participant** assets (supporting). The grid response from one CaCSM may consist of *several*
  ORACS loops, one per geographic cluster or operational domain, coordinated as a federation.

- **DNA / schema (synonyms).** The genetic blueprint of a loop or a scout: the organized structure
  that defines its composition and its cognitive behavior. The **DNA map** is what drives scout
  incubation (which roles, how many) and inter-cell coordination. DNA is *matched from history*
  (you don't design each loop from scratch — you retrieve the closest proven blueprint and adapt it).

- **Meta object.** The runtime artifact that **causes an asset to execute a task** — a behavioral
  deployment descriptor. The pipeline's whole purpose is to produce validated meta objects and the
  launch plan that places them.

- **The data objects, in order** (this is the connective tissue — memorize this chain):

  ```
  action stress frame (va_n, sd_n, t_i)        ← GWM perceives the event
    → CAPs (ranked by relevancy index)         ← GA structures it
    → Production CaCSM                          ← GA reasons a response
    → federation command template              ← Logistician matches tasks+requirements
    → provisional logistics list gWFCll(id).p  ← Logistician selects + procures
    → verified logistics file ORACS(id).lf     ← Portfolio Manager verifies indexes
    → OC-meta-object (per-asset meta objects,
        DNA map, scouts roster)                ← Operation Loop Formation assembles + simulates
    → launch plan (time,load,origin,dest,id)   ← Scout Command schedules
    → running scouts on FADs                   ← execution
  ```

---

## Part 6 — Scouts and the Edge (where the work actually happens)

### What a scout is

A **scout** is a lightweight, role-typed software agent — formally "a complex meta-object
encapsulated with a required operation module, configured to perform a specific function in a
particular operating cell." Think of it as a purpose-built container/microservice that gets
deployed onto a field device and assumes a role. The four roles:

| Role | Symbol | Job |
|------|--------|-----|
| **Coordinator** | `s_c` | The cell's authority — manages the cell and the mission |
| **Messenger** | `s_m` | Handles data in motion — ingestion, transformation, storage, inter-cell comms |
| **Inspector** | `s_i` | Observes cell behavior/performance; feeds the decision-support system |
| **Guard** | `s_g` | Defends the cell against physical and cyber threats and functional misalignment |

### The scout lifecycle (the same shape as a process/agent lifecycle)

```
receive → verify (authenticity + timeliness, via authentication key)
        → execute (assume assigned role)
        → detect trigger
        → { perform task | communicate | clone | terminate }
```

Two powerful behaviors fall out of this:

- **Clone** — under a trigger, a scout replicates itself to another cell (and can transfer its
  authority/role under stress). This is how the system *scales and heals* at the edge without HQ.
- **Self-terminate ("demise")** — on a trigger or timeout, a scout cleans itself up. Cells are
  **self-forming and self-terminating**: they exist exactly as long as the operation needs them.

### Field Agent Devices and operating cells

Scouts run on **Field Agent Devices (FADs)** — the physical edge hardware (alongside ordinary
application payloads). A cluster of FADs cooperating under a Coordinator is an **operating cell**.

**▶ Juan:** scout roles = role-differentiated containers on a shared edge cluster (an inference
service, an MQTT messenger, a monitoring sidecar, a security service). The lifecycle +
clone/terminate = K3s controllers reconciling replicas. This is the runtime substrate the whole
patent family ultimately lands on, and you've built it.

---

## Part 7 — Federation, Autonomy, and Island Mode (the payoff)

This is *why* the architecture is decentralized, and it's the part that directly answers the
"central control is a liability" problem from Part 1.

- **Island mode.** An operating cell can run **autonomously for hours or days without contacting
  AGMS at all**. It has its scouts, its local data (POV-served), and its CaCSM-derived behavior —
  it keeps the local control loop alive when the WAN is gone. This is the single most important
  resilience property of the system.
- **Self-forming federations.** Cells can **merge** into larger cells, or band together into a
  **federation** under a *scout-master* cell, to handle a bigger event cooperatively.
- **Transfer of authority.** A cell can **hand off authority** to a neighbor (e.g. if its
  Coordinator's host degrades). This is managed by the **Federated Edge Transaction Manager
  (240/437)**, which guarantees data correctness and referential integrity across the handoff —
  a **federated transaction**, so authority moves without corrupting shared state.

The operation formation type (`oft`) names where a cell sits on the autonomy spectrum: an
independent cell supporting central command (`ioc.cc`), a fully autonomous cell (`ioc.sc`), a
member of cooperating neighbors (`ioc.coc`), or a sub-federation member (`ioc.fm`).

**▶ Juan:** island-mode = OSED **edge-autonomous operation with local buffering**
(InfluxDB/TimescaleDB, MQTT store-and-forward) keeping the control loop running through cloud
outages. Federated authority transfer with integrity guarantees ≈ the consistency discipline
behind a service mesh / leader handoff.

---

## Part 8 — The Cross-Cutting Systems (the threads that run through everything)

Four ideas aren't stages — they're woven through the whole architecture. Spotting them is how you
sound like you *understand* the system rather than just listing its boxes.

1. **The Learning Engine is everywhere.** It ranks CAPs, matches CaCSM patterns, matches DNA
   schemas, picks POV view patterns, and recalibrates states during execution. AGMS is
   fundamentally **retrieval-and-adaptation from historical experience**, not hand-coded rules.
   Almost nothing is designed from scratch at runtime; the best-matched prior is retrieved and adapted.

2. **Simulate-before-commit is a law, not a feature.** The CaCSM is simulated before promotion;
   the operation loop is simulated before execution (and it's in the *granted claims*); asset
   verification runs an ORACS simulation. The architecture *never actuates on an unvalidated plan.*

3. **Data is mediated, never raw (POV).** No module or cell queries the asset DB directly. Everyone
   gets a role-filtered POV view. This is simultaneously a *decoupling* mechanism (modules stay
   independent, can run offline) and a *security* mechanism (no role sees data outside its context).

4. **Security is in the protocol, not bolted on.** Every inter-module message carries a
   **`ga-authenticationkey`**, validated by a **`ga-GateKeeper`** before any state machine activates
   or any data is released — fail the token, the request is dropped. And **gAVA** (the Grid Artificer
   Virtual Agent) standardizes the *message schema* between all modules, so the whole system speaks
   one enforced language. Authentication + schema enforcement are structural.

**▶ Juan:** Learning-Engine retrieval ≈ SI-MAPPER best-matched-pattern lookup over an ontology
graph. Simulate-before-commit ≈ CVXPY MPC. POV mediation ≈ FastAPI service layer. ga-authenticationkey
≈ gRPC service-to-service auth / MCP tool-call auth; gAVA ≈ the enforced MQTT topic+payload schema.

---

## Part 9 — End-to-End Walkthrough (one concrete story)

Put it all together. A storm rolls through a distribution region.

1. **Perceive (GWM).** Hundreds of field sensors throw alerts — undervoltage, a downed-line fault
   indicator, two substations islanding, DER inverters tripping. The Alert Correlation Engine
   refuses to panic; it correlates them into **one action stress frame**: *vital attributes =
   {feeder X fault, DER cluster Y unstable}, severity = high, t = now.* Decision Support proposes a
   response with a confidence score; the Learning Engine supplies "here's what worked in the 2024
   storm like this."

2. **Reason (GA).** The GA-Parser breaks the frame into context, groups it into **CAPs**, and ranks
   them — the feeder-X fault is the highest-relevancy panel. The CSM Builder retrieves the
   best-matched **CaCSM** pattern ("isolate fault → reconfigure feeder → stabilize DER cluster →
   restore"), assembles a **provisional CaCSM**, **simulates** it to calibrate the state transitions,
   and **promotes** it to production. The GateKeeper checks the token; the CSM Operator is cleared to
   run it — which means it fires the **formation pipeline**.

3. **Logistics (Logistician).** For the "reconfigure feeder" state, the Logistician matches a
   **federation command template** (tasks: open these switches, pick up this load, dispatch this
   battery), selects asset classes, picks specific available assets by real-time status, **procures**
   them, and **audits** the list. → *provisional logistics list.*

4. **Verify (Portfolio Manager).** Each candidate is checked for **ORACS** indexes — is that
   recloser observable and reachable? is the battery controllable and stable? One sensor is offline
   (fails observability) → it's excluded and a **replacement request goes back to the Logistician**,
   which substitutes a neighboring unit (or AGMS leans on **virtual sensing** to estimate the missing
   state). → *verified logistics file `ORACS(id).lf`.*

5. **Assemble + simulate (Operation Loop Formation).** The formation construct module retrieves the
   matching **DNA/schema** for this kind of loop, builds **per-asset meta objects**, analyzes
   interdependency (the battery is the critical asset in the cascade), and **simulates the whole
   operation loop** before committing. It closes inter-cell gaps with the Logistician. → *OC-meta-object.*

6. **Deploy (Scout Command).** The Scout Incubator checks availability for the loop's roles, **clones**
   a Coordinator and a Guard onto the substation FAD and **incubates** a fresh Inspector, and the
   Launch Manager schedules them (time/load/origin/destination/asset-id). Scouts go **live** on the
   field devices. → *running operating cell.*

7. **Execute + survive (the edge).** The CSM Operator now runs the loop as a state machine, the cell
   coordinates locally, Inspectors stream observations (as **POV frames**), Guards watch for cyber
   threats. **Then the WAN link drops.** The cell shrugs and keeps going in **island mode** — it
   already has its scouts, its data views, and its CaCSM behavior. It stabilizes the feeder
   autonomously, and when connectivity returns, it transfers state back through a **federated
   transaction** and the scouts that are no longer needed **self-terminate.**

That arc — *correlate → reason → logistics → verify → assemble → deploy → autonomous execution →
graceful island-mode survival* — **is AGMS.**

---

## Part 10 — The Recurring Design Principles (what to actually take away)

If you strip away the vocabulary, AGMS is built from five repeating principles. These are the
things to *say* in the interview, because they show you grasped the philosophy:

1. **Decentralize authority to the edge.** Push decision-making into self-forming, self-terminating
   field cells that survive loss of the center. Resilience comes from autonomy, not from a bigger
   control center.
2. **Reason from learned experience, not hardcoded rules.** Retrieve the best-matched historical
   pattern (CaCSM, DNA, view pattern) and adapt it. The Learning Engine is the spine.
3. **Never actuate on an unvalidated plan.** Simulate-before-commit at every level — it's even in
   the granted claims.
4. **Type your assets and mediate your data.** DNA maps give every asset a typed, relationship-aware
   fingerprint; POV files give every consumer a role-appropriate, access-controlled view. Decoupling
   and security fall out of these two ideas.
5. **Make the whole thing one assembly line.** Logistician → Portfolio Manager → Operation Loop
   Formation → Scout Command is a clean pipeline with a well-defined object passed at each handoff.
   Separation of concerns at the architecture level.

---

## Part 11 — Where Juan's Work Maps (the consolidated bridge map)

| AGMS layer / concept | What it does | Juan's analog | The one-liner |
|---|---|---|---|
| **GWM** alert correlation + decision support | Turn alert storms into a clean situation + recommendation | Databricks/PySpark substation analytics; HEMS edge ML | "I built the streaming-analytics + ML layer that feeds correlation." |
| **CaCSM** simulate→promote | Reason a response, validate before going live | **CVXPY MPC solve-before-commit** | "I've shipped the validate-before-execute gate, just as one optimization." |
| **GWCH / Logistician** orchestration | Turn abstract intent into placed, monitored resources | **OSED FastAPI control plane → K3s** | "That's my orchestration control plane, with grid semantics." |
| **ORACS index verification** | Gate assets on observability/reachability/controllability | OSED health/reachability gating; **virtual sensing** | "I gate dispatch on node health — and ML-estimate state where observability is missing." |
| **Operation Loop Formation** (granted) | Match DNA, build meta objects, **simulate the loop** | **CVXPY MPC** (literal match) + K3s manifests | "Their granted claim 3 is my solve-before-commit. The meta objects are my deployment descriptors." |
| **Scout Incubator** | Reconcile role-typed agents onto field devices | **K3s/K8s scheduler** | "The Incubator *is* a Kubernetes scheduler for the grid." |
| **DNA map** | Typed, relationship-aware asset fingerprint | **SI-MAPPER** (CV→ontology knowledge graph) | "SI-MAPPER is the DNA map for building assets." |
| **Data Management / POV** | Role-filtered, access-controlled data views | **FastAPI service layer + Grafana** over InfluxDB/TimescaleDB | "POV files are my API-mediated, role-scoped data layer." |
| **ga-authenticationkey / gAVA** | Authenticated, schema-enforced inter-module messaging | **gRPC auth + MQTT schema; MCP tool-call auth** | "Authenticated structured messaging — I've built it at gRPC and MCP layers." |
| **Island mode / federation** | Autonomous edge operation through WAN loss | **OSED edge autonomy + local buffering** | "My platform was designed to keep the control loop alive when the cloud drops." |

**The master narrative:** *"The patent family describes one self-organizing platform — perceive,
reason, then run an assembly line (Logistician → verify → assemble+simulate → deploy) that pushes
autonomous scouts onto field cells that survive losing the center. I've built the components of
exactly this, independently, in buildings and DER: OSED is the edge runtime and orchestration
control plane the scouts would land on, my K3s scheduler is the Scout Incubator with grid
semantics, SI-MAPPER is the typed DNA-map asset model, CVXPY MPC is the simulate-before-commit gate
that the granted Operation Loop patent — GE Vernova's own IP — puts in its claims, and my analytics
stack is the GWM data foundation. Coming to GE Vernova means integrating those into a T&D-scale
version of precisely this architecture."*

---

## Quick links

- Map of the family + pipeline diagram + glossary → `INDEX.md`
- Parent architecture in patent detail → `adaptive-power.md`
- Per-stage detail → `logistician-module.md`, `asset-portfolio.md`, `operation-loop.md`,
  `scout-command.md`, `data-management.md`
- Extra OCR-only detail (gAVA, relevancy tiers, CSM validation stages) → `ocr.md`
