# PUBLISH.md — Deploy Guide for the GE Vernova Virtual Sensing Study Site

This is a checklist a reader can follow without re-reading the codebase.
The site lives entirely in `docs/` and is served verbatim by GitHub Pages.

---

## 1. Rebuild (HTML-06)

Re-run the build any time notes or demos change:

```bash
cd <repo-root>
.venv-site/bin/python docs/build_site.py
```

The script is idempotent. One run regenerates notes, architecture pages,
demos, hub, `.nojekyll`, `robots.txt`, and then runs the link-validation +
noindex audit. It exits 0 only when zero broken links are found and every
emitted page carries `noindex`.

---

## 2. Offline Smoke Test (HTML-06)

Verify the site works at `file://` with no network before sharing or deploying.

1. **Disable networking** — airplane mode, or:
   ```bash
   nmcli networking off   # restore with: nmcli networking on
   ```
2. Open `docs/index.html` in a browser via `file://`:
   ```
   file:///home/<user>/codes/ge-vernova-virtual-sensing/docs/index.html
   ```
3. From the hub:
   - Click **AGMS Architecture Walkthrough** — page loads, cross-link to
     "Grid Operations & Director's Role" works.
   - Click **AGMS Architecture Diagram** — SVG renders inline.
   - Open 2–3 Study Notes (e.g., `kal-03-ieee738-ekf-worked-example`) —
     display equations typeset (not raw `$` or boxes). Sticky TOC works.
   - Click **Hands-On Demos** — inline figures (`ekf_line_temp.png`,
     `dc_powerflow_baddata.png`) display, highlighted code blocks render,
     "View full source" links resolve.
4. Confirm **zero broken links / 404s while fully offline**.
   Math typesets with no network (MathJax is vendored under `docs/vendor/mathjax/`).

---

## 3. Deploy to GitHub Pages from `/docs` (D-06)

Zero-config deploy — no CI/CD, no Jekyll, no build step on Pages.

1. Commit the `docs/` directory to the default branch (`main`):
   ```bash
   git add docs/
   git commit -m "chore: rebuild study site"
   git push
   ```
2. In GitHub: **Settings → Pages → Source → Deploy from a branch**
   - Branch: `main`
   - Folder: `/docs`
   - Click **Save**.
3. GitHub Pages publishes at:
   ```
   https://<username>.github.io/<repository>/
   ```
4. **`.nojekyll`** is present in `docs/` — this is required. It tells GitHub
   Pages NOT to run Jekyll, which would otherwise mangle `vendor/` and
   `_`-prefixed MathJax component paths and break offline math rendering.

---

## 4. Unlisted / noindex Sharing (HTML-07)

Every emitted page carries:

```html
<meta name="robots" content="noindex,nofollow">
```

`docs/robots.txt` also disallows all crawlers:

```
User-agent: *
Disallow: /
```

The site URL is shareable with interviewers (e.g., paste the GitHub Pages
URL), but it is **discouraged from search indexing** by both directives.

**This is unlisted-by-obscurity, not access-controlled.** Anyone who receives
the URL can view the site. Legitimate use: sharing the URL directly with a
hiring manager or interviewer.

---

## 5. Deferred Deploy-Time Privacy Decision (CONTEXT.md)

**Read this before actually enabling GitHub Pages.**

Publishing `docs/` makes everything in that directory publicly fetchable at
the site URL. This includes:

- Six patent PDFs (`patent-*.pdf`) — patents are public record; no issue.
- IEC 61850 and IntelliGrid reference PDFs — publicly available documents.
- **Juan's CV** (`Juan Carlos Oviedo Cepeda - 2026.pdf` / `.docx`) —
  a personal document. The site is `noindex`/unlisted, but the URL is
  not access-controlled.

**Before enabling Pages, decide:**

- **Accept** — the site is unlisted, `noindex`, and shared only with
  interviewers who need the CV anyway. No action required.
- **Relocate** — move the CV (and any other sensitive PDFs) out of `docs/`
  before deploying. Update any links inside the site that reference them.

This is a conscious deploy-time choice, not a build blocker. The build
does not move or delete files in `docs/`. Recorded as deferred per
`.planning/phases/07-integrated-html-study-site/07-CONTEXT.md`.
