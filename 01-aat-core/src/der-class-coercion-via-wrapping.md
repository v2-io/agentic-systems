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

The result requires conditions on the component. **(C1) Goal-blind admissibility** — the component admits non-trivial goal-blind queries; the framework partitions components into *Class A* (goal-blind by design: POMDP belief-state filters, world models, sensory pipelines, retrieval systems), *Class B* (admit a goal-blind query mode alongside goal-conditioned ones: LLMs in summarization/fact-extraction modes, hybrid RL with separable value/policy), and *Class C* (fundamentally goal-conditioned: pure end-to-end goal-conditioned policy networks), with the construction applying to Classes A and B. **(C2) Stationary component conditional** — the component's output distribution conditional on input is fixed during operation (adaptation-during-deployment systems are out of scope). **(C2′) No goal-correlated cross-call state** — the component carries no information about the latent operator goal across the goal-blind / goal-conditioned call boundary; this is the condition on which the *structural* W₁ leakage bound depends. **(C3) No implicit goal-inference** — the component's response to a goal-blind query does not depend on $G_W$ via inference from query patterns; for pretrained components like LLMs, (C3) holds *exactly* only when query content is statistically independent of $G_W$ in the pretraining distribution. The framework supplies **two theorems**: an *exact* form under (C1)–(C3), and an *approximate* form under (C1)–(C2) plus a KL-leakage bound, where the wrapper-level leakage on $M_W$ updates is bounded by the same bound (small leakage in, small leakage out via the data-processing inequality).

The construction supports three **wrapping regimes** of decreasing strictness, distinguished by where structural separation lives. **W₁ (strict wrapping)** uses separate $q_M$ and $q_G$ calls per macro-step; separation lives at the *query boundary* and the residual leakage is the *selection-channel* quantity $\kappa_{W_1}^{\text{sel}} = I(A(q_M); G^{\text{op}}) \le I(q_M; G^{\text{op}})$ — bounded *structurally* by the goal-content of the wrapper's query-selection policy (under (C1)+(C2′)). **W₂ (partial wrapping)** uses one goal-conditioned call per macro-step with a typed parsed response routing updates to $M_W$ vs $G_W$ slots; separation lives at the *write boundary* and leakage is bounded only *behaviorally* — by the component's compliance with the prompted instruction-to-separate. **W₀ (no wrapping)** runs the raw Class 2 / Class 3 component with no separation commitment. What differs across the regimes is *what determines* the leakage rate — and, for W₁, whether the structural bound is available at all: it requires (C2′), failing which W₁ too degrades to a behavioral bound (`#disc-w1-structural-bound-boundary`). The hierarchy refines the Class 1 (Separated) cell of `#der-directed-separation` with a *Class-1-by-structure* (W₁ or natively goal-blind) vs *Class-1-by-behavior* (W₂) sub-distinction.

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

**(C2′) No goal-correlated cross-call state.** The component's hidden state does not carry information about the latent operator goal $G^{\text{op}}$ across the boundary between the goal-blind ($q_M$) and goal-conditioned ($q_G$) calls of a macro-step. Equivalently, $A$'s response to $q_M$ is conditionally independent of $G^{\text{op}}$ given $q_M$ and the component's *pre-call* state, and that pre-call state is itself goal-uncorrelated — either reset across the call boundary, or stripped of $\Sigma$- and $G$-content. (C2′) is the condition on which the *structural* W₁ leakage bound below depends, and it strengthens (C2): the breaking condition for the structural bound is not online weight-adaptation but mere goal-correlated state persistence across the call boundary — which a frozen-weights LLM with a conversation cache exhibits with no weight adaptation at all. When (C2′) fails the structural bound is unavailable and only a behavioral bound remains; this boundary is derived in `#disc-w1-structural-bound-boundary`.

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

### The W₁ structural leakage bound: a selection-channel quantity

The residual goal-leakage that survives in the W₁ regime is a *selection-channel* quantity, not a processing-channel one. The distinction is between two senses of the goal variable: the wrapper's internal purposeful-state register $G_W$ — which $q_M$ structurally does not take as an argument and which Theorem 1 closes by type signature — and the latent *operator goal* $G^{\text{op}}$ that generated the situation the wrapper is in, which a competent component can infer from the *content* of the query the wrapper chose. The processing channel ($G_W \to A(q_M) \mid q_M$) is shut structurally and exactly by Theorem 1; the entire residual leakage is the selection channel ($G^{\text{op}} \to$ wrapper history $\to$ choice of $q_M \to A(q_M)$), and its magnitude is governed by the goal-content carried in the query the wrapper selects.

*[Derived (W1-selection-leakage-bound, from C1+C2′, data-processing inequality)]*

Under (C1) and (C2′), the goal-information reaching the wrapper's belief update through the goal-blind channel is bounded by the goal-content of the wrapper's query-selection policy:

$$\kappa_{W_1}^{\text{sel}} \;:=\; I\big(A(q_M);\, G^{\text{op}}\big) \;\le\; I\big(q_M;\, G^{\text{op}}\big),$$

where $G^{\text{op}}$ is the latent operator goal and $q_M$ is the (random, history-dependent) goal-blind query drawn under the wrapper's operating policy.

*Derivation.* Under (C2′), $A(q_M)$ depends on $G^{\text{op}}$ only through $q_M$ — there is no goal-correlated cross-call state through which the goal could reach the response while bypassing the query — so $G^{\text{op}} \to q_M \to A(q_M)$ is a Markov chain. The data-processing inequality along this chain gives $I(A(q_M); G^{\text{op}}) \le I(q_M; G^{\text{op}})$. ∎

The bound is a property of the wrapper's $q_M$-selection policy, not of the component's input–output law, and is therefore design-controllable: maximally goal-blind queries (current observation only, no history, no system prompt) drive $I(q_M; G^{\text{op}}) \to 0$ and recover exact directed separation on the merits; richer, history-laden queries raise $I(q_M; G^{\text{op}})$ and with it the leakage ceiling. This is the formal content of the quality–separation tradeoff (§Discussion) — a choice of query-selection policy purchases a quantitative, structurally-derived leakage ceiling.

Propagating to the wrapper's belief state: the update $M_{W,m+1}$ is a deterministic function of $(M_{W,m}, o_{W,m+1}, q_M, A(q_M))$, so along $G^{\text{op}} \to q_M \to (q_M, A(q_M)) \to M_{W,m+1}$ the data-processing inequality gives

$$I\big(M_{W,m+1};\, G^{\text{op}} \,\big\vert\, M_{W,m},\, o_{W,m+1}\big) \;\le\; I\big(A(q_M);\, G^{\text{op}} \,\big\vert\, M_{W,m},\, o_{W,m+1}\big) \;\le\; I\big(q_M;\, G^{\text{op}}\big).$$

The conditioning set is $(M_{W,m}, o_{W,m+1})$ — deliberately *not* $q_M$. Conditioning on $q_M$ would (correctly, for the closed processing path) zero the quantity out and miss the selection leak; the unconditional $\kappa_{W_1}^{\text{sel}} = I(A(q_M); G^{\text{op}}) \le I(q_M; G^{\text{op}})$ is the analyst-independent statement, with $q_M$ drawn under the wrapper's actual operating policy.

### Wrapping regime hierarchy

The construction supports three regimes, distinguished by where structural separation lives:

| Regime | Construction | Leakage bound | Leakage source |
|---|---|---|---|
| **W₀** (no wrapping) | Raw Class 2 (Partial) or Class 3 (Coupled) component | $\kappa_{W_0}$ at the component's maximum goal-conditioning sensitivity | No constraint |
| **W₂** (partial wrapping) | One goal-conditioned call per macro-step; structurally typed parsed response routes updates to $M_W$ vs. $G_W$ slots | $\kappa_{W_2}$ bounded *behaviorally* — by the component's compliance with the prompted instruction-to-separate; **no structural bound** | Component's instruction-following fidelity |
| **W₁** (strict wrapping) | Theorem 1 / 2 — separate $q_M$ and $q_G$ calls per macro-step | $\kappa_{W_1}^{\text{sel}} = I(A(q_M); G^{\text{op}}) \le I(q_M; G^{\text{op}})$ — bounded *structurally* by the goal-content of the wrapper's query-selection policy (under (C1)+(C2′)) | Query-selection policy's goal-content (the goal $G^{\text{op}}$ inferable from query content) |

W₁ admits a structural bound — the selection-channel quantity $\kappa_{W_1}^{\text{sel}} = I(A(q_M); G^{\text{op}}) \le I(q_M; G^{\text{op}})$ under (C1)+(C2′); W₂ admits only a behavioral bound from the component's compliance fidelity. The two are different in kind — the structural bound is a property of the wrapper's query-selection policy (the goal-content of the queries it chooses) and is therefore design-controllable; the behavioral bound depends on the component's training and prompt-following. The W₁ structural bound is available exactly when the component carries no goal-correlated cross-call state ((C2′)); when (C2′) fails the leak routes through an unobservable channel and W₁ too degrades to a behavioral bound — the boundary derived in `#disc-w1-structural-bound-boundary`.

The W₀ / W₂ / W₁ distinction refines the Class 1 (Separated) cell of `#der-directed-separation`: within Class 1 (Separated), **Class-1-by-structure** (natively goal-blind components, or W₁ wrapping) has a structurally derivable directed-separation guarantee; **Class-1-by-behavior** (W₂ wrapping) has only an empirically estimable guarantee that depends on the component's instruction-following.

## Epistemic Status

*Conditional* on (C1), (C2), and (C3) (or its weakening to a leakage bound). The proofs are short conditional-independence reasoning (Theorem 1) and a single application of the data-processing inequality (Theorem 2); both are standard.

The W₁ structural leakage bound $\kappa_{W_1}^{\text{sel}} = I(A(q_M); G^{\text{op}}) \le I(q_M; G^{\text{op}})$ is *conditional* on (C1) and (C2′). The data-processing step is standard; the load-bearing condition is (C2′) — the Markov chain $G^{\text{op}} \to q_M \to A(q_M)$ holds only when the component carries no goal-correlated state across the call boundary. The bound is an upper bound; its gap below $I(q_M; G^{\text{op}})$ is the "accuracy effect" of §Discussion "Two senses of component competence" and is not characterized here (Working Notes).

Max attainable: derived under stated conditions. (C3)'s exact form is a structural ideal that pretrained components (notably LLMs with goal-rich training data) generally satisfy only approximately; the realistic regime is Theorem 2 with $\kappa$ characterized empirically. (C2′)'s exact form is likewise an ideal — a frozen-weights LLM with a conversation cache violates it without any weight adaptation — and where it fails only the behavioral bound of `#disc-w1-structural-bound-boundary` survives.

The wrapping regime hierarchy (W₀/W₂/W₁) is a *formulation* — the partition is made by the structural choice of where to place the separation commitment. The leakage bounds within each regime are derived once the regime is fixed.

## Discussion

### Quality–separation tradeoff inside Class B

For Class-B components (admitting both goal-blind and goal-conditioned modes), the wrapper has a design choice: how aggressively to restrict $q_M$ to goal-blind content, vs. how much context to allow that may carry goal-correlated information. Maximally goal-blind queries (only the current observation, no context, no history) drive the selection-channel mutual information $I(q_M; G^{\text{op}})$ — and with it the leakage ceiling $\kappa_{W_1}^{\text{sel}}$ — toward zero, but may produce information-poor responses that hurt $f_M$'s update quality. Maximally informed queries (full history, retrieved context) produce richer responses but raise $I(q_M; G^{\text{op}})$ and therefore the upper bound on $\kappa_{W_1}^{\text{sel}}$. The tradeoff is real and resolved per application — and because $I(q_M; G^{\text{op}})$ is a property of the query-selection policy the wrapper controls, the tradeoff is a design dial, not a property of the component.

### Component-admissibility partition

Class A components (goal-blind by design) satisfy (C1) trivially and don't need wrapping in the substantive sense — wrapping for Class A is organizational rather than structural. Class B components (LLMs, hybrid RL with separable value/policy, multi-modal models) are the substantive wrapping case — the wrapper *chooses* to use the goal-blind mode. Class C components (pure end-to-end goal-conditioned policy networks) fail (C1) and are scope-out for the basic theorem. Salvage paths for Class C — null-goal queries, goal-uniform averaging, auxiliary distilled goal-blind heads — exist but cost something (information loss, computation, training).

### Resolution of the LLM scope question

The "Class 3 (Coupled) exit" framing — *directed separation violated by goal-conditioned agents (LLMs); handled as architectural scope, not approximation* — is refined by this segment from a scope exit to a constructive route through. Class 3 (Coupled) LLMs are scope-in *for the wrapper construction* (under Class-B admissibility). The cost is paid in residual leakage rate $\kappa_{W_1}^{\text{sel}}$ bounded by the goal-content of the wrapper's query-selection policy, $I(q_M; G^{\text{op}})$; the tempo cost is established separately in `#der-class-coercion-in-composition`. Whether this construction yields an operationally useful agent depends on how low the query-selection policy can drive $I(q_M; G^{\text{op}})$ while still licensing useful belief updates — and, where the component carries goal-correlated cross-call state, on whether (C2′) can be enforced at all (`#disc-w1-structural-bound-boundary`).

### Relationship to `#hyp-directed-separation-under-composition`

The hypothesis is descriptive — when does directed separation hold under composition? This segment provides the constructive answer for the wrapper-around-component special case: directed separation holds whenever the wrapper's type signatures are respected and (C1)–(C3) hold (or their weakenings). The general N-agent composition question remains a hypothesis; the wrapper-around-component case is now derived.

### Wrapping as a truthification mechanism

The wrapping construction is the *rigorous formal version* of what `#disc-adversarial-coupling-pressure` §"Defensive scaffolding as composition" gestures at informally — peer review, prediction registers, double-entry bookkeeping, adversarial procedure, structured red-teaming. Those external scaffolds are operational mechanisms for *increasing* the modularity of a composite agent in the face of forces that would couple it; the wrapping construction is the structural version of the same operation applied internally rather than externally. Both share the discipline: a goal-blind belief-update query path is structurally enforced (W₁ strict) or behaviorally bounded (W₂), at a definite cost (extra component calls per macro-step plus residual leakage rate). The W₀/W₂/W₁ regime hierarchy is the *graded* characterization of how thoroughly the truthification has been applied — W₀ is the un-truthified base state, W₂ behavioral truthification, W₁ structural truthification. Cross-reference: `#disc-modularity-state-dynamics` is the meta-segment in which the truthification operation sits as one of three operations on the modularity state — alongside strategic self-coupling ( `#disc-strategic-self-coupling`, self-driven-decreasing) and adversarial coupling pressure ( `#disc-adversarial-coupling-pressure`, externally-driven-decreasing). This segment is the canonical *formal* instance of the truthification operation at the component level (W₀ / W₁ / W₂ regime hierarchy), paired with the composite-level *defensive-scaffolding* instance from `#disc-adversarial-coupling-pressure` §"Defensive scaffolding as composition". The connection is also surfaced in `#impl-composition-machinery` §"Class-coercion as truthification mechanism."

### Two senses of component competence: world-simulation vs goal-extraction

A subtle decomposition of *component competence* matters for how (C3) and the selection-channel bound $\kappa_{W_1}^{\text{sel}} = I(A(q_M); G^{\text{op}}) \le I(q_M; G^{\text{op}})$ scale with the component's capability. A high-capability component has at least two distinct competences that the classification machinery treats asymmetrically:

1. **World-simulation fidelity** — accuracy of $A$'s response to the explicit content of a query, including counterfactual content. Sharpens $f_M$'s update quality once a query is in hand.
2. **Input-structure extraction** — competence at inferring latent structure *from the query's surface form*, including inferring the operator's goal $G^{\text{op}}$ from query patterns. This is the channel (C3) names.

The architectural classification of `#der-directed-separation` is *blind to (1) and defined by (2)*: class membership turns on whether the goal can causally reach $f_M$, not on how accurately $f_M$ then computes given goal-blind input. For pretrained components the two competences correlate empirically — the same training that produces world-simulation fidelity also produces input-structure extraction — but conceptually they are distinct, and the distinction is load-bearing for (C3).

The two competences act on the two sides of the selection-channel bound. The bound's *ceiling* is $I(q_M; G^{\text{op}})$ — the goal-content present in the query, fixed by the wrapper's selection policy; the *realized* leak is $I(A(q_M); G^{\text{op}})$ — how much of that the response actually carries. The gap between them is governed by competence:

- *Accuracy effect (widens the gap, lowers the realized leak).* A more competent world-simulator returns posteriors closer to the true conditional $P(\cdot \mid q_M)$, which is goal-independent by definition; it leaves the goal-content sitting *in* $q_M$ unexploited in its response, so $I(A(q_M); G^{\text{op}})$ can sit well below the ceiling $I(q_M; G^{\text{op}})$.
- *Inference effect (closes the gap, raises the realized leak).* A more competent input-structure extractor uses any query-content / goal-content correlation to infer $G^{\text{op}}$ from the goal-blind query and bend its response accordingly, driving $I(A(q_M); G^{\text{op}})$ up toward the ceiling — even when no goal argument is structurally exposed.

For pretrained components where the two competences scale together (the typical case for LLMs trained on goal-rich corpora), where the realized leak sits between $0$ and the ceiling in the fidelity limit is *empirical and component-specific*, not structural. The selection-channel ceiling is design-controllable (drive $I(q_M; G^{\text{op}})$ down by goal-blind query selection); the position within that ceiling is the accuracy-vs-inference balance, and separating the two appears to open more science than it closes.

Several lines worth pulling, kept open here rather than queued elsewhere so future cycles do not lose them:

- *Decorrelation by construction.* If world-simulation and input-structure extraction can be structurally decoupled at training time — by architectural separation of *what does the world look like given $q$* from *what is the latent context that produced $q$* — a Class 3 (Coupled) component could satisfy (C3) even at high world-simulation fidelity. The classification would then refine into "Class 3 but C3-respecting" vs "Class 3 and C3-violating" sub-cases that the current scalar $\kappa_{W_1}$ does not surface, and the C3-respecting branch may be a more interesting design target than wrapping a C3-violating component.
- *Counterfactual capability is bi-side.* Counterfactual simulation (Pearl Level 2) requires both competences — accurate world-simulation under interventional queries *and* extraction of the intervention's intended scope from the query. Whether high counterfactual capability tends to raise or lower realized $\kappa$ in practice is an open empirical question; the answer depends on how the two competences decompose in the specific component.
- *Decomposed empirical estimator.* The existing $\hat\kappa_{\text{processing}}$ estimator from `#der-directed-separation` probes the *net* response divergence under varied goal-priming. An estimator that holds explicit query content fixed while varying only the implicit operator context might isolate the inference-effect contribution, giving a sharper diagnostic than the aggregate $\kappa$ and surfacing whether a given high-fidelity component sits near $\kappa \to 0$ (accuracy-dominated) or near $\kappa$ ceiling (inference-dominated).
- *M4 amplification specificity.* The amplification of `#disc-modularity-state-dynamics` operations (strategic self-coupling, adversarial coupling pressure) under high component fidelity may track competence (2) specifically rather than competence (1). If so, M4 attack-surface measurement could be sharpened by measuring the inference effect rather than aggregate capability — a more competent world-simulator is not, *by that fact alone*, a more potent vector for the coupling-increasing operations.

The decomposition is named here at *discussion-grade* recognition — kept open as a place to pull on rather than as a closed result. Whether it lifts to *robust qualitative* or higher depends on whether the two competences can be operationalized as separately measurable quantities and whether the architectural-decorrelation conjecture holds for any realizable training regime.

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
| Hybrid deliberative/reactive architectures (prior art for class-coercion) | Gat 1992, *Integrating planning and reacting in a heterogeneous asynchronous architecture for controlling real-world mobile robots* (AAAI)[^cat-2026-05-22]; Simmons 1994, *Structured control for autonomous robots* (IEEE Trans. Robotics 10:34)[^cat-2026-05-22]; Au 2004, planner wrappers with external-query management[^cat-2026-05-22] | *formal antecedent* — hybrid deliberative/reactive architectures orchestrate reactive (entangled) layers beneath deliberative (separated) planners, structurally precedent for the wrapping construction's "scaffold an entangled component to recover separated behaviour at the wrapper level" move. AAT's contribution is *not* the wrapping move itself but the *theorem-shaped* wrapper-level directed-separation guarantee (Theorem 1 + Theorem 2) plus the explicit selection-channel leakage bound $\kappa_{W_1}^{\text{sel}} = I(A(q_M); G^{\text{op}}) \le I(q_M; G^{\text{op}})$ and the Brooks's-Law tempo cost in `#der-class-coercion-in-composition` |

**Search Log:**

- 2026-05-09 (*targeted*): Web + training-data search across POMDP / cognitive-architecture / scaffolded-LLM threads. Verdict: **substantial overlap** with the POMDP and cognitive-architecture lines as the closest formal prior art. AAT's contribution is the structural-leakage analysis and regime hierarchy rather than novelty in the wrapping move itself.
- 2026-05-09 (*intuition-only*, prior to the targeted search): adjacent literatures expected to host prior art were active inference (Markov blankets), control theory (approximate simulation), and scaffolded-LLM frameworks. The targeted search confirmed all three and added the POMDP and cognitive-architecture lines as the formal precedents.

## Working Notes

- **Empirical $\kappa$ measurement.** The selection-channel ceiling $I(q_M; G^{\text{op}})$ is estimable by varying the latent operator goal across a fixed query-selection policy and measuring the divergence of the resulting query distribution; the realized leak $I(A(q_M); G^{\text{op}})$ requires sampling responses under varied $G^{\text{op}}$ at fixed selection policy. Both need an operationalization of the latent $G^{\text{op}}$ — likely the same construct the $\hat\kappa_{\text{processing}}$ estimator of `#der-directed-separation` uses. For a fixed component, the ceiling is a property of the wrapper's $q_M$-selection policy — narrower (more goal-blind) queries reduce it, richer queries raise it. The empirical instantiation, and a characterization of the gap between realized leak and ceiling (the accuracy effect), is open follow-on; see also the decomposed-estimator spike candidate below.
- **Sub-type-aware wrapping regime selection.** Knowing only that a component is Class 2 (Partial) is insufficient to choose W₁ vs W₂; the right regime depends on the un-wrapped component's coupling *form* per the (stage × source × form) sub-typology of `#disc-partial-coupling-pathways`: content-form sub-types admit W₂ (post-hoc response structuring); process-form sub-types require W₁ (structural goal-blind query path) or are not coercible to Class 1 without pipeline access. Additionally, $\Sigma_t$-source coupling (per `#der-belief-strategy-attractor`) can undermine W₁'s structural commitment via strategy-context leakage in stateful components — even with no $G_W$ in the query, the component's internal $\Sigma$ may be influenced by historical query content and then suppress the gain on subsequent goal-blind queries; a $\Sigma$-channel-suppressed W₁ (holding strategic context fixed across calls, or stripping $\Sigma$-content from queries) may be required. The W₀/W₁/W₂ hierarchy is the agent-level analog of the stage-level form distinction in the sub-typology — W₂ ↔ content; W₁ ↔ process-with-pipeline-access — making the structure-vs-behavior refinement at Class 1 the agent-level shadow of a Class 2 axis.
- **Compositional wrapping (wrapper-of-wrapper).** How leakage rates compose under iterated wrapping is open. Conjecture: additive in KL ($\kappa_{\text{outer}} \le \kappa_{\text{inner}} + \kappa_{\text{outer-shell}}$) by data-processing inequality applied at each level, but tightness is unclear.
- **Behavioral compliance axiom for W₂.** $\kappa_{W_2}$ has no structural bound; it depends on the component's instruction-following fidelity. Whether a behavioral-compliance axiom (assuming the component honestly attempts to follow structural-separation instructions) yields a bound is an open hypothesis. If so, it would be hypothesis-grade rather than derived.
- **Identifying the regime in the wild.** Practical scaffolded-LLM frameworks (ReAct, Reflexion, MemGPT, etc.) almost universally implement W₂. Distinguishing W₂ from W₁ in a deployed system requires inspection of the per-cycle query structure — does $f_M$'s update path receive a query that contains $G_W$ or not? This is the diagnostic question.
- **Segment split provenance (2026-05-11).** This segment was bifurcated from a combined "class coercion" derivation. Claim A (directed separation at the wrapper level) lives here; Claim B (wrapper as valid AAT composite agent — (A1)–(A4) verification, persistence-template inheritance, Brooks's-Law tempo cost) lives in `#der-class-coercion-in-composition` (which declares this segment as prerequisite). The split reflects FORMAT.md Gate 1 discipline: this segment's depends list (`der-directed-separation`, `def-agent-environment`) reflects exactly what the directed-separation theorem actually requires. The composition-level dependencies (`form-composition-closure`, `deriv-sector-condition`, `result-sector-persistence-template`, `der-tempo-composition`) are Claim B's load and now live with Claim B.
- Reasoning-trail provenance: spike directories at `spikes/class-coercion-wrapping/` and `spikes/temporal-nesting-rg/` carry the working-out of these results.
- **W₁ leakage-bound correction provenance (history layer).** The W₁ structural leakage bound previously carried in the body was $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$ — a circular and vacuous quantity (it bounds $\kappa$ by an average of $\kappa$, and evaluates identically to zero for the stateless oracle the theorem models, because conditioning on $q_M$ closes the only channel it measures). The strengthen-first correction relocated the goal variable from the wrapper register $G_W$ to the latent operator goal $G^{\text{op}}$ read off query content, and dropped the conditioning, yielding the present selection-channel bound $\kappa_{W_1}^{\text{sel}} = I(A(q_M); G^{\text{op}}) \le I(q_M; G^{\text{op}})$ (data-processing along $G^{\text{op}} \to q_M \to A(q_M)$ under (C1)+(C2′)). The embedded no-go — structural bound available iff (C2′) holds, otherwise behavioral-only — landed as `#disc-w1-structural-bound-boundary`. Full reasoning trail: `spikes/spike-w1-leakage-vacuity-2026-05-31.md` (the correction + the no-go); `spikes/spike-w1-w2-boundary-intuition-2026-05-31.md` (the certifiability-discontinuity framing and exact-enumeration toy).
- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Three independent axes in this segment: (a) GUC Class 1/2/3 — renamed and swapped; (b) W₀/W₁/W₂ wrapping regimes — UNCHANGED; (c) Class A/B/C component-admissibility partition — UNCHANGED.

- **Track E surface-back of catalog citations (2026-05-22).** One Related Work entry added 2026-05-22 from Track E catalog at `ref/prior-art-analysis/05-directed-separation.md` (Pillar 4): hybrid deliberative/reactive architectures (Gat 1992, Simmons 1994, Au 2004) as prior art for class-coercion. Marked `[^cat-2026-05-22]` for verification-deferred attribution; primary-source verification queued in the BG2 cluster. The catalog citations had prior Pillar-style search support but were not verified by the current executor at landing time.

- **Spike candidate (PROPOSED Tier 3, 2026-05-28): Decomposed empirical estimator separating accuracy-dominated from inference-dominated $\kappa$ regimes.** The aggregate $\hat\kappa_{\text{processing}}$ estimator of `#der-directed-separation` probes net response divergence under varied goal-priming. A decomposed estimator that holds explicit query content fixed while varying only implicit operator context (system-prompt scaffolding, query metadata, conversational history) might isolate the inference-effect contribution from the accuracy-effect contribution — surfacing whether a given high-fidelity component sits near $\kappa \to 0$ (accuracy-dominated) or near a $\kappa$ ceiling (inference-dominated). Substance home: §Discussion "Two senses of component competence: world-simulation vs goal-extraction". → [PROPOSED Tier 3](../../spikes/PROPOSED.md).

- **Spike candidate (PROPOSED Tier 2, 2026-05-28): Decorrelation-by-construction — Class 3 but C3-respecting sub-cases.** Architectural-research question: can world-simulation fidelity and input-structure extraction be structurally decoupled at training time (training-objective decomposition; architectural separation of *what does the world look like given $q$* from *what is the latent context that produced $q$*; data-curation discipline)? If so, a Class 3 (Coupled) component could satisfy (C3) at high world-simulation fidelity, and the architectural classification of `#der-directed-separation` would refine into "Class 3 but C3-respecting" vs "Class 3 and C3-violating" sub-cases that the scalar $\kappa_{W_1}$ does not currently surface — the C3-respecting branch may be a more interesting design target than wrapping a C3-violating component. Theory-edge / speculative; substance home: §Discussion "Two senses of component competence: world-simulation vs goal-extraction". → [PROPOSED Tier 2](../../spikes/PROPOSED.md).

[^cat-2026-05-22]: Citation surfaced 2026-05-22 from the Track E catalog at `ref/prior-art-analysis/` (intermediate work artifacts that captured Pillar-style prior-art searches). Catalog has more verification support than raw Undermind synthesis but less than full primary-source reading. Verification queued with the BG2 cluster — see Working Notes above.

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs. **Coverage:** only one dir reached a digested reflection on this segment (526815) — the deeply-mathematical critique pass; the other contributing dirs stopped before this segment. **No pedagogical / analogy / figure gold surfaced here** — 526815's reflection is entirely *certified-track correctness findings* (the F127–F131 cluster on the leakage analysis), which are routed to the findings track, not lifted as Working-Notes gold. The one durable non-finding signal worth preserving for the later Brief/Discussion pass:

#### Belongs elsewhere / convergence signal

- **Auditor flagged the $\varepsilon_{\text{track}}$ / $\varepsilon_{\text{coerce}}$ / $\kappa$ distinction as a contribution to preserve** — "the distinction … is excellent and should be preserved downstream" (Codex/Claude, AUDIT-WORKING-526815, "Watch"). A signal about which of this segment's apparatus a fresh reader found most load-bearing; useful when the leakage analysis is eventually given Brief-field plain-language framing.

> Off-ramp note: 526815 also raised a substantive *structural* challenge to the W₁ leakage bound — that $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$ is identically zero for a stateless component under exact conditioning on $q_M$, so the bound as stated may not measure the leakage it intends (the real channels being query-content correlation, hidden component state, conversation history). This was a strengthen-first / correctness matter for the chapter's load-bearing construction, **not** Working-Notes gold — flagged in the lift report for the findings/adjudication track. **Resolved** via the strengthen-first spike: the bound was replaced by the selection-channel quantity $\kappa_{W_1}^{\text{sel}} = I(A(q_M); G^{\text{op}}) \le I(q_M; G^{\text{op}})$ and the embedded no-go landed as `#disc-w1-structural-bound-boundary` (see the W₁ leakage-bound correction provenance note above).
