# patents-site/ — self-contained AGMS patent study notes

A single, fully self-contained HTML page of Juan's study notes on the
director's six-patent **AGMS** (Adaptive Power Grid Management System) family —
the architecture diagram first, then the written walkthrough (Parts 0–11).

Built to share with interviewers as evidence the patents were read and understood.

## What's here

- **`index.html`** — the deliverable. One file, no dependencies:
  all CSS inline, the architecture diagram embedded as a base64 data URI,
  zero external/network references. Opens correctly via `file://` offline.
- **`build.py`** — regenerates `index.html` from the repo's rendered notes
  (`docs/architecture/AGMS-architecture.html`) and diagram
  (`docs/architecture/AGMS-architecture.drawio.png`).

## Publish it

Copy this folder (or just `index.html`) into the target project and serve it.
Because it is self-contained, no asset paths need rewriting — point a route at
`index.html` and it renders as-is. The page carries `noindex,nofollow`.

## Regenerate (only inside this repo)

```bash
python3 patents-site/build.py
```

Edit the source notes in `docs/architecture/AGMS-architecture.html` (or the
Markdown it is rendered from) and re-run, rather than hand-editing the 3 MB
generated `index.html`.
