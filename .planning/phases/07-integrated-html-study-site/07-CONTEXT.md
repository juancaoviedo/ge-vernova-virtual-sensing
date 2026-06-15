# Phase 7: Integrated HTML Study Site - Context

**Gathered:** 2026-06-15
**Status:** Ready for planning

<domain>
## Phase Boundary

Assemble a single, self-contained, publish-ready static HTML study site that integrates the existing AGMS architecture/patents research HTML, all Phase 1–5 Markdown study notes (converted to HTML), and natural-language explanations of the three hands-on demos — behind one hub page with consistent navigation. The site lives in `/docs` (GitHub Pages-ready), works offline, and is shareable via an unlisted URL.

</domain>

<spec_lock>
## Requirements (locked via SPEC.md)

**7 requirements are locked.** See `07-SPEC.md` for full requirements, boundaries, and acceptance criteria.

Downstream agents MUST read `07-SPEC.md` before planning or implementing. Requirements are not duplicated here.

**In scope (from SPEC.md):**
- A hub `index.html` with consistent navigation
- Reuse (link, don't rebuild) of the three existing research HTML pages + AGMS architecture diagram
- Conversion of all 15 Phase 1–5 `notes/*.md` files into styled HTML pages
- Locally bundled (offline) MathJax for equation rendering
- A demos area: natural-language explanation + embedded key code/pseudocode + linked results/source for all three demos
- A self-contained, publish-ready static site folder + `PUBLISH.md` deploy guide
- `noindex` directive for unlisted sharing

**Out of scope (from SPEC.md):**
- Actual deployment to a live host (deferred — deploy later)
- A separate redacted/curated "share" build (single full build, unlisted URL)
- Phase 0 / Phase 6 content (no notes exist yet)
- The IntelliGrid website mirror under `summaries/intelligrid-architecture/mirror/`
- A running web server / server-side features
- Re-authoring or fact-editing note/research content
- Executing or re-running the demos (link to existing committed results)

</spec_lock>

<decisions>
## Implementation Decisions

### Build approach
- **D-01:** Convert the 15 Markdown notes to HTML with a **reproducible Python build script** (`python-markdown` + `pygments` + bundled MathJax), not hand-authored pages or an SSG/pandoc. The script reads `notes/*.md` from each phase folder and emits styled HTML pages sharing one CSS. Re-runnable when notes change.
- **D-02:** `pygments` (2.17.2) is already installed; `python-markdown` is NOT installed and must be added (one `pip install`, can reuse the existing `.venv-crawl` or a fresh venv — planner's discretion). `pandoc` is not installed and is not to be used.
- **D-03:** The script must extract/preserve the canonical CSS design system from the existing research HTML (GE Vernova green `#0b6e4f`, dark masthead, sticky TOC, `.card`/`.callout`/`.juan` patterns) into a shared stylesheet so converted notes match the existing pages visually.

### Site location & publishing
- **D-04:** The site is built **into the existing `/docs` folder** (kept as-is — do NOT rename it). Rationale: the user reconsidered the `/docs`→`/data` rename; keeping `/docs` (a) preserves the ~30 existing `docs/...` references across notes/research (no breakage) and (b) places the source PDFs inside the published site so links resolve.
- **D-05:** Site structure inside `/docs`: hub `index.html` at `/docs/index.html`, plus subfolders `architecture/`, `notes/`, `demos/`, and `vendor/mathjax/`. Existing source PDFs remain at `/docs/*.pdf`.
- **D-06:** Publishing target is **GitHub Pages from `/docs`** (zero-config: Settings → Pages → /docs). Provide a `PUBLISH.md` (`/docs/PUBLISH.md` or repo root — planner's discretion) with concrete deploy steps and the unlisted/`noindex` note. Actual deployment is deferred (out of scope this phase).

### Existing research HTML integration
- **D-07:** **Copy** the three existing research HTML pages — `AGMS-architecture.html`, `grid-operations-and-role.html`, `INDEX.html` — plus the AGMS architecture diagram (`AGMS-architecture.svg`/`.png`) into the site (`/docs/architecture/`), preserving their relative cross-links between each other. Do not rebuild them.
- **D-08:** Fix the patent-PDF links inside the copied `INDEX.html` so they resolve to the PDFs at `/docs/*.pdf` via correct relative paths (e.g. `../patent-adaptive-power.pdf` from `/docs/architecture/`). Source PDFs are served from within `/docs` (D-04), so links stay local — no external Google Patents rewrite needed.

### Hub & navigation design
- **D-09:** Hub landing page is a **card-grid** organized into three groups — Architecture / Study Notes / Demos — each card linking to a page. Each individual content page keeps its own **sticky sidebar TOC** (matching the existing research pages).

### Demo presentation
- **D-10:** Embed demo **result images inline with a short caption**: `ekf_line_temp.png` (Phase 1) and `dc_powerflow_baddata.png` (Phase 2). The Phase 5 federated demo has no PNG — render its key numeric output (FedAvg/FedProx/Krum/median error contrast) as a table or code block.
- **D-11:** Embed **key functions only** (e.g. EKF predict/update, WLS normal-equations solve, FedAvg/Krum aggregation) — not whole files — highlighted **at build time with pygments** (offline, no runtime JS). Link to the full source `.py` for each demo.
- **D-12:** Each demo section gives a natural-language explanation: what it is, why it was built (which interview gap it closes), and what it demonstrates — sourced from the existing demo `README.md` files.

### Math rendering
- **D-13:** Bundle **MathJax locally** under `/docs/vendor/mathjax/` (tex-chtml or equivalent) configured for `$…$`/`$$…$$` delimiters, so equation-dense notes render typeset math at `file://` with no network.

### Claude's Discretion
- Exact venv strategy for `python-markdown` (reuse `.venv-crawl` vs. new venv).
- Precise MathJax component/version and config object.
- File-naming scheme for converted note pages (e.g. `notes/kal-01-wls.html`).
- Whether `PUBLISH.md` lives at repo root or `/docs/`.
- Per-page footer "back to hub" / prev-next navigation niceties.
- How the shared CSS is delivered (single `assets/site.css` vs. inlined) — single external stylesheet preferred for maintainability.

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Locked requirements (read first)
- `.planning/phases/07-integrated-html-study-site/07-SPEC.md` — Locked requirements, boundaries, acceptance criteria — MUST read before planning.

### Existing HTML to reuse (design system + content to copy)
- `.planning/research/patents/AGMS-architecture.html` — AGMS architecture walkthrough (Parts 0–11); canonical design system reference (CSS variables, masthead, TOC, `.juan` callouts).
- `.planning/research/grid-operations-and-role.html` — Grid-ops/role companion (Appendices A–G); cross-links to the AGMS walkthrough.
- `.planning/research/patents/INDEX.html` — Per-patent index; links to source PDFs in `docs/` (links need relative-path fix per D-08).
- `.planning/research/patents/AGMS-architecture.svg` / `.png` — AGMS architecture diagram assets.

### Study notes to convert (15 files)
- `.planning/phases/01-kalman-state-estimation/notes/` — KAL-01 (WLS), KAL-02 (Kalman family), KAL-03 (IEEE 738 EKF).
- `.planning/phases/02-distribution-virtual-sensing/notes/` — TVS-01..04 (voltage stability, DC power-flow angle-WLS, observability/bad-data, asset health).
- `.planning/phases/03-director-s-patents-deep-read/notes/AGMS-patent-rehearsal-deck.md` — AGMS patent rehearsal deck.
- `.planning/phases/04-protocols-stack-architecture/notes/` — STK-01..05 (protocol stack, IEC 61850, messaging/orchestration, observability, reference architecture).
- `.planning/phases/05-federated-architectures-security/notes/` — FED-01..03 (federated-vs-distributed, byzantine robustness, edge security).

### Demos (explanation source + code + results)
- `.planning/phases/01-kalman-state-estimation/demo/` — `ekf_line_temp_demo.py`, `ekf_line_temp.png`, `README.md`.
- `.planning/phases/02-distribution-virtual-sensing/demo/` — `dc_powerflow_baddata_demo.py`, `dc_powerflow_baddata.png`, `README.md`.
- `.planning/phases/05-federated-architectures-security/demo/` — `fedavg_fedprox_krum_demo.py`, `README.md` (text output, no PNG).

### Publish target
- `docs/` — existing folder containing source PDFs (six patents, `IEC 61850-3.pdf`, `intelligrid.pdf`, CV, `job-requirements.md`); the site is built INTO this folder; GitHub Pages serves it.

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **Hand-authored research HTML design system** (`AGMS-architecture.html` et al.): a complete, polished CSS theme (CSS custom properties, masthead gradient, sticky `nav.toc`, `section.card`, `.callout`, `.juan` bridge boxes). Extract once into a shared stylesheet — do NOT reinvent.
- **`pygments` 2.17.2** (installed): build-time syntax highlighting for embedded demo code; can emit a CSS class set + highlighted HTML.
- **Demo `README.md` files**: ready-made source for each demo's "what/why/what-it-shows" narrative.
- **`.venv-crawl`** (existing virtualenv with bs4): candidate environment for adding `python-markdown`.
- **`summaries/intelligrid-architecture/convert_to_markdown.py`**: an HTML→MD converter (opposite direction) — reference only, not reused.

### Established Patterns
- Notes use LaTeX-style `$…$`/`$$…$$` math (per project convention) → requires MathJax at render time (D-13).
- Existing research HTML uses relative cross-links between sibling files → preserve by copying the trio together (D-07).

### Integration Points
- Source PDFs already in `/docs/*.pdf` → site links resolve locally once site is built into `/docs` (D-04, D-08).
- ~30 `docs/...` references across `.planning/` remain valid because `/docs` is NOT renamed.

</code_context>

<specifics>
## Specific Ideas

- "Easier to study" is the north star: one entry point, see results/equations without clicking out, consistent look across patents + notes + demos.
- Reuse the existing GE Vernova-styled research pages as-is rather than rebuilding — the design is already strong.
- Build it into `/docs` so the source PDFs and the site coexist and links just work.

</specifics>

<deferred>
## Deferred Ideas

- **Actual deployment** to GitHub Pages (enable Pages → /docs, get the unlisted URL) — deferred to a post-build step per SPEC.md ("deploy later").
- **Privacy decision at deploy time:** publishing `/docs` makes the six patent PDFs and the CV publicly fetchable at the site URL. Patents are public record and the site is `noindex`/unlisted, but confirm this is acceptable (or move sensitive PDFs out of the served path) before actually deploying. Recorded as a conscious deploy-time choice, not a build blocker.
- **Curated/redacted "share" build** (stripping `▶ Juan` personal bridge notes) — explicitly rejected for now (single full build, unlisted URL); could revisit if sharing more widely.
- Phase 0 (Document Ingestion) and Phase 6 (Synthesis) note content — fold into the site once those phases produce notes.

### Reviewed Todos (not folded)
None — no pending todos matched this phase.

</deferred>

---

*Phase: 7-integrated-html-study-site*
*Context gathered: 2026-06-15*
