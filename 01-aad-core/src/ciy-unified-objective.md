---
slug: ciy-unified-objective
type: discussion
status: discussion-grade
depends:
  - causal-information-yield
  - ciy-observational-proxy
  - value-object
  - action-selection
stage: draft
---

# Discussion: CIY Unified Policy Objective

The exploration-exploitation tension can be expressed as a single policy objective that jointly maximizes expected value and a causal information surrogate. This formulation is *heuristic* — CIY measures action-distinguishability, not expected information gain (see #causal-information-yield), so the objective selects for causally distinctive actions rather than maximally informative ones. The $\lambda$-weighting partially compensates by suppressing the CIY term when model uncertainty is low, but the surrogate nature is inherent.

## Formal Expression

*[Discussion (unified-policy-objective — heuristic)]*

$$\pi^\ast(M_t) = \arg\max_a \left[\mathbb{E}[\text{value}(a) \mid M_t] + \lambda(M_t) \cdot \text{CIY}_q(a;\, M_t)\right]$$

The first term is exploitation (expected value given current model). The second is a *heuristic exploration term* using CIY as a surrogate for expected information gain ( #causal-information-yield). CIY measures how different the action's outcome distribution is from alternatives — this is action-distinguishability, not learning value. The surrogate is reasonable when $U_M$ is high (distinguishable actions are also informative to an uncertain agent) and poor when $U_M$ is low (distinguishable actions teach nothing to a confident agent). $\lambda(M_t)$ controls the balance:

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

Discussion-grade (heuristic). The structural claim — that a useful policy jointly considers value and causal information — is supported by convergent results in Bayesian RL, active inference, and information-directed sampling, but not derived from first principles within AAD. The use of CIY rather than proper expected information gain (EIG) makes this a *surrogate* formulation: the objective selects for causally distinctive actions, which approximately coincides with selecting for informative actions when model uncertainty is high but diverges when it is low. The $\lambda(M_t)$ weighting partially compensates (suppressing CIY when $U_M$ is low) but the compensation is heuristic, not derived.

Max attainable: *heuristic* unless CIY is replaced by proper EIG. The structural form (value + information term) is well-supported, but the specific information term (CIY rather than EIG) is a tractability-motivated surrogate that selects for distinguishability rather than informativeness. The $\lambda$ parameterization is domain-dependent and the surrogate nature of CIY places a ceiling below robust-qualitative.

## Discussion

**Connection to the zero-mismatch ambiguity.** An agent that only exploits (acts to maximize predicted value) will tend toward confirmation bias — observing only what its model already explains ( #mismatch-signal, zero-mismatch ambiguity case (b)). Exploration via CIY-maximizing actions is the mechanism by which the agent actively tests its model.

**Connection to Section II.** For actuated agents, the exploration-exploitation tension extends to three modes: exploit (pursue $O_t$ via $\Sigma_t$), explore (improve $M_t$), deliberate (revise $\Sigma_t$). The CIY framework provides the information-theoretic grounding for why strategy edges ( #strategy-dag) need observational access ( #observability-dominance) — edges the agent cannot observe have frozen CIY.

**Connection to active inference.** The expected free energy (EFE) in active inference (Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29; Da Costa, Parr, Sajid, Veselic, Neacsu & Friston 2020, "Active inference on discrete state-spaces," *J. Math. Psych.* 99; Sajid, Ball, Parr & Friston 2021, "Active inference: demystified and compared," *Neural Computation* 33) decomposes into *pragmatic value* (preferences-aligned outcomes) and *epistemic value* (expected information gain about hidden states). AAD's unified objective is structurally isomorphic: $Q_O$ ≈ pragmatic, CIY ≈ epistemic. The convergence is at the shared-shape level — objective decomposes into value-and-information terms — not unified content. Two substantive differences remain. First, AAD grounds exploration in explicitly *causal* information (action-distinguishability under $do$) rather than entropy reduction over hidden states — not all uncertainty reduction is equally valuable for purposeful action; causal information specifically enables better *intervention* (see #causal-hierarchy-requirement; the gap between CIY and proper expected information gain is logged in this segment's Epistemic Status as a known surrogate). Second, AAD does not encode preferences as priors over outcomes ($C(o) = \log P_{\mathrm{pref}}(o)$ in the AI form): AAD's $O_t$ is a value functional on trajectories ( #objective-functional), and the satisfaction-gap / control-regret diagnostic in #satisfaction-gap, #control-regret depends on this distinction — the diagnostic structure does not survive the priors-as-preferences collapse (the dark-room critique, Sun & Firestone 2020, "The dark room problem," *Trends Cog. Sci.* 24).

**(Descended from TF-08.)**
