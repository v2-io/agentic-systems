# SOP consolidation — inventory synthesis + `doc/SOP/` design proposal (2026-06-01)

> [!warning]
> **Superseded for planning (2026-06-02) — do NOT execute from this file.** The shift is well underway: five SOPs are interred (naming ×2, spikes, format, the agents orientation/index), `bin/check-links` is the gate, and the root runtime files symlink to `doc/sop/agents.sop.md`. Several leans below are overtaken by what landed — FORMAT/agents are **symlink-aliased, not branched**; the master index **is `doc/sop/agents.sop.md`**, not a deferred `sop.md`. The **live plan** is [`sop-shift-completion-plan-2026-06-02.md`](sop-shift-completion-plan-2026-06-02.md); **live state** is `NEXT-UP.md`; **Joseph-decisions** are `JOSEPH-TODO.md`. Read *this* file only for the original six-cluster inventory + rationale.
>
> *(Original header: a proposal/decision-support doc — the synthesized inventory, proposed architecture, migration map, and reserved decisions; the repo-wide generalization of [`wn-discipline-coherence-pass-2026-05-31.md`](wn-discipline-coherence-pass-2026-05-31.md).)*

## Ratified gate decisions (2026-06-01)

Joseph's gate on §5, plus the home conventions he set — these supersede the leans recorded below where they differ (most notably: FORMAT does **not** stay at root; it is interred here and branches):

1. **Scope: project-layer first.** The global `~/.claude/` layer is also overloaded and carries ASF-specific material to mine, but that is a successor pass on its own seam — recorded in `doc/sop/sop-creation.sop.md` §"Near-future work to mine" so it is not lost.
2. **The big manuals + FORMAT are interred under `doc/sop/` and branch** (relocate — §5 option a). Relocation is staged future work (it touches many cross-references); the topic stubs are touched now.
3. **The `.sop` file convention** (set by Joseph): a leaf topic is `doc/sop/<topic>.sop.md`; a branching topic's `<topic>.sop.md` becomes an index whose pieces live in `doc/sop/<topic>.sop/<piece>.sop.md` (recursively, for organic growth). *"See the X sop"* resolves to `doc/sop/X.sop.md` first, then into `X.sop/` if it is an index. Master index `doc/sop/sop.md` is **deferred** (pending the CLAUDE.md-redundancy question, §5.3 / decision #3 — gather and order first, build the entrypoint later). Full statement: `doc/sop/sop-creation.sop.md`.
4. **`NOTATION.md` and `terminology/README.md` are *not* interred for now** — they stay as reference / subdirectory-governance and get indexed from the SOP home. Revisit only if "etc." is meant to include them.
5. **First file written:** `doc/sop/sop-creation.sop.md` (the meta-SOP every other SOP inherits). Topic stubs touched as honest one-block placeholders (status + current home + planned scope), not empty files.

## 0. The charter — what we are sorting, and by what cut

The repo's "how an agent works here" rules are scattered across the auto-loaded layer (`CLAUDE.md` project + global, the memory files), the segment-convention docs (`FORMAT.md`, `NOTATION.md`), the process docs (`doc/*`), the subdirectory READMEs (`spikes/`, `audits/`, `terminology/`), and a few working docs (`msc/`) and navigators. The goal is a single coherent, authoritative home for each *process* discipline under `doc/SOP/`, with the auto-loaded layer demoted from *restating* the rules to *pointing* at them.

**The load-bearing cut is disposition vs. procedure.**

- **Disposition** — *how to BE.* The truth-honoring stance; the failure-mode body-signals (the *"therefore"* trigger, the urge to write *"this is not a weakening"*, hedge-clauses forming before the honest math); the peer-voice stance; the strengthen-before-soften reflex; integration-is-replacement; the collaboration posture with Joseph. This is texture, not checklist, and it is deliberately auto-loaded so it is *present* at the load-bearing moment. **Disposition does not move to `doc/SOP/`.** It stays in `CLAUDE.md` + memory, because a procedure file you have to remember to open cannot fire a reflex.
- **Procedure** — *how to DO a repeatable thing.* The audit walk and its gates; spike disposition/routing; the naming cycle; segment promotion mechanics; the build/auto-generation pipeline; the multi-agent methods; commit hygiene; the terminology-system CLI. These have steps, enums, decision trees. **Procedure is what `doc/SOP/` is for** — stated once, authoritatively, on-demand.

**The architectural mirror.** This is exactly the relationship the *global* layer already uses and that works: `~/.claude/CLAUDE.md` is the auto-loaded index + disposition + before-action triggers; `~/.claude/memory/<cluster>/` holds the on-demand detail. The project gets the same two-layer shape: `CLAUDE.md` (auto-loaded: disposition + index + before-action triggers) ↔ `doc/SOP/` (on-demand: authoritative procedure). A before-action trigger is the seam — *"before softening an audit finding, read `doc/SOP/...`"* — disposition in the auto-loaded layer, procedure in the SOP.

**The discipline that governs the consolidation itself: defer-don't-fork.** State each rule once, in its home; everywhere else references it. The corpus already does this well in one place (`doc/sop/spikes.sop.md` is deliberately thin and defers its shared core to `doc/audit-routing-instructions.md`). The whole effort is generalizing that one good instinct across the corpus and reversing the places it forked.

## 1. The finding — the core is already consolidated; scatter lives in three specific places

The reassuring result: **the hard-won procedural core is not forked.** Strengthen-first, the no-go protocol, ghost-forms, the meta-stance, the independent-verify gate all live once in `doc/audit-routing-instructions.md`, and `spikes.sop.md` defers to it explicitly. Segment mechanics live once in `FORMAT.md`. The terminology system lives once in `terminology/README.md`. The auto-generation disciplines (README/LEXICON/FINDINGS) each have one tool + one source-of-truth. `CLAUDE.md` mostly *points* at these rather than restating them. This is not a contradiction-cleanup; it is an organization-and-gap-filling pass on a corpus whose core is sound.

Scatter actually concentrates in three places:

1. **Sole-carrier disciplines stranded in auto-loaded memory with no in-repo home.** A whole cluster of *ratified* multi-agent-method and git-hygiene disciplines exists only as project-memory `feedback_*.md` files — invisible to anyone reading the repo, and contributing to the MEMORY.md over-limit problem (§6). These are the clearest gap: they are procedure, they are settled, and they have no `doc/` home. (Names in §3 / §4.)

2. **The auto-loaded layer restating procedure it should only point at.** `CLAUDE.md` (project) carries full procedural statements of things that have, or should have, an authoritative on-demand home: the slug role-prefix mapping table, the README/LEXICON build mechanics, Gate-2 mechanics, the audit-cycle three-document layout. These are migration-to-pointer candidates. (Distinct from the *disposition* in `CLAUDE.md`, which stays.)

3. **Duplicated disciplines across CLAUDE.md + project-memory + global-memory.** strengthen-before-soften, integration-is-replacement, segment-voice-not-diff-voice, peer-voice, working-theory-belongs-in-canon, math-lives-in-segments each appear in two or three of those layers. These want one authoritative carrier (disposition: the global memory file; procedure-slice: the SOP) with the others thinned to pointers.

Plus a handful of **settled disciplines stranded in transient working files** (the WN-discipline in `msc/wn-discipline-coherence-pass-*` + the `INTEGRATION-CLEANUP-TODO.md` carrying-note; the audit-gold two-track currently shaped in `NEXT-UP.md`), which should land in a durable home as they are gated.

## 2. The topic taxonomy

The six inventories converged on the same clusters. These become the `doc/SOP/` file set (one file per discipline-cluster — the granularity the sibling repos validate, neither monolith nor over-fragmented):

| Cluster | Procedure or disposition? | Current authoritative home(s) | Proposed home |
|---|---|---|---|
| Audit (de-novo walk + finding routing) | procedure | `doc/de-novo-audit-instructions.md`, `doc/audit-routing-instructions.md` | `doc/SOP/audit.md` (+ the two manuals relocated as its detail — see §3) |
| Spike disposition / routing | procedure | `doc/sop/spikes.sop.md`, `spikes/README.md` | `doc/SOP/spikes.md` (thin; defers to audit) |
| Naming cycle + principles | procedure | `doc/sop/naming.sop/principles.sop.md`, `doc/sop/naming.sop/methodology.sop.md` | `doc/SOP/naming.md` (+ the citability / lexicon-coherence memories folded in) |
| Segment promotion + gates + format | procedure | `FORMAT.md` | **stays `FORMAT.md`**, cross-linked from SOP (not duplicated) |
| Terminology system (`bin/term`) | procedure | `terminology/README.md` | **stays** `terminology/README.md`, indexed from SOP |
| Build / auto-generation pipeline | procedure | `msc/markdown-first-pipeline.md` + tool headers + `FORMAT-TODO.md` | `doc/SOP/build-pipeline.md` (consolidates the auto-gen + monograph disciplines) |
| Multi-agent methods | procedure (sole-carrier memories) | project-memory only | **`doc/SOP/multi-agent.md` (NEW)** |
| Commit / git hygiene | procedure (sole-carrier memories) | project-memory only | **`doc/SOP/git-hygiene.md` (NEW)** |
| Working-Notes discipline | procedure-slice of integration-is-replacement | `msc/wn-...` proposal + `FORMAT.md` §Working Notes | single-source in `FORMAT.md` (per the WN-coherence pass), referenced from SOP |
| Math / notation discipline | procedure-slice + disposition | `FORMAT.md`, `NOTATION.md`, CLAUDE.md self-reminder | **stays** (the visceral self-reminder is disposition → CLAUDE.md; the mechanical rules → `FORMAT.md`) |
| Voice / epistemic discipline | **disposition** | `CLAUDE.md` + global memory | **stays auto-loaded** (the procedural Gate-2 slice → `doc/SOP/audit.md`) |
| Truth-honoring, failure-mode body-signals, collaboration posture | **disposition** | global `CLAUDE.md` + memory | **stays auto-loaded** (untouched) |

## 3. Proposed `doc/SOP/` architecture

```
doc/SOP/
  README.md          index + read-order + workflow entry-points + the disposition-vs-procedure charter (§0).
                     This is the navigation anchor every sibling repo validates. Lists each SOP with a
                     one-line purpose and "read when"; links the auto-loaded triggers to their procedures;
                     points back to FORMAT.md / NOTATION.md / terminology/README.md as adjacent homes.

  audit.md           the audit SOP. Open question for the gate (§5): does it ABSORB the two big manuals
                     (de-novo-audit-instructions.md ~106KB, audit-routing-instructions.md ~40KB) by
                     relocating them here as doc/SOP/audit-de-novo.md / audit-routing.md, or stay a short
                     orientation that points to them where they sit? Either way: one authoritative core,
                     no fork. Folds in the gem-hints / gold-lift / architectural-proposals-first-class /
                     gate-2-probes-discussion / independent-verify disciplines (the first two currently
                     sole-carried in memory; the latter two restated in CLAUDE.md).

  spikes.md          thin, like today's spikes.sop.md — defers shared core to audit.md, carries the
                     spike-specific delta (the five-state disposition, .integrated vs .archived, the
                     archivability test, the canon-cites-only-canon binary, sim/empirical-as-spike-class).
                     Likely just a relocation+rename of doc/sop/spikes.sop.md.

  naming.md          relocation of doc/sop/naming.sop/principles.sop.md + doc/sop/naming.sop/methodology.sop.md, with the
                     sole-carrier memories folded in: citability (Crit-9) four-resolution paths,
                     lexicon-coherence dimensions, voting-round load/scale-drift lessons.

  multi-agent.md     NEW HOME for the stranded methods: delegation (peer-voice stays disposition; this
                     points to it), consolidation-audit pattern, multi-agent voting pattern, the
                     sonnet-modifies/opus-verifies verification cadence, pilot-then-sweep, cluster-work
                     reconciliation, subagent-destructive-action (constrain-by-tool-set), subagent-
                     questions-as-framing-diagnostic + the two-shot pattern, workflow-restatement gate,
                     convergence-as-coherence-evidence.

  git-hygiene.md     NEW HOME: commit granularity + state-the-batching-plan-first; pre-spike commit (the
                     seam); hybrid commit cadence for parallel sweeps (agents edit tree, parent commits
                     per batch); lint-gates-the-commit; pathspec discipline; the bash-sed-i-noop and
                     backtick-args footguns.

  build-pipeline.md  the auto-generation + monograph disciplines in one procedural home: README /
                     README-auditor / LEXICON / FINDINGS / recent-progress / known-issues are
                     auto-generated (edit source, never output); bin/refresh-all orchestration; the
                     three-stage markdown-first monograph pipeline + chunk-format contract (anchored to
                     msc/markdown-first-pipeline.md as the design record); the Ruby-internal /
                     Python-community script-language convention.
```

**What deliberately does NOT move:** `FORMAT.md`, `NOTATION.md`, `terminology/README.md` stay where they are (heavily cross-referenced, correctly single-sourced) and are *indexed* from `doc/SOP/README.md`, not duplicated into it. The disposition layer of `CLAUDE.md` (both project and global) stays. The big audit manuals' *content* stays authoritative wherever the gate decides they live — we are not rewriting them, only deciding their address.

## 4. Migration map by source

- **`CLAUDE.md` (project).** *Keep (disposition):* strengthen-before-soften, integration-is-replacement, working-theory-belongs-in-canon, math-novelty-recognition, prior-art-integration stance, the math-notation self-reminder, the reading/writing posture, the AAT architectural-decisions orientation. *Demote to pointer (procedure):* slug role-prefix mapping table → `doc/SOP/` (or keep as `bin/align-slug` is the source of truth + a pointer); README/LEXICON build mechanics → `doc/SOP/build-pipeline.md`; Gate-2 mechanics → `doc/SOP/audit.md` (keep the *why* as disposition); audit-cycle three-document layout → `doc/SOP/audit.md`. Net effect: `CLAUDE.md` gets shorter and more clearly disposition-plus-index, which also de-risks the "unreviewed amplifier" concern (`INTEGRATION-CLEANUP-TODO.md` §F6) by shrinking the procedural surface that drifts unwatched.
- **`CLAUDE.md` (global) + global memory.** *Decision §5(scope).* If in-scope: the before-action prescriptions stay (they are disposition + triggers), but project-specific procedure triggers point into `doc/SOP/`. **Verify against the live `~/.claude/memory/` first-hand** — the inventory surveyed a `~/src/memorata/` copy; the live layer's authored-vs-index-only state must be checked before any edit.
- **`FORMAT.md` / `NOTATION.md`.** Stay. Single-source the WN-discipline here (the WN-coherence pass's option B). Cross-link from `doc/SOP/README.md`.
- **`doc/*`.** The process docs relocate/rename under `doc/SOP/` per §3 (or stay and get indexed — gate decision §5). `spikes.sop.md`'s defer-to-audit pattern is the template.
- **READMEs (`spikes/`, `audits/`, `terminology/`).** Stay as *subdirectory governance* (they document their own corpus and are correctly single-sourced). Indexed from `doc/SOP/README.md`; trim any restatement of a rule whose home is now an SOP, leaving a pointer.
- **Project memory.** *Extract* the sole-carrier procedure memories to their `doc/SOP/` homes (multi-agent.md, git-hygiene.md, audit.md), leaving each memory thinned to a one-line pointer + the Joseph-quote/why (the disposition slice memory is good at). *Thin* the duplicate memories to pointers. *Keep* the pure-disposition and project-context memories untouched. This is also the lever that gets MEMORY.md back under its limit (§6).
- **`msc/` + navigators.** The WN-coherence-pass doc archives to `.archive/` once its rule lands in FORMAT. The audit-gold two-track's settled shape moves from `NEXT-UP.md` into `doc/SOP/audit.md` as it is gated. `markdown-first-pipeline.md` stays as the design record, anchored from `doc/SOP/build-pipeline.md`.

## 5. Reserved decisions (Joseph's gate)

1. **Scope.** Project-only, or also consolidate/point the global `~/.claude/` layer (cross-project; live path `~/.claude/memory/`)? Lead lean: **start project-only**, leave a clean seam for a later global pass, because the global layer is cross-project and higher-blast-radius and the project pass will teach us the right shape first.
2. **The two big audit manuals.** (a) **Relocate** them under `doc/SOP/` so the whole process tree is in one place (lead lean — cleanest "authoritative spot", and `doc/SOP/README.md` makes them findable); (b) **leave at `doc/`** and have `doc/SOP/` index/point to them; (c) **distill-and-link** (short SOP + manual) — *not* recommended, it re-creates the fork we are removing.
3. **Disposition line — confirm.** The visceral disposition/body-signal material stays auto-loaded and only *procedure* migrates. (Stated as the charter; flagging because it reshapes what you read every session.)
4. **Granularity — confirm.** One file per discipline-cluster (the §3 set), with a `doc/SOP/README.md` index. (All sibling repos validate this; not really a fork, but it is the structural commitment.)

## 6. The MEMORY.md tie-in (folds into this work, not a separate pass)

Project `MEMORY.md` is over its load limit (~33–36 KB vs. 24.4 KB) and truncating, so some indexed memories silently do not load. This consolidation is the natural fix: extracting the sole-carrier procedure memories into `doc/SOP/` and thinning the duplicates to pointers removes exactly the bulk that pushed it over. Sequence: migrate a memory's procedural content to its SOP home → thin the memory to pointer+why → prune its index line to one tight entry. Do the MEMORY.md index curation in the *same* batches as the extraction, not as a deferred pass. (The new `delegate-weeds-lead-stays-at-synthesis` entry gets indexed in that pass.)

## 7. Execution discipline (when gated)

- **Staged, one topic-cluster per batch**, committed per batch with the batching plan stated first (per `feedback_commit_granularity_and_communicate`). The order that front-loads value and de-risks: (1) the two NEW homes (multi-agent.md, git-hygiene.md) — pure gain, no fork to untangle, and they drain the worst MEMORY.md bloat; (2) the `doc/SOP/README.md` index + charter; (3) relocate the existing process docs per the §5(2) decision; (4) demote the CLAUDE.md restatements to pointers; (5) thin the duplicate memories.
- **Verify each migration first-hand** against the primary source before moving — the inventory is peer-reported hints, not truth.
- **Reduce, don't repoint:** when content moves, the old site is deleted and replaced with a pointer, never left as a softened duplicate (integration-is-replacement, at the doc level).
- **Lint every `.md` before claiming clean** (`bin/lint-md`), and eyeball for Unicode-in-backticks (lint skips code spans).
- **Peer-delegate the per-file drafting**, lead gates each against the disposition-vs-procedure cut and the defer-don't-fork test, lead does the git.

## 8. Provenance + corrections

Synthesized 2026-06-01 from six read-only inventory peers (process-docs+FORMAT+NOTATION; READMEs+governance; CLAUDE.md project+global; memories; msc/+navigators; sibling-repo organizational survey) + lead synthesis. **Correction carried forward:** the memory-cluster peer surveyed a `~/src/memorata/...` copy of the global memory, not the live `~/.claude/memory/` that the global `CLAUDE.md` indexes — global-layer specifics are flagged for first-hand re-check (§4, §5(1)). Sibling survey's transferable patterns (neurips `AGENTS.md`/`AUTHORING.md` disposition-vs-pragma split; the navigation-README; the "distilled SOP links to reference manual"; explicit read-order) directly informed §0 and §3.
