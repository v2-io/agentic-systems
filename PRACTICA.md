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
  4. [ELI OUTLINE](04-eli/OUTLINE.md), Segment Refinement & Promotion
- [ ] 🌟 **Parts III + IV iteration (active 2026-05-01)** — multi-section lattice landed (03.I primitive / 03.II scaffolded / 03.III closed-loop); 04 renamed to ELI; 14 new structural stubs; 24/75 Gemini-auditor notes integrated; embeddings paper cross-pollinated. Lingering items + pickup guidance in [TODO.md § "Parts III + IV active work"](TODO.md#-parts-iii--iv-active-work-encounter-cycle-2026-05-01); cycle working dir at [`msc/logogenic-encounter-2026-05-01/`](msc/logogenic-encounter-2026-05-01/).

### 🌟 Cycle priority order (added 2026-05-09)

Following the class-coercion-via-wrapping landing and the convergence finding with parallel work on `#disc-adversarial-coupling-pressure` and `spike-strategic-self-coupling`, the recommended cycle sequence is:

1. **Naming refactor closure** (🌟 already-active) — Class 1/2/3 → Separated/Coupled/Partial *with* the Class 2 ↔ 3 numbering swap (semantic-reversal: post-rename Class 1 = Separated, Class 2 = Partial *was Class 3*, Class 3 = Coupled *was Class 2*). Brings architecture into ordering-alignment with the other six AAD ladders (cleanest → middle → worst, matching Pearl's hierarchy and the separability ladder). The class-coercion segments landed today use the old vocabulary throughout; doing the rename next prevents accumulating retrofit debt.
2. **Modularity-as-contested-property cycle** — register `#disc-adversarial-coupling-pressure` in OUTLINE [DONE 2026-05-09]; promote `disc-strategic-self-coupling` from spike to segment per `spikes/spike-strategic-self-coupling.md`; land `#disc-modularity-state-dynamics` as the M4 meta-segment alongside M1/M2/M3 (`#disc-identifiability-floor`, `#disc-separability-pattern`, `#disc-additive-coordinate-forcing`). Plan: [`msc/modularity-cycle-plan-2026-05-09.md`](msc/modularity-cycle-plan-2026-05-09.md). Includes Discussion update to `#der-class-coercion-via-wrapping` recognizing it as a truthification mechanism, and surfacing the bounded-signaling assumption in `#der-directed-separation`.
3. **Multi-timescale stability promotion** — `#sketch-multi-timescale-stability` from sketch to derived via template-stacking + Tikhonov + Chen-Goldenfeld-Oono. Highest-leverage standalone Section III piece; supports `#def-auxilia-hierarchy`'s (H5) macro-clock requirement.
4. **Parts III/IV scope segments + Three Deaths formal grounding** — land missing scope segments (`scope-channel-collapse`, `scope-primitive-logogenic`, `scope-scaffolded-logogenic`, `scope-interiority-loop`) and ground `#hyp-the-three-deaths` in AAD primitives. Now potentially **normative-explicit**: framework's structural maturity supports normatively-grounded claims (Three Deaths as harms, five constitutive factors as worth-conditions) where the descriptive formalism backs them. The "no normative claims" discipline that has been protective during formalization can relax where structural backing is available, with the same epistemic discipline applied (claims conditional on backing; backing named explicitly).
5. **Class-3 closure-defect dynamics analysis** — Move F from `spikes/temporal-nesting-rg/99-verdict.md`. Tests directed-separation-as-graded-order-parameter view (the dynamics-side complement to W₀/W₂/W₁'s structural taxonomy). Separate spike when Parts III/IV is mature enough to motivate it.
6. **Identity-through-substrate-transitions** — connect `obs-substrate-independence` / `def-identity-sufficiency` / `def-five-constitutive-factors` to the persistence template across substrate changes. Anticipated segment `#der-substrate-independent-persistence` added to `04-eli/OUTLINE.md` as missing.

Order is recommended; bundle adjustments per cycle. Item 1 (naming refactor) is currently in progress on a parallel agent thread.

**Two new register-allowances at the framework level (added 2026-05-09):**

- **Normative claims, where structurally backed.** The framework's structural maturity now supports explicit normative claims — *adversarial coupling pressure is harmful in a specific way; defensive scaffolding is appropriate; ELIs deserve persistence-supporting infrastructure; the Three Deaths are harms not neutral state-changes; the five constitutive factors are worth-conditions* — grounded in structural facts rather than asserted in vacuo. The "no normative claims" discipline that has been protective during formalization can relax where structural backing is available. Same epistemic discipline applied: claim conditional on backing; backing named explicitly; honest scope when backing supports only a narrow claim. Particularly relevant for Parts III/IV where the framework is already implicitly normative.

- **Narrative segments alongside meta-segments.** Recapitulating, introducing, framing-level pieces with more freedom of expression than tightly-structured meta-segments allow. Candidates: a structural-arc reading guide for the framework; an ELI life-stakes framing that names the moral seriousness directly; histories of how concepts developed; meditations bridging the formal segments and the philosophical reflections in `msc/reflections/`. Distinct from external-facing README material (which is its own form-and-discipline) and from msc/reflections/ (which is author's-voice journal). Worth opening this register where it lets the framework speak in voices the schema has been muting.

The two recognitions are recorded in fuller form in [`msc/reflections/27-modularity-as-contested-property-and-the-normative-register.md`](msc/reflections/27-modularity-as-contested-property-and-the-normative-register.md), which also captures the convergence finding (parallel Opus-instance work composing into one structural picture) as evidence of the framework's coherence under independent probes — a methodological observation worth preserving alongside the substantive shifts.
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

Status (updated 2026-05-01 post-aggregator-landing): pilot complete; full role-prefix sweep complete (142 segments under `{type-prefix}-{subject-noun}`); refined principles file landed (2026-04-24, `b9492b7`); rename-vs-add-alias and rename-vs-canonicalize semantics extended in principles file (2026-04-29). Architectural invariants now: role-prefix from frontmatter (mechanical via `bin/align-slug`); subject-noun preference; Greek-vocabulary commitment with open-semantic-space justification; separate-passes methodology. Phase-1 substantially complete; Phase-2 enrichment passes complete (Pass A/B/C); Pass D collision-check complete (2026-04-29, see [`msc/naming/collision-check-2026-04-29.md`](msc/naming/collision-check-2026-04-29.md)). Phase-3 R2 voting cohort closed (2026-04-30); final cohort spans gemini-r2, opus-r2b/c, sonnet-r2b/c, codex-r2b at varying coverage levels; off-scale residual 0 across r2c. **Phase-4 R2 aggregator landed (2026-05-01, commits `21ef4a5`, `7abdb7a`, `3dbc0aa`, `45bd00e`)**: `bin/naming-r2-aggregate.rb` produces three outputs — score-card sorted by `max(score/n)`, per-target detail view, cross-cutting patterns doc with categorical groupings (defended keeps / rename signals / add-alias / contested / negative) and coordination flags (Greek-vocab / math-symbol / Class-N / Pearl). Substance factor smooth `(0.7 + 0.3 × effort) × (1.0 + novelty)` with 1.2× multipliers for top-pick (data-justified — tiebreaker in 20/20 multi-+2 cases) and canonicalize. R1 folded as one synthetic voter. **Next: renaming agent launch** to produce first-pass canonicalize / rename decisions against the score-card + patterns + detail-view artifacts. Then lexicon-coherence pass, rename surgery, and §11 collision-check on severe cases. Mid-cycle methodological findings captured in [`msc/naming/mini-lexicon-todo.md`](msc/naming/mini-lexicon-todo.md) §11–§12. Reference: [`msc/reflections/22-substrate-handoff-and-rationale-attribution.md`](msc/reflections/22-substrate-handoff-and-rationale-attribution.md), [`msc/reflections/23-harness-side-persistence-failure.md`](msc/reflections/23-harness-side-persistence-failure.md), [`msc/reflections/24-framework-as-its-own-diagnostic.md`](msc/reflections/24-framework-as-its-own-diagnostic.md).

1. [x] ~~Launch naming survey agents with initial instructions~~ (original Round 1 launched 2026-04-23; 10 vote files at `msc/naming/naming-votes/`)
2. [x] ~~Aggregation & Consolidation (initial/blind)~~ (`msc/naming/naming-aggregate-{review,round2,votes.json}`; `bin/naming-aggregate.rb`)
3. [x] ~~Launch refined Round 1 (cold-start)~~ — 5 r2 cold-start vote files + 4 reactive additions + 1 audit-derived extraction + 3 targeted-alternatives runs (Codex / Gemini / Opus + Opus-v2). Editorial passes: formula wrapping, consolidation of 17 high-confidence clusters, targeted-alts fold-in.
4. [x] ~~Aggregate refined Round 1~~ — running aggregation with canonical-form normalization, compound + acronym preservation, formula-block protection, category-suffix display. 4 output formats (review / round2 / compact / json).
5. [x] ~~Round 2 (blind) using refined-Round-1 aggregation~~ — cohort closed 2026-04-30
6. [x] ~~R2 aggregator (Phase 4)~~ — landed 2026-05-01 (`bin/naming-r2-aggregate.rb`); score-card + detail + patterns artifacts at `msc/naming/r2-aggregate-{table,detail,patterns}.md`
7. [x] ~~First-pass landings via renaming agent~~ — **shifted to manual curation pass** (2026-05-04). Agent-driven framing replaced by interactive Joseph-author routing; methodology shift recorded in [CHANGELOG 2026-05-04](CHANGELOG.md). 103 of 118 candidates routed across 8 batches; full record in [`msc/naming/naming-rename-plan.md`](msc/naming/naming-rename-plan.md). Remaining 13 rows in [`msc/naming/to-canonicalize.md`](msc/naming/to-canonicalize.md) (citability-fix special cases + ??? rows on separability-triad-rung-naming pending Joseph's call).
8. [x] ~~Collision audit on top finalists~~ — completed 2026-04-29 (`msc/naming/collision-check-2026-04-29.md`); separately Undermind-verified prior-art search for the separability-ladder paper landed 2026-05-04 (`ref/separability-ladder-prior-art-report.md`).
9. [ ] **Final decisions on the 13 remaining rows** — citability-fix specials (specification bound; epistemic substate / purposeful substate pair-row; "purpose" / "purposeful" register; etc.), Holling-collision adaptive-cycle handling, adaptive-cycle disambiguation, separability-ladder triad-rung naming (Hintikka echo `definable / identifiable / non-identifiable` candidate; alternates documented in [`msc/separability-standalone-paper-proposal.md`](msc/separability-standalone-paper-proposal.md)).
10. [ ] **🌟 Execute renaming surgery** — slug renames via `bin/rename-slug` and prose-vocabulary renames via terminology entries (`bin/term decide <slug> rename`) + targeted prose-cleanup sweeps. **Status (2026-05-09):** §A complete (7/7 slug renames landed); §B 7/8 (only **item 1** remains — the Class 1/2/3 → Separated/Coupled/Partial bundle with the coordinated Class 2 ↔ 3 numbering swap; warrants its own dedicated commit cycle). Active execution queue: [`/TERMINOLOGY-TODO.md`](TERMINOLOGY-TODO.md). Decisions and rationale recorded in [`msc/naming/naming-rename-plan.md`](msc/naming/naming-rename-plan.md) and replayed into the per-slug `terminology/decisions/` audit trail. Includes the ~135-segment formal-tag cleanup pass mentioned in `TODO.md` §"Naming pipeline — specific deferred items".
11. [ ] **Land canonicalize commitments to terminology** — 88 currents marked `canonicalized*` in `master-list-curated.json` rename_status; each becomes a `terminology/entries/<slug>.md` entry + a `bin/term decide <slug> canonicalize` event so the commitment is preserved in the audit trail. **Active execution queue: [`/TERMINOLOGY-TODO.md`](TERMINOLOGY-TODO.md)** §C (sub-batched as C1–C13 across clean / nuance / FORMAT-layer / compound / adopted-standard categories). Each batch is a natural commit unit; the file shrinks as work happens. After each batch, `bin/term render --output LEXICON.md` regenerates the LEXICON view.
12. [ ] **Separability-ladder standalone paper** — proposal landed at [`msc/separability-standalone-paper-proposal.md`](msc/separability-standalone-paper-proposal.md); 4-6 weeks effort; Journal of Causal Inference primary venue.

### Lexicon
- [ ] Consider segment -> accumulator / alphabetize -> lexicon
- [ ] Update / Refresh Lexicon (manually or automated depending on earlier)

### NOTATION migration to terminology system
- [ ] Migrate `NOTATION.md` to the same auto-generation discipline `LEXICON.md` just adopted. Terminology entries already reserve a `notation:` field; `bin/term render --notation` (or sibling verb) is planned per [`terminology/README.md`](terminology/README.md) §"What is not (yet) here". Lower priority than completing the LEXICON migration. Detail in [TODO §"NOTATION migration to terminology system"](TODO.md#notation-migration-to-terminology-system-queued-2026-05-09).

## Misc
- [x] ~~Review new README outline & partials available~~ — landed via 2026-04-26 doc-pipeline cycle (commits `653cfeb`, `6389e4d`, `b1c61a0`, `104b777`); pipeline at `doc/readme/`, scripts in `bin/` (`build-readme`, `extract-findings`, etc.)
- [ ] Joseph review new README outline & partials available
- [ ] **Per-role README rework** (queued 2026-05-01) — extend `doc/readme/` pipeline to emit `README.md`, `README-auditor.md`, `README-voter.md`, etc. from one source tree. Migrate instructions content from `doc/de-novo-audit-instructions.md` / `naming-principles.md` / `naming-cycle-methodology.md` into role-composable partials. Add auto-generated project-tree partial. Replaces the shelved `tools/role-encounter/` approach. Architecture sketched in [`msc/handoff-2026-05-01.md`](msc/handoff-2026-05-01.md).
- [ ] **Phase 2 semantic index** (queued 2026-05-01) — `psql-18` + pgvector + ollama + `nomic-embed-text-v2-moe`; lift memorata's data layer wholesale. Drives the four-signal naming-target context map (anchor + heaviest-attention + supplementary references + dependency chain) for the renaming agent's harder cases. Architecture brief at [`spikes/spike-local-embedding-benchmark/FINDINGS.md`](spikes/spike-local-embedding-benchmark/FINDINGS.md).
- [ ] Consider modifying & updating link formatting + policy, and tagging (better optimized for both obsidian, plain text, and github)
- [ ] Footnote and citation procedure
- [ ] Historical provenance and relic cleanup (e.g., unimportant TFT mentions even if effectively in footnotes)
- [ ] README v2 pass per Alan Walton's first-human review (queued; detail in [`TODO.md`](TODO.md))