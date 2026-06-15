#!/usr/bin/env python3
"""
build_site.py — Idempotent build script for the GE Vernova Virtual Sensing study site.

Plan 07-01 scope: note discovery, MD→HTML conversion, shared HTML shell, pygments highlight.
Plan 07-02 scope: copy research trio + sources + diagram into docs/architecture/; rewrite
                  cross-links; emit diagram.html viewer.
Plan 07-03 scope: demos page (build_demos()) and card-grid hub index.html (build_hub()).
Plan 07-04 scope: emit .nojekyll + robots.txt; build-time link-validation + noindex audit
                  (HTML-06/HTML-07 acceptance gate — fails loud on first miss).

Usage:
    .venv-site/bin/python docs/build_site.py
"""

import ast
import html
import json
import pathlib
import re
import shutil
import sys
import textwrap

import markdown
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer

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
    # Escape the title for safe injection into <title>/<h1> (note H1s contain '&', etc.)
    title = html.escape(title)
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


_NOINDEX_META = '<meta name="robots" content="noindex,nofollow">'

def _copy_and_rewrite(src: pathlib.Path, dst: pathlib.Path, rewrites: list[tuple[str, str]]) -> None:
    """Read src HTML, apply string-replacement rewrites, inject noindex if absent, write to dst.

    HTML-07: every emitted page must carry noindex,nofollow.  Architecture pages are
    copied from research originals that predate this requirement; inject the tag after
    the viewport meta if not already present.
    """
    text = src.read_text(encoding="utf-8")
    for old, new in rewrites:
        text = text.replace(old, new)
    # Inject noindex meta if absent (HTML-07 — copied pages may not carry it)
    if "noindex" not in text:
        text = text.replace(
            '<meta name="viewport" content="width=device-width, initial-scale=1">',
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            + _NOINDEX_META,
        )
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
    """Emit docs/architecture/diagram.html — shared-shell viewer for the AGMS architecture PNG.

    Uses the same .wrap shell as note pages; no MathJax (no math on this page).
    Paths: ../assets/site.css, ../assets/pygments.css (one level up from architecture/).

    Embeds the annotated PNG (AGMS-architecture.drawio.png, ~4885x4265 px, includes
    user hand-annotations).  The PNG is faithful to the original draw.io colors.
    The image is wrapped in a click-to-zoom link (<a target="_blank">) and styled
    responsively (max-width:100%; height:auto) so it fits any viewport.
    The SVG remains in architecture/ as an alternate; a secondary link is provided.
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
        <style>
        .diagram-figure img {
          max-width: 100%;
          height: auto;
          display: block;
          border: 1px solid #ddd;
          border-radius: 4px;
        }
        .diagram-figure figcaption {
          margin-top: 0.5em;
          font-size: 0.875em;
          color: #555;
        }
        </style>
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
              Click the image to open full-size (4885&times;4265 px) in a new tab &mdash;
              annotations are visible at full zoom.</p>
              <figure class="diagram-figure">
                <a href="AGMS-architecture.drawio.png" target="_blank" rel="noopener">
                  <img src="AGMS-architecture.drawio.png"
                       alt="AGMS architecture diagram (with annotations)">
                </a>
                <figcaption>AGMS architecture (source: director&#x27;s patent family walkthrough,
                with hand-added study annotations). PNG exported from draw.io — faithful colors.
                Also available: <a href="AGMS-architecture.svg">vector SVG</a>.</figcaption>
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
# Demo page builder (Plan 07-03)
# ---------------------------------------------------------------------------

# Demo source roots
_DEMO_SRCS = {
    "ekf": REPO_ROOT / ".planning/phases/01-kalman-state-estimation/demo",
    "dc":  REPO_ROOT / ".planning/phases/02-transmission-virtual-sensing/demo",
    "fed": REPO_ROOT / ".planning/phases/05-federated-architectures-security/demo",
}


def _slice_function(py_path: pathlib.Path, func_name: str) -> str:
    """Return the source text of a single top-level function from a .py file.

    Uses ast to find the exact line range, then falls back to a regex approach
    if ast cannot parse.  Returns only the named function — not the whole file (D-11).
    """
    source = py_path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == func_name:
                lines = source.splitlines()
                return "\n".join(lines[node.lineno - 1 : node.end_lineno])
        raise ValueError(f"function {func_name!r} not found in {py_path.name}")
    except SyntaxError:
        # Fallback: regex from ^def <name>( to next ^def /^class /^if __name__
        pattern = re.compile(
            r"^def " + re.escape(func_name) + r"\b.*?(?=^def |^class |^if __name__|\\Z)",
            re.MULTILINE | re.DOTALL,
        )
        m = pattern.search(source)
        if m:
            return m.group(0).rstrip()
        raise ValueError(f"function {func_name!r} not found in {py_path.name} (regex fallback)")


def _highlight_snippet(code: str) -> str:
    """Return pygments-highlighted HTML for a Python snippet (cssclass='highlight')."""
    return highlight(code, PythonLexer(), HtmlFormatter(cssclass="highlight"))


def build_demos() -> None:
    """Copy demo assets into docs/demos/ and emit docs/demos/index.html.

    Per-demo: README-sourced prose + inline result (PNG figure or numeric table)
    + pygments-highlighted key functions only (D-11) + full-source link (D-10/D-12).
    """
    demos_dir = DOCS / "demos"
    demos_dir.mkdir(parents=True, exist_ok=True)

    # ---- 1. Copy demo source files and result PNGs into docs/demos/ ----
    _DEMO_COPIES = [
        (_DEMO_SRCS["ekf"] / "ekf_line_temp_demo.py",     demos_dir / "ekf_line_temp_demo.py"),
        (_DEMO_SRCS["ekf"] / "ekf_line_temp.png",         demos_dir / "ekf_line_temp.png"),
        (_DEMO_SRCS["dc"]  / "dc_powerflow_baddata_demo.py", demos_dir / "dc_powerflow_baddata_demo.py"),
        (_DEMO_SRCS["dc"]  / "dc_powerflow_baddata.png",  demos_dir / "dc_powerflow_baddata.png"),
        (_DEMO_SRCS["fed"] / "fedavg_fedprox_krum_demo.py", demos_dir / "fedavg_fedprox_krum_demo.py"),
    ]
    for src, dst in _DEMO_COPIES:
        shutil.copy2(src, dst)
        print(f"  copied demo asset  {src.name}")

    # ---- 2. Slice and highlight key functions (D-11 — key functions only) ----
    # Demo 1: EKF — ekf_step only (the predict-update cycle)
    ekf_py = _DEMO_SRCS["ekf"] / "ekf_line_temp_demo.py"
    ekf_step_html = _highlight_snippet(_slice_function(ekf_py, "ekf_step"))

    # Demo 2: DC power-flow — wls_solve + chi2_test + normalized_residuals
    dc_py = _DEMO_SRCS["dc"] / "dc_powerflow_baddata_demo.py"
    wls_solve_html      = _highlight_snippet(_slice_function(dc_py, "wls_solve"))
    chi2_test_html      = _highlight_snippet(_slice_function(dc_py, "chi2_test"))
    norm_resid_html     = _highlight_snippet(_slice_function(dc_py, "normalized_residuals"))

    # Demo 3: FedAvg/Krum — fedavg_aggregate + krum_select
    fed_py = _DEMO_SRCS["fed"] / "fedavg_fedprox_krum_demo.py"
    fedavg_agg_html = _highlight_snippet(_slice_function(fed_py, "fedavg_aggregate"))
    krum_html       = _highlight_snippet(_slice_function(fed_py, "krum_select"))

    # ---- 3. Emit docs/demos/index.html ----
    html = textwrap.dedent(f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="robots" content="noindex,nofollow">
        <title>Hands-On Demos — GE Vernova Virtual Sensing Study Site</title>
        <link rel="stylesheet" href="../assets/site.css">
        <link rel="stylesheet" href="../assets/pygments.css">
        </head>
        <body>
        <div class="wrap">
          <header class="masthead">
            <h1>Hands-On Demos</h1>
            <div class="meta">Three from-scratch NumPy demos — EKF line temperature, DC
            power-flow bad-data detection, and federated learning robustness.</div>
          </header>
          <nav class="toc">
            <h2>Contents</h2>
            <a href="#ekf">1. EKF Line Temperature</a>
            <a href="#dc">2. DC Power-Flow Bad-Data</a>
            <a href="#fed">3. Federated Learning</a>
          </nav>
          <main>

        <!-- ================================================================
             Demo 1: EKF Line Temperature
             ================================================================ -->
        <section class="card" id="ekf">
          <h2 class="sec">1. EKF Line-Temperature / Dynamic Line Rating</h2>

          <h3 class="sub">What it is</h3>
          <p>A from-scratch <strong>Extended Kalman Filter (EKF)</strong> — NumPy/SciPy only,
          no external KF library — that estimates overhead conductor temperature from simulated
          current telemetry, demonstrating the core idea behind <strong>Dynamic Line Rating
          (DLR)</strong> virtual sensing.</p>

          <h3 class="sub">Why it was built (interview gap it closes)</h3>
          <p>The role requires virtual-sensing experience: inferring unmeasured physical
          quantities from indirect measurements.  This demo shows the EKF predict-update
          loop applied to a conductor thermal model — the same first-order thermal ODE
          structure used in building energy management (Juan's OSED work), just with Drake
          ACSR parameters instead of building RC parameters.</p>
          <div class="juan"><strong>&#9658; Juan:</strong> The bridge story: <em>"My OSED
          building thermal model is <code>C&middot;dT/dt = Q_HVAC &minus; UA&middot;(T&minus;Ta)</code>
          — structurally identical to the IEEE&nbsp;738 conductor ODE.  Swapping building RC
          parameters for Drake ACSR parameters is a parameter substitution, not a conceptual
          leap."</em></div>

          <h3 class="sub">What it demonstrates</h3>
          <ul>
            <li>Simulates a Drake ACSR conductor heating up as current ramps 400&nbsp;A&nbsp;&rarr;&nbsp;600&nbsp;A over one hour using the <strong>IEEE&nbsp;738 thermal ODE</strong> as the physics engine.</li>
            <li>Generates noisy apparent-resistance measurements (<code>z&nbsp;=&nbsp;R25&middot;(1&nbsp;+&nbsp;&alpha;&middot;(Tc&minus;25))</code>) mimicking current + voltage-drop observations.</li>
            <li>Runs the <strong>EKF predict-update loop</strong> — IEEE&nbsp;738 ODE as the predict step; resistance model as the update step.</li>
            <li>Computes a <strong>Dynamic Line Rating ampacity</strong> at the estimated temperature, showing available capacity vs. the 75&nbsp;&deg;C thermal limit.</li>
            <li>Monitors filter health via a <strong>Normalized Innovation Squared (NIS) / chi-squared gate</strong> — only 0.3&nbsp;% of steps trigger (well below the expected 5&nbsp;% false-alarm rate).</li>
          </ul>

          <figure>
            <img src="ekf_line_temp.png"
                 alt="EKF line-temperature estimation: three-subplot figure showing true Tc vs EKF estimate with uncertainty band, innovation sequence, and posterior uncertainty convergence">
            <figcaption>EKF output: true conductor temperature vs estimate with &plusmn;2&sigma;
            band (top), innovation sequence (middle), and posterior uncertainty showing rapid
            convergence from &plusmn;10&nbsp;&deg;C to &lt;0.2&nbsp;&deg;C (bottom).</figcaption>
          </figure>

          <h3 class="sub">Key function: <code>ekf_step</code></h3>
          <p>One complete predict-update cycle (scalar state).  The IEEE&nbsp;738 ODE is the
          predict step; the apparent-resistance model is the update step.</p>
        <!-- embedded: def ekf_step -->
        {ekf_step_html}

          <p><a href="ekf_line_temp_demo.py">View full source &rarr;</a></p>
        </section>

        <!-- ================================================================
             Demo 2: DC Power-Flow Bad-Data Detection
             ================================================================ -->
        <section class="card" id="dc">
          <h2 class="sec">2. DC Power-Flow Bad-Data Detection</h2>

          <h3 class="sub">What it is</h3>
          <p>A from-scratch <strong>Weighted-Least-Squares (WLS) state estimator</strong>
          for a 3-bus DC power-flow network — NumPy/SciPy only, no power-flow library —
          that infers bus voltage angles from a redundant measurement set, then
          <strong>detects and removes a single corrupted measurement</strong> using the
          chi-squared test and the largest normalized residual.</p>

          <h3 class="sub">Why it was built (interview gap it closes)</h3>
          <p>The role names state estimation and bad-data detection as core competencies.
          This demo is the textbook TVS-02&nbsp;+&nbsp;TVS-03 illustration: the DC model
          <code>h(&theta;)&nbsp;=&nbsp;H&theta;</code> is linear, so the Gauss-Newton
          iteration from Phase&nbsp;1 collapses to a single normal-equations solve
          — demonstrating the same WLS machinery Juan already uses, now applied to a
          grid power network.</p>

          <h3 class="sub">What it demonstrates</h3>
          <ul>
            <li>Builds a <strong>3-bus DC network</strong> and solves the reduced power flow for ground-truth angles.</li>
            <li>Estimates two voltage angles via <strong>one-shot linear WLS</strong> from 5 redundant measurements (injections + line flows).</li>
            <li>Injects a <strong>gross error (+15&sigma;)</strong> on the line-flow 2&rarr;3 measurement.</li>
            <li>Runs the <strong>chi-squared test</strong> (<em>J&nbsp;=&nbsp;176.7 vs threshold&nbsp;7.8</em>) to detect bad data.</li>
            <li>Uses the <strong>largest normalized residual</strong> (<em>rN&nbsp;=&nbsp;13.2 on measurement&nbsp;5</em>) to identify the culprit.</li>
            <li><strong>Removes the suspect and re-solves</strong>: <em>J&nbsp;=&nbsp;1.8</em>, angles within 7&times;10<sup>&minus;4</sup>&nbsp;rad of truth.</li>
          </ul>

          <figure>
            <img src="dc_powerflow_baddata.png"
                 alt="DC power-flow bad-data detection: normalized residuals bar chart with flagged measurement highlighted in red (left), true vs estimated angles before and after bad-data removal (right)">
            <figcaption>Bad-data detection output: normalized residuals with the 3&sigma; line
            and flagged measurement #5 in red (left); true vs estimated angles before/after
            bad-data removal (right).</figcaption>
          </figure>

          <h3 class="sub">Key functions</h3>
          <p><strong><code>wls_solve</code></strong> — one-shot linear WLS (the linear
          collapse of KAL-01's normal equations):</p>
        {wls_solve_html}

          <p><strong><code>chi2_test</code></strong> — detection: is there bad data?</p>
        {chi2_test_html}

          <p><strong><code>normalized_residuals</code></strong> — identification: which
          measurement is the culprit?</p>
        {norm_resid_html}

          <p><a href="dc_powerflow_baddata_demo.py">View full source &rarr;</a></p>
        </section>

        <!-- ================================================================
             Demo 3: Federated Learning — FedAvg / FedProx / Byzantine Robustness
             ================================================================ -->
        <section class="card" id="fed">
          <h2 class="sec">3. Federated Learning — FedAvg / FedProx / Byzantine Robustness</h2>

          <h3 class="sub">What it is</h3>
          <p>A from-scratch implementation of <strong>FedAvg</strong>, <strong>FedProx</strong>
          (proximal regularization), <strong>Krum</strong>, and <strong>coordinate-wise
          median</strong> entirely in NumPy — no Flower, no PySyft, no framework
          dependency.  Six simulated substations with non-IID data distributions demonstrate
          client drift, FedProx's proximal damping, and Byzantine-robust aggregation.</p>

          <h3 class="sub">Why it was built (interview gap it closes)</h3>
          <p>The role names <em>"federated control frameworks"</em> and edge-ML expertise.
          This demo shows FedAvg aggregation math, the proximal term that keeps substation
          models tethered to the global fleet model, and Krum's distance-based rejection of
          a poisoned client — all the algorithmic pieces that underpin a production federated
          virtual-sensing system without ever shipping raw telemetry.</p>

          <h3 class="sub">What it demonstrates</h3>
          <ul>
            <li><strong>Non-IID clients:</strong> six substations with different local data distributions (feeder means 0.0&nbsp;&hellip;&nbsp;2.5).</li>
            <li><strong>FedAvg convergence</strong> over 20 communication rounds: <em>weighted average w&nbsp;=&nbsp;&sum;(n_k/n)&middot;w_k</em>.</li>
            <li><strong>FedProx damps client drift:</strong> proximal term +(&mu;/2)&Vert;w&minus;w_t&Vert;&sup2; lives in the <em>client's local objective</em> (not the server aggregation — a common interview pitfall).</li>
            <li><strong>Byzantine injection:</strong> client&nbsp;0 sends a poisoned update (shift &minus;5.0). Plain FedAvg averages the poison in; Krum and coordinate-wise median reject it.</li>
          </ul>

          <h3 class="sub">Key numeric output (seed&nbsp;42, reproducible)</h3>
          <table>
            <thead>
              <tr>
                <th>Method</th>
                <th>Final estimate</th>
                <th>Error vs true optimum (1.22)</th>
                <th>Notes</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Plain FedAvg</td>
                <td>+0.5826</td>
                <td>&minus;0.64</td>
                <td>Poisoned — client&nbsp;0 pulled it off</td>
              </tr>
              <tr>
                <td>FedProx (&mu;&nbsp;=&nbsp;0.5)</td>
                <td>+1.2237</td>
                <td>+0.006</td>
                <td>Proximal term kept local models near global</td>
              </tr>
              <tr>
                <td>Krum (f&nbsp;=&nbsp;1)</td>
                <td>+1.4743</td>
                <td>+0.26</td>
                <td>Rejected client&nbsp;0; selected honest update</td>
              </tr>
              <tr>
                <td>Coord&nbsp;Median</td>
                <td>+1.2548</td>
                <td>+0.04</td>
                <td>Median ignores outlier</td>
              </tr>
            </tbody>
          </table>

          <h3 class="sub">Key functions</h3>
          <p><strong><code>fedavg_aggregate</code></strong> — server-side weighted-average
          aggregation (McMahan et al.&nbsp;2017):</p>
        {fedavg_agg_html}

          <p><strong><code>krum_select</code></strong> — Byzantine-robust update selection
          (Blanchard et al.&nbsp;2017): picks the update with the minimum sum of distances
          to its nearest neighbors — honest updates cluster, the poisoned update is distant:</p>
        {krum_html}

          <p><a href="fedavg_fedprox_krum_demo.py">View full source &rarr;</a></p>
        </section>

            <footer><a href="../index.html">&larr; Back to study hub</a></footer>
          </main>
        </div>
        </body>
        </html>
        """)

    out = demos_dir / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"  generated  demos/index.html  (3 demo sections, {len(_DEMO_COPIES)} assets copied)")


# ---------------------------------------------------------------------------
# Hub page builder (Plan 07-03)
# ---------------------------------------------------------------------------

# Card-group → hub-card definitions
# Architecture group: fixed set of 4 pages from 07-02
_ARCH_CARDS = [
    ("AGMS Architecture Walkthrough",
     "Read the AGMS system walkthrough — self-organizing grid-management platform, patents deep-dive.",
     "architecture/AGMS-architecture.html"),
    ("Grid Operations &amp; Director&#x27;s Role",
     "Read grid operations and role companion — Appendices A&ndash;G mapping the role to the architecture.",
     "architecture/grid-operations-and-role.html"),
    ("Patent Family Index",
     "Browse the patent index — six patents covering AGMS, Logistician Module, Scout Command, and more.",
     "architecture/INDEX.html"),
    ("AGMS Architecture Diagram",
     "View the full AGMS reference-architecture diagram (annotated PNG, click to zoom).",
     "architecture/diagram.html"),
]

# Demo group: single entry-point card
_DEMO_CARDS = [
    ("Hands-On Demos",
     "See three from-scratch NumPy demos: EKF line temperature, DC power-flow bad-data detection, and federated learning robustness.",
     "demos/index.html"),
]

# Phase prefix → group label for study notes
_NOTE_GROUPS = [
    ("KAL", "Phase 1 — Kalman State Estimation"),
    ("TVS", "Phase 2 — Transmission Virtual Sensing"),
    ("AGMS", "Phase 3 — Director&#x27;s Patents"),
    ("STK", "Phase 4 — Protocols &amp; Stack Architecture"),
    ("FED", "Phase 5 — Federated Architectures &amp; Security"),
]


def _note_group(slug: str) -> str:
    """Return the phase-prefix key for a note slug (first hyphen-delimited part, uppercase)."""
    return slug.split("-")[0].upper()


def build_hub(manifest: dict) -> None:
    """Emit docs/index.html — card-grid hub in three groups.

    Hub is at docs/ root so asset paths have NO '../' prefix (assets/site.css not ../assets/).
    Note cards are generated from the manifest (single source of truth — Pitfall 5).
    Architecture cards are fixed (from 07-02 outputs).
    """
    # ---- Build note-card HTML grouped by phase prefix ----
    # Collect slug→relpath from manifest (only notes/ entries)
    note_entries = {
        slug: relpath
        for slug, relpath in manifest.items()
        if relpath.startswith("notes/")
    }

    note_cards_html = ""
    for prefix, group_label in _NOTE_GROUPS:
        group_slugs = sorted(
            slug for slug in note_entries
            if _note_group(slug) == prefix
        )
        if not group_slugs:
            continue  # skip empty groups (UI-SPEC: never render empty group)
        note_cards_html += f'\n    <h3 class="sub">{group_label}</h3>\n    <div class="card-grid">\n'
        for slug in group_slugs:
            relpath = note_entries[slug]
            # Derive a readable title from the slug (capitalize each word)
            readable = slug.replace("-", " ").title()
            note_cards_html += (
                f'      <a class="hub-card" href="{relpath}">'
                f'<h3>Open study note</h3>'
                f'<p>{readable}</p></a>\n'
            )
        note_cards_html += "    </div>\n"

    # ---- Build architecture card HTML ----
    arch_cards_html = '<div class="card-grid">\n'
    for title, desc, href in _ARCH_CARDS:
        arch_cards_html += (
            f'      <a class="hub-card" href="{href}">'
            f'<h3>{title}</h3>'
            f'<p>{desc}</p></a>\n'
        )
    arch_cards_html += "    </div>"

    # ---- Build demos card HTML ----
    demo_cards_html = '<div class="card-grid">\n'
    for title, desc, href in _DEMO_CARDS:
        demo_cards_html += (
            f'      <a class="hub-card" href="{href}">'
            f'<h3>{title}</h3>'
            f'<p>{desc}</p></a>\n'
        )
    demo_cards_html += "    </div>"

    html = textwrap.dedent(f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="robots" content="noindex,nofollow">
        <title>GE Vernova Virtual Sensing &mdash; Interview Study Site</title>
        <link rel="stylesheet" href="assets/site.css">
        <link rel="stylesheet" href="assets/pygments.css">
        </head>
        <body>
        <div class="wrap">
          <header class="masthead">
            <h1>GE Vernova Virtual Sensing &mdash; Interview Study Site</h1>
            <div class="meta">Architecture, study notes, and hands-on demos in one place.</div>
          </header>
          <nav class="toc">
            <h2>Jump to</h2>
            <a href="#architecture">Architecture</a>
            <a href="#notes">Study Notes</a>
            <a href="#demos">Demos</a>
          </nav>
          <main>

        <!-- ================================================================
             Group 1: Architecture
             ================================================================ -->
        <section class="card" id="architecture">
          <h2 class="sec">Architecture</h2>
          <p>Research pages covering the AGMS patent family, the director&#x27;s architecture,
          and the grid-operations context &mdash; copied directly from the hand-authored
          research HTML.</p>
          {arch_cards_html}
        </section>

        <!-- ================================================================
             Group 2: Study Notes
             ================================================================ -->
        <section class="card" id="notes">
          <h2 class="sec">Study Notes</h2>
          <p>{len(note_entries)} notes converted from Markdown, organized by phase.</p>
          {note_cards_html}
        </section>

        <!-- ================================================================
             Group 3: Demos
             ================================================================ -->
        <section class="card" id="demos">
          <h2 class="sec">Demos</h2>
          <p>Three from-scratch NumPy demos with embedded key-function code, inline
          results, and links to full source &mdash; built offline, no runtime dependencies.</p>
          {demo_cards_html}
        </section>

            <footer>GE Vernova Virtual Sensing Study Site &mdash; local, offline, no deployment required.</footer>
          </main>
        </div>
        </body>
        </html>
        """)

    out = DOCS / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"  generated  docs/index.html  ({len(note_entries)} note cards + {len(_ARCH_CARDS)} arch cards + {len(_DEMO_CARDS)} demo card)")


# ---------------------------------------------------------------------------
# Publishing config files (Plan 07-04)
# ---------------------------------------------------------------------------

def emit_publishing_files() -> None:
    """Emit docs/.nojekyll (empty marker) and docs/robots.txt (disallow all).

    .nojekyll: stops GitHub Pages' Jekyll from mangling vendor/ and _-prefixed
    MathJax component paths (anti-pattern: absent .nojekyll breaks offline math
    on Pages — RESEARCH.md).

    robots.txt: reinforces noindex,nofollow on every page (HTML-07).
    """
    nojekyll = DOCS / ".nojekyll"
    nojekyll.write_text("", encoding="utf-8")
    print(f"  emitted   docs/.nojekyll  (empty marker — stops Jekyll mangling vendor/)")

    robots = DOCS / "robots.txt"
    robots.write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
    print(f"  emitted   docs/robots.txt  (Disallow: /)")


# ---------------------------------------------------------------------------
# Link-validation pass (Plan 07-04) — HTML-06 + HTML-07 acceptance gate
# ---------------------------------------------------------------------------

def validate_links() -> None:
    """Validate every emitted HTML page in docs/:
      1. Each href/src that is not external (http/https/mailto) and not a pure
         anchor (#...) must resolve to a file that exists on disk relative to the
         page's own directory.  Missing targets are collected and reported as
         BROKEN lines; then sys.exit(1) is raised (fail loud — HTML-06).
      2. Every emitted .html must contain the string 'noindex' in its content
         (HTML-07).  Pages lacking it are reported as NOINDEX-MISSING and also
         trigger sys.exit(1).

    Uses only stdlib (re + pathlib) — no third-party deps.

    NOTE: Architecture pages (copied from research) retain their own
    noindex,nofollow meta from the originals; docs/ source PDFs and .docx files
    that nothing links to are out-of-scope and intentionally skipped.
    """
    # Collect all emitted HTML pages under docs/
    all_pages = sorted(DOCS.rglob("*.html"))

    # Pattern: match href="..." or src="..." (single or double quotes)
    attr_pattern = re.compile(r"""(?:href|src)=["']([^"']+)["']""")

    broken: list[str] = []
    noindex_missing: list[str] = []

    for page in all_pages:
        text = page.read_text(encoding="utf-8", errors="replace")
        page_dir = page.parent

        # ---- noindex audit (HTML-07) ----
        if "noindex" not in text:
            noindex_missing.append(f"NOINDEX-MISSING: {page.relative_to(DOCS)}")

        # ---- link audit (HTML-06) ----
        for match in attr_pattern.finditer(text):
            raw = match.group(1)

            # Skip external schemes and pure anchors
            if raw.startswith(("http://", "https://", "mailto:", "data:", "//")):
                continue
            if raw.startswith("#"):
                continue

            # Strip fragment (#anchor) if present
            href = raw.split("#")[0]
            if not href:
                continue  # pure anchor after stripping

            # Resolve relative to the page's own directory
            target = (page_dir / href).resolve()

            if not target.exists():
                broken.append(f"BROKEN: {page.relative_to(DOCS)} -> {raw}")

    # Report all issues, then fail loud if any
    issues = noindex_missing + broken
    if issues:
        print("\n--- LINK VALIDATION FAILED ---", file=sys.stderr)
        for issue in issues:
            print(f"  {issue}", file=sys.stderr)
        print(f"\n  {len(broken)} broken link(s), {len(noindex_missing)} noindex-missing page(s)",
              file=sys.stderr)
        sys.exit(1)

    print(f"  validate_links: OK — {len(all_pages)} pages, 0 broken links, 0 noindex-missing")


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

    # Plan 07-03: demos page + card-grid hub
    print("--- demos page ---")
    build_demos()
    print()

    print("--- hub (index.html) ---")
    build_hub(manifest)
    print()

    # Plan 07-04: emit publishing config files + final link-validation pass
    print("--- publishing config ---")
    emit_publishing_files()
    print()

    print("--- link validation (HTML-06 + HTML-07 acceptance gate) ---")
    validate_links()
    print()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"\nFATAL: {exc}", file=sys.stderr)
        sys.exit(1)
