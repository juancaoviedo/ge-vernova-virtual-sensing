# Phase 3: Director's Patents Deep-Read — Research

**Researched:** 2026-06-13
**Domain:** Distillation of existing AGMS patent research into a single spoken-rehearsal deck
**Confidence:** HIGH — all source material is already in the repo; no external lookups needed

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

- **D-01:** All six AGMS-family patents get the full summary + connection + question treatment.
  Family: `adaptive-power` (WO 2023/064623, parent), `logistician-module` (US 2024/0337997),
  `asset-portfolio` (WO 2024/211758), `operation-loop` (US 12,596,341 B2 — GRANTED, GE Vernova),
  `scout-command` (US 2024/0339835), `data-management` (WO 2024/211800).
- **D-02:** `ocr.md` is the OCR duplicate of `data-management`, NOT a seventh patent. Six is
  authoritative; the requirement text ("three") and roadmap text ("four") are stale.
- **D-03:** ONE consolidated rehearsal deck (single study doc), NOT per-patent files. This is
  a new artifact — do not augment `INDEX.md` or `AGMS-architecture.md`.
- **D-04:** The deck is performance layer; reference docs (INDEX.md, AGMS-architecture.md)
  remain the reference layer.
- **D-05:** Pipeline order: Parent (adaptive-power) → Logistician → Asset Portfolio →
  Operation Loop Formation → Scout Command → Data Management.
- **D-06:** No separate say-aloud block per patent. The 2–3 sentence summary IS the spoken
  track.
- **D-07:** One ~90-second whole-family "walk the assembly line" pitch at deck level.
- **D-08:** Each patent gets one sharp standalone connection + the deck closes with the unified
  "one assembly line = my stack" master narrative. Source both from INDEX.md — refine, don't
  invent.
- **D-09:** Director-directed questions are architecture-level (design tradeoffs, island-mode,
  federation, simulate-before-commit bounds, operational-index model) — NOT claim-number quotes.

### Claude's Discretion

- Exact deck section layout and any summary table-of-contents.
- Precise wording of each summary, connection, and question.
- How heavily the deck cross-links back to INDEX.md.
- Whether the granted Operation Loop patent gets a visual flag (e.g., ★) to cue emphasis.
- The ~90s family pitch may be lightly adapted from the INDEX's existing "interview master
  narrative."

### Deferred Ideas (OUT OF SCOPE)

- Aggregate vocabulary-bridge table (BRG-01..03) — Phase 6.
- OSED 10-minute pitch in GE Vernova language + STAR stories — Phase 6.
- Timed mock-interview rehearsal / Q&A drill loop — Phase 6.
- Deep protocol/federated treatment triggered by patent content — Phases 4 & 5.
</user_constraints>

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| PAT-01 | Deep-read summary of each of the six patents (REQUIREMENTS.md says "three" — stale; D-01 is authoritative). 2–3 sentence spoken summary per patent. | All six per-patent files are complete (adaptive-power.md, logistician-module.md, asset-portfolio.md, operation-loop.md, scout-command.md, data-management.md). One-line summaries exist in INDEX.md; per-patent files have full "Problem Addressed" and "Core Technical Method" sections. Planner writes 2–3 sentence distillations from these for the deck. |
| PAT-02 | One concrete connection per patent linking it to Juan's OSED/HEMS/SI-MAPPER work. | INDEX.md "How Juan Connects His Work" table + AGMS-architecture.md Part 11 consolidated bridge map + each per-patent file's "Connection to Juan's Work" table. All six connections are drafted and sharp. Planner refines the "sharpest bridge story" from each per-patent file into a spoken one-liner for the deck, plus lifts the master narrative from INDEX.md for the closing section. |
| PAT-03 | One sharp, director-directed question per patent demonstrating understanding and inviting follow-on conversation. | All six per-patent files have a "Question to Ask the Director" already drafted at architecture-level (not claim-quoting). These are interview-ready as written. Planner takes them verbatim or lightly refines for deck voice. |
</phase_requirements>

---

## Summary

**This phase produces one artifact from one operation: distillation, not research.** The deep
reading is fully done. The six per-patent files (adaptive-power.md, logistician-module.md,
asset-portfolio.md, operation-loop.md, scout-command.md, data-management.md), the INDEX.md, and
AGMS-architecture.md together constitute a thorough, cross-referenced knowledge base. The rehearsal
deck is a performance-layer document that lifts, tightens, and voices material that already exists —
not a second reading.

The three PAT requirements (summary, connection, question per patent) are substantively answered
in the existing research. What is missing is the single consolidated document in spoken-delivery
voice that Juan rehearses from. That document does not yet exist — it is the sole deliverable of
this phase.

The source material quality is HIGH. Per-patent questions are already architecture-level and
interview-directed. Per-patent connections are already ranked by sharpness ("sharpest bridge story"
callout in every file). Per-patent summaries can be derived from the "Problem Addressed" and
"Core Technical Method" sections. The master narrative exists verbatim in INDEX.md. The planner's
job is to author the deck by distilling and reordering these sources into one spoken-delivery doc
— a single task, not six.

**Primary recommendation:** One plan, one task: write the deck. The plan should cite each source
section explicitly so the implementer knows exactly where each deck element comes from.

---

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Deck authorship (distill summaries) | Claude (implementer) | — | Source material is in repo; distillation is writing, not research |
| Spoken-delivery voicing | Claude (implementer) | Juan (rehearsal validator) | Deck is written by Claude, validated by Juan rehearsing aloud |
| Connection accuracy | Existing per-patent files (source) | AGMS-architecture.md Part 11 | Per-patent "Connection" tables are authoritative; deck lifts from these |
| Question accuracy | Existing per-patent files (source) | — | "Question to Ask the Director" in each file is ready-to-use |
| Master narrative | INDEX.md (source) | AGMS-architecture.md Part 11 | Both contain the master narrative; INDEX.md version is crisper |
| Phase 6 hand-off | This deck (output) | — | Deck's per-patent connections become BRG-01 raw material |

---

## Source Material Audit: What Exists and Its Completeness

This is the core research finding: a complete inventory of what the planner has to work from.

### Per-Patent Completeness

| Patent (pipeline order) | Summary Draft? | Connection Draft? | Question Draft? | Gap? |
|-------------------------|---------------|-------------------|-----------------|------|
| adaptive-power.md (Parent) | One-liner in INDEX.md; full "Problem Addressed" + "Core Technical Method" + "Key Claims" in file | Full table + "Sharpest bridge story" | Yes — CaCSM simulation fidelity vs. latency | NONE |
| logistician-module.md | One-liner in INDEX.md; full spec + claims in file | Full table + "Sharpest bridge story" | Yes — historical-archive over-fitting vs. novel context | NONE |
| asset-portfolio.md | One-liner in INDEX.md; full spec + claims in file | Full table + "Sharpest bridge story" | Yes — operational index update frequency + marginal-index tradeoff | NONE |
| operation-loop.md (GRANTED ★) | One-liner in INDEX.md; full spec + granted claims in file | Full table + "Sharpest bridge story" (strongest in set) | Yes — degraded/bounded-authority mode vs. hold-for-simulation | NONE |
| scout-command.md | One-liner in INDEX.md; full spec + claims in file | Full table + "Sharpest bridge story" | Yes — warm scout pool vs. incubation on critical path | NONE |
| data-management.md | One-liner in INDEX.md; full spec + claims in file | Full table + "Sharpest bridge story" | Yes — patterns DB evolution + novel-condition detection | NONE |

**Finding:** Zero gaps. Every per-patent element required by PAT-01/02/03 is drafted and ready to
lift. The planner task is pure distillation-and-voicing.

### Deck-Level Elements: What Exists

| Deck Element | Source Location | Status |
|---|---|---|
| ~90s whole-family pitch (D-07) | INDEX.md "The interview master narrative" paragraph + AGMS-architecture.md Part 11 master narrative paragraph | EXISTS — two near-identical versions; deck uses INDEX.md version, lightly tightened for 90s delivery |
| "One assembly line = my stack" master narrative (D-08) | INDEX.md "The interview master narrative" (bottom of How Juan Connects section); AGMS-architecture.md Part 11 (final paragraph) | EXISTS — both sources identical in substance; select one |
| Pipeline order mnemonic (D-05) | INDEX.md formation pipeline diagram + AGMS-architecture.md Part 4 opening | EXISTS — "which / procure → verify → assemble + simulate → deploy" one-liner |
| Glossary / cheat sheet | INDEX.md "Key Technical Terms Cheat Sheet" table | EXISTS — 20+ terms; deck may include a condensed reference |
| Operation Loop ★ flag (D-09 + CONTEXT.md) | INDEX.md file table (★ in row), operation-loop.md opening banner | EXISTS |

---

## Standard Stack (Deck Structure)

This phase has no library stack — the deliverable is a Markdown study document. The relevant
"stack" is the deck's structural template:

### Deck Sections (recommended layout — Claude's discretion)

```
# AGMS Patent Rehearsal Deck

## How to Use This Deck
(one short paragraph: read aloud, do not read silently)

## The Assembly Line at a Glance
(the pipeline mnemonic: Parent → Logistician → Portfolio → Loop Formation ★ → Scout Command → Data Mgmt)
(one-liner owners: which/procure → verify → assemble+simulate → deploy → data-plane)

## The ~90-Second Pitch
(the whole-family "walk the assembly line" spoken narrative, adapted from INDEX.md)

---

## Patent 1: Adaptive Power Grid Management System (Parent)
**WO 2023/064623 A1 | Sharif-Askary | General Electric Company**

### Summary (say this aloud)
[2–3 sentences distilled from adaptive-power.md "Problem Addressed" + one-liner]

### My Connection: OSED / HEMS / SI-MAPPER
[one sharp standalone connection, from per-patent "sharpest bridge story"]

### Question for the Director
[from adaptive-power.md "Question to Ask the Director" — verbatim or lightly refined]

---

## Patent 2: Logistician Module
...

## Patent 3: Asset Portfolio Manager
...

## Patent 4: Operation Loop Formation ★ (GRANTED — GE Vernova's own IP)
...

## Patent 5: Scout Command
...

## Patent 6: Data Management
...

---

## Closing: The Master Narrative
("I've been building the components of this exact assembly line, in a different domain...")

## Quick-Reference Cheat Sheet
(condensed glossary: 8–10 essential terms)
```

### Format Conventions (from Phase 2 established style, adapted)

- **Voice:** Second-person is wrong here; deck speaks in first-person for Juan. "I built...",
  "My OSED platform...", "My CVXPY MPC..."
- **No LaTeX:** This is a prose/architecture deck; the project's LaTeX-in-markdown convention
  applies to equation-dense notes only (CLAUDE.md confirms, Phase 2 notes confirm).
- **Say-aloud framing:** Phase 2 used a `## <3-min say-aloud version` block at the top of each
  note. Here D-06 eliminates per-patent aloud blocks — the 2–3 sentence summary IS the spoken
  track. The `## How to Use This Deck` note covers this instruction once.
- **Single doc:** Departs from Phase 2's per-requirement files. One `.md` file, no sub-files.
- **★ flag for Operation Loop:** Use ★ in the section heading to cue Juan to emphasize it.
- **Cross-links:** Minimal — deck is performance layer; one parenthetical "(full reference:
  operation-loop.md)" per section is sufficient for depth look-up.

---

## Architecture Patterns

### The Formation Pipeline (the deck's spine)

The entire deck is organized around this pipeline, which the planner must preserve:

```
Alert → GWM (Parent) fires context
  → LOGISTICIAN: formation plan → provisional logistics list
  → ASSET PORTFOLIO MANAGER: verify 7 operational indexes → verified logistics list
  → OPERATION LOOP FORMATION ★: match DNA/schema → build meta objects → simulate → ✓
  → SCOUT COMMAND: incubate + role-assign + launch plan → scouts live on FADs
  → CSM OPERATOR: run the ORACS as state-machine execution loop
  (DATA MANAGEMENT: serves POV views to every module throughout — cross-cutting layer)
```

**One-liner owners (memorize for the pitch):**
- Logistician = *which / procure*
- Portfolio Manager = *verify*
- Operation Loop Formation = *assemble + simulate*
- Scout Command = *deploy*
- Data Management = *what each module sees*

### Per-Patent Summary Sources (Planner Reference)

The 2–3 sentence summary for each patent should be derived from these source passages:

| Patent | Source for Summary |
|--------|-------------------|
| adaptive-power | INDEX.md one-liner + AGMS-architecture.md Part 1 "core insight" paragraph; focus on: alert correlation → CaCSM → formation pipeline → autonomous scouts + island-mode |
| logistician-module | INDEX.md one-liner + logistician-module.md "Problem Addressed"; focus on: formation plan → template → class/asset selection → provisional logistics list + gap ownership |
| asset-portfolio | INDEX.md one-liner + asset-portfolio.md "Problem Addressed" + ORACS index definition; focus on: 7 operational indexes → verified logistics list → replacement loop |
| operation-loop | INDEX.md one-liner + operation-loop.md "Problem Addressed" + granted-claim summary; focus on: DNA/schema retrieval → per-asset meta objects → simulate-before-commit (claim 3) → GE Vernova's own IP |
| scout-command | INDEX.md one-liner + scout-command.md "Problem Addressed"; focus on: Liaison→Processor→Incubator→Launch Manager; role-typed scouts; clone/self-form; launch plan = time/load/origin/dest/asset-id |
| data-management | INDEX.md one-liner + data-management.md "Problem Addressed"; focus on: POV files = role-filtered data views on demand; patterns database; sole interface to asset DB; ga-authenticationkey gating |

### Per-Patent Connection Sources (Planner Reference)

| Patent | Primary Connection Source | Spoken One-Liner (from source) |
|--------|--------------------------|-------------------------------|
| adaptive-power | adaptive-power.md "Sharpest bridge story" | OSED edge nodes = the runtime scouts land on (K8s, FastAPI, MQTT, CVXPY, K3s) |
| logistician-module | logistician-module.md "Sharpest bridge story" | OSED FastAPI orchestrator = Logistician: abstract job → placed, audited K3s workloads; CVXPY = audit-before-dispatch |
| asset-portfolio | asset-portfolio.md "Sharpest bridge story" | SI-MAPPER = the DNA map: typed, relationship-aware asset fingerprint + knowledge graph |
| operation-loop | operation-loop.md "Sharpest bridge story" | CVXPY MPC solve-before-commit = claim 3 simulate-before-commit (most literal, strongest analogy in family) |
| scout-command | scout-command.md "Sharpest bridge story" | K3s scheduler = Scout Incubator: declarative desired state, role-typed pods, reconcile replicas; SI-MAPPER = DNA map |
| data-management | data-management.md "Sharpest bridge story" | FastAPI service layer = data management module: mediated access, role-scoped views, gRPC/MCP auth = ga-authenticationkey |

### Master Narrative Source

INDEX.md bottom section: "The interview master narrative" (final paragraph of "How Juan Connects His Work"). Also in AGMS-architecture.md Part 11 final paragraph. Both are substantively identical; use INDEX.md version. The deck's closing section refines it for spoken first-person delivery and ensures it lands as a 60–90 second spoken answer.

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Per-patent summaries | New original research / re-reading PDFs | Per-patent files "Problem Addressed" + INDEX.md one-liners | Research is done; re-reading is wasted time |
| Per-patent connections | New connection analysis | Per-patent "Connection to Juan's Work" tables + INDEX.md connection table | Existing connections are accurate and sharp |
| Per-patent questions | New question generation | Per-patent "Question to Ask the Director" sections | Already architecture-level; already interview-ready |
| The master narrative | New synthesis | INDEX.md "interview master narrative" paragraph | Already written; refine voice only |
| The pipeline mnemonic | Inventing new framing | INDEX.md formation pipeline diagram + AGMS-architecture.md Part 4 opening paragraph | The "assembly line" framing is the canonical mental model |

**Key insight:** Every substantive element of the deck already exists in the research layer. The implementation task is editorial: select, distill, voice, and organize. Any implementer who re-reads the source PDFs or rewrites connections from scratch is doing unnecessary work.

---

## Common Pitfalls

### Pitfall 1: Making the Summary Too Long
**What goes wrong:** Implementer includes sub-module detail (reference numbers, claim numbers,
acronym expansions) in the 2–3 sentence summary, making it undeliverable aloud in the interview.
**Why it happens:** The per-patent files are detailed; it's tempting to preserve fidelity.
**How to avoid:** The summary must pass the "can Juan say this in 20 seconds without notes?"
test. Two or three sentences maximum. Sentence 1: what the patent solves. Sentence 2: how (the
key mechanism). Sentence 3 (optional): the payoff / distinctive claim.
**Warning signs:** If the summary contains a reference number (e.g., "1023A") or a WO/US
application number, it's too detailed for the spoken track.

### Pitfall 2: Repeating the Same Connection Across Patents
**What goes wrong:** Multiple patents get "CVXPY MPC" as the connection, without differentiation.
**Why it happens:** MPC is Juan's strongest technical analog and it appears in every patent's
connection table to some degree.
**How to avoid:** Each patent's standalone connection must be distinct. Per-patent primary
connections are: Parent = OSED runtime (broadest); Logistician = orchestration/FastAPI;
Portfolio = SI-MAPPER DNA map; Operation Loop = CVXPY (most literal, anchor it here); Scout
Command = K3s scheduler; Data Management = FastAPI service layer + auth pattern. MPC surfaces
as the primary connection only for Operation Loop Formation.
**Warning signs:** If CVXPY appears in more than two patent connection sections, revise.

### Pitfall 3: Making Questions Sound Like Exam Queries
**What goes wrong:** A question that begins "Can you explain what claim 3 says about..." or
"What is the formal definition of ORACS?"
**Why it happens:** The research files list claim details; it's natural to reference them.
**How to avoid:** D-09 is explicit: questions must be architecture-level — about design choices
and tradeoffs. Check: does the question invite the director to share a design decision and its
rationale? If it could be answered by reading the patent, it's too literal. The existing
per-patent questions all pass this test; use them as written.
**Warning signs:** Any question that quotes a specific claim number in the question itself.

### Pitfall 4: Letting the Deck Drift Into Reference Mode
**What goes wrong:** Deck sections accumulate background, glossary entries, and architectural
detail until they read like a second INDEX.md rather than a rehearsal performance script.
**Why it happens:** AGMS is architecturally rich; there is always more to say.
**How to avoid:** D-03 and D-04 are the guard rails: the deck is the performance layer, not
the reference layer. Anything that belongs in INDEX.md or AGMS-architecture.md stays there;
the deck links to those docs for depth. Per-patent sections should be completable in 90 seconds
of reading.
**Warning signs:** If a per-patent deck section exceeds ~250 words, audit for reference content.

### Pitfall 5: Burying the Granted Operation Loop Patent
**What goes wrong:** All six patents are formatted identically; the granted patent does not
stand out.
**Why it happens:** Uniformity of deck structure.
**How to avoid:** D-09 + CONTEXT.md `<specifics>` section: Operation Loop Formation gets a ★
in the heading, a brief "(GRANTED — GE Vernova's own IP)" label, and the connection should
explicitly name "claim 3" because knowing it is in the granted claims (not a published
application) IS the talking point. The deck should cue Juan to pause and let this land.
**Warning signs:** If the Operation Loop section looks visually identical to the others with no
distinguishing marker.

---

## Code Examples

No code applies. This is a prose/Markdown deliverable. The "patterns" are structural:

### Example: Per-Patent Deck Section Template

```markdown
## Patent N: [Title]
**[Publication number] | Sharif-Askary | [Assignee]**
*(reference: `.planning/research/patents/[filename].md`)*

### Summary
[2–3 sentences. Sentence 1: what problem. Sentence 2: the mechanism. Sentence 3: the payoff.]

### My Connection
[One standalone sentence or short paragraph. First-person. Specific project (OSED / HEMS /
SI-MAPPER). No jargon that requires explaining. Ends with a concrete claim ("I shipped this").]

### Question for the Director
> "[Architecture-level question. Design tradeoff. Invites director to share a decision and
> its rationale. Does not quote a specific claim number.]"
```

### Example: Master Narrative Template (closing section)

```markdown
## Closing: The Master Narrative

> "The patent family describes one self-organizing platform — an assembly line:
> the Logistician decides *which* assets and procures them, the Portfolio Manager
> *verifies* them, Operation Loop Formation *assembles and simulates* the ORACS loop,
> and Scout Command *deploys* the scouts. I've built the components of exactly this,
> independently, in buildings and DER:
> - OSED is the edge runtime and orchestration control plane the scouts would land on;
> - my K3s scheduler IS the Scout Incubator — declarative desired state, role-typed pods,
>   reconcile replicas;
> - SI-MAPPER is the typed DNA-map asset model (ASHRAE 223P ontology, CV-to-graph);
> - CVXPY MPC is the simulate-before-commit gate that the *granted* Operation Loop patent —
>   GE Vernova's own IP — puts in its allowed claims;
> - and my Databricks analytics stack is the GWM data foundation.
> Coming to GE Vernova means integrating those into a T&D-scale version of precisely this
> architecture."
```
(Source: INDEX.md "interview master narrative," lightly revised for spoken first-person delivery.)

---

## Open Questions

1. **Deck length vs. rehearsal depth**
   - What we know: six patents × ~3 elements each = 18 deck items; plus pitch + master narrative
   - What's unclear: whether a single consolidated Markdown file will feel navigable or overwhelming
   - Recommendation: include a "How to Use This Deck" header that instructs Juan to read each
     section aloud and move on — keeps pace. A TOC at the top helps navigation during rehearsal.

2. **Question verbatim vs. lightly refined**
   - What we know: all six per-patent questions are written; they are already architecture-level
   - What's unclear: whether any should be shortened for interview pacing (some are two-part)
   - Recommendation: keep them as-is for the deck; the natural interview moment is to ask one
     part and let the conversation unfold. Do not shorten them.

3. **Connection condensation**
   - What we know: each per-patent file has a multi-paragraph "sharpest bridge story"
   - What's unclear: the deck needs a spoken one-liner, not a multi-sentence paragraph
   - Recommendation: distill to one sentence ("The Operation Loop's claim 3 simulate-before-commit
     is the exact discipline I shipped as CVXPY MPC in OSED") — that IS the deck; the file has
     the depth backing it up.

---

## Environment Availability

Step 2.6: SKIPPED — this phase is a prose document authoring task with no external dependencies.

---

## Validation Architecture

Step 4: SKIPPED — `workflow.nyquist_validation` is `false` in `.planning/config.json`.

---

## State of the Art

| Aspect | Status at Phase Start | Action |
|--------|-----------------------|--------|
| Per-patent summaries | Exist as INDEX.md one-liners + per-file "Problem Addressed" | Distill to 2–3 sentence spoken version in deck |
| Per-patent connections | Exist as per-file tables + sharpest bridge stories | Condense to one spoken statement per patent |
| Per-patent questions | Exist in all six files; architecture-level, interview-ready | Lift verbatim or lightly tighten |
| Master narrative | Exists in INDEX.md + AGMS-architecture.md Part 11 | Refine voice only; use first-person |
| ~90s pitch | INDEX.md "interview master narrative" paragraph | Adapt to explicit "90 seconds / 6 steps" deck framing |
| Deck document itself | Does NOT exist | This phase creates it |

---

## Assumptions Log

All claims in this research are verified against files already in the repository. No external
sources were consulted. No assumed knowledge was applied.

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| — | — | — | — |

**If this table is empty:** All claims in this research were verified against existing repo
files — no user confirmation needed.

---

## Sources

### Primary (HIGH confidence — verified against files in this session)

- `.planning/research/patents/INDEX.md` — six-patent family map, formation pipeline, per-patent one-liners, connection table, interview master narrative, glossary cheat sheet
- `.planning/research/patents/AGMS-architecture.md` — end-to-end architecture walkthrough (47KB); Parts 1–11 read in full; Part 11 confirmed as the consolidated bridge map
- `.planning/research/patents/adaptive-power.md` — "Problem Addressed", "Core Technical Method", "Key Claims", "Connection to Juan's Work", "Question to Ask the Director" — all read and confirmed complete
- `.planning/research/patents/logistician-module.md` — same sections — read and confirmed complete
- `.planning/research/patents/asset-portfolio.md` — same sections — read and confirmed complete
- `.planning/research/patents/operation-loop.md` — same sections + granted-claim confirmation — read and confirmed complete
- `.planning/research/patents/scout-command.md` — same sections — read and confirmed complete
- `.planning/research/patents/data-management.md` — same sections — read and confirmed complete
- `.planning/phases/03-director-s-patents-deep-read/03-CONTEXT.md` — locked decisions D-01 through D-09, canonical refs, specifics
- `.planning/REQUIREMENTS.md` — PAT-01/02/03 as written (noted as stale re: count; D-02 supersedes)
- `.planning/STATE.md` — project history, quick-task completion record
- `.planning/config.json` — `nyquist_validation: false`, `commit_docs: true`
- `.planning/phases/02-distribution-virtual-sensing/notes/TVS-01-voltage-stability.md` — Phase 2 style reference (For:/Purpose: header, <3-min say-aloud block)

---

## Metadata

**Confidence breakdown:**
- Source material completeness: HIGH — all six patents researched, every PAT-01/02/03 element drafted
- Deck structure recommendation: HIGH — derived from D-03 through D-09 + Phase 2 style
- Question quality: HIGH — verified as architecture-level in all six files
- Connection sharpness: HIGH — each file has an explicit "sharpest bridge story" callout
- Implementation risk: LOW — task is editorial, not research; no new knowledge required

**Research date:** 2026-06-13
**Valid until:** Indefinite — source material is in-repo; no external dependency
