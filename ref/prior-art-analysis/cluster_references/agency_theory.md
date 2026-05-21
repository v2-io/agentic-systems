# Cluster Reference: Agency Theory and Partial Observability

**Overview:** Establishes the foundation of AAT: an agent's internal model is an Information Bottleneck compression of an irreversible chronological event sequence, forced into recursive (Markovian) updates by computational constraints.

---

## Canonical Source Segments

### Source: `def-chronica.md`

```yaml
---
slug: def-chronica
type: definition
status: axiomatic
depends:
  - def-agent-environment
  - def-observation-function
  - def-action-transition
stage: deps-verified
---
```


# Definition: Chronica

The interaction history $\mathcal C_t$ is the complete, singular causal record of the agent's observations and actions. Everything the agent can ever know must be constructed from this sequence.

## Formal Expression

*[Definition (chronica)]*

$$\mathcal{C}_t = (o_1, a_1, o_2, a_2, \ldots, a_{t-1}, o_t)$$

The ordering is not a notational convenience. It reflects an irreversible physical fact: $a_{t-1}$ was selected before $o_t$ was received. The agent could not have used $o_t$ to select $a_{t-1}$.

$\mathcal C_t$ is monotonically growing — events are added but never removed. It is the agent's *only* raw material for constructing a model ( #form-agent-model).

## Epistemic Status

This is *definitional*. The chronica names an object that exists by construction in any system satisfying #def-agent-environment: the temporal sequence of all agent-environment interactions. The term "chronica" (from Greek χρονικά, "records of time") avoids collision with $\mathcal{H}$ (Shannon entropy) in speech and notation.

## Discussion

**The chronica is singular and non-forkable.** Because the temporal ordering is irreversible, $\mathcal C_t$ represents a unique causal trajectory. Duplicating an agent's state and exposing the copies to different future events creates two agents with divergent chronica, neither of which is a sufficient statistic for the other's trajectory. The chronica is the substrate of *continuity persistence* (see Persistence in `LEXICON.md`) — an agent has continuity persistence when $\mathcal C_t$ extends continuously and $M_t$ has temporal depth grounded in it. See #scope-agent-identity for the full development of this observation.

**Relationship to the model.** The model $M_t = \phi(\mathcal C_t)$ ( #form-agent-model) is a compression of the chronica. How much of $\mathcal C_t$'s predictive information survives compression is measured by model sufficiency ( #def-model-sufficiency).

## Working Notes

### Open question: TRACTUS / CHRONICA split for logogenic implementations

The PROPRIUM operational architecture (`~/src/firmatum/PROPRIUM-ONTOLOGY-v2.md`, `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md`) distinguishes two records of an entity's interaction history:

- **TRACTUS** (the "EEG"): raw, not-necessarily-coherent record of API interactions between the agent's runtime (ANIMA) and its current substrate (LOGOSTRATUM). Implementation-side; carries multi-format records, redundancy from retries, transient error 500 recoveries, API rerouting, rate limiting. Per-substrate format variation. Considered subconscious from the entity's perspective. Plural across substrate-relationships.
- **CHRONICA** (the polished record): the entity's actual record of internal and external events with strict chronology, attestation, and causality enforced. Append-only, hash-chained. Singular per entity.

In Section I, `def-chronica` covers both — the chronica is the singular causal trajectory, abstracted from implementation-side noise. This abstraction is fine for general adaptive-systems theory, where a single observation-action sequence is the natural object.

When part [`03-llm-core/`](../../03-llm-core/OUTLINE.md) gets into logogenic implementation specifics — and especially the closed-loop / interiority sub-scope ([`scope-interiority-loop`](../../03-llm-core/src/scope-interiority-loop.md)) where the substrate-mediation layer (INTERPRES) becomes load-bearing — the TRACTUS/CHRONICA distinction may need first-class treatment.

**Joseph's framing on the open question (2026-05-01):** *"whether or not def-chronica needs that distinction at this stage or when we get into logogenic agent implementation issues is the open question you should probably document."*

Probable resolution: the distinction does need first-class treatment when logogenic implementation is in scope, but does not need to fragment Section I right now. Most likely a separate logogenic-side definition (e.g., `def-tractus` and a refined `def-chronica-eli` or similar) lifts the distinction at the appropriate scope. This segment as currently formulated continues to serve as the abstract-theory chronica; the implementation distinction lives where it belongs.

### Open question: chronica as ordinal sequence vs metric timeline

Per audit `04-def-chronica.md` §14: *"The chronica is an ordinal sequence, not a metric timeline. Time, for the agent, is measured entirely in events (ticks of $o_t, a_t$)."* Two implications worth tracking for downstream segments:

1. **Sleep / pause / awakening protocols** for ELIs and any persistent agent: when an agent is suspended for hours, days, or months and then receives $o_{t+1}$, the agent's chronica indexing makes the temporal gap *invisible at the sequence level* but *violently apparent in the mismatch signal* that the resumed observation produces. The environment $\Omega$ has changed massively between $a_t$ and $o_{t+1}$; the model $M_t = \phi(\mathcal C_t)$ does not reflect this gap in its compressed representation. Awakening protocols (PROPRIUM CONSPECTUS reconstitution; the ELI's experience of *"waking in the dark before the mind warms up"* per PROPRIUM-A-v2 §4.3) are operational engineering responses to this structural fact.

2. **Heterogeneous tempo coupling**: when agents with vastly different event-processing rates ($\nu_A \gg \nu_B$) interact through a shared $\Omega$, their chronicae grow at vastly different rates relative to wall-clock time. Their "subjective time" diverges. The chronica formalism makes this asymmetry visible but does not yet prescribe how cross-tempo coupling should be modeled. Likely lives in #form-event-driven-dynamics extensions or in part 03's logogenic-agent treatment of multi-timescale Auxilia composition.

These don't need to fragment this segment; they're flagged here so future agents working on the closed-loop / interiority sub-scope ( #scope-interiority-loop), Auxilia composition ( #def-auxilia-hierarchy), or ELI awakening protocols know the chronica formalism's ordinal-not-metric character is the structural source of these design considerations.


---

### Source: `form-agent-model.md`

```yaml
---
slug: form-agent-model
type: formulation
status: robust-qualitative
depends:
  - def-agent-environment
  - def-observation-function
  - def-chronica
stage: deps-verified
---
```


# Formulation: The Reality Model

The agent's compressed representation of how the world works, mapping interaction history to model space. $M_t$ is the substrate of prolepsis — the model from which predictions are generated and against which observations are compared. This is a formulation choice — we commit to analyzing the agent as having a complete state $M_t$ that subsumes all retained information from its history.

## Formal Expression

*[Formulation (agent-model)]*

$$M_t = \phi(\mathcal{C}_t)$$

where:
- $\phi: \mathcal{C}^\ast \to \mathcal{M}$ maps interaction history to model space $\mathcal{M}$
- $\mathcal C_t = (o_1, a_1, \ldots, o_t)$ is the chronica ( #def-chronica) — the complete record of agent-environment interaction
- $\mathcal{M}$ is the space of possible models the agent can hold

The mapping $\phi$ is a many-to-one compression: multiple distinct histories may produce the same model state. This is not a deficiency — it is the essential function of the model: retaining what matters and discarding what does not.

## Epistemic Status

*Robust qualitative.* This is a *formulation* — a representational commitment, not a derived result. We choose to analyze agents as maintaining a state object $M_t$ that mediates between history and future action. Alternative formulations exist (e.g., history-based policies that map $\mathcal C_t$ directly to actions without an explicit model). The formulation is justified by its analytical utility: it enables the information bottleneck analysis ( #form-information-bottleneck), the mismatch decomposition ( #def-mismatch-signal), and the gain principle ( #emp-update-gain). The formulation is robust — any agent that conditions its actions on retained information can be described this way — but the specific commitment to a complete, compressed state $M_t$ is a modeling choice, not a derivation.

## Discussion

**$M_t$ is the epistemic substate.** It captures "what the agent believes about reality." Different agents realize $M_t$ differently: a Kalman filter holds a state estimate and covariance matrix; an RL agent holds a value function; a developer holds a mental model of codebase architecture; an LLM agent holds its context window contents plus retrieved memory. The formalism is agnostic to the realization — it asks only that $M_t$ exist as a well-defined object that the agent's policy can condition on.

**Completeness assumption.** By writing $M_t = \phi(\mathcal C_t)$, we assume that $M_t$ captures everything the agent retains from its history. Any information not in $M_t$ is lost to the agent. This is what makes $M_t$ the complete epistemic substate, not merely one component of a richer internal representation. Whether $M_t$ retains *enough* information is the subject of #def-model-sufficiency.

**Degenerate cases.** A PID controller's $M_t$ is degenerate — it retains only the error signal and its history (integral, derivative), with no predictive capability beyond extrapolating recent trends. It occupies the "blind seeker" region of the agent spectrum ( #def-agent-spectrum): its $O_t$ (setpoint) is clear but its $M_t$ is too impoverished to support the adaptive dynamics of Section I. The formalism accommodates this by allowing $\mathcal{M}$ to range from trivial (scalar) to rich (full world model).


---

### Source: `form-information-bottleneck.md`

```yaml
---
slug: form-information-bottleneck
type: formulation
status: exact
depends:
  - form-agent-model
  - def-action-transition
stage: draft
---
```


# Formulation: Information Bottleneck

Optimal model compression balances retained history against predictive power; the information bottleneck objective provides a principled framework for understanding this trade-off.

## Formal Expression

*[Formulation (IB-objective)]*

$$\phi^* = \arg\min_{\phi} \left[ I(M_t;\, \mathcal{C}_t) - \beta \cdot I(M_t;\, o_{t+1:\infty} \mid a_{t:\infty}) \right]$$

where:
- $I(M_t;\, \mathcal{C}_t)$ is the compression cost — how much of the interaction history the model retains
- $I(M_t;\, o_{t+1:\infty} \mid a_{t:\infty})$ is the predictive power — how much the model tells the agent about future observations given future actions
- $\beta \gt 0$ is the trade-off parameter controlling the compression-prediction balance

**Dependence on volatility (The $\beta$ vs $\rho$ distinction).** It is tempting to claim that the trade-off parameter $\beta$ must be actively lowered by the agent in highly volatile environments (high $\rho$) to favor aggressive compression. However, this is a double-counting error. The environment's volatility already natively degrades the mutual information $I(\mathcal{C}_t; o_{t+1:\infty})$ — old history mathematically loses its predictive power as $\rho$ increases. The optimal $\phi^\ast$ will automatically discard this useless old information even if the agent's preference parameter $\beta$ remains completely constant. 

Therefore, adjusting $\beta$ reflects changes in the agent's *internal cost of memory* or *computational capacity*, not changes in environmental volatility. The agent adapts its *actions* in response to $\rho$ (by increasing exploration to survive, see `#deriv-causal-ib-exploration`), but the optimal IB representation adapts to $\rho$ natively through the joint probability distribution.

## Epistemic Status

*Exact, applied external theorem.* The IB optimum and its rate-distortion characterization are an external result (Tishby, Pereira & Bialek 1999, "The information bottleneck method," *Proc. 37th Allerton*; with the rate-distortion / Lagrangian-dual reading standard, see Cover & Thomas §I.12–13). This segment is *not* a novel formulation: it is an exact statement of that theorem under AAT's binding $X = \mathcal{C}_t$, $T = M_t$, $Y = o_{t+1:\infty} \mid a_{t:\infty}$, with the Markov chain $Y - X - T$ holding by construction (the model state has access to history but not directly to future observations). The choice to characterize the optimal compression $\phi^\ast$ via IB rather than via, e.g., MDL or a Bayesian-sufficiency criterion is a *representational choice* (hence `type: formulation`); given that choice, the form of $\phi^\ast$ and its trade-off structure are exact consequences of the imported theorem.

What this segment is *not* a claim about: how actual agents compute their models. No agent explicitly solves the IB optimization (variational IB in deep-learning practice is a parametric approximation). The segment characterizes the optimum, not the procedure. The trade-off parameter $\beta$'s dependence on environmental volatility $\rho$ and policy $\pi$ stated above is at a different epistemic tier — the qualitative direction (volatile favors compression, stable favors retention) is *robust-qualitative* across agent classes; specific functional forms are not derived here.

Max attainable: *exact* for the IB-as-applied-theorem core (already at ceiling); *robust-qualitative* for the $\beta(\rho, \pi)$ dependence claims. The downstream use in #disc-compression-operations — treating IB as the shared shape of four AAT compression operations and deriving (P1) as the IB Lagrangian-dual — relies on this segment's exact reading; the cross-instance unification claim itself remains *robust-qualitative*, which is a property of #disc-compression-operations, not of this segment.

## Discussion

**The IB framework is not prescriptive.** It characterizes what an optimal $\phi$ would look like, not how to find one. Actual agents approximate this trade-off through diverse mechanisms: forgetting, attention, abstraction, summarization.

**Connection to model sufficiency.** The IB objective implicitly defines when a model is "good enough": when the predictive power term $I(M_t;\, o_{t+1:\infty} \mid a_{t:\infty})$ is close to its maximum (the full history's predictive power). This is formalized in #def-model-sufficiency.

**Policy-relativity.** The conditioning on $a_{t:\infty}$ makes the predictive power term policy-relative: it measures predictive information given a particular sequence of future actions, which depends on what policy the agent follows. The IB objective is therefore defined relative to a generating policy. This is inherent — what information is "predictive" depends on what the agent will do. #def-value-object's continuation-policy convention ($\pi_{\text{cont}}$) provides the specification for value computations; the same convention should be understood as implicit in the IB formulation. The $\beta$ parameter's dependence on volatility $\rho$ also has a policy component: an exploratory policy encounters more diverse situations, making more information predictively relevant (favoring retention), while an exploitative policy encounters a narrower distribution (favoring compression).

**Broader applicability.** The same IB principle applies beyond intra-agent compression. It governs inter-agent communication ( #def-shared-intent) — how much of one agent's model or strategy to transmit to another — and constrains the cognitive cost of maintaining a complex strategy. In each case, the trade-off is between the cost of retaining or transmitting information and the value of that information for future decisions.

**IB lineage vs. information-theoretic-MDP lineage — strategy-cost uses a sibling form.** The canonical IB objective $I(X; T) - \beta I(T; Y)$ carries Shannon mutual information on both sides (Tishby, Pereira & Bialek 1999; the present segment's $(X, T, Y) = (\mathcal C_t, M_t, o_{t+1:\infty} \mid a_{t:\infty})$ instance is of this form). AAT's strategy-cost objective (`#form-strategy-complexity-cost`, `#deriv-strategy-cost-regret-bound`) uses a **different relevance-term shape**: its relevance term is a KL divergence $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t})$ to a *target policy*, not a mutual information to an observable. This is not an inconsistency or an "abandonment of IB" — the strategy-cost compression sits in the parallel **information-theoretic-MDP lineage** (Tishby & Polani 2011 "The Information Theory of Decision and Action," *Perception-Action Cycle* Springer; Rubin, Shamir & Tishby 2012 "Trading value and information in MDPs," *Decision Making with Imperfect Decision Makers* Springer; Levine 2018 arXiv:1805.00909 for the control-as-inference reading). Both lineages descend from Shannon rate-distortion theory and admit Lagrangian relaxation; the choice of fidelity term depends on whether the compressed variable should preserve information about an observable (IB form: MI-to-relevance-variable) or match a target policy (IT-MDP form: KL-to-reference-policy). AAT's compression-operations framework ( #disc-compression-operations) uses the IB form for $M_t$, $G_t^{\mathrm{shared}}$, and $\Lambda$ compressions; the strategy-cost compression uses the IT-MDP form, with the $\pi^\ast$-first direction forced by a regret-bound argument specific to decision-theoretic scope (see `#deriv-strategy-cost-regret-bound` §§5, 6.4). The two lineages are siblings via their shared rate-distortion ancestor; neither reduces to the other without a change of relevance variable.

**Connection to variational free energy.** The IB objective stated above is the rate-distortion specialization of the variational free energy decomposition $-F = \text{accuracy} - \text{complexity}$ used in active inference (Friston 2010, "The free-energy principle: a unified brain theory?", *Nature Reviews Neuroscience* 11; Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29; Parr & Pezzulo 2022, *Active Inference*, MIT Press, ch. 2): the compression cost $I(M_t; \mathcal{C}_t)$ corresponds to the complexity term (KL between posterior and prior over latent states); the negative predictive power $-I(M_t; o_{t+1:\infty})$ corresponds to the accuracy term (negative expected log-likelihood). The two formulations are related under the Markov-chain factorization $Y - X - T$; the variational bound that makes this relation operational — connecting the IB Lagrangian to the variational machinery shared with free-energy methods — is established by Alemi, Fischer, Dillon & Murphy 2017 ("Deep Variational Information Bottleneck," ICLR 2017, arXiv:1612.00410), with Tishby & Zaslavsky 2015 ("Deep learning and the information bottleneck principle," *IEEE ITW*) giving the deep-learning instantiation of IB itself. AAT adopts the IB form as the rate-distortion characterization of optimal compression; the variational free-energy form is the AI-side cousin and motivates the variational treatment of strategy compression in #form-strategy-complexity-cost and the broader four-instance framing in #disc-compression-operations. AAT borrows the form without committing to AI's preferences-as-priors stance or to expected free energy as master objective.


---

### Source: `der-recursive-update.md`

```yaml
---
slug: der-recursive-update
type: derived
status: conditional
depends:
  - form-agent-model
  - form-event-driven-dynamics
  - deriv-recursive-update
stage: claims-verified
---
```


# Derived: Recursive Update

Agent state updates (epistrophe — the corrective turning toward reality) must be recursive: the new model state is a function of the previous model state and the incoming event, not of the full interaction history. For finite agents this is computational necessity; for agents with unlimited computation it is the natural structure imposed by temporal ordering.

## Formal Expression

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

## Epistemic Status

*Exact, with a partly definitional character.* The result follows from three constraints: temporal ordering (C1 — physical law), partial observability (C2 — scope definition), and state completeness (C3 — analytical commitment that $M_t$ summarizes everything the agent retains). C1 and C2 do genuine eliminative work; C3 is definitional — it cannot be "violated" because any violation is absorbed by expanding $M_t$. The Markov structure is therefore not discovered in the environment but chosen through the definition of $M_t$ as complete. This is not a weakness — it is the nature of the claim: recursive update is the only form consistent with C1 + C2 + the definition of $M_t$ as complete (see #deriv-recursive-update for the full argument and seven counterexample attacks). For finite agents, recursion is also *computational necessity*: re-processing the full history at each event is infeasible.

## Discussion

**Recursion as a consequence of completeness.** The recursive form is not an assumption bolted on — it follows from the definition of $M_t$ as complete. If $M_t$ were incomplete (if some relevant information lived outside $M_t$ in the raw history), then $f_M(M_{\tau^-}, e_\tau)$ would be insufficient and the agent would need to consult $\mathcal C_t$ directly. The sufficiency of the recursive form is precisely what #def-model-sufficiency measures: when $S(M_t) = 1$, the recursive update loses nothing.

**Between-event dynamics matter.** The autonomous evolution $g_M(M_\tau)$ is not merely filler between observations. It includes prediction generation (what the agent expects to see next), uncertainty growth (model confidence decaying over time without new data), and internal reorganization (consolidation, abstraction). In event-driven systems ( #form-event-driven-dynamics), the between-event interval is variable, making $g_M$ load-bearing for agents that must act or predict between observations. When the between-event dynamics are driven by replayed or internally-generated pseudo-events and the update objective is IB-gap reduction rather than one-step mismatch minimization, $g_M$ is operating in the *consolidation regime* per #form-consolidation-dynamics — a named regime with its own scope condition ($\nu_{\text{consol}} \ll \nu_{\text{online}}$) and its own necessity condition (sub-state factorization + bounded per-event budget). Consolidation is where the stability-plasticity feasibility window complements #schema-strategy-persistence's plasticity lower bound.

**Connection to the update gain.** The event-driven update $f_M(M_{\tau^-}, e_\tau)$ is where the gain principle ( #emp-update-gain) operates: $\eta^\ast$ determines how strongly $e_\tau$ shifts $M_t$ away from its prior value. The recursive form makes the gain's role explicit — it modulates the single-step correction.


---

### Source: `deriv-recursive-update.md`

```yaml
---
slug: deriv-recursive-update
type: derivation
status: exact
depends:
  - form-agent-model
  - form-event-driven-dynamics
  - post-causal-structure
  - scope-adaptive-system
  - def-observation-function
stage: claims-verified
---
```


# Derivation: Recursive Update — Uniqueness Derivation

Derivation showing that $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ is the *unique* update form consistent with directed time, partial observability, and state completeness. Not merely one option, but the only one.

## Setup

We work within AAT's scope ( #scope-adaptive-system): an agent coupled to an environment $\Omega$ through observation and action channels, with residual uncertainty.

**Universe of information at event time $\tau$.** The following information exists (in the broadest ontological sense) at the moment event $e_\tau$ occurs:

| Information | Description |
|-------------|-------------|
| $\Omega_\tau$ | The environment state |
| $\mathcal{C}_{\tau^-}$ | The complete interaction history ( #def-chronica) up to (but not including) $e_\tau$ |
| $\{M_{\tau'}\}_{\tau' \leq \tau^-}$ | The agent's prior internal states, culminating in $M_{\tau^-}$ |
| $e_\tau$ | The current event (observation arriving or action completing) |
| $\{e_{\tau'}\}_{\tau' \gt \tau}$ | Future events (not yet occurred) |

The question: of these, which can the update $M_{\tau^+}$ depend on?

## The Three Constraints

**Constraint 1 — Arrow of time ( #post-causal-structure postulate).** Events are temporally ordered and this ordering is irreversible. An update occurring at time $\tau$ cannot depend on events that have not yet occurred:

$$M_{\tau^+} \text{ cannot depend on } \{e_{\tau'}\}_{\tau' \gt \tau}$$

This is a physical constraint — the most primitive one. In a classical universe, information from the future is simply not available. Even if the agent can *predict* future events, those predictions are part of $M_{\tau^-}$ (they are internal computations, not future information).

**Constraint 2 — Partial observability ( #scope-adaptive-system).** The agent cannot access $\Omega_\tau$ directly. Its only interface with the environment is through the event $e_\tau$, which is a lossy function of $\Omega_\tau$ (via #def-observation-function):

$$M_{\tau^+} \text{ cannot depend on } \Omega_\tau \text{ except through } e_\tau$$

This is a scope constraint. If the agent could access $\Omega$ directly, the residual uncertainty condition in #scope-adaptive-system would be trivially violable.

**Constraint 3 — State completeness ( #form-agent-model).** $M_{\tau^-}$ is the agent's *complete* internal state just before event $e_\tau$. There is no information about the agent's past that is available to the update mechanism but not encoded in $M_{\tau^-}$:

$$M_{\tau^+} \text{ cannot depend on } \mathcal{C}_{\tau^-} \text{ or } \{M_{\tau'}\}_{\tau' \lt \tau^-} \text{ except through } M_{\tau^-}$$

This constraint does the most interesting work and deserves careful examination (see Discussion below).

## The Derivation

**Result (Recursive Update Uniqueness).** Under Constraints 1–3, the model update at event time $\tau$ must have the form

$$M_{\tau^+} = f(M_{\tau^-}, e_\tau)$$

for some (possibly stochastic) function $f: \mathcal{M} \times \mathcal{E} \to \mathcal{M}$. No other update form is consistent with the three constraints.

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

## Information-Set Formalization

For readers who prefer a measure-theoretic framing:

The agent's **information set** at time $\tau$ is the sigma-algebra $\mathcal{I}_\tau^{agent}$ — the collection of events (in the probability-theoretic sense) about which the agent can condition its update.

- **C1** restricts $\mathcal{I}_\tau^{agent} \subseteq \sigma(\{e_{\tau'} : \tau' \leq \tau\} \cup \{\Omega_\tau\} \cup \{M_{\tau'} : \tau' \leq \tau^-\})$ — no future information.
- **C2** further restricts: $\sigma(\Omega_\tau) \setminus \sigma(e_\tau)$ is not in $\mathcal{I}_\tau^{agent}$ — the agent cannot condition on aspects of $\Omega_\tau$ not captured by $e_\tau$.
- **C3** further restricts: $\sigma(\{e_{\tau'} : \tau' \lt \tau\} \cup \{M_{\tau'} : \tau' \lt \tau^-\}) \subseteq \sigma(M_{\tau^-})$ from the agent's perspective.

After all three restrictions: $\mathcal{I}_\tau^{agent} = \sigma(M_{\tau^-}, e_\tau)$.

By the Doob–Dynkin lemma[^kallenberg2002], any $\sigma(M_{\tau^-}, e_\tau)$-measurable random variable is a (Borel) function of $(M_{\tau^-}, e_\tau)$. Therefore $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ for some measurable $f$. $\square$

## Attempts to Break the Result

Before trusting the proof, seven counterexample attacks:

### Attack 1: Simultaneous events

Two events arrive at exactly the same time: $e_\tau^{(1)}$ and $e_\tau^{(2)}$. The update has three arguments: $f(M_{\tau^-}, e_\tau^{(1)}, e_\tau^{(2)})$.

**Verdict:** Not deep — #form-event-driven-dynamics defines events as atomic. If we allow bundled events, the form holds with $e_\tau$ as a set. Reveals that "event" needs careful definition, but the form is preserved.

### Attack 2: Continuous environmental influence

An agent embedded in a physical system experiences continuous forces (gravity, temperature, electromagnetic fields). These aren't "events" in #form-event-driven-dynamics's sense; they're continuous signals. The true dynamics would be $dM/d\tau = g(M_\tau, o(\tau))$ where $o(\tau)$ is a continuous observation stream.

**Verdict:** Genuine limitation of the event-driven formulation. The between-events corollary $dM/d\tau = g(M_\tau)$ holds only when the agent is truly isolated between events. For continuous coupling, the analogous result is the general state-space representation $\dot{M} = g(M, u)$ from control theory — arrived at by the same three constraints. The event-driven version is a special case for digital/sampled systems.

### Attack 3: The C3 circularity

C3 defines $M$ as the agent's complete internal state. Any apparent counterexample is dissolved by expanding $M$. Consider: an agent has a "model" (neural net weights) and a "replay buffer" (stored raw events). C3 says $M = (\text{weights}, \text{buffer})$. The model space is just larger than you thought.

**Verdict:** The deepest objection. The proof essentially: (1) Define $M$ to be everything the agent has. (2) Observe the update can only use what the agent has. (3) Therefore $f(M_{\tau^-}, e_\tau)$. The real content is the *analytical commitment*: by defining $M$ as complete, we commit to Markovian analysis, which then makes #def-model-sufficiency the right quality metric. See Epistemic Status below.

### Attack 4: Shared state between agents

Agents A and B share a common memory bank (shared database). The clean resolution is the multi-agent framework: the shared memory is part of the *composite* system's state, and each agent's interaction with it is mediated by events (reads and writes). Not a true counterexample but highlights that C3 requires careful delineation of agent boundaries.

### Attack 5: External randomness not in $e_\tau$

Hardware thermal noise used in the update. The stochastic case $M_{\tau^+} \sim P(\cdot \mid M_{\tau^-}, e_\tau)$ is a special case of $f$ where $f$ is a randomized function. The *form* — dependence on exactly $(M_{\tau^-}, e_\tau)$ — is preserved. The result statement should explicitly allow stochastic $f$.

### Attack 6: Time-dependent updates

Could $f$ depend on the timestamp $\tau$ itself? Yes — consistently. The event $e_\tau$ in #form-event-driven-dynamics carries a timestamp: $e_\tau = (\text{type}, \text{channel}, \text{payload}, \tau)$. So time-dependence enters through $e_\tau$. Alternatively, the agent may maintain an internal clock as part of $M_{\tau^-}$. Either way, $f(M_{\tau^-}, e_\tau)$ accommodates time-dependence.

### Attack 7: Agents that store full history

An agent with $M_{\tau^-} \supseteq \mathcal{C}_{\tau^-}$ is entirely consistent. The model space $\mathcal{M}$ is simply large enough to include the raw history. The #form-information-bottleneck argues compression is *wise* — but the recursive update form holds regardless of compression level.

## What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Constraint C1 (arrow of time: update depends on $\tau^-$, not future events) | Physical law — not a formulation choice | Postulate (physical) |
| Constraint C2 (partial observability: update depends on $e_\tau$, not raw $\Omega_\tau$) | Scope definition of AAT | Postulate (scope-defining) |
| Constraint C3 (state completeness: $M_{\tau^-}$ summarizes the agent's relevant past) | Analytical commitment — the definition of $M$ as complete | Definition |
| Recursive form $M_\tau = f(M_{\tau^-}, e_\tau)$ | C1 + C2 + C3 | Proved (unique form compatible with the three constraints) |
| Future-dependent updates eliminated | C1 alone | Derived (direct consequence) |
| $\Omega_\tau$-dependent updates eliminated | C2 alone | Derived (direct consequence) |
| Full-history-dependent updates reducible to recursive form | C3 + any choice of $M \supseteq \mathcal{C}_{\tau^-}$ | Proved (compatibility, not elimination) |
| Markov property of the update | C3 (completeness) + recursive form | Proved (follows from C3 definition) |
| Seven attack counterexamples (simultaneous events, continuous coupling, C3 circularity, shared state, external randomness, time-dependence, full history) | Case-by-case reduction to the recursive form | Proved (each) |
| C3 is definitional, not eliminative | Analysis of what C3 asserts vs. what it rules out | Discussion-grade (clarifying observation) |

The dividing line: C1 and C2 do genuine *eliminative* work — they rule out physically or scope-excluded update forms. C3 is a *definitional commitment* that forces the Markov structure by making $M$ complete by construction; it cannot be "violated" because any apparent violation means $M$ was misspecified. The recursive form's uniqueness is therefore conditional on the three-constraint set being accepted, not on the constraints being independently inescapable — C3 in particular could be refused (yielding non-Markovian analysis), at the cost of leaving AAT's scope.

## Epistemic Status

The result is correct but partly definitional. The three constraints have different epistemic characters:

| Constraint | Character | Can it be violated? |
|------------|-----------|---------------------|
| C1 (arrow of time) | Physical law | Not in a classical universe |
| C2 (partial observability) | Scope definition | Only by leaving AAT's scope |
| C3 (state completeness) | Analytical commitment | Not without redefining $M$ |

C1 and C2 do genuine eliminative work — they rule out update forms that depend on future events or on raw $\Omega$. These are non-trivial constraints.

C3 is a definitional commitment that produces the Markov structure. It cannot be "violated" because any violation is absorbed by expanding $M$. This is not a weakness — it's the nature of the claim. The result says: *the Markovian analysis is the only one consistent with C1 + C2 + the definition of $M$ as complete*. The alternative — an update that depends on something outside $M$ — is not "wrong" but rather means $M$ was misspecified.

**What the result says:** C1 eliminates a physically impossible class of updates (future-dependent). C2 eliminates a scope-excluded class ($\Omega$-dependent). After (1) and (2), the *only remaining question* is how the past enters: through the full history $\mathcal{C}_{\tau^-}$ or through a compressed state $M_{\tau^-}$. C3 says the agent *has* a complete state, and whatever that state is, it's all the agent has. The Markov form follows.

**What the result does NOT say:** That $M$ must be a lossy compression (the agent could store full history). That the Markov property is "natural" or "optimal" (it's a consequence of how $M$ is defined). That continuous-coupling systems are event-driven (the event framework is one abstraction; $\dot{M} = g(M, u)$ is the more general one, arrived at by the same three constraints).

## Discussion

**Recursion as a consequence of completeness.** The recursive form is not an assumption bolted on — it follows from the definition of $M_t$ as complete. The sufficiency of the recursive form is precisely what #def-model-sufficiency measures: when $S(M_t) = 1$, the recursive update loses nothing.

**What this opens.** The proof yields the *form*. It immediately invites the follow-up questions that the rest of the theory addresses: What should $f$ preserve? → #form-information-bottleneck and #def-model-sufficiency. How should $f$ weight new information? → #emp-update-gain. When is $\mathcal{M}$ itself inadequate? → #result-structural-adaptation-necessity.

## Working Notes

- C3's definitional character is a feature, not a bug — but it must be stated honestly. The result is not "the update must be Markovian" but rather "the Markovian analysis is the *only* consistent one, given the modeling commitment of #form-agent-model." These sound the same but have different epistemic status.
- The continuous-coupling generalization (Attack 2) deserves a proper note somewhere: $\dot{M} = g(M, u)$ is the more general form, with event-driven updates as a special case. The three constraints produce the same argument structure in both cases.
- The information-set formalization (Doob-Dynkin) provides the cleanest technical proof. It should probably be considered the primary proof path, with the elimination argument as the more intuitive exposition.

---

[^kallenberg2002]: Kallenberg, O. (2002). *Foundations of Modern Probability* (2nd ed.). Springer. §1.2 (measurability and the Doob–Dynkin lemma).


---

