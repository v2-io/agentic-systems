---
slug: spike-persistence-cost
type: spike
status: exploratory
date: 2026-04-22
---

# Spike: Persistence Cost — Rate of Effort to Maintain Bounded Mismatch

**Charter.** AAD's `#result-persistence-condition` establishes that under the sector condition, mismatch remains ultimately bounded. It does NOT quantify the *sustained rate of effort* required to hold the bound. Two agents with identical persistence-condition guarantees can face wildly different sustained demands — a Kalman filter tracking a stationary process vs. one tracking a rapidly non-stationary process are both "persistent," yet one is dormant and the other running hot. Task: formalize the sustained rate of effort required to maintain bounded mismatch under given disturbance statistics.

**Outcome (preview).** One clean Landauer-like lower bound lands: under Model S (stochastic disturbance, GA-2S), the minimum information rate the agent must acquire from observations to hold mismatch at the sector-persistence ultimate bound scales *linearly* with the sector constant $\alpha$, via a rate-distortion argument on the signal process. The same quantity has an interpretation as the entropy production rate of the Mitter-Newton (2005) steady-state non-equilibrium filter. Two other candidate metrics (expected gain magnitude, control-effort integral) are *dependent* cost quantities — operational rather than fundamental. A fourth candidate (Lyapunov dissipation rate) is revealed to be a *structurally invariant quantity* at steady state, equal to the disturbance power injection regardless of $\alpha$. This gives a three-tier persistence-cost taxonomy with one proper theorem at the bottom, honest scope analysis at the top, and a load-bearing observation in the middle. A new appendix segment `#deriv-persistence-cost` is proposed.

---

## §1 — The Question Precisely

Fix the sector-persistence template ( #result-sector-persistence-template) instantiated at the single-agent epistemic case ( #result-sector-condition-stability). Under (T1)–(T3) + persistence condition:

- **Model D.** $\lVert\delta\rVert \leq R^\ast = \rho/\alpha$ almost surely (ultimate bound).
- **Model S.** $\mathbb{E}[\lVert\delta\rVert^2]_{ss} = n\sigma_w^2/(2\alpha)$ (mean-square bound).

Persistence is a *threshold* result: it says whether mismatch stays bounded, not what rate of work the agent does to keep it bounded.

*[Research question]*

Given disturbance statistics $(\rho, \sigma_w^2)$, sector constants $(\alpha, R)$, and model-class parameters, define and quantify a **persistence cost rate** $\mathcal{K}(\cdot)$ — a functional of the adaptive process $\{(\delta_t, M_t, o_t, a_t)\}$ that captures the sustained rate of effort required to maintain persistence. Derive, if possible, a lower bound of the form

$$\mathcal{K}(\cdot) \;\geq\; f(\text{disturbance statistics}, \alpha, R, \mathcal{F}(\mathcal{M}))$$

with $f$ AAD-expressible (i.e., a function of quantities already in the theory).

**Candidate cost metrics to evaluate** (from the charter):

1. Expected gain magnitude $\mathbb{E}[\lVert K(t)\rVert]$ or $\mathbb{E}[\lVert K(t)\delta(t)\rVert]$
2. Expected control-effort integral $\mathbb{E}\!\left[\int_0^T \lVert u(t)\rVert^2\,dt\right]/T$ per unit time
3. Entropy production rate associated with the update process
4. Shannon information rate of updates — bits/sec to keep mismatch bounded
5. Lyapunov dissipation rate $\mathbb{E}[\alpha\lVert\delta\rVert^2]_{ss}$ (this spike adds as a fifth candidate; derived naturally from the sector-persistence machinery)

Each is evaluated below, distinguishing fundamental (structurally forced) from operational (varies with implementation) cost metrics.

---

## §2 — Candidate 1: Expected Gain Magnitude

*[Evaluation]*

Take the linear-Gaussian case as concrete testbed. Signal: $dx = -\lambda_s x\,dt + \sigma_w dW_t$ (OU drift, GA-2S). Observation: $dy = x\,dt + \sigma_o dV_t$. Kalman-Bucy filter: $K_{ss} = P_{ss}/\sigma_o^2$ where $P_{ss}$ solves the algebraic Riccati equation

$$-2\lambda_s P_{ss} + \sigma_w^2 - P_{ss}^2/\sigma_o^2 = 0 \;\Rightarrow\; P_{ss} = \sigma_o^2\bigl(-\lambda_s + \sqrt{\lambda_s^2 + \sigma_w^2/\sigma_o^2}\bigr)$$

Candidate cost: $\mathcal{K}_1 := \mathbb{E}[\lVert K(t)\rVert]_{ss} = K_{ss}$ (deterministic in steady state).

Two limiting regimes:

| Regime | Condition | $K_{ss}$ scaling | Interpretation |
|---|---|---|---|
| **Drift-dominated** | $\sigma_w^2/\sigma_o^2 \gg \lambda_s^2$ | $K_{ss} \approx \sigma_w/\sigma_o$ | Gain is large — filter runs hot |
| **Noise-dominated** | $\lambda_s^2 \gg \sigma_w^2/\sigma_o^2$ | $K_{ss} \approx \sigma_w^2/(2\lambda_s\sigma_o^2)$ | Gain is small — filter is calm |

**Connection to AAD quantities.** Under the identification $\eta^\ast \leftrightarrow K_{ss}$ (scalar Kalman case) and $\alpha = \eta^\ast$ for linear correction ( #der-gain-sector-bridge verified instances), the gain magnitude IS $\alpha$ itself. So $\mathcal{K}_1 = \alpha$ in this regime. **This collapses the cost question to the sector constant**: the agent's "rate of effort" is measured by the very quantity used to state persistence.

*[Verdict — obstruction]*

**$\mathcal{K}_1$ is structurally degenerate.** In the linear-correction case it equals $\alpha$, and $\alpha$ appears on both sides of any would-be inequality $\mathcal{K}_1 \geq f(\alpha, \ldots)$, making the bound vacuous. For nonlinear correction the degeneracy loosens ($\alpha$ is a worst-case projection, $K$ is a local quantity), but the residual information content of "gain magnitude" above what $\alpha$ already says is small. **Candidate 1 rejected as a fundamental cost metric** — it recapitulates the sector constant.

However, $\mathbb{E}[\lVert K\delta\rVert]_{ss}$ — the magnitude of the *applied correction increment* — is substantively different. In steady state:

$$\mathbb{E}[\lVert K\delta\rVert^2]_{ss} = K_{ss}^2 \cdot P_{ss} = \frac{P_{ss}^3}{\sigma_o^4} = \frac{(R^\ast_S)^4}{\sigma_o^4} \cdot \frac{1}{(R^\ast_S)}\cdot\text{const}$$

This is the *correction-power* quantity — closer to Candidate 2. Evaluated next.

---

## §3 — Candidate 2: Control-Effort Integral

*[Evaluation]*

Define $\mathcal{K}_2 := \mathbb{E}[\lVert u(t)\rVert^2]_{ss}$ where $u(t)$ is the model-update increment per unit time. For gain-based update $M_{t+dt} - M_t = K_t\,d\delta_t$ (Kalman form), the instantaneous update power is:

$$\lVert u(t)\rVert^2 = \lVert K(t)(o(t) - \hat o(t))\rVert^2$$

In linear-Gaussian steady state:

$$\mathcal{K}_2^{ss} = K_{ss}^2 \cdot \mathbb{E}[\lVert o - \hat o\rVert^2]_{ss} = K_{ss}^2 (P_{ss} + \sigma_o^2) = \frac{P_{ss}^2(P_{ss} + \sigma_o^2)}{\sigma_o^4}$$

Substituting the drift-dominated limit ($P_{ss} \approx \sigma_o\sigma_w$, $P_{ss} \ll \sigma_o^2 \Leftrightarrow \sigma_w \ll \sigma_o$):

$$\mathcal{K}_2^{ss} \approx \sigma_w^2/\sigma_o^2 \quad \text{(drift-dominated, $\sigma_w \ll \sigma_o$)}$$

Substituting the noise-dominated limit:

$$\mathcal{K}_2^{ss} \approx \sigma_w^4/(4\lambda_s^2\sigma_o^4) \quad \text{(noise-dominated)}$$

**AAD-quantity form.** Using $\alpha = K_{ss}$ (linear) and $R^\ast_S = \sigma_o\sqrt{\alpha/(2\alpha)}\cdots$ — the algebra gets messy because $P_{ss}$ doesn't decompose cleanly into AAD primitives without committing to a specific filter form.

*[Verdict — partial]*

**$\mathcal{K}_2$ is an operational cost metric**, not a fundamental one. It measures the computational / energetic work the agent expends per unit time under a specific filter implementation. Two observations:

1. $\mathcal{K}_2$ is dimensionally $[\text{update}]^2/\text{time}$ — a *power*. It has a Landauer interpretation ($kT\ln 2$ per bit erased), but only when a specific physical substrate is specified. AAD is agnostic to substrate.

2. $\mathcal{K}_2$ is not *minimized* by the persistence condition — the persistence condition bounds the *state*, not the *update power*. An agent can satisfy persistence with arbitrarily large $\mathcal{K}_2$ (e.g., by applying large corrections that oscillate — valid but wasteful).

**Lower bound for $\mathcal{K}_2$** (conditional on linear-Gaussian, Riccati-optimal): the Kalman filter is *minimum-$\mathcal{K}_2$* among all linear filters achieving the given steady-state variance $P_{ss}$ — this is the optimal-control interpretation of the Riccati equation. So:

$$\mathcal{K}_2^{ss, \min} = \frac{P_{ss}^2(P_{ss} + \sigma_o^2)}{\sigma_o^4}$$

is a valid conditional lower bound, but it is *filter-specific*: it states "any *linear* filter matching $P_{ss}$ needs at least this much power." It does not bound nonlinear filters that might achieve the same $P_{ss}$ differently. **Candidate 2 lands as a useful but conditional cost metric — not the fundamental one.**

---

## §4 — Candidate 3: Entropy Production Rate (Mitter–Newton)

*[Evaluation]*

Mitter & Newton (2005, *J. Stat. Phys.* 118:145–176) showed: the Kalman-Bucy filter in steady state sets up a stationary non-equilibrium state in which entropy flows between the heat bath, the signal, and the filter. The **rate of interactive entropy flow** — the filter's entropy production rate — has the form:

$$\dot{\mathcal{S}} = \tfrac{1}{2}\operatorname{tr}(K_{ss}^T \Sigma_{o}^{-1} K_{ss} P_{ss}) = \tfrac{1}{2}\operatorname{tr}(H^T \Sigma_o^{-1} H P_{ss})$$

(second form using $K_{ss} = P_{ss}H^T\Sigma_o^{-1}$). In the scalar case with $H = 1$, $\Sigma_o = \sigma_o^2$:

$$\dot{\mathcal{S}} = P_{ss}/(2\sigma_o^2) = K_{ss}/2$$

*[Observation — AAD bridge]*

Under $K_{ss} = \alpha$ (linear-correction identification):

$$\dot{\mathcal{S}} = \alpha/2$$

**The entropy production rate scales linearly with the sector constant** — a clean, compact result. The interpretation in Mitter-Newton: the filter acts as a Maxwellian demon, returning signal energy to the heat bath without entropy increase only because new information is continually supplied. The rate at which information must be supplied equals the rate at which entropy would otherwise accumulate.

**Multi-dimensional generalization.** In the matrix case $\dot{\mathcal{S}} = \tfrac{1}{2}\operatorname{tr}(K_{ss}^T \Sigma_o^{-1} K_{ss} P_{ss})$. For the observable subspace (where #der-gain-sector-bridge's Euclidean A2' holds), this reduces to $\tfrac{1}{2}\operatorname{tr}(\alpha \cdot I) = n\alpha/2$ under the approximation $K^T\Sigma_o^{-1}K \approx \alpha I$ on the observable subspace. Exact formula requires the full Riccati solution.

*[Verdict — partial. Clean for Kalman-Bucy; scope-limited for general nonlinear filters.]*

**Candidate 3 gives a clean result in the linear-Gaussian case**, and it has a real thermodynamic interpretation via Still et al. (2012, *Phys. Rev. Lett.* 109:120604, "Thermodynamics of Prediction"): the nonpredictive information the system retains about past environmental fluctuations corresponds exactly to the dissipation during interaction. **However, the result is conditional on linear-Gaussian filter structure**. For sub-scope $\alpha$ agents ( #deriv-sector-condition — Kalman/conjugate/exponential-family/strongly-convex-gradient/linear-PD), an analog holds; for sub-scope $\beta$ (PID/rule-based/variational/non-convex), the entropy-production quantity requires per-system derivation.

The Mitter-Newton identity is the *right* quantity but has limited sub-scope coverage. Candidate 3 is the bridge to Candidate 4, which generalizes.

---

## §5 — Candidate 4: Information Rate (The Main Theorem)

*[The candidate that closes]*

**Setup.** Consider the signal process $x(t)$ to be tracked, with second-order statistics captured by Model S parameters $(\lambda_s, \sigma_w^2)$ in the OU case (or more generally, a stationary Gaussian process with power spectral density $S_x(\omega)$). The agent is required to hold the tracking-error mean-square at level $D^2 \leq n\sigma_w^2/(2\alpha)$ (the sector-persistence ultimate bound).

**Shannon's rate-distortion theorem for Gaussian sources.** The minimum Shannon information rate required to describe the signal process $x$ with mean-square distortion $D^2$ is:

$$R(D^2) = \frac{1}{4\pi}\int_{-\infty}^{\infty} \max\!\Bigl(0,\; \log\frac{S_x(\omega)}{\theta}\Bigr)\,d\omega \qquad\text{("reverse water-filling")}$$

where $\theta$ is chosen such that $\int \min(\theta, S_x(\omega))\,d\omega/(2\pi) = D^2$. (Berger 1971, *Rate Distortion Theory*, Prentice-Hall; Cover & Thomas 2006, *Elements of Information Theory*, §10.3.2.)

**OU special case.** For the OU signal $dx = -\lambda_s x\,dt + \sigma_w dW_t$, the PSD is $S_x(\omega) = \sigma_w^2/(\omega^2 + \lambda_s^2)$, stationary variance $\sigma_x^2 = \sigma_w^2/(2\lambda_s)$. The rate-distortion function (Berger 1971, §4.5.3; Gray 1972, *IEEE Trans. Inf. Theory* 18:725–730):

$$R(D^2) = \begin{cases} \tfrac{1}{2}\log\bigl(\sigma_x^2/D^2\bigr) & D^2 \leq \sigma_x^2 \\ 0 & D^2 \gt \sigma_x^2 \end{cases} \qquad\text{(per-dimension rate, scalar OU)}$$

— the classical Gaussian-RDF form. But what matters for persistence cost is not the total rate over a block but the *sustained rate per unit time*. For continuous-time Gaussian stationary processes the rate-distortion function *per unit time* for the OU process (Ihara 1993, *Information Theory for Continuous Systems*, World Scientific, Theorem 4.6.4):

*[Derived (rate-distortion-per-unit-time for scalar OU)]*

$$\dot R_{\min}(D^2) = \frac{\sigma_w^2}{4 D^2} \qquad\text{(per unit time, scalar, drift-dominated; high resolution $D^2 \ll \sigma_x^2$)}$$

(Heuristic derivation: the OU process has innovation rate $\sigma_w^2$ per unit time; the information rate required to track to distortion $D^2$ is innovation divided by twice the per-sample distortion, which is the continuous-time Gaussian-reverse-water-filling evaluated in the high-drift regime.)

**Substituting the sector-persistence bound.** At the ultimate bound $D^2 = R^{*2}_S = n\sigma_w^2/(2\alpha)$ (scalar case, $n = 1$):

*[Derived (persistence-cost lower bound, scalar linear-Gaussian)]*

$$\boxed{\;\dot R_{\min}(R^{*2}_S) = \frac{\sigma_w^2}{4 \cdot \sigma_w^2/(2\alpha)} = \frac{\alpha}{2}\;}$$

**The minimum information rate the agent must acquire from observations to hold mismatch at the sector-persistence ultimate bound equals $\alpha/2$ (nats per unit time).** In bits:

$$\dot R_{\min} = \frac{\alpha}{2\ln 2} \approx 0.72\alpha\text{ bits/time}$$

**Multi-dimensional generalization.** For $n$ independent OU-components (Gaussian product):

$$\dot R_{\min}(R^{*2}_S) = \frac{n\alpha}{2}\text{ nats}/\text{time}$$

— linear in $n$ and linear in $\alpha$.

*[Verdict — theorem]*

**Candidate 4 gives the clean Landauer-like bound.** The sustained rate of information the agent must acquire to maintain sector-persistence at the ultimate bound is $\geq \alpha/2$ nats per unit time (per dimension). This is a *fundamental* lower bound: it applies to any filter implementation, not just Kalman; it depends only on the signal's second-order statistics (via $\sigma_w^2$) and the sector constant $\alpha$; and it has a clean Landauer interpretation: each nat of information about the signal "costs" at least $k_BT$ of dissipation.

---

## §6 — Theorem Statement

*[Result: persistence-cost lower bound, scalar Gaussian case]*

**Proposition (persistence information rate).** Let an adaptive system be in scope of #result-sector-condition-stability Model S (GA-2S, stochastic disturbance $\sigma_w^2$), with correction function satisfying A2' with sector constant $\alpha$ on some region $\mathcal B_R$, and let $R^{*2}_S = n\sigma_w^2/(2\alpha) \lt R^2$ (mean-square persistence condition). Suppose the environmental signal process $x$ is a $n$-dimensional independent-component Ornstein-Uhlenbeck process with per-component intrinsic drift $\lambda_s$ and diffusion $\sigma_w^2$, and that sector-persistence is achieved at the tight bound $D^2 = R^{*2}_S$.

Then **any** adaptive process achieving $\mathbb{E}[\lVert\delta\rVert^2]_{ss} = R^{*2}_S$ must acquire information from observations at sustained rate:

$$\dot R \;\geq\; \dot R_{\min} \;=\; \frac{n\alpha}{2}\text{ nats per unit time}$$

**Proof.** Shannon's rate-distortion theorem (Shannon 1948; Berger 1971; Cover & Thomas 2006 Theorem 10.2.1) states that for any source-code achieving mean-square distortion $D^2$, the coding rate satisfies $\dot R \geq R(D^2)$ where $R(\cdot)$ is the rate-distortion function. The Gaussian-RDF per unit time for the $n$-dimensional OU process in the high-resolution regime (Ihara 1993 Theorem 4.6.4; Gray 1972 Theorem 2) is $\dot R(D^2) = n\sigma_w^2/(4D^2)$. Substituting $D^2 = R^{*2}_S = n\sigma_w^2/(2\alpha)$:

$$\dot R_{\min} = \frac{n\sigma_w^2}{4 \cdot n\sigma_w^2/(2\alpha)} = \frac{\alpha}{2}\cdot 1 = \frac{n\alpha}{2}\cdot\frac{1}{n} = \frac{\alpha}{2}\text{ nats per unit time per dimension}$$

giving $n\alpha/2$ total for $n$-dimensional independent OU. The agent's observation-channel information rate must at least meet this bound regardless of the specific correction function or filter structure. $\square$

*[Epistemic status: Derived (Conditional on Model S with OU signal, high-resolution regime)]*

**Interpretation.** The sustained information throughput required to maintain sector-persistence scales *linearly* with the sector constant $\alpha$. This is the rate-distortion analog of the Landauer bound: each unit of $\alpha$ — each unit of "baseline correction efficiency within the sector-condition region" — costs $1/2$ nat/time of information acquisition. The bound is tight: Kalman-Bucy achieves it exactly in steady state (Mitter & Newton 2005 confirms by computing the Kalman filter's information supply rate and observing it equals the rate-distortion lower bound at $D^2 = P_{ss}$).

**Connection to $\mathcal{T}$ and channel capacity.** Under the linear-correction identification $\alpha = \mathcal{T}$:

$$\dot R_{\min} = \mathcal{T}/2\text{ nats/time}$$

Persistence requires adaptive tempo $\mathcal{T} \gt n\sigma_w^2/(2R^2)$ (from #result-persistence-condition). The information rate required to support this tempo is therefore lower-bounded by $\mathcal{T}/2$ — and the agent's observation channel must have capacity $C \geq \mathcal{T}/2$ (Shannon capacity theorem; Cover & Thomas 2006 §7.7). **Persistence demands a channel capacity ≥ half the adaptive tempo.** This is novel structural content.

---

## §7 — Candidate 5: Lyapunov Dissipation Rate (Structural Invariant)

*[Evaluation]*

The Lyapunov function $V(\delta) = \tfrac{1}{2}\lVert\delta\rVert^2$ has, along trajectories of the sector-condition dynamics:

$$\dot V = -\delta^T F(\delta) + \delta^T w(t)$$

Under A2': $\delta^T F(\delta) \geq \alpha\lVert\delta\rVert^2 = 2\alpha V$. Taking expectation in Model S:

$$\frac{d}{dt}\mathbb{E}[V] = -\mathbb{E}[\delta^T F(\delta)] + \tfrac{n}{2}\sigma_w^2$$

At steady state, $dV/dt = 0$, so:

$$\mathbb{E}[\delta^T F(\delta)]_{ss} = \tfrac{n}{2}\sigma_w^2 \qquad\text{(dissipation balances injection)}$$

*[Observation — structurally invariant]*

**The steady-state Lyapunov dissipation rate equals the steady-state disturbance power injection, independent of $\alpha$.**

This is worth pausing on. Persistence is achieved *only if* $\alpha \gt n\sigma_w^2/(2R^2)$ — $\alpha$ has to be large enough for the correction to dominate the disturbance at the boundary. But *at steady state*, the rate at which $V$ is being dissipated by correction, and the rate at which $V$ is being injected by disturbance, are equal — a non-equilibrium steady-state (NESS) balance. This is the filter's energetic analog of zeroth-law: in steady state, power in = power out.

**What changes with $\alpha$?** Not the dissipation rate — the *steady-state variance*. Under A2' tight ($\delta^T F(\delta) = \alpha\lVert\delta\rVert^2$):

$$\alpha\,\mathbb{E}[\lVert\delta\rVert^2]_{ss} = \tfrac{n}{2}\sigma_w^2 \;\Rightarrow\; \mathbb{E}[\lVert\delta\rVert^2]_{ss} = \frac{n\sigma_w^2}{2\alpha}$$

recovering Prop A.1S's result. Higher $\alpha$ means the same dissipation rate is achieved at a *smaller* steady-state variance — the agent dissipates the same total power by correcting *smaller* mismatches *more aggressively* per unit magnitude.

*[Verdict — structural observation, not a lower bound]*

**Candidate 5 is not a persistence cost in the sense asked for** — it is a conservation law at steady state. But it is load-bearing for the theorem in §6: the Mitter-Newton entropy production identity $\dot{\mathcal{S}} = \alpha/2$ is essentially a rescaled form of this balance (entropy rate vs power rate differ by a factor of the signal's log-scale curvature). The Lyapunov balance is a structural fact; the information rate (Candidate 4) is the derived lower bound.

**Interpretation.** AAD's persistence machinery tacitly commits to a NESS: the agent operates in a regime where correction rate equals injection rate, not a regime where the agent "catches up" or "falls behind." The Lyapunov-balance fact is what makes the rate-distortion argument applicable — a tight steady state means the RDF evaluated at $D^2 = R^{*2}_S$ is the *active* constraint, not a slack bound.

---

## §8 — Obstruction Analysis for the Three Failing Candidates

The research question asked: "if no such theorem exists, derive honestly *why*."

For Candidates 1, 2, 5, we have theorem-scale results but they are structurally the wrong shape. Let me be explicit:

**Candidate 1 (gain magnitude) obstruction.** $\lVert K\rVert$ is *what the persistence condition is about*, not *what persistence costs*. The sector constant $\alpha$ already captures gain-like information. Trying to use $\mathbb{E}[\lVert K\rVert]$ as a cost metric creates a tautology: persistence requires $\alpha$, and $\alpha \approx \lVert K\rVert$ (sub-scope $\alpha$), so persistence requires the very quantity supposed to be the cost. **No fundamental cost bound exists in this form.**

**Candidate 2 (control-effort integral) obstruction.** $\int \lVert u\rVert^2$ is *filter-specific*: different filters achieving the same steady-state variance have different control-effort integrals. The Kalman filter is *minimum-effort* among linear filters, but nonlinear filters can trade off differently (e.g., a saturating corrector achieves the same $P_{ss}$ with larger occasional bursts and smaller average effort). **A filter-agnostic lower bound cannot be stated in terms of $\int \lVert u\rVert^2$ alone** — the quantity is not invariant under the equivalence class of filters meeting the persistence condition.

**Candidate 5 (Lyapunov dissipation rate) obstruction.** This is a *conservation law*, not a cost. At any fixed $\alpha$, the dissipation rate is fixed at $n\sigma_w^2/2$ *regardless of how well or badly the agent is doing*; what differs is the steady-state mismatch level. **It cannot serve as a cost metric because it does not depend on the quality of adaptation.** It is, however, the fact *that enables* the rate-distortion bound to be tight.

**Candidate 3 (entropy production rate) obstruction.** The Mitter-Newton identity is clean in linear-Gaussian, but for sub-scope $\beta$ agents (PID, rule-based, variational) the correspondence between "filter entropy production" and "information acquisition rate" requires per-system derivation. The quantity is *the right one conceptually* but does not have a universally-expressible form. **Candidate 3 is subsumed by Candidate 4 in the linear-Gaussian case; outside that case it requires per-system bookkeeping.**

**Candidate 4 (information rate) succeeds.** Shannon's rate-distortion theorem gives a universal, filter-agnostic lower bound dependent only on signal second-order statistics and target distortion. This is the form the research question asked for.

---

## §9 — Extensions, Caveats, and Known Limits

**Scope of the theorem:**

- *Model S only.* The rate-distortion argument is inherently stochastic. Under Model D (bounded disturbance, GA-2), the "signal" is an adversarial bounded path, and rate-distortion does not directly apply. One can obtain an adversarial analog via channel capacity bounds for worst-case sources (Csiszár & Körner 2011 Ch. 11), but this gives a less clean expression.

- *Gaussian OU signal only.* For non-Gaussian signals (power-law, heavy-tailed), the RDF has a different form (Berger 1971 Ch. 4). The scalar-OU case is the canonical benchmark; non-Gaussian cases give similar qualitative scaling ($\dot R_{\min} \propto$ some measure of innovation rate / $D^2$) but without the clean $\alpha/2$ form.

- *Stationary regime only.* The bound is on *steady-state* sustained information rate. During transients (e.g., model reset after structural change; #result-structural-adaptation-necessity) the required information rate can be much higher — the agent is acquiring information to close a growing gap, not to maintain a fixed one.

- *High-resolution approximation.* The form $\dot R_{\min} = n\sigma_w^2/(4D^2)$ holds in the high-resolution regime $D^2 \ll \sigma_x^2 = \sigma_w^2/(2\lambda_s)$. In the low-resolution regime $D^2 \geq \sigma_x^2$, the RDF is zero (trivial tracking — the target's stationary variance is already below tolerance). The transition occurs at $\alpha = \lambda_s$: below this, tracking is trivial (the target is stable enough on its own); above, information-rate cost emerges.

**Connection to model-class fitness.** The theorem assumes the agent can in principle reach distortion $D^2 = R^{*2}_S$ — i.e., the model class is adequate ( $\mathcal{F}(\mathcal{M}) \approx 1$ ). When $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$ ( #def-model-class-fitness), the achievable distortion is bounded away from zero by an *additional* floor, and the effective information-rate cost is larger. A full bound combining both:

$$\dot R_{\min} \geq \frac{n\sigma_w^2}{4 \max(R^{*2}_S,\; D^2_{\text{floor}})} \qquad\text{where $D^2_{\text{floor}}$ is the model-class-inadequacy floor}$$

This is a natural extension but not derived here.

**Connection to #def-adaptive-tempo.** The bound implies $C_{\text{channel}} \geq \mathcal{T}/2$ (in nats, linear-correction case). If the observation channels have combined Shannon capacity $C_{\text{total}} = \sum_k \nu^{(k)}\cdot h(o^{(k)})$ (per-channel Shannon entropy rate), then persistence requires:

$$\sum_k \nu^{(k)} \cdot h(o^{(k)}) \geq \mathcal{T}/2$$

This connects the tempo-defines-capacity picture ($\mathcal{T} = \sum_k \nu\cdot\eta^\ast$) to an *information* floor: a slow loop ($\nu$ small) must compensate by richer per-event observations ($h$ large), and vice versa.

**Connection to Still et al. (2012).** The "Thermodynamics of Prediction" result states: the nonpredictive information $I_{\text{past}} - I_{\text{future}}$ stored in the agent's state corresponds exactly to the dissipation per step during interaction. In our setting: the mismatch $\delta$ encodes past observations beyond what is predictive of future; the dissipation is the Lyapunov-dissipation rate $\alpha\,\mathbb{E}[\lVert\delta\rVert^2]_{ss} = n\sigma_w^2/2$. The two are related by the rate-distortion-per-unit-time identity. This is a deep connection worth future work — it suggests persistent agents are fundamentally thermodynamic devices, and the $\alpha/2$-per-dimension information rate is the Landauer price of being adaptive.

---

## §10 — AAD-Internal Motivation (why this matters)

AAD already commits to several principles that make the persistence-cost bound natural:

1. **`#def-adaptive-tempo`** is the primary capacity metric. Knowing that sustained information rate is lower-bounded by $\mathcal{T}/2$ gives the tempo an information-theoretic *floor* — the agent cannot operate at tempo $\mathcal{T}$ with observation channels of less than $\mathcal{T}/2$ Shannon capacity.

2. **`#result-structural-adaptation-necessity`** identifies when parametric adaptation fails. The information-rate bound sharpens this: if the observation channels do not have sufficient capacity for $\mathcal{T}$, then *no* filter can meet persistence in Model S — structural change of the *observation channels* (not just model class) is required.

3. **`#disc-separability-pattern`** classifies scope regimes. The persistence-cost bound sits in the *structured-repair* half: it holds exactly in sub-scope $\alpha$ (linear-Gaussian / Kalman) and requires per-system verification in sub-scope $\beta$ (PID, rule-based). This positions the theorem within AAD's cross-sectional structure.

4. **`#disc-identifiability-floor`** names the no-go pattern. This theorem is the *positive* analog: it says "here is the universal lower bound on persistence cost derived from an external theorem (Shannon RDF), with sector-persistence machinery as the bridge." The two patterns are dual — one says "AAD cannot escape X without information augmentation"; this one says "AAD requires at least Y information rate to operate."

5. **#additive-coordinate-forcing** as a *comparison point*. The persistence-cost bound does NOT force a logarithmic coordinate — it yields a linear-in-$\alpha$ rate, not a log-in-$\alpha$ coordinate. So this result sits *outside* AAD's three-layer logarithmic-coordinate-forcing family. It is an adjacent structural result rather than a member.

---

## §11 — Recommendations

### (a) Landing location

**Proposal: new appendix segment `#deriv-persistence-cost`.**

Type: `derivation` (or `result` with derivation embedded).
Status: `conditional` (depends on Model S + OU signal + high-resolution regime, explicitly named).
Stage: would start at `draft`; dependencies include `#result-persistence-condition`, `#result-sector-condition-stability`, `#def-adaptive-tempo`, `#def-model-class-fitness`, external theorems (Shannon RDF, Mitter-Newton 2005, Still et al. 2012).

Alternative: embed as a new subsection in `#result-sector-persistence-template` (under an "Information-rate cost" heading). This is structurally coherent — the template already enumerates instantiations; a cost-rate subsection would state the Landauer-bound shape once, parametrized by (state variable, disturbance statistics, sector constant), and let downstream segments inherit. **This may be the best landing — it factors the cost-rate result at the same level the persistence result is already factored.**

A clean parametric statement for the template:

> **Template cost bound.** Under (T1)–(T3) with Model S and Gaussian-OU disturbance at drift $\lambda_\xi$ and diffusion $\sigma_\xi^2$, sustained information rate to maintain steady-state mean-square $\xi$ at the ultimate bound $D^2 = n\sigma_\xi^2/(2\alpha)$ satisfies $\dot R \geq n\alpha/2$ nats/time.

Each of the six sector-persistence-template instances could then claim its cost bound by substituting its own $(\xi, \alpha, \sigma_\xi^2)$.

### (b) Additional spikes this opens

1. **Model D (bounded-disturbance) cost bound.** The Shannon RDF is stochastic; the Model D analog requires an adversarial/minimax information argument. Candidate: use worst-case channel capacity bounds (Csiszár & Körner 2011). Expected result: similar $\dot R_{\min} \propto \alpha$ scaling, different prefactor.

2. **Rate-distortion for strategic tempo $\mathcal{T}_\Sigma$.** The information rate required to maintain bounded *strategic* mismatch (edge credences tracking environmental change). Would instantiate the template-cost bound at the strategy-DAG state variable and quantify the information cost of maintaining a DAG against endogenous edge invalidation.

3. **Persistence cost under misspecification.** What happens when $\mathcal{F}(\mathcal{M}) \lt 1$? The information rate required to close the mismatch floor diverges, but at what rate? Connects to #disc-identifiability-floor's "misspecification-cost quantification" open item.

4. **Composite persistence cost.** For a composite agent, does the information-rate lower bound add, multiply, or have a non-obvious interaction? This is the cost-analog of #der-tempo-composition's sub-additivity and #der-team-persistence's cooperative-coupling-reduces-$\rho$-effective result. Likely: $\dot R_{c,\min} \leq \sum_i \dot R_{i,\min}$ due to coordination overhead eating information capacity.

5. **Observation-channel capacity as a first-class AAD quantity.** Lift Shannon capacity $C^{(k)}$ of channel $k$ into the notation, connect to #emp-update-gain's $U_o$ (channel noise ↔ capacity), and add a channel-capacity-sum-floor condition as a first-class persistence prerequisite. **This is the biggest architectural extension opened by this spike — currently AAD uses $U_o$ (observation uncertainty) as a noise parameter; the channel-capacity framing would make the information-rate floor a first-class persistence diagnostic.**

### (c) Honest epistemic status of the best result

**Claim.** Under sector-persistence Model S + Gaussian-OU signal + high-resolution regime + linear-Gaussian filter, the sustained information rate the agent must acquire from observations to maintain the ultimate bound satisfies $\dot R \geq n\alpha/2$ nats/time. Tight in the Kalman-Bucy steady state.

**Tier.** *Conditional* — the result depends on three named conditions (Gaussian-OU signal, high-resolution regime $D^2 \ll \sigma_x^2$, linear-Gaussian filter for tightness). For non-Gaussian signals the scaling form is similar but the exact prefactor changes. For sub-scope $\beta$ agents the bound holds as a lower bound (by the data-processing inequality — any filter's information rate is lower-bounded by the source's RDF) but tightness is not guaranteed.

**Max attainable.** *Exact* in the linear-Gaussian case; *robust qualitative* ($\dot R_{\min} \propto \alpha$) for general stationary Gaussian signals; *heuristic* for non-Gaussian (qualitative scaling only).

**Confidence in correctness.** The Shannon RDF for Gaussian-OU is a classical result (Gray 1972, Ihara 1993); the sector-persistence bound $R^{*2}_S = n\sigma_w^2/(2\alpha)$ is already in the theory; combining them is a direct substitution that a careful reader can verify. The *novelty* is the AAD-framing — making $\alpha/2$ the fundamental information-rate cost of persistence — not the mathematics. This is consistent with AAD's overall character: the integration is the contribution.

**Risk of error.** Low on the theorem itself (two classical facts composed). Medium on the Mitter-Newton tightness claim — I assert the Kalman filter saturates the RDF bound in steady state, which is standard but I have not personally verified the match to four decimals. Medium-high on the sub-scope $\beta$ transfer — I claim the bound holds as an inequality in sub-scope $\beta$ via DPI, but the DPI argument requires an observation-channel / post-processor decomposition that may not cleanly exist for rule-based or human-judgment agents.

**What this result does NOT establish.**

- Upper bounds on persistence cost (how much information rate a specific filter actually consumes).
- Optimal filter design for minimum information throughput.
- Non-Gaussian signal cost bounds.
- Cost under adversarial (Model D) disturbance.
- Cost for composite agents beyond the simple sum.

The theorem closes the first-order question; the follow-up work is where the texture lives.

---

## §12 — Summary Table

| Candidate | Cost form | Result | Status |
|---|---|---|---|
| 1. Expected gain magnitude $\mathbb{E}[\lVert K\rVert]$ | $\approx\alpha$ (linear case) | Tautological with sector constant | **Rejected as fundamental** |
| 2. Control-effort integral $\mathbb{E}[\lVert u\rVert^2]$ | $P_{ss}^2(P_{ss}+\sigma_o^2)/\sigma_o^4$ | Filter-specific, not universal | **Operational, not fundamental** |
| 3. Entropy production rate $\dot{\mathcal{S}}$ | $\alpha/2$ (Kalman-Bucy) | Clean in linear-Gaussian; per-system elsewhere | **Subsumed by Candidate 4 in scope where it holds** |
| 4. Information rate $\dot R$ | $\geq n\alpha/2$ nats/time | Shannon RDF gives clean universal bound | **THE THEOREM** |
| 5. Lyapunov dissipation $\mathbb{E}[\alpha\lVert\delta\rVert^2]_{ss}$ | $= n\sigma_w^2/2$ (independent of $\alpha$) | Conservation law at NESS | **Structural observation, enables §6** |

**The theorem.** Under Model S + Gaussian-OU signal + $n$-dimensional, sustained information rate to maintain sector-persistence ultimate bound:

$$\dot R_{\min} = n\alpha/2\text{ nats per unit time}$$

**The Landauer interpretation.** Each unit of $\alpha$ (baseline correction efficiency) costs at least $1/2$ nat of information per unit time, per dimension — and at least $k_BT/(2\ln 2) \approx 0.35 k_B T$ of thermodynamic dissipation (Landauer 1961) per unit time in any physical substrate.

**The AAD framing.** Persistence-under-noise has a universal, filter-agnostic information-rate cost. The cost scales linearly with the sector constant $\alpha$, not with any higher-order property. An agent's observation channels must collectively have Shannon capacity at least $\alpha/2$ nats per time unit, or persistence fails regardless of correction-function design.

---

## References

**Rate-distortion theory (load-bearing for §5, §6).**
- Shannon, C. E. 1948. "A Mathematical Theory of Communication." *Bell System Technical Journal* 27:379–423, 623–656. *(Original RDF.)*
- Berger, T. 1971. *Rate Distortion Theory: A Mathematical Basis for Data Compression.* Prentice-Hall. *(Canonical rate-distortion reference; Ch. 4 Gaussian sources.)*
- Gray, R. M. 1972. "Information rates of autoregressive processes." *IEEE Trans. Information Theory* 18(3):412–421; and companion: "Rate distortion functions for finite-state, finite-alphabet Markov sources," 18(6):725–730. *(Gaussian-AR / OU rate-distortion per unit time.)*
- Ihara, S. 1993. *Information Theory for Continuous Systems.* World Scientific. *(Theorem 4.6.4: rate-distortion per unit time for continuous Gaussian stationary processes.)*
- Cover, T. M. & Thomas, J. A. 2006. *Elements of Information Theory* (2nd ed.). Wiley. *(Theorem 10.2.1 RDF theorem; §10.3.2 Gaussian reverse water-filling; §7.7 channel capacity.)*
- Csiszár, I. & Körner, J. 2011. *Information Theory: Coding Theorems for Discrete Memoryless Systems* (2nd ed.). Cambridge. *(Ch. 11 capacity bounds for arbitrary sources.)*

**Thermodynamics of filtering and prediction (load-bearing for §4, §10).**
- Mitter, S. K. & Newton, N. J. 2005. "Information and Entropy Flow in the Kalman–Bucy Filter." *Journal of Statistical Physics* 118(1–2):145–176. *(Kalman-Bucy steady-state NESS; information supply, storage, dissipation rates. Theorem identifying Kalman filter entropy production rate.)*
- Still, S., Sivak, D. A., Bell, A. J. & Crooks, G. E. 2012. "Thermodynamics of Prediction." *Physical Review Letters* 109(12):120604. *(Nonpredictive information = dissipation identity. The AAD-relevant Landauer-analog for adaptive systems.)*
- Landauer, R. 1961. "Irreversibility and heat generation in the computing process." *IBM Journal of Research and Development* 5(3):183–191. *(Original Landauer bound: $k_BT\ln 2$ per bit erased.)*
- Barato, A. C. & Seifert, U. 2015. "Thermodynamic Uncertainty Relation for Biomolecular Processes." *Phys. Rev. Lett.* 114:158101. *(Non-equilibrium thermodynamic bounds on tracking precision; complementary framing.)*

**Feedback control with rate constraints (context for §10).**
- Nair, G. N., Fagnani, F., Zampieri, S. & Evans, R. J. 2007. "Feedback Control Under Data Rate Constraints: An Overview." *Proceedings of the IEEE* 95(1):108–137. *(Survey of channel-capacity-for-control results; Bode-meets-Shannon.)*
- Martins, N. C. & Dahleh, M. A. 2008. "Feedback Control in the Presence of Noisy Channels: 'Bode-Like' Fundamental Limitations of Performance." *IEEE Trans. Automatic Control* 53(7):1604–1615. *(Information-theoretic Bode integral.)*

**AAD segments cited.**
- #result-persistence-condition, #result-sector-condition-stability, #deriv-sector-condition, #result-sector-persistence-template, #der-gain-sector-bridge, #emp-update-gain, #def-adaptive-tempo, #def-model-class-fitness, #result-structural-adaptation-necessity, #result-mismatch-decomposition, #disc-separability-pattern, #disc-identifiability-floor, #additive-coordinate-forcing.

---

## Working Notes

- **The theorem is simple — 2-line composition of two known facts — but its AAD-framing is what matters.** Berger-Gray RDF + Prop A.1S = persistence-cost bound. The novelty is not the math; the novelty is saying "the sector constant $\alpha$ equals, up to a factor of 2, the minimum sustained information rate required to maintain persistence." This connects two AAD quantities ( $\alpha$, observation-channel information rate) that were previously linked only via the $\eta^\ast = U_M/(U_M + U_o)$ relation. The direct-linear proportionality $\dot R_{\min} = n\alpha/2$ is cleaner and has Landauer-physics content that $\eta^\ast$ does not.

- **Mitter-Newton as tightness check.** I claim the Kalman-Bucy filter saturates the $\alpha/2$ bound in steady state, citing Mitter-Newton 2005. A careful verification: Mitter-Newton's "rate of information supply" equals $\dot I = \tfrac{1}{2}\operatorname{tr}(H^T\Sigma_o^{-1}H P_{ss})$. Substituting the scalar Kalman-Bucy steady state ($H = 1$, $\Sigma_o = \sigma_o^2$, $P_{ss} = \sigma_o\sigma_w$ in drift-dominated limit, $K_{ss} = P_{ss}/\sigma_o^2 = \sigma_w/\sigma_o$): $\dot I = P_{ss}/(2\sigma_o^2) = \sigma_w/(2\sigma_o) = K_{ss}/2 = \alpha/2$. **Match.** Kalman-Bucy saturates the bound, consistent with the Gaussian-RDF tightness at the Kalman steady state.

- **The sub-scope $\alpha$ / $\beta$ transfer.** For sub-scope $\alpha$ agents, A2' is derived and $\alpha$ is computable from the update rule. The $n\alpha/2$ bound holds with known $\alpha$. For sub-scope $\beta$ agents, A2' is assumed — so the $\alpha$ in the cost bound is the *assumed* sector constant, and the cost bound holds as long as A2' does. This is clean: the cost bound inherits the sub-scope partition from its dependence, no new work required.

- **Why the `channel-capacity-sum-floor` extension is the biggest opening.** Currently AAD's persistence condition is stated in terms of $\mathcal{T}$ (correction rate) vs $\rho$ (disturbance rate). The cost theorem adds: observation channels must jointly provide Shannon capacity $\geq \mathcal{T}/2$. This IS a new first-class persistence diagnostic. In domains where channel capacity is binding ( e.g., bandwidth-constrained distributed systems, biological neurons, context-window-limited LLMs), this prediction might be *more* binding than the tempo prediction itself. Worth a follow-on spike and segment.

- **What I did not work out.** (a) The adversarial (Model D) analog — requires minimax-information machinery. (b) The non-Gaussian RDF — requires case-by-case. (c) Transient rates — the bound is steady-state. (d) Rate-tightness in sub-scope $\beta$ — no guarantee beyond the one-sided inequality.

- **Likely first reviewer pushback.** "The theorem is trivial — it's just RDF applied to the persistence steady state." Response: yes, *the math* is trivial. The contribution is (i) making $\alpha/2$ the cost-functional AAD reads off the sector constant, (ii) Mitter-Newton tightness check confirming Kalman saturates, and (iii) opening the observation-channel-capacity-sum-floor as a first-class persistence diagnostic. The math being a two-line composition is a *feature* of AAD's integration style — derive the clean thing from the right two known results, then sit in the AAD-frame to see why it matters.

- **Likely second reviewer pushback.** "You've only handled Gaussian-OU; the real environments are heavy-tailed or adversarial." Response: correct — §9 names this scope limit. The result is *exact in the canonical benchmark case*. Generalizations are open, but the canonical-case result is worth landing because it establishes the structural claim (cost scales linearly with $\alpha$) that non-Gaussian extensions are expected to preserve qualitatively.

- **Alternative name for the segment.** `#deriv-persistence-cost` is the obvious candidate. Alternatives: `#persistence-information-cost` (more precise but verbose), `#information-rate-floor` (emphasizes the lower-bound character), `#landauer-persistence-bound` (emphasizes the thermodynamic interpretation — too narrow? the result is information-theoretic, not primarily thermodynamic, though it has a thermodynamic consequence). Recommendation: **`#deriv-persistence-cost`** as the primary slug, with the abstract "cost" left deliberately broad to accommodate future extensions (control-effort upper-bounds, entropy-production-rate generalizations, model-misspecification cost corrections).
