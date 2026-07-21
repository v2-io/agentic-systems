# Answers — Batch 2 quiz

*Grounding policy (adopted after batch-1 verification): answers are grounded in each segment's Formal Expression / Epistemic Status / Discussion; where an answer's full depth lives only in Working-Notes material, the core credit-line is body-derivable and the WN-depth is marked as bonus.*

## (1) Critical Mental Model

### A b02-1.1 [mental-model]
Added conditions: (3) at least binary choice ($\lvert\mathcal A\rvert \geq 2$) and (4) at least one pair of distinct actions whose *interventional* outcome distributions differ. Choice alone is insufficient because two actions with identical outcome distributions provide no interventional contrast — the agent cannot learn which action produces which effect when the effects coincide. Form of choice without substance of choice is non-agentic ("nominal agent").

### A b02-1.2 [mental-model]
**(c)** — weaker than both. The postulate: event $A$ can be a cause of event $B$ only if $A$ temporally precedes $B$ — a statement about the structure of *possible* influence, not actual influence. It is logically prior to the Pearl hierarchy: the hierarchy builds on it (and requires action-contingent observation for Levels 2–3), but the temporal-ordering postulate holds even when statistical influence is negligible (e.g., passive observers still have a causal history). Answering (a) is the classic summary-level conflation.

### A b02-1.3 [mental-model]
Query-only agent: **inside** agency (its choice-of-what-to-observe produces distinguishable observation distributions — nonzero interventional contrast, sparse information per action; post-causal-structure's "nominal/query-only coupling" tier). Unobservable-effect agent: **outside** — the agent cannot learn from what it cannot observe. Principle: the agency boundary is the *observable environment-interventional contrast*, observation-mediated in both directions; the operative contrast for causal learning is the $\Omega$-routed one surfacing through $h$. (Depth: a *pure* active-perception agent sits at the boundary — observation-channel agency without environment-causal learning.)

### A b02-1.4 [mental-model]
Completeness: by writing $M_t = \phi(\mathcal C_t)$, $M_t$ captures **everything the agent retains** from its history — anything not in $M_t$ is lost to the agent *by construction*. Stronger than "one component of internal state": $M_t$ is the *complete* epistemic substate, not a part of a richer representation. It is honest because it is tautological-relative-to-*retention* (retains, not needs) and the substantive cost — is what's retained *enough*? — is explicitly relocated to #def-model-sufficiency rather than hidden.

### A b02-1.5 [mental-model]
Because volatility enters through the joint distribution, not the preference parameter: high $\rho$ natively degrades the mutual information $I(\mathcal C_t; o_{t+1:\infty})$ — old history mathematically loses predictive power — so the optimal $\phi^\ast$ discards stale information automatically *at constant $\beta$*. Claiming the agent "lowered $\beta$" double-counts the volatility. Forgetting in a volatile world is a property of the joint distribution, not a changed internal preference.

### A b02-1.6 [mental-model]
(1) Sufficiency $S(M_t)$ — how good is *this* compression (fraction of predictive content retained); (2) model-class fitness $\mathcal F(\mathcal M)$ — the ceiling any model in the current representational class can reach. When *fitness* is low, no tuning within the class helps — the remedy is changing the model **class** (structural adaptation), not the parameters. (The trigger lives in Ch.2; the consequence is Ch.4's structural-adaptation-necessity result.)

## (2) Mathematics

### A b02-2.1 [math]
$\mathcal S_{\text{agency}} = \mathcal S_{\text{adaptive}} \cap \{(\text{Agent},\Omega) : \lvert\mathcal A\rvert \geq 2,\ \exists a \neq a' \text{ s.t. } P(o\mid do(a)) \neq P(o\mid do(a'))\}$. The existential ranges over *pairs of actions*: **one** effective contrast suffices — an agent with 99 nominal actions and 1 effective pair still qualifies. (Watch-item asymmetry: downstream results must not quietly assume full contrast across $\mathcal A$.)

*(WN-depth note: the "one effective action suffices" asymmetry is grounded in the formal existential quantifier itself — body-derivable — but the watch-item framing is WN bonus.)*
### A b02-2.2 [math]
$\phi^\ast = \arg\min_\phi [\, I(M_t;\mathcal C_t) - \beta\, I(M_t;\, o_{t+1:\infty} \mid a_{t:\infty})\,]$ with bindings $X=\mathcal C_t$, $T=M_t$, $Y = o_{t+1:\infty}\mid a_{t:\infty}$. The relevance target is **future observations given future actions** — not $\Omega$, because $\Omega$ is constitutively inaccessible (the information-loss boundary): an operationally meaningful compression target must be something the agent can eventually check against, and prediction of observations is that target. (Also makes the objective policy-relative — inherent, per the segment.)

### A b02-2.3 [math]
The *choice* to characterize optimal compression via IB (rather than MDL or Bayesian sufficiency) is the formulation — the only formulation-status element. *Given* that choice, the form of $\phi^\ast$ and its trade-off structure are exact consequences of the imported Tishby theorem (the Markov chain $Y-X-T$ holds by construction under the bindings). "Formulation ⇒ can't be exact" is the shallow pattern-match this question punishes.

### A b02-2.4 [math]
It holds because $M_t$ is constructed from history only: the model state has access to $\mathcal C_t$ but not directly to future observations, so $Y$ and $T$ are conditionally independent given $X = \mathcal C_t$. Flagged possible-failure class (WN bonus): goal-conditioned Class 2/3 agents whose $M_t$ update is influenced by goals shaped by expected future outcomes.

### A b02-2.5 [math]
Volatility enters through the **joint distribution** $p(\mathcal C_t, o_{t+1:\infty})$ — it degrades the predictive-power term's achievable value, so the optimizer discards stale history with no parameter change. $\beta$'s correct interpretation: the agent's *internal* cost of memory/computational capacity. Moving $\beta$ in response to $\rho$ is the double-counting error the segment names.

### A b02-2.6 [math]
Zero coupling: $T(\Omega_{t+1}\mid\Omega_t,a_t) = T(\Omega_{t+1}\mid\Omega_t)$ for all $a_t$ **and** observation distributions are action-independent. Such a system is outside the *agency* scope (Level-2 access vanishes; loop collapses to a one-way channel) but **inside the adaptive scope** if it observes under residual uncertainty: Part I's machinery (mismatch, gain, tempo, persistence) still applies, and the causal-structure postulate itself still holds (temporal ordering remains constitutive); only the causal *hierarchy* Levels 2–3 are inaccessible.

### A b02-2.7 [math]
Automatic — mutual information with any variable is bounded by that variable's entropy ($I(M_t;\mathcal C_t) \leq H(\mathcal C_t)$ always); the IB objective doesn't need to impose it. The compression-cost term measures *how much of the interaction history the model retains* — the number of bits of history the representation carries.

## (3) Implications

### A b02-3.1 [implications]
(1) **Structural availability**: do the tool calls actually produce Ω-routed, *observable* interventional contrast — do distinct calls yield distinct interventional outcome distributions whose effects surface back through the agent's observation channel? (Pure retrieval/query calls give only sparse query-contrast; unobserved effects give none.) (2) **Exploitation**: does the agent's model/policy actually operate on causal structure, or does it pattern-match at Level 1 despite Level-2 access being structurally present? Both must hold for the claim; most current agents fail (2) even when (1) holds.

*(WN bonus: the structural-availability vs exploitation distinction is Working-Notes gold, not body text; core credit = the observation-mediated boundary questions.)*
### A b02-3.2 [implications]
Naming the category makes visible that having-actions ≠ having-*effective*-actions — most agent literature conflates them. The boxed AI: it retains full Part-I standing (it models, mismatch-corrects, persists as an adaptive system) but is structurally denied the agency-scope results — it cannot learn causal structure or rationally plan against it, because the environment denies its choices any observable causal contrast. Diagnosis vocabulary for "internal machinery of an agent, environment denies the agency."

*(WN bonus: the boxed-AI example is WN/ELI-volume material; core credit = nominal-agent category + Part-I-still-applies.)*
### A b02-3.3 [implications]
**Anti-collapse** (#disc-anti-collapse): the refusal to merge two things a naive model treats as one, because the collapse hides a difference that *routes to a different repair* — individuate causes at the grain the remedy cares about. In the instance: volatility ($\rho$) and internal memory cost ($\beta$) are distinct causes with distinct repair channels. A volatile-world failing agent should adjust its *actions* (e.g., increase exploration — the action channel), not its compression preference; reach for $\beta$ only if the actual problem is internal memory/compute cost.

### A b02-3.4 [implications]
scope-agency's "**nominal agents**": choices with *no* causal contrast — **excluded** from agency. post-causal-structure's "**nominal coupling**": negligible effect on $\Omega$ but choice-of-observation produces distinguishable distributions (query-only) — **included** in agency. Same word, opposite scope-membership; post-causal-structure's "zero coupling" row is what actually matches scope-agency's "nominal agents." (This is a live, known terminology collision in the corpus — an agent that reports it cleanly has read both segments.)

*(WN-grounded: the collision is documented in Working Notes as a live certified finding; a segment-body-only reader can still derive it by comparing the two segments directly — that comparison is the intended test.)*
### A b02-3.5 [implications]
(a) A generalist that must be predictive across all action sequences can compress little (predictive relevance is maximal — "memorize the internet"); a specialist with a narrow policy achieves the same predictive power at far lower retention cost — the information-theoretic root of expertise. (b) If the *optimal* epistemic compression depends on the planned policy/strategy, then epistemic state formation is not automatically goal-blind — an apparent crack in directed separation. The device that manages it: predictive information is defined relative to a *continuation-policy convention* ($\pi_{\text{cont}}$, per #def-value-object), which fixes the policy-dependence conventionally rather than coupling $M_t$'s update to live goals. (Full resolution is Part-II material; at this point the tension should be *noticed*, not resolved.)

*(WN bonus for both halves: generalist/specialist and the directed-separation tension are WN gold; core credit = policy-relativity itself + the pi_cont convention pointer, which are body text.)*
### A b02-3.6 [implications]
Mechanism: the feedback loop becomes a source of **interventional (Pearl Level-2) data** — the agent's own actions generate action-contingent observations no passive stream contains. The responsible condition is the causal-contrast requirement (∃ distinct actions with distinct interventional outcome distributions); it is what #der-loop-interventional-access needs to convert the loop into a causal-data engine, and everything purposeful (Parts II–III) descends from it.
