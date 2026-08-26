# RUNS — glyph-magnitude-perception

*Per charter: date, parameters, seed, environment, output digest. Pilot rows are provenance-graded (see MANIFEST honesty note): `[full]` = seeded+parameterized, `[partial]` = prompts+run-id recorded, no per-call pins.*

## 2026-08-25 — pilot day (protocol v0.9, evolving during the day)

| Run | Instrument | Judges | Provenance | Record |
|---|---|---|---|---|
| probe (pairs, ASCII sym, uncounterbalanced) | pairwise | llama3.2:3b t0/0.7 seed 20260825 | [full] | pilot/results-llama3.2_3b.jsonl |
| probe2 (pairs, ASCII sym, both orders) | pairwise | llama3.2:3b | [full] | pilot/results2-llama3.2_3b.jsonl |
| probe3 (pairs, glyph-echo, both orders) | pairwise | llama3.2:3b | [full] | pilot/results3-llama3.2_3b.jsonl |
| probe5 (closed protocol on triad sheets, per-item option perms) | triads | llama3.2:3b t0 seed 555 | [full] | pilot/results5-llama3.2_3b.jsonl |
| battery1/2 (symbol vs glyph-echo judge rounds) | pairwise | Sonnet ×6+6 | [partial] wf_428f0aea, wf_e4e17a04 | pilot-record.md §Results |
| graded battery (7-operator) | pairwise-graded | Sonnet ×6 | [partial] wf_3a5d0a20 | pilot-record.md |
| walk1 (uniform random pool 278) | discovery | Sonnet ×12 | [partial] wf_89b68086 | pilot-record.md |
| walk2 (densified 60/25/15) | discovery | Sonnet ×12 | [partial] wf_0e31665e | pilot-record.md |
| walk3 (⟂ rerun, same sheets) | discovery | Sonnet ×12 | [partial] wf_545a1ae1 | pilot-record.md |
| walk4 (graded glyph-echo + ⟂) | discovery | Sonnet ×12 | [partial] wf_a6881e52 | pilot-record.md |
| walk5/5b (triads, fixed vs permuted options) | triads | Sonnet ×12+12 | [partial] wf_015b9497, wf_2a3d4efa | pilot-record.md |
| conflict battery | axis-conflict | Sonnet ×8 | [partial] wf_1f85e030 | pilot-record.md |
| morph battery | pairwise | Sonnet ×8 | [partial] wf_be11f829 | pilot-record.md |
| gestalt reconstruction | whole-set | Sonnet ×6 | [partial] wf_e56e578d | pilot-record.md |
| extension generation | generative | Sonnet ×6 | [partial] wf_0392c567 | pilot-record.md |
| unnamed continuation | generative | Sonnet ×6 | [partial] wf_dd71ae5f | pilot-record.md |
| salted reconstruction | membership | Sonnet ×10+5 | [partial] wf_c9bc51cc | pilot-record.md |
| de-novo surveys | introspective | Sonnet ×4 | [partial] wf_428f0aea (survey arm) | data/surveys-v1/ |

Environment: darwin 25.5.0; ollama local; Claude Code workflow subagents (model 'sonnet', session defaults). Task/key JSONs and scripts: `../data/judgments-v0/` + `harness/pilot-scripts/` (migrated from msc/ working dirs, since deleted).

## (next) — first harness-ledger run

Not yet run. Must be [full]: ledger row per judgment, pinned model versions, seeded shuffles, per-item option permutation, stimulus hygiene enforced.
