# SOP shift — completion plan (2026-06-02)

The plan to finish the `doc/sop/` consolidation without stranding the repo in an intermediate state. Companion to the design/inventory doc [`sop-consolidation-design-2026-06-01.md`](sop-consolidation-design-2026-06-01.md); this is the executable end-state plan.

> [!note]
> **✓ WHOLE SHIFT COMPLETE 2026-06-02.** Phase A (audit pair) + Phase B (B1 orphan SOPs, B2 WN-discipline single-source, B3 agents.sop.md slim) all landed; durable narrative in `CHANGELOG.md` (2026-06-02). Retained as the reasoning trail (the symlink-vs-full-move pattern, the phase ordering). The only deliberately-deferred slice is the **global/memory-layer pass** (the global `~/.claude/CLAUDE.md` + `~/.claude/memory/` carriers inheriting the WN-narrowing), which is out of this project-scoped shift.

## Done

`doc/sop/` home + `sop-creation.sop.md` (the convention); interred `naming.sop` (methodology + principles, under its index), `spikes.sop`, and `format.sop` (FORMAT.md is now a symlink to it — zero inbound rewriting); `bin/check-links` (the link-integrity gate); `JOSEPH-TODO.md`; `bin/build-tex` sunset. Tree green throughout.

## Phase A — finish the mechanical interments ✓ DONE 2026-06-02

The audit pair is interred (`doc/sop/audit.sop/{de-novo,routing}.sop.md` + the `audit.sop.md` index; old paths symlinked; check-links green). The record below is kept as the worked pattern.

- **The audit pair** (codependent — move together): `doc/de-novo-audit-instructions.md` → `doc/sop/audit.sop/de-novo.sop.md`; `doc/audit-routing-instructions.md` → `doc/sop/audit.sop/routing.sop.md`; reshape `doc/sop/audit.sop.md` into the index. **Use the symlink trick** (leave `de-novo-audit-instructions.md` and `audit-routing-instructions.md` as symlinks to the new pieces): then *all* inbound refs — the ~300 in CLAUDE.md, segments, audits/, the README partials, even `spikes.sop`'s deferral — resolve through the symlinks untouched. The only edits are: (1) the two moved files' own outbound links (depth `doc/` → `doc/sop/audit.sop/` is **+2** `../`), and (2) the two cross-references between them become same-directory (`./de-novo.sop.md` / `./routing.sop.md`). `check-links` gates it.
- **`format.sop` branching** into `format.sop/` pieces is an optional later nicety, not required. Leave it whole.

- **Convention note — symlink vs full-move.** The heavily-referenced docs (FORMAT, the agents onboarding, this audit pair) are *symlink-aliased*: the real file lives in `doc/sop/`, the old path becomes a symlink to it, so inbound refs resolve untouched. The lighter docs (naming, spikes) were *fully moved* — old paths retired, the handful of live refs rewritten. Both are fine and `check-links` is symlink-aware; rule of thumb: symlink when inbound refs are many.

That closes the file-shuffling. Everything below is the part that actually needed judgment.

## Phase B — the substantive consolidation (the value; do in this order)

> **This phase needs a *thinking* agent, not the mechanical Phase-A treatment.** Single-sourcing the drift and slimming the body are judgment calls (use the disposition-vs-procedure test in [`../../doc/sop/sop-creation.sop.md`](../../doc/sop/sop-creation.sop.md)); a blind/fast agent can do Phase A but should not autopilot Phase B.

**B1 — Author the two orphan SOPs ✓ DONE 2026-06-02.** Both authored in peer register and committed: `doc/sop/multi-agent.sop.md` (the seven method carriers; points to peer-voice for the delegation register, which stays disposition) and `doc/sop/git-hygiene.sop.md` (commit granularity + state-the-plan-first, the pre-spike seam, lint-gates-the-commit, pathspec discipline, the two session footguns). check-links green.

**B1-residual — the memory thinning is a FLAGGED DECISION, not executed.** The plan said "thin those memories to one-line pointers," but the global `~/.claude/CLAUDE.md` documents these project `feedback_*.md` carriers as the *substrate the indices distill* and as an explicit *fallback layer* — so gutting them is a cross-project blast-radius move, not mechanical cleanup. Options for Joseph: **(a)** gut bodies to SOP-pointers (the global fallback chain would re-point at the SOPs); **(b)** retain bodies as substrate, add an "authoritative → SOP" banner atop each + tighten their `MEMORY.md` index lines (lossless, reversible; recommended); **(c)** leave entirely, just tighten `MEMORY.md` index lines for budget. The actual `MEMORY.md` budget lever is the *index line lengths*, not the body sizes (bodies load on-demand, not into the auto-load budget) — so (b)/(c) still deliver the budget win. → flagged in `JOSEPH-TODO.md`.

**B2 — Single-source the drifted disciplines** (each is currently stated in 2–3 layers; pick one home, point the rest):
- **WN-discipline** → `format.sop.md` §Working Notes (the single home). *No fork:* the older `wn-discipline-coherence-pass-2026-05-31.md` "A/B" framing predates `doc/sop/` — single-sourcing *is* this cycle's premise, not a decision. The global `~/.claude/` copy is a separate later pass, outside this shift.
- **strengthen-before-soften, integration-is-replacement, peer-voice, voice-discipline** are *disposition* → authoritative home is the global `~/.claude/memory/` files; `CLAUDE.md` keeps the before-action *trigger* + a pointer, not the restatement.
- **segment-voice-not-diff-voice, math-lives-in-segments, working-theory-in-canon** → `FORMAT.md` (segment mechanics); `CLAUDE.md` points.

**B3 — Slim `agents.sop.md`'s body** (`CLAUDE.md` / `AGENTS.md` / `GEMINI.md` now symlink to it; the orientation header + SOP index are authored — `4d5b1be`). Remaining, after B1/B2 settle the homes: demote the body's procedure *restatements* to pointers. Target: roughly halve the body into a clean *disposition + index + triggers* file.
- **Keep (disposition / orientation / reflex-firing):** what-the-project-is and the naming lineage; the Key Architectural Decisions (GUC classes, directed separation, AND/OR DAG, sector-condition-primary); the epistemic conventions (claim tiers, equation tags); the math-in-files self-reminder; the strengthen-before-soften / integration-is-replacement / math-novelty / prior-art-integration *stances*; the reading-and-writing posture.
- **Demote to "see `doc/sop/X.sop.md`" + (where reflex-relevant) a before-action trigger:** the Working-Conventions *procedures* — audit-cycle handling, the Gate-2 mechanics, naming mechanics, the README/LEXICON/build auto-generation mechanics, the slug role-prefix table. These are step-by-step procedure, not disposition.
- **File Organization** → trim to the project map + a pointer to the SOP index; the per-SOP detail lives in the SOPs.
- The test for each line: *does it fire a reflex (keep) or do you follow it step-by-step (demote to the SOP)?*

**B4 — DONE (2026-06-02, `4d5b1be`): the master index is `doc/sop/agents.sop.md`** — the agent-orientation home (reading-order by role + the SOP index), with `CLAUDE.md` / `AGENTS.md` / `GEMINI.md` symlinked to it. The `sop.md` question is resolved.

## Why this order

A (mechanical) is independent and can run anytime. Within B: author the orphans (B1) and single-source the drift (B2) first, because B3 (slimming CLAUDE.md) and B4 (the index) *point at* the homes B1/B2 establish — slim CLAUDE.md last, once there's a settled place for every pointer to land. That ordering is what prevents a half-slimmed CLAUDE.md pointing at SOPs that don't exist yet.
