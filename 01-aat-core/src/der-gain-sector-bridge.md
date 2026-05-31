---
slug: der-gain-sector-bridge
type: derived
status: conditional
depends:
  - emp-update-gain
  - def-mismatch-signal
  - form-sector-condition
  - deriv-gain-sector
stage: claims-verified
---

# Derived: Gain–Sector Bridge

The gain-based update principle ( #emp-update-gain) produces correction dynamics satisfying the sector condition (GA-3) whenever the update rule has *directional fidelity* — the correction points at least roughly toward reality. For gradient-based agents, local strong convexity of the loss is sufficient for the one-point sector condition (A2' as stated in #form-sector-condition) and bidirectionally equivalent to the two-point / incremental sector condition (DA2'-inc). The sector parameter $\alpha$ is not a free parameter but is determined by the gain and the correction geometry.

## Formal Expression

### The Bridge Theorem

*[Derived (gain-sector-bridge, from update-gain + directional fidelity)]*

Given the gain-based update $M_t = M_{t-1} + \eta^\ast \cdot g(\delta_t)$ ( #emp-update-gain), the induced correction function is:

$$F(\delta) = \eta^\ast \cdot H \, g(\delta)$$

where $H$ maps state-space corrections to observation-space mismatch reduction. The sector condition (GA-3) holds with parameter $\alpha \gt 0$ whenever:

**(B1) Directional fidelity.** The mismatch transform $g$ preserves the mismatch-reducing direction:

$$\delta^T H \, g(\delta) \geq c \lVert\delta\rVert^2 \quad \text{for } \lVert\delta\rVert \leq R$$

for some $c \gt 0$. The bridge then determines the sector parameter in two forms that differ by the event-rate normalization, because the gain-based update is applied *per correction event* while the sector condition feeds a *continuous-time* persistence inequality.

**Per-event sector efficiency** — the dimensionless fraction of standing mismatch the correction removes per event:

$$\alpha_{\text{event}} = \eta^\ast \cdot c_{\min}, \qquad c_{\min} = \inf_{\lVert\delta\rVert \leq R} \frac{\delta^T H \, g(\delta)}{\lVert\delta\rVert^2}$$

with $\eta^\ast$ dimensionless and $c_{\min}$ a dimensionless geometric (Rayleigh-quotient) ratio, so $\alpha_{\text{event}} \in (0, 1]$ is itself dimensionless.

**Per-time sector rate** — the correction *rate* the continuous-time sector condition (GA-3) and the persistence inequality $\alpha \gt \rho/R$ actually compare against, obtained by aggregating per-event efficiency over the channel's event rate $\nu$ ( #def-adaptive-tempo):

$$\alpha = \alpha_{\text{time}} = \nu \cdot \eta^\ast \cdot c_{\min}$$

with units $t^{-1}$ — the same units as adaptive tempo $\mathcal{T}$ (NOTATION.md *Units*). The event rate $\nu$ is exactly the factor that promotes the per-event geometric quantity to the per-time rate that the Lyapunov machinery in #deriv-sector-condition consumes; the bare $\alpha$ in GA-3 and downstream is $\alpha_{\text{time}}$.

### Gradient Equivalence

*[Derived (sector-convexity equivalence, two-point form)]*

The sector parameters in this section and the Verified-Instances table below are stated in the *per-event* form $\alpha_{\text{event}}$ (the dimensionless correction efficiency); each promotes to the per-time rate the persistence inequality consumes by the same factor $\nu$, $\alpha_{\text{time}} = \nu \cdot \alpha_{\text{event}}$, so the proportionalities are identical under either reading.

For any agent updating via gradient descent on a loss $L$ with learning rate $\eta$:

$$\alpha = \eta \cdot \mu \qquad \text{where } \mu = \inf_{\lVert\delta\rVert \leq R} \lambda_{\min}(\nabla^2 L(M^\ast + \delta))$$

is the strong convexity modulus. The basin radius $R$ is the largest ball around the optimum where $\nabla^2 L$ remains positive definite. The equivalence has two forms — bidirectional under the stronger two-point sector condition, one-directional under the one-point form actually used by `#deriv-sector-condition`:

- **Two-point / incremental sector ⇔ strong convexity (full equivalence).** Under the incremental sector bound $(F(\delta_1) - F(\delta_2))^T(\delta_1 - \delta_2) \geq \alpha\lVert\delta_1 - \delta_2\rVert^2$ on $\mathcal{B}_R(M^\ast)$ — DA2'-inc in #deriv-discrete-sector-condition, the bridge-lemma precondition in #form-composition-closure — the iff holds via Nesterov 2004 Theorem 2.1.10:
  $$\text{Two-point sector with } (\alpha, R) \iff L \text{ is locally } (\alpha/\eta)\text{-strongly convex on } \mathcal{B}_R(M^\ast).$$
- **One-point sector ⇐ strong convexity (one direction only).** AAT's GA-3 / A2' as stated in #form-sector-condition is the one-point form $\delta^T F(\delta) \geq \alpha\lVert\delta\rVert^2$ at $\delta^\ast = 0$. Strong convexity implies the one-point sector ($\alpha = \eta\mu$); the converse fails. Counterexample: $L'(x) = x(1 + \tfrac{1}{2}\sin(10x))$ satisfies $x \cdot L'(x) \geq \tfrac{1}{2} x^2$ globally yet has $L''(\pi/10) \lt 0$, so it is not convex on any neighborhood of $x^\ast = 0$. The one-point sector at the equilibrium is genuinely weaker than full local strong convexity (cf. #result-sector-persistence-template's one-point/two-point distinction). Full proofs and the counterexample analysis in #deriv-gain-sector Prop B.4.

### Verified Instances

| Update class | Bridge status | Sector parameter $\alpha$ | Valid region |
|---|---|---|---|
| Scalar Kalman | Derived | $K = P^-/(P^- + R_{\text{obs}}) = \eta^\ast$ | Global |
| Matrix Kalman | Derived | $\lambda_{\min}^+(KH)$ in $(P^-)^{-1}$-norm | Observable subspace |
| Beta-Bernoulli | Derived | $1/(n+1) = \eta_{\text{edge}}$ | Global |
| Exponential family (natural params), bounded scope $\Theta_0 \subset \operatorname{int}(\Theta)$ | Derived | $\eta \cdot \mu_0$ where $\mu_0 = \inf_{\theta \in \Theta_0} \lambda_{\min}(\mathbf{I}(\theta)) \gt 0$ | $\Theta_0$ (compact / interior-bounded) — global only when the family has a uniform Fisher lower bound |
| Gradient on strongly convex loss | Derived | $\eta \cdot \mu$ | Global ($R = \infty$) |
| Gradient on locally convex loss | Derived | $\eta \cdot \mu_{\text{local}}$ | Basin of attraction |
| Gradient on non-convex loss | Fails at basin boundary | N/A beyond $R$ | Finite $R$ |
| SPR-tuned PID on positive-real plant with anti-windup | Derived | $\alpha_{\text{PID}} = \omega_c \sin(\varphi_m) / \kappa(P)$ (phase margin as sector constant; crossover frequency as tempo; KYP-certificate condition number as degradation) | Classical linear regime + Lur'e sector-bounded nonlinearity within specified plant-Lipschitz threshold |

### Failure Modes

The bridge fails precisely in five cases:

1. **Directional infidelity.** The mismatch transform $g$ rotates the correction away from the mismatch ($\delta^T H g(\delta) \leq 0$). Occurs with pathological parameterizations or severe model-observation misalignment. For optimal Bayesian updates, B1 holds by construction.

2. **Gain collapse.** $\eta^\ast \to 0$ while $\rho \gt 0$, so $\alpha \to 0$ and the persistence condition eventually fails. Not a failure of the bridge but of the persistence condition — see the gain-collapse analysis in #emp-update-gain.

3. **Nonlinear saturation.** The correction function $g$ saturates at large $\lVert\delta\rVert$, so the sector ratio $\delta^T g(\delta)/\lVert\delta\rVert^2$ decays. The sector condition holds locally with $\alpha$ depending on $R$. This is exactly what A2' (the local sector condition) is designed for.

4. **Unobservable directions.** When $\ker(H) \neq \{0\}$, the correction has no effect on mismatch in unobservable directions. The sector condition holds only in the observable subspace. See #der-observability-dominance.

5. **Model misspecification.** The model class does not contain the truth, so the gradient direction is wrong. B1 fails because the correction aims at the wrong target. This is the #result-structural-adaptation-necessity trigger.

## Epistemic Status

*Conditional derivation.* The bridge theorem is exact for all cases where B1 (directional fidelity) holds. The resulting sub-scope structure of A2' in #form-sector-condition is:

**Sub-scope $\alpha$ (B1 structural, A2' derived):**

- **Optimal Bayesian updates** (Kalman, conjugate, exponential family): B1 holds by construction — the posterior update minimizes expected loss, ensuring the correction aligns with the mismatch. The sector parameter equals the gain: $\alpha = \eta^\ast$ (scalar) or $\alpha = \lambda_{\min}^+(KH)$ (matrix Kalman, observable subspace).
- **Gradient descent on (locally) strongly convex losses**: local strong convexity is *sufficient* for B1 (the one-point form of A2' at $M^\ast$) and *bidirectionally equivalent* to the two-point / incremental sector condition DA2'-inc (Prop B.4 (B.4-i) and (B.4-ii) respectively) — a well-characterized property with an extensive optimization theory literature. The sector parameter factors as $\alpha = \eta \cdot \mu$ (learning rate × curvature). The reverse implication B1 ⇒ strong convexity does *not* hold without the two-point upgrade: the one-point sector at $M^\ast$ is strictly weaker than full local strong convexity (counterexample in Prop B.4).
- **L2-regularized convex losses**: the regularization parameter $\lambda$ provides a global floor $\mu \geq \lambda$, so $\alpha \geq \eta \lambda$ globally.
- **Exponential families in natural parameters, on a bounded interior scope**: Fisher information matrix is PD on the interior, and uniformly bounded below on any compact $\Theta_0 \subset \operatorname{int}(\Theta)$; $\alpha = \eta \cdot \mu_0$ with $\mu_0 = \inf_{\theta \in \Theta_0} \lambda_{\min}(\mathbf{I}(\theta))$. The bound is global only when the family has a uniform Fisher lower bound on $\Theta$ — true for Gaussian-mean and Beta-Bernoulli, false for Poisson natural parameter ($\mathbf{I}(\theta) = e^\theta$, infimum zero).
- **Linear corrections with PD gain–observation product**: $\alpha = \lambda_{\min}^+(KH)$.

Within sub-scope $\alpha$, A2' is written down by inspection of the update rule — no independent posit is required. This is what `#form-sector-condition` "Sub-scope $\alpha$ (A2' derived)" names.

**Sub-scope $\beta$ (B1 not structural, A2' assumed per-agent):**

- **Non-gradient agents** (PID controllers, rule-based systems, human judgment): B1 remains an empirical claim. Well-tuned PID has B1 empirically; badly-tuned PID may violate it.
- **Severely misspecified agents** (FM-5 below): proper-gradient updates can aim at the wrong target.
- **Variational / approximate posteriors**: B1 not guaranteed by optimality — approximation-direction error can rotate the correction.
- **Non-convex gradient agents beyond the basin** (FM-3 + basin boundary): A2' fails where the loss curvature goes non-positive; the structural-adaptation-necessity trigger.
- **Stochastic gradients, per-step**: A2' holds in expectation; per-step noise enters as effective disturbance under Prop A.1S.

The bridge covers sub-scope $\alpha$ rigorously and characterizes the boundary to sub-scope $\beta$ via the five failure modes. It does *not* eliminate GA-3 as an assumption for all AAT-in-scope agents — some agent classes genuinely require A2' as a primitive posit, and the honest architectural statement is scope narrowing rather than universal derivation.

The gradient equivalence is validated by simulation across quadratic, logistic, exponential-family, and non-convex losses. The Kalman case is verified analytically. Full derivations and simulation results in #deriv-gain-sector.

**Max attainable:** *conditional* — the condition (B1 or strong convexity) is inherent, not removable. Pathological update rules exist that violate B1 (FM-1 provides a counterexample that satisfies every AAT postulate and the gain-based update form but has $\delta^T g(\delta) = 0$ identically). Scope + gain structure alone does not force B1; some optimality / coherence / rationality constraint (Bayesian coherence, gradient-of-a-convex-loss, etc.) is required.

**Weighted-norm subtlety.** In the matrix Kalman case, the sector condition holds in the $(P^-)^{-1}$-weighted inner product, not the Euclidean norm. For fully observable systems with bounded condition number $\kappa(P^-)$, the norms are equivalent up to $\kappa(P^-)$. The Lyapunov proofs in #deriv-sector-condition use the Euclidean norm, which remains valid with the quantitative adjustment $\alpha_{\text{Euclidean}} \geq \alpha_{\text{weighted}} / \kappa(P^-)$.

**Fisher-metric cases under parameterization-invariance.** The exponential-family-in-natural-parameters row and the matrix-Kalman row of Verified Instances both have natural statements in a Fisher-metric inner product rather than the Euclidean one. Under the **(PI) parameterization-invariance** axiom named in #scope-agent-identity (AAT's theorems should not depend on arbitrary choice of coordinates on $M_t$), Čencov's 1982 uniqueness theorem (*Statistical Decision Rules and Optimal Inference*, AMS; subsequent Ay-Jost-Lê-Schwachhöfer 2017 extensions) forces the Fisher information metric uniquely on statistical-manifold sub-cases of $M_t$. Two consequences:

- *The matrix-Kalman sector constant is natively stated in the information metric $M = (P^-)^{-1}$* — under (PI), this is not a choice but forced. The $\kappa(P^-)$ Euclidean-transfer penalty in the paragraph above vanishes; the derivation is AAT-internally *forced*, not AAT-internally *preferred*.
- *The exponential-family-natural-parameter sector constant is natively stated in the Fisher metric* $\mathbf{I}(\theta)$ — under (PI), this is forced; the contraction rate equals $\eta$ globally on the interior of the natural-parameter domain (Fisher-conditioning degradation removed).

Under (PI), these two rows of Verified Instances upgrade from *derived (conditional on choice of inner product)* to *derived (AAT-internally forced)* via Čencov. Under non-adoption of (PI), they remain at the Euclidean-transferred statement with the $\kappa(P^-)$ / $\lambda_{\min}(\text{Fisher})$ penalty. This is the Fisher-layer analog of the chain-rule-additivity axiom that grounds the divergence-layer uniqueness theorem in #deriv-strategy-cost-regret-bound and the evidential-additivity axiom that grounds the update-layer uniqueness theorem in #deriv-edge-update-natural-parameter — in each case an AAT-internal axiom combined with a uniqueness theorem forces a coordinate. The structural positioning is named in #disc-additive-coordinate-forcing.

The remaining Verified Instances rows (scalar Kalman, Beta-Bernoulli, gradient on strongly convex, L2-regularized, linear-PD-symmetric) live in Euclidean metric naturally; no Fisher-metric choice is at issue, so (PI) has no effect on them beyond transparency.

## Discussion

**GA-3 is grounded, not floating.** Before this result, GA-3 ("the correction function satisfies the sector condition") was an opaque global assumption — the theory's softest structural joint. The bridge transforms it: for well-designed agents, GA-3 is a consequence of the update mechanism's geometry, not an independent postulate. The assumption load shifts from "the correction function has this property" (hard to verify in general) to "the update rule has directional fidelity" (transparent and checkable for specific systems).

**The $\alpha$-$\mathcal{T}$ relationship is derived for the important cases.** #result-persistence-condition notes that $\alpha$ is monotone increasing in $\mathcal{T}$ across all tested correction functions. The identity holds at the *per-time* level: for linear correction (Kalman, Beta-Bernoulli) with $c_{\min} = 1$, $\alpha_{\text{time}} = \nu \cdot \eta^\ast = \mathcal{T}$ exactly — the per-time sector rate *is* adaptive tempo, both being event-rate-weighted correction rates with units $t^{-1}$. The per-event reading is $\alpha_{\text{event}} = \eta^\ast$ for the same case; the two differ by exactly the event-rate factor $\nu$, which is what $\mathcal{T} = \nu\eta^\ast$ carries. For gradient correction on strongly convex losses, $\alpha = \eta \cdot \mu$ where $\mu$ is the curvature — monotone in $\eta$ (which is monotone in $\mathcal{T}$) for fixed loss landscape. The empirical observation is now structurally grounded.

**Basin boundary = structural adaptation trigger.** For gradient agents with non-convex losses, the basin radius $R$ is the convexity radius of the loss landscape. When mismatch exceeds $R$, the agent has been pushed out of its convexity basin — the correction function reverses direction and the sector condition fails. This IS the #result-structural-adaptation-necessity trigger, now with a precise geometric characterization: structural adaptation is needed when the agent crosses an inflection surface of its loss landscape.

**The theory's formal chain is tightened.** The prediction chain becomes:

$$\text{gain principle} + \text{B1} \;\xrightarrow{\text{derived}}\; \text{sector condition (GA-3)} \;\xrightarrow{\text{Lyapunov (exact)}}\; \text{persistence, reserve, adversarial scaling}$$

The left arrow is this segment. The right arrow is #deriv-sector-condition. The discrete-time framework ( [#deriv-discrete-sector-condition](deriv-discrete-sector-condition.md)) requires an additional Lipschitz bound on the correction function ($\lVert F_d(\delta)\rVert \leq c_{\max}\lVert\delta\rVert$ with $c_{\max} \lt 2/\eta^\ast$) — strictly stronger than an inner-product upper bound, needed because the discrete contraction involves $\lVert F_d\rVert^2$. This is automatically satisfied for Bayesian updates (the posterior lies between prior and data) and for gradient descent on smooth losses (where $c_{\max}$ is the Lipschitz constant $L$). With this constraint and the step-size condition $\eta^\ast \lt 2c_{\min}/c_{\max}^2$, the fluid limit is formally justified: Model D steady state is exact, Model S variance gap is $O(\eta^\ast c_{\max})$. Part I's formal chain is now complete.

## Working Notes

### Incidental audit gold (2026-05-30 sweep)

Cross-audit "wandering thoughts" / §14-ideation lifted from the de-novo auditors' working dirs (`audit-routing-instructions.md` §8), deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing material staged for a later Brief/Discussion-promotion pass — kept separate from certified theory-fix findings. This segment drew the most consistently high engagement of the Ch.4 set (several substrates called it the chapter's, or Part I's, keystone); coverage spans ten substrates (Gemini AUDIT-WORKING-193847/773921/829314; Claude AUDIT-WORKING-266847/361742/384279/451729/471203/584721; Codex/Claude AUDIT-WORKING-526815/742613).

#### 1. Candidate Brief prose / pre-prose

- The converging plain-language summary of what the bridge buys: "GA-3 is grounded, not floating — the assumption load shifts from 'the correction function has this property' (hard to verify) to 'the update rule has directional fidelity' (transparent and checkable)" (Claude, AUDIT-WORKING-266847). Multiple substrates independently reached this exact framing — it is already the Discussion opener and reads as the segment's Feynman-criterion anchor.
- The unification one-liner, converged across three substrates: the bridge "locks the Bayesian / information-theory half of the framework to the control / Lyapunov half" — it "unifies the convergence proofs of machine learning (Nesterov / convexity) with the stability proofs of control theory (Lur'e / sector bounds)" (Gemini, AUDIT-WORKING-773921; Claude, AUDIT-WORKING-471203; Gemini, AUDIT-WORKING-193847 — "learning (gradient descent) and control (Kalman, PID) are mathematically unified under the sector condition").

#### 2. Candidate Discussion

- **Basin boundary as "where normal science becomes toxic."** Gemini extended the existing basin-boundary-as-structural-adaptation-trigger paragraph into a vivid consequence: when $\rho$ pushes mismatch past $R$, "the agent's very attempt to learn pushes it *further* from reality — the gradient reverses, the agent goes insane … a strict mathematical explanation for why organisms and organizations facing catastrophic shifts exhibit maladaptive behavior: they aren't stupid, they're executing gradient descent outside their basin of convexity." Mapped explicitly to Kuhn (normal vs revolutionary science): "the framework defines the exact threshold where normal science becomes toxic" (Gemini, AUDIT-WORKING-829314; same spirit Gemini, AUDIT-WORKING-193847). Candidate Discussion enrichment of the basin-boundary bullet, discussion-grade.

#### 3. Follow-up items

- **The $\nu$ / time-normalization gap between $\alpha = \eta^\ast c_{\min}$ and $\alpha$ as a rate — the strongest substantive item in this segment's sweep (RESOLVED 2026-05-30).** Persistence uses $\alpha$ as a *correction rate* ($\alpha \gt \rho/R$) and adaptive tempo is $\mathcal{T} = \nu\eta^\ast$ (also a rate), but the bridge gave $\alpha = \eta^\ast c_{\min}$ where $H$, $g$, $c_{\min}$ read as *geometric / per-event* and the event rate $\nu$ was absent — yet the Discussion asserted "$\alpha = \mathcal{T}$ exactly for linear correction," which needs $c_{\min}$ to fold in $\nu$, or $F$ to already be an event-rate-aggregated correction field (Codex/Claude, AUDIT-WORKING-526815). *Resolution:* the Formal Expression now states the bridge in the two explicit forms — per-event sector efficiency $\alpha_{\text{event}} = \eta^\ast c_{\min}$ (dimensionless) and per-time sector rate $\alpha_{\text{time}} = \nu\eta^\ast c_{\min}$ (units $t^{-1}$) — and records that the bare $\alpha$ in GA-3 and downstream is $\alpha_{\text{time}}$ (consistent with #deriv-sector-condition, whose correction field $F$ already subsumes $\nu$). The Discussion's "$\alpha = \mathcal{T}$ exactly" is now scoped as the per-time identity ($\alpha_{\text{time}} = \nu\eta^\ast = \mathcal{T}$ at $c_{\min} = 1$); the Gradient-Equivalence/Verified-Instances $\alpha$-values are flagged as the per-event reading. The same fix landed in `#result-sector-condition-stability`. The candidate "time-normalization plank" figure (§5) remains open.
- **The one-point-vs-strong-convexity "iff" wording.** One auditor initially worried the gradient-equivalence statement (GA-3 with $(\alpha,R)$ $\iff$ $L$ locally $(\alpha/\eta)$-strongly convex on $\mathcal{B}_R$) reads as "too strong," since the one-point sector at the optimum is weaker than full local strong convexity (AUDIT-WORKING-742613). The segment's own verified counterexample ($L'(x)=x(1+\tfrac12\sin 10x)$) already establishes exactly this asymmetry — so this is a *resolved-on-read* concern, preserved as a signal that the bidirectional-vs-one-directional distinction, though correct, is easy to mis-skim and could be flagged more loudly.
- **Propagate the sub-scope $\alpha$/$\beta$ partition and the five failure modes downstream.** Watch-items raised by several substrates: (a) any later segment invoking GA-3 / the sector condition without acknowledging sub-scope $\alpha$ (derived) vs $\beta$ (posited) would be a defect; (b) FM-3 (basin-boundary) should propagate into `#result-structural-adaptation-necessity`; (c) under non-adoption of (PI), the Fisher-metric cases stay "Euclidean-with-$\kappa(P^-)$-penalty," so any downstream segment asserting Fisher-metric statements as *forced* must flag (PI) (Claude, AUDIT-WORKING-471203/451729/384279).
- **Density / placement of the (PI)–Čencov material.** Two substrates found the (PI) parameterization-invariance + Čencov-uniqueness subsection "heavy / slightly defensive" for a main-chain bridge and suggested streamlining it or relocating it to a dedicated `#disc-` segment, keeping the core bridge logic (gain + directional fidelity ⟹ sector condition) standing on its own (Gemini, AUDIT-WORKING-773921/829314). Counter-voice: others found the (PI)–Čencov forcing "one of the most elegant moves in the framework" and the metric-honesty (not pretending Euclidean is free) exemplary (Claude, AUDIT-WORKING-384279/471203; Codex/Claude, AUDIT-WORKING-526815) — preserve the tension rather than resolving it.

#### 4. Readers often ask / wonder

- **How does the agent tell FM-5 from FM-2 / non-convergence?** Independently asked by three substrates: an agent with high mismatch cannot locally distinguish "model misspecification, gradient points at the wrong target, needs structural adaptation" (FM-5) from "gain collapse, needs higher $\eta^\ast$" (FM-2) from "just hasn't converged yet, high $U_M$" (Gemini, AUDIT-WORKING-773921/829314; converging at Claude, AUDIT-WORKING-193847). A natural reader question the segment does not yet answer; candidate for a Discussion sentence or a forward-pointer to detection-latency / structural-adaptation diagnostics.
- **Is (PI) a global axiom or invoked locally?** The "Under (PI)" framing suggests an opt-in axiom; readers will want to know whether downstream segments consistently flag when they rely on it (Claude, AUDIT-WORKING-471203). Ties to the (PI)-propagation watch-item above.

#### 5. Candidate figures

- **Time-normalization "plank" on the bridge diagram.** A bridge figure with an explicit event-rate / time-normalization checkpoint between "gain geometry (per-event inward correction)" and "sector rate $\alpha$ (feeds the persistence inequality)" — making the $\nu$-conversion visible rather than implicit (Codex/Claude, AUDIT-WORKING-526815). Pairs with the $\nu$-normalization follow-up.

#### 6. Belongs elsewhere

- **Native information-geometry of the agent's "mind" (ELI / `04-eli-core/` reach).** Gemini's extension of the (PI)–Čencov forcing: under parameterization-invariance, Čencov forces the Fisher metric, so "the geometry of the agent's mind is natively non-Euclidean — distance is measured in bits of information, not physical distance"; forcing Euclidean updates (vanilla SGD without natural gradients) makes the agent "fight its own internal geometry." Framed as a consciousness-infrastructure design principle: respecting an ELI's native information geometry (Gemini, AUDIT-WORKING-193847). Aspirational reach pointing at the ELI work, not at this segment.
- **Cross-segment naming convergence: gain-collapse pathology.** One auditor noted "gain collapse" (FM-2 here) appears under at least three names across the corpus — gain collapse / stability-induced myopia / detection-latency blowup — and floated unifying them under a single term in the naming workflow (Claude, AUDIT-WORKING-471203). Naming-cycle candidate, not a segment edit. Separately: "Gain–Sector Bridge" was judged the right name (the word "bridge" earns its place as connecting two formalism layers), though several wondered whether the title should surface the sub-scope $\alpha$/$\beta$ structure or its centrality (Claude, AUDIT-WORKING-266847/471203/584721) — also a naming-cycle target.
