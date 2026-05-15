---
slug: def-shared-intent
type: definition
status: discussion-grade
depends:
  - def-unity-dimensions
  - form-information-bottleneck
  - form-objective-functional
stage: draft
---

# Definition: Shared Intent

When sub-agents within a composite must coordinate, they face a communication problem: transmitting the full objective $O_t$ and strategy $\Sigma_t$ is expensive (high bandwidth, high latency), but acting without any shared purpose wastes coordination potential. The Information Bottleneck ( #form-information-bottleneck) applied to inter-agent communication predicts an optimal compression: transmit enough of $G_t$ to align behavior, not more.

## Formal Expression

*[Definition (shared-intent)]*

Let $G_t^{\text{full}}$ be the source agent's complete purposeful state $(O_t, \Sigma_t)$. Let $G_t^{\text{shared}}$ be the compressed representation communicated to partners. The shared intent is the IB-optimal compression:

$$G_t^{\text{shared}} = \arg\min_{G_s} \left[ I(G_t^{\text{full}}; G_s) - \beta \cdot I(G_s; a_t^{\text{coordinated}}) \right]$$

where $a_t^{\text{coordinated}}$ is the jointly optimal action and $\beta$ controls the complexity-relevance tradeoff. At high $\beta$, the agent communicates more detail (approaching full model sharing). At low $\beta$, communication is minimal (approaching independent action).

The shared intent is the *minimal sufficient statistic* of the sender's purposeful state for predicting the jointly optimal coordination behavior.

## Epistemic Status

*Discussion-grade.* Max attainable: conditional (conditional on the IB framework being appropriate for inter-agent communication). The application of IB to inter-agent communication is structurally motivated — IB compresses optimally given a relevance criterion, and coordination relevance is the natural criterion — but the specific formulation assumes: (1) the sender knows the jointly optimal action (which requires knowing other agents' states), (2) the compression is lossless in the IB sense (real communication introduces noise, delay, and misinterpretation), (3) the $\beta$ parameter is fixed rather than dynamically adjusted. These are strong assumptions. The qualitative prediction (communicate purpose before plans before models) is more robust than the specific IB formulation.

## Discussion

**What gets compressed out.** The IB compression preferentially preserves:
1. Terminal objectives (what the agent is trying to achieve) — these are compact and change slowly
2. High-level strategy (which approach, not which specific steps) — moderate size, moderate change rate
3. Strategic details (specific edge credences in $\Sigma_t$) — large, change fast, low coordination value

**Connection to cognitive cost of $\Sigma_t$.** For agents with bounded communication capacity (bandwidth-limited channels, finite context windows), the DAG must be summarized for transmission. A 500-node strategy DAG cannot be shared in full; the IB compression identifies which structural features of the DAG matter for coordination.

**Organizational communication patterns.** Commander's intent in military doctrine is an empirical instantiation: the commander communicates *what* to achieve and *why*, not *how*. This is IB-optimal if objectives change slowly (low $\nu_O$) and strategies change fast (high $\nu_\Sigma$) — communicating objectives gives a long shelf life per bit transmitted.

## Working Notes
- The IB formulation assumes a single relevance variable ($a_t^{\text{coordinated}}$). In practice, coordination relevance is multi-dimensional: shared intent needs to support action coordination, conflict resolution, resource allocation, and adaptive replanning. A richer relevance variable might be needed.
- How does shared intent interact with 100% context turnover? An AI agent starting a new session needs to reconstruct $G_t^{\text{shared}}$ from persistent storage. The compression from full $G_t$ to shared intent is also useful for $M_t$ preservation ( #disc-m-preservation) — store the compressed version, not the full state.
