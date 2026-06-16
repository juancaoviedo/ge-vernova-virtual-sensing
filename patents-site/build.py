#!/usr/bin/env python3
"""
Build patents-site/index.html — a single, fully self-contained page of Juan's
AGMS patent study notes, for sharing with interviewers.

It derives the page from two already-existing artifacts so the prose stays
faithful to the source notes and keeps its styling:

  - docs/architecture/AGMS-architecture.html  (Parts 0-11 already rendered)
  - docs/architecture/AGMS-architecture.drawio.png  (the big architecture diagram)

Output is ONE file with:
  - all CSS inline,
  - the architecture diagram embedded as a base64 data URI (zero network deps),
  - the diagram first, then the written notes Parts 0-11,
  - a simple sticky left index (Architecture + Parts 0-11),
  - the "Quick links" annex and every external/companion-file link removed.

Run from anywhere:  python3 patents-site/build.py
"""

import base64
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SRC_HTML = ROOT / "docs" / "architecture" / "AGMS-architecture.html"
SRC_PNG = ROOT / "docs" / "architecture" / "AGMS-architecture.drawio.png"
OUT = HERE / "index.html"

TITLE = "The AGMS Architecture — A Full, Conceptual Walkthrough"

INTRO = """<section class="card" id="intro">
<p><em>These are my own study notes from a close read of the six-patent <strong>AGMS</strong> family — the Adaptive Power Grid Management System authored by the lab director, Jamshid Sharif-Askary. They walk the architecture end to end, in plain language.</em></p>
<div class="callout"><p><strong>How to read this.</strong> The diagram above is the whole system on one page; the sections below explain what AGMS is, why it exists, how it works, and how the pieces connect. Patent reference numbers (e.g. <code>1400</code>) and object names (e.g. <code>gWFCll(id)</code>) appear in parentheses so they cross-walk to the patent text. Where my own edge/DER engineering maps onto the architecture, there is a <strong>&#9654; Juan</strong> note.</p></div>
</section>"""

EXTRA_CSS = """
  header.masthead p.sub{margin:10px 0 0;font-size:14px;color:#cfe0d8;font-weight:400;}
  figure.arch{margin:8px 0 0;overflow:auto;}
  figure.arch img{display:block;width:100%;height:auto;border:1px solid var(--line);border-radius:10px;background:#fff;cursor:zoom-in;}
  figure.arch img.zoomed{width:auto;max-width:none;cursor:zoom-out;}
  figure.arch figcaption{color:var(--muted);font-size:12.5px;margin-top:8px;text-align:center;}"""


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if not SRC_HTML.exists():
        fail(f"source HTML not found: {SRC_HTML}")
    if not SRC_PNG.exists():
        fail(f"diagram PNG not found: {SRC_PNG}")

    html = SRC_HTML.read_text(encoding="utf-8")

    # 1. Reuse the source stylesheet verbatim, plus our additions.
    style_m = re.search(r"<style>(.*?)</style>", html, re.S)
    if not style_m:
        fail("could not locate <style> block in source HTML")
    css = style_m.group(1).rstrip() + "\n" + EXTRA_CSS

    # 2. Pull the rendered section cards. Keep Parts 0-11 (have an <h2 class="sec">
    #    heading) and drop the intro card (no heading) and the p13 "Quick links" annex.
    cards = re.findall(r'<section class="card">(.*?)</section>', html, re.S)
    parts = []
    for inner in cards:
        if '<h2 class="sec"' not in inner:
            continue  # intro card — replaced with our interviewer-facing INTRO
        if 'id="p13"' in inner:
            continue  # "Quick links" annex — excluded
        parts.append(f'<section class="card">{inner}</section>')
    if not parts:
        fail("no Part sections (p1..p12) found in source HTML")

    # 2b. Strip internal sibling-file breadcrumbs (e.g. "(logistician-module.md)")
    #     that point at per-patent notes not shipped in this standalone page.
    cleaned = []
    for inner in parts:
        inner = re.sub(r" \(<code>[a-z-]+\.md</code>, (cross-cutting)\)", r" (\1)", inner)
        inner = re.sub(r" \(<code>[a-z-]+\.md</code>\)", "", inner)
        cleaned.append(inner)
    parts = cleaned

    # 3. Regenerate the TOC from the kept sections; lead with Architecture; no annex.
    toc_lines = ['    <a href="#architecture">Architecture diagram</a>']
    for inner in parts:
        m = re.search(r'<h2 class="sec" id="(p\d+)">(.*?)</h2>', inner, re.S)
        if not m:
            fail("a kept section is missing its <h2 class=\"sec\" id> heading")
        pid, label = m.group(1), m.group(2).strip()
        toc_lines.append(f'    <a href="#{pid}">{label}</a>')
    toc = "\n".join(toc_lines)

    # 4. Embed the diagram as a base64 data URI (single copy; click-to-zoom in CSS/JS).
    b64 = base64.b64encode(SRC_PNG.read_bytes()).decode("ascii")
    data_uri = f"data:image/png;base64,{b64}"
    arch = f"""<section class="card" id="architecture">
<h2 class="sec">The Whole System, One Diagram</h2>
<p>The complete AGMS architecture, reconstructed from the six-patent family: perception (<strong>GridWideMind</strong>) &rarr; reasoning (<strong>GridArtificer</strong>) &rarr; orchestration and execution (<strong>GridWideCommandHub</strong>), the five-stage formation pipeline, scouts at the edge, and the cross-cutting POV / security / learning threads.</p>
<figure class="arch">
<img id="archImg" src="{data_uri}" alt="AGMS architecture — full system diagram" onclick="this.classList.toggle('zoomed')">
<figcaption>Click the diagram to zoom to full resolution; click again to fit. (4885 &times; 4265 px source.)</figcaption>
</figure>
</section>"""

    body = "\n".join([arch, INTRO] + parts)

    out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{TITLE}</title>
<style>
{css}
</style>
</head>
<body>
<div class="wrap">
  <header class="masthead">
    <h1>{TITLE}</h1>
    <p class="sub">Study notes from a close read of the six-patent Adaptive Power Grid Management System family &middot; Juan Carlos Oviedo Cepeda</p>
  </header>
  <nav class="toc">
    <h2>Contents</h2>
{toc}
  </nav>
  <main>
{body}
    <footer>Self-contained study notes by Juan Carlos Oviedo Cepeda &middot; derived from a close reading of the AGMS patent family.</footer>
  </main>
</div>
</body>
</html>
"""

    OUT.write_text(out, encoding="utf-8")

    # Fail loud if anything external slipped through.
    leaks = re.findall(r'(?:href|src)="(?!#)(?!data:)[^"]*"', out)
    if leaks:
        fail("external reference(s) leaked into output: " + ", ".join(sorted(set(leaks))))

    kb = len(out.encode("utf-8")) / 1024
    print(f"Wrote {OUT.relative_to(ROOT)} ({kb:.0f} KB, {len(parts)} note sections, diagram embedded).")


if __name__ == "__main__":
    main()
