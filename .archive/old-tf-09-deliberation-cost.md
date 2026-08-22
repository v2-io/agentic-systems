# TF-09: The Cost of Deliberation (Derived)

Explicit deliberation (TF-07) improves action quality by using the model for internal simulation before acting. But deliberation takes time — and during that time, the environment continues to evolve. This creates a fundamental trade-off between action quality and action timeliness.

**Epistemic status**: *Derived, conditional on a local deliberation-drift assumption.* Depends on TF-07 (action selection), TF-06 (gain quality), and TF-04 (event timing). The threshold condition (Proposition 9.1) uses a local assumption that mismatch accumulates approximately linearly while the agent is not acting. TF-11 later provides a global mismatch-dynamics hypothesis consistent with this local assumption.

## Assumption 9.0: Local Deliberation Drift

During a deliberation pause of duration $\Delta\tau$, mismatch increases at an approximately constant local rate $\rho_{\text{delib}}$:

*[Hypothesis (Local Deliberation Drift)]*
$$\Delta\Vert\delta\Vert_{\text{deliberation}} \approx \rho_{\text{delib}} \cdot \Delta\tau$$

This is a short-horizon assumption about inaction windows, not a full global dynamics model. It is weaker than TF-11's ODE and can be estimated directly from pause windows in empirical traces.

## The Deliberation Trade-off

When an agent deliberates for duration $\Delta\tau$:

**Benefit**: The quality of the subsequent action improves. Specifically, the effective update gain on the *next* update cycle increases by $\Delta\eta^\ast(\Delta\tau)$ — the agent's model-based simulation has refined its predictions and action selection, leading to better mismatch correction when it does act.

**Cost**: During $\Delta\tau$, the environment evolves at local drift rate $\rho_{\text{delib}}$, introducing new mismatch that the agent is not correcting (because it is deliberating, not acting). By Assumption 9.0, the accumulated mismatch during deliberation is:

*[Derived (Conditional on Assumption 9.0)]*
$$\Delta\Vert\delta\Vert_{\text{deliberation}} = \rho_{\text{delib}} \cdot \Delta\tau$$

## Proposition 9.1: Deliberation Threshold

**Statement.** Deliberation of duration $\Delta\tau$ is net-beneficial when the improvement in post-deliberation adaptation exceeds the mismatch accumulated during deliberation:

*[Derived (Conditional on Assumption 9.0, deliberation-threshold)]*
$$\Delta\eta^*(\Delta\tau) \cdot \Vert\delta_{\text{post}}\Vert \gt \rho_{\text{delib}} \cdot \Delta\tau$$

where $\Vert\delta_{\text{post}}\Vert$ is the mismatch magnitude the agent will face when it resumes acting.

**Scope of the comparison.** This is a *single-cycle* threshold: the LHS is the additional mismatch corrected in the first post-deliberation correction event, under the fractional-reduction interpretation ($\delta_{\text{new}} = (1-\eta)\delta_{\text{old}}$, so that $\eta \cdot \Vert\delta\Vert$ is the mismatch removed per event). The RHS is the total mismatch accumulated during the pause. If the gain improvement persists across multiple future correction cycles, the cumulative benefit may justify deliberation even when this single-cycle threshold is not met. As a *design criterion*, the threshold is conservative — it demands the benefit be realizable in one cycle.

**Limitation: epistemic benefit only.** This formalization captures the *epistemic* benefit of deliberation — improving the quality of model updates ($\Delta\eta^\ast$). In practice, deliberation often provides a second, distinct benefit: improving *action quality* directly (choosing a fundamentally better action that alters the environment trajectory). A chess player deliberating doesn't just learn more from the opponent's response — they avoid being checkmated. This direct action-value benefit operates through $\rho$ (better actions reduce future disturbance) and through immediate reward, neither of which is captured in $\Delta\eta^\ast$. A fuller formalization would incorporate the expected value improvement from TF-08's policy objective, at the cost of significantly more complexity. For the current purpose, Proposition 9.1 provides a *sufficient* condition for deliberation based on the epistemic channel alone; the action-value channel provides additional justification when present.

**Note on $\Vert\delta_{\text{post}}\Vert$.** Evaluating this threshold requires the agent to *predict* post-deliberation mismatch using its current model — the same model that deliberation is meant to improve. This circularity is typically benign: $\Vert\delta_{\text{post}}\Vert$ is bounded below by the accumulation term $\rho_{\text{delib}} \cdot \Delta\tau$ (which is model-independent) and above by current mismatch plus that accumulation. The agent's estimate may be biased — a model that underestimates its own mismatch will under-deliberate, while one that overestimates will over-deliberate — but the bias is self-correcting through the feedback loop: under-deliberation leads to poor actions that increase observable mismatch, eventually triggering longer deliberation. The practical consequence is that Proposition 9.1 is best understood as a *design criterion* (the deliberation duration should satisfy this inequality) rather than a *decision procedure* (compute $\Vert\delta_{\text{post}}\Vert$ exactly, then decide).

**Proof sketch.**

1. Without deliberation, the agent acts immediately. Its mismatch correction rate is $\mathcal T_0 = \nu \cdot \eta^\ast_0$ (its current tempo).

2. With deliberation of duration $\Delta\tau$, the agent pauses, then acts with improved gain $\eta^\ast_0 + \Delta\eta^\ast$. But during the pause, mismatch has grown by $\rho_{\text{delib}} \cdot \Delta\tau$ (Assumption 9.0).

3. The net mismatch *reduction* from acting after deliberation versus acting immediately is:

*[Derived (Conditional on Assumption 9.0)]*
$$\text{Net} = \underbrace{\Delta\eta^* \cdot \Vert\delta_{\text{post}}\Vert}_{\text{better correction}} - \underbrace{\rho_{\text{delib}} \cdot \Delta\tau}_{\text{accumulated drift}}$$

4. Deliberation is justified iff $\text{Net} \gt 0$. $\square$

**Note on resource costs.** This analysis captures the *temporal* cost of deliberation (mismatch accumulation during inaction). Real agents also incur *computational and energetic* costs: internal simulation burns calories, compute cycles, or opportunity cost of not processing new observations. These costs are additive with the mismatch cost, making the threshold strictly tighter: $\Delta\eta^\ast(\Delta\tau) \cdot \Vert\delta_{\text{post}}\Vert \gt \rho_{\text{delib}} \cdot \Delta\tau + C(\Delta\tau)$ where $C(\Delta\tau)$ is the resource cost. In high-$\rho_{\text{delib}}$ environments the temporal cost dominates and the omission is immaterial; in low-$\rho_{\text{delib}}$ environments where the temporal cost is small, resource costs may be the binding constraint on deliberation. See Open Question #1 for further discussion.

## Consequences

### High-$\rho_{\text{delib}}$ environments penalize deliberation

When the environment is changing rapidly during pause windows ($\rho_{\text{delib}}$ large), the cost term $\rho_{\text{delib}} \cdot \Delta\tau$ grows quickly. Only *very* short deliberation with *large* $\Delta\eta^\ast$ can justify the pause. This formalizes a principle Boyd emphasized repeatedly: in fast-tempo adversarial environments, over-deliberation is fatal not because thinking is bad, but because the environment moves during the thinking.

### Diminishing returns on deliberation

In most models, $\Delta\eta^\ast(\Delta\tau)$ exhibits diminishing returns — the first moments of simulation yield the largest improvement (identifying the best action from a small candidate set), while additional time yields progressively smaller refinements. Combined with the linear cost $\rho_{\text{delib}} \cdot \Delta\tau$, this implies an **optimal deliberation duration**:

*[Derived (Conditional on Diminishing-Returns Assumption + Assumption 9.0)]*
$$\Delta\tau^* = \arg\max_{\Delta\tau} \left[\Delta\eta^*(\Delta\tau) \cdot \Vert\delta_{\text{post}}\Vert - \rho_{\text{delib}} \cdot \Delta\tau \right]$$

At the first-order condition: $\frac{\partial \Delta\eta^\ast}{\partial \Delta\tau} \cdot \Vert\delta_{\text{post}}\Vert = \rho_{\text{delib}}$.

### Implicit action as the high-tempo limit

As $\rho_{\text{delib}} \to \infty$ or $\Delta\tau^\ast \to 0$: the optimal strategy converges to **zero deliberation** — pure implicit action from TF-07. This provides a mathematical basis for why high-tempo environments favor implicit action (TF-07's "action fluency"): the cost of deliberation exceeds its benefit when $\Delta\eta^\ast$ is small (the model's action-selection is already fluent) or $\rho_{\text{delib}}$ is large (the environment penalizes delay).

### Deliberation as an investment

When $\rho_{\text{delib}}$ is low (stable environment during pause windows) or $\Vert\delta_{\text{post}}\Vert$ is large (the agent faces a significant model-reality gap), deliberation pays off. This formalizes the intuition that deliberation is appropriate for novel, high-stakes, low-urgency situations — exactly the conditions where System 2 thinking is optimal in dual-process theory.

## Connection to Temporal Nesting (TF-11)

Deliberation is itself a *nested loop*: an internal simulation running at some internal clock rate $\nu_{\text{internal}}$ within the external action loop at rate $\nu_{\text{external}}$. The convergence constraint from TF-11 applies: the internal loop must approximately converge before the external loop acts on its output.

The local drift rate here, $\rho_{\text{delib}}$, is the short-horizon pause-window quantity used in Proposition 9.1. TF-11's $\rho(t)$ is the global mismatch-introduction rate in the full dynamics model. Under local stationarity during the deliberation window, $\rho_{\text{delib}} \approx \rho(t)$ over that interval.

## Domain Instantiations

| Domain | Deliberation | $\Delta\eta^\ast$ source | When $\rho_{\text{delib}}$ is high |
|--------|-------------|----------------------|---------------------|
| Boyd's OODA | Explicit "Decide" step | War-gaming, staff analysis | Collapses to IG&C (implicit) |
| RL / MCTS | Planning rollouts | Monte Carlo tree search | Fewer rollouts, shallower search |
| MPC | Online optimization | Trajectory optimization | Shorter horizons, faster solvers |
| Human cognition | System 2 deliberation | Mental simulation, reasoning | Defaults to System 1 (intuition) |
| Organization | Strategic planning | Scenario analysis, committees | "Move fast and break things" |
| Scientific method | Theoretical prediction | Model-based prediction before experiment | Rapid prototyping, fail-fast |

## Open Questions

1. **Computational cost of deliberation** is not just elapsed time but also *resource* cost (energy, opportunity cost of not processing new observations). A fuller model would include both temporal and computational budgets.

2. **Deliberation about deliberation**: The agent must decide *whether* to deliberate, which itself takes time. This meta-deliberation is bounded by the same trade-off at a higher level, suggesting a hierarchy of diminishing deliberation horizons.

3. **Deliberation that *generates* observations**: Internal simulation can surface model inconsistencies (a form of internal mismatch), functioning as "exploration without external action." This blurs the line between deliberation-as-cost and deliberation-as-information-source. Connection to TF-08's CIY: can deliberation generate *internal* causal information yield?
