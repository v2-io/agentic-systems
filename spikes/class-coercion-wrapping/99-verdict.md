# Class-Coercion Spike: Verdict and Synthesis

**Status**: complete (sub-spikes E, G deferred as future work; their absence does not block the verdict).
**Date**: 2026-05-09
**Inputs**: `00-brief.md`, `01-theorem-statement.md`, `02-admissibility.md`, `03-leakage.md`, `04-epsilon-semantics.md`, `06-empirical-instances.md` (delegated), `08-parts-3-4-connection.md`, `09-prior-art-differentiation.md` (delegated).

**Posture** (per Joseph's framing correction during the spike): truth-discovery and theory-strengthening, not novelty-claim or paper-extraction. The verdict reads accordingly — the wrapping construction is integration content within ASF's prior-art-integration discipline.

---

## 1. The question this spike addressed

Joseph asked: can we constructively narrow the scope of `#der-directed-separation` to just the separated-goal-update-causal class by wrapping any Class-2 / Class-3 component into a higher-level Class-1 composition? More concretely: is what Parts III/IV do for logogenic agents (with PROPRIUM as the canonical scaffold) something that we can do more generally?

## 2. The honest answer

**Yes, with significant qualifications.** Here is the structure of what was found.

### 2.1 The wrapping move works as a theorem

Theorems 1 and 2 in `01-theorem-statement.md` hold under stated conditions. Specifically:

- The wrapper $W$ has explicit external state $X_W = (M_W, G_W)$ with type-level structural separation: $f_M$ has no $G_W$ argument; $q_M$ has no $G_W$ argument.
- Under conditions (C1) admissibility, (C2) stationary component conditional, (C3) no implicit goal-inference, directed separation holds at the wrapper level *exactly*.
- Under (C3) replaced by KL-leakage bound $\kappa$, directed separation holds *approximately*, with KL-divergence on $M_W$ updates bounded by $\kappa$ via the data-processing inequality.

(A1) of `#form-composition-closure` follows by construction. (A2)–(A4) are wrapper-design constraints (D-A2/D-A3/D-A4) that hold for Tier-1 belief-update maps (Bayesian on exponential families, gradient on strongly convex losses, linear-PD with bounded gain). The wrapper inherits AAD's existing persistence template (`#result-sector-persistence-template`) and Brooks's-Law tempo accounting (`#der-tempo-composition`) at the wrapper level.

### 2.2 The wrapping move is mostly rediscovery

Per `09-prior-art-differentiation.md` (V1 verdict — substantial overlap):

- **POMDP / Bayesian decision theory** (Astrom 1965 onward) does the same separation move by construction. Bayesian belief-update is goal-blind by design; the wrapping construction is reformalization in AAD vocabulary.
- **Cognitive architectures** (SOAR, ACT-R, CLARION, GWT — Newell 1990 onward) have done modular agent design with separated belief / goal / action state for 40+ years.

AAD's contribution within this neighborhood is *integration*: bringing the wrapping construction into the AAD framework with sector-Lyapunov persistence machinery, Brooks's-Law tempo accounting, the Class-1/2/3 directed-separation classification, and the LLM-specific (C1)–(C3) admissibility/leakage conditions.

### 2.3 PROPRIUM is partial wrapping (W₂), not strict wrapping (W₁)

Per `06-empirical-instances.md` §1.2: PROPRIUM-as-implemented (shoshin) is one goal-conditioned LLM call per cycle with structurally typed parsed response. The structural separation lives at the *write boundary* (typed update fields), not at the *query boundary* (one goal-conditioned input).

This makes PROPRIUM **W₂** in the leakage hierarchy of `03-leakage.md`: directed separation holds *behaviorally* (the LLM is asked, via prompt structure, to separate its outputs), not *structurally* (the LLM still sees $G_W$). The leakage rate $\kappa_\text{W₂}$ is bounded only by the LLM's instruction-following fidelity — a behavioral, not theoretical, bound.

PROPRIUM's auxilia hierarchy (`06-empirical-instances.md` §1.3 item 5) is a candidate constructive realization of strict wrapping (W₁): auxilia handle $f_M$ updates with goal-blind queries on cheap substrate; the entity's main LLM call handles $f_G$ goal-conditionally. **This is a strengthening of PROPRIUM that's consistent with the documented architecture but not yet implemented.**

### 2.4 The leakage hierarchy is the AAD-distinctive contribution

The W₀ / W₂ / W₁ hierarchy in `03-leakage.md` is a real distinction that the prior literature does not surface:

| Regime | Construction | Leakage bound | Practical example |
|---|---|---|---|
| **W₀** (no wrapping) | Raw Class-3 component | At component's max goal-conditioning sensitivity | Direct LLM use without scaffold |
| **W₂** (partial wrapping) | One goal-conditioned call, parsed response | Behavioral — bounded by instruction-following fidelity; **no structural bound** | PROPRIUM/shoshin, ReAct, Reflexion, BabyAGI, AutoGPT |
| **W₁** (strict wrapping) | Separate goal-blind and goal-conditioned calls | Structural — bounded by $I(A(q_M); G_W \mid q_M)$ in pretraining distribution | Generative Agents (Park 2023) memory step; cognitive-loop-spec CONTEXTUALIZE→CHOOSE if implemented |

This hierarchy connects directly to AAD's architecture-class taxonomy: W₁ is *Class-1 by structure*, W₂ is *Class-1 by behavior*, W₀ is *Class-3*. The structure-vs-behavior distinction within Class-1 is a refinement of `#der-directed-separation` that this spike surfaces.

### 2.5 ELI-specific load is independent of class coercion

Per `08-parts-3-4-connection.md` §4 + `06-empirical-instances.md` §1.3: PROPRIUM contains substantial ELI-specific structure (sovereignty axes, append-only governance, identity factors, substrate-independence, CADENTIA temporal driver, INDIVISUM forking-lock) that is **not** part of class coercion. These are added structures that distinguish ELIs from generic Class-1-coerced systems.

This clarifies the project architecture: Parts III/IV stop being "a different problem domain" and become "the worked instantiation of class coercion for the language-substrate component class, plus the additional structure required for emergent logozoetic intelligences."

## 3. Theory-strengthening achieved

### 3.1 `#hyp-directed-separation-under-composition` promoted

The hypothesis is currently descriptive — when does directed separation hold under composition? The wrapping construction provides a *constructive* answer for the wrapper-around-component special case: directed separation holds whenever the wrapper's type signatures are respected and (C1)–(C3) hold. This promotes the hypothesis to a derived result for that special case, preserving its hypothesis status for the general N-agent composition question.

### 3.2 `#der-directed-separation` taxonomy refined

The Class-1 / Class-2 / Class-3 taxonomy gains a meaningful sub-distinction: within Class-1, *by-structure* (W₁) vs. *by-behavior* (W₂). This is operationally important — these have different leakage bounds derivable in different ways.

### 3.3 The "Class 2 exit" framing in CLAUDE.md is resolved

CLAUDE.md currently says: *"Directed separation violated by goal-conditioned agents (LLMs) — handled as architectural scope (Class 2 exit), not approximation."*

The wrapping construction promotes this from "scope exit" to "constructive route through": Class-3 components are scope-in *for the wrapper construction*, not scope-out. The cost is paid in tempo (Brooks's-Law form) and a measurable leakage residual. This is a more honest and more useful framing.

### 3.4 The Parts I/II ↔ Parts III/IV relationship clarifies

Currently treated as separate research threads requiring "coupled formulation from the start." After class coercion: Parts I/II are the AAD core; the wrapping construction is the bridge; Parts III/IV are domain instantiation + ELI-specific structure. This is a coherent architecture rather than a parallel-tracks one.

## 4. What lands as new AAD content

### 4.1 New segment in `01-aat-core/src/`

Tentative slug: `der-class-coercion-via-wrapping.md`. Content:
- Setup (§1 of `01-theorem-statement.md`).
- Conditions C1–C3 (§2 of theorem-statement; §3 of admissibility for class characterization).
- Theorem 1 (exact form) and proof (§4 of theorem-statement).
- Theorem 2 (approximate form) and proof (§5 of theorem-statement).
- Discussion: relationship to `#hyp-directed-separation-under-composition`; W₀/W₂/W₁ hierarchy; integration with persistence template and tempo composition.
- Findings: brief in plain language; impact; novelty claim (per AAD's discipline: *integration only*, citing POMDP and cognitive architectures generously).
- Search log: cite `spikes/class-coercion-wrapping/09-prior-art-differentiation.md` for the prior-art landscape.

### 4.2 Updates to existing segments

- **`#der-directed-separation`**: extend Discussion with the W₀/W₂/W₁ refinement of Class-1. Add the structure-vs-behavior distinction.
- **`#hyp-directed-separation-under-composition`**: cite the constructive class-coercion result as a derived special case.
- **`#form-composition-closure`** Discussion: note the wrapping construction as a specific instance where (A1)–(A4) admissibility holds *by construction* via wrapper type signatures.
- **`#der-tempo-composition`** Discussion: note the wrapping construction as a Brooks's-Law instance with $C_\text{coord}^\text{wrap}$ tied to $K$ (component calls per macro-step).

### 4.3 New segment in `03-logogenic-agents/src/`

Tentative slug: `der-logogenic-as-wrapping.md`. Specialize the class-coercion theorem to logogenic substrate: language-component as $A$, language-mediated $M_W$ representation, leakage analysis specific to LLM pretraining.

### 4.4 Cross-component references in `04-eli/src/`

ELI-specific segments cite the wrapping construction in `01-aat-core/` for class-coercion content. ELI-specific structure (sovereignty, accountability, identity factors, substrate-independence) remains in `04-eli/`.

### 4.5 Citation discipline (per `09-prior-art-differentiation.md`)

Cite generously:
- POMDP / Bayesian decision theory: Astrom 1965, Kaelbling-Littman-Cassandra 1998 (closest formal prior art for goal-blind belief-update).
- Cognitive architectures: Laird 2012 (SOAR), Anderson 2007 (ACT-R), Sun 2016 (CLARION), Baars 1988 / Dehaene 2014 (Global Workspace).
- MDP-homomorphism: already cited in `Novelty_defense_and_integration.md`; reuse.
- Categorical structured systems theory: Smithe 2024, Capucci et al. 2022 — adopt the lens framing directly.
- Tool-using LLM frameworks (engineering instances): ReAct, Toolformer, MemGPT, Generative Agents, etc. Cite as practical instantiations, not theoretical contributions.

## 5. What was deferred and why

**Sub-spike E (tempo cost detailed accounting).** The tempo cost of wrapping is real and follows from `#der-tempo-composition`. The detailed accounting for canonical wrapper architectures (computing $C_\text{coord}^\text{wrap}$ for ReAct-shape, PROPRIUM-shape, etc.) was deferred. The verdict-level finding that *wrapping pays in tempo* is honest without the detailed accounting; specific quantitative predictions belong in follow-up work if needed for downstream applications.

**Sub-spike G (quantitative bounds for LLM systems).** Specific predictions — slowdown vs. wrapper depth, leakage rate vs. context-window goal-content — require empirical work outside this spike's scope. The bounds derived in `03-leakage.md` ($\kappa_\text{W₁} \le I(A(q_M); G_W \mid q_M)$ and the unbounded-by-structure $\kappa_\text{W₂}$) are theoretical; empirical instantiation is follow-up. Joseph's note: *"some good paper-sized findings may fall out"* — this is the natural extension if it does, but is not load-bearing for the spike's theory verdict.

These deferrals do not block the verdict because:
- The theorem holds without them.
- The W₀/W₂/W₁ hierarchy distinguishes the regimes structurally.
- Segment-landing recommendations are clear from what was completed.
- Specific empirical work is its own research direction — better as standalone follow-up than rushed inside this spike.

## 6. Cross-checks against project disciplines

- **Strengthen-before-softening**. The strict wrapping move is the *strengthening* of what most practical systems (including PROPRIUM) currently do. The leakage analysis articulates what's gained by moving from W₂ to W₁ and what's lost in tempo. The verdict honors strengthening — recommending the W₁ direction for PROPRIUM (via auxilia) where feasible — while honestly characterizing W₂ as the dominant practical pattern.

- **Prior-art integration discipline**. *"AAD's contribution is integration, not invention."* The verdict adopts POMDP and cognitive-architecture prior art generously per V1 of the differentiation report. The wrapping move itself is not claimed as AAD-novel; the integration with sector-Lyapunov + Brooks's-Law + class taxonomy is the contribution.

- **Honest epistemic labels**. Theorem 1 and Theorem 2 are *derived*; (C3) is *conditional*; W₀/W₂/W₁ is *formulation*; PROPRIUM-as-W₂ characterization is *empirically observed* (via shoshin source); ELI-specific load is *characterized from documents*.

- **Clean theory and unification, not novelty** (Joseph's framing correction). The verdict reads as integration content. The wrapping construction *unifies* Parts I/II and Parts III/IV; *clarifies* the directed-separation classification; *cohere* with the form-preservation reading from the temporal-nesting-RG spike.

## 7. Final recommendation

**To Joseph**:

The wrapping construction is real and theoretically clean. It strengthens `#hyp-directed-separation-under-composition`, refines `#der-directed-separation`, and resolves the "Class 2 exit" framing into a "constructive route through." Per the prior-art findings, it is integration content rather than invention — POMDP and cognitive architectures already established the structural move; AAD's contribution is the synthesis with sector-Lyapunov / Brooks's-Law / class-taxonomy machinery, plus the LLM-specific (C1)–(C3) leakage characterization.

**Recommended segment-landing path**:

1. **Land** `#der-class-coercion-via-wrapping` in `01-aat-core/src/` per §4.1. The theorem statement and proof are ready (in `01-theorem-statement.md`); writing the segment is mostly translation into FORMAT.md conventions.

2. **Update** `#der-directed-separation` Discussion with the W₀/W₂/W₁ refinement; cite POMDP and cognitive-architecture prior art for the directed-separation guarantee.

3. **Update** `#hyp-directed-separation-under-composition` to cite the new segment as a derived special case.

4. **Land** `#der-logogenic-as-wrapping` in `03-logogenic-agents/src/` (specialization to language substrate) once the AAD-core segment is in place.

5. **Strengthen PROPRIUM toward W₁** via the auxilia hierarchy — this is engineering work in shoshin, not theory, but the spike has identified the path. It would be a worthwhile follow-up project.

6. **Future spike (separate)**: Class-3 closure-defect analysis to test the directed-separation-as-graded-order-parameter view (Move F from `spikes/temporal-nesting-rg/99-verdict.md`). The wrapping construction has provided the W₀/W₂/W₁ hierarchy as the structural side of this; the dynamics-side analysis (do W₀ vs. W₁ systems flow differently under coarse-graining?) is the remaining piece.

**My judgment**: this is a clean strengthening of ASF's structural foundation, with full citation of the POMDP and cognitive-architecture prior art per the prior-art-integration discipline. It clarifies what was previously a "scope exit" into a "constructive route." Worth landing.

If Joseph agrees, the next concrete actionable step is writing the `01-aat-core/src/der-class-coercion-via-wrapping.md` segment per FORMAT.md conventions, drawing from `01-theorem-statement.md`, `02-admissibility.md`, `03-leakage.md`, and `04-epsilon-semantics.md` for content.

---

## File index (final)

- `00-brief.md` — framing and sub-spike enumeration. Reframed mid-spike to truth-discovery emphasis after Joseph's correction.
- `01-theorem-statement.md` — theorems 1 and 2, proofs, conditions, what's wrapper-design constraint vs. theorem content. Load-bearing.
- `02-admissibility.md` — three-class partition (Class A goal-blind by design; Class B admit goal-blind mode; Class C fundamentally goal-conditioned). LLMs sit in Class B with leakage caveats.
- `03-leakage.md` — W₀/W₂/W₁ hierarchy. $\kappa_\text{W₁}$ bounded by $I(A(q_M); G_W \mid q_M)$; $\kappa_\text{W₂}$ has no structural bound, only behavioral. Central distinction.
- `04-epsilon-semantics.md` — $\varepsilon^*_\text{track}$ vs $\varepsilon^*_\text{coerce}$ disambiguation. Quick clarification.
- `05-tempo-cost.md` — DEFERRED. Follow-up if specific predictions needed.
- `06-empirical-instances.md` — delegated. PROPRIUM as W₂; auxilia hierarchy as W₁ realization candidate; output-structuring as the dominant pattern.
- `07-quantitative-bounds.md` — DEFERRED. Follow-up if empirical predictions needed.
- `08-parts-3-4-connection.md` — PROPRIUM class assignment, strengthening proposal, ELI-specific-load separation, segment-level integration.
- `09-prior-art-differentiation.md` — delegated. V1 verdict: substantial overlap with POMDP and cognitive architectures. Integration content.
- `99-verdict.md` — this file.
