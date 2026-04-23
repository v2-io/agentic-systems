---
slug: gain-sector-bridge
type: derived
status: conditional
depends:
  - update-gain
  - mismatch-signal
  - sector-condition-derivation
  - gain-sector-derivation
stage: draft
---

# Derived: Gain–Sector Bridge

The gain-based update principle ( #update-gain) produces correction dynamics satisfying the sector condition (GA-3) whenever the update rule has *directional fidelity* — the correction points at least roughly toward reality. For gradient-based agents, this is equivalent to local strong convexity of the loss function. The sector parameter $\alpha$ is not a free parameter but is determined by the gain and the correction geometry.

## Formal Expression

### The Bridge Theorem

*[Derived (gain-sector-bridge, from update-gain + directional fidelity)]*

Given the gain-based update $M_t = M_{t-1} + \eta^\ast \cdot g(\delta_t)$ ( #update-gain), the induced correction function is:

$$F(\delta) = \eta^\ast \cdot H \, g(\delta)$$

where $H$ maps state-space corrections to observation-space mismatch reduction. The sector condition (GA-3) holds with parameter $\alpha > 0$ whenever:

**(B1) Directional fidelity.** The mismatch transform $g$ preserves the mismatch-reducing direction:

$$\delta^T H \, g(\delta) \geq c \lVert\delta\rVert^2 \quad \text{for } \lVert\delta\rVert \leq R$$

for some $c > 0$. The sector parameter is then:

$$\alpha = \eta^\ast \cdot c_{\min}, \qquad c_{\min} = \inf_{\lVert\delta\rVert \leq R} \frac{\delta^T H \, g(\delta)}{\lVert\delta\rVert^2}$$

### Gradient Equivalence

*[Derived (sector-convexity equivalence)]*

For any agent updating via gradient descent on a loss $L$ with learning rate $\eta$:

$$\alpha = \eta \cdot \mu \qquad \text{where } \mu = \inf_{\lVert\delta\rVert \leq R} \lambda_{\min}(\nabla^2 L(M^\ast + \delta))$$

is the strong convexity modulus. The basin radius $R$ is the largest ball around the optimum where $\nabla^2 L$ remains positive definite. The equivalence is exact:

$$\text{GA-3 holds with } (\alpha, R) \iff L \text{ is locally } (\alpha/\eta)\text{-strongly convex on } \mathcal B_R(M^\ast)$$

### Verified Instances

| Update class | Bridge status | Sector parameter $\alpha$ | Valid region |
|---|---|---|---|
| Scalar Kalman | Derived | $K = P^-/(P^- + R_{\text{obs}}) = \eta^\ast$ | Global |
| Matrix Kalman | Derived | $\lambda_{\min}^+(KH)$ in $(P^-)^{-1}$-norm | Observable subspace |
| Beta-Bernoulli | Derived | $1/(n+1) = \eta_{\text{edge}}$ | Global |
| Exponential family (natural params) | Derived | $\eta \cdot \lambda_{\min}(\text{Fisher})$ | Global |
| Gradient on strongly convex loss | Derived | $\eta \cdot \mu$ | Global ($R = \infty$) |
| Gradient on locally convex loss | Derived | $\eta \cdot \mu_{\text{local}}$ | Basin of attraction |
| Gradient on non-convex loss | Fails at basin boundary | N/A beyond $R$ | Finite $R$ |
| SPR-tuned PID on positive-real plant with anti-windup | Derived | $\alpha_{\text{PID}} = \omega_c \sin(\varphi_m) / \kappa(P)$ (phase margin as sector constant; crossover frequency as tempo; KYP-certificate condition number as degradation) | Classical linear regime + Lur'e sector-bounded nonlinearity within specified plant-Lipschitz threshold |

### Failure Modes

The bridge fails precisely in five cases:

1. **Directional infidelity.** The mismatch transform $g$ rotates the correction away from the mismatch ($\delta^T H g(\delta) \leq 0$). Occurs with pathological parameterizations or severe model-observation misalignment. For optimal Bayesian updates, B1 holds by construction.

2. **Gain collapse.** $\eta^\ast \to 0$ while $\rho > 0$, so $\alpha \to 0$ and the persistence condition eventually fails. Not a failure of the bridge but of the persistence condition — see the gain-collapse analysis in #update-gain.

3. **Nonlinear saturation.** The correction function $g$ saturates at large $\lVert\delta\rVert$, so the sector ratio $\delta^T g(\delta)/\lVert\delta\rVert^2$ decays. The sector condition holds locally with $\alpha$ depending on $R$. This is exactly what A2' (the local sector condition) is designed for.

4. **Unobservable directions.** When $\ker(H) \neq \{0\}$, the correction has no effect on mismatch in unobservable directions. The sector condition holds only in the observable subspace. See #observability-dominance.

5. **Model misspecification.** The model class does not contain the truth, so the gradient direction is wrong. B1 fails because the correction aims at the wrong target. This is the #structural-adaptation-necessity trigger.

## Epistemic Status

*Conditional derivation.* The bridge theorem is exact for all cases where B1 (directional fidelity) holds. The resulting sub-scope structure of A2' in #sector-condition-derivation is:

**Sub-scope $\alpha$ (B1 structural, A2' derived):**

- **Optimal Bayesian updates** (Kalman, conjugate, exponential family): B1 holds by construction — the posterior update minimizes expected loss, ensuring the correction aligns with the mismatch. The sector parameter equals the gain: $\alpha = \eta^\ast$ (scalar) or $\alpha = \lambda_{\min}^+(KH)$ (matrix Kalman, observable subspace).
- **Gradient descent on (locally) strongly convex losses**: B1 is *equivalent* to strong convexity (Prop B.4) — a well-characterized property with an extensive optimization theory literature. The sector parameter factors as $\alpha = \eta \cdot \mu$ (learning rate × curvature).
- **L2-regularized convex losses**: the regularization parameter $\lambda$ provides a global floor $\mu \geq \lambda$, so $\alpha \geq \eta \lambda$ globally.
- **Exponential families in natural parameters**: Fisher information matrix is PD on the interior; $\alpha = \eta \cdot \lambda_{\min}(\text{Fisher})$ globally.
- **Linear corrections with PD gain–observation product**: $\alpha = \lambda_{\min}^+(KH)$.

Within sub-scope $\alpha$, A2' is written down by inspection of the update rule — no independent posit is required. This is what `#sector-condition-derivation` "Grounding of GA-3 — sub-scope $\alpha$" names.

**Sub-scope $\beta$ (B1 not structural, A2' assumed per-agent):**

- **Non-gradient agents** (PID controllers, rule-based systems, human judgment): B1 remains an empirical claim. Well-tuned PID has B1 empirically; badly-tuned PID may violate it.
- **Severely misspecified agents** (FM-5 below): proper-gradient updates can aim at the wrong target.
- **Variational / approximate posteriors**: B1 not guaranteed by optimality — approximation-direction error can rotate the correction.
- **Non-convex gradient agents beyond the basin** (FM-3 + basin boundary): A2' fails where the loss curvature goes non-positive; the structural-adaptation-necessity trigger.
- **Stochastic gradients, per-step**: A2' holds in expectation; per-step noise enters as effective disturbance under Prop A.1S.

The bridge covers sub-scope $\alpha$ rigorously and characterizes the boundary to sub-scope $\beta$ via the five failure modes. It does *not* eliminate GA-3 as an assumption for all AAD-in-scope agents — some agent classes genuinely require A2' as a primitive posit, and the honest architectural statement is scope narrowing rather than universal derivation (see `msc/spike-a2-prime-strengthening.md` for the analysis).

The gradient equivalence is validated by simulation across quadratic, logistic, exponential-family, and non-convex losses. The Kalman case is verified analytically. Full derivations and simulation results in #gain-sector-derivation.

**Max attainable:** *conditional* — the condition (B1 or strong convexity) is inherent, not removable. Pathological update rules exist that violate B1 (FM-1 provides a counterexample that satisfies every AAD postulate and the gain-based update form but has $\delta^T g(\delta) = 0$ identically). Scope + gain structure alone does not force B1; some optimality / coherence / rationality constraint (Bayesian coherence, gradient-of-a-convex-loss, etc.) is required.

**Weighted-norm subtlety.** In the matrix Kalman case, the sector condition holds in the $(P^-)^{-1}$-weighted inner product, not the Euclidean norm. For fully observable systems with bounded condition number $\kappa(P^-)$, the norms are equivalent up to $\kappa(P^-)$. The Lyapunov proofs in #sector-condition-derivation use the Euclidean norm, which remains valid with the quantitative adjustment $\alpha_{\text{Euclidean}} \geq \alpha_{\text{weighted}} / \kappa(P^-)$.

**Fisher-metric cases under parameterization-invariance.** The exponential-family-in-natural-parameters row and the matrix-Kalman row of Verified Instances both have natural statements in a Fisher-metric inner product rather than the Euclidean one. Under the **(PI) parameterization-invariance** axiom named in #agent-identity (AAD's theorems should not depend on arbitrary choice of coordinates on $M_t$), Čencov's 1982 uniqueness theorem (*Statistical Decision Rules and Optimal Inference*, AMS; subsequent Ay-Jost-Lê-Schwachhöfer 2017 extensions) forces the Fisher information metric uniquely on statistical-manifold sub-cases of $M_t$. Two consequences:

- *The matrix-Kalman sector constant is natively stated in the information metric $M = (P^-)^{-1}$* — under (PI), this is not a choice but forced. The $\kappa(P^-)$ Euclidean-transfer penalty in the paragraph above vanishes; the derivation is AAD-internally *forced*, not AAD-internally *preferred*.
- *The exponential-family-natural-parameter sector constant is natively stated in the Fisher metric* $\mathbf I(\theta)$ — under (PI), this is forced; the contraction rate equals $\eta$ globally on the interior of the natural-parameter domain (Fisher-conditioning degradation removed).

Under (PI), these two rows of Verified Instances upgrade from *derived (conditional on choice of inner product)* to *derived (AAD-internally forced)* via Čencov. Under non-adoption of (PI), they remain at the Euclidean-transferred statement with the $\kappa(P^-)$ / $\lambda_{\min}(\text{Fisher})$ penalty. This is the Fisher-layer analog of the chain-rule-additivity axiom that grounds the divergence-layer uniqueness theorem in #strategy-cost-regret-bound and the evidential-additivity axiom that grounds the update-layer uniqueness theorem in #edge-update-natural-parameter — in each case an AAD-internal axiom combined with a uniqueness theorem forces a coordinate. The structural positioning is named in #discussion-additive-coordinate-forcing.

The remaining Verified Instances rows (scalar Kalman, Beta-Bernoulli, gradient on strongly convex, L2-regularized, linear-PD-symmetric) live in Euclidean metric naturally; no Fisher-metric choice is at issue, so (PI) has no effect on them beyond transparency.

## Discussion

**GA-3 is grounded, not floating.** Before this result, GA-3 ("the correction function satisfies the sector condition") was an opaque global assumption — the theory's softest structural joint. The bridge transforms it: for well-designed agents, GA-3 is a consequence of the update mechanism's geometry, not an independent postulate. The assumption load shifts from "the correction function has this property" (hard to verify in general) to "the update rule has directional fidelity" (transparent and checkable for specific systems).

**The α-T relationship is derived for the important cases.** #persistence-condition notes that $\alpha$ is monotone increasing in $\mathcal{T}$ across all tested correction functions. For linear correction (Kalman, Beta-Bernoulli), $\alpha = \mathcal{T}$ exactly. For gradient correction on strongly convex losses, $\alpha = \eta \cdot \mu$ where $\mu$ is the curvature — monotone in $\eta$ (which is monotone in $\mathcal{T}$) for fixed loss landscape. The empirical observation is now structurally grounded.

**Basin boundary = structural adaptation trigger.** For gradient agents with non-convex losses, the basin radius $R$ is the convexity radius of the loss landscape. When mismatch exceeds $R$, the agent has been pushed out of its convexity basin — the correction function reverses direction and the sector condition fails. This IS the #structural-adaptation-necessity trigger, now with a precise geometric characterization: structural adaptation is needed when the agent crosses an inflection surface of its loss landscape.

**The theory's formal chain is tightened.** The prediction chain becomes:

$$\text{gain principle} + \text{B1} \;\xrightarrow{\text{derived}}\; \text{sector condition (GA-3)} \;\xrightarrow{\text{Lyapunov (exact)}}\; \text{persistence, reserve, adversarial scaling}$$

The left arrow is this segment. The right arrow is #sector-condition-derivation. The discrete-time framework ( [#discrete-sector-condition](discrete-sector-condition.md)) requires an additional Lipschitz bound on the correction function ($\lVert F_d(\delta)\rVert \leq c_{\max}\lVert\delta\rVert$ with $c_{\max} < 2/\eta^\ast$) — strictly stronger than an inner-product upper bound, needed because the discrete contraction involves $\lVert F_d\rVert^2$. This is automatically satisfied for Bayesian updates (the posterior lies between prior and data) and for gradient descent on smooth losses (where $c_{\max}$ is the Lipschitz constant $L$). With this constraint and the step-size condition $\eta^\ast < 2c_{\min}/c_{\max}^2$, the fluid limit is formally justified: Model D steady state is exact, Model S variance gap is $O(\eta^\ast c_{\max})$. Section I's formal chain is now complete.
