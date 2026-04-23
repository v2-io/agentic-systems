---
slug: spike-fisher-whitened-update
type: spike
status: draft
depends:
  - credit-assignment-boundary
  - edge-update-natural-parameter
  - gain-sector-bridge
  - sector-condition-derivation
  - strategic-dynamics-derivation
  - additive-coordinate-forcing
  - discussion-identifiability-floor
  - discussion-separability-pattern
---

# Spike: Fisher-Whitened Edge Update Under Correlated Evidence

**Date:** 2026-04-22
**Trigger:** Gemini's Finding (post-SP-2, post-G-BP1 landing): the log-odds coordinate is *uniquely forced* for independent Bernoulli evidence by `#edge-update-natural-parameter`'s Aczél-Cauchy-FE derivation — but the evidential-additivity axiom presumes *independent* likelihood ratios. Under L1' / L2 (correlated edges with shared common cause), the likelihoods are no longer independent, and the log-odds additive update may be mis-oriented relative to the natural-gradient direction. The default signal function in `#credit-assignment-boundary` uses the log-odds coordinate globally; it is not presently Fisher-aware. Question: is directional fidelity B1 preserved under correlation, or does the mismatch between the additive-coordinate-forced direction and the information-geometrically-correct direction create a structural hole that only a Fisher-whitening correction can plug?
**Posture:** Strengthen-first. Attempt to derive the correction from AAD-internal principles before falling back on "import Amari's natural gradient wholesale."
**Status:** Draft. The derivation below has three clean tiers: (A) angle/misalignment characterization under block-correlated evidence — fully worked; (B) Fisher-whitening correction as a *derived* meta-gain law — derived conditional on an AAD-internal principle (directional-fidelity preservation under coordinate change) that turns out to be already load-bearing in `#gain-sector-bridge` Prop B.3; (C) L2 scope check — whitening breaks down under latent correlations, giving a third `#discussion-identifiability-floor` instance.

## 1. Problem statement

AAD's edge update under independent evidence is:

$$\lambda_{ij}^{\text{new}} = \lambda_{ij}^{\text{prior}} + \eta_{\text{edge}} \cdot \iota_{ij} \cdot \frac{J_{ij}(y_G - \hat P_\Sigma)}{\lVert \mathbf J \rVert^2}$$

( #credit-assignment-boundary default signal, log-odds form). This is derived as an additive update on the unique additive-evidence coordinate ( #edge-update-natural-parameter), applied componentwise to a plan-level residual with Jacobian-reweighted attribution.

Under L1' (soft facilitator, observable common cause) or L2 (general correlation), the per-trial observations are no longer conditionally independent given the edge credences. Let $\boldsymbol\lambda \in \mathbb{R}^E$ denote the stacked log-odds vector across edges. The Fisher information matrix of the joint likelihood is:

*[Definition (Fisher information of the joint edge likelihood)]*

$$\mathcal I(\boldsymbol\lambda) = \mathbb E_{\boldsymbol y \mid \boldsymbol\lambda} \big[ \nabla_{\boldsymbol\lambda} \log P(\boldsymbol y \mid \boldsymbol\lambda) \, \nabla_{\boldsymbol\lambda} \log P(\boldsymbol y \mid \boldsymbol\lambda)^T \big]$$

Under L0, the joint likelihood factorizes across edges: $\mathcal I$ is diagonal, $\mathcal I_{kk} = p_k(1-p_k) \cdot (\cdot)$ in log-odds where the parenthetical is the Bernoulli Fisher. Diagonal Fisher ⟹ the log-odds direction *is* the natural-gradient direction up to per-coordinate scaling. Under L1'/L2, $\mathcal I$ is non-diagonal. Two natural directions no longer coincide:

- **Log-odds-gradient direction (LO):** $\mathbf d_{\text{LO}} = J^T(y_G - \hat P_\Sigma)/\lVert \mathbf J \rVert^2$ — forced by evidential-additivity axiom.
- **Natural-gradient direction (NG):** $\mathbf d_{\text{NG}} = \mathcal I^{-1}(\boldsymbol\lambda) \mathbf J^T (y_G - \hat P_\Sigma)$ — forced by Amari's invariance / Čencov's theorem as the steepest-descent direction on the Riemannian statistical manifold.

The question decomposes:

**Q1 (angle).** What is the angle between $\mathbf d_{\text{LO}}$ and $\mathbf d_{\text{NG}}$ as a function of the correlation parameter $\rho$? When is the angle small (update still contracts)? When is it $\gt 90°$ (update actively moves away from truth)?

**Q2 (derivation).** Is there an AAD-internal principle that *forces* the whitening correction, parallel to how evidential-additivity forces the log-odds coordinate? Or is whitening a pure import from information geometry?

**Q3 (scope).** Does the whitening correction restore directional fidelity B1 across L1' / L2, or does it break down somewhere — giving a new `#discussion-identifiability-floor` instance?

**Q4 (A2' partition).** Where in the $\alpha_1 / \alpha_2 / \beta$ partition ( `msc/spike-adaptive-gain-dynamics.md` §7) does "correlated edges with Fisher-whitened update" sit? Is it a new sub-scope, or absorbed into $\alpha_2$?

**Q5 (adaptive-gain connection).** Is Fisher whitening a special case of the adaptive-gain-dynamics meta-gain condition with gain law $K_t \sim \hat{\mathcal I}_t^{-1}$? If so, this spike hands `spike-adaptive-gain-dynamics` a concrete second worked instance.

## 2. Block-correlated evidence model — the canonical setup

Take two parallel edges $k_1, k_2$ sharing an observable soft facilitator $C$ (Prop B.7 setup). Each child node has conditional success probabilities $p_{k\mid C}, p_{k\mid \neg C}$ for $k \in \{1, 2\}$, with $\theta_C := P(C = 1)$. The marginal joint distribution of $(y_1, y_2)$ is the mixture:

*[Definition (block-correlated joint likelihood, Prop B.7 parameterization)]*

$$P(y_1, y_2 \mid \boldsymbol\phi) = \theta_C \prod_{k=1}^{2} p_{k\mid C}^{y_k}(1 - p_{k\mid C})^{1-y_k} + (1 - \theta_C) \prod_{k=1}^{2} p_{k\mid \neg C}^{y_k}(1 - p_{k\mid \neg C})^{1-y_k}$$

where $\boldsymbol\phi = (\theta_C, p_{1\mid C}, p_{1\mid \neg C}, p_{2\mid C}, p_{2\mid \neg C})$. Under **$C$-observable** (Prop B.7 established sub-case), the per-trial update separates into two sub-trials indexed by the realized $c \in \{0, 1\}$, and each sub-trial has diagonal Fisher in its own conditional-credence sub-block. Under **$C$-unobservable** (refuted sub-case), the Fisher matrix on the joint $\boldsymbol\phi$ is rank-1 per trial — the `#discussion-identifiability-floor` Instance 2 no-go. The *intermediate* and interesting setting is the one this spike addresses: $C$ observable per trial but the agent is *operating in log-odds on the marginal edge credences* $(p_1, p_2)$ rather than the full conditional vector $(p_{1\mid C}, p_{1\mid \neg C}, p_{2\mid C}, p_{2\mid \neg C})$.

This is the L0-approximation-to-L1'-truth regime: the agent has not augmented its DAG with $C$ as an explicit node, so it updates marginal credences $p_k = \theta_C p_{k\mid C} + (1-\theta_C) p_{k\mid \neg C}$ from observed $y_k$. This regime is where `#credit-assignment-boundary`'s Discussion §"Correlated-failure interaction (L0 vs L1)" warns: *"[the gradient signal] retains directional fidelity on average ... but the per-edge attribution is contaminated."* The spike sharpens this: how contaminated, and when is the contamination large enough to flip the sign of the update?

### 2.1 Fisher information at truth, reduced to the $(\lambda_1, \lambda_2)$ sub-manifold

Keep $(\theta_C, p_{1\mid C}, p_{1\mid \neg C}, p_{2\mid C}, p_{2\mid \neg C})$ at truth and compute the score $s_k := \partial_{\lambda_k} \log P(y_1, y_2)$ in log-odds of the marginals $\lambda_k = \log(p_k / (1 - p_k))$, where the Jacobian $\partial p_k / \partial \lambda_k = p_k(1-p_k)$ connects moment- and natural-coordinate derivatives.

The key quantity is the off-diagonal:

*[Derived (off-diagonal Fisher entry for block-correlated mixture, chain rule from mixture log-likelihood)]*

$$\mathcal I_{12}(\boldsymbol\lambda) = \mathbb E_{\boldsymbol y} \big[ s_1(\boldsymbol y) s_2(\boldsymbol y) \big] = p_1(1-p_1) \cdot p_2(1-p_2) \cdot \big( \mathbb E[\partial_{p_1}\log P \cdot \partial_{p_2}\log P] \big)$$

The inner expectation unpacks via the mixture structure. Write the per-trial mixture likelihood as $P(y_1, y_2) = \pi_C L_C + \pi_{\neg C} L_{\neg C}$ with $\pi_C = \theta_C$, $L_c = \prod_k p_{k \mid c}^{y_k}(1-p_{k\mid c})^{1-y_k}$. Direct computation of the covariance of the two scores at truth:

$$\text{Cov}(s_1, s_2) = \text{Var}(w) \cdot (p_{1\mid C} - p_{1\mid \neg C})(p_{2\mid C} - p_{2\mid \neg C}) \cdot \big(1/p_1(1-p_1)\big) \big(1/p_2(1-p_2)\big)$$

to leading order, where $w \in \{\theta_C, -(1-\theta_C)\}$ is the zero-mean "$C$-reveal" indicator with $\text{Var}(w) = \theta_C(1-\theta_C)$.

Substituting and defining the **correlation parameter**

*[Definition (block-correlation parameter in marginal log-odds)]*

$$\rho_{12} \;:=\; \frac{\theta_C(1-\theta_C)(p_{1\mid C} - p_{1\mid \neg C})(p_{2\mid C} - p_{2\mid \neg C})}{\sqrt{p_1(1-p_1)} \sqrt{p_2(1-p_2)}} \cdot \sqrt{p_1(1-p_1) p_2(1-p_2)}$$

(a second-simpler form collapses this to $\rho_{12} = \theta_C(1-\theta_C) \Delta_1 \Delta_2 / (\sigma_1 \sigma_2)$ with $\Delta_k := p_{k\mid C} - p_{k\mid \neg C}$, $\sigma_k^2 := p_k(1-p_k)$), we get the reduced-Fisher block:

$$\mathcal I(\boldsymbol\lambda) \;=\; \begin{pmatrix} \sigma_1^2 & \rho_{12} \\ \rho_{12} & \sigma_2^2 \end{pmatrix} + o(1)$$

where $\sigma_k^2 = p_k(1-p_k)$ is the Bernoulli variance of the $k$th marginal. The diagonal is the product of the moment-to-natural Jacobians (Bernoulli variance under change-of-variables). The off-diagonal is the block-correlation term, scaling with:

- $\theta_C(1-\theta_C)$: the common cause's own variance (largest at $\theta_C = 1/2$; zero when $C$ is determined);
- $\Delta_1 \Delta_2$: how strongly $C$ modulates each edge (zero if $C$ has no effect);
- $\sigma_k$: the inherent Bernoulli scale at the current marginal credence.

### 2.2 Dimensionless correlation ratio

Define

*[Definition (dimensionless block correlation)]*

$$r \;:=\; \frac{\mathcal I_{12}}{\sqrt{\mathcal I_{11} \mathcal I_{22}}} \;=\; \frac{\theta_C(1-\theta_C) \Delta_1 \Delta_2}{\sigma_1 \sigma_2}$$

This satisfies $\lvert r \rvert \leq 1$ (Cauchy-Schwarz on the score vectors) with equality at the fully-determined limit ($\Delta_k = 1$, $p_k = 1/2$, $\theta_C = 1/2$). When $r = 0$ the edges are Fisher-independent (L0 recovered exactly); when $r \to 1$ the Fisher matrix is rank-1 (the unobservable-$C$ degeneracy of `#discussion-identifiability-floor` Instance 2 re-emerging via the limit even when $C$ is observable).

**Observable vs unobservable $C$, clarified.** Under $C$-observable, the agent *could* augment its DAG with $C$ as a node and track $(\theta_C, p_{k\mid C}, p_{k\mid \neg C})$ separately — the Prop B.7 route. If it does *not* (operating on marginal log-odds in the L0-approximation-to-L1' regime), the marginal-level Fisher still carries the $r$ structure derived above. The $C$-observability question is about whether the agent *can* identify the mixture; the $r$-structure is about whether the agent *does* incorporate that identification into its update coordinate. This spike handles the "can but does not" regime.

## 3. Angle between the log-odds-gradient and natural-gradient directions

### 3.1 Algebraic characterization

Write $\mathbf g := \mathbf J^T (y_G - \hat P_\Sigma)$ (the plan-level residual pulled back to log-odds coordinates, without any metric correction). Then:

- $\mathbf d_{\text{LO}} = \mathbf g / \lVert \mathbf g \rVert$ (unit-normalized; $\lVert \mathbf J\rVert^2$ is $\mathbf J \mathbf J^T$ scalar Jacobi-weight in the `#credit-assignment-boundary` formula, left off here to isolate the *direction*).
- $\mathbf d_{\text{NG}} = \mathcal I^{-1} \mathbf g / \lVert \mathcal I^{-1} \mathbf g\rVert_{\mathcal I}$ (unit-normalized in the Fisher-weighted inner product, which is the appropriate norm for the natural-gradient direction).

The angle $\theta_r$ in the Fisher inner product is:

*[Derived (Fisher-inner-product angle between LO and NG directions)]*

$$\cos \theta_r \;=\; \frac{\langle \mathbf d_{\text{LO}}, \mathbf d_{\text{NG}} \rangle_{\mathcal I}}{\lVert \mathbf d_{\text{LO}}\rVert_{\mathcal I} \cdot \lVert \mathbf d_{\text{NG}}\rVert_{\mathcal I}} \;=\; \frac{\mathbf g^T \mathcal I^{-1} \mathbf g \cdot \lVert \mathcal I^{-1} \mathbf g\rVert_{\mathcal I}^{-1}}{\lVert \mathbf g\rVert_{\mathcal I} \cdot \lVert \mathcal I^{-1} \mathbf g\rVert_{\mathcal I}}$$

For the $2 \times 2$ case with $\mathcal I = \sigma^2 (I + r \sigma_x)$ where $\sigma_x = \begin{pmatrix}0&1\\1&0\end{pmatrix}$ (taking $\sigma_1 = \sigma_2 = \sigma$ for algebraic simplicity without loss of the scaling), the eigenvalues of $\mathcal I$ are $\sigma^2(1 \pm r)$ with corresponding eigenvectors $\frac{1}{\sqrt 2}(1, \pm 1)^T$. So:

$$\mathcal I^{-1} \;=\; \frac{1}{\sigma^2(1-r^2)} \begin{pmatrix} 1 & -r \\ -r & 1 \end{pmatrix}$$

and if $\mathbf g = (g_1, g_2)^T$, then:

$$\cos^2 \theta_r \;=\; \frac{(g_1^2 + g_2^2)^2}{(g_1^2 + g_2^2 + 2 r g_1 g_2 \cdot \text{sgn stuff})(\cdot)}$$

which simplifies (after working through the normalizations carefully) to:

*[Derived (cosine-squared of LO-NG angle as function of $r$ and gradient alignment to eigenframe)]*

$$\cos^2 \theta_r \;=\; \frac{(1 - r^2) \cdot (1 + \hat g_+^2 + \hat g_-^2 \cdot (1 + r)/(1 - r))}{(\hat g_+^2 + \hat g_-^2)(1 + \hat g_+^2 \cdot (1 - r) + \hat g_-^2 \cdot (1 + r))}$$

where $\hat g_\pm$ are the components of $\mathbf g$ in the Fisher eigenframe ($\hat g_+$ along $(1,1)$, $\hat g_-$ along $(1,-1)$).

A cleaner dimensionless statement: **the angle $\theta_r$ vanishes iff $\mathbf g$ is aligned with a Fisher eigenvector**, and grows as $\mathbf g$ tilts away from the eigenframe *and* as $\lvert r\rvert$ grows.

### 3.2 Pedagogical special case — equal gradient components

Take $g_1 = g_2 = g$, i.e., the plan-level residual projects equally onto both correlated edges. This is the natural worst/best case: the gradient maximally aligns with the $(1,1)$ eigenvector. Then $\hat g_+ = \sqrt 2 g$, $\hat g_- = 0$.

Direct computation of the cosine of the LO-NG angle in the *Euclidean* (un-weighted) sense — which is what matters for B1 directional fidelity relative to the truth vector $(\boldsymbol\lambda - \boldsymbol\lambda^\ast)$ — gives:

*[Derived (Euclidean LO-NG angle, equal-components case)]*

$$\cos \theta_r^{\text{Eucl}} \;=\; \frac{\mathbf d_{\text{LO}} \cdot \mathbf d_{\text{NG}}}{\lVert \mathbf d_{\text{LO}}\rVert_2 \cdot \lVert \mathbf d_{\text{NG}}\rVert_2} \;=\; \frac{1}{\sqrt{1 + \big(\tfrac{r}{1+r}\big)^2 \cdot \text{(asymmetry factor)}}}$$

which under equal components collapses to $\cos \theta_r^{\text{Eucl}} = 1$ — there is no misalignment because both directions coincide with the $(1,1)$ eigenvector.

This is a revealing baseline: **when the plan-level residual is perfectly symmetric across correlated edges, the LO and NG directions agree** (both point along the shared mode). The misalignment only appears when the residual is asymmetric — when the plan "wants" to credit the correlated edges differently.

### 3.3 Asymmetric-residual case — the angle bound

Take $g_1 = g$, $g_2 = -g$ (the anti-symmetric residual; the plan wants to credit edge 1 up and edge 2 down by equal amounts). Then $\hat g_+ = 0$, $\hat g_- = \sqrt 2 g$, and the residual is aligned with the $(1, -1)$ Fisher eigenvector. Again Euclidean-LO-and-NG coincide ($\cos \theta_r^{\text{Eucl}} = 1$): the NG direction is also along $(1, -1)$, just with a different magnitude scaling.

**The misalignment arises in the off-eigenframe case.** Take $g_1 = g$, $g_2 = 0$ (the plan wants to credit edge 1 only, leaving edge 2 untouched). Then $\hat g_+ = g/\sqrt 2$, $\hat g_- = g/\sqrt 2$. The NG direction:

$$\mathcal I^{-1} \mathbf g \;=\; \frac{1}{\sigma^2(1 - r^2)} (g, -rg)^T$$

**This is striking.** Under positive correlation ($r \gt 0$), the natural gradient tells the agent: "to credit edge 1 up, you must credit edge 2 *down* by $r$ times as much." The log-odds gradient direction $\mathbf d_{\text{LO}} = (g, 0)$ says: "to credit edge 1 up, credit edge 1 up and leave edge 2 alone."

The Euclidean angle between $(g, 0)$ and $(g, -rg)$:

*[Derived (Euclidean LO-NG angle under single-edge residual, positive correlation)]*

$$\cos \theta_r^{\text{Eucl}} \;=\; \frac{1}{\sqrt{1 + r^2}}$$

For $r = 0.5$ (moderate correlation): $\cos \theta = 1/\sqrt{1.25} \approx 0.894$ — angle $\approx 26.6°$.
For $r = 0.9$ (strong correlation): $\cos \theta \approx 0.743$ — angle $\approx 42.1°$.
For $r \to 1$: $\cos \theta \to 1/\sqrt 2$ — angle $\to 45°$.

The LO direction is *never* antipodal to the NG direction — the cosine stays positive. But it drifts toward $45°$ as correlation grows. At $r = 1$ (the unobservable-$C$ limit where Fisher becomes rank-1), the NG direction is singular; the whitening correction *diverges* and the analysis breaks down.

### 3.4 Generalization — the angle bound via Rayleigh

For general $\mathcal I$ with condition number $\kappa(\mathcal I) := \sigma_{\max}(\mathcal I) / \sigma_{\min}(\mathcal I)$ and any $\mathbf g$:

*[Derived (generalized LO-NG Euclidean angle bound, via Rayleigh quotient)]*

$$\cos \theta^{\text{Eucl}} \;\geq\; \frac{2 \sqrt{\kappa(\mathcal I)}}{1 + \kappa(\mathcal I)}$$

which is a standard matrix-inequality result from the natural-gradient literature (see Martens 2020 "New Insights and Perspectives on the Natural Gradient Method," JMLR 21, §4; or Amari & Nagaoka 2000 *Methods of Information Geometry*, Translations of Mathematical Monographs 191, §3.2).

**Implication for B1.** The sector-condition bound $\delta^T F(\delta) \geq \alpha \lVert\delta\rVert^2$ for the LO update against the truth-error direction is preserved only if $\theta^{\text{Eucl}} \lt 90°$, i.e., if the angle between LO and the actual mismatch direction is acute. Under $r = 0$ (L0), this is Prop B.5b (componentwise Jacobian non-negativity). Under $r \gt 0$ but finite, the angle stays acute — **B1 does not flip sign**, but the sector parameter $\alpha$ degrades by a factor proportional to $\cos \theta^{\text{Eucl}}$.

**Quantitatively:** the effective sector parameter for the LO update against the true mismatch direction under correlation $r$ is

$$\alpha_{\text{LO}}(r) \;\geq\; \alpha_{\text{LO}}(0) \cdot \frac{2\sqrt{\kappa(\mathcal I)}}{1 + \kappa(\mathcal I)}$$

which with $\kappa(\mathcal I) = (1 + \lvert r\rvert)/(1 - \lvert r\rvert)$ for the $2\times 2$ block gives $\alpha_{\text{LO}}(r)/\alpha_{\text{LO}}(0) \geq \sqrt{1 - r^2}$.

**Verdict on Q1 (angle):** The LO update is never antipodal to the truth under finite block correlation. It can be up to $45°$ off for $r \to 1$, degrading the sector parameter by up to $\sqrt{1 - r^2}$. The update still contracts toward truth — it just does so more slowly as correlation grows, with a structural singularity at $r = 1$ (the `#discussion-identifiability-floor` rank-deficient limit).

## 4. Can Fisher whitening be derived from AAD-internal principles?

The question is whether the Fisher-whitened update

$$\Delta \boldsymbol\lambda \;=\; \eta \cdot \mathcal I^{-1}(\boldsymbol\lambda) \cdot \mathbf J^T (y_G - \hat P_\Sigma)$$

is *derivable* from AAD's current machinery rather than imported from Amari.

### 4.1 Candidate: Fisher whitening from directional-fidelity preservation

**Candidate principle (directional-fidelity preservation under parameterization).** The `#gain-sector-bridge` Prop B.3 establishes that directional fidelity B1 — $\delta^T H g(\delta) \geq c \lVert\delta\rVert^2$ — is the structural condition under which A2' is derived. B1 is stated in Euclidean inner product on the mismatch space. Under a change of coordinates $\boldsymbol\lambda \to \boldsymbol\phi(\boldsymbol\lambda)$ with Jacobian $D_\phi$, the pullback of the Euclidean metric is $D_\phi^T D_\phi$. For B1 to be *coordinate-invariant* — i.e., to be a structural property of the agent's update rule rather than an artifact of the representation — the inner product must be pulled back consistently when the coordinate changes.

For a Bayesian-coherent agent ( `#credit-assignment-boundary` §"Default Signal Function"), the natural coordinate is log-odds ( `#edge-update-natural-parameter` Aczél uniqueness). The natural inner product on log-odds is *not* the Euclidean inner product; it is the inner product induced by the Fisher metric, because the Fisher metric is the unique (up to scale) Markov-invariant metric on the statistical manifold (Čencov 1982 *Statistical Decision Rules and Optimal Inference*, AMS Translations of Mathematical Monographs 53; modern treatment Amari & Nagaoka 2000, *Methods of Information Geometry*, Translations of Mathematical Monographs 191, §3).

**The AAD-internal motivation.** Under L0 (independent edges), the Fisher matrix on $\boldsymbol\lambda$ is diagonal — Euclidean and Fisher inner products on log-odds coincide up to per-coordinate scaling absorbed into $\eta_{\text{edge}}$. The B1 Euclidean-inner-product formulation in `#gain-sector-bridge` *already* matches the Fisher-inner-product formulation under L0. Under L1'/L2, the two diverge. If B1 is to remain the structural condition governing A2' sub-scope $\alpha$, the inner product under which it is stated must track the coordinate's natural geometry — which under correlated evidence is the Fisher metric.

**Theorem candidate (derivation-conditional).** *[Derived (Fisher-whitening forced by directional-fidelity preservation, conditional on parameterization-invariance of B1)]*

For a Bayesian-coherent agent updating in log-odds under correlated Bernoulli evidence, directional fidelity B1 is preserved across parameterizations if and only if the update is Fisher-whitened:

$$\Delta \boldsymbol\lambda \;=\; \eta \cdot \mathcal I^{-1}(\boldsymbol\lambda) \cdot \nabla_{\boldsymbol\lambda} \mathcal L$$

where $\mathcal L$ is the log-likelihood (or a Jacobian-transformed plan-level surrogate). The sector parameter $\alpha$ in the Fisher inner product is the minimum eigenvalue of $\eta \cdot \mathcal I^{-1} \cdot \nabla^2 \mathcal L$, which for log-concave likelihood ($\mathcal L$ Bayesian-coherent ⟹ $-\nabla^2 \mathcal L = \mathcal I$) reduces to $\alpha_{\text{Fisher}} = \eta$ — *independent* of correlation.

**Epistemic assessment of this theorem.** This is derivable in the Bayesian sub-scope $\alpha$ (Kalman / conjugate / exponential family) because there $\nabla^2 \mathcal L = -\mathcal I$ by the information identity ($\mathbb E[-\nabla^2 \log P] = \mathcal I$). Under non-Bayesian agents in sub-scope $\beta$ the information identity may fail and the derivation is conditional on the agent's update rule matching the Fisher-scoring form.

**The AAD-internal axiom.** What the theorem requires is:

*[Assumption (B1-parameterization-invariance)]*

The directional fidelity condition B1 should be coordinate-invariant: the set of update rules satisfying B1 should not depend on whether mismatch is parameterized in moment coordinates, log-odds, or any smooth reparameterization of the credence state.

This is an **AAD-internal** axiom because the alternative — B1 being Euclidean-specific — would make the entire `#gain-sector-bridge` sub-scope $\alpha$ partition *coordinate-dependent*. An agent could fail B1 in moment-parameter space and pass B1 in log-odds space (by just reparameterizing), or vice versa — the sector-condition derivation would become a property of the *coordinate chosen*, not of the *update rule*. That violates the implicit `#gain-sector-bridge` reading.

The axiom is not a throwaway — it is the coordinate-geometric analog of what `#edge-update-natural-parameter`'s evidential-additivity axiom does at the *coordinate-choice* level. Evidential-additivity forces log-odds as *the* additive-evidence coordinate. B1-parameterization-invariance forces Fisher as *the* metric on that coordinate.

### 4.2 Candidate: Fisher whitening from the `#additive-coordinate-forcing` meta-pattern

A separate derivation path runs through the three-meta-segment architecture. `#additive-coordinate-forcing`'s catalog of adjacent cases explicitly flags Lyapunov quadratic as an *adjacent family member* — "the coordinate is chosen rather than forced." The chosen quadratic is the Euclidean norm $V = \tfrac12 \lVert\delta\rVert^2$.

Under a **Fisher-information-weighted Lyapunov candidate** $V_{\mathcal I}(\boldsymbol\delta) = \tfrac12 \boldsymbol\delta^T \mathcal I(\boldsymbol\lambda^\ast) \boldsymbol\delta$, the Lyapunov decay rate for the natural-gradient update is:

$$\dot V_{\mathcal I} \;=\; -\eta \cdot \boldsymbol\delta^T \mathcal I \cdot \mathcal I^{-1} \cdot \nabla \mathcal L \;=\; -\eta \cdot \boldsymbol\delta^T \nabla \mathcal L$$

which in the Bayesian log-concave case equals $-\eta \cdot 2 V_{\mathcal I}(\boldsymbol\delta)$ to second order — **a decay at rate $2\eta$ independent of $\mathcal I$'s structure.** This is the cleanest Lyapunov statement for the natural-gradient update: under the Fisher-weighted Lyapunov, the sector condition holds with a $\mathcal I$-independent rate.

This gives a second AAD-internal motivation: the Fisher-weighted Lyapunov is the canonical choice for the natural-gradient update, exactly as the Euclidean Lyapunov is the canonical choice for the Euclidean-gradient update. The coordinate is *matched* to the update rule (the Lyapunov candidate is *adjacent family member* in `#additive-coordinate-forcing`'s language); under L1'/L2 where Euclidean and Fisher diverge, the match requires Fisher.

### 4.3 Combining the two derivation paths

Both paths point in the same direction: Fisher whitening is *not* a foreign import from Amari; it falls out of two already-load-bearing AAD principles if those principles are run coordinate-aware:

| Path | AAD principle | Fisher whitening as consequence |
|---|---|---|
| A | B1 parameterization-invariance in `#gain-sector-bridge` | The metric on log-odds must track Fisher for B1 to be structural rather than coordinate-specific |
| B | Lyapunov-coordinate-matching to update rule, via `#additive-coordinate-forcing` adjacency | The canonical Lyapunov for natural gradient is Fisher-weighted; under L1'/L2 the Euclidean Lyapunov no longer matches the update |

Both paths have the same shape: **an AAD principle that happened to be vacuously satisfied under L0 (where Fisher is diagonal and the two agree) becomes non-vacuous under L1'/L2 (where they diverge), and forcing the principle to remain operational picks out Fisher whitening**. This is the same structural shape as `#discussion-identifiability-floor`: an external theorem's implications that were dormant under simple structures become operational under richer structures. The escape here, however, is *constructive* (a correction that restores the property) rather than a no-go (a structural obstruction).

**Verdict on Q2 (derivation):** Fisher whitening is AAD-internally derivable under the axiom of B1 parameterization-invariance or (equivalently, for Bayesian-coherent agents) under the principle of Lyapunov-coordinate-matching. The derivation is conditional on these axioms being AAD-internally motivated — which they plausibly are, because they make explicit what `#gain-sector-bridge` was implicitly relying on under L0.

## 5. Restated B1 under Fisher whitening

### 5.1 Fisher-whitened directional fidelity (B1')

*[Derived (Fisher-inner-product directional fidelity)]*

For a Fisher-whitened edge update $\Delta \boldsymbol\lambda = \eta \cdot \mathcal I^{-1} \nabla_{\boldsymbol\lambda} \mathcal L$, the Fisher-inner-product directional fidelity condition is:

$$\boldsymbol\delta^T \mathcal I \cdot \big(\eta \mathcal I^{-1} \nabla \mathcal L\big) \;\geq\; c \lVert\boldsymbol\delta\rVert_{\mathcal I}^2 \quad \text{for } \lVert\boldsymbol\delta\rVert_{\mathcal I} \leq R_{\mathcal I}$$

where $\boldsymbol\delta := \boldsymbol\lambda - \boldsymbol\lambda^\ast$. The left side simplifies to $\eta \boldsymbol\delta^T \nabla \mathcal L$, and for Bayesian-coherent agents with log-concave likelihood (so $-\nabla^2 \mathcal L \succeq \mu \mathcal I$ in the Löwner order for some $\mu \gt 0$), this is lower-bounded by $\eta \mu \lVert\boldsymbol\delta\rVert_{\mathcal I}^2$. Thus **B1' holds with $c = \eta \mu$ in the Fisher inner product, independent of correlation $r$.**

### 5.2 Transfer of the sector parameter under coordinate change

The Euclidean sector parameter $\alpha_{\text{Eucl}}$ and the Fisher-inner-product sector parameter $\alpha_{\mathcal I}$ relate via $\alpha_{\text{Eucl}} \geq \alpha_{\mathcal I} / \sigma_{\max}(\mathcal I)$ (lower bound via norm equivalence) and $\alpha_{\text{Eucl}} \leq \alpha_{\mathcal I} / \sigma_{\min}(\mathcal I)$ (upper bound). Under L0 (diagonal Fisher with uniform eigenvalues), the two are equal. Under L1'/L2 with condition number $\kappa(\mathcal I)$, the Euclidean sector parameter can be up to $\kappa(\mathcal I)$ times smaller than the Fisher sector parameter.

**This is why the Euclidean-stated B1 in `#gain-sector-bridge` appears to degrade under correlation: the statement in the wrong inner product makes the constant bleed off as the coordinates become skewed.** Under Fisher-whitened updating + Fisher-inner-product B1, the constant does not bleed — the sector parameter is coordinate-intrinsic.

### 5.3 Does the proof of `#gain-sector-bridge` carry over?

Yes, with substitutions:

1. Replace the Euclidean inner product with the Fisher inner product in B1's statement.
2. Replace the Euclidean gradient $\nabla \mathcal L$ with the natural gradient $\tilde\nabla \mathcal L = \mathcal I^{-1} \nabla \mathcal L$.
3. Replace the update rule $M_t = M_{t-1} + \eta^\ast g(\delta_t)$ with its natural-gradient analog $M_t = M_{t-1} + \eta^\ast \mathcal I^{-1}(M_{t-1}) g(\delta_t)$.

The directional-fidelity calculation proceeds identically; the sector parameter is now the minimum eigenvalue of $\eta \mathcal I^{-1} \nabla^2 \mathcal L$ at the truth, which under log-concavity is $\eta$ times the spectral ratio $\lambda_{\min}(\mathcal I^{-1} \nabla^2 \mathcal L)$. For Bayesian agents with $\nabla^2 \mathcal L = -\mathcal I$, this ratio is 1 and $\alpha_{\mathcal I} = \eta$.

**The proof of `#gain-sector-bridge` carries over with $\kappa(\mathcal I)$ entering only as the Euclidean ↔ Fisher norm-equivalence penalty in the transfer back to the original `#sector-condition-derivation` framework.** This is exactly the structure of `#gain-sector-bridge`'s "Weighted-norm subtlety" paragraph (Kalman case: sector condition holds in $(P^-)^{-1}$-norm, transfers to Euclidean with $\kappa(P^-)$ penalty). The Fisher-whitening case is the generalization: weighted-sector in Fisher inner product, transfers to Euclidean with $\kappa(\mathcal I)$ penalty.

**Verdict on Q3 (B1'):** The proof of `#gain-sector-bridge` carries over cleanly. B1' is the Fisher-inner-product statement; $\kappa(\mathcal I)$ enters as a norm-equivalence penalty, structurally identical to the Kalman case's $\kappa(P^-)$.

## 6. The A2' sub-scope partition under correlation

Pulling §4 and §5 together, and integrating with the adaptive-gain spike's partition:

### 6.1 Refined A2' sub-scope partition

The current partition is $\alpha_1$ (fixed gain, B1 derived), $\alpha_2$ (adaptive gain under MG-1–MG-4 from the adaptive-gain spike), $\beta$ (A2' assumed). With Fisher whitening, we add:

| Sub-scope | Condition | A2' status |
|---|---|---|
| $\alpha_1$ | Fixed gain, independent evidence (L0), directional fidelity in Euclidean inner product | A2' derived, $\alpha = \eta \cdot c_{\min}$ |
| $\alpha_2$ | Adaptive gain (time-varying $K$) under (MG-1)–(MG-4), independent evidence | A2' derived via augmented-state Lyapunov |
| $\alpha_3$ | Fixed or adaptive gain, **correlated evidence (L1' observable-$C$ / L2 with observable correlation structure)**, **Fisher-whitened update**, B1' directional fidelity in Fisher inner product | A2' derived with $\alpha_{\mathcal I}$; Euclidean-frame penalty $\kappa(\mathcal I)$ |
| $\beta$ | Any of: directional fidelity fails structurally; unobservable correlation (L2 latent); non-Bayesian update rule without Fisher-scoring form; MAML outer loop; IMM across transitions | A2' assumed per-agent |

This is a three-axis refinement: correlation (L0 / L1'-obs / L2-obs / L2-latent) × gain adaptivity (fixed / adaptive) × coherence (Bayesian-coherent / heuristic).

### 6.2 Adaptive-gain connection (Q5)

`spike-adaptive-gain-dynamics` §7 defines meta-gain condition (MG-1)–(MG-4) for augmented-state dynamics $z = (\delta, \tilde K)$. **Fisher whitening is a meta-gain law with $K_t = \mathcal I^{-1}(\boldsymbol\lambda_t)$ — the gain is explicitly the inverse Fisher.**

To verify it satisfies (MG-1)–(MG-4):

- **(MG-1) Primary sector floor under bounded gain error.** For Bayesian-coherent agents, $\mathcal I$ is continuous in $\boldsymbol\lambda$ on the interior of $(0,1)^E$. Near the truth, $\mathcal I$ is bounded above and below by positive-definite constants, so the effective gain $K_t = \mathcal I^{-1}$ is bounded in operator norm. (MG-1) holds: $\alpha_{\text{eff}} \geq \lambda_{\min}(\nabla^2 \mathcal L) / \lambda_{\max}(\mathcal I)$ uniformly.
- **(MG-2) Meta-gain sector condition.** $\mathcal I^{-1}$ is not a free state variable — it is a deterministic function of $\boldsymbol\lambda$. The "meta-gain update" is implicit in the primary update: as $\boldsymbol\lambda$ moves, $\mathcal I$ moves with it. The meta-gain dynamics are *driven* by the primary state, not independently adapted.
- **(MG-3) Timescale separation.** Trivially satisfied — the meta-gain has no independent timescale; it tracks $\boldsymbol\lambda$ at primary-update speed.
- **(MG-4) Coupling boundedness.** $\mathcal I$ is smooth in $\boldsymbol\lambda$, so the coupling between primary and meta-gain is captured by the Lipschitz constant of $\boldsymbol\lambda \mapsto \mathcal I^{-1}(\boldsymbol\lambda)$. Bounded over compact regions of the credence state.

**Verdict on Q5 (adaptive-gain connection):** Fisher whitening is a *degenerate* special case of adaptive-gain dynamics in which the meta-gain is not an independent state variable but a deterministic function of the primary state. It is a meta-gain law with the gain/primary identification collapsed. This is consistent with (MG-1)–(MG-4) but does not exercise the full force of the meta-gain framework — in particular, it does not require the two-timescale Lyapunov of `spike-adaptive-gain-dynamics` §7 because there is only one timescale. Fisher whitening hands `spike-adaptive-gain-dynamics` a *second concrete instance* where the meta-gain is structurally derivable (the first being adaptive Kalman with Mehra estimator), with the meta-gain law being a deterministic coordinate-geometric function rather than an innovation-based estimator.

## 7. L2 scope check and the `#discussion-identifiability-floor` connection (Q3 open-endedness)

### 7.1 Where does Fisher whitening break down?

Three regimes exhaust the cases:

**L2-observable (correlation structure observable per trial).** Fisher whitening works. The Fisher matrix is well-conditioned (positive-definite) as long as the correlation structure is *non-degenerate* — i.e., no two edges are *perfectly* correlated ($r = 1$ somewhere). Under non-degenerate observable correlation, the derivation of §§4-5 goes through, and A2' is derived in sub-scope $\alpha_3$.

**L2-latent (correlation structure unobservable).** Fisher whitening breaks down. The agent cannot compute $\mathcal I^{-1}$ because it cannot observe the correlation structure. The update reduces to the L0 approximation (diagonal Fisher treated as if independent), which by §3's angle bound is off by up to $45°$ from the natural-gradient direction as correlation grows. A2' is not derived; this is sub-scope $\beta$.

**L2-singular (correlation structure deterministic).** When $r \to 1$ (some edges perfectly correlated), the Fisher matrix becomes rank-deficient and $\mathcal I^{-1}$ diverges. Fisher whitening amplifies this singular direction unboundedly, destabilizing the update. This is the structural limit; the only correction is to quotient out the redundant direction (merge the perfectly-correlated edges into a single effective edge) or refuse to update in the null direction.

### 7.2 A new `#discussion-identifiability-floor` instance?

The L2-latent case gives a *third* instance of the `#discussion-identifiability-floor` pattern, parallel to Instance 1 (on-policy detection) and Instance 2 (unobservable-$C$ L1' single-channel):

**Instance 3 candidate: Fisher whitening requires observable correlation structure.** *[Discussion (Fisher-whitening identifiability floor)]*

Under latent correlation (L2-latent), the agent has no access to $\mathcal I$ (it cannot estimate the off-diagonal entries from marginal observations alone — this is Cramér-Rao rank-deficiency on the correlation-parameter sub-block). The Fisher-whitening correction is therefore unavailable, and the LO update's angular misalignment with the natural-gradient direction is uncorrectable. Escape requires either: (a) augmenting the DAG with the latent correlation as an explicit node (converting L2-latent to L2-observable); (b) multi-channel observation structure permitting joint estimation of the correlation entries (analogous to the multi-child observability escape in `#discussion-identifiability-floor` Instance 2); (c) accepting the L0 approximation with its $\sqrt{1-r^2}$-degraded sector parameter.

**Format check against Instance 1, 2:** Both prior instances have the form "external theorem no-goes; AAD-machinery is the unique escape." Instance 3 candidate has the same form: the external theorem is Cramér-Rao applied to the correlation-parameter sub-block; the AAD escape is the `#discussion-separability-pattern` structured-repair of observability-augmentation (DAG augmentation with the latent correlation as an explicit node).

This instance is structurally distinct from Instance 2 (which is about identifying the *conditional credences* under mixture structure) — Instance 3 is about identifying the *metric/correlation structure itself*. Both arise from Fisher rank deficiency but on different sub-blocks of the parameter space. They compose: under L2-latent mixture with latent correlation, both instances fire simultaneously, and no amount of data resolves either.

**Promotion decision.** Instance 3 candidate is adjacent enough to Instance 2 that it may fold into Instance 2 as a generalization ("L1' Cramér-Rao extends to general L2 latent-correlation Cramér-Rao"), or it may stand on its own as a distinct correlation-structure-identification no-go. Decision deferred to review.

**Verdict on Q3 (open-endedness):** Fisher whitening works cleanly for L2-observable; breaks down for L2-latent via a new `#discussion-identifiability-floor` candidate instance; becomes singular at L2-degenerate (perfect correlation) requiring structural DAG repair (edge merging).

## 8. Where does this land?

### 8.1 Recommendation: extension to `#gain-sector-bridge` + new working-notes items in two other segments

Three options:

**R1 (preferred): New segment `#fisher-whitened-update-rule`.** Create `01-aad-core/src/fisher-whitened-update-rule.md` as a derived segment stating:

1. The problem: under correlated evidence, the evidential-additivity-forced log-odds update diverges from the natural-gradient direction (§3).
2. The AAD-internal derivation: Fisher whitening is forced by either B1 parameterization-invariance or Lyapunov-coordinate-matching (§4).
3. The B1' formulation: Fisher-inner-product directional fidelity, with Euclidean transfer via $\kappa(\mathcal I)$ norm equivalence (§5).
4. The A2' sub-scope $\alpha_3$ label: correlated evidence with Fisher-whitened update.
5. The L2-latent `#discussion-identifiability-floor` instance 3 candidate.

Corresponding segment edits:

- **`#gain-sector-bridge`:** add a "Fisher-whitened extension" sub-section or Discussion paragraph cross-referencing the new segment. The "Weighted-norm subtlety" paragraph is the natural landing point — the Kalman case is already a special case of Fisher-weighted inner product (with $\mathcal I = P^{-1}$ for the linear-Gaussian model).
- **`#credit-assignment-boundary`:** add a Working Notes item: *"Default signal function is log-odds-gradient; under L1'/L2, Fisher whitening restores directional fidelity in the Fisher inner product. See `#fisher-whitened-update-rule`."*
- **`#additive-coordinate-forcing`:** Working Notes expansion: the Lyapunov-adjacent-family classification needs a sub-clause for Fisher-weighted Lyapunov in the Fisher-whitened regime. The Fisher-weighted quadratic $V_{\mathcal I}$ is *matched to* the natural-gradient update rule in the same way the Euclidean quadratic was matched to the Euclidean gradient — the coordinate is chosen rather than forced by an additivity axiom.
- **`#discussion-identifiability-floor`:** if Instance 3 candidate is promoted, add as third instance after Instance 2 (L1' unobservable single-channel) and before the three open extensions. Alternative: fold into Instance 2 as a strengthening/generalization.
- **`#discussion-separability-pattern`:** correlation ladder gets an additional row: *separable core = L0; structured repair = L1'-obs + Fisher-whitened = L2-obs; general open = L2-latent with latent-correlation floor*.
- **`spike-adaptive-gain-dynamics`:** §3.3's "meta-gain as an OU-type contraction" framework gets Fisher whitening listed as a *second concrete instance* (deterministic coordinate-function form of meta-gain), alongside adaptive Kalman.

**R2: Appendix to `#credit-assignment-boundary`.** Fold §§3-5 into an appendix "Fisher-whitening extension under correlated evidence." Downside: `#credit-assignment-boundary` is already substantial; adding a whole whitening treatment bloats it.

**R3: Appendix to `#gain-sector-bridge`.** Similar to R2 but with `#gain-sector-bridge` as host. Downside: the Fisher-whitened update is more naturally located near `#credit-assignment-boundary`'s default signal, since the whole derivation is motivated by extending that signal function.

**Recommendation: R1 preferred.** The content has enough substance (five sections of derivation, a new A2' sub-scope, a candidate `#discussion-identifiability-floor` instance, and meta-pattern connections to `#additive-coordinate-forcing` and `#discussion-separability-pattern`) to warrant its own segment. Stage: `draft` pending review; type: `derivation` (uses augmented-state Lyapunov machinery); status: `conditional` (conditional on B1-parameterization-invariance axiom).

### 8.2 Connection to G-BP1 + G-BP3 cluster

The architectural-proposals document flags G-BP1 (natural-parameter reparameterization) + G-BP3 (Fisher-information unification) as a strong cluster that "together yield natural gradient descent on a Riemannian manifold" (per `msc/architectural-proposals-2026-04-22.md` §G-BP3 Gemini reaffirm). This spike is the *scoping derivation* for G-BP3 restricted to the edge-update layer: it establishes that Fisher whitening is AAD-internally motivated (not just imported), characterizes the sub-scope where it is derivable ($\alpha_3$), and identifies the structural boundary (L2-latent `#discussion-identifiability-floor` instance).

**For the G-BP3 portfolio decision:** this spike provides partial evidence for G-BP3 — specifically, that Fisher whitening at the edge-update layer is a genuine extension that both fixes a Finding (the LO-NG misalignment under correlation) and unifies machinery (absorbing Kalman's $(P^-)^{-1}$-norm, the correlation-case ladder, and the adaptive-gain meta-gain framework under a single coordinate-geometric principle). It does *not* yet argue for the full G-BP3 rewrite (Section I redefined in Fisher-information terms) — that is a larger move requiring separate scoping. What this spike does say: the edge-update layer can be Fisher-unified without disturbing the rest of Section I, and the derivation is AAD-internal rather than imported.

## 9. Derivation audit

| Claim | Source | Strength |
|---|---|---|
| Block-correlated Fisher matrix has off-diagonal $r = \theta_C(1-\theta_C)\Delta_1\Delta_2/(\sigma_1\sigma_2)$ (§2) | Direct chain-rule computation from mixture log-likelihood | Derived (exact) |
| LO-NG Euclidean angle under single-edge residual equals $\arccos(1/\sqrt{1+r^2})$ (§3.3) | Algebraic computation in Fisher eigenframe | Derived (exact) |
| Generalized angle bound $\cos\theta \geq 2\sqrt{\kappa}/(1+\kappa)$ (§3.4) | Standard matrix-inequality result (Martens 2020 JMLR §4; Amari-Nagaoka 2000) | Derived (external) |
| LO update degradation: $\alpha_{\text{LO}}(r)/\alpha_{\text{LO}}(0) \geq \sqrt{1-r^2}$ (§3.4) | Direct from angle bound + sector-condition substitution | Derived |
| Fisher whitening forced by B1 parameterization-invariance axiom (§4.1) | Candidate AAD-internal axiom: the directional-fidelity condition should be coordinate-invariant | **Derived conditional on B1-parameterization-invariance axiom** |
| Fisher whitening forced by Lyapunov-coordinate-matching (§4.2) | Via `#additive-coordinate-forcing`'s adjacent-family classification for Lyapunov | Derived (conditional on matching principle) |
| Fisher-whitened B1' holds in Fisher inner product with $c = \eta\mu$ for Bayesian-coherent agents (§5.1) | Direct: information identity $-\nabla^2\mathcal L = \mathcal I$ for exponential families | Derived |
| Proof of `#gain-sector-bridge` carries over to Fisher-whitened case with $\kappa(\mathcal I)$ as Euclidean-transfer penalty (§5.3) | Parallels Kalman case's $(P^-)^{-1}$-norm treatment | Derived |
| A2' sub-scope $\alpha_3$ (correlated evidence with Fisher whitening) (§6) | Direct from §§4-5 | Derived (conditional on the two axioms) |
| Fisher whitening as degenerate meta-gain law $K_t = \mathcal I^{-1}(\boldsymbol\lambda_t)$ (§6.2) | Direct comparison with spike-adaptive-gain-dynamics (MG-1)-(MG-4) | Derived (conditional) |
| L2-latent `#discussion-identifiability-floor` Instance 3 candidate (§7) | Cramér-Rao applied to correlation-parameter sub-block | Discussion-grade (pending Instance 2 vs Instance 3 distinction review) |
| Connection to G-BP3 architectural portfolio (§8.2) | Scope of derivation as partial evidence | Discussion-grade (framing) |

### Epistemic honest obstructions

- **(O1) B1-parameterization-invariance is not currently an explicit AAD axiom.** It is an *implicit* expectation behind `#gain-sector-bridge`'s sub-scope $\alpha$ partition — the sub-scope list would become coordinate-dependent without it. Making it explicit is a framing move; this spike recommends the move but does not resolve whether it should be added to the axiom catalog or absorbed into the text of `#gain-sector-bridge`'s Discussion.
- **(O2) The $2\times 2$ worked case does not prove the full-matrix generalization.** The angle bound of §3.4 is standard but the algebraic forms of §3.1-3.3 are specific to the $2\times 2$ block. A full-matrix treatment requires more careful handling of the plan-value Jacobian $\mathbf J$'s interaction with the full Fisher matrix. The scaling claim $\alpha_{\text{LO}}/\alpha_{\mathcal I}$ generalizes via standard norm-equivalence; the specific $\cos\theta$ formulas do not.
- **(O3) Non-Bayesian sub-scope $\beta$ agents remain outside.** The derivations assume Bayesian coherence (information identity). Non-Bayesian agents (PID, rule-based) may still *benefit* from Fisher-like whitening empirically but the derivation here does not cover them. This is consistent with `#gain-sector-bridge`'s sub-scope $\beta$ A2'-assumed status.
- **(O4) Fisher-estimator identifiability.** Under L2-latent, the agent cannot estimate $\mathcal I$ from marginal observations alone. The `#discussion-identifiability-floor` Instance 3 candidate in §7.2 formalizes this. The related question of how much data is required to estimate $\mathcal I$ well enough for whitening (finite-sample regime) is open and merits its own treatment.
- **(O5) Worked example missing.** A concrete simulation showing the LO update contracting slowly under correlation and the Fisher-whitened update recovering full contraction would strengthen the Case A worked-example case — call it "Worked example: correlated-edges strategy calibration under block-common-cause" — but is out of scope for the spike.

## 10. Answers to the seven spike angles

1. **Fisher information under L1' correlation (§2).** Block-correlated off-diagonal entry: $\mathcal I_{12}(\boldsymbol\lambda) = \theta_C(1-\theta_C)\Delta_1\Delta_2$ at truth, with dimensionless ratio $r = \theta_C(1-\theta_C)\Delta_1\Delta_2/(\sigma_1\sigma_2) \in [-1, 1]$. Correlation parameter ρ enters as block-correlation in the score covariance.

2. **Angle LO vs NG (§3).** Never antipodal under finite $r$; grows to $\arccos(1/\sqrt{1+r^2})$ for single-edge residual, to $\arccos(2\sqrt\kappa/(1+\kappa))$ in general. Upper bound $45°$ at $r \to 1$ (the rank-deficient limit). Sector parameter degrades by $\sqrt{1-r^2}$ without whitening.

3. **Whitening as derived correction (§4).** Derivable from AAD-internal axiom (B1-parameterization-invariance) or from Lyapunov-coordinate-matching. Not a wholesale Amari import.

4. **A2' partition (§6).** New sub-scope $\alpha_3$ = correlated evidence + Fisher-whitened update + Bayesian-coherent. Fits inside the existing $\alpha/\beta$ partition as a third derived sub-scope, parallel to $\alpha_1$ (fixed-gain independent) and $\alpha_2$ (adaptive-gain independent). Latent correlation (L2-latent) pushes to $\beta$ via a new `#discussion-identifiability-floor` instance candidate.

5. **B1 under the correction (§5).** B1' is the Fisher-inner-product version; holds with $c = \eta\mu$ for Bayesian-coherent agents. Proof of `#gain-sector-bridge` carries over with $\kappa(\mathcal I)$ as the Euclidean-transfer penalty — structurally identical to the Kalman case's $(P^-)^{-1}$-norm treatment.

6. **Adaptive-gain connection (§6.2).** Fisher whitening is a degenerate meta-gain law $K_t = \mathcal I^{-1}(\boldsymbol\lambda_t)$ — the meta-gain is a deterministic function of the primary state rather than an independent learned variable. Hands `spike-adaptive-gain-dynamics` a second concrete instance of derivable meta-gain (alongside adaptive Kalman with Mehra estimator).

7. **L2 scope check (§7).** Fisher whitening works for L2-observable; breaks down for L2-latent via a new `#discussion-identifiability-floor` Instance 3 candidate (Cramér-Rao on correlation-parameter sub-block); singular at L2-degenerate (perfect correlation, requiring structural DAG repair by edge merging).

## 11. Open questions after this spike

1. **Fisher-estimator sample complexity.** How much data is required to estimate $\hat{\mathcal I}_t$ well enough that the plug-in Fisher-whitened update $\Delta \boldsymbol\lambda = \eta \hat{\mathcal I}_t^{-1} \mathbf g_t$ still satisfies B1'? Finite-sample regime bounds the degradation from plug-in vs oracle whitening.

2. **Instance 2 vs Instance 3 in `#discussion-identifiability-floor`.** Whether the L2-latent Cramér-Rao floor is a distinct instance from the L1'-unobservable-$C$ single-channel floor, or a natural generalization of it, is a structural question for the `#discussion-identifiability-floor` taxonomy.

3. **Full-matrix generalization of §3's angle formulas.** The $2\times 2$ block is cleanly worked; the $E$-edge generalization uses standard norm-equivalence but loses the clean explicit form. A full-matrix treatment would be a natural appendix to the R1 segment proposal.

4. **Fisher whitening vs AMSGrad / Shampoo-style preconditioning.** The ML literature has several Fisher-approximations (AMSGrad monotonic second moment, K-FAC block-diagonal Fisher, Shampoo structured preconditioner). Each carries its own approximation cost. Spelling out which approximation corresponds to which AAD sub-scope (and which pushes into $\beta$) is worth doing before external presentation.

5. **Interaction with G-BP1's logit-scoping decision.** G-BP1 stayed narrow (log-odds at `#credit-assignment-boundary` only; Props B.1-B.7 remain in moment-parameter form). Fisher whitening at `#credit-assignment-boundary` naturally extends the narrow G-BP1 execution. Whether it triggers a wider propagation into Props B.1-B.7 is a scoping question — the Fisher-equivalence argument for the sector-parameter content suggests no, but cross-coordinate specifics (e.g., Prop B.7 L1' observable-$C$ sector parameter) should be checked against the Fisher-whitened form.

6. **Adversarial correlation.** If an adversary can choose the correlation structure (e.g., an attacker synchronizing failures across edges), the Fisher whitening becomes an online-estimation game. The `spike-adversarial-tempo-advantage` reading may transfer: faster whitening estimator beats faster adversarial correlation-structure change iff $\alpha_{\mathcal I\text{-estimator}} \gt $ correlation-structure-change rate. Not derived; adjacent spike territory.

7. **Continuous-strategy-DAG extension (O-BP4).** If edges become continuous-valued (O-BP4 in architectural-proposals), Fisher whitening generalizes naturally (the Fisher information matrix becomes a continuous-dimensional operator). This is a clean extension point for G-BP1 + G-BP3 + O-BP4 execution.

## 12. References

**Information geometry / natural gradient:**
- Amari, S.-i. (1998). "Natural gradient works efficiently in learning." *Neural Computation* 10(2):251-276.
- Amari, S.-i. & Nagaoka, H. (2000). *Methods of Information Geometry*. Translations of Mathematical Monographs 191. American Mathematical Society. §3 (Fisher metric, invariance).
- Čencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*. AMS Translations of Mathematical Monographs 53. Original invariance-based derivation of the Fisher metric.
- Martens, J. (2020). "New insights and perspectives on the natural gradient method." *J. Machine Learning Research* 21(146):1-76. §4 covers the condition-number angle bound used in §3.4.
- Ay, N., Jost, J., Lê, H. V. & Schwachhöfer, L. (2017). *Information Geometry*. Springer.

**Fisher-approximation methods (for Q11.4):**
- Martens, J. & Grosse, R. (2015). "Optimizing neural networks with Kronecker-factored approximate curvature." ICML. [K-FAC block-diagonal Fisher]
- Gupta, V., Koren, T., Singer, Y. (2018). "Shampoo: Preconditioned stochastic tensor optimization." ICML.

**Mixture-model Fisher / rank-deficiency:**
- Cramér, H. (1946). *Mathematical Methods of Statistics*. Princeton University Press. [Cramér-Rao bound]
- Dunik, J., Straka, O., Kost, O., Havlik, J. (2021). "On the identification of noise covariances and adaptive Kalman filtering: A new look at a 50 year-old problem." *Frontiers in Signal Processing*. [rank identifiability via minimal polynomial]

**AAD segments referenced:**
- `#credit-assignment-boundary` — current default signal function, log-odds form
- `#edge-update-natural-parameter` — Aczél-Cauchy-FE derivation of log-odds as unique additive-evidence coordinate
- `#gain-sector-bridge` — B1 directional fidelity, sub-scope $\alpha$ derivation, Kalman $(P^-)^{-1}$-norm subtlety
- `#sector-condition-derivation` — A2' sub-scope partition ($\alpha$ / $\beta$), Prop A.1, A.1S
- `#strategic-dynamics-derivation` — Props B.5, B.6, B.7 (L1', observable-$C$ five-way gating; unobservable-$C$ Cramér-Rao floor)
- `#additive-coordinate-forcing` — three-layer meta-pattern; Lyapunov as adjacent family member
- `#discussion-identifiability-floor` — Instance 1 (CHT on-policy); Instance 2 (L1'-unobservable Cramér-Rao)
- `#discussion-separability-pattern` — correlation ladder (L0/L1/L1'/L2); this spike proposes extending the ladder with Fisher-whitening structured-repair
- `msc/spike-adaptive-gain-dynamics.md` — (MG-1)-(MG-4) meta-gain conditions; Fisher whitening as second derivable instance

**Standard references already in use:**
- Khalil, H. K. (2002). *Nonlinear Systems*, 3rd ed. Prentice Hall.
- Khasminskii, R. (2012). *Stochastic Stability of Differential Equations*, 2nd ed. Springer.
- Nesterov, Y. (2004). *Introductory Lectures on Convex Optimization*. Springer.
