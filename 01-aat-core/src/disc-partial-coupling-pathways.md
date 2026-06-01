---
slug: disc-partial-coupling-pathways
type: discussion
status: discussion-grade
depends:
  - der-directed-separation
  - der-orient-cascade
  - der-class-coercion-via-wrapping
  - disc-adversarial-coupling-pressure
stage: draft
---

# Discussion: Partial-Coupling Pathways — A Sub-Typology Within Class 2

Class 2 (Partial Coupling) per `#der-directed-separation` is named structurally as "some shared infrastructure, some separate pathways" and operationalized as a scalar $\kappa_{\text{processing}} \in (0, 1)$ that aggregates over the un-modeled internal sub-structure. The scalar is distribution-dependent and tracks the *magnitude* of goal-coupling, but not its *kind*: it cannot distinguish the agent that uses goals to *attend* from the one that uses goals to *interpret*, or the agent biased by *what it wants to be true* from the one foreclosed by *what plan it has committed to*, or the additively-biased agent (whose coupling is wrappable by post-hoc debiasing) from the multiplicatively-entangled agent (whose coupling is not). These distinctions are operationally distinct — they recommend different repairs, predict different dynamical signatures, and gate different wrapping regimes.

This segment names the structural sub-space the scalar projects over. Class 2 partial coupling decomposes along three structurally-independent axes — *stage*, *source*, and *form* — yielding a parameterization within which the Class 3 (fully Coupled) corner and the Class 1 (Separated) corner are recovered as the two trivial endpoints. The stage axis tracks which step of the belief-update pipeline takes a $G_t$ argument; the source axis tracks whether the coupling comes from the objective $O_t$ or from the strategy $\Sigma_t$; the form axis tracks whether the coupling acts as separable additive bias on a stage's output (*content*) or as a non-separable change of the stage's functional form (*process*). The three axes have distinct operational consequences (Discussion §"Operational consequences" below), and the form axis at Class 2 unifies with the *structure*-vs-*behavior* refinement at Class 1 — they are the same distinction read at different architectural levels.

The treatment is discussion-grade at the structural-recognition level. The pipeline decomposition is posited as canonical for Bayesian-style updaters and serves as an interpretive lens for monolithic architectures. The substantive structural results that fall out — form-determines-wrappability (a content-form / process-form no-go cut), and the source asymmetry of belief-strategy attractors — are stated qualitatively here and derived in their own segments (`#der-belief-strategy-attractor` for the source-asymmetry result; the form no-go is stated formally in this segment's Discussion). The combinatorial parameterization is structurally complete but operationally too fine; the load-bearing distinctions live on the (form × source) projection with stage as a localization tag.

## Formal Expression

### Pipeline decomposition of $f_M$

*[Formulation (partial-coupling-pipeline)]*

Any belief-update function $f_M$ that maintains $M_t$ — whether Bayesian, Kalman, RL with separate world model, or LLM-as-tracker — factors functionally through a small set of operations. The canonical decomposition is

$$f_M \;=\; \tau \;\circ\; \alpha \;\circ\; \lambda \;\circ\; \phi$$

with the four stages mapping to AAT machinery already in canon:

| Stage | Operation | AAT correspondent |
|---|---|---|
| **P1 — Featurization** | $\phi: \mathcal{E} \times \mathcal{M} \to \mathcal{X}$, $x = \phi(e_\tau, M_{\tau^-})$ | Extracts features from the realized event given current model; in a Kalman tracker, the innovation $\delta = o - \hat o$ per `#def-mismatch-signal` |
| **P2 — Likelihood evaluation** | $\lambda: \mathcal{X} \times \mathcal{M} \to \mathcal{L}$, $\ell = \lambda(x, M_{\tau^-})$ | Evaluates the likelihood of features under representable hypotheses; in a Kalman tracker, the Gaussian likelihood on $\delta$ with innovation covariance $S$ |
| **P3 — Aggregation** | $\alpha: \mathcal{L} \times \mathcal{M} \to \mathcal{M}^+$, $M' = \alpha(\ell, M_{\tau^-})$ | Combines likelihood with prior to produce new belief; in a Kalman tracker, the gain-weighted update with $\eta^\ast = U_M / (U_M + U_o)$ per `#emp-update-gain` |
| **P4 — Consolidation** | $\tau: \mathcal{M}^+ \to \mathcal{M}$, $M_{\tau^+} = \tau(M')$ | Post-update transformation: storage, normalization, regularization, memory consolidation |

Each of (P1)–(P4) can independently take or omit a $G_t$ argument. The Class 1 case has none; the Class 3 case has all; Class 2 is everything between.

The decomposition is posited rather than derived. It is canonical for Bayesian-style belief-updating agents and serves as an interpretive lens for monolithic architectures (where the stages are not architecturally distinct in the forward pass) — the typology's precision drops the more monolithic the agent.

### The (stage × source × form) parameterization

*[Definition (class-2-sub-type)]*

A Class 2 partial-coupling sub-type is a triple $\mathcal{C}_2 = (S, R, F)$ with:

- $S \subseteq \{P1, P2, P3, P4\}$, $S \neq \emptyset$ and $S \neq \{P1, P2, P3, P4\}$ — the **stage set** at which goals enter $f_M$. Empty $S$ recovers Class 1; full $S$ (with all-process form) recovers Class 3.
- $R \subseteq \{O, \Sigma\}$, $R \neq \emptyset$ — the **source set** within $G_t = (O_t, \Sigma_t)$ that acts as the coupling input.
- $F: S \to \{\text{content}, \text{process}\}$ — the **form** at each coupled stage.

The endpoints recover canon: $S = \emptyset$ is Class 1; $(S, R, F) = (\{P1, P2, P3, P4\}, \{O, \Sigma\}, \text{process})$ is Class 3 (fully Coupled). The scalar $\kappa_{\text{processing}}$ is the projection of $\mathcal{C}_2$ onto the magnitude axis.

### Form classification — content vs process

*[Definition (coupling-form)]*

A stage operation $\xi(\cdot; G)$ is **content-form coupled** if there exist functions $\xi^0$ (goal-blind) and $b_\xi$ (bias) such that

$$\xi(u; G) \;=\; \xi^0(u) \;+\; b_\xi(G; u)$$

with $b_\xi$ identifiable from a probing protocol that varies $G$ at fixed $u$ (specifically: a reference goal $G_0$ exists with $b_\xi(G_0; u) = 0$, or $b_\xi$ is identifiable up to a $u$-dependent constant by varying $G$ across finitely many probes).

A stage operation is **process-form coupled** if no such decomposition exists — the operation's *functional form* depends on $G$, not just its output. The multiplicative case $\xi(u; G) = \xi^0(u) \cdot h(G; u)$ is the most common process form (multiplicative attention coupling, gain modulation, precision weighting); the compositional case $\xi(u; G) = \xi^\dagger(u, G)$ with no separable factor is the starkest form.

The classification is *probing-protocol-dependent*: an analyst with reference-goal access may classify as content where an analyst without that access classifies as process. This is the same epistemic situation as the existing $\hat\kappa_{\text{processing}}$ behavioral estimator — the form classification inherits the same probe-dependence.

### Form-determines-wrappability — the central operational claim

*[Derived (content-process-wrappability, conditional on probing model)]*

For a Class 2 sub-type with coupling triple $(S, R, F)$:

**Positive half (content-form is post-hoc-wrappable).** Stages with content-form coupling admit an *external debiasing wrapper* that requires only behavioral-probing access (no internal pipeline access). The wrapper estimates $b_\xi(G; u)$ from probes that vary $G$ at fixed $u$, then subtracts the estimated bias in normal operation. The wrapped output converges to $\xi^0(u)$ as the estimator becomes consistent. This corresponds to the W₂ (partial-wrapping) regime at the agent level — "the query boundary still passes $G_W$ to the component" with typed-output structuring extracting a goal-blind belief-update.

**Negative half (process-form is not post-hoc-wrappable).** Stages with process-form coupling do not admit such an external wrapper. The argument is identifiability-theoretic: under process-form there is no $G_0$ making $h \equiv 1$ (or, more generally, no $u$-independent reference goal recovering $\xi^0$); behavioral probes that vary $G$ reveal goal-correlated differences but cannot collapse them to a $G$-invariant honest output. Repair requires either *stage replacement* (substituting a goal-blind version of the stage in the pipeline — requires substitutability access at the stage's input/output boundary) or *full-agent wrapping* (the W₁ strict-wrapping regime, operating at the whole-agent boundary).

The form distinction is therefore *load-bearing*, not ornamental — it gates the wrapping regimes available for coercion to Class 1.

### Stage-cascade propagation

*[Derived (cascade-propagation)]*

Goal-coupling at stage $P_k$ contaminates all downstream stages $P_{k+1}, \ldots, P_4$ even when those downstream stages are individually goal-blind, because their inputs are functions of $G$ through the cascade. The *naming* of a sub-type by its primary coupling stage refers to where the coupling originates; the *effect* propagates forward through the pipeline. Minimal repair (per stage-localization-of-repair, below) is therefore at the *most upstream coupled stage*, not at the most downstream symptom.

### Stage-localization of repair

*[Derived (stage-localization-of-repair, conditional on pipeline access)]*

If pipeline access is available at stages $P_k \in S$ — the wrapper can intercept the stage's input and supply its output to $P_{k+1}$ — then substituting goal-blind operations $P_k^0$ at every coupled stage produces a wrapped agent that is Class 1 at the wrapper level. The construction has a capability cost (the substitute operations may be weaker than the agent's native ones) and a Brooks's-Law tempo overhead (more pipeline calls per macro-step), but the structural class-coercion is exact.

For monolithic architectures without pipeline access, only full-agent wrapping (the construction of `#der-class-coercion-via-wrapping`) is available; stage-level repair does not apply.

### Composition with the leakage locus

Goal contamination's *effect on belief* is confined to the Fisher null space $\ker\mathcal{I}_\tau$ of the observation given the current latent state (the leakage-locus result, when promoted to its own segment, will be the formal statement). This locus is *universal across Class 2 sub-types* — it does not depend on which pipeline stage the coupling enters. The sub-type determines the *functional form* of the displacement within the locus:

- Content-form sub-types produce displacement linear in $G$ (the $\Delta\mu = \Lambda_0^{-1} g(G)$ shape in the linear-Gaussian instantiation, with $g(G)$ a linear function of the goal-tilt parameter).
- Process-form sub-types produce displacement with a $G$-dependent gain matrix or a $G$-dependent covariance structure — non-linear in $G$.
- $\Sigma$-source sub-types compound the per-step displacement across the closed-loop dynamics; under multiplicative process form, self-stabilizing belief-strategy attractors arise (`#der-belief-strategy-attractor`).
- $O$-source sub-types produce exogenously-bounded tilt magnitude (because $O_t$ revises only when forced, per `#der-orient-cascade`).

### Wrapping-regime correspondence

The W₀ / W₁ / W₂ wrapping regimes of `#der-class-coercion-via-wrapping` are the agent-level analogs of the stage-level form distinction:

| Wrapping regime | Stage-level analog | Class achieved at wrapper |
|---|---|---|
| W₀ (no wrapping) | n/a — the agent stands as-is | Whatever the un-wrapped agent is |
| W₂ (partial wrapping) | Content-form at the agent level — wrapper passes $G$ to component, post-hoc structures the response | Class-1-by-behavior (per `#der-directed-separation`) |
| W₁ (strict wrapping) | Process-form-with-pipeline-access — wrapper structurally substitutes goal-blind execution | Class-1-by-structure |

This unifies the *structure*-vs-*behavior* distinction at Class 1 with the *content*-vs-*process* form distinction at Class 2: they are the same axis read at different architectural levels. The structure / behavior distinction at the Class 1 cell is the agent-level shadow of a sub-classification axis that runs all through Class 2.

Sub-type matching refines the wrapping-regime recommendation: a Class 2 agent with content-form coupling only is sufficient with W₂; a Class 2 agent with process-form coupling at any stage requires W₁ or remains effectively Class 2 under W₂; a Class 2 agent with $\Sigma$-source coupling may need a $\Sigma$-channel-suppressed W₁ even with pipeline access, because strategy-context can leak through stateful component channels independent of the query. The call-boundary condition under which W₁'s structural guarantee survives such stateful leakage is the (C2′) condition of `#disc-w1-structural-bound-boundary`: when goal-correlated state crosses the call boundary, W₁'s structural bound is unavailable and only a behavioral bound remains.

## Epistemic Status

*Discussion-grade* at the structural-recognition level. The pipeline decomposition is a *formulation choice* — canonical for Bayesian-style updaters and well-motivated by AAT's existing machinery, but not forced by AAT canon. The (stage × source × form) parameterization is derived from the choice. The form distinction is *robust qualitative* at the operational level (the content / process distinction has a clean identifiability argument); the formal definition is probing-protocol-dependent.

The two substantive structural consequences carry their own tiers:

- **Form-determines-wrappability** (this segment, Discussion §): *robust qualitative* — the identifiability argument is exact under the formal non-separability definition; the operational dependence on probing-protocol availability is honest scope.
- **Source asymmetry / belief-strategy attractors** (`#der-belief-strategy-attractor`): *conditional* — exact under the linearized dynamics and the posited multiplicative form for $\Sigma$-source aggregation-stage coupling; robust qualitative beyond.
- **Composition with leakage locus**: *derived* under the linear-Gaussian instantiation; robust qualitative more generally (it composes existing structural results).
- **Wrapping-regime correspondence**: *robust qualitative* — the structural correspondence is exact, but boundary cases (partial-information wrappers between W₁ and W₂) require per-case analysis.

The full $42 \times 2^{\lvert S\rvert}$-cell parameterization is structural completeness; operationally the load-bearing distinctions live on the coarsening to *upstream-most coupled stage* × *source-set* × *form*, which gives roughly 30 cells, of which empirically about a dozen are populated by recognizable phenomena (canonical phenomena placed in Discussion §"Canonical phenomena" below).

## Discussion

**Why the form axis is the operationally-load-bearing one.** Of the three axes — stage, source, form — the form axis is the one that gates wrappability: it determines whether external post-hoc debiasing suffices or whether stage replacement / full-agent wrapping is required. The source axis is the one that gates *dynamics*: $\Sigma$-source coupling closes a feedback loop through the orient cascade and can produce self-stabilizing attractors that $O$-source coupling cannot. The stage axis is the one that gates *architectural location of repair*: it determines where in the pipeline the substitution or debiasing must be applied. These three operational outputs from the typology — wrappability, attractor possibility, repair location — each correlate with one axis, which is why the three-axis decomposition is more informative than the scalar.

**Unification with Class 1's structure-vs-behavior refinement.** The Class 1 cell of `#der-directed-separation` admits a refinement: *Class-1-by-structure* (no $G$ in the belief-update query — structural commitment by type signature) vs *Class-1-by-behavior* (the query passes $G$ but the component is instructed not to use it — separation by compliance). The form distinction at Class 2 is the same axis: *content-form* is the behavior-side (the operation accepts $G$ but its goal-shaped component is post-hoc-subtractable); *process-form* is the structure-side (the operation's functional form depends on $G$ inseparably, requiring substitution). Read together, the structure / content side and the behavior / process side describe two distinct *modes* of goal-coupling — one in which the coupling can be neutralized by *not asking* (or by subtracting after asking), and one in which the coupling is constitutive of the operation.

**Why the $\Sigma$-source / $O$-source asymmetry matters.** The orient cascade (`#der-orient-cascade`) has $\Sigma$ updated as a function of $(M, O)$ and $O$ revised only when forced. This makes $\Sigma$ *endogenous* to $M$ via the cascade — $\Sigma$ updates from the new $M$ that the agent's $f_M$ produces — but leaves $O$ *exogenous* to $M$ in steady state. The asymmetry feeds back: a Class 2 agent with $\Sigma$-source coupling at any stage of $f_M$ has the structure $M \to \Sigma \to f_M \to M$ closing a loop, while the same coupling sourced from $O$ has no such closure (because $O$ does not update from $M$ per step). The result is that $\Sigma$-source coupling under multiplicative process-form admits *self-stabilizing fixed points* in which $M$ stays misaligned with the environment indefinitely — the formal sunk-cost attractor of `#der-belief-strategy-attractor`. $O$-source coupling produces *bias* but not *runaway commitment*.

**Canonical phenomena placed in the typology.** The cells the typology produces are operationally meaningful:

| Phenomenon | Stage(s) | Source | Form | Repair regime |
|---|---|---|---|---|
| Goal-directed attention | (selection — pre-$f_M$) | $O$ or $\Sigma$ | — | None — formally allowed by `#der-directed-separation` scope condition |
| Motivated reasoning (identity-driven) | P1 + P2 | $O$ | Content (moderate) → Process (strong) | W₂ moderate; W₁ + identity-suppression strong |
| Sunk-cost commitment | P3 | $\Sigma$ | Process (multiplicative) | W₁ + $\Sigma$-suppression; admits attractors per `#der-belief-strategy-attractor` |
| Identity-protective consolidation | P4 | $O$ | Process (compositional) | W₁ + storage-protocol externalization |
| Frame coupling | P1 | $O + \Sigma$ | Process (compositional) | Multi-frame composition (not coercion to Class 1) |
| Wishful thinking | P3 | $O$ | Content (mild) → Process (strong) | W₂ mild; W₁ strong |
| Affect / urgency cascade-bypass | (cascade-bypass) | n/a (not stage-coupling) | n/a | External pacing scaffolding (per `#disc-adversarial-coupling-pressure` affect mechanism) |
| Attention-mediated transformer-LLM | P1+P2+P3 | $O + \Sigma$ (prompt-mixed) | Process (compositional) | Full Class-3 — W₁ wrapping construction, no stage repair without internal access |

The transformer-LLM case lands at the corner $(S = \{P1, P2, P3\} \text{ or } \{P1, P2, P3, P4\}, R = \{O, \Sigma\}, F \equiv \text{process})$, which is the parameterization's structural corner near Class 3 (Coupled). The typology recovers canon at its endpoints. Classical confirmation bias is a *separate* failure mode: it is structurally $M_t^{\text{prior}} \to f_M$ self-coupling, not $G_t \to f_M$ coupling, and is allowed by `#der-directed-separation`'s scope condition (which has $M_{\tau^-}$ as an argument); it lives outside the (S, R, F) parameterization, except in the *trajectory-coupling* case where the prior has been historically shaped by $G$-coupled updates and the cumulative effect carries effective $G$-content. Trajectory coupling is a separate per-trajectory axis from the per-step typology.

**Connection to the three operations on modularity state.** The M4 meta-segment `#disc-modularity-state-dynamics` names three operations — truthification, strategic self-coupling, adversarial coupling pressure — that change modularity state. The typology here is *orthogonal* to those operations: the operations describe *transitions* through the parameterization (truthification reduces $S$ or simplifies $F$; strategic self-coupling expands $S$ and shifts $F$ toward process; adversarial pressure expands $S$ from the outside, targeting specific cells — identity-binding targets P1+P2 / $O$; sunk-cost-engineering targets P3 / $\Sigma$); the typology describes the *static structural sub-space* on which the operations act. Each adversarial-coupling-pressure mechanism corresponds to a specific cell, and the three-mechanism table is best read as the projection of the typology's static structure onto the *externally-driven-decreasing* leg of M4's three-operation pattern. M4 names the operations; this segment names the structural state-space.

**Operational consequences — refined behavioral estimator.** The existing $\hat\kappa_{\text{processing}}$ behavioral estimator (per `#der-directed-separation` §"Empirical estimator") aggregates over the typology. A refined estimator would distinguish:

- *Stage*: probing intermediate representations (where mechanistic-interpretability access exists) localizes the upstream-most coupled stage.
- *Source*: probing under $O$ varied at fixed $\Sigma$ vs $\Sigma$ varied at fixed $O$ separates the source set.
- *Form*: probing distinguishes mean shifts (content signature) from covariance shifts or functional-form changes (process signature) in the agent's responses across goal-variants.

The refinement targets *which sub-type* the agent inhabits, not just the aggregate magnitude. Per the composition with the leakage locus, all such probing should be confined to $\ker\mathcal{I}_\tau$ — the directions the observation does not identify — which is where the displacement lives.

**Honest scope.** The typology is most precise for *modular* Class 2 architectures (biological cortex per the canonical example; hybrid AI systems with separable preprocessing / inference / aggregation modules). For monolithic architectures (transformer LLMs, end-to-end-trained policies), the stage decomposition is *interpretive* — the stages are not architecturally distinct in the forward pass; the typology serves as a lens for mechanistic-interpretability investigations rather than as a structural classification. The form classification is *probing-protocol-dependent*; analysts should specify which probes were available. Content-form wrapping gives *Class-1-by-behavior*, not honesty: under gauge freedom in the identifiability, the wrapper produces a $G$-invariant version of the agent's belief, up to an unknowable additive constant.

## Findings

### Partial-Coupling Sub-Typology (Stage × Source × Form)

**Brief:** The Class 2 (Partial Coupling) label in AAT names "some shared infrastructure, some separate pathways" between belief-update and goal-state processing, but the existing scalar measure $\kappa_{\text{processing}}$ collapses a rich internal sub-structure into a single magnitude number. Look more carefully and three structurally-independent axes emerge: *which stage* of the belief-update pipeline takes a goal argument (attention / interpretation / aggregation / storage); *which source* of goal-state acts (the agent's objective, or its committed strategy); and *which form* the dependency takes (additive bias subtractable by post-hoc debiasing, vs functional-form change requiring internal substitution). Each axis carries a distinct operational consequence: the form axis gates whether external wrapping can coerce the agent back to Class 1; the source axis gates whether self-stabilizing belief-strategy attractors are possible; the stage axis gates where the repair must be applied. The Class 3 (fully Coupled) limit is the corner where all stages couple, both sources act, and the form is process-throughout; Class 1 is the opposite corner; Class 2 is the structured space between.

**Impact:** Refines the operational meaning of the Class 2 label from "uncomfortable middle category" to "structured sub-space with specific repair regimes per cell." Unifies the *Class-1-by-structure* vs *Class-1-by-behavior* refinement (currently sitting at the Class 1 cell of `#der-directed-separation`) with the form-axis of the Class 2 sub-typology — they are the same distinction read at different architectural levels. Sharpens wrapping-regime selection (W₁ vs W₂) by sub-type rather than by Class label alone. Maps the three adversarial mechanisms named in `#disc-adversarial-coupling-pressure` (identity-binding / affect-urgency / sunk-cost-engineering) onto specific cells of the typology, with the affect/urgency case recognized as outside the static (stage × source × form) parameterization (it is a cascade-bypass, a separate failure mode). Provides the static-structural complement to the M4 meta-segment `#disc-modularity-state-dynamics`'s three operations on modularity state — the operations describe transitions through the parameterization the typology names.

**Novelty Claim:** *Claim recognition* of the (stage × source × form) sub-typology as the structural complement to Class 1's structure-vs-behavior refinement. *Claim differentiation* on the wrapping-regime correspondence: which wrapping regime suffices for Class 2 → Class 1 coercion is determined by the sub-type's form, not just by the Class label. The integration with the leakage-locus result (locus universal in $\ker\mathcal{I}_\tau$; typology determines functional form within the locus) and the source-asymmetry implication (`#der-belief-strategy-attractor`) are the load-bearing structural consequences.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| Active inference / FEP fused goal-perception | Friston 2010+ corpus; covered in `ref/Prior_art_for_AAT_directed_separation.md` Pillar | *adjacent literature* — the unified variational machinery is structurally process-form at all stages (the Class 3 case); the *partial-separation sub-typology* is not addressed in this literature |
| Motivated reasoning / cultural cognition | Kunda 1990 *Psych Bull*; Kahan cultural-cognition project | *not yet searched* — primary novelty target for the source asymmetry and form-classification of motivated cognition |
| Identity economics & motivated beliefs | Bénabou-Tirole 2002, 2011 *QJE*; Akerlof-Kranton 2000 *QJE*, 2010 | *not yet searched* — primary target for whether the $O$-source vs $\Sigma$-source asymmetry has an economics-side antecedent |
| Dual-process theory | Evans 2008; Kahneman 2011; Stanovich 2009 | *not yet searched* — coarse Class 1 / Class 3 distinction is informally present; the sub-typology of partial coupling is not the literature's frame |
| Self-deception philosophical taxonomy | Mele 2001 *Self-Deception Unmasked*; von Hippel & Trivers 2011 *BBS* | *not yet searched* — possible direct anticipation on the philosophical sub-classification side |
| Goal-shielding | Shah, Friedman & Kruglanski 2002 *JPSP* | *not yet searched* — candidate empirical instantiation of P3 / $\Sigma$ / process-form coupling |

**Search Log:**

- 2026-05-22 (*intuition-only*): The active-inference / Pearl-blanket / Friston-blanket prior-art landscape is already covered in `ref/Prior_art_for_AAT_directed_separation.md` (Pillar-3 search) and addresses the unified variational machinery as the Class 3 (fully Coupled) case; the *partial-separation sub-typology* this segment develops is not in that prior-art landscape. The cognitive-psychology / motivated-reasoning / identity-economics / dual-process / self-deception literatures are *unsearched*; targeted Pillar search recommended before any tier upgrade. The form distinction (content vs process) likely has analogs scattered across literatures (most explicitly in Bénabou-Tirole's identity-vs-instrumental belief framing and in dual-process system 1 / system 2 separation); the source-asymmetry result is plausibly partially in the sunk-cost / commitment-cascade empirical literature implicitly but not as a derived structural theorem. The combined (stage × source × form) parameterization in AAT-internal vocabulary is plausibly novel under the search-depth conducted.

## Working Notes

- **Promotion path requires two sub-spikes.** (a) Pillar-style targeted prior-art search across motivated-reasoning, identity-economics, dual-process, and self-deception literatures; (b) derivation of the multiplicative form for $\Sigma$-source aggregation-stage gain $K(\Sigma)$ from utility-cost analysis of belief-revision-under-strategic-commitment (this gates `#der-belief-strategy-attractor`'s tier from *conditional* to *exact*). Both are in `TODO.md` per the queue maintenance.

- **Composite-level sub-type inheritance.** The composite-level class-inheritance table in `#der-directed-separation` (axis-decomposed by routing × substrate × dynamic-regime) tracks Class (1/2/3) inheritance. Extending the table to track Class 2 *sub-type* inheritance under composition is a substantive follow-on: given sub-agents with sub-types $(S_i, R_i, F_i)$, what sub-type does the composite occupy under routing $R$ and substrate $\sigma$? Not on the critical path for this segment; recorded as a candidate sub-spike for the composition machinery to extend.

- **Trajectory coupling as separate axis.** The per-step (stage × source × form) parameterization does not cover *trajectory* coupling — cumulative goal-content accumulating in $M_t$'s prior across history through repeated small Class 2 couplings, then amplified by goal-blind processing of new evidence. This is a real failure mode (and arguably the operational route to confirmation-bias cascades) but lives in a per-trajectory dynamics layer rather than the per-step structural typology. A separate spike treating trajectory coupling would parallel this segment's per-step analysis; not pursued here.

- **Refined behavioral estimator — construction.** §Discussion sketches a refined estimator that probes along $\ker\mathcal{I}_\tau$ and distinguishes mean (content) from covariance/functional-form (process) signatures. Actual estimator construction is a separate work item; the segment names the targets but does not construct the estimator.

- **Brief is not yet at Feynman criterion.** The current Brief reaches for the structural-recognition framing rather than an everyday physical analog. A candidate analog under consideration: the difference between (a) an engineer reading instruments and writing a goal-blind report, then a separate engineer reading the report and deciding what to do, versus (b) a single engineer reading instruments with the decision already in mind, where what they notice depends on what they're trying to accomplish — the first is Class 1, the second Class 3, and Class 2 is the messy middle where the typology says *which* part of the data-reading process is being shaped by the goal, *whether* the shaping is what-the-engineer-wants or what-plan-they're-committed-to, and *whether* the shaping is a measurable bias (subtractable) or a wholesale reframing (not subtractable). The bathtub-equivalent has not been written; the engineer-and-report analog is a working candidate but its isomorphism to the load-bearing structure (especially the source-asymmetry attractor and the form-determines-wrappability cut) needs verification.

- **Connection back to `#def-agent-spectrum` Working Note.** The Working Note in `#def-agent-spectrum` ("The one genuinely-new thread: where the dangerous coupling concentrates") points at the leakage locus as a *where-in-the-inference* localization. This segment is the *through-what-stage-of-the-inference* complement. Together with the leakage-locus result they answer the two complementary questions: *where in state-space the effect lives* (leakage locus) and *what functional form it takes there* (this typology). When the leakage-locus result lands as its own appendix segment, the cross-reference should be made explicit on both sides.
