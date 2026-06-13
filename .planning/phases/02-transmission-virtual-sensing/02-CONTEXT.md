# Phase 2: Transmission Virtual Sensing - Context

**Gathered:** 2026-06-13
**Status:** Ready for planning

<domain>
## Phase Boundary

Produce equation-aware study notes that give Juan fluent **transmission-side (T&D)
virtual-sensing vocabulary** across four areas, each bridged to an OSED analog, so he can
explain them **aloud and timed** in the interview without defaulting to distribution-side
framing:

- **TVS-01** — Voltage stability monitoring: P-V curve / voltage collapse, Thevenin-equivalent VSI from PMU data, operating-margin concept.
- **TVS-02** — Phase-angle / power-flow inference: DC approximation (P = Bθ), sparse PMU coverage problem, angle inference as a WLS problem.
- **TVS-03** — Observability analysis & bad-data detection: chi-squared test, normalized residuals, leverage measurements as the critical limitation, Jacobian rank as the observability check.
- **TVS-04** — Asset-health estimation: transformer hot-spot (IEEE C57.91 ODE), DGA indicator gases, Dynamic Line Rating as a virtual-sensing product, RUL framing.

**Out of scope (belongs to other phases):** the director's patents (Phase 3), grid
protocol stack / IEC 61850 / NATS-K3s-Prometheus (Phase 4), federated architecture
(Phase 5), and the full vocabulary-bridge table + STAR stories + timed mock rehearsal
(Phase 6). This phase produces *reference notes + one small demo*, not aggregate rehearsal artifacts.
</domain>

<decisions>
## Implementation Decisions

### Hands-on demo (TVS-02 / TVS-03)
- **D-01:** Build **one small Python demo** (~80 lines) — a **3-bus DC power-flow WLS angle estimation + chi-squared bad-data detection** (injects one corrupted measurement, flags it via normalized residual, re-solves). Notes lead; the demo is supporting reinforcement and a concrete "I built this" whiteboard story.
- **D-02:** The demo **reuses Phase 1's WLS / Gauss-Newton machinery** (see `.planning/phases/01-kalman-state-estimation/demo/ekf_line_temp_demo.py` for style/structure). Keep it self-contained with a short README, mirroring Phase 1's `demo/` layout.
- **D-03:** Demo scope stays focused on **TVS-02 (P = Bθ angle WLS)** and **TVS-03 (chi-squared / normalized-residual bad-data detection)** — the two most computable, WLS-reusing topics. TVS-01 (Thevenin VSI) and TVS-04 (asset health) remain notes-only unless trivially cheap to add.

### OSED-analog bridge (core differentiation)
- **D-04:** **Every** one of the four notes ends with a boxed **"→ Bridge to your work"** callout: 1–2 sentences mapping the T&D concept to a concrete **OSED / HEMS / SI-MAPPER** analog, phrased as a ready interview pivot. This satisfies success-criterion 4 everywhere, not just TVS-04.
- **D-05:** Do **not** build an aggregate bridge table here — the full vocabulary-bridge table (BRG-01..03) is owned by **Phase 6**. Per-note callouts feed that later table without duplicating it now.

### Aloud-delivery aids
- **D-06:** Each note carries a tight **"<3-min say-aloud version"** talk-track (a compressed spoken script hitting the criterion's named points) — placed so it directly serves the timed-aloud success criteria at the point of learning.
- **D-07:** Full mock-interview rehearsal, Q&A question bank, and timing drills stay in **Phase 6**. Phase 2 notes provide the script, not the rehearsal loop.

### Depth vs breadth
- **D-08:** **Deep where named, aware elsewhere.** Full derivations + worked numbers ONLY for concepts the success criteria name as must-explain: P-V/Thevenin VSI + operating margin (TVS-01), P = Bθ WLS angle inference (TVS-02), chi-squared + normalized residuals + Jacobian-rank observability (TVS-03), IEEE C57.91 hot-spot ODE (TVS-04). Awareness level (crisp, no derivation) for DGA gases, leverage-measurement intuition, DLR productization, and RUL framing. Mirrors Phase 1's "depth where it differentiates" principle.

### Note granularity (defaulted — carried forward from Phase 1)
- **D-09:** **One file per requirement** in a `notes/` directory: `TVS-01-…md` … `TVS-04-…md`, following Phase 1's `notes/` convention. TVS-04 is the heaviest (hot-spot + DGA + DLR + RUL) — keep it as a single well-sectioned file rather than splitting, unless it grows unwieldy during execution.

### Established note style (carried forward — non-negotiable conventions)
- **D-10:** Equation-dense markdown with **LaTeX-in-markdown** ($…$ inline, $$…$$ display) per the project convention. Each note opens with the Phase-1 "oral rehearsal" framing header (**For:** / **Purpose:**), uses numbered sections, and is written for speak-aloud recall.

### Claude's Discretion
- Exact section ordering within each note, bus topology / numbers chosen for the demo, and whether the "<3-min say-aloud" track sits at the top or bottom of each note. Whether to lightly extend the demo to touch TVS-01 if cheap.
</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

ROADMAP.md declares no explicit "Canonical refs" line for Phase 2; the references below were
accumulated from REQUIREMENTS.md, the project source material in `docs/`, and the Phase 1
artifacts this phase builds on.

### Phase 1 artifacts to reuse (style + WLS machinery)
- `.planning/phases/01-kalman-state-estimation/demo/ekf_line_temp_demo.py` — demo structure/style to mirror; source of reusable WLS/Gauss-Newton code for the Phase 2 demo.
- `.planning/phases/01-kalman-state-estimation/demo/README.md` — demo README pattern.
- `.planning/phases/01-kalman-state-estimation/notes/KAL-01-wls-state-estimation.md` — WLS / Gauss-Newton state-estimation notes that TVS-02/TVS-03 extend to the transmission angle-estimation problem.
- `.planning/phases/01-kalman-state-estimation/notes/KAL-02-kalman-family-kf-ekf-ukf.md` — canonical note-style reference (oral-rehearsal header, LaTeX, numbered sections).
- `.planning/phases/01-kalman-state-estimation/notes/KAL-03-ieee738-ekf-worked-example.md` — worked-example depth bar for "deep where named" topics.

### Domain source material (in `docs/`)
- `docs/job-requirements.md` — the JD; the vocabulary target Juan must speak fluently.
- `docs/Juan Carlos Oviedo Cepeda - 2026.pdf` — Juan's CV; source of the OSED / HEMS / SI-MAPPER analogs used in every bridge callout.
- `docs/intelligrid.pdf` — IntelliGrid architecture reference for T&D framing.
- `docs/IEC 61850-3.pdf` — substation context (awareness; deep treatment is Phase 4).

### Standards referenced by requirements (cite, don't reproduce)
- **IEEE C57.91** — transformer thermal / hot-spot model (TVS-04, deep).
- **IEEE C37.118** — synchrophasor / PMU data standard (TVS-01/02 context; deep treatment is Phase 4).
- **IEEE 738** — conductor thermal model underpinning Dynamic Line Rating (TVS-04; already worked in Phase 1, reference back to it).

### Project reference content already on hand
- `CLAUDE.md` — "Category 3: Grid Protocols" section contains PMU/synchrophasor, IEC 61850, and SCADA vocabulary useful for grounding T&D terminology (deep protocol study is Phase 4).
</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **Phase 1 EKF/WLS demo** (`01-kalman-state-estimation/demo/ekf_line_temp_demo.py`): the WLS/Gauss-Newton solve, plotting, and simulated-telemetry scaffolding can be adapted into the 3-bus DC power-flow angle-WLS + bad-data demo. Same NumPy-only, single-file, README-paired pattern.

### Established Patterns
- **`notes/` + `demo/` per-phase layout** (from Phase 1): one markdown note per requirement in `notes/`, an optional self-contained `demo/` with script + README + output figure. Phase 2 follows the same shape.
- **Oral-rehearsal note header** (**For:** / **Purpose:**), LaTeX-in-markdown math, numbered sections — established and expected.

### Integration Points
- Phase 2 notes feed **Phase 6** (vocabulary-bridge table BRG-01..03, STAR stories, timed Q&A). Per-note "→ Bridge to your work" callouts and "<3-min say-aloud" tracks are the raw material Phase 6 aggregates — keep them in a form Phase 6 can lift directly.
</code_context>

<specifics>
## Specific Ideas

- Demo concretely: a **3-bus DC power-flow** network, estimate bus voltage angles via WLS from (redundant) line-flow / injection measurements, then **corrupt one measurement**, detect it with the **chi-squared test + largest normalized residual**, remove it, and re-solve — demonstrating bad-data detection end to end. This is the canonical textbook illustration of TVS-02 + TVS-03 together.
- Bridge callouts should read as **interview pivots** ("This is exactly the observability problem I faced in OSED when…"), not academic asides.
</specifics>

<deferred>
## Deferred Ideas

- **Aggregate vocabulary-bridge table** (T&D term → OSED analog → pivot sentence) — explicitly **Phase 6** (BRG-01..03). Per-note callouts here feed it.
- **Full Q&A / mock-interview drills and timing rehearsal** — **Phase 6**.
- **Deep PMU / IEC 61850 / C37.118 protocol treatment** — **Phase 4** (Phase 2 uses these only at the vocabulary level needed for voltage-stability and angle-inference framing).
- **Extending the demo to a federated / multi-substation setting** — out of scope; federated architecture is **Phase 5**.

</deferred>

---

*Phase: 2-Transmission Virtual Sensing*
*Context gathered: 2026-06-13*
