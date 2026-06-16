# Phase 6: Synthesis, Drills & Mock Interview — Research

**Researched:** 2026-06-16
**Domain:** Interview preparation synthesis — HR phone-screen technique, STAR method, TN visa
logistics, rehearsal mechanics, document structure
**Confidence:** HIGH (for technique and structure); MEDIUM (for TN visa details given June 2025
policy change; see Assumptions Log)

---

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

- **D-01:** Phone-screen-first layering. Round 1 is a non-technical HR phone screen. HR-screen
  material is primary and front-loaded; QNA-01/QNA-02 technical material is built but tagged
  for rounds 2–4.
- **D-02:** Hybrid doc set in `notes/` + a tracker. Six named files: `PHONE-SCREEN.md`,
  `REFRAME.md`, `STAR-STORIES.md`, `QUESTION-BANK.md`, `SYSTEM-DESIGN-DRILLS.md`,
  `REHEARSAL-TRACKER.md`.
- **D-03:** Work authorization = TN visa. Lead as a positive selling point: fast, no H-1B
  lottery, low cost and friction. TN-eligible: Engineer / Scientist / Computer Systems Analyst.
- **D-04:** Relocation = eager, already researched. Script as zero-friction, enthusiastic.
- **D-05:** Comp = fit-first, soft upper-half anchor, defer the number. Posted range
  $98.4k–$164k. Do not commit a hard figure on the screen.
- **D-06:** Vocabulary bridges (BRG-01) are two-layered. Layer A = HR plain-language
  (≤10 s delivery). Layer B = technical T&D + tool bridges (MQTT→NATS, K8s→K3s, etc.).
- **D-07:** OSED pitch (BRG-02) is tiered: ≤90 s plain-language "tell me about yourself"
  for screen; ~2–3 min plain summary; full ~10-min technical pitch for later rounds. All
  versions open with a deployed outcome. Honest framing — no false production-FL claim.
- **D-08:** Four STAR stories: (1) OSED build, (2) HEMS PoC, (3) big-data substation
  analysis, (4) SI-MAPPER/MCP/agentic-AI → AGMS "scouts" (the #1 differentiator).
  Each story: plain-language screen version + ≤2-min technical STAR version, mapped to
  specific JD lines.
- **D-09:** JD-bullet question generator: behavioral "tell me about a time when…" + situational
  "how would you…" for each JD responsibility bullet; each anchored to concrete CV evidence.
- **D-10:** 12 tough domain questions (QNA-01), differentiator-weighted (Kalman/DSSE/federated/
  patents), mined from the prior-phase "<3-min say-aloud" tracks. Tagged for rounds 2–4.
- **D-11:** Consolidated bank (QNA-03) organized by interview round (HR-screen → technical
  → behavioral) and by category.
- **D-12:** HR-screen question set lives in `PHONE-SCREEN.md`: tell-me-about-yourself, why
  role / why GE Vernova, why leave Hydro-Québec, strengths/weaknesses, salary, availability,
  work-auth & relocation.
- **D-13:** Two system-design drills (QNA-02), ASCII-whiteboard + narration format (mirror
  STK-05): (1) 500-node virtual-sensing pipeline (K3s + NATS + EKF + federated + GitOps);
  (2) close-the-loop simulation / digital-twin → field validation.
- **D-14:** Flashcards + tracker + written rehearsal protocol. `REHEARSAL-TRACKER.md` table.
  One-page protocol: out loud, record & time, space across days, hit target durations,
  flag 2–3 weakest. Target times: bridges ≤10 s, STAR ≤2 min, phone-screen pitch ≤90 s,
  full OSED pitch ~10 min.
- **D-15:** Oral-rehearsal note style + honest bridge framing + Markdown + selective LaTeX
  only in technical-round material. Screen material stays jargon-light.
- **D-16:** No new technical material. Phase 6 synthesizes Phase 1–5 notes only.

### Claude's Discretion

Exact filenames/slugs within `notes/`; section ordering within each doc; exact wording of
pitch opening hook; which JD bullets get both question styles vs. one; exact membership of the
12 differentiator-weighted questions; precise plain-language analogies in Layer-A bridges;
how richly STAR story 4 cross-links to Phase 3 patent deck; target-time numbers in tracker.

### Deferred Ideas (OUT OF SCOPE)

- Deep technical-round live drills beyond QNA-01/QNA-02
- Live mock-interview role-play (usage activity, not a written deliverable)
- Folding material into Phase 7 HTML study site (Phase 7 is already complete)
</user_constraints>

---

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| BRG-01 | Rehearsed vocabulary-bridge table translating each OSED/HEMS/SI-MAPPER concept to its T&D analog | Layer A (HR translation) and Layer B (technical tool bridges) structure defined; raw bridges already present as "→ Bridge to your work" callouts in every Phase 1–5 note |
| BRG-02 | 10-minute OSED pitch rewritten in GE Vernova vocabulary, outcome-first | Tiered structure defined (90 s / 2–3 min / 10 min); deployed-outcome opening hook identified; honest-framing constraint documented |
| BRG-03 | Three STAR behavioral stories mapped to JD lines (extended to four by D-08) | STAR method structure, timing, JD-line mapping technique documented; CV evidence inventory complete |
| QNA-01 | 12 tough domain questions with strong personalized answer keys, rehearsed aloud | Raw material is the per-note "<3-min say-aloud" tracks from Phases 1–5; differentiator weighting defined by CLAUDE.md gap-priority order |
| QNA-02 | At least two system-design drill walkthroughs | Drill topics and format (ASCII + narration mirroring STK-05) locked by D-13; raw architecture content from STK-05 and FED-01/02/03 |
| QNA-03 | Consolidated mock-interview question bank (technical + domain + behavioral) for final-day rehearsal | Round-based organization structure defined; merger of HR-screen set + JD-bullet bank + 12 domain Qs |
</phase_requirements>

---

## Summary

Phase 6 is a synthesis-and-packaging phase, not a technical-content phase. Every piece of
knowledge exists in the Phase 1–5 notes; the work is to convert that knowledge into verbal,
timed, pressure-tested answers layered by interview round. The governing reframe (D-01) is
that the first interview is an HR phone screen, not a technical round, so the highest-yield
work is plain-language self-presentation and logistics scripting, not another deep-dive into
Kalman filters.

The research confirms two areas where outside knowledge genuinely matters: (1) HR phone-screen
dynamics and STAR-method technique, where established best practices can directly shape the
document structure and content of `PHONE-SCREEN.md` and `STAR-STORIES.md`; and (2) TN visa
logistics, where the June 2025 USCIS policy tightening introduces material risk that must be
flagged accurately. For all technical domain content, the research rule is D-16: cross-reference
Phase 1–5 notes, do not re-derive.

The raw material inventory below confirms that every requirement has draft content already
waiting in Phase 1–5 notes — this phase's plan tasks are about extraction, tightening, and
packaging, not authoring. The six deliverable files map cleanly to the six requirements.

**Primary recommendation:** Plan tasks that (1) extract and tighten the existing bridge callouts
and say-aloud tracks, (2) author the phone-screen front matter using the logistics facts from
D-03/04/05, (3) assemble the JD-bullet question bank from the JD bullets, and (4) build the
two system-design drills from the STK-05 architecture. Do not author new technical content.

---

## Architectural Responsibility Map

This phase has no software architecture. The "architecture" is the document set and the
layering of answers by interview round.

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Phone-screen content | `PHONE-SCREEN.md` | `REHEARSAL-TRACKER.md` | First-consumed doc; all screen-relevant material in one place |
| Vocabulary bridges | `REFRAME.md` | `PHONE-SCREEN.md` (Layer A references) | Bridges needed for both screen and technical rounds; keep in one indexed table |
| STAR stories | `STAR-STORIES.md` | `QUESTION-BANK.md` (cross-reference) | Stories are the behavioral answer to JD-bullet Qs; cross-link, don't duplicate |
| Q&A bank | `QUESTION-BANK.md` | `REHEARSAL-TRACKER.md` (flashcard prompts) | Single source of truth for all questions; tracker references by ID |
| System-design drills | `SYSTEM-DESIGN-DRILLS.md` | `QUESTION-BANK.md` (round-3/4 tag) | Standalone walkthrough docs; tagged in question bank as technical-round items |
| Rehearsal protocol | `REHEARSAL-TRACKER.md` | All other docs (cross-linked) | Governs HOW to use all other deliverables |

---

## Raw Material Inventory (Phase 1–5 Notes)

> This section is the planner's source for "what to lift." Every item listed contains draft
> content Phase 6 should extract, not re-author.

### Phase 1 — Kalman / Virtual Sensing Fusion Engine

| File | Extractable for Phase 6 |
|------|------------------------|
| `KAL-01-virtual-sensing-fusion-engine.md` | `<3-min say-aloud>` → QNA-01 answer key Q1 ("what is virtual sensing"); "→ Bridge to your work" = OSED edge-inference analogy for REFRAME Layer B |
| `KAL-02-kalman-family-kf-ekf-ukf.md` | `<3-min say-aloud>` → QNA-01 answer key Q2 (KF→EKF→UKF progression) |
| `KAL-03-fase-augmented-load-feeder-walk.md` | `<3-min say-aloud>` → QNA-01 answer key Q3 (FASE dark-node walk; ORACS covariance framing) |
| `KAL-04-ieee738-asset-health-ekf.md` | Bridge callout → REFRAME Layer B (DLR / asset-health = OSED anomaly detection analog) |

### Phase 2 — Distribution Virtual Sensing (DSSE)

| File | Extractable for Phase 6 |
|------|------------------------|
| `DSSE-01-under-observability-and-information-sourcing.md` | `<3-min say-aloud>` → QNA-01 answer key Q4 (under-observability, information sourcing); bridges → REFRAME |
| `DSSE-02-side-information-taxonomy.md` | Bridge callouts → REFRAME Layer B (AMI / smart-inverter self-reports analogy to OSED telemetry ingestion) |
| `DSSE-03-distribution-modeling-and-pseudo-measurement-honesty.md` | Honesty framing → STAR story 1 (honest bridge: OSED ≠ DSSE, it is an analog) |
| `DSSE-04-virtual-sensing-in-agms-and-federated-dsse.md` | `<3-min say-aloud>` → QNA-01 answer key Q5 (AGMS Inspector-scout placement); ORACS Observability index framing for STAR story 4 |

### Phase 3 — Director's Patents

| File | Extractable for Phase 6 |
|------|------------------------|
| `AGMS-patent-rehearsal-deck.md` | Entire doc is rehearsal-ready: 90-second family pitch → PHONE-SCREEN differentiator hook; per-patent summary + connection + question → STAR story 4 differentiator framing and QNA-01 answer keys Q6/Q7 |

### Phase 4 — Protocols, Stack & Architecture

| File | Extractable for Phase 6 |
|------|------------------------|
| `STK-01-protocol-stack.md` | Bridge callouts → REFRAME Layer B (Modbus→DNP3, Zigbee→LoRa); QNA-01 answer key Q8 |
| `STK-02-iec-61850.md` | Bridge callout → REFRAME Layer B; awareness bridges for plain-language screen |
| `STK-03-messaging-orchestration.md` | Bridge callouts → REFRAME Layer B (MQTT→NATS, K8s→K3s) |
| `STK-04-observability.md` | Bridge callout → REFRAME Layer B (InfluxDB→Prometheus); QNA-01 answer key Q9 |
| `STK-05-reference-architecture.md` | ASCII diagram + narration → SYSTEM-DESIGN-DRILLS.md drill 1 seed; AGMS overlay = patent hook in drill 1 closing |

### Phase 5 — Federated Architectures & Security

| File | Extractable for Phase 6 |
|------|------------------------|
| `FED-01-federated-vs-distributed.md` | `<3-min say-aloud>` → QNA-01 answer key Q10 (federated vs distributed, FedAvg/FedProx) |
| `FED-02-byzantine-robustness.md` | `<3-min say-aloud>` → QNA-01 answer key Q11 (Krum/coord-median, Byzantine robustness) |
| `FED-03-edge-security.md` | `<3-min say-aloud>` → QNA-01 answer key Q12 (OTA signing, TPM, SPIFFE/SPIRE) + bridge callouts → REFRAME Layer B |

### The 04-HUMAN-UAT.md Tracker Format

The existing `04-HUMAN-UAT.md` uses YAML frontmatter (status/phase/source/started/updated),
a `## Current Test` section, numbered `### N. [test name]` entries with `expected:` and
`result: [pending]` fields, and a `## Summary` table (total/passed/issues/pending/skipped/
blocked). `REHEARSAL-TRACKER.md` should mirror this structure with columns adapted for oral
rehearsal: prompt · said-aloud date · timed duration · confidence (✗/⚠/✓) · notes.
[VERIFIED: reading 04-HUMAN-UAT.md directly]

---

## Standard Stack

This phase has no software stack. The deliverable format is Markdown, consistent with all
prior phases. The "stack" is the document conventions from D-15.

### Document Conventions (from D-15, verified in Phase 1–5 notes)

| Convention | Detail | Where enforced |
|------------|--------|----------------|
| Header block | `**For:** / **Purpose:**` in every note | All Phase 1–5 notes |
| Depth strategy line | Italic blockquote naming FULL/AWARENESS depth + ceiling | STK notes, FED notes |
| Say-aloud track | `## <3-min say-aloud version` block using a blockquote | KAL-01, KAL-03, FED-01/02/03, DSSE-04 |
| Bridge callout | `**→ Bridge to your work:**` inline paragraph | All Phase 1–5 notes |
| LaTeX | `$…$` / `$$…$$` in technical-round material only | KAL/DSSE notes; forbidden in screen material |
| Target time annotations | Explicit aloud targets ("≤2 min", "≤90 s") | D-14 protocol; mirror in REHEARSAL-TRACKER |

---

## Architecture Patterns (Document Structure)

### Document Set Layout

```
.planning/phases/06-synthesis-drills-mock-interview/notes/
├── PHONE-SCREEN.md          # PRIMARY (round 1) — all screen content
├── REFRAME.md               # BRG-01 (bridge table) + BRG-02 (tiered OSED pitch)
├── STAR-STORIES.md          # BRG-03 + D-08 4th story (STAR × 4, two versions each)
├── QUESTION-BANK.md         # D-09 JD-bullet Qs + QNA-01 (12 Qs) + QNA-03 (merged bank)
├── SYSTEM-DESIGN-DRILLS.md  # QNA-02 (2 drills, ASCII + narration)
└── REHEARSAL-TRACKER.md     # D-14 (flashcard tracker + written protocol)
```

### PHONE-SCREEN.md Internal Structure

```
For: / Purpose: header
## 0. How This Doc Works (round-tagging legend)
## 1. Tell Me About Yourself (≤90 s script)
## 2. Why This Role / Why GE Vernova
## 3. Why Leave Hydro-Québec
## 4. Work Authorization & Relocation (TN one-liner + relocation line)
## 5. Salary Expectations (fit-first script, defer the number)
## 6. Strengths & Weaknesses (plain language)
## 7. Behavioral Screen Questions (plain-language versions from D-09)
## 8. Notice Period / Availability
## <say-aloud track> — full screen arc in ~10 minutes
```

### REFRAME.md Internal Structure

```
For: / Purpose: header
## Layer A — HR Translation Bridges (plain language, ≤10 s each)
| Your term | HR plain-language analog | GE Vernova term |
## Layer B — Technical Tool Bridges (for technical rounds)
| Your tool | GE Vernova tool | One-liner justification |
## Tiered OSED Pitch
### Version 1: ≤90 s (screen)
### Version 2: ~2–3 min (first technical touch)
### Version 3: ~10 min (deep technical round)
```

### STAR-STORIES.md Internal Structure

```
For: / Purpose: header
## How to Use (plain version first; ≤2-min technical on request)
## Story 1: OSED Build — [JD lines mapped]
  ### Screen version (plain, ≤90 s)
  ### Technical STAR (≤2 min)
  ### JD-line mapping
## Story 2: HEMS PoC — [JD lines mapped]
  ... same structure
## Story 3: Big-Data Substation Analysis — [JD lines mapped]
  ... same structure
## Story 4: SI-MAPPER / MCP / Agentic AI → AGMS Scouts — [JD lines mapped]
  ... same structure (the differentiator)
```

### QUESTION-BANK.md Internal Structure

```
For: / Purpose: header
## Part A — JD-Bullet Question Generator (D-09)
  ### Edge Engineering & Data Pipelines bullets
  ### Virtual Sensing & Control bullets
  ### Simulation & Integration bullets
  ### Required Skills bullets
  (each bullet: behavioral Q + situational Q + CV anchor)
## Part B — 12 Tough Domain Questions (QNA-01, rounds 2–4)
  (numbered Q1–Q12, each: prompt + bullet answer key mined from say-aloud tracks)
## Part C — Consolidated Bank (QNA-03)
  ### Round 1: HR Screen
  ### Rounds 2–3: Technical/Domain
  ### Any Round: Behavioral
```

### SYSTEM-DESIGN-DRILLS.md Internal Structure

```
For: / Purpose: header
## Drill 1: 500-Node Virtual Sensing Pipeline
  ### Problem Statement (2–3 sentences)
  ### ASCII Whiteboard Diagram
  ### Narration Script (component-by-component walk)
  ### Key Justification One-Liners (K3s/NATS/EKF/Flower/GitOps)
## Drill 2: Close the Loop — Simulation / Digital Twin → Field Validation
  ### Problem Statement
  ### ASCII Whiteboard Diagram
  ### Narration Script
  ### Key Justification One-Liners (EMT/Opal-RT awareness, validate vs. model, AGMS)
```

### REHEARSAL-TRACKER.md Internal Structure

```
YAML frontmatter (status, phase, started, updated)
## Rehearsal Protocol (one page: aloud, record, time, space, flag weakest)
  Target times table:
  | Item | Target | Pass/Fail |
  | Bridges (each) | ≤10 s | |
  | STAR stories | ≤2 min | |
  | Phone-screen arc | ≤90 s | |
  | Full OSED pitch | ~10 min | |
## Tracker — Screen Material (Round 1)
  | # | Prompt | Said Aloud | Duration | Confidence | Notes |
## Tracker — Technical Questions (Rounds 2–4)
  | # | Q-ID | Said Aloud | Duration | Confidence | Notes |
## Tracker — STAR Stories
  | # | Story | Version | Said Aloud | Duration | Confidence | Notes |
## Tracker — System-Design Drills
  | # | Drill | Said Aloud | Duration | Confidence | Notes |
## Summary
  total / passed / weak (need re-run) / pending
```

---

## HR Phone-Screen Best Practices

### What a Non-Technical HR Screener Actually Does

[CITED: keka.com/top-phone-screening-interview-questions]
[CITED: breezy.hr/blog/phone-screen-interview]

The HR screen (typically 15–30 minutes) has one job: determine whether to advance the
candidate to the technical rounds. The screener is non-technical and probes five areas:

1. **CV verification** — does the experience match what was written?
2. **Role interest / motivation** — why this company and role?
3. **Culture and communication fit** — can this person speak clearly and professionally?
4. **Logistics** — work authorization, relocation readiness, availability, salary range fit
5. **Basic behavioral fit** — 1–2 soft-skills behavioral questions, if any

Technical depth is NOT tested in round 1. Screeners use structured question lists and will
note answers for hiring-manager review. They screen OUT on: disorganized answers, salary
misalignment, logistics problems, and inability to connect experience to the role.

**Implication for Phase 6:** `PHONE-SCREEN.md` is a scripted, outcome-first, plain-language
document. Every answer should pass a "would a non-engineer friend understand this?" test.
Equations, acronyms, and architecture diagrams do not belong there.

### "Tell Me About Yourself" — Proven Structure

[CITED: indeed.com/career-advice/interviewing/phone-interview-questions-and-answers]
[CITED: themuse.com/advice/phone-screen-definition-preparation]

The standard 60–90 s structure that interviewers expect:
1. **Current position + headline accomplishment** (one sentence, outcome-first)
2. **Relevant past experience** (one sentence, outcome-first; avoid deep history)
3. **Why this role / forward-looking hook** (one sentence linking to GE Vernova's mission)

For Juan: open with the deployed outcome (the 21% energy-cost result) in plain language,
name Hydro-Québec as context, then pivot to the GE Vernova mission. Do NOT open with "I have
a PhD in…" — that is past-focused and jargon-triggering.

**Model opening (for planner to tighten):**
> "I built and shipped a cloud-edge platform that is now running grid services on real field
> hardware and cut isolated-community energy costs by 21%. I've spent the last [N] years at
> Hydro-Québec bridging machine learning, control systems, and IoT at the distribution edge —
> and GE Vernova's mission to push intelligence into the field at scale is exactly where I want
> to take that work next."

### Common Screen-Out Triggers and Neutralizations

[ASSUMED — drawn from established interview-coaching consensus; not verified against a single
source; flag for Juan's review]

| Screen-Out Trigger | Neutralization |
|--------------------|----------------|
| "Can they work in the US?" | TN one-liner up front (see D-03 / TN section below) |
| "Will they actually relocate?" | Melbourne research line (D-04) |
| "Is salary expectation realistic?" | Fit-first pivot + soft senior anchor (D-05) |
| Jargon-heavy answer to "tell me about yourself" | Deployed-outcome opening; no PhD/DSSE mention |
| Vague answers with no numbers | Anchor every answer to a specific outcome (21%, billions of points) |
| Trash-talking current employer | Forward-framing of why-leave: mission alignment, not complaint |

### "Why Leave Hydro-Québec" — Forward-Framing Technique

[CITED: careerbuilder.com/advice/blog/common-questions-in-an-exit-interview-and-how-to-answer-them]

The standard guidance: lead with what pulls you toward the new role, not what pushes you from
the current one. Frame departure as a proactive career move toward mission alignment, not a
complaint. For Juan:

> "Hydro-Québec gave me a rare combination — PhD-level research access with production
> deployment responsibility. I'm proud of that. The reason I'm excited about this conversation
> is that GE Vernova is building at exactly the scale and in exactly the domain — T&D
> intelligence at the field edge — where I want to invest the next chapter. This role is the
> convergence point I've been working toward."

---

## TN Visa Logistics Research

> **IMPORTANT:** USCIS released a material policy change in June 2025 affecting TN eligibility.
> Several claims in this section are MEDIUM confidence because the June 2025 guidance is recent
> and its application to Juan's specific role requires an immigration attorney review.

### What Changed — June 2025 USCIS Policy Update

[CITED: natlawreview.com/article/uscis-makes-changes-tn-policy-manual-key-updates-employers]
[CITED: stoneoakimmigration.com/major-tn-visa-changes-june-2025-uscis-policy-updates]
[CITED: rjimmigrationlaw.com/resources/2025-tn-visa-update-uscis-tightens-rules-for-multiple-professions]

On June 4, 2025, USCIS released updated guidance that tightens TN eligibility requirements.
Key changes relevant to Juan:

**Engineer category (tightened):**
- Must have a bachelor's degree in the related engineering field (EE, CE, CompE qualify; CS
  may not qualify for the Engineer category)
- Job duties must align with engineering tasks per the Occupational Outlook Handbook
- Generic IT or software-development roles are more likely to be excluded
- **Positive signal for Juan:** A PhD in Electrical Engineering + a job title of "Senior
  Software Engineer & Scientist" with duties in "virtual sensing algorithms, state estimation,
  control theory" maps more cleanly to the Engineer category than a generic SWE role

**Computer Systems Analyst category (confirmed restriction):**
- "Programmers are not included"; incidental programming permitted
- Role must focus on systems analysis, not software development
- **Risk for Juan:** His role includes "Build and deploy edge-native software components"
  which sounds like software development — the Computer Systems Analyst category may not apply

**Scientist category:**
- Must work in direct support of engineering/scientific disciplines listed in USMCA Annex
- The "Senior Software Engineer & Scientist" dual title may support a Scientist application
- Physics, Engineering Science, Computer Science as named disciplines [ASSUMED]

**Canadian citizen port of entry change:**
- As of June 2025, Canadians may only apply for TN status at pre-flight inspection stations
  in Canada, not at US ports of entry at the land border or in the terminal
  [CITED: stoneoakimmigration.com — MEDIUM confidence; verify with GE Vernova HR or attorney]

### What Juan Should Say in the Phone Screen

Given the policy uncertainty, the D-03 framing should be confident but accurate:

**Revised TN one-liner (more defensible than CONTEXT.md draft):**
> "As a Canadian citizen, I'm TN-visa eligible under USMCA — this role's combination of
> engineering work and my electrical engineering PhD is a clean fit for the Engineer category.
> There's no H-1B lottery, no waiting period, low cost to the company."

**What NOT to say:** Do not mention "Scientist / Computer Systems Analyst" as backup
categories until you have confirmed with an immigration attorney which category GE Vernova's
legal team intends to use. The screener does not need this detail — they need reassurance
that authorization is fast, cheap, and certain.

**Follow-up action before the screen (flagged for Juan):** Contact a Canadian immigration
attorney or GE Vernova HR to confirm which TN category the offer letter will cite. The
June 2025 tightening makes this a one-call verification, not an assumption.

### Comp Script (D-05)

[ASSUMED — general salary-negotiation technique; no single source]
[CITED: glassdoor.com/Interview/One-is-asked-about-desired-salary — general guidance]

Posted range: $98.4k–$164k. Strategy: acknowledge range, gently anchor seniority, defer.

> "The posted range looks reasonable for a senior role. My priority right now is proving I'm
> the right long-term fit — once we both see that clearly, I'm confident we'll align on a
> number that reflects that seniority. I don't want the comp conversation to get in the way of
> understanding whether this is the right match."

Do NOT give a specific number. The person who names a number first is anchored. The screener
cannot negotiate; they can only note whether the candidate is "within range."

---

## STAR Method Best Practices

[CITED: blog.theinterviewguys.com/the-star-method]
[CITED: indeed.com/career-advice/interviewing/how-to-use-the-star-interview-response-technique]
[CITED: capd.mit.edu/resources/the-star-method-for-behavioral-interviews]

### Tight 2-Minute STAR Structure

A 2-minute STAR answer allocates time approximately as follows:

| Component | Time | Key discipline |
|-----------|------|----------------|
| **S**ituation | ~15 s | One sentence; just enough context for the interviewer to place the story |
| **T**ask | ~15 s | What you specifically owned; distinguish your role from team's role |
| **A**ction | ~60 s | The longest section; specific decisions, why you made them, what you did |
| **R**esult | ~30 s | Quantified outcome + retrospective insight; end with impact, not process |

**Key discipline:** The Result must come last and must be quantified wherever possible. Do not
bury the outcome in the middle of the narrative. If the screener interrupts or cuts you short,
make sure the result has already been stated.

### Outcome-First Discipline

[CITED: milestonecareer.org/blog — MEDIUM confidence]

For Juan's plain-language screen versions, reverse the natural chronological order: open with
the result, then contextualize. This is especially important for the 90 s screen version of
each story.

**Anti-pattern:** "I was working on OSED, which was a project where we tried to…"
**Pattern:** "This project cut isolated-community energy costs by 21%. Here's how: I built…"

### Mapping Stories to JD Lines

Each STAR story should have an explicit "**JD line mapping**" sub-section that names the exact
JD bullet the story satisfies. This serves two purposes: (1) Juan can retrieve the right story
under pressure when asked a JD-bullet behavioral question, and (2) a reviewer can verify
requirements coverage.

**Suggested JD-line anchors (for planner to verify against full JD text):**

| Story | Primary JD Line | Secondary JD Line |
|-------|-----------------|-------------------|
| OSED build | "Build and deploy edge-native software components for decentralized operation" | "Develop federated data pipelines that allow distributed nodes to collaborate securely" |
| HEMS PoC | "Deploy adaptive edge intelligence and control logic to enable real-time grid insights" | "Apply control theory and signal processing techniques (e.g., Kalman filters, state estimation)" |
| Big-data substation analysis | "Integrate field data sources (SCADA, PMUs, DER controllers)" | "Domain Expertise: Proven experience with T&D applications" |
| SI-MAPPER / MCP → AGMS scouts | "Integrate AI/ML capabilities, federated control frameworks, and digital twins" | "Bridge the gap between simulation environments and live grid operations" |

---

## JD-Bullet Question Generator Technique (D-09)

### The Method

[ASSUMED — standard behavioral-interview question-generation technique; no single source]

For each JD responsibility bullet, produce:
- **Behavioral:** "Tell me about a time when you [verb from JD bullet]…"
- **Situational:** "How would you approach [JD bullet scenario]…"
- **CV anchor:** The specific project/metric/story that satisfies the question

**The behavioral question belongs in the HR-screen section of `QUESTION-BANK.md`** (screeners
use these). The situational / technical question is tagged for technical rounds 2–3.

### JD Bullet Inventory (for planner's question-generation pass)

From `docs/job-requirements.md`, the responsibility bullets are:

**Edge Engineering & Data Pipelines:**
1. Build and deploy edge-native software components for decentralized operation, sensing, and control
2. Develop federated data pipelines that allow distributed nodes to collaborate securely without central coordination
3. Integrate field data sources (SCADA, PMUs, DER controllers) and industrial IoT protocols (LoRa, MQTT, DNP3, Modbus)

**Virtual Sensing & Control:**
4. Develop and deploy robust virtual sensing algorithms to infer critical power grid parameters from limited edge sensor data
5. Deploy adaptive edge intelligence and control logic to enable real-time grid insights with minimal latency
6. Apply control theory and signal processing techniques (e.g., Kalman filters, state estimation) to refine virtual sensor accuracy

**Simulation & Integration:**
7. Collaborate with power systems engineers to validate virtual sensor performance against physical models and real-world field data
8. Bridge the gap between simulation environments and live grid operations to "close the loop"
9. Integrate AI/ML capabilities, federated control frameworks, and digital twins into next-generation grid platforms

**Required Skills (key bullets for question generation):**
10. Deep experience with Kubernetes/K3s, Kafka/NATS, MQTT, gRPC, and Pulsar
11. Hands-on experience with InfluxDB/TimescaleDB and observability stacks (Prometheus, Grafana)
12. Proven experience with federated architectures, resilient edge software, and T&D applications
13. Experience developing and deploying AI/ML models in production environments

That is 13 JD bullets → 13 behavioral + 13 situational questions → 26 entries in Part A of
`QUESTION-BANK.md`. The planner should assign one plan task per JD section (three bullets
each) to keep tasks manageable.

---

## 12 Tough Domain Questions — Differentiator-Weighted Membership

The 12-question set (QNA-01) should be weighted by the CLAUDE.md gap-priority order and the
specific differentiator framing from CONTEXT.md D-10. Suggested membership (for planner; this
is Claude's discretion per CONTEXT.md):

| Q# | Topic | Source note for answer key | Differentiator level |
|----|-------|---------------------------|----------------------|
| Q1 | What is virtual sensing and why does distribution differ from transmission? | KAL-01 `<3-min>` | HIGH |
| Q2 | Walk me through KF→EKF→UKF and when you'd choose each | KAL-02 `<3-min>` | HIGH |
| Q3 | Explain FASE: how do you estimate a dark node? | KAL-03 `<3-min>` | HIGH — differentiator |
| Q4 | What is under-observability and how do you source side information? | DSSE-01 `<3-min>` | HIGH |
| Q5 | How does virtual sensing sit inside the AGMS architecture? | DSSE-04 `<3-min>` | HIGH — patent connection |
| Q6 | Walk me through the AGMS patent family in 90 seconds | Patent deck `## The ~90-Second Pitch` | HIGHEST — differentiator |
| Q7 | What is the Operation Loop Formation patent and why is it the granted one? | Patent deck Patent 4 section | HIGHEST |
| Q8 | Justify NATS JetStream vs. MQTT vs. Kafka for a substation edge node | STK-03 `<say-aloud>` | MEDIUM-HIGH |
| Q9 | How would you observe a federated K3s fleet? What Prometheus tells you that InfluxDB doesn't | STK-04 `<say-aloud>` | MEDIUM |
| Q10 | Distinguish federated from distributed learning; explain FedAvg | FED-01 `<3-min>` | HIGH |
| Q11 | How does Krum make gradient aggregation Byzantine-robust? | FED-02 `<3-min>` | MEDIUM-HIGH |
| Q12 | What does "edge security beyond TLS" mean? Name three mechanisms | FED-03 `<3-min>` | MEDIUM-HIGH |

Each answer key = the bullet-summary of the corresponding `<3-min say-aloud>` track, tightened
to ~5–7 bullets for fast recall. The say-aloud tracks exist in the source notes — the planner
task is to extract, not to write.

---

## System-Design Drill Format

[VERIFIED: reading STK-05-reference-architecture.md directly]

STK-05 establishes the format the two drills should mirror:
1. **For:/Purpose: header** — identifies the rehearsal goal and what criteria it satisfies
2. **ASCII diagram** — a box-and-arrow diagram drawable from memory in ~90 s; labeled tiers
   with key components and protocol arrows
3. **Narration script** — numbered sections, each a spoken paragraph covering one tier or
   component; includes "why this component" justification for each choice
4. **Closing hook** — the AGMS overlay or patent connection as the differentiation move
5. **Target time** — state the total expected narration time (e.g., ~5 min per drill)

**Drill 1 seed (from STK-05):** The four-tier ASCII diagram in STK-05 is a near-complete
seed for drill 1. The planner task is to adapt it: (a) scope to 500-node fleet context,
(b) add GitOps fleet management component (STK-05 does not highlight GitOps explicitly),
(c) add the federated aggregator as a named component with Flower reference, (d) narrate
the EKF/virtual-sensing engine as the edge computation.

**Drill 2 seed:** DSSE-04 provides the AGMS simulate-before-commit loop (Operation Loop
Formation patent, `simulate-before-commit` framing). STK-05 section 4 ("Tier 2 — Edge")
notes the field validation loop. The drill narration should walk: (1) EMT model baseline
(awareness level), (2) virtual sensor output vs. model output comparison, (3) when the
virtual sensor diverges → triggers a field validation request, (4) field data feeds back to
retrain the model → the loop closes. AGMS closing hook: the Operation Loop Formation
"simulate-before-commit" gate is the patent embodiment of this exact validate-before-act
philosophy.

---

## Rehearsal Mechanics — Evidence-Based Protocol

[CITED: bcu.ac.uk/exams-and-revision/best-ways-to-revise/spaced-repetition]
[CITED: blog.pastpaperhub.com/2025/09/active-recall-spaced-repetition-science]

### Core Technique: Active Recall + Spaced Repetition

Active recall (test yourself before checking the answer) is consistently the highest-effect
study technique in the evidence base. Combined with spaced repetition (increasing intervals
between review sessions), it is the fastest path to confident retrieval under pressure.

For Juan's ~1-week runway from 2026-06-16 to the phone screen:

**Suggested spacing protocol (for REHEARSAL-TRACKER.md protocol section):**

| Day | Activity |
|-----|----------|
| Day 1 (today) | First pass: read each section of PHONE-SCREEN.md aloud; time yourself |
| Day 2 | Active recall: cover answer keys, say each bridge aloud, then check |
| Day 3 | Active recall: full phone-screen arc (≤90 s) + two STAR stories, timed |
| Day 4 | Weak items only: flag and repeat the ⚠ items from Day 3 tracker |
| Day 5 | Full mock pass: every screen question + STAR stories; update tracker |
| Day 6 | Weak items only: the 2–3 flagged items from Day 5 |
| Day 7 (screen eve) | Light pass: bridges only; no deep technical review — trust the work |

**Active recall mechanics for flashcard-style tracker:**
- The prompt column IS the flashcard front
- The candidate covers the answer-key and says the answer aloud
- Only then checks the answer-key bullets
- Marks confidence: ✗ = didn't get it / ⚠ = partial / ✓ = solid
- Any ✗ or ⚠ goes to the next-session repeat list

### Target Durations (from D-14 — confirmed sensible)

| Item | Target | Rationale |
|------|--------|-----------|
| Each bridge sentence | ≤10 s | Conversational; anything longer is recitation |
| STAR story (screen version) | ≤90 s | Screener attention span; matches "tell me about yourself" |
| STAR story (technical version) | ≤2 min | Standard behavioral answer target; prevent rambling |
| Phone-screen opening arc | ≤90 s | The "tell me about yourself" slot is typically <2 min |
| Full OSED pitch (technical) | ~10 min | A full technical "walk me through your work" answer |
| System-design drill (each) | ~5 min | Whiteboard narration in a 45-min technical round |

---

## Vocabulary Bridge — Inventory of Raw Bridges to Lift

Every Phase 1–5 note contains a "→ Bridge to your work" callout. The planner tasks should
instruct the implementer to read each note and extract these callouts directly into REFRAME.md.

**Layer A bridges to author (HR plain-language — not pre-written; Claude's discretion per D-06):**

| Your technical term | Plain-language "HR translation" target |
|---------------------|---------------------------------------|
| MQTT + K8s edge orchestration | "I make thousands of field devices coordinate in real time" |
| EKF / state estimation | "Software that infers what a sensor would read at a location that has no sensor" |
| Federated learning | "Models trained locally at each site; only the learning, not the raw data, is shared" |
| Convex optimization / MPC | "Software that makes the optimal control decision every few seconds" |
| IEC 61850 GOOSE | "A sub-4-millisecond protection signal — the fire alarm of the substation" |
| ORACS / CaCSM | "The grid's autonomous response system — the director's patented architecture" |

*(These are seed examples per the CONTEXT.md D-06 specifics. Planner should instruct full
expansion to cover all terms in the bridge table.)*

**Layer B bridges to extract (already written in Phase 1–5 notes):**

| Source note | Bridge type | Content status |
|-------------|-------------|----------------|
| KAL-01 | OSED edge inference → virtual-sensing fusion engine | WRITTEN in note |
| KAL-04 | OSED anomaly detection → DLR asset-health analog | WRITTEN in note |
| STK-01 | Modbus → DNP3; Zigbee → LoRa | WRITTEN in note |
| STK-03 | MQTT → NATS JetStream; K8s → K3s | WRITTEN in note |
| STK-04 | InfluxDB push → Prometheus pull | WRITTEN in note |
| FED-03 | MQTT device fleet → SPIFFE/SPIRE workload identity | WRITTEN in note |
| DSSE-02 | AMI/inverter self-reports → OSED telemetry ingestion | WRITTEN in note |

---

## Don't Hand-Roll

| Problem | Don't Build | Use Instead |
|---------|-------------|-------------|
| HR-screen question content | Inventing questions from scratch | Derive from JD bullets (D-09) + standard HR-screen set (D-12) |
| Bridge sentences (Layer B) | Writing new bridges | Lift from existing "→ Bridge to your work" callouts in Phase 1–5 notes |
| Domain Q answer keys | Re-deriving technical content | Lift from `<3-min say-aloud>` tracks in Phase 1–5 notes (D-16) |
| OSED pitch technical content | Rewriting OSED from memory | Lift from KAL-01 and DSSE-04 say-aloud tracks; tighten for GE Vernova vocabulary |
| System-design drill 1 diagram | Drawing from scratch | Adapt the STK-05 ASCII diagram (D-13) |
| Rehearsal-tracker format | Inventing a new format | Mirror `04-HUMAN-UAT.md` structure (D-14) |

**Key insight:** Phase 6 is a packaging phase. Every sentence of technical content is already
authored. The risk is re-authoring instead of extracting — that wastes runway and introduces
inconsistency.

---

## Common Pitfalls

### Pitfall 1: Starting with technical depth instead of screen content
**What goes wrong:** The implementer authors the 12 domain questions (QNA-01) first because
they are technically interesting, leaving `PHONE-SCREEN.md` until the end. If time runs short,
the most important document is incomplete.
**Why it happens:** Technical content feels more substantial than scripting a 90-second pitch.
**How to avoid:** Plan tasks must author `PHONE-SCREEN.md` first. This is the phone-screen-first
principle (D-01).
**Warning signs:** A plan wave that starts with `QUESTION-BANK.md` before `PHONE-SCREEN.md`.

### Pitfall 2: Over-engineering the 90-second script into a memorized recitation
**What goes wrong:** The "tell me about yourself" becomes a word-for-word script that Juan
rehearses exactly as written but cannot adapt when interrupted.
**Why it happens:** Natural tendency to write prose, which then feels like something to memorize.
**How to avoid:** Write the 90-second version as a set of 4–5 numbered bullet points with the
opening hook sentence fully scripted; the rest are prompts, not scripts.
**Warning signs:** A prose paragraph with no structural markers.

### Pitfall 3: Burying the TN visa complexity in the phone-screen document
**What goes wrong:** `PHONE-SCREEN.md` includes a long explanation of the June 2025 USCIS
tightening, confusing Juan during the actual call.
**Why it happens:** The researcher has found nuance; the document inherits it.
**How to avoid:** `PHONE-SCREEN.md` contains only the one-liner script (D-03). The nuance and
the "consult attorney" flag lives in a footnote or a separate preparation note — not in the
verbal script itself.
**Warning signs:** More than 3 sentences on TN logistics in the PHONE-SCREEN say-aloud track.

### Pitfall 4: Writing STAR stories as essays instead of structured prompts
**What goes wrong:** STAR stories are written as flowing prose; Juan over-explains during the
screen and loses the result.
**Why it happens:** Narrative instinct.
**How to avoid:** Each version of each story is structured as: one-line hook → S (1 sentence)
→ T (1 sentence) → A (3–4 bullet actions) → R (1–2 quantified sentences). The plain-language
version should be completable in ≤90 s without notes.
**Warning signs:** STAR story sections with more than 300 words for the screen version.

### Pitfall 5: Including LaTeX in phone-screen material
**What goes wrong:** `PHONE-SCREEN.md` or the screen version of STAR stories contains formulas
(e.g., the EKF update equation) that look impressive in Markdown but are jargon on a phone call.
**Why it happens:** D-15 allows LaTeX generally; D-16 scope confusion.
**How to avoid:** Apply D-15 strictly: LaTeX is confined to technical-round material. Screen
material uses plain-language substitution ("software that updates its estimate of the voltage
using only the measurements available").
**Warning signs:** Any `$…$` or `$$…$$` in `PHONE-SCREEN.md` or the "Screen version" sections
of `STAR-STORIES.md`.

---

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | TN visa Engineer category is a clean fit for Juan's PhD in EE + "Senior Software Engineer & Scientist" role title | TN Visa Logistics | Wrong: GE Vernova might use a different TN category; the one-liner in PHONE-SCREEN.md becomes inaccurate. Mitigation: Juan should verify with GE Vernova HR or an immigration attorney before the screen. |
| A2 | Canadians may now only apply for TN status at pre-flight inspection stations in Canada, not at land-border ports of entry | TN Visa Logistics | Wrong: the source (stoneoakimmigration.com, June 2025) is a law firm blog, not the USCIS policy manual. Verify against uscis.gov/policy-manual before the interview. |
| A3 | The screen-out trigger table (jargon, lack of numbers, trash-talking) reflects current HR practice at a large US engineering firm | HR Screen Best Practices | Low-medium risk: these are well-established interview-coaching principles, unlikely to be specific to GE Vernova. Confidence: MEDIUM. |
| A4 | "Computer Systems Analyst" is unlikely to be the TN category GE Vernova's legal team would use for this role given the June 2025 tightening | TN Visa Logistics | Wrong: GE Vernova legal might specifically use this category. Do not proactively mention it in the screen. |
| A5 | The 12 Q membership table above is a correct interpretation of "differentiator-weighted" from D-10 | 12 Tough Domain Questions | Low risk: D-10 says differentiator-weighted but leaves membership to Claude's discretion. The table is a recommendation; the planner can adjust. |

---

## Open Questions

1. **TN category verification**
   - What we know: Engineer category likely fits; June 2025 tightened requirements; PhD in EE is
     strong qualification; role title includes "Scientist"
   - What's unclear: Which specific TN category GE Vernova's legal team intends to use on the
     offer letter
   - Recommendation: Juan should ask GE Vernova HR "which work authorization category would you
     use for this role?" either before or early in the process; or consult a Canadian immigration
     attorney. Do not improvise this on the phone screen.

2. **Current employer notice period**
   - What we know: Hydro-Québec is Juan's current employer; D-04 says relocation is eager and
     fast; no notice period is specified in CONTEXT.md
   - What's unclear: Juan's actual contractual notice period (typically 2–4 weeks for engineering
     roles in Quebec); what "availability" answer to give the screener
   - Recommendation: `PHONE-SCREEN.md` should include a placeholder `[NOTICE PERIOD]` for Juan
     to fill in with his actual contractual obligation before the screen.

3. **Whether the screener will ask behavioral questions**
   - What we know: Standard HR screens focus on logistics and fit; behavioral Qs are more common
     in subsequent rounds
   - What's unclear: GE Vernova's specific screening protocol (some large companies have the HR
     screener ask 1–2 behavioral Qs from a structured list)
   - Recommendation: Include 2–3 plain-language behavioral answers in `PHONE-SCREEN.md` as a
     "if asked" section; don't over-invest.

---

## Environment Availability

Step 2.6: SKIPPED (no external dependencies; this phase produces Markdown documents only).

---

## Validation Architecture

`nyquist_validation` is `false` in `.planning/config.json`. This section is omitted.

---

## Security Domain

`security_enforcement` is not set in `.planning/config.json`; however, this phase produces
only Markdown study documents. There is no code, no deployment, no secrets. ASVS categories
V2–V6 do not apply. Omitted.

---

## Sources

### Primary (HIGH confidence)
- `06-CONTEXT.md` (D-01 through D-16) — authoritative spec for all deliverable decisions
- `docs/job-requirements.md` — JD bullets for question generator; logistics facts
- Phase 1–5 notes (read directly) — raw material inventory confirmed
- `04-HUMAN-UAT.md` (read directly) — tracker format confirmed
- `STK-05-reference-architecture.md` (read directly) — drill format confirmed

### Secondary (MEDIUM confidence)
- [National Law Review — USCIS TN policy changes June 2025](https://natlawreview.com/article/uscis-makes-changes-tn-policy-manual-key-updates-employers)
- [Stone Oak Immigration — June 2025 TN changes](https://stoneoakimmigration.com/major-tn-visa-changes-june-2025-uscis-policy-updates/)
- [RJ Immigration Law — 2025 TN update](https://rjimmigrationlaw.com/resources/2025-tn-visa-update-uscis-tightens-rules-for-multiple-professions)
- [Indeed — phone interview best practices](https://www.indeed.com/career-advice/interviewing/phone-interview-questions-and-answers)
- [The Muse — phone screen preparation](https://www.themuse.com/advice/phone-screen-definition-preparation)
- [The Interview Guys — STAR method complete guide](https://blog.theinterviewguys.com/the-star-method/)
- [MIT CAPD — STAR method for behavioral interviews](https://capd.mit.edu/resources/the-star-method-for-behavioral-interviews/)
- [Birmingham City University — spaced repetition](https://www.bcu.ac.uk/exams-and-revision/best-ways-to-revise/spaced-repetition)

### Tertiary (LOW confidence — ASSUMED)
- Screen-out trigger table — interview-coaching consensus; not verified against GE Vernova-specific practice
- Salary deferral script — general negotiation technique; not verified against GE Vernova recruiter behavior
- Comp anchoring advice — general; GE Vernova HR may ask for a number regardless

---

## Metadata

**Confidence breakdown:**
- Document structure: HIGH — locked by CONTEXT.md D-02/D-06 through D-14
- HR screen technique: MEDIUM-HIGH — cited from multiple credible sources; standard practice
- TN visa logistics: MEDIUM — material policy change in June 2025; attorney verification needed
- STAR method: HIGH — well-established, multi-source confirmed
- Rehearsal mechanics: MEDIUM-HIGH — evidence-based (active recall / spaced rep); adapted to 1-week runway

**Research date:** 2026-06-16
**Valid until:** 2026-07-16 for technique content; TN section should be re-verified if the
interview is delayed past 2026-07-01 (USCIS policy continues to evolve)
