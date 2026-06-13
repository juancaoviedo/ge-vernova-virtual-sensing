---
quick_id: 260613-gyx
slug: extract-three-new-agms-patents-logistici
date: 2026-06-13
status: complete
---

# Summary: Extract three new AGMS patents and integrate into INDEX.md

## What was done

Three newly-added image-only patent PDFs in `docs/` were OCR'd and extracted into
structured study notes matching the existing `.planning/research/patents/` format, then
integrated into `INDEX.md`. The director's patent family is now documented as **six
distinct patents** (was three).

## New patents extracted

| File | Title | Publication | Notable |
|------|-------|-------------|---------|
| `logistician-module.md` | Logistician Module for AGM | US 2024/0337997 A1 (App 18/131,743) | Logistics orchestrator (1023A): builds/procures/audits the provisional logistics list; owns inter-ORACS gap files |
| `operation-loop.md` | Operation Loop Formation for AGM | **US 12,596,341 B2 (GRANTED, 2026-04-07)** | **Granted, assigned to GE Vernova Infrastructure Technology LLC.** Formation construct module (1400): schema/DNA match → meta objects → simulate-before-commit (claim 3) → execute |
| `scout-command.md` | Scout Command for AGM | US 2024/0339835 A1 (App 18/131,781) | Scout deployment: Incubator Manager (1445) role-assigns + clones scouts; Launch Manager (1447) builds launch plan |

## Key findings worth remembering

1. **Operation Loop Formation is a GRANTED US patent assigned to GE Vernova itself**
   (not the parent's "General Electric Company") — strongest "I read your live IP"
   interview talking point. Its allowed claim 3 puts *simulate-before-commit* into the
   enforceable claims, mapping directly onto Juan's CVXPY MPC solve-before-commit work.
2. **The five continuations form one assembly line** kicked off by the parent's CaCSM:
   Logistician (*which*) → Asset Portfolio Manager (*verify*) → Operation Loop Formation
   (*assemble + simulate*) → Scout Command (*deploy*). Documented as a pipeline diagram in INDEX.md.
3. **ORACS acronym drift:** parent/Asset-Portfolio notes gloss it as Operation+Role+Asset+
   Context+Scouts; the newer Logistician and Operation Loop patents gloss it as the
   operational-index set (Observability, Reachability, Adaptability, Controllability,
   Security). Flagged in INDEX.md and the individual files rather than silently resolved.
4. **Authoritative application numbers** (front-page, since OCR docket cross-refs were
   garbled): Logistician 18/131,743; Asset Portfolio 18/131,758; Operation Loop 18/131,770;
   Scout Command 18/131,781; Data Management 18/131,790 — all 2023-04-06, all tracing to
   PCT/US2022/046851.

## Process notes

- OCR via `ocrmypdf --force-ocr --optimize 0` (the `jbig2` optimizer binary was unavailable
  / not packaged for this Ubuntu; `--optimize 0` skips it with no impact on text quality).
  Text extracted with `pdftotext`; ~176–178K chars per patent. OCR artifacts kept in `/tmp`,
  not committed.
- Three parallel extraction agents (one per patent) wrote the summaries; INDEX integration
  and cross-patent reconciliation done in the main thread.

## Files

- Created: `.planning/research/patents/logistician-module.md`
- Created: `.planning/research/patents/operation-loop.md`
- Created: `.planning/research/patents/scout-command.md`
- Updated: `.planning/research/patents/INDEX.md` (rewritten for six patents)
- Updated: `.planning/STATE.md` (added Quick Tasks Completed section)
- Source PDFs added to `docs/`: `patent-logistician-module.pdf`, `patent-operation-loop.pdf`, `patent-scout-command.pdf`

## Not in scope of this commit

- `docs/patent_ocr.pdf` deletion (pre-existing uncommitted working-tree change, unrelated).
