---
phase: 07-integrated-html-study-site
plan: "02"
subsystem: docs-site
tags: [html, architecture, copy-not-rebuild, link-rewrite, diagram-viewer]
dependency_graph:
  requires: [plan-07-01]
  provides:
    - docs/architecture/AGMS-architecture.html
    - docs/architecture/grid-operations-and-role.html
    - docs/architecture/INDEX.html
    - docs/architecture/sources/flisr-distributed-fsm-2014.html
    - docs/architecture/sources/mapek-aware-2025.html
    - docs/architecture/AGMS-architecture.svg
    - docs/architecture/AGMS-architecture.drawio.png
    - docs/architecture/diagram.html
  affects: [plan-07-03, plan-07-04]
tech_stack:
  added: [shutil (stdlib)]
  patterns: [copy-not-rebuild, deterministic-string-rewrite, shared-wrap-shell]
key_files:
  created:
    - docs/architecture/AGMS-architecture.html
    - docs/architecture/grid-operations-and-role.html
    - docs/architecture/INDEX.html
    - docs/architecture/sources/flisr-distributed-fsm-2014.html
    - docs/architecture/sources/mapek-aware-2025.html
    - docs/architecture/AGMS-architecture.svg
    - docs/architecture/AGMS-architecture.drawio.png
    - docs/architecture/diagram.html
  modified:
    - docs/build_site.py
decisions:
  - "D-07: Research pages copied not rebuilt — build_architecture() reads originals and writes to docs/architecture/ with string rewrites"
  - "D-08 confirmed: INDEX.html contains no real PDF hrefs; patent PDFs appear only in <code> labels — no rewrite applied"
  - "Rewrite map applied exactly per PATTERNS table; verified by grep on output files before commit"
  - "Diagram viewer uses same .wrap shell as notes but omits MathJax (no math on this page)"
metrics:
  duration_minutes: 3
  completed_date: "2026-06-15"
  tasks_completed: 2
  tasks_total: 2
  files_created: 8
---

# Phase 7 Plan 02: Architecture Integration Summary

**One-liner:** AGMS research trio (3 HTML pages + 2 source siblings + SVG/PNG diagram) copied into docs/architecture/ with deterministic cross-link rewrites and a shared-shell diagram.html viewer surfacing the previously-orphaned SVG.

## What Was Built

### Task 1: Copy research trio + sources + diagram into docs/architecture/

Extended `docs/build_site.py` with two new functions (`build_architecture()`, `build_diagram_page()`) and a call to each from `main()`. Used `shutil.copy2` for binary assets (SVG/PNG) and a `_copy_and_rewrite()` helper for HTML pages.

**Architecture directory layout produced:**
```
docs/architecture/
  AGMS-architecture.html          (copied + relinked from .planning/research/patents/)
  grid-operations-and-role.html   (copied + relinked from .planning/research/)
  INDEX.html                      (copied + relinked from .planning/research/patents/)
  AGMS-architecture.svg           (binary copy, 2.9 MB)
  AGMS-architecture.drawio.png    (binary copy, 1.6 MB)
  diagram.html                    (generated viewer)
  sources/
    flisr-distributed-fsm-2014.html   (copied + relinked)
    mapek-aware-2025.html             (copied + relinked)
```

**Exact rewrites applied** (verified by grep on output files before commit):

| File | Old href | New href | Reason |
|------|----------|----------|--------|
| grid-operations-and-role.html | `href="patents/AGMS-architecture.html"` | `href="AGMS-architecture.html"` | trio flattened into architecture/ |
| grid-operations-and-role.html | `href="patents/INDEX.html"` | `href="INDEX.html"` | trio flattened |
| AGMS-architecture.html | `href="../grid-operations-and-role.html"` | `href="grid-operations-and-role.html"` | was relative to patents/ subdir |
| sources/flisr-distributed-fsm-2014.html | `href="../patents/AGMS-architecture.html"` | `href="../AGMS-architecture.html"` | patents/ subdir eliminated |
| sources/mapek-aware-2025.html | `href="../patents/AGMS-architecture.html"` | `href="../AGMS-architecture.html"` | patents/ subdir eliminated |

**Unchanged hrefs (verified):**
- `AGMS-architecture.html` → `href="INDEX.html"` (INDEX.html is a sibling — unchanged)
- `INDEX.html` → `href="AGMS-architecture.html"` (already sibling — unchanged)
- sources → `href="../grid-operations-and-role.html"` (resolves correctly from architecture/sources/)
- D-08 confirmed: INDEX.html has no real `<a href="...patent-*.pdf">` links — patent PDFs appear only inside `<code>` text labels; no rewrite invented

### Task 2: AGMS diagram viewer page

`build_diagram_page()` emits `docs/architecture/diagram.html` using the same `.wrap` grid shell as plan 07-01 note pages:
- `<meta name="robots" content="noindex,nofollow">`
- `<link rel="stylesheet" href="../assets/site.css">` / `../assets/pygments.css`
- MathJax script omitted (no math on this page — lean output)
- Inline `<img src="AGMS-architecture.svg">` with PNG fallback link (`AGMS-architecture.drawio.png`)
- Footer `← Back to study hub` → `../index.html`

The previously-orphaned SVG (Pitfall 7 from RESEARCH.md) is now reachable via `diagram.html`.

## Acceptance Criteria Verified

| Check | Result |
|-------|--------|
| `test -f docs/architecture/AGMS-architecture.html` | PASS |
| `test -f docs/architecture/grid-operations-and-role.html` | PASS |
| `test -f docs/architecture/INDEX.html` | PASS |
| `test -f docs/architecture/sources/flisr-distributed-fsm-2014.html` | PASS |
| `test -f docs/architecture/sources/mapek-aware-2025.html` | PASS |
| `test -f docs/architecture/AGMS-architecture.svg` | PASS |
| `test -f docs/architecture/AGMS-architecture.drawio.png` | PASS |
| `grep -c 'href="patents/' grid-operations-and-role.html` == 0 | PASS (0) |
| `grep -c 'href="AGMS-architecture.html"' grid-operations-and-role.html` >= 1 | PASS (3) |
| `grep -c 'href="../grid-operations-and-role.html"' AGMS-architecture.html` == 0 | PASS (0) |
| `grep -c 'href="grid-operations-and-role.html"' AGMS-architecture.html` >= 1 | PASS (2) |
| `grep -c 'href="../patents/' sources/mapek-aware-2025.html` == 0 | PASS (0) |
| `test -f docs/architecture/diagram.html` | PASS |
| `grep -cE '<img[^>]*src="AGMS-architecture.svg"' diagram.html` >= 1 | PASS (1) |
| `grep -c 'AGMS-architecture.drawio.png' diagram.html` >= 1 | PASS (1) |
| `grep -c 'noindex' diagram.html` >= 1 | PASS (1) |
| `grep -c '../index.html' diagram.html` >= 1 | PASS (1) |

## Hub (Plan 07-04) Link Reference

The hub page (plan 07-04) should link to these pages in the Architecture section:

| Card title | href (relative to docs/) |
|-----------|--------------------------|
| AGMS Architecture Walkthrough | `architecture/AGMS-architecture.html` |
| Grid Operations & Role | `architecture/grid-operations-and-role.html` |
| Patent Family Index | `architecture/INDEX.html` |
| AGMS Diagram Viewer | `architecture/diagram.html` |

## Deviations from Plan

None — plan executed exactly as written. Both tasks were added to `docs/build_site.py` in a single edit and committed together (inseparable — both functions share the same build run).

## Known Stubs

None — all architecture pages contain real content from the source research HTML.

## Threat Surface Scan

No new network endpoints, auth paths, or trust boundary changes. Architecture pages are static HTML served at `file://`. Threat T-07-05 (link-integrity) mitigated by the deterministic string-replacement rewrite map verified by grep before commit. T-07-04 (noindex) satisfied on `diagram.html`; the three copied pages retain their own `<head>` noindex tags from the originals.

## Self-Check: PASSED

- `docs/architecture/AGMS-architecture.html`: FOUND
- `docs/architecture/grid-operations-and-role.html`: FOUND
- `docs/architecture/INDEX.html`: FOUND
- `docs/architecture/sources/flisr-distributed-fsm-2014.html`: FOUND
- `docs/architecture/sources/mapek-aware-2025.html`: FOUND
- `docs/architecture/AGMS-architecture.svg`: FOUND
- `docs/architecture/AGMS-architecture.drawio.png`: FOUND
- `docs/architecture/diagram.html`: FOUND
- `docs/build_site.py` (modified): FOUND
- Commit b312dcc (Tasks 1+2): FOUND
