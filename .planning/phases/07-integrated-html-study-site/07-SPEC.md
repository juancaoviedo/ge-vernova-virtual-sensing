# Phase 7: Integrated HTML Study Site — Specification

**Created:** 2026-06-15
**Ambiguity score:** 0.15 (gate: ≤ 0.20)
**Requirements:** 7 locked

## Goal

Produce a single, self-contained, publish-ready **static HTML study site** that integrates everything produced so far — the AGMS architecture/patents research HTML, all Phase 1–5 Markdown study notes (converted to HTML), and natural-language explanations of the three hands-on demos — behind one hub page with consistent navigation, so Juan can revise all material in one place and later share an unlisted URL with interviewers.

## Background

The repo already contains a polished, consistent HTML design system in `.planning/research/` (GE Vernova green accent `#0b6e4f`, dark masthead, sticky TOC, `.card` sections, `.callout` and `.juan` bridge boxes). Three large research HTML docs exist and are excellent as-is:
- `.planning/research/patents/AGMS-architecture.html` (~60KB, Parts 0–11 walkthrough)
- `.planning/research/grid-operations-and-role.html` (~82KB, Appendices A–G)
- `.planning/research/patents/INDEX.html` (per-patent index)

Plus the AGMS architecture diagram in `.drawio/.svg/.png/.pdf` form.

What does **not** exist yet: a single entry point that ties these together with the ~15 study-note Markdown files, which currently live unconverted across phase folders:
- Phase 1 (`01-kalman-state-estimation/notes/`): KAL-01 WLS, KAL-02 Kalman family, KAL-03 IEEE 738 EKF
- Phase 2 (`02-transmission-virtual-sensing/notes/`): TVS-01 voltage stability, TVS-02 DC power-flow angle-WLS, TVS-03 observability/bad-data, TVS-04 asset health
- Phase 3 (`03-director-s-patents-deep-read/notes/`): AGMS patent rehearsal deck
- Phase 4 (`04-protocols-stack-architecture/notes/`): STK-01 protocol stack, STK-02 IEC 61850, STK-03 messaging/orchestration, STK-04 observability, STK-05 reference architecture
- Phase 5 (`05-federated-architectures-security/notes/`): FED-01 federated-vs-distributed, FED-02 byzantine robustness, FED-03 edge security

The notes are equation-dense and use LaTeX-style `$…$`/`$$…$$` math. Three demos exist, each with code + README (and result PNGs for two of them):
- `01-…/demo/` — EKF line-temperature estimator (`ekf_line_temp_demo.py`, `ekf_line_temp.png`)
- `02-…/demo/` — DC power-flow WLS + chi-squared bad-data detection (`dc_powerflow_baddata_demo.py`, `dc_powerflow_baddata.png`)
- `05-…/demo/` — NumPy FedAvg/FedProx/Krum/coord-median (`fedavg_fedprox_krum_demo.py`, text output)

## Requirements

1. **HTML-01 Hub landing page**: A single `index.html` entry point with consistent masthead + navigation linking to all three content areas (Architecture, Study Notes, Demos).
   - Current: No unifying entry point exists; the research HTML pages are standalone and the notes are unlinked Markdown
   - Target: `index.html` renders a hub with the existing design system, grouped navigation to every section/page below
   - Acceptance: Opening `index.html` shows a navigable hub; every link resolves to a real page in the site (no 404 / broken relative link)

2. **HTML-02 Architecture section integrated**: The AGMS architecture/patents research HTML is reachable from the hub, reusing the existing pages as-is (not rebuilt).
   - Current: `AGMS-architecture.html`, `grid-operations-and-role.html`, `patents/INDEX.html`, and the architecture diagram live only under `.planning/research/`
   - Target: These pages (and the AGMS architecture diagram, e.g. `.svg`/`.png`) are part of the published site and linked from the hub, with their internal cross-links still working
   - Acceptance: From the hub, each of the three architecture pages opens and renders; the AGMS architecture diagram displays; existing cross-page links between them still resolve within the site

3. **HTML-03 All Phase 1–5 notes converted to HTML**: Every Markdown note in the five phase `notes/` folders is rendered as an HTML page styled to match the existing design system.
   - Current: 15 notes exist only as Markdown; none are HTML
   - Target: Each note (KAL-01/02/03, TVS-01/02/03/04, AGMS deck, STK-01/02/03/04/05, FED-01/02/03) has a corresponding styled HTML page reachable from the hub
   - Acceptance: Every note file listed in Background has a rendered HTML page linked from the hub; spot-check confirms headings, tables, lists, and code blocks render correctly

4. **HTML-04 Offline math rendering**: Equations render correctly without internet, using a locally bundled MathJax.
   - Current: Notes contain `$…$`/`$$…$$` LaTeX that renders as raw text in plain HTML; no math engine bundled
   - Target: MathJax is vendored into the site folder and configured so `$…$`/`$$…$$` render as typeset math at `file://` with no network
   - Acceptance: With networking disabled, opening a math-heavy note (e.g. KAL-03 or TVS-02) shows typeset equations, not raw `$` source

5. **HTML-05 Demo sections (explain + embed key code + link results)**: Each of the three demos has a section giving a natural-language explanation (what it is, why it was built, what it shows), the core code/pseudocode embedded inline, and a link to its result artifact and source.
   - Current: Demos are reachable only as raw `.py` + `README.md` in phase folders
   - Target: A demos area (page or section) covers all three demos; each has a plain-language write-up, an inlined key code snippet (syntax-styled), a link to its result (PNG where present, text output otherwise), and a reference/link to the full source
   - Acceptance: All three demos appear; each shows explanation + at least one embedded code snippet + a working link to its result/source

6. **HTML-06 Self-contained & publish-ready**: The site is a self-contained folder that works offline by opening `index.html` (file://) AND is ready to deploy to a static host, with a short publish guide.
   - Current: No assembled site folder exists; content is scattered under `.planning/`
   - Target: One site folder containing all HTML, vendored MathJax, and referenced assets (diagrams, demo PNGs); plus a `PUBLISH.md` documenting how to deploy to a static host (e.g. GitHub Pages / Netlify)
   - Acceptance: The folder opens and navigates fully at `file://` with no server and no network; `PUBLISH.md` exists with concrete deploy steps; no link points outside the site folder for core content

7. **HTML-07 Unlisted-by-default**: The published site discourages search indexing so an unlisted URL can be shared without public discovery.
   - Current: N/A — no site
   - Target: Pages include `<meta name="robots" content="noindex,nofollow">` (and/or a `robots.txt` disallow) so the shared URL is not indexed
   - Acceptance: Site pages contain the noindex directive; `PUBLISH.md` notes the unlisted-URL sharing intent

## Boundaries

**In scope:**
- A hub `index.html` with consistent navigation
- Reuse (link, don't rebuild) of the three existing research HTML pages + AGMS architecture diagram
- Conversion of all 15 Phase 1–5 `notes/*.md` files into styled HTML pages
- Locally bundled (offline) MathJax for equation rendering
- A demos area: natural-language explanation + embedded key code/pseudocode + linked results/source for all three demos
- A self-contained, publish-ready static site folder + `PUBLISH.md` deploy guide
- `noindex` directive for unlisted sharing

**Out of scope:**
- Actual deployment to a live host — deferred to a follow-up once the host is chosen (user chose "publish-ready static, deploy later")
- A separate redacted/curated "share" build — user chose a single full build shared via unlisted URL; the `▶ Juan` bridge notes stay in
- Phase 0 (Document Ingestion) and Phase 6 (Synthesis) content — no notes exist yet; not blocking and excluded
- The IntelliGrid website mirror under `summaries/intelligrid-architecture/mirror/` — third-party page dump, not study notes
- A running web server / server-side features — static site only
- Re-authoring or fact-editing the note/research content — this phase converts and integrates, it does not rewrite the study material
- Executing or re-running the demos — explanation links to existing committed results

## Constraints

- **Offline-first:** Must render fully (including math) from `file://` with no network — MathJax bundled locally, all asset references relative and inside the site folder.
- **Static only:** No server process required to view or to publish.
- **Visual consistency:** New pages (hub, converted notes, demos) must match the existing design system (GE Vernova green `#0b6e4f`, masthead, sticky TOC, `.card`/`.callout`/`.juan` patterns) so the site reads as one document.
- **Non-destructive to sources:** The canonical Markdown notes and existing research HTML under `.planning/` remain the source of truth; the site is an assembled artifact, not a replacement.
- **Equation fidelity:** `$…$`/`$$…$$` LaTeX must render as typeset math (per the project's LaTeX-in-Markdown convention).

## Acceptance Criteria

- [ ] `index.html` opens and presents a navigable hub with Architecture, Study Notes, and Demos sections
- [ ] All three existing research HTML pages (AGMS architecture, grid-operations, patent index) and the AGMS diagram are reachable from the hub and render, with internal cross-links intact
- [ ] All 15 Phase 1–5 notes have corresponding styled HTML pages linked from the hub
- [ ] With networking disabled, a math-heavy note renders typeset equations (not raw `$` source) via bundled MathJax
- [ ] All three demos have a section with explanation + embedded key code + a working link to results/source
- [ ] The entire site navigates at `file://` with no server and no network (no broken/absent links for core content)
- [ ] A `PUBLISH.md` exists with concrete static-host deploy steps
- [ ] Pages carry a `noindex` directive for unlisted sharing

## Ambiguity Report

| Dimension          | Score | Min  | Status | Notes                                              |
|--------------------|-------|------|--------|----------------------------------------------------|
| Goal Clarity       | 0.90  | 0.75 | ✓      | Hub + linked pages; integrate everything           |
| Boundary Clarity   | 0.85  | 0.70 | ✓      | Explicit out-of-scope (deploy, redaction, mirror)  |
| Constraint Clarity | 0.80  | 0.65 | ✓      | Offline static, bundled MathJax, style match       |
| Acceptance Criteria| 0.82  | 0.70 | ✓      | 8 pass/fail checks                                 |
| **Ambiguity**      | 0.15  | ≤0.20| ✓      |                                                    |

Status: ✓ = met minimum, ⚠ = below minimum (planner treats as assumption)

## Interview Log

| Round | Perspective     | Question summary                          | Decision locked                                                        |
|-------|-----------------|-------------------------------------------|------------------------------------------------------------------------|
| 1     | Researcher      | Single file vs hub + linked pages?        | Hub + linked pages; reuse existing big HTML as-is                      |
| 1     | Boundary/Simpl. | Which content to include?                 | Everything — all Phase 1–5 notes + AGMS architecture/patents + demos   |
| 1     | Simplifier      | How deep should demo sections go?         | Natural explanation + embed key code/pseudocode + link results         |
| 2     | Constraint      | How should equations render?              | MathJax bundled offline                                                |
| 2     | Failure Analyst | How will the site be used?                | Publish + share with interviewers → static, publish-ready              |
| 3     | Boundary Keeper | Publishing approach?                       | Publish-ready static now; deploy later; include PUBLISH.md             |
| 3     | Failure Analyst | How public, given personal prep content?  | Full site, unlisted URL (noindex); no separate redacted build          |

---

*Phase: 07-integrated-html-study-site*
*Spec created: 2026-06-15*
*Next step: /gsd-discuss-phase 7 — implementation decisions (MD→HTML conversion approach, hub layout, folder structure, build/automation)*
