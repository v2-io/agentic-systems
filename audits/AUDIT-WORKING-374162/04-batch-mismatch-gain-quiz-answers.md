# Answers — Batch 4 quiz

*Grounding: all core credit-lines are from segment bodies; WN-only depth tagged.*

## (1) Critical Mental Model

### A b04-1.1 [mental-model]
Three components: (i) **estimation error** — gap between the model's predictive mean and the *Bayes predictor* (best chronica-measurable predictor) — reducible by better modeling; (ii) **state-uncertainty floor** — variance the true conditional mean retains given the history — *irreducible by modeling* (binds the Bayes-optimal predictor itself) but **movable by acting** (more informative actions/observations shrink it); (iii) **channel noise** — irreducible outright, a property of the sensor, movable only by changing the instrument. The two senses of irreducible: by-any-model-on-this-history (ii) vs by-anything-short-of-a-new-sensor (iii).

### A b04-1.2 [mental-model]
(a) The model genuinely reflects reality (desirable); (b) the agent only observes aspects its model already explains — confirmation bias; (c) the channel is too noisy to reveal model errors — architectural limitation. Only (a) is desirable ("silence can mean peace or deafness"). The mechanism motivated by the ambiguity: **active testing** — choosing actions that generate informative mismatch, formalized as causal information yield (CIY).

### A b04-1.3 [mental-model]
Gain collapse: $\eta^\ast \to 0$, so the corrective phase (epistrophe) ceases — mismatch still arrives but is no longer turned toward. Etiologies: spurious confidence ($U_M$ estimated too low — dogmatism) or spurious sensor-distrust ($U_o$ estimated too high — nihilism). Behaviorally identical because both zero the same ratio — the agent stops updating and coasts on priors either way. To distinguish them you need the agent's *internal uncertainty attributions* (its $U_M$/$U_o$ estimates), not its behavior. *(The dogmatism/nihilism naming is WN gloss; the two etiologies and the collapse mechanics are body text.)*

### A b04-1.4 [mental-model]
CIY measures **action-distinguishability** — how different an action's interventional outcome distribution is from alternatives' — not learning value. Counterexample: a deterministic button that beeps — its outcome distribution is maximally distinct (high CIY) yet after the first press the agent learns nothing (zero expected information gain). Relationship: high CIY is *necessary* for learning (indistinguishable actions can't teach) but *not sufficient* (distinguishable actions teach only when the agent is uncertain). The heuristic $\lambda(M_t)$ gate (suppressing exploration when $U_M$ is low) is what makes CIY behave like EIG as a surrogate.

### A b04-1.5 [mental-model]
Fluency: the degree to which effective action flows from the model without deliberative computation. Formal characterization: high fluency ⟺ $\Delta\eta^\ast(\Delta\tau) \approx 0$ — additional deliberation yields negligible improvement (via #der-deliberation-cost). Distinct from sufficiency: sufficiency is about *retained predictive information*; fluency about *cheap action generation*. Canonical example: a chess engine with a perfect rule-model — high $S$, low fluency (search remains expensive). Converse: a reflex — moderate sufficiency, high fluency in its narrow domain.

### A b04-1.6 [mental-model]
Mechanism: when two selection modes yield equivalent expected outcomes, the faster is preferable because the persistence condition penalizes slower tempo — so selective pressure (evolution, competition, training) internalizes recurring action patterns, converting deliberation into fluency. Stronger when: (1) $\rho$ high (fast-changing environment), (2) the pattern recurs frequently, (3) $\mathcal T$ sits near the persistence threshold with no deliberation slack. Deliberation remains essential when: the situation is genuinely novel, the action space is large relative to model capacity, stakes are asymmetric (error cost ≫ delay cost), or $\rho$ is low.

## (2) Mathematics

### A b04-2.1 [math]
$$\mathbb E[\Vert\delta_t\Vert^2] = \mathbb E[\Vert\hat o_t - \hat o_t^{\mathrm B}\Vert^2] + \mathbb E[\operatorname{Var}(\bar o_t \mid \mathcal C_{t-1}, a_{t-1})] + \mathbb E[\operatorname{Var}(o_t \mid \Omega_t, a_{t-1})]$$
with $\hat o_t^{\mathrm B} = \mathbb E[o_t \mid \mathcal C_{t-1}, a_{t-1}]$ (Bayes predictor — best chronica-measurable predictive mean) and $\bar o_t = \mathbb E[o_t \mid \Omega_t, a_{t-1}]$ (true conditional mean given environment state). GA-1 (**fresh noise**: $\varepsilon_t$ conditionally independent of $\mathcal C_{t-1}$ given $(\Omega_t, a_{t-1})$) kills the noise cross-terms; the third cross-term vanishes because the Bayes predictor is the conditional mean given the history. The argument is **orthogonality (zero conditional mean / uncorrelatedness), not full independence** — the body says so explicitly.

### A b04-2.2 [math]
Floor for **every chronica-measurable predictor, including the Bayes-optimal one** — no model built from the history can go below it. Only named route to move it: **acting** — making the interaction history more informative (the door through which active sensing and CIY enter the mismatch budget). Alignment qualifier: the floor is positive exactly when residual state uncertainty *moves the one-step conditional mean*; uncertainty confined to mean-irrelevant coordinates or to higher moments only leaves the floor at zero — so $H(\Omega_t\mid\mathcal C_t) \gt 0$ (which concerns the state, not the mean) is necessary but not sufficient.

### A b04-2.3 [math]
$\eta^\ast = U_M/(U_M+U_o)$; $M_t = M_{t-1} + \eta^\ast \cdot g(\delta_t)$. Exact in the **Fisher-local regime**: any smooth log-likelihood with a non-degenerate local quadratic expansion — grounded in **Amari's natural-gradient invariance theorem** ($\Delta\theta = K\tilde\nabla$, $K = (H_M+H_L)^{-1}H_L$, scalar collapse along the natural-gradient direction); Kalman and conjugate-Bayesian cases are *globally* exact instances. Outside the regime (non-quadratic losses, non-conjugate priors, heavy tails/multimodality): the **direction** is preserved (gain rises with $U_M$, falls with $U_o$) — robust-qualitative — but global quantitative fidelity is not claimed.

### A b04-2.4 [math]
Paradox: optimal gain requires $U_o$, but #def-observation-function makes the noise distribution constitutively unknown to the agent. Resolution: the agent *estimates* $U_M$ and $U_o$ from the observable statistics of its own mismatch/innovation sequence, making the gain an **endogenous state variable updated meta-adaptively** — the update machinery applied to its own parameter. The proof that this meta-adaptation preserves Lyapunov stability without violating opacity is deferred to #deriv-adaptive-gain-dynamics.

### A b04-2.5 [math]
$\mathrm{CIY}(a; M) = \mathbb E_{a' \sim q(\cdot\mid M)}\left[D_{\mathrm{KL}}\left(P(o \mid do(a), M)\,\Vert\, P(o\mid do(a'), M)\right)\right]$. Default $q$: **policy-induced**, $q = \pi(\cdot\mid M)$. Consequence: CIY then reads "how different is this action's outcome from what I'd *typically* do" — partly a measure of deviation from the agent's own habits, not an intrinsic action property; and CIY values are **not comparable across different $q$ choices**.

### A b04-2.6 [math]
Innovation variance at the steady-state optimum: $HP^-H^\top + R \gt R$. $R$ is the channel-noise floor (term iii); the excess $HP^-H^\top$ is the **state-uncertainty floor** (term ii) — present even at the in-class optimum of a well-specified filter, which is exactly the claim that the middle floor binds the Bayes-optimal predictor.

### A b04-2.7 [math]
Exact: action is a function of the agent's complete internal state — $a_t = \pi(M_t)$ under Part I scope ($G_t = \emptyset$), $\pi(M_t, G_t)$ after the Part II lift, both by the completeness argument. Discussion-grade: the implicit/explicit distinction and the action-fluency concept (qualitative, not formally derived propositions — the segment says so). Cleaner one-statement form: $a_t = \pi(X_t)$ with $X_t = M_t$ in Part I and $X_t = (M_t, G_t)$ in Part II. *(The $\pi(X_t)$ restatement is WN-suggested; the two-scope structure is body text.)*

## (3) Implications

### A b04-3.1 [implications]
(1) Check whether the remaining error is at the floors: white residuals at the channel + state floors mean no architecture change removes them — the state floor yields only to *more informative action/sensing*, the channel floor only to better instruments. (2) Attempting to model below the floors is **overfitting**: the model adjusts to explain irreducible noise, *increasing* error on future predictions (gain miscalibration, $\eta$ too high). The "further architecture work" proposal treats an acting/instrumentation problem as a modeling problem.

### A b04-3.2 [implications]
Not through the update rule: the gain weights observations by **informativeness/uncertainty** ($U_M$ vs $U_o$), with no causal-downstreamness term. Causal weighting enters through **action selection**: CIY scores actions by interventional contrast, so the agent *generates* causally informative observations by choosing high-CIY actions (gated by $\lambda(M_t)$); the mismatch-decomposition's state floor also moves only via acting. So the earlier normative claim is delivered by the exploration/selection machinery, not by up-weighting Level-2 observations in $\eta^\ast$ — a precision most summaries flatten.

### A b04-3.3 [implications]
Veteran: low $U_M$ (confident model), treats test as high-$U_o$ noise ⇒ $\eta^\ast \approx 0$, ignore. New hire: high $U_M$, low $U_o$ ⇒ $\eta^\ast \approx 1$, large correction. Each is near-optimal in the matching circumstance (stable known domain vs genuine novice uncertainty); each is pathological in the other's. Moving to a new codebase = structural change: the framework prescribes a **gain reset** — $U_M$ should spike, raising $\eta^\ast$ for rapid re-learning. Ignored: the veteran keeps trusting a stale model — Boyd's "incestuous amplification," the brittle-failure mode in non-stationary environments. *(The senior/junior casting is WN gloss; reset-after-structural-change and the Boyd naming are body text.)*

### A b04-3.4 [implications]
Query actions tap a source whose model has *already done the compression work* — the response transfers the output of another agent's IB. Properties (body lists four): information density (one query ≈ thousands of probe-observe cycles); trust-dependent gain (update depends on source reliability/alignment, not channel noise); pre-compressed information (with a translation cost across representational frameworks); structural adaptation via grafting external model structure. Mirror risk: **deception** — the same high-trust channel admits large *misdirected* updates; a deceptive response is positive-CIY but drives model-reality mismatch upward — adversarial disturbance injected through the observation channel, coupling scaled by the victim's trust.

### A b04-3.5 [implications]
The body couples the reset to **structural change in the environment** via #result-structural-adaptation-necessity: when the environment changes in ways the model cannot track incrementally, $U_M$ *should* spike (the model "admits" uncertainty), raising $\eta^\ast$ for rapid re-learning — so the reset is principled because it is tied to the same event class the structural-adaptation machinery detects, not to a clock or heuristic schedule. What the segment does *not* derive is an operational trigger signature; the natural conjecture — that the persistent-mismatch signature from the class-fitness machinery is the shared detector — is posed in the segment's own Working Notes as a reader conjecture, not a resolved claim. *(Corrected after verification: an earlier version asserted the shared-diagnostic identity as established.)* A standalone fixed-interval reset would decouple the reset from evidence of actual staleness — that much is body-grounded.

### A b04-3.6 [implications]
Confirmation bias = a *fully rational Bayesian-style update run with a miscalibrated gain*: the agent weights evidence by $\eta^\ast \approx 0$ because its internal estimate says $U_M \approx 0$ (model nearly perfect). Nothing in the update mechanics is irrational given the estimate; the estimate is wrong. Persistence: by epistemic opacity the agent cannot read the true $U_o$ or verify its own calibration from outside — it can only consult its innovation statistics, and a collapsed gain *suppresses the very corrections* that would reveal the miscalibration. The pathology is self-sealing from the inside. *(Core = body's gain-collapse + endogenous-estimation text; the "rational with miscalibrated gain" phrasing is WN gloss.)*
