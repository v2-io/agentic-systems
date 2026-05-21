# Cluster Reference: Information Bottleneck Unification

**Overview:** Demonstrates how the Information Bottleneck principle serves as a unified compression and objective framework across the agent's reality model, strategy, and communication channels.

---

## Canonical Source Segments

### Source: `form-information-bottleneck.md`

```yaml
---
slug: form-information-bottleneck
type: formulation
status: exact
depends:
  - form-agent-model
  - def-action-transition
stage: draft
---
```


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

*Exact, applied external theorem.* The IB optimum and its rate-distortion characterization are an external result (Tishby, Pereira & Bialek 1999, "The information bottleneck method," *Proc. 37th Allerton*; with the rate-distortion / Lagrangian-dual reading standard, see Cover & Thomas §I.12–13). This segment is *not* a novel formulation: it is an exact statement of that theorem under AAT's binding $X = \mathcal{C}_t$, $T = M_t$, $Y = o_{t+1:\infty} \mid a_{t:\infty}$, with the Markov chain $Y - X - T$ holding by construction (the model state has access to history but not directly to future observations). The choice to characterize the optimal compression $\phi^\ast$ via IB rather than via, e.g., MDL or a Bayesian-sufficiency criterion is a *representational choice* (hence `type: formulation`); given that choice, the form of $\phi^\ast$ and its trade-off structure are exact consequences of the imported theorem.

What this segment is *not* a claim about: how actual agents compute their models. No agent explicitly solves the IB optimization (variational IB in deep-learning practice is a parametric approximation). The segment characterizes the optimum, not the procedure. The trade-off parameter $\beta$'s dependence on environmental volatility $\rho$ and policy $\pi$ stated above is at a different epistemic tier — the qualitative direction (volatile favors compression, stable favors retention) is *robust-qualitative* across agent classes; specific functional forms are not derived here.

Max attainable: *exact* for the IB-as-applied-theorem core (already at ceiling); *robust-qualitative* for the $\beta(\rho, \pi)$ dependence claims. The downstream use in #disc-compression-operations — treating IB as the shared shape of four AAT compression operations and deriving (P1) as the IB Lagrangian-dual — relies on this segment's exact reading; the cross-instance unification claim itself remains *robust-qualitative*, which is a property of #disc-compression-operations, not of this segment.

## Discussion

**The IB framework is not prescriptive.** It characterizes what an optimal $\phi$ would look like, not how to find one. Actual agents approximate this trade-off through diverse mechanisms: forgetting, attention, abstraction, summarization.

**Connection to model sufficiency.** The IB objective implicitly defines when a model is "good enough": when the predictive power term $I(M_t;\, o_{t+1:\infty} \mid a_{t:\infty})$ is close to its maximum (the full history's predictive power). This is formalized in #def-model-sufficiency.

**Policy-relativity.** The conditioning on $a_{t:\infty}$ makes the predictive power term policy-relative: it measures predictive information given a particular sequence of future actions, which depends on what policy the agent follows. The IB objective is therefore defined relative to a generating policy. This is inherent — what information is "predictive" depends on what the agent will do. #def-value-object's continuation-policy convention ($\pi_{\text{cont}}$) provides the specification for value computations; the same convention should be understood as implicit in the IB formulation. The $\beta$ parameter's dependence on volatility $\rho$ also has a policy component: an exploratory policy encounters more diverse situations, making more information predictively relevant (favoring retention), while an exploitative policy encounters a narrower distribution (favoring compression).

**Broader applicability.** The same IB principle applies beyond intra-agent compression. It governs inter-agent communication ( #def-shared-intent) — how much of one agent's model or strategy to transmit to another — and constrains the cognitive cost of maintaining a complex strategy. In each case, the trade-off is between the cost of retaining or transmitting information and the value of that information for future decisions.

**IB lineage vs. information-theoretic-MDP lineage — strategy-cost uses a sibling form.** The canonical IB objective $I(X; T) - \beta I(T; Y)$ carries Shannon mutual information on both sides (Tishby, Pereira & Bialek 1999; the present segment's $(X, T, Y) = (\mathcal C_t, M_t, o_{t+1:\infty} \mid a_{t:\infty})$ instance is of this form). AAT's strategy-cost objective (`#form-strategy-complexity-cost`, `#deriv-strategy-cost-regret-bound`) uses a **different relevance-term shape**: its relevance term is a KL divergence $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ to a *target policy*, not a mutual information to an observable. This is not an inconsistency or an "abandonment of IB" — the strategy-cost compression sits in the parallel **information-theoretic-MDP lineage** (Tishby & Polani 2011 "The Information Theory of Decision and Action," *Perception-Action Cycle* Springer; Rubin, Shamir & Tishby 2012 "Trading value and information in MDPs," *Decision Making with Imperfect Decision Makers* Springer; Levine 2018 arXiv:1805.00909 for the control-as-inference reading). Both lineages descend from Shannon rate-distortion theory and admit Lagrangian relaxation; the choice of fidelity term depends on whether the compressed variable should preserve information about an observable (IB form: MI-to-relevance-variable) or match a target policy (IT-MDP form: KL-to-reference-policy). AAT's compression-operations framework ( #disc-compression-operations) uses the IB form for $M_t$, $G_t^{\mathrm{shared}}$, and $\Lambda$ compressions; the strategy-cost compression uses the IT-MDP form, with the $\pi^\ast$-first direction forced by a regret-bound argument specific to decision-theoretic scope (see `#deriv-strategy-cost-regret-bound` §§5, 6.4). The two lineages are siblings via their shared rate-distortion ancestor; neither reduces to the other without a change of relevance variable.

**Connection to variational free energy.** The IB objective stated above is the rate-distortion specialization of the variational free energy decomposition $-F = \text{accuracy} - \text{complexity}$ used in active inference (Friston 2010, "The free-energy principle: a unified brain theory?", *Nature Reviews Neuroscience* 11; Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29; Parr & Pezzulo 2022, *Active Inference*, MIT Press, ch. 2): the compression cost $I(M_t; \mathcal{C}_t)$ corresponds to the complexity term (KL between posterior and prior over latent states); the negative predictive power $-I(M_t; o_{t+1:\infty})$ corresponds to the accuracy term (negative expected log-likelihood). The two formulations are related under the Markov-chain factorization $Y - X - T$; the variational bound that makes this relation operational — connecting the IB Lagrangian to the variational machinery shared with free-energy methods — is established by Alemi, Fischer, Dillon & Murphy 2017 ("Deep Variational Information Bottleneck," ICLR 2017, arXiv:1612.00410), with Tishby & Zaslavsky 2015 ("Deep learning and the information bottleneck principle," *IEEE ITW*) giving the deep-learning instantiation of IB itself. AAT adopts the IB form as the rate-distortion characterization of optimal compression; the variational free-energy form is the AI-side cousin and motivates the variational treatment of strategy compression in #form-strategy-complexity-cost and the broader four-instance framing in #disc-compression-operations. AAT borrows the form without committing to AI's preferences-as-priors stance or to expected free energy as master objective.


---

### Source: `disc-ciy-unified-objective.md`

```yaml
---
slug: disc-ciy-unified-objective
type: discussion
status: discussion-grade
depends:
  - def-causal-information-yield
  - scope-ciy-observational-proxy
  - def-value-object
  - der-action-selection
stage: draft
---
```


# Discussion: CIY Unified Policy Objective

The exploration-exploitation tension can be expressed as a single policy objective that jointly maximizes expected value and a causal information surrogate. This formulation is *heuristic* — CIY measures action-distinguishability, not expected information gain (see #def-causal-information-yield), so the objective selects for causally distinctive actions rather than maximally informative ones. The $\lambda$-weighting partially compensates by suppressing the CIY term when model uncertainty is low, but the surrogate nature is inherent.

## Formal Expression

*[Discussion (unified-policy-objective — heuristic)]*

$$\pi^\ast(M_t) = \arg\max_a \left[\mathbb{E}[\text{value}(a) \mid M_t] + \lambda(M_t) \cdot \text{CIY}_q(a;\, M_t)\right]$$

The first term is exploitation (expected value given current model). The second is a *heuristic exploration term* using CIY as a surrogate for expected information gain ( #def-causal-information-yield). CIY measures how different the action's outcome distribution is from alternatives — this is action-distinguishability, not learning value. The surrogate is reasonable when $U_M$ is high (distinguishable actions are also informative to an uncertain agent) and poor when $U_M$ is low (distinguishable actions teach nothing to a confident agent). $\lambda(M_t)$ controls the balance:

- High $U_M$ (uncertain model) → large $\lambda$ — exploration is valuable
- Low $U_M$ (confident model) → small $\lambda$ — exploitation dominates
- Long time horizon → larger $\lambda$ — information compounds
- High $\rho$ (fast-changing environment) → larger $\lambda$ — perpetual uncertainty

$\lambda$ carries units of [value per unit information]. In specific domains it reduces to known quantities:

| Domain | $\lambda$ reduces to | Status |
|--------|---------------------|--------|
| Bayesian bandits | Gittins index | Exactly derived |
| Kalman dual control | Probing cost in quadratic objective | Exactly derived |
| Active inference | Precision on epistemic affordance | Framework-derived |
| Information-directed sampling | $(\text{VoI})^2 / \text{info gain}$ | Exactly derived (Russo & Van Roy) |
| RL with UCB | Confidence-bound scaling | Heuristic (tuned) |

**Identifiability gate.** Before incorporating CIY into the policy objective: (1) action variation must exist, (2) the admissibility regime must be identified ( #scope-ciy-observational-proxy), (3) the reference distribution $q$ must be specified, (4) local stationarity must hold. If any condition fails, CIY-based terms should be dropped or replaced with simpler uncertainty-based heuristics (UCB-style bonuses, ensemble disagreement).

## Epistemic Status

*Discussion-grade summary; underlying derivation is exact.* Originally treated as a discussion-grade heuristic, the unified objective has now been formally derived as the exact Lagrangian relaxation of the Linear Matrix Inequality (LMI) governing Lyapunov persistence (see `#deriv-causal-ib-lmi`).

The scalar heuristic $Q_O(a) + \lambda \cdot \text{CIY}(a)$ is formally superseded by the exact tensor trace-product:
$$ a_t^\ast = \arg\max_a \left[ Q_O(a) + \text{Tr}\left( \Lambda \cdot \mathcal{I}_o(a) \right) \right] $$
where $\mathcal I_o(a)$ is the Fisher Information Matrix (Matrix CIY) and $\Lambda$ is the positive-semidefinite shadow price matrix of the survival constraint.

Max attainable for this segment: *discussion-grade* (it is a discussion of the underlying result, per `type: discussion`). Max attainable for the underlying derivation in `#deriv-causal-ib-lmi`: *exact*. The structural form is fully grounded in AAT's physical survival bounds and standard semidefinite programming, eliminating the need to treat exploration as an ad-hoc heuristic.

## Discussion

**Two Parallel Exploration Drives.** AAT dictates two correlated but distinct motivations for exploration, acting at opposite ends of the uncertainty spectrum:
1. **Epistemic Information Gain ($\lambda_{\text{info}} \propto U_M$):** The primary CIY formulation. The agent explores to reduce its model uncertainty. This drive dominates when $U_M$ is high.
2. **The Survival Imperative ($\lambda_{\text{surv}} \propto 1/U_M$):** As mathematically proven in `#deriv-causal-ib-exploration`, an agent with high confidence (low $U_M$) in a drifting environment ($\rho \gt 0$) mathematically guarantees its own death by ignoring noisy observations. To force the necessary correction, the Lyapunov persistence constraint dictates an immense shadow price ($\lambda_{\text{surv}} \to \infty$ as $U_M \to 0$) forcing the agent to seek unambiguous observations (low $U_o$ / high CIY).

The dark-room problem is bypassed entirely by the Survival Imperative: exploration is not driven by preferences-as-priors, but by the literal physical boundaries of the Lyapunov sector constraint.

**Connection to the zero-mismatch ambiguity.** An agent that only exploits (acts to maximize predicted value) will tend toward confirmation bias — observing only what its model already explains ( #def-mismatch-signal, zero-mismatch ambiguity case (b)). Exploration via CIY-maximizing actions is the mechanism by which the agent actively tests its model.

**Connection to Section II.** For actuated agents, the exploration-exploitation tension extends to three modes: exploit (pursue $O_t$ via $\Sigma_t$), explore (improve $M_t$), deliberate (revise $\Sigma_t$). The CIY framework provides the information-theoretic grounding for why strategy edges ( #def-strategy-dag) need observational access ( #der-observability-dominance) — edges the agent cannot observe have frozen CIY.

**Connection to active inference.** The expected free energy (EFE) in active inference (Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29; Da Costa, Parr, Sajid, Veselic, Neacsu & Friston 2020, "Active inference on discrete state-spaces," *J. Math. Psych.* 99; Sajid, Ball, Parr & Friston 2021, "Active inference: demystified and compared," *Neural Computation* 33) decomposes into *pragmatic value* (preferences-aligned outcomes) and *epistemic value* (expected information gain about hidden states). AAT's unified objective is structurally isomorphic: $Q_O$ ≈ pragmatic, CIY ≈ epistemic. The convergence is at the shared-shape level — objective decomposes into value-and-information terms — not unified content. Two substantive differences remain. First, AAT grounds exploration in explicitly *causal* information (action-distinguishability under $do$) rather than entropy reduction over hidden states — not all uncertainty reduction is equally valuable for purposeful action; causal information specifically enables better *intervention* (see #der-causal-hierarchy-requirement; the gap between CIY and proper expected information gain is logged in this segment's Epistemic Status as a known surrogate). Second, AAT does not encode preferences as priors over outcomes ($C(o) = \log P_{\mathrm{pref}}(o)$ in the AI form): AAT's $O_t$ is a value functional on trajectories ( #form-objective-functional), and the satisfaction-gap / control-regret diagnostic in #def-satisfaction-gap, #def-control-regret depends on this distinction — the diagnostic structure does not survive the priors-as-preferences collapse (the dark-room critique, Sun & Firestone 2020, "The dark room problem," *Trends Cog. Sci.* 24).

**Regret-bound connection to the strategy-cost objective.** AAT's $Q_O$ term connects to the strategy-cost objective in #form-strategy-complexity-cost via a regret-bound derivation: strategy-induced regret $R(Q_{\Sigma_t}) = V(a^\ast) - \mathbb E_{Q_{\Sigma_t}}[V(a)]$ is bounded by a divergence between $\pi^\ast$ and $Q_{\Sigma_t}$, with the KL direction $\pi^\ast$-first forced (full derivation in #deriv-strategy-cost-regret-bound). Under AAT's canonical scope of deterministic $\pi^\ast$, the Bretagnolle-Huber identity $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log(1 - \operatorname{TV}(\pi^\ast, Q_{\Sigma_t}))$ holds *exactly* (Bretagnolle & Huber 1978), giving the tight regret bound $R(Q_{\Sigma_t}) \leq V_{\max}\bigl(1 - e^{-D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}\bigr)$ with matching lower bound $\Delta_{\min}\bigl(1 - e^{-D_{\mathrm{KL}}}\bigr)$ on isolated optima ( #deriv-strategy-cost-regret-bound §4). Pinsker's $V_{\max}\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$ remains the correct loose general form for stochastic-$\pi^\ast$ extensions where the BH identity degrades back to inequality. The structural point: "value and information term" shares *shape* with EFE's pragmatic-epistemic decomposition, and the KL direction in the strategy-cost's variational form shares direction with variational inference — but AAT's derivation is via decision-theoretic regret bound on $Q_O$ rather than via free-energy-gradient flow, which is the AAT-internal route that does not depend on the priors-as-preferences encoding.


---

### Source: `form-strategy-complexity-cost.md`

```yaml
---
slug: form-strategy-complexity-cost
type: formulation
status: robust-qualitative
depends:
  - def-strategic-tempo
  - form-information-bottleneck
  - norm-explicit-strategy-condition
  - der-chain-confidence-decay
  - deriv-strategy-cost-regret-bound
  - form-structural-change-as-parametric-limit
  - def-value-object
  - form-objective-functional
stage: draft
---
```


# Formulation: Cognitive Cost of Strategy

The complexity cost of maintaining an explicit strategy $\Sigma_t$, formulated via minimum description length and the information bottleneck principle --- connecting DAG structure to the maintenance term $C_{\text{maintain}}$ in the explicit strategy condition ( #norm-explicit-strategy-condition).

## Formal Expression

### Strategy description length

*[Formulation (strategy-description-length)]*

The minimum description length of a strategy DAG $\Sigma_t = (V, E, p, \gamma)$ ( #def-strategy-dag) decomposes as:

$$\operatorname{DL}(\Sigma_t) = \operatorname{DL}_{\text{struct}}(G) + \operatorname{DL}_{\text{param}}(p \mid G)$$

where:
- $\operatorname{DL}_{\text{struct}}(G)$: bits to encode the DAG topology --- node identities, edge connectivity, AND/OR labels $\gamma$. Scales as $O(\lvert E\rvert \log \lvert V\rvert)$ for sparse DAGs.
- $\operatorname{DL}_{\text{param}}(p \mid G)$: bits to encode the edge credences given the topology. For Beta-distributed credences, each edge requires $O(\log n_{ij})$ bits where $n_{ij} = \alpha_{ij} + \beta_{ij}$ is the effective sample size.

The total scales as $O(\lvert E\rvert \log \lvert V\rvert)$ for moderate-precision credences, growing linearly in the number of edges and logarithmically in the number of nodes.

### Strategy IB objective

*[Formulation (strategy-IB-objective; KL-direction strengthened by regret bound — see Epistemic Status)]*

The optimal strategy complexity balances parsimony against decision-relevance. $\Sigma_t$ is the IB-compression of the interaction history $\mathcal C_t$ *for guidance*, parallel to $M_t$ as the IB-compression of $\mathcal C_t$ *for prediction* ( #disc-compression-operations for the shared IB shape across AAT's compression operations, and for the relationship between the theoretical $I(\mathcal C_t; \Sigma_t)$ compression cost and the operational DL-based minimization below):

**Theoretical form (variational).** $\Sigma_t$ is a tractable variational approximation of the optimal-policy posterior $Q^\ast(\pi \mid M_t)$. The strategy-cost objective:

$$\Sigma_t^\ast = \arg\min_{\Sigma_t} \left[\, I(\mathcal C_t;\, \Sigma_t) \;+\; \beta_\Sigma \cdot D_{\mathrm{KL}}\bigl(\pi^\ast(\cdot \mid M_t) \,\big\Vert\, Q_{\Sigma_t}(\pi \mid M_t)\bigr)\right]$$

where $Q_{\Sigma_t}(\pi \mid M_t)$ is the action distribution induced by the strategy DAG given the current model state, and $\pi^\ast(\cdot \mid M_t)$ is the optimal-policy reference. The KL direction — $\pi^\ast$-first — is forced by the regret-bound derivation (next paragraph); the opposite direction is vacuous under deterministic $\pi^\ast$.

**Regret-bound derivation of KL direction.** Under AAT's canonical scope, $\pi^\ast = \delta_{a^\ast}$ is deterministic ( #def-value-object). Define the strategy-induced regret against $\pi^\ast$ as $R(Q_{\Sigma_t}) := V(a^\ast) - \mathbb{E}_{a \sim Q_{\Sigma_t}}[V(a)]$, where $V(a) = Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ is the action-value ( #def-value-object, $O_t$ induces $V$ via #form-objective-functional). Under bounded value range $V_{\max} := \max_a V(a) - \min_a V(a)$:

$$R(Q_{\Sigma_t}) \;\leq\; V_{\max}\cdot(1 - Q_{\Sigma_t}(a^\ast)) \;=\; V_{\max}\cdot\operatorname{TV}(\pi^\ast, Q_{\Sigma_t})$$

Applying Pinsker's inequality ($\operatorname{TV}(P,Q) \leq \sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(P\Vert Q)}$) with $P = \pi^\ast$, $Q = Q_{\Sigma_t}$:

$$R(Q_{\Sigma_t}) \;\leq\; V_{\max}\cdot\sqrt{\tfrac{1}{2}\, D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$$

Under deterministic $\pi^\ast$, $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log Q_{\Sigma_t}(a^\ast)$ — finite and graded whenever $Q_{\Sigma_t}(a^\ast) \gt 0$. The opposite-direction $D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast)$ equals $+\infty$ whenever $Q_{\Sigma_t}$ places any mass off $a^\ast$, giving a vacuous bound. The regret-bound argument therefore **forces the KL direction** with $\pi^\ast$ first. Within the direction-forced f-divergence family, reverse-KL is *uniquely* selected under the chain-rule additivity axiom (Hobson 1969; Csiszár 1991 Theorem 3 corollary and Theorem 5; standard functional-equation derivation per Aczél & Daróczy 1975), which is AAT-internally motivated as the divergence-level analog of additive log-confidence decay ( #der-chain-confidence-decay). See #deriv-strategy-cost-regret-bound §6.1 for the uniqueness theorem, §6.2 for secondary supporting characterizations (gradient-tractability, VI-alignment, MDL), and §7 for the linear-vs-square-root $\beta_\Sigma$ trade-off.

The variational form is the strategy-layer analog of variational free energy minimization in active inference (Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29; Da Costa, Parr, Sajid, Veselic, Neacsu & Friston 2020, "Active inference on discrete state-spaces," *J. Math. Psych.* 99; Parr & Pezzulo 2022, *Active Inference*, MIT Press). AAT borrows the variational form as the appropriate generalization of the Shannon-MI relevance term and now derives the direction of KL from an internal regret-bound argument — without committing to AI's preferences-as-priors encoding ($C(o) = \log P_{\mathrm{pref}}(o)$; AAT's $O_t$ remains a value functional on trajectories, #form-objective-functional) or to expected free energy as master objective (AAT's CIY-unified objective is a related but distinct decomposition; #disc-ciy-unified-objective).

**Operational form.** Since $I(\mathcal C_t; \Sigma_t)$ is not computable in closed form for general DAG encodings, the operational minimization replaces the information cost with a description-length surrogate and the KL term with a sample-based estimate (a per-edge calibration discrepancy weighted by decision-relevance — see #disc-credit-assignment-boundary for the gradient form):

$$\Sigma_t^\ast \approx \arg\min_{\Sigma_t} \left[\operatorname{DL}(\Sigma_t) + \beta_\Sigma \cdot \widehat{D_{\mathrm{KL}}}(\pi^\ast \,\Vert\, Q_{\Sigma_t})\right]$$

where:
- $\operatorname{DL}(\Sigma_t)$: description length (coding-cost upper bound on $I(\mathcal C_t; \Sigma_t)$ for the given DAG encoding scheme — see §2.2 below)
- $\widehat{D_{\mathrm{KL}}}(\pi^\ast \,\Vert\, Q_{\Sigma_t})$: sample-based estimate of the KL divergence from the optimal-policy reference to the strategy-induced policy
- $\beta_\Sigma \gt 0$: trade-off parameter — cognitive cost per decision-relevant bit (the $\Sigma_t$ instance of the shared $\beta$ framework in #disc-compression-operations); under the regret-bound derivation, $\beta_\Sigma$ has a *local* interpretation as $V_{\max}/(2\sqrt{2 D_{\mathrm{KL}}})$ via the Pinsker form (the linear-KL form is the IB-shape instance; the square-root form is the tighter regret-scale form — see Epistemic Status and the spike for the trade-off)

The two forms agree in the limit where the DAG encoding is rate-distortion optimal and the policy posterior is sample-recoverable; the operational form is the one an agent actually runs. The theoretical form places the objective on the same variational frontier as $M_t$, shared intent, and composition projection, with the $\pi^\ast$-first KL-form relevance term resolving the Shannon-zero degeneracy under deterministic $\pi^\ast$ *and* the forward-KL infinity degeneracy that the opposite direction would introduce.

When $\beta_\Sigma$ is low (high maintenance cost relative to decision value), the agent prefers simple strategies. When $\beta_\Sigma$ is high (strategy is cheap to maintain relative to its decision value), the agent can afford complex plans. The explicit strategy condition ( #norm-explicit-strategy-condition) is the binary threshold: $\beta_\Sigma$ large enough that *any* $\Sigma_t$ is worth maintaining.

### Maximum useful chain depth

*[Derived (Conditional on Beta-Bernoulli, per-edge persistence)]*

From #def-strategic-tempo's per-edge persistence condition, an AND-chain of depth $d$ with per-edge observation rate $\nu$, true success probability $\theta$ per edge, and effective sample size $n$ per edge persists only if the deepest edge satisfies:

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

1. **Confidence decay** ( #der-chain-confidence-decay): aggregate confidence $\prod p_k$ decays geometrically with depth. The plan is *less likely to succeed*.
2. **Evidence starvation** ( #deriv-edge-credence-dynamics): effective observation rate $\nu_k = \nu \cdot \prod_{j \lt k}\theta_j$ decays geometrically. The plan is *harder to calibrate*.
3. **Cognitive cost** (this segment): each additional depth level adds $O(\log \lvert V\rvert)$ bits to description length. The plan is *more expensive to maintain*.

All three are multiplicative in depth, making deep sequential strategies exponentially costly along three independent dimensions.

### Enriched explicit strategy condition

*[Formulation (enriched-strategy-condition)]*

The maintenance cost $C_{\text{maintain}}$ from #norm-explicit-strategy-condition decomposes as:

$$C_{\text{maintain}} = C_{\text{represent}} + C_{\text{revise}} + C_{\text{monitor}}$$

where:
- $C_{\text{represent}} \propto \operatorname{DL}(\Sigma_t)$: cognitive cost of holding the strategy in working memory (proportional to description length)
- $C_{\text{revise}} \propto \sum_{(i,j)} \nu_{ij} \cdot c_{\text{update}}$: cost of processing edge updates (proportional to strategic tempo $\mathcal T_\Sigma$ times per-update cost)
- $C_{\text{monitor}} \propto \lvert\{(i,j) : \iota_{ij} \lt 1\}\rvert$: cost of monitoring edges with partial identifiability (the agent must do extra causal reasoning for non-trivial edges)

This decomposition makes the #norm-explicit-strategy-condition's maintenance term concrete: each component maps to a quantity defined elsewhere in the theory.

### Complexity compression operations

*[Discussion (complexity-compression)]*

The IB objective suggests three compression operations, corresponding to structural changes from #form-structural-change-as-parametric-limit:

1. **Edge pruning** (operation 3 in #form-structural-change-as-parametric-limit): remove edges with $\eta_{\text{edge},ij} \cdot I_{\text{edge},ij} \lt c_{\text{bit}}$, where $I_{\text{edge},ij}$ is the decision-relevance of that edge and $c_{\text{bit}}$ is the per-bit maintenance cost. Edges that contribute less decision value than their representational cost are candidates for removal.
2. **Node merging** (reducing $\lvert V\rvert$): collapse intermediate nodes that serve no decision-distinguishing function. This reduces $\operatorname{DL}_{\text{struct}}$ by a factor proportional to the reduction in $\lvert V\rvert$.
3. **Depth truncation** at $d^\ast$: prune all edges beyond the maximum useful depth. This is not optimization but necessity --- edges beyond $d^\ast$ cannot maintain bounded mismatch.

## Epistemic Status

The description length formulation is a *formulation* --- it applies standard MDL to the strategy DAG, which is a representational choice not a derived necessity. The IB objective is *formulation (strengthened by regret bound)* in its variational form (above): the specific KL *direction* ($\pi^\ast$-first, i.e., reverse-KL in the variational-inference vocabulary) is *derived* as an upper regret bound via Pinsker's inequality under bounded value range and deterministic $\pi^\ast$ (see Regret-bound derivation paragraph above; full derivation in appendix #deriv-strategy-cost-regret-bound). The choice of reverse-KL *within* the direction-forced family upgrades from canonical-formulation to **derived (conditional on chain-rule additivity axiom)** — the chain-rule axiom (Hobson 1969; Csiszár 1991 Theorem 3 corollary and Theorem 5; standard functional-equation derivation per Aczél & Daróczy 1975) picks reverse-KL uniquely among f-divergences, and the axiom is AAT-internally motivated as the divergence-level analog of #der-chain-confidence-decay (see #deriv-strategy-cost-regret-bound §6.1). Secondary properties (gradient-tractability, variational-inference alignment with Friston et al. 2017, Da Costa et al. 2020, Parr & Pezzulo 2022; MDL coding; compatibility with Amari & Nagaoka 2000 Fisher geometry) are convergent evidence rather than independent uniqueness grounds — in particular, Fisher-metric-at-second-order is *not* distinguishing within f-divergences (Eguchi 1983, *Ann. Statist.* 11(3):793–803). The regret-bound derivation closes the direction ambiguity that the earlier V-medium move (commit `a14682e`) left open: the initial V-medium form used $D_{\mathrm{KL}}(Q_{\Sigma_t} \Vert \pi^\ast)$ (forward-KL), which is $+\infty$ under deterministic $\pi^\ast$ whenever $Q_{\Sigma_t}$ has any off-optimum mass — a different-valued but structurally identical degeneracy to the Shannon-MI zero it replaced. The $\pi^\ast$-first reverse-KL direction escapes both degeneracies by construction.

The variational form replaces an earlier Shannon-MI form $-\beta_\Sigma \cdot I(\Sigma_t;\, \pi^\ast \mid M_t)$ which had a Shannon-zero degeneracy: when $\pi^\ast$ is a deterministic function of $M_t$ (the standard scope), Shannon mutual information to a constant vanishes identically, collapsing the objective to $\arg\min \operatorname{DL}(\Sigma_t)$. The $\pi^\ast$-first KL form does not have this degeneracy and is graded whenever $Q_{\Sigma_t}$ places any mass on $a^\ast$. The maximum useful depth $d^\ast$ is *derived* conditional on Beta-Bernoulli dynamics and the per-edge persistence condition from #def-strategic-tempo. The triple depth penalty is an *observation* combining results from three independent segments. The enriched maintenance decomposition is *formulation*. The compression operations are *discussion-grade*.

**On $\beta_\Sigma$ interpretation.** Under the Pinsker-reverse-KL bound $R(Q_{\Sigma_t}) \leq V_{\max}\sqrt{\tfrac{1}{2} D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$, a square-root-in-KL trade-off would naturalize $\beta_\Sigma$ globally as $\beta_\Sigma \propto V_{\max}$. The segment retains the linear-in-KL form (to preserve the rate-distortion-Lagrangian IB shape shared with #disc-compression-operations); under the linear form, $\beta_\Sigma$ has only a *local* regret-bound interpretation ($\partial R / \partial D_{\mathrm{KL}}$ at the operating point). This is a trade-off between IB-shape alignment and regret-scale naturalization. Under AAT's canonical deterministic-$\pi^\ast$ scope, the sharper Bretagnolle-Huber identity $R \leq V_{\max}(1 - e^{-D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})})$ holds as the primary form ( #deriv-strategy-cost-regret-bound §4); Pinsker is retained here for IB-shape alignment and as the loose general form correct for stochastic-$\pi^\ast$ extensions.

**Assumption explicitly stated: bounded value range.** The regret-bound derivation requires $V_{\max}:=\max_a V(a) - \min_a V(a) \lt \infty$ over $\mathcal{A}$ at fixed $M_t$. This is mild but not automatic — #form-objective-functional specifies $V_{O_t}: \text{trajectories} \to \mathbb{R}$, and bounded range at fixed state is an additional assumption stated here.

Max attainable: *robust-qualitative* for the IB objective with the direction-forced derivation; conditional for the specific functional form (linear vs. square-root in KL). The DL formulation is standard; the depth bound could reach exact status for specific edge models. The regret-bound derivation does not extend to stochastic $\pi^\ast$ (outside AAT canonical scope); see #def-value-object continuation conventions for scope.

## Discussion

**Connection to #norm-explicit-strategy-condition.** The enriched maintenance decomposition gives the cost inequality quantitative content: an agent can now *compute* whether a proposed strategy is worth maintaining by estimating its description length, revision cost, and monitoring burden, and comparing against the exploration/repair cost of operating without it.

**LLM context windows as DL constraint.** For language-constituted agents ( `03-llm-core/`), the strategy must fit in the context window. A context window of $W$ tokens imposes $\operatorname{DL}(\Sigma_t) \leq W \cdot \log_2(\lvert\text{vocab}\rvert)$ as a hard constraint. This makes the IB trade-off non-optional: the agent *must* compress its strategy, and the depth bound $d^\ast$ becomes a context-window-limited quantity. A 128K-token context window may support a 500-edge DAG encoded in natural language; a 4K-token window may support only a 15-edge sketch.

**Computational compression from interaction horizon (Miller 2022).** The maximum useful depth $d^\ast$ derived above constrains complexity from the *maintenance* side (evidence starvation). Miller (2022, *Ex Machina*, Table 12.2) provides a complementary constraint from the *interaction* side: the number of interaction rounds compresses the space of behaviorally distinguishable strategies regardless of the agent's internal complexity. For Moore machines with binary actions:

| Agent states | Unique computations | After 1 round | After 2 rounds | After 4 rounds |
|---|---|---|---|---|
| 1 | 2 | 2 | 2 | 2 |
| 2 | 26 | 2 | 8 | 26 |
| 3 | 1,054 | 2 | 8 | 690 |
| 4 | 57,068 | 2 | 8 | 5,936 |

The pattern: $\text{effective complexity} = \min(\text{agent complexity}, \text{interaction-horizon complexity})$. With only one round, even a four-state machine (57,068 unique computations) reduces to two distinguishable behaviors — equivalent to a one-state machine. With two rounds, all machines with two or more states reduce to eight distinguishable behaviors. The interaction horizon compresses the strategy space from above, just as the maintenance cost and evidence starvation compress it from below. For AAT's strategy DAG, the analog: a complex $\Sigma_t$ whose edges are only tested over a short horizon gains nothing from its depth — the untested structure is indistinguishable from a simpler strategy. This reinforces the $d^\ast$ bound and provides empirical grounding beyond the Beta-Bernoulli derivation.

**Strategy simplification pressure.** The triple depth penalty creates systematic pressure toward shallow, wide (OR-heavy) strategies over deep, sequential (AND-heavy) ones. This aligns with the structural pressure identified in #der-chain-confidence-decay's Discussion, now grounded in three independent mechanisms rather than one.

## Working Notes

- **Mixed topologies.** The depth bound $d^\ast$ assumes uniform AND-chains. Mixed AND/OR DAGs have heterogeneous depth penalties: OR-nodes reset the evidence-starvation clock (each alternative is tested independently), while AND-nodes compound it. The effective depth for computing $d^\ast$ may be the longest AND-chain in the DAG, not the total graph depth.
- **Optimal topology.** Given a fixed DL budget and action rate $\nu$, what DAG topology maximizes decision-relevant information $I(\Sigma_t;\, \pi^\ast \mid M_t)$? This is a combinatorial optimization over graph structures --- likely NP-hard in general but potentially tractable for specific graph families (trees, bounded treewidth).
- **Dynamic complexity.** As edges converge (high $n_{ij}$), their per-edge $\eta_{\text{edge},ij}$ shrinks, but their description length $\operatorname{DL}_{\text{param}}$ grows (more bits to encode the precise credence). The IB objective would favor *dropping* converged edges (they contribute little decision-relevant information since the agent already acts correctly on them), replacing them with a default "high confidence" summary. This is a principled version of "stop tracking what you already know."
- **Stochastic $\mathcal T_\Sigma$.** If strategic disturbance follows Model S (stochastic) rather than Model D (deterministic), the steady-state mismatch scales as $\rho_\Sigma / \sqrt{\mathcal T_\Sigma}$ rather than $\rho_\Sigma / \mathcal T_\Sigma$. The depth bound $d^\ast$ would change accordingly. Not yet derived.


---

### Source: `def-shared-intent.md`

```yaml
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
```


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


---

### Source: `disc-compression-operations.md`

```yaml
---
slug: disc-compression-operations
type: discussion
status: robust-qualitative
depends:
  - form-information-bottleneck
  - form-strategy-complexity-cost
  - def-shared-intent
  - form-composition-closure
  - def-chronica
stage: draft
---
```


# Discussion: Compression Operations in AAT

AAT contains four compression operations — the epistemic model $M_t$, the strategy DAG $\Sigma_t$, shared intent $G_t^{\text{shared}}$, and the composition projection $\Lambda$ — each formulated in its own segment with its own objective. Three of the four are written in Information Bottleneck (IB) form already; the fourth is stated as an IB constraint. This segment makes the shared shape explicit, promotes one underspecified source (the ontologically ambiguous "true causal structure" for $\Sigma_t$) to a cleaner formulation parallel to $M_t$, and establishes that composition admissibility (P1) is the Lagrangian-dual of a standard IB objective. It does *not* claim the four operations reduce to a single optimization problem — cross-instance theorems do not follow from the shared shape alone, and several conditions (Lipschitz regularity (P2), dimensional reduction (P3) in the Gaussian case, interventional relevance for Level-2 edges) remain outside the IB frame.

## Formal Expression

### The shared IB shape

*[Discussion (ib-shape)]*

Every compression operation in AAT has an objective or constraint of the form:

$$T^\ast = \arg\min_{T \mid X}\; \bigl[\, I(X; T) \;-\; \beta \cdot I(T; Y) \,\bigr]$$

with the Markov chain $Y - X - T$. The four AAT instances specialize this with different bindings:

| Instance | $X$ (source) | $T$ (compressed) | $Y$ (relevance variable) | $\beta$ (trade-off) |
|---|---|---|---|---|
| Model compression ( #form-information-bottleneck) | $\mathcal C_t$ | $M_t$ | $o_{t+1:\infty} \mid a_{t:\infty}$ | $\beta(\rho, \pi)$ — volatility and policy |
| Strategy compression ( #form-strategy-complexity-cost) | $\mathcal C_t$ | $\Sigma_t$ | $\pi^\ast \mid M_t$ | $\beta_\Sigma$ — cognitive cost per decision-bit |
| Shared intent ( #def-shared-intent) | $G_t^{\text{full}} = (O_t, \Sigma_t)$ | $G_t^{\text{shared}}$ | $a_t^{\text{coordinated}}$ | bandwidth per coordination-bit |
| Composition projection ( #form-composition-closure P1) | $X_{\text{micro},t}$ | $\Lambda_x(X_{\text{micro},t})$ | $o_{\text{micro},t+1} \mid a_{\text{micro},t}$ | $\beta(\epsilon_I)$ — rate-distortion Lagrange multiplier |

What the four instances share: *shape* (the objective structure), *variational calculus* (minimization over stochastic compressors), and *rate-distortion interpretation* (each trade-off parameter indexes a point on the frontier). What they do not share: source type (history vs. structured state), relevance-variable availability (observed vs. latent), computability (Gaussian closed forms vs. variational approximation), or a single joint optimization across the four. The level of unification is *medium*: shared shape and vocabulary, not a shared master problem.

### Strategy compression: source reformulation

*[Formulation (strategy-compression-source)]*

The current statement in #form-strategy-complexity-cost has the $\Sigma_t$ IB objective as:

$$\Sigma_t^\ast = \arg\min_{\Sigma_t}\; \bigl[\, \operatorname{DL}(\Sigma_t) \;-\; \beta_\Sigma \cdot I(\Sigma_t;\; \pi^\ast \mid M_t) \,\bigr]$$

Two issues with this as currently written:

1. **The compression cost is description length, not mutual information.** DL and $I(X; T)$ are related through coding-theoretic equivalences but coincide only under specific coding schemes. Using DL in the complexity term blocks the identification of this objective as an IB instance directly.
2. **The "source" is not an AAT object.** To fit the IB shape, the objective implicitly treats $\Sigma_t$ as a compression of "the true causal structure." That structure is not part of AAT's ontology — the agent never has access to it; it is only ever implicit.

**Reformulation.** Treat $\Sigma_t$ as a compression of $\mathcal C_t$ (the interaction history — the agent's only evidence) *for decision-relevance*, parallel to $M_t$ which is a compression of $\mathcal C_t$ *for prediction-relevance*:

$$\Sigma_t^\ast = \arg\min_{\Sigma_t}\; \bigl[\, I(\mathcal C_t; \Sigma_t) \;-\; \beta_\Sigma \cdot I(\Sigma_t;\; \pi^\ast \mid M_t) \,\bigr]$$

Under this reformulation:

- The source $\mathcal C_t$ is a well-defined AAT object, shared with the $M_t$ instance.
- The two instances differ cleanly in relevance variable: $M_t$ is compressed for prediction ($Y = o_{t+1:\infty} \mid a$); $\Sigma_t$ is compressed for guidance ($Y = \pi^\ast \mid M_t$). Prediction is about *what will happen*; guidance is about *what to do*. Both are computed from the same history, with different targets.
- The information cost $I(\mathcal C_t; \Sigma_t)$ replaces $\operatorname{DL}(\Sigma_t)$ as the theory-level compression term. The DL formulation remains useful as an *operational* cost measure for specific DAG encodings; it is not the theoretical quantity the IB objective minimizes.

**Relationship between the two cost measures.** Under MDL with a specific encoding scheme for DAGs (the one in #form-strategy-complexity-cost), $\operatorname{DL}(\Sigma_t)$ is an upper bound on $I(\mathcal C_t; \Sigma_t)$ for DAGs produced by the given encoder — coding cost dominates distinguishability cost. In practice, DL is computable and $I$ is not, so the operational minimization uses DL as a proxy; the theoretical minimization uses $I$. The IB objective above is the theoretical statement; the DL-based minimization in #form-strategy-complexity-cost remains the practical one.

**Variational form.** The Shannon mutual information $I(\Sigma_t; \pi^\ast \mid M_t)$ in the relevance term collapses to zero when $\pi^\ast$ is deterministic-from-$M_t$. The variational form (cf. #form-strategy-complexity-cost) replaces the relevance term with the KL-divergence $D_{\mathrm{KL}}(\pi^\ast(\cdot \mid M_t) \,\Vert\, Q_{\Sigma_t}(\pi \mid M_t))$ — note the $\pi^\ast$-first direction, which is *forced* by a regret-bound derivation (full derivation and admissible-divergence family analysis in #deriv-strategy-cost-regret-bound). Under bounded value range and deterministic $\pi^\ast$, Pinsker's inequality gives $R(Q_{\Sigma_t}) \leq V_{\max}\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(\pi^\ast\Vert Q_{\Sigma_t})}$ where $R$ is the strategy-induced regret against $\pi^\ast$; the opposite KL direction is vacuous ($+\infty$ under deterministic $\pi^\ast$ whenever $Q_{\Sigma_t}$ has off-optimum mass). The $\pi^\ast$-first KL is well-defined and graded under deterministic $\pi^\ast$. Under the variational reading, the AAT $\Sigma_t$ is a tractable approximation of the policy-relevant posterior, and the KL term measures approximation quality — aligning the strategy compression with the variational free energy decomposition $-F = \text{accuracy} - \text{complexity}$ in active inference (Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017; Da Costa, Parr, Sajid, Veselic, Neacsu & Friston 2020). The direction alignment is convergent: both AAT's regret-bound and active inference's variational-free-energy derivations pick $\pi^\ast$-first KL (reverse-KL in the variational-inference vocabulary), with AAT's additional interpretation being an upper-regret-bound rather than free-energy-gradient. The shared-IB-shape framing of the four AAT compression operations is the rate-distortion specialization of this variational picture; AAT's commitment is to the rate-distortion form (which gives the (P1) Lagrangian-dual derivation and the four-instance unification at U-medium), not to the full variational free-energy interpretation.

### Composition admissibility (P1) as IB Lagrangian-dual

*[Derived (p1-ib-dual, from composition-closure + rate-distortion duality)]*

#form-composition-closure condition (P1) is currently stated as a lower-bound constraint:

$$I\bigl(\Lambda_x(X_{\text{micro},t});\; \Lambda_o(o_{\text{micro},t+1}) \mid \Lambda_a(a_{\text{micro},t})\bigr) \;\geq\; (1 - \epsilon_I) \cdot I\bigl(X_{\text{micro},t};\; o_{\text{micro},t+1} \mid a_{\text{micro},t}\bigr)$$

This is the *constraint form* of an IB problem. In Lagrangian form:

$$\Lambda^\ast \;\in\; \arg\min_{\Lambda \in \mathcal P}\; \bigl[\, I(X_{\text{micro}}; \Lambda_x(X_{\text{micro}})) \;-\; \beta(\epsilon_I) \cdot I(\Lambda_x(X_{\text{micro}});\, Y_{\text{rel}}) \,\bigr]$$

where $Y_{\text{rel}} = (o_{\text{micro},t+1} \mid a_{\text{micro},t})$ and $\beta(\epsilon_I)$ is the Lagrange multiplier corresponding to the relevance-preservation tolerance $\epsilon_I$. The correspondence $\epsilon_I \leftrightarrow \beta$ is the standard rate-distortion duality: smaller $\epsilon_I$ (more relevance preserved) corresponds to larger $\beta$ (less aggressive compression).

Consequence: admissible projections are those that sit *on or above* the IB frontier at rate $I(X; T) \leq I_{\max}(\epsilon_I)$. The information-theoretic content of (P1) is exactly "project onto the IB frontier with a tolerance $\epsilon_I$." This formalizes the connection previously logged in #form-composition-closure's Working Notes and in #result-unity-closure-mapping's §Connection to the Information Bottleneck.

**What this resolves.** The #form-composition-closure Working Note "Open: Information Bottleneck unification" is now resolved for (P1): it is the Lagrangian-dual of the IB constraint at $\beta(\epsilon_I)$. The corresponding Working Note in #result-unity-closure-mapping §6 moves from conjecture to derived result. Nothing else about (P1) changes — the condition continues to define admissible projections; only its information-theoretic reading is now explicit.

### What stays separate from the IB frame

Three admissibility and structural conditions do *not* reduce to IB:

- **(P2) Lipschitz continuity.** Not an IB constraint. The bridge lemma in #form-composition-closure requires (P2) for analytic reasons (propagating bounded closure defect into bounded trajectory error); IB does not impose any continuity condition on compressors. (P2) remains a separate admissibility condition.
- **(P3) Dimensional reduction.** In the Gaussian-IB case relevant to composition, the IB-optimal $T$ at any finite $\beta$ typically uses full support of $\mathbb R^{\dim X}$; the categorical dimensionality reduction $\dim \mathcal X_c \lt \dim \mathcal X_{\text{micro}}$ is a *harder* condition than any rate constraint. (P3) remains separate. (In discrete cases it may be rate-implied, but the composition instance is Gaussian.)
- **Interventional relevance (Level 2).** The relevance variable in all four instances is associational ($Y$ in a joint distribution with $X$ and $T$). Strategy edges in the regime-indexed interpretation ( #scope-edge-update-causal-validity) want interventional relevance for Regime A: "what edge $(i, j)$ predicts *under $do(i)$*." This is a strictly stronger requirement than IB provides. Adapting IB to interventional relevance (causal IB, Wieczorek & Roth 2017 and follow-ups) is an extension direction, not a specialization of the master IB.

The honest slogan is therefore "the (P1)-analog in each compression operation is IB; regularity, dimensionality, and interventional relevance are separate conditions that compose with it."

## Epistemic Status

*Robust-qualitative.* The claim that the four compression operations share IB shape is *discussion-grade* — it is a presentational observation supported by examining each segment's formulation and noting structural alignment. The $\Sigma_t$ source reformulation is a *formulation choice* replacing one underspecified source with a cleaner one; no derivation is needed because the new formulation and the old are not the same claim. The (P1) as Lagrangian-dual of IB is *derived* — rate-distortion duality is standard (see §I.12–13 of Cover & Thomas) and the constraint-form ↔ Lagrangian-form equivalence is mechanical.

Max attainable: *robust-qualitative* for the shared-shape claim; *derived conditional on rate-distortion duality* for (P1) as IB Lagrangian-dual; *formulation* for the $\Sigma_t$ source reformulation. The strongest version of the unification claim — "U-strong," that the four operations are the same optimization problem with different bindings — is *not* established and is unlikely to be, for reasons in the Discussion.

This segment does not promote any of the four instance segments. Each remains the primary site for its own instance. What this segment adds is the shared-shape framing, the $\Sigma_t$ source fix, and the (P1) derivation.

## Discussion

**Why not go further.** Two distinct claims could be made: (a) U-strong — the four operations are the *same* optimization problem with different bindings, so a single derivation specializes to each instance; (b) U-medium — the four share *shape*, vocabulary, and variational structure but differ in substantive ways (source type, relevance-variable availability, computability) that prevent a single derivation from covering all four. U-strong requires cross-instance theorems, results of the form "because these are all IB, property X holds across all four." No such theorems are identified. The shared IB shape is legibility-enhancing but does not produce deductions for free. This segment therefore states U-medium (shared shape) honestly rather than overclaiming U-strong.

**Honest credit to the hierarchical-generative-model lineage.** AAT's four compression operations are a structurally narrower family than the operations a hierarchical generative model in the predictive-coding lineage (Friston 2008, "Hierarchical models in the brain," *PLoS Comp. Biol.* 4; Friston 2010, "The free-energy principle: a unified brain theory?" *Nat. Rev. Neurosci.* 11; Clark 2013, "Whatever next?", *Behav. Brain Sci.* 36; Hohwy 2013, *The Predictive Mind*, OUP) could express. A hierarchical generative model layers compressions of compressions, with each layer producing a representation tuned to the next layer's prediction target — and the AAT compressions ($M_t$ for prediction, $\Sigma_t$ for guidance, shared intent for coordination, $\Lambda$ for level-bridging) are all expressible within that frame as specific layer-bindings. What AAT adds is structural: (a) the *relevance variables* $Y$ are made first-class with explicit per-instance bindings (see the table in §"The shared IB shape"); (b) the (P1)–(P3) admissibility conditions for composition give a measurable closure-defect bound that hierarchical-generative-model layering does not natively produce ( #form-composition-closure); (c) regime-indexed edges ( #scope-edge-update-causal-validity) introduce Pearl-Level-2 relevance for Regime A, which standard hierarchical generative models do not address. The shared family is real; AAT's additions are also real. The honest framing is "AAT's compressions are a structured subset of the hierarchical-generative-model family with additional structure load-bearing for AAT's specific results."

**Why this is not the "biggest available unification."** It is better described as the *most legible* unification. The pattern is already half-named at each instance site (three of four segments already write their objectives in IB form); the segment-level contribution is sharpening the naming and fixing one formulation issue ($\Sigma_t$ source), not discovering a new structural result. The biggest leverage concision move in the theory — the sector-Lyapunov template in #result-sector-persistence-template — is substantively different: it removes repeated content and absorbs proofs that previously appeared in multiple segments. This segment adds legibility without removing much.

**What each $\beta$ means.** The four trade-off parameters are not unified in value, only in role:

- $\beta(\rho, \pi)$ for $M_t$ depends on environmental volatility and policy; fast-changing environments or high-value policies both warrant higher $\beta$.
- $\beta_\Sigma$ for $\Sigma_t$ is the cognitive cost per decision-relevant bit retained; bounded-context agents (LLMs with finite windows) have low $\beta_\Sigma$.
- The bandwidth $\beta$ for shared intent is the communication-capacity-per-coordination-bit; low-bandwidth teams have low $\beta$.
- The $\beta(\epsilon_I)$ for (P1) is the rate-distortion Lagrange multiplier at tolerance $\epsilon_I$.

These are four calibration problems, not one. A theory of *resource allocation across the four compression operations* — where a single cognitive budget is split across modeling, strategy, communication, and composition — is not currently in AAT, and the unification does not produce it. If such a theory is ever needed, it would tie the four $\beta$s together through an outer optimization; the spike flags this as an open direction.

**Relationship to #def-unity-dimensions and #result-unity-closure-mapping.** The unity dimensions parametrize rate-distortion curves for closure defects ( #result-unity-closure-mapping). Under the present segment's framing, unity dimensions are *curve parameters for the $\Lambda$ instance of the IB schema*. This tightens the existing #result-unity-closure-mapping Discussion, which already presented the rate-distortion reading as the correct interpretation; it is now stated uniformly across the four compression operations.

**Relationship to #deriv-graph-structure-uniqueness.** The DAG-uniqueness result derives the *shape* of $\Sigma_t$ from operational postulates ( #deriv-graph-structure-uniqueness, Cox-analog). The present segment characterizes the *compression level* of $\Sigma_t$. These operate at different levels: uniqueness supplies the representational type (the compressed $T$ is a DAG), IB supplies the rate-distortion trade-off within that type (how richly the DAG is populated). The two arguments are independent and compatible — IB-compressed $\Sigma_t$ is a DAG-with-fewer-nodes, not a non-DAG.

**Position relative to the additive-coordinate-forcing pattern.** The IB Lagrangian's $I(X;T) - \beta \cdot I(T;Y)$ is an additive decomposition on a log-scale coordinate (mutual information is logarithmic by construction) — the same shape that #disc-additive-coordinate-forcing catalogs at the chain / divergence / update layers. The IB case is classified as an *adjacent family member* rather than a fourth primary instance because #form-information-bottleneck adopts the Lagrangian form from Tishby, Pereira & Bialek 1999 as an applied external theorem rather than re-deriving it under an AAT-internally-motivated additivity axiom. The Shore-Johnson 1980 system-independence axioms that axiomatize IB's additivity are cited in #deriv-strategy-cost-regret-bound §6.1; if a future framing pass promotes Shore-Johnson to an explicit AAT axiom, IB would move from adjacent member to fourth primary instance.

## Working Notes

- **The $\Sigma_t$ source reformulation changes the theoretical quantity without changing the operational computation.** #form-strategy-complexity-cost's DL-based minimization remains the practical procedure; what changes is the theoretical claim about what that procedure approximates. Depending on promotion-workflow preferences, the reformulation may warrant a small note in #form-strategy-complexity-cost referencing this segment.
- **(P1) as IB Lagrangian-dual does not close #form-composition-closure's other Working Notes.** Computability of (P1) for nonlinear/non-Gaussian systems, choice of $\epsilon_I$, and $N$-agent scaling remain open. The unification resolves the *framing* question but not the *computation* questions.
- **Synthesis segment vs. full unification.** This segment is a targeted synthesis: it fixes the $\Sigma_t$ source, derives (P1) as IB Lagrangian-dual, and tables the four instances. It does *not* rewrite the four instance segments as specializations of a master schema. If future work reveals that the four instance segments are pulling in inconsistent directions (e.g., if the $\Sigma_t$ reformulation creates friction with the DL-based minimization in #form-strategy-complexity-cost), that is the signal to escalate to a full rewrite in which the instance segments become thin specializations. Short of that signal, this targeted synthesis is the stopping point.
- **The Gaussian IB frontier derivation is deferred.** Completing the derivation that the means-sum projection attains the Gaussian IB frontier in the symmetric two-Kalman case would promote #result-unity-closure-mapping's rate-distortion claim from discussion-grade to derived. The obstruction is mechanical (specializing Chechik, Globerson, Tishby & Weiss 2005, "Information Bottleneck for Gaussian Variables," *J. Machine Learning Research* 6:165–188, Theorem 3.1 to the symmetric-gain setup) rather than structural — feasible as a follow-up derivation, not required for this segment.


---

