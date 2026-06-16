---
phase: quick-260616-nit
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - patents-site/index.html
  - patents-site/build.py
  - patents-site/README.md
autonomous: true
requirements: [QUICK-260616-nit]

must_haves:
  truths:
    - "patents-site/index.html is a single, fully self-contained HTML file: all CSS inline, the architecture diagram embedded as a base64 data URI, and ZERO external/network references (no http(s) links, no relative file links to .md/.html/.png/vendor)."
    - "The page opens with the full AGMS architecture diagram (the big 4885x4265 PNG) as the first content section, before any of the written notes — 'start everything by the architecture'."
    - "All written notes Parts 0 through 11 from AGMS-architecture.md are present, with their original styling preserved (callouts, '▶ Juan' notes, tables, ASCII diagrams)."
    - "The 'Quick links' annex section and its TOC entry are removed; no annex/appendix links remain."
    - "The left sidebar index is the same simple sticky TOC as the existing page, minus the annex link, plus a leading 'Architecture' entry that jumps to the diagram."
    - "The deliverable is a portable folder (patents-site/) that can be copied wholesale into another project; index.html renders correctly opened directly via file:// with networking off."
  artifacts:
    - path: "patents-site/index.html"
      provides: "Self-contained single-page patent study site: architecture diagram first, Parts 0-11 notes, simple left index, no annexes, image embedded"
      min_lines: 80
      contains: "id=\"architecture\""
    - path: "patents-site/build.py"
      provides: "Reproducible generator that derives index.html from docs/architecture/AGMS-architecture.html + the diagram PNG"
      min_lines: 40
      contains: "base64"
---

<objective>
Produce `patents-site/` — a portable folder containing a single, fully self-contained
`index.html` that Juan can copy-paste into another (already domain-wired) project and
publish, to show interviewers he read and understood the director's six-patent AGMS family.

The page:
1. opens with the big AGMS architecture diagram (PNG embedded as base64) as the first section,
2. then presents the written walkthrough Parts 0–11 (faithful to AGMS-architecture.md styling),
3. carries a simple sticky left index (Architecture + Parts 0–11) — the "Quick links" annex and
   all external/companion-file links removed so nothing dangles when copied elsewhere.

Derived reproducibly by `build.py` from the already-rendered
`docs/architecture/AGMS-architecture.html` (content base) and
`docs/architecture/AGMS-architecture.drawio.png` (diagram).
</objective>

<approach>
- Reuse the existing rendered HTML (Parts 0–11 already styled) rather than re-render from
  Markdown, guaranteeing content fidelity and preserving callout/juan/table/diagram CSS.
- Keep section cards p1..p12 (Parts 0..11); drop the intro card and the p13 "Quick links" card.
- Rewrite the intro into an interviewer-facing framing line (no companion-file links).
- Prepend an `#architecture` hero section with the embedded, click-to-zoom diagram.
- Regenerate the TOC from the kept sections; lead with "Architecture"; no annex entry.
- Strip every remaining external reference; verify zero `http`, zero relative file links.
</approach>

<decisions>
- Single self-contained file (image embedded) housed in a folder — honors both "one HTML
  self-contained" and "self-contained HTML folder"; copy the folder OR just index.html.
- Use the PNG (renders identically everywhere) over the SVG; embed once and click-to-zoom
  to full resolution (no doubling the payload).
- Include Part 0 ("What Is This Actually For?") through Part 11 — "all the notes"; exclude only
  the "Quick links" annex.
- Author at repo top-level `patents-site/` (not under docs/) because it is an artifact destined
  for a different project, decoupled from this repo's GitHub Pages site.
</decisions>
