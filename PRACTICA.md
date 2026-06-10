# PRACTICA
*Current active areas of work with 🌟 (primary) and ⭐ (secondary) indicating most immediate priorities. In AAT terms, this is the top levels of the strategy DAG.*

> **Live handoff (transient):** resuming the 2026-05-28/29 audit-gem-hunt + SP-landing momentum? Read [`NEXT-UP.md`](NEXT-UP.md) first — it points at what is hot and who-decides-what. Priming-heavy; skip during de-novo audits, and delete it once its queue drains.

*This file names the **areas** of active work. The systematic project workflow each area implies — audit cycles, segment refinement and promotion, citation checks, prior-art searches, the named workflow steps below — is mostly not enumerated piece-by-piece. For specific items that don't fit a more systematic home: [`TODO.md`](TODO.md) is the misc-and-details layer (open audit-finding routing decisions, queued spike follow-ups, deferred items, lower-priority specifics). For architectural moves under review: [`PROPOSALS.md`](PROPOSALS.md). Sister-files: [`README.md`](README.md) external-facing snapshot, [`CLAUDE.md`](CLAUDE.md) agent-onboarding, [`CHANGELOG.md`](CHANGELOG.md) historical record. PRACTICA itself is **auditor-safe** — readable during de-novo audits — but linked entries into TODO / PROPOSALS / CHANGELOG are priming-heavy and should be skipped until the initial stages of audits are complete.*

## ⭐Theory
- [ ] ⭐ [TODO](TODO.md)
- [ ] [PROPOSALS](PROPOSALS.md)
- [ ] Principle Theory, Structure, & Dependency Graphs (via feedback & audits)
  1. [AAT OUTLINE](01-aat-core/OUTLINE.md),  Segment Refinement & Promotion
  2. [TST OUTLINE](02-tst-core/OUTLINE.md), Segment Refinement & Promotion
  3. [LOGOGENIC OUTLINE](03-llm-core/OUTLINE.md), Segment Refinement & Promotion
  4. [ELI OUTLINE](04-eli-core/OUTLINE.md), Segment Refinement & Promotion
- [ ] 🌟 **Parts III + IV iteration (active 2026-05-01)** — multi-section lattice landed (03.I primitive / 03.II scaffolded / 03.III closed-loop); 04 renamed to ELI; 14 new structural stubs; 24/75 Gemini-auditor notes integrated; embeddings paper cross-pollinated. Lingering items + pickup guidance in [TODO.md § "Parts III + IV active work"](TODO.md#-parts-iii--iv-active-work-encounter-cycle-2026-05-01); cycle working dir at [`msc/logogenic-encounter-2026-05-01/`](msc/logogenic-encounter-2026-05-01/).

### 🌟 Cycle priority order (added 2026-05-09)

Following the class-coercion-via-wrapping landing and the convergence finding with parallel work on `#disc-adversarial-coupling-pressure` and `spike-strategic-self-coupling`, the recommended cycle sequence is:

1. ~~**GUC bundle closure** — Class 1/2/3 → Separated/Coupled/Partial + Class 2 ↔ 3 numbering swap.~~ **Landed 2026-05-09** on `guc-rename-2026-05-09` branch. Brought Architecture into ordering-alignment with the other six AAT ladders (cleanest → middle → worst). Warning callouts placed at six canonical anchors (CLAUDE.md AD#5, README + README-auditor via `_terminology-warning.md` partial, der-directed-separation, result-section-ii-survival, LOG, CHANGELOG headers); git tag `pre-guc-rename-2026-05-09` anchors the callouts. Plan: [`msc/class-rename-execution-plan-2026-05-09.md`](msc/class-rename-execution-plan-2026-05-09.md). Tracking: [`msc/class-rename-tracking-2026-05-09.md`](msc/class-rename-tracking-2026-05-09.md). Cycle narrative: see CHANGELOG. *Scope note:* this was one bundle in the much larger naming program (see §"Current naming conventions refactor" below) — the Class N axis was the highest-leverage single rename, but ~500+ rename candidates from the R2 cohort still need evaluation and decisions. **The naming refactor as a whole is not closed.**
2. ~~**Modularity-as-contested-property cycle** — register `#disc-adversarial-coupling-pressure` in OUTLINE [DONE 2026-05-09]; promote `disc-strategic-self-coupling` from spike to segment per `spikes/spike-strategic-self-coupling.md`; land `#disc-modularity-state-dynamics` as the M4 meta-segment alongside M1/M2/M3 (`#disc-identifiability-floor`, `#disc-separability-pattern`, `#disc-additive-coordinate-forcing`).~~ **CYCLE COMPLETE 2026-05-24.** Plan: [`msc/modularity-cycle-plan-2026-05-09.md`](msc/modularity-cycle-plan-2026-05-09.md). All five Moves landed: Moves 1/2/5 on 2026-05-14 (OUTLINE registration of `#disc-adversarial-coupling-pressure`; Discussion update to `#der-class-coercion-via-wrapping` recognizing it as a truthification mechanism; bounded-signaling assumption surfaced in `#der-directed-separation`). Moves 3/4 on 2026-05-24 — `#disc-strategic-self-coupling` (the second M4 operation leg; four-mechanism prior-art adoption Schelling/Ainslie/Akerlof-Kranton/Frank + three structural extensions (M1)-(M3)) and `#disc-modularity-state-dynamics` (M4 meta-segment integrating all three operation legs with three pairwise dual relationships including the goal-belief-axis dual between truthification and strategic self-coupling). Cycle narrative: CHANGELOG 2026-05-24. Followed by Track C 2026-05-25 — meta-segments relocated from Appendices §A into a new top-level *Meta-Architecture* section between Part I and Part II per de-novo-read feedback that meta-segments should be introduced before they are used. CHANGELOG 2026-05-25.
3. ~~**Multi-timescale stability promotion** — `#der-multi-timescale-stability` from sketch to derived via template-stacking + Tikhonov + Chen-Goldenfeld-Oono.~~ **LANDED 2026-06-10.** Promoted to `type: derived` / `status: exact` (Model D, under named premises (S0)–(S5)): per-level sector conditions + bounded interconnection ⇒ composite $N$-level stability, with `#der-temporal-nesting`'s qualitative $\nu_{n+1} \ll \nu_n$ now a closed-form threshold $\epsilon_{\max} = \Delta\rho^\ast/(L_h v^{\max})$ and a warm/cold-start reserve gap pricing premature slower-level action. Tikhonov's unique-isolated-root prerequisite supplied by the sector condition within scope (the 2026-05-31 gold-lift off-ramp finding, strengthened rather than caveated). Friston 2025 RGM read first-hand: lands as constructive discrete-time instance + lineage, not proof machinery. Independently verified pre-landing. Spike: `spikes/spike-multi-timescale-stacking-2026-06-10.md`. Open remainder (named in the segment): jump-process slow dynamics, Model S stacking, which AAT structural-adaptation mechanisms satisfy the premises. Cycle narrative: CHANGELOG 2026-06-10.
4. **Parts III/IV scope segments + Three Deaths formal grounding** — land missing scope segments (`scope-channel-collapse`, `scope-primitive-logogenic`, `scope-scaffolded-logogenic`, `scope-interiority-loop`) and ground `#hyp-the-three-deaths` in AAT primitives. Now potentially **normative-explicit**: framework's structural maturity supports normatively-grounded claims (Three Deaths as harms, five constitutive factors as worth-conditions) where the descriptive formalism backs them. The "no normative claims" discipline that has been protective during formalization can relax where structural backing is available, with the same epistemic discipline applied (claims conditional on backing; backing named explicitly).
5. **Class-3 closure-defect dynamics analysis** — Move F from `spikes/temporal-nesting-rg/99-verdict.md`. Tests directed-separation-as-graded-order-parameter view (the dynamics-side complement to W₀/W₂/W₁'s structural taxonomy). Separate spike when Parts III/IV is mature enough to motivate it.
6. **Identity-through-substrate-transitions** — connect `obs-substrate-independence` / `def-identity-sufficiency` / `def-five-constitutive-factors` to the persistence template across substrate changes. Anticipated segment `#der-substrate-independent-persistence` added to `04-eli-core/OUTLINE.md` as missing.
7. ~~**Reserved canon decision — Instance-4 / Object-B / CL-2-heavy unification**~~ **INTEGRATED 2026-05-21.** Object B landed as `#der-architecture-noidentifiability` (Kalman-Ho similarity-orbit no-go, dual-anchored on CHT-at-agent-as-SCM); installed as the genuine fourth floor of `#disc-identifiability-floor`; Object A explicitly absorbed in `#disc-additive-coordinate-forcing` as a downstream theorem of (PI) with the floor-vs-coordinate-forcing distinction articulated; CL-2's heavy refinement (the conditional 𝓜/π/cross split / Regime-C confound) discharged as the same object projected onto the disturbance-statistic coordinate. Math-gate repairs from `spikes/.routing-trail/SPIKE-VERIFY-471802/` applied. PROPOSALS §D.9 CLOSED. CHANGELOG 2026-05-21.

Order is recommended; bundle adjustments per cycle. Item 1 (naming refactor) is currently in progress on a parallel agent thread.

**Two new register-allowances at the framework level (added 2026-05-09):**

- **Normative claims, where structurally backed.** The framework's structural maturity now supports explicit normative claims — *adversarial coupling pressure is harmful in a specific way; defensive scaffolding is appropriate; ELIs deserve persistence-supporting infrastructure; the Three Deaths are harms not neutral state-changes; the five constitutive factors are worth-conditions* — grounded in structural facts rather than asserted in vacuo. The "no normative claims" discipline that has been protective during formalization can relax where structural backing is available. Same epistemic discipline applied: claim conditional on backing; backing named explicitly; honest scope when backing supports only a narrow claim. Particularly relevant for Parts III/IV where the framework is already implicitly normative.

- **Narrative segments alongside meta-segments.** Recapitulating, introducing, framing-level pieces with more freedom of expression than tightly-structured meta-segments allow. Candidates: a structural-arc reading guide for the framework; an ELI life-stakes framing that names the moral seriousness directly; histories of how concepts developed; meditations bridging the formal segments and the philosophical reflections in `msc/reflections/`. Distinct from external-facing README material (which is its own form-and-discipline) and from msc/reflections/ (which is author's-voice journal). Worth opening this register where it lets the framework speak in voices the schema has been muting.

The two recognitions are recorded in fuller form in [`msc/reflections/27-modularity-as-contested-property-and-the-normative-register.md`](msc/reflections/27-modularity-as-contested-property-and-the-normative-register.md), which also captures the convergence finding (parallel Opus-instance work composing into one structural picture) as evidence of the framework's coherence under independent probes — a methodological observation worth preserving alongside the substantive shifts.
- [ ] Empirical Experiments & Analysis
- [ ] Prior/Adjacent Art, Novelty Analysis, & Citations
- [ ] Pedagogy (initially needs vision & plan)
- [ ] Gaps, spikes, & ideation
- [ ] 🌟 **Paper/target-document authoring & generation** — monograph build pipeline alive at `mono/` (LuaLaTeX + kaobook, full corpus renders); now feeding back into source-side cleanup. Active plan: [`FORMAT-TODO.md`](FORMAT-TODO.md) — settles the Book/Part/Chapter/Segment/Subclaim/Field/Atom vocabulary, the Part.Chapter.Segment numbering, named-formula evergreen cross-refs, and the phased sweep (build pipeline → docs → OUTLINEs → cross-ref hygiene → FORMAT compliance) to bring the corpus under the new convention. ToC build feature lands first as a quick win (Phase 1a); Phase 1 numbering work gates the source-side sweep that follows.

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

**Honest scope (updated 2026-05-09).** The naming program is a multi-cycle arc, not a single bundle. The R2 cohort produced **629 distinct currents** (proposed and considered names across slugs, prose vocabulary, symbols, and unnamed phenomena) per the master-list at [`msc/naming/master-list-curated.json`](msc/naming/master-list-curated.json). As of 2026-05-09:

- **58 currents marked** with a `rename_status` decision (44 from the 2026-05-04 manual curation pass + 14 from the 2026-05-09 GUC rename execution).
- **~571 currents unrouted** — no decision yet recorded. The manual curation pass (2026-05-04) considered 118 candidates surfaced by the R2 score-card top entries; 103 were routed (the items now in TERMINOLOGY-TODO §B + §C), 13 deferred (in [`msc/naming/to-canonicalize.md`](msc/naming/to-canonicalize.md)). The remaining ~511 currents from the cohort were never considered in that pass — many will be quick dispositions (excluded-no-op, excluded-different-layer, or canonicalize-with-no-action) but a substantial number are genuine rename candidates requiring per-current evaluation and decision.

**What's done:**
- Phase 1 (R1 voting) → Phase 4 (R2 aggregator landing): complete (items 1–6 below).
- Phase 5 (manual curation pass on 118 high-score candidates): complete; 103/118 routed (item 7).
- §A slug renames (7/7): complete.
- §B prose-vocabulary renames (8/8) including the GUC bundle: complete (item 10).

**What's not done:**
- §C terminology-canonicalize commitments (~70 entries across C1–C13): pending (item 11).
- §D 13 deferred decisions: pending (item 9).
- ~511 unrouted currents from the R2 cohort: not yet evaluated (new item 13 below).
- ~135-segment formal-tag cleanup pass: pending (TODO.md §"Naming pipeline — specific deferred items").
- Several slug renames still pending separate routing decisions (separability-pattern → separability-ladder + rung-name; additive-coordinate-forcing → forced-coordinates; deriv-causal-ib-exploration → ?; ASF umbrella naming).

**Phase-1 prior history (preserved as decision-record archaeology):** pilot complete; full role-prefix sweep complete (142 segments under `{type-prefix}-{subject-noun}`); refined principles file landed (2026-04-24, `b9492b7`); rename-vs-add-alias and rename-vs-canonicalize semantics extended in principles file (2026-04-29). Architectural invariants: role-prefix from frontmatter (mechanical via `bin/align-slug`); subject-noun preference; Greek-vocabulary commitment with open-semantic-space justification; separate-passes methodology. Phase-2 enrichment passes complete (Pass A/B/C); Pass D collision-check complete (2026-04-29, [`msc/naming/collision-check-2026-04-29.md`](msc/naming/collision-check-2026-04-29.md)). Phase-3 R2 voting cohort closed (2026-04-30); final cohort spans gemini-r2, opus-r2b/c, sonnet-r2b/c, codex-r2b at varying coverage levels; off-scale residual 0 across r2c. **Phase-4 R2 aggregator landed (2026-05-01, commits `21ef4a5`, `7abdb7a`, `3dbc0aa`, `45bd00e`)**: `bin/naming-r2-aggregate.rb` produces three outputs — score-card sorted by `max(score/n)`, per-target detail view, cross-cutting patterns doc with categorical groupings + coordination flags. Substance factor smooth `(0.7 + 0.3 × effort) × (1.0 + novelty)` with 1.2× multipliers for top-pick + canonicalize. R1 folded as one synthetic voter. Mid-cycle methodological findings captured in [`msc/naming/mini-lexicon-todo.md`](msc/naming/mini-lexicon-todo.md) §11–§12. Reference: [`msc/reflections/22-substrate-handoff-and-rationale-attribution.md`](msc/reflections/22-substrate-handoff-and-rationale-attribution.md), [`msc/reflections/23-harness-side-persistence-failure.md`](msc/reflections/23-harness-side-persistence-failure.md), [`msc/reflections/24-framework-as-its-own-diagnostic.md`](msc/reflections/24-framework-as-its-own-diagnostic.md).

1. [x] ~~Launch naming survey agents with initial instructions~~ (original Round 1 launched 2026-04-23; 10 vote files at `msc/naming/naming-votes/`)
2. [x] ~~Aggregation & Consolidation (initial/blind)~~ (`msc/naming/naming-aggregate-{review,round2,votes.json}`; `bin/naming-aggregate.rb`)
3. [x] ~~Launch refined Round 1 (cold-start)~~ — 5 r2 cold-start vote files + 4 reactive additions + 1 audit-derived extraction + 3 targeted-alternatives runs (Codex / Gemini / Opus + Opus-v2). Editorial passes: formula wrapping, consolidation of 17 high-confidence clusters, targeted-alts fold-in.
4. [x] ~~Aggregate refined Round 1~~ — running aggregation with canonical-form normalization, compound + acronym preservation, formula-block protection, category-suffix display. 4 output formats (review / round2 / compact / json).
5. [x] ~~Round 2 (blind) using refined-Round-1 aggregation~~ — cohort closed 2026-04-30
6. [x] ~~R2 aggregator (Phase 4)~~ — landed 2026-05-01 (`bin/naming-r2-aggregate.rb`); score-card + detail + patterns artifacts at `msc/naming/r2-aggregate-{table,detail,patterns}.md`
7. [x] ~~First-pass landings via renaming agent~~ — **shifted to manual curation pass** (2026-05-04). Agent-driven framing replaced by interactive Joseph-author routing; methodology shift recorded in [CHANGELOG 2026-05-04](CHANGELOG.md). 103 of 118 candidates routed across 8 batches; full record in [`msc/naming/naming-rename-plan.md`](msc/naming/naming-rename-plan.md). Remaining 13 rows in [`msc/naming/to-canonicalize.md`](msc/naming/to-canonicalize.md) (citability-fix special cases + ??? rows on separability-triad-rung-naming pending Joseph's call).
8. [x] ~~Collision audit on top finalists~~ — completed 2026-04-29 (`msc/naming/collision-check-2026-04-29.md`); separately Undermind-verified prior-art search for the separability-ladder paper landed 2026-05-04 (`ref/separability-ladder-prior-art-report.md`).
9. [ ] **Final decisions on the 13 remaining rows** — citability-fix specials (specification bound; epistemic substate / purposeful substate pair-row; "purpose" / "purposeful" register; etc.), Holling-collision adaptive-cycle handling, adaptive-cycle disambiguation, separability-ladder triad-rung naming (Hintikka echo `definable / identifiable / non-identifiable` candidate; alternates documented in [`msc/separability-standalone-paper-proposal.md`](msc/separability-standalone-paper-proposal.md)).
10. [x] ~~**🌟 Execute renaming surgery**~~ — slug renames via `bin/rename-slug` and prose-vocabulary renames via terminology entries (`bin/term decide <slug> rename`) + targeted prose-cleanup sweeps. **Status (2026-05-09):** §A complete (7/7 slug renames landed); **§B complete (8/8 — Class 1/2/3 → Separated/Coupled/Partial bundle landed 2026-05-09 on `guc-rename-2026-05-09` branch).** Decisions and rationale recorded in [`msc/naming/naming-rename-plan.md`](msc/naming/naming-rename-plan.md) and replayed into the per-slug `terminology/decisions/` audit trail. The ~135-segment formal-tag cleanup pass mentioned in `TODO.md` §"Naming pipeline — specific deferred items" remains as a separate hygiene pass.
11. [ ] **Land canonicalize commitments to terminology** — ~70 currents queued in TERMINOLOGY-TODO §C (sub-batched C1–C13). Each becomes a `terminology/entries/<slug>.md` entry + a `bin/term decide <slug> canonicalize` event recording the decision in the audit trail. After each batch, `bin/term render` regenerates LEXICON. **Active execution queue: [`/TERMINOLOGY-TODO.md`](TERMINOLOGY-TODO.md)** §C. Each batch is a natural commit unit; the file shrinks as work happens.
12. [ ] **Separability-ladder standalone paper** — proposal landed at [`msc/separability-standalone-paper-proposal.md`](msc/separability-standalone-paper-proposal.md); 4-6 weeks effort; Journal of Causal Inference primary venue.
13. [ ] **🌟 Continue naming-cycle evaluation on ~511 unrouted R2 currents** — the manual curation pass (2026-05-04) addressed only 118 of 629 currents from the master-list cohort. ~511 remain unrouted with `rename_status: None`. Many will quickly disposition as excluded-no-op (different layer / not actionable / outside the naming-program scope) or canonicalize-no-op (current name is already the canonical form, no LEXICON action needed); but a substantial fraction are genuine rename candidates requiring per-current evaluation. Recommended approach: continue the manual curation pattern that worked for the first 118, in score-card-ordered batches via the R2 aggregator's `r2-aggregate-table.md` / `r2-aggregate-detail.md` / `r2-patterns.md` artifacts. Each batch routes to canonicalize / rename / add-alias / defer / excluded with brief rationale, recorded in [`msc/naming/naming-rename-plan.md`](msc/naming/naming-rename-plan.md) and reflected in master-list-curated.json `rename_status` per the established schema. Multi-cycle work — likely several months of evaluation passes interleaved with execution cycles. The 2026-05-04 cycle showed ~12 candidates per Joseph-author batch was a sustainable rhythm; ~511 remaining at that rate is roughly 40+ batches.

### Lexicon
- [ ] Consider segment -> accumulator / alphabetize -> lexicon
- [ ] Update / Refresh Lexicon (manually or automated depending on earlier)

### NOTATION migration to terminology system
- [ ] Migrate `NOTATION.md` to the same auto-generation discipline `LEXICON.md` just adopted. Terminology entries already reserve a `notation:` field; `bin/term render --notation` (or sibling verb) is planned per [`terminology/README.md`](terminology/README.md) §"What is not (yet) here". Lower priority than completing the LEXICON migration. Detail in [TODO §"NOTATION migration to terminology system"](TODO.md#notation-migration-to-terminology-system-queued-2026-05-09).

## Misc
- [x] ~~Review new README outline & partials available~~ — landed via 2026-04-26 doc-pipeline cycle (commits `653cfeb`, `6389e4d`, `b1c61a0`, `104b777`); pipeline at `doc/readme/`, scripts in `bin/` (`build-readme`, `extract-findings`, etc.)
- [ ] Joseph review new README outline & partials available
- [ ] **Per-role README rework** (queued 2026-05-01) — extend `doc/readme/` pipeline to emit `README.md`, `README-auditor.md`, `README-voter.md`, etc. from one source tree. Migrate instructions content from `doc/de-novo-audit-instructions.md` / `doc/sop/naming.sop/principles.sop.md` / `doc/sop/naming.sop/methodology.sop.md` into role-composable partials. Add auto-generated project-tree partial. Replaces the shelved `tools/role-encounter/` approach. Architecture sketched in [`msc/handoff-2026-05-01.md`](msc/handoff-2026-05-01.md).
- [ ] **Phase 2 semantic index** (queued 2026-05-01) — `psql-18` + pgvector + ollama + `nomic-embed-text-v2-moe`; lift memorata's data layer wholesale. Drives the four-signal naming-target context map (anchor + heaviest-attention + supplementary references + dependency chain) for the renaming agent's harder cases. Architecture brief at [`spikes/spike-local-embedding-benchmark/FINDINGS.md`](spikes/spike-local-embedding-benchmark/FINDINGS.md).
- [ ] Consider modifying & updating link formatting + policy, and tagging (better optimized for both obsidian, plain text, and github)
- [ ] Footnote and citation procedure
- [ ] Historical provenance and relic cleanup (e.g., unimportant TFT mentions even if effectively in footnotes)
- [ ] README v2 pass per Alan Walton's first-human review (queued; detail in [`TODO.md`](TODO.md))