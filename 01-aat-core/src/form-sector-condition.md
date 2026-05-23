---
slug: form-sector-condition
type: formulation
status: conditional
depends:
  - def-mismatch-signal
  - def-adaptive-tempo
  - emp-update-gain
stage: claims-verified
---

# Formulation: Sector Condition (A2')

The sector condition (A2') is the structural shape AAT chooses for the correction-function geometry: the correction points roughly inward, with magnitude bounded below relative to the mismatch, on a local region of validity. Together with the companion structural properties (A1) zero-correction-at-zero-mismatch and (A3) tempo-monotonicity, A2' is the formal expression of "the agent's adaptation tracks reality with at least baseline efficiency" — the form on which the persistence and adaptive-reserve results of #deriv-sector-condition rest, and the form which downstream consumers (`#deriv-discrete-sector-condition`, `#deriv-variational-sector-condition`, `#deriv-adaptive-gain-dynamics`, `#der-gain-sector-bridge`) extend, weaken, or ground.

## Formal Expression

### Setup objects (carried into the form)

Let $\delta(t) \in \mathbb{R}^n$ be the mismatch vector ( #def-mismatch-signal — the difference between the model's predictions and reality across $n$ observable dimensions). Let $F(\mathcal{T}, \delta) \colon \mathbb{R}_+ \times \mathbb{R}^n \to \mathbb{R}^n$ be the **correction function** — how the agent's adaptive process reduces mismatch — mapping into the same space as $\delta$ so that the inner product $\delta^T F$ is well-defined. This subsumes the update gain $\eta^\ast$ ( #emp-update-gain), event rate $\nu$, and the structure of the update rule. The adaptive tempo $\mathcal{T}$ ( #def-adaptive-tempo) is the rate parameter.

### (A1) Zero Correction at Zero Mismatch

*[Assumption A1]*

$$F(\mathcal{T}, 0) = 0$$

No correction is applied when the model perfectly matches reality. Uncontroversial by construction.

### (A2') Local Sector Condition

There exists a region $\mathcal{B}_R = \{\delta : \lVert\delta\rVert \leq R\}$ and $\alpha \gt 0$ such that (following the sector-condition framework of Lur'e[^lure1957]):

*[Formulation A2' (sector-condition) — derived in sub-scope $\alpha$, assumed in sub-scope $\beta$ (see Grounding below)]*

$$\delta^T F(\mathcal{T}, \delta) \geq \alpha \lVert\delta\rVert^2 \quad \forall \delta \in \mathcal{B}_R$$

The correction function always points "inward" (reducing mismatch), and its magnitude is bounded below relative to $\lVert\delta\rVert^2$. The linear case has $\alpha = \mathcal{T}$. A saturating correction has $\alpha$ decreasing for large $\lVert\delta\rVert$. A threshold correction has $\alpha = 0$ for small $\lVert\delta\rVert$.

The local form allows the correction to break down outside $\mathcal{B}_R$ — the structural adaptation regime of #result-structural-adaptation-necessity.

### (A3) Tempo Monotonicity

*[Assumption A3]*

For fixed $\delta$, $\delta^T F(\mathcal{T}, \delta)$ is monotone increasing in $\mathcal{T}$. Higher tempo means faster correction.

### Parameter interpretation

The sector parameter $\alpha$ is determined by the adaptive tempo $\mathcal{T}$ and the structure of the correction function. In the linear case, $\alpha = \mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$. In nonlinear cases, $\alpha$ represents the *worst-case* correction efficiency within the valid region — the minimum ratio of correction power to mismatch magnitude. The radius $R$ represents the model class capacity: how large a mismatch can grow before the correction mechanism fails (i.e., before the sector condition ceases to hold), at which point structural adaptation ( #result-structural-adaptation-necessity) becomes necessary.

## Epistemic Status

A2' is a *formulation* — a chosen structural shape for the correction-function geometry that captures "the correction points roughly inward with bounded efficiency." Several structurally distinct shapes would fit the same role (a sign-only condition; a two-point monotonicity; a contraction-rate bound; a non-Euclidean weighted inner-product variant — see *Why Euclidean A2' specifically* in Discussion below). A2' is the canonical choice *matched to the quadratic Lyapunov candidate* $V = \tfrac12\lVert\delta\rVert^2$ used in #deriv-sector-condition, and matched to the gain-based update form on which #der-gain-sector-bridge derives it for sub-scope $\alpha$.

The status is *conditional* because A2' is **derived** for one explicitly named sub-scope of AAT-in-scope agents and **assumed as a per-system empirical claim** for the complementary sub-scope. The Lyapunov derivations downstream of A2' ( #deriv-sector-condition Props A.1, A.1S, A.2; Corollary A.1S.1) apply uniformly across both sub-scopes — they operate downstream of A2' regardless of how it is established. The sub-scope partition is *scope narrowing*, not scope retreat: it makes explicit which agent classes get A2' as a derived consequence of their update geometry, and which classes carry it as a structurally well-scoped posit.

### Sub-scope $\alpha$ (A2' derived)

For a characterized class of AAT-in-scope agents, A2' is a *derived* consequence of the update rule, not a primitive assumption. #der-gain-sector-bridge (Prop B.3) shows that the gain-based update $M_t = M_{t-1} + \eta^\ast g(\delta_t)$ ( #emp-update-gain) induces a correction function satisfying A2' whenever the update rule has **directional fidelity (B1)** — $\delta^T H g(\delta) \geq c_{\min} \lVert\delta\rVert^2$ on $\mathcal{B}_R$. Sub-scope $\alpha$ — the agent classes where B1 holds structurally — includes:

- *Optimal Bayesian updates* (Kalman, conjugate families): B1 holds by Bayes-risk minimization. $\alpha = \eta^\ast \cdot c_{\min}$, reducing to $\alpha = \eta^\ast$ in the scalar case.
- *Exponential families in natural parameters*, on a bounded interior scope $\Theta_0 \subset \operatorname{int}(\Theta)$: the Hessian is the Fisher information matrix, PD on the interior. $\alpha = \eta \cdot \mu_0$ where $\mu_0 = \inf_{\theta \in \Theta_0} \lambda_{\min}(\mathbf{I}(\theta)) \gt 0$. Pointwise PD does not imply a uniform global lower bound: $\inf_{\theta \in \Theta} \lambda_{\min}(\mathbf{I}(\theta))$ can be zero (Poisson: $\mathbf{I}(\theta) = e^\theta$, $\inf_{\theta \in \mathbb{R}} e^\theta = 0$), so $\Theta_0$ supplies the local-region scope $R$ that A2' requires. Families with a uniform Fisher floor on $\Theta$ (Gaussian-mean, Beta-Bernoulli) extend to global $\alpha$.
- *Gradient descent on locally strongly convex losses* (Prop B.4): B1 is *equivalent* to strong convexity via the gradient-monotonicity characterization (Nesterov 2004[^nesterov2004], Thm 2.1.10). $\alpha = \eta \cdot \mu$ where $\mu$ is the strong convexity modulus.
- *L2-regularized convex losses*: regularization provides a floor $\mu \geq \lambda$, so $\alpha \geq \eta \lambda$ globally.
- *Linear corrections with positive-definite gain–observation product*: $\alpha = \lambda_{\min}^+(KH)$ (matrix Kalman, restricted to the observable subspace).

Within sub-scope $\alpha$, A2' is written down by inspection of the update rule; no independent posit is required.

### Sub-scope $\beta$ (A2' assumed as empirical claim)

For the remaining AAT-in-scope agents, A2' stands as a well-scoped empirical claim about the agent's correction geometry. Sub-scope $\beta$ includes:

- *PID controllers with fixed gains* — no gradient / optimality structure; B1 is a tuning question, not a structural consequence.
- *Rule-based systems* — no continuous update rule; A2' is domain-specific (see also the structural Lipschitz-floor scope-exit in Discussion below).
- *Human judgment / organizational learning* — structural analogy in #emp-update-gain; no formal B1 guarantee.
- *Severely misspecified agents* (FM-5 in #der-gain-sector-bridge) — proper-gradient rules can aim at the wrong target.
- *Variational / approximate posteriors* — B1 not guaranteed by optimality because approximation error can rotate the correction. Under a controlled KL bound, an intermediate sub-scope $\alpha'$ recovers a degraded form of A2' (see #deriv-variational-sector-condition).
- *Non-convex gradient agents beyond the basin* — A2' fails at basin boundary; this IS the #result-structural-adaptation-necessity trigger.
- *Stochastic gradients (per-step)* — A2' holds in expectation; per-step noise enters as effective disturbance under #deriv-sector-condition Prop A.1S.

Within sub-scope $\beta$, A2' must be verified per-system — the claim is stronger than what AAT's postulates + gain structure alone can force (an agent with $g(\delta) = R_{90°}\delta$ satisfies every AAT postulate but violates B1 trivially; see #der-gain-sector-bridge FM-1).

## Discussion

### Operator-family classification (external mathematical lineage)

The sub-scope $\alpha$/$\beta$ partition can be restated precisely in the operator-theoretic language of Rockafellar 1970 (*Convex Analysis*, §24) and Bauschke & Combettes 2017 (*Convex Analysis and Monotone Operator Theory in Hilbert Spaces*, 2nd ed., §§22–28). Casting the discrete update map as $T_d(\delta) = \delta - \eta^\ast F_d(\delta)$ with $T_d(0) = 0$, A2' at $\delta^\ast = 0$ is exactly a **one-point strong monotonicity condition** on $A = I - T_d$, and DA2'-inc (the incremental strengthening required by `#form-composition-closure`'s bridge lemma, stated in #deriv-discrete-sector-condition) is **full two-point strong monotonicity** in the Rockafellar sense. Sub-scope $\alpha$ maps onto established operator families:

- **Optimal Bayesian updates** (Kalman, conjugate, exponential family) ≡ proximal / firmly nonexpansive operators (Bauschke-Combettes Prop 23.7). Firmly nonexpansive is equivalent to $\tfrac{1}{2}$-averaged; operator-sector condition holds with the gain as the sector constant.
- **Gradient operators on strongly convex functions** ≡ cocoercive operators via the Baillon-Haddad theorem; strong monotonicity with modulus $\eta\mu$.
- **Exponential families in natural parameters** ≡ natural-gradient operators in the Fisher-weighted Hilbert space (Amari 1998; cf. #der-gain-sector-bridge "Fisher-metric cases under parameterization-invariance" for the AAT-internal forcing via (PI)/Čencov named in #disc-additive-coordinate-forcing).
- **L2-regularized convex gradients** ≡ shifted monotone-gradient operators with regularization-provided floor.
- **Linear corrections with PD gain–observation product** ≡ linear contraction in the $(P^-)^{-1}$-weighted inner product.

Sub-scope $\beta$ maps onto "operator families that are not cocoercive in any natural inner product": PID (tuning-dependent; not cocoercive generically); rule-based / symbolic (no inner-product structure); variational / amortized (approximation-gap rotation); non-convex-gradient beyond basin (non-monotone on the full domain); per-step SGD (noise-dominated); human judgment (no formal rule). The $\alpha$/$\beta$ epistemic labeling in AAT tracks whether the operator family admits operator-sector structurally (derived from the class definition) or only under empirical per-instance verification — a scope-honesty move, not a mathematical reclassification.

This recognition positions AAT's sector-condition framework as a specialization of monotone-operator theory (Minty 1962; Browder 1968; Rockafellar 1970; Bauschke-Combettes 2017) to one-point-anchored strong monotonicity under a specific inner product structure. AAT's distinctive content — one-point anchoring at the equilibrium (strictly weaker than full two-point strong monotonicity, matched to fixed-point-at-target semantics); Model D / Model S disturbance decomposition; composition with the identifiability-floor meta-pattern; composition-consistency postulate; the $\alpha$/$\beta$ epistemic labeling itself — sits as specialization + repurposing rather than strict generalization. This acknowledgment is load-bearing for scope honesty: the mathematical machinery is established; AAT's value lies in its AAT-internal architecture (organization-of-scope under a singular-trajectory agent, signed-coupling structure, forced coordinates via uniqueness theorems, three meta-patterns) rather than in novel monotone-operator mathematics. The unification has honest limits: the coarse-graining projection $\Lambda$ (`#form-composition-closure`) does not fit the operator-sector primitive; three of five metric-$\alpha_2$ cases in `#result-contraction-template` remain theorem-imported; the identifiability-floor axis is orthogonal.

### Sub-scope $\beta$ "rule-based / discontinuous" — structural Lipschitz floor

*[Derived, status: exact scope-exit statement.]* The rule-based / state-machine / threshold-triggered / discontinuous entry in sub-scope $\beta$ is not merely "empirical verification required"; it is a **structural scope-exit for contraction-based bridge-lemma analysis**. For correction functions $F$ that are not locally Lipschitz, no scalar sector bound $\delta^\top F(\delta) \geq \alpha\lVert\delta\rVert^2$ implies the full-update-map contraction required by `#form-composition-closure`'s bridge lemma — the update map $f_c(X, o) = X - \eta^\ast F(X)$ can exhibit $\Omega(1)$ jumps between arbitrarily close $X, X'$ at rule-firing boundaries, so no $\lambda \lt 1$ Lipschitz constant exists. Concrete counterexample: $F(\delta) = \alpha\delta$ for $\lvert\delta\rvert \lt 1$ and $F(\delta) = \alpha\delta + \operatorname{sign}(\delta)$ for $\lvert\delta\rvert \geq 1$ — the sector bound holds with $\alpha$, but $f_c$ jumps by $\eta^\ast$ at $\lvert X\rvert = 1$, violating contraction. The appropriate external apparatus for this class is the **hybrid-dissipative framework** (van der Schaft & Schumacher 2000, *An Introduction to Hybrid Dynamical Systems*, Springer; Di Bernardo, Liuzza & Russo 2014, *SIAM J. Control Optim.* 52) — distinct machinery (dwell-time, Filippov solutions, impulsive-dissipative inequalities) operating on a different regularity class. AAT's Lyapunov machinery in #deriv-sector-condition and the contraction machinery in `#result-contraction-template` both require $C^1$ or better regularity; the scope-exit to hybrid-dissipative analysis is honest and structural, not a deficiency to be repaired within AAT's current apparatus. Under `#disc-identifiability-floor`'s Instance 2 pattern (Cramér-Rao floor under unobservable common cause), rule-based agents whose rule firing depends on regime structure — e.g., threshold-triggered state-machines with regime-dependent thresholds — additionally suffer regime-C identifiability collapse when the regime variable is unobservable; the non-contractibility and the non-identifiability compose in that case.

### Why Euclidean A2' specifically

The A2' form $\delta^T F \geq \alpha \lVert\delta\rVert^2$ is the sector condition *matched to the quadratic Lyapunov candidate* $V = \tfrac{1}{2}\lVert\delta\rVert^2$ used by #deriv-sector-condition. A converse-Lyapunov argument (Khalil 2002[^khalil2002], Thm 4.17) gives: if persistence holds under the dynamics $\dot\delta = -F(\delta)$ on $\mathcal{B}_R$, then there exists a quadratic-equivalent Lyapunov function $V_\ast(\delta)$ with $c_1\lVert\delta\rVert^2 \leq V_\ast \leq c_2\lVert\delta\rVert^2$ — but $V_\ast$ may not be the Euclidean norm itself. Under a weighted Lyapunov candidate $V(\delta) = \tfrac{1}{2}\delta^T P \delta$, the natural sector condition is $\delta^T P F(\delta) \geq \alpha\, \delta^T P \delta$; the matrix-Kalman case of #der-gain-sector-bridge is exactly this in the $(P^-)^{-1}$-weighted inner product, with a norm-equivalence transfer to Euclidean A2' degraded by the condition number $\kappa(P^-)$. Euclidean A2' is therefore not the unique sector form — it is the canonical one matched to the canonical $V$. An agent that persists under a non-Euclidean metric satisfies a weighted-sector A2' that transfers to Euclidean A2' only up to norm equivalence. #disc-additive-coordinate-forcing classifies the Lyapunov case as an *adjacent family member* to AAT's three primary additive-coordinate-forcing instances (chain / divergence / update, where a logarithmic coordinate is uniquely forced via Cauchy's functional equation under an AAT-internal additivity axiom): here the quadratic coordinate is matched to the sector form rather than forced by one.

### How downstream segments use this form

- #deriv-sector-condition consumes A2' as the Lyapunov-derivation input: Props A.1 / A.1S / A.2 prove ultimate boundedness, mean-square persistence, and adaptive reserve under (A1), (A2'), (A3); Corollary A.1S.1 establishes the disturbance-model containment dichotomy $P(\tau_R \lt \infty) \in \{0,1\}$.
- #deriv-stochastic-non-exit demonstrates the load-bearing Model-S half of Cor A.1S.1 — that no horizon-independent non-exit bound exists under additive stochastic forcing — using A2' on $\mathcal{B}_R$ as the Itô-Lyapunov input.
- #der-gain-sector-bridge derives A2' for sub-scope $\alpha$ under directional fidelity (B1), making the sub-scope-$\alpha$ partition above structural rather than postulated.
- #deriv-discrete-sector-condition states the discrete-time analog (DA2'), strengthening A2' with an additional Lipschitz bound on $\lVert F_d\rVert$ to control the quadratic term that arises in discrete contraction.
- #deriv-variational-sector-condition states $\varepsilon$-fidelity A2' under controlled-KL variational approximation, with $O(\sqrt\varepsilon)$ sector-constant degradation — recovering an intermediate sub-scope $\alpha'$ within the partition above.
- #deriv-adaptive-gain-dynamics refines sub-scope $\alpha$ into fixed-gain ($\alpha_1$) and adaptive-gain ($\alpha_2$ under meta-gain conditions MG-1–MG-4) layers.
- #result-sector-condition-stability and #result-sector-persistence-template state the persistence results in result-segment voice; #form-composition-closure and the composite-agent segments in Part III consume DA2'-inc as the bridge-lemma precondition.

## Working Notes

- Landing-context provenance: this segment was carved out of #deriv-sector-condition in the 451729 D.1 Gate verification cycle (2026-05-20) to resolve a depends-graph topology issue — #der-gain-sector-bridge and #deriv-stochastic-non-exit both already depended on #deriv-sector-condition, so making the Lyapunov-derivation segment depend on its own A2'-form-consumers would have created cycles. The sub-scope $\alpha$/$\beta$ partition reflects the strengthening trail recorded in `spikes/spike-a2-prime-strengthening.md` — the analysis that ruled out a universal A2' derivation and identified the five operator families where the bridge is structural.
- The companion-property partition (A1, A2', A3 together) is held here as the canonical setup; alternate orderings or sub-scope refinements (e.g., the $\alpha_1$/$\alpha_2$/$\alpha_3$/$\alpha'$ ladder accumulated across `#deriv-variational-sector-condition`, `#deriv-adaptive-gain-dynamics`, `#deriv-fisher-whitened-update-rule`) live in their respective segments and inherit this form by reference rather than re-stating it.

---

[^lure1957]: Lur'e, A. I. (1957). *Some Nonlinear Problems in the Theory of Automatic Control*. Gostekhizdat. Original sector-condition framework for absolute stability.
[^nesterov2004]: Nesterov, Y. (2004). *Introductory Lectures on Convex Optimization*. Springer. Theorem 2.1.10 (strong convexity characterized by gradient monotonicity).
[^khalil2002]: Khalil, H. K. (2002). *Nonlinear Systems* (3rd ed.). Prentice Hall. Theorem 4.17 (converse Lyapunov).
