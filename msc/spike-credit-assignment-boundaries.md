# Spike: Credit Assignment Boundaries for Strategy DAGs

**Status**: Spike (investigatory). Maps the tractability boundary for credit assignment in AND/OR strategy DAGs.

**Date**: 2026-04-02

**Objective**: Characterize the boundary between tractable and intractable credit assignment for the strategy DAG $\Sigma_t$. Establish negative results (what cannot be done), identify tractable special cases (what can), propose principled approximations for the general case, and state precisely what the theory *requires* of a credit-assignment scheme.

**Depends on**: #strategy-dag, #strategic-calibration, #edge-update-via-gain, #observability-dominance, #strategic-dynamics-derivation (Props B.1--B.5), `spike-two-edge-strategic-dynamics.md`

---

## 0. What Credit Assignment Means in AAD

Credit assignment in AAD is the problem of decomposing an observed outcome at a DAG node into per-edge contributions, so that each edge's credence $p_{ij}$ can be updated appropriately. Formally:

Given observation $o_t$ at some set of observable nodes $\mathcal{V}_{\text{obs}} \subseteq V_t$, compute, for each edge $(i,j) \in E_t$, a **signal** $\text{signal}(o_t, i, j) \in [0,1]$ that represents the evidential content of $o_t$ about the causal link $i \to j$.

This is the unspecified function in #edge-update-via-gain. The update rule is:

$$p_{ij}^{\text{new}} = p_{ij}^{\text{old}} + \eta_{\text{edge}} \cdot (\text{signal}(o_t, i, j) - p_{ij}^{\text{old}})$$

When the signal function is well-defined, the gain principle provides the magnitude. The question is whether, and when, the signal function *can* be well-defined.

**Terminology.** Throughout this spike:
- **Exact credit assignment**: computing the signal function that yields the Bayesian-optimal per-edge posterior update.
- **Directionally faithful credit assignment**: computing a signal function such that each edge's update points in the mismatch-reducing direction (i.e., $\text{sign}(\text{signal} - p_{ij}) = \text{sign}(\theta_{ij} - p_{ij})$ in expectation).
- **Plan-level assessment**: tracking only aggregate plan success, without per-edge decomposition.

---

## 1. Negative Results: Intractability and Underdetermination

### 1.1 Computational Intractability via Shapley Reduction

**Claim.** Exact credit assignment for general AND/OR DAGs with partial observability is at least as hard as computing Shapley values for weighted voting games, which is #P-complete.

**Sketch of reduction.** Consider a strategy DAG $\Sigma_t$ with:
- A single goal node $G$ with $\gamma(G) = \text{AND}$ (or a threshold gate, which AND/OR can simulate).
- $m$ parent edges, each with credence $p_k$ and true probability $\theta_k$.
- The goal node $G$ is the only observable node. All intermediate nodes are unobservable.

The agent observes $y_G \in \{0, 1\}$ and must attribute the outcome to the $m$ edges. Define the "contribution" of edge $k$ to the observed outcome as the expected change in plan-value that edge $k$ is responsible for.

For an AND-node with $m$ parents, the plan success probability is $\Phi = \prod_{k=1}^{m} \theta_k$. On failure ($y_G = 0$), the probability that edge $k$ is the "first cause" of failure (i.e., edge $k$ failed and all edges with index $< k$ in some ordering succeeded) depends on the ordering. The natural attribution --- "what fraction of the total blame does edge $k$ deserve?" --- is formally:

$$\phi_k = \sum_{S \subseteq [m] \setminus \{k\}} \frac{|S|!(m - |S| - 1)!}{m!} \left[\Phi_S - \Phi_{S \cup \{k\}}\right]$$

where $\Phi_S$ is the plan success probability when only the edges in $S$ are "working" (set to $\theta_j = 1$ for $j \in S$) and the rest are at their true values. This is exactly the Shapley value of edge $k$ in the cooperative game where the "value" of coalition $S$ is $\Phi_S$.

For a general AND/OR DAG (which can represent any monotone Boolean function), computing the Shapley value of an edge's contribution to the plan-value function requires summing over all $2^{m-1}$ subsets. Since:

1. Monotone Boolean functions (representable by AND/OR DAGs) include weighted threshold functions.
2. Computing the Shapley value for weighted voting games is #P-complete (Deng & Papadimitriou, 1994).

The reduction goes: given a weighted voting game instance, construct an AND/OR DAG that represents the corresponding threshold function (this is polynomial --- any monotone Boolean function has a polynomial-size AND/OR formula). The Shapley-value attribution of each edge in the DAG encodes the Shapley value of the corresponding player in the voting game.

*[Discussion (Shapley reduction sketch)]*

**Caveats on the reduction.**
- The reduction is to *exact* computation. Approximate Shapley values are computable in polynomial time with sampling (see Section 3).
- The reduction requires the DAG to have unobservable intermediates. With full observability, credit assignment decomposes into per-edge independent updates (Prop B.2), bypassing the combinatorial explosion entirely.
- The Shapley value is one particular notion of "fair attribution." The theory does not require Shapley fairness --- it requires directional fidelity (Section 4). The intractability result says that *exact, axiomatically fair* attribution is hard, not that *any useful* attribution is hard.

**Result.** Exact Shapley-value-based credit assignment for general AND/OR DAGs with unobservable intermediates is #P-hard. This is a genuine computational barrier, not merely an analysis difficulty.

### 1.2 Information-Theoretic Underdetermination

**Claim.** When intermediate nodes are unobservable, per-edge credit assignment is fundamentally underdetermined --- not just hard to compute, but impossible to resolve from the available data.

**Argument.** This is already established for the two-edge case in `spike-two-edge-strategic-dynamics.md` (Section 4.1): from $y_G$ alone, only $\Phi = \theta_1 \theta_2$ is identifiable. Any pair $(\theta_1', \theta_2')$ with $\theta_1' \theta_2' = \Phi$ produces identical observations.

The general case is stronger. Consider a DAG with $m$ edges, of which only the root node is observable. The observation $y_G \sim \text{Bernoulli}(\Phi(\boldsymbol{\theta}))$ is a single scalar constraint on the $m$-dimensional parameter vector $\boldsymbol{\theta} = (\theta_1, \ldots, \theta_m)$. The level set $\{\boldsymbol{\theta} : \Phi(\boldsymbol{\theta}) = c\}$ is an $(m-1)$-dimensional manifold. No amount of repeated binary observations can resolve position within this manifold --- repeated observations identify $\Phi$ but not the decomposition.

*[Derived (non-identifiability, general DAG)]*

More precisely, define the **identifiable subspace** $\mathcal{I}(\mathcal{V}_{\text{obs}})$ as the set of functions of $\boldsymbol{\theta}$ that can be consistently estimated from observations at nodes $\mathcal{V}_{\text{obs}}$. For an AND/OR DAG:

- **Full observability** ($\mathcal{V}_{\text{obs}} = V_t$): $\mathcal{I} = \mathbb{R}^m$ --- all individual $\theta_k$ are identifiable.
- **Root-only** ($\mathcal{V}_{\text{obs}} = \{v_\text{root}\}$): $\mathcal{I} = \text{span}(\Phi)$ --- only the composite plan success probability is identifiable.
- **Partial observability**: $\mathcal{I}$ is intermediate. Each observable node $v$ constrains the edges on paths passing through $v$, but only through their composite effect.

**The identifiable-subspace dimension equals the number of independent observation channels.** Each observable node provides one scalar constraint (its success/failure status). If there are $|\mathcal{V}_{\text{obs}}|$ observable nodes, then at most $|\mathcal{V}_{\text{obs}}|$ independent functions of $\boldsymbol{\theta}$ are identifiable. When $|\mathcal{V}_{\text{obs}}| < m$ (fewer observable nodes than edges), some directions in $\boldsymbol{\theta}$-space are fundamentally unresolvable.

*[Derived (identifiable subspace dimension bound)]*

$$\dim(\mathcal{I}(\mathcal{V}_{\text{obs}})) \leq |\mathcal{V}_{\text{obs}}|$$

**Consequences for AAD:**
1. Credit assignment for edges whose effects are pooled at unobservable nodes is not just computationally hard --- it is *information-theoretically impossible* without additional structure (prior information, structural constraints, or interventional data).
2. Any credit-assignment scheme operating with fewer observations than edges must rely on prior beliefs to resolve the underdetermined directions. The quality of the attribution depends on prior quality, not just on the update algorithm.
3. This is not a failure of the theory but a fundamental property of partial observability. The theory's response (#observability-dominance) is correct: unobservable edges are epistemically frozen, and the correct unit of analysis is the largest identifiable aggregate.

### 1.3 The Posterior Correlation Barrier

Beyond non-identifiability, there is a representation barrier even for approximately identifiable cases.

**Claim.** Any factored representation of per-edge beliefs (independent Beta posteriors) necessarily discards information after observing failure at a non-leaf node with multiple parents.

**Argument.** From the two-edge spike (Section 3.2): after success, the joint posterior factors. After failure, the factor $(1 - \theta_1\theta_2)$ introduces correlation. For $m$ parents at an AND-node, each failure introduces a factor $(1 - \prod_k \theta_k)$, creating a posterior of the form:

$$\pi(\boldsymbol{\theta} \mid \text{data}) \propto \prod_{\text{successes}} \prod_k \theta_k \cdot \prod_{\text{failures}} (1 - \textstyle\prod_k \theta_k) \cdot \pi_0(\boldsymbol{\theta})$$

After $n_f$ failures, the posterior contains $n_f$ factors of $(1 - \prod_k \theta_k)$, each introducing cross-edge correlation. Expanding these factors yields a polynomial of degree $m \cdot n_f$ in the $\theta_k$. Representing this exactly requires exponentially growing storage.

*[Derived (exponential posterior complexity)]*

The factored (independent Beta) representation is therefore an *approximation by construction*. It is the best rank-1 tensor approximation to the true posterior, but it necessarily discards the correlation structure. The proportional-blame update (Section 3.4 of the two-edge spike) is the optimal approximation within this factored family, but it is biased (SA1 violation of $O(1/n)$).

**The representation barrier is distinct from the computational barrier.** Even if we could compute the exact joint posterior efficiently (which we cannot for general DAGs), we could not store it in the factored representation without loss. Coupled corrections are inherent to the problem, not an artifact of a bad algorithm.

---

## 2. Tractable Special Cases

### 2.1 Classification of Tractable Structures

The tractability of credit assignment depends on the interaction of DAG topology and observability structure. Here is a taxonomy, ordered from most to least tractable.

#### Case 1: Fully Observable Intermediates (Trivial)

**Topology**: Any DAG. **Observability**: All nodes observed.

**Result**: Credit assignment decomposes into per-edge independent updates. Each edge $(i,j)$ is tested whenever node $i$ succeeds, and the outcome at node $j$ provides a direct Bernoulli observation of $\theta_{ij}$. The signal function is:

$$\text{signal}(o_t, i, j) = \begin{cases} y_j & \text{if } y_i = 1 \\ \text{no update} & \text{if } y_i = 0 \end{cases}$$

**Update rule**: Standard Beta-Bernoulli conjugate update. Sector condition satisfied with $\alpha_\Sigma = \min_k \eta_k$ modulated by evidence-starvation factors (Prop B.2, generalized).

**Status**: *Established* (Props B.1, B.2 in #strategic-dynamics-derivation).

#### Case 2: Tree-Structured DAGs (Each Node Has At Most One Parent)

**Topology**: Tree (forest). **Observability**: At least the root is observed.

**Result**: In a tree, every node has a unique parent. The path from any leaf to the root is unique. Credit assignment along a chain is the only structure that arises.

- **Observable intermediates**: Reduces to Case 1.
- **Unobservable intermediates**: Each path from a leaf to the root is an AND-chain. The non-identifiability from Section 1.2 applies to each chain independently. Plan-level tracking per chain recovers the sector condition (Prop B.3(b)).

**Update rule**: For each maximal subchain between consecutive observable nodes, treat the chain as a single composite edge and apply Beta-Bernoulli updating to the composite. Per-edge decomposition within the subchain relies on prior beliefs.

**Sector condition**: $\alpha_\Sigma = \min_{\text{subchain } c} 1/(n_c + 1)$ where $n_c$ is the pseudo-count for subchain $c$'s composite probability.

**Key property**: No multi-parent nodes means no "blame splitting" within a tree. The only credit assignment difficulty is the serial-chain non-identifiability.

**Status**: *Derived from existing results* (composition of Props B.2 and B.3).

#### Case 3: Series-Parallel DAGs

**Topology**: Series-parallel (recursively built from series and parallel composition). **Observability**: At least root; potentially some intermediates.

**Definition.** A DAG is **series-parallel** (SP) if it can be built by:
- **Base**: A single edge $A \to B$.
- **Series composition**: Given SP-DAGs $G_1$ (source $s_1$, sink $t_1$) and $G_2$ (source $s_2$, sink $t_2$), merge $t_1$ with $s_2$ to get a new SP-DAG with source $s_1$ and sink $t_2$.
- **Parallel composition**: Given SP-DAGs $G_1$ and $G_2$, merge $s_1$ with $s_2$ and $t_1$ with $t_2$.

**Why SP is tractable.** SP-DAGs have a natural recursive decomposition. Credit assignment can proceed recursively:

1. **Series**: Two subgraphs in series. If the junction node is observable, decompose into independent subproblems (Case 1/2). If unobservable, treat the series pair as a composite edge (analogous to the two-edge AND-chain).

2. **Parallel**: Multiple subgraphs in parallel. At an OR-junction, success identifies which path succeeded (if only one can succeed per trial) or at least identifies that at least one succeeded. At an AND-junction, all must succeed. The parallel structure means each sub-DAG produces a semi-independent observation.

**Update rule (recursive).** For an SP-DAG, define the **composite probability** for each SP-component:

$$\Phi_{\text{series}}(G_1 \circ G_2) = \Phi(G_1) \cdot \Phi(G_2)$$
$$\Phi_{\text{parallel-AND}}(G_1 \| G_2) = \Phi(G_1) \cdot \Phi(G_2)$$
$$\Phi_{\text{parallel-OR}}(G_1 \| G_2) = 1 - (1 - \Phi(G_1))(1 - \Phi(G_2))$$

Observable junction nodes split the recursion into independent subproblems. Unobservable junctions force composite tracking at that level of the recursion. The total number of independent estimation problems equals the number of maximal subgraphs between consecutive observable nodes.

**Sector condition**: $\alpha_\Sigma = \min_c 1/(n_c + 1)$ over all independent composite subproblems $c$. The recursive structure ensures the minimum is taken over at most $|\mathcal{V}_{\text{obs}}|$ subproblems.

**Computational complexity**: $O(|V| + |E|)$ per update step (one pass through the recursive decomposition).

**Status**: *Hypothesis, structurally motivated.* The recursive decomposition is well-defined for SP-DAGs. The claim is that the sector condition composes correctly under this recursion. This is plausible (each level of the recursion is a two-component composition, for which Props B.2--B.4 apply), but the formal induction is not carried out here.

#### Case 4: Bounded Treewidth DAGs

**Topology**: General DAG with treewidth $\leq w$. **Observability**: General.

**Why bounded treewidth helps.** The joint posterior $\pi(\boldsymbol{\theta} \mid \text{data})$ on the edge parameters can be represented as a factor graph. The factor graph's treewidth determines the complexity of exact inference. For treewidth $w$:

- Exact marginal computation: $O(|V| \cdot 2^w)$ per update.
- Exact MAP estimation: Same complexity.

When $w$ is bounded by a constant (or grows slowly with $|V|$), exact Bayesian inference is tractable, and therefore exact credit assignment is tractable.

**Connection to strategy DAGs.** The treewidth of a strategy DAG is related to the "width" of the plan --- how many parallel threads of activity are being pursued simultaneously. A purely sequential plan (AND-chain) has treewidth 1. A plan with $k$ parallel workstreams has treewidth at most $k$. Real-world strategies typically have small treewidth because human cognitive limits constrain parallelism.

**Update rule**: Run junction-tree belief propagation on the factor graph of edge parameters. Each edge receives the exact marginal posterior update.

**Sector condition**: Exact Bayesian inference satisfies SA1 for the full joint posterior. The marginal point-estimate bias (Section 1.3) arises only when the posterior is *approximated* by a factored representation. If the agent maintains the full (junction-tree) posterior, the bias disappears. Whether the full posterior satisfies a sector condition in the joint parameter space is an open question --- the standard sector framework operates on point estimates, and the full-posterior analog requires a different analysis (e.g., posterior contraction rates).

**Status**: *Hypothesis.* The computational tractability claim follows from standard results in graphical model inference. The sector-condition implications are speculative.

#### Case 5: Linear Chains with a Single Unobservable Node

**Topology**: $A_1 \to A_2 \to \cdots \to A_d \to G$, with exactly one $A_k$ unobservable. **Observability**: All nodes except $A_k$ observed.

**Result**: The unobservable node $A_k$ creates a single composite edge from $A_{k-1}$ to $A_{k+1}$ (or from $A_{k-1}$ through $A_k$ to $A_{k+1}$). All other edges are independently identifiable. The credit assignment problem reduces to a single two-edge unobservable subproblem (the two edges adjacent to $A_k$) embedded in an otherwise fully observable chain.

**Update rule**: Apply Props B.1/B.2 to all observable edges. Apply Prop B.3 (plan-level tracking) to the two edges adjacent to $A_k$.

**Sector condition**: $\alpha_\Sigma = \min(\alpha_{\text{observable edges}}, 1/(n_{\text{composite}} + 1))$.

**Status**: *Derived from existing results.*

### 2.2 Summary of Tractability Boundary

| Structure | Observability | Credit Assignment | Complexity | Sector Condition |
|-----------|--------------|-------------------|-----------|-----------------|
| Any DAG | Full | Trivial (per-edge independent) | $O(\lvert V\rvert + \lvert E\rvert)$ | Prop B.2 (generalized) |
| Tree | Partial | Chain decomposition | $O(\lvert V\rvert + \lvert E\rvert)$ | Min over subchains |
| Series-parallel | Partial | Recursive decomposition | $O(\lvert V\rvert + \lvert E\rvert)$ | Min over SP-components |
| Treewidth $\leq w$ | Any | Junction tree inference | $O(\lvert V\rvert \cdot 2^w)$ | Exact (if full posterior tracked) |
| General DAG | Partial | #P-hard (Shapley); underdetermined | Intractable (exact) | Approximation required |

**The key structural distinction is not topology but the interaction of topology with observability.** Any DAG with full observability is trivial. Any DAG with root-only observability is hard (unless the DAG has special structure like SP or bounded treewidth). The tractability boundary is the number of independent observation channels relative to the number of free parameters.

---

## 3. Principled Approximations

For the intractable general case, we need approximation schemes. The critical requirement from the theory is **directional fidelity** (Section 4). Here we evaluate four candidate approximations.

### 3.1 Proportional Blame (Generalized from Two-Edge Spike)

**Method.** On failure at a node $v$ with parents $\{i_1, \ldots, i_k\}$ (AND-node), compute the posterior probability that each parent edge caused the failure:

$$q_{i_j} = \frac{P(\text{edge } i_j \text{ failed} \mid v \text{ failed},\, \hat{\mathbf{p}})}{P(v \text{ failed} \mid \hat{\mathbf{p}})}$$

where $\hat{\mathbf{p}}$ is the vector of current credence estimates. For an AND-node:

$$q_{i_j} = \frac{(1 - p_{i_j}) \prod_{l \neq j} p_{i_l}}{1 - \prod_l p_{i_l}}$$

(This generalizes the two-edge formula $q_1 = (1-p_1)/(1-p_1 p_2)$.)

Update: decrement each edge's credence by its blame share.

**Properties:**
- **Is the marginal Bayesian point-estimate update.** Established for the two-edge case in the spike; the argument generalizes to any AND-node with independent edge priors.
- **Violates SA1.** At truth, the expected update is nonzero with bias $O(1/n)$, pushing all credences downward (toward pessimism). The bias magnitude for edge $j$ at an AND-node:

$$|b_j| = \frac{\theta_j(1-\theta_j)(1 - \theta_j / \Phi)}{n_j + 1} \cdot \Phi$$

where $\Phi = \prod_k \theta_k$. For large $m$ (many parents), $\Phi \to 0$, and the bias can be substantial relative to the update magnitude.

- **Directional fidelity.** *Satisfied asymptotically.* Near truth, the bias dominates and directional fidelity fails. Far from truth (when $|\delta_k|$ is large relative to $|b_k|$), the update direction is correct because the Bayesian update is consistent --- the proportional-blame signal tracks the mismatch sign when the signal-to-bias ratio is large. Formally: directional fidelity holds when $|\delta_k| \gg \theta_k(1-\theta_k)(1-\theta_k/\Phi)/(n_k+1)$.

- **Error bound.** The $O(1/n)$ bias means the point estimates converge to a point on the level set $\{\boldsymbol{\theta}' : \prod_k \theta_k' = \Phi\}$ that is close to, but not exactly at, the true $\boldsymbol{\theta}$. The convergence is to the prior-determined decomposition.

**When it breaks:** (a) Many parents at an AND-node with small $\Phi$ (bias dominates); (b) prior beliefs are far from truth (the prior-determined decomposition may be very wrong); (c) the agent needs per-edge precision, not just plan-level correctness.

**Verdict.** Usable for AAD's purposes when combined with plan-level tracking as a fallback. The directional fidelity requirement is approximately satisfied when the agent has reasonable priors and moderate per-edge mismatch.

### 3.2 Gradient-Based Attribution

**Method.** Treat edge credences $\mathbf{p}$ as parameters of the plan-value function $\hat{P}_\Sigma(\mathbf{p})$. Observe the realized outcome $y_G$. The "surprise" is $y_G - \hat{P}_\Sigma$. Attribute this surprise to edges proportionally to their plan-value gradient:

$$\text{signal}(o_t, i, j) = p_{ij} + \frac{\partial \hat{P}_\Sigma}{\partial p_{ij}} \cdot (y_G - \hat{P}_\Sigma) \cdot c$$

where $c$ is a normalization constant ensuring the signal lies in $[0,1]$. This is analogous to the gradient-based update in neural network training (backpropagation).

**Computation of the gradient.** The plan-value function $\hat{P}_\Sigma(\mathbf{p})$ is defined by the AND/OR status propagation formulas (#strategy-dag). The gradient $\nabla_\mathbf{p} \hat{P}_\Sigma$ is the Jacobian $\mathbf{J}$ from Prop B.5, computable in $O(|V| + |E|)$ by reverse-mode differentiation through the propagation.

For an AND-node with parents $\{i_1, \ldots, i_k\}$ feeding into node $v$:

$$\frac{\partial \hat{P}_\Sigma}{\partial p_{i_j,v}} = s_{i_j} \cdot \prod_{l \neq j} (p_{i_l,v} \cdot s_{i_l}) \cdot \frac{\partial \hat{P}_\Sigma}{\partial s_v}$$

For an OR-node:

$$\frac{\partial \hat{P}_\Sigma}{\partial p_{i_j,v}} = s_{i_j} \cdot \prod_{l \neq j} (1 - p_{i_l,v} \cdot s_{i_l}) \cdot \frac{\partial \hat{P}_\Sigma}{\partial s_v}$$

Both are computable in a single backward pass.

**Properties:**
- **Directional fidelity.** *Satisfied by construction* when the gradient is nonzero and the normalization is correct. The gradient points in the direction that most increases plan value. If $y_G > \hat{P}_\Sigma$ (surprise success), all edges with positive gradient receive a credence increase. If $y_G < \hat{P}_\Sigma$ (surprise failure), all edges receive a credence decrease, with larger decreases for higher-sensitivity edges. Since $\partial \hat{P}_\Sigma / \partial p_{ij} \geq 0$ for all edges in a well-formed AND/OR DAG (monotonicity), the direction is always mismatch-reducing for the *aggregate* plan value.

  **However**: directional fidelity for the aggregate does not imply directional fidelity per edge. An edge that is actually well-calibrated still receives an update if other edges cause a plan-level surprise. This is the same issue as the proportional-blame bias, expressed differently.

- **Connection to Prop B.5.** The gradient is exactly the Jacobian $\mathbf{J}$ from Prop B.5. The gradient-based update can be written as:

  $$\Delta p_{ij} = \eta_{\text{edge}} \cdot J_{ij} \cdot (y_G - \hat{P}_\Sigma) / \lVert\mathbf{J}\rVert^2$$

  This is a form of natural-gradient update, projecting the plan-level surprise onto the edge credences via the Jacobian.

- **SA1 check.** At truth ($\mathbf{p} = \boldsymbol{\theta}$): $\hat{P}_\Sigma = \Phi$, and $\mathbb{E}[y_G - \hat{P}_\Sigma] = 0$. Therefore $\mathbb{E}[\Delta p_{ij}] = 0$ at truth. **SA1 is satisfied** --- the gradient-based attribution has zero expected correction at truth, unlike proportional blame.

  Wait --- this needs more care. The gradient-based update at truth gives:

  $$\mathbb{E}[\Delta p_{ij}] = \eta \cdot J_{ij} \cdot \mathbb{E}[y_G - \Phi] / \lVert\mathbf{J}\rVert^2 = 0$$

  Yes, SA1 is satisfied because $\mathbb{E}[y_G] = \Phi$ exactly.

- **Does it satisfy the sector condition?** Consider the expected sector product:

  $$\mathbb{E}[\boldsymbol{\delta}^T \mathbf{F}(\boldsymbol{\delta})] = \eta \cdot \mathbb{E}\left[\boldsymbol{\delta}^T \frac{\mathbf{J} (y_G - \hat{P}_\Sigma)}{\lVert\mathbf{J}\rVert^2}\right]$$

  Since $\mathbb{E}[y_G - \hat{P}_\Sigma] = \Phi - \hat{P}_\Sigma = -\mathbf{J}^T \boldsymbol{\delta}$ (to first order):

  $$= -\eta \cdot \frac{\boldsymbol{\delta}^T \mathbf{J} \mathbf{J}^T \boldsymbol{\delta}}{\lVert\mathbf{J}\rVert^2} = -\eta \cdot \frac{\lVert\mathbf{J}^T \boldsymbol{\delta}\rVert^2}{\lVert\mathbf{J}\rVert^2}$$

  This is *negative*, meaning the correction reduces mismatch. But is it bounded below by $\alpha \lVert\boldsymbol{\delta}\rVert^2$? By Cauchy-Schwarz:

  $$\lVert\mathbf{J}^T \boldsymbol{\delta}\rVert^2 \geq \sigma_{\min}(\mathbf{J})^2 \lVert\boldsymbol{\delta}\rVert^2$$

  So:

  $$\mathbb{E}[\boldsymbol{\delta}^T \mathbf{F}(\boldsymbol{\delta})] \leq -\eta \cdot \frac{\sigma_{\min}(\mathbf{J})^2}{\lVert\mathbf{J}\rVert^2} \lVert\boldsymbol{\delta}\rVert^2$$

  (Note: the correction function $F$ should be positive when aligned with $\delta$, so we need to be careful with signs. The sector product $\boldsymbol{\delta}^T \mathbf{F}$ should be positive. Here $F_k = -\Delta p_k / \eta$ in the convention where $F$ is the correction toward truth. Let me re-derive.)

  Defining $F_k(\boldsymbol{\delta}) = -\mathbb{E}[\Delta p_k] / 1 = \eta \cdot J_k \cdot \mathbf{J}^T \boldsymbol{\delta} / \lVert\mathbf{J}\rVert^2$ (using $\mathbb{E}[y_G - \hat{P}_\Sigma] = \Phi - \hat{P}_\Sigma \approx -\mathbf{J}^T\boldsymbol{\delta}$):

  $$\boldsymbol{\delta}^T \mathbf{F}(\boldsymbol{\delta}) = \eta \cdot \frac{(\boldsymbol{\delta}^T \mathbf{J})(\mathbf{J}^T \boldsymbol{\delta})}{\lVert\mathbf{J}\rVert^2} = \eta \cdot \frac{\lVert\mathbf{J}^T \boldsymbol{\delta}\rVert^2}{\lVert\mathbf{J}\rVert^2} \geq \eta \cdot \frac{\sigma_{\min}^2}{\sigma_{\max}^2} \lVert\boldsymbol{\delta}\rVert^2$$

  So:

  $$\alpha_\Sigma^{\text{grad}} = \eta \cdot \frac{\sigma_{\min}(\mathbf{J})^2}{\sigma_{\max}(\mathbf{J})^2} = \frac{\eta}{\kappa(\mathbf{J})^2}$$

  **The gradient-based attribution incurs the condition-number penalty.** This matches the coupled-correction case in Prop B.5b. The gradient-based scheme couples all edges through the shared plan-level surprise, so the $\kappa^2$ penalty is expected.

- **Error bound.** The convergence rate is governed by $\alpha_\Sigma^{\text{grad}} = \eta / \kappa(\mathbf{J})^2$. For well-conditioned DAGs ($\kappa \approx 1$), this is comparable to the per-edge rate. For ill-conditioned DAGs (deep chains, highly unbalanced edge sensitivities), the rate degrades quadratically in the condition number.

**When it breaks:** Ill-conditioned DAGs (large $\kappa(\mathbf{J})$), which occur when some edges are much more sensitive to plan value than others. In deep AND-chains, edges near the root have exponentially larger $J_k$ than edges near the leaves, giving $\kappa = O(\prod \theta_k / \min_k J_k)$ which can be exponentially large.

**Verdict.** Gradient-based attribution is the only approximation that satisfies SA1. It provides directional fidelity and a sector condition, at the cost of a condition-number penalty. It is the principled choice for the theory because it directly leverages the Jacobian bridge (Prop B.5).

### 3.3 Monte Carlo Tree Search Style (Sampling-Based Attribution)

**Method.** Estimate each edge's contribution by sampling. For each edge $(i,j)$:
1. Sample $N$ rollouts with edge $(i,j)$ "on" (set $p_{ij} = 1$, all other edges at their current credences).
2. Sample $N$ rollouts with edge $(i,j)$ "off" (set $p_{ij} = 0$).
3. The estimated contribution of edge $(i,j)$: $\hat{c}_{ij} = \hat{P}_{\text{on}} - \hat{P}_{\text{off}}$.

This is a sampling-based approximation to the leave-one-out influence, not the Shapley value. (The Shapley value averages over all orderings; this computes only the marginal contribution.)

**Properties:**
- **Computational cost**: $O(N \cdot m \cdot (|V| + |E|))$ per update --- $m$ edges, each requiring $N$ simulated rollouts through the DAG.
- **Does not require actual execution.** This is a *model-based* estimate, computed from the agent's current beliefs about edge probabilities. No real-world observations are needed beyond the initial plan-value model.
- **Directional fidelity.** The leave-one-out contribution $\hat{c}_{ij}$ is non-negative for all edges in a monotone AND/OR DAG (removing an edge never increases plan value). This gives a relative importance ranking but does not directly give a signal in $[0,1]$ for the update rule.
- **Does not directly satisfy the sector condition.** The sampling estimate introduces noise ($O(1/\sqrt{N})$ per edge), and the leave-one-out decomposition does not sum to the total plan value in general (the interactions are ignored). The update direction is approximately correct, but the magnitude is not principled.

**When it breaks:** Small $N$ (high variance), DAGs with strong edge interactions (leave-one-out misses interaction effects), and computational budget constraints.

**Verdict.** Useful as a diagnostic tool (identifying which edges matter most) but not as a primary update mechanism. The per-edge updates it suggests are not Bayesian and do not have a clear sector-condition characterization.

### 3.4 Belief Propagation on the Factor Graph

**Method.** Represent the joint posterior $\pi(\boldsymbol{\theta} \mid \text{data})$ as a factor graph and run loopy belief propagation (LBP) or expectation propagation (EP) to approximate the marginal posteriors.

**Properties:**
- **For tree-structured factor graphs**: BP gives exact marginals. This covers Cases 1--2 (trees) and is equivalent to the per-edge independent update.
- **For SP-DAGs**: BP on the recursive decomposition is equivalent to the recursive composite update (Case 3).
- **For general DAGs**: LBP is an approximation with no convergence guarantee. EP (moment-matching at each factor) tends to be more stable.

**Directional fidelity.** Not guaranteed for LBP (can oscillate or diverge). EP, when it converges, produces consistent marginal approximations that respect the posterior's mode structure. The directional fidelity of EP depends on the quality of the moment-matching approximation.

**Sector condition.** No general sector-condition result is known for LBP or EP. For EP specifically, the moment-matching update for each edge's Beta posterior has a known convergence analysis (Minka, 2001), but it is not expressed in sector-condition form.

**Computational cost.** $O(|V| \cdot |E| \cdot k_{\text{iter}})$ per update, where $k_{\text{iter}}$ is the number of BP iterations to convergence.

**Verdict.** BP/EP is the standard approximate inference toolkit. It subsumes proportional blame (which is one iteration of EP on the two-edge factor graph) and bounded-treewidth exact inference (which is BP on a junction tree). For AAD's purposes, EP is a reasonable implementation strategy, but it does not have the clean sector-condition characterization that the theory demands.

### 3.5 Comparison of Approximation Schemes

| Scheme | SA1 | Directional Fidelity | Sector Condition | Complexity | Best For |
|--------|-----|---------------------|-----------------|-----------|----------|
| Proportional blame | No ($O(1/n)$ bias) | Approximately (far from truth) | Plan-level only | $O(\lvert V\rvert + \lvert E\rvert)$ | Simple DAGs, quick updates |
| Gradient-based | Yes | Yes (aggregate) | $\eta / \kappa(\mathbf{J})^2$ | $O(\lvert V\rvert + \lvert E\rvert)$ | General DAGs, well-conditioned |
| MCTS sampling | N/A | Approximately | Not characterized | $O(N m (\lvert V\rvert + \lvert E\rvert))$ | Diagnostics, importance ranking |
| Belief propagation / EP | Varies | Approximately | Not characterized | $O(\lvert V\rvert \lvert E\rvert k)$ | Complex posteriors, iterative refinement |

**Recommendation for AAD.** The gradient-based scheme is the most principled because it (a) satisfies SA1, (b) has a characterizable sector parameter, and (c) directly leverages the Jacobian bridge (Prop B.5). Its weakness --- the condition-number penalty --- is the same penalty that Prop B.5b already identifies as inherent to coupled corrections. This is not an artifact of the approximation; it is the cost of credit assignment with partial observability.

---

## 4. The Design Requirement: What the Theory Actually Needs

### 4.1 What Persistence Requires (Nothing)

The central insight from Prop B.5 is that **persistence does not require credit assignment at all.**

The persistence guarantee requires the sector condition in value-residual space: $\delta_s \cdot F_s(\delta_s) \geq \alpha_s \delta_s^2$. Prop B.5 shows that this transfers from credence space to value space via the Jacobian $\mathbf{J} = \nabla_\mathbf{p} \hat{P}_\Sigma$. The Jacobian is computable from the DAG's status propagation formulas without solving credit assignment.

- For componentwise (per-edge independent) corrections: the transfer is exact ($\alpha_s = \alpha_c$).
- For coupled corrections: the transfer incurs $\kappa(\mathbf{J})^2$ penalty ($\alpha_s \geq \alpha_c / \kappa^2$).

In both cases, what matters is the *existence* of a per-edge correction mechanism satisfying the sector condition, not the *optimality* of the credit assignment.

**Therefore: the persistence guarantee is credit-assignment-free.** An agent that uses *any* update scheme satisfying the sector condition (even a suboptimal one) gets the persistence guarantee. The quality of credit assignment affects the *rate* of convergence (via $\alpha_\Sigma$) but not the *existence* of bounded mismatch.

### 4.2 What Calibration Requires (Directional Fidelity)

The strategic calibration diagnostic (#strategic-calibration) requires per-edge residuals $r_{ij}$. Computing $r_{ij}$ requires attributing observed value changes to specific edges --- this IS credit assignment.

But the theory's structural requirements on the calibration diagnostic are weaker than "compute the exact per-edge residual." What is needed:

**Directional fidelity (B1).** For each edge $(i,j)$ with mismatch $\delta_{ij} = p_{ij} - \theta_{ij}$, the expected correction must satisfy:

$$\text{sign}(\mathbb{E}[F_{ij}(\boldsymbol{\delta})]) = \text{sign}(\delta_{ij})$$

whenever $|\delta_{ij}|$ exceeds a threshold $\epsilon_{ij}$ (which may depend on the DAG structure and observability).

This is strictly weaker than exact attribution. It says: "on average, push each edge in the right direction." It does not require the push to be the Bayesian-optimal magnitude, or that the per-edge updates be independent, or that SA1 hold exactly.

### 4.3 What the Gain Principle Requires (Bounded Signal)

The gain principle (#edge-update-via-gain) requires $\text{signal}(o_t, i, j) \in [0, 1]$ and $\eta_{\text{edge}} = U_{\text{edge}} / (U_{\text{edge}} + U_{\text{obs}})$. The gain provides the step size; the signal provides the direction.

**Minimal requirement on the signal function:**
1. $\text{signal}(o_t, i, j) \in [0, 1]$ (bounded).
2. $\mathbb{E}[\text{signal}(o_t, i, j)] \to \theta_{ij}$ as $n \to \infty$ (consistency).
3. $\text{sign}(\mathbb{E}[\text{signal} - p_{ij}]) = \text{sign}(\theta_{ij} - p_{ij})$ when $|p_{ij} - \theta_{ij}| > \epsilon$ (directional fidelity above a threshold).

These three conditions are sufficient for the edge update to produce convergent, directionally faithful corrections. They do not require the signal to be the Bayesian-optimal posterior mean, or to be independent of other edges' signals, or to be unbiased at every finite $n$.

### 4.4 The Minimal Credit Assignment Requirement

Combining Sections 4.1--4.3:

**Theorem (informal).** For the theory's persistence and calibration guarantees:

1. **Persistence** requires only that the aggregate plan-level correction satisfies the sector condition. This is achievable with plan-level tracking (Prop B.3(b)) and requires no per-edge credit assignment.

2. **Per-edge calibration** requires directional fidelity: each edge's signal must point in the mismatch-reducing direction in expectation, beyond a threshold set by the DAG's condition number and observability structure.

3. **The signal function need not be exact, unbiased, or independent across edges.** It must be bounded, asymptotically consistent, and directionally faithful.

*[Discussion (minimal credit assignment requirement)]*

**The hierarchy of credit assignment quality:**

| Level | Requirement | What it buys | Cost |
|-------|------------|-------------|------|
| **0** (none) | Plan-level tracking only | Persistence guarantee | No per-edge diagnostics |
| **1** (directional) | Directional fidelity per edge | Persistence + rough diagnostics | Gradient computation ($O(\lvert V\rvert + \lvert E\rvert)$) |
| **2** (approximate) | Proportional blame / EP | Persistence + per-edge diagnostics (with bias) | Factor-graph inference |
| **3** (exact) | Full Bayesian posterior | Persistence + optimal per-edge calibration | #P-hard (general case) |

AAD's formal guarantees require only Level 0. Practical agents need at least Level 1 for adaptive behavior. Level 2 is the sweet spot for most applications. Level 3 is a mathematical ideal that is computationally unattainable in the general case.

---

## 5. Connection to Existing Literature

### 5.1 Reinforcement Learning: Temporal Credit Assignment

RL faces the same problem: when a reward arrives at the end of an episode, which actions contributed? The standard approaches:

**Temporal difference (TD) learning.** TD($\lambda$) with eligibility traces assigns credit to past state-action pairs based on temporal recency. The eligibility trace $e_t(s, a)$ decays exponentially with time since the pair was visited. This is a heuristic that assumes "recent actions are more responsible" --- a temporal analog of proportional blame.

- **AAD parallel**: The evidence-starvation effect (Props B.2, generalized) is the structural analog of eligibility-trace decay. Upstream edges (earlier in time) receive cleaner attribution than downstream edges, because their outcomes are observed first.
- **What AAD can borrow**: The idea that credit should decay with causal distance (not just temporal distance) is more principled than TD's temporal-only decay. AAD's DAG structure provides the causal distance; the Jacobian $\mathbf{J}$ provides the sensitivity weighting.

**Policy gradient methods.** REINFORCE and its variants estimate $\nabla_\theta J(\theta)$ by $\mathbb{E}[\nabla_\theta \log \pi_\theta(a|s) \cdot R]$. This attributes the total reward $R$ to each parameter proportional to the score function $\nabla \log \pi$.

- **AAD parallel**: The gradient-based attribution (Section 3.2) is the AAD analog of policy gradient. The Jacobian $\mathbf{J}$ plays the role of the score function, and the plan-level surprise $(y_G - \hat{P}_\Sigma)$ plays the role of the reward signal.
- **What AAD can borrow**: Variance reduction techniques (baselines, advantage functions) from policy gradient literature could reduce the variance of the gradient-based edge update. A "baseline" for edge $(i,j)$ would be the average plan-value change when that edge is not the one being updated.

**Hindsight credit assignment (HCA).** Recent RL work (Harutyunyan et al., 2019; Mesnard et al., 2021) develops methods that retrospectively attribute outcomes to specific actions using counterfactual reasoning: "what would have happened if a different action had been taken at time $k$?"

- **AAD parallel**: This is exactly the leave-one-out influence computation in Section 3.3. The counterfactual "set $p_{ij} = 0$ vs. $p_{ij} = 1$" is the AAD version of "what if this edge didn't exist?"
- **What AAD can borrow**: HCA's key insight is that counterfactual attribution is tractable when a model of the environment is available. Since $\Sigma_t$ IS the agent's model of its plan dynamics, model-based counterfactual attribution is natural.

### 5.2 Causal Inference: Attribution Methods

**Do-calculus and interventional queries.** Pearl's framework provides the gold standard for causal attribution: the effect of edge $(i,j)$ is $P(j \mid do(i)) - P(j \mid do(\neg i))$. This requires interventional data (or identifiability conditions that allow interventional conclusions from observational data).

- **AAD connection**: Edge credences $p_{ij}$ are intended to approximate $P(j \mid do(i), M_t)$ (#strategy-dag, edge semantics). In intervention-rich domains (software, laboratory), the agent can directly estimate this via experiment. In confounded domains, the do-calculus provides conditions under which observational data suffice.
- **Key insight for AAD**: The identifiability conditions from do-calculus (back-door criterion, front-door criterion) translate directly to observability conditions on the strategy DAG. A "back-door admissible" set in the DAG is a set of observable nodes that blocks confounding. This gives a formal criterion for when per-edge credences are identifiable from partial observations.

**Mediation analysis.** Decomposes the total effect of a treatment into direct and indirect effects (through mediating variables). The AND-chain $A \to B \to G$ is a mediation model where $B$ is the mediator.

- **AAD connection**: The two-edge spike's observable-intermediate case IS mediation analysis: the total effect $\theta_1 \theta_2$ is decomposed into direct effects $\theta_1$ (on $B$) and $\theta_2$ ($B$ on $G$). The unobservable case is mediation analysis without observing the mediator --- known to be problematic in the causal inference literature as well.

**Shapley-based methods (SHAP, Owen values).** Recent work in ML interpretability uses Shapley values to attribute model predictions to input features. Efficient approximation algorithms exist:
- **KernelSHAP** (Lundberg & Lee, 2017): Approximates Shapley values by weighted least-squares regression over sampled coalitions. Complexity: $O(m \cdot N)$ where $N$ is the number of coalition samples.
- **TreeSHAP** (Lundberg et al., 2020): Exact Shapley values for tree-structured models in $O(TLD^2)$. Exploits tree structure for efficient subset enumeration.

- **What AAD can borrow**: KernelSHAP's sampling approach could be adapted for approximate edge attribution in strategy DAGs. The "model" being explained is the plan-value function $\hat{P}_\Sigma$, and the "features" are the edge credences. The Shapley value of each edge would give its "fair" contribution to plan value, providing a principled signal function. TreeSHAP's exploitation of tree structure is relevant to the tractable cases (Section 2).

### 5.3 Summary of Literature Connections

| AAD Problem | RL Analog | Causal Inference Analog | Tractable Method |
|-------------|-----------|------------------------|-----------------|
| Per-edge attribution | Temporal credit assignment | Mediation analysis | Gradient (policy gradient) |
| Unobservable intermediates | Partial observability / POMDPs | Unobserved mediators | Plan-level tracking / EM |
| Multi-parent blame | Multi-agent credit assignment | Shapley value decomposition | Sampling (KernelSHAP) |
| Observable intermediates | Fully observed MDPs | Experimental identification | Direct estimation |

---

## 6. Open Questions and Future Directions

### 6.1 The Gradient-Based Scheme as the Canonical Signal Function

The gradient-based attribution (Section 3.2) is the strongest candidate for the unspecified signal function in #edge-update-via-gain. It:
- Satisfies SA1 (zero expected correction at truth).
- Has a characterizable sector parameter ($\eta / \kappa(\mathbf{J})^2$).
- Is computable in $O(|V| + |E|)$ (one forward pass + one backward pass).
- Reduces to the standard Beta-Bernoulli update in the single-edge case.
- Reduces to proportional blame (approximately) in the two-edge unobservable case (to first order in the mismatch).

**Open question**: Is the gradient-based signal function the *unique* scheme satisfying SA1 and monotonicity for general AND/OR DAGs? Or is there a family of SA1-satisfying schemes parameterized by some choice? If there is a family, the gradient-based scheme is the one with minimal variance (it is the steepest-descent direction in parameter space).

### 6.2 The Condition Number as Strategy Health Metric

The condition number $\kappa(\mathbf{J})$ of the plan-value Jacobian emerges as a central quantity: it governs the sector-parameter degradation under any coupled credit-assignment scheme. A well-conditioned DAG ($\kappa \approx 1$) has all edges contributing approximately equally to plan value; an ill-conditioned DAG has a few critical edges and many inconsequential ones.

**Open question**: Can the agent *improve* $\kappa(\mathbf{J})$ by restructuring the DAG? E.g., adding redundant paths (OR-nodes) to reduce the dependence on any single edge, or introducing observable intermediates to decouple the corrections. If so, there is a second-order optimization problem: choose the DAG structure to minimize $\kappa(\mathbf{J})$, subject to the constraint that the DAG still represents a viable strategy for $O_t$.

This connects to the strategy health metrics mentioned in the working notes of #strategy-dag (groundedness, bottleneck scores). The condition number may provide a principled replacement.

### 6.3 Adaptive Observability Investment

The tractability boundary (Section 2) shows that observability is the key determinant of credit-assignment quality. An agent that can choose *where to invest in observability* faces a value-of-information problem: which unobservable nodes, if made observable, would most improve $\alpha_\Sigma$?

**The answer follows from the condition-number analysis.** Making a node observable decouples the corrections above and below it, potentially reducing $\kappa(\mathbf{J})$ for each subgraph. The node whose observation most reduces $\kappa$ is the best investment target. For a linear AND-chain, this is the midpoint node (splitting the chain into two halves of equal depth). For a general DAG, it is the node that most reduces the maximum path length between consecutive observable nodes.

**Open question**: Formalize the observability investment problem as: minimize $\kappa(\mathbf{J})$ (or equivalently maximize $\alpha_\Sigma$) subject to a budget constraint on the number of observable nodes. Is this a submodular optimization problem (which would give efficient greedy approximation)?

### 6.4 The OR-Node Credit Assignment Problem

The two-edge spike analyzed AND-chains. OR-nodes have the complementary problem: success must be attributed (which alternative worked?), while failure is clean (all alternatives failed).

For an OR-node with $k$ alternatives:
- **Failure ($y_G = 0$)**: All alternatives failed. Each edge receives a standard failure update. Credit assignment is trivial (all edges get blame independently, since all were tested and all failed).
- **Success ($y_G = 1$)**: At least one alternative succeeded. If only one was attempted (the $\varepsilon$-greedy case from Prop B.4), credit assignment is trivial (the attempted edge succeeded). If multiple were attempted simultaneously, the agent must determine which one(s) caused success.

In the simultaneous-attempt case, the OR-node success attribution is a *coverage* problem: "which of these redundant methods actually contributed?" This is analogous to A/B testing --- the agent needs to determine which variant caused the positive outcome.

**Open question**: Develop the sector condition for simultaneous OR-node attempts. The expected correction should have an exploration-gated structure analogous to Prop B.4, but the allocation is over simultaneous attempts rather than sequential $\varepsilon$-greedy selection.

### 6.5 Mixed AND/OR DAGs

The general case --- mixed AND/OR DAGs with partial observability --- combines AND-chain evidence starvation, OR-node exploration gating, and the credit-assignment barriers from this spike. The sector parameter for a general DAG should have the form:

$$\alpha_\Sigma = \min_{c \in \text{components}} \alpha_c(\text{topology}_c, \text{observability}_c, \text{policy}_c)$$

where the minimum is over the independent subproblems created by observable nodes, and each $\alpha_c$ depends on the local topology (AND/OR structure), observability (how many intermediates are observed), and policy (exploration rate for OR-nodes).

**Open question**: Does the weakest-link composition $\alpha_\Sigma = \min_c \alpha_c$ hold for general mixed DAGs, or do interactions between AND and OR regions create additional penalties?

---

## 7. Summary of Results

### Negative Results

1. **Exact credit assignment is #P-hard** for general AND/OR DAGs with partial observability (via reduction to Shapley value computation for weighted voting games). This is a computational intractability result.

2. **Per-edge attribution is information-theoretically underdetermined** when the number of observable nodes is less than the number of edges. The identifiable-subspace dimension is bounded by $|\mathcal{V}_{\text{obs}}|$.

3. **The factored representation barrier**: any factored (independent Beta) representation of per-edge beliefs necessarily discards the posterior correlation introduced by failure at multi-parent nodes. The exact posterior complexity grows exponentially with the number of failures observed.

### Tractable Cases

4. **Fully observable intermediates**: trivial, per-edge independent. (Established.)
5. **Trees**: chain decomposition between observable nodes. (Derived from existing results.)
6. **Series-parallel DAGs**: recursive decomposition. (Hypothesis, structurally motivated.)
7. **Bounded treewidth**: junction-tree exact inference. (Standard result, applied to AAD.)

### Principled Approximations

8. **Gradient-based attribution** is the most principled scheme: satisfies SA1, has sector parameter $\eta / \kappa(\mathbf{J})^2$, computable in $O(|V| + |E|)$. The condition-number penalty is inherent to coupled corrections (Prop B.5b).

9. **Proportional blame** is the marginal Bayesian point-estimate update, but violates SA1 with $O(1/n)$ bias. Useful as a quick approximation when directional fidelity suffices.

### Design Requirements

10. **Persistence is credit-assignment-free** (Prop B.5). Only the Jacobian is needed, not per-edge attribution.

11. **Per-edge calibration requires only directional fidelity**: the signal function must be bounded, asymptotically consistent, and directionally faithful beyond a threshold.

12. **The theory's formal guarantees require Level 0 (plan-level tracking). Practical agents need Level 1 (directional fidelity). Level 3 (exact Bayesian) is computationally unattainable in general.**

### Literature Connections

13. The gradient-based scheme is the AAD analog of policy gradient methods in RL.
14. The Jacobian bridge (Prop B.5) is the AAD analog of the score function in REINFORCE.
15. Do-calculus identifiability conditions translate to observability conditions on the strategy DAG.
16. Sampling-based Shapley approximation (KernelSHAP) is applicable to approximate attribution.

---

## 8. Path Forward

1. **Promote the gradient-based signal function to a hypothesis-grade segment.** It is the natural completion of #edge-update-via-gain's unspecified signal function. The segment should state the update rule, the sector parameter, and the condition-number penalty.

2. **Promote the identifiability result to a derived segment.** $\dim(\mathcal{I}(\mathcal{V}_{\text{obs}})) \leq |\mathcal{V}_{\text{obs}}|$ is a clean result connecting observability to credit-assignment tractability. It formalizes the content of #observability-dominance for strategy DAGs.

3. **Investigate the condition number.** Compute $\kappa(\mathbf{J})$ for the canonical DAG topologies (depth-$d$ AND-chain, $k$-arm OR-node, balanced binary tree). Determine whether $\kappa$ is bounded for "reasonable" strategies.

4. **Develop the mixed AND/OR sector condition.** This is the remaining gap between the four verified cases (Props B.1--B.4) and the general case. The gradient-based scheme provides a candidate update rule; the sector condition needs to be verified for the mixed case.

5. **Connect to observability investment.** Formalize the problem of choosing which nodes to make observable to maximize $\alpha_\Sigma$, and determine whether it has efficient (submodular) structure.
