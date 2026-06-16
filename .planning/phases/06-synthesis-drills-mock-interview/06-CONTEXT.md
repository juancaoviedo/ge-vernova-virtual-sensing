# Phase 6: Synthesis, Drills & Mock Interview - Context

**Gathered:** 2026-06-16
**Status:** Ready for planning

<domain>
## Phase Boundary

Convert all accumulated Phase 1–5 study material into **deliverable, spoken, time-boxed
interview answers** — the synthesis capstone. **No new technical material**: this phase
*packages* existing knowledge for verbal delivery under pressure. Six requirements:
vocabulary-bridge table (**BRG-01**), 10-min OSED pitch in GE Vernova language (**BRG-02**),
STAR stories mapped to JD lines (**BRG-03**), 12 tough-question answer keys (**QNA-01**),
≥2 system-design drills (**QNA-02**), consolidated mock-interview bank (**QNA-03**).

**The reframe that governs everything (D-01):** the **first interview is a non-technical
HR phone screen** (round 1 of ~4 GE Vernova rounds) that verifies the CV and role fit.
Juan must pass it to reach the technical rounds. So Phase 6 is **phone-screen-first**:
plain-language self-presentation + fit + logistics is the primary, front-and-center
target; the deep technical material (12 domain Qs, system-design drills) is **built but
staged behind**, tagged for technical rounds 2–4.

**In scope:** synthesizing the existing notes into a phone-screen pack + tiered narrative
(bridges, pitch, STAR), a JD-bullet-driven question bank, two system-design drills, and a
rehearsal protocol + tracker.

**Out of scope:** any *new* Kalman / DSSE / protocol / federated / patent content (Phases
1–5 own that — cross-reference, don't re-derive); re-converting notes into the HTML site
(Phase 7 owns that); live mock-interview role-play (a usage activity, not a written
deliverable — see Deferred).

</domain>

<decisions>
## Implementation Decisions

### Interview-round strategy (the governing reframe)
- **D-01:** **Phone-screen-first layering.** GE Vernova runs ~4 rounds; round 1 is a
  **non-technical HR phone screen** verifying CV + fit in plain language. Deliverables are
  layered so the **HR-screen material is primary and front-loaded**; the deep technical
  material (QNA-01 12 domain Qs, QNA-02 drills) is **fully built but tagged for rounds
  2–4**. Rationale: you can't show technical skill until you pass the screen, and the
  screener is non-technical — so the immediate, highest-yield work is *how to present
  yourself in comprehensible, outcome-first language*. (Chosen over "two equal-weight
  packs" and "one integrated set + plain layer".)

### Deliverable structure
- **D-02:** **Hybrid doc set in `notes/` + a tracker** (matches the prior-phase `notes/`
  convention; note count > requirement count is fine, per Phase 5 D-01). Proposed grouping
  (exact filenames = Claude's discretion):
  - **`PHONE-SCREEN.md`** — the front doc (round 1): plain-language "tell me about
    yourself", fit narrative (why GE Vernova / why leave Hydro-Québec / why this role),
    **logistics answers** (TN / relocation / comp — D-03/04/05), plain-language behavioral,
    and the standard HR-screen question set (D-12).
  - **`REFRAME.md`** — vocabulary-bridge table (BRG-01, two-layered per D-06) + the tiered
    OSED pitch (BRG-02, per D-07).
  - **`STAR-STORIES.md`** — 4 STAR stories (BRG-03 + the SI-MAPPER 4th, D-08), each with a
    plain-language version (screen) and a 2-min technical version (later rounds), mapped to
    JD lines.
  - **`QUESTION-BANK.md`** — JD-bullet question generator (D-09) + the 12 tough domain Qs
    (QNA-01, D-10) + the consolidated bank organized by round/category (QNA-03, D-11).
  - **`SYSTEM-DESIGN-DRILLS.md`** — the 2 drills (QNA-02, D-13).
  - **`REHEARSAL-TRACKER.md`** — flashcard tracker + written "how to rehearse" protocol
    (D-14), mirroring the Phase 4 `04-HUMAN-UAT.md` precedent.

### Phone-screen content & logistics (the un-guessable Juan-specific facts)
- **D-03:** **Work authorization = TN visa (Juan is a Canadian citizen).** Lead with it as a
  **positive selling point**, not a caveat: *"As a Canadian citizen I'm TN-eligible for this
  Engineer/Scientist role — fast, no H-1B lottery, low cost and friction for GE Vernova."*
  (The TN profession categories cover Engineer / Scientist / Computer Systems Analyst; the
  PhD + role title make this a clean fit.)
- **D-04:** **Relocation = eager, already researched.** Juan wants to relocate to **Melbourne,
  FL as fast as possible** and has already chosen where he'd live. Script it as enthusiastic
  and zero-friction — this turns the biggest screen-out risk (on-site hybrid, no relo
  assistance) into a strength.
- **D-05:** **Comp = fit-first, soft upper-half anchor, defer the number.** Acknowledge the
  posted **$98.4k–$164k** range is reasonable, gently note it's a **senior** post, then pivot:
  *"What matters most is proving I'm the right long-term fit — once we both see that, I'm
  confident we can align on numbers."* Do **not** commit a hard figure on the screen.

### Reframe & narrative bridges (BRG)
- **D-06:** **Vocabulary bridges (BRG-01) are two-layered.**
  - **Layer A — plain-language "HR translation"** (jargon → outcome/impact): the PRIMARY
    layer for the screen (e.g. "MQTT + K8s edge orchestration" → *"I make thousands of field
    devices coordinate in real time"*; "convex optimization / MPC" → *"software that makes the
    smartest control decision every few seconds"*).
  - **Layer B — technical T&D analog + tool bridges**: OSED/HEMS/SI-MAPPER concept → GE
    Vernova virtual-sensing/T&D analog, plus tool bridges (MQTT→NATS, K8s→K3s,
    InfluxDB→Prometheus, Pub/Sub→Kafka). For technical rounds.
  - Success bar: each bridge sentence deliverable within **~10 s** of being prompted.
- **D-07:** **OSED pitch (BRG-02) is tiered.** A **~60–90 s plain-language "tell me about
  yourself"** + a **~2–3 min plain-language OSED summary** for the screen; the **full ~10-min
  outcome-first technical pitch** staged for later rounds. All versions **open with a deployed
  outcome** (e.g. *"a cloud-edge platform now running grid services on real edge nodes — it cut
  isolated-community energy cost by 21%"*). **Honest framing** (no false production-FL claim —
  carried from Phase 5 D-07). On the screen, **avoid PhD / distribution-side jargon**; lead
  with impact.

### STAR stories (BRG-03)
- **D-08:** **FOUR STAR stories** (keep the 3 named + add the differentiator as a 4th):
  1. **OSED build** (architect of the cloud-edge grid-services platform),
  2. **HEMS PoC** (whole-home load management respecting grid limits),
  3. **Big-data substation analysis** (Databricks/PySpark, billions of points across
     substations),
  4. **SI-MAPPER / agentic-AI / MCP → AGMS "scouts"** — the **#1 differentiator** (Operation
     Loop Formation US 12,596,341 B2 is **GRANTED and assigned to GE Vernova**).
  Each story: a **plain-language version** (screen) + a **≤2-min technical STAR** (later
  rounds), explicitly **mapped to specific JD lines** (e.g. story 4 → "Integrate AI/ML
  capabilities, federated control frameworks, and digital twins").

### Q&A, JD-bullet questions & drills (QNA)
- **D-09:** **JD-bullet question generator** (Juan's explicit directive). For each JD
  *responsibility* bullet (and each key required-skill), produce **both** a behavioral
  *"Tell me about a time when you…"* (anchored to concrete CV evidence) **and** a situational
  *"How would you…"*. Plain-language **behavioral** surfaces on the screen; *"how would you
  [technical design]"* is staged for technical rounds. Every question gets a **CV-anchored
  answer key**.
- **D-10:** **The 12 tough domain questions (QNA-01) are differentiator-weighted** —
  Kalman/state-estimation, DSSE virtual sensing, federated, the patents — with **tight bullet
  answer keys** (fast aloud recall), **mined from the prior-phase "<3-min say-aloud" tracks**.
  **Tagged for technical rounds 2–4**, not the screen.
- **D-11:** **Consolidated bank (QNA-03)** = the union of all questions, organized **by
  interview round** (HR-screen → technical → behavioral) and **by category**, serving as the
  final-day rehearsal index.
- **D-12:** **HR-screen question set** (beyond JD bullets): "tell me about yourself", "why this
  role / why GE Vernova", "why leave Hydro-Québec", strengths/weaknesses, salary expectations,
  availability/notice, work-auth & relocation. Plain-language answer keys; lives in
  `PHONE-SCREEN.md`.
- **D-13:** **Two system-design drills (QNA-02)**, both technical-round material, in an
  **ASCII-whiteboard + narration** format mirroring **STK-05**:
  1. **500-node virtual-sensing pipeline** — force in **K3s, NATS, EKF engine, federated
     aggregator, GitOps fleet management** (fixed by the success criterion).
  2. **Close-the-loop: simulation / digital-twin → field validation** — digital twins,
     EMT/Opal-RT awareness, validate virtual-sensor output against physical models, then close
     the loop to live edge control. (Chosen to cover the JD "Simulation & Integration" section
     that drill 1 doesn't.)

### Rehearsal mechanism
- **D-14:** **Flashcards + tracker + written protocol** (Juan explicitly asked to be *guided
  how to rehearse*). Each question = a **prompt with a collapsed bullet answer-key**
  (self-test, then check). A **`REHEARSAL-TRACKER.md`** table (date · said-aloud ✓ · time-to-
  deliver · confidence ⚠/✓ · notes). A one-page **rehearsal protocol**: out loud, **record &
  time** yourself, **space** it across the days before the screen, hit **target durations**,
  and **flag the 2–3 weakest** to redo (satisfies success-criterion 5's "identify 2–3 that
  need more rehearsal"). Target times: bridges **≤10 s**, STAR **≤2 min**, phone-screen pitch
  **≤90 s**, full OSED pitch **~10 min**.

### Conventions carried forward (non-negotiable, not re-discussed)
- **D-15:** **Oral-rehearsal note style** (For:/Purpose: header, numbered sections, tight
  say-aloud tracks) + **honest bridge framing** (Phase 5 D-07/D-08/D-09). **Markdown +
  selective LaTeX** only where a formula genuinely helps — and **only in technical-round
  material**; the screen material stays jargon-light (Phase 5 D-10).
- **D-16:** **No new technical material.** Phase 6 synthesizes Phase 1–5 notes only —
  **cross-reference, don't re-derive** (ROADMAP: "Phase 6 is synthesis/drill-only").

### Claude's Discretion
Exact filenames/slugs within `notes/`; precise section ordering within each doc; the exact
wording of the pitch opening hook; which specific JD bullets get both question styles vs.
one; the exact membership of the 12 differentiator-weighted questions; the precise
plain-language analogies in the Layer-A "HR translation" bridges; how richly STAR story 4
cross-links to the Phase 3 patent deck; the target-time numbers in the tracker (sensible
defaults given).

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

ROADMAP.md declares no explicit "Canonical refs" line for Phase 6. The list below was
accumulated from REQUIREMENTS.md, the `docs/` source material, the Phase 1–5 artifacts this
phase synthesizes, and the two docs Juan explicitly directed me to use (the JD + CV).

### The two primary inputs (Juan-directed — read FIRST)
- `docs/job-requirements.md` — **THE job description.** Source of every bullet for the
  JD-bullet question generator (D-09), the role vocabulary the bridges/pitch must adopt, the
  logistics facts (West Melbourne FL, hybrid, no relo assistance, US work auth, $98.4k–$164k),
  and the JD lines STAR stories map to (D-08). The vocabulary + fit target.
- `docs/Juan Carlos Oviedo Cepeda - 2026.pdf` — **Juan's CV** (also `… 2026.docx`). Source of
  all STAR evidence (OSED, HEMS, big-data/Databricks, SI-MAPPER/MCP/IoT-as-context), the
  "your work" side of every bridge, and the −21% / billions-of-points / Linux Foundation
  Energy / TN-Canadian-citizen facts.

### Content base & gap framing
- `CLAUDE.md` — the **Summary Reference Table** (tool one-liners → Layer-B tool bridges), the
  **gap analysis** (priority order → the 12-Q differentiator weighting, D-10), and **"What NOT
  to Over-Invest In"** (depth ceiling for the staged technical material).
- `.planning/REQUIREMENTS.md` — BRG-01..03 / QNA-01..03 definitions and "Complete when
  deliverable aloud under pressure" framing.
- `.planning/ROADMAP.md` (Phase 6 section) — goal + the 5 success criteria the deliverables
  must satisfy.

### Phase 1–5 notes — the RAW MATERIAL to synthesize (lift, don't re-author)
- `.planning/phases/01-kalman-state-estimation/notes/` — KAL-01..04 (virtual-sensing fusion
  engine, KF/EKF/UKF, FASE augmented-load feeder walk, IEEE 738 asset-health).
- `.planning/phases/02-distribution-virtual-sensing/notes/` — DSSE-01..04 (under-observability,
  side-information taxonomy, distribution modeling + pseudo-measurement honesty, virtual
  sensing in AGMS + federated DSSE).
- `.planning/phases/03-director-s-patents-deep-read/notes/AGMS-patent-rehearsal-deck.md` —
  per-patent summary + connection + question + the **"one assembly line = my stack"** master
  narrative. **Primary source for STAR story 4 and the patent-connection bridges.**
- `.planning/phases/04-protocols-stack-architecture/notes/` — STK-01..05 (protocol stack, IEC
  61850, messaging/orchestration, observability, four-tier reference architecture → drill 1).
- `.planning/phases/05-federated-architectures-security/notes/` — FED-01..03 (federated vs
  distributed, Byzantine robustness, edge security).
- Every Phase 1–5 note already carries per-note **"→ Bridge to your work"** callouts and
  **"<3-min say-aloud"** tracks — direct raw material for BRG-01, the QNA-01 answer keys, and
  STAR pivots.

### Format precedents
- `.planning/phases/04-protocols-stack-architecture/04-HUMAN-UAT.md` — the **rehearsal-tracker
  precedent** to mirror for D-14.
- `.planning/phases/05-federated-architectures-security/05-CONTEXT.md` — the note-style /
  honest-framing conventions carried forward (D-15).
- `.planning/research/patents/INDEX.md` — AGMS component map; supports STAR story 4 and the
  patent connections (Operation Loop = GRANTED to GE Vernova).

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **All Phase 1–5 `notes/`** already contain "→ Bridge to your work" callouts and "<3-min
  say-aloud" tracks — these ARE the bridges, the QNA-01 answer keys, and the STAR pivots in
  draft form. Phase 6 lifts and tightens; it does not author technical content from scratch.
- **AGMS patent rehearsal deck (Phase 3)** — per-patent connection + question + master
  narrative; directly seeds STAR story 4 and the differentiator framing.
- **`04-HUMAN-UAT.md` (Phase 4)** — the oral/whiteboard rehearsal-tracker pattern to mirror
  for `REHEARSAL-TRACKER.md` (D-14).
- **STK-05 reference-architecture doc** — the ASCII + narration whiteboard format to mirror
  for both system-design drills (D-13).

### Established Patterns
- **`notes/` topic-file split** (Phases 1–5) — followed; note count > requirement count is
  fine (Phase 5 D-01 precedent) because the phone-screen reframe adds a front doc.
- **Oral-rehearsal note style + honest framing + selective LaTeX** (Phase 5 D-08/09/10) —
  carried (D-15); LaTeX confined to technical-round material.

### Integration Points
- Phase 6 is the **spoken layer** over the Phase 1–5 written notes and the Phase 7 HTML site —
  it does not re-convert notes (Phase 7 owns the site). Cross-link back to the source notes so
  the deeper "why" is one hop away during rehearsal.
- The JD-bullet generator (D-09) and STAR mapping (D-08) bind directly to `docs/job-
  requirements.md` lines and `…CV…pdf` evidence — keep those mappings explicit so a reviewer
  can trace each answer to a JD line + a CV bullet.

</code_context>

<specifics>
## Specific Ideas

- **TN one-liner (D-03):** *"As a Canadian citizen I'm TN-visa eligible for this
  Engineer/Scientist role — that's fast, no H-1B lottery, and low cost and friction for the
  team."*
- **Relocation line (D-04):** *"I want to relocate to Melbourne as fast as possible — I've
  already looked at exactly where I'd live. The hybrid/on-site setup is a plus for me, not a
  hurdle."*
- **Comp line (D-05):** *"The posted range looks reasonable for a senior role; what matters
  most to me right now is proving I'm the right long-term fit — once we both see that, I'm
  confident we'll align on the number."*
- **Screen tone:** the listener is **non-technical HR**. Plain language, concrete analogies,
  **outcomes and impact over architecture**. No PhD/distribution jargon; no equations.
- **Pitch opening:** lead with the **deployed outcome** ("a platform now running on real edge
  nodes that cut isolated-community energy cost 21%"), then *what it does* in plain terms, then
  *why it maps to GE Vernova's decentralized-grid mission* — only then any technical depth.
- **Differentiator to surface early:** agentic AI / MCP / SI-MAPPER → the director's AGMS
  "scouts" (Operation Loop Formation is **granted to GE Vernova**). This is the single
  strongest "I already think like your lab" hook.
- **JD-bullet question styles (D-09):** *"Tell me about a time when you [JD bullet]"* +
  *"How would you [JD bullet]"* — generated systematically from the JD bullets, each tied to
  CV evidence.

</specifics>

<deferred>
## Deferred Ideas

- **Deep technical-round (2–4) live drills** — beyond the staged QNA-01/QNA-02 material:
  live whiteboard coding, deeper EMT/digital-twin walk-throughs, a real-framework (Flower) FL
  demo. The staged material covers the substance; deeper live drills are a follow-on if time
  remains after the screen is secured.
- **A live mock-interview role-play** (Claude acting as interviewer over the bank) — a
  *usage* activity that the `REHEARSAL-TRACKER.md` protocol enables, not a written deliverable
  of this phase. Can be run as a rehearsal aid once the bank exists.
- **Folding the phone-screen / STAR / bank material into the Phase 7 HTML study site** —
  future enhancement; Phase 7's build is complete and this phase keeps the spoken material in
  `notes/` markdown for fast editing during the runway.

None beyond the above — discussion stayed within phase scope (the phone-screen reframe is a
re-prioritization of in-scope deliverables, not new scope).

</deferred>

---

*Phase: 6-Synthesis, Drills & Mock Interview*
*Context gathered: 2026-06-16*
