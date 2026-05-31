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

# Derivation: Recursive Update — Uniqueness Derivation

Appendix derivation backing #der-recursive-update. The claim being established is *uniqueness*: under three constraints — arrow of time, partial observability, and state completeness — the recursive form $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ is the only update form realizable, not merely one consistent option. The structure is an elimination argument over the universe of information potentially accessible at event time $\tau$: the environment state, the full chronica, all prior model states, the current event $e_\tau$, and future events.

The three constraints do different kinds of work. **C1 (arrow of time, from #post-causal-structure)** rules out dependence on future events: in a classical universe such information is simply not accessible, and predictions about the future, however accurate, are internal computations belonging to $M_{\tau^-}$, not future information. **C2 (partial observability, from #scope-adaptive-system and #def-observation-function)** rules out direct access to $\Omega_\tau$ except through the lossy observation channel $e_\tau$. **C3 (state completeness, from #form-agent-model)** compresses all prior-past information — the full chronica and every earlier model state — into $M_{\tau^-}$, because by construction $M$ is the agent's complete internal state and any information available to the update but not in $M$ would mean $M$ was misspecified. After all three eliminations only $(M_{\tau^-}, e_\tau)$ remains in the dependency set. A measure-theoretic version via the Doob–Dynkin lemma — restricting the agent's sigma-algebra to $\sigma(M_{\tau^-}, e_\tau)$ — gives a cleaner technical proof.

The derivation then mounts seven adversarial attacks to test whether the result really holds. Simultaneous events are absorbed by treating the bundle as a single $e_\tau$ (form preserves). Continuous environmental coupling is genuinely outside the event-driven formulation — but the analogous result reached by the same three-constraint argument in continuous time is the state-space representation $\dot{M} = g(M, u)$ from classical control theory, so the underlying structure survives. The objection that C3 is circular — anything not in $M$ gets absorbed into $M$ by definition — is acknowledged as the deepest objection, and the derivation is explicit about it: the real content is an *analytical commitment* that by defining $M$ as complete one commits to Markovian analysis, which then makes #def-model-sufficiency the right quality metric. Shared state, external randomness, time-dependence, and agents that store full history each reduce to the recursive form by appropriate enlargement of the model space or interpretation of $f$.

The honest epistemic accounting at the end is load-bearing. **C1** (physical postulate) and **C2** (scope definition) do *eliminative* work — they rule out physically impossible and scope-excluded update forms. **C3** (analytical commitment) does not eliminate; it is *definitional* and cannot be "violated" because any apparent violation is absorbed by expanding $M$. The recursive form's uniqueness is therefore conditional on accepting the three-constraint set, not on the constraints being independently inescapable — C3 in particular *could* be refused, at the cost of leaving AAT's scope and accepting non-Markovian analysis. The Markov property is not a discovered law of adaptive systems but the unique form compatible with the modeling commitment of #form-agent-model.

## Setup

We work within AAT's scope ( #scope-adaptive-system): an agent coupled to an environment $\Omega$ through observation and action channels, with residual uncertainty.

**Universe of information at event time $\tau$.** The following information exists (in the broadest ontological sense) at the moment event $e_\tau$ occurs:

| Information | Description |
|-------------|-------------|
| $\Omega_\tau$ | The environment state |
| $\mathcal C_{\tau^-}$ | The complete interaction history ( #def-chronica) up to (but not including) $e_\tau$ |
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

**(iii) Reduce past information to $M_{\tau^-}$.** By C3 (state completeness), $M_{\tau^-}$ is the agent's complete internal state. Every element of $\mathcal C_{\tau^-}$ and every prior model state $M_{\tau'}$ ($\tau' \lt \tau^-$) that could influence the update can do so *only through* its effect on $M_{\tau^-}$. The agent's internal state evolves through a sequence of updates; the cumulative effect of all prior events is exactly $M_{\tau^-}$. The raw events that produced this state are no longer separately available — they were "consumed" by the update mechanism and their information (to the extent it was retained) is now encoded in $M_{\tau^-}$.

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

The agent's **information set** at time $\tau$ is the sigma-algebra $\mathcal I_\tau^{agent}$ — the collection of events (in the probability-theoretic sense) about which the agent can condition its update.

- **C1** restricts $\mathcal I_\tau^{agent} \subseteq \sigma(\{e_{\tau'} : \tau' \leq \tau\} \cup \{\Omega_\tau\} \cup \{M_{\tau'} : \tau' \leq \tau^-\})$ — no future information.
- **C2** further restricts: $\sigma(\Omega_\tau) \setminus \sigma(e_\tau)$ is not in $\mathcal I_\tau^{agent}$ — the agent cannot condition on aspects of $\Omega_\tau$ not captured by $e_\tau$.
- **C3** further restricts: $\sigma(\{e_{\tau'} : \tau' \lt \tau\} \cup \{M_{\tau'} : \tau' \lt \tau^-\}) \subseteq \sigma(M_{\tau^-})$ from the agent's perspective.

After all three restrictions: $\mathcal I_\tau^{agent} = \sigma(M_{\tau^-}, e_\tau)$.

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

An agent with $M_{\tau^-} \supseteq \mathcal C_{\tau^-}$ is entirely consistent. The model space $\mathcal{M}$ is simply large enough to include the raw history. The #form-information-bottleneck argues compression is *wise* — but the recursive update form holds regardless of compression level.

## What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Constraint C1 (arrow of time: update depends on $\tau^-$, not future events) | Physical law — not a formulation choice | Postulate (physical) |
| Constraint C2 (partial observability: update depends on $e_\tau$, not raw $\Omega_\tau$) | Scope definition of AAT | Postulate (scope-defining) |
| Constraint C3 (state completeness: $M_{\tau^-}$ summarizes the agent's relevant past) | Analytical commitment — the definition of $M$ as complete | Definition |
| Recursive form $M_\tau = f(M_{\tau^-}, e_\tau)$ | C1 + C2 + C3 | Proved (unique form compatible with the three constraints) |
| Future-dependent updates eliminated | C1 alone | Derived (direct consequence) |
| $\Omega_\tau$-dependent updates eliminated | C2 alone | Derived (direct consequence) |
| Full-history-dependent updates reducible to recursive form | C3 + any choice of $M \supseteq \mathcal C_{\tau^-}$ | Proved (compatibility, not elimination) |
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

**What the result says:** C1 eliminates a physically impossible class of updates (future-dependent). C2 eliminates a scope-excluded class ($\Omega$-dependent). After (1) and (2), the *only remaining question* is how the past enters: through the full history $\mathcal C_{\tau^-}$ or through a compressed state $M_{\tau^-}$. C3 says the agent *has* a complete state, and whatever that state is, it's all the agent has. The Markov form follows.

**What the result does NOT say:** That $M$ must be a lossy compression (the agent could store full history). That the Markov property is "natural" or "optimal" (it's a consequence of how $M$ is defined). That continuous-coupling systems are event-driven (the event framework is one abstraction; $\dot{M} = g(M, u)$ is the more general one, arrived at by the same three constraints).

## Discussion

**Recursion as a consequence of completeness.** The recursive form is not an assumption bolted on — it follows from the definition of $M_t$ as complete. The sufficiency of the recursive form is precisely what #def-model-sufficiency measures: when $S(M_t) = 1$, the recursive update loses nothing.

**What this opens.** The proof yields the *form*. It immediately invites the follow-up questions that the rest of the theory addresses: What should $f$ preserve? → #form-information-bottleneck and #def-model-sufficiency. How should $f$ weight new information? → #emp-update-gain. When is $\mathcal{M}$ itself inadequate? → #result-structural-adaptation-necessity.

## Working Notes

- C3's definitional character is a feature, not a bug — but it must be stated honestly. The result is not "the update must be Markovian" but rather "the Markovian analysis is the *only* consistent one, given the modeling commitment of #form-agent-model." These sound the same but have different epistemic status.
- The continuous-coupling generalization (Attack 2) deserves a proper note somewhere: $\dot{M} = g(M, u)$ is the more general form, with event-driven updates as a special case. The three constraints produce the same argument structure in both cases.
- The information-set formalization (Doob-Dynkin) provides the cleanest technical proof. It should probably be considered the primary proof path, with the elimination argument as the more intuitive exposition.

### Incidental audit gold (gold-lift, 2026-05-31)

Cross-audit ideation harvested from de-novo auditors' working dirs, deduplicated and lightly attributed. Orthogonal framing / pedagogy; off-ramp (status-label harmonization) at the end. **Coverage:** five substrates reached a digested reflection (Gemini, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-584721; Claude, AUDIT-WORKING-471203; Codex, AUDIT-WORKING-742613; Gemini-voiced, AUDIT-WORKING-773921) — unusually strong convergence; several rated this the most-trusted derivation they had read.

#### 1. Candidate Brief prose / pre-prose

- **"The Markov property is a boundary you draw around the agent, not a fact about the world."** The recurring one-line synthesis across substrates: most ML/RL frameworks *postulate* the Markov property; here it is *forced* by C1 (arrow of time) + C2 (partial observability) + C3 (state completeness), with C3 the definitional commitment. "A rigorous proof that the Markov assumption in RL is not an assumption about the world, but a tautological boundary drawn around the agent" (Gemini-voiced, AUDIT-WORKING-773921; same framing, Gemini, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-471203).
- **"Memory as digestion."** When event $e_\tau$ arrives, the agent extracts the update and discards the raw event; $M_t$ is "the accumulated nutritional value of all past events," not a storage bin. A concrete everyday analog for the recursive form that a non-specialist can re-derive (Gemini, AUDIT-WORKING-193847).

#### 2. Candidate Discussion

- **This derivation as the *template* for AAT's inevitability-core segments.** Three substrates independently read the segment's structure — three named constraints (eliminative C1/C2 vs definitional C3), dual proof paths (set-elimination + Doob-Dynkin), seven explicit counterexample "attacks" with honest verdicts, and the "What Is Derived vs. What Is Chosen" table — as the form *every other* AAT inevitability claim should adopt (Claude, AUDIT-WORKING-584721 and AUDIT-WORKING-471203; the seven-attack discipline named as a candidate meta-pattern, e.g. `#result-mismatch-decomposition` could enumerate "what would break the bias-variance decomposition?").
- **"Epistemic-architectural rather than mathematical."** Naming-seed for AAT's distinctive contribution as legible here: most frameworks contribute new math; AAT's distinctive move may be new *forms of stating* what is known, with explicit constraint-naming, definitional-character disclosure, and attack-defense. Closer to a philosophy-of-science contribution than a purely mathematical one — candidate for framing-level material (Claude, AUDIT-WORKING-471203). *(Note the early finding-vs-framing texture: offered as a re-characterization of the whole framework's contribution, not just this segment.)*

#### 3. Follow-up items

- **The C3-circularity acknowledgment must survive downstream.** Several auditors flag a consistency-watch: segments that *use* the recursive-update result should preserve the "C3 is definitional, the result is conditional-on-the-modeling-commitment" honesty rather than treating Markovianity as physically derived; drift here is a cross-segment finding (Claude, AUDIT-WORKING-471203; Codex, AUDIT-WORKING-742613).
- **Continuous-coupling caveat propagation.** Attack 2's $\dot M = g(M,u)$ generalization is the more-general form; the main `#der-recursive-update` between-event corollary $dM/d\tau = g_M(M_\tau)$ should probably carry the same "event-driven is the special case" caveat more prominently (Codex, AUDIT-WORKING-742613; already noted in this segment's own Working Notes above — the auditors converged on it independently).
- **The "(Descended from TFT Appendix ...)" annotation is diff-voice in the body.** Editorial: move to Working Notes or remove; flagged as the fourth instance of the diff-voice pattern across Section I (Claude, AUDIT-WORKING-471203).

#### 4. Readers often ask / wonder

- **"What is the discretization penalty for the continuous case (Attack 2)?"** If the true dynamic is $\dot M = g(M, o(\tau))$, the event-driven form is a Riemann-sum-style approximation — does the agent suffer an integration error scaling with the inter-event gap? (Gemini, AUDIT-WORKING-193847).
- **"Doesn't a lossy $\phi$ make the recursive form epistemically sub-optimal?"** If $M_{\tau^-}$ is not a sufficient statistic for $\mathcal C_{\tau^-}$ (lossy compression per `#form-information-bottleneck`), the recursive form locks the agent out of re-querying discarded history — mathematically valid but a structural disadvantage versus an agent that can read raw $\mathcal C_{\tau^-}$. Offered as the formal motivation for *why* agents build external memory systems (writing things down bypasses the recursive bottleneck) (Gemini, AUDIT-WORKING-193847). *(Connects to SP-27 / lossy-$\phi$ recursion and `#disc-m-preservation`.)*

#### Belongs elsewhere

- **Logogenic / Section IV reading** (points at `03-llm-core/` `#disc-m-preservation`, not this appendix): the C3-as-definitional move means a logogenic agent with externalized $M_t$ (on disk) can have its $M_t$ *defined* to include the externalized state, and the recursive form holds — the formal substrate for the $M_t$-preservation argument. Also the provocative architectural claim that Transformers "carry the raw apples around" (re-processing the full context each forward pass) rather than digesting history, so an external recursive loop must extract $M_t$ and feed it forward — aspirational reach toward the logogenic-wrapping material (Gemini, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-471203 names `#disc-m-preservation` as the destination).

#### Off-ramp (NOT gold) — routed for adjudication

- **Status-label harmonization: `exact` (this appendix) vs `conditional` (`#der-recursive-update` body) — a genuine cross-substrate disagreement worth preserving as signal.** Two readings landed: (a) Claude (AUDIT-WORKING-471203) initially flagged a mismatch, then **withdrew** it after reading — concluding the layering is *deliberate and honest*: the appendix is "exact given the three constraints," the body is "conditional on accepting C3 as a modeling commitment," two angles on the same derivation. (b) Codex (AUDIT-WORKING-742613) and Gemini-voiced (AUDIT-WORKING-773921) judged the *language* should still be harmonized, proposing "exact conditional on C1–C3 and the event-driven/sampled representation; continuous coupling generalizes the input form." Net: not a defect in the math, possibly a wording-clarity improvement on whether the two statuses read as obviously-the-same-claim-at-two-layers. Light-touch; route as a status/voice-clarity check, not a correctness finding.

---

[^kallenberg2002]: Kallenberg, O. (2002). *Foundations of Modern Probability* (2nd ed.). Springer. §1.2 (measurability and the Doob–Dynkin lemma).
