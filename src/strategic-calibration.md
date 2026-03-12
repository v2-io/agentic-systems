---
slug: strategic-calibration
type: definition
status: discussion-grade
depends:
  - strategy-dag
  - value-object
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

**Connection to #strategy-persistence-schema.** $\delta_{\text{strategic}}$ is the candidate strategic mismatch state for the persistence schema. The correction function would be edge-credence revision (reducing $p_{ij}$ when $r_{ij}$ is persistently positive, increasing when consistently negative — see #edge-update-via-gain). The disturbance would be environmental changes that alter edge-traversal outcomes. Whether this correction satisfies the sector condition remains open.

**Typing as value-increment residuals.** Each edge predicts a scalar (value increment), not a full state transition. This is the most tractable typing because it connects directly to the value object $V_O$ and allows aggregation across heterogeneous step types (a military advance and a logistics delivery produce different state changes but both produce value increments measurable on the same scale).

## Working Notes

- The aggregation into a single $\delta_{\text{strategic}}$ may lose important structure. A per-edge or per-path profile of residuals would be more informative for diagnosis: which parts of the strategy are well-calibrated and which are not? The scalar summary is useful for the persistence condition (which needs a single mismatch magnitude) but not for strategy revision (which needs to know WHERE the problem is).
- Alternative aggregation: maximum edge residual (worst-calibrated edge), or weighted by information value (edges the agent is most uncertain about). The right aggregation depends on the use case.
- Execution fidelity monitoring is a genuine challenge for agents that don't have a clear execution trace. For software agents operating through tool calls, execution fidelity is relatively easy to assess (did the agent issue the right commands?). For organizational agents, it's much harder (did the subordinate actually follow the directive, or reinterpret it?).
