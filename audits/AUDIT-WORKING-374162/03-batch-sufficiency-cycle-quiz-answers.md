# Answers — Batch 3 quiz

*Grounding: all core credit-lines below are grounded in segment bodies (Formal Expression / Epistemic Status / Discussion) of the six files read (five walk segments + the deriv-recursive-update appendix). WN-only depth is explicitly tagged.*

## (1) Critical Mental Model

### A b03-1.1 [mental-model]
Actual claim: under three constraints, the recursive form $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ is the *unique* realizable update — uniqueness conditional on accepting the constraint set, not an unconditional law. C1 (arrow of time, physical postulate) and C2 (partial observability, scope condition) do genuine *eliminative* work. C3 (state completeness) is *definitional*: it cannot be violated because any apparent violation (a log, buffer, cache outside "the model") is absorbed by expanding $M_t$ — violating it just means $M$ was misspecified. So the Markov structure is not discovered in the environment; it is chosen through defining $M_t$ as complete. "AAT proves updates must be Markovian" flattens exactly the honesty the segment works hardest to state.

### A b03-1.2 [mental-model]
$S(M_t)$: how much of the chronica's predictive content *this* model retains (instance quality — bias + estimation). $\mathcal F(\mathcal M)$: the supremum of $S$ over the whole representational class (the ceiling — pure bias). Operational rule: the class-ceiling signature is **persistent *structured* residuals despite adequate learning** (high gain, sufficient data, converged parameters) — autocorrelation/pattern that does not whiten with more work. The discriminator is residual *structure*, NOT mismatch magnitude: an $S=\mathcal F=1$ agent in a noisy world still has an arbitrarily high absolute mismatch floor, but its residuals are white. Derived in-batch is the two-way split: noisy-world ⇒ white residuals sitting on the floor; class ceiling ⇒ structured residuals persisting *after convergence*. Distinguishing "still-learning" is handled by the "despite adequate learning" precondition (converged parameters, sufficient data) rather than a residual signature — the segment's own Working Notes flag the ceiling-vs-still-learning reliability question as open, deferred to #result-structural-adaptation-necessity. *(Corrected after verification: an earlier version presented a three-way residual discriminator the batch's segments do not derive.)*

### A b03-1.3 [mental-model]
The inference conflates retention with truth. Sufficiency measures information *retention*: $S=1$ means the model captures all predictive information *in the chronica* — but if the history itself is systematically biased (e.g., corrupted observations), the model is faithfully sufficient to a lying record. Accuracy is measured by the mismatch signal; sufficiency by completeness of compression. "I learned everything I could from the history" ≠ "the history wasn't lying to me."

### A b03-1.4 [mental-model]
**Attack 2 — continuous environmental influence.** Concession: continuous signals (gravity, temperature, fields) are not events, so the event-driven formulation genuinely does not cover continuous coupling; the between-event corollary $dM/d\tau = g_M(M_\tau)$ holds only when the agent is truly isolated between events. The framework's answer: the same three-constraint argument in continuous time yields the classical state-space representation $\dot M = g(M, u)$ — the underlying structure survives; event-driven is the special case for digital/sampled systems.

### A b03-1.5 [mental-model]
Real agents face multiple observation channels at heterogeneous rates (camera 30Hz / LIDAR 10Hz / GPS 1Hz; compiler output vs bug reports), multiple action latencies, and asynchronous arrivals. Discrete time is the *special case* of event-driven dynamics where a single observation and single action alternate at a uniform rate on one channel. Any multi-rate/asynchronous agent (robot, developer, organization) makes fixed-clock discrete time inadequate — and the multi-channel tempo sum $\sum_k \nu^{(k)}\eta^{(k)\ast}$ is inexpressible without it.

### A b03-1.6 [mental-model]
$g_M$: the autonomous evolution of $M$ between events — prediction generation, uncertainty growth (confidence decay without data), internal reorganization (consolidation, abstraction). Not filler because inter-event intervals are variable and agents must predict/act inside them. When driven by replayed or internally-generated pseudo-events with an IB-gap-reduction objective (rather than one-step mismatch minimization), $g_M$ operates in the **consolidation regime** (#form-consolidation-dynamics), a named mode with its own scope condition $\nu_{\text{consol}} \ll \nu_{\text{online}}$.

## (2) Mathematics

### A b03-2.1 [math]
$$S(M_t) = 1 - \frac{I(\mathcal C_t;\, o_{t+1:\infty} \mid M_t, a_{t:\infty})}{I(\mathcal C_t;\, o_{t+1:\infty} \mid a_{t:\infty})}$$
Numerator: predictive information the full history carries *beyond* the model — what compression lost. Denominator: total predictive information in the history. Well-definedness: denominator $\gt 0$; violated in predictively-vacuous regimes (saturated noise, fully iid observations independent of history) — there $S$ is *undefined*, and downstream constructs (class fitness, structural-adaptation necessity) inherit the same scope.

### A b03-2.2 [math]
$\mathcal F(\mathcal M) = \sup_{M\in\mathcal M} S(M)$; structural inadequacy: $\mathcal F(\mathcal M) \lt 1-\varepsilon$ (no model in the class exceeds $1-\varepsilon$; the gap cannot close parametrically). The agent cannot compute $\mathcal F$ — that requires searching the entire class. Consequence: the trigger must operate through an *observable signature* (persistent structured residuals after parametric convergence), i.e., structural adaptation is diagnosed from symptoms, never from direct measurement of the ceiling.

### A b03-2.3 [math]
Universe at $\tau$: $\{\Omega_\tau$ (environment state), $\mathcal C_{\tau^-}$ (full history), $\{M_{\tau'}\}_{\tau'\leq\tau^-}$ (prior model states), $e_\tau$ (current event), $\{e_{\tau'}\}_{\tau'\gt\tau}$ (future events)$\}$. C1 eliminates future events; C2 eliminates direct $\Omega_\tau$ access (reaches the agent only through $e_\tau$); C3 absorbs the history and prior model states into $M_{\tau^-}$ (their retained effect *is* $M_{\tau^-}$). Survivors: $(M_{\tau^-}, e_\tau)$, hence $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$. Measure-theoretic version: restrict the agent's information set to $\sigma(M_{\tau^-}, e_\tau)$ and apply the **Doob–Dynkin lemma**.

### A b03-2.4 [math]
This is **Attack 7** (agents that store full history). Verdict: entirely consistent — the log *is part of* $M$ ($M_{\tau^-} \supseteq \mathcal C_{\tau^-}$ is allowed; the model space is just larger than you thought). The recursive form holds regardless of compression level; IB argues compression is *wise*, not required. No violation: anything available to the update mechanism is, by C3, in $M$.

### A b03-2.5 [math]
$\mathcal I(e_\tau) = I(e_\tau;\, \Omega_\tau \mid M_{\tau^-})$. Seam: $I(\cdot;\cdot)$ is mutual information — an *expected/average* quantity over the channel — while the prose reads it as the *realized* surprise of a particular event ("an event that surprises the model carries much"). The realized object would be pointwise information / Bayesian information gain, e.g. $D_{\mathrm{KL}}(p(\Omega\mid M,e) \,\Vert\, p(\Omega\mid M))$ for the specific $e$. *(Seam documented in the segment's WN as a recurring reader confusion; the notation/prose gap itself is visible from the body alone.)*

### A b03-2.6 [math]
Policy-relativity: the conditioning on $a_{t:\infty}$ means "predictive information" depends on the generating policy; $S$-comparisons require the policy held constant or specified (the continuation-policy convention $\pi_{\text{cont}}$ from #def-value-object is understood as implicit). Trajectory-relativity: $S$ is measured against *this agent's* singular chronica — the trajectory indexes it. Two copies of the same $M_t$ on divergent event streams each have their own $S$ against their own $\mathcal C_t$; neither value is the other's, and "the model has sufficiency $S$" is meaningless without naming the trajectory.

### A b03-2.7 [math]
$\eta^\ast = U_M/(U_M+U_o)$; $\mathcal T = \sum_k \nu^{(k)}\eta^{(k)\ast}$. Tier: **exactly the Kalman gain for linear-Gaussian agents; robust-qualitative for the rest of AAT's scope** — the claim is that any rational adaptive process must *approximate* this functional form, not that it is derived for all agents. (The segment type for the gain is `empirical`, itself a signal: the general form is an empirical/robust generalization, not a theorem.)

## (3) Implications

### A b03-3.1 [implications]
Check whether the residuals are **structured or white**. Structured (autocorrelated, patterned) residuals persisting after convergence ⇒ class ceiling: signal exists that the class cannot capture; architecture change (structural adaptation) is warranted. White residuals ⇒ the error is sitting on the irreducible mismatch floors (channel noise / state uncertainty); no class change removes it, and "improving the model" means chasing noise. Recommending an architecture rewrite on magnitude alone risks catastrophic thrashing.

### A b03-3.2 [implications]
The commitment is: *by defining $M$ as complete, we commit to Markovian analysis* — which then makes sufficiency the right quality metric. The claim's precise character (unique form given the constraint set) is stated instead of a false stronger claim (unconditional physical law). The real empirical work relocates to determining *what $M_t$ actually contains* for a given agent and *whether it retains enough* ($S$, $\mathcal F$) — the definitional move doesn't eliminate the cost, it names where the cost went.

### A b03-3.3 [implications]
Reconciliation: external memory the agent can read is part of its complete state — $M$ includes notes/stores by C3 (Attack 4/7 logic; the boundary is what the update mechanism can access, not what's in RAM). The structural point *(WN bonus — Gemini's reach)*: because internal $\phi$ is lossy, the recursive form locks an agent out of re-querying discarded history; external memory is the workaround — writing things down bypasses the recursive bottleneck by moving retention into a part of $M$ with different capacity/decay characteristics.

### A b03-3.4 [implications]
Neither the model nor the world changes — the *action distribution* $a_{t:\infty}$ changes, which changes which future observations are reachable/relevant and therefore what "predictive information" means. Exploration visits regimes the old compression discarded as policy-irrelevant, so $S$ drops instantly with no change in $M_t$ itself. Implication: the epistemic state's *adequacy* is coupled to strategy even if its *update* is kept goal-blind — a coupling later Parts must manage explicitly (continuation-policy convention now; directed-separation machinery in Part II).

### A b03-3.5 [implications]
The form makes the epistemic character *auditable*: the reader sees exactly which constraints eliminate, which define, what was proved vs chosen, and which attacks were faced (with honest verdicts including a conceded limitation). A bare theorem+proof hides the constraint provenance and invites over-reading. Downstream risk if the C3 caveat is dropped: segments citing the result as "updates are provably Markovian" would convert a conditional-on-modeling-commitment result into a false physical law — the drift the appendix's own Working Notes explicitly warn against propagating.

### A b03-3.6 [implications]
Steelman: normal science = parametric update within a fixed model class $\mathcal M$ (mismatch-driven refinement); anomaly accumulation = persistent structured residuals despite converged learning; crisis = the observable signature of $\mathcal F(\mathcal M) \lt 1-\varepsilon$; revolution = structural adaptation — switching to a class with a higher ceiling, which no within-paradigm tuning can substitute for. Check before promotion: isomorphism requires the analogy to make *perturbable predictions* — e.g., does Kuhnian "incommensurability" correspond to anything formal (the new class not containing the old as a subset? loss of $S$-comparability across classes given changed relevance targets)? If the mapping only matches the two endpoint concepts and not the perturbations, it is evocative, not isomorphic — and stays discussion-grade. *(The analogy itself is WN gold; grading it is the exercise.)*
