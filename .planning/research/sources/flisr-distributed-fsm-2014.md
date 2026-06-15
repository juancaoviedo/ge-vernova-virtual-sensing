# Source: Distributed FLISR as a Finite-State Machine over IEC 61850

## Citation

> Cosmin Koch-Ciobotaru, Mehdi Monadi, Alvaro Luna, Pedro Rodriguez,
> **"Distributed FLISR Algorithm for Smart Grid Self-Reconfiguration based on IEC 61850,"**
> 3rd International Conference on Renewable Energy Research and Applications (ICRERA), Milwaukee,
> USA, 19–22 Oct 2014. IEEE, pp. 418–423.
> Affiliations: Technical University of Catalonia (UPC), SEER Center; Abengoa Research.

Source file: `docs/flisr.pdf` (6 pages, text-native — no OCR needed).

---

## What it is (one paragraph)

A concrete, published design for **decentralized self-healing of a distribution feeder.** Instead of
a central controller computing the restoration switching, **each circuit breaker runs the *same*
algorithm, implemented as an event-driven finite-state machine**, and the breakers cooperate by
exchanging **IEC 61850 GOOSE messages** with their immediate neighbors only. Collectively, the local
machines reconfigure the grid to re-energize the maximum number of loads after a fault — no central
brain, no global model.

---

## Key technical content

**Three breaker "agents," each its own finite-state machine (Fig. 2 a/b/c):**
- **Circuit breaker** — connects the feeder to the transformer.
- **Sectionalizing breaker** — separates sections on the same feeder.
- **Tie breaker** — interconnects neighboring feeders (the alternate-supply path).

The states are grouped into **7 numbered states** (State1 = nominal/initial; State7 = idle/no-action;
after a crew clears the fault and resets, the FSM returns to State1). Transitions are **event-driven**,
fired by *local measurements* (overcurrent) or *messages from neighbors*.

**The global behavior unfolds in three phases:**
1. **Phase I — fault isolation (cascade downstream).** A breaker detects overcurrent, opens, and sends
   two GOOSE messages downstream: a *trip* message and the *measured current* prior to the fault. Each
   downstream breaker opens on receiving the trip and forwards the pair — cascading to the end of the feeder.
2. **Phase II — search upstream.** Starting from the last breaker, the feeder is "covered" upstream to
   find a **tie breaker** connected to a neighboring feeder with **spare current capacity.**
3. **Phase III — restore.** The qualifying tie breaker closes and energizes the recoverable section
   from the neighboring feeder — repeated until the feeder is restored or the neighbor's capacity is reached.

**Communication:** IEC 61850 **GOOSE**, with the standard's **~5 ms** peer-to-peer delivery; signals
(Table I) include `OverCurrent`, `RecTrip`, `SendTrip`, `SendPrimaryTrip`, section-load values, tie-breaker
exchanges, and cover-direction flags — to be mapped to IEC 61850 **Logical Nodes.**

**KPIs:** SAIDI (System Average Interruption Duration Index), **CARTI** (Customers' Average Restoration
Time Index), and **FoS** (Fraction of Served nodes) — FoS is the paper's efficiency indicator.

**The honest tradeoff (important):** the distributed approach computes a **fast local optimum**, not the
global optimum. Grid reconfiguration is **NP-complete** — the true optimum needs a holistic, centralized
view exploring all configurations. So: *centralized = global-optimal but slow and needs full observability;
distributed = sub-optimal but fast, modular, and needs only neighbor data.*

---

## Why it matters for our notes / the role

This single paper independently validates several of the architecture's central claims with a real,
citable engineering design:

- **"Decentralized self-healing as a state machine" is real, not hand-waving.** AGMS's distributed
  FLISR / loop schemes (study note Appendix C/E.7) and the whole "operating cells run a state machine
  locally" thesis (AGMS-architecture Part 3, Appendix F meaning ③) are exactly what this paper builds —
  an FSM per device, driven by local events and neighbor messages.
- **It grounds the centralized-vs-decentralized tradeoff** the notes lean on (Appendix C, Part 0/7): the
  paper states plainly that distributed FLISR trades global optimality for speed and modularity. AGMS's
  "act locally in seconds, survive loss of the center" bet is the same tradeoff, made deliberately.
- **It ties FLISR to IEC 61850 / GOOSE** — a *preferred qualification* in the job description. Being able
  to say "distributed FLISR is implemented as an FSM exchanging GOOSE messages between breakers, ~5 ms"
  shows real T&D fluency.
- **It is the simplest concrete instance of an AGMS scout/operating-cell idea**: same algorithm on every
  field device, neighbor-only messaging, collective self-reconfiguration — a 2014 special-purpose
  ancestor of the generalized, learning-driven version the patents describe.

## Interview talking points

- "FLISR can be centralized in the ADMS or distributed across the breakers. The distributed version is
  literally a finite-state machine per breaker exchanging IEC 61850 GOOSE with its neighbors — that's the
  decentralized self-healing the role is generalizing."
- "The catch is that reconfiguration is NP-complete, so distributed FLISR gets a fast *local* optimum, not
  the global one — which is exactly the speed-vs-optimality tradeoff behind decentralized grid operations."
- "Where AGMS goes further: instead of a *fixed* FSM hard-coded into each breaker, the response state
  machine is selected/built from learned patterns per situation — fixed logic becomes reasoning."

## Where it is cited in our notes

- Study note [`grid-operations-and-role.md`](../grid-operations-and-role.html) — Appendix E.7 (distributed FLISR).
- Relates to [`patents/AGMS-architecture.md`](../patents/AGMS-architecture.html) Part 3 (the CaCSM as a state machine) and Appendix F
  (meaning ③, the plan-step state machine).
