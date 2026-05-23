---
slug: deriv-strategic-persistence-hard-ceiling
type: derivation
status: exact
depends:
  - schema-strategy-persistence
  - deriv-edge-credence-dynamics
  - result-sector-persistence-template
stage: draft
---

# Derivation: Hard Ceiling on Strategic-Persistence Reachability under Exponential Forgetting

The strategic-persistence schema's instantaneous persistence form $\alpha_\Sigma \gt \rho_\Sigma/R_\Sigma$ ( #schema-strategy-persistence), instantiated under Beta-Bernoulli edge dynamics with exponential forgetting at rate $\lambda \in (0,1)$, has a sharp structural cap at $\rho_\Sigma/R_\Sigma = 1/2$: no $\lambda$ satisfies the prerequisite when strategic disturbance reaches half the strategic reserve. The schema's reachable persistence region is exactly the open half-plane $\rho_\Sigma \lt R_\Sigma/2$.

## Formal Expression

### Setup

Per #deriv-edge-credence-dynamics Prop B.1, the Beta-Bernoulli edge update with $n$ accumulated pseudo-counts gives sector parameter $\alpha_\Sigma = 1/(n+1)$. Without forgetting, $n \to \infty$ and $\alpha_\Sigma \to 0$ for every edge asymptotically — so the schema's instantaneous persistence form eventually fails under any positive disturbance rate. *Exponential forgetting* with discount $\lambda \in (0,1)$ replaces the raw update with the discounted recurrence:

*[Definition (Discounted Beta-Bernoulli Update)]*

$$\alpha_k \mapsto \lambda\,\alpha_k + y_k, \qquad \beta_k \mapsto \lambda\,\beta_k + (1 - y_k)$$

following the standard adaptive-control / online-learning treatment (Ljung 1987).

### Proposition C.1 (Steady-State Sector Parameter)

*[Derived (Conditional on Beta-Bernoulli edges + exponential forgetting)]*

Under the discounted Beta-Bernoulli recurrence, the steady-state sector parameter at the fixed point $\hat p = \theta$ is:

$$\alpha_\Sigma^{\text{ss}} = \frac{1-\lambda}{2-\lambda}$$

*Proof.* At a fixed point in expectation, the discounted recurrence stabilizes when each pseudo-count equals its own contribution rate divided by the dissipation:

$$\alpha^\ast = \lambda\,\alpha^\ast + \theta \implies \alpha^\ast = \frac{\theta}{1-\lambda}, \qquad \beta^\ast = \lambda\,\beta^\ast + (1-\theta) \implies \beta^\ast = \frac{1-\theta}{1-\lambda}$$

The effective sample size is the sum:

$$n_{\text{eff}} = \alpha^\ast + \beta^\ast = \frac{1}{1-\lambda}$$

Substituting into Prop B.1's $\alpha_\Sigma = 1/(n+1)$ at $n = n_{\text{eff}}$:

$$\alpha_\Sigma^{\text{ss}} = \frac{1}{n_{\text{eff}}+1} = \frac{1}{1/(1-\lambda) + 1} = \frac{1-\lambda}{1 + (1-\lambda)} = \frac{1-\lambda}{2-\lambda} \qquad \square$$

The slow-forgetting linear form $\alpha_\Sigma^{\text{ss}} \approx 1-\lambda$ is the asymptotic expansion as $\lambda \to 1$ (the regime where the $1/(2-\lambda)$ damping factor approaches unity). Outside the slow-forgetting limit the linear form overstates the steady-state $\alpha_\Sigma^{\text{ss}}$ — at $\lambda = 0.5$ by $50\%$ ($1/3$ exact vs $1/2$ linear); at $\lambda = 0.9$ by $10\%$ ($1/11$ exact vs $1/10$ linear). The exact form is operationally the threshold to check against; the linear form is unsafe outside its asymptotic regime.

### Proposition C.2 (Hard-Ceiling No-Go)

*[Derived (Conditional on Prop C.1 + the schema's persistence form)]*

The forgetting prerequisite for the schema's trajectory guarantee under exponential forgetting is:

$$\frac{1-\lambda}{2-\lambda} \;\gt\; \frac{\rho_\Sigma}{R_\Sigma}$$

This inequality is unsatisfiable for any $\lambda \in [0,1]$ when $\rho_\Sigma \geq R_\Sigma/2$. The supremum is sharp:

$$\sup_{\lambda \in [0,1]} \alpha_\Sigma^{\text{ss}}(\lambda) = \frac{1}{2}$$

achieved as $\lambda \to 0^+$ (maximally aggressive forgetting — no memory). The schema's reachable persistence region in $(\rho_\Sigma, R_\Sigma)$-space is exactly the open half-plane $\rho_\Sigma \lt R_\Sigma/2$.

*Proof.* Let $x = \rho_\Sigma/R_\Sigma$ with $x \in [0,1)$. Solving for the threshold $\lambda$ at which the inequality becomes equality:

$$(1-\lambda) = x(2-\lambda) \implies \lambda(x-1) = 2x-1 \implies \lambda = \frac{2x-1}{x-1} = \frac{1-2x}{1-x}$$

For $\lambda \in (0,1)$ to admit a strict solution to the inequality, we need $\lambda \gt 0$ at the threshold. With $x \lt 1$ (denominator positive), this requires $1 - 2x \gt 0$, i.e., $x \lt 1/2$.

At $x = 1/2$ exactly: the threshold $\lambda = 0$, giving $\alpha_\Sigma^{\text{ss}}(0) = (1-0)/(2-0) = 1/2 = x$ — equality, not strict satisfaction. For $x \gt 1/2$: no $\lambda \in [0,1]$ satisfies the strict inequality, since even maximally aggressive forgetting ($\lambda \to 0^+$) only achieves $\alpha_\Sigma^{\text{ss}} \to 1/2$. The supremum is exactly $1/2$ at $\lambda = 0$. $\square$

Equivalently: the schema's reachable set under any exponential-forgetting design is exactly $\{(\rho_\Sigma, R_\Sigma) : \rho_\Sigma \lt R_\Sigma/2\}$. The boundary $\rho_\Sigma = R_\Sigma/2$ is not in the reachable region (strict satisfaction required), and the half-plane above the boundary is entirely outside.

## Epistemic Status

*Exact* under the named conditions: (i) Beta-Bernoulli edge dynamics ( #deriv-edge-credence-dynamics Prop B.1), (ii) exponential forgetting with $\lambda \in (0,1)$, (iii) the schema's persistence form per #schema-strategy-persistence and the underlying template-instantiation conditions (T1)–(T3) of #result-sector-persistence-template. Both Propositions C.1 and C.2 are algebraically exact within these conditions — no slack, no approximation. The "exact" tier reflects that uncertainty resides in whether the conditions hold (which mismatch state, which topology, whether the forgetting mechanism is in fact exponential vs another discounting scheme), not in the derivation.

The hard ceiling is *structural*: it is independent of $\lambda$ choice and independent of which topology among the schema's verified instances (single-edge, two-edge AND observable/unobservable, two-arm OR with $\varepsilon$-greedy, mixed AND/OR with common cause). It is a *class-level cap on reachability* — not a refutation of the schema's persistence form, but a refinement of which $(\rho_\Sigma, R_\Sigma)$ regimes the schema can be satisfied in.

## Discussion

**Why this no-go matters.** The hard ceiling *refines*, not refutes, the schema. The schema's persistence form $\alpha_\Sigma \gt \rho_\Sigma/R_\Sigma$ remains the right form; what the ceiling establishes is that under exponential forgetting, the form is *unreachable* across half the $(\rho_\Sigma, R_\Sigma)$-space. Above the ceiling, structural persistence of $\Sigma_t$ is not available to this architecture — no tuning of $\lambda$ can recover it. This is the canonical analog at the strategic layer of #result-structural-adaptation-necessity's epistemic-layer trigger: when parametric adaptation cannot keep up, structural change is required.

**Boundary behavior.** At $\rho_\Sigma/R_\Sigma = 1/2$ exactly, the supremum is achieved at $\lambda = 0$ — the *no-memory* regime where every observation fully replaces the prior. This corresponds to effective sample size $n_{\text{eff}} = 1$ (only the most recent observation counts), giving $\alpha_\Sigma = 1/2$ in Prop B.1's $1/(n+1)$. The reachable region's open-versus-closed character at the boundary is itself informative: persistence requires *strict* satisfaction, so the boundary $\rho_\Sigma = R_\Sigma/2$ is not in the reachable region even with $\lambda = 0$.

**Connection to the broader gain-decay class.** The hard ceiling sharpens to a class-level no-go on a wider class of update mechanisms — see NeurIPS 2026 Paper 2 ($\mathcal{A}_{\text{decay}}$ structural-class theorem) for the lift from Beta-Bernoulli with forgetting to all gain-decay updates: every mechanism whose effective gain decays to zero with accumulated experience universally violates the persistence threshold for any positive disturbance rate, and finite-gain mechanisms face *bidirectional* thresholds (this lower bound from the schema's persistence form, plus an upper bound from noise blow-up). The hard ceiling at $1/2$ is the Beta-Bernoulli + exponential-forgetting instance of this broader structural pattern.

**Strict-form independent-verify note.** Per #disc-stability-certificate and the project's verification discipline, the canonical strict-form check on this derivation is a fresh-mathematician re-derivation of Propositions C.1 and C.2 (algebra above) plus independent reading of #deriv-edge-credence-dynamics Prop B.1 (the source the C.1 derivation reduces to). This is owed before any further status elevation; the present "exact" tier rests on the algebra's elementariness plus the conditional structure being clean.

## Findings

### The Hard Ceiling at $\rho_\Sigma = R_\Sigma/2$ (Class-Level Reachability Cap)

**Brief:** Under the schema's Beta-Bernoulli + exponential-forgetting instantiation, $\sup_{\lambda \in [0,1]} \alpha_\Sigma^{\text{ss}} = 1/2$, achieved as $\lambda \to 0^+$. The schema's reachable persistence region in $(\rho_\Sigma, R_\Sigma)$-space is exactly the open half-plane $\rho_\Sigma \lt R_\Sigma/2$. When the strategic disturbance rate reaches half the strategic reserve, no choice of forgetting rate satisfies the persistence prerequisite — structural persistence of $\Sigma_t$ is unavailable to this architecture above the ceiling.

**Impact:** Identifies a sharp, $\lambda$-independent cap on what exponential forgetting can achieve. The cap is not an artifact of tuning; it is structural — a class-level no-go on the gain-decay-plus-forgetting class of strategic update mechanisms. For an agent whose strategic-disturbance-to-reserve ratio approaches $1/2$, no engineering of the forgetting mechanism can restore the schema's trajectory guarantee. The hard ceiling closes the design space: above it, the agent must change *something else* — the update mechanism class (away from gain-decay-plus-forgetting toward constant-step finite-gain, per the NeurIPS Paper 2 $\mathcal{A}_{\text{decay}}$ structural-class theorem), the mismatch state, or the topology. This is the canonical strategic-layer analog of #result-structural-adaptation-necessity's epistemic-layer trigger.

**Novelty Claim:** *Synthesis* of standard discounted-Beta-Bernoulli mechanics with the schema's environment-side parameters into a class-level structural cap. The constituent algebra is elementary — the discounted-update steady state $n_{\text{eff}} = 1/(1-\lambda)$ is in Ljung 1987; the $\alpha = 1/(n+1)$ form is in #deriv-edge-credence-dynamics Prop B.1. The AAT-distinctive contribution is the *combination* with $\rho_\Sigma/R_\Sigma$ into a sharp reachability cap, surfaced via the §D.3 strengthen-first work that replaced the prior linear approximation (which had hidden the ceiling) with the exact form.

**Related Work:**

| ASF Concern | Prior-art Language | Relationship / Positioning |
|---|---|---|
| Exponential forgetting / discounted least squares | Ljung 1987 *System Identification: Theory for the User*, MIT Press | *formal antecedent* — supplies the discounted-update mechanism that the C.1 steady state is built on |
| Class-level structural cap on gain-decay updates | NeurIPS 2026 Paper 2 §App-D ($\mathcal{A}_{\text{decay}}$ structural-class theorem) | *downstream sharpening* — lifts this Beta-Bernoulli instance to the gain-decay class; finite-gain mechanisms face bidirectional thresholds |
| Bias-variance trade-off in finite-gain adaptive filtering | Kushner & Yin 2003 *Stochastic Approximation and Recursive Algorithms and Applications*, 2nd ed. Springer | *contextual* — characterizes the upper bound complementing this lower bound for finite-gain (constant-step) mechanisms |
| Structural adaptation necessity (epistemic-layer analog) | #result-structural-adaptation-necessity | *parallel structural pattern* — when parametric adaptation cannot keep up, structural change is required; this no-go is the strategic-layer instance |
