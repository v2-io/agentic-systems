# Spike: Bridge Lemma Contraction — From Sector Condition to Full Update Map

**Status**: Exploratory derivation — characterizing the gap, attempting proof, establishing boundary
**Date**: 2026-04-06
**Motivation**: The bridge lemma in #composition-closure requires that bounded closure defect implies bounded trajectory error. The argument needs the full update map $f_c(\cdot, o)$ to be a contraction in its state argument. Currently, (A4) constrains only the *correction component* of $f_c$, not the full map. This is verified for Kalman-type agents but remains an independent assumption for general agents. This spike attempts to close the gap — or, failing that, to characterize exactly what additional conditions are needed and for what agent classes they hold.

**Depends on**: #composition-closure, #sector-condition-derivation, #discrete-sector-condition, #gain-sector-bridge, `msc/spike-composition-bridge-2agent.md`, `msc/spike-composition-correlated-kalman.md`

---

## 1. Precise Statement of the Gap

### 1.1 What the bridge lemma needs

The bridge lemma tracks the trajectory error $e_t = X_{c,t} - \tilde{X}_{c,t}$ where $X_{c,t}$ is the macro-state evolved by macro-dynamics and $\tilde{X}_{c,t} = \Lambda_x(X_{\text{micro},t})$ is the projected micro-state. The per-step decomposition is:

$$e_{t+1} = \underbrace{\big[f_c(\tilde{X}_{c,t} + e_t,\; o_{c,t+1}) - f_c(\tilde{X}_{c,t},\; o_{c,t+1})\big]}_{\text{error propagation term}} + \underbrace{\big[f_c(\tilde{X}_{c,t},\; o_{c,t+1}) - \tilde{X}_{c,t+1}\big]}_{\text{new closure error } \leq \varepsilon_x}$$

The bridge lemma requires:

**(Contraction Property, CP):** For all states $X, X'$ in the macro-state space within the sector-condition region, and for all admissible observations $o$:

$$\lVert f_c(X, o) - f_c(X', o) \rVert \leq \lambda \lVert X - X' \rVert$$

for some $\lambda < 1$ (independent of $o$). This makes the error propagation term contracting: $\lVert f_c(\tilde{X} + e, o) - f_c(\tilde{X}, o) \rVert \leq \lambda \lVert e \rVert$.

### 1.2 What (A4) provides

The sector condition (A4) constrains the correction function $F_c$:

$$\delta_c^T F_c(\mathcal{T}_c, \delta_c) \geq \alpha_c \lVert \delta_c \rVert^2 \quad \text{for } \lVert \delta_c \rVert \leq R_c$$

This says the correction component of the update reduces mismatch. But the full update map $f_c$ has the structure:

$$f_c(X_{c,t}, o_{t+1}) = X_{c,t} - \eta_c F_d(\delta_{c,t}) + \text{observation-driven terms}$$

where $\delta_{c,t} = o_{t+1} - \hat{o}_{c,t+1}(X_{c,t})$ and $F_d$ is the discrete correction direction. The sector condition constrains $F_d$; it does not directly constrain the observation-driven terms.

### 1.3 The gap, precisely stated

**The gap is the observation-driven amplification.** When comparing $f_c(X, o)$ and $f_c(X', o)$ for the same observation $o$ but different states $X \neq X'$:

1. The mismatch signals differ: $\delta(X) = o - \hat{o}(X) \neq o - \hat{o}(X') = \delta(X')$.
2. The corrections differ accordingly: $F_d(\delta(X)) \neq F_d(\delta(X'))$.
3. Any observation-driven term that depends on the state may amplify or attenuate the difference $X - X'$.

The sector condition guarantees that the correction *component* acts contractively (under the discrete-sector-Lipschitz conditions from #discrete-sector-condition). The question is whether other components of the update can amplify state differences enough to overwhelm the correction's contraction.

---

## 2. Decomposition of the Full Update Map

### 2.1 General AAD update structure

The general discrete-time AAD update for the macro-agent has the form (from #event-driven-dynamics and #recursive-update):

*[Definition (general-update-decomposition)]*

$$f_c(X, o) = X - \eta_c F_d(\delta(X)) + h(X, o)$$

where:
- $X - \eta_c F_d(\delta(X))$: the correction step (parametric update driven by mismatch)
- $h(X, o)$: any residual state-observation coupling

For a mismatch-driven agent, the update is driven entirely by the innovation $\delta = o - \hat{o}(X)$. Most AAD agents have this structure:

$$f_c(X, o) = X + \eta_c \cdot g(\delta(X))$$

where $g$ is the state-space correction induced by the mismatch (incorporating the observation-to-state mapping $H$ from #gain-sector-bridge). The correction function in observation space is $F(\delta) = -H g(\delta)$, so $\delta^T F(\delta) = -\delta^T H g(\delta) \geq \alpha \lVert\delta\rVert^2$ by the sector condition.

### 2.2 The state-difference expansion

Fix an observation $o$ and consider two states $X, X'$ in the macro-state space. Define:

$$\delta = o - \hat{o}(X), \qquad \delta' = o - \hat{o}(X')$$

The state difference through the update is:

$$f_c(X, o) - f_c(X', o) = (X - X') + \eta_c \big[g(\delta) - g(\delta')\big]$$

**Key structural observation.** The mismatch depends on the state through the prediction function: $\hat{o}(X) = h_{\text{pred}}(X)$. Therefore:

$$\delta - \delta' = \hat{o}(X') - \hat{o}(X) = h_{\text{pred}}(X') - h_{\text{pred}}(X)$$

The mismatch difference is determined by the prediction function's sensitivity to state changes, with opposite sign (a higher state prediction means a lower mismatch for the same observation).

### 2.3 The linear (Kalman) case as template

For the Kalman filter: $g(\delta) = K\delta$ (linear), $\hat{o}(X) = HX$ (linear prediction). Then:

$$f_c(X, o) - f_c(X', o) = (X - X') + K H (X' - X) = (I - KH)(X - X')$$

The contraction factor is:

$$\lambda = \lVert I - KH \rVert$$

For the scalar Kalman filter with $H = 1$: $\lambda = |1 - K| = 1 - K^\ast < 1$ since $K^\ast \in (0, 1)$.

For the matrix case: $\lambda = \rho(I - KH)$ (spectral radius), which is $< 1$ whenever the Kalman filter is stable (standard result from estimation theory).

**Why the Kalman case works.** The update map $f_c(X, o) = (I - KH)X + Ko$ is affine in $X$. The matrix $(I - KH)$ is the *complement* of the gain-observation product. The sector condition with $\alpha = \lambda_{\min}^+(KH)$ and the Lipschitz bound with $c_{\max} = \lVert KH \rVert$ together imply $\lambda_{\text{eff}}^2 = 1 - 2\alpha + c_{\max}^2 \eta^2 < 1$ (by the DA2' stability condition from #discrete-sector-condition). But this *is* the contraction of the full update map, because the full update map IS the correction step — there are no additional observation-driven terms independent of the mismatch.

**The key insight from the Kalman case:** The contraction property holds trivially when the entire state update is mismatch-driven. The gap arises only when $f_c$ contains state-dependent terms that are not mediated by the mismatch.

---

## 3. Attempt at a General Proof

### 3.1 Setup: mismatch-driven agents

Consider an agent whose update is purely mismatch-driven:

*[Definition (mismatch-driven update)]*

$$f_c(X, o) = X + \eta \cdot g(o - \hat{o}(X))$$

where $\hat{o}: \mathcal{X} \to \mathcal{O}$ is the prediction function and $g: \mathcal{O} \to \mathcal{X}$ is the correction map (state-space response to innovation).

**Assumption M1 (Lipschitz prediction):** The prediction function is Lipschitz:

$$\lVert \hat{o}(X) - \hat{o}(X') \rVert_\mathcal{O} \leq L_h \lVert X - X' \rVert_\mathcal{X}$$

**Assumption M2 (Lipschitz correction):** The correction map is Lipschitz:

$$\lVert g(\delta) - g(\delta') \rVert_\mathcal{X} \leq L_g \lVert \delta - \delta' \rVert_\mathcal{O}$$

These are the minimal regularity conditions. For the Kalman filter: $L_h = \lVert H \rVert$ and $L_g = \lVert K \rVert$.

### 3.2 Contraction bound for mismatch-driven agents

*[Derived (Conditional on M1, M2, and sector-Lipschitz DA2')]*

**Theorem 1 (Contraction of mismatch-driven update).** Let $f_c(X, o) = X + \eta \cdot g(o - \hat{o}(X))$ satisfy M1 and M2 with $\hat{o}(X)$ Lipschitz-$L_h$ and $g$ Lipschitz-$L_g$. Then:

$$\lVert f_c(X, o) - f_c(X', o) \rVert \leq (1 + \eta L_g L_h) \lVert X - X' \rVert$$

**Proof.**

$$f_c(X, o) - f_c(X', o) = (X - X') + \eta [g(o - \hat{o}(X)) - g(o - \hat{o}(X'))]$$

By M2 (Lipschitz correction):

$$\lVert g(o - \hat{o}(X)) - g(o - \hat{o}(X')) \rVert \leq L_g \lVert \hat{o}(X) - \hat{o}(X') \rVert$$

By M1 (Lipschitz prediction):

$$\leq L_g L_h \lVert X - X' \rVert$$

By triangle inequality:

$$\lVert f_c(X, o) - f_c(X', o) \rVert \leq \lVert X - X' \rVert + \eta L_g L_h \lVert X - X' \rVert = (1 + \eta L_g L_h) \lVert X - X' \rVert$$

$\square$

**This gives EXPANSION, not contraction!** The triangle inequality loses the sign structure. The correction $g(o - \hat{o}(X))$ moves the state *toward* the observation, so when $X$ is further from the truth, the correction is larger and in the right direction. The triangle inequality discards this directional information.

### 3.3 Exploiting the directional structure

The triangle inequality fails because it treats the correction as potentially adversarial. We need to use the fact that the correction *opposes* the state difference. Let us work in inner-product space.

Define $\Delta X = X - X'$ and $\Delta\hat{o} = \hat{o}(X) - \hat{o}(X')$. Then $\Delta\delta = -\Delta\hat{o}$.

The update difference is:

$$f_c(X, o) - f_c(X', o) = \Delta X + \eta [g(\delta) - g(\delta')] = \Delta X - \eta [g(\delta') - g(\delta)]$$

Now compute the squared norm:

$$\lVert f_c(X) - f_c(X') \rVert^2 = \lVert \Delta X \rVert^2 + 2\eta \langle \Delta X, g(\delta) - g(\delta') \rangle + \eta^2 \lVert g(\delta) - g(\delta') \rVert^2$$

The critical term is $\langle \Delta X, g(\delta) - g(\delta') \rangle$. This is where the directional structure enters.

**The sector condition gives us information about $\langle \delta, F_d(\delta) \rangle$, not about $\langle \Delta X, g(\delta) - g(\delta') \rangle$.** These are related but not identical. The sector condition operates in observation space; the contraction property operates in state space.

### 3.4 The observation-state bridge

**Assumption M3 (Prediction alignment).** There exists a constant $\mu > 0$ such that:

$$\langle X - X', g(o - \hat{o}(X)) - g(o - \hat{o}(X')) \rangle \leq -\mu \lVert X - X' \rVert^2$$

for all $X, X'$ in the sector-condition region and all admissible $o$.

This says: the state-space correction difference is negatively aligned with the state difference. When the state is perturbed, the mismatch-driven correction acts to reduce the perturbation.

**Claim: M3 follows from the sector condition plus a regularity condition on the prediction-correction chain.**

*[Attempt at derivation]*

Consider the map $\phi: \mathcal{X} \to \mathcal{X}$ defined by $\phi(X) = g(o - \hat{o}(X))$ for fixed $o$. The Jacobian of $\phi$ is:

$$D\phi(X) = -Dg \cdot D\hat{o}$$

where $Dg$ is the Jacobian of $g$ at $\delta = o - \hat{o}(X)$ and $D\hat{o}$ is the Jacobian of $\hat{o}$ at $X$.

M3 requires $\langle \Delta X, \phi(X) - \phi(X') \rangle \leq -\mu \lVert \Delta X \rVert^2$, which by the mean value theorem (when applicable) is equivalent to:

$$v^T D\phi(X) v \leq -\mu \lVert v \rVert^2 \quad \forall v$$

i.e., $D\phi$ is negative definite with eigenvalues $\leq -\mu$. This means:

$$v^T (Dg \cdot D\hat{o}) \, v \geq \mu \lVert v \rVert^2 \quad \forall v$$

**Connection to the sector condition.** The sector condition says $\delta^T F_d(\delta) \geq c_{\min} \lVert \delta \rVert^2$ (DA2'a). For differentiable $F_d$, this means $\delta^T (DF_d) \delta \geq c_{\min} \lVert \delta \rVert^2$, i.e., $DF_d$ is positive definite with eigenvalues $\geq c_{\min}$.

Now $F_d(\delta) = H g(\delta)$ where $H$ maps state corrections to observation-space mismatch reduction (#gain-sector-bridge). So $DF_d = H \cdot Dg$, and the sector condition gives:

$$\delta^T H \, Dg \, \delta \geq c_{\min} \lVert \delta \rVert^2$$

What we need is:

$$v^T Dg \cdot D\hat{o} \, v \geq \mu \lVert v \rVert^2$$

Setting $\delta = D\hat{o} \, v$ and using the sector condition:

$$(D\hat{o}\, v)^T H \, Dg \, (D\hat{o}\, v) \geq c_{\min} \lVert D\hat{o}\, v \rVert^2$$

This gives us information about $Dg$ acting on vectors of the form $D\hat{o}\, v$, weighted by $H$. What we need is $v^T Dg \, D\hat{o}\, v$ — note the different ordering and the absence of $H$.

**The two expressions coincide when $H = D\hat{o}$.** This is the case when the prediction function and the observation operator are the same linear map (as in the Kalman filter, where $\hat{o}(X) = HX$ and the observation model is $o = HX + v$).

### 3.5 Theorem: Sufficient conditions for contraction

*[Derived (sufficient-conditions-for-contraction)]*

**Theorem 2 (Sufficient Conditions for Full Update Map Contraction).** Let $f_c(X, o) = X + \eta \cdot g(o - \hat{o}(X))$ be a mismatch-driven update with:

**(C1) Sector-Lipschitz condition on $F_d$.** The observation-space correction $F_d(\delta) = H g(\delta)$ satisfies DA2':
- $\delta^T F_d(\delta) \geq c_{\min} \lVert \delta \rVert^2$ (lower sector bound)
- $\lVert F_d(\delta) \rVert \leq c_{\max} \lVert \delta \rVert$ (Lipschitz bound)

**(C2) Linear prediction model.** The prediction function is linear: $\hat{o}(X) = HX$ for a matrix $H$.

**(C3) Bounded gain.** $\eta < 2c_{\min}/c_{\max}^2$ (the DA2' step-size condition).

Then the full update map is a contraction:

$$\lVert f_c(X, o) - f_c(X', o) \rVert_{H^TH} \leq \lambda_{\text{eff}} \lVert X - X' \rVert_{H^TH}$$

where $\lVert v \rVert_{H^TH}^2 = v^T H^T H v$ is the $H$-weighted norm, and $\lambda_{\text{eff}}^2 = 1 - 2\eta c_{\min} + \eta^2 c_{\max}^2 < 1$.

**Proof.**

With linear prediction, $\delta - \delta' = H(X' - X)$, so:

$$f_c(X, o) - f_c(X', o) = (X - X') + \eta[g(\delta) - g(\delta')]$$

Apply $H$ to both sides:

$$H[f_c(X, o) - f_c(X', o)] = H(X - X') + \eta H[g(\delta) - g(\delta')]$$

$$= -(\delta - \delta') + \eta F_d^{\text{diff}}$$

where $F_d^{\text{diff}} = H g(\delta) - H g(\delta') = F_d(\delta) - F_d(\delta')$.

Define $\Delta\delta = \delta - \delta' = H(X' - X)$. Then:

$$H \Delta f = -\Delta\delta + \eta [F_d(\delta) - F_d(\delta')]$$

Now compute the squared $H$-norm of $\Delta f = f_c(X,o) - f_c(X',o)$:

$$\lVert \Delta f \rVert_{H^TH}^2 = \lVert H \Delta f \rVert^2 = \lVert -\Delta\delta + \eta[F_d(\delta) - F_d(\delta')] \rVert^2$$

$$= \lVert \Delta\delta \rVert^2 - 2\eta \langle \Delta\delta, F_d(\delta) - F_d(\delta') \rangle + \eta^2 \lVert F_d(\delta) - F_d(\delta') \rVert^2$$

Now apply the sector-Lipschitz conditions. We need these to apply to differences, not just to absolute values. This requires the *incremental* versions of DA2':

**(DA2'a-inc) Incremental sector bound:**

$$\langle \delta - \delta', F_d(\delta) - F_d(\delta') \rangle \geq c_{\min} \lVert \delta - \delta' \rVert^2$$

**(DA2'b-inc) Incremental Lipschitz bound:**

$$\lVert F_d(\delta) - F_d(\delta') \rVert \leq c_{\max} \lVert \delta - \delta' \rVert$$

The incremental Lipschitz bound (DA2'b-inc) follows from the standard Lipschitz bound DA2'b by the mean value theorem when $F_d$ is differentiable (with the same constant $c_{\max}$), or directly from the Lipschitz condition on $F_d$ itself.

The incremental sector bound (DA2'a-inc) is the *monotonicity* condition: $F_d$ is *strongly monotone* with constant $c_{\min}$. This is strictly stronger than the one-point sector bound DA2'a in general. For differentiable $F_d$, it is equivalent to $\lambda_{\min}(DF_d(\delta)) \geq c_{\min}$ for all $\delta$ in the region — i.e., the Jacobian of $F_d$ is uniformly positive definite. For the important special case where $F_d$ is linear ($F_d(\delta) = A\delta$), both reduce to $\lambda_{\min}^+(A + A^T)/2 \geq c_{\min}$.

**FLAG: The incremental sector bound DA2'a-inc is the key additional assumption.** It does not follow from the one-point sector bound DA2'a alone. The one-point condition $\delta^T F_d(\delta) \geq c_{\min} \lVert\delta\rVert^2$ constrains $F_d$ at each point relative to the origin; the incremental condition constrains $F_d$ between any two points. A function can satisfy the one-point condition while violating the incremental condition (see Section 4 for examples).

Assuming DA2'a-inc and DA2'b-inc:

$$\lVert \Delta f \rVert_{H^TH}^2 \leq \lVert\Delta\delta\rVert^2 - 2\eta c_{\min}\lVert\Delta\delta\rVert^2 + \eta^2 c_{\max}^2 \lVert\Delta\delta\rVert^2$$

$$= (1 - 2\eta c_{\min} + \eta^2 c_{\max}^2)\lVert\Delta\delta\rVert^2 = \lambda_{\text{eff}}^2 \lVert\Delta\delta\rVert^2$$

Since $\lVert\Delta\delta\rVert^2 = \lVert H(X'-X)\rVert^2 = \lVert X - X'\rVert_{H^TH}^2$:

$$\lVert f_c(X,o) - f_c(X',o) \rVert_{H^TH} \leq \lambda_{\text{eff}} \lVert X - X' \rVert_{H^TH}$$

$\square$

### 3.6 When $H$ is invertible: Euclidean-norm contraction

If $H$ is square and invertible (fully observable system), the $H^TH$-norm is equivalent to the Euclidean norm:

$$\frac{1}{\kappa(H)} \lVert v \rVert \leq \lVert v \rVert_{H^TH}^{1/2} / \lVert H \rVert \leq \lVert v \rVert$$

where $\kappa(H) = \lVert H \rVert \cdot \lVert H^{-1} \rVert$ is the condition number.

**Corollary.** Under the conditions of Theorem 2, if $H$ is invertible with condition number $\kappa(H)$, then:

$$\lVert f_c(X,o) - f_c(X',o) \rVert \leq \kappa(H)^2 \cdot \lambda_{\text{eff}} \lVert X - X' \rVert$$

The Euclidean-norm contraction factor is $\kappa(H)^2 \cdot \lambda_{\text{eff}}$. This is $< 1$ only when $\lambda_{\text{eff}} < 1/\kappa(H)^2$ — a much more restrictive condition for ill-conditioned $H$. For well-conditioned observation models ($\kappa(H) \approx 1$), the Euclidean contraction factor is close to $\lambda_{\text{eff}}$.

For $H = I$ (direct observation): $\kappa(H) = 1$, and the Euclidean contraction is exactly $\lambda_{\text{eff}}$, matching the Kalman scalar case.

### 3.7 Summary of Theorem 2

The full update map is a contraction (in the $H^TH$-norm) under three conditions:

| Condition | What it requires | Status |
|---|---|---|
| C1: Sector-Lipschitz on $F_d$ (incremental) | $F_d$ is strongly monotone and Lipschitz | **Stronger than (A4)** — requires incremental monotonicity, not just one-point sector bound |
| C2: Linear prediction | $\hat{o}(X) = HX$ | Satisfied for Kalman, exponential family natural parameter models; fails for nonlinear observation models |
| C3: Bounded gain | $\eta < 2c_{\min}/c_{\max}^2$ | Same as DA2' step-size condition |

---

## 4. Characterizing the Boundary

### 4.1 When does the incremental sector bound (DA2'a-inc) hold?

The incremental sector bound — strong monotonicity of $F_d$ — is the critical additional assumption. Let us characterize when it holds.

**Proposition 3 (Sufficient conditions for DA2'a-inc).**

**(a) Linear correction:** $F_d(\delta) = A\delta$ with $A$ positive definite. Then DA2'a-inc holds with $c_{\min} = \lambda_{\min}(A_{\text{sym}})$ where $A_{\text{sym}} = (A + A^T)/2$. This covers: scalar Kalman ($A = 1$), matrix Kalman ($A = KH$ restricted to observable subspace), Beta-Bernoulli on $[0,1]$ (linearized near the truth).

**(b) Gradient of strongly convex function:** $F_d(\delta) = \nabla L(\delta)$ where $L$ is $\mu$-strongly convex on $\mathcal{B}_R$. Then by the standard characterization of strong convexity:

$$\langle \nabla L(\delta) - \nabla L(\delta'), \delta - \delta' \rangle \geq \mu \lVert \delta - \delta' \rVert^2$$

DA2'a-inc holds with $c_{\min} = \mu$. This covers: gradient descent on quadratic or log-concave losses, natural gradient in exponential families (where the loss in natural parameters is convex).

**(c) Monotone operator plus strongly monotone perturbation:** $F_d = F_1 + F_2$ where $F_1$ is monotone ($\langle \delta - \delta', F_1(\delta) - F_1(\delta') \rangle \geq 0$) and $F_2$ is strongly monotone with constant $c_{\min}$. Then DA2'a-inc holds with constant $c_{\min}$. This allows decomposing the correction into a "base monotone" part and a "coercive" part.

**Proposition 4 (When DA2'a-inc can fail despite DA2'a holding).**

Consider a scalar correction function $F_d: \mathbb{R} \to \mathbb{R}$ satisfying the one-point sector bound $\delta \cdot F_d(\delta) \geq c_{\min} |\delta|^2$ for all $|\delta| \leq R$. The incremental condition requires:

$$(\delta - \delta')(F_d(\delta) - F_d(\delta')) \geq c_{\min}(\delta - \delta')^2$$

In one dimension, this is equivalent to $F_d'(\delta) \geq c_{\min}$ for all $|\delta| \leq R$ (i.e., $F_d$ is uniformly strongly increasing).

**Counterexample.** Let $F_d(\delta) = c_{\min}\delta + A\sin(\omega\delta)$ for $A > 0$, $\omega > 0$. The one-point sector bound: $\delta F_d(\delta) = c_{\min}\delta^2 + A\delta\sin(\omega\delta) \geq c_{\min}\delta^2 - A|\delta|^2$ (using $|\sin(x)| \leq |x|$, approximately for small $\omega$). More precisely, using $|\delta\sin(\omega\delta)| \leq |\delta|^2 \omega$ for $|\omega\delta| \leq \pi$ (from $|\sin(x)| \leq |x|$):

Actually, let us construct the counterexample more carefully.

**Counterexample (revised).** Define $F_d(\delta) = 2\delta + 3\sin(\delta)$ on $\mathbb{R}$. Check the one-point sector bound: $\delta F_d(\delta) = 2\delta^2 + 3\delta\sin(\delta) \geq 2\delta^2 - 3|\delta\sin(\delta)| \geq 2\delta^2 - 3\delta^2 = -\delta^2$. This is not helpful. We need $\delta \sin(\delta) \geq 0$, which is true for $|\delta| \leq \pi$ (since $\sin(\delta)$ and $\delta$ have the same sign). So for $|\delta| \leq \pi$:

$$\delta F_d(\delta) = 2\delta^2 + 3\delta\sin\delta \geq 2\delta^2$$

The one-point sector bound holds with $c_{\min} = 2$.

But $F_d'(\delta) = 2 + 3\cos(\delta)$, which equals $-1$ at $\delta = \pi$. The incremental condition fails: at $\delta = \pi$, the derivative is negative, so for $\delta$ near $\pi$ and $\delta'$ slightly larger, $F_d(\delta) > F_d(\delta')$ while $\delta < \delta'$, violating monotonicity.

**More precisely:** At $\delta = \pi$, $F_d'(\pi) = 2 + 3\cos(\pi) = 2 - 3 = -1 < 0$. There exist $\delta_1 < \delta_2$ near $\pi$ with $F_d(\delta_1) > F_d(\delta_2)$, so $(\delta_1 - \delta_2)(F_d(\delta_1) - F_d(\delta_2)) < 0$, violating the incremental sector bound with any $c_{\min} > 0$.

Yet the one-point bound holds with $c_{\min} = 2$ on $[0, \pi]$ (and by odd symmetry, with $c_{\min} = 2$ on $[-\pi, \pi]$, since $\delta\sin\delta \geq 0$ on this interval).

**Conclusion.** The one-point sector bound does NOT imply the incremental sector bound. Functions with oscillatory corrections can satisfy DA2'a (corrections are globally inward-pointing with sufficient margin) while violating DA2'a-inc (locally the correction can decrease as mismatch increases).

**Physical interpretation.** The one-point sector bound says "each correction pushes toward the origin." The incremental bound says "larger mismatches always get larger corrections." An oscillatory correction function can push toward the origin at every point while having local regions where the correction magnitude decreases — it "wobbles" while maintaining overall inward direction.

### 4.2 Which AAD agent classes satisfy DA2'a-inc?

| Agent class | DA2'a-inc status | Reason |
|---|---|---|
| Scalar Kalman | Holds (trivially) | $F_d(\delta) = \delta$, linear |
| Matrix Kalman | Holds | $F_d(\delta) = KH\delta$, linear with $KH$ positive definite on observable subspace |
| Beta-Bernoulli | Holds locally | $F_d(p, \delta) = \delta/(n+1)$, linear in $\delta$ at each $n$ |
| Exponential family (natural params) | Holds | $F_d = \nabla A(\theta) - \bar{x}$, gradient of convex $A$ is monotone; strongly monotone when Fisher information has bounded eigenvalues |
| Gradient descent, strongly convex loss | Holds | By definition of strong convexity |
| Gradient descent, locally convex loss | Holds locally | In the convexity basin; fails at inflection points |
| Gradient descent, non-convex loss | **Fails** | Non-monotone gradient at saddle points and between local minima |
| PID controller | **Fails in general** | Integral term can create oscillatory corrections that violate incremental monotonicity |
| Rule-based / threshold agents | **Fails** | Discontinuous corrections violate incremental sector bound at thresholds |

**Key finding: DA2'a-inc holds for all Bayesian-update agents (where it follows from convexity of the log-partition function or from conjugate-prior structure) and for gradient agents on convex losses. It fails for non-convex optimization agents and for agents with discontinuous or oscillatory correction rules.**

### 4.3 The nonlinear prediction case (C2 violation)

When the prediction function is nonlinear ($\hat{o}(X)$ is not $HX$), the mismatch difference $\delta - \delta' = \hat{o}(X') - \hat{o}(X)$ is no longer a linear function of $X - X'$. The proof of Theorem 2 breaks at the step where we identify $\lVert\Delta\delta\rVert$ with $\lVert X - X'\rVert_{H^TH}$.

**Proposition 5 (Contraction with nonlinear prediction, local version).** If $\hat{o}$ is $C^1$ and the Jacobian $D\hat{o}(X)$ has bounded condition number $\kappa_h$ uniformly on $\mathcal{B}_R$, then locally:

$$\lVert f_c(X, o) - f_c(X', o) \rVert \leq (1 - \eta c_{\min}/\kappa_h^2 + \eta^2 c_{\max}^2 \kappa_h^2) \lVert X - X' \rVert + O(\lVert X - X' \rVert^2)$$

The contraction factor becomes approximately $\lambda_{\text{eff}}' = 1 - \eta c_{\min}/\kappa_h^2 + \eta^2 c_{\max}^2 \kappa_h^2$, which is $< 1$ when:

$$\eta < \frac{2c_{\min}}{\kappa_h^4 c_{\max}^2}$$

This is a much tighter step-size restriction than the linear case (extra factor of $\kappa_h^4$). For mildly nonlinear predictions ($\kappa_h \approx 1$), the restriction is similar. For strongly nonlinear predictions, the contraction may fail at practically achievable step sizes.

*Epistemic status: sketch. The $O(\lVert X - X'\rVert^2)$ remainder requires Lipschitz bounds on the second derivative of $\hat{o}$, which are domain-specific. The local-to-global extension requires the Jacobian condition to hold throughout the trajectory, not just at each point.*

---

## 5. The Discrete-Time Connection

### 5.1 Using $\lambda_{\text{eff}}$ from #discrete-sector-condition

The discrete-sector-condition segment defines:

$$\lambda_{\text{eff}}^2 = 1 - 2\eta^\ast c_{\min} + (\eta^\ast)^2 c_{\max}^2$$

for the mismatch dynamics $\delta_{k+1} = \delta_k - \eta^\ast F_d(\delta_k) + w_k$. This $\lambda_{\text{eff}}$ is the contraction factor for the *mismatch* — it bounds how fast $\lVert\delta_k\rVert$ shrinks.

**The bridge question:** Does the mismatch contraction factor bound the *full update map* contraction factor?

**Answer: Yes, when C1-C3 hold (Theorem 2).** The proof of Theorem 2 shows that the full update map's contraction factor (in the $H^TH$-norm) is exactly $\lambda_{\text{eff}}$ from the discrete sector condition. The contraction of the full map IS the contraction of the mismatch dynamics, viewed through the lens of the observation operator $H$.

This is not a coincidence — it reflects the structural identity noted in #composition-closure's Discussion: "The trajectory error $e_t$ evolves under the same dynamics as mismatch $\delta_t$." When the update is purely mismatch-driven and the prediction is linear, the trajectory error IS a mismatch — the error $e_t$ generates a "virtual mismatch" $He_t$ that is contracted by the same mechanism that contracts actual mismatch.

### 5.2 The discrete bridge lemma with explicit contraction

Combining Theorem 2 with the bridge lemma from #composition-closure:

*[Derived (Conditional on C1-C3)]*

**Theorem 3 (Bridge Lemma with Verified Contraction).** Let the macro-dynamics satisfy (A1)-(A4) with C1-C3 holding (mismatch-driven update, incremental sector-Lipschitz correction, linear prediction, bounded gain). Let the projection $\Lambda$ be $L$-Lipschitz (P2). Then the trajectory error satisfies:

$$\lVert e_t \rVert \leq \frac{\kappa(H)^2 \cdot \varepsilon_x}{1 - \lambda_{\text{eff}}} \cdot (1 - \lambda_{\text{eff}}^t)$$

and in steady state:

$$\limsup_{t \to \infty} \lVert e_t \rVert \leq \frac{\kappa(H)^2 \cdot \varepsilon_x}{1 - \lambda_{\text{eff}}}$$

The meaningful composition condition becomes:

$$\varepsilon_x < \frac{(1 - \lambda_{\text{eff}}) R_c}{\kappa(H)^2}$$

When $H = I$ (direct observation), $\kappa(H) = 1$ and the bound recovers the original bridge lemma exactly: $\limsup \lVert e_t \rVert \leq \varepsilon_x / (1 - \lambda_{\text{eff}}) = \varepsilon_x \nu_c / \alpha_c$ (using $1 - \lambda_{\text{eff}} \approx \eta^\ast c_{\min} = \alpha_c / \nu_c$ in the fluid limit).

**Proof.** Combine the contraction bound from Theorem 2 (in Euclidean norm via the condition number) with the standard linear recurrence argument from #composition-closure. The per-step evolution:

$$\lVert e_{t+1} \rVert \leq \kappa(H)^2 \lambda_{\text{eff}} \lVert e_t \rVert + \varepsilon_x$$

Since $\kappa(H)^2 \lambda_{\text{eff}} < 1$ by the contraction condition, the geometric series converges. $\square$

### 5.3 Stochastic version

For stochastic closure errors (when $\varepsilon_{x,t}$ varies with the observation realization), the bridge lemma gives:

$$\mathbb{E}[\lVert e_t \rVert^2] \leq \frac{\kappa(H)^4 \cdot \mathbb{E}[\varepsilon_{x,t}^2]}{1 - \kappa(H)^4 \lambda_{\text{eff}}^2}$$

by the same argument as Prop DA.1S (the squared contraction factor applies to the second moment, and the stochastic closure errors play the role of i.i.d. disturbances).

---

## 6. Agent Classes: The Full Characterization

### 6.1 Three tiers of contraction guarantee

The analysis yields a three-tier characterization of when the bridge lemma's contraction assumption is justified:

**Tier 1: Contraction is PROVED (from sector condition + structure).**

These agents satisfy C1-C3 and the contraction property follows from Theorem 2:

- Kalman filters (scalar and matrix, at steady state)
- Exponential-family Bayesian updaters with conjugate priors
- Gradient descent on strongly convex losses with linear observation models
- Any linear correction function with positive definite gain-observation product

For these agents, the bridge lemma is exact. The contraction factor $\lambda_{\text{eff}}$ from #discrete-sector-condition bounds the full update map. **The bridge lemma can be promoted from "conditional" to "derived (conditional on sector-Lipschitz DA2')" for this class.**

**Tier 2: Contraction holds LOCALLY (additional conditions checkable per domain).**

These agents satisfy C1 and C3 but violate C2 (nonlinear prediction):

- Extended Kalman filters (linearized prediction)
- Bayesian updaters with non-conjugate likelihoods
- Gradient descent on locally convex losses with nonlinear observation models
- Particle filters in low-variance regimes

For these agents, contraction holds in a neighborhood of the current state with a degraded factor $\lambda_{\text{eff}}' \approx \kappa_h^2 \lambda_{\text{eff}}$ (Proposition 5). The bridge lemma holds locally with a tighter meaningful-composition condition. **The contraction is checkable per domain via the condition number $\kappa_h$ of the prediction Jacobian.**

**Tier 3: Contraction REQUIRES INDEPENDENT VERIFICATION.**

These agents violate one or more of C1-C3:

- Agents with non-monotone corrections (non-convex optimization, oscillatory rules)
- Agents with discontinuous correction functions (threshold-based, rule-based)
- Agents whose update includes state-dependent terms not mediated by mismatch
- Agents undergoing structural adaptation (where the correction function itself changes)

For these agents, the sector condition alone does not imply contraction of the full update map. **The contraction property must be verified independently for each domain, or the bridge lemma must be used with the contraction as an explicit additional assumption.**

### 6.2 Summary table

| Agent class | Tier | Contraction factor | Additional conditions | Norm |
|---|---|---|---|---|
| Scalar Kalman | 1 | $1 - K^\ast$ | None | Euclidean |
| Matrix Kalman | 1 | $\rho(I - K^\ast H)$ | None | $H^TH$ (or Euclidean with $\kappa(H)^2$ factor) |
| Beta-Bernoulli edge | 1 | $1 - 1/(n+1)$ | None | Euclidean |
| Exp. family (nat. params) | 1 | $1 - \eta \lambda_{\min}(\text{Fisher})$ | Fisher info bounded | Natural metric |
| Gradient, strongly convex | 1 | $1 - \eta\mu + \eta^2 L^2$ | None | Euclidean |
| Extended Kalman | 2 | $\sim \kappa_h^2 \lambda_{\text{eff}}$ | $\kappa_h$ bounded | Euclidean (local) |
| Gradient, locally convex | 2 | $\sim \lambda_{\text{eff}}$ in basin | Basin containment | Euclidean (local) |
| Non-convex optimization | 3 | Not guaranteed | Independent verification | Domain-specific |
| Rule-based | 3 | Not guaranteed | Independent verification | Domain-specific |

---

## 7. What This Establishes (and What Remains)

### 7.1 The gap is now characterized

The bridge lemma's contraction assumption decomposes into three checkable conditions:

1. **Incremental sector-Lipschitz (C1):** $F_d$ is strongly monotone and Lipschitz. This is the strengthening of (A4) needed for the bridge lemma. It is automatically satisfied for Bayesian updaters and gradient descent on convex losses. It is the first-class additional assumption that must be stated.

2. **Linear prediction (C2):** The prediction model $\hat{o}(X)$ is linear. This holds for the standard observation models in estimation theory. For nonlinear models, the contraction degrades by the condition number of the prediction Jacobian.

3. **Bounded gain (C3):** Same as the existing DA2' step-size condition. Not new.

**The genuine gap is C1 (incremental monotonicity).** C2 and C3 are either already assumed or checkable. The incremental sector bound is the structural condition that separates "sector-bounded correction" from "contracting update map."

### 7.2 Recommendation for #composition-closure

The bridge lemma should be restated with the condition hierarchy:

*[Formulation (revised bridge lemma conditions)]*

**For Tier 1 agents** (linear prediction, incremental sector-Lipschitz correction): the bridge lemma is derived from (A4) + C1 + C2. The contraction factor equals $\lambda_{\text{eff}}$ from #discrete-sector-condition. No independent contraction assumption needed.

**For Tier 2 agents** (nonlinear prediction, incremental sector-Lipschitz correction): the bridge lemma holds locally, with contraction factor degraded by $\kappa(D\hat{o})^2$. The meaningful-composition condition is tighter.

**For Tier 3 agents**: the contraction is an independent assumption (as currently stated). The bridge lemma is conditional on per-domain verification.

### 7.3 The incremental sector condition as the right formulation

The key theoretical contribution of this spike is identifying **incremental monotonicity (strong monotonicity) of the correction function** as the precise condition bridging sector-bounded correction to update-map contraction.

This is a well-studied property in optimization and monotone operator theory. Strong monotonicity of the gradient is equivalent to strong convexity of the objective. The AAD connection: *an agent whose correction function is strongly monotone has the property that perturbations to its state are always reduced by the correction mechanism* — not just perturbations from the origin (the one-point sector bound), but perturbations between any two states.

For the working notes in #composition-closure, the characterization is:

> The contraction assumption holds when the correction function $F_d$ is strongly monotone (incremental sector bound, DA2'a-inc). This is satisfied by: (i) all linear corrections with positive definite gain-observation product, (ii) all Bayesian updates on exponential-family models, (iii) all gradient updates on strongly convex losses. It fails for non-convex optimization and discontinuous correction rules. When the prediction model is additionally linear, the full update map is a contraction with the same factor $\lambda_{\text{eff}}$ as the mismatch dynamics. When the prediction model is nonlinear, the contraction factor degrades by the condition number of the prediction Jacobian squared.

### 7.4 What remains open

1. **Global (non-local) contraction for nonlinear prediction models.** Proposition 5 is local. A global result would require uniform bounds on the prediction Jacobian's condition number over the entire operating region — available for specific systems but not in general.

2. **Mixed-type composite agents.** When the epistemic substate ($M_c$) is Tier 1 (Kalman) but the purposeful substate ($G_c$) is Tier 2 or 3, the composite contraction factor depends on the coupling between $M$ and $G$ updates. The directed-separation assumption (#directed-separation) simplifies this by decoupling the substates, but Section III composites may violate directed separation (#directed-separation-under-composition).

3. **The Beta-Bernoulli edge update's incremental sector bound.** The update $p \mapsto p + (x - p)/(n+1)$ is linear in $p$ for fixed $n$, so DA2'a-inc holds at each step. But $n$ increases over time, changing $c_{\min} = 1/(n+1)$ — the incremental sector constant is time-varying and converges to zero. The bridge lemma for agents with decaying gain requires time-varying contraction analysis (noted in #discrete-sector-condition Working Notes).

4. **Connection to incremental input-to-state stability (iISS).** The contraction property (CP) is closely related to the concept of *incremental input-to-state stability* in nonlinear systems theory (Angeli 2002). An iISS system has the property that the distance between any two trajectories is bounded by a function of the distance between the corresponding inputs. Theorem 2 proves incremental stability for the class of mismatch-driven agents with monotone corrections and linear predictions. The full iISS theory may provide tools for extending to the nonlinear-prediction case.

---

## 8. Assessment

**What's new.** The decomposition of the contraction assumption into checkable conditions (C1-C3) is new. The identification of the incremental sector bound (strong monotonicity) as the precise gap-closing condition is new. The three-tier classification of agent classes is new. The counterexample (Section 4.1) showing that the one-point sector bound does not imply the incremental bound is new (though the mathematical fact is well-known in monotone operator theory).

**What's proved.** Theorem 2 (contraction for Tier 1 agents) is proved. The bridge lemma is fully derived for Tier 1 agents, conditional only on the sector-Lipschitz condition DA2' in its incremental form. Theorem 3 restates the bridge lemma with explicit conditions.

**What's sketched.** Proposition 5 (local contraction for Tier 2 agents) is a sketch — the remainder term needs formalization. The stochastic version (Section 5.3) is stated without detailed proof (but follows the same pattern as DA.1S).

**What remains open.** Tier 3 agents, time-varying contraction factors, and the global nonlinear case.

**Confidence.** Theorems 2 and 3 are correct and the proofs are complete (conditional on C1-C3). The three-tier classification is well-grounded. The counterexample is valid. The main uncertainty is whether the Tier 2 local result can be made global under reasonable additional conditions.

**Recommendation.** This spike provides enough to:
1. Restate the bridge lemma in #composition-closure with explicit conditions rather than a blanket "contraction assumption."
2. Promote the bridge lemma to "derived (conditional on DA2'-inc + C2)" for Tier 1 agents.
3. Close the open item in #composition-closure's Working Notes about "proving it from (A4) alone" with the answer: "It cannot be proved from (A4) alone. The incremental sector bound DA2'a-inc is the minimal additional condition. It holds for all Bayesian and convex-gradient agents."
