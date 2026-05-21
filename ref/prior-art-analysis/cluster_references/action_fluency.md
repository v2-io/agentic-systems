# Cluster Reference: Action Fluency and Deliberation Cost

**Overview:** Explores the mathematical threshold where the tempo-cost of 'System 2' deliberation outweighs its epistemic benefits, forcing the agent to rely on 'System 1' implicit fluency.

---

## Canonical Source Segments

### Source: `der-deliberation-cost.md`

```yaml
---
slug: der-deliberation-cost
type: derived
status: conditional
depends:
  - der-action-selection
  - emp-update-gain
  - def-adaptive-tempo
  - form-event-driven-dynamics
stage: claims-verified
---
```


# Derived: Deliberation Cost

Explicit deliberation improves action quality by using the model for internal simulation before acting — pausing praxis to improve upcoming epistrophe. But deliberation takes time, and during that time aporia accumulates (the environment continues to evolve while the agent is not correcting). Deliberation is justified when the improvement in epistrophe quality exceeds the aporia accumulated during the pause.

## Formal Expression

**Assumption (local deliberation drift):**

*[Assumption (deliberation-drift)]*

During a deliberation pause of duration $\Delta\tau$, mismatch increases at an approximately constant local rate $\rho_{\text{delib}}$:

$$\Delta\Vert\delta\Vert_{\text{deliberation}} \approx \rho_{\text{delib}} \cdot \Delta\tau$$

This is a short-horizon assumption about inaction windows, not a full global dynamics model. It is weaker than the mismatch ODE and can be estimated directly from pause windows in empirical traces.

**Proposition (deliberation threshold):**

*[Derived (Conditional on deliberation-drift assumption)]*

Deliberation of duration $\Delta\tau$ is net-beneficial when:

$$\Delta\eta^*(\Delta\tau) \cdot \Vert\delta_{\text{post}}\Vert \gt \rho_{\text{delib}} \cdot \Delta\tau$$

where $\Delta\eta^\ast(\Delta\tau)$ is the improvement in post-deliberation update gain and $\Vert\delta_{\text{post}}\Vert$ is the mismatch magnitude the agent will face when it resumes acting.

### Derivation

1. Without deliberation, the agent acts immediately at current tempo $\mathcal{T}_0 = \nu \cdot \eta^\ast_0$.
2. With deliberation of duration $\Delta\tau$, the agent pauses, then acts with improved gain $\eta^\ast_0 + \Delta\eta^\ast$. But during the pause, mismatch has grown by $\rho_{\text{delib}} \cdot \Delta\tau$.
3. The net mismatch reduction from acting after deliberation versus acting immediately: $\text{Net} = \Delta\eta^\ast \cdot \Vert\delta_{\text{post}}\Vert - \rho_{\text{delib}} \cdot \Delta\tau$.
4. Deliberation is justified iff $\text{Net} \gt 0$. $\square$

**Optimal deliberation duration** (under diminishing returns):

*[Derived (Conditional on diminishing-returns + deliberation-drift)]*

$$\Delta\tau^* = \arg\max_{\Delta\tau} \left[\Delta\eta^*(\Delta\tau) \cdot \Vert\delta_{\text{post}}\Vert - \rho_{\text{delib}} \cdot \Delta\tau \right]$$

where $\Vert\delta_{\text{post}}\Vert$ is treated as a parameter estimated by the agent before deliberation begins (not optimized over — the agent estimates the mismatch it will face, then decides how long to deliberate). Under this approximation, the first-order condition is: $\frac{\partial \Delta\eta^\ast}{\partial \Delta\tau} \cdot \Vert\delta_{\text{post}}\Vert = \rho_{\text{delib}}$. Stop deliberating when the marginal improvement rate drops below the mismatch drift rate (normalized by post-deliberation mismatch). When the dependence $\Vert\delta_{\text{post}}\Vert = \Vert\delta_0\Vert + \rho_{\text{delib}} \cdot \Delta\tau$ is included in the optimization, the exact FOC acquires a correction factor $(1 - \Delta\eta^\ast)$ on the cost side; this is negligible when $\Delta\eta^\ast \ll 1$ (the typical case — deliberation produces small gain improvements).

## Epistemic Status

*Conditional* on the local deliberation-drift assumption. The threshold condition is derived given the assumption; the assumption itself is a local approximation validated by consistency with the global mismatch dynamics ( #result-persistence-condition). The result captures the *epistemic* benefit of deliberation (improving $\eta^\ast$); in practice, deliberation also provides a direct *action-value* benefit (choosing better actions that alter the environment trajectory), which operates through $\rho$ reduction and immediate reward — a fuller formalization would incorporate the unified policy objective ( #def-causal-information-yield) at significantly more complexity.

## Discussion

**High-$\rho_{\text{delib}}$ environments penalize deliberation.** When the environment changes rapidly during pause windows, the cost term grows quickly. Only very short deliberation with large $\Delta\eta^\ast$ can justify the pause. The model captures the same tradeoff Boyd emphasized: in fast-tempo adversarial environments, over-deliberation is fatal not because thinking is bad, but because the environment moves during the thinking. Whether the specific mechanism (mismatch drift during pause) is the dominant real-world effect is an empirical question.

**Diminishing returns.** In most models, $\Delta\eta^\ast(\Delta\tau)$ exhibits diminishing returns — the first moments of simulation yield the largest improvement. Combined with the linear cost $\rho_{\text{delib}} \cdot \Delta\tau$, this implies a finite optimal deliberation duration. Past that point, additional thinking is net-harmful.

**Implicit action as the high-tempo limit.** As $\rho_{\text{delib}} \to \infty$ or $\Delta\tau^\ast \to 0$: the optimal strategy converges to zero deliberation — pure implicit action ( #der-action-selection). This provides a mathematical basis for why high-tempo environments favor action fluency: the cost of deliberation exceeds its benefit when $\Delta\eta^\ast$ is small (action-selection is already fluent) or $\rho_{\text{delib}}$ is large.

**Deliberation as an investment.** When $\rho_{\text{delib}}$ is low (stable environment) or $\Vert\delta_{\text{post}}\Vert$ is large (significant model-reality gap), deliberation pays off. The conditions favoring deliberation — stable environment, large mismatch — resemble the high-stakes, low-urgency scenarios where deliberative reasoning (System 2) is advantageous in dual-process theories. The structural parallel is suggestive; whether the cost-benefit mechanism is the same one governing System 1/System 2 selection is an open question.

**The circularity of $\Vert\delta_{\text{post}}\Vert$.** Evaluating the threshold requires the agent to *predict* post-deliberation mismatch using its current model — the same model deliberation is meant to improve. This circularity is typically benign: $\Vert\delta_{\text{post}}\Vert$ is bounded below by $\rho_{\text{delib}} \cdot \Delta\tau$ and above by current mismatch plus that accumulation. An agent that underestimates its mismatch will under-deliberate; one that overestimates will over-deliberate. The bias is self-correcting through the feedback loop. The threshold is best understood as a *design criterion*, not a real-time decision procedure.

**Resource costs beyond time.** Real agents also incur computational and energetic costs: internal simulation burns calories, compute cycles, or opportunity cost of not processing new observations. These are additive: $\Delta\eta^\ast(\Delta\tau) \cdot \Vert\delta_{\text{post}}\Vert \gt \rho_{\text{delib}} \cdot \Delta\tau + C(\Delta\tau)$. In high-$\rho_{\text{delib}}$ environments the temporal cost dominates; in low-$\rho_{\text{delib}}$ environments, resource costs may be the binding constraint.

**Structural adaptation as an analogy.** Structural adaptation ( #result-structural-adaptation-necessity) superficially resembles deliberation with a massive $\Delta\tau$: the agent's parametric loop is partially suspended while it searches for a new model class, incurring a large mismatch debt $\rho_{\text{delib}} \cdot \Delta\tau$. However, this is an informal analogy, not a consequence of the deliberation-cost formalism. Deliberation as formalized here improves $\eta^\ast$ *within a fixed model class*; structural adaptation changes the model class itself, which is a mechanistically different operation ( #result-structural-adaptation-necessity). The cost-benefit structure may be similar in form, but the quantities involved ($\mathcal{F}(\mathcal{M})$ vs. $\eta^\ast$, model-class search vs. gain improvement) are distinct.

**Connection to temporal nesting.** Deliberation is a nested loop: internal simulation running at rate $\nu_{\text{internal}}$ within the external action loop at rate $\nu_{\text{external}}$. The convergence constraint applies: the internal loop must approximately converge before the external loop acts on its output.

**Connection to Section II.** For actuated agents, the deliberation tradeoff extends to three modes: exploit ($O_t$ via $\Sigma_t$), explore (improve $M_t$), and deliberate (revise $\Sigma_t$). The three-way allocation ( #disc-exploit-explore-deliberate) extends this segment's threshold by adding a strategic benefit term $\Delta V_\Sigma$; the extended threshold is the one genuinely derived piece. The broader three-way framing is discussion-grade — simulation shows deliberation is rarely chosen by an oracle in simple settings, and a unified objective outperforms the two-stage decomposition.

**The AI agent's dilemma.** An AI agent with 100% context turnover faces a severe version: it MUST deliberate (comprehend the codebase) before acting effectively, but during comprehension its context fills and the environment may change. The optimal comprehension depth depends on $\rho_{\text{delib}}$ and the session's action horizon. This is why reading CLAUDE.md and architecture docs first (high-CIY query actions) dominates reading random source files (low-CIY exploration).

**Domain instantiations:**

| Domain | Deliberation | $\Delta\eta^\ast$ source | When $\rho_{\text{delib}}$ is high |
|--------|-------------|----------------------|---------------------|
| Boyd's OODA | Explicit "Decide" step | War-gaming, staff analysis | Collapses to IG&C (implicit) |
| RL / MCTS | Planning rollouts | Monte Carlo tree search | Fewer rollouts, shallower search |
| MPC | Online optimization | Trajectory optimization | Shorter horizons, faster solvers |
| Human cognition | System 2 deliberation | Mental simulation | Defaults to System 1 (intuition) |
| Organization | Strategic planning | Scenario analysis | "Move fast and break things" |
| Software developer | Reading code, analyzing alternatives | Architecture analysis | Ship now, refactor later |
| AI agent | Reading codebase, planning approach | Context-building | Limit comprehension, act sooner |

**Open questions:**

1. *Computational cost of deliberation* is not just elapsed time but resource cost. A fuller model would include both temporal and computational budgets.
2. *Deliberation about deliberation*: deciding whether to deliberate itself takes time. This meta-deliberation is bounded by the same tradeoff at a higher level, suggesting a hierarchy of diminishing deliberation horizons.
3. *Deliberation that generates observations*: internal simulation can surface model inconsistencies (internal mismatch), functioning as "exploration without external action." Can deliberation generate internal CIY?


---

### Source: `disc-exploit-explore-deliberate.md`

```yaml
---
slug: disc-exploit-explore-deliberate
type: discussion
status: discussion-grade
depends:
  - disc-ciy-unified-objective
  - der-deliberation-cost
  - norm-explicit-strategy-condition
  - der-orient-cascade
  - def-control-regret
stage: draft
---
```


# Discussion: Three-Way Resource Allocation

At each decision point, an actuated agent with explicit strategy $\Sigma_t$ faces a three-way allocation of its finite cycle budget across exploit (take the currently-best action), explore (take an information-gathering action), and deliberate (pause acting to revise the model or strategy internally).

## Formal Expression

### The three activities

*[Definition (three-activity-decomposition)]*

An actuated agent's cycle budget decomposes into three activities:

1. **Exploit**: select and execute the action maximizing expected value under the current model and strategy. Earns immediate value $Q_O(M_t, a; \pi_{\text{cont}}, N_h)$.

2. **Explore**: select and execute an action maximizing causal information yield. Earns future model improvement via $\text{CIY}(a; M_t)$.

3. **Deliberate**: pause external action to run the orient cascade ( #der-orient-cascade) --- internal model refinement ($\Delta\eta^\ast$), strategy revision ($\Delta\alpha_\Sigma$), or objective reassessment. Earns improved future action quality.

**The key distinction:** Exploit and explore both involve external actions with environmental consequences. Deliberation is *internal exploration* --- simulation, counterfactual reasoning, cross-domain synthesis, and contingency planning conducted in model-space rather than environment-space. It acquires no new environmental data, but it can generate genuinely new information by combining, recombining, and extrapolating from what the agent already knows --- including knowledge from entirely different domains. A chess engine deliberating explores millions of future board states; a commander war-gaming evaluates counterfactual scenarios; a developer doing architecture review synthesizes cross-domain expertise. Deliberation's fidelity ceiling is set by model quality, not by data quantity.

### Extended deliberation threshold

*[Derived (Conditional on GA-4, deliberation-drift assumption from #der-deliberation-cost)]*

Extending #der-deliberation-cost to incorporate strategic deliberation, the deliberation threshold becomes:

$$\Delta\tau^\ast = \arg\max_{\Delta\tau \geq 0} \left[\underbrace{\Delta\eta^\ast(\Delta\tau) \cdot \lVert\delta_{\text{post}}\rVert}_{\text{epistemic benefit}} + \underbrace{\Delta V_\Sigma(\Delta\tau)}_{\text{strategic benefit}} - \underbrace{\rho_{\text{delib}} \cdot \Delta\tau}_{\text{drift cost}}\right]$$

where:
- $\Delta\eta^\ast(\Delta\tau)$ is the improvement in model update gain from $\Delta\tau$ of internal simulation ( #der-deliberation-cost)
- $\lVert\delta_{\text{post}}\rVert$ is the post-deliberation mismatch magnitude
- $\Delta V_\Sigma(\Delta\tau)$ is the improvement in strategy value from deliberation: the expected increase in $V_O$ from revising $\Sigma_t$ during the pause
- $\rho_{\text{delib}}$ is the local mismatch drift rate during inaction (GA-4)

**First-order condition:**

$$\frac{\partial \Delta\eta^\ast}{\partial \Delta\tau} \cdot \lVert\delta_{\text{post}}\rVert + \frac{\partial \Delta V_\Sigma}{\partial \Delta\tau} = \rho_{\text{delib}}$$

Stop deliberating when the marginal joint improvement rate (epistemic plus strategic) drops below the mismatch drift rate.

**Reduction to existing results.** When $\Delta V_\Sigma = 0$ (no strategy revision benefit), this reduces to the deliberation threshold in #der-deliberation-cost. When $\Delta\tau^\ast = 0$ (deliberation never beneficial), the agent acts immediately.

### On the structure of the allocation

*[Discussion (allocation-structure)]*

**Two-stage decomposition.** The three-way allocation can be decomposed into two nested decisions: (1) how long to deliberate before acting, (2) conditional on acting, which action to take (solved by #disc-ciy-unified-objective). This decomposition is natural because exploit and explore are both external actions ($\in \mathcal{A}$), while deliberation is internal processing. However, this decomposition is a *modeling convenience*, not a structural necessity. A unified objective over $\mathcal{A} \cup \{\text{deliberate}\}$ with temporal discount $\gamma$ is equally valid:

$$\bar{\pi}^\ast = \arg\max_{\bar{a} \in \mathcal{A} \cup \{\text{deliberate}\}} \bar{Q}(\bar{a}; M_t, \gamma)$$

where $\bar{Q}(\text{deliberate}) = \gamma \cdot \mathbb{E}[V_{\text{act}}(f_{\text{delib}}(M_t))]$ and $\bar{Q}(a) = r(a) + \gamma \cdot \mathbb{E}[V_{\text{act}}(M_{t+1})]$.

The two-stage decomposition is useful because it allows reusing the CIY-unified objective for the action-selection step, but it is not the unique or forced structure.

**Additive benefit decomposition.** The objective function above decomposes deliberation benefit into additive epistemic and strategic terms. This assumes the two benefits are approximately independent. Under directed separation ( #der-directed-separation), $M_t$ updates independently of $G_t$, which makes the decomposition structurally motivated for Class 1 (Separated) agents. However, strategic benefit depends on the improved model ($\Delta V_\Sigma(\Delta\tau, M_t + \Delta M_t(\Delta\tau))$), creating an interaction that the additive form ignores. The additive form is a linearization that holds when $\Delta M_t$ is small relative to $M_t$. For Class 3 (Coupled) agents, epistemic and strategic deliberation are coupled, and the additive decomposition is a convenience.

### Control regret as deliberation ceiling

*[Discussion (deliberation-ceiling)]*

When $\delta_{\text{regret}} \approx 0$ ( #def-control-regret), strategic deliberation has no value: the agent is already executing the best available strategy. This is the formal reason why low control regret suppresses deliberation. The ceiling on strategic deliberation value is $\delta_{\text{regret}}$ --- the most the agent could gain by finding a better strategy.

However, this ceiling applies only to the *strategy-revision* channel of deliberation. Deliberation may also:
- Reveal that the *objective* should change (step 5 of the orient cascade), producing value not bounded by $\delta_{\text{regret}}$
- Reduce *uncertainty about* strategy quality, enabling more confident exploitation even when the strategy doesn't change

### Connection to active inference

*[Discussion (ai-connection)]*

The exploit/explore decomposition maps cleanly onto the expected free energy (EFE) decomposition into *pragmatic value* (preferences-aligned outcomes) and *epistemic value* (expected information gain about hidden states) in active inference (Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29; Da Costa, Parr, Sajid, Veselic, Neacsu & Friston 2020, "Active inference on discrete state-spaces," *J. Math. Psych.* 99 §2.4; Sajid, Ball, Parr & Friston 2021, "Active inference: demystified and compared," *Neural Computation* 33). Under the mapping, AAT's exploit term $Q_O$ corresponds to EFE's pragmatic value when the value functional $V_{O_t}$ is read as expected log-preferences, and AAT's CIY corresponds to EFE's epistemic value when the relevance variable is read as the hidden-state posterior. The structural correspondence is at the shared-shape level: both decomposed into value-and-information terms, but AAT does *not* commit to AI's preferences-as-priors form (preserving the satisfaction-gap diagnostic in #def-satisfaction-gap, which the priors-as-preferences collapse would erase).

The deliberation axis — internal exploration in model-space rather than environment-space — is structurally adjacent to "sophisticated active inference" (Friston, Da Costa, Hafner, Hesp & Parr 2021, "Sophisticated inference," *Neural Computation* 33), which handles bounded computation via recursive expected free energy with depth-limited belief-about-belief reasoning. AAT's machinery for deliberation cost ( #der-deliberation-cost) and the extended deliberation threshold above derives the same trade-off via per-edge persistence and evidence starvation, with the structural advantage that the depth bound $d^\ast$ is causally derived from the strategy DAG rather than from belief-recursion depth. The two frameworks address the same problem with different machinery; AAT can credit the AI lineage as a co-developed alternative.

**Exploit-regret and the strategy-cost objective.** The exploit term's control regret $\delta_{\text{regret}} = A_O - V_O(\pi_{\text{current}})$ ( #def-control-regret) is the same decision-theoretic regret that underwrites the KL-direction derivation in #form-strategy-complexity-cost. There, strategy-induced regret $R(Q_{\Sigma_t}) = V(a^\ast) - \mathbb E_{a \sim Q_{\Sigma_t}}[V(a)]$ is bounded above by $V_{\max}\sqrt{\tfrac{1}{2}D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})}$ (Pinsker), forcing the KL direction with $\pi^\ast$ first. The exploit term thus shares structure with the strategy-cost relevance term: both are regret-aligned, with the action-selection objective operating pointwise and the strategy-cost objective operating over the strategy's induced distribution. This is the structural cleanup that "value and information term" shares with EFE's pragmatic-epistemic decomposition at the shape level, without the preferences-as-priors commitment — the regret framing is the AAT-internal derivation of the direction that the variational-inference literature arrives at from free-energy-gradient arguments.

### Qualitative regime descriptions

*[Discussion (qualitative-regimes)]*

The three activities have natural dominance conditions that follow from the structure of the problem:

**Exploit dominates** when the strategy is near-optimal ($\delta_{\text{regret}} \approx 0$), model uncertainty is low ($\lambda(M_t) \approx 0$), and the environment penalizes pauses ($\rho_{\text{delib}}$ high). The agent knows what to do and must act now. This is Boyd's implicit guidance and control.

**Explore dominates** when model uncertainty is high ($U_M$ large), and the model needs correction via external evidence that internal simulation cannot provide. Exploration acquires new data; deliberation only processes existing data.

**Deliberate dominates** when the strategy needs revision ($\delta_{\text{regret}} \gg 0$ or $\delta_{\text{strategic}} \gg 0$), the environment is stable during pauses ($\rho_{\text{delib}}$ low), and the agent has unprocessed information or structural hypotheses it can evaluate internally. This regime requires that internal computation is cheaper or more efficient than external probing --- otherwise exploration dominates deliberation.

**Boundary conditions.** As $\rho_{\text{delib}} \to \infty$: $\Delta\tau^\ast \to 0$, and the allocation collapses to the binary exploit/explore tradeoff. As $\lambda \to 0$ and $\Delta V_\Sigma \to 0$: the allocation collapses to pure exploitation. As $\delta_{\text{regret}} \to 0$: strategic deliberation value vanishes, and the allocation reduces to #der-deliberation-cost's epistemic think/act threshold combined with #disc-ciy-unified-objective's exploit/explore balance.

These regime descriptions are qualitative observations about the problem structure, not derived predictions. They restate what the constituent objectives already imply (high uncertainty favors information acquisition, low cost favors deliberation) without adding quantitative content. The theory does not provide the thresholds at which one regime transitions to another --- these are domain-specific.

## Epistemic Status

*Discussion-grade.* The extended deliberation threshold is *derived* (conditional on GA-4 and the deliberation-drift assumption from #der-deliberation-cost) and is the one genuinely formal contribution of this segment. The regime descriptions are *discussion-grade* --- qualitatively correct observations that restate the problem structure. The two-stage decomposition is a *formulation choice*, not a derived result. The additive benefit decomposition is a *linearization* that is structurally motivated under directed separation but not derived.

**Simulation check (drifting multi-armed bandit, `spikes/sim-three-way-tradeoff.py`):** The three-way allocation with perfect foresight outperformed binary exploit/explore by 2--6% across five configurations. The oracle almost never chose deliberation (0--8 out of 200 steps). Exploration earned 3.5x more information per step than deliberation. A unified objective (single argmax with temporal discount) outperformed two-stage UCB by 8--13%. The simulation is UNFAVORABLE to deliberation (no strategy structure, no irreversible actions, small action space), so these results are a lower bound on deliberation's value in complex domains. The simulation confirms that deliberation adds little in simple settings and that the two-stage decomposition is not necessary.

Max attainable: *discussion-grade* for the overall framing. The extended deliberation threshold could reach *conditional* (it inherits its status from #der-deliberation-cost). The regime descriptions are unlikely to advance beyond discussion-grade without domain-specific instantiation that provides quantitative thresholds.

## Discussion

**Why this is Section II content, not Section I.** Section I's deliberation-cost handles the binary think/act threshold using only $M_t$ and $\eta^\ast$. The three-way allocation is inherently a Section II result because it requires:
- $\Sigma_t$ to exist (the strategy that deliberation can improve)
- $\delta_{\text{regret}}$ to be defined (the signal that motivates strategic deliberation)
- The orient cascade (the internal structure of what "deliberation" does for an actuated agent)

Without $G_t$, there is no strategic deliberation mode --- the agent can only improve $M_t$ or act, which is the Section I binary.

**Deliberation as internal exploration.** The deepest characterization of deliberation is not "computation on existing data" but *lower-cost, more efficient, usually lower-fidelity exploration in model-space rather than environment-space*. All three activities are forms of information acquisition; they differ in source, cost, fidelity, and scope:

- **Exploitation** acquires value directly from the environment.
- **Exploration** acquires information from the environment via novel observations --- high fidelity, high cost (real actions have real consequences).
- **Deliberation** acquires information from the agent's internal model via simulation, synthesis, and counterfactual reasoning --- lower fidelity (model may be wrong), lower cost (no environmental consequences), but potentially unlimited scope.

A chess engine deliberating is not "reprocessing existing data" --- it is exploring a vast space of futures that no amount of external probing could cover at the same rate. A military commander war-gaming is performing Level 3 counterfactual reasoning ( #def-pearl-causal-hierarchy): "what *would have happened* if the enemy had moved north?" A developer doing architecture review is synthesizing patterns from entirely different domains --- cross-domain expertise that no local exploration of the current codebase could surface. An AI agent planning its approach is simulating the universe it inhabits and weighing future possibilities.

**What deliberation can do that external exploration cannot:**
- **Counterfactual reasoning** (Level 3): evaluate actions never taken, in situations never encountered
- **Cross-domain synthesis**: bring expertise and experience from other contexts to bear on the current problem
- **Combinatorial search**: systematically evaluate a space of futures too large to probe externally (chess, Go, multi-step planning)
- **Contingency planning**: prepare responses to events that haven't happened yet
- **Risk assessment**: evaluate irreversible actions before committing to them

**Why deliberation has diminishing returns:** The agent's internal model has finite fidelity. Deeper simulation eventually hits the model's accuracy boundary --- further deliberation generates predictions the model cannot reliably distinguish. This explains why deliberation is most valuable early (when many model-derivable insights remain unextracted) and why high-fidelity internal models increase deliberation's value. But unlike "computation on existing data," this ceiling is about model fidelity, not data quantity --- an agent with a perfect model and finite data can still generate unbounded value from deliberation (this is exactly what MCTS does).

**The computational-extraction-gap framing.** A sharper structural characterization than "third activity on par with exploit and explore" reads deliberation's value as the *gap between information in the existing data and information already extracted into $M_t$*. The three activities differ in which bit-channel they operate on: exploitation earns value-bits (direct reward, no new information); exploration earns environment-bits (reduces $H(\Omega_t \mid M_t)$ via new observations); deliberation earns inference-bits (reduces $H(\theta \mid M_t, \mathcal C_t)$ via additional computation on existing data). The information ceiling for deliberation is

$$I_{\text{delib}}(\Delta\tau) \;\le\; I_{\mathcal C_t} \;-\; I_{\text{already-extracted}}$$

For an agent that processes its observation history optimally (full Bayesian update, exact inference), this gap is zero — deliberation has no value. The gap exists when the agent uses point estimates instead of full posteriors, when inference is intractable and approximate methods (MCMC, variational inference) have not converged, or when the agent has structural hypotheses it has not yet tested against existing data (cross-arm correlations in bandits; common-cause structure at L1; etc.). Three structural consequences follow:

1. *Agent-architecture-dependent*: a hypothetical perfect-Bayesian has zero deliberation value; real bounded-rational agents have non-zero deliberation value calibrated by their inference budget.
2. *Diminishing within a cycle*: each deliberation step closes part of the computation gap, with the next step's marginal value bounded by the remaining gap.
3. *Not independent of exploration*: new data changes what's available to extract; an exploration step expands $I_{\mathcal C_t}$ and therefore can *raise* the ceiling on subsequent deliberation value.

This places deliberation as a different *kind* of thing than exploit/explore — it operates on existing data rather than acquiring new data or value — even though the three-way framing in the Formal Expression treats them as comparable allocation targets. Both readings are valid: the allocation framing is useful for engineering decisions about $\Delta\tau$; the gap-closing framing is useful for understanding *why* deliberation has the structural properties it does.

**Deliberation's comparative advantage** is greatest when:
- Internal simulation is cheaper than external probing (bits per unit cost, not bits per timestep)
- The action space is too large for systematic exploration (planning/search)
- Actions are irreversible and error costs are high (deliberation as risk management)
- The agent has cross-domain knowledge exploitable by synthesis
- The model supports counterfactual reasoning (Level 3 access)

**Connection to #form-strategy-complexity-cost.** Deliberation duration required to revise $\Sigma_t$ grows with strategy complexity. The description length $\operatorname{DL}(\Sigma_t)$ from #form-strategy-complexity-cost provides a lower bound on the deliberation time needed for meaningful revision.

**Connection to #def-strategic-tempo.** Strategic tempo $\mathcal T_\Sigma$ is the rate of useful strategy revision from *external* evidence. Deliberation provides an *internal* channel for strategy revision that supplements $\mathcal T_\Sigma$.

**Domain instantiations:**

| Domain | Exploit | Explore | Deliberate |
|--------|---------|---------|------------|
| Military (Boyd) | Execute the mission | Reconnaissance, probing attacks | Staff planning, war-gaming |
| RL agent | Greedy action | $\varepsilon$-exploration, UCB | MCTS planning, model-based rollouts |
| Software developer | Write code along current plan | Try unfamiliar approach, spike | Architecture review, read docs |
| Organization | Execute strategy | A/B test, pilot program | Strategic planning offsite |
| AI coding agent | Execute planned edit | Read unfamiliar code, run tests | Plan approach, analyze requirements |

## Working Notes

- **Migration note (2026-05-09 GUC rename):** Class 2 ↔ Class 3 swap. Pre-2026-05-09: Class 2 = fully merged, Class 3 = partially modular. Post: Class 2 = Partial, Class 3 = Coupled. Removed at `candidate` stage per FORMAT.md Gate 4.
- **Open: conditions for deliberation dominance.** The simulation showed deliberation rarely dominates in bandit settings (no strategy structure, small action space, reversible actions). The open question is: what formal conditions make deliberation strictly dominate external exploration? Likely candidates: large action spaces requiring combinatorial search, irreversible actions requiring risk assessment, cross-domain knowledge available for synthesis, and high model fidelity enabling accurate counterfactual reasoning. The bandit simulation was unfavorable to deliberation by design (no structure to exploit internally); a planning-heavy domain (chess, logistics, architecture design) would likely show the opposite.
- **Open: the additive decomposition.** Under what conditions is the additive separation of epistemic and strategic benefit a good approximation? The interaction term ($\Delta V_\Sigma$ depends on $\Delta M_t$) may be quantitatively significant when deliberation produces a model insight that transforms the strategy evaluation. Formalizing this requires a coupled model of epistemic and strategic improvement.

- **The $\Delta V_\Sigma$ approximation misses two channels of deliberation value.** The strategic-deliberation ceiling $\Delta V_\Sigma \approx \delta_{\text{regret}} \cdot \Pr[\text{revision succeeds}]$ captures only the *strategy-revision* channel — deliberation that finds a better $\Sigma_t$ within the current objective $O_t$. Two other channels of value are not in the approximation: (a) the *objective-revision* channel, where deliberation reveals that $O_t$ should change (step 5 of the orient cascade); the value is then $V_{O'}(M_t, \pi') - V_O(M_t, \pi)$ where $O'$ is the revised objective, a quantity with no necessary relationship to $\delta_{\text{regret}}$ (which measures regret *within* the current objective); (b) the *uncertainty-reduction* channel, where deliberation confirms that the current strategy is good and shifts the agent from cautious mixed-mode to confident exploitation; the value of *certainty about your strategy* is a behavioral effect not captured by $\delta_{\text{regret}}$. The approximation is best read as a *strategy-revision ceiling* rather than a full deliberation-value ceiling; the other two channels operate on different quantities and should be tracked separately if they matter for the use case.

- **Landing context.** The adversarial analysis behind the Epistemic Status downgrade (formulation-choice + linearization + discussion-grade tags rather than "derived" headlines) landed in the 2026-05-12 (late) Group-I surgical-promotion sweep; see CHANGELOG 2026-05-13. Its four attacks (two-stage decomposition not forced; additive form unjustified; $\Delta V_\Sigma$ approximation inadequate; dominance regimes trivially correct) are absorbed into the Epistemic Status block, the §Discussion "Computational-extraction-gap framing" sub-section, and the missing-channels Working Note above. Originating spike is absorbed archaeology, not a live reference.
- **Open: the unified vs two-stage question.** Simulation suggests the unified approach may be strictly better. If so, the segment should present the unified formulation as primary and the two-stage decomposition as a computational simplification.
- **Relationship to working memory.** Deliberation requires maintaining internal state. For LLM agents, this manifests as context-window competition: tokens spent "thinking" are tokens unavailable for representing the problem state. This architectural constraint on deliberation is real but domain-specific.


---

