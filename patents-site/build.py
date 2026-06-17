#!/usr/bin/env python3
"""
Build patents-site/index.html — a single, fully self-contained page of Juan's
AGMS patent study notes, for sharing with interviewers.

It derives the page from two already-existing artifacts so the prose stays
faithful to the source notes and keeps its styling:

  - docs/architecture/AGMS-architecture.html  (Parts 0-11 already rendered + viewer CSS)
  - docs/architecture/AGMS-architecture.svg   (the architecture diagram, vector)

Output is ONE file with:
  - all CSS inline,
  - the architecture diagram INLINED as vector SVG with a pan/zoom/full-screen
    viewer (zero network deps; crisp at any zoom; works offline at file://),
  - the diagram first, then the written notes Parts 0-11,
  - a simple sticky left index (Architecture + Parts 0-11),
  - the "Quick links" annex and every external/companion-file link removed.

Run from anywhere:  python3 patents-site/build.py
"""

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SRC_HTML = ROOT / "docs" / "architecture" / "AGMS-architecture.html"
SRC_SVG = ROOT / "docs" / "architecture" / "AGMS-architecture.svg"
OUT = HERE / "index.html"

TITLE = "The AGMS Architecture — A Full, Conceptual Walkthrough"

INTRO = """<section class="card" id="intro">
<p><em>These are my own study notes from a close read of the six-patent <strong>AGMS</strong> family — the Adaptive Power Grid Management System authored by the lab director, Jamshid Sharif-Askary. They walk the architecture end to end, in plain language.</em></p>
<div class="callout"><p><strong>How to read this.</strong> The diagram above is the whole system on one page; the sections below explain what AGMS is, why it exists, how it works, and how the pieces connect. Patent reference numbers (e.g. <code>1400</code>) and object names (e.g. <code>gWFCll(id)</code>) appear in parentheses so they cross-walk to the patent text.</p></div>
</section>"""

# Only the masthead subtitle is unique to this page; the diagram viewer CSS
# (.svgv*) already arrives via the copied <style> block from the source HTML.
EXTRA_CSS = """
  header.masthead p.sub{margin:10px 0 0;font-size:14px;color:#cfe0d8;font-weight:400;}"""

# Pan/zoom/full-screen viewer for the inline SVG. Identical to the docs page.
VIEWER_JS = """<script>
(function(){
  var v=document.getElementById('svgv');
  if(!v) return;
  var stage=v.querySelector('.svgv-stage'), svg=v.querySelector('svg');
  if(!svg) return;
  var bb=svg.viewBox&&svg.viewBox.baseVal;
  var natW=(bb&&bb.width)||parseFloat(svg.getAttribute('width'))||2432;
  var natH=(bb&&bb.height)||parseFloat(svg.getAttribute('height'))||2132;
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


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if not SRC_HTML.exists():
        fail(f"source HTML not found: {SRC_HTML}")
    if not SRC_SVG.exists():
        fail(f"diagram SVG not found: {SRC_SVG}")

    html = SRC_HTML.read_text(encoding="utf-8")

    # 1. Reuse the source stylesheet verbatim (includes the .svgv viewer CSS), plus additions.
    style_m = re.search(r"<style>(.*?)</style>", html, re.S)
    if not style_m:
        fail("could not locate <style> block in source HTML")
    css = style_m.group(1).rstrip() + "\n" + EXTRA_CSS

    # 2. Pull the rendered section cards. Keep Parts 0-11 (have an <h2 class="sec">
    #    heading) and drop the intro card (no heading) and the p13 "Quick links" annex.
    #    The diagram card uses <section class="card" id="diagram"> so this regex
    #    (no attributes) naturally skips it — we rebuild the diagram below.
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
        m = re.search(r'<h2 class="sec" id="([\w-]+)">(.*?)</h2>', inner, re.S)
        if not m:
            fail("a kept section is missing its <h2 class=\"sec\" id> heading")
        pid, label = m.group(1), m.group(2).strip()
        toc_lines.append(f'    <a href="#{pid}">{label}</a>')
    toc = "\n".join(toc_lines)

    # 4. Inline the diagram as vector SVG inside a pan/zoom/full-screen viewer.
    #    Strip the XML prolog/doctype so it embeds as valid inline HTML5 SVG.
    svg_text = SRC_SVG.read_text(encoding="utf-8")
    svg_inline = svg_text[svg_text.index("<svg"):]
    arch = f"""<section class="card" id="architecture">
<h2 class="sec">The Whole System, One Diagram</h2>
<p>The complete AGMS architecture, reconstructed from the six-patent family: perception (<strong>GridWideMind</strong>) &rarr; reasoning (<strong>GridArtificer</strong>) &rarr; orchestration and execution (<strong>GridWideCommandHub</strong>), the five-stage formation pipeline, scouts at the edge, and the cross-cutting POV / security / learning threads. The diagram is the live vector: <strong>drag to pan, scroll to zoom</strong>, and <strong>click it for full-screen</strong>.</p>
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
<figcaption>AGMS architecture — reconstructed from the director's six-patent family, with hand-added study annotations (live vector, faithful colors).</figcaption>
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
{VIEWER_JS}
</body>
</html>
"""

    OUT.write_text(out, encoding="utf-8")

    # Fail loud if anything external slipped through. Exclude the inline SVG, whose
    # only refs are embedded data: images plus one harmless drawio-docs link.
    check = re.sub(r"<svg\b.*?</svg>", "", out, flags=re.S)
    leaks = re.findall(r'(?:href|src)="(?!#)(?!data:)[^"]*"', check)
    if leaks:
        fail("external reference(s) leaked into output: " + ", ".join(sorted(set(leaks))))

    kb = len(out.encode("utf-8")) / 1024
    print(f"Wrote {OUT.relative_to(ROOT)} ({kb:.0f} KB, {len(parts)} note sections, inline SVG viewer).")


if __name__ == "__main__":
    main()
