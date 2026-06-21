# Appendix — Self-Healing Distribution Networks (FLISR and the Action Layer)

## Purpose & framing

The two companion appendixes stop at the *state*: the
[device inventory](appendix-distribution-observability-sources.html) enumerates what a feeder
can **observe**, and the [virtual sensing module](appendix-virtual-sensing-module.html) turns
those observations into the reconstructed network state plus its uncertainty. **This appendix
is about what you *do* with that state** — the **action layer** that detects a fault, isolates
it, and restores service. It is a standalone study card, grounded in two source papers:

- **Arefifar, Alam & Hamadi (2023)**, *"A Review on Self-Healing in Modern Power Distribution
  Systems,"* J. of Modern Power Systems & Clean Energy — the **taxonomy**: stages, control
  actions, objective functions, optimization algorithms, centralized vs. distributed
  architectures, and the open research frontier.
- **Meteab, Tousi & Omran (2025)**, *"Efficient self-healing framework for smart distribution
  networks,"* Scientific Reports — a **concrete worked framework**: an IEEE 33-bus feeder
  with a three-phase fault, isolated and restored by tie-switch reconfiguration with PSO-placed
  distributed generation.

The interview value is the layering. Virtual sensing is the *eyes*; self-healing is the
*hands*. The job description names both — "voltage stability, phase angles, line temperature,
asset health" (sensing) and "decentralized grid operations" (acting) — and self-healing is the
loop that closes one onto the other. Where it touches the AGMS family, self-healing is the
**ORACS operation loop in execution**: detect (Observability), reach the switches
(Reachability), reconfigure (Controllability), simulate-before-commit (the granted Operation
Loop Formation patent, US 12,596,341 B2), and ride out WAN loss as an island (the operating
cell).

> **One sentence:** self-healing is the closed loop that consumes the reconstructed grid state
> and *acts on it* — **F**ault **L**ocation, **I**solation, and **S**ervice **R**estoration —
> autonomously, in milliseconds-to-minutes, with minimal human intervention.

## Self-healing vs. resilience — get the distinction right first

The single sharpest framing in the review (Arefifar §II) is a distinction interviewers love to
test, because the words are used interchangeably in marketing and they are **not** the same:

| | **Self-healing** | **Resilience** |
|---|---|---|
| Question it answers | *How fast do I recover **after** the hit?* | *How well do I **withstand** the hit?* |
| Temporal position | **After** the incident — minimize its impact | **Around** the incident — absorb / survive it |
| Metric flavor | Restoration time, customers restored, unserved load | Withstand a low-frequency high-impact event |
| Relationship | Self-healing **improves** resilience | Resilience is the broader property |

> **The trap is** calling a system "resilient" when you mean it reconfigures quickly after a
> fault. Say it precisely: *resilience is the ability to withstand the disaster; self-healing
> is the ability to recover from a fault automatically once it has happened — and a good
> self-healing system raises the system's resilience.*

Both source papers anchor self-healing to its origin: the term comes jointly from the U.S. DOD
and EPRI's *Complex Interactive Networks* initiative, and NETL's "modern grid" view names
self-healing as the **defining characteristic of a smart grid** — the ability of the grid to
*automatically and intelligently* restore itself after faults.

## FLISR — the four-stage loop

Self-healing is not one act; it is a **staged loop**. Arefifar decomposes it into four stages;
Meteab collapses the same idea into a three-phase engineering pipeline. Lining them up is the
cleanest way to hold the whole thing in your head:

| Arefifar stage (review taxonomy) | Meteab phase (worked framework) | What happens |
|---|---|---|
| **1. Fault Detection** | Fault Detection & Isolation | Sensors/relays see the abnormal event (overcurrent, voltage anomaly) as fast as possible |
| **2. Fault Understanding** (classification + location) | *(folded into detection)* | Classify the fault (symmetrical vs. unsymmetrical; LG / LL / LLG) and **locate** it |
| **3. Fault Isolation** | *(isolation)* | Trip breakers / open switches to disconnect the faulted segment from healthy feeder |
| **4. Service Restoration** | Network Reconfiguration → Power Restoration | Reroute power from available sources to downstream healthy loads |

The industry acronym for the whole loop is **FLISR — Fault Location, Isolation, Service
Restoration.** Per the U.S. DOE figure both papers cite, FLISR cuts **customer minutes of
interruption by ~51%** and **the number of customers interrupted by ~45%** for an outage event.
That single statistic is the business case — memorize it.

> **One sentence:** FLISR = *find the fault, fence it off, feed the rest from somewhere else* —
> and doing it without a truck roll is worth roughly half your outage-minutes.

**Detection nuance** worth a sentence in the room: detection is "straightforward" only on a
slide. On a real feeder, distinguishing a true fault from a transient inrush, and *locating* it
with sparse sensing, is exactly where the **virtual-sensing state estimate earns its keep** —
the residual/χ² bad-data machinery from the sensing appendix is a fault *detector*, and the
reconstructed state narrows the *location*.

## The five control actions (the verbs of restoration)

Once a fault is isolated, restoration is performed through a set of **control actions**.
Arefifar (§IV) classifies them into five; Meteab's framework exercises the first two heavily
and the others implicitly. These are the levers a self-healing controller pulls:

| # | Control action | What it does | Seen in Meteab's IEEE-33 case |
|---|---|---|---|
| 1 | **Grid reconfiguration** | Open/close sectionalizing + tie switches to re-route power while keeping the feeder **radial** | ★ core — open Sw-8/Sw-9, close tie Sw-35 |
| 2 | **DG output control** | Dispatch distributed generators to supply load locally; needs **forecasted** DG/load to plan | ★ PSO-sized DGs at buses 6 & 32 backstop the restored zone |
| 3 | **Load management** | Shed / curtail by **customer priority** when sources can't cover all load | implicit (restore max load within limits) |
| 4 | **Energy storage control** | Discharge BESS to energize remaining loads when DG is insufficient | — (named as the resilience extension) |
| 5 | **Reactive power source control** | Switch caps/reactors or use smart-inverter Volt-VAR to hold voltage in band | implicit (voltage profile constraint) |

> **The trap is** treating "self-healing" as synonymous with "reconfiguration." Reconfiguration
> is the **first and most common** control action, but the modern story is the *coordination* of
> all five — DG dispatch, storage, load priority, and reactive support **together** — which is
> exactly the multi-resource orchestration the AGMS operating cell is built to do.

**Reconfiguration's two jobs** (Arefifar §IV-A), worth saying explicitly: it both (a) *isolates*
the faulted zone to stop the fault current hurting healthy loads, and (b) *reroutes* power to
the downstream loads. One mechanism, two purposes — isolation **and** restoration.

## Worked example — the IEEE 33-bus self-healing run (Meteab et al.)

This is the appendix's one **concrete, say-aloud** example — a small enough system to draw on a
whiteboard, large enough to be credible. Know these numbers.

**The testbed.** IEEE 33-bus radial feeder, 12.66 kV, total load **3715 kW + 2300 kVAR**,
**32 sectionalizing switches** (normally closed) + **5 tie switches** (normally open). Initial
load-flow: losses **202.66 kW**, minimum voltage **0.90 p.u. at bus 17**, with under-voltage
(<0.95 p.u.) in 19 sections — i.e. it starts out stressed.

**The method stack** (each piece is a small interview hook):

| Step | Tool | Why it's the right choice here |
|---|---|---|
| Load flow | **Backward/Forward Sweep** | Purpose-built for **radial** feeders with **high R/X**, where Newton-Raphson and Gauss-Seidel struggle to converge |
| DG sizing & placement | **Particle Swarm Optimization (PSO)** | Fast, swarm information-sharing convergence; beats GA/WOA on speed for this loss-minimization objective |
| Restoration | **Tie-switch reconfiguration** | Close a normally-open tie to back-feed the isolated healthy zone, keeping radiality |

**The fault and the fix.** A three-phase short (a "big disturbance") is dropped in **Section 8**.
The loop:

1. **Detect & isolate** — the relay trips, opening **Sw-8** (and **Sw-9**) to fence off the
   faulted line. This disrupts power to Sects. 8–17: an unserved load of **815 kW**.
2. **Reconfigure** — open **Sw-9**, **close normally-open tie Sw-35** — the optimal switching
   that minimizes losses and balances load while *staying radial*.
3. **Restore** — the 815 kW flows back to feeders 9–17 through the tie. With the PSO-placed DGs
   backstopping, post-fault losses drop to **48.6 kW (a 76% reduction vs. 202.66 kW)** and the
   minimum voltage recovers to **0.94 p.u.** — all within acceptable 0.95–1.05 limits after DG.

**The headline number:** in the MATLAB/Simulink run, voltage at bus 9 re-stabilizes to
**0.947 p.u. within ~60 milliseconds** of the fault, using only **three switch operations per
fault** (one bus-bar trip, one downstream trip, one tie-close).

> **The trap is** quoting "60 ms" as if a truck-roll restoration is being beaten by seconds. The
> 60 ms is the **automated switching transient** in simulation — the point is *no human in the
> loop*, fully automatic detect-isolate-reconfigure, not the multi-minute manual dispatch it
> replaces.

## Permanent vs. temporary fault — the decision branch

Meteab's Fig. 1 encodes a branch that is easy to forget and good to volunteer: the **smart
recloser's first action** is *disconnect & reclose*. What happens next depends on the fault:

| Fault type | Recloser outcome | Self-healing response |
|---|---|---|
| **Temporary** (e.g. branch contact, transient) | Reclose **succeeds** — fault clears | Restore power via the **regular** supply; no reconfiguration needed |
| **Permanent** (e.g. three-phase short) | Reclose **fails** — fault persists | **Isolate** the affected area and use **microgrid / DG sources** to restore the unaffected zone |

> **One sentence:** the recloser's reclose attempt is a free *test* — it weeds out transient
> faults cheaply, so the expensive reconfiguration logic only fires for the **permanent** ones.

This is the substrate for the next card: when the fault is permanent and the main feed is gone,
restoration leans on **local generation running in island mode** — the resilience extension.

## Networked microgrids and island-mode restoration

Both papers converge on the same resilience pattern. Arefifar (§VII-H) names **networked
microgrids** as a leading future direction; Meteab operationalizes it (permanent fault →
microgrid sources restore the unaffected area). The idea:

- When a fault severs a zone from its source, the de-energized area is **sectionalized into an
  islanded microgrid** that **autonomously supplies** its customers from local DG + storage —
  rescheduling DG output to cover as many affected loads as possible.
- **Multiple points of common coupling** within a networked microgrid let healthy sub-grids
  **compensate** for shortages in the faulted area — a self-sufficient micro-grid formed *on
  demand* for the duration of the outage.
- The hard problem the review flags as still-open: **priority-based formation** of those
  microgrids under uncertainty — *which* loads to energize first when local generation can't
  cover them all (load management by customer priority, control action #3).

**Where this lands on the AGMS architecture** (kept light, standalone): an on-demand islanded
microgrid that self-forms, restores critical load, and self-terminates when the WAN/main feed
returns is — almost verbatim — the patents' **operating cell that "operates autonomously
without WAN" (island mode)**. The self-healing literature and the patent family are describing
the same object from two directions.

## Centralized vs. distributed self-healing (the architecture fork)

The review (§VI-E, §VII-E, and the Centralized-Approach discussion) draws the fork that maps
straight onto the role's "**decentralized** grid operations" language:

| | **Centralized** | **Distributed / decentralized** |
|---|---|---|
| Data path | IEDs → **SCADA** → control center; strategy computed centrally | **Peer-to-peer** multi-agent; agents exchange messages and decide locally |
| Decision locus | One control center plans the restoration | Feeder / zone / switch / DG **agents** cooperate (the multi-agent pattern) |
| Strength | Global optimum, full-system view, simpler to reason about | Survives comms loss; scales; lower latency; local autonomy |
| Weakness | Single point of failure; latency; comms-dependent | Harder to guarantee global optimality; coordination complexity |
| Future-work flag (review) | "overcoming the limitations of the centralized approach" | the **research frontier** the review pushes toward |

> **The trap is** assuming centralized = obsolete. The review is explicit that centralized
> approaches are *"gaining attention"* again (HPC/GPGPU make central optimization fast), while
> distributed multi-agent is where resilience lives. The honest answer is **hybrid**: a
> centralized planner that degrades to distributed agent autonomy when the WAN drops — which is,
> again, the AGMS operating-cell story.

This fork is the cleanest bridge to the **federated multi-area** thread in the virtual-sensing
appendix (its [Thread C / D3](appendix-virtual-sensing-module.html#open-decisions)): hierarchical
(coordinator reconciles) vs. peer-to-peer (consensus, survives WAN loss) is the *same* fork, one
layer up — federation for *estimation* there, for *restoration* here.

## Objective functions and algorithms (the optimization underneath)

Restoration is an **optimization problem**: pick the switching/dispatch plan that best satisfies
an objective under radiality, voltage, and current constraints. The review (Fig. 3, Tables I–II)
catalogs both the objectives and the solvers — useful to recognize, not to derive.

**Eight objective functions** self-healing papers optimize for:

| Objective | Plain-English goal |
|---|---|
| Reduce power losses | minimize `I²R` over the restored configuration (Meteab's PSO target) |
| Minimize recovery time | restore the most load in the least time |
| Minimize operational cost | cheap generators, less load-shed, shorter transfer distance |
| **Minimize number of switching operations** | fewer switch ops = faster, less equipment wear (Meteab's 3-switch result) |
| Improve voltage profile | hold every bus inside 0.95–1.05 p.u. |
| **Improve system observability** | place PMUs so the restored network stays observable |
| Enhance system resiliency | survive high-impact events; mobile resources, multi-microgrids |
| Enhance system reliability | reduce SAIDI/SAIFI-type interruption exposure |

**Solver families** the review tabulates (recognize the names):

```
MILP / MINLP            the workhorses — switching + load-shed + restoration as integer programs
Multi-agent             feeder/zone/switch/DG agents cooperate (distributed restoration)
Graph theory            spanning-tree / connectivity reasoning for radial reconfiguration
Heuristics / metaheur.  PSO (Meteab), GA, Tabu search, fuzzy logic, ant-colony, GWO
Dynamic programming     staged restoration toward the global optimum
```

> **The trap is** getting pulled into solver math in the room. The interview-grade point is the
> *shape*: restoration is a **constrained combinatorial optimization** — discrete switch states,
> continuous DG/var dispatch, hard radiality + voltage/current limits — and **simulate-before-
> commit** (validate the candidate plan in a power-flow/load-flow before you actually throw the
> switches) is the safety gate. That gate is literally claim 3 of the granted Operation Loop
> Formation patent.

## The open frontier (what the review says is still hard)

Arefifar's §VII (Future Work) is a ready-made list of "where the role's work goes next" — each a
talking point that connects self-healing back to the sensing stack and the JD:

| Frontier | Why it's open | Connects to |
|---|---|---|
| **Improve observability** | restoration needs the network to stay observable; optimal **PMU placement** under changing topology | the device-inventory + virtual-sensing appendixes directly |
| **Accurate forecasting** | non-dispatchable DG/RES output is uncertain; restoration planning needs **forecasted** load & generation | FASE predict-step / pseudo-measurements (sensing appendix) |
| **Cyber security** | control actions are only as trustworthy as the data; any cyber-attack corrupts the heal | the patents' `ga-authenticationkey` / POV trust boundary |
| **Event-prediction models** | predict critical events (cascades, weather, cyber) *before* they hit — pre-emptive healing | GWM alert-correlation / learning engine (AGMS) |
| **Networked microgrid formation** | priority-based, uncertainty-aware islanding is unsolved | island-mode operating cells (AGMS) |
| **High-performance computing** | real-time restoration at scale needs GPGPU/HPC acceleration | edge-compute placement (deployment story) |

> **One sentence:** every open problem in self-healing is *"the action layer is only as good as
> the state estimate and the forecast feeding it"* — which is precisely why virtual sensing and
> self-healing are one system, not two.

## Wrap-up — where self-healing sits

A standalone closer, not a deployment-proposal continuation. The clean mental stack, top to
bottom:

```
   STATE          observe the grid            → device inventory  (see also: that appendix)
     │            reconstruct + uncertainty   → virtual sensing module (see also: that appendix)
     ▼
   ACTION         FLISR: detect → isolate → restore   ← THIS appendix
     │            via 5 control actions, optimized, simulate-before-commit
     ▼
   RESILIENCE     island-mode microgrids, networked PCCs, priority restoration
```

Self-healing is the **action layer**: it is what makes the reconstructed state *worth*
reconstructing. The two source papers split the labor cleanly — **Arefifar** gives the map (the
distinction from resilience, the FLISR stages, the five control actions, the centralized↔
distributed fork, the open frontier), and **Meteab** gives the worked route (IEEE 33-bus,
BW/FW + PSO, a Sect.-8 fault isolated and restored through tie Sw-35 in ~60 ms with a 76% loss
cut).

For Juan, the interview-speakable through-line is short: *"I've built the sensing and the edge
orchestration; self-healing is the FLISR control loop that sits on top — detect with the state
estimate, isolate with the switches I can reach, restore by reconfiguring and dispatching DG,
and validate the plan before committing — and when the WAN drops, that loop keeps running as an
island. That last property is the AGMS operating cell, and the simulate-before-commit gate is
the granted Operation Loop Formation patent."*

The companion appendixes ([device inventory](appendix-distribution-observability-sources.html),
[virtual sensing module](appendix-virtual-sensing-module.html)) are the *state* half; this one
is the *action* half — they read independently, but together they are eyes-and-hands.
