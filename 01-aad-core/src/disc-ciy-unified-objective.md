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
where $\mathcal{I}_o(a)$ is the Fisher Information Matrix (Matrix CIY) and $\Lambda$ is the positive-semidefinite shadow price matrix of the survival constraint.

Max attainable for this segment: *discussion-grade* (it is a discussion of the underlying result, per `type: discussion`). Max attainable for the underlying derivation in `#deriv-causal-ib-lmi`: *exact*. The structural form is fully grounded in AAD's physical survival bounds and standard semidefinite programming, eliminating the need to treat exploration as an ad-hoc heuristic.

## Discussion

**Two Parallel Exploration Drives.** AAD dictates two correlated but distinct motivations for exploration, acting at opposite ends of the uncertainty spectrum:
1. **Epistemic Information Gain ($\lambda_{\text{info}} \propto U_M$):** The primary CIY formulation. The agent explores to reduce its model uncertainty. This drive dominates when $U_M$ is high.
2. **The Survival Imperative ($\lambda_{\text{surv}} \propto 1/U_M$):** As mathematically proven in `#deriv-causal-ib-exploration`, an agent with high confidence (low $U_M$) in a drifting environment ($\rho > 0$) mathematically guarantees its own death by ignoring noisy observations. To force the necessary correction, the Lyapunov persistence constraint dictates an immense shadow price ($\lambda_{\text{surv}} \to \infty$ as $U_M \to 0$) forcing the agent to seek unambiguous observations (low $U_o$ / high CIY). 

The dark-room problem is bypassed entirely by the Survival Imperative: exploration is not driven by preferences-as-priors, but by the literal physical boundaries of the Lyapunov sector constraint.

**Connection to the zero-mismatch ambiguity.** An agent that only exploits (acts to maximize predicted value) will tend toward confirmation bias — observing only what its model already explains ( #def-mismatch-signal, zero-mismatch ambiguity case (b)). Exploration via CIY-maximizing actions is the mechanism by which the agent actively tests its model.

**Connection to Section II.** For actuated agents, the exploration-exploitation tension extends to three modes: exploit (pursue $O_t$ via $\Sigma_t$), explore (improve $M_t$), deliberate (revise $\Sigma_t$). The CIY framework provides the information-theoretic grounding for why strategy edges ( #def-strategy-dag) need observational access ( #der-observability-dominance) — edges the agent cannot observe have frozen CIY.

**Connection to active inference.** The expected free energy (EFE) in active inference (Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29; Da Costa, Parr, Sajid, Veselic, Neacsu & Friston 2020, "Active inference on discrete state-spaces," *J. Math. Psych.* 99; Sajid, Ball, Parr & Friston 2021, "Active inference: demystified and compared," *Neural Computation* 33) decomposes into *pragmatic value* (preferences-aligned outcomes) and *epistemic value* (expected information gain about hidden states). AAD's unified objective is structurally isomorphic: $Q_O$ ≈ pragmatic, CIY ≈ epistemic. The convergence is at the shared-shape level — objective decomposes into value-and-information terms — not unified content. Two substantive differences remain. First, AAD grounds exploration in explicitly *causal* information (action-distinguishability under $do$) rather than entropy reduction over hidden states — not all uncertainty reduction is equally valuable for purposeful action; causal information specifically enables better *intervention* (see #der-causal-hierarchy-requirement; the gap between CIY and proper expected information gain is logged in this segment's Epistemic Status as a known surrogate). Second, AAD does not encode preferences as priors over outcomes ($C(o) = \log P_{\mathrm{pref}}(o)$ in the AI form): AAD's $O_t$ is a value functional on trajectories ( #form-objective-functional), and the satisfaction-gap / control-regret diagnostic in #def-satisfaction-gap, #def-control-regret depends on this distinction — the diagnostic structure does not survive the priors-as-preferences collapse (the dark-room critique, Sun & Firestone 2020, "The dark room problem," *Trends Cog. Sci.* 24).

**Regret-bound connection to the strategy-cost objective.** AAD's $Q_O$ term connects to the strategy-cost objective in #form-strategy-complexity-cost via a regret-bound derivation: strategy-induced regret $R(Q_{\Sigma_t}) = V(a^\ast) - \mathbb{E}_{Q_{\Sigma_t}}[V(a)]$ is bounded by a divergence between $\pi^\ast$ and $Q_{\Sigma_t}$, with the KL direction $\pi^\ast$-first forced (full derivation in #deriv-strategy-cost-regret-bound). Under AAD's canonical scope of deterministic $\pi^\ast$, the Bretagnolle-Huber identity $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log(1 - \operatorname{TV}(\pi^\ast, Q_{\Sigma_t}))$ holds *exactly* (Bretagnolle & Huber 1978), giving the tight regret bound $R(Q_{\Sigma_t}) \leq V_{\max}\bigl(1 - e^{-D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}\bigr)$ with matching lower bound $\Delta_{\min}\bigl(1 - e^{-D_{\mathrm{KL}}}\bigr)$ on isolated optima ( #deriv-strategy-cost-regret-bound §4). Pinsker's $V_{\max}\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$ remains the correct loose general form for stochastic-$\pi^\ast$ extensions where the BH identity degrades back to inequality. The structural point: "value and information term" shares *shape* with EFE's pragmatic-epistemic decomposition, and the KL direction in the strategy-cost's variational form shares direction with variational inference — but AAD's derivation is via decision-theoretic regret bound on $Q_O$ rather than via free-energy-gradient flow, which is the AAD-internal route that does not depend on the priors-as-preferences encoding.

## Working Notes

- *Lineage:* descended from TF-08 in the prior TFT corpus (kept as Working Notes provenance per FORMAT.md voice discipline).
