---
slug: strategic-calibration
type: definition
status: discussion-grade
depends:
  - strategy-dag
  - value-object
stage: draft
---

# Definition: Strategic Calibration

The strategic calibration residual measures whether the strategy's causal model is correct: are the edges in $\Sigma_t$ accurate predictors of how much value each step actually produces? This is the fine-grained diagnostic that localizes control regret to specific parts of the strategy.

## Formal Expression

*[Definition (strategic-calibration)]*

For each edge $(i, j)$ in $\Sigma_t$ with credence $p_{ij}$, the **edge residual**:

$$r_{ij} = \mathbb{E}[\Delta V_O \mid \text{edge } (i,j) \text{ traversed},\, M_t] - \Delta V_O^{\text{observed}}$$

where $\Delta V_O$ is the change in $V_O(M_t, \pi;\, N_h)$ attributable to completing step $j$ — as predicted by $\Sigma_t$ versus as observed.

The **strategic calibration residual** aggregates across active edges:

$$\delta_{\text{strategic}} = \left(\sum_{(i,j) \in \text{active}} w_{ij} \cdot r_{ij}^2 \right)^{1/2}$$

where $w_{ij}$ weights edges by importance (e.g., criticality to the current plan's critical path).

**Conditioning.** The edge residual $r_{ij}$ is meaningful only when:
- The edge was actually traversed (the agent attempted the step)
- $M_t$ is adequate (so the observed $\Delta V_O$ is meaningful, not noise)
- The agent followed $\Sigma_t$'s prescription for step $j$ (execution fidelity — otherwise the residual conflates bad plan with bad execution)

Without the execution fidelity condition, a positive residual could mean "the plan is wrong" or "the agent didn't follow the plan." These require different corrections ($\Sigma_t$ revision vs. execution improvement).

## Epistemic Status

*Discussion-grade.* The edge residual concept is well-motivated: each edge predicts a value increment, and comparing prediction to observation is standard calibration. But the specific aggregation ($L^2$ norm with importance weights) is a reasonable first pass, not a derived result. The weighting scheme ($w_{ij}$ by criticality) is sensible but ungrounded. The conditioning requirements (especially execution fidelity) make this quantity hard to estimate in practice — the agent must know whether it followed its own plan, which requires a level of self-monitoring that many agents lack.

This is a **second-order inference** — it requires accumulating evidence over multiple edge traversals. It is inherently slower to evaluate than $\delta_{\text{epistemic}}$ (which updates on every observation) or $\delta_{\text{sat}}$ (which can be evaluated from $M_t$ and $\Sigma_t$ alone).

## Discussion

**Connection to #strategy-persistence-schema.** There are two distinct strategic mismatch quantities:

1. **Plan-confidence error** $\delta_s = \hat P_\Sigma - \Phi$ — the scalar gap between the agent's plan-confidence score and the independence-model plan value at true edge parameters. Computable from status propagation alone, without credit assignment. The sector condition transfers to $\delta_s$ (Prop B.5 in #strategic-dynamics-derivation). Note: $\Phi$ is the AND/OR propagation formula evaluated at true edge rates — it equals actual plan success probability only when the DAG is causally sufficient (L0 of the Correlation Hierarchy in #strategy-dag). Under correlated failure (causally insufficient DAG, the dominant real-world case), $\Phi$ overestimates actual success. $\delta_s$ tracks calibration *within the independence model*, not calibration to strategic reality. For L1 (augmented DAGs with explicit common-cause nodes), $\delta_s$ of the augmented graph tracks calibration within the augmented model, which is more accurate.

2. **Strategic calibration residual** $\delta_{\text{strategic}}$ (this segment) — an $L^2$ aggregation of per-edge value-increment residuals requiring credit assignment to compute.

These are related (both measure strategy-reality mismatch) but not interchangeable. $\delta_s$ is the proven persistence target; $\delta_{\text{strategic}}$ provides finer-grained diagnostics but its persistence properties remain open, pending the credit-assignment machinery in #credit-assignment-boundary. The correction function for both is edge-credence revision ( #edge-update-via-gain); the disturbance is environmental changes that alter edge-traversal outcomes.

**Typing as value-increment residuals.** Each edge predicts a scalar (value increment), not a full state transition. This is the most tractable typing because it connects directly to the value object $V_O$ and allows aggregation across heterogeneous step types (a military advance and a logistics delivery produce different state changes but both produce value increments measurable on the same scale).

**Credit-assignment problem.** The edge residual $r_{ij}$ subtracts "predicted value increment" from "observed value change." These are different types: the prediction comes from $\Sigma_t$'s internal causal model, while the observation comes from empirical measurement of $\Delta V_O$. The subtraction is meaningful only when the observed value change can be *attributed to the specific edge* — a credit-assignment problem the current formulation does not address. For edges with a single parent, attribution is straightforward. For multi-parent AND/OR nodes, the observed $\Delta V_O$ at the child reflects the combined effect of all parent edges, and decomposing it into per-edge contributions requires additional structure (e.g., Shapley-value decomposition, or sequential observation of parent completions). In the absence of clean attribution, $r_{ij}$ measures "how well did the overall prediction work?" rather than "how well did this specific edge predict?" — still useful for aggregate calibration, but not sufficient for targeted edge revision.

## Working Notes

- The aggregation into a single $\delta_{\text{strategic}}$ may lose important structure. A per-edge or per-path profile of residuals would be more informative for diagnosis: which parts of the strategy are well-calibrated and which are not? The scalar summary is useful for the persistence condition (which needs a single mismatch magnitude) but not for strategy revision (which needs to know WHERE the problem is).
- Alternative aggregation: maximum edge residual (worst-calibrated edge), or weighted by information value (edges the agent is most uncertain about). The right aggregation depends on the use case.
- Execution fidelity monitoring is a genuine challenge for agents that don't have a clear execution trace. For software agents operating through tool calls, execution fidelity is relatively easy to assess (did the agent issue the right commands?). For organizational agents, it's much harder (did the subordinate actually follow the directive, or reinterpret it?).
