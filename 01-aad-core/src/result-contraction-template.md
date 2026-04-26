---
slug: result-contraction-template
type: result
status: conditional
depends:
  - result-sector-persistence-template
  - deriv-sector-condition
  - der-gain-sector-bridge
  - form-composition-closure
  - deriv-critical-mass-composition
  - disc-separability-pattern
stage: draft
---

# Result: Contraction Template

`#result-sector-persistence-template` states AAD's persistence arguments with a Euclidean sector condition (T2) matched to a quadratic Lyapunov in Euclidean norm. Generalizing the sector inequality to a **contraction-metric condition** (Lohmiller & Slotine 1998) preserves the template's ultimate-bound results while extending its coverage in three directions: (a) sub-scope α gains natural non-Euclidean metrics that remove condition-number penalties currently visible in #der-gain-sector-bridge; (b) two additional sub-scope β items (PID-bounded-plant; non-convex-within-basin) promote to derived sub-scope metric-α₂ under explicit conditions; (c) composition acquires **topology-indexed closure results** (parallel / hierarchical / small-gain-feedback) from Slotine 2003 that generalize `#deriv-critical-mass-composition`'s matched-symmetric-Tier-1 closed form to heterogeneous sub-agents. This segment states the generalization once in parameter-free form so that each lifting citation can reference it and specify only what varies.

`#result-sector-persistence-template` remains as the $M = I$ Euclidean specialization.

## Formal Expression

### Preconditions

*[Template preconditions (contraction-template)]*

Let $\xi(t) \in \mathbb{R}^n$ evolve under $\dot\xi = -F(\xi, t) + w(t)$ where $F$ is $C^1$ in $\xi$ and continuous in $t$. Let $M: \mathbb{R}^n \times \mathbb{R}_+ \to \mathbb{S}_{++}^n$ be a smooth symmetric positive-definite matrix-valued function with uniform conditioning:

$$m_1 I \preceq M(\xi, t) \preceq m_2 I \quad \text{for all } \xi \in \mathcal{B}_R,\, t \geq 0 \tag{M0}$$

with constants $0 < m_1 \leq m_2 < \infty$.

**(CT1) Zero correction at zero state.** $F(0, t) = 0$ for all $t$.

**(CT2) Local differential-contraction condition.** There exist $\lambda > 0$ and $R > 0$ such that for all $\xi \in \mathcal{B}_R$, $t \geq 0$:

$$\dot M(\xi, t) + M(\xi, t) \frac{\partial F}{\partial \xi}(\xi, t) + \Big(\frac{\partial F}{\partial \xi}(\xi, t)\Big)^T M(\xi, t) \succeq 2\lambda\, M(\xi, t). \tag{CT2}$$

**(CT3) Bounded disturbance.** Either Model D ($\lVert w(t)\rVert \leq \rho_\xi$) or Model S ($w(t)$ Wiener-process increment with $\mathbb E[\lVert w(t)\rVert^2] = \sigma_\xi^2$).

### Ultimate bound — Model D

*[Result (contraction-template-D), conditional on (M0), (CT1)–(CT3-D)]*

Under the preconditions with $V(\xi, t) = \xi^T M(\xi, t) \xi$, the state is ultimately bounded:

$$\limsup_{t \to \infty} \lVert \xi(t) \rVert \leq \frac{\rho_\xi}{\lambda} \sqrt{\frac{m_2}{m_1}}. \tag{CT-D}$$

Structural persistence (the ultimate bound fits within the contraction region $\mathcal B_R$) requires

$$\lambda R \sqrt{m_1/m_2} > \rho_\xi. \tag{CT-D-persist}$$

*Proof sketch.* Compute $\dot V = \xi^T \dot M \xi - 2 \xi^T M F + 2 \xi^T M w$. Integrate (CT2) along the ray $s\xi$, $s \in [0,1]$, using $F(0) = 0$: $2 \xi^T M F(\xi, t) \geq 2\lambda\, \xi^T M \xi - \xi^T \dot M \xi$. Substituting: $\dot V \leq -2\lambda V + 2 \xi^T M w$. Cauchy-Schwarz in $M$-inner product + (M0) gives the affine-contraction bound on $W = \sqrt V$; conversion to Euclidean norm via (M0) yields (CT-D). $\square$

### Ultimate bound — Model S (with Itô correction)

*[Result (contraction-template-S), conditional on (M0), (CT1)–(CT3-S), Itô-compatible metric]*

Under stochastic disturbance $d\xi = -F(\xi, t)\,dt + \sigma_\xi\,dW_t$ and a metric $M$ satisfying the Itô-correction bound $\tfrac{1}{2}\sigma_\xi^2\,\mathrm{tr}(M + \text{Hessian correction in drift direction}) \leq c_{\text{Itô}}\,m_2$ locally (automatic for state-independent $M$; bounded by $M$'s Hessian otherwise), the stopped process satisfies

$$\mathbb E[V(\xi(t \wedge \tau_R), t \wedge \tau_R)] \leq V(\xi(0), 0)\,e^{-2\lambda t} + \frac{n\sigma_\xi^2 c_{\text{Itô}} m_2}{2\lambda},$$

where $\tau_R = \inf\{t: \lVert\xi(t)\rVert > R\}$. Mean-square structural persistence requires

$$\lambda R^2 > \frac{n \sigma_\xi^2 c_{\text{Itô}}\, m_2^2}{2 m_1}. \tag{CT-S-persist}$$

This is the natural extension of `#deriv-sector-condition`'s Prop A.1S region condition (Khasminskii 2012 ch. 5) to weighted metrics. When $M = I$ (Euclidean), $c_{\text{Itô}} = 1$, and the result reduces to Prop A.1S.

### Recovery of `#result-sector-persistence-template`

When $M \equiv I$ (Euclidean metric, time-independent), (CT2) reduces to

$$-\frac{\partial F}{\partial \xi} - \Big(\frac{\partial F}{\partial \xi}\Big)^T \preceq -2\lambda I,$$

which is the **incremental Euclidean sector condition** (strong monotonicity of $F$ in Euclidean norm, equivalently **DA2'-inc** in `#form-composition-closure`'s bridge-lemma language). This implies the one-point sector condition $\xi^T F(\xi) \geq \lambda \lVert\xi\rVert^2$ by integration along the ray $s\xi$, so $\alpha = \lambda$ when $M = I$. The template's ultimate bound $\rho_\xi/\alpha$ is reproduced with $m_1 = m_2 = 1$.

**The structural observation:** (CT2) at $M = I$ is strictly stronger than (T2) — it requires the Jacobian's symmetric part to be uniformly positive definite everywhere, matching DA2'-inc rather than (T2). The contraction formulation therefore **collapses (T2) and DA2'-inc into one condition** at the cost of requiring differential (Jacobian-level) rather than integral (inner-product-at-a-point) information. This is one of the template's structural contributions: the same condition that runs the template runs the bridge-lemma that `#form-composition-closure` depends on, so the gap between single-agent persistence and composite tracking faithfulness closes when (CT2) holds.

### Sub-scope metric-α₁ / metric-α₂ / metric-β partition

The contraction formulation refines `#deriv-sector-condition`'s A2' sub-scope partition into three tiers:

**Sub-scope metric-α₁ (Euclidean metric, AAD-internally derived via DA2'-inc ≡ (CT2) with M=I).** Scalar Kalman, Euclidean strongly-convex gradient, L2-regularized convex, linear-PD-symmetric. These cases carry (CT2) with $M = I$ which is exactly DA2'-inc — a condition `#form-composition-closure` has required at the composite level all along. AAD's existing commitment already forces (CT2)-Euclidean at these cases; the template surfaces it.

**Sub-scope metric-α₂ (non-Euclidean metric, derived under explicit conditions).** Five cases lift here:

- *Matrix Kalman under information metric* $M = (P^-)^{-1}$: contraction rate $\lambda = \lambda_{\min}(H^T R^{-1} H)/2$ on the observable subspace; Euclidean $\kappa(P^-)$ degradation removed. Under (PI)/Čencov (see `#der-gain-sector-bridge` "Fisher-metric cases under parameterization-invariance"), the information-metric form is *uniquely forced* — AAD-internally derived rather than theorem-imported.
- *Exponential-family natural parameters under Fisher metric* $M = \mathbf I(\theta)$: contraction rate $\lambda = \eta$ globally on the interior of the natural-parameter domain (Fisher-conditioning degradation removed). Also AAD-internally forced under (PI)/Čencov.
- *Hessian-metric strongly-convex* $M = \nabla^2 L$: contraction rate $\lambda = \eta$ under bounded metric-derivative in the drift direction. Theorem-imported (Hessian metric chosen to match loss curvature; no AAD-internal axiom forces the specific coordinate).
- *Linear-Hurwitz-non-symmetric under Lyapunov metric*: $M$ solves $M A + A^T M = -Q$ for $Q \succ 0$. Contraction rate $\lambda = \lambda_{\min}(Q)/(2\lambda_{\max}(M))$ in the $M$-metric. **New coverage:** asymmetric-stable linear corrections where Euclidean A2' fails. Theorem-imported (Lyapunov equation construction is standard; no AAD-internal axiom forces $Q$).
- *PID with bounded plant nonlinearity under Lyapunov metric*: derived under plant-Lipschitz bound $L_p < \lambda_{\min}(Q)/(2\lambda_{\max}(M))$. **Promotion from sub-scope β.** Theorem-imported for the Lyapunov-metric construction; specializations include SPR-tuned PID (phase margin as sector constant; see `#der-gain-sector-bridge` Verified Instances).

**Sub-scope metric-β (contraction-metric formulation fails).** Four cases:

- *Variational / amortized / approximate posteriors*: contraction to the *projected* target (best-in-class $q^\ast$) is derivable, but the projection error $\mathrm{KL}[q^\ast \| p_t]$ to the true posterior is a residual disturbance that contraction machinery cannot address.
- *Rule-based / symbolic / discontinuous updates*: non-smooth $F$; (CT2) requires $C^1$. Piecewise-smooth extensions (Di Bernardo et al. 2014) cover switched systems but not general rule-based reasoning.
- *Severely misspecified agents*: contraction to a wrong target is still wrong. Metric choice is silent on target validity.
- *Per-step SGD / human judgment*: noise-is-disturbance treatment identical to the Euclidean formulation; no improvement from metric choice.

This is **the seventh ladder** in `#disc-separability-pattern` (A2'-scope): metric-α₁ separable-core / metric-α₂ structured-repair / metric-β general-open.

### Compositional contraction

*[Result (compositional-contraction), conditional on Slotine 2003 Thm 1–3 + per-sub-agent (CT1)–(CT3)]*

When sub-agents individually satisfy the preconditions with metrics $M_i$ and rates $\lambda_i$, the composite satisfies (CT1)–(CT3) under specific topologies:

**(CC-parallel) Parallel composition.** $\dot x = (\dot x_1, \dot x_2)^T$ with independent $(\dot x_i = -F_i(x_i) + w_i)$. The composite contracts under $M_c = \mathrm{blockdiag}(M_1, M_2)$ at rate $\lambda_c = \min(\lambda_1, \lambda_2)$. Recovers `#der-team-persistence`'s weakest-link bound; cooperative coupling improves effective disturbance via the existing signed-coupling mechanism.

**(CC-cascade) Hierarchical / lower-triangular cascade.** If $\dot x_1 = f_1(x_1)$ contracts at $\lambda_1$ and $\dot x_2 = f_2(x_1, x_2)$ contracts in $x_2$ at $\lambda_2$ uniformly in $x_1$ with coupling gain $\lVert \partial f_2 / \partial x_1 \rVert \leq k$, the cascade contracts. Rate bounded below by $\min(\lambda_1, \lambda_2)$ up to coupling-gain-dependent adjustment.

**(CC-feedback) Negative feedback with bounded loop gain (Slotine 2003 Thm 3).** Two systems with rates $\lambda_1, \lambda_2$ connected by negative feedback with loop gains $k_{12}, k_{21}$ — the closed loop contracts iff

$$k_{12} k_{21} < 4\lambda_1 \lambda_2. \tag{CC-feedback}$$

### Heterogeneous critical-mass — (CM2-M)

*[Derived (CM2-M), from (CC-feedback) + `#deriv-critical-mass-composition` signed-coupling structure]*

Specializing (CC-feedback) to the signed-coupling structure of `#deriv-critical-mass-composition` for heterogeneous Tier-1M sub-agents with metric-contraction rates $\lambda_1, \lambda_2$, coordination costs $C_1, C_2$, and feedback loop gains $k_{12}, k_{21}$:

$$(\lambda_1 - C_1)(\lambda_2 - C_2) > k_{12} k_{21}/4. \tag{CM2-M}$$

Specializing further to the matched-symmetric case ($\lambda_1 = \lambda_2 = \lambda$, $C_1 = C_2 = C$, $k_{12} = k_{21} = k$): $(\lambda - C)^2 > k^2/4 \iff \lambda - C > k/2$, which matches `#deriv-critical-mass-composition`'s (CM2) with $k = 2\gamma\mathcal T/R$ (up to normalization). **Heterogeneous-architecture composites now have a closed-form critical-mass inequality** where the matched-symmetric case was the only closed form previously available; `#deriv-critical-mass-composition`'s §6.1 obstruction on heterogeneous composites is thereby closed for the Tier-1M case.

## Epistemic Status

*Conditional.* Conditional on (M0) + (CT1)–(CT3) and the specific metric $M$ chosen for each sub-scope α entry. The (CT-D) and (CT-S) ultimate-bound results are standard Lohmiller-Slotine theory (Lohmiller & Slotine 1998; Slotine 2003) specialized to AAD's per-instance state-variable choices; the proof technique is integration along the ray $s\xi$ followed by affine contraction. The contraction-metric primitive (Riemannian M) is standard in nonlinear control theory (Lohmiller-Slotine 1998; Forni & Sepulchre 2014 for the Finsler extension); AAD's contribution is the AAD-internal mapping of M-choices to sub-scope α₁/α₂ and the recognition that the compositional theorems (CC-parallel / CC-cascade / CC-feedback / CM2-M) directly generalize Section III's existing closure machinery.

**The Jacobian-level observation.** `#form-composition-closure`'s DA2'-inc condition is equivalent to (CT2) with $M = I$ for $C^1$ $F$ on convex domains. AAD has been carrying the Jacobian-level Euclidean contraction condition at the composite level all along under the name DA2'-inc; the contraction template's Euclidean specialization surfaces this at the single-agent level.

**The (PI)/Čencov observation.** Two metric-α₂ cases (information-metric Kalman, Fisher-metric exp-family) are AAD-internally forced under the (PI) axiom in `#scope-agent-identity` combined with Čencov's 1982 uniqueness theorem — the fourth primary instance of the meta-pattern in `#disc-additive-coordinate-forcing`. The Euclidean metric-α₁ case is **AAD-internally derived via DA2'-inc equivalence** rather than theorem-imported, structurally connecting it to the bridge lemma in `#form-composition-closure`. The remaining metric-α₂ cases (Hessian, Lyapunov-linear-Hurwitz, Lyapunov-PID) are theorem-imported: the metric choice is problem-specific (matched to loss curvature or plant structure) rather than forced by an AAD-internal axiom.

**Max attainable:** *conditional*. The condition (the metric specification must be consistent with the system structure; the Slotine 2003 compositional theorems must apply to the topology) is inherent to the contraction-metric framework, not removable. Non-smooth systems (rule-based), strategic/game-theoretic equilibria, and systems without regular metric-state coupling remain honestly outside the template's scope (see §Honest failure modes).

**Relationship to monotone-operator theory.** The contraction-metric condition (CT2) is a specialization of monotone-operator theory's strong-monotonicity condition in a Hilbert space with a specific inner product structure (Rockafellar 1970; Bauschke & Combettes 2017 §§4, 22–28). AAD's `#deriv-sector-condition` reading of A2' α/β as operator-family classification — proximal / firmly nonexpansive / cocoercive / strongly-monotone-gradient / linear-PD — identifies the same mathematical content in operator-theoretic language; see that segment's Grounding paragraph for the correspondence. The present template does not claim the contraction-metric machinery as distinctively AAD — it claims the specific instantiation to AAD's state-variable choices and the composition with identifiability-floor + composition-scope-condition content as AAD-distinctive.

## Honest failure modes

The contraction-metric formulation does **not** lift AAD's coverage in five cases:

1. **Non-smooth dynamics.** Rule-based agents, state-machine controllers, threshold-triggered switches, and discontinuous policies fail the $C^1$ requirement. Piecewise-contraction extensions exist (Di Bernardo, Liuzza & Russo 2014, *SIAM J. Control Optim.* 52) but apply to specific switched structures, not general rule-based reasoning. This barrier is structural, not a gap in the metric machinery.

2. **Strategic / adversarial equilibria — three independent convergent obstructions.** The adversarial / strategic half of Section III is structurally outside contraction-metric scope for three distinct reasons that converge on the same conclusion; the convergence matters because it shows the limit is not an accident of one particular framework choice:

    (i) *Compositional-contraction applicability* (Slotine 2003 §III): compositional contraction theorems require each sub-system to be individually contracting *and* for the composition topology to preserve contraction. Two-agent strategic dynamics with opposing objectives yield **saddle-point equilibria of the joint best-response dynamics** — attracting in some directions and repelling in others. Contraction requires attracting fixed points; saddle points break the framework directly.

    (ii) *Passivity universality* (Khalil 2002 ch. 6 Thm 6.4): the dissipation inequality $\dot S \leq s(u, y)$ holds for *all* inputs $u$ by the passivity property's universal quantifier. A strategic opponent can select $u$ to maximize the recipient's storage-function growth rather than respecting the port structure. Passivity delivers cooperative/neutral robustness, not adversarial.

    (iii) *Last-iterate convergence failure* (Daskalakis, Ilyas, Syrgkanis & Zeng 2018 "Training GANs with optimism" *ICLR*): adversarial gradient-ascent-descent dynamics (fictitious play, no-regret dynamics) converge to Nash equilibria *in average-iterate* sense (Cesàro-mean) but generically **fail last-iterate convergence** for non-zero-sum games. No contraction metric exists for systems whose last iterates do not converge to an attractor.

    The three obstructions come from different theorem families (compositional-contraction / dissipativity-universality / differential-Lyapunov-attractor-theory) but converge on the same verdict: **contraction metrics cover the cooperative half of Section III** (`#der-team-persistence`, cooperative `#deriv-critical-mass-composition`, cooperative `#form-composition-closure`). The adversarial / strategic half belongs to `#deriv-strategic-composition` (equilibrium convergence via Monderer-Shapley / Rosen) and `#der-adversarial-destabilization` (asymmetric attacker-target dynamics). This is a scope boundary that AAD correctly honors, not a gap to be closed — the apparatus that handles adversarial regimes is equilibrium-theoretic, structurally different from Lyapunov-contraction machinery.

3. **State-dependent metric stochastic coupling.** Pham & Slotine 2007 extends contraction to stochastic systems under small-noise bounds; the Itô-correction $c_{\text{Itô}}$ in (CT-S) is manageable for state-independent or slow-varying metrics. Strongly state-dependent $M$ (adaptive-metric algorithms where $M$ is learned alongside $\xi$) introduces cross-coupling that can destabilize contraction — the same structural issue `#deriv-adaptive-gain-dynamics` handles with its (MG-4) meta-gain coupling-boundedness condition.

4. **Multi-basin dynamics.** Lohmiller-Slotine contraction is local-on-a-region. Agents with multiple basins of attraction admit only basin-local metrics, giving a basin-chart structure rather than a single global metric. The basin-crossing boundary is exactly the `#result-structural-adaptation-necessity` trigger; the metric formulation makes the basin structure explicit but does not escape it.

5. **Identifiability-floor intersection.** The metric formulation operates downstream of identification. It assumes the correction function $F$ points in a valid direction. Under the floors in `#disc-identifiability-floor` (on-policy L0-insufficiency no-go; L1' unobservable-$C$ Cramér-Rao floor; composition-layer Instance 3 Liberzon no-go), the correction direction is structurally unavailable. Contraction metrics cannot recover identification — the two architectural moves are orthogonal.

## Discussion

**Why factor this out.** The Euclidean sector inequality in `#result-sector-persistence-template` (T2) matches a quadratic Lyapunov in Euclidean norm. For several AAD-relevant agent classes, the natural Lyapunov lives in a non-Euclidean metric (Fisher for statistical-manifold learning; Mahalanobis for Kalman; Hessian-induced for strongly-convex optimization; Lyapunov-equation-determined for asymmetric-stable linear systems). Stating AAD's persistence machinery once in parameter-free metric-formulation form makes visible that the sector condition and the contraction-metric condition are two states of the same apparatus — Euclidean and non-Euclidean — with the specific metric instantiated per sub-scope entry.

**The compositional payoff.** The topology-indexed closures (CC-parallel / CC-cascade / CC-feedback) extend to heterogeneous-architecture composites via (CM2-M), closing the §6.1 heterogeneous-architecture obstruction in `#deriv-critical-mass-composition`. This is Section III's single largest coverage expansion: from "closed form for symmetric-matched-Tier-1" to "closed form under any of four topology classes with per-sub-agent (CT1)–(CT3) verification."

**Relationship to `#result-sector-persistence-template`.** The two segments coexist. `#result-sector-persistence-template`'s Euclidean formulation remains the default for agents whose natural coordinate is already Euclidean; `#result-contraction-template` is invoked when a non-Euclidean metric is natural (matrix Kalman, exp-family, ill-conditioned gradient, asymmetric-stable linear, PID-with-bounded-plant-nonlinearity). Every `#result-sector-persistence-template` invocation can be re-read as a `#result-contraction-template` invocation at $M = I$; the inverse mapping goes from metric to Euclidean with a $\kappa(M)$ degradation. Which direction is natural depends on the instance.

**Relationship to `#form-composition-closure`'s bridge lemma.** The bridge lemma's DA2'-inc condition is equivalent to (CT2) with $M = I$ on convex $C^1$ domains. `#result-contraction-template` therefore sharpens the bridge-lemma understanding: Tier 1 (DA2'-inc globally) ≡ metric-contracting-globally at $M = I$; Tier 2 (DA2'-inc locally with $\kappa(D\hat o)^2$ degradation) ≡ metric-contracting-locally with a specific local metric; Tier 3 (per-domain verification) ≡ no globally valid metric exists. The tier structure of the bridge lemma carries over to `#result-contraction-template` as Tier 1M / 2M / 3M respectively.

**Relationship to `#disc-identifiability-floor` Instance 3 (composition-layer no-go).** Instance 3's §3.3 construction uses matched-symmetric-Tier-1 scalar systems; the coupling-sign bit is unidentifiable from component marginals. Escape route (E-d) in that Instance names "shared metric structure (common contraction metric; Lohmiller-Slotine 1998)" as an adjacent machinery the no-go motivates; `#result-contraction-template` is the segment that machinery lives in. The Instance 3 escape is therefore operationalized by a `#result-contraction-template` invocation with a composite metric constructed from sub-agent metrics per the topology (parallel / cascade / feedback).

**Relationship to meta-patterns.**

- *`#disc-separability-pattern`:* metric-α₁ / metric-α₂ / metric-β is the seventh ladder (A2'-scope), closing the "binary special case" gap that segment's Discussion flagged. Separable-core (metric-α₁, Euclidean, AAD-internally derived via DA2'-inc ≡ (CT2)-M=I) / structured-repair (metric-α₂, non-Euclidean, derived under explicit conditions including (PI)/Čencov for Fisher-metric cases) / general-open (metric-β, metric formulation fails).
- *`#disc-identifiability-floor`:* orthogonal axis. Contraction metrics lift the *geometry-of-correction* half of sub-scope α; identifiability-floor operates on the *what-correction-to-make* half. The two architectural moves compose (Instance 3 at composition layer + metric-Tier structure at single-agent layer) but do not interact.
- *`#disc-additive-coordinate-forcing`:* the (PI)/Čencov axiom that grounds two of five metric-α₂ cases is the fourth primary instance of the meta-pattern, adding a Čencov-invariance machinery alongside the three Cauchy-FE instances. See that segment's Four Instances tables.

## Working Notes

- **Landing context.** The segment is the primary result of `msc/spike-contraction-metric-generalization.md` (2026-04-23 Gap A/B cycle). The Jacobian-level observation (DA2'-inc ≡ (CT2)-M=I) and the (PI)/Čencov observation derive from `msc/spike-jacobian-b1-strengthening.md` (2026-04-23 follow-up).

- **Heterogeneous general-graph composition.** Slotine 2003 §IV's virtual-system technique covers general directed graphs under a small-gain-along-every-cycle condition. Operationalizing this for `#form-composition-closure`'s general multi-agent setting — including identifying which cycle-gains to measure in practice — is a follow-up derivation. (CM2-M) in this segment handles 2-agent negative-feedback; $N \geq 3$ with general topology remains open but structurally clear.

- **Jacobian-level B1 strengthening is open.** The (CT2) condition on $F$'s Jacobian is a Jacobian-level B1 analog. Whether the integral B1 of `#der-gain-sector-bridge` can be *strengthened* to a Jacobian-level B1* that implies (CT2) AAD-internally (rather than via theorem-import from Lohmiller-Slotine) was attacked in `msc/spike-jacobian-b1-strengthening.md`. Three of the five metric-α₂ cases (Hessian, Lyapunov-linear-Hurwitz, Lyapunov-PID) remain theorem-imported after that spike; two (Fisher-metric-Kalman, Fisher-metric-exp-family) lift AAD-internally under (PI)/Čencov. The remaining gap is the three theorem-imported cases.

- **Candidate strong-option promotion.** Under a *heredity* axiom (composite admissibility derivable from sub-agent properties — a legitimate AAD-internal strengthening of `#post-composition-consistency`), agent-level B1* is forced, metric-Tier structure collapses, and (CM2-M) promotes from Slotine-imported to AAD-derived. Flagged in the Jacobian-level B1 spike's §11 strong option; promotion is an architectural decision requiring its own scoping.

- **Finsler metrics.** Forni & Sepulchre 2014 extends the differential Lyapunov framework to Finsler (direction-dependent) metrics. Likely useful only for highly anisotropic corrections (coordinate-asymmetric agents); not priority.

- **The (T2) / (CT2) structural observation matters for Section I too.** `#result-persistence-condition`'s linear special case ($F = \mathcal T \delta$, $\alpha = \mathcal T$, (T2) global) is trivially contraction-metric with $M = I$ and $\lambda = \alpha$. But non-linear `#result-persistence-condition` instances (nonlinear mismatch dynamics, gradient on strongly convex losses) would benefit from contraction-metric framing to remove the Euclidean-norm-specific condition-number penalty in the persistence constant. A cross-reference from `#result-persistence-condition` back to this segment may be warranted after the next promotion pass.
