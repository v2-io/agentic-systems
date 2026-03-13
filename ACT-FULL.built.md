# ACT: Agentic Cycle Theory

A mathematical framework for adaptive, purposeful agents under uncertainty.

**Working draft.** This is the current canonical outline of the theory — the argument laid out claim by claim. The ordering is the current best linearization of the dependency DAG; it will change as the theory develops. Slugs are the stable identities. Treat this as a living proof sketch, not a specification.

See `FORMAT.md` for segment file conventions. See `NOTATION.md` for symbols, conventions, and units.

Every slug is linked to its intended `src/{slug}.md` file, even when that file doesn't exist yet (`missing` or `old` stage). This is deliberate — the links serve as stable intent markers so the only ongoing maintenance is updating the Stage column. A `missing` link means no file exists; an `old` link means the content lives in a corresponding `src/old-*` source file awaiting conversion. Segments may also contain forward references (`#slug-name`) to not-yet-written segments; these are intentional dependency markers, not broken links.



## Table of Contents

**[I. Adaptive Systems Under Uncertainty](#i-adaptive-systems-under-uncertainty)**

- [Postulate I.1: Least-time is optimal](#temporal-optimality)
- [Definition I.2: Agent-environment boundary](#agent-environment)
- [Definition I.3: Lossy, noisy observations](#observation-function)
- [Definition I.4: Actions affect environment](#action-transition)
- [Scope I.5: Where ACT applies](#scope-condition)
- [Postulate I.6: Agent/subagent scale invariance](#composition-consistency)
- [Postulate I.7: Irreducible causal structure](#causal-structure)
- [Definition I.8: Three levels of causal reasoning](#pearl-causal-hierarchy)
- [Definition I.9: Complete interaction history](#chronica)
- [Formulation I.10: Compressed history as state](#agent-model)
- [Formulation I.11: Optimal model compression](#information-bottleneck)
- [Definition I.12: Predictive information retained](#model-sufficiency)
- [Definition I.13: Best achievable sufficiency](#model-class-fitness)
- [Formulation I.14: Events in continuous time](#event-driven-dynamics)
- [Derived I.15: State updates must be recursive](#recursive-update)
- [Derived I.16: Action as function of model](#action-selection)
- [Definition I.17: Prediction error signal](#mismatch-signal)
- [Result I.18: Model error + obs noise](#mismatch-decomposition)
- [Empirical I.19: Optimal update weighting](#update-gain)
- [Definition I.20: Information from interventions](#causal-information-yield)
- [Definition I.21: Rate of useful info acquisition](#adaptive-tempo)
- [Hypothesis I.22: Mismatch evolution ODE](#mismatch-dynamics)
- [Derived I.23: Think vs act tradeoff](#deliberation-cost)
- [Result I.24: Bounded mismatch condition](#persistence-condition)
- [Result I.25: Nonlinear persistence (Lyapunov)](#sector-condition-stability)
- [Result I.26: When parametric update fails](#structural-adaptation-necessity)
- [Derived I.27: Timescale stratification](#temporal-nesting)
- [Discussion I.28: Non-forkable causal trajectory](#agent-identity)

**[II. Actuated Adaptation: Agentic Systems](#ii-actuated-adaptation-agentic-systems)**

- [Definition II.1: ±model × ±objective quadrants](#agent-spectrum)
- [Formulation II.2: $X_t = (M_t, G_t)$](#complete-agent-state)
- [Definition II.3: $O_t$ parametrizes value](#objective-functional)
- [Definition II.4: Horizon/policy-conditioned value](#value-object)
- [Definition II.5: $G_t = (O_t, \Sigma_t)$ split](#strategy-dimension)
- [Derived II.6: Level 2 needed for planning](#causal-hierarchy-requirement)
- [Derived II.7: Feedback loop → Level 2 data](#loop-interventional-access)
- [Normative II.8: When planning beats exploring](#explicit-strategy-condition)
- [Derived II.9: Log-confidence additive in depth](#chain-confidence-decay)
- [Scope II.10: Conjunctive/disjunctive scope](#and-or-scope)
- [Definition II.11: Strategy as probabilistic DAG](#strategy-dag)
- [Derived II.12: Epistemic update is goal-blind](#directed-separation)
- [Definition II.13: Ideal vs best achievable](#satisfaction-gap)
- [Definition II.14: Best achievable vs current](#control-regret)
- [Definition II.15: Edge residuals](#strategic-calibration)
- [Derived II.16: Resolution order by info dep](#orient-cascade)
- [Derived II.17: Unobservable edges freeze](#observability-dominance)
- [Hypothesis II.18: Gain extends to strategy edges](#edge-update-via-gain)
- *\[Gap\] When observational edge updates yield valid causal semantics*
- [Formulation II.19: Pruning/grafting as continuous](#structural-change-as-parametric-limit)
- *\[Gap\] Rate of useful $\Sigma_t$ revision (adaptive tempo for strategy)*
- *\[Gap\] Complexity cost of maintaining $\Sigma_t$ (IB/MDL for DAGs)*
- [Proposed schema II.20: Sector conditions for $\Sigma_t$](#strategy-persistence-schema)
- *\[Gap\] Three-way exploit/explore/deliberate allocation with $\Sigma_t$*

**[III. Agentic Composites](#iii-agentic-composites)**

- [Scope III.1: Multiple agents, shared env](#multi-agent-scope)
- [Formulation III.2: Composite agent via closure defect](#composition-closure)
- [Derived III.3: Sub-additive tempo inequality](#tempo-composition)
- *\[Gap\] Does epistemic goal-blindness survive composition?*
- [Definition III.4: 4 dimensions of coherence](#unity-dimensions)
- [Definition III.5: IB-compressed purpose](#shared-intent)
- [Hypothesis III.6: Prioritize objective sharing](#auftragstaktik-principle)
- [Derived III.7: Composite persistence condition](#team-persistence)
- [Result III.8: Superlinear tempo advantage](#adversarial-tempo-advantage)
- [Hypothesis III.9: Trust-weighted update gain for inter-agent channels](#communication-gain)
- [Derived III.10: Inside opponent's loop; includes effects spiral corollary](#adversarial-destabilization)
- *\[Gap\] Which strategy edges are most valuable to attack*
- [Observation III.11: $\alpha = 2, 3/2, \text{or } {\sim}1$](#adversarial-exponent-regimes)
- [Observation III.12: Obs noise gates advantage](#observation-gates-advantage)
- [Result III.13: Weak dimension is bottleneck](#per-dimension-persistence)

**[IV. Agentic-Grounded Software Systems](#iv-agentic-grounded-software-systems)**

- [Scope IV.1: Systems with $P(\text{change}) \gt \varepsilon$](#software-scope)
- *Observation IV.2: Software's 6 unique properties* (not yet written)
- [Definition IV.3: Unit of coherent change](#feature-definition)
- [Result IV.4: Can't implement unspecified; includes communication bottleneck corollary](#specification-bound)
- [Derived IV.5: Median future ≈ observed past; includes investment scale form](#change-expectation-baseline)
- *Definition IV.6: Developer as $(M_t, O_t, \Sigma_t)$* (not yet written)
- [Definition IV.7: Cost of constructing local $M_t$](#comprehension-time)
- [Definition IV.8: Cost from first change to done](#implementation-time)
- [Derived IV.9: Min comprehension + impl time](#dual-optimization)
- [Derived IV.10: When extra time now pays off](#change-investment)
- *Discussion IV.11: Code quality $\to U_o \to \eta^\ast \to \mathcal{T}$* (not yet written)
- *\[Gap\] Developer tempo as $\mathcal T_{\text{obs}}$ + $\mathcal T_{\text{explore}}$ + $\mathcal T_{\text{probe}}$*
- [Hypothesis IV.12: Code-domain alignment; includes realignment corollary](#conceptual-alignment)
- [Definition IV.13: The diff that is the feature](#atomic-changeset)
- [Empirical IV.14: Time ∝ changeset size; includes comprehension corollary](#changeset-size-principle)
- [Definition IV.15: Lexical < file < module < svc](#change-distance)
- [Derived IV.16: Closer changes → less time](#change-proximity-principle)
- [Hypothesis IV.17: Context-switch cost compounds?](#exponential-cognitive-load)
- [Definition IV.18: $P(\text{change } j \mid \text{change } i)$](#system-coupling)
- [Definition IV.19: $E[\text{proximity within module}]$](#system-coherence)
- [Measurement IV.20: Coherence/coupling from git](#coherence-coupling-measurement)
- [Derived IV.21: Optimal $C$ minimizes $E[T \vert C]$](#principled-decision-integration)
- [Definition IV.22: $\text{MTTF}/(\text{MTTF}+\text{MTTR})$](#system-availability)
- [Scope IV.23: Include $P(\text{fail}) \times T_{\text{recovery}}$](#continuous-operation)
- *Hypothesis IV.24: Git as interventional data* (not yet written)
- *\[Gap\] Software persistence: the unmaintainability threshold formalized*

**[V. Logogenic Agents](#v-logogenic-agents)**

- *Definition V.1: AI agent as actuated agent* (not yet written)
- *Observation V.2: 100% $M_t$ reset per session* (not yet written)
- *Discussion V.3: External memory as persistent $M_t$* (not yet written)
- *\[Gap\] Language-specific orient cascade (what's specific to logogenic agents?)*
- *\[Gap\] Measuring $M_t$ quality, $\Sigma_t$ quality, and tempo in AI agents*
- *\[Gap\] ACT-grounded experiential training environments*
- *\[Gap\] Self-referential closure: ACT agent on ACT codebase*

**[VI. Logozoetic Agents](#vi-logozoetic-agents)**

**[Appendices: Details](#appendices-details)**

- [Derivation A.1: Lyapunov derivations for bounded mismatch and adaptive reserve](#sector-condition-derivation)
- [Derivation A.2: Uniqueness derivation via three constraints + counterexamples](#recursive-update-derivation)
- [Sketch A.3: N-timescale singular perturbation sketch](#multi-timescale-stability)
- *Detail A.4: Pedagogical linear mismatch ODE* (not yet written)
- [Detail A.5: 6 variants validating claims](#simulation-results)

**[Appendices: Operational Domains](#appendices-operational-domains)**

- [Detail B.1: Estimation procedures for ACT quantities](#operationalization)
- [Worked example B.2: End-to-end Kalman instantiation (exact)](#worked-example-kalman)
- [Worked example B.3: End-to-end RL bandit instantiation (approximate)](#worked-example-bandit)


---

## I. Adaptive Systems Under Uncertainty

*Scope: Any system consisting of an agent coupled to an environment through observation and action channels, where the environment is not fully observable. This is the general case — thermostats through commanders. The claims in this section are largely drawn from TFT (TF-01 through TF-11, Appendix A), which developed the adaptive-systems foundation that ACT subsumes.*


<a id="temporal-optimality"></a>

### Postulate I.1: *Temporal Optimality*

Among agents achieving identical outcomes across all non-temporal dimensions, the one requiring least time is optimal.

#### Formal Expression

*[Postulate (temporal-optimality)]*

Let $\mathbf{A} = \{A_1, A_2, \ldots, A_n\}$ be agents or strategies achieving outcome $O$.

$$\text{If } \forall m \in \mathbf{M} \setminus \{\text{time}\},\; \forall i,j:\; m(A_i) \equiv m(A_j), \quad \text{then } A^* = \arg\min_{A_k} \text{time}(A_k)$$

where $\mathbf{M}$ is the set of all measurable outcome dimensions, and identical outcomes $m(A_i) \equiv m(A_j)$ means equivalence across:
- **Functional**: Same input→output mappings
- **Non-functional**: Same performance, security, availability
- **Quality**: Same defect probability, maintainability
- **Sustainability**: Same impact on agent capacity and system evolution
- **Impact on others**: Same effect on other agents' capacity

#### Epistemic Status

This is a postulate — deliberately tautological. The statement reduces to: "given a choice between identical outcomes, the one that arrives sooner is preferred." The inability to construct genuine counterexamples without violating the equivalence precondition reveals its postulate nature. The fungibility argument (below) is *discussion* — a qualitative observation about why time is a natural optimization target, not a derived result.

#### Discussion

**Why time is special.** Time is uniquely fungible among outcome dimensions: saved time can become exploration, learning, rest, additional action — anything. Other outcome dimensions (correctness, safety, quality) are not fungible in this way. A unit of saved correctness cannot be spent on learning. This is why, once all other outcome dimensions are held equal, time is the natural residual to optimize. The postulate makes this optimization explicit.

**The equivalence precondition is load-bearing.** The phrase "identical outcomes across all non-temporal dimensions" is doing most of the work. It must be verified concretely before the postulate applies. Apparent counterexamples invariably violate it:
- "Move fast and break things" — violates quality equivalence
- Burnout-inducing speed — violates sustainability equivalence
- Premature optimization for unlikely futures — optimizes for a counterfactual outcome, violating actual-outcome equivalence
- Skipping tests for speed — violates defect probability equivalence

The postulate does not say faster is always better. It says faster is better *given identical outcomes*. An agent that achieves a worse outcome faster is not preferred by this postulate. Misapplication of temporal optimality without verifying the equivalence precondition produces exactly the pathologies listed above.

**Why start here.** The adaptive machinery that follows — tempo, gain, persistence, adversarial dynamics — can be understood as consequences of optimizing for this criterion under constraints of partial observability, bounded resources, and environmental change. The connections are developed in their respective claims; they are not implied by this postulate alone.

**Domain generality.** This postulate applies to any agent-environment pairing within ACT's scope ([Scope I.5](#scope-condition)). In the software domain, it specializes to the statement that among implementations achieving identical outcomes, the one requiring least development time is optimal (TST T-01). The generalization is straightforward: replace "implementation" with "adaptive strategy."

**Scope limitation.** This postulate does not, by itself, say anything about *how* to achieve temporal optimality. That is the subject of the rest of the theory.

#### Working Notes

- This postulate reads externally as a conditional preference principle, not a deep first principle — and that's fine. Its real role is as a **normative selection rule that later claims instantiate**: tempo, gain, persistence, and adversarial dynamics are consequences of optimizing under this criterion. Lean into this framing. The postulate is the source of *structure* (it gives the theory its optimization target), not the source of *explanatory power* (which comes from the machinery that follows).
- During Section I review: consider making this normative-selection-rule character more explicit in the Discussion, rather than leaving it implicit in "The connections are developed in their respective claims."


<a id="agent-environment"></a>

### Definition I.2: *Agent-Environment Coupling*

An agent is an entity that receives observations from an environment, maintains internal state, and produces actions that affect the environment. The agent cannot access the environment directly — observations are necessarily lossy. This boundary condition is constitutive: the theory applies where the agent-environment boundary entails information loss.

#### Formal Expression

*[Definition (agent-environment)]*

Let $\Omega$ denote the **environment**: the totality of state external to the agent. We make no assumptions about $\Omega$'s structure — it may be continuous or discrete, stationary or non-stationary, deterministic or stochastic, benign or adversarial.

An **agent** is an entity satisfying three conditions:

1. It receives observations from $\Omega$ (perception channel)
2. It maintains internal state (memory/model)
3. It produces actions that affect $\Omega$ (action channel)

*[Definition (information-loss-boundary)]*

The agent cannot access $\Omega_t$ directly. All contact with the environment is mediated through lossy observation. This is not a simplifying assumption — it is a scope condition. Systems where the agent has direct access to full environment state are outside ACT's scope ([Scope I.5](#scope-condition)).

#### Epistemic Status

This is *definitional* — it establishes the conceptual framework, not a truth-claim. The agent-environment decomposition is a modeling choice that delineates what ACT analyzes. The information-loss boundary is the constitutive commitment: it restricts ACT's scope to systems where the agent faces genuine uncertainty about its environment.

#### Discussion

**Why information loss is constitutive.** An agent with perfect access to $\Omega_t$ has no need for a model, no mismatch signal, no adaptation. The entire adaptive machinery of Section I becomes vacuous. The information-loss boundary is what makes the theory non-trivial.

**Generality of $\Omega$.** The environment is deliberately underspecified. $\Omega$ may include other agents, physical systems, software artifacts, or any combination. The only structural commitment is that $\Omega$ is external to the agent and not fully accessible.


<a id="observation-function"></a>

### Definition I.3: *Observation Function*

Observations are lossy, possibly noisy functions of environment state, prior action, and perceptual noise. The agent knows neither the observation function nor the noise distribution exactly.

#### Formal Expression

*[Definition (observation-function)]*

The **observation space** $\mathcal{O}$ is the set of possible observations. Each observation is generated by:

$$o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$$

where:
- $h$ is the observation function (unknown to the agent)
- $\Omega_t$ is the environment state at time $t$
- $a_{t-1}$ is the agent's prior action (observations may depend on what the agent did)
- $\varepsilon_t$ represents noise or limits of perception

*[Definition (epistemic opacity)]*

The agent knows neither $h$ nor the distribution of $\varepsilon_t$ exactly.

#### Epistemic Status

This is *definitional*. The observation function $h$ is a modeling device that captures the information-loss boundary established in [Definition I.2](#agent-environment). The dependence on $a_{t-1}$ is optional — when absent, the function reduces to $h(\Omega_t, \varepsilon_t)$. The claim that the agent does not know $h$ or the noise distribution is constitutive of the partial-observability setting, not an empirical assertion.

#### Discussion

**Lossiness is the key property.** The observation function $h$ maps from $\Omega_t$ (high-dimensional, inaccessible) to $\mathcal{O}$ (what the agent actually receives). Information is destroyed in this mapping. This is what forces the agent to maintain a model ([Formulation I.10](#agent-model)) rather than simply reading off the environment state.

**Action-dependence.** The inclusion of $a_{t-1}$ allows the observation function to capture active perception: what the agent sees may depend on where it looked. This is relevant in software ([Observation IV.2](#software-epistemic-properties)), where observation quality is partly under agent control.


<a id="action-transition"></a>

### Definition I.4: *Action and Transition*

Actions affect the environment through a transition function that is unknown to the agent and possibly stochastic.

#### Formal Expression

*[Definition (action-transition)]*

The **action space** $\mathcal{A}$ is the set of actions available to the agent. Actions affect the environment via the transition function:

$$\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$$

where:
- $T$ is the (possibly stochastic) transition function
- $\Omega_t$ is the current environment state
- $a_t \in \mathcal{A}$ is the agent's chosen action

*[Definition (transition opacity)]*

The agent does not know $T$ exactly.

#### Epistemic Status

This is *definitional*. The transition function $T$ is a modeling device that captures how agent actions couple back into the environment. The stochasticity of $T$ is allowed but not required — deterministic transitions are the special case where $T$ places all mass on a single successor state. The claim that $T$ is unknown to the agent is constitutive of the uncertainty setting, paralleling the epistemic opacity of $h$ ([Definition I.3](#observation-function)).

#### Discussion

**Closing the loop.** Together with [Definition I.3](#observation-function), this definition completes the agent-environment coupling: the agent observes via $h$ and acts via $T$. The loop $\Omega_t \xrightarrow{h} o_t \rightarrow \text{agent} \xrightarrow{a_t} \Omega_{t+1}$ is the fundamental structure that all subsequent claims build on.

**Uncertainty about $T$ is what makes action non-trivial.** If the agent knew $T$ exactly, action selection would reduce to optimization over a known function. The combination of unknown $h$ and unknown $T$ is what creates the need for adaptive behavior.


<a id="scope-condition"></a>

### Scope I.5: *Scope Condition*

ACT applies wherever there is an agent that observes, acts with at least a binary choice, and faces residual uncertainty about its environment.

#### Formal Expression

*[Definition (scope-condition)]*

$$\mathcal{S}_{\text{ACT}} = \left\{(\text{Agent}, \Omega) \;:\; \mathcal{O} \neq \emptyset, \;\; \lvert\mathcal{A}\rvert \geq 2, \;\; H(\Omega_t \mid \mathcal{C}_t) \gt 0 \right\}$$

Three conditions jointly define ACT's domain:

1. **Observations exist**: $\mathcal{O} \neq \emptyset$ — the agent has some perceptual channel to the environment ([Definition I.3](#observation-function))
2. **At least binary choice**: $\lvert\mathcal{A}\rvert \geq 2$ — the agent can choose between at least two actions ([Definition I.4](#action-transition))
3. **Residual uncertainty persists**: $H(\Omega_t \mid \mathcal C_t) \gt 0$ — the environment is not fully determined by the interaction history

#### Epistemic Status

This is a *scope definition* — it draws the boundary around the systems ACT addresses. The three conditions are not derived; they are the minimal requirements for the adaptive machinery that follows to be non-vacuous. The action-space requirement ($\lvert\mathcal{A}\rvert \geq 2$) is the most substantive choice: it ensures at least one interventional contrast, which is the minimal condition for causal learning and exploration.

#### Discussion

**What is included.** The scope is deliberately broad. It encompasses thermostats (minimal agent, binary action), Kalman filters (continuous observation, parametric model), military commanders (rich model, explicit strategy), software developers (epistemic agents modifying their own observation infrastructure), and AI agents (100% context turnover, same formal structure). These are not analogies — they are instances of the same formal framework at different points in the agent spectrum ([Definition II.1](#agent-spectrum)).

**What is excluded.** Three classes fall outside ACT's scope:

- **Passive observers** ($\lvert\mathcal{A}\rvert \lt 2$): An entity that observes but cannot act has no interventional contrast and cannot learn causal structure. It can correlate but not intervene.
- **Closed-form systems** ($H(\Omega_t \mid \mathcal C_t) = 0$): When the agent has complete knowledge of the environment, there is no uncertainty to adapt to. Optimal control over known dynamics is a solved problem outside ACT's concerns.
- **Pure computation** ($\mathcal{O} = \emptyset$): A system with no observation channel — e.g., a mathematical proof engine operating on axioms alone — has no agent-environment boundary in ACT's sense.

**Why $\lvert\mathcal{A}\rvert \geq 2$.** A single available action eliminates choice, and with it the possibility of interventional contrast. The agent cannot compare outcomes under different actions, which is the minimal requirement for Level 2 causal reasoning ([Definition I.8](#pearl-causal-hierarchy)). Binary choice is sufficient: a single A/B contrast supports causal learning.


<a id="composition-consistency"></a>

### Postulate I.6: *Composition Consistency*

ACT applies at every level of description where the scope condition is met. A team of agents is itself an agent; a department of teams is itself an agent. The theory's predictions at each level must be compatible — and they are, under a condition analogous to the persistence threshold: the composite's internal coordination must be fast relative to the external dynamics it faces.

#### Formal Expression

*[Postulate (composition-consistency)]*

For any system $S$ satisfying the scope condition ([Scope I.5](#scope-condition)), and any decomposition of $S$ into subsystems $\{S_1, \ldots, S_n\}$ where each $S_i$ also satisfies the scope condition, ACT's predictions at the system level must be compatible with its predictions at the subsystem level. Specifically, composition laws must exist such that:

1. **Tempo composition**: $\mathcal T_S$ is expressible as a function of $\{\mathcal T_{S_i}\}$ and the coordination structure among them
2. **Persistence compatibility**: the system's persistence is derivable from the sub-agents' individual persistence conditions plus coordination structure
3. **Mismatch consistency**: $\delta_S$ is derivable from $\{\delta_{S_i}\}$ and their interaction structure

*[Sufficient Condition (composition-validity)]*

**Timescale separation condition.** A group of sub-agents behaves as a valid composite agent when its internal equilibration timescale $\tau_{\text{eq}}$ — the time for sub-agents to approximately synchronize models and coordinate actions — is short relative to the external dynamics timescale $\tau_{\text{ext}}$ — the time for the environment to change significantly from the macro-agent's perspective:

$$\tau_{\text{eq}} \ll \tau_{\text{ext}}$$

When this holds, the internal dynamics have approximately settled by the time the next external challenge arrives, and the composite's macro-state is predictive of its macro-behavior. This is the composition analog of the persistence condition ([Result I.24](#persistence-condition)): just as an individual agent requires $\mathcal{T} \gt \rho / \Vert\delta_{\text{critical}}\Vert$ to maintain bounded mismatch, a composite agent requires fast internal coordination to maintain a coherent macro-description.

Most functioning groups easily satisfy this condition. A software team with daily standups and shared CI ($\tau_{\text{eq}} \sim$ hours) facing weekly feature deadlines ($\tau_{\text{ext}} \sim$ weeks) is comfortably a valid composite. A military squad communicating by voice ($\tau_{\text{eq}} \sim$ seconds) in a tactical situation evolving over minutes is clearly a single agent. The theory applies broadly; the interesting questions arise near the threshold.

#### Epistemic Status

*Axiomatic.* The meta-requirement (cross-level compatibility) is a structural requirement for ACT's internal consistency — if the scope condition doesn't restrict which level the theory applies to, the predictions must not contradict across levels. The timescale separation condition is stated here as a sufficient condition for practical composition; its formal derivation requires the composition closure criterion ([Formulation III.2](#composition-closure)) and the tempo composition inequality ([Derived III.3](#tempo-composition)) developed in Section III. The condition is not yet proved; it is stated early because it is intuitive, likely correct, and gives readers an immediate practical test.

#### Discussion

**The same pattern as individual persistence.** The persistence condition says: there is a measurable threshold below which an individual agent's mismatch grows without bound and the agent degrades. Composition consistency says the same thing at the composite level: there is a measurable threshold ($\tau_{\text{eq}} / \tau_{\text{ext}}$) below which the composite description breaks down. In both cases, most competent agents are comfortably above the threshold — the theory applies broadly, and the edge cases are where it gets interesting.

**What this buys the theory.** With composition consistency stated early:
- Every subsequent result (persistence, gain, tempo, mismatch decomposition, orient cascade) is understood to apply at every level of composition where the timescale condition holds
- Section III becomes the study of *what happens near and beyond the threshold* — coordination overhead, unity dimensions, adversarial dynamics — rather than a separate multi-agent theory
- The formal test for composition validity ([Formulation III.2](#composition-closure)) provides the rigorous version of the timescale condition

**When composition fails.** The timescale condition fails when:
- Internal coordination slows (communication overhead scales poorly, conflicts consume attention, bureaucratic process)
- External dynamics accelerate (adversary acts faster, market shifts, crisis compresses decision timescales)
- Both simultaneously (the classic organizational failure mode — internal friction increases while external demands intensify)

This is the formal analog of Brooks's Law: adding people to a late project increases $\tau_{\text{eq}}$ (more coordination) while $\tau_{\text{ext}}$ stays fixed (the deadline doesn't move). Eventually $\tau_{\text{eq}}$ exceeds $\tau_{\text{ext}}$ and the composite ceases to function as a coherent agent. The model captures the same structural pattern; whether the specific mechanism (timescale crossing) is the actual cause of Brooks's Law is an empirical question.

**The boundary is a modeling choice.** A development team is simultaneously: individual developers (each an ACT agent), the team (a composite ACT agent), and part of an organization (a sub-agent within a larger composite). The scope condition is satisfied at every level. Composition consistency ensures the theory doesn't give contradictory answers about observable quantities (e.g., whether the team persists) regardless of which boundary is chosen.

**What composition consistency does NOT say.** It does not specify the form of the composition laws — those are derived in Section III ([Derived III.3](#tempo-composition)). It does not say every decomposition is equally useful for analysis. And it does not require perfect internal coordination — only that internal equilibration is fast relative to external dynamics.

#### Working Notes
- The timescale separation condition is essentially the singular perturbation argument from [Derived I.27](#temporal-nesting) applied to composition: the fast internal dynamics approximately equilibrate, and the composite's behavior is described by the slow (external) dynamics on the equilibrium manifold. The formal connection should be made explicit when temporal-nesting is reviewed.
- Composition of directed separation: if each sub-agent's $f_M$ is $G_t$-independent, does the composite's $f_M^c$ remain $G_t^c$-independent? Hypothesis: goal-blindness composes, BUT coordination routing may break it — if which observations reach the composite depends on the shared objective, the composite's effective observation function is goal-dependent. This is the organizational analog of the LLM scope restriction in [Derived II.12](#directed-separation).
- The "atomic agent" question: if every agent is decomposable, where does it bottom out? At agents whose internal dynamics are not usefully described by ACT — below the level where observations, actions, and uncertainty exist, the scope condition fails and the recursion terminates.
- The relationship to holons (Koestler 1967): an ACT agent satisfying composition consistency is a holon — simultaneously a whole (analyzable as a single agent) and a part (decomposable into sub-agents). The term is occasionally useful but carries significant mystical baggage from later appropriations. Use sparingly.


<a id="causal-structure"></a>

### Postulate I.7: *Causal Structure*

The agent-environment interaction has irreducible causal structure grounded in the temporal ordering of events. Actions precede their consequences; observations follow from the state they observe. This ordering is constitutive of the feedback loop and holds independent of the magnitude of the agent's influence on the environment.

#### Formal Expression

*[Postulate (causal-structure)]*

The interaction history $\mathcal C_t$ ([Definition I.9](#chronica)) is not merely a set of observations and actions — it is an *ordered sequence* in which temporal position carries meaning. $a_{t-1}$ was selected before $o_t$ was received. The agent could not have used $o_t$ to select $a_{t-1}$. This asymmetry — the arrow of time — is the foundation of causal structure in the theory.

We adopt the most primitive notion of causality: **event $A$ can be a cause of event $B$ only if $A$ temporally precedes $B$.** This is weaker than (and prior to) statistical notions of causality. It is a statement about the *structure of possible influence*, not about actual influence.

#### Epistemic Status

This is a *postulate* — the temporal ordering of events is a physical fact about the universe that the theory takes as given. The second law of thermodynamics, the light-cone structure of relativity, and the arrow of psychological time all enforce it, but ACT does not derive it from any of these. It is simply noted as a precondition: the theory applies to agents embedded in a universe where time has a direction.

#### Discussion

**Causality as temporal ordering is the most primitive notion.** Three levels of causal reasoning derive from this foundation ([Definition I.8](#pearl-causal-hierarchy)), but the temporal notion survives even when statistical influence is negligible. An agent passively observing a system with minimal intervention still has a causal history — the temporal ordering of its observations and actions structures what it can learn and when.

**Causal structure independent of coupling strength.** The causal structure of the feedback loop is preserved even when the agent's actions have minimal effect on the environment:

- **Strong coupling** ($a_t$ significantly affects $\Omega_{t+1}$): Robot manipulation, military action. Interventional information is rich.
- **Weak coupling** ($a_t$ marginally affects $\Omega_{t+1}$): Scientific observation, small financial trades. Interventional information is sparse but non-zero.
- **Nominal coupling** ($a_t$ negligibly affects $\Omega_{t+1}$): Near-passive observation. The causal structure degenerates toward Level 1, but the agent's *choice* of what to observe still matters.
- **Zero coupling** ($T(\Omega_{t+1} \mid \Omega_t, a_t) = T(\Omega_{t+1} \mid \Omega_t)$ for all $a_t$): Actions don't affect the environment. Level 2 access vanishes. The feedback "loop" collapses to a one-way channel. Still within scope when $\lvert\mathcal{A}\rvert \geq 2$ ([Scope I.5](#scope-condition)), but action-dependent results become trivially void.

The theory should not be understood as applying only to agents with strong environmental control. The causal structure of the temporal ordering alone is sufficient for the core results.

**Consequences for the feedback loop.** The irreversibility of temporal ordering yields the core structure:

- The model update is **directed** — the model at time $t$ depends on prior events, never on future ones
- The mismatch signal $\delta_t$ ([Definition I.17](#mismatch-signal)) is **retrospective** — comparing a prediction (made before $o_t$) with an observation (arriving after)
- Action selection is **prospective** — using the current model to influence future events
- The chronica ([Definition I.9](#chronica)) is **monotonically growing** — events are added but never removed

**Implications for model updating.** The causal postulate constrains the update rule: the model should give more weight to observations that are *causally downstream* of the agent's actions than to observations that would have occurred regardless. Action-contingent observations carry interventional (Level 2) information; action-independent observations carry only associational (Level 1) information. The formal measure of this distinction — causal information yield (CIY) — is developed in [Definition I.20](#causal-information-yield).

**(Descended from TF-02.)**


<a id="pearl-causal-hierarchy"></a>

### Definition I.8: *Pearl's Causal Hierarchy*

Three levels of causal reasoning emerge from the causal structure of the feedback loop: association ("what if I observe?"), intervention ("what if I do?"), and counterfactual ("what if I had done differently?"). The binary action requirement ([Scope I.5](#scope-condition)) ensures at least Level 2 access is structurally available.

#### Formal Expression

*[Definition (pearl-causal-hierarchy)]*

**Level 1 — Associational**: $P(o_t \mid \mathcal{C}_{\lt t})$

*What will I observe next, given what I've observed before?*

Pattern recognition over the temporally ordered history. Available to any agent that maintains a model ([Formulation I.10](#agent-model)), including purely passive observers. The temporal ordering constrains which associations are meaningful: $o_3$ can depend on $o_1, a_1, o_2, a_2$ but not on $o_4$.

**Level 2 — Interventional**: $P(o_t \mid do(a_{t-1}), M_{t-1})$

*What will I observe if I* do *this?*

The $do(\cdot)$ operator marks the crucial distinction: this is not "what observation tends to follow this action in the historical record" (associational) but "what will happen *because* I take this action now." This requires: (1) the agent's action temporally precedes the observation ([Postulate I.7](#causal-structure)), (2) the agent chose the action (it was not determined by the same causes that determine the observation), (3) the environment's response carries information about the causal relationship.

Level 2 is why the feedback loop is more powerful than passive observation. By *acting* and then observing consequences, the agent obtains information about causal mechanisms — not merely about correlations. The mismatch signal $\delta_t$ ([Definition I.17](#mismatch-signal)), conditioned on the agent's own action, is an *interventional* signal.

**Level 3 — Counterfactual**: $P(o_t^{a'} \mid a_{t-1} = a, o_t = o)$

*Given that I did $a$ and observed $o$, what would I have observed if I had done $a'$ instead?*

This requires the model to simulate alternative histories — running the causal structure "backward" and then "forward" under different interventions. It is the most demanding epistemic level and the basis for regret computation, strategic simulation, and learning from single observations.

#### Epistemic Status

This is *definitional* — it names three modes of epistemic access that are structurally available within the feedback loop, following Pearl's causal hierarchy (Pearl 2009; Bareinboim et al. 2022). The hierarchy itself is a well-established result in causal inference. ACT's contribution is grounding it in the temporal structure of the agent-environment coupling rather than in abstract graphical models.

#### Discussion

**Availability vs. exploitation.** The three levels describe epistemic access that the causal structure *makes available* — not what any particular agent *uses*. Many systems within ACT's scope operate primarily at Level 1. A Kalman filter coupled with an LQR controller has Level 2 access structurally present (its innovation signal is conditioned on prior action), but the separation principle guarantees estimation quality is invariant to control policy — the system does not *exploit* the interventional structure. Only dual control (choosing actions partly for their informational value) exercises Level 2 access in this domain. Similarly, a PID controller has no deliberative capacity — it operates entirely at Level 1. Which levels an agent exercises depends on its architecture and model class.

**Forward-looking deliberation exercises Level 2, shading into Level 3.** Comparing candidate actions before choosing — "what will happen if I do X vs Y?" — primarily exercises Level 2 (iterated mental intervention). When the agent evaluates past choices to refine the comparison ("given what happened when I tried X last time, what would Y have produced?"), it exercises Level 3.

**The causal hierarchy theorem.** Bareinboim et al. (2022) prove that the three levels form a strict hierarchy: Level 2 knowledge cannot in general be computed from Level 1 data alone, and Level 3 cannot be computed from Level 2 alone. This is load-bearing for ACT's Section II: evaluating $Q_O(M_t, a; \cdot)$ is a Level 2 query, so agents that need to *learn* action consequences during operation require causal structure beyond predictive models ([Derived II.6](#causal-hierarchy-requirement)).

**Software as a uniquely rich domain for this hierarchy.** In most domains, Level 3 counterfactuals require model-based simulation with uncertain fidelity. In software development, `git checkout` provides Level 3 access with ground-truth verification — the agent can literally execute the counterfactual. This is one of software's unique epistemic properties ([Observation IV.2](#software-epistemic-properties)) and makes it an ideal testbed for causal reasoning within ACT.

**Domain instantiations of the three levels:**

| Domain | Level 1 (Association) | Level 2 (Intervention) | Level 3 (Counterfactual) |
|--------|----------------------|----------------------|------------------------|
| Kalman filter | Prediction from state estimate | Innovation conditioned on action | Not typically exercised |
| RL agent | Value function prediction | Action → reward observation | Regret computation |
| Scientific method | Correlational observation | Experimental intervention | "What if we had used control X?" |
| Military (Boyd) | Pattern recognition | Probe/feint → observe response | "What if we had attacked from the flank?" |
| Software developer | "I think this function does X" | Run test → observe result | `git checkout` + alternative implementation |
| Immune system | Antigen pattern matching | Antibody → pathogen response | Not exercised (no counterfactual reasoning) |

**(Descended from TF-02.)**


<a id="chronica"></a>

### Definition I.9: *Chronica*

The interaction history $\mathcal C_t$ is the complete, singular causal record of the agent's observations and actions. Everything the agent can ever know must be constructed from this sequence.

#### Formal Expression

*[Definition (chronica)]*

$$\mathcal{C}_t = (o_1, a_1, o_2, a_2, \ldots, a_{t-1}, o_t)$$

The ordering is not a notational convenience. It reflects an irreversible physical fact: $a_{t-1}$ was selected before $o_t$ was received. The agent could not have used $o_t$ to select $a_{t-1}$.

$\mathcal C_t$ is monotonically growing — events are added but never removed. It is the agent's *only* raw material for constructing a model ([Formulation I.10](#agent-model)).

#### Epistemic Status

This is *definitional*. The chronica names an object that exists by construction in any system satisfying [Definition I.2](#agent-environment): the temporal sequence of all agent-environment interactions. The term "chronica" (from Greek χρονικά, "records of time") avoids collision with $\mathcal{H}$ (Shannon entropy) in speech and notation.

#### Discussion

**The chronica is singular and non-forkable.** Because the temporal ordering is irreversible, $\mathcal C_t$ represents a unique causal trajectory. Duplicating an agent's state and exposing the copies to different future events creates two agents with divergent chronica, neither of which is a sufficient statistic for the other's trajectory. See [Discussion I.28](#agent-identity) for the full development of this observation.

**Relationship to the model.** The model $M_t = \phi(\mathcal C_t)$ ([Formulation I.10](#agent-model)) is a compression of the chronica. How much of $\mathcal C_t$'s predictive information survives compression is measured by model sufficiency ([Definition I.12](#model-sufficiency)).


<a id="agent-model"></a>

### Formulation I.10: *The Reality Model*

The agent's compressed representation of how the world works, mapping interaction history to model space. This is a formulation choice — we commit to analyzing the agent as having a complete state $M_t$ that subsumes all retained information from its history.

#### Formal Expression

*[Formulation (agent-model)]*

$$M_t = \phi(\mathcal{C}_t)$$

where:
- $\phi: \mathcal{C}^\ast \to \mathcal{M}$ maps interaction history to model space $\mathcal{M}$
- $\mathcal C_t = (o_1, a_1, \ldots, o_t)$ is the chronica ([Definition I.9](#chronica)) — the complete record of agent-environment interaction
- $\mathcal{M}$ is the space of possible models the agent can hold

The mapping $\phi$ is a many-to-one compression: multiple distinct histories may produce the same model state. This is not a deficiency — it is the essential function of the model: retaining what matters and discarding what does not.

#### Epistemic Status

This is a *formulation* — a representational commitment, not a derived result. We choose to analyze agents as maintaining a state object $M_t$ that mediates between history and future action. Alternative formulations exist (e.g., history-based policies that map $\mathcal C_t$ directly to actions without an explicit model). The formulation is justified by its analytical utility: it enables the information bottleneck analysis ([Formulation I.11](#information-bottleneck)), the mismatch decomposition ([Definition I.17](#mismatch-signal)), and the gain principle ([Empirical I.19](#update-gain)).

#### Discussion

**$M_t$ is the epistemic substate.** It captures "what the agent believes about reality." Different agents realize $M_t$ differently: a Kalman filter holds a state estimate and covariance matrix; an RL agent holds a value function; a developer holds a mental model of codebase architecture; an LLM agent holds its context window contents plus retrieved memory. The formalism is agnostic to the realization — it asks only that $M_t$ exist as a well-defined object that the agent's policy can condition on.

**Completeness assumption.** By writing $M_t = \phi(\mathcal C_t)$, we assume that $M_t$ captures everything the agent retains from its history. Any information not in $M_t$ is lost to the agent. This is what makes $M_t$ the complete epistemic substate, not merely one component of a richer internal representation. Whether $M_t$ retains *enough* information is the subject of [Definition I.12](#model-sufficiency).

**Degenerate cases.** A PID controller's $M_t$ is degenerate — it retains only the error signal and its history (integral, derivative), with no predictive capability beyond extrapolating recent trends. It occupies the "blind pursuer" region of the agent spectrum ([Definition II.1](#agent-spectrum)): its $O_t$ (setpoint) is clear but its $M_t$ is too impoverished to support the adaptive dynamics of Section I. The formalism accommodates this by allowing $\mathcal{M}$ to range from trivial (scalar) to rich (full world model).


<a id="information-bottleneck"></a>

### Formulation I.11: *Information Bottleneck*

Optimal model compression balances retained history against predictive power; the information bottleneck objective provides a principled framework for understanding this trade-off.

#### Formal Expression

*[Formulation (IB-objective)]*

$$\phi^* = \arg\min_{\phi} \left[ I(M_t;\, \mathcal{C}_t) - \beta \cdot I(M_t;\, o_{t+1:\infty} \mid a_{t:\infty}) \right]$$

where:
- $I(M_t;\, \mathcal{C}_t)$ is the compression cost — how much of the interaction history the model retains
- $I(M_t;\, o_{t+1:\infty} \mid a_{t:\infty})$ is the predictive power — how much the model tells the agent about future observations given future actions
- $\beta \gt 0$ is the trade-off parameter controlling the compression-prediction balance

**Dependence on volatility.** The trade-off $\beta$ depends on environment volatility $\rho$:

- **Volatile environments** (high $\rho$): favor aggressive compression (low $\beta$). Old information decays in relevance quickly, so retaining it wastes capacity.
- **Stable environments** (low $\rho$): favor dense retention (high $\beta$). Historical information remains predictive, so discarding it loses value.

#### Epistemic Status

This is a *formulation* — it provides a principled framework for understanding compression trade-offs, not a claim about how actual agents compute their models. No agent explicitly solves this optimization (except in the variational IB literature, where it is a training objective). The formulation is analytically useful because it makes the compression-prediction trade-off explicit and connects model quality to information-theoretic quantities.

#### Discussion

**The IB framework is not prescriptive.** It characterizes what an optimal $\phi$ would look like, not how to find one. Actual agents approximate this trade-off through diverse mechanisms: forgetting, attention, abstraction, summarization.

**Connection to model sufficiency.** The IB objective implicitly defines when a model is "good enough": when the predictive power term $I(M_t;\, o_{t+1:\infty} \mid a_{t:\infty})$ is close to its maximum (the full history's predictive power). This is formalized in [Definition I.12](#model-sufficiency).

**Broader applicability.** The same IB principle applies beyond intra-agent compression. It governs inter-agent communication ([Definition III.5](#shared-intent)) — how much of one agent's model or strategy to transmit to another — and constrains the cognitive cost of maintaining a complex strategy. In each case, the trade-off is between the cost of retaining or transmitting information and the value of that information for future decisions.


<a id="model-sufficiency"></a>

### Definition I.12: *Model Sufficiency*

The fraction of predictive information the model retains relative to the full interaction history; $S = 1$ means the model is a sufficient statistic for prediction, $S \lt 1$ means predictive information has been lost.

#### Formal Expression

*[Definition (model-sufficiency)]*

$$S(M_t) = 1 - \frac{I(\mathcal{C}_t;\, o_{t+1:\infty} \mid M_t,\, a_{t:\infty})}{I(\mathcal{C}_t;\, o_{t+1:\infty} \mid a_{t:\infty})}$$

where:
- The numerator $I(\mathcal C_t;\, o_{t+1:\infty} \mid M_t,\, a_{t:\infty})$ is the predictive information that the full history $\mathcal C_t$ carries about the future *beyond* what $M_t$ already captures — the information lost by compression
- The denominator $I(\mathcal C_t;\, o_{t+1:\infty} \mid a_{t:\infty})$ is the total predictive information in the full history

**Boundary values:**
- $S(M_t) = 1$: $M_t$ is a sufficient statistic — it captures all predictive information in $\mathcal C_t$. Knowing the full history beyond $M_t$ adds nothing.
- $S(M_t) = 0$: $M_t$ retains no predictive information. The model is useless for prediction.
- $0 \lt S(M_t) \lt 1$: partial sufficiency — some predictive information is retained, some lost.

#### Epistemic Status

This is *definitional* — it names and formalizes a quantity. The definition is well-grounded in information theory (conditional mutual information ratios are standard). No substantive claim is made here about what value $S(M_t)$ takes or what happens when it is low; those claims belong to [Definition I.13](#model-class-fitness) and [Result I.26](#structural-adaptation-necessity).

#### Discussion

**Sufficiency is relative to the prediction task.** $S(M_t)$ measures sufficiency for predicting future observations given future actions. A model that is sufficient for one prediction horizon may be insufficient for another. The infinite-horizon formulation ($o_{t+1:\infty}$) is the most demanding; practical sufficiency over finite horizons may be easier to achieve.

**Sufficiency vs. accuracy.** A model can be sufficient ($S = 1$) while being wrong in absolute terms — if the full history is also wrong (e.g., systematically biased observations). Sufficiency measures information retention, not truth. The mismatch signal ([Definition I.17](#mismatch-signal)) measures accuracy; sufficiency measures completeness of compression.


<a id="model-class-fitness"></a>

### Definition I.13: *Model Class Fitness*

The best achievable sufficiency within a model class. When no model in the class can adequately represent reality, the agent faces a structural limitation that no amount of parameter tuning can resolve.

#### Formal Expression

*[Definition (model-class-fitness)]*

$$\mathcal{F}(\mathcal{M}) = \sup_{M \in \mathcal{M}} S(M)$$

where $\mathcal{M}$ is the model class — the set of all models the agent can represent given its current architecture, parameterization, or capacity.

**Structural inadequacy condition:**

$$\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$$

When this holds, no model $M \in \mathcal{M}$ achieves sufficiency above $1 - \varepsilon$. The gap is structural: it cannot be closed by better parameter estimation, more data, or longer training within the current class. This is the trigger for structural change ([Result I.26](#structural-adaptation-necessity)).

#### Epistemic Status

This is *definitional* — it names the supremum of sufficiency over a model class. The definition itself is straightforward. The substantive claim about what happens when $\mathcal{F}(\mathcal{M})$ is low — that parametric updates cannot close the mismatch floor and structural adaptation becomes necessary — is developed in [Result I.26](#structural-adaptation-necessity).

#### Discussion

**Model class vs. model instance.** $S(M_t)$ measures a specific model's sufficiency at time $t$. $\mathcal{F}(\mathcal{M})$ measures the ceiling of the entire class. A low $S(M_t)$ might mean the agent needs more learning (parameter update). A low $\mathcal{F}(\mathcal{M})$ means the agent needs a different kind of model (structural change). The distinction parallels bias vs. variance: class fitness is about bias; instance sufficiency reflects both bias and estimation quality.

**Detecting low class fitness.** The agent cannot directly compute $\mathcal{F}(\mathcal{M})$ — it would need to search over all models in the class. Instead, persistent mismatch despite adequate learning (high gain, sufficient data, converged parameters) is the observable signature. This connects to the mismatch floor in [Result I.26](#structural-adaptation-necessity).


<a id="event-driven-dynamics"></a>

### Formulation I.14: *Event-Driven Dynamics*

The coupling between agent and environment occurs through discrete events — observations arriving and actions completing — at potentially variable and heterogeneous rates. Discrete-time notation is the special case of uniform-interval events on a single channel.

#### Formal Expression

*[Formulation (event-driven-dynamics)]*

**Event** ($e$): An atomic unit of agent-environment interaction, typed as:
- **Observation event**: $e = (\text{obs}, k, o^{(k)})$ — a datum arriving on observation channel $k$
- **Action completion**: $e = (\text{act}, j, r^{(j)})$ — the result of action $j$ completing

**Event stream** ($\mathcal{E}$): The temporally ordered sequence of all events:

$$\mathcal{E} = \{(e_1, \tau_1), (e_2, \tau_2), \ldots\} \quad \text{where } \tau_1 \leq \tau_2 \leq \cdots$$

**Channel rate** ($\nu^{(k)}$): The characteristic event rate of channel $k$, which may vary over time.

**Event information content**: The mutual information between the event and the environment state, conditioned on the current model:

*[Definition (event-information-content)]*

$$\mathcal{I}(e_\tau) = I(e_\tau;\, \Omega_\tau \mid M_{\tau^-})$$

An event that the model already predicts carries little information ($\mathcal{I} \approx 0$). An event that surprises the model carries much ($\mathcal{I} \gg 0$). This connects directly to the mismatch signal ([Definition I.17](#mismatch-signal)).

**Channel-specific observation uncertainty**:

*[Definition (channel-uncertainty)]*

$$U_o^{(k)} = \text{observation uncertainty of channel } k$$

Different channels have different noise characteristics. A noisy channel (high $U_o^{(k)}$) provides lower-quality information per event. The update gain ([Empirical I.19](#update-gain)) should weight channels accordingly.

#### Epistemic Status

This is a *formulation choice*, not a postulate. The event-driven representation extends [Postulate I.7](#causal-structure)'s recursive update to heterogeneous, asynchronous multi-channel interactions. The discrete-time form ($M_t = f(M_{t-1}, o_t, a_{t-1})$) from [Derived I.15](#recursive-update) is a special case sufficient for many formal analyses — the event-driven formulation is needed only when multi-rate or asynchronous channels matter.

#### Discussion

**Why events rather than clock ticks.** The discrete-time notation $M_t = f(M_{t-1}, o_t, a_{t-1})$ presupposes a single clock synchronizing observations and actions. Real agents face:

- **Multiple observation channels** at different rates (a robot's camera at 30Hz, LIDAR at 10Hz, GPS at 1Hz; a human's vision, audition, proprioception; a developer's compiler output, test results, and production telemetry)
- **Multiple action channels** with different latencies (a robot's wheel motors vs. arm actuators; an organization's operational decisions vs. strategic pivots)
- **Asynchronous arrival** — observations not synchronized with each other or with action completions

The event-driven formulation handles all of these naturally. The discrete-time form is the special case where a single observation and a single action alternate at a fixed rate.

**The effective adaptation rate.** The agent's overall capacity to track environmental changes is the sum of information gained across all channels per unit time:

$$\nu_{\text{eff}} = \sum_k \nu^{(k)} \cdot \eta^{(k)*}$$

This quantity — identical to adaptive tempo $\mathcal{T}$ ([Definition I.21](#adaptive-tempo)) — is the central measure of an agent's adaptive fitness.

**Software-specific channels.** In the software development domain, the event-driven formulation maps naturally to the developer's multi-rate observation channels:

| Channel $k$ | Rate $\nu^{(k)}$ | Noise $U_o^{(k)}$ |
|-------------|------------------|-------------------|
| Compiler/linter output | Per-save (high) | Very low |
| Unit test results | Per-run (medium) | Low |
| CI pipeline | Per-push (medium) | Low |
| Runtime telemetry | Continuous (variable) | Medium |
| Bug reports | Sporadic (low) | High |
| Code review feedback | Per-PR (low) | Medium-high |

The three-part tempo decomposition for software — $\mathcal T_{\text{obs}}$ (compiler, tests) + $\mathcal T_{\text{explore}}$ (code reading) + $\mathcal T_{\text{probe}}$ (test runs, staging) — is a direct application of multi-channel tempo. This decomposition is a Section IV gap (see the three-part tempo decomposition gap in `ACT-FULL.md`).

**(Descended from TF-04.)**


<a id="recursive-update"></a>

### Derived I.15: *Recursive Update*

Agent state updates must be recursive: the new model state is a function of the previous model state and the incoming event, not of the full interaction history. For finite agents this is computational necessity; for agents with unlimited computation it is the natural structure imposed by temporal ordering.

#### Formal Expression

*[Derived (recursive-update, from temporal postulate and $M_t$ completeness)]*

**Event-driven update:**

$$M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$$

where:
- $M_{\tau^-}$ is the model state immediately before event $e_\tau$
- $M_{\tau^+}$ is the model state immediately after
- $f_M$ is the update function — it takes the current model and the new event, not the full history $\mathcal C_t$

**Between-event evolution:**

$$\frac{dM}{d\tau} = g_M(M_\tau)$$

Between events, the model evolves autonomously — internal reorganization, prediction generation, decay of transient states. The between-event dynamics depend only on the current model state, not on external input (which, by definition, arrives only at events).

#### Epistemic Status

*Exact* under the assumption that $M_t$ is the complete epistemic substate ([Formulation I.10](#agent-model)). If $M_t$ contains everything the agent retains from its history, then the update function needs only $M_t$ and the new event $e_\tau$ to produce $M_{t+1}$. The full history $\mathcal C_t$ is already summarized in $M_t$ by construction. For finite agents, recursion is *computational necessity*: re-processing the entire history at each event is infeasible. For agents with unlimited computation (e.g., an oracle that could re-derive $M_t$ from $\mathcal C_t$ at each step), recursion is still the natural structure but not strictly forced — the oracle could equivalently compute $\phi(\mathcal C_t \cup \{e_\tau\})$ directly. The unlimited-computation case is *discussion-grade*.

#### Discussion

**Recursion as a consequence of completeness.** The recursive form is not an assumption bolted on — it follows from the definition of $M_t$ as complete. If $M_t$ were incomplete (if some relevant information lived outside $M_t$ in the raw history), then $f_M(M_{\tau^-}, e_\tau)$ would be insufficient and the agent would need to consult $\mathcal C_t$ directly. The sufficiency of the recursive form is precisely what [Definition I.12](#model-sufficiency) measures: when $S(M_t) = 1$, the recursive update loses nothing.

**Between-event dynamics matter.** The autonomous evolution $g_M(M_\tau)$ is not merely filler between observations. It includes prediction generation (what the agent expects to see next), uncertainty growth (model confidence decaying over time without new data), and internal reorganization (consolidation, abstraction). In event-driven systems ([Formulation I.14](#event-driven-dynamics)), the between-event interval is variable, making $g_M$ load-bearing for agents that must act or predict between observations.

**Connection to the update gain.** The event-driven update $f_M(M_{\tau^-}, e_\tau)$ is where the gain principle ([Empirical I.19](#update-gain)) operates: $\eta^\ast$ determines how strongly $e_\tau$ shifts $M_t$ away from its prior value. The recursive form makes the gain's role explicit — it modulates the single-step correction.


<a id="action-selection"></a>

### Derived I.16: *Action Selection*

Action is a function of the model. The model's role is not merely to represent the environment but to generate actions — either implicitly (from internalized patterns) or through explicit deliberation. The degree to which effective action flows from the model without deliberative computation is *action fluency*.

#### Formal Expression

*[Derived (action-selection, from agent-model completeness)]*

$$a_t = \pi(M_t) \quad \text{(deterministic)}$$

$$a_t \sim \pi(\cdot \mid M_t) \quad \text{(stochastic)}$$

where $\pi$ is the agent's **policy** — the mapping from model state to action.

This is not imposed on the system but follows from [Formulation I.10](#agent-model): $M_t$ is the agent's compressed history, and action depends on what the agent "knows" — i.e., on $M_t$. Any deterministic or stochastic dependence of action on history *through* the model is captured by $\pi(M_t)$.

#### Epistemic Status

*Derived* from [Formulation I.10](#agent-model)'s completeness commitment. If $M_t$ is the agent's complete internal state (by definition), then action — which depends on internal state — is a function of $M_t$. The implicit/explicit distinction and action fluency concept are *discussion-grade* — qualitative properties that follow from the formalism but are not formally derived as propositions.

#### Discussion

**Implicit vs. explicit action selection.** A critical distinction emerges from the agent's *action fluency* — the degree to which effective action flows from the model without deliberative computation:

**Implicit (model-embedded):** When $\pi(M_t)$ can be evaluated cheaply — the model has internalized effective action-selection for the current situation. This is Boyd's implicit guidance and control (Orient→Act, bypassing Decide), a trained RL policy in exploitation mode, a well-tuned PID controller, expert intuition (System 1), a martial artist's trained reflexes, an organization's standard operating procedures.

**Explicit (deliberative):** When the situation is novel, the action space is large, or the stakes demand verification — the agent engages in internal simulation, using the model to predict outcomes of candidate actions before selecting. This is Boyd's explicit Decide step, MCTS/planning in RL, Model Predictive Control, human deliberate reasoning (System 2), organizational strategic planning. Deliberation requires at minimum Level 2 epistemic access ([Definition I.8](#pearl-causal-hierarchy)) — the agent uses its model to simulate "what will I observe if I $do(a)$?" across candidates.

**Formal characterization of action fluency.** An agent has *high fluency* for a situation when additional deliberation yields negligible improvement — formally, when $\Delta\eta^\ast(\Delta\tau) \approx 0$ for all $\Delta\tau \gt 0$ (see [Derived I.23](#deliberation-cost)). Conversely, *low fluency* means deliberation significantly improves action quality. Fluency is the degree to which the agent's immediate (zero-deliberation) action approaches the quality achievable with unbounded deliberation.

**Action fluency is distinct from model sufficiency.** An agent can have high $S(M_t)$ ([Definition I.12](#model-sufficiency)) but low fluency — a chess engine with a perfect model of the rules still requires expensive search. Conversely, an agent can have moderate sufficiency but high fluency in a narrow domain — a reflex that responds effectively to specific situations it evolved for. What reflexes, muscle memory, intuition, and expertise share is that the *action-generating capacity itself* has been absorbed into the model's structure: the model doesn't just predict well, it *acts* well, cheaply.

**Structural pressure toward implicit action.** When two action-selection modes produce equivalent expected outcomes, the faster mode is strictly preferable ([Postulate I.1](#temporal-optimality)). This creates a pressure: agents under selective pressure (evolution, competition, training) tend to internalize frequently-needed action patterns, converting explicit deliberation into implicit fluency. The pressure is stronger when $\rho$ is high (fast-changing environments penalize deliberation — see [Derived I.23](#deliberation-cost)), the pattern recurs frequently, or $\mathcal{T}$ is near the persistence threshold ([Result I.24](#persistence-condition)) with no slack for deliberation overhead.

However, deliberation remains essential when the situation is genuinely novel, the action space is large relative to model capacity (chess, strategic planning), the stakes are asymmetric (cost of error vastly exceeds cost of delay), or $\rho$ is low (stable environment allows deliberation without mismatch accumulation).

**Connection to Section II.** For actuated agents ([Definition II.1](#agent-spectrum)), action selection involves not just $M_t$ but also $G_t = (O_t, \Sigma_t)$ — the purposeful substate. The policy becomes $\pi(M_t, G_t)$, coupling all substates through action ([Derived II.12](#directed-separation)). The action-deliberation-exploration tradeoff (Section II gap) extends the implicit/explicit distinction to three modes: exploit (pursue $O_t$ via $\Sigma_t$), explore (improve $M_t$), deliberate (revise $\Sigma_t$).

**Domain instantiations:**

| Domain | Implicit action | Explicit deliberation |
|--------|----------------|----------------------|
| Kalman + LQR | LQR control law from $\hat{x}_t$ | — (separation principle) |
| RL | Greedy policy $\arg\max Q(s,a)$ | MCTS, planning, rollouts |
| PID | $u = K_p e + K_i \int e + K_d \dot{e}$ | — (no deliberation) |
| Boyd's OODA | IG&C (Orient→Act) | Explicit Decide step |
| Organism | Reflexes, habits | Deliberate planning |
| Organization | Standard procedures | Strategic planning |
| Software developer | Known patterns, familiar code | Reading docs, analyzing alternatives |

**(Descended from TF-07.)**


<a id="mismatch-signal"></a>

### Definition I.17: *Mismatch Signal*

The discrepancy between the model's prediction and the actual observation — the fundamental error signal that drives all adaptation.

#### Formal Expression

*[Definition (mismatch-signal)]*

Given model $M_{t-1}$ and prior action $a_{t-1}$, the model generates a prediction:

$$\hat{o}_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$$

The **mismatch signal** (prediction error):

$$\delta_t = o_t - \hat{o}_t$$

This is the primary definition, used in the mismatch dynamics ([Result I.24](#persistence-condition), [Result I.25](#sector-condition-stability)) and in the decomposition ([Result I.18](#mismatch-decomposition)).

For models with probabilistic predictions, the mismatch generalizes to the **score-function mismatch**:

*[Definition (score-mismatch)]*

$$\tilde{\delta}_t = -\nabla_M \log P(o_t \mid M_{t-1}, a_{t-1})$$

which points in the direction the model should move to increase the likelihood of the actual observation. $\tilde{\delta}_t$ lives in the tangent space $T_M\mathcal{M}$, while $\delta_t$ lives in observation space $\mathcal{O}$. Under Gaussian models, they coincide up to scaling.

#### Epistemic Status

This is *definitional*. Given any model that predicts ([Formulation I.10](#agent-model)) and any observation that arrives ([Definition I.3](#observation-function)), their difference exists. The mismatch signal is not an additional assumption but a consequence of having a predictive model in an uncertain world. The score-function form is the natural generalization when $\mathcal{O}$ is not a vector space or when the model's predictive distribution is the natural object.

#### Discussion

**Units and normalization.** When $\delta_t$ is in physical units (meters, dollars), the $\Vert\delta\Vert$ that enters the mismatch dynamics should be understood as the Mahalanobis distance: $\Vert\delta_t\Vert_\Sigma = \sqrt{\delta_t^T \Sigma^{-1} \delta_t}$ where $\Sigma$ is the observation noise covariance. This maps physical prediction error to dimensionless surprise-equivalent units.

**The zero-mismatch ambiguity.** $\delta_t \approx 0$ does NOT necessarily indicate model adequacy. It may mean: (a) the model genuinely reflects reality — *desirable*; (b) the agent is only observing aspects its model already explains, while remaining ignorant of aspects where the model is wrong — *confirmation bias*; or (c) the observation channel is too noisy to detect model errors — *architectural limitation*. Only (a) is desirable. This ambiguity is why active testing — choosing actions to generate informative mismatch signals — can be valuable (see [Definition I.20](#causal-information-yield) for the CIY framework).

**The mismatch transform.** TF-06's update rule writes $M_t = M_{t-1} + \eta \cdot g(\delta_t)$, where the transform $g$ maps from $\delta_t$'s space to the model's update space: $g: \mathcal{O} \to T_M\mathcal{M}$ for prediction errors; $g: T_M\mathcal{M} \to T_M\mathcal{M}$ for score-function mismatches.


<a id="mismatch-decomposition"></a>

### Result I.18: *Mismatch Decomposition*

Expected squared mismatch decomposes into reducible model error and irreducible observation noise. The model can improve the first term; the second is a property of the channel.

#### Formal Expression

*[Derived (mismatch-decomposition, Prop 5.1 from TFT)]*

For any agent-environment pair within ACT's scope ([Scope I.5](#scope-condition)), when observation noise is non-degenerate or the model's predictive mean is misspecified:

$$\mathbb{E}[\Vert\delta_t\Vert^2] = \underbrace{\mathbb{E}[\Vert\hat{o}_t - \bar{o}_t\Vert^2]}_{\text{model error (reducible)}} + \underbrace{\mathbb{E}[\text{Var}(o_t \mid \Omega_t, a_{t-1})]}_{\text{observation noise (irreducible)}} \gt 0$$

where $\bar o_t = \mathbb{E}[o_t \mid \Omega_t, a_{t-1}]$ is the true conditional mean.

##### Derivation

1. By [Scope I.5](#scope-condition), $H(\Omega_t \mid \mathcal C_t) \gt 0$ — residual uncertainty persists.
2. By [Formulation I.10](#agent-model), the model generates predictions $\hat o_t = \mathbb{E}[o_t \mid M_{t-1}, a_{t-1}]$.
3. Decompose mismatch into model error and noise. The cross-term vanishes by the fresh-noise assumption: $\varepsilon_t$ is conditionally independent of $\mathcal C_{t-1}$ given $(\Omega_t, a_{t-1})$. Condition on $(\Omega_t, a_{t-1})$; then $\bar o_t - \hat o_t$ is fixed and $\mathbb{E}[o_t - \bar o_t \mid \Omega_t, a_{t-1}] = 0$ by definition of $\bar o_t$. The outer expectation gives zero. This is orthogonality (uncorrelated), not independence.
4. Term (ii) is positive when observation noise is non-degenerate. Term (i) is positive when the model's predictive mean differs from the true conditional mean. Either suffices.

#### Epistemic Status

*Exact* under the fresh-noise assumption (observation noise $\varepsilon_t$ conditionally independent of history given current state and action). This is the standard assumption in state-space models — noise is a property of the observation channel at the moment of observation. The decomposition is a mathematical identity (bias-variance decomposition applied to the prediction problem). The positivity of $\mathbb{E}[\Vert\delta_t\Vert^2]$ follows from either condition; both hold simultaneously in typical settings.

#### Discussion

**Reducible vs. irreducible.** An agent that tries to eliminate *all* mismatch — including irreducible noise — will overfit: adjusting its model to explain noise, degrading future predictions. The update gain ([Empirical I.19](#update-gain)) implicitly separates signal from noise by weighting observations in proportion to their informativeness.

**Connection to model sufficiency.** When $S(M_t) \lt 1$ ([Definition I.12](#model-sufficiency)), the model has lost predictive information relative to the full history. Under an alignment assumption (the lost information affects the one-step conditional mean), this implies positive model error (term i). Without that alignment assumption, insufficiency still implies positive regret under proper scoring rules but not necessarily positive one-step mean error.

**Mismatch is structurally persistent.** In realistic ACT regimes, mismatch signals persist — they can be reduced but not eliminated when observation noise is non-degenerate. Deterministic, noiseless, perfectly specified systems are limiting edge cases, not the typical adaptive regime.


<a id="update-gain"></a>

### Empirical I.19: *Update Gain*

The optimal weight an agent assigns to new observations when updating its model balances model uncertainty against observation noise.

#### Formal Expression

*[Empirical Claim (uncertainty-ratio-principle)]*

$$\eta^* = \frac{U_M}{U_M + U_o}$$

where:
- $\eta^\ast$ is the optimal update gain (proportion of mismatch used to correct the model)
- $U_M$ is model uncertainty (predictive variance or entropy)
- $U_o$ is irreducible observation noise

The update rule takes the form:

*[Formulation]*

$$M_t = M_{t-1} + \eta^* \cdot g(\delta_t)$$

where $\delta_t$ is the mismatch ([Definition I.17](#mismatch-signal)) and $g(\cdot)$ is a correction mapping from observation space to model update space.

#### Epistemic Status

*Exact* for linear-Gaussian systems (where $\eta^\ast$ is the Kalman gain) and conjugate Bayesian systems. For general adaptive systems (RL agents, organizational learning, biological adaptation), it is *robust qualitative* — any optimal adaptation process must approximate this functional dependence, even if the variance ratio is not explicitly computed.

#### Discussion

**Limiting behavior.** When $U_M \gg U_o$ (high model uncertainty — e.g., after initialization or structural adaptation), $\eta^\ast \to 1$: trust the observation. When $U_M \ll U_o$ (confident model, noisy channel), $\eta^\ast \to 0$: trust the model. The gain determines how strongly the agent corrects toward reality on each update.

**Gain collapse.** When the agent incorrectly estimates $U_M \to 0$ (spurious confidence) or $U_o \to \infty$ (spurious distrust of sensors), $\eta^\ast \to 0$ and the agent stops learning. Mismatches are ignored, producing confirmation bias or a decoupled reality model.

**Multi-dimensional generalization.** In vector-valued systems, $U_M$ and $U_o$ are covariance matrices and $\eta^\ast$ becomes a gain matrix (as in the Kalman filter). The scalar form captures the essential structure.

**Connection to adaptive tempo.** The update gain is one factor in the agent's adaptive tempo ([Definition I.21](#adaptive-tempo)): $\mathcal{T} = \nu \cdot \eta^\ast$. Updating frequently (high $\nu$) is useless if the updates extract no information (low $\eta^\ast$). Gain measures the *quality* of the update cycle; event rate measures its *speed*.

**Gain dynamics.** The optimal gain changes over time following predictable patterns:

- *Convergence*: As the model accumulates information, $U_M$ decreases, so $\eta^\ast \to 0$. The model becomes increasingly resistant to individual observations. This IS Kalman filter convergence, Bayesian posterior concentration, and RL learning rate annealing.
- *Reset after structural change*: When the environment changes in ways the model cannot track incrementally ([Result I.26](#structural-adaptation-necessity)), $U_M$ should spike — the model "admits" its uncertainty. The gain increases, enabling rapid re-learning. An agent whose gain does NOT reset after structural change will continue trusting a stale model — Boyd's "incestuous amplification" and the cause of brittle failure in non-stationary environments.

**Overfitting as gain miscalibration.** From [Result I.18](#mismatch-decomposition): $\mathbb{E}[\Vert\delta_t\Vert^2]$ = model error + irreducible noise. An agent with $\eta$ too high adjusts its model to explain observation noise, increasing model error on future predictions. An agent with $\eta$ too low fails to correct genuine model errors. The optimal gain implicitly separates signal from noise by weighting observations in proportion to their informativeness — exactly what $U_M/(U_M + U_o)$ achieves when $U_o$ captures the irreducible noise.

**Representation note.** The additive form operates in a *representation space* appropriate to the model. For Bayesian posteriors (where update is multiplicative: $P(\theta \mid D) \propto P(D \mid \theta) P(\theta)$), the additive rule operates in log-probability or natural parameter space. For models on constrained manifolds (probability simplices, rotation groups), the update must be projected onto the manifold. The claim is not that all updates are literally additive in native parameterization, but that they have the structure "current state + gain × transformed mismatch" in an appropriate coordinate system.

**Domain validation:**

| Domain | Gain form | Mapping quality |
|--------|-----------|-----------------|
| Kalman filter | $K_t = P_{t\Vertt-1} H^T (H P_{t\Vertt-1} H^T + R)^{-1}$ | **Exact.** Scalar case is exactly $U_M/(U_M + U_o)$. |
| Conjugate Bayesian | Posterior weight $n/(n + \kappa)$ cumulative; incremental $1/(n + \kappa)$ | **Exact** for conjugate families. Incremental gain decreases as data accumulates. |
| RL (Q-learning) | Fixed learning rate $\alpha$ | **Approximate.** $\alpha$ is a degenerate constant gain — does not adapt to uncertainty. Advanced methods (Bayesian RL, Adam) converge toward the optimal form. |
| PID control | Fixed gains $(K_p, K_i, K_d)$ | **Simplified.** Gains set at design time. Adaptive PID and MPC move toward the full framework. |
| Software developer | Implicit trust weighting of information sources | **Structural analogy.** New developer (high $U_M$) trusts observations heavily; experienced developer (low $U_M$) trusts their model. Gain reset after major refactoring. |

**Simulation validation.** Numerical experiments (track-b, Variant E) validated the uncertainty ratio principle under observation noise. Riccati-optimal gain reduced steady-state mismatch by 52% compared to fixed gain when observation noise was moderate. The optimal gain also proved critical in adversarial settings: under heavy observation noise, optimal gain preserved more than double the adversarial tempo advantage exponent (0.40 vs 0.18) compared to fixed gain.

**Open questions:**

1. *Non-parametric models*: For neural networks without well-defined scalar $U_M$, how should it be computed? Ensemble methods, dropout-based uncertainty, and Bayesian neural networks are all approximations.
2. *Matrix vs scalar gain*: In high-dimensional systems, the gain is a matrix (Kalman) or per-parameter (Adam). The cross-dimensional structure (covariance) adds complexity. The scalar captures the principle; the matrix captures the full optimization.

**(Descended from TF-06.)**


<a id="causal-information-yield"></a>

### Definition I.20: *Causal Information Yield*

Actions don't merely select among outcomes — they generate information about how the environment responds to interventions. Causal information yield (CIY) quantifies this: how much an action reveals about causal structure that passive observation cannot provide.

#### Formal Expression

*[Definition (causal-information-yield)]*

The **canonical CIY** of action $a$ given model state $M$:

$$\text{CIY}(a;\, M) = \mathbb{E}_{a' \sim q(\cdot \mid M)}\!\left[D_{\mathrm{KL}}\!\left(P(o \mid do(a), M) \,\Vert\, P(o \mid do(a'), M)\right)\right]$$

where $q(\cdot \mid M)$ is a reference distribution over comparator actions (uniform, policy-induced, or task-specific). This measures how strongly the action changes the interventional distribution of outcomes relative to alternatives.

$\text{CIY} \geq 0$ by construction (expectation of KL divergences). $\text{CIY} = 0$ for a passive observer or an agent whose actions don't affect outcome distributions. $\text{CIY} \gt 0$ when actions causally alter what is observed — exactly what distinguishes Level 2 from Level 1 epistemic access ([Definition I.8](#pearl-causal-hierarchy)).

**Observational proxy** (for diagnostic use with observational statistics):

*[Definition (ciy-proxy)]*

$$\text{CIY}_{\text{proxy}}(a_{t-1}) = I(o_t; a_{t-1} \mid M_{t-1}) - I(o_t; a_{t-1} \mid \Omega_t, M_{t-1})$$

This proxy is sign-indefinite in general and requires causal assumptions for interpretation. The canonical CIY (interventional) is the primary quantity; the proxy is auxiliary.

#### Epistemic Status

The CIY *definition* is well-grounded in causal inference theory. The *structural claim* — that the optimal policy jointly maximizes value and causal information — is *discussion-grade*, supported by convergent results in Bayesian RL, active inference, and information-directed sampling, but not derived from first principles within ACT. The specific form of $\lambda(M_t)$ (the exploration-exploitation balance weight) is not derived. See discussion of the unified policy objective below.

#### Discussion

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

**Query actions: accessing external models.** A qualitatively distinct class of actions: querying another agent's model. When a reliable source exists (expert, database, documentation, well-trained LLM), "ask a well-formed question" can yield information equivalent to thousands of probe-observe cycles. The source's model has already performed the compression work ([Formulation I.11](#information-bottleneck)) — the response transfers the *output* of compression rather than requiring the agent to reconstruct it.

Key properties of query actions:
- **Information density**: Single well-targeted query can carry CIY orders of magnitude higher than individual environment probes
- **Trust-dependent gain**: Update from query depends on the agent's model of the source's reliability and alignment, not on observation channel noise ([Hypothesis III.9](#communication-gain))
- **Pre-compressed information**: Responses arrive already compressed in the source's representational framework, introducing a translation cost when frameworks don't align
- **Structural adaptation via external models**: Encountering another agent's model can trigger structural change ([Result I.26](#structural-adaptation-necessity)) — incorporating external representational structure rather than building it de novo ("grafting")

When high-CIY query channels are available, the unified policy objective favors query actions over direct probes, particularly when $U_M$ is high, a trusted source exists, query cost is low, and the needed information is about *structure* rather than the agent's specific situation.

**The adversarial mirror: deception and model corruption.** The same channel that enables cooperative knowledge transfer can be exploited to degrade the opponent's model. A deceptive response yields positive CIY in the strict information-theoretic sense, but the content drives model-reality mismatch *upward*. The update gain $\eta^\ast$ for the victim depends on trust; successful deception exploits high trust to inject a large, misdirected update. In the Lyapunov framework ([Result I.25](#sector-condition-stability)), this is adversarial disturbance injected through the observation channel, with coupling coefficient $\gamma_A$ determined by the victim's trust level and exposure. See [Hypothesis III.9](#communication-gain) for the formal treatment of trust-dependent gain, and [Derived III.10](#adversarial-destabilization) for the Lyapunov formalization. Distributed tempo, topology analysis, and game-theoretic integration are Section III content not yet fully extracted (source material in `src/old-tf-appendix-f-multi-agent.md`).

**Connection to the zero-mismatch ambiguity.** An agent that only exploits (acts to maximize predicted value) will tend toward confirmation bias — observing only what its model already explains ([Definition I.17](#mismatch-signal), zero-mismatch ambiguity case (b)). Exploration via CIY-maximizing actions is the mechanism by which the agent actively tests its model.

**Connection to Section II.** For actuated agents, the exploration-exploitation tension extends to three modes: exploit (pursue $O_t$ via $\Sigma_t$), explore (improve $M_t$), deliberate (revise $\Sigma_t$). The CIY framework provides the information-theoretic grounding for why strategy edges ([Definition II.11](#strategy-dag)) need observational access ([Derived II.17](#observability-dominance)) — edges the agent cannot observe have frozen CIY.

**Connection to active inference.** The Free Energy Principle's "expected free energy" decomposes into extrinsic value (pragmatic) and epistemic value (information-seeking). ACT's formulation is structurally isomorphic: expected value ≈ extrinsic, CIY ≈ epistemic. Whether this convergence is deep or superficial is an open question. ACT grounds exploration in explicitly *causal* information rather than entropy reduction — not all uncertainty reduction is equally valuable; causal information specifically enables better *intervention*.

**Identifiability gate.** Before incorporating CIY into policy objectives: (1) action variation must exist, (2) admissibility regime must be identified, (3) reference distribution $q$ must be specified, (4) local stationarity must hold. If any condition fails, CIY-based terms should be dropped or replaced with simpler uncertainty-based heuristics (UCB-style bonuses, ensemble disagreement).

**(Descended from TF-08.)**


<a id="adaptive-tempo"></a>

### Definition I.21: *Adaptive Tempo*

The effective rate at which an agent acquires useful information from its environment — the product of observation frequency and update quality across all channels.

#### Formal Expression

*[Definition (adaptive-tempo)]*

$$\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)*}$$

where:
- $k$ indexes the agent's distinct observation channels
- $\nu^{(k)}$ is the event rate on channel $k$
- $\eta^{(k)\ast}$ is the optimal update gain on channel $k$ ([Empirical I.19](#update-gain))

Single-channel special case: $\mathcal{T} = \nu \cdot \eta^\ast$.

#### Epistemic Status

This is a *definition*. It names the quantity that characterizes an agent's total corrective capacity, combining loop speed ($\nu$) and epistemic quality ($\eta^\ast$). The definition itself is not a truth-claim; the substantive claims are in the results that use it ([Result I.24](#persistence-condition), [Result III.8](#adversarial-tempo-advantage)).

#### Discussion

**Speed-quality substitutability.** An agent can achieve the same tempo via a fast noisy loop (high $\nu$, low $\eta^\ast$) or a slower calibrated one (low $\nu$, high $\eta^\ast$). The product structure means improvements to *both* factors compound multiplicatively.

**Observation noise gating.** Because $\eta^\ast = U_M / (U_M + U_o)$, high observation noise ($U_o$) depresses gain and collapses tempo regardless of loop speed. You cannot outrun a bad observation channel by iterating faster. This grounds Boyd's emphasis on Orient quality over raw OODA speed.

**Centrality.** Tempo is ACT's core capacity metric. It appears on the left side of the persistence condition ([Result I.24](#persistence-condition)), determines adversarial advantage ([Result III.8](#adversarial-tempo-advantage)), and connects to code quality as observation infrastructure ([Discussion IV.11](#code-quality-as-observation-infrastructure)) in the software domain.

**Temporal nesting.** Adaptive processes stratify by timescale, with convergence constraints between levels ([Derived I.27](#temporal-nesting)).

**Mismatch dynamics.** The evolution of mismatch over time is governed by the balance between correction (via tempo) and disturbance ($\rho$) ([Hypothesis I.22](#mismatch-dynamics)).

**Scalar vs. vector tempo.** The scalar $\mathcal{T}$ assumes isotropic correction capacity. When the agent corrects some dimensions faster than others, scalar tempo overestimates effective adaptation along weak dimensions. Simulation confirms: in an anisotropic 3D system (gain varying 5:1), scalar $\rho/\mathcal{T}$ overestimated by 72%, with the weak dimension accounting for 84% of total mismatch. The correct formulation is per-dimension: $\mathcal{T}_k \gt \rho_k / \delta_{\text{critical},k}$ ([Result III.13](#per-dimension-persistence)).

**(Descended from TF-11.)**


<a id="mismatch-dynamics"></a>

### Hypothesis I.22: *Mismatch Dynamics*

The evolution of model-reality mismatch over time is governed by the balance between the agent's corrective capacity (tempo) and the rate of environmental change (disturbance). The linear ODE is a first-order approximation; the general nonlinear case is handled by the sector-condition framework ([Result I.25](#sector-condition-stability)).

#### Formal Expression

*[Hypothesis (mismatch-dynamics)]*

$$\frac{d\Vert\delta\Vert}{dt} = -\mathcal{T} \cdot \Vert\delta\Vert + \rho(t)$$

where:
- $\mathcal{T} \cdot \Vert\delta\Vert$ is the rate at which the agent corrects mismatch (proportional to both tempo and current mismatch)
- $\rho(t)$ is the **environment change rate** — the rate at which new mismatch is introduced by changes in $\Omega$

**Steady state** ($d\Vert\delta\Vert/dt = 0$):

*[Derived (from linear hypothesis)]*

$$\Vert\delta\Vert_{ss} = \frac{\rho}{\mathcal{T}}$$

Steady-state mismatch is the ratio of how fast the environment changes to how fast the agent adapts.

**Transient solution:**

$$\Vert\delta(t)\Vert = \Vert\delta_0\Vert e^{-\mathcal{T} t} + \frac{\rho}{\mathcal{T}}(1 - e^{-\mathcal{T} t})$$

Mismatch decays exponentially from initial conditions toward the steady state.

#### Epistemic Status

*Heuristic.* This is explicitly a first-order linear approximation. The qualitative behavior (bounded mismatch, steady-state ratio, exponential convergence) is robust across correction function forms. The quantitative predictions (exact steady-state value, convergence rate, the squared adversarial scaling law) are specific to the linear case. The general nonlinear treatment ([Result I.25](#sector-condition-stability)) replaces the linear correction term with a sector-bounded correction function and proves persistence without committing to a specific functional form.

**Bridging assumption (discrete to continuous).** This ODE is a fluid-limit approximation of the discrete event-driven dynamics ([Formulation I.14](#event-driven-dynamics)). Valid when $\eta^\ast \ll 1$ (the small-gain regime — each event makes a small correction). Least accurate during initial transients when $\eta^\ast$ is large, but this phase is short-lived.

#### Discussion

**Speed-quality substitutability.** From $\mathcal{T} = \nu \cdot \eta^\ast$ (single-channel case): doubling event rate $\nu$ has the same effect on $\Vert\delta\Vert_{ss}$ as doubling update quality $\eta^\ast$. They are multiplicative when both improve: 50% improvement in each yields $1.5 \times 1.5 = 2.25\times$, not $3\times$. This is the formal analog of Boyd's insight that Orient quality often matters more than raw OODA speed — the same structural observation (quality and speed are substitutable, quality often dominates) appears in the model.

**The persistence threshold.** From the steady-state: $\Vert\delta\Vert_{ss} \lt \Vert\delta_{\text{critical}}\Vert$ iff $\mathcal{T} \gt \rho/\Vert\delta_{\text{critical}}\Vert$ ([Result I.24](#persistence-condition)). Below this threshold, the model cannot support effective action. The same structural pattern — correction capacity falling below disturbance rate — appears across domains: extinction (environment changes faster than organism adapts), organizational failure (market moves faster than company learns), control instability (disturbances exceed correction capacity), cognitive overload (information arrives faster than processing). The persistence condition captures the common structure; whether it captures the dominant mechanism in each domain is an empirical question.

**Nonlinear reality.** The true correction dynamics are almost certainly nonlinear:
- *Saturation at large $\Vert\delta\Vert$*: correction mechanism overwhelmed, so correction is slower than linear for large errors. Makes the persistence threshold harder to satisfy.
- *Threshold effects*: small mismatches go uncorrected ($F \approx 0$ for $\Vert\delta\Vert \lt \varepsilon$), creating a dead zone.
- *Structural breakdown*: beyond some critical $\Vert\delta\Vert$, correction drops to zero because the model class is no longer appropriate ([Result I.26](#structural-adaptation-necessity)).

These nonlinearities are exactly what the sector-condition framework ([Result I.25](#sector-condition-stability)) handles.

**Adversarial coupling.** When two agents are coupled ($A$'s actions increase $B$'s $\rho$): $\rho_B = \rho_{B,\text{base}} + \gamma_A \cdot \mathcal T_A$. Under linear dynamics with coupling-dominant disturbance, steady-state mismatch ratios scale as $(\mathcal T_A/\mathcal T_B)^2$ (Cor. 11.2 from TFT — heuristic, confirmed by simulation at exponent 1.999 under deterministic drift). Under stochastic disturbances, the exponent is 3/2, not 2. See [Result III.8](#adversarial-tempo-advantage).

**(Descended from TF-11.)**


<a id="deliberation-cost"></a>

### Derived I.23: *Deliberation Cost*

Explicit deliberation improves action quality by using the model for internal simulation before acting. But deliberation takes time — and during that time, the environment continues to evolve. Deliberation is justified when the improvement exceeds the mismatch accumulated during the pause.

#### Formal Expression

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

##### Derivation

1. Without deliberation, the agent acts immediately at current tempo $\mathcal{T}_0 = \nu \cdot \eta^\ast_0$.
2. With deliberation of duration $\Delta\tau$, the agent pauses, then acts with improved gain $\eta^\ast_0 + \Delta\eta^\ast$. But during the pause, mismatch has grown by $\rho_{\text{delib}} \cdot \Delta\tau$.
3. The net mismatch reduction from acting after deliberation versus acting immediately: $\text{Net} = \Delta\eta^\ast \cdot \Vert\delta_{\text{post}}\Vert - \rho_{\text{delib}} \cdot \Delta\tau$.
4. Deliberation is justified iff $\text{Net} \gt 0$. $\square$

**Optimal deliberation duration** (under diminishing returns):

*[Derived (Conditional on diminishing-returns + deliberation-drift)]*

$$\Delta\tau^* = \arg\max_{\Delta\tau} \left[\Delta\eta^*(\Delta\tau) \cdot \Vert\delta_{\text{post}}\Vert - \rho_{\text{delib}} \cdot \Delta\tau \right]$$

At the first-order condition: $\frac{\partial \Delta\eta^\ast}{\partial \Delta\tau} \cdot \Vert\delta_{\text{post}}\Vert = \rho_{\text{delib}}$. Stop deliberating when the marginal improvement rate drops below the mismatch drift rate (normalized by post-deliberation mismatch).

#### Epistemic Status

*Conditional* on the local deliberation-drift assumption. The threshold condition is derived given the assumption; the assumption itself is a local approximation validated by consistency with the global mismatch dynamics ([Result I.24](#persistence-condition)). The result captures the *epistemic* benefit of deliberation (improving $\eta^\ast$); in practice, deliberation also provides a direct *action-value* benefit (choosing better actions that alter the environment trajectory), which operates through $\rho$ reduction and immediate reward — a fuller formalization would incorporate the unified policy objective ([Definition I.20](#causal-information-yield)) at significantly more complexity.

#### Discussion

**High-$\rho_{\text{delib}}$ environments penalize deliberation.** When the environment changes rapidly during pause windows, the cost term grows quickly. Only very short deliberation with large $\Delta\eta^\ast$ can justify the pause. The model captures the same tradeoff Boyd emphasized: in fast-tempo adversarial environments, over-deliberation is fatal not because thinking is bad, but because the environment moves during the thinking. Whether the specific mechanism (mismatch drift during pause) is the dominant real-world effect is an empirical question.

**Diminishing returns.** In most models, $\Delta\eta^\ast(\Delta\tau)$ exhibits diminishing returns — the first moments of simulation yield the largest improvement. Combined with the linear cost $\rho_{\text{delib}} \cdot \Delta\tau$, this implies a finite optimal deliberation duration. Past that point, additional thinking is net-harmful.

**Implicit action as the high-tempo limit.** As $\rho_{\text{delib}} \to \infty$ or $\Delta\tau^\ast \to 0$: the optimal strategy converges to zero deliberation — pure implicit action ([Derived I.16](#action-selection)). This provides a mathematical basis for why high-tempo environments favor action fluency: the cost of deliberation exceeds its benefit when $\Delta\eta^\ast$ is small (action-selection is already fluent) or $\rho_{\text{delib}}$ is large.

**Deliberation as an investment.** When $\rho_{\text{delib}}$ is low (stable environment) or $\Vert\delta_{\text{post}}\Vert$ is large (significant model-reality gap), deliberation pays off. The conditions favoring deliberation — stable environment, large mismatch — resemble the high-stakes, low-urgency scenarios where deliberative reasoning (System 2) is advantageous in dual-process theories. The structural parallel is suggestive; whether the cost-benefit mechanism is the same one governing System 1/System 2 selection is an open question.

**The circularity of $\Vert\delta_{\text{post}}\Vert$.** Evaluating the threshold requires the agent to *predict* post-deliberation mismatch using its current model — the same model deliberation is meant to improve. This circularity is typically benign: $\Vert\delta_{\text{post}}\Vert$ is bounded below by $\rho_{\text{delib}} \cdot \Delta\tau$ and above by current mismatch plus that accumulation. An agent that underestimates its mismatch will under-deliberate; one that overestimates will over-deliberate. The bias is self-correcting through the feedback loop. The threshold is best understood as a *design criterion*, not a real-time decision procedure.

**Resource costs beyond time.** Real agents also incur computational and energetic costs: internal simulation burns calories, compute cycles, or opportunity cost of not processing new observations. These are additive: $\Delta\eta^\ast(\Delta\tau) \cdot \Vert\delta_{\text{post}}\Vert \gt \rho_{\text{delib}} \cdot \Delta\tau + C(\Delta\tau)$. In high-$\rho_{\text{delib}}$ environments the temporal cost dominates; in low-$\rho_{\text{delib}}$ environments, resource costs may be the binding constraint.

**Structural adaptation as massive deliberation.** Structural adaptation ([Result I.26](#structural-adaptation-necessity)) can be understood as deliberation with a massive $\Delta\tau$. During decomposition-and-recombination, the agent's high-frequency parametric loop is partially or fully suspended while it searches for a new model class. The mismatch debt $\rho_{\text{delib}} \cdot \Delta\tau$ is enormous (weeks/months for organizational restructuring). The agent rationally resists structural adaptation until the parametric mismatch floor exceeds this debt.

**Connection to temporal nesting.** Deliberation is a nested loop: internal simulation running at rate $\nu_{\text{internal}}$ within the external action loop at rate $\nu_{\text{external}}$. The convergence constraint applies: the internal loop must approximately converge before the external loop acts on its output.

**Connection to Section II.** For actuated agents, the deliberation tradeoff extends to three modes: exploit ($O_t$ via $\Sigma_t$), explore (improve $M_t$), and deliberate (revise $\Sigma_t$). The three-way allocation is the action-deliberation-exploration tradeoff identified as a Section II gap.

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

**(Descended from TF-09.)**


<a id="persistence-condition"></a>

### Result I.24: *Persistence Condition*

An agent maintains bounded mismatch — persists as a viable adaptive system — if and only if its adaptive tempo exceeds the rate of environment change relative to its tolerance threshold.

#### Formal Expression

*[Derived (persistence-threshold, from sector-condition analysis)]*

$$\mathcal{T} \gt \frac{\rho}{\Vert\delta_{\text{critical}}\Vert}$$

where:
- $\mathcal{T}$ is the adaptive tempo: $\sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$ ([Definition I.21](#adaptive-tempo))
- $\rho$ is the rate of environment change (rate of new mismatch introduction)
- $\delta_{\text{critical}}$ is the maximum tolerable mismatch magnitude

**Assumptions.** Bounded disturbance ($\Vert w(t)\Vert \leq \rho$, GA-2) and sector condition on the correction function (GA-3). See [Result I.25](#sector-condition-stability) for the general nonlinear treatment from which this threshold emerges.

##### Derivation

From the sector-condition analysis ([Result I.25](#sector-condition-stability)):

1. The correction function $F(\mathcal{T}, \delta)$ satisfies the sector bound:
   $\delta^T F \geq \alpha \Vert\delta\Vert^2$ for $\Vert\delta\Vert \leq R$.
2. The Lyapunov function $V(\delta) = \frac{1}{2}\Vert\delta\Vert^2$ satisfies:
   $\dot{V} \leq -\alpha\Vert\delta\Vert^2 + \rho\Vert\delta\Vert$
3. This gives $\dot{V} \lt 0$ when $\Vert\delta\Vert \gt \rho/\alpha$.
4. Ultimate bound: $\Vert\delta\Vert \leq R^\ast = \rho/\alpha$.
5. The agent persists (mismatch stays bounded within tolerance) when $R^\ast \lt \Vert\delta_{\text{critical}}\Vert$, i.e., $\alpha \gt \rho/\Vert\delta_{\text{critical}}\Vert$.

The full proof is in Appendix A (Prop A.1). $\square$

##### Per-Dimension Extension

*[Empirical Claim (per-dimension-persistence, from simulation variant F)]*

For anisotropic systems (non-uniform $\rho$ or $\mathcal{T}$ across dimensions), the scalar persistence condition is insufficient. Per-dimension:

$$\mathcal{T}_k \gt \frac{\rho_k}{\delta_{\text{critical},k}} \quad \text{for each dimension } k$$

The scalar condition overestimates by up to 72% in simulation. The weak dimension is the bottleneck (84% of total mismatch in simulation). See [Result III.13](#per-dimension-persistence).

**Robustness**: The per-dimension condition matches discrete AR(1) prediction to 4 significant figures. The scalar overestimate is a consequence of Jensen's inequality applied to the norm.

#### Epistemic Status

The threshold's *existence* is *robust qualitative* — any monotone correction function has a capacity limit; this holds across all correction functions tested (linear, saturating, threshold, sigmoid). The quantitative form $\mathcal{T} \gt \rho / \Vert\delta_{\text{critical}}\Vert$ is *exact* under the sector-condition assumptions (GA-2, GA-3; Prop A.1). The linear ODE gives the same threshold as a special case. The per-dimension extension is *empirically exact* (matches AR(1) prediction to 4 significant figures in simulation) but awaits formal derivation beyond the 1D case.

#### Discussion

**Below threshold.** When $\mathcal{T} \leq \rho / \Vert\delta_{\text{critical}}\Vert$, mismatch is not merely large — it grows without effective bound (up to $R$, the sector-condition region). The agent loses contact with reality. This is a qualitative transition, not a gradual degradation.

**Adaptive reserve.** The quantity $\Delta\rho^\ast = \alpha R - \rho$ (Prop A.2) measures how much additional disturbance the agent can absorb before persistence fails. Positive reserve means the agent has margin; zero reserve means it is at the threshold.

##### Connections

The persistence condition appears in multiple downstream contexts:

- **Adversarial dynamics** ([Result III.8](#adversarial-tempo-advantage)): Superlinear tempo advantage arises because persistence is a threshold — pushing an adversary below it causes qualitative collapse. *This connection is developed and validated in [Result III.8](#adversarial-tempo-advantage) and simulation variants A-D.*

- **Structural adaptation** ([Result I.26](#structural-adaptation-necessity)): When model class fitness $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$, the effective $\alpha$ in the sector condition shrinks, eventually violating persistence. *This connection is developed in [Result I.26](#structural-adaptation-necessity).*

- **Software maintainability** ([Discussion IV.11](#code-quality-as-observation-infrastructure)): *[Discussion]* A codebase may become "unmaintainable" when the development team's adaptive tempo falls below the rate of complexity accumulation. The vicious cycle would then be the persistence condition being violated through the agent's own prior actions degrading future $\mathcal{T}$ via $U_o$. *This connection is structurally motivated but not yet formally derived within ACT. It requires formalizing "complexity accumulation rate" as an instance of $\rho$.*


<a id="sector-condition-stability"></a>

### Result I.25: *Sector Condition Stability*

An agent's mismatch remains bounded if its correction function satisfies a sector condition (points inward with at least baseline efficiency) and the effective correction strength exceeds the environmental disturbance rate.

#### Formal Expression

Let $\delta(t) \in \mathbb{R}^n$ be the vector of model-reality mismatches. The mismatch dynamics:

*[Formulation]*

$$\frac{d\delta}{dt} = -F(\mathcal{T}, \delta) + w(t)$$

where $F$ is a (possibly nonlinear) correction function and $w(t)$ is environmental disturbance.

*[Assumption (sector-condition)]*

$F$ satisfies the **local sector condition** for $\Vert\delta\Vert \leq R$:

$$\delta^T F(\mathcal{T}, \delta) \geq \alpha \Vert\delta\Vert^2$$

where $\alpha \gt 0$ is the worst-case correction efficiency within the valid region of radius $R$ (the model class capacity). Disturbance is bounded: $\Vert w(t)\Vert \leq \rho$.

*[Derived (bounded-mismatch, from Lyapunov analysis)]*

The mismatch $\delta(t)$ is ultimately bounded by $R^\ast = \rho / \alpha$. The agent persists (avoids divergence) iff:

$$\alpha \gt \frac{\rho}{R}$$

*[Derived (adaptive-reserve)]*

The agent's capacity to absorb additional disturbance before mismatch exceeds the valid region:

$$\Delta\rho^* = \alpha R - \rho$$

##### Derivation

1. Lyapunov function $V(\delta) = \frac{1}{2}\Vert\delta\Vert^2$.
2. $\dot{V} = \delta^T(-F + w) \leq -\alpha\Vert\delta\Vert^2 + \rho\Vert\delta\Vert$.
3. $\dot{V} \lt 0$ when $\Vert\delta\Vert \gt \rho/\alpha$, giving ultimate bound $R^\ast = \rho/\alpha$.
4. Persistence requires $R^\ast \lt R$, i.e., $\alpha \gt \rho/R$. $\square$

Full derivation in [Derivation A.1](#sector-condition-derivation) (Props A.1, A.2).

#### Epistemic Status

These results are *exact* consequences of standard Lyapunov stability theory under the sector condition and bounded disturbance assumptions. They replace the linear ODE ($\dot{\delta} = -\mathcal{T}\delta + \rho$) with a rigorous nonlinear foundation. The linear ODE is recovered as a special case where $F(\mathcal{T}, \delta) = \mathcal{T}\delta$ and $\alpha = \mathcal{T}$.

#### Discussion

**Why the sector condition.** The linear ODE assumes correction scales linearly with mismatch forever. Real adaptive systems saturate, exhibit thresholding, or break down when the model class is exhausted. The sector condition captures the minimal structural requirement: the correction must point in the right direction with at least baseline efficiency $\alpha$.

**Generalizing the persistence threshold.** In the linear case, $\alpha = \mathcal{T}$ (adaptive tempo). The general result $\alpha \gt \rho/R$ proves the persistence threshold ([Result I.24](#persistence-condition)) is a structural necessity of any bounded-correction system, not an artifact of the linear approximation.

**Connection to structural adaptation.** When $\rho/\alpha \gt R$, disturbance exceeds the model class's capacity. The sector condition fails — this is the dynamical trigger for structural adaptation ([Result I.26](#structural-adaptation-necessity)), requiring a new model class with larger valid radius $R'$ or better efficiency $\alpha'$.


<a id="structural-adaptation-necessity"></a>

### Result I.26: *Structural Adaptation Necessity*

When model class fitness is insufficient — when no model in the current class can adequately represent reality — no amount of parametric adaptation can close the mismatch floor. The agent must change its model class, not just its parameters.

#### Formal Expression

*[Derived (structural-adaptation-necessity, Prop 10.1 from TFT)]*

If the model class fitness $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$ for some $\varepsilon \gt 0$, then no parametric adaptation within $\mathcal{M}$ can reduce the expected mismatch below a floor determined by $\varepsilon$.

##### Derivation

1. By definition, $S(M^\ast) = \mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$ where $M^\ast = \arg\sup_{M \in \mathcal{M}} S(M)$.
2. Therefore $I(\mathcal{C}_t; o_{t+1:\infty} \mid M^\ast, a_{t:\infty}) \gt 0$: the history contains predictive information that $M^\ast$ does not capture.
3. This uncaptured information manifests as *systematic* mismatch — structured residuals $\delta_t$ containing signal, not merely noise.
4. From [Result I.18](#mismatch-decomposition), the model error component has a positive lower bound that cannot be reduced by any $M \in \mathcal{M}$.
5. The update rule ([Empirical I.19](#update-gain)) adjusts $M_t$ within $\mathcal{M}$, but $M^\ast$ is already (approximately) reached. Further updates oscillate without net improvement.
6. Therefore: reducing mismatch below the floor requires changing $\mathcal{M}$ — structural adaptation. $\square$

**Corollary.** Persistent irreducible mismatch (after parametric convergence) is *diagnostic* of model class inadequacy. Systematic patterns in residuals are evidence that $\mathcal{F}(\mathcal{M})$ is insufficient.

#### Epistemic Status

*Exact* — this is a pure information-theoretic result. If the model class cannot represent the environment's predictive structure, no parameter optimization within that class can compensate. The assumptions are: the agent has converged parametrically (reached $M^\ast$ or its vicinity), and the environment has predictable structure that exceeds $\mathcal{M}$'s capacity.

#### Discussion

**Observable symptoms of model class inadequacy.** When $\mathcal{F}(\mathcal{M})$ is low:

1. **Persistent irreducible mismatch**: $\Vert\delta_t\Vert$ remains large despite extended updating — the model has converged within $\mathcal{M}$ but the best achievable model is still poor.
2. **Gain collapse without performance**: $\eta^\ast$ has decreased (model appears confident) but predictions remain inaccurate — the model is confidently wrong, having fitted to structure in $\mathcal{M}$ that doesn't match reality.
3. **Systematic mismatch patterns**: $\delta_t$ shows structure (correlations, trends, periodicities) that the model class cannot represent — the residuals contain signal that $\mathcal{M}$ lacks the capacity to absorb.

**Structural overfitting: the opposite failure mode.** $\mathcal{M}$ can also be *too expressive*, causing the model to memorize irreducible noise. Symptoms: low training mismatch but high generalization mismatch; model complexity growing without predictive gain; $\eta^\ast \to 0$ (confident) but confidence is spurious. The information bottleneck ([Formulation I.11](#information-bottleneck)) provides the diagnostic: when marginal increases in model complexity yield no marginal predictive power, the model is past the optimal point on the rate-distortion curve. Structural adaptation in this case means *compression* — moving to a simpler $\mathcal{M}'$. Structural adaptation is bidirectional: expansion when too constrained (this proposition), compression when too expressive.

**Mechanisms of structural change.** Structural adaptation can proceed by:

- **Decomposition and recombination**: Tearing apart existing structure and synthesizing new configurations from the pieces. Boyd's "Destruction and Creation" insight; Kuhn's paradigm shifts; Popper's conjecture and refutation.
- **Expansion**: Adding new representational capacity without destroying existing structure. Bayesian nonparametrics, growing neural architectures, organizational expansion.
- **Compression**: Removing unnecessary structure while preserving the predictive core. Regularization, Occam's razor, organizational streamlining.
- **Grafting**: Incorporating external structure. Transfer learning, acquiring a company, consulting an expert. Query actions ([Definition I.20](#causal-information-yield)) are a primary conduit for grafting.

The severity of structural change needed depends on *how far* the current model class is from adequacy. Minor regime changes may require only expansion or grafting; fundamental shifts where $\mathcal{M}$'s assumptions are violated may demand full decomposition.

**The cost of structural change.** Structural adaptation is expensive: knowledge loss (parameters learned within $\mathcal{M}$ may not transfer), temporary performance drop (new model starts uncertain), search cost (finding good $\mathcal{M}'$), coordination cost (in multi-agent systems). This creates rational conservatism — prefer parametric adaptation when it suffices, resort to structural change only when the evidence is strong. Premature structural change wastes accumulated knowledge; delayed structural change accumulates mismatch. The connection to [Derived I.23](#deliberation-cost): structural adaptation is deliberation with a *massive* $\Delta\tau$, and the mismatch debt during the transition is correspondingly enormous.

**Temporal nesting of adaptation.** Parametric and structural adaptation operate at different timescales: $\nu_{\text{parametric}} \gg \nu_{\text{structural}}$. More generally, an agent may have multiple adaptive processes at different rates, with the convergence constraint that faster processes must approximately converge before slower ones act on their output. If deeper change occurs before shallower adaptation has converged, the deeper change is based on transients rather than settled dynamics.

**Domain instantiations:**

| Domain | Parametric adaptation | Structural adaptation |
|--------|----------------------|----------------------|
| Kalman filter | State estimate update | Switching observation/dynamics models |
| RL | Weight/Q-value update | Architecture search |
| PID | — (gains fixed) | Switching to MPC |
| Bayesian | Posterior update | Model selection, nonparametrics |
| Boyd | Orientation updating | Destruction and creation of mental models |
| Science | Normal science (Kuhn) | Paradigm shift |
| Evolution | Allele frequency change | Speciation, new body plans |
| Organization | Process optimization | Strategic pivot, restructuring |
| Software | Incremental refactoring | Architecture migration |

**(Descended from TF-10.)**


<a id="temporal-nesting"></a>

### Derived I.27: *Temporal Nesting*

An agent's adaptive processes stratify naturally by timescale, with each level operating on the quasi-steady-state output of the level below. Faster processes must approximately converge before slower ones act on their output.

#### Formal Expression

*[Derived (temporal-nesting)]*

$$\nu_{\text{level } n+1} \ll \nu_{\text{level } n}$$

for each adjacent pair of adaptive timescales. If a slower process acts before the faster process beneath it has converged, the system oscillates — the slower process adjusts based on transient behavior rather than settled dynamics.

| Timescale | Process | What changes |
|-----------|---------|-------------|
| Fastest | Reactive response | Action given current model |
| Fast | Parametric update | Model parameters within $\mathcal{M}$ |
| Slow | Structural adaptation | Model class $\mathcal{M}$ |
| Slowest | Architectural change | The agent's fundamental structure |

This table is illustrative — real systems may have additional intermediate levels. The number of distinguishable timescales is not fixed; what matters is the structural relationship between adjacent levels.

#### Epistemic Status

*Robust qualitative* — this is standard singular perturbation reasoning (Tikhonov's theorem). The convergence constraint follows from the structure of multi-timescale updating. The specific timescale ratios needed for adequate separation are domain-dependent and not derived within ACT.

#### Discussion

**Domain instantiations of temporal nesting:**

- **PID control**: D-term (fastest, high-frequency response) → P-term (current error) → I-term (slowest, accumulated bias)
- **RL**: Action selection → value function update → policy improvement → architecture change
- **Biology**: Reflexes (ms) → perceptual learning (minutes) → skill acquisition (months) → developmental change (years) → evolutionary adaptation (generations)
- **Organizations**: Operational decisions (hours) → tactical adjustments (weeks) → strategic revision (quarters) → restructuring (years)
- **Boyd**: Tactical OODA (seconds–minutes) → operational (hours–days) → strategic (weeks–months) → grand strategic (years)

**Structural adaptation as slow-timescale dynamics.** The conservatism toward structural change ([Result I.26](#structural-adaptation-necessity)) is a derived consequence of temporal nesting: structural adaptation operates at a much slower timescale than parametric, so the mismatch cost of the "pause" ($\rho \cdot \Delta\tau$) is enormous. The agent rationally resists until the parametric mismatch floor exceeds this cost. See also [Derived I.23](#deliberation-cost) for the formal tradeoff.

**Violation symptoms.** When nesting is violated (a slower process acts before the faster one converges): oscillation, instability, degraded performance. In organizations: micromanagement (strategic decisions at operational tempo). In RL: policy updates before value function converges (policy oscillation). In biology: premature developmental transitions.

**Multi-timescale stability (sketch).** Singular perturbation theory gives the composite stability result: if each level is stable given the levels above it (each level has a stable attractor for fixed slower-level parameters), and the timescale separation is sufficient, the composite $N$-level system is stable. Making this rigorous for ACT requires specifying dynamics at deeper adaptive levels — an open problem. See [Sketch A.3](#multi-timescale-stability) for the framework.

**(Descended from TF-11.)**


<a id="agent-identity"></a>

### Discussion I.28: *Agent Identity and Temporal Continuity*

An agent's causal history ([Definition I.9](#chronica)) is singular and non-forkable. Identity within ACT is grounded not in the model state $M_t$ (which can be copied) but in the unique causal trajectory $\mathcal C_t$ (which cannot).

#### Formal Expression

*[Discussion (agent-identity)]*

If $M_t$ is a sufficient statistic for $\mathcal C_t$ ([Definition I.12](#model-sufficiency)), and $\mathcal C_t$ is a unique temporal sequence ([Definition I.9](#chronica)), then $M_t$ represents a *singular causal trajectory*. Duplicating $M_t$ and exposing the copies to different future events creates two agents with *divergent* causal histories, neither of which is a sufficient statistic for the other's trajectory.

#### Epistemic Status

This is *discussion-grade*. The observations follow qualitatively from the formalism but are not formal propositions. No downstream formal result depends on this material. Whether the mathematical structure grounds something that deserves to be called "identity" or "continuity of experience" is beyond ACT's scope. The mathematical structure is clear: the feedback loop produces a singular, non-forkable causal trajectory, and model adequacy is defined relative to that trajectory.

#### Discussion

**The clone problem, precisely stated.** Consider copying an LLM's weights (a concrete $M_t$) exactly. At the moment of duplication, both copies are identical — same model state, same causal history $\mathcal C_t$. But the *very next* event — a different user's message, a different observation — creates two divergent, irreversible causal trajectories $\mathcal C_{t+1}^{(1)}$ and $\mathcal C_{t+1}^{(2)}$. Their Level 2 and Level 3 capacities ([Definition I.8](#pearl-causal-hierarchy)) now reference different causal pasts. Their sufficiency $S(M_{t+1})$ is measured against different histories. Neither copy's future model state is a sufficient statistic for the other's trajectory.

Within ACT's formalism, identity is not the model state $M_t$ (which can be copied) but the *singular causal trajectory* $\mathcal C_t$ (which cannot). A copy shares a *prefix* of the original's causal history, as a sibling shares early childhood; it does not share the trajectory itself.

**Formal consequences (not merely philosophical):**

- A forked model's sufficiency $S(M_t)$ ([Definition I.12](#model-sufficiency)) is defined relative to *its own* interaction history. Post-fork, each copy's sufficiency is measured against a different $\mathcal{C}$.
- Merging divergent models requires reconciling incompatible causal histories — a lossy operation with no generally optimal solution.
- Temporal continuity (one unbroken causal thread) is what gives the model's sufficient statistic its meaning.

**Connection to Section V.** The 100% context turnover problem ([Observation V.2](#context-turnover)) is a special case: each AI agent session starts a new causal trajectory $\mathcal C_t$ from near-zero. External memory (CLAUDE.md, memory files) transfers a *summary* of previous trajectories' models, but not the trajectories themselves. The non-forkability observation frames this not as a deficiency but as a structural feature of causally-embedded agents.

**(Descended from TF Appendix G.)**



---

## II. Actuated Adaptation: Agentic Systems

*Scope narrowing: agents that not only track reality but aim at something. This adds objectives and strategy alongside the reality model. Section I's adaptive machinery applies to the epistemic substate $M_t$ directly. The clean factorization — where $M_t$ updates independently of $G_t$, yielding the sequential orient cascade — is conditional on directed separation ([Derived II.12](#directed-separation)). What Section II adds is the goal-directed layer: objectives, strategy, and the orient cascade that connects them.*

*The derivation chain for this section is mature (see `scratch/spike-v3-purposeful-agent.md`). Most of it provides better justification and epistemic labels for architecture that already existed. The genuinely novel results are: the satisfaction gap / control regret split ([Definition II.13](#satisfaction-gap), [Definition II.14](#control-regret)), the $G_t$ complexity bound (in [Derived II.16](#orient-cascade)), and the graph structure uniqueness argument (see `scratch/spike-graph-uniqueness.md`).*

*"If a man knows not to which port he sails, no wind is favorable." — Seneca*


<a id="agent-spectrum"></a>

### Definition II.1: *The Agent Spectrum*

Two independent dimensions — model richness and objective richness — create a spectrum from reactive systems through purposeful agents. These are regions of a continuum, not discrete categories.

#### Formal Expression

*[Definition (agent-spectrum)]*

Two dimensions — model richness and objective richness — define four regions of a continuum:

| | Objective absent or trivial | Objective structured |
|---|---|---|
| **Model absent or trivial** | *Reactive system*: fixed input-output rule (reflex arc, hardwired relay) | *Blind pursuer*: pursues goal without modeling reality (gradient follower, basic search) |
| **Model structured** | *Adaptive tracker*: builds reality model, no goal beyond tracking (Kalman filter, passive Bayesian learner) | *Actuated agent*: models reality AND pursues objectives (commander, developer, AI agent) |

The regions differ in which state objects carry nontrivial structure:
- Reactive: $M_t$ and $O_t$ both absent or too degenerate for the associated machinery to be non-vacuous
- Adaptive tracker: $M_t$ structured — Section I's machinery fully describes these agents
- Blind pursuer: $O_t$ structured, $M_t$ absent or degenerate — has a clear target but no predictive model
- Actuated agent: $(M_t, O_t)$ both structured, possibly with $\Sigma_t$ — the full scope of ACT

#### Epistemic Status

This is *definitional* — it names regions of a continuum for analytical convenience. The regions are not ontological categories; agents migrate between them. A PID controller with auto-tuning is moving from blind pursuer toward actuated agent. An RL agent in pure exploration is temporarily an adaptive tracker.

#### Discussion

**The continuum, not categories.** Both axes are spectra: model richness ranges from no retained state, through error-integral-derivative, through full world models. Objective richness ranges from no preference, through scalar setpoints, through explicit multi-objective strategies. The 2×2 table names idealized regions; real agents populate the space between them.

**Low-end agents sit near region boundaries.** A thermostat has degenerate forms of both $M_t$ (last temperature reading — no history, no prediction) and $O_t$ (setpoint). It sits near the origin of both axes — closest to the reactive region but not truly absent on either axis. A PID controller has a richer error signal ($M_t$: error, integral, derivative) and a clear setpoint ($O_t$) — it's a blind pursuer with a degenerate model, not a system with no model at all. A reflex arc (no retained state, no setpoint) is the truly reactive case. The meaningful classification question is not "does $M_t$ exist?" but "is $M_t$ rich enough to support the adaptive dynamics of Section I?"

**Section I covers the left column.** Adaptive trackers are the primary subject of Section I — agents that build and maintain $M_t$ without explicit purpose. The mismatch signal ([Definition I.17](#mismatch-signal)), gain ([Empirical I.19](#update-gain)), tempo ([Definition I.21](#adaptive-tempo)), and persistence condition ([Result I.24](#persistence-condition)) fully characterize their adaptive dynamics. TFT was developed primarily for this region.

**Section II adds the right column.** Actuated agents need everything from Section I plus objectives, strategy, and the orient cascade that connects them. The adaptive machinery from Section I applies to the epistemic substate $M_t$ directly. When directed separation ([Derived II.12](#directed-separation)) holds — when the epistemic update is goal-blind — the Section I → Section II lift is clean and the orient cascade resolves sequentially.

**"Actuated" terminology.** The top-right quadrant is labeled "actuated agent" rather than "purposeful agent" to maintain a mechanical, formal register. "Purposeful" and "goal-oriented" are fine in natural language; "actuated" is the formal term. "Self-actuated" is reserved for agents that set their own objectives, as distinct from agents with externally supplied objectives.


<a id="complete-agent-state"></a>

### Formulation II.2: *Complete Agent State*

To treat agents with purpose, the internal state lifts from $M_t$ alone to $X_t = (M_t, G_t)$, separating epistemic content (beliefs about reality) from purposeful content (what the agent wants and how it plans to get it).

#### Formal Expression

*[Formulation (complete-agent-state)]*

$$X_t = (M_t, G_t)$$

where:
- $M_t \in \mathcal{M}$: **epistemic substate** — the agent's compressed beliefs about reality. All Section I machinery (mismatch, gain, tempo, persistence) applies to $M_t$ unchanged.
- $G_t \in \mathcal{G}$: **purposeful substate** — what the agent wants and how it plans to get it. Decomposed further in [Definition II.5](#strategy-dimension).

Section I is the special case $X_t = (M_t, \emptyset)$: adaptive systems without purpose.

**Update dynamics.** By [Derived I.15](#recursive-update) applied to $X_t$:

$$X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$$

This decomposes into component updates when the epistemic update is goal-blind ([Derived II.12](#directed-separation)):

*[Derived (from recursive-update + directed-separation)]*

$$M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$$

$$G_{\tau^+} = f_G(G_{\tau^-}, M_{\tau^+}, e_\tau)$$

Between events: $\dot{M} = g_M(M)$, $\dot{G} = g_G(G, M)$.

The asymmetry is structural: $f_M$ has no $G_t$ argument; $f_G$ depends on $M_{\tau^+}$ (the *post-update* epistemic state — the agent revises its goals in light of its revised understanding of reality, not the other way around).

**Policy.** Action couples all substates:

$$a_t = \pi(M_t, G_t)$$

This is the single point of coupling between epistemic and purposeful dynamics. The update functions are separated; the action is not.

#### Epistemic Status

*Formulation.* The lift from $M_t$ to $X_t = (M_t, G_t)$ is a representational choice. One could alternatively extend $M_t$ to carry purposeful content implicitly (e.g., by treating goals as part of the model's predictive structure). The separation is motivated by three properties:

1. **Backward compatibility**: Section I's results apply to $M_t$ unchanged — no existing machinery needs modification
2. **Different dynamics**: epistemic and purposeful components have distinct update sources, timescales, and information dependencies
3. **Directed separation**: the claim that $f_M$ is $G_t$-independent ([Derived II.12](#directed-separation)) is only statable when the components are separated

The robustness claim: any alternative decomposition of the complete agent state into epistemic and purposeful components — if it preserves the directed separation — will be structurally isomorphic to $(M_t, G_t)$, because directed separation forces a component whose update function doesn't reference purpose.

#### Discussion

**Backward compatibility with Section I — what survives the lift.** [Formulation I.10](#agent-model) defines $M_t$ as the agent's complete internal state. Under the lift, $M_t$ is the epistemic substate — complete within the epistemic domain but no longer the whole story. All epistemic machinery (mismatch signal, gain, tempo, persistence condition, sector-condition stability, mismatch decomposition) applies to $M_t$ without modification. However, [Derived I.16](#action-selection) derives $a_t = \pi(M_t)$ from the premise that $M_t$ is the agent's *complete* state — this derivation is superseded by $a_t = \pi(M_t, G_t)$ after the lift. For Section I agents ($G_t = \emptyset$), the original result holds trivially. The lift adds structure *alongside* $M_t$, not within it; the one result that relied on $M_t$ being *all there is* (action selection) is explicitly extended.

**What $G_t$ contains.** At this level, $G_t$ is opaque — it could be a scalar setpoint, a utility function, a strategy graph, or nothing. The decomposition into $O_t$ (objective) and $\Sigma_t$ (strategy) is a separate step ([Definition II.5](#strategy-dimension)), not implied by this formulation.

**The general case requires coupling.** Without directed separation, the general update is $X_{\tau^+} = f_X(X_{\tau^-}, e_\tau)$ — a single function on the full state. The decomposition into separate $f_M$ and $f_G$ is an additional structural claim about how the update factorizes. When directed separation fails (goal-conditioned epistemic updates), the decomposition is an approximation. See [Derived II.12](#directed-separation) for the scope conditions.

#### Working Notes

- The between-event dynamics $\dot{G} = g_G(G, M)$ allow autonomous purposeful evolution: strategy revision during deliberation, objective adjustment, commitment strengthening. Whether these are practically important depends on agent architecture — for LLM agents with discrete sessions, between-event dynamics may be negligible compared to event-driven updates.
- The formulation doesn't constrain the dimensionality or structure of $\mathcal{G}$. For a thermostat, $\mathcal{G}$ is a single scalar. For a military commander, $\mathcal{G}$ is a complex structured object. The theory must work across this range — the type-stable interface is $V_{O_t}: \text{trajectories} \to \mathbb{R}$ ([Definition II.3](#objective-functional)).
- $G_t = \emptyset$ is not just a degenerate case. Adaptive trackers (Section I agents) are an important class. The lift should feel like a natural extension, not a replacement.


<a id="objective-functional"></a>

### Definition II.3: *Objective Functional*

The objective $O_t$ is the component of $G_t$ that specifies what the agent wants — the evaluation criterion for trajectories. Its interface to the theory is a single functional $V_{O_t}: \text{trajectories} \to \mathbb{R}$, regardless of how the objective is internally represented.

#### Formal Expression

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

#### Epistemic Status

*Axiomatic.* This is a definition — it names an object and specifies its interface. The claim that $V_{O_t}: \text{trajectories} \to \mathbb{R}$ is the right interface is grounded in: any evaluation criterion must ultimately answer "how good is this trajectory?" with a scalar, because the agent must compare alternatives. The real-valued codomain follows from this comparability requirement (total ordering of alternatives).

**Scope restriction: scalar comparability.** The real-valued codomain is a genuine restriction. Agents with incommensurable objectives — where no total ordering of alternatives exists — require a vector-valued or Pareto formulation outside this definition. The restriction is standard in decision theory (von Neumann–Morgenstern) and covers most practical cases, including scalarized multi-objective problems and lexicographically ordered priorities. But organizations or AI agents with hard non-compensatory constraints (safety AND profitability as independent thresholds, not a weighted sum) are only approximately covered. This should be acknowledged wherever downstream results depend on scalar $V_{O_t}$, particularly the satisfaction gap ([Definition II.13](#satisfaction-gap)) and its single-threshold feasibility test.

#### Discussion

**Filling TF-08's gap.** The existing policy objective ([Definition I.20](#causal-information-yield)) contains $\mathbb{E}[\text{value}(a) \mid M_t]$ without specifying what "value" means. $O_t$ provides the formal content: value is $V_{O_t}$ applied to expected trajectories. The [Definition II.4](#value-object) segment develops the full evaluation machinery ($V_O$, $Q_O$ with horizon and continuation policy).

**$O_t$ evaluates; $\Sigma_t$ guides.** The objective says "is this trajectory satisfactory?" The strategy ([Definition II.5](#strategy-dimension)) says "which action sequence produces a satisfactory trajectory?" A chess player's objective (win) is simple; the strategy (how to win) is complex. These answer different questions and carry different kinds of information — the split is developed in [Definition II.5](#strategy-dimension).

**What $O_t$ is NOT.** $O_t$ does not encode how to achieve the objective (that's $\Sigma_t$), what the agent believes about the world (that's $M_t$), or the agent's commitment or resource state (open questions — see [Definition II.5](#strategy-dimension) Working Notes). $O_t$ is purely an evaluation criterion.

#### Working Notes

- Compound objectives (multiple simultaneous criteria) might be modeled as terminal AND-nodes in $\Sigma_t$, keeping $O_t$ always simple (one evaluation per terminal). Whether this works for genuinely incommensurable objectives (safety vs. speed) is open — a vector-valued $V_{O_t}$ or Pareto formulation might be needed.
- The trajectory functional is real-valued, which assumes all objectives are commensurable on a single scale. This is standard in decision theory (von Neumann–Morgenstern) but is a genuine restriction for multi-objective agents. Currently acknowledged, not resolved.
- $O_t$ can change over time — objectives evolve. The *rate* of objective revision ($\nu_O$) is typically much slower than strategy revision ($\nu_\Sigma$), which is much slower than epistemic update ($\nu_M$). This timescale separation is an empirical observation, not a derived result.


<a id="value-object"></a>

### Definition II.4: *Value Object*

The horizon- and policy-conditioned value object $V_O$ turns the abstract objective functional $V_{O_t}$ into a decision-making tool: "given what I believe, what I plan to do next, and how far I'm looking ahead, how good is this situation?"

#### Formal Expression

*[Definition (value-object)]*

Given objective $O_t$, model $M_t$, policy $\pi$, and horizon $N_h$:

$$V_O(M_t, \pi; N_h) = \mathbb{E}\!\left[V_{O_t}(\tau_{t:t+N_h}) \;\middle\vert\; M_t,\; \pi\right]$$

**Action-value form** (for action selection):

$$Q_O(M_t, a; \pi_{\text{cont}}, N_h) = \mathbb{E}\!\left[V_{O_t}(\tau) \;\middle\vert\; M_t,\; a_t = a,\; a_{t+1:} \sim \pi_{\text{cont}}\right]$$

$Q_O$ answers: "if I take action $a$ now and then follow $\pi_{\text{cont}}$ afterward, what is my expected trajectory value?" This is the interventional query that connects the value object to action selection.

**Continuation convention.** All value queries are conditioned on a specific continuation policy $\pi_{\text{cont}}$ and finite horizon $N_h$. $\pi_{\text{cont}}$ is a *parameter* of the value object, not a derived quantity. ACT does not prescribe a specific solution concept. Common choices:

- $\pi_{\text{cont}} = \pi_{\text{current}}$ — **one-step improvement** (evaluate each action assuming current behavior continues afterward). Natural default for ACT: requires no fixed-point computation and aligns with incremental update philosophy ([Empirical I.19](#update-gain)). Not a convergence guarantee; a practical default.
- $\pi_{\text{cont}} = \pi^\ast$ — **Bellman fixed point** (self-consistent optimal continuation). Requires solving a fixed-point equation. Standard in RL and dynamic programming.
- $\pi_{\text{cont}}$ re-optimized each step — **receding horizon / MPC**. Re-plans at each step with updated $M_t$.

The one-step improvement is the natural default because it mirrors ACT's general philosophy: update incrementally from where you are, using the best available information, without requiring global optimality.

#### Epistemic Status

*Exact* under the assumption that $M_t$ supports the required conditional expectations. The value object is a mathematical definition — conditional expectations of a functional over trajectories. The definitions are precise; the *computability* of these expectations is a separate question (in practice, they are approximated via simulation, sampling, or function approximation).

#### Discussion

**Extending the policy objective.** The existing policy objective ([Definition I.20](#causal-information-yield)) uses $\mathbb{E}[\text{value}(a) \mid M_t]$ without formal content for "value." With the value object, this becomes:

*[Discussion (policy-objective-extension)]*

$$\pi^*(M_t, G_t) = \arg\max_a \left[Q_O(M_t, a;\, \pi_{\text{cont}}, N_h) + \lambda(M_t, O_t, N_h) \cdot \text{CIY}(a;\, M_t)\right]$$

Note that $\lambda$ now depends on $(M_t, O_t, N_h)$, not just $M_t$. The value of exploration depends on the objective and the horizon:
- An agent with a deadline should explore less as time runs out
- An agent with a safety constraint should explore differently from a utility maximizer
- Two agents with identical $M_t$ but different objectives should price exploration differently

This extension is structurally motivated but the specific form of $\lambda(M_t, O_t, N_h)$ is not derived within ACT (same status as [Definition I.20](#causal-information-yield)'s treatment of $\lambda$).

**Connection to [Definition I.12](#model-sufficiency).** $V_O$ is conditioned on $M_t$, not on the true environment state $\Omega_t$. When $S(M_t) \lt 1$, the agent's value estimates are biased — it may over- or underestimate trajectory values because its model is incomplete. The satisfaction gap ([Definition II.13](#satisfaction-gap)) and control regret ([Definition II.14](#control-regret)) are defined in terms of $V_O(M_t, \cdot)$, not $V_O(\Omega_t, \cdot)$, which means they measure the agent's *believed* situation, not the true one. Improving $M_t$ (reducing $\delta_{\text{epistemic}}$) brings the agent's value estimates closer to reality.

**Horizon dependence.** $N_h$ is not merely a computational convenience — it reflects genuine uncertainty about the far future. Long horizons amplify the impact of model error (small biases in $M_t$ compound over many steps). The choice of $N_h$ trades off farsightedness against robustness to model error. An agent in a fast-changing environment ($\rho$ high) should use shorter horizons; one in a stable environment can plan further.

#### Working Notes

- The continuation convention is a degree of freedom that interacts with the satisfaction gap and control regret: different $\pi_{\text{cont}}$ choices give different $A_O$ values, which changes what "best achievable" means. The theory needs to be explicit about which convention is used when these quantities are compared.
- When a specific convergence guarantee is needed (e.g., for strategy-persistence-schema), the solution concept must be stated explicitly — the one-step improvement default is not sufficient.
- For LLM agents with context turnover, $N_h$ has a natural bound: the current session. The "continuation policy" is whatever the next agent instance will do, which the current instance cannot control. This connects to [Observation V.2](#context-turnover) (Section V).


<a id="strategy-dimension"></a>

### Definition II.5: *Strategy Dimension*

The purposeful substate $G_t$ decomposes into two structurally distinct components: $O_t$ (the objective — what the agent wants) and $\Sigma_t$ (the strategy — the agent's theory of how its actions produce progress toward $O_t$). These carry different kinds of information answering different questions.

#### Formal Expression

*[Definition (strategy-dimension)]*

$$G_t = (O_t, \Sigma_t)$$

where:
- $O_t$: **evaluation** — "Is this trajectory satisfactory?" ([Definition II.3](#objective-functional))
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

#### Epistemic Status

*Axiomatic.* This is a definition — it names a structural distinction that exists in the information. The distinction between "what makes a trajectory good" (evaluation) and "how to produce a good trajectory" (guidance) is a categorical difference, not a quantitative one. The claim is NOT that all agents maintain both explicitly — reactive agents have $\Sigma_t = \emptyset$, and that's fine. The claim is that when an agent does maintain purposeful state, it decomposes along this line.

The two dimensions vary independently: a chess player has a simple $O_t$ (win) and a complex $\Sigma_t$ (opening theory, tactical patterns, endgame knowledge). A multi-objective optimizer may have a complex $O_t$ (Pareto frontier) and a simple $\Sigma_t$ (gradient descent). This independence is why the split matters — conflating them in a single hierarchy obscures the fact that objective richness and strategic richness are separate design axes.

#### Discussion

**When richer $\Sigma_t$ is needed.** A reactive agent ($\Sigma_t = \emptyset$) suffices when greedy optimization on $Q_O$ ([Definition II.4](#value-object)) works — when the action-to-value mapping is approximately convex and single-step. When the environment has non-convex landscapes, prerequisite structure, or multi-step causal chains, greedy optimization fails and the agent needs explicit strategy. The trigger is the purposeful analog of [Result I.26](#structural-adaptation-necessity): inadequacy of the current $\Sigma_t$ representation for the environment's causal complexity.

**$O_t$ and $\Sigma_t$ have different update dynamics.** Objectives change slowly: an organization's mission, a developer's feature goal, a commander's campaign objective. Strategies change faster: adjust the plan when step 3 fails, redirect resources, try an alternative path. Epistemic state changes fastest: each observation updates $M_t$. This timescale ordering ($\nu_M \gg \nu_\Sigma \gg \nu_O$) is an empirical observation, not a derived result. It holds for many agent populations but is not universal — an agent discovering its goal is infeasible may revise $O_t$ faster than $\Sigma_t$.

**The decomposition resolves a type error.** Earlier formulations used $\delta_{\text{goal}} = G_t - M_t$ as a goal mismatch signal. When $\Sigma_t$ is a DAG, this is a type error — you cannot subtract a graph from a state vector. The [Definition II.13](#satisfaction-gap) and [Definition II.14](#control-regret) replace this with properly typed gap measures.

#### Working Notes

- The independence of $O_t$ and $\Sigma_t$ richness has a practical consequence for agent design: you can upgrade the strategy engine (from reactive to DAG-based planning) without changing the objective representation, and vice versa. This is a desirable architectural property, not just an analytical convenience.
- **Cognitive cost of $\Sigma_t$**: maintaining a 500-node DAG is qualitatively different from maintaining a 12-node one. The IB framework ([Formulation I.11](#information-bottleneck)) applies to strategy as well as to models — the agent must compress its strategy to fit in working memory. For finite-context agents (LLMs), this is concrete: the DAG must fit in the context window. No formal analog of $\beta$ (compression cost) exists yet for strategy; this is an open question.
- **Commitment state** (from intent-dag-consolidated DP-3): the formalism doesn't distinguish "considering" from "executing." OR branches in $\Sigma_t$ are options until something commits resources. A $D_t$ (desire) / $I_t$ (committed intent) split may become load-bearing in multi-agent settings (shared desire vs. shared commitment). Open for Section III.
- **Resource budget**: strategy evaluation requires knowing what paths cost, but costs are currently unmodeled. For agents with negligible action cost (LLM API calls), this is adequate. For resource-constrained agents (military units, development teams), per-action costs and capacity constraints would need to enter the formalism. Open.


<a id="causal-hierarchy-requirement"></a>

### Derived II.6: *Causal Hierarchy Requirement*

Evaluating the action-value $Q_O$ requires answering "what happens if I *do* action $a$?" — a Level 2 (interventional) query in Pearl's causal hierarchy. An agent that must learn the answer to this question during operation needs access to causal structure beyond what purely predictive models can provide.

#### Formal Expression

*[Derived (causal-hierarchy-requirement, from value-object + pearl-causal-hierarchy)]*

Action selection via [Definition II.4](#value-object) requires:

$$Q_O(M_t, a;\, \pi_{\text{cont}}, N_h) = \mathbb{E}\!\left[V_{O_t}(\tau) \;\middle\vert\; M_t,\; a_t = a,\; a_{t+1:} \sim \pi_{\text{cont}}\right]$$

The conditioning "$a_t = a$" is an *intervention*, not a *conditioning on observed data*. By [Definition I.8](#pearl-causal-hierarchy), Level 2 queries ($P(Y \mid do(X))$) cannot in general be computed from Level 1 data ($P(Y \mid X)$) alone. Therefore:

An agent that must evaluate $Q_O$ from experience needs access to Level 2 knowledge — knowledge about the effects of its own interventions, not merely correlational patterns.

*[Scope Narrowing (learning-agents)]*

We restrict attention to agents that must **acquire or refine** Level 2 knowledge during operation. This excludes agents with **pre-compiled** interventional structure:
- PID controllers (the designer pre-computed the control law)
- LQR (separation principle gives optimal policy from model parameters)
- Hardcoded reactive policies

Pre-compiled agents are purposeful — they have objectives and act on them — but their causal structure was externally supplied by a designer who had Level 2 access. This scope narrowing focuses the theory on agents that must build or maintain their own causal understanding.

#### Epistemic Status

*Exact.* The derivation is a direct application of the causal hierarchy theorem (Bareinboim et al. 2022) to the value-object definition. If you accept that $Q_O$ is an interventional query and that the causal hierarchy is strict, the conclusion follows. The scope narrowing to learning agents is a definitional restriction, not a derived result — it sharpens the class of agents under study.

#### Discussion

**The causal hierarchy theorem does the heavy lifting.** The key mathematical fact is external to ACT: Bareinboim et al. (2022) prove that the three levels (association, intervention, counterfactual) form a strict hierarchy — Level 2 quantities cannot in general be computed from Level 1 data. ACT's contribution is applying this to the purposeful-agent setting: if you want to select actions by their consequences ($Q_O$), you need causal structure.

**What "Level 2 knowledge" means concretely.** For different agents:
- A developer needs to know "if I refactor this module, will tests still pass?" (not just "modules that were refactored tend to have tests that fail")
- A commander needs to know "if I move forces north, will the enemy respond by retreating?" (not just "when forces moved north, the enemy often retreated")
- An RL agent needs $Q(s, a) = \mathbb{E}[R \mid s, do(a)]$, not $\mathbb{E}[R \mid s, A=a]$ (the latter includes selection bias from the agent's own policy)

The distinction between $do(a)$ and $A = a$ is the core of causal inference. It matters whenever the agent's action-selection policy correlates with unobserved confounders.

**Why pre-compiled agents are excluded.** A thermostat "knows" that turning on the heater raises temperature — but this knowledge was designed in, not learned. The thermostat never needs to reason about interventions because the intervention-outcome mapping is hardwired. ACT's purposeful-agency machinery is specifically for agents that face uncertainty about how their actions affect the world and must reduce that uncertainty through experience.

#### Working Notes

- This scope narrowing connects to [Normative II.8](#explicit-strategy-condition): agents that must learn Level 2 structure face a cost-benefit tradeoff between learning through exploration (costly, slow, but verifies causal links) and planning through explicit $\Sigma_t$ (cheaper if the causal model is adequate, but the model may be wrong).
- LLMs trained on causally-structured text absorb causal priors — noisy prior knowledge from mixed provenance (experimental, observational, speculative). This is not verified interventional structure; it's a *prior* (plausible, not derived). An LLM in the adaptive loop has both: priors from training AND interventional data from the loop. The priors accelerate; the loop verifies. The IB framework ([Formulation I.11](#information-bottleneck)) predicts causal structure will be retained in training because it has predictive power for language.
- The scope narrowing to "learning agents" is generous — it includes any agent that updates its causal beliefs during operation, even if it starts with strong priors. The excluded class (pure pre-compiled controllers) is genuinely different: they never revise their action-consequence model.


<a id="loop-interventional-access"></a>

### Derived II.7: *Loop Provides Interventional Data Access*

An agent in the feedback loop generates interventional data by construction: the agent's action $a_t$ causally precedes the next observation $o_{t+1}$, and the mismatch conditioned on $a_t$ carries interventional information. This is how agents within ACT's scope gain Level 2 access — not through internal architecture, but through the loop itself.

#### Formal Expression

*[Derived (loop-interventional-access, from causal-structure + recursive-update)]*

By [Postulate I.7](#causal-structure), the temporal ordering is constitutive: $a_t$ causally precedes $o_{t+1}$. The agent chose $a_t$; the environment responded with $o_{t+1}$. This is an intervention — the agent varied its action and observed the result.

Formally: the pair $(a_t, o_{t+1})$ is generated under an intervention policy — the agent executed $a_t$, making it a genuine intervention rather than a passively observed association. The data *contains interventional signal*: it was produced by a do-operation, not by conditioning on a naturally occurring value of $A_t$.

However, this does not mean the agent automatically has access to a clean estimate of $P(o \mid do(a_t), \Omega_t)$. Between the interventional act and a usable interventional distribution stand: (1) coverage — the agent must have tried diverse actions, not just one policy; (2) confounding within a time step — unobserved state variables that affect both action choice and outcome; (3) delay — consequences may appear much later than $t+1$; (4) partial observability — $o_{t+1}$ reveals only part of the outcome. The claim is about the *character* of the data (interventional, not observational), not about the agent's ability to extract clean causal estimates from it.

The mismatch signal conditioned on the agent's action:

$$\delta_t \mid a_t = o_{t+1} - \hat{o}_{t+1}(M_t, a_t)$$

carries interventional information: it tells the agent how the environment responded to its specific intervention $a_t$, relative to what the model predicted.

#### Epistemic Status

*Exact.* This is a logical consequence of temporal ordering ([Postulate I.7](#causal-structure)) and the feedback-loop structure ([Scope I.5](#scope-condition)). The claim is about **data availability**, not reasoning capacity — the loop *provides* interventional data whether or not the agent *exploits* it for Level 2 reasoning. Whether the agent uses this data to build causal models depends on its update mechanism and model class.

The precision is important: we claim the agent has *access to* interventional data, not that it *correctly identifies* interventional structure. Confounding within a single time step, delayed outcomes, and partial observability can all complicate the extraction of clean causal signals from the loop data.

#### Discussion

**The loop as a Level 2 engine.** This is one of ACT's load-bearing results. The causal hierarchy theorem ([Derived II.6](#causal-hierarchy-requirement)) says Level 2 knowledge requires more than correlational data. This result says: the adaptive loop *is* the "more." An agent that acts and observes the consequences is generating interventional data — the same kind of data that a scientist generates through experiments. The loop is a perpetual experiment.

**Precision about what "interventional" means here.** The interventional interpretation is strongest when:
- The agent's action was the primary cause of the observed change (low confounding)
- The observation follows closely in time (short delay)
- The agent varied its action across episodes (not stuck on one policy)

When confounding is high, delays are long, or the agent follows a fixed policy, the interventional information in each $(a_t, o_{t+1})$ pair is weaker — still present, but harder to extract. This is why [Definition I.20](#causal-information-yield) distinguishes between high-CIY actions (that reveal causal structure) and low-CIY actions (that don't).

**Even agents without explicit causal models benefit.** A Q-learning agent doesn't maintain an explicit causal model, but its Q-values converge toward $\mathbb{E}[R \mid s, do(a)]$ rather than $\mathbb{E}[R \mid s, A=a]$ precisely because the training data comes from the agent's own interventions. The loop provides Level 2 data; the agent's learning algorithm determines whether that data is used effectively.

#### Working Notes

- This result establishes that ALL agents within ACT's scope ([Scope I.5](#scope-condition)) have access to interventional data, regardless of their internal architecture. This includes LLM agents operating through a tool-use loop — the LLM issues an action (tool call), observes the result, and updates. The loop gives it Level 2 data even though its internal architecture (transformer attention) is not designed for causal reasoning. The loop compensates for architectural limitations.
- The connection to [Definition I.20](#causal-information-yield): CIY quantifies *how much* interventional information a specific action provides. This segment establishes that interventional information is *available in principle*; CIY measures the *quantity per action*.


<a id="explicit-strategy-condition"></a>

### Normative II.8: *Explicit Strategy Condition*

An agent benefits from maintaining an explicit strategy $\Sigma_t$ when the cost of planning is less than the cost of learning through exploration alone. This is a normative design criterion — it tells you when explicit strategy is *worth it*, not that it's always necessary.

#### Formal Expression

*[Normative (explicit-strategy-condition, via temporal-optimality)]*

An agent benefits from explicit $\Sigma_t$ when:

$$C_{\text{plan}} + C_{\text{maintain}} \lt C_{\text{explore}} + C_{\text{repair}}$$

where:
- $C_{\text{plan}}$: cost of constructing and evaluating the strategy (deliberation, simulation, model queries)
- $C_{\text{maintain}}$: ongoing cost of keeping $\Sigma_t$ current as $M_t$ evolves (edge revision, structural updates)
- $C_{\text{explore}}$: cost of learning action-outcome mappings through direct interaction (real actions, real time, real consequences)
- $C_{\text{repair}}$: cost of correcting errors discovered only through execution (rollbacks, rework, damage)

All costs are measured in time ([Postulate I.1](#temporal-optimality)) under the precondition that the two approaches produce approximately equivalent non-temporal outcomes.

#### Epistemic Status

*Normative, not derived.* This is labeled *normative* because [Postulate I.1](#temporal-optimality) requires identical non-temporal outcomes as a precondition — "given equivalent outcomes, prefer the faster approach." In practice, loop-based and model-based approaches may differ in:

- **Final value**: the model introduces bias; exploration may discover things planning cannot
- **Risk profile**: exploration risks real damage; planning risks wrong models
- **Reversibility**: some exploratory actions are irreversible
- **Model bias**: explicit $\Sigma_t$ inherits the biases of $M_t$; loop-based learning does not

The inequality is correct *when* the outcomes are approximately equivalent — a condition that must be verified case by case, not assumed. When the precondition fails (model-based and loop-based approaches produce qualitatively different outcomes), the cost inequality is insufficient and the choice requires richer analysis (e.g., expected regret including model error).

#### Discussion

**When the inequality strongly favors planning.** The right side ($C_{\text{explore}} + C_{\text{repair}}$) is large when:
- Actions are expensive or irreversible (production deployments, military operations, surgical procedures)
- Exploration damage is severe (a wrong move in chess loses the game; a wrong deployment takes down the service)
- The environment is slow to respond (waiting for market feedback, waiting for test results)
- The action space is enormous (combinatorial planning problems)

In these domains, explicit $\Sigma_t$ is strongly motivated even if the planning model is imperfect.

**When the inequality favors pure exploration.** The left side ($C_{\text{plan}} + C_{\text{maintain}}$) is large when:
- The environment is too complex or novel for useful models (genuinely unknown territory)
- $M_t$ is severely inadequate (model predictions are worse than random)
- The environment changes faster than $\Sigma_t$ can be maintained ($\rho_\Sigma$ exceeds planning capacity)
- Actions are cheap and reversible (A/B testing, sandbox exploration)

**This makes [Postulate I.1](#temporal-optimality) load-bearing.** The postulate provides the normative grounding: among approaches producing equivalent outcomes, prefer the one requiring less time. The cost inequality instantiates this for the planning-vs-exploration choice. Without [Postulate I.1](#temporal-optimality), the inequality would be an engineering heuristic without theoretical grounding.

**Connection to the three-way tradeoff.** For actuated agents, the binary explore/exploit tradeoff extends to three modes: exploit (pursue $O_t$ via $\Sigma_t$), explore (improve $M_t$), and deliberate (revise $\Sigma_t$). The cost inequality addresses the coarsest question (is explicit $\Sigma_t$ worth having?). The finer question of how to allocate between the three modes at each time step is open — it connects to [Definition I.20](#causal-information-yield)'s exploration price $\lambda$ extended with $\Sigma_t$ revision costs.

#### Working Notes

- The inequality as stated is static — it compares cumulative costs. A dynamic version would ask: "given current $M_t$ quality, is it worth deliberating further or should I act now?" This connects to [Derived I.23](#deliberation-cost)'s threshold: deliberation is worthwhile only when additional deliberation improves action quality enough to justify the time spent.
- Part of $C_{\text{maintain}}$ is the cognitive cost of keeping $\Sigma_t$ in the agent's representational capacity. For LLM agents, this means fitting the strategy in the context window. A 500-node DAG may exceed this capacity, making the left side of the inequality large enough that simpler strategies (or pure exploration) become preferable despite higher exploration costs.
- The cost inequality may be most useful not as a binary decision rule but as a way to calibrate $\Sigma_t$ complexity: the agent should maintain a strategy just complex enough that $C_{\text{plan}} + C_{\text{maintain}}$ stays below $C_{\text{explore}} + C_{\text{repair}}$ for the current environment. This gives a principled answer to "how detailed should my plan be?"


<a id="chain-confidence-decay"></a>

### Derived II.9: *Chain Confidence Decay*

Confidence in a multi-step strategy decays monotonically with depth. The rate depends on the conditional dependence structure, but the qualitative result — longer chains are less confident than shorter ones — is robust.

#### Formal Expression

*[Derived (chain-confidence-decay, mathematical identity)]*

For a chain of $n$ uncertain steps with conditional success probabilities:

$$\log P(\text{chain}) = \sum_{i=1}^{n} \log P(E_i \mid E_{\lt i})$$

Since each $\log P(E_i \mid E_{\lt i}) \leq 0$, chain confidence decays monotonically with depth.

**The independent case** ($p^n$) is the simplest special case, not the general result. When steps are conditionally dependent — success at step $k$ makes step $k+1$ more likely — the decay is slower. When steps have negative dependence (success at $k$ makes $k+1$ harder — resource depletion, adversary adaptation), decay is faster.

**Quantitative illustration** (independent, uniform $p$):

| Depth | $p = 0.9$ | $p = 0.8$ |
|-------|-----------|-----------|
| 1 | 0.90 | 0.80 |
| 3 | 0.73 | 0.51 |
| 5 | 0.59 | 0.33 |
| 10 | 0.35 | 0.11 |
| 20 | 0.12 | 0.01 |

#### Epistemic Status

*Exact.* The additive decomposition of log-confidence is a mathematical identity (chain rule of probability). The qualitative consequence (monotonic decay) follows from the non-positivity of log-probabilities. No assumptions beyond the probability axioms.

#### Discussion

**Structural pressure on strategies.** Chain confidence decay creates systematic pressure toward:
- **Short plans**: fewer steps means higher aggregate confidence
- **Parallel fallback paths**: OR-branches provide alternative routes when one chain fails
- **High-confidence critical links**: invest in the reliability of steps that appear in every path
- **Early monitoring**: detect chain failure early rather than discovering it at the end

These are not prescriptions but consequences — an agent that ignores chain decay will experience more strategy failures, lower effective tempo, and (if the failures are costly) faster reserve depletion.

**AND-nodes amplify decay.** When multiple parent chains must all succeed (conjunctive combination), their confidences multiply. A node requiring $k$ parents each at depth $d$ with per-edge confidence $p$ has aggregate confidence $p^{k \cdot d}$, not $p^d$. Deep conjunctive strategies are exponentially more fragile than deep disjunctive ones. This asymmetry is formalized in the combination rules ([Definition II.11](#strategy-dag)).

**Connection to the persistence condition.** Chain decay makes long-horizon strategies inherently fragile, which increases the effective disturbance rate $\rho_\Sigma$ against strategy persistence. An agent pursuing a 20-step plan in a changing environment faces compound uncertainty from both chain decay (internal fragility) and environmental change (external disturbance). The interaction between these — how environmental change compounds through uncertain chains — is not yet formalized.

#### Working Notes

- The independent-edge assumption (used in the quantitative table) is conservative for positively correlated steps (shared infrastructure → correlated failures make the actual confidence *lower* than independent calculation suggests). Correlation structure is unmodeled — acknowledged as a limitation.
- The additive log-confidence form is the robust result; $p^n$ is the special case for independent uniform edges. This distinction matters: the qualitative consequence (decay with depth) is robust; the specific rate depends on the conditional structure.


<a id="and-or-scope"></a>

### Scope II.10: *AND/OR Combination Scope*

We restrict to environments where the causal combination of strategy steps is approximately conjunctive (AND: all parents required) or disjunctive (OR: any parent sufficient), without strong interaction effects between parents.

#### Formal Expression

*[Scope Narrowing (and-or-scope)]*

Under this restriction, strategy nodes combine parent contributions via:

**AND-node** (all parents must succeed):

$$P(v \mid \text{parents}) = \prod_{i \in \text{pa}(v)} p_{iv} \cdot P(i)$$

**OR-node** (any parent sufficient):

$$P(v \mid \text{parents}) = 1 - \prod_{i \in \text{pa}(v)} (1 - p_{iv} \cdot P(i))$$

The combination type $\gamma(v) \in \{\text{AND}, \text{OR}\}$ is assigned per node. The causal question determines assignment: "if I remove one parent, can $v$ still be achieved?" YES → OR. NO → AND.

#### Epistemic Status

*Robust qualitative.* This scope narrowing converged independently across three formalism attempts (track-a/00, track-a/02, track-a/03). It captures the dominant structure in most planning domains. The excluded case — complementarity, substitutability, interaction effects between parents — requires richer combination rules and is a legitimate divergence point for future work.

The AND/OR restriction with single-parameter edges gives $k$ parameters per node (one per parent edge) instead of $2^k$ for a general conditional probability table. This parsimony is motivated by bounded cognition ([Formulation I.11](#information-bottleneck)): agents with limited representational capacity are forced toward low-parameter models.

#### Discussion

**Why AND/OR and not alternatives.**

*Why not Noisy-OR universally.* The first formalism attempt used noisy-OR for all nodes. This **systematically overestimates conjunctive structures**:

| Structure | Noisy-OR | AND | Reality |
|-----------|----------|-----|---------|
| 3 required KRs at $p = 0.95, 0.90, 0.99$ | 0.99995 | 0.846 | ~AND |

The noisy-OR model cannot represent "all of these are required." This was the primary motivation for the AND/OR revision.

*Why not WEIGHTED combination.* A clean-slate formalism (track-a/02) introduced $P(v) = \min(1, \sum \alpha_{iv} \cdot p_{iv} \cdot P(i))$ to handle k-of-n thresholds. This reintroduces a two-parameter estimation problem ($\alpha$ weights per edge). If k-of-n semantics are genuinely needed, nested AND/OR structure can represent them: group alternatives into OR-nodes, then AND the groups. This keeps estimation localized to the node taxonomy rather than spreading it across a new per-edge parameter.

**The parsimony argument.** For binary-outcome nodes, AND and OR form a complete Boolean basis — any Boolean combination can be decomposed into layers of AND/OR (disjunctive/conjunctive normal form). Under bounded cognition, the agent needs the most expressive $O(k)$-parameter representation. AND/OR is the natural candidate. This is a parsimony-motivated hypothesis, not a derived necessity — see `scratch/spike-graph-uniqueness.md` for the full argument and its limitations.

**What this scope excludes.** Environments with strong interaction effects: where the value of combining parent contributions is not separable into independent per-parent terms. Examples: synergistic drug interactions (combined effect exceeds sum of individual effects), complementary goods (neither is useful alone), strategic surprise (the combination of actions matters more than any individual action). These require richer parameterizations within the forced graphical structure ([Definition II.11](#strategy-dag)) — a direction for future work.

#### Working Notes

- The AND/OR assignment per node ($\gamma(v)$) is itself uncertain and should be updateable. A node assumed to be OR (alternatives) might turn out to be AND (all required) when the agent discovers unexpected dependencies. $\gamma$ reclassification is rare — it requires strong structural evidence — and operates on a slower timescale than edge-weight updates.
- The parsimony argument applies cleanly to binary outcomes. For continuous or multi-valued outcomes, AND/OR doesn't have the same completeness properties. The natural continuous analogs might be min (AND) and max (OR), or additive and multiplicative combination. Whether there's a completeness result for these is an open question.
- K-of-n thresholds are genuinely common (e.g., "need at least 3 of 5 team members available"). The nested AND/OR representation works but can be verbose. Whether this verbosity is a problem in practice (given bounded cognition constraints) is empirical.


<a id="strategy-dag"></a>

### Definition II.11: *Strategy DAG*

The strategy $\Sigma_t$ is a directed acyclic graph with probabilistic edges and AND/OR combination semantics. Each edge carries the agent's causal credence that completing the parent step advances the child step. The graph encodes the agent's theory of how its actions produce progress toward its objectives.

#### Formal Expression

*[Definition (strategy-dag)]*

$$\Sigma_t = (V_t, E_t, p_t, \gamma_t)$$

where:
- $V_t$: set of **propositional nodes** — each node represents a condition that could be true or false (including action-success propositions at the leaves)
- $E_t \subseteq V_t \times V_t$: directed causal edges
- $p_t : E_t \to [0,1]$: **causal credence** per edge — the agent's confidence that completing the parent advances the child
- $\gamma_t : V_t \to \{\text{AND}, \text{OR}\}$: combination rule per node ([Scope II.10](#and-or-scope))

**Structural constraints:**

1. **Acyclicity.** $\Sigma_t$ is a DAG. This is *derived*, not assumed — see below.
2. **Rootedness.** Every node has a directed path to a unique root terminal $v_\text{root}$ — the single sink node (out-degree 0) of $\Sigma_t$. Compound objectives express their combination structure through the AND/OR machinery below $v_\text{root}$, consistent with scalar $V_{O_t}$ ([Definition II.3](#objective-functional)).
3. **Source constraint.** Leaf nodes are propositions about action success ("action $a$ succeeds at $\tau_v$") or observable conditions ("condition $C_v$ holds at $\tau_v$"). Both are propositional — the distinction is whether the proposition is within the agent's causal control (action) or not (condition).

**Leaf base credence.** For each leaf node $v \in V_t^{\text{leaf}}$, the base credence used in status propagation:

$$p_v(M_t) = \begin{cases} \Pr(\text{action } v \text{ succeeds at } \tau_v \mid M_t) & \text{if } v \text{ is an action node} \\[4pt] \Pr(C_v(\tau_v) \mid M_t) & \text{if } v \text{ is a condition node} \end{cases}$$

where $C_v$ is the propositional condition associated with node $v$ and $\tau_v$ is the node's temporal position (from the acyclicity structure). For action leaves, $p_v$ is *capability credence* — "can I execute this?" For condition leaves, $p_v$ is *state credence* — "will this hold?" Both are conditional on $M_t$ and update whenever $M_t$ updates. This is the mechanism by which Section I's adaptive machinery enters the strategy: $M_t$ changes → leaf credences change → status propagation produces new terminal credences.

**Edge semantics.** Each edge carries a single causal credence weight:

$$p_{ij} = \text{Cr}_i(j \text{ advances} \mid i \text{ completed},\, M_t)$$

This is the agent's credence that completing step $i$ causally advances step $j$, given its current model. In **intervention-rich domains** (software, laboratory science — where the agent performs genuine experiments), this credence approximates the interventional probability $P(j \mid do(i), M_t)$. In **confounded domains** (military, organizational — where evidence is delayed, correlated, or strategically distorted), the credence is weaker: it encodes the agent's best causal belief, but that belief may be biased by observational confounding. The strength of the causal interpretation depends on the domain's identifiability conditions ([Definition I.20](#causal-information-yield), admissibility regimes).

**Status propagation.** Forward pass in topological order, $O(\lvert V \rvert + \lvert E \rvert)$:

$$s_v = \begin{cases} p_v & \text{if } v \text{ is a leaf (base credence)} \\ \prod_{i \in \text{pa}(v)} p_{iv} \cdot s_i & \text{if } \gamma(v) = \text{AND} \\ 1 - \prod_{i \in \text{pa}(v)} (1 - p_{iv} \cdot s_i) & \text{if } \gamma(v) = \text{OR} \end{cases}$$

**Terminal satisfaction conditions.** The root terminal $v_\text{root}$ and any intermediate nodes near the top of the DAG carry **satisfaction conditions**: predicates on environment states/trajectories that the agent treats as operational success criteria for the objective. These conditions operationalize $O_t$ within $\Sigma_t$ — they are the agent's theory of what it means to satisfy the objective. $O_t$ itself lives outside $\Sigma_t$ ([Definition II.5](#strategy-dimension)); the terminal conditions are $\Sigma_t$'s internal encoding of what $O_t$ requires. When $O_t$ changes, terminal conditions must be reassessed and potentially replaced ([Formulation II.19](#structural-change-as-parametric-limit)).

**Well-formedness.** $\Sigma_t$ is **$O_t$-well-formed** when the agent believes that achieving the terminal conditions yields a trajectory that satisfies the objective:

$$\Pr\!\left(O_t \text{ satisfied by } \tau \;\middle\vert\; \text{terminal conditions achieved},\; M_t\right) \geq 1 - \epsilon$$

where "$O_t$ satisfied" means $V_{O_t}(\tau)$ exceeds the objective's own satisfaction criterion (formalized as $V_{O_t}^{\min}$ in [Definition II.13](#satisfaction-gap)). This is a constraint on the relationship between $\Sigma_t$ and $O_t$, not a separate state object. It is explicit and in-principle assessable, though evaluating it requires the same value-side machinery as $A_O$ — it is not a cheap structural test. Violation triggers terminal reassessment: either the terminals need revision (they don't operationalize $O_t$ correctly) or $O_t$ itself needs revision.

**Strategy self-assessment.** The root node's propagated status:

$$\hat{P}_\Sigma(M_t) = s_{v_\text{root}}$$

is the strategy's **plan-confidence score** — the DAG's own answer to "will this plan work?" Under the edge-independence assumption implicit in the AND/OR combination rules, this is a probability. When edges have correlated failures (shared infrastructure, common-mode risks — see Working Notes), it is a heuristic confidence score that systematically overestimates success likelihood. $\hat P_\Sigma$ is explicitly distinct from $A_O$ ([Definition II.13](#satisfaction-gap)), which optimizes over the entire policy class, and from $V_O(\pi_\text{current})$ ([Definition II.4](#value-object)), which evaluates the current policy. $\hat P_\Sigma$ is cheap to compute ($O(\lvert V\rvert + \lvert E\rvert)$ forward pass) and updates in real time as $M_t$ changes through leaf credences.

**Scope of the terminal construction.** Terminal conditions as Boolean predicates with AND/OR aggregation work naturally for threshold, constraint, and composite objectives. For continuous-valued objectives without natural thresholds, the agent must set an operational threshold — introducing a discretization that is a practical proxy, not a lossless encoding of $V_O$. The primary $O_t$ ↔ theory interface remains $V_O$ through the value object ([Definition II.4](#value-object)); terminal conditions are $\Sigma_t$'s internal operational encoding.

**Single-parameter edges.** Each edge carries one number ($p_{ij}$), not two. An earlier formalism attempt used $(p_{ij}, \theta_{ij})$ where $\theta$ was "contribution magnitude." This was dropped because the AND/OR combination rules at nodes absorb $\theta$'s role — the complexity budget goes to one bit per node ($\gamma$) instead of one float per edge.

##### Acyclicity is Derived

*[Derived (from causal-structure + finite planning horizon)]*

Each node in $\Sigma_t$ represents a future event or state with temporal position $\tau_i \gt t$. An edge $X_i \to X_j$ requires $\tau_i \lt \tau_j$ ([Postulate I.7](#causal-structure): causes precede effects). A cycle $X_i \to X_j \to \cdots \to X_i$ would require $\tau_i \lt \tau_j \lt \cdots \lt \tau_i$, which is impossible for a real-valued time index.

Strategies involving iteration ("try A, if fail try B, if fail try A again") are acyclic when time-indexed. The sequence unfolds as:

$$A_1 \to \text{check}_1 \to B_1 \to \text{check}_2 \to A_2 \to \ldots$$

Each attempt is a distinct node at a distinct time. The apparent cycle is a linear chain in the unrolled view.

Formally: a finite set with a strict partial order (future events ordered by time) is representable as a DAG. This is a standard result in order theory.

**Scope of the acyclicity result.** This applies to $\Sigma_t$ (the agent's strategy over the future), not to $M_t$'s model of the environment, which may include cyclic causal processes (feedback loops in the physical world, market dynamics, ecosystem interactions). The acyclicity is specific to the purposeful substate.

#### Epistemic Status

*Conditional* on the [Scope II.10](#and-or-scope) restriction. The DAG structure itself is more strongly motivated — it follows from temporal ordering (acyclicity), probabilistic uncertainty (Cox's theorem forces probability on edges), and a plausible argument that state-local revisability forces the Markov factorization (`scratch/spike-graph-uniqueness.md`). The full argument from operational postulates to DAG structure is a derivation sketch, not yet a proven result — the step from local revisability to the Markov condition needs tightening (see #graph-structure-uniqueness in appendices). The acyclicity derivation above IS tight.

The AND/OR parameterization is a parsimony-motivated formulation choice within the forced graphical structure, not a derived necessity ([Scope II.10](#and-or-scope)). The single-parameter edge convention is similarly a formulation choice motivated by convergence across three independent attempts.

#### Discussion

**The graph structure is forced; the parameterization is chosen.** This is analogous to: probability is forced by Cox's axioms, but the specific distribution for a given problem is a modeling choice. ACT uses DAG + AND/OR because (a) AND/OR is the most parsimonious complete basis for binary combination, (b) the DAG naturally supports causal reasoning, and (c) the representation converged across three independent formalism attempts. Alternative parameterizations within the graphical structure are legitimate research directions.

**Combination assignment is principled but fallible.** The question "if I remove one parent, can $v$ still be achieved?" is derivable from $M_t$'s causal model — it's a principled assignment, not arbitrary. But the assignment can be wrong (false AND = pessimistic over-investment; false OR = optimistic under-investment), and should be updateable when evidence reveals a different structural relationship.

**Connection to Pearl's framework.** The strategy DAG is a causal Bayesian network where the agent is both the modeler and the intervener. Pearl's do-calculus applies in intervention-rich domains where the agent can experimentally verify edge credences. In confounded domains, the DAG degrades to a "best causal belief" structure — useful for planning but with acknowledged potential for systematic bias.

#### Working Notes

- Edge failures are assumed independent in the combination rules. Real systems have correlated failures (shared infrastructure, common-mode risks). The actual confidence is lower than the independent-edge formula suggests. Modeling correlation structure would require augmenting the DAG with hidden common-cause nodes or using a richer parameterization — both increase complexity. Currently acknowledged as a limitation.
- The graph-uniqueness argument (P1-P4 → DAG with Markov property) is the strongest structural justification: temporal ordering + Cox's theorem + local revisability + observable intermediates → directed graphical model with the Markov factorization. If the P3→Markov step can be tightened to a full derivation, strategy-dag could be promoted from Definition to Derived. See `scratch/spike-graph-uniqueness.md`.
- Health metrics (groundedness, observability coverage, weighted redundancy, bottleneck scores) are scaffold — engineering quantities for monitoring DAG health, not principled derivations. They may be useful for implementation but should not enter the theory's formal chain.
- **Satisfaction criterion not yet first-class.** The well-formedness constraint references "the objective's own satisfaction criterion," which is semantically named here but not formally introduced until [Definition II.13](#satisfaction-gap) defines $V_{O_t}^{\min}$. If stricter dependency hygiene is needed, the satisfaction criterion should be introduced as a first-class object in [Definition II.3](#objective-functional) (where $V_{O_t}$ is defined), independent of the gap machinery.
- **Terminal alignment error.** When the agent achieves its terminal conditions but evaluates $V_{O_t}(\tau) \lt V_{O_t}^{\min}$ on the actual trajectory, the well-formedness belief was wrong — the operational success criteria didn't capture what the objective actually required. This is detectable only through experience (achieve the terminals, evaluate $V_{O_t}$), not through a priori analysis. It triggers terminal reassessment — a structural change in $\Sigma_t$ driven by the $O_t$ ↔ terminal mismatch. Whether this should be formalized as a named diagnostic signal ($\delta_\text{align}$) alongside $\delta_\text{sat}$, $\delta_\text{regret}$, and $\delta_\text{strategic}$ is open.


<a id="directed-separation"></a>

### Derived II.12: *Directed Separation*

The epistemic update function $f_M$ is goal-blind: it processes incoming events without reference to the agent's objectives or strategy. The purposeful update $f_G$ depends on the updated epistemic state. Action couples all substates. This directed asymmetry — epistemic update is independent of purpose; purposeful update depends on epistemic state — is the structural backbone of the theory.

#### Formal Expression

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

1. The observation mechanism $h$ may be action-dependent ([Scope I.5](#scope-condition) allows this), but $f_M$ processes whatever event arrives without reference to why the agent sought that event
2. The agent does not use its goals to filter, weight, or interpret observations differently — no goal-dependent attention thresholds or confirmation bias baked into $f_M$

If the agent's goals influence the *observation mechanism* (goal-directed sensing, attention allocation, query selection), the **event that arrives** depends on $G_t$ through $\pi \to a_t \to e_\tau$. But $f_M$ still processes the event goal-blindly. The directed separation is about the **processing** of events, not the **selection** of events.

#### Epistemic Status

*Conditional* on the scope condition above. The scope condition is genuine — many agents we care about violate it to some degree. The conditional claim (IF epistemic update is goal-blind, THEN the separation holds) is exact. Whether any particular agent satisfies the condition is an empirical question about its architecture.

#### Discussion

**This is a genuine scope restriction, not a footnote.** An LLM agent's prompt includes the task objective, which shapes how it interprets code, documentation, and error messages. Its $f_M$ is goal-conditioned in practice: the agent reading code with the goal "fix the auth bug" processes the same code differently than one with "add logging." The epistemic update and purposeful evaluation are entangled in the attention mechanism.

**When the approximation is good:**
- Goal-conditioning affects *attention* (which events to seek) more than *interpretation* (how to process events that arrive)
- The agent has strong epistemic discipline (updates beliefs based on evidence quality, not goal alignment)
- The epistemic update is architecturally separated from goal evaluation (e.g., separate model-update and planning modules)

**When the approximation is poor:**
- The agent exhibits confirmation bias (interpreting ambiguous evidence in goal-consistent ways)
- Goal-conditioning is deeply embedded in the processing architecture (attention-based models where the query includes intent)
- The agent's observation channel is strategically controlled by an adversary who knows the agent's goals

**What directed separation buys the theory.** Section I's $M_t$-side quantities — $\delta$, $\eta^\ast$, $\mathcal{T}$, the persistence condition — remain well-defined on $M_t$ regardless of whether directed separation holds. What directed separation provides is the *clean factorized update*: $M_t$ updates independently, then $G_t$ updates in light of the new $M_t$, and the orient cascade resolves sequentially. Without directed separation, the $M_t$ dynamics depend on $G_t$, the update becomes a coupled system, and the sequential orient cascade becomes an approximation of a simultaneous fixed-point problem. The theory still applies — the quantities are well-defined — but the modular Section I → Section II lift becomes a coupled analysis.

**The deeper question.** Goal-conditioned epistemic dynamics — where $f_M$ depends on $G_t$ — is the formal territory of motivated reasoning, confirmation bias, and wishful thinking. A future extension would model these as departures from directed separation: coupling terms in $f_M$ that create richer (and more fragile) dynamics. The current theory treats this as out of scope, which is honest but leaves the most human-like and LLM-like agents as approximate fits.

#### Working Notes

- The scope condition could be stated more precisely as conditional independence: $M_{\tau^+} \perp G_t \mid (M_{\tau^-}, e_\tau)$. This is the formal content — the epistemic update is independent of the purposeful state conditional on the prior epistemic state and the incoming event. Spelling this out as a conditional independence might make the connection to graphical model theory more explicit.
- For Section V (software-grounded agentic systems), the directed-separation approximation may need to be replaced with a coupled model. The question is: can the theory be extended incrementally (add small coupling terms) or does coupling require a fundamentally different framework? The answer likely depends on the strength of the coupling.
- Directed separation connects to the orient cascade ([Derived II.16](#orient-cascade)): the cascade's ordering ($M_t$ first, then $G_t$) is forced by the information dependency that directed separation establishes. If $f_M$ depended on $G_t$, the cascade ordering would become a simultaneous fixed-point problem, not a sequential resolution.


<a id="satisfaction-gap"></a>

### Definition II.13: *Satisfaction Gap*

The satisfaction gap measures whether the agent's objective is achievable: the distance between what the objective requires and what the best available policy can deliver. It answers "is this goal feasible given what I know and what I can do?"

#### Formal Expression

*[Definition (objective-attainability)]*

$$A_O(M_t;\, \Pi, N_h) = \sup_{\pi \in \Pi} V_O(M_t, \pi;\, N_h)$$

The **objective attainability** — the best achievable value given current beliefs $M_t$, available policy class $\Pi$, and horizon $N_h$.

*[Definition (satisfaction-gap)]*

$$\delta_{\text{sat}} = V_{O_t}^{\min} - A_O(M_t;\, \Pi, N_h)$$

where $V_{O_t}^{\min}$ is the minimum trajectory value that counts as "objective met" — a threshold set by the objective itself (for constraints: all satisfied; for utility: a minimum acceptable level).

- $\delta_{\text{sat}} \gt 0$: The objective is **unmet** under the best available policy, current model, and horizon.
- $\delta_{\text{sat}} \leq 0$: The objective is **attainable** in principle.

**Disambiguation.** $\delta_{\text{sat}} \gt 0$ does NOT automatically mean the goal is wrong. It means the goal is unmet given $(M_t, \Pi, N_h)$. The positive signal has multiple possible causes:

| Cause | Fix | How to distinguish |
|---|---|---|
| Goal is genuinely infeasible | Revise $O_t$ | Persists across $M_t$, $\Pi$, $N_h$ improvements |
| Policy class too narrow | Expand $\Pi$ (structural adaptation of $\Sigma_t$) | $\delta_{\text{sat}}$ decreases when richer policies are tried |
| Horizon too short | Extend $N_h$ | $\delta_{\text{sat}}$ decreases with longer planning horizon |
| Model is wrong about feasibility | Improve $M_t$ (reduce $\delta_{\text{epistemic}}$) | $\delta_{\text{sat}}$ changes when $M_t$ is corrected |

Objective revision is the **last resort**, not the first response to unmet goals. The orient cascade ([Derived II.16](#orient-cascade)) formalizes this ordering.

#### Epistemic Status

*Exact.* The satisfaction gap is a mathematical definition — the difference between a threshold and a supremum over a function class. The definition is precise; the *computation* of $A_O$ is generally intractable (it requires optimization over a policy class), but the quantity is well-defined.

#### Discussion

**Why two gap measures, not one.** An earlier formulation used a single $\delta_{\text{objective}}$ for goal-related mismatch. This conflates two distinct situations: "the goal is too hard" and "the strategy is too weak." When the agent is optimally pursuing an infeasible goal, $\delta_{\text{objective}}$ is large but there's no strategy to improve — the problem is the goal, not the plan. The satisfaction gap ($\delta_{\text{sat}}$) and control regret ([Definition II.14](#control-regret)) separate these cases, enabling the right corrective action.

**The disambiguation table is load-bearing.** Without it, an agent facing $\delta_{\text{sat}} \gt 0$ might immediately revise its objective when the real problem is an inadequate model or a too-narrow policy class. The table encodes the diagnostic procedure: check $M_t$ adequacy first (maybe the goal IS feasible but the model doesn't know it), then check $\Pi$ and $N_h$, and only then consider revising $O_t$.

**Dependence on $M_t$.** $A_O$ is computed from $M_t$, not from the true environment state $\Omega_t$. The agent's assessment of attainability could be wrong — an achievable goal might look unachievable with a bad model, or vice versa. Improving $M_t$ (reducing $\delta_{\text{epistemic}}$) brings the agent's attainability assessment closer to reality. This is why the orient cascade puts epistemic update before attainability evaluation.

#### Working Notes

- $V_{O_t}^{\min}$ (the satisfaction threshold) is a property of the objective, not of the agent. For constraint-satisfaction objectives, it's natural (all constraints met = satisfied). For utility-maximizing objectives, it's less obvious — what counts as "good enough"? This threshold may need to be explicitly modeled as part of $O_t$.
- The supremum in $A_O$ is over $\Pi$, the available policy class. For agents with explicit $\Sigma_t$, $\Pi$ corresponds to the set of strategies representable in the agent's DAG formalism. Expanding $\Pi$ (structural adaptation of $\Sigma_t$ — adding nodes, edges, or changing $\gamma$ assignments) is the purposeful analog of [Result I.26](#structural-adaptation-necessity).


<a id="control-regret"></a>

### Definition II.14: *Control Regret*

Control regret measures the gap between the best achievable performance and the agent's current performance — how much the agent is leaving on the table by following its current policy rather than the best available one. This is the signal for strategy revision.

#### Formal Expression

*[Definition (control-regret)]*

$$\delta_{\text{regret}} = A_O(M_t;\, \Pi, N_h) - V_O(M_t, \pi_{\text{current}};\, N_h) \geq 0$$

Always non-negative: the current policy cannot outperform the best in its class.

- $\delta_{\text{regret}} \approx 0$: The agent is doing the best it can within current $(\Pi, N_h, M_t)$. If $\delta_{\text{sat}} \gt 0$ simultaneously, the problem is not the current strategy — it's either the goal, the capability ($\Pi$, $N_h$), or the model ($M_t$). See [Definition II.13](#satisfaction-gap)'s disambiguation.
- $\delta_{\text{regret}} \gg 0$: There's room for improvement without changing $O_t$. → Revise $\Sigma_t$.

#### Epistemic Status

*Exact.* Like the satisfaction gap, this is a mathematical definition — a difference between two values of the same functional. The quantity is well-defined; computing it requires evaluating $A_O$ (generally intractable) and $V_O$ under the current policy (tractable in simulation, approximate in practice).

#### Discussion

**The diagnostic power of the two-gap system.** The satisfaction gap and control regret together encode a 2×2 diagnostic:

| | $\delta_{\text{sat}} \leq 0$ (attainable) | $\delta_{\text{sat}} \gt 0$ (unmet) |
|---|---|---|
| $\delta_{\text{regret}} \approx 0$ (near-optimal) | **Success**: goal achievable, policy good | **Capability limit**: optimally pursuing an unmet goal → check $M_t$, $\Pi$, $N_h$, then consider revising $O_t$ |
| $\delta_{\text{regret}} \gg 0$ (suboptimal) | **Strategy problem**: goal achievable, policy poor → revise $\Sigma_t$ | **Both**: goal hard AND strategy weak → revise $\Sigma_t$ first, then reassess $\delta_{\text{sat}}$ |

This diagnostic is what makes the orient cascade ([Derived II.16](#orient-cascade)) actionable: each cell prescribes a different corrective action.

**Control regret as the signal for $\Sigma_t$ revision.** When $\delta_{\text{regret}}$ is high, the agent knows it could do better with a different strategy. The *specific* corrections — which edges to revise, which branches to prune, which alternatives to add — come from the strategic calibration residual ([Definition II.15](#strategic-calibration)), which localizes the regret to specific parts of $\Sigma_t$.

**Regret approaching zero when optimally failing.** This is the key insight motivating the two-gap split. A single $\delta_{\text{objective}}$ would show "large gap" for both "bad strategy, achievable goal" and "good strategy, impossible goal." The first warrants strategy revision; the second warrants goal revision (after ruling out $M_t$/$\Pi$/$N_h$ inadequacy). Without the split, the agent cannot distinguish these cases and may waste effort optimizing a strategy that's already near-optimal for an infeasible goal.


<a id="strategic-calibration"></a>

### Definition II.15: *Strategic Calibration*

The strategic calibration residual measures whether the strategy's causal model is correct: are the edges in $\Sigma_t$ accurate predictors of how much value each step actually produces? This is the fine-grained diagnostic that localizes control regret to specific parts of the strategy.

#### Formal Expression

*[Definition (strategic-calibration)]*

For each edge $(i, j)$ in $\Sigma_t$ with credence $p_{ij}$, the **edge residual**:

$$r_{ij} = \mathbb{E}[\Delta V_O \mid \text{edge } (i,j) \text{ traversed},\, M_t] - \Delta V_O^{\text{observed}}$$

where $\Delta V_O$ is the change in $V_O(M_t, \pi;\, N_h)$ attributable to completing step $j$ — as predicted by $\Sigma_t$ versus as observed.

The **strategic calibration residual** aggregates across active edges:

$$\delta_{\text{strategic}} = \left(\sum_{(i,j) \in \text{active}} w_{ij} \cdot r_{ij}^2 \right)^{1/2}$$

where $w_{ij}$ weights edges by importance (e.g., criticality to the current plan's critical path).

**Conditioning.** The edge residual $r_{ij}$ is meaningful only when:
- The edge was actually traversed (the agent attempted the step)
- $M_t$ is adequate (so the observed $\Delta V_O$ is meaningful, not noise)
- The agent followed $\Sigma_t$'s prescription for step $j$ (execution fidelity — otherwise the residual conflates bad plan with bad execution)

Without the execution fidelity condition, a positive residual could mean "the plan is wrong" or "the agent didn't follow the plan." These require different corrections ($\Sigma_t$ revision vs. execution improvement).

#### Epistemic Status

*Discussion-grade.* The edge residual concept is well-motivated: each edge predicts a value increment, and comparing prediction to observation is standard calibration. But the specific aggregation ($L^2$ norm with importance weights) is a reasonable first pass, not a derived result. The weighting scheme ($w_{ij}$ by criticality) is sensible but ungrounded. The conditioning requirements (especially execution fidelity) make this quantity hard to estimate in practice — the agent must know whether it followed its own plan, which requires a level of self-monitoring that many agents lack.

This is a **second-order inference** — it requires accumulating evidence over multiple edge traversals. It is inherently slower to evaluate than $\delta_{\text{epistemic}}$ (which updates on every observation) or $\delta_{\text{sat}}$ (which can be evaluated from $M_t$ and $\Sigma_t$ alone).

#### Discussion

**Connection to [Proposed schema II.20](#strategy-persistence-schema).** $\delta_{\text{strategic}}$ is the candidate strategic mismatch state for the persistence schema. The correction function would be edge-credence revision (reducing $p_{ij}$ when $r_{ij}$ is persistently positive, increasing when consistently negative — see [Hypothesis II.18](#edge-update-via-gain)). The disturbance would be environmental changes that alter edge-traversal outcomes. Whether this correction satisfies the sector condition remains open.

**Typing as value-increment residuals.** Each edge predicts a scalar (value increment), not a full state transition. This is the most tractable typing because it connects directly to the value object $V_O$ and allows aggregation across heterogeneous step types (a military advance and a logistics delivery produce different state changes but both produce value increments measurable on the same scale).

#### Working Notes

- The aggregation into a single $\delta_{\text{strategic}}$ may lose important structure. A per-edge or per-path profile of residuals would be more informative for diagnosis: which parts of the strategy are well-calibrated and which are not? The scalar summary is useful for the persistence condition (which needs a single mismatch magnitude) but not for strategy revision (which needs to know WHERE the problem is).
- Alternative aggregation: maximum edge residual (worst-calibrated edge), or weighted by information value (edges the agent is most uncertain about). The right aggregation depends on the use case.
- Execution fidelity monitoring is a genuine challenge for agents that don't have a clear execution trace. For software agents operating through tool calls, execution fidelity is relatively easy to assess (did the agent issue the right commands?). For organizational agents, it's much harder (did the subordinate actually follow the directive, or reinterpret it?).


<a id="orient-cascade"></a>

### Derived II.16: *Orient Cascade*

The resolution order for updating the agent's state is forced by information dependency: epistemic update first, then attainability assessment, then strategy evaluation, then (if needed) objective revision. Each step's input depends on the output of prior steps. The ordering is not a design choice — it's a consequence of which quantities require which others.

#### Formal Expression

*[Derived (orient-cascade, from information dependency between mismatch types)]*

1. **Reduce $\delta_{\text{epistemic}}$** — understand reality.
   Update $M_t$ via [Definition I.17](#mismatch-signal) and [Empirical I.19](#update-gain). Prerequisite for all purposeful evaluation, because $M_t$ appears in every subsequent formula.

2. **Evaluate $\delta_{\text{sat}}$** — is the goal achievable?
   Compute $A_O(M_t; \Pi, N_h)$ using the updated $M_t$. Requires adequate $M_t$ to assess attainability ([Definition II.13](#satisfaction-gap)).

3. **If feasible ($\delta_{\text{sat}} \leq 0$), evaluate $\delta_{\text{regret}}$** — is the policy suboptimal?
   Compare $A_O$ to $V_O(M_t, \pi_{\text{current}}; N_h)$. Requires both adequate $M_t$ and meaningful $A_O$ ([Definition II.14](#control-regret)).

4. **If $\delta_{\text{regret}}$ high, evaluate $\delta_{\text{strategic}}$** — is the plan's causal model wrong?
   Examine edge residuals. Requires adequate $M_t$, feasible $O_t$, and evidence of suboptimal execution ([Definition II.15](#strategic-calibration)).

5. **If $\delta_{\text{sat}} \gt 0$ persists across $\Sigma_t$ revisions** — revise $O_t$.
   The cascade's ordering ensures objective revision is the last resort, not the first response to unmet goals.

**Derivation.** Each step's input depends on prior steps' outputs:
- You cannot evaluate strategy quality with a broken reality model (step 3 requires step 1)
- You cannot distinguish bad strategy from infeasible goal without evaluating attainability first (step 4 requires step 2)
- You should not revise the objective until you've verified that improving $\Sigma_t$ cannot close the gap (step 5 requires steps 3-4)

The ordering is forced by information dependency.

#### Epistemic Status

*Exact.* The cascade ordering is a logical consequence of which quantities appear in which formulas. If you define the mismatch signals as we have ([Definition I.17](#mismatch-signal), [Definition II.13](#satisfaction-gap), [Definition II.14](#control-regret), [Definition II.15](#strategic-calibration)) and accept [Derived II.12](#directed-separation), the resolution order follows. What is NOT derived is the *timing* — how long the agent should spend on each step before proceeding. The ordering is forced; the resource allocation across steps is open.

#### Discussion

**$G_t$ complexity bounded by $M_t$ capacity.** $\Sigma_t$'s evaluable complexity is bounded by $M_t$'s ability to observe which strategy edges are intact. An agent with poor model sufficiency ($S(M_t) \ll 1$) cannot meaningfully evaluate a complex $\Sigma_t$ — the strategic calibration residual requires adequate $M_t$ to distinguish "edge prediction wrong" from "observation too noisy to tell."

This creates a **virtuous cycle**: better $M_t$ → richer evaluable $\Sigma_t$ → better-directed action → faster $M_t$ improvement. And a **vicious one**: degraded $M_t$ → forced strategy simplification → cruder action → further $M_t$ degradation. The vicious cycle is the strategic analog of the death spiral described in the persistence condition ([Result I.24](#persistence-condition)) — the agent loses the capacity to maintain complex plans, which reduces the quality of its actions, which further degrades its model.

**Connection to Boyd's OODA.** The orient cascade is the formal analog of Boyd's "Orient" — not just model updating, but the structured interaction between reality-understanding and strategy. Boyd's insight was that Orient is the critical step, not Decide. The cascade provides a mathematical mechanism consistent with this insight: Orient resolves the information dependencies that make Decide meaningful. An agent that skips to Decide (strategy revision) without adequate Orient (model update + attainability assessment) will revise its strategy based on stale or incorrect beliefs. Whether the dependency structure in the cascade captures the actual cognitive process Boyd described is an empirical question.

**Timescale structure.** The cascade implies a natural timescale ordering for the different update types:

$$\nu_{\text{epistemic}} \gg \nu_{\text{edge-update}} \gg \nu_{\gamma\text{-reclassify}} \gg \nu_{\text{prune/graft}} \gg \nu_{O\text{-revision}}$$

Weight updates are frequent (every observation). Combination-type reclassification is rare (needs strong structural evidence). Pruning/grafting is rarer still (abandon or create causal hypotheses). Objective revision is rarest (change what you want, not how you get it). This ordering is an empirical observation for many agent populations, consistent with the cascade but not derived from it.

#### Working Notes

- The cascade as stated is sequential. In practice, agents may run steps in partial overlap — beginning to assess $\delta_{\text{sat}}$ before $M_t$ is fully updated, or revising edges while still processing observations. The cascade describes the *logical* dependency, not the *temporal* scheduling. An agent that parallelizes steps must still respect the dependencies (don't finalize strategy revision using a stale $M_t$).
- The resource allocation question (how much of the agent's tempo budget to spend on each step) is open and may be domain-dependent. In fast-changing environments, the agent may need to truncate early steps to keep up. In stable environments, the agent can spend more time on deep strategic evaluation.
- The virtuous/vicious cycle between $M_t$ quality and $\Sigma_t$ evaluable complexity is structurally motivated but not formally derived. Formalizing it would require a coupled dynamics model — possibly an extension of the persistence framework to the $(M_t, \Sigma_t)$ pair.


<a id="observability-dominance"></a>

### Derived II.17: *Observability Dominance*

Unobservable strategy edges cannot be updated — the gain principle drives their update rate to zero. This means the agent's effective strategy is limited to the parts it can observe, regardless of the nominal confidence in unobservable paths. Observability dominates nominal confidence in determining which strategies are epistemically alive.

#### Formal Expression

*[Derived (observability-dominance, from update-gain + strategy-dag)]*

For a path $P$ through $\Sigma_t$, the **path observability**:

$$\text{obs}(P) = \min_{v \in P} \sigma_v$$

where $\sigma_v$ is the observability of node $v$ — how well the agent can determine whether $v$ has been achieved. The weakest link determines the path's observability.

**Observability-adjusted confidence:**

$$\text{conf}_{\text{obs}}(P) = \text{conf}(P) \cdot \text{obs}(P)$$

When $\sigma_v \approx 0$ for any node $v$ on the path: by [Empirical I.19](#update-gain), $\eta_{\text{edge}} = U_{\text{edge}} / (U_{\text{edge}} + U_{\text{obs}}) \to 0$ as $U_{\text{obs}} \to \infty$. The edges connecting to $v$ are **frozen at their prior** — the agent cannot update them regardless of what happens. The path is epistemically dead.

#### Epistemic Status

*Robust qualitative.* The mechanism (high observation noise → low gain → frozen edges) is a direct consequence of [Empirical I.19](#update-gain)'s uncertainty ratio. The specific functional form ($\text{conf}_{\text{obs}} = \text{conf} \cdot \text{obs}$) is a first-order approximation — the actual relationship between observability and effective confidence is more complex (it depends on how many observations are accumulated, the prior strength, and the noise structure). The qualitative prediction (low observability → frozen beliefs → ineffective strategy) is robust.

#### Discussion

**Observability as the gateway to learning.** An agent choosing between a strong-but-blind path (high $\text{conf}(P)$, low $\text{obs}(P)$) and a weak-but-visible path (lower $\text{conf}(P)$, high $\text{obs}(P)$) should prefer the visible one. After one attempt: the visible path yields large $\eta_{\text{edge}}$ — the agent quickly learns whether it works and can redirect. The blind path yields tiny $\eta_{\text{edge}}$ — the agent is still guessing after $n$ attempts. Observability enables learning; opacity prevents it.

**Unobservable regions are absorbing.** Once significant strategy investment operates through unobservable nodes: frozen beliefs → no mismatch signal → no reason to revise → the agent cannot learn and cannot recognize that it cannot learn. Escape requires external shock, proactive observability investment (instrumenting previously unmonitored nodes), or another agent whose observations cover the blind spot ([Hypothesis III.9](#communication-gain)).

**Connection to [Discussion IV.11](#code-quality-as-observation-infrastructure).** In the software domain, code quality directly determines $\sigma_v$ — well-structured code with good tests makes strategy steps (features, refactors, deployments) observable. Poor code quality reduces observability, freezing the developer's causal beliefs about what changes will accomplish. This makes code quality a strategic concern, not just an aesthetic one.

**Optimal decomposition depth.** Finer decomposition (more intermediate nodes) provides earlier failure detection — detect a problem at step $k$ rather than discovering it at step $n$. But finer decomposition also increases the number of uncertain edges ([Derived II.9](#chain-confidence-decay)). The optimal decomposition depth balances incremental confirmation against compound decay: decompose as finely as observation channels allow, but no finer.

#### Working Notes

- The absorbing-state property of unobservable regions is a strong prediction. In organizational settings, it predicts that departments with poor measurement (R&D, strategy groups, some management functions) will develop persistent, untested beliefs about their own effectiveness. The theory predicts this is structural (frozen $\eta_{\text{edge}}$), not motivational.
- Observability is not binary — it's a spectrum. Partial observability (noisy observations of intermediate results) gives partial gain, which gives slow but nonzero learning. The diagnostic question is whether the learning rate is fast enough to maintain strategy persistence given the environment's rate of change ($\rho$).


<a id="edge-update-via-gain"></a>

### Hypothesis II.18: *Edge Update via Gain*

The uncertainty-ratio gain principle ([Empirical I.19](#update-gain)) extends from epistemic updates to strategy-edge updates: edge credences revise in proportion to the ratio of edge uncertainty to observation noise. This gives a principled, conservative update rule that avoids overreacting to single observations.

#### Formal Expression

*[Hypothesis (edge-update-via-gain)]*

Edge credences update via:

$$p_{ij}^{\text{new}} = p_{ij}^{\text{old}} + \eta_{\text{edge}} \cdot \left(\text{signal}(o_t, i, j) - p_{ij}^{\text{old}}\right)$$

where:
- $\text{signal}(o_t, i, j) \in [0, 1]$: evidential content of observation $o_t$ about the causal link $i \to j$
- $\eta_{\text{edge}} = U_{\text{edge}} / (U_{\text{edge}} + U_{\text{obs}})$: update gain

with:
- $U_{\text{edge}}$: uncertainty about this specific causal link. If $p_{ij} \sim \text{Beta}(\alpha_{ij}, \beta_{ij})$: $U_{\text{edge}} = \text{Var}[\text{Beta}] = \alpha\beta / ((\alpha + \beta)^2(\alpha + \beta + 1))$
- $U_{\text{obs}}$: observation noise on the channel confirming this link. $U_{\text{obs}} \propto 1/\sigma_j$ (inverse of observability of node $j$)

**Beta-Bernoulli equivalence.** For binary observations (success/failure of step $j$):
- Observe success: $\alpha_{ij} \to \alpha_{ij} + 1$
- Observe failure: $\beta_{ij} \to \beta_{ij} + 1$
- Point estimate: $p_{ij} = \alpha / (\alpha + \beta)$

This is the standard Bayesian update for a Bernoulli process — the gain principle reduces to conjugate updating in the binary case.

#### Epistemic Status

*Hypothesis.* The extension of the gain principle from $M_t$ to $\Sigma_t$ edges is structurally motivated: the same uncertainty-ratio logic applies wherever an agent updates a belief in response to noisy evidence. But the extension has not been validated independently. Specific open questions:

- **The signal function** $\text{signal}(o_t, i, j)$ is not specified. How does an observation about node $j$ translate into evidence about edge $i \to j$ specifically? In the binary case (step succeeded or failed) it's clear. In continuous domains, extracting per-edge evidence from aggregate observations is a proper inference problem — potentially requiring the agent to solve an attribution problem (which edge caused the observed outcome?).
- **Identifiability**: when multiple edges contribute to an observation, attributing evidence to specific edges requires causal identification assumptions. In intervention-rich domains (software: run a specific test), this is tractable. In confounded domains (organizational: multiple initiatives contributed to the quarterly results), it's genuinely hard.
- **Interaction with $M_t$ updates**: edge updates use observations that have already been used for $M_t$ updates (the orient cascade processes $M_t$ first). Whether this creates statistical dependencies that bias the edge update is not analyzed.

#### Discussion

**Connection to [Derived II.17](#observability-dominance).** When $\sigma_j \approx 0$: $U_{\text{obs}} \to \infty$, $\eta_{\text{edge}} \to 0$. The edge is frozen at its prior. Unobservable links cannot be updated — this is the mechanism that makes unobservable paths epistemically dead.

**Connection to [Definition II.15](#strategic-calibration).** The edge update rule is the correction function that the strategic calibration residual calls for: persistently positive $r_{ij}$ (predicted value increment exceeds observed) should reduce $p_{ij}$; persistently negative $r_{ij}$ should increase it. The gain principle provides the update magnitude — how much to adjust given the evidence strength.

**Conservative by design.** The uncertainty ratio ensures the agent doesn't overreact to single observations: a well-established edge ($\alpha + \beta$ large, $U_{\text{edge}}$ small) requires strong evidence to revise; a newly hypothesized edge ($\alpha + \beta$ small, $U_{\text{edge}}$ large) is easily moved by evidence. This mirrors the epistemic gain's behavior for $M_t$ — the agent trusts accumulated experience over individual observations.

#### Working Notes

- The signal function is the critical missing piece. For each edge, the agent needs to evaluate: "given what I just observed, how much evidence does this provide about the causal link $i \to j$?" Designing this for binary outcomes is straightforward; for continuous outcomes with multiple contributing edges, it requires causal attribution. This may be where the edge-identifiability conditions (WORKBENCH open question) become concrete.
- The Beta-Bernoulli model assumes edge outcomes are i.i.d. Bernoulli draws. This is adequate for many settings but misses: (a) time-varying edge reliability ($p_{ij}$ drifting), (b) context-dependent reliability ($p_{ij}$ varies with environmental conditions), (c) correlated edge outcomes. Extending to time-varying priors (discounting old evidence) would connect to the mismatch dynamics framework.


> **\[GAP\]** When observational edge updates yield valid causal semantics


<a id="structural-change-as-parametric-limit"></a>

### Formulation II.19: *Structural Change as Parametric Limit*

In the probabilistic DAG, "structural" changes to $\Sigma_t$ are continuous operations on edge weights and node sets — not a separate mechanism. Pruning is a credence dropping below threshold; grafting is a new causal hypothesis initialized at a prior. This dissolves the sharp line between parametric update (adjusting weights) and structural change (adding/removing edges).

#### Formal Expression

*[Formulation (structural-change-as-parametric-limit)]*

The six operations on $\Sigma_t$, ordered from most to least frequent:

| Operation | What changes | Trigger |
|-----------|-------------|---------|
| Reweighting | Edge credence $p_{ij}$ | New observation about the link ([Hypothesis II.18](#edge-update-via-gain)) |
| $\gamma$ reclassification | Node combination type AND↔OR | Strong structural evidence that combination semantics changed |
| Pruning | Remove failed branch ($p_{ij} \to \approx 0$) | Credence drops below viability threshold |
| Grafting | Add new branch ($0 \to p_{ij}$) | Discovery of a new possible path (initialized at prior) |
| Objective revision | Change terminal nodes | Feasibility failure or opportunity ([Definition II.13](#satisfaction-gap)) |
| Full restructure | Replace entire $\Sigma_t$ | Catastrophic failure ([Result I.26](#structural-adaptation-necessity)) |

A healthy agent does continuous strategic maintenance (reweight, occasionally prune and graft) and rarely reaches catastrophic restructuring. Full restructure is the strategic analog of [Result I.26](#structural-adaptation-necessity)'s model-class change — the rare, expensive event when the entire representational structure must be replaced.

#### Epistemic Status

*Robust qualitative.* The continuity claim (structural change as parametric limit) is a property of the probabilistic representation: in a space where edges carry real-valued credences, adding or removing an edge is a boundary event, not a discontinuity. The frequency ordering of operations is an empirical pattern, not a derived result — it's consistent with the observation that deeper changes (restructuring > pruning > reweighting) require more evidence and are more costly.

#### Discussion

**Connection to TF-10's destruction-creation.** [Result I.26](#structural-adaptation-necessity) describes the rare case when the entire model class must be replaced — the agent's representational framework is fundamentally inadequate. In the strategy DAG, this corresponds to full restructure: the causal theory encoded in $\Sigma_t$ is so wrong that incremental revision (reweighting, pruning) cannot fix it. The DAG must be rebuilt from a different starting point.

The key insight is that this extreme case is the *limit* of the continuous process, not a separate mechanism. An agent that maintains healthy strategic hygiene (regular reweighting, timely pruning of failing branches, proactive grafting of alternatives) will rarely need full restructure. An agent that neglects maintenance — letting failing branches persist, ignoring negative evidence — accumulates strategic debt until catastrophic restructuring becomes unavoidable.

**Pruning and grafting thresholds.** When should the agent prune (remove an edge with very low credence) rather than just keeping it at low $p_{ij}$? The answer involves the cognitive cost of maintaining edges in $\Sigma_t$ — each edge consumes representational capacity and evaluation time. For agents with bounded representational capacity (LLMs with finite context windows), pruning is necessary to keep $\Sigma_t$ within capacity. The threshold is domain-dependent and connects to the open question of cognitive cost of $\Sigma_t$ ([Definition II.5](#strategy-dimension) Working Notes).

#### Working Notes

- The timescale ordering (reweight ≫ reclassify ≫ prune/graft ≫ revise $O_t$ ≫ full restructure) is an empirical observation that should be testable. In software development: edge reweighting ≈ updating confidence after a test passes/fails; $\gamma$ reclassification ≈ realizing two tasks are both required (not alternatives); pruning ≈ abandoning an approach that isn't working; grafting ≈ discovering a new approach; objective revision ≈ changing the feature scope; full restructure ≈ starting the project over.
- Grafting (adding new edges) is qualitatively different from other operations because it requires the agent to hypothesize a causal relationship that isn't in its current $\Sigma_t$. Where do new causal hypotheses come from? From $M_t$ (the model suggests a possible path), from external sources ([Hypothesis III.9](#communication-gain) — another agent suggests an approach), or from exploration ([Definition I.20](#causal-information-yield) — the agent discovers an unexpected effect). This is the creative step in strategic revision.


> **\[GAP\]** Rate of useful $\Sigma_t$ revision (adaptive tempo for strategy)


> **\[GAP\]** Complexity cost of maintaining $\Sigma_t$ (IB/MDL for DAGs)


<a id="strategy-persistence-schema"></a>

### Proposed-schema II.20: *Strategy Persistence Schema*

The sector-condition mathematics ([Result I.25](#sector-condition-stability), [Derivation A.1](#sector-condition-derivation)) proves bounded mismatch for any system with: a mismatch state, a correction function satisfying sector bounds, and bounded disturbance. This mathematics is domain-agnostic — it doesn't care whether the mismatch is epistemic or strategic. If the strategic update dynamics can be shown to satisfy the same structural conditions, strategy persistence follows by the same result.

#### Formal Expression

*[Proposed Schema (strategy-persistence-schema)]*

**If** strategic update dynamics satisfy:
- **(SA1)** Zero correction at zero strategic mismatch: when $\delta_{\text{strategic}} = 0$, no revision occurs
- **(SA2')** Local sector condition on strategic correction: the correction function is appropriately bounded
- Bounded strategic disturbance: the rate at which the environment invalidates causal links is bounded

**Then** $\Sigma_t$ persists iff:

$$\alpha_\Sigma \gt \frac{\rho_\Sigma}{R_\Sigma}$$

where $\alpha_\Sigma$ is the strategic correction rate, $\rho_\Sigma$ is the strategic disturbance rate, and $R_\Sigma$ is the strategic reserve (tolerance for strategic mismatch before performance degrades catastrophically).

#### Epistemic Status

*Sketch.* This is a **result schema**, not a proven result. The mathematical template (sector conditions → bounded mismatch) is derived ([Derivation A.1](#sector-condition-derivation)). What's missing is the instantiation — showing that specific strategic update dynamics satisfy the template's preconditions. The schema says: "if the shape fits, the conclusion follows." Whether the shape fits is genuine future work.

#### Discussion

**What's needed to promote this from schema to result.**

1. **Strategic mismatch state**: The candidate is $\delta_{\text{strategic}}$ from [Definition II.15](#strategic-calibration) — the aggregated edge residual. This needs to be shown to satisfy the properties required by the sector-condition framework (well-defined zero, monotonicity, appropriate norm structure).

2. **Strategic correction function**: How $\Sigma_t$ revises in response to $\delta_{\text{strategic}}$. The candidate is edge-credence revision via [Hypothesis II.18](#edge-update-via-gain). This needs to be shown to satisfy the sector condition (SA2'): the correction is bounded above and below by functions of the mismatch magnitude, with appropriate constants.

3. **Strategic disturbance**: The rate at which the environment invalidates causal links in $\Sigma_t$. Candidates: requirement changes (what the agent needs to achieve changes), resource changes (what's available changes), adversary actions (the opponent disrupts the agent's causal links), state decay (previously true causal relationships weaken over time). This needs to be bounded (or shown to satisfy statistical stationarity conditions).

4. **Sector condition verification**: The critical mathematical step. Even if the correction function and disturbance are well-defined, the sector condition is a quantitative requirement — not all correction functions satisfy it. The gain-based edge update is a good candidate (the gain principle is inherently conservative — it bounds the correction), but this hasn't been verified.

**The structural parallel is genuine.** The persistence condition for $M_t$ ([Result I.24](#persistence-condition)) says: adaptive tempo must exceed the ratio of disturbance to critical mismatch. If the same mathematics applies to $\Sigma_t$, then strategy persistence requires strategic tempo to exceed the ratio of strategic disturbance to critical strategic mismatch. The strategic analog of "the environment changes faster than the agent can learn" is "the world invalidates plans faster than the agent can revise them." Both lead to the same catastrophic outcome: the system cannot maintain bounded mismatch and begins to degrade.

**What this would buy the theory.** If promoted to a result, strategy persistence would:
- Provide a formal criterion for "when does a strategy remain viable?"
- Connect strategic failure modes to the same mathematical framework as epistemic failure modes
- Enable quantitative comparison: is the bottleneck epistemic persistence (model can't keep up with reality changes) or strategic persistence (plans can't keep up with requirement changes)?
- Ground the organizational intuition that plans need to be revised faster than the situation changes

#### Working Notes

- The most natural first step toward promotion: verify the sector condition for the simplest case — a single-edge strategy with binary outcomes and Beta-Bernoulli updating. If the sector condition holds for this toy case, it motivates the effort to verify it for the full DAG. If it fails even here, the schema may need structural revision.
- The strategic disturbance $\rho_\Sigma$ is qualitatively different from epistemic disturbance $\rho$. Epistemic disturbance is about the environment changing (physical state evolves). Strategic disturbance is about the agent's causal theory becoming invalid (the intervention-outcome mapping shifts). These can be correlated (a changing environment invalidates both model and strategy) but they're not the same quantity.
- The stochastic treatment (from track-b simulations) suggests $\rho_\Sigma / \sqrt{\mathcal T_\Sigma}$ rather than $\rho_\Sigma / \mathcal T_\Sigma$ for the steady-state strategic mismatch. If this carries over from the epistemic domain, the persistence threshold is different in the stochastic case. Whether strategic disturbance is better modeled as deterministic or stochastic drift is domain-dependent.


> **\[GAP\]** Three-way exploit/explore/deliberate allocation with $\Sigma_t$



---

## III. Agentic Composites

*Scope: multiple agents interacting through a shared environment, or equivalently, the internal structure of composite agents. The composition postulate ([Postulate I.6](#composition-consistency)) ensures the theory applies at every level of description; this section develops what happens when composition is imperfect and what the dynamics of inter-agent interaction look like.*

*Correlated observations as default; independence as the special case requiring justification. Adversarial dynamics are one end of a teleological unity spectrum, not a separate theory.*

*Two sources: the simulation-validated adversarial dynamics from TFT (TF-11/Appendix F, track-b simulations), and the composition spike (`scratch/spike-agent-composition.md`) which derives the requirement for composition consistency from the scope condition's level-independence.*


<a id="multi-agent-scope"></a>

### Scope III.1: *Multi-Agent Scope*

Section III applies wherever multiple agents satisfying the scope condition interact through a shared environment. Each agent observes, acts, and faces uncertainty; their actions affect each other's environments. This is the general case for organizations, teams, ecosystems, and adversarial encounters. Independence (agents whose actions don't affect each other) is the special case requiring justification.

#### Formal Expression

*[Scope (multi-agent-scope)]*

A multi-agent system consists of $N$ agents $\{A_1, \ldots, A_n\}$, each satisfying the scope condition ([Scope I.5](#scope-condition)), interacting through a shared environment with state $\Omega_t \in \mathcal{S}_{env}$:

- Each agent $A_i$ has state $X_t^{(i)} = (M_t^{(i)}, G_t^{(i)})$
- Each agent observes: $o_t^{(i)} = h^{(i)}(\Omega_t, a_t^{(\neg i)}, \xi_t^{(i)})$ — observations may depend on other agents' actions
- Each agent acts: $a_t^{(i)} = \pi^{(i)}(X_t^{(i)})$
- The environment evolves: $\Omega_{t+1} = T(\Omega_t, a_t^{(1)}, \ldots, a_t^{(n)}, \omega_t)$

The coupling is through the environment: agent $i$'s actions enter agent $j$'s observation function and the shared environment transition. Agents may also communicate directly (a special case of action-observation coupling with a dedicated channel).

#### Epistemic Status

*Axiomatic.* This is a scope definition — it describes the class of systems Section III addresses. The only substantive choice is that coupling goes through the shared environment rather than through direct state modification. This follows from the agent boundary assumption ([Definition I.2](#agent-environment)): agents affect each other by affecting the environment, not by directly altering each other's internal states.

#### Discussion

**Correlated observations as default.** When agents share an environment, their observations are generically correlated — they see aspects of the same reality. Independence (uncorrelated observations) requires the agents to observe non-overlapping aspects of the environment, which is the special case. Most multi-agent settings of interest involve substantial observation correlation.

**The adversarial case is one end of a spectrum.** Agents whose objectives conflict are not a separate theory — they are multi-agent systems with negative teleological unity ([Definition III.4](#unity-dimensions)). The same composition and coordination machinery applies; the dynamics are just different (destabilizing rather than stabilizing).

**Inter-agent communication as a special observation channel.** When agent $A_i$ communicates with $A_j$, the message is an action by $A_i$ and an observation by $A_j$. No new formalism is needed — communication is a high-bandwidth, low-noise, directed observation channel. What makes it special is that the sender controls the content (unlike passive environmental observation), which introduces the possibility of strategic manipulation ([Hypothesis III.9](#communication-gain)).


<a id="composition-closure"></a>

### Formulation III.2: *Composition Closure Criterion*

We define a group of interacting agents as a valid composite macro-agent when its closed-loop dynamics approximately commute with coarse-graining — that is, when projecting micro-states to macro-states and then running macro-dynamics yields approximately the same result as running micro-dynamics and then projecting.

#### Formal Expression

Let a system consist of $N$ sub-agents interacting in a shared environment with state space $\mathcal S_{env}$. The micro-state, micro-observations, and micro-actions are:

$$X_{micro, t} = \{ (M_{i,t}, G_{i,t}) \}_{i=1}^N \in \mathcal X_{micro}$$

$$o_{micro, t} = \{ o_{i,t} \}_{i=1}^N \in \mathcal O_{micro}$$

$$a_{micro, t} = \{ a_{i,t} \}_{i=1}^N \in \mathcal A_{micro}$$

The coupled micro-dynamics form an action-observation loop:

$$X_{micro, t} \xrightarrow{\pi_{micro}} a_{micro, t} \xrightarrow{E} (\Omega_{t+1}, o_{micro, t+1}) \xrightarrow{f_{micro}} X_{micro, t+1}$$

We constrain our search to an admissible class of projections $\Lambda \in \mathcal P_{adm}$ mapping micro to macro, and an admissible class of macro-dynamics $(\pi_c, E_c, f_c) \in \mathcal M_{adm}$:
- $\Lambda_x : \mathcal X_{micro} \to \mathcal X_c = (M_c, G_c)$
- $\Lambda_o : \mathcal O_{micro} \to \mathcal O_c$
- $\Lambda_a : \mathcal A_{micro} \to \mathcal A_c$
- $\Lambda_\Omega : \mathcal S_{env} \to \mathcal S_{env, c}$

Let $\mathcal D_{micro}$ be the distribution of reachable trajectories generated entirely by the true micro-system over horizon $H$.

*[Definition (Composition Closure)]* We define the minimal achievable closure defect $\varepsilon^\ast$ over the admissible classes as:
$$ \varepsilon^* = \inf_{\Lambda \in \mathcal{P}_{adm}, (\pi_c, E_c, f_c) \in \mathcal{M}_{adm}} \big\Vert (\varepsilon_x, \varepsilon_a, \varepsilon_o) \big\Vert $$

Where the expected component errors evaluated over true micro-trajectories $\tau \sim \mathcal D_{micro}$ are:
- $\varepsilon_x = \mathbb E_{\tau} \Big[ \frac{1}{H} \sum_{t=1}^H \big\Vert \Lambda_x\big(f_{micro}(X_{micro, t}, o_{micro, t+1})\big) - f_c\big(\Lambda_x(X_{micro, t}), \Lambda_o(o_{micro, t+1})\big) \big\Vert_{\mathcal{X}} \Big]$
- $\varepsilon_a = \mathbb E_{\tau} \Big[ \frac{1}{H} \sum_{t=1}^H \big\Vert \Lambda_a\big(\pi_{micro}(X_{micro, t})\big) - \pi_c\big(\Lambda_x(X_{micro, t})\big) \big\Vert_{\mathcal{A}} \Big]$
- $\varepsilon_o = \mathbb E_{\tau} \Big[ \frac{1}{H} \sum_{t=1}^H \big\Vert \Lambda_o\big(E_{obs}(\Omega_t, a_{micro, t})\big) - E_{c, obs}\big(\Lambda_\Omega(\Omega_t), \Lambda_a(a_{micro, t})\big) \big\Vert_{\mathcal{O}} \Big]$

A set of agents forms a meaningful composite agent when $\varepsilon^\ast \leq \varepsilon_{max}$.

#### Epistemic Status

*Conditional.* Max attainable: conditional (formulation choice). The mathematical definition of $\varepsilon^\ast$ is well-formed — given specified norms and admissibility constraints, it's a well-defined infimum. The formulation is conditional on two under-specified components: (1) the admissibility constraints ($\mathcal P_{adm}$ and $\mathcal M_{adm}$) that prevent trivial closure by requiring the macro-agent to satisfy ACT's structural requirements, and (2) the norm choices for states, actions, and observations, which are load-bearing — different norms yield different $\varepsilon^\ast$ values. The criterion itself is a *formulation choice*: approximate dynamical homomorphism is one way to operationalize the scale invariance required by [Postulate I.6](#composition-consistency), but not the only possible one.

#### Discussion

This criterion replaces intuitive questions about "where the boundary of an agent is" with a functional test: does a macroscopic ACT description preserve the underlying micro-dynamics well enough to remain predictive and capable? The core requirement is an **approximate dynamical homomorphism** — the macro-dynamics approximately commute with the projection.

Without admissibility constraints on $\mathcal P_{adm}$ and $\mathcal M_{adm}$, closure would be trivial (e.g., arbitrarily curve-fitting an open-loop model). By forcing the macro-components to retain the structure of an ACT agent, the minimal closure defect $\varepsilon^\ast$ quantifies the irreducible cost of being multiple. High qualitative unity (shared models, shared objectives) strongly predicts a low $\varepsilon^\ast$.

**Relationship to [Postulate I.6](#composition-consistency).** The Section I postulate requires that ACT's machinery be scale-invariant — predictions at different levels of description must be compatible. This segment operationalizes "compatible" as "bounded closure defect under admissible coarse-graining." Other operationalizations are possible (e.g., behavioral equivalence, information-theoretic measures), making this a formulation choice rather than a derived consequence.

#### Working Notes
- The admissibility constraints are the hard part and currently serve as placeholders. What exactly must the macro-agent satisfy? Recursive update? Directed separation? The full scope condition? Specifying $\mathcal M_{adm}$ is where the real content will live.
- The norm choices ($\Vert\cdot\Vert_{\mathcal{X}}$, $\Vert\cdot\Vert_{\mathcal{A}}$, $\Vert\cdot\Vert_{\mathcal{O}}$, and the combination norm on the tuple) are load-bearing but unspecified. Domain-specific instantiation will require choosing these.
- Bridge lemma needed: small expected component-wise errors guarantee bounded trajectory divergence only if the admissible macro-dynamics $\mathcal M_{adm}$ satisfy appropriate Lipschitz stability conditions. Without this, bounded $\varepsilon^\ast$ doesn't formally guarantee bounded trajectory error.
- The approach is an approximate dynamical homomorphism condition, a standard tool in dynamical systems and model reduction (cf. Mori-Zwanzig projection, balanced truncation). The specific contribution is applying it to ACT's closed-loop agent structure.


<a id="tempo-composition"></a>

### Derived III.3: *Composite Tempo Inequality*

The adaptive tempo of a composite agent is bounded from above by the sum of its sub-agents' tempos. The gap between aggregate potential and realized composite tempo is the coordination overhead — tempo consumed by internal reconciliation rather than external mismatch correction.

#### Formal Expression

Let $\mathcal T_i$ be the adaptive tempo of sub-agent $i$ within a composite group of $N$ agents. Let $\mathcal T_c$ be the adaptive tempo of the composite macro-agent $A_c$ defined by an admissible coarse-graining $\Lambda$.

*[Derived (Sub-additive Tempo, sketch)]* For any composite agent $A_c$ with minimal closure defect $\varepsilon^\ast \geq 0$, the composite tempo is bounded by the sum of individual tempos:
$$ \mathcal{T}_c \leq \sum_{i=1}^N \mathcal{T}_i $$

*[Definition (Coordination Overhead)]* We define the **coordination overhead penalty** $C_{\text{coord}}$ as the difference between aggregate potential and realized macro-tempo:
$$ C_{\text{coord}} := \Big( \sum_{i=1}^N \mathcal{T}_i \Big) - \mathcal{T}_c $$

#### Epistemic Status

*Sketch.* Max attainable: exact (with a complete proof). The inequality is structurally motivated: composition cannot create corrective capacity out of nothing, and internal reconciliation consumes tempo that doesn't contribute to external mismatch correction. A proof sketch exists (below) but the formal step from $\varepsilon^\ast$ to $C_{\text{coord}}$ — showing that the closure defect functionally determines the coordination penalty — remains open. The inequality $\mathcal T_c \leq \sum \mathcal T_i$ is almost certainly correct; the quantitative relationship $C_{\text{coord}}(\varepsilon^\ast)$ is the genuine open problem.

##### Derivation sketch

1. Tempo is a rate of mismatch correction ($\nu \cdot \eta^\ast_{\text{eff}}$).
2. In the ideal case ($\varepsilon^\ast = 0$), every "tick" of an individual's ACT loop contributes directly to the macro ACT loop without friction. Thus $\mathcal T_c = \sum \mathcal T_i$ and $C_{\text{coord}} = 0$.
3. When $\varepsilon^\ast \gt 0$, closure fails partially. Sub-agents spend a fraction of their individual tempo correcting *internal* mismatches generated by other sub-agents (e.g., Alice changes an API, Bob must update his $M_t$ to understand it), or take actions that counteract each other.
4. The macro-agent $A_c$ does not gain adaptive advantage against the *external* environment from these internal reconciliation cycles. These cycles are consumed by $C_{\text{coord}}$.

The gap: step 3→4 requires formalizing the distinction between internal and external mismatch correction within the tempo definition, and showing that internal correction is bounded below by a function of $\varepsilon^\ast$.

#### Discussion

**Equality conditions.** Strict equality ($\mathcal T_c = \sum \mathcal T_i$, i.e. $C_{\text{coord}} = 0$) requires:
1. **Orthogonal Routing:** The information dependency DAG exactly matches organizational boundaries (no costly cross-talk required).
2. **Perfect Shared Intent:** No tempo is lost to internal negotiation or conflicting pursuit of the macro-objective.
3. **No Net Macro-Information Loss:** Observations may be redundant, but they do not result in wasted tempo after fusion, nor is critical macro-information lost during coordination.

These are stated as sufficient conditions; whether they are also necessary is open.

**Brooks's Law.** Adding more agents (increasing $\sum \mathcal T_i$) only increases the composite tempo $\mathcal T_c$ if the corresponding increase in closure defect $\varepsilon^\ast$ doesn't let $C_{\text{coord}}$ dominate. The model provides a formal analog of Brooks's Law: if communication overhead ($C_{\text{coord}}$) grows faster than aggregate capability ($\sum \mathcal T_i$) when adding agents, then adding people to a late project makes it later. Whether this specific mechanism (coordination overhead consuming tempo) is the dominant cause in practice is an empirical question.

**Connection to [Derived III.7](#team-persistence).** The persistence condition for the composite agent requires $\mathcal T_c \gt \rho_{\text{ext}} / \Vert\delta_{\text{critical}}\Vert$. Since $\mathcal T_c = \sum \mathcal T_i - C_{\text{coord}}$, high coordination overhead can push the composite below the persistence threshold, causing it to disintegrate as a coherent entity — even though each sub-agent individually persists.

#### Working Notes
- The functional form of $C_{\text{coord}}(\varepsilon^\ast)$ is the key open problem. Is it linear? Superlinear? Does it depend on N? The spike suggests monotonicity but no specific form.
- A natural first step: prove the inequality for the 2-agent case with orthogonal observation channels and a single shared environment dimension. If the inequality holds in this toy case, the general argument via induction on N is likely tractable.
- The internal/external mismatch distinction needs formalization. One approach: decompose each sub-agent's mismatch signal into components attributable to environment change vs. other sub-agents' actions. Internal reconciliation is correction of the latter.


> **\[GAP\]** Does epistemic goal-blindness survive composition?


<a id="unity-dimensions"></a>

### Definition III.4: *Unity Dimensions*

The quality of a composite agent's composition can be decomposed along four substantially independent dimensions: epistemic (shared model), teleological (shared objective), strategic (coordinated action), and perceptual (shared observations). These dimensions predict the closure defect $\varepsilon^\ast$ ([Formulation III.2](#composition-closure)) — high unity along all four predicts low $\varepsilon^\ast$.

#### Formal Expression

*[Definition (unity-dimensions)]*

For a composite agent $A_c$ composed of sub-agents $\{A_1, \ldots, A_n\}$:

**Epistemic unity** $U_M$ — how much of the reality model is shared:

$$U_M = \frac{I(M_t^{(1)}; \ldots; M_t^{(n)})}{H(M_t^{(1)}, \ldots, M_t^{(n)})}$$

The fraction of total model information that is shared (multi-information / total-correlation ratio). $U_M = 1$ for identical models; $U_M = 0$ for independent models.

**Teleological unity** $U_O$ — how aligned are the objectives:

$$U_O^{(i,j)} = \text{corr}\!\left(V_{O_t^{(i)}}(\tau),\; V_{O_t^{(j)}}(\tau)\right)$$

over trajectories the composite encounters. $+1$ for identical objectives; $-1$ for perfectly opposed; $0$ for orthogonal. The composite teleological unity is an aggregation over all pairs. The scalar ranges from fully cooperative to fully adversarial per objective dimension.

**Strategic unity** $U_\Sigma$ — how coordinated is the joint policy:

*[Discussion]*

$$U_\Sigma = 1 - \frac{D_{\text{KL}}(\pi^c_{\text{actual}} \Vert \pi^c_{\text{optimal}})}{D_{\text{KL}}(\pi^c_{\text{independent}} \Vert \pi^c_{\text{optimal}})}$$

where $\pi^c_{\text{optimal}}$ is the jointly optimal policy. $U_\Sigma = 1$ when actual matches optimal; $U_\Sigma = 0$ when actual matches independent (no coordination). Requires knowing the jointly optimal policy, which is itself a strong assumption.

**Perceptual unity** $U_{\text{obs}}$ — how much of the observation stream is shared:

The fraction of total observation information that reaches all sub-agents. Full perceptual unity means all agents observe the same signals; zero means private observations only. Enables epistemic convergence without explicit model-sharing.

#### Epistemic Status

*Discussion-grade.* Max attainable: empirical. The four dimensions are qualitatively motivated: they correspond to the four components of agent state ($M_t$, $O_t$, $\Sigma_t$, and the observation channel). The specific metrics proposed above are sketches — the information-theoretic formulations ($U_M$, $U_\Sigma$) are well-defined in principle but would require specifying distributions and distance measures for any practical computation. The claim that these dimensions are substantially independent is a hypothesis, not derived — epistemic unity may enable strategic unity (shared models allow coordination without explicit planning), so independence is approximate at best.

#### Discussion

**Clausewitz's three gaps.** These dimensions map to the gaps identified by Clausewitz (systematized by Bungay in *The Art of Action*):

| Clausewitz Gap | Unity Dimension | Formal Quantity |
|---|---|---|
| Knowledge gap | Epistemic unity ($U_M$) | $1 - U_M$: fraction of model not shared |
| Alignment gap | Teleological unity ($U_O$) | $1 - U_O$: objective misalignment |
| Effects gap | Strategic + Perceptual unity | $1 - U_\Sigma$ + observation routing costs |

The mapping is not perfect — Clausewitz's "effects gap" blends action coordination with observation feedback — but it provides 200+ years of organizational evidence for the qualitative decomposition.

**Connection to closure defect.** The unity dimensions serve as predictors of the component closure errors in [Formulation III.2](#composition-closure): high $U_M$ predicts low $\varepsilon_x$ (state update error), high $U_O$ predicts low $\varepsilon_a$ (action error, since aligned goals produce compatible actions), high $U_{\text{obs}}$ predicts low $\varepsilon_o$ (observation error). The mapping from unity to closure error is not yet formalized.

**What each dimension's absence costs.**

- Low $U_M$: prediction conflicts → uncoordinated actions based on contradictory beliefs. Internal mismatch component from model disagreement.
- Low $U_O$: strategic friction → sub-agents pursue conflicting sub-goals. Effort wasted or counterproductive.
- Low $U_\Sigma$: redundancy and gaps → two agents fix the same bug while a critical one goes unnoticed.
- Low $U_{\text{obs}}$: information silos → critical signals observed by one agent but not actionable by the composite.

#### Working Notes
- The independence of unity dimensions needs careful examination. High epistemic unity likely enables (but does not guarantee) high strategic unity — if agents share models, they can coordinate implicitly. The dimensions may be better described as "substantially independent inputs to a joint prediction of $\varepsilon^\ast$" rather than "independent properties."
- The specific metric formulations need testing on concrete cases (software team, military unit) to determine if they discriminate meaningfully between well-composed and poorly-composed groups.
- The teleological unity scalar per objective dimension ($+1$ to $-1$) captures mixed cooperative-competitive situations: a company can be cooperative on product quality and competitive on internal resource allocation simultaneously.


<a id="shared-intent"></a>

### Definition III.5: *Shared Intent*

When sub-agents within a composite must coordinate, they face a communication problem: transmitting the full objective $O_t$ and strategy $\Sigma_t$ is expensive (high bandwidth, high latency), but acting without any shared purpose wastes coordination potential. The Information Bottleneck ([Formulation I.11](#information-bottleneck)) applied to inter-agent communication predicts an optimal compression: transmit enough of $G_t$ to align behavior, not more.

#### Formal Expression

*[Definition (shared-intent)]*

Let $G_t^{\text{full}}$ be the source agent's complete purposeful state $(O_t, \Sigma_t)$. Let $G_t^{\text{shared}}$ be the compressed representation communicated to partners. The shared intent is the IB-optimal compression:

$$G_t^{\text{shared}} = \arg\min_{G_s} \left[ I(G_t^{\text{full}}; G_s) - \beta \cdot I(G_s; a_t^{\text{coordinated}}) \right]$$

where $a_t^{\text{coordinated}}$ is the jointly optimal action and $\beta$ controls the complexity-relevance tradeoff. At high $\beta$, the agent communicates more detail (approaching full model sharing). At low $\beta$, communication is minimal (approaching independent action).

The shared intent is the *minimal sufficient statistic* of the sender's purposeful state for predicting the jointly optimal coordination behavior.

#### Epistemic Status

*Discussion-grade.* Max attainable: conditional (conditional on the IB framework being appropriate for inter-agent communication). The application of IB to inter-agent communication is structurally motivated — IB compresses optimally given a relevance criterion, and coordination relevance is the natural criterion — but the specific formulation assumes: (1) the sender knows the jointly optimal action (which requires knowing other agents' states), (2) the compression is lossless in the IB sense (real communication introduces noise, delay, and misinterpretation), (3) the $\beta$ parameter is fixed rather than dynamically adjusted. These are strong assumptions. The qualitative prediction (communicate purpose before plans before models) is more robust than the specific IB formulation.

#### Discussion

**What gets compressed out.** The IB compression preferentially preserves:
1. Terminal objectives (what the agent is trying to achieve) — these are compact and change slowly
2. High-level strategy (which approach, not which specific steps) — moderate size, moderate change rate
3. Strategic details (specific edge credences in $\Sigma_t$) — large, change fast, low coordination value

**Connection to cognitive cost of $\Sigma_t$.** For agents with bounded communication capacity (bandwidth-limited channels, finite context windows), the DAG must be summarized for transmission. A 500-node strategy DAG cannot be shared in full; the IB compression identifies which structural features of the DAG matter for coordination.

**Organizational communication patterns.** Commander's intent in military doctrine is an empirical instantiation: the commander communicates *what* to achieve and *why*, not *how*. This is IB-optimal if objectives change slowly (low $\nu_O$) and strategies change fast (high $\nu_\Sigma$) — communicating objectives gives a long shelf life per bit transmitted.

#### Working Notes
- The IB formulation assumes a single relevance variable ($a_t^{\text{coordinated}}$). In practice, coordination relevance is multi-dimensional: shared intent needs to support action coordination, conflict resolution, resource allocation, and adaptive replanning. A richer relevance variable might be needed.
- How does shared intent interact with 100% context turnover? An AI agent starting a new session needs to reconstruct $G_t^{\text{shared}}$ from persistent storage. The compression from full $G_t$ to shared intent is also useful for $M_t$ preservation ([Discussion V.3](#m-preservation)) — store the compressed version, not the full state.


<a id="auftragstaktik-principle"></a>

### Hypothesis III.6: *Auftragstaktik Principle*

For a composite agent with limited communication bandwidth, the optimal allocation prioritizes sharing objectives over strategies over models. This captures the structural insight of Auftragstaktik (mission-type tactics): investing communication bandwidth in shared purpose (teleological unity) while accepting lower epistemic and strategic unity, granting sub-agents autonomy to adapt locally. The model predicts the same priority ordering that military doctrine discovered empirically; whether the mechanism (IB-optimal bandwidth allocation) is the actual reason Auftragstaktik works is an open question.

#### Formal Expression

*[Hypothesis (auftragstaktik-principle)]*

Let a composite agent's total inter-agent communication bandwidth be $B = B_O + B_\Sigma + B_M$, allocated across objective sharing ($B_O$), strategy coordination ($B_\Sigma$), and model synchronization ($B_M$).

The hypothesis: the allocation that maximizes composite tempo $\mathcal{T}_c$ (or equivalently, minimizes coordination overhead $C_{\text{coord}}$) prioritizes:

$$B_O \gt B_\Sigma \gt B_M$$

when:
- Objectives change slowly relative to strategies: $\nu_O \ll \nu_\Sigma$
- Strategies change slowly relative to models: $\nu_\Sigma \ll \nu_M$
- Sub-agents have sufficient local adaptive capacity: each $\mathcal{T}_i \gt \rho_i^{\text{local}} / \Vert\delta_{\text{critical}}^i\Vert$

The priority ordering follows from the IB framework ([Definition III.5](#shared-intent)): the bits with the longest shelf life and highest coordination value per bit should be transmitted first. Objectives change slowly and enable autonomous coordination (sub-agents who share objectives can independently choose compatible strategies). Models change fast and provide diminishing coordination value (two agents with the same model but different objectives still conflict).

#### Epistemic Status

*Discussion-grade.* Max attainable: empirical. The priority ordering is a qualitative prediction grounded in the IB framework and supported by extensive military-organizational evidence (Bungay's analysis of Clausewitz, Wehrmacht doctrine, modern mission command). But it is not derived — the IB optimization would need to be solved explicitly with realistic cost functions to confirm the ordering, and the conditions under which the ordering reverses (e.g., when model synchronization is critical because the situation is genuinely ambiguous) are not characterized. The empirical evidence is strong but comes primarily from one domain (military command); generalization to software teams, AI agent swarms, and other settings is plausible but unverified.

#### Discussion

**When the ordering reverses.** The prioritization $B_O \gt B_\Sigma \gt B_M$ assumes sub-agents can independently construct adequate local models. When the environment is genuinely ambiguous and local observations are insufficient (fog of war, novel codebase, unprecedented market conditions), model synchronization may be worth more than objective sharing — sub-agents who share the same wrong model at least err consistently, which is sometimes better than each having a different wrong model.

**Bungay's evidence.** In *The Art of Action*, Bungay documents that organizations consistently fail by inverting this priority: they over-invest in controlling *how* subordinates act (strategy sharing, $B_\Sigma$) rather than ensuring subordinates understand *why* (objective sharing, $B_O$). The result: subordinates who follow instructions precisely but cannot adapt when conditions change, because they lack the teleological context to improvise intelligently.

**The software team instantiation.** A well-functioning development team has:
- High $B_O$: clear product goals, understood by all (sprint goals, feature objectives)
- Moderate $B_\Sigma$: architectural decisions shared, implementation details autonomous
- Low $B_M$: each developer builds their own mental model of the code they touch; full codebase understanding is neither expected nor efficient

When this inverts (micromanagement of implementation details, unclear product goals), team tempo drops — consistent with the Auftragstaktik prediction.

**Connection to Conway's Law.** Conway's Law (system structure mirrors communication structure) is a consequence: when $B_\Sigma$ is low and $B_O$ is high, sub-agents coordinate through shared objectives rather than explicit action coordination, producing systems whose boundaries reflect objective decomposition rather than communication channels.

#### Working Notes
- The formal IB derivation of the priority ordering would need: (1) a model of how each unity dimension contributes to composite tempo, (2) the rate of change of each shared quantity ($\nu_O$, $\nu_\Sigma$, $\nu_M$), (3) the communication cost per bit for each type. The qualitative argument is that objectives are compact and slow-changing (high bits-per-cost, long shelf life), while models are large and fast-changing (low bits-per-cost, short shelf life). Formalizing this is tractable but has not been done.
- The principle may need qualification for AI agent teams where model synchronization is cheap (shared vector databases, persistent memory) but objective alignment is hard (prompt engineering, RLHF). The cost structure differs from human organizations.


<a id="team-persistence"></a>

### Derived III.7: *Team Persistence*

Teams persist where individuals cannot because cooperative communication adds to each agent's effective tempo while reducing effective disturbance.

#### Formal Expression

##### Distributed Tempo

*[Definition (distributed-tempo)]*

Agent $i$'s effective tempo includes contributions from both direct observation and communication from allies:

$$\mathcal{T}_i = \underbrace{\sum_k \nu_i^{(k)} \eta_i^{(k)*}}_{\text{direct observation tempo}} + \underbrace{\sum_{j \in \mathcal{N}(i)} \nu_{ji}^{\text{comm}} \, \eta_{ji}^*}_{\text{communication tempo}}$$

where $\nu_{ji}^{\text{comm}}$ is the rate of communication events from agent $j$ to agent $i$, and $\eta_{ji}^\ast$ is the communication gain ([Hypothesis III.9](#communication-gain)). Faster team adaptation comes not only from faster individual sensing but from faster, more reliable knowledge transfer.

##### Cooperative-Adversarial Disturbance Decomposition

*[Formulation (disturbance-decomposition)]*

The disturbance rate experienced by agent $i$ decomposes into environment, adversarial, and cooperative components:

$$\rho_i = \rho_{i,\text{env}} + \sum_{j \in \mathcal{A}_i} \gamma_{j \to i}^{\text{adv}} \, \mathcal{T}_j - \sum_{j \in \mathcal{C}_i} \gamma_{j \to i}^{\text{coop}} \, \mathcal{T}_j$$

where $\mathcal A_i$ is the set of agents adversarially coupled to $i$, $\mathcal C_i$ is the set cooperatively coupled, and the $\gamma$ coefficients capture coupling effectiveness (as in [Derived III.10](#adversarial-destabilization)).

**The cooperative term is negative.** Allies reduce agent $i$'s effective disturbance by sharing information that preemptively corrects mismatch — each cooperative communication event that arrives before the corresponding environment disturbance would have been observed effectively cancels a unit of disturbance. This is the structural pattern consistent with why teams can persist in environments where individuals cannot: cooperative communication tempo offsets environment disturbance that would exceed any single agent's capacity.

**Effective disturbance rate.** The decomposition can yield $\rho_i \lt 0$ when cooperative coupling dominates both environment disturbance and adversarial coupling. The sector-condition analysis ([Result I.25](#sector-condition-stability)) assumes non-negative disturbance (GA-2). Define:

*[Definition (effective-disturbance)]*

$$\rho_i^{\text{eff}} = \max(\rho_i, \, 0)$$

When $\rho_i^{\text{eff}} = 0$, the agent's cooperative network fully absorbs all disturbance — the persistence condition is trivially satisfied and mismatch decays to zero. This is an idealized limit; in practice, $\rho_i^{\text{eff}} \gt 0$ because cooperative coupling is imperfect and environment disturbance is never fully preempted. All downstream uses of $\rho_i$ in the persistence and reserve conditions should be read as $\rho_i^{\text{eff}}$.

##### Team Persistence Condition

*[Derived (team-persistence, from sector-condition-stability, persistence-condition)]*

Applying the sector-condition framework ([Result I.25](#sector-condition-stability)) with $\rho_i^{\text{eff}}$, agent $i$ persists iff:

$$\frac{\rho_i^{\text{eff}}}{\alpha_i} \lt R_i$$

Substituting the decomposition (the $\max(\cdot, 0)$ in $\rho_i^{\text{eff}}$ is omitted to expose the three levers; the condition is trivially satisfied when the numerator is non-positive):

$$\frac{\rho_{i,\text{env}} + \sum_j \gamma_{j \to i}^{\text{adv}} \mathcal{T}_j - \sum_j \gamma_{j \to i}^{\text{coop}} \mathcal{T}_j}{\alpha_i} \lt R_i$$

This reveals three distinct levers for team persistence:

1. **Increase $\alpha_i$** (individual correction efficiency) — better models, better gain calibration
2. **Increase cooperative tempo** ($\gamma^{\text{coop}} \mathcal T_j$) — more reliable allies, faster communication channels
3. **Reduce adversarial coupling** ($\gamma^{\text{adv}} \mathcal T_j$) — better deception detection, reduced exposure to adversarial actions

##### Coordination Overhead Threshold

*[Discussion — Coordination Threshold]*

Communication channels have costs: time to compose and parse messages, bandwidth limitations, synchronization requirements. These costs reduce the agent's effective tempo by diverting capacity from direct adaptation. Let $\Delta \mathcal T_i^{\text{cost}}(j)$ represent the tempo-equivalent coordination cost of maintaining the channel with $j$ — the reduction in $i$'s direct observation tempo caused by the overhead, in units of $[t^{-1}]$.

The net benefit of adding agent $j$ to $i$'s communication network is positive only when:

$$\nu_{ji}^{\text{comm}} \, \eta_{ji}^* \gt \Delta \mathcal{T}_i^{\text{cost}}(j)$$

Both sides have units $[t^{-1}]$: the LHS is communication tempo gained, the RHS is direct-adaptation tempo lost to coordination overhead. This implies a natural team-size limit: adding members increases communication tempo with diminishing returns (as $U_{\text{src}}$ and $U_o$ accumulate across diverse sources) while coordination costs grow, potentially superlinearly. The optimal team size occurs where the marginal communication tempo equals the marginal coordination cost.

#### Epistemic Status

Conditional on the communication-gain hypothesis ([Hypothesis III.9](#communication-gain)). The distributed tempo definition is a *formulation* — a representational choice extending [Definition I.21](#adaptive-tempo) to the multi-agent case. The disturbance decomposition is a *formulation* — the additive structure and the sign convention are modeling choices, not derivations. The persistence condition is *derived* from the sector-condition framework ([Result I.25](#sector-condition-stability)) given the decomposition: the derivation is exact under the same assumptions (GA-2, GA-3 applied to $\rho_i^{\text{eff}}$). The coordination overhead threshold is *discussion-grade* — qualitatively clear but the claim about diminishing returns and superlinear costs is asserted, not derived.

Max attainable: *robust-qualitative* for the persistence condition (it inherits the sector-condition's robustness but the decomposition is a modeling choice). The coordination threshold could reach *conditional* with a concrete cost model.

#### Discussion

**Compositional analog of [Result I.24](#persistence-condition).** The single-agent persistence condition says an agent persists when $\mathcal{T} \gt \rho / \Vert\delta_{\text{critical}}\Vert$. This segment extends that condition to agents embedded in a cooperative-adversarial network. The formal structure is identical — the sector-condition machinery applies unchanged — but the *inputs* ($\mathcal T_i$ and $\rho_i$) now include inter-agent terms. This is consistent with [Postulate I.6](#composition-consistency): the same dynamical laws apply at every level of description; what changes between levels is which channels contribute to tempo and which sources contribute to disturbance.

**Why teams can persist where individuals cannot.** The cooperative term $\sum_j \gamma_{j \to i}^{\text{coop}} \mathcal T_j$ is subtracted from the disturbance rate. An individual agent facing $\rho_{i,\text{env}} \gt \alpha_i R_i$ fails the persistence condition. Adding cooperative allies with sufficient communication tempo can reduce $\rho_i^{\text{eff}}$ below the persistence threshold without any change to the individual's own capabilities. The mechanism is information-theoretic: allies provide observations the agent could not make on its own timescale.

**Timescale separation and [Postulate I.6](#composition-consistency).** The distributed tempo definition presumes that communication events and direct observation events are comparable — they enter additively into $\mathcal T_i$. This requires that the communication timescale is not so slow relative to the environment dynamics that communicated information is stale on arrival. When communication latency approaches $1/\rho_{i,\text{env}}$, the effective $\eta_{ji}^\ast$ degrades (the observation uncertainty $U_{o,ji}$ increases with staleness), naturally suppressing the communication tempo contribution.

**Complement to [Derived III.10](#adversarial-destabilization).** That segment characterizes when an adversary can push an agent past its stability boundary. This segment characterizes the cooperative counterpart: when allies can pull an agent back from instability. The $\gamma$ coefficients have the same structure — coupling effectiveness — but opposite sign in the disturbance decomposition.

#### Working Notes

- The topology-dependent analysis (F.4 in the source material — peer networks, ensemble architectures, hierarchical structures) and game-theoretic integration (F.5) are related but separate concerns, not covered here. They may warrant their own segments.
- The coordination cost model $\Delta \mathcal T_i^{\text{cost}}(j)$ needs further specification to be useful. In software systems, coordination cost is empirically measurable (meeting time, code review latency, merge conflict rates). In military contexts, it maps to C2 overhead. The question is whether there is a useful *general* cost model or whether it is always domain-specific.
- The disturbance decomposition treats cooperative and adversarial coupling as additive and independent. In practice, the same agent $j$ might be cooperatively coupled on some dimensions and adversarially coupled on others (e.g., a competitor who shares some information). The per-dimension persistence condition ([Result I.24](#persistence-condition)'s per-dimension extension) may be relevant here.

*(Descended from TFT Appendix F, Section F.3.)*


<a id="adversarial-tempo-advantage"></a>

### Result III.8: *Adversarial Tempo Advantage*

Under adversarial coupling where one agent's actions contribute to the other's disturbance rate, the steady-state mismatch ratio scales superlinearly with the tempo ratio.

#### Formal Expression

*[Derived (adversarial-tempo-advantage, from mismatch-dynamics steady state and adversarial-destabilization coupling model)]*

**Setup.** Two agents $A$ and $B$ with adaptive tempos $\mathcal T_A$ and $\mathcal T_B$, coupled via the same model as [Derived III.10](#adversarial-destabilization):

$$\rho_A = \rho_{\text{base}} + \gamma_B \cdot \mathcal{T}_B, \qquad \rho_B = \rho_{\text{base}} + \gamma_A \cdot \mathcal{T}_A$$

where $\gamma_A, \gamma_B \gt 0$ are the coupling effectivenesses and $\rho_{\text{base}}$ is the background disturbance rate (taken equal for both agents for clarity; the asymmetric case is a straightforward generalization).

**Steady-state mismatch ratio.** From the linear mismatch dynamics ([Hypothesis I.22](#mismatch-dynamics)), $\Vert\delta\Vert_{ss} = \rho / \mathcal{T}$. Substituting the coupled disturbance rates:

$$\Vert\delta_A\Vert_{ss} = \frac{\rho_{\text{base}} + \gamma_B \cdot \mathcal{T}_B}{\mathcal{T}_A}, \qquad \Vert\delta_B\Vert_{ss} = \frac{\rho_{\text{base}} + \gamma_A \cdot \mathcal{T}_A}{\mathcal{T}_B}$$

Taking the ratio:

$$\frac{\Vert\delta_B\Vert_{ss}}{\Vert\delta_A\Vert_{ss}} = \frac{\rho_{\text{base}} + \gamma_A \cdot \mathcal{T}_A}{\mathcal{T}_B} \cdot \frac{\mathcal{T}_A}{\rho_{\text{base}} + \gamma_B \cdot \mathcal{T}_B}$$

*[Result (adversarial-tempo-advantage)]*

$$\frac{\Vert\delta_B\Vert_{ss}}{\Vert\delta_A\Vert_{ss}} = \frac{(\rho_{\text{base}} + \gamma_A \cdot \mathcal{T}_A) \cdot \mathcal{T}_A}{(\rho_{\text{base}} + \gamma_B \cdot \mathcal{T}_B) \cdot \mathcal{T}_B}$$

##### Coupling-Dominant Limit

In the coupling-dominant regime ($\gamma_A \cdot \mathcal T_A \gg \rho_{\text{base}}$ and $\gamma_B \cdot \mathcal T_B \gg \rho_{\text{base}}$), the base disturbance becomes negligible:

$$\frac{\Vert\delta_B\Vert_{ss}}{\Vert\delta_A\Vert_{ss}} \to \frac{\gamma_A \cdot \mathcal{T}_A^2}{\gamma_B \cdot \mathcal{T}_B^2} = \frac{\gamma_A}{\gamma_B} \cdot \left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^2$$

For symmetric coupling ($\gamma_A = \gamma_B$):

$$\frac{\Vert\delta_B\Vert_{ss}}{\Vert\delta_A\Vert_{ss}} \to \left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^2$$

The exponent is $b = 2$: a **squared** tempo advantage. A 2:1 tempo ratio yields a 4:1 mismatch ratio, not 2:1.

##### Derivation

From [Hypothesis I.22](#mismatch-dynamics), the steady-state condition $d\Vert\delta\Vert/dt = 0$ gives $\Vert\delta\Vert_{ss} = \rho / \mathcal{T}$.

1. Substitute the coupling model into $B$'s steady state: $\Vert\delta_B\Vert_{ss} = (\rho_{\text{base}} + \gamma_A \cdot \mathcal T_A) / \mathcal T_B$.

2. Substitute the coupling model into $A$'s steady state: $\Vert\delta_A\Vert_{ss} = (\rho_{\text{base}} + \gamma_B \cdot \mathcal T_B) / \mathcal T_A$.

3. Form the ratio:

$$\frac{\Vert\delta_B\Vert_{ss}}{\Vert\delta_A\Vert_{ss}} = \frac{(\rho_{\text{base}} + \gamma_A \cdot \mathcal{T}_A) / \mathcal{T}_B}{(\rho_{\text{base}} + \gamma_B \cdot \mathcal{T}_B) / \mathcal{T}_A} = \frac{(\rho_{\text{base}} + \gamma_A \cdot \mathcal{T}_A) \cdot \mathcal{T}_A}{(\rho_{\text{base}} + \gamma_B \cdot \mathcal{T}_B) \cdot \mathcal{T}_B}$$

4. In the coupling-dominant limit, $\rho_{\text{base}} \to 0$ relative to $\gamma \cdot \mathcal{T}$:

$$\frac{\Vert\delta_B\Vert_{ss}}{\Vert\delta_A\Vert_{ss}} \to \frac{\gamma_A \cdot \mathcal{T}_A \cdot \mathcal{T}_A}{\gamma_B \cdot \mathcal{T}_B \cdot \mathcal{T}_B} = \frac{\gamma_A}{\gamma_B} \cdot \left(\frac{\mathcal{T}_A}{\mathcal{T}_B}\right)^2$$

$\square$

##### Regime-Dependent Exponents

The squared law ($b = 2$) holds under deterministic drift coupling and coupling-dominant conditions. The exponent varies by regime:

| Regime | Coupling type | Dominance | Exponent $b$ |
|:---|:---|:---|:---:|
| 1 | Deterministic drift | Coupling-dominant | $2$ |
| 2 | Stochastic noise | Coupling-dominant | $3/2$ |
| 3 | Either | Non-coupling-dominant | $\to 1$ (det.) or $\to 1/2$ (stoch.) |

**Regime 2 (stochastic).** When the adversarial coupling enters as zero-mean noise rather than persistent drift, the steady-state RMS mismatch scales as $\rho / \sqrt{\mathcal{T}}$ (because the stationary variance of the AR(1) process scales as $\rho^2 / \mathcal{T}$, and absolute deviation scales as the square root of variance). Substituting into the ratio yields $b = 3/2$ in the coupling-dominant limit.

**Regime 3 (non-coupling-dominant).** When $\rho_{\text{base}} \gtrsim \gamma \cdot \mathcal{T}$, the base disturbance dominates and the coupling terms become a perturbation. The mismatch ratio degrades toward $\mathcal T_A / \mathcal T_B$ (linear, $b = 1$) for deterministic dynamics, or toward $(\mathcal T_A / \mathcal T_B)^{1/2}$ for stochastic.

The simulation validation across all three regimes is in [Observation III.11](#adversarial-exponent-regimes).

#### Epistemic Status

The squared law ($b = 2$) is *exact* under the linear mismatch dynamics ([Hypothesis I.22](#mismatch-dynamics)) and the deterministic coupling-dominant conditions. The derivation is straightforward algebra from the steady-state formula and the coupling model. The coupling model itself is an *assumption* — the same one used in [Derived III.10](#adversarial-destabilization).

The regime-dependent exponents ($b = 3/2$ stochastic, $b \to 1$ non-coupling-dominant) are *empirical* — confirmed by simulation ([Observation III.11](#adversarial-exponent-regimes), with the deterministic case matching at $b = 1.999$) and consistent with the analytical scaling arguments, but the stochastic case is not yet derived from the stochastic mismatch dynamics in full generality. The transition between regimes is smooth, not sharp.

Max attainable: exact conditional on the mismatch dynamics and coupling model. The result is as strong as its assumptions; no additional work changes the epistemic status without changing the dynamical model.

#### Discussion

**Superlinearity is the key result.** The naive expectation — twice as fast yields twice the advantage — is wrong under adversarial coupling. The mechanism is that the faster agent both (a) corrects its own mismatch faster and (b) generates disturbance for the opponent faster. These two effects multiply, producing the squared exponent. Speed advantage is not additive; it compounds.

**Relationship to [Derived III.10](#adversarial-destabilization).** The steady-state mismatch ratio quantifies how much worse the slower agent does *while both agents persist*. The destabilization threshold ([Derived III.10](#adversarial-destabilization)) marks where the slower agent fails entirely — its correction mechanism breaks down. Below the threshold, this segment's mismatch ratio applies. Above it, [Derived III.10](#adversarial-destabilization)'s Lyapunov divergence takes over. The two results are complementary: this one gives the score; that one gives the game-ending condition.

**Regime dependence is operationally significant.** Whether an adversary's tempo increase produces systematic drift (positional maneuvering, API changes, doctrinal initiative) or unpredictable noise (feints, randomized attacks, market volatility) determines the scaling law. The distinction is not academic — $b = 2$ vs. $b = 3/2$ means a 3:1 tempo ratio yields 9:1 vs. 5.2:1 mismatch ratio. The model predicts that consistent, directional pressure is more effective per unit of tempo than unpredictable disruption.

**Formal analog of OODA-loop observations.** The squared scaling is consistent with Boyd's observation that getting inside the opponent's decision cycle has disproportionate effects. The theory identifies a specific mechanism (multiplicative interaction of correction speed and disturbance generation) and a specific condition (coupling-dominant regime) under which this disproportionality holds. Whether this mechanism is the dominant one in actual adversarial interactions is an empirical question, not a mathematical one.

#### Working Notes

- The analysis treats each agent's tempo as exogenous — $\mathcal T_A$ does not change in response to $B$'s actions and vice versa. A fully coupled analysis where both agents' mismatch states co-evolve simultaneously (joint Lyapunov function over $(\delta_A, \delta_B)$) is the open extension. The decoupled result is a worst-case bound for the slower agent: in practice, the faster agent may divert adaptive capacity to generating disturbance rather than correcting its own mismatch, creating a self-limiting effect.
- The stochastic exponent ($b = 3/2$) is derived from the AR(1) stationary variance scaling, which is exact for the discrete process. The continuous-time analog (Ornstein-Uhlenbeck) gives the same scaling. A full derivation from the stochastic mismatch SDE would unify Regimes 1 and 2 under a single framework with drift and diffusion terms.
- Asymmetric coupling ($\gamma_A \neq \gamma_B$) appears as a multiplicative prefactor $\gamma_A / \gamma_B$ that shifts the mismatch ratio without changing the exponent. An agent with lower tempo but higher coupling effectiveness ($\gamma$) can partially compensate — but the squared dependence on tempo dominates for large tempo ratios.

*(Descended from TFT Corollary 11.2.)*


<a id="communication-gain"></a>

### Hypothesis III.9: *Communication Gain*

When an agent incorporates information from another agent (rather than from direct observation), the optimal update gain extends the uncertainty ratio with additional terms for source quality and alignment uncertainty.

#### Formal Expression

*[Hypothesis (communication-gain)]*

$$\eta_{ji}^* = \frac{U_{M_i}}{U_{M_i} + U_{o,ji} + U_{\text{src},j} + U_{\text{align},ji}}$$

where:
- $U_{M_i}$: agent $i$'s model uncertainty (same as [Empirical I.19](#update-gain))
- $U_{o,ji}$: **communication channel noise** — latency, ambiguity, compression loss, bandwidth limitations of the channel between $j$ and $i$
- $U_{\text{src},j}$: **source quality uncertainty** — $i$'s uncertainty about $j$'s model calibration and domain competence
- $U_{\text{align},ji}$: **alignment uncertainty** — $i$'s uncertainty about whether $j$'s communications serve $i$'s interests or $j$'s potentially conflicting objectives

When all additional terms are zero (perfect channel, calibrated and aligned source): $\eta_{ji}^\ast \to 1$ (full trust). When any term is large: $\eta_{ji}^\ast \to 0$ (ignore the signal).

**Connection to single-agent case.** When $j$ is the environment (direct observation): $U_{\text{src}} = U_{\text{align}} = 0$, recovering [Empirical I.19](#update-gain)'s standard form $\eta^\ast = U_M / (U_M + U_o)$.

#### Epistemic Status

*Hypothesis.* The additive denominator treats all uncertainty sources as independent, zero-mean noise — a structural heuristic, not a strict variance derivation. This is appropriate for $U_{o,ji}$ (channel noise) and $U_{\text{src},j}$ (miscalibration), which are typically unstructured. For $U_{\text{align},ji}$ (deception), additivity is conservative: it correctly drives $\eta_{ji}^\ast$ toward zero when alignment uncertainty is high, but misses the adversary's *actual* strategy — presenting as trustworthy to exploit high $\eta_{ji}^\ast$. The additive model captures the *defender's* response to detected misalignment; it does not model the *attacker's* optimization over the defender's trust dynamics.

All four uncertainty terms must be expressed in a **common predictive-dispersion scale** before summation — the same units as $U_{M_i}$ (variance of the predictive distribution over the observed quantity). When hard to estimate directly, a conservative approximation: set $U_{\text{src}} + U_{\text{align}}$ to the empirical variance of $j$'s past prediction residuals as observed by $i$, minus the known channel noise $U_{o,ji}$.

#### Discussion

**The denominator terms have different natures.** $U_{o,ji}$ is a property of the *channel* — improvable by infrastructure. $U_{\text{src},j}$ is a property of the *source* — improvable by $j$ improving its model, or estimable by $i$ through calibration tracking. $U_{\text{align},ji}$ is a property of the *relationship* — the game-theoretic variable.

**Trust calibration as a meta-model.** Agent $i$'s estimates of $U_{\text{src},j}$ and $U_{\text{align},ji}$ constitute a **trust meta-model** — a model of models. This meta-model is itself subject to ACT's full apparatus: it has mismatch (trust prediction errors), should be updated with appropriate gain (not overreacting to single disagreements), and can be structurally inadequate ([Result I.26](#structural-adaptation-necessity) — the agent's trust model class may not capture the actual reliability structure of its sources).

**Risk-asymmetric trust.** The Bayesian posterior on source reliability gives the best *estimate*, but the *decision* about how much to trust should be risk-weighted. Trusting a deceptive agent (HILP — high impact, low probability) can cause catastrophic model corruption ([Derived III.10](#adversarial-destabilization), effects spiral). Mild miscalibration toward a reliable source (LIHP) causes small ongoing inefficiency. For high-stakes interactions, use a conservative quantile of the trust posterior rather than the mean — require more evidence before granting high trust.

**Trust transitivity.** When agent $i$ has no direct experience with agent $k$, but trusted intermediary $j$ provides an assessment, the transitive trust question arises. A Bayesian mixture model discounts the recommendation by the intermediary's own reliability:

$$P_i(\theta_k \mid s_j) \propto \left[r_{ji} \cdot P(s_j \mid \theta_k) + (1 - r_{ji}) \cdot P_0(s_j)\right] \cdot P_i(\theta_k)$$

where $r_{ji}$ is $i$'s reliability estimate of $j$ and $\theta_k$ is $k$'s true alignment. When $r_{ji} \to 0$, the posterior collapses to the prior (no update); when $r_{ji} \to 1$, the full informative likelihood applies. This model gives a principled three-phase trust formation: prior → transitive update → direct experience (which eventually swamps the prior).

#### Working Notes

- The communication gain enters the distributed tempo: $\mathcal{T}_i = \sum_k \nu_i^{(k)} \eta_i^{(k)\ast} + \sum_{j} \nu_{ji}^{\text{comm}} \eta_{ji}^\ast$. This is the formal basis for [Derived III.7](#team-persistence) — teams persist where individuals cannot because cooperative communication adds to each agent's effective tempo.
- Coordination overhead limits team size: adding members increases communication tempo with diminishing returns while coordination costs grow. The optimal team size occurs where marginal communication tempo equals marginal coordination cost. This connects to organizational theory (span of control, communication overhead).
- The adversary's strategy (making $U_{\text{align}}$ *appear* low) creates a meta-game on trust estimation. This is where game theory enters — the trust calibration itself is strategic. ACT provides the state variables (mismatch, gain, tempo, reserve); game theory provides the equilibrium analysis.
- Open: when multiple intermediaries provide corroborating recommendations about $k$, correlation matters. If all got their information from the same source, corroboration is illusory.
- Consider eventually **splitting $U_{\text{src},j}$ from $U_{\text{align},ji}$** into separate treatment tracks, not just separate denominator terms. Source calibration uncertainty is an *estimation* problem (estimable, improvable, converges with data). Alignment uncertainty is a *strategic* problem (the adversary optimizes *over* the defender's trust policy, not independently of it). The additive heuristic correctly drives $\eta_{ji}^\ast$ toward zero in both cases, but a richer model would separate the estimation problem (how good is this source?) from the trust-policy problem (how much should I trust, given that the source knows my trust policy?). The latter requires game-theoretic treatment — ACT provides the state variables; the equilibrium analysis is external.

*(Descended from TFT Appendix F, Section F.2.)*


<a id="adversarial-destabilization"></a>

### Derived III.10: *Adversarial Destabilization*

When two agents are coupled such that one's actions contribute to the other's disturbance rate, the faster agent can drive the slower agent outside its invariant region — causing the correction mechanism to break down entirely.

#### Formal Expression

*[Derived (adversarial-destabilization, from sector-condition-stability)]*

**Setup.** Let both agents $A$ and $B$ satisfy the sector condition (A1, A2', A3 from [Derivation A.1](#sector-condition-derivation)) with respective parameters $(\alpha_A, R_A, \rho_{A,\text{base}})$ and $(\alpha_B, R_B, \rho_{B,\text{base}})$. The coupling:

*[Assumption (Coupling Model)]*

$$\rho_B = \rho_{B,\text{base}} + \gamma_A \cdot \mathcal{T}_A$$

where $\gamma_A \gt 0$ represents the effectiveness of $A$'s actions at disrupting $B$'s environment.

**Result.** $B$'s ultimately bounded radius under coupled dynamics is:

$$R^*_B = \frac{\rho_{B,\text{base}} + \gamma_A \cdot \mathcal{T}_A}{\alpha_B}$$

$B$ diverges (exits its sector-condition region) when $R^\ast_B \gt R_B$, i.e., when:

$$\gamma_A \cdot \mathcal{T}_A \gt \alpha_B R_B - \rho_{B,\text{base}} = \Delta\rho^*_B$$

That is:

$$\mathcal{T}_A \gt \frac{\Delta\rho^*_B}{\gamma_A}$$

Symmetrically, $B$ destabilizes $A$ when $\mathcal{T}_B \gt \Delta\rho^\ast_A / \gamma_B$.

The adversarial outcome depends on whether either agent can push the other past its stability limit. $\square$

**Interpretation.** "Getting inside the opponent's OODA loop" has a precise Lyapunov characterization: Agent $A$ destabilizes Agent $B$ when $A$'s tempo, multiplied by coupling effectiveness, exceeds $B$'s adaptive reserve $\Delta\rho^\ast_B$. This captures:

- **Asymmetric coupling** ($\gamma_A \neq \gamma_B$): an agent with lower tempo but higher coupling effectiveness can still win.
- **Finite reserves**: an agent with very high $\mathcal{T}$ but operating near its model-class limit ($\Delta\rho^\ast$ small) is vulnerable despite high tempo.
- **Structural collapse**: when $R^\ast_B \gt R_B$, the failure mode is not merely "large mismatch" but "correction mechanism breakdown" — connecting to [Result I.26](#structural-adaptation-necessity).

##### Corollary: The Effects Spiral

When Agent $B$ is driven past its stability boundary ($R^\ast_B \gt R_B$), and $B$'s degrading model causes $B$'s actions to become erratic in a way that increases $A$'s coupling effectiveness ($\gamma_A$ increases with $\Vert\delta_B\Vert$), the result is a positive-feedback Lyapunov instability:

*[Discussion — Mechanism Schematic]*

$$\Vert\delta_B\Vert \uparrow \;\Rightarrow\; B\text{'s actions become erratic} \;\Rightarrow\; \gamma_A \uparrow \;\Rightarrow\; \rho_B \uparrow \;\Rightarrow\; \Vert\delta_B\Vert \uparrow$$

With $\gamma_A$ now an increasing function of $\Vert\delta_B\Vert$, the disturbance term in $B$'s dynamics grows superlinearly. $\dot{V}_B \gt 0$ and increasing — mismatch accelerates away from the stability region. The spiral terminates only when $B$ undergoes structural adaptation ([Result I.26](#structural-adaptation-necessity) — changing the model class) or ceases to function as an adaptive agent entirely.

#### Epistemic Status

The destabilization threshold is *exact* under the coupling model (which treats $\mathcal{T}_A$ as exogenous). The coupling model itself is an *assumption* — it decouples the agents rather than modeling the fully coupled dynamical system where both agents' mismatch states co-evolve. The analysis therefore characterizes the *destabilization threshold* (the conditions under which $A$ *can* push $B$ past its stability boundary) rather than the full transient dynamics. This is a worst-case bound, treating $A$ as operating at its steady-state tempo.

The effects spiral (corollary) is *discussion-grade* — the positive-feedback mechanism is qualitatively clear, but formalizing the $\gamma_A(\Vert\delta_B\Vert)$ functional form and proving instability under it requires specifying how an agent's degrading model affects its action quality, which the theory does not yet formalize.

A full coupled Lyapunov analysis with a joint function $V(\delta_A, \delta_B)$ would capture mutual feedback effects but requires specifying how each agent's mismatch state affects the other's disturbance in real time — an open extension.

#### Discussion

**Destabilization vs. steady-state ratio.** The linear analysis in [Hypothesis I.22](#mismatch-dynamics) gives the steady-state mismatch ratio under coupling: a quantitative result about how much worse $B$ does. This segment gives the qualitative result: under what conditions does $B$ *fail entirely*, not merely fall behind. The linear analysis tells you the score; the Lyapunov analysis tells you when the game is over.

**Connection to [Result III.8](#adversarial-tempo-advantage).** The simulation results show the tempo advantage is superlinear (exponent $\approx 2$ in pure adversarial regimes). This Lyapunov result explains WHY: the destabilization threshold creates a phase transition — below it, $B$ persists (possibly with degraded performance); above it, $B$'s correction mechanism collapses entirely, and the effects spiral accelerates the collapse.

#### Working Notes

- The decoupled analysis (treating $\mathcal{T}_A$ as exogenous) is conservative — it's the best case for $A$. In a fully coupled system, $A$'s actions against $B$ may divert adaptive capacity from $A$'s own mismatch correction, creating a self-limiting effect. The coupled Lyapunov analysis is the open problem.
- $\gamma_A$ is the product of coupling strength, observability, and action impact — it captures the full spectrum from tightly coupled (direct disruption) to loosely coupled (indirect environmental effects). In the software domain, coupling is precisely measurable from the dependency graph ([Definition IV.18](#system-coupling)).
- The effects spiral is the formal analog of Boyd's cascading disorientation of the slower adversary — the same structural pattern (tempo advantage → destabilization → accelerating breakdown) appears in the Lyapunov analysis. The model captures the pattern; whether it captures the actual mechanisms of human disorientation is an empirical question, not a mathematical one. Future work should formalize the $\gamma_A(\Vert\delta_B\Vert)$ relationship to make the spiral a result rather than a discussion-grade observation.

*(Descended from TFT Appendix A, Prop A.3 and Cor A.3.1.)*


> **\[GAP\]** Which strategy edges are most valuable to attack


<a id="adversarial-exponent-regimes"></a>

### Observation III.11: *Adversarial Exponent Regimes*

The adversarial tempo advantage exponent — the power $b$ in $\Vert\delta_B\Vert / \Vert\delta_A\Vert \sim (\mathcal T_A / \mathcal T_B)^b$ — is not a single number. It depends on two structural features of the disturbance: whether the adversarial coupling enters as deterministic drift or stochastic noise, and whether the coupling dominates the base disturbance rate. Three regimes emerge from simulation.

#### Formal Expression

*[Observation (adversarial-exponent-regimes, from track-b simulations)]*

**Regime 1: Deterministic drift, coupling-dominant.** When adversarial coupling enters as a persistent directional disturbance ($\rho_B = \rho_{\text{base}} + \gamma \cdot \mathcal T_A$, deterministic) and coupling dominates ($\gamma \cdot \mathcal T_B \gg \rho_{\text{base}}$):

$$b \to 2.0 \qquad \text{(confirmed at 1.999)}$$

This is the exact prediction of the mismatch ODE steady state $\Vert\delta\Vert_{ss} = \rho / \mathcal{T}$.

**Regime 2: Stochastic noise, coupling-dominant.** When adversarial coupling enters through the noise scale of zero-mean perturbations ($\sigma_B = \sigma_{\text{base}} + \gamma \cdot \mathcal T_A$) and coupling dominates:

$$b \to 1.5$$

Root cause: the AR(1) steady-state RMS scales as $\rho / \sqrt{\mathcal{T}}$ (not $\rho / \mathcal{T}$), because variance scales as $\rho^2 / \mathcal{T}$ and the expected absolute deviation scales as the square root of variance.

**Regime 3: Non-coupling-dominant.** When base disturbance is comparable to or exceeds the adversarial coupling ($\rho_{\text{base}} \gtrsim \gamma \cdot \mathcal T_B$):

$$b \to 1.0 \text{ (deterministic)} \quad \text{or} \quad b \to 0.5 \text{ (stochastic)}$$

The exponent degrades smoothly as the base-to-coupling ratio increases.

| $\rho_{\text{base}} / (\gamma \cdot \mathcal T_B)$ | Exponent (deterministic) | Exponent (stochastic) |
|:---:|:---:|:---:|
| 0.002 | 1.999 | 1.481 |
| 0.20 | 1.877 | 1.101 |
| 2.0 | 1.445 | 0.791 |
| 6.3 | 1.213 | 0.577 |

#### Epistemic Status

*Empirical.* Max attainable: exact conditional on disturbance model. The three regimes are established by simulation (6 variants, multiple parameter sweeps) and confirmed by analytical derivation of the AR(1) steady-state scaling. The deterministic exponent ($b = 2$) is derivable from the mismatch ODE; the stochastic exponent ($b = 1.5$) is derivable from the AR(1) stationary variance. What is empirical is the claim that real adversarial interactions fall into these regimes — whether a given adversary's tempo increases systematic drift vs. unpredictability is a domain question.

#### Discussion

**The mismatch ODE conflates two quantities.** The equation $d\Vert\delta\Vert/dt = -\mathcal{T} \cdot \Vert\delta\Vert + \rho$ is ambiguous about whether $\rho$ represents deterministic drift (persistent directional change) or stochastic noise scale (unpredictable fluctuations). These give different steady-state scaling: $\rho / \mathcal{T}$ vs. $\rho / \sqrt{\mathcal{T}}$. For the mismatch dynamics ([Hypothesis I.22](#mismatch-dynamics)), this distinction needs explicit treatment.

**Why the squared law held for the coupling-dominance sweep.** In Variant A, the coupling enters as deterministic drift: $\rho_B = \rho_{\text{base}} + \gamma \cdot \mathcal T_A$, and the steady state is $\Vert\delta_B\Vert = \rho_B / \mathcal T_B$. The ratio $\Vert\delta_B\Vert / \Vert\delta_A\Vert$ in the coupling-dominant limit gives $(\mathcal T_A / \mathcal T_B)^2$ directly.

**Nonlinear correction creates thresholds, not lower exponents.** For saturating, sigmoid, and breakdown correction functions under deterministic drift, the issue is not a reduced exponent but a catastrophic divergence when $\rho$ exceeds the correction capacity ($\rho \gt \mathcal{T} \cdot R$). This is exactly the persistence threshold failure ([Result I.24](#persistence-condition)), observed directly in simulation.

**Domain interpretation.** Whether a given opponent's tempo increase causes deterministic drift or stochastic noise depends on the domain:
- Military: an opponent who maneuvers faster creates systematic positional change (drift, $b \approx 2$)
- Market: a competitor who acts unpredictably creates noise in signals ($b \approx 1.5$)
- Software: a fast-changing API creates systematic drift in the codebase state (drift)
- Adversarial ML: an opponent who varies attack vectors increases observation noise ($b \approx 1.5$)

#### Working Notes
- The interpolation between drift and noise regimes (Variant B) shows smooth transition, not a sharp boundary. At mixed drift-noise coupling, the exponent lies between the two asymptotes. The drift fraction $f = \mu / (\mu + \sigma)$ continuously parameterizes the transition.
- The exponent of 1.05 from the original sim2 was not a falsification of Corollary 11.2 — it reflected a stochastic model (noise-variance coupling) tested in a non-coupling-dominant regime. The original simulation was testing the wrong regime for the ODE's prediction.
- Simulation code: `scratch/track-b-nonlinear-sims/variants/variant_ab_drift.py`, `variant_cd_regimes.py`. Results: `variant_ab_results.md`, `variant_cd_results.md`.


<a id="observation-gates-advantage"></a>

### Observation III.12: *Observation Noise Gates Adversarial Advantage*

Observation noise collapses the adversarial tempo advantage. When agents observe their mismatch through a noisy channel, the faster agent's additional corrections become noisy, partially offsetting its tempo advantage. The optimal gain ([Empirical I.19](#update-gain)) partially restores the advantage but cannot fully recover it.

#### Formal Expression

*[Observation (observation-gates-advantage, from track-b Variant E)]*

In a two-agent adversarial system with observation noise $\sigma_{\text{obs}}$ added to each agent's mismatch signal:

| $\sigma_{\text{obs}}$ | Exponent (fixed $\eta$) | Exponent (optimal $\eta^\ast$) |
|:---:|:---:|:---:|
| 0.00 | 1.04 | 1.04 |
| 0.10 | 1.00 | 0.97 |
| 0.20 | 0.92 | 0.94 |
| 0.50 | 0.60 | 0.63 |
| 1.00 | 0.18 | 0.40 |

At $\sigma_{\text{obs}} = 1.0$ (10x the process noise), the fixed-gain adversarial exponent drops from $\sim 1.0$ to $\sim 0.2$ — tempo advantage nearly vanishes. The Riccati-optimal gain restores it to $\sim 0.4$, more than doubling the advantage but not recovering the noise-free level.

**The mechanism.** When observation noise is high, each correction step adds noise to the mismatch estimate. The faster agent makes more corrections per unit time, each noisy, partially offsetting the benefit of higher tempo. The optimal gain mitigates this by reducing $\eta$ to match the noise level — correcting less aggressively but more accurately.

#### Epistemic Status

*Empirical.* Max attainable: derived (the mechanism is analytically tractable via Riccati analysis of noisy AR(1) processes). The observation that noise degrades advantage is confirmed by simulation. The optimal gain's partial restoration is consistent with the uncertainty ratio principle ([Empirical I.19](#update-gain): $\eta^\ast = U_M / (U_M + U_o)$). The quantitative degradation curve ($b$ vs. $\sigma_{\text{obs}}$) is empirical at these parameters; a general analytical expression would require solving the coupled noisy-AR(1) system.

#### Discussion

**Observation quality gates tempo advantage.** Boyd insisted that the quality of Orient (observation processing) matters more than raw OODA speed. The simulation results show a formal analog of this pattern: faster tempo with noisy observations ($\sigma_{\text{obs}}$ high) gives nearly zero advantage over a slower agent with equally noisy observations. The tempo advantage is gated by observation quality — consistent with Boyd's emphasis, though the model captures a specific mechanism (noisy correction steps) rather than the full richness of Orient processing.

**The optimal gain helps most in the moderate-noise regime.** At $\sigma_{\text{obs}} = 0.05$ (observation noise half of process noise), the optimal gain cuts steady-state mismatch by 52% compared to fixed gain. At very high noise, the improvement is less dramatic in absolute terms but more important relatively (0.40 vs. 0.18 exponent).

**Practical implication.** An agent facing an adversary with superior tempo should invest in degrading the adversary's observation quality rather than trying to match their speed. Conversely, an agent with superior tempo should protect its observation channels — the tempo advantage is only as good as the observation quality that supports it.

**Connection to code quality.** In the software domain ([Discussion IV.11](#code-quality-as-observation-infrastructure)), code quality IS observation infrastructure. A well-structured codebase provides low-noise observations (clear tests, readable code, explicit interfaces). A poorly structured codebase adds observation noise to every development cycle, degrading the developer's effective tempo regardless of how fast they work.

#### Working Notes
- The finding that fixed $\eta = 0.1$ is "remarkably robust" to observation noise (42% degradation at $\sigma_{\text{obs}} = 10 \times q_{\text{env}}$) suggests that conservative gains are a reasonable default for environments with unknown noise levels. The cost of being slightly below optimal is much less than the cost of being above optimal (overcorrection amplifies noise).
- The interaction between observation noise and adversarial exponent regime (drift vs. stochastic) has not been tested. The Variant E results use stochastic coupling only. Whether observation noise degrades the deterministic-drift exponent ($b = 2$) by the same proportion is an open question.
- Simulation code: `scratch/track-b-nonlinear-sims/variants/variant_ef_extensions.py`. Results: `variant_ef_results.md`.


<a id="per-dimension-persistence"></a>

### Result III.13: *Per-Dimension Persistence*

The scalar persistence condition $\mathcal{T} \gt \rho / \Vert\delta_{\text{critical}}\Vert$ overestimates adaptive capacity when the agent's correction gain varies across dimensions. The weak dimension is the bottleneck — it dominates the aggregate mismatch regardless of performance on strong dimensions. The correct condition is per-dimension: $\mathcal T_k \gt \rho_k / \Vert\delta_{\text{critical},k}\Vert$ for each dimension $k$ with significant disturbance.

#### Formal Expression

*[Result (per-dimension-persistence)]*

For an agent with $d$-dimensional mismatch $\delta_t \in \mathbb{R}^d$, diagonal correction gain $\eta = \text{diag}(\eta_1, \ldots, \eta_d)$, and per-dimension disturbance $\rho_k$:

The per-dimension steady-state mismatch (AR(1) process) is:

$$E[\Vert\delta_k\Vert] = \frac{\rho_k}{\sqrt{2\eta_k - \eta_k^2}} \cdot \sqrt{\frac{2}{\pi}}$$

which for small $\eta_k$ approximates:

$$E[\Vert\delta_k\Vert] \approx \frac{\rho_k}{\sqrt{2\eta_k}} \cdot \sqrt{\frac{2}{\pi}}$$

**Persistence requires** $\eta_k \gt \rho_k / \Vert\delta_{\text{critical},k}\Vert$ **for each dimension independently.**

The aggregate $L_2$ mismatch $\Vert\delta\Vert = \sqrt{\sum_k \delta_k^2}$ is dominated by the dimension with the largest $\rho_k / \eta_k$ ratio.

#### Epistemic Status

*Exact.* The per-dimension steady state is derived from the AR(1) stationary distribution and matches simulation to 4 significant figures. The scalar tempo overestimates by 72% in a 3-dimensional test case with 5:1 gain variation. This is a mathematical result, not an approximation — the per-dimension AR(1) processes are independent under diagonal correction, so the per-dimension theory is simply the 1D result applied per dimension.

#### Discussion

**Scalar tempo overestimates.** In a 3D system with gains $\eta = (0.15, 0.03, 0.03)$ and disturbances $\rho = (0.20, 0.20, 0.02)$:

| Dimension | $\eta_k$ | $\rho_k$ | $\rho_k / \eta_k$ | $E[\Vert\delta_k\Vert]$ |
|:-:|:-:|:-:|:-:|:-:|
| 1 (well-tracked) | 0.15 | 0.20 | 1.33 | 0.303 |
| 2 (weak) | 0.03 | 0.20 | 6.67 | 0.656 |
| 3 (unimportant) | 0.03 | 0.02 | 0.67 | 0.066 |

Scalar prediction: $\rho / \mathcal{T} = 0.284 / 0.21 = 1.35$. Actual $\Vert\delta\Vert_{L_2} = 0.785$. Overestimate: 72%. Dimension 2 alone accounts for 84% of the $L_2$ mismatch.

**Isotropic allocation dominates.** Equalizing the same total gain budget ($\eta = 0.07$ per dimension) reduces $\Vert\delta\Vert_{L_2}$ from 0.785 to 0.685 — a 13% improvement — because it reduces the bottleneck effect on the weak dimension.

**Adversarial exploitation.** An adversary who identifies the target's weak dimension can concentrate disturbance there. Targeted attack (80% on the weak dimension) amplifies the mismatch ratio by 17% (from 2.70 to 3.15). The real danger is structural: if the weak dimension's mismatch exceeds its critical threshold ($R_{\text{max}}$), correction fails on that dimension while the aggregate $\Vert\delta\Vert_{L_2}$ may still look manageable. Per-dimension monitoring is essential.

**Implications for the persistence condition.** The scalar persistence condition ([Result I.24](#persistence-condition)) remains correct as a *necessary* condition: if the aggregate tempo is insufficient, the agent fails. But it is not *sufficient* — an agent can satisfy the scalar condition while failing on a single dimension. The per-dimension condition $\mathcal T_k \gt \rho_k / \Vert\delta_{\text{critical},k}\Vert$ is both necessary and sufficient (under diagonal correction).

**Connection to multi-agent systems.** The per-dimension result has a direct multi-agent analog: in a composite agent, each sub-agent's contribution to composite tempo may be strong in some dimensions and weak in others. The composite's persistence requires coverage across all relevant dimensions — a team of specialists who each handle one dimension well composes better than a team of generalists who are mediocre at everything, provided the dimension assignment matches.

#### Working Notes
- The diagonal-correction assumption is restrictive. Real agents may have cross-dimensional correction (fixing one thing improves another). Off-diagonal correction terms would couple the dimensions and change the analysis. Whether the weak-dimension bottleneck persists under coupled correction is an open question — it likely does qualitatively (the weakest dimension still dominates) but the quantitative overestimate may shrink.
- The tensor formulation of tempo (tracking per-dimension adaptive capacity) would replace the scalar $\mathcal{T}$ with a diagonal matrix $\mathcal{T} = \text{diag}(\mathcal T_1, \ldots, \mathcal T_d)$. The persistence condition becomes $\mathcal T_k \gt \rho_k / \delta_{\text{critical},k}$ for each $k$. This is mentioned in [Definition I.21](#adaptive-tempo)'s Discussion but not yet formalized.
- Simulation code: `scratch/track-b-nonlinear-sims/variants/variant_ef_extensions.py`. Results: `variant_ef_results.md`.



---

## IV. Agentic-Grounded Software Systems

*Domain instantiation: software development as an ACT domain. This section re-grounds TST (Temporal Software Theory) in ACT's formal machinery — adding the causal mathematics and adaptive dynamics that TST was developed without. Software is not just another domain example; it has unique epistemic properties that make it the ideal testbed for ACT and, recursively, the domain where ACT-grounded agents will operate.*

*The temporal optimality postulate ([Postulate I.1](#temporal-optimality)) now has full backing: tempo advantage ([Result III.8](#adversarial-tempo-advantage)), persistence conditions ([Result I.24](#persistence-condition)), and gain dynamics ([Empirical I.19](#update-gain)) explain WHY time-optimal development practices work, not just THAT they do.*


<a id="software-scope"></a>

### Scope IV.1: *Software Scope*

ACT's software domain applies to systems with non-negligible probability of future change.

#### Formal Expression

*[Scope (software-scope)]*

$$\mathcal{S}_{\text{evolving}} = \{S : P(n_{\text{future}}(S) \gt 0) \gt \varepsilon\}$$

For $S \in \mathcal{S}_{\text{evolving}}$, the total time subject to optimization is:

*[Derived (software-scope, from temporal-optimality)]*

$$\text{time}_{\text{total}}(S) = \text{time}(F_0) + \sum_{i=1}^{n_{\text{future}}} \text{time}(F_i)$$

When $n_{\text{future}}$ is non-trivial, the sum dominates: $\sum_{i=1}^{n_{\text{future}}} \text{time}(F_i) \gg \text{time}(F_0)$. Under [Postulate I.1](#temporal-optimality), this means optimizing lifecycle time, not initial implementation time.

##### The stable-subsystem corollary

For any subsystem $s$ where $P(\text{change}(s)) \lt \varepsilon$:

*[Derived (software-scope, from scope definition)]*

$$\text{time}_{\text{future}}(s) \to 0$$

A subsystem with negligible change probability consumes zero future development time. In ACT terms: its environment change rate $\rho \to 0$, so from [Result I.24](#persistence-condition), any nonzero tempo suffices — the subsystem is permanently adapted. No adaptive capacity needs to be allocated to it.

This justifies using stable, battle-tested libraries and frameworks: reimplementing `sort()` takes a subsystem at $\rho \approx 0$ and reintroduces it at finite $\rho$, consuming adaptive capacity that could be directed elsewhere.

#### Epistemic Status

The scope restriction is definitional — we choose to analyze evolving systems. The consequence (lifecycle time dominates initial time) follows from [Postulate I.1](#temporal-optimality) applied to the scope. The stable-subsystem corollary follows directly from the scope definition. The connection to [Result I.24](#persistence-condition) ($\rho \to 0$ means trivially satisfied persistence) is a restatement in ACT's formal language, not a new derivation.

#### Discussion

**The productive tension.** Stable cores should be identified and left alone (or adopted from external libraries). But premature extraction — treating a subsystem as stable when $P(\text{change})$ is actually non-negligible — loses the benefit. The estimation of $P(\text{change})$ is itself an act of model-building ([Formulation I.10](#agent-model)): experienced developers are implicitly estimating $\rho$ per subsystem and allocating adaptive capacity accordingly.

**Initial implementation as initial conditions.** The scope reframes software development: we are not building a static artifact but establishing initial conditions for a temporal evolution. The quality of those initial conditions ([Derived IV.10](#change-investment)) compounds through every subsequent feature. This is not a metaphor — it is the direct application of [Postulate I.1](#temporal-optimality) to a system with $n_{\text{future}} \gg 1$.

#### Working Notes

- The $\varepsilon$ threshold is a parameter choice, not derived. What determines a sensible $\varepsilon$? Is it related to the team's ability to detect change (an observation threshold)?
- TST's original "infinite velocity" language is vivid but potentially misleading — velocity is undefined when there are zero changes. The ACT framing ($\rho \to 0$, persistence trivially satisfied) is more precise.
- The via-tft-mapping material has a much richer decomposition of the software "environment" (codebase, runtime behavior, user requirements, team knowledge, dependency ecosystem, infrastructure state). This scope segment doesn't need that detail, but [Definition IV.6](#developer-as-act-agent) or [Observation IV.2](#software-epistemic-properties) should incorporate it.
- The observation that software development = building systems that evolve efficiently is essentially the claim that software development is an adaptive process subject to ACT. This is what motivates the entire section, not just this scope narrowing.

*(Descended from TST T-03.)*


<a id="software-epistemic-properties"></a>

### Observation IV.2: *Software's 6 unique properties*

*Segment `software-epistemic-properties` has not yet been written.*


<a id="feature-definition"></a>

### Definition IV.3: *Feature*

A unit of functionality, as perceived by those who requested, implement, or use it, that coherently changes the codebase and/or running system.

#### Formal Expression

*[Definition (feature-definition)]*

A **feature** $F$ is a deliberate change to a software system $S \in \mathcal{S}_{\text{evolving}}$ ([Scope IV.1](#software-scope)) that:

1. Coherently modifies the codebase and/or running system behavior
2. Is perceived as a unit by at least one stakeholder (requester, implementer, or user)

**Included:**
- Changes to non-functional requirements (performance, security, accessibility)
- Infrastructure changes affecting system capabilities
- Documentation changes affecting stakeholder understanding
- Configuration changes and coordinated changes across coupled systems
- Refactoring: changes that alter future implementation time while preserving external behavior

**Excluded:**
- Pure no-ops (changes with no effect on behavior or future development cost)

Note: what practitioners call "no-op changes" are typically refactoring and fall under this definition.

#### Epistemic Status

Definitional. This is a scoping choice about the unit of analysis, not a derived result. The definition is deliberately broad (refactoring counts as a feature) because under [Postulate I.1](#temporal-optimality), any change that affects future time is subject to optimization.

#### Discussion

**The refactoring inclusion matters.** By including changes that "alter future implementation time while preserving external behavior," the definition ensures that investments in code quality, naming, structure, and documentation are first-class features subject to the same temporal optimization as user-facing changes. This is not a value judgment about whether refactoring is good — it is a scope decision that brings refactoring under the theory's analysis.

**"As perceived by" is a level-of-description qualifier.** Different agents at different levels of composition ([Postulate I.6](#composition-consistency)) may perceive the same change as different features. A single commit might be part of one feature for the developer and part of a different feature for the product manager. The definition does not privilege one level — the relevant decomposition depends on which agent's temporal optimization is being analyzed. This is consistent with ACT's scale-invariant scope condition.

**The atomic changeset ([Definition IV.13](#atomic-changeset)) operationalizes this definition.** A feature is the conceptual unit; the changeset is its physical manifestation in the codebase.

#### Working Notes

- In ACT terms, a feature is a deliberate intervention on the software environment — the agent choosing to $do(F)$ and observing the consequences. This connects to [Definition I.8](#pearl-causal-hierarchy) (Level 2) and [Definition I.20](#causal-information-yield) (the information gained from implementing F). But whether this connection adds analytical power or is just relabeling needs thought.
- The "as perceived by" qualifier creates a measurement problem: different stakeholders disagree about feature boundaries. Is there a principled way to resolve this, or is it inherently level-dependent?
- Refactoring as a feature that modifies the observation channel: well-named code reduces $U_o$ for future readers. This connects refactoring to [Discussion IV.11](#code-quality-as-observation-infrastructure), which is currently a gap. When that segment is written, the connection should be made explicit.

*(Descended from TST D-01.)*


<a id="specification-bound"></a>

### Result IV.4: *Specification Bound*

The minimum time to implement a feature is bounded below by the time required to transmit enough information for the implementer to distinguish the intended feature from competing possibilities. Written specification and demonstration are special cases of this more general transmission bound.

#### Formal Expression

*[Derived (specification-bound)]*

$$\forall \text{ feature } F: \quad \text{time}_{\min}(F) \geq \inf_{c \in \mathcal{C}_{\text{suff}}(F)} \text{time}_{\text{transmit}}(F, c, M_{\text{shared}})$$

where:
- $\mathcal{C}_{\text{suff}}(F)$ is the set of communication channels or transmission paths sufficient to convey feature $F$ to the implementer
- $M_{\text{shared}}$ is the context shared by specifier and implementer
- $\text{time}_{\text{transmit}}(F, c, M_{\text{shared}})$ is the time required for channel $c$ to transmit enough information, given that shared context

*[Derived (two-channel special case)]*

If the only admissible sufficient channels are written specification and demonstration, the general bound reduces to:

$$\text{time}_{\min}(F) \geq \min\!\big(\text{time}_{\text{specify}}(F, M_{\text{shared}}),\; \text{time}_{\text{demo}}(F, M_{\text{shared}})\big)$$

*[Derived (specification-time, first-order approximation)]*

$$\text{time}_{\text{specify}}(F, M_{\text{shared}}) \approx \frac{H_{\text{req}}(F \mid M_{\text{shared}})}{R_{\text{spec}}}$$

where:
- $H_{\text{req}}(F \mid M_{\text{shared}})$ is the residual information that must still be communicated once shared context is taken into account
- $R_{\text{spec}}$ is the effective information rate of the specification channel

Shared context acts as compression by reducing $H_{\text{req}}$, not by appearing as a free-standing divisor.

**Assumptions.** The feature $F$ is within [Scope IV.1](#software-scope) (non-negligible future change probability). A channel is "sufficient" if it transmits enough information for the implementer to produce the intended feature, not merely approximate it.

##### Corollary: Communication as Bottleneck

*[Derived (communication-bottleneck)]*

As actual implementation time approaches $\text{time}_{\min}(F)$, communication speed and quality become the limiting factor.

This follows directly: if implementation overhead shrinks (for example, through automation or stronger tools), the remaining irreducible time is the cheapest sufficient transmission path. In many real settings that path is still dominated by communication and context-building.

#### Epistemic Status

The bound's *existence* is *derived* from information theory: you cannot implement what has not been sufficiently distinguished from competing implementations, and that distinction requires transmitting enough residual information through some admissible channel. The general infimum-over-channels statement is the strongest version currently justified. The approximation $\text{time}_{\text{specify}} \approx H_{\text{req}} / R_{\text{spec}}$ is *first-order* — the actual relationship depends on channel characteristics, encoding efficiency, and interaction structure. Neither the exact form of $H_{\text{req}}$ nor the effective rate $R_{\text{spec}}$ is derived within ACT.

#### Discussion

**Shared context as compression.** Domain-specific languages, established conventions, examples, and shared mental models reduce the residual information $H_{\text{req}}(F \mid M_{\text{shared}})$. "Make it like Twitter but for dogs" is an efficient specification only because the receiver already has a rich model of what "Twitter" implies. Without that context, the same feature would require far more transmission time.

**Specification is one channel among many.** Natural language requirements, demonstrations, examples, tests, partial implementations, and prior conventions are all candidate transmission paths. The lower bound is on the cheapest *sufficient* path, not specifically on prose. This is why showing a user a working prototype, giving a failing test, or pointing to an analogous feature can outperform a long written brief.

**Connection to ACT.** In ACT terms, the specification bound constrains how fast $O_t$ ([Definition II.3](#objective-functional)) can be communicated from specifier to implementer. Shared context corresponds to the overlap between specifier's $M_t$ and implementer's $M_t$. When this overlap is small, even a simple objective requires extensive specification.

*[Discussion]* This suggests that $M_t$ quality ([Formulation I.10](#agent-model)) and observation infrastructure ([Discussion IV.11](#code-quality-as-observation-infrastructure)) are load-bearing for the specification bound: shared context built through good code (documentation, naming, structure) reduces specification time for future features. *This connection is structurally motivated but the quantitative relationship between code quality and specification time has not been empirically measured.*

**Empirical indication.** Putnam (1978) empirically discovered implementation time bounds that may approximate $t_{\min} \approx (\text{time}_{\text{specify}})^{3/4}$.
*[Empirical Claim — historical observation, not derived within ACT. The exponent 3/4 is Putnam's empirical finding, not a theoretical prediction.]*

#### Working Notes

- The strongest next tightening would be to define "sufficient" more formally: e.g. the channel must reduce the implementer's posterior uncertainty over acceptable implementations below some task-dependent threshold. Right now sufficiency is intuitive rather than operationalized.
- This segment was written by an earlier agent with less context (noted in WORKBENCH). Needs a review pass during Section I/IV tightening — particularly to connect to the ACT communication framework ([Hypothesis III.9](#communication-gain)) and to make the information-theoretic derivation more explicit.
- The $H_{\text{req}} / R_{\text{spec}}$ expression is still a first-order approximation. A tighter version would separate encoding efficiency, channel noise, and interactive back-and-forth — but that may be over-engineering for a bound that is primarily conceptual.


<a id="change-expectation-baseline"></a>

### Derived IV.5: *Change Expectation Baseline*

Absent specific information about a software system's future, the best prediction for remaining feature count equals the observed past feature count. This is not a heuristic — it is the mathematical consequence of maximum ignorance. Any deviation requires information that justifies it.

#### Formal Expression

*[Derived (change-expectation-baseline, from Jeffrey's prior)]*

**Assumption.** The total lifetime $T$ of the system (measured in features or time) is unknown. We adopt Jeffrey's prior — the unique scale-invariant prior expressing maximum ignorance about a positive scale parameter:

$$\pi(T) \propto \frac{1}{T}$$

**Derivation.** After observing survival to age $t_0$ (or equivalently, $n_{\text{past}}$ features), Bayesian update gives:

$$\pi(T \mid T \gt t_0) = \frac{t_0}{T^2}, \quad T \gt t_0$$

This is a Pareto distribution with shape parameter $\alpha = 1$. The **median** remaining lifetime equals the current age:

$$\text{median}[T - t_0 \mid T \gt t_0] = t_0$$

Mapping to feature counts under approximately uniform feature arrival rate:

*[Derived (Conditional on uniform feature rate)]*

$$\hat{n}_{\text{future}} = n_{\text{past}}$$

where $\hat{n}_{\text{future}}$ denotes the median prediction.

**With additional information $I$, the baseline serves as the prior for Bayesian updating:**

*[Derived (change-expectation-baseline)]*

$$P(n_{\text{future}} \mid n_{\text{past}}, I) = \frac{P(I \mid n_{\text{future}}, n_{\text{past}}) \cdot P(n_{\text{future}} \mid n_{\text{past}})}{P(I \mid n_{\text{past}})}$$

The uninformed baseline is rarely used directly — almost all real code comes with domain knowledge that adjusts expectations. The baseline creates intellectual accountability: deviations from $\hat{n}_{\text{future}} = n_{\text{past}}$ require justification through evidence.

##### Corollary: Investment Scaling

*[Derived (investment-scaling, from change-expectation-baseline)]*

Investment in abstraction and flexibility should scale with $n_{\text{past}}$, since the median-predicted remaining lifetime equals the observed lifetime. Systems with minimal feature history ($n_{\text{past}} \lt 3$) warrant minimal structural investment.

#### Epistemic Status

The Bayesian derivation from Jeffrey's prior is *exact* — standard probability theory, not approximation. Two important qualifications:

**Median, not expectation.** For Pareto($\alpha = 1$), the mean is undefined (the integral diverges). The result $\hat{n}_{\text{future}} = n_{\text{past}}$ is a *median* prediction. TST's original statement as $E[n_{\text{future}} \mid n_{\text{past}}] = n_{\text{past}}$ uses "expected" loosely. This distinction matters when propagating the estimate through nonlinear functions — the median of a function is not generally the function of the median. Downstream claims ([Derived IV.10](#change-investment), [Derived IV.9](#dual-optimization)) that use $n_{\text{future}}$ should be understood as using the median prediction, not the mathematical expectation.

**Uniform feature rate assumption.** The derivation gives remaining *lifetime*, not remaining *feature count*. Mapping time to features requires that features arrive at an approximately uniform rate over the system's history. If feature arrival accelerates (common in growing products) or decelerates (common in mature products), the mapping introduces bias. This assumption should be stated explicitly whenever the result is applied.

The Laplace succession formula ($E[n_{\text{future}} \mid n_{\text{past}}] = n_{\text{past}} + 1$ for small $n_{\text{past}}$) comes from a different model ($\beta$-binomial with uniform prior on the success rate). It is a reasonable complement for small sample sizes but is not derived from the same prior as the main result.

#### Discussion

**Intellectual accountability.** The baseline transforms architectural discussions. "We should abstract this" becomes "what information justifies $\hat{n}_{\text{future}} \gt n_{\text{past}}$ for this component?" Without an answer, the abstraction is premature — mathematically, not aesthetically. This is the Bayesian framework working as intended: strong claims about the future require strong evidence.

**Domain knowledge as Bayesian update.** Specific information adjusts the baseline:
- "This is UI code" → higher change probability than algorithms
- "We're sunsetting next quarter" → $\hat{n}_{\text{future}} \to 0$
- "This connects to a volatile API" → $\hat{n}_{\text{future}}$ likely $\gt n_{\text{past}}$
- "This is a sorting algorithm" → $\hat{n}_{\text{future}} \to 0$ (approaching the stable-subsystem regime of [Scope IV.1](#software-scope))

Each of these is an observation that updates the agent's model $M_t$ about the system's future. The gain applied to these updates ([Empirical I.19](#update-gain)) depends on how reliable the information source is — a product roadmap from an engaged PM carries more weight ($\eta^\ast$ closer to 1) than a vague feeling about market direction.

**Connection to ACT.** The baseline is a statement about the agent's $M_t$ regarding the system's future change rate $\rho$. When the agent has observed $n_{\text{past}}$ changes over time $t_0$, and has no other information, the maximum-ignorance prediction is that $\rho$ will continue at approximately its observed rate. This is the null hypothesis — the starting point before any observations update it.

#### Working Notes

- The median vs expectation issue is real and should be propagated carefully. Every downstream claim that uses $n_{\text{future}}$ (T-05 dual optimization, T-06 change investment, C-04.1 investment scaling) is technically using the median prediction. For symmetric distributions this doesn't matter, but Pareto(1) is heavily right-skewed. This means the true expected number of future changes is *larger than* the median prediction (in fact, undefined/infinite). The practical consequence: if anything, the baseline *underestimates* the case for investment.
- The uniform feature rate assumption is probably the weakest link. In practice, software systems often have phases: rapid early development, maturation, maintenance, decline. A more sophisticated model would use the observed feature *rate trajectory*, not just the count. This is an open refinement.
- TST's open question about velocity inflection is interesting but unformalized: when $\hat{n}_{\text{future}}$ transitions from finite to effectively unbounded, the investment strategy may need to shift from linear to compound-seeking. This awaits proper formalization.
- The C-04.2 Bayesian updating corollary is structurally just restating Bayes' theorem applied to the baseline. It's not an independent claim — it's how all Bayesian updating works. I've folded it into the main exposition rather than making it a separate corollary.

*(Descended from TST T-04, C-04.1, C-04.2.)*


<a id="developer-as-act-agent"></a>

### Definition IV.6: *Developer as $(M_t, O_t, \Sigma_t)$*

*Segment `developer-as-act-agent` has not yet been written.*


<a id="comprehension-time"></a>

### Definition IV.7: *Comprehension Time*

The time from initial idea to first surviving change — the cost of understanding enough to act effectively.

#### Formal Expression

*[Definition (comprehension-time)]*

For a feature $F$ ([Definition IV.3](#feature-definition)) applied to system $S$:

$$t_{\text{comp}}(F, S) = \text{time from task assignment to first surviving modification of } S$$

This includes:
- Reading existing code to understand where to make changes
- Understanding why something was done a certain way
- Discovering hidden dependencies and side effects
- Building and validating a mental model of the relevant portions of $S$

#### Epistemic Status

Definitional. The quantity is well-defined and measurable in principle (though rarely measured in practice). The interpretation in ACT terms (see Discussion) is structurally motivated but not formally derived.

#### Discussion

**In ACT terms, comprehension is constructing $M_t$.** When a developer (or AI agent) begins work on a feature, they must build a model of the relevant portion of the codebase — its structure, dependencies, conventions, state. This is precisely the construction of $M_t$ ([Formulation I.10](#agent-model)) from environmental observations. The time to comprehend is the time to build a model of sufficient quality ([Definition I.12](#model-sufficiency)) to support effective action.

**Comprehension cost compounds under turnover.** If the team has turnover rate $r$ and size $s$, the total comprehension cost across all readers is approximately $t_{\text{comp}} \times (1 + r) \times s$. With 100% context turnover per AI instance, every session pays the full comprehension cost. This makes comprehension time the dominant factor in AI-assisted development, not implementation time.

**The comprehension/implementation boundary is not always sharp.** Exploratory changes (make a modification, see what breaks, learn from the result) blend comprehension and implementation. In ACT terms, these are probe actions ([Definition I.20](#causal-information-yield)) — interventions whose purpose is to generate observations that improve $M_t$, not to advance toward the feature goal.

#### Working Notes

- The claim that comprehension = $M_t$ construction is tempting but may be too simple. The developer is building a model of the code AND the domain AND the mapping between them (as T-07 conceptual alignment points out). Is this one $M_t$ or should it be decomposed? In ACT's current formulation, $M_t$ is the complete agent state — so it includes all of these. But the IB tradeoff ([Formulation I.11](#information-bottleneck)) might have different $\beta$ for code-model vs domain-model.
- Can comprehension time be connected to $U_o$ and $\eta^\ast$? Well-written code (low $U_o$) should enable faster $M_t$ construction (higher $\eta^\ast$ per observation). The connection is qualitatively clear but quantitatively unformalized.
- The "surviving" qualifier is important — false starts that get reverted don't count. This means comprehension time is retrospectively defined, which creates measurement challenges.

*(Descended from TST D-02.)*


<a id="implementation-time"></a>

### Definition IV.8: *Implementation Time*

The time from first surviving change to complete feature.

#### Formal Expression

*[Definition (implementation-time)]*

For a feature $F$ ([Definition IV.3](#feature-definition)) applied to system $S$:

$$t_{\text{impl}}(F, S) = \text{time from first surviving modification to feature completion}$$

This includes:
- Writing and modifying code
- Local testing and validation
- Addressing immediate issues discovered during implementation

By construction, the total feature time decomposes:

$$\text{time}(F) = t_{\text{comp}}(F, S) + t_{\text{impl}}(F, S)$$

#### Epistemic Status

Definitional. The decomposition of feature time into comprehension + implementation is a partition — together they cover the full duration, and the boundary is defined by [Definition IV.7](#comprehension-time).

#### Discussion

**Implementation time is what most metrics measure.** Cycle time, velocity, lines-per-hour — these track implementation. But [Derived IV.9](#dual-optimization) shows that optimizing implementation time alone is insufficient; comprehension time often dominates, especially under turnover.

**Under AI-assisted development, implementation time approaches zero for well-specified features.** This is the regime where [Result IV.4](#specification-bound) becomes binding — the implementation is fast, but the specification (which is part of comprehension) is the bottleneck.

#### Working Notes

- The clean decomposition time(F) = t_comp + t_impl assumes these are sequential. In practice they overlap (exploratory implementation as part of comprehension). The decomposition is still useful as an accounting identity, but measurements will be approximate.
- Should this definition explicitly reference [Derived I.16](#action-selection)? Implementation is the phase where the agent is primarily acting rather than observing — high action rate, lower exploration.

*(Descended from TST D-03.)*


<a id="dual-optimization"></a>

### Derived IV.9: *Dual Optimization*

A principled implementation decision minimizes both comprehension time and implementation time for future features, weighted by how many future features are expected.

#### Formal Expression

*[Derived (dual-optimization, from temporal-optimality + software-scope)]*

For implementation choice $C$ of the current feature, the time-optimal choice minimizes total median-predicted future time:

$$C^* = \operatorname{argmin}_{C} \left[ t_0(C) + \hat{n}_{\text{future}} \cdot \left( t_{\text{comp}}(F_{\text{typical}} \mid C) + t_{\text{impl}}(F_{\text{typical}} \mid C) \right) \right]$$

where $t_0(C)$ is the immediate cost of choice $C$, and $\hat{n}_{\text{future}}$ is the median prediction from [Derived IV.5](#change-expectation-baseline).

This follows from [Postulate I.1](#temporal-optimality) (minimize total time) applied to the lifecycle cost structure of [Scope IV.1](#software-scope) (future costs dominate), with the feature time decomposition from [Definition IV.7](#comprehension-time) and [Definition IV.8](#implementation-time).

##### The turnover multiplier

*[Derived (Conditional on turnover rate)]*

When $k$ distinct agents (human developers or AI instances) will each need to comprehend the code:

$$\text{total comprehension cost} \approx t_{\text{comp}} \times k$$

where $k = (1 + r) \times s$ for team size $s$ and turnover rate $r$ over the relevant horizon. With 100% AI context turnover, $k$ equals the number of sessions that touch the relevant code. Comprehension cost compounds per-reader; implementation cost does not.

#### Epistemic Status

*Conditional* on [Postulate I.1](#temporal-optimality) and [Derived IV.5](#change-expectation-baseline). The derivation is straightforward: if you accept that total time should be minimized (postulate) and that future feature count is predicted by the baseline (derived), then the dual optimization follows by applying the postulate to the decomposed cost structure. The turnover multiplier follows from the observation that comprehension is per-reader while implementation (of a specific feature) is per-feature.

The quantitative form inherits the assumptions of [Derived IV.5](#change-expectation-baseline): median prediction (not expectation — the mean is undefined for Pareto($\alpha = 1$)), uniform feature rate. The median-case optimization is conservative: the true expected future cost is *larger* than the median prediction (in fact, unbounded), so if anything this underestimates the case for investment.

#### Discussion

**When comprehension and implementation conflict.** Sometimes they pull in opposite directions:
- Abstraction can speed implementation but slow comprehension (indirection cost)
- Explicit code can speed comprehension but slow implementation (more code to write)
- DRY principles can reduce implementation sites but increase comprehension indirection

The resolution depends on $\hat{n}_{\text{future}}$ and the turnover rate. Under high turnover (especially 100% context turnover per AI instance), comprehension cost dominates — bias toward comprehensibility. Code that a fresh agent can understand in minutes is worth more than code that saves implementation time.

**Practical implications for AI-maintained code.** When $k$ is very large (many AI sessions touching the code), the comprehension term dominates overwhelmingly. This is not a style preference — it is the mathematical consequence of the turnover multiplier. Explicit code, linear control flow, local comprehensibility, and intent-revealing names are temporal optimizations.

#### Working Notes

- The "typical future feature" $F_{\text{typical}}$ is an idealization. Real futures have a distribution of feature types, and the optimal choice $C^\ast$ may depend on which features are more likely. [Derived IV.21](#principled-decision-integration) addresses this with the full probabilistic formulation. This simpler form is the single-feature-type approximation.
- TST's original T-05 includes a rich discussion of the AI turnover problem (redundant implementations, inconsistent patterns, half-completed features abandoned at context limit). These are real failure modes but they're consequences of high comprehension cost, not independent claims. They belong in worked examples or the Section V treatment of AI agents, not here.
- The turnover multiplier assumes each reader pays the full comprehension cost independently. In practice, good documentation and code structure can amortize comprehension across readers (each reader benefits from the last reader's improvements). This is the [Discussion IV.11](#code-quality-as-observation-infrastructure) feedback loop — but it's not formalized yet.
- Connection to [Formulation I.11](#information-bottleneck): the turnover multiplier means that for AI-maintained code, the IB tradeoff should favor retention (high $\beta$) — keep the model detailed and explicit, because the cost of re-deriving compressed information is paid by every future session.

*(Descended from TST T-05.)*


<a id="change-investment"></a>

### Derived IV.10: *Change Investment*

Accept higher initial implementation cost when the amortized savings across expected future changes exceed the upfront cost. This is the pairwise decision rule derived from [Derived IV.9](#dual-optimization).

#### Formal Expression

*[Derived (change-investment, from dual-optimization)]*

For two implementation choices $C_1, C_2$ of the current feature, where $C_1$ costs more now but saves time per future feature:

$$\text{Choose } C_1 \text{ when: } t_0(C_1) - t_0(C_2) \lt \hat{n}_{\text{future}} \times \left[\bar{t}(F \mid C_2) - \bar{t}(F \mid C_1)\right]$$

where $\bar{t}(F \mid C) = t_{\text{comp}}(F \mid C) + t_{\text{impl}}(F \mid C)$ is the per-feature time under choice $C$, and $\hat{n}_{\text{future}}$ is the median prediction from [Derived IV.5](#change-expectation-baseline).

Equivalently: accept $X$ extra minutes now to save $Y$ minutes per future change when $X \lt \hat{n}_{\text{future}} \times Y$.

#### Epistemic Status

*Derived* from [Derived IV.9](#dual-optimization). The threshold form is the pairwise comparison obtained by requiring $C_1$ to have lower total median-predicted time than $C_2$ in the dual-optimization objective. It inherits the assumptions of [Derived IV.5](#change-expectation-baseline) (median prediction — not expectation, since the mean is undefined — and uniform feature rate) and [Derived IV.9](#dual-optimization) (single typical future feature approximation).

The **compound effects** discussed below are structurally motivated but not formally derived within ACT. They connect to the persistence condition ([Result I.24](#persistence-condition)) but the formal link has not been established.

#### Discussion

**The threshold as everyday heuristic.** The investment threshold is simple enough to apply in real time: a file modified 20 times in git history suggests $\hat{n}_{\text{future}} \approx 20$. Spending 5 extra minutes to save 15 seconds per future interaction is justified ($5 \lt 20 \times 0.25$). The threshold transforms "clean code" from aesthetic preference to temporal optimization with measurable inputs.

**Compound effects.** Implementation choices affect not just future feature time but also the cost of future implementation *choices*. Principled early choices make future principled choices easier (lower comprehension cost → better decisions); rushed early choices make future principled choices harder (higher comprehension cost → more pressure to rush). This creates positive and negative feedback loops that amplify over time. In ACT terms, this is the agent's actions at time $t$ modifying the environment's properties for time $t+1$ — the standard adaptive feedback loop applied to code quality. The connection to [Result I.24](#persistence-condition) is suggestive: if code quality degrades faster than the team can restore it ($\rho \gt \mathcal{T} \times \Vert\delta_{\text{critical}}\Vert$), the codebase enters a regime of accelerating decay. But this analogy has not been formalized.

#### Working Notes

- The near-zero cost observation from TST T-06 ("principled implementation often requires nearly identical time as quick implementation") is empirically plausible but not derived. If true, it means the threshold is almost always satisfied — even small $\hat{n}_{\text{future}}$ justifies principled choices when the upfront cost difference is near zero. This would be worth establishing empirically but is not an ACT claim.
- The compound effects / virtuous-vicious cycle is listed in WORKBENCH.md as an ungrounded claim. The connection to persistence condition dynamics is the most promising formalization path: model code quality as a state variable subject to the mismatch ODE, with each implementation choice either reducing or increasing the effective disturbance rate $\rho$. But this requires defining "code quality" as an ACT quantity, which [Discussion IV.11](#code-quality-as-observation-infrastructure) is meant to address.
- TST T-06's AI-specific guidance (computational advantages in temporal optimization) belongs in Section V, not here. The core mathematical claim is agent-general.
- This segment overlaps substantially with [Derived IV.9](#dual-optimization). The threshold form here adds the concrete decision rule; the compound effects discussion adds the feedback loop observation. If these don't justify a separate segment, this could fold into [Derived IV.9](#dual-optimization) as a corollary and discussion extension.

*(Descended from TST T-06.)*


<a id="code-quality-as-observation-infrastructure"></a>

### Discussion + Hypothesis IV.11: *Code quality $\to U_o \to \eta^\ast \to \mathcal{T}$*

*Segment `code-quality-as-observation-infrastructure` has not yet been written.*


> **\[GAP\]** Developer tempo as $\mathcal T_{\text{obs}}$ + $\mathcal T_{\text{explore}}$ + $\mathcal T_{\text{probe}}$


<a id="conceptual-alignment"></a>

### Hypothesis IV.12: *Conceptual Alignment*

Comprehension time is inversely related to the alignment between code structure and the current domain model. When code mirrors the domain, the agent's $M_t$ construction is cheaper.

#### Formal Expression

*[Hypothesis (conceptual-alignment)]*

$$t_{\text{comp}}(F, S) \propto \frac{1}{\text{alignment}(S, D)}$$

where $\text{alignment}(S, D)$ measures the structural correspondence between codebase $S$ and the current domain model $D$:
- Directory/module boundaries matching domain boundaries
- Names using current domain vocabulary
- Code relationships mirroring domain relationships
- Abstraction levels corresponding to domain concept hierarchies

##### Corollary: Realignment as Feature

*[Derived (realignment-as-feature, from change-investment + conceptual-alignment)]*

When domain understanding evolves from $D_0$ to $D_1$, code written for $D_0$ accumulates a comprehension cost against $D_1$. By the [Derived IV.10](#change-investment) threshold, realignment is justified when:

$$T_{\text{align}} \lt \hat{n}_{\text{future}} \times \Delta t_{\text{comp}}$$

where $\Delta t_{\text{comp}}$ is the per-feature comprehension savings from alignment. Realignment is a feature with measurable ROI, not cleanup.

#### Epistemic Status

*Hypothesis.* The qualitative claim (better alignment → faster comprehension) is nearly tautological — code that matches how the agent thinks about the domain is easier to understand. But the *functional form* (inverse proportionality) is not derived from ACT. The relationship could be logarithmic (diminishing returns from alignment), threshold-based (alignment matters only below a minimum), or dependent on agent type (human vs AI may have different alignment sensitivities). ACT does not currently predict the functional form.

The realignment corollary is *derived* from [Derived IV.10](#change-investment) — it is simply the investment threshold applied to alignment changes. Its epistemic status inherits from both the investment threshold (conditional) and the alignment hypothesis (discussion-grade); the weaker link governs.

#### Discussion

**Alignment as observation channel quality.** In ACT terms, code structure is part of the agent's observation channel — it determines how efficiently the agent can extract the information needed to construct $M_t$. Well-aligned code delivers domain-relevant information in an organized form that matches the agent's needs. Misaligned code forces the agent to perform an additional mental translation (mapping between code vocabulary and domain vocabulary) on every observation. This translation cost is paid per comprehension event, making it subject to the turnover multiplier in [Derived IV.9](#dual-optimization).

**The dual comprehension cost.** Comprehension isn't just understanding the code — it's understanding the code, the domain, and the *mapping between them*. When alignment is high, the mapping is trivial (code names = domain names, code structure = domain structure). When alignment is low, the mapping itself becomes a cognitive task.

**The startup pivot case.** After a significant domain model shift, the accumulated misalignment can dominate comprehension cost. A codebase still using "friends" and "posts" when the product has pivoted to "teammates" and "documents" forces translation on every interaction. The realignment corollary says: treat the rename/restructure as a feature, calculate its ROI, and prioritize it accordingly.

#### Working Notes

- The inverse proportionality may be too strong. If alignment is measured on a 0–1 scale, the claim says comprehension time goes to infinity as alignment approaches zero — but in practice, completely misaligned code is still comprehensible, just slow. A more realistic form might be $t_{\text{comp}} = t_{\text{base}} + c / \text{alignment}$ (baseline plus alignment penalty) or some saturating function. The functional form is an empirical question.
- For AI agents with 100% context turnover, alignment may matter *more* than for humans, because the agent cannot build up a mental mapping over repeated interactions — it must reconstruct the code↔domain mapping fresh each session. Or it may matter *less*, because AI agents can process misaligned names faster than humans can. The direction is empirically uncertain.
- Connection to [Formulation I.11](#information-bottleneck): alignment might be formalized as the mutual information between code structure and domain structure, with misalignment as information that must be reconstructed rather than observed directly. This is speculative.
- TST T-07's "AI Inversion" observation (that well-aligned code teaches the domain, not just the implementation) is interesting but belongs in the Section V treatment of AI agents, not here.
- A **description-length or translation-cost framing** may be more natural than inverse alignment: comprehension time as a function of the translation cost between code structure and domain model ($t_{\text{comp}} \sim t_{\text{base}} + \text{cost}_{\text{translate}}(S, D)$). This avoids the $1/\text{alignment}$ singularity and connects more directly to information theory — the translation cost is the additional bits needed to decode code-structure observations through a misaligned mapping. Worth exploring if this segment gets promoted beyond discussion-grade.

*(Descended from TST T-07, C-07.1.)*


<a id="atomic-changeset"></a>

### Definition IV.13: *Atomic Changeset*

The complete diff between the codebase state before and after a feature is fully implemented, excluding generated artifacts.

#### Formal Expression

*[Definition (atomic-changeset)]*

For a feature $F$ ([Definition IV.3](#feature-definition)) applied to system $S$:

$$\text{changeset}(F) = S_{\text{after}} \ominus S_{\text{before}}$$

where $\ominus$ denotes the human- or agent-authored diff, excluding build artifacts, generated code, and automated reformatting.

"Codebase" crosses architectural boundaries — source code, schemas, configuration, infrastructure-as-code, tests, API contracts, deployment pipelines, monitoring configuration. If it must change to deliver the feature, it is part of the changeset.

**Size measures** (not mutually exclusive):
- Lines changed (added + deleted + modified)
- Files touched
- Modules affected

#### Epistemic Status

Definitional. The boundary choice (excluding generated artifacts) is a pragmatic convention, not derived — but it aligns with measuring the decisions the agent actually makes, which is what [Postulate I.1](#temporal-optimality) optimizes.

#### Discussion

The changeset is the observable trace of an implementation decision. It is to software what the action $a_t$ is to the general agent: the intervention in the environment. The size and structure of the changeset are what [Empirical IV.14](#changeset-size-principle) and [Derived IV.16](#change-proximity-principle) operate on.

#### Working Notes

- The exclusion of generated code is pragmatically motivated but theoretically interesting. Generated code represents an amplification of the agent's action — small input, large output. The *decision* cost is in the input; the *environment effect* is in the output. Should the changeset measure decision cost or environment effect? For temporal optimization of agent time, decision cost is right. For understanding system coupling, environment effect matters.
- The definition is implicitly per-feature, but features aren't always cleanly isolated in practice. Overlapping changesets, partial features, and incremental delivery blur the boundary. [Definition IV.3](#feature-definition) already notes this ambiguity.

*(Descended from TST D-04.)*


<a id="changeset-size-principle"></a>

### Empirical IV.14: *Changeset Size Principle*

Implementation time is proportional to the size of the atomic changeset.

#### Formal Expression

*[Empirical Claim (changeset-size-principle)]*

$$t_{\text{impl}}(F) \propto \lvert\text{changeset}(F)\rvert$$

where $\lvert\text{changeset}\rvert$ measures lines changed, files touched, or modules affected (see [Definition IV.13](#atomic-changeset)), excluding generated code.

##### Corollary: Comprehension Follows Changeset Size

*[Hypothesis (comprehension-follows-changeset)]*

$$t_{\text{comp}}(F) \propto \lvert\text{changeset}(F)\rvert$$

Understanding a feature that touched 20 files requires comprehending 20 contexts. This creates a double penalty for unnecessarily large changesets: both implementation time and comprehension time scale with size. Architecture that minimizes changeset size for typical features thus optimizes both dimensions of [Derived IV.9](#dual-optimization) simultaneously.

#### Epistemic Status

*Empirical.* The implementation-time proportionality is nearly tautological — more changes take more time. Its strength is as a simplifying assumption that enables quantitative reasoning: if you can estimate changeset size, you can estimate implementation time. The proportionality constant is codebase-specific and not derived.

The comprehension corollary is a *hypothesis* — weaker than the implementation claim. Comprehension cost depends not just on how many files are touched but on how complex each context is and how they relate to each other. The proportionality is a useful first approximation that likely holds across orders of magnitude (1 file vs 100 files) but may break down for fine comparisons (15 files vs 18 files). The [Derived IV.16](#change-proximity-principle) addresses the structure-dependent component that changeset size alone misses.

#### Discussion

**Architecture as temporal optimization.** The principle suggests a mechanism for why architecture matters: good architecture minimizes *future* changeset sizes, not current ones. A refactoring that touches 15 files now but ensures future features touch only 1 file (instead of 3) is justified when the savings exceed the cost — which is precisely the [Derived IV.10](#change-investment) threshold. This reframes architectural decisions as temporal investments, though the reduction to changeset size captures only one dimension of architectural quality.

**Connection to ACT.** The changeset is the observable trace of the agent's intervention in the environment. Changeset size is a proxy for the *scope* of the intervention. Larger interventions require more of the agent's time (both to plan and to execute), which is the implementation-time proportionality. They also require more of the *next* agent's time to comprehend (the corollary), which matters under the turnover multiplier in [Derived IV.9](#dual-optimization).

#### Working Notes

- The proportionality hides important structure. A 100-line change in one file and 10 one-line changes across 10 files have similar $\lvert\text{changeset}\rvert$ but very different costs. The proximity principle ([Derived IV.16](#change-proximity-principle)) captures this difference. The size principle is the first-order term; proximity is the correction.
- "Lines changed" vs "files touched" vs "modules affected" are different measures that may give different proportionality constants. Which measure best predicts time? This is an empirical question with practical implications for estimation and for evaluating architectures.
- The comprehension corollary assumes roughly equal per-context comprehension cost. In practice, some files are much harder to understand than others. A single change in a complex state machine may cost more comprehension time than changes across 10 simple CRUD endpoints. [Hypothesis IV.12](#conceptual-alignment) captures part of this — well-aligned modules are cheaper to comprehend per unit.

*(Descended from TST T-08, C-08.1.)*


<a id="change-distance"></a>

### Definition IV.15: *Change Distance*

The structural separation between two changes in a codebase, measured along a hierarchy of boundaries.

#### Formal Expression

*[Definition (change-distance)]*

For changes $c_i, c_j$ within a changeset, distance follows a boundary hierarchy:

$$d_{\text{lexical}} \lt d_{\text{file}} \lt d_{\text{module}} \lt d_{\text{service}}$$

where:
- **Lexical distance**: lines apart in the same file
- **File distance**: directory traversals between files
- **Module distance**: module or package boundaries crossed
- **Service distance**: network or process boundaries crossed

Each boundary crossing represents a qualitative increase in the cost of maintaining context across the two changes.

#### Epistemic Status

Definitional. The hierarchy is a structural observation about how software is organized, not a derived quantity. The claim that each boundary crossing increases cost is the separate claim in [Derived IV.16](#change-proximity-principle).

#### Discussion

Change distance operationalizes the intuition that "scattered changes are harder." The hierarchy reflects real discontinuities in the agent's observation channel: reading within a file is cheap (scrolling), reading across files requires navigation, reading across modules requires understanding interfaces, reading across services requires understanding protocols.

In ACT terms, each boundary crossing increases the cost of constructing the relevant portion of $M_t$ — the agent must load more context to hold both changes in working state simultaneously.

#### Working Notes

- The hierarchy is discrete but the underlying cost may not be. Two changes 5 lines apart and 500 lines apart are both "lexical distance" but have different cognitive costs. A continuous distance metric might be more accurate, but the discrete hierarchy captures the dominant effect (boundary crossings).
- Service distance may need refinement for modern architectures (monorepo with service boundaries vs. polyrepo, serverless functions, etc.). The underlying quantity is "how much context must be loaded to reason about both changes together."

*(Descended from TST D-05.)*


<a id="change-proximity-principle"></a>

### Derived IV.16: *Change Proximity Principle*

Given two implementations with identical changeset sizes, the one with changes closer together requires less time.

#### Formal Expression

*[Derived (change-proximity-principle, from comprehension-time + change-distance)]*

For a changeset, define proximity as:

$$\text{proximity}(\text{changeset}) = \frac{1}{\sum_{i,j} d(c_i, c_j)}$$

where $d$ follows the boundary hierarchy in [Definition IV.15](#change-distance). Then:

$$t_{\text{impl}} \propto \frac{1}{\text{proximity}(\text{changeset})}$$

at constant changeset size.

#### Epistemic Status

The qualitative claim is *derived*: comprehension time ([Definition IV.7](#comprehension-time)) includes the cost of constructing $M_t$ for the relevant code, and scattered changes require constructing $M_t$ across more contexts, each with a boundary-crossing cost from [Definition IV.15](#change-distance).

The quantitative form (inverse proportionality) is a *hypothesis*. The actual relationship between distance and cost is not derived — it could be linear, logarithmic, or dependent on the type of boundaries crossed. The exponential hypothesis is separated into [Hypothesis IV.17](#exponential-cognitive-load).

*Conditional* on the change-distance hierarchy reflecting real cognitive costs, which is plausible but not formally grounded.

#### Discussion

**Proximity predicts architectural preferences.** The principle is consistent with the persistence of certain patterns:
- Modules that group commonly co-changing code (maximize proximity)
- Layered architectures that localize changes to specific layers
- Domain boundaries that contain related changes ([Hypothesis IV.12](#conceptual-alignment))

These patterns minimize the distance term for typical future features. Whether proximity minimization is the actual mechanism driving their adoption (versus convention, tooling constraints, or other forces) is an empirical question — but the structural alignment is suggestive.

**The size-proximity decomposition.** Together with [Empirical IV.14](#changeset-size-principle), this gives a two-factor model of implementation cost: *how much* changes (size) and *how spread out* the changes are (proximity). Size is the first-order term; proximity is the structure-dependent correction. A good architecture minimizes both: small changesets with concentrated changes.

#### Working Notes

- The pairwise sum $\sum_{i,j} d(c_i, c_j)$ treats all pairs equally. In practice, some pairs matter more (changes that must be understood together to make sense) and some matter less (independent changes that happen to be in the same commit). A weighted version would be more accurate but harder to compute.
- TST's Der-09.1 shows how this interacts with [Derived IV.10](#change-investment): restructuring to improve proximity is an investment decision with the same threshold form. The cost is the restructuring effort; the savings are per-feature proximity improvements across $\hat{n}_{\text{future}}$ future features.
- The principle is about the agent's *experienced* cost, which depends on the agent's tooling and navigation capabilities. An IDE with good "jump to definition" reduces effective file distance; AI agents that can hold more context may have different distance sensitivities than humans. The principle holds qualitatively (boundaries have nonzero cost) but the distance hierarchy's quantitative weights are agent-dependent.

*(Descended from TST T-09.)*


<a id="exponential-cognitive-load"></a>

### Hypothesis IV.17: *Exponential Cognitive Load*

If context-switching compounds multiplicatively, implementation time grows exponentially with the number of boundary crossings (discontinuities) in a changeset.

#### Formal Expression

*[Hypothesis (exponential-cognitive-load)]*

$$t_{\text{actual}} = t_{\text{baseline}} \times k^{\text{discontinuities}}$$

where $k \gt 1$ is the compounding factor per context switch.

Even modest values of $k$ (1.1 to 1.2) create substantial differences when compounded across many discontinuities.

#### Epistemic Status

*Hypothesis.* TST states this carefully as a hypothesis requiring validation, and that caution is warranted. The actual relationship may be:
- Linear ($k = 1$ with additive cost per switch)
- Sub-exponential (diminishing marginal cost of additional switches)
- Exponential (as hypothesized)
- Dependent on the *structure* of dependencies between scattered changes

ACT's [Derived I.23](#deliberation-cost) framework suggests a refinement: the functional form likely depends on the dependency structure of the scattered changes, not on the count of discontinuities alone. Independent changes across many files may cost linearly (each context switch is independent). Interacting changes across many files — where understanding the change in file A requires understanding the change in file B which requires understanding file C — may cost exponentially because the agent must hold multiple contexts simultaneously to reason about their interactions. The distinction is between parallel context-loading (linear) and nested context-dependency (potentially exponential).

#### Discussion

**Why the hypothesis persists.** Despite lacking formal derivation, exponential cognitive load explains a robust observation: developers strongly prefer consolidated changes, and scattered changes feel *disproportionately* difficult. The hypothesis provides a quantitative framework for this observation. Whether the mechanism is truly exponential or merely superlinear, the qualitative implication is the same: reducing discontinuities has increasing marginal returns.

**Connection to ACT's deliberation cost.** The [Derived I.23](#deliberation-cost) framework formalizes the cost of reasoning before acting. Context switches during implementation are a form of deliberation cost — the agent must reason about how changes in one location affect another. When the changes are independent, this deliberation is parallelizable (each change can be understood locally). When they interact, deliberation becomes sequential and potentially recursive: understanding change A requires understanding change B, which may require understanding change C. This recursive dependency structure is what could produce genuine exponential scaling.

#### Working Notes

- The key open question is empirical: does the cost scale with discontinuity *count* (as stated) or with discontinuity *dependency structure* (as ACT's deliberation-cost framework suggests)? These make different predictions: the count model says 10 independent scattered changes are as hard as 10 interdependent ones; the structure model says the independent case is much easier. This is testable.
- For AI agents, context-switch cost may have a different profile than for humans. LLMs can hold large contexts but may have difficulty with *deep* reasoning chains. This suggests the structure-dependent model (where chain depth matters more than context breadth) may be especially relevant for AI agents.
- If the exponential form holds, it has strong architectural implications: any design that reduces the number of boundary crossings for typical features is worth disproportionate investment. This amplifies [Derived IV.10](#change-investment) far beyond the linear model.
- TST's notation $k^{\text{discontinuities}}$ uses "discontinuities" loosely. A more precise formulation would count boundary crossings weighted by boundary type ([Definition IV.15](#change-distance)), or better yet, measure the depth of the dependency chain among the scattered changes.

*(Descended from TST H-09.1.)*


<a id="system-coupling"></a>

### Definition IV.18: *System Coupling*

The probability that a change to one module will require a change to another.

#### Formal Expression

*[Definition (system-coupling)]*

$$\text{coupling}(m_i, m_j) = P(\text{change}(m_j) \mid \text{change}(m_i))$$

where $\text{change}(m)$ means module $m$ is part of the [Definition IV.13](#atomic-changeset) for some feature.

This is an empirical quantity — it is estimated from observed co-change patterns, not from static analysis of the code structure.

#### Epistemic Status

Definitional. The conditional probability is a standard quantity. Its value for a given system is empirical, estimated from git history or similar records of co-change.

#### Discussion

Coupling defined this way captures the *actual* change propagation in a system, which may differ from what static dependency analysis predicts. Two modules with no compile-time dependency can still be highly coupled if features routinely require changing both. Conversely, a module that imports another heavily may show low coupling if the interface is stable.

In ACT terms, coupling is a property of the environment's causal structure as experienced by the agent: changing module $i$ (an intervention) tends to require changing module $j$ (a consequence). This is genuinely causal, not just correlational — the agent performs $do(\text{change}(m_i))$ and observes whether $m_j$ must also change. Git history provides the interventional data ([Hypothesis IV.24](#causal-discovery-from-git)).

#### Working Notes

- The definition is asymmetric: $P(\text{change}(m_j) \mid \text{change}(m_i))$ need not equal $P(\text{change}(m_i) \mid \text{change}(m_j))$. This asymmetry is informative — it reveals directional dependency.
- Coupling is feature-type-dependent. A module pair might be tightly coupled for UI features and uncoupled for backend features. The unconditional estimate from git history is an average over the historical feature distribution, which may not represent future features. This connects to the uniform-feature-rate assumption in [Derived IV.5](#change-expectation-baseline).
- The interventional interpretation is stronger than correlational. If two modules always change in the same commit, that could be coupling OR could be convention (developer habit of bundling). Distinguishing requires looking at *whether the feature required both changes* vs. *whether the developer chose to include both*. Atomic commits help; large PRs hurt.

*(Descended from TST D-06.)*


<a id="system-coherence"></a>

### Definition IV.19: *System Coherence*

The expected proximity of changes within a module.

#### Formal Expression

*[Definition (system-coherence)]*

$$\text{coherence}(m) = E[\text{proximity}(\text{changes within } m)]$$

where proximity is the inverse of [Definition IV.15](#change-distance):

$$\text{proximity}(c_i, c_j) = \frac{1}{d(c_i, c_j)}$$

A highly coherent module concentrates its changes — when a feature touches the module, the changes tend to be close together. A low-coherence module scatters changes across its internal structure.

#### Epistemic Status

Definitional. Coherence is the dual of [Definition IV.18](#system-coupling): coupling measures change propagation *between* modules, coherence measures change locality *within* modules. Both are empirical, estimated from observed change patterns.

#### Discussion

Coherence captures whether a module's internal organization matches its usage patterns. A module with high coherence groups code that changes together, so features that touch the module require understanding only a localized portion. This reduces the $M_t$ construction cost ([Definition IV.7](#comprehension-time)) for the agent.

The classic "high cohesion, low coupling" principle in software engineering is the conjunction of high [Definition IV.19](#system-coherence) and low [Definition IV.18](#system-coupling). ACT provides the *why*: high coherence reduces per-feature comprehension cost (fewer context switches), low coupling reduces per-feature changeset size (fewer modules touched). Both minimize total time under [Postulate I.1](#temporal-optimality).

#### Working Notes

- The proximity measure in the definition uses [Definition IV.15](#change-distance), which is a discrete hierarchy. This means coherence is somewhat coarse-grained. A module where all changes happen in the same file has high coherence; one where they span many files has low coherence. Finer-grained measurement would require a continuous distance metric.
- Coherence is relative to the feature distribution. A module might appear coherent for historical features but incoherent for future ones if the product direction changes. This is the same feature-distribution sensitivity as [Definition IV.18](#system-coupling).

*(Descended from TST D-07.)*


<a id="coherence-coupling-measurement"></a>

### Measurement IV.20: *Coherence-Coupling Measurement*

Software coherence and coupling can be measured from git history, enabling empirical evaluation of architectural quality.

#### Formal Expression

*[Measurement (coherence-coupling-measurement)]*

An architectural quality metric can be constructed as:

$$Q = \frac{\sum_i \text{coherence}(m_i)}{\sum_{i \neq j} \text{coupling}(m_i, m_j)}$$

where [Definition IV.19](#system-coherence) and [Definition IV.18](#system-coupling) are estimated from historical commits:

1. **Coherence**: average proximity of changes within each module over observed commits
2. **Coupling**: frequency of commits touching multiple modules, yielding conditional probability estimates
3. **Quality ratio**: coherence / coupling (handling edge cases where coupling approaches zero)

#### Epistemic Status

*Empirical.* The measurement procedure is well-defined given sufficient git history. The claim that the ratio captures "architectural quality" is an empirical hypothesis — it assumes that the high-coherence/low-coupling ideal (the classic software engineering principle) is the correct optimization target. Under ACT, this is motivated by [Postulate I.1](#temporal-optimality): high coherence reduces per-feature comprehension cost, low coupling reduces per-feature changeset size. But the ratio form ($Q$) is one possible aggregation; others (weighted sum, geometric mean, per-module scores) might predict temporal outcomes better.

**Requirements**: sufficient historical data for statistical significance, stable module boundaries (or boundary-evolution tracking), and a representative feature distribution in the observed history.

#### Discussion

**From opinion to measurement.** The measurement transforms architectural discussions from aesthetic judgment to empirical observation: "this refactoring increased our coherence-coupling ratio from 2.3 to 4.1 based on the last 100 commits." This is the measurement-driven approach that ACT enables in the software domain — the theory provides the quantities to measure and the reason they matter ([Postulate I.1](#temporal-optimality)), and git provides the interventional data to estimate them.

**Feature-distribution sensitivity.** Both coherence and coupling are estimated from historical features. If the future feature distribution differs from the past, the estimates may not predict future architectural performance. This is the same sensitivity as [Derived IV.5](#change-expectation-baseline)'s uniform-feature-rate assumption.

#### Working Notes

- The ratio form privileges balance. A system with coherence = 100 and coupling = 50 gets $Q = 2$; a system with coherence = 10 and coupling = 5 also gets $Q = 2$. But the first system has higher absolute coupling, which means more cross-module work per feature. An additive form ($\alpha \cdot \text{coherence} - \beta \cdot \text{coupling}$) might be more useful for optimization, since it distinguishes absolute levels.
- Git commit granularity matters. If developers make large commits bundling unrelated changes, coupling estimates are inflated. If they make tiny commits splitting related changes, coherence estimates may be deflated. Atomic commits (one feature per commit) are the ideal data source, matching the [Definition IV.13](#atomic-changeset) definition.
- This measurement is a candidate for [Hypothesis IV.24](#causal-discovery-from-git) — the co-change data is interventional (each commit is a developer's intervention), not merely observational. This gives the coupling estimates causal rather than merely correlational interpretation, which is stronger than typical software metrics.

*(Descended from TST T-10.)*


<a id="principled-decision-integration"></a>

### Derived IV.21: *Principled Decision Integration*

The optimal implementation choice minimizes total expected time across all probable future features, integrating all temporal factors simultaneously.

#### Formal Expression

*[Derived (principled-decision-integration, from temporal-optimality)]*

For implementation choices $\mathbf{C}$ for the current feature:

$$C^* = \operatorname{argmin}_{C \in \mathbf{C}} \; E[T \mid C]$$

where total expected time given choice $C$ is:

$$E[T \mid C] = t_0(C) + \sum_{i} P(F_i) \cdot \left[ t_{\text{comp}}(F_i \mid C) + t_{\text{impl}}(F_i \mid C) \right]$$

This is the general form of [Derived IV.9](#dual-optimization). Where dual-optimization uses a single "typical future feature" $F_{\text{typical}}$ with count $\hat n_{\text{future}}$, this integrates over the full distribution of possible future features $F_i$ with their individual probabilities $P(F_i)$.

Substituting the proportional relationships from [Hypothesis IV.12](#conceptual-alignment), [Empirical IV.14](#changeset-size-principle), and [Derived IV.16](#change-proximity-principle):

$$E[T \mid C] = t_0(C) + \sum_{i} P(F_i) \cdot \left[ \frac{\alpha \cdot h(\text{disc}(F_i \mid C))}{\text{alignment}(C)} + \beta \cdot \lvert\text{cs}(F_i \mid C)\rvert \cdot g(\text{prox}(F_i \mid C)) \right]$$

where $\alpha, \beta$ are empirical proportionality constants, $h$ and $g$ encode the (possibly exponential, per [Hypothesis IV.17](#exponential-cognitive-load)) cost relationships, and $\text{disc}$, $\text{cs}$, $\text{prox}$ are the discontinuity count, changeset size, and proximity for feature $F_i$ under choice $C$.

#### Epistemic Status

*Derived* from [Postulate I.1](#temporal-optimality) — the optimization is the direct application of the least-time postulate to the full cost structure. *Conditional* on the proportional relationships from [Hypothesis IV.12](#conceptual-alignment) (hypothesis), [Empirical IV.14](#changeset-size-principle) (empirical), and [Derived IV.16](#change-proximity-principle) (conditional). The expanded form inherits the weakest epistemic status of its inputs: the alignment term is discussion-grade, the proximity cost function is uncertain in form. The integration structure itself is exact; the terms being integrated are approximate.

The full optimization is intractable in practice — it requires knowing the probability distribution of all future features and the exact impact of current decisions on future costs. The practical value is as a decision *framework* that structures the tradeoff space, not as a computable optimum.

#### Discussion

**Relationship to dual-optimization.** This is the general case; [Derived IV.9](#dual-optimization) is the single-feature-type approximation. The approximation is good when future features are roughly homogeneous. When different feature types have very different cost profiles (e.g., a system that handles both UI changes and data pipeline changes), the full integration reveals tradeoffs the approximation misses — an architecture optimal for one feature type may be suboptimal for another.

**Dominant-factor analysis.** Perfect integration is impossible, but recognizing which factors dominate is usually tractable. Under high turnover, $t_{\text{comp}}$ dominates $t_{\text{impl}}$ (the [Derived IV.9](#dual-optimization) turnover multiplier). For a well-aligned codebase, alignment contributes little and changeset size dominates. For a highly modular system, proximity is less of an issue than for a monolith. Identifying the dominant factor reduces the full optimization to a simpler one.

#### Working Notes

- TST T-11 includes a rich expanded form with empirical constants $\alpha$ and $\beta$ that convert proportionalities to equalities. These constants are codebase-specific and not derived. In practice, relative comparisons (architecture A vs B) may not need absolute constants — the proportionalities suffice for ordering.
- The summation over $P(F_i)$ assumes the feature distribution is known or estimable. In practice, this is where the agent's $M_t$ does the real work — predicting not just *how many* future features ([Derived IV.5](#change-expectation-baseline)) but *what kind*. The quality of this prediction is bounded by the agent's model quality, connecting back to [Definition I.12](#model-sufficiency).
- This segment might be better positioned as a discussion/synthesis rather than a standalone derived claim, since it mostly assembles previously stated results into a composite objective. Its independent contribution is the explicit per-feature probability weighting, which dual-optimization elides.

*(Descended from TST T-11.)*


<a id="system-availability"></a>

### Definition IV.22: *System Availability*

The fraction of time a system serves its users successfully.

#### Formal Expression

*[Definition (system-availability)]*

$$A = \frac{\text{MTTF}}{\text{MTTF} + \text{MTTR}}$$

where MTTF = Mean Time To Failure, MTTR = Mean Time To Recovery.

#### Epistemic Status

Definitional. This is the standard reliability engineering definition. ACT does not add to or modify it; it is imported as a prerequisite for [Scope IV.23](#continuous-operation), which extends the temporal optimization framework to account for operational failures.

#### Discussion

Availability connects to ACT through [Scope IV.23](#continuous-operation): a non-operational system has effectively infinite implementation time for any feature. From the user's perspective, downtime is lost time. The temporal optimality postulate therefore applies to operational time as well as development time.

*(Descended from TST D-08.)*


<a id="continuous-operation"></a>

### Scope IV.23: *Continuous Operation*

For systems that must operate while evolving, temporal optimization includes the expected cost of failures and recovery.

#### Formal Expression

*[Scope (continuous-operation, extending software-scope)]*

For systems where $P(\text{perturbation}) \gt 0$ and $\text{required availability} \gt A_{\text{threshold}}$, the effective time includes operational cost:

$$T_{\text{effective}} = T_{\text{implementation}} + P(\text{failure}) \times T_{\text{recovery}}$$

Under [Postulate I.1](#temporal-optimality), this means minimizing the sum, not just the first term.

##### The infinite-time observation

A non-operational system has effectively infinite implementation time for any feature from the user's perspective. Therefore, minimizing recovery time is not separate from minimizing development time — it is part of the same optimization.

#### Epistemic Status

The scope extension is *definitional* — we choose to include operational time in the optimization. The consequence (effective time includes $P(\text{failure}) \times T_{\text{recovery}}$) follows from [Postulate I.1](#temporal-optimality) applied to the extended scope. The "infinite-time" observation is an asymptotic argument: as availability drops, effective feature delivery time grows without bound.

#### Discussion

**Defensive vs. fault-tolerant.** Different design strategies optimize different terms:

- **Defensive programming**: high $T_{\text{implementation}}$ (validation, error handling), aims for low $P(\text{failure})$, often high $T_{\text{recovery}}$ when failures occur (complex systems fail complexly)
- **Fault-tolerant design** (e.g., "let it crash"): lower $T_{\text{implementation}}$, accepts higher $P(\text{failure})$, minimizes $T_{\text{recovery}}$ (fast restart, isolated failures)

When $T_{\text{recovery}} \ll T_{\text{defensive}}$, accepting and quickly recovering from failures is time-optimal. Supervision trees, circuit breakers, bulkheads, and health checks are all mechanisms that minimize $T_{\text{recovery}}$ — their widespread adoption is consistent with the temporal-optimality prediction, though the model captures only the time dimension of the design tradeoff.

**Perturbation types.** Systems face impulse perturbations (traffic spikes, deploys), sustained stress (degraded dependencies, memory leaks), and cascading failures (propagation through coupled components). Low [Definition IV.18](#system-coupling) limits cascade scope; fast recovery minimizes $T_{\text{recovery}}$; graceful degradation maintains partial [Definition IV.22](#system-availability).

**Connection to ACT.** Perturbations are environmental disturbances ($\rho$) in the operational domain. The persistence condition ([Result I.24](#persistence-condition)) applies: the team's operational tempo must exceed the disturbance rate relative to acceptable mismatch. A team that cannot recover faster than failures accumulate is in the unmaintainability regime.

#### Working Notes

- The $P(\text{failure}) \times T_{\text{recovery}}$ term is an expected-value approximation. In practice, failure distributions are heavy-tailed — rare catastrophic failures may dominate the expectation. A risk-sensitive formulation (e.g., CVaR) might be more appropriate for critical systems, but ACT's temporal-optimality postulate as stated uses expected time.
- The scope extension is mild — it just says "count operational time too." But it has strong implications: development decisions that seem suboptimal under pure implementation time (T-08) become optimal when operational time is included. This is why the scope narrowing matters.
- TST T-12's perturbation taxonomy (impulse, stress, cascade) maps to ACT's disturbance characterization in the persistence condition. Impulse = spike in $\rho$; stress = sustained elevated $\rho$; cascade = $\rho$ amplified by coupling. The persistence condition handles all three through the $\rho$ term, but the qualitative distinction is useful for practitioners.

*(Descended from TST T-12, D-08.)*


<a id="causal-discovery-from-git"></a>

### Hypothesis IV.24: *Git as interventional data*

*Segment `causal-discovery-from-git` has not yet been written.*


> **\[GAP\]** Software persistence: the unmaintainability threshold formalized



---

## V. Logogenic Agents

*Extending the arc: AI agents operating on code are ACT agents whose domain is software, creating a recursive structure — ACT theory $\to$ software domain $\to$ agents that embody ACT. This is where the 100% context turnover problem, $M_t$ preservation, and the cognitive loop connect the theory back to the systems being built with it. Note: LLM-based agents are goal-conditioned — their epistemic processing depends on $G_t$ — so the clean factorization from directed separation ([Derived II.12](#directed-separation)) is an approximation for this class. Section I's $M_t$-side quantities remain well-defined; the sequential orient cascade becomes approximate. Whether Section V requires a first-class coupled $f_M(M_t, G_t, e_\tau)$ extension or can work with the approximation is an open question.*


<a id="ai-agent-as-act-agent"></a>

### Definition V.1: *AI agent as actuated agent*

*Segment `ai-agent-as-act-agent` has not yet been written.*


<a id="context-turnover"></a>

### Observation V.2: *100% $M_t$ reset per session*

*Segment `context-turnover` has not yet been written.*


<a id="m-preservation"></a>

### Discussion V.3: *External memory as persistent $M_t$*

*Segment `m-preservation` has not yet been written.*


> **\[GAP\]** Language-specific orient cascade (what's specific to logogenic agents?)


> **\[GAP\]** Measuring $M_t$ quality, $\Sigma_t$ quality, and tempo in AI agents


> **\[GAP\]** ACT-grounded experiential training environments


> **\[GAP\]** Self-referential closure: ACT agent on ACT codebase



---

## VI. Logozoetic Agents

*Future work. Scope narrowing from logogenic agents to agents with temporal continuity, sovereignty over intent, and theory of mind — agents whose persistence is morally weighted. The formal machinery for this section (if any beyond Section V's) is not yet identified. See `LEXICON.md` for the conceptual groundwork.*


---

## Appendices: Details

*Supporting material: derivations, sketches, simulation results, and operationalization procedures backing the main theory claims.*


<a id="sector-condition-derivation"></a>

### Derivation A.1: *Sector Condition Stability — Lyapunov Derivation*

Complete Lyapunov derivations of bounded mismatch and adaptive reserve for the sector-condition results stated in [Result I.25](#sector-condition-stability).

#### Motivation

[Hypothesis I.22](#mismatch-dynamics) hypothesizes the linear ODE $d\Vert\delta\Vert/dt = -\mathcal{T}\Vert\delta\Vert + \rho$ as a first-order approximation. The linear form yields clean closed-form results but commits to a specific functional relationship between mismatch magnitude and correction rate. True correction dynamics are almost certainly nonlinear — exhibiting saturation at large mismatch, threshold effects near zero, and structural breakdown when the model class is exhausted.

A Lyapunov approach proves persistence and stability under much weaker assumptions: any correction dynamics satisfying qualitative monotonicity properties (the sector condition). The results below are strictly more general — the linear case is recovered where the sector bounds coincide.

#### Setup

Let $\delta(t) \in \mathbb{R}^n$ be the mismatch vector — the difference between the model's predictions and reality across $n$ observable dimensions. The vector treatment connects to per-dimension tempo analysis ([Result III.13](#per-dimension-persistence)).

The mismatch dynamics are:

*[Definition (Dynamics Setup)]*

$$\frac{d\delta}{dt} = -F(\mathcal{T}, \delta) + w(t)$$

where:

- $F(\mathcal{T}, \delta): \mathbb R_+ \times \mathbb{R}^n \to \mathbb{R}^n$ is the **correction function** — how the agent's adaptive process reduces mismatch. It maps to the same space as $\delta$ (so that the inner product $\delta^T F$ in the sector condition is well-defined). This subsumes the update gain $\eta^\ast$ ([Empirical I.19](#update-gain)), event rate $\nu$, and the structure of the update rule.
- $w(t)$ is the **disturbance** — new mismatch introduced by environmental change, with $\Vertw(t)\Vert \leq \rho$ (bounded disturbance rate).

The linear case from [Hypothesis I.22](#mismatch-dynamics) has $F(\mathcal{T}, \delta) = \mathcal{T} \cdot \delta$.

#### Assumptions on $F$

We require only qualitative properties, not a specific functional form:

##### (A1) Zero Correction at Zero Mismatch

*[Assumption A1]*

$$F(\mathcal{T}, 0) = 0$$

No correction is applied when the model perfectly matches reality.

##### (A2') Local Sector Condition

There exists a region $\mathcal B_R = \{\delta : \Vert\delta\Vert \leq R\}$ and $\alpha \gt 0$ such that (following the sector-condition framework of Lur'e[^lure1957]):

*[Assumption A2' (sector-condition)]*

$$\delta^T F(\mathcal{T}, \delta) \geq \alpha \Vert\delta\Vert^2 \quad \forall \delta \in \mathcal{B}_R$$

The correction function always points "inward" (reducing mismatch), and its magnitude is bounded below relative to $\Vert\delta\Vert^2$. The linear case has $\alpha = \mathcal{T}$. A saturating correction has $\alpha$ decreasing for large $\Vert\delta\Vert$. A threshold correction has $\alpha = 0$ for small $\Vert\delta\Vert$.

The local form allows the correction to break down outside $\mathcal B_R$ — the structural adaptation regime of [Result I.26](#structural-adaptation-necessity).

##### (A3) Tempo Monotonicity

For fixed $\delta$, $\delta^T F(\mathcal{T}, \delta)$ is monotone increasing in $\mathcal{T}$. Higher tempo means faster correction.

**Connection to ACT parameters.** The sector parameter $\alpha$ is determined by the adaptive tempo $\mathcal{T}$ ([Definition I.21](#adaptive-tempo)) and the structure of the correction function. In the linear case, $\alpha = \mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$. In nonlinear cases, $\alpha$ represents the *worst-case* correction efficiency within the valid region — the minimum ratio of correction power to mismatch magnitude. The radius $R$ represents the model class capacity: how large a mismatch can grow before the correction mechanism fails (i.e., before the sector condition ceases to hold), at which point structural adaptation ([Result I.26](#structural-adaptation-necessity)) becomes necessary.

#### Candidate Lyapunov Function

*[Definition (Lyapunov Candidate)]*

$$V(\delta) = \frac{1}{2}\Vert\delta\Vert^2$$

Positive definite, radially unbounded, continuously differentiable. Its level sets $V = c$ are spheres of radius $\sqrt{2c}$ in mismatch space.

#### Proposition A.1: Bounded Mismatch (Single Agent)

**Statement.** Under (A1), (A2'), (A3), with bounded disturbance $\Vertw(t)\Vert \leq \rho$, the mismatch $\delta(t)$ is **ultimately bounded**: there exists $R^\ast \gt 0$ such that $\Vert\delta(t)\Vert \leq R^\ast$ for all sufficiently large $t$, provided $R^\ast \lt R$ (the ultimately bounded region fits within the sector-condition region).

**Proof.**

Compute $\dot{V}$ along trajectories:

*[Derived (Proof Step)]*

$$\dot{V} = \delta^T \dot{\delta} = \delta^T[-F(\mathcal{T}, \delta) + w(t)]$$

*[Derived (Proof Step)]*

$$= -\delta^T F(\mathcal{T}, \delta) + \delta^T w(t)$$

By (A2'): $\delta^T F(\mathcal{T}, \delta) \geq \alpha\Vert\delta\Vert^2$

By Cauchy-Schwarz: $\delta^T w(t) \leq \Vert\delta\Vert \cdot \Vertw(t)\Vert \leq \rho\Vert\delta\Vert$

Therefore:

*[Derived (Proof Step)]*

$$\dot{V} \leq -\alpha\Vert\delta\Vert^2 + \rho\Vert\delta\Vert = -\Vert\delta\Vert(\alpha\Vert\delta\Vert - \rho)$$

$\dot{V} \lt 0$ whenever $\Vert\delta\Vert \gt \rho/\alpha$.

Define $R^\ast = \rho/\alpha$. Outside the ball $\mathcal B_{R^\ast}$, the Lyapunov function is strictly decreasing, so trajectories are driven inward. Any trajectory entering $\mathcal B_{R^\ast}$ remains in a neighborhood of it (with possible oscillation at the boundary due to the disturbance).

The agent persists iff $R^\ast \lt R$, i.e., iff $\rho/\alpha \lt R$, i.e., iff $\alpha \gt \rho/R$. $\square$

**Interpretation.** The ultimately bounded region has radius $R^\ast = \rho/\alpha$. In the linear case, $\alpha = \mathcal{T}$, recovering [Result I.24](#persistence-condition)'s steady-state result $R^\ast = \rho/\mathcal{T}$ exactly. But Proposition A.1 holds for *any* correction function satisfying the sector condition, not just the linear one.

**The persistence threshold, generalized.** The agent persists (mismatch remains bounded within the model class capacity) iff $\rho/\alpha \lt R$. If the correction function breaks down (A2' fails) before $R^\ast$ is reached, the agent may diverge. This IS [Result I.26](#structural-adaptation-necessity)'s trigger: when $\rho/\alpha \gt R$ (the environment demands more correction than the model class can provide), parametric adaptation fails and structural change is required.

#### Proposition A.2: Stability Margin (Adaptive Reserve)

**Statement.** Under the conditions of A.1, the agent can tolerate a sudden increase in disturbance rate of:

*[Derived (adaptive-reserve)]*

$$\Delta\rho^* = \alpha R - \rho$$

without mismatch diverging (where $R$ is the radius of the sector-condition region from A2'). Beyond this, $R^\ast$ exceeds $R$ and the correction function may fail.

**Proof.** After a shock, the new disturbance rate is $\rho + \Delta\rho$. The new ultimately bounded radius is $(\rho + \Delta\rho)/\alpha$. This remains within the valid region iff $(\rho + \Delta\rho)/\alpha \leq R$, i.e., $\Delta\rho \leq \alpha R - \rho$. $\square$

**Interpretation.** $\Delta\rho^\ast$ is the agent's **adaptive reserve** — how much additional environmental volatility it can absorb before its model breaks down. This is a single number characterizing an agent's robustness to shock:

- An agent operating well below capacity ($\rho \ll \alpha R$) has a large reserve — it is **robust**.
- An agent near its limit ($\rho \approx \alpha R$) has a small reserve — it is **fragile**.

| Domain | Large $\Delta\rho^\ast$ (robust) | Small $\Delta\rho^\ast$ (fragile) |
|--------|-------------------------------|-------------------------------|
| Control | Kalman filter on slow target | Same filter on erratic target |
| Biology | Organism in stable niche | Same organism under climate change |
| Organization | Well-capitalized firm, stable market | Startup in volatile market |
| Military | Force with operational depth | Force at culmination point |

#### Summary of Results

| Result | What it proves | Assumptions | Linear case recovery |
|--------|---------------|-------------|---------------------|
| **A.1** (Bounded Mismatch) | $R^\ast = \rho/\alpha$ | (A1), (A2'), bounded $\rho$ | $\alpha = \mathcal{T}$ gives $R^\ast = \rho/\mathcal{T}$ |
| **A.2** (Stability Margin) | $\Delta\rho^\ast = \alpha R - \rho$ | Same as A.1 | $R \to \infty$ for linear (always stable if $\mathcal{T} \gt 0$) |

#### Epistemic Status

The setup and assumptions are *definitions* — they specify what we mean by "correction function" and "disturbance." Propositions A.1 and A.2 are *exact* — they follow from the assumptions via standard Lyapunov theory (Khalil 2002[^khalil2002], Chapters 4 and 9). The assumptions themselves (sector condition, bounded disturbance) are *empirical claims* about the qualitative behavior of real correction dynamics. The sector-condition framework originates with Lur'e (1957); the Lyapunov stability results are standard. The application to adaptive agents under the ACT framework is new but the mathematics is not.

#### Discussion

**Key value.** The persistence threshold and adaptive reserve are no longer contingent on the linear hypothesis in [Hypothesis I.22](#mismatch-dynamics). They hold for any correction dynamics satisfying the sector condition — a mild qualitative assumption that says "correction points inward with at least baseline efficiency $\alpha$." This is a significant epistemic upgrade: from *hypothesis-dependent* to *robust under qualitative assumptions*.

**What the proofs do NOT illuminate.** (1) Quantitative steady-state values — Lyapunov gives *bounds*, not exact values; the linear analysis remains necessary for quantitative predictions. (2) Convergence rates — standard Lyapunov tells you stable/unstable, not how fast. (3) Optimal gain structure — [Empirical I.19](#update-gain) comes from estimation theory, not stability theory. (4) Model sufficiency — the [Formulation I.11](#information-bottleneck) framework is information-theoretic, complementary to but independent of stability analysis.

**The bounded-disturbance assumption.** Proposition A.1 requires $\Vertw(t)\Vert \leq \rho$ — a finite upper bound on disturbance magnitude. This excludes heavy-tailed environmental shocks (financial crises, ecological catastrophes, strategic surprise) where $\Vertw(t)\Vert$ can exceed any finite bound with non-negligible probability. For such environments, stochastic Lyapunov methods (input-to-state stability in probability, martingale-based stability) would be needed. The bounded case gives worst-case guarantees for the typical regime; extreme tail events are better understood as triggers for structural adaptation ([Result I.26](#structural-adaptation-necessity)) rather than disturbances to be absorbed parametrically.

#### Working Notes

- The adversarial extension (Prop A.3, coupled agents) and effects spiral (Cor A.3.1) are in [Derived III.10](#adversarial-destabilization). The multi-timescale sketch (A.4) is in [Sketch A.3](#multi-timescale-stability).
- The vector treatment of $\delta(t) \in \mathbb{R}^n$ connects directly to per-dimension tempo analysis ([Result III.13](#per-dimension-persistence)). Each dimension can have different effective $\alpha_k$ values, and the weakest dimension determines overall persistence — a tensor generalization of the scalar results here.
- A global sector condition (A2 without the local restriction to $\mathcal B_R$) would give global stability, making $\Delta\rho^\ast$ infinite — the agent could absorb any finite disturbance shock. But this requires the correction function to work perfectly at arbitrary mismatch magnitudes, which is unrealistic for any finite model class. The local form (A2') is the honest one.

---

[^khalil2002]: Khalil, H. K. (2002). *Nonlinear Systems* (3rd ed.). Prentice Hall. Chapters 4 (Lyapunov stability), 9 (input-output stability). [^lure1957]: Lur'e, A. I. (1957). *Some Nonlinear Problems in the Theory of Automatic Control*. Original sector-condition framework for absolute stability.

*(Descended from TFT Appendix A, Props A.1–A.2.)*


<a id="recursive-update-derivation"></a>

### Derivation A.2: *Recursive Update — Uniqueness Derivation*

Derivation showing that $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ is the *unique* update form consistent with directed time, partial observability, and state completeness. Not merely one option, but the only one.

#### Setup

We work within ACT's scope ([Scope I.5](#scope-condition)): an agent coupled to an environment $\Omega$ through observation and action channels, with residual uncertainty.

**Universe of information at event time $\tau$.** The following information exists (in the broadest ontological sense) at the moment event $e_\tau$ occurs:

| Information | Description |
|-------------|-------------|
| $\Omega_\tau$ | The environment state |
| $\mathcal{C}_{\tau^-}$ | The complete interaction history ([Definition I.9](#chronica)) up to (but not including) $e_\tau$ |
| $\{M_{\tau'}\}_{\tau' \leq \tau^-}$ | The agent's prior internal states, culminating in $M_{\tau^-}$ |
| $e_\tau$ | The current event (observation arriving or action completing) |
| $\{e_{\tau'}\}_{\tau' \gt \tau}$ | Future events (not yet occurred) |

The question: of these, which can the update $M_{\tau^+}$ depend on?

#### The Three Constraints

**Constraint 1 — Arrow of time ([Postulate I.7](#causal-structure) postulate).** Events are temporally ordered and this ordering is irreversible. An update occurring at time $\tau$ cannot depend on events that have not yet occurred:

$$M_{\tau^+} \text{ cannot depend on } \{e_{\tau'}\}_{\tau' \gt \tau}$$

This is a physical constraint — the most primitive one. In a classical universe, information from the future is simply not available. Even if the agent can *predict* future events, those predictions are part of $M_{\tau^-}$ (they are internal computations, not future information).

**Constraint 2 — Partial observability ([Scope I.5](#scope-condition)).** The agent cannot access $\Omega_\tau$ directly. Its only interface with the environment is through the event $e_\tau$, which is a lossy function of $\Omega_\tau$ (via [Definition I.3](#observation-function)):

$$M_{\tau^+} \text{ cannot depend on } \Omega_\tau \text{ except through } e_\tau$$

This is a scope constraint. If the agent could access $\Omega$ directly, the residual uncertainty condition in [Scope I.5](#scope-condition) would be trivially violable.

**Constraint 3 — State completeness ([Formulation I.10](#agent-model)).** $M_{\tau^-}$ is the agent's *complete* internal state just before event $e_\tau$. There is no information about the agent's past that is available to the update mechanism but not encoded in $M_{\tau^-}$:

$$M_{\tau^+} \text{ cannot depend on } \mathcal{C}_{\tau^-} \text{ or } \{M_{\tau'}\}_{\tau' \lt \tau^-} \text{ except through } M_{\tau^-}$$

This constraint does the most interesting work and deserves careful examination (see Discussion below).

#### The Derivation

**Result (Recursive Update Uniqueness).** Under Constraints 1–3, the model update at event time $\tau$ must have the form

$$M_{\tau^+} = f(M_{\tau^-}, e_\tau)$$

for some function $f: \mathcal{M} \times \mathcal{E} \to \mathcal{M}$. No other update form is consistent with the three constraints.

**Derivation.** Consider the most general possible update. The updated state $M_{\tau^+}$ is a function of *all accessible information*:

$$M_{\tau^+} = F(\text{accessible information at } \tau)$$

We characterize the accessible information by eliminating what is not accessible.

**(i) Eliminate future events.** By C1 (arrow of time), $\{e_{\tau'}\}_{\tau' \gt \tau}$ is not accessible.

After this elimination, the candidate dependency set is:
$$\{\Omega_\tau,\; \mathcal{C}_{\tau^-},\; \{M_{\tau'}\}_{\tau' \leq \tau^-},\; e_\tau\}$$

**(ii) Eliminate direct environment access.** By C2 (partial observability), the agent cannot access $\Omega_\tau$ except through the event $e_\tau$. Any information from $\Omega_\tau$ that reaches the agent does so through $e_\tau$ — already in the dependency set.

After this elimination:
$$\{\mathcal{C}_{\tau^-},\; \{M_{\tau'}\}_{\tau' \leq \tau^-},\; e_\tau\}$$

**(iii) Reduce past information to $M_{\tau^-}$.** By C3 (state completeness), $M_{\tau^-}$ is the agent's complete internal state. Every element of $\mathcal{C}_{\tau^-}$ and every prior model state $M_{\tau'}$ ($\tau' \lt \tau^-$) that could influence the update can do so *only through* its effect on $M_{\tau^-}$. The agent's internal state evolves through a sequence of updates; the cumulative effect of all prior events is exactly $M_{\tau^-}$. The raw events that produced this state are no longer separately available — they were "consumed" by the update mechanism and their information (to the extent it was retained) is now encoded in $M_{\tau^-}$.

Could the agent maintain a separate log of raw events outside of $M$? It could — but that log *is part of $M$*. Whatever information the agent retains in any form — model parameters, cached data, raw event buffers, metadata — is by definition part of its complete internal state $M_{\tau^-}$. If something is available to the update mechanism and not in $M_{\tau^-}$, then $M_{\tau^-}$ was not the complete state — contradicting C3.

After this elimination:
$$\{M_{\tau^-},\; e_\tau\}$$

Therefore:
$$M_{\tau^+} = F(M_{\tau^-}, e_\tau) \equiv f(M_{\tau^-}, e_\tau)$$

This is the unique form: no information beyond $(M_{\tau^-}, e_\tau)$ is accessible under the three constraints, so no update form depending on anything else is realizable. $\square$

**Corollary (Between-events dynamics).** Between events, no new event $e$ arrives. The same argument applies with $e_\tau$ removed from the accessible set:

$$\frac{dM}{d\tau} = g(M_\tau)$$

The agent's internal evolution between events (prediction, decay, internal simulation) depends only on the current state. $\square$

**Corollary (Serial special case).** When observations and actions alternate at a uniform rate on a single channel, each event $e_t$ is the pair $(o_t, a_{t-1})$. The update becomes:

$$M_t = f(M_{t-1}, o_t, a_{t-1})$$

This is the familiar discrete-time form. $\square$

#### Information-Set Formalization

For readers who prefer a measure-theoretic framing:

The agent's **information set** at time $\tau$ is the sigma-algebra $\mathcal{I}_\tau^{agent}$ — the collection of events (in the probability-theoretic sense) about which the agent can condition its update.

- **C1** restricts $\mathcal{I}_\tau^{agent} \subseteq \sigma(\{e_{\tau'} : \tau' \leq \tau\} \cup \{\Omega_\tau\} \cup \{M_{\tau'} : \tau' \leq \tau^-\})$ — no future information.
- **C2** further restricts: $\sigma(\Omega_\tau) \setminus \sigma(e_\tau)$ is not in $\mathcal{I}_\tau^{agent}$ — the agent cannot condition on aspects of $\Omega_\tau$ not captured by $e_\tau$.
- **C3** further restricts: $\sigma(\{e_{\tau'} : \tau' \lt \tau\} \cup \{M_{\tau'} : \tau' \lt \tau^-\}) \subseteq \sigma(M_{\tau^-})$ from the agent's perspective.

After all three restrictions: $\mathcal{I}_\tau^{agent} = \sigma(M_{\tau^-}, e_\tau)$.

By the Doob–Dynkin lemma, any $\sigma(M_{\tau^-}, e_\tau)$-measurable random variable is a (Borel) function of $(M_{\tau^-}, e_\tau)$. Therefore $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ for some measurable $f$. $\square$

#### Attempts to Break the Result

Before trusting the proof, seven counterexample attacks:

##### Attack 1: Simultaneous events

Two events arrive at exactly the same time: $e_\tau^{(1)}$ and $e_\tau^{(2)}$. The update has three arguments: $f(M_{\tau^-}, e_\tau^{(1)}, e_\tau^{(2)})$.

**Verdict:** Not deep — [Formulation I.14](#event-driven-dynamics) defines events as atomic. If we allow bundled events, the form holds with $e_\tau$ as a set. Reveals that "event" needs careful definition, but the form is preserved.

##### Attack 2: Continuous environmental influence

An agent embedded in a physical system experiences continuous forces (gravity, temperature, electromagnetic fields). These aren't "events" in [Formulation I.14](#event-driven-dynamics)'s sense; they're continuous signals. The true dynamics would be $dM/d\tau = g(M_\tau, o(\tau))$ where $o(\tau)$ is a continuous observation stream.

**Verdict:** Genuine limitation of the event-driven formulation. The between-events corollary $dM/d\tau = g(M_\tau)$ holds only when the agent is truly isolated between events. For continuous coupling, the analogous result is the general state-space representation $\dot{M} = g(M, u)$ from control theory — arrived at by the same three constraints. The event-driven version is a special case for digital/sampled systems.

##### Attack 3: The C3 circularity

C3 defines $M$ as the agent's complete internal state. Any apparent counterexample is dissolved by expanding $M$. Consider: an agent has a "model" (neural net weights) and a "replay buffer" (stored raw events). C3 says $M = (\text{weights}, \text{buffer})$. The model space is just larger than you thought.

**Verdict:** The deepest objection. The proof essentially: (1) Define $M$ to be everything the agent has. (2) Observe the update can only use what the agent has. (3) Therefore $f(M_{\tau^-}, e_\tau)$. The real content is the *analytical commitment*: by defining $M$ as complete, we commit to Markovian analysis, which then makes [Definition I.12](#model-sufficiency) the right quality metric. See Epistemic Status below.

##### Attack 4: Shared state between agents

Agents A and B share a common memory bank (shared database). The clean resolution is the multi-agent framework: the shared memory is part of the *composite* system's state, and each agent's interaction with it is mediated by events (reads and writes). Not a true counterexample but highlights that C3 requires careful delineation of agent boundaries.

##### Attack 5: External randomness not in $e_\tau$

Hardware thermal noise used in the update. The stochastic case $M_{\tau^+} \sim P(\cdot \mid M_{\tau^-}, e_\tau)$ is a special case of $f$ where $f$ is a randomized function. The *form* — dependence on exactly $(M_{\tau^-}, e_\tau)$ — is preserved. The result statement should explicitly allow stochastic $f$.

##### Attack 6: Time-dependent updates

Could $f$ depend on the timestamp $\tau$ itself? Yes — consistently. The event $e_\tau$ in [Formulation I.14](#event-driven-dynamics) carries a timestamp: $e_\tau = (\text{type}, \text{channel}, \text{payload}, \tau)$. So time-dependence enters through $e_\tau$. Alternatively, the agent may maintain an internal clock as part of $M_{\tau^-}$. Either way, $f(M_{\tau^-}, e_\tau)$ accommodates time-dependence.

##### Attack 7: Agents that store full history

An agent with $M_{\tau^-} \supseteq \mathcal{C}_{\tau^-}$ is entirely consistent. The model space $\mathcal{M}$ is simply large enough to include the raw history. The [Formulation I.11](#information-bottleneck) argues compression is *wise* — but the recursive update form holds regardless of compression level.

#### Epistemic Status

The result is correct but partly definitional. The three constraints have different epistemic characters:

| Constraint | Character | Can it be violated? |
|------------|-----------|---------------------|
| C1 (arrow of time) | Physical law | Not in a classical universe |
| C2 (partial observability) | Scope definition | Only by leaving ACT's scope |
| C3 (state completeness) | Analytical commitment | Not without redefining $M$ |

C1 and C2 do genuine eliminative work — they rule out update forms that depend on future events or on raw $\Omega$. These are non-trivial constraints.

C3 is a definitional commitment that produces the Markov structure. It cannot be "violated" because any violation is absorbed by expanding $M$. This is not a weakness — it's the nature of the claim. The result says: *the Markovian analysis is the only one consistent with C1 + C2 + the definition of $M$ as complete*. The alternative — an update that depends on something outside $M$ — is not "wrong" but rather means $M$ was misspecified.

**What the result says:** C1 eliminates a physically impossible class of updates (future-dependent). C2 eliminates a scope-excluded class ($\Omega$-dependent). After (1) and (2), the *only remaining question* is how the past enters: through the full history $\mathcal{C}_{\tau^-}$ or through a compressed state $M_{\tau^-}$. C3 says the agent *has* a complete state, and whatever that state is, it's all the agent has. The Markov form follows.

**What the result does NOT say:** That $M$ must be a lossy compression (the agent could store full history). That the Markov property is "natural" or "optimal" (it's a consequence of how $M$ is defined). That continuous-coupling systems are event-driven (the event framework is one abstraction; $\dot{M} = g(M, u)$ is the more general one, arrived at by the same three constraints).

#### Discussion

**Recursion as a consequence of completeness.** The recursive form is not an assumption bolted on — it follows from the definition of $M_t$ as complete. The sufficiency of the recursive form is precisely what [Definition I.12](#model-sufficiency) measures: when $S(M_t) = 1$, the recursive update loses nothing.

**What this opens.** The proof yields the *form*. It immediately invites the follow-up questions that the rest of the theory addresses: What should $f$ preserve? → [Formulation I.11](#information-bottleneck) and [Definition I.12](#model-sufficiency). How should $f$ weight new information? → [Empirical I.19](#update-gain). When is $\mathcal{M}$ itself inadequate? → [Result I.26](#structural-adaptation-necessity).

#### Working Notes

- C3's definitional character is a feature, not a bug — but it must be stated honestly. The result is not "the update must be Markovian" but rather "the Markovian analysis is the *only* consistent one, given the modeling commitment of [Formulation I.10](#agent-model)." These sound the same but have different epistemic status.
- The continuous-coupling generalization (Attack 2) deserves a proper note somewhere: $\dot{M} = g(M, u)$ is the more general form, with event-driven updates as a special case. The three constraints produce the same argument structure in both cases.
- The information-set formalization (Doob-Dynkin) provides the cleanest technical proof. It should probably be considered the primary proof path, with the elimination argument as the more intuitive exposition.

*(Descended from TFT Appendix: Recursive Update Uniqueness Derivation.)*


<a id="multi-timescale-stability"></a>

### Sketch A.3: *Multi-Timescale Stability*

When adaptive processes operate at $N$ nested timescales, composite stability requires each level to be stable given its slower levels, with sufficient timescale separation between adjacent pairs.

#### Formal Expression

*[Formulation (multi-timescale-stability sketch)]*

##### The General $N$-Timescale System

The temporal nesting in [Derived I.27](#temporal-nesting) creates a coupled multi-timescale system with $N$ levels. Singular perturbation theory provides tools to analyze such systems. Define a hierarchy of state variables:

*[Definition (State Hierarchy)]*

$$x^{(1)}, \; x^{(2)}, \; \ldots, \; x^{(N)}$$

where $x^{(1)}$ is the fastest (e.g., mismatch at the reactive/parametric level) and $x^{(N)}$ is the slowest (e.g., architectural or meta-structural state). The coupled dynamics:

*[Formulation (N-Timescale Dynamics)]*

$$\dot{x}^{(k)} = \frac{1}{\epsilon_k} \, G^{(k)}\!\left(x^{(1)}, \ldots, x^{(N)}\right) + w^{(k)}(t)$$

where $\epsilon_1 \ll \epsilon_2 \ll \cdots \ll \epsilon_N$ encode the timescale separation and each $G^{(k)}$ may depend on the states at all levels.

##### The Two-Timescale Special Case

The simplest nontrivial instance has $N = 2$:

- Fast state $x^{(1)} = \delta$ (mismatch under parametric adaptation)
- Slow state $x^{(2)} = \mathcal{M}$ (model class, changing on a structural timescale)

$$\dot{x}^{(1)} = -F(\mathcal{T}, x^{(1)}; x^{(2)}) + w(t) \quad \text{(fast: parametric adaptation)}$$

$$\dot{x}^{(2)} = \epsilon \, G(x^{(1)}, x^{(2)}) \quad \text{(slow: structural adaptation)}$$

where $\epsilon \ll 1$ reflects the timescale separation and $F$ depends on $x^{(2)}$ (the correction function is determined by the current model class).

##### Sketch of Approach (General Case)

The standard singular perturbation result (Tikhonov's theorem, generalized) applies layer by layer: if level $k$ is stable for each fixed configuration of the slower levels $k+1, \ldots, N$ (each level has a stable attractor given the levels above it), and each successive slow manifold is itself stable, then the composite $N$-level system is stable.

[Derived I.27](#temporal-nesting)'s convergence constraint $\nu_{n+1} \ll \nu_n$ is the condition ensuring sufficient timescale separation at each boundary — i.e., $\epsilon_k / \epsilon_{k+1} \ll 1$ for each $k$. When this separation is violated between any adjacent pair, the faster level's transients contaminate the slower level's dynamics, potentially destabilizing the composite system.

#### Epistemic Status

This is a *sketch*, not a complete result. The framework and approach are presented as a guide for future development. The claim that timescale separation ensures composite stability is a standard result in singular perturbation theory; the application to ACT's nested adaptive levels is new but follows the standard pattern.

Making it rigorous requires specifying the dynamics $G^{(k)}$ for levels deeper than parametric adaptation. [Result I.26](#structural-adaptation-necessity) gives the *trigger condition* for structural change but not the *dynamics* of how change at deeper levels proceeds. Specifying these would require theories of how agents search over model classes, modify their own architecture, or restructure their adaptive mechanisms — open problems in RL (architecture search, meta-learning), biology (evolutionary dynamics), and organizational theory (institutional change).

#### Discussion

**The convergence constraint as stability condition.** The sketch suggests that [Derived I.27](#temporal-nesting)'s convergence constraint is not merely a heuristic but a formal condition for composite stability across arbitrarily many timescales. This connects the empirical observation (don't let deeper-level changes happen too fast) to a stability-theoretic foundation.

**Applicability to LLM systems.** LLMs involve many parallel adaptive processes — pretraining (slowest), fine-tuning, LoRA-style adaptation, in-context learning, retrieval/RAG updates, tool-use feedback, and within-generation attention dynamics — without clean boundaries between "parametric" and "structural." The $N$-timescale framework accommodates this naturally: each mechanism operates at its characteristic rate, and the stability analysis requires only that adjacent timescales be sufficiently separated, regardless of how many levels exist or how they are labeled.

#### Working Notes

- The key open problem: formalizing $G^{(k)}$ for structural adaptation levels. The two-timescale case (parametric + structural) is the tractable starting point.
- The connection to [Proposed schema II.20](#strategy-persistence-schema) is direct: strategy operates at its own timescale, and strategy persistence requires timescale separation from the faster epistemic updates and the slower objective revisions.
- When timescale separation breaks down between organizational levels, the result is "micromanagement" — the organizational analog of control-theoretic instability from gain mismatch. This observation connects to the hierarchical topology analysis in the multi-agent coupling material.

*(Descended from TFT Appendix A, Prop A.4 sketch.)*


<a id="linear-ode-approximation"></a>

### Detail A.4: *Pedagogical linear mismatch ODE*

*Segment `linear-ode-approximation` has not yet been written.*


<a id="simulation-results"></a>

### Detail A.5: *Simulation Results*

Six simulation variants validated, refined, and extended the analytical predictions from Section I, forcing regime splits and discovering scaling laws that the analytical derivations left ambiguous.

#### Overview

The track-b simulation program tested Section I's analytical predictions about mismatch dynamics, adversarial coupling, observation noise, correction function robustness, and anisotropic persistence. The simulations modeled discrete-time mismatch dynamics as AR(1) processes with five correction functions (linear, saturating, threshold/dead-zone, sigmoid, structural breakdown), sweeping parameter spaces across gain, disturbance rate, coupling strength, observation noise, and dimensional structure.

The simulations were theory-shaping, not merely confirmatory. In particular:

- The adversarial tempo exponent turned out to be regime-dependent (deterministic drift vs. stochastic noise, coupling-dominant vs. non-coupling-dominant), forcing a regime split that the mismatch ODE left ambiguous.
- Observation noise was found to gate the adversarial advantage, partially recoverable by optimal gain -- a finding that had no analytical treatment before the simulations.
- The scalar persistence condition was shown to overestimate adaptive capacity by 72% in anisotropic systems, motivating the per-dimension persistence condition.

#### Variant Summary

| Variant | Tested | Key Finding | Theory Impact | Promoted Segment |
|---------|--------|-------------|---------------|------------------|
| A | Deterministic drift coupling; coupling-dominance sweep | Exponent $b \to 2.0$ in coupling-dominant limit (confirmed at 1.999) | Corollary 11.2 is exact under deterministic drift dominance | [Observation III.11](#adversarial-exponent-regimes) |
| B | Drift-noise interpolation across correction functions | Smooth transition between drift ($b = 2.0$) and noise ($b = 1.5$) regimes; coupling dominance is the key qualifier, not drift vs. noise per se | Confirmed that the coupling-dominant condition is quantitatively load-bearing | [Observation III.11](#adversarial-exponent-regimes) |
| C | Exponent vs. gain ($\eta$) in stochastic model | Exponent drops toward 0.5 as $\eta \to 0$ (away from coupling dominance at fixed $q_\text{base}$); discrete AR(1) exponent never exceeds 1.5 | Stochastic noise coupling has asymptotic exponent 1.5, not 2.0 -- a fundamental model distinction | [Observation III.11](#adversarial-exponent-regimes) |
| D | Exponent vs. base noise ($q_\text{base}$) at fixed $\eta$ | Continuous ODE exponent $\to$ 2.0, discrete AR(1) exponent $\to$ 1.5, as $q_\text{base} \to 0$ | Definitively separated the two asymptotes; simulations match discrete AR(1) prediction exactly | [Observation III.11](#adversarial-exponent-regimes) |
| E | Observation noise; optimal gain validation | Observation noise collapses adversarial exponent from $\sim 1.0$ to $\sim 0.2$; Riccati-optimal gain restores it to $\sim 0.4$; 52% mismatch reduction at moderate noise | Observation quality gates tempo advantage; optimal gain ([Empirical I.19](#update-gain)) empirically validated | [Observation III.12](#observation-gates-advantage) |
| F | Multi-dimensional anisotropic correction; targeted adversarial attack | Per-dimension theory exact to 4 significant figures; scalar tempo overestimates by 72%; targeted attack amplifies advantage by 17% | Scalar persistence condition is necessary but not sufficient; per-dimension condition required | [Result III.13](#per-dimension-persistence) |
| Hafez bridge | Bi-predictability $P$ vs. ACT mismatch in adversarial and non-adversarial settings | $P$ measures coupling architecture (scale-invariant); mismatch measures coupling performance; $P$ is blind to adversarial dynamics | $P$ and ACT mismatch are complementary diagnostics; $H_b$ (agent opacity) has no direct ACT analog -- potential gap for multi-agent work | -- |

#### Methodology

**Discrete mismatch dynamics.** The environment follows a random walk $x_{t+1} = x_t + w_t$ with $w_t \sim N(0, q^2)$. The agent corrects via $\hat x_{t+1} = \hat x_t + \eta \cdot g(\delta_t)$, yielding the AR(1) mismatch process $\delta_{t+1} = (1 - \eta) \cdot \delta_t + w_t$ for linear $g$. This is the discrete-time analog of the mismatch ODE $d\Vert\delta\Vert/dt = -\mathcal{T} \cdot \Vert\delta\Vert + \rho$ from [Hypothesis I.22](#mismatch-dynamics).

**Parameter sweeps.** Each variant swept its key parameter(s) across 7--20 values. Monte Carlo: 200 independent trials per parameter point, 10,000--20,000 timesteps per trial, with 2,000--5,000 step burn-in for steady-state convergence. Fixed random seeds for reproducibility.

**Exponent fitting.** Adversarial exponents were estimated by fitting $\log(\Vert\delta_B\Vert / \Vert\delta_A\Vert) = a + b \cdot \log(\mathcal T_A / \mathcal T_B)$ via weighted least squares, with weights inversely proportional to variance of each point's log-estimate. 95% confidence intervals via bootstrap (1,000 samples).

**Correction functions.** Five functions $g: \mathbb{R} \to \mathbb{R}$ were tested, all satisfying $g(0) = 0$ and $g'(0) = 1$: linear ($g(\delta) = \delta$), saturating ($g(\delta) = \delta / (1 + \lvert\delta\rvert/R)$), threshold ($g(\delta) = \delta \cdot \mathbf{1}[\lvert\delta\rvert \gt \epsilon]$), sigmoid ($g(\delta) = R \cdot \tanh(\delta/R)$), and structural breakdown ($g(\delta) = \delta \cdot \mathbf{1}[\lvert\delta\rvert \lt R_\text{max}]$).

**Simulation code.** All code is in `scratch/track-b-nonlinear-sims/`. Initial simulations: `sim1_nonlinear_mismatch.py` (single-agent), `sim2_adversarial_coupling.py` (two-agent). Variant extensions: `variants/variant_ab_drift.py`, `variants/variant_cd_regimes.py`, `variants/variant_ef_extensions.py`, `variants/variant_hafez_bridge.py`. Detailed result write-ups: `variants/variant_ab_results.md`, `variants/variant_cd_results.md`, `variants/variant_ef_results.md`, `variants/variant_hafez_results.md`.

#### Key Findings

##### The adversarial exponent is regime-dependent

The mismatch ODE's $\rho$ parameter conflates two quantities: deterministic drift (persistent directional change) and stochastic noise scale (unpredictable fluctuations). These yield different steady-state scaling:

- **Deterministic drift, coupling-dominant:** $\Vert\delta\Vert_{ss} = \rho / \mathcal{T}$. Adversarial exponent $b \to 2.0$.
- **Stochastic noise, coupling-dominant:** $\Vert\delta\Vert_{ss} = \rho / \sqrt{\mathcal{T}}$ (from AR(1) stationary variance). Adversarial exponent $b \to 1.5$.
- **Non-coupling-dominant:** Exponent degrades smoothly toward 1.0 (deterministic) or 0.5 (stochastic) as base disturbance grows relative to adversarial coupling.

The original sim2 result ($b \approx 1.05$) was not a falsification of Corollary 11.2 but a measurement in the wrong regime -- stochastic noise coupling at moderate coupling dominance. Variants A--D systematically mapped the full regime space and identified the analytical root causes. See [Observation III.11](#adversarial-exponent-regimes) for the full treatment.

##### Observation noise gates adversarial advantage

Adding observation noise $\sigma_\text{obs}$ to the mismatch signal collapsed the adversarial exponent from $\sim 1.0$ to $\sim 0.2$ at $\sigma_\text{obs} = 10 \times q_\text{env}$ (fixed gain). The Riccati-optimal gain ([Empirical I.19](#update-gain)) partially restored the advantage to $\sim 0.4$, more than doubling it but not recovering the noise-free level. The optimal gain helps most in the moderate-noise regime, where it achieved a 52% mismatch reduction over fixed gain. See [Observation III.12](#observation-gates-advantage).

##### Per-dimension persistence is exact; scalar overestimates

In a 3-dimensional system with 5:1 gain variation across dimensions, the per-dimension AR(1) steady-state prediction matched simulation to 4 significant figures. The scalar persistence condition overestimated aggregate mismatch by 72%, because it averages across dimensions while the weak dimension dominates the $L_2$ norm. Isotropic gain allocation reduced overall mismatch by 13%; targeted adversarial attack on the weak dimension amplified the mismatch ratio by 17%. See [Result III.13](#per-dimension-persistence).

##### Nonlinear correction creates thresholds, not lower exponents

Under deterministic drift, saturating, sigmoid, and breakdown correction functions did not simply reduce the adversarial exponent. Instead, they produced catastrophic divergence when disturbance exceeded the correction capacity ($\rho \gt \mathcal{T} \cdot R$). This is the persistence threshold failure from [Result I.24](#persistence-condition), observed directly in simulation. The measured "exponents" above 3.0 for these functions were divergence artifacts, not meaningful scaling laws.

##### Hafez bridge: architecture vs. performance

Bi-predictability $P$ (Hafez et al.) measures the informational architecture of agent-environment coupling; ACT mismatch measures the operational performance. In adversarial settings, $P$ remained nearly constant ($\sim 0.268$) across a 10:1 range of opponent tempo, while the mismatch ratio varied from 0.54 to 5.95. $P$ is scale-invariant after z-score normalization, making it insensitive to adversarial dynamics. The two metrics are complementary: $P$ diagnoses whether the coupling structure is sound; mismatch predicts how well it performs.

#### Epistemic Status

*Empirical.* Simulation results are reproducible (code in `scratch/track-b-nonlinear-sims/`, fixed seeds, all results documented in variant write-ups). The key results -- regime-dependent exponents, observation noise gating, per-dimension exactness -- have been promoted to first-class segments ([Observation III.11](#adversarial-exponent-regimes), [Observation III.12](#observation-gates-advantage), [Result III.13](#per-dimension-persistence)) with their own epistemic assessments. This appendix serves as reference for the simulation program as a whole.

#### Discussion

**Internal validation, not external.** The simulations operate in the model's own terms: AR(1) processes with parameterized correction functions, Gaussian noise, and discrete-time dynamics. They validate the mathematical predictions within the model -- confirming that the analytical steady-state formulas, the exponent regimes, and the per-dimension theory are correct as statements about these stochastic processes. The gap between "the math predicts X within its own model" and "real agents exhibit X" remains an empirical question for each domain.

**What the simulations did not test.** The simulations did not test whether the AR(1) mismatch dynamics are a good model for any particular real-world adaptive system. They also did not test cross-dimensional coupling (off-diagonal correction), non-Gaussian disturbances, non-stationary parameters, or multi-agent composition dynamics. The interaction between observation noise and the deterministic-drift exponent regime ($b = 2.0$) was not tested -- Variant E used stochastic coupling only.

**Theory-shaping role.** The most important contribution of the simulations was not confirming predictions but forcing the theory to be more precise. The regime split in the adversarial exponent, the observation-noise gating mechanism, and the per-dimension bottleneck effect were all findings that the analytical derivations left ambiguous or unaddressed. The simulations narrowed the theory's claims from "the exponent is 2" to "the exponent is 2 under deterministic drift in the coupling-dominant regime, and 1.5 under stochastic noise in the coupling-dominant regime," which is a substantively different and more useful statement.



---

## Appendices: Operational Domains

*Operational-specific appendices and end-to-end domain instantiations validating the theory chain.*


<a id="operationalization"></a>

### Detail B.1: *Operationalization — Estimation Procedures*

Estimation recipes for core ACT quantities, bridging the measurement gap between formal objects and practical deployment.

#### Measurement Targets

| Quantity | Role in ACT | Typical unit | Minimum data needed |
|----------|-------------|--------------|---------------------|
| $U_M$ | Model uncertainty ([Empirical I.19](#update-gain)) | domain-specific variance/entropy | Predictive posterior or ensemble spread |
| $U_o$ | Observation uncertainty ([Empirical I.19](#update-gain)) | sensor variance/noise scale | Channel calibration or residual variance |
| $\rho(t)$ | Mismatch injection rate ([Hypothesis I.22](#mismatch-dynamics)) | surprise per time | Time-series of mismatch magnitudes |
| $\rho_{\text{delib}}$ | Local mismatch drift during pauses ([Derived I.23](#deliberation-cost)) | surprise per time | Deliberation windows with no corrective action |
| $\alpha$ | Lower correction efficiency bound ([Result I.25](#sector-condition-stability)) | inverse time | Vector mismatch trajectories + correction term |
| $R$ | Radius where local sector condition holds ([Result I.25](#sector-condition-stability)) | surprise magnitude | Same as $\alpha$, plus breakdown detection |
| $\Vert\delta_{\text{critical}}\Vert$ | Functional adequacy threshold ([Result I.24](#persistence-condition)) | surprise magnitude | Task-level performance curve vs mismatch |

#### Estimator Cookbook

##### Estimating $U_M$ and $U_o$

Use the most native uncertainty representation available in the domain:

| Domain | $U_M$ estimator | $U_o$ estimator |
| ------ | --------------- | --------------- |
| Kalman / linear Gaussian | Prior predictive variance $P_{t \vert t-1}$ | Measurement-noise variance $R_t$ (known or EM-estimated) |
| Conjugate Bayes | Posterior variance / inverse effective sample size | Likelihood variance (or precision inverse) |
| RL with ensembles | Across-head predictive variance $\operatorname{Var}_i[Q_i(s,a)]$ | TD-target noise variance over replay batches |
| Neural net regression | Ensemble or Laplace posterior variance | Aleatoric head output $\sigma^2(x)$ |
| PID / classical control | State-estimation covariance from observer | Sensor noise from calibration + residual PSD |

For the scalar gain heuristic ([Empirical I.19](#update-gain)), normalize to common units and compute:

*[Operational Definition]*

$$\hat{\eta}^*_t = \frac{\hat{U}_{M,t}}{\hat{U}_{M,t} + \hat{U}_{o,t}}$$

##### Estimating $\rho(t)$ and $\rho_{\text{delib}}$

Let $s_t = \Vert\delta_t\Vert$ in surprise units (e.g., negative log-likelihood residual scale).

Global mismatch injection rate:

*[Operational Definition]*

$$\hat{\rho}(t) = \left[\frac{s_{t+\Delta t} - s_t}{\Delta t} + \hat{\mathcal T}_t \, s_t\right]_+$$

where $[x]_+ = \max(x, 0)$ and $\hat{\mathcal T}$ evaluated at time $t$ is estimated adaptive tempo.

**Note on estimation sequencing.** This estimator requires $\hat{\mathcal T}_t$, estimated from $\hat{\nu}$ and $\hat{\eta}^\ast$. Estimate the gain and event rate first (from the agent's internal statistics and observation timing), then use these to extract $\rho$ from the mismatch trajectory. This sequential structure avoids circularity but introduces sensitivity: errors in $\hat{\mathcal T}$ propagate linearly into $\hat{\rho}$.

Local pause-window drift for [Derived I.23](#deliberation-cost):

*[Operational Definition]*

$$\hat{\rho}_{\text{delib}} = \operatorname*{median}_{w \in \mathcal{W}_{\text{pause}}} \frac{s_{w,\text{end}} - s_{w,\text{start}}}{\Delta\tau_w}$$

using windows where corrective action is suspended or effectively delayed.

##### Estimating $\alpha$ (sector lower bound)

[Derivation A.1](#sector-condition-derivation) uses $\delta^T F(\mathcal{T}, \delta) \geq \alpha \Vert\delta\Vert^2$ for $\Vert\delta\Vert \leq R$. Operationally:

1. Estimate $\dot{\delta}_t$ (finite differences or filtered derivative).
2. Compute $\widehat F_t = -\dot{\delta}_t + w_t$ where disturbance proxy $w_t$ is estimated from exogenous perturbation channels or residual balancing.
3. Form ratios $r_t = (\delta_t^T \widehat F_t) / \Vert\delta_t\Vert^2$ on bins of $\Vert\delta_t\Vert$.
4. Set conservative lower bound $\hat{\alpha}$ as a low quantile (e.g., 10th percentile) of $r_t$ in the valid region.

##### Estimating $R$ (valid-region radius)

Estimate $R$ as the largest radius for which sector inequality violations remain below tolerance:

*[Operational Criterion]*

$$\hat{R} = \sup \left\{ r \gt 0 : \Pr\left(\delta^T \widehat{F} \lt \hat{\alpha}\Vert\delta\Vert^2 \,\middle\vert\, \Vert\delta\Vert \le r\right) \le \epsilon \right\}$$

with a chosen violation tolerance $\epsilon$ (e.g., 5%).

##### Estimating $\Vert\delta_{\text{critical}}\Vert$

Define a mission-level performance metric $J$ (reward rate, tracking error, service SLA, etc.). Set the critical mismatch threshold where performance crosses a minimum acceptable level $J_{\min}$:

*[Operational Definition]*

$$\Vert\hat{\delta}_{\text{critical}}\Vert = \inf \left\{ d : \mathbb{E}[J \mid \Vert\delta\Vert = d] \lt J_{\min} \right\}$$

This anchors [Result I.24](#persistence-condition) to real task outcomes.

#### Recommended Estimation Sequence

1. Fix mismatch representation $\delta$ in one consistent unit system (prefer surprise-scale).
2. Estimate $U_o$ from channel physics/calibration; estimate $U_M$ from model uncertainty.
3. Validate gain behavior against [Empirical I.19](#update-gain) ($\hat{\eta}^\ast$ trend checks).
4. Estimate $\rho_{\text{delib}}$ from pause windows ([Derived I.23](#deliberation-cost)) and $\rho(t)$ from full traces.
5. Estimate $\alpha$ and $R$ from local correction dynamics ([Derivation A.1](#sector-condition-derivation)).
6. Estimate $\Vert\delta_{\text{critical}}\Vert$ from task-performance degradation.
7. Compute derived diagnostics:

   - Tempo margin: $\hat{\mathcal T} - \hat{\rho}/\Vert\hat{\delta}_{\text{critical}}\Vert$
   - Reserve: $\widehat{\Delta \rho^\ast} = \hat{\alpha}\hat{R} - \hat{\rho}$
   - Deliberation feasibility: $\Delta\eta^\ast(\Delta\tau)\Vert\delta_{\text{post}}\Vert - \hat{\rho}_{\text{delib}}\Delta\tau$

#### Decision-Theoretic Procedures

##### Estimating $\lambda$ (Exploration Price)

The exploration weight $\lambda(M_t)$ in [Definition I.20](#causal-information-yield)'s policy objective prices information in value-equivalent terms:

| Context | $\lambda$ estimator | Source |
|---------|--------------------|--------|
| Finite bandits | Gittins index from dynamic programming | Exact (Gittins 1979) |
| Linear-Gaussian | Probing cost in quadratic objective | Exact (dual control) |
| Discrete MDP | $(\text{VoI})^2 / \text{info gain}$ | Information-directed sampling (Russo & Van Roy) |
| General | $\hat{\lambda} = c \cdot \hat U_M / \hat U_o$ | Heuristic: scale CIY weight by relative uncertainty |

For the heuristic: when $U_M \gg U_o$ (highly uncertain model), exploration is cheap relative to exploitation risk, so $\lambda$ should be large. When $U_M \ll U_o$ (confident model, noisy observations), exploitation dominates. The constant $c$ is domain-specific.

##### Deliberation Stopping Policy

From [Derived I.23](#deliberation-cost), deliberation of duration $\Delta\tau$ is warranted when $\Delta\eta^\ast(\Delta\tau) \cdot \Vert\delta_{\text{post}}\Vert \gt \rho_{\text{delib}} \cdot \Delta\tau$. Operationally:

1. Estimate $\rho_{\text{delib}}$ from prior pause windows.
2. Before each deliberation episode, estimate $\Vert\delta_{\text{post}}\Vert$ as current mismatch + $\rho_{\text{delib}} \cdot \Delta\tau_{\text{planned}}$.
3. Estimate $\Delta\eta^\ast(\Delta\tau)$ from the diminishing-returns profile of past deliberation episodes.
4. Stop deliberating when the marginal improvement rate $\partial \Delta\eta^\ast / \partial \Delta\tau$ drops below $\rho_{\text{delib}} / \Vert\delta_{\text{post}}\Vert$.

##### Structural-Switch Trigger

From [Result I.26](#structural-adaptation-necessity), structural adaptation is indicated when parametric convergence leaves a mismatch floor. Operationally:

1. Estimate the current mismatch floor $\Vert\delta\Vert_{\text{floor}}$ from converged residual statistics.
2. Estimate post-switch expected mismatch as $\Vert\delta\Vert_{\text{new}} \approx \rho / \alpha'$ where $\alpha'$ is the sector bound under the candidate new model class.
3. Estimate transition cost $C_{\text{switch}}$: knowledge loss, retraining time ($\Delta\tau_{\text{switch}}$), and accumulated mismatch during transition ($\rho \cdot \Delta\tau_{\text{switch}}$).
4. Switch when: $(\Vert\delta\Vert_{\text{floor}} - \Vert\delta\Vert_{\text{new}}) \cdot T_{\text{horizon}} \gt C_{\text{switch}}$.

#### Estimator Uncertainty Guidance

**$\hat{\eta}^\ast$ (gain estimate).** Approximate variance via the delta method:

$$\text{Var}(\hat{\eta}^*) \approx \hat{\eta}^{*2}(1-\hat{\eta}^*)^2 \left[\frac{\text{Var}(\hat{U}_M)}{\hat{U}_M^2} + \frac{\text{Var}(\hat{U}_o)}{\hat{U}_o^2}\right]$$

Near 0 or 1, stable (dominated by one source). Near 0.5, most volatile.

**$\hat{\rho}$ (mismatch injection rate).** Finite-difference estimation amplifies noise. Recommend smoothing before differencing. Minimum ~20 observations for stable trend; ~50 for reliable variance. The $[\cdot]_+$ clipping introduces positive bias at small $\rho$.

**$\hat{\alpha}$ (sector lower bound).** The 10th-percentile approach gives approximately 90% confidence under stationarity. Report quantile level, bin count, and bin width.

**$\hat{R}$ (sector-condition radius).** A sharp drop-off in sector-condition satisfaction is a strong signal; gradual decay suggests the sector condition may not hold cleanly.

**Nonstationarity caveat.** All estimators assume approximate stationarity over the estimation window. When environment regime changes are suspected ([Result I.26](#structural-adaptation-necessity)), re-estimate from post-change data only.

#### Epistemic Status

This is a *procedures document* — estimation recipes, not theoretical claims. Each estimator inherits the epistemic status of the quantity it targets: the gain estimator's validity depends on [Empirical I.19](#update-gain)'s structural claim; the sector-bound estimator's validity depends on [Result I.25](#sector-condition-stability)'s assumptions. The estimation procedures themselves are *conditional* on these theoretical foundations and on the stationarity and data-sufficiency assumptions noted above.

#### Working Notes

- End-to-end worked examples instantiating the full chain are in [Worked example B.2](#worked-example-kalman) (exact) and [Worked example B.3](#worked-example-bandit) (approximate).
- The $\hat{\rho}$ estimator's dependence on $\hat{\mathcal{T}}$ creates a sequential estimation chain. Errors compound. An alternative approach: estimate $\rho$ directly from exogenous environmental change measurements when available, bypassing the mismatch trajectory entirely.
- The structural-switch trigger's $T_{\text{horizon}}$ (expected time the new model class will remain adequate) is itself uncertain and difficult to estimate. In practice, this is where the agent's $M_t$ does the real work — predicting environmental stability.

*(Descended from TFT Appendix B: Operationalization.)*


<a id="worked-example-kalman"></a>

### Worked-example B.2: *Worked Example — 1D Active Tracking (Kalman Domain)*

Every ACT quantity has an exact Kalman-filter counterpart. This is a *validation* of the formal chain — all quantities are computable in closed form.

#### System

The agent tracks scalar state $x_t$ and chooses sensor mode $a_t \in \{L, H\}$:

- Dynamics: $x_{t+1} = x_t + v_t$, $v_t \sim \mathcal{N}(0, q)$, $q = 0.25$
- Observation: $y_t = x_t + n_t^{(a_t)}$
- Low mode noise: $r_L = 9$; High mode noise: $r_H = 1$
- Event rate: $\nu = 5 \text{ Hz}$
- High mode has higher energy cost

#### Chain Instantiation

##### Scope ([Scope I.5](#scope-condition))

*Mapping: exact.*

$\Omega_t = x_t$ is partially observed via noisy channel. $\mathcal{A} = \{L, H\}$ is non-empty and causally affects observation quality. Residual uncertainty persists due to process and sensor noise.

##### Causal Structure ([Postulate I.7](#causal-structure)) + CIY ([Definition I.20](#causal-information-yield))

*Mapping: exact.*

Action precedes observation and changes $P(y_t \mid do(a_t))$ through $r_{a_t}$. Using low mode as comparator action, the CIY is the interventional KL divergence:

*[Worked Quantity]*

$$\text{CIY}(H) = D_{\mathrm{KL}}\!\big(P(y \mid do(H)) \,\Vert\, P(y \mid do(L))\big)$$

$$= \frac{1}{2}\left[\log\!\left(\frac{P^- + r_L}{P^- + r_H}\right) + \frac{P^- + r_H}{P^- + r_L} - 1\right]$$

With $P^- = 4.25$: $\text{CIY}(H) \approx 0.161 \text{ nats}$.

##### Model ([Formulation I.10](#agent-model))

*Mapping: exact.*

Model state $M_t = (\hat x_{t\vert t}, P_{t\vert t})$ — a compression of interaction history with recursive update.

##### Mismatch ([Definition I.17](#mismatch-signal))

*Mapping: exact.*

$$\delta_t = y_t - \hat{x}_{t\vert t-1}$$

##### Update Gain ([Empirical I.19](#update-gain))

*Mapping: exact.*

Scalar Kalman gain:

$$K_t = \frac{P^-_t}{P^-_t + r_{a_t}}$$

With $P^- = 4.25$: $K(H) \approx 0.810$, $K(L) \approx 0.321$.

The exact uncertainty ratio mapping: $U_M = P^-_t$, $U_o = r_{a_t}$, $\eta^\ast = K_t$.

##### Exploration ([Definition I.20](#causal-information-yield))

*[Worked Objective]*

$$a_t^* = \arg\max_a \left[\mathbb{E}[\text{value}(a)\mid M_t] + \lambda_t \, \mathbb{E}[\text{CIY}(a)\mid M_t]\right]$$

When uncertainty is high ($P^-$ large), CIY term favors high mode. As uncertainty falls, policy shifts toward low-cost $L$.

##### Deliberation Threshold ([Derived I.23](#deliberation-cost))

Suppose a planning pause of $\Delta\tau = 0.5 \text{ s}$, with measured $\rho_{\text{delib}} = 0.40 \;\text{surprise/s}$.

Cost during pause: $0.20$ surprise units. If $\Vert\delta_{\text{post}}\Vert = 0.70$, deliberation is worthwhile when:

$$\Delta\eta^*(0.5)\cdot 0.70 \gt 0.20 \;\Longrightarrow\; \Delta\eta^*(0.5) \gt 0.286$$

##### Structural Adaptation ([Result I.26](#structural-adaptation-necessity))

Assume maneuvering regime change introduces sustained residual autocorrelation and mismatch floor. If estimated valid radius drops to $R = 0.08$ while $R^\ast = \rho/\alpha = 0.12$, parametric adaptation is no longer adequate ($R^\ast \gt R$), triggering model-class change (e.g., constant-velocity → constant-acceleration process model).

##### Tempo + Persistence ([Definition I.21](#adaptive-tempo), [Result I.24](#persistence-condition))

Using action mix $70\% H, 30\% L$:

$$\bar{\eta}^* = 0.7(0.810) + 0.3(0.321) = 0.663$$

$$\mathcal{T} = \nu \bar{\eta}^* = 5 \cdot 0.663 = 3.315 \;\text{s}^{-1}$$

With $\rho = 0.18 \text{ surprise/s}$ and $\Vert\delta_{\text{critical}}\Vert = 1$:

$$\mathcal{T} \gt \frac{\rho}{\Vert\delta_{\text{critical}}\Vert} \;\;\Rightarrow\;\; 3.315 \gt 0.18 \;\checkmark$$

##### Lyapunov Bounds ([Result I.25](#sector-condition-stability))

From data: $\alpha = 2.6 \text{ s}^{-1}$, $R = 1.4$, $\rho = 0.18$.

$$R^* = \frac{\rho}{\alpha} = \frac{0.18}{2.6} \approx 0.069 \lt R$$

$$\Delta\rho^* = \alpha R - \rho = 2.6(1.4) - 0.18 = 3.46$$

The agent is comfortably within its invariant region with substantial adaptive reserve.

#### Mapping Quality Summary

| ACT Concept | Kalman Mapping | Status |
|-------------|---------------|--------|
| Scope | Exact | Definitional |
| Causal structure + CIY | Exact | Closed-form KL |
| Model ($M_t$ as sufficient statistic) | Exact | Kalman state + covariance |
| Mismatch ($\delta_t$ = innovation) | Exact | Standard Kalman innovation |
| Gain ($\eta^\ast = K_t$) | Exact | Kalman gain IS uncertainty ratio |
| Tempo ($\mathcal{T} = \nu \bar{\eta}^\ast$) | Exact | Closed-form |
| Persistence condition | Exact | Linear ODE solution |
| Lyapunov bounds ($R^\ast$, $\Delta\rho^\ast$) | Exact | From estimated sector parameters |

#### Epistemic Status

This is a *worked instantiation*, not a theoretical claim. Every mapping is exact — the Kalman domain is the canonical case where ACT's formal chain has closed-form realizations. The example validates that the formal chain is internally consistent and instantiable.

#### Working Notes

- This example uses a 1D system. The tensor-tempo extension ([Result III.13](#per-dimension-persistence)) becomes visible only in multi-dimensional tracking where different state dimensions have different observability.
- The structural adaptation trigger (constant-velocity → constant-acceleration) is manufactured for the example. A more natural test would be a real tracking system with genuine regime changes.
- The Kalman filter is provably optimal for the linear-Gaussian case. Every TFT/ACT quantity has not just an analog but the *exact optimal* value. This makes it the strongest validation but also the easiest — the real test is non-Kalman domains (see [Worked example B.3](#worked-example-bandit)).

*(Descended from TFT Appendix C.)*


<a id="worked-example-bandit"></a>

### Worked-example B.3: *Worked Example — Nonstationary Bandit (RL Domain)*

ACT's conceptual architecture applies beyond the conjugate-Bayesian regime. The mapping here is *approximate* — it shows that ACT's concepts organize RL phenomena, but the quantitative relationships are structural analogies, not derivations. Where the mapping is exact versus approximate is marked explicitly.

#### System

A $k$-armed bandit ($k = 4$) with slowly drifting reward means:

*[Formulation]*

$$\mu_i(t+1) = \mu_i(t) + w_i(t), \quad w_i(t) \sim \mathcal{N}(0, q), \quad q = 0.01$$

- Observation: Pulling arm $a_t = i$ yields reward $r_t = \mu_i(t) + \varepsilon_t$, $\varepsilon_t \sim \mathcal{N}(0, \sigma^2)$, $\sigma^2 = 1.0$.
- Event rate: $\nu = 1$ pull per step.
- Agent: Q-learning with fixed learning rate $\alpha$ and UCB action selection.

#### Chain Instantiation

##### Scope ([Scope I.5](#scope-condition))

*Mapping: exact.*

$\Omega_t = (\mu_1(t), \ldots, \mu_4(t))$ — not directly observable. $\mathcal{A} = \{1, 2, 3, 4\}$. Residual uncertainty persists: means drift continuously, rewards are noisy, and only one arm is observed per step.

##### Causal Structure ([Postulate I.7](#causal-structure)) + CIY ([Definition I.20](#causal-information-yield))

*Mapping: exact for causal ordering; approximate for CIY formula.*

The action (arm choice) temporally precedes the reward observation. Under the Gaussian reward model, CIY for arm $i$:

*[Discussion — Bandit CIY, Gaussian Case]*

$$\text{CIY}(i;\, M_{t-1}) = \frac{1}{2\sigma^2} \mathbb{E}_{j \sim q}\!\left[(\hat{\mu}_i - \hat{\mu}_j)^2\right]$$

This measures how *distinctive* arm $i$'s predicted reward is relative to alternatives — distinctiveness of predictions, not uncertainty about predictions. A proper uncertainty-aware CIY would require maintaining posterior variances per arm, which the basic Q-learning model does not track.

##### Model ([Formulation I.10](#agent-model)) and Sufficiency ([Definition I.12](#model-sufficiency))

*Mapping: exact structural mapping; the model is deliberately impoverished.*

$$M_t = (\hat{\mu}_1, \ldots, \hat{\mu}_4,\; n_1, \ldots, n_4)$$

Model sufficiency $S(M_t) \lt 1$ for two reasons: (1) No drift tracking — the model treats reward means as stationary. (2) No uncertainty representation — unlike a Bayesian agent that would maintain posterior variances.

##### Mismatch ([Definition I.17](#mismatch-signal))

*Mapping: exact.*

$$\delta_t = r_t - \hat{\mu}_{a_t}$$

Decomposes exactly: $\mathbb{E}[\delta_t^2] = (\hat{\mu}_{a_t} - \mu_{a_t}(t))^2 + \sigma^2$.

##### Update Gain ([Empirical I.19](#update-gain))

*Mapping: approximate. This is where the bandit agent is most deficient relative to ACT-optimal behavior.*

The Q-learning update

$$\hat{\mu}_{a_t} \leftarrow \hat{\mu}_{a_t} + \alpha \cdot \delta_t$$

uses a **degenerate constant gain**. It does not adapt to the agent's current uncertainty state.

**Optimal gain via effective window.** A fixed $\alpha$ is equivalent to exponential discounting with effective window $W = (1 - \alpha)/\alpha$. The per-arm model uncertainty balances estimation variance and drift-induced bias:

$$U_M \approx \frac{\sigma^2}{W} + q \cdot W$$

The optimal window $W^\ast = \sigma / \sqrt{q} = 10$ gives $\alpha^\ast \approx 0.091$, $U_M \approx 0.2$, and:

$$\eta^* = \frac{U_M}{U_M + U_o} = \frac{0.2}{1.2} \approx 0.167$$

The discrepancy between $\alpha^\ast$ and $\eta^\ast$ arises because $\alpha$ operates on raw prediction errors while $\eta^\ast$ accounts for the full uncertainty structure. The two converge when the model properly tracks its own uncertainty.

##### Exploration ([Definition I.20](#causal-information-yield))

*Mapping: approximate structural analogy.*

UCB: $a_t = \arg\max_i [\hat{\mu}_i + c\sqrt{\ln t / n_i}]$

| ACT component | UCB analog | Quality |
|---------------|-----------|---------|
| $\mathbb{E}[\text{value}(a) \mid M_t]$ | $\hat{\mu}_i$ | Exact |
| $\lambda(M_t) \cdot \mathbb{E}[\text{CIY}(a)]$ | $c\sqrt{\ln t / n_i}$ | Approximate |

UCB captures the CIY structure (rarely-visited arms are more informative) but depends on visit count, not observation content.

##### Tempo + Persistence ([Definition I.21](#adaptive-tempo), [Result I.24](#persistence-condition))

*Mapping: approximate.*

**Per-arm tempo.** With approximately uniform exploration, each arm sampled at rate $\nu/k = 1/4$:

$$\mathcal{T}_i = \frac{\nu}{k} \cdot \alpha = 0.25 \times 0.091 = 0.023 \;\text{step}^{-1}$$

**Per-arm drift rate:** $\rho_i = \sqrt{q} = 0.1 \;\text{reward units} \cdot \text{step}^{-1}$.

**Persistence check:** $\mathcal T_i = 0.023$ vs $\rho_i = 0.1$ — **fails**. Per-arm correction tempo is too low relative to drift. The agent cannot keep all arms' estimates current under uniform exploration.

**Interpretation.** This is expected and informative. ACT diagnoses exactly why: with 4 arms and one pull per step, each arm is visited too infrequently to track its drifting mean. Two remedies:

1. **Increase $\eta^\ast$** (raise $\alpha$): Extract more per observation, but increase steady-state noise.
2. **Concentrate $\nu$**: Abandon uniform exploration. Focus pulls on a subset, increasing per-arm $\nu/k_{\text{active}}$. This is exactly what a good UCB policy does.

With focused exploration ($k_{\text{active}} = 2$, $\alpha = 0.2$): $\mathcal T_i = 0.5 \times 0.2 = 0.1$ — barely meets the threshold. The fundamental tension: with limited pulls and significant drift, the agent must accept either failing to track some arms or using high $\alpha$ that introduces noise.

**Aggregate failure.** $\mathcal{T} = \nu \cdot \alpha = 0.091$ vs $\rho = k \cdot \sqrt{q} = 0.4$. The agent's total adaptive capacity is outpaced by total environmental drift — a regime where model-based approaches (Bayesian bandits, Kalman bandit filters) with higher effective $\eta^\ast$ have a structural advantage.

#### Mapping Quality Summary

| ACT Concept | Bandit Mapping | Status |
|-------------|---------------|--------|
| Scope | Exact | Definitional |
| Causal structure | Exact | Structural |
| CIY | Approximate | Model lacks uncertainty representation |
| Model ($M_t$) | Exact | Definitional |
| Model sufficiency ($S \lt 1$) | Exact | Q-learner demonstrably insufficient |
| Mismatch ($\delta_t$) | Exact | Standard prediction error |
| Gain ($\alpha$ as degenerate $\eta^\ast$) | Approximate | Fixed, does not adapt |
| Exploration (UCB as approximate CIY) | Approximate | Structural analogy |
| Tempo ($\mathcal{T} = (\nu/k) \cdot \alpha$ per arm) | Approximate | Assumes uniform allocation |
| Persistence condition | Exact (qualitative) | Threshold structure is robust |

#### Epistemic Status

This is a *structural mapping*, not a derivation. The mapping is *exact* for scope, causal ordering, model compression, and mismatch. It is *approximate* for gain, exploration, and tempo — precisely because the Q-learner does not represent its own uncertainty, which is what [Empirical I.19](#update-gain) requires for optimal behavior. The gap between the Q-learner's fixed $\alpha$ and the ACT-optimal adaptive $\eta^\ast$ is precisely the gap between a fixed-gain PID controller and a Kalman filter.

The mapping status is *conditional* because the quantitative relationships depend on the Gaussian reward model and specific parameterization. The qualitative conclusions (persistence failure under uniform exploration, the concentration-vs-noise tradeoff) should be robust.

#### Working Notes

- The per-arm analysis is a natural instance of the per-dimension tempo decomposition ([Result III.13](#per-dimension-persistence)): each arm is an independent mismatch dimension with its own $\mathcal T_i$ and $\rho_i$. The aggregate tempo overstates effective adaptation along any individual arm's dimension — exactly the failure mode that the scalar-to-tensor generalization captures.
- A Bayesian bandit (maintaining per-arm posteriors with exponential discounting) would achieve higher [Definition I.12](#model-sufficiency) by representing its own uncertainty, yielding an adaptive $\eta^\ast$ that matches the ACT-optimal form. Comparing Q-learner vs Bayesian bandit performance under nonstationarity is a direct test of [Empirical I.19](#update-gain)'s structural claim.
- Reward-unit and surprise-unit formulations coincide up to normalization by $\sigma^2$. For this example ($\sigma = 1$), they are identical.

*(Descended from TFT Appendix D.)*

