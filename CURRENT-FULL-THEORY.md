# ACT: Agentic Cycle Theory

A first-principles theory of adaptive, purposeful agents under uncertainty.

**Working draft.** This is the current canonical outline of the theory — the argument laid out claim by claim. The ordering is the current best linearization of the dependency DAG; it will change as the theory develops. Slugs are the stable identities. Treat this as a living proof sketch, not a specification.

See `FORMAT.md` for segment file conventions. See `notation.md` for symbols, conventions, and units.


## Index

| Slug | Type | § | Status |
|------|------|---|--------|
| [#temporal-optimality](src/temporal-optimality.md) | Axiom | I | written |
| [#agent-environment](src/agent-environment.md) | Definition | I | written |
| [#observation-function](src/observation-function.md) | Definition | I | written |
| [#action-transition](src/action-transition.md) | Definition | I | written |
| [#scope-condition](src/scope-condition.md) | Scope | I | written |
| [#composition-consistency](src/composition-consistency.md) | Axiom | I | — |
| [#causal-structure](src/causal-structure.md) | Axiom | I | written |
| [#pearl-causal-hierarchy](src/pearl-causal-hierarchy.md) | Definition | I | written |
| [#chronica](src/chronica.md) | Definition | I | written |
| [#agent-model](src/agent-model.md) | Formulation | I | written |
| [#information-bottleneck](src/information-bottleneck.md) | Formulation | I | written |
| [#model-sufficiency](src/model-sufficiency.md) | Definition | I | written |
| [#model-class-fitness](src/model-class-fitness.md) | Definition | I | written |
| [#event-driven-dynamics](src/event-driven-dynamics.md) | Formulation | I | written |
| [#recursive-update](src/recursive-update.md) | Derived | I | written |
| [#action-selection](src/action-selection.md) | Derived | I | written |
| [#mismatch-signal](src/mismatch-signal.md) | Definition | I | written |
| [#mismatch-decomposition](src/mismatch-decomposition.md) | Theorem | I | written |
| [#update-gain](src/update-gain.md) | Empirical | I | written |
| [#causal-information-yield](src/causal-information-yield.md) | Definition | I | written |
| [#adaptive-tempo](src/adaptive-tempo.md) | Definition | I | written |
| [#mismatch-dynamics](src/mismatch-dynamics.md) | Hypothesis | I | written |
| [#deliberation-cost](src/deliberation-cost.md) | Derived | I | written |
| [#persistence-condition](src/persistence-condition.md) | Theorem | I | written |
| [#sector-condition-stability](src/sector-condition-stability.md) | Theorem | I | written |
| [#structural-adaptation-necessity](src/structural-adaptation-necessity.md) | Theorem | I | written |
| [#temporal-nesting](src/temporal-nesting.md) | Derived | I | written |
| [#agent-identity](src/agent-identity.md) | Discussion | I | written |
| [#agent-spectrum](src/agent-spectrum.md) | Definition | II | written |
| [#complete-agent-state](src/complete-agent-state.md) | Formulation | II | — |
| [#objective-functional](src/objective-functional.md) | Definition | II | — |
| [#value-object](src/value-object.md) | Definition | II | — |
| [#strategy-dimension](src/strategy-dimension.md) | Definition | II | — |
| [#causal-hierarchy-requirement](src/causal-hierarchy-requirement.md) | Derived + Scope | II | — |
| [#loop-interventional-access](src/loop-interventional-access.md) | Derived | II | — |
| [#explicit-strategy-condition](src/explicit-strategy-condition.md) | Normative | II | — |
| [#chain-confidence-decay](src/chain-confidence-decay.md) | Derived | II | — |
| [#and-or-scope](src/and-or-scope.md) | Scope | II | — |
| [#strategy-dag](src/strategy-dag.md) | Definition | II | — |
| [#directed-separation](src/directed-separation.md) | Derived + Scope | II | — |
| [#satisfaction-gap](src/satisfaction-gap.md) | Definition | II | — |
| [#control-regret](src/control-regret.md) | Definition | II | — |
| [#strategic-calibration](src/strategic-calibration.md) | Definition | II | — |
| [#orient-cascade](src/orient-cascade.md) | Derived | II | — |
| [#observability-dominance](src/observability-dominance.md) | Derived | II | — |
| [#edge-update-via-gain](src/edge-update-via-gain.md) | Hypothesis | II | — |
| [#structural-change-as-parametric-limit](src/structural-change-as-parametric-limit.md) | Formulation | II | — |
| [#strategy-persistence-schema](src/strategy-persistence-schema.md) | Proposed schema | II | — |
| [#multi-agent-scope](src/multi-agent-scope.md) | Scope | III | — |
| [#unity-dimensions](src/unity-dimensions.md) | Definition (sketch) | III | — |
| [#shared-intent](src/shared-intent.md) | Definition + Discussion | III | — |
| [#auftragstaktik-principle](src/auftragstaktik-principle.md) | Hypothesis | III | — |
| [#tempo-composition](src/tempo-composition.md) | Derived (sketch) | III | — |
| [#team-persistence](src/team-persistence.md) | Derived (sketch) | III | — |
| [#adversarial-tempo-advantage](src/adversarial-tempo-advantage.md) | Theorem | III | — |
| [#adversarial-destabilization](src/adversarial-destabilization.md) | Derived | III | — |
| [#adversarial-exponent-regimes](src/adversarial-exponent-regimes.md) | Observation | III | — |
| [#observation-gates-advantage](src/observation-gates-advantage.md) | Observation | III | — |
| [#per-dimension-persistence](src/per-dimension-persistence.md) | Theorem | III | — |
| [#software-scope](src/software-scope.md) | Scope | IV | — |
| [#software-epistemic-properties](src/software-epistemic-properties.md) | Observation | IV | — |
| [#feature-definition](src/feature-definition.md) | Definition | IV | — |
| [#specification-bound](src/specification-bound.md) | Theorem | IV | written |
| [#communication-as-bottleneck](src/communication-as-bottleneck.md) | Corollary | IV | — |
| [#change-expectation-baseline](src/change-expectation-baseline.md) | Theorem | IV | — |
| [#investment-scaling](src/investment-scaling.md) | Corollary | IV | — |
| [#developer-as-act-agent](src/developer-as-act-agent.md) | Definition | IV | — |
| [#comprehension-time](src/comprehension-time.md) | Definition | IV | — |
| [#implementation-time](src/implementation-time.md) | Definition | IV | — |
| [#dual-optimization](src/dual-optimization.md) | Derived | IV | — |
| [#change-investment](src/change-investment.md) | Derived | IV | — |
| [#code-quality-as-observation-infrastructure](src/code-quality-as-observation-infrastructure.md) | Discussion + Hypothesis | IV | — |
| [#conceptual-alignment](src/conceptual-alignment.md) | Hypothesis | IV | — |
| [#realignment-as-feature](src/realignment-as-feature.md) | Corollary | IV | — |
| [#atomic-changeset](src/atomic-changeset.md) | Definition | IV | — |
| [#changeset-size-principle](src/changeset-size-principle.md) | Empirical | IV | — |
| [#comprehension-follows-changeset](src/comprehension-follows-changeset.md) | Corollary + Hypothesis | IV | — |
| [#change-distance](src/change-distance.md) | Definition | IV | — |
| [#change-proximity-principle](src/change-proximity-principle.md) | Derived + Hypothesis | IV | — |
| [#exponential-cognitive-load](src/exponential-cognitive-load.md) | Hypothesis | IV | — |
| [#system-coupling](src/system-coupling.md) | Definition | IV | — |
| [#system-coherence](src/system-coherence.md) | Definition | IV | — |
| [#coherence-coupling-measurement](src/coherence-coupling-measurement.md) | Measurement | IV | — |
| [#principled-decision-integration](src/principled-decision-integration.md) | Integration | IV | — |
| [#system-availability](src/system-availability.md) | Definition | IV | — |
| [#continuous-operation](src/continuous-operation.md) | Scope Extension | IV | — |
| [#causal-discovery-from-git](src/causal-discovery-from-git.md) | Hypothesis | IV | — |
| [#ai-agent-as-act-agent](src/ai-agent-as-act-agent.md) | Definition | V | — |
| [#context-turnover](src/context-turnover.md) | Observation | V | — |
| [#m-preservation](src/m-preservation.md) | Discussion | V | — |

---

## I. Adaptive Systems Under Uncertainty

*Scope: Any system consisting of an agent coupled to an environment through observation and action channels, where the environment is not fully observable. This is the general case — thermostats through commanders. The claims in this section are largely drawn from TFT (TF-01 through TF-11, Appendix A), which developed the adaptive-systems foundation that ACT subsumes.*

**[#temporal-optimality](src/temporal-optimality.md)** — Axiom
Among agents achieving identical outcomes across all non-temporal dimensions, the one requiring least time is optimal. *(Generalizes TST T-01 beyond software.)*

**[#agent-environment](src/agent-environment.md)** — Definition
An agent receives observations from an environment, maintains internal state, and produces actions that affect the environment. The agent cannot access the environment directly — observations are necessarily lossy. This is constitutive: the theory applies where the agent-environment boundary entails information loss. *(From TF-01.)*

**[#observation-function](src/observation-function.md)** — Definition
Observations are lossy, possibly noisy functions of environment state: $o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$. The agent knows neither $h$ nor the noise distribution exactly. *(From TF-01.)*

**[#action-transition](src/action-transition.md)** — Definition
Actions affect environment: $\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$. The transition function $T$ is unknown to the agent and possibly stochastic. *(From TF-01.)*

**[#scope-condition](src/scope-condition.md)** — Scope
ACT applies where: observations exist, the agent has at least binary choice ($|\mathcal{A}| \geq 2$, the minimum for interventional contrast and causal learning), and residual uncertainty persists: $H(\Omega_t \mid \mathcal{C}_t) \gt 0$. *(From TF-01.)*

**[#composition-consistency](src/composition-consistency.md)** — Axiom
Any system satisfying the scope condition may be composed of subsystems that themselves satisfy the scope condition. ACT's predictions at the composite level must be compatible with the aggregate of sub-level predictions plus coordination structure. The scope condition does not restrict level of description — the theory applies at every level where it applies at all. This means composition laws for tempo, persistence, gain, and mismatch are *required* for internal consistency, not optional extensions. *(From composition spike. The consistency argument is strong; specific composition laws are sketches; the requirement for their existence is near-derived.)*

**[#causal-structure](src/causal-structure.md)** — Axiom
The agent-environment interaction has irreducible causal structure. Temporal ordering is constitutive, not incidental. The interaction creates a causal DAG from which associations, interventions, and counterfactuals derive. *(From TF-02, grounded in Pearl.)*

**[#pearl-causal-hierarchy](src/pearl-causal-hierarchy.md)** — Definition
Three levels of causal reasoning: Level 1 (association — "what if I observe?"), Level 2 (intervention — "what if I do?"), Level 3 (counterfactual — "what if I had done differently?"). The binary action requirement ( #scope-condition) ensures Level 2 access. *(From TF-02.)*

**[#chronica](src/chronica.md)** — Definition
The interaction history $\mathcal{C}_t = (o_1, a_1, \ldots, o_t)$ is the complete record of agent-environment interaction. All the agent can ever know derives from this sequence. *(From TF-02.)*

**[#agent-model](src/agent-model.md)** — Formulation
$M_t = \phi(\mathcal{C}_t)$: the agent's compressed representation of how the world works, mapping interaction history to model space $\mathcal{M}$. This is a formulation choice — we commit to analyzing the agent as having a complete state $M_t$ that subsumes all retained information from its history. *(From TF-03.)*

**[#information-bottleneck](src/information-bottleneck.md)** — Formulation
Optimal model compression balances retained history against predictive power: $\phi^* = \operatorname{argmin}[I(M_t; \mathcal{C}_t) - \beta \cdot I(M_t; o_{t+1:\infty} \mid a_{t:\infty})]$. The trade-off $\beta$ depends on environment volatility $\rho$: volatile $\to$ aggressive compression; stable $\to$ dense retention. *(From TF-03.)*

**[#model-sufficiency](src/model-sufficiency.md)** — Definition
$S(M_t)$ measures what fraction of predictive information the model retains relative to the full history. $S = 1$ means $M_t$ is a sufficient statistic. $S \lt 1$ means predictive information has been lost. *(From TF-03/TF-10.)*

**[#model-class-fitness](src/model-class-fitness.md)** — Definition
$\mathcal{F}(\mathcal{M}) = \sup_{M \in \mathcal{M}} S(M)$. When $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$, no model in the current class can adequately represent reality, regardless of parameter tuning. This is the trigger for structural change ( #structural-adaptation-necessity). *(From TF-10.)*

**[#event-driven-dynamics](src/event-driven-dynamics.md)** — Formulation
The primary formulation is event-driven: observations and actions occur as events in continuous time at potentially different and variable rates. Discrete-time notation is the special case of uniform-interval events on a single channel. *(From TF-04.)*

**[#recursive-update](src/recursive-update.md)** — Derived
Agent state updates must be recursive: $M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$. Between events, the model evolves autonomously: $dM/d\tau = g_M(M_\tau)$. The agent cannot re-derive $M_t$ from scratch at each event — this is computational necessity for finite agents, and architectural choice for others. *(From TF-04.)*

**[#action-selection](src/action-selection.md)** — Derived
Action is a function of the model: $a_t = \pi(M_t)$. The model's role is not merely to represent the environment but to generate actions — either implicitly (from internalized patterns) or through explicit deliberation. The degree to which effective action flows from the model without deliberative computation is *action fluency*. *(From TF-07.)*

**[#mismatch-signal](src/mismatch-signal.md)** — Definition
$\delta_t = o_t - \hat{o}_t$: the discrepancy between observation and prediction. This is the fundamental error signal that drives all adaptation. Zero mismatch can mean accurate model, confirmation bias, or high observation noise masking miscomprehension. *(From TF-05.)*

**[#mismatch-decomposition](src/mismatch-decomposition.md)** — Theorem
$\mathbb{E}[\|\delta\|^2] = \mathbb{E}[\|\text{model\_error}\|^2] + \mathbb{E}[\|\text{obs\_noise}\|^2]$. Mismatch decomposes into reducible model error (improvable by learning) and irreducible observation noise (a property of the channel). Prop 5.1, proven. *(From TF-05.)*

**[#update-gain](src/update-gain.md)** — Empirical Claim
$\eta^* = U_M / (U_M + U_o)$: the optimal update weight balances model uncertainty against observation uncertainty. High model uncertainty $\to$ trust observations. Low model uncertainty $\to$ trust the model. Riccati-optimal gain validated empirically with 52% mismatch reduction. *(From TF-06.)*

**[#causal-information-yield](src/causal-information-yield.md)** — Definition
Actions generate information about causal structure that passive observation cannot provide. Causal information yield: $\text{CIY}(a; M) = \mathbb{E}_{a'}[D_{\text{KL}}(P(o \mid do(a), M) \| P(o \mid do(a'), M))]$. $\text{CIY} = 0$ for passive observers; $\text{CIY} \gt 0$ when actions causally alter observations — distinguishing Level 2 from Level 1 epistemic access ( #pearl-causal-hierarchy). The unified policy objective combines exploitation and exploration weighted by $\lambda(M_t)$. *(From TF-08.)*

**[#adaptive-tempo](src/adaptive-tempo.md)** — Definition
$\mathcal{T} = \sum \nu^{(k)} \cdot \eta^{*(k)}$: adaptive tempo is the sum across observation channels of event rate $\times$ gain. This measures the agent's total rate of useful information acquisition. *(From TF-06/TF-08.)*

**[#mismatch-dynamics](src/mismatch-dynamics.md)** — Hypothesis
$d\|\delta\|/dt = -\mathcal{T} \cdot \|\delta\| + \rho(t)$: mismatch evolves as the balance between corrective capacity (tempo) and environmental change rate. Steady state: $\|\delta\|_{ss} = \rho/\mathcal{T}$. This linear ODE is a first-order approximation; the general nonlinear case is handled by the sector-condition framework ( #sector-condition-stability). *(Named hypothesis; pedagogically valuable but not the primary stability result. From TF-11.)*

**[#deliberation-cost](src/deliberation-cost.md)** — Derived
Deliberation improves action quality but takes time during which the environment evolves. Deliberation is justified when improvement exceeds mismatch accumulated during the pause: $\Delta\eta^*(\Delta\tau) \cdot \|\delta_{\text{post}}\| \gt \rho_{\text{delib}} \cdot \Delta\tau$. Optimal deliberation depth increases with decision stakes and model quality, decreases with environment volatility and tempo. *(From TF-09.)*

**[#persistence-condition](src/persistence-condition.md)** — Theorem
The agent maintains bounded mismatch (persists) iff $\mathcal{T} \gt \rho / \|\delta_{\text{critical}}\|$, where $\rho$ is the rate of environment change and $\delta_{\text{critical}}$ is the maximum tolerable mismatch. Robust across all correction functions tested. *(From TF-07, Appendix A.)*

**[#sector-condition-stability](src/sector-condition-stability.md)** — Theorem
The general nonlinear persistence result: the correction function must satisfy sector bounds with $\alpha \gt \rho/R$. This is the Lyapunov/sector-condition framework — more general than the linear ODE, handles arbitrary nonlinear correction functions. Includes adaptive reserve $\Delta\rho^* = \alpha R - \rho$. The linear ODE is a pedagogical special case. *(From Appendix A, promoted to primary.)*

**[#structural-adaptation-necessity](src/structural-adaptation-necessity.md)** — Theorem
When model class fitness $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$, no parametric update closes the mismatch floor. The agent must change its model class (structural adaptation), not just its parameters. Catastrophic breakdown observed at predicted threshold. Prop 10.1, proven. *(From TF-10.)*

**[#temporal-nesting](src/temporal-nesting.md)** — Derived
An agent's adaptive processes stratify by timescale: $\nu_{\text{level } n+1} \ll \nu_{\text{level } n}$. Each level operates on the quasi-steady-state output of the level below. Faster processes must approximately converge before slower ones act on their output — otherwise the system oscillates on transient behavior. Standard singular perturbation reasoning (Tikhonov). *(From TF-11.)*

**[#agent-identity](src/agent-identity.md)** — Discussion
An agent's identity within ACT is grounded not in the model state $M_t$ (which can be copied) but in the unique causal trajectory $\mathcal{C}_t$ (which cannot). Duplicating $M_t$ creates two agents with divergent causal histories — neither is a sufficient statistic for the other's trajectory. Discussion-grade; no downstream formal result depends on this. *(From TF Appendix G.)*


---

## II. Actuated Adaptive Systems

*Scope narrowing: agents that not only track reality but aim at something. This adds objectives and strategy alongside the reality model. The adaptive machinery from Section I carries over unchanged ( #directed-separation) — what we add is the goal-directed layer.*

*The derivation chain for this section is mature (see `scratch/spike-v3-purposeful-agent.md`). Most of it provides better justification and epistemic labels for architecture that already existed. The genuinely novel results are: the satisfaction gap / control regret split ( #satisfaction-gap, #control-regret), the $G_t$ complexity bound (in #orient-cascade), and the graph structure uniqueness argument (see `scratch/spike-graph-uniqueness.md`).*

*"If a man knows not to which port he sails, no wind is favorable." — Seneca*

**[#agent-spectrum](src/agent-spectrum.md)** — Definition
Two independent dimensions create an agent spectrum: $\{\pm\text{model}\} \times \{\pm\text{objective}\}$. Four quadrants: reactive system (thermostat), adaptive tracker (Kalman filter), blind pursuer (PID controller), actuated agent (commander, developer, AI agent). These are regions of a continuum, not discrete categories.

**[#complete-agent-state](src/complete-agent-state.md)** — Formulation
$X_t = (M_t, G_t)$: the complete agent state lifts $M_t$ from "the" state (as in TFT) to the epistemic substate, adding $G_t$ (the purposeful substate — what the agent wants and how it plans to get it). Section I is the special case $X_t = (M_t, \emptyset)$. Update dynamics: $f_M$ has no $G_t$ argument; $f_G$ references $M_{\tau^+}$; policy couples all three. *(From v3 spike.)*

**[#objective-functional](src/objective-functional.md)** — Definition
$O_t$ parametrizes TF-08's "value" term: given objective $O_t$, the induced value functional $V_{O_t}$: trajectories $\to \mathbb{R}$ measures how well a trajectory satisfies the objective. $O_t$ can be a point target, region, constraint set, utility, or trajectory functional — all unified through $V_{O_t}$. The trajectory functional is the most general form; the others are special cases. *(From v3 spike.)*

**[#value-object](src/value-object.md)** — Definition
$V_O(M_t, \pi; N_h)$ and $Q_O(M_t, a; \pi_{\text{cont}}, N_h)$: horizon- and policy-conditioned value objects. Continuation policy $\pi_{\text{cont}}$ is a parameter, not derived. Common choices: one-step improvement (natural default), Bellman fixed point, receding horizon. $\lambda$ depends on $(M_t, O_t, N_h)$ — exploration price depends on objective and horizon, not just epistemic state. *(From v3 spike.)*

**[#strategy-dimension](src/strategy-dimension.md)** — Definition
$G_t = (O_t, \Sigma_t)$: the purposeful substate decomposes into objective (evaluation criterion — "is this trajectory satisfactory?") and strategy (action guidance — "which action sequence produces a satisfactory trajectory?"). This is a definitional split reflecting different kinds of information, not a dynamic or timescale claim. Strategy representations range from none (reactive), through cached policies, subgoal sequences, to full causal DAGs. *(From v3 spike.)*

**[#causal-hierarchy-requirement](src/causal-hierarchy-requirement.md)** — Derived + Scope
Evaluating $Q_O(M_t, a; \cdot)$ is a Level 2 query ("what happens if I *do* $a$?"). The causal hierarchy theorem (Bareinboim et al. 2022) proves Level 2 knowledge requires causal structure beyond predictive models. *Scope narrowing*: we restrict to agents that must acquire or refine Level 2 knowledge during operation, as opposed to pre-compiled controllers (PID, LQR) where the designer supplied it. *(From v3 spike.)*

**[#loop-interventional-access](src/loop-interventional-access.md)** — Derived
An agent in the feedback loop generates interventional data: $a_t$ causally precedes $o_{t+1}$, so the mismatch $\delta_t$ conditioned on $a_t$ carries interventional information. The loop provides *access* to Level 2 data; whether the agent *exploits* it depends on its update mechanism and model class. LLM training data provides causal priors (noisy, mixed provenance); the loop verifies. *(From TF-02 + temporal ordering; v3 spike.)*

**[#explicit-strategy-condition](src/explicit-strategy-condition.md)** — Normative
An agent benefits from explicit $\Sigma_t$ when $C_{\text{plan}} + C_{\text{maintain}} \lt C_{\text{explore}} + C_{\text{repair}}$. Labeled *normative*, not *derived*, because #temporal-optimality requires identical non-temporal outcomes as a precondition — loop-based and model-based approaches may differ in final value, risk, and model bias. When the precondition holds, this makes #temporal-optimality load-bearing for the purposeful layer. *(From v3 spike.)*

**[#chain-confidence-decay](src/chain-confidence-decay.md)** — Derived
$\log P(\text{chain}) = \sum \log P(E_i \mid E_{\lt i})$: chain confidence decays monotonically with depth. The robust result is additive log-confidence, not the special case $p^n$ (which assumes independence and uniformity). Longer chains are structurally less confident, creating pressure toward short plans, parallel fallback paths, high-confidence critical links, and early failure monitoring. *(From v3 spike. Generalizes the earlier compound-probability-decay result.)*

**[#and-or-scope](src/and-or-scope.md)** — Scope
We restrict to environments where causal combination is approximately conjunctive (AND) or disjunctive (OR), without strong interaction effects. Converged across three independent formalism attempts. The excluded case (complementarity, substitutability, interaction effects) requires richer combination rules — a legitimate divergence point for future work. *(From v3 spike.)*

**[#strategy-dag](src/strategy-dag.md)** — Definition
Post-narrowing: the agent's strategy $\Sigma_t = (V, E, p, \gamma)$ is a probabilistic causal DAG. Nodes are propositions; edges carry confidence weights $p \in [0,1]$; combination rules $\gamma(v) \in \{\text{AND}, \text{OR}\}$. *Graph structure is strongly motivated*: temporal ordering $\to$ directed edges (proved), Cox's theorem $\to$ probabilistic uncertainty (proved), local revisability $\to$ Markov factorization (sketch — needs tightening), finite horizon $\to$ acyclicity (derived, resolves a former known fragility). The AND/OR parameterization is a formulation choice within the forced graph structure, motivated by Boolean completeness + parsimony under bounded cognition. *(From intent-dag-consolidated + graph uniqueness spike.)*

**[#directed-separation](src/directed-separation.md)** — Derived + Scope
$f_M$ has no $G_t$ argument; $f_G$ references $M_{\tau^+}$. The epistemic update is goal-blind *conditional on the realized event*. The policy couples all substates through action selection. *Scope condition*: this requires that goals influence event *selection* (through action) but not event *processing*. Many agents (including LLMs with goal-conditioned prompts) violate this to some degree. The approximation is better when goal-conditioning affects attention more than interpretation, and worse when the agent exhibits confirmation bias. A future extension: coupled $M_t$/$G_t$ dynamics formalizing motivated reasoning. *(From v3 spike.)*

**[#satisfaction-gap](src/satisfaction-gap.md)** — Definition
$\delta_{\text{sat}} = V_{O_t}^{\min} - A_O(M_t; \Pi, N_h)$: the gap between the minimum acceptable value and the best achievable under current model, policy class, and horizon. $\delta_{\text{sat}} \gt 0$ means the objective is unmet, but this does NOT automatically mean the goal is wrong — it may indicate narrow $\Pi$, short $N_h$, or incorrect $M_t$. The revised cascade checks $M_t$, $\Pi$, $N_h$ adequacy *before* revising $O_t$. Objective revision is last resort. *(From v3 spike. Replaces the simpler "$\delta_{\text{objective}}$" from earlier formulations.)*

**[#control-regret](src/control-regret.md)** — Definition
$\delta_{\text{regret}} = A_O(M_t; \Pi, N_h) - V_O(M_t, \pi_{\text{current}}; N_h) \geq 0$: the gap between best achievable and current performance. This is the signal for $\Sigma_t$ revision. *Diagnostic*: large $\delta_{\text{sat}}$ + small $\delta_{\text{regret}}$ = doing the best possible but goal may be infeasible $\to$ check $M_t$/$\Pi$/$N_h$ then consider revising $O_t$. Large $\delta_{\text{sat}}$ + large $\delta_{\text{regret}}$ = bad strategy $\to$ revise $\Sigma_t$ first. *(From v3 spike.)*

**[#strategic-calibration](src/strategic-calibration.md)** — Definition
Edge residuals $r_{ij}$: predicted $\Delta V_O$ $-$ observed $\Delta V_O$ per edge traversal. $\delta_{\text{strategic}} = (\sum w_{ij} \cdot r_{ij}^2)^{1/2}$, aggregated across active edges with criticality weighting. This is a second-order inference — inherently slower to evaluate than $\delta_{\text{epistemic}}$, requires accumulating evidence over multiple edge traversals. Connects to #strategy-persistence-schema as the candidate strategic mismatch state. *(From v3 spike.)*

**[#orient-cascade](src/orient-cascade.md)** — Derived
Resolution ordering forced by information dependency: (1) reduce $\delta_{\text{epistemic}}$ (prerequisite — $M_t$ appears in every subsequent formula), (2) evaluate $\delta_{\text{sat}}$ (requires adequate $M_t$), (3) evaluate $\delta_{\text{regret}}$ (requires adequate $M_t$ + meaningful $A_O$), (4) evaluate $\delta_{\text{strategic}}$ (requires feasible $O_t$ + evidence of suboptimal execution), (5) revise $O_t$ (last resort, after $\Sigma_t$ revisions exhaust). *$G_t$ evaluable complexity bounded by $M_t$ capacity*: an agent with poor $S(M_t)$ cannot meaningfully evaluate a complex $\Sigma_t$. This creates virtuous/vicious cycles at the purposeful level. *(From v3 spike.)*

**[#observability-dominance](src/observability-dominance.md)** — Derived
Unobservable edges freeze beliefs — the agent cannot update confidence on what it cannot see. Strategy effectiveness is gated by which edges the agent can observe. Observability enables strategy; its absence disables it, regardless of the strategy's structural quality.

**[#edge-update-via-gain](src/edge-update-via-gain.md)** — Hypothesis
Strategy edges update via the same uncertainty ratio principle: $\eta_{\text{edge}} = U_{\text{edge}} / (U_{\text{edge}} + U_{\text{obs}})$. TFT's gain machinery ( #update-gain) extends to strategy revision. *Parallel to $M_t$ gain but not independently validated.*

**[#structural-change-as-parametric-limit](src/structural-change-as-parametric-limit.md)** — Formulation
In the probabilistic DAG, pruning (edge $\to$ 0) and grafting ($0 \to$ edge) are continuous operations on edge weights, not discrete structural events. TF-10's destruction-creation cycle is the rare limiting case.

**[#strategy-persistence-schema](src/strategy-persistence-schema.md)** — Proposed schema
If strategic update dynamics satisfy sector conditions analogous to #sector-condition-stability — (SA1) zero correction at zero strategic mismatch, (SA2') local sector bound on strategic correction, bounded strategic disturbance — then $\Sigma_t$ persists iff $\alpha_\Sigma \gt \rho_\Sigma / R_\Sigma$. Awaiting: formal strategic mismatch state (candidate: #strategic-calibration residual), correction function (edge confidence revision via gain), disturbance characterization (rate at which environment invalidates causal links). *(From v3 spike.)*

### Section II — Gaps

**???** — Gap: *Action-deliberation-exploration tradeoff.* Three-way: exploit (pursue $O_t$ via $\Sigma_t$), explore (improve $M_t$), deliberate (revise $\Sigma_t$). TF-07/08/09 treat explore/exploit for $M_t$; adding $\Sigma_t$ creates a richer tradeoff. Connects to CIY (TF-09) and the exploration price $\lambda$.

**???** — Gap: *Strategy tempo.* The analog of #adaptive-tempo for $\Sigma_t$ updates. What observation channels contribute to strategy revision? How fast must the agent revise $\Sigma_t$ to maintain strategy persistence ( #strategy-persistence-schema)?

**???** — Gap: *Cognitive cost of $\Sigma_t$.* The IB analog for strategy maintenance: a 500-node DAG is qualitatively different from a 12-node one. For finite-context agents, the DAG must fit in working memory. Connects to #information-bottleneck, shared intent compression ( #shared-intent), and the cost inequality ( #explicit-strategy-condition).

**???** — Gap: *Edge identifiability.* Edges claim interventional semantics ($p_{ij} = P(j \mid do(i), M_t)$) but update from observational signals. In confounded domains (military, organizational), this is a real causal-identification problem. In software, genuine interventions (tests, deploys, git bisect) are available. Resolution may come from the software domain pushing requirements back up.


---

## III. Composition and Coordination

*Scope: multiple agents interacting through a shared environment, or equivalently, the internal structure of composite agents. The composition axiom ( #composition-consistency) ensures the theory applies at every level of description; this section develops what happens when composition is imperfect and what the dynamics of inter-agent interaction look like.*

*Correlated observations as default; independence as the special case requiring justification. Adversarial dynamics are one end of a teleological unity spectrum, not a separate theory.*

*Two sources: the simulation-validated adversarial dynamics from TFT (TF-11/Appendix F, track-b simulations), and the composition spike (`scratch/spike-agent-composition.md`) which derives the requirement for composition consistency from the scope condition's level-independence.*

**[#multi-agent-scope](src/multi-agent-scope.md)** — Scope
Multiple agents interact through shared environment. Each agent has its own $X_t = (M_t, G_t)$ state. Observations may be correlated. Agents may be cooperative, adversarial, or mixed — positions on a continuous spectrum, not discrete categories. A composite agent $A_c$ satisfies the scope condition and can be analyzed as a single agent at a higher level ( #composition-consistency). *(From TF-11/Appendix F, extended by composition spike.)*

**[#unity-dimensions](src/unity-dimensions.md)** — Definition (sketch)
Four substantially independent dimensions characterize a composite agent's internal coherence: epistemic unity $U_M$ (shared model), teleological unity $U_O$ (shared objective), strategic unity $U_\Sigma$ (coordinated action), perceptual unity $U_{\text{obs}}$ (shared observation). These map to Clausewitz's three gaps (Bungay): knowledge gap $\leftrightarrow$ $1 - U_M$, alignment gap $\leftrightarrow$ $1 - U_O$, effects gap $\leftrightarrow$ $(1 - U_\Sigma)(1 - U_{\text{obs}})$. *(From composition spike. Unity metrics are discussion-grade; Clausewitz mapping is hypothesis.)*

**[#shared-intent](src/shared-intent.md)** — Definition + Discussion (sketch)
IB-compressed purpose communicated between agents for coordinated action. The Auftragstaktik insight: communicate *enough* intent to enable local adaptation, not so much that you constrain it. The information bottleneck principle ( #information-bottleneck) applied to inter-agent purpose rather than intra-agent compression.

**[#auftragstaktik-principle](src/auftragstaktik-principle.md)** — Hypothesis
Optimal allocation of communication bandwidth across unity dimensions prioritizes teleological unity ($B_O$) over strategic coordination ($B_\Sigma$) over model sharing ($B_M$). The IB framework predicts this when objectives change slowly, strategies moderately, and models fast. *(From composition spike, grounded in Bungay's analysis of military history.)*

**[#tempo-composition](src/tempo-composition.md)** — Derived (sketch)
Under perfect communication and independent channels, tempos add: $\mathcal{T}_c = \sum \mathcal{T}_i$. With overlapping channels, diminishing returns. Communication overhead subtracts: $\mathcal{T}_c = \sum \mathcal{T}_i^{\text{local}} + \sum \mathcal{T}_{i \to j}^{\text{shared}} - C_{\text{coord}}$. The composition gap $\Delta\mathcal{T} = \sum \mathcal{T}_i - \mathcal{T}_c \geq 0$ measures the cost of being multiple. *(From composition spike.)*

**[#team-persistence](src/team-persistence.md)** — Derived (sketch)
A team of sub-agents, each below individual persistence threshold, persists as a composite when $\sum \mathcal{T}_i - C_{\text{coord}} \gt \rho_c / \|\delta_{\text{critical}}^c\|$. Coordination overhead $C_{\text{coord}}$ directly subtracts from composite persistence margin — a team with high individual tempos but terrible coordination can fall below the threshold. *(From composition spike.)*

**[#adversarial-tempo-advantage](src/adversarial-tempo-advantage.md)** — Theorem
Tempo advantage is superlinear: the ratio of adversarial mismatch scales as $(\mathcal{T}_A/\mathcal{T}_B)^\alpha$ where $\alpha \gt 1$ in all coupling-dominant regimes. Faster adaptation doesn't just help linearly — it compounds. This is the formal grounding of Boyd's OODA loop insight. *(From TF-11, validated across 6 simulation variants.)*

**[#adversarial-destabilization](src/adversarial-destabilization.md)** — Derived
If adversary $A$ injects disturbance into agent $B$'s environment ($\rho_B = \rho_{B,\text{base}} + \gamma_A \cdot \mathcal{T}_A$), $A$ destabilizes $B$ when $\gamma_A \cdot \mathcal{T}_A \gt \Delta\rho^*_B$ (adaptive reserve, #sector-condition-stability). Formally defines "getting inside the opponent's loop" as Lyapunov instability. Once $B$ exceeds its invariant region, erratic actions increase $A$'s coupling effectiveness in a positive-feedback loop. *(Derived from sector-condition analysis applied to adversarial coupling.)*

**[#adversarial-exponent-regimes](src/adversarial-exponent-regimes.md)** — Observation
The exponent $\alpha$ depends on the disturbance mechanism: $\alpha = 2$ under deterministic drift (coupling-dominant); $\alpha = 3/2$ under stochastic disturbances; $\alpha \approx 1$ when coupling doesn't dominate base noise. The linear ODE is correct in the deterministic regime; the stochastic regime needs separate treatment. *(From simulation variants C/D.)*

**[#observation-gates-advantage](src/observation-gates-advantage.md)** — Observation
Observation noise ($U_o$) collapses adversarial exponent from ${\sim}1.0$ to ${\sim}0.2$. Optimal gain ( #update-gain) partially restores it to ${\sim}0.4$. Formally grounds Boyd's emphasis on Orient quality over raw OODA speed — a fast agent with bad observations loses most of its advantage. *(From simulation variant E.)*

**[#per-dimension-persistence](src/per-dimension-persistence.md)** — Theorem
Scalar tempo is a poor summary for anisotropic systems (72% overestimate in simulation). The per-dimension persistence condition is exact: $\mathcal{T}_k \gt \rho_k / \delta_{\text{critical},k}$ for each dimension $k$. The weak dimension is the bottleneck (84% of total mismatch). Targeted adversarial attack on the weak dimension amplifies advantage by 17%. *(From simulation variant F.)*

### Section III — Gaps

**???** — Gap: *Adversarial DAG targeting.* Which strategy edges are most valuable to attack? Centrality in the DAG, inter-agent coupling edges, edges observable to the adversary. #chain-confidence-decay as a weapon: disrupting one AND-edge in a deep chain collapses the whole path.

**???** — Gap: *Directed separation at the composite level.* If each sub-agent's $f_M$ is $G_t$-independent, is the composite's $f_M^c$ independent of $G_t^c$? Hypothesis: goal-blindness composes, BUT coordination routing may break it — if which observations reach the composite depends on the shared objective, the composite's effective observation function is goal-dependent.

**???** — Gap: *Minimum unity for meaningful composition.* At what point is a "composite agent" a useful fiction vs a genuine entity? Is there a phase transition or continuous degradation? What is the irreducible cost of being multiple (compositional entropy)?


---

## IV. Evolving Software Systems

*Domain instantiation: software development as an ACT domain. This section re-grounds TST (Temporal Software Theory) in ACT's formal machinery — adding the causal mathematics and adaptive dynamics that TST was developed without. Software is not just another domain example; it has unique epistemic properties that make it the ideal testbed for ACT and, recursively, the domain where ACT-grounded agents will operate.*

*The temporal optimality axiom ( #temporal-optimality) now has full backing: tempo advantage ( #adversarial-tempo-advantage), persistence conditions ( #persistence-condition), and gain dynamics ( #update-gain) explain WHY time-optimal development practices work, not just THAT they do.*

**[#software-scope](src/software-scope.md)** — Scope
ACT's software domain applies to systems with non-negligible future change probability: $P(n_{\text{future}} \gt 0) \gt \varepsilon$. For such systems, total lifetime cost dominates initial implementation cost. Stable subsystems with $P(\text{change}) \lt \varepsilon$ operate at "infinite velocity" — consuming zero future time. *(Regrounding TST T-03 in ACT.)*

**[#software-epistemic-properties](src/software-epistemic-properties.md)** — Observation
Software has six unique epistemic properties: (1) fully inspectable environment — partial observability from cognitive bandwidth, not physics; (2) Level 3 counterfactuals executable via git; (3) causal DAG partially explicit — imports, types, dependencies; (4) history perfectly recorded — git as complete chronica; (5) multi-agent through shared versioned artifact; (6) observation channel quality under agent control — code quality IS observation infrastructure.

**[#feature-definition](src/feature-definition.md)** — Definition
A unit of functionality that coherently changes the codebase and/or running system, as perceived by those who requested, implement, or use it. Includes refactoring (alters future implementation time), excludes true no-ops. *(TST D-01.)*

**[#specification-bound](src/specification-bound.md)** — Theorem
$\text{time}_{\min}(F) \geq \text{time}_{\text{specify}}(F, \text{context})$. You cannot implement what you cannot specify. Information-theoretic necessity: Shannon entropy of the feature specification bounds implementation time below, modulated by shared context between specifier and implementer. As AI approaches instant implementation, software engineering becomes specification engineering. *(TST T-02. One of TST's strongest claims.)*

**[#communication-as-bottleneck](src/communication-as-bottleneck.md)** — Corollary
As implementation time approaches the specification bound, communication speed and quality become the limiting factor. *(TST C-02.1.)*

**[#change-expectation-baseline](src/change-expectation-baseline.md)** — Theorem
$\mathbb{E}[n_{\text{future}} \mid n_{\text{past}}] = n_{\text{past}}$. The Bayesian consequence of maximum ignorance (Jeffrey's prior, scale-invariant). Not a heuristic — the mathematical null hypothesis of temporal prediction. Any deviation requires information that justifies it. Creates intellectual accountability for abstraction decisions. *(TST T-04. Genuinely well-grounded.)*

**[#investment-scaling](src/investment-scaling.md)** — Corollary
Abstraction investment should scale with $n_{\text{past}}$. Systems with $n_{\text{past}} \lt 3$ warrant minimal structural investment. *(TST C-04.1.)*

**[#developer-as-act-agent](src/developer-as-act-agent.md)** — Definition
The developer's $M_t$ = codebase understanding (mental model of architecture, dependencies, conventions, state). $O_t$ = task objective. $\Sigma_t$ = implementation strategy (the plan, with AND/OR structure, observable checkpoints, contingency branches).

**[#comprehension-time](src/comprehension-time.md)** — Definition
Time from initial idea to first surviving change. Reading, understanding, discovering hidden dependencies, building and validating mental model. This is the cost of constructing $M_t$ for the relevant portion of the codebase. *(TST D-02.)*

**[#implementation-time](src/implementation-time.md)** — Definition
Time from first change to complete feature. Writing, testing, addressing immediate issues. *(TST D-03.)*

**[#dual-optimization](src/dual-optimization.md)** — Derived
Principled decisions minimize both comprehension time and implementation time for future features. Under high turnover (especially 100% context turnover per AI instance), comprehension cost compounds across every new reader. *(TST T-05, derived from #temporal-optimality + #change-expectation-baseline.)*

**[#change-investment](src/change-investment.md)** — Derived
Accept $X$ extra minutes now to save $Y$ per future change when $X \lt n_{\text{future}} \times Y$. The threshold form is derived from #temporal-optimality + #change-expectation-baseline. *(TST T-06.)*

**[#code-quality-as-observation-infrastructure](src/code-quality-as-observation-infrastructure.md)** — Discussion + Hypothesis
Past actions (writing code) affect future observation quality (reading code). Well-written code has low $U_o$ for future readers; obfuscated code has high $U_o$. This creates a second-order feedback loop: code quality $\to$ $U_o$ $\to$ $\eta^*$ ( #update-gain) $\to$ $\mathcal{T}$ ( #adaptive-tempo) $\to$ slack $\to$ code quality.

**[#conceptual-alignment](src/conceptual-alignment.md)** — Hypothesis
$\text{time}_{\text{comprehension}} \propto 1/\text{alignment}(\text{code}, \text{domain})$. Misalignment (code says "user\_score," domain says "reputation") taxes every future comprehension. Not just naming — module boundaries, relationship structure, abstraction levels. *(TST T-07.)*

**[#realignment-as-feature](src/realignment-as-feature.md)** — Corollary
As domain understanding evolves, realigning code is a principled investment when $T_{\text{align}} \lt n_{\text{future}} \times \Delta t_{\text{comprehension}}$. *(TST C-07.1.)*

**[#atomic-changeset](src/atomic-changeset.md)** — Definition
The diff between codebase states before and after feature implementation, excluding generated artifacts. Crosses architectural boundaries: source, schema, config, tests, infrastructure, documentation. *(TST D-04.)*

**[#changeset-size-principle](src/changeset-size-principle.md)** — Empirical
$\text{time}_{\text{implementation}}(F) \propto |\text{changeset}(F)|$. Nearly tautological (more changes take more time), but reveals that good architecture minimizes FUTURE changeset sizes. *(TST T-08.)*

**[#comprehension-follows-changeset](src/comprehension-follows-changeset.md)** — Corollary + Hypothesis
Understanding a feature that touched 20 files requires comprehending 20 contexts. Double the changeset $\approx$ double the comprehension burden. *(TST C-08.1.)*

**[#change-distance](src/change-distance.md)** — Definition
Distance between changes in a codebase: lexical $\lt$ file $\lt$ module $\lt$ service. *(TST D-05.)*

**[#change-proximity-principle](src/change-proximity-principle.md)** — Derived + Hypothesis
Given identical changeset sizes, closer changes require less implementation time. Explains why modules group co-changing code, layers localize changes, domain boundaries contain related changes. *(TST T-09.)*

**[#exponential-cognitive-load](src/exponential-cognitive-load.md)** — Hypothesis
$\text{time}_{\text{actual}} = \text{time}_{\text{baseline}} \times k^{\text{discontinuities}}$, where $k \gt 1$. If context-switching compounds multiplicatively, even modest $k$ (1.1–1.2) creates substantial differences. Requires empirical validation — the actual relationship may be linear or sub-exponential. *(TST H-09.1.)*

**[#system-coupling](src/system-coupling.md)** — Definition
$\text{coupling}(m_i, m_j) = P(\text{change}(m_j) \mid \text{change}(m_i))$.
*(TST D-06.)*

**[#system-coherence](src/system-coherence.md)** — Definition
$\text{coherence}(m) = \mathbb{E}[\text{proximity}(\text{changes within } m)]$.
*(TST D-07.)*

**[#coherence-coupling-measurement](src/coherence-coupling-measurement.md)** — Measurement
$\text{quality} = \sum\text{coherence} / \sum\text{coupling}$. Computable from git history. Transforms architectural discussions from opinion to empirical observation. *(TST T-10.)*

**[#principled-decision-integration](src/principled-decision-integration.md)** — Integration
$C^* = \operatorname{argmin} \mathbb{E}[T \mid C]$ where expected time integrates across future features, weighting comprehension ( #conceptual-alignment), changeset size ( #changeset-size-principle), and proximity ( #change-proximity-principle). Perfect optimization is impossible (requires knowing all future features), but the framework structures the decision space. *(TST T-11.)*

**[#system-availability](src/system-availability.md)** — Definition
$\text{availability} = \text{MTTF} / (\text{MTTF} + \text{MTTR})$. *(TST D-08.)*

**[#continuous-operation](src/continuous-operation.md)** — Scope Extension
For operational systems: $T_{\text{effective}} = T_{\text{implementation}} + P(\text{failure}) \times T_{\text{recovery}}$. A non-operational system has infinite implementation time from the user's perspective. Fault-tolerant design (accept failure, minimize recovery) can be time-optimal vs defensive programming (prevent failure, complex recovery). *(TST T-12.)*

**[#causal-discovery-from-git](src/causal-discovery-from-git.md)** — Hypothesis
Git provides temporal ordering + interventional data (every commit is an intervention). Proper causal analysis — not just co-change correlation — is possible. Software is in Pearl's Regime A (randomized interventions) for causal discovery. The gap between declared dependencies and empirical causal structure reveals hidden coupling or stable interfaces.

### Section IV — Gaps

**???** — Gap: *Three-part tempo decomposition for software:* $\mathcal{T}_{\text{obs}}$ (compiler, linter, tests) + $\mathcal{T}_{\text{explore}}$ (code reading, navigation) + $\mathcal{T}_{\text{probe}}$ (test runs, staging). Which component is the bottleneck? How does each connect to #code-quality-as-observation-infrastructure?

**???** — Gap: *Software persistence condition: the unmaintainability threshold formalized.* $\mathcal{T}_{\text{team}} \gt \rho_{\text{total}} / \|\delta_{\text{critical}}\|$. When does a codebase cross from maintainable to unmaintainable? What are the observable precursors?


---

## V. Software-Grounded Agentic Systems

*Extending the arc: AI agents operating on code are ACT agents whose domain is software, creating a recursive structure — ACT theory $\to$ software domain $\to$ agents that embody ACT. This is where the 100% context turnover problem, $M_t$ preservation, and the cognitive loop connect the theory back to the systems being built with it.*

**[#ai-agent-as-act-agent](src/ai-agent-as-act-agent.md)** — Definition
An AI coding agent is an actuated adaptive agent with 100% context turnover per session. It inhabits the actuated quadrant ( #agent-spectrum): it has $M_t$ (context window + retrieved memory), $O_t$ (task objective), and $\Sigma_t$ (approach plan).

**[#context-turnover](src/context-turnover.md)** — Observation
$M_t$ resets to near-zero at session start. Not gradual degradation but catastrophic loss. The agent must reconstruct $M_t$ from the environment (codebase, CLAUDE.md, memory files) at each session. This is fundamentally different from human developers who retain $M_t$ across sessions. In composition terms ( #composition-consistency), this is an epistemic unity problem: each session starts with $U_M \approx 0$ relative to previous sessions.

**[#m-preservation](src/m-preservation.md)** — Discussion
External memory (CLAUDE.md, memory directories, well-structured code) converts ephemeral $M_t$ into persistent environmental state. The agent's past actions modify the environment to make future $M_t$ reconstruction faster. This is #code-quality-as-observation-infrastructure applied to agent infrastructure itself.

### Section V — Gaps

**???** — Gap: *Cognitive loop formalization.* The cycle: read environment $\to$ construct $M_t$ $\to$ form/revise $\Sigma_t$ $\to$ select action $\to$ observe result $\to$ update $M_t$. How does this differ from the generic orient cascade ( #orient-cascade)? What's specific to language-based agents?

**???** — Gap: *Evaluation framework.* How do you measure an AI agent's ACT quantities? $M_t$ quality, $\Sigma_t$ quality, tempo. Connects to creche and training design.

**???** — Gap: *Creche concept.* Experiential training environments where agents develop adaptive capacity. What does an ACT-grounded training regime look like?

**???** — Gap: *The recursive completion.* An agent using ACT to guide its own behavior while operating on a codebase that implements ACT. Self-referential but not paradoxical.


---

## Appendices (Evidence & Reference)

*These support specific claims above with detailed evidence, worked examples, or historical development. Like claim segments, appendices are identified by slug, not by position.*

**[#linear-ode-approximation](src/linear-ode-approximation.md)** — Reference
The linear ODE from #mismatch-dynamics: $d\|\delta\|/dt = -\mathcal{T}\|\delta\| + \rho$. Correct for deterministic drift in continuous time. Pedagogically valuable, not the general case. The sector-condition framework ( #sector-condition-stability) is primary.

**[#simulation-results](src/simulation-results.md)** — Evidence
Six simulation variants validating and refining claims from Sections I–III. Variant A/B: deterministic drift confirms $\alpha = 2$. Variant C/D: stochastic gives $\alpha = 3/2$. Variant E: observation noise gates advantage. Variant F: per-dimension persistence exact. *(From track-b-nonlinear-sims.)*

**[#worked-examples](src/worked-examples.md)** — Reference
Kalman filter ($M_t$ only), PID controller ($O_t$ only), LQG ($M_t + O_t$ without explicit $\Sigma_t$), RL agent (full triple), developer (software domain). Source material: old-tf-appendix-c-kalman-example, old-tf-appendix-d-rl-example.

**[#operationalization](src/operationalization.md)** — Reference
Estimation procedures for $U_M$, $U_o$, $\rho$, $\alpha$, $R$, $\|\delta_{\text{critical}}\|$. Decision procedures for $\lambda$ (exploration price), deliberation stopping, structural-switch triggers. Source material: old-tf-appendix-b-operationalization.

**[#intent-dag-development](src/intent-dag-development.md)** — Historical
Three independent formalism attempts converging on AND/OR + single-parameter edges. Documents the convergence testing and what was settled vs open. *(From `scratch/04-intent-dag-consolidated.md`.)*

**[#prior-art-positioning](src/prior-art-positioning.md)** — Reference
Assessment of Hafez (bi-predictability $P$ — complementary diagnostic), IBM 2025 (calls for what ACT provides), BDI (named the parts, no dynamics), active inference (closest competitor, different foundation). *(From `scratch/02-prior-art-assessment.md`, `scratch/prior-tf-novelty-analysis.md`.)*

**[#graph-structure-uniqueness](src/graph-structure-uniqueness.md)** — Research direction
Four axioms strongly motivate DAG structure for strategy representation. Acyclicity is *derived* from temporal ordering over finite planning horizon. P3 $\to$ Markov step is a sketch. AND/OR parameterization follows from Boolean completeness + parsimony. *(From `scratch/spike-graph-uniqueness.md`.)*


