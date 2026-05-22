---
slug: der-class-coercion-via-wrapping
type: derived
status: conditional
depends:
  - der-directed-separation
  - def-agent-environment
stage: draft
---

# Derived: Class Coercion via Wrapping

A *constructive* result of substantial practical importance. A Class 2 (Partial) or Class 3 (Coupled) component (one whose forward pass entangles belief-update and goal-conditioning) can be embedded inside an external scaffold whose state $X_W = (M_W, G_W)$ is updated by *structurally distinct query channels*: **goal-blind queries** to the component update $M_W$; **goal-conditioned queries** update $G_W$. Under stated conditions on the component, directed separation holds at the wrapper level *by construction*, and the composite system is Class 1 (Separated) per `#der-directed-separation` — even though the underlying component is not. This is the constructive direction of `#hyp-directed-separation-under-composition` for the wrapper-around-component special case: a procedure for *making* directed separation hold when the underlying component does not provide it.

The wrapper has four type-signed components: a *belief-side query selector* that chooses the model-update query from belief and observation only — *no goal argument*; a *strategy-side query selector* that may depend on the goal; a *belief-update map* that updates $M_W$ from prior belief, observation, the query made, and the component's response — *no goal argument*; and a *strategy-update map* that may depend on the goal. The wrapper makes at least two component calls per macro-step: one goal-blind for the model update and one goal-conditioned for the purposeful-state update.

The result requires three conditions on the component. **(C1) Goal-blind admissibility** — the component admits non-trivial goal-blind queries; the framework partitions components into *Class A* (goal-blind by design: POMDP belief-state filters, world models, sensory pipelines, retrieval systems), *Class B* (admit a goal-blind query mode alongside goal-conditioned ones: LLMs in summarization/fact-extraction modes, hybrid RL with separable value/policy), and *Class C* (fundamentally goal-conditioned: pure end-to-end goal-conditioned policy networks), with the construction applying to Classes A and B. **(C2) Stationary component conditional** — the component's output distribution conditional on input is fixed during operation (adaptation-during-deployment systems are out of scope). **(C3) No implicit goal-inference** — the component's response to a goal-blind query does not depend on $G_W$ via inference from query patterns; for pretrained components like LLMs, (C3) holds *exactly* only when query content is statistically independent of $G_W$ in the pretraining distribution. The framework supplies **two theorems**: an *exact* form under (C1)–(C3), and an *approximate* form under (C1)–(C2) plus a KL-leakage bound, where the wrapper-level leakage on $M_W$ updates is bounded by the same bound (small leakage in, small leakage out via the data-processing inequality).

The construction supports three **wrapping regimes** of decreasing strictness, distinguished by where structural separation lives. **W₁ (strict wrapping)** uses separate $q_M$ and $q_G$ calls per macro-step; separation lives at the *query boundary* and leakage is bounded *structurally* by pretraining-induced mutual information. **W₂ (partial wrapping)** uses one goal-conditioned call per macro-step with a typed parsed response routing updates to $M_W$ vs $G_W$ slots; separation lives at the *write boundary* and leakage is bounded only *behaviorally* — by the component's compliance with the prompted instruction-to-separate. **W₀ (no wrapping)** runs the raw Class 2 / Class 3 component with no separation commitment. The same KL-form bound covers W₁ and W₂; what differs is *what determines* the leakage rate. The hierarchy refines the Class 1 (Separated) cell of `#der-directed-separation` with a *Class-1-by-structure* (W₁ or natively goal-blind) vs *Class-1-by-behavior* (W₂) sub-distinction.

The result is *load-bearing* for the framework's treatment of LLM agents: an LLM is internally Class 3 (Coupled), but an LLM-agent *system* (LLM + tools + memory + monitoring) can be designed with modular topology that recovers Class 1 status at the system level. The construction's cost is paid in two places — *more component calls per macro-step* (the Brooks's-Law tempo overhead derived in the companion segment) and a *residual leakage rate* bounded structurally under W₁ or behaviorally under W₂. The companion segment `#der-class-coercion-in-composition` establishes that the wrapped system is also a valid AAT composite agent (satisfying (A1)–(A4) of `#form-composition-closure`) and inherits the sector-persistence template at the wrapper level.

## Formal Expression

### Setup

Let $A : \mathcal I_A \to \mathcal O_A$ be a primitive component, treated by the wrapper as a black-box oracle: the wrapper issues queries (inputs) and consumes responses (outputs), without access to $A$'s internal state. $\mathcal Q_A \subseteq \mathcal I_A$ is the set of admissible queries.

A **wrapper** $W$ over $A$ has state $X_W = (M_W, G_W) \in \mathcal X_M \times \mathcal X_G$ with $\mathcal X_G = \mathcal X_O \times \mathcal X_\Sigma$ per `#def-strategy-dimension`. The wrapper interacts with an environment via observations $o_W \in \mathcal O_W$ and actions $a_W \in \mathcal A_W$.

*[Definition (wrapper-update-maps)]* The wrapper's update at macro-step $m$ uses four type-signed components:

- **Belief-side query selector:** $q_M : \mathcal X_M \times \mathcal O_W \to \mathcal Q_A$. The wrapper chooses the query for $M_W$ updates from belief and observation only — *no $G_W$ argument*.
- **Strategy-side query selector:** $q_G : \mathcal X_M \times \mathcal X_G \to \mathcal Q_A$. May depend on $G_W$.
- **Belief-update map:** $f_M : \mathcal X_M \times \mathcal O_W \times \mathcal Q_A \times \mathcal O_A \to \mathcal X_M$. Updates $M_W$ from prior belief, observation, the query made, and the component's response. *No $G_W$ argument.*
- **Strategy-update map:** $f_G : \mathcal X_G \times \mathcal X_M \times \mathcal Q_A \times \mathcal O_A \to \mathcal X_G$. May depend on $G_W$.

The external policy $\pi_W : \mathcal X_W \to \mathcal A_W$ selects the wrapper's external action.

A macro-step proceeds: construct $q_M(M_W, o_W)$ → query $A$ → apply $f_M$; construct $q_G(M_W', G_W)$ → query $A$ → apply $f_G$; emit $\pi_W(X_W')$. The wrapper makes $K \geq 2$ component calls per macro-step in this minimal form (more in richer wrapper designs).

### Conditions

*[Conditions (component-admissibility)]* The theorem applies under three conditions on the component $A$:

**(C1) Goal-blind admissibility.** $\mathcal Q_A$ contains queries whose specification can be constructed from $(M_W, o_W)$ alone — i.e., a non-trivial $q_M$ exists. Components partition into three classes:
- **Class A (goal-blind by design).** $A$'s interface is goal-blind by construction — POMDP belief-state filters, world models, sensory pipelines, retrieval systems, calculators. (C1) holds trivially.
- **Class B (admit a goal-blind query mode).** $A$ supports goal-conditioned queries but also goal-blind ones. Large language models in summarization or fact-extraction modes; hybrid RL agents with separable value/policy; multi-modal models. (C1) holds operationally — the wrapper *chooses* to use the goal-blind mode.
- **Class C (fundamentally goal-conditioned).** $A$'s only operating mode requires goal-conditioning. Pure end-to-end goal-conditioned policy networks. (C1) fails; the construction does not apply.

**(C2) Stationary component conditional.** $A$'s output distribution conditional on input is fixed during the wrapper's operation: $P(A(\cdot) \mid q)$ does not depend on prior queries or on side information beyond $q$. Adaptation-during-deployment systems are out of scope.

**(C3) No implicit goal-inference.** $A$'s response to a goal-blind query does not depend on $G_W$ via inference from query patterns:

$$P(A(q_M) \mid q_M, G_W) = P(A(q_M) \mid q_M) \quad \forall\, q_M, G_W$$

For pretrained components (notably LLMs), (C3) holds *exactly* only when query content is statistically independent of $G_W$ in the pretraining distribution. The approximate form weakens (C3) to a leakage bound (Theorem 2 below).

### Theorem 1: Directed separation at the wrapper level (exact form)

*[Derived (directed-separation-at-wrapper-exact, from C1+C2+C3)]*

Under (C1)–(C3), directed separation holds *exactly* at the wrapper level:

$$P(M_{W,m+1} \mid M_{W,m},\ o_{W,m+1},\ G_{W,m}) = P(M_{W,m+1} \mid M_{W,m},\ o_{W,m+1})$$

Therefore $W$ is a Class 1 (Separated) architecture per `#der-directed-separation`.

*Proof.* Identify all paths from $G_{W,m}$ to $M_{W,m+1}$ given $(M_{W,m}, o_{W,m+1})$. The update is

$$M_{W,m+1} = f_M\big(M_{W,m},\, o_{W,m+1},\, q_M(M_{W,m}, o_{W,m+1}),\, A(q_M(M_{W,m}, o_{W,m+1}))\big)$$

$f_M$ has no $G_W$ argument by type signature (D-pathway-1 closed). $q_M$ has no $G_W$ argument by type signature (D-pathway-2 closed). The remaining pathway is $A(q_M)$ depending on $G_W$ given $q_M$. Under (C3), $P(A(q_M) \mid q_M, G_W) = P(A(q_M) \mid q_M)$ — the response is conditionally independent of $G_W$ given $q_M$. Since $q_M$ is itself a deterministic function of $(M_{W,m}, o_{W,m+1})$, conditioning on $(M_{W,m}, o_{W,m+1})$ determines $q_M$, and the integrand $P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1}, q_M, A(q_M)) \cdot P(A(q_M) \mid q_M, G_W)$ no longer depends on $G_W$. The conditional distribution of $M_{W,m+1}$ given $(M_{W,m}, o_{W,m+1}, G_{W,m})$ equals that given $(M_{W,m}, o_{W,m+1})$. ∎

### Theorem 2: Directed separation (approximate form, C3 weakened to leakage bound)

*[Derived (directed-separation-at-wrapper-approximate, from C1+C2+leakage-bound)]*

If (C3) is replaced by a KL-leakage bound

$$D_\text{KL}\big(P(A(q_M) \mid q_M, G_W)\, \big\Vert\, P(A(q_M) \mid q_M)\big) \le \kappa \quad \forall\, q_M, G_W$$

then the wrapper-level KL-divergence on $M_W$ updates is bounded by the same $\kappa$:

$$D_\text{KL}\big(P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1}, G_{W,m})\, \big\Vert\, P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1})\big) \le \kappa$$

The wrapper is *almost-Class-1 (Separated)* with leakage rate $\le \kappa$. *Proof.* The wrapper-level $M_W$ update is a deterministic function of the component response given the wrapper's other inputs; the data-processing inequality propagates the KL bound from response distribution to wrapper-state distribution. ∎

### Wrapping regime hierarchy

The construction supports three regimes, distinguished by where structural separation lives:

| Regime | Construction | Leakage bound | Leakage source |
|---|---|---|---|
| **W₀** (no wrapping) | Raw Class 2 (Partial) or Class 3 (Coupled) component | $\kappa_{W_0}$ at the component's maximum goal-conditioning sensitivity | No constraint |
| **W₂** (partial wrapping) | One goal-conditioned call per macro-step; structurally typed parsed response routes updates to $M_W$ vs. $G_W$ slots | $\kappa_{W_2}$ bounded *behaviorally* — by the component's compliance with the prompted instruction-to-separate; **no structural bound** | Component's instruction-following fidelity |
| **W₁** (strict wrapping) | Theorem 1 / 2 — separate $q_M$ and $q_G$ calls per macro-step | $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$ — bounded *structurally* by mutual information in the pretraining distribution | Pretraining-induced query-content / goal-content correlation |

W₁ admits a structural bound from (C3) or its weakening; W₂ admits only a behavioral bound from the component's compliance fidelity. The two are different in kind — structural bounds are derivable from query content; behavioral bounds depend on the component's training and prompt-following. The same KL-form bound of Theorem 2 covers both regimes; what changes is *what determines* $\kappa$.

The W₀ / W₂ / W₁ distinction refines the Class 1 (Separated) cell of `#der-directed-separation`: within Class 1 (Separated), **Class-1-by-structure** (natively goal-blind components, or W₁ wrapping) has a structurally derivable directed-separation guarantee; **Class-1-by-behavior** (W₂ wrapping) has only an empirically estimable guarantee that depends on the component's instruction-following.

## Epistemic Status

*Conditional* on (C1), (C2), and (C3) (or its weakening to a leakage bound). The proofs are short conditional-independence reasoning (Theorem 1) and a single application of the data-processing inequality (Theorem 2); both are standard.

Max attainable: derived under stated conditions. (C3)'s exact form is a structural ideal that pretrained components (notably LLMs with goal-rich training data) generally satisfy only approximately; the realistic regime is Theorem 2 with $\kappa$ characterized empirically.

The wrapping regime hierarchy (W₀/W₂/W₁) is a *formulation* — the partition is made by the structural choice of where to place the separation commitment. The leakage bounds within each regime are derived once the regime is fixed.

## Discussion

### Quality–separation tradeoff inside Class B

For Class-B components (admitting both goal-blind and goal-conditioned modes), the wrapper has a design choice: how aggressively to restrict $q_M$ to goal-blind content, vs. how much context to allow that may carry goal-correlated information. Maximally goal-blind queries (only the current observation, no context, no history) reduce the pretraining-induced leakage that bounds $\kappa_{W_1}$, but may produce information-poor responses that hurt $f_M$'s update quality. Maximally informed queries (full history, retrieved context) produce richer responses but increase the mutual information $I(q_M; G_W)$ and therefore the upper bound on $\kappa_{W_1}$. The tradeoff is real and resolved per application.

### Component-admissibility partition

Class A components (goal-blind by design) satisfy (C1) trivially and don't need wrapping in the substantive sense — wrapping for Class A is organizational rather than structural. Class B components (LLMs, hybrid RL with separable value/policy, multi-modal models) are the substantive wrapping case — the wrapper *chooses* to use the goal-blind mode. Class C components (pure end-to-end goal-conditioned policy networks) fail (C1) and are scope-out for the basic theorem. Salvage paths for Class C — null-goal queries, goal-uniform averaging, auxiliary distilled goal-blind heads — exist but cost something (information loss, computation, training).

### Resolution of the LLM scope question

The "Class 3 (Coupled) exit" framing — *directed separation violated by goal-conditioned agents (LLMs); handled as architectural scope, not approximation* — is refined by this segment from a scope exit to a constructive route through. Class 3 (Coupled) LLMs are scope-in *for the wrapper construction* (under Class-B admissibility). The cost is paid in residual leakage rate $\kappa_{W_1}$ bounded by pretraining-distribution mutual information; the tempo cost is established separately in `#der-class-coercion-in-composition`. Whether this construction yields an operationally useful agent depends on how favorable the pretraining-distribution-induced bounds are for the application.

### Relationship to `#hyp-directed-separation-under-composition`

The hypothesis is descriptive — when does directed separation hold under composition? This segment provides the constructive answer for the wrapper-around-component special case: directed separation holds whenever the wrapper's type signatures are respected and (C1)–(C3) hold (or their weakenings). The general N-agent composition question remains a hypothesis; the wrapper-around-component case is now derived.

### Wrapping as a truthification mechanism

The wrapping construction is the *rigorous formal version* of what `#disc-adversarial-coupling-pressure` §"Defensive scaffolding as composition" gestures at informally — peer review, prediction registers, double-entry bookkeeping, adversarial procedure, structured red-teaming. Those external scaffolds are operational mechanisms for *increasing* the modularity of a composite agent in the face of forces that would couple it; the wrapping construction is the structural version of the same operation applied internally rather than externally. Both share the discipline: a goal-blind belief-update query path is structurally enforced (W₁ strict) or behaviorally bounded (W₂), at a definite cost (extra component calls per macro-step plus residual leakage rate). The W₀/W₂/W₁ regime hierarchy is the *graded* characterization of how thoroughly the truthification has been applied — W₀ is the un-truthified base state, W₂ behavioral truthification, W₁ structural truthification. Forward-reference: `#disc-modularity-state-dynamics` (queued; scoped in `msc/modularity-cycle-plan-2026-05-09.md`) is the meta-segment in which the truthification operation sits as one of three operations on the modularity state — alongside strategic self-coupling (self-driven-decreasing) and adversarial coupling pressure (externally-driven-decreasing). When that meta-segment lands, this segment becomes the canonical *formal* instance of the truthification operation, paired with the *informal* defensive-scaffolding instance from the adversarial-pressure segment. Until then, the connection is named here and in `#impl-composition-machinery` §"Class-coercion as truthification mechanism."

## Findings

### Constructive Directed Separation via Wrapping

**Brief:** When you have a component (like an LLM) whose belief-update and goal-conditioning are entangled in a single forward pass, you can build a scaffold around it that maintains explicit, separate stores for what the system believes and what it wants. The structural rule is that belief updates only see queries to the component that don't include the goal as input. Under reasonable conditions on the component, the wrapped system is goal-blind in its belief updates *by construction* — even though the underlying component isn't. The cost shows up as a residual leakage from the component's pretraining (the component might still infer the goal from query content, even when the goal isn't explicit in the input). Two practical regimes appear: strict wrapping with separate goal-blind and goal-conditioned calls (theoretically clean, with a structural leakage bound), and partial wrapping with one goal-conditioned call whose response is parsed into separate update fields (operationally common, with only a behavioral leakage bound — depending on the component's instruction-following fidelity rather than its query structure).

**Impact:** Promotes `#hyp-directed-separation-under-composition` to derived (in the wrapper-around-component special case). Refines the Class 1 (Separated) cell of `#der-directed-separation` with a structural-vs-behavioral sub-distinction (W₁ vs. W₂). Resolves the LLM scope question — Class 3 (Coupled) components are scope-in for the wrapper construction at a measurable cost, not scope-out. The composition-level consequences (wrapper as valid AAT composite agent, persistence-template inheritance, tempo cost) are derived in the companion segment `#der-class-coercion-in-composition`.

**Novelty Claim:** *Claim integration* of POMDP / cognitive-architecture prior art with the AAT Class 1/2/3 (Separated/Partial/Coupled) directed-separation taxonomy, plus the W₀/W₂/W₁ regime hierarchy that surfaces the structural-vs-behavioral leakage distinction and the LLM-specific (C1)–(C3) admissibility/leakage conditions. The wrapping move itself is rediscovery of patterns established in POMDP theory (Bayesian belief-update is goal-blind by construction) and cognitive architectures (modular agent design with separated belief/goal/action state, four decades). AAT's contribution is the structural-leakage analysis at the directed-separation level and the regime hierarchy that names where the separation guarantee lives.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| Goal-blind belief-update by construction | Astrom 1965, "Optimal control of Markov processes with incomplete state information," *J. Math. Anal. Appl.* 10; Kaelbling, Littman, Cassandra 1998, "Planning and acting in partially observable stochastic domains," *Artificial Intelligence* 101 | *formal antecedent* — POMDP belief-state filters are goal-blind by construction; the wrapping move recapitulates this in the AAT vocabulary. The closest formal prior art for the directed-separation guarantee. |
| Modular agent design with separated belief/goal/action | Newell 1990, *Unified Theories of Cognition*; Laird 2012, *The Soar Cognitive Architecture*; Anderson 2007, *How Can the Human Mind Occur in the Physical Universe?*; Sun 2016 *Anatomy of the Mind* (CLARION); Baars 1988 *A Cognitive Theory of Consciousness* / Dehaene 2014 *Consciousness and the Brain* (Global Workspace) | *formal antecedent* — cognitive architectures have done modular agent design with separated belief/goal/action state for 40+ years. The W₁ wrapping move is essentially the per-cycle commitment that cognitive architectures make at the system level. |
| Tool-using language-model agent frameworks | Yao et al. 2022, "ReAct: Synergizing reasoning and acting in language models"; Shinn et al. 2023, "Reflexion: language agents with verbal reinforcement learning"; Park et al. 2023, "Generative Agents: Interactive Simulacra of Human Behavior"; Packer et al. 2023, "MemGPT: Towards LLMs as operating systems"; Schick et al. 2023, "Toolformer: language models can teach themselves to use tools" | *empirical instantiation* — practical wrappers around language-model substrates. Most fall in W₂ (partial wrapping / output-structuring); Generative Agents' observation→memory step is the closest empirical instance of W₁. AAT's regime hierarchy gives these constructions a structural reading. |
| Hybrid deliberative/reactive architectures (prior art for class-coercion) | Gat 1992, *Integrating planning and reacting in a heterogeneous asynchronous architecture for controlling real-world mobile robots* (AAAI)[^cat-2026-05-22]; Simmons 1994, *Structured control for autonomous robots* (IEEE Trans. Robotics 10:34)[^cat-2026-05-22]; Au 2004, planner wrappers with external-query management[^cat-2026-05-22] | *formal antecedent* — hybrid deliberative/reactive architectures orchestrate reactive (entangled) layers beneath deliberative (separated) planners, structurally precedent for the wrapping construction's "scaffold an entangled component to recover separated behaviour at the wrapper level" move. AAT's contribution is *not* the wrapping move itself but the *theorem-shaped* wrapper-level directed-separation guarantee (Theorem 1 + Theorem 2) plus the explicit leakage bound $\kappa_{W_1} \leq I(A(q_M); G_W \mid q_M)$ and the Brooks's-Law tempo cost in `#der-class-coercion-in-composition` |

**Search Log:**

- 2026-05-09 (*targeted*): Web + training-data search across POMDP / cognitive-architecture / scaffolded-LLM threads. Verdict: **substantial overlap** with the POMDP and cognitive-architecture lines as the closest formal prior art. AAT's contribution is the structural-leakage analysis and regime hierarchy rather than novelty in the wrapping move itself.
- 2026-05-09 (*intuition-only*, prior to the targeted search): adjacent literatures expected to host prior art were active inference (Markov blankets), control theory (approximate simulation), and scaffolded-LLM frameworks. The targeted search confirmed all three and added the POMDP and cognitive-architecture lines as the formal precedents.

## Working Notes

- **Empirical $\kappa$ measurement.** $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$ is computable for any component with stochastic outputs by sampling responses under multiple goal-conditioning histories and estimating the divergence. For a fixed component, this bound is a property of the wrapper's choice of $q_M$ — narrower queries reduce the bound, richer queries increase it. The empirical instantiation is open follow-on.
- **Sub-type-aware wrapping regime selection.** Knowing only that a component is Class 2 (Partial) is insufficient to choose W₁ vs W₂; the right regime depends on the un-wrapped component's coupling *form* per the (stage × source × form) sub-typology of `#disc-partial-coupling-pathways`: content-form sub-types admit W₂ (post-hoc response structuring); process-form sub-types require W₁ (structural goal-blind query path) or are not coercible to Class 1 without pipeline access. Additionally, $\Sigma_t$-source coupling (per `#der-belief-strategy-attractor`) can undermine W₁'s structural commitment via strategy-context leakage in stateful components — even with no $G_W$ in the query, the component's internal $\Sigma$ may be influenced by historical query content and then suppress the gain on subsequent goal-blind queries; a $\Sigma$-channel-suppressed W₁ (holding strategic context fixed across calls, or stripping $\Sigma$-content from queries) may be required. The W₀/W₁/W₂ hierarchy is the agent-level analog of the stage-level form distinction in the sub-typology — W₂ ↔ content; W₁ ↔ process-with-pipeline-access — making the structure-vs-behavior refinement at Class 1 the agent-level shadow of a Class 2 axis.
- **Compositional wrapping (wrapper-of-wrapper).** How leakage rates compose under iterated wrapping is open. Conjecture: additive in KL ($\kappa_{\text{outer}} \le \kappa_{\text{inner}} + \kappa_{\text{outer-shell}}$) by data-processing inequality applied at each level, but tightness is unclear.
- **Behavioral compliance axiom for W₂.** $\kappa_{W_2}$ has no structural bound; it depends on the component's instruction-following fidelity. Whether a behavioral-compliance axiom (assuming the component honestly attempts to follow structural-separation instructions) yields a bound is an open hypothesis. If so, it would be hypothesis-grade rather than derived.
- **Identifying the regime in the wild.** Practical scaffolded-LLM frameworks (ReAct, Reflexion, MemGPT, etc.) almost universally implement W₂. Distinguishing W₂ from W₁ in a deployed system requires inspection of the per-cycle query structure — does $f_M$'s update path receive a query that contains $G_W$ or not? This is the diagnostic question.
- **Segment split provenance (2026-05-11).** This segment was bifurcated from a combined "class coercion" derivation. Claim A (directed separation at the wrapper level) lives here; Claim B (wrapper as valid AAT composite agent — (A1)–(A4) verification, persistence-template inheritance, Brooks's-Law tempo cost) lives in `#der-class-coercion-in-composition` (which declares this segment as prerequisite). The split reflects FORMAT.md Gate 1 discipline: this segment's depends list (`der-directed-separation`, `def-agent-environment`) reflects exactly what the directed-separation theorem actually requires. The composition-level dependencies (`form-composition-closure`, `deriv-sector-condition`, `result-sector-persistence-template`, `der-tempo-composition`) are Claim B's load and now live with Claim B.
- Reasoning-trail provenance: spike directories at `spikes/class-coercion-wrapping/` and `spikes/temporal-nesting-rg/` carry the working-out of these results.
- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Three independent axes in this segment: (a) GUC Class 1/2/3 — renamed and swapped; (b) W₀/W₁/W₂ wrapping regimes — UNCHANGED; (c) Class A/B/C component-admissibility partition — UNCHANGED.

- **Track E surface-back of catalog citations (2026-05-22).** One Related Work entry added 2026-05-22 from Track E catalog at `ref/prior-art-analysis/05-directed-separation.md` (Pillar 4): hybrid deliberative/reactive architectures (Gat 1992, Simmons 1994, Au 2004) as prior art for class-coercion. Marked `[^cat-2026-05-22]` for verification-deferred attribution; primary-source verification queued in the BG2 cluster. The catalog citations had prior Pillar-style search support but were not verified by the current executor at landing time.

[^cat-2026-05-22]: Citation surfaced 2026-05-22 from the Track E catalog at `ref/prior-art-analysis/` (intermediate work artifacts that captured Pillar-style prior-art searches). Catalog has more verification support than raw Undermind synthesis but less than full primary-source reading. Verification queued with the BG2 cluster — see Working Notes above.
