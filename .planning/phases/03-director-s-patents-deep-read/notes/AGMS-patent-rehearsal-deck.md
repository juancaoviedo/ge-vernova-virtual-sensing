# AGMS Patent Rehearsal Deck

**For:** Oral rehearsal before the GE Vernova interview — Jamshid Sharif-Askary, director.
**Purpose:** Distill the AGMS patent family into three deliverables per patent (summary,
connection, question) and two deck-level deliverables (90-second family pitch, closing master
narrative). Rehearse aloud; this is the performance layer. For depth, see
`.planning/research/patents/INDEX.md` and the per-patent files.

---

## How to Use This Deck

Read each patent section aloud, in order. The two-to-three sentence summary under
`### Summary` IS the spoken track — say it without notes, then move to the next patent.
Do not memorize word-for-word; aim to deliver the idea in your own words in about twenty
seconds per patent. Practice the `## The ~90-Second Pitch` at the top as a standalone
opening if the director asks "what do you know about our patents?" Close every
conversation with the `## Closing: The Master Narrative`.

---

## The Assembly Line at a Glance

The five continuation patents are sequential stages of a single assembly line kicked off by
the parent's CaCSM. Memorize this order:

```
Parent (adaptive-power)    → fires the alert → builds context → forms a CaCSM
   ↓
Logistician Module         → WHICH assets / PROCURE / AUDIT   (provisional logistics list)
   ↓
Asset Portfolio Manager    → VERIFY the assets (7 operational indexes)
   ↓
Operation Loop Formation ★ → ASSEMBLE + SIMULATE the ORACS loop (simulate-before-commit)
   ↓
Scout Command              → DEPLOY the scouts onto field devices
   ↓
Data Management            → WHAT each module SEES (POV views served throughout all stages)
```

One-liner owners: Logistician = *which/procure*; Portfolio Manager = *verify*;
Operation Loop Formation = *assemble + simulate*; Scout Command = *deploy*.

---

## The ~90-Second Pitch

> "The AGMS patent family describes one complete assembly line for autonomous grid response.
> The parent patent — the Adaptive Power Grid Management System — defines the whole
> architecture: detect a multi-source alert condition, build a contextual-and-cognitive state
> machine, and send a formation plan downstream. The five continuation patents each own one
> stage of that plan's execution. The Logistician Module takes the abstract formation plan and
> decides *which* assets are needed, procuring and auditing a provisional logistics list.
> The Asset Portfolio Manager then *verifies* each candidate asset across seven operational
> indexes — observability, reachability, adaptability, controllability, security, sustainability,
> stability — before clearing it for inclusion. Operation Loop Formation, which is the GRANTED
> GE Vernova patent, takes the verified list and *assembles* the ORACS operation loop: it
> matches a behavioral schema from history, builds per-asset meta objects, simulates the loop
> before committing, and only then causes execution. Scout Command then *deploys* the scout
> software — role-typed Coordinator, Messenger, Inspector, Guard agents — onto the actual
> field hardware per a time-ordered launch plan. And Data Management runs throughout all
> stages, serving each module a role-filtered Point of View file rather than raw database
> access. When I read through this family I recognized the architecture I've been building in
> buildings and DER: edge orchestration, typed asset models, schema-matched behavior, a
> simulate-before-commit control gate, and autonomous field agents. Coming here means applying
> that experience at T&D scale."

---

## Patent 1: Adaptive Power Grid Management System (Parent)
**WO 2023/064623 A1 | Sharif-Askary | General Electric Company**
*(full reference: `.planning/research/patents/adaptive-power.md`)*

### Summary

The parent patent establishes the end-to-end AGMS architecture for autonomous grid response:
it detects multi-source alert conditions, correlates them into an "action stress frame," and
feeds a three-layer system — GridWideMind (alert correlation and ML), GridArtificer (contextual
reasoning and state machine construction), and GridWideCommandHub (orchestration and deployment)
— that produces a Contextual and Cognitive State Machine (CaCSM) and deploys lightweight
"scout" applications to self-organizing clusters of field agent devices. The key payoff is that
operating cells can execute their formation plan autonomously for hours or days without WAN
connectivity — the grid fragments never go blind.

### My Connection

My OSED edge platform is the runtime that scout applications would land on: I built the full
operating-cell stack — MQTT telemetry ingestion, local ML inference, CVXPY convex-optimization
control loop, and K8s orchestration — every component an operating cell needs to function, just
in a buildings-and-DER domain rather than a T&D substation.

### Question for the Director

> "The CaCSM Simulation Engine runs a provisional state machine to calibrate state transitions
> before promoting it to production — very similar to MPC's solve-before-commit philosophy.
> In practice, how do you handle the tension between simulation fidelity and real-time latency
> when the grid is evolving faster than the simulation can converge? Do you use simplified
> surrogate models, or is there a degraded-mode path that promotes an under-calibrated state
> machine under time pressure?"

---

## Patent 2: Logistician Module
**US 2024/0337997 A1 | Sharif-Askary | GE Infrastructure Technology LLC**
*(full reference: `.planning/research/patents/logistician-module.md`)*

### Summary

On receipt of a CaCSM-authorized formation plan, the Logistician Module translates the plan's
abstract tasks and class requirements into a concrete, audited provisional logistics list: it
matches the formation context to a historical template, selects asset classes and individual
assets by observability/reachability/resiliency/security indexes, procures them from a
marketplace, audits the list against the combined task requirements, and hands the verified list
to the downstream Portfolio Manager. Critically, the Logistician stays the standing owner of
any unresolved inter-ORACS logistic gap files — it keeps open the replenishment loop until
every participant slot is filled.

### My Connection

My OSED FastAPI control plane is the Logistician's analog in the buildings domain: it takes
an abstract job request, resolves it into concrete K8s/K3s workloads placed on specific edge
nodes, health-checks and monitors them, and reschedules on failure — the same "general
contractor" control-plane pattern that turns an abstract formation plan into placed, audited,
running work.

### Question for the Director

> "The Logistician builds the provisional logistics list by matching the context meta object
> against a logistics-list historical archive, and it stays the owner of the inter-ORACS gap
> files when participants are missing. In practice, how aggressive is that historical-archive
> matching versus first-principles re-planning — when a formation plan hits a novel context with
> no good historical template, does the Logistician fall back to a from-scratch class/asset
> solve, and how do you keep the learning engine from over-fitting to past logistics patterns
> in a grid whose asset population is constantly changing?"

---

## Patent 3: Asset Portfolio Manager
**WO 2024/211758 A1 | Sharif-Askary | GE Infrastructure Technology LLC**
*(full reference: `.planning/research/patents/asset-portfolio.md`)*

### Summary

The Asset Portfolio Manager is the "are the assets fit" gate between the provisional logistics
list and the verified logistics list: it checks every candidate asset against seven operational
indexes — observability, reachability, adaptability, controllability, security, sustainability,
stability — and runs an ORACS resource interdependency analysis to map 1-to-n and n-to-n
cascading dependencies before clearing assets for formation. Assets that fail any threshold
trigger the asset replacement processor, which routes a replenishment request back to the
Logistician. Only fully verified assets advance to the Operation Loop Formation stage.

### My Connection

When I built SI-MAPPER I was solving the same core problem as the DNA map in this patent: I
needed a typed, relationship-aware asset fingerprint — based on the ASHRAE 223P ontology — so
automated agents could reason about inter-asset dependencies without human configuration.
SI-MAPPER's knowledge graph traversal is the same dependency-graph analysis the Asset Portfolio
Manager performs using DNA matching.

### Question for the Director

> "The ORACS operational index has six dimensions — observability, reachability, adaptability,
> controllability, sustainability, stability. How are these indexes derived in practice: are they
> continuously updated from telemetry in real-time, or are they pre-computed from historical
> operational data and refreshed on a schedule? And when a formation plan needs to execute under
> a tight time constraint, is there a mechanism to accept an asset with a marginal index on one
> dimension if all other dimensions are strong?"

---

## Patent 4: Operation Loop Formation ★ (GRANTED — GE Vernova's own IP)
**US 12,596,341 B2 | Sharif-Askary | GE Vernova Infrastructure Technology LLC**
*(full reference: `.planning/research/patents/operation-loop.md`)*

This is the keystone. Take a breath and let it land: this is a **granted US patent assigned to
GE Vernova** — the hiring company's own live IP. Every word here is enforceable.

### Summary

The Formation Construct Module (1400) takes the verified formation plan and logistics list and
physically assembles the ORACS operation loop: it retrieves a matching behavioral schema (DNA)
from a historical meta-object database, constructs per-asset meta objects that encode each
asset's role and behavior, runs the full loop in a learning/simulation engine to validate
operability and inter-asset interdependencies — and only then causes the network of devices to
execute. The simulate-before-commit discipline is explicit in claim 3: a learning engine
simulates the formation plan against historical archives before the module commits to execution.
Never dispatch on an unvalidated plan.

### My Connection

Claim 3 of this granted patent gates execution on a learning engine that simulates the
operation loop before causing the devices to execute — that is the exact discipline I shipped
in OSED with CVXPY MPC: I solve and feasibility-check the control problem first, then commit
to the actuators. The simulate-before-commit gate is not a coincidence; it is the correct
control discipline for any system where a bad commit causes a physical consequence you cannot
easily undo.

### Question for the Director

> "The operation loop formation patent gates execution on a learning engine that simulates the
> formation plan to calibrate asset interdependency. In a real substation event, the
> interdependency simulation is racing the physical disturbance. When the ORACS cannot be fully
> validated in time — say a critical asset's health index is stale or the inter-ORACS gap file
> is not closed — does the formation construct module promote a partially-validated operation
> loop in a degraded or bounded-authority mode, or does it hold execution until the simulation
> converges? Where is the line between simulate-before-commit and the grid needs an action
> right now?"

---

## Patent 5: Scout Command
**US 2024/0339835 A1 | Sharif-Askary | GE Infrastructure Technology LLC**
*(full reference: `.planning/research/patents/scout-command.md`)*

### Summary

Scout Command is the deployment and orchestration subsystem that turns the constructed ORACS
operation loop into running software on the field hardware: the Scout Incubator Manager checks
which role-typed scouts — Coordinator, Messenger, Inspector, Guard — are available for the
DNA-specified requirements, clones or fresh-incubates new scouts when slots are unfilled, and
feeds the rosters to the Scout Launch Manager, which builds a time-ordered launch plan
specifying load, origin, destination, and asset ID for each host and participant scout.
Operating cells launch autonomously and can clone, self-form, or terminate in response to
triggers — without any WAN round-trip to AGMS.

### My Connection

The Scout Incubator Manager is a Kubernetes scheduler with grid semantics: it checks desired
role availability against a typed DNA map and instantiates new agents when a role is unfilled,
exactly as my K3s scheduler places role-typed workloads — inference service, MQTT messenger,
monitoring sidecar — on OSED edge nodes, reconciling desired state by cloning or replacing
pods when a role drops off the cluster.

### Question for the Director

> "Scout Command verifies participant availability against assigned roles and, when a role is
> unfilled, either clones an existing scout or initiates a fresh incubation-and-training cycle
> before launch. In a fast-moving disturbance where the launch plan also has to specify time,
> load, origin, and destination — how do you bound the incubation latency so it does not blow
> the formation timing? Is there a notion of pre-incubated warm scout pools on the launchpad
> per DNA type, analogous to a warm container pool, and does the launch plan's time field
> schedule against that warm pool, or is incubation always on the critical path?"

---

## Patent 6: Data Management
**WO 2024/211800 A1 | Sharif-Askary | GE Infrastructure Technology LLC**
*(full reference: `.planning/research/patents/data-management.md`)*

### Summary

The Data Management patent introduces the POV (Point of View) file system: the data management
module is the sole gateway to the asset database, and every AGMS module — the Grid Wide
Formation Manager, GridwideEye, CSM Operator, ORACS correlation engine — receives only a
role-filtered, context-appropriate slice of asset data assembled on demand using a patterns
database that encodes what each module role should see. The three construct types — view (for
situational awareness), control (for action lists), and admin (for app collaboration) — ensure
no module receives data outside its operational context. The ga-authenticationkey token must be
validated by the GateKeeper before any POV frame is released.

### My Connection

My OSED FastAPI service layer IS the data management module for my edge platform: all sensor
data access goes through a FastAPI service that assembles role-scoped responses, edge nodes
never query InfluxDB directly, and the gRPC service-to-service auth tokens in OSED plus the
MCP server tool-call authentication in SI-MAPPER map directly to the ga-authenticationkey
access gate in this patent.

### Question for the Director

> "The POV file patterns database is central to the whole data management design — it encodes
> what each module role should see. How is that patterns database populated and evolved? Is it
> hand-authored by domain engineers at design time, or does the Learning Engine update it based
> on observing which patterns actually resulted in effective formation outcomes? And is there a
> mechanism to detect when existing patterns are insufficient for a novel grid condition and
> trigger a human-in-the-loop review?"

---

## Closing: The Master Narrative

> "The patent family describes a platform I have been building the components of —
> independently, in a different domain (buildings and DER), but with the same architectural
> DNA. It is one assembly line: the Logistician decides *which* assets, the Portfolio Manager
> *verifies* them, Operation Loop Formation *assembles and simulates* the ORACS loop, and
> Scout Command *deploys* the scouts. My OSED platform is the edge runtime those scouts would
> land on — I built the telemetry stack, the local ML inference, the K8s orchestration layer,
> and the convex-optimization control loop. My K3s scheduler is the Scout Incubator Manager
> with grid semantics: it places role-typed workloads on field nodes and reconciles desired
> state by cloning or replacing when a role drops. SI-MAPPER is the DNA map: a typed,
> relationship-aware asset fingerprint built from a CV-to-ontology pipeline, using ASHRAE 223P
> the same way the patents use the schema/DNA store. My CVXPY MPC is the simulate-before-commit
> gate that the granted Operation Loop patent — GE Vernova's own IP — puts in its allowed
> claims. And my Databricks substation analytics pipeline is the data foundation that feeds
> the alert correlation and asset-health layers. Coming to GE Vernova means integrating those
> experiences into a T&D-scale version of exactly this architecture."

---

## Quick-Reference Cheat Sheet

| Term | What it means (say-aloud version) |
|------|-----------------------------------|
| AGMS | Adaptive Grid Management System — the full platform covering all six patents |
| GWM / GA / GWCH | The three top-level modules: GridWideMind (intelligence), GridArtificer (reasoning/state machine), GridWideCommandHub (orchestration) |
| CaCSM | Contextual and Cognitive State Machine — the core reasoning engine GA builds from alert context; drives the whole formation pipeline |
| CAP | Contextual Abstraction Panel — a ranked contextual grouping that CaCSM is built from |
| ORACS | The operation loop unit; patents define it as Observability, Reachability, Adaptability, Controllability, Security (five indexes; seven with sustainability + stability for asset verification) |
| DNA / schema | Synonyms: the unique structured fingerprint encoding an ORACS's role, behavior, asset composition, and scout roster — the template the Formation Construct Module matches from history |
| Meta object | The per-asset constructed object — carries DNA map, logistics, scout roster + launch plan — that "causes an asset to execute a task" |
| Scout roles | Coordinator (s_c, cell authority), Messenger (s_m, data in motion), Inspector (s_i, monitoring), Guard (s_g, security) |
| POV file | Point of View file — role-filtered data view served by the data management module; no AGMS module queries the asset DB directly |
| ga-authenticationkey | The security token every inter-module message carries; validated by ga-GateKeeper before any command or data release |

*(Source: INDEX.md "Key Technical Terms Cheat Sheet" — condensed to the eight terms most likely
to come up in conversation with the director.)*
