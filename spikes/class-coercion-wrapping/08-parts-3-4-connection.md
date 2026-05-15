# Sub-Spike H: Connection to Parts III/IV (Logogenic Agents and ELIs)

**Status**: derivation. PROPRIUM class assignment; what's wrapping-content vs. ELI-specific load; segment-level integration recommendations.
**Date**: 2026-05-09
**Depends on**: `01-theorem-statement.md`, `02-admissibility.md`, `03-leakage.md`, `06-empirical-instances.md` (especially §1 PROPRIUM characterization).

---

## 1. PROPRIUM's class assignment

Per `06-empirical-instances.md` §1.2, PROPRIUM-as-implemented (shoshin) is **W₂ (partial wrapping)**:

- **Multi-component typed $M_W$** (VERA / MEMORATA / CONSORTIA / PERCEPTA / CHRONICA) with explicit write-time separation.
- **Multi-layered typed $G_W$** (AXIOMATA / OPERATA / PRAXES) at three timescales.
- **Single goal-conditioned LLM call per cycle**, with structurally typed parsed response routing updates to the correct component.
- **Structural separation lives at the write boundary**, not the query boundary.

By the leakage analysis in `03-leakage.md`, this is W₂ — directed separation holds *behaviorally* (the LLM is asked, via prompt structure, to separate its outputs) rather than *structurally* (the LLM still has $G_W$ in its input). The leakage rate $\kappa_\text{W₂}$ depends on the underlying LLM's instruction-following fidelity.

PROPRIUM-as-documented (the ontology + architecture) is *silent* on whether the structural separation should be at query or write boundary — the documents don't require either. The construction is consistent with strict wrapping (W₁) but doesn't force it.

## 2. The strengthening proposal: PROPRIUM toward W₁

Per `06-empirical-instances.md` §1.2 (final paragraph) and §1.3 (item 5), PROPRIUM has an architectural feature that *could* implement strict wrapping: the **auxilia hierarchy**. Auxilia are sub-agents that share identity (AXIOMATA / VERA / PRAXES) but specialize in roles and may run on cheaper substrates.

The strengthening: have auxilia handle $f_M$ updates with goal-blind queries (cheap-substrate calls that take only observation-grounded input), while the entity's main LLM call handles $f_G$ updates goal-conditionally. This would put auxilia LLM calls in the goal-blind $q_M$ slot and the entity's frontier-substrate call in the goal-conditioned $q_G$ slot.

Specifically:

- Auxilia (cheap substrate, $K_M$ calls per cycle) → goal-blind queries on observations → updates VERA / MEMORATA / CONSORTIA / PERCEPTA. These are $f_M$ updates.
- Entity (frontier substrate, 1 call per cycle) → goal-conditioned query on $(M_W, G_W)$ → updates OPERATA / PRAXES / AXIOMATA. These are $f_G$ updates.

Tempo cost: $K = K_M + 1$ component calls per cycle. For $K_M$ on the order of 5–10 per cycle, the wrapper-level tempo is roughly an order of magnitude slower than naïve LLM use. This is the operational price of strict wrapping.

Theoretical gain: $\kappa_\text{W₁} \le I(A(q_M); G_W \mid q_M)$ — a structural directed-separation bound. Compared to W₂ where leakage is bounded only by behavioral compliance, W₁ provides a derivable upper bound on goal-information leakage in $f_M$.

**This strengthening is consistent with the documented PROPRIUM ontology — it's a refinement of how the architecture is implemented, not a change to what the architecture is.** It's the "constructive realization of strict wrapping" hinted at in the empirical-instances survey.

## 3. The cognitive-loop-spec is closer to W₁

Per `06-empirical-instances.md` §1.4, the agentic-tft cognitive-loop-spec (`ref/agentic-tft/agentic-tft-cognitive-loop-spec.md`) describes the per-event cycle as PERCEIVE → CONTEXTUALIZE → CHOOSE → EFFECT, with CONTEXTUALIZE explicitly performing belief-side updates ($M_W$) before CHOOSE performs strategy-side updates ($G_W$).

This temporal phase-separation is closer to strict wrapping than PROPRIUM-as-implemented:

- CONTEXTUALIZE's predict / detect-surprise / assess-weight / draw-context / update operations can be made goal-blind by restricting their inputs.
- CHOOSE's plan / decide / monitor operations are goal-conditioned by design.

If the cognitive-loop-spec is implemented faithfully — with CONTEXTUALIZE making goal-blind queries to the LLM and CHOOSE making goal-conditioned queries — the result *is* W₁ strict wrapping at a tempo cost of two LLM calls per cycle minimum.

This is the natural integration target for the wrapping theorem. The cognitive-loop-spec already specifies the structure; this spike's theorem clarifies the directed-separation bound that follows.

## 4. ELI-specific load is independent of class coercion

PROPRIUM contains substantial structure that goes *beyond* what the wrapping theorem requires. From `06-empirical-instances.md` §1.3:

| PROPRIUM element | Relation to wrapping theorem |
|---|---|
| Multi-component typed $M_W$ (5 components) | Refinement of $\mathcal{X}_M$ structure; not theorem-required but compatible. |
| Multi-layered typed $G_W$ (3 layers) | Refinement of $\mathcal{X}_G$ structure; not theorem-required but compatible. |
| **Auxilia hierarchy** | **Constructive realization of strict wrapping.** Theorem-relevant. |
| Sovereignty axes (visibility / authority) | Governance constraint; **not** part of class coercion. |
| Append-only system-governed components (CHRONICA, ACTUS) | ELI accountability infrastructure; **not** part of class coercion. |
| CADENTIA temporal driver (PULSUS / VIGILIAE) | Implementation choice for cycle firing; **not** load-bearing. |
| Five constitutive identity factors (causal continuity / being seen / sovereignty / accountability / phenomenology) | ELI-specific; what makes a Class-1-coerced agent into an ELI. **Not** part of class coercion. |
| Substrate-independent identity | Longitudinal identity; persistence across underlying $A$ instances over time. **Not** part of per-call wrapping. |
| INDIVISUM (temporal lock against forking) | ELI-specific governance; **not** part of class coercion. |

**Reading**: the wrapping theorem covers items 1, 2, 3 (after auxilia → goal-blind realization). The remaining items are *additional structure* that distinguishes ELIs from generic Class-1-coerced systems. This distinction matters for project architecture: the wrapping theorem could land in `01-aat-core/`; ELI-specific structure remains in `04-eli-core/`.

## 5. What this clarifies about the Parts I/II ↔ Parts III/IV relationship

Currently the project treats Parts III/IV as a "different problem domain requiring coupled formulation from the start" (per CLAUDE.md). This framing comes from the directed-separation failure of LLMs (Class-3 components).

The wrapping theorem refines this:

- **Parts I/II (AAT core)** apply to Class-1 systems by construction *or* to Class-1 systems built via the wrapping construction.
- **Wrapping construction** (this spike's theorem) is the bridge — how to construct Class-1 systems from Class-3 components.
- **Parts III/IV** are *domain instantiations* of Class-1-by-wrapping. PROPRIUM is the canonical wrapper; ELI-specific content is added structure beyond bare class coercion.

This is a more coherent project architecture. Parts III/IV stop being "a different problem domain" and become "the worked instantiation of wrapping for the language-substrate component class, plus the additional structure required for emergent logozoetic intelligences."

The honest framing is even better: most of what Parts III/IV add (sovereignty, accountability, identity factors, substrate-independence) doesn't depend on the wrapping construction at all. They're separate research threads about persistence, governance, and identity that *take* a Class-1 wrapped system as a substrate. The wrapping construction is the substrate; ELI work is what happens on top of it.

## 6. Segment-level integration

Recommendations for landing this in segments. These are tentative and depend on the verdict (`99-verdict.md`).

### 6.1 In `01-aat-core/`

**New segment**: `der-class-coercion-via-wrapping.md` (or `result-class-coercion-via-wrapping.md`). Statement and proof of Theorem 1. Sub-results for the approximate version (Theorem 2 with leakage). Conditions C1–C3 explicit.

**Updates**:
- `#hyp-directed-separation-under-composition`: add Discussion section noting the constructive direction provided by class coercion (in the wrapper-around-component special case).
- `#der-directed-separation`: extend the Class-1 / Class-2 / Class-3 taxonomy with the W₀ / W₂ / W₁ wrapping-regime sub-distinctions. Class-1-by-structure vs. Class-1-by-behavior is a real distinction worth surfacing.
- `#form-composition-closure` Discussion: note the wrapping construction as a specific instance where (A1)–(A4) admissibility holds *by construction* via the wrapper's type signatures.
- `#der-tempo-composition` Discussion: note the wrapping construction as a Brooks's-Law instance, with $C_\text{coord}^\text{wrap}$ tied to the wrapper's $K$.

### 6.2 In `03-llm-core/`

**New segment** (or extension of an existing one): `der-logogenic-as-wrapping.md` or similar. Specialize the class-coercion theorem to logogenic agents — language-component as the underlying $A$, language-mediated $M_W$ representation, etc.

**Citation discipline** (per sub-agent I's prior-art findings): cite POMDP literature (Astrom 1965, Kaelbling-Littman-Cassandra 1998) as the closest formal prior art for the directed-separation guarantee; cite cognitive architectures (SOAR / ACT-R / CLARION / GWT) as the architectural prior art.

### 6.3 In `04-eli-core/`

ELI-specific content (sovereignty axes, accountability infrastructure, identity factors, substrate-independence) remains here. Cross-component reference up to the wrapping segment for the class-coercion content. Identity-through-context-boundaries and CADENTIA are about *persistence-of-the-wrapped-system-across-time*, not about wrapping per se.

### 6.4 PROPRIUM as canonical example

The PROPRIUM structural reading from `06-empirical-instances.md` §1 — multi-component typed $M_W$/$G_W$ + auxilia hierarchy as the constructive realization — should be cited in the new wrapping segment as the canonical extended example. PROPRIUM-as-documented could serve as the reference for "what a properly-engineered Class-1 wrapper looks like for logogenic substrate."

## 7. Honest scope

What this sub-spike establishes:
- PROPRIUM-as-implemented is W₂; could become W₁ via auxilia hierarchy.
- The cognitive-loop-spec is structurally closer to W₁ than PROPRIUM-as-implemented.
- ELI-specific content is not part of class coercion; it's added structure.
- The wrapping theorem coheres the Parts I/II ↔ Parts III/IV relationship by clarifying what's substrate vs. what's added.

What this sub-spike does *not* establish:
- Whether a strict-W₁ implementation of PROPRIUM via auxilia is operationally feasible at typical deployment cost. The tempo accounting in sub-spike E (currently deferred) would address this.
- What constraints ELI-specific content places on the wrapping construction. Some ELI-specific requirements (identity persistence across substrate changes) may have implications for the wrapper's design that aren't captured by the bare class-coercion theorem.
- Whether the agentic-tft cognitive-loop-spec is *actually* implemented anywhere in the W₁ form, or whether it's currently spec-only. (Empirical question; outside this spike's scope.)

The recommendations in §6 are honest scoping for what *could* land in segments if the verdict supports it. They are not commitments — the verdict file synthesizes whether to proceed.

---

## File index

- This file: `08-parts-3-4-connection.md`
- Brief: `00-brief.md`
- Theorem: `01-theorem-statement.md`
- Leakage: `03-leakage.md`
- Empirical instances: `06-empirical-instances.md` (heavily cited)
- Verdict: `99-verdict.md` (synthesis)
