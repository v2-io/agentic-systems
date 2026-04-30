# PRACTICA
*Current active areas of work with 🌟 (primary) and ⭐ (secondary) indicating most immediate priorities. In AAD terms, this is the top levels of the strategy DAG.*

*This file names the **areas** of active work. The systematic project workflow each area implies — audit cycles, segment refinement and promotion, citation checks, prior-art searches, the named workflow steps below — is mostly not enumerated piece-by-piece. For specific items that don't fit a more systematic home: [`TODO.md`](TODO.md) is the misc-and-details layer (open audit-finding routing decisions, queued spike follow-ups, deferred items, lower-priority specifics). For architectural moves under review: [`PROPOSALS.md`](PROPOSALS.md). Sister-files: [`README.md`](README.md) external-facing snapshot, [`CLAUDE.md`](CLAUDE.md) agent-onboarding, [`CHANGELOG.md`](CHANGELOG.md) historical record. PRACTICA itself is **auditor-safe** — readable during de-novo audits — but linked entries into TODO / PROPOSALS / CHANGELOG are priming-heavy and should be skipped until the initial stages of audits are complete.*

## ⭐Theory
- [ ] ⭐ [TODO](TODO.md)
- [ ] [PROPOSALS](PROPOSALS.md)
- [ ] Principle Theory, Structure, & Dependency Graphs (via feedback & audits)
  1. [AAD OUTLINE](01-aad-core/OUTLINE.md),  Segment Refinement & Promotion
  2. [TST OUTLINE](02-tst-core/OUTLINE.md), Segment Refinement & Promotion
  3. [LOGOGENIC OUTLINE](03-logogenic-agents/OUTLINE.md), Segment Refinement & Promotion
  4. [LOGOZOETIC OUTLINE](04-logozoetic-agents/OUTLINE.md), Segment Refinement & Promotion
- [ ] Empirical Experiments & Analysis
- [ ] Prior/Adjacent Art, Novelty Analysis, & Citations
- [ ] Pedagogy (initially needs vision & plan)
- [ ] Gaps, spikes, & ideation
- [ ] Paper/target-document authoring & generation

## 🌟 Findings

*(NOTE: **(soft-) blocked until "Current naming conventions refactor" below**)*

1. [ ] (Current FINDINGS + README + msc/FINDINGS-RANKED* & brainstorm) -> segments
2. [ ] segments <-> FINDINGS-OUTLINE (or normal outline with findings extraction; to decide)
3. [ ] FINDINGS-OUTLINE (or normal outline w/ findings extraction) -> FINDINGS (was -RANKED)
4. [ ] FINDINGS (was -RANKED) -> (README.md's summary)
5. [ ] Additional explanations & findings for remaining segments

## Ops

### Processes
1. [ ] Need a Theory Improvement process & rhythm now for the highest level cycle
    - [ ] Working notes scanning
    - [ ] De novo audits
    - [ ] "Full (stepwise) Comprehension" de novo audits
    - [ ] FORMAT, epistemology, and voice audit
    - [ ] TODO / PROPOSALS work
    - [ ] Spikes
    - [ ] Drafting & Outline modification & repair
    - [ ] Segment refinement and promotion advancement
    - [ ] CI/CD (below)

### CI/CD
- [ ] Revisit automatic segment -> outline normalizer (e.g., types, tags, status, etc.)
- [ ] Automatic dependency graph generation & outline linting
- [ ] FINDINGS regeneration (from above)
- [ ] IN-PROGRESS regeneration (from this file — PRACTICA — and potentially TODO, PROPOSALS, & working notes from segments)
- [ ] LEXICON regeneration (potentially, see below)
- [ ] TODO/CHANGELOG hygiene
- [ ] README regeneration
    - [ ] FINDINGS -> README summary
    - [ ] IN-PROGRESS -> README summary
    - [ ] LEXICON -> README summary

## Names & Lexicon
### 🌟 Current naming conventions refactor

Status (updated 2026-04-30 post-R2-cohort-close): pilot complete; full role-prefix sweep complete (142 segments under `{type-prefix}-{subject-noun}`); refined principles file landed (2026-04-24, `b9492b7`); rename-vs-add-alias and rename-vs-canonicalize semantics extended in principles file (2026-04-29). Architectural invariants now: role-prefix from frontmatter (mechanical via `bin/align-slug`); subject-noun preference; Greek-vocabulary commitment with open-semantic-space justification; separate-passes methodology. Phase-1 substantially complete; Phase-2 enrichment passes complete (Pass A/B/C); Pass D collision-check complete (2026-04-29, see [`msc/naming/collision-check-2026-04-29.md`](msc/naming/collision-check-2026-04-29.md)). **Phase-3 R2 voting cohort closed** across two cohort iterations: r2 (v1-prompt, archived to [`msc/naming/naming-votes/r2-early/`](msc/naming/naming-votes/r2-early/)), r2b (v2 methodology, no consolidation checkpoint), r2c (v2 methodology + consolidation checkpoint). Final cohort: gemini-r2 (190 voted / 466 can-vote / Pro→Flash with documented harness-side persistence failure), opus-r2b (54), sonnet-r2b (43), codex-r2b (58, post-sweep), opus-r2c (83), sonnet-r2c (74). Cohort-wide off-scale residual: 0 across r2c (the consolidation-checkpoint mechanism + principles-file fix held). The §12.3 mechanism produced ~70% coverage improvement (sonnet) and ~54% (opus) at maintained engagement quality compared to pre-fix r2b runs. Mid-cycle methodological findings captured in [`msc/naming/mini-lexicon-todo.md`](msc/naming/mini-lexicon-todo.md) §11–§12. Reference: [`msc/reflections/22-substrate-handoff-and-rationale-attribution.md`](msc/reflections/22-substrate-handoff-and-rationale-attribution.md), [`msc/reflections/23-harness-side-persistence-failure.md`](msc/reflections/23-harness-side-persistence-failure.md), [`msc/reflections/24-framework-as-its-own-diagnostic.md`](msc/reflections/24-framework-as-its-own-diagnostic.md). **Next: aggregator design and execution** — four design questions queued (substance-weighting, scale-clamping, consensus thresholds, output banding); detail in handoff. Then finalist landing decisions, rename surgery, lexicon-coherence pass.

1. [x] ~~Launch naming survey agents with initial instructions~~ (original Round 1 launched 2026-04-23; 10 vote files at `msc/naming/naming-votes/`)
2. [x] ~~Aggregation & Consolidation (initial/blind)~~ (`msc/naming/naming-aggregate-{review,round2,votes.json}`; `bin/naming-aggregate.rb`)
3. [x] ~~Launch refined Round 1 (cold-start)~~ — 5 r2 cold-start vote files + 4 reactive additions + 1 audit-derived extraction + 3 targeted-alternatives runs (Codex / Gemini / Opus + Opus-v2). Editorial passes: formula wrapping, consolidation of 17 high-confidence clusters, targeted-alts fold-in.
4. [x] ~~Aggregate refined Round 1~~ — running aggregation with canonical-form normalization, compound + acronym preservation, formula-block protection, category-suffix display. 4 output formats (review / round2 / compact / json).
5. [ ] **🌟 Round 2 (blind) using refined-Round-1 aggregation** — design and tooling in `msc/naming/round-2-plan.md`. Pre-launch tasks include: Tier-2 retrofit (R1 category retro-classification — last Phase-1 item), agent-passes A/B/C/D for master-list enrichment, manual master-list curation (split `class 1/2/3` trio etc.), `bin/naming-master-card` zero-leak voting-card generator, R2 launch prompt, voter-slate decision.
6. [ ] Collision audit on top finalists (web search for external collisions, à la ACT → AAD precedent) — now scoped as agent-pass D in the R2 plan.
7. [ ] Final decisions
8. [ ] Strategically execute renaming surgery, historical map, & audit (specific deferred renames listed in [`TODO.md`](TODO.md) §"Naming pipeline — specific deferred items")

### Lexicon
- [ ] Consider segment -> accumulator / alphabetize -> lexicon
- [ ] Update / Refresh Lexicon (manually or automated depending on earlier)

## Misc
- [x] ~~Review new README outline & partials available~~ — landed via 2026-04-26 doc-pipeline cycle (commits `653cfeb`, `6389e4d`, `b1c61a0`, `104b777`); pipeline at `doc/readme/`, scripts in `bin/` (`build-readme`, `extract-findings`, etc.)
- [ ] Joseph review new README outline & partials available
- [ ] Consider modifying & updating link formatting + policy, and tagging (better optimized for both obsidian, plain text, and github)
- [ ] Footnote and citation procedure
- [ ] Historical provenance and relic cleanup (e.g., unimportant TFT mentions even if effectively in footnotes)
- [ ] README v2 pass per Alan Walton's first-human review (queued; detail in [`TODO.md`](TODO.md))