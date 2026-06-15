# Source: MAPE-K and AWARE — the Self-Adaptive-Systems Vocabulary for AGMS

## Citation

> Brell Sanwouo, Clément Quinton, Paul Temple,
> **"Breaking the Loop: AWARE is the New MAPE-K,"**
> 33rd ACM International Conference on the Foundations of Software Engineering (FSE Companion '25),
> Trondheim, Norway, 23–28 June 2025. ACM, 5 pages. [https://doi.org/10.1145/3696630.3728512](https://doi.org/10.1145/3696630.3728512)
> Affiliations: Univ. Lille / Univ. Rennes, CNRS, Inria, CRIStAL / IRISA.

Source file: `docs/mapek.pdf` (5 pages, text-native — no OCR needed).

Background reference (the original): J. O. Kephart & D. M. Chess, "The Vision of Autonomic Computing,"
IEEE Computer, 2003 — which introduced the **MAPE-K** loop.

---

## Why this source matters

It gives us the **established software-engineering vocabulary** for what AGMS *is* as a class of system:
a **self-adaptive system** built on an **autonomic feedback loop.** Being able to name the paradigm —
and to position AGMS against both the classic loop (**MAPE-K**) and the 2025 frontier (**AWARE**) — lets
Juan describe the patent architecture in terms a CTO-org software audience already respects, instead of
only in the patents' bespoke vocabulary.

---

## MAPE-K in one paragraph

**MAPE-K** (Kephart et al., IBM, ~2003) is the canonical loop for **self-adaptive systems** — systems that
adjust their own behavior at runtime. A *managing system* (the adaptation logic) controls a *managed system*
through a cyclic loop:
- **Monitor** — collect raw/aggregated data from the managed system and its environment.
- **Analyze** — evaluate adaptation options and their feasibility against the system's goals.
- **Plan** — select the best option and produce an actionable plan to reach the desired configuration.
- **Execute** — carry out the planned actions (often automatically).
- **K (Knowledge)** — a *centralized* shared knowledge base supporting all four phases.

It's widely used in cloud computing, IoT, cyber-physical systems, networks, and security.

## The paper's critique of MAPE-K (the limitations AGMS answers)

1. **Monitor sees only raw data** — no contextual interpretation, so root causes are hard to understand.
2. **Strictly sequential (M → A → P → E)** — inherently **reactive**; cannot anticipate or explore future scenarios.
3. **Centralized knowledge base** — poor fit for distributed/collaborative settings; limits flexibility and scalability.
4. **No built-in continuous learning** — cannot refine decisions from past experience.
   (Even "LLM-enhanced MAPE-K" only patches individual phases; the loop stays sequential and centralized.)

## AWARE (the proposed evolution)

**AWARE = Assess, Weigh, Act, Reflect, Enrich** — a **distributed, goal-driven** framework of autonomous,
collaborating **AI agents** with proactive anticipation and continuous learning:
- **Assess** [observe & *understand*] — contextual/semantic perception beyond raw monitoring; understand root causes.
- **Weigh** [evaluate & decide] — agents formulate *multiple* adaptation options, score them (cost/risk/performance), and **negotiate** (merges MAPE-K's Analyze + Plan).
- **Act** [execute] — multiple agents apply decisions, coordinated and possibly distributed, with conflict resolution.
- **Reflect** [continuous learning] — *new* vs. MAPE-K; learn from outcomes.
- **Enrich** [update & capitalize] — update models/rules, share knowledge across agents, grow a smarter (distributed) knowledge base.

**Paper's comparison (Table 1):**

| Criterion | MAPE-K | LLM-MAPE-K | AWARE |
|---|---|---|---|
| Architecture | Centralized | Centralized | **Distributed** |
| Adaptation | Reactive | Reactive | **Pro/re-active** |
| Continuous learning | Absent | Partial | **Complete** |
| Anticipation | Nonexistent | Moderate | **Complete** |
| Collaboration | Absent | Absent | **Strong** |
| Knowledge | Centralized | Centralized | **Distributed** |

---

## The mapping that makes this gold: AGMS ≈ AWARE for the grid

AGMS is, almost line for line, the AWARE critique of MAPE-K applied to grid operations. Today's grid control
(SCADA + ADMS/DERMS + a human) **is** a centralized, largely reactive MAPE-K loop. AGMS replaces it with the
distributed, proactive, learning, agent-based pattern AWARE describes.

**AWARE stage ↔ AGMS component:**

| AWARE stage | MAPE-K phase | AGMS embodiment |
|---|---|---|
| **Assess** (understand context) | Monitor (+) | GWM Alert Correlation + GA Context Construct Engine / CAPs; **virtual sensing** supplies the physical state |
| **Weigh** (decide among options, simulate) | Analyze + Plan | GA CaCSM build (match → provisional → **simulate-before-commit**) + Decision Support + Simulation Engine |
| **Act** (distributed execution) | Execute | GWCH + scouts on operating cells; coordinated, edge-local actions |
| **Reflect** (continuous learning) | — (new) | Learning Engine Agents watching per-state variance, firing recalibration |
| **Enrich** (update & share knowledge) | K | Learning Engine updating the patterns DB; POV-mediated distributed knowledge |

**MAPE-K limitation → how AGMS fixes it:**

| MAPE-K limitation | AGMS's answer |
|---|---|
| Centralized | Distributed operating cells + scouts; island-mode autonomy |
| Reactive only | Grid-Wide **Foresight** Manager + simulate-before-commit (proactive) |
| Sequential, raw monitoring | Contextual perception (action stress frame → CAPs) before acting |
| No continuous learning | Learning Engine: pattern recognition + per-state calibration |
| Centralized knowledge | POV files / patterns DB — role-mediated, distributable knowledge |

---

## Interview talking points

- "As a class of system, AGMS is a **self-adaptive / autonomic system**. The textbook loop is **MAPE-K**;
  today's centralized grid control is basically a reactive MAPE-K with a human in it."
- "The architecture maps onto the 2025 frontier — **AWARE**: distributed agents, proactive anticipation,
  continuous learning, distributed knowledge. AGMS is essentially AWARE for the grid: scouts are the agents,
  the Foresight Manager is the anticipation, the Learning Engine is Reflect/Enrich, and simulate-before-commit
  is the scenario evaluation in Weigh."
- "My role lives in **Assess** — virtual sensing is the contextual-state perception the whole loop depends on."

## Where it is cited in our notes

- Study note [`grid-operations-and-role.md`](../grid-operations-and-role.html) — Appendix G (AGMS in self-adaptive-systems terms).
- Relates to [`patents/AGMS-architecture.md`](../patents/AGMS-architecture.html) Part 8 (cross-cutting: learning, simulate-before-commit) and Part 10 (design principles).
