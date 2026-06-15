---
phase: 07-integrated-html-study-site
plan: "01"
subsystem: docs-site
tags: [html, markdown, mathjax, pygments, build-script, offline-math]
dependency_graph:
  requires: []
  provides: [docs/build_site.py, docs/assets/site.css, docs/assets/pygments.css, docs/vendor/mathjax/, docs/notes/*.html, docs/.build_manifest.json]
  affects: [plan-07-02, plan-07-03, plan-07-04]
tech_stack:
  added: [python-markdown==3.10.2, pymdown-extensions==10.21.3, pygments==2.17.2, MathJax==3.2.2]
  patterns: [arithmatex-generic-math-safety, codehilite-pygments, single-shared-css, offline-vendored-mathjax]
key_files:
  created:
    - docs/build_site.py
    - docs/assets/site.css
    - docs/assets/pygments.css
    - docs/vendor/mathjax/tex-chtml.js
    - docs/notes/kal-03-ieee738-ekf-worked-example.html
    - docs/.build_manifest.json
  modified: []
decisions:
  - "D-02: Fresh .venv-site (not .venv-crawl) for pinned markdown/pymdown-extensions/pygments"
  - "D-03: Verbatim design-system CSS lifted from AGMS-architecture.html lines 8-35"
  - "D-13: MathJax 3.2.2 full es5/ tree vendored (incl. CHTML fonts for file:// rendering)"
  - "Slug scheme: lowercase file stem (KAL-03-ieee738-ekf-worked-example.md -> kal-03-ieee738-ekf-worked-example)"
  - "Manifest format: docs/.build_manifest.json {slug: rel_output_path}"
metrics:
  duration_minutes: 10
  completed_date: "2026-06-15"
  tasks_completed: 2
  tasks_total: 3
  files_created: 126
---

# Phase 7 Plan 01: Build Foundation & 16-Note Conversion Summary

**One-liner:** Fresh .venv-site with python-markdown/pymdown-extensions/pygments converts 16 Phase 1-5 Markdown study notes to styled offline HTML via arithmatex generic + vendored MathJax 3.2.2 es5/ tree, with shared verbatim GE Vernova design-system CSS.

## What Was Built

### Task 1: Build Environment + Stylesheets + MathJax Vendor

- **`.venv-site`** — fresh virtualenv (NOT .venv-crawl) with pinned: `markdown==3.10.2`, `pymdown-extensions==10.21.3`, `pygments==2.17.2`.
- **`docs/vendor/mathjax/`** — full MathJax 3.2.2 `es5/` tree (109 files including CHTML fonts at `output/chtml/fonts/woff-v2/`) vendored from `npm install mathjax@3.2.2`. The full tree is required for offline `file://` rendering (CHTML fonts must be co-located with `tex-chtml.js`).
- **`docs/assets/pygments.css`** — generated via `pygmentize -S friendly -f html -a .highlight`, scoped to `.highlight` class.
- **`docs/assets/site.css`** — verbatim design system (28-line `:root + rules` from `AGMS-architecture.html` lines 8–35) + INDEX.html `.meta` carry-overs + 3 additive rule sets: `.card-grid`/`.hub-card`, `figure`/`figcaption`, and `div.highlight pre` pygments host tuning.

### Task 2: build_site.py + 16 Note Conversions

**`docs/build_site.py`** module layout (for plans 07-02/03/04 extension):

```
docs/build_site.py
  ├── REPO_ROOT / DOCS / NOTES_OUT / MANIFEST_PATH  (module constants)
  ├── NOTE_GLOBS   (5 phase glob patterns)
  ├── discover_notes()  →  sorted list of .md source paths
  ├── slug_from_path()  →  lowercase file stem (slug scheme)
  ├── title_from_text() →  extract first "# H1" line
  ├── md               (singleton Markdown instance, reset() between files)
  ├── MATHJAX_HEAD     (verbatim MathJax config + defer script block)
  ├── build_note_page() →  full HTML document (head + .wrap shell)
  ├── convert_note()   →  md.convert() + md.toc + md.reset() + write HTML
  ├── write_manifest() →  JSON persist {slug: rel_path}
  └── main()           →  discover → convert loop → manifest → loud fail on error
```

**Slug naming scheme:** `{md_stem.lower()}` — e.g. `KAL-03-ieee738-ekf-worked-example.md` → `kal-03-ieee738-ekf-worked-example` → `docs/notes/kal-03-ieee738-ekf-worked-example.html`.

**Manifest format (`docs/.build_manifest.json`):**
```json
{
  "agms-patent-rehearsal-deck": "notes/agms-patent-rehearsal-deck.html",
  "fed-01-federated-vs-distributed": "notes/fed-01-federated-vs-distributed.html",
  ...
}
```
Later plans (07-02 architecture copy, 07-03 demos, 07-04 hub) extend `build_site.py` and read this manifest for hub card generation.

**MathJax vendor path:** `docs/vendor/mathjax/tex-chtml.js` (entry point), fonts at `docs/vendor/mathjax/output/chtml/fonts/woff-v2/`. All note pages reference it via `<script defer src="../vendor/mathjax/tex-chtml.js"></script>`.

**16 notes converted:**
| Slug | Title (truncated) |
|------|------------------|
| kal-01-wls-state-estimation | KAL-01: WLS / Gauss-Newton Power-System State Estimation |
| kal-02-kalman-family-kf-ekf-ukf | KAL-02: Kalman Filter Family — KF, EKF, UKF |
| kal-03-ieee738-ekf-worked-example | KAL-03: Line-Temperature EKF — IEEE 738 Worked Example |
| tvs-01-voltage-stability | TVS-01: Voltage Stability Monitoring |
| tvs-02-dc-powerflow-angle-wls | TVS-02: DC Power-Flow Angle Inference (P→θ WLS) |
| tvs-03-observability-bad-data | TVS-03: Observability & Bad-Data Detection |
| tvs-04-asset-health | TVS-04: Asset-Health Estimation |
| agms-patent-rehearsal-deck | AGMS Patent Rehearsal Deck |
| stk-01-protocol-stack | STK-01: Grid Protocol Stack |
| stk-02-iec-61850 | STK-02: IEC 61850 — GOOSE / SV / MMS |
| stk-03-messaging-orchestration | STK-03: Edge Messaging & Orchestration — NATS/K3s |
| stk-04-observability | STK-04: Observability — Prometheus, PromQL |
| stk-05-reference-architecture | STK-05: Four-Tier Reference Architecture |
| fed-01-federated-vs-distributed | FED-01: Federated vs Distributed — FedAvg/FedProx |
| fed-02-byzantine-robustness | FED-02: Byzantine Robustness — Krum, Coord-Median |
| fed-03-edge-security | FED-03: Edge Security — OTA Integrity, TPM, SPIFFE |

## Acceptance Criteria Verified

- `.venv-site/bin/python -c "import markdown, pymdownx.arithmatex, pygments"` exits 0
- `docs/vendor/mathjax/tex-chtml.js` exists; `docs/vendor/mathjax/output/chtml/fonts/` directory exists
- `grep -c '.highlight' docs/assets/pygments.css` = 70 (>= 1)
- `grep -c '--accent:#0b6e4f' docs/assets/site.css` = 1
- `.hub-card`, `figcaption`, `div.highlight pre` all present in `site.css`
- `ls docs/notes/*.html | wc -l` = 16
- KAL-03 has 193 `class="arithmatex"` spans (zero raw `$$` survive — arithmatex converted all)
- All 16 notes carry `noindex,nofollow` meta
- `tex-chtml.js` script tag present in note pages
- STK-05 has 2 `class="highlight"` code blocks (fenced code routed through pygments)
- TVS-02 has `nav class="toc"` sticky sidebar
- Re-running `build_site.py` is idempotent (verified by second run)

## Deviations from Plan

None — plan executed exactly as written.

## Checkpoint Status

**Task 3 (checkpoint:human-verify) — PENDING user verification.**

The human-verify checkpoint requires the user to:
1. Disable networking
2. Open `docs/notes/kal-03-ieee738-ekf-worked-example.html` at `file://`
3. Confirm display equations typeset (not raw `$`), subscripts render correctly, sticky TOC and masthead match existing research pages

This checkpoint cannot be auto-approved — it is a critical HTML-04 acceptance gate.

## Known Stubs

None — all 16 notes are fully converted from their Markdown source with real content.

## Threat Surface Scan

No new network endpoints, auth paths, or trust boundary changes introduced. All files are static, read-only HTML served at `file://`. Threat model T-07-01 (supply chain) mitigated: versions pinned, MathJax vendored locally. T-07-02 (noindex) satisfied: every emitted page carries `noindex,nofollow`.

## Self-Check: PASSED

- `docs/build_site.py` exists: FOUND
- `docs/assets/site.css` exists: FOUND
- `docs/assets/pygments.css` exists: FOUND
- `docs/vendor/mathjax/tex-chtml.js` exists: FOUND
- `docs/notes/kal-03-ieee738-ekf-worked-example.html` exists: FOUND
- `docs/.build_manifest.json` exists: FOUND
- Commit 613c262 (Task 1): FOUND
- Commit e9c8726 (Task 2): FOUND
