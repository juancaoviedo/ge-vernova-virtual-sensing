# Phase 6: Synthesis, Drills & Mock Interview - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-16
**Phase:** 6-Synthesis, Drills & Mock Interview
**Areas discussed:** Deliverable structure & rehearsal, The 12 tough questions (→ reframed to phone-screen-first), STAR stories & OSED pitch, System-design drills, JD-bullet question generation, Phone-screen logistics (work auth / relocation / comp), Rehearsal mechanism

---

## Area selection (multiSelect)

User selected **all four** offered areas and added a fifth directive via free text:
build JD-bullet-driven questions in two styles — *"tell me about a time when you … [JD bullet]"*
and *"how would you … [JD bullet]"* — from the JD bullet points, with guidance on how to
rehearse them, grounded in the CV. CV was read on this instruction.

---

## Deliverable structure

| Option | Description | Selected |
|--------|-------------|----------|
| Hybrid: ~4 docs + tracker | notes/: REFRAME, STAR-STORIES, QUESTION-BANK, SYSTEM-DESIGN-DRILLS + a thin REHEARSAL-TRACKER | ✓ |
| Single consolidated playbook | One INTERVIEW-PLAYBOOK.md with all six sections | |
| Six per-requirement files | BRG-01/02/03 + QNA-01/02/03 separate | |

**User's choice:** Hybrid: ~4 docs + tracker (later extended with a front PHONE-SCREEN doc per the reframe).
**Notes:** Matches the prior-phase `notes/` convention; coherent chunks to rehearse one at a time.

---

## The 12 tough questions → reframed to phone-screen-first

| Option | Description | Selected |
|--------|-------------|----------|
| Differentiator-weighted, tight bullet keys | Weight toward Kalman/DSSE/federated/patents, bullet keys | (kept, but staged) |
| Coverage-balanced across all 7 gaps | One/two Qs per gap | |
| Full prose model answers | Full sentences | |

**User's choice (the pivotal reframe):** *"I'm going to have the first interview, the phone
screen — a simple screening with an HR person, NOT a technical person. GE usually has four
rounds. I need to pass the phone screen to reach the technical rounds. Focus first on how to
present myself and show what I did in language understandable to a non-technical listener."*
**Notes:** This reframed the whole phase to **phone-screen-first** (CONTEXT D-01). The
differentiator-weighted 12 Qs are still built (D-10) but **staged for technical rounds 2–4**;
the plain-language self-presentation + fit + logistics becomes the primary deliverable.

---

## STAR stories & OSED pitch

| Option | Description | Selected |
|--------|-------------|----------|
| Add SI-MAPPER→scouts as a 4th STAR story | Standalone agentic-AI story, the #1 patent connection | ✓ |
| Keep 3 stories; thread SI-MAPPER through pitch + bridges | Differentiator surfaces in pitch/bridges only | |
| Swap big-data story for the SI-MAPPER story | Stay at 3, demote big-data | |

**User's choice:** Add SI-MAPPER→AGMS-scouts as a 4th STAR story.
**Notes:** Operation Loop Formation (US 12,596,341 B2) is GRANTED/assigned to GE Vernova —
the strongest "I already think like your lab" hook gets its own story (CONTEXT D-08).

---

## System-design drills

| Option | Description | Selected |
|--------|-------------|----------|
| Close-the-loop: sim/digital-twin → field validation | Covers JD "Simulation & Integration" | ✓ |
| Federated multi-area DSSE across substations | Deepens differentiators but overlaps drill 1 | |
| Edge ingest & bad-data fusion | SCADA+PMU+DER fuse + bad-data rejection | |

**User's choice:** Close-the-loop sim/digital-twin → field validation as drill 2 (drill 1 fixed
= 500-node pipeline).
**Notes:** Both drills are technical-round material, ASCII-whiteboard + narration format
mirroring STK-05 (CONTEXT D-13).

---

## Phone-screen logistics (work auth / relocation / comp)

| Option | Description | Selected |
|--------|-------------|----------|
| Work auth — Already US-authorized | Citizen/GC/existing visa | |
| Work auth — Eligible via TN (Canadian/Mexican citizen) | Fast, low-friction | ✓ |
| Work auth — Would need sponsorship | H-1B/other | |
| Work auth — Unsure/complex | Careful answer | |

**User's choice (work auth):** TN-eligible (Canadian citizen) — to be led as a positive selling point.

| Option | Description | Selected |
|--------|-------------|----------|
| Relocation — Willing to relocate to FL | Clear yes | (free-text, stronger) |
| Relocation — Open, negotiable | Flexible | |
| Relocation — Prefer remote | — | |
| Relocation — Not willing | — | |

**User's choice (relocation):** *"I want to relocate as fast as possible. I already checked the
place where I'm going to live. I want to live in Melbourne, Florida."* — script as eager,
zero-friction.

| Option | Description | Selected |
|--------|-------------|----------|
| Comp — Deflect to fit, stay flexible | Open/market-competitive | (blended) |
| Comp — State the posted range | Signal band alignment | (blended) |
| Comp — Anchor upper-half | Senior + PhD | (blended) |

**User's choice (comp):** *"Range seems ok, but highlight this is for a senior post. Most
important is to prove I'm the amazing long-term fit; once we establish that we can negotiate
the salary."* — acknowledge range, soft upper-half anchor, defer the number (CONTEXT D-05).

| Option | Description | Selected |
|--------|-------------|----------|
| Phone-screen-first, technical staged behind | Front SCREEN doc; 12 Qs + drills staged | ✓ |
| Two parallel packs, equal weight | SCREEN + TECHNICAL together | |
| One integrated set + plain-language layer | Single set + HR translation on top | |

**User's choice:** Phone-screen-first, technical staged behind (CONTEXT D-01/D-02).

---

## Rehearsal mechanism

| Option | Description | Selected |
|--------|-------------|----------|
| Flashcards + tracker + written protocol | Prompt→answer + timing/confidence tracker + how-to-rehearse guide | ✓ |
| Tracker only | Checklist/timing table | |
| Protocol only | How-to-rehearse guide, self-track | |

**User's choice:** Flashcards + tracker + written protocol (CONTEXT D-14).
**Notes:** User explicitly asked to be *guided how to rehearse*. Mirrors the Phase 4
`04-HUMAN-UAT.md` precedent; target times set per deliverable.

---

## Claude's Discretion

Exact filenames/slugs within `notes/`; section ordering; the exact pitch opening-hook wording;
which JD bullets get both question styles vs. one; the exact membership of the 12
differentiator-weighted questions; the plain-language analogies in the Layer-A "HR
translation" bridges; how richly STAR story 4 cross-links to the Phase 3 deck; tracker
target-time numbers.

## Deferred Ideas

- Deep technical-round (2–4) live drills (whiteboard coding, deeper EMT/digital-twin, real-
  framework Flower FL demo) — follow-on after the screen is secured.
- A live mock-interview role-play (Claude as interviewer over the bank) — a usage activity the
  tracker protocol enables, not a written deliverable here.
- Folding the phone-screen / STAR / bank material into the Phase 7 HTML study site — future.
