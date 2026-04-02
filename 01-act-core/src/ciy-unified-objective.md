---
slug: ciy-unified-objective
type: discussion
status: discussion-grade
depends:
  - causal-information-yield
  - ciy-observational-proxy
  - value-object
  - action-selection
---

# Discussion: CIY Unified Policy Objective

The exploration-exploitation tension can be formalized as a single policy objective that jointly maximizes expected value and causal information yield.

## Formal Expression

*[Discussion (unified-policy-objective)]*

$$\pi^\ast(M_t) = \arg\max_a \left[\mathbb{E}[\text{value}(a) \mid M_t] + \lambda(M_t) \cdot \text{CIY}_q(a;\, M_t)\right]$$

The first term is exploitation (expected value given current model). The second is exploration (causal information yield, #causal-information-yield). $\lambda(M_t)$ controls the balance:

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

**Identifiability gate.** Before incorporating CIY into the policy objective: (1) action variation must exist, (2) the admissibility regime must be identified ( #ciy-observational-proxy), (3) the reference distribution $q$ must be specified, (4) local stationarity must hold. If any condition fails, CIY-based terms should be dropped or replaced with simpler uncertainty-based heuristics (UCB-style bonuses, ensemble disagreement).

## Epistemic Status

Discussion-grade. The structural claim — that the optimal policy jointly maximizes value and causal information — is supported by convergent results in Bayesian RL, active inference, and information-directed sampling, but not derived from first principles within ACT. The specific form of $\lambda(M_t)$ is not derived; its behavior (increasing with $U_M$, horizon, $\rho$) is motivated by the convergent results but not formally constrained by ACT machinery.

Max attainable: robust-qualitative. The structural form is well-supported by convergent results across multiple frameworks, but the specific $\lambda$ parameterization is domain-dependent and will never be exact within ACT.

## Discussion

**Connection to the zero-mismatch ambiguity.** An agent that only exploits (acts to maximize predicted value) will tend toward confirmation bias — observing only what its model already explains ( #mismatch-signal, zero-mismatch ambiguity case (b)). Exploration via CIY-maximizing actions is the mechanism by which the agent actively tests its model.

**Connection to Section II.** For actuated agents, the exploration-exploitation tension extends to three modes: exploit (pursue $O_t$ via $\Sigma_t$), explore (improve $M_t$), deliberate (revise $\Sigma_t$). The CIY framework provides the information-theoretic grounding for why strategy edges ( #strategy-dag) need observational access ( #observability-dominance) — edges the agent cannot observe have frozen CIY.

**Connection to active inference.** The Free Energy Principle's "expected free energy" decomposes into extrinsic value (pragmatic) and epistemic value (information-seeking). ACT's formulation is structurally isomorphic: expected value ≈ extrinsic, CIY ≈ epistemic. Whether this convergence is deep or superficial is an open question. ACT grounds exploration in explicitly *causal* information rather than entropy reduction — not all uncertainty reduction is equally valuable; causal information specifically enables better *intervention*.

**(Descended from TF-08.)**
