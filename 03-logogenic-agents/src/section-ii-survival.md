---
slug: section-ii-survival
type: result
status: conditional
depends:
  - scope-logogenic-agent
  - coupled-update-dynamics
  - directed-separation
  - complete-agent-state
  - agent-spectrum
  - objective-functional
  - value-object
  - strategy-dimension
  - causal-hierarchy-requirement
  - loop-interventional-access
  - ciy-observational-proxy
  - ciy-unified-objective
  - explicit-strategy-condition
  - chain-confidence-decay
  - and-or-scope
  - strategy-dag
  - satisfaction-gap
  - control-regret
  - strategic-calibration
  - orient-cascade
  - observability-dominance
  - edge-update-via-gain
  - edge-update-causal-validity
  - credit-assignment-boundary
  - structural-change-as-parametric-limit
  - strategy-persistence-schema
stage: draft
---

# Result: Section II Survival Classification

Of Section II's 24 results, 16 survive exactly for Class 2 (fully merged) agents, 5 survive approximately with bounded error, 2 require modification, and 1 fails by definition. The damage from dropping directed separation is concentrated in the *processing dynamics* — the ordering of updates and the accuracy of individual update steps — not in the *definitional and structural* architecture.

## Formal Expression

*[Derived (section-ii-survival, from segment-by-segment analysis of directed-separation dependency)]*

### Classification

Each Section II result is classified by whether its statement or derivation references directed separation, and if so, whether the result can be recovered in the coupled formulation.

**SURVIVES EXACTLY (16):** The result does not reference directed separation in its statement or derivation. It holds for any agent with $X_t = (M_t, G_t)$, regardless of how the update factorizes.

| # | Segment | Rationale |
|---|---------|-----------|
| 1 | #agent-spectrum | Classifies by what information is maintained, not how it is processed |
| 2 | #objective-functional | Defines evaluation interface $V_{O_t}$; no processing dependency |
| 3 | #value-object (definitions only) | $V_O$ and $Q_O$ as conditional expectations are agnostic to how $M_t$ was produced. **Partial.** The *causal-validity* claim — that $Q_O$ depends on $M_t$ alone as a state variable — is conditional on directed separation ( #value-object Epistemic Status) and degrades for Class 2 agents because $M_t$ carries goal-conditioned bias. Definitions survive exactly; the causal-validity layer does not. Count this as half-exact, half-approximate. |
| 4 | #strategy-dimension | Structural decomposition $G_t = (O_t, \Sigma_t)$; definitional, not dynamic |
| 5 | #causal-hierarchy-requirement | Evaluating $Q_O$ requires Level 2 queries; property of the question type, not the processing |
| 6 | #loop-interventional-access | The feedback loop provides interventional data by construction; architecture-independent |
| 7 | #ciy-observational-proxy | Admissibility regimes (A/B/C) are domain properties, not agent-architecture properties |
| 8 | #ciy-unified-objective | Policy objective structure (exploit + explore) exists for any learning agent |
| 9 | #explicit-strategy-condition | Cost comparison $C_{\text{plan}} + C_{\text{maintain}} \lt C_{\text{explore}} + C_{\text{repair}}$ is architecture-independent |
| 10 | #chain-confidence-decay | $\log P(\text{chain}) = \sum_i \log P(E_i \mid E_{\lt i})$ — mathematical identity |
| 11 | #and-or-scope | Scope restriction on strategy representation; constrains $\Sigma_t$, not $f_M$ |
| 12 | #satisfaction-gap | Definition: $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O(M_t; \Pi, N_h)$; computed from $(M_t, V_{O_t})$ regardless of provenance |
| 13 | #control-regret | Definition: $\delta_{\text{regret}} = A_O - V_O(M_t, \pi_{\text{current}}; N_h)$; same reasoning |
| 14 | #observability-dominance | When $\sigma_v \approx 0$, $\eta_{\text{edge}} \to 0$; information-channel property |
| 15 | #edge-update-causal-validity | Conditions (C1-C3) and regimes (A/B/C) are domain/interface properties |
| 16 | #credit-assignment-boundary | DAG inference structure; "persistence is credit-assignment-free" (Prop B.5) holds for Class 2 |

Additionally, the DAG *structure* of #strategy-dag (acyclicity, propositional nodes, AND/OR combination, status propagation) survives exactly — these are properties of the strategy representation, not of the processing architecture.

**SURVIVES APPROXIMATELY (5):** The result's statement is exact under directed separation and becomes an approximation when directed separation fails, with error depending on $\kappa_{\text{processing}}$.

| # | Segment | Source of approximation | Error structure |
|---|---------|------------------------|-----------------|
| 1 | #complete-agent-state | Factorized update dynamics | $\lVert f_X - (f_M, f_G \circ f_M)\rVert = O(\kappa)$; at $\kappa \approx 1$ the factored form is not useful |
| 2 | #strategic-calibration | Residual conflated with $M_t$ bias from goal-conditioning | $b_{ij} = O(\kappa \cdot \text{ambiguity}(e_\tau))$; see #observation-ambiguity-modulation |
| 3 | #edge-update-via-gain | Signal function is goal-conditioned | Gain formula's form is robust; magnitude biased by $O(\kappa \cdot \text{goal-evidence correlation})$ |
| 4 | #strategy-persistence-schema | Sector parameter degraded by goal-conditioned signals | $\alpha_\Sigma^{\text{eff}} \leq \alpha_\Sigma - O(\kappa^2)$; persistence threshold harder to satisfy |
| 5 | #strategy-dag (credence conditioning) | Leaf and edge credences conditioned on full $X_t$ rather than $M_t$ alone | Credences may exhibit goal-dependent bias; see below |

**REQUIRES MODIFICATION (2):**

| # | Segment | What changes |
|---|---------|-------------|
| 1 | #orient-cascade | Sequential ordering derived from unidirectional information dependency → replaced by coupled resolution with post-hoc diagnostic decomposition. Ordering survives as normative design pattern, not derived result. See #coupled-diagnostic-framework. |
| 2 | #strategy-dag (credence mechanism) | Leaf credences $p_v(M_t) \to p_v(X_t)$; edge credences $p_{ij}(M_t) \to p_{ij}(X_t)$. Credences become explicitly conditioned on the full state, reflecting goal-dependent assessment. |

**FAILS (1):**

| # | Segment | Reason |
|---|---------|--------|
| 1 | #directed-separation | This is the result that defines the Class 2 boundary. It fails by construction for fully merged agents. |

### Scorecard

$$\text{Exact: } 15.5/24 \qquad \text{Approximate: } 5.5/24 \qquad \text{Modified: } 2/24 \qquad \text{Fails: } 1/24$$

**Note on the fractional counts.** #value-object is counted as half-exact (its definitions survive) and half-approximate (its causal-validity layer is conditional on directed separation and degrades for Class 2 agents). Most segments split cleanly into one category; #value-object does not. The scorecard's total stays at 24 to match the segment count but the fractional count acknowledges that a clean integer bucketing understates the qualitative complexity for segments whose definitions and dynamics live at different tier levels.

### Structure of the approximate results

*[Derived (approximation-error-structure, from analysis of goal-information leakage)]*

For the five approximately surviving results, the fundamental error source is goal-information leaking into the epistemic update. The epistemic bias:

$$\Delta M_{\text{bias}} = f_X^M(X_{\tau^-}, e_\tau) - f_M(M_{\tau^-}, e_\tau)$$

where $f_X^M$ denotes the epistemic component of the coupled update. This bias is bounded (in expectation) by the mutual-information form derived in #observation-ambiguity-modulation (equation at line 43):

$$\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa_{\text{eff}}(e_\tau) \cdot H(\Omega_\tau \mid e_\tau, M_{\tau^-}) = C \cdot \kappa_{\text{processing}} \cdot I(G;\, \Omega_\tau \mid e_\tau, M_{\tau^-})$$

where $C$ is a domain-dependent constant and $\kappa_{\text{eff}}(e_\tau) = \kappa_{\text{processing}} \cdot \mathcal{A}(e_\tau)$. This is a strict refinement of the coarser form $C \cdot \kappa_{\text{processing}} \cdot H(G_t \mid e_\tau, M_{\tau^-})$, since $I(G;\Omega_\tau \mid e_\tau, M_{\tau^-}) \leq H(G_t \mid e_\tau, M_{\tau^-})$: only the portion of the residual world-state uncertainty that is *goal-resolvable given the observation* can be channeled into epistemic bias. The bias is zero when $\kappa = 0$ (modular), zero when $\mathcal{A}(e_\tau) = 0$ (the observation's residual uncertainty is goal-neutral or absent), and maximal when $\kappa \approx 1$ *and* the observation is interpretively goal-resolvable.

The impact of $\kappa$ on approximation quality is therefore **modulated by observation ambiguity** — binary, verifiable observations carry minimal goal-conditioning bias regardless of $\kappa$. See #observation-ambiguity-modulation for the full treatment, including the definition of $\mathcal{A}(e_\tau)$ and the operationalization of $\hat{\mathcal{A}}$.

## Epistemic Status

*Conditional.* The classification is conditional on: (1) the segment-by-segment analysis of each result's dependency on directed separation, and (2) the correctness of the underlying Section II results themselves. The "survives exactly" classifications are the strongest — they follow directly from verifying that the result's statement and derivation do not reference directed separation. The "survives approximately" classifications depend on the error bound, which uses the epistemic bias structure. Since 2026-04-24 the bound's constant $C$ is derived under named sub-scopes in [#bias-bound-derivation](../../01-aad-core/src/bias-bound-derivation.md) — Track 1 (transport-inequality, linear in $I$, $C_{W_2}^2 = 2L_{\text{post}}^2/\rho_{\text{LSI}}$) and Track 2 (Fisher-Rao under (PI)+Čencov, $\sqrt I$ scaling, universal $C_{FR} = \sqrt 2$). The "survives approximately" classifications therefore upgrade from "order-of-magnitude characterization" to conditional theorem within the Track 1 / Track 2 sub-scopes; outside those sub-scopes the order-of-magnitude reading remains the correct epistemic tier.

Max attainable: conditional. The classification's epistemic ceiling is determined by the underlying Section II results. If a Section II result is itself discussion-grade (e.g., #strategic-calibration), its survival classification inherits that status.

## Discussion

**Why the majority survives.** The survival rate (16/24 exact) reflects a structural property of AAD's design: Section II's *definitional architecture* — what states exist, how they decompose, what evaluation means, what the strategy represents — is about the *structure of purposeful agency*, not about the *processing architecture*. Directed separation is about how the state is *updated*, not about what the state *is*. Results that define objects ($V_{O_t}$, $\delta_{\text{sat}}$, $\delta_{\text{regret}}$, $\Sigma_t$ as DAG) or establish architectural requirements (causal hierarchy, interventional access) are processing-agnostic by construction.

**Where the damage is concentrated.** The five approximate results and two modified results all concern *dynamics* — how the state evolves, how edge credences are updated, how the orient cascade resolves, whether the strategy persists. These are precisely the results that depend on how the update factorizes. The pattern: *statics survive; dynamics degrade.*

**Implications for logogenic agent engineering.** The 16/24 exact-survival count is a *statement-level* result: these results' formal claims do not invoke directed separation, so their definitions and structural classifications carry over to Class 2 agents. This is not the same as *operational extractability* — the claim that an LLM agent system designer can *compute* these quantities at runtime without additional machinery. Operational extractability requires separate instrumentation: the satisfaction gap $\delta_{\text{sat}}$ is formally well-defined for a Class 2 agent, but computing it requires that $V_{O_t}^{\min}$ and $A_O$ actually be available to the agent's reasoning loop. For LLM-based agents this generally means explicit instrumentation beyond the agent's internal state — commit messages, PR descriptions, structured reasoning traces, external monitoring streams — that materialize the quantities the theory references. #scope-logogenic-agent discusses this distinction as the mapping from LLM interaction to AAD's formal objects; #coupled-update-dynamics treats the identification $X_t = (M_t, G_t)$ as approximate and analytical rather than computable. The instrumentation-boundary framing in `02-tst-core/`'s `#software-epistemic-properties` P5 is the parallel observation in the software domain: statement-level survival does not imply that the quantities are cheap or automatic to extract.

So: Section II's *conceptual architecture* applies to Class 2 agents (16/24 exact survival is a claim about this), but Section II's *operational deployment* on Class 2 agents requires additional instrumentation whose design is the subject of `03-logogenic-agents/` more broadly. The engineering challenge is therefore two-part: (a) minimizing goal-conditioned bias in the coupled update so the inherited structural results remain quantitatively accurate, and (b) instrumenting the agent system so the results' quantities are computable at all. The second is not a failure of the theory; it is the work the theory identifies as necessary for its application.

**The $\kappa^2$ result for strategy persistence.** The strategy persistence schema's sector parameter degrades as $O(\kappa^2)$, not $O(\kappa)$, because the bias must both enter the signal and survive the sector-condition averaging. This means Class 2 agents need faster correction rates — equivalently, they tolerate lower strategic disturbance rates — to achieve the same persistence guarantees. The squared dependence is a tighter result than the linear dependence of the other approximate results; it arises from the specific structure of the sector condition's inner-product averaging.

## Working Notes

- The classification counts #strategy-dag twice (once for the structure, which survives exactly, and once for the credence mechanism, which requires modification). The scorecard counts these as contributing to both categories. One could instead count #strategy-dag once as "survives approximately" (the weakest classification applying to any part of the result). The two-part count is more informative.
- The bound $\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa_{\text{processing}} \cdot I(G;\Omega_\tau \mid e_\tau, M_{\tau^-})$ (the tighter MI form now primary, per #observation-ambiguity-modulation and the 2026-04-21 Finding B resolution). **Constant $C$ derived 2026-04-24** in [#bias-bound-derivation](../../01-aad-core/src/bias-bound-derivation.md) under two named sub-scopes: Track 1 gives $C_{W_2}^2 = 2L_{\text{post}}^2/\rho_{\text{LSI}}$ linear in $I$ under LSI + Lipschitz-posterior regularity; Track 2 gives universal dimension-free $C_{FR} = \sqrt 2$ under (PI)+Čencov + small-information regime. A no-go result in the appendix shows universal $C$ in Euclidean-parameter norm does not exist — the (PI) axiom is load-bearing for the derivation, not coincidental. Bound epistemic tier: *conditional (exact under Track 1 hypotheses H1-H3 or Track 2 hypotheses H1+H4)*, replacing the earlier "order-of-magnitude guidance" caveat. The assumption-about-geometry-of-$\mathcal M$ the earlier formulation required is now discharged by the (PI) adoption in [#scope-agent-identity](../../01-aad-core/src/scope-agent-identity.md) (fourth primary instance of [#discussion-additive-coordinate-forcing](../../01-aad-core/src/discussion-additive-coordinate-forcing.md)).
- The "fails" category contains only #directed-separation itself. One might argue this is not a "failure" but a "scope exit" — the result defines the boundary, and Class 2 agents are outside it. The classification is stated as "fails" for symmetry with the other categories, but the semantic content is "inapplicable by design."
