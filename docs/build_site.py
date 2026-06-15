#!/usr/bin/env python3
"""
build_site.py — Idempotent build script for the GE Vernova Virtual Sensing study site.

Plan 07-01 scope: note discovery, MD→HTML conversion, shared HTML shell, pygments highlight.
Later plans (07-02/03/04) will extend this file with architecture copy, hub, demos, publish.

Usage:
    .venv-site/bin/python docs/build_site.py
"""

import json
import pathlib
import sys
import textwrap

import markdown

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = pathlib.Path(__file__).parent.parent.resolve()
DOCS = REPO_ROOT / "docs"
NOTES_OUT = DOCS / "notes"
MANIFEST_PATH = DOCS / ".build_manifest.json"

# ---------------------------------------------------------------------------
# Note discovery — all 16 Phase 1-5 study notes (sorted order)
# ---------------------------------------------------------------------------
NOTE_GLOBS = [
    ".planning/phases/01-kalman-state-estimation/notes/*.md",
    ".planning/phases/02-transmission-virtual-sensing/notes/*.md",
    ".planning/phases/03-director-s-patents-deep-read/notes/*.md",
    ".planning/phases/04-protocols-stack-architecture/notes/*.md",
    ".planning/phases/05-federated-architectures-security/notes/*.md",
]


def discover_notes():
    """Return sorted list of source .md paths across all Phase 1-5 note dirs."""
    paths = []
    for pattern in NOTE_GLOBS:
        paths.extend(sorted(REPO_ROOT.glob(pattern)))
    return paths


def slug_from_path(md_path: pathlib.Path) -> str:
    """Derive output slug from source stem (lowercase). e.g. KAL-03-... -> kal-03-..."""
    return md_path.stem.lower()


def title_from_text(text: str) -> str:
    """Extract the H1 title (first line starting with '# ')."""
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Study Note"


# ---------------------------------------------------------------------------
# Markdown converter (Pattern 1 — arithmatex generic; math-safety path)
# Build ONE Markdown instance and md.reset() between files.
# Anti-patterns avoided:
#   - No pymdownx.highlight/superfences (two-highlighter clash)
#   - No raw $ delimiters in MathJax config
# ---------------------------------------------------------------------------
md = markdown.Markdown(
    extensions=[
        "pymdownx.arithmatex",
        "tables",
        "fenced_code",
        "codehilite",
        "toc",
        "attr_list",
        "md_in_html",
        "sane_lists",
    ],
    extension_configs={
        "pymdownx.arithmatex": {"generic": True},
        "codehilite": {"guess_lang": False, "css_class": "highlight"},
        "toc": {"toc_depth": "2-3"},
    },
)

# ---------------------------------------------------------------------------
# HTML shell builder
# ---------------------------------------------------------------------------
MATHJAX_HEAD = textwrap.dedent("""\
    <script>
    window.MathJax = {
      tex: { inlineMath: [["\\\\(","\\\\)"]], displayMath: [["\\\\[","\\\\]"]],
             processEscapes: true, processEnvironments: true },
      options: { ignoreHtmlClass: ".*", processHtmlClass: "arithmatex" }
    };
    </script>
    <script defer src="../vendor/mathjax/tex-chtml.js"></script>""")


def build_note_page(title: str, toc_html: str, html_body: str) -> str:
    """Assemble the full HTML document for a note page."""
    return textwrap.dedent(f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="robots" content="noindex,nofollow">
        <title>{title}</title>
        <link rel="stylesheet" href="../assets/site.css">
        <link rel="stylesheet" href="../assets/pygments.css">
        {MATHJAX_HEAD}
        </head>
        <body>
        <div class="wrap">
          <header class="masthead"><h1>{title}</h1></header>
          <nav class="toc"><h2>Contents</h2>{toc_html}</nav>
          <main>
        {html_body}
            <footer><a href="../index.html">&larr; Back to study hub</a></footer>
          </main>
        </div>
        </body>
        </html>
        """)


# ---------------------------------------------------------------------------
# Conversion engine
# ---------------------------------------------------------------------------

def convert_note(md_path: pathlib.Path, out_path: pathlib.Path) -> str:
    """Convert one Markdown note to HTML. Returns the slug."""
    text = md_path.read_text(encoding="utf-8")
    title = title_from_text(text)

    try:
        html_body = md.convert(text)
        toc_html = md.toc
    except Exception as exc:
        raise RuntimeError(f"could not convert: {md_path}") from exc
    finally:
        md.reset()

    page_html = build_note_page(title, toc_html, html_body)
    out_path.write_text(page_html, encoding="utf-8")
    return title


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------

def write_manifest(manifest: dict) -> None:
    """Persist {slug: relative_output_path} as docs/.build_manifest.json."""
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, sort_keys=True),
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    NOTES_OUT.mkdir(parents=True, exist_ok=True)

    note_paths = discover_notes()
    if not note_paths:
        raise RuntimeError("could not convert: no note files found — check REPO_ROOT")

    manifest: dict[str, str] = {}

    for md_path in note_paths:
        if not md_path.exists():
            raise RuntimeError(f"could not convert: {md_path} — file missing")

        slug = slug_from_path(md_path)
        out_path = NOTES_OUT / f"{slug}.html"
        rel_path = out_path.relative_to(DOCS).as_posix()

        title = convert_note(md_path, out_path)
        manifest[slug] = rel_path
        print(f"  converted  {md_path.name!s:55s}  ->  notes/{slug}.html  [{title[:40]}]")

    write_manifest(manifest)
    print(f"\n  manifest written -> {MANIFEST_PATH.relative_to(REPO_ROOT)}")
    print(f"  total: {len(note_paths)} notes converted\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nFATAL: {exc}", file=sys.stderr)
        sys.exit(1)
