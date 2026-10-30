---
slug: def-action-transition
type: definition
status: axiomatic
depends:
  - def-agent-environment
stage: deps-verified
---

# Definition: Action and Transition

The action channel is now formalized. The agent has an **action space** $\mathcal{A}$, and actions affect the environment through a possibly-stochastic **transition function** $T$: the next environment state is drawn from $T(\cdot \mid \Omega_t, a_t)$. Deterministic transitions are the special case where $T$ concentrates all mass on a single successor; stochasticity is permitted but not required. The agent may not know $T$. $T$ is the transition part $\theta_T$ of the environment's law, and whatever of it the agent was not built knowing is random under the reference measure of #scope-adaptive-system, whoever else may know it. Together with the observation channel ( #def-observation-function), this completes the agent-environment loop: environment $\to$ observation $\to$ agent $\to$ action $\to$ next environment.

Not knowing $T$ is one of two ways the loop can leave the agent something to learn; not knowing the state is the other. A Kalman filter knows its transition law exactly and still has a hidden state to track, and a reinforcement learner that reads its state exactly still has a transition law to learn. Each kind of knowledge removes one kind of work: a known state leaves nothing to filter, a known law leaves nothing to learn, and only the two together leave nothing to adapt to ( #scope-adaptive-system).

One subtle modeling commitment is surfaced: by writing the transition as Markov in $\Omega$ (only $\Omega_t$ and $a_t$ appear in the conditioning), the framework implicitly takes $\Omega$ to be the *sufficient state* for its own evolution — any non-Markov environment is absorbed by extending $\Omega$ to include enough history. This is the world-side analog of a parallel move the framework will make later for the agent's internal model ( #deriv-recursive-update Constraint C3): Markov properties here are commitments about the *breadth* of the named object, not structural claims about underlying dynamics.

## Formal Expression

*[Definition (action-transition)]*

The **action space** $\mathcal{A}$ is the set of actions available to the agent. Actions affect the environment via the transition function:

$$\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$$

where:
- $T$ is the (possibly stochastic) transition function
- $\Omega_t$ is the current environment state
- $a_t \in \mathcal{A}$ is the agent's chosen action

*[Definition (fresh-transition)]*

The draw is **fresh**: given $\Omega_t$, $a_t$ and $T$, the next state $\Omega_{t+1}$ is drawn from $T(\cdot \mid \Omega_t, a_t)$ independently of everything earlier in the run (earlier states, observations and actions, the noise behind those observations, and the agent's own randomness). This is the Markov commitment, stated for the whole run rather than for the state's own past: anything that carries forward, including the noise of an earlier observation, is part of $\Omega_t$.

*[Definition (transition opacity)]*

The agent may not know $T$ exactly. $T$ is the transition component $\theta_T$ of the environment's law, and whatever of it the agent was not built knowing is random under the reference measure $\pi_0$ of #scope-adaptive-system, whose set of possible worlds only the agent's design-time knowledge cuts down. Transition opacity is not required of every system in scope; the scope requires that the state or the law, or both, leave something for the world to reveal.

## Epistemic Status

This is *definitional*. The transition function $T$ is a modeling device that captures how agent actions couple back into the environment. The stochasticity of $T$ is allowed but not required — deterministic transitions are the special case where $T$ places all mass on a single successor state. The fresh-transition clause commits to the breadth of $\Omega$, and holds without loss of generality for the same reason the Markov commitment it extends does: whatever the world remembers is declared as state. Transition opacity is one of the typed components of the uncertainty the adaptive scope requires (state, transition law, observation law); it is not required on its own, in parallel with the observation-law opacity of #def-observation-function.

## Discussion

**Closing the loop.** Together with #def-observation-function, this definition completes the agent-environment coupling: the agent observes via $h$ and acts via $T$. The loop $\Omega_t \xrightarrow{h} o_t \rightarrow \text{agent} \xrightarrow{a_t} \Omega_{t+1}$ is the fundamental structure that all subsequent claims build on.

**What known and unknown $T$ each leave.** If the agent knows $T$ and can read the state, action selection is planning under chance over a known decision process, which is outside the adaptive scope. If it knows $T$ but cannot read the state, it still has to filter, and it plans over its beliefs about the state. If it does not know $T$, it has to learn, whatever it can see. Adaptive behavior is needed whenever the state or the law is open.

**Markov-of-$\Omega$ as a modeling commitment, not an empirical assumption.** The form $\Omega_{t+1} \sim T(\cdot \mid \Omega_t, a_t)$ is implicitly Markov in $\Omega$ — only the current $\Omega_t$ and $a_t$ appear in the conditioning. Without loss of generality, $\Omega$ is taken to be the *sufficient state* for its own evolution under $T$: any non-Markov environment is absorbed by extending $\Omega$ to include enough history to make future-state distribution depend only on current state and action. This is the world-side analog of the Markov-by-completeness move that #der-recursive-update makes for the agent-side state $M_t$ ( #deriv-recursive-update Constraint C3). The two are independent — Markov-of-$M_t$ is forced by *defining $M_t$ as complete*; Markov-of-$\Omega$ is forced by *defining $\Omega$ as the sufficient state*. Both are modeling commitments about the *breadth* of the named object, not structural assumptions about underlying world dynamics.

**Sufficient for the run, not only for its own past.** Markov in its own past is not enough. Take a known law, a hidden bit $x$ in $\Omega_1$, a first reading $o_1 = x \oplus \varepsilon_1$ with $\varepsilon_1$ a fair coin, so that $o_1$ alone says nothing about $x$, and a later state whose bit is $\varepsilon_1$, reported at step $K$. Given its own past, that state's bit is a fair coin, so the state is Markov in its own evolution and the channel's noise is fresh at every step. Yet $o_K \oplus o_1 = x$: the world remembers $\varepsilon_1$ between steps $1$ and $K$ outside anything named as state, and what the next observation shows about the world is no longer settled by the current state. The fresh-transition clause rules this out by declaration: the remembered noise is state from step $1$ on. With fresh noise ( #def-observation-function), it gives the factorization the rest of the framework uses. Given the current state, the action and the law, the next state and observation are independent of everything earlier, and the law of a run is a product of kernels and policy.

## Working Notes

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical / framing / figure / naming material, kept separate from the certified theory-fix findings (handled elsewhere). **Coverage:** 10 dirs carry a dedicated reflection (193847, 266847, 361742, 384279, 471203, 526815, 742613, 773921, 829314, 849201) plus the figure-cycle dir 472913; 451729 and 963715 cover it inside a Section-I batch. Substrate attribution inferred from voice where not explicit; uncertain cases hedged.

#### 1. Candidate Brief prose / pre-prose

- *Superseded 2026-10-30: AAT does not require joint opacity; it requires that the state or the law leave something to reveal ( #scope-adaptive-system), and a Kalman filter (law known) and a tabular learner (state read exactly) are each inside on one component. The quoted form below is kept as the reader reaction it was.* The dual-opacity hook: AAT applies under *joint opacity of perception and dynamics*. "If only $h$ were unknown, the agent could plan against a known dynamics; if only $T$ were unknown, the agent could see the world directly but couldn't predict consequences" (Gemini, AUDIT-WORKING-193847). The paired-naming form — *opacity of perception* (info-loss boundary) and *opacity of action* (transition opacity) — framed as "AAD applies under double opacity," floated as more memorable than either term alone (Claude, AUDIT-WORKING-471203).
- The computation-vs-adaptation dividing line as a plain-language gloss: "If the agent knew $T$ exactly, action selection would reduce to optimization over a known function" — i.e., "If $T$ is known, you don't need a cycle, you just need a planner (like A* or Dijkstra)" (Gemini, AUDIT-WORKING-829314). Each action is then "simultaneously an intervention to achieve a goal and an experiment to reduce uncertainty about $T$."

#### 2. Candidate Discussion

- **The bounded-vs-unbounded Markov asymmetry** *(strongest item here).* The segment says the $\Omega$-side and $M_t$-side Markov moves are "independent" and parallel. One substrate flagged a glossed asymmetry: $\Omega$ is "the totality of state external to the agent" with *no finiteness assumption*, so Markovization-by-augmentation of $\Omega$ is genuinely without-loss; but $M_t = \phi(\mathcal{C}_t)$ is a *bounded, lossily compressed* object (by the seg-01 information-loss boundary), and "Markov-by-completeness for a *bounded* object is **not** free — augmenting to recover sufficiency can hit the capacity wall. So the two commitments are parallel in *form* but asymmetric in *cost*: $\Omega$-side is WLOG; $M_t$-side has teeth." The framing offered: discharging an objection *by definition* doesn't make the cost vanish — it *relocates* to wherever the defined object meets a constraint; for $\Omega$ the cost relocates nowhere, for $M_t$ it relocates to the model-capacity machinery ($R$, model-class fitness, sufficiency) (Claude, AUDIT-WORKING-472913, "THREAD-B"). A candidate clause acknowledging the bounded/unbounded asymmetry, or a forward-ref to where the $M_t$-side cost is discharged.
- **Markov-as-commitment is methodologically reusable.** Naming the Markov property as a *commitment about breadth* rather than an empirical claim is "a reusable modeling defense" (Claude, AUDIT-WORKING-526815) — "if the world has memory, then that memory is part of the world's state" (Claude, AUDIT-WORKING-773921). Candidate one-line gloss for the existing Discussion paragraph, which several substrates singled out as a model of epistemic hygiene.

#### 3. Follow-up items

- **A hidden learnability / smoothness assumption.** For mismatch-driven updates to work, "$T$ cannot be adversarial white noise. There has to be a hidden assumption of *learnability* or *smoothness* in $T$ that hasn't been formalized here." If the universe is deeply non-Markov, "the opacity of $T$ approaches totality" and action becomes "blind thrashing" — adaptation requires *some* locally exploitable structure the framework has not yet named (Gemini, AUDIT-WORKING-193847). A candidate scope condition / open formalization.
- **Practical $\Omega$-sizing cost.** The "extend $\Omega$ until Markov" move is WLOG but "may require including infinite history" — the formal $\Omega$ (complete sufficient state) and the practical compressed approximation diverge, and the practical question of $\Omega$-construction should be addressed somewhere (likely `02-tst-core/` or `03-llm-core/`) (Claude, AUDIT-WORKING-384279; Claude, AUDIT-WORKING-451729; Codex/Claude, AUDIT-WORKING-526815).
- **Equation-tag-vs-content typing of "transition opacity."** Two substrates read the `*[Definition (transition opacity)]*` tag as mistyped: "the agent does not know $T$ exactly" *restricts epistemic access* rather than introducing an object, so it reads as a *postulate*- or *scope*-flavored claim. FORMAT.md's eq-tag list does include `*[Postulate (slug)]*`, so the atom could carry `*[Postulate (transition-opacity)]*` while the segment type stays `definition` — correctable without restructuring (Claude, AUDIT-WORKING-384279). A *third* substrate examined the same tag and *withdrew* the candidate on second look (the parenthetical names a *term being introduced*, and FORMAT has no `*[Scope]*` tag) (Claude, AUDIT-WORKING-471203). The disagreement itself is the signal: the eq-tag taxonomy for constitutive-scope claims is genuinely ambiguous — a `§G`/FORMAT-vs-corpus question rather than a clean segment fix.

#### 4. Readers often ask / wonder

- **How does the agent learn when *both* $T$ and $h$ are unknown?** "The credit assignment problem seems insurmountable without some anchor. Does the mismatch signal provide that anchor?" (Gemini, AUDIT-WORKING-193847). A natural reader question at this point in the build.
- **Does discrete $\Omega_{t+1} \sim T(\cdot\mid\Omega_t,a_t)$ commit to a clock?** The notation implies discrete ticks; readers will want to know how this bridges to the continuous-time / event-driven framing hinted in the overview (Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-193847 — "this fluid limit will likely be a major pain point" for continuous control / high-frequency trading).
- *Dissolved 2026-10-30: transition opacity is no longer required of every in-scope system, so a known token-append step violates nothing; whether the loop is in scope turns on what remains unknown about the user, tools and world.* **Doesn't the LLM case violate transition opacity?** Appending a token to the context is deterministic and known to the LLM; the resolution offered is that $\Omega$ also includes the human user / API whose dynamics are not known, preserving opacity (Claude, AUDIT-WORKING-773921). A Volume-3 reader will reach for this.
- **The "unknown $h$ and unknown $T$" gloss is slightly circular.** "It's essentially restating that uncertainty creates the need for adaptation. The deeper point is that *partial information under change* creates the need … Unknown-but-fixed $T$ would still require optimization, just not adaptation" (Claude, AUDIT-WORKING-963715). A candidate sharpening of the Discussion's "what makes action non-trivial" sentence.

#### 5. Candidate figures

- **Hidden-kernel two-state diagram.** Two world states with an *opaque* transition kernel between them: the agent chooses $a_t$, but the actual map $\Omega_t \to \Omega_{t+1}$ is hidden; the visual should "separate the real world-side sufficient-state transition from the agent's model of it, which is intentionally missing at this point" (Claude, AUDIT-WORKING-526815).
- **Closed-loop + asymmetry inset.** Left: the fundamental loop $\Omega \xrightarrow{h} o \to \text{agent} \xrightarrow{a} \Omega$ with the two opacity lenses ($h$ unknown, $T$ unknown). Right: the asymmetry inset — $\Omega$ as an arbitrarily-extensible box (augment freely, WLOG) vs $M_t$ as a fixed-capacity box (augmentation hits the wall) — drafted to carry THREAD-B above (Claude, AUDIT-WORKING-472913).

#### Belongs elsewhere

- **03-llm-core — $\Omega$ for a logogenic agent.** Several substrates noted that for an LLM the environment "*includes* the conversation history, including the agent's own previous outputs," so the Markov-of-$\Omega$ move "becomes interesting … $\Omega$ would need to include enough of the conversation history to make the next-token distribution Markov — essentially the entire context window" (Claude, AUDIT-WORKING-963715; Claude, AUDIT-WORKING-384279 on multi-agent $\Omega$ containing another agent's $M_t,G_t,\Sigma_t$). Points at Volume 3, not this segment.
- **02-tst-core — running a test as an observation of $T$.** "A developer cannot simulate the entire JVM or V8 engine … running a test isn't just a verification step; it is a vital observation of the unknown transition function $T$ … software tools artificially lower the entropy of $T$, not because $T$ is naturally known" (Gemini, AUDIT-WORKING-829314). A TST-instantiation seed.
- **Predictive-state vs belief-state stance.** A note that AAT's $M_t = \phi(\mathcal{C}_t)$ (history compression) leans closer to the predictive-state-representation tradition than to explicit Bayesian belief-over-$T$; "the agent doesn't compute beliefs about $T$ directly; it compresses history into $M_t$." Whether AAT is architecture-agnostic on this axis or forces one stance is flagged to watch downstream (Claude, AUDIT-WORKING-471203). Belongs with `#form-agent-model` / `#form-information-bottleneck`.
