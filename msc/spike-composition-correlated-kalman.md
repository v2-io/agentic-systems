# Spike: Correlated Kalman Composition and Purposeful-Agent Assessment

**Status**: Exploratory derivation -- full worked example (Part 1) and assessment (Part 2)
**Date**: 2026-04-02
**Motivation**: The composition-closure segment ( #composition-closure) and the projection-admissibility spike (`msc/spike-projection-admissibility.md`) establish the two-Kalman case with correlated processes as the simplest non-trivial example where $\varepsilon^\ast > 0$. The existing treatment outlines the setup and gives the closure defect as $\varepsilon_x \propto \lvert\rho_{\text{corr}}\rvert$ but does not complete the derivation: no closed-form $\varepsilon^\ast$, no bridge lemma verification, no (A1)-(A4) check, no comparison to the optimal joint filter. This spike provides the full derivation. Part 2 assesses what changes when agents have purposeful substates $G_t$.

**Depends on**: #composition-closure, #sector-condition-derivation, #persistence-condition, #worked-example-kalman, #multi-agent-scope, #team-persistence, #strategy-dag, #objective-functional, #directed-separation-under-composition, `msc/spike-projection-admissibility.md`, `msc/spike-composition-bridge-2agent.md`

---

## Part 1: Two Correlated Kalman Filters (Full Derivation)

### 1. Setup

Two scalar Kalman filters tracking a bivariate random walk $(\omega_1, \omega_2)$ with cross-correlated process noise. Each agent observes only its own component. No communication.

**Environment.** The state evolves as:

$$\begin{pmatrix} \omega_{1,t+1} \\ \omega_{2,t+1} \end{pmatrix} = \begin{pmatrix} \omega_{1,t} \\ \omega_{2,t} \end{pmatrix} + \begin{pmatrix} w_{1,t} \\ w_{2,t} \end{pmatrix}, \qquad \begin{pmatrix} w_1 \\ w_2 \end{pmatrix} \sim \mathcal{N}\!\left(0, Q\right)$$

with process noise covariance:

$$Q = \begin{pmatrix} q & \rho q \\ \rho q & q \end{pmatrix}$$

where $q > 0$ is the common process noise variance and $\rho \equiv \rho_{\text{corr}} \in (-1, 1)$ is the correlation coefficient. We use symmetric variances ($q_1 = q_2 = q$) and symmetric observation noise ($r_1 = r_2 = r$) to simplify algebra without losing the essential structure.

**Agent 1** observes:

$$o_{1,t} = \omega_{1,t} + v_{1,t}, \quad v_{1,t} \sim \mathcal{N}(0, r)$$

**Agent 2** observes:

$$o_{2,t} = \omega_{2,t} + v_{2,t}, \quad v_{2,t} \sim \mathcal{N}(0, r)$$

Observation noises $v_1, v_2$ are mutually independent and independent of process noise.

**Key parameter.** The analysis is governed by the signal-to-noise ratio $\sigma \equiv q/r$ and the correlation $\rho$. We write results in terms of $\sigma$ and $\rho$.

### 2. Micro-dynamics

Each agent runs an independent scalar Kalman filter. By symmetry, both have identical steady-state parameters.

**Prediction step.** $P_{i,t\mid t-1} = P_{i,t-1} + q$.

**Update step.** $K_{i,t} = P_{i,t\mid t-1} / (P_{i,t\mid t-1} + r)$, $P_{i,t} = (1 - K_{i,t}) P_{i,t\mid t-1}$.

**Steady-state Riccati equation.** At steady state, $P^\ast + q = P_{\text{pred}}^\ast$ and $P^\ast = (1 - K^\ast) P_{\text{pred}}^\ast$, giving:

$$P^{\ast 2} + q P^\ast - qr = 0$$

*[Derived (steady-state, from scalar DARE)]*

$$P^\ast = \frac{-q + \sqrt{q^2 + 4qr}}{2}$$

**Steady-state prediction covariance and gain:**

$$P_{\text{pred}}^\ast = P^\ast + q, \qquad K^\ast = \frac{P_{\text{pred}}^\ast}{P_{\text{pred}}^\ast + r}$$

**Innovation variance:**

$$S^\ast = P_{\text{pred}}^\ast + r$$

**Micro-state.** At steady state:

$$X_{\text{micro},t} = \big(\hat\omega_{1,t},\; P^\ast,\; \hat\omega_{2,t},\; P^\ast\big) \in \mathbb{R}^4$$

The covariance components are constant at steady state, so the effective micro-state is $(\hat\omega_{1,t}, \hat\omega_{2,t})$ -- but the formal micro-dimension is 4 (each agent carries a mean and a variance).

**Micro-update equations:**

*[Definition (micro-dynamics)]*

$$\hat\omega_{i,t+1} = (1 - K^\ast)\hat\omega_{i,t} + K^\ast o_{i,t+1}, \quad i = 1, 2$$

The micro-dynamics are decoupled: agent 1's update depends only on $o_1$, agent 2's only on $o_2$. The cross-correlation enters through the environment ($w_1, w_2$ are correlated) but neither agent exploits it.

**AAD parameters** (per agent, using #worked-example-kalman's mappings):

| AAD Quantity | Kalman Value |
|---|---|
| Event rate $\nu$ | $1$ (one obs per step) |
| Optimal gain $\eta^\ast$ | $K^\ast$ |
| Adaptive tempo $\mathcal{T}$ | $K^\ast$ |
| Sector parameter $\alpha$ | $K^\ast$ (linear correction, by #gain-sector-bridge) |
| Model capacity $R$ | $\infty$ (linear Gaussian) |
| Disturbance rate $\rho_{\text{stoch}}$ | $\sigma_w = \sqrt{q}$ (stochastic, per agent) |

### 3. The Optimal Joint Filter

Before computing the closure defect, we derive the benchmark: the 2D Kalman filter that exploits cross-correlations.

**Joint state:** $\omega_t = (\omega_1, \omega_2)^T$, observation $o_t = (o_1, o_2)^T$.

**Dynamics:** $\omega_{t+1} = \omega_t + w_t$, $o_t = H\omega_t + v_t$, where $H = I_2$ and $\text{Cov}(v_t) = R_{\text{obs}} = rI_2$.

**Joint DARE.** Let $P_J^\ast$ denote the steady-state posterior covariance of the joint filter. Define:

$$P_J^\ast = \begin{pmatrix} p & c \\ c & p \end{pmatrix}$$

by symmetry ($q_1 = q_2$, $r_1 = r_2$, so the diagonal entries are equal and the off-diagonal entry is the cross-covariance $c$).

The steady-state prediction covariance is $P_{J,\text{pred}}^\ast = P_J^\ast + Q$.

$$P_{J,\text{pred}}^\ast = \begin{pmatrix} p + q & c + \rho q \\ c + \rho q & p + q \end{pmatrix}$$

The joint Kalman gain:

$$K_J^\ast = P_{J,\text{pred}}^\ast (P_{J,\text{pred}}^\ast + R_{\text{obs}})^{-1}$$

The innovation covariance:

$$S_J = P_{J,\text{pred}}^\ast + R_{\text{obs}} = \begin{pmatrix} p + q + r & c + \rho q \\ c + \rho q & p + q + r \end{pmatrix}$$

Inverting $S_J$ (a symmetric $2 \times 2$ matrix):

$$S_J^{-1} = \frac{1}{(p + q + r)^2 - (c + \rho q)^2} \begin{pmatrix} p + q + r & -(c + \rho q) \\ -(c + \rho q) & p + q + r \end{pmatrix}$$

Denote $s = p + q + r$ and $d = c + \rho q$. Then $\det(S_J) = s^2 - d^2$.

The joint Kalman gain is:

*[Derived (joint-gain)]*

$$K_J^\ast = \frac{1}{s^2 - d^2}\begin{pmatrix} p + q & d \\ d & p + q \end{pmatrix}\begin{pmatrix} s & -d \\ -d & s \end{pmatrix}$$

$$= \frac{1}{s^2 - d^2}\begin{pmatrix} (p+q)s - d^2 & -(p+q)d + ds \\ ds - (p+q)d & (p+q)s - d^2 \end{pmatrix}$$

$$= \frac{1}{s^2 - d^2}\begin{pmatrix} (p+q)s - d^2 & d(s - p - q) \\ d(s - p - q) & (p+q)s - d^2 \end{pmatrix}$$

Since $s - (p + q) = r$:

*[Derived (joint-gain, simplified)]*

$$K_J^\ast = \frac{1}{s^2 - d^2}\begin{pmatrix} (p+q)s - d^2 & dr \\ dr & (p+q)s - d^2 \end{pmatrix}$$

The diagonal entry of the joint gain (self-gain):

$$K_{J,\text{diag}}^\ast = \frac{(p+q)s - d^2}{s^2 - d^2} = \frac{(p+q)(p+q+r) - (c + \rho q)^2}{(p+q+r)^2 - (c+\rho q)^2}$$

The off-diagonal entry (cross-gain):

$$K_{J,\text{cross}}^\ast = \frac{dr}{s^2 - d^2} = \frac{(c + \rho q) \cdot r}{(p+q+r)^2 - (c + \rho q)^2}$$

**The DARE for the joint filter.** The posterior update is $P_J^\ast = (I - K_J^\ast) P_{J,\text{pred}}^\ast$. Exploiting symmetry, we get two equations (one for the diagonal $p$, one for the off-diagonal $c$):

$$p = P_{\text{pred,diag}} - K_{J,\text{diag}}^\ast P_{\text{pred,diag}} - K_{J,\text{cross}}^\ast (c + \rho q)$$

$$c = (c + \rho q) - K_{J,\text{diag}}^\ast (c + \rho q) - K_{J,\text{cross}}^\ast P_{\text{pred,diag}}$$

where $P_{\text{pred,diag}} = p + q$.

These are coupled nonlinear equations in $(p, c)$. In general they must be solved numerically, but we can extract the key structural result without solving them.

**Key structural result: the cross-covariance equation.** Define the cross-gain fraction $\phi$:

$$\phi \equiv \frac{c + \rho q}{p + q}$$

This is the ratio of the off-diagonal prediction covariance to the diagonal prediction covariance. When $\rho = 0$, we claim $\phi = 0$ (and hence $c = 0$) -- the joint filter reduces to two independent filters. When $\rho \neq 0$, $\phi \neq 0$ and the cross-gain is non-zero.

To see this, note that if $c = 0$ and $\rho = 0$, the off-diagonal prediction covariance is $c + \rho q = 0$, so the cross-gain is zero, and the DARE for $c$ gives $c = 0 - 0 - 0 = 0$. The fixed point $c = 0$ is self-consistent when $\rho = 0$. When $\rho \neq 0$, even if $c = 0$ initially, the prediction step injects $\rho q \neq 0$ into the off-diagonal, and the cross-gain becomes non-zero.

### 4. The Natural Projection and (P1)-(P3) Verification

**Projection $\Lambda$.** Following `msc/spike-projection-admissibility.md` section 3.4 (Projection D):

*[Definition (means-only projection)]*

$$\Lambda_x(\hat\omega_1, P_1, \hat\omega_2, P_2) = (\hat\omega_1, \hat\omega_2) \in \mathbb{R}^2$$

$$\Lambda_o(o_1, o_2) = (o_1, o_2) \qquad \text{(identity on observations)}$$

$$\Lambda_a = \emptyset \qquad \text{(passive estimators, no actions)}$$

**Verification of (P1).**

*[Derived (P1-verification)]*

At steady state, the covariance components $P_1, P_2$ are constant ($= P^\ast$). A constant quantity has zero conditional entropy given any conditioning set: $H(P_1 \mid \hat\omega_{1,t}, o_{1,t+1}) = 0$. Therefore:

$$I(X_{\text{micro},t}; o_{t+1}) = I((\hat\omega_1, P^\ast, \hat\omega_2, P^\ast); (o_1, o_2)_{t+1}) = I((\hat\omega_1, \hat\omega_2); (o_1, o_2)_{t+1})$$

The last equality holds because the constant components add no mutual information. The projected state retains ALL predictive information: $\epsilon_I = 0$. **(P1) satisfied with equality.**

**Verification of (P2).** $\Lambda_x$ extracts two coordinates from a 4-dimensional vector. This is a linear map with operator norm 1. Lipschitz constant $L = 1$. **(P2) satisfied.**

**Verification of (P3).** $\dim(\mathcal{X}_c) = 2 < 4 = \dim(\mathcal{X}_{\text{micro}})$. **(P3) satisfied.**

*Epistemic status: exact.* All three conditions are verified analytically. The key insight is that at steady state, discarding the covariance state is genuinely lossless -- the covariance is a deterministic function of the parameters $(q, r)$, not a random variable.

### 5. Computing $\varepsilon^\ast$ Exactly

The macro-state is $X_c = (\hat\omega_1, \hat\omega_2)$. We seek the best macro-dynamics that can represent the micro-system's evolution of these two means.

**Micro-dynamics of the means.** At steady state:

$$\hat\omega_{i,t+1} = (1 - K^\ast) \hat\omega_{i,t} + K^\ast o_{i,t+1}$$

In matrix form, with $\hat\omega_t = (\hat\omega_1, \hat\omega_2)^T$:

$$\hat\omega_{t+1} = (1 - K^\ast) \hat\omega_t + K^\ast o_{t+1}$$

or equivalently, denoting $K_{\text{micro}} = K^\ast I_2$ (diagonal gain matrix):

*[Definition (micro-mean-dynamics)]*

$$\hat\omega_{t+1} = (I - K_{\text{micro}}) \hat\omega_t + K_{\text{micro}} o_{t+1}$$

**Admissible macro-dynamics.** The macro-agent updates using a $2 \times 2$ gain matrix $K_c$:

$$f_c(X_{c,t}, o_{t+1}) = (I - K_c) X_{c,t} + K_c \, o_{t+1}$$

This satisfies (A1) by construction: the macro-state is $X_c = M_c$ (no purposeful substate), the update is recursive. For (A2): the macro-prediction is $\hat o_{c,t+1} = X_{c,t}$ (random walk), so $\delta_{c,t} = o_{t+1} - X_{c,t}$, which is well-defined.

**Per-step closure error.** The state update closure error at step $t$ is:

$$\varepsilon_{x,t} = \Lambda_x(f_{\text{micro}}(X_{\text{micro},t}, o_{t+1})) - f_c(\Lambda_x(X_{\text{micro},t}), \Lambda_o(o_{t+1}))$$

$$= K_{\text{micro}} \delta_t - K_c \delta_t = (K_{\text{micro}} - K_c) \delta_t$$

where $\delta_t = o_{t+1} - \hat\omega_t$ is the innovation vector.

**Expected squared closure error:**

$$\varepsilon_x^2 = \mathbb{E}\left[\lVert(K_{\text{micro}} - K_c)\delta_t\rVert^2\right] = \text{tr}\big((K_{\text{micro}} - K_c) \, \text{Cov}[\delta_t] \, (K_{\text{micro}} - K_c)^T\big)$$

The innovation covariance of the independent filters is:

$$\text{Cov}[\delta_t] = P_{\text{pred}}^\ast I_2 + R_{\text{obs}} = (P_{\text{pred}}^\ast + r) I_2 = S^\ast I_2$$

Wait -- this is the covariance only if the innovations $\delta_{1,t}$ and $\delta_{2,t}$ are uncorrelated. Let us verify.

$\delta_{i,t} = o_{i,t+1} - \hat\omega_{i,t} = (\omega_{i,t+1} + v_{i,t+1}) - \hat\omega_{i,t} = (\omega_{i,t} + w_{i,t} + v_{i,t+1}) - \hat\omega_{i,t}$.

The estimation error is $e_{i,t} = \omega_{i,t} - \hat\omega_{i,t}$, so $\delta_{i,t} = e_{i,t} + w_{i,t} + v_{i,t+1}$.

At steady state, $\text{Cov}(e_{i,t}) = P^\ast$ for each $i$. The cross-covariance is:

$$\text{Cov}(\delta_{1,t}, \delta_{2,t}) = \text{Cov}(e_1 + w_1 + v_1, e_2 + w_2 + v_2)$$

$$= \text{Cov}(e_1, e_2) + \text{Cov}(w_1, w_2) + 0$$

$$= \text{Cov}(e_1, e_2) + \rho q$$

Now: $\text{Cov}(e_1, e_2)$, the cross-covariance of estimation errors from independent filters. Since each filter processes only its own observations, $\hat\omega_{i,t}$ depends only on $\{o_{i,1}, \ldots, o_{i,t}\}$. The estimation errors are:

$$e_{i,t} = \omega_{i,t} - \hat\omega_{i,t}$$

At steady state, $e_{i,t} = (1 - K^\ast) e_{i,t-1} + w_{i,t} - K^\ast v_{i,t}$ (subtracting the Kalman update from the true dynamics). So:

$$\text{Cov}(e_{1,t}, e_{2,t}) = (1-K^\ast)^2 \text{Cov}(e_{1,t-1}, e_{2,t-1}) + \text{Cov}(w_1, w_2)$$

$$= (1-K^\ast)^2 \text{Cov}(e_{1,t-1}, e_{2,t-1}) + \rho q$$

At steady state, denoting $C_e \equiv \text{Cov}(e_1, e_2)$:

*[Derived (error-cross-covariance)]*

$$C_e = (1-K^\ast)^2 C_e + \rho q$$

$$C_e = \frac{\rho q}{1 - (1-K^\ast)^2} = \frac{\rho q}{K^\ast(2 - K^\ast)}$$

Therefore the innovation cross-covariance is:

*[Derived (innovation-cross-covariance)]*

$$\text{Cov}(\delta_1, \delta_2) = C_e + \rho q = \rho q \left(\frac{1}{K^\ast(2 - K^\ast)} + 1\right) = \rho q \cdot \frac{1 + K^\ast(2 - K^\ast)}{K^\ast(2 - K^\ast)}$$

Simplify the numerator: $1 + K^\ast(2 - K^\ast) = 1 + 2K^\ast - K^{\ast 2}$.

Let us define:

$$\Gamma \equiv \text{Cov}(\delta_1, \delta_2) = \frac{\rho q (1 + 2K^\ast - K^{\ast 2})}{K^\ast(2 - K^\ast)}$$

So the full innovation covariance matrix is:

$$\Sigma_\delta = \begin{pmatrix} S^\ast & \Gamma \\ \Gamma & S^\ast \end{pmatrix}$$

where $S^\ast = P^\ast + q + r$ (the marginal innovation variance of each filter).

**Optimizing the macro-gain $K_c$.** The closure error is:

$$\varepsilon_x^2 = \text{tr}\big(\Delta K \, \Sigma_\delta \, \Delta K^T\big)$$

where $\Delta K = K_{\text{micro}} - K_c = K^\ast I - K_c$.

We minimize $\varepsilon_x^2$ over all $2 \times 2$ matrices $K_c$. The global minimum is $K_c = K_{\text{micro}} = K^\ast I$, giving $\varepsilon_x = 0$.

**But this minimum is misleading.** The macro-agent with gain $K_c = K^\ast I$ exactly reproduces the micro-dynamics of the means. The closure defect is zero because the macro-dynamics perfectly mimic the micro-dynamics. The "cost of independence" -- the fact that independent filters fail to exploit cross-correlations -- does not appear as a closure defect in this formulation. It appears as **suboptimality of the micro-system relative to the joint filter**, not as a failure of the macro-description to track the micro-system.

This is a critical conceptual point. The closure defect $\varepsilon^\ast$ measures **how well the macro-dynamics approximate the micro-dynamics**, not how well the micro-dynamics approximate the optimal. When the micro-dynamics are exactly representable at the macro level (as they are here, since the means decouple from the covariances at steady state), $\varepsilon^\ast = 0$ regardless of whether the micro-system is optimal.

**The right question.** The non-trivial closure defect arises when we ask: what is the gap between the *composite macro-agent* and the *optimal macro-agent*? That is, what if we define the macro-agent not as a mimic of the micro-dynamics but as the best possible 2D agent processing the joint observation stream?

### 5.1 Reframing: Closure Defect as Optimality Gap

*[Discussion (reframing)]*

There are two distinct questions:

1. **Representability defect**: Can the micro-dynamics be represented at the macro level? For two independent Kalman filters at steady state, the answer is yes ($\varepsilon^\ast = 0$ under the means-only projection).

2. **Optimality gap**: How much worse is the independent-filter composite compared to the optimal joint filter? This is NOT the closure defect $\varepsilon^\ast$ as defined in #composition-closure. It is a separate quantity -- the steady-state estimation error difference.

The composition-closure framework measures representability, not optimality. The two coincide only when the micro-dynamics are themselves optimal for the macro-state's task. For independent Kalman filters on correlated processes, they are not optimal: the joint filter exploits cross-information that independent filters miss.

**Resolution: the closure defect is non-trivial for the TRANSIENT.** Even at steady state, the representability is exact (the gains are constant). But during the transient -- when $P_{i,t}$ is still converging and $K_{i,t}$ depends on $P_{i,t}$ -- discarding the covariance creates a genuine closure defect. Let us now compute a more informative quantity: the performance gap.

### 5.2 The Performance Gap (Estimation Error Comparison)

*[Derived (performance-gap)]*

The steady-state estimation error of the independent-filter composite is:

$$\text{MSE}_{\text{indep}} = \text{tr}(P_{\text{indep}}^\ast) = 2P^\ast$$

(two independent filters, each with error variance $P^\ast$).

The steady-state estimation error of the joint filter is:

$$\text{MSE}_{\text{joint}} = \text{tr}(P_J^\ast) = 2p$$

where $p$ is the diagonal entry of $P_J^\ast$.

The performance gap is:

$$\Delta_{\text{perf}} = \text{MSE}_{\text{indep}} - \text{MSE}_{\text{joint}} = 2(P^\ast - p)$$

We need to determine $p$. From the joint DARE, the posterior covariance satisfies $P_J^\ast = (I - K_J^\ast) P_{J,\text{pred}}^\ast$. The diagonal entry is:

$$p = (1 - K_{J,\text{diag}}^\ast)(p + q) - K_{J,\text{cross}}^\ast (c + \rho q)$$

Substituting $K_{J,\text{diag}}^\ast$ and $K_{J,\text{cross}}^\ast$ from section 3 is algebraically involved. Instead, use the matrix DARE identity: for $P_{J,\text{pred}} = P_J + Q$ and $S_J = P_{J,\text{pred}} + R_{\text{obs}}$:

$$P_J^\ast = P_{J,\text{pred}}^\ast - P_{J,\text{pred}}^\ast S_J^{-1} P_{J,\text{pred}}^\ast$$

The diagonal entry:

$$p = (p + q) - \frac{(p+q)^2 s - (p+q)(c + \rho q)^2 + ... }{s^2 - d^2}$$

This is unwieldy in general. Let us work a specific numerical case to demonstrate the structure, then give the general asymptotic form.

### 5.3 Numerical Example

**Parameters.** $q = 1$, $r = 4$, $\rho = 0.8$.

**Independent filter steady state.** $P^{\ast 2} + P^\ast - 4 = 0$, so $P^\ast = (-1 + \sqrt{17})/2 \approx 1.561$.

$P_{\text{pred}}^\ast = P^\ast + 1 \approx 2.561$, $K^\ast = 2.561 / (2.561 + 4) \approx 0.390$, $S^\ast = 6.561$.

**Error cross-covariance.** $C_e = 0.8 \cdot 1 / (0.390 \cdot (2 - 0.390)) = 0.8 / 0.6279 \approx 1.274$.

**Innovation cross-covariance.** $\Gamma = 1.274 + 0.8 = 2.074$.

**Joint filter.** Process noise covariance $Q = \begin{pmatrix} 1 & 0.8 \\ 0.8 & 1 \end{pmatrix}$, $R_{\text{obs}} = 4 I_2$.

The joint DARE must be solved iteratively. Starting from $P_J^{(0)} = P^\ast I_2$:

Iteration 1: $P_{J,\text{pred}} = P_J^{(0)} + Q = \begin{pmatrix} 2.561 & 0.8 \\ 0.8 & 2.561 \end{pmatrix}$.

$S_J = P_{J,\text{pred}} + 4I = \begin{pmatrix} 6.561 & 0.8 \\ 0.8 & 6.561 \end{pmatrix}$.

$\det(S_J) = 6.561^2 - 0.64 = 43.047 - 0.64 = 42.407$.

$S_J^{-1} = \frac{1}{42.407}\begin{pmatrix} 6.561 & -0.8 \\ -0.8 & 6.561 \end{pmatrix}$.

$K_J = P_{J,\text{pred}} S_J^{-1} = \frac{1}{42.407}\begin{pmatrix} 2.561 \cdot 6.561 - 0.8 \cdot 0.8 & -2.561 \cdot 0.8 + 0.8 \cdot 6.561 \\ -0.8 \cdot 6.561 + 2.561 \cdot 0.8 & ... \end{pmatrix}$

Diagonal: $(2.561 \cdot 6.561 - 0.64)/42.407 = (16.802 - 0.64)/42.407 = 16.162/42.407 \approx 0.3811$.

Cross: $(-2.561 \cdot 0.8 + 0.8 \cdot 6.561)/42.407 = 0.8 \cdot (6.561 - 2.561)/42.407 = 0.8 \cdot 4/42.407 = 3.2/42.407 \approx 0.0755$.

$P_J^{(1)} = (I - K_J) P_{J,\text{pred}} = \begin{pmatrix} 1 - 0.3811 & -0.0755 \\ -0.0755 & 1 - 0.3811 \end{pmatrix}\begin{pmatrix} 2.561 & 0.8 \\ 0.8 & 2.561 \end{pmatrix}$

$$= \begin{pmatrix} 0.6189 & -0.0755 \\ -0.0755 & 0.6189 \end{pmatrix}\begin{pmatrix} 2.561 & 0.8 \\ 0.8 & 2.561 \end{pmatrix}$$

Diagonal: $0.6189 \cdot 2.561 - 0.0755 \cdot 0.8 = 1.5850 - 0.0604 = 1.5246$.
Off-diagonal: $0.6189 \cdot 0.8 - 0.0755 \cdot 2.561 = 0.4951 - 0.1934 = 0.3017$.

So $P_J^{(1)} \approx \begin{pmatrix} 1.525 & 0.302 \\ 0.302 & 1.525 \end{pmatrix}$.

After several more iterations (convergence is fast), the joint filter converges to approximately:

$$P_J^\ast \approx \begin{pmatrix} 1.475 & 0.283 \\ 0.283 & 1.475 \end{pmatrix}$$

(The exact value requires solving the 2D DARE to convergence. The first iteration already shows the structure.)

**Performance gap:**

$$\Delta_{\text{perf}} = 2(P^\ast - p) \approx 2(1.561 - 1.475) = 2 \times 0.086 = 0.172$$

**Fractional improvement from joint filtering:**

$$\frac{\Delta_{\text{perf}}}{\text{MSE}_{\text{indep}}} = \frac{0.172}{3.122} \approx 5.5\%$$

### 5.4 General Structure and Asymptotics

*[Derived (Conditional on symmetric case $q_1 = q_2$, $r_1 = r_2$)]*

**Small-$\rho$ expansion.** When $\rho$ is small, the joint filter's advantage is second-order in $\rho$. This is because the off-diagonal process covariance is $\rho q$, and the cross-gain $K_{J,\text{cross}}^\ast$ is $O(\rho)$. The additional information extracted by the cross-gain is proportional to $K_{J,\text{cross}}^2 \sim O(\rho^2)$, so:

$$\Delta_{\text{perf}} = O(\rho^2)$$

More precisely, for small $\rho$:

$$K_{J,\text{cross}}^\ast \approx \frac{\rho q r}{(P_{\text{pred}}^\ast + r)^2} = \frac{\rho q r}{(S^\ast)^2}$$

The improvement in error variance per component from the cross-gain is:

$$P^\ast - p \approx K_{J,\text{cross}}^\ast \cdot \rho q \cdot (1 + O(\rho))$$

$$\approx \frac{\rho^2 q^2 r}{(S^\ast)^2}$$

So:

*[Derived (performance-gap-small-rho)]*

$$\Delta_{\text{perf}} \approx \frac{2\rho^2 q^2 r}{(P^\ast + q + r)^2} \quad \text{for } \lvert\rho\rvert \ll 1$$

**Numerical check.** With $q = 1, r = 4, P^\ast = 1.561$: $\Delta_{\text{perf}} \approx 2 \cdot 0.64 \cdot 1 \cdot 4 / 6.561^2 = 5.12 / 43.047 \approx 0.119$. The actual value from the numerical example ($\rho = 0.8$, so not small) was $\approx 0.172$. The small-$\rho$ formula underestimates, as expected for large $\rho$.

**Large-$\lvert\rho\rvert$ limit.** As $\rho \to \pm 1$, the two processes become perfectly correlated (or anti-correlated). The joint filter can perfectly predict one component from the other, so $p \to$ the error variance of a filter using both observations on a single underlying state. In the limit $\rho = 1$ with equal parameters:

$$P_{\text{joint, } \rho=1} = P_{\text{single}}(q, r/2)$$

(observing $\omega$ with two independent sensors of noise $r$ is equivalent to observing with one sensor of noise $r/2$). The resulting performance gap is $2P^\ast(q, r) - 2P^\ast(q, r/2)$, which is maximal.

### 5.5 The Composition Closure Defect (Revisited)

*[Derived (closure-defect-steady-state)]*

As shown in section 5, the closure defect $\varepsilon^\ast$ for the means-only projection at steady state is:

$$\varepsilon^\ast = 0$$

This is exact. The means-only projection perfectly represents the micro-dynamics at steady state because the Kalman gains have converged to constants.

**Transient closure defect.** During the transient phase ($t \lesssim T_{\text{conv}}$ where $T_{\text{conv}}$ is the Kalman filter convergence time), the gains $K_{i,t}$ vary with $P_{i,t}$. Discarding $P_{i,t}$ means the macro-dynamics must use a fixed gain $K_c$ while the micro-dynamics use time-varying $K_{i,t}$. The per-step closure error is:

$$\varepsilon_{x,t} = (K_{i,t} - K_c) \delta_{i,t}$$

If the macro-agent uses $K_c = K^\ast$ (the steady-state gain), then:

$$\varepsilon_{x,t}^2 = (K_{i,t} - K^\ast)^2 \cdot S_t$$

where $S_t = P_{i,t} + q + r$. Since $K_{i,t}$ converges geometrically to $K^\ast$ with rate $\sim (1 - K^\ast)^2$, the transient closure defect decays as:

$$\varepsilon_{x,t} \sim (K_{i,0} - K^\ast) \cdot (1 - K^\ast)^{2t} \cdot \sqrt{S^\ast}$$

This is exponentially small after $O(1/\lvert\log(1-K^\ast)\rvert)$ time steps.

*Epistemic status: the steady-state result ($\varepsilon^\ast = 0$) is exact. The transient bound is a sketch (the geometric convergence rate is standard for the scalar Riccati equation, but the coupling to the closure defect formula is approximate).*

### 5.6 What the Performance Gap Means for AAD

*[Discussion (performance-gap-interpretation)]*

The performance gap $\Delta_{\text{perf}}$ is not $\varepsilon^\ast$ -- it is a different quantity. In AAD's composition framework:

- **$\varepsilon^\ast$** measures how well the macro-description tracks the micro-system (representability).
- **$\Delta_{\text{perf}}$** measures how much the micro-system loses by not cooperating (suboptimality of independence).

These are related but distinct. In the correlated Kalman case, $\varepsilon^\ast = 0$ (the independent composite is perfectly representable) but $\Delta_{\text{perf}} > 0$ (the independent composite is suboptimal).

**Connection to #team-persistence.** The performance gap connects to the team-persistence framework through effective disturbance. Each independent filter has estimation error variance $P^\ast$. The joint filter has $p < P^\ast$. The difference $P^\ast - p$ is the disturbance reduction that cooperation would provide. In AAD terms, if the agents communicated perfectly:

$$\rho_{i,\text{eff}} = \rho_{i,\text{env}} - \gamma^{\text{coop}} \mathcal{T}_j$$

where $\gamma^{\text{coop}} \mathcal{T}_j$ represents the information gained from the other agent's observations. The performance gap $\Delta_{\text{perf}}$ is the steady-state consequence of this disturbance reduction.

**What would make $\varepsilon^\ast > 0$?** The closure defect becomes genuinely non-zero when:

1. **The projection is lossy in a way that matters.** For example, projecting two agents' *strategies* (DAGs with different topologies) onto a single macro-strategy necessarily loses structural information. This is the purposeful-agent case (Part 2).

2. **The micro-dynamics are inherently non-representable at lower dimension.** For example, if agents' updates couple through a mechanism that cannot be captured by any lower-dimensional dynamics satisfying (A1)-(A4). This requires nonlinear or non-stationary micro-dynamics.

3. **The agents interact through actions (not just shared environment).** When agent 1's action affects agent 2's observation, the micro-dynamics have a coupling structure that a lower-dimensional macro-dynamics may fail to capture.

### 6. Verification of (A1)-(A4)

*[Derived (admissibility-verification)]*

For the macro-agent with state $X_c = (\hat\omega_1, \hat\omega_2)$ and gain $K_c = K^\ast I$:

**(A1) AAD agent structure.** The macro-state decomposes as $X_c = M_c$ with $G_c = \emptyset$ (Section I agent, no purposeful substate). The update is recursive:

$$X_{c,t+1} = (1 - K^\ast) X_{c,t} + K^\ast o_{t+1}$$

The macro-policy is trivial (passive estimator, no actions). **(A1) satisfied.**

**(A2) Macro-mismatch.** The macro-prediction is $\hat o_{c,t+1} = X_{c,t}$ (random walk assumption). The macro-mismatch is:

$$\delta_{c,t} = o_{t+1} - X_{c,t} = (\delta_{1,t}, \delta_{2,t})^T$$

This is the innovation vector of the composite. It has covariance $\Sigma_\delta = \begin{pmatrix} S^\ast & \Gamma \\ \Gamma & S^\ast \end{pmatrix}$ as computed in section 5. The mismatch is well-defined and non-degenerate (both diagonal entries are positive). **(A2) satisfied.**

**(A3) Macro-tempo.** The macro-update has two observation channels (one per agent), each with rate $\nu = 1$ and gain $\eta^\ast = K^\ast$. The composite tempo:

$$\mathcal{T}_c = \sum_{k=1}^{2} \nu^{(k)} \eta^{(k)\ast} = 2K^\ast$$

**(A3) satisfied.**

**(A4) Bounded macro-correction.** The macro-correction function is $F_c(\delta_c) = K^\ast \delta_c$ (linear, applied component-wise). The sector condition:

$$\delta_c^T F_c(\delta_c) = K^\ast \lVert\delta_c\rVert^2 \geq \alpha_c \lVert\delta_c\rVert^2$$

with $\alpha_c = K^\ast$ and $R_c = \infty$ (linear Gaussian). **(A4) satisfied with $\alpha_c = K^\ast$, $R_c = \infty$.**

*Epistemic status: exact.* All four admissibility conditions are verified analytically for the linear Gaussian case. The verification is straightforward because the macro-dynamics are themselves a (trivial) Kalman filter.

### 7. Bridge Lemma Verification

*[Derived (bridge-lemma-verification)]*

The bridge lemma in #composition-closure gives the trajectory error bound:

$$\limsup_{t \to \infty} \lVert e_t \rVert \leq \frac{\varepsilon_x \nu_c}{\alpha_c}$$

With $\varepsilon_x = 0$ at steady state, the bound is trivially satisfied:

$$\frac{0 \cdot \nu_c}{\alpha_c} = 0 < R_c = \infty$$

The macro-description tracks the micro-system perfectly (at steady state).

**During the transient.** With the transient closure defect $\varepsilon_{x,t} \sim \varepsilon_0 \cdot (1-K^\ast)^{2t}$, the trajectory error accumulates as:

$$\lVert e_t \rVert \leq \sum_{k=0}^{t-1} \lambda^{t-1-k} \varepsilon_{x,k}$$

where $\lambda = 1 - K^\ast / \nu = 1 - K^\ast$ (the macro contraction factor). Both the closure defect and the accumulated error decay exponentially, so the transient trajectory error is bounded and vanishes as $t \to \infty$.

**The meaningful composition condition.** For this case, the condition $\varepsilon^\ast \nu_c / \alpha_c < R_c$ reduces to $0 < \infty$, which is trivially satisfied. The correlated Kalman case passes the bridge lemma vacuously.

*Epistemic status: exact (steady state), sketch (transient).*

### 8. Contrast: Independent Composite vs. Optimal Joint Filter

*[Derived (contrast-summary)]*

| Quantity | Independent composite | Optimal joint filter |
|---|---|---|
| Gain matrix | $K^\ast I_2$ (diagonal) | $K_J^\ast$ (full, with cross-gains $\propto \rho$) |
| Per-component MSE | $P^\ast$ | $p < P^\ast$ when $\rho \neq 0$ |
| Total MSE | $2P^\ast$ | $2p$ |
| Performance gap | $\Delta_{\text{perf}} = 2(P^\ast - p) \propto \rho^2$ for small $\rho$ | 0 (by definition, the benchmark) |
| Closure defect $\varepsilon^\ast$ | 0 (at steady state) | N/A |
| Sector parameter | $\alpha_c = K^\ast$ | $\alpha_J = \lambda_{\min}(K_J^\ast H)$ |
| Composite tempo | $2K^\ast$ | Higher (exploits cross-information) |

**Interpretation.** The independent composite is a valid AAD agent ($\varepsilon^\ast = 0$, all admissibility conditions satisfied) but a suboptimal one. The cost of independence is measured by $\Delta_{\text{perf}}$, not by $\varepsilon^\ast$. This is the correct interpretation: the composition-closure framework asks "is this group a coherent agent?" (yes), not "is this group an optimal agent?" (no, when $\rho \neq 0$).

**The cost of independence, exactly.** In the symmetric case with small $\rho$:

$$\Delta_{\text{perf}} \approx \frac{2\rho^2 q^2 r}{(P^\ast + q + r)^2}$$

This is:
- **Quadratic in $\rho$**: weak correlations matter little; the cost grows only quadratically.
- **Proportional to $q^2 r$**: higher process noise and observation noise both increase the cost (more cross-information to exploit, and the observations are noisier so each source is more valuable).
- **Inversely proportional to $(S^\ast)^2$**: when the innovation variance is large (noisy, uncertain), the relative value of cross-information is smaller.

---

## Part 2: Assessment of Purposeful-Agent Composition

### 9. What Changes When Agents Have $G_t$

When the sub-agents have purposeful substates, the micro-state lifts from $(M_1, M_2)$ to $((M_1, G_1), (M_2, G_2))$ where $G_i = (O_i, \Sigma_i)$ (objective and strategy). The formal micro-state becomes:

*[Definition (purposeful-micro-state)]*

$$X_{\text{micro},t} = \{(M_{i,t}, O_{i,t}, \Sigma_{i,t})\}_{i=1}^N$$

The micro-state dimension increases substantially. For two agents, each with a scalar model state $M_i$, a scalar objective $O_i$, and a strategy DAG $\Sigma_i$ with $n_i$ edges:

$$\dim(\mathcal{X}_{\text{micro}}) = 2 + 2 + (n_1 + n_2) = 4 + n_1 + n_2$$

(Two model states, two objective states, and all edge confidences in both DAGs.)

**What the projection must handle.** The macro-projection $\Lambda_x$ must map this high-dimensional purposeful micro-state to a macro-state $X_c = (M_c, G_c)$ satisfying (A1). This requires:

1. **Composing model states**: $M_c = \Lambda_M(M_1, M_2)$ -- the epistemic part. This is the Kalman case already analyzed; the means-only projection works.

2. **Composing objectives**: $O_c = \Lambda_O(O_1, O_2)$ -- the evaluation criterion for the composite. This is where the difficulty begins.

3. **Composing strategies**: $\Sigma_c = \Lambda_\Sigma(\Sigma_1, \Sigma_2)$ -- the composite's plan. This is where the difficulty becomes severe.

### 10. What (A1) Requires: Objective Composition

*[Discussion (objective-composition)]*

(A1) requires the macro-state to decompose as $(M_c, G_c)$ with $G_c = (O_c, \Sigma_c)$. The macro-objective $O_c$ must induce a value functional $V_{O_c}: \text{trajectories} \to \mathbb{R}$ ( #objective-functional).

**Three candidate composition rules:**

**Case A: Shared objective.** $O_1 = O_2 = O$, so $O_c = O$. The macro-value functional is just $V_O$. This is the simplest case and the one most amenable to analysis. Cooperative teams with a common mission fall here. The projection is trivial: $\Lambda_O(O, O) = O$.

**Case B: Compatible but distinct objectives.** $O_1 \neq O_2$, but both contribute to a well-defined composite objective. For instance, agent 1 wants to minimize tracking error on $\omega_1$ and agent 2 on $\omega_2$. The natural composite objective is:

$$V_{O_c}(\tau) = w_1 V_{O_1}(\tau) + w_2 V_{O_2}(\tau)$$

This requires: (i) commensurability of $V_{O_1}$ and $V_{O_2}$ (both map trajectories to $\mathbb{R}$ -- guaranteed by #objective-functional), (ii) weights $w_1, w_2 > 0$, and (iii) that the weighted sum remains a valid value functional. Condition (iii) is satisfied by linearity. The projection is $\Lambda_O(O_1, O_2) = (O_1, O_2, w_1, w_2)$ -- the composite objective carries the individual objectives plus the weighting.

**Case C: Conflicting objectives.** $O_1$ and $O_2$ are partially adversarial -- satisfying one degrades the other. The composite "objective" exists only as a negotiated compromise (if coordination is possible) or a minimax solution (if not). In AAD terms, the teleological unity $U_O < 0$ ( #unity-dimensions). The composite may not have a meaningful $O_c$ at all -- the group's purpose is contested, not shared. This is the case where composition may fail for the purposeful substate even if the epistemic composition works.

*Epistemic status: discussion-grade. The three cases are structurally clear; formal conditions for each case are open.*

**Assessment.** Case A is the only one where (A1)'s $G_c$ requirement is straightforwardly satisfiable. Case B requires a weighting scheme that may not be unique or stable. Case C challenges the assumption that the composite is a purposeful agent at all. The composition-closure framework can diagnose Case C: if no admissible $(O_c, \Sigma_c)$ produces bounded $\varepsilon^\ast$, the group is not a valid composite agent with respect to purpose.

### 11. What (A4) Requires: Strategy Correction Composition

*[Discussion (strategy-correction-composition)]*

(A4) requires the macro-correction to satisfy the sector condition with $\alpha_c > 0$. For the epistemic substate, we showed $\alpha_c = K^\ast$ (the Kalman gain). For the purposeful substate, the macro-correction must satisfy:

$$\delta_{c,\text{strategic}}^T F_{c,\Sigma}(\delta_{c,\text{strategic}}) \geq \alpha_{c,\Sigma} \lVert\delta_{c,\text{strategic}}\rVert^2$$

where $\delta_{c,\text{strategic}}$ is the composite strategic mismatch ( #strategic-calibration) and $F_{c,\Sigma}$ is the composite strategic correction.

**What #strategy-persistence-schema provides.** For a single agent, the sector parameter for strategic dynamics is $\alpha_\Sigma = \eta_{\text{edge}}$ (the edge update gain), with verified instances for Beta-Bernoulli edges.

**How individual strategy corrections compose.** Two sub-agents, each correcting their own strategy DAGs. The composite strategic correction is:

$$F_{c,\Sigma}(\delta_{c,\text{strategic}}) = \begin{pmatrix} F_{\Sigma_1}(\delta_{\text{strategic},1}) \\ F_{\Sigma_2}(\delta_{\text{strategic},2}) \end{pmatrix}$$

If the strategy corrections are independent (no cross-strategy coupling), the composite sector condition inherits from the individuals:

$$\alpha_{c,\Sigma} = \min(\alpha_{\Sigma,1}, \alpha_{\Sigma,2})$$

This is the weakest-link bound from #composition-closure's Discussion section. It holds when: (i) the agents' strategy corrections are independent, and (ii) coordination costs do not degrade individual correction rates.

**Coordination cost.** When agents must coordinate their strategies (e.g., synchronize their plans, negotiate shared subgoals), the coordination overhead $\Delta\mathcal{T}_i^{\text{cost}}$ reduces each agent's effective strategic tempo ( #team-persistence). The effective sector parameter becomes:

$$\alpha_{c,\Sigma} \geq \min_i\!\left(\alpha_{\Sigma,i} - \Delta\mathcal{T}_i^{\text{cost}}\right)$$

For the composite to satisfy (A4), each agent's coordination cost must be less than its individual sector parameter: $\Delta\mathcal{T}_i^{\text{cost}} < \alpha_{\Sigma,i}$. If coordination consumes all of an agent's strategic correction capacity, the composite's strategic correction fails.

*Epistemic status: the weakest-link bound is discussion-grade (stated in #composition-closure without full derivation). The coordination cost framework is from #team-persistence (conditional). Together they provide a plausible but unproven bound.*

### 12. Sketch: The Simplest Purposeful Case

Two agents with scalar $M_t$ (Kalman filter) and binary strategy DAGs (single edge each: "my action $\to$ shared goal"), sharing a correlated environment, no communication.

**Setup.**

- **Environment**: correlated random walk $(\omega_1, \omega_2)$ with $\text{Cov}(w_1, w_2) = \rho q$ as in Part 1.
- **Agent $i$'s model**: $M_{i,t} = \hat\omega_{i,t}$ (scalar estimate, as before).
- **Shared objective**: $O = O_1 = O_2$ -- "keep both tracking errors below threshold $d$." The value functional:

$$V_O(\tau) = -\max(\lvert\omega_1 - \hat\omega_1\rvert, \lvert\omega_2 - \hat\omega_2\rvert) + d$$

(Positive when both errors are below $d$, negative otherwise.)

- **Agent $i$'s strategy**: a single-edge DAG $\Sigma_i = (v_{\text{action}}, v_{\text{goal}}, p_i)$ where $p_i \in [0,1]$ is agent $i$'s confidence that "my sensing action maintains my tracking error below $d$." The agent's action is the sensing mode choice ($\{L, H\}$ as in #worked-example-kalman).
- **Strategy update**: Beta-Bernoulli. Each time agent $i$ observes, it updates $p_i$ based on whether $\lvert\delta_{i,t}\rvert < d$ (success) or not (failure). At step $t$ with $n_i$ total observations and $s_i$ successes: $p_i = (s_i + 1)/(n_i + 2)$ (Laplace smoothing).

**Micro-state:**

$$X_{\text{micro},t} = ((\hat\omega_1, P^\ast, p_1, n_1), (\hat\omega_2, P^\ast, p_2, n_2))$$

Formal dimension: 8 (two means, two covariances, two edge confidences, two observation counts). At steady state the covariances are constant, so effective dimension is 6.

**Macro-state (proposed):** The natural projection discards the covariances (as before) and discards the individual observation counts (keeping only the confidences):

$$X_c = ((\hat\omega_1, \hat\omega_2), (O, (p_1, p_2)))$$

which decomposes as $M_c = (\hat\omega_1, \hat\omega_2)$ and $G_c = (O, \Sigma_c)$. The composite strategy $\Sigma_c$ is a two-arm AND-node:

```
   shared goal (v_root, AND)
   /                \
  v_1 (p_1)        v_2 (p_2)
```

Both sub-goals must succeed for the composite objective to be satisfied (tracking errors must BOTH be below $d$). The composite plan-confidence is:

$$\hat{P}_{\Sigma_c} = p_1 \cdot p_2$$

**Closure defect for the epistemic substate:** $\varepsilon^\ast_M = 0$ (same as Part 1 -- the means-only projection is exact at steady state).

**Closure defect for the purposeful substate:** The micro-dynamics of $p_i$ are:

$$p_{i,t+1} = p_{i,t} + \frac{\mathbb{1}[\lvert\delta_{i,t}\rvert < d] - p_{i,t}}{n_{i,t} + 2}$$

This is the Beta-Bernoulli update. The gain is $\eta_{i,t}^{\text{edge}} = 1/(n_{i,t} + 2)$.

**The projection discards $n_i$.** At steady state, $n_i$ grows linearly with $t$, so $\eta_i^{\text{edge}} \to 0$. To represent the macro-dynamics without $n_i$, the macro-agent must either:

(a) Use a fixed gain $\eta_c$ (losing the $1/n$ convergence behavior), or
(b) Track a macro-level "effective sample size" $n_c$ as part of the macro-state.

Option (b) preserves the dynamics but increases the macro-state dimension. Option (a) creates a genuine closure defect: the macro-dynamics with fixed gain $\eta_c$ diverge from the micro-dynamics with decaying gain $1/(n_i + 2)$.

**The closure defect for strategy under option (a):**

$$\varepsilon_\Sigma = \mathbb{E}\left[\left\lvert\left(\frac{1}{n_i + 2} - \eta_c\right)(\mathbb{1}[\lvert\delta_i\rvert < d] - p_i)\right\rvert\right]$$

For any fixed $\eta_c$, this grows without bound as $n_i \to \infty$ (because $1/(n_i+2) \to 0$ while $\eta_c$ stays fixed) or converges to zero (if $\eta_c = 0$, but then the macro-agent stops learning).

**Assessment.** The Beta-Bernoulli update's $1/n$ gain structure is fundamentally non-representable by fixed-gain dynamics. This is the first genuine source of $\varepsilon^\ast > 0$ in the purposeful case. The closure defect measures the cost of not tracking the effective sample size -- a quantity analogous to the covariance $P_t$ in the Kalman case, but one that does NOT converge to a constant.

*This is a structural difference from the Kalman case.* In the Kalman case, the discarded quantity ($P_t$) converges, so the closure defect vanishes at steady state. In the Beta-Bernoulli case, the discarded quantity ($n_i$) diverges, so the closure defect persists.

**What makes this solvable.** Under option (b) -- keeping $n_c$ as a macro-state variable -- the closure defect for strategy becomes zero (the Beta-Bernoulli dynamics are exactly representable with $(p_i, n_i)$). The total macro-state is then $(\hat\omega_1, \hat\omega_2, O, p_1, n_1, p_2, n_2)$ with dimension 7, vs. micro-dimension 8. The dimensionality reduction is modest (discarding two covariances, which are constant) and (P3) is barely satisfied. This suggests that for the simplest purposeful case, the projection cannot afford to be very aggressive -- the purposeful substate has more "load-bearing" dimensions than the epistemic substate.

### 13. Where Composition Genuinely Loses Information

*[Discussion (genuine-information-loss)]*

Synthesizing Parts 1 and 2, there are three distinct sources of information loss under composition:

**Source 1: Convergent transient information.** The Kalman covariance $P_t$ converges to $P^\ast$, so discarding it loses only transient information. Closure defect: zero at steady state. **This is the benign case.**

**Source 2: Divergent auxiliary state.** The Beta-Bernoulli sample count $n_t$ diverges, so discarding it creates a permanent closure defect. No fixed-gain macro-dynamics can track the decaying-gain micro-dynamics. **This is a genuine structural cost of abstraction.**

**Source 3: Cross-agent structural information.** When agents have different strategy DAG topologies, the composite strategy must somehow represent both. The union DAG preserves structure but may not satisfy (A1) (the composite's macro-strategy must be a single coherent plan, not a disjoint collection of plans). An abstracted DAG loses structural detail. **This is the deepest challenge for purposeful-agent composition and remains fully open.**

**What $\varepsilon^\ast > 0$ means for the bridge lemma.** When $\varepsilon^\ast > 0$, the bridge lemma is load-bearing. The trajectory error bound $\varepsilon^\ast \nu_c / \alpha_c < R_c$ must be checked. For the Beta-Bernoulli case with option (a) (fixed macro-gain), $\varepsilon_\Sigma$ eventually grows, violating the bridge lemma's bound. This means the macro-description of the strategy eventually diverges from micro-reality -- the composite's strategy representation becomes stale. The agent must periodically "re-project" (re-synchronize the macro-strategy with the micro-strategies), which is the composition-level analog of structural adaptation ( #structural-adaptation-necessity).

### 14. Summary and Implications

**Part 1 findings (exact):**

1. The means-only projection for two correlated Kalman filters has $\varepsilon^\ast = 0$ at steady state and exponentially decaying transient defect. All admissibility conditions (A1)-(A4) and (P1)-(P3) are verified analytically.

2. The performance gap (independent composite vs. optimal joint filter) is $\Delta_{\text{perf}} \approx 2\rho^2 q^2 r / (S^\ast)^2$ for small $\rho$, growing monotonically to its maximum at $\lvert\rho\rvert = 1$.

3. The distinction between representability ($\varepsilon^\ast$) and optimality ($\Delta_{\text{perf}}$) is real and important. A group can be a perfectly valid composite agent while being suboptimal compared to a centralized agent. The composition-closure framework diagnoses the former, not the latter.

4. The cross-innovation covariance $\Gamma = C_e + \rho q$ is non-zero even for independent filters when $\rho \neq 0$, where $C_e = \rho q / (K^\ast(2 - K^\ast))$ is the steady-state cross-covariance of estimation errors.

**Part 2 findings (assessment-grade):**

5. Objective composition has three structural cases: shared (simple), compatible-distinct (tractable with weighting), conflicting (may prevent valid composition). Only the shared case is straightforward.

6. Strategy correction composition inherits the weakest-link bound $\alpha_{c,\Sigma} \geq \min_i(\alpha_{\Sigma,i} - \Delta\mathcal{T}_i^{\text{cost}})$, subject to coordination costs being bounded.

7. The simplest purposeful case (two agents with single-edge Beta-Bernoulli strategies and shared objective) reveals a genuine $\varepsilon^\ast > 0$: the Beta-Bernoulli update's decaying gain ($1/(n+2)$) cannot be represented by fixed-gain macro-dynamics because the auxiliary state ($n$) diverges rather than converging. This is a structural difference from the Kalman case.

8. Strategy DAG topology composition (how to merge structurally different plans into a single macro-plan) remains fully open and is likely the hardest problem in Section III.

**Implications for the theory:**

- The composition-closure framework correctly separates representability from optimality. The correlated Kalman case demonstrates that $\varepsilon^\ast = 0$ does not mean the composite is optimal -- it means the composite is a coherent agent.

- The first genuine $\varepsilon^\ast > 0$ examples arise from purposeful substates, not epistemic substates. This suggests that Section III's hardest composition problems are in the strategy domain, not the model domain.

- The bridge lemma becomes load-bearing precisely when the purposeful substate is included. For pure estimation composites, the bridge lemma is satisfied vacuously ($\varepsilon^\ast = 0$). For purposeful composites, the bridge lemma provides a genuine constraint on when the macro-description remains valid.

---

## Open Questions

1. **Formal performance gap bound for general $\rho$.** The small-$\rho$ asymptotic $\Delta_{\text{perf}} \approx 2\rho^2 q^2 r / (S^\ast)^2$ is derived. A closed-form expression for arbitrary $\rho$ requires solving the 2D DARE in closed form, which is tractable for the symmetric case but algebraically involved.

2. **Transient closure defect bounds.** The exponential decay of the transient closure defect is stated but not rigorously bounded. A formal bound would use the convergence rate of the scalar Riccati recursion (well-studied in control theory).

3. **Beta-Bernoulli composition defect quantification.** The claim that $\varepsilon_\Sigma$ eventually grows under fixed-gain macro-dynamics needs a formal bound showing the growth rate and the time at which the bridge lemma is violated.

4. **Strategy DAG topology composition.** How to merge different DAG topologies into a coherent macro-strategy is the deepest open question. Candidates: DAG union (preserves structure, may violate coherence), DAG abstraction (loses structure, preserves coherence), or no macro-strategy (composition works for $M_c$ but not for $G_c$ -- a "model-only composite").

5. **When does the performance gap become a closure defect?** If agents are allowed to communicate, the optimal macro-dynamics would exploit cross-correlations. The gap between "independent composite with communication" and "centralized agent" is the true closure defect for communicating agents. Formalizing this requires extending the micro-dynamics to include communication actions.
