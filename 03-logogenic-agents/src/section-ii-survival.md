---
slug: section-ii-survival
type: result
status: conditional
depends:
  - ai-agent-as-act-agent
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
| 3 | #value-object | Conditional expectations given $(M_t, \pi)$; agnostic to how $M_t$ was produced |
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

$$\text{Exact: } 16/24 \qquad \text{Approximate: } 5/24 \qquad \text{Modified: } 2/24 \qquad \text{Fails: } 1/24$$

### Structure of the approximate results

*[Derived (approximation-error-structure, from analysis of goal-information leakage)]*

For the five approximately surviving results, the fundamental error source is goal-information leaking into the epistemic update. The epistemic bias:

$$\Delta M_{\text{bias}} = f_X^M(X_{\tau^-}, e_\tau) - f_M(M_{\tau^-}, e_\tau)$$

where $f_X^M$ denotes the epistemic component of the coupled update. This bias is bounded (in expectation) by:

$$\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa_{\text{processing}} \cdot H(G_t \mid e_\tau, M_{\tau^-})$$

where $C$ is a domain-dependent constant. The bias is zero when $\kappa = 0$ (modular), maximal when $\kappa \approx 1$ and the goal state is highly informative given the event and prior model.

The impact of $\kappa$ on approximation quality is **modulated by observation ambiguity** — binary, verifiable observations carry minimal goal-conditioning bias regardless of $\kappa$. See #observation-ambiguity-modulation for the full treatment.

## Epistemic Status

*Conditional.* The classification is conditional on: (1) the segment-by-segment analysis of each result's dependency on directed separation (see `msc/spike-coupled-survival-analysis.md` for the full argument), and (2) the correctness of the underlying Section II results themselves. The "survives exactly" classifications are the strongest — they follow directly from verifying that the result's statement and derivation do not reference directed separation. The "survives approximately" classifications depend on the error bound, which uses the epistemic bias structure; the bound is informally derived (the constant $C$ is not computed) and is best treated as an order-of-magnitude characterization.

Max attainable: conditional. The classification's epistemic ceiling is determined by the underlying Section II results. If a Section II result is itself discussion-grade (e.g., #strategic-calibration), its survival classification inherits that status.

## Discussion

**Why the majority survives.** The survival rate (16/24 exact) reflects a structural property of AAD's design: Section II's *definitional architecture* — what states exist, how they decompose, what evaluation means, what the strategy represents — is about the *structure of purposeful agency*, not about the *processing architecture*. Directed separation is about how the state is *updated*, not about what the state *is*. Results that define objects ($V_{O_t}$, $\delta_{\text{sat}}$, $\delta_{\text{regret}}$, $\Sigma_t$ as DAG) or establish architectural requirements (causal hierarchy, interventional access) are processing-agnostic by construction.

**Where the damage is concentrated.** The five approximate results and two modified results all concern *dynamics* — how the state evolves, how edge credences are updated, how the orient cascade resolves, whether the strategy persists. These are precisely the results that depend on how the update factorizes. The pattern: *statics survive; dynamics degrade.*

**Implications for logogenic agent engineering.** An LLM agent system designer can rely on Section II's full conceptual architecture — objectives, strategy DAGs, satisfaction gaps, control regret, the 2x2 diagnostic — without modification. The engineering challenge is in the dynamics: ensuring that the coupled update produces accurate epistemic states (minimizing goal-conditioned bias), that the orient cascade ordering is followed as a reasoning discipline, and that strategy persistence is maintained across the 100% context turnover ( #context-turnover).

**The $\kappa^2$ result for strategy persistence.** The strategy persistence schema's sector parameter degrades as $O(\kappa^2)$, not $O(\kappa)$, because the bias must both enter the signal and survive the sector-condition averaging. This means Class 2 agents need faster correction rates — equivalently, they tolerate lower strategic disturbance rates — to achieve the same persistence guarantees. The squared dependence is a tighter result than the linear dependence of the other approximate results; it arises from the specific structure of the sector condition's inner-product averaging.

## Working Notes

- The classification counts #strategy-dag twice (once for the structure, which survives exactly, and once for the credence mechanism, which requires modification). The scorecard counts these as contributing to both categories. One could instead count #strategy-dag once as "survives approximately" (the weakest classification applying to any part of the result). The two-part count is more informative.
- The bound $\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa \cdot H(G_t \mid e_\tau, M_{\tau^-})$ deserves formal derivation. The constant $C$ relates information-theoretic coupling (in bits) to state-space error (in the norm on $\mathcal{M}$). This requires an assumption about the geometry of $\mathcal{M}$ — e.g., that $M_t$ is parameterized such that mutual information and state-space distance are locally proportional. Without this, the bound is order-of-magnitude guidance, not a theorem.
- The "fails" category contains only #directed-separation itself. One might argue this is not a "failure" but a "scope exit" — the result defines the boundary, and Class 2 agents are outside it. The classification is stated as "fails" for symmetry with the other categories, but the semantic content is "inapplicable by design."
