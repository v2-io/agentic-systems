# HANDOFF: state of the refactored study (2026-10-05, ~11:40 MDT)

*Written by the coordinating instance (Claude Opus 5.5) near the end of its context window, for whoever continues: me after compaction, or a fresh instance. Read METHODOLOGY.md first; this file is state and open threads, not method.*

## What exists

The study now lives in `refactored/`. It is to become the project root, and the triad-era files one level up will move to `.archive/triad-era/` once Joseph and the coordinator are confident.

| path | concern | what it does |
|---|---|---|
| `METHODOLOGY.md` | — | the method: context tree, the 4 concerns, negative evidence, porting, seeds as tagged votes |
| `port/port_triad_era.py`, `port/spotcheck.py` | 4 | ledgers r000–r012 → `data/answers/triad-era.jsonl` (34,196 records; 0 mismatches in 1,588 spot checks); `data/answers/PORT-REPORT.md` |
| `port/port_seeds.py` | 3→2 | survey sequences → `data/answers/seeds.jsonl`: 4,850 tagged votes from the surveyor's family |
| `probe/probe.py` | 1 | protocol `ctx-0.1`: `continue` and `inhibit` questions, prompts, fated sheets, raw answers → canonical records |
| `tree/tree.py` | 2 | context tree → `SEQUENCES.md` (`--pure` leaves seeds out) |
| `priority/plan.py` | 3 | the planner: 15% hot exploration; tiers across sequences (ends + cycle probes, seed-only steps, k\*, branch inhibits, inside contexts) |
| `report/best.py` | read-off | `BEST.md`, the stretches confirmed by real minds; nothing reads it back |
| `run.py` | — | `plan / ask / record / tree / progress / round / loop` |
| `core/` | — | judges, fate and the roster, copied from `../harness/core` |

Everything in `data/answers/` and `data/tree/` is regenerable and gitignored. To rebuild it after a fresh clone, run `port/port_triad_era.py`, then `port/port_seeds.py`, then `run.py record <rid>` for each context round. The truth, which is committed, is the verbatim ledgers: `data/rounds/<rid>/raw/<mind>/ledger.jsonl`, plus `questions.jsonl`, `sheets.jsonl` and `plan.json`.

## Running now

- **The loop:** `nohup python3 -u run.py loop --budget 700 >> data/logs/loop.log` (started from `refactored/`). Round c001 was planned with the old sequence-first order and finishes around 12:15 MDT. `data/rounds/STOP` was set, so the loop stops after c001; a background waiter then removes STOP and restarts the loop. **Check:** `tail data/logs/loop.log`, and confirm that c002's `plan.json` has `by_tier`.
  - Each round commits itself (ledgers, SEQUENCES.md, PROGRESS.md, BEST.md) and takes about 50–60 minutes. The bottleneck is Gemini Flash, whose agy adapter runs one call at a time.
  - **To stop it:** `touch data/rounds/STOP`; the loop stops after the current round.
- **The triad-era loop is finished:** r012 was committed, and its fit was killed because it fed nothing.
- **Embedding spike: landed and committed** (`cc05dc89`; entry point `spikes/embedding-tendrils-2026-10-05/README.md`, `debrief.md` for Joseph, `no-go.md`). **An independent verification is running** (bare brief). Its report goes to `de-novo-feedback-1.md` in the spike directory: commit it, then act. The spiker's claims, *unverified until then*:
  - Bare-glyph embeddings fail.
  - Unicode *names* help on jumps between blocks: interleaved with codepoint order, they raise recall@30 where codepoint order fails from 0.52 to 0.67–0.74. A no-model name matcher is in `work/rankers.py` (`name_num_scores`).
  - **Codepoint order leaks into the minds' answers.** About 80% of first proposals on never-shown glyphs are the next code point; Claude about 57%, Gemini about 30% and Grok rarely on the obscurest glyphs. Their tests at the boundaries of UTF-8 byte-length ranges point to knowledge of the Unicode charts, not a tokenizer artefact.
  - Lines and axes in embedding space are a no-go in the spaces tested.
- **What follows if it verifies, all pending:**
  - **(a) A "chart order" read-off.** Mark links where the next glyph is the codepoint neighbour (±1). That is a property of the glyph pair, so it is a legitimate read-off, not provenance. It would let chart-following sequences be weighed or split out in SEQUENCES.md, BEST.md and PROGRESS.md.
  - **(b) Unicode-name siblings in exploration,** alternating with codepoint-neighbour partners (`priority/plan.py` `explore`).
  - **(c) For Joseph:** chart-following is a measurement-validity question. Answers that follow the chart may be chart knowledge rather than perception, especially from Claude and Gemini. The spike also suggests that some triad-era rows (`ⅱ … ⅻ ⅼ`, `㈠ … ㈨ ㈪`) follow the chart.
  - **(d) Spiker feedback for future briefs:** state who else is using the machine. It ran a local LLM on the GPU for about an hour, and Joseph noticed the heat.
  - **(e) Spike code still excludes `⟂ ⊥ ≈`.** Harmless to the study.

## Open threads and decisions

- **Tier starvation.** With ends first, tiers 3–5 (k\*, branches, inside contexts) will get little budget while open ends are plentiful. This is Joseph's rule taken at its word. Watch PROGRESS: "k\* known / steps" and the open ends count. If k\* never moves, raise it with Joseph rather than inventing shares.
- **The arrow row** `↓ ↘ → ↗ ↑ ↖ ←` is missing `↙` (Joseph caught it). Its end questions are in c002's plan. Cycle probes follow if the walk wraps.
- **Hex:** whether `…8 9 → ?` yields `A` was Joseph's early question. The question is now in the tier-5 inside work.
- **The spinner canary** `| / - \`: exploration draws printable ASCII at weight 4, and nothing is seeded. Watch BEST.md's cycles table.
- **Gemini speed and rate limits** (Joseph: *"go ahead and speed up gemini for now. When we start hitting rate limits we can let claude go ahead ideally so we can start at least getting the claude-supported sequences well defined in the data."*). In `run.py`:
  - `AGY_WORKERS = 3`, from c002.
  - `GRACE_MIN = 20`: once every Claude mind has finished a round, the other minds get 20 more minutes. Then the round moves on, and their unanswered sheets stay open.
  - **Backfill** with `run.py ask <rid>`, then `run.py record <rid>`, `tree` and `progress`. The ledgers resume.
  - **Watch** each round's ledger for errors: rate limits show up as error strings in `result.error`. Also check that agy runs cleanly at 3 concurrent sessions; that's untested.
- **The agreement cut-offs** (0.75 in BEST.md and in PROGRESS's "settled") are read-offs chosen without evidence. Joseph: *"I suspect it will be kind of a relative number or a soft threshold."*
- **Not yet built:**
  - the reflection probe (`7 8 9 8 → ?`), METHODOLOGY §3;
  - triad and order checks in new rounds (the tree uses the ported triads only as a check column);
  - a Postgres index (kept in reserve; the in-memory tree builds in about a second);
  - per-family BEST.md views.
- **Archive move:** `../harness`, `../PLAN.md`, `../STANDINGS.md`, `../PROGRESS.md`, `../data/growth` and the rest of the triad era go to `.archive/triad-era/`, and `refactored/` becomes the root. **Wait for Joseph's word.**

## Joseph's standing directions this session

Verbatim where it matters:
- **Priority rule:** *"various minds start to find a sequence … extend that sequence to the right and to the left as far as they will go while still spending time looking for other 'kernels' … square away the most obvious and stable (empirically) sequences"*, and *"15% of our effort was always 'hot'."*
- **Nothing discarded:** *"I don't understand why there is some sort of consolidation work anymore at all … that throws away good data because it's not supported enough."*
- **No invented rules:** *"I'm so sick of rules invented for no reason."* Every chosen number is listed as a parameter chosen without evidence.
- **Cycles:** counted only when manifested (*"at the moment the entire pattern has repeated itself"*), with at least 4 distinct glyphs, and probes never spoiling the beginning.
- **Seeds:** count as tagged votes, *"segregate those out if we need a more pure analysis"*.
- **Answer options** are words, never glyphs.
- **Glyph draws:** printable ASCII 4 : 2-byte 3 : 3-byte 2 : 4-byte 1.
- **Local models:** skipped for now. Glimmer is not on the roster.
- **Commits:** scoped to the study, with the attribution lines from the session's system reminder.
- **Delegation:** use peer briefs (AGENTIC-DELEGATION). Joseph is persuadable, and wants honest pushback over compliance.
