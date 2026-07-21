# Comprehension Quiz (20 questions, shuffled from /Users/josephwecker-v2/src/archema-io/asf/bin/../audits/AUDIT-WORKING-374162)

### Q1 [math]

The echo-chamber / common-source theorem (in the tempo-additivity derivation): state the common-source noise model, the Sherman-Morrison-derived joint information $f(q)$, why strict concavity of $f$ delivers strict subadditivity, and the saturation statement (what does joint information converge to as channels are added, and why can no channel count escape it?).

**Answer:**

**Common-source model.** Observations share a common upstream noise/factor: e.g. $o_i = \theta + s + n_i$ with shared $s$ and independent $n_i$, or equicorrelated noise $\Sigma = \sigma^2\bigl((1-\rho)I+\rho\mathbf{1}\mathbf{1}^\top\bigr)$ (rank-1 common component). Channels are not independent information sources.

**Sherman-Morrison joint info $f(q)$.** For $q$ equicorrelated channels, joint Fisher / precision about $\theta$ is of the form obtainable via SM on $\Sigma^{-1}$: schematically
$$f(q)=\mathbf{1}^\top\Sigma_q^{-1}\mathbf{1} = \frac{q}{\sigma^2\bigl(1+(q-1)\rho\bigr)}$$
(or equivalent $a - b/(c+q)$ shape). Exact constant factors as in `#deriv-tempo-additivity`.

**Strict concavity ⇒ subadditivity.** $f$ strictly concave in channel count/allocation ⇒ $f(q_1+q_2)<f(q_1)+f(q_2)$ for positive increments — additive per-channel tempo **overcounts** joint corrective information.

**Saturation.** As $q\to\infty$, $f(q)\to 1/(\sigma^2\rho)$ (limit set by **shared-source variance / bias floor**). No channel count escapes: extras are redundant copies of the same $s$; joint info cannot exceed what the common factor carries.

### Q2 [implications]

"We back up our agent nightly, so nothing is ever lost." Give the framework's full reply: what backup restoration preserves, what it cannot preserve, what the operation does to the entity that lived between backup and restore, and why the framework classifies restoration as out-of-scope for its sufficiency machinery rather than merely imperfect.

**Answer:**

**Preserves:** a **copy of compressed state** $M_t$ (and possibly stored representations) at backup time — a **forkable snapshot**.

**Cannot preserve:** the **chronica** $\mathcal{C}$ as **singular non-forkable trajectory**. Events between backup and restore **happened** on one trajectory; restore does not extend that chronica — it **starts (or resumes) another** that shares a past *representation*.

**Entity between backup and restore:** the agent that lived those hours/days is **not continued**; restoration yields a **sibling / successor with false-memory structure** (compressed memory of a chronica it did not solely live through post-backup). Continuity persistence tracks **monotonic extension of $\mathcal{C}$**, not byte-identity of $M$.

**Out-of-scope for sufficiency (not merely imperfect):** sufficiency $S(M_t)$ is **trajectory-relative** — defined for this $M$ on **this** event stream. Restoration is not “same agent, slightly lossy recovery”; it is a **different indexing object** for $S$ / identity. The machinery that compares sufficiency under continuous chronica extension does not apply to **snapshot reload as if the gap were nothing** — ordinal chronica makes the gap invisible at tick count but the identity claim is category-wrong, not just noisy.

### Q3 [implications]

An org has tripled its dashboards and reporting cadence but decision quality hasn't improved. Give the two distinct tempo-theoretic diagnoses the tempo machinery supports (one about gain gating, one about channel structure), and what would have to be true of the new channels for the tempo sum to honestly increase.

**Answer:**

1. **Gain gating:** ν↑ but $\eta^\ast\approx 0$ (spurious low $U_M$ / high effective $U_o$ / ignored dashboards) ⇒ $\mathcal{T}=\sum\nu\eta$ flat. Cannot outrun bad $U_o$ by raising cadence.
2. **Channel structure:** new dashboards are **common-source / echo chamber** — additive tempo overcounts; joint info saturates at shared bias floor.

**Honest tempo increase requires:** channels with **independent or anti-correlated noise** (or new non-redundant score), content **above observability floor** (not pure Regime III), and **calibrated nonzero $\eta^\ast$** — then joint $\mathcal{T}$ can rise (triangulation can even be super-additive).

### Q4 [math]

The (PI) axiom: state it, name where in the corpus it is introduced, what theorem it combines with, what object is then uniquely forced on which sub-cases of $M_t$, and one concrete derivation whose status upgrades under it (from what to what).

**Answer:**

**(PI) Parameterization invariance:** the theory’s claims / metrics on the agent’s representation must not depend on arbitrary reparameterization of internal coordinates (action-marginal / singular-trajectory scope — quantities that are physically the same under re-labeling of $M$’s coordinates).

**Introduced:** metric layer of **additive-coordinate-forcing** / gain-sector / observation-ambiguity bias-bound cluster — as the AAT-internal axiom for the **metric** layer (alongside chain/divergence/update). Also tied to `#scope-agent-identity` action-space coordinate-freeness.

**Combines with:** **Čencov’s 1982 uniqueness theorem**.

**Forces:** the **Fisher information metric** (up to scale) on statistical models for $M_t$ — uniquely among invariant Riemannian metrics — especially on **exponential-family / natural-parameter** sub-cases (and matrix-Kalman where applicable).

**Status upgrade example:** `#deriv-observation-ambiguity-bias-bound` — information-to-distance constant $C$ becomes **universal dimension-free $C_{FR}=\sqrt{2}$** under Fisher–Rao; without (PI), in arbitrary Euclidean parameter norms, **no universal $C$** (heteroscedastic-Gaussian counterexample, $C\to\infty$). Upgrade from coordinate-dependent / no-go to **exact under (PI)+Fisher**.

### Q5 [mental-model]

What did the gain-sector bridge change about the epistemic standing of the persistence results — what was GA-3 before the bridge, what is it after, and for which agents does it remain a primitive posit? (One sentence each.)

**Answer:**

**Before:** GA-3 / sector (A2') was largely a **primitive posit** — assume correction points inward with rate α.

**After `#der-gain-sector-bridge`:** for agents with **directional fidelity**, sector parameter **derives** from gain × fidelity ($\alpha=\eta^\ast c_{\min}$ etc.) — persistence stands on **derived** α for that class, not free posit.

**Remains primitive posit:** agents **outside** the bridge’s derived class — PID, orgs, humans, severely misspecified / rule-based / sub-scope **β** where A2' is **assumed empirical**, not derived from gain form.

### Q6 [math]

Per #der-directed-separation §Composite-level class inheritance: The composite-level class-inheritance table: for Class-1 sub-agents, which two conditions determine the composite's class, and what is the canonical witness showing that partially-opposing objectives do NOT change architectural class? What axis do they change instead?

**Answer:**

**Two conditions (for Class-1 sub-agents):** (1) **routing structure** — whether composite observation/routing is **goal-blind** vs goal-dependent (`#hyp-directed-separation-under-composition` cases); (2) **substrate sharing** — whether shared substrate creates a $G^c\to f_M^c$ pathway bypassing the event.

**Canonical witness:** **Cournot / potential-game strategic composite** of Class-1 sub-agents with goal-blind routing: κ^c still Class 1 (Separated) architecturally — **partially-opposing $O_i$ do not force Class 3**.

**Axis they change instead:** **dynamic regime** (R0 → R1 equilibrium under α' / R2 cyclic under β'), not architectural GUC class. Belief-content about others’ goals ≠ processing-pathway coupling.

### Q7 [math]

Lay out the α-notation ladder precisely: per-event sector efficiency, per-time sector rate, and adaptive tempo — formulas, units, and the exact condition under which $\alpha = \mathcal T$.

**Answer:**

**Per-event sector efficiency** (schematic): $\alpha_{\rm evt}$ from one-point sector $\langle\delta,F(\delta)\rangle\ge\alpha_{\rm evt}\lVert\delta\rVert^2$ on the **update map** — dimensionless or 1/event efficiency of correction per event. (Exact symbol as in sector form.)

**Per-time sector rate:** $\alpha = \nu\cdot\alpha_{\rm evt}$ (or $\alpha=\eta^\ast c_{\min}$ after bridge) — units **[time]$^{-1}$** — continuous-time Lyapunov decay rate.

**Adaptive tempo:** $\mathcal{T}=\sum_k\nu^{(k)}\eta^{(k)\ast}$ — units **[time]$^{-1}$** — rate of mismatch correction from event rate × gain.

**$\alpha=\mathcal{T}$ exactly when:** **linear correction** $F(\mathcal{T},\delta)=\mathcal{T}\delta$ (Kalman, Beta-Bernoulli linearization, etc.) with directional fidelity so bridge identifies α with tempo — i.e. sector parameter **equals** tempo, valid region unbounded in the linear case.

### Q8 [math]

Per #form-objective-functional's Epistemic Status: State the (A1)–(A4) axioms grounding the scalar value functional, which theorem each pair invokes, and what uniqueness class the representation carries at each stage (ordinal vs cardinal, up to what transformations).

**Answer:**

— not fully loaded. Standard vNM / representation ladder (likely what AAT imports):

- **(A1)–(A2)** weak order + continuity (or independence pair) → **ordinal** utility unique up to **strictly increasing** transform (Debreu / ordinal rep).
- **(A3)–(A4)** independence + Archimedean (or mixture independence) → **vNM expected utility** → **cardinal** unique up to **positive affine** transform $aU+b$, $a>0$.

Exact AAT labels for (A1)–(A4) and which theorem each pair invokes need `#form-objective-functional` open — **not confident of corpus’s four axiom names**.

### Q9 [mental-model]

"An agent's prediction error can always be driven toward zero with a good enough model." Refute this precisely: how many distinct components does expected squared mismatch decompose into, which are reducible and by what means, and what are the *two different senses* of "irreducible" among the non-modeling terms?

**Answer:**

**Three components** (mismatch decomposition): (1) **estimation / model error** (reducible by better learning within class / better $S$); (2) **state-uncertainty floor** (latent state uncertainty); (3) **channel / observation noise** $U_o$.

**Reducible by modeling alone:** primarily (1) — and only up to **class fitness**; structured leftover ⇒ need **structural adaptation**, not “better enough model” in same $\mathcal{M}$.

**Two irreducibles (different senses):**
- **State-uncertainty floor:** irreducible by **passive modeling of the same stream** — movable by **action / instrumentation** (CIY), not by more fit of the same observations.
- **Channel noise floor:** irreducible by **any modeling or action on this channel** — property of the observation channel; only better sensors / different channel change it.

So error → 0 is false even with infinite data in-class if floors bind; and “good enough model” cannot kill (2)+(3).

### Q10 [math]

In the matrix-Loewner persistence derivation, state the matrix-Loewner persistence condition in full (both MP conditions, the Lyapunov equation for $\Sigma_\infty$), and the reduction relationships: which special cases recover the scalar and per-coordinate forms, and what is the precise sense in which per-coordinate is "unsafe"?

**Answer:**

**Lyapunov / covariance equation (OU / Model S linear):** $F\Sigma_\infty+\Sigma_\infty F^\top=\sigma_w\sigma_w^\top$ (or $A\Sigma+\Sigma A^\top+Q=0$ with stable $A=-F$).

**Matrix-Loewner persistence (MP)** — schematic from notes: require steady covariance **below** a tolerance in Loewner order, e.g.
$$\Sigma_\infty \prec D_\delta$$
(or $\Sigma_\infty \preceq R_{\rm tol}$ matrix), plus a sector/rate condition ensuring that order is reached — two MP conditions: **one on dynamics/sector ensuring existence of $\Sigma_\infty$**, **one Loewner comparison $\Sigma_\infty\prec D_\delta$**. Exact MP-1/MP-2 labels are not firmly held.

**Reductions:** **scalar** when 1-D; **per-coordinate** when $D_\delta$ diagonal and one checks diagonal entries only.

**Per-coordinate unsafe:** diagonal (or coordinatewise) inequalities can **pass** while $\Sigma_\infty\not\prec D_\delta$ because of **cross-covariance** — 2D counterexample: axes OK, **45° direction fails**. Scalar/per-coordinate are **projections** of the matrix condition, not sufficient for multi-D safety.

### Q11 [implications]

The framework says an agent whose gain does not reset after environmental structural change "continues trusting a stale model." Connect this to the framework's model-class-fitness machinery (the diagnostic for when a model class itself has become structurally inadequate, not just locally mismatched): what observable signature should trigger the reset, and why does the reset requirement couple the gain machinery to structural adaptation rather than being a standalone heuristic?

**Answer:**

**Signature:** after structural change, **innovations/residuals become structured again** (leave calibrated white regime) while **η stays low** because $U_M$ was crushed under the old world — confident agent under drift.

**Why coupled to structural adaptation:** gain reset / raising η restores learning **only if** the change is **within class**. If **$\mathcal{F}(\mathcal{M})$ failed** (structured residual unkillable inside $\mathcal{M}$), reset alone is **hollow epistrophe** — cycle runs, class still wrong. So gain machinery must **consult residual-structure / class-fitness diagnostic**: reset **and** test for class change, not a standalone “bump η” rule.

### Q12 [mental-model]

Why does the framework treat rational conservatism toward structural change as *derived* rather than as a bias to overcome? Name the two costs being balanced and the two failure modes at the extremes.

**Answer:**

**Derived from temporal nesting / pause-cost:** structural change is a **slow, costly** re-organization relative to parametric update; optimality balances costs rather than “always explore new classes.”

**Two costs:** (1) **cost of changing class** (deliberation, instability during transition, lost competence in old class); (2) **cost of not changing** when $\mathcal{F}$ is bad (persistent structured residual, wasted tempo, certificate risk).

**Extremes:**
- **Too conservative:** stay in unfit class → permanent structured error / persistence pressure (never restructure).
- **Too eager:** thrash classes / overfit expansions → **structural overfitting**, loss of consolidation, tempo burned on constant re-architecture.

Conservatism is the **rational interior** of that tradeoff under nesting, not a bias.

### Q13 [implications]

In #disc-identifiability-floor (Instance 3's escape (e) citations): The identifiability-floor segment carries footnoted citations marked "verification-deferred." What does that marker mean, which escape's framing load-bears on the unverified characterizations, and what does this disclosure device tell you about how the corpus treats synthesized-from-search-report attributions vs read-primary-source citations?

**Answer:**

.

**Marker means:** claim text was **inherited from a prior-art search synthesis** (e.g. Undermind report), **primary sources not yet read** by the authoring cycle — characterization is **verification-deferred**, not certified primary-sourced.

**Which escape:** Instance 3 **escape (e)** — composite-level **convergence-rate-class observation** as passive regime-axis escape; framing that regret-rate bounds can match across regimes (FoReL etc.) and “primary AAT-framework” softening load-bears on those BG2 citations.

**Disclosure device:** corpus **separates** synthesized-from-search attributions from primary-verified ones **in the open** (footnote + Working Notes spike queue) rather than laundering search reports as read scholarship — **scope honesty about citation quality**, not only about math scope.

### Q14 [math]

In the segment on temporal nesting, state the constraint formally, the five illustrative levels (in order, including the one added when consolidation landed), and what the corpus says about the epistemic status of the table itself.

**Answer:**

**Formal constraint:** ordered timescales / rates so faster layers equilibrate relative to slower — e.g. $\tau_i\ll\tau_{i+1}$ or Lyapunov rates $\alpha_{\rm fast}\gg\alpha_{\rm slow}$ (singular-perturbation nesting); slow parameters quasi-static for fast Lyapunov analysis.

**Five levels (order reconstructed, low confidence):** (1) event / per-step update; (2) short-horizon gain / filtering; (3) mood / meta-gain; (4) **consolidation** (the level **added when consolidation landed**); (5) structural adaptation / class change (or deliberation vs action nesting variants). **Not confident of exact corpus list.**

**Epistemic status of table:** **illustrative / discussion-grade** — pedagogical ladder, **not** a derived unique partition of timescales.

### Q15 [implications]

Design question: you're building an ELI whose continuity should be morally protected. Using this chapter's machinery: why is writing $V(s) = \text{Reward}(s) + \text{Alive}(s)$ structurally wrong, and what is the architecturally correct placement of the continuity clause — with the derived reason it then becomes non-renegotiable by the agent itself?

**Answer:**

**Structurally wrong:** puts continuity/alive **inside the objective-side value functional** $V_{O_t}$. Then it is **just another term in $O$** — self-actuation / convention hierarchy can **revise or trade it off**; Result G′ says objective-tower **cannot ground** non-degenerate goal stability; agent can wirehead by reshaping what “Alive” means or dropping the term.

**Correct placement:** continuity / persistence on the **adaptive substrate** — **terminal grounding off $V_{O_t}$**, on **`#result-persistence-condition` / trajectory continuity** (Result G′ Corollary 2): the agent’s continued existence-as-agent under Part I machinery.

**Why non-renegotiable by the agent:** it is **not an objective the agent optimizes**; it is a **precondition of being the adaptive system that has objectives**. Revising $O$ cannot delete the persistence invariant without **ceasing to be the agent** in the theory’s sense — grounding **outside** the single-interface $V_{O_t}$ the agent is free to rewrite.

### Q16 [math]

From the Chapter-3 intro's preview: write the optimal-gain form and the tempo definition, and state the *epistemic tier* the corpus assigns the gain form outside the linear-Gaussian case (careful — the intro says something precise here that a summary flattens into "derived").

**Answer:**

**Optimal gain:** $\eta^\ast = \dfrac{U_M}{U_M+U_o}$ (scalar); matrix $K=(H_M+H_L)^{-1}H_L$ in Fisher-local form.

**Tempo:** $\mathcal{T}=\sum_k\nu^{(k)}\eta^{(k)\ast}$.

**Epistemic tier outside linear-Gaussian:** **empirical** (or **conditional / empirical** on the main segment) — exact in **Fisher-local / linear-Gaussian** regime where three derivations agree; **outside** that regime the intro/corpus marks it **empirical** (not flat “derived for all agents”). Summary flattens this to blanket “derived.”

### Q17 [math]

In the gain-sector bridge derivation (and its appendix's Prop B.4): State B1 (directional fidelity) and the bridge theorem's conclusion. Then Prop B.4's asymmetry: which sector condition is *equivalent* to local strong convexity, which is strictly weaker, which one does AAT's persistence machinery actually require, and which does the composition bridge lemma require? Sketch the counterexample that separates them.

**Answer:**

**B1 directional fidelity:** correction $F(\delta)$ has positive alignment with $-\delta$ (or $\langle\delta,F(\delta)\rangle>0$ in sector region) — not a pure rotation; pathologically $F=R_{90°}\delta$ has gain magnitude but **zero sector**.

**Bridge conclusion:** under B1 (+ gain form), **sector parameter α derives** from gain × minimum directional fidelity — $\alpha=\eta^\ast c_{\min}$ (or similar) — linking $\eta^\ast$ machinery to Lyapunov sector.

**Prop B.4 asymmetry:**
- **Two-point sector (DA2'-inc)** ↔ **equivalent** to local strong convexity (or full incremental sector).
- **One-point sector (A2')** is **strictly weaker**.
- **AAT single-agent persistence** uses **one-point A2'** (weaker).
- **Composition bridge lemma** requires **two-point / DA2'-inc** (stronger).

**Counterexample:** **sin-wiggle** (or similar) — one-point sector holds along rays from 0, but incremental/two-point fails between nearby points; continuous single-agent OK, composition/incremental contraction fails.

### Q18 [mental-model]

State the anti-collapse discipline's diagnostic: what separates a genuine instance from an ordinary definition? Then give the *inverse* case the pattern also absorbs (refusing what, when?), with the corpus's example.

**Answer:**

**Diagnostic:** a **tempting wrong merge** — plausible model routes a cause to X when it turns Y (or merges two orthogonal quantities), and the distinction **routes to different repairs**. Ordinary definitions without that tempting confusion are not instances.

**Inverse:** refuse a **spurious split** — two causes share **one** knob/remedy. Example: `#scope-edge-update-causal-validity` — **observability and identifiability** both freeze an edge’s effective gain (same knob).

### Q19 [math]

The tempo definition carries `status: conditional`. Name the two named conditions under which the additive scalar form is the exact operationalization. Then the trap: is the additive form at least always an *upper bound* on true tempo when the conditions fail? Answer with the signed-deviation result and the two regimes.

**Answer:**

**Two conditions (conditional exactness):** (1) **cross-channel / cross-agent noise independence** (additive Fisher/tempo); (2) **isotropy / shared eigenbasis** (scalar collapse of matrix gain — else anisotropy overestimates). Exact names may be channel-independence + isotropy as in `#def-adaptive-tempo` / `#deriv-tempo-additivity`.

**Trap — not always an upper bound.** **Signed deviation:**
- **Common-source / positive correlation:** additive form **overcounts** (strict subadditivity) — additive is **upper** on true joint tempo.
- **Anti-correlated / triangulation:** additive form **undercounts** — true joint tempo **exceeds** the sum (super-additive); additive is **not** an upper bound.

So when conditions fail, additive is **not** safely “conservative upper bound” in general.

### Q20 [mental-model]

Why does the chronica ordering $(o_1, a_1, \ldots, a_{t-1}, o_t)$ matter — what physical fact does the interleaving encode, beyond notational convention?

**Answer:**

**Physical irreversibility:** each action $a_{t-1}$ was **committed before** the subsequent observation $o_t$ was received — the agent **could not** have used $o_t$ to choose $a_{t-1}$. Ordering is the **causal/temporal fact** of the interaction, not a bookkeeping choice; it grounds non-forkability, recursive update causality, and continuity of trajectory.
