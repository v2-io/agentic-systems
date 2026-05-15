---
slug: form-information-bottleneck
type: formulation
status: exact
depends:
  - form-agent-model
  - def-action-transition
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

**Dependence on volatility (The $\beta$ vs $\rho$ distinction).** It is tempting to claim that the trade-off parameter $\beta$ must be actively lowered by the agent in highly volatile environments (high $\rho$) to favor aggressive compression. However, this is a double-counting error. The environment's volatility already natively degrades the mutual information $I(\mathcal{C}_t; o_{t+1:\infty})$ — old history mathematically loses its predictive power as $\rho$ increases. The optimal $\phi^\ast$ will automatically discard this useless old information even if the agent's preference parameter $\beta$ remains completely constant. 

Therefore, adjusting $\beta$ reflects changes in the agent's *internal cost of memory* or *computational capacity*, not changes in environmental volatility. The agent adapts its *actions* in response to $\rho$ (by increasing exploration to survive, see `#deriv-causal-ib-exploration`), but the optimal IB representation adapts to $\rho$ natively through the joint probability distribution.

## Epistemic Status

*Exact, applied external theorem.* The IB optimum and its rate-distortion characterization are an external result (Tishby, Pereira & Bialek 1999, "The information bottleneck method," *Proc. 37th Allerton*; with the rate-distortion / Lagrangian-dual reading standard, see Cover & Thomas §I.12–13). This segment is *not* a novel formulation: it is an exact statement of that theorem under AAD's binding $X = \mathcal{C}_t$, $T = M_t$, $Y = o_{t+1:\infty} \mid a_{t:\infty}$, with the Markov chain $Y - X - T$ holding by construction (the model state has access to history but not directly to future observations). The choice to characterize the optimal compression $\phi^\ast$ via IB rather than via, e.g., MDL or a Bayesian-sufficiency criterion is a *representational choice* (hence `type: formulation`); given that choice, the form of $\phi^\ast$ and its trade-off structure are exact consequences of the imported theorem.

What this segment is *not* a claim about: how actual agents compute their models. No agent explicitly solves the IB optimization (variational IB in deep-learning practice is a parametric approximation). The segment characterizes the optimum, not the procedure. The trade-off parameter $\beta$'s dependence on environmental volatility $\rho$ and policy $\pi$ stated above is at a different epistemic tier — the qualitative direction (volatile favors compression, stable favors retention) is *robust-qualitative* across agent classes; specific functional forms are not derived here.

Max attainable: *exact* for the IB-as-applied-theorem core (already at ceiling); *robust-qualitative* for the $\beta(\rho, \pi)$ dependence claims. The downstream use in #disc-compression-operations — treating IB as the shared shape of four AAD compression operations and deriving (P1) as the IB Lagrangian-dual — relies on this segment's exact reading; the cross-instance unification claim itself remains *robust-qualitative*, which is a property of #disc-compression-operations, not of this segment.

## Discussion

**The IB framework is not prescriptive.** It characterizes what an optimal $\phi$ would look like, not how to find one. Actual agents approximate this trade-off through diverse mechanisms: forgetting, attention, abstraction, summarization.

**Connection to model sufficiency.** The IB objective implicitly defines when a model is "good enough": when the predictive power term $I(M_t;\, o_{t+1:\infty} \mid a_{t:\infty})$ is close to its maximum (the full history's predictive power). This is formalized in #def-model-sufficiency.

**Policy-relativity.** The conditioning on $a_{t:\infty}$ makes the predictive power term policy-relative: it measures predictive information given a particular sequence of future actions, which depends on what policy the agent follows. The IB objective is therefore defined relative to a generating policy. This is inherent — what information is "predictive" depends on what the agent will do. #def-value-object's continuation-policy convention ($\pi_{\text{cont}}$) provides the specification for value computations; the same convention should be understood as implicit in the IB formulation. The $\beta$ parameter's dependence on volatility $\rho$ also has a policy component: an exploratory policy encounters more diverse situations, making more information predictively relevant (favoring retention), while an exploitative policy encounters a narrower distribution (favoring compression).

**Broader applicability.** The same IB principle applies beyond intra-agent compression. It governs inter-agent communication ( #def-shared-intent) — how much of one agent's model or strategy to transmit to another — and constrains the cognitive cost of maintaining a complex strategy. In each case, the trade-off is between the cost of retaining or transmitting information and the value of that information for future decisions.

**IB lineage vs. information-theoretic-MDP lineage — strategy-cost uses a sibling form.** The canonical IB objective $I(X; T) - \beta I(T; Y)$ carries Shannon mutual information on both sides (Tishby, Pereira & Bialek 1999; the present segment's $(X, T, Y) = (\mathcal C_t, M_t, o_{t+1:\infty} \mid a_{t:\infty})$ instance is of this form). AAD's strategy-cost objective (`#form-strategy-complexity-cost`, `#deriv-strategy-cost-regret-bound`) uses a **different relevance-term shape**: its relevance term is a KL divergence $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ to a *target policy*, not a mutual information to an observable. This is not an inconsistency or an "abandonment of IB" — the strategy-cost compression sits in the parallel **information-theoretic-MDP lineage** (Tishby & Polani 2011 "The Information Theory of Decision and Action," *Perception-Action Cycle* Springer; Rubin, Shamir & Tishby 2012 "Trading value and information in MDPs," *Decision Making with Imperfect Decision Makers* Springer; Levine 2018 arXiv:1805.00909 for the control-as-inference reading). Both lineages descend from Shannon rate-distortion theory and admit Lagrangian relaxation; the choice of fidelity term depends on whether the compressed variable should preserve information about an observable (IB form: MI-to-relevance-variable) or match a target policy (IT-MDP form: KL-to-reference-policy). AAD's compression-operations framework ( #disc-compression-operations) uses the IB form for $M_t$, $G_t^{\mathrm{shared}}$, and $\Lambda$ compressions; the strategy-cost compression uses the IT-MDP form, with the $\pi^\ast$-first direction forced by a regret-bound argument specific to decision-theoretic scope (see `#deriv-strategy-cost-regret-bound` §§5, 6.4). The two lineages are siblings via their shared rate-distortion ancestor; neither reduces to the other without a change of relevance variable.

**Connection to variational free energy.** The IB objective stated above is the rate-distortion specialization of the variational free energy decomposition $-F = \text{accuracy} - \text{complexity}$ used in active inference (Friston 2010, "The free-energy principle: a unified brain theory?", *Nature Reviews Neuroscience* 11; Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29; Parr & Pezzulo 2022, *Active Inference*, MIT Press, ch. 2): the compression cost $I(M_t; \mathcal{C}_t)$ corresponds to the complexity term (KL between posterior and prior over latent states); the negative predictive power $-I(M_t; o_{t+1:\infty})$ corresponds to the accuracy term (negative expected log-likelihood). The two formulations are related under the Markov-chain factorization $Y - X - T$ (Tishby & Zaslavsky 2015, "Deep learning and the information bottleneck principle," *IEEE ITW*, makes the deep-learning instantiation explicit). AAD adopts the IB form as the rate-distortion characterization of optimal compression; the variational free-energy form is the AI-side cousin and motivates the variational treatment of strategy compression in #form-strategy-complexity-cost and the broader four-instance framing in #disc-compression-operations. AAD borrows the form without committing to AI's preferences-as-priors stance or to expected free energy as master objective.
