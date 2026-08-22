# PRACTICA
*Current active areas of work with 🌟 (primary) and ⭐ (secondary) indicating most immediate priorities. In AAT terms, this is the top levels of the strategy DAG.*

> **Resuming momentum:** [`CHANGELOG.md`](CHANGELOG.md)'s top entries name what just landed; open Joseph-decisions live in [`JOSEPH-TODO.md`](JOSEPH-TODO.md) (→ the one-sitting briefs at `msc/decision-briefs-2026-07-15.md`). *(The former NEXT-UP.md transient pointer was drained 2026-07-15 per its own charter — residuals migrated, archaeology at `.archive/NEXT-UP-drained-2026-07-15.md`.)* Priming-heavy pointers; skip during de-novo audits.

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

Following the class-coercion-via-wrapping landing and the convergence finding with parallel work on `#disc-adversarial-coupling-pressure` and `spike-strategic-self-coupling`, remaining items in the recommended cycle sequence (GUC rename, M4 cycle, multi-timescale promotion, and Instance-4/Object-B integration are in CHANGELOG 2026-05-09 / 05-21 / 05-24 / 06-10 — not re-queued):

1. **Parts III/IV scope segments — Gate 1.** Deaths taxonomy and both agency-death legs are in canon; their released follow-ons live in TODO §"Deaths taxonomy". The four 03-llm-core scope segments exist at `stage: draft` (verified 2026-08-22: `scope-channel-collapse`, `scope-primitive-logogenic`, `scope-scaffolded-logogenic`, `scope-interiority-loop`; matching OUTLINE rows). `#hyp-checkpoint-forking-failure-modes` lives in `04-eli-core/src/` with an E1 `draft` OUTLINE row. Remaining work here is the **Gate 1 dependency audit** (and onward Gate 2/3) for that 03 cluster, not authoring.
2. **Class-3 closure-defect dynamics analysis** — Move F from `spikes/temporal-nesting-rg/99-verdict.md`. Tests directed-separation-as-graded-order-parameter view (the dynamics-side complement to W₀/W₂/W₁'s structural taxonomy). Separate spike when Parts III/IV is mature enough to motivate it.
3. **Identity-through-substrate-transitions** — connect `obs-substrate-independence` / `def-identity-sufficiency` / `def-five-constitutive-factors` to the persistence template across substrate changes. Anticipated segment `#der-substrate-independent-persistence` added to `04-eli-core/OUTLINE.md` as missing.
4. **Multi-timescale stacking remainders** (promotion of `#der-multi-timescale-stability` is in CHANGELOG 2026-06-10): jump-process slow dynamics, Model S stacking, and which AAT structural-adaptation mechanisms satisfy the premises. Named in the segment's Working Notes.

Order is recommended; bundle adjustments per cycle. The wider naming refactor (the 506 unrouted R2 currents beyond the landed GUC bundle) is queued but stalled — no execution since ~2026-05-10; see §"Current naming conventions refactor" below.

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

**Naming-cycle record packed 2026-08-22** at [`.archive/msc-naming-2026-08-22.tar.gz`](.archive/msc-naming-2026-08-22.tar.gz) (formerly `msc/naming/`). Unpack at the repo root (`tar -xzf .archive/msc-naming-2026-08-22.tar.gz`) to restore the tree. Inner paths below (`msc/naming/...`) are relative to that unpack.

**Honest scope (updated 2026-05-09).** The naming program is a multi-cycle arc, not a single bundle. The R2 cohort produced **629 distinct currents** (proposed and considered names across slugs, prose vocabulary, symbols, and unnamed phenomena) per the master-list at `msc/naming/master-list-curated.json`. Counts re-verified 2026-07-15 against the JSON (the earlier "58 marked / ~511 unrouted" prose undercounted the 2026-05-04 curation pass, which marked 109 entries, not 44):

- **123 currents marked** with a `rename_status` decision (109 from the 2026-05-04 manual curation pass + 14 from the 2026-05-09 GUC rename execution).
- **506 currents unrouted** — no decision yet recorded. The manual curation pass (2026-05-04) considered 118 candidates surfaced by the R2 score-card top entries; 103 were routed (the items now in TERMINOLOGY-TODO §B + §C), 13 deferred (in `msc/naming/to-canonicalize.md`). The remaining 506 currents from the cohort were never considered in that pass — many will be quick dispositions (excluded-no-op, excluded-different-layer, or canonicalize-with-no-action) but a substantial number are genuine rename candidates requiring per-current evaluation and decision.

**What's done:**
- Phase 1 (R1 voting) → Phase 4 (R2 aggregator landing): complete.
- Phase 5 (manual curation pass on 118 high-score candidates): complete; 103/118 routed.
- §A slug renames (7/7): complete.
- §B prose-vocabulary renames (8/8) including the GUC bundle: complete.

**What's not done:**
- §C terminology-canonicalize: C5–C13 executed (CHANGELOG 2026-07-15; 176 entries load). Residues in TERMINOLOGY-TODO: C8 three-word vs compound form (Joseph) and C12 first-encounter cite sweep (item 11).
- §D 13 deferred decisions: pending (item 9).
- 506 unrouted currents from the R2 cohort: not yet evaluated (new item 13 below).
- ~135-segment formal-tag cleanup pass: pending (TODO.md §"Naming pipeline — specific deferred items").
- Several slug renames still pending separate routing decisions (separability-pattern → separability-ladder + rung-name; additive-coordinate-forcing → forced-coordinates; deriv-causal-ib-exploration → ?; ASF umbrella naming).

**Phase-1 prior history (preserved as decision-record archaeology):** pilot complete; full role-prefix sweep complete (142 segments under `{type-prefix}-{subject-noun}`); refined principles file landed (2026-04-24, `b9492b7`); rename-vs-add-alias and rename-vs-canonicalize semantics extended in principles file (2026-04-29). Architectural invariants: role-prefix from frontmatter (mechanical via `bin/align-slug`); subject-noun preference; Greek-vocabulary commitment with open-semantic-space justification; separate-passes methodology. Phase-2 enrichment passes complete (Pass A/B/C); Pass D collision-check complete (2026-04-29, `msc/naming/collision-check-2026-04-29.md`). Phase-3 R2 voting cohort closed (2026-04-30); final cohort spans gemini-r2, opus-r2b/c, sonnet-r2b/c, codex-r2b at varying coverage levels; off-scale residual 0 across r2c. **Phase-4 R2 aggregator landed (2026-05-01, commits `21ef4a5`, `7abdb7a`, `3dbc0aa`, `45bd00e`)**: `bin/naming-r2-aggregate.rb` produces three outputs — score-card sorted by `max(score/n)`, per-target detail view, cross-cutting patterns doc with categorical groupings + coordination flags. Substance factor smooth `(0.7 + 0.3 × effort) × (1.0 + novelty)` with 1.2× multipliers for top-pick + canonicalize. R1 folded as one synthetic voter. Mid-cycle methodological findings captured in `msc/naming/mini-lexicon-todo.md` §11–§12. Reference: [`msc/reflections/22-substrate-handoff-and-rationale-attribution.md`](msc/reflections/22-substrate-handoff-and-rationale-attribution.md), [`msc/reflections/23-harness-side-persistence-failure.md`](msc/reflections/23-harness-side-persistence-failure.md), [`msc/reflections/24-framework-as-its-own-diagnostic.md`](msc/reflections/24-framework-as-its-own-diagnostic.md).

9. [ ] **Final decisions on the 13 remaining rows** — citability-fix specials (specification bound; epistemic substate / purposeful substate pair-row; "purpose" / "purposeful" register; etc.), Holling-collision adaptive-cycle handling, adaptive-cycle disambiguation, separability-ladder triad-rung naming (Hintikka echo `definable / identifiable / non-identifiable` candidate; alternates documented in [`msc/separability-standalone-paper-proposal.md`](msc/separability-standalone-paper-proposal.md)).
11. [ ] **Terminology canonicalize residues** — C5–C13 executed (CHANGELOG 2026-07-15). Remaining in [`TERMINOLOGY-TODO.md`](TERMINOLOGY-TODO.md): C8 three-word vs compound form (Joseph) and C12 first-encounter cite sweep. The ~135-segment formal-tag cleanup pass in TODO §"Naming pipeline" is a separate hygiene pass.
12. [ ] **Separability-ladder standalone paper** — proposal landed at [`msc/separability-standalone-paper-proposal.md`](msc/separability-standalone-paper-proposal.md); 4-6 weeks effort; Journal of Causal Inference primary venue.
13. [ ] **🌟 Continue naming-cycle evaluation on 506 unrouted R2 currents** — the curation + GUC passes marked 123 of 629 currents from the master-list cohort. 506 remain unrouted with no `rename_status` (verified 2026-07-15). Many will quickly disposition as excluded-no-op (different layer / not actionable / outside the naming-program scope) or canonicalize-no-op (current name is already the canonical form, no LEXICON action needed); but a substantial fraction are genuine rename candidates requiring per-current evaluation. Recommended approach: continue the manual curation pattern that worked for the first 118, in score-card-ordered batches via the R2 aggregator's `r2-aggregate-table.md` / `r2-aggregate-detail.md` / `r2-patterns.md` artifacts. Each batch routes to canonicalize / rename / add-alias / defer / excluded with brief rationale, recorded in `msc/naming/naming-rename-plan.md` and reflected in master-list-curated.json `rename_status` per the established schema. Multi-cycle work — likely several months of evaluation passes interleaved with execution cycles. The 2026-05-04 cycle showed ~12 candidates per Joseph-author batch was a sustainable rhythm; 506 remaining at that rate is roughly 40+ batches.

### Lexicon
- [ ] Consider segment -> accumulator / alphabetize -> lexicon
- [ ] Update / Refresh Lexicon (manually or automated depending on earlier)

### NOTATION migration to terminology system
- [ ] Migrate `NOTATION.md` to the same auto-generation discipline `LEXICON.md` just adopted. Terminology entries already reserve a `notation:` field; `bin/term render --notation` (or sibling verb) is planned per [`terminology/README.md`](terminology/README.md) §"What is not (yet) here". Lower priority than completing the LEXICON migration. Detail in [TODO §"NOTATION migration to terminology system"](TODO.md#notation-migration-to-terminology-system-queued-2026-05-09).

## Misc
- [ ] Joseph review new README outline & partials available
- [ ] **Per-role README rework** (queued 2026-05-01) — extend `doc/readme/` pipeline to emit `README.md`, `README-auditor.md`, `README-voter.md`, etc. from one source tree. Migrate instructions content from `doc/de-novo-audit-instructions.md` / `doc/sop/naming.sop/principles.sop.md` / `doc/sop/naming.sop/methodology.sop.md` into role-composable partials. Add auto-generated project-tree partial. Replaces the shelved `tools/role-encounter/` approach. Architecture sketched in [`msc/handoff-2026-05-01.md`](msc/handoff-2026-05-01.md).
- [ ] **Phase 2 semantic index** (queued 2026-05-01) — `psql-18` + pgvector + ollama + `nomic-embed-text-v2-moe`; lift memorata's data layer wholesale. Drives the four-signal naming-target context map (anchor + heaviest-attention + supplementary references + dependency chain) for the renaming agent's harder cases. Architecture brief at [`spikes/spike-local-embedding-benchmark/FINDINGS.md`](spikes/spike-local-embedding-benchmark/FINDINGS.md).
- [ ] Consider modifying & updating link formatting + policy, and tagging (better optimized for both obsidian, plain text, and github)
- [ ] Footnote and citation procedure
- [ ] Historical provenance and relic cleanup (e.g., unimportant TFT mentions even if effectively in footnotes)
- [ ] README v2 pass per Alan Walton's first-human review (queued; detail in [`TODO.md`](TODO.md))