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

## 2026-08-25 late — first ingest (derived index established)

`harness/ingest/{schema.sql,ingest.py}` → local Postgres 18 database `empirica_glyph` (psql-18; pgvector enabled, embedding column reserved). 1,235 records from 9 JSONL files (7 pass-1 + 2 capture-correction), idempotent rebuild by construction. Views: `revision_arcs` (82 links), `glyph_occurrences`. First-look integrity: one machine-cleanliness defect found and routed to source (bracket-marks inside 11 sonnet5-1 arc ids; schema v0.9.1 rule added). First exploration tastes: `█` is the most universal glyph (7/7 surveyors); `⊂⊆` and `Ⓐ` the most-shared negatives; trigram family contested (ladder for some, negative for others); per-surveyor negative-ratio 0.13–0.41. The DB is disposable — `python3 harness/ingest/ingest.py` rebuilds it from data/ at any time.

## (next) — harness proper

Explore the ingested corpus (un-gates the tabled queue items) → protocol v1.0 freeze + PREDICTIONS → the fated-randomness runner with ledger rows per judgment, pinned models, per-item option permutation, stimulus hygiene (ban ≈/⟂/answer vocab from stimulus pools; A/B index answer fallback for echo-fragile judges). See pilot/DESIGN-scale-up.md (with its addenda) for the full spec; RECONCILIATION-QUEUE.md for gates and rulings.

## 2026-10-03 — v1.0 harness built; protocol frozen; predictions registered

Harness `harness/runner/` (stdlib Python): `fate.py` (fated seeds), `judges.py` (isolated adapters: claude CLI, ollama, grok CLI, codex exec, agy), `instruments.py` (prompts + parser p1.0), `stimuli.py` (fated held-out stimulus sets, byte-identical on rebuild), `run.py` (append-only ledger per run). Protocol: `protocol/PROTOCOL-v1.0.md` (`gmp-v1.0`). Registered predictions: `PREDICTIONS-v1.0.md`, committed before any confirmation run. Pilot re-derivations: `harness/reanalysis/` (walk2→walk3 dissolution 425/533; feature correlates over pilot edges).

| Run | Instrument | Judges | Provenance | Record |
|---|---|---|---|---|
| shakedown (adapter debugging, < 70 calls total) | triads/format/gestalt | haiku45, sonnet55, llama32-3b, grok46, gpt56terra, gemini31pro, gemini38flash | [full] ledger | `data/runs-v1/*-shakedown/` — excluded from all analyses |

Environment: darwin (Apple M4 Max, 48 GB); claude CLI 2.1.288; grok CLI 1.0.44; codex exec; agy; ollama 0.34.4. Local weights for qwen3:4b, gemma3:4b, phi4-mini, mistral:7b, gpt-oss:20b were pulled on this date for the panel (they had been absent; `ollama rm` reverses).

## 2026-10-03 — v1.0 campaign (protocol gmp-v1.0; predictions registered in commit 026cfb56 before the first data row)

The per-run record is `data/runs-v1/INVENTORY.md` (generated by `harness/runner/inventory.py`; one row per run directory with call counts, failures, UTC span, provider-reported model, list cost, and ledger sha256). Every call is one append-only row in `data/runs-v1/<run>/ledger.jsonl`. Seeds are fated (`seed = sha256(protocol || purpose || canonical(object))`), so there is no seed bookkeeping. Stimuli: `data/stimuli-v1/`; md5 recorded byte-identical across two rebuilds on 2026-10-03.

| Run family | Instrument(s) | Judges | Provenance | Record |
|---|---|---|---|---|
| main campaign, single mode | triads, conflict (3 reps), holistic, gestalt, format ×{forced, tie, perp} | haiku45, sonnet5, sonnet55, opus55 (claude -p, effort low); llama32-3b, gemma3-4b, phi4mini, mistral7b, hermes3-3b, qwen25-3b (ollama, temperature 0, seed 0) | [full] | `data/runs-v1/*-single-*` |
| main campaign, sheet mode (40 items/call) | same | grok46, gpt56terra (partial: Codex quota exhausted), gemini31pro, gemini38flash, sonnet55 (mode control) | [full] | `data/runs-v1/*-sheet-*` |
| pilot-condition arm | format tie/perp, pilot-replication stratum | claude-sonnet-5-5 as Claude Code Agent-tool subagents (pilot wording, 80-item sheet files) | [full] (transcripts kept outside git) | `data/runs-v1/format-*-pilotcond-sonnetagent/` |
| invalid | everything | qwen3-4b (adapter failure; no valid answers) | [full] raw kept | excluded from analysis (see PROTOCOL notes) |
| aborted | triads sheet | grok46, adapter a1 (tools leaked) | [full] raw kept | `data/runs-v1/triads-perp-sheet-grok46-aborted-toolleak/` |
| exploratory: old-SIGNA-sample-string probe (not SIGNA) | 55 pairs × 2 orders + 3 gestalt shuffles | frontier judges, llama32-3b, glimmer30b | [full] | `data/runs-v1/signa-*` |
| exploratory: top-40 battery | adjacent rungs × 2 orders + 2 gestalt shuffles, batches a and b | frontier judges, llama32-3b, qwen25-3b, some other local models | [full] | `data/runs-v1/top40*` |
| exploratory: Meta Muse Glimmer 30B (llama.cpp, sheet mode) | conflict, old SIGNA sample string, holistic | glimmer30b | [full] | `data/runs-v1/*glimmer30b*` |

Environment: Apple M4 Max 48 GB, darwin; claude CLI 2.1.288; grok CLI 1.0.44; codex exec; agy; ollama 0.34.4; llama.cpp b10358. Model ids as reported by each provider are in every ledger row.

### Lineage note (2026-10-03, after the campaign)

Each run in `data/runs-v1/INVENTORY.md` now carries a lineage class: A = fixed by rule or pilot, B = builder-chosen, C = driven by the old SIGNA sample string. The definitions and the reasons are in `data/stimuli-v1/LINEAGE.md`. The "exploratory: old-SIGNA-sample-string probe" row above is class C. It exists because of the coordinating agent's brief, not a request of Joseph's; Joseph has since reframed it, post hoc, as a control (see LINEAGE.md for the reframing and its limits).
