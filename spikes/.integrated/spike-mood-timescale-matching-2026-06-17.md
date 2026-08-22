# Spike: the optimal mood time-constant (F2)

*2026-06-17. Tests the F2 candidate result logged in `#def-mood` Working Notes: "the optimal mood time-constant matches the environment's autocorrelation timescale." Spike disposition per `spikes.sop.md` §0c — attempt the strong (1:1-match) result; land honestly at whatever tier the math supports.*

## The claim under test

`#def-mood` defines mood as a slow leaky integral of the recent surprise stream that modulates the adaptation gain $K$ and tempo $\mathcal{T}$. Its time-constant is $\tau = 1/\lambda$ in

$$m_t = (1-\lambda)\, m_{t-1} + \lambda\, a_t.$$

The candidate result asserts $\tau^\ast$ "matches the environment's autocorrelation timescale." This spike asks whether that is derivable, and in what exact form.

## Model

Mood's functional job (per `#def-mood`, and Eldar et al. 2016 / Bennett et al. 2022) is to estimate a slowly-varying **regime** variable — the local operating point the fast loop should adapt to — from a noisy per-step surprise signal. Cast that as estimation of a drifting latent $\theta_t$ (the regime) observed through noise:

- **Regime dynamics (stationary, autocorrelated).** $\theta_t = \phi\,\theta_{t-1} + \xi_t$, with $\phi = e^{-1/\tau_{\mathrm{env}}}$ and $\xi_t \sim \mathcal{N}(0,\sigma_\xi^2)$ — an AR(1)/Ornstein–Uhlenbeck process with autocorrelation timescale $\tau_{\mathrm{env}}$ and stationary variance $\sigma_\theta^2 = \sigma_\xi^2/(1-\phi^2)$. Autocorrelation $\operatorname{corr}(\theta_t,\theta_{t-k}) = \phi^k = e^{-k/\tau_{\mathrm{env}}}$.
- **Observation.** $a_t = y_t = \theta_t + \eta_t$, $\eta_t \sim \mathcal{N}(0, r)$, $r = \sigma_\eta^2$ the per-step surprise-measurement noise.
- **Estimator.** Mood is the leaky integral $m_t = (1-\lambda) m_{t-1} + \lambda y_t$, i.e. an exponential smoother with memory $\tau = 1/\lambda$.

**Objective.** Choose $\lambda$ (equivalently $\tau$) to minimize the steady-state tracking error $J(\lambda) = \mathbb{E}\!\left[(m_t - \theta_t)^2\right]$.

## Derivation

**Error recursion.** With $e_t = m_t - \theta_t$,

$$e_t = (1-\lambda)m_{t-1} + \lambda(\theta_t + \eta_t) - \theta_t = (1-\lambda)(m_{t-1} - \theta_t) + \lambda\eta_t = (1-\lambda)e_{t-1} - (1-\lambda)\,\Delta\theta_t + \lambda\eta_t,$$

where $\Delta\theta_t = \theta_t - \theta_{t-1}$.

**Regime over mood's window — the operative regime.** The result lives in the slowly-drifting regime $\tau_{\mathrm{env}} \gg 1$ (mood is *for* slow regimes). There $\phi \to 1$ and over the estimator's own (short) memory the AR(1) is locally a random walk with increment variance

$$q \equiv \operatorname{Var}(\Delta\theta_t) = 2\sigma_\theta^2(1-\phi) \approx \frac{2\sigma_\theta^2}{\tau_{\mathrm{env}}}.$$

In that local-random-walk regime $\Delta\theta_t$ is, to leading order, the fresh innovation **uncorrelated** with $e_{t-1}$. (It is not strictly *independent*: $\Delta\theta_t = (\phi-1)\theta_{t-1} + \xi_t$ shares $\theta_{t-1}$ with $e_{t-1}$. The retained mean-reversion cross-covariance $\operatorname{Cov}(\theta_t, e_t) \approx -(1-\phi)\sigma_\theta^2/\lambda$ contributes to $\operatorname{Var}(e)$ at relative order $O(\tau_{\mathrm{env}}^{-1/2})$ — genuinely higher-order, vanishing in the regime of interest. Independent verification 2026-06-17 confirmed the drop is self-consistently negligible; the premise is "uncorrelated to leading order in $1/\tau_{\mathrm{env}}$," not "independent.")

**Steady-state error.** $e_t = (1-\lambda)e_{t-1} + u_t$ with $u_t = \lambda\eta_t - (1-\lambda)\Delta\theta_t$ independent of $e_{t-1}$ and $\operatorname{Var}(u_t) = \lambda^2 r + (1-\lambda)^2 q$. A stable AR(1) with iid forcing has $\operatorname{Var}(e) = \operatorname{Var}(u)/[1-(1-\lambda)^2] = \operatorname{Var}(u)/[\lambda(2-\lambda)]$, so

$$J(\lambda) = \frac{\lambda^2 r + (1-\lambda)^2 q}{\lambda(2-\lambda)}.$$

This is the exact steady-state MSE for the local-random-walk model — a clean bias–variance split: $\lambda^2 r$ is the **noise-tracking** cost (large $\lambda$ admits more observation noise), $(1-\lambda)^2 q$ the **lag** cost (small $\lambda$ lags the drift).

**Optimum.** For $\lambda \ll 1$, $J \approx \dfrac{q}{2\lambda} + \dfrac{\lambda r}{2}$. Then $J'(\lambda) = -\dfrac{q}{2\lambda^2} + \dfrac{r}{2} = 0$ gives

$$\boxed{\;\lambda^\ast = \sqrt{q/r}, \qquad \tau^\ast = 1/\lambda^\ast = \sqrt{r/q}.\;}$$

(Second derivative $q/\lambda^3 \gt 0$: a genuine interior minimum. Both $\lambda \to 0$ and $\lambda \to 1$ are strictly worse — too-slow mood lags the regime, too-fast mood chases noise.)

**Exact minimizer vs. leading-order box.** $J(\lambda)$ above is exact (modulo the leading-order uncorrelatedness step). Its *minimizer*, however, has the exact closed form $\lambda^\ast_{\mathrm{exact}} = \dfrac{\sqrt{q(q+4r)}-q}{2r}$, of which $\sqrt{q/r}$ is the leading-order term — the boxed value overstates $\lambda^\ast$ by a factor $\approx (1 + \tfrac12\sqrt{q/r})$ (≈5% at $q/r = 10^{-2}$, vanishing as $\tau_{\mathrm{env}} \to \infty$). The box is the **leading-order optimum**, not exact; the $J(\lambda)$ formula is what is exact.

**In terms of the environment's autocorrelation timescale.** Substituting $q \approx 2\sigma_\theta^2/\tau_{\mathrm{env}}$:

$$\tau^\ast = \sqrt{\frac{r}{q}} = \sqrt{\frac{r\,\tau_{\mathrm{env}}}{2\sigma_\theta^2}} = \sqrt{\tau_{\mathrm{env}}}\cdot\sqrt{\frac{r}{2\sigma_\theta^2}}.$$

Self-consistency: $\tau^\ast/\tau_{\mathrm{env}} = \sqrt{r/(2\sigma_\theta^2\,\tau_{\mathrm{env}})} \to 0$ as $\tau_{\mathrm{env}} \to \infty$, so $\tau^\ast \ll \tau_{\mathrm{env}}$ exactly where the local-random-walk approximation was invoked. The derivation does not undercut itself.

## Result — and the honest refinement (this is strengthen-vs-soften)

The strong "$\tau^\ast$ **matches** (equals) the environmental autocorrelation timescale" is **not** what the math gives, and asserting it would be false. What is derived is sharper *and* more useful than a slogan:

1. **Exact MSE (local-random-walk model).** $J(\lambda) = \dfrac{\lambda^2 r + (1-\lambda)^2 q}{\lambda(2-\lambda)}$ is exact for the stated model; its minimizer is $\lambda^\ast_{\mathrm{exact}} = \dfrac{\sqrt{q(q+4r)}-q}{2r}$, with leading-order term $\sqrt{q/r}$ (the form used below). "Exact" attaches to the MSE, not to the boxed leading-order minimizer.
2. **Scaling law (autocorrelated environment).** $\tau^\ast = \sqrt{\tau_{\mathrm{env}}\, r/(2\sigma_\theta^2)}$ — the optimal mood time-constant grows as the **square root** of the environmental autocorrelation time, scaled by the surprise noise-to-signal ratio $r/\sigma_\theta^2$. Monotone increasing in $\tau_{\mathrm{env}}$, but sublinear: a 1:1 "match" over-states it.
3. **Robust-qualitative (survives the modeling choices).** The optimum is *interior* and *increasing in $\tau_{\mathrm{env}}$*: faster-changing environments demand shorter mood memory; slower environments reward longer memory; both extremes are strictly suboptimal. This is the load-bearing claim and it does not depend on the Gaussian/AR(1) specifics — it is the generic bias–variance shape of any leaky integrator tracking a drifting source.

Per integration-is-replacement, the canon claim should be **replaced**, not softened-with-a-pointer: the "matches the autocorrelation timescale" phrasing is deleted in favor of the derived scaling law (2) + the robust qualitative claim (3). The refinement is a result, not a retreat — a derived $\sqrt{\cdot}$ scaling law is strictly more than the slogan it replaces.

## The clinical signature (independent corroboration, not part of the derivation)

The affect AR(1) coefficient is $1-\lambda$. **Emotional inertia** (Kuppens, Allen & Sheeber 2010 — formalized as exactly this autocorrelation, valence-general) being *maladaptive when high* reads, through the result, as operating at $\lambda \lt \lambda^\ast$ — i.e. $\tau \gg \tau^\ast(\text{environment})$, the over-smoothing/lag branch. The normative content is sharp: the pathology is not "slowness" per se but **slowness mismatched to a faster-changing-than-assumed environment**. This is corroboration of the result's direction from an independent empirical literature; it is not load-bearing for the math.

## Canon landing (recommended, pending the independent-verify gate)

- Land the derivation as a segment (math-lives-in-segments): a `der-mood-timescale` derived segment carrying $J(\lambda)$, $\lambda^\ast = \sqrt{q/r}$, and the $\tau^\ast \propto \sqrt{\tau_{\mathrm{env}}}$ scaling, at status `conditional`. **Premises (stated explicitly):** stationary AR(1) regime; additive Gaussian surprise noise; slowly-drifting environment $\tau_{\mathrm{env}} \gg 2\sigma_\theta^2/r$ (equivalently $\lambda^\ast \ll 1$ and mood memory $\tau^\ast \gg 1$ step — the single condition validating both the small-$\lambda$ reduction and the leaky-integrator regime); quadratic loss.
- Update `#def-mood`: replace the "matches the autocorrelation timescale" Working Note with the derived scaling; promote the relevant claim to `conditional`; cite `der-mood-timescale`. Spike referenced only from Working Notes.
- This spike is the reasoning trail; the segment carries the theory.

**Gate passed 2026-06-17.** Independent refute-posture verification re-derived every step clean and judged the result safe to land at `conditional`. Three refinements folded in above: (i) "independent" → "uncorrelated to leading order in $1/\tau_{\mathrm{env}}$" (mean-reversion cross-term is $O(\tau_{\mathrm{env}}^{-1/2})$ relative); (ii) the boxed minimizer is leading-order, with exact closed form $\lambda^\ast_{\mathrm{exact}} = (\sqrt{q(q+4r)}-q)/(2r)$ given; (iii) the $\tau_{\mathrm{env}} \gg 2\sigma_\theta^2/r$ premise named explicitly.

## Open remainder (released to the standing cycle)

- **Exact AR(1) (drop the local-random-walk approximation).** The mean-reversion cross-term is higher-order in $\tau^\ast/\tau_{\mathrm{env}}$ but an exact closed form over the full AR(1) (not just its random-walk limit) would remove the one approximation. Expected to shift constants, not the $\sqrt{\cdot}$ law.
- **Mood-sets-gain composition.** Here mood *is* the estimator; in `#def-mood` mood *modulates* $K$. The two-layer version — mood estimates the regime at $\tau^\ast$, then maps its estimate to the fast gain $K$ — should confirm the same $\tau^\ast$ governs the mood layer. Likely a corollary; not yet written.
- **Pre-goal volatility link (Behrens-style).** If $a_t$ is read as a volatility/surprise-rate signal rather than a regime mean, the structure is identical (estimating a drifting latent) but the literature anchor differs; verify the Behrens 2007 volatility-learning-rate result before citing it as prior art.
- **Asymmetric loss.** Quadratic $J$ gives a symmetric optimum. The F-asymmetry of the design memo (deaths-weighted vigilance) would enter as an asymmetric loss, shifting $\lambda^\ast$ — out of scope here, flagged.
