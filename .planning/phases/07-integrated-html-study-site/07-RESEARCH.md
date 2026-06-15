# Phase 7: Integrated HTML Study Site - Research

**Researched:** 2026-06-15
**Domain:** Static-site assembly via a Python build script (python-markdown + pymdownx + pygments + vendored MathJax), built into `/docs` for GitHub Pages
**Confidence:** HIGH (environment verified by direct probing; key library/version claims verified against PyPI/npm; MathJax+math approach verified against official docs)

## Summary

This phase is a **mechanical assembly job**, not a design or research problem: the design system already exists (extract it verbatim), the content already exists (15 notes + 3 research HTML pages + 3 demos), and every implementation decision D-01..D-13 is locked. The dominant technical risk is a single, well-known failure mode — **LaTeX `$...$` math being mangled by Markdown's emphasis/escape processing** (underscores in `T_c`, asterisks, backslashes). The decisive, least-fragile mitigation is verified below: use `pymdownx.arithmatex` with `generic=True`, which extracts math *before* Markdown touches it, normalizes to `\(...\)`/`\[...\]`, and pairs with a MathJax config that only processes `.arithmatex` elements. This eliminates the entire class of `$`-mangling bugs without escaping gymnastics.

The second-largest risk is **broken relative links** after copying the three research HTML pages into `/docs/architecture/`: those pages cross-link to each other, to `sources/*.html` siblings (mapek, flisr), and contain *dead* `.md` references (`adaptive-power.md`, `ocr.md`) that never had HTML equivalents. The build must copy the full link-closure (trio + `sources/` + the AGMS diagram) and the planner must decide how to handle the dead `.md` "Quick links" (leave as-is = harmless dead links, or strip). The AGMS diagram is **standalone** (not embedded in any HTML) — it needs its own viewer page or inline `<img>` on an architecture page.

**Primary recommendation:** One idempotent `build_site.py` run in the **system Python** (pygments 2.17.2 already there; `pip install --user markdown pymdown-extensions` or a fresh venv adds the rest). Convert notes with extensions `[arithmatex(generic), tables, fenced_code, codehilite(pygments), toc, attr_list, md_in_html, sane_lists, smarty-off]`; wrap each in the extracted shared `assets/site.css` shell; vendor **MathJax 3.2.2** (not 4.x) for offline `tex-chtml`; generate pygments CSS once via `pygmentize -S friendly -f html`; copy the research trio + `sources/` + diagram into `architecture/` and rewrite only the PDF links in `INDEX.html`.

## User Constraints (from CONTEXT.md)

### Locked Decisions (D-01..D-13)
- **D-01:** Convert the 15 Markdown notes with a reproducible **Python build script** (`python-markdown` + `pygments` + bundled MathJax) — NOT hand-authored, NOT SSG, NOT pandoc. Re-runnable.
- **D-02:** `pygments` already installed; `python-markdown` must be added (one `pip install`; reuse `.venv-crawl` or fresh venv = planner's discretion). `pandoc` not installed and not to be used.
- **D-03:** Extract the canonical CSS design system from the existing research HTML into a shared stylesheet so converted notes match visually.
- **D-04:** Build **into the existing `/docs` folder** — do NOT rename it. Preserves ~30 `docs/...` references and co-locates source PDFs.
- **D-05:** Structure inside `/docs`: hub `index.html`, subfolders `architecture/`, `notes/`, `demos/`, `vendor/mathjax/`. Source PDFs stay at `/docs/*.pdf`.
- **D-06:** Publish target = GitHub Pages from `/docs`. Provide `PUBLISH.md` (root or `/docs` = discretion). Actual deploy deferred.
- **D-07:** **Copy** the three research HTML pages + AGMS diagram (`.svg`/`.png`) into `/docs/architecture/`, preserving relative cross-links. Do not rebuild.
- **D-08:** Fix patent-PDF links inside copied `INDEX.html` to resolve to `/docs/*.pdf` (e.g. `../patent-data-management.pdf` from `/docs/architecture/`).
- **D-09:** Hub = **card-grid** in 3 groups (Architecture / Study Notes / Demos). Each content page keeps its own sticky sidebar TOC.
- **D-10:** Embed demo result images inline with caption (`ekf_line_temp.png`, `dc_powerflow_baddata.png`). Phase 5 has no PNG → render its key numeric output as a table/code block.
- **D-11:** Embed **key functions only** (not whole files), highlighted **at build time with pygments** (no runtime JS). Link to full source `.py`.
- **D-12:** Each demo section = natural-language what/why(gap-closed)/what-it-shows, sourced from the demo `README.md` files.
- **D-13:** Bundle **MathJax locally** under `/docs/vendor/mathjax/` (tex-chtml), `$…$`/`$$…$$` delimiters, offline `file://`.

### Claude's Discretion
- venv strategy for `python-markdown` (reuse `.venv-crawl` vs new venv).
- Precise MathJax component/version + config object.
- File-naming scheme for converted note pages (e.g. `notes/kal-01-wls.html`).
- `PUBLISH.md` location (repo root vs `/docs/`).
- Per-page footer "back to hub" / prev-next niceties.
- CSS delivery (single external `assets/site.css` preferred).

### Deferred Ideas (OUT OF SCOPE)
- Actual deployment to GitHub Pages (enable Pages → get unlisted URL).
- Deploy-time privacy review (publishing `/docs` exposes patent PDFs + CV; patents are public record, site is noindex/unlisted — confirm at deploy, not a build blocker).
- Curated/redacted "share" build (rejected; single full build keeps `▶ Juan` notes).
- Phase 0 / Phase 6 note content (none exists yet).

## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| HTML-01 | Hub `index.html` with grouped nav to all 3 areas | Build script generates card-grid hub from a manifest of emitted pages; broken-link self-check validates every href (see Build-Script Architecture, Pitfall 5) |
| HTML-02 | Architecture section integrated (reuse, not rebuild) | Copy trio + `sources/` + diagram into `architecture/`; rewrite INDEX PDF links; link from hub (see Link-Closure & Relative Paths) |
| HTML-03 | All 15 Phase 1–5 notes → styled HTML | python-markdown + extension set + shared CSS shell; verified file inventory (15 files confirmed present) |
| HTML-04 | Offline math via bundled MathJax | `pymdownx.arithmatex(generic)` + vendored MathJax 3.2.2 tex-chtml + arithmatex config (see Math Rendering — verified against official docs) |
| HTML-05 | Demo sections: explain + embed key code + link results | Function-name slicing of `.py` (clean `def` boundaries verified) + pygments highlight at build; README narrative; inline `<figure>` for 2 PNGs, table for FED demo |
| HTML-06 | Self-contained, offline, publish-ready + PUBLISH.md | All-relative links inside `/docs`; vendored MathJax; `.nojekyll`; PUBLISH.md (see GitHub Pages section) |
| HTML-07 | Unlisted-by-default (noindex) | `<meta name="robots" content="noindex,nofollow">` in every emitted `<head>` + optional `robots.txt` |

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Markdown → HTML conversion | Build script (Python, build-time) | — | D-01; offline static site, no runtime processing |
| Syntax highlighting | Build script (pygments, build-time) | — | D-11 explicitly forbids runtime JS highlighting |
| Math typesetting | Browser (MathJax JS, render-time) | — | Math must reflow/typeset client-side; only thing that runs in browser |
| Styling | Static CSS asset (`assets/site.css`) | — | Single external stylesheet (D-03, discretion) |
| Navigation / hub | Static HTML (build-generated) | — | No server; all links relative |
| Hosting | CDN/Static (GitHub Pages from `/docs`) | Browser `file://` | Must work both at `file://` and over Pages (D-06, HTML-06) |

**Key point:** The ONLY thing that executes in the browser is MathJax. Everything else (highlighting, TOC anchors, page assembly) happens once at build time. This is the safest possible architecture for the offline-first constraint.

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| `markdown` (python-markdown) | **3.10.2** (latest) `[VERIFIED: PyPI]` | MD→HTML conversion engine | Reference Python Markdown impl; D-01 mandates it; pluggable extension API |
| `pymdown-extensions` | **10.21.3** (latest) `[VERIFIED: PyPI]` | Provides `arithmatex` (robust math) + `superfences`/`highlight` | The de-facto extension pack (powers MkDocs Material); arithmatex is THE solution to the `$`-mangling pitfall `[CITED: facelessuser.github.io/pymdown-extensions/extensions/arithmatex]` |
| `pygments` | **2.17.2** (already installed in SYSTEM python) `[VERIFIED: pip3 list + /usr/bin/pygmentize]` | Build-time syntax highlighting | D-11; emits `<div class="highlight">` + a separate CSS file |
| MathJax | **3.2.2** (latest 3.x) `[VERIFIED: npm registry]` | Offline client-side math typesetting | tex-chtml component; 3.2.2 is battle-tested + abundant offline-hosting docs. See "MathJax version" note below |

> **Correction to briefing:** The briefing/CONTEXT stated `pygments` is installed in `.venv-crawl`. **VERIFIED FALSE** — `.venv-crawl` contains only `bs4 4.15.0`. `pygments 2.17.2` (and `pygmentize`) live in the **system Python** (`/usr/bin/python3`, `/usr/bin/pygmentize`). `python-markdown` is in neither. This changes the venv recommendation (see below).

### Supporting / built-in extensions (no install — ship with python-markdown)
| Extension | Purpose | When to Use |
|-----------|---------|-------------|
| `tables` | GitHub-style pipe tables | All notes (every note has tables) |
| `fenced_code` | ` ``` ` fenced blocks | KAL-03, STK-04/05, FED, demos |
| `codehilite` | Routes fenced code through pygments | Paired with pygments CSS; use `guess_lang=False` |
| `toc` | Generates heading anchor IDs (`#...`) for the sticky sidebar TOC | Every note page (D-09 TOC); set `toc_depth="2-3"` |
| `attr_list` | `{: .class}` attributes on elements | Optional — lets notes opt into `.callout`/`.juan` if authored |
| `md_in_html` | Markdown inside raw HTML blocks | Defensive — some notes may embed HTML |
| `sane_lists` | Predictable list numbering | Avoids list-restart surprises |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| `pymdownx.arithmatex` | `python-markdown-math` (`mdx_math`) | Also works, but smaller/less-maintained; arithmatex is better-tested and already bundled with pymdown-extensions which you want anyway |
| `codehilite` (built-in) | `pymdownx.highlight` + `pymdownx.superfences` | superfences is more robust (handles nested fences, custom fences) but adds complexity. For these notes, built-in `codehilite` + `fenced_code` is sufficient. Either is fine — pick one, do not mix two highlighters |
| MathJax 3.2.2 | MathJax 4.1.2 (current npm latest) | v4 is newer/faster but a fresh major; for a 1-week deadline, v3.2.2 has the most-documented offline-hosting path and arithmatex config examples target it. **Recommend v3.2.2.** `[ASSUMED: v3 lower-risk; both work with arithmatex generic]` |
| MathJax tex-chtml | KaTeX | KaTeX is faster but doesn't cover all the LaTeX these notes use (`\lVert`, environments); MathJax is safer for fidelity (HTML-04 "render correctly"). D-13 already says MathJax |

**Installation (recommended — fresh dedicated venv to avoid mutating `.venv-crawl`):**
```bash
cd /home/juan/codes/ge-vernova-virtual-sensing
python3 -m venv .venv-site
.venv-site/bin/pip install "markdown==3.10.2" "pymdown-extensions==10.21.3" "pygments==2.17.2"
```
(Alternatively reuse system Python which already has pygments: `pip3 install --user markdown pymdown-extensions`. A dedicated venv is cleaner and pinnable; `.venv-crawl` is reserved for the bs4 crawl tooling and need not be touched.)

**Version verification performed this session:**
- `markdown` latest **3.10.2** `[VERIFIED: pip index versions markdown]`
- `pymdown-extensions` latest **10.21.3** `[VERIFIED: pip index versions pymdown-extensions]`
- `pygments` **2.17.2** present in system python `[VERIFIED: pip3 list]`
- MathJax npm dist-tags: `latest=4.1.2`, latest 3.x = **3.2.2** `[VERIFIED: registry.npmjs.org/mathjax]`

## Architecture Patterns

### System Architecture Diagram

```
                          build_site.py  (run once, idempotent)
                          ───────────────────────────────────────
  SOURCES (read-only, stay in .planning/)            BUILD STEPS                 OUTPUT (/docs)
  ┌─────────────────────────────────┐
  │ .planning/phases/0{1..5}/notes/ │──discover 15 .md──►  [convert]  md→HTML  ──► /docs/notes/<slug>.html
  │   *.md  (LaTeX $..$, tables,    │                      (markdown +              (shared shell + sticky TOC
  │          fenced code)           │                       arithmatex +             + MathJax script tag)
  └─────────────────────────────────┘                       codehilite/pygments
                                                             + toc)
  ┌─────────────────────────────────┐
  │ .planning/research/patents/*.html│──copy trio + sources/──►  [copy + relink]  ──► /docs/architecture/*.html
  │ .planning/research/*.html        │                           (rewrite INDEX           (cross-links intact,
  │ .planning/research/sources/*.html│                            PDF hrefs → ../*.pdf)    PDFs resolve to /docs/*.pdf)
  │ AGMS-architecture.svg/.drawio.png│──copy diagram──────────►  /docs/architecture/AGMS-architecture.svg(+png)
  └─────────────────────────────────┘
  ┌─────────────────────────────────┐
  │ .planning/phases/0{1,2,5}/demo/ │──read .py + README + png──► [extract+highlight] ──► /docs/demos/index.html
  │   *.py  *.png  README.md         │                            (slice key funcs,        (explain + <figure> img
  └─────────────────────────────────┘                             pygments-highlight,       + highlighted code +
                                                                   inline png/figure)        "view full source" → copied .py)
                                                                          │
  npm mathjax@3.2.2 es5/ ────vendor tex-chtml subset──────────────────────┼──► /docs/vendor/mathjax/...
  pygmentize -S friendly ───generate code CSS──────────────────────────────┼──► /docs/assets/pygments.css
  extracted <style> block ──one shared stylesheet (D-03)───────────────────┼──► /docs/assets/site.css
                                                                          │
                                                                          ▼
                                              [generate hub]  card-grid from manifest  ──► /docs/index.html
                                              [emit]  .nojekyll, robots.txt, PUBLISH.md
                                              [validate]  every emitted href resolves to a real file (fail loud)
```

A reader can trace one note: `KAL-03-...md` → markdown(arithmatex extracts `$$mC_p...$$` to `\[...\]` span) → wrapped in `site.css` shell with MathJax script → `/docs/notes/kal-03-ieee738-ekf.html` → opened at `file://`, MathJax processes only `.arithmatex` spans → typeset equations.

### Recommended /docs structure (D-05)
```
docs/
├── index.html              # hub (card-grid, 3 groups) — HTML-01
├── PUBLISH.md              # deploy guide (or repo root — discretion) — HTML-06
├── .nojekyll              # CRITICAL: stops Pages/Jekyll mangling vendor/ + _-prefixed files
├── robots.txt             # optional reinforcement of noindex — HTML-07
├── assets/
│   ├── site.css           # extracted design system (D-03) + new hub-card/figure/pygments-host rules
│   └── pygments.css       # generated: pygmentize -S friendly -f html -a .highlight
├── architecture/          # HTML-02 (copied, NOT rebuilt — D-07)
│   ├── AGMS-architecture.html
│   ├── grid-operations-and-role.html
│   ├── INDEX.html         # PDF links rewritten ../*.pdf (D-08)
│   ├── AGMS-architecture.svg   (2.9 MB) + AGMS-architecture.drawio.png (1.6 MB)
│   └── sources/           # flisr-distributed-fsm-2014.html, mapek-aware-2025.html (link-closure!)
├── notes/                 # HTML-03 (15 generated pages)
│   ├── kal-01-wls.html ... fed-03-edge-security.html
├── demos/                 # HTML-05
│   ├── index.html         # 3 demo sections
│   ├── ekf_line_temp.png  ekf_line_temp_demo.py
│   ├── dc_powerflow_baddata.png  dc_powerflow_baddata_demo.py
│   └── fedavg_fedprox_krum_demo.py
├── vendor/mathjax/        # HTML-04 (vendored 3.2.2 tex-chtml + fonts/components)
└── *.pdf, job-requirements.md   # EXISTING source PDFs — leave in place (D-04)
```

### Pattern 1: Robust math — arithmatex generic + scoped MathJax
**What:** Extract math before Markdown can mangle it; tell MathJax to process only extracted spans.
**When to use:** Every note page (HTML-04).
**Build-side (python-markdown):**
```python
import markdown
md = markdown.Markdown(extensions=[
    "pymdownx.arithmatex",
    "tables", "fenced_code", "codehilite", "toc", "attr_list", "md_in_html", "sane_lists",
], extension_configs={
    "pymdownx.arithmatex": {"generic": True},   # normalize $..$/$$..$$ → \(..\)/\[..\] in .arithmatex spans
    "codehilite": {"guess_lang": False, "css_class": "highlight"},  # align class with pygments.css
    "toc": {"toc_depth": "2-3"},
})
html_body = md.convert(md_text)
toc_html  = md.toc            # ready-made sidebar TOC fragment
md.reset() # MUST reset between files when reusing the instance
```
**Page-side (in every note `<head>`, BEFORE the mathjax script):** `[CITED: facelessuser.github.io/pymdown-extensions/extensions/arithmatex]`
```html
<script>
window.MathJax = {
  tex: { inlineMath: [["\\(","\\)"]], displayMath: [["\\[","\\]"]],
         processEscapes: true, processEnvironments: true },
  options: { ignoreHtmlClass: ".*", processHtmlClass: "arithmatex" }
};
</script>
<script defer src="../vendor/mathjax/tex-chtml.js"></script>
```
Why this is the safest path: arithmatex stashes math during preprocessing, so `T_c`, `\alpha_s`, `R_{25}`, `\lVert w - w_t \rVert^2` never reach Markdown's emphasis/escape logic. `ignoreHtmlClass: ".*"` + `processHtmlClass: "arithmatex"` means MathJax ignores everything except the extracted spans — so stray `$` in prose or code blocks won't accidentally typeset.

### Pattern 2: Function-name slicing for demo code (D-11)
**What:** Embed only specific functions, not whole files.
**When to use:** Demo page (HTML-05). All three demos have clean top-level `def name(...):` boundaries `[VERIFIED: grep of the .py files]`:
- `ekf_line_temp_demo.py`: `ieee738_rhs`, `_process_jacobian`, `ekf_step` (the key one), `nis_check`, `ieee738_ampacity`, `run_demo`
- `dc_powerflow_baddata_demo.py`: `build_B_matrix`, `build_H`, `wls_solve` (key), `chi2_test` (key), `normalized_residuals`, `run_demo`
- `fedavg_fedprox_krum_demo.py`: `local_sgd`, `fedprox_local_step`, `fedavg_aggregate` (key), `krum_select` (key), `coord_median`, `run_demo`
**Approach (most robust):** parse with `ast` and slice by line numbers, OR simpler regex on `^def <name>` until the next top-level `^def `/`^class `/`^if __name__`. Then highlight:
```python
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
snippet_html = highlight(func_source, PythonLexer(), HtmlFormatter(cssclass="highlight"))
```
Generate the matching CSS once: `pygmentize -S friendly -f html -a .highlight > docs/assets/pygments.css` (friendly is a light style that coexists with `--code-bg #f4f6f8`; `default` also fine).

### Pattern 3: Shared shell template
**What:** One Python f-string/Jinja-free template producing the `.wrap` grid (masthead + `nav.toc` + `main` + footer) wrapping converted body + generated TOC. CSS extracted once from `AGMS-architecture.html` lines 8–35 (the full `:root` + rules block — read and copy verbatim per D-03/UI-SPEC) into `assets/site.css`, plus the 3 additive rules (`.hub-card`/`.card-grid`, `figure/figcaption`, pygments host tuning).

### Anti-Patterns to Avoid
- **Two highlighters at once:** Do NOT enable both `codehilite` and `pymdownx.highlight`/`superfences` — class clashes + double-wrapping. Pick one.
- **Raw-`$` MathJax (`inlineMath: [["$","$"]])`:** the fragile path the briefing warns about. With arithmatex generic you do NOT use `$` delimiters in MathJax config at all — you use `\(`/`\[`. Do not re-add `$`.
- **Rebuilding the research HTML:** D-07 says copy. Re-converting `AGMS-architecture.md` would lose the hand-tuned design.
- **Forgetting `.nojekyll`:** Pages runs Jekyll by default, which ignores `vendor/`-style and `_`-prefixed paths and can break the MathJax component tree. Always emit `.nojekyll`.
- **`md.convert()` without `md.reset()`** between files: TOC/footnote state leaks across pages.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Protect `$...$` math from Markdown | Custom regex to escape `_`/`*`/`\` in math | `pymdownx.arithmatex(generic=True)` | Edge cases (nested braces, `\\`, environments, math inside tables) are exactly what eats hand-rolled escaping; arithmatex is purpose-built and tested |
| Syntax highlighting | Hand CSS-classing tokens | pygments (already installed) | D-11; thousands of token rules |
| Heading anchors / sidebar TOC | Manual `id=` injection + link list | `toc` extension (`md.toc`) | Slug collisions, unicode, depth control handled |
| MD tables/lists/code | Custom parser | python-markdown built-ins | Don't reimplement a CommonMark-ish parser |
| Math typesetting in browser | Anything | Vendored MathJax 3.2.2 | D-13 |

**Key insight:** Every hard part of this phase already has a maintained library. The only bespoke code is glue: file discovery, the shared HTML shell, function slicing, link rewriting, and the broken-link self-check.

## Common Pitfalls

### Pitfall 1: `$...$` math mangled by Markdown (THE big one)
**What goes wrong:** `T_c`, `q_i`, `R_{25}` → underscores become `<em>` italics; `$I^2 \cdot R$` corrupted; `\(`/`\)` escaped away. Notes contain 170 `$` in KAL-03 alone, dense subscripts everywhere `[VERIFIED: grep]`.
**Why it happens:** Markdown processes `_`/`*`/`\` as formatting before any math engine sees them.
**How to avoid:** `pymdownx.arithmatex(generic=True)` + scoped MathJax config (Pattern 1). Math is stashed pre-processing.
**Warning signs:** italicized subscripts, literal `\(` in output, equations rendering as plain text.

### Pitfall 2: CHTML fonts fail at `file://`
**What goes wrong:** `tex-chtml.js` needs its font/component files at a path relative to the script; if you vendor only `tex-chtml.js` without the font tree, math renders boxes/fallback at `file://`. `[CITED: docs.mathjax.org v3 hosting — "CHTML files require access to additional fonts"]`
**Why it happens:** MathJax loads sub-components (output fonts, a11y) lazily relative to the main script.
**How to avoid:** Vendor the **entire `node_modules/mathjax/es5/` tree** (or at minimum `tex-chtml.js` + `output/chtml/fonts/woff-v2/` + `input/` + `output/` dirs it references) into `vendor/mathjax/`. Simplest reliable move: `npm install mathjax@3.2.2` then copy the whole `es5/` directory. Test by opening a note with networking off.
**Warning signs:** math shows tofu/boxes offline but works online (means it's silently CDN-fetching components).

### Pitfall 3: Broken cross-links after copying research HTML
**What goes wrong:** Copied pages link to siblings that weren't copied. `[VERIFIED: grep of the HTML]`
- `grid-operations-and-role.html` → `patents/AGMS-architecture.html`, `patents/INDEX.html`, **`sources/flisr-distributed-fsm-2014.html`**, **`sources/mapek-aware-2025.html`**
- `AGMS-architecture.html` → `INDEX.html`, `../grid-operations-and-role.html`
- `INDEX.html` → `AGMS-architecture.html` (+ a body PDF link `patent-data-management.pdf`)
**Why it happens:** The trio currently lives in two dirs (`patents/` + `research/`) with relative `../` and `patents/` paths. Flattening all into `architecture/` changes the relative depth. Also `sources/` is easy to miss.
**How to avoid:** Decide a layout and rewrite accordingly. Cleanest: put `grid-operations-and-role.html` and the `patents/` pages all directly in `architecture/` and `sources/` in `architecture/sources/`. Then `../grid-operations-and-role.html` (from old patents/ depth) must become `grid-operations-and-role.html`, and `patents/AGMS-architecture.html` (from grid-ops) becomes `AGMS-architecture.html`. **Rewrite cross-links during copy**, don't assume they survive.
**Warning signs:** 404 on the architecture pages; the build-time link checker (HTML-01 acceptance) catching them.

### Pitfall 4: Dead `.md` "Quick links" in AGMS-architecture.html
**What goes wrong:** AGMS-architecture.html's "Quick links" section references `adaptive-power.md`, `logistician-module.md`, `asset-portfolio.md`, `operation-loop.md`, `scout-command.md`, `data-management.md`, `ocr.md` — these are **plain `<code>` text, not links** for most, but `INDEX.md` is a real `<a href="INDEX.html">` (works). `ocr.md` was deleted (git status `D`). `[VERIFIED: tail of AGMS-architecture.html]`
**Why it happens:** The HTML was generated from a richer source set; those `.md` siblings were never converted to HTML and won't be copied (out of scope — only the trio is copied).
**How to avoid:** These are mostly inert `<code>` labels (not hrefs) → harmless, leave as-is. The only real `href` in that block is `INDEX.html` (valid) and `../grid-operations-and-role.html` (fix per Pitfall 3). Planner decision: leave the `<code>` labels (lowest effort, recommended) — they are not broken links, just references. Do not treat them as link targets.

### Pitfall 5: Hub links to non-existent pages / silent 404s
**What goes wrong:** Hub card points to a note slug that the converter named differently → 404 at `file://`, failing HTML-01 acceptance.
**How to avoid:** Single source of truth — the build generates the hub **from the same manifest** it used to emit pages (slug ↔ file). Add a final validation pass: for every `href` the build wrote, assert the target file exists on disk; **fail loudly** (UI-SPEC error contract).

### Pitfall 6: Large assets / repo bloat
**What goes wrong:** AGMS-architecture.svg is **2.9 MB**, the drawio png **1.6 MB**, patent PDFs up to **21 MB** each `[VERIFIED: ls -la]`. Copying svg+png into `architecture/` is fine; PDFs already exist in `/docs` (not copied again).
**How to avoid:** Prefer the SVG for inline display (crisp, but 2.9 MB); offer the PNG as a fallback/download. Don't duplicate PDFs. This is a note, not a blocker.

### Pitfall 7: AGMS diagram is standalone (not embedded anywhere)
**What goes wrong:** `[VERIFIED: grep — no `<img>`/`.svg`/`.png` reference in AGMS-architecture.html]` The diagram is a separate file referenced by nothing. If the hub just links the three HTML pages, the diagram is orphaned (fails HTML-02 "the AGMS architecture diagram displays").
**How to avoid:** Either (a) inject an `<img src="AGMS-architecture.svg">` into a new figure on the architecture hub/section, or (b) create a tiny `architecture/diagram.html` viewer page wrapping the SVG in the shared shell, linked from the hub. Recommend (b) for consistency.

## Code Examples

### Generate pygments stylesheet (one-time, build step)
```bash
# friendly = light style harmonizing with --code-bg #f4f6f8; -a scopes to .highlight
pygmentize -S friendly -f html -a .highlight > docs/assets/pygments.css
```

### Vendor MathJax 3.2.2 offline (recommended)
```bash
# in a scratch dir
npm install mathjax@3.2.2          # creates node_modules/mathjax/es5/
mkdir -p docs/vendor/mathjax
cp -r node_modules/mathjax/es5/* docs/vendor/mathjax/   # whole es5 tree → fonts/components included
# page loads:  <script defer src="../vendor/mathjax/tex-chtml.js"></script>
```
(No npm? Download the MathJax 3.2.2 release tarball from GitHub `mathjax/MathJax` and copy its `es5/` folder. `[CITED: docs.mathjax.org v3 hosting]`)

### Per-page `<head>` contract (from UI-SPEC, every emitted page)
```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">                <!-- HTML-07 -->
<link rel="stylesheet" href="../assets/site.css">
<link rel="stylesheet" href="../assets/pygments.css">
<!-- note pages only: MathJax config block + tex-chtml.js (see Pattern 1) -->
```

### robots.txt (optional reinforcement, /docs root)
```
User-agent: *
Disallow: /
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| `$`-delimiter MathJax + escaping hacks | arithmatex generic + scoped `processHtmlClass` | mature since pymdownx 7+ | eliminates the `$`-mangling class of bugs |
| MathJax 2 `MathJax.Hub` config | MathJax 3 `window.MathJax = {...}` object before script | MathJax 3 (2019) | training data may show v2 syntax — use v3 object form |
| MathJax 3.x | MathJax **4.1.2** now npm `latest` | 2024–2025 | v4 exists; recommend staying on **3.2.2** for this deadline (most docs/examples) |

**Deprecated/outdated:**
- `MathJax.Hub.Config(...)` / `tex2jax` (v2): replaced by the `window.MathJax` object + `tex`/`options` keys in v3+.
- Loading MathJax from CDN: violates offline constraint — must vendor.

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | MathJax **3.2.2** is the lower-risk choice over 4.1.2 for this deadline | Standard Stack | LOW — both work with arithmatex generic; v4 would also function, just less example coverage. Verify the chosen version's `tex-chtml.js` path |
| A2 | `friendly` pygments style harmonizes with the design system | Code Examples | LOW — cosmetic; swap style string if it clashes |
| A3 | Dead `.md` references in AGMS Quick links are inert `<code>` labels, safe to leave | Pitfall 4 | LOW — verified most are `<code>` not `href`; planner should confirm during link-check |
| A4 | Copying whole `es5/` tree suffices for offline CHTML fonts | Pitfall 2 | MEDIUM — if a leaner subset is desired, must include the chtml font dir explicitly; whole-tree copy is the safe default |

**Note:** No `[ASSUMED]` claims affect compliance/security/retention — this is a static doc site. A1/A4 are the only ones worth a quick executor confirmation (test math offline before declaring done).

## Open Questions

1. **MathJax 3.2.2 vs 4.1.2** — Recommendation: vendor 3.2.2 (`npm install mathjax@3.2.2`). If 4.x is preferred, the arithmatex generic config is unchanged; only verify `tex-chtml.js` still exists at the es5 root in v4 (it does).
2. **PUBLISH.md location** — discretion (D-06). Recommendation: `/docs/PUBLISH.md` so it travels with the site, but it is itself served — harmless (noindex). Repo-root is equally valid.
3. **Dead `.md` Quick links in copied AGMS HTML** — leave inert `<code>` labels (recommended) vs strip them. Low stakes.

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| python3 | build script | ✓ | 3.12.3 | — |
| pygments / pygmentize | D-11 highlighting | ✓ (system) | 2.17.2 | — |
| python-markdown | D-01 conversion | ✗ | — | `pip install markdown` (no network? would block — confirm pip access) |
| pymdown-extensions | arithmatex math safety | ✗ | — | `pip install pymdown-extensions`; fallback `python-markdown-math` |
| pandoc | (forbidden by D-02) | ✗ | — | N/A — not used |
| npm | vendoring MathJax | unknown (not probed) | — | download MathJax 3.2.2 release tarball from GitHub, copy `es5/` |
| MathJax (vendored) | D-13 offline math | ✗ (not yet vendored anywhere) | — | must be fetched/vendored |
| `.venv-crawl` | candidate env (has bs4 only) | ✓ | py3.12 | prefer fresh `.venv-site` |

**Missing dependencies with no fallback:** none hard-blocking, BUT installation requires either pip network access or an offline wheel cache, and MathJax requires either npm or a one-time download. **Confirm the executor has network for the install/vendor step** (the *site* is offline; the *build* needs to fetch these once).

**Missing with fallback:** python-markdown/pymdown-extensions (pip), MathJax (npm or GitHub tarball).

## Validation Architecture

> `.planning/config.json` `workflow.nyquist_validation` was not located as explicitly `false`; this is a static-site/docs phase so validation is link/render integrity, not a unit-test framework.

### Test "Framework"
| Property | Value |
|----------|-------|
| Framework | None code-test; integrity checks are build-script asserts + manual offline open |
| Config file | none |
| Quick run command | `python build_site.py && python -c "import pathlib,re,sys; ..."` (link check, see below) |
| Full check | Open `docs/index.html` at `file://` with networking disabled; click through all areas |

### Phase Requirements → Validation Map
| Req | Behavior | Check Type | Command / Method |
|-----|----------|-----------|------------------|
| HTML-01 | Every hub href resolves | automated | Build emits manifest; assert each linked file exists; fail loud |
| HTML-02 | 3 research pages + diagram render, cross-links work | automated+manual | grep emitted `architecture/*.html` hrefs, assert targets exist; eyeball render |
| HTML-03 | 15 notes emitted + render | automated | assert 15 files in `notes/`; spot-check headings/tables/code |
| HTML-04 | Math typesets offline | **manual (critical)** | disable network, open KAL-03 / TVS-02; confirm typeset, not raw `$` |
| HTML-05 | 3 demos: explain+code+result link | manual | open `demos/index.html`; verify figure, snippet, source link each demo |
| HTML-06 | Full offline navigation | manual | networking off, traverse from `index.html`; zero broken links |
| HTML-07 | noindex present | automated | grep `noindex` in every emitted `.html` |

### Wave 0 Gaps
- [ ] Build script must include a **link-validation pass** (every written href → file exists) — this IS the HTML-01/HTML-06 acceptance gate. Build it into `build_site.py`, not as a separate tool.
- [ ] One **offline smoke test** documented in PUBLISH.md or a comment: "disable network, open index.html, reach a math note."
- Framework install: `pip install markdown pymdown-extensions` (pygments present).

## Security Domain

> Static, offline study site with no auth, no input, no server, no data store. `security_enforcement` is effectively N/A for runtime. The only security-relevant facts are disclosure-related and already captured as a deferred deploy-time decision.

### Applicable ASVS Categories
| ASVS Category | Applies | Standard Control |
|---------------|---------|-----------------|
| V2 Authentication | no | static site, no auth |
| V3 Session | no | no sessions |
| V4 Access Control | no (deploy-time only) | `noindex` + unlisted URL (HTML-07); publishing `/docs` exposes patent PDFs + CV publicly — **deploy-time disclosure decision**, recorded as deferred |
| V5 Input Validation | no | no runtime input |
| V6 Cryptography | no | none |
| V14 Config | yes (light) | `.nojekyll`, `robots.txt`, `noindex` meta; do not commit secrets to `/docs` |

### Known Threat Patterns
| Pattern | STRIDE | Standard Mitigation |
|---------|--------|---------------------|
| Unintended public disclosure of CV/patent PDFs via served `/docs` | Information Disclosure | `noindex`/`nofollow` + unlisted URL; deploy-time confirm-or-relocate sensitive PDFs (deferred per CONTEXT). Patents are public record |
| Search-engine indexing of personal prep | Information Disclosure | HTML-07 noindex meta + robots.txt Disallow |

## Sources

### Primary (HIGH confidence)
- Direct environment probing (this session): `.venv-crawl` contents, system pygments/pygmentize, docs/ inventory, all 15 note files, 3 research HTML files + cross-links, demo `.py` function boundaries, AGMS diagram standalone, dead `.md` quick-links — all VERIFIED by Bash.
- PyPI version queries (this session): `markdown 3.10.2`, `pymdown-extensions 10.21.3`, `pygments 2.17.2`.
- npm registry: `mathjax` dist-tags (latest 4.1.2, latest 3.x = 3.2.2).
- PyMdown Extensions docs — arithmatex generic mode + MathJax 3 config — https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/
- MathJax docs — hosting your own copy / CHTML font requirement — https://docs.mathjax.org/en/v3.2/web/hosting.html , https://docs.mathjax.org/en/latest/web/start.html

### Secondary (MEDIUM confidence)
- MathJax v3.0–3.2 hosting docs (search-surfaced) — offline es5/ vendoring pattern.

### Tertiary (LOW confidence)
- None — all load-bearing claims verified or cited.

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — versions verified against PyPI/npm this session; arithmatex approach verified against official docs.
- Architecture: HIGH — every step maps to a locked decision (D-01..D-13) and verified source files.
- Pitfalls: HIGH — math-mangling, link-closure, dead `.md` links, standalone diagram, CHTML fonts all verified by direct inspection or official docs.
- Environment: HIGH — probed directly; one correction to briefing (pygments is system, not `.venv-crawl`).

**Research date:** 2026-06-15
**Valid until:** 2026-07-15 (stable tooling; library versions may tick but APIs stable)
