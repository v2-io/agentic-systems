# Answers (40 questions, shuffled from /Users/josephwecker-v2/src/archema-io/asf/bin/../audits/AUDIT-WORKING-374162)

### A1 [math] (b05-2.7 — 05-batch-tempo-sector-quiz-questions.md)

(i) Stopped second moment: $\mathbb E[\Vert\delta(t\wedge\tau_R)\Vert^2] \leq \Vert\delta(0)\Vert^2 e^{-2\alpha t} + n\sigma_w^2/2\alpha$ — steady state $n\sigma_w^2/2\alpha$ (RMS $\sigma_w\sqrt{n/2\alpha}$). (ii) Fixed-time tail: $P(\Vert\delta(t)\Vert \gt R) \leq n\sigma_w^2/(2\alpha R^2)$, stationary-sharp — an instantaneous, not path, guarantee. (iii) Finite-horizon sup bound: $P(\sup_{s\leq T}\Vert\delta(s)\Vert \gt R) \leq (\Vert\delta(0)\Vert^2 + n\sigma_w^2 T)/R^2$ — controls the whole path on $[0,T]$ but grows linearly in $T$ and becomes vacuous for $T \gtrsim R^2/(n\sigma_w^2)$, consistent with a.s. eventual exit.

### A2 [implications] (b09-3.6 — 09-batch-meta-architecture-quiz-questions.md)

For: cross-cutting vocabulary exists *before* its instances arrive, so a linear reader meets each Part-II/III instance with the lens in hand (recognition instead of scattered local cleverness); the alternative — meta-patterns at the end — forces re-reading. Against: the chapter's claims reference machinery (strategy DAGs, composition closure, coupling classes) a linear reader hasn't met, making first passage partly opaque and trust-demanding — the depends lists even point forward (whitelisted ordering exceptions). Device: the **plant / develop / recall** protocol — anti-collapse is *planted* at its first concrete instance (β-vs-ρ in Part I's IB segment, with a short forward flag), *developed* here as vocabulary, and *recalled* with one-sentence pointers at each later instance — so the abstraction is always anchored to an already-seen concrete case.

### A3 [mental-model] (b02-1.6 — 02-batch-agency-model-quiz-questions.md)

(1) Sufficiency $S(M_t)$ — how good is *this* compression (fraction of predictive content retained); (2) model-class fitness $\mathcal F(\mathcal M)$ — the ceiling any model in the current representational class can reach. When *fitness* is low, no tuning within the class helps — the remedy is changing the model **class** (structural adaptation), not the parameters. (The trigger lives in Ch.2; the consequence is Ch.4's structural-adaptation-necessity result.)

### A4 [implications] (b09-3.5 — 09-batch-meta-architecture-quiz-questions.md)

Rejection: each obstruction is invariant under exactly the freedoms the others manipulate — cross-checks: a *metric change* (M3's freedom) cannot fix *non-$J$-invariance* of a resolved subspace (the projection obstruction persists under any certificate choice); *projection* cannot fix *non-symmetry* of $J$ (Helmholtz split is basis-independent); *rank augmentation* (the boundary escape) cannot remove a *memory kernel* (the Mori–Zwanzig commutator is a dynamics property, not an information deficit). Collapsing them would hide exactly the anti-collapse discipline's target: the three failures route to **different repairs** (get new information / accept matched-not-forced / redesign the resolved subspace), and a merged "integrability failure" diagnosis would send practitioners to the wrong repair — the repair-hiding merge is the definition of the error the framework's own style discipline forbids.

### A5 [implications] (b07-3.6 — 07-batch-part1-close-quiz-questions.md)

Any three of (popular → licensed): (1) "Persistence iff $\alpha \gt \rho/R$" → sufficiency + class-level tightness; agent-level iff only under radially-tight sector. (2) "Strong correction keeps a stochastic agent contained" → $P(\text{exit}) = 1$ under Model S for every $\alpha$; α buys typical scale and fixed-time tails only. (3) "Below threshold, mismatch diverges" → the *certificate* is lost; escape certified only for extremal/tight cases (dip counterexample). (4) "$\mathcal T \gt \rho/\delta_{\text{crit}}$ is the persistence theorem" → it is the linear operational form expressing task adequacy alone; overstates margin under saturation. (5) "Updates are provably Markovian" → uniqueness conditional on C1+C2+C3, with C3 definitional. (6) "Additive tempo is exact (or at least an upper bound)" → conditional on channel-independence + isotropy; deviation is *signed*, upper-bound reading refuted. (7) "The loop is interventional because the trajectory is singular" → retracted; singularity grounds only whose-effect. (8) "$S=1$ means the model is right" → sufficiency ≠ accuracy.

### A6 [implications] (b01-3.4 — 01-batch-ch1-foundations-quiz-questions.md)

Identical: the epistemic update mathematics — mismatch-driven model correction under uncertainty is the same operation whether or not the agent caused the observations. Passive systems never gain: the interventional/causal results (Level-2 machinery, CIY, and everything purposeful in Parts II–III), via the missing property of *Pearl-level-2 causal contrast* (distinct actions yielding distinct interventional distributions) — they are "passive observers" (no choice) or "nominal agents" (choice without causal effect).

### A7 [mental-model] (b08-1.3 — 08-batch-appendices-quiz-questions.md)

Signature: **unbounded scale function ⇒ no non-constant bounded harmonic function of the generator ⇒ no horizon-independent non-exit certificate**. Function: future "stays-in-region-forever w.h.p." proposals anywhere in the corpus can be *settled by invocation* — check whether the disturbance is additive-non-degenerate; if so the signature forbids the certificate — instead of re-attempting the Doob/Ville route each time. It converts a worked dead-end into standing infrastructure.

### A8 [mental-model] (b05-1.6 — 05-batch-tempo-sector-quiz-questions.md)

Deliberate while (gain improvement × post-deliberation mismatch) exceeds (pause-window drift rate × duration); stop when the *marginal* improvement rate falls below the drift rate normalized by post-deliberation mismatch. Both slogans are regime-optimal: high $\rho_{\text{delib}}$ (world moves fast during pauses) makes thinking net-harmful quickly — action bias is correct; low $\rho_{\text{delib}}$ with large mismatch makes deliberation a high-return investment — deliberation bias is correct. Neither is universal; each optimizes a different drift regime.

### A9 [math] (b08-2.3 — 08-batch-appendices-quiz-questions.md)

$\Vert\delta_{k+1}\Vert^2 = \Vert\delta_k\Vert^2 - 2\eta^\ast\delta_k^T F_d(\delta_k) + (\eta^\ast)^2\Vert F_d(\delta_k)\Vert^2 \leq (1 - 2\eta^\ast c_{\min} + (\eta^\ast)^2 c_{\max}^2)\Vert\delta_k\Vert^2 = \lambda_{\text{eff}}^2\Vert\delta_k\Vert^2$. Stability ($\lambda_{\text{eff}}^2 \lt 1$) requires $\eta^\ast \lt 2c_{\min}/c_{\max}^2$ (the no-overshoot condition; classical $2/L$ when well-conditioned). Fluid-limit gaps: Model D — **zero** (discrete steady state equals continuous exactly); Model S — additive correction of order $\eta^\ast c_{\max}^2/c_{\min}^2$.

### A10 [implications] (b02-3.4 — 02-batch-agency-model-quiz-questions.md)

scope-agency's "**nominal agents**": choices with *no* causal contrast — **excluded** from agency. post-causal-structure's "**nominal coupling**": negligible effect on $\Omega$ but choice-of-observation produces distinguishable distributions (query-only) — **included** in agency. Same word, opposite scope-membership; post-causal-structure's "zero coupling" row is what actually matches scope-agency's "nominal agents." (This is a live, known terminology collision in the corpus — an agent that reports it cleanly has read both segments.)

*(WN-grounded: the collision is documented in Working Notes as a live certified finding; a segment-body-only reader can still derive it by comparing the two segments directly — that comparison is the intended test.)*

### A11 [math] (b08-2.6 — 08-batch-appendices-quiz-questions.md)

Model: $n^{(k)} = s + w^{(k)}$, shared $s \sim \mathcal N(0,\sigma_s^2)$, independent $w^{(k)}$; $\Sigma_n = \sigma_s^2\mathbf{11}^T + \mathrm{diag}(\sigma_{w,k}^2)$. Sherman-Morrison: $J_{\text{joint}} = f(q)$ with $q = \sum_k 1/\sigma_{w,k}^2$, $f(x) = x/(1+\sigma_s^2 x)$. Strict concavity with $f(0)=0$ gives $f(q) \lt \sum_k f(q_k)$ (strict subadditivity) whenever $\sigma_s^2 \gt 0$ and ≥2 channels are active. Saturation: $f(q) \to 1/\sigma_s^2$ as $q \to \infty$ — joint information is capped at the **shared-bias floor**; no number of common-source channels buys past it, because the shared component is common to all and cannot be averaged away.

### A12 [math] (b06-2.5 — 06-batch-bridge-persistence-mood-quiz-questions.md)

$m_t = (1-\lambda)m_{t-1} + \lambda a_t$, $0 \lt \lambda \ll 1$, $\tau \approx 1/\lambda$; modulation $K_t = K_0\, g(m_t)$ with monotone bounded $g \in [g_{\min}, g_{\max}]$, band inside sector-validity and under the discrete step-size ceiling. MG instantiations: **MG-1** = the band itself (floor keeps $\alpha_t \geq \alpha_{\min} \gt \rho/R$ — excludes complacency; ceiling keeps gain-raising under the contraction ceiling); **MG-2** = trivial, the mood channel is a *linear* leaky integrator with sector constant **exactly $\lambda$**; **MG-3** = quasi-static, $\lambda \ll \underline\alpha$; **MG-4** = $\delta$-bounded second moment of the surprise summary, $\mathbb E[a_t^2\mid\delta] \leq \sigma_0^2 + c_a\Vert\delta\Vert^2$ (stated as a check on any concrete $a_t$, whose form is deliberately unpinned). Result: mood sits in sub-scope $\alpha_2$ of the adaptive-gain refinement.

### A13 [mental-model] (b01-1.3 — 01-batch-ch1-foundations-quiz-questions.md)

Thermostat: inside (observes temperature under residual uncertainty). Passive Kalman filter: inside — action is *not* required for adaptive scope. Proof engine: outside, fails $\mathcal O \neq \emptyset$ (no observation channel / no agent-environment boundary), not the entropy condition.

### A14 [implications] (b10-3.1 — 10-batch-lift-chapter-quiz-questions.md)

Prompting achieves at best **Class-1 by behavior** (partial wrapping, W₂): structural separation lives only at the *write boundary*; the *query boundary* still passes the goal to the component, so separation is bounded by the component's *compliance with the prompted instruction* — empirical, with no structural upper bound, and adversarially fragile. **Class-1 by structure** (strict wrapping, W₁, or native goal-blindness) requires the belief-update query to carry no goal in its input — checkable by inspection — with leakage bounded structurally. Under adversarial pressure the difference is decisive: a behavioral bound can be talked out of; a structural bound has no port to attack. Certification language should say which kind is claimed.

### A15 [implications] (b05-3.6 — 05-batch-tempo-sector-quiz-questions.md)

**State floor (b04)**: part of the agent's standing mismatch may be the state-uncertainty floor — irreducible by any model on this history; priced remedy: *act* to make the history more informative (active sensing, high-CIY actions). **Adaptive reserve (b05)**: $\Delta\rho^\ast = \alpha R - \rho$ is nearly exhausted when mismatch rides near $R$ — the agent is fragile; a modest disturbance shock exceeds the reserve and voids the certificate; priced remedies: raise $\alpha$ (better gain/fidelity), raise $R$ (capacity), or shed $\rho$ (environment shaping). **Structural adaptation (b03)**: if the near-$R$ mismatch is *structured* residual persisting after converged learning, the class ceiling is binding — no parametric spend helps; the priced remedy is changing model class, and (per the dichotomy) in a stochastic world this lever will eventually be required regardless. The three constructs price three different interventions: acting, absorbing, and re-architecting.

### A16 [math] (b08-2.4 — 08-batch-appendices-quiz-questions.md)

(R1) smooth log-likelihood with non-degenerate local quadratic expansion, $H_M + H_L \succ 0$; (R2) first-order-in-step-size (cubic terms negligible); (R3) Bayesian-coherent update (posterior coordinate). Gain operator: $K = (H_M+H_L)^{-1}H_L$, from $\Delta\theta = (H_M+H_L)^{-1}s = K\tilde\nabla$. Correspondences: $U_M = H_M^{-1}$ (inverse prior precision), $U_o = H_L^{-1}$ (inverse observed Fisher — the Cramér-Rao floor). Scalar collapse holds along the **natural-gradient direction**, always in 1-D and in higher dimensions **under (PI)/Čencov** (shared eigenbasis).

### A17 [mental-model] (b10-1.1 — 10-batch-lift-chapter-quiz-questions.md)

The classes index **one coupling** — $G_t \to f_M$ (goal-state into the belief-update map), measured by $\kappa_{\text{processing}}$ — by *what is certifiable about it*, not by architectural virtue. A Class 1 agent and an idealized Class 2 agent both at $\kappa = 0$ are **equally causally-disciplined**: same zero, same reality-tracking, same behavior. What distinguishes Class 1 is the *modal status* of the zero — structural (no port exists, so the zero is provable by inspecting the wiring and stable under perturbation) rather than realized-but-uncertifiable. "By construction" reads as *certifiable*, not *cleaner*.

### A18 [implications] (b04-3.6 — 04-batch-mismatch-gain-quiz-questions.md)

Confirmation bias = a *fully rational Bayesian-style update run with a miscalibrated gain*: the agent weights evidence by $\eta^\ast \approx 0$ because its internal estimate says $U_M \approx 0$ (model nearly perfect). Nothing in the update mechanics is irrational given the estimate; the estimate is wrong. Persistence: by epistemic opacity the agent cannot read the true $U_o$ or verify its own calibration from outside — it can only consult its innovation statistics, and a collapsed gain *suppresses the very corrections* that would reveal the miscalibration. The pathology is self-sealing from the inside. *(Core = body's gain-collapse + endogenous-estimation text; the "rational with miscalibrated gain" phrasing is WN gloss.)*

### A19 [mental-model] (b06-1.4 — 06-batch-bridge-persistence-mood-quiz-questions.md)

Mood is a **slow global scalar** — the leaky integral of a per-step tracking-surprise summary (how much better/worse the mismatch stream is behaving than the agent's short-horizon expectation). It modulates the update gain and thereby tempo ($K_t = K_0 g(m_t)$, $\mathcal T_t = \nu_t K_t$) within a bounded band, adding no new fast dynamics — second-order adaptation. It is definable pre-goal because nothing in it references $O_t$, $\Sigma_t$, or reward — the integrated quantity is tracking-surprise, not reward. The band's floor $g_{\min}$ prevents **mood-induced complacency**: sustained easy tracking driving correction power toward zero just before the next regime shift.

### A20 [implications] (b04-3.1 — 04-batch-mismatch-gain-quiz-questions.md)

(1) Check whether the remaining error is at the floors: white residuals at the channel + state floors mean no architecture change removes them — the state floor yields only to *more informative action/sensing*, the channel floor only to better instruments. (2) Attempting to model below the floors is **overfitting**: the model adjusts to explain irreducible noise, *increasing* error on future predictions (gain miscalibration, $\eta$ too high). The "further architecture work" proposal treats an acting/instrumentation problem as a modeling problem.

### A21 [implications] (b03-3.6 — 03-batch-sufficiency-cycle-quiz-questions.md)

Steelman: normal science = parametric update within a fixed model class $\mathcal M$ (mismatch-driven refinement); anomaly accumulation = persistent structured residuals despite converged learning; crisis = the observable signature of $\mathcal F(\mathcal M) \lt 1-\varepsilon$; revolution = structural adaptation — switching to a class with a higher ceiling, which no within-paradigm tuning can substitute for. Check before promotion: isomorphism requires the analogy to make *perturbable predictions* — e.g., does Kuhnian "incommensurability" correspond to anything formal (the new class not containing the old as a subset? loss of $S$-comparability across classes given changed relevance targets)? If the mapping only matches the two endpoint concepts and not the perturbations, it is evocative, not isomorphic — and stays discussion-grade. *(The analogy itself is WN gold; grading it is the exercise.)*

### A22 [implications] (b01-3.6 — 01-batch-ch1-foundations-quiz-questions.md)

Because the mathematics is domain-agnostic, the framework refuses to smuggle mattering into its variables; the moral weight is "a shell around the physics, not a term inside it." What this buys: the later volumes' claims become *defensible rather than mystical* — the structural facts (identity = irreversible trajectory; coherence = sustained information cost; an objective without "enough" cannot rest) are theorems that hold regardless of one's stance on moral status, so the moral layer inherits proven structure instead of doing double duty as both physics and ethics.

### A23 [math] (b08-2.8 — 08-batch-appendices-quiz-questions.md)

(MG-1) primary sector floor uniform over the gain-error ball ($\delta^T F \geq \underline\alpha\Vert\delta\Vert^2$ for all $\Vert\tilde K\Vert \leq r_K$); (MG-2) the gain-update map itself satisfies a sector condition in gain-error space ($\tilde K^T\Phi \geq \alpha_K\Vert\tilde K\Vert^2$); (MG-3) timescale separation $\alpha_K \ll \underline\alpha$ — **temporal nesting transcribed onto Lyapunov decay rates**; (MG-4) coupling boundedness of the gain-channel disturbance ($\mathbb E[\Vert v\Vert^2\mid\delta] \leq \sigma_{K,0}^2 + c_v\Vert\delta\Vert^2$). Composed result: augmented state $z = (\delta,\tilde K)$ with weighted candidate $V(z) = \tfrac12\Vert\delta\Vert^2 + \tfrac c2\Vert\tilde K\Vert^2$ is ultimately bounded in mean square — the sector-persistence template applied twice with coupling (Khalil Thm 4.18 composition, not Tikhonov reduction).

### A24 [mental-model] (b01-1.1 — 01-batch-ch1-foundations-quiz-questions.md)

**(c)** It is a *scope condition* — a constitutive/definitional boundary, not an assumption or empirical claim. With direct full-state access the entire adaptive machinery (mismatch, model, correction) is vacuous, so the theory draws its boundary where the machinery is non-degenerate. Consequence: perfect-information objections are out of scope by construction; no downstream result must re-earn the uncertainty premise. (Grading: "simplifying assumption" = summary-level wrong answer.)

### A25 [implications] (b05-3.2 — 05-batch-tempo-sector-quiz-questions.md)

(1) **Gain gating**: if the new channels are noisy ($U_o$ high) or the org's model uncertainty attribution is off, $\eta^{(k)\ast} \approx 0$ and the added $\nu$ multiplies into nothing — more reporting, no more tempo. (2) **Channel dependence**: if the dashboards draw from a shared upstream source, the channels' noises are common-source-correlated — the additive sum overcounts, with saturation at the shared-bias floor (no number of correlated channels buys information past it). For an honest tempo increase, the new channels must be *structurally independent* (uncorrelated noise sources) and individually informative (decent gain). *(The org-dashboard casting is WN-flavored; both mechanisms are body text.)*

### A26 [math] (b02-2.3 — 02-batch-agency-model-quiz-questions.md)

The *choice* to characterize optimal compression via IB (rather than MDL or Bayesian sufficiency) is the formulation — the only formulation-status element. *Given* that choice, the form of $\phi^\ast$ and its trade-off structure are exact consequences of the imported Tishby theorem (the Markov chain $Y-X-T$ holds by construction under the bindings). "Formulation ⇒ can't be exact" is the shallow pattern-match this question punishes.

### A27 [math] (b04-2.6 — 04-batch-mismatch-gain-quiz-questions.md)

Innovation variance at the steady-state optimum: $HP^-H^\top + R \gt R$. $R$ is the channel-noise floor (term iii); the excess $HP^-H^\top$ is the **state-uncertainty floor** (term ii) — present even at the in-class optimum of a well-specified filter, which is exactly the claim that the middle floor binds the Bayes-optimal predictor.

### A28 [mental-model] (b08-1.4 — 08-batch-appendices-quiz-questions.md)

DA2' = (DA2'a) directional fidelity $\delta^T F_d \geq c_{\min}\Vert\delta\Vert^2$ (identical in spirit to A2') + **(DA2'b) Lipschitz norm bound** $\Vert F_d\Vert \leq c_{\max}\Vert\delta\Vert$ — the new one. Continuous analysis never needed it because $\dot V$ involves only $\delta^T F$; the discrete recurrence produces the quadratic term $(\eta^\ast)^2\Vert F_d\Vert^2$, which needs the *norm*, not the projection. Gap-admitted pathology: correction functions with a **large transverse component** (orthogonal to $\delta$) — inner-product bound satisfied, norm bound violated.

### A29 [math] (b10-2.5 — 10-batch-lift-chapter-quiz-questions.md)

(R1) value-functional-typed; (R2) non-vacuously monotone across revision; (R3) agent-internal and itself self-actuatable; (R4) convention- and trajectory-stable. Lemma 1 (from #def-value-object's convention-monotonicity, static-pointwise): the cheap C1 verdict false-positives on merely-hard goals — only the C3/Bellman reading is a genuine infeasibility verdict, so the *only convention-invariant verdict is C3's*. Lemma 2 (from #der-directed-separation + #form-objective-functional): the C3 verdict is a global Bellman solve, not a finite per-step operation — an agent that couldn't act until computing it would be "stuck, not purposeful." Collision: (R4) forces the C3 verdict; (R3) requires per-step availability; both cannot hold. Premises: **scalar-objective scope**, **no-primitive-reflective-oracle**, and the **#der-directed-separation substrate stage** (the result's tier ceiling is bound to its draft-stage substrate).

### A30 [mental-model] (b09-1.5 — 09-batch-meta-architecture-quiz-questions.md)

Diagnostic: **there must be a tempting wrong merge** — a definition is an instance only if it names the quantity it is routinely confused with and says why turning the wrong knob is the error. Inverse case: **refusing a spurious split** — recognizing two distinct causes drive the *same* knob and share one remedy; example: #scope-edge-update-causal-validity, where observability failure and identifiability failure both freeze an edge's effective gain.

### A31 [math] (b03-2.6 — 03-batch-sufficiency-cycle-quiz-questions.md)

Policy-relativity: the conditioning on $a_{t:\infty}$ means "predictive information" depends on the generating policy; $S$-comparisons require the policy held constant or specified (the continuation-policy convention $\pi_{\text{cont}}$ from #def-value-object is understood as implicit). Trajectory-relativity: $S$ is measured against *this agent's* singular chronica — the trajectory indexes it. Two copies of the same $M_t$ on divergent event streams each have their own $S$ against their own $\mathcal C_t$; neither value is the other's, and "the model has sufficiency $S$" is meaningless without naming the trajectory.

### A32 [mental-model] (b03-1.2 — 03-batch-sufficiency-cycle-quiz-questions.md)

$S(M_t)$: how much of the chronica's predictive content *this* model retains (instance quality — bias + estimation). $\mathcal F(\mathcal M)$: the supremum of $S$ over the whole representational class (the ceiling — pure bias). Operational rule: the class-ceiling signature is **persistent *structured* residuals despite adequate learning** (high gain, sufficient data, converged parameters) — autocorrelation/pattern that does not whiten with more work. The discriminator is residual *structure*, NOT mismatch magnitude: an $S=\mathcal F=1$ agent in a noisy world still has an arbitrarily high absolute mismatch floor, but its residuals are white. Derived in-batch is the two-way split: noisy-world ⇒ white residuals sitting on the floor; class ceiling ⇒ structured residuals persisting *after convergence*. Distinguishing "still-learning" is handled by the "despite adequate learning" precondition (converged parameters, sufficient data) rather than a residual signature — the segment's own Working Notes flag the ceiling-vs-still-learning reliability question as open, deferred to #result-structural-adaptation-necessity. *(Corrected after verification: an earlier version presented a three-way residual discriminator the batch's segments do not derive.)*

### A33 [implications] (b04-3.4 — 04-batch-mismatch-gain-quiz-questions.md)

Query actions tap a source whose model has *already done the compression work* — the response transfers the output of another agent's IB. Properties (body lists four): information density (one query ≈ thousands of probe-observe cycles); trust-dependent gain (update depends on source reliability/alignment, not channel noise); pre-compressed information (with a translation cost across representational frameworks); structural adaptation via grafting external model structure. Mirror risk: **deception** — the same high-trust channel admits large *misdirected* updates; a deceptive response is positive-CIY but drives model-reality mismatch upward — adversarial disturbance injected through the observation channel, coupling scaled by the victim's trust.

### A34 [implications] (b04-3.5 — 04-batch-mismatch-gain-quiz-questions.md)

The body couples the reset to **structural change in the environment** via #result-structural-adaptation-necessity: when the environment changes in ways the model cannot track incrementally, $U_M$ *should* spike (the model "admits" uncertainty), raising $\eta^\ast$ for rapid re-learning — so the reset is principled because it is tied to the same event class the structural-adaptation machinery detects, not to a clock or heuristic schedule. What the segment does *not* derive is an operational trigger signature; the natural conjecture — that the persistent-mismatch signature from the class-fitness machinery is the shared detector — is posed in the segment's own Working Notes as a reader conjecture, not a resolved claim. *(Corrected after verification: an earlier version asserted the shared-diagnostic identity as established.)* A standalone fixed-interval reset would decouple the reset from evidence of actual staleness — that much is body-grounded.

### A35 [math] (b03-2.3 — 03-batch-sufficiency-cycle-quiz-questions.md)

Universe at $\tau$: $\{\Omega_\tau$ (environment state), $\mathcal C_{\tau^-}$ (full history), $\{M_{\tau'}\}_{\tau'\leq\tau^-}$ (prior model states), $e_\tau$ (current event), $\{e_{\tau'}\}_{\tau'\gt\tau}$ (future events)$\}$. C1 eliminates future events; C2 eliminates direct $\Omega_\tau$ access (reaches the agent only through $e_\tau$); C3 absorbs the history and prior model states into $M_{\tau^-}$ (their retained effect *is* $M_{\tau^-}$). Survivors: $(M_{\tau^-}, e_\tau)$, hence $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$. Measure-theoretic version: restrict the agent's information set to $\sigma(M_{\tau^-}, e_\tau)$ and apply the **Doob–Dynkin lemma**.

### A36 [math] (b07-2.2 — 07-batch-part1-close-quiz-questions.md)

$\nu_{\text{level } n+1} \ll \nu_{\text{level } n}$ for each adjacent pair; violation ⇒ the slower level adjusts on transients ⇒ oscillation. Levels (fast→slow): reactive response → parametric update → **consolidation** (offline IB-gap-reduction redistribution — the level added with form-consolidation-dynamics) → structural adaptation → architectural change. Status of the table: explicitly **illustrative** — real systems may have more levels; what matters is the adjacency relationship, not the count.

### A37 [implications] (b07-3.7 — 07-batch-part1-close-quiz-questions.md)

Examples (any two): the Lemma A.1N landing (a false fixed-agent "iff" was caught, a mandated strengthening attempted, and the landing is *strictly more content* — sufficiency + class-level necessity + tight-case iff + the dip counterexample, with a regression guard against restoring the "iff"); the Cor A.1S.1 landing (a false infinite-horizon bound → attempted Doob/Ville strengthening → structural failure → a *new exact theorem* plus a reusable no-go signature); also the tempo-additivity upper-bound refutation and the mood-timescale matching refutation. What the trail certifies: that claims have been *adversarially load-tested* — the reader can see which statements survived attempted refutation and exactly what died, so the surviving claims carry evidence of their boundary rather than an unexamined confidence. A clean corpus shows only assertions; a scarred corpus shows the difference between what was aspired to and what is true, which is precisely the calibration a downstream user needs. The trails also prevent re-attempting dead ends (disconfirmed predictions are recorded as such).

### A38 [math] (b09-2.4 — 09-batch-meta-architecture-quiz-questions.md)

Chain: probability chain rule (mathematical identity) / Cauchy-FE / **log-probability**. Divergence: chain-rule additivity over conditional factorizations / Cauchy-FE / **reverse-KL** (up to scaling). Update: evidential additivity / Cauchy-FE / **log-odds**. Metric: (PI) parameterization invariance / Čencov 1982 / **Fisher information metric**. Single object: the **exponential-family Legendre-Fenchel geometry** (convex potential, Fenchel conjugate, softmax/log-odds primal-dual map, Bregman divergence, Fisher = Hessian of dual potential). Caveat: the Čencov-Fenchel coincidence is **scope-dependent** — exact on exponential families in natural parameters; outside them Čencov still forces Fisher but the Fenchel-Bregman correspondence doesn't straightforwardly apply.

### A39 [implications] (b01-3.1 — 01-batch-ch1-foundations-quiz-questions.md)

Best example: the information-loss boundary. By *excluding* the full-access case definitionally, every downstream theorem may assume genuine uncertainty without an added hypothesis, and no result can be trivialized by a perfect-information limit — the limit exits the scope. (Also acceptable: the $H\gt 0$ wall making persistence machinery non-vacuous; the Markov-as-breadth commitment discharging non-Markov objections.)

### A40 [mental-model] (b01-1.2 — 01-batch-ch1-foundations-quiz-questions.md)

Known $T$: action selection collapses toward optimization/planning over a known function (a solver, not an adapter) — consequence-prediction becomes computation. Known $h$ (with $T$ still unknown): uncertainty does *not* dissolve — $h$ is constitutively lossy, so $\Omega_t$ remains unrecoverable — but the perception side reduces to standard filtering against a known observation law; the distinctive AAT setting is degraded, not eliminated. The segments' claim is that the *combination* of unknown $h$ and unknown $T$ is what creates the need for adaptive behavior; each single-known case removes a different part of the problem, asymmetrically (known $T$ is the more degenerating of the two). *(Corrected after verification: an earlier version of this answer wrongly equated "known $h$" with full-state access.)*

