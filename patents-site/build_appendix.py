#!/usr/bin/env python3
"""
build_appendix.py — Render the AGMS patent *appendices* from Markdown into self-contained,
styled HTML pages that match the existing patent study notes.

Each appendix derives styling from the canonical patent page so it is visually identical to
the rest of the family (single source of truth for the look-and-feel). Output per appendix is
ONE self-contained file: all CSS inline, masthead + sticky TOC + .card sections (one per H2),
noindex,nofollow, and no network dependencies (renders offline at file://) — except the
deliberate Google Images "see the real device" links on the device-inventory appendix.

Appendices (see APPENDICES registry below):
  - appendix-distribution-observability-sources  (device inventory; per-row image links)
  - appendix-virtual-sensing-module              (state-estimator architecture)

docs/build_site.py then copies the outputs into docs/architecture/ during the site build.
Internal cross-links between the two appendices (and to other patent pages) are allowed and
resolved at the docs/ layer; only true external/network references are rejected.

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
STYLE_DONOR = PATENTS / "AGMS-architecture.html"

# Registry of appendices to build. device_links=True injects per-row Google Images links on
# the physical-hardware tiers (only meaningful for the device-inventory appendix).
APPENDICES = [
    {
        "md": "appendix-distribution-observability-sources.md",
        "out": "appendix-distribution-observability-sources.html",
        "subtitle": (
            "The universe of distribution-level state-information sources, framed by the "
            "ORACS observability &amp; reachability indexes &middot; Juan Carlos Oviedo Cepeda"
        ),
        "device_links": True,
    },
    {
        "md": "appendix-virtual-sensing-module.md",
        "out": "appendix-virtual-sensing-module.html",
        "subtitle": (
            "From devices to network state — the state-estimator architecture for the "
            "virtual sensing module &middot; Juan Carlos Oviedo Cepeda"
        ),
        "device_links": False,
        # A pan/zoom/full-screen architecture diagram inlined at the top of the page,
        # using the same vector viewer as the AGMS walkthrough.
        "diagram": {
            "svg": "appendix-virtual-sensing-module.svg",
            "title": "The Module on One Page",
            "intro": (
                "The whole virtual-sensing module as one architecture: inputs (field devices "
                "&amp; model) &rarr; forecast / pseudo-measurements &rarr; one coupled, "
                "multi-rate state estimator (power flow embedded in <code>h(x)</code>) &rarr; "
                "the four virtual sensors and the ORACS observability index, with the "
                "federation layer and the open decisions. The diagram is the live vector: "
                "<strong>drag to pan, scroll to zoom</strong>, and <strong>click it for "
                "full-screen</strong>."
            ),
            "caption": (
                "Virtual sensing module architecture (A1&ndash;A11) &mdash; reconstructed from "
                "the design discussion; spine settled, decisions D1&ndash;D3 left open."
            ),
        },
    },
]

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

# Pan/zoom/full-screen viewer for an inline SVG. Identical to the AGMS walkthrough's viewer
# (docs/architecture/AGMS-architecture.html) so the appendix diagram behaves the same.
VIEWER_JS = """<script>
(function(){
  var v=document.getElementById('svgv');
  if(!v) return;
  var stage=v.querySelector('.svgv-stage'), svg=v.querySelector('svg');
  if(!svg) return;
  var bb=svg.viewBox&&svg.viewBox.baseVal;
  var natW=(bb&&bb.width)||parseFloat(svg.getAttribute('width'))||1602;
  var natH=(bb&&bb.height)||parseFloat(svg.getAttribute('height'))||806;
  svg.removeAttribute('width'); svg.removeAttribute('height');
  svg.setAttribute('preserveAspectRatio','xMidYMid meet');
  svg.style.width='100%'; svg.style.height='100%'; svg.style.display='block';
  var vb={x:0,y:0,w:natW,h:natH}, fitW=natW;
  function applyVB(){ svg.setAttribute('viewBox', vb.x+' '+vb.y+' '+vb.w+' '+vb.h); }
  function WH(){ var r=stage.getBoundingClientRect(); return [r.width||1, r.height||1]; }
  function fit(){
    var d=WH(), sa=d[0]/d[1], da=natW/natH;
    if(da>sa){ vb.w=natW; vb.h=natW/sa; } else { vb.h=natH; vb.w=natH*sa; }
    vb.x=(natW-vb.w)/2; vb.y=(natH-vb.h)/2; fitW=vb.w; applyVB();
  }
  function zoomAt(cx,cy,fac){
    var d=WH(), W=d[0], H=d[1];
    var nw=vb.w*fac;
    if(nw < natW/16) fac=(natW/16)/vb.w;
    if(vb.w*fac > fitW) fac=fitW/vb.w;
    nw=vb.w*fac; var nh=vb.h*fac;
    var ux=vb.x+(cx/W)*vb.w, uy=vb.y+(cy/H)*vb.h;
    vb.x=ux-(cx/W)*nw; vb.y=uy-(cy/H)*nh; vb.w=nw; vb.h=nh; applyVB();
  }
  fit();
  window.addEventListener('resize', fit);
  stage.addEventListener('wheel', function(e){
    e.preventDefault();
    var r=stage.getBoundingClientRect();
    zoomAt(e.clientX-r.left, e.clientY-r.top, e.deltaY<0?1/1.2:1.2);
  }, {passive:false});
  var down=false, moved=false, sx=0, sy=0, ox=0, oy=0;
  stage.addEventListener('pointerdown', function(e){
    e.preventDefault();
    down=true; moved=false; sx=e.clientX; sy=e.clientY; ox=vb.x; oy=vb.y;
    try{ stage.setPointerCapture(e.pointerId); }catch(_){}
    stage.classList.add('grabbing');
  });
  stage.addEventListener('pointermove', function(e){
    if(!down) return;
    var d=WH(), dx=e.clientX-sx, dy=e.clientY-sy;
    if(Math.abs(dx)>4||Math.abs(dy)>4) moved=true;
    vb.x=ox-(dx/d[0])*vb.w; vb.y=oy-(dy/d[1])*vb.h; applyVB();
  });
  stage.addEventListener('pointerup', function(){
    down=false; stage.classList.remove('grabbing');
    if(!moved) toggleFs();
  });
  function toggleFs(){
    var fsEl=document.fullscreenElement||document.webkitFullscreenElement;
    if(fsEl){ (document.exitFullscreen||document.webkitExitFullscreen).call(document); }
    else { (v.requestFullscreen||v.webkitRequestFullscreen).call(v); }
  }
  function onFs(){ setTimeout(fit, 80); }
  document.addEventListener('fullscreenchange', onFs);
  document.addEventListener('webkitfullscreenchange', onFs);
  v.querySelector('.svgv-controls').addEventListener('click', function(e){
    var b=e.target.closest('button'); if(!b) return;
    var d=WH();
    var a=b.getAttribute('data-act');
    if(a==='in') zoomAt(d[0]/2, d[1]/2, 1/1.35);
    else if(a==='out') zoomAt(d[0]/2, d[1]/2, 1.35);
    else if(a==='reset') fit();
    else if(a==='fs') toggleFs();
  });
})();
</script>"""

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


def _force_light(svg: str) -> str:
    """Pin a draw.io SVG to light rendering.

    draw.io exports theme colors as CSS `light-dark(<light>, <dark>)` and tags the root with
    `color-scheme: light dark`. On an OS in dark mode the browser then picks the *dark* side —
    so text goes white and label backgrounds go near-black on our light page. Collapse every
    `light-dark(a, b)` to its light value `a` (respecting nested parens, e.g. rgb()/var()), and
    force `color-scheme: only light`.
    """
    svg = svg.replace("color-scheme: light dark", "color-scheme: only light")
    key = "light-dark("
    out, i = [], 0
    while True:
        j = svg.find(key, i)
        if j == -1:
            out.append(svg[i:])
            break
        out.append(svg[i:j])
        p, depth, comma = j + len(key), 1, None
        while p < len(svg) and depth > 0:
            c = svg[p]
            if c == "(":
                depth += 1
            elif c == ")":
                depth -= 1
                if depth == 0:
                    break
            elif c == "," and depth == 1 and comma is None:
                comma = p
            p += 1
        out.append(svg[j + len(key):(comma if comma is not None else p)].strip())  # light value
        i = p + 1
    return "".join(out)


def _inline_svg_viewer(diagram: dict) -> str:
    """Build the pan/zoom/full-screen viewer card with the diagram SVG inlined as crisp vector.

    Normalizes the draw.io SVG (drops the requiredFeatures gate, the embedded raster <image>
    fallback, and the drawio.com FAQ link) so it renders as vector everywhere and is small —
    then writes the cleaned SVG back to source (idempotent) and inlines it.
    """
    svg_path = PATENTS / diagram["svg"]
    if not svg_path.exists():
        fail(f"diagram SVG not found: {svg_path}")
    svg_text = svg_path.read_text(encoding="utf-8")
    cleaned = re.sub(r'\s*requiredFeatures="[^"]*"', "", svg_text)
    cleaned = re.sub(r"<image\b[^>]*?/>", "", cleaned, flags=re.S)     # drop raster fallback
    cleaned = re.sub(r"<a\b[^>]*drawio\.com/doc/faq[^>]*>.*?</a>", "", cleaned, flags=re.S)
    cleaned = _force_light(cleaned)                                   # pin to light rendering
    if cleaned != svg_text:
        svg_path.write_text(cleaned, encoding="utf-8")
    svg_inline = cleaned[cleaned.index("<svg"):]                       # strip XML prolog/doctype

    return f"""<section class="card" id="architecture">
<h2 class="sec">{diagram["title"]}</h2>
<p>{diagram["intro"]}</p>
<figure class="diagram-figure">
<div class="svgv" id="svgv">
<div class="svgv-controls">
<button type="button" data-act="out" title="Zoom out" aria-label="Zoom out">&minus;</button>
<button type="button" data-act="in" title="Zoom in" aria-label="Zoom in">+</button>
<button type="button" data-act="reset" title="Reset / fit to view" aria-label="Reset view">&#8634;</button>
<button type="button" data-act="fs" title="Full screen" aria-label="Full screen">&#9974;</button>
</div>
<div class="svgv-stage"><div class="svgv-pan">{svg_inline}</div></div>
<span class="svgv-hint">Drag to pan &middot; scroll to zoom &middot; click for full-screen</span>
</div>
<figcaption>{diagram["caption"]}</figcaption>
</figure>
</section>"""


def _is_external_leak(url: str) -> bool:
    """A self-containment violation = a network/external reference.

    Allowed (return False): pure anchors (#...), data: URIs, the deliberate Google Images
    links, and *relative same-site* links (e.g. a sibling appendix/patent .html, with or
    without an #anchor) which are resolved at the docs/ layer and link-checked there.
    Rejected (return True): anything with a URL scheme (http/https/mailto/...) other than the
    Google exception, and protocol-relative (//) or absolute (/...) references.
    """
    if url.startswith("#") or url.startswith("data:"):
        return False
    if url.startswith("https://www.google.com/search"):
        return False
    if url.startswith("//") or url.startswith("/"):
        return True
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.\-]*:", url))  # has a scheme -> external


def _build_one(spec: dict, css: str) -> None:
    src_md = PATENTS / spec["md"]
    out_path = PATENTS / spec["out"]
    if not src_md.exists():
        fail(f"source markdown not found: {src_md}")

    text = src_md.read_text(encoding="utf-8")

    # Extract the H1 title (masthead), then split the rest into H2 sections.
    title_m = re.search(r"(?m)^# (.+)$", text)
    if not title_m:
        fail(f"source markdown has no H1 title: {src_md}")
    title = title_m.group(1).strip()
    rest = text[title_m.end():]

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
        fail(f"no H2 sections found in source markdown: {src_md}")

    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "attr_list", "sane_lists", "md_in_html"]
    )

    cards, toc_lines = [], []
    for sid, heading, body_md in sections:
        md.reset()
        body_html = md.convert(body_md)
        body_html = body_html.replace("<h3>", '<h3 class="sub">').replace("<h4>", '<h4 class="sub">')
        if spec["device_links"]:
            tier_m = re.match(r"tier-(\d+)-", sid)
            if tier_m and int(tier_m.group(1)) in _DEVICE_TIERS:
                body_html = _add_image_links(body_html, _TIER_SUFFIX.get(int(tier_m.group(1)), ""))
        cards.append(
            f'<section class="card" id="{sid}">\n'
            f'<h2 class="sec" id="{sid}">{heading}</h2>\n{body_html}\n</section>'
        )
        toc_lines.append(f'    <a href="#{sid}">{heading}</a>')

    # Optional architecture diagram inlined at the very top, with a pan/zoom/full-screen viewer.
    diagram = spec.get("diagram")
    if diagram:
        cards.insert(0, _inline_svg_viewer(diagram))
        toc_lines.insert(0, f'    <a href="#architecture">{diagram["title"]}</a>')

    body = "\n".join(cards)
    toc = "\n".join(toc_lines)
    viewer_js = VIEWER_JS if diagram else ""

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
    <p class="sub">{spec["subtitle"]}</p>
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
{viewer_js}
</body>
</html>
"""

    out_path.write_text(out, encoding="utf-8")

    # Fail loud on any external/network reference (self-containment); internal relative
    # cross-links between appendices/patent pages are allowed and link-checked at docs/ build.
    # Exclude any inlined <svg> (self-contained vector; its refs are intra-document) from the scan.
    scan = re.sub(r"<svg\b.*?</svg>", "", out, flags=re.S)
    ext = re.findall(r'(?:href|src)="([^"]*)"', scan)
    leaks = sorted({u for u in ext if _is_external_leak(u)})
    if leaks:
        fail(f"external reference(s) leaked into {spec['out']}: " + ", ".join(leaks))

    kb = len(out.encode("utf-8")) / 1024
    print(f"Wrote {out_path.relative_to(ROOT)} ({kb:.0f} KB, {len(sections)} card sections).")


def main() -> None:
    if not STYLE_DONOR.exists():
        fail(f"style donor not found: {STYLE_DONOR}")
    donor = STYLE_DONOR.read_text(encoding="utf-8")
    style_m = re.search(r"<style>(.*?)</style>", donor, re.S)
    if not style_m:
        fail("could not locate <style> block in style donor")
    css = style_m.group(1).rstrip() + "\n" + EXTRA_CSS

    for spec in APPENDICES:
        _build_one(spec, css)


if __name__ == "__main__":
    main()
