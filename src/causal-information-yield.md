---
slug: causal-information-yield
type: definition
status: discussion-grade
depends:
  - pearl-causal-hierarchy
  - action-selection
  - mismatch-signal
---

# Definition: Causal Information Yield

Actions don't merely select among outcomes — they generate information about how the environment responds to interventions. Causal information yield (CIY) quantifies this: how much an action reveals about causal structure that passive observation cannot provide.

## Formal Expression

*[Definition (causal-information-yield)]*

The **canonical CIY** of action $a$ given model state $M$:

$$\text{CIY}(a;\, M) = \mathbb{E}_{a' \sim q(\cdot \mid M)}\!\left[D_{\mathrm{KL}}\!\left(P(o \mid do(a), M) \,\Vert\, P(o \mid do(a'), M)\right)\right]$$

where $q(\cdot \mid M)$ is a reference distribution over comparator actions (uniform, policy-induced, or task-specific). This measures how strongly the action changes the interventional distribution of outcomes relative to alternatives.

$\text{CIY} \geq 0$ by construction (expectation of KL divergences). $\text{CIY} = 0$ for a passive observer or an agent whose actions don't affect outcome distributions. $\text{CIY} \gt 0$ when actions causally alter what is observed — exactly what distinguishes Level 2 from Level 1 epistemic access ( #pearl-causal-hierarchy).

**Observational proxy** (for diagnostic use with observational statistics):

*[Definition (ciy-proxy)]*

$$\text{CIY}_{\text{proxy}}(a_{t-1}) = I(o_t; a_{t-1} \mid M_{t-1}) - I(o_t; a_{t-1} \mid \Omega_t, M_{t-1})$$

This proxy is sign-indefinite in general and requires causal assumptions for interpretation. The canonical CIY (interventional) is the primary quantity; the proxy is auxiliary.

## Epistemic Status

The CIY *definition* is well-grounded in causal inference theory. The *structural claim* — that the optimal policy jointly maximizes value and causal information — is *discussion-grade*, supported by convergent results in Bayesian RL, active inference, and information-directed sampling, but not derived from first principles within ACT. The specific form of $\lambda(M_t)$ (the exploration-exploitation balance weight) is not derived. See discussion of the unified policy objective below.

## Discussion

**Dependence on the reference distribution $q$.** The quantitative CIY value depends on the choice of $q$, which is a significant degree of freedom. A uniform $q$ treats all alternatives equally; a policy-induced $q$ emphasizes alternatives the agent would consider. ACT adopts the policy-induced $q$ as default: $q(\cdot \mid M) = \pi(\cdot \mid M)$, yielding CIY as "how different is this action's outcome from what I'd typically see?" CIY values are not comparable across different $q$ choices.

**CIY admissibility regimes.** Three regimes determine when CIY can be estimated:

- **Regime A — Randomized interventions.** Actions are varied (RL agents exploring, scientists experimenting, organisms probing). CIY is directly estimable and non-negative. The standard case for active agents.
- **Regime B — Observational with causal assumptions.** Agent cannot freely vary actions. CIY estimation requires a known DAG, instrumental variables, or functional form assumptions. Results inherit the causal assumptions.
- **Regime C — Adversarial communication.** Observation channel includes responses from potentially adversarial sources. CIY from the query itself remains non-negative, but the *content* may be designed to increase model-reality mismatch. The adversary operates through the disturbance term $\rho$, not through the information measure.

**The unified policy objective.** The exploration-exploitation tension suggests:

*[Discussion (unified-policy-objective)]*

$$\pi^*(M_t) = \arg\max_a \left[\mathbb{E}[\text{value}(a) \mid M_t] + \lambda(M_t) \cdot \text{CIY}_q(a;\, M_t)\right]$$

The first term is exploitation (expected value given current model). The second is exploration (causal information yield). $\lambda(M_t)$ controls the balance:

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

**Query actions: accessing external models.** A qualitatively distinct class of actions: querying another agent's model. When a reliable source exists (expert, database, documentation, well-trained LLM), "ask a well-formed question" can yield information equivalent to thousands of probe-observe cycles. The source's model has already performed the compression work ( #information-bottleneck) — the response transfers the *output* of compression rather than requiring the agent to reconstruct it.

Key properties of query actions:
- **Information density**: Single well-targeted query can carry CIY orders of magnitude higher than individual environment probes
- **Trust-dependent gain**: Update from query depends on the agent's model of the source's reliability and alignment, not on observation channel noise ( #communication-gain)
- **Pre-compressed information**: Responses arrive already compressed in the source's representational framework, introducing a translation cost when frameworks don't align
- **Structural adaptation via external models**: Encountering another agent's model can trigger structural change ( #structural-adaptation-necessity) — incorporating external representational structure rather than building it de novo ("grafting")

When high-CIY query channels are available, the unified policy objective favors query actions over direct probes, particularly when $U_M$ is high, a trusted source exists, query cost is low, and the needed information is about *structure* rather than the agent's specific situation.

**The adversarial mirror: deception and model corruption.** The same channel that enables cooperative knowledge transfer can be exploited to degrade the opponent's model. A deceptive response yields positive CIY in the strict information-theoretic sense, but the content drives model-reality mismatch *upward*. The update gain $\eta^\ast$ for the victim depends on trust; successful deception exploits high trust to inject a large, misdirected update. In the Lyapunov framework ( #sector-condition-stability), this is adversarial disturbance injected through the observation channel, with coupling coefficient $\gamma_A$ determined by the victim's trust level and exposure. See #communication-gain for the formal treatment of trust-dependent gain, and #adversarial-destabilization for the Lyapunov formalization. Distributed tempo, topology analysis, and game-theoretic integration are Section III content not yet fully extracted (source material in `src/old-tf-appendix-f-multi-agent.md`).

**Connection to the zero-mismatch ambiguity.** An agent that only exploits (acts to maximize predicted value) will tend toward confirmation bias — observing only what its model already explains ( #mismatch-signal, zero-mismatch ambiguity case (b)). Exploration via CIY-maximizing actions is the mechanism by which the agent actively tests its model.

**Connection to Section II.** For actuated agents, the exploration-exploitation tension extends to three modes: exploit (pursue $O_t$ via $\Sigma_t$), explore (improve $M_t$), deliberate (revise $\Sigma_t$). The CIY framework provides the information-theoretic grounding for why strategy edges ( #strategy-dag) need observational access ( #observability-dominance) — edges the agent cannot observe have frozen CIY.

**Connection to active inference.** The Free Energy Principle's "expected free energy" decomposes into extrinsic value (pragmatic) and epistemic value (information-seeking). ACT's formulation is structurally isomorphic: expected value ≈ extrinsic, CIY ≈ epistemic. Whether this convergence is deep or superficial is an open question. ACT grounds exploration in explicitly *causal* information rather than entropy reduction — not all uncertainty reduction is equally valuable; causal information specifically enables better *intervention*.

**Identifiability gate.** Before incorporating CIY into policy objectives: (1) action variation must exist, (2) admissibility regime must be identified, (3) reference distribution $q$ must be specified, (4) local stationarity must hold. If any condition fails, CIY-based terms should be dropped or replaced with simpler uncertainty-based heuristics (UCB-style bonuses, ensemble disagreement).

**(Descended from TF-08.)**
