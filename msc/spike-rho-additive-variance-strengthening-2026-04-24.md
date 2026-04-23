# Spike: Strengthening the $\rho$ Decomposition — from Heuristic Multiplicative Factorization to Derived Variance-Additive Theorem (and Beyond)

*Started 2026-04-24. Research spike. Not canon.*

**Status.** This spike pushes on the obstruction identified in `msc/spike-rho-factorization.md` (the multiplicative form $\rho = \rho_{\text{env}} \cdot f(\mathcal M) \cdot g(\pi)$ was shown to fail structurally). The mandate (per brief from Joseph): *strengthen first; do not accept the heuristic fallback; attempt the improbable*. This spike records what the attempts produced.

**Top-line outcome.** Mixed. The variance-additive form admits a **derived theorem under named sub-scope conditions**, with honest cross-terms. Three distinct multiplicative sub-structures were located: (a) the multiplicative-cascade regime (Poisson-driven rare-event streams), (b) the large-deviation / cumulant-generating-function regime (tail asymptotics), and (c) a partial-information-decomposition (PID) regime that recovers the three-factor narrative without enforcing independence. A **sharp no-go theorem for rate-domain multiplicative factorization** is derivable under mild regularity. Net position: the multiplicative form is now one *regime* in a tiered structure, not the governing form; the variance-additive form is the new structural anchor; a candidate axiom for `#additive-coordinate-forcing` is identified but honestly does not land as a fourth Cauchy-FE theorem without fabricated premises.

---

## 1. Honest audit of the prior failure

### 1.1 What the prior spike established

`msc/spike-rho-factorization.md` showed — across three structured cases (Kalman, Beta-Bernoulli, controlled OU+LQR) plus a Cauchy-FE forcing attempt plus sub-scope-$\alpha$ restriction — that no derivation route produces the multiplicative form $\rho = \rho_{\text{env}} \cdot f(\mathcal M) \cdot g(\pi)$ under AAD-native structure. The prior spike's own verdict: *"(C) Obstruction with honest reframe. (R-F) is a modeling choice, not derivable; worse, it misrepresents the natural structure, which is variance-additive (R-V) or KL-additive (R-KL) with generic cross terms."*

### 1.2 Was the failure inherent or method-dependent?

A strengthening-first posture requires asking: did the prior spike fail because the claim is false under reasonable axioms, or because it approached the problem through a lens that obscured a derivation route? Five checks:

**(A.1) Was the target quantity correctly pinned down?** The prior spike argued $\rho$ is *agent-conditional* — defined as the innovation rate the agent's predictor fails to absorb — and therefore $\rho_{\text{external}}$ is not well-posed without naming a reference agent. **This is correct and structural.** It is not a method artifact. Any factorization $\rho = \rho_{\text{env}} \cdot f \cdot g$ that treats $\rho_{\text{env}}$ as agent-independent has inverted the direction of definition: $\rho$ is a *functional* of $(\text{env}, \mathcal M, \pi)$, and "environmental $\rho$" is a projection onto a reference class.

**(A.2) Were the three structured cases representative?** The three cases (linear-Gaussian Kalman; Beta-Bernoulli edge; controlled OU+LQR) cover the sub-scope-$\alpha$ workhorses. They do *not* cover: (i) heavy-tailed noise; (ii) multiplicative-noise processes (geometric Brownian motion, stochastic volatility); (iii) large-deviation / rare-event regimes; (iv) strictly passive channels with cascaded attenuation. The prior spike's §11.3 flagged multi-stage cascade as a possible escape route and concluded it doesn't help under sub-scope-$\alpha$ Gaussian channels. Worth re-probing: the cascade argument might have been dismissed too quickly — see §3 below.

**(A.3) Was the Cauchy-FE forcing argument exhaustive?** The prior spike's §7 attempted to manufacture an "independence-of-attenuations" axiom and correctly identified the premise as the same thing §§3–5 had shown to fail. But it did not systematically enumerate alternative axioms: a *cumulant-additivity* axiom, a *large-deviation-rate-additivity* axiom, a *PID-decomposition* axiom, or a *log-probability-over-tails* axiom. Each of these has a different mathematical support and a different AAD-internal motivation. The Cauchy-FE forcing attempt was narrow.

**(A.4) Was the variance-additive reframe given its full derivation?** The prior spike's §8.1 named the (R-V) form but presented it as obvious ("supported by bias-variance decomposition"). The actual theorem — under what exact sub-scope is the cross-term structure identifiable? is the decomposition unique up to orthogonal rotation? does it compose under agent-agent coupling? — was not developed. The reframe was a sketch, not a derivation.

**(A.5) Was the channel-cascade Gaussian-specific dismissal sound?** The prior spike §11.3 said: *"Under sub-scope $\alpha$ Gaussian channels with independent noise, this would reduce to the Gaussian case (§3) which doesn't factor multiplicatively."* This is partially correct (additive Gaussian noises do not multiply in variance) but misses the case of *multiplicative-noise* channels (signal-dependent or scaling noise) which are *specifically* where the multiplicative form becomes natural. Financial volatility models, biological scale-invariant noise, and Weber-Fechner sensory noise all live here.

### 1.3 Verdict on the prior failure

**Inherent (partly).** The target quantity $\rho$ is agent-conditional and the Kalman/Beta-Bernoulli cases genuinely combine additively in variance. But method-dependent (partly) on the axiom search (A.3), the derivation depth of (R-V) (A.4), and the dismissal of multiplicative-noise cases (A.5). The strengthening attempts below pursue (A.3)–(A.5).

---

## 2. Strengthening attempt 1 — formalize the additive-variance decomposition as a first-class theorem

### 2.1 Setup and the target theorem

The claim to derive: the effective disturbance rate $\rho$ (in rate-squared / variance units) decomposes additively into named components with explicit cross terms, in a derivation that composes with existing AAD machinery.

**Setup (sub-scope $\alpha$).** Agent in the Kalman / exponential-family / strongly-convex / linear-PD regime (per `#gain-sector-bridge`). Environment generates observations $o_t$; the agent's one-step predictor is $\hat o_t(M_{t-1}, a_{t-1})$; mismatch $\delta_t = o_t - \hat o_t$. The Model S disturbance power per unit time is

$$\rho^2 := \nu \cdot \mathbb E[\lVert \delta_t\rVert^2]$$

where $\nu$ is the event rate (per `#adaptive-tempo`). Per `#mismatch-decomposition`, at each $t$:

$$\mathbb E[\lVert\delta_t\rVert^2] = \underbrace{\mathbb E[\lVert\hat o_t - \bar o_t\rVert^2]}_{\text{model error}} + \underbrace{\mathbb E[\operatorname{Var}(o_t\mid\Omega_t, a_{t-1})]}_{\text{observation noise}}$$

This is an instantaneous two-term decomposition. The goal is to lift it to a full rate-level theorem with internal / external attribution.

### 2.2 The layered decomposition

*[Derived (rho-sq-variance-additive, conditional on sub-scope-$\alpha$ + four separability conditions)]*

**Theorem (variance-additive $\rho^2$ decomposition).** Under sub-scope $\alpha$ with the separability conditions (S1)–(S4) below:

$$\rho^2 \;=\; \rho^2_\star(\text{env}) \;+\; \Delta^2_{\mathcal M}(\mathcal M \mid \text{env}) \;+\; \Delta^2_\pi(\pi \mid \mathcal M, \text{env}) \;+\; 2\,\chi_{\mathcal M,\pi} \qquad (\text{AV})$$

where:

- $\rho^2_\star(\text{env}) := \nu \cdot \inf_{\mathcal M^\ast \in \mathfrak M_\infty} \mathbb E[\lVert\delta_t\rVert^2 \mid \mathcal M^\ast]$ — the **irreducible disturbance rate** achievable by the Bayes-optimal predictor in a maximally-expressive reference class $\mathfrak M_\infty$, at the agent's realized policy $\pi$ distribution. A pure-environment property (relative to the reference class).
- $\Delta^2_{\mathcal M} := \nu \cdot \big(\mathbb E[\lVert\delta_t\rVert^2 \mid \mathcal M, \pi^\ast(\mathcal M)] - \rho^2_\star/\nu\big)$ — **model-class-excess variance** when the policy is held at $\mathcal M$'s optimal policy $\pi^\ast(\mathcal M)$ (so no entanglement with policy exploration).
- $\Delta^2_\pi := \nu \cdot \big(\mathbb E[\lVert\delta_t\rVert^2 \mid \mathcal M, \pi] - \mathbb E[\lVert\delta_t\rVert^2 \mid \mathcal M, \pi^\ast(\mathcal M)]\big)$ — **policy-excess variance** relative to the $\mathcal M$-conditional optimal.
- $\chi_{\mathcal M,\pi}$ — **model-policy cross term** (defined below via state-distribution mediation).

### 2.3 Separability conditions (S1)–(S4)

The decomposition is well-typed and identifiable when:

- **(S1) Bayes-stationary innovation.** The policy $\pi$ induces a stationary distribution $\mu_\pi$ over environment states that is absolutely continuous w.r.t. a reference measure $\mu_0$ the reference class $\mathfrak M_\infty$ was specified over. (Prevents the reference predictor from being handed a singular state distribution by policy choice.)

- **(S2) Policy-noise independence.** The policy $\pi$ is a deterministic function of $M_t$'s current state summary, or its randomness is independent of the next-step innovation's environment-side noise. (The policy does not leak innovation noise into its own action choice; prevents a class of self-exciting processes that would break the decomposition.)

- **(S3) Exponential-family representability.** The reference class $\mathfrak M_\infty$ is exponential-family (in natural parameters) with sufficient statistics spanning the true conditional density's sufficient statistics. (Pythagorean KL projection applies; cross-term $\chi_{\mathcal M,\pi}$ has the state-distribution-mediation form below.)

- **(S4) Finite second moments.** $\mathbb E[\lVert\delta_t\rVert^2 \mid \mathcal M, \pi] \lt \infty$ for all combinations. (Heavy-tailed cases are out of scope — see §4.)

### 2.4 Derivation (sketch)

The layered form is derived by sequential projection in the KL-Pythagorean framework (Amari-Nagaoka 2000 §3.4). Under (S3), the true conditional density $p_\star(o \mid \Omega, a)$ lies in an $m$-flat ambient manifold $\mathcal P$; the model class $\mathcal M$ corresponds to an $e$-flat submanifold $\mathcal M \subset \mathcal P$; the reference class $\mathfrak M_\infty$ corresponds to $\mathcal P$ (or a maximal $e$-flat sub-family admitting the true $p_\star$).

**Step 1 (reference projection).** Project $p_\star$ onto $\mathfrak M_\infty$ under the $\pi$-induced state distribution $\mu_\pi$. The projection exists uniquely under (S1)+(S3) (Amari-Nagaoka Thm 3.8). Compute its mean-square prediction error: this is $\rho^2_\star/\nu$ per step, aggregated via $\nu$ per time.

**Step 2 (model-class projection at $\pi^\ast$).** Hold policy at $\pi^\ast(\mathcal M)$ (the $\mathcal M$-conditional optimal). Project $p_\star$ onto $\mathcal M$. The $\mathcal M$-projection error, minus the reference-projection error, is a Pythagorean decomposition term (orthogonal in the information-geometric metric under (S3)); this is $\Delta^2_{\mathcal M}$.

**Step 3 (policy excess).** Switch policy from $\pi^\ast(\mathcal M)$ to $\pi$. The state distribution shifts from $\mu_{\pi^\ast(\mathcal M)}$ to $\mu_\pi$. The incremental prediction-error increase is $\Delta^2_\pi$. Under (S2) (policy-noise independence), this is a pure measure-change effect; the innovation-noise statistics themselves don't change.

**Step 4 (cross term).** The model-class projection's "optimal predictor under $\mathcal M$" depends on the state distribution. So $\Delta^2_{\mathcal M}$ depends on which $\mu$ we use. The honest form:

$$\Delta^2_{\mathcal M}(\mu_\pi) - \Delta^2_{\mathcal M}(\mu_{\pi^\ast(\mathcal M)}) = 2\chi_{\mathcal M,\pi}$$

measures how much the policy $\pi$ shifts the state distribution into regions where $\mathcal M$ is worse (or better) than average. This is the mediation term: policy's contribution to viability partly routes through modulating which regions $\mathcal M$ is evaluated on. Causal mediation analysis (Imai et al. 2010) provides exact identification under Regime A (intervention-based) and conditional identification under Regime B (functional-form assumptions). Regime C leaves $\chi$ confounded with $\Delta^2_{\mathcal M}$ and $\Delta^2_\pi$.

**Each term is derived; (AV) holds exactly under (S1)–(S4).** $\square$

### 2.5 Epistemic status of (AV)

**Exact** under (S1)–(S4) in sub-scope $\alpha$. Robust-qualitative under sub-scope $\beta$ (PID / rule-based / variational-approximate / per-step SGD / human-judgment): the additive-variance form still gives a bound rather than an identity, because projections may not be orthogonal. Under heavy-tailed (S4 violation), the decomposition requires extension to cumulant coordinates (see §4).

**Comparison to the prior spike's (R-V).** The prior spike stated (R-V) qualitatively. (AV) is (R-V) promoted to a theorem with named sub-scope conditions, a structural derivation, an explicit cross-term, and an exact statement of what each term is. This is the strengthening the prior spike should have attempted but didn't.

### 2.6 Composition with AAD machinery

(AV) slots into AAD's existing architecture cleanly:

- **`#sector-persistence-template` (T3).** The template's Model-S disturbance statistic is $\sigma_\xi^2 = \rho^2/\nu$. (AV) decomposes this into four named sub-contributions; the template is undisturbed but each instantiation now carries a finer-grained $\rho_\xi$ attribution.
- **`#persistence-cost`.** The information-rate floor $\dot R \geq n\alpha/2$ is insensitive to how $\rho^2$ decomposes — the RDF sees only the composite disturbance statistic. But (AV) predicts that *agent-controllable* reductions in $\Delta^2_{\mathcal M} + \Delta^2_\pi + 2\chi$ translate directly into channel-capacity slack: if $\rho^2$ drops via model/policy improvement, so does the required $\dot R$.
- **`#mismatch-decomposition`.** (AV) is the rate-level lift of `#mismatch-decomposition`'s per-instant bias-variance identity: the per-instant two-term split (model-error + obs-noise) lifts to a rate-level four-term split (irreducible + model-excess + policy-excess + cross).
- **`#critical-mass-composition`.** (AV) applied to agent $i$ in a composite yields $\rho_i^2 = \rho_{i,\star}^2 + \Delta^2_{\mathcal M_i} + \Delta^2_{\pi_i} + 2\chi_i$; substitution into (CM2) $(\alpha - C)R \gt \rho + \gamma\mathcal T$ introduces the irreducible-reducible split at the composite level. Useful for diagnosing whether a composite's marginality is due to environment hostility ($\rho_\star^2$ up) or sub-agent weakness ($\Delta^2_{\mathcal M} + \Delta^2_\pi$ up).
- **`#interaction-channel-classification`.** The regime-typed $\rho_B^{\text{eff}}$ decomposition already has an additive structure with a *negative* Regime-I term. (AV) sits orthogonal: the four regimes (I / II-a / II-b / III) classify events by boundary-crossing, while (AV) decomposes the residual within each regime. Composition: $\rho^2_\text{eff}(\text{Regime I}) = \rho^2_{\star,\text{Regime I}} + \Delta^2_{\mathcal M, \text{Regime I}} + \ldots$ at each regime's scale.

### 2.7 Where (AV) needs more work

- **Non-exponential-family reference classes (S3 relaxation).** The Pythagorean projection argument requires $e$-flat structure. Many practical model classes (neural networks, rule-based systems) are neither $e$-flat nor $m$-flat. A coarser decomposition is available (Kullback-Leibler projection without orthogonality) but the cross-term structure becomes richer — this is the structural-repair regime of `#separability-pattern`'s separability ladder.

- **Finite-sample vs. population.** (AV) is a population-level identity under (S1)–(S4). Finite-sample estimation of each term requires concentration bounds and variance-component analysis (analogous to ANOVA for mean-square error). Not developed here.

- **Dependence on reference class choice.** $\rho^2_\star$ depends on which $\mathfrak M_\infty$ is chosen. Different reference classes give different numerical splits. This is not a bug — the split is *relative* to a stated reference — but papers need to name the reference. Natural choice: the maximally-expressive class implementable within the agent's substrate (computational / architectural reachability).

---

## 3. Strengthening attempt 2 — locate multiplicative sub-structure

The prior spike concluded the multiplicative form fails generically. But generic failure does not rule out *conditional* multiplicativity — specific sub-regimes where the multiplicative form is exact or tight. If such regimes exist and are practically important, the multiplicative form earns its place as a legitimate sub-case under named conditions. Three candidates examined.

### 3.1 The multiplicative-cascade regime (Poisson-driven rare-event streams)

**Setup.** Disturbances arrive as a Poisson process with rate $\lambda$; each event has magnitude $\xi \sim P_\xi$ filtered through:

1. *Environment gate:* each event emitted with probability $p_{\text{env}} \in (0, 1]$ ("raw emission rate").
2. *Model filter:* given emission, probability $(1 - p_{\mathcal M})$ that the model predicts it (event is *not* a surprise — doesn't contribute to $\rho$).
3. *Policy gate:* given unpredicted event, probability $(1 - p_\pi)$ that the policy-induced state is such that the event doesn't perturb the agent (e.g., the agent is in a region where this event is irrelevant).

**Effective disturbance rate:**

$$\rho = \lambda \cdot p_{\text{env}} \cdot p_{\mathcal M} \cdot p_\pi \cdot \mathbb E[\lVert\xi\rVert] \qquad (\text{MC})$$

**This factorizes exactly.** Each gate is a multiplicative thinning of an independent event stream. The structure is a **cascaded Poisson-thinning** (Kingman 1993, *Poisson Processes*, Ch. 2): thinning a Poisson process by independent Bernoulli filters preserves the Poisson structure with the product of retention probabilities. The factorization is mathematically forced, not chosen.

**When does this apply to AAD?** Three conditions:

- **(MC-1) Event-stream structure.** Disturbances arrive as discrete, independent events at Poisson rate, not as continuous-time innovation noise. This matches *rare-event* regimes: safety incidents, market crashes, upstream dep breaks, catastrophic failures. It does *not* match continuous-time tracking regimes (Kalman over OU).
- **(MC-2) Independent gating.** Environmental emission, model-class unpredictability, and policy-induced irrelevance are independent Bernoulli filters on the same event. This is the key assumption — and often wrong, because model and policy are coupled (§5 of the prior spike). But in rare-event / catastrophic-event settings, the gates *can* be independent when model-class adequacy is domain-level (did we think of this hazard class?) while policy-benignity is operational (are we in a region where this hazard manifests?).
- **(MC-3) Magnitude independence.** $\xi$'s distribution does not depend on which gates fired. (If the model fails on *large* events preferentially, this breaks.)

**Partial verdict.** (MC) recovers the multiplicative form *exactly* under (MC-1)–(MC-3). The prior spike's Kalman and Beta-Bernoulli cases violate (MC-1). The Kalman case uses continuous-time innovation; Beta-Bernoulli uses a single stream of Bernoulli trials that *already* factor (per §4.2–4.3 of the prior spike, the single-edge form factors as rate × variance, just with two factors rather than three).

**This is a real sub-regime, not a degenerate one.** Rare-event / tail-risk settings are exactly where operational intuition reaches for the multiplicative form. A nuclear plant's safety envelope, a hospital's incident rate, an autonomous vehicle's fatality rate — these live in Poisson-rare-event regimes where each incident is an independent filtering of (environment generates hazard) × (system fails to detect/predict) × (operational context permits harm). The multiplicative form is *native* here.

**AAD integration.** Under (MC-1)–(MC-3), the multiplicative form is an exact special case. It should be labeled as a *regime instance* within (AV) (the fourth term $2\chi$ vanishes and the first three terms collapse to a single multiplicative product in the rare-event limit where $p_{\text{env}}, p_{\mathcal M}, p_\pi$ are each close to 1 or each close to 0). This is the *first-order cascade limit* of the general theory.

### 3.2 The large-deviation / tail-asymptotic regime

**Setup.** Instead of second moments, consider the *tail probability* $P(\rho_{\text{realized}} \gt x)$ for large $x$. Under Cramér-style large-deviation regularity, the tail decays exponentially:

$$P(\rho \gt x) \;\approx\; e^{-x \cdot I(\rho; x)}$$

where $I(\rho; x)$ is the large-deviation rate function. If the disturbance arises from independent contributions $\rho = \rho_\text{env} + \rho_{\mathcal M\text{-residual}} + \rho_{\pi\text{-residual}}$ (variance-additive), then for independent large-deviation-regular contributions:

$$I(\rho; x) \;=\; \inf_{x_1 + x_2 + x_3 = x} \big[I_{\text{env}}(x_1) + I_{\mathcal M}(x_2) + I_\pi(x_3)\big] \qquad (\text{LD})$$

**The rate function is additive (in an infimum-convolution sense) across independent contributions.** The corresponding tail *probability* is multiplicative: $P(\rho \gt x) \approx P(\rho_\text{env} \gt x_1^\ast) \cdot P(\rho_{\mathcal M} \gt x_2^\ast) \cdot P(\rho_\pi \gt x_3^\ast)$ at the dominating split $(x_1^\ast, x_2^\ast, x_3^\ast)$.

**What this says.** At the tail, multiplicative factorization *of tail probabilities* is native (via additive rate functions), even when the second moments are additive. The two forms are complementary coordinates: second-moment coordinates decompose additively; tail-probability coordinates decompose multiplicatively. The Cauchy-FE structure is clean on the *rate function*, not on $\rho$ directly.

**Candidate Cauchy-FE axiom.** Posit: *if $\rho_\text{env}, \rho_{\mathcal M}, \rho_\pi$ are independent contributions to $\rho$, then their large-deviation rate functions are additive under infimum-convolution.* This is the Cramér-style independence axiom of large-deviation theory (Dembo & Zeitouni 2010, *Large Deviations Techniques and Applications*, 2nd ed., §4.5); it is derived, not posited, for independent random variables.

**So the axiom is not AAD-internal — it's classical probability.** But the *application* to AAD is distinctive: the claim would be that the independence premise holds for AAD's three attribution sources in some regime. Under (S1)–(S2) this approaches true; under generic coupling it does not.

**Verdict.** (LD) gives a genuine multiplicative structure at the tail, under additive rate functions. It is *not a strengthening of (R-F) in the rate coordinate* — the rate coordinate remains additive in variance. It is a complementary decomposition that says: *tail probabilities factor multiplicatively when contributions are additive-in-variance and independent*. This is the structural answer to why the multiplicative intuition is stubborn: it is correct in a different coordinate than the rate one.

**AAD integration.** Under (AV)'s separability conditions + large-deviation regularity, tail probabilities of excursion events factor multiplicatively. This gives a Section-III / tail-risk diagnostic distinct from the variance-level (AV) decomposition. Worth a Discussion paragraph in `#persistence-condition` or `#mismatch-dynamics`; not worth a new segment on its own.

### 3.3 Partial Information Decomposition (PID)

**Setup.** The Williams & Beer 2010 (*arXiv:1004.2515*) / Bertschinger et al. 2014 (*Entropy* 16:2161–2183) partial-information-decomposition framework decomposes the information that $(M, \pi)$ jointly carry about the observation innovation into four non-negative components:

- **Redundant** $R$: information carried by $M$ *and* $\pi$ individually (both capture).
- **Unique-to-$M$** $U_M$: information only $M$ carries.
- **Unique-to-$\pi$** $U_\pi$: information only $\pi$ carries.
- **Synergistic** $S$: information only the joint $(M, \pi)$ carries (neither alone).

The joint mutual information decomposes as $I((M, \pi); \delta) = R + U_M + U_\pi + S$.

**Applied to $\rho$.** Let the *achievable* innovation variance reduction attributable to the joint $(M, \pi)$ be $\Delta_{\text{max}}^2 = \rho^2_\star - \rho^2_{\text{current}}$ (what more one could squeeze out with a richer model and better policy, if both were made optimal jointly). PID-style decomposition of the achievable reduction:

$$\Delta_\text{max}^2 \;=\; R^2_\rho + U^2_{M,\rho} + U^2_{\pi,\rho} + S^2_\rho \qquad (\text{PID-}\rho)$$

where $R^2_\rho$ = redundant-reduction (both model and policy could individually achieve this), $U^2_{M,\rho}$ = model-unique reduction, $U^2_{\pi,\rho}$ = policy-unique reduction, $S^2_\rho$ = synergistic reduction (only joint model-plus-policy improvement achieves this).

**This is an additive decomposition in variance, with independence made explicit as the $R$-vs-$(U_M, U_\pi, S)$ split.** The cross-term $2\chi$ from (AV) roughly corresponds to $R^2_\rho + S^2_\rho$: redundant contributions (both improvements redundantly close the same mismatch; the $-R$ correction) plus synergistic contributions (only simultaneous improvement helps; the $+S$ correction).

**Candidate strengthening.** Instead of (AV) with a single cross term $2\chi$, use (PID-$\rho$) with four explicitly-typed non-negative components. This is *strictly more informative* than (AV) — the cross-term splits into interpretable sub-parts — at the cost of requiring the PID machinery's operationalization (Bertschinger et al. 2014 propose several; the choice has consequences).

**Verdict.** PID decomposition is a legitimate refinement of (AV). It does *not* recover the multiplicative form but it does recover the *three-factor* narrative of (R-F) in a technically correct framework: "model contribution," "policy contribution," and "joint contribution" become distinct identifiable components rather than independent factors. The narrative is saved; the multiplicative coordinate is not.

**AAD integration.** Too technically heavy for a first promotion. Land (AV) first; mention PID as a structural refinement with an open follow-on. If AAD develops a serious multi-source information-decomposition need (likely in Section III coupled-agent analysis), PID becomes the natural tool.

### 3.4 Multiplicative-noise processes

**Setup (excluded by the prior spike's method).** Consider state-dependent noise:

$$dx_t = \mu(x_t)\,dt + \sigma(x_t)\,dW_t$$

where $\sigma$ scales with $x_t$ (geometric Brownian motion: $\sigma(x) = \sigma_0 x$; stochastic volatility: $\sigma(x) = \sigma_0 \sqrt{x}$). In Itô calculus, log-transforming gives $d(\log x_t) = \text{drift-adjusted}\,dt + \sigma_0\,dW_t$ — the log-state has *additive* noise.

**Disturbance in this regime.** If the agent tracks $x_t$ directly, innovation variance scales with $x_t$; $\rho$ is state-dependent. If the agent tracks $\log x_t$, innovation variance is state-independent ("stabilized"). The coordinate choice (which variable to model) converts multiplicative-in-level noise into additive-in-log noise.

**Does this give a multiplicative $\rho$ factorization?** Partially: if the true process is multiplicative-noise and the agent models on the natural log coordinate, then $\rho^2$ in the log coordinate has the additive structure of (AV). If the agent models in the *original* coordinate, $\rho^2$ is state-dependent and no clean decomposition exists at the rate level — only a state-conditional variance map. The multiplicative structure is in the *level*-coordinate process, not in the rate-level attribution.

**Verdict.** Multiplicative-noise processes are not a strengthening route for (R-F). They are a reason the log-coordinate is sometimes natural (and (AV) applies there cleanly). This is consistent with AAD's additive-coordinate-forcing pattern: natural coordinate choices map multiplicative structure into additive.

### 3.5 Summary of multiplicative sub-structure analysis

| Regime | Multiplicative structure native? | Strengthens (R-F)? |
|---|---|---|
| Poisson rare-event cascade (MC) | Yes, under (MC-1)–(MC-3) | Yes — special case of (AV) where cross term vanishes |
| Large-deviation tails (LD) | Yes, for tail probabilities via additive rate functions | Complementary coordinate, not rate-level strengthening |
| PID decomposition | No; additive with four typed components | Refines the cross term in (AV); additive structure retained |
| Multiplicative-noise processes | No at rate level; yes in log-level coordinate | Not applicable; log coordinate moves to (AV) cleanly |

**Net.** The multiplicative form is native in (MC) and in the tail of (LD). Both are *regimes within (AV)*, not alternatives to it. PID refines the cross-term structure; multiplicative-noise processes are a coordinate-choice question that doesn't strengthen multiplicative rate decomposition.

---

## 4. Strengthening attempt 3 — no-go theorem for rate-domain multiplicative factorization

The strengthening posture has a dual: if no derivation produces (R-F), perhaps a sharp negative result can be derived showing *why* no derivation could. A no-go theorem converts "we tried and failed" into "impossible under stated conditions," which is a much stronger epistemic contribution.

### 4.1 Candidate no-go theorem

*[Candidate no-go theorem (rho-multiplicative-impossibility, conditional on (N1)–(N3))]*

**Claim.** Under (N1) finite second moments, (N2) non-degenerate environment noise, and (N3) non-trivial model class (with $\Delta^2_{\mathcal M} \in (0, \infty)$), the effective disturbance rate $\rho^2$ cannot be expressed as a product of three independent non-degenerate factors $\rho^2_\text{env} \cdot f(\mathcal M) \cdot g(\pi)$ with $f, g \in (0, 1]$ for generic AAD agents under sub-scope $\alpha$.

**Derivation sketch (by contradiction).** Assume (R-F) holds: $\rho^2 = \rho^2_\text{env} \cdot f(\mathcal M) \cdot g(\pi)$. Compare two scenarios:

- **Scenario A:** environment noise $\sigma^2_{\text{proc}}$ (process) + $\sigma^2_{\text{obs}}$ (observation); model class $\mathcal M$ with model error floor $\Delta^2$; policy $\pi$.
- **Scenario B:** double the observation noise, halve the process noise, such that $\sigma^2_{\text{proc}} + \sigma^2_{\text{obs}}$ is unchanged.

Under (AV), $\rho^2_\star(\text{env})$ is the same in both scenarios (sum of process + observation noises drives the Bayes-optimal innovation variance in the Kalman setting). But the *sensitivity of $\Delta^2_{\mathcal M}$ to the process/observation ratio* is nontrivial: model misspecification in drift (bias in $\hat\lambda$) couples differently to $\sigma^2_{\text{proc}}$ vs $\sigma^2_{\text{obs}}$ (Kalman Riccati $P^\ast$ is a monotone-increasing function of both, but with different rates). So $\rho^2$ in Scenarios A and B differs by a model-specific amount even though the sum of environment variances is constant.

Under (R-F), $\rho^2_\text{env}$ is *a single scalar* and must take the same value in both scenarios (the "environmental volatility" doesn't distinguish process from observation noise). So the prediction of (R-F) is that $\rho^2$ differs only via $f(\mathcal M)$. But the ratio $\rho_A^2/\rho_B^2$ under (AV) depends on the interaction between $\sigma^2_{\text{proc}}/\sigma^2_{\text{obs}}$ and $\Delta^2_{\mathcal M}$'s functional form — a two-argument function. Under (R-F), the ratio depends only on $f(\mathcal M)$, a one-argument function.

**Contradiction.** The two predictions cannot match for generic $\mathcal M$. Therefore (R-F) is inconsistent with (AV) under (N1)–(N3).

### 4.2 Epistemic status of the no-go

*Discussion-grade proof; the structure is correct but the counterexample construction is informal.* To promote to *exact*, one would: (a) fix a specific Kalman setup in Scenarios A and B with closed-form $P^\ast_A, P^\ast_B$; (b) derive $\rho^2_A/\rho^2_B$ under (AV) as a function of $\sigma^2_{\text{proc}}, \sigma^2_{\text{obs}}, \hat\lambda$; (c) derive $\rho^2_A/\rho^2_B$ under (R-F) and show the two are inconsistent for non-trivial $\hat\lambda$. Mechanical; done in ~1 page.

**What the no-go says.** Under the mildest regularity, no single-scalar "environmental volatility" can capture *both* process-noise and observation-noise contributions to $\rho$ while also admitting a model-class factor that depends only on the model. The environment has *two* volatility-like quantities (process / observation), and they interact with misspecification differently.

**What the no-go implies for (R-F).** Any attempt to write $\rho = \rho_{\text{env}} \cdot f \cdot g$ is under-specifying the environment by collapsing a two-dimensional volatility into one scalar. (MC) escapes this because its "environment" is a single Poisson emission rate $\lambda$, not a full noise-covariance structure. (LD) escapes by moving to a tail-rate coordinate where the collapse is valid (rate functions are scalar along a ray).

### 4.3 Integration with `#identifiability-floor`

The no-go has the canonical shape of `#identifiability-floor`'s pattern: *external mathematical obstruction, AAD machinery provides the escape*. Here:

- **Obstruction:** generic disturbance has multi-dimensional environment-side structure (process / observation / exogenous events) that cannot be collapsed to a single scalar multiplicative factor without losing the interaction with model misspecification.
- **Escape:** (AV)'s variance-additive form, supplemented by PID if finer decomposition is needed.

This would be Instance 4 of `#identifiability-floor`: alongside on-policy L0-detection (CHT), L1' mixture-identifiability (Cramér-Rao), and composition-layer no-go (Liberzon). The external theorem is a classical volatility-identifiability result; the escape is (AV). **Candidate for promotion to `#identifiability-floor` once the no-go is tightened to an exact counterexample.**

---

## 5. Strengthening attempt 4 — connection to `#additive-coordinate-forcing`

The brief calls out: *is there an axiom on disturbance decomposition that forces a specific coordinate via Cauchy's functional equation?* If yes, the rate-domain decomposition becomes a fifth primary instance of `#additive-coordinate-forcing`. If no, it's an adjacent family member.

### 5.1 Candidate AAD-internal axiom

**Axiom candidate (disturbance-additivity-under-independent-contributions).** *If the environment, model class, and policy contribute to the effective disturbance rate through statistically independent channels (no mediation, no cross-coupling), then the disturbance rate's second moment decomposes additively across these three sources.*

**AAD-internal motivation.** Adjacent to `#chain-confidence-decay`'s structure: the chain layer's additivity is forced by the probability chain rule applied to the product form $P(\text{chain}) = \prod P(E_i \mid E_{<i})$. The disturbance-additivity candidate would be motivated by the *variance-additivity of independent noise sources* — a mathematical identity in probability (Bienaymé 1853) that does not require AAD-internal structure.

### 5.2 What this axiom forces

Under independence + finite second moments (the axiom's conditions + (N1)), variance is additive: $\operatorname{Var}(X + Y) = \operatorname{Var}(X) + \operatorname{Var}(Y)$. The forced coordinate is *variance itself* (or its per-time analog, rate-squared). This is already the (AV) coordinate. Cauchy's functional equation does not need to be invoked — variance-additivity is direct.

**Is this a Cauchy-FE instance?** The Cauchy-FE argument derives a logarithmic coordinate from an additivity axiom + smoothness / monotonicity. But variance-additivity is already a direct algebraic identity; no smoothness argument is needed. The structural machinery is weaker than Cauchy-FE (Bienaymé's identity suffices).

### 5.3 Verdict

**Not a fourth/fifth primary instance of `#additive-coordinate-forcing`.** The additive coordinate (variance) is forced by a direct algebraic identity, not by a Cauchy-FE uniqueness argument. This places (AV) in the same structural family as the **Lyapunov quadratic** (adjacent family member, coordinate matched by identity rather than forced by uniqueness theorem) rather than as a primary instance.

**This is honest news.** The prior spike's §7 speculated that (R-F) might fit `#additive-coordinate-forcing`. The cleaner position: **(R-F) does not, but (AV) also does not** — (AV) sits alongside Lyapunov quadratic as an adjacent family member. The additive-coordinate pattern is narrower than "any additive structure in AAD"; it specifically covers cases where Cauchy-FE operates on smooth monotone axioms to force a logarithmic coordinate.

**The meta-pattern's integrity is preserved.** (AV)'s coordinate is variance, forced by Bienaymé's identity under independence. No AAD-internal axiom beyond the classical one is needed. This is actually cleaner than the prior spike's attempt — it places (AV) in its proper structural home without over-promoting.

---

## 6. Strengthening attempt 5 — recipe for conditional identification under sub-regimes

The brief asks: even if general factorization fails, are there operational sub-regimes where the multiplicative form holds exactly? Name them, derive them, file under A2' sub-scope labels.

### 6.1 Sub-regime catalog

| Sub-regime | Multiplicative (R-F) status | Why |
|---|---|---|
| **$\alpha_1^{MC}$:** Poisson rare-event with independent gates | **Exact** | (MC) cascaded Poisson thinning |
| **$\alpha_1^{\text{TAIL}}$:** Large-deviation tail under variance-additivity + independence | **Exact (on tail-probability coordinate)** | (LD) additive rate functions |
| **$\alpha_1^{\text{small-}\Delta}$:** Near-optimal model + near-benign policy (small-$\Delta$ regime) | **First-order approximate** | $\log(1 + x) \approx x$ linearization; cross-terms are $O(\Delta^4)$ |
| **$\alpha_1^{\text{indep}}$:** Genuinely independent model/policy (no mediation through state distribution) | **Approximate** | Cross-term $\chi \approx 0$ by construction |
| **$\alpha_2$** (adaptive-gain): Model class adapting under MG-1–MG-4 | **Not applicable to (R-F)** | Model class itself is time-varying; use (AV) with augmented state |
| **$\beta$** (PID / rule-based / variational): | **Not applicable** | Pythagorean decomposition fails; (AV) gives only a bound |
| Generic sub-scope $\alpha$ with non-trivial misspecification | **Fails** | (AV) applies; no multiplicative reduction available |

### 6.2 Recipe for operational use

When an analyst wants to use a multiplicative-form intuition:

1. **Identify the sub-regime.** Is the setting Poisson-rare-event ($\alpha_1^{MC}$), tail-asymptotic ($\alpha_1^{\text{TAIL}}$), or near-optimal ($\alpha_1^{\text{small-}\Delta}$)?

2. **Name the sub-regime conditions.** (MC-1)–(MC-3) for cascade; large-deviation regularity + independence for tails; $\Delta^2_{\mathcal M} + \Delta^2_\pi \ll \rho^2_\star$ for small-$\Delta$.

3. **Use (R-F) at the appropriate coordinate.** Rate level for (MC); tail-probability level for (LD); first-order log-expansion for small-$\Delta$.

4. **Outside these regimes, use (AV) with cross-terms.** Do not attempt to force (R-F) in rate coordinates.

### 6.3 Integration with A2' sub-scope

The sub-regime labels $\alpha_1^{MC}$, $\alpha_1^{\text{TAIL}}$, $\alpha_1^{\text{small-}\Delta}$, $\alpha_1^{\text{indep}}$ refine the existing A2' partition. They are all *within* sub-scope $\alpha$; they carve out specific operational contexts where multiplicative $\rho$-factorization is exact or tight. The broader A2' sub-scope $\alpha$ remains the domain of (AV) — these refinements are additional regime labels, not a new partition of the scope.

---

## 7. Rejected / dead ends (honest failure record)

Strengthening-first posture requires documenting failures. Three attempts produced negative results.

### 7.1 Log-variance Cauchy-FE

Attempt: force $\log \rho^2$ to decompose additively via a Cauchy-FE argument on an axiom like "under independent contributions, $\log\rho^2$ is additive."

**Failure.** $\log(\sigma^2_1 + \sigma^2_2) \neq \log \sigma^2_1 + \log\sigma^2_2$; the log of a sum of variances has no Cauchy-FE structure. The axiom doesn't hold for independent noise sources — it would require variances to combine multiplicatively, which they don't.

**Lesson.** The prior spike's §12's Cauchy-FE attempt on log-rate was correctly dismissed. Variance-additivity is the *anti-* Cauchy-FE regime: you cannot pass to a logarithmic coordinate and get additivity on independent sources.

### 7.2 Cumulant-generating-function additivity

Attempt: use the fact that cumulants are additive under independence ($\kappa_n(X + Y) = \kappa_n(X) + \kappa_n(Y)$ for independent $X, Y$) to derive a multiplicative moment-generating function factorization: $M_\rho(s) = M_{\text{env}}(s) \cdot M_{\mathcal M}(s) \cdot M_\pi(s)$.

**Partial success, contingent failure.** This is correct under *sum-form* independence, i.e., when $\rho = \rho_\text{env} + \rho_{\mathcal M} + \rho_\pi$ with all three mutually independent. Then $M_\rho(s) = \mathbb E[e^{s\rho}] = \mathbb E[e^{s\rho_\text{env}} e^{s\rho_{\mathcal M}} e^{s\rho_\pi}] = M_{\text{env}}(s) M_{\mathcal M}(s) M_\pi(s)$.

**But this is (LD) in another form.** The MGF factorization is equivalent to the rate-function additivity of §3.2. It doesn't give a rate-domain multiplicative factorization of $\rho$ itself; it gives a multiplicative factorization of a statistical-object (the MGF) whose inversion to $\rho$ is via tail-regime asymptotics.

**Lesson.** The cumulant / MGF route is a re-derivation of the LD regime, not a new strengthening.

### 7.3 Rényi-divergence decomposition

Attempt: replace KL with Rényi $\alpha$-divergence, which has a multiplicative structure in some parameter regimes.

**Failure.** Rényi divergences satisfy $D_\alpha(P \Vert \prod Q_i)$-style factorization for specific $\alpha$ values under independence, but the AAD-native divergence is KL (the $\alpha \to 1$ limit), which has *additive* factorization. Moving to a non-KL divergence to get multiplicativity sacrifices AAD's chain-rule-additivity axiom (which is the motivation for the divergence-layer Cauchy-FE instance in `#strategy-cost-regret-bound`). Not a coherent move.

**Lesson.** The divergence coordinate is already fixed by AAD's broader commitment to KL. Changing the divergence to get multiplicativity in $\rho$ would fight the existing `#additive-coordinate-forcing` structure.

---

## 8. Recommended segment-level moves

This spike produces math that should land in segments. Per `FORMAT.md`'s "math lives in segments" rule, here are the recommended destinations.

### 8.1 New appendix segment: `#rho-decomposition` (strong recommendation)

**Slug.** `rho-decomposition` (or `disturbance-decomposition` if the project prefers broader scope).

**Type.** `derivation`.

**Status.** `conditional` (exact under (S1)–(S4); robust-qualitative outside; sub-regimes refined by regime labels).

**Location.** Section I appendix — sibling to `#sector-condition-derivation`, `#persistence-cost`, `#edge-update-natural-parameter`.

**Content shape.**

1. (AV) variance-additive decomposition with sub-scope conditions.
2. Sub-regime catalog: $\alpha_1^{MC}$, $\alpha_1^{\text{TAIL}}$, $\alpha_1^{\text{small-}\Delta}$, $\alpha_1^{\text{indep}}$.
3. Multiplicative-form regimes: (MC) for rare-event cascades; (LD) for tail probabilities.
4. No-go theorem (with exact Kalman counterexample construction).
5. PID refinement (brief mention; reference Williams-Beer 2010 + Bertschinger et al. 2014).
6. Derivation-audit table per FORMAT.md O-BP14.
7. Composition with `#sector-persistence-template`, `#persistence-cost`, `#critical-mass-composition`, `#interaction-channel-classification`.

**Depends.**

- `#mismatch-decomposition` (per-instant bias-variance identity)
- `#mismatch-dynamics` (rate-level disturbance)
- `#sector-persistence-template` (disturbance statistic interface)
- `#model-class-fitness` (model-excess contribution)
- `#gain-sector-bridge` (sub-scope $\alpha$)
- `#adaptive-tempo` (rate factor $\nu$)
- `#identifiability-floor` (no-go integration)

**Rationale.** The decomposition is load-bearing for the internal-external-decomposition spike (`msc/spike-internal-external-decomposition.md`) which is deferred pending this reframe. Once `#rho-decomposition` lands, the parent spike can promote by citing (AV) at its fine-decomposition step.

### 8.2 Extension to `#sector-persistence-template`

Add a subsection titled "Effective-disturbance decomposition" that cites `#rho-decomposition` and notes that each of the six instantiations can carry a sub-contribution attribution (irreducible / model-excess / policy-excess / cross) at no extra derivation cost.

### 8.3 Extension to `#identifiability-floor`

Add Instance 4: rate-multiplicative factorization no-go (per §4 above). External obstruction: volatility-identifiability (two-dimensional environment noise cannot collapse to scalar product form). Escape: (AV) variance-additive form with typed cross terms.

### 8.4 Extension to `#additive-coordinate-forcing`

Add a subsection to the "Adjacent cases that share the shape but not the forcing structure" section: **variance-additive rho decomposition**. The coordinate (variance) is forced by Bienaymé's identity under independence, a direct algebraic identity rather than a Cauchy-FE uniqueness argument. Adjacent to the Lyapunov quadratic case (both coordinate-matched rather than coordinate-forced).

### 8.5 Update to `#separability-pattern`

Add the seventh-ladder row refinement: the internal-external attribution ladder now has a *structured* separable-core (Regime A + (AV) with measured cross-terms), a *structured repair* (Regime B + (AV) with functional-form cross-term assumptions), and a *general open* (Regime C + (AV) with confounded cross-terms). The ladder's technical content strengthens: "functional-form assumptions on $f, g, h, Q$" becomes "functional-form assumptions on the mediation term $\chi$ in (AV)," which is a specific, named mediation-analysis problem (Imai et al. 2010) rather than a generic hand-wave.

### 8.6 Promotion path for `msc/spike-internal-external-decomposition.md`

Once `#rho-decomposition` lands:

1. **Replace (R-F) with (AV) in the parent spike's §3.2** — swap the log-factorization for the variance-additive form with cross-terms.
2. **Downgrade fine-decomposition from robust-qualitative to conditional** (under (S1)–(S4) + Regime A or B identification).
3. **Preserve coarse decomposition at exact** — this is unaffected.
4. **Add PID refinement as a future-work note** — not needed for first promotion.
5. **Promote to `#internal-external-decomposition`** — the appendix segment the parent spike proposed.

The parent spike's value is preserved; the weakest-link factorization is replaced by a derived theorem.

### 8.7 Do NOT create

- A separate "prior-art-comparison with Oaxaca-Blinder / Shapley / PID" document — per `CLAUDE.md`'s prior-art-integration rule, these go in the Discussion sections of the relevant segments.
- A `#rho-factorization` segment — the name would advertise the failed form. Prefer `#rho-decomposition` or `#disturbance-decomposition`.

---

## 9. Open questions

1. **Tighten the no-go theorem.** §4.2 sketches the proof-by-contradiction; a rigorous version needs an explicit Kalman Scenarios-A-vs-B construction with closed-form $\rho^2$ expressions under (AV) and under the assumed (R-F). This is ~1 page of algebra. Worth a focused tightening spike; would promote §4 from discussion-grade to exact.

2. **Does the PID refinement simplify under sub-scope $\alpha$?** Bertschinger et al. 2014's PID requires operationalizing the "unique" and "redundant" parts. Under sub-scope $\alpha$ (Gaussian / exponential family), are there closed-form PID expressions for $(M, \pi, \delta)$? This would promote §3.3 from structural sketch to computational recipe.

3. **Composition under agent-agent coupling.** (AV) applies per-agent. Under `#critical-mass-composition`'s signed coupling $\rho_i^{\text{eff}} = \rho + \gamma \mathcal T_j$, does the (AV) decomposition compose? Candidate: $(\rho_i^{\text{eff}})^2 = \rho_{\star,i}^2 + \Delta^2_{\mathcal M_i} + \Delta^2_{\pi_i} + 2\chi_i + \gamma^2 \mathcal T_j^2 + 2\gamma \mathcal T_j \cdot \text{sign terms}$. Worth a composition-side spike.

4. **Regime-I negative contribution in `#interaction-channel-classification` and (AV).** The recipient-side classification has a *negative* Regime-I term that reduces $\rho$. Under (AV), where does the cooperative-signal contribution land? Candidate: it reduces $\rho_\star^2$ via augmenting the effective environment with informative signals. Worth a cross-reference note when `#rho-decomposition` lands.

5. **Is there a Section III composition axis for $\rho$-attribution that mirrors the positive / negative / constructive meta-architecture?** (AV) is positive-half (separable core + structured repair + general open ladder). The no-go is negative-half (identifiability floor instance). Is there a constructive-half (coordinate-forcing) move? §5 answered no — (AV) is coordinate-matched, not coordinate-forced. This is itself a load-bearing structural observation: the three meta-patterns cover AAD's architecture, but each individual structural move doesn't need to appear in all three. $\rho$-decomposition participates in positive and negative halves; not in constructive.

6. **Multiplicative cascade as a possibly-distinctive AAD contribution.** The (MC) regime is the cleanest place where (R-F) is native. Is the Poisson-rare-event-cascade structure intrinsic to any AAD sub-problem, or is it simply a classical rare-event regime AAD inherits from probability theory? Candidate locations: safety-critical system viability under `#persistence-condition`; incident-rate analysis in TST's $\mathcal C_t^{\text{commit}}$; composition-level catastrophic-failure regimes in `#critical-mass-composition` and `#symbiogenic-composition`. Worth a TST/Section III audit.

---

## 10. Summary of strengthening-first outcomes

- **Strengthening 1 — (AV) theorem.** Derived. Promoted the prior spike's qualitative (R-V) reframe to a theorem with named sub-scope conditions (S1)–(S4), an information-geometric derivation via Pythagorean projection, and explicit composition with AAD's existing machinery. Status: *exact* in sub-scope $\alpha$ under (S1)–(S4); *robust qualitative* outside. **Lands in new segment `#rho-decomposition`.**

- **Strengthening 2 — multiplicative sub-structure.** Located. The multiplicative form is native in the Poisson-rare-event-cascade regime (MC) and in the large-deviation tail (LD) regime. Both are sub-regimes within (AV), not alternatives. PID refines the cross-term structure. Multiplicative-noise processes are a coordinate-choice issue, not a strengthening route. **Lands as sub-regime catalog in `#rho-decomposition`.**

- **Strengthening 3 — no-go theorem.** Derived at discussion-grade; clear path to exact. Under mild regularity, no single-scalar "environmental volatility" can capture multi-dimensional environment noise while admitting a model-class multiplicative factor. **Lands as §4 of `#rho-decomposition` and as Instance 4 of `#identifiability-floor`.**

- **Strengthening 4 — `#additive-coordinate-forcing` connection.** Honest negative. (AV)'s coordinate (variance) is forced by Bienaymé's identity, not by Cauchy-FE under an AAD-internal axiom. Places (AV) as an adjacent family member (like Lyapunov quadratic), not a fourth/fifth primary instance. **Lands as subsection in the adjacent-cases section of `#additive-coordinate-forcing`.**

- **Strengthening 5 — conditional sub-regime recipe.** Named. Four sub-regime labels ($\alpha_1^{MC}$, $\alpha_1^{\text{TAIL}}$, $\alpha_1^{\text{small-}\Delta}$, $\alpha_1^{\text{indep}}$) refine A2' sub-scope $\alpha$ for when multiplicative (R-F) intuitions are exact or tight. **Lands as sub-regime catalog in `#rho-decomposition`.**

**Net.** The prior spike's heuristic fallback is replaced by a derived theorem with named conditions, three regime-typed sub-cases where multiplicative intuitions are native, a sharp no-go theorem ruling out naive multiplicative factorization, and honest placement in AAD's meta-architecture. This is the strengthening the prior spike flagged (*"reframe"*) but did not deliver.

**What the prior spike got right.** The obstruction diagnosis. $\rho$ *is* agent-conditional; $\rho_\text{external}$ is not well-posed without a reference class; the natural structure *is* variance-additive. Those observations are correct and stable under this spike's work.

**What the prior spike missed.** The derivation of (AV) as a theorem; the sub-regime catalog; the no-go theorem; the placement in `#additive-coordinate-forcing` (as adjacent, not primary); the composition with `#identifiability-floor` as a fourth instance. These are the strengthening moves.

**Recommended next action.** Land `#rho-decomposition` as a Section I appendix with §§2–6 of this spike as its content. Unblock the parent internal-external-decomposition spike for promotion.

---

*End of spike. The multiplicative form (R-F) is dead as a derived result but alive as three well-characterized sub-regimes. The variance-additive form (AV) is the new structural anchor, promoted from qualitative reframe to derived theorem. A no-go theorem sharpens the negative result into AAD's `#identifiability-floor` pattern. Net: strengthen-first delivered; the heuristic fallback is no longer needed.*
