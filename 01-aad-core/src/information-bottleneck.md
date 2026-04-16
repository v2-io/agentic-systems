---
slug: information-bottleneck
type: formulation
status: discussion-grade
depends:
  - agent-model
stage: deps-verified
---

# Formulation: Information Bottleneck

Optimal model compression balances retained history against predictive power; the information bottleneck objective provides a principled framework for understanding this trade-off.

## Formal Expression

*[Formulation (IB-objective)]*

$$\phi^* = \arg\min_{\phi} \left[ I(M_t;\, \mathcal{C}_t) - \beta \cdot I(M_t;\, o_{t+1:\infty} \mid a_{t:\infty}) \right]$$

where:
- $I(M_t;\, \mathcal{C}_t)$ is the compression cost — how much of the interaction history the model retains
- $I(M_t;\, o_{t+1:\infty} \mid a_{t:\infty})$ is the predictive power — how much the model tells the agent about future observations given future actions
- $\beta \gt 0$ is the trade-off parameter controlling the compression-prediction balance

**Dependence on volatility.** The trade-off $\beta$ depends on environment volatility $\rho$:

- **Volatile environments** (high $\rho$): favor aggressive compression (low $\beta$). Old information decays in relevance quickly, so retaining it wastes capacity.
- **Stable environments** (low $\rho$): favor dense retention (high $\beta$). Historical information remains predictive, so discarding it loses value.

## Epistemic Status

This is a *formulation* — it provides a principled framework for understanding compression trade-offs, not a claim about how actual agents compute their models. No agent explicitly solves this optimization (except in the variational IB literature, where it is a training objective). The formulation is analytically useful because it makes the compression-prediction trade-off explicit and connects model quality to information-theoretic quantities.

## Discussion

**The IB framework is not prescriptive.** It characterizes what an optimal $\phi$ would look like, not how to find one. Actual agents approximate this trade-off through diverse mechanisms: forgetting, attention, abstraction, summarization.

**Connection to model sufficiency.** The IB objective implicitly defines when a model is "good enough": when the predictive power term $I(M_t;\, o_{t+1:\infty} \mid a_{t:\infty})$ is close to its maximum (the full history's predictive power). This is formalized in #model-sufficiency.

**Policy-relativity.** The conditioning on $a_{t:\infty}$ makes the predictive power term policy-relative: it measures predictive information given a particular sequence of future actions, which depends on what policy the agent follows. The IB objective is therefore defined relative to a generating policy. This is inherent — what information is "predictive" depends on what the agent will do. #value-object's continuation-policy convention ($\pi_{\text{cont}}$) provides the specification for value computations; the same convention should be understood as implicit in the IB formulation. The $\beta$ parameter's dependence on volatility $\rho$ also has a policy component: an exploratory policy encounters more diverse situations, making more information predictively relevant (favoring retention), while an exploitative policy encounters a narrower distribution (favoring compression).

**Broader applicability.** The same IB principle applies beyond intra-agent compression. It governs inter-agent communication ( #shared-intent) — how much of one agent's model or strategy to transmit to another — and constrains the cognitive cost of maintaining a complex strategy. In each case, the trade-off is between the cost of retaining or transmitting information and the value of that information for future decisions.
