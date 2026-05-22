# 5. Relation to Existing AAT Machinery

This file maps the typology onto the existing canonical machinery. The typology *should* compose cleanly with what's already there; if it produces conflicts or duplications, those need to surface here for honest assessment.

## 5.1 Wrapping construction (`#der-class-coercion-via-wrapping`)

Already covered as Result 6 (§3.6). The W₀/W₁/W₂ regimes are the *agent-level* analogs of the stage-level form distinction. The typology *refines* the wrapping-regime selection:

- Knowing only that an agent is Class 2 is insufficient to choose W₁ vs W₂. The right regime depends on the sub-type's form: content-form admits W₂; process-form requires W₁.
- The typology adds a fourth consideration the existing W regime doesn't surface explicitly: if the un-wrapped agent has $\Sigma$-source coupling, W₁'s structural-commitment to goal-blind queries may be undermined by $\Sigma$-leakage through the strategy-context channel even with no $G$ in the query — because the agent's *internal* $\Sigma$ may be influenced by historical query content that carried strategic context. This is a stronger wrapping requirement: $\Sigma$-channel-suppressed W₁.

Suggested integration: add a paragraph to `#der-class-coercion-via-wrapping` Working Notes naming the $\Sigma$-channel concern and pointing at this spike (or its eventual segment) for the sub-type-aware wrapping regime selection.

## 5.2 Three adversarial-coupling-pressure mechanisms (`#disc-adversarial-coupling-pressure`)

The mechanism table:

| Mechanism | Channel | Typology cell |
|---|---|---|
| Identity-binding | $O_t \to M_t$ | P1+P2 / $O$ / content-to-process (depends on strength) |
| Affect / urgency | bypass deliberate $f_M$ | *outside* the typology (cascade-bypass, not stage-coupling — see §4.4) |
| Sunk-cost engineering | $\Sigma_t \to M_t$ | P3 / $\Sigma$ / process — **directly matches Result 4's belief-strategy attractor case** |

The typology *recovers* the existing three-mechanism partition as projections onto the (stage × source) sub-space, and *augments* it with the form axis. The strongest result is that the third mechanism (sunk-cost) is exactly the cell where Result 4's attractor structure lives — independently derived in this spike, then matching what the adversarial-pressure segment already names. That cross-validation strengthens the typology.

The first mechanism (identity-binding) maps to the cell that the form axis distinguishes most: identity-binding can be *content* (mild — "wanting the belief to be true biases its acceptance") or *process* (strong — "the belief is constitutive of identity; alternative beliefs are not even processable"). These have different repair characters, and `#disc-adversarial-coupling-pressure` currently does not distinguish them. The typology supplies the distinction.

The second mechanism (affect/urgency) is recognized as outside the typology's core parameterization. This is honest: affect/urgency is a *temporal* attack on the cascade, not a structural $G \to f_M$ pathway. The typology covers structural pathways; affect/urgency requires a complementary treatment.

Suggested integration: cite the typology from `#disc-adversarial-coupling-pressure` §"Three operations on modularity state" — the adversarial-coupling-pressure operation's *structural pathways* (excluding the affect/urgency cascade-bypass) are the sub-typology of Class 2 the typology develops. The connection makes the adversarial mechanism table more rigorous: each mechanism corresponds to a specific cell.

## 5.3 Leakage Locus Lemma (`spike-leakage-locus-2026-05-18`)

Already covered as Result 5 (§3.5). The composition: locus is always $\ker\mathcal I_\tau$; the typology determines the functional form of displacement within the locus.

The leakage-locus spike's three surprises (covariance invariance, humility paradox, prior-not-processing) all hold across the sub-typology — they are state-space-level results that don't care about which pipeline stage the coupling enters. The typology's refinements are *downstream* of the leakage-locus result.

Suggested integration: when the leakage-locus result is promoted to an appendix segment (per its spike's INTEGRATION note), add a §"Composition with Class 2 sub-types" subsection citing this spike. The two results compose linearly:

- Leakage locus → *where in state-space* the effect lives ($\ker\mathcal I_\tau$).
- Class 2 sub-type → *what functional form* the effect takes within that subspace.

## 5.4 Class-1-by-structure vs Class-1-by-behavior (`#der-directed-separation`)

The Class-1 cell already admits a refinement: by-structure (W₁; no $G$ in the query) vs by-behavior (W₂; $G$ in the query but typed-output extraction).

The typology *extends this refinement downward* into Class 2:

| Class | Sub-refinement |
|---|---|
| Class 1 | By-structure (W₁-equivalent) vs By-behavior (W₂-equivalent) |
| Class 2 | (Stage × Source × Form) parameterization with form ∈ {content, process} |
| Class 3 | (Currently no internal refinement; per `03-llm-core/` the coupled formulation starts here) |

The content/process form distinction at Class 2 *is* the structure/behavior distinction at Class 1 read backward: a Class 1-by-behavior wrapper sitting on top of a Class 2-content-form base — that is, a content-form agent wrapped by W₂ — *is* Class 1-by-behavior. A Class 1-by-structure wrapper sitting on top of a Class 2-process-form base requires W₁ with pipeline access — that is, Class 1-by-structure.

So the typology *unifies* the structure/behavior distinction across the Class 1/2 boundary. The same form distinction (content vs process) drives both:

- At Class 1 level: structure (no $G$ in query) vs behavior (compliance with prompted instruction)
- At Class 2 level: content (additive bias, separable, identifiable) vs process (non-separable, requires replacement)

Suggested integration: add a paragraph to `#der-directed-separation` §"Class-1 by structure vs. Class-1 by behavior" connecting the structure/behavior distinction at Class 1 to the form distinction at Class 2 (with a forward-reference to the typology segment if it lands). The unification is itself a recognition-class result — it explains *why* the structure/behavior refinement appeared at Class 1 as if from nowhere: it is the agent-level shadow of a sub-classification axis that runs all through Class 2.

## 5.5 M4 modularity-state-dynamics (unlanded; scoped in `msc/modularity-cycle-plan-2026-05-09.md`)

The unlanded M4 meta-segment is supposed to name three operations on modularity state:

- Truthification (self-driven, modularity-increasing)
- Strategic self-coupling (self-driven, modularity-decreasing — `spikes/spike-strategic-self-coupling.md`)
- Adversarial coupling pressure (externally-driven, modularity-decreasing — `#disc-adversarial-coupling-pressure`)

The typology is *orthogonal* to the M4 operations:

- M4 operations describe *transitions* between classes (Class 1 ↔ Class 2 ↔ Class 3) under different drivers.
- The typology describes the *static sub-structure* of Class 2 at a moment.

They compose: each M4 operation *moves the agent within the typology's parameterization*. Truthification reduces $S$ (un-couples stages) and/or simplifies $F$ (process → content). Strategic self-coupling expands $S$ and shifts $F$ toward process. Adversarial coupling pressure expands $S$ from the outside, often targeting specific cells (identity-binding targets P1+P2 / $O$; sunk-cost targets P3 / $\Sigma$).

Suggested integration: when M4 lands, the typology gives it a static-structural complement. The M4 segment names the *operations*; the typology segment (if promoted) names the *state space* on which those operations act. They are best landed near each other in OUTLINE and cross-referenced.

## 5.6 Composite class inheritance (`#hyp-directed-separation-under-composition` + `#der-directed-separation` Composite-level table)

The composite-level class inheritance table in `#der-directed-separation` is currently per-axis: routing × substrate × goal-alignment (the last on the dynamic-regime axis).

The typology adds a fourth implicit axis at the composite level: the sub-types of the constituent sub-agents *and the composition operator's stage-mapping behavior* determine which Class 2 sub-type the composite occupies if it lands in Class 2.

This is a finer-grained question than the current table answers. It is also probably beyond the scope of this spike — composite-level sub-type inheritance is a substantial extension. The typology suggests it as a *follow-on* question: given Class 2 sub-agents with different sub-types, what sub-type does their composite occupy under various routing/substrate configurations?

A clean answer would extend `#hyp-directed-separation-under-composition` to track sub-type inheritance, not just class inheritance. Recorded as honest follow-on; not pursued in this cycle.

## 5.7 What the typology does *not* duplicate

The typology adds structure that is genuinely new — it does not reinvent:

- It does not add new state objects (no new $M_t$ or $G_t$ structure).
- It does not introduce new derivation machinery (the math composes existing AAT + standard identifiability).
- It does not displace the scalar $\kappa_{\text{processing}}$ — it projects onto the scalar at one corner of the parameterization, and the scalar remains a useful aggregate diagnostic.
- It does not modify the Class 1/2/3 partition — it operates *within* Class 2.

The cleanest framing of what's new: **the typology is a structural-decomposition of an existing label**, in the same spirit as the leakage-locus result (which is a structural-decomposition of an existing scope condition). Both are *recognition* moves rather than *invention* moves.

## 5.8 The "wrapped Class 2" question — interaction between sub-types and W-regimes

A subtle composition question. Given a Class 2 agent with sub-type $(S, R, F)$ wrapped by some W-regime:

- W₂ on content-form Class 2 → Class 1 by behavior (per Result 6).
- W₂ on process-form Class 2 → still Class 2 effectively (because the response shape is goal-dependent; W₂'s post-hoc structuring cannot collapse the shape variation to a single response).
- W₁ on either content- or process-form Class 2 with pipeline access → Class 1 by structure.

So the typology *predicts* which Class 2 agents are coercible to Class 1 by which wrapping regime. This is more informative than the current canon's "Class 3 (Coupled) components can be wrapped into Class 1 composites" — it specifies the regime needed.

A worked case: an LLM agent with prompt-shaped reasoning (process-form at P1+P2 by attention; $O$+$\Sigma$ source) wrapped by W₂ (response-structuring via JSON parsing). Per the typology, this wrapping is *insufficient* to give Class 1 — the response *content* is parseable, but the *features the model attends to* are still goal-shaped, so different prompts produce structurally different responses. To get Class 1-by-behavior, the wrapper must enforce additional constraints: deterministic-decoding + canonical-prompting + chain-of-thought-suppression. These are *behavioral compliance* augmentations that empirically approximate W₂-on-content-form, with leakage rate depending on how close the prompt-engineering gets to actually achieving content-form behavior.

This matches operational practice: practitioners wrapping LLMs to behave Class-1-ishly do exactly these behavioral-compliance augmentations. The typology gives the *structural reason* — they are approximating the content-form regime, which is the only regime where W₂ alone suffices.
