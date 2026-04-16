---
slug: strategy-complexity-cost
type: formulation
status: discussion-grade
depends:
  - strategic-tempo
  - information-bottleneck
  - explicit-strategy-condition
  - chain-confidence-decay
  - structural-change-as-parametric-limit
stage: draft
---

# Formulation: Cognitive Cost of Strategy

The complexity cost of maintaining an explicit strategy $\Sigma_t$, formulated via minimum description length and the information bottleneck principle --- connecting DAG structure to the maintenance term $C_{\text{maintain}}$ in the explicit strategy condition ( #explicit-strategy-condition).

## Formal Expression

### Strategy description length

*[Formulation (strategy-description-length)]*

The minimum description length of a strategy DAG $\Sigma_t = (V, E, p, \gamma)$ ( #strategy-dag) decomposes as:

$$\operatorname{DL}(\Sigma_t) = \operatorname{DL}_{\text{struct}}(G) + \operatorname{DL}_{\text{param}}(p \mid G)$$

where:
- $\operatorname{DL}_{\text{struct}}(G)$: bits to encode the DAG topology --- node identities, edge connectivity, AND/OR labels $\gamma$. Scales as $O(\lvert E\rvert \log \lvert V\rvert)$ for sparse DAGs.
- $\operatorname{DL}_{\text{param}}(p \mid G)$: bits to encode the edge credences given the topology. For Beta-distributed credences, each edge requires $O(\log n_{ij})$ bits where $n_{ij} = \alpha_{ij} + \beta_{ij}$ is the effective sample size.

The total scales as $O(\lvert E\rvert \log \lvert V\rvert)$ for moderate-precision credences, growing linearly in the number of edges and logarithmically in the number of nodes.

### Strategy IB objective

*[Formulation (strategy-IB-objective)]*

The optimal strategy complexity balances parsimony against decision-relevance, by analogy with #information-bottleneck's compression-prediction trade-off for $M_t$:

$$\Sigma_t^\ast = \arg\min_{\Sigma_t} \left[\operatorname{DL}(\Sigma_t) - \beta_\Sigma \cdot I(\Sigma_t;\, \pi^\ast \mid M_t)\right]$$

where:
- $\operatorname{DL}(\Sigma_t)$: description length (complexity cost)
- $I(\Sigma_t;\, \pi^\ast \mid M_t)$: mutual information between the strategy and the optimal policy, conditioned on the current model --- how much the strategy helps the agent choose good actions beyond what the model already provides
- $\beta_\Sigma \gt 0$: trade-off parameter analogous to #information-bottleneck's $\beta$

When $\beta_\Sigma$ is low (high maintenance cost relative to decision value), the agent prefers simple strategies. When $\beta_\Sigma$ is high (strategy is cheap to maintain relative to its decision value), the agent can afford complex plans. The explicit strategy condition ( #explicit-strategy-condition) is the binary threshold: $\beta_\Sigma$ large enough that *any* $\Sigma_t$ is worth maintaining.

### Maximum useful chain depth

*[Derived (Conditional on Beta-Bernoulli, per-edge persistence)]*

From #strategic-tempo's per-edge persistence condition, an AND-chain of depth $d$ with per-edge observation rate $\nu$, true success probability $\theta$ per edge, and effective sample size $n$ per edge persists only if the deepest edge satisfies:

$$\nu \cdot \theta^{d-1} \cdot \frac{1}{n+1} \gt \frac{\rho_\Sigma}{R_\Sigma}$$

Solving for the maximum depth at which persistence is achievable:

$$d^\ast = 1 + \left\lfloor \frac{\log\bigl(\frac{\nu}{(n+1)\rho_\Sigma / R_\Sigma}\bigr)}{\log(1/\theta)} \right\rfloor$$

When $\nu / ((n+1)\rho_\Sigma / R_\Sigma) \leq 1$, even $d = 1$ fails --- the agent cannot maintain a single edge under these conditions.

**Interpretation.** Beyond depth $d^\ast$, evidence starvation makes edges uncorrectable faster than the environment invalidates them. The agent accumulates strategic mismatch on deep edges regardless of how fast it acts at the top of the chain.

**Quantitative illustration** ($\theta = 0.8$, $\nu = 1$):

| $n$ | $\rho_\Sigma / R_\Sigma$ | $d^\ast$ |
|-----|--------------------------|----------|
| 10 | 0.01 | 10 |
| 10 | 0.1 | 0 |
| 100 | 0.01 | 5 |
| 100 | 0.1 | 0 |

High evidence requirements ($n$ large) and volatile environments ($\rho_\Sigma / R_\Sigma$ large) severely limit useful chain depth.

### Triple depth penalty

Deep AND-chains suffer three independent penalties that compound:

1. **Confidence decay** ( #chain-confidence-decay): aggregate confidence $\prod p_k$ decays geometrically with depth. The plan is *less likely to succeed*.
2. **Evidence starvation** ( #strategic-dynamics-derivation): effective observation rate $\nu_k = \nu \cdot \prod_{j \lt k}\theta_j$ decays geometrically. The plan is *harder to calibrate*.
3. **Cognitive cost** (this segment): each additional depth level adds $O(\log \lvert V\rvert)$ bits to description length. The plan is *more expensive to maintain*.

All three are multiplicative in depth, making deep sequential strategies exponentially costly along three independent dimensions.

### Enriched explicit strategy condition

*[Formulation (enriched-strategy-condition)]*

The maintenance cost $C_{\text{maintain}}$ from #explicit-strategy-condition decomposes as:

$$C_{\text{maintain}} = C_{\text{represent}} + C_{\text{revise}} + C_{\text{monitor}}$$

where:
- $C_{\text{represent}} \propto \operatorname{DL}(\Sigma_t)$: cognitive cost of holding the strategy in working memory (proportional to description length)
- $C_{\text{revise}} \propto \sum_{(i,j)} \nu_{ij} \cdot c_{\text{update}}$: cost of processing edge updates (proportional to strategic tempo $\mathcal T_\Sigma$ times per-update cost)
- $C_{\text{monitor}} \propto \lvert\{(i,j) : \iota_{ij} \lt 1\}\rvert$: cost of monitoring edges with partial identifiability (the agent must do extra causal reasoning for non-trivial edges)

This decomposition makes the #explicit-strategy-condition's maintenance term concrete: each component maps to a quantity defined elsewhere in the theory.

### Complexity compression operations

*[Discussion (complexity-compression)]*

The IB objective suggests three compression operations, corresponding to structural changes from #structural-change-as-parametric-limit:

1. **Edge pruning** (operation 3 in #structural-change-as-parametric-limit): remove edges with $\eta_{\text{edge},ij} \cdot I_{\text{edge},ij} \lt c_{\text{bit}}$, where $I_{\text{edge},ij}$ is the decision-relevance of that edge and $c_{\text{bit}}$ is the per-bit maintenance cost. Edges that contribute less decision value than their representational cost are candidates for removal.
2. **Node merging** (reducing $\lvert V\rvert$): collapse intermediate nodes that serve no decision-distinguishing function. This reduces $\operatorname{DL}_{\text{struct}}$ by a factor proportional to the reduction in $\lvert V\rvert$.
3. **Depth truncation** at $d^\ast$: prune all edges beyond the maximum useful depth. This is not optimization but necessity --- edges beyond $d^\ast$ cannot maintain bounded mismatch.

## Epistemic Status

The description length formulation is a *formulation* --- it applies standard MDL to the strategy DAG, which is a representational choice not a derived necessity. The IB objective is *formulation/discussion-grade* --- it names the right trade-off by analogy with #information-bottleneck but the mutual information term $I(\Sigma_t;\, \pi^\ast \mid M_t)$ is not operationalized. The maximum useful depth $d^\ast$ is *derived* conditional on Beta-Bernoulli dynamics and the per-edge persistence condition from #strategic-tempo. The triple depth penalty is an *observation* combining results from three independent segments. The enriched maintenance decomposition is *formulation*. The compression operations are *discussion-grade*.

Max attainable: conditional. The DL formulation is standard; the IB objective and compression operations would require empirical validation or formal optimality proofs to advance beyond discussion-grade. The depth bound could reach exact status for specific edge models.

## Discussion

**Connection to #explicit-strategy-condition.** The enriched maintenance decomposition gives the cost inequality quantitative content: an agent can now *compute* whether a proposed strategy is worth maintaining by estimating its description length, revision cost, and monitoring burden, and comparing against the exploration/repair cost of operating without it.

**LLM context windows as DL constraint.** For language-constituted agents ( `03-logogenic-agents/`), the strategy must fit in the context window. A context window of $W$ tokens imposes $\operatorname{DL}(\Sigma_t) \leq W \cdot \log_2(\lvert\text{vocab}\rvert)$ as a hard constraint. This makes the IB trade-off non-optional: the agent *must* compress its strategy, and the depth bound $d^\ast$ becomes a context-window-limited quantity. A 128K-token context window may support a 500-edge DAG encoded in natural language; a 4K-token window may support only a 15-edge sketch.

**Computational compression from interaction horizon (Miller 2022).** The maximum useful depth $d^\ast$ derived above constrains complexity from the *maintenance* side (evidence starvation). Miller (2022, *Ex Machina*, Table 12.2) provides a complementary constraint from the *interaction* side: the number of interaction rounds compresses the space of behaviorally distinguishable strategies regardless of the agent's internal complexity. For Moore machines with binary actions:

| Agent states | Unique computations | After 1 round | After 2 rounds | After 4 rounds |
|---|---|---|---|---|
| 1 | 2 | 2 | 2 | 2 |
| 2 | 26 | 2 | 8 | 26 |
| 3 | 1,054 | 2 | 8 | 690 |
| 4 | 57,068 | 2 | 8 | 5,936 |

The pattern: $\text{effective complexity} = \min(\text{agent complexity}, \text{interaction-horizon complexity})$. With only one round, even a four-state machine (57,068 unique computations) reduces to two distinguishable behaviors — equivalent to a one-state machine. With two rounds, all machines with two or more states reduce to eight distinguishable behaviors. The interaction horizon compresses the strategy space from above, just as the maintenance cost and evidence starvation compress it from below. For ACT's strategy DAG, the analog: a complex $\Sigma_t$ whose edges are only tested over a short horizon gains nothing from its depth — the untested structure is indistinguishable from a simpler strategy. This reinforces the $d^\ast$ bound and provides empirical grounding beyond the Beta-Bernoulli derivation.

**Strategy simplification pressure.** The triple depth penalty creates systematic pressure toward shallow, wide (OR-heavy) strategies over deep, sequential (AND-heavy) ones. This aligns with the structural pressure identified in #chain-confidence-decay's Discussion, now grounded in three independent mechanisms rather than one.

## Working Notes

- **Mixed topologies.** The depth bound $d^\ast$ assumes uniform AND-chains. Mixed AND/OR DAGs have heterogeneous depth penalties: OR-nodes reset the evidence-starvation clock (each alternative is tested independently), while AND-nodes compound it. The effective depth for computing $d^\ast$ may be the longest AND-chain in the DAG, not the total graph depth.
- **Optimal topology.** Given a fixed DL budget and action rate $\nu$, what DAG topology maximizes decision-relevant information $I(\Sigma_t;\, \pi^\ast \mid M_t)$? This is a combinatorial optimization over graph structures --- likely NP-hard in general but potentially tractable for specific graph families (trees, bounded treewidth).
- **Dynamic complexity.** As edges converge (high $n_{ij}$), their per-edge $\eta_{\text{edge},ij}$ shrinks, but their description length $\operatorname{DL}_{\text{param}}$ grows (more bits to encode the precise credence). The IB objective would favor *dropping* converged edges (they contribute little decision-relevant information since the agent already acts correctly on them), replacing them with a default "high confidence" summary. This is a principled version of "stop tracking what you already know."
- **Stochastic $\mathcal T_\Sigma$.** If strategic disturbance follows Model S (stochastic) rather than Model D (deterministic), the steady-state mismatch scales as $\rho_\Sigma / \sqrt{\mathcal T_\Sigma}$ rather than $\rho_\Sigma / \mathcal T_\Sigma$. The depth bound $d^\ast$ would change accordingly. Not yet derived.
