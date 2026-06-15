---
phase: 07-integrated-html-study-site
reviewed: 2026-06-15T00:00:00Z
depth: standard
files_reviewed: 1
files_reviewed_list:
  - docs/build_site.py
findings:
  critical: 0
  warning: 6
  info: 5
  total: 11
status: issues_found
---

# Phase 7: Code Review Report

**Reviewed:** 2026-06-15
**Depth:** standard
**Files Reviewed:** 1 (`docs/build_site.py`, 982 lines)
**Status:** issues_found

## Summary

`build_site.py` is a single-file, top-to-bottom build script with clear structure, good
docstrings, and a genuine fail-loud `validate_links()` gate. The happy-path build is
sound and the link-rewrite map was verified against the actual research HTML sources
(all five rewrite entries match real hrefs; no dead rewrites). No security vulnerabilities
were found — there is no `eval`, no shell, no untrusted network input, and all file I/O is
to repo-local paths.

However, this site is shareable with interviewers, and several defects will either produce
**silently-wrong-but-passing builds** or **invalid HTML** on a clean rebuild. The most
serious are: (1) note titles are injected into templates with **no HTML escaping** while at
least four real titles contain a literal `&`, producing malformed `<title>`/`<h1>` markup;
(2) the build **never cleans stale output**, so a deleted or renamed source note leaves an
orphan HTML page that `validate_links()` will happily pass; and (3) `validate_links()` has a
**false-pass hole** — it only checks `href`/`src` attributes, so a broken link expressed any
other way (or a missing fragment target) is never caught, and its `errors="replace"` read can
mask encoding problems. None rise to BLOCKER given the offline, single-author, trusted-input
context, but the WARNINGs below are real correctness/robustness issues that can embarrass on a
fresh checkout.

## Warnings

### WR-01: Note titles injected into HTML without escaping — malformed markup on real inputs

**File:** `docs/build_site.py:62-67, 109-134, 141-156`
**Issue:** `title_from_text()` returns the raw H1 text (a plain string slice, no escaping).
`build_note_page()` then interpolates it directly into both `<title>{title}</title>` and
`<h1>{title}</h1>` via an f-string. Several real note H1s contain characters that are
significant in HTML — confirmed in source:

- `# TVS-03: Observability & Bad-Data Detection`
- `# STK-02: IEC 61850 — GOOSE / SV / MMS, Hierarchy & Logical Nodes`
- `# STK-03: Edge Messaging & Orchestration — NATS/MQTT/Kafka, K3s/K8s`
- `# FED-01: Federated vs Distributed — FedAvg, FedProx & Non-IID`

A raw `&` in `<title>` is an unescaped ampersand (invalid HTML; browsers may render
`& Bad-Data` literally but it is malformed, and an `&word;` sequence could be mis-parsed as
an entity). A future title containing `<` or `>` would break the page outright. This is a
correctness defect that triggers on already-present content, not a hypothetical.

**Fix:** Escape the title before interpolation. Note the body HTML and TOC come from Markdown
and must NOT be escaped, so escape only the title:
```python
import html

def convert_note(md_path, out_path):
    text = md_path.read_text(encoding="utf-8")
    title = html.escape(title_from_text(text))   # escape for <title>/<h1>
    ...
```
The hub-card titles (`_ARCH_CARDS`, `_NOTE_GROUPS`) are already hand-escaped (`&amp;`,
`&#x27;`), so the inconsistency is isolated to note-page titles and the hub note-card
`readable` text (see WR-02).

### WR-02: Hub note-card title (`readable`) also unescaped + lossy slug round-trip

**File:** `docs/build_site.py:736-740`
**Issue:** `readable = slug.replace("-", " ").title()` is injected into the hub card
`<p>{readable}</p>` without escaping. While current slugs are ASCII-only (so no escaping
bug fires today), the derived title is also lossy and wrong: `kal-03-ieee738-ekf-worked-example`
becomes `Kal 03 Ieee738 Ekf Worked Example` — the real H1 (`KAL-03: Line-Temperature EKF —
IEEE 738 Worked Example`) is already captured in the per-note conversion but is thrown away
and not stored in the manifest. The hub therefore shows mangled, low-quality titles to the
interviewer despite the correct title being available at build time.

**Fix:** Store the real title in the manifest during conversion and use it for the hub card:
```python
# in main(): manifest[slug] = {"path": rel_path, "title": title}
# in build_hub(): readable = html.escape(note_entries[slug]["title"])
```
(If you keep the flat `{slug: path}` manifest, at minimum `html.escape(readable)` to remove
the latent escaping bug.)

### WR-03: No stale-output cleanup — deleted/renamed notes leave orphan pages; build is not truly idempotent

**File:** `docs/build_site.py:927-950` (and `build_architecture`, `build_demos`)
**Issue:** The script is described as "idempotent," but it only ever writes/overwrites; it
never removes outputs whose source disappeared. If a note `.md` is deleted or renamed, the
old `docs/notes/<old-slug>.html` remains on disk. It is dropped from the manifest (so the hub
no longer links it), but it still exists and is still scanned by `validate_links()`. Worse, if
that orphan page references an asset that was also removed, validation could fail on a file the
current build doesn't even produce — or, more commonly, the orphan silently lingers and ships
to interviewers. This makes "clean rebuild" non-deterministic with respect to history.

**Fix:** Clear generated output dirs at the start of the run before regenerating:
```python
def main():
    for d in (NOTES_OUT, DOCS / "architecture", DOCS / "demos"):
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True, exist_ok=True)
    ...
```
(Be careful to only remove fully-generated dirs, not `docs/assets` or `docs/vendor` if those
are produced by a separate step.)

### WR-04: `validate_links()` only inspects href/src attributes and never validates `#` fragment targets — false-pass hole

**File:** `docs/build_site.py:876, 894-908`
**Issue:** The validator regex matches only `href=`/`src=` attributes and explicitly *skips*
all pure-anchor links (`if raw.startswith("#"): continue`) and strips fragments before
resolving (`href = raw.split("#")[0]`). Consequences:
1. Pages emit in-page nav anchors (`<a href="#diagram">`, `<a href="#ekf">`, `<a href="#dc">`,
   `<a href="#fed">`, `#architecture`, `#notes`, `#demos`). None of these fragment targets are
   ever verified to exist. A typo in an `id=` or a renamed section would pass validation and
   ship a dead in-page jump link. This directly undercuts the HTML-06 "no broken links" intent.
2. Links expressed via anything other than `href`/`src` (e.g. CSS `url(...)`, `<link>` with
   different attr ordering edge cases, MathJax loader paths) are not checked. The MathJax
   `<script defer src="../vendor/mathjax/tex-chtml.js">` *is* an `src` and will be checked —
   good — but its transitive component loads are not.

The gate therefore advertises stronger guarantees than it delivers.

**Fix:** At minimum, collect every `id="..."`/`name="..."` per page and validate that each
`#fragment` (both pure-anchor and the stripped fragment of a same-page link) resolves to an
id in the target page. Document explicitly that only `href`/`src` are scanned so future
maintainers don't over-trust the gate.

### WR-05: `validate_links()` reads with `errors="replace"`, masking encoding corruption

**File:** `docs/build_site.py:882`
**Issue:** Every other read in the file uses `read_text(encoding="utf-8")` (strict), but the
validator uses `read_text(encoding="utf-8", errors="replace")`. If a copied research page or a
generated page contains malformed UTF-8, the validator silently substitutes U+FFFD and reports
"OK" instead of surfacing the corruption. For a "fail loud" acceptance gate, silently repairing
the input it is auditing is the wrong default and can hide a genuinely broken artifact.

**Fix:** Use strict decoding so the gate fails on corrupt output:
```python
text = page.read_text(encoding="utf-8")  # let a UnicodeDecodeError fail the build loud
```

### WR-06: `_slice_function` AST branch misses `async def` and nested targets; regex fallback can mis-slice

**File:** `docs/build_site.py:375-398`
**Issue:** Two robustness gaps in the function slicer:
1. The AST walk matches only `ast.FunctionDef`. An `async def` is an `ast.AsyncFunctionDef`
   and would not be found, falling through to the `ValueError`. The current target functions
   are all plain `def` (verified), so this does not fire today, but it is a latent trap for any
   future async demo helper.
2. `ast.walk` matches by name anywhere in the tree (including methods inside a class or nested
   functions), so a name collision would slice the wrong definition. Acceptable for the current
   flat demo files, but worth a guard.
3. The regex fallback pattern uses `\\Z` inside a raw string. In a raw string `r"...\\Z"` is the
   two characters backslash-Z, not the regex end-of-string anchor `\Z`. The intended terminator
   is broken; the fallback relies entirely on `^def /^class /^if __name__` lookaheads and would
   over-capture to EOF for the last function in a file that has none of those trailing markers.
   The fallback only runs on a `SyntaxError` (unparseable demo), so it is unlikely to trigger,
   but the anchor bug is real.

**Fix:**
```python
if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == func_name:
```
and in the fallback use a non-raw escape or fix the anchor: `... |\Z)` (single backslash) so
end-of-string actually anchors. Optionally restrict the AST search to `tree.body` for top-level
only.

## Info

### IN-01: Manifest key collision risk between note prefix and architecture group

**File:** `docs/build_site.py:694-705, 717-721`
**Issue:** The note `AGMS-patent-rehearsal-deck.md` produces slug prefix `AGMS`, which is also
the conceptual name of the architecture group. The grouping logic keys notes off the first
hyphen segment, so this note correctly lands in `_NOTE_GROUPS` "Phase 3 — Director's Patents"
(verified). No actual collision occurs because `note_entries` is filtered to `notes/` paths
only. Flagging as awareness: the prefix-as-group scheme is fragile — a future note whose stem
starts with `KAL`/`TVS`/etc. is fine, but any note without a recognized prefix is silently
dropped from the hub (the `if not group_slugs: continue` only skips empty *known* groups; an
unknown-prefix note never appears in any group and is never reported).

**Fix:** After grouping, assert that every `note_entries` slug landed in some group, else print
a warning listing the orphaned slugs.

### IN-02: `print` calls embedded throughout mix logging with logic; no `--quiet`/`--check` mode

**File:** `docs/build_site.py` (throughout)
**Issue:** Build progress is emitted via bare `print`. Fine for a CLI build tool, but there is
no separation between progress output and the structured validation report, and no flag to run
validation-only (useful for CI re-checks without regenerating). Minor maintainability note.
**Fix:** Optional — route progress through `logging` and gate behind a verbosity flag.

### IN-03: Hardcoded demo function names and asset lists duplicated across copy + slice steps

**File:** `docs/build_site.py:416-441`
**Issue:** Demo source filenames are listed once in `_DEMO_COPIES` and again implicitly in the
slice calls (`_DEMO_SRCS["ekf"] / "ekf_line_temp_demo.py"`, etc.). A rename requires editing two
places. Magic strings (function names to slice) are inline. Low risk given the file's stability.
**Fix:** Define a single per-demo data structure (path, png, functions-to-slice) and iterate.

### IN-04: `discover_notes()` silently tolerates a glob matching zero files per phase

**File:** `docs/build_site.py:49-54, 930-932`
**Issue:** The only guard is "no notes found at all" (total == 0). If one phase's note dir is
empty or its path drifts, that phase is silently skipped and the build still passes with fewer
than the expected 16 notes. The site would ship missing a whole phase without any error.
**Fix:** Optionally assert an expected count or warn when any individual `NOTE_GLOBS` entry
matches zero files.

### IN-05: Stale/typo'd `print` f-strings without interpolation

**File:** `docs/build_site.py:360, 845, 849`
**Issue:** Several `print(f"...")` calls use the `f` prefix but contain no `{}` placeholders
(e.g. line 360, 845, 849). Harmless, but the `f` is dead and a linter will flag it.
**Fix:** Drop the `f` prefix on those literals.

---

_Reviewed: 2026-06-15_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: standard_
