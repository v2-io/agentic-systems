# Spike: The Update-Gain → Sector-Condition Bridge

**Status**: Spike (investigatory). Attempts to close the theory's softest structural joint — the gap between the gain-based update mechanism and the sector condition assumed by the Lyapunov stability results.

**Date**: 2026-04-02

**Objective**: Determine whether gain-based updating (the uncertainty-ratio principle, #emp-update-gain) produces correction dynamics satisfying the sector condition (GA-3), thereby grounding the quantitative predictions that flow through #deriv-sector-condition.

**Depends on**: #emp-update-gain, #deriv-sector-condition, #result-sector-condition-stability, #result-persistence-condition, #hyp-mismatch-dynamics, #def-adaptive-tempo, #example-kalman

---

## 0. The Gap

AAD's quantitative prediction chain:

$$\text{gain principle} \;\xrightarrow{\text{GA-3 assumed}}\; \text{sector condition} \;\xrightarrow{\text{Lyapunov (exact)}}\; \text{persistence, reserve, adversarial scaling}$$

The right arrow is proved (Props A.1, A.1S, A.2 in #deriv-sector-condition). The left arrow is *assumed*: GA-3 states $\delta^T F(\mathcal{T}, \delta) \geq \alpha \|\delta\|^2$ for $\|\delta\| \leq R$, but whether the correction function $F$ induced by the gain principle $M_t = M_{t-1} + \eta^* \cdot g(\delta_t)$ actually satisfies this is never derived.

The single-edge spike (`spike-single-edge-strategic-dynamics.md`) verified the bridge for Beta-Bernoulli, where the expected correction is exactly linear: $F(\delta) = \delta/(n+1)$, giving $\alpha = 1/(n+1)$ trivially.

This spike investigates the Kalman filter case, then generalizes.

---

## 1. The Kalman Filter: Setup

Consider a linear-Gaussian system:

$$x_{t+1} = A x_t + v_t, \qquad v_t \sim \mathcal{N}(0, Q)$$
$$o_t = H x_t + \varepsilon_t, \qquad \varepsilon_t \sim \mathcal{N}(0, R_{\text{obs}})$$

where $x_t \in \mathbb{R}^n$ is the state, $o_t \in \mathbb{R}^m$ is the observation, $A$ is the dynamics matrix, $H$ is the observation matrix, $Q$ is the process noise covariance, and $R_{\text{obs}}$ is the observation noise covariance. (We write $R_{\text{obs}}$ to avoid collision with the sector-condition radius $R$.)

The Kalman filter maintains $M_t = (\hat{x}_{t|t}, P_{t|t})$ where $\hat{x}_{t|t}$ is the state estimate and $P_{t|t}$ is the error covariance.

**Prediction step:**

$$\hat{x}_{t|t-1} = A \hat{x}_{t-1|t-1}$$
$$P_{t|t-1} = A P_{t-1|t-1} A^T + Q$$

**Update step:**

$$K_t = P_{t|t-1} H^T (H P_{t|t-1} H^T + R_{\text{obs}})^{-1}$$
$$\hat{x}_{t|t} = \hat{x}_{t|t-1} + K_t (o_t - H \hat{x}_{t|t-1})$$
$$P_{t|t} = (I - K_t H) P_{t|t-1}$$

The innovation (mismatch) is $\delta_t = o_t - H \hat{x}_{t|t-1} \in \mathbb{R}^m$.

---

## 2. Identifying the Correction Function

### 2.1 Which Space?

The sector condition operates on mismatch dynamics: $d\delta/dt = -F(\mathcal{T}, \delta) + w(t)$. We need to identify the correction function $F$ and the space it operates in.

**Option A: State-space mismatch.** Define $e_t = x_t - \hat{x}_{t|t} \in \mathbb{R}^n$ (the estimation error). The state correction is $K_t \delta_t$, but this corrects the *state estimate*, not the mismatch directly.

**Option B: Observation-space mismatch.** The innovation $\delta_t = o_t - H \hat{x}_{t|t-1} \in \mathbb{R}^m$. This is the mismatch in the space where the agent measures discrepancy.

**Option C: Predicted-observation-space.** Track $\hat{\delta}_t = H e_t = H(x_t - \hat{x}_{t|t})$, the projection of the state error into observation space. This is the predictable part of the next innovation.

We work in **observation space** (Option B), because that is where AAD defines the mismatch signal (#def-mismatch-signal): $\delta_t = o_t - \hat{o}_t$, with $\hat{o}_t = H \hat{x}_{t|t-1}$.

### 2.2 Mismatch Dynamics in Observation Space

The estimation error evolves as:

$$e_t = x_t - \hat{x}_{t|t} = x_t - \hat{x}_{t|t-1} - K_t \delta_t$$

Since $\delta_t = H(x_t - \hat{x}_{t|t-1}) + \varepsilon_t = H e_{t|t-1} + \varepsilon_t$ (where $e_{t|t-1} = x_t - \hat{x}_{t|t-1}$):

$$e_t = e_{t|t-1} - K_t(H e_{t|t-1} + \varepsilon_t) = (I - K_t H) e_{t|t-1} - K_t \varepsilon_t$$

At the next prediction step: $e_{t+1|t} = A e_t + v_t$.

The observation-space error at the next step (the "predictable mismatch component") is:

$$H e_{t+1|t} = H A e_t + H v_t = H A (I - K_t H) e_{t|t-1} - H A K_t \varepsilon_t + H v_t$$

This is getting complicated. Let us instead work with the *expected* correction and then state-space mismatch, which gives cleaner results.

### 2.3 State-Space Analysis (Cleaner Path)

Define the state-space mismatch (estimation error): $e_t = x_t - \hat{x}_{t|t}$.

After the prediction step, the prior error is $e_{t|t-1} = x_t - \hat{x}_{t|t-1} = A e_{t-1} + v_{t-1}$.

The correction step reduces this to:

$$e_t = (I - K_t H) e_{t|t-1} - K_t \varepsilon_t$$

Taking the expected outer product (the error covariance), the standard Kalman result gives:

$$P_{t|t} = (I - K_t H) P_{t|t-1}$$

The key quantity: the correction step transforms $e_{t|t-1}$ to $e_t = (I - K_t H) e_{t|t-1} + \text{noise}$. The *expected* correction (in state space) is:

*[Derived (Kalman expected state correction)]*

$$\mathbb{E}[\Delta e \mid e_{t|t-1}] = \mathbb{E}[e_t - e_{t|t-1} \mid e_{t|t-1}] = -K_t H \cdot e_{t|t-1}$$

So the correction function in state space is:

$$F_{\text{state}}(e) = K_t H \cdot e$$

This is linear with matrix $K_t H$.

### 2.4 The Sector Condition in State Space

*[Derived (Kalman sector condition, state space)]*

The sector condition requires $e^T F_{\text{state}}(e) \geq \alpha \|e\|^2$, i.e.:

$$e^T K_t H \cdot e \geq \alpha \|e\|^2 \quad \forall e$$

This holds iff the symmetric part of $K_t H$ is positive definite with minimum eigenvalue $\geq \alpha$:

$$\frac{1}{2}(K_t H + H^T K_t^T) \succeq \alpha I$$

**Claim:** The symmetric part of $K_t H$ is positive semidefinite, and positive definite when $(H, A)$ is observable and $P_{t|t-1}$ is positive definite.

**Proof.** Substitute the Kalman gain $K_t = P_{t|t-1} H^T S_t^{-1}$ where $S_t = H P_{t|t-1} H^T + R_{\text{obs}}$ is the innovation covariance:

$$K_t H = P_{t|t-1} H^T S_t^{-1} H$$

Consider the quadratic form:

$$e^T K_t H \, e = e^T P_{t|t-1} H^T S_t^{-1} H \, e$$

Let $z = H e$ (the projection of the state error into observation space). Then:

$$e^T K_t H \, e = e^T P_{t|t-1} H^T S_t^{-1} z$$

This is not immediately a clean quadratic form because $P_{t|t-1}$ couples different directions. Let us try a different approach.

**Direct approach via the Joseph form.** The posterior covariance satisfies:

$$P_{t|t} = (I - K_t H) P_{t|t-1} (I - K_t H)^T + K_t R_{\text{obs}} K_t^T$$

But also $P_{t|t} = P_{t|t-1} - K_t S_t K_t^T$ (from the standard formula). Therefore:

$$P_{t|t-1} - P_{t|t} = K_t S_t K_t^T$$

This is the *covariance reduction* from the update step — it is positive semidefinite by construction ($S_t \succ 0$ when $R_{\text{obs}} \succ 0$). This tells us the update *reduces* total uncertainty, but it doesn't directly give the sector condition on the *state error vector*.

**Spectral approach.** Let us work in the eigenbasis of $P_{t|t-1}$. Write $P = P_{t|t-1}$ for brevity. Since $P \succ 0$, we can write $P = P^{1/2} P^{1/2}$. Define $\tilde{e} = P^{-1/2} e$ and $\tilde{H} = H P^{1/2}$. Then:

$$e^T K H \, e = e^T P H^T (H P H^T + R_{\text{obs}})^{-1} H \, e$$
$$= \tilde{e}^T P^{1/2} P H^T (H P H^T + R_{\text{obs}})^{-1} H P^{1/2} \tilde{e}$$
$$= \tilde{e}^T \tilde{H}^T (\tilde{H} \tilde{H}^T + R_{\text{obs}})^{-1} \tilde{H} \cdot P \cdot P^{-1/2} P^{1/2} \tilde{e}$$

This is getting algebraically awkward. Let us instead work with a cleaner special case first, then generalize.

---

## 3. The Scalar Kalman Case (1D State, 1D Observation)

### 3.1 Setup

$n = m = 1$, $H = 1$ (direct observation), $A = 1$ (random walk). All quantities are scalar.

- Prior variance: $P^- = P_{t|t-1}$
- Innovation covariance: $S = P^- + R_{\text{obs}}$
- Kalman gain: $K = P^- / (P^- + R_{\text{obs}})$

The state-space mismatch is $e = x - \hat{x}$. The correction function is:

$$F(e) = K \cdot e = \frac{P^-}{P^- + R_{\text{obs}}} \cdot e$$

### 3.2 Sector Condition

$$e \cdot F(e) = K \cdot e^2 = \frac{P^-}{P^- + R_{\text{obs}}} \cdot e^2$$

*[Derived (scalar Kalman sector condition)]*

The sector condition $e \cdot F(e) \geq \alpha \cdot e^2$ holds with:

$$\alpha = K = \frac{P^-}{P^- + R_{\text{obs}}} = \eta^*$$

**The sector parameter equals the Kalman gain, which equals the uncertainty-ratio gain.** This is exact, not an approximation. The correction is linear, so the sector bound is tight.

### 3.3 Steady-State Sector Parameter

At steady state, $P^-$ satisfies the algebraic Riccati equation. For the random walk ($A = 1$):

$$P^- = P + Q = (1 - K) P^- + Q = P^-(1 - K) + Q$$
$$K P^- = Q \implies P^- = Q / K$$

Also $K = P^- / (P^- + R_{\text{obs}})$, so $P^- = K(P^- + R_{\text{obs}}) = K P^- + K R_{\text{obs}}$, giving $(1-K) P^- = K R_{\text{obs}}$, i.e., $P^- = K R_{\text{obs}} / (1-K)$.

From $K P^- = Q$: $K \cdot K R_{\text{obs}} / (1-K) = Q$, so $K^2 R_{\text{obs}} = Q(1-K)$, giving:

$$K^2 R_{\text{obs}} + Q K - Q = 0$$

$$K = \frac{-Q + \sqrt{Q^2 + 4 Q R_{\text{obs}}}}{2 R_{\text{obs}}}$$

(taking the positive root). The steady-state sector parameter is:

*[Derived (steady-state scalar Kalman sector parameter)]*

$$\alpha_{ss} = K_{ss} = \frac{-Q + \sqrt{Q^2 + 4 Q R_{\text{obs}}}}{2 R_{\text{obs}}}$$

**Limiting cases:**
- $Q \gg R_{\text{obs}}$ (fast dynamics, clean observations): $K_{ss} \to 1$, $\alpha_{ss} \to 1$. The agent trusts observations fully; maximum correction efficiency.
- $Q \ll R_{\text{obs}}$ (slow dynamics, noisy observations): $K_{ss} \approx \sqrt{Q / R_{\text{obs}}}$, $\alpha_{ss} \approx \sqrt{Q / R_{\text{obs}}}$. Correction efficiency degrades as the square root of the signal-to-noise ratio.
- $Q = 0$ (static target): $K_{ss} \to 0$, $\alpha_{ss} \to 0$. No correction needed (and no disturbance $w = 0$), so the persistence question is vacuous.

### 3.4 Connection to AAD Quantities

The adaptive tempo (for a single observation channel at rate $\nu$):

$$\mathcal{T} = \nu \cdot K_{ss}$$

And the sector parameter (in the continuous-time AAD framework) is $\alpha = \mathcal{T} = \nu \cdot K_{ss}$. The bridge holds trivially in the scalar Kalman case: the gain IS the sector parameter. The linear correction means the sector bound is tight, not merely a lower bound.

This matches the worked example (#example-kalman) where $\alpha$ is reported from data but the derivation from $K$ is not shown.

---

## 4. The Matrix Kalman Case (General $n$, $m$)

### 4.1 The Correction Matrix

The state-space correction function is $F(e) = K H \cdot e$ with $K = P^- H^T (H P^- H^T + R_{\text{obs}})^{-1}$.

So $KH = P^- H^T (H P^- H^T + R_{\text{obs}})^{-1} H$.

The sector condition requires:

$$e^T (KH) e \geq \alpha \|e\|^2 \quad \forall e \in \mathbb{R}^n$$

Since the sector condition involves $e^T (KH) e$, we need the symmetric part $\frac{1}{2}(KH + (KH)^T)$ to have minimum eigenvalue $\geq \alpha$. But first we must check: is $KH$ even positive semidefinite in the symmetric-part sense?

### 4.2 Positive Semidefiniteness of $KH$

*[Derived (KH quadratic form)]*

Write $S = H P^- H^T + R_{\text{obs}} \succ 0$, so $K = P^- H^T S^{-1}$ and:

$$e^T K H \, e = e^T P^- H^T S^{-1} H \, e$$

Let $u = S^{-1/2} H e$ (well-defined since $S \succ 0$). Let $v = S^{-1/2} H P^- e$. We need to express the quadratic form more carefully.

Actually, let us use a different decomposition. Note:

$$e^T K H \, e = (H e)^T S^{-1} (H P^- e) = (H e)^T S^{-1} H P^- e$$

This is NOT a standard quadratic form in $e$ because $H$ and $P^-$ can be asymmetric in their effect. However, we can bound it.

**Symmetrization.** The symmetric part of $KH$ is:

$$\text{sym}(KH) = \frac{1}{2}(P^- H^T S^{-1} H + H^T S^{-T} H P^-)$$

Since $S$ is symmetric and positive definite, $S^{-T} = S^{-1}$. So:

$$\text{sym}(KH) = \frac{1}{2}(P^- H^T S^{-1} H + H^T S^{-1} H P^-)$$

For this to be positive definite, we need to work harder. Let us use a congruence argument.

### 4.3 The Key Identity

*[Derived (covariance reduction identity)]*

From the Kalman covariance update:

$$P = P^- - K S K^T = P^- - P^- H^T S^{-1} H P^-$$

Therefore:

$$P^- - P = P^- H^T S^{-1} H P^- = (KH) P^- = K S K^T$$

This is positive semidefinite (since $S \succ 0$). But this gives $(KH) P^-$ is symmetric positive semidefinite, not $KH$ directly.

Since $P^- \succ 0$, we can write $(KH) P^- \succeq 0 \implies (P^-)^{-1/2} (KH) P^- (P^-)^{-1/2} = (P^-)^{-1/2} (KH) (P^-)^{1/2} \succeq 0$.

This tells us $KH$ is *similar* to a positive semidefinite matrix (via the congruence $P^{-1/2} (\cdot) P^{1/2}$), so its eigenvalues are all non-negative. But the quadratic form $e^T (KH) e$ is not guaranteed to be non-negative for all $e$ because $KH$ need not be symmetric.

**However**, we can work with the appropriate inner product. Since $P^- \succ 0$, define the $P^-$-weighted inner product: $\langle u, v \rangle_{P^-} = u^T (P^-)^{-1} v$.

In this inner product:

$$\langle e, KH \, e \rangle_{P^-} = e^T (P^-)^{-1} KH \, e = e^T (P^-)^{-1} P^- H^T S^{-1} H \, e = e^T H^T S^{-1} H \, e$$

and $H^T S^{-1} H$ is symmetric positive semidefinite (since $S \succ 0$). So:

$$e^T H^T S^{-1} H \, e \geq 0 \quad \forall e$$

with equality iff $He = 0$ (i.e., $e$ is in the null space of $H$).

### 4.4 Sector Condition with the Appropriate Lyapunov Function

This suggests the sector condition holds NOT with $V(e) = \frac{1}{2}\|e\|^2$ (the standard Euclidean norm) but with the weighted Lyapunov function:

*[Derived (weighted Lyapunov function for Kalman)]*

$$V(e) = \frac{1}{2} e^T (P^-)^{-1} e$$

Then:

$$\dot{V}_{\text{correction}} = -e^T (P^-)^{-1} K H \, e = -e^T H^T S^{-1} H \, e$$

We need $e^T H^T S^{-1} H \, e \geq \alpha \cdot e^T (P^-)^{-1} e$, i.e.:

$$H^T S^{-1} H \succeq \alpha (P^-)^{-1}$$

or equivalently:

$$P^- H^T S^{-1} H P^- \succeq \alpha P^-$$

Using $P^- H^T S^{-1} H P^- = P^- - P$:

$$P^- - P \succeq \alpha P^-$$

$$(1 - \alpha) P^- \succeq P$$

$$P \preceq (1 - \alpha) P^-$$

Since $P = (I - KH) P^-$, we need $(I - KH) P^- \preceq (1 - \alpha) P^-$, i.e.:

$$KH \, P^- \succeq \alpha P^-$$

$$KH \succeq \alpha I \quad \text{(in the } P^-\text{-weighted sense)}$$

From $KH = P^- H^T S^{-1} H$, this requires:

$$P^- H^T S^{-1} H \succeq \alpha I$$

**For the fully observable case** ($m = n$, $H$ invertible): $H^T S^{-1} H$ is congruent to $S^{-1}$, and $P^- S^{-1} = P^- (H P^- H^T + R_{\text{obs}})^{-1}$ has eigenvalues in $(0, 1)$ when $R_{\text{obs}} \succ 0$. The minimum eigenvalue of $KH$ gives $\alpha$.

**For the partially observable case** ($m < n$): $H^T S^{-1} H$ has rank $m < n$, so it has a null space. The sector condition fails for error directions $e$ in $\ker(H)$ — errors invisible to the observation. These directions are unobservable, so the correction function literally cannot reduce them.

This is not a pathology but a structural fact: **the sector condition can only hold in the observable subspace.**

### 4.5 The Observable Subspace Result

*[Derived (Kalman sector condition, observable subspace)]*

**Theorem (Kalman Sector Condition).** For a linear-Gaussian system with Kalman filter, the correction function $F(e) = KH \cdot e$ satisfies the sector condition in the $(P^-)^{-1}$-weighted norm:

$$e^T (P^-)^{-1} KH \, e \geq \alpha \cdot e^T (P^-)^{-1} e$$

restricted to the observable subspace $\mathcal{O} = \text{range}(H^T)$, with:

$$\alpha = \lambda_{\min}^+(P^{1/2} (P^-)^{-1} P^{1/2}) = 1 - \lambda_{\max}(P (P^-)^{-1})$$

Wait — let me redo this more carefully. From the identity $(I - KH) P^- = P$ (the posterior covariance), we have $KH = I - P (P^-)^{-1}$. So the eigenvalues of $KH$ (in the $P^-$-weighted sense) are $1 - \lambda_i(P (P^-)^{-1})$, where $\lambda_i(P (P^-)^{-1})$ denotes the generalized eigenvalues of $P$ relative to $P^-$.

Since $P \preceq P^-$ (the posterior is tighter than the prior, in the PSD ordering), we have $P (P^-)^{-1} \preceq I$, so $\lambda_i(P(P^-)^{-1}) \leq 1$, and $1 - \lambda_i(P(P^-)^{-1}) \geq 0$.

But in unobservable directions (where $H e = 0$), the update has no effect: $KH e = 0$, so $\lambda_i(P(P^-)^{-1}) = 1$ in those directions and the sector parameter is 0.

**In observable directions**, $P < P^-$ (strict inequality), so $\lambda_i(P(P^-)^{-1}) < 1$ and $\alpha > 0$.

For the **fully observable, steady-state** case:

$$\alpha = \min_i (1 - \lambda_i(P_{ss} P_{ss}^{-,-1}))$$

where $P_{ss}$ and $P_{ss}^-$ are the steady-state posterior and prior covariances, related by the algebraic Riccati equation.

### 4.6 Explicit Formula: Fully Observable, Diagonal Case

Consider $n = m$, $H = I$, $A = I$ (multidimensional random walk with direct observation), and $Q = \text{diag}(q_1, \ldots, q_n)$, $R_{\text{obs}} = \text{diag}(r_1, \ldots, r_n)$. Then the problem decouples into $n$ scalar problems, and:

$$K_{ss} = \text{diag}(K_1, \ldots, K_n), \quad K_i = \frac{-q_i + \sqrt{q_i^2 + 4 q_i r_i}}{2 r_i}$$

The sector condition holds with $\alpha = \min_i K_i$. In the Euclidean norm (which equals the $(P^-)^{-1}$-norm up to a diagonal rescaling in this decoupled case):

*[Derived (diagonal Kalman sector parameter)]*

$$\alpha = \min_{i=1}^n \frac{-q_i + \sqrt{q_i^2 + 4 q_i r_i}}{2 r_i}$$

The bottleneck is the dimension with the worst signal-to-noise ratio $q_i / r_i$, consistent with the per-dimension persistence result (#result-per-dimension-persistence).

---

## 5. The Bridge: From Gain to Sector Parameter

### 5.1 What the Kalman Case Establishes

The Kalman filter correction function $F(e) = KH \cdot e$ satisfies the sector condition because:

1. **The correction is linear.** $F(e) = KH \cdot e$, so the sector condition reduces to a spectral condition on $KH$.

2. **$KH$ has non-negative eigenvalues** (in the appropriate sense). From $P = (I - KH) P^-$ and $P \preceq P^-$, the eigenvalues of $KH$ in the $P^-$-weighted inner product lie in $[0, 1]$.

3. **The sector parameter is the minimum eigenvalue of $KH$ over observable directions.** In the scalar case, $\alpha = K = \eta^*$ exactly. In the matrix case, $\alpha = \min_{\text{observable}} \lambda_i(KH)$ in the weighted norm.

4. **The sector parameter is bounded below** by a positive constant iff the system is detectable (all unstable modes are observable). For a stable system ($\rho(A) < 1$), the Kalman filter converges and $\alpha > 0$ at steady state, even if some modes are unobservable — the stable unobservable modes decay naturally.

### 5.2 The General Bridge Theorem

Now generalize beyond Kalman. The gain principle (#emp-update-gain) gives:

$$M_t = M_{t-1} + \eta^* \cdot g(\delta_t)$$

where $\eta^* = U_M / (U_M + U_o)$ and $g$ maps mismatch to the update direction.

**When does this satisfy the sector condition?**

Define the induced correction function (in expected value):

$$F(\delta) = -\mathbb{E}[\Delta\delta \mid \delta] = -\mathbb{E}[\delta_{t+1} - \delta_t \mid \delta_t = \delta]$$

The sector condition $\delta^T F(\delta) \geq \alpha \|\delta\|^2$ then requires:

**(S1) Directional alignment.** The expected correction must point in the *mismatch-reducing* direction: $\delta^T F(\delta) \geq 0$. Equivalently, $\delta^T \mathbb{E}[\Delta\delta] \leq 0$ — the expected update reduces the projection of the mismatch.

**(S2) Proportional lower bound.** The correction magnitude must scale at least linearly with $\|\delta\|$: $|\delta^T F(\delta)| \geq \alpha \|\delta\|^2$.

### 5.3 Sufficient Conditions for the Bridge

*[Derived (sufficient conditions for gain → sector bridge)]*

**Theorem (Gain-to-Sector Bridge).** The gain-based update $M_t = M_{t-1} + \eta^* \cdot g(\delta_t)$ induces a correction function satisfying the sector condition with parameter $\alpha > 0$ if:

**(B1) Directional fidelity.** The mismatch transform $g$ preserves the inner-product sign: $\delta^T g(\delta) \geq c \|\delta\|^2$ for some $c > 0$ and all $\|\delta\| \leq R$. That is, $g$ does not rotate the correction away from the mismatch direction.

**(B2) Positive gain.** $\eta^* > 0$ (the agent actually updates).

**(B3) Observation-to-mismatch coupling.** The correction $\eta^* g(\delta)$ applied to the model state induces a proportional reduction in the observation-space mismatch. Specifically, if $H$ is the observation function and the correction in state space is $\eta^* g(\delta)$, then the resulting change in predicted observation satisfies $\delta^T H \eta^* g(\delta) \geq \alpha \|\delta\|^2$.

Under these conditions, the sector parameter is:

$$\alpha = \eta^* \cdot c_{\min}$$

where $c_{\min} = \inf_{\|\delta\| \leq R} \frac{\delta^T H g(\delta)}{\|\delta\|^2}$ is the worst-case directional fidelity of the observation-space correction.

**Proof.** The expected mismatch change from the update is:

$$\mathbb{E}[\Delta\delta_{\text{correction}}] = -H \cdot \eta^* \cdot g(\delta)$$

(the minus sign because the correction *reduces* mismatch). So $F(\delta) = H \eta^* g(\delta)$, and:

$$\delta^T F(\delta) = \eta^* \cdot \delta^T H g(\delta) \geq \eta^* \cdot c_{\min} \|\delta\|^2 = \alpha \|\delta\|^2 \quad \square$$

### 5.4 Verification for Known Cases

**Case 1: Scalar Kalman.** $H = 1$, $g(\delta) = \delta$ (identity transform), $\eta^* = K = P^-/(P^- + R_{\text{obs}})$. Then $c_{\min} = 1$, $\alpha = K$. Bridge holds with $\alpha = \eta^*$. $\checkmark$

**Case 2: Matrix Kalman.** $g(\delta) = H^T S^{-1} \delta \cdot P^- / \|P^- H^T S^{-1}\|$ (the Kalman gain direction), $\eta^* = \|K\|$ (the gain magnitude). More precisely, the Kalman update has the matrix form $Kg(\delta) = K\delta$ with $K$ the full Kalman gain matrix. Then $F(\delta) = HK\delta$ and $\alpha = \lambda_{\min}^+(HK)$ (minimum positive eigenvalue). The bridge holds with $\alpha$ determined by the spectral structure of $HK$. $\checkmark$

**Case 3: Beta-Bernoulli (single edge).** $H = 1$ (scalar), $g(\delta) = \delta$ (identity), $\eta^* = 1/(n+1)$. Then $\alpha = 1/(n+1)$, matching the single-edge spike. $\checkmark$

**Case 4: Exponential family (conjugate).** For a conjugate-prior update on a natural exponential family with sufficient statistic $T(o)$, the update in natural parameter space is additive: $\theta_{\text{post}} = \theta_{\text{prior}} + \Delta\theta$ where $\Delta\theta$ depends on $T(o)$. The expected correction in the mean parameter space has the form $F(\mu) = \eta_{\text{eff}} \cdot (\mu_{\text{true}} - \mu)$, where $\eta_{\text{eff}} = 1/(n+1)$ for $n$ prior observations (in the scalar conjugate case). This generalizes the Beta-Bernoulli. The bridge holds with $\alpha = \eta_{\text{eff}} = 1/(n+1)$. $\checkmark$

---

## 6. What Breaks the Bridge

### 6.1 Failure Mode 1: Directional Infidelity ($g$ Rotates Away from $\delta$)

If the mismatch transform $g$ rotates the correction direction away from the mismatch, $\delta^T g(\delta)$ can become negative or zero.

**Concrete example.** Suppose $\delta \in \mathbb{R}^2$ and $g(\delta) = R_{90} \delta$ where $R_{90}$ is a 90-degree rotation. Then $\delta^T g(\delta) = \delta^T R_{90} \delta = 0$ for all $\delta$. The correction is perpendicular to the mismatch and never reduces it. The sector condition fails with $\alpha = 0$.

**When does this happen in practice?** When the model parameterization is poorly aligned with the observation space. For example, if the model updates latitude when the mismatch is in longitude (a coordinate mismatch between model space and observation space). Well-designed systems avoid this, but nothing in the gain principle *guarantees* directional fidelity.

**For optimal Bayesian updates** (including all conjugate families and the Kalman filter), directional fidelity holds by construction: the update minimizes expected posterior loss, which ensures the correction aligns with the mismatch. The gain principle $\eta^* = U_M/(U_M + U_o)$ implicitly assumes the update direction is correct; the uncertainty ratio determines only the magnitude.

### 6.2 Failure Mode 2: Gain Collapse ($\eta^* \to 0$ Prematurely)

If $\eta^* \to 0$ while $\rho > 0$ (non-stationary environment), the sector parameter $\alpha \to 0$ and the persistence condition $\alpha > \rho/R$ eventually fails.

This is the same gain-collapse phenomenon identified in the single-edge spike (Section 4.3 there): an agent that accumulates experience in a changing environment will eventually have gain too small to track the changes.

**This is not a failure of the bridge but of the persistence condition.** The bridge holds ($\alpha = \eta^* > 0$ for finite experience), but the persistence threshold is violated when $\eta^*$ falls below $\rho/R$.

### 6.3 Failure Mode 3: Nonlinear Saturation

If $g$ is a saturating function — e.g., $g(\delta) = \tanh(\delta)$ — then for large $\|\delta\|$:

$$\delta^T g(\delta) = \delta \tanh(\delta) \approx |\delta|$$

while $\|\delta\|^2 = \delta^2$. The ratio $\delta^T g(\delta) / \|\delta\|^2 \approx 1/|\delta| \to 0$ as $|\delta| \to \infty$.

The sector condition fails globally but holds locally for $\|\delta\| \leq R$ with:

$$\alpha = \eta^* \cdot \inf_{|\delta| \leq R} \frac{\tanh(\delta)}{\delta} = \eta^* \cdot \frac{\tanh(R)}{R}$$

For small $R$, $\alpha \approx \eta^*$ (the linear regime). For large $R$, $\alpha \approx \eta^* / R$ (the saturated regime).

**This is not a failure of the bridge but a constraint on $R$.** The sector condition holds locally; the valid region shrinks as the nonlinearity strengthens. This is exactly the design of A2' — the local sector condition anticipates saturation.

### 6.4 Failure Mode 4: Unobservable Directions

As shown in Section 4.4, when $m < n$ (fewer observations than state dimensions), the correction function has no effect in unobservable directions. The sector condition fails in those directions: $e^T KH \, e = 0$ for $e \in \ker(H)$.

**This is a fundamental structural limitation, not an approximation.** The agent cannot correct errors it cannot observe. In AAD terms: the model class capacity $R$ in unobservable directions is effectively infinite (no correction, but no disturbance detection either), or equivalently, $\alpha = 0$ in those directions.

For the sector condition to hold in the full state space, the system must be *detectable* — all unstable modes must be observable. Stable unobservable modes decay naturally (via $A$) without needing correction.

### 6.5 Failure Mode 5: Model Misspecification

The gain principle assumes the model class contains the truth (or a reasonable approximation). If the model class is wrong — e.g., fitting a linear model to quadratic dynamics — then the expected correction does not point toward the true state. The mismatch transform $g$ is computed under a false model, and directional fidelity (B1) fails.

In AAD terms: this is the model-class-fitness condition $\mathcal{F}(\mathcal{M}) < 1$. When the model class cannot represent reality, the correction function's sector parameter degrades. The sector condition holds with reduced $\alpha$ (or fails entirely) proportional to the model misspecification.

This is the trigger for structural adaptation (#result-structural-adaptation-necessity): the sector condition fails not because the gain is wrong but because the correction *direction* is wrong.

---

## 7. Assessment: Is the Bridge Derivable?

### 7.1 What We Have Shown

1. **For linear correction functions** (Kalman, Beta-Bernoulli, conjugate Bayesian): the bridge holds with $\alpha = \eta^*$ (scalar) or $\alpha = \lambda_{\min}^+(KH)$ (matrix). This is a **derivation**, not an assumption.

2. **For nonlinear but monotone corrections** (saturating $g$, threshold $g$): the bridge holds locally with $\alpha$ depending on the nonlinearity and the region $R$. This is a **derivation** (under the assumption that $g$ satisfies directional fidelity).

3. **For arbitrary corrections**: the bridge requires directional fidelity (B1), which is a structural property of the update rule, not a consequence of the gain principle alone.

### 7.2 The Verdict

**The bridge is derivable for all optimal Bayesian updates and their fluid-limit approximations.** The key insight is:

> An optimal Bayesian update, by construction, moves the posterior toward the truth. The gain $\eta^*$ controls how far. The correction function inherits the sector condition from the optimality of the Bayesian update.

More precisely: for any update that minimizes expected posterior loss (e.g., KL divergence from the true posterior), the expected correction aligns with the mismatch, and the gain controls the sector parameter.

**The bridge is NOT derivable for arbitrary $g$.** A pathological mismatch transform (one that rotates the correction away from the mismatch) violates the sector condition regardless of the gain.

**The bridge is NOT a convergent choice** (it is not merely one of several equivalent formulations). It is a *conditional derivation*: derivable under the assumption that the update rule is optimal (or at least directionally correct).

### 7.3 Reclassification of GA-3

The current status of GA-3 is "Global Assumption" — it is listed alongside GA-1 (fresh noise) and GA-2 (bounded disturbance) as a foundational assumption of the theory.

This spike shows GA-3 should be **reclassified as a derived conditional result**: it follows from the gain principle *when the update rule satisfies directional fidelity*. The sector condition is not an independent assumption but a *consequence* of well-designed updating.

**Proposed reclassification:**

| Current | Proposed | Justification |
|---------|----------|---------------|
| GA-3: Sector condition (assumed) | GA-3: Sector condition (derived conditional on B1: directional fidelity) | For optimal Bayesian updates, B1 holds by construction. For approximate updates, B1 is a design requirement, not a global assumption. |

The load-bearing assumption shifts from "the correction function satisfies the sector condition" (opaque — what correction function?) to "the update rule has directional fidelity" (transparent — the correction must at least point in the right direction).

---

## 8. Summary of Results

### 8.1 The Kalman Case

| Quantity | Expression | Status |
|----------|-----------|--------|
| Correction function | $F(e) = KH \cdot e$ (linear) | Exact |
| Sector parameter (scalar) | $\alpha = K = P^-/(P^- + R_{\text{obs}})$ | Derived |
| Sector parameter (matrix) | $\alpha = \lambda_{\min}^+(\text{sym}(KH))$ in $(P^-)^{-1}$-norm | Derived |
| Steady-state $\alpha$ (scalar) | $(-Q + \sqrt{Q^2 + 4QR_{\text{obs}}})/(2R_{\text{obs}})$ | Derived |
| Valid region | Global (linear correction, no saturation) | Structural |
| Sector condition holds? | **Yes** — for observable directions | Derived |
| Bridge closed? | **Yes** — gain → sector parameter is a derivation | |

### 8.2 The General Case

| Update class | Bridge status | Sector parameter | Condition |
|-------------|---------------|------------------|-----------|
| Linear-Gaussian (Kalman) | **Derived** | $\lambda_{\min}^+(KH)$ | Observability |
| Conjugate Bayesian | **Derived** | $\eta_{\text{eff}} = 1/(n+1)$ | Conjugacy |
| Exponential family | **Derived** | Depends on Fisher information geometry | Regularity |
| Monotone nonlinear $g$ | **Derived (local)** | $\eta^* \cdot \inf \delta^T g(\delta)/\|\delta\|^2$ | B1: directional fidelity |
| Arbitrary $g$ | **Fails in general** | N/A | B1 can be violated |
| Misspecified model | **Fails or degrades** | Reduced $\alpha$ | Model-class fitness |

### 8.3 What Changes

**If the bridge is formally established** (as a conditional derivation):

1. **GA-3 loses its status as an independent assumption.** It becomes a consequence of the gain principle + directional fidelity. The theory's assumption count drops by one, and the remaining assumption (B1: directional fidelity) is more transparent and checkable.

2. **The α-T relationship is grounded.** The persistence condition segment notes that "$\alpha$ is monotone increasing in $\mathcal{T}$" is empirically verified for all correction function classes. This becomes *derived* for the linear case ($\alpha = \mathcal{T}$ exactly) and *structurally motivated* for the nonlinear case (higher tempo → larger gain → larger sector parameter, modulo saturation).

3. **The worked example is fully closed.** The Kalman worked example (#example-kalman) currently reports $\alpha = 2.6$ from data. With the bridge, $\alpha$ can be computed from the Kalman gain and observation matrix, making the example fully derived rather than semi-empirical.

4. **The failure modes are precisely characterized.** Instead of "the sector condition might fail," the theory can say exactly when it fails: directional infidelity, unobservable directions, model misspecification, or gain collapse.

**If the bridge remains an assumption:**

1. **The theory's quantitative predictions are conditional on an unverified assumption.** Every numerical result (persistence thresholds, adversarial scaling, adaptive reserve) carries the caveat "if the correction function satisfies the sector condition."

2. **The assumption is at least checkable.** For any specific system, one can compute $\delta^T F(\delta) / \|\delta\|^2$ and verify GA-3 empirically. But the *general* statement "gain-based updates satisfy the sector condition" would remain unproven.

---

## 9. Path to Promotion

### 9.1 To close the bridge formally

1. **Write a segment `gain-sector-bridge.md`** (in `01-aad-core/src/`) that states the conditional derivation: the gain principle + directional fidelity implies the sector condition. Type: `derived`. Status: `conditional` (conditional on B1).

2. **Modify `sector-condition-derivation.md`** to note that GA-3 is derivable from the gain principle under B1, not merely assumed. The Lyapunov proofs themselves are unchanged — they operate downstream of GA-3 regardless of whether GA-3 is assumed or derived.

3. **Modify `NOTATION.md`** to reclassify GA-3 from "Global Assumption" to "Derived (conditional on B1: directional fidelity)."

4. **Update `worked-example-kalman.md`** to derive $\alpha$ from the Kalman gain rather than reporting it "from data."

### 9.2 Open questions remaining

1. **The weighted-norm subtlety.** In the matrix Kalman case, the sector condition holds in the $(P^-)^{-1}$-weighted norm, not the Euclidean norm. The Lyapunov proofs in #deriv-sector-condition use the Euclidean Lyapunov function $V = \frac{1}{2}\|\delta\|^2$. Does the bridge require changing the Lyapunov function, or is the Euclidean version sufficient? For the fully observable case with bounded condition number $\kappa(P^-)$, the two norms are equivalent up to a factor of $\kappa(P^-)$, so $\alpha_{\text{Euclidean}} \geq \alpha_{\text{weighted}} / \kappa(P^-)$. This is a quantitative refinement, not a qualitative issue.

2. **The fluid-limit gap.** The bridge analysis works in expected value (the expected correction satisfies the sector condition). The actual per-step correction is stochastic, with noise that enters as effective disturbance. The single-edge spike (Section 3.2) showed how to decompose this into correction + observation noise. The same decomposition applies to the Kalman case: the observation noise $\varepsilon_t$ contributes $K\varepsilon_t$ to the state update, which acts as an effective disturbance of magnitude $\|K\| \sigma_\varepsilon$ per step. The sector condition on the *expected* correction, combined with the *stochastic* noise, maps exactly to the Prop A.1S framework.

3. **Directional fidelity for approximate updates.** For variational inference, gradient descent, and other approximate methods, directional fidelity (B1) is not guaranteed by optimality. It must be verified empirically or derived from the approximation's properties. For gradient descent on a convex loss, the gradient direction aligns with the mismatch (by convexity), so B1 holds. For non-convex losses, B1 can fail locally.

4. **Time-varying $\alpha$.** The Kalman gain $K_t$ converges to $K_{ss}$ (the steady-state gain) under detectability. During the transient, $\alpha_t$ changes. The sector-condition framework assumes constant $\alpha$. For time-varying $\alpha(t)$, the Lyapunov analysis still works if $\alpha(t) \geq \alpha_{\min} > 0$ for all $t$ (which holds after a finite transient for detectable systems).

---

## 10. Implications for Theory Architecture

The bridge result has a satisfying structural consequence. AAD's formal chain becomes:

$$\text{gain principle} + \text{directional fidelity (B1)} \;\xrightarrow{\text{derived}}\; \text{sector condition (GA-3)} \;\xrightarrow{\text{Lyapunov (exact)}}\; \text{persistence, reserve, scaling}$$

The "softest joint" identified by three independent reviews is not a gap but a conditional derivation. The condition (B1: directional fidelity) is:

- **Trivially satisfied** for optimal Bayesian updates (Kalman, conjugate, exponential family)
- **Satisfied by construction** for gradient-descent-on-convex-loss updates
- **Checkable** for specific approximate update rules
- **Precisely characterizes failure** when it does not hold (model misspecification, pathological parameterization)

This is a materially better epistemic situation than "GA-3 is assumed." The assumption is not eliminated but transformed from an opaque global assumption to a transparent, verifiable design condition on the update rule.

The theory can now make a clean conditional statement: **if your update rule has directional fidelity — if the correction at least points toward reality — then the Lyapunov stability results follow.** For well-designed agents (optimal Bayesian updaters, Kalman filters, conjugate posteriors), this is automatic. For ad-hoc agents, it is a design constraint.
