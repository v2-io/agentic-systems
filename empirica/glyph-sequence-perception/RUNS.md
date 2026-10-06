# RUNS — glyph-sequence-perception

*Restarted 2026-10-04. Every run before this date, from the 2026-08-25 pilot through the 2026-10-03 v1.0 campaign and a run stopped on 2026-10-04, is archived with its record: `.archive/2026-10-04-magnitude-era/RUNS-2026-10-03.md` and that directory's README.*

*Per charter: date, parameters, seed, environment, output digest. Rows begin with round 0 of `PLAN.md`.*

| date | round | instruments | judges | stimuli digest | record |
|---|---|---|---|---|---|
| 2026-10-04 | synthetic validation (before r000) | full loop, 4 rounds, budget 300, 3 chains: `python3 harness/seq/round.py --data <scratch> loop 4 --synth` then `harness/seq/validate.py <scratch>` | 4 synthetic minds in 3 families with planted nuisance (slot bias, ⟂-propensity, guessing) | world `synth.world_default()` | Planted A, C, D, E recovered in full, order agreement 1.00. D's holistic signature recovered (s3 ≈ 0.1, s4 0.5–0.97). No splice candidates; the bridge-glyph trap (A/F) held. F half-grown (4 of 7 glyphs; only one side was seeded). B (never seeded) not found in 4 rounds. The rotation diagnostic found the slot-biased mind (shown-middle share 0.54 vs 0.32–0.38; 3/3 consistency 0.22 vs 0.75–0.88); the model's own slot-bias estimate is weak (all ≈ 0.5). Two fixes came out of a first validation run before this one: the witnessed-connectivity penalty (an annealed candidate had interleaved unrelated sequences), and witnesses needing ≥ 2 consistent answers and a majority (a noisy mind had knit two sequences). |
| 2026-10-04 | r000 | triad (Latin rotation, rep 0), order (2 shuffles), next, between; 1–5 presentations per sheet; protocol gsp-0.1, parser q0.1 | core: sonnet55, haiku45, grok46, gemini38flash, glimmer30b-sheet; second (fated ~20% of sheets): opus55, gemini31pro | sheets db2e31e0992d2a17 | `data/rounds/r000/`; 299 presentations on 96 sheets; pool 3,164 glyphs (2,140 seed + 1,024 uniform tail), 956 seeds (929 survey records with ≥2 valid glyphs + 27 dress-lattice chains); budget 300 |
| 2026-10-04 | r001 | as r000, plus Latin-rotation follow-ups (reps 1–2 of triads not answered ⟂ by every mind) | core API minds + second minds; Glimmer answers via `harness/seq/local-worker.sh` and lags | basis fit `data/rounds/r001/basis-fit.json` | 114 new items + 150 follow-up presentations (274 wanted) → 300 presentations on 91 sheets; fit on 12442 triple observations → 99 candidates (`report.md`) |
| 2026-10-04 | r002 | as r000, plus Latin-rotation follow-ups (reps 1–2 of triads not answered ⟂ by every mind) | core API minds + second minds; Glimmer answers via `harness/seq/local-worker.sh` and lags | basis fit `data/rounds/r002/basis-fit.json` | 114 new items + 150 follow-up presentations (217 wanted) → 299 presentations on 84 sheets; fit on 19042 triple observations → 107 candidates (`report.md`) |

*Paths in the rows above are as of their day: the triad era's `data/rounds/rNNN/` is now `data/triad-era/rounds/rNNN/`, and its `harness/` is in `.archive/2026-10-06-triad-era/` (moved 2026-10-06). Rounds r003–r012 were run but not entered here; their record is in their round directories and the git log.*

## Context-tree rounds (c001 on, from 2026-10-05; METHODOLOGY.md)

Each round is committed as it closes, and the commit is its record:

- **Parameters and stimuli:** `data/rounds/<round>/plan.json` (budget, questions by reason, Unicode version), `questions.jsonl` and `sheets.jsonl`. Random draws are keyed by round and purpose (`core/fate.py`).
- **Judges and environment:** the roster and each mind's adapter, model, effort and thinking budget are in `core/minds.json` and copied into every ledger row, with the adapter version and the prompt and system hashes. Python is `/opt/homebrew/bin/python3` with Unicode 16 (`run.py` refuses older). c001–c002 first ran on Unicode 14 and were re-recorded.
- **Output:** the verbatim ledgers `data/rounds/<round>/raw/<mind>/ledger.jsonl`. Claude minds answer in the round; the other families drain into earlier rounds' ledgers asynchronously.
- **Void rounds:** c028–c079 were planned while Claude's weekly limit refused every call (`data/rounds/VOID.json`). Their questions are planned again in live rounds.
- **Summary per round:** `PROGRESS.md`.
