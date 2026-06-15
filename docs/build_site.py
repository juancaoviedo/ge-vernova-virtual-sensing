#!/usr/bin/env python3
"""
build_site.py — Idempotent build script for the GE Vernova Virtual Sensing study site.

Plan 07-01 scope: note discovery, MD→HTML conversion, shared HTML shell, pygments highlight.
Plan 07-02 scope: copy research trio + sources + diagram into docs/architecture/; rewrite
                  cross-links; emit diagram.html viewer.
Later plans (07-03/04) will extend this file with demos page and hub.

Usage:
    .venv-site/bin/python docs/build_site.py
"""

import json
import pathlib
import shutil
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
# Architecture copy + link rewriting (Plan 07-02)
# ---------------------------------------------------------------------------
RESEARCH = REPO_ROOT / ".planning" / "research"

# Source paths (read-only originals — never modified)
_TRIO_SRCS = {
    "AGMS-architecture.html":     RESEARCH / "patents"  / "AGMS-architecture.html",
    "grid-operations-and-role.html": RESEARCH / "grid-operations-and-role.html",
    "INDEX.html":                 RESEARCH / "patents"  / "INDEX.html",
}
_SOURCES_SRCS = {
    "flisr-distributed-fsm-2014.html": RESEARCH / "sources" / "flisr-distributed-fsm-2014.html",
    "mapek-aware-2025.html":           RESEARCH / "sources" / "mapek-aware-2025.html",
}
_ASSET_SRCS = {
    "AGMS-architecture.svg":         RESEARCH / "patents" / "AGMS-architecture.svg",
    "AGMS-architecture.drawio.png":  RESEARCH / "patents" / "AGMS-architecture.drawio.png",
}

# Link-rewrite map — keyed by target filename, value is list of (old, new) string pairs.
# Applied to the trio + sources pages. (D-07/D-08; T-07-05)
_REWRITES: dict[str, list[tuple[str, str]]] = {
    "grid-operations-and-role.html": [
        # Flatten patents/ prefix (was 2 dirs deep; now siblings in architecture/)
        ('href="patents/AGMS-architecture.html"', 'href="AGMS-architecture.html"'),
        ('href="patents/INDEX.html"',              'href="INDEX.html"'),
        # sources/ hrefs stay unchanged — sources/ dir is copied to architecture/sources/
    ],
    "AGMS-architecture.html": [
        # Was ../grid-operations-and-role.html (relative to patents/ subdir); now sibling
        ('href="../grid-operations-and-role.html"', 'href="grid-operations-and-role.html"'),
        # href="INDEX.html" stays unchanged (already sibling)
    ],
    "INDEX.html": [
        # href="AGMS-architecture.html" stays unchanged (already sibling)
        # D-08 verified: no real <a href="...patent-*.pdf"> links in INDEX.html;
        # patent PDFs appear only inside <code> labels — no rewrite needed.
    ],
    "flisr-distributed-fsm-2014.html": [
        # Was ../patents/AGMS-architecture.html (relative to sources/ one level up)
        ('href="../patents/AGMS-architecture.html"', 'href="../AGMS-architecture.html"'),
        # href="../grid-operations-and-role.html" stays unchanged
    ],
    "mapek-aware-2025.html": [
        ('href="../patents/AGMS-architecture.html"', 'href="../AGMS-architecture.html"'),
        # href="../grid-operations-and-role.html" stays unchanged
    ],
}


def _copy_and_rewrite(src: pathlib.Path, dst: pathlib.Path, rewrites: list[tuple[str, str]]) -> None:
    """Read src HTML, apply string-replacement rewrites, write to dst."""
    text = src.read_text(encoding="utf-8")
    for old, new in rewrites:
        text = text.replace(old, new)
    dst.write_text(text, encoding="utf-8")


def build_architecture() -> None:
    """Copy research trio + source siblings + diagram assets into docs/architecture/.

    Layout:
      docs/architecture/AGMS-architecture.html
      docs/architecture/grid-operations-and-role.html
      docs/architecture/INDEX.html
      docs/architecture/sources/flisr-distributed-fsm-2014.html
      docs/architecture/sources/mapek-aware-2025.html
      docs/architecture/AGMS-architecture.svg
      docs/architecture/AGMS-architecture.drawio.png
    """
    arch_dir = DOCS / "architecture"
    arch_dir.mkdir(parents=True, exist_ok=True)
    (arch_dir / "sources").mkdir(parents=True, exist_ok=True)

    # Copy + rewrite the trio
    for fname, src in _TRIO_SRCS.items():
        dst = arch_dir / fname
        rewrites = _REWRITES.get(fname, [])
        _copy_and_rewrite(src, dst, rewrites)
        print(f"  copied+relinked  {src.relative_to(REPO_ROOT)!s:<60s}  ->  architecture/{fname}")

    # Copy + rewrite source siblings into architecture/sources/
    for fname, src in _SOURCES_SRCS.items():
        dst = arch_dir / "sources" / fname
        rewrites = _REWRITES.get(fname, [])
        _copy_and_rewrite(src, dst, rewrites)
        print(f"  copied+relinked  {src.relative_to(REPO_ROOT)!s:<60s}  ->  architecture/sources/{fname}")

    # Copy diagram assets (binary — no rewrite, use shutil.copy2)
    for fname, src in _ASSET_SRCS.items():
        dst = arch_dir / fname
        shutil.copy2(src, dst)
        print(f"  copied asset     {src.relative_to(REPO_ROOT)!s:<60s}  ->  architecture/{fname}")

    print(f"  architecture/: {len(_TRIO_SRCS)} trio + {len(_SOURCES_SRCS)} sources + {len(_ASSET_SRCS)} assets")


# ---------------------------------------------------------------------------
# Diagram viewer page (Plan 07-02)
# ---------------------------------------------------------------------------

def build_diagram_page() -> None:
    """Emit docs/architecture/diagram.html — shared-shell viewer for the AGMS SVG.

    Uses the same .wrap shell as note pages; no MathJax (no math on this page).
    Paths: ../assets/site.css, ../assets/pygments.css (one level up from architecture/).
    """
    arch_dir = DOCS / "architecture"
    arch_dir.mkdir(parents=True, exist_ok=True)

    html = textwrap.dedent("""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="robots" content="noindex,nofollow">
        <title>AGMS Architecture Diagram</title>
        <link rel="stylesheet" href="../assets/site.css">
        <link rel="stylesheet" href="../assets/pygments.css">
        </head>
        <body>
        <div class="wrap">
          <header class="masthead"><h1>AGMS Architecture Diagram</h1></header>
          <nav class="toc">
            <h2>On this page</h2>
            <a href="#diagram">AGMS reference architecture</a>
          </nav>
          <main>
            <section class="card" id="diagram">
              <h2 class="sec">AGMS reference architecture</h2>
              <p>The self-organizing grid-management platform: perceive (GWM) &rarr; reason
              (CaCSM) &rarr; orchestrate (Logistician/GWCH) &rarr; deploy autonomous scouts.
              SVG below; <a href="AGMS-architecture.drawio.png">PNG fallback</a>.</p>
              <figure>
                <img src="AGMS-architecture.svg" alt="AGMS reference architecture diagram">
                <figcaption>AGMS architecture (source: director&#x27;s patent family walkthrough).
                Crisp SVG render.</figcaption>
              </figure>
            </section>
            <footer><a href="../index.html">&larr; Back to study hub</a></footer>
          </main>
        </div>
        </body>
        </html>
        """)

    out = arch_dir / "diagram.html"
    out.write_text(html, encoding="utf-8")
    print(f"  generated         diagram viewer                                            ->  architecture/diagram.html")


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

    # Plan 07-02: copy architecture research pages + diagram viewer
    print("--- architecture copy ---")
    build_architecture()
    build_diagram_page()
    print()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nFATAL: {exc}", file=sys.stderr)
        sys.exit(1)
