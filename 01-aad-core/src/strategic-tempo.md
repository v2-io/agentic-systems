---
slug: strategic-tempo
type: definition
status: conditional
depends:
  - adaptive-tempo
  - edge-update-via-gain
  - strategy-dag
  - edge-update-causal-validity
  - strategic-dynamics-derivation
stage: draft
---

# Definition: Strategic Tempo

The effective rate at which an agent acquires useful revisions to its strategy $\Sigma_t$ --- the sum of per-edge correction capacities across the strategy DAG.

## Formal Expression

*[Definition (strategic-tempo)]*

$$\mathcal T_\Sigma = \sum_{(i,j) \in E} \nu_{ij} \cdot \eta_{\text{edge},ij}$$

where:
- $(i,j)$ indexes the edges of the strategy DAG ( #strategy-dag)
- $\nu_{ij}$ is the effective observation rate for edge $(i,j)$ --- how often the agent obtains evidence about the causal link $i \to j$
- $\eta_{\text{edge},ij}$ is the per-edge update gain ( #edge-update-via-gain)

**Parallel with epistemic tempo.** The definition mirrors #adaptive-tempo's $\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$, replacing observation channels with strategy edges and epistemic gain with edge gain. The structural parallel is exact: both are sums of (rate $\times$ quality) products over correction channels.

**Key difference: endogenous edge rates.** Epistemic tempo's channel rates $\nu^{(k)}$ are largely exogenous --- the environment generates observations at its own pace. Strategic tempo's edge rates $\nu_{ij}$ are *endogenous*: they depend on the agent's action policy (which edges get tested) and on upstream success (downstream edges are tested only when upstream edges fire). This endogeneity is the source of the structural differences between epistemic and strategic persistence.

### Consistency verification

The definition is consistent with the four verified topologies from #strategic-dynamics-derivation:

**Case B.1 (single edge $A \to G$).** One edge, $\nu = \nu_{AG}$, $\eta_{\text{edge}} = 1/(n+1)$. $\mathcal T_\Sigma = \nu_{AG}/(n+1)$. The sector parameter $\alpha_\Sigma = 1/(n+1)$ is the per-observation correction quality; $\mathcal T_\Sigma = \nu \cdot \alpha_\Sigma$, matching the epistemic tempo pattern exactly.

**Case B.2 (two-edge AND chain, $A \to B \to G$, $B$ observable).** Two edges. Edge 1 is tested at rate $\nu_1 = \nu$ (every execution). Edge 2 is tested only when edge 1 succeeds: $\nu_2 = \nu \cdot \theta_1$. The bottleneck edge has $\alpha_\Sigma = \min(1/(n_1+1),\; \theta_1/(n_2+1))$. $\mathcal T_\Sigma = \nu/(n_1+1) + \nu\theta_1/(n_2+1)$, consistent with depth-gated attenuation.

**Case B.3 (two-edge AND chain, $B$ unobservable).** Per-edge tempo is ill-defined (the marginal point estimate is biased). Plan-level tempo is well-defined: $\mathcal T_{\Sigma,\text{plan}} = \nu/(n_\Phi + 1)$, treating $\hat\Phi = p_1 p_2$ as a single tracked quantity.

**Case B.4 (two-arm OR node, $\varepsilon$-greedy).** Edge 1 tested at rate $\nu_1 = \nu(1-\varepsilon)$, edge 2 at rate $\nu_2 = \nu\varepsilon$. $\mathcal T_\Sigma = \nu(1-\varepsilon)/(n_1+1) + \nu\varepsilon/(n_2+1)$. Action selection directly controls the rate allocation --- exploration-gated, not depth-gated.

### Structural decomposition

**AND-chains: depth-gated (geometric attenuation).** In a chain of depth $d$ with edge success probabilities $\theta_k$, the effective observation rate for edge $k$ is:

*[Derived (Conditional on independent edges)]*

$$\nu_k = \nu \cdot \prod_{j \lt k} \theta_j$$

Each additional depth level attenuates by a factor $\theta_k \lt 1$. For a uniform chain ($\theta_k = \theta$, $n_k = n$ for all $k$):

$$\mathcal{T}_\Sigma = \frac{\nu}{n+1} \sum_{k=1}^{d} \theta^{k-1} = \frac{\nu}{n+1} \cdot \frac{1 - \theta^d}{1 - \theta}$$

This converges to $\nu / ((n+1)(1-\theta))$ as $d \to \infty$ --- total strategic tempo is bounded even for arbitrarily deep chains. The marginal tempo contribution of edge $k$ decays as $\theta^{k-1}$, falling below any fixed threshold at depth $d^\ast$ ( #strategy-complexity-cost). Deep AND-chains have low $\mathcal T_\Sigma$ at their leaves regardless of how fast the agent acts --- the evidence-starvation effect identified in #strategic-dynamics-derivation.

**OR-nodes: exploration-gated.** At an OR-node with $m$ alternatives under $\varepsilon$-exploration, the rate allocated to alternative $l$ is:

*[Definition (OR-node rate allocation)]*

$$\nu_l = \begin{cases} \nu(1 - \varepsilon + \varepsilon/m) & l = l^\ast \text{ (greedy arm)} \\ \nu \cdot \varepsilon/m & l \neq l^\ast \text{ (exploratory arms)} \end{cases}$$

The bottleneck is the least-explored alternative. Pure greedy ($\varepsilon = 0$) gives $\nu_l = 0$ for non-greedy arms, making those edges permanently uncorrectable.

### Regime adjustment via identifiability

By #edge-update-causal-validity, the effective gain on each edge is modulated by the identifiability coefficient $\iota_{ij} \in [0, 1]$:

*[Definition (identifiability-adjusted strategic tempo)]*

$$\mathcal T_\Sigma = \sum_{(i,j) \in E} \nu_{ij} \cdot \iota_{ij} \cdot \eta_{\text{edge},ij}$$

where $\iota_{ij} = 1$ for directly intervened edges with attributable outcomes (Regime A in #edge-update-causal-validity), $\iota_{ij} \lt 1$ for edges requiring observational proxy or partial identification, and $\iota_{ij} = 0$ for edges that are causally unidentifiable. This ensures the tempo accounts for the quality of causal evidence, not just its quantity.

### Per-edge persistence

*[Derived (from persistence-condition applied per edge)]*

For $\Sigma_t$ to persist, every edge must maintain bounded mismatch. The bottleneck condition is:

$$\forall (i,j) \in E: \quad \nu_{ij} \cdot \iota_{ij} \cdot \eta_{\text{edge},ij} \gt \frac{\rho_{\Sigma,ij}}{R_{\Sigma,ij}}$$

This is the per-edge analog of #per-dimension-persistence's per-dimension condition for $M_t$. The aggregate relationship between $\mathcal T_\Sigma$ and the average correction rate $\alpha_\Sigma$ is:

$$\alpha_\Sigma \leq \frac{\mathcal T_\Sigma}{\lvert E\rvert} \leq \mathcal T_\Sigma$$

(minimum $\leq$ average $\leq$ sum). Consequently, $\mathcal T_\Sigma \gt \lvert E\rvert \cdot \rho_\Sigma / R_\Sigma$ is *necessary* for persistence but not sufficient --- the persistence condition is bottleneck-limited by the weakest edge, not governed by the aggregate.

## Epistemic Status

The definition itself is axiomatic --- it names a quantity by analogy with #adaptive-tempo. The consistency verification with the four cases from #strategic-dynamics-derivation is *derived* (conditional on Beta-Bernoulli dynamics). The AND-chain geometric attenuation is *derived* (conditional on independent edge outcomes). The OR-node exploration gating and identifiability adjustment are *hypotheses* in the general DAG case, though verified for the specific topologies above. The bottleneck-limited persistence observation is *derived* from #per-dimension-persistence's result applied to the strategy substate.

Max attainable: conditional. Currently conditional because the general DAG case (mixed AND/OR topologies, correlated edges) has not been verified.

## Discussion

**Connection to #per-dimension-persistence.** The per-edge persistence condition inherits the same structure as the per-dimension epistemic result: the weak edge is the bottleneck. Scalar $\mathcal T_\Sigma$ overestimates effective strategic adaptation for the same reason scalar $\mathcal T$ overestimates epistemic adaptation --- it averages over heterogeneous correction capacities.

**Three-way tradeoff.** Strategic tempo competes with both epistemic tempo and exploitation for the agent's finite action capacity. Each action that tests a strategy edge (improving $\mathcal T_\Sigma$) is an action not spent gathering epistemic information (improving $\mathcal T$) or pursuing the current best action (exploitation). The allocation is addressed in #exploit-explore-deliberate — the extended deliberation threshold is derived, but the broader three-way framing is discussion-grade. Deliberation (internal computation) supplements $\mathcal T_\Sigma$ via an internal channel distinct from action-generated evidence.

**Software as Regime A.** In software development, tests are genuine interventions with attributable outcomes ($\iota_{ij} \approx 1$). This makes software agents naturally high-$\mathcal T_\Sigma$ --- a structural advantage identified but not yet formalized in the TST domain ( `02-tst-core/`).

## Working Notes

- **Mixed AND/OR DAGs.** The structural decomposition treats AND-chains and OR-nodes separately. Real strategy DAGs interleave both. How the geometric attenuation (AND) and exploration gating (OR) interact in mixed topologies is unverified. The per-edge persistence condition sidesteps this by treating each edge independently, but the *aggregate* behavior of $\mathcal T_\Sigma$ in mixed DAGs may exhibit interference effects (e.g., evidence starvation in an AND-chain feeding into an OR-node's greedy arm).
- **Optimal topology.** Given a fixed action budget $\nu$, what DAG topology maximizes $\mathcal T_\Sigma$? Shallow OR-heavy structures maximize tempo (more edges are directly observable, no attenuation). Deep AND-chains minimize tempo. This may yield a principled argument for preferring flat, option-rich strategies over deep sequential plans --- complementing the confidence-decay argument in #chain-confidence-decay.
- **Dynamic complexity.** As $n_{ij}$ grows (more observations per edge), $\eta_{\text{edge},ij}$ shrinks (diminishing returns). Strategic tempo declines over time even in a static environment --- the agent's corrections become smaller as edges converge. This is the correct qualitative behavior (converged edges need less correction) but means $\mathcal T_\Sigma$ is not a fixed property of the agent-environment pair.
