---
phase: 07-integrated-html-study-site
plan: "04"
subsystem: docs-site
tags: [html, validation, publishing-config, nojekyll, robots-txt, noindex, publish-guide]
dependency_graph:
  requires: [plan-07-01, plan-07-02, plan-07-03]
  provides:
    - docs/build_site.py (validate_links + emit_publishing_files)
    - docs/.nojekyll
    - docs/robots.txt
    - docs/PUBLISH.md
  affects: []
tech_stack:
  added: [re (stdlib), pathlib (stdlib) — validate_links uses only stdlib]
  patterns: [fail-loud-build-gate, noindex-injection-on-copy, offline-first-validation]
key_files:
  created:
    - docs/.nojekyll
    - docs/robots.txt
    - docs/PUBLISH.md
    - .planning/phases/07-integrated-html-study-site/07-04-SUMMARY.md
  modified:
    - docs/build_site.py
    - docs/architecture/diagram.html
    - docs/architecture/AGMS-architecture.drawio.png
    - docs/index.html
    - docs/architecture/AGMS-architecture.html
    - docs/architecture/grid-operations-and-role.html
    - docs/architecture/INDEX.html
    - docs/architecture/sources/flisr-distributed-fsm-2014.html
    - docs/architecture/sources/mapek-aware-2025.html
decisions:
  - "emit_publishing_files() writes .nojekyll (empty) + robots.txt before validate_links() runs — so they are present when the gate fires"
  - "_copy_and_rewrite() now injects noindex,nofollow after the viewport meta for any copied page that lacks it — auto-fix for pre-HTML-07 research originals"
  - "validate_links() runs as the FINAL main() step — all outputs are already on disk when the gate fires; no separate validation script needed"
  - "PUBLISH.md placed in docs/ (co-located with site) per D-06 discretion — travels with the site if cloned"
  - "D-06 deferred: actual GitHub Pages enable is not done here; PUBLISH.md records the deploy-time CV/patent-PDF privacy decision explicitly"
  - "PNG primary in diagram viewer: user-exported annotated PNG (4885x4265, ~2.4MB) has faithful draw.io colors; SVG rendered with wrong colors — PNG is now the canonical embed, SVG is secondary link"
  - "Click-to-zoom: <a href=PNG target=_blank> wrapping <img> so user can inspect hand-annotations at full resolution"
metrics:
  duration_minutes: 15
  completed_date: "2026-06-15"
  tasks_completed: 3
  tasks_total: 3
  files_created: 4
  checkpoint_task: "Task 3 (checkpoint:human-verify) — APPROVED by user 2026-06-15"
---

# Phase 7 Plan 04: Publishing Config + Link-Validation Gate + Annotated Diagram PNG Summary

**One-liner:** Build-time validate_links() gate (24 pages, 0 broken links, 0 noindex-missing), .nojekyll + robots.txt + PUBLISH.md emitted, and diagram viewer upgraded to annotated PNG (draw.io export with user hand-annotations, faithful colors, click-to-zoom) — full offline navigation approved by user.

## What Was Built

### Task 1: validate_links() pass + .nojekyll + robots.txt

Extended `docs/build_site.py` with two new functions wired as the final `main()` steps:

**`emit_publishing_files()`**
- `docs/.nojekyll` — empty marker (its presence stops GitHub Pages' Jekyll from ignoring `vendor/` and `_`-prefixed MathJax component paths that are needed for offline math rendering)
- `docs/robots.txt` — `User-agent: *\nDisallow: /\n` (reinforces noindex,nofollow on all pages)

**`validate_links()`**
- Walks every `docs/**/*.html` file (24 pages on a clean build)
- Parses all `href="..."` and `src="..."` attribute values
- Skips external schemes (`http://`, `https://`, `mailto:`, `data:`, `//`) and pure anchors (`#...`)
- Strips trailing `#anchor` fragments, resolves remaining paths relative to the page's own directory
- Collects all misses, prints each as `BROKEN: {page} -> {href}`, raises `SystemExit(1)` — fail loud
- Also audits every `.html` for the string `noindex` (HTML-07); missing pages reported as `NOINDEX-MISSING`
- Uses only stdlib (`re` + `pathlib`) — no third-party deps

**Auto-fix applied (Rule 2 — missing noindex on copied pages):**

`_copy_and_rewrite()` now injects `<meta name="robots" content="noindex,nofollow">` after the viewport meta for any architecture page that lacks `noindex`. The 5 copied research pages predated HTML-07; the fix ensures all 24 emitted pages pass the HTML-07 audit.

**Negative test confirmed:** Injecting a phantom href into `docs/index.html` produces `BROKEN: index.html -> architecture/NONEXISTENT-PAGE.html` and `SystemExit(1)`. Gate is live.

**Final build output:**
```
validate_links: OK — 24 pages, 0 broken links, 0 noindex-missing
```

### Task 2: docs/PUBLISH.md

Five sections, checklist-style:

1. **Rebuild** — `.venv-site/bin/python docs/build_site.py` (idempotent; regenerates + validates)
2. **Offline smoke test (HTML-06)** — disable networking, open `docs/index.html` at `file://`, click through architecture/notes/demos, confirm typeset equations and zero 404s
3. **Deploy to GitHub Pages from /docs** — Settings → Pages → Deploy from branch → main, /docs → Save; `.nojekyll` rationale included
4. **Unlisted / noindex sharing (HTML-07)** — every page carries `noindex,nofollow` + robots.txt; unlisted-by-obscurity explanation
5. **Deferred deploy-time privacy decision** — publishing `/docs` exposes CV + patent PDFs; patents are public record; CV requires confirm-or-relocate decision before enabling Pages; recorded as conscious deferred choice per CONTEXT.md

## Acceptance Criteria Verified

| Check | Result |
|-------|--------|
| `test -f docs/.nojekyll` | PASS |
| `test ! -s docs/.nojekyll` (empty) | PASS |
| `grep -c 'Disallow: /' docs/robots.txt` >= 1 | PASS (1) |
| `grep -c 'User-agent: *' docs/robots.txt` >= 1 | PASS (1) |
| `grep -c 'def validate' docs/build_site.py` >= 1 | PASS (1) |
| `.venv-site/bin/python docs/build_site.py` exits 0 | PASS |
| All 24 pages have noindex (grep -rL noindex ... empty) | PASS |
| Negative test — broken href triggers exit 1 + BROKEN line | PASS |
| `test -f docs/PUBLISH.md` | PASS |
| `grep -ci 'github pages' docs/PUBLISH.md` >= 1 | PASS (5) |
| `grep -c '/docs' docs/PUBLISH.md` >= 1 | PASS (3) |
| `grep -c 'noindex' docs/PUBLISH.md` >= 1 | PASS (6) |
| `grep -ci 'offline' docs/PUBLISH.md` >= 1 | PASS (3) |
| `grep -ci 'file://' docs/PUBLISH.md` >= 1 | PASS (3) |
| `grep -ciE 'patent|cv|disclosure' docs/PUBLISH.md` >= 1 | PASS (4) |

## Checkpoint Status

**Task 3 (checkpoint:human-verify) — APPROVED by user (2026-06-15).**

User verified full offline navigation:
- Hub, Architecture pages, Study Notes (math typesets), Demos (result images + code) — all working
- Zero broken links, zero 404s while fully offline (file://)
- PUBLISH.md reads as a clear deploy checklist

**Feedback applied with approval:** Embed annotated PNG in diagram viewer instead of SVG (SVG rendered with wrong colors in browser). User's draw.io hand-annotations are now visible at full resolution via click-to-zoom. Fix committed in `c6c2634`.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 2 - Missing noindex on copied architecture pages]**
- **Found during:** Task 1 — first build run with validate_links() showed 5 NOINDEX-MISSING pages
- **Issue:** The 5 research HTML pages copied into `docs/architecture/` (trio + 2 sources) were authored before HTML-07 and lack the `noindex,nofollow` meta tag. The validate_links() audit caught them.
- **Fix:** Added noindex injection to `_copy_and_rewrite()` — if the copied page lacks `noindex`, inject `<meta name="robots" content="noindex,nofollow">` after the viewport meta. This is an extension of the existing copy step (not a new pass).
- **Files modified:** `docs/build_site.py`, and all 5 copied architecture pages (regenerated on next build)
- **Commit:** 75d7368

**2. [Human feedback - Diagram PNG fix at checkpoint approval]**
- **Found during:** Task 3 (checkpoint:human-verify) — user approved site but requested diagram fix
- **Issue:** `build_diagram_page()` embedded `AGMS-architecture.svg` as the primary `<img src>`; the SVG rendered with wrong colors in the browser. The user's updated draw.io file has hand-added annotations visible only in the PNG export.
- **Fix:** Updated `build_diagram_page()` to embed `AGMS-architecture.drawio.png` with responsive CSS (`max-width:100%; height:auto`), click-to-zoom `<a href=PNG target=_blank>` wrapper, and SVG as secondary link in figcaption. `build_architecture()` already copies the fresh PNG from source via `shutil.copy2` — no extra copy logic needed. Hub card copy updated too.
- **Files modified:** `docs/build_site.py`, `docs/architecture/diagram.html`, `docs/architecture/AGMS-architecture.drawio.png`, `docs/index.html`
- **Verification:** PNG embed confirmed (`grep 'img src' docs/architecture/diagram.html`); PNG size 2419307 bytes matches fresh source; full rebuild exits 0 with 0 broken links
- **Commit:** c6c2634

## Known Stubs

None — all three output files (`.nojekyll`, `robots.txt`, `PUBLISH.md`) contain real content. The site is fully wired.

## Threat Surface Scan

No new network endpoints, auth paths, or trust boundary changes.

| Flag | File | Description |
|------|------|-------------|
| (none new) | — | T-07-10/11/12 all mitigated per plan threat model |

- T-07-10 (CV/patent PDF disclosure): accepted/deferred — documented in PUBLISH.md Section 5
- T-07-11 (broken nav / tampering): mitigated — validate_links() fails build on any broken href
- T-07-12 (.nojekyll absent): mitigated — emit_publishing_files() creates it on every build run

## Self-Check: PASSED

- `docs/.nojekyll` exists and is empty: FOUND
- `docs/robots.txt` contains `Disallow: /`: FOUND
- `docs/PUBLISH.md` exists with all required sections: FOUND
- `docs/build_site.py` contains `def validate_links`: FOUND
- `docs/build_site.py` contains `def emit_publishing_files`: FOUND
- `docs/architecture/diagram.html` embeds `AGMS-architecture.drawio.png` (not SVG): FOUND
- `docs/architecture/AGMS-architecture.drawio.png` is 2419307 bytes (fresh annotated export): FOUND
- Full rebuild exits 0 with 0 broken links, 0 noindex-missing across 24 pages: CONFIRMED
- Task 1 commit 75d7368: FOUND
- Task 2 commit 3830e46: FOUND
- Diagram PNG fix commit c6c2634: FOUND
