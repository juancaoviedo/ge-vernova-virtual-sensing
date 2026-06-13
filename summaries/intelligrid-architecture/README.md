# IntelliGrid Architecture — Full Site Extraction

A complete crawl and Markdown extraction of the **IntelliGrid Architecture** (formerly IECSA — Integrated Energy and Communications System Architecture) reference website published by EPRI / Xanthus Consulting.

## Source

- **Entry point:** <https://xanthus-consulting.com/IntelliGrid_Architecture/Overview_Guidelines/Intelligrid_index.htm>
- **Site root:** <https://xanthus-consulting.com/IntelliGrid_Architecture/>
- **Crawled:** 2026-06-13
- Copyright EPRI 2004. Captured here for reference/research use.

> This is the web edition of the same document set summarized in [`../../docs/patent-report.md`](../../docs/patent-report.md) (EPRI report 1012160). The website contains far more detail — the full Use Case library, all 20 Environments, the complete technology catalog, requirements, and glossary.

## What was captured

| Item | Count |
|---|---|
| HTML pages → Markdown | **935** |
| Images (jpg/png/gif) | 771 |
| Linked PDFs (the IECSA Volumes & appendices) | 38 |
| Raw mirror size | ~123 MB |
| Markdown size | ~21 MB |

## Folder layout

```
intelligrid-architecture/
├── README.md                 ← this file
├── convert_to_markdown.py    ← HTML→Markdown converter used
├── wget-crawl.log            ← full crawl log
├── mirror/                   ← raw wget mirror (HTML + images + PDFs, links rewritten for offline browsing)
└── markdown/                 ← extracted Markdown, mirroring the site structure
    └── INDEX.md              ← index of every page, grouped by section
```

## Markdown sections (page counts)

| Section | Pages | Contents |
|---|---|---|
| `New_Technologies/` | 563 | Catalog of standards & technologies (IEC, IEEE, IETF, ISO, security, networking, media) |
| `Use_Cases/` | 76 | Power System Function use cases (Market, Transmission, Distribution, DER, Consumer) |
| `Requirements/` | 68 | Detailed requirement definitions |
| `Technology_Analysis/` | 61 | Strategic vision, security, network mgmt, UML model analysis |
| `Overview_Guidelines/` | 51 | Vision, guidelines, recommendations, project summary |
| `Glossary/` | 36 | A–Z glossary of terms |
| `Environments/` | 21 | The 20 IntelliGrid Environments |
| `IECSA_Volumes/` | 21 | Landing pages for the printable PDF volumes |
| `Marketing_IntelliGrid/` | 15 | Marketing / overview material |
| `High_Level_Concepts/` | 13 | Abstract modeling, security, interoperability, tactical approach |
| `FluffySearch/`, `navigation/`, `Questions_Comments/` | 10 | Site infrastructure pages |

Start at [`markdown/INDEX.md`](markdown/INDEX.md).

## How it was produced

1. **Crawler:** `wget` recursive mirror, restricted to the `/IntelliGrid_Architecture/` path, with page-requisites (images/CSS), link conversion, and polite rate-limiting (`--wait=0.3 --random-wait`).
2. **Extraction:** `convert_to_markdown.py` (Python + `markdownify` + `beautifulsoup4`) — decodes the site's Windows-1252 charset, strips the repeated navigation menu and copyright footer, unwraps FrontPage layout tables while preserving genuine data tables, and emits one Markdown file per page plus `INDEX.md`.

To re-run the conversion after re-crawling:

```bash
# from repo root; venv created during setup at .venv-crawl/
.venv-crawl/bin/python summaries/intelligrid-architecture/convert_to_markdown.py
```

## Notes / known limitations

- Each Markdown page keeps its original **source URL** in a `> Source:` header line.
- Image links point into the `mirror/` tree (relative `../images/...` paths as on the original site).
- A small banner (`IntelliGrid Architecture` logo) appears at the top of most pages — a harmless remnant of the site's header.
- One glossary entry (`Glossary/Glossary_F.md`) contains a single math symbol that has no clean text representation.
- 124 pages contain preserved multi-column data tables.
