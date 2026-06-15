# Phase 3: Director's Patents Deep-Read - Context

**Gathered:** 2026-06-13
**Status:** Ready for planning

<domain>
## Phase Boundary

Produce **one interview-ready rehearsal deck** that distills the *already-completed*
deep-read research on director **Jamshid Sharif-Askary's** AGMS patent family into the
three things Juan must be able to deliver in the room (PAT-01/02/03):

- **PAT-01** — A 2–3 sentence summary of each patent identifying its core technical claim.
- **PAT-02** — One concrete connection per patent linking it to Juan's OSED / HEMS / SI-MAPPER work.
- **PAT-03** — One sharp, director-directed question per patent that demonstrates understanding and invites follow-on conversation.

**Scope correction (material change since roadmap/requirements were written):** ROADMAP.md
says "four patents (adaptive power, asset portfolio, data management, OCR)"; REQUIREMENTS.md
PAT-01 says "three." Both are **stale**. A 2026-06-13 quick task OCR'd three additional
patents; the research now covers **six distinct patents** in the Adaptive Grid Management
System (AGMS) family, all sole-invented by Sharif-Askary. **This phase treats all six**
(decision D-01). Notably, **Operation Loop Formation (US 12,596,341 B2) is GRANTED and
assigned to GE Vernova Infrastructure Technology LLC** — the hiring company's own IP and the
single strongest "I read your actual patent" talking point.

The deep *reading* is done (see canonical refs — INDEX.md, AGMS-architecture.md, six
per-patent files). **This phase is the rehearsal artifact, not re-reading.**

**Out of scope (belongs to other phases):** grid protocol stack / IEC 61850 / NATS-K3s-Prometheus
(Phase 4), federated architecture (Phase 5), and the aggregate vocabulary-bridge table +
STAR stories + timed mock-interview rehearsal loop (Phase 6). This phase produces the
patent rehearsal deck; Phase 6 aggregates and drills it.

</domain>

<decisions>
## Implementation Decisions

### Patent scope (PAT-01)
- **D-01:** **All six AGMS-family patents get the full summary + connection + question treatment.** The family: `adaptive-power` (WO 2023/064623, parent), `asset-portfolio` (WO 2024/211758), `data-management` (WO 2024/211800), `logistician-module` (US 2024/0337997), `operation-loop` (**US 12,596,341 B2 — GRANTED, GE Vernova**), `scout-command` (US 2024/0339835).
- **D-02:** The roadmap's "four patents (… OCR)" and REQUIREMENTS' "three" are superseded — `ocr.md` is the OCR'd duplicate of `data-management`, NOT a separate patent, and the AGMS continuations expand the set to six. Planner should treat six as authoritative and may note the requirement-text drift.

### Deliverable format (PAT-01/02/03)
- **D-03:** Produce **one consolidated rehearsal deck** (a single study doc), NOT per-patent files. One section per patent, each carrying: 2–3 sentence summary (the spoken track), the per-patent connection, and the director-directed question. This is the one artifact Juan rehearses from.
- **D-04:** The deck is a **NEW, rehearsal-focused** artifact distinct from the existing reference docs. Do **not** augment or bloat `INDEX.md` / `AGMS-architecture.md` — those remain the reference layer; the deck is the distilled performance layer that lifts from them.

### Ordering (PAT-01)
- **D-05:** Order the six patents in **pipeline / "assembly line" order**, matching the INDEX's formation pipeline: **Parent (adaptive-power) → Logistician → Asset Portfolio → Operation Loop Formation → Scout Command → Data Management.** This reinforces the master narrative and is the most memorable recall structure. (Data Management serves all stages, so it sits last as the cross-cutting layer.)

### Say-aloud / timed delivery (PAT-01)
- **D-06:** **No separate say-aloud block per patent.** The 2–3 sentence summary IS the spoken track for each patent (matches success criterion 1 exactly). Keeps the deck lean.
- **D-07:** Add **one ~90-second whole-family "walk the assembly line" pitch** at the deck level — the consolidated spoken narrative Juan can deliver if asked "what do you know about our patents?"

### Connection framing (PAT-02)
- **D-08:** **Both levels.** Each patent gets **one sharp standalone connection** (satisfies the criterion literally and lets Juan answer a narrow probe), AND the deck closes with the unified **"one assembly line = my stack"** master narrative (the power move). Source both from the INDEX's existing connection table + master narrative — refine for spoken delivery, don't invent new ones.

### Question framing (PAT-03)
- **D-09:** Director-directed questions are **architecture-level** — about design choices and tradeoffs (federation, island-mode/WAN-loss operation, edge deployment, simulate-before-commit as a system gate, the operational-index model) rather than narrowly quoting a specific claim number. Safer (no risk of misstating a claim) while still demonstrating genuine reading. Each question should invite a follow-on conversation, not be answerable yes/no.

### Claude's Discretion
- Exact deck section layout and any summary table-of-contents; precise wording of each summary, connection, and question; how heavily the deck cross-links back to `INDEX.md` for depth; whether the granted Operation Loop patent gets a brief visual flag (e.g., ★) to cue Juan to emphasize it. The ~90s family pitch may be lightly adapted from the INDEX's existing "interview master narrative."

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

ROADMAP.md declares no explicit "Canonical refs" line for Phase 3. The reading is already
done — the refs below are the completed research the deck distills, plus the source material.

### Completed patent research (the deck distills THESE — read first)
- `.planning/research/patents/INDEX.md` — **primary source.** Six-patent family map, formation pipeline, per-patent one-liners, the connection table (`How Juan Connects His Work`), the "interview master narrative," and the technical-terms cheat sheet. The deck is largely a distillation/refinement of this for spoken delivery.
- `.planning/research/patents/AGMS-architecture.md` — the extensive conceptual end-to-end walkthrough of the whole AGMS pattern; depth source behind the per-patent summaries.
- `.planning/research/patents/adaptive-power.md` — parent patent (WO 2023/064623 A1): full system architecture (GWM + GA + GWCH + Operating Cells + Scouts).
- `.planning/research/patents/asset-portfolio.md` — WO 2024/211758 A1: ORACS construct + 7 operational indexes; "are the assets fit" verification layer.
- `.planning/research/patents/data-management.md` — WO 2024/211800 A1: POV files, role-filtered data views, `ga-authenticationkey`.
- `.planning/research/patents/logistician-module.md` — US 2024/0337997 A1: Logistician Module (1023A); "which assets / assemble + procure + audit."
- `.planning/research/patents/operation-loop.md` — **US 12,596,341 B2 (GRANTED, GE Vernova).** Formation Construct Module (1400): match schema/DNA → per-asset meta objects → **simulate-before-commit (claim 3)** → execute. The keystone talking point.
- `.planning/research/patents/scout-command.md` — US 2024/0339835 A1: Scout Command (Liaison→Formation Processor→Incubator→Launch Manager); deploy role-typed scouts onto Field Agent Devices.

### Source PDFs (in `docs/`, only if a claim needs re-verification)
- `docs/patent-adaptive-power.pdf`, `docs/patent-asset-portfolio.pdf`, `docs/patent-data-management.pdf`, `docs/patent-logistician-module.pdf`, `docs/patent-operation-loop.pdf`, `docs/patent-scout-command.pdf` — the primary patents. (`docs/patent_ocr.pdf` was removed — it was the OCR duplicate of data-management.)

### Juan's background (source of every connection — PAT-02)
- `docs/Juan Carlos Oviedo Cepeda - 2026.pdf` — CV; source of the OSED / HEMS / SI-MAPPER / K3s / CVXPY-MPC / Databricks analogs used in each per-patent connection and the master narrative.
- `docs/job-requirements.md` — the JD; frames why these connections land for THIS role.

### Phase convention reference (deck style)
- `.planning/phases/02-distribution-virtual-sensing/02-CONTEXT.md` and the Phase 1/2 `notes/` artifacts — established oral-rehearsal style (For:/Purpose: header, say-aloud framing). Note the deck is a *single consolidated doc*, not the per-requirement `notes/` split used in Phases 1–2.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **`INDEX.md` connection table + master narrative** — already maps every AGMS component to Juan's work (Scout Incubator→K3s scheduling, Operation Loop simulate-before-commit→CVXPY MPC, Logistician→OSED FastAPI control plane, DNA-map→SI-MAPPER, POV files→OSED service layer, island-mode→OSED local buffering). The deck lifts and tightens these into spoken per-patent connections — no new connection research needed.
- **`INDEX.md` "interview master narrative"** — already a draft of the ~90s whole-family pitch (D-07). Refine for delivery rather than write from scratch.

### Established Patterns
- **Oral-rehearsal framing** (For:/Purpose: header, say-aloud talk-tracks) from Phases 1–2 notes. The deck adopts the spoken-delivery voice but as ONE consolidated doc (D-03), departing from the per-requirement `notes/` split.
- **No-LaTeX-needed:** this is a patents/architecture deck, not equation-dense — the project's LaTeX-in-markdown convention applies elsewhere; here prose + the pipeline structure carry it.

### Integration Points
- Deck feeds **Phase 6**: per-patent connections and the master narrative become raw material for the aggregate vocabulary-bridge table (BRG-01..03) and the OSED pitch. Keep connections in a form Phase 6 can lift directly.

</code_context>

<specifics>
## Specific Ideas

- The deck's spine is the **formation pipeline / "assembly line"**: Parent fires the context → Logistician decides *which* assets → Portfolio Manager *verifies* them (7 operational indexes) → Operation Loop Formation *assembles + simulates* the ORACS loop → Scout Command *deploys* the scouts → Data Management *serves POV views* throughout. The narrative payoff: "I've been building the components of this exact assembly line, in a different domain."
- **Emphasize the granted Operation Loop patent** as the keystone: it's GE Vernova's own IP and its *allowed claim 3* (simulate-before-commit) is the most literal analog to Juan's CVXPY MPC solve-before-commit gate.
- Questions should read as **peer-to-peer architecture curiosity** (e.g., how the system degrades to island-mode on WAN loss, how simulate-before-commit is bounded in time-critical formations, how the operational-index model trades off across asset classes), not exam questions.

</specifics>

<deferred>
## Deferred Ideas

- **Aggregate vocabulary-bridge table** (AGMS term → Juan's-work analog → pivot sentence) — **Phase 6** (BRG-01..03). Per-patent connections here feed it.
- **OSED 10-minute pitch in GE Vernova language** and **STAR stories** — **Phase 6**.
- **Timed mock-interview rehearsal / Q&A drill loop** — **Phase 6**. This phase writes the deck; Phase 6 rehearses it under pressure.
- **Deep protocol/federated treatment** triggered by patent content (e.g., federated edge transaction manager internals) — **Phases 4 & 5**; reference at awareness level only here.

None — discussion stayed within phase scope.

</deferred>

---

*Phase: 3-Director's Patents Deep-Read*
*Context gathered: 2026-06-13*
