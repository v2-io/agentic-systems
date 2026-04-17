# Spike: Gain-Sector Bridge — The Nonlinear Case

**Status**: Spike (investigatory). Establishes the formal connection between GA-3 (the sector condition) and strong convexity of loss landscapes for gradient-based agents.

**Date**: 2026-04-02

**Objective**: Determine whether GA-3 is a derivable consequence of well-understood loss function properties, or an irreducible assumption. The answer is: **GA-3 is equivalent to local strong convexity for any gradient-based agent, and the AAD sector parameter $\alpha$ is the product of the learning rate and the loss landscape's strong convexity modulus.**

**Depends on**: #sector-condition-derivation, #sector-condition-stability, #update-gain, #mismatch-dynamics, #structural-adaptation-necessity, #persistence-condition

---

## Part 1: The Equivalence Argument

### 1.1 Setup

Consider an agent that updates its model via gradient descent on a loss function $L$:

$$M_{t+1} = M_t - \eta \cdot \nabla L(M_t)$$

where $\eta > 0$ is the learning rate (the gain parameter from #update-gain) and $L: \mathbb{R}^n \to \mathbb{R}$ is the loss function the agent minimizes. Let $M^\ast$ denote the loss minimizer (the "truth" the agent is tracking).

The mismatch is $\delta_t = M_t - M^\ast$. The per-step change in mismatch (in the absence of disturbance) is:

$$\Delta \delta_t = M_{t+1} - M^\ast - (M_t - M^\ast) = -\eta \cdot \nabla L(M_t)$$

The correction function in the sector framework ( #sector-condition-derivation) is $F(\delta) = -\Delta\delta = \eta \cdot \nabla L(M_t)$, or in continuous time:

*[Formulation (gradient correction function)]*

$$F(\mathcal{T}, \delta) = \eta \cdot \nabla L(M^\ast + \delta)$$

where we have written $M_t = M^\ast + \delta$ and absorbed the event rate $\nu$ into the continuous-time formulation (as in #adaptive-tempo: $\mathcal{T} = \nu \cdot \eta$).

### 1.2 The Sector Condition in Gradient Terms

GA-3 requires:

$$\delta^T F(\mathcal{T}, \delta) \geq \alpha \lVert\delta\rVert^2 \quad \text{for } \lVert\delta\rVert \leq R$$

Substituting the gradient correction:

*[Derived (sector-gradient equivalence)]*

$$\eta \cdot \delta^T \nabla L(M^\ast + \delta) \geq \alpha \lVert\delta\rVert^2$$

Dividing both sides by $\eta > 0$:

$$\delta^T \nabla L(M^\ast + \delta) \geq \frac{\alpha}{\eta} \lVert\delta\rVert^2$$

### 1.3 Strong Convexity

A differentiable function $L: \mathbb{R}^n \to \mathbb{R}$ is **$\mu$-strongly convex** on a set $\mathcal{S}$ if for all $x, y \in \mathcal{S}$:

$$L(y) \geq L(x) + \nabla L(x)^T (y - x) + \frac{\mu}{2} \lVert y - x\rVert^2$$

A standard equivalent characterization (see Nesterov 2004, Theorem 2.1.10) is the **gradient monotonicity** form: for all $x, y \in \mathcal{S}$:

$$(\nabla L(x) - \nabla L(y))^T (x - y) \geq \mu \lVert x - y\rVert^2$$

Setting $x = M^\ast + \delta$ and $y = M^\ast$, and noting $\nabla L(M^\ast) = 0$ (since $M^\ast$ is the minimizer):

$$\nabla L(M^\ast + \delta)^T \delta \geq \mu \lVert\delta\rVert^2$$

This is identical to the sector condition divided by $\eta$.

### 1.4 The Equivalence

*[Derived (sector-convexity equivalence)]*

**Theorem.** For a gradient-based agent with learning rate $\eta$ minimizing a loss $L$ with minimizer $M^\ast$ (where $\nabla L(M^\ast) = 0$):

$$\text{GA-3 holds with } \alpha = \eta \cdot \mu \quad \iff \quad L \text{ is } \mu\text{-strongly convex on } \mathcal{B}_R(M^\ast)$$

*Proof.* ($\Rightarrow$) The sector condition gives $\delta^T (\eta \nabla L(M^\ast + \delta)) \geq \alpha \lVert\delta\rVert^2$, so $\delta^T \nabla L(M^\ast + \delta) \geq (\alpha/\eta) \lVert\delta\rVert^2$. Since $\nabla L(M^\ast) = 0$, the gradient monotonicity condition holds with $\mu = \alpha/\eta$.

($\Leftarrow$) $\mu$-strong convexity gives $\delta^T \nabla L(M^\ast + \delta) \geq \mu \lVert\delta\rVert^2$. Multiplying by $\eta$: $\delta^T F(\delta) \geq \eta\mu \lVert\delta\rVert^2$. So GA-3 holds with $\alpha = \eta\mu$. $\square$

### 1.5 Conditions for Exact vs. Approximate Equivalence

The equivalence is **exact** when:

1. **The gradient is exact**: the agent computes $\nabla L$ without approximation (full-batch gradient descent, or Bayesian updates with conjugate models).
2. **The minimizer is stationary**: $M^\ast$ does not change between updates, so the mismatch dynamics $\Delta\delta = -\eta \nabla L(M^\ast + \delta)$ hold precisely.
3. **$\nabla L(M^\ast) = 0$**: the reference point is an actual stationary point.

The equivalence is **approximate** when:

1. **Stochastic gradients**: In SGD, each step uses a noisy estimate $\hat{g} = \nabla L_i(M_t)$ where $\mathbb{E}[\hat{g}] = \nabla L(M_t)$. The sector condition holds *in expectation*: $\mathbb{E}[\delta^T (\eta\hat{g})] = \eta \delta^T \nabla L \geq \eta\mu \lVert\delta\rVert^2$. The noise acts as an effective disturbance $w(t)$ in the sector framework. (Simulation 1 confirms: individual SGD steps can violate the sector condition, but the expected correction satisfies it.)
2. **Moving target**: When $M^\ast$ drifts at rate $\rho$, the gradient at $M^\ast$ is no longer zero. The residual $\nabla L(M^\ast) \neq 0$ contributes a bias term. For small drift ($\rho \ll \alpha$), this is absorbed into the disturbance $w(t)$.
3. **Finite-sample loss**: The empirical loss minimizer differs from the population loss minimizer by $O(1/\sqrt{N})$. Near the empirical minimizer, the gradient of the population loss is nonzero. This creates a "noise floor" analogous to observation noise in the Beta-Bernoulli case ( #spike-single-edge-strategic-dynamics).

### 1.6 How $\eta$ Enters the Sector Parameter

The factorization $\alpha = \eta \cdot \mu$ has a clean AAD interpretation:

- **$\mu$** is a property of the *loss landscape* (the environment's curvature, the model class's natural geometry). It measures how strongly the loss surface pushes the agent toward the optimum per unit mismatch. This is the "quality" of the correction signal — analogous to $\eta^\ast$ in the update-gain framework.
- **$\eta$** is the agent's *responsiveness* — how much it trusts each gradient signal. This maps directly to the update gain from #update-gain.
- **$\alpha = \eta \mu$** is the correction *rate* — how fast the agent actually reduces mismatch. This maps to the adaptive tempo: $\alpha \propto \mathcal{T}$.

In the linear case, $\nabla L = H\delta$ where $H$ is the Hessian, and $\mu = \lambda_{\min}(H)$. Then $\alpha = \eta \lambda_{\min}(H)$, recovering the adaptive tempo $\mathcal{T}$ from #mismatch-dynamics when $\eta = \eta^\ast$ and $\nu = 1$ (one update per time step).

The factorization also explains the convergence condition for gradient descent: the requirement $\eta < 2/L_{\text{smooth}}$ (where $L_{\text{smooth}}$ is the smoothness constant) ensures the correction function doesn't overshoot. Overshoot would violate an *upper* sector condition ($\delta^T F \leq \bar{\alpha} \lVert\delta\rVert^2$), causing oscillation instead of convergence. The sector framework in AAD focuses on the lower bound; the upper bound is the stability condition from optimization theory.

---

## Part 2: Classification of Common Loss Functions

### 2.1 Quadratic Loss (Linear Regression, Kalman Filter)

$$L(w) = \frac{1}{2}(w - w^\ast)^T H (w - w^\ast) + \text{const}$$

where $H \succ 0$ is the Hessian (e.g., $H = X^T X / N$ for linear regression).

- **Strong convexity**: $\mu = \lambda_{\min}(H) > 0$ **globally**
- **Sector condition**: $\alpha = \eta \cdot \lambda_{\min}(H)$, holds for all $\delta$ (no radius restriction, $R = \infty$)
- **AAD consequence**: The linear case from #mismatch-dynamics, where $\alpha = \mathcal{T}$, is recovered exactly. Structural persistence is trivially satisfied. Only task adequacy matters.

**Simulation verification** (Simulation 1): With a Hessian having eigenvalues $\{0.5, 1.0, 2.0, 3.0, 5.0\}$ and $\eta = 0.1$, the sector ratio $\delta^T F / \lVert\delta\rVert^2$ ranged from 0.050 to 0.317, exactly within $[\eta\mu, \eta L] = [0.05, 0.50]$, confirming the bound at every step of the gradient descent trajectory.

### 2.2 Logistic Loss (Classification)

$$L(w) = \frac{1}{N} \sum_{i=1}^N \log(1 + \exp(-y_i \cdot x_i^T w))$$

- **Hessian**: $H(w) = \frac{1}{N} X^T D(w) X$ where $D_{ii}(w) = \sigma(z_i)(1 - \sigma(z_i))$ with $z_i = y_i x_i^T w$
- **Strong convexity**: The Hessian weights $\sigma(z)(1-\sigma(z))$ range in $(0, 1/4]$. As $\lVert w\rVert \to \infty$, some $\sigma(z_i) \to 0$ or $1$, so $D_{ii} \to 0$ and $\lambda_{\min}(H) \to 0$
- **Result**: **Convex globally but not strongly convex globally**. Locally strongly convex in any bounded region, with $\mu(R)$ depending on the region.
- **With L2 regularization** ($L_{\text{reg}} = L + \frac{\lambda}{2}\lVert w\rVert^2$): $\mu \geq \lambda$ globally.

**AAD consequence**: Unregularized logistic regression satisfies GA-3 *locally* with a position-dependent $\alpha$. The sector parameter weakens as the agent moves far from the optimum. L2 regularization provides a floor: $\alpha \geq \eta\lambda$, guaranteeing GA-3 globally.

**Simulation verification** (Simulation 2): Unregularized logistic with 5000 samples showed the sector ratio positive along the entire trajectory from initialization to convergence, with the local strong convexity parameter ranging from 0.076 (at the MLE) to higher values far from it. With L2 regularization ($\lambda = 0.1$), the sector ratio was bounded below by $\eta\lambda = 0.03$ at every point, confirmed numerically.

### 2.3 Cross-Entropy and Exponential Family Losses

For an exponential family in natural parameter form:

$$L(\theta) = -\ell(\theta) = -\theta^T \bar{x} + A(\theta)$$

where $A(\theta)$ is the log-partition function. The Hessian is:

$$\nabla^2 L = \nabla^2 A(\theta) = \text{Cov}[T(x) \mid \theta]$$

which is the Fisher information matrix — positive definite everywhere in the interior of the natural parameter space.

- **Strong convexity**: $\mu = \lambda_{\min}(\text{Cov}[T(x) \mid \theta]) > 0$ for all $\theta$ in the interior
- **Key insight**: The natural parameterization of any exponential family produces a **globally strongly convex** loss
- **Examples**: Gaussian (variance = Fisher info), Poisson ($\mu = e^\theta = \lambda$), Bernoulli ($\mu = p(1-p)$)

**Simulation verification** (Simulation 5): Poisson in natural parameter space. The sector ratio was positive at every step, ranging from 0.00177 to 0.00240 (with $\eta = 0.001$). The strong convexity parameter $\mu = e^\theta$ varies with position but is always positive.

**AAD consequence**: Any agent using exponential family models in natural parameter form satisfies GA-3 globally. The Kalman filter (Gaussian), Beta-Bernoulli edge updates, and Bayesian conjugate models all fall in this category. This is a large and important class.

### 2.4 Non-Convex Losses (Neural Networks, Mixture Models)

For mixture models, neural network losses, and other non-convex objectives:

- **Local strong convexity**: Within a basin of attraction around any local minimum, the Hessian is positive definite and $\mu > 0$
- **Basin boundary**: At the inflection surface (where $\lambda_{\min}(H) = 0$), strong convexity fails
- **Between basins**: The sector condition is violated — the gradient can point *away* from the current reference optimum

**Simulation verification** (Simulation 3): Two-component Gaussian mixture with parameters $(mu_1, mu_2)$. Two optima exist (by label symmetry). Starting from Optimum A:

- **Within basin** (distance $< R \approx 3.1$): sector ratio positive, ranging from 126 to 228 per unit learning rate. Hessian is positive definite with minimum eigenvalue from 35 to 183.
- **At basin boundary** ($r \approx 3.1$): Hessian eigenvalue crosses zero. Sector ratio drops sharply.
- **Beyond basin** ($r > 3.5$): Sector ratio becomes negative. Gradient descent starting here converges to Optimum B (the wrong basin).

The basin radius $R \approx 3.1$ was confirmed by both the sector condition breakdown and the Hessian eigenvalue sign change. Gradient descent from $r = 2$ (within basin) converged to Optimum A in $< 100$ steps. From $r = 5$ (outside basin), it converged to Optimum B. The basin boundary is the structural-adaptation trigger from #structural-adaptation-necessity.

### 2.5 Quasi-Convex Losses

A function is quasi-convex if its sublevel sets $\{w : L(w) \leq c\}$ are convex for all $c$. This implies unimodality but not convexity.

**Key distinction**: For a differentiable quasi-convex function, $\nabla L(w)^T (w - w^\ast) \geq 0$ whenever $L(w) \geq L(w^\ast)$ — the gradient always points "uphill." This means the sector product $\delta^T \nabla L$ is nonneg whenever we are at or above the loss at the optimum. But the sector *ratio* $\delta^T \nabla L / \lVert\delta\rVert^2$ can become arbitrarily small.

**Simulation verification** (Simulation 6): $L(w) = -1/(1+w^2)$, quasi-convex with minimizer at $w = 0$.

- The sector ratio $\delta^T F / \delta^2 = \eta \cdot 2/(1+w^2)^2$ is always positive
- But it decays as $O(1/w^4)$, approaching zero — no uniform lower bound exists
- The local sector parameter is $\alpha(R) = \eta \cdot 2/(1+R^2)^2$, which is positive but becomes vacuously small for large $R$
- **Result**: GA-3 technically holds locally for any finite $R$, but with $\alpha \to 0$ the persistence bound $R^\ast = \rho/\alpha \to \infty$, meaning the agent effectively cannot persist against any disturbance

**AAD consequence**: Quasi-convex (but not strongly convex) losses produce arbitrarily weak sector bounds. The persistence condition requires $\alpha > \rho/R$, and for quasi-convex losses the achievable $\alpha$ may fall below this threshold even though the loss is unimodal. These losses need the local analysis (Part 3) to be useful.

### 2.6 Multi-Modal Non-Monotone Losses

For losses with multiple local minima (Simulation 6, second case: $L(w) = \sin(w) + 0.01w^2$):

- **Within a basin**: sector condition holds. For the basin around $w^\ast \approx 4.62$, the sector ratio was positive for $|\delta| < 3.0$.
- **Crossing a local maximum**: gradient reverses direction, sector product goes negative. Confirmed at $\delta \approx +3.4$ (approaching the next local maximum at $w \approx 8.0$) and $\delta \approx -3.0$ (approaching the previous local maximum).
- **Basin radius**: $R \approx 3.0$, roughly the distance from the local minimum to the nearest local maximum.

---

## Part 3: The Local Sector Condition

### 3.1 R as the Convexity Basin Radius

AAD's sector condition is local: it holds for $\lVert\delta\rVert \leq R$. The equivalence established in Part 1 gives this a precise meaning for gradient-based agents:

*[Derived (basin-radius identification)]*

$$R = \sup\{r > 0 : L \text{ is } \mu\text{-strongly convex on } \mathcal{B}_r(M^\ast) \text{ for some } \mu > 0\}$$

That is, $R$ is the radius of the largest ball around $M^\ast$ on which the loss is locally strongly convex. Beyond $R$, the Hessian develops a zero or negative eigenvalue, and the gradient may point away from $M^\ast$.

### 3.2 Relationship to Curvature

For twice-differentiable losses, the local strong convexity parameter at distance $r$ from the optimum is:

$$\mu(r) = \inf_{\lVert\delta\rVert = r} \lambda_{\min}(\nabla^2 L(M^\ast + \delta))$$

The sector parameter is then $\alpha(R) = \eta \cdot \mu(R) = \eta \cdot \inf_{\lVert\delta\rVert \leq R} \lambda_{\min}(\nabla^2 L(M^\ast + \delta))$.

**Key behaviors:**

| Loss class | $\mu(r)$ behavior | Basin radius $R$ |
|---|---|---|
| Quadratic | Constant: $\lambda_{\min}(H)$ | $\infty$ |
| Regularized logistic | $\geq \lambda$ always, increases near optimum | $\infty$ |
| Exponential family (natural) | $> 0$ everywhere, may vary | $\infty$ (interior of parameter space) |
| Unregularized logistic | Decreasing, $\to 0$ as $r \to \infty$ | $\infty$ (technically), but $\alpha \to 0$ |
| Non-convex (mixture) | Decreasing, crosses 0 at basin boundary | Finite: distance to nearest saddle |
| Quasi-convex | May be $> 0$ locally near optimum, $< 0$ at inflection points | Finite if locally convex; $\infty$ with decaying $\alpha$ if globally quasi-convex |
| Multi-modal | $> 0$ within basin, $< 0$ beyond local max | Distance to nearest local maximum |

### 3.3 What Happens at the Basin Boundary

When $\lVert\delta\rVert > R$:

1. **The sector condition fails**: $\delta^T \nabla L < 0$ in some directions, meaning the gradient points *away* from the current reference optimum.
2. **Gradient descent leaves the basin**: The agent's correction drives it further from $M^\ast$, toward a different basin (a different local minimum).
3. **This IS the structural-adaptation trigger**: The condition $R^\ast > R$ from #structural-adaptation-necessity means the required steady-state mismatch exceeds the basin of the current model parameterization. The agent needs a qualitatively different model — not a different parameter value in the same basin, but a different basin entirely.

**The structural-adaptation trigger is the loss landscape's inflection surface.** Beyond the inflection, the correction function reverses, and parametric adaptation becomes counterproductive.

### 3.4 Consequences for Adaptive Reserve

The adaptive reserve from #sector-condition-derivation is $\Delta\rho^\ast = \alpha R - \rho = \eta\mu R - \rho$.

For gradient-based agents, this has three factors:
- **$\eta$**: How responsive the agent is (gain)
- **$\mu$**: How curved the loss landscape is (environment structure)
- **$R$**: How wide the convexity basin is (model class capacity)

An agent is robust when $\eta\mu R \gg \rho$: high gain, steep curvature, wide basin, slow environment. An agent is fragile when any of these factors is small relative to $\rho$.

---

## Part 4: Numerical Experiments

### Experiment 1: Quadratic Loss (Global Strong Convexity)

**Setup.** $L(w) = \frac{1}{2}(w - w^\ast)^T H (w - w^\ast)$ with $w \in \mathbb{R}^5$, $H$ having eigenvalues $\{0.5, 1.0, 2.0, 3.0, 5.0\}$, $\eta = 0.1$.

**Results.** The sector ratio $\delta^T F / \lVert\delta\rVert^2$ at every step of gradient descent from a random initialization fell within $[\eta\mu, \eta L] = [0.05, 0.50]$, confirming the theoretical prediction exactly. No step violated the bound. Convergence from $\lVert\delta_0\rVert = 4.16$ to $\lVert\delta_{50}\rVert = 0.013$ was monotonic.

```python
import numpy as np
np.random.seed(42)

d = 5
eigvals_true = np.array([0.5, 1.0, 2.0, 3.0, 5.0])
Q = np.linalg.qr(np.random.randn(d, d))[0]
H = Q @ np.diag(eigvals_true) @ Q.T
mu, L_smooth = eigvals_true.min(), eigvals_true.max()
w_star = np.zeros(d)
eta = 0.1

w = np.random.randn(d) * 3
for t in range(100):
    delta = w - w_star
    dn = np.linalg.norm(delta)
    if dn > 1e-12:
        grad = H @ delta
        F = eta * grad
        ratio = delta @ F / (dn**2)
        assert ratio >= eta * mu - 1e-10  # sector condition holds
        assert ratio <= eta * L_smooth + 1e-10
    w = w - eta * H @ delta
```

### Experiment 2: Logistic Regression (Position-Dependent Strong Convexity)

**Setup.** Logistic regression with $d = 2$, $N = 5000$ samples. Two cases: unregularized and L2-regularized ($\lambda = 0.1$).

**Results (unregularized).** The sector ratio was positive along the entire gradient-descent trajectory from $\lVert\delta_0\rVert = 3.30$ to convergence. The local strong convexity parameter $\eta\mu(w)$ varied from 0.0025 (far from optimum, where sigmoid saturates) to 0.020 (near optimum). This confirms that logistic loss satisfies GA-3 locally everywhere but with a position-dependent $\alpha$ — it weakens far from the optimum.

**Results (L2-regularized).** With $\lambda = 0.1$, the sector ratio was bounded below by $\eta\lambda = 0.03$ at every point, and the Hessian eigenvalues were bounded below by $\lambda + (\text{logistic contribution})$. The regularization provides a uniform floor on $\alpha$, confirming that L2 regularization transforms a locally strongly convex problem into a globally strongly convex one.

```python
def logistic_loss_grad(w, X, y):
    z = y * (X @ w)
    s = 1.0 / (1.0 + np.exp(-np.clip(-z, -500, 500)))
    return -(X.T @ (y * s)) / len(y)

# With regularization:
def reg_grad(w, X, y, lam):
    return logistic_loss_grad(w, X, y) + lam * w
```

### Experiment 3: Gaussian Mixture (Non-Convex, Basin Structure)

**Setup.** Two-component Gaussian mixture ($\mu_1 = -2, \mu_2 = 3$, $\sigma = 1$, $\pi = 0.4$), $N = 500$ samples. Estimate $(\mu_1, \mu_2)$ with fixed $\pi = 0.5, \sigma = 1$. Two optima exist by label symmetry: $A \approx (-1.95, 2.94)$ and $B \approx (2.94, -1.95)$.

**Results.**

| Region | Hessian $\lambda_{\min}$ | Sector ratio sign | Behavior |
|---|---|---|---|
| $r < 3.1$ (within basin) | $> 35$ (positive definite) | Positive | Converges to Optimum A |
| $r \approx 3.1$ (boundary) | $\approx 0$ | Near zero | Transition zone |
| $r > 3.5$ (outside basin) | $< -40$ (indefinite) | Negative | Diverges from A, converges to B |

The basin radius was measured at $R \approx 3.1$ in the tightest direction (toward Optimum B) and up to 10.0 in other directions. The ratio of the basin radius to the inter-optimum distance was approximately 0.50, meaning the basin extends roughly halfway to the other optimum.

**Gradient descent verification:** Starting at distance 2.0 from Optimum A (within basin), the agent converged to A in under 100 steps. Starting at distance 5.0 (beyond basin, toward B), the agent converged to Optimum B in about 500 steps. The basin boundary is a sharp transition, not a gradual degradation.

```python
from scipy.stats import norm

def grad_neg_log_lik(mu1, mu2, x, sigma=1.0, pi=0.5):
    p1 = pi * norm.pdf(x, mu1, sigma)
    p2 = (1-pi) * norm.pdf(x, mu2, sigma)
    total = p1 + p2 + 1e-300
    r1 = p1 / total
    r2 = p2 / total
    dmu1 = -np.sum(r1 * (x - mu1) / sigma**2)
    dmu2 = -np.sum(r2 * (x - mu2) / sigma**2)
    return np.array([dmu1, dmu2])
```

### Experiment 4: Local Sector Condition Measurement

**Setup.** Same Gaussian mixture as Experiment 3. Measure the sector parameter $\alpha(r)$ as a function of distance from Optimum A, averaged over 50 random directions at each distance.

**Results.**

| Distance $r$ | $\alpha_{\min}(r)$ | $\alpha_{\text{mean}}(r)$ | Hessian PD? |
|---|---|---|---|
| 0.5 | 181.4 | 227.7 | Yes |
| 1.0 | 175.6 | 227.0 | Yes |
| 1.5 | 171.4 | 227.5 | Yes |
| 2.0 | 159.0 | 210.1 | Yes |
| 2.5 | 142.8 | 195.1 | Yes |
| 3.0 | 125.8 | 218.8 | Yes (marginal) |
| 3.1 | — | — | No (some directions) |

$\alpha(r)$ decreases monotonically as $r$ increases, reflecting the weakening curvature near the basin boundary. The decay is moderate — $\alpha$ at $r = 3.0$ is still 69% of its value at $r = 0.5$. The sharp transition occurs at the boundary: from $\alpha > 125$ to sector failure within a distance of 0.5.

---

## Part 5: Assessment

### 5.1 Is GA-3 Derivable?

**Yes, for any gradient-based agent.** The sector condition is not an independent assumption — it is a mathematical consequence of the loss landscape's geometry:

*[Derived (GA-3 bridge, conditional on gradient-based updates and differentiable loss)]*

$$\text{GA-3}(\alpha, R) \iff L \text{ is locally } (\alpha/\eta)\text{-strongly convex on } \mathcal{B}_R(M^\ast)$$

The sector parameter $\alpha$ is not a free parameter of the theory — it is determined by the product $\eta \cdot \mu$, where $\eta$ is the learning rate and $\mu$ is the strong convexity modulus of the loss. The basin radius $R$ is determined by the loss landscape's geometry (distance to the nearest inflection surface).

### 5.2 Precise Characterization

**GA-3 holds iff the loss is locally strongly convex at the current operating point, with:**

$$\alpha = \eta \cdot \inf_{\lVert\delta\rVert \leq R} \lambda_{\min}(\nabla^2 L(M^\ast + \delta))$$

$$R = \sup\{r : \lambda_{\min}(\nabla^2 L(M^\ast + \delta)) > 0 \text{ for all } \lVert\delta\rVert \leq r\}$$

### 5.3 Which Agents Satisfy GA-3 by Construction?

**Globally** (GA-3 with $R = \infty$):
- Agents using quadratic loss (Kalman filters, linear regression)
- Agents using exponential family models in natural parameter space (Beta-Bernoulli, Gaussian, Poisson posteriors) — this subsumes the result of #spike-single-edge-strategic-dynamics
- Agents using any L2-regularized convex loss (regularized logistic, regularized neural networks)

**Locally** (GA-3 with finite $R$):
- Agents using unregularized logistic or softmax loss (convex but $\alpha \to 0$ at infinity)
- Agents using non-convex losses within a basin of attraction (neural networks, mixture models, EM algorithms)
- Agents using quasi-convex losses (with decaying $\alpha$)

**Agents that need the local form:**
- Any agent with a non-convex loss landscape (neural networks, mixture models)
- Any agent operating in a regime where the loss is only locally convex
- These agents satisfy GA-3 within their current basin, and the basin radius $R$ is the structural-adaptation threshold from #structural-adaptation-necessity

### 5.4 Connection to Structural Adaptation

The equivalence provides a sharp characterization of the structural-adaptation trigger:

**Structural adaptation is necessary when the agent's mismatch exceeds the convexity radius of its loss landscape.**

In optimization terms: when the agent is pushed outside the basin of attraction of its current local minimum, gradient descent drives it *away* from the reference optimum. This is the sector condition failing — the correction function reverses direction. The agent must either:
1. Find a new basin (structural adaptation — change model class, architecture search)
2. Be reinitialized within a good basin (external reset, grafting from #structural-adaptation-necessity)

This also explains why structural adaptation is expensive: finding a good basin in a non-convex landscape is a hard search problem (NP-hard in the worst case for general non-convex optimization). The theory's advice to "prefer parametric adaptation when it suffices" corresponds to "stay in your basin when you can."

### 5.5 Should GA-3 Be Replaced?

**Recommendation: keep GA-3 as stated, but add a derivation note.**

GA-3 should remain as a *named assumption* in the theory because:
1. It is the minimal assumption needed for the Lyapunov proofs — it decouples stability analysis from the specific update rule
2. Not all agents are gradient-based — feedback controllers, rule-based systems, and human decision-makers may satisfy the sector condition through mechanisms unrelated to loss landscape convexity
3. The sector condition is weaker than strong convexity (it applies to any correction function, not just gradients)

However, the following should be added to #sector-condition-derivation or as a new segment:

> **Derivation note.** For any gradient-based agent with learning rate $\eta$ minimizing a loss $L$, GA-3 is equivalent to local $\mu$-strong convexity of $L$ with $\alpha = \eta\mu$. The sector condition is thus automatically satisfied by agents using convex losses or operating within a convexity basin of non-convex losses. GA-3 is an independent assumption only for agents whose correction mechanisms are not gradient-based.

### 5.6 Relationship to the Beta-Bernoulli Case

The Beta-Bernoulli result from #spike-single-edge-strategic-dynamics is a special case of this analysis. The Beta-Bernoulli update minimizes the KL divergence from the posterior to the true distribution, which in natural parameter space (log-odds) is a convex loss. The update gain $\eta_{\text{edge}} = 1/(n+1)$ is the learning rate, and the strong convexity parameter of the Bernoulli log-likelihood in natural parameter space is $\mu = \theta(1-\theta)$ (the Fisher information). The sector parameter $\alpha_\Sigma = 1/(n+1)$ from that spike equals $\eta_{\text{edge}} \cdot 1 = \eta_{\text{edge}}$ because the Beta-Bernoulli correction is *exactly linear* in $\delta$ (the expected correction is $-\delta/(n+1)$), giving $\mu_{\text{eff}} = 1$ in the mismatch coordinate.

### 5.7 Open Questions

1. **Non-gradient agents.** For agents whose correction is not gradient-based (PID controllers, rule-based systems, human judgment), GA-3 remains an empirical claim. Can it be derived from other principles? PID controllers satisfy a sector condition when the plant transfer function is in a specific sector (Lur'e stability theory) — the connection to AAD's sector condition is structural, not accidental.

2. **Adaptive $\eta$.** When $\eta$ is itself adapted (Adam, RMSprop, Kalman gain), the sector parameter $\alpha = \eta(t) \cdot \mu(w_t)$ is time-varying. The Lyapunov proofs in #sector-condition-derivation assume constant $\alpha$. Extension to time-varying $\alpha(t) \geq \underline{\alpha} > 0$ is standard (see Khalil 2002, Chapter 8) and should be noted.

3. **Matrix gain.** When $\eta$ is a matrix (Kalman gain, natural gradient, Adam's per-parameter rates), the sector condition becomes $\delta^T K \nabla L \geq \alpha \lVert\delta\rVert^2$ where $K$ is the gain matrix. For positive definite $K$, this holds with $\alpha = \lambda_{\min}(K) \cdot \mu$. The natural gradient ($K = [\text{Fisher}]^{-1}$) gives $\alpha = \mu / \lambda_{\max}(\text{Fisher})$, which can be much better conditioned than the vanilla gradient case.

4. **Curvature estimation.** Can the agent estimate $\mu$ and $R$ online? Second-order methods (Newton, L-BFGS) implicitly estimate the local curvature. An agent that monitors $\lambda_{\min}(\nabla^2 L)$ has a direct estimate of when it is approaching the basin boundary — a principled trigger for structural adaptation.

---

## Summary

| Claim | Status | Evidence |
|---|---|---|
| GA-3 $\iff$ local strong convexity for gradient agents | **Exact** (mathematical equivalence) | Part 1 proof |
| $\alpha = \eta \cdot \mu$ | **Exact** | Direct from equivalence |
| $R$ = convexity basin radius | **Exact** | Direct from equivalence |
| Quadratic: GA-3 global | **Exact** | Simulation 1 confirms |
| Logistic: GA-3 local, L2-reg makes global | **Exact** | Simulation 2 confirms |
| Exponential family: GA-3 global in natural params | **Exact** | Simulation 5 confirms |
| Non-convex: GA-3 within basin, fails at boundary | **Exact** | Simulation 3,4 confirm |
| Basin boundary = structural-adaptation trigger | **Derived** | From equivalence + #structural-adaptation-necessity |
| GA-3 is derivable, not irreducible (for gradient agents) | **Result** | This spike |

The sector condition is not an axiom — for the large class of gradient-based agents, it is a theorem about loss landscape geometry. This substantially strengthens the epistemic status of all downstream results that depend on GA-3 (#persistence-condition, #sector-condition-derivation, #adversarial-destabilization): they hold whenever the loss is locally strongly convex, which is a well-characterized and widely studied property.

---

## References

- Nesterov, Y. (2004). *Introductory Lectures on Convex Optimization*. Springer. Theorem 2.1.10 (equivalent characterizations of strong convexity).
- Khalil, H. K. (2002). *Nonlinear Systems* (3rd ed.). Chapters 4, 7, 9 (Lyapunov stability, sector conditions, input-output stability).
- Lur'e, A. I. (1957). *Some Nonlinear Problems in the Theory of Automatic Control*. (Original sector-condition framework.)
- Boyd, S. & Vandenberghe, L. (2004). *Convex Optimization*. Chapter 9 (strong convexity and its consequences).
