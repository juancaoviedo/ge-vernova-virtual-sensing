#!/usr/bin/env python3
"""
build_appendix.py — Render the distribution-observability appendix from Markdown into a
self-contained, styled HTML page that matches the existing AGMS patent study notes.

It derives styling from the canonical patent page so the appendix is visually identical
to the rest of the family (single source of truth for the look-and-feel):

  source MD   : .planning/research/patents/appendix-distribution-observability-sources.md
  style donor : .planning/research/patents/AGMS-architecture.html  (its <style> block)
  output HTML : .planning/research/patents/appendix-distribution-observability-sources.html

The output is ONE self-contained file:
  - all CSS inline (copied verbatim from the donor + a few additions),
  - masthead + sticky left TOC + .card sections (one per H2),
  - noindex,nofollow (study material — never indexed),
  - zero network dependencies (renders offline at file://).

docs/build_site.py then copies the output into docs/architecture/ during the site build.

Run from anywhere:  python3 patents-site/build_appendix.py
"""

import html as html_lib
import re
import sys
import urllib.parse
from pathlib import Path

import markdown

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PATENTS = ROOT / ".planning" / "research" / "patents"
SRC_MD = PATENTS / "appendix-distribution-observability-sources.md"
STYLE_DONOR = PATENTS / "AGMS-architecture.html"
OUT = PATENTS / "appendix-distribution-observability-sources.html"

SUBTITLE = (
    "The universe of distribution-level state-information sources, framed by the ORACS "
    "observability &amp; reachability indexes &middot; Juan Carlos Oviedo Cepeda"
)

# Code/diagram blocks and blockquote callouts aren't covered by the donor's note CSS;
# add the few rules needed so fenced code and blockquotes match the family's styling.
EXTRA_CSS = """
  header.masthead p.sub{margin:10px 0 0;font-size:14px;color:#cfe0d8;font-weight:400;}
  main pre{background:#0f1722;color:#d6e3ee;border-radius:10px;padding:16px 20px;overflow-x:auto;font-family:"SF Mono",ui-monospace,Menlo,Consolas,monospace;font-size:12.5px;line-height:1.6;border:1px solid #1c2a3a;}
  main pre code{background:none;border:0;color:inherit;padding:0;font-size:inherit;}
  blockquote{background:var(--callout);border-left:4px solid var(--callout-line);border-radius:0 8px 8px 0;padding:12px 18px;margin:16px 0;color:#4a3d12;}
  blockquote p{margin:6px 0;}
  a.imglink{text-decoration:none;font-size:13px;margin-left:5px;opacity:.55;white-space:nowrap;}
  a.imglink:hover{opacity:1;}"""

# Physical-hardware tiers get a per-row "see real-world photos" Google Images link.
# Abstract tiers (6 topology, 7 pseudo-measurements, 8 control-center systems,
# 9 environmental data, 10 event records, 13 protocols, 14 non-utility) are skipped —
# a device photo is meaningless for a model, a forecast, or a protocol.
_DEVICE_TIERS = {1, 2, 3, 4, 5, 11, 12}
# Light per-tier query qualifier to sharpen image results where device names are generic.
_TIER_SUFFIX = {1: "substation", 2: "distribution feeder", 3: "power grid", 12: "utility field"}


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def slugify(text: str) -> str:
    """Heading text -> stable anchor id (lowercase alnum joined by hyphens)."""
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "section"


def _device_query(cell_html: str, suffix: str) -> str | None:
    """Derive a clean Google Images search query from a table's device-name cell.

    Drops parentheticals (vendor lists, standard refs, acronym expansions), normalizes
    separators, and appends an optional tier qualifier. Returns None if nothing usable.
    """
    t = re.sub(r"<[^>]+>", "", cell_html)        # strip inline tags (<code> etc.)
    t = html_lib.unescape(t)                      # &amp; -> &, &#124; -> |
    t = re.sub(r"\([^)]*\)", " ", t)              # drop parentheticals
    t = t.replace("/", " ").replace("&", " ")
    t = re.sub(r"[^\w\s-]", " ", t)               # keep word chars, spaces, hyphens
    t = re.sub(r"\s+", " ", t).strip()
    if not t:
        return None
    return f"{t} {suffix}".strip() if suffix else t


def _image_link(query: str) -> str:
    """Build a 'see real-world photos' Google Images link for a device query."""
    url = "https://www.google.com/search?tbm=isch&q=" + urllib.parse.quote_plus(query)
    url = url.replace("&", "&amp;")               # valid HTML attribute
    title = html_lib.escape(f"See real-world photos — Google Images: {query}")
    return f'<a class="imglink" href="{url}" target="_blank" rel="noopener" title="{title}">&#128247;</a>'


def _add_image_links(section_html: str, suffix: str) -> str:
    """Append an image-search link to the first cell of every body row in the section's table."""
    def repl(m: "re.Match[str]") -> str:
        opening, cell = m.group(1), m.group(2)
        query = _device_query(cell, suffix)
        if not query:
            return m.group(0)
        return f"{opening}<td>{cell} {_image_link(query)}</td>"

    # First <td> of each row only (headers use <th>, so they are never matched).
    return re.sub(r"(<tr>\s*)<td>(.*?)</td>", repl, section_html, flags=re.S)


def main() -> None:
    if not SRC_MD.exists():
        fail(f"source markdown not found: {SRC_MD}")
    if not STYLE_DONOR.exists():
        fail(f"style donor not found: {STYLE_DONOR}")

    # 1. Pull the donor stylesheet verbatim (includes masthead/toc/card/table CSS) + additions.
    donor = STYLE_DONOR.read_text(encoding="utf-8")
    style_m = re.search(r"<style>(.*?)</style>", donor, re.S)
    if not style_m:
        fail("could not locate <style> block in style donor")
    css = style_m.group(1).rstrip() + "\n" + EXTRA_CSS

    text = SRC_MD.read_text(encoding="utf-8")

    # 2. Extract the H1 title (masthead), then split the rest into H2 sections.
    title_m = re.search(r"(?m)^# (.+)$", text)
    if not title_m:
        fail("source markdown has no H1 title")
    title = title_m.group(1).strip()
    rest = text[title_m.end():]

    # Split on top-level H2 headings; first chunk is any preamble (ignored if blank).
    chunks = re.split(r"(?m)^## ", rest)
    sections = []  # (sid, heading, body_md)
    for chunk in chunks[1:]:
        nl = chunk.find("\n")
        heading = (chunk[:nl] if nl != -1 else chunk).strip()
        body_md = chunk[nl + 1:] if nl != -1 else ""
        # Drop standalone horizontal-rule lines so they don't trail a stray <hr> in a card.
        body_md = "\n".join(ln for ln in body_md.splitlines() if ln.strip() != "---")
        sections.append((slugify(heading), heading, body_md))
    if not sections:
        fail("no H2 sections found in source markdown")

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "attr_list", "sane_lists", "md_in_html"]
    )

    cards, toc_lines = [], []
    for sid, heading, body_md in sections:
        md.reset()
        body_html = md.convert(body_md)
        # Style sub-headings like the rest of the family (h3.sub / h4.sub).
        body_html = body_html.replace("<h3>", '<h3 class="sub">').replace("<h4>", '<h4 class="sub">')
        # Add per-device "see real-world photos" image-search links on the hardware tiers.
        tier_m = re.match(r"tier-(\d+)-", sid)
        if tier_m and int(tier_m.group(1)) in _DEVICE_TIERS:
            body_html = _add_image_links(body_html, _TIER_SUFFIX.get(int(tier_m.group(1)), ""))
        cards.append(
            f'<section class="card" id="{sid}">\n'
            f'<h2 class="sec" id="{sid}">{heading}</h2>\n{body_html}\n</section>'
        )
        toc_lines.append(f'    <a href="#{sid}">{heading}</a>')

    body = "\n".join(cards)
    toc = "\n".join(toc_lines)

    out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{title}</title>
<style>
{css}
</style>
</head>
<body>
<div class="wrap">
  <header class="masthead">
    <h1>{title}</h1>
    <p class="sub">{SUBTITLE}</p>
  </header>
  <nav class="toc">
    <h2>Contents</h2>
{toc}
  </nav>
  <main>
{body}
    <footer>Appendix to the AGMS patent study notes &middot; Juan Carlos Oviedo Cepeda</footer>
  </main>
</div>
</body>
</html>
"""

    OUT.write_text(out, encoding="utf-8")

    # Fail loud if any external href/src slipped in (this page must be self-contained),
    # EXCEPT the deliberate Google Images "see the real device" links on hardware rows.
    ext = re.findall(r'(?:href|src)="((?!#)(?!data:)[^"]*)"', out)
    leaks = [u for u in ext if not u.startswith("https://www.google.com/search")]
    if leaks:
        fail("external reference(s) leaked into output: " + ", ".join(sorted(set(leaks))))

    kb = len(out.encode("utf-8")) / 1024
    print(f"Wrote {OUT.relative_to(ROOT)} ({kb:.0f} KB, {len(sections)} card sections).")


if __name__ == "__main__":
    main()
