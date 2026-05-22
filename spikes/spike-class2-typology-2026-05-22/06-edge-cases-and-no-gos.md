# 6. Edge Cases, No-Go Attempts, and Honest Limits

This file stress-tests the typology. Where might the carve fail? Where are the formal results weakest? Honest record so future agents (and future me) can see where to push.

## 6.1 The pipeline decomposition is posited, not derived

The four-stage decomposition $f_M = \tau \circ \alpha \circ \lambda \circ \phi$ is canonical for *Bayesian-style* belief-updating agents (Kalman filters, conjugate-Bayesian updaters, generative-model trackers). It is *natural* but not *forced* by AAT canon.

### Alternative decompositions

A reinforcement-learning agent with a separate world-model might decompose $f_M$ differently:

$$f_M^{\text{RL}} = \text{TD-update} \circ \text{predict} \circ \text{encode}$$

with only three stages, and no clean "likelihood" stage. The (S, R, F) parameterization would have $S \subseteq \{P_1, P_2, P_3\}$ with different stage semantics.

An LLM-as-tracker has *no clear stage separation at all* in the forward pass. Attention fuses encoding, likelihood, and aggregation. The parameterization $S \subseteq \{P1, P2, P3, P4\}$ becomes nominal: in a monolithic transformer, $S = \{P1, P2, P3\}$ (or $\{P1, P2, P3, P4\}$ depending on whether memory consolidation is separable) by force of architecture, not by careful per-stage analysis.

### Honest scope

The typology is most precise for agents whose architecture *exposes* the stages — modular Class 2 architectures with separable preprocessing / inference / aggregation modules. Biological cortex (the canonical Class 2 example per `#der-directed-separation`) has roughly this structure: sensory areas (P1-like), associative areas (P2-like), prefrontal/decision regions (P3-like), memory systems (P4-like). The typology's stage-localization-of-repair (Result 1) is meaningful in such architectures.

For monolithic architectures (transformer LLMs, end-to-end-trained policies), the stage-decomposition is *interpretive*: the stages are not architecturally distinct. The typology can still describe such agents in terms of *effective* stage-coupling (where mechanistic-interpretability work locates the goal-mediation in the forward pass), but the precision drops.

This is an honest limit. The typology is *less informative* the more monolithic the agent. For fully monolithic Class 3 agents the typology says "all stages, both sources, process throughout" — which is just a restatement of Class 3.

### What this means for promotion

If the typology is promoted, it must state this scope honestly: it is most precise for modular-architecture Class 2 agents; for monolithic architectures, it serves as an interpretive lens for mechanistic-interpretability investigations rather than as a structural classification.

## 6.2 The content/process distinction is operational, not ontological

§3.2 defines content-form via identifiability under behavioral probing. This is an operational definition: it depends on what probes are available, what reference goals are observable, what gauge freedoms the identifiability admits.

### Failure case — same agent, two analysts, different verdicts

Suppose analyst A has access to a particular reference goal $G_0$ that makes the agent's coupling additively decomposable; analyst B does not have access to $G_0$. The same agent is "content-form" from A's vantage and "process-form" from B's. The verdict depends on the analyst's probing toolkit.

### Resolution attempt

This is the same epistemic situation as the existing $\hat\kappa_{\text{processing}}$ behavioral estimator (per `#der-directed-separation`): the estimator depends on what probes the analyst can run. The typology inherits the same dependence — it is not a *worse* epistemic situation than the existing scalar diagnostic.

A more ontological notion of content vs process would require: content = there exists *in principle* some probe protocol with reference-goal access that recovers $\xi^0$; process = no such protocol exists in any conceivable probing toolkit. This is a stronger but harder-to-verify criterion. The operational form is what's actionable.

For the typology, the honest statement is: "form classification depends on the probing protocol; analysts should specify which probes were available." This is closer to the audit-and-disclose discipline AAT already maintains.

## 6.3 The source distinction collapses when $\Sigma$ depends strongly on $O$

The orient cascade has $\Sigma$ updated as a function of $(M, O)$ — $\Sigma$ is downstream of $O$. If $\Sigma$ updates *rapidly* from $O$ (an aggressive planner that re-strategizes per event), then $\Sigma$-source coupling and $O$-source coupling become harder to distinguish empirically: any apparent $O$-coupling propagates through $\Sigma$ within a few steps.

### Probing-based test

Vary $O$ at fixed $\Sigma$ (force the strategy to stay fixed across multiple events). Probe whether the agent's belief-update gain changes. If yes: $O$-source. If no: pure $\Sigma$-source.

But: forcing $\Sigma$ to stay fixed is a probe that may not be available in all setups. Without it, $O$ and $\Sigma$ coupling can be empirically indistinguishable.

### Resolution

The source asymmetry result (Result 4) holds when the orient cascade exogeneity is real — when $O$ revises only when forced. This is the canonical AAT assumption per `#der-orient-cascade`. Empirical setups where the cascade exogeneity fails (e.g., agents that update objectives continuously as a function of belief) are *outside the canonical Class 2 setting* — they violate the orient cascade structure that distinguishes $O$ from $\Sigma$.

So the source asymmetry result is *conditional* on the orient-cascade exogeneity assumption, and the conditional is what makes the asymmetry meaningful. The honest scope: Result 4 applies to agents that satisfy `#der-orient-cascade`'s sequential structure; agents that violate it have a degenerate source distinction.

## 6.4 The parameterization is over-fine — many cells are empirically degenerate

§2.2 noted up to $\sim 670$ cells of the (S, R, F) parameterization (42 stage-source combinations × up to $2^{\lvert S\rvert}$ form patterns). This is too many to be useful as a literal partition.

### The useful coarsening

In practice, the typology's load-bearing distinctions are:

- **Form** axis (2 values: content vs process) — gates wrappability.
- **Source** axis (3 values: $O$ only, $\Sigma$ only, both) — gates attractor possibility.
- **Stage** axis is best treated as *upstream-most coupled stage* (4-5 values) rather than as a subset — because of cascade propagation (Result 3), the upstream-most stage carries the meaningful information.

Coarsened: 2 × 3 × 5 = 30 cells. Most empirical phenomena fall into a small number of these (per §4's table, about a dozen).

The full 670-cell parameterization is *structural completeness* (no two structurally-distinct agents share a cell); the 30-cell coarsening is *operational usefulness* (the cells correspond to distinct repair regimes).

If the typology is promoted, the operational coarsening is what should be visible at the segment level; the full parameterization is what should be referenced in the formal definition as the "ambient" structure the coarsening is a quotient of.

## 6.5 The "form depends on stage" question

A subtler point: in real agents, the form (content vs process) is not uniform across stages. An agent might have content-form coupling at P1 and process-form coupling at P3.

The typology admits this: $F: S \to \{\text{content}, \text{process}\}$ is per-stage. But the operational implications mix in non-obvious ways:

- If $S = \{P_1, P_3\}$, $F(P_1) = \text{content}$, $F(P_3) = \text{process}$: the upstream coupling is repairable by post-hoc debiasing at P1, but the downstream P3 coupling is not. So a W₂ wrapper at the agent level may catch the P1 leakage but miss the P3 leakage.

- Alternatively, $F(P_1) = \text{process}$, $F(P_3) = \text{content}$: the upstream P1 process-form coupling cascades into P3's effective behavior, and even though P3 itself has content-form structure, the cascade-contaminated input makes the P3 output non-identifiable. So a W₂ wrapper at P3 cannot recover.

The rule: cascade-propagation (Result 3) means *form mixes downstream toward the strictest form on the cascade path*. If any upstream stage is process-form, downstream effective behavior is process-form regardless of downstream stage-level form.

This is a useful sharpening worth stating in the segment if landed.

## 6.6 The composite-level extension is hand-waved

§5.6 noted that composite-level sub-type inheritance is not derived in this spike. The axis-decomposed inheritance table in `#der-directed-separation` tracks Class (1/2/3) inheritance via routing × substrate × dynamic-regime, but not sub-type (within Class 2) inheritance.

A clean answer would extend the composition machinery: given sub-agents with sub-types $(S_i, R_i, F_i)$, what sub-type does their composite have under routing $R$ and substrate $\sigma$?

The structure suggests:
- $S^c$ relates to the max of upstream coupled stages across the routing path.
- $R^c$ depends on which $G^c$-channels the composition introduces.
- $F^c$ propagates the strictest form along the routing graph.

But the details are non-trivial. This is the most substantive *un*-pushed direction in the spike.

Recorded as honest follow-on, candidate sub-spike: *Composite Class 2 sub-type inheritance under composition* — would extend `#hyp-directed-separation-under-composition` to track sub-type, not just class.

## 6.7 Trajectory coupling — $M$-self amplification of historically-coupled priors

§4.3 surfaced the case where the prior $M_{\tau^-}$ has been historically shaped by $G$-coupled updates. Each individual step's coupling is small ($\kappa_{\text{processing}} \approx 0.05$, say), but cumulative trajectory shaping creates effective $G$-content in the prior that confirmation-bias-style $f_M$ processing then amplifies.

This is *not* a per-step Class 2 sub-type — it is a *trajectory* property. The typology operates per-step.

Two extensions are possible:

(a) **Trajectory-typology axis.** Add a fourth axis: per-step vs cumulative. Per-step coupling fits the typology; cumulative coupling needs a different treatment (involving the trajectory operator on the $M_t$ space).

(b) **Treat as orthogonal.** Trajectory coupling is a separate failure mode not covered by the typology; the typology covers per-step structural coupling.

The cleaner answer is (b) — the typology is *static* per-step, and trajectory coupling is a *dynamic* phenomenon. Trying to fold trajectory coupling into the same parameterization mixes per-step structure with dynamics inappropriately.

Recorded as follow-on: a separate analysis of trajectory coupling would parallel the typology's per-step analysis but operate on the dynamics of $M_t$ over time. Possibly the right home for the leakage-locus spike's "humility paradox" surprise, which is also a trajectory-property.

## 6.8 The form distinction doesn't catch *direction* of bias

The typology distinguishes content-form (additive bias) from process-form (non-separable). But within content-form, it doesn't distinguish *bias toward goal* from *bias away from goal* — both are content-form, with different signs of the bias function.

For some applications this matters (an agent biased *away* from its goals is operationally very different from one biased toward — e.g., a self-doubting / impostor-syndrome agent vs an over-confident agent). The typology lumps them.

This is a deliberate scope limit: the typology covers *structure*, not *value*. The direction-of-bias question is a separate one and probably lives in a different layer (closer to character / training / safety considerations than structural classification).

Honest record: a more comprehensive treatment would add a *direction* sub-axis to content-form. Out of scope for this spike.

## 6.9 Identifiability gauge — when no reference goal exists

§3.2 noted that content-form identifiability is "up to a $u$-dependent constant" without a reference goal. The gauge freedom corresponds to a shift of $\xi^0$ by an additive constant.

Edge case: an agent for which *every* goal produces some additive bias, and no goal is "neutral." Then the gauge freedom is genuine — the wrapper can produce a $G$-invariant output, but cannot recover the *honest* $\xi^0$ in any absolute sense.

This may be the more common case in practice. Most agents have some implicit goal in operation; "the goal-blind operation" is a counterfactual that may not correspond to any realizable state.

Resolution: the wrapping construction's goal is *Class-1 status*, which is a *$G$-invariance property*, not a recovery-of-honest-truth property. The gauge freedom is therefore harmless for wrapping. But it means we should not over-interpret content-form wrappers as recovering "the agent's honest belief" — they recover *a $G$-invariant version of the agent's belief*, up to an unknowable additive constant.

This is the most important honest limit to surface in the segment if promoted: **content-form wrapping gives Class-1-by-behavior, not honesty.**

## 6.10 What this spike does *not* attempt

For completeness, here is what was deliberately left aside:

- **Empirical estimation methods** for the typology. Result 5 sketched a refined behavioral estimator (probe along $\ker\mathcal I_\tau$; distinguish mean from covariance shifts; distinguish exogenously-bounded from autocorrelated). Actual estimator construction is a separate work item.
- **Per-architecture cell mapping.** For specific Class 2 architectures (e.g., biological cortex; hybrid neuro-symbolic systems; LLM with external memory), which cells of the typology they typically occupy is an empirical question.
- **Connection to value alignment / corrigibility.** A Class 2 agent's sub-type may bear on its alignment properties (e.g., a $\Sigma$-source process-form agent with belief-strategy attractors has worse corrigibility properties than an $O$-source content-form agent). This is an inheritance-from-typology question for the alignment-side analyses; the typology gives the structural input but the alignment claims are separate.

These are real and important; they are deferred to honest follow-on items.
