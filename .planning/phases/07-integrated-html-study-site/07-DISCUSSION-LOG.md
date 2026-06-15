# Phase 7: Integrated HTML Study Site - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-06-15
**Phase:** 07-integrated-html-study-site
**Areas discussed:** Build approach, Site location & publish target, Existing HTML integration, Hub & navigation design, Demo presentation, Source-PDF handling

---

## Build approach

| Option | Description | Selected |
|--------|-------------|----------|
| Python build script | Reproducible script (python-markdown + pygments + MathJax) emitting styled pages; regenerates on note changes | ✓ |
| Hand-author each page | Manually write HTML for all 15 notes; max control, slow, drifts from source | |
| Pandoc / static-site gen | pandoc/MkDocs; not installed, new toolchain under time pressure | |

**User's choice:** Python build script
**Notes:** pygments already installed; python-markdown needs one pip install; pandoc not to be used.

---

## Site location & publish target

| Option | Description | Selected |
|--------|-------------|----------|
| docs/ at repo root | GitHub Pages serves /docs natively, zero config | ✓ (adapted) |
| site/ at repo root | Neutral folder; needs host config for GH Pages | |
| Under .planning/ | Convenient but bad for publishing | |

**User's choice:** Use `/docs` — but initially asked to rename the existing `/docs` (source PDFs) to `/data` first; then reconsidered after seeing the reference-breakage and PDF-serving implications, and chose to **keep `/docs` as-is and build the site INTO it**.
**Notes:** Keeping `/docs` preserves ~30 existing `docs/...` references and places source PDFs inside the published site so links resolve.

---

## Existing HTML integration

| Option | Description | Selected |
|--------|-------------|----------|
| Copy the set into the site | Copy AGMS-architecture.html + grid-operations-and-role.html + INDEX.html + diagram, preserving cross-links; self-contained | ✓ |
| Link in place to .planning/ | No duplication, but not self-contained and exposes .planning when published | |

**User's choice:** Copy the set into the site
**Notes:** Patent-PDF links in copied INDEX.html need relative-path fixes to resolve to /docs/*.pdf.

---

## Hub & navigation design

| Option | Description | Selected |
|--------|-------------|----------|
| Card-grid hub + per-page TOC | Landing card grid in 3 groups (Architecture / Notes / Demos); each page keeps sticky sidebar TOC | ✓ |
| Single sticky mega-TOC | One persistent sidebar listing all ~20 pages | |

**User's choice:** Card-grid hub + per-page TOC

---

## Demo presentation

| Option | Description | Selected |
|--------|-------------|----------|
| Inline images + caption | Embed result PNGs with caption; federated demo shows numeric output | ✓ |
| Link to result files | Reference results by link; lighter pages | |

| Option | Description | Selected |
|--------|-------------|----------|
| Key functions, build-time pygments | Embed core functions only, highlighted offline via pygments; full source linked | ✓ |
| Full file, runtime highlight.js | Embed entire files, client-side highlighting | |

**User's choice:** Inline images + caption; key functions with build-time pygments

---

## Source-PDF handling

| Option | Description | Selected |
|--------|-------------|----------|
| Don't publish PDFs; link to public sources | Keep PDFs local, point patent links to Google Patents | |
| Copy PDFs into the site | Self-contained but +140MB and publicly republishes patents/CV | |
| Local-only links (../data) | Works locally, breaks when published | |

**User's choice:** Resolved by keeping `/docs` as-is and building the site into it — the source PDFs already live in `/docs`, so they are served from within the site and links resolve locally. (Superseded the three options above.)
**Notes:** Privacy implication flagged — publishing `/docs` exposes patent PDFs + CV; recorded as a deploy-time decision.

---

## Claude's Discretion

- venv strategy for python-markdown (reuse `.venv-crawl` vs. new venv)
- MathJax component/version and config object
- Converted-note file-naming scheme
- Whether PUBLISH.md lives at repo root or `/docs/`
- Per-page footer / prev-next navigation niceties
- Shared-CSS delivery (single external stylesheet preferred)

## Deferred Ideas

- Actual GitHub Pages deployment (deploy later)
- Deploy-time privacy decision: publishing `/docs` exposes patent PDFs + CV
- Curated/redacted "share" build (rejected for now)
- Phase 0 / Phase 6 note content (fold in once those phases produce notes)
