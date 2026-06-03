# SOP shift — completion plan (2026-06-02)

The plan to finish the `doc/sop/` consolidation without stranding the repo in an intermediate state. Companion to the design/inventory doc [`sop-consolidation-design-2026-06-01.md`](sop-consolidation-design-2026-06-01.md); this is the executable end-state plan.

## Done

`doc/sop/` home + `sop-creation.sop.md` (the convention); interred `naming.sop` (methodology + principles, under its index), `spikes.sop`, and `format.sop` (FORMAT.md is now a symlink to it — zero inbound rewriting); `bin/check-links` (the link-integrity gate); `JOSEPH-TODO.md`; `bin/build-tex` sunset. Tree green throughout.

## Phase A — finish the mechanical interments (commodity work; a fast agent + `check-links`)

- **The audit pair** (codependent — move together): `doc/de-novo-audit-instructions.md` → `doc/sop/audit.sop/de-novo.sop.md`; `doc/audit-routing-instructions.md` → `doc/sop/audit.sop/routing.sop.md`; reshape `doc/sop/audit.sop.md` into the index. **Use the symlink trick** (leave `de-novo-audit-instructions.md` and `audit-routing-instructions.md` as symlinks to the new pieces): then *all* inbound refs — the ~300 in CLAUDE.md, segments, audits/, the README partials, even `spikes.sop`'s deferral — resolve through the symlinks untouched. The only edits are: (1) the two moved files' own outbound links (depth `doc/` → `doc/sop/audit.sop/` is **+2** `../`), and (2) the two cross-references between them become same-directory (`./de-novo.sop.md` / `./routing.sop.md`). `check-links` gates it.
- **`format.sop` branching** into `format.sop/` pieces is an optional later nicety, not required. Leave it whole.

That closes the file-shuffling. Everything below is the part that actually needed judgment.

## Phase B — the substantive consolidation (the value; do in this order)

**B1 — Author the two orphan SOPs** (currently memory-only; stubs in `doc/sop/`). This frees the most value and starts draining `MEMORY.md` (which is over its load limit).
- `multi-agent.sop.md` ← the project-memory carriers: `feedback_multi_agent_methods`, `_multi_agent_verification_cadence`, `_pilot_then_sweep_pattern`, `_cluster_work_reconciliation_pattern`, `_subagent_destructive_action_authorization`, `_subagent_questions_as_framing_diagnostic`, `_workflow_restatement_as_feedback_channel`. (Delegation *stance* — peer-voice — stays disposition; the SOP points to it.)
- `git-hygiene.sop.md` ← `feedback_commit_granularity_and_communicate`, `_commit_before_canon_modifying_spike`, `_hybrid_commit_cadence_for_parallel_sweeps`, plus lint-gates-the-commit and the bash-in-place-editor / backtick-args footguns.
- Then thin those memories to one-line pointers at the new SOPs.

**B2 — Single-source the drifted disciplines** (each is currently stated in 2–3 layers; pick one home, point the rest):
- **WN-discipline** → `FORMAT.md` §Working Notes (per `wn-discipline-coherence-pass-2026-05-31.md`, option B). *Gate: Joseph (A/B + scope) — in JOSEPH-TODO.*
- **strengthen-before-soften, integration-is-replacement, peer-voice, voice-discipline** are *disposition* → authoritative home is the global `~/.claude/memory/` files; `CLAUDE.md` keeps the before-action *trigger* + a pointer, not the restatement.
- **segment-voice-not-diff-voice, math-lives-in-segments, working-theory-in-canon** → `FORMAT.md` (segment mechanics); `CLAUDE.md` points.

**B3 — Slim `CLAUDE.md`** (the biggest project-wide lever; do it *after* B1/B2 so it points at settled homes). Target: roughly halve it, into a clean *disposition + index + triggers* file.
- **Keep (disposition / orientation / reflex-firing):** what-the-project-is and the naming lineage; the Key Architectural Decisions (GUC classes, directed separation, AND/OR DAG, sector-condition-primary); the epistemic conventions (claim tiers, equation tags); the math-in-files self-reminder; the strengthen-before-soften / integration-is-replacement / math-novelty / prior-art-integration *stances*; the reading-and-writing posture.
- **Demote to "see `doc/sop/X.sop.md`" + (where reflex-relevant) a before-action trigger:** the Working-Conventions *procedures* — audit-cycle handling, the Gate-2 mechanics, naming mechanics, the README/LEXICON/build auto-generation mechanics, the slug role-prefix table. These are step-by-step procedure, not disposition.
- **File Organization** → trim to the project map + a pointer to the SOP index; the per-SOP detail lives in the SOPs.
- The test for each line: *does it fire a reflex (keep) or do you follow it step-by-step (demote to the SOP)?*

**B4 — The `doc/sop/sop.md` master index** *(Joseph gate, in JOSEPH-TODO).* Lean: a thin `sop.md` (read-order + one-liner per SOP) that `CLAUDE.md`'s index points at, rather than duplicating the list in CLAUDE.md.

## Why this order

A (mechanical) is independent and can run anytime. Within B: author the orphans (B1) and single-source the drift (B2) first, because B3 (slimming CLAUDE.md) and B4 (the index) *point at* the homes B1/B2 establish — slim CLAUDE.md last, once there's a settled place for every pointer to land. That ordering is what prevents a half-slimmed CLAUDE.md pointing at SOPs that don't exist yet.
