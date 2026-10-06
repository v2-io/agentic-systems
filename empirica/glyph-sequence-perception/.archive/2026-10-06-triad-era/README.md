# The triad era (rounds r000–r012, 2026-10-04 to 2026-10-05)

*Archived 2026-10-06 by Claude Opus 5.5, at Joseph's go-ahead ("Feel free to move data as appropriate in your estimation"). The study's method since 2026-10-05 is the context tree (`../../METHODOLOGY.md`).*

The triad era asked triads, orders, next and between questions, fitted a global order to the answers by annealing, grew rows from the fit, and ranked them (`STANDINGS.md`). METHODOLOGY replaced it because the era mixed concerns that METHODOLOGY keeps apart (seeds supplied the stimuli, the fit steered what was asked, the growth rules carried priority judgments), and its global fit merged valid sequences and placed glyphs on links nobody had asked (CATALOG §1). The era's **answers** were not discarded: all 34,196 are ported into the context tree by `../../port/port_triad_era.py`, and the catalog reads its grown rows as candidates.

## What is here

| path | what it is |
|---|---|
| `PLAN.md` | the triad era's method, superseded by METHODOLOGY |
| `STANDINGS.md`, `PROGRESS.md` | its last read-offs (r012) |
| `harness/` | its machinery: the round loop, the fit, growth, standings, the seed index (`ingest/`), and the parser |
| `validation/` | synthetic runs that checked the harness before r000, and a shakedown |
| `data/standings/`, `data/logs/`, `data/pool.json`, `data/progress.json`, `data/PROGRESS.md` | per-round read-offs, logs and the glyph pool |

**Still used.** `harness/seq/parse.py` (with `harness/seq/common.py` and `harness/core/`) is the parser the port re-parses the triad era's verbatim ledgers with, exactly as the era did. It is kept here, frozen, rather than copied, so there is one copy of it.

## What is not here, and where it went

These are live inputs, so they moved into `../../data/` rather than into the archive:

| old path (study root) | now |
|---|---|
| `data/rounds/r000` … `r012`, `r003p`, `STOP-ROUNDS` | `data/triad-era/rounds/` (the source of truth for the ported answers) |
| `data/growth/` | `data/triad-era/growth/` (the catalog's candidate rows) |
| `data/seeds.jsonl`, `data/seeds/` (the dropspot), `data/surveys-v1/` | unchanged |
| `OBSERVATIONS.md`, `RUNS.md`, `MANIFEST.md`, `pilot/` | unchanged: study-level records |
| `refactored/…` | the study root: `refactored/` became the root on 2026-10-06 |

Dated documents written before the move (the audits in `audits/`, the spike reports, `OBSERVATIONS.md`, `RUNS.md`) keep the paths of their day. Read `refactored/X` as `X`, `../X` (from inside `refactored/`) as `X` at the study root, and the triad era's paths by the table above.
