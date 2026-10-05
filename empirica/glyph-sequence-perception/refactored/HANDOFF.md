# HANDOFF: state of the refactored study (2026-10-05, ~12:05 MDT; the coordinating session ends here)

*Written by the coordinating instance (Claude Opus 5.5) for the session that continues the work on its own (Joseph, 2026-10-05: "pick up a new one that doesn't have a coordinator attached to it to continue the work here in glyph-land independently"). Read METHODOLOGY.md first; this file is state and open threads, not method. Joseph's earlier sessions also hold context: his messages relayed through the coordinator are quoted here where they matter.*

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

## Running now (updated 2026-10-05 ~12:40 MDT by the independent session)

**How rounds run now.** Claude drives the cadence, and every other family drains asynchronously (Joseph: *"go ahead and move forward without stopping on claude responses, but … start slowing down the claude responses a bit so that I don't hit my claude quota before it resets tomorrow AM. Once they are running asynchronously, we should go ahead and really slow down gemini again to see if that helps"*). Three processes run, all from `refactored/`:
- `python3 -u run.py loop --budget 700 >> data/logs/loop.log`. Each round plans, asks only the Claude minds, re-records *every* round so that drained answers fold in, then builds the tree and progress and commits.
- `python3 -u run.py drain --minds gemini38flash gemini31pro >> data/logs/drain-gemini.log`
- `python3 -u run.py drain --minds grok46 >> data/logs/drain-grok.log`

The drains ask their minds' open sheets, oldest round first, and idle when caught up. **Pacing** is in `pace.json`, re-read before every call, so it can be edited live. It started at Claude 2 workers / 20 s, Gemini 1 worker / 60 s and Grok 6 workers. **To stop everything:** `touch data/rounds/STOP`. The loop stops after its current round; the drains stop at their next check.

**Gemini's empty answers are tool attempts, not rate limits.** Every empty Gemini answer checked (172 in c001 and r012) was a soft-denied `run_command`, almost all `python3 -c … unicodedata.name(…)`, a few `chr()` ranges. No successful answer used a tool. So, as of this change:
- **agy adapter `a2-transcript`** copies each call's thinking and tool calls into the ledger (`adapter_meta.steps` / `tool_calls`). agy keeps only its ~500 latest conversations; the 455 that survived from c001 and r012 were harvested to `data/agy/` (transcripts committed, sqlite dbs gitignored).
- **Outcome `tool-attempt`**, with the command kept. A sheet that drew one is re-asked with prompt variant `no-lookup`, and records are split and tagged by variant. METHODOLOGY §4 has the reasoning, and Joseph's call for a separate *reasoned* pass where a lookup tool works.
- **Spike under way:** a Unicode-lookup MCP server (no shell) at `~/src/arch/firmatum/utils/…` (the agent names it). The coordinator commissions its verification.
- **Latent hole:** the judges' agy loads Joseph's personal allow-list (`grep`, `head`, `ls`, `diff`, `wc`, some `curl`s) from `~/.gemini/antigravity-cli/settings.json`, so those commands would run unprompted. None ran so far, and every tool call is now in the ledger. An isolated HOME fixes it but breaks keychain auth and pops a dialog on Joseph's screen. **Don't change HOME for agy.**

**The embedding spike's verification landed** (`spikes/embedding-tendrils-2026-10-05/de-novo-feedback-1.md`, committed). Most numbers reproduce. The "~80% next code point" share is mostly alphabet knowledge: where alphabet and chart disagree, every family puts the alphabet first. **So follow-up (a) below, a plain ±1 "chart order" tag, would mark most genuine runs, and should not be built as written.** The report proposes a narrower tag (discriminator positions; the chart glyph as runner-up) and a cheap probe.

**Haiku is the Claude quota hog:** ~5.7k output tokens per sheet at "low" effort (c001: $6.72-equivalent, against $2.23 for Sonnet). `pace.json` can slow it alone with `"minds": {"haiku45": {...}}`.

**Earlier pending follow-ups from the spike**, as the coordinating session left them, revised by the verification:
  - (a) A "chart order" read-off: superseded by the verifier's narrower tag, above.
  - (b) Unicode-name siblings in exploration (`priority/plan.py` `explore`). The verifier confirms a smaller gain (cp-far hit@30 0.54 → 0.68–0.74 without CJK). It also notes that names and codepoint are the *same* source (Unicode's own metadata), and suggests a share of kernels drawn from neither.
  - (c) For Joseph: chart-following is a measurement-validity question. It is now narrower; see METHODOLOGY §4.
  - (d) Spiker feedback for future briefs: state who else is using the machine.
  - (e) Spike code still excludes `⟂ ⊥ ≈`. Harmless.

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
