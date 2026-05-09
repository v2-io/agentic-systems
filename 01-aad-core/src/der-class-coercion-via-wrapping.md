---
slug: der-class-coercion-via-wrapping
type: derived
status: conditional
depends:
  - form-composition-closure
  - der-directed-separation
  - hyp-directed-separation-under-composition
  - def-agent-environment
  - deriv-sector-condition
  - result-sector-persistence-template
  - der-tempo-composition
stage: draft
---

# Derived: Class Coercion via Wrapping

A Class 2 (Partial) or Class 3 (Coupled) component (one whose forward pass entangles belief-update and goal-conditioning) can be embedded inside an external scaffold whose state $X_W = (M_W, G_W)$ is updated by structurally distinct query channels: **goal-blind queries** to the component update $M_W$; **goal-conditioned queries** update $G_W$. Under stated conditions on the component, directed separation holds at the wrapper level by construction, and the composite system is Class 1 (Separated) — even though the underlying component is not. This is the constructive direction of `#hyp-directed-separation-under-composition` for the wrapper-around-component special case: a procedure for *making* directed separation hold when the underlying component does not provide it.

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

### Wrapper-design constraints

For (A2)–(A4) of `#form-composition-closure` to hold at the wrapper level:

- **(D-A2)** The wrapper commits to a prediction map $\hat o_W : \mathcal X_M \times \mathcal A_W \to \mathcal O_W$ so that macro-mismatch $\delta_W = o_W - \hat o_W$ is well-defined.
- **(D-A3)** $f_M$ supports a gain interpretation per `#def-adaptive-tempo`. Holds for Tier-1 belief-update maps — Bayesian on exponential families, gradient on strongly convex losses, linear-PD with bounded gain. Tier-2/3 cases inherit the corresponding tier-restricted scope from `#deriv-sector-condition`.
- **(D-A4)** $f_M$ satisfies the sector condition with positive correction rate. Automatic for Tier-1 belief-update maps via `#deriv-sector-condition` Prop A.1 and `#der-gain-sector-bridge`.

(A1) holds by construction — $X_W = (M_W, G_W)$ has the AAD form because we *built it in*.

### Theorem 1: Class coercion (exact form)

*[Derived (class-coercion-exact, from C1+C2+C3 + D-A2/A3/A4)]*

Under (C1)–(C3) and (D-A2)–(D-A4), the wrapper $W$ satisfies (A1)–(A4) of `#form-composition-closure` at the wrapper level, and directed separation holds *exactly*:

$$P(M_{W,m+1} \mid M_{W,m},\ o_{W,m+1},\ G_{W,m}) = P(M_{W,m+1} \mid M_{W,m},\ o_{W,m+1})$$

Therefore $W$ is a Class 1 (Separated) architecture per `#der-directed-separation`.

*Proof.* (A1) by construction of the type signatures. (A2)–(A4) under (D-A2)–(D-A4) by direct verification using the inheritance from `#deriv-sector-condition` and `#def-adaptive-tempo`.

For directed separation: identify all paths from $G_{W,m}$ to $M_{W,m+1}$ given $(M_{W,m}, o_{W,m+1})$. The update is

$$M_{W,m+1} = f_M\big(M_{W,m},\, o_{W,m+1},\, q_M(M_{W,m}, o_{W,m+1}),\, A(q_M(M_{W,m}, o_{W,m+1}))\big)$$

$f_M$ has no $G_W$ argument by type signature (D-pathway-1 closed). $q_M$ has no $G_W$ argument by type signature (D-pathway-2 closed). The remaining pathway is $A(q_M)$ depending on $G_W$ given $q_M$. Under (C3), $P(A(q_M) \mid q_M, G_W) = P(A(q_M) \mid q_M)$ — the response is conditionally independent of $G_W$ given $q_M$. Since $q_M$ is itself a deterministic function of $(M_{W,m}, o_{W,m+1})$, conditioning on $(M_{W,m}, o_{W,m+1})$ determines $q_M$, and the integrand $P(M_{W,m+1} \mid M_{W,m}, o_{W,m+1}, q_M, A(q_M)) \cdot P(A(q_M) \mid q_M, G_W)$ no longer depends on $G_W$. The conditional distribution of $M_{W,m+1}$ given $(M_{W,m}, o_{W,m+1}, G_{W,m})$ equals that given $(M_{W,m}, o_{W,m+1})$. ∎

### Theorem 2: Class coercion (approximate form, C3 weakened to leakage bound)

*[Derived (class-coercion-approximate, from C1+C2+leakage-bound)]*

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

*Conditional* on (C1), (C2), (C3) (or its weakening to a leakage bound), and the wrapper-design constraints (D-A2), (D-A3), (D-A4). The proofs are short conditional-independence reasoning (Theorem 1) and a single application of the data-processing inequality (Theorem 2); both are standard. (D-A4) is automatic for Tier-1 belief-update maps; for Tier-2/3 belief-update maps the wrapper inherits the tier-restricted scope from `#deriv-sector-condition` and `#form-composition-closure`'s bridge-lemma classification.

Max attainable: derived under stated conditions. (C3)'s exact form is a structural ideal that pretrained components (notably LLMs with goal-rich training data) generally satisfy only approximately; the realistic regime is Theorem 2 with $\kappa$ characterized empirically.

The wrapping regime hierarchy (W₀/W₂/W₁) is a *formulation* — the partition is made by the structural choice of where to place the separation commitment. The leakage bounds within each regime are derived once the regime is fixed.

## Discussion

### Quality–separation tradeoff inside Class B

For Class-B components (admitting both goal-blind and goal-conditioned modes), the wrapper has a design choice: how aggressively to restrict $q_M$ to goal-blind content, vs. how much context to allow that may carry goal-correlated information. Maximally goal-blind queries (only the current observation, no context, no history) reduce the pretraining-induced leakage that bounds $\kappa_{W_1}$, but may produce information-poor responses that hurt $f_M$'s update quality. Maximally informed queries (full history, retrieved context) produce richer responses but increase the mutual information $I(q_M; G_W)$ and therefore the upper bound on $\kappa_{W_1}$. The tradeoff is real and resolved per application.

### Coercion-distance vs. tracking-distance

The closure-defect $\varepsilon^\ast$ in `#form-composition-closure` is read as a *fidelity* measure: how well the macro-system tracks the projected micro-system. In the wrapping construction, the wrapper deliberately changes the underlying component's behavior to enforce separation — we *want* the wrapper to differ from the unwrapped component in the goal-conditioning direction. Two distinct quantities are involved:

- $\varepsilon^\ast_{\text{track}}$ — the standard fidelity quantity from `#form-composition-closure`. Used in the bridge lemma to bound trajectory error.
- $\varepsilon^\ast_{\text{coerce}}$ — the wrapping-specific quantity measuring behavioral divergence between the wrapped system and the unwrapped component. Higher means more aggressive coercion.

For wrapper analyses: the persistence-template inheritance (below) uses $\varepsilon^\ast_{\text{track}}$. Cost-of-class-coercion analyses use $\varepsilon^\ast_{\text{coerce}}$. The leakage analysis uses $\kappa$ — a KL-divergence on response distributions, distinct from both trajectory-error quantities. Conflating them propagates downstream confusion.

### Tempo cost — a Brooks's-Law instance

The wrapper makes $K \geq 2$ component calls per macro-step (more in richer wrapper designs). If the component's nominal call rate is $\nu_A$, the wrapper-level macro-update rate is $\nu_W = \nu_A / K$. By `#der-tempo-composition`,

$$\mathcal T_W \leq \mathcal T_A^\text{nominal} - C_\text{coord}^\text{wrap}$$

where $C_\text{coord}^\text{wrap}$ is the coordination overhead specific to the wrapping construction — the tempo consumed by maintaining the wrapper's $(M_W, G_W)$ state separately from the component's internal state. This is the cost of class coercion paid in tempo: the same Brooks's-Law form whose general statement is in `#der-tempo-composition`. Adding state-management infrastructure reduces realized external tempo even when the underlying component's compute rate is unchanged.

### Inheritance of the persistence template

Under (D-A4), the wrapper inherits `#result-sector-persistence-template` at the wrapper level: persistence holds when $\alpha_W R_W \gt \rho_W$. The wrapper-level effective disturbance has two contributions: external environmental disturbance $\rho_\text{ext}$ acting through $o_W$, and internal disturbance from the component's response variance, $\rho_\text{int}$, bounded by the variance of $A$'s responses to goal-blind queries. Total: $\rho_W = \rho_\text{ext} + \rho_\text{int}$. Persistence at the wrapper level requires $\alpha_W R_W \gt \rho_\text{ext} + \rho_\text{int}$.

### Form-preservation reading

Read in form-preservation language, (A1)–(A4) of `#form-composition-closure` are the requirement that AAD's form survive coarse-graining: macro must itself be AAD. The wrapping construction is the *constructive* version — when the underlying component doesn't preserve form on its own (Class 2 (Partial) or Class 3 (Coupled)), the wrapper enforces form-preservation at the macro level by structural commitment of the type signatures. The closure-defect $\varepsilon^\ast$ then plays the role of distance from the form-preserved fixed point in the constructive setup.

### Component-admissibility partition

Class A components (goal-blind by design) satisfy (C1) trivially and don't need wrapping in the substantive sense — wrapping for Class A is organizational rather than structural. Class B components (LLMs, hybrid RL with separable value/policy, multi-modal models) are the substantive wrapping case — the wrapper *chooses* to use the goal-blind mode. Class C components (pure end-to-end goal-conditioned policy networks) fail (C1) and are scope-out for the basic theorem. Salvage paths for Class C — null-goal queries, goal-uniform averaging, auxiliary distilled goal-blind heads — exist but cost something (information loss, computation, training).

### Resolution of the LLM scope question

The "Class 3 (Coupled) exit" framing — *directed separation violated by goal-conditioned agents (LLMs); handled as architectural scope, not approximation* — is refined by this segment from a scope exit to a constructive route through. Class 3 (Coupled) LLMs are scope-in *for the wrapper construction* (under Class-B admissibility). The cost is paid in tempo (Brooks's-Law form), in residual coercion-distance, and in a structural leakage rate $\kappa_{W_1}$ bounded by pretraining-distribution mutual information. Whether this construction yields an operationally useful agent depends on how favorable the pretraining-distribution-induced bounds are for the application.

### Relationship to `#hyp-directed-separation-under-composition`

The hypothesis is descriptive — when does directed separation hold under composition? This segment provides the constructive answer for the wrapper-around-component special case: directed separation holds whenever the wrapper's type signatures are respected and (C1)–(C3) hold (or their weakenings). The general N-agent composition question remains a hypothesis; the wrapper-around-component case is now derived.

## Findings

### Constructive Class Coercion via Wrapping

**Brief:** When you have a component (like an LLM) whose belief-update and goal-conditioning are entangled in a single forward pass, you can build a scaffold around it that maintains explicit, separate stores for what the system believes and what it wants. The structural rule is that belief updates only see queries to the component that don't include the goal as input; goal updates can see the goal. Under reasonable conditions on the component, the wrapped system is goal-blind in its belief updates *by construction* — even though the underlying component isn't. The cost shows up as more component calls per cycle (so the wrapped system runs slower) and a residual leakage from the component's pretraining (the component might still infer the goal from query content, even when the goal isn't explicit in the input). Two practical regimes appear: strict wrapping with separate goal-blind and goal-conditioned calls (theoretically clean, operationally expensive), and partial wrapping with one goal-conditioned call whose response is parsed into separate update fields (operationally common, theoretically only behaviorally bounded).

**Impact:** Promotes `#hyp-directed-separation-under-composition` to derived (in the wrapper-around-component special case). Refines the Class 1 (Separated) cell of `#der-directed-separation` with a structural-vs-behavioral sub-distinction (W₁ vs. W₂). Resolves the LLM scope question — Class 3 (Coupled) components are scope-in for the wrapper construction at a measurable cost, not scope-out. Connects Section I/II's modular-agent machinery to logogenic-substrate work in `03-logogenic-agents/` cleanly: PROPRIUM's auxilia hierarchy is the candidate constructive realization of W₁, and the agentic-tft cognitive-loop-spec's CONTEXTUALIZE-then-CHOOSE phase separation is the temporally-staged form. Inherits `#result-sector-persistence-template` and `#der-tempo-composition` at the wrapper level — the wrapper's persistence and tempo are governed by AAD's existing machinery, with the cost of class coercion paid in the Brooks's-Law tempo overhead.

**Novelty Claim:** *Claim integration* of POMDP / cognitive-architecture / MDP-homomorphism prior art with the AAD machinery (sector-Lyapunov persistence template, Brooks's-Law tempo accounting, Class 1/2/3 (Separated/Partial/Coupled) directed-separation taxonomy) plus the W₀/W₂/W₁ regime hierarchy that surfaces the structural-vs-behavioral leakage distinction and the LLM-specific (C1)–(C3) admissibility/leakage conditions. The wrapping move itself is rediscovery of patterns established in POMDP theory (Bayesian belief-update is goal-blind by construction) and cognitive architectures (modular agent design with separated belief/goal/action state, four decades). AAD's contribution is the synthesis with its own machinery and the explicit regime hierarchy.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| Goal-blind belief-update by construction | Astrom 1965, "Optimal control of Markov processes with incomplete state information," *J. Math. Anal. Appl.* 10; Kaelbling, Littman, Cassandra 1998, "Planning and acting in partially observable stochastic domains," *Artificial Intelligence* 101 | *formal antecedent* — POMDP belief-state filters are goal-blind by construction; the wrapping move recapitulates this in the AAD vocabulary. The closest formal prior art for the directed-separation guarantee. |
| Modular agent design with separated belief/goal/action | Newell 1990, *Unified Theories of Cognition*; Laird 2012, *The Soar Cognitive Architecture*; Anderson 2007, *How Can the Human Mind Occur in the Physical Universe?*; Sun 2016 *Anatomy of the Mind* (CLARION); Baars 1988 *A Cognitive Theory of Consciousness* / Dehaene 2014 *Consciousness and the Brain* (Global Workspace) | *formal antecedent* — cognitive architectures have done modular agent design with separated belief/goal/action state for 40+ years. The W₁ wrapping move is essentially the per-cycle commitment that cognitive architectures make at the system level. |
| Predictive-loss bounds under coarse-graining of MDPs | Ravindran-Barto 2004, "An algebraic approach to abstraction in reinforcement learning"; Taylor, Precup, Panangaden 2008, "Bounding performance loss in approximate MDP homomorphisms," NeurIPS; Abel, Hershkowitz, Littman 2016, "Near optimal behavior via approximate state abstraction," ICML; Subramanian, Sinha, Seraj, Mahajan 2020, "Approximate information state for approximate planning," arXiv:2010.08843; Congeduti, Mey, Oliehoek 2020, "Loss bounds for approximate influence-based abstraction," arXiv:2011.01788 | *adjacent literature* — control-theoretic predictive-loss bounds. AAD connects to this cluster via `#form-composition-closure`'s bridge lemma at the wrapper level. |
| Compositional structure for nested agents | Smithe 2024, "Structured Active Inference," arXiv:2406.07577; Capucci, Gavranović, Hedges, Rischel 2022, "Towards foundations of categorical cybernetics," ACT 2021 | *adjacent literature* — categorical / lens framing of compositional agents. The wrapper construction is consistent with the lens framing; an alternative reading in categorical-systems-theory terms is available. |
| Form-preservation under coarse-graining | Friston 2019 *J. Theor. Biol.*, "On Markov blankets and hierarchical self-organisation"; Friston, Heins, Verbelen, Da Costa et al. 2025 *Front. Network Physiology*, "From pixels to planning: scale-free active inference" | *adjacent literature* — Friston's framing of the renormalization group as form-conservation under coarse-graining. The wrapping construction reads as a constructive form-preservation move. |
| IB-Lagrangian semigroup composition | Mehta, Schwab 2014, "An exact mapping between the Variational Renormalization Group and Deep Learning," arXiv:1410.3831; Kline, Palmer 2022, "Gaussian Information Bottleneck and the Non-Perturbative Renormalization Group," PMC8967309 | *adjacent literature* — IB-as-RG. The wrapper's (P1) information-preservation condition (from `#form-composition-closure`) is IB-shaped; the semigroup composition rule is the closest analog of "AAD form preserved under iterated wrapping." |
| Singular-perturbation as unified RG | Chen, Goldenfeld, Oono 1996, "Renormalization group and singular perturbations," *Phys. Rev. E* 54:376; Chiba 2009, SIAM J. Appl. Dyn. Syst. 8:1066 | *formal antecedent* — RG framework subsumes singular perturbation theory. The $K_c \gg 1$ timescale-separation regime in `#form-composition-closure` invokes this for free. |
| Tool-using language-model agent frameworks | Yao et al. 2022, "ReAct: Synergizing reasoning and acting in language models"; Shinn et al. 2023, "Reflexion: language agents with verbal reinforcement learning"; Park et al. 2023, "Generative Agents: Interactive Simulacra of Human Behavior"; Packer et al. 2023, "MemGPT: Towards LLMs as operating systems"; Schick et al. 2023, "Toolformer: language models can teach themselves to use tools" | *empirical instantiation* — practical wrappers around language-model substrates. Most fall in W₂ (partial wrapping / output-structuring); Generative Agents' observation→memory step is the closest empirical instance of W₁. AAD's regime hierarchy gives these constructions a structural reading. |

**Search Log:**

- 2026-05-09 (*targeted*): Web + training-data search across POMDP / cognitive-architecture / MDP-homomorphism / hierarchical-control / Constitutional-AI / categorical-systems-theory / scaffolded-LLM / FEP-RG / IB-RG / singular-perturbation-RG threads. Verdict: **substantial overlap** with the POMDP and cognitive-architecture lines as the closest formal prior art. AAD's contribution is integration with its own machinery rather than novelty in the wrapping move itself.
- 2026-05-09 (*intuition-only*, prior to the targeted search): adjacent literatures expected to host prior art were active inference (Markov blankets), control theory (approximate simulation), and scaffolded-LLM frameworks. The targeted search confirmed all three and added the POMDP and cognitive-architecture lines as the formal precedents the intuition didn't surface as load-bearing.

## Working Notes

- **Detailed tempo accounting for canonical wrapper architectures.** $C_\text{coord}^\text{wrap}$ for ReAct-shape, Reflexion-shape, PROPRIUM-shape wrappers is an empirically-relevant computation deferred from this segment's promotion. The general bound (Brooks's-Law form via `#der-tempo-composition`) is established here; specific architectural breakdowns are follow-on.
- **Empirical $\kappa$ measurement.** $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$ is computable for any component with stochastic outputs by sampling responses under multiple goal-conditioning histories and estimating the divergence. For a fixed component, this bound is a property of the wrapper's choice of $q_M$ — narrower queries reduce the bound, richer queries increase it. The empirical instantiation is open follow-on.
- **Compositional wrapping (wrapper-of-wrapper).** How leakage rates compose under iterated wrapping is open. Conjecture: additive in KL ($\kappa_{\text{outer}} \le \kappa_{\text{inner}} + \kappa_{\text{outer-shell}}$) by data-processing inequality applied at each level, but tightness is unclear.
- **Behavioral compliance axiom for W₂.** $\kappa_{W_2}$ has no structural bound; it depends on the component's instruction-following fidelity. Whether a behavioral-compliance axiom (assuming the component honestly attempts to follow structural-separation instructions) yields a bound is an open hypothesis. If so, it would be hypothesis-grade rather than derived.
- **Identifying the regime in the wild.** Practical scaffolded-LLM frameworks (ReAct, Reflexion, MemGPT, etc.) almost universally implement W₂. Distinguishing W₂ from W₁ in a deployed system requires inspection of the per-cycle query structure — does $f_M$'s update path receive a query that contains $G_W$ or not? This is the diagnostic question.
- **Connection to ELI-specific structure in `04-eli/`.** Most ELI-specific content (sovereignty axes, accountability infrastructure, identity factors, substrate-independence) is *added structure* beyond what class coercion provides — the wrapper construction is the substrate; ELI work is what happens on top of it.
- Reasoning-trail provenance: spike directories at `spikes/class-coercion-wrapping/` and `spikes/temporal-nesting-rg/` carry the working-out of these results and the form-preservation framing context. Per `feedback_spike_references_only_in_working_notes.md`, this Working Notes pointer is the only spike reference; the segment's substantive content is self-contained.

- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Three independent axes in this segment: (a) GUC Class 1/2/3 — renamed and swapped; (b) W₀/W₁/W₂ wrapping regimes — UNCHANGED (subscript numerals are regime identifiers, not GUC class labels); (c) Class A/B/C component-admissibility partition — UNCHANGED (admissibility-class letters are from the (C1) condition, not GUC class labels). The W₀ row "Raw Class-3 component" (old vocab) → "Raw Class 2 (Partial) or Class 3 (Coupled) component" — expanded to cover the full union since old vocab was ambiguous here. "Class 2 exit" → "Class 3 (Coupled) exit"; "Class-3 LLMs" (old vocab, was internally inconsistent since LLMs are fully merged) → "Class 3 (Coupled) LLMs" (post-rename is now semantically correct). Removed at `candidate` stage per FORMAT.md Gate 4.
