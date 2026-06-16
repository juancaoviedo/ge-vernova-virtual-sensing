---
phase: quick-260616-lmr
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md
autonomous: true
requirements: [QUICK-260616-lmr]

must_haves:
  truths:
    - "Every section of 260616-lmr-SOURCE.md appears in the output, transformed into scannable bullet points in Juan's own voice (no prose-paragraph dumps, no invented claims)."
    - "The five behavioral stories are STAR/HERO-structured: each leads with a Headline/Hook, then Situation, Task, Action, Result (mirroring Juan's own 'fail' story format)."
    - "The four BLANK questions (why-hire-you/different/impact, time-management, ethical conflict, Ingenium UIS teamwork) and the trailing disagreements sentence are filled with clearly-marked [DRAFT — refine] scaffolds drawn only from Juan's existing material."
    - "The JD anchor callout (Kalman filters / state estimation -> 'Juan does state estimation daily') is present and tied into the fit/role answers."
    - "The file opens with the established For:/Purpose: header, stays jargon-light (HR screen voice), and cross-links the three sibling notes (PHONE-SCREEN.md, STAR-STORIES.md, REHEARSAL-TRACKER.md) as relative links, positioning itself as the own-voice complement -- not a duplicate."
  artifacts:
    - path: ".planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md"
      provides: "Juan's own-voice, bullet-point, STAR/HERO-structured HR phone-screen answer bank transformed from his verbatim braindump"
      min_lines: 180
      contains: "**For:**"
  key_links:
    - from: ".planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md"
      to: "PHONE-SCREEN.md"
      via: "relative markdown link (sibling note in same notes/ dir)"
      pattern: "\\(PHONE-SCREEN\\.md\\)"
    - from: ".planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md"
      to: "STAR-STORIES.md"
      via: "relative markdown link"
      pattern: "\\(STAR-STORIES\\.md\\)"
    - from: ".planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md"
      to: "REHEARSAL-TRACKER.md"
      via: "relative markdown link"
      pattern: "\\(REHEARSAL-TRACKER\\.md\\)"
---

<objective>
Author `notes/PHONE-SCREEN-ANSWERS.md` -- Juan's OWN-VOICE HR phone-screen answer bank. Transform his verbatim braindump (`260616-lmr-SOURCE.md`) into a polished, scannable, STAR/HERO-structured study note: every section converted to rehearsable bullet points in his own phrasing, behavioral stories restructured around a Headline + Situation/Task/Action/Result, BLANK questions filled with clearly-flagged DRAFT scaffolds drawn only from his existing material, and the whole file positioned as the own-voice complement to the already-generated `PHONE-SCREEN.md` companion pack.

Purpose: The companion `PHONE-SCREEN.md` gives Juan a polished recruiter-facing script in a neutral voice. This file gives Juan answers in HIS voice and phrasing -- so what he rehearses sounds like him, not like a generated script he has to fake. It is the bridge between his raw braindump and a deliverable he can actually say aloud.

Output: One Markdown file: `.planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md`.
</objective>

<execution_context>
@$HOME/.claude/get-shit-done/workflows/execute-plan.md
</execution_context>

<context>
@.planning/quick/260616-lmr-author-phone-screen-own-voice-answer-ban/260616-lmr-SOURCE.md

# Style + section-set reference (the established phone-screen note -- DO NOT duplicate it; complement it)
@.planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN.md

# STAR structure + cross-link target
@.planning/phases/06-synthesis-drills-mock-interview/notes/STAR-STORIES.md

# Cross-link target (rehearsal index)
@.planning/phases/06-synthesis-drills-mock-interview/notes/REHEARSAL-TRACKER.md

<authoring_rules>
<!-- The executor MUST honor these. They encode the quick-task constraints. -->

1. SINGLE FILE deliverable: `.planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md`.
   NOT in the quick dir -- it belongs in the Phase 6 study-note set alongside its siblings.

2. PRESERVE JUAN'S VOICE. Transform his sentences into bullets, tighten, structure -- but keep his
   phrasing and his metaphors ("not who is right but what is right"; "strong opinions loosely held";
   "consult, not audition"; "the interesting version"). Do NOT rewrite him into corporate-speak.
   Do NOT invent new claims, metrics, or stories beyond what is in SOURCE.md or already established
   in the Phase 6 sibling notes.

3. BULLETS, NOT PROSE. Every section becomes scannable, rehearsable bullet points -- not the wall-of-text
   paragraphs in his braindump. He must be able to glance and recall under phone pressure.

4. JARGON-LIGHT. This is the non-technical HR screen. Plain language, outcomes over architecture.
   No equations, no acronym soup. (Technical depth lives in QUESTION-BANK.md / STAR-STORIES.md
   Technical STAR versions -- cross-reference those, do not reproduce them here.)

5. DRAFTS ARE FLAGGED. Anything Juan left blank or trailing, and anything you scaffold for him, must be
   marked literally `[DRAFT — refine]` (em dash) so he knows to own it. Scaffolds draw ONLY from his
   existing material (this SOURCE file + the Phase 6 sibling notes), never from new invention.

6. COMPLEMENT, DON'T DUPLICATE. Where `PHONE-SCREEN.md` already has a polished version (e.g. work-auth/TN,
   salary, relocation, notice period, the full say-aloud arc), cross-reference it rather than rewriting it.
   This file is the own-voice answer bank for the conversational questions in Juan's braindump.
</authoring_rules>
</context>

<tasks>

<task type="auto">
  <name>Task 1: Header + framing + the conversational Q&A sections (own-voice bullets)</name>
  <files>.planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md</files>
  <action>
Create the file and write the top + the non-behavioral conversational answers, all as scannable bullets in Juan's voice.

**Header (mirror the sibling style -- `**For:**` / `**Purpose:**` lines, NOT YAML frontmatter):**
- `**For:**` -- Round-1 HR phone screen, in Juan's OWN voice (the own-voice complement to PHONE-SCREEN.md).
- `**Purpose:**` -- One line: this is Juan's verbatim braindump (260616-lmr-SOURCE.md) transformed into rehearsable, STAR-structured bullets that sound like him; pair it with PHONE-SCREEN.md (polished recruiter script), STAR-STORIES.md (technical STAR depth), and REHEARSAL-TRACKER.md (timed practice).
- A short blockquote orientation note: jargon-light, HR-screen voice; technical depth lives in the sibling notes; anything marked `[DRAFT — refine]` is a scaffold for Juan to finish in his own words.

**JD anchor callout** (place it high, right after the header, as a callout/blockquote) -- per SOURCE "JD anchor":
- Quote: "Apply control theory and signal processing techniques (e.g., Kalman filters, state estimation) to refine virtual sensor accuracy."
- One line: Juan does state estimation daily -- weave this into the why-this-role / why-hire-you answers (plain language: "the math this role names is the math I use every day").

**Then convert these SOURCE sections to bullet points, in this order, each as its own `##` section, IN JUAN'S VOICE:**
- **Framing** ("Consult, not audition" -- how can we together define if I'm a good fit; STAR = just a history; "Accomplished X, measured by Y, while doing Z"; Jamshid Sharif-Askary / Electrification Innovation Lab). Short framing-mindset block.
- **Opening rapport script** -- the Jamshid / 6-patents / AGMS hook + the Vera / Claudia Blanco CTO-org hook. Beat-by-beat script he can follow (bullets, but preserve the conversational flow and his actual lines).
- **Tell me about yourself (the "interesting version")** -- bullets: offer the choice (CV recap vs interesting version); proudly Colombian/Latino, ~10 yrs in Canada, Canadian citizen; 6 yrs Hydro-Quebec at the client<->grid interface owning full stack cloud-to-edge; daily state estimation, ML, distributed computing, cloud-edge orchestration, multi-protocol comms; lately reasoning engines with AI for autonomous buildings+grid; owns projects end-to-end, delivers fast; the startup-style / create-value-fast pull from the JD.
- **Walk me through your resume** -- bullets: PhD EE, 9 yrs research, 5 yrs HQ on DER control programs; full-stack contributions (IoT, comms protocols, control, state estimation, ML); latest = HVAC of big buildings responsive to grid needs via structured knowledge DBs for agentic AI + reasoning engines for autonomous demand response; end-to-end ownership, deliver fast.
- **Why should we hire you / great fit?** -- BLANK in SOURCE. Provide a `[DRAFT — refine]` scaffold built ONLY from his own established material: end-to-end full-stack cloud-to-edge ownership; does state estimation daily (tie to JD anchor); studied the 6 patents / understands AGMS; startup-style fast delivery; worldwide-impact motivation. Bullet it; flag clearly as a draft for Juan to own.
- **Why work for GE?** -- bullets: follows Vera Silva (CTO) on LinkedIn; met Claudia Blanco at a conference in Europe (now AI lead); knows Joshua Wong (OpusOne founder, early GridOS); knows GE Vernova as a worldwide leader; wants a role with worldwide impact; "natural next step."
- **Why this specific role?** -- bullets: studied Jamshid's 6 patents; wants to build the grid of the future; can help with distributed control, orchestration, cloud-edge infra, the learning engine, the scouts' deployment. (Tie the JD anchor here too.)
- **Where do you see yourself in 5 years?** -- bullets: in Melbourne, FL, at the Electrification Innovation Lab; expert at the intersection of physics, AI, distributed computing; AGMS deployed as a commercial product (real customers, not a pilot).
- **Why looking for a new opportunity?** -- bullets: learned a lot, ready for a new challenge; the "few moments I felt I can do more" arc (PhD -> moved to Canada -> now an org with worldwide impact); certain he can add long-term value.
- **Why leave Hydro-Quebec?** -- bullets, forward-framed: HQ is amazing, respected there, real influence in a reduced area (Quebec); now seeking bigger impact; "not that I want to leave, it's that I'm certain I can create more value." NOTE: cross-reference PHONE-SCREEN.md §3 for the polished forward-frame version (do not duplicate it).
- **Current manager** -- bullets: smooth; the "not about who is right, but what is right" quote; wants to bring that mentality to the new team.
- **Hobbies** -- bullets: building/architecting things -- mobile apps, web apps, IoT home control, blockchain experiments, building a house on a farm in Colombia (designed the architecture + electrical/water plans); software AND engineering architecture.
- **Handling stress** -- bullets: rarely stressed; last time = two projects on a tight deadline; what he did (discuss with team, reorganize priorities, redistribute load, extend hours); result (both delivered on time, near-zero scope reduction).
- **How do you collaborate?** -- bullets: flexible, sync OR async; sync = meetings/brainstorm/workshops; async = email, git commits, Slack/Discord.
- **Handling disagreements** -- bullets: "strong opinions loosely held" (support what I believe; if proven wrong, no problem adopting the new view). The SOURCE sentence trails off ("Therefore, ..."). Finish it as a `[DRAFT — refine]` scaffold consistent with his voice -- e.g. "...therefore I keep the discussion about what's right, not who's right, and I update fast when the evidence changes." Flag it clearly as a draft.
- **Job title clarification** -- bullets: Scientific researcher = some research / data science / data engineering, but mostly software development.
- **How do you prioritize?** -- bullets: Eisenhower matrix; bias toward long-term-value work first while keeping the urgent under control.
- **Best time-management strategies** -- BLANK in SOURCE. Provide a `[DRAFT — refine]` scaffold from his own material ONLY: Eisenhower matrix (from the prioritization answer) + the stress-handling tactics (reorganize priorities, redistribute load, timebox) + end-to-end ownership focus. Flag clearly as a draft.

Write all of this as clean bullets. Preserve his phrasing. Do NOT add new claims.
  </action>
  <verify>
    <automated>test -f .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -q '\*\*For:\*\*' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -q '\*\*Purpose:\*\*' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -q 'Kalman filters, state estimation' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -q 'who is right' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -q 'strong opinions loosely held' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -q 'Eisenhower' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md</automated>
  </verify>
  <done>Header (For:/Purpose:), JD-anchor callout, and all 18 conversational SOURCE sections present as own-voice bullets; the two BLANK questions in this group (why-hire-you, time-management) and the trailing disagreements sentence carry `[DRAFT — refine]` scaffolds drawn only from Juan's material.</done>
</task>

<task type="auto">
  <name>Task 2: The five behavioral stories in STAR/HERO structure (Headline + S/T/A/R)</name>
  <files>.planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md</files>
  <action>
Append a `## Behavioral Stories (STAR / HERO)` section. Lead it with a one-line note: each story leads with a **Headline/Hook**, then **Situation, Task, Action, Result** -- mirroring Juan's own "fail" story which already uses Headline/Situation/Action/Outcome. Keep these jargon-light (HR-screen voice); for technical depth, cross-link `STAR-STORIES.md` (do not reproduce its Technical STAR versions).

Restructure each SOURCE behavioral entry into a labeled STAR/HERO block (use bold field labels: **Headline:**, **Situation:**, **Task:**, **Action:**, **Result:**). Preserve Juan's phrasing.

1. **Leadership / Initiative -- Open source -> Linux Foundation Energy** (SOURCE "show leadership/initiative"):
   - Headline: brought open-source from zero to HQ becoming the first North American utility in Linux Foundation Energy.
   - Situation: open-source dev was non-existent at HQ when he joined.
   - Task/Action: talked to his manager, presented the value to colleagues / research-center director / IT director; presented his cloud-edge DER-coordination work at a Linux Foundation conference; converted the manager into an ally.
   - Result: HQ entered Linux Foundation Energy, first utility in North America to do so. Tie the closing line: the manager got most of the credit -- "not who is right but what is right" (this is the humble-leadership beat; keep it).

2. **Failure / Resilience -- 3-yr project closed -> repackaged to open-source libs -> HEMS foundation** (SOURCE "time you fail"):
   - This one is ALREADY in Headline/Situation/Action/Outcome form in SOURCE. Keep his structure verbatim-faithful; relabel "Outcome" as **Result** for consistency (or keep Outcome and note it's the R in STAR). Headline: 3+ years on a project he loved, closed without real-world impact. Situation: the dream DER-orchestration project (price signals, markets, cloud-edge, IoT, ML); built almost everything from scratch; not the PM but still felt like failure because the work felt wasted. Action: repackaged the code into smaller functional blocks, transferred them to other projects, eventually published as open-source on HQ's official repo. Result: those packages are still used elsewhere and are now the mathematical foundation for the internal HEMS being built.

3. **Biggest achievement -- writing skills / Stanford course** (SOURCE "biggest achievement"):
   - Headline: turned "all possible writing mistakes" into publishing in internationally recognized journals.
   - Situation: PhD supervisor said his first written piece made every error possible.
   - Action: took a Stanford technical-writing course; even started writing a book to practice.
   - Result: published in internationally recognized journals; supervisor noted his writing was very good by the end -- "and that was before ChatGPT" (keep this line, it's his).

4. **Teamwork -- Ingenium UIS** (SOURCE = pointer only "Ingenium UIS. [pointer — to expand]"):
   - This is a POINTER, not content. Build a `[DRAFT — refine]` STAR scaffold and clearly mark it as a draft Juan must fill from his own memory. Provide the empty STAR skeleton (Headline / Situation / Task / Action / Result) with bracketed prompts describing what to put in each (a team with disparate goals / people he didn't know, brought together around a shared objective at Ingenium UIS). Do NOT invent specifics -- leave bracketed `[DRAFT — refine: ...]` prompts so Juan supplies the real details.

5. **Persuade someone more senior -- Open source (same Linux Foundation story)** (SOURCE "persuade someone more senior"):
   - This points to the SAME Linux Foundation Energy story as #1. Do NOT rewrite the whole story -- add a short cross-reference block: "Use the Leadership/Initiative story above, framed as persuasion: the senior people I convinced were my manager, the research-center director, and the IT director." One or two bullets on the persuasion angle (strong evidence + a conference demo turned skeptics into allies). Point back to story #1 in this same file.

Keep every story HR-screen length and jargon-light. Cross-link STAR-STORIES.md for the technical-round versions.
  </action>
  <verify>
    <automated>grep -q 'STAR / HERO\|STAR/HERO' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -qc '\*\*Headline:\*\*' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -q '\*\*Situation:\*\*' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -q '\*\*Action:\*\*' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -q '\*\*Result:\*\*' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -q 'Linux Foundation' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -q 'Ingenium UIS' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -q 'HEMS' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -q 'Stanford' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && [ "$(grep -c '\*\*Headline:\*\*' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md)" -ge 3 ]</automated>
  </verify>
  <done>Five behavioral stories present: three fully restructured (leadership/open-source, failure/resilience, biggest achievement) each with Headline + S/T/A/R labels; Ingenium UIS teamwork is a clearly-flagged `[DRAFT — refine]` STAR skeleton; persuade-senior is a cross-reference to the open-source story (no duplication). Each story is jargon-light and cross-links STAR-STORIES.md for technical depth.</done>
</task>

<task type="auto">
  <name>Task 3: Ethical-conflict draft, questions-for-us, closing/nudge scripts, JD-anchor weave, cross-links</name>
  <files>.planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md</files>
  <action>
Append the remaining SOURCE sections and the cross-link footer.

1. **Ethical / moral conflict** (SOURCE = BLANK):
   - Provide a `[DRAFT — refine]` scaffold drawn ONLY from Juan's established material/values. Use his "not who is right but what is right" principle and "strong opinions loosely held" as the ethical-stance frame, and leave a bracketed STAR skeleton for him to supply a real example (`[DRAFT — refine: situation where he saw/handled something unethical]`). Do NOT invent a fabricated incident -- give the values frame + an empty STAR slot he fills himself.

2. **Do you have questions for us?** (SOURCE "Do you have questions for us?"):
   - Convert his list to clean bullets, preserving his questions: How is working for GE? / Why is this position open? / What does success look like in the first 90 days? / How could I exceed expectations in the first six months? / What's the immediate challenge after I'm accepted? / If I want to hit the ground running, what should I start on first?
   - Keep his "recapitulate" closing question as a highlighted line: it sounds like you're at a critical point where you need to add the virtual-sensing module to the AGMS to start proof-of-concept tests; if I started next week I'd focus on --- does that align with what you're envisioning? (This is where the JD anchor pays off -- add a one-line note tying it to "state estimation / virtual sensing is what I do daily.")

3. **Closing -- next steps + polite nudge** (SOURCE "Closing"):
   - Bullets, preserving his scripts: "I've enjoyed our conversation -- before I go, what are the next steps and when should I expect an update?" then "[whatever time they said]: perfect -- and if I don't hear by then, is it okay if I give you a polite nudge?"

4. **JD-anchor weave reminder** -- add a short closing callout reminding Juan to thread the state-estimation / virtual-sensing JD line into the why-hire-you, why-this-role, and the "recapitulate" question. (Reinforces the anchor placed in Task 1.)

5. **Cross-links footer** -- add a `## Related notes` (or `## See also`) section with relative markdown links to the three siblings, each with a one-line "what it's for" so Juan knows when to reach for each:
   - `[PHONE-SCREEN.md](PHONE-SCREEN.md)` -- the polished recruiter-facing script + full timed say-aloud arc (this file is its own-voice complement).
   - `[STAR-STORIES.md](STAR-STORIES.md)` -- the four pressure-tested stories with Technical STAR depth + JD-line mapping for rounds 2-4.
   - `[REHEARSAL-TRACKER.md](REHEARSAL-TRACKER.md)` -- the timed, spaced-repetition practice tracker; rehearse these answers aloud against it.
   - One framing line: "This file = Juan's own words. PHONE-SCREEN.md = the polished script. Use this to make the polished version sound like you."

Keep everything jargon-light and in his voice.
  </action>
  <verify>
    <automated>grep -q '(PHONE-SCREEN.md)' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -q '(STAR-STORIES.md)' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -q '(REHEARSAL-TRACKER.md)' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -qi 'polite nudge' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -qi 'next steps' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -qi 'questions for us\|Do you have questions' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && grep -qi 'ethical' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md && [ "$(grep -c '\[DRAFT — refine' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md)" -ge 4 ] && [ "$(wc -l < .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md)" -ge 180 ]</automated>
  </verify>
  <done>Ethical-conflict `[DRAFT — refine]` values-frame + empty STAR slot present; questions-for-us and closing/nudge scripts converted to own-voice bullets; JD-anchor weave reminder present; `## Related notes` footer cross-links all three siblings as relative links with usage notes. At least 4 `[DRAFT — refine]` flags total across the file; file >= 180 lines.</done>
</task>

</tasks>

<verification>
After all tasks, confirm against the must_haves:
- All 4 source artifact requirements covered: every SOURCE section transformed to bullets; 5 STAR/HERO stories; 4 BLANK questions + trailing sentence drafted-and-flagged; JD anchor present and woven.
- File lives at `.planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md` (Phase 6 note set), NOT the quick dir.
- Opens with `**For:**` / `**Purpose:**`; jargon-light throughout (no equations, no acronym soup).
- Relative links to PHONE-SCREEN.md, STAR-STORIES.md, REHEARSAL-TRACKER.md all present.
- No invented claims beyond SOURCE + Phase 6 sibling material; every scaffolded/blank item is marked `[DRAFT — refine]`.

Grep-verifiable acceptance (run after Task 3):
```
test -f .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md
grep -c '\[DRAFT — refine' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md   # >= 4
grep -c '\*\*Headline:\*\*' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md  # >= 3
grep -E '\(PHONE-SCREEN\.md\)|\(STAR-STORIES\.md\)|\(REHEARSAL-TRACKER\.md\)' .planning/phases/06-synthesis-drills-mock-interview/notes/PHONE-SCREEN-ANSWERS.md
```
</verification>

<success_criteria>
- ONE markdown file authored at the Phase 6 notes path, in Juan's own voice, fully bulletized.
- Every SOURCE section present; nothing dropped, nothing invented.
- Five behavioral stories in Headline + STAR/HERO form; the three with content fully written, the two pointers (Ingenium UIS teamwork, persuade-senior) handled (draft skeleton / cross-reference).
- Four BLANK questions + the trailing disagreements sentence filled with clearly-flagged `[DRAFT — refine]` scaffolds drawn only from Juan's material.
- JD anchor callout present and threaded into the fit/role answers.
- For:/Purpose: header; jargon-light; relative cross-links to the three sibling notes positioning this as the own-voice complement.
</success_criteria>

<output>
After completion, create `.planning/quick/260616-lmr-author-phone-screen-own-voice-answer-ban/260616-lmr-SUMMARY.md` capturing: file path produced, sections transformed, which items were drafted/flagged, and the cross-links added.
</output>
