# Spike: Mori-Zwanzig Memory Kernel and the Composition Closure Defect

**Status**: Speculation / partial derivation -- the upper-bound direction goes through under stated assumptions; the named target (lower bound $\varepsilon^\ast \geq C \cdot \lVert K \rVert_{\text{norm}}$) does **not** close under the current AAD formulation without additional structural hypotheses.
**Date**: 2026-04-20
**Motivation**: The composition-closure segment ( #form-composition-closure, Working Notes) identifies an unworked connection: "The closure defect should relate to the MZ memory kernel -- when correlations between projected and discarded variables decay fast, $\varepsilon^\ast$ is small. A rigorous lower bound $\varepsilon^\ast \geq f(\text{memory kernel norm})$ would anchor AAD's composition framework in established dynamical-systems theory. Plausible but unworked." This spike attempts that derivation, documents where it closes, and flags where it does not.

**Depends on**: #form-composition-closure, #scope-multi-agent, #deriv-sector-condition, #deriv-discrete-sector-condition, `spikes/spike-composition-correlated-kalman.md`, `spikes/spike-bridge-lemma-contraction.md`, `spikes/spike-projection-admissibility.md`

---

## 1. Framing and the Target Hypothesis

### 1.1 What is being attempted

The Mori-Zwanzig (MZ) formalism (Mori 1965, Zwanzig 1961, 1973; discrete-time formulations in Chorin-Hald 2007) decomposes the dynamics of a *projected* observable into three exactly-separable parts:

$$\frac{d}{dt}(P A)(t) = \underbrace{P L P A(t)}_{\text{Markov term}} \;+\; \underbrace{\int_0^t K(t-s)\, P A(s)\, ds}_{\text{memory term}} \;+\; \underbrace{F(t)}_{\text{orthogonal noise}}$$

where $L$ is the Liouvillian (generator of the full dynamics), $P$ is an orthogonal projection on a Hilbert space of observables, $Q = I - P$, and the memory kernel is:

$$K(s) = P L \, e^{s Q L} \, Q L P$$

The noise $F(t) = e^{t Q L} Q L P A(0)$ lives in the range of $Q$ (orthogonal to $P$'s range).

**Target hypothesis (from #form-composition-closure Working Notes):** There exists a constant $C$ depending on $\alpha_c, \nu_c$ such that

$$\varepsilon^\ast \;\geq\; C \cdot \lVert K \rVert_{\text{norm}}$$

for an appropriate norm on the memory kernel $K$. Slow-decaying kernel $\Rightarrow$ irreducibly large $\varepsilon^\ast$; fast-decaying kernel $\Rightarrow$ small $\varepsilon^\ast$ achievable.

### 1.2 What would make this a real result

A genuine lower bound of this form has three ingredients:

1. **A functional-analytic setting** where both $\varepsilon^\ast$ and $\lVert K \rVert$ are well-defined -- a Hilbert space of observables with a measure under which MZ's projection is a genuine orthogonal projection.
2. **Compatibility between AAD's state-space projection $\Lambda$ and MZ's Hilbert-space projection $P$** -- these are different objects and the relationship is non-trivial.
3. **A lower-bound argument**: closure defect from AAD's infimum $\geq$ some computable function of $K$. The direction matters: upper bounds ($\varepsilon^\ast \leq \ldots$) are relatively accessible; lower bounds require an obstruction theorem.

This spike makes ingredients (1) and (2) precise, derives the upper-bound direction cleanly, and identifies the specific obstacle to the lower bound.

---

## 2. Functional-Analytic Setting

### 2.1 The observable Hilbert space

*[Formulation]*

Let $\pi$ be a probability measure on $\mathcal X_{\text{micro}}$ that is stationary (or quasi-stationary) under the micro-dynamics -- for Kalman-type agents, $\pi$ is the steady-state joint distribution of $(X_{\text{micro}}, o_{\text{micro}})$. For event-driven AAD agents ( #form-event-driven-dynamics), $\pi$ exists when the process is ergodic; stationarity is an additional assumption that holds in the regime the sector condition is most often invoked (bounded mismatch, persistent disturbance).

Define the Hilbert space

$$\mathcal H = L^2(\mathcal X_{\text{micro}}, \pi)$$

with inner product $\langle \phi, \psi \rangle = \mathbb E_\pi[\phi(X) \psi(X)]$ and norm $\lVert \phi \rVert_\pi = \sqrt{\mathbb E_\pi[\phi^2]}$.

**Koopman operator.** The micro-dynamics induce a shift operator $U: \mathcal H \to \mathcal H$ by:

$$(U \phi)(X_{\text{micro},t}) = \phi(f_{\text{micro}}(X_{\text{micro},t}, o_{\text{micro},t+1}))$$

Under stationarity, $U$ is well-defined as a bounded operator. Its adjoint is the Perron-Frobenius operator. (For stochastic dynamics $U \phi = \mathbb E[\phi(X_{t+1}) \mid X_t = \cdot]$ -- the conditional expectation operator of the Markov kernel. The discrete-time MZ formalism works with $U$ directly rather than its infinitesimal generator.)

*Epistemic status of this step.* The construction is standard for ergodic Markov systems. The load-bearing assumption is that the full micro-chain $(X_{\text{micro},t}, o_{\text{micro},t})_{t \geq 0}$ admits a stationary (or quasi-stationary) measure under coupled dynamics. For two interacting Kalman filters on a stationary correlated random-walk *environment* this is not literally true (the random-walk environment does not have a stationary measure), but the *innovation process* and *estimator state relative to truth* do. The spike-composition-correlated-kalman derivation operates implicitly in this stationary innovation frame. For purposeful agents whose strategy state $\Sigma_t$ is non-stationary (Beta-Bernoulli with diverging $n$, as in §12 of that spike), the Hilbert-space setting fails -- there is no stationary measure to define $\mathcal H$. This is the first real obstruction.

### 2.2 Projection induced by $\Lambda$

AAD's $\Lambda_x$ is a state-space map, not a Hilbert-space operator. To connect to MZ, lift $\Lambda$ to observables.

*[Definition (induced-projection)]*

Let $\sigma(\Lambda)$ be the sub-$\sigma$-algebra of micro-events generated by $\Lambda_x$, i.e., the events that can be distinguished using only the macro-state. Define:

$$P_\Lambda : \mathcal H \to \mathcal H, \qquad P_\Lambda \phi = \mathbb E_\pi[\phi \mid \sigma(\Lambda)]$$

This is the standard orthogonal projection onto the closed subspace $\mathcal H_\Lambda \subset \mathcal H$ of $\sigma(\Lambda)$-measurable $L^2$ functions.

**Key properties:**

- $P_\Lambda$ is a genuine orthogonal projection in $\mathcal H$: $P_\Lambda^2 = P_\Lambda$, $P_\Lambda^\ast = P_\Lambda$.
- $P_\Lambda \phi = \phi$ iff $\phi$ factors through $\Lambda_x$: $\phi(X) = \tilde\phi(\Lambda_x(X))$ for some $\tilde\phi: \mathcal X_c \to \mathbb R$.
- The range $\mathcal H_\Lambda$ is canonically isometric to $L^2(\mathcal X_c, \Lambda_{\ast} \pi)$ where $\Lambda_\ast \pi$ is the pushforward measure.
- $Q_\Lambda = I - P_\Lambda$ projects onto the orthogonal complement -- functions whose conditional expectation given the macro-state is zero.

**Interpretation.** $P_\Lambda \phi$ is the best $\sigma(\Lambda)$-measurable approximation of $\phi$. For $\phi(X) = X$ (the identity observable, in coordinate form), $P_\Lambda \phi(X) = \mathbb E[X \mid \Lambda_x(X)]$ -- the conditional mean of the micro-state given the macro-state. This is NOT the same as $\Lambda_x(X)$ itself except when $\Lambda_x$ is an orthogonal projection with respect to $\pi$.

### 2.3 Compatibility question: does $P_\Lambda$ act like $\Lambda$?

*[Discussion]*

Consider the scalar observable $\phi_i(X_{\text{micro}}) = (\Lambda_x(X_{\text{micro}}))_i$ -- the $i$-th coordinate of the macro-state viewed as a micro-observable. By construction $P_\Lambda \phi_i = \phi_i$ (it's already $\sigma(\Lambda)$-measurable).

Now the question: is $\Lambda_x(f_{\text{micro}}(X)) - f_c(\Lambda_x(X))$ (the AAD per-step closure error) equal to $(U - P_\Lambda U P_\Lambda) \phi(X)$ for some natural choice of $\phi$?

Compute, for $\phi = \phi_i$ (coordinate observable):

$$(U \phi_i)(X) = \phi_i(f_{\text{micro}}(X, o_{t+1})) = (\Lambda_x \circ f_{\text{micro}})(X)_i$$

Now $(P_\Lambda U \phi_i)$ is the conditional expectation of $(\Lambda_x \circ f_{\text{micro}})(X)_i$ given $\Lambda_x(X)$. This is the **MZ-optimal macro-dynamics** -- the best Markovian macro-update in the $L^2$ sense:

$$f_c^\text{MZ}(X_c) := \mathbb E_\pi[\Lambda_x(f_{\text{micro}}(X_{\text{micro}})) \mid \Lambda_x(X_{\text{micro}}) = X_c]$$

This is the *mathematically optimal* Markovian macro-dynamics, ignoring the AAD admissibility constraints $\mathcal M_{\text{adm}}$.

**Claim (compatibility, stated with care).** Under the stationary-measure setting of §2.1 and for coordinate observables,

$$\Lambda_x(f_{\text{micro}}(X)) - f_c^\text{MZ}(\Lambda_x(X)) \;=\; (Q_\Lambda U \phi_\cdot)(X)$$

where the left side is the per-step error of the MZ-optimal macro-dynamics and the right side is the orthogonal component of $U \phi$. Hence

$$\mathbb E_\pi\big[\lVert \Lambda_x(f_{\text{micro}}(X)) - f_c^\text{MZ}(\Lambda_x(X)) \rVert^2\big] \;=\; \sum_i \lVert Q_\Lambda U \phi_i \rVert_\pi^2$$

*Epistemic status.* Derived, conditional on (i) stationarity of $\pi$, (ii) coordinate observables being the right choice (which requires the macro-state space $\mathcal X_c$ to be a Euclidean subspace that $\Lambda_x$ projects onto, not an arbitrary manifold), (iii) the L² norm matching AAD's norm choice $\lVert\cdot\rVert_{\mathcal X_c}$. For Kalman-type agents with the Mahalanobis norm (§193 of composition-closure, §5 of the Kalman spike), condition (iii) requires reweighting by the inverse-covariance -- the same covariance that defines $\pi$ at steady state, so this works.

---

## 3. What MZ Lets Us Say About $\varepsilon^\ast$

### 3.1 The clean upper-bound comparison

*[Derived (Conditional on §2.1-2.3 assumptions and linear macro-dynamics)]*

Consider a *restricted* infimum over the class of Markovian macro-dynamics without admissibility constraints:

$$\tilde\varepsilon := \inf_{g: \mathcal X_c \to \mathcal X_c} \mathbb E_\pi\big[\lVert \Lambda_x(f_{\text{micro}}(X)) - g(\Lambda_x(X)) \rVert^2\big]^{1/2}$$

The infimum is attained by $g = f_c^\text{MZ}$ (regression-to-the-mean is the $L^2$-optimal predictor). Therefore:

$$\tilde\varepsilon^2 = \sum_i \lVert Q_\Lambda U \phi_i \rVert_\pi^2$$

Now the AAD infimum is over $\mathcal M_{\text{adm}}$ (constrained class), not all functions. A smaller admissible class gives a *larger* infimum:

$$\varepsilon^\ast \;\geq\; \tilde\varepsilon \qquad \text{whenever } f_c^\text{MZ} \notin \mathcal M_{\text{adm}}$$

and $\varepsilon^\ast = \tilde\varepsilon$ when $f_c^\text{MZ} \in \mathcal M_{\text{adm}}$.

*This is the cleanest statement available.* It is not the target form $\varepsilon^\ast \geq C \cdot \lVert K \rVert_{\text{norm}}$ but it is rigorous within the stated setting.

### 3.2 Connecting $\tilde\varepsilon$ to the memory kernel

*[Derived (Conditional)]*

The discrete-time MZ decomposition (Chorin-Hald 2007, eq. 2.11) for the projected evolution is:

$$P_\Lambda U^{n+1} P_\Lambda = P_\Lambda U P_\Lambda \cdot P_\Lambda U^n P_\Lambda \;+\; \sum_{s=0}^{n-1} K_s \cdot P_\Lambda U^{n-1-s} P_\Lambda \;+\; (\text{orthogonal terms})$$

with discrete memory kernel

$$K_s = P_\Lambda U (Q_\Lambda U)^s Q_\Lambda U P_\Lambda$$

The "noise" term $F_n = (Q_\Lambda U)^n Q_\Lambda U P_\Lambda$ lives in $\text{Ran}(Q_\Lambda)$.

Note $K_0 = P_\Lambda U Q_\Lambda U P_\Lambda$. A standard identity (orthogonality of $P_\Lambda$ and $Q_\Lambda$) gives:

$$\lVert Q_\Lambda U P_\Lambda \phi \rVert_\pi^2 = \langle \phi, P_\Lambda U^\ast Q_\Lambda U P_\Lambda \phi \rangle$$

For coordinate observables $\phi_i$ (which already satisfy $P_\Lambda \phi_i = \phi_i$), this means:

$$\tilde\varepsilon^2 = \sum_i \lVert Q_\Lambda U \phi_i \rVert_\pi^2 = \sum_i \langle \phi_i,\, U^\ast Q_\Lambda U \phi_i \rangle$$

The operator $U^\ast Q_\Lambda U$ appearing here is closely related to the *generator* of the kernel sequence: $K_0$ in the self-adjoint case equals $P_\Lambda U^\ast Q_\Lambda U P_\Lambda$. So $\tilde\varepsilon^2 = \operatorname{tr}(K_0|_{\text{coordinate subspace}})$ when $U$ is self-adjoint (reversible dynamics).

**Partial result:**

$$\boxed{\varepsilon^\ast \;\geq\; \sqrt{\operatorname{tr}\big(K_0\!\restriction_{\text{coord}}\big)} \quad \text{(under §2 assumptions + reversibility + } f_c^\text{MZ} \notin \mathcal M_{\text{adm}})}$$

This identifies $\varepsilon^\ast$ with the *zeroth-order* memory kernel norm, not $\lVert K \rVert$ as a sum or supremum over lags.

*Epistemic status: Derived (conditional on stationarity, reversibility, coordinate observable compatibility, and $f_c^\text{MZ}$ being outside $\mathcal M_{\text{adm}}$).* The reversibility condition $U = U^\ast$ is strong and excludes most interesting AAD dynamics (Kalman filters are not reversible). For non-reversible $U$ the identification involves the *symmetric part* $(K_0 + K_0^\ast)/2$, not $K_0$ itself.

### 3.3 Why $\lVert K \rVert$ (the full kernel norm) does not appear

The target hypothesis is $\varepsilon^\ast \geq C \lVert K \rVert_{\text{norm}}$ where $\lVert K \rVert$ presumably means a time-summed or sup-norm over all kernel lags $K_s$ for $s \geq 0$. The derivation in §3.2 captures only $K_0$. The higher-lag kernels $K_s$ for $s \geq 1$ measure memory beyond the *single-step* Markovian residual -- they enter when one examines the *trajectory-accumulated* error, not the per-step closure error.

**The natural place for $\lVert K \rVert$ is in the bridge lemma, not the closure defect directly.** The bridge lemma converts per-step error $\varepsilon_x$ (one-step) into trajectory error $e_t$ (accumulated) via a contraction argument. The analogous MZ quantity is the accumulated effect of the memory over a trajectory, which involves the full kernel sequence. This is developed below (§4) and is where the MZ connection has the most natural AAD interpretation, at the cost of a bound on *trajectory* error rather than on $\varepsilon^\ast$ itself.

---

## 4. The Bridge Lemma Reinterpreted Through MZ

### 4.1 Trajectory error as memory accumulation

Recall the bridge lemma recurrence ( #form-composition-closure, eq. referenced in §143):

$$\lVert e_{t+1} \rVert \leq \lambda \lVert e_t \rVert + \varepsilon_x, \qquad \lambda = 1 - \alpha_c/\nu_c$$

If the *per-step* macro-approximation error is exactly the MZ residual (memory + noise terms), then trajectory error evolution is:

$$e_{t+1} = \lambda e_t + \underbrace{[\text{memory}]_{t+1} + [\text{noise}]_{t+1}}_{\text{per-step MZ residual}}$$

Unrolling:

$$e_T = \sum_{t=0}^{T-1} \lambda^{T-1-t} \big( [\text{memory}]_t + [\text{noise}]_t \big)$$

The memory term at step $t$ is the convolution $\sum_{s<t} K_s \phi(X_{t-s})$. Substituting into the trajectory sum and changing order of summation:

$$\lVert e_T \rVert_\pi \lesssim \underbrace{\sum_{s \geq 0} \frac{\lVert K_s \rVert_\pi}{1 - \lambda}}_{\text{memory contribution}} + \underbrace{\frac{\sigma_F}{\sqrt{1 - \lambda^2}}}_{\text{noise contribution}}$$

where $\sigma_F^2 = \mathbb E_\pi \lVert F \rVert^2$ is the per-step orthogonal noise variance.

*Epistemic status: Sketch.* The ordering and norm choices need care (is this an $L^2$ norm, an $L^\infty$ in time, a trajectory-averaged norm?) and the "$\lesssim$" hides constants. But the structural result is clean: **the trajectory error bound splits cleanly into a memory contribution scaling with $\sum_s \lVert K_s \rVert / (1-\lambda)$ and a noise contribution scaling with $\sigma_F / \sqrt{1 - \lambda^2}$.**

### 4.2 Where $\lVert K \rVert$ enters as a lower bound

*[Hypothesis]*

If the MZ-optimal macro-dynamics $f_c^\text{MZ}$ is in $\mathcal M_{\text{adm}}$, then using it gives $\varepsilon_x = \tilde\varepsilon = $ per-step MZ residual, and the trajectory error bound is:

$$\limsup_T \mathbb E_\pi \lVert e_T \rVert \;\geq\; \frac{1}{1 - \lambda} \sum_s \lVert K_s \rVert_{\text{op}} \;\cdot\; \lVert \phi \rVert_\pi \;-\; (\text{noise cancellation})$$

This would give the target form with $C = 1/(1 - \lambda) = \nu_c / \alpha_c$:

$$\lim_T \lVert e_T \rVert \;\geq\; \frac{\nu_c}{\alpha_c} \cdot \lVert K \rVert_{\ell^1}$$

**But this is the *trajectory* error, not the closure defect $\varepsilon^\ast$.** The closure defect is the per-step error, which lower-bounds only by $\lVert K_0 \rVert$ (§3.2), not by $\sum_s \lVert K_s \rVert$.

*Epistemic status: Hypothesis.* The argument requires noise and memory contributions not to cancel -- they do not cancel in general (they live in orthogonal subspaces) but lower-bounding a sum of norms by a single norm requires additional non-negativity structure.

### 4.3 Contraction assumption ↔ spectral gap of $Q U$

*[Discussion]*

The bridge lemma requires contraction factor $\lambda < 1$. In MZ language, this corresponds to the spectral properties of the *orthogonal-dynamics propagator* $Q_\Lambda U$. The kernel decays geometrically when $Q_\Lambda U$ has spectral radius $< 1$ on $\text{Ran}(Q_\Lambda)$:

$$\lVert K_s \rVert \lesssim \rho(Q_\Lambda U)^s$$

If $\rho(Q_\Lambda U) < 1$, the sum $\sum_s \lVert K_s \rVert < \infty$ and the memory contribution to the trajectory error is bounded. This is the MZ analog of "fast decay of correlations" or "spectral gap" (in the continuous-time Liouvillian setting).

**The connection to the bridge lemma's contraction assumption** ( #form-composition-closure, eq. 131, and `spikes/spike-bridge-lemma-contraction.md`): the contraction of $f_c$ in state space is *not* the same as the spectral gap of $Q U$ in observable space. The former controls how the macro-dynamics contract state differences; the latter controls how fast micro-correlations between projected and discarded variables decay. They are related but distinct:

- **$f_c$ contraction** is a property of the *macro*-dynamics chosen (A4 + strong monotonicity, per the bridge-lemma-contraction spike).
- **$Q U$ spectral gap** is a property of the *micro*-dynamics restricted to the orthogonal subspace -- it does not depend on the macro-dynamics choice, only on $\Lambda$ and $f_{\text{micro}}$.

For the correlated Kalman case (§7 of `spikes/spike-composition-correlated-kalman.md`), both are geometric: $f_c$ contracts with factor $1 - K^\ast$ (the sector condition), and $Q U$ contracts with factor $(1 - K^\ast)^2$ on the error cross-covariance (eq. for $C_e$ in §5 of that spike). The Kalman calculation recovers both ingredients in matching quantitative form -- this is why the MZ picture "works" for Kalman, numerically.

*Epistemic status: Discussion-grade correspondence.* The identification of $(1-K^\ast)^2$ with $\rho(Q U)$ is suggestive but not formally derived here. A full derivation would compute $Q_\Lambda U$ explicitly on the error-covariance subspace and compute its spectrum.

---

## 5. Where the Target Result Fails to Close

The honest account of why the target $\varepsilon^\ast \geq C \cdot \lVert K \rVert_{\text{norm}}$ does not close under the current formulation:

### 5.1 Obstruction 1: ε* is per-step, memory kernel is multi-lag

$\varepsilon^\ast$ as defined in #form-composition-closure (eq. 47) is a *per-step* (trajectory-averaged) norm error. The memory kernel $K$ is inherently a *lag-indexed sequence* $\{K_s\}_{s \geq 0}$. The per-step closure defect can at best be related to $K_0$, the zero-lag kernel. The sum or sup of $\lVert K_s \rVert$ over lags captures a trajectory-accumulation phenomenon. To get $\varepsilon^\ast \geq C \lVert K \rVert$ with $\lVert K \rVert$ including multi-lag structure, one would need to *redefine* $\varepsilon^\ast$ as a trajectory error (integrating over a horizon) rather than a per-step error. This is a formulation-level choice, not a derivation gap.

### 5.2 Obstruction 2: Admissibility class constraint gap

MZ's $P_\Lambda U P_\Lambda$ (the optimal Markovian approximation) is in general *not* an AAD agent in the sense of (A1)-(A4). It is the $L^2$-projected dynamics, which need not decompose as $X_c = (M_c, G_c)$ or satisfy a sector condition. Therefore:

$$\varepsilon^\ast_{\mathcal M_{\text{adm}}} \geq \tilde\varepsilon_{\text{Markov, unconstrained}}$$

with equality only when $P_\Lambda U P_\Lambda$ happens to be in $\mathcal M_{\text{adm}}$. For the Kalman case, the means-only projection's induced MZ-optimal update is the steady-state Kalman update $(1 - K^\ast)X_c + K^\ast o$, which *is* AAD-admissible -- equality holds. In general, the gap

$$\varepsilon^\ast - \tilde\varepsilon = \text{admissibility price}$$

is domain-dependent and has no clean MZ interpretation.

### 5.3 Obstruction 3: Stationarity failure for purposeful agents

The Hilbert-space setup in §2.1 requires a stationary measure. For purposeful agents whose strategy confidences $p_i$ follow Beta-Bernoulli updates with diverging sample count $n_i$ (§12 of the Kalman spike), there is no stationary measure on the full micro-state. The MZ formalism does not directly apply. One could work in the "innovation frame" (where mismatch signals are stationary even when the underlying state is not), but the projection $\Lambda$ acts on the non-stationary state space, not the innovation process. Bridging these is an additional technical step not attempted here.

**This is the same obstruction identified in the Kalman spike (§13, Source 2) as "divergent auxiliary state" -- the case where $\varepsilon^\ast > 0$ genuinely -- is exactly the case where the MZ formalism doesn't directly apply.** Bitter: the most interesting cases are the ones where the tool is weakest.

### 5.4 Obstruction 4: Norm compatibility

AAD uses the Mahalanobis norm for estimation-type agents ( #form-composition-closure, §193) and leaves the norm open for other domains. MZ's natural norm is $L^2(\pi)$. For the Kalman case these align (the inverse steady-state covariance is the Mahalanobis weight and coincides with the weighting induced by $\pi$). For non-Gaussian agents or discrete state spaces, the compatibility is not automatic.

### 5.5 What *would* close the target

A rigorous $\varepsilon^\ast \geq C \cdot \lVert K \rVert_{\ell^1}$ would require:

1. **Redefining $\varepsilon^\ast$ as a trajectory error** (or defining a distinct trajectory-error quantity $\varepsilon^\ast_{\text{traj}}$), accepting that the per-step version doesn't capture multi-lag memory.
2. **Adding a stationarity assumption** to $\mathcal P_{\text{adm}}$ or $\mathcal M_{\text{adm}}$, restricting the composition framework to agents with (quasi-)stationary joint measures.
3. **Proving that $P_\Lambda U P_\Lambda \in \mathcal M_{\text{adm}}$** for the class of admissible projections considered -- i.e., that the MZ-optimal Markovian reduction is AAD-shaped. This is a non-trivial result: it would say the $L^2$-optimal macro-dynamics inherits the decomposition $(M_c, G_c)$ and the sector condition from the micro-dynamics.
4. **Isolating the memory-contribution mode** that lower-bounds the trajectory error. Noise and memory contributions are orthogonal in observable space but both contribute non-negatively to the trajectory-error norm, so lower bounds on a sum $\lVert K \rVert + \sigma_F$ translate to lower bounds on the trajectory error with an appropriate non-cancellation condition.

Each of these is a real piece of work.

---

## 6. Two-Kalman Sanity Check

### 6.1 Applying the framework to the Kalman spike

Specializing to the correlated Kalman setup of `spikes/spike-composition-correlated-kalman.md` (two scalar Kalman filters, correlation $\rho$, means-only projection):

- **Stationary measure $\pi$**: The innovation process $(\delta_{1,t}, \delta_{2,t})$ is stationary at steady state with joint covariance $\Sigma_\delta$ (§5 of the Kalman spike, eq. following "Full innovation covariance").
- **Koopman operator $U$**: On observables of the innovation process, $U$ is the conditional-expectation operator of the Kalman filter, which is linear.
- **Induced projection $P_\Lambda$**: Since $\Lambda_x$ discards the covariance state (constant at steady state), $P_\Lambda$ conditions on $(\hat\omega_1, \hat\omega_2)$ and takes expectation over the (constant) covariance components.
- **Orthogonal subspace $\text{Ran}(Q_\Lambda)$**: At steady state, the discarded components are constants; $\text{Ran}(Q_\Lambda)$ has zero dimension on the stationary distribution. Therefore $Q_\Lambda U = 0$ and $K_0 = 0$.

**Prediction:** $\varepsilon^\ast \geq 0$ with equality. This matches the Kalman spike's exact result $\varepsilon^\ast = 0$ at steady state.

*Epistemic status: Derived -- the MZ prediction reproduces the known result in the one case where the full answer is available.* This is reassuring but weak: the test case is degenerate (orthogonal subspace is trivial). A stronger test would be the transient regime (where the covariance is time-varying and $K_s \neq 0$), but the MZ machinery requires stationarity and so doesn't directly apply to the transient.

### 6.2 The non-degenerate analog

A non-degenerate test would be: two Kalman filters where the *projection* discards something non-constant. For example, project the 2D state $(\hat\omega_1, \hat\omega_2)$ down to the 1D sum $\hat\omega_+ = \hat\omega_1 + \hat\omega_2$. The orthogonal component is $\hat\omega_- = \hat\omega_1 - \hat\omega_2$, which is non-constant and carries predictive information about future innovations when $\rho \neq 0$.

In this case:
- $K_0$ measures the one-step predictive content of $\hat\omega_-$ for future $\hat\omega_+$ -- non-zero when $\rho \neq 0$.
- The MZ-optimal macro-dynamics has a non-Markovian memory: the current $\hat\omega_+$ alone doesn't optimally predict the next $\hat\omega_+$; you also need lagged $\hat\omega_+$ values to reconstruct the information lost when $\hat\omega_-$ was discarded.

This would be the natural worked example to test the framework. It has not been computed here; it is a concrete next step.

---

## 7. What This Gives AAD (and What It Doesn't)

### 7.1 What genuinely transfers

1. **The Hilbert-space framing makes the closure defect a well-defined inner-product quantity** under stationarity -- this is a meaningful formulation upgrade, not just a technical rephrasing. It means $\varepsilon_x$ has the *same mathematical type* as the trace of a positive operator, which opens up trace-inequality tools.

2. **The identification $f_c^\text{MZ} = P_\Lambda U P_\Lambda$ gives a concrete construction of the optimal Markovian macro-dynamics** against which any admissible $f_c$ can be compared. This is a missing benchmark in the current AAD formulation.

3. **The spectral interpretation of the bridge lemma's contraction** ($f_c$ contraction in state space ↔ $Q_\Lambda U$ spectral gap in observable space) connects AAD's sector condition to the standard dynamical-systems theory of decay of correlations. This is a *conceptual* anchor that doesn't require the full lower-bound result to be useful.

4. **The orthogonal noise $F$ acquires a clean interpretation** as the information content of discarded micro-variables that is not mediated through the macro-state. For purposeful agents this is exactly the strategic-information-content of $\Sigma_i$ that does not survive projection to $\Sigma_c$.

### 7.2 What does not close

The target hypothesis $\varepsilon^\ast \geq C \cdot \lVert K \rVert_{\ell^1}$ **does not hold as stated** under current AAD formulation, for the obstructions in §5. The weaker derivable result is:

$$\varepsilon^\ast_{\text{per-step}} \geq \lVert Q_\Lambda U P_\Lambda \rVert_{\text{op}} \quad \text{(when } f_c^\text{MZ} \notin \mathcal M_{\text{adm}} \text{)}$$

which involves only the zero-lag kernel and a potential admissibility gap.

The stronger form $\varepsilon^\ast_{\text{traj}} \geq (\nu_c / \alpha_c) \lVert K \rVert_{\ell^1}$ is *plausible* as a trajectory-error bound (§4.2) but requires the four additional pieces in §5.5 to close.

---

## 8. Open Questions

1. **Compute the non-degenerate Kalman test case** (§6.2): two filters with $\hat\omega_+$ projection, derive $K_0$ and $K_s$ explicitly, check whether the per-step and trajectory MZ predictions match direct calculation of $\varepsilon^\ast$ and $e_T$ in that setup.

2. **Does $P_\Lambda U P_\Lambda \in \mathcal M_{\text{adm}}$ generically?** If the MZ-optimal Markovian reduction automatically inherits AAD structure from the micro-dynamics, the admissibility gap of §5.2 disappears and one of the obstructions goes away. This is itself an interesting question about AAD -- it would say "the $L^2$-best macro-dynamics is automatically AAD-shaped when the micro-dynamics are."

3. **Reformulate $\varepsilon^\ast$ as a trajectory quantity** or define $\varepsilon^\ast_{\text{traj}}$ explicitly. The current per-step definition in #form-composition-closure is compatible with the bridge-lemma style trajectory error but they are not *the same quantity*. Distinguishing them explicitly may clean up several results.

4. **Handle non-stationary auxiliary states** (Beta-Bernoulli with diverging $n$, structurally adapting DAGs). This is the main technical obstacle to extending MZ to purposeful agents. The candidate is to work in the *innovation frame* (stationary signal) plus an explicit quasi-stationary correction for the slowly-varying auxiliary state -- a Magnus-expansion-style perturbation of MZ.

5. **Quantify the admissibility-price** $\varepsilon^\ast - \tilde\varepsilon$. When does the constraint "macro-dynamics is AAD-shaped" cost closure-defect, and when is it free? The Kalman case has zero admissibility-price; the Beta-Bernoulli case has positive admissibility-price (since no fixed-gain AAD dynamics can match the decaying-gain micro-update). A classification would be useful.

---

## 9. Summary and Recommended Epistemic Stance

**The MZ connection to AAD's composition framework is real but partial.** Under stationarity and coordinate-compatibility conditions, the closure defect $\varepsilon^\ast$ admits a Hilbert-space reformulation, and the MZ-optimal Markovian macro-dynamics provides a benchmark against which admissibility constraints can be measured. The zero-lag kernel $K_0$ lower-bounds $\varepsilon^\ast$ when the MZ-optimal dynamics falls outside $\mathcal M_{\text{adm}}$.

**The target hypothesis $\varepsilon^\ast \geq C \cdot \lVert K \rVert_{\ell^1}$ does not close as stated.** $\lVert K \rVert_{\ell^1}$ is a trajectory-accumulation quantity; $\varepsilon^\ast$ is a per-step quantity; they are the wrong type-match. The natural place for the full-kernel norm is in the bridge lemma's trajectory-error bound, not in $\varepsilon^\ast$ itself.

**The worst-case interaction with AAD is that the most interesting cases** (purposeful agents with diverging auxiliary state) **are exactly the cases where MZ's stationarity assumption fails.** This suggests the MZ connection will anchor AAD's *epistemic-substate* composition cleanly (Kalman-type agents, stationary estimation frames) but will not, without substantial additional work, anchor the *purposeful-substate* composition where the composition-closure framework is most load-bearing.

**Recommended update to #form-composition-closure Working Notes.** The MZ connection should be promoted from "plausible but unworked" to "partially worked; per-step bound via $K_0$ derived under stationarity; full kernel bound requires reformulating $\varepsilon^\ast$ as a trajectory quantity or accepting the hypothesis as applying to the bridge lemma's trajectory-error bound rather than to $\varepsilon^\ast$ directly. Extension to purposeful agents blocked by non-stationarity of strategy updates." This spike is the reference for that update.

---

## Appendix: References

- Mori, H. (1965). "Transport, collective motion, and Brownian motion." *Prog. Theor. Phys.* 33, 423.
- Zwanzig, R. (1961). "Memory effects in irreversible thermodynamics." *Phys. Rev.* 124, 983.
- Zwanzig, R. (1973). "Nonlinear generalized Langevin equations." *J. Stat. Phys.* 9, 215.
- Chorin, A. J., Hald, O. H. (2007). *Stochastic Tools in Mathematics and Science*, 2nd ed., Springer. (Chapter 6: "Mori-Zwanzig formalism" and the discrete-time version.)
- Givon, D., Kupferman, R., Stuart, A. M. (2004). "Extracting macroscopic dynamics: model problems and algorithms." *Nonlinearity* 17, R55.
- Lin, Y. T., Lu, F. (2021). "Data-driven model reduction, Wiener projections, and the Koopman-Mori-Zwanzig formalism." *J. Comput. Phys.* 424, 109864.

These references are cited from memory and should be verified before any formal use. The Chorin-Hald discrete-time formalism is the relevant reference for the event-driven AAD setting.
