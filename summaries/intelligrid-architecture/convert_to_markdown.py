#!/usr/bin/env python3
"""Convert the mirrored IntelliGrid Architecture HTML site to Markdown.

Walks mirror/ for .htm/.html files, extracts the main text + images, and writes
a parallel tree under markdown/ preserving the original directory layout and
relative links. Also emits an INDEX.md listing every converted page.
"""
import os
import re
import sys
from pathlib import Path

from bs4 import BeautifulSoup
from markdownify import markdownify as md

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "mirror"
OUT = ROOT / "markdown"

HTML_EXTS = {".htm", ".html"}


def read_html(path: Path) -> str:
    """Decode respecting the site's Windows-1252 charset."""
    raw = path.read_bytes()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("cp1252", errors="replace")


def table_max_filled_cols(table) -> int:
    """Max number of non-empty cells in any direct row of this table."""
    cols = 0
    rows = table.find_all("tr", recursive=False) or table.find_all("tr")
    for tr in rows:
        cells = tr.find_all(["td", "th"], recursive=False)
        filled = sum(1 for c in cells if c.get_text(strip=True))
        cols = max(cols, filled)
    return cols


def clean_soup(soup: BeautifulSoup) -> BeautifulSoup:
    # Drop non-content elements.
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # Remove the repeated left-hand navigation menu: it lives in its own <td>
    # alongside the content cell, so remove only that cell, not the table.
    nav = soup.find(string=re.compile("Parent Menu"))
    if nav:
        (nav.find_parent("td") or nav.parent).decompose()

    # Remove the copyright footer (a small standalone table).
    foot = soup.find(string=re.compile("Copyright EPRI"))
    if foot:
        tbl = foot.find_parent("table")
        if tbl and len(tbl.get_text(strip=True)) < 300:
            tbl.decompose()
        else:
            (foot.find_parent("td") or foot.parent).decompose()

    # Unwrap layout tables (FrontPage used nested tables purely for layout):
    # any table whose rows never hold more than one non-empty cell. Genuine
    # multi-column data tables (Requirements, Use Cases) are preserved.
    for table in soup.find_all("table"):
        if table_max_filled_cols(table) <= 1:
            table.unwrap()
    for tag in soup.find_all(["tr", "td", "th", "tbody", "thead"]):
        if tag.find_parent("table") is None:
            tag.unwrap()

    return soup


def extract_title(soup: BeautifulSoup, fallback: str) -> str:
    if soup.title and soup.title.string and soup.title.string.strip():
        return soup.title.string.strip()
    h1 = soup.find(["h1", "h2"])
    if h1 and h1.get_text(strip=True):
        return h1.get_text(strip=True)
    return fallback


def convert_file(path: Path) -> tuple[str, str]:
    raw = read_html(path)
    soup = clean_soup(BeautifulSoup(raw, "html.parser"))
    rel = path.relative_to(SRC)
    title = extract_title(soup, rel.stem)

    # Prefer the body; fall back to the whole document.
    body = soup.body or soup
    markdown = md(str(body), heading_style="ATX", strip=["a"] if False else None)

    # Collapse runs of blank lines.
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()

    src_url = (
        "https://xanthus-consulting.com/IntelliGrid_Architecture/"
        + rel.as_posix()
    )
    header = f"# {title}\n\n> Source: {src_url}\n\n---\n\n"
    return title, header + markdown + "\n"


def main() -> int:
    if not SRC.exists():
        print(f"mirror dir not found: {SRC}", file=sys.stderr)
        return 1

    pages = []
    for path in sorted(SRC.rglob("*")):
        if path.suffix.lower() not in HTML_EXTS or not path.is_file():
            continue
        rel = path.relative_to(SRC)
        out_path = (OUT / rel).with_suffix(".md")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            title, content = convert_file(path)
        except Exception as exc:  # keep going on a bad page
            print(f"FAILED {rel}: {exc}", file=sys.stderr)
            continue
        out_path.write_text(content, encoding="utf-8")
        pages.append((rel.as_posix(), title, out_path.relative_to(OUT).as_posix()))

    # Build an index.
    index_lines = [
        "# IntelliGrid Architecture — Extracted Pages Index",
        "",
        "> Mirrored from "
        "https://xanthus-consulting.com/IntelliGrid_Architecture/",
        "",
        f"Total pages converted: **{len(pages)}**",
        "",
    ]
    by_dir: dict[str, list] = {}
    for src_rel, title, md_rel in pages:
        section = src_rel.split("/")[0] if "/" in src_rel else "(root)"
        by_dir.setdefault(section, []).append((title, md_rel))
    for section in sorted(by_dir):
        index_lines.append(f"## {section}")
        index_lines.append("")
        for title, md_rel in sorted(by_dir[section], key=lambda x: x[1]):
            index_lines.append(f"- [{title}]({md_rel})")
        index_lines.append("")
    (OUT / "INDEX.md").write_text("\n".join(index_lines), encoding="utf-8")

    img_count = sum(
        1
        for p in SRC.rglob("*")
        if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".gif"}
    )
    print(f"Converted {len(pages)} pages -> {OUT}")
    print(f"Images available in mirror: {img_count}")
    print(f"Index: {OUT / 'INDEX.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
