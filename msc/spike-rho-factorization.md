# Spike: Factorization of the Effective Disturbance Rate $\rho$

*Started 2026-04-22. Research spike. Not canon.*

## 1. Problem statement

The internal-external-decomposition spike (`msc/spike-internal-external-decomposition.md`) rests on a working hypothesis:

$$\rho \;=\; \rho_{\text{external}} \cdot f(\mathcal M) \cdot g(\pi) \qquad\text{(R-F)}$$

with $f(\mathcal M), g(\pi) \in (0, 1]$, and its log form

$$\log \rho \;=\; \log \rho_{\text{external}} + \log f(\mathcal M) + \log g(\pi). \qquad\text{(log-R-F)}$$

The parent spike explicitly flags this as the weakest link (§3.2, §10, §12.4 item 1). Its status determines whether the internal-external decomposition can be promoted to conditional or robust-qualitative or must remain heuristic.

**The task.** Attack the factorization rigorously. Derive it from AAD primitives if possible; otherwise characterize the obstruction precisely and propose an honest reframe. The investigation must:

1. Pin down what $\rho$ actually is (operationally and mathematically).
2. Ask whether $\rho_{\text{external}}$ is a well-defined limit.
3. Ask whether $f(\mathcal M)$ and $g(\pi)$ are derivable from named AAD quantities.
4. Ask whether the multiplicative form (equivalently, log-additive form) is forced or chosen.
5. Work at least two structured cases (linear-Gaussian; Beta-Bernoulli; OU with LQR) end-to-end.
6. Report outcome as (A) full derivation, (B) partial, or (C) obstruction with honest reframe.

**Scope.** I attempt the derivation under sub-scope $\alpha$ (Kalman / conjugate-Bayesian / exponential-family / strongly-convex-gradient / linear-PD) — the regime where `#gain-sector-bridge` already delivers structural results. If the factorization fails under sub-scope $\alpha$, it has no chance under sub-scope $\beta$.

## 2. What $\rho$ is

`#mismatch-dynamics` writes

$$\frac{d\lVert\delta\rVert}{dt} = -\mathcal T \cdot \lVert\delta\rVert + \rho(t), \qquad \lVert w(t)\rVert \le \rho \text{ (Model D)}, \qquad \mathbb E\lVert w(t)\rVert^2 = \sigma_w^2 \text{ (Model S)}$$

where $w(t)$ is the disturbance injected into the mismatch process
$d\delta/dt = -F(\mathcal T, \delta) + w(t)$ per `#sector-condition-stability`.

**Key observation: $w(t)$ is defined agent-relatively.** By construction, $\delta_t = o_t - \hat o_t(M_{t-1}, a_{t-1})$ (`#mismatch-signal`) is the residual that the model does *not* predict. So the "disturbance" $w(t)$ is *whatever part of the environment's evolution the agent's prediction fails to track* — not some raw environmental quantity.

Substituting into Model D:

$$\rho \;=\; \sup_t \,\lVert w(t)\rVert \;=\; \sup_t \,\Big\lVert \tfrac{d\delta}{dt} + F(\mathcal T, \delta) \Big\rVert$$

which depends on $M_t$ (what the model predicts), $\pi$ (what actions the agent takes, which affect the next $o_{t+1}$), and the environment jointly.

**This is the heart of the issue.** $\rho$ is not "the environment's volatility" in any agent-independent sense. It is the *effective innovation rate* the agent's predictor fails to absorb. Calling it "environment-side" in the persistence condition was a useful simplification; the factorization (R-F) is trying to un-simplify by peeling agent-side factors back out.

**Four candidates for what $\rho$ *is*:**

1. **(a) Agent-conditional innovation rate.** $\rho = \rho(\mathcal M, \pi, \text{env}) = $ rate at which $\delta$ is driven by un-modeled dynamics given agent's specific $(\mathcal M, \pi)$. This is what the equations actually use.
2. **(b) Environment-only disturbance rate.** Intrinsic to the environment, not agent-dependent. This is the intuition behind $\rho_{\text{external}}$ but is *not* what the AAD equations define.
3. **(c) Joint agent-environment property.** Something between (a) and (b) that does not cleanly factor.
4. **(d) Regime-dependent.** Different things in different regimes (deterministic drift vs stochastic noise; Model D vs Model S).

The AAD literal-reading is (a). The parent spike needs (b) for the leading term $\rho_{\text{external}}$ to be well-posed. The translation from (a) to (b) — if possible — is exactly what the factorization is trying to accomplish.

**Pinning down $\rho_{\text{external}}$.** For $\rho_{\text{external}}$ to be well-defined requires choosing a reference agent: a maximally-naive predictor. Three candidates:

- **Max-entropy reference:** $M^{\text{ref}}$ predicts the marginal $P(o_{t+1})$ with no dependence on history. Then $\rho^{\text{ref}}$ is the full entropy rate of the observation sequence.
- **Delta-function reference:** $\hat o_{t+1}^{\text{ref}} = o_t$ (naive-persistence predictor). Then $\rho^{\text{ref}}$ is the first-difference scale of the observation sequence.
- **Constant-zero reference:** $\hat o = 0$. Then $\rho^{\text{ref}}$ is the scale of $o$ itself.

Each gives a different numerical $\rho_{\text{external}}$ and therefore a different $f(\mathcal M)$. The factorization (R-F) is under-specified without naming a reference.

This is already a warning sign. A factorization that depends on an arbitrary reference-agent choice is a *decomposition relative to a reference*, not an absolute factorization.

## 3. Structured derivation 1 — Scalar linear-Gaussian (Kalman)

### 3.1 Setup

True process (scalar state $x_t$, continuous time):

$$dx_t = -\lambda_s x_t\,dt + \sigma_\text{nat}\,dW_t \qquad \text{(stationary OU)}$$

Observation at event times $t_k = k/\nu$ (Poisson or uniform):

$$y_k = x_{t_k} + \varepsilon_k, \qquad \varepsilon_k \sim \mathcal N(0, r)$$

Agent is a Kalman filter with possibly misspecified parameters $(\hat\lambda, \hat\sigma, \hat r)$. Policy: passive observer (no control yet; controlled case in §5).

Predictor state $\hat x_{k|k-1}$; innovation (AAD's mismatch)

$$\delta_k = y_k - \hat x_{k|k-1}$$

Steady-state innovation variance $\sigma_\nu^2 = \mathbb E[\delta_k^2]$ is the object. In AAD's Model S reading, $\rho^2 \equiv \nu \cdot \sigma_\nu^2$ (the innovation-driven disturbance power per unit time).

### 3.2 Innovation variance: the closed-form answer

Under correctly-specified parameters, the steady-state prediction covariance $P^\ast$ solves the algebraic Riccati equation; the innovation variance is

$$\sigma_\nu^2 \;=\; P^\ast + r. \qquad (\star)$$

Critically: the innovation variance is an **additive decomposition**, not a multiplicative one. $P^\ast$ (the prior-predictive variance) depends on $(\hat\lambda, \hat\sigma, \lambda_s, \sigma_\text{nat})$ and the sampling period. $r$ is observation noise.

**Can we force (★) into (R-F)?** Try:

$$\sigma_\nu^2 = \sigma_\text{nat}^2 / (2\hat\lambda) \cdot [\text{stuff}] + r$$

The first term contains both environment ($\sigma_\text{nat}^2$, $\lambda_s$) and agent ($\hat\lambda$) quantities; the second term is pure environment. There is no way to write this as a product $\rho_\text{ext} \cdot f(\mathcal M) \cdot g(\pi)$ with $f(\mathcal M)$ depending only on the model class and $\rho_\text{ext}$ depending only on the environment.

**The form $\sigma_\nu^2 = P^\ast + r$ is linear-additive in $P^\ast$ and $r$.** The *product* form would require $P^\ast$ and $r$ to combine as $P^\ast \cdot r$, which they do not.

### 3.3 Comparing against a reference agent

Try the max-entropy reference: agent predicts $\hat x^{\text{ref}}_{k|k-1} = 0$. Steady-state innovation variance:

$$\sigma_\nu^{\text{ref},2} = \mathbb E[y_k^2] = \sigma_\text{nat}^2/(2\lambda_s) + r. \qquad (\text{marginal})$$

Now the ratio:

$$\frac{\sigma_\nu^2}{\sigma_\nu^{\text{ref},2}} \;=\; \frac{P^\ast + r}{\sigma_\text{nat}^2/(2\lambda_s) + r} \;\in\; (0, 1]$$

This ratio is a legitimate $f(\mathcal M)$-like quantity relative to the max-entropy reference. It is **not** a product-of-independent-factors form. The ratio mixes environment ($\lambda_s, \sigma_\text{nat}, r$) and agent ($\hat\lambda, \hat\sigma, \hat r$ via $P^\ast$) in a non-factorable way.

Define

$$f^{\text{ratio}}(\mathcal M) := \frac{P^\ast(\mathcal M; \text{env}) + r}{\sigma_\text{nat}^2/(2\lambda_s) + r}$$

Two observations:

1. $f^{\text{ratio}}$ depends on the environment (through $\lambda_s, \sigma_\text{nat}, r$), not just the model class. The separation "agent-only" vs "environment-only" has failed at the factor level.
2. The ratio form *mathematically* is a quotient of sums, not a product of independent factors. Taking logs:

$$\log \sigma_\nu^2 - \log \sigma_\nu^{\text{ref},2} = \log(P^\ast + r) - \log(\sigma_\text{nat}^2/(2\lambda_s) + r)$$

has no Cauchy-FE-style additivity structure; the log of a sum doesn't decompose.

### 3.4 The deterministic limit $r \to 0$

In the limit $r \to 0$ (perfect observation), we get $\sigma_\nu^2 = P^\ast$ and $\sigma_\nu^{\text{ref},2} = \sigma_\text{nat}^2/(2\lambda_s)$, so

$$\frac{\sigma_\nu^2}{\sigma_\nu^{\text{ref},2}} = \frac{P^\ast}{\sigma_\text{nat}^2/(2\lambda_s)}.$$

Under correctly-specified $\hat\lambda = \lambda_s$, $\hat\sigma = \sigma_\text{nat}$, and $\nu \to \infty$ (continuous observation), one-step prediction is nearly exact, so $P^\ast \to 0$ and $f^{\text{ratio}} \to 0$. Under misspecified $\hat\lambda$, $P^\ast$ stays bounded away from zero even at $\nu \to \infty$ — the model's inability to track the true drift sets an irreducible floor.

**In this noiseless limit, the factorization (R-F) nominally works** — the ratio is bounded in $(0, 1]$ and depends primarily on the model class's adequacy. But $g(\pi) = 1$ identically (no policy control), so it's a one-factor decomposition, not a three-factor one. And we've still chosen an arbitrary reference ($\hat x = 0$); a different reference gives a different $f$.

**The $r \gt 0$ generic case blocks multiplicative factorization.** The sum structure $P^\ast + r$ is additive-irreducible: it reflects two independent noise sources (process innovations $\sigma_\text{nat}\,dW$ and observation noise $r$) that combine additively in variance.

### 3.5 Misspecification: separating "intrinsic" from "model-class-attributable"

Suppose the environment's true drift is $\lambda_s$ but the agent's model has $\hat\lambda \ne \lambda_s$. The Kalman filter minimizes MSE *within* its model class, so its steady-state $P^\ast$ is *worse than* the optimal $P^\ast_\text{opt}$ achievable under correct specification:

$$P^\ast(\hat\lambda) \;=\; P^\ast_\text{opt}(\lambda_s) \;+\; \text{misspecification penalty}(\hat\lambda - \lambda_s)$$

Working this out explicitly: under the filter's model, the Kalman gain is
$K = P^\ast / (P^\ast + r)$; but the environment produces innovations of magnitude
$P^\ast_\text{env} + r$ where $P^\ast_\text{env}$ is the *true* one-step variance of
$x_{t_{k+1}} - e^{-\hat\lambda/\nu} \hat x_{k|k-1}$. The misspecified filter converges
but to a sub-optimal operating point with $P^\ast \ge P^\ast_\text{opt}$.

Let me define:

- $\sigma_\nu^{2, \text{opt}}$: innovation variance under correctly-specified $\mathcal M_\text{opt}$
- $\sigma_\nu^{2, \mathcal M}$: innovation variance under model class $\mathcal M$
- $\sigma_\nu^{2, \text{ref}}$: innovation variance under max-entropy reference

Then

$$\sigma_\nu^{2, \mathcal M} = \sigma_\nu^{2, \text{opt}} + \Delta(\mathcal M)$$

where $\Delta(\mathcal M) \ge 0$ is the model-class-excess innovation variance. This is the Pythagorean-style bias-variance decomposition in prediction:

- $\sigma_\nu^{2, \text{opt}}$: **irreducible innovation** — what even the best model in a rich class cannot predict (the process's own stochasticity plus observation noise).
- $\Delta(\mathcal M)$: **reducible misspecification** — what the current model class is missing.

This is an **additive** decomposition in variance units. On log scale:

$$\log \sigma_\nu^{2, \mathcal M} = \log(\sigma_\nu^{2, \text{opt}} + \Delta(\mathcal M))$$

has no clean Cauchy-FE additive structure. The log of a sum doesn't split.

### 3.6 Verdict from Kalman

The linear-Gaussian case, worked end-to-end, says: **innovation variance is additive in the variance coordinate, not multiplicative in the rate coordinate.** The factorization (R-F) does not hold. The natural decomposition is

$$\underbrace{\sigma_\nu^{2, \mathcal M}}_{\text{total innovation}} \;=\; \underbrace{\sigma_\nu^{2, \text{opt}}}_{\text{irreducible}} \;+\; \underbrace{\Delta(\mathcal M)}_{\text{model-class-attributable}} \;+\; \underbrace{\Delta(\pi)}_{\text{policy-attributable (if controlled)}} \qquad (\text{log-R-F'})$$

additive in variance, not log-additive in rate. Taking square roots to convert to rate units (to match $\rho$'s definition in Model S, $\rho \sim \sqrt{\text{variance}} \cdot \sqrt\nu$) *still* doesn't factor multiplicatively: $\sqrt{A + B} \ne \sqrt A \cdot \sqrt B$.

## 4. Structured derivation 2 — Beta-Bernoulli edge

### 4.1 Setup

Consider a strategy DAG edge (per `#strategy-dag`) carrying confidence $p_{ij} \in (0, 1)$ updated by Bernoulli observations. The agent's model of the edge is a Beta distribution $\text{Beta}(\alpha_{ij}, \beta_{ij})$ with point-estimate $\hat p_{ij} = \alpha_{ij}/(\alpha_{ij} + \beta_{ij})$.

True success probability of the underlying event: $p^\ast_{ij}$. Agent's policy $\pi$ affects whether the edge is tested (action $a_t$ invokes this sub-plan, producing a Bernoulli sample).

"Disturbance" in the strategy-dynamics sense (`#strategic-dynamics-derivation`) is the rate at which the edge-credence process $p_{ij}(t)$ is driven away from its current estimate by incoming likelihood mass. Per `#edge-update-natural-parameter`'s log-odds form:

$$\lambda_{ij}^{\text{post}} = \lambda_{ij}^{\text{prior}} + \ell(y)$$

with log-likelihood ratio $\ell(y)$ of $+\log[p^\ast/(1-p^\ast)]$ on success and $-\log[p^\ast/(1-p^\ast)]$ on failure under a unit-noise Bernoulli channel.

### 4.2 Per-observation disturbance variance

Under the log-odds coordinate, the per-observation innovation is $\ell(y)$. Its variance (assuming $y$ is drawn from true probability $p^\ast$):

$$\text{Var}[\ell(y)] = p^\ast(1-p^\ast) \cdot \ell_0^2, \qquad \ell_0 := \log\!\tfrac{p^\ast}{1-p^\ast}$$

where $\ell_0$ is the log-likelihood ratio magnitude. Rate per unit time:

$$\rho_\Sigma^2 \cdot (\text{per edge}) \;=\; \nu_{\text{edge},\pi} \cdot p^\ast(1-p^\ast) \cdot \ell_0^2$$

Here $\nu_{\text{edge},\pi}$ is the rate at which the policy $\pi$ visits this edge — a pure agent-choice quantity (under `#causal-structure`'s temporal ordering, the agent's policy determines edge visits).

### 4.3 Attempted factorization

Try to write $\rho_\Sigma^2$ for this edge in the form (R-F):

$$\rho_\Sigma^2 \stackrel{?}{=} \rho_{\text{external}}^2 \cdot f(\mathcal M) \cdot g(\pi)$$

Candidates:
- $\rho_{\text{external}}^2 = p^\ast(1-p^\ast) \cdot \ell_0^2$ (pure environment: intrinsic Bernoulli variance weighted by log-likelihood-ratio magnitude, evaluated at the true probability).
- $g(\pi) = \nu_{\text{edge},\pi}/\nu_{\text{max}}$ (fraction of maximum edge-visit rate the policy uses).
- $f(\mathcal M) = ?$ — but there's no residual agent-model factor in the expression.

**The Beta-Bernoulli case factors (R-F) successfully *for the single edge*.** With two factors; no $f(\mathcal M)$ appears because, at the per-observation level, the Bernoulli innovation is model-free (it depends only on the true $p^\ast$ and the log-likelihood ratio).

**But this is just the per-observation variance times the per-observation rate.** Any stochastic disturbance in exponential-family form will factor as (rate per observation) × (intrinsic variance per observation). The "factorization" in this case is structural to any additive-Poisson-driven innovation — it's not specific to AAD, and it's *multiplicative in rate because the Poisson structure already makes it so*.

### 4.4 The multi-edge case

Extend to the full strategy DAG. The aggregate $\rho_\Sigma^2$ summed over edges:

$$\rho_\Sigma^2 = \sum_{(i,j) \in E} \nu_{\text{edge},\pi}(i,j) \cdot p^\ast_{ij}(1-p^\ast_{ij}) \cdot \ell_{0,ij}^2$$

**Summed over edges, not multiplied.** The policy's contribution is which edges it visits and at what rate; the intrinsic contribution is the per-edge variance. The model-class $\mathcal M$ enters only in *how the agent aggregates these into its plan*, not in the disturbance rate itself.

So the Beta-Bernoulli strategic-disturbance case gives:

$$\rho_\Sigma^2 = \sum_e \nu_{\pi,e} \cdot \sigma_e^2$$

which is **additive in edges, multiplicative in (rate × variance) per edge**. Trying to force this into $\rho = \rho_{\text{ext}} \cdot f \cdot g$ requires a violent compression that hides the additivity structure.

### 4.5 Verdict from Beta-Bernoulli

The per-edge form is multiplicative (two factors: rate × variance), but no $f(\mathcal M)$ appears. The aggregate form is additive across edges. The "three-factor product (R-F)" form is not visible in this setting.

**If anything, this is evidence that the cleanest AAD-native decomposition of disturbance is *additive* rather than *multiplicative*.** A pattern emerging from both §3 and §4: variance / second-moment / rate-squared quantities decompose *additively* across their structural components, not multiplicatively.

## 5. Structured derivation 3 — Controlled OU with LQR policy

### 5.1 Setup

Environment: OU with control input $u_t$

$$dx_t = (-\lambda_s x_t + b u_t) dt + \sigma_\text{nat} dW_t$$

Observation: $y_k = x_{t_k} + \varepsilon_k$, $\varepsilon_k \sim \mathcal N(0, r)$.

Agent: Kalman filter (correctly-specified) + LQR controller

$$u_t = -K_\text{LQR}(Q, R_u) \hat x_{t|t}$$

with quadratic cost $\int (Q x^2 + R_u u^2) dt$ shaping the gain $K_\text{LQR}$. The policy $\pi$ is controlled entirely by the cost ratio $Q/R_u$; small $Q/R_u$ gives a gentle (benign) controller, large $Q/R_u$ gives an aggressive one.

### 5.2 How does $\rho$ depend on policy?

**The predictor innovation $\delta_k = y_k - \hat x_{k|k-1}$ has variance $P^\ast + r$ that is *independent of the control gain*** under correctly-specified filtering. Why? Because the innovation is computed *before* the state update, and the effect of $u_{t_{k-1}}$ on $\hat x_{t_k|t_{k-1}}$ is known exactly by the agent (the control is the agent's own choice, fed through the agent's model).

In other words: **the control-input-affected part of the dynamics is *predictable by the agent*, so it doesn't enter $\delta$.** Only the unpredictable process noise $\sigma_\text{nat} dW$ does.

**Consequence:** in this setting, $g(\pi) = 1$ exactly. Policy choice does not reduce $\rho$. The policy only affects what *region of state space* the agent visits — it changes the *level* of $x_t$, not the *innovation rate*.

### 5.3 When does policy reduce $\rho$?

Policy reduces $\rho$ only when the environment's stochastic structure depends on state or action in ways the agent cannot predict. Three mechanisms:

1. **State-dependent noise.** If $\sigma_\text{nat}(x)$ grows with $x$ (e.g., process noise scales with state), then a policy that keeps $x$ small reduces innovation variance. Under Gaussian LQR-style filtering, state-dependent noise breaks the Kalman structure; the agent's predictor no longer matches the optimal Bayesian predictor, and $\rho$ picks up a policy-dependent term.
2. **Regime switching.** If the environment transitions between modes (linear / nonlinear, low-noise / high-noise), and the transition rate depends on state, then policy affects the mode-occupation distribution and thence average innovation rate.
3. **Adversarial or strategic environments.** If another agent's action (the environment) depends on ours (`#adversarial-destabilization`), then policy shapes the adversary's response, which shapes our innovation.

**Crucially, these are exactly the cases where the Kalman/LQR structure breaks.** In the clean sub-scope-$\alpha$ linear-Gaussian case, $g(\pi) \equiv 1$; $f(\mathcal M)$ is a ratio of sums, not a factor; $\rho_{\text{external}}$ is the marginal-predictor innovation variance, which itself depends on environment parameters.

### 5.4 A stronger observation: policy-benignity is not a reduction of $\rho$; it's a change of the *reference region*

When we say "the agent's policy keeps the environment benign," we often mean: the agent avoids state-space regions where the environment is volatile. But within the AAD framework, if the environment is Markov in $(x, u)$ and the agent correctly models both, then innovation is predictable away up to process noise, which is state-dependent only via explicit nonlinearities.

**The usual intuition about "policy benignity" corresponds to the agent's model class breaking down in some regions** — e.g., the LQR controller correctly models linear dynamics near the origin but not far-field nonlinearities. Policy keeps the agent near the origin, where the linear model is valid. This is policy-mediated $f(\mathcal M)$, not policy-mediated $\rho$-reduction.

### 5.5 Verdict from controlled OU

**Sub-scope-$\alpha$ (correctly-specified Kalman with LQR) makes $g(\pi) \equiv 1$.** Policy-benignity is not a factor of $\rho$ in this clean regime. When $g(\pi) \lt 1$ appears, it's because the model class is actually misspecified in some regions — i.e., $f(\mathcal M)$ is *state-dependent* and the policy selects the benign region. The factorization (R-F) collapses two agent-controllable factors into one: **$f(\mathcal M)$ is state-dependent, and $g(\pi)$ is the state-distribution the policy induces; they aren't independent**.

This is a deep observation. The parent spike treats $f$ and $g$ as independent factors. In reality, policy-benignity is a *statement about which region of the state space the policy visits*, which is the same thing as a *statement about which submodel of $\mathcal M$ is binding*. The two factors are entangled at the source.

## 6. What the three cases jointly say

### 6.1 Pattern across all three cases

| Case | Natural decomposition of $\rho$ (or $\rho^2$) | Is (R-F) forced? | What fails? |
|---|---|---|---|
| **Kalman (3)** | $\sigma_\nu^2 = P^\ast + r$; with reference-agent, $\sigma_\nu^2/\sigma_\nu^{\text{ref},2}$ is a ratio of sums | No | Variance is *additive* in independent noise sources; sum doesn't factor multiplicatively |
| **Beta-Bernoulli (4)** | $\rho_\Sigma^2 = \sum_e \nu_{\pi,e} \cdot \sigma_e^2$ | No | Disturbance is *additive across edges*; only per-edge form is multiplicative |
| **Controlled OU + LQR (5)** | $\sigma_\nu^2 = P^\ast + r$, independent of policy | Trivially but vacuously: $g(\pi) = 1$ | Policy-benignity conflates with model-class adequacy when the model is correctly specified |

**Common thread:** variance / second-moment / $\rho^2$ quantities decompose *additively* in AAD's natural settings. The multiplicative form (R-F) is imposed from outside; it is not emerging from the structure.

### 6.2 Where (R-F) comes from

(R-F) is a reasonable modeling choice if we interpret each factor as an **independent multiplicative attenuation of a raw base rate**:
- environment emits disturbance at raw rate $\rho_\text{ext}$;
- the agent's model captures fraction $(1 - f)$ of that, leaving $f \cdot \rho_\text{ext}$;
- the policy further attenuates by fraction $(1 - g)$, leaving $f \cdot g \cdot \rho_\text{ext}$.

This is the structure of an **independent-attenuation chain** (a cascaded channel). It is correct if and only if the three attenuations act on independent aspects of the disturbance signal. The three structured cases in §3–§5 show that this independence generically fails:
- in Kalman, model capture and observation noise *add*, not multiply (variance-additivity of independent noises);
- in Beta-Bernoulli, no model-factor appears — the innovation is model-free at the Bernoulli level;
- in OU + LQR, policy and model interact (policy selects the region where model is valid), violating independence.

### 6.3 The KL-coordinate comes out additive

Here's a curiosity. Taking the KL-divergence perspective: for a true process $p^\ast$ and a predictive model $q_{\mathcal M, \pi}$, the excess log-loss (or, equivalently, the innovation entropy excess) is

$$D_\text{KL}(p^\ast \| q_{\mathcal M, \pi}) = \text{information rate }(p^\ast) - \text{captured information rate}(\mathcal M, \pi).$$

Under natural independence assumptions on the sources of model error (the sources that $\mathcal M$ fails to capture vs. those that $\pi$ visits), the KL-excess decomposes *additively*:

$$D_\text{KL}(p^\ast \| q_{\mathcal M, \pi}) = \underbrace{H(p^\ast) - H(p^\ast_\text{opt-in-class})}_{\text{model-class gap}} + \underbrace{D_\text{KL}(p^\ast_\text{opt-in-class} \| q_{\mathcal M, \pi})}_{\text{estimation + policy gap}}$$

by the information-geometric Pythagorean theorem (Amari & Nagaoka 2000 §3.4; `ref/ay-2017-information-geometry.pdf`). The first term is the "model-class error"; the second is "everything else the agent could tighten given the class."

**In KL-coordinates, the decomposition is additive. In rate-squared coordinates, the decomposition is *also* additive (via Kalman §3). In log-rate coordinates (the one (R-F) commits to), the decomposition is *not* additive — it is the log of an additive sum.** This is strong evidence that the natural additive coordinate for disturbance-decomposition is **variance / information-rate**, not log-rate.

## 7. Does the `#additive-coordinate-forcing` pattern apply?

The meta-segment `#additive-coordinate-forcing` catalogs three instances where an AAD-internal additivity axiom forces a logarithmic coordinate via Cauchy's functional equation. Does (R-F) fit?

**The diagnostic from the meta-segment:**
> (a) is the decomposition multiplicative across independent factors?
> (b) is there an AAD-internal commitment that the decomposition should be additive?

**For (R-F):**
- (a) *claims* yes but §§3–5 show this claim fails generically (the natural structure is additive in variance, not multiplicative in rate);
- (b) there is no AAD-internal commitment that forces $\log \rho$ to be additive. The chain layer (probabilities along a chain) is a mathematical identity via the chain rule; the divergence layer (KL over DAG factorizations) has a chain-rule-additivity axiom; the update layer (log-odds) has an evidential-additivity axiom. The disturbance layer has no such axiom.

**Attempting to construct the axiom.** An "independence-of-attenuations axiom" would say: *if the environment, model, and policy act on independent aspects of the disturbance signal, then $\log \rho$ decomposes additively.* The Cauchy-FE argument would then force $\log \rho$ to be the unique additive coordinate on which this independence is respected. But:

1. The premise "act on independent aspects" is exactly what §§3–5 show *fails* in the natural AAD settings. It would be a stipulation, not a derived property.
2. Even granted the premise, the Cauchy-FE doesn't give a unique logarithmic coordinate for $\rho$; it gives a unique additive coordinate *on which the stipulation holds by construction*. That's a circular derivation.

**Conclusion: (R-F) is not a primary instance of `#additive-coordinate-forcing`.** It lacks the AAD-internal additivity axiom that makes the three primary instances load-bearing. The logarithmic coordinate here is *chosen* (to make the decomposition look log-additive), not *forced* by an independently-motivated axiom — exactly the "adjacent family member" pattern, not the "primary instance" pattern, in `#additive-coordinate-forcing`'s taxonomy.

## 8. The honest reframe

The three structured cases + the KL observation point to a consistent alternative. Let me state it.

### 8.1 Reframe 1 — additive variance decomposition

Replace (R-F) with a **variance-additive decomposition**:

$$\rho^2 = \rho^2_{\text{irreducible}} + \Delta_{\mathcal M}^2 + \Delta_\pi^2 + \text{cross terms} \qquad (\text{R-V})$$

where:

- $\rho^2_{\text{irreducible}}$: what even an optimal-in-class Bayesian agent cannot predict (corresponds to "process noise + observation noise" in Kalman, "Bernoulli sampling variance" in Beta-Bernoulli). This is the closest thing to "purely external," but still depends on the reference model class.
- $\Delta_{\mathcal M}^2$: excess innovation variance due to model class misspecification — how much extra unpredictability comes from using a class that cannot reach optimality.
- $\Delta_\pi^2$: excess innovation variance due to the policy visiting regions where the model is weaker or where the environment is more volatile.
- **cross terms:** coupling between $\mathcal M$ and $\pi$ (the policy-model entanglement of §5.4). Generically *not* zero.

This form is supported by:
- The bias-variance decomposition of prediction error (Geman et al. 1992);
- The Pythagorean theorem of information geometry (Amari & Nagaoka 2000 §3.4; `ref/ay-2017-information-geometry.pdf`);
- The Kalman innovation identity (§3);
- The rate-distortion / IB decomposition of prediction cost.

It has a cross term — which is honest. In feedback systems, model and policy interact.

### 8.2 Reframe 2 — KL-additive decomposition

Replace (R-F) with a **KL-divergence decomposition**:

$$D_\text{KL}(p^\ast \| q_{\mathcal M, \pi}) = D_\text{KL}(p^\ast \| q_{\mathcal M_\text{opt}}) + D_\text{KL}(q_{\mathcal M_\text{opt}} \| q_{\mathcal M}) + D_\text{KL}(q_{\mathcal M} \| q_{\mathcal M, \pi}) + \text{cross} \qquad (\text{R-KL})$$

This is a three-way Pythagorean decomposition (modulo cross-terms from non-nested projections). Each term has a clean AAD interpretation:

- First: **intrinsic-limit gap** (how much the best model in the class falls short of the true distribution — an identifiability lower bound for the class).
- Second: **model-class-attributable gap** (how far the current model is from the class optimum).
- Third: **policy-attributable gap** (how much the policy's state-distribution tilts the agent's predictor away from the model's ideal).

This is the *structured repair* version of (R-F): replace multiplicative factors with KL-additive contributions.

### 8.3 Reframe 3 — two-term decomposition

Replace (R-F) with a cleaner two-term split that doesn't try to separate $f$ from $g$:

$$\rho^2 = \rho^2_\text{irreducible}(\text{env}) + \Delta^2(\text{agent-controllable}) \qquad (\text{R-2T})$$

Agent-controllable part subsumes both model-class and policy contributions without claiming they are independent. This concedes the fine internal decomposition but preserves the coarse one.

### 8.4 Comparison of reframes

| Form | Structural coordinate | Cross terms | AAD-internal motivation | Preserves parent spike's internal vs external narrative? |
|---|---|---|---|---|
| (R-F) *(original)* | log-rate | absent by assumption (generically wrong) | none (no additivity axiom) | Yes, cleanly — but misleadingly |
| (R-V) *(additive variance)* | variance | present, honest | bias-variance identity | Yes, with cross terms |
| (R-KL) *(KL-additive)* | information-geometric | present (non-nested projections) | Pythagorean + IB lineage | Yes, more rigorous |
| (R-2T) *(two-term)* | variance | absent (collapsed) | bias-variance identity (coarse) | Yes, with fine split dropped |

**My recommendation:** (R-V) with cross terms is the honest technical statement; (R-2T) is the honest presentational form if the fine $f$-vs-$g$ split is not needed; (R-KL) is the strongest result if the agent has a Bayesian / exponential-family structure where the Pythagorean theorem applies cleanly (sub-scope $\alpha$).

## 9. Connection map to existing AAD quantities

| AAD quantity | How (R-F) wanted it | How the honest reframe uses it |
|---|---|---|
| `#mismatch-decomposition` | (not directly used) | Central — the per-instant bias-variance identity is exactly the starting point for (R-V). Cross-sectional; (R-V) integrates it over time |
| `#model-class-fitness` ($\mathcal F(\mathcal M)$) | supplied $f(\mathcal M)$ as a direct multiplicative factor | supplies a *ceiling* for the reducible-model-error term $\Delta_{\mathcal M}^2$; not a factor but an upper bound on one term |
| `#model-sufficiency` | (not directly used) | $S(M_t) \lt 1$ corresponds to positive $\Delta_{\mathcal M}^2$; $S(M_t) = 1$ drives the model-class term to zero |
| `#loop-interventional-access` | supplied $g(\pi)$ implicitly (policy chooses which disturbance the agent sees) | supplies the mechanism whereby $\Delta_\pi^2$ exists at all — the policy couples action to next observation |
| `#ciy-observational-proxy` | (not directly used) | the regime structure (A/B/C) governs whether the cross terms between $\Delta_{\mathcal M}^2$ and $\Delta_\pi^2$ can be estimated |
| `#adaptive-tempo` / `#update-gain` | (not directly used in $\rho$ decomposition) | these are the *other side* of the persistence inequality; they determine $\alpha$, not $\rho$. The factorization error is *only* in $\rho$; the $\alpha$ factorization (§3.1 of parent spike) is fine |
| `#information-bottleneck` | (not directly used) | (R-KL) is the rate-distortion specialization of the IB objective where $\beta$-varying picks out different points on the Pareto curve between $\rho^2_\text{irreducible}$ and $\Delta^2_{\mathcal M}$ |

Additionally: Imai et al. 2010 causal mediation analysis is the right framework for quantifying the cross terms in (R-V). The parent spike's §5 lists four confounding channels; those channels are *precisely* the sources of the cross terms.

## 10. The strengthen-first attempt

The brief asks for strengthen-first: before concluding obstruction, try hard to derive (R-F) under specific structured cases.

**I tried the following paths:**

1. **Linear-Gaussian Kalman (§3).** Attempted to write $\sigma_\nu^2 = P^\ast + r$ as a product. Failed: sum of independent variances is additive, not multiplicative. The log of the sum has no Cauchy-FE structure.

2. **Beta-Bernoulli edge (§4).** Attempted to write the per-edge innovation as a product of three factors. Succeeded for the per-edge factor but only with two factors (rate × variance), and with no $f(\mathcal M)$ factor at all. Multi-edge aggregate is additive across edges.

3. **Controlled OU + LQR (§5).** Attempted to separate policy-benignity from model-class expressiveness. Found that in the correctly-specified sub-scope-$\alpha$ regime, $g(\pi) \equiv 1$; policy only matters when the model is misspecified in some regions, which makes $g$ and $f$ entangled.

4. **Cauchy-FE forcing argument (§7).** Attempted to manufacture an AAD-internal additivity axiom (independence-of-attenuations) that would force $\log \rho$ additive. Failed: the axiom's premise (independent aspects) is what §§3–5 show fails generically.

5. **Sub-scope $\alpha$ restriction.** Attempted to hold the factorization to the narrower regime. Under sub-scope $\alpha$, (R-F) is strictly *vacuous* (policy doesn't enter) or *degenerate* (model is correctly specified, so $f = 1$). Outside sub-scope $\alpha$ — where (R-F) might be empirically useful — the structure isn't there.

**All paths fail cleanly under close examination.** The obstruction is not a technical gap; it's a structural mismatch between the multiplicative form (R-F) and the additive-in-variance natural structure of AAD disturbance.

## 11. Assumption exercise: when does (R-F) nevertheless hold approximately?

The brief asks to characterize honest obstruction. An honest obstruction includes *where the heuristic nevertheless holds*, since the parent spike's presentation may still be useful operationally.

**Scenarios where (R-F) is approximately correct:**

1. **Small-$\Delta$ regime.** When $\Delta_{\mathcal M}^2 \ll \rho^2_\text{irreducible}$ and $\Delta_\pi^2 \ll \rho^2_\text{irreducible}$:

$$\log \rho^2 = \log(\rho^2_\text{irr} + \Delta_{\mathcal M}^2 + \Delta_\pi^2) = \log \rho^2_\text{irr} + \log(1 + \Delta_{\mathcal M}^2/\rho^2_\text{irr} + \Delta_\pi^2/\rho^2_\text{irr})$$

$$\approx \log \rho^2_\text{irr} + \Delta_{\mathcal M}^2/\rho^2_\text{irr} + \Delta_\pi^2/\rho^2_\text{irr}$$

by $\log(1 + x) \approx x$ for small $x$. The additive structure emerges as a *first-order Taylor approximation* around "near-optimal model + near-optimal policy." In this small-$\Delta$ regime, the separate contributions of model and policy are approximately independent, and the decomposition (R-F) approximately holds — but with meanings $\log f(\mathcal M) \approx -\Delta_{\mathcal M}^2/\rho^2_\text{irr}$ and $\log g(\pi) \approx -\Delta_\pi^2/\rho^2_\text{irr}$ (the log is not of the factors themselves but of the normalized variance contributions).

2. **Separable-source regime.** When the environment has genuinely independent noise sources (e.g., observation noise and process noise are uncorrelated), and the model class addresses exactly one of them, and the policy addresses exactly the other. Highly stylized; rarely true in practice.

3. **Multi-stage channel cascade.** When the disturbance genuinely passes through independent multiplicative channels: environment → model filter → policy filter → observed mismatch. This requires a *channel* interpretation where each filter is independent. Under sub-scope $\alpha$ Gaussian channels with independent noise, this would reduce to the Gaussian case (§3) which *doesn't* factor multiplicatively. Under non-Gaussian channels, the factorization would depend on specific entropy inequalities that are rarely tight.

**Operational conclusion for TST:** in high-performing teams on well-understood codebases, the small-$\Delta$ regime is plausible — model error is small, policy error is small, both are ~1st-order perturbations over irreducible complexity. In this regime, the (R-F) log-additive decomposition is approximately right. In high-stakes settings (novel domains, new teams, messy codebases), the $\Delta$-terms are large, cross terms dominate, and (R-F) breaks down.

## 12. Does the decomposition work in KL-units even when it fails in rate-units?

Worth checking directly: does $D_\text{KL}(p^\ast \| q_{\mathcal M, \pi}) = D_\text{KL,ext} + D_\text{KL}(\mathcal M) + D_\text{KL}(\pi)$ hold cleanly?

**The Pythagorean answer.** Amari-Nagaoka §3.4: if $q_{\mathcal M, \pi}$ is the I-projection of $p^\ast$ onto the $(\mathcal M, \pi)$-family, and the family is e-flat, m-flat, or mixed-flat, then KL decomposes exactly when projections are along orthogonal directions.

For nested classes $\mathcal M \subset \mathcal M_\text{opt}$ with the projection structure:
- $p^\ast \to q_\mathcal M$ in one step: $D_\text{KL}(p^\ast \| q_\mathcal M) = D_\text{KL}(p^\ast \| q_{\mathcal M_\text{opt}}) + D_\text{KL}(q_{\mathcal M_\text{opt}} \| q_\mathcal M)$ by Pythagoras, **only if** the projections are orthogonal in the information-geometric sense (typically: $\mathcal M$ is an exponential sub-family of $\mathcal M_\text{opt}$ in e-coordinates, and $p^\ast$ projects along m-geodesics).

For policy-induced distributional shifts, the story is subtler: policy changes the sampling distribution (not just the model), so the "policy contribution" is not strictly a projection but a measure change. The KL decomposition picks up a term that is not orthogonal to the model-class gap.

**Pragmatic verdict.** In sub-scope $\alpha$ (Gaussian families, exponential-family models, conjugate-Bayesian updates), the KL-additive decomposition (R-KL) is *approximately* exact when the e-coordinates align with the structural splits. In full generality, cross terms appear. This is *strictly stronger* than (R-F) — KL-additivity holds under cleaner conditions than rate-log-additivity — and it does not require the full multiplicative factorization.

## 13. Impact on the parent spike

The parent spike (`msc/spike-internal-external-decomposition.md`) assembles $\mathcal V = \mathcal V_E + \mathcal V_I$ with specific constituent terms. Let me trace how each component is affected.

**Components whose (R-F)-factor is load-bearing:**

- $\log \rho_\text{external}$ in $\mathcal V_E$: this is supposed to be a pure-environment quantity. After (R-V)/(R-KL), the corresponding quantity is $\tfrac{1}{2}\log \rho^2_\text{irreducible}$ — the irreducible-innovation log-variance *relative to the optimal class*. Not pure-environment; it depends on the reference class.
- $-\log f(\mathcal M)$ in $\mathcal V_I$: the "richer model predicts more" factor. After (R-V), this is $-\tfrac{1}{2}\log(1 + \Delta_{\mathcal M}^2/\rho^2_\text{irreducible})$ in the small-$\Delta$ regime; an additive KL-gap in (R-KL).
- $-\log g(\pi)$ in $\mathcal V_I$: the policy-benignity factor. After (R-V), this is coupled to $-\log f(\mathcal M)$ via cross terms — not an independent additive contribution.

**Components unaffected:**

- The $\alpha$-side decomposition in §3.1 of the parent spike is fine. $\alpha = \eta^\ast \cdot c_\text{min}$ and $\mathcal T = \nu \cdot \eta^\ast$ are derived, not hypothesized. Their internal-vs-external attribution has its own subtleties (each factor is "mixed") but this is honestly reported in the parent spike.
- $\lVert \delta_\text{critical}\rVert$ and $h(O_t)$: the task-toughness factors. These are genuinely external (domain) and internal (objective-chosen), and the parent spike's split is plausible. Not affected by $\rho$-factorization issues.
- The coarse decomposition $\mathcal V = \log \lVert \delta_\text{crit}\rVert - \log \rho + \log \alpha$ is exact. The internal-external split at this coarse level is well-posed.
- The regime A/B/C identifiability analysis is fine. It is an independent result about whether $\mathcal V_E$ and $\mathcal V_I$ are separately identifiable, and does not depend on how the fine decomposition is done.

### 13.1 Recommended revision for the parent spike

The parent spike should be revised along the following lines:

1. **Retain the coarse $\mathcal V = \log \lVert \delta_\text{crit}\rVert - \log \rho + \log \alpha$ decomposition at exact tier.** This is unaffected.
2. **Retain the $\alpha$-side decomposition.** This does not use (R-F).
3. **Replace the $\rho$-side factorization (R-F) with either (R-V) or (R-2T).** The fine decomposition then becomes:
   - *(R-V) version:* $\mathcal V_I$ contains a term $-\tfrac{1}{2}\log(\rho^2_\text{irr} + \Delta_{\mathcal M}^2 + \Delta_\pi^2 + \text{cross})/\rho^2_\text{irr}$, which in the small-$\Delta$ regime approximates $-\tfrac{1}{2}(\Delta_{\mathcal M}^2 + \Delta_\pi^2)/\rho^2_\text{irr}$ — first-order-additive in the squared-excess variances, with cross-terms of order $\Delta^4$.
   - *(R-2T) version:* $\mathcal V_I$ contains a single aggregated "agent-controllable disturbance reduction" term, without separate $f$ and $g$ factors.
4. **Downgrade the overall tier.** The coarse form remains *exact* for Model D linear; the fine form with (R-V) is *conditional* (on the independence-of-sources Pythagorean conditions holding approximately, which is a sub-scope-$\alpha$ assumption) and in the full-generality case is *heuristic / first-order-approximation*.
5. **The confounding discussion in §5 of the parent spike should be preserved but reframed.** The four confounding channels now manifest as cross terms in (R-V), not as coupling between independent multiplicative factors. This is *more rigorous*, not less — the cross terms have explicit mediation-analysis interpretation (Imai et al. 2010).

### 13.2 Impact on the `#discussion-identifiability-floor` claim

The parent spike's §5.3 claims the decomposition is Instance 3 of the identifiability-floor pattern. This claim *survives* the reframe, but with a slightly different content: under Regime C (observational, fixed coupling), the full (R-V) decomposition with its cross terms is not identifiable; under Regime A (rotation / natural experiments) the decomposition *with cross terms treated as a third identifiable quantity* (mediation analysis) becomes identifiable. The Instance 3 status is preserved.

### 13.3 Impact on `#discussion-separability-pattern` ladder

The seventh ladder (internal-external attribution) stands. The "separable core" is the Regime A case under the coarse decomposition; the "structured repair" is (R-V) under functional-form assumptions (the cross terms) + Regime B; the "general open" is (R-V) under Regime C with unrestricted cross terms. The pattern positioning is actually *strengthened* by the reframe, because the structured-repair ring now has a concrete technical content (mediation analysis on the cross terms) rather than "functional-form assumptions on $f, g, h, Q$" as abstract placeholders.

## 14. Outcome: (C) — honest obstruction + reframe

**The research question was:** Can (R-F) be derived from more primitive AAD quantities, or is it a modeling choice?

**Answer:** It is a modeling choice, and the structural cases show it is an *incorrect* choice. AAD's natural disturbance-decomposition structure is additive-in-variance (§3, §4) and additive-in-KL (§12), not multiplicative-in-rate. The factorization (R-F) works only in a small-$\Delta$ first-order regime where $\log(1+x) \approx x$, and even there the decomposition is *variance-additive* rather than *rate-multiplicative*; the log-factor presentation of the parent spike hides this.

**The honest reframe is (R-V) — the variance-additive decomposition with explicit cross terms** — or its strengthened cousin (R-KL) — the KL-additive information-geometric form — either of which recovers the fine internal-external attribution without the invented multiplicative structure.

**Specific findings:**

1. **$\rho$ is agent-conditional.** The AAD equations define $\rho$ as the innovation the agent's predictor fails to absorb — not an environment-intrinsic quantity. $\rho_\text{external}$ is not well-defined without choosing a reference agent, and different reference choices yield different numerical $\rho_\text{external}$.

2. **Variance-additivity is the natural structure.** Kalman innovation is $P^\ast + r$, not $P^\ast \cdot r$. Beta-Bernoulli aggregate is a sum over edges, not a product. This is a consequence of how independent noise sources combine (variance-additivity), which is structural to stochastic processes, not a contingent AAD modeling choice.

3. **$g(\pi)$ and $f(\mathcal M)$ are not independent.** In the clean sub-scope-$\alpha$ case (Kalman + LQR, correctly specified), $g(\pi) \equiv 1$. When $g(\pi) \lt 1$ appears, it is because the model class is state-dependent: policy selects the region where the model is adequate. This is not two independent factors; it is one factor (model-class adequacy) modulated by another (policy-induced state distribution).

4. **No AAD-internal additivity axiom motivates $\log \rho$ decomposition.** The `#additive-coordinate-forcing` pattern needs an axiom like "this should decompose additively under AAD-internal conditions X"; no such X is on offer for $\log \rho$. The three primary instances (chain / divergence / update) each have such an axiom; the disturbance layer does not.

5. **The small-$\Delta$ Taylor expansion is where (R-F) is approximately correct.** In the regime where the model is near-optimal and the policy is near-benign, the variance-additive decomposition linearizes to a log-additive form. This is an approximation, not a derivation, and has to be flagged as such.

**Recommended actions for the parent spike:**

- Replace (R-F) with (R-V) in the fine-decomposition section. Keep the small-$\Delta$ approximation as an optional first-order reading with explicit scope.
- Downgrade the fine decomposition from *robust-qualitative* to *conditional* (under first-order approximation) or *heuristic* (in general).
- Preserve the coarse decomposition $\mathcal V = \log\lVert\delta_\text{crit}\rVert - \log\rho + \log\alpha$ at *exact* tier — this is unaffected.
- Reframe the confounding analysis in §5 of the parent spike as *cross terms in a variance decomposition* rather than *coupling between independent multiplicative factors*. This is a technical upgrade: mediation analysis (Imai et al. 2010) gives concrete quantitative content to cross terms; "coupling between multiplicative factors" was always hand-wavy.
- Keep `#discussion-identifiability-floor` Instance 3 status. Under Regime C, the cross-terms are not separately identifiable; under Regime A, rotation-style experiments resolve them.
- Keep `#discussion-separability-pattern` seventh-ladder status. The separable core + structured repair + general open frame survives.

**Recommendation for promotion of the parent spike:** With the reframe, the parent spike can be promoted to `#internal-external-decomposition` (new appendix segment) at *conditional* tier for the fine decomposition and *exact* for the coarse decomposition. Without the reframe, the (R-F) weakest link forces the fine decomposition to *heuristic*, which erodes the value of the fine split.

## 15. Open questions

1. **Can the cross terms be characterized under sub-scope $\alpha$?** The Pythagorean theorem of information geometry gives clean conditions under which the KL decomposition is exactly orthogonal (zero cross terms). For exponential-family models with e-flat model class and m-flat policy-induced measure change, this could deliver a clean (R-KL) result. Worth a separate spike.

2. **What is the natural additive coordinate for disturbance?** The evidence from §§3–4 and §12 is that it is *variance* (for Gaussian-like families) or *information-divergence* (for exponential-family generalization), not *log-rate*. Is there a unifying principle that names which coordinate a given AAD quantity should decompose in? This might strengthen `#additive-coordinate-forcing`'s typology.

3. **Is there a non-trivial factorization in rate under any AAD sub-scope?** The three structured cases and the Cauchy-FE argument suggest no, but I have not checked heavy-tailed, discrete-time, or non-stationary cases exhaustively. A negative result (proven impossibility of multiplicative factorization under stationarity + Markov + exponential-family) would close this question definitively.

4. **Does the (R-V) cross-term structure compose under agent composition (Section III)?** The parent spike's §12.5 notes composition as out-of-scope. (R-V) composes additively in variance, so the cross-term composition question is whether the inter-agent cross terms are cleanly bounded. This bears on the `#composition-closure` machinery.

5. **TST-specific: is the policy-benignity / model-class-expressiveness entanglement visible in TST metrics?** The parent spike's §8.2 lists per-component exactness. The reframe says $f$ and $g$ are entangled at source; TST coupling metrics (`#system-coupling`) may already be catching this entanglement rather than separating it. Worth a specific TST-specialization note.

## 16. Summary

- **Problem.** The $\rho = \rho_\text{ext} \cdot f(\mathcal M) \cdot g(\pi)$ factorization is a working hypothesis in the internal-external-decomposition spike; its status determines whether the fine decomposition can be promoted.
- **Approach.** Three structured derivations (scalar linear-Gaussian Kalman; Beta-Bernoulli edge; controlled OU with LQR) + Cauchy-FE forcing argument + AAD-internal axiom search.
- **Outcome.** (C) Obstruction with honest reframe. (R-F) is a modeling choice, not derivable; worse, it misrepresents the natural structure, which is variance-additive (R-V) or KL-additive (R-KL) with generic cross terms.
- **Four specific findings.** (1) $\rho$ is agent-conditional, not environmental. (2) Variance-additivity is the native structure. (3) $f$ and $g$ are not independent — they entangle at source. (4) No AAD-internal additivity axiom motivates $\log\rho$ decomposition.
- **Honest reframe.** (R-V): $\rho^2 = \rho^2_\text{irr} + \Delta_{\mathcal M}^2 + \Delta_\pi^2 + \text{cross}$, variance-additive with explicit cross terms. (R-2T): agent-controllable vs environment-irreducible two-term split if the fine decomposition is not essential. (R-KL): information-geometric Pythagorean decomposition, strongest under sub-scope $\alpha$.
- **Impact on parent spike.** Coarse decomposition survives at *exact*; fine decomposition is *conditional* under (R-V) first-order approximation or *heuristic* in general. `#discussion-identifiability-floor` Instance 3 status survives; `#discussion-separability-pattern` seventh-ladder status survives. `#additive-coordinate-forcing` is *not* a primary instance; the logarithmic coordinate here is *matched rather than forced*, like the Lyapunov and IB adjacent-family members.
- **Small-$\Delta$ regime.** (R-F) is approximately correct as a first-order Taylor expansion around near-optimal model + near-benign policy. This is an honest special case, not a derivation.
- **Recommendation.** The parent spike should promote with the (R-V) reframe: retain the coarse decomposition at exact tier; express the fine decomposition with explicit cross terms; downgrade the fine tier from *robust-qualitative* to *conditional* (with small-$\Delta$ scope) or *heuristic* (in general). This is still a substantial contribution — the coarse decomposition, the regime structure, the identifiability-floor instance, and the separability-pattern ladder all stand.

---

*End of spike. The factorization (R-F) is obstructed; the honest reframe (R-V) is the variance-additive Pythagorean-style decomposition with explicit cross terms. The parent spike's fine decomposition should be re-expressed in (R-V) form; its coarse decomposition is unaffected.*
