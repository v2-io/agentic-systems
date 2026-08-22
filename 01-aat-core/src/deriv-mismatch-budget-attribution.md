---
slug: deriv-mismatch-budget-attribution
type: derivation
status: conditional
depends:
  - result-mismatch-decomposition
  - internal-external-decomposition
  - form-agent-model
  - def-model-class-fitness
  - result-persistence-condition
stage: draft
---

# Derivation: Mismatch-Budget Attribution — Policy as Measure, First-Order Log-Additivity, and the Information Form

The agent-side mismatch budget has no separate policy term. Each of the three terms of the exact mismatch decomposition ( #result-mismatch-decomposition) is the expectation of a policy-independent *kernel* — estimation error, state-uncertainty variance, channel variance, each a fixed function of the conditioning variables — taken under the **on-policy law** $\mathbb P_\pi$ of the agent-environment trajectory. The policy enters every term, the environmental floor included, only through that law. Three consequences follow directly. First, the "policy-benignity" that a multiplicative intuition treats as an independent attenuation factor $g(\pi)$ is a *reweighting* of where the estimation and state-uncertainty kernels are evaluated: a policy lowers the budget exactly when it concentrates the trajectory where the model class is adequate or the state is well-pinned, and cannot lower it at all when the kernels are state-independent (the linear-Gaussian / LQR case, where the innovation law is control-invariant). Model adequacy and policy are therefore entangled at the source — one kernel modulated by one measure — not two factors. Second, log-viability has an exact form in which the agent-movable excess enters as $-\tfrac12\log(1 + x)$ with $x$ the excess-to-floor ratio; this is log-additive in the estimation and state-uncertainty terms to first order in $x$, with a remainder bounded by $x^2/2$. That first-order regime is the precise and only sense in which the multiplicative picture was approximately right, and its "factors" are floor-relative exponentials of additive terms, each still policy-dependent through the measure. Third, the same three-way structure holds **exactly** in information units — expected log-loss of the model's predictive distribution splits into channel entropy, state-uncertainty information, and an estimation divergence, by the chain rule of log-loss alone, with no flatness or orthogonality condition — and the estimation divergence refines further into a class-ceiling gap plus a within-class gap exactly when the predictive class is an exponential family (sub-scope $\alpha$), by the generalized Pythagorean theorem.

## Formal Expression

### Setting and the two conditions

Fix a time $t$. Write $\mathcal C := \mathcal C_{t-1}$ for the chronica, $a := a_{t-1}$ for the action taken, $\Omega := \Omega_t$ for the environment state, and $o := o_t$ for the observation. The model's predictive mean is $\hat o = \mathbb E_q[o \mid M_{t-1}, a]$ with $M_{t-1} = m(\mathcal C)$ a fixed (possibly learned) map of the chronica ( #form-agent-model); the Bayes predictor is $\hat o^{\mathrm B} = \mathbb E[o \mid \mathcal C, a]$; the true conditional mean is $\bar o = \mathbb E[o \mid \Omega, a]$. Two conditions are in force throughout:

*[Assumption (GA-1, fresh noise — inherited from #result-mismatch-decomposition)]* — observation noise is conditionally independent of the chronica given $(\Omega, a)$, so $p(o \mid \Omega, a, \mathcal C) = p(o \mid \Omega, a)$.

*[Assumption (P, chronica-measurable policy)]* — the action depends on the environment only through the chronica: $a_s \sim \pi(\cdot \mid \mathcal C_s)$ (deterministic or randomized with internal randomness), and the environment's transition kernel $p(\Omega_{s+1} \mid \Omega_s, a_s)$ responds to *actions*, not to the policy object itself. This is AAT's standing agent-environment interface ( #def-action-transition). Adversarial coupling in the sense of #der-adversarial-destabilization — the attacker's action stream amplifying the target's disturbance — is *inside* (P) and is handled by Corollary 1c (measure reweighting). What (P) excludes is a kernel of the form $T(\cdot \mid \Omega, a, \pi)$: an environment that reads the policy object itself (source-code or Stackelberg access), which AAT has not canonized.

Write $\mathbb P_\pi$ for the joint law of $(\mathcal C, a, \Omega, o)$ induced by the environment and the policy $\pi$, and $\mathbb E_\pi$ for expectation under it.

### Proposition 1 — the policy is the measure

*[Derived (policy-as-measure), exact under GA-1 and (P)]*

Define the three kernels

$$e(\mathcal C, a) := \lVert \hat o(\mathcal C, a) - \hat o^{\mathrm B}(\mathcal C, a) \rVert^2, \qquad u(\mathcal C, a) := \operatorname{Var}(\bar o \mid \mathcal C, a), \qquad c(\Omega, a) := \operatorname{Var}(o \mid \Omega, a).$$

Then each kernel is a policy-independent function of its arguments, and the exact mismatch decomposition reads

$$\mathbb E_\pi \lVert \delta_t \rVert^2 = \mathbb E_\pi[e(\mathcal C, a)] + \mathbb E_\pi[u(\mathcal C, a)] + \mathbb E_\pi[c(\Omega, a)] =: E_\pi + U_\pi + C_\pi .$$

The policy enters the budget only through $\mathbb P_\pi$.

**Derivation.** The identity is #result-mismatch-decomposition, written with its three conditional quantities displayed as functions of the conditioning variables. What remains is that the kernels themselves do not depend on $\pi$. (i) $c(\Omega, a)$ is a conditional variance given $(\Omega, a)$; under GA-1 the conditional law $p(o \mid \Omega, a)$ is a property of the observation channel alone. (ii) Under (P), the joint law factorizes as $\mathbb P_\pi(\mathcal C, \Omega_{0:t}) = \big[\prod_{s \lt t} \pi(a_s \mid \mathcal C_s)\big] \cdot \big[\text{environment and channel factors}\big]$, and the policy factors are constant in $\Omega_{0:t}$ once $\mathcal C$ is fixed. They therefore cancel from the normalization of the posterior $p(\Omega \mid \mathcal C, a)$, which is policy-independent (the belief state is a function of the action-observation history, standard in partially observed control). Hence $\hat o^{\mathrm B}$ and $u$ — the mean and variance of $\bar o(\Omega, a)$ under that posterior — are policy-independent kernels. (iii) $\hat o$ is a fixed function of $(m(\mathcal C), a)$ by #form-agent-model, so $e$ is a policy-independent kernel. $\square$

**Corollary 1a (reweighting).** For two policies with $\mathbb P_{\pi'} \ll \mathbb P_\pi$ on the relevant coordinates, each term transforms by the likelihood ratio: $E_{\pi'} = \mathbb E_\pi\!\big[e \cdot \tfrac{d\mathbb P_{\pi'}}{d\mathbb P_\pi}\big]$, and likewise for $U$ and $C$. A change of policy is a change of measure on fixed integrands — not a projection, not an attenuation, and not a fourth term.

**Corollary 1b (invariance).** If the three kernels are $\mathbb P_\pi$-a.s. constant across the policies under comparison, the budget is policy-invariant. In the linear-Gaussian sub-scope with a well-specified filter this holds exactly: $e \equiv 0$, $u \equiv H P^{-} H^{\top}$ (the steady-state prior covariance, which solves a Riccati recursion independent of the control input), and $c \equiv R$ — the innovation law is invariant to the control gain (standard LQG: the prediction covariance recursion $A P A^{\top} + Q$ carries no control term; the LQR worked case is in the reasoning trail, `spikes/.integrated/spike-rho-factorization.md` §5). In the multiplicative vocabulary this is "$g(\pi) \equiv 1$"; in the present one it is simply that there is nothing state-dependent for the measure to reweight.

**Corollary 1c (entanglement and the movable floor).** A policy lowers $E_\pi$ exactly when $e(\mathcal C, a)$ is state-dependent and the policy concentrates $\mathbb P_\pi$ where $e$ is small — i.e., where the model class is adequate. A policy lowers $U_\pi$ exactly when it makes the interaction history more state-informative (the active-sensing door of #def-causal-information-yield). And a policy moves $C_\pi$ exactly when the channel variance depends on the action or state — as when the action selects the sensor ( #example-kalman, modes $L$ / $H$). "Irreducible" for the channel term therefore means *kernel-level*: no model touches $c(\Omega, a)$; its on-policy expectation $C_\pi$ is nonetheless policy-movable whenever the instrument or the visited states are. None of these is an independent factor: each is one kernel under one measure.

### Proposition 2 — exact log form and first-order log-additivity

*[Derived (first-order-log-additivity), exact given the rate-lift convention of #internal-external-decomposition]*

With $\rho^2 = \nu \, \mathbb E_\pi\lVert\delta_t\rVert^2$ and linear Model D ($R^\ast = \rho/\alpha$, #result-persistence-condition), log-viability is exactly

$$\mathcal V = \underbrace{\log \lVert \delta_{\text{critical}} \rVert + \log\alpha - \tfrac12 \log(\nu \, C_\pi)}_{\text{floor-relative viability}} \;-\; \tfrac12 \log(1 + x_\pi), \qquad x_\pi := \frac{E_\pi + U_\pi}{C_\pi} \;\ge\; 0,$$

provided $C_\pi \gt 0$. Since $x - \tfrac{x^2}{2} \le \log(1+x) \le x$ for $x \ge 0$ (the lower bound from $h(x) = \tfrac{x^2}{2} - x + \log(1+x)$, $h(0)=0$, $h'(x) = x^2/(1+x) \ge 0$),

$$\mathcal V = \Big[\log \lVert \delta_{\text{critical}} \rVert + \log\alpha - \tfrac12 \log(\nu \, C_\pi)\Big] - \frac{E_\pi}{2 C_\pi} - \frac{U_\pi}{2 C_\pi} + r(x_\pi), \qquad 0 \le r(x_\pi) \le \frac{x_\pi^2}{4}.$$

**Derivation.** $\log \rho^2 = \log\nu + \log(C_\pi(1 + x_\pi))$ by Proposition 1 and the definition of $x_\pi$; substitute into $\mathcal V = \log\lVert\delta_{\text{critical}}\rVert - \log\rho + \log\alpha$ and apply the elementary bounds. $\square$

**Reading.** The agent-movable contribution to viability is additive in the estimation and state-uncertainty terms *to first order in the excess-to-floor ratio*, with a remainder no larger than a quarter of the square of that ratio (the bound is the leading Taylor coefficient, so it is tight as $x_\pi \to 0$). Exponentiating, $\exp(-E_\pi / 2C_\pi)$ and $\exp(-U_\pi / 2C_\pi)$ are the only honest "attenuation factors": they attenuate the floor-relative viability, they are exponentials of additive variance terms rather than primitive multipliers, and both depend on the policy through $\mathbb P_\pi$ — there is no model-only factor and no policy-only factor at any order. Outside the small-$x_\pi$ regime the cross-dependence $\log(1 + x_\pi)$ is the whole story and no log-additive reading survives.

### Proposition 3 — the information form (exact)

*[Derived (log-loss-decomposition), exact under GA-1 and chronica-measurability of the model]*

Let $q_t(\cdot) := q(\cdot \mid M_{t-1}, a)$ be the model's full predictive distribution for $o_t$, $p_t^{\mathrm B}(\cdot) := p(\cdot \mid \mathcal C, a)$ the Bayes predictive distribution, and $p_t(\cdot) := p(\cdot \mid \Omega, a)$ the channel law, with $q_t \gg p_t^{\mathrm B}$ and all quantities finite. Then

$$\mathbb E_\pi\big[-\log q_t(o_t)\big] = \underbrace{H_\pi(o_t \mid \Omega_t, a_{t-1})}_{\text{(iii′) channel entropy}} + \underbrace{I_\pi(o_t ; \Omega_t \mid \mathcal C_{t-1}, a_{t-1})}_{\text{(ii′) state-uncertainty information}} + \underbrace{\mathbb E_\pi\, D\big(p_t^{\mathrm B} \,\Vert\, q_t\big)}_{\text{(i′) estimation divergence}} .$$

**Derivation.** Two tower-property steps. (a) Given $(\mathcal C, a)$, $o_t \sim p_t^{\mathrm B}$, so $\mathbb E_\pi[-\log q_t(o_t)] - \mathbb E_\pi[-\log p_t^{\mathrm B}(o_t)] = \mathbb E_\pi\,\mathbb E_{o \sim p_t^{\mathrm B}}\big[\log p_t^{\mathrm B}(o)/q_t(o)\big] = \mathbb E_\pi D(p_t^{\mathrm B} \Vert q_t)$. (b) Given $(\Omega, a, \mathcal C)$, $o_t \sim p_t$ by GA-1, so $\mathbb E_\pi[-\log p_t^{\mathrm B}(o_t)] - \mathbb E_\pi[-\log p_t(o_t)] = \mathbb E_\pi\,\mathbb E_{o \sim p_t}\big[\log p_t(o)/p_t^{\mathrm B}(o)\big] = I_\pi(o_t; \Omega_t \mid \mathcal C_{t-1}, a_{t-1})$, the conditional mutual information. (c) $\mathbb E_\pi[-\log p_t(o_t)] = H_\pi(o_t \mid \Omega_t, a_{t-1})$ by definition. Sum. $\square$

(i′) and (ii′) are non-negative (a divergence and a mutual information); (iii′) is a conditional entropy and, as a differential entropy on a continuous observation space, may be negative — the Gaussian specialization below makes this explicit. (i′) vanishes iff the model's predictive distribution coincides with the Bayes predictive $\mathbb P_\pi$-a.s.; (ii′) vanishes iff residual state uncertainty does not change the one-step predictive *distribution*. No orthogonality is invoked — the cross-terms of the squared form are replaced by the chain rule of log-loss, which is an identity. As in Proposition 1, the integrands are policy-independent kernels under (P) and the policy enters only as $\mathbb P_\pi$; the same three consequences (reweighting, invariance, entanglement) hold verbatim.

**Gaussian specialization (consistency with Propositions 1–2).** In the linear-Gaussian sub-scope with scalar observation, $p_t = \mathcal N(\bar o, c)$ and $p_t^{\mathrm B} = \mathcal N(\hat o^{\mathrm B}, u + c)$, so (iii′) $= \tfrac12\log(2\pi e\, c)$ and (ii′) $= \tfrac12 \log\!\big(1 + u/c\big)$ — the $\log(1 + x)$ structure of Proposition 2 appears pointwise. If the model is Gaussian with calibrated variance $\hat s^2 = u + c$, (i′) $= e / \big(2(u + c)\big)$; a miscalibrated $\hat s^2$ adds the standard penalty $\tfrac12\big[\log(\hat s^2/(u+c)) + (u+c)/\hat s^2 - 1\big] \ge 0$, a contribution the squared form cannot see.

### Proposition 4 — class-ceiling refinement of the estimation divergence (sub-scope $\alpha$)

*[Derived (class-ceiling-pythagorean), exact conditional on the predictive class being an exponential family with an attainable moment match]*

Fix $(\mathcal C, a)$ and suppose the model class's predictive family $\mathcal Q = \{q_\theta\}$ is an exponential family with sufficient statistic $T$ and log-partition $\psi$ (e-flat in the sense of Amari & Nagaoka 2000 §3.4). Let $q^\ast \in \mathcal Q$ be the m-projection of $p_t^{\mathrm B}$ onto $\mathcal Q$ — the member with $\mathbb E_{q^\ast}[T] = \mathbb E_{p_t^{\mathrm B}}[T]$, assumed to exist. Then for every $q_\theta \in \mathcal Q$,

$$D\big(p_t^{\mathrm B} \Vert q_\theta\big) = \underbrace{D\big(p_t^{\mathrm B} \Vert q^\ast\big)}_{\text{class ceiling}} + \underbrace{D\big(q^\ast \Vert q_\theta\big)}_{\text{within-class estimation}} .$$

**Derivation.** $\log\big(q^\ast / q_\theta\big) = (\theta^\ast - \theta)^{\top} T - \big(\psi(\theta^\ast) - \psi(\theta)\big)$ is affine in $T$, so its expectation under $p_t^{\mathrm B}$ equals its expectation under $q^\ast$ by the moment match; the former is $D(p_t^{\mathrm B} \Vert q_\theta) - D(p_t^{\mathrm B} \Vert q^\ast)$ and the latter is $D(q^\ast \Vert q_\theta)$. $\square$ (This is the generalized Pythagorean theorem of Csiszár 1975 and Amari & Nagaoka 2000 §3.4, specialized to an e-flat family; it is recorded here because the identification of the two legs with AAT's class ceiling and within-class learning is the content.)

Averaging under $\mathbb P_\pi$ gives $(\text{i}′) = \mathbb E_\pi D(p_t^{\mathrm B} \Vert q^\ast) + \mathbb E_\pi D(q^\ast \Vert q_t)$. The second leg is what parameter learning removes; the first is the one-step information-form counterpart of the ceiling that #def-model-class-fitness names and #result-structural-adaptation-necessity acts on — no estimate inside $\mathcal Q$ lowers it. The policy is again a measure on the pointwise projections, never a projection itself. Outside e-flat classes the identity acquires a residual $\mathbb E_{p_t^{\mathrm B}}\log(q^\ast/q_\theta) - D(q^\ast \Vert q_\theta)$ of either sign; that residual is the only place a genuine "cross term" lives in this attribution, and it is a class-geometry artifact, not a model–policy interaction.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Three terms are expectations of policy-independent kernels under $\mathbb P_\pi$ (Prop. 1) | #result-mismatch-decomposition + GA-1 + (P) | Proved |
| Policy change = measure change; invariance when kernels are state-independent; entanglement (Cor. 1a–1c) | Prop. 1 | Proved |
| Linear-Gaussian invariance of the innovation law under the control gain | Riccati covariance independent of input ( #example-kalman) | Proved (sub-scope) |
| Exact log form; first-order log-additivity with remainder $\le x^2/4$ (Prop. 2) | Prop. 1 + elementary bounds | Proved, conditional on the rate-lift convention and linear Model D |
| Information-form three-term identity (Prop. 3) | Chain rule of log-loss + GA-1 | Proved |
| Class-ceiling / within-class split (Prop. 4) | Csiszár–Amari–Nagaoka Pythagorean identity | Proved, conditional on e-flat predictive class with attainable moment match |
| Identification of the class-ceiling leg with #def-model-class-fitness | Interpretation (different horizons; ratio vs divergence) | Discussion-grade |
| Separate identifiability of $E_\pi$, $U_\pi$, $C_\pi$ from on-policy data | Not claimed here; obstructed per #disc-identifiability-floor Instance 4 | — |

## Epistemic Status

*Conditional.* Propositions 1 and 3 and the corollaries are *exact* under GA-1 and the chronica-measurable-policy condition (P) — both standing AAT interface assumptions, named so that the adversary-reads-the-policy case is visibly excluded. Proposition 2 is exact algebra plus an elementary inequality, conditional on the fluid-limit rate-lift convention and linear Model D that #internal-external-decomposition already states. Proposition 4 is exact within sub-scope $\alpha$ (exponential-family predictive class, m-projection attainable) and acquires a signed residual outside it. Max attainable: *exact* for Propositions 1–3 as stated; Proposition 4 cannot exceed *conditional* because the e-flat hypothesis is a genuine restriction on the model class, and the link to #def-model-class-fitness is interpretive. What is *not* claimed: that the three terms are separately identifiable from on-policy innovation data — they are not, and the obstruction is #der-architecture-noidentifiability projected onto the disturbance-statistic coordinate ( #disc-identifiability-floor Instance 4); this segment lands the *structure* of the attribution, the floor governs its *estimation*.

## Discussion

**Why the multiplicative picture felt right, and exactly where it was wrong.** A product $\rho_{\text{external}} \cdot f(\mathcal M) \cdot g(\pi)$ is an independent-attenuation chain. Proposition 2 shows the one regime in which such a chain is approximately visible — small excess relative to the floor — and shows that even there the "factors" are $\exp(-E_\pi/2C_\pi)$ and $\exp(-U_\pi/2C_\pi)$, exponentials of additive variance terms, each policy-dependent through the measure. The constitutive no-go of #internal-external-decomposition says the product cannot be exact; this segment says what the first-order approximation actually approximates, and that it approximates a split by *what moves the term* (modeling vs acting), not a split by *who owns the factor* (model vs policy). The reference-agent ambiguity that haunted "$\rho_{\text{external}}$" dissolves as well: the environmental floor is a kernel, $c(\Omega, a)$, agent-independent pointwise and policy-dependent only in expectation — a number once a policy is fixed, never a number on its own.

**Worked anchors.** *Well-specified Kalman, passive or LQR-controlled:* $e \equiv 0$, $u \equiv H P^{-} H^{\top}$, $c \equiv R$; the innovation variance $H P^- H^\top + R$ is control-invariant, so no policy choice moves the budget (Corollary 1b). *Misspecified drift with a regulating policy:* if the filter carries $\hat\lambda \ne \lambda$, its one-step prediction differs from the Bayes prediction by a quantity that scales with the state estimate, so to leading order $e(\mathcal C, a) \propto \hat x^2$ and $E_\pi \propto \mathbb E_\pi[x^2]$ — a stiffer LQR gain that holds the state near the origin lowers $E_\pi$ while leaving $u$ and $c$ untouched. That is Corollary 1c in the flesh: the policy does not attenuate the environment; it keeps the trajectory where the model's inadequacy bites least. *[Discussion-grade as an anchor — the leading-order scaling is stated, the constants are not derived here.]* *Strategy layer, Bernoulli edges:* the disturbance driving an edge credence is a per-visit innovation with variance fixed by the true success probability, summed over edges at the policy's visit rates; the policy's role is the visit measure over edges, and no model-class kernel appears at the per-observation level — the same shape as Proposition 1 one layer up ( #deriv-edge-credence-dynamics).

**Two coordinates, one structure.** The squared form (Propositions 1–2) is the Bregman decomposition on a squared-norm potential — the variance-additive adjacent case of #disc-additive-coordinate-forcing, *matched* to the sector-Lyapunov machinery rather than forced. The information form (Propositions 3–4) lives on the negative-entropy geometry — the same Legendre–Fenchel object the forced coordinates of that meta-segment inhabit — but it is *adopted* (log-loss is a proper scoring rule; the Pythagorean identity is Csiszár's), not forced by an AAT-internal additivity axiom: no axiom of the disturbance layer demands log-additivity, which is precisely why the multiplicative form was a choice and not a theorem. The two forms agree where they overlap (the Gaussian specialization), and the information form carries strictly more: it has no alignment qualifier — residual state uncertainty registers whenever it changes the predictive distribution, not only its mean — and it sees predictive-variance miscalibration.

**Interface with the identifiability floor.** Everything above is structural: it says what the budget *is* made of and how a policy moves it. An on-policy observer sees only the sum (the innovation law), and the three terms are separately identifiable only through Level-2 access — change the instrument to move $c$, change the actions to move $u$, change the model to move $e$ ( #der-loop-interventional-access; #disc-identifiability-floor Instance 4). The structural result and the floor are complementary, and neither weakens the other.

## Working Notes

- `#example-kalman` is consumed by Corollary 1c (sensor modes $L$/$H$) but deliberately absent from `depends:` — it sits in §B after the appendix, and listing it trips `bin/lint-outline`'s ordering check; the fact used (action selects the instrument, moving $c$) is elementary. Revisit at `deps-verified`.

- The class-ceiling leg of Proposition 4 and $\mathcal F(\mathcal M)$ of #def-model-class-fitness are defined over different objects (one-step divergence vs infinite-horizon information ratio); a derivation that relates them under a named horizon assumption would lift that row of the audit table from discussion-grade. Open.
- Under Model S the relation $R^\ast = \rho/\alpha$ changes homogeneity in $\alpha$ ( #deriv-sector-condition); the $\alpha$-coefficient of Proposition 2 would change, while the budget-side term $-\tfrac12\log(1 + x_\pi)$ enters through $\log\rho$ either way. Not worked here.
