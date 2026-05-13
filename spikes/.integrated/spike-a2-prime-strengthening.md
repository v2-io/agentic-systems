# Spike: A2' Strengthening — Derivability within AAD Scope

**Date:** 2026-04-22
**Trigger:** O-BP14 derivation-table pass on `#deriv-sector-condition` surfaced epistemic slack — A2' labeled "Assumption" in the main Assumptions section but "Derived (conditional on #der-gain-sector-bridge)" in the O-BP14 row, with the "Grounding of GA-3" paragraph describing it as derivable. Classic three-layer-separation territory on a Section I load-bearing primitive.
**Posture:** Strengthen first (attempt the improbable), then soften honestly if needed.

## 1. The question

**Is the local sector condition (A2') fully *derivable* within AAD's formal scope, or is there an agent class in AAD scope where A2' must stand as a primitive assumption?**

Separately: **can the Prop A.1S "sufficiently large region" condition be lifted from Epistemic Status into the proposition statement cleanly?**

A2' is load-bearing — every Section I persistence-flavored result, every Section III composition result (via `#result-sector-persistence-template`), every downstream adversarial / structural / team result uses an instance of A2'. Tightening A2' tightens the entire Lyapunov chain.

## 2. What is already known

From `#der-gain-sector-bridge` (claims-verified, conditional status):

- Prop B.3 derives A2' conditional on **B1 (directional fidelity)**: $\delta^T H g(\delta) \geq c \lVert\delta\rVert^2$ on $\mathcal B_R$. Given B1, $\alpha = \eta^\ast \cdot c_{\min}$.
- For **optimal Bayesian updates** (Kalman, conjugate, exponential family in natural parameters), B1 holds *by construction* — the posterior minimizes expected loss.
- For **gradient descent** on differentiable losses, B1 is *equivalent* to local strong convexity (Prop B.4) with $\alpha = \eta \cdot \mu$.
- For **non-gradient agents** (PID, rule-based, human judgment), B1 is explicitly stated as an empirical claim.
- Five failure modes characterized (FM-1 directional infidelity, FM-2 gain collapse, FM-3 nonlinear saturation, FM-4 unobservable directions, FM-5 model misspecification).

So A2' is *already* a conditional derivation in the bridge segment. The spike's question is whether the condition (B1) is itself derivable from AAD's postulates, or whether it stands as the sub-scope-defining assumption.

## 3. Paths attempted

### Path 1 — Bayesian coherence forces directional fidelity (DOES NOT WORK UNIVERSALLY)

**Claim to test.** If AAD's scope requires Bayesian-coherent updating, directional fidelity is inherited and A2' is derived universally.

**Check.** `#deriv-recursive-update` proves only the recursive *form* $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ — it constrains structure, not rule. `#emp-update-gain` is *robust qualitative*, explicitly noting that RL (fixed $\alpha$), PID (fixed $K_p$), and human judgment are in scope but non-Bayesian. `#def-agent-spectrum` explicitly places PID controllers in the "blind pursuer" region of AAD scope.

**Verdict.** Bayesian coherence is *sufficient* for B1 (Prop B.3's remark, standard Bayesian-decision-theory argument — posterior update is the Bayes-risk minimizer, so correction is gradient-of-log-likelihood-aligned). But Bayesian coherence is NOT universally required in AAD scope. Path 1 yields a sub-scope derivation, not a universal one.

### Path 2 — Scope + gain structure suffices (DOES NOT WORK)

**Claim to test.** (P1)–(P4) + directed separation (Class 1) + gain-based update structure together force B1.

**Check.** The gain-based form $M_t = M_{t-1} + \eta^\ast g(\delta_t)$ leaves the *direction* of $g(\delta)$ unconstrained. The postulates require observation, recursive update, temporal ordering, causal hierarchy — none of these pins down a monotonicity relation between $g(\delta)$ and $\delta$. An agent with $g(\delta) = R_{90°} \delta$ satisfies every AAD postulate but fails B1 trivially ($\delta^T g(\delta) = 0$). `#der-gain-sector-bridge` §FM-1 exhibits exactly this counterexample.

**Verdict.** Scope + gain structure does NOT force B1. Some optimality / coherence / rationality principle is needed.

### Path 3 — Lyapunov persistence implies B1 retroactively (CONDITIONAL)

**Claim to test.** If an agent persists (bounded mismatch under bounded disturbance), this retroactively constrains its update to have directional fidelity (on some region, relative to some norm).

**Argument structure.** Suppose $\dot \delta = -F(\delta) + w(t)$ with $\|w\| \leq \rho$ and the agent exhibits ultimate boundedness: $\limsup \|\delta(t)\| \leq R^\ast$. Does this imply $\delta^T F(\delta) \geq \alpha \|\delta\|^2$ on some ball?

**Converse Lyapunov theorem (Khalil 2002, Thm 4.17).** If the origin of $\dot \delta = -F(\delta)$ is exponentially stable on a region $D$, then there exists a Lyapunov function $V(\delta)$ and constants $c_1, c_2, c_3, c_4$ such that $c_1 \|\delta\|^2 \leq V(\delta) \leq c_2 \|\delta\|^2$, $\dot V \leq -c_3 \|\delta\|^2$, $\|\partial V / \partial \delta\| \leq c_4 \|\delta\|$. This gives a *quadratic-type* Lyapunov witness for the persistence property.

**But the witness may not be $V = \tfrac{1}{2}\|\delta\|^2$.** The converse theorem delivers *some* quadratic-equivalent Lyapunov function, not specifically the Euclidean-norm one. The corresponding "sector-like" condition is with respect to the matrix $P$ defining $V(\delta) = \delta^T P \delta$, not the Euclidean inner product.

**Counterexample to the universal Euclidean A2'.** The matrix-Kalman case (`#deriv-gain-sector` Prop B.2) already exhibits this: the sector condition holds in the $(P^-)^{-1}$-weighted inner product, not the Euclidean one. The Euclidean-norm A2' holds only up to the condition number $\kappa(P^-)$. For systems with ill-conditioned prior covariance, Euclidean A2' can fail while weighted A2' holds — and the agent still persists. This is already flagged in `#der-gain-sector-bridge` Epistemic Status.

**What this gives.** A conditional converse: persistence *implies* a sector condition *in the quadratic-Lyapunov-witness inner product*. Under norm equivalence (bounded condition number), this transfers to Euclidean A2' with a degraded $\alpha$.

**Verdict.** Path 3 yields: persistence + quadratic Lyapunov witness + bounded norm-equivalence ⇒ Euclidean A2' on the witness region, with $\alpha$ potentially degraded by the condition number. Not a universal derivation of A2'; an important structural clarification.

### Path 4 — Characterize the boundary (THIS IS THE HONEST OUTCOME)

Combining Paths 1–3: A2' is derived in a characterized sub-scope and must be verified per-agent in the rest. The boundary has sharp structure.

**Sub-scope α (A2' derived):** Agents whose update rule has B1 as a structural consequence:

| Agent class | Source of B1 | $\alpha$ |
|---|---|---|
| Optimal Bayesian (Kalman, conjugate) | Bayes-risk minimization (posterior aligned with likelihood gradient) | $\eta^\ast$ (scalar); $\lambda_{\min}^+$ restricted to observable subspace (matrix) |
| Exponential family in natural parameters | Fisher information matrix is PD on interior of natural parameter space | $\eta \cdot \lambda_{\min}(\text{Fisher})$ |
| Gradient descent on strongly convex loss | Strong convexity ⇔ gradient monotonicity (Nesterov 2004, Thm 2.1.10) | $\eta \cdot \mu$ |
| L2-regularized convex loss | Regularization floor $\mu \geq \lambda$ | $\eta \cdot \lambda$ |
| Gradient on locally convex loss | Within basin of attraction only | $\eta \cdot \mu_{\text{local}}$ |

For sub-scope α, A2' is a **derived** consequence of the update rule's structure. The magnitude $\alpha$ is computable from the update-rule parameters.

**Sub-scope β (A2' must be verified or assumed):** All other AAD-in-scope agents:

| Agent class | Why B1 is not structurally guaranteed |
|---|---|
| PID controllers with fixed gains | No gradient / optimality structure; B1 is a tuning question |
| Rule-based systems | No continuous update rule; A2' is a domain-specific empirical claim |
| Human judgment / organizational learning | Structural analogy in `#emp-update-gain`; no formal B1 guarantee |
| Severely misspecified agents | FM-5: even proper-gradient rules aim at the wrong target |
| Variational / approximate posteriors | B1 not guaranteed by optimality (approximation error can rotate) |
| Non-convex gradient agents beyond the basin | A2' fails at basin boundary — structural-adaptation trigger |
| Stochastic gradient (per-step) | A2' holds in expectation; per-step noise enters as effective disturbance |

For sub-scope β, A2' is an **assumption** — a well-scoped empirical claim about the agent's correction geometry. The Lyapunov proofs operate downstream of A2' regardless of how it is established.

**Verdict.** A2' is **derived in sub-scope α, assumed in sub-scope β**. This is the honest scoping. The current segment language ("the sector condition is not an irreducible assumption for well-designed agents") is *approximately right* but should be tightened to explicitly name the two sub-scopes rather than let the reader infer the scope from context.

### Path 5 — Prop A.1S region condition (LIFTABLE)

**Question.** Prop A.1S uses A2' on the entire trajectory, but Wiener excursions can push $\delta$ outside $\mathcal B_R$ where A2' may not hold. Can the condition be lifted from Epistemic Status into the proposition statement?

**Standard technique (Khasminskii 2012, *Stochastic Stability of Differential Equations*, ch. 5).** Use a stopping-time localization. Define $\tau_R = \inf\{t : \|\delta(t)\| > R\}$ (first exit from $\mathcal B_R$). The stopped process $\delta(t \wedge \tau_R)$ satisfies A2' almost surely on $[0, t \wedge \tau_R]$.

**Lifted statement (what the proposition can cleanly say).**

Under (A1), (A2') on $\mathcal B_R$, (A3), with GA-2S ($\mathbb E[\|w(t)\|^2] = \sigma_w^2$):

(i) (Stopped bound.) The stopped process satisfies
$$\mathbb E[\|\delta(t \wedge \tau_R)\|^2] \leq \|\delta(0)\|^2 e^{-2\alpha t} + \frac{n \sigma_w^2}{2\alpha}$$
for all $t \geq 0$.

(ii) (Non-exit probability.) If $R^\ast_S := \sigma_w \sqrt{n/(2\alpha)} \lt R$ (the ultimately-bounded radius fits within the sector-condition region), then by the Markov tail bound applied to the supermartingale $V(\delta) - n\sigma_w^2 t /4$ at steady state, $P(\tau_R = \infty) \geq 1 - n\sigma_w^2 / (2\alpha R^2)$.

(iii) (Unstopped bound.) On the event $\{\tau_R = \infty\}$, the unstopped Grönwall bound $\mathbb E[\|\delta(t)\|^2] \leq \|\delta(0)\|^2 e^{-2\alpha t} + n \sigma_w^2/(2\alpha)$ holds. The excursion contribution is bounded by $n\sigma_w^2 / (2\alpha R^2)$ times the excursion-regime second moment — a higher-order correction when $R^\ast_S \ll R$.

**Minimal region characterization.** The proposition needs A2' on $\mathcal B_R$ with $R$ large enough that $R^\ast_S \lt R$, i.e., $\alpha R^2 \gt n \sigma_w^2 / 2$. This is the *structural persistence condition in mean-square*. The "sufficiently large region" condition in the current Epistemic Status is precisely this inequality.

**Verdict.** Liftable. The proposition should state (i)–(iii) explicitly. The Epistemic Status paragraph on Wiener excursions becomes redundant once the proposition is region-aware.

## 4. Outcome declaration

**Outcome B (scope narrowing) + partial Outcome A (Prop A.1S lift).**

1. **A2' is derived in sub-scope α, assumed in sub-scope β.** The current segment language is close to this but doesn't name the sub-scopes explicitly. Sharpen.
2. **Prop A.1S can be lifted** using a standard stopping-time localization. The region condition becomes part of the proposition statement.
3. **Path 3's converse-Lyapunov observation** (persistence implies A2' in the Lyapunov-witness inner product, Euclidean A2' up to condition number) is worth surfacing as a Discussion-grade note — it clarifies why the Euclidean form is a *formulation choice* that happens to match the canonical quadratic Lyapunov candidate.

**Outcome C (structural non-derivability, back out "Grounding of GA-3")** is NOT the right move. The grounding paragraph is approximately correct; the fix is precision about sub-scope, not retreat.

## 5. Segment edits to land

### 5.1 `#deriv-sector-condition`

- **Sharpen the A2' Assumptions subsection.** After the A2' statement, add an explicit sub-scope paragraph naming sub-scope α (A2' derived, listing the five classes from the bridge) and sub-scope β (A2' assumed / empirical claim, listing the agent classes where B1 is not structurally guaranteed). Reference `#der-gain-sector-bridge` Prop B.3 as the derivation source for sub-scope α.
- **Tighten the "Grounding of GA-3" paragraph.** Replace "is not an irreducible assumption for well-designed agents" (imprecise) with the explicit sub-scope α / β split. Retain $\alpha = \eta^\ast \cdot c_{\min}$ as the sub-scope-α magnitude.
- **Lift the Prop A.1S region condition into the proposition statement.** Replace the current "implicit strengthening / stopping-time argument" Epistemic Status language with the stopped / unstopped / non-exit probability statement (i)–(iii).
- **Update the O-BP14 table row for A2'.** From "Derived (conditional on #der-gain-sector-bridge's directional-fidelity premise); otherwise Assumption" to "Derived within sub-scope α (Bayesian / gradient-strongly-convex / exponential family; B1 structural); Assumption within sub-scope β (PID, rule-based, non-Bayesian); see #der-gain-sector-bridge Props B.3–B.4 and §Failure Modes."
- **Add a Discussion note on Path 3** (converse Lyapunov): the Euclidean A2' is the canonical sector form matched to $V = \tfrac{1}{2}\|\delta\|^2$; under the weighted Lyapunov candidate $V = \tfrac{1}{2}\delta^T P \delta$, the sector condition is $\delta^T P F(\delta) \geq \alpha \delta^T P \delta$, and persistence-implies-sector holds in the weighted inner product. This clarifies why the matrix-Kalman weighted-norm subtlety in `#der-gain-sector-bridge` is not an exception but an instance of a general structure.

### 5.2 `#der-gain-sector-bridge`

- **Add a sub-scope α / β naming paragraph** to the Epistemic Status section, mirroring `#deriv-sector-condition`. No new math; clarity in terminology.
- **Stage:** leave at `claims-verified` if the changes are purely language tightening; revert to `draft` if substantive.

### 5.3 Prop A.1S region-aware statement impact

- **`#result-sector-persistence-template`** (T3-S) currently uses the Grönwall bound form without region-awareness. Add a brief Epistemic Status sentence pointing to the stopped / unstopped refinement, citing the updated Prop A.1S. No change to the template's instantiation table.
- Downstream consumers (`#result-persistence-condition`, `#schema-strategy-persistence`, `#der-team-persistence`, `#form-composition-closure`, `#der-tempo-composition`, `#der-adversarial-destabilization`) do not need edits — they invoke the template without reference to A.1S's region technicality.

### 5.4 Stage updates

- `#deriv-sector-condition`: already `draft` — substantive content change, remains `draft` for re-review.
- `#der-gain-sector-bridge`: was `claims-verified` — substantive language change (sub-scope naming); revert to `draft` for re-review.
- `#result-sector-persistence-template`: was `draft` — small epistemic-status addition only; remains `draft`.

## 6. References

- Khalil, H. K. (2002). *Nonlinear Systems* (3rd ed.). Prentice Hall. Ch. 4 (Lyapunov stability), ch. 9 (input-output stability), Thm 4.17 (converse Lyapunov), Thm 4.18 (ultimate boundedness).
- Khasminskii, R. (2012). *Stochastic Stability of Differential Equations* (2nd ed.). Springer. Ch. 5 (Lyapunov functions and stochastic stability; stopping-time localization).
- Lur'e, A. I. (1957). *Some Nonlinear Problems in the Theory of Automatic Control*. Gostekhizdat. Original sector-condition framework for absolute stability.
- Nesterov, Y. (2004). *Introductory Lectures on Convex Optimization*. Springer. Thm 2.1.10 (strong convexity ⇔ gradient monotonicity).
- AAD segments cited: `#deriv-sector-condition`, `#der-gain-sector-bridge`, `#deriv-gain-sector`, `#emp-update-gain`, `#deriv-recursive-update`, `#form-agent-model`, `#def-agent-spectrum`, `#scope-agency`, `#result-sector-persistence-template`, `#deriv-discrete-sector-condition`.

## 7. Open questions (after this spike)

1. **Non-gradient agents in AAD scope.** For PID controllers, rule-based systems, and human-judgment agents, A2' remains an empirical claim. Is there a narrower mid-level sub-scope (e.g., "PID with gains tuned to Ziegler-Nichols ranges") where B1 can be argued structurally? Deferred — not blocking Section I completion.
2. **Variational inference.** A2' holds in expectation for optimal Bayesian updates, but variational approximations can violate B1 by approximation-direction error. This is structurally outside sub-scope α as currently defined. Worth a future note cross-referencing Wainwright & Jordan 2008 (variational methods and Bethe free energy) if the active-inference integration deepens.
3. **Global sector bound for structural-adaptation-resistant agents.** A2 (global, without $\mathcal B_R$ restriction) is stronger and would give global ultimate boundedness and infinite adaptive reserve. It is unrealistic for finite model classes (flagged in Working Notes of `#deriv-sector-condition`), but is there a domain-specific agent class (e.g., specialists in convex-only environments) where A2 holds globally by construction?
4. **Tier interaction with sector condition.** The tier 1/2/3 structure in `#form-composition-closure` uses DA2'-inc (incremental / strong monotonicity), strictly stronger than one-point A2'. The relationship between A2' sub-scope α/β and the composition tiers is not yet characterized — sub-scope α agents are largely Tier 1, but the mapping is not exact. Future spike.
