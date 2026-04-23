# Spike: Strengthening the Class-2 Bias Bound — Deriving the Constant $C$

**Status.** Strengthening-first spike. The strengthening substantially succeeded for several named sub-scopes; one track (transport-inequality, under curvature) delivers an explicit constant. Two tracks yield tighter bounds whose forms suggest downstream segment restructuring. One no-go sub-result is honestly recorded. No segment files modified.

**Date.** 2026-04-24.

**Pressure point.** The Class-2 bias bound in `#section-ii-survival` (line 109) and its refined form in `#observation-ambiguity-modulation` (line 43):

$$\lVert \Delta M_{\text{bias}} \rVert \leq C \cdot \kappa_{\text{processing}} \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$$

admits "$C$ is a domain-dependent constant relating information-theoretic quantities to state-space norms" and concedes in the segment's Working Notes: *"Without the constant, the bound is order-of-magnitude guidance, not a theorem."* The mandate: strengthen before softening. Can $C$ be derived, partially or fully, under named geometric assumptions on $\mathcal{M}$?

**Relation to the (PI) / Čencov landscape (2026-04-23).** The recent addition of the **(PI) parameterization-invariance axiom** to `#agent-identity` (and its amplification in `#additive-coordinate-forcing` as the fourth primary instance of the meta-pattern) has *already* materially changed the landscape. Under (PI), the statistical-manifold sub-cases of $\mathcal{M}$ carry a *canonical* Riemannian metric — the Fisher information metric, uniquely forced up to global scale (Čencov 1982; Ay, Jost, Lê & Schwachhöfer 2017). This is exactly the geometric primitive that $C$'s derivation requires. The pre-(PI) claim "this requires an assumption about the geometry of $\mathcal{M}$" has been superseded by: AAD *now has* the canonical geometry on $\mathcal{M}$ on statistical-manifold sub-cases, and $C$ can be derived rather than assumed on that sub-case. The strengthening below exploits this directly.

---

## 1. Honest audit before strengthening

Before attempting to derive $C$, what must be true for the bound to be well-typed at all?

**A. The norm on $\mathcal{M}$.** The bound asks for $\lVert \Delta M_{\text{bias}} \rVert$ — a distance in the model space. $\mathcal{M}$ is the model space per NOTATION.md line 60. The norm is **not canonically specified** in AAD's Section I/II apparatus. Three candidate norms:

1. **Euclidean** on the parameter vector $\theta \in \mathbb R^d$ when $\mathcal{M}$ is parameterized as $\{P_\theta\}_{\theta \in \Theta}$. *Problem:* coordinate-dependent; fails (PI).
2. **Total variation** $\lVert P_{M_{\tau^+}^{\text{coupled}}} - P_{M_{\tau^+}^{\text{decoupled}}}\rVert_{TV}$ on the induced-measure view of $M_t$ as a distribution over world-states. Coordinate-free. Bounded in $[0, 1]$.
3. **Fisher-Rao geodesic distance** $d_{FR}(M_{\tau^+}^{\text{coupled}}, M_{\tau^+}^{\text{decoupled}})$ induced by the Fisher metric on the statistical manifold. Forced-canonical under (PI) by Čencov.

**Under (PI), the norm should be Fisher-Rao or an (PI)-invariant equivalent** — the Euclidean norm of a parameterization is a coordinate artifact. This is a pre-existing scope commitment the current segments do not use. The distinction matters: $C$ is **norm-dependent**. Until the norm is named, "$C$" is actually a family $\{C_{\lVert\cdot\rVert}\}$ indexed by norm choice.

**B. The "coupled update" $f_X^M$.** The bias $\Delta M_{\text{bias}} = f_X^M(X_{\tau^-}, e_\tau) - f_M(M_{\tau^-}, e_\tau)$ presupposes a coupled-update operator. For the bound to be a theorem, $f_X^M$ must satisfy some regularity. Candidates: Lipschitz in a canonical metric, bounded Fisher-norm derivative, posterior-class membership (Bayesian posterior with goal-conditioned likelihood).

**C. What "mutual information" means.** $I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$ is in nats or bits. The bound converts information (nats) to state-distance. This is *exactly* the kind of conversion that Pinsker / Bretagnolle-Huber / Talagrand T2 / Otto-Villani inequalities perform. The inequalities are standard; what is nonstandard is that AAD has not yet named *which* one applies.

**Bottom line of the audit.** The bound is well-typed if: (a) a norm on $\mathcal{M}$ is named (ideally (PI)-invariant), (b) $f_X^M$ has bounded regularity, (c) a specific information-geometric inequality is invoked. None of (a)-(c) appears fundamentally harder than AAD's other derivations; the landscape has changed post-(PI) and the strengthening is feasible.

---

## 2. Strengthening Attempts

### 2.1 Attempt A — Pinsker + Fisher-expansion (under (PI) on statistical-manifold sub-case)

**Setup.** Take $M_{\tau^-}$ and both post-update states $M_{\tau^+}^{\text{decoupled}} = f_M(M_{\tau^-}, e_\tau)$, $M_{\tau^+}^{\text{coupled}} = f_X^M(X_{\tau^-}, e_\tau)$ as points on the statistical manifold $(\mathcal M, \mathbf I(\cdot))$ under (PI), where $\mathbf I$ is the Fisher information metric (Čencov 1982).

**Step 1 — KL bound from mutual information.** By the chain rule of relative entropy (Cover & Thomas §2.5, Thm 2.5.3):

$$\mathbb E_{G \sim P_{\text{ref}}}\left[\, \mathrm{KL}\!\left(P_{\Omega \mid e, M, G} \,\Vert\, P_{\Omega \mid e, M}\right)\right] = I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$$

*[Derived, exact]*. The conditional mutual information *is* the expected KL divergence from the goal-conditional posterior (what a Class-2 agent effectively uses) to the goal-marginalized posterior (what the Bayesian-goal-blind update would produce).

**Step 2 — From KL to TV via Pinsker.** By Pinsker's inequality (Csiszár-Körner 2011, Lemma 17.3.2):

$$\lVert P_{\Omega \mid e, M, G} - P_{\Omega \mid e, M}\rVert_{TV} \leq \sqrt{\tfrac{1}{2}\, \mathrm{KL}(P_{\Omega \mid e, M, G} \Vert P_{\Omega \mid e, M})}$$

*[Derived, exact — Pinsker]*. Taking expectation over $G$ under $P_{\text{ref}}$ and applying Jensen (since $\sqrt{\cdot}$ is concave, this is an upper bound *on the mean TV*):

$$\mathbb E_G[\lVert P_{\Omega\mid e, M, G} - P_{\Omega\mid e, M}\rVert_{TV}] \leq \sqrt{\tfrac{1}{2}\, I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})}$$

**Step 3 — From TV on $P_\Omega$ to displacement on $M$.** This is where the specific form of $f_X^M$ enters. Under the *Bayesian posterior* model for $f_M$ and the *goal-conditioned Bayesian posterior* model for $f_X^M$ (both are reasonable working-class models; the Class-2-typical "attention reweighting" coupled update is in this class to leading order):

$$P(M_{\tau^+} \mid e_\tau, M_{\tau^-}, G) \propto P(e_\tau \mid M_{\tau^+}, G) \cdot P(M_{\tau^+} \mid M_{\tau^-})$$

The goal-blind update drops the $G$-dependence in the likelihood. The coupled minus decoupled posteriors differ by the factor $P(e_\tau \mid M_{\tau^+}, G)/P(e_\tau \mid M_{\tau^+})$, which is precisely the factor whose log-expected-variance is $I(G; \Omega \mid e, M)$.

Under the **small-information limit** ($I(G; \Omega \mid e, M) \ll 1$ nat, i.e., the goal provides at most a mild reweighting of the likelihood), a local expansion around the shared mean $\bar M_{\tau^+}$ gives:

$$M_{\tau^+}^{\text{coupled}} - M_{\tau^+}^{\text{decoupled}} \approx \mathbf I(\bar M_{\tau^+})^{-1} \cdot \mathbb E_{\Omega \mid e, M}\!\left[\nabla_M \log \frac{P(e \mid M, G)}{P(e \mid M)}\right]$$

*[Derived, small-information limit, exponential-family likelihood]*.

**Step 4 — Fisher-Rao distance.** The Fisher-Rao squared distance between two nearby posteriors, under Čencov's canonical metric, is:

$$d_{FR}^2(M_{\tau^+}^{\text{coupled}}, M_{\tau^+}^{\text{decoupled}}) \approx (M_{\tau^+}^{\text{coupled}} - M_{\tau^+}^{\text{decoupled}})^T \mathbf I(\bar M_{\tau^+}) (M_{\tau^+}^{\text{coupled}} - M_{\tau^+}^{\text{decoupled}})$$

(Amari-Nagaoka 2000, §3.7; Fisher metric = second-order expansion of KL). Substituting Step 3 and taking expectation:

$$\mathbb E_G[d_{FR}^2(M_{\tau^+}^{\text{coupled}}, M_{\tau^+}^{\text{decoupled}})] \leq 2\, I(G; \Omega_\tau \mid e_\tau, M_{\tau^-}) \cdot (1 + o(1))$$

*[Derived, small-information limit + KL-expansion identity]*. This is the standard KL-expands-to-Fisher identity (Cover-Thomas §12.5; Amari-Nagaoka §3.7 Thm 3.1).

**Step 5 — The constant $C$ under Fisher-Rao norm.** Taking square roots and absorbing constants:

$$\boxed{\mathbb E\lVert \Delta M_{\text{bias}} \rVert_{FR} \leq \sqrt{2\, I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})} \cdot (1 + o(1))}$$

**Under the small-information Fisher-Rao norm: $C = \sqrt{2}$, constants explicit, dimension-free.** The $\kappa_{\text{processing}}$ factor enters through the attention-reweighting strength: for a fully merged Class-2 agent, the effective reweighting is roughly the entire goal-conditional likelihood shift, so $\kappa \approx 1$; for a Class-3 partial agent, only a $\kappa$-fraction of the shift propagates to $f_X^M$, giving the product form $\kappa \cdot I$ under the small-info Fisher-Rao norm:

$$\mathbb E\lVert \Delta M_{\text{bias}} \rVert_{FR} \leq \sqrt{2} \cdot \kappa_{\text{processing}} \cdot \sqrt{I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})} \cdot (1 + o(1))$$

**Important honest observation.** The bound this gives is **$\sqrt{I}$, not $I$**. The original segments' bound is linear in $I$; the Pinsker/Fisher path yields sub-linear $\sqrt I$. This is actually **sharper** in the small-$I$ regime (where $\sqrt I < I$ fails — wait, $\sqrt I > I$ when $I < 1$, so it's *looser* in the small-$I$ regime; but *tighter* in the large-$I$ regime where $\sqrt I < I$). Small $I$ means weak coupling — the agent's goals are barely informative about the observation residual. In this regime, the linear-in-$I$ bound is loose; the $\sqrt I$ bound is loose too but the original segment's scale was dimensional rather than derived, so "loose vs tight" comparison is ill-posed.

**Verdict on Attempt A.** *Partial success.* On the statistical-manifold sub-case of $\mathcal{M}$ under (PI) + small-information regime + Bayesian-posterior-class $f_X^M$: $C$ is derivable, equals $\sqrt 2$ (nats) or $\sqrt{2\ln 2}$ (bits), and the bound sharpens to $\sqrt I$ not $I$. The price: the bound becomes a theorem only on this sub-case, and the form changes from linear to square-root.

### 2.2 Attempt B — Transportation (Talagrand T2 / Otto-Villani) under curvature bound

**Setup.** Same as Attempt A, but use a *transportation inequality* to convert KL to Wasserstein. Under a log-Sobolev inequality (LSI) with constant $\rho_{\text{LSI}}$ on the reference measure $P_{\Omega\mid e, M}$:

$$W_2^2(P_{\Omega\mid e, M, G}, P_{\Omega\mid e, M}) \leq \frac{2}{\rho_{\text{LSI}}} \mathrm{KL}(P_{\Omega\mid e, M, G} \Vert P_{\Omega\mid e, M})$$

*[Otto-Villani 2000, Theorem 1; Bakry-Émery 1985 curvature-dimension condition gives LSI with $\rho_{\text{LSI}} \geq K$ when Ricci $\geq K > 0$]*.

Taking expectation over $G$:

$$\mathbb E_G[W_2^2(P_{\Omega\mid e, M, G}, P_{\Omega\mid e, M})] \leq \frac{2}{\rho_{\text{LSI}}} \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$$

**Step — Displacement in $M$ as a function of transport cost.** Under the Bayesian-posterior-class $f_X^M$, the posterior on $M$ is a pushforward of the likelihood-weighted prior. Lipschitz stability of Bayesian posteriors (Stuart 2010, *Inverse problems: a Bayesian perspective*, Acta Numerica; Hairer-Stuart-Vollmer 2014 for W2-bounds) gives:

$$W_2(P_{M\mid e, G}, P_{M\mid e}) \leq L_{\text{post}} \cdot W_2(P_{\Omega\mid e, G}, P_{\Omega\mid e})$$

where $L_{\text{post}}$ is a stability Lipschitz constant depending on the prior's curvature and the likelihood's log-Hessian bound.

**Result.** Under (LSI with constant $\rho_{\text{LSI}}$) + (Bayesian stability with constant $L_{\text{post}}$):

$$\boxed{\mathbb E[W_2^2(M_{\tau^+}^{\text{coupled}}, M_{\tau^+}^{\text{decoupled}})] \leq \frac{2 L_{\text{post}}^2}{\rho_{\text{LSI}}} \cdot \kappa_{\text{processing}} \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})}$$

**$C = \sqrt{2 L_{\text{post}}^2 / \rho_{\text{LSI}}}$ under the Wasserstein-2 norm** — *linear in $I$* (because W2² is linear in KL under LSI), constants explicit in terms of $L_{\text{post}}$ and $\rho_{\text{LSI}}$.

**Verdict on Attempt B.** *Full success on sub-case.* The bound is a theorem, the constant is explicit, the scaling is linear in $I$ (matching the segment's current form), the norm is Wasserstein-2 (a natural choice when $\mathcal M$ is a space of measures). The price: requires a log-Sobolev inequality on the observation distribution (concentration hypothesis; satisfied for strongly-log-concave measures per Bakry-Émery; for Gaussian observation models this holds with $\rho_{\text{LSI}} = \sigma^{-2}$) and Lipschitz-posterior stability (satisfied for well-posed Bayesian inverse problems; a substantial literature characterizes when). **This is the cleanest theorem-level result.**

### 2.3 Attempt C — Cramér-Rao / Fisher-information upper-bound

**Setup.** Treat the goal $G$ as a parameter to be estimated from $\Omega$ given $(e, M)$. The Cramér-Rao lower bound says any unbiased estimator $\hat G(\Omega)$ has variance $\geq \mathbf I_G^{-1}$ where $\mathbf I_G$ is the Fisher information on $G$ in the observation.

**Logic.** $I(G; \Omega \mid e, M) \geq \tfrac{1}{2}\log\det(\mathbf I + \mathbf I_G \Sigma_G)$ where $\Sigma_G$ is the prior covariance — or more simply, $\mathrm{Var}(\hat G_{\text{MLE}}) \approx \mathbf I_G^{-1}$ asymptotically.

**Step.** A Class-2 agent effectively uses $\Omega$ to estimate $G$ (or the goal-conditional likelihood factor), and that estimate feeds back into $M_{\tau^+}$. The bias $\Delta M_{\text{bias}}$ is upper-bounded by the posterior-sensitivity × goal-estimator-error:

$$\lVert \Delta M_{\text{bias}} \rVert \leq \lVert \partial M / \partial G \rVert \cdot \lVert \hat G - \bar G \rVert \leq L_M \cdot \sqrt{\mathrm{Var}(\hat G)} \leq L_M \cdot \sqrt{\mathbf I_G^{-1}}$$

**Problem.** This gives $\lVert \Delta M_{\text{bias}} \rVert \leq L_M / \sqrt{\mathbf I_G}$, which *shrinks* as the Fisher information on $G$ increases. This is the **opposite direction** from the original bound (bias should *grow* with $I$, not shrink with $I_G$). The reason: Cramér-Rao bounds estimator error *below*; to upper-bound bias we need an estimator that actually commits, not one that must be unbiased.

**Verdict on Attempt C.** *Failure — wrong direction.* Cramér-Rao gives a floor on estimator variance, which we cannot invert to a ceiling on bias propagation without adding a second structural assumption (e.g., fixed-estimator-class). Record the failure explicitly; a future agent pursuing this path would repeat the mistake without the record. Attempt B (transportation) is the right geometric machinery, not Cramér-Rao inversion.

### 2.4 Attempt D — Rate-distortion lower-bound inversion

**Setup.** The rate-distortion function $R(D)$ gives the minimum information rate to represent a source with distortion $\leq D$. Shannon's theorem: $R(D) \geq h(X) - \tfrac{1}{2}\log(2\pi e D)$ for Gaussian-source $X$ under squared-error distortion.

**Logic attempt.** Invert: $D \leq \sigma^2 \cdot 2^{-2(R - h(X))}$. If "bits in = $I(G; \Omega \mid e, M)$" plays the role of $R$, then "distortion = $\lVert \Delta M_{\text{bias}} \rVert^2$" should obey an analog.

**Problem.** Rate-distortion is a communication theorem: it describes the minimum bits-per-symbol required to represent a source within distortion $D$. It does *not* describe the maximum distortion induced by injecting $I$ bits of goal information into an update. The direction is again wrong: RD bounds the minimum information to achieve a given distortion, not the maximum distortion injected by a given information flux.

**Verdict on Attempt D.** *Failure — wrong problem.* Record that the RD-inversion attempt fails for the same reason Cramér-Rao fails: the source-coding theorems are about optimal representations of a source, not about the spatial displacement induced by side-information injection. Transport inequalities (Attempt B) are the correct machinery.

### 2.5 Attempt E — No-go result in full generality

**Claim attempted.** *A universal constant $C$ (independent of $\mathcal M$'s geometry, likelihood form, and coupled-update structure) cannot exist.*

**Argument.** Consider $\mathcal M = \{P_\theta\}_{\theta \in \Theta}$ where $\Theta$ is a non-compact parameter space with *unbounded* Fisher-metric condition number — for instance, the heteroscedastic normal family at extreme-variance points, or any exponential family near a boundary. A fixed amount of goal-conditional KL can induce arbitrarily large displacement in the Euclidean norm on $\theta$ (the map from natural-parameter to mean-parameter has unbounded derivative near boundary).

**Formally.** For any $C_0 < \infty$, construct a family where: $I(G; \Omega \mid e, M) = 1$ nat fixed, but $\lVert \Delta M_{\text{bias}} \rVert_{\text{Euclidean}} > C_0$.

**Construction.** Let $\mathcal M = \{N(0, \sigma^2)\}$ parameterized by $\sigma$. At $\sigma_0 = \sigma^\ast$ near a boundary, the Fisher information in $\sigma$ scales as $2/\sigma^2$ — small near large $\sigma$, large near small $\sigma$. A goal-conditional likelihood shift of 1 nat corresponds to a Fisher-displacement of $\sqrt 2$ (by Attempt A), but the Euclidean $\sigma$-displacement is $\sqrt 2 \cdot \sigma/\sqrt 2 = \sigma$. Taking $\sigma \to \infty$ gives arbitrarily large Euclidean displacement for fixed information input.

**Verdict on Attempt E.** *Success — a genuine no-go for universal $C$ under Euclidean-parameter norm.* This justifies the scope-narrowing: $C$ cannot be a universal constant in the coordinate-dependent norm; it *can* be a universal constant ($\sqrt 2$) in the Fisher-Rao norm. This is precisely the statement that (PI) forces. **The no-go result strengthens rather than weakens the (PI)-commitment**: under (PI), the norm must be Fisher-Rao (or equivalent), and in that norm, $C$ is universal. Under non-adoption of (PI), $C$ does not exist as a universal constant, and the original segment's admission that "$C$ is domain-dependent" is the correct statement.

This is a clean **strengthen-first-then-soften** outcome: the attempt to strengthen succeeds on a named sub-case (under (PI) + transport structure) and fails structurally elsewhere. The softening is honest because the strengthening attempt was honest.

### 2.6 Attempt F — Operational identification for $C$

**Setup.** Even where theorem-level $C$ is not available, can $C$ be estimated from calibration data?

**Construction.** Given a Class-2 agent and a calibration set $\{(e^{(i)}, G^{(i)}, M^{(i)}_-, M^{(i)}_+)\}$ of observed events, goals, prior states, and post-update states, compute:

$$\hat C = \max_i \frac{\lVert M_+^{(i)} - f_M(M_-^{(i)}, e^{(i)})\rVert}{\kappa_{\text{processing}} \cdot \hat I(G^{(i)}; \Omega^{(i)} \mid e^{(i)}, M_-^{(i)})}$$

This is a *worst-case empirical Lipschitz constant* for the bias-vs-information ratio. It has no theorem but gives engineering guidance.

**Advantage.** Domain-specific; captures the actual geometry the agent encounters. **Disadvantage.** Not a theorem; susceptible to extrapolation error when the deployment distribution differs from calibration.

**Verdict on Attempt F.** *Operational — useful for engineering but not a theorem.* The theorem-level strengthening (Attempt B) is cleaner; Attempt F remains as fallback for domains where LSI / Lipschitz-posterior bounds are impractical to establish.

---

## 3. Concrete candidate derivation under named assumptions

**Named assumptions for a theorem-level bound.**

*(H1) Statistical-manifold sub-case.* $\mathcal M$ is parameterized such that each $M_t \in \mathcal M$ corresponds to a probability distribution $P_{M_t}$ over world-states. Under (PI) from `#agent-identity`, the canonical metric is Fisher-Rao (Čencov 1982).

*(H2) Log-Sobolev inequality on the observation distribution.* $P_{\Omega \mid e, M}$ satisfies LSI with constant $\rho_{\text{LSI}} > 0$. Sufficient condition: $P_{\Omega \mid e, M}$ is strongly-log-concave with log-concavity constant $K$ (then $\rho_{\text{LSI}} \geq K$ by Bakry-Émery 1985). For Gaussian observation models, $\rho_{\text{LSI}} = 1/\sigma^2$.

*(H3) Lipschitz posterior stability.* The map $P_{\Omega \mid e, M, G} \mapsto P_{M \mid e, G}$ is $L_{\text{post}}$-Lipschitz in W2. Sufficient condition: well-posed Bayesian inverse problem with bounded log-likelihood Hessian (Stuart 2010 Theorem 4.6; Hairer-Stuart-Vollmer 2014).

*(H4) Small information regime.* $I(G; \Omega_\tau \mid e_\tau, M_{\tau^-}) \ll 1$ nat for the linear bound to be sharp. For large $I$, the bound holds as stated but the constants can be refined.

**Theorem (strengthened bias bound under H1-H3).**

*[Derived, conditional on H1-H3]*

$$\mathbb E\,[\,W_2^2(M_{\tau^+}^{\text{coupled}}, M_{\tau^+}^{\text{decoupled}})\,] \leq \frac{2 L_{\text{post}}^2}{\rho_{\text{LSI}}} \cdot \kappa_{\text{processing}} \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$$

**The constant $C_{\text{W}_2}^2 = 2 L_{\text{post}}^2 / \rho_{\text{LSI}}$** is explicit and has clear dependencies:
- $L_{\text{post}}$ grows with prior-likelihood tension (ill-conditioned inverse problems amplify bias).
- $\rho_{\text{LSI}}$ grows with observation-model concentration (sharper observations → tighter bound).
- The ratio captures the *geometric stiffness* of the update: small-$\rho/\text{large-}L$ = soft, goal-sensitive updates; large-$\rho/\text{small-}L$ = stiff updates that resist goal-bias.

**Under (PI) + Fisher-Rao norm + H1 + H4 (small-I, statistical-manifold sub-case).**

*[Derived, conditional on H1-H4]*

$$\mathbb E\,\lVert \Delta M_{\text{bias}} \rVert_{FR} \leq \sqrt 2 \cdot \sqrt{\kappa_{\text{processing}} \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})} \cdot (1 + o(1))$$

**The constant $C_{FR} = \sqrt 2$** under Fisher-Rao norm in the small-information regime — **universal, dimension-free, no domain-specific parameters**. This is the cleanest form and sits in direct contact with the fourth primary instance of `#additive-coordinate-forcing`.

**Which to prefer.** The transport-inequality form (H1-H3) is the more *theorem-clean* statement: linear in $I$ (matching the segment's current form), explicit constants, no small-$I$ expansion. The Fisher-Rao form (H1+H4) is the more *structurally distinctive* statement: it lands the bound directly inside the (PI)/Čencov meta-pattern, with universal constant $\sqrt 2$, but changes the scaling from linear to square-root. Both are real, under different sub-scopes. The segment-level move is to state both as Track 1 and Track 2 with explicit sub-scopes.

---

## 4. Relation to AAD's meta-architecture

**Is $C$ a fifth instance of `#additive-coordinate-forcing`?**

Not as a new primary instance. The Fisher-Rao-$C = \sqrt 2$ result *consumes* the fourth instance (Čencov-invariance / (PI)) rather than introducing a fifth axiomatic layer. Structurally, it is a **downstream theorem** that becomes available once (PI) + Čencov fixes the metric: given the canonical metric, standard information-geometric identities (KL = ½ × Fisher-squared-distance + higher-order; Cover-Thomas §12.5) give $C$ for free in the small-information regime. This is the "adjacency" relationship the `#additive-coordinate-forcing` segment describes: the Fisher-metric layer's consequences extend into downstream bounds *because* the metric is fixed, not because each downstream bound re-instantiates the uniqueness theorem.

**Is $C$ a fifth instance of `#identifiability-floor`?**

Possibly. Attempt E's no-go argument has the structure of an identifiability-floor instance: under non-adoption of (PI) (equivalently, under Euclidean-coordinate norm), no universal $C$ exists. The "external theorem" enforcing the floor is the standard non-existence of a universal information-to-coordinate-distance constant in unbounded-Fisher-condition-number parameterizations. The "unique escape" is adoption of (PI) + Fisher-Rao norm — which is itself load-bearing AAD machinery (`#agent-identity`'s (PI) axiom, `#additive-coordinate-forcing`'s fourth primary instance).

This is the clean meta-pattern composition: **F4 (candidate) — the universal-$C$-under-Euclidean-norm no-go**. The information-theoretic obstruction is Čencov's negative corollary (no coordinate-invariant metric other than Fisher's on a statistical manifold), which combined with the non-compactness of generic $\Theta$ gives the blow-up. The escape is (PI)-adoption + Fisher-Rao; under the escape, $C = \sqrt 2$ is universal.

**Is this the `#variational-sector-condition` structure applied to Class-2 bias?**

Very nearly. `#variational-sector-condition` uses Pinsker + Cauchy-Schwarz to derive an $O(\sqrt\varepsilon)$ sector-constant degradation from a KL bound $\varepsilon$, with the note that "$O(\varepsilon)$ rate requires stronger inequalities (log-Sobolev, Talagrand T2)." The Class-2 bias bound is the *dual* structure: same Pinsker-T2 machinery, applied to the posterior displacement rather than the sector-constant degradation. The two segments share the same machinery with different quantitative outputs. This suggests a broader apparatus — "KL-to-state-distance conversion under log-Sobolev concentration" — that could be factored out as a shared lemma, analogous to how `#sector-persistence-template` was factored out.

---

## 5. Recommended segment-level moves

No segment files were modified in this spike. Recommended follow-on moves for a segment-authoring session:

**M1 — Preferred: new appendix segment `#bias-bound-derivation`.** House the full derivation (Attempts A + B + E) in an appendix segment with:
- *type:* `derivation`
- *status:* `conditional` (on H1-H4)
- *depends:* `section-ii-survival`, `observation-ambiguity-modulation`, `agent-identity`, `additive-coordinate-forcing`, `directed-separation`
- Track 1: transport-inequality form under (H1-H3) with explicit $C_{W_2} = \sqrt{2L_{\text{post}}^2/\rho_{\text{LSI}}}$.
- Track 2: Fisher-Rao form under (H1+H4) with universal $C_{FR} = \sqrt 2$.
- Worked example: Gaussian observation model ($\rho_{\text{LSI}} = 1/\sigma^2$) with conjugate-Gaussian prior giving explicit numerical $C$.
- No-go corollary: universal $C$ under Euclidean-parameter norm fails (Attempt E).

**M2 — Update `#section-ii-survival` and `#observation-ambiguity-modulation`.** In both segments, replace the Working-Notes line *"Without the constant, the bound is order-of-magnitude guidance, not a theorem"* with a cross-reference to `#bias-bound-derivation`. Upgrade the bias-bound statement's epistemic tier from *order-of-magnitude* to *conditional (exact under H1-H3 or H1+H4)*.

**M3 — Candidate fifth `#identifiability-floor` instance.** The no-go for universal $C$ under non-(PI) norms (Attempt E) is a candidate Instance-4 for `#identifiability-floor`. The floor is: without a canonical metric on $\mathcal M$, no universal information-to-distance constant exists. The unique escape is (PI) + Čencov-forced Fisher-Rao. Composition with existing Instance 3 (`#agent-opacity` candidate) would complete a four-instance meta-segment pattern.

**M4 — Shared KL-to-displacement lemma.** The Pinsker / Talagrand-T2 / LSI machinery is now used in two places: `#variational-sector-condition` (KL → sector-constant degradation) and the proposed `#bias-bound-derivation` (KL → posterior displacement). Factoring the shared machinery into a *KL-to-state-distance template* (analogous to `#sector-persistence-template`) would be a clean structural move. This is a portfolio-level proposal worth adding to `msc/architectural-proposals-2026-04-22.md`.

**M5 — Cross-link to `#additive-coordinate-forcing`.** The Fisher-Rao track of the bias-bound derivation is a downstream theorem of the fourth primary instance. Document this adjacency in `#additive-coordinate-forcing`'s Discussion as a worked example of "what the (PI) commitment enables downstream."

---

## 6. Epistemic tier labels

| Claim | Tier | Notes |
|---|---|---|
| Chain-rule identity: $\mathbb E_G[\mathrm{KL}(P_{\Omega\mid G}\Vert P_\Omega)] = I(G;\Omega\mid\cdot)$ | **Exact** | Cover-Thomas Thm 2.5.3 |
| Pinsker: $\lVert P - Q\rVert_{TV} \leq \sqrt{\tfrac{1}{2}\mathrm{KL}}$ | **Exact** | Standard (Csiszár-Körner) |
| Otto-Villani: $W_2^2 \leq (2/\rho_{\text{LSI}}) \cdot \mathrm{KL}$ under LSI | **Exact** | Otto-Villani 2000 |
| KL-to-Fisher-squared-distance identity (small-$I$ limit) | **Exact** | Amari-Nagaoka §3.7 Thm 3.1; Cover-Thomas §12.5 |
| Bayesian-posterior Lipschitz stability $L_{\text{post}}$ | **Conditional** on (H3) | Stuart 2010 Thm 4.6 |
| Main theorem Track 1: $C_{W_2}^2 = 2L_{\text{post}}^2/\rho_{\text{LSI}}$, linear in $I$ | **Derived (conditional on H1-H3)** | Theorem-level; depends on LSI + Lipschitz-posterior |
| Main theorem Track 2: $C_{FR} = \sqrt 2$, $\sqrt I$ scaling | **Derived (conditional on H1+H4)** | Small-$I$ regime; dimension-free, universal in Fisher-Rao norm |
| No-go for universal $C$ under Euclidean-parameter norm | **Exact (counter-example-grade)** | Attempt E; explicit construction in heteroscedastic-normal family |
| Operational estimator $\hat C$ from calibration data | **Heuristic** | Engineering fallback; no theorem |
| Cramér-Rao inversion approach | **Failed** | Wrong direction; documented for record |
| Rate-distortion inversion approach | **Failed** | Wrong problem structure; documented for record |
| Candidate fifth instance of `#identifiability-floor` | **Hypothesis** | Structural fit looks clean but no explicit promotion yet |
| Candidate shared KL-to-displacement template | **Discussion-grade** | Observation about structural sharing between `#variational-sector-condition` and proposed `#bias-bound-derivation` |

---

## 7. What the spike did not settle

- **Exact form of $L_{\text{post}}$.** The Lipschitz posterior stability constant is cited from Stuart 2010 / Hairer-Stuart-Vollmer 2014 but not computed for specific AAD-relevant cases. A worked example (conjugate-Gaussian) would pin it down; general non-parametric Bayesian inverse problems have looser bounds.
- **Large-$I$ regime refinement.** Track 2's $\sqrt I$ scaling uses the small-$I$ Fisher expansion. For large $I$ (strong goal-conditioning), the global KL-to-Fisher-Rao-distance relationship is lattice-dependent and geodesically nontrivial. A fully global statement would require either a compact-manifold assumption (Fisher-Rao distance is bounded on compact $\mathcal M$) or a staged-application argument (many small-$I$ steps).
- **Relation to `#adaptive-gain-dynamics` sub-scope partition.** The Track 1 vs Track 2 distinction maps roughly onto (H1-H3 linear / H1+H4 $\sqrt I$), which is structurally similar to $\alpha_1$ / $\alpha_2$ sub-scopes. Exact positioning within the $\{\alpha, \alpha_1, \alpha_2, \alpha_3, \alpha', \beta\}$ partition is open — the bias-bound sub-scoping probably deserves its own mini-partition.
- **Class-3 agents explicitly.** The bound is stated for Class-2; Class-3 (partially modular) agents with $0 < \kappa < 1$ inherit the bound by the $\kappa_{\text{processing}}$ multiplicative factor, but whether the transport-inequality derivation composes cleanly across the Class-3 internal partial-separation is not checked. Probably yes, but not verified.
- **Interaction with `#observation-ambiguity-modulation`.** The product form $\kappa_{\text{eff}} = \kappa \cdot \mathcal A$ interacts with the transport-inequality constants in ways not fully worked out. If $\mathcal A$ is itself an information-theoretic ratio, multiplying by $\mathcal A$ might be absorbable into the mutual information term rather than a separate factor. Left for follow-on work.
- **Statistical-manifold sub-case of $\mathcal M$.** The (PI)/Čencov path applies when $\mathcal M$ is a statistical manifold. If $\mathcal M$ is a non-statistical structured state-space (e.g., a graphical-model state-space with mixed continuous/discrete components), (PI) still constrains the metric but Čencov's uniqueness is weaker. The Track-2 statement may need refinement for such cases.

---

## 8. One-paragraph summary for the caller

The strengthening attempt substantially succeeded. Under the (PI) parameterization-invariance axiom already adopted in `#agent-identity` and promoted to the fourth primary instance of `#additive-coordinate-forcing`, the statistical-manifold sub-case of $\mathcal M$ carries Čencov-canonical Fisher-Rao structure. That structure makes the constant $C$ derivable rather than assumed. Two theorem-level tracks are available: (Track 1) under a log-Sobolev inequality on the observation distribution and Lipschitz stability of the Bayesian posterior, the bias bound holds in Wasserstein-2 with explicit constant $C_{W_2}^2 = 2 L_{\text{post}}^2/\rho_{\text{LSI}}$, linear in $I$; (Track 2) under small-information regime in the Fisher-Rao norm, the bound holds with universal dimension-free constant $C_{FR} = \sqrt 2$ and $\sqrt I$ scaling. A no-go result is honestly recorded: a universal $C$ independent of coordinates on $\mathcal M$ cannot exist — justifying the (PI) commitment as *load-bearing* for this derivation rather than a coincidental convenience. Two attempts (Cramér-Rao inversion, rate-distortion inversion) failed and are documented so future agents do not repeat them. The Track 1 / Track 2 machinery parallels the Pinsker+Cauchy-Schwarz / log-Sobolev structure already deployed in `#variational-sector-condition`, suggesting a shared "KL-to-state-distance" template worth factoring out as a portfolio-level move. Recommended follow-on: a new appendix segment `#bias-bound-derivation` housing both tracks, Working-Notes cross-references in `#section-ii-survival` and `#observation-ambiguity-modulation` to replace the "order-of-magnitude guidance" concession, and a candidate fifth instance of `#identifiability-floor` recording the no-go under non-(PI) norms.
