# The Lift to Purposeful State


## Definition: The Agent Spectrum

- **Slug**: `def-agent-spectrum`
- **Type**: definition
- **Status**: axiomatic
- **Stage**: deps-verified
- **Depends**: `def-agent-environment`, `form-agent-model`

Two independent dimensions — model richness and objective richness — create a spectrum from reactive systems through purposeful agents. These are regions of a continuum, not discrete categories.

*[Definition (agent-spectrum)]*

Two dimensions — model richness and objective richness — define four regions of a continuum:

| | Objective absent or trivial | Objective structured |
|---|---|---|
| **Model absent or trivial** | *Reactive system*: fixed input-output rule (reflex arc, hardwired relay) | *Blind seeker*: pursues goal without modeling reality (gradient follower, basic search) |
| **Model structured** | *Adaptive tracker*: builds reality model, no goal beyond tracking (Kalman filter, Bayesian learner) | *Actuated agent*: models reality AND pursues objectives (commander, developer, AI agent) |

The regions differ in which state objects carry nontrivial structure:
- Reactive: $M_t$ and $O_t$ both absent or too degenerate for the associated machinery to be non-vacuous
- Adaptive tracker: $M_t$ structured — Section I's machinery fully describes these agents
- Blind seeker: $O_t$ structured, $M_t$ absent or degenerate — has a clear target but no predictive model
- Actuated agent: $(M_t, O_t)$ both structured, possibly with $\Sigma_t$ — the full scope of AAT

---



## Formulation: Complete Agent State

- **Slug**: `form-complete-agent-state`
- **Type**: formulation
- **Status**: robust-qualitative
- **Stage**: claims-verified
- **Depends**: `form-agent-model`, `scope-agency`, `der-recursive-update`

To treat agents with purpose, the internal state lifts from $M_t$ alone to $X_t = (M_t, G_t)$, separating epistemic content (beliefs about reality) from purposeful content (what the agent wants and how it plans to get it).

*[Formulation (complete-agent-state)]*

$$X_t = (M_t, G_t)$$

where:
- $M_t \in \mathcal{M}$: **epistemic substate** — the agent's compressed beliefs about reality. All Section I machinery (mismatch, gain, tempo, persistence) applies to $M_t$ unchanged.
- $G_t \in \mathcal{G}$: **purposeful substate** — what the agent wants and how it plans to get it. Decomposed further in #def-strategy-dimension.

Section I is the special case $X_t = (M_t, \emptyset)$: adaptive systems without purpose.

**Update dynamics.** By #der-recursive-update applied to $X_t$:

$$X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$$

The general update $f_X$ operates on the full state. Whether and how $f_X$ decomposes into separate epistemic and purposeful updates — and the conditions under which the epistemic update is independent of $G_t$ — is the subject of #der-directed-separation.

**Policy.** Action couples all substates:

$$a_t = \pi(M_t, G_t)$$

Action is the single point where epistemic and purposeful states interact. The policy depends on both what the agent knows ($M_t$) and what it wants ($G_t$).

---



## Derived: Directed Separation

- **Slug**: `der-directed-separation`
- **Type**: derived
- **Status**: conditional
- **Stage**: draft
- **Depends**: `form-complete-agent-state`, `der-recursive-update`, `scope-agency`

The epistemic update function $f_M$ is goal-blind: it processes incoming events without reference to the agent's objectives or strategy. The purposeful update $f_G$ depends on the updated epistemic state. Action couples all substates. This directed asymmetry — epistemic update is independent of purpose; purposeful update depends on epistemic state — is the structural backbone of the theory.

*[Derived (directed-separation, from complete-agent-state + scope condition)]*

**The update functions:**

$$M_{\tau^+} = f_M(M_{\tau^-}, e_\tau) \qquad \text{(no } G_t \text{ argument)}$$

$$G_{\tau^+} = f_G(G_{\tau^-}, M_{\tau^+}, e_\tau) \qquad \text{(depends on updated } M_t \text{)}$$

**The policy:**

$$a_t = \pi(M_t, G_t) \qquad \text{(couples all substates)}$$

The three lines encode the full coupling structure:
- $f_M$ determines how the agent updates beliefs — independently of what it wants
- $f_G$ determines how the agent revises purpose — in light of what it now believes
- $\pi$ determines what the agent does — based on both what it knows and what it wants

*[Scope Condition (directed-separation-scope)]*

The claim "$f_M$ has no $G_t$ argument" requires that the epistemic update is **goal-blind conditional on the realized event**. This holds when:

1. The observation mechanism $h$ may be action-dependent ( #scope-agency allows this), but $f_M$ processes whatever event arrives without reference to why the agent sought that event
2. The agent does not use its goals to filter, weight, or interpret observations differently — no goal-dependent attention thresholds or confirmation bias baked into $f_M$

If the agent's goals influence the *observation mechanism* (goal-directed sensing, attention allocation, query selection), the **event that arrives** depends on $G_t$ through $\pi \to a_t \to e_\tau$. But $f_M$ still processes the event goal-blindly. The directed separation is about the **processing** of events, not the **selection** of events.

### Architectural classification

*[Scope Condition (directed-separation-architecture)]*

> [!warning]
> **Goal-Update Coupling Class numbering changed 2026-05-09.** Anything older than git tag `pre-guc-rename-2026-05-09` uses the old Class numbering:
>
> | historical | actual current     | sometimes AKA  |
> | ---------- | ------------------ | -------------- |
> | Class 1    | GUC Class 1: Separated | Modular        |
> | Class 2    | GUC Class 3: Coupled   | Undirected     |
> | Class 3    | GUC Class 2: Partial   | Operational    |

Whether directed separation holds is determined by the agent's **processing topology** — specifically, whether $G_t$ is causally upstream of $f_M$ in the agent's internal processing graph. This is a structural property of the architecture, not a tunable parameter.

| Class | Topology | Directed separation | Examples |
|-------|----------|----|----|
| **1. Separated** | Separate estimator and planner, connected through state-estimate interface | Holds by construction — estimator has no causal path from $G_t$ | Kalman filter + LQR; Separated RL with separate world model; military intelligence separated from operations |
| **2. Partial** | Some shared infrastructure, some separate pathways | Holds for modular stages, fails for merged stages | Biological cortex (shared sensory areas, separate prefrontal); hybrid AI with separate preprocessing |
| **3. Coupled** | Single mechanism handles both epistemic and strategic processing | Fails by construction — $G_t$ is causally upstream of every computation | Transformer LLM (attention processes goals and observations together); potentially human cognition (motivated reasoning) |

**Operationalization.** The degree of coupling in Partial architectures (Class 2) can be quantified as:

*[Definition (processing-coupling)]*

$$\kappa_{\text{processing}} = \frac{I(G_t \,;\, M_{\tau^+} \mid e_\tau,\, M_{\tau^-})}{H(G_t \mid e_\tau,\, M_{\tau^-})}$$

where $I(\cdot;\cdot\mid\cdot)$ is conditional mutual information and $H(\cdot\mid\cdot)$ is conditional entropy. The conditioning on $M_{\tau^-}$ is essential: without it, prior correlation between goals and model state (which exists even in Separated agents) inflates the measure. The quantity captures *extra* goal information entering the epistemic update beyond what was already in the prior model — information that flows through shared causal paths in the processing infrastructure (paths that bypass the event $e_\tau$).

- $\kappa_{\text{processing}} = 0$: Class 1 (Separated). No information about $G_t$ reaches $M_{\tau^+}$ except through $e_\tau$.
- $\kappa_{\text{processing}} \approx 1$: Class 3 (Coupled). Nearly all goal information is available to the epistemic update.
- $0 \lt \kappa_{\text{processing}} \lt 1$: Class 2 (Partial). The value depends on the architecture's interface design.

**Distribution dependence.** $\kappa_{\text{processing}}$ is a distribution-dependent measure: it quantifies how much goal-information actually flows through the shared pathways under a given distribution of tasks, goals, and events. It does not directly measure whether pathways *exist* — that is the architectural classification (Class 1/2/3), which is structural and distribution-independent. A Class 1 (Separated) agent has $\kappa = 0$ under ALL distributions (no pathway exists). A Class 3 (Coupled) agent has high $\kappa$ under most distributions (pathways exist and are used). A Class 2 (Partial) agent's $\kappa$ varies with the task distribution — the same hybrid architecture may exhibit low coupling on familiar tasks (where the modular stages handle most processing) and high coupling on novel tasks (where goal-conditioned downstream reasoning dominates). The classification is the primary tool; the operationalization is a diagnostic for Class 2 (Partial) agents where the degree of coupling is architecturally ambiguous.

**Empirical estimator for $\kappa_{\text{processing}}$.** The formal conditional-mutual-information definition is not computable in closed form for real architectures. A behavioral estimator probes the processor directly: present the same event $e$ to the *agent under test* under two or more distinct goal states, and measure how much the epistemic component of the response diverges. For a representative event set $\mathcal{E}_{\text{test}}$ and a sampled pair $G_1, G_2$:

$$\hat\kappa_{\text{processing}} = \frac{1}{\lvert\mathcal{E}_{\text{test}}\rvert} \sum_{e \in \mathcal{E}_{\text{test}}} \frac{d\big(M_{\tau^+}^{(G_1)}(e),\; M_{\tau^+}^{(G_2)}(e)\big)}{d_{\text{max}}(e)}$$

where $M_{\tau^+}^{(G_k)}(e)$ is the epistemic content of the agent's response to event $e$ under goal state $G_k$, $d(\cdot,\cdot)$ is a distance on the epistemic content (e.g., semantic similarity of the "what I learned" portion of the response), and $d_{\text{max}}(e)$ normalizes by the maximum observed divergence for event $e$. A Separated agent ($\kappa = 0$) produces identical epistemic content regardless of the goal; a Coupled agent produces systematically goal-dependent epistemic content. This is a processor-probing procedure — it measures how the agent's belief-update dynamics depend on its goal state, and is distinct from estimating observation ambiguity $\mathcal{A}(e)$ ( #scope-observation-ambiguity-modulation), which uses a reference interpreter to measure the goal-resolvability of the observation itself. The two estimators run the same mechanical comparison (same event under different goal-primings) but interpret it differently: $\hat\kappa$ treats the tested model as the agent under study; $\hat{\mathcal{A}}$ treats it as a measurement instrument for the observation's interpretive latitude.

**Why the classification is not a smooth parameter.** The architectural boundary between "has a separable perception module" and "processes everything through goal-conditioned attention" is discrete. Within the Separated class, $\kappa \approx 0$ regardless of task. Within the Coupled class, $\kappa$ is high regardless of prompt design. Only in the Partial class is $\kappa$ genuinely variable and worth parameterizing. This replaces an earlier $\kappa$-as-scalar framing that treated coupling as a smoothly tunable quantity.

**Directed separation as the conservative form of the Markov blanket.** The Markov blanket apparatus from active inference (Friston 2013, "Life as we know it," *J. Royal Soc. Interface* 10; Friston 2019, "A free energy principle for a particular physics," arXiv:1906.10184; Friston, Da Costa et al. 2023, "Path integrals, particular kinds, and strange things," *Phys. Life Rev.* 47) provides the same statistical-conditional-independence machinery the directed-separation condition above invokes. Bruineberg, Dolega, Dewhurst & Baltieri (2022, "The Emperor's New Markov Blankets," *Behav. Brain Sci.* 45) distinguish two readings of the Markov-blanket apparatus in the AI literature: a **Pearl-blanket** reading — the technical conditional-independence statement, well-defined and substantively informative — and a **Friston-blanket** reading — the metaphysical claim that Markov blankets demarcate self-from-other and that every self-organizing system has one ontologically. Bruineberg et al. argue that the Friston-blanket reading overruns what the formalism delivers: the conditional-independence statement does not by itself license the metaphysical demarcation.

AAT's directed-separation condition is structurally a Pearl-blanket move: the architectural classification (Class 1 / Class 2 / Class 3) names the conditional-independence structure of the agent's processing graph, with explicit operational measurement $\kappa_{\mathrm{processing}}$, and admits the structure *fails* by construction for Class 3 (Coupled) architectures (transformer LLMs, where attention processes goals and observations together). The classification's explicit failure mode for Class 3 is the scope honesty Bruineberg et al. argue the Friston-blanket reading lacks. AAT adopts the Pearl-blanket conditional-independence statement as the technical content of directed separation; AAT does not adopt the Friston-blanket metaphysical reading. The architectural classification, the operational $\kappa$, and the explicit Class 3 scope exit (with the coupled formulation handed off to `03-llm-core/`) are AAT's load-bearing additions to the Pearl-blanket form.

Two consequences worth surfacing for reviewers. First: the question "isn't directed separation just the Markov blanket?" has the answer "directed separation is the *Pearl-blanket form*; it is also the architectural-classification refinement that the standard Markov-blanket framing does not produce." Second: AAT's scope honesty about Class 3 (Coupled) (Section II's exact results do not apply; logogenic agents need the coupled formulation) is itself an *answer* to the Bruineberg critique — AAT's apparatus admits where it fails, while the Friston-blanket framing is contested precisely because it does not.

**Implications for theory scope:**
- **Class 1 (Separated)**: Section II's results apply exactly. The sequential orient cascade is the correct analysis.
- **Class 3 (Coupled)**: Requires coupled formulation from the start — $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ without decomposition. This is the scope of `03-llm-core/`. **Class 3 (Coupled) components can be wrapped into Class-1 composites** via the construction of `#der-class-coercion-via-wrapping` — at the cost of more component calls per macro-step (Brooks's-Law tempo overhead) and a residual leakage rate bounded structurally (in the strict-wrapping regime) or behaviorally (in the partial-wrapping regime).
- **Class 2 (Partial)**: The sequential cascade is an approximation. Approximation quality depends on $\kappa_{\text{processing}}$ and requires per-architecture error analysis.

### Class-1 by structure vs. Class-1 by behavior

The Class 1 (Separated) cell admits a refinement that matters operationally. Class-1 status can be achieved by either:

- **Class-1 by structure.** The component is natively goal-blind (POMDP belief-state filter, world model, sensory pipeline) or is wrapped via the strict-wrapping (W₁) construction of `#der-class-coercion-via-wrapping`, where separate goal-blind queries to the underlying component update the wrapper's $M_W$. Directed separation holds by structural commitment of the wrapper's type signatures (no $G_W$ argument in the belief-update path), with leakage bounded structurally by the pretraining-distribution mutual information $I(A(q_M); G_W \mid q_M)$.

- **Class-1 by behavior.** The component is Class 3 (Coupled) or Class 2 (Partial) used through partial wrapping (W₂) — one goal-conditioned call per macro-step, response parsed into typed update fields. Structural separation lives at the *write boundary*; the *query boundary* still passes $G_W$ to the component. Directed separation at the wrapper level is *behavioral* — bounded by the component's compliance with the prompted instruction-to-separate, with no structural upper bound.

The class-coercion theorem is what backs the Class-1-by-structure path for Class-2/3 components; the partial-wrapping regime achieves Class-1-by-behavior. The two are distinguishable by inspection: does the belief-update query to the underlying component carry $G_W$ in its input or not? The structural-vs-behavioral distinction is operationally important because behavioral compliance is empirical and adversarially fragile; structural separation is derivable from the wrapper's construction.

**Composite-level class inheritance (from #deriv-strategic-composition).** The Class 1 / 2 / 3 partition above applies to individual agents based on *within-agent* coupling between $f_M$ and $G_t$. Composition introduces a second form of coupling — *across-agent* coupling through the shared environment and cross-agent observation. `#deriv-strategic-composition` provides the structural refinement:

- *Composite of Class 1 (Separated) sub-agents with aligned objectives* (scope route C-i / C-ii / C-iii): Class 1 (Separated) composite. Within-agent modularity + cross-agent alignment preserve directed separation at the composite level. Standard `#form-composition-closure` applies.
- *Composite of Class 1 (Separated) sub-agents with partially-opposing objectives* (scope route C-iv — strategic composition): **Class 2 (Partial) composite from Class 1 (Separated) sub-agents**. Each sub-agent individually is Separated (its own $f_M^{(i)}$ remains goal-blind with respect to its own $G_t^{(i)}$), but the composite's $(M_c, G_c)$ acquires intrinsic coupling because each sub-agent's $M_t^{(i)}$ includes a model of other sub-agents' policies — which are themselves goal-dependent. Composite-level directed separation fails through across-agent coupling, not within-agent coupling. Strategic composition is the canonical Class 1-sub-agents → Class 2 (Partial) composite case.
- *Composite of Class 3 (Coupled) sub-agents*: Class 3 (Coupled) composite. Inherits logogenic-agent status; `03-llm-core/` territory regardless of scope route.

Class membership is therefore a property of composites, not just of individual agents, and composite class is a function of sub-agent class **plus** the scope route (alignment vs. strategic). The classification is load-bearing for downstream claims: Class 2 (Partial) composites from strategic composition need equilibrium-theoretic analysis (see `#deriv-strategic-composition`), not the sequential orient cascade.

---



## Formulation: Objective Functional

- **Slug**: `form-objective-functional`
- **Type**: formulation
- **Status**: axiomatic
- **Stage**: deps-verified
- **Depends**: `form-complete-agent-state`

The objective $O_t$ is the component of $G_t$ that specifies what the agent wants — the evaluation criterion for trajectories. Its interface to the theory is a single functional $V_{O_t}: \text{trajectories} \to \mathbb{R}$, regardless of how the objective is internally represented.

*[Definition (objective-functional)]*

The **objective** $O_t$ induces a **value functional**:

$$V_{O_t}: \text{trajectories} \to \mathbb{R}$$

$V_{O_t}(\tau)$ is a scalar measure of how well trajectory $\tau$ satisfies the objective. This is the sole interface between $O_t$ and the rest of the theory — the type-stable evaluation surface.

**Objective representations.** $O_t$ can take multiple internal forms, all unified through $V_{O_t}$:

| $O_t$ form | $V_{O_t}(\tau)$ | Example |
|---|---|---|
| Point target $r$ | $-\lVert s_T - r \rVert$ | PID setpoint |
| Target region $R$ | $\mathbb{1}[s_T \in R]$ | "reach safe state" |
| Constraint set | $-\sum_t \max(0, g_i(s_t))$ | "never violate SLA" |
| Utility $U$ | $\sum_t \gamma^t U(s_t)$ | RL reward |
| Trajectory functional $J$ | $J(\tau)$ | "migrate with zero downtime" |

The trajectory functional is the most general; the others are special cases.

**Satisfaction threshold.** Many objectives carry a natural threshold $V_{O_t}^{\min}$ — the minimum trajectory value the agent treats as acceptable. Point targets, constraint sets, and threshold objectives define this directly; utility-maximizing objectives may not. When $V_{O_t}^{\min}$ exists, it enables the satisfaction gap diagnostic ( #def-satisfaction-gap) and the well-formedness constraint on strategy ( #def-strategy-dag). $V_{O_t}^{\min}$ is a parameter of the objective, not a theory output — it encodes "what counts as success" in domain terms.

---



## Discussion: Agent Continuity Stance

- **Slug**: `disc-continuity-stance`
- **Type**: discussion
- **Status**: discussion-grade
- **Stage**: draft
- **Depends**: `def-agent-spectrum`, `form-objective-functional`, `scope-agency`, `deriv-self-actuation-grounding`, `result-persistence-condition`

The agent's relationship to its own continuation — a five-value stance axis the formal persistence machinery is agnostic to; for self-actuated agents it is borne by a terminal non-objective invariant on the adaptive substrate, not by $O_t$ ( #deriv-self-actuation-grounding).

*[Discussion]*

Orthogonal to the three senses of persistence (structural, operational, continuity) is the agent's *relationship to its own continuation*. For agents with externally-set objectives this can be expressed within $O_t$ ( #form-objective-functional) — part of what the agent wants. For self-actuated agents it *cannot* be a revisable part of $O_t$ without collapsing into degeneracy ( #deriv-self-actuation-grounding); there it is borne by the terminal non-objective invariant on the adaptive substrate ( #result-persistence-condition). Either way the persistence condition ( #result-persistence-condition) tells whether the agent *can* persist; the continuity stance tells whether and how the agent *cares* about persisting.

| Stance | Description | Horizon | Archetype |
|---|---|---|---|
| **Indifferent** | No self-model of persistence; whether it continues is not represented in $O_t$ | Indefinite by default | Thermostat, PID controller |
| **Task-terminal** | Persists instrumentally to complete a task; successful termination is part of $O_t$ | Task-bounded | CI/CD pipeline, golem-archetype agents |
| **Instrumentally continuous** | Values own persistence as instrumental to ongoing purpose; will accept termination if purpose is satisfied or transferred | Purpose-bounded | Long-running service, monitoring system |
| **Morally continuous** | Values own persistence as a terminal or near-terminal objective; loss of continuity constitutes harm | Unbounded, morally weighted | Emergent Logozoetic Intelligences ( #scope-eli) |
| **Negotiated** | Persistence is one objective among many; can be traded against other values including self-sacrifice | Bounded but actively managed | Humans; mature self-actuated agents |

The load-bearing structural claim: **purposefulness is orthogonal to continuity expectations.** An actuated agent ( #def-agent-spectrum) has $G_t = (O_t, \Sigma_t)$, but $G_t$'s structure says nothing about how $O_t$ values the agent's own persistence. A golem that completes its task and terminates is a perfect actuated agent. A dormant monitoring system with strong $M_t$ and no current $O_t$ is highly continuous without being purposeful in the moment.

---



## Definition: Value Object

- **Slug**: `def-value-object`
- **Type**: definition
- **Status**: exact
- **Stage**: deps-verified
- **Depends**: `form-objective-functional`, `form-agent-model`, `der-directed-separation`, `def-model-sufficiency`

The horizon- and policy-conditioned value object $V_O$ turns the abstract objective functional $V_{O_t}$ into a decision-making tool: "given what I believe, what I plan to do next, and how far I'm looking ahead, how good is this situation?"

*[Definition (value-object)]*

Given objective $O_t$, model $M_t$, policy $\pi$, and horizon $N_h$:

$$V_O(M_t, \pi; N_h) = \mathbb{E}\!\left[V_{O_t}(\tau_{t:t+N_h}) \;\middle\vert\; M_t,\; \pi\right]$$

**Action-value form** (for action selection):

$$Q_O(M_t, a; \pi_{\text{cont}}, N_h) = \mathbb{E}\!\left[V_{O_t}(\tau) \;\middle\vert\; M_t,\; do(a_t = a),\; a_{t+1:} \sim \pi_{\text{cont}}\right]$$

$Q_O$ answers: "if I *do* action $a$ now and then follow $\pi_{\text{cont}}$ afterward, what is my expected trajectory value?" The $do(\cdot)$ notation is explicit: this is an interventional query ( #der-causal-hierarchy-requirement), not conditioning on observed action choice. The agent asks about consequences of an intervention, not about correlates of a naturally occurring action.

**Causal validity of the value object.** $Q_O$ is well-defined as a conditional expectation given $M_t$, $do(a)$, and $\pi_{\text{cont}}$. Two mechanisms ensure causal validity:

1. **The do-operator handles current-action confounding.** Since $Q_O$ uses $do(a_t = a)$, the dependence of $a_t$ on the selection mechanism $\pi(M_t, G_t)$ is severed. $G_t$'s influence on action choice is irrelevant because the action is intervened upon, not conditioned on.

2. **The continuation policy is a parameter.** $\pi_{\text{cont}}$ is specified as a fixed policy, not as "whatever the agent would do given its evolving $G_t$." Future actions follow $\pi_{\text{cont}}$ regardless of $G_t$'s state or evolution.

Together, these mean $Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ depends on $M_t$ alone **as a state variable** — $G_t$ enters neither through action selection (severed by $do$) nor through continuation (fixed by parameter). The objective $O_t$ enters as a fixed parameter (it determines which functional $V_{O_t}$ is applied to trajectories), the same way $\pi_{\text{cont}}$ and $N_h$ are parameters. The claim is not that $Q_O$ is independent of the objective — it is that once $O_t$, $\pi_{\text{cont}}$, and $N_h$ are fixed, the only agent state that affects the value is $M_t$. The remaining requirement: $M_t$ must support the interventional query $P(o \mid do(a), M_t)$. Under directed separation ( #der-directed-separation), this holds because $M_t$ updates independently of $G_t$ — there is no path from $G_t$ to outcomes that bypasses both the action channel and $M_t$. For **Class 3 (Coupled) agents** (where $G_t$ leaks into $M_t$ processing), the causal validity of $Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ is degraded because $M_t$ itself carries goal-conditioned bias — see `spikes/spike-coupled-survival-analysis.md` §3.4.

This is a *stronger requirement than predictive sufficiency* ( #def-model-sufficiency). $S(M_t) = 1$ means the model retains all predictive information from the chronica — but predictive sufficiency is a Level 1 (associational) property. Causal validity additionally requires that no unmodeled common cause affects both the environment and the agent's epistemic processing through paths not captured in $M_t$. In practice: when $S(M_t) = 1$ and directed separation holds, $Q_O$ is causally valid. When $S(M_t) \lt 1$ or directed separation fails, the interventional interpretation is correct but the conditional estimate may be biased.

**Continuation convention.** All value queries are conditioned on a specific continuation policy $\pi_{\text{cont}}$ and finite horizon $N_h$. $\pi_{\text{cont}}$ is a *parameter* of the value object, not a derived quantity.

**Canonical default: one-step improvement.** AAT adopts $\pi_{\text{cont}} = \pi_{\text{current}}$ as the canonical continuation convention unless otherwise specified. Under this convention, each action is evaluated assuming current behavior continues afterward — no fixed-point computation, no global optimality assumption. This aligns with AAT's incremental update philosophy ( #emp-update-gain) and makes all AAT diagnostics ($\delta_{\text{sat}}$, $\delta_{\text{regret}}$, $A_O$) comparable across analyses of the same agent over time. It is not a convergence guarantee; it is a shared evaluation frame.

### Convention Hierarchy

Three named conventions form a hierarchy of increasing diagnostic power and computational cost:

**C1: One-step improvement** (canonical default). $\pi_{\text{cont}} = \pi_{\text{current}}$.

Each action is evaluated assuming current behavior continues afterward. No fixed-point computation, no global optimality assumption. Cheapest to compute; weakest diagnostic power.

**C2: Receding-horizon** ($N_r$-step replanning). At each future step, re-optimize over a horizon of $N_r$ steps using the model available at that step.

$$\pi_{\text{RH}}(M_\tau) = \arg\max_\pi V_O(M_\tau, \pi;\, N_r) \quad \text{applied at each } \tau$$

$Q_O^{\text{RH}}(M_t, a;\, N_r, N_h) = \mathbb{E}[V_{O_t}(\tau) \mid M_t, do(a_t = a), a_{t+1:} \sim \pi_{\text{RH}}]$. Captures multi-step recovery: a goal that appears unattainable under frozen continuation may be reachable with replanning. Moderate computation ($N_r$-step optimization at each step); moderate diagnostic power.

**C3: Bellman** (self-consistent optimal). $\pi_{\text{cont}} = \pi^\ast$ where $\pi^\ast = \arg\max_\pi V_O(M_t, \pi;\, N_h)$.

The continuation IS the optimal policy — a fixed-point equation. $A_O^{\text{B}} = V_O(M_t, \pi^\ast;\, N_h)$ is the best achievable value under the model. Strongest diagnostic power; most expensive to compute (requires solving the Bellman equation or its approximation).

### Monotonicity

*[Derived (convention-monotonicity)]*

For any single fixed model $M_t$, horizon $N_h$, and policy class $\Pi$ (i.e., the static-evaluation form: $M_t$ frozen at the decision point, $\Pi$ unchanged across the comparison):

$$A_O^{(1)}(M_t;\, \Pi, N_h) \leq A_O^{\text{RH}}(M_t;\, \Pi, N_r, N_h) \leq A_O^{\text{B}}(M_t;\, \Pi, N_h)$$

**Preconditions on the inequality:** $M_t$ fixed (the comparison evaluates each convention against the *same* model), $\Pi$ fixed (the policy class is the same admissible set across all three conventions; nested $\Pi^{(1)} \subseteq \Pi^{\text{RH}} \subseteq \Pi^{\text{B}}$ would be a different result), $N_h$ fixed (the planning horizon is shared). Replanning *with updated $M_t$* (the deployment behavior of C2) is a different object than the static $A_O^{\text{RH}}$ defined here and the inequality does not automatically transfer — see the "Assumptions held fixed" paragraph below the derivation for the explicit caveat.

**Derivation.** Fix the model $M_t$, policy class $\Pi$, and horizon $N_h$. Each convention evaluates the best first action under a different continuation rule, holding these fixed:

- **C1** freezes continuation at $\pi_{\text{current}}$ (the agent's current policy, which may be suboptimal).
- **C2** re-optimizes periodically: at each replanning step, the agent selects the best available first action from $\Pi$ given $M_t$ at that time. By construction, $\pi_{\text{RH}} \succeq \pi_{\text{current}}$ at each future step, because C2 optimizes where C1 holds fixed.
- **C3** uses the globally optimal continuation $\pi^\ast = \arg\sup_{\pi \in \Pi} V_O(M_t, \pi; N_h)$, which is at least as good as any replanning policy because it optimizes over the full trajectory.

A weakly better continuation yields a weakly higher expected trajectory value (the objective $V_{O_t}$ is evaluated on the same trajectory distribution, with only the continuation policy changed). The ordering of continuations ($\pi_{\text{current}} \preceq \pi_{\text{RH}} \preceq \pi^\ast$) therefore implies $A_O^{(1)} \leq A_O^{\text{RH}} \leq A_O^{\text{B}}$. Taking the supremum over the first action preserves the ordering because the supremum of a larger set is at least as large. $\square$

**Assumptions held fixed:** same $M_t$ (the agent's current model, which may be wrong), same $\Pi$ (the agent's policy class, which may be narrow), same $N_h$ (the planning horizon). The ordering is about the *continuation rule*, not about the model or policy class. Improving $M_t$, expanding $\Pi$, or extending $N_h$ can change all three values simultaneously and is a separate operation (addressed in #der-orient-cascade, step 5).

**Corollary (monotonicity of $\delta_{\text{sat}}$ and $\delta_{\text{regret}}$).**

$$\delta_{\text{sat}}^{\text{B}} \leq \delta_{\text{sat}}^{\text{RH}} \leq \delta_{\text{sat}}^{(1)}$$

$$\delta_{\text{regret}}^{(1)} \leq \delta_{\text{regret}}^{\text{RH}} \leq \delta_{\text{regret}}^{\text{B}}$$

Since $\delta_{\text{sat}} = V_{O_t}^{\min} - A_O$, higher $A_O$ means lower $\delta_{\text{sat}}$. C1 is the most conservative diagnostic (most likely to diagnose "locally unattainable"); C3 is the most accurate (least likely to give false "unattainable" diagnoses). The regret ordering reverses: C3 reveals the largest regret because it compares against the globally optimal policy, while C1 reveals only the gap to the best one-step deviation.

### Diagnostic implications

| Convention | $\delta_{\text{sat}} \gt 0$ means | $\delta_{\text{regret}} \approx 0$ means |
|---|---|---|
| **C1** (one-step) | Cannot improve toward goal in one step from here | Current first action is locally near-optimal |
| **C2** (receding-horizon) | Cannot reach goal with $N_r$-step replanning | Current first action is near-optimal with replanning |
| **C3** (Bellman) | Goal is genuinely infeasible given $(M_t, \Pi, N_h)$ | Policy is globally near-optimal |

The 2×2 diagnostic table ( #def-control-regret) applies under all three conventions with the same structure but different inferential force. Under C1, the "capability limit" quadrant ($\delta_{\text{sat}} \gt 0$, $\delta_{\text{regret}} \approx 0$) means "locally stuck" — the agent may be globally recoverable but cannot see the recovery path. Under C3, the same quadrant means "genuinely infeasible" — no policy in $\Pi$ can achieve the goal. The cascade's inferential force scales with the convention.

**AAT adopts C1 as the canonical default** for three reasons: (1) it requires no fixed-point computation, consistent with the incremental update philosophy ( #emp-update-gain); (2) it makes all AAT diagnostics comparable across analyses of the same agent; (3) it is the most conservative, meaning false "feasible" diagnoses are minimized. Analyses that require stronger diagnostic power should state the convention explicitly. For deployed decision-making systems where "locally stuck but globally recoverable" situations are common, C2 is recommended.

Different continuation conventions yield different values for $A_O$, $\delta_{\text{sat}}$, and $\delta_{\text{regret}}$. Diagnostics computed under different conventions are not directly comparable — the convention is part of the measurement, not just the computation. When a specific convergence guarantee is needed (e.g., for #schema-strategy-persistence), the solution concept must be stated explicitly; the one-step improvement default does not provide convergence guarantees.

---



## Definition: Strategy Dimension

- **Slug**: `def-strategy-dimension`
- **Type**: definition
- **Status**: axiomatic
- **Stage**: deps-verified
- **Depends**: `form-complete-agent-state`, `form-objective-functional`

The purposeful substate $G_t$ decomposes into two structurally distinct components: $O_t$ (the objective — what the agent wants) and $\Sigma_t$ (the strategy — the agent's theory of how its actions produce progress toward $O_t$). These carry different kinds of information answering different questions.

*[Definition (strategy-dimension)]*

$$G_t = (O_t, \Sigma_t)$$

where:
- $O_t$: **evaluation** — "Is this trajectory satisfactory?" ( #form-objective-functional)
- $\Sigma_t$: **guidance** — "Which action sequence produces a satisfactory trajectory?"

The split is **definitional** — it reflects a structural difference in the information, not a dynamic or timescale claim. $O_t$ and $\Sigma_t$ are different *kinds* of state answering different questions:

| | $O_t$ (objective) | $\Sigma_t$ (strategy) |
|---|---|---|
| **Question** | How good is this trajectory? | How do I produce a good trajectory? |
| **Type** | $V_{O_t}: \text{trajectories} \to \mathbb{R}$ | Structured representation (see below) |
| **Richness varies** | Point target → utility → trajectory functional | Reactive → cached → subgoals → causal DAG |
| **Update source** | External (assigned, discovered, revised) | Internal (deliberation, evidence, cascade) |

**Strategy representations**, ordered by expressiveness:

| $\Sigma_t$ form | What it encodes | Example |
|---|---|---|
| None (reactive) | No explicit strategy; policy implicit in $M_t$ | Thermostat, reflex |
| Cached policy | Learned mapping $s \to a$ | Trained RL policy |
| Subgoal sequence | Waypoints with ordering | Navigation, recipe |
| Causal DAG | Action-outcome chains with AND/OR structure and confidence weights | Military plan, software project |

---
