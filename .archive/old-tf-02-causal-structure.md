# TF-02: Causal Structure (Axiom)

The agent-environment coupling has an irreducible **causal structure** grounded in the temporal ordering of events. Actions precede their consequences; observations follow from the state they observe. This ordering is constitutive of the feedback loop and holds independent of the magnitude of the agent's influence on the environment.

## The Temporal Arrow

The interaction history $\mathcal C_t$ is not merely a set of observations and actions — it is an *ordered sequence* in which temporal position carries meaning:

*[Definition]*
$$\mathcal{C}_t = (o_1, a_1, o_2, a_2, \ldots, a_{t-1}, o_t)$$

The ordering is not a notational convenience. It reflects an irreversible physical fact: $a_{t-1}$ was selected before $o_t$ was received. The agent could not have used $o_t$ to select $a_{t-1}$. This asymmetry — **the arrow of time** — is the foundation of causal structure in the theory.

## Causality as Temporal Ordering

We adopt the most primitive notion of causality: **event $A$ can be a cause of event $B$ only if $A$ temporally precedes $B$.** This is weaker than (and prior to) statistical notions of causality:

**Temporal causality** (this axiom): $A$ precedes $B$; $A$ is in $B$'s causal past. This holds regardless of whether $A$ actually influenced $B$. It is a statement about the *structure of possible influence*, not about actual influence.

**Statistical/functional causality** (derived, when applicable): Intervening to change $A$ changes the distribution of $B$. This requires coupling — the agent's actions must actually affect the environment. It may be strong (a robot pushing an object), weak (a scientist publishing a paper), or nominal (an observer whose actions barely perturb the system).

**Counterfactual causality** (derived, requires model): Had $A$ been different, $B$ would have been different. This requires the agent to maintain a model capable of counterfactual reasoning — a Level 3 capability in Pearl's hierarchy.

The temporal notion is the most primitive because it survives even when statistical influence is negligible. An agent passively observing a system with minimal intervention still has a causal history — the temporal ordering of its observations and (minimal) actions still structures what it can learn and when. The feedback loop's power does not *require* strong environmental coupling, though it benefits from it.

## The Three Levels of Epistemic Access

From this causal foundation, three levels of epistemic access emerge (following Pearl's causal hierarchy[^pearl2009][^bareinboim2022], but grounded here in temporal structure):

**Level 1 — Associational**: $P(o_t \mid \mathcal C_{\ltt})$

*What will I observe next, given what I've observed before?*

This is pattern recognition over the temporally ordered history. Available to any agent that maintains a model (TF-03), including purely passive observers. The temporal ordering constrains which associations are meaningful: $o_3$ can depend on $o_1, a_1, o_2, a_2$ but not on $o_4$.

**Level 2 — Interventional**: $P(o_t \mid do(a_{t-1}), M_{t-1})$

*What will I observe if I* do *this?*

The $do(\cdot)$ operator marks the crucial distinction: this is not "what observation tends to follow this action in the historical record" (associational) but "what will happen *because* I take this action now." This requires that:
1. The agent's action temporally precedes the observation (causal structure — this axiom)
2. The agent chose the action (it was not determined by the same causes that determine the observation)
3. The environment's response carries information about the *causal* relationship between action and outcome

Level 2 is why the feedback loop is more powerful than passive observation. By *acting* and then observing consequences, the agent obtains information about causal mechanisms — not merely about correlations. The mismatch signal $\delta_t = o_t - \hat o_t(M_{t-1}, a_{t-1})$, conditioned on the agent's own action, is an *interventional* signal. It tells the agent something about the causal structure of the environment that no amount of passive observation can provide.

**Level 3 — Counterfactual**: $P(o_t^{a'} \mid a_{t-1} = a, o_t = o)$

*Given that I did $a$ and observed $o$, what* would *I have observed if I had done $a'$ instead?*

This requires the model to simulate alternative histories — to run the causal structure "backward" and then "forward" under different interventions. It is the most demanding epistemic level and the basis for:
- Regret computation in RL (how much better would the alternative have been?)
- Boyd's mental simulation of alternative strategies
- Scientific reasoning about controlled experiments from observational data
- Moral reasoning (what would have happened if I had acted differently?)

Note that *forward-looking* deliberation — comparing candidate actions before choosing — primarily exercises Level 2 (iterated mental intervention), shading into Level 3 when the agent evaluates past choices to refine the comparison. See TF-07 and TF-08 for the full treatment of deliberation as interventional and counterfactual simulation.

**Availability vs. exploitation.** The three levels describe the epistemic access that the causal structure *makes available* — not what any particular agent *uses*. Many systems within TFT's scope operate primarily or exclusively at Level 1. A Kalman filter coupled with an LQR controller has actions that causally affect the environment, and its innovation signal is technically conditioned on its prior action (through the prediction $\hat x_{t|t-1} = A\hat x_{t-1} + B a_{t-1}$). Level 2 access is structurally present. But the separation principle guarantees that the estimation quality is invariant to the control policy — the system does not *exploit* the interventional structure of its observations for informational purposes. It operates at Level 1 in practice. Only dual control[^feldbaum1960] — choosing actions partly for their informational value, breaking the separation principle — exercises Level 2 access in the Kalman domain. Similarly, a PID controller has no deliberative capacity and no counterfactual reasoning; it operates entirely at Level 1. The levels characterize the *structure of possible epistemic access* inherent in any feedback loop, not the capabilities of any specific agent. Which levels an agent actually exercises depends on its architecture and model class ($\mathcal{M}$).

## Why This Is an Axiom

The temporal ordering of events is not derived from the other axioms — it is a physical fact about the universe that the theory takes as given. The second law of thermodynamics, the light-cone structure of relativity, and the arrow of psychological time all enforce it, but TFT does not derive it from any of these. It is simply noted as a precondition: the theory applies to agents embedded in a universe where time has a direction.

## The Recursive Update

The causal structure constrains how an agent can update its internal state. Three constraints jointly determine the update form:

1. **The arrow of time** (this axiom): The updated state cannot depend on future events — only on what has already occurred. This is a physical constraint.
2. **Partial observability** (TF-01): The agent cannot access $\Omega$ directly — only through lossy observations. This is a scope constraint.
3. **State completeness** (TF-03): $M$ is the agent's *complete* internal state — whatever the agent retains in any form (parameters, buffers, caches, metadata) is by definition part of $M$. This is an analytical commitment, not a physical constraint: by defining $M$ as the agent's complete state, we commit to Markovian analysis. Any apparent "side channel" to historical information not in $M$ simply indicates that $M$ was misspecified.

### The general form

Under these three constraints, the most general causal-respecting update is:

*[Derived (recursive-update, general)]*
$$\dot{M}(\tau) = g(M(\tau),\, u(\tau))$$

where $u(\tau)$ is whatever input the agent receives from the environment at time $\tau$. This is the standard state-space representation from control theory[^kailath1980]. C1 forbids dependence on future inputs. C2 restricts $u(\tau)$ to observable quantities (not raw $\Omega$). C3 eliminates dependence on prior states — they are subsumed by $M(\tau)$.

This continuous form applies to agents with continuous environmental coupling: physical systems subject to forces, sensors with continuous readout, analog controllers. For such systems, the "between events" distinction does not arise — the agent is always receiving input.

### The event-driven special case

TFT's primary formulation assumes agent-environment interaction occurs through discrete **events** (TF-04) — observations arriving and actions completing at specific times, with the agent isolated between events. This is the natural abstraction for digital systems, sampled-data controllers, message-passing agents, and organisms whose sensory processing is neurally discretized. Under this assumption, $u(\tau)$ is zero between events and impulsive at event times, yielding:

*[Derived (recursive-update, event-driven)]*
$$M_{\tau^+} = f(M_{\tau^-}, e_\tau)$$

where $M_{\tau^-}$ is the model state just before the event and $M_{\tau^+}$ is the state just after. Between events, no new external information arrives, so autonomous evolution depends only on the current state:

$$\frac{dM}{d\tau} = g(M_\tau) \qquad \text{(between events)}$$

The serial single-channel special case, where observations and actions alternate at a uniform rate, recovers the familiar form:

*[Derived (recursive-update, serial special case)]*
$$M_t = f(M_{t-1}, o_t, a_{t-1})$$

See TF-04 for the multi-channel, multi-rate event framework.

### Uniqueness

Once you commit to analyzing the agent as having a complete state $M$ (constraint 3), the Markovian update form is the only one consistent with directed time and partial observability. The argument:

- **Eliminate future information** (C1): The update cannot depend on events that have not yet occurred. Any "predictions" of future events are computations already reflected in $M$.
- **Eliminate direct $\Omega$ access** (C2): Information about $\Omega$ reaches the agent only through $u(\tau)$ (or $e_\tau$ in the event-driven case).
- **Consolidate past into $M$** (C3): All prior events and prior states are accessible only through their cumulative effect on the current state $M$. The agent has no separate channel to raw history.

After these eliminations, the only information available to the update is $(M, u)$ — or $(M_{\tau^-}, e_\tau)$ in the event-driven case. The Doob–Dynkin lemma gives the formal conclusion: any update measurable with respect to $\sigma(M_{\tau^-}, e_\tau)$ must be a function of $(M_{\tau^-}, e_\tau)$.

The three constraints have different characters — C1 is physical, C2 is from the scope definition, C3 is a modeling commitment — but they are jointly necessary: dropping any one permits update forms the others cannot eliminate. See `scratch/recursive-update-uniqueness-proof.md` for the full analysis, including attempted counterexamples.

### What this result establishes

The recursive form follows from the temporal axiom, the scope definition, and TF-03's modeling commitment — not from the model's quality as a sufficient statistic. How *good* the recursion is — how much information each step loses compared to (infeasible) batch reprocessing — is a separate question, addressed by the sufficiency apparatus ($S$, $\mathcal{F}$) introduced in TF-10.

## Consequences for the Feedback Loop

The irreversibility of temporal ordering, combined with the recursive update, yields the core structure of the feedback loop:

- The model update is **directed** — the model at time $t$ depends on prior events, never on future ones
- The mismatch signal $\delta_t$ is **retrospective** — it compares a prediction (made before $o_t$) with an observation (arriving after)
- Action selection $a_t = \pi(M_t)$ is **prospective** — it uses the current model to influence future events
- The interaction history $\mathcal C_t$ is a **monotonically growing** causal record — events are added but never removed

## Causal Structure Independent of Coupling Strength

A critical property: the causal structure of the feedback loop is preserved even when the agent's actions have minimal or nominal effect on the environment:

**Strong coupling** ($a_t$ significantly affects $\Omega_{t+1}$): Robot manipulation, military action, organizational decisions. Interventional information is rich; Level 2 epistemic access is highly productive.

**Weak coupling** ($a_t$ marginally affects $\Omega_{t+1}$): Scientific observation (the act of measuring slightly perturbs), financial markets (a small trader's effect on prices), early-stage AI agents. Interventional information is sparse but non-zero; the causal structure still enables learning that passive observation cannot.

**Nominal coupling** ($a_t$ negligibly affects $\Omega_{t+1}$): An observer with nearly zero environmental impact. The causal structure degenerates toward Level 1, but the temporal ordering of the agent's *own* actions and observations still matters — the agent's *choice* of what to observe and when (even if it doesn't change the environment) structures what it learns.

**Zero coupling** ($T(\Omega_{t+1} \mid \Omega_t, a_t) = T(\Omega_{t+1} \mid \Omega_t)$ for all $a_t$): The agent's actions do not affect the environment state. Level 2 access vanishes — different actions produce the same outcome distribution, so no interventional contrast exists. The feedback "loop" collapses to a one-way channel. Note that this case is still *within scope* when $|\mathcal{A}| \geq 2$ (TF-01), since the agent does choose among actions — but those choices produce no causal information about the environment. The theory's action-dependent results (TF-07, TF-08 adversarial dynamics) become trivially void, but the model (TF-03), mismatch (TF-05), and update gain (TF-06) still apply to the passive learning case. Systems with $|\mathcal{A}| \lt 2$ (passive observers, single-action agents) are outside TFT's scope entirely (TF-01).

The theory should not be understood as applying only to agents with strong environmental control. The causal structure of the temporal ordering alone is sufficient for the core results.

## Implications for Model Updating

The causal axiom constrains the update rule (TF-06) in a specific way: the model should give more weight to observations that are **causally downstream** of the agent's actions than to observations that would have occurred regardless. This is because action-contingent observations carry interventional (Level 2) information, while action-independent observations carry only associational (Level 1) information. The formal measure of this distinction — **causal information yield** (CIY) — is developed in TF-08, where it enters the exploration-exploitation framework.

## Agent Identity and Temporal Continuity

The causal structure has implications for agent identity: an agent's causal history $\mathcal C_t$ is a singular, non-forkable trajectory. This observation, including a precise statement of the "clone problem," is developed in [Appendix G](Appendix-G-Agent-Identity.md). It is discussion-grade and not required for the formal theorem chain.

---

[^pearl2009]: Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
[^bareinboim2022]: Bareinboim, E., Correa, J. D., Ibeling, D., & Icard, T. (2022). "Pearl's Hierarchy and the Foundations of Causal Inference." In *Probabilistic and Causal Inference* (eds. Geffner et al.).
[^kailath1980]: Kailath, T. (1980). *Linear Systems*. Prentice-Hall. The state-space representation $\dot{x} = f(x, u)$, $y = h(x)$ is the standard framework for continuous-time dynamic systems. TFT's recursive update is the event-driven discrete counterpart.
[^feldbaum1960]: Feldbaum, A. A. (1960). "Dual control theory I–IV." *Avtomatika i Telemekhanika*, 21(9).
