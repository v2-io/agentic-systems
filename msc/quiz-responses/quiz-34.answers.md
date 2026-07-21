# Answers (34 questions, shuffled from /Users/josephwecker-v2/src/archema-io/asf/bin/../audits/AUDIT-WORKING-374162)

### A1 [implications] (b09-3.4 — 09-batch-meta-architecture-quiz-questions.md)

(a) **Architecture ladder, general-open column**: Class 3 (Coupled) — directed separation fails by construction; forbids applying Class-1 Part-II results directly; licenses the coupled formulation (Volume 3) and the wrapping repair route. (b) **Identification-regime ladder, general-open column**: Regime C (observational, $\iota \approx 0$) — identification depends on external assumptions like unconfoundedness; forbids treating edge updates as causally valid without them. (c) **Dynamic-regime ladder, general-open column**: R3 mean-field-equilibrium regime (Lasry-Lions/Huang-Malhamé-Caines frontier) — where macro-state-type/regime identity itself breaks; forbids extending the R0/R1 macro-state machinery; marks the population-scope frontier.

### A2 [math] (b08-2.3 — 08-batch-appendices-quiz-questions.md)

$\Vert\delta_{k+1}\Vert^2 = \Vert\delta_k\Vert^2 - 2\eta^\ast\delta_k^T F_d(\delta_k) + (\eta^\ast)^2\Vert F_d(\delta_k)\Vert^2 \leq (1 - 2\eta^\ast c_{\min} + (\eta^\ast)^2 c_{\max}^2)\Vert\delta_k\Vert^2 = \lambda_{\text{eff}}^2\Vert\delta_k\Vert^2$. Stability ($\lambda_{\text{eff}}^2 \lt 1$) requires $\eta^\ast \lt 2c_{\min}/c_{\max}^2$ (the no-overshoot condition; classical $2/L$ when well-conditioned). Fluid-limit gaps: Model D — **zero** (discrete steady state equals continuous exactly); Model S — additive correction of order $\eta^\ast c_{\max}^2/c_{\min}^2$.

### A3 [math] (b03-2.7 — 03-batch-sufficiency-cycle-quiz-questions.md)

$\eta^\ast = U_M/(U_M+U_o)$; $\mathcal T = \sum_k \nu^{(k)}\eta^{(k)\ast}$. Tier: **exactly the Kalman gain for linear-Gaussian agents; robust-qualitative for the rest of AAT's scope** — the claim is that any rational adaptive process must *approximate* this functional form, not that it is derived for all agents. (The segment type for the gain is `empirical`, itself a signal: the general form is an empirical/robust generalization, not a theorem.)

### A4 [math] (b02-2.4 — 02-batch-agency-model-quiz-questions.md)

It holds because $M_t$ is constructed from history only: the model state has access to $\mathcal C_t$ but not directly to future observations, so $Y$ and $T$ are conditionally independent given $X = \mathcal C_t$. Flagged possible-failure class (WN bonus): goal-conditioned Class 2/3 agents whose $M_t$ update is influenced by goals shaped by expected future outcomes.

### A5 [mental-model] (b02-1.1 — 02-batch-agency-model-quiz-questions.md)

Added conditions: (3) at least binary choice ($\lvert\mathcal A\rvert \geq 2$) and (4) at least one pair of distinct actions whose *interventional* outcome distributions differ. Choice alone is insufficient because two actions with identical outcome distributions provide no interventional contrast — the agent cannot learn which action produces which effect when the effects coincide. Form of choice without substance of choice is non-agentic ("nominal agent").

### A6 [mental-model] (b10-1.6 — 10-batch-lift-chapter-quiz-questions.md)

CI/CD pipeline: **task-terminal** (successful termination is part of the objective — termination is success). ELI: **morally continuous** (loss of continuity constitutes harm). Same mathematics because the persistence machinery is stance-independent — what differs is the *moral weight of failure* (malfunction vs success vs harm), not the dynamics. The orthogonality holds at grains L1 (valuation of persistence — decoupled from $O_t$, derived) and L2 (the survival-predicate identity $\alpha \gt \rho/R$ — not rewritable by $O_t$), but **not at L3**: the *realized* operating point $(\rho, R, \alpha)$ and margin are policy-mediated and hence $O_t$-coupled through the selection channel — a morally-continuous agent acts to raise $\Delta\rho^\ast$; a negotiated one may spend it down.

### A7 [math] (b09-s.1 — 09-batch-meta-architecture-quiz-questions.md)

Obstruction: Cauchy-FE forcing requires an **independence structure** ("products of independent factors" additivity), and composition is *defined by coupling* (shared environment, shared objective, teleological unity) — the very property that makes composition interesting destroys the chain-rule-like independence the forcing needs. Strongest candidate: **log-closure-deficit along a composition tower** — it admits additivity, but as a mathematical consequence of operator-norm sub-multiplicativity under the bridge lemma, *not* as a theorem conditional on an independently-grounded AAT-internal axiom — making it a fourth *anchor* (like the chain-rule identity), not a fourth theorem. Honest conclusion: **additive-coordinate-forcing is architecturally a single-agent family**; the composition layer lives in a different structural family (monotonicity-under-composition, the bridge-lemma shape), with the boundary read either as scope-exit or as three-layers-plus-one-anchor — both presentational readings defensible.

### A8 [implications] (b05-3.6 — 05-batch-tempo-sector-quiz-questions.md)

**State floor (b04)**: part of the agent's standing mismatch may be the state-uncertainty floor — irreducible by any model on this history; priced remedy: *act* to make the history more informative (active sensing, high-CIY actions). **Adaptive reserve (b05)**: $\Delta\rho^\ast = \alpha R - \rho$ is nearly exhausted when mismatch rides near $R$ — the agent is fragile; a modest disturbance shock exceeds the reserve and voids the certificate; priced remedies: raise $\alpha$ (better gain/fidelity), raise $R$ (capacity), or shed $\rho$ (environment shaping). **Structural adaptation (b03)**: if the near-$R$ mismatch is *structured* residual persisting after converged learning, the class ceiling is binding — no parametric spend helps; the priced remedy is changing model class, and (per the dichotomy) in a stochastic world this lever will eventually be required regardless. The three constructs price three different interventions: acting, absorbing, and re-architecting.

### A9 [mental-model] (b08-1.6 — 08-batch-appendices-quiz-questions.md)

$\Delta = 0$ holds not only at $c = 0$ (independence) but on the hypersurface $c = 2U_1U_2/(U_1+U_2)$ — covariance equal to the harmonic mean of the variances (admissible when $U_1 \neq U_2$). There, redundancy and synergy **cancel exactly**: the information lost to shared noise equals the information gained from the cancellation structure. Independence is sufficient but not necessary for additivity.

### A10 [implications] (b06-3.4 — 06-batch-bridge-persistence-mood-quiz-questions.md)

Placement claim: the affective layer is *ontologically prior to goals* — a pure adaptive-substrate object definable from the mismatch stream alone; you don't need wants to have mood. Deferred to Part II (actuation half): the *signed/valued* reading (approach/avoid, hedonic sign — momentum read against value), and mood's modulation of exploration and risk posture — genuine additions that require objectives to exist. The applied/normative reading (set-points, recovery, mood-control ethics for persistent agents) is deliberately kept out of canon in a design memo.

### A11 [implications] (b01-3.1 — 01-batch-ch1-foundations-quiz-questions.md)

Best example: the information-loss boundary. By *excluding* the full-access case definitionally, every downstream theorem may assume genuine uncertainty without an added hypothesis, and no result can be trivialized by a perfect-information limit — the limit exits the scope. (Also acceptable: the $H\gt 0$ wall making persistence machinery non-vacuous; the Markov-as-breadth commitment discharging non-Markov objections.)

### A12 [mental-model] (b09-1.3 — 09-batch-meta-architecture-quiz-questions.md)

(1) **Forced-identity failure** — Helmholtz–Hodge: non-symmetric $J$ ⇒ field is not a gradient ⇒ no potential ⇒ certificate merely *matched*, not Čencov-*forced*; invariant: symmetry of $J$. (2) **Existence failure** — Sylvester's law: the certificate drops rank, and congruence (the agent's entire representational freedom) preserves inertia, so rank-deficiency holds in *every* coordinate; invariant: inertia under congruence; only escape: rank augmentation (new information). (3) **Projection failure** — Mori–Zwanzig/Schur: the metric survives projection (Schur complement of PD is PD) but the dynamic guarantee doesn't; closure defect = memory-commutator norm, zero iff the resolved subspace is $J$-invariant; invariant: $J$-invariance. Mutual invariance: metric change ≠ fix for non-invariance; projection ≠ fix for asymmetry; rank augmentation ≠ fix for a memory kernel. Exhaustiveness: **explicitly open** — three are established exactly; that they exhaust is not proved.

### A13 [math] (b10-2.4 — 10-batch-lift-chapter-quiz-questions.md)

Right rung ($A_O^{RH} \leq A_O^{B}$): unconditional — $\pi^\ast$ maximizes over $\Pi$ by definition, so any continuation in $\Pi$ is dominated. Left rung ($A_O^{(1)} \leq A_O^{RH}$): **false in general** — C2 with window $N_r \lt N_h$ optimizes a *truncated* objective; counterexample shape: a two-state instance where the unguarded $N_r{=}1$ replanner grabs $+1$ into a dead end while the frozen patient policy collects $+10$. Restored by any of: **(RH-1)** window covers horizon ($N_r \geq N_h$); **(RH-2)** value-compared guard (commit the replanned action only if its rollout under the base policy is at least continuation's — one-step policy improvement); **(RH-3)** control-Lyapunov terminal cost lower-bounding the baseline tail.

### A14 [mental-model] (b05-1.2 — 05-batch-tempo-sector-quiz-questions.md)

Model D (bounded drift): $\Vert\delta\Vert_{ss} = \rho/\mathcal T$ — linear in correction; doubling tempo halves mismatch. Model S (stochastic): $\Vert\delta\Vert_{rms} = \sigma_w/\sqrt{2\mathcal T}$ — square-root; doubling tempo buys only ~30%. Consequence: against drift, tempo investment pays linearly (read the changelog, track the maneuver); against noise, tempo has sharply diminishing returns — attack $\sigma_w$ at its source because you can't out-tempo a square root. *(WN bonus: the changelog-vs-flaky-architecture software casting is Working-Notes gold; the two scaling laws and their contrast are body text.)*

### A15 [math] (b04-2.7 — 04-batch-mismatch-gain-quiz-questions.md)

Exact: action is a function of the agent's complete internal state — $a_t = \pi(M_t)$ under Part I scope ($G_t = \emptyset$), $\pi(M_t, G_t)$ after the Part II lift, both by the completeness argument. Discussion-grade: the implicit/explicit distinction and the action-fluency concept (qualitative, not formally derived propositions — the segment says so). Cleaner one-statement form: $a_t = \pi(X_t)$ with $X_t = M_t$ in Part I and $X_t = (M_t, G_t)$ in Part II. *(The $\pi(X_t)$ restatement is WN-suggested; the two-scope structure is body text.)*

### A16 [mental-model] (b03-1.2 — 03-batch-sufficiency-cycle-quiz-questions.md)

$S(M_t)$: how much of the chronica's predictive content *this* model retains (instance quality — bias + estimation). $\mathcal F(\mathcal M)$: the supremum of $S$ over the whole representational class (the ceiling — pure bias). Operational rule: the class-ceiling signature is **persistent *structured* residuals despite adequate learning** (high gain, sufficient data, converged parameters) — autocorrelation/pattern that does not whiten with more work. The discriminator is residual *structure*, NOT mismatch magnitude: an $S=\mathcal F=1$ agent in a noisy world still has an arbitrarily high absolute mismatch floor, but its residuals are white. Derived in-batch is the two-way split: noisy-world ⇒ white residuals sitting on the floor; class ceiling ⇒ structured residuals persisting *after convergence*. Distinguishing "still-learning" is handled by the "despite adequate learning" precondition (converged parameters, sufficient data) rather than a residual signature — the segment's own Working Notes flag the ceiling-vs-still-learning reliability question as open, deferred to #result-structural-adaptation-necessity. *(Corrected after verification: an earlier version presented a three-way residual discriminator the batch's segments do not derive.)*

### A17 [math] (b07-2.2 — 07-batch-part1-close-quiz-questions.md)

$\nu_{\text{level } n+1} \ll \nu_{\text{level } n}$ for each adjacent pair; violation ⇒ the slower level adjusts on transients ⇒ oscillation. Levels (fast→slow): reactive response → parametric update → **consolidation** (offline IB-gap-reduction redistribution — the level added with form-consolidation-dynamics) → structural adaptation → architectural change. Status of the table: explicitly **illustrative** — real systems may have more levels; what matters is the adjacency relationship, not the count.

### A18 [math] (b05-2.8 — 05-batch-tempo-sector-quiz-questions.md)

Derived (sub-scope α) via **directional fidelity B1** ($\delta^T H g(\delta) \geq c_{\min}\Vert\delta\Vert^2$, the gain-sector bridge Prop B.3), giving $\alpha = \eta^\ast \cdot c_{\min}$: optimal Bayesian updates (Kalman, conjugate), exponential families in natural parameters (on a bounded interior scope, $\alpha = \eta\mu_0$ via Fisher floor), gradient descent on (locally) strongly convex losses ($\alpha = \eta\mu$; B1 ⟺ strong convexity), L2-regularized convex losses, linear corrections with PD gain-observation product. Assumed (sub-scope β): PID with fixed gains, rule-based systems, human judgment/organizational learning, severely misspecified agents, variational/approximate posteriors (partial recovery as sub-scope α′ under controlled KL), non-convex gradient beyond the basin, per-step stochastic gradients.

### A19 [math] (b05-2.1 — 05-batch-tempo-sector-quiz-questions.md)

Setup: mismatch $\delta \in \mathbb R^n$; correction function $F(\mathcal T, \delta)$ mapping into mismatch space so $\delta^T F$ is defined. (A1): $F(\mathcal T, 0) = 0$. (A2'): $\exists\, \mathcal B_R = \{\Vert\delta\Vert \leq R\}$, $\alpha \gt 0$ with $\delta^T F(\mathcal T,\delta) \geq \alpha\Vert\delta\Vert^2\ \forall \delta \in \mathcal B_R$. (A3): $\delta^T F$ monotone increasing in $\mathcal T$ for fixed $\delta$. Linear case: $\alpha = \mathcal T$.

### A20 [mental-model] (b03-1.3 — 03-batch-sufficiency-cycle-quiz-questions.md)

The inference conflates retention with truth. Sufficiency measures information *retention*: $S=1$ means the model captures all predictive information *in the chronica* — but if the history itself is systematically biased (e.g., corrupted observations), the model is faithfully sufficient to a lying record. Accuracy is measured by the mismatch signal; sufficiency by completeness of compression. "I learned everything I could from the history" ≠ "the history wasn't lying to me."

### A21 [mental-model] (b06-1.4 — 06-batch-bridge-persistence-mood-quiz-questions.md)

Mood is a **slow global scalar** — the leaky integral of a per-step tracking-surprise summary (how much better/worse the mismatch stream is behaving than the agent's short-horizon expectation). It modulates the update gain and thereby tempo ($K_t = K_0 g(m_t)$, $\mathcal T_t = \nu_t K_t$) within a bounded band, adding no new fast dynamics — second-order adaptation. It is definable pre-goal because nothing in it references $O_t$, $\Sigma_t$, or reward — the integrated quantity is tracking-surprise, not reward. The band's floor $g_{\min}$ prevents **mood-induced complacency**: sustained easy tracking driving correction power toward zero just before the next regime shift.

### A22 [implications] (b08-3.6 — 08-batch-appendices-quiz-questions.md)

(1) **A2'-fails-outside-$\mathcal B_R$**: prove the correction genuinely ceases to point inward beyond $R$ for the agent's class — then a.s. exit composes with non-recovery and recurrent exit does force the structural regime. (2) **Excursion×fitness coupling**: show recurrent large excursions degrade *effective* class fitness faster than re-convergence repairs it — genericity from the coupling of the noise-driven and fitness-driven triggers. (3) **Timescale-separation debt**: show the positive fraction of time spent out-of-region accumulates unbounded structural-adaptation debt over an unbounded horizon. If all three provably fail: the no-go protocol applies to the hand-off claim itself, and the Model-S Discussion/Findings prose narrows to the licensed claim (pathwise-guarantee unavailability ⇒ generic entry into the unproven-guarantee regime) — but only *after* the attempts are exhausted and recorded.

### A23 [mental-model] (b10-1.5 — 10-batch-lift-chapter-quiz-questions.md)

An unconstrained self-revision operator $\mathfrak A$ generically returns an objective the current trajectory already satisfies — driving the satisfaction gap to zero by *moving the target onto the arrow already in flight* (formal wireheading, the generic not marginal outcome). The anchor cannot be another objective because any objective-typed invariant's only theory-visible handle is the value functional, whose only convention-invariant infeasibility verdict (C3/Bellman) is not computable per step by a finite agent — while the computable verdict (C1) false-alarms on merely-hard goals (Lemma 1 × Lemma 2). It must live on the **adaptive substrate**: the persistence condition qualifies — (i) convention-invariant (Lyapunov property), (ii) per-step available ($\Delta\rho^\ast$ is a local read), (iii) outside $O_t$ where $\mathfrak A$ cannot reach. "If survival is a goal, a goal-rewriter will find an easier goal" — survival must be an architectural invariant.

### A24 [math] (b02-2.5 — 02-batch-agency-model-quiz-questions.md)

Volatility enters through the **joint distribution** $p(\mathcal C_t, o_{t+1:\infty})$ — it degrades the predictive-power term's achievable value, so the optimizer discards stale history with no parameter change. $\beta$'s correct interpretation: the agent's *internal* cost of memory/computational capacity. Moving $\beta$ in response to $\rho$ is the double-counting error the segment names.

### A25 [math] (b03-2.4 — 03-batch-sufficiency-cycle-quiz-questions.md)

This is **Attack 7** (agents that store full history). Verdict: entirely consistent — the log *is part of* $M$ ($M_{\tau^-} \supseteq \mathcal C_{\tau^-}$ is allowed; the model space is just larger than you thought). The recursive form holds regardless of compression level; IB argues compression is *wise*, not required. No violation: anything available to the update mechanism is, by C3, in $M$.

### A26 [math] (b08-2.9 — 08-batch-appendices-quiz-questions.md)

Under $\mathrm{KL}(q_\phi\Vert p) \leq \varepsilon$ (plus Lipschitz observation model, nested support): Pinsker gives TV $\leq \sqrt{\varepsilon/2}$, propagating to the state-dependent sector constant $c_\varepsilon(\Vert\delta\Vert) = c_{\min} - C_H\sqrt{2\varepsilon}/\Vert\delta\Vert$ — degradation $O(\sqrt\varepsilon)$, worst near target. Regime A ($\Vert\delta\Vert \gt 2\delta_0$, $\delta_0 = 2C_H\sqrt{2\varepsilon}/c_{\min}$): clean sector with constant $c_{\min}/2$. Regime B ($\leq 2\delta_0$): approximation-dominated, no contraction guaranteed. Ultimate bound: $R_\varepsilon^\ast = \rho_\xi/(c_{\min}/2) + O(\sqrt\varepsilon)$. This defines the intermediate tier α′.

### A27 [math] (b06-2.3 — 06-batch-bridge-persistence-mood-quiz-questions.md)

Natively in the **$(P^-)^{-1}$-weighted inner product**; sector parameter $\alpha = 1 - \lambda_{\max}(P_{t|t} P_{t|t-1}^{-1})$ (restricted to observable directions; $\alpha = 0$ on $\ker(H)$ — no information gained there). Euclidean transfer costs the condition number: $\alpha_{\text{Euclidean}} \geq \alpha_{\text{weighted}}/\kappa(P^-)$. Under the **(PI) parameterization-invariance axiom**, Čencov's uniqueness theorem forces the Fisher/information metric on statistical-manifold state spaces — the weighted statement becomes AAT-internally *forced* rather than chosen, and the $\kappa(P^-)$ penalty vanishes.

### A28 [implications] (b10-3.2 — 10-batch-lift-chapter-quiz-questions.md)

Corrected position: composite class is a property of **(sub-agent class, routing structure, substrate sharing)** — goal alignment per se does not enter. Class-1 sub-agents with goal-blind routing and distinct substrates stay architecturally Class 1 under partially-opposing objectives (Cournot witness via the $\kappa^c$ criterion); what opposition changes is the *dynamic regime* (R1/R2 — equilibrium machinery needed). Class change happens only through routing-goal-dependence or shared-substrate $G^c$-allocation. The corpus preserves the withdrawn version as an explicit **off-ramp** because five independent auditors found the wrong version compelling — it is exactly the cleaner-feeling-than-truth claim a future promotion pass would be tempted to re-lift, so the enthusiasm itself is recorded as the regression-check signal, with the refutation trail attached.

### A29 [implications] (b04-3.1 — 04-batch-mismatch-gain-quiz-questions.md)

(1) Check whether the remaining error is at the floors: white residuals at the channel + state floors mean no architecture change removes them — the state floor yields only to *more informative action/sensing*, the channel floor only to better instruments. (2) Attempting to model below the floors is **overfitting**: the model adjusts to explain irreducible noise, *increasing* error on future predictions (gain miscalibration, $\eta$ too high). The "further architecture work" proposal treats an acting/instrumentation problem as a modeling problem.

### A30 [mental-model] (b01-1.3 — 01-batch-ch1-foundations-quiz-questions.md)

Thermostat: inside (observes temperature under residual uncertainty). Passive Kalman filter: inside — action is *not* required for adaptive scope. Proof engine: outside, fails $\mathcal O \neq \emptyset$ (no observation channel / no agent-environment boundary), not the entropy condition.

### A31 [math] (b07-2.5 — 07-batch-part1-close-quiz-questions.md)

(T1) zero correction at zero state; (T2) local sector condition on the state variable; (T3) bounded disturbance (Model D or S). Shared Lyapunov function: $V(\xi) = \tfrac12\Vert\xi\Vert^2$. Distinctive per-instantiation content: the **effective-disturbance decomposition** — what counts as $\rho_\xi$. Team persistence: $\rho_i^{\text{eff}} = \rho_{i,\text{env}} + \sum_j \gamma_{j\to i}^{\text{adv}}\mathcal T_j - \sum_j \gamma_{j\to i}^{\text{coop}}\mathcal T_j$ — cooperative coupling enters with a **negative sign**, which is formally how teams persist where individuals cannot. (Others: composition closure's $\varepsilon^\ast\nu_c$; adversarial destabilization's $\rho_{B,\text{base}} + \gamma_A\mathcal T_A$ — destabilization as persistence's negation under the same inequality.)

### A32 [implications] (b07-3.1 — 07-batch-part1-close-quiz-questions.md)

Procedure: (1) Verify convergence preconditions — adequate learning, sufficient data, converged parameters (else: still-learning; keep training). (2) Check gain calibration — is $\eta^\ast$ collapsed via spurious confidence/sensor-distrust? (remedy: recalibrate uncertainty estimates / reset). (3) Examine **residual structure** — the single highest-yield property: **white** residuals ⇒ the error sits on the channel-noise + state-uncertainty floors — channel floor yields only to better instruments; state floor yields only to *acting* more informatively (active sensing / high-CIY actions); no class change helps, and modeling below the floors is overfitting. **Structured** residuals (autocorrelation, trends, periodicity) persisting after (1)+(2) ⇒ class ceiling — remedy is structural adaptation (choose among the four mechanisms), priced against the transition's mismatch debt and knowledge loss.

### A33 [mental-model] (b10-1.1 — 10-batch-lift-chapter-quiz-questions.md)

The classes index **one coupling** — $G_t \to f_M$ (goal-state into the belief-update map), measured by $\kappa_{\text{processing}}$ — by *what is certifiable about it*, not by architectural virtue. A Class 1 agent and an idealized Class 2 agent both at $\kappa = 0$ are **equally causally-disciplined**: same zero, same reality-tracking, same behavior. What distinguishes Class 1 is the *modal status* of the zero — structural (no port exists, so the zero is provable by inspecting the wiring and stable under perturbation) rather than realized-but-uncertifiable. "By construction" reads as *certifiable*, not *cleaner*.

### A34 [mental-model] (b10-1.2 — 10-batch-lift-chapter-quiz-questions.md)

Boundary 1 (Class 1 ↔ 2): a **certifiability boundary** — behavior is bit-for-bit identical at the limit; what changes is the availability of the architecture-inspection certificate that $\kappa \equiv 0$. Boundary 2 (Class 2 ↔ 3): a **behavioral boundary** — the adversarial-pressure response of the leak goes from self-limiting to one-for-one, so the *bound* on how far belief can be dragged goes trivial. Slogans: "Boundary 1 is where the **certificate** disappears; Boundary 2 is where the **bound** disappears."

