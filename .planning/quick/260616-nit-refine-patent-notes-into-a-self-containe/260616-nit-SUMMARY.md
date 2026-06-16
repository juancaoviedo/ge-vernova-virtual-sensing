---
phase: quick-260616-nit
plan: "01"
status: complete
subsystem: patents-site
tags: [patents, agms, html, self-contained, interviewer-share, architecture-diagram]
dependency_graph:
  requires:
    - docs/architecture/AGMS-architecture.html
    - docs/architecture/AGMS-architecture.drawio.png
  provides:
    - patents-site/index.html
    - patents-site/build.py
    - patents-site/README.md
  affects: [interviewer-deliverables]
tech_stack:
  added: []
  patterns: [single-file self-contained HTML, base64-embedded image, derive-from-rendered-HTML build]
key_files:
  created:
    - patents-site/index.html
    - patents-site/build.py
    - patents-site/README.md
  modified: []
decisions:
  - "Single self-contained file (image embedded as base64) housed in a folder — honors both 'one HTML self-contained' and 'self-contained HTML folder'; copy the folder OR just index.html."
  - "Used the PNG (4885x4265, renders identically everywhere) over the 2.9MB SVG; embedded once with CSS/JS click-to-zoom so the payload is not doubled."
  - "Included Part 0 ('What Is This Actually For?') through Part 11 — 'all the notes'; excluded only the 'Quick links' annex."
  - "Authored at repo top-level patents-site/ (not docs/) because it is destined for a different, already-domain-wired project — decoupled from this repo's GitHub Pages site."
  - "Derived from the already-rendered AGMS-architecture.html rather than re-rendering Markdown, to guarantee content fidelity and preserve callout/Juan-note/table/diagram styling."
  - "Refined the notes for the standalone audience: stripped internal sibling-file breadcrumbs (e.g. '(logistician-module.md)') and all companion-file links so nothing dangles when copied elsewhere."
---

# Quick Task 260616-nit — Self-contained AGMS patent study site

## What was built

`patents-site/` — a portable folder with a single, fully self-contained
`index.html` (3.2 MB) that Juan can drop into another (already domain-wired)
project and publish, to show interviewers he read and studied the director's
six-patent AGMS family.

The page:
1. **opens with the full architecture diagram** (the 4885×4265 PNG embedded as a
   base64 data URI, click-to-zoom to full resolution) — "start everything by the
   architecture";
2. then presents the written walkthrough **Parts 0–11**, with original styling
   preserved (callouts, ▶ Juan notes, tables, ASCII diagrams);
3. carries a **simple sticky left index** — `Architecture diagram` + Part 0…Part 11 —
   with the **"Quick links" annex and every external/companion-file link removed**.

`build.py` regenerates it reproducibly from `docs/architecture/AGMS-architecture.html`
+ `…drawio.png`; `README.md` documents copy/publish/regenerate.

## Verification

- **Self-contained:** zero `href`/`src` references other than `#` anchors and the
  one embedded `data:image` URI — build script fails loud if any external ref leaks.
  Renders via `file://` with networking off.
- **Order:** section sequence is `#architecture` → `#intro` → `p1`(Part 0) → … → `p12`(Part 11).
- **Notes complete:** all 12 note sections (Parts 0–11) present; section open/close balanced (14/14).
- **No annex:** zero matches for `Quick links` / `id="p13"` / `grid-operations-and-role`.
- **TOC:** `Architecture diagram` first, then Part 0–Part 11, no annex entry.
- **Refined:** all 6 `(*.md)` internal breadcrumbs removed; `⑤ Data Management`
  keeps its `(cross-cutting)` qualifier.

## Notes / follow-ups

- The page intentionally keeps the **▶ Juan** experience-mapping notes and the
  Part 11 bridge table — they are the core "I understand the work and here's how my
  background maps" signal for interviewers.
- If Juan prefers a lighter, hand-editable file, switch `build.py` to reference the
  PNG relatively (`<img src="AGMS-architecture.drawio.png">`) and ship both files in
  the folder — one-line change; current default favors a single bulletproof file.
