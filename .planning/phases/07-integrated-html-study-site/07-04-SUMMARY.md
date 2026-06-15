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
  modified:
    - docs/build_site.py
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
metrics:
  duration_minutes: 2
  completed_date: "2026-06-15"
  tasks_completed: 2
  tasks_total: 3
  files_created: 3
  checkpoint_task: "Task 3 (checkpoint:human-verify) — awaiting user verification"
---

# Phase 7 Plan 04: Publishing Config + Link-Validation Gate Summary

**One-liner:** Build-time validate_links() pass (HTML-06 acceptance gate: 24 pages, 0 broken links, 0 noindex-missing), .nojekyll + robots.txt emitted, and PUBLISH.md deploy guide written with the deferred CV/patent-PDF privacy decision documented.

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

**Task 3 (checkpoint:human-verify) — AWAITING USER.**

The human-verify checkpoint requires the user to:
1. Disable networking
2. Open `docs/index.html` via `file://`
3. Navigate through Architecture, Study Notes (math typesets), Demos (figures + code work)
4. Confirm zero broken links and that PUBLISH.md reads as a clear deploy checklist

This checkpoint was NOT auto-approved (plan `autonomous: false`; checkpoint instructions require human action).

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 2 - Missing noindex on copied architecture pages]**
- **Found during:** Task 1 — first build run with validate_links() showed 5 NOINDEX-MISSING pages
- **Issue:** The 5 research HTML pages copied into `docs/architecture/` (trio + 2 sources) were authored before HTML-07 and lack the `noindex,nofollow` meta tag. The validate_links() audit caught them.
- **Fix:** Added noindex injection to `_copy_and_rewrite()` — if the copied page lacks `noindex`, inject `<meta name="robots" content="noindex,nofollow">` after the viewport meta. This is an extension of the existing copy step (not a new pass).
- **Files modified:** `docs/build_site.py`, and all 5 copied architecture pages (regenerated on next build)
- **Commit:** 75d7368

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
- Task 1 commit 75d7368: FOUND
- Task 2 commit 3830e46: FOUND
