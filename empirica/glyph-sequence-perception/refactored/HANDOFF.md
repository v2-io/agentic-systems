# HANDOFF: state of the refactored study (updated 2026-10-05 ~22:15 MDT by the independent session)

*Written by the coordinating instance (Claude Opus 5.5) for the session that continues the work on its own (Joseph, 2026-10-05: "pick up a new one that doesn't have a coordinator attached to it to continue the work here in glyph-land independently"). Read METHODOLOGY.md first; this file is state and open threads, not method. Joseph's earlier sessions also hold context: his messages relayed through the coordinator are quoted here where they matter.*

## What exists

The study now lives in `refactored/`. It is to become the project root, and the triad-era files one level up will move to `.archive/triad-era/` once Joseph and the coordinator are confident.

| path | concern | what it does |
|---|---|---|
| `METHODOLOGY.md` | — | the method: the goal (sequences recognised as sequences, §1), the 5 concerns and the one evidence standard (§2a), negative evidence, the questions (§4), the recognition tests and the generator (§4a), priority (§5), porting (§6) |
| `port/port_triad_era.py`, `port/spotcheck.py` | 4 | ledgers r000–r012 → `data/answers/triad-era.jsonl` (34,196 records; 0 mismatches in 1,588 spot checks); `data/answers/PORT-REPORT.md` |
| `port/port_seeds.py` | 3→2 | survey sequences → `data/answers/seeds.jsonl`: 4,850 tagged votes from the surveyor's family |
| `probe/probe.py` | 1 | protocol `ctx-0.1`: question kinds `continue`, `inhibit`, `triad`, `cohere` (a whole run: coherent? why?), `pick` (forced single character, sampled); prompts, fated sheets, raw answers → canonical records |
| `tree/tree.py` | 2 | context tree → `SEQUENCES.md` (`--pure` leaves seeds out) |
| `priority/plan.py` | 3 | the planner: 15% hot exploration; tiers across sequences (ends + cycle probes, seed-only steps, k\*, branch inhibits, inside contexts); recognition with controls; whole-run coherence; the pick tendrils |
| `report/best.py` | read-off | `BEST.md`: runs recognised as wholes, rejected wholes, candidates grown from the strongest edges; nothing reads it back; reloaded by the loop every round |
| `run.py` | — | `plan / ask / record / tree / progress / round / loop` |
| `core/` | — | judges, fate and the roster, copied from `../harness/core` |

Everything in `data/answers/` and `data/tree/` is regenerable and gitignored. To rebuild it after a fresh clone, run `port/port_triad_era.py`, then `port/port_seeds.py`, then `run.py record <rid>` for each context round. The truth, which is committed, is the verbatim ledgers: `data/rounds/<rid>/raw/<mind>/ledger.jsonl`, plus `questions.jsonl`, `sheets.jsonl` and `plan.json`.

## Running now (2026-10-05 ~22:15 MDT)

**Four processes**, all from `refactored/`, all on `/opt/homebrew/bin/python3` (Unicode 16+; `run.py` refuses older):
- `run.py loop --budget 700 >> data/logs/loop.log`: plans a round, asks the Claude minds (core, second, generator `sonnet55g`/`haiku45g`), re-records every round so drained answers fold in, builds tree, BEST and progress, commits. Rounds take ~7 minutes (`round_gap_min` 0).
- `run.py drain --minds gemini38flash gemini31pro gemini38flashg >> data/logs/drain-gemini.log`: at 1 worker / 60 s (Joseph's quota call), many rounds behind (at c003 at 22:00).
- `run.py drain --minds grok46 >> data/logs/drain-grok.log`: about 40 minutes a round, slowed by a tail of 600 s timeouts; at c011 at 22:00, so its first coherence answers (c015) arrive around 00:30.
- `run.py drain --minds grok46g >> data/logs/drain-grok-gen.log`: the Grok generator mind in its own drain (3 workers), since its sheets start at c017.

**Pacing** is in `pace.json`, re-read before every call. **To stop everything:** `touch data/rounds/STOP`.

**Restarting safely.** The loop imports the planner, probe and tree once, so their changes need a restart. BEST is reloaded every round and doesn't. Restart while the log's last line is `cmd_ask`, by process ID: `kill <pid>` (from `pgrep -f "run.py loop"`), wait for it to exit, then start it again. It resumes the unfinished round. Two scars from tonight:
- `pkill -f "run.py loop"` inside a script kills the script too, because its own command line matches.
- A failed kill followed by a start leaves two loops. Check `pgrep -f "run.py loop"` after every restart.

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
  - reflection questions (§3), kept apart;
  - triad-agreed kernels: a third of exploration, weighted by agreement (§4, §7).
- **Triad-era triads (19,665) and order answers (5,716)** were ported but unused until now. They test every confirmed stretch.
- **Still open:**
  - order questions in the new protocol;
  - orthogonality as a soft weight in exploration (§2b);
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

## The evening of 2026-10-05: recognition is the goal

Joseph, after the cross-block sequences turned out to be invisible in BEST: *"generation is for exploring the space but also counts as a recognition, but recognition is the final goal — 'best recognized sequences as sequences' is the goal"*. METHODOLOGY §1, §2a, §4a and §5 now say so, and these were built (all committed):
- **The cause.** BEST confirmed links only by majority in continue answers, with "none" counting against: one kind of evidence among many, used against §2b's own sentence. Joseph's morph ladder `-=>})|` (the founding example of the survey's morph family) was invisible. Its continue answers are "none" or `]`, while two families put `)` between `}` and `|` in triads. My first report called that "none" honest. That was wrong: it was my impression standing in for a measurement.
- **Generation is one-way evidence.** "None" is about ends; only a "no" beyond a control counts against a link.
- **The cohere question** (Joseph's wording: *"does this look like a coherent sequence? why?"*). 80 whole runs a round, each with a shuffled control and never on the same sheet. Chart windows are kept as a measurement, not a decoy. Shuffles a mind called coherent become candidate runs (Joseph: *"I can absolutely attest to seeing ideated sequences that are better after some shuffling"*).
- **The generator: tendrils of forced picks** (Joseph's design, quoted in METHODOLOGY §4a). *"Pick a single character that would extend this sequence. You may be creative, but give a reason"*, at medium effort, 5 samples per generator mind. Every answer is a branch, extended in later rounds, prioritised on an S-curve with a long tail (Efraimidis–Spirakis order). Branch paths go to coherence. My first build stopped every path at one step; Joseph: *"do you not understand the mission here???"*. It grows now: `O o ᵒ ₒ`, `∰ ∯ ∮ ∫`, `→ ⇒ ⇉ ⇛ ⇶ ⟹ ⟾`, `⫴ ∥ ∣ ⊥ ⊤`.
- **BEST.**
  - The main table is runs recognised as wholes.
  - Candidates are grown from the strongest edges along the strongest branch, with no merging.
  - One family suffices (Joseph dropped the ≥ 2 cap). Per-family counts are on every row.
  - **│** marks a break: a link confidently weaker than its run, judged from the links' posteriors (Joseph: *"Don't we have real confidences?"*).
  - It builds in ~1 s.

**What the first data say** [Claude only so far]:
- **Coherence discriminates order.** Sonnet said yes to 76 of 80 real runs and 2 of 80 shuffled ones. Haiku with thinking off said yes to 12 of 80 shuffles, reading "coherent" as "a coherent set". Its own control rate absorbs that.
- **It doesn't rank ordered runs.** 229 of 240 asked runs are recognised, chart walks and interleavings included.
- **The whys show chart reasoning** (*"consecutive Unicode code points"*). For Joseph: does that count as felt, or as the reasoned arithmetic signa should replace? Haiku with thinking off also says yes to chart windows (16 of 21), so low effort alone won't separate them. The other families will show whether it's universal.
- **Stopping branches on spread** (Joseph's suggested rule; he left the maths to me). First look, Claude only, 44 parent-to-child pairs: flat parents had flat children in 7 of 20 cases, structured parents in 9 of 24. That's no sign yet that flatness persists, so nothing is stopped. Re-run it when Grok's picks are in.

## Open threads and decisions

- **The order question** (§4a): put a shuffled set in order. Next to build; it finds the *best* order, not only whether a given one holds.
- **Not built from §4a:** swap detection, two-alternative next, gap fill, the effort contrast, and the rest of the list. Branch inhibits (tier 4) and inside contexts (tier 5) still get no budget.
- **Runs over 24 glyphs** can't be asked whole. Windows of them would be fair game for coherence; nothing does that yet.
- **The whys** (coherence and picks) are saved, not analysed, per Joseph.
- **Gemini** lags many rounds (Joseph's pacing). Grok newest-first was offered and not decided.
- **The arrow row** `↓ ↘ → ↗ ↑ ↖ ←` missing `↙`, the hex question (`…8 9 → ?`), and the spinner canary `| / - \` remain watch items.
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
- **The goal:** *"'best recognized sequences as sequences' is the goal"*. Generation explores and counts as a recognition, one way.
- **Never exclude, weight:** *"I wouldn't outright exclude *anything* — when I do stochastic work I always use s-curves with there always being a long tail."*
- **Prompt wording matters:** *"'Choose a single symbol' — not 'Choose the one symbol' which implies there is one expected answer."*
- **BEST:** one family suffices (*"Let's drop the >= 2 model family cap in 'best'"*); sort by length, but length isn't the ranking; │ is *"just a visual aide"*.
