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

**Claude thinking budgets** (found and changed 2026-10-05):
- **The inherited budget.** Until c001, the Claude judges inherited `MAX_THINKING_TOKENS=31000` from Joseph's shell, unrecorded. Haiku used ~5–6k thinking tokens a sheet (c001: $6.72-equivalent, against $2.23 for Sonnet).
- **Budgets are now set per mind** in `core/minds.json` and recorded in each ledger row's judge spec.
- **From c002, `haiku45nt` (budget 0, thinking off) is core and `haiku45` (31000) a second mind.** The reasoned condition stays sampled, so the change is measurable. Evidence and reasoning: `spikes/thinking-felt-2026-10-05/README.md`.
- **Sonnet isn't reached by the budget lever**; it thinks adaptively, about one sheet in five with zero.
- **This is the independent session's call, made while Joseph was away.** It is reversible in `minds.json`.

**Loop state.** c002 was started 12:51 MDT under all of the above, with `round_gap_min` 30 in `pace.json`, which gives roughly a dozen rounds by tomorrow morning.

**`tree.sequences()` fixed 2026-10-05:** a sequence now holds supported links only. Walk start contexts carried the triad era's gaps (`⑩ ⑪ ⑬ ⑭`, `㊳ ㊲ ㉒ ㉑`).

**Written answers and the five concerns (2026-10-05, evening).**
- **The bug.** The later glyphs of every continue answer were stored but used by nothing, against METHODOLOGY §4. That was a bug: never a "rule", and never "by design". Joseph: *"an implementation choice that contradicts the method document -- that's called a BUG (a serious one) -- not a RULE."*
- **The fix keeps the concerns apart.** Joseph: *"possibly mixing the 5 concerns that need to be independent? (if the BEST read of the context tree is considered a 5th concern)"*. METHODOLOGY §2a now lists read-offs as concern 5, and §4 covers the shown and written channels.
  - **The tree** stores both channels. Its walk, the planner's view, stays on shown answers.
  - **The planner** turns written continuations past shown ends into recognition questions.
  - **BEST.md** applies its own per-channel criteria. Shown-confirmed links must also not be contradicted in the reverse reading. A second table holds runs carried by written answers. Confirmed rotations are listed once, as wrapping.
- **Dropped.** A "two-family deciding context" rule, tried in between, was dropped: it fixed a read-off symptom inside the tree and the planner.
- **Don't reintroduce either kind of mixing.** If a read-off looks wrong, fix the read-off unless the answers themselves are wrong.

**Evidence and tests (2026-10-05, late evening; all in METHODOLOGY §2a, §4, §5).**
- **One standard.** The tree supplies facts (per-family counts). BEST.md decides with one rule:
  - Beta–Jeffreys per family, an equal-weight mean, 90% confidence, ≥ 2 families;
  - choice answers against 0.5, yes/no answers against near controls.

  Agreement is perceptual strength; the interval is the evidence.
- **The planner's question set:**
  - recognition with matched controls;
  - join probes (the other direction; replicate at most once);
  - thin-link replication (by answer count only);
  - falsification: skip, lengthening, and new triad questions in the triad era's wording;
  - reflection questions (§3), kept apart.
- **Triad-era triads (19,665) and order answers (5,716)** were ported but unused until now. They test every confirmed stretch.
- **Still open:**
  - order questions in the new protocol;
  - orthogonality as a soft weight in exploration (§2b);
  - triad-agreed kernels for exploration (§4);
  - per-family views;
  - Gemini pacing (Joseph's call: it lags rounds behind at 1 worker / 60 s).

**md-press here: always `--no-math`** (Joseph, 2026-10-05: *"this is the one case where you'll almost certainly want to run with --no-math"*). Since 2026-10-05, md-press only reports unless given `--fix`, and its math pass is on by default. This study's docs carry glyph sequences in plain prose (`⑳ → ㉑`, `↖ ↑ ↗`), which a Unicode-math promotion would turn into `$…$`. So use `md-press --no-math FILE`, then `md-press --fix --no-math FILE`.

**utf-mcp is installed for Joseph's own tools** (2026-10-05 ~17:10, at his go-ahead: "make the mcp server available as a tool wherever you see fit"): `claude mcp` user scope, `~/.grok/config.toml` and `~/.codex/config.toml`, each tagged (`claude-code-user`, `grok-user`, `codex-user`). The study's judges can't see it: Claude judges use `--strict-mcp-config`, which was checked live and reported `tools: []`, and grok and codex judges run in isolated homes. **It is deliberately not in agy.** The study's Gemini judges run agy in Joseph's own HOME, so a global agy server (plus the allow-rule it needs) would hand the lookup tool to the first-impression Gemini judges. Don't add it there unless the agy adapter gets its own isolated configuration first.

**Paused 2026-10-05 17:05–17:31** for Joseph's global md-press update: the loop and both drains were stopped mid-c005 (c004 had committed at 15:51) and restarted afterwards. The loop resumed c005.

**More from the same afternoon, all committed:**
- **Run on Python with Unicode 16+:** `/opt/homebrew/bin/python3 run.py …`. `run.py` refuses older data. Everything through c002 had run on mise's 3.11 (Unicode 14), so Unicode 15–16 characters were unaskable and read as "unassigned". The triad-era port, seeds and c001–c002 were re-recorded (spot checks 1,588/0).
- **Continuations into truly unassigned code points** (e.g. `𝋱 𝋲 𝋳 → U+1D2F4`) are a clean marker of code-point arithmetic. Per 1,000: haiku45 (thinking) 35, Gemini Pro 21, Flash 15, Sonnet 9, Grok 8, Opus 0. Recorded in METHODOLOGY §4.
- **The cycle rule is tightened.** A manifested cycle now needs less than a whole period shown: end questions on 4-glyph runs had shown the whole period, and the mind's repeat of it had counted. 7 of c002's 11 cycles survive, including clocks and moon phases (Claude + Grok), each with the unseen part written by the mind.
- **The loop resumes an unfinished round on start.** Restarting mid-round (`pkill -f "run.py loop"`, then start it again) is safe.
- **Answers carry their measured `thinking_tokens`.** The tree keeps 0-thinking answers as their own vector, and BEST.md shows each stretch's *unreasoned* support (Joseph: *"potentially as distinct input vectors"*).
- **The Unicode-lookup MCP server is built** at `~/src/arch/firmatum/utils/utf-mcp/` (arch commit `0420485`; README and debrief there). Its independent verification is running; its report goes to `de-novo-feedback-1.md` there. **Joseph's decision needed for agy:** it only allows MCP calls via an allow-rule in his `~/.gemini/antigravity-cli/settings.json` (`proposed-integration.md` §3). A tools-on *reasoned* pass in the study is not built yet.

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
