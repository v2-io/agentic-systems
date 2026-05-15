# Class-Coercion Spike: Integration Plan

**Status**: **complete** (execution finished 2026-05-09). All Phase A–F items closed; lint clean on new segments; outline-lint shows 0 missing dependencies. Reasoning trail in spike directory preserved per project convention; segments under `01-aat-core/`, `03-logogenic-agents/`, `04-eli/` carry the substantive theory.
**Purpose**: durable, executable plan for interning class-coercion spike results into the theory so that the spike directory is no longer load-bearing. Designed for handoff: any agent (or future-me) reading this should be able to pick up at the next unchecked step.
**Authoritative inputs**: `99-verdict.md` (especially §4 segment-landing recommendations) and the empirical/theoretical content in `01`–`08` and `09`.

**Posture** (per Joseph's framing during the spike): integration content within ASF's prior-art-integration discipline. AAD's contribution is the *synthesis* with sector-Lyapunov / Brooks's-Law / class-taxonomy machinery, plus the W₀/W₂/W₁ leakage-regime hierarchy. The wrapping move itself is rediscovery of POMDP / cognitive-architecture moves, cited generously.

---

## Tracking key

- `[ ]` not started
- `[~]` in progress
- `[x]` done
- `[!]` blocked / needs Joseph

## Phase A — Read existing context

Verifies the integration's specifics. No writes yet.

- [x] `01-aat-core/src/der-directed-separation.md` — read (during plan-writing). Already has Class 1/2/3 + κ_processing + Pearl-blanket framing + composite class inheritance. Discussion update is additive, not destructive.
- [ ] `01-aat-core/src/hyp-directed-separation-under-composition.md` — read for current state and how to add the "constructive special case" Discussion note.
- [ ] `01-aat-core/src/form-composition-closure.md` — already heavily read in conversation. Confirm Discussion-section landing slot.
- [ ] `01-aat-core/src/der-tempo-composition.md` — already heavily read. Confirm Discussion-section landing slot.
- [ ] `03-logogenic-agents/src/def-coupled-update-dynamics.md` — read; the wrapping segment in 03 must dovetail with the existing coupled-formulation framing.
- [ ] `03-logogenic-agents/src/scope-scaffolded-logogenic.md` — read; the W₂/W₁ regime distinction probably maps onto a refinement of scaffolded-logogenic.
- [ ] `03-logogenic-agents/src/scope-primitive-logogenic.md` — read; check the partition logic.
- [ ] `04-eli/src/def-auxilia-hierarchy.md` — read; auxilia are the constructive realization of W₁ for logogenic substrate.
- [ ] `01-aat-core/OUTLINE.md` — read for canonical-ordering insertion point.
- [ ] `03-logogenic-agents/OUTLINE.md` — read for canonical-ordering insertion point.
- [ ] `FORMAT.md` — refresh on segment cadence (frontmatter, sections, Findings schema, Working Notes rules).
- [ ] `LEXICON.md` — check if any wrapping vocabulary already exists; if not, add new entries during D-phase.

## Phase B — New segments

### B1. `01-aat-core/src/der-class-coercion-via-wrapping.md` (NEW)

Load-bearing AAD-core segment. Slug per CLAUDE.md role-prefix mapping: `derived` → `der`, subject-noun = `class-coercion-via-wrapping`. Final slug: `der-class-coercion-via-wrapping`.

- [ ] frontmatter:
  ```yaml
  slug: der-class-coercion-via-wrapping
  type: derived
  status: derived
  depends:
    - form-composition-closure
    - der-directed-separation
    - hyp-directed-separation-under-composition
    - def-agent-environment
    - deriv-sector-condition
    - result-sector-persistence-template
    - der-tempo-composition
  stage: draft
  ```
- [ ] Title and one-sentence summary.
- [ ] Formal Expression:
  - §1 Setup (wrapper state X_W = (M_W, G_W), query selectors q_M / q_G, update maps f_M / f_G with type signatures).
  - §2 Conditions C1 (admissibility), C2 (stationary component conditional), C3 (no implicit goal-inference).
  - §3 Theorem 1 (exact form): under C1–C3, wrapper satisfies (A1)–(A4) at wrapper level (with wrapper-design constraints D-A2/D-A3/D-A4), and directed separation holds exactly at wrapper level. Therefore wrapper is Class-1.
  - §4 Theorem 2 (approximate form): C3 replaced by KL leakage bound κ; data-processing inequality propagates to wrapper-level KL bound.
  - §5 W₀/W₂/W₁ regime hierarchy table (from `03-leakage.md` §2). κ_W₁ ≤ I(A(q_M); G_W | q_M) — *structural*. κ_W₂ bounded only behaviorally; **no structural bound**.
- [ ] Epistemic Status: derived under (C1)–(C3) + D-A2/A3/A4. Tier 1 belief-update class for D-A4. Honest scope on C3-failure for real LLMs (κ_W₁ bound is empirical, the structural form is the ideal).
- [ ] Discussion:
  - Component admissibility: Class A (goal-blind by design) / Class B (admit goal-blind mode) / Class C (fundamentally goal-conditioned). LLMs in Class B with leakage caveats.
  - ε*_track vs ε*_coerce disambiguation (from `04-epsilon-semantics.md`).
  - Quality-vs-separation tradeoff inside Class B.
  - Connection to Brooks's-Law form: C_coord^wrap as cost of class coercion in tempo.
  - Connection to persistence template: wrapper-level persistence inherits with effective disturbance ρ_W = ρ_ext + ρ_int.
  - Form-preservation reading (cite Friston 2019 / 2025 RGM and Mehta-Schwab 2014 / Kline-Palmer 2022 IB-as-RG / Chen-Goldenfeld-Oono 1996 — DO NOT cite the temporal-nesting-rg spike directly, segment voice).
- [ ] Findings section per FORMAT.md:
  - **Brief** (Feynman-criterion plain-language): A Class-3 component (one whose belief and goal updates are entangled) can be wrapped in an external scaffold that maintains explicit belief and goal stores separately, with the structural rule that belief updates only see goal-blind queries to the component. Under stated conditions this gives directed separation at the wrapper level — the wrapped system is Class-1 by construction, even though the underlying component isn't. The cost shows up as more component calls per cycle and a residual leakage bound from the component's pretraining.
  - **Impact**: promotes `#hyp-directed-separation-under-composition` to derived (special case); refines `#der-directed-separation` Class-1 with structural-vs-behavioral sub-distinction; resolves CLAUDE.md "Class 2 exit" framing into a constructive route through; clarifies Parts I/II ↔ III/IV relationship; gives the LLM-substrate scope a clean theoretical handle.
  - **Novelty Claim**: *Claim integration*. The wrapping move is rediscovery of POMDP / cognitive-architecture patterns; AAD's contribution is the integration with sector-Lyapunov persistence machinery, Brooks's-Law tempo accounting, the Class-1/2/3 directed-separation classification, and the LLM-specific (C1)–(C3) admissibility + leakage conditions. Cite generously per the prior-art-integration discipline.
  - **Related Work table**:
    - POMDP / Bayesian decision theory (Astrom 1965; Kaelbling, Littman, Cassandra 1998 *Artificial Intelligence* 101) — *closest formal prior art*; Bayesian belief-update is goal-blind by construction.
    - Cognitive architectures (Newell 1990 *Unified Theories of Cognition*; Laird 2012 *The Soar Cognitive Architecture*; Anderson 2007 *How Can the Human Mind Occur in the Physical Universe*; Sun 2016 CLARION; Baars 1988 / Dehaene 2014 Global Workspace) — *architectural prior art* for modular agent design with separated belief/goal/action state.
    - MDP-homomorphism / state abstraction (Ravindran-Barto 2004; Taylor-Precup-Panangaden 2008; Abel et al. 2016/2020; Subramanian-Mahajan 2020; Congeduti-Mey-Oliehoek 2020) — *adjacent* control-theoretic predictive-loss bounds; AAD connects via the bridge lemma.
    - Categorical / structured systems theory (Smithe 2024 *Structured Active Inference* arXiv:2406.07577; Capucci, Gavranović, Hedges et al. 2022) — *adjacent compositional algebra*; AAD's wrapping construction is consistent with the lens framing.
    - FEP-RG / scale-free active inference (Friston 2019 *J. Theor. Biol.*; Friston et al. 2025 *Front. Network Physiology*) — *adjacent form-preservation literature*; AAD's wrapper inherits form-preservation under coarse-graining.
    - IB-as-RG (Mehta-Schwab 2014 arXiv:1410.3831; Kline-Palmer 2022 PMC8967309) — *adjacent IB-Lagrangian preservation*; (P1) of `#form-composition-closure` is IB-shaped.
    - Singular-perturbation–RG (Chen-Goldenfeld-Oono 1996 *Phys. Rev. E* 54:376) — *adjacent timescale-separation* tools; the K_c≫1 regime invokes this.
    - Tool-using LLM frameworks (Yao et al. 2022 ReAct; Shinn et al. 2023 Reflexion; Park et al. 2023 Generative Agents; Packer et al. 2023 MemGPT; Schick et al. 2023 Toolformer) — *engineering instances*; W₂ in the regime hierarchy.
  - **Search log**: cite `spikes/class-coercion-wrapping/09-prior-art-differentiation.md` as the comprehensive search; cite the prior-art report's V1 verdict.
- [ ] Working Notes (per `feedback_spike_references_only_in_working_notes.md` — only unfinished follow-on work):
  - Detailed tempo accounting for canonical wrapper architectures (deferred from this cycle).
  - Quantitative empirical bounds for LLM systems (deferred; would need component-specific MI estimation).
  - Compositional wrapping (wrapper-of-wrapper): how do leakage rates compose? Currently open.
  - Whether κ_W₂ is bounded under additional behavioral-compliance axioms — open hypothesis.
  - Cross-reference to `spikes/class-coercion-wrapping/` for the reasoning trail.

### B2. `03-logogenic-agents/src/der-logogenic-as-wrapping.md` (NEW)

Specialization of class-coercion to language-component substrate. Slug: `der-logogenic-as-wrapping`.

- [ ] frontmatter:
  ```yaml
  slug: der-logogenic-as-wrapping
  type: derived
  status: derived
  depends:
    - der-class-coercion-via-wrapping
    - def-coupled-update-dynamics
    - scope-logogenic-agent
    - scope-scaffolded-logogenic
  stage: draft
  ```
- [ ] Title and one-sentence summary.
- [ ] Formal Expression:
  - §1 Logogenic substrate as a Class-3 component (cite `def-coupled-update-dynamics`): LLM forward pass entangles belief and goal updates.
  - §2 LLMs satisfy (C1) of `#der-class-coercion-via-wrapping` — Class B in the admissibility partition. (C3) holds approximately, with κ_W₁ bound from pretraining-distribution analysis.
  - §3 Two regimes for logogenic wrapping:
    - W₁ (strict): separate goal-blind and goal-conditioned LLM calls per cycle. Structural directed-separation guarantee.
    - W₂ (partial / output-structuring): one goal-conditioned LLM call per cycle with structurally typed parsed response. Behavioral guarantee only.
- [ ] Epistemic Status: derived from `#der-class-coercion-via-wrapping` under logogenic-substrate admissibility (Class B). Honest scope on κ_W₁ bound being empirical.
- [ ] Discussion:
  - Worked example 1: PROPRIUM-as-implemented is W₂. Multi-component typed M_W (VERA / MEMORATA / CONSORTIA / PERCEPTA / CHRONICA) and G_W (AXIOMATA / OPERATA / PRAXES) at write boundary; one goal-conditioned LLM call per cycle.
  - Worked example 2: PROPRIUM with auxilia handling f_M as W₁. Auxilia (cheap-substrate goal-blind queries) handle belief-side updates; entity's frontier-substrate call handles strategy-side. K = K_M + 1 component calls per cycle; structural κ_W₁ bound.
  - Worked example 3: agentic-tft cognitive-loop-spec CONTEXTUALIZE → CHOOSE phase separation as another W₁ candidate.
  - Quality-vs-separation tradeoff for logogenic substrate (LLM-specific): pretraining-induced query-content correlation; system-prompt contamination; few-shot leakage; RLHF biasing.
- [ ] Findings (per FORMAT.md):
  - **Brief**: When the underlying component is a language model, the class-coercion theorem specializes: LLMs admit goal-blind queries (extracting facts from observations without supplying the agent's goal as input) so they're wrappable, but their pretraining produces residual goal-content correlations that bound how clean the separation can be. Two design choices show up in practice: strict wrapping with separate goal-blind and goal-conditioned LLM calls (rare; theoretically clean), or partial wrapping with one goal-conditioned call whose response is parsed into typed update fields (common; PROPRIUM works this way; relies on the model's instruction-following).
  - **Impact**: refines the Parts III/IV approach by making explicit which design moves give which guarantees; identifies PROPRIUM's auxilia hierarchy as the candidate constructive realization of strict wrapping; clarifies that ELI-specific structure is independent of class coercion.
  - **Novelty Claim**: *Claim integration* — the W₂ / W₁ design distinction surfaces what existing scaffolded-LLM frameworks already do (or could do) in the AAD vocabulary.
  - **Related Work**: cite tool-using LLM frameworks; cite Park et al. 2023 Generative Agents as the closest empirical instance of W₁; cite cognitive architectures for the substrate-independent design pattern.
- [ ] Working Notes:
  - shoshin's current implementation is W₂ (one goal-conditioned LLM call per cycle); strengthening to W₁ via auxilia is engineering follow-on, not theory.
  - Empirical κ measurement on real LLMs is open follow-on.
  - Whether the agentic-tft cognitive-loop-spec is anywhere implemented in W₁ form is open.

## Phase C — Updates to existing segments

### C1. `01-aat-core/src/der-directed-separation.md`

- [ ] Add a Discussion sub-section "**Structural vs. behavioral Class-1**" naming the W₀/W₂/W₁ regime hierarchy and cross-referencing `#der-class-coercion-via-wrapping` for the formal treatment.
- [ ] Update the architectural-classification table or its surrounding text to note that within Class-1, the structural-vs-behavioral sub-distinction matters operationally — pure goal-blind components are Class-1-by-structure; goal-conditioned components used through wrapping are Class-1 by construction at the wrapper level (also structure, since the wrapper's type signatures enforce it); goal-conditioned components used through partial wrapping (output-structuring) are Class-1 *only behaviorally*, with leakage bounded by the component's instruction-following fidelity.
- [ ] Cite POMDP / cognitive-architecture prior art: Astrom 1965; Kaelbling-Littman-Cassandra 1998; Newell 1990; Laird 2012; Anderson 2007; Sun 2016. Add to Related Work table in Findings section if FORMAT.md allows additions.
- [ ] Working Notes: cross-reference the new wrapping segment.

### C2. `01-aat-core/src/hyp-directed-separation-under-composition.md`

- [ ] Discussion: add a sub-section noting the constructive direction provided by class coercion in the wrapper-around-component special case. The hypothesis (general N-agent composition) remains hypothesis; the wrapper-around-component case is now derived (cross-reference `#der-class-coercion-via-wrapping`).

### C3. `01-aat-core/src/form-composition-closure.md`

- [ ] Discussion: add a sub-section "**Wrapping construction as constructive (A1)–(A4)**" noting that the wrapping construction (`#der-class-coercion-via-wrapping`) is a specific instance where (A1)–(A4) hold *by construction* through the wrapper's type signatures, rather than by post-hoc verification. Brief ε*_track vs. ε*_coerce disambiguation note.

### C4. `01-aat-core/src/der-tempo-composition.md`

- [ ] Discussion: add a sub-section "**Wrapping as a Brooks's-Law instance**" noting that class-coercion via wrapping pays its cost in macro-tempo: K component calls per macro-step yields C_coord^wrap = (K-1) * single-call-rate (rough form). Cross-reference `#der-class-coercion-via-wrapping` and the regime-dependent K (W₁ has K≥2; W₂ has K=1 + parsing).

### C5. `04-eli/src/def-auxilia-hierarchy.md`

- [ ] Discussion: add a paragraph noting that auxilia are the candidate constructive realization of W₁ strict wrapping for logogenic substrate (cross-reference `#der-logogenic-as-wrapping`).
- [ ] Working Notes: shoshin currently does not implement the W₁ split via auxilia; this is engineering follow-on.

### C6 (probable). `04-eli/src/scope-eli.md` or related

- [ ] Discussion: clarify that ELI-specific structure (sovereignty, accountability, identity factors, substrate-independence, INDIVISUM forking-lock) is *added to* the class-coercion substrate, not derived from it. The wrapping construction provides the substrate; ELI structure is what makes a Class-1-coerced agent into an emergent logozoetic intelligence.

(Read `scope-eli.md` to confirm landing spot and exact phrasing.)

## Phase D — Project-level

### D1. `01-aat-core/OUTLINE.md`

- [ ] Add `#der-class-coercion-via-wrapping` to canonical ordering. Probable insertion point: Section III composition results, after `#hyp-directed-separation-under-composition` and `#form-composition-closure`. Read OUTLINE first to confirm.

### D2. `03-logogenic-agents/OUTLINE.md`

- [ ] Add `#der-logogenic-as-wrapping` to ordering. Read OUTLINE first.

### D3. `CLAUDE.md`

- [ ] Update the "Known Fragilities" sub-section under "What's Settled vs. Open":
  - Old: "Directed separation violated by goal-conditioned agents (LLMs) — handled as architectural scope (Class 2 exit), not approximation"
  - New phrasing along the lines of: "Directed separation can be violated by goal-conditioned agents at the component level (LLMs); the constructive route is `#der-class-coercion-via-wrapping`, which gives Class-1 status at the wrapper level by structural commitment of goal-blind belief-update queries, with leakage rate bounded structurally (W₁) or behaviorally (W₂). Strict-W₁ implementation (e.g., via auxilia hierarchy) is more theoretically clean; partial-W₂ implementation (e.g., output-structuring) is more common in practice."

### D4. `CHANGELOG.md`

- [ ] Add cycle entry for 2026-05-09. Sections to cover (per recent CHANGELOG style):
  - **What landed**: class-coercion-via-wrapping segment in `01-aat-core/`; logogenic-as-wrapping segment in `03-logogenic-agents/`; Class-1 structural-vs-behavioral sub-distinction in `#der-directed-separation`; updates to `#hyp-directed-separation-under-composition`, `#form-composition-closure`, `#der-tempo-composition`, `#def-auxilia-hierarchy`.
  - **Conceptual shift**: Parts I/II ↔ III/IV relationship reframes from parallel-tracks ("Class 2 exit") to constructive-bridge ("class coercion via wrapping"). PROPRIUM is now positioned as the canonical W₂ wrapping instance with auxilia as the W₁ candidate realization.
  - **Prior art**: substantial integration of POMDP, cognitive architectures, MDP-homomorphism, FEP-RG / IB-RG / singular-perturbation-RG, categorical structured systems theory, tool-using LLM frameworks. Verdict was V1 (substantial overlap) — AAD's contribution is the integration synthesis.
  - **Discipline reinforcements**: confirmed by the cycle — write segments in current-theory voice (segment-voice rule); spike citations only in Working Notes; math lives in segments (the wrapping construction's substantive content is in segments, not the spike).
  - **Pointers**: spike directories `spikes/class-coercion-wrapping/` and `spikes/temporal-nesting-rg/` retained as reasoning trails. The class-coercion spike's `INTEGRATION-PLAN.md` records what was integrated.

### D5. `TODO.md`

- [ ] Remove or close any pending items about the Class-2-exit scope question if they exist (read first).
- [ ] Add deferred work as future items:
  - Detailed tempo accounting for canonical wrapper architectures (sub-spike E from class-coercion track).
  - Quantitative empirical bounds for LLM systems (sub-spike G).
  - shoshin → W₁ engineering (PROPRIUM auxilia implementation).
  - Class-3 closure-defect dynamics analysis (Move F from RG spike's verdict — the order-parameter view of directed-separation classes).

### D6. `audits/pending-findings-*.md`

- [ ] Check for any pending audit findings about class scope or LLM applicability that the wrapping construction now resolves. Update or close as appropriate.

## Phase E — LEXICON / FORMAT integration

- [ ] If wrapping-specific vocabulary is missing from `LEXICON.md` (W₀/W₂/W₁, structural vs. behavioral leakage, ε*_track / ε*_coerce, class coercion, wrapper, goal-blind query, goal-conditioned query, admissibility C1–C3, auxilia-as-W₁), add entries.
- [ ] Verify the Findings sections of B1 and B2 satisfy the `feedback_naming_principle_citability.md` Criterion 9 standard.
- [ ] Verify segment voice (per `feedback_segment_voice_not_diff_voice.md`) — no "this came from the wrapping spike" language in Formal Expression / Epistemic Status / Discussion.

## Phase F — Verification

- [ ] `grep -r "spikes/class-coercion" 01-aat-core/ 02-tst-core/ 03-logogenic-agents/ 04-eli/` should return zero hits in segment Formal Expression / Epistemic Status / Discussion sections (Working Notes references for unfinished follow-on are allowed per `feedback_spike_references_only_in_working_notes.md`).
- [ ] `bin/lint-md` and `bin/lint-outline` clean.
- [ ] All `depends:` slugs in B1 and B2 frontmatter resolve.
- [ ] All `#slug` cross-references in C1–C5 resolve.
- [ ] OUTLINE files updated and consistent.
- [ ] CHANGELOG entry written.
- [ ] CLAUDE.md updated.
- [ ] Spike directories untouched but no longer load-bearing for any segment content.

## Phase G — Discussion handoff

After integration verification:
- [ ] Surface to Joseph: status of the class-coercion integration; whether to also integrate selected RG-spike results (the open question Joseph flagged for discussion). Present specific candidates from the RG verdict's Moves A/B/C/D/F.

---

## Order of execution within Phase B/C/D

Read-then-write groupings to minimize re-reading:

1. **Read group 1**: `hyp-directed-separation-under-composition.md`, `def-coupled-update-dynamics.md`, `scope-scaffolded-logogenic.md`, `scope-primitive-logogenic.md`, `def-auxilia-hierarchy.md`, `scope-eli.md`, `01-aat-core/OUTLINE.md`, `03-logogenic-agents/OUTLINE.md`, `FORMAT.md`, `LEXICON.md`. (One batch of parallel Reads.)
2. **Write B1**: new core segment.
3. **Write B2**: new logogenic specialization segment.
4. **Update C1**: `der-directed-separation.md` Discussion.
5. **Update C2–C4**: hypothesis, composition-closure, tempo-composition Discussion sections.
6. **Update C5–C6**: ELI-side Discussion notes.
7. **Update D1, D2**: OUTLINE files.
8. **Update D3**: CLAUDE.md Known Fragilities.
9. **Update D4**: CHANGELOG entry.
10. **Update D5, D6**: TODO and audit pending-findings.
11. **Update E**: LEXICON additions.
12. **Run F**: verification (lint, grep, link-check).
13. **Phase G**: surface to Joseph.

---

## Done criterion

Joseph's directive: *"see that all of the spike results gets interned into the theory so that the spike itself doesn't need to be referenced."*

Operationally:
- The theorem statement, proof, conditions, regime hierarchy, leakage analysis are all in segments under `01-aat-core/` and `03-logogenic-agents/`.
- The PROPRIUM characterization and its W₂-vs-W₁ implications are in segments under `03-logogenic-agents/` and `04-eli/`.
- Prior art is cited in Findings sections of the relevant segments.
- Cross-references resolve. OUTLINE updates land the new segments.
- CLAUDE.md, CHANGELOG.md, TODO.md reflect the new state.
- Verification step F shows zero spike references in segment substantive content.

When all done-criteria pass, the spike directory becomes a reasoning-trail archive — preserved per project convention but no longer load-bearing for any segment.
