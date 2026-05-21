---
slug: result-sector-condition-stability
type: result
status: exact
depends:
  - def-adaptive-tempo
  - def-mismatch-signal
  - deriv-sector-condition
  - result-sector-persistence-template
stage: claims-verified
---

# Result: Sector Condition Stability

The framework's first major *Lyapunov result*, stated as a specific instantiation of a more general sector-persistence template ( #result-sector-persistence-template) whose abstract form lives in the appendices. The mismatch dynamics are taken in their general nonlinear form: mismatch changes at rate (correction function applied to mismatch) plus (environmental disturbance). The correction function is required only to satisfy the **local sector condition** — that its inner product with the mismatch is at least $\alpha$ times the mismatch's squared magnitude, within a radius-$R$ region where it remains valid. The sector condition is what generalizes the linear ODE: it captures the qualitative essence of correction (the function points inward with at least baseline efficiency) without committing to a specific functional form like linear, saturating, sigmoid, threshold, or PID. Saturation, thresholding, and basin boundaries all live under one Lyapunov argument.

Under this sector condition plus bounded disturbance, the chapter's headline persistence inequality is *derived*: the agent persists if and only if $\alpha \gt \rho/R$. When the inequality holds, the mismatch is ultimately bounded by $R^\ast = \rho/\alpha$, and the "adaptive reserve" — the additional disturbance the agent can absorb before mismatch reaches the edge of the valid region — is $\alpha R - \rho$.

Under **Model S** (stochastic disturbance), the analog is sharper and qualitatively different: the steady-state root-mean-square mismatch scales as $\sigma_w\sqrt{n/(2\alpha)}$ — the square root of the disturbance-to-correction ratio. Model D scales as $1/\alpha$, Model S as $1/\sqrt{\alpha}$: **correction is less effective against noise than against drift**. This is one of the volume's striking results, separating two genuinely different physics of adaptation under deterministic vs stochastic environments.

The linear ODE from Chapter 3 ( #hyp-mismatch-dynamics) is recovered as the special case where the sector condition holds globally with $\alpha = \mathcal{T}$. The general sector-condition framework proves the persistence threshold is a *structural necessity of any bounded-correction system* — not an artifact of the linear approximation. The result is also where the structural-adaptation-necessity result will be anchored: when disturbance exceeds the model class's capacity (i.e., $\rho/\alpha \gt R$), the sector condition fails. This *is* the dynamical trigger for needing a new model class with larger valid radius or better efficiency — which #result-structural-adaptation-necessity treats formally a few segments later.

## Formal Expression

This segment is the **single-agent epistemic instantiation** of the sector-persistence template ( #result-sector-persistence-template). The template's state variable is $\xi = \delta(t) \in \mathbb{R}^n$ (model-reality mismatch); the correction function is $F(\mathcal{T}, \delta)$; the disturbance is environmental ($w(t)$); the region of validity $R$ is the model class capacity.

*[Formulation]*

$$\frac{d\delta}{dt} = -F(\mathcal{T}, \delta) + w(t)$$

*[Assumption (sector-condition)]*

$F$ satisfies the local sector condition (template condition (T2)) for $\lVert\delta\rVert \leq R$:

$$\delta^T F(\mathcal{T}, \delta) \geq \alpha \lVert\delta\rVert^2$$

with $\alpha \gt 0$. Disturbance is bounded: $\lVert w(t)\rVert \leq \rho$ (Model D, GA-2) or $\mathbb{E}[\lVert w(t)\rVert^2] = \sigma_w^2$ (Model S, GA-2S). Grounding of (T2) for gain-based agents: #der-gain-sector-bridge gives $\alpha = \eta^\ast \cdot c_{\min}$. The linear case $F = \mathcal{T} \cdot \delta$ yields $\alpha = \mathcal{T}$ exactly.

*[Derived (from sector-persistence-template)]*

The template's Model D conclusion specializes to: $\delta(t)$ is ultimately bounded by $R^\ast = \rho/\alpha$, and the agent persists iff

$$\alpha \gt \frac{\rho}{R}.$$

The adaptive reserve is $\Delta\rho^\ast = \alpha R - \rho$ — the additional disturbance the agent can absorb before $R^\ast$ exceeds the valid region.

The template's Model S conclusion specializes to: the steady-state RMS mismatch is $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)}$ (where $n = \dim(\delta)$), and mean-square persistence requires $\alpha \gt n\sigma_w^2/(2R^2)$. Model D scales as $1/\alpha$; Model S scales as $1/\sqrt{\alpha}$ — correction is less effective against noise than against drift.

Full Lyapunov proofs: #deriv-sector-condition Props A.1, A.1S, A.2.

## Epistemic Status

*Exact.* Both results are direct instances of the sector-persistence template applied to the single-agent epistemic case. Template precondition (T1) is satisfied because no correction should be applied at zero mismatch; (T2) reduces to the local sector condition above and is grounded structurally by #der-gain-sector-bridge for gain-based agents; (T3) is the disturbance-model choice (D or S), a domain question. The linear ODE of #hyp-mismatch-dynamics is the special case where (T2) holds globally with $\alpha = \mathcal{T}$; the sector framework generalizes this to saturating, thresholded, and structurally-limited correction functions under the same persistence condition. Disturbance-model choice is a domain question, not a theory question.

## Discussion

**Why the sector condition.** The linear ODE assumes correction scales linearly with mismatch forever. Real adaptive systems saturate, exhibit thresholding, or break down when the model class is exhausted. The sector condition captures the minimal structural requirement: the correction must point in the right direction with at least baseline efficiency $\alpha$.

**Generalizing the persistence threshold.** In the linear case, $\alpha = \mathcal{T}$ (adaptive tempo). The general result $\alpha \gt \rho/R$ proves the persistence threshold ( #result-persistence-condition) is a structural necessity of any bounded-correction system, not an artifact of the linear approximation. This result addresses *structural persistence* — the machinery's capacity to bound mismatch — not operational persistence (current proximity to $R$) or continuity persistence (identity through time). See Persistence in `LEXICON.md` for the full disambiguation.

**Connection to structural adaptation.** When $\rho/\alpha \gt R$, disturbance exceeds the model class's capacity. The sector condition fails — this is the dynamical trigger for structural adaptation ( #result-structural-adaptation-necessity), requiring a new model class with larger valid radius $R'$ or better efficiency $\alpha'$.
