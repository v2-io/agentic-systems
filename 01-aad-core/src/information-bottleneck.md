---
slug: information-bottleneck
type: formulation
status: exact
depends:
  - agent-model
stage: draft
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

*Exact, applied external theorem.* The IB optimum and its rate-distortion characterization are an external result (Tishby, Pereira & Bialek 1999, "The information bottleneck method," *Proc. 37th Allerton*; with the rate-distortion / Lagrangian-dual reading standard, see Cover & Thomas §I.12–13). This segment is *not* a novel formulation: it is an exact statement of that theorem under AAD's binding $X = \mathcal{C}_t$, $T = M_t$, $Y = o_{t+1:\infty} \mid a_{t:\infty}$, with the Markov chain $Y - X - T$ holding by construction (the model state has access to history but not directly to future observations). The choice to characterize the optimal compression $\phi^\ast$ via IB rather than via, e.g., MDL or a Bayesian-sufficiency criterion is a *representational choice* (hence `type: formulation`); given that choice, the form of $\phi^\ast$ and its trade-off structure are exact consequences of the imported theorem.

What this segment is *not* a claim about: how actual agents compute their models. No agent explicitly solves the IB optimization (variational IB in deep-learning practice is a parametric approximation). The segment characterizes the optimum, not the procedure. The trade-off parameter $\beta$'s dependence on environmental volatility $\rho$ and policy $\pi$ stated above is at a different epistemic tier — the qualitative direction (volatile favors compression, stable favors retention) is *robust-qualitative* across agent classes; specific functional forms are not derived here.

Max attainable: *exact* for the IB-as-applied-theorem core (already at ceiling); *robust-qualitative* for the $\beta(\rho, \pi)$ dependence claims. The downstream use in #compression-operations — treating IB as the shared shape of four AAD compression operations and deriving (P1) as the IB Lagrangian-dual — relies on this segment's exact reading; the cross-instance unification claim itself remains *robust-qualitative*, which is a property of #compression-operations, not of this segment.

## Discussion

**The IB framework is not prescriptive.** It characterizes what an optimal $\phi$ would look like, not how to find one. Actual agents approximate this trade-off through diverse mechanisms: forgetting, attention, abstraction, summarization.

**Connection to model sufficiency.** The IB objective implicitly defines when a model is "good enough": when the predictive power term $I(M_t;\, o_{t+1:\infty} \mid a_{t:\infty})$ is close to its maximum (the full history's predictive power). This is formalized in #model-sufficiency.

**Policy-relativity.** The conditioning on $a_{t:\infty}$ makes the predictive power term policy-relative: it measures predictive information given a particular sequence of future actions, which depends on what policy the agent follows. The IB objective is therefore defined relative to a generating policy. This is inherent — what information is "predictive" depends on what the agent will do. #value-object's continuation-policy convention ($\pi_{\text{cont}}$) provides the specification for value computations; the same convention should be understood as implicit in the IB formulation. The $\beta$ parameter's dependence on volatility $\rho$ also has a policy component: an exploratory policy encounters more diverse situations, making more information predictively relevant (favoring retention), while an exploitative policy encounters a narrower distribution (favoring compression).

**Broader applicability.** The same IB principle applies beyond intra-agent compression. It governs inter-agent communication ( #shared-intent) — how much of one agent's model or strategy to transmit to another — and constrains the cognitive cost of maintaining a complex strategy. In each case, the trade-off is between the cost of retaining or transmitting information and the value of that information for future decisions.

**Connection to variational free energy.** The IB objective stated above is the rate-distortion specialization of the variational free energy decomposition $-F = \text{accuracy} - \text{complexity}$ used in active inference (Friston 2010, "The free-energy principle: a unified brain theory?", *Nature Reviews Neuroscience* 11; Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29; Parr & Pezzulo 2022, *Active Inference*, MIT Press, ch. 2): the compression cost $I(M_t; \mathcal{C}_t)$ corresponds to the complexity term (KL between posterior and prior over latent states); the negative predictive power $-I(M_t; o_{t+1:\infty})$ corresponds to the accuracy term (negative expected log-likelihood). The two formulations are related under the Markov-chain factorization $Y - X - T$ (Tishby & Zaslavsky 2015, "Deep learning and the information bottleneck principle," *IEEE ITW*, makes the deep-learning instantiation explicit). AAD adopts the IB form as the rate-distortion characterization of optimal compression; the variational free-energy form is the AI-side cousin and motivates the variational treatment of strategy compression in #strategy-complexity-cost and the broader four-instance framing in #compression-operations. AAD borrows the form without committing to AI's preferences-as-priors stance or to expected free energy as master objective.
