# Cluster Reference: Lyapunov Persistence and Sector Conditions

**Overview:** Formalizes agent survival using Lyapunov stability and sector bounds, establishing the exact scaling dichotomy of tracking error against deterministic drift versus stochastic noise.

---

## Canonical Source Segments

### Source: `form-sector-condition.md`

```yaml
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
```


# Formulation: Sector Condition (A2')

The sector condition (A2') is the structural shape AAT chooses for the correction-function geometry: the correction points roughly inward, with magnitude bounded below relative to the mismatch, on a local region of validity. Together with the companion structural properties (A1) zero-correction-at-zero-mismatch and (A3) tempo-monotonicity, A2' is the formal expression of "the agent's adaptation tracks reality with at least baseline efficiency" — the form on which the persistence and adaptive-reserve results of #deriv-sector-condition rest, and the form which downstream consumers (`#deriv-discrete-sector-condition`, `#deriv-variational-sector-condition`, `#deriv-adaptive-gain-dynamics`, `#der-gain-sector-bridge`) extend, weaken, or ground.

## Formal Expression

### Setup objects (carried into the form)

Let $\delta(t) \in \mathbb{R}^n$ be the mismatch vector ( #def-mismatch-signal — the difference between the model's predictions and reality across $n$ observable dimensions). Let $F(\mathcal{T}, \delta) \colon \mathbb R_+ \times \mathbb{R}^n \to \mathbb{R}^n$ be the **correction function** — how the agent's adaptive process reduces mismatch — mapping into the same space as $\delta$ so that the inner product $\delta^T F$ is well-defined. This subsumes the update gain $\eta^\ast$ ( #emp-update-gain), event rate $\nu$, and the structure of the update rule. The adaptive tempo $\mathcal{T}$ ( #def-adaptive-tempo) is the rate parameter.

### (A1) Zero Correction at Zero Mismatch

*[Assumption A1]*

$$F(\mathcal{T}, 0) = 0$$

No correction is applied when the model perfectly matches reality. Uncontroversial by construction.

### (A2') Local Sector Condition

There exists a region $\mathcal B_R = \{\delta : \lVert\delta\rVert \leq R\}$ and $\alpha \gt 0$ such that (following the sector-condition framework of Lur'e[^lure1957]):

*[Formulation A2' (sector-condition) — derived in sub-scope $\alpha$, assumed in sub-scope $\beta$ (see Grounding below)]*

$$\delta^T F(\mathcal{T}, \delta) \geq \alpha \lVert\delta\rVert^2 \quad \forall \delta \in \mathcal{B}_R$$

The correction function always points "inward" (reducing mismatch), and its magnitude is bounded below relative to $\lVert\delta\rVert^2$. The linear case has $\alpha = \mathcal{T}$. A saturating correction has $\alpha$ decreasing for large $\lVert\delta\rVert$. A threshold correction has $\alpha = 0$ for small $\lVert\delta\rVert$.

The local form allows the correction to break down outside $\mathcal B_R$ — the structural adaptation regime of #result-structural-adaptation-necessity.

### (A3) Tempo Monotonicity

*[Assumption A3]*

For fixed $\delta$, $\delta^T F(\mathcal{T}, \delta)$ is monotone increasing in $\mathcal{T}$. Higher tempo means faster correction.

### Parameter interpretation

The sector parameter $\alpha$ is determined by the adaptive tempo $\mathcal{T}$ and the structure of the correction function. In the linear case, $\alpha = \mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$. In nonlinear cases, $\alpha$ represents the *worst-case* correction efficiency within the valid region — the minimum ratio of correction power to mismatch magnitude. The radius $R$ represents the model class capacity: how large a mismatch can grow before the correction mechanism fails (i.e., before the sector condition ceases to hold), at which point structural adaptation ( #result-structural-adaptation-necessity) becomes necessary.

## Epistemic Status

A2' is a *formulation* — a chosen structural shape for the correction-function geometry that captures "the correction points roughly inward with bounded efficiency." Several structurally distinct shapes would fit the same role (a sign-only condition; a two-point monotonicity; a contraction-rate bound; a non-Euclidean weighted inner-product variant — see *Why Euclidean A2' specifically* in Discussion below). A2' is the canonical choice *matched to the quadratic Lyapunov candidate* $V = \tfrac12\lVert\delta\rVert^2$ used in #deriv-sector-condition, and matched to the gain-based update form on which #der-gain-sector-bridge derives it for sub-scope $\alpha$.

The status is *conditional* because A2' is **derived** for one explicitly named sub-scope of AAT-in-scope agents and **assumed as a per-system empirical claim** for the complementary sub-scope. The Lyapunov derivations downstream of A2' ( #deriv-sector-condition Props A.1, A.1S, A.2; Corollary A.1S.1) apply uniformly across both sub-scopes — they operate downstream of A2' regardless of how it is established. The sub-scope partition is *scope narrowing*, not scope retreat: it makes explicit which agent classes get A2' as a derived consequence of their update geometry, and which classes carry it as a structurally well-scoped posit.

### Sub-scope $\alpha$ (A2' derived)

For a characterized class of AAT-in-scope agents, A2' is a *derived* consequence of the update rule, not a primitive assumption. #der-gain-sector-bridge (Prop B.3) shows that the gain-based update $M_t = M_{t-1} + \eta^\ast g(\delta_t)$ ( #emp-update-gain) induces a correction function satisfying A2' whenever the update rule has **directional fidelity (B1)** — $\delta^T H g(\delta) \geq c_{\min} \lVert\delta\rVert^2$ on $\mathcal B_R$. Sub-scope $\alpha$ — the agent classes where B1 holds structurally — includes:

- *Optimal Bayesian updates* (Kalman, conjugate families): B1 holds by Bayes-risk minimization. $\alpha = \eta^\ast \cdot c_{\min}$, reducing to $\alpha = \eta^\ast$ in the scalar case.
- *Exponential families in natural parameters*, on a bounded interior scope $\Theta_0 \subset \operatorname{int}(\Theta)$: the Hessian is the Fisher information matrix, PD on the interior. $\alpha = \eta \cdot \mu_0$ where $\mu_0 = \inf_{\theta \in \Theta_0} \lambda_{\min}(\mathbf I(\theta)) \gt 0$. Pointwise PD does not imply a uniform global lower bound: $\inf_{\theta \in \Theta} \lambda_{\min}(\mathbf I(\theta))$ can be zero (Poisson: $\mathbf I(\theta) = e^\theta$, $\inf_{\theta \in \mathbb R} e^\theta = 0$), so $\Theta_0$ supplies the local-region scope $R$ that A2' requires. Families with a uniform Fisher floor on $\Theta$ (Gaussian-mean, Beta-Bernoulli) extend to global $\alpha$.
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

The A2' form $\delta^T F \geq \alpha \lVert\delta\rVert^2$ is the sector condition *matched to the quadratic Lyapunov candidate* $V = \tfrac{1}{2}\lVert\delta\rVert^2$ used by #deriv-sector-condition. A converse-Lyapunov argument (Khalil 2002[^khalil2002], Thm 4.17) gives: if persistence holds under the dynamics $\dot\delta = -F(\delta)$ on $\mathcal B_R$, then there exists a quadratic-equivalent Lyapunov function $V_\ast(\delta)$ with $c_1\lVert\delta\rVert^2 \leq V_\ast \leq c_2\lVert\delta\rVert^2$ — but $V_\ast$ may not be the Euclidean norm itself. Under a weighted Lyapunov candidate $V(\delta) = \tfrac{1}{2}\delta^T P \delta$, the natural sector condition is $\delta^T P F(\delta) \geq \alpha\, \delta^T P \delta$; the matrix-Kalman case of #der-gain-sector-bridge is exactly this in the $(P^-)^{-1}$-weighted inner product, with a norm-equivalence transfer to Euclidean A2' degraded by the condition number $\kappa(P^-)$. Euclidean A2' is therefore not the unique sector form — it is the canonical one matched to the canonical $V$. An agent that persists under a non-Euclidean metric satisfies a weighted-sector A2' that transfers to Euclidean A2' only up to norm equivalence. #disc-additive-coordinate-forcing classifies the Lyapunov case as an *adjacent family member* to AAT's three primary additive-coordinate-forcing instances (chain / divergence / update, where a logarithmic coordinate is uniquely forced via Cauchy's functional equation under an AAT-internal additivity axiom): here the quadratic coordinate is matched to the sector form rather than forced by one.

### How downstream segments use this form

- #deriv-sector-condition consumes A2' as the Lyapunov-derivation input: Props A.1 / A.1S / A.2 prove ultimate boundedness, mean-square persistence, and adaptive reserve under (A1), (A2'), (A3); Corollary A.1S.1 establishes the disturbance-model containment dichotomy $P(\tau_R \lt \infty) \in \{0,1\}$.
- #deriv-stochastic-non-exit demonstrates the load-bearing Model-S half of Cor A.1S.1 — that no horizon-independent non-exit bound exists under additive stochastic forcing — using A2' on $\mathcal B_R$ as the Itô-Lyapunov input.
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


---

### Source: `result-sector-condition-stability.md`

```yaml
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
```


# Result: Sector Condition Stability

An agent's mismatch remains bounded if its correction function satisfies a sector condition (points inward with at least baseline efficiency) and the effective correction strength exceeds the environmental disturbance rate.

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


---

### Source: `result-persistence-condition.md`

```yaml
---
slug: result-persistence-condition
type: result
status: exact
depends:
  - def-adaptive-tempo
  - def-mismatch-signal
  - result-sector-condition-stability
  - result-sector-persistence-template
stage: claims-verified
---
```


# Result: Persistence Condition

An agent persists when two independent conditions hold: the correction machinery can contain mismatch within its operating region (*structural persistence*), and the resulting steady-state mismatch is small enough for the agent's actions to remain adequate (*task adequacy*).

## Formal Expression

This segment is the canonical single-agent instantiation of the sector-persistence template ( #result-sector-persistence-template) with state variable $\xi = \delta_t$ (epistemic mismatch), correction function $F(\mathcal{T}, \delta)$, and disturbance rate $\rho_\xi = \rho$ (environmental change rate). Structural persistence is the direct template conclusion. Task adequacy adds a domain-specific constraint beyond the template's reach.

### Structural Persistence

*[Derived (structural-persistence, from sector-persistence-template)]*

Applying the template to the single-agent epistemic case gives: the correction machinery bounds $\delta$ within the model class capacity iff

$$\alpha \gt \frac{\rho}{R} \quad \text{(Model D)} \qquad \alpha \gt \frac{n\sigma_w^2}{2R^2} \quad \text{(Model S)}$$

with ultimate bound $R^\ast = \rho/\alpha$ (Model D) or $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)}$ (Model S). See #result-sector-condition-stability for how (T1)–(T3) are verified in this instantiation, and #deriv-sector-condition for the proof. Structural persistence is a property of the adaptive architecture — the machinery's ability to contain mismatch — not of the task.

**Linear case.** When $F(\mathcal{T}, \delta) = \mathcal{T}\delta$, $\alpha = \mathcal{T}$ and $R \to \infty$, so structural persistence is trivially satisfied whenever $\mathcal{T} \gt 0$. The binding constraint then becomes task adequacy (below).

### Task Adequacy

*[Definition (task-adequacy)]*

The steady-state mismatch is small enough for the agent's actions to remain acceptable:

$$R^\ast \lt \lVert\delta_{\text{critical}}\rVert$$

where $\lVert\delta_{\text{critical}}\rVert$ is a domain-specific tolerance threshold — "how wrong can the model be before the agent's actions become harmful or ineffective?" This is set by the application domain, not derived by AAT.

**Task adequacy is a separate condition from structural persistence.** An agent can be structurally persistent ($R^\ast \lt R$) but task-inadequate ($R^\ast \gt \lVert\delta_{\text{critical}}\rVert$) — the machinery contains mismatch, but not tightly enough for the domain's needs. Conversely, when $\lVert\delta_{\text{critical}}\rVert \lt R$ (the domain's tolerance is stricter than the model class capacity), task adequacy is the binding constraint.

### Operational Persistence Condition

*[Derived (operational-persistence, conjunction of structural persistence + task adequacy)]*

The agent persists operationally when BOTH conditions hold. In the nonlinear case with $\lVert\delta_{\text{critical}}\rVert \lt R$, the binding condition is:

$$\alpha \gt \frac{\rho}{\lVert\delta_{\text{critical}}\rVert} \quad \text{(Model D)} \qquad \alpha \gt \frac{n\sigma_w^2}{2\lVert\delta_{\text{critical}}\rVert^2} \quad \text{(Model S)}$$

These are the same as the structural conditions with $R$ replaced by $\lVert\delta_{\text{critical}}\rVert$, because when $\lVert\delta_{\text{critical}}\rVert \lt R$, task adequacy is stricter.

**Linear operational forms:** In the linear case ($\alpha = \mathcal{T}$, $R \to \infty$), structural persistence is trivially satisfied and the operational condition reduces to task adequacy alone:

$$\mathcal{T} \gt \frac{\rho}{\lVert\delta_{\text{critical}}\rVert} \quad \text{(Model D)} \qquad \mathcal{T} \gt \frac{n\sigma_w^2}{2\lVert\delta_{\text{critical}}\rVert^2} \quad \text{(Model S)}$$

These are the forms used throughout the theory as the operational persistence condition. They are exact for linear correction and useful proxies for mildly nonlinear correction (where $\alpha \approx \mathcal{T}$), but they overstate the persistence margin when the correction function saturates, because they omit the structural constraint ($\alpha \gt \rho/R$) that becomes binding when $R$ is finite.

**Per-dimension (Model S):** $\eta_k \gt c \cdot \rho_k^2 / \delta_{\text{critical},k}^2$ where $c$ depends on the probability guarantee. See #result-per-dimension-persistence.

### The relationship between $\alpha$ and $\mathcal{T}$

#der-gain-sector-bridge shows that for agents with directional fidelity, $\alpha = \eta^\ast \cdot c_{\min}$ where $c_{\min}$ is the worst-case directional fidelity. For linear correction (Kalman, Beta-Bernoulli), $\alpha = \mathcal{T}$ exactly. For gradient descent on strongly convex losses, $\alpha = \eta \cdot \mu$ where $\mu$ is the strong convexity modulus — monotone in $\eta$ (and hence in $\mathcal{T}$) for fixed loss landscape. For nonlinear correction tested in simulation (saturating, sigmoid, threshold), $\alpha$ remains monotone increasing in $\mathcal{T}$: for a saturating function with capacity $R$, $\alpha \approx \mathcal{T}/2$ (worst case at the capacity boundary); for sigmoid (tanh), $\alpha \approx 0.76 \cdot \mathcal{T}$. The qualitative conclusion — "faster adaptation improves persistence" — is structurally grounded for the important cases and empirically confirmed for all correction function classes tested.

### Per-Dimension Extension

*[Empirical Claim (per-dimension-persistence, from simulation variant F)]*

For anisotropic systems (non-uniform $\rho$ or $\mathcal{T}$ across dimensions), the scalar persistence condition is insufficient. Per-dimension:

$$\mathcal{T}_k \gt \frac{\rho_k}{\delta_{\text{critical},k}} \quad \text{for each dimension } k$$

The scalar condition overestimates by up to 72% in simulation. The weak dimension is the bottleneck (84% of total mismatch in simulation). See #result-per-dimension-persistence.

**Robustness**: The per-dimension condition matches discrete AR(1) prediction to 4 significant figures. The scalar overestimate is a consequence of Jensen's inequality applied to the norm.

## Epistemic Status

**Structural persistence** thresholds are *exact* under their stated assumptions: Model D gives $\alpha \gt \rho/R$ (Prop A.1, exact under GA-2, GA-3); Model S gives $\alpha \gt n\sigma_w^2/(2R^2)$ (Prop A.1S, exact under GA-2S, GA-3). The threshold's *existence* is *robust qualitative* — any monotone correction function has a capacity limit; this holds across all correction functions tested.

**Task adequacy** ($R^\ast \lt \lVert\delta_{\text{critical}}\rVert$) is *exact as a definition* — given $R^\ast$ (derived) and $\lVert\delta_{\text{critical}}\rVert$ (domain parameter), the comparison is well-defined. The substance lies in estimating $\lVert\delta_{\text{critical}}\rVert$ for specific domains, which is an operationalization question ( #detail-operationalization), not a theory question.

**The linear operational forms** ($\mathcal{T} \gt \rho/\lVert\delta_{\text{critical}}\rVert$ for Model D; $\mathcal{T} \gt n\sigma_w^2/(2\lVert\delta_{\text{critical}}\rVert^2)$ for Model S) are *exact* for linear correction (where they express task adequacy alone, structural persistence being trivially satisfied) and *useful approximations* for mildly nonlinear correction (where $\alpha \approx \mathcal{T}$). For strongly nonlinear correction, the general $\alpha$-forms are required and BOTH structural and task-adequacy conditions must be checked. Downstream segments that use the linear operational forms should be understood as expressing task adequacy, not structural stability.

The per-dimension extension is *empirically exact* for Model S (matches AR(1) prediction to 4 significant figures in simulation); the Model D per-dimension threshold ($\mathcal T_k \gt \rho_k/\delta_{\text{critical},k}$) is exact by the same Lyapunov argument applied per dimension.

## Discussion

**Two conditions, not one.** This segment now separates what was previously conflated. Structural persistence ($\alpha \gt \rho/R$) is the Lyapunov-derived result — it says the machinery *works*. Task adequacy ($R^\ast \lt \lVert\delta_{\text{critical}}\rVert$) is a domain-specific constraint — it says the machinery works *well enough*. Neither implies the other, and downstream segments should specify which they mean. Most adversarial-dynamics results ( #result-adversarial-tempo-advantage, #der-adversarial-destabilization) depend on structural persistence. Most domain instantiations (TST, logogenic agent design) care about task adequacy. See Persistence in `LEXICON.md` and `README.md` for the full three-sense taxonomy (structural, operational, continuity).

**Below structural threshold.** When $\alpha \leq \rho / R$, mismatch is not merely large — it grows without effective bound (up to $R$, the sector-condition region). The correction machinery is overwhelmed. This is a qualitative transition, not a gradual degradation.

**Below task-adequacy threshold.** When $R^\ast \gt \lVert\delta_{\text{critical}}\rVert$ but $R^\ast \lt R$, the system is structurally stable but performing unacceptably. Mismatch is bounded but too large for the domain. The remedy is different from structural failure: increase $\mathcal{T}$ (faster or better correction), decrease $\rho$ (reduce environmental volatility), or relax $\lVert\delta_{\text{critical}}\rVert$ (accept more mismatch). Structural failure requires changing the correction architecture entirely ( #result-structural-adaptation-necessity).

**$\delta_{\text{critical}}$ and $R$ are domain parameters, not theory outputs.** The theory derives the *existence* of persistence thresholds and their *form* (ratio of correction to disturbance). But the specific values are set by the application domain: $\delta_{\text{critical}}$ encodes "how wrong can the model be before the agent's actions become harmful or ineffective?" — this depends on the stakes, the action space, and the environment's forgiveness. $R$ encodes "how large a mismatch can the correction function handle before it saturates or breaks down?" — this depends on the model class and the correction architecture. See #detail-operationalization for guidance on estimating these quantities in specific domains.

**Channel independence and scalar tempo.** The linear operational forms use scalar $\mathcal{T}$, which inherits the channel-independence assumption from #def-adaptive-tempo: the additive formula overcounts when observation channels are correlated. In anisotropic systems the scalar condition also overestimates margins — up to 72% in simulation (see #def-adaptive-tempo, scalar vs. vector tempo). Where precision matters, the per-dimension condition ($\mathcal T_k \gt \rho_k / \delta_{\text{critical},k}$) should be used instead — and under cross-dimensional correction (off-diagonal $\mathcal{T}$ in the coordinate basis of $D_\delta = \mathrm{diag}(\delta_{\text{critical},k}^2)$), the matrix-Loewner form $\Sigma_\infty \prec D_\delta$ ( #deriv-matrix-persistence-condition) is canonical: per-coordinate is unsafe in that regime (gives a false-pass on persistence), while matrix-Loewner reads persistence correctly off the worst direction whether or not it aligns with a coordinate axis.

**Adaptive reserve.** The quantity $\Delta\rho^\ast = \alpha R - \rho$ (Prop A.2) measures how much additional disturbance the agent can absorb before persistence fails. Positive reserve means the agent has margin; zero reserve means it is at the threshold.

**Persistence has a cost, not just a threshold.** The inequality above says mismatch is bounded; it does not say what rate of effort the agent expends to hold that bound. #deriv-persistence-cost establishes the complementary *information-rate* bound: under Model S with Gaussian-OU signal, the sustained Shannon information rate the agent must acquire from observations to maintain the ultimate bound satisfies $\dot R \geq n\alpha/2$ nats/time — a Landauer-analog floor that Kalman-Bucy saturates. The corollary is a channel-capacity prerequisite $C \geq \mathcal T/2$ that the threshold condition alone does not name. Two agents with identical persistence guarantees can face wildly different sustained demands because the cost scales linearly with $\alpha$; the threshold alone cannot distinguish dormant from running-hot.

### Connections

The persistence condition appears in multiple downstream contexts:

- **Adversarial dynamics** ( #result-adversarial-tempo-advantage): Superlinear tempo advantage arises because persistence is a threshold — pushing an adversary below it causes qualitative collapse. *This connection is developed and validated in #result-adversarial-tempo-advantage and simulation variants A-D.*

- **Structural adaptation** ( #result-structural-adaptation-necessity): When model class fitness $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$, the effective $\alpha$ in the sector condition shrinks, eventually violating persistence. *This connection is developed in #result-structural-adaptation-necessity.*

- **Software maintainability** ( #der-code-quality-as-observation-infrastructure — cross-component reference, see `02-tst-core/`): *[Discussion]* A codebase may become "unmaintainable" when the development team's adaptive tempo falls below the rate of complexity accumulation. The vicious cycle would then be the persistence condition being violated through the agent's own prior actions degrading future $\mathcal{T}$ via $U_o$. *This connection is structurally motivated but not yet formally derived within AAT. It requires formalizing "complexity accumulation rate" as an instance of $\rho$.*

## Findings

### The Persistence Condition with Structural / Task-Adequacy Decomposition

**Brief:** An adaptive system persists when its correction speed beats the rate at which its world is changing, relative to how forgiving the world is. Below this threshold the system doesn't merely degrade — it loses bounded behavior, the way a balance held just barely beneath a tipping point is qualitatively different from one well above it. The same inequality, with different inputs, governs whether a Kalman filter tracks a moving target, whether a development team keeps a codebase maintainable, and whether an organization keeps up with strategic change. The threshold itself decomposes into two distinct conditions — *structural persistence* (the machinery's correction rate can outpace disturbance) and *task adequacy* (the resulting steady-state mismatch is small enough for what the agent is trying to do). Conflating the two leads to category errors in domain transfer.

**Impact:** This is the framework's central inequality and the load-bearing connection between control-theoretic Lyapunov stability analysis and the broader question of when any adaptive system — thermostat, software team, immune system, RL agent — can maintain coherent function under change. The two-condition decomposition is itself non-obvious and consequential: prior work that conflated "the machinery works" with "the machinery works well enough" produced category errors in domain transfer (a structurally persistent codebase team can be task-inadequate; the remedies differ). The complementary information-rate bound from `#deriv-persistence-cost` ($\dot R \geq n\alpha/2$) shows the threshold has a sustained-cost shadow: two agents with identical persistence guarantees can face wildly different sustained demands.

**Novelty Claim:** *Claim synthesis* on Lyapunov stability theory, sector-bounded nonlinear correction, and adaptive-tempo information-rate accounting, applied uniformly across single-agent classes that range from Kalman filtering through saturating nonlinear correction through PID control. The Lyapunov machinery itself is standard; the synthesis is its use as the central inequality of an integrated agent theory, with the two-condition decomposition (structural / task-adequacy) as the AAT-internal contribution that cleanly separates "the machinery works" from "the machinery works well enough."

**Related Work:**

- Khalil 2002, *Nonlinear Systems* (3rd ed.), Prentice Hall (published 2002, found pre-2026) — *formal antecedent* — chapters 4 and 9 supply the converse Lyapunov, ultimate boundedness, and sector-condition machinery the segment uses. Standard control-theoretic apparatus.
- Lyapunov 1892 / Khasminskii 2012 *Stochastic Stability of Differential Equations* — *formal antecedent* — the underlying Lyapunov stability tradition; Khasminskii's stopping-time localization underpins the Model S derivation.
- Rockafellar & Wets 1998, *Variational Analysis* — *formal antecedent* — supplies the monotone-operator machinery that underwrites the sector condition's strong-convexity equivalents.
- Wiener 1948 *Cybernetics*; Ashby 1956 *Introduction to Cybernetics*; Conant & Ashby 1970 — *conceptual precursor* — the cybernetic-feedback tradition that frames the "correction must outpace disturbance" intuition without supplying the quantitative inequality.

**Search Log:**
- 2026-04 (*intuition-only* on broader prior-art): no targeted Undermind-grade search has been conducted on the persistence-condition-as-central-inequality positioning. Pre-search expectation: the Lyapunov-based stability machinery is standard; the AAT-distinctive content is the two-condition decomposition (structural vs task adequacy) and its uniform application across agent classes. A targeted search would query the bounded-rationality / control-theoretic decision-making literature (Ortega-Braun line; Genewein et al.) for prior decompositions of "stability vs adequacy" in adaptive-control settings, and the active-inference literature for the same distinction.
- 2025 (*targeted*): Khalil 2002 / Khasminskii 2012 / Rockafellar-Wets 1998 confirmed as the formal antecedents for the sector-Lyapunov machinery; the segment cites them inline.


---

### Source: `result-sector-persistence-template.md`

```yaml
---
slug: result-sector-persistence-template
type: result
status: exact
depends:
  - deriv-sector-condition
stage: draft
---
```


# Result: Sector-Persistence Template

Any state variable evolving under bounded-correction dynamics with bounded disturbance admits the same Lyapunov persistence argument. AAT's persistence-flavored results — epistemic, strategic, team, composite closure, composite tempo, adversarial destabilization, and identity-continuity across turnover — are instances of a single template. This segment states the template once in parameter-free form so that each instantiation can cite it and specify only what varies: its state variable, correction function, effective disturbance rate, and reserve.

## Formal Expression

*[Template preconditions (sector-persistence-template)]*

Let $\xi(t) \in \mathbb{R}^n$ be a state variable evolving under

$$\frac{d\xi}{dt} = -F(\xi) + w(t)$$

where $F$ is a correction function and $w(t)$ is a disturbance. The template applies when:

**(T1) Zero correction at zero state.** $F(0) = 0$ — no correction is applied when the state is at its target.

**(T2) Local sector condition.** There exist $\alpha \gt 0$ and $R \gt 0$ such that

$$\xi^T F(\xi) \geq \alpha \lVert\xi\rVert^2 \quad \text{for } \lVert\xi\rVert \leq R.$$

The correction points inward with at least baseline efficiency $\alpha$ throughout the region of radius $R$.

**(T3) Bounded disturbance.** Either:

- *Model D (deterministic bound):* $\lVert w(t)\rVert \leq \rho_\xi$, or
- *Model S (stochastic zero-mean):* $\mathbb{E}[\lVert w(t)\rVert^2] = \sigma_\xi^2$ with $w(t)$ a Wiener-process increment.

*[Template result (from sector-condition-derivation Props A.1, A.1S, A.2)]*

Under (T1)–(T3), with $V(\xi) = \tfrac{1}{2}\lVert\xi\rVert^2$ as Lyapunov function:

**Model D.** The state is ultimately bounded by $R^\ast = \rho_\xi / \alpha$. Structural persistence (the ultimate bound fits within the sector-condition region) requires

$$\alpha \gt \frac{\rho_\xi}{R}.$$

The adaptive reserve — the additional disturbance the system can absorb before persistence fails — is $\Delta\rho_\xi^\ast = \alpha R - \rho_\xi$.

**Model S.** The state satisfies $\mathbb{E}[\lVert\xi(t)\rVert^2] \to n\sigma_\xi^2/(2\alpha)$ in mean square, giving RMS bound $R^\ast_S = \sigma_\xi\sqrt{n/(2\alpha)}$. Structural persistence in the mean-square sense requires

$$\alpha \gt \frac{n\sigma_\xi^2}{2R^2}.$$

The Model D result scales as $1/\alpha$; the Model S result scales as $1/\sqrt{\alpha}$ — correction is less effective against noise than against drift. This scaling difference propagates into the adversarial exponent regimes ( #result-adversarial-exponent-regimes): $b = 2$ under Model D, $b = 3/2$ under Model S.

### Instantiations in AAT

The template is invoked across seven segments. Each specifies its own $(\xi, F, \rho_\xi, R)$ and verifies (T1)–(T3) locally:

| Segment | $\xi$ | Effective $\rho_\xi$ | $R$ | Locally-verified precondition |
|---|---|---|---|---|
| #result-persistence-condition | $\delta_t$ (epistemic mismatch) | $\rho$ (environmental disturbance rate) | model-class capacity, or task-adequacy threshold $\lVert\delta_{\text{critical}}\rVert$ if stricter | (T2) via #der-gain-sector-bridge |
| #schema-strategy-persistence | $\delta_\Sigma$ (strategic mismatch) | $\rho_\Sigma$ (rate of edge invalidation) | $R_\Sigma$ (strategic reserve) | (T2) via Beta-Bernoulli edge updates ( #deriv-edge-credence-dynamics Props B.1–B.6); constant-$\alpha$ requires experience discounting |
| #der-team-persistence | $\delta_i$ (sub-agent mismatch) | $\rho_i^{\text{eff}} = \rho_{i,\text{env}} + \sum_j \gamma_{j\to i}^{\text{adv}}\mathcal T_j - \sum_j \gamma_{j\to i}^{\text{coop}}\mathcal T_j$ | $R_i$ | Cooperative coupling can drive $\rho_i^{\text{eff}}$ below the single-agent $\rho$ |
| #form-composition-closure (bridge lemma) | $e_m$ (trajectory error at macro-boundaries $m$) | $\varepsilon^\ast \nu_c$ (closure-defect per macro-step $\times$ macro-update rate) | the composite's $R_c$ | Tier-specific contraction stronger than (T2): incremental sector bound (DA2'-inc). Tier 1 proved; Tier 2 local; Tier 3 domain-specific |
| #der-tempo-composition | $\delta_c$ (composite mismatch) | $\rho_{\text{ext}} + \varepsilon^\ast \nu_c$ (external + internal) | $R_c$ | (T3) requires the bridge-lemma contraction; $C_{\text{coord}} \geq \varepsilon^\ast\nu_c$ is the tempo-equivalent of the internal disturbance |
| #der-adversarial-destabilization | $\delta_B$ (target-agent mismatch) | $\rho_{B,\text{base}} + \gamma_A \mathcal T_A$ (Model D) or $\sigma_{B,\text{base}} + \gamma_A \mathcal T_A$ (Model S) | $R_B$ | Destabilization is the negation of persistence: (T3)'s coupling-amplified disturbance violates $\alpha R \gt \rho_\xi$ |
| #der-identity-continuity-threshold | $g_k$ (identity gap, turnover-indexed) | $\rho_k$ (projected static identity rate-distortion floor, per boundary) | $D_\Delta$ (fidelity-bounded identity-relevant information) | The reflected (Lindley) discrete instantiation on the turnover axis; compensation is relational re-grounding $\varrho_{\text{rg},k}$; Model-S-family, $\mu=0$ driftless boundary load-bearing; conditional under (M-ADD)/(M-FREE)/(C-S) — the $\mathcal A_{\mathrm{refl}}$ operator family (see Discussion) |

The same Lyapunov argument applies in every row. What varies is how each instantiation defines its state variable, its correction function, and — most importantly — what counts as "effective disturbance" for its context (environmental noise, adversarial coupling, closure defect, or a decomposition of these).

### External mathematical lineage: monotone-operator theory

The sector-Lyapunov apparatus this segment factors out has a well-established mathematical home: AAT's sector condition (T2) is a **one-point strong monotonicity** condition in the sense of Rockafellar 1970 (*Convex Analysis*, §24) anchored at the equilibrium $\xi^\ast = 0$, and the incremental strengthening DA2'-inc required by `#form-composition-closure`'s bridge lemma is **full two-point strong monotonicity** in the Bauschke-Combettes 2017 (*Convex Analysis and Monotone Operator Theory in Hilbert Spaces*, 2nd ed., §§22–28) monotone-operator framework. The Lyapunov-plus-Grönwall argument proving the Model D ultimate bound and the Itô-Lyapunov argument proving Prop A.1S are standard specializations of the **monotone-operator perturbation theorem** (Bauschke-Combettes Thm 5.14–5.16; Parikh & Boyd 2014, *Proximal Algorithms*, §2). Banach-Picard contraction under bounded perturbation, monotone-operator convergence under square-summable noise, operator-splitting for composite systems (Douglas-Rachford, ADMM) — the full supporting apparatus is available in that literature.

AAT's relationship to monotone-operator theory is *specialization + repurposing*, not generalization. AAT-distinctive content: (i) **one-point anchoring at the equilibrium** — strictly weaker than full two-point strong monotonicity, matched to fixed-point-at-target semantics, admitting agent classes (PID-bounded-plant, variational-approximate) where full monotonicity fails but persistence-at-the-target is available. (ii) The **Model D / Model S disturbance decomposition** with distinct $1/\alpha$ vs $1/\sqrt\alpha$ scaling — monotone-operator theory has perturbation theorems but no systematic bounded-adversarial vs stochastic-zero-mean split propagating to adversarial-exponent regimes at $b = 2$ vs $b = 3/2$. (iii) Composition with the `#disc-identifiability-floor` meta-pattern supplies a second (information-theoretic) axis orthogonal to the operator-theoretic machinery. (iv) The `#post-composition-consistency` postulate operates at AAT's level of description (agent / composite / macro-agent) rather than at the abstract operator level. (v) The sub-scope $\alpha$/$\beta$ epistemic labeling is scope-honesty, not a mathematical partition — it tracks which agent classes give the monotone-operator structure *by construction* versus *by per-instance verification*.

This acknowledgment is load-bearing for scope honesty: the mathematical machinery is established external to AAT; AAT's distinctive content is the agent-architecture specialization (singular-trajectory identity per `#scope-agent-identity`; signed-coupling composition; coordinate-forcing via uniqueness theorems per `#disc-additive-coordinate-forcing`; three meta-patterns) rather than novel monotone-operator mathematics. `#deriv-sector-condition`'s Grounding paragraphs name the specific operator-family correspondence (proximal / firmly-nonexpansive / cocoercive / strongly-monotone-gradient / linear-PD) for the five sub-scope-$\alpha$ agent classes. `#result-contraction-template` extends to non-Euclidean metrics via Lohmiller-Slotine differential-contraction (also within the broader monotone-operator lineage). The honest limits of the unification: the coarse-graining projection $\Lambda$ ( #form-composition-closure) does not fit the operator-sector primitive (heterogeneous spaces, three independent admissibility conditions); three of five metric-$\alpha_2$ cases in `#result-contraction-template` remain theorem-imported rather than AAT-internally derived; the identifiability-floor axis is orthogonal to the operator-sector axis.

### Comparison with the FEP-flow stability argument

Active inference's stability arguments come from the geometry of the variational free-energy landscape — agents are argued to flow toward the minimum of variational free energy on a non-equilibrium-steady-state (NESS) density. The primary source for the NESS-density framing is Friston 2019, "A free energy principle for a particular physics," arXiv:1906.10184; the path-integral / particular-kinds methodological extension is Friston, Da Costa, Sakthivadivel, Heins, Pavliotis, Ramstead & Parr 2023, "Path integrals, particular kinds, and strange things," *Phys. Life Rev.* 47 (which rewrites the FEP-flow argument in path-integral language rather than proving new stability bounds). Aguilera, Millidge, Tschantz & Buckley (2022, "How particular is the physics of the free energy principle?", *Phys. Life Rev.* 40:24–50) showed that the FEP-flow argument's mathematical validity is narrow: the NESS-density framing holds only in a small parameter regime for non-equilibrium linear stochastic systems, and natural extensions (nonlinear, non-Gaussian, non-equilibrium) often fall outside the proven regime.

The AAT persistence template is structurally different: it is a Lyapunov-based argument requiring only (T1) zero-correction-at-zero-state, (T2) local sector condition (correction points inward), and (T3) bounded disturbance — all of which are checked locally for each instantiation ( #deriv-sector-condition Props A.1, A.1S, A.2). The template applies to bounded and to mean-square-stochastic disturbance, gives explicit ultimate-bound and adaptive-reserve formulas, and does not depend on NESS structure or on a free-energy gradient.

The breadth difference is not rhetorical: where the FEP-flow argument's parameter regime is debated in the AI literature itself, the sector-Lyapunov apparatus is the standard machinery of nonlinear control theory (Khalil 2002, *Nonlinear Systems*, 3rd ed., Prentice Hall, ch. 4) and applies wherever (T1)–(T3) hold. This is one of AAT's stronger structural positions and is worth making explicit when comparing AAT to active inference: AAT does the persistence work AI tries to do, with broader validity and explicit ultimate-bound formulas.

## Epistemic Status

*Exact.* The template is the abstract form of the Lyapunov result proved in #deriv-sector-condition (Props A.1, A.1S, A.2). The proofs transfer without modification whenever (T1)–(T3) hold; the template's contribution is the recognition that AAT's persistence-flavored results are instances of a single pattern and the enumeration of what each instantiation must verify.

**On (T2) and A2' sub-scoping.** (T2) is the local sector condition A2' transcribed to a generic state variable $\xi$. Within the state-variable spaces relevant to AAT's instantiations (epistemic mismatch $\delta$, strategic mismatch $\delta_\Sigma$, sub-agent mismatch $\delta_i$, composite trajectory error $e_m$, composite mismatch $\delta_c$, target-agent mismatch $\delta_B$), the update rules are overwhelmingly sub-scope $\alpha$ in the #form-sector-condition / #der-gain-sector-bridge sense — Bayesian, exponential-family, strongly-convex-gradient, or linear-PD. For these, (T2) is *derived* from the update-rule structure under B1 directional fidelity. **Important, and easy to miss: this is not what carries forward universally.** For sub-scope $\beta$ instantiations (e.g. a team with a rule-based sub-agent) (T2) is an *empirical precondition, verified per-instantiation*, not derived. That distinction scopes which instantiations satisfy (T2) by which route; it does not touch the template's exactness, which is the conditional "(T1)–(T3) $\Rightarrow$ persistence" — anything satisfying (T2) by either route inherits the exact result.

**On Prop A.1S region-awareness.** The Model S case uses the region-aware form of Prop A.1S (stopped second-moment bound + the fixed-time tail $P(\lVert\xi(t)\rVert \gt R) \leq \text{const}$ under the mean-square persistence condition). Instantiations that rely on the Model S result automatically inherit the stopping-time localization — no extra work is required at the template level. As at #deriv-sector-condition, Model S provides a distributional / fixed-time guarantee, not pathwise-forever containment (which is a Model-D-only guarantee); template instantiations inherit that kind-of-guarantee distinction, not an infinite-horizon non-exit bound.

Max attainable: *exact*. The result is as strong as Lyapunov stability theory. Additional work could extend the template (state-dependent noise, time-varying $\alpha$, non-quadratic Lyapunov functions) but would not strengthen it within its stated scope.

**What the template does not establish:**

- *Quantitative convergence rates.* Lyapunov gives stability and ultimate bounds, not convergence speed. Specific rates require instantiation-level analysis.
- *Behavior outside the sector-condition region.* (T2) holds only for $\lVert\xi\rVert \leq R$. Beyond $R$, correction may break down — the structural-adaptation regime of #result-structural-adaptation-necessity.
- *Time-varying parameters.* The template assumes constant $\alpha$ and $R$. Time-varying cases require additional machinery. #schema-strategy-persistence documents the most important AAT example: $\alpha_\Sigma = 1/(n+1)$ decays with experience, so strategic persistence requires experience discounting at rate $(1-\lambda) \gt \rho_\Sigma/R_\Sigma$ to recover constant-$\alpha$.
- *Heavy-tailed disturbances.* Neither (T3-D) nor (T3-S) covers disturbances with unbounded moments. Extreme tail events are better handled as triggers for structural adaptation than as disturbances the template can absorb.

## Discussion

**Why factor this out.** Every persistence-flavored result in AAT takes the form "correction rate exceeds effective disturbance rate (relative to reserve)" and is proved by the same Lyapunov function $V(\xi) = \tfrac{1}{2}\lVert\xi\rVert^2$. Stating the argument once, parameter-free, makes visible that the theory is *one result about bounded-correction dynamics applied to several state spaces*, not six separately-proved results that happen to look alike.

Each instantiation's distinctive content is now sharply visible: *what is the state variable, and what counts as its effective disturbance?* The Lyapunov machinery is shared; the characterization of $\rho_\xi$ is where the domain-specific insight lives. Adversarial destabilization's content is the coupling term $\gamma_A \mathcal T_A$; team persistence's content is the cooperative-minus-adversarial decomposition; composition closure's content is the closure-defect rate $\varepsilon^\ast \nu_c$. In each case, the template absorbs the Lyapunov boilerplate and lets the distinctive claim stand without it.

This template is the *interior facet* of the stability certificate ( #disc-stability-certificate): the "correction rate exceeds effective disturbance rate" condition is the certificate being positive-definite on the scope ball, and the existence of such a certificate is equivalent to exponential stability ( #result-certificate-existence). The shared Lyapunov function $V(\xi)=\tfrac12\lVert\xi\rVert^2$ is the certificate in the Euclidean metric; #result-contraction-template carries the non-Euclidean-metric interior.

**The template is the typed-bridge shared upstream — two-model, not one operator.** This template is the canonical anchor of the *accumulation typing* convention ( `NOTATION.md` §"Accumulation typing"): the bridge from a per-step residue to its accumulated consequence *is* this conditional. The bridge is **two-model, not a single bounded operator** — (T3)'s Model D and Model S are co-equal, and the $1/\alpha$ vs $1/\sqrt\alpha$ scaling (line above) plus the Cor-A.1S.1 categorical containment dichotomy ( #deriv-sector-condition) are the structural fingerprint that they are *different functionals*, not one functional read in two norms (a change of $\alpha$-homogeneity *degree* cannot come from a norm choice on a fixed operator). The across-turnover axis is the worked demonstration that the split is structural, with two operator families at *opposite ends of the same singular contraction parameter*, **neither superseding the other**: the $\mathcal A_{\mathrm{refl}}$ family — a reflected (Lindley/Loynes) walk whose load-bearing content is its driftless $\mu=0$ boundary — *instantiates* the template on the turnover index ( #der-identity-continuity-threshold, the new row above); the $\mathcal A_D$ family — the linear destroy-and-reconstruct contraction whose affine norm *diverges* exactly as the contraction gap closes — is the **honest scope boundary where the template provably does *not* transfer** ( #der-turnover-information-recursion: an unforced multiplicative information decay has no correction function pointing a perturbed state inward, so (T1)–(T3) have no counterpart; the non-transfer is a definite result, not a caveat). The $\mu=0$ boundary of the $\mathcal A_{\mathrm{refl}}$ instantiation *is* the singularity of the $\mathcal A_D$ regime — you cannot linearize across that pole, which is why the two are distinct operators and the accumulation-type confound (treating one as a normalization or linearization of the other) is a category error, independently adjudicated ( `spikes/adjudicate-disc-m-preservation-operator.md`). The typing convention exists precisely so this — *which model, which operator family* — is carried in the notation rather than silently reconstructed.

**What each instantiation must still verify.** Invoking the template is not trivial. Each instantiation must establish (T1)–(T3) for its specific $(\xi, F, \rho_\xi, R)$, and the non-trivial verifications differ substantively:

- *Strategic persistence* ( #schema-strategy-persistence): (T2) is verified for Beta-Bernoulli edge updates across five DAG topologies ( #deriv-edge-credence-dynamics Props B.1–B.6). But $\alpha_\Sigma = 1/(n+1)$ is time-varying: it decays monotonically with experience. Constant-$\alpha$ — and therefore the template's trajectory guarantee — requires experience discounting as a prerequisite, not a heuristic.
- *Composition closure* ( #form-composition-closure): (T2) as stated is insufficient. The bridge lemma requires the *incremental sector bound* (DA2'-inc) — strongly monotone $F$ across the whole state space, strictly stronger than the one-point sector bound (T2). Three agent tiers result: Tier 1 where contraction is proved for the full class (Bayesian on exponential families, gradient descent on strongly convex losses, linear correctors with positive-definite gain), Tier 2 where it holds locally, Tier 3 where it must be verified per-domain.
- *Team persistence* ( #der-team-persistence): (T3) is the decomposition $\rho_i^{\text{eff}} = \rho_{i,\text{env}} + \sum_j \gamma_{j\to i}^{\text{adv}}\mathcal T_j - \sum_j \gamma_{j\to i}^{\text{coop}}\mathcal T_j$. Cooperative coupling enters through a negative term, which can drive $\rho_i^{\text{eff}}$ below the single-agent $\rho$ — this is formally how teams persist where individuals cannot.

**Persistence and destabilization as one result.** Adversarial destabilization ( #der-adversarial-destabilization) is the template applied with coupling-amplified disturbance: $\rho_B = \rho_{B,\text{base}} + \gamma_A \mathcal T_A$. The "destabilization threshold" — the condition under which agent $A$ pushes agent $B$ past its stability boundary — is precisely the *negation* of the template's persistence condition for $B$'s instantiation. $B$ persists iff $\alpha_B R_B \gt \rho_B$; $B$ destabilizes iff $\rho_B \gt \alpha_B R_B$. These are the same inequality viewed in opposite directions, not independent results. The superlinear adversarial scaling ($b=2$ under Model D, $b=3/2$ under Model S) follows from the template's $1/\alpha$ vs $1/\sqrt{\alpha}$ scaling without further derivation.

**Signed-coupling pattern across instantiations.** The six instantiations above — plus #deriv-critical-mass-composition, which derives a closed-form composite (T2) for the matched-symmetric-Tier-1 dyad — share a signed-coupling structure: each effective $\rho_\xi$ is a sum of environmental disturbance plus a cross-agent contribution whose sign encodes cooperative vs adversarial coupling. Team persistence, composition closure (via bridge-lemma), tempo composition, adversarial destabilization, and composite critical-mass are instances of one inequality at different state-variable levels. The template is where this pattern lives at the meta level; the per-segment instantiations supply the domain-specific $(\xi, F, \rho_\xi, R)$ quadruples.

**Cost complement: the template's information-rate floor.** Alongside the threshold condition, each instantiation inherits an information-rate lower bound from #deriv-persistence-cost: under Model S with Gaussian-OU-shaped disturbance statistics on $\xi$, the sustained information rate required to maintain $\mathbb E[\lVert\xi\rVert^2]_{ss}$ at the ultimate bound satisfies $\dot R \geq n\alpha/2$ nats/time with the instantiation's own $(\alpha, n, \sigma_\xi^2)$. For the epistemic-mismatch instance, this translates to the channel-capacity floor $C \geq \mathcal T/2$ — a first-class persistence prerequisite that the threshold condition alone does not surface. Each instantiation can derive its own cost bound by direct substitution into the main theorem of #deriv-persistence-cost; the consolidation of this into a parametric template-cost subsection is flagged in that segment's Working Notes.

**The coordination overhead $C_{\text{coord}}$ is effective disturbance at the composite level.** The tempo-composition inequality $\mathcal T_c \leq \sum_i \mathcal T_i$ has a lower bound on the gap: $C_{\text{coord}} \geq \varepsilon^\ast \nu_c$ ( #der-tempo-composition). This is the template's instantiation with $\xi = \delta_c$ and effective disturbance $\rho_{\text{ext}} + \varepsilon^\ast \nu_c$ — the composite's internal closure error acts as an additional disturbance at the macro level, absorbing correction capacity that would otherwise address the external environment. Brooks's Law follows as an instance: adding agents increases $\sum_i \mathcal T_i$ but may increase $\varepsilon^\ast \nu_c$ faster, pushing $\rho_c^{\text{eff}}$ above $\alpha_c R_c$.

**Relationship to #result-persistence-condition.** #result-persistence-condition is the canonical single-agent instantiation. It carries additional content beyond the template — *task adequacy*, a domain-specific constraint $R^\ast \lt \lVert\delta_{\text{critical}}\rVert$ that further restricts the usable region — and it instantiates the template in the linear special case where $F = \mathcal{T}\delta$, $\alpha = \mathcal{T}$, and (T2) holds globally. Task adequacy is not part of the template because it is not part of the Lyapunov argument; it is an application-level constraint the agent's domain imposes.

**Relationship to #post-composition-consistency.** The composition-consistency postulate requires that AAT's predictions be compatible across levels of description. The template is how this compatibility cashes out operationally: the same persistence argument applies at every level where a state variable with a sector-bounded correction function is present. Section III segments that invoke the template (team persistence, composition closure, tempo composition) are applying AAT's single persistence argument at the composite level, with effective disturbance decompositions that capture what is distinctive about the composite scope.

**Relationship to #result-contraction-template (metric-formulation generalization).** The Euclidean sector inequality (T2) is the $M = I$ specialization of a broader contraction-metric condition (CT2) under a Riemannian metric $M$ (Lohmiller & Slotine 1998). For several AAT-relevant agent classes, the natural Lyapunov lives in a non-Euclidean metric — Fisher for statistical-manifold learning (matrix Kalman in information metric; exponential family in natural parameters), Hessian-induced for ill-conditioned strongly-convex optimization, Lyapunov-equation-determined for asymmetric-stable linear systems, or Lyapunov-metric for PID-with-bounded-plant-nonlinearity. #result-contraction-template states the generalization once with (CT1)–(CT3) preconditions matching (T1)–(T3), adds compositional theorems (parallel / cascade / negative-feedback with small-gain) that extend `#deriv-critical-mass-composition` (CM2) to heterogeneous sub-agents via (CM2-M), and fills `#disc-separability-pattern`'s seventh ladder (A2'-scope into metric-$\alpha_1$ / metric-$\alpha_2$ / metric-$\beta$). The Euclidean formulation stated in this segment remains the default for Euclidean-natural instances; #result-contraction-template is invoked when the natural coordinate is non-Euclidean. Structural consequence worth noting: the (CT2) condition at $M = I$ is equivalent to `#form-composition-closure`'s DA2'-inc (incremental sector bound), so AAT has been carrying the Jacobian-level Euclidean contraction condition at the composite level all along; #result-contraction-template makes this explicit at the single-agent level.

## Working Notes

- The template is type `result` because it states a result abstractly; the proof lives in #deriv-sector-condition (the canonical instance for $\delta$), and the transfer to other state variables is routine once (T1)–(T3) are verified. Treating it as a `formulation` would misrepresent its status — the Lyapunov argument does not leave room for alternative formulations within its stated scope.
- Candidate extensions that would strengthen the template: (i) time-varying $\alpha(t)$ with lower bound, for the strategic case; (ii) state-dependent noise intensity, for cases where the disturbance magnitude depends on the current mismatch; (iii) non-quadratic Lyapunov functions, for richer stability regions. Each is a real extension of Lyapunov theory, not specific to AAT.
- The template's role in #post-composition-consistency's "applies at every level" claim is now explicit: the claim holds at every level where (T1)–(T3) can be verified for the level's state variable. This sharpens the composition postulate from "applies at every level" to "applies at every level the template applies to," which is a testable condition rather than a universal assertion.


---

### Source: `deriv-persistence-cost.md`

```yaml
---
slug: deriv-persistence-cost
type: derivation
status: conditional
depends:
  - result-persistence-condition
  - result-sector-condition-stability
  - deriv-sector-condition
  - result-sector-persistence-template
  - def-adaptive-tempo
  - emp-update-gain
  - der-gain-sector-bridge
  - def-model-class-fitness
stage: draft
---
```


# Derivation: Persistence Cost — Information Rate to Maintain Bounded Mismatch

AAT's persistence machinery establishes that under the sector condition, mismatch stays bounded. It does not quantify the *sustained rate of effort* an agent must expend to hold that bound. Two agents with identical persistence guarantees can face wildly different demands — a Kalman filter tracking a stationary process vs one tracking a rapidly non-stationary process are both persistent; one is dormant, the other running hot. Under Model S with Gaussian-OU signal, the sustained Shannon information rate the agent must acquire from observations to maintain the sector-persistence ultimate bound is $\dot R_{\min} \geq n\alpha/2$ nats per unit time — a Landauer-analog lower bound that depends only on the signal's second-order statistics and the sector constant $\alpha$, and that Kalman-Bucy saturates in steady state. The bound promotes channel capacity $C \geq \mathcal T/2$ into a first-class persistence prerequisite that the current theory does not name.

## Formal Expression

### Setup

The agent is in scope of #result-sector-condition-stability Model S (GA-2S, stochastic disturbance).
Per Prop A.1S the state satisfies $\mathbb E[\lVert\delta\rVert^2]_{ss} = n\sigma_w^2/(2\alpha)$.
The RMS bound is $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)}$.
The environmental signal is $n$-dimensional independent-component Ornstein-Uhlenbeck with per-component intrinsic drift $\lambda_s$ and diffusion coefficient $\sigma_w^2$.
The mean-square persistence condition $\alpha \gt n\sigma_w^2/(2R^2)$ holds.
Sector-persistence is achieved at the tight bound $D^2 = R^{\ast 2}_S$.

### Persistence Information Rate (main theorem)

*[Proved (persistence-information-rate, from Shannon RDF + Prop A.1S)]*

**Proposition.** Any adaptive process achieving the tight Model-S ultimate bound $\mathbb E[\lVert\delta\rVert^2]_{ss} = n\sigma_w^2/(2\alpha)$ under the stated setup must acquire information from observations at sustained rate

$$\boxed{\;\dot R \;\geq\; \dot R_{\min} \;=\; \frac{n\alpha}{2} \text{ nats per unit time}\;}$$

**Derivation.** Shannon's rate-distortion theorem (Shannon 1948; Berger 1971; Cover & Thomas 2006 Theorem 10.2.1) states that for any source-code achieving mean-square distortion $D^2$, the coding rate satisfies $\dot R \geq R(D^2)$ where $R(\cdot)$ is the rate-distortion function. For $n$-dimensional independent-component OU in the high-resolution regime ($D^2 \ll \sigma_x^2 = \sigma_w^2/(2\lambda_s)$), the RDF per unit time is (Ihara 1993 Theorem 4.6.4; Gray 1972 Theorem 2):

$$\dot R(D^2) = \frac{n\sigma_w^2}{4 D^2}$$

Substituting $D^2 = R^{\ast 2}_S = n\sigma_w^2/(2\alpha)$:

$$\dot R_{\min} = \frac{n\sigma_w^2}{4 \cdot n\sigma_w^2/(2\alpha)} = \frac{\alpha}{2} \cdot 1 = \frac{n\alpha}{2} \text{ nats per unit time}$$

(the calculation gives $\alpha/2$ per dimension and $n\alpha/2$ total for $n$ independent OU components). The agent's observation-channel information rate must meet this bound regardless of the specific correction function, filter structure, or implementation. $\square$

### Kalman-Bucy Saturates the Bound

*[Derived (Kalman-tight, Mitter-Newton 2005)]*

The Kalman-Bucy filter attains the bound exactly in steady state. Mitter & Newton (2005, *J. Stat. Phys.* 118:145–176) derive the filter's rate of information supply as

$$\dot I = \tfrac{1}{2}\operatorname{tr}(H^T \Sigma_o^{-1} H P_{ss})$$

Scalar case ($H = 1$, $\Sigma_o = \sigma_o^2$) with steady-state covariance $P_{ss} = \sigma_o \sigma_w$ in the drift-dominated limit and Kalman gain $K_{ss} = P_{ss}/\sigma_o^2 = \sigma_w/\sigma_o$:

$$\dot I = \frac{P_{ss}}{2\sigma_o^2} = \frac{K_{ss}}{2} = \frac{\alpha}{2}$$

Under the linear-correction identification $\alpha = K_{ss}$ (from #der-gain-sector-bridge, scalar Kalman case), the Kalman filter's information supply rate equals $\alpha/2$ exactly. This matches the RDF lower bound, confirming tightness. **The bound is not merely a lower bound — it is achieved by the Kalman-optimal filter.**

### Channel-Capacity Prerequisite

*[Derived (channel-capacity-floor, from main theorem + Shannon capacity)]*

By Shannon's channel coding theorem (Cover & Thomas 2006 §7.7), an observation channel of Shannon capacity $C_{\text{channel}}$ can support any information rate up to $C_{\text{channel}}$ and no higher. Combining with the persistence information rate:

$$C_{\text{channel}} \;\geq\; \dot R_{\min} \;=\; \frac{n\alpha}{2}$$

Under the linear-correction identification $\alpha = \mathcal T$ (from #def-adaptive-tempo + #der-gain-sector-bridge scalar Kalman):

$$\boxed{\;C_{\text{channel}} \;\geq\; \mathcal T / 2 \text{ nats/time per dimension}\;}$$

**Persistence demands observation-channel capacity at least half the adaptive tempo.** This is a *new first-class persistence diagnostic* not present in the current theory. Its binding matters most in capacity-constrained settings — bandwidth-limited distributed systems, biological neurons, context-window-limited LLMs — where the tempo framework alone underestimates the difficulty of maintaining bounded mismatch.

### Rejected Candidate Cost Metrics

The information-rate bound is not the only candidate for a cost-of-persistence quantity. Three alternatives fail structurally. Recording them here keeps the scope-honesty visible.

*[Observation (gain-magnitude-tautological)]* $\mathbb E[\lVert K(t)\rVert]$ as a cost metric: in the linear Kalman case $K_{ss} = \alpha$ (sub-scope $\alpha$ per #der-gain-sector-bridge), so "gain magnitude" equals the sector constant itself. Any bound of shape $\mathbb E[\lVert K\rVert] \geq f(\alpha, \ldots)$ becomes tautological. Rejected as fundamental cost metric — it recapitulates $\alpha$.

*[Observation (control-effort-filter-specific)]* $\mathbb E[\lVert u(t)\rVert^2]$ (per-unit-time control-effort integral): filter-specific. Different filters achieving the same steady-state variance $P_{ss}$ have different control-effort integrals. The Kalman filter is minimum-effort among linear filters (optimal-control interpretation of the Riccati equation); nonlinear filters can trade effort vs variance differently. A filter-agnostic bound cannot be stated in this quantity — it is not invariant under the equivalence class of filters meeting the persistence condition.

*[Observation (Lyapunov-dissipation-conservation)]*
$\mathbb E[\alpha\lVert\delta\rVert^2]_{ss}$ (Lyapunov dissipation rate) at steady state equals $n\sigma_w^2/2$ regardless of $\alpha$ — a non-equilibrium-steady-state conservation law (dissipation balances disturbance-power injection).
The quantity is *structurally invariant*: it does not depend on the quality of adaptation, only on the disturbance statistics.
This is what makes the RDF bound tight at the Model-S ultimate bound (the steady state is active, not slack), but it cannot itself serve as a cost metric because it does not distinguish well-adapted from poorly-adapted agents at a given $\alpha$.

Candidate 4 — the Shannon information rate above — is the one that closes. The structural reason: information rate is filter-agnostic (depends only on signal second-order statistics and target distortion), universal (any filter implementation is lower-bounded), and has a clean thermodynamic interpretation (Still et al. 2012, "Thermodynamics of Prediction", *Phys. Rev. Lett.* 109:120604: nonpredictive information retained equals dissipation during interaction).

### What Is Derived vs. What Is Chosen

| Property | Source | Strength |
|---|---|---|
| Persistence information rate $\dot R_{\min} \geq n\alpha/2$ | Shannon RDF (Berger 1971; Gray 1972; Ihara 1993 Thm 4.6.4) composed with Prop A.1S | Derived (conditional on Model S + Gaussian-OU + high-resolution regime) |
| Kalman-Bucy saturates bound | Mitter-Newton 2005 Theorem (information-supply identity); linear-correction identification $\alpha = K_{ss}$ per #der-gain-sector-bridge | Derived (linear-Gaussian; exact when A2' is derived in sub-scope $\alpha$) |
| Channel-capacity prerequisite $C \geq \mathcal T/2$ | Main theorem + Shannon channel-capacity theorem (Cover-Thomas 2006 §7.7) + $\alpha = \mathcal T$ identification | Derived |
| Gain-magnitude as cost metric | $\mathbb E[\lVert K\rVert] \approx \alpha$ in sub-scope $\alpha$ | Rejected as fundamental (tautological) |
| Control-effort integral as cost metric | Filter-specific; depends on optimality class | Rejected as universal (filter-dependent) |
| Lyapunov dissipation rate | Conservation law $= n\sigma_w^2/2$ at steady state | Not a cost metric — structural observation enabling tightness of main theorem |
| Non-Gaussian signal extension | Different RDF form (Berger 1971 Ch. 4) | Open — qualitative scaling $\dot R \propto$ innovation-rate/$D^2$ likely preserved; exact prefactor changes |
| Model D (bounded disturbance) analog | Requires adversarial / minimax information argument (Csiszár-Körner 2011 Ch. 11) | Open |
| Transient-regime rate | Bound is steady-state; transient rates during structural adaptation much higher | Open |
| Sub-scope $\beta$ transfer | RDF bound holds as inequality (data-processing); tightness not guaranteed | Conditional (holds as lower bound; Kalman-Bucy saturation requires sub-scope $\alpha$) |

## Epistemic Status

*Conditional.* Max attainable: *exact* in the linear-Gaussian case; *robust qualitative* for general stationary Gaussian signals; *heuristic* for non-Gaussian.

The theorem rests on three named conditions: (i) Model S stochastic disturbance per #result-sector-condition-stability (GA-2S); (ii) $n$-dimensional independent-component Ornstein-Uhlenbeck signal structure; (iii) high-resolution regime $D^2 \ll \sigma_x^2$. Within this scope the result is as tight as the Shannon RDF allows — Kalman-Bucy exactly saturates per Mitter-Newton 2005. For non-Gaussian signals the RDF has a different form (Berger 1971 Ch. 4) but the scaling $\dot R_{\min} \propto \sigma_w^2 / D^2$ is expected to persist qualitatively; exact prefactors change per signal class. Under Model D (bounded disturbance) the argument requires worst-case channel-capacity machinery (Csiszár-Körner 2011 Ch. 11) and gives a different expression.

**Sub-scope transfer.** Sub-scope $\alpha$ agents (Kalman / conjugate-Bayesian / exponential-family / strongly-convex-gradient / linear-PD) have $\alpha$ derived from the update rule's structure per #form-sector-condition + #der-gain-sector-bridge, so the $n\alpha/2$ bound holds with known $\alpha$ and is tight in the linear-Gaussian case. Sub-scope $\beta$ agents (PID / rule-based / human-judgment) assume A2' rather than deriving it — the RDF bound still holds as an inequality (by the data-processing inequality applied to any filter mapping observation to update), but tightness is not guaranteed and the assumed $\alpha$ enters the bound.

**Confidence in correctness.** The Shannon RDF for Gaussian-OU is a classical result (Gray 1972; Ihara 1993). The sector-persistence bound is already in AAT (Prop A.1S of #deriv-sector-condition). The theorem's mathematical core is a two-line composition of both; a careful reader can verify. The contribution is not the mathematics but the AAT-framing — reading $\alpha/2$ off the sector constant as the fundamental information-rate cost of persistence — and the channel-capacity-as-first-class-quantity opening.

**What this does not establish.**

- Upper bounds on persistence cost (how much rate a specific filter consumes; the bound is a lower limit).
- Optimal filter design for minimum information throughput.
- Non-Gaussian signal cost bounds (qualitative scaling expected; quantitative forms open).
- Cost under Model D adversarial disturbance.
- Cost for composite agents beyond simple additivity.
- The stability upper bound on plasticity that #form-consolidation-dynamics references — that involves the consolidation cadence, not the online information rate.

## Discussion

**The $\alpha/2$ per-dimension Landauer analog.** The theorem has a clean thermodynamic reading per Still et al. 2012: each nat of information about the signal costs at least $k_BT$ of dissipation (Landauer 1961). Combined, persistence at sector constant $\alpha$ in $n$ dimensions costs at least $n\alpha/2$ nats/time of information acquisition and at least $n\alpha k_BT/(2\ln 2) \approx 0.35 n\alpha k_BT$ of thermodynamic dissipation per unit time in any physical substrate. AAT does not commit to a specific substrate, but the bound is substrate-agnostic: it constrains any filter implementation via the RDF (information-theoretic) and, when physical, any computational realization via Landauer (thermodynamic).

**Why channel capacity matters as a first-class quantity.** AAT's #result-persistence-condition and #def-adaptive-tempo currently frame persistence as a correction-rate vs disturbance-rate inequality. This theorem adds a *lower* constraint: observation channels must jointly supply Shannon capacity $\geq \mathcal T/2$ nats/time per dimension, else persistence fails regardless of correction-function design. The constraint is binding in any setting where observation bandwidth is non-abundant — most real systems. Three domains where the capacity floor is more binding than the tempo bound:

- *Biological systems*: neural channel capacity is finite; this bound gives a quantitative minimum on sensory bandwidth for a given adaptive rate.
- *Bandwidth-constrained distributed systems*: agents operating over noisy or low-bandwidth links face channel capacity directly as a hard constraint.
- *Context-window-limited LLMs*: the effective information rate per unit of cognition is bounded by context size and token-throughput; this theorem predicts a minimum tempo achievable at a given context budget.

In each, knowing that $\mathcal T/2$ is the floor converts an opaque "just needs more capacity" observation into a specific dimensional requirement.

**Connection to AAT's meta-architecture.** The result composes with AAT's three meta-segments.

- *#disc-separability-pattern (positive half)*: the bound sits in structured-repair along the identification-regime ladder — derived in sub-scope $\alpha$ via composition of two external theorems; holds as inequality (not tightness) in sub-scope $\beta$.
- *#disc-identifiability-floor (negative half)*: this is the positive-dual of the floor pattern. Where the floor says "AAT cannot distinguish X without information augmentation" (external no-go + AAT escape), this result says "AAT requires at least $n\alpha/2$ nats/time of information supply to operate" (external lower bound + AAT bridge through sector-persistence template). The two patterns are duals: external-theorem-forbids vs external-theorem-lower-bounds.
- *#disc-additive-coordinate-forcing (constructive half)*: the bound is linear in $\alpha$, not logarithmic. It sits *outside* the three-layer logarithmic-coordinate family (chain / divergence / update). No Cauchy-FE argument forces the coordinate here — the result is a direct substitution from classical information theory. This is a useful non-example: AAT's additive-coordinate-forcing pattern is not universal; specific results live on different coordinates.

**Relationship to #result-sector-persistence-template.** The template enumerates six instantiations (epistemic mismatch; strategic mismatch; sub-agent mismatch; composite trajectory error; composite mismatch; target-agent mismatch). Each has its own state variable $\xi$, sector constant $\alpha$, and disturbance statistics. The persistence cost bound *specializes* for each instantiation: under Model S with Gaussian-OU-shaped disturbance on the state variable, the information-rate cost is $n\alpha/2$ with the template's $\alpha$ and $n$. A compact template-cost bound — parametric in $(\xi, \alpha, n, \sigma_\xi)$ — could land as a subsection of #result-sector-persistence-template so all six instances inherit the cost bound by substitution. That move is flagged in Working Notes as an optional consolidation.

**The relationship to Mitter-Newton's thermodynamic reading.** Mitter & Newton (2005) showed the Kalman-Bucy filter operates as a Maxwellian demon: it returns signal energy to the heat bath without entropy increase, but only because new information is continually supplied at rate $\dot I$. This supply rate *is* what persistence costs — the filter maintains bounded mismatch by paying, information-theoretically, for new observations at a rate matched to the environment's innovation rate. Our theorem makes this quantitative as a function of the sector constant: at a given $\alpha$, the matching rate is $\alpha/2$. Faster correction requires more information supply; the bound is tight.

## Working Notes

- **Template-cost subsection.** A compact parametric statement — "under (T1)–(T3) with Model S and Gaussian-OU disturbance at per-component parameters $(\lambda_\xi, \sigma_\xi^2)$, sustained information rate to maintain steady-state mean-square $\xi$ at ultimate bound $D^2 = n\sigma_\xi^2/(2\alpha)$ satisfies $\dot R \geq n\alpha/2$ nats/time" — would let each of #result-sector-persistence-template's six instances inherit the cost bound by substitution. Worth considering on next template revision; would consolidate this segment's core result into the template.
- **Model D adversarial analog.** Rate-distortion is inherently stochastic; Model D's bounded-disturbance version of the theorem requires minimax / worst-case channel capacity (Csiszár-Körner 2011 Ch. 11). Candidate follow-up spike. Expected form: similar $\propto \alpha$ scaling, different prefactor.
- **Non-Gaussian signals.** For heavy-tailed or power-law signals the RDF has a different exact form (Berger 1971 Ch. 4). The qualitative scaling $\dot R_{\min} \propto \sigma_w^2/D^2$ is expected to persist; quantitative extensions are per-family.
- **Misspecification cost.** When $\mathcal F(\mathcal M) \lt 1 - \varepsilon$ per #def-model-class-fitness, achievable distortion is bounded away from zero by an additional floor.
  Natural extension has the sustained information rate lower-bounded by $n\sigma_w^2$ divided by $4$ times the larger of the Model-S ultimate bound and $D^2_{\text{floor}}$.
  Connects to #disc-identifiability-floor's "Misspecification-cost quantification" open extension.
- **Composite persistence cost.** For a composite agent, the information-rate bound's scaling under composition is not trivial. Candidate: $\dot R_{c,\min} \leq \sum_i \dot R_{i,\min}$ due to coordination overhead eating capacity. Cost-analog of #der-tempo-composition's sub-additivity + #der-team-persistence's cooperative-coupling reduction. Open.
- **Observation-channel capacity as notation.** Currently AAT uses $U_o$ (observation uncertainty) as a noise parameter. Lifting Shannon channel capacity $C^{(k)}$ of channel $k$ into NOTATION.md and relating it to $U_o$ (via the channel-capacity-from-noise standard transform) would make the capacity-floor condition a first-class persistence diagnostic. This is the biggest architectural opening from this theorem and worth a follow-up scoping decision.
- **Connection to #schema-strategy-persistence.** The strategy-edge persistence condition has its own disturbance statistics $\rho_\Sigma$ and sector constant $\alpha_\Sigma$. Specializing this theorem gives the information rate required to track strategy-edge invalidation: $\dot R_{\Sigma,\min} = n_\Sigma \alpha_\Sigma / 2$. If $\alpha_\Sigma = 1/(n+1)$ with experience discounting, the rate decays with accumulated $n$ — which connects to the stability-induced myopia result in the pending spike G.
- **Not forced by a Cauchy-FE axiom.** Unlike the three primary instances of #disc-additive-coordinate-forcing (chain, divergence, update), the linear-in-$\alpha$ coordinate of this bound is not forced by an AAT-internal additivity axiom. It is a direct consequence of Gaussian-RDF's specific functional form. This places the result *outside* the three-layer family — a useful non-example that shows the additive-coordinate-forcing pattern is not universal.


---

