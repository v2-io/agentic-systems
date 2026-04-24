---
slug: bias-bound-derivation
type: derivation
status: conditional
depends:
  - scope-agent-identity
  - discussion-additive-coordinate-forcing
  - directed-separation
  - information-bottleneck
  - compression-operations
stage: draft
---

# Derivation: Bias-Bound Constant $C$ for Class-2 Agent Observation-Ambiguity Modulation

The observation-ambiguity bias bound carried by Class-2 (fully-coupled) agents in the logogenic-agents scope — $\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa_{\text{processing}} \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$ ([#observation-ambiguity-modulation](../../03-logogenic-agents/src/observation-ambiguity-modulation.md), [#section-ii-survival](../../03-logogenic-agents/src/section-ii-survival.md)) — previously treated the constant $C$ as "domain-dependent" and the bound as "order-of-magnitude guidance, not a theorem." This appendix derives $C$ under two named sub-scopes, records a no-go showing that $C$ cannot be universal without the (PI) parameterization-invariance axiom of [#scope-agent-identity](agent-identity.md), and documents two failed derivation routes so future agents do not repeat them.

## Formal Expression

### §1 — Setup and the audit before strengthening

Let $M_{\tau^-} \in \mathcal M$ be the pre-update epistemic substate. Let $e_\tau$ be the event triggering update, $G_t$ the goal substate, and $\Omega_\tau$ the latent world-state. In Class-1 (modular) scope, [#directed-separation](directed-separation.md) guarantees the update $f_M(M_{\tau^-}, e_\tau)$ is goal-blind: $M_{\tau^+}^{\text{decoupled}} = f_M(M_{\tau^-}, e_\tau)$. In Class-2 (coupled) scope, the coupled update $f_X^M(X_{\tau^-}, e_\tau)$ carries goal-conditional reweighting; the bias is

$$\Delta M_{\text{bias}} := f_X^M(X_{\tau^-}, e_\tau) - f_M(M_{\tau^-}, e_\tau)$$

**Pre-strengthening type audit.** For the bound "$\lVert \Delta M_{\text{bias}}\rVert \leq C \cdot \kappa \cdot I$" to be well-typed:

1. **Norm on $\mathcal M$.** The LHS is a norm on model-space. $\mathcal M$ is the model space of [#agent-model](agent-model.md). Three candidate norms: Euclidean on parameters, total variation on induced measures, Fisher-Rao geodesic distance. **Under the (PI) parameterization-invariance axiom in [#scope-agent-identity](agent-identity.md)** (fourth primary instance of [#discussion-additive-coordinate-forcing](additive-coordinate-forcing.md)), Euclidean-on-parameters is a coordinate artifact and Fisher-Rao is the canonical AAD-invariant choice on statistical-manifold sub-cases of $\mathcal M$ (Čencov 1982 uniqueness).

2. **Regularity of $f_X^M$.** For the bound to be a theorem, $f_X^M$ must satisfy some regularity. The Bayesian-posterior model (prior + likelihood reweighting) is the canonical working class; it covers the attention-reweighting mechanism typical of Class-2 architectures to leading order.

3. **Information coordinate.** $I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$ is in nats (or bits). Converting information to state-distance is exactly what the Pinsker / Bretagnolle-Huber / Otto-Villani / Bakry-Émery machinery does.

The bound is well-typed under (a) named norm, (b) bounded $f_X^M$ regularity, (c) specified information-geometric inequality. Without (PI) adopted, $C$ is norm-dependent; under (PI), Fisher-Rao is canonical and $C$ becomes derivable.

### §2 — Track 1: Transport-inequality derivation under log-Sobolev + Lipschitz-posterior

*[Derived (w2-transport-track, conditional on H1-H3)]*

**Named sub-scope (H1-H3).**

- **(H1) Statistical-manifold sub-case.** Each $M_t \in \mathcal M$ corresponds to a probability distribution $P_{M_t}$ over world-states. $\mathcal M$ is (locally) a statistical manifold.
- **(H2) Log-Sobolev inequality.** The observation distribution $P_{\Omega \mid e, M}$ satisfies a log-Sobolev inequality (LSI) with constant $\rho_{\text{LSI}} \gt 0$. Sufficient condition: $P_{\Omega \mid e, M}$ is strongly log-concave with constant $K$ (Bakry-Émery 1985 curvature-dimension condition gives $\rho_{\text{LSI}} \geq K$). For Gaussian observation models, $\rho_{\text{LSI}} = 1/\sigma^2$ explicitly.
- **(H3) Lipschitz-posterior stability.** The Bayesian-posterior pushforward from observation to state is $L_{\text{post}}$-Lipschitz in $W_2$:

    $$W_2(P_{M \mid e, G}, P_{M \mid e}) \leq L_{\text{post}} \cdot W_2(P_{\Omega \mid e, G}, P_{\Omega \mid e})$$

    Sufficient condition: well-posed Bayesian inverse problem with bounded log-likelihood Hessian (Stuart 2010 *Inverse problems: a Bayesian perspective*, *Acta Numerica* 19:451–559, Theorem 4.6; Hairer, Stuart & Vollmer 2014 *SIAM J. Math. Anal.* 46(1):415–451 for explicit $W_2$-bounds in infinite-dimensional settings).

**Step 1 — KL from mutual information.** By the chain rule of relative entropy (Cover & Thomas 2006 Theorem 2.5.3):

$$\mathbb E_G\bigl[\mathrm{KL}\bigl(P_{\Omega \mid e, M, G} \,\Vert\, P_{\Omega \mid e, M}\bigr)\bigr] = I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$$

*Exact identity.*

**Step 2 — Otto-Villani under LSI.** From (H2) and Otto & Villani 2000 *J. Funct. Anal.* 173(2):361–400 Theorem 1:

$$W_2^2\bigl(P_{\Omega \mid e, M, G}, P_{\Omega \mid e, M}\bigr) \leq \tfrac{2}{\rho_{\text{LSI}}} \cdot \mathrm{KL}\bigl(P_{\Omega \mid e, M, G} \,\Vert\, P_{\Omega \mid e, M}\bigr)$$

Taking expectation over $G$ and substituting Step 1:

$$\mathbb E_G\bigl[W_2^2(P_{\Omega \mid e, M, G}, P_{\Omega \mid e, M})\bigr] \leq \tfrac{2}{\rho_{\text{LSI}}} \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$$

**Step 3 — Lipschitz-posterior pushforward.** From (H3):

$$\mathbb E_G\bigl[W_2^2(P_{M \mid e, G}, P_{M \mid e})\bigr] \leq L_{\text{post}}^2 \cdot \mathbb E_G\bigl[W_2^2(P_{\Omega \mid e, G}, P_{\Omega \mid e})\bigr]$$

**Step 4 — $\kappa_{\text{processing}}$ factor.** The $\kappa_{\text{processing}}$ coefficient from [#directed-separation](directed-separation.md)'s Class 1/2/3 taxonomy multiplies the goal-conditional reweighting strength by the modularity coefficient. For Class 2 fully-coupled, $\kappa_{\text{processing}} \approx 1$; for Class 3 partially-modular with modularity $\kappa$, the effective bound carries a factor $\kappa$ multiplicatively on the information term.

**Result (Track 1).** *[Derived, conditional on (H1)-(H3)]*

$$\boxed{\;\mathbb E\bigl[W_2^2(M_{\tau^+}^{\text{coupled}}, M_{\tau^+}^{\text{decoupled}})\bigr] \;\leq\; \frac{2 L_{\text{post}}^2}{\rho_{\text{LSI}}} \cdot \kappa_{\text{processing}} \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})\;}$$

**The constant is explicit:** $C_{W_2}^2 = 2 L_{\text{post}}^2 / \rho_{\text{LSI}}$, linear in $I$, with geometric interpretation:

- $L_{\text{post}}$ grows with *prior-likelihood tension* — ill-conditioned inverse problems amplify bias.
- $\rho_{\text{LSI}}$ grows with *observation-distribution concentration* — sharper observations yield tighter bounds.
- The ratio $2 L_{\text{post}}^2 / \rho_{\text{LSI}}$ captures the **geometric stiffness** of the update: small-$\rho$/large-$L$ = soft, goal-sensitive updates; large-$\rho$/small-$L$ = stiff updates that resist goal-bias.

### §3 — Track 2: Fisher-Rao derivation under (PI) + Čencov + small-information regime

*[Derived (fisher-rao-track, conditional on H1 + H4)]*

**Named sub-scope (H1 + H4).**

- **(H1) Statistical-manifold sub-case** — as in §2. Under the (PI) parameterization-invariance axiom of [#scope-agent-identity](agent-identity.md), Čencov's 1982 uniqueness theorem (*Statistical Decision Rules and Optimal Inference*, AMS) forces the Fisher information metric as the canonical Riemannian metric on $\mathcal M$ up to global scale (Ay, Jost, Lê & Schwachhöfer 2017 *Information Geometry*, Theorem 5.1).
- **(H4) Small-information regime.** $I(G; \Omega_\tau \mid e_\tau, M_{\tau^-}) \ll 1$ nat. The second-order Taylor expansion of KL at coincident distributions is sharp.

**Step 1 — KL-to-Fisher-squared-distance identity.** For nearby distributions $P$, $Q$ on a statistical manifold with Fisher metric $\mathbf I$, the KL divergence admits the second-order expansion

$$\mathrm{KL}(P \Vert Q) \;=\; \tfrac{1}{2} \cdot d_{FR}^2(P, Q) + O(d_{FR}^3)$$

where $d_{FR}$ is the Fisher-Rao geodesic distance (Cover & Thomas 2006 §12.5; Amari & Nagaoka 2000 §3.7 Theorem 3.1). This is the infinitesimal form of the Bregman divergence on the exponential family's dual geometry (cf. [#strategy-cost-regret-bound](strategy-cost-regret-bound.md) §6.3 for the related Fenchel-Bregman identification).

**Step 2 — Posterior-displacement in Fisher-Rao.** Under (H1)+(H4) + Bayesian-posterior-class $f_X^M$, the goal-conditional posterior and goal-marginalized posterior are nearby points on the statistical manifold; their Fisher-Rao distance satisfies

$$d_{FR}^2\bigl(M_{\tau^+}^{\text{coupled}}, M_{\tau^+}^{\text{decoupled}}\bigr) \;\leq\; 2 \cdot \mathrm{KL}\bigl(P_{M \mid e, G} \,\Vert\, P_{M \mid e}\bigr) + O(d_{FR}^3)$$

Using the data-processing inequality $\mathrm{KL}(P_{M \mid e, G} \Vert P_{M \mid e}) \leq \mathrm{KL}(P_{\Omega \mid e, G} \Vert P_{\Omega \mid e})$ (Bayesian posterior is a pushforward), and Step 1 of §2 ($\mathbb E_G[\mathrm{KL}(P_{\Omega \mid e, M, G} \Vert P_{\Omega \mid e, M})] = I$):

$$\mathbb E\bigl[d_{FR}^2(M_{\tau^+}^{\text{coupled}}, M_{\tau^+}^{\text{decoupled}})\bigr] \;\leq\; 2 \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-}) \cdot (1 + o(1))$$

**Step 3 — Taking square roots (with $\kappa$ factor).** Under Class-3 modularity, $\kappa_{\text{processing}}$ enters multiplicatively on the goal-conditional reweighting strength, hence on the KL and Fisher-Rao distance:

**Result (Track 2).** *[Derived, conditional on (H1)+(H4), small-information regime]*

$$\boxed{\;\mathbb E\,\lVert\Delta M_{\text{bias}}\rVert_{FR} \;\leq\; \sqrt{2} \cdot \sqrt{\kappa_{\text{processing}} \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})} \cdot (1 + o(1))\;}$$

**The constant is universal and dimension-free:** $C_{FR} = \sqrt{2}$ (nats) or $\sqrt{2 \ln 2}$ (bits). **No domain-specific parameters.** The (PI) commitment eliminates the coordinate-dependence that made $C$ ambiguous under Euclidean-parameter norms.

**Scaling difference between tracks.** Track 1 gives $W_2^2 \propto I$ (linear in information). Track 2 gives $d_{FR}^2 \propto I$, equivalently $d_{FR} \propto \sqrt I$ (square-root in information). The two tracks are not contradictory — they are bounds under different assumptions in different metrics. Track 1 is tight in the large-$I$ regime where Otto-Villani's linear form dominates; Track 2 is tight in the small-$I$ regime where the Fisher-metric second-order expansion is sharp. The two compose at intermediate scales by taking the tighter of the two under the local curvature conditions.

### §4 — No-go result: universal $C$ under Euclidean-parameter norm fails

*[Proved (no-universal-C-euclidean, counterexample-grade)]*

**Claim.** No universal constant $C$ — independent of $\mathcal M$'s geometry, parameterization, and coupled-update structure — exists such that $\lVert\Delta M_{\text{bias}}\rVert_{\text{Euclidean}} \leq C \cdot \kappa \cdot I$ under the Euclidean norm on an arbitrary parameter vector.

**Counterexample.** Let $\mathcal M = \{N(0, \sigma^2) : \sigma \gt 0\}$ parameterized by $\sigma$. The Fisher information in $\sigma$ scales as $\mathbf I(\sigma) = 2/\sigma^2$ — small near large $\sigma$, large near small $\sigma$. For any $C_0 \lt \infty$, choose $\sigma_0$ large enough that the Fisher-Rao displacement corresponding to $I(G; \Omega) = 1$ nat of goal-conditional reweighting translates to Euclidean-$\sigma$ displacement $\sigma_0 / \sqrt{2} \gt C_0$. Specifically, by Track 2's $\sqrt 2$ bound:

$$d_{FR}(M^{\text{coupled}}, M^{\text{decoupled}}) \leq \sqrt 2 \cdot 1 = \sqrt 2$$

Under the Fisher metric $\mathbf I(\sigma) = 2/\sigma^2$, the Fisher-Rao line element is $ds^2 = 2 d\sigma^2/\sigma^2$, so $\Delta\sigma \approx \sigma \cdot d_{FR}/\sqrt 2 = \sigma$ (Euclidean displacement scales linearly in $\sigma$). Taking $\sigma \to \infty$ gives arbitrarily large Euclidean-$\sigma$ displacement for fixed $I = 1$ nat. No universal $C$ in Euclidean-parameter norm exists.

**Implication.** The no-go strengthens the (PI) commitment rather than weakening the bound: **under (PI), Fisher-Rao is the canonical norm and $C = \sqrt 2$ is universal; without (PI), $C$ does not exist as a universal constant.** The (PI) axiom is *load-bearing* for this derivation, not coincidental.

**Position relative to [#discussion-identifiability-floor](identifiability-floor.md).** The no-go has the shape of a floor-pattern no-go (external obstruction: Euclidean-parameter norms carry unbounded Fisher condition numbers; escape: (PI) + Fisher-Rao gives universal $C$), but it does not match the five-element test for a floor instance (see [#discussion-identifiability-floor](identifiability-floor.md)): it has a *single* escape (the (PI) adoption), not ≥ 2 distinct escapes, and its strengthened consequence is *re-use* of existing (PI)+Čencov machinery (fourth primary instance of [#discussion-additive-coordinate-forcing](additive-coordinate-forcing.md)) rather than elevation of new machinery. The honest position: this no-go is a **downstream theorem of the (PI) commitment**, not a new floor instance. It belongs in this appendix as motivating justification for why (PI) is load-bearing for the derivation, not as a separate meta-segment entry. (Triage detail in `msc/spike-identifiability-floor-instance-triage-2026-04-24.md`.)

### §5 — Failed derivation routes (honest record)

Two derivation routes were attempted and failed at a structural level. Documented here so future agents do not re-attempt them without new evidence.

**(F1) Cramér-Rao inversion — wrong direction.** Attempt: treat $G$ as a parameter estimated from $\Omega$ given $(e, M)$; use the Cramér-Rao lower bound $\mathrm{Var}(\hat G) \geq \mathbf I_G^{-1}$ inverted to bound $\lVert\Delta M_{\text{bias}}\rVert \leq L_M \cdot \sqrt{\mathbf I_G^{-1}}$ via a posterior-sensitivity factor. Failure: Cramér-Rao bounds estimator error *below*, not above; the bound goes in the opposite direction to what the bias bound needs. Inverting Cramér-Rao for an upper bound on bias propagation requires a fixed-estimator-class assumption that is not available for a Class-2 agent's attention-reweighting mechanism. The transport-inequality route of §2 is the correct machinery.

**(F2) Rate-distortion inversion — wrong problem structure.** Attempt: apply Shannon's rate-distortion inequality $R(D) \geq h(X) - \tfrac{1}{2}\log(2\pi e D)$ (Gaussian source), invert to $D \leq \sigma^2 \cdot 2^{-2(R - h(X))}$ with "bits in" = $I(G; \Omega \mid e, M)$. Failure: rate-distortion theory describes the minimum bits-per-symbol required to represent a source within distortion $D$; it does **not** describe the maximum distortion induced by injecting side-information into an update. Source-coding theorems are about optimal representations of a source, not spatial displacement induced by side-information injection. The direction is again wrong. Transport inequalities (Attempt B) are the correct machinery.

The pattern shared across (F1) and (F2): **information-theoretic source-coding theorems (Cramér-Rao bounds, rate-distortion lower bounds) are structural lower-bound machinery for an estimator's or encoder's performance; they cannot be inverted to produce upper bounds on displacement induced by side-information.** Upper bounds on displacement require transport-inequality machinery (Pinsker, Otto-Villani, Bakry-Émery, posterior-stability).

### §6 — Gaussian worked example

*[Illustrative, exact under specified assumptions]*

**Setup.** Gaussian observation model $P_{\Omega \mid e, M} = N(\mu_M, \sigma^2 I)$ with fixed $\sigma^2$; conjugate-Gaussian prior $P_{M} = N(0, \tau^2 I)$; goal-conditional likelihood reweighting $P_{\Omega \mid e, M, G} = N(\mu_M + \beta(G), \sigma^2 I)$ where $\beta(G)$ is a goal-dependent shift with $\lVert\beta(G)\rVert^2$ bounded by the information budget $I(G; \Omega_\tau)$.

**LSI constant.** Gaussian $N(\mu, \sigma^2 I)$ satisfies LSI with $\rho_{\text{LSI}} = 1/\sigma^2$ (Bakry-Émery; direct Hessian bound on $-\log p$).

**Posterior-Lipschitz constant.** Conjugate-Gaussian posterior: $P_{M \mid \Omega} = N(\mu_{\text{post}}, \Sigma_{\text{post}})$ with $\mu_{\text{post}} = \tau^2/(\tau^2 + \sigma^2) \cdot \Omega$. Lipschitz-in-$\Omega$ constant $L_{\text{post}} = \tau^2/(\tau^2 + \sigma^2) \lt 1$. Under $W_2$-Lipschitz (Hairer-Stuart-Vollmer 2014), $L_{\text{post}} \leq 1$ for well-conditioned priors.

**Track 1 bound (numerical).** $C_{W_2}^2 = 2 L_{\text{post}}^2 / \rho_{\text{LSI}} = 2 \sigma^2 \cdot \tau^4/(\tau^2 + \sigma^2)^2$. In the prior-dominant limit ($\tau^2 \ll \sigma^2$): $C_{W_2}^2 \approx 2 \tau^4/\sigma^2$ (tight prior amplifies bias). In the likelihood-dominant limit ($\sigma^2 \ll \tau^2$): $C_{W_2}^2 \approx 2 \sigma^2$ (sharp observations limit bias).

**Track 2 bound (numerical).** Under (PI) + Fisher-Rao on the Gaussian mean-manifold with metric $\mathbf I(\mu) = I/\sigma^2$: $d_{FR}(\mu_1, \mu_2) = \lVert\mu_1 - \mu_2\rVert/\sigma$. Under small-$I$: $\mathbb E\,d_{FR}(\Delta M_{\text{bias}}) \leq \sqrt{2 \cdot \kappa \cdot I}$. In Euclidean-on-$\mu$ norm: $\lVert\Delta\mu_{\text{bias}}\rVert \leq \sigma \cdot \sqrt{2 \kappa I}$ — the $\sigma$ prefactor is the Fisher-Rao-to-Euclidean conversion. The Euclidean form is coordinate-dependent (per Attempt E §4); Fisher-Rao form is universal.

**Comparison at operating point.** For $\tau = \sigma = 1$ (balanced): Track 1 gives $C_{W_2}^2 = 2 \cdot (1/4) = 1/2$, so $\mathbb E\,W_2 \leq \sqrt{I/2}$. Track 2 gives $\mathbb E\,d_{FR} \leq \sqrt{2I}$. The two are within a factor of 2 of each other at balanced scale; they diverge in the ill-conditioned limits where Track 1's $L_{\text{post}}$ or $\rho_{\text{LSI}}$ blows up while Track 2 remains dimension-free.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Chain-rule identity $\mathbb E_G[\mathrm{KL}(P_{\Omega\mid G}\Vert P_\Omega)] = I(G;\Omega\mid \cdot)$ | Cover & Thomas 2006 Theorem 2.5.3 | Exact |
| Pinsker's inequality $\lVert P-Q\rVert_{TV} \leq \sqrt{\tfrac{1}{2}\mathrm{KL}}$ | Standard (Csiszár-Körner) | Exact |
| Otto-Villani $W_2^2 \leq (2/\rho_{\text{LSI}})\mathrm{KL}$ under LSI | Otto & Villani 2000 Theorem 1; Bakry-Émery 1985 curvature-dimension for LSI | Exact |
| KL-to-Fisher-squared-distance $\mathrm{KL}(P\Vert Q) = \tfrac{1}{2}d_{FR}^2 + O(d_{FR}^3)$ | Cover-Thomas 2006 §12.5; Amari-Nagaoka 2000 §3.7 Theorem 3.1 | Exact (standard information geometry) |
| Bayesian-posterior $W_2$-Lipschitz stability $L_{\text{post}}$ | Stuart 2010 Theorem 4.6 under well-posed inverse problem | Conditional on (H3) |
| **Track 1 bound** $\mathbb E[W_2^2(M^{\text{coupled}}, M^{\text{decoupled}})] \leq (2L_{\text{post}}^2/\rho_{\text{LSI}}) \cdot \kappa \cdot I$ | Composition of §2 Steps 1–4 | **Derived (conditional on H1-H3)** |
| **Track 2 bound** $\mathbb E\,\lVert\Delta M_{\text{bias}}\rVert_{FR} \leq \sqrt{2} \cdot \sqrt{\kappa I}(1+o(1))$ | Composition of §3 Steps 1–3 under (PI) + Čencov | **Derived (conditional on H1+H4, small-$I$ regime)** |
| $C_{FR} = \sqrt{2}$ is universal, dimension-free, no domain constants | §3 Result | Exact under (H1)+(H4) |
| $C_{W_2}^2 = 2L_{\text{post}}^2/\rho_{\text{LSI}}$ with explicit geometric interpretation | §2 Result | Exact under (H1)-(H3) |
| Attempt E no-go: no universal $C$ in Euclidean-parameter norm | Heteroscedastic-normal counterexample §4 | Proved (counterexample-grade) |
| (F1) Cramér-Rao inversion fails | Direction mismatch (estimator lower bound cannot invert to upper bound) | Recorded failure |
| (F2) Rate-distortion inversion fails | Problem-structure mismatch (source-coding theorem cannot yield side-information injection bound) | Recorded failure |
| Gaussian worked example with explicit $C_{W_2}$ and $C_{FR}$ | Conjugate-Gaussian direct computation | Exact under specified assumptions |

The dividing line: both tracks are derived theorems under named hypotheses; the hypotheses (LSI, Lipschitz-posterior, small-$I$, statistical-manifold sub-case, (PI) adoption) are either standard mathematical regularity (LSI, Lipschitz-posterior) or AAD-internal axioms ((PI), already adopted in [#scope-agent-identity](agent-identity.md) and elevated to fourth primary instance of [#discussion-additive-coordinate-forcing](additive-coordinate-forcing.md)). The no-go §4 justifies the (PI) commitment as load-bearing rather than coincidental. The failed attempts §5 document structural reasons two alternative routes cannot work, preventing future re-attempts.

## Epistemic Status

*Conditional — exact under H1-H3 (Track 1) or H1+H4 (Track 2).* Both tracks are derived theorems under named hypotheses:

- Track 1 is exact under the three regularity conditions (H1 statistical-manifold sub-case; H2 log-Sobolev on observation distribution; H3 Lipschitz-posterior stability). All three are standard mathematical regularity conditions satisfied for canonical cases (Gaussian observations: (H2) direct; well-posed Bayesian inverse problems: (H3) per Stuart 2010). The bound is linear in $I$, with explicit geometric-stiffness constants.

- Track 2 is exact under (H1) + (H4) small-information regime, leveraging (PI) + Čencov. The bound is $\sqrt I$ scaling with universal dimension-free constant $C_{FR} = \sqrt 2$. Does not depend on domain-specific $L_{\text{post}}$ or $\rho_{\text{LSI}}$; the price is the small-$I$ regime restriction.

The no-go §4 is *proved* via the heteroscedastic-normal family counterexample — universal $C$ in Euclidean-parameter norm does not exist; the (PI) commitment is load-bearing for the derivation. The failed attempts §5 are *recorded* at structural-reason level; they document why Cramér-Rao inversion and rate-distortion inversion cannot produce the needed upper bound, not merely that the attempts failed.

**Upgrade over prior formulation.** The bias bound in [#section-ii-survival](../../03-logogenic-agents/src/section-ii-survival.md) and [#observation-ambiguity-modulation](../../03-logogenic-agents/src/observation-ambiguity-modulation.md) previously carried the honest admission *"Without the constant, the bound is order-of-magnitude guidance, not a theorem."* This appendix **promotes the bound to theorem-level** under named sub-scopes. The order-of-magnitude admission is superseded by the two explicit tracks with their H-conditions. Updates to the logogenic-agents segments cross-reference this appendix.

Max attainable: *exact* for the composition of the three textbook inequalities (Step 1 chain-rule; Step 2 Otto-Villani; Step 3 Lipschitz-posterior or KL-to-Fisher-Rao identity) and for the no-go counterexample §4. *Conditional* overall — the theorem statements carry their H-conditions explicitly, and the sub-scope boundary is where "derived" transitions back to "admitted empirical regularity" (cases where H2 or H3 fails require separate treatment, flagged in Working Notes).

## Honest failure modes

The appendix does **not** cover:

1. **Non-statistical-manifold sub-cases of $\mathcal M$.** If $\mathcal M$ carries structured state-space geometry (mixed continuous/discrete components, graphical-model structure, non-parametric models without sufficient statistics), (H1) is weakened and Čencov's uniqueness does not straightforwardly apply. The Fisher-Rao track degrades; Track 1 may still apply under suitable alternative regularity.

2. **Unbounded KL / structural-failure limit.** If $P_{\Omega \mid e, M, G}$ has support disjoint from $P_{\Omega \mid e, M}$ at $G$-values carrying non-trivial prior probability, the KL (and thus $I$) diverges. The bound is vacuous in this regime. This is a structural failure of the coupled-update model, not a bound weakness.

3. **Non-Lipschitz pushforward.** If $f_X^M$ is not a well-posed Bayesian posterior (e.g., ill-posed inverse problem, degenerate likelihood, rank-deficient observation channel), (H3) fails and Track 1 does not apply. Track 2's small-$I$ expansion may still apply in the local-linearization sub-region.

4. **Large-information regime beyond the small-$I$ expansion.** Track 2's $\sqrt I$ scaling uses the second-order Fisher-metric expansion of KL; the full global relationship is lattice-dependent. A fully-global Fisher-Rao statement requires either compact-manifold assumption (Fisher-Rao distance bounded) or a staged-application argument (many small-$I$ steps composed).

5. **Heavy-tailed observation distributions.** LSI fails for heavy-tailed measures. Track 1 degrades to the Pinsker bound $W_2 \leq \sqrt{\mathrm{KL}/(2\rho_{\text{LSI}})}$ when $\rho_{\text{LSI}} \to 0$; this is the $O(\sqrt\varepsilon)$ baseline without the LSI tightening.

## Discussion

**Position in the [#discussion-additive-coordinate-forcing](additive-coordinate-forcing.md) meta-pattern.** Track 2's $C_{FR} = \sqrt 2$ result is a **downstream theorem of the fourth primary instance** (Čencov-invariance at the metric layer, under (PI)). Once (PI) adoption forces Fisher-Rao as the canonical metric on statistical-manifold sub-cases of $\mathcal M$, the KL-to-Fisher-squared-distance identity supplies the universal constant "for free" in the small-$I$ regime. The no-go §4 tightens the connection: the (PI) commitment is not just "useful axiom" but load-bearing for the bound's theorem-level status — without (PI), $C$ does not exist as a universal constant.

**Connection to [#variational-sector-condition](variational-sector-condition.md).** Both segments use Pinsker's inequality as a first step in propagating a KL bound. After Pinsker, the two segments diverge: this segment's cascade (Pinsker → Otto-Villani → Lipschitz-posterior → $W_2$ on pushforward) is a KL-to-state-distance machinery; `#variational-sector-condition`'s use (Pinsker + Cauchy-Schwarz → scalar sector-constant degradation) is a KL-to-scalar-constant machinery. The shared first step is Pinsker; the post-Pinsker cascade is not shared. Candidate shared-lemma extraction is flagged in `msc/spike-kl-to-state-distance-template-extraction-2026-04-24.md` (Option B, `#posterior-displacement-template`); `#variational-sector-condition` is positioned there as an adjacent family member (Pinsker shared; cascade not).

**Forward-looking clients.** Three open extensions in [#discussion-identifiability-floor](identifiability-floor.md) Working Notes are candidate future primary clients of this appendix's machinery: causal-IB (KL → W₂ on post-intervention pushforward), misspecification-cost (KL → W₂ on posterior under model misspecification), composition-scope-robustness (KL → W₂ on composite-state pushforward). Each would reuse the Track 1 Otto-Villani + Lipschitz-posterior cascade with client-specific $(P, Q, f)$ and $(L_{\text{post}}, \rho_{\text{LSI}})$ instantiations. If two or more of these materialize, factoring the cascade out as a template segment becomes attractive (see the extraction spike).

**Why the Fisher-Rao specialization is worth landing even under the small-$I$ restriction.** In the AAD-canonical operating regime, Class-2 bias is *moderate* — the goal-conditional reweighting shifts the posterior but does not replace it. Small-$I$ is the honest model of this regime; large-$I$ is the structural-failure limit where the coupled agent's goal-conditioning overwhelms evidence. Track 2's universal $C_{FR} = \sqrt 2$ is the right bound in the operating regime; Track 1 is the fallback under structural conditions where $I$ is not small or where Fisher-Rao is not available.

**Connection to logogenic agents.** This appendix's bounds are the quantitative apparatus underlying [#observation-ambiguity-modulation](../../03-logogenic-agents/src/observation-ambiguity-modulation.md)'s product-form bias bound and [#section-ii-survival](../../03-logogenic-agents/src/section-ii-survival.md)'s Class-2 scope-survival analysis. Both segments previously carried the "constant $C$ not computed" caveat; with this appendix landed, $C$ is computed under named conditions and the epistemic tier of the bias bound upgrades to "conditional (exact under H1-H3 or H1+H4)." The logogenic-agents segments retain their client status; the quantitative work moves here.

## Working Notes

- **Trail.** Full derivation history in `msc/spike-bias-bound-constant-C-strengthening-2026-04-24.md`. The spike's Track 1 and Track 2 structure maps directly to §§2–3 here; the no-go Attempt E maps to §4; the failed attempts (F1 Cramér-Rao, F2 rate-distortion) map to §5. The spike also flags the shared Pinsker / Otto-Villani machinery with `#variational-sector-condition` as a candidate shared-lemma extraction (`msc/spike-kl-to-state-distance-template-extraction-2026-04-24.md` Option B); that extraction is contingent on this appendix landing + forward-looking clients materializing.

- **$L_{\text{post}}$ for AAD-native cases.** The Lipschitz-posterior stability constant $L_{\text{post}}$ is cited from Stuart 2010 / Hairer-Stuart-Vollmer 2014 but not computed for all AAD-relevant cases. The conjugate-Gaussian case of §6 is explicit; general non-parametric Bayesian inverse problems have looser bounds. A future refinement could compute $L_{\text{post}}$ for the exponential-family / conjugate-prior cases in [#gain-sector-bridge](gain-sector-bridge.md) directly.

- **Large-$I$ Fisher-Rao refinement.** Track 2's $\sqrt I$ scaling is the small-$I$ Taylor expansion. Extending to large $I$ requires either compact-manifold assumption or staged composition; flagged for future work.

- **Interaction with the $\mathcal A$ factor from `#observation-ambiguity-modulation`.** The product form $\kappa_{\text{eff}} = \kappa \cdot \mathcal A$ interacts with the transport-inequality constants in ways not fully worked out here. If $\mathcal A$ is itself an information-theoretic ratio, the $\mathcal A$ factor may be absorbable into the $I$ term rather than appearing as a separate multiplicative factor. Flagged for a clarification pass when the logogenic-agents segments are next revised.

- **Non-Bayesian pushforwards.** The Track 1 (T3) posterior-Lipschitz step is stated for Bayesian-posterior pushforwards. Non-Bayesian pushforwards (e.g., post-intervention transformations in the causal-IB candidate) would use the general $W_2$-Lipschitz form; the machinery generalizes, though the concrete constants are client-specific.

- **Relation to active-inference bounds.** Active inference (Friston 2017 *Active inference: a process theory*, *Neural Computation* 29) uses KL bounds on posterior beliefs under the free-energy principle; those bounds are formulated in a different framework but share the underlying transport-inequality machinery. AAD's Track 1 derivation is consistent with the active-inference reading but does not require the variational-free-energy-as-master-objective commitment (see [#information-bottleneck](information-bottleneck.md) Discussion for the lineage distinction).
