# Recursive Update Uniqueness Proof — Working Draft

**Status**: Scratch/draft. Working toward a proof suitable for inclusion in TF-02.

**Goal**: Prove that $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ is the *unique* update form consistent with directed time, partial observability, and state completeness. Not merely one option, but the only one.

---

## 1. Setup

We work within TFT's scope ($\mathcal S_{\text{TFT}}$, TF-01): an agent coupled to an environment $\Omega$ through observation and action channels, with residual uncertainty.

**Universe of information at event time $\tau$.** The following information exists (in the broadest ontological sense) at the moment event $e_\tau$ occurs:

| Information | Description |
|-------------|-------------|
| $\Omega_\tau$ | The environment state |
| $\mathcal C_{\tau^-}$ | The complete event history up to (but not including) $e_\tau$ |
| $\{M_{\tau'}\}_{\tau' \leq \tau^-}$ | The agent's prior internal states, culminating in $M_{\tau^-}$ |
| $e_\tau$ | The current event (observation arriving or action completing) |
| $\{e_{\tau'}\}_{\tau' \gt \tau}$ | Future events (not yet occurred) |

The question: of these, which can the update $M_{\tau^+}$ depend on?

## 2. The Three Constraints

**Constraint 1 — Arrow of time (TF-02 axiom).** Events are temporally ordered and this ordering is irreversible. An update occurring at time $\tau$ cannot depend on events that have not yet occurred:

$$M_{\tau^+} \text{ cannot depend on } \{e_{\tau'}\}_{\tau' \gt \tau}$$

This is a physical constraint — the most primitive one. In a classical universe, information from the future is simply not available. Even if the agent can *predict* future events, those predictions are part of $M_{\tau^-}$ (they are internal computations, not future information). Even an oracle's outputs would arrive as events $e_\tau$ through the observation channel.

**Constraint 2 — Partial observability (TF-01 scope).** The agent cannot access $\Omega_\tau$ directly. Its only interface with the environment is through the event $e_\tau$, which is a lossy function of $\Omega_\tau$ (via TF-01's observation model $o = h(\Omega, a, \varepsilon)$):

$$M_{\tau^+} \text{ cannot depend on } \Omega_\tau \text{ except through } e_\tau$$

This is a scope constraint. If the agent could access $\Omega$ directly, the residual uncertainty condition ($H(\Omega_t \mid \mathcal C_t) \gt 0$) in TF-01 would be trivially violable — the agent could simply read off the environment state. Partial observability is constitutive of TFT's scope.

**Constraint 3 — State completeness.** $M_{\tau^-}$ is the agent's *complete* internal state just before event $e_\tau$. By "complete" we mean: there is no information about the agent's past that is available to the update mechanism but not encoded in $M_{\tau^-}$.

$$M_{\tau^+} \text{ cannot depend on } \mathcal{C}_{\tau^-} \text{ or } \{M_{\tau'}\}_{\tau' \lt \tau^-} \text{ except through } M_{\tau^-}$$

This constraint deserves careful examination (see Section 4 below).

## 3. The Proof

**Theorem (Recursive Update Uniqueness).** Under Constraints 1–3, the model update at event time $\tau$ must have the form

$$M_{\tau^+} = f(M_{\tau^-}, e_\tau)$$

for some function $f: \mathcal{M} \times \mathcal{E} \to \mathcal{M}$. No other update form is consistent with the three constraints.

**Proof.** Consider the most general possible update. The updated state $M_{\tau^+}$ is a function of *all accessible information*:

$$M_{\tau^+} = F(\text{accessible information at } \tau)$$

We characterize the accessible information by eliminating what is not accessible.

**(i) Eliminate future events.** By C1 (arrow of time), $\{e_{\tau'}\}_{\tau' \gt \tau}$ is not accessible. These events have not occurred; no physical process can deliver their content to the update mechanism at time $\tau$.

After this elimination, the candidate dependency set is:
$$\{\Omega_\tau,\; \mathcal{C}_{\tau^-},\; \{M_{\tau'}\}_{\tau' \leq \tau^-},\; e_\tau\}$$

**(ii) Eliminate direct environment access.** By C2 (partial observability), the agent cannot access $\Omega_\tau$ except through the event $e_\tau$, which is a lossy function of $\Omega_\tau$ (and possibly of the agent's prior action). Any information from $\Omega_\tau$ that reaches the agent does so through $e_\tau$ — which is already in the dependency set. Dependence on $\Omega_\tau$ beyond $e_\tau$ requires access the agent does not have.

After this elimination:
$$\{\mathcal{C}_{\tau^-},\; \{M_{\tau'}\}_{\tau' \leq \tau^-},\; e_\tau\}$$

**(iii) Reduce past information to $M_{\tau^-}$.** By C3 (state completeness), $M_{\tau^-}$ is the agent's complete internal state. Every element of $\mathcal C_{\tau^-}$ and every prior model state $M_{\tau'}$ ($\tau' \lt \tau^-$) that could influence the update can do so *only through* its effect on $M_{\tau^-}$. The agent has no independent access channel to raw historical events or prior states — its sole record of the past is $M_{\tau^-}$.

To see why: the agent's internal state evolves through a sequence of updates. At each prior event $\tau_k$, the state was updated based on the then-available information. The cumulative effect of all prior events on the agent's current state is exactly $M_{\tau^-}$. The raw events $e_{\tau_1}, e_{\tau_2}, \ldots$ that produced this state are no longer separately available to the agent — they were "consumed" by the update mechanism and their information (to the extent it was retained) is now encoded in $M_{\tau^-}$.

Could the agent maintain a separate log of raw events outside of $M$? It could — but that log *is part of $M$*. Whatever information the agent retains in any form — model parameters, cached data, raw event buffers, metadata — is by definition part of its complete internal state $M_{\tau^-}$. If something is available to the update mechanism and not in $M_{\tau^-}$, then $M_{\tau^-}$ was not the complete state — contradicting C3.

After this elimination:
$$\{M_{\tau^-},\; e_\tau\}$$

Therefore:
$$M_{\tau^+} = F(M_{\tau^-}, e_\tau) \equiv f(M_{\tau^-}, e_\tau)$$

This is the unique form: no information beyond $(M_{\tau^-}, e_\tau)$ is accessible under the three constraints, so no update form depending on anything else is realizable. $\square$

**Corollary (Between-events dynamics).** Between events, no new event $e$ arrives. The same argument applies with $e_\tau$ removed from the accessible set:

$$\frac{dM}{d\tau} = g(M_\tau)$$

The agent's internal evolution between events (prediction, decay, internal simulation) depends only on the current state. No new external information arrives, so C2 contributes nothing new; C1 and C3 together yield autonomous dynamics. $\square$

**Corollary (Serial special case).** When observations and actions alternate at a uniform rate on a single channel, each event $e_t$ is the pair $(o_t, a_{t-1})$ — the observation received and the action whose consequences are now being observed. The update becomes:

$$M_t = f(M_{t-1}, o_t, a_{t-1})$$

This is the familiar discrete-time form. $\square$

## 4. Discussion: What the Proof Does and Doesn't Say

### What it says

The proof establishes that the *form* $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ is the unique update form consistent with the three constraints. Any agent operating within TFT's scope must update this way — it has no other option. The specific *function* $f$ varies enormously across agents (a Kalman filter's update differs from a neural network's), but the *argument signature* is universal.

### The role of C3 (state completeness)

C3 does the most interesting work. It is simultaneously:

- **Definitional**: "complete state" means "everything the agent has." This is tautological in isolation.
- **Substantive**: it *excludes* update mechanisms that bypass the model state — that reach into some separate information reservoir not captured by $M$. This exclusion is what gives the Markov property.
- **A modeling choice**: by adopting TF-03's definition of the model as the agent's complete internal state, we commit to analyzing the agent's dynamics as Markovian in $M$. This is the right choice for TFT because it makes $M$ the *right* object to study — but it is a choice, not a discovery.

The depth of C3 is not in the constraint itself but in its *consequences*: because $M_{\tau^-}$ must contain everything the agent retains, the quality of the update depends entirely on what $\phi$ (the compression, TF-03) chose to preserve. This is precisely what the sufficiency measure $S(M_t)$ (TF-10) quantifies: how much predictively relevant information survived compression into $M$.

### What about stochastic updates?

The update function $f$ may be stochastic: $M_{\tau^+} \sim P(\cdot \mid M_{\tau^-}, e_\tau)$. Random number generators, sampling procedures, and stochastic approximation methods all involve randomness. But the source of randomness is either:

- **Internal** (a PRNG whose state is part of $M_{\tau^-}$), in which case the update is deterministic given $M_{\tau^-}$ in its full specification; or
- **External** (thermal noise, quantum randomness), in which case the random input is either part of the event $e_\tau$ (arriving through the observation channel) or modeled as internal state.

In either case, the stochastic update $M_{\tau^+} \sim P(\cdot \mid M_{\tau^-}, e_\tau)$ is a special case of $f$, where $f$ is a randomized function. The *form* — dependence on exactly $(M_{\tau^-}, e_\tau)$ — is preserved.

### What about time-dependent updates?

Could the function $f$ depend on the timestamp $\tau$ itself? Yes — and this is consistent with the theorem. The event $e_\tau$ in the event-driven formulation (TF-04) carries a timestamp: $e_\tau = (\text{type}, \text{channel}, \text{payload}, \tau)$. So time-dependence enters through $e_\tau$. Alternatively, the agent may maintain an internal clock as part of $M_{\tau^-}$. Either way, $f(M_{\tau^-}, e_\tau)$ accommodates time-dependence without violating the form.

### What about agents that store full history?

An agent that maintains a complete log of all past events — with $M_{\tau^-} \supseteq \mathcal C_{\tau^-}$ — is entirely consistent. The model space $\mathcal{M}$ is simply large enough to include the raw history. The update $f(M_{\tau^-}, e_\tau)$ appends $e_\tau$ to the log (and possibly updates derived quantities). The theorem doesn't say the agent *must* compress; it says whatever the agent retains is $M_{\tau^-}$, and the update is a function of that plus the new event.

The information bottleneck (TF-03) argues that compression is *wise* — the Pareto-optimal trade-off between retention cost and predictive power — but the recursive update form holds regardless of compression level.

### Relationship to the Markov property

The theorem establishes that the agent's update dynamics are **Markovian in $M$** — the next state depends only on the current state and the current input, not on the history of states. This is not an assumption imposed on the agent; it is a consequence of the three constraints.

This is analogous to how any finite-state automaton has Markovian dynamics by construction: the state is *defined* as "everything the automaton remembers." The non-trivial content is that this Markov structure is the *only* structure consistent with directed time and partial observability — not merely one convenient modeling choice among many.

### Necessity of the constraints

Are all three constraints needed? Consider what happens if each is dropped:

**Without C1 (arrow of time):** An agent with access to future events could use them to pre-adjust its model. This violates basic physics but is conceivable in science fiction scenarios (time travel, precognition). In any such scenario, the update form would be $f(M_{\tau^-}, e_\tau, e_{\tau_1'}, e_{\tau_2'}, \ldots)$ — a function of both current and future events. The recursive form breaks.

**Without C2 (partial observability):** An agent with direct access to $\Omega_\tau$ could update as $f(M_{\tau^-}, \Omega_\tau)$, bypassing the observation channel entirely. The update would still be recursive (C1 + C3 ensure this), but the argument of $f$ would be $(M_{\tau^-}, \Omega_\tau)$ rather than $(M_{\tau^-}, e_\tau)$ — a much richer input. This case is outside TFT's scope by definition.

**Without C3 (state completeness):** An agent with a "side channel" to historical information not encoded in $M_{\tau^-}$ — say, a separate memory bank that the analysis doesn't include in $M$ — could update as $f(M_{\tau^-}, e_\tau, \text{side channel})$. But this just means $M$ was incorrectly specified — the side channel should have been included in $M$. C3 is unfalsifiable in this sense: it defines $M$ to be complete, and any apparent violation is a misidentification of $M$.

All three constraints are necessary for the conclusion: C1 eliminates the future, C2 eliminates direct environment access, C3 consolidates the past into $M_{\tau^-}$.

## 5. Formalization via Information Sets

For readers who prefer a measure-theoretic framing:

**Definition.** The agent's **information set** at time $\tau$ is the sigma-algebra $\mathcal I_\tau^{agent}$ — the collection of events (in the probability-theoretic sense) about which the agent can condition its update.

**C1** restricts $\mathcal I_\tau^{agent} \subseteq \sigma(\{e_{\tau'} : \tau' \leq \tau\} \cup \{\Omega_\tau\} \cup \{M_{\tau'} : \tau' \leq \tau^-\})$ — no future information.

**C2** further restricts: $\sigma(\Omega_\tau) \setminus \sigma(e_\tau)$ is not in $\mathcal I_\tau^{agent}$ — the agent cannot condition on aspects of $\Omega_\tau$ that are not captured by $e_\tau$.

**C3** further restricts: $\sigma(\{e_{\tau'} : \tau' \lt \tau\} \cup \{M_{\tau'} : \tau' \lt \tau^-\}) \subseteq \sigma(M_{\tau^-})$ from the agent's perspective — all past information accessible to the agent is subsumed by $M_{\tau^-}$.

After all three restrictions:
$$\mathcal{I}_\tau^{agent} = \sigma(M_{\tau^-}, e_\tau)$$

The update $M_{\tau^+}$ must be $\mathcal I_\tau^{agent}$-measurable. By the Doob–Dynkin lemma, any $\sigma(M_{\tau^-}, e_\tau)$-measurable random variable is a (Borel) function of $(M_{\tau^-}, e_\tau)$. Therefore $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ for some measurable $f$. $\square$

## 6. What This Opens

The proof yields the *form*. It immediately invites the follow-up questions that the rest of TFT addresses:

- **What should $f$ preserve?** → The information bottleneck (TF-03) and sufficiency measure (TF-10)
- **How should $f$ weight new information?** → The update gain (TF-06)
- **How much does each application of $f$ lose?** → The per-step information loss question (TF-10, open)
- **When is $\mathcal{M}$ itself inadequate?** → Structural adaptation (TF-10, Prop 10.1)

The recursive update uniqueness is the formal foundation that makes all of these questions well-posed.

---

## 7. Attempts to Break the Result

Before trusting the proof, try to construct counterexamples — update forms that are *not* $f(M_{\tau^-}, e_\tau)$ but seem legitimate.

### Attack 1: Simultaneous events

Two events arrive at exactly the same time: $e_\tau^{(1)}$ and $e_\tau^{(2)}$. The update is:
$$M_{\tau^+} = f(M_{\tau^-}, e_\tau^{(1)}, e_\tau^{(2)})$$

This has *three* arguments. Is the theorem broken?

**Assessment:** Not really — but it exposes a silent assumption. The theorem assumes events are atomic and sequential. If multiple events can arrive simultaneously, we either:
- Define the "event" as the *bundle* of simultaneous arrivals: $e_\tau = (e_\tau^{(1)}, e_\tau^{(2)})$. Then the form is preserved — but now we're adjusting the definition of $\mathcal{E}$ to save the theorem.
- Accept that the update has a variable-arity signature, and the theorem is stating something about the structure of *sequential* processing.

**Verdict:** Not a deep counterexample but reveals that "event" needs to be defined carefully. In TF-04's formulation, events are already atomic by definition. If we allow bundled events, the form holds with $e_\tau$ as a set. This should be acknowledged, not swept under the rug.

### Attack 2: Continuous environmental influence

An agent embedded in a physical system experiences continuous forces — gravity, temperature, electromagnetic fields. These aren't "events" in TF-04's sense; they're continuous signals. The true dynamics are:

$$\frac{dM}{d\tau} = g(M_\tau, \text{continuous environment signal}(\tau))$$

This violates the claim that between-events dynamics are $dM/d\tau = g(M_\tau)$.

**Assessment:** This is a real tension. The event-driven formulation assumes all environment-agent interaction occurs through discrete events. A continuous signal can be modeled as a stream of events at arbitrarily high rate, but this is a modeling choice, not a physical fact. A truly continuous agent-environment coupling doesn't fit neatly into the event framework.

**Verdict:** Genuine limitation of the event-driven formulation. The between-events corollary $dM/d\tau = g(M_\tau)$ holds only when the agent is truly isolated between events. For continuous coupling, the dynamics are $dM/d\tau = g(M_\tau, o(\tau))$ where $o(\tau)$ is the continuous observation stream — which is still consistent with the *spirit* of the theorem (the update depends on current state plus current input) but not with the discrete event *letter*.

The honest conclusion: the theorem's event-driven form is the right abstraction for digital/sampled systems. For continuous systems, the analogous result is the more general **state-space representation** $\dot{M} = g(M, u)$ from control theory, where $u$ is the continuous input. The same three constraints yield this form. The event-driven version is a special case, not the most general statement.

### Attack 3: The C3 circularity

C3 defines $M$ as the agent's complete internal state. Any apparent counterexample is dissolved by expanding $M$ to include whatever additional information the counterexample uses. This makes the proof unfalsifiable.

Consider: an agent has a "model" (weights of a neural net) and a "replay buffer" (stored raw events). The update uses both:
$$M_{\tau^+} = f(\text{weights}_{\tau^-}, \text{buffer}_{\tau^-}, e_\tau)$$

Is this a counterexample? No — C3 says $M = (\text{weights}, \text{buffer})$. The model space is just larger than you thought.

**Assessment:** This is the deepest objection. The proof is essentially:
1. Define $M$ to be everything the agent has. (C3)
2. Observe that the update can only use what the agent has. (tautology)
3. Therefore the update is $f(M_{\tau^-}, e_\tau)$. (QED)

The real content is not the mathematical argument but the *analytical commitment*: by defining $M$ as complete, we commit to Markovian analysis, which then makes $S$ (sufficiency) the right quality metric. The theorem's value is in showing that *once you make this commitment*, no alternative update form exists — but the commitment itself is a modeling choice, not a theorem about reality.

**Verdict:** C3 is not a constraint in the same sense as C1 (physical) and C2 (scope). It is a definitional commitment that produces the Markov structure as a consequence. This should be stated honestly. The theorem is not "the update must be Markovian" but rather "the Markovian analysis is the *only* consistent one, given that we define $M$ as the complete state." These sound the same but have different epistemic status.

### Attack 4: Shared state between agents

Agent A and Agent B share a common memory bank (think: shared database, Google Docs, shared filesystem). When Agent A updates, it reads from and writes to the shared memory. The shared memory is not "A's state" or "B's state" — it's a third entity.

$$M_A^{\tau^+} = f(M_A^{\tau^-}, e_\tau, \text{shared\-mem}_{\tau^-})$$

**Assessment:** C3 absorbs this by saying $M_A$ should include A's portion of the shared memory. But if the shared memory is *truly shared* (both agents read and write it concurrently), it's unclear whose state it belongs to. The clean resolution is the multi-agent framework (Appendix F): the shared memory is part of the *composite* system's state, and each agent's interaction with it is mediated by events (reads and writes).

**Verdict:** Not a true counterexample but highlights that C3 requires careful delineation of agent boundaries. In multi-agent settings, the agent-environment boundary (TF-01) must be drawn to include all state the agent has direct access to. The shared memory is either: (a) part of A's model (if A has sole access), (b) part of the environment (if A accesses it through observation/action channels), or (c) reveals that "Agent A" is not the right unit of analysis — the composite (A + shared memory + B) is.

### Attack 5: External randomness not in $e_\tau$

Suppose the agent's update uses thermal noise from its hardware — randomness that isn't an observation of the environment and isn't part of $M_{\tau^-}$:

$$M_{\tau^+} = f(M_{\tau^-}, e_\tau, \text{hardware\-noise}_\tau)$$

**Assessment:** Where does hardware noise live in the ontology?
- If it's modeled as part of the agent's internal state ($M$ includes RNG state), it's deterministic.
- If it's modeled as an external input, it should be an event — the agent is "observing" its own hardware noise.
- If it's truly random and external, the update is *stochastic*: $M_{\tau^+} \sim P(\cdot \mid M_{\tau^-}, e_\tau)$.

The stochastic case is addressed in Section 4 — the *form* is still "depends on $(M_{\tau^-}, e_\tau)$" even if the dependence is probabilistic. But this attack highlights that "function" in the theorem should be read as "possibly stochastic mapping" (kernel), not "deterministic function."

**Verdict:** Not a counterexample, but the theorem statement should explicitly allow stochastic $f$.

### Attack 6: Update depends on *how long* since last event

An event arrives at time $\tau$. The agent hasn't received an event since $\tau_{prev}$. The update depends on $\Delta\tau = \tau - \tau_{prev}$:

$$M_{\tau^+} = f(M_{\tau^-}, e_\tau, \Delta\tau)$$

Is $\Delta\tau$ part of $e_\tau$? Part of $M_{\tau^-}$?

**Assessment:** Either:
- The agent has an internal clock (part of $M_{\tau^-}$) that records $\tau_{prev}$, so $\Delta\tau$ is computable from $M_{\tau^-}$ and the timestamp in $e_\tau$.
- $\Delta\tau$ is supplied as part of the event metadata (part of $e_\tau$).
- The between-events evolution $dM/d\tau = g(M_\tau)$ already handles time-dependent drift — by the time $e_\tau$ arrives, $M_{\tau^-}$ already reflects the elapsed time.

**Verdict:** Absorbed by existing mechanisms. But this is a good example of how "$M$ is complete" does real work — it forces us to include the clock in the model.

## 8. Revised Assessment

After attempting to break the result, I find that:

**The theorem is correct but partly definitional.** The three constraints have different epistemic characters:

| Constraint | Character | Can it be violated? |
|------------|-----------|---------------------|
| C1 (arrow of time) | Physical law | Not in a classical universe |
| C2 (partial observability) | Scope definition | Only by leaving TFT's scope |
| C3 (state completeness) | Analytical commitment | Not without redefining $M$ |

C1 and C2 do genuine eliminative work — they rule out update forms that depend on future events or on raw $\Omega$. These are non-trivial constraints.

C3 is a definitional commitment that produces the Markov structure. It cannot be "violated" because any violation is absorbed by expanding $M$. This is not a weakness — it's the nature of the claim. The theorem says: *the Markovian analysis is the only one consistent with C1 + C2 + the definition of $M$ as complete*. The alternative — an update that depends on something outside $M$ — is not "wrong" but rather means $M$ was misspecified.

**The genuine content of the theorem is:**
1. C1 eliminates a physically impossible class of updates (future-dependent).
2. C2 eliminates a scope-excluded class ($\Omega$-dependent).
3. After (1) and (2), the *only remaining question* is how the past enters: through the full history $\mathcal C_{\tau^-}$ or through a compressed state $M_{\tau^-}$. C3 says the agent *has* a complete state, and whatever that state is, it's all the agent has. The Markov form follows.

The theorem does NOT say:
- That $M$ must be a lossy compression (the agent could store full history)
- That the Markov property is "natural" or "optimal" (it's a consequence of how $M$ is defined)
- That continuous-coupling systems are event-driven (the event framework is one abstraction; continuous state-space $\dot{M} = g(M, u)$ is the more general one, arrived at by the same three constraints)

**What should go in TF-02:** An honest version that:
1. States the three constraints clearly, with their different characters labeled
2. Shows the elimination argument
3. Acknowledges that C3 is definitional, not physical — and that this is by design
4. Notes the continuous-coupling generalization
5. Positions the result as establishing *why Markovian analysis is the right framework*, not as discovering a surprising fact about update mechanisms

---

## Notes for Integration into TF-02

The proof is ready for integration in revised form. Key changes from the first draft:
- Acknowledge C3's definitional character explicitly, rather than presenting all three constraints as independent physical/scope constraints
- Add a note about continuous-coupling systems (the event-driven form is a special case of the general state-space form $\dot{M} = g(M, u)$)
- State $f$ as a possibly stochastic mapping
- Frame the result's value correctly: not "surprising uniqueness" but "the Markovian framework is the only consistent one under C1 + C2 + the modeling commitment of TF-03"
