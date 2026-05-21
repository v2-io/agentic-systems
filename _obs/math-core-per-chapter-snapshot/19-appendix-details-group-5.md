# Appendix — Details (group 5)


## Formulation: Resource Budget

- **Slug**: `form-resource-budget`
- **Type**: formulation
- **Status**: conditional
- **Stage**: draft
- **Depends**: `def-adaptive-tempo`, `def-strategy-dimension`

A depletable scalar reservoir whose drain rate rises with mismatch and whose level gates correction capacity — the minimal structure that makes "a degrading model is more expensive to run" a dynamical statement rather than an informal one.

AAT's core machinery is resource-blind: the policy $\pi(M_t, G_t)$ acts at no modeled cost, and correction capacity (tempo $\mathcal T$, #def-adaptive-tempo) does not deplete. #def-strategy-dimension records this as an explicit open scope item — for resource-constrained agents (embodied controllers under torque/battery/episode-length limits; teams under headcount; any agent whose every corrective action spends an exhaustible pool) the formalism carries no state for the pool and no coupling from model quality to its drain. This formulation introduces the minimal such structure.

*[Definition (resource-budget)]*

A scalar **resource budget** $\mathcal B_t \geq 0$ (calligraphic-scalar by the NOTATION convention exception, as for $\mathcal T$; distinct from the agent label $B$ of #der-adversarial-destabilization and from the strategy-edge set $E$). Its evolution:

$$\frac{d\mathcal B}{dt} \;=\; -\,c\big(\lVert\delta\rVert\big) \;+\; r_{\mathcal B}$$

where $\delta$ is the agent's mismatch ( #def-mismatch-signal), $c(\cdot)\geq 0$ is the **correction-cost rate**, and $r_{\mathcal B}\geq 0$ is the **replenishment rate**. The hard-budget regime is $r_{\mathcal B}=0$ (a finite pool that only depletes — a combat episode's battery, a fixed torque-integral, a bounded step count); the regenerative regime is $r_{\mathcal B}\gt 0$.

The formulation is fixed by two structural posits — introduced, not derived from existing AAT.

*[Assumption (A-cost: cost rises with mismatch)]*

$c$ is non-decreasing in $\lVert\delta\rVert$, with $c(0)\gt 0$ (running the loop at all costs something) and $c$ strictly increasing where $\lVert\delta\rVert\gt 0$. Minimal concrete form:

$$c\big(\lVert\delta\rVert\big) \;=\; c_0\big(1 + \beta_{\mathcal B}\,\lVert\delta\rVert\big), \qquad c_0\gt 0,\ \beta_{\mathcal B}\geq 0.$$

*Motivation, not derivation:* a model that is wrong by $\delta$ actuates partly in wrong directions — the agent pays for the corrective action *and* for the wasted component, and re-observes more often to recover. Degradation is literally more expensive to carry. $\beta_{\mathcal B}=0$ recovers the resource-blind special case (cost independent of model quality).

*[Assumption (A-gate: tempo is resource-gated)]*

The sector/correction rate the persistence machinery uses — $\alpha$ in #result-sector-persistence-template, equal to $\mathcal T$ in the canonical epistemic instantiation ( #def-adaptive-tempo, #result-persistence-condition) — is throttled by available resource:

$$\alpha(\mathcal B) \;=\; \alpha^{\max}\,\psi(\mathcal B), \qquad \psi:\mathbb{R}_{\geq 0}\to[0,1]\ \text{non-decreasing},\ \ \psi(0)=0,\ \ \psi(\mathcal B)\to 1\ \text{as}\ \mathcal B\to\infty.$$

*Motivation, not derivation:* with the pool exhausted the agent cannot run its observe–update–actuate loop at full rate (fewer sensor sweeps, slower control cycle, fewer remaining episode steps). $\psi\equiv 1$ recovers the resource-blind special case (constant $\alpha$, exactly today's template).

Together: $\mathcal B_t$ is the new state; (A-cost) couples model quality *into* its drain; (A-gate) couples its level *into* correction capacity. These two couplings are exactly what close the otherwise-open feedback in #der-adversarial-destabilization's Effects-Spiral corollary — the consequence is derived in #der-resource-bounded-destabilization.

---



## Derived: Resource-Bounded Destabilization

- **Slug**: `der-resource-bounded-destabilization`
- **Type**: derived
- **Status**: conditional
- **Stage**: draft
- **Depends**: `form-resource-budget`, `result-sector-persistence-template`, `der-adversarial-destabilization`, `schema-strategy-persistence`

A hard-budget agent self-depletes to certain finite-time destabilization against even a *constant*-effectiveness adversary — closing #der-adversarial-destabilization's Effects-Spiral not by formalizing its open coupling term but by making that term unnecessary, via the decaying-$\alpha$ instantiation of #result-sector-persistence-template.

#der-adversarial-destabilization's Effects-Spiral corollary ($\lVert\delta_B\rVert\uparrow \Rightarrow$ erratic action $\Rightarrow \gamma_A\uparrow \Rightarrow \rho_B\uparrow \Rightarrow \lVert\delta_B\rVert\uparrow$) is *discussion-grade* there because the link "degrading model $\Rightarrow$ stronger adversary coupling" requires specifying how model degradation feeds back into the dynamics, which that segment's machinery does not carry. The resource-budget formulation ( #form-resource-budget) supplies that feedback through a different and cleaner channel — the agent's *own* correction rate, not the adversary's coupling.

### Setup: the resource-coupled adversarial instantiation

Instantiate #result-sector-persistence-template with the target agent $B$'s mismatch as state variable, $\xi=\delta_B$, exactly as #der-adversarial-destabilization does, but with the sector parameter made resource-gated per #form-resource-budget (A-gate):

$$\frac{d\delta_B}{dt}=-\,\alpha_B(\mathcal B)\,\delta_B+w_B(t),\qquad \lVert w_B(t)\rVert\leq\rho_B^{\text{eff}}=\rho_{B,\text{base}}+\gamma_A\mathcal T_A,$$
$$\frac{d\mathcal B}{dt}=-\,c\big(\lVert\delta_B\rVert\big)+r_{\mathcal B},\qquad \alpha_B(\mathcal B)=\alpha_B^{\max}\,\psi(\mathcal B),$$

with $\rho_B^{\text{eff}}$ the coupling-amplified disturbance of #der-adversarial-destabilization (treated there, and here, with $\gamma_A,\mathcal T_A$ exogenous) and $c,\psi$ as posited in #form-resource-budget (A-cost),(A-gate). The novelty is the *coupled pair*: $\delta_B$ and $\mathcal B$ co-evolve, with model quality draining the budget and the budget gating correction.

### Regime split

*[Derived (resource-regime-split, from form-resource-budget + sector-persistence-template)]*

**Budget-sufficient regime.** If $\mathcal B_t$ stays large enough that $\psi(\mathcal B_t)\approx 1$ over the engagement (the pool is effectively infinite relative to the integrated cost), then $\alpha_B(\mathcal B_t)\approx\alpha_B^{\max}$ is constant and the system *is* #der-adversarial-destabilization's constant-$\alpha$ instantiation, unchanged. The resource structure adds nothing here. This is the honest boundary: the resource-blind special case ($\psi\equiv 1$) is exactly today's machinery, and it is correct there.

**Budget-scarce hard regime ($r_{\mathcal B}=0$).** With no replenishment, $d\mathcal B/dt=-c(\lVert\delta_B\rVert)\leq -c(0)\lt 0$ whenever correction runs, so $\mathcal B_t$ is strictly decreasing and reaches any level in finite time. Then $\alpha_B(\mathcal B_t)$ is a **time-varying, monotonically-decaying** sector parameter — exactly the structure #result-sector-persistence-template's Epistemic Status flags as requiring additional machinery, and the structure #schema-strategy-persistence already instantiates (there $\alpha_\Sigma=1/(n+1)$ decays with experience; persistence then requires the decay be counteracted faster than $\rho_\Sigma/R_\Sigma$). The resource-bounded case is the *same template slot* with budget-depletion in the role experience-accumulation plays for strategy persistence.

### The result

*[Derived (Conditional on A-cost, A-gate; hard regime $r_{\mathcal B}=0$)]*

Define the **critical budget** $\mathcal B_{\text{crit}}$ by the persistence boundary of #result-sector-persistence-template (Model D) at the coupling-amplified disturbance:

$$\alpha_B(\mathcal B_{\text{crit}})=\frac{\rho_B^{\text{eff}}}{R_B}\qquad\Longleftrightarrow\qquad \psi(\mathcal B_{\text{crit}})=\frac{\rho_B^{\text{eff}}}{\alpha_B^{\max}R_B},$$

and the destabilization **hitting time** $\tau=\inf\{t:\mathcal B_t=\mathcal B_{\text{crit}}\}$. Then, in the hard regime with correction ongoing:

1. **Certain finite-time destabilization.** $\mathcal B_t\downarrow$ strictly, so $\tau\lt\infty$ for any finite $\mathcal B_0$. Because $\psi(0)=0$, once $\mathcal B_t\lt\mathcal B_{\text{crit}}$ the persistence condition $\alpha_B(\mathcal B_t)\gt\rho_B^{\text{eff}}/R_B$ fails and #der-adversarial-destabilization's destabilization threshold is crossed. **The static persistence inequality holding at $t=0$ does not prevent this** — an agent that would persist forever at full budget ($\alpha_B^{\max}R_B\gt\rho_B^{\text{eff}}$) still destabilizes once the fuel drains the rate below threshold.

2. **The spiral, derived.** Substituting (A-cost), a mismatch excursion accelerates its own destabilization:
$$\lVert\delta_B\rVert\uparrow\;\Rightarrow\;c(\lVert\delta_B\rVert)\uparrow\;\Rightarrow\;\dot{\mathcal B}\ \text{more negative}\;\Rightarrow\;\alpha_B(\mathcal B)\downarrow\;\Rightarrow\;\big(\alpha_B R_B-\rho_B^{\text{eff}}\big)\downarrow\;\Rightarrow\;\lVert\delta_B\rVert\uparrow,$$
which brings $\tau$ forward: a transient noise burst in $w_B$ permanently advances the destabilization time. This is #der-adversarial-destabilization's Effects-Spiral, now a derived consequence of (A-cost)/(A-gate) rather than a discussion-grade schematic.

3. **The adversary's coupling need not grow.** The spiral closes through $\alpha_B$ *decaying* with $\gamma_A$ held **constant**. The Effects-Spiral's substantive content — collapse invisible to the static threshold — is captured *without* the unspecified $\gamma_A(\lVert\delta_B\rVert)$ leg #der-adversarial-destabilization could not formalize. Adversarial survival reduces to a **budget-versus-engagement-length race**: $B$ persists iff the engagement ends before $\tau$.

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Budget-sufficient regime ≡ constant-$\alpha$ template, unchanged | #result-sector-persistence-template (status `exact`), $\psi\equiv 1$ limit | Inherited exact |
| Resource-scarce case is the decaying-$\alpha$ template slot (the reduction) | #result-sector-persistence-template time-varying-$\alpha$ + #schema-strategy-persistence precedent | Derived, conditional on (A-cost),(A-gate) |
| Certain finite-time destabilization, $r_{\mathcal B}=0$ | Monotone-budget + Lyapunov persistence-boundary crossing | Derived (conditional) |
| Effects-Spiral as derived feedback; $\tau$ advanced by excursions | (A-cost) substituted into the depletion law | Derived (conditional) |
| Adversary coupling need not grow ($\gamma_A$ constant suffices) | Corollary of the above | Derived (conditional) |
| Orthogonal to — not a resolution of — the deferred symmetric joint-Jacobian problem | Comparison of which term carries the feedback ($\alpha_B$ vs $\gamma_A$) | Verified relationship |
| (A-cost), (A-gate) | #form-resource-budget | Introduced posits, not derived |
| Regenerative regime $r_{\mathcal B}\gt 0$ | — | Open (not attempted) |

---



## Result: Contraction Template

- **Slug**: `result-contraction-template`
- **Type**: result
- **Status**: conditional
- **Stage**: draft
- **Depends**: `result-sector-persistence-template`, `deriv-sector-condition`, `der-gain-sector-bridge`, `form-composition-closure`, `deriv-critical-mass-composition`, `disc-separability-pattern`

`#result-sector-persistence-template` states AAT's persistence arguments with a Euclidean sector condition (T2) matched to a quadratic Lyapunov in Euclidean norm. Generalizing the sector inequality to a **contraction-metric condition** (Lohmiller & Slotine 1998) preserves the template's ultimate-bound results while extending its coverage in three directions: (a) sub-scope α gains natural non-Euclidean metrics that remove condition-number penalties currently visible in #der-gain-sector-bridge; (b) two additional sub-scope β items (PID-bounded-plant; non-convex-within-basin) promote to derived sub-scope metric-α₂ under explicit conditions; (c) composition acquires **topology-indexed closure results** (parallel / hierarchical / small-gain-feedback) from Slotine 2003 that generalize `#deriv-critical-mass-composition`'s matched-symmetric-Tier-1 closed form to heterogeneous sub-agents. This segment states the generalization once in parameter-free form so that each lifting citation can reference it and specify only what varies.

`#result-sector-persistence-template` remains as the $M = I$ Euclidean specialization.

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

**Sub-scope metric-α₁ (Euclidean metric, AAT-internally derived via DA2'-inc ≡ (CT2) with M=I).** Scalar Kalman, Euclidean strongly-convex gradient, L2-regularized convex, linear-PD-symmetric. These cases carry (CT2) with $M = I$ which is exactly DA2'-inc — a condition `#form-composition-closure` has required at the composite level all along. AAT's existing commitment already forces (CT2)-Euclidean at these cases; the template surfaces it.

**Sub-scope metric-α₂ (non-Euclidean metric, derived under explicit conditions).** Five cases lift here:

- *Matrix Kalman under information metric* $M = (P^-)^{-1}$: contraction rate $\lambda = \lambda_{\min}(H^T R^{-1} H)/2$ on the observable subspace; Euclidean $\kappa(P^-)$ degradation removed. Under (PI)/Čencov (see `#der-gain-sector-bridge` "Fisher-metric cases under parameterization-invariance"), the information-metric form is *uniquely forced* — AAT-internally derived rather than theorem-imported.
- *Exponential-family natural parameters under Fisher metric* $M = \mathbf I(\theta)$: contraction rate $\lambda = \eta$ globally on the interior of the natural-parameter domain (Fisher-conditioning degradation removed). Also AAT-internally forced under (PI)/Čencov.
- *Hessian-metric strongly-convex* $M = \nabla^2 L$: contraction rate $\lambda = \eta$ under bounded metric-derivative in the drift direction. Theorem-imported (Hessian metric chosen to match loss curvature; no AAT-internal axiom forces the specific coordinate).
- *Linear-Hurwitz-non-symmetric under Lyapunov metric*: $M$ solves $M A + A^T M = -Q$ for $Q \succ 0$. Contraction rate $\lambda = \lambda_{\min}(Q)/(2\lambda_{\max}(M))$ in the $M$-metric. **New coverage:** asymmetric-stable linear corrections where Euclidean A2' fails. Theorem-imported (Lyapunov equation construction is standard; no AAT-internal axiom forces $Q$).
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

---



## Derivation: Variational Approximate-A2' (ε-Fidelity)

- **Slug**: `deriv-variational-sector-condition`
- **Type**: derivation
- **Status**: conditional
- **Stage**: draft
- **Depends**: `deriv-sector-condition`, `result-sector-persistence-template`, `der-gain-sector-bridge`, `form-strategy-complexity-cost`, `disc-compression-operations`

Variational / approximate-posterior agents (VI, amortized VI, active-inference-style variational free energy) currently sit in A2' sub-scope $\beta$ per `#form-sector-condition`: their correction functions target the *best-in-class* variational posterior $q^\ast$ rather than the true posterior $p$, and the approximation gap can rotate the correction direction enough to break B1 directional fidelity ( #der-gain-sector-bridge). Under a KL bound $\mathrm{KL}(q_\phi \Vert p) \leq \varepsilon$ on the variational approximation, directional fidelity recovers in a quantifiable form: **ε-fidelity B1**, with sector-constant degradation scaling as $O(\sqrt\varepsilon)$ (Pinsker-tight). The sector-persistence template applies under a Regime-A / Regime-B decomposition — clean sector bound on an annulus away from the projection-error floor, approximation-dominated on a ball of radius $\delta_0 = O(\sqrt\varepsilon)$ around the target. This promotes controlled-KL VI from sub-scope $\beta$ to a new intermediate tier $\alpha'$ within the A2' partition (cf. the α / α₁ / α₂ / β refinements from `#deriv-adaptive-gain-dynamics` and `#deriv-fisher-whitened-update-rule`).

### ε-fidelity B1

*[Derived (epsilon-fidelity-B1, from Pinsker + Cauchy-Schwarz)]*

Let the true posterior be $p(z \mid x)$ and the variational approximation $q_\phi(z \mid x)$ with $\mathrm{KL}(q_\phi \Vert p) \leq \varepsilon$. Under standard Lipschitz assumptions on the observation model and nested-support on the variational family, the total-variation distance bounds as $\lVert q_\phi - p\rVert_{TV} \leq \sqrt{\varepsilon/2}$ (Pinsker's inequality). Propagating this bound through the correction function via Cauchy-Schwarz:

$$(K\hat P - P^\ast)^T (\hat P - P^\ast) \geq (c_{\min} - C_H \sqrt{2\varepsilon}/\lVert\delta\rVert) \cdot \lVert\delta\rVert^2$$

where $C_H$ is a constant depending on the observation-model Lipschitz constant. The effective sector constant

$$c_\varepsilon(\lVert\delta\rVert) = c_{\min} - C_H\sqrt{2\varepsilon}/\lVert\delta\rVert$$

is state-dependent: large-mismatch regions see near-full sector constant; near-target regions see degraded sector constant due to approximation error dominating.

### Regime-A / Regime-B decomposition

*[Formulation (regime-decomposition-variational)]*

Define $\delta_0 = 2 C_H \sqrt{2\varepsilon}/c_{\min}$ (the approximation-dominated radius around target). Then:

- **Regime A — clean sector bound** ($\lVert\delta\rVert > 2\delta_0$). On the annulus $\mathcal B_R \setminus \mathcal B_{2\delta_0}$, $c_\varepsilon \geq c_{\min}/2$: sector condition holds with constant $c_{\min}/2$. The template's ultimate bound $\rho_\xi / (c_{\min}/2)$ applies.
- **Regime B — approximation-dominated floor** ($\lVert\delta\rVert \leq 2\delta_0$). Near target, $c_\varepsilon$ can be arbitrarily small; the correction may not contract. The ultimate bound gains an additive $O(\sqrt\varepsilon)$ term: $R^\ast_\varepsilon = \rho_\xi/(c_{\min}/2) + \delta_0 = \rho_\xi/(c_{\min}/2) + O(\sqrt\varepsilon)$.

Sector-persistence template instantiates with:
- State variable $\xi = \hat P - P^\ast$ (variational mismatch to target posterior).
- Effective ultimate bound $R^\ast_\varepsilon$ on Euclidean norm.
- Persistence requires $R^\ast_\varepsilon < R$, i.e., $\rho_\xi/(c_{\min}/2) + O(\sqrt\varepsilon) < R$.

Khasminskii stopping-time localization (same technique as `#deriv-sector-condition` Prop A.1S and the A2' strengthening spike) applies to the annulus Regime A; Regime B is handled by accepting $\delta_0$ as a projection-error floor.

### Per-case verdicts

*[Derived (per-variational-case)]*

The $\alpha'$-membership depends on the specific variational scheme:

**Natural-gradient VI with exponential-family $q_\phi$.** Khan & Lin 2017 (*Conjugate-computation variational inference*) showed natural-gradient VI is equivalent to closed-form conjugate-Bayesian updates for exponential-family variational distributions. This recovers *full* sub-scope $\alpha$ membership (not merely α'), with A2' derived rather than ε-degraded, by converting the variational update into a Bayesian update in a reparameterized family. The $\varepsilon = 0$ limit is exact.

**Mean-field VI.** When the true posterior is approximately factorized ($p(z) \approx \prod_i p_i(z_i)$), mean-field VI achieves small $\varepsilon$ and is the workhorse α' case. Ultimate bound degrades by additive $O(\sqrt\varepsilon)$; sector persistence holds.

**Amortized VI (VAE-style).** Amortization adds a second approximation error (the variational network's function-class limit). KL bounds compose *additively*: $\delta_0$ grows as $\sqrt{\varepsilon_{\text{family}} + \varepsilon_{\text{amort}} + \varepsilon_{\text{generalization}}}$. Under controlled-ε amortized VI, α' membership holds with a larger floor.

**Diffusion-posterior / energy-based with uncontrolled MCMC.** No controlled $\varepsilon$ bound; $\varepsilon$ grows with mixing time. Stays firmly in sub-scope $\beta$.

**Active inference (variational free energy).** Conditional α' under exponential-family $q$ + natural-gradient; ε-degraded α' otherwise. This does **not** force V-strong G-BP2 (presentation of AAT as control-theoretic specialization of active inference) — V-medium (KL-divergence-based cognitive cost) remains the appropriate scope commitment; the comparison trail is in the spike-routing cycle (CHANGELOG 2026-05-17).

### Sub-scope $\alpha'$ in the A2' partition

*[Derived (alpha-prime-partition)]*

The A2' sub-scope partition is structured as:

- **Sub-scope α** (derived under B1 directional fidelity; `#der-gain-sector-bridge`): Kalman, conjugate Bayesian, exponential-family natural parameters, strongly-convex gradient, L2-regularized, linear-PD-symmetric.
- **Sub-scope α₁/α₂** (`#result-contraction-template`): metric-formulation generalization of α.
- **Sub-scope α₃** (`#deriv-fisher-whitened-update-rule`): correlated evidence + Fisher-whitened under (PI)/Čencov.
- **Sub-scope α'** (this segment): controlled-KL VI under Pinsker's inequality with $O(\sqrt\varepsilon)$ sector-constant degradation + Regime-A/B decomposition.
- **Sub-scope β**: uncontrolled-ε agents; non-smooth rule-based; severely misspecified; per-step SGD; human judgment.

This gives the full current picture: {α, α₁, α₂, α₃, α', β}.

---



## Derivation: L1' Update-Bias Formula

- **Slug**: `deriv-l1-update-bias`
- **Type**: derivation
- **Status**: conditional
- **Stage**: draft
- **Depends**: `disc-credit-assignment-boundary`, `deriv-edge-update-natural-parameter`, `deriv-edge-credence-dynamics`, `disc-identifiability-floor`, `schema-strategy-persistence`

Under L1' correlated-evidence regimes with unobservable common cause, the default log-odds edge-update ( #deriv-edge-update-natural-parameter) converges to a **biased fixed point** — edges settle at log-odds values that match the L1' root-probability rather than the marginal-edge truth. This segment derives a closed-form bias formula for the two-edge OR-root case, verifies it via Monte Carlo, and composes it with `#disc-identifiability-floor` Instance 2 and `#schema-strategy-persistence`'s forgetting prerequisite to produce a **dual forgetting-rate requirement** on strategic persistence.

The bias is the quantitative companion to F13's structural-identifiability-floor result: F13 shows identification is *structurally impossible* from single-channel observation; this segment shows the resulting *magnitude drift* is bounded, Lipschitz in correlation strength $\rho$, and Cramér-Rao-floored under forgetting.

### Closed-form bias at matched-marginal initial conditions (two-edge OR-root)

*[Derived (L1-bias-formula-OR-root)]*

Let root node $G$ have two direct causal parents $e_1, e_2$ via OR-aggregation under L1' with latent common cause $C$ producing correlation $\rho$ between the parent edges. Assume matched-marginal initial conditions: $\hat\mu_j^{\text{init}} = \mu_j^\ast$ for each edge's marginal probability. Under the default log-odds update with per-edge gain $\eta_{\text{edge}} = 1/(n_k+1)$ and identifiability coefficient $\iota_k$, the per-cycle bias on edge $k$'s log-odds update satisfies

$$B_k(\rho) = -\frac{\iota_k \cdot (1 - \mu_{\bar k}) \cdot \rho}{(n_k + 1) \cdot \left[(1 - \mu_1)^2 + (1 - \mu_2)^2\right]}$$

where $\bar k \in \{1, 2\} \setminus \{k\}$ is the sibling edge. The bias is linear in $\rho$, decays as $1/(n_k+1)$ with experience, topologically asymmetric via the Jacobian factor $(1 - \mu_{\bar k})/\lVert\mathbf J\rVert^2$.

**Admissible region (precise).** The denominator is the squared OR-aggregation Jacobian norm $\lVert\mathbf J\rVert^2 = (1 - \mu_1)^2 + (1 - \mu_2)^2$. The first-order perturbation is well-posed precisely when $\lVert\mathbf J\rVert$ is bounded below by some fixed $\epsilon_J > 0$ — equivalently, when at least one edge probability is bounded away from $1$. This is the **Jacobian-norm admissibility condition** $\lVert\mathbf J\rVert \ge \epsilon_J$; it is *weaker* than requiring both $\mu_1, \mu_2$ to be bounded away from $1$, and it is *sharper* than the qualitative "bounded away from determinism" reading: only the joint deterministic-success corner $\mu_1, \mu_2 \to 1$ together is excluded. As either edge alone approaches deterministic success the bias formula remains valid (the surviving sibling edge carries the Jacobian norm); only the diagonal corner where both edges saturate is excluded, and there the per-cycle update itself vanishes (observations carry no residual information), so "no learning, no bias" is the operationally correct behaviour and the formula's apparent singularity is degenerate rather than physical. Inside the admissible region $\lVert\mathbf J\rVert \ge \epsilon_J$, the closed-form predictions are quantitatively verified by Monte Carlo; at the diagonal corner the segment defers to `#deriv-edge-credence-dynamics`'s degenerate-update analysis. The Jacobian-norm condition is the natural admissibility statement because the bias formula is the projection of the update onto $\mathbf J / \lVert\mathbf J\rVert^2$, so well-posedness requires only that this projection be defined.

For AND-root aggregation, the bias has the same structural form with opposite sign. For mixed OR-AND sub-plans, the bias decomposes sub-plan-wise.

### L1'-induced biased fixed point

*[Derived (biased-fixed-point-exists)]*

Under continued L1' evidence, the log-odds fixed point satisfies

$$\lambda_k^{\text{L1'-FP}} = \lambda_k^\ast + \int_0^\infty e^{-\eta_{\text{edge}} \iota_k t} B_k(\rho)\, dt = \lambda_k^\ast - \rho \cdot (1 - \mu_{\bar k})/\left[(1 - \mu_1)^2 + (1 - \mu_2)^2\right]$$

(for constant-$\iota$ approximation). Each edge's log-odds converges to a **wrong value** that matches the L1' root probability rather than the marginal truth. **Plan-level correctness is purchased at edge-level miscalibration**: the agent predicts plan outcomes correctly on-policy (the L1' mixture on the sibling matches the L1' marginal), but its per-edge credences are systematically biased.

This is the quantitative companion to F1's on-policy undetectability (`#disc-identifiability-floor` Instance 1) at the marginal level: the bias accumulates at rate $1/(n_k+1)$, converges to a bounded non-zero value, and is *not detectable from on-policy data* because the mixture's marginal is matched to the on-policy observations.

### Observable-$C$ zero-bias result

*[Derived (observable-C-zero-bias)]*

Under Prop B.7's five-way-gating with $C$ observable, conditioning on $C$ decomposes the L1' mixture into two single-child-per-component problems:

$$B_k(\rho \mid C = c) = 0 \quad \text{in expectation at conditional truth, for each } c \in \{0, 1\}.$$

Prop B.7's decomposition *exactly eliminates the bias* — the five gating conditions (facilitator monotonicity; $C$-observability; $\iota > 0$ for common-cause edge; marginal sector condition; identifiability of per-component rates) are precisely the conditions under which conditional-on-$C$ updates restore exactness. This makes Prop B.7's derivation the quantitative escape from the L1' bias.

### Unobservable-$C$ Cramér-Rao bias floor under forgetting

*[Derived (bias-floor-under-forgetting)]*

When $C$ is unobservable and the agent uses experience discounting at rate $\lambda \in [0, 1)$ to maintain plasticity (`#schema-strategy-persistence`'s forgetting prerequisite), the steady-state bias is

$$B_k^{\text{SS}}(\rho, \lambda) = -\frac{\iota_k \cdot \rho \cdot (1 - \mu_{\bar k})}{(1 - \lambda) \cdot \left[(1 - \mu_1)^2 + (1 - \mu_2)^2\right]}.$$

The Cramér-Rao floor from `#disc-identifiability-floor` Instance 2's rank-1 Fisher matrix translates directly: no unbiased estimator can reduce the bias below $\rho / (1 - \lambda) \cdot [\text{constant}]$. The bias is structurally present in any online estimator operating on single-channel observation of one child edge, not merely the specific default-signal estimator.

### Dual forgetting-rate requirement

*[Derived (dual-forgetting-requirement)]*

`#schema-strategy-persistence` requires forgetting rate $(1 - \lambda) > \rho_\Sigma / R_\Sigma$ for asymptotic sector-persistence. The L1' bias floor above imposes a **second** constraint: to keep the bias bounded relative to the sector reserve,

$$(1 - \lambda) > c_B \cdot \rho / R_\Sigma^{\text{bias}}$$

where $c_B$ is a topology-dependent constant from the Jacobian factor and $R_\Sigma^{\text{bias}}$ is the tolerable bias-reserve within the sector region. The forgetting rate must satisfy **both**:

$$(1 - \lambda) > \max\left(\frac{\rho_\Sigma}{R_\Sigma},\; \frac{c_B \cdot \rho}{R_\Sigma^{\text{bias}}}\right).$$

**When the admissibility window is empty** (no forgetting rate satisfies both constraints simultaneously), no standard persistence regime works — the agent must augment (observable-$C$ via instrumented regime indicators; multi-child joint observation; plan-level fallback) or accept biased-fixed-point operation.

### Monte Carlo verification

*[Empirical claim (monte-carlo-confirmation)]*

Numerical simulation (400 trials × 5000 cycles, four scenarios: OR-cooperative, OR-adversarial, AND-cooperative, AND-adversarial) confirms the closed-form predictions:
- Sign of bias matches theoretical prediction in all scenarios.
- Magnitude matches closed form within $< 5\%$ at $\rho \in \{0.1, 0.3, 0.5, 0.7, 0.9\}$.
- Vanishing at $\rho = 0$ verified.
- Jacobian-induced topological asymmetry verified: OR and AND roots produce opposite-sign biases of matching magnitude.
- Initial-cycle rate $dB_k/dt \mid_{t=0}$ matches closed form quantitatively.
- Logarithmic cumulative drift matches (biased-fixed-point convergence rate).

Full simulation parameters and results in `spikes/spike-l1-update-bias.md` §7.

---
