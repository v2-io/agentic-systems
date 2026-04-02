---
slug: credit-assignment-boundary
type: discussion
status: discussion-grade
depends:
  - strategy-dag
  - edge-update-via-gain
  - strategic-calibration
  - observability-dominance
  - gain-sector-bridge
  - strategic-dynamics-derivation
stage: draft
---

# Discussion: Credit Assignment Boundary

The strategy-revision loop requires assigning credit for observed outcomes to specific edges in the strategy DAG — decomposing "the plan partially worked" into "step 3 failed, step 5 was irrelevant, step 1 succeeded." This is ACT's version of RL's temporal credit assignment problem. This segment characterizes the boundary between tractable and intractable cases, states what the theory requires of any credit-assignment scheme, and identifies what the theory can guarantee without solving the problem at all.

## Formal Expression

### The Credit Assignment Problem for Strategy DAGs

*[Discussion (credit-assignment-problem)]*

Given strategy DAG $\Sigma_t = (V, E, p, \gamma)$, an observed outcome at the root (and possibly at some intermediate nodes), produce per-edge signals $\text{signal}(o_t, i, j)$ for each edge $(i,j) \in E$ such that the edge update

$$p_{ij}^{\text{new}} = p_{ij} + \eta_{\text{edge}} \cdot (\text{signal}(o_t, i, j) - p_{ij})$$

drives credences toward truth. The problem is trivial when all intermediates are observable (each edge updates from its own observation) and genuinely hard when intermediates are unobservable and the DAG has shared structure.

### What the Theory Can Guarantee Without Solving Credit Assignment

Three results hold independently of any specific credit-assignment scheme:

**1. Persistence is credit-assignment-free.** Proposition B.5 in #strategic-dynamics-derivation shows that the sector condition transfers from per-edge credence space to the value-residual diagnostic $\delta_{\text{strategic}}$ via the Jacobian $\mathbf{J} = \nabla_\mathbf{p} P_\Sigma$. The Jacobian is computable from status propagation in $O(\lvert V\rvert + \lvert E\rvert)$ — no outcome decomposition required. The persistence guarantee (whether the strategy can be maintained) does not depend on the agent's ability to attribute outcomes to edges.

**2. The diagnostic framework is plan-level.** The satisfaction gap ( #satisfaction-gap), control regret ( #control-regret), and the orient cascade ordering ( #orient-cascade) operate on aggregate value, not per-edge quantities. They tell the agent *whether* the strategy is failing (and whether the failure is feasibility vs. optimality vs. calibration), without requiring per-edge attribution.

**3. Observability-dominance identifies the tractable edges.** #observability-dominance determines which edges have nonzero observability — only these can receive informative signals. Edges with zero observability are frozen regardless of the credit-assignment scheme. The tractable boundary is the observable subgraph of $\Sigma_t$.

### The Tractable Cases

*[Discussion (tractable-credit-assignment)]*

Credit assignment is solved (exact, polynomial-time) when:

| Condition | Why tractable | Update rule |
|---|---|---|
| **All intermediates observable** | Each edge has its own observation; updates decouple | Beta-Bernoulli per edge (Prop B.2) |
| **Binary outcomes, independent edges, linear chain** | Marginal Bayesian update = proportional blame | Prop B.3 (with plan-level fallback for unobservable) |
| **Tree DAG, observable leaves** | No shared descendants; message passing is exact | Belief propagation (standard) |

### The Expected Intractable Cases

*[Discussion (intractable-credit-assignment, sketch)]*

Exact per-edge attribution in general AND/OR DAGs with partial observability is expected to be computationally hard. The structural argument: the "contribution of edge $k$ to the observed outcome" has the form of a Shapley value over a cooperative game defined by the AND/OR propagation. Shapley value computation for general coalitional games is \#P-complete (Deng and Papadimitriou, 1994). If the AND/OR propagation game reduces to a general weighted threshold game, the hardness transfers.

Beyond computational hardness, there is an information-theoretic issue: when intermediates are unobservable, per-edge attribution is *underdetermined*, not just hard. Multiple distinct edge-credence vectors produce the same root-level observation distribution. The system of equations is rank-deficient — the observations do not carry enough information to uniquely identify which edges failed. This is not a limitation of any algorithm but a structural property of partial observability.

### The Design Requirement

*[Discussion (credit-assignment-design-requirement)]*

The theory does not prescribe a specific credit-assignment scheme. It states what any scheme must satisfy for the persistence guarantees to hold:

**Minimal requirement (from #gain-sector-bridge):** The per-edge signal function must have **directional fidelity** — the expected update for each edge must point toward the true credence:

$$\mathbb{E}[(\text{signal}(o_t, i, j) - p_{ij}) \cdot (p_{ij} - \theta_{ij})] \leq 0$$

(the expected correction is non-positively correlated with the current error). This is the per-component version of condition B1 from the bridge theorem. Any signal function satisfying this produces sector-satisfying corrections that transfer losslessly to value space (Prop B.5b, componentwise case).

**Sufficient condition for persistence:** Per-component directional fidelity + bounded gain ($\eta_{\text{edge}} > 0$). The theory guarantees persistence when these hold, regardless of how the signals are computed.

**What's NOT required:** Exact attribution, unbiased estimation, minimum-variance estimation, or optimality of any kind. The persistence guarantee is robust to approximation — a sloppy but directionally correct signal function still produces bounded strategic mismatch. The *quality* of the approximation affects the *tightness* of the persistence bound (how close $R^\ast_\Sigma$ is to zero), not whether persistence holds at all.

## Epistemic Status

*Discussion-grade.* This segment characterizes a boundary, not a result. The tractable cases are derived (Props B.2-B.4 in #strategic-dynamics-derivation). The intractable cases are structurally motivated (the Shapley connection is a sketch, not a formal reduction). The design requirement is derived from the bridge theorem ( #gain-sector-bridge, #strategic-dynamics-derivation Prop B.5).

Max attainable: *conditional* — with a formal intractability reduction, the boundary characterization could be promoted. The design requirement is already exact (it follows from the bridge theorem).

## Discussion

**ACT characterizes the structure, not the algorithm.** The theory's contribution to credit assignment is not a solution but a characterization: when it's trivial (observable intermediates), when it's hard (general partial observability), what any solution must satisfy (directional fidelity), and what guarantees hold without it (persistence, plan-level diagnostics). This is the right level of ambition for a theory of adaptive systems — the specific algorithm is domain-specific engineering; the structural characterization is universal.

**The analogy to the gain principle.** #update-gain characterizes the optimal gain structure ($\eta^\ast = U_M/(U_M + U_o)$) without prescribing how $U_M$ and $U_o$ are estimated. A Kalman filter computes them exactly; an RL agent approximates them; a human intuits them. The gain *principle* is theory; the gain *estimator* is engineering. Credit assignment has the same structure: the *requirement* (directional fidelity) is theory; the *implementation* (proportional blame, gradient attribution, belief propagation) is engineering.

**The observability lever.** The most powerful insight from this analysis is that credit assignment is primarily an *observability design problem*, not an algorithm design problem. An agent that designs its strategy with observable intermediates (instrumented plans, staged rollouts, checkpoints) sidesteps the intractability entirely. This connects to #observability-dominance's practical guidance: invest in making intermediate states observable, because unobservable regions are both epistemically dead (frozen credences) and computationally intractable (no efficient attribution).

## Working Notes

- A formal reduction from AND/OR credit assignment to Shapley value computation would promote the intractability claim from sketch to derived. The key step: mapping the AND/OR propagation to a weighted threshold game.
- The proportional-blame heuristic (attribute in proportion to prior credence) satisfies directional fidelity for independent edges. Does it satisfy directional fidelity in general? The two-edge analysis (B.3) shows it introduces O(1/n) bias — which means it has directional fidelity in expectation but not per-step. Whether the expected-value directional fidelity is sufficient for the sector condition (it should be, since the sector condition is also stated in expectation) is worth verifying formally.
- Gradient-based attribution ($\text{signal}_k = \partial P_\Sigma / \partial p_k \cdot \text{root outcome residual}$) is a natural candidate that uses the Jacobian already computed for the persistence analysis. It satisfies directional fidelity when the DAG is monotone (which AND/OR DAGs are). Whether it gives better persistence bounds than proportional blame is an open question.
- The connection between ACT's credit assignment and RL's temporal credit assignment (TD learning, eligibility traces) deserves formal treatment. Both face the same structural problem (partial observability of the causal chain) and both use similar heuristics (discounted attribution to recent actions). ACT's DAG structure is richer than RL's linear temporal chain, which may make the problem harder but also provides more structural information.
