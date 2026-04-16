---
slug: recursive-update-derivation
type: derivation
status: exact
depends:
  - agent-model
  - event-driven-dynamics
  - causal-structure
  - scope-condition
  - observation-function
stage: claims-verified
---

# Derivation: Recursive Update — Uniqueness Derivation

Derivation showing that $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ is the *unique* update form consistent with directed time, partial observability, and state completeness. Not merely one option, but the only one.

## Setup

We work within ACT's scope ( #scope-condition): an agent coupled to an environment $\Omega$ through observation and action channels, with residual uncertainty.

**Universe of information at event time $\tau$.** The following information exists (in the broadest ontological sense) at the moment event $e_\tau$ occurs:

| Information | Description |
|-------------|-------------|
| $\Omega_\tau$ | The environment state |
| $\mathcal{C}_{\tau^-}$ | The complete interaction history ( #chronica) up to (but not including) $e_\tau$ |
| $\{M_{\tau'}\}_{\tau' \leq \tau^-}$ | The agent's prior internal states, culminating in $M_{\tau^-}$ |
| $e_\tau$ | The current event (observation arriving or action completing) |
| $\{e_{\tau'}\}_{\tau' \gt \tau}$ | Future events (not yet occurred) |

The question: of these, which can the update $M_{\tau^+}$ depend on?

## The Three Constraints

**Constraint 1 — Arrow of time ( #causal-structure postulate).** Events are temporally ordered and this ordering is irreversible. An update occurring at time $\tau$ cannot depend on events that have not yet occurred:

$$M_{\tau^+} \text{ cannot depend on } \{e_{\tau'}\}_{\tau' \gt \tau}$$

This is a physical constraint — the most primitive one. In a classical universe, information from the future is simply not available. Even if the agent can *predict* future events, those predictions are part of $M_{\tau^-}$ (they are internal computations, not future information).

**Constraint 2 — Partial observability ( #scope-condition).** The agent cannot access $\Omega_\tau$ directly. Its only interface with the environment is through the event $e_\tau$, which is a lossy function of $\Omega_\tau$ (via #observation-function):

$$M_{\tau^+} \text{ cannot depend on } \Omega_\tau \text{ except through } e_\tau$$

This is a scope constraint. If the agent could access $\Omega$ directly, the residual uncertainty condition in #scope-condition would be trivially violable.

**Constraint 3 — State completeness ( #agent-model).** $M_{\tau^-}$ is the agent's *complete* internal state just before event $e_\tau$. There is no information about the agent's past that is available to the update mechanism but not encoded in $M_{\tau^-}$:

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

By the Doob–Dynkin lemma, any $\sigma(M_{\tau^-}, e_\tau)$-measurable random variable is a (Borel) function of $(M_{\tau^-}, e_\tau)$. Therefore $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ for some measurable $f$. $\square$

## Attempts to Break the Result

Before trusting the proof, seven counterexample attacks:

### Attack 1: Simultaneous events

Two events arrive at exactly the same time: $e_\tau^{(1)}$ and $e_\tau^{(2)}$. The update has three arguments: $f(M_{\tau^-}, e_\tau^{(1)}, e_\tau^{(2)})$.

**Verdict:** Not deep — #event-driven-dynamics defines events as atomic. If we allow bundled events, the form holds with $e_\tau$ as a set. Reveals that "event" needs careful definition, but the form is preserved.

### Attack 2: Continuous environmental influence

An agent embedded in a physical system experiences continuous forces (gravity, temperature, electromagnetic fields). These aren't "events" in #event-driven-dynamics's sense; they're continuous signals. The true dynamics would be $dM/d\tau = g(M_\tau, o(\tau))$ where $o(\tau)$ is a continuous observation stream.

**Verdict:** Genuine limitation of the event-driven formulation. The between-events corollary $dM/d\tau = g(M_\tau)$ holds only when the agent is truly isolated between events. For continuous coupling, the analogous result is the general state-space representation $\dot{M} = g(M, u)$ from control theory — arrived at by the same three constraints. The event-driven version is a special case for digital/sampled systems.

### Attack 3: The C3 circularity

C3 defines $M$ as the agent's complete internal state. Any apparent counterexample is dissolved by expanding $M$. Consider: an agent has a "model" (neural net weights) and a "replay buffer" (stored raw events). C3 says $M = (\text{weights}, \text{buffer})$. The model space is just larger than you thought.

**Verdict:** The deepest objection. The proof essentially: (1) Define $M$ to be everything the agent has. (2) Observe the update can only use what the agent has. (3) Therefore $f(M_{\tau^-}, e_\tau)$. The real content is the *analytical commitment*: by defining $M$ as complete, we commit to Markovian analysis, which then makes #model-sufficiency the right quality metric. See Epistemic Status below.

### Attack 4: Shared state between agents

Agents A and B share a common memory bank (shared database). The clean resolution is the multi-agent framework: the shared memory is part of the *composite* system's state, and each agent's interaction with it is mediated by events (reads and writes). Not a true counterexample but highlights that C3 requires careful delineation of agent boundaries.

### Attack 5: External randomness not in $e_\tau$

Hardware thermal noise used in the update. The stochastic case $M_{\tau^+} \sim P(\cdot \mid M_{\tau^-}, e_\tau)$ is a special case of $f$ where $f$ is a randomized function. The *form* — dependence on exactly $(M_{\tau^-}, e_\tau)$ — is preserved. The result statement should explicitly allow stochastic $f$.

### Attack 6: Time-dependent updates

Could $f$ depend on the timestamp $\tau$ itself? Yes — consistently. The event $e_\tau$ in #event-driven-dynamics carries a timestamp: $e_\tau = (\text{type}, \text{channel}, \text{payload}, \tau)$. So time-dependence enters through $e_\tau$. Alternatively, the agent may maintain an internal clock as part of $M_{\tau^-}$. Either way, $f(M_{\tau^-}, e_\tau)$ accommodates time-dependence.

### Attack 7: Agents that store full history

An agent with $M_{\tau^-} \supseteq \mathcal{C}_{\tau^-}$ is entirely consistent. The model space $\mathcal{M}$ is simply large enough to include the raw history. The #information-bottleneck argues compression is *wise* — but the recursive update form holds regardless of compression level.

## Epistemic Status

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

## Discussion

**Recursion as a consequence of completeness.** The recursive form is not an assumption bolted on — it follows from the definition of $M_t$ as complete. The sufficiency of the recursive form is precisely what #model-sufficiency measures: when $S(M_t) = 1$, the recursive update loses nothing.

**What this opens.** The proof yields the *form*. It immediately invites the follow-up questions that the rest of the theory addresses: What should $f$ preserve? → #information-bottleneck and #model-sufficiency. How should $f$ weight new information? → #update-gain. When is $\mathcal{M}$ itself inadequate? → #structural-adaptation-necessity.

## Working Notes

- C3's definitional character is a feature, not a bug — but it must be stated honestly. The result is not "the update must be Markovian" but rather "the Markovian analysis is the *only* consistent one, given the modeling commitment of #agent-model." These sound the same but have different epistemic status.
- The continuous-coupling generalization (Attack 2) deserves a proper note somewhere: $\dot{M} = g(M, u)$ is the more general form, with event-driven updates as a special case. The three constraints produce the same argument structure in both cases.
- The information-set formalization (Doob-Dynkin) provides the cleanest technical proof. It should probably be considered the primary proof path, with the elimination argument as the more intuitive exposition.

*(Descended from TFT Appendix: Recursive Update Uniqueness Derivation.)*
