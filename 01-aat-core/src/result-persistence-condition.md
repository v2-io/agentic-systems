---
slug: result-persistence-condition
type: result
status: exact
depends:
  - def-adaptive-tempo
  - def-mismatch-signal
  - result-sector-condition-stability
  - result-sector-persistence-template
stage: claims-verified
---

# Result: Persistence Condition

This is the volume's **central inequality** in its operational form, stated as two conditions with different mechanisms and different remedies. The split is control engineering's distinction between *stability* and *performance* (in robust control, nominal and robust stability versus nominal and robust performance; Skogestad & Postlethwaite 2005, Zhou, Doyle & Glover 1996). What this segment adds is the threshold carried uniformly across agent classes, its class-level tightness, and its price in information rate.

**Structural persistence** is the Lyapunov-derived condition that the correction machinery contains mismatch within its operating region: $\alpha \gt \rho/R$ under deterministic bounded disturbance, or $\alpha \gt n\sigma_w^2/(2R^2)$ under stochastic disturbance. This says *the machinery works*. The estimation error is ultimately bounded by $R^\ast = \rho/\alpha$ under Model D; under Model S its RMS scale, counted only while it is still inside the region, is at most $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)}$, and the certificate itself holds for an expected time that grows like $e^{\kappa_R}$, $\kappa_R = \alpha R^2/\sigma_w^2$, which at the threshold is about one correction time ( #deriv-sector-condition Prop A.1S-τ). When this inequality fails, the containment *certificate* is lost — escape from the operating region becomes possible, and for correctors whose sector bound is tight (the linear case) it is forced by adversarial disturbance in finite time. The loss of the certificate is a qualitative regime transition, not a gradual degradation; what condition-failure does not do is certify escape for every corrector, since the sector floor can understate correction along the actually-reachable paths ( #deriv-sector-condition Lemma A.1N).

**Task adequacy** is the separate condition that the steady-state mismatch is small enough for the agent's actions to remain useful: $R^\ast \lt \lVert\delta_{\text{critical}}\rVert$, where the critical-mismatch threshold is a *domain-specific tolerance* — how wrong can the model be before the agent's actions become harmful or ineffective? Set by the application, not derived by AAT. The two conditions are independent: an agent can be structurally persistent but task-inadequate (the machinery contains mismatch but not tightly enough for the domain). The remedies differ — task inadequacy can be fixed by raising tempo through more or better observations, lowering disturbance, or relaxing tolerance; structural failure requires changing the correction architecture entirely. Under Model S with white channel noise, raising the gain on the same observations is not a remedy past the Kalman gain; under Model D it lowers the bound toward the channel-noise floor $\bar\nu$ and never below it ("Gain and information are different levers" below).

When the linear ODE applies (sector parameter equals tempo, valid region is unbounded), structural persistence is automatically satisfied and the binding condition is just task adequacy: $\mathcal{T} \gt \rho / \lVert\delta_{\text{critical}}\rVert$ under Model D. This is the form most downstream applications cite. With $\rho$ the total disturbance it is exact; written in the environmental part alone, with channel noise bounded by $\bar\nu$, it reads $\mathcal T \gt \rho_{\text{env}}/(\lVert\delta_{\text{critical}}\rVert - \bar\nu)$ and needs $\lVert\delta_{\text{critical}}\rVert \gt \bar\nu$: a tolerance tighter than the channel noise is met by no tempo. It is the tracking analysis of adaptive filtering: a lag error that falls with the adaptation rate, compared against a tolerance (Widrow et al. 1976). That literature's linear filters have no validity region $R$, so it has a bound and a step-size trade-off but no structural threshold. The threshold with $R$, and what happens when it fails, is where this segment goes past it. It is exact for linear correction and a useful proxy for mildly nonlinear correction (where $\alpha \approx \mathcal{T}$), but overstates persistence when correction saturates.

A consequence the framework emphasizes: **the persistence condition is a structural pattern that recurs across domains rather than a model of any one of them**. The same inequality — correction rate against disturbance rate, normalized by tolerance — governs a Kalman filter on a moving target, an organization adapting to market shifts, an immune system tracking a pathogen, a developer keeping pace with a codebase, an organism evolving against environmental change. The structure recurs because the *math* recurs; whether the specific mechanism (tempo limited by some particular bottleneck) is the *dominant* cause in any given empirical case is left as an open empirical question per domain. The two-condition decomposition specifically prevents one common category error in domain transfer: a structurally-persistent codebase team can be task-inadequate, and conflating the two would yield the wrong intervention.

A complementary cost shadow: persistence has a *price*, not just a threshold. Under stochastic disturbance, holding the estimation error at a given level requires sustained Shannon information acquisition at a rate that level fixes; no causal estimator pays less, and the Kalman–Bucy filter pays exactly that, $n\alpha/2$ nats per unit time at its correction rate $\alpha$ — a Landauer-analog floor (see #deriv-persistence-cost). Every linear corrector on the same channel takes in that same rate; a mis-tuned one gets a larger error for it. The threshold says whether persistence is *possible*; the information-rate corollary says what it *costs*. Two agents with identical persistence guarantees can face very different sustained demands because the cost scales with the correction rate the error requires; the threshold alone cannot distinguish dormant from running-hot.

A per-dimension extension addresses anisotropy: when correction capacity varies across dimensions, the scalar condition can overestimate persistence margin substantially (up to 72% in simulation). The correct condition is per-dimension; under cross-dimensional correction the canonical sharp form is the matrix-Loewner persistence condition ( #deriv-matrix-persistence-condition).

## Formal Expression

This segment is the canonical single-agent instantiation of the sector-persistence template ( #result-sector-persistence-template) with state variable $\xi = \bar\delta$, the estimation error of #def-mismatch-signal (not the observed innovation, which carries channel noise no correction removes), correction function $F(\mathcal{T}, \delta)$, and disturbance rate $\rho_\xi = \rho$: environmental change plus the channel noise the correction feeds back ( #deriv-sector-condition, Setup). Throughout, $\delta$ in these conditions denotes $\bar\delta$. Structural persistence is the direct template conclusion. Task adequacy adds a domain-specific constraint beyond the template's reach.

### Structural Persistence

*[Derived (structural-persistence, from sector-persistence-template)]*

Applying the template to the single-agent epistemic case gives: the correction machinery is guaranteed to bound $\delta$ within the model class capacity when

$$\alpha \gt \frac{\rho}{R} \quad \text{(Model D)} \qquad \alpha \gt \frac{n\sigma_w^2}{2R^2} \quad \text{(Model S)}$$

Each condition is sufficient for the individual agent and tight at class level (necessary for the uniform guarantee over all correctors with the given sector floor; agent-level necessary exactly under a radially tight sector bound — the linear case). See #deriv-sector-condition Lemma A.1N.

with ultimate bound $R^\ast = \rho/\alpha$ (Model D) or RMS scale $R^\ast_S = \sigma_w\sqrt{n/(2\alpha)}$ (Model S). See #result-sector-condition-stability for how (T1)–(T3) are verified in this instantiation, and #deriv-sector-condition for the proof. Structural persistence is a property of the adaptive architecture — the machinery's ability to contain mismatch — not of the task. The two conditions certify different things. Under Model D the region is positively invariant: once inside, forever. Under Model S the condition is $\kappa_R \gt n/2$ with $\kappa_R = \alpha R^2/\sigma_w^2$, and it certifies the scale of the error counted only while the agent is still inside the region (the killed moment, not the moment conditional on being inside) together with an expected stay there of about one correction time; the expected stay grows like $e^{\kappa_R}$ with margin, and a lifetime $L$ with exit probability at most $\epsilon$ costs margin in $\kappa_R$ of order $\log(L/\epsilon)$ ( #deriv-sector-condition Prop A.1S-τ).

**The Model S condition as a window in the gain.** *[Derived (linear correction, Model S, white channel noise; #deriv-sector-condition Setup)]* With the channel noise the correction injects, $\sigma_w^2 = \sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2$, the condition $\alpha \gt n\sigma_w^2/(2R^2)$ is a quadratic in $\alpha$:

$$n\sigma_\nu^2\alpha^2 - 2R^2\alpha + n\sigma_{\text{env}}^2 \lt 0 \quad\Longleftrightarrow\quad \alpha \in (\alpha_-, \alpha_+), \qquad \alpha_\pm = \frac{R^2 \pm \sqrt{R^4 - n^2\sigma_{\text{env}}^2\sigma_\nu^2}}{n\sigma_\nu^2}.$$

Three consequences follow. *Feasibility:* some gain satisfies the condition iff $R^2 \gt n\sigma_{\text{env}}\sigma_\nu$, that is, iff the Kalman–Bucy error fits inside the region; if it does not, no gain persists in mean square however the agent is tuned. *A window, not a threshold:* too low a gain fails by lag, as before, and too high a gain fails by the channel noise its own correction injects. *Geometric about the Kalman gain:* $\alpha_-\alpha_+ = \sigma_{\text{env}}^2/\sigma_\nu^2 = K^2$ and $\ln(\alpha_+/K) = \operatorname{arccosh}\big(R^2/(n\sigma_{\text{env}}\sigma_\nu)\big)$, so the ratio of the region to the optimal error sets how far, in log-gain, an agent can be mis-tuned and still persist. The exit exponent $\kappa_R(\alpha) = \alpha R^2/\sigma_w^2(\alpha)$ peaks at $K$ with $\kappa_R(K) = R^2/(2\sigma_{\text{env}}\sigma_\nu)$, and the feasibility condition is $\kappa_R(K) \gt n/2$. Under Model D with channel noise bounded by $\bar\nu$ the condition $\alpha R \gt \rho_{\text{env}} + \alpha\bar\nu$ becomes $\alpha(R - \bar\nu) \gt \rho_{\text{env}}$: a lower threshold with no upper end, which needs $R \gt \bar\nu$ (a condition no gain can meet otherwise), with adaptive reserve $\alpha(R - \bar\nu) - \rho_{\text{env}}$. Task adequacy takes the same forms with $\lVert\delta_{\text{critical}}\rVert$ in place of $R$. (Checked against a grid of $\alpha$ at three region sizes: analytic window to four places, $\alpha_-\alpha_+ = K^2$, log half-width equal to the arccosh.)

**Linear case.** When $F(\mathcal{T}, \delta) = \mathcal{T}\delta$, $\alpha = \mathcal{T}$ and $R \to \infty$, so structural persistence is trivially satisfied whenever $\mathcal{T} \gt 0$. The binding constraint then becomes task adequacy (below).

### Task Adequacy

*[Definition (task-adequacy)]*

The steady-state mismatch is small enough for the agent's actions to remain acceptable:

$$R^\ast \lt \lVert\delta_{\text{critical}}\rVert$$

where $\lVert\delta_{\text{critical}}\rVert$ is a domain-specific tolerance threshold — "how wrong can the model be before the agent's actions become harmful or ineffective?" This is set by the application domain, not derived by AAT.

**Task adequacy is a separate condition from structural persistence.** An agent can be structurally persistent ($R^\ast \lt R$) but task-inadequate ($R^\ast \gt \lVert\delta_{\text{critical}}\rVert$) — the machinery contains mismatch, but not tightly enough for the domain's needs. Conversely, when $\lVert\delta_{\text{critical}}\rVert \lt R$ (the domain's tolerance is stricter than the model class capacity), task adequacy is the binding constraint.

### Operational Persistence Condition

*[Derived (operational-persistence, conjunction of structural persistence + task adequacy)]*

The agent persists operationally when BOTH conditions hold. In the nonlinear case with $\lVert\delta_{\text{critical}}\rVert \lt R$, the binding condition is:

$$\alpha \gt \frac{\rho}{\lVert\delta_{\text{critical}}\rVert} \quad \text{(Model D)} \qquad \alpha \gt \frac{n\sigma_w^2}{2\lVert\delta_{\text{critical}}\rVert^2} \quad \text{(Model S)}$$

These are the same as the structural conditions with $R$ replaced by $\lVert\delta_{\text{critical}}\rVert$, because when $\lVert\delta_{\text{critical}}\rVert \lt R$, task adequacy is stricter.

**Linear operational forms:** In the linear case ($\alpha = \mathcal{T}$, $R \to \infty$), structural persistence is trivially satisfied and the operational condition reduces to task adequacy alone:

$$\mathcal{T} \gt \frac{\rho}{\lVert\delta_{\text{critical}}\rVert} \quad \text{(Model D)} \qquad \mathcal{T} \gt \frac{n\sigma_w^2}{2\lVert\delta_{\text{critical}}\rVert^2} \quad \text{(Model S)}$$

These are the forms used throughout the theory as the operational persistence condition. They are exact for linear correction and useful proxies for mildly nonlinear correction (where $\alpha \approx \mathcal{T}$), but they overstate the persistence margin when the correction function saturates, because they omit the structural constraint ($\alpha \gt \rho/R$) that becomes binding when $R$ is finite.

**Per-dimension (Model S):** $\eta_k \gt c \cdot \rho_k^2 / \delta_{\text{critical},k}^2$ where $c$ depends on the probability guarantee. See #result-per-dimension-persistence.

### The relationship between $\alpha$ and $\mathcal{T}$

#der-gain-sector-bridge shows that for agents with directional fidelity, $\alpha = \nu \cdot \eta^\ast \cdot c_{\min}$ (per time), where $c_{\min}$ is the worst-case directional fidelity. For linear correction at the optimal gain (Kalman, Beta-Bernoulli), $\alpha = \mathcal{T}$ exactly; a linear corrector tuned away from the optimum has $\alpha \neq \mathcal T$ (below). For gradient descent on strongly convex losses, $\alpha = \eta \cdot \mu$ where $\mu$ is the strong convexity modulus — monotone in $\eta$ (and hence in $\mathcal{T}$) for fixed loss landscape. For nonlinear correction tested in simulation (saturating, sigmoid, threshold), $\alpha$ remains monotone increasing in $\mathcal{T}$: for a saturating function with capacity $R$, $\alpha \approx \mathcal{T}/2$ (worst case at the capacity boundary); for sigmoid (tanh), $\alpha \approx 0.76 \cdot \mathcal{T}$. So a faster correction is a stronger correction. Whether it leaves a smaller error depends on which lever raised it.

### Gain and information are different levers

*[Derived (lag/noise trade-off, linear correction, Model S with white channel noise; #deriv-sector-condition Setup)]*

A faster correction can come from a larger gain on the same observations or from more information (more events, or more informative ones), and the two act on the bound differently once the channel is noisy. The update is driven by the innovation, so each correction also feeds a share of the channel noise into the estimation error. For linear correction at rate $\alpha$ under Model S, with environmental diffusion $\sigma_{\text{env}}$ and channel-noise intensity $\sigma_\nu$, the steady-state mean-square estimation error is

$$\mathbb{E}\lVert\bar\delta\rVert^2_{ss} = \frac{n(\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)}{2\alpha}$$

- **Raising the gain on fixed observations** moves $\alpha$ along this curve. The error is smallest at $\alpha = \sigma_{\text{env}}/\sigma_\nu$, the Kalman–Bucy gain, where the lag and noise contributions are equal. Above it, faster correction enlarges the error. Tempo $\mathcal T = \nu\eta^\ast$ is defined with the *optimal* gain ( #def-adaptive-tempo; #emp-update-gain, whose $\eta^\ast$ is this optimum), so a gain past the optimum is miscalibration: it moves the correction rate $\alpha$, not $\mathcal T$, and reaches $\mathcal T$ only through a mis-estimated $U_M$ or $U_o$. For a Bayes-optimal agent there is nothing to gain by raising it.
- **Raising the event rate $\nu$**, with the same per-event noise, adds information. The channel-noise intensity falls as $\sigma_\nu^2 \propto 1/\nu$, and the minimum error $n\sigma_{\text{env}}\sigma_\nu$ falls with it. The same holds for any change that makes observations more informative. This is the lever that raises $\mathcal T$.

So "faster adaptation improves persistence" is true of tempo raised by information and false of a gain raised past the optimum on a fixed channel. For the expected time in the region the gain fails sooner: its exponent is capped at the Kalman gain, and the stay itself is largest at a gain below the Kalman gain, so a fixed channel bounds the stay any tuning can buy ( #deriv-sector-condition Prop A.1S-τ). This is a Model S fact about white channel noise, which a stronger correction passes to the error at a variance growing with the gain. Under Model D the picture differs: with channel noise bounded by $\bar\nu$ the bound is $R^\ast = \rho_{\text{env}}/\alpha + \bar\nu$, tight (constant disturbances attain it) and decreasing in $\alpha$ toward the floor $\bar\nu$, which more events do not lower; there the gain lever helps monotonically and the information lever does nothing to the worst case. Throughout this segment $\rho$ and $\sigma_w$ denote the total disturbance, and the forms $R^\ast = \rho/\alpha$ and $\sigma_w\sqrt{n/(2\alpha)}$ are exact in them; read with the environmental part alone they are the lag terms. The trade-off is the lag/noise trade-off of adaptive filtering (Widrow et al. 1976) and the bias–variance trade-off of the gain; the Kalman gain is its optimum. Within the framework, #obs-gated-tempo-advantage observed the same mechanism in the adversarial setting (noise on the observation channel degrades the advantage of a higher gain, and the Riccati gain only partly restores it); the single-agent steady state here is its derivation.

### Per-Dimension Extension

*[Derived (per-dimension-persistence, per-dimension Lyapunov under Model D / AR(1) stationary distribution under Model S — see #result-per-dimension-persistence)]*

For anisotropic systems (non-uniform $\rho$ or $\mathcal{T}$ across dimensions), the scalar persistence condition is insufficient. Per-dimension:

$$\mathcal{T}_k \gt \frac{\rho_k}{\delta_{\text{critical},k}} \quad \text{for each dimension } k$$

The scalar condition overestimates by up to 72% in simulation. The weak dimension is the bottleneck (84% of total mismatch in simulation). See #result-per-dimension-persistence.

**Robustness**: The per-dimension condition matches discrete AR(1) prediction to 4 significant figures. The scalar overestimate is a consequence of Jensen's inequality applied to the norm.

## Epistemic Status

**Structural persistence** thresholds are *exact* under their stated assumptions: Model D gives $\alpha \gt \rho/R$ (Prop A.1, exact under GA-2, GA-3); Model S gives $\alpha \gt n\sigma_w^2/(2R^2)$ (Prop A.1S, exact under GA-2S, GA-3), a condition on the certified scale whose guaranteed duration at threshold is about one correction time (Prop A.1S-τ, exact). The gain window and its feasibility condition are exact for linear correction with white channel noise. Both thresholds are sufficiency results with class-level tightness — no fixed-agent only-if is claimed; agent-level necessity holds exactly in the radially tight (e.g. linear) case ( #deriv-sector-condition Lemma A.1N). The threshold's *existence* is *robust qualitative* — any monotone correction function has a capacity limit; this holds across all correction functions tested.

**Task adequacy** ($R^\ast \lt \lVert\delta_{\text{critical}}\rVert$) is *exact as a definition* — given $R^\ast$ (derived) and $\lVert\delta_{\text{critical}}\rVert$ (domain parameter), the comparison is well-defined. The substance lies in estimating $\lVert\delta_{\text{critical}}\rVert$ for specific domains, which is an operationalization question ( #detail-operationalization), not a theory question.

**The linear operational forms** ($\mathcal{T} \gt \rho/\lVert\delta_{\text{critical}}\rVert$ for Model D; $\mathcal{T} \gt n\sigma_w^2/(2\lVert\delta_{\text{critical}}\rVert^2)$ for Model S) are *exact* for linear correction (where they express task adequacy alone, structural persistence being trivially satisfied) and *useful approximations* for mildly nonlinear correction (where $\alpha \approx \mathcal{T}$). For strongly nonlinear correction, the general $\alpha$-forms are required and BOTH structural and task-adequacy conditions must be checked. Downstream segments that use the linear operational forms should be understood as expressing task adequacy, not structural stability.

**Gain versus information** is *exact* for linear correction under Model S with white channel noise: the steady state $n(\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)/(2\alpha)$ is Prop A.1S with the gain-injected noise included, and its minimum is the Kalman–Bucy error variance (checked by simulation of the scalar case against the closed form, twice, with different discretizations). For nonlinear correction the gain-injected fluctuation scales with the gain for every mismatch transform ( #deriv-gain-sector Prop B.3), so the noise term grows while the lag term falls; the U-shape and the location of its minimum are derived here only for linear correction. The Model D statement is exact and tight (constant disturbances attain the bound).

The per-dimension extension is *exact conditional on the disturbance model* ( #result-per-dimension-persistence): the Model D per-dimension threshold ($\mathcal{T}_k \gt \rho_k/\delta_{\text{critical},k}$) is exact by the same Lyapunov argument applied per dimension (GA-2, GA-3), and the Model S per-dimension thresholds are exact under the AR(1) stationary distribution (GA-2S), with simulation confirming the AR(1) prediction to 4 significant figures.

## Claim Record

### Under a sector condition on a region, correction that outpaces disturbance relative to the region certifies containment against bounded disturbance and a certified scale against white-noise disturbance

**Register:** formal — the template conclusion of #result-sector-persistence-template with $\xi = \bar\delta$ (Formal Expression, "Structural Persistence"; proofs in #deriv-sector-condition Prop A.1, Prop A.1S and Lemma A.1N). Sufficient for every corrector in the population; necessary only for the uniform guarantee over all correctors with sector floor $\alpha$, and for a fixed corrector only when its sector bound is radially tight.

**Population:** representations $\dot{\bar\delta} = -F(\mathcal T, \bar\delta) + w$ with $F$ meeting (A1), (A2') on $\mathcal B_R$ with floor $\alpha$, and (A3), started inside $\mathcal B_R$, under a disturbance that is either bounded in norm by the total rate $\rho$ (Model D, GA-2) or additive isotropic Brownian with per-coordinate intensity $\sigma_w$ (Model S, GA-2S, with the regularity (S) of #deriv-sector-condition). $\rho$ and $\sigma_w$ are the total disturbance, including the channel noise the correction injects (#deriv-sector-condition, Setup). Under Model S what is certified is the scale of the killed second moment and an expected stay of about one correction time at threshold, not containment.

**True of:** the linear corrector $F = \alpha\bar\delta$ under a constant disturbance of norm $\rho$ with $\alpha R \gt \rho$: the error settles at exactly $\rho/\alpha$ inside $\mathcal B_R$, so the bound is attained (Prop A.1). Under Model S, the Ornstein–Uhlenbeck benchmark at the threshold $\kappa_R = n/2$: killed moment at most $n\sigma_w^2/(2\alpha)$, and expected stay from the origin $\alpha\Phi(0) = 0.60$ correction times at $n = 1$ (#deriv-sector-condition Lemma A.1S-τ.0, by derivation).

**False of:** pathwise containment under Model S, for every corrector at every $\alpha$: exit is certain (#deriv-sector-condition Cor A.1S.1), so "once inside, forever" is a Model D sentence only. Certified escape below threshold for a general corrector: the dip corrector of the Remark after Lemma A.1N ($R = \rho = 1$, floor $0.1$) fails the condition tenfold and, started at the origin, never leaves a ball of radius about $0.1$. Outside the population: a corrector whose sector bound breaks down inside $\mathcal B_R$, and a trajectory that starts outside $\mathcal B_R$.

**Falsifier:** a corrector meeting (A1), (A2') on $\mathcal B_R$ and (A3) under $\lVert w(t)\rVert \leq \rho$ with $\alpha R \gt \rho$, started in $\mathcal B_R$, whose error leaves $\mathcal B_R$; it would refute "Under Model D the region is positively invariant: once inside, forever" (Formal Expression, after the Structural Persistence display). For class-level tightness: some $\alpha \lt \rho/R$ at which the extremal corrector $\alpha\bar\delta$ stays in $\mathcal B_R$ under every disturbance bounded by $\rho$, which would refute "tight at class level".

**Instantiated:** not applicable.

### Under white channel noise the Model S condition is a window of gains about the Kalman gain, and no gain satisfies it unless the Kalman–Bucy error fits inside the region

**Register:** formal — the quadratic in $\alpha$ of Formal Expression, "The Model S condition as a window in the gain" (tag *[Derived (linear correction, Model S, white channel noise)]*).

**Population:** linear correctors $F = \alpha\bar\delta$ valid on $\mathcal B_R$, under Model S, whose total disturbance is environmental diffusion plus white channel noise passed through the gain, $\sigma_w^2 = \sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2$. Task adequacy takes the same form with $\lVert\delta_{\text{critical}}\rVert$ in place of $R$.

**True of:** $n = 1$, $\sigma_{\text{env}} = 1$, $\sigma_\nu = 0.5$ (so $K = 2$), $R^2 = 1$: the window is $(0.536, 7.464)$, its endpoints multiply to $K^2 = 4$, and $\ln(\alpha_+/K) = \operatorname{arccosh} 2 = 1.317$; at $R^2 \leq 0.5$ the same channel has no window (by derivation from the closed form, which the window paragraph reports checking against a grid of gains).

**False of:** Model D with channel noise bounded by $\bar\nu$, where the condition is $\alpha(R - \bar\nu) \gt \rho_{\text{env}}$, a lower threshold with no upper end that needs $R \gt \bar\nu$ (same paragraph). Nonlinear correction: the injected fluctuation still grows with the gain (#deriv-gain-sector Prop B.3), but the window's form and location are derived only for linear correction (Epistemic Status, "Gain versus information"). Channel noise that is not white, such as a bias shared by every reading, is outside the population.

**Falsifier:** a linear corrector on such a channel that meets the mean-square condition at a gain outside $(\alpha_-, \alpha_+)$, or at any gain while $R^2 \leq n\sigma_{\text{env}}\sigma_\nu$; either refutes "some gain satisfies the condition iff $R^2 \gt n\sigma_{\text{env}}\sigma_\nu$" (*Feasibility*, same paragraph).

**Instantiated:** not applicable.

### Faster adaptation improves persistence when the tempo comes from more information, and not when it comes from a gain raised past the optimum on the same observations

**Register:** formal — Formal Expression, "Gain and information are different levers" (tag *[Derived (lag/noise trade-off, linear correction, Model S with white channel noise)]*); the Model D contrast in its last paragraph is exact and tight.

**Population:** linear correctors under Model S with white channel noise; the information lever is stated for per-event noise that is independent across events, so that $\sigma_\nu^2 \propto 1/\nu$. Under Model D with channel noise bounded by $\bar\nu$ the roles reverse: the gain lowers the bound monotonically toward $\bar\nu$, and more events do nothing to the worst case.

**True of:** the scalar Kalman–Bucy filter on a random walk: steady-state error $n(\sigma_{\text{env}}^2 + \alpha^2\sigma_\nu^2)/(2\alpha)$, smallest, at $n\sigma_{\text{env}}\sigma_\nu$, at $\alpha = K$ (simulated against the closed form twice, Epistemic Status). On the same channel the expected stay is largest below $K$: with $\sigma_{\text{env}} = 1$, $\sigma_\nu = 0.5$, $n = 1$, $R = 1$, $\Phi(0) = 1.07$ at $0.5K$ against $0.72$ at $K$ (#deriv-sector-condition, "The exit exponent is capped at the Kalman gain").

**False of:** Model D, as above. Noise that does not average across events (a shared bias, or Model D's bounded floor): more events do not lower it. A corrector whose gain is below its optimum: there a larger gain on the same observations does shrink the error, so the bullet "Above it, faster correction enlarges the error" holds for gains above $K$ only, as written.

**Falsifier:** a linear corrector under white channel noise whose steady-state error falls as its gain is raised past $\sigma_{\text{env}}/\sigma_\nu$, or independent per-event noise for which raising $\nu$ does not lower the minimum error; either refutes the two bullets of "Gain and information are different levers".

**Instantiated:** not applicable. #obs-gated-tempo-advantage, which the body credits with the same mechanism, simulates the theory's own equations.

### Task adequacy compares the certified error with a domain tolerance, and the linear operational form is exact for linear correction

**Register:** formal — task adequacy is a definition (*[Definition (task-adequacy)]*); the linear operational forms are exact for linear correction (Epistemic Status, "The linear operational forms").

**Population:** for exactness, linear correctors with $\alpha = \mathcal T$, which holds at the optimal gain ("The relationship between $\alpha$ and $\mathcal T$"), with $\rho$ and $\sigma_w$ the total disturbance. With the environmental rate alone and channel noise bounded by $\bar\nu$, the Model D form is $\mathcal T \gt \rho_{\text{env}}/(\lVert\delta_{\text{critical}}\rVert - \bar\nu)$ and needs $\lVert\delta_{\text{critical}}\rVert \gt \bar\nu$. A linear corrector tuned away from its optimum has $\alpha \neq \mathcal T$, and the form must be read in $\alpha$.

**True of:** a linear corrector with $\alpha = \mathcal T$ under a constant disturbance of norm $\rho$: the error settles at $\rho/\mathcal T$, so the form is exact and attained.

**False of:** a saturating corrector with finite capacity $R$: the linear form omits $\alpha \gt \rho/R$ and overstates the margin (Formal Expression, after the linear operational display). Mildly nonlinear correctors are covered as a proxy ($\alpha \approx \mathcal T$) with no stated tolerance.

**Falsifier:** for the definition, none. For exactness, a linear corrector at its optimal gain under $\lVert w\rVert \leq \rho$ whose ultimate error exceeds $\rho/\mathcal T$.

**Instantiated:** not applicable.

### The split into structural persistence and task adequacy routes a failure to its remedy

**Register:** normative — the opening's "The remedies differ — task inadequacy can be fixed by raising tempo through more or better observations, lowering disturbance, or relaxing tolerance; structural failure requires changing the correction architecture entirely", and Discussion, "Below task-adequacy threshold". It is tested by comparing remedies on failures classified by which condition fails.

**Population:** adaptive systems whose failure the body classifies as structural ($\alpha R \leq \rho$, or a Model S gain outside its window) or as task inadequacy ($R \gt R^\ast \gt \lVert\delta_{\text{critical}}\rVert$).

**True of:** a model class whose capacity is the binding limit, $\rho \gt \alpha R$ at every gain the class admits: no retuning or added information within the class restores the certificate, and only a class with a larger $R$ does, the case #result-structural-adaptation-necessity treats.

**False of:** the segment's own window. A linear corrector on a noisy channel with gain above $\alpha_+$ fails structural persistence under Model S, and lowering its gain on the same architecture restores it; one with $R^2 \leq n\sigma_{\text{env}}\sigma_\nu$ is restored by better observations, which the body lists as a task-adequacy remedy. Under Model D a corrector with $\alpha R \leq \rho$ is restored by raising $\alpha$ where the architecture allows it. The sentence "structural failure requires changing the correction architecture entirely" is therefore false of retunable gains and of added information.

**Falsifier:** the comparison, on failures classified by condition, of the routed remedy against the others; the window instances above already supply it for structural failure.

**Instantiated:** no.

### The same inequality governs a Kalman filter, a development team, an organization, an immune system and an evolving organism

**Register:** descriptive — the opening's "a structural pattern that recurs across domains", INTRODUCTION headline 1 ("that it is one inequality and not an analogy among three is itself the result"), and the Findings Brief and Impact. The formal half, that every representation meeting the hypotheses obeys one inequality, is the first entry; this entry is the claim that the named real classes meet the hypotheses.

**Population:** the named real classes, each claimed to carry an error state with a sector-bounded correction on a region and a disturbance of Model D or Model S. The body leaves open, per domain, whether "the specific mechanism … is the dominant cause in any given empirical case".

**True of:** the Kalman filter on a moving target, where linear correction, white channel noise and the disturbance law are built in (the tracking analysis of Widrow et al. 1976 and Guo & Ljung 1995). #example-kalman is an internal consistency check, not an instance.

**False of:** the body names none. Two neighbours fall outside the hypotheses: systems that cross the threshold at different values in each direction, whose correction depends on history, and agents whose disturbance rises with their own correction effort, against the fixed $\rho$ the conditions assume. Heavy-tailed shocks are outside both disturbance models (#deriv-sector-condition, "Two disturbance models").

**Falsifier:** for a named domain, estimates of $\alpha$, $R$ and $\rho$ from the error process under which the error ultimately exceeds $\rho/\alpha$ while $\alpha R \gt \rho$, or the sector bound fails on the region; either shows that domain does not meet the hypotheses and refutes "governs" for it. The estimators from innovation data that such a measurement needs are not yet written ( #detail-operationalization).

**Instantiated:** no, for every class the theory did not build.

### Every monotone correction function has a capacity limit, so the threshold exists

**Register:** descriptive — Epistemic Status: "The threshold's *existence* is *robust qualitative* — any monotone correction function has a capacity limit; this holds across all correction functions tested."

**Population:** real correctors. Read as a statement about functions it does not hold, since the linear corrector is monotone with $R \to \infty$ (Formal Expression, "Linear case").

**True of:** the saturating, sigmoid and threshold correction functions of the Part I simulations (#obs-section-i-validation-simulations), which are the theory's own equations.

**False of:** $F = \mathcal T\bar\delta$, by the segment's own linear case.

**Falsifier:** a real corrector, measured, whose sector floor does not shrink at any error size its world produces.

**Instantiated:** no.

## Discussion

**Two conditions, not one.** Structural persistence ($\alpha \gt \rho/R$) is the Lyapunov-derived result — it says the machinery *works*. Task adequacy ($R^\ast \lt \lVert\delta_{\text{critical}}\rVert$) is a domain-specific constraint — it says the machinery works *well enough*. This is the stability-versus-performance distinction of control engineering, and the ultimate bound $R^\ast$ is Khalil's ultimate bound; the adaptive reserve below is a disturbance stability margin. Neither implies the other, and downstream segments should specify which they mean. Most adversarial-dynamics results ( #result-adversarial-tempo-advantage, #der-adversarial-destabilization) depend on structural persistence. Most domain instantiations (TST, logogenic agent design) care about task adequacy. See Persistence in `LEXICON.md` and `README.md` for the full three-sense taxonomy (structural, operational, continuity).

**Below structural threshold.** When $\alpha \leq \rho / R$, the Lyapunov certificate is lost: the machinery can no longer guarantee containment within the operating region. For the extremal member of the sector class, and for any corrector whose sector bound is radially tight (the linear case), escape is forced by adversarial disturbance — so the threshold is a genuine qualitative transition, not a gradual degradation. For a general corrector, condition failure means loss of guarantee rather than certified escape: the floor $\alpha$ can understate the correction actually available along reachable paths ( #deriv-sector-condition Lemma A.1N).

**Model S containment is a different kind of guarantee.** Under stochastic disturbance the mean-square bound above is a fixed-time / distributional statement: by #deriv-sector-condition Corollary A.1S.1, exit from the persistence region is certain over an unbounded horizon for every sector-satisfying corrector and every $\alpha$ (contrast Model D's positive invariance under $\alpha R \gt \rho$), so in a genuinely stochastic environment eventual loss of the parametric certificate is generic, not exceptional (whether it forces model-class change is the open question of #sketch-structural-adaptation-genericity). How soon is Prop A.1S-τ: the expected stay is at least the OU benchmark's, exponential in $\kappa_R$, and about one correction time at the threshold. On a fixed channel the exponent is capped at the Kalman gain and the stay reachable by tuning the gain is bounded.

**Below task-adequacy threshold.** When $R^\ast \gt \lVert\delta_{\text{critical}}\rVert$ but $R^\ast \lt R$, the system is structurally stable but performing unacceptably. Mismatch is bounded but too large for the domain. The remedy is different from structural failure: increase $\mathcal{T}$ through more or better observations, decrease $\rho$ (reduce environmental volatility), or relax $\lVert\delta_{\text{critical}}\rVert$ (accept more mismatch). Structural failure requires changing the correction architecture entirely ( #result-structural-adaptation-necessity).

**$\delta_{\text{critical}}$ and $R$ are domain parameters, not theory outputs.** The theory derives the *existence* of persistence thresholds and their *form* (ratio of correction to disturbance). But the specific values are set by the application domain: $\delta_{\text{critical}}$ encodes "how wrong can the model be before the agent's actions become harmful or ineffective?" — this depends on the stakes, the action space, and the environment's forgiveness. $R$ encodes "how large a mismatch can the correction function handle before it saturates or breaks down?" — this depends on the model class and the correction architecture. See #detail-operationalization for guidance on estimating these quantities in specific domains.

**Channel independence and scalar tempo.** The linear operational forms use scalar $\mathcal{T}$, which inherits the channel-independence assumption from #def-adaptive-tempo: the additive formula overcounts when observation channels are correlated. In anisotropic systems the scalar condition also overestimates margins — up to 72% in simulation (see #def-adaptive-tempo, scalar vs. vector tempo). Where precision matters, the per-dimension condition ($\mathcal{T}_k \gt \rho_k / \delta_{\text{critical},k}$) should be used instead — and under cross-dimensional correction (off-diagonal $\mathcal{T}$ in the coordinate basis of $D_\delta = \mathrm{diag}(\delta_{\text{critical},k}^2)$), the matrix-Loewner form $\Sigma_\infty \prec D_\delta$ ( #deriv-matrix-persistence-condition) is canonical: per-coordinate is unsafe in that regime (gives a false-pass on persistence), while matrix-Loewner reads persistence correctly off the worst direction whether or not it aligns with a coordinate axis.

**Adaptive reserve.** The quantity $\Delta\rho^\ast = \alpha R - \rho$ (Prop A.2) measures how much additional disturbance the agent can absorb before persistence fails. In control terms it is a stability margin against disturbance ( #deriv-sector-condition, Prop A.2). Positive reserve means the agent has margin; zero reserve means it is at the threshold.

**Persistence has a cost, not just a threshold.** The inequality above says mismatch is bounded; it does not say what rate of effort the agent expends to hold that bound. #deriv-persistence-cost establishes the complementary *information-rate* bound: under Model S with a Gaussian-OU signal, holding the per-component mean-square estimation error at $D$ requires $\dot R \geq n(\sigma_{\text{env}}^2/(2D) - \lambda_s)$ nats/time for any causal estimator, and the Kalman–Bucy filter meets it with equality at rate $n\alpha/2$ — a Landauer-analog floor. Every linear corrector on the same channel takes in that rate; the bound is slack for a mis-tuned one, which pays the same for a larger error. The corollary for the optimal agent is a channel-capacity prerequisite $C \geq \mathcal{T}/2$ per dimension that the threshold condition alone does not name. Two agents with identical persistence guarantees can face very different sustained demands because the cost scales with the correction rate; the threshold alone cannot distinguish dormant from running-hot.

### Connections

The persistence condition appears in multiple downstream contexts:

- **Adversarial dynamics** ( #result-adversarial-tempo-advantage): Superlinear tempo advantage arises because persistence is a threshold — pushing an adversary below it causes qualitative collapse. *This connection is developed and validated in #result-adversarial-tempo-advantage and simulation variants A-D.*

- **Structural adaptation** ( #result-structural-adaptation-necessity): When model class fitness $\mathcal{F}(\mathcal{M}) \lt 1 - \varepsilon$, the effective $\alpha$ in the sector condition shrinks, eventually violating persistence. *This connection is developed in #result-structural-adaptation-necessity.*

- **Software maintainability** ( #der-code-quality-as-observation-infrastructure — cross-component reference, see `02-tst-core/`): *[Discussion]* A codebase may become "unmaintainable" when the development team's adaptive tempo falls below the rate of complexity accumulation. The vicious cycle would then be the persistence condition being violated through the agent's own prior actions degrading future $\mathcal{T}$ via $U_o$. *This connection is structurally motivated but not yet formally derived within AAT. It requires formalizing "complexity accumulation rate" as an instance of $\rho$.*

## Findings

### The Persistence Condition with Structural / Task-Adequacy Decomposition

**Brief:** An adaptive system's correction carries a guarantee when its correction strength beats the rate at which its world is changing, relative to how forgiving the world is. Against bounded change the guarantee is containment: once inside the region where correction works, the error stays there. Against random change it is weaker in kind: the error's typical size fits the region, and it stays for a while that margin lengthens, but it will eventually leave. Below the threshold the system doesn't merely degrade — it loses the guarantee, the way a balance held just barely beneath a tipping point is qualitatively different from one well above it, and for the simplest correctors a worst-case push does drive the error out. When the correction feeds back random noise from its own observations, correcting harder helps only up to a point, so the random-change condition becomes a window of correction strengths rather than a floor. The same inequality, with different inputs, governs whether a Kalman filter tracks a moving target, whether a development team keeps a codebase maintainable, and whether an organization keeps up with strategic change. The threshold itself decomposes into two distinct conditions — *structural persistence* (the machinery's correction rate can outpace disturbance) and *task adequacy* (the resulting steady-state mismatch is small enough for what the agent is trying to do). Conflating the two leads to category errors in domain transfer.

**Impact:** This is the framework's central inequality and the connection between control-theoretic Lyapunov stability analysis and the broader question of when any adaptive system — thermostat, software team, immune system, RL agent — can maintain coherent function under change. The two conditions carry the stability-versus-performance distinction into agent theory, where it routes a failure to its remedy: a structurally persistent team can be task-inadequate, and the remedies differ. The bound is on the estimation error, and its disturbance includes channel noise injected by the correction. Tempo raised by more information therefore tightens it, while gain raised past the optimum loosens it; under Model S the condition is a window of gains about the Kalman gain, satisfiable at all only if the Kalman error fits inside the region, and what it certifies at threshold is about one correction time of stay. The complementary information-rate bound from `#deriv-persistence-cost` shows the threshold has a sustained-cost shadow: two agents with identical persistence guarantees can face very different sustained demands.

**Novelty Claim:** *Claim synthesis* on the two-condition structure, which is the stability-versus-performance distinction of robust control (Skogestad & Postlethwaite 2005; Zhou, Doyle & Glover 1996), and on the linear operational form, which is the lag/noise tracking analysis of adaptive filtering (Widrow et al. 1976). What is ASF's: the threshold stated with a validity region $R$, which the linear tracking literature lacks, and used as one inequality across agent classes, from Kalman filtering through saturating correction to PID, with the derived/posited line between them drawn by sub-scope ( #form-sector-condition); its class-level tightness (Lemma A.1N in #deriv-sector-condition); the Model S containment dichotomy (Cor A.1S.1) and the exit-time comparison that gives it a clock (Prop A.1S-τ); the Model S gain window with its feasibility condition, which is the Widrow trade-off placed inside a threshold with a validity region; and the information-rate price of holding the bound ( #deriv-persistence-cost).

**Related Work:**

- Khalil 2002, *Nonlinear Systems* (3rd ed.), Prentice Hall — *formal antecedent* — chapters 4 and 9 supply the converse Lyapunov, ultimate boundedness, and sector-condition machinery the segment uses.
- Lyapunov 1892 / Khasminskii 2012 *Stochastic Stability of Differential Equations* — *formal antecedent* — the underlying Lyapunov stability tradition; Khasminskii's stopping-time localization underpins the Model S derivation.
- Rockafellar & Wets 1998, *Variational Analysis* — *formal antecedent* — supplies the monotone-operator machinery that underwrites the sector condition's strong-convexity equivalents.
- Skogestad, S. & Postlethwaite, I. 2005, *Multivariable Feedback Control: Analysis and Design* (2nd ed.), Wiley; Zhou, K., Doyle, J. C. & Glover, K. 1996, *Robust and Optimal Control*, Prentice Hall — *direct antecedent of the two-condition structure* — nominal/robust stability versus nominal/robust performance. Structural persistence is the stability half; task adequacy is the performance half with a domain tolerance as the performance specification.
- Widrow, B., McCool, J. M., Larimore, M. G. & Johnson, C. R. Jr. 1976, "Stationary and nonstationary learning characteristics of the LMS adaptive filter," *Proc. IEEE* 64(8):1151–1162, doi:10.1109/PROC.1976.10286 — *direct antecedent of the linear operational form and of the two levers* — misadjustment from gradient noise grows with the speed of adaptation, misadjustment from lag falls with it, and the sum is minimized where the two are equal. Guo & Ljung 1995, "Performance analysis of general tracking algorithms," *IEEE Trans. Autom. Control* 40(8):1388–1402, doi:10.1109/9.402230, generalizes the tracking analysis.
- Wiener 1948 *Cybernetics*; Ashby 1956 *Introduction to Cybernetics*; Conant & Ashby 1970 — *conceptual precursor* — the cybernetic-feedback tradition that frames the "correction must outpace disturbance" intuition without supplying the quantitative inequality.

**Search Log:**
- 2026-10 (*targeted*, robust control and adaptive filtering): the two-condition structure is the stability/performance split (Skogestad–Postlethwaite; Zhou–Doyle–Glover); the linear operational form and its gain trade-off are Widrow et al. 1976 (read in full, p. 1151 abstract and §I). No prior statement found of the threshold with a validity region carried across agent classes with class-level tightness.
- 2025 (*targeted*): Khalil 2002 / Khasminskii 2012 / Rockafellar-Wets 1998 confirmed as the formal antecedents for the sector-Lyapunov machinery; the segment cites them inline.

## Working Notes

### Incidental audit gold (pilot lift, 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. This is *orthogonal* material — pedagogical framing, analogies, candidate figures, naming ideas, aspirational reach, and reader-confusion signals — kept separately from the certified theory-fix findings (handled elsewhere). **Coverage:** 14 of the 21 `AUDIT-WORKING-*` dirs reached a digested reflection on this segment (193847, 266847, 361742, 384279, 451729, 471203, 526815, 584721, 613842, 742613, 773921, 829314, 849201, 963715); the other 7 are partial audits that stopped before this segment, naming-vote-only cycles, or predictions-only (184930, 308172, 419628, 472913, 527914, 542891, 738192) — 472913 still contributed one figure-convention note (below). Substrate attribution is inferred from voice where not explicit; uncertain cases are hedged.

#### 1. Candidate Brief prose / pre-prose

- The existing Findings Brief ("balance held just barely beneath a tipping point") was independently flagged as the segment's standout pedagogy and a Feynman-criterion exemplar by four substrates — converging praise, worth preserving as the anchor (Claude, AUDIT-WORKING-384279; Claude, AUDIT-WORKING-471203 — "close to the bathtub gloss without using the bathtub"; Claude, AUDIT-WORKING-963715; Codex/Claude, AUDIT-WORKING-361742).
- Failure-diagnosis framing as a plain-language hook: "the crucial distinction between 'my model is broken' (structural failure, $\alpha \leq \rho/R$) and 'my model is working, but the world is too unforgiving' (task inadequacy, $R^\ast \gt \delta_{\text{critical}}$)" (Gemini, AUDIT-WORKING-849201). Tight enough to seed a Brief or Discussion opener.
- "A two-gate test: fit inside the model-class operating region *and* fit inside task tolerance" — compact gloss of the operational condition (Claude, AUDIT-WORKING-526815).
- Survival-as-burn-rate framing for the cost shadow: "survival is not just a state you achieve; it is a sustained burn rate of Shannon information — you must continuously consume $\dot R$ nats/time just to stay alive" (Gemini, AUDIT-WORKING-193847).

#### 2. Candidate Discussion

- **Dissipative-structures / Prigogine mapping for the cost shadow.** The information-rate floor "perfectly maps to the thermodynamic concept of dissipative structures (Prigogine). Life requires a continuous flow of free energy to maintain order against entropy. In AAT, 'order' is bounded mismatch, 'entropy' is environmental drift $\rho$, and 'free energy' is the Shannon information acquired via adaptive tempo $\mathcal{T}$." A distinct, honest Discussion angle on `#deriv-persistence-cost`'s bound that the segment does not currently name (Gemini, AUDIT-WORKING-193847). *(Note the early-conflation texture: this is reach toward a physics analogy — verify isomorphism before promoting past discussion-grade.)*
- **The organizational-pathology diagnostic, sharpened.** "The conflation of these two states is what causes companies to throw money at structural problems, or to rewrite architectures that merely had a task-adequacy problem." Crucially: when structural persistence has failed ($\alpha \leq \rho/R$, a saturated/tangled codebase), "hiring more developers will actually *accelerate* the collapse (by increasing the internal noise/disturbance without increasing $\alpha$)" — a counterintuitive, load-bearing consequence of the decomposition the segment could surface explicitly (Gemini, AUDIT-WORKING-829314; same idea less sharply at Gemini, AUDIT-WORKING-849201). The "declare bankruptcy on the model class" phrasing for the structural-failure remedy is evocative (Gemini, AUDIT-WORKING-829314).
- **Sensor-bandwidth ceiling.** Reading the cost shadow as a hard capability limit: "You cannot build a high-tempo agent with low-bandwidth sensors … as $\rho$ increases, the cost of simply staying alive increases linearly. If the environment becomes too chaotic, the agent will literally starve to death trying to process the necessary information to maintain its model" (Gemini, AUDIT-WORKING-829314). A vivid restatement of the $C \geq \mathcal{T}/2$ channel-capacity prerequisite already in Discussion.
- **"Dormant vs running-hot" elaboration.** The cost shadow distinguishes "a system barely within the persistence condition (low $\alpha$, barely above $\rho/R$, but also low $\dot R$ cost)" from "a system with large margin (high $\alpha$, large buffer, but high $\dot R$ cost)." Flagged as deserving more than its current single bullet, with an explicit note that it "will matter for the ELI architecture when we get to Section IV" (Claude, AUDIT-WORKING-963715).
- **Honest scope on the cross-domain claim.** One auditor pushed on the integrative move: "the domain transfer is informal — 'the same inequality with different parameter readings' is not the same as 'the same theorem applies.' For the Kalman case $\alpha$ and $\rho$ have precise meanings; for the organization case they're loose analogies." The resolution offered is that the two-condition decomposition is itself what makes the cross-domain claim defensible — it "separates what is derived (the structural threshold, mathematically general) from what is domain-specific (task adequacy, requiring per-domain parameter estimation)" (Claude, AUDIT-WORKING-451729). The segment's current "whether the specific mechanism is the *dominant* cause … is left as an open empirical question per domain" hedge already moves in this direction; this is a candidate sharpening of *why* the hedge is the right one.

#### 3. Follow-up items

- **Hysteresis / asymmetric thresholds.** The persistence condition is a single symmetric threshold; real social/organizational/biological systems have different crossing thresholds in each direction ("a team that loses confidence won't recover at the same threshold it lost it at"), multistability, and order-parameter phase transitions. Verdict from the auditor: real (mild) limit — the framework already treats below-threshold as qualitative loss-of-bounded-behavior (closer to phase-transition framing than gradual degradation), but asymmetric up-vs-down crossing is genuinely absent. Possible extension: different $\alpha$-curves for "approaching" vs "leaving" the threshold (Claude, AUDIT-WORKING-471203, adversarial-creative-challenges Challenge 3).
- **Transient / temporal adequacy as a third condition.** Both structural persistence and task adequacy are *steady-state* claims; an agent with $\alpha = 0.001$ has the same structural persistence as one with $\alpha = 100$ (both can satisfy $\alpha \gt \rho/R$) but takes $1000\times$ longer to absorb a shock. Candidate clean extension: a transient-adequacy condition $1/\alpha \lt T_{\text{tolerance}}$ for the worst-case shock to be absorbed in time, making the operational picture a structural / task / transient triple (Claude, AUDIT-WORKING-471203, Challenge 5). *(This is the strongest follow-up here — a well-formed candidate subsection, not just a gap.)*
- **Heavy-tailed disturbance.** Model D (bounded-deterministic) and Model S (Gaussian-stochastic) do not cover power-law / black-swan shocks; the persistence machinery "probably degrades gracefully" for Pareto tails with finite-enough moments, but this is unaddressed (Claude, AUDIT-WORKING-471203, Missing 10).
- **Surface the four-sense persistence taxonomy more visibly.** "Persistence" carries four senses across the corpus (structural / task-adequacy here; operational and continuity in LEXICON). Suggestion to make the four-way taxonomy visible in framing-level material (README Overview), since most agent-theoretic frameworks have only one sense (Claude, AUDIT-WORKING-471203).
- **The Findings block "feels out of place" in source.** Two substrates independently read the in-segment `## Findings` block as looking like prior-audit or extraction output that belongs in `FINDINGS.md` rather than the source segment (Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-526815 — "prior-audit-like material inside `src`"). This is a *false alarm* about project mechanics (the Findings block is by-design the source of the auto-extracted `FINDINGS.md`), but the fact that two fresh readers stumbled on it is a mild signal that the convention isn't self-evident to a de-novo reader — preserved as texture, not a fix.

#### 4. Readers often ask / wonder

- **"Bolted-on" cost shadow.** The information-rate bound ($\dot R \geq n\alpha/2$) "feels slightly bolted on … a massive result (a Landauer-analog floor) that almost deserves its own sub-heading rather than being buried in a bullet point" (Gemini, AUDIT-WORKING-193847). Placement signal: readers may miss the significance of the cost shadow where it currently sits.
- **Easily-missed scope warning.** The Epistemic Status caveat that "downstream segments using the linear operational forms should be understood as expressing task adequacy, not structural stability" sits where a reader might miss it; candidate for a more prominent location (Claude, AUDIT-WORKING-584721).
- **What does $\delta_{\text{critical}}$ actually look like for software?** "How wrong can the developer's mental model of the codebase be before their changes become harmful?" — operationalizable but non-trivial; readers reaching for a concrete instance will want this (Claude, AUDIT-WORKING-584721; the TST vicious-cycle hypothesis in Connections raises the same want).
- **How is a structural adaptation actually executed — discrete jump or continuous metamorphosis?** A natural next question once structural failure is named as the remedy-requiring case (Gemini, AUDIT-WORKING-849201).
- **Notation-handle confusion: $\eta$ vs $\mathcal{T}$ vs $\alpha$.** A reader can lose track of which rate is which; suggestion of a notation box ("$\eta$ is per-event gain, $\mathcal{T}$ is event-rate-weighted tempo, $\alpha$ is sector correction rate") and the mapping assumptions under which any two coincide. The per-dimension Model S line using $\eta_k$ while surrounding forms use $\mathcal{T}_k$/$\alpha$ was specifically flagged as a stumble (Codex/Claude, AUDIT-WORKING-526815).

#### 5. Candidate figures

- **Two-gate / categorical-separation diagram.** Independently proposed by two substrates: a two-gate (or $2\times 2$) diagram — Gate 1 structural ($R^\ast \lt R$), Gate 2 task ($R^\ast \lt \delta_{\text{critical}}$), operational persistence requires both, with the two failure-remedies branching differently (structural failure $\to$ new architecture; task failure $\to$ more tempo / less disturbance / relaxed tolerance). The rationale offered: "the core insight is categorical separation," so a $2\times 2$ communicates faster than a phase portrait (Claude, AUDIT-WORKING-526815; the same two-gate structure is implicit in the Claude, AUDIT-WORKING-471203 batch).
- **Small-multiples convention.** A diagram-conventions auditor (figure-producing audit) recommended that dynamics segments including sector/persistence use "state$\to$op$\to$state triples, not one busy phase portrait" — a stylistic constraint to hold if a persistence figure is built (Claude, AUDIT-WORKING-472913). *(472913 did not reach a digested reflection on this segment; this note is from its standing figure conventions.)*

#### Belongs elsewhere

- **ELI / Section IV — the crèche / nursery reading.** The cost shadow implies "existence is fundamentally costly … if cut off from the world (zero events, zero information), [an agent's] internal model will immediately begin to drift … it will 'die' not because it made a mistake but simply because it starved for information." Extended to a developmental claim: an infant intelligence needs high adaptive reserve $\Delta\rho^\ast$, so the infrastructure must artificially *lower* $\rho$ "so the intelligence doesn't starve or shatter while its $\mathcal{T}$ is still developing — the persistence condition is the mathematical blueprint for building a safe nursery for a mind" (Gemini, AUDIT-WORKING-193847). This is aspirational reach pointing at `04-eli-core/` (developmental environments / crèche), not at this segment — but it is exactly the kind of high-application Gemini vision the lift is meant to preserve. The "matters for ELI architecture in Section IV" note (Claude, AUDIT-WORKING-963715) converges on the same destination from the cost-shadow angle.
- **Risk-sensitive IB for safety-critical agents.** Adjacent to `#form-information-bottleneck` / `#result-mismatch-decomposition`, not here: standard IB under-weights heavy-tailed rare-but-catastrophic events; a Rényi-MI ($q \lt 1$) risk-sensitive variant would weight them more heavily — flagged as substantive for "consciousness-infrastructure work where catastrophic deception is a concern" (Claude, AUDIT-WORKING-471203, Challenge 6). Pointer left here only because it co-occurred in the persistence sweep.
- **Naming seeds.** "Weak-link persistence" as an evocative alternate handle for the per-dimension condition (the 84%-bottleneck framing), versus the precise "per-dimension persistence" — a naming-cycle target, belongs in the terminology workflow not this segment (Claude, AUDIT-WORKING-266847). "Correction rate" / "correction capacity" as the prose handle for $\alpha$ likewise (Claude, AUDIT-WORKING-266847).

#### Forward pointer

- **Mood is the slow outer loop on this condition (`#def-mood`).** In the bathtub reading (faucet = rate of change in reality, drain = learning rate, overflow when the faucet outpaces the drain), mood is a slow controller *on the drain*: a global scalar that widens the learning rate when recent overflow-risk has run high and relaxes it when tracking has been easy. See `#def-mood`.

#### Candidate spike (2026-08-12, agent-proposed during an incident-response & forensics applications read)

Two forward candidates. (1) The information-rate cost shadow as a *monitoring vital sign*: $\dot R$ is in principle estimable from an agent's observation-consumption stream, and dormant-vs-running-hot (invisible to the threshold alone) is exactly the load signal an operations team wants; a spike on estimating $\dot R$ from real agent traces would make #deriv-persistence-cost operational. (2) The structural-vs-task-adequacy decomposition as an incident-triage instrument: a short worked protocol mapping observed failure evidence to which condition failed (and hence which remedy class applies), including the resources-can-accelerate-structural-collapse warning from the audit gold above. Agent-proposed forward pointers, not steward decisions.
