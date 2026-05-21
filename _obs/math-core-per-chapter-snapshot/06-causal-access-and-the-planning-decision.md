# Causal Access and the Planning Decision


## Definition: Pearl's Causal Hierarchy (Recapitulation)

- **Slug**: `def-pearl-causal-hierarchy`
- **Type**: definition
- **Status**: axiomatic
- **Stage**: deps-verified
- **Depends**: `post-causal-structure`, `scope-agency`

AAT adopts Pearl's three-level hierarchy of causal reasoning — association, intervention, counterfactual — as the vocabulary for distinguishing kinds of epistemic access within the feedback loop. This segment recapitulates the hierarchy at the level of detail AAT's derivations deploy, with the canonical sources (Pearl 2009, *Causality*, 2nd ed., Cambridge; Bareinboim, Correa, Ibeling & Icard 2022, in *Probabilistic and Causal Inference: The Works of Judea Pearl*) carrying the underlying theory. The binary action requirement of #scope-agency ensures at least Level 2 access is structurally available; the chapter that follows is what deploys the hierarchy as operational machinery.

*[Definition (pearl-causal-hierarchy, recapitulating Pearl 2009 and Bareinboim et al. 2022)]*

**Level 1 — Associational**: $P(o_t \mid \mathcal{C}_{\lt t})$

*What will I observe next, given what I've observed before?*

Pattern recognition over the temporally ordered history. Available to any agent that maintains a model ( #form-agent-model), including purely passive observers. The temporal ordering constrains which associations are meaningful: $o_3$ can depend on $o_1, a_1, o_2, a_2$ but not on $o_4$.

**Level 2 — Interventional**: $P(o_t \mid do(a_{t-1}), M_{t-1})$

*What will I observe if I* do *this?*

The $do(\cdot)$ operator marks the crucial distinction: this is not "what observation tends to follow this action in the historical record" (associational) but "what will happen *because* I take this action now." This requires: (1) the agent's action temporally precedes the observation ( #post-causal-structure), (2) the agent chose the action (it was not determined by the same causes that determine the observation), (3) the environment's response carries information about the causal relationship.

Level 2 is why the feedback loop is more powerful than passive observation. By *acting* and then observing consequences, the agent obtains information about causal mechanisms — not merely about correlations. The mismatch signal $\delta_t$ ( #def-mismatch-signal), conditioned on the agent's own action, is an *interventional* signal.

**Level 3 — Counterfactual**: $P(o_t^{a'} \mid a_{t-1} = a, o_t = o)$

*Given that I did $a$ and observed $o$, what would I have observed if I had done $a'$ instead?*

This requires the model to simulate alternative histories — running the causal structure "backward" and then "forward" under different interventions. It is the most demanding epistemic level and the basis for regret computation, strategic simulation, and learning from single observations.

---



## Derived: Causal Hierarchy Requirement

- **Slug**: `der-causal-hierarchy-requirement`
- **Type**: derived
- **Status**: exact
- **Stage**: deps-verified
- **Depends**: `def-value-object`, `def-pearl-causal-hierarchy`, `scope-agency`

Evaluating the action-value $Q_O$ requires answering "what happens if I *do* action $a$?" — a Level 2 (interventional) query in Pearl's causal hierarchy. An agent that must learn the answer to this question during operation needs access to causal structure beyond what purely predictive models can provide.

*[Derived (causal-hierarchy-requirement, from value-object + pearl-causal-hierarchy)]*

Action selection via #def-value-object requires:

$$Q_O(M_t, a;\, \pi_{\text{cont}}, N_h) = \mathbb{E}\!\left[V_{O_t}(\tau) \;\middle\vert\; M_t,\; do(a_t = a),\; a_{t+1:} \sim \pi_{\text{cont}}\right]$$

The $do(\cdot)$ notation is explicit: this is an *intervention*, not a *conditioning on observed data*. By #def-pearl-causal-hierarchy, Level 2 queries ($P(Y \mid do(X))$) cannot in general be computed from Level 1 data ($P(Y \mid X)$) alone. Therefore:

An agent that must evaluate $Q_O$ from experience needs access to Level 2 knowledge — knowledge about the effects of its own interventions, not merely correlational patterns.

*[Scope Narrowing (learning-agent scope)]*

We restrict attention to **learning purposeful agents** — agents that must **acquire or refine** Level 2 knowledge during operation. This is a named sub-scope of the agency scope defined in #scope-agency. It excludes agents with **pre-compiled** interventional structure:
- PID controllers (the designer pre-computed the control law)
- LQR (separation principle gives optimal policy from model parameters)
- Hardcoded reactive policies

Pre-compiled agents are within agency scope (they have objectives and act on them) but outside learning-agent scope — their causal structure was externally supplied by a designer who had Level 2 access. **All remaining Section II results operate within learning-agent scope** unless explicitly noted otherwise. This scope narrowing focuses the theory on agents that must build or maintain their own causal understanding.

---



## Derived: Loop Provides Interventional Data Access

- **Slug**: `der-loop-interventional-access`
- **Type**: derived
- **Status**: exact
- **Stage**: draft
- **Depends**: `der-causal-hierarchy-requirement`, `der-recursive-update`, `post-causal-structure`, `scope-agent-identity`

An agent in the feedback loop generates interventional data by construction: the agent's action $a_t$ causally precedes the next observation $o_{t+1}$, and the mismatch conditioned on $a_t$ carries interventional information. This is how agents within AAT's **agency scope** ($\mathcal{S}_{\text{agency}}$, which requires $\lvert\mathcal{A}\rvert \geq 2$ and at least one action with causal effect) gain Level 2 access — not through internal architecture, but through the loop itself. Agents in the adaptive scope but outside agency scope (passive observers) lack the action contrasts needed for interventional data.

*[Derived (loop-interventional-access, from causal-structure + recursive-update)]*

By #post-causal-structure, the temporal ordering is constitutive: $a_t$ causally precedes $o_{t+1}$. The agent chose $a_t$; the environment responded with $o_{t+1}$. The feedback loop therefore generates **intervention-produced data** — data whose causal character differs from passive observation because the agent's action was a genuine cause of the subsequent observation.

The critical distinction: **"action-generated data" is not the same as "cleanly identified do-estimates."** The pair $(a_t, o_{t+1})$ is produced under intervention — the agent executed $a_t$, making it interventional in character rather than a passively observed association. But between intervention-produced data and a usable estimate of $P(o \mid do(a_t), \Omega_t)$ stand: (1) coverage — the agent must have tried diverse actions, not just one policy; (2) confounding within a time step — unobserved state variables that affect both action choice and outcome; (3) delay — consequences may appear much later than $t+1$; (4) partial observability — $o_{t+1}$ reveals only part of the outcome. The strength of causal identification from this data depends on the regime ( #scope-edge-update-causal-validity): strong in Regime A (intervention-rich domains like software and laboratory science), moderate in Regime B (partial intervention), weak in Regime C (observation-only). The claim here is about the *character* of the data (interventional, not observational), not about the agent's ability to extract clean causal estimates from it.

The mismatch signal conditioned on the agent's action:

$$\delta_t \mid a_t = o_{t+1} - \hat{o}_{t+1}(M_t, a_t)$$

carries interventional information: it tells the agent how the environment responded to its specific intervention $a_t$, relative to what the model predicted.

---



## Scope: CIY Observational Proxy

- **Slug**: `scope-ciy-observational-proxy`
- **Type**: scope
- **Status**: conditional
- **Stage**: draft
- **Depends**: `def-causal-information-yield`, `der-loop-interventional-access`

When and how causal information yield can be approximated from observational data rather than interventional experiments.

*[Definition (ciy-proxy)]*

$$\text{CIY}_{\text{proxy}}(a_{t-1}) = I(o_t; a_{t-1} \mid M_{t-1}) - I(o_t; a_{t-1} \mid \Omega_t, M_{t-1})$$

This proxy is **sign-indefinite in general** and requires causal assumptions for interpretation. The canonical CIY (interventional, #def-causal-information-yield) is the primary quantity; the proxy is auxiliary.

**Safety conditions for proxy use.** The proxy form should NOT be used in policy optimization (e.g., as the CIY term in a policy objective) because an agent maximizing a sign-indefinite quantity may optimize in the wrong direction. The proxy is suitable only for diagnostic purposes: detecting whether an action carried causal information (large proxy magnitude) vs. none (proxy near zero). For decision-making, use the canonical CIY (non-negative by construction) or a known-safe surrogate (ensemble disagreement, UCB bonuses). If the canonical CIY is intractable and no safe surrogate is available, the CIY term should be dropped from the policy objective entirely, defaulting to pure exploitation.

### Admissibility regimes

*[Scope Condition (ciy-admissibility)]*

Three regimes determine when CIY can be estimated and how strong the causal identification is:

**Regime A — Randomized interventions.** The agent varies its actions across episodes (RL agents exploring, scientists experimenting, organisms probing). CIY is directly estimable from the agent's execution data and non-negative by construction. This is the standard case for active agents within the adaptive loop ( #der-loop-interventional-access). Action variation provides the identification needed for clean interventional estimates.

**Regime B — Observational with causal assumptions.** The agent cannot freely vary actions (constrained by coordination, policy, or resource limits). CIY estimation requires additional structure: a known causal DAG, instrumental variables, or functional form assumptions. Results inherit whatever causal assumptions are made. The interventional interpretation of CIY is weaker — it holds under the assumed causal structure but not model-free.

**Regime C — Adversarial or passive observation.** The agent either did not intervene (passive monitoring) or the observation channel includes responses from potentially adversarial sources. In the passive case, CIY is zero by definition (no intervention, no interventional information). In the adversarial case, CIY from the query action itself remains non-negative, but the *content* of the response may be designed to increase model-reality mismatch. The adversary operates through the disturbance term $\rho$, not through the information measure.

The regime is a property of the **domain and the agent's action space**, not a parameter the agent chooses. Software development is typically Regime A (the agent runs tests, deploys to staging, observes results — high action variation). Organizational strategy is typically Regime B (multiple initiatives run concurrently, attribution requires assumptions). Intelligence analysis is typically Regime C (the analyst observes but does not intervene).

---



## Discussion: CIY Unified Policy Objective

- **Slug**: `disc-ciy-unified-objective`
- **Type**: discussion
- **Status**: discussion-grade
- **Stage**: draft
- **Depends**: `def-causal-information-yield`, `scope-ciy-observational-proxy`, `def-value-object`, `der-action-selection`

The exploration-exploitation tension can be expressed as a single policy objective that jointly maximizes expected value and a causal information surrogate. This formulation is *heuristic* — CIY measures action-distinguishability, not expected information gain (see #def-causal-information-yield), so the objective selects for causally distinctive actions rather than maximally informative ones. The $\lambda$-weighting partially compensates by suppressing the CIY term when model uncertainty is low, but the surrogate nature is inherent.

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

---



## Normative: Explicit Strategy Condition

- **Slug**: `norm-explicit-strategy-condition`
- **Type**: normative
- **Status**: conditional
- **Stage**: draft
- **Depends**: `def-strategy-dimension`, `der-causal-hierarchy-requirement`

An agent benefits from maintaining an explicit strategy $\Sigma_t$ when the cost of planning is less than the cost of learning through exploration alone. This is a normative design criterion — it tells you when explicit strategy is *worth it*, not that it's always necessary.

*[Normative (explicit-strategy-condition)]*

An agent benefits from explicit $\Sigma_t$ when:

$$C_{\text{plan}} + C_{\text{maintain}} \lt C_{\text{explore}} + C_{\text{repair}}$$

where:
- $C_{\text{plan}}$: cost of constructing and evaluating the strategy (deliberation, simulation, model queries)
- $C_{\text{maintain}}$: ongoing cost of keeping $\Sigma_t$ current as $M_t$ evolves (edge revision, structural updates)
- $C_{\text{explore}}$: cost of learning action-outcome mappings through direct interaction (real actions, real time, real consequences)
- $C_{\text{repair}}$: cost of correcting errors discovered only through execution (rollbacks, rework, damage)

All costs are measured in the same units (typically time or tempo-equivalent cost). The inequality requires that the two approaches produce approximately equivalent non-temporal outcomes — otherwise the comparison is between different strategies, not different approaches to the same goal.

---
