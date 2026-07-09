# Findings — cluster 09: tooling / automation / capability-utilization

*2026-07-07. The gap between what the Claude Code harness / ecosystem offers and what `~/src/agentic-systems` actually uses, mapped against the project's real bottleneck (bandwidth + decision-routing), not as a generic feature tour. All counts and file states verified firsthand this session; where I relay a doc's claim without independent proof I say so.*

## Headline

The project has **out-invented the harness at the cognitive layer and under-used it at the mechanical layer** — and those are the same fact. Its own emergent methodology (the de-novo "agentic reading" audit) is a more sophisticated instrument than anything the harness ships, yet it runs entirely by hand: no scaffolder, no enforcement, no state. Meanwhile the automation surface underneath is nearly empty — **zero git hooks, zero project subagents, one MCP server, no scheduled agents, and a gitignored config file that is a graveyard of dead `act`-era permissions**. The highest-leverage adoptions are the three or four harness primitives that would carry processes the project *already runs manually*, plus one seam aimed squarely at the decision-routing bottleneck.

---

## (a) De-facto processes actually running

1. **De-novo "agentic reading" audit** — the crown-jewel emergent method. `doc/de-novo-audit-instructions.md` (703 lines). Reads segments one-at-a-time with a written orient-cascade reflection between each, explicitly framed as the theory auditing itself. **Evidence it is real and heavily used:** 22 `AUDIT-WORKING-NNNNNN/` directories on disk + 4 `audit-*-FINAL-*.md` reports (2026-05-10 → 2026-07-02). Fully manual — the SOP *pleads in prose* for discipline (don't batch reads §4.4, don't delegate comprehension §3.1) that no tool enforces.

2. **Parallel multi-agent mining** — hand-orchestrated fan-out for large surveys. Git-attested: `a6774dc` ("4 parallel agents → 81 findings"), `592c115` ("99 spike files surveyed via 3 parallel agents"). Uses `Task` subagents for *discovery* (the SOP's sanctioned use), reconciled by a parent. No reusable harness; each fan-out is re-orchestrated per session.

3. **Generated-artifact refresh pipeline** — mature and real. `bin/refresh-all` (Ruby) chains `extract-findings` → `extract-recent-progress` → `extract-known-issues` → `build-readme`, regenerating `README.md`, `README-auditor.md`, `FINDINGS.md`. Plus `bin/term` (LEXICON), `bin/align-slug`, `bin/lint-md`, `bin/lint-outline`, `bin/build-monograph`. Ruby internal / Python community-facing per convention. **Invoked manually** — nothing guarantees it runs.

4. **Cross-architecture agent diversity** — Opus / Gemini / Codex run as independent auditors and naming-voters (naming-vote files under `msc/naming/naming-votes/` show `opus-*`, `codex-*`, `gemini` passes; audit SOP credits independent Gemini/Codex passes). A real epistemic asset; entirely manual invocation.

5. **Naming-cycle tooling** — `bin/naming-master-*`, `bin/naming-r2-*`, `bin/naming-aggregate.rb` aggregate multi-agent voting rounds. Real, purpose-built, manual.

6. **context7 MCP** — the *only* wired MCP server (global `mcpServers` in `.claude.json`). Library-docs lookup; marginal relevance to a math-theory project.

---

## (b) Aspirational processes the docs/SOPs intend but that are not built

- **`bin/refresh-all --check` as a pre-commit / pre-push hook.** The code *names its own missing automation*: `bin/refresh-all` header comment reads *"Future: a pre-commit / pre-push hook can call `bin/refresh-all --check` and stage the regenerated files automatically if there's drift, so README never goes stale."* Never built. Consequence: generated files drift silently (see (d)).
- **`bin/lint-readme`** (TODO §J-15, "deferred") — slug-existence + cross-reference link validation. Named, not written.
- **SOP stubs** — `doc/sop/multi-agent.sop.md`, `git-hygiene.sop.md`, `build-pipeline.sop.md` are all marked *"being authored; thin for now"* in `agents.sop.md`. The manual processes (2) and (4) above are exactly what these would codify.
- **A process for latest theory-relevant news** (explicit on Joseph's brainstorm list). Grep for news/arxiv-monitoring across `msc/`, `doc/` returns nothing. Does not exist.

---

## (c) Emergent patterns from git history

- **Parallel-agent fan-out is a recurring, unnamed method** (commits in (a.2)) — a de-facto process the tracking files don't formalize; git is where it's visible.
- **Worktrees: tried once, not adopted.** `446b891` "Ignore claude code worktrees" is the only trace; `git worktree list` shows a single working tree (zero auxiliary worktrees now). Available primitive, effectively abandoned after one touch.
- **SOP-ification arc** — the recent move to `doc/sop/*.sop.md` (symlinked `CLAUDE.md`/`AGENTS.md`/`GEMINI.md`) is the project trying to *codify its manual meta-processes into orientation*. The audit SOP is the mature one; the automation-adjacent SOPs are stubs. The arc is toward written discipline, not toward mechanical enforcement.
- **1015 commits, 2026-03-09 → 2026-07-04**, single active branch `main`. Commit messages are unusually rich (as the brief flagged) and are themselves the de-facto changelog for methodology that never lands in a tracking file.

---

## (d) Stale / broken / abandoned — concretely

- **`.claude/settings.local.json` is a config graveyard.** 92 `permissions.allow` entries; **8 reference the dead `/src/act/` repo path** (repo renamed away from `act` on 2026-03-16), **27 are one-off `mtxrun`/ConTeXt/pdflatex experiment invocations** long superseded by the markdown-first monograph pipeline. It contains literal fragments of parsed bash loops (`"Bash(do echo \"=== $f ===\")"`, `"Bash(done)"`) — accreted, never curated. It is **gitignored** (whole `.claude/` dir is in `.gitignore`), so it is purely local cruft that cannot be shared or reviewed.
- **No git hooks.** `.git/hooks/` contains only `*.sample`. The one the code asks for (refresh-drift guard) is absent → README / FINDINGS / LEXICON can silently desync from source.
- **Global subagents are domain-mismatched dead weight.** `~/.claude/agents/` holds 8 subagent defs — `sub-agent-{architecture-reviewer, migration-assistant, new-feature, performance-optimizer, refactor, tech-debt-finder-fixer, test-generator}` — all **software-engineering** oriented. For a mathematical-theory corpus (segments, derivations, naming cycles) these are inapplicable; there are **no project-specific subagent definitions** (auditor, spike-miner, math-verifier) anywhere.
- **The `refresh-all` "Future: hook" comment** is itself stale-aspirational — written, never acted on.
- **No hooks configured at any level** — neither `~/.claude/settings.json` (no `hooks` key) nor the project local settings. So none of the "automated behavior on X" capability is in use.

---

## (e) Decisions genuinely blocked on Joseph

1. **Should `.claude/` be un-gitignored (at least `.claude/agents/` + a curated `settings.json`) so project automation can be version-controlled and shared across agent runtimes?** Right now the whole dir is ignored, which structurally forecloses *any* checked-in project subagent / hook / permission config. This is the gating decision under most of the adoptions below. One-line context: today no shared, reviewable harness automation is even *possible* for this repo.
2. **Build the `refresh-all` drift-guard hook (pre-commit or pre-push)?** Trade-off is commit-flow friction vs. silent generated-file drift; needs his tolerance call. Cheap to build once decided.
3. **Stand up project-specific subagent definitions** (de-novo-auditor, spike-miner, math-verifier) to replace the mismatched coding ones? Depends on (1).
4. **Formalize cross-architecture diversity (Gemini/Codex) via CLI invocation**, or keep it manual? A `claude`/`codex`/`gemini` headless-invocation seam would make the multi-agent audit reproducible; currently zero scripted invocation exists.
5. **Stand up a scheduled theory-news-monitoring agent** (the named want in (b))? Low-risk, but it is a standing-cost commitment that is his call.

---

## (f) Candidate meta-process definitions (raw material for a MECE hierarchy)

| Process | Trigger | Steps (current) | Health |
|---|---|---|---|
| **Agentic-Reading Audit** | "do a de-novo audit" | working-dir → 00-predictions → per-segment reflect (orient cascade) → 80%-gate → Phase-2 triangulate → ALL-CAPS FINAL | Method HEALTHY; **un-automated** (no dir-scaffolder, no template, no cadence enforcement — SOP pleads in prose) |
| **Parallel Multi-Agent Mining** | large survey (spikes, findings, votes) | fan-out N discovery agents → reconcile → land | DE-FACTO; ad-hoc orchestration, no reusable harness or SOP (`multi-agent.sop.md` is a stub) |
| **Generated-Artifact Refresh** | cycle-close | `bin/refresh-all` | Tool WORKS; **UNGUARDED** — no hook, silent drift risk |
| **Cross-Architecture Voting/Audit** | naming cycle / high-stakes verification | independent Opus/Gemini/Codex passes → aggregate | DE-FACTO; manual invocation, no scripted seam |
| **Config/Permission Hygiene** | (should be) periodic | — | BROKEN — 92-entry local graveyard, gitignored, uncurated |
| **Theory-News Monitoring** | (should be) scheduled | — | ABSENT / ASPIRATIONAL |
| **Decision Surfacing to Joseph** | session/cycle close | (currently: hand him scrollback) | ABSENT as a process — this is the bottleneck the whole review targets |

---

## Highest-leverage adoptions (ranked to THIS project's bottleneck, not a feature tour)

The bottleneck is bandwidth + decision-routing (Joseph blocked on calls he can't reconstruct). Rank by leverage on *that*, not by novelty.

1. **Decision-surfacing seam (HIGHEST).** A project skill (e.g. `/for-joseph`) or a `Stop`-hook that emits a structured artifact at cycle-close: *the ≤N decisions genuinely his, context reconstructed, recommendation, honest uncertainty* — replacing the scrollback dump. Directly attacks the decision-routing failure both orientation letters name. Precedent exists (`msc/for-joseph.md` per global memory). Skill is the clean vehicle; hook is the enforcing version.
2. **`refresh-all` drift-guard hook (HIGH, CHEAP).** Pre-commit/pre-push `bin/refresh-all --check`. The code already requests it; kills silent README/FINDINGS/LEXICON drift. Gated on decision (e2)/(e1).
3. **Audit-working-dir scaffolder (HIGH).** `bin/audit-init NNNNNN` (or a skill) that stamps the dir, the `00-initial-predictions.md` template, and a per-segment reflection-cadence checklist. Lowers activation energy for the 703-line ritual and *structurally* enforces the per-segment cadence the SOP keeps pleading for (the single most-repeated failure mode in §3–§4). Turns the crown-jewel method from prose-discipline into scaffolded-discipline.
4. **Project subagent definitions (MEDIUM-HIGH).** Replace the 8 coding subagents with de-novo-auditor / spike-miner / math-verifier defs codifying the manual fan-out (a.2). Gated on un-gitignoring `.claude/` (e1).
5. **Scheduled theory-news agent (MEDIUM).** Use the `schedule`/cron capability for a low-frequency arXiv/adjacent-work monitor (active inference, causal-RL, digital-minds macrostrategy à la Forethought). Named want; low-risk; reduces the "am I missing prior art" tax that recurs in naming/prior-art cycles.
6. **plan-mode / `ultrareview` for high-stakes landings (MEDIUM).** Currently absent from the workflow; the strengthen-before-soften culture and canon-modifying spikes are exactly where a plan/deep-review gate pays.

**Config hygiene (do-anyway, low-effort):** curate or reset `.claude/settings.local.json` — the 35 provably-dead `act`-era + ConTeXt entries can go regardless of the larger decisions.

---

## Out-of-scope surfacings (passing back)

- The **`.claude/` gitignore decision (e1)** is upstream of most project-level agent-experience improvements beyond this slice — it silently prevents *any* shared harness config (settings, hooks, subagents, MCP allowlists) from being version-controlled. Worth a deliberate call independent of tooling.
- **Commit messages are a shadow methodology-log.** Real emergent process (parallel mining counts, worktree trial, SOP arc) lives *only* in git, not in any tracking file. Whatever meta-process hierarchy this review produces should treat `git log` as a first-class source and consider a periodic "mine the commit log into CHANGELOG/methodology" pass.
- **The `bin/` toolchain is genuinely strong** (multi-agent-safe append-only `term`, idempotent `align-slug`, `refresh-all` orchestration) — the deficit is *harness-integration and enforcement*, not tool quality. Any recommendation should build on this, not around it.
- **Unlocated:** I could not find the "illustration-impact-judging attempt" named in the brief anywhere in `agentic-systems` or `ops`. If it exists it is in a session transcript or a repo I did not search; flagging so it can be relocated rather than assumed lost.
