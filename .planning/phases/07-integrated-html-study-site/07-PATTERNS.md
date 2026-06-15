# Phase 7: Integrated HTML Study Site - Pattern Map

**Mapped:** 2026-06-15
**Files analyzed:** 9 file groups (build script, hub, shared CSS, pygments CSS, 15 note pages, demos page, 3 copied architecture pages, MathJax vendor, PUBLISH.md/robots/.nojekyll)
**Analogs found:** 7 / 9 (build_site.py and PUBLISH.md are greenfield — no analog)

This is a **mechanical assembly job** (per RESEARCH.md): the design system already exists and must be lifted **verbatim**, not redesigned. The single most important analog is the hand-authored research HTML — every new page's `<style>`/shell/markup is copied from it.

---

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `docs/build_site.py` | build script (greenfield glue) | batch / transform (MD→HTML) | *(none — closest reference is the HTML it must emit)* | **no analog** |
| `docs/assets/site.css` | config / shared stylesheet | static asset | `AGMS-architecture.html` lines 8–35 (`<style>`) | **exact** (lift verbatim) |
| `docs/assets/pygments.css` | config / generated stylesheet | static asset (build-generated) | `pre.diagram` / `code` rules in AGMS CSS (palette target) | role-match |
| `docs/index.html` (hub) | template / landing | request-response (navigation) | `INDEX.html` (masthead `.meta` + card grid) | **exact** (shell), additive `.card-grid` |
| `docs/notes/<slug>.html` ×15 | template (build-emitted page) | transform output | `AGMS-architecture.html` (full `.wrap` shell + `nav.toc`) | **exact** (shell) |
| `docs/demos/index.html` | template (build-emitted page) | transform output | `AGMS-architecture.html` shell + `<figure>`/pygments additive | role-match |
| `docs/architecture/*.html` ×3 | content (copied, NOT rebuilt) | static (copy + relink) | the three source files themselves | **identity copy** |
| `docs/vendor/mathjax/**` | vendored library | static asset (offline) | *(none — vendored 3rd-party)* | n/a (vendored) |
| `docs/PUBLISH.md`, `robots.txt`, `.nojekyll` | config / docs | static | *(none — greenfield)* | **no analog** |

**Source files for content extraction (read-only, NOT modified):**
- 15 notes under `.planning/phases/0{1..5}/.../notes/*.md` (HTML-03)
- 3 demo `.py` + `README.md` + 2 `.png` under `.planning/phases/0{1,2,5}/demo/` (HTML-05)
- Research trio + `sources/` + diagram under `.planning/research/` (HTML-02)

---

## Pattern Assignments

### `docs/assets/site.css` (shared stylesheet) — THE canonical pattern

**Analog:** `.planning/research/patents/AGMS-architecture.html` lines 8–35 (the complete `<style>` block).

**Copy this `:root` + rule block VERBATIM** (D-03; this is the locked design system — do not re-derive values):

```css
:root{--panel:#fff;--ink:#1a2230;--muted:#5c6b7a;--line:#e3e8ee;--accent:#0b6e4f;--accent-soft:#e7f4ee;--gold:#b8860b;--code-bg:#f4f6f8;--callout:#fff8e6;--callout-line:#e0b84c;--juan-bg:#eef7f1;--juan-line:#0b6e4f;}
*{box-sizing:border-box;} html{scroll-behavior:smooth;}
body{margin:0;background:#eef1f5;color:var(--ink);font:16px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;}
.wrap{max-width:1180px;margin:0 auto;padding:0 20px 80px;display:grid;grid-template-columns:250px 1fr;gap:36px;}
@media (max-width:900px){.wrap{grid-template-columns:1fr;}nav.toc{position:static!important;max-height:none!important;}}
header.masthead{grid-column:1/-1;background:linear-gradient(135deg,#0f1f2e 0%,#11342a 100%);color:#fff;border-radius:14px;padding:30px 36px;margin:28px 0 6px;box-shadow:0 8px 30px rgba(15,31,46,.25);}
header.masthead h1{margin:0;font-size:28px;letter-spacing:.2px;line-height:1.25;}
nav.toc{position:sticky;top:18px;align-self:start;max-height:calc(100vh - 36px);overflow:auto;font-size:13.5px;background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:16px 14px;}
nav.toc h2{font-size:11px;text-transform:uppercase;letter-spacing:1.4px;color:var(--muted);margin:0 0 10px;}
nav.toc a{display:block;color:var(--muted);text-decoration:none;padding:5px 8px;border-radius:6px;border-left:2px solid transparent;}
nav.toc a:hover{color:var(--accent);background:var(--accent-soft);border-left-color:var(--accent);}
main{min-width:0;}
section.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:18px 30px 26px;margin:18px 0;box-shadow:0 1px 3px rgba(20,30,45,.04);}
h2.sec{font-size:22px;margin:10px 0 6px;padding-bottom:10px;border-bottom:2px solid var(--accent-soft);color:#0c2a20;scroll-margin-top:16px;}
h3.sub{font-size:17px;margin:22px 0 4px;color:#13433a;}
p{margin:12px 0;} strong{color:#0c2233;} em{color:#33324a;} a{color:var(--accent);}
code{background:var(--code-bg);border:1px solid var(--line);border-radius:5px;padding:1px 5px;font-family:"SF Mono",ui-monospace,Menlo,Consolas,monospace;font-size:13px;color:#33424f;}
pre.diagram{background:#0f1722;color:#d6e3ee;border-radius:10px;padding:18px 20px;overflow-x:auto;font-family:"SF Mono",ui-monospace,Menlo,Consolas,monospace;font-size:12.5px;line-height:1.5;border:1px solid #1c2a3a;}
table{width:100%;border-collapse:collapse;margin:14px 0;font-size:14.5px;}
th,td{text-align:left;vertical-align:top;padding:9px 12px;border-bottom:1px solid var(--line);}
thead th{background:var(--accent-soft);color:#0c2a20;border-bottom:2px solid #cfe7dc;font-size:13px;}
tbody tr:nth-child(even){background:#fafbfc;} td code{font-size:12.5px;}
ul,ol{margin:12px 0;padding-left:24px;} li{margin:7px 0;}
.callout{background:var(--callout);border-left:4px solid var(--callout-line);border-radius:0 8px 8px 0;padding:12px 18px;margin:16px 0;}
.callout p{margin:0;}
.juan{background:var(--juan-bg);border-left:4px solid var(--juan-line);border-radius:0 8px 8px 0;padding:11px 18px;margin:14px 0;font-size:14.5px;}
footer{grid-column:1/-1;text-align:center;color:var(--muted);font-size:12.5px;margin-top:24px;}
```

**Plus carry over from `INDEX.html` lines 20–21, 41–43** (for the hub `.meta` subtitle + optional "Start here" cue):

```css
--start-bg:#eaf3ff; --start-line:#4a90d9;   /* INDEX :root additions */
header.masthead h1 { margin: 0 0 14px; font-size: 30px; }   /* INDEX uses 30px h1 + 14px gap when a .meta follows */
header.masthead .meta { font-size: 15px; line-height: 1.7; color: #d7e3dd; }
header.masthead .meta strong { color: #fff; }
```

**Three ADDITIVE rule sets to author NEW** (not in any analog — per UI-SPEC component inventory):
1. `.card-grid` / `.hub-card` — hub cards; reuse the `section.card` surface + the `nav.toc a:hover` accent treatment (accent text + `--accent-soft` bg + accent left border) for hover.
2. `figure` / `figcaption` — demo result images (D-10); caption at meta scale (13.5px, `--muted`).
3. pygments host tuning — `div.highlight pre { font-size:12.5px; line-height:1.5; }` so generated code blocks sit alongside `pre.diagram`/inline `code`.

---

### `docs/notes/<slug>.html` ×15 (build-emitted note pages)

**Analog (shell):** `.planning/research/patents/AGMS-architecture.html` lines 37–56 (`.wrap` → masthead → `nav.toc` → `main`) and lines 263–266 (`footer` + close).

**Page shell template** (Python f-string in `build_site.py`; one external stylesheet, D-03/discretion):

```html
<div class="wrap">
  <header class="masthead"><h1>{note_title}</h1></header>
  <nav class="toc">
    <h2>Contents</h2>
    {md.toc}            <!-- generated by python-markdown `toc` extension -->
  </nav>
  <main>
    {converted_md_body}
    <footer><a href="../index.html">← Back to study hub</a></footer>
  </main>
</div>
```

**`<head>` contract** (every emitted page — RESEARCH.md "Per-page `<head>` contract" + HTML-07):

```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<link rel="stylesheet" href="../assets/site.css">
<link rel="stylesheet" href="../assets/pygments.css">
<!-- note pages: MathJax config block + tex-chtml.js BEFORE/with the script (Pattern 1 below) -->
```

**Markdown conversion (the load-bearing math-safety pattern — RESEARCH.md Pattern 1):**

```python
import markdown
md = markdown.Markdown(extensions=[
    "pymdownx.arithmatex", "tables", "fenced_code", "codehilite",
    "toc", "attr_list", "md_in_html", "sane_lists",
], extension_configs={
    "pymdownx.arithmatex": {"generic": True},
    "codehilite": {"guess_lang": False, "css_class": "highlight"},
    "toc": {"toc_depth": "2-3"},
})
html_body = md.convert(md_text)
toc_html  = md.toc
md.reset()   # MUST reset between files
```

**Per-note-page MathJax `<head>` block** (scoped so stray `$` never typesets — RESEARCH.md, CITED arithmatex docs):

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

**Source-note facts the converter must handle** (verified):
- Notes have **no YAML front matter** — they start with a `# H1` title (use it as `{note_title}` / masthead h1; the `toc` extension will pick up `##`/`###`).
- Heavy math: KAL-03 has 564 `$` chars (`$$mC_p \frac{dT_c}{dt}=...$$`, dense `T_c`/`R_{25}` subscripts); TVS-02 has 216. This is exactly the `$`-mangling risk arithmatex solves.
- GitHub pipe tables present in nearly every note (KAL-03: 47 table lines, STK-05: 46). `tables` extension required.
- Fenced code present (KAL-03: 16 fences, STK-05: 4) → `fenced_code` + `codehilite` route through pygments.
- STK-05 has 0 `$` (math optional per page) — MathJax script is harmless when no `.arithmatex` spans exist; keep the contract uniform.

**Suggested slug scheme** (discretion, D-claudes): lowercase the file stem, e.g. `KAL-03-ieee738-ekf-worked-example.md` → `notes/kal-03-ieee738-ekf-worked-example.html`. The hub MUST be generated from the same slug↔file manifest the converter emits (Pitfall 5 — single source of truth).

---

### `docs/index.html` (hub — HTML-01)

**Analog:** `.planning/research/patents/INDEX.html` — masthead with `.meta` subtitle (lines 41–43) is the closest existing pattern; the `.wrap` grid + masthead are identical to AGMS.

**Masthead copy (from UI-SPEC copywriting contract):**

```html
<header class="masthead">
  <h1>GE Vernova Virtual Sensing — Interview Study Site</h1>
  <div class="meta">Architecture, study notes, and hands-on demos in one place.</div>
</header>
```

**Card-grid structure** (NEW `.card-grid`/`.hub-card`, 3 groups — D-09): Architecture / Study Notes / Demos. Verb-led card links ("Read the AGMS walkthrough", "Open the study notes", "See the demos"). Reuse `section.card` look + `nav.toc a:hover` accent treatment. The hub may use `nav.toc` for the group jump-links or a flat header — TOC optional on the hub, mandatory on content pages.

---

### `docs/demos/index.html` (demos — HTML-05)

**Analog (shell):** `AGMS-architecture.html` shell (same as notes). **Additive components:** `<figure>` (D-10) and pygments `<div class="highlight">` (D-11).

**Per-demo block structure** (UI-SPEC demo copy contract, sourced from each `README.md`): "What it is" → "Why it was built (interview gap)" → "What it demonstrates" → inline `<figure>` result + caption → highlighted key-function code → "View full source →" link to the copied `.py`.

**README heading structure to mine for narrative** (verified, demo 01 `README.md`): `## What It Demonstrates`, `## Interview Talking Points`, `## Key Implementation Details`. Use these as the natural-language source.

**Key functions to embed (NOT whole files — D-11), verified `def` boundaries:**

| Demo `.py` | Key function(s) to slice | Line | Result artifact |
|------------|--------------------------|------|-----------------|
| `01-…/demo/ekf_line_temp_demo.py` | `ekf_step` (the key one), optionally `ieee738_rhs`, `_process_jacobian` | `ekf_step` @120, `ieee738_rhs` @54, `_process_jacobian` @96 | `ekf_line_temp.png` (inline `<figure>`) |
| `02-…/demo/dc_powerflow_baddata_demo.py` | `wls_solve` (key), `chi2_test` (key), optionally `normalized_residuals` | `wls_solve` @77, `chi2_test` @86, `normalized_residuals` @92 | `dc_powerflow_baddata.png` (inline `<figure>`) |
| `05-…/demo/fedavg_fedprox_krum_demo.py` | `fedavg_aggregate` (key), `krum_select` (key), optionally `coord_median` | `fedavg_aggregate` @86, `krum_select` @92, `coord_median` @110 | **no PNG** → render numeric output as `<table>`/code block |

**Slicing approach** (RESEARCH.md Pattern 2): all three files have clean top-level boundaries (`^def `, terminated by next `^def `/`^class `/`^if __name__ ==`). Use `ast` line numbers or regex; then:

```python
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
snippet_html = highlight(func_source, PythonLexer(), HtmlFormatter(cssclass="highlight"))
```

Demo `.py` files must be **copied into** `docs/demos/` so the "View full source →" link resolves offline.

---

### `docs/architecture/*.html` ×3 (copied, NOT rebuilt — HTML-02 / D-07)

**Analog = the files themselves** (`AGMS-architecture.html`, `grid-operations-and-role.html`, `INDEX.html`). Copy, do not regenerate. The CRITICAL work is **relative-link rewriting** because the trio currently lives at two directory depths and gets flattened into `architecture/`.

**Link-closure / rewrite map** (verified by grep — Pitfall 3). Target layout: trio directly in `architecture/`, `sources/` in `architecture/sources/`, diagram in `architecture/`, PDFs stay at `docs/*.pdf`:

| File | Existing href | Rewrite to |
|------|---------------|------------|
| `grid-operations-and-role.html` | `patents/AGMS-architecture.html` | `AGMS-architecture.html` |
| `grid-operations-and-role.html` | `patents/INDEX.html` | `INDEX.html` |
| `grid-operations-and-role.html` | `sources/flisr-distributed-fsm-2014.html` | `sources/flisr-distributed-fsm-2014.html` (unchanged — copy `sources/` too) |
| `grid-operations-and-role.html` | `sources/mapek-aware-2025.html` | unchanged (copy `sources/`) |
| `AGMS-architecture.html` | `INDEX.html` | `INDEX.html` (unchanged) |
| `AGMS-architecture.html` | `../grid-operations-and-role.html` | `grid-operations-and-role.html` |
| `INDEX.html` | `AGMS-architecture.html` | `AGMS-architecture.html` (unchanged) |
| `INDEX.html` | patent PDF body link(s) (e.g. `patent-data-management.pdf`) | `../<name>.pdf` (D-08 — resolves to `docs/*.pdf`) |

**Files to copy into `architecture/`:** the 3 HTML + `sources/flisr-distributed-fsm-2014.html` + `sources/mapek-aware-2025.html` + `AGMS-architecture.svg` (2.9 MB) + `AGMS-architecture.drawio.png` (1.6 MB).

**Dead `.md` "Quick links" (Pitfall 4):** `AGMS-architecture.html` line 261's "Quick links" references `adaptive-power.md`, `ocr.md`, etc. as inert `<code>` labels (NOT hrefs) — leave as-is (lowest effort, recommended). The only real hrefs there are `INDEX.html` (valid) and `../grid-operations-and-role.html` (rewrite per table).

**Standalone diagram (Pitfall 7):** `AGMS-architecture.svg` is referenced by **no** `<img>` in any page. Either inject `<img src="AGMS-architecture.svg">` into a figure on an architecture landing/section, OR create a tiny `architecture/diagram.html` viewer in the shared shell linked from the hub (RESEARCH recommends the viewer page). Otherwise the diagram is orphaned and HTML-02 fails.

---

### `docs/build_site.py` (NO ANALOG — greenfield)

There is **no prior Python build script** in the repo. (`summaries/intelligrid-architecture/convert_to_markdown.py` is HTML→MD, the opposite direction — reference only, not reused.) The closest reference is the HTML it must emit (the shell template above). Flagged in **No Analog Found**. The bespoke glue is: file discovery (15 notes), the shared HTML shell, function slicing, link rewriting + copy, hub generation from a manifest, and a **broken-link self-check** (HTML-01/HTML-06 acceptance gate — for every emitted href, assert the target file exists; fail loud).

---

## Shared Patterns

### Page shell (`.wrap` grid)
**Source:** `AGMS-architecture.html` lines 11, 38–56 + 34, 263–266.
**Apply to:** hub, all 15 notes, demos page, diagram viewer.
Grid `250px 1fr`, masthead `grid-column:1/-1`, sticky `nav.toc`, `main`, full-width `footer`. Already in the verbatim CSS above.

### `<head>` contract (noindex + relative stylesheets)
**Source:** RESEARCH.md per-page contract + UI-SPEC.
**Apply to:** every emitted `.html`.
```html
<meta name="robots" content="noindex,nofollow">
<link rel="stylesheet" href="{rel}/assets/site.css">
<link rel="stylesheet" href="{rel}/assets/pygments.css">
```
HTML-07 needs `noindex` in **every** page; the build's grep-for-`noindex` is an automated acceptance check.

### Callout / Juan bridge boxes
**Source:** `AGMS-architecture.html` line 59 (`.callout`), line 84 (`.juan`).
**Apply to:** notes that author `{: .callout}`/`{: .juan}` via `attr_list`, and hand-written hub/demos prose. Keep `▶ Juan` boxes (single full build — not redacted, per SPEC out-of-scope).
```html
<div class="callout"><p><strong>How to read…</strong> …</p></div>
<div class="juan"><strong>▶ Juan:</strong> …</div>
```

### MathJax offline (arithmatex generic + scoped processing)
**Source:** RESEARCH.md Pattern 1 (CITED arithmatex docs).
**Apply to:** all note pages (math) + demos page if it embeds math.
Vendor whole `node_modules/mathjax@3.2.2/es5/` tree into `docs/vendor/mathjax/` (Pitfall 2 — CHTML fonts must be present for `file://`). Use `\(`/`\[` delimiters in config, NOT raw `$`.

### Pygments build-time highlight
**Source:** RESEARCH.md Code Examples.
**Apply to:** fenced code in notes + sliced demo functions.
Generate CSS once: `pygmentize -S friendly -f html -a .highlight > docs/assets/pygments.css`. Match `css_class="highlight"` in codehilite config so note fences and demo snippets share one stylesheet.

### Footer "back to hub"
**Source:** `AGMS-architecture.html` footer (line 263) + UI-SPEC copy.
**Apply to:** every content page. Copy: `← Back to study hub` → `../index.html`.

---

## No Analog Found

Files with no close match in the codebase (planner/executor uses RESEARCH.md patterns):

| File | Role | Data Flow | Reason |
|------|------|-----------|--------|
| `docs/build_site.py` | build script | batch/transform | No prior Python build script exists; `convert_to_markdown.py` is the opposite direction (HTML→MD), reference-only. Closest reference is the HTML it emits + RESEARCH.md Patterns 1–3. |
| `docs/PUBLISH.md` | docs | static | Greenfield deploy guide; structure per RESEARCH.md GitHub-Pages section + D-06. |
| `docs/.nojekyll` / `docs/robots.txt` | config | static | Greenfield; content per RESEARCH.md (`.nojekyll` empty; robots.txt `User-agent: *` / `Disallow: /`). |
| `docs/vendor/mathjax/**` | vendored lib | static | 3rd-party vendored asset (MathJax 3.2.2 `es5/` tree), not a codebase analog. |

---

## Metadata

**Analog search scope:** `.planning/research/` (patents/ + sources/ + grid-ops), `.planning/phases/0{1..5}/notes/` and `/demo/`, `summaries/intelligrid-architecture/`.
**Files scanned:** 3 research HTML (267/268/335 lines) + 15 notes (inventory + math/table/fence profiling) + 3 demo `.py` (function boundaries) + 1 demo README (heading structure) + directory listings.
**Pattern extraction date:** 2026-06-15
