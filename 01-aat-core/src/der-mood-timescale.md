---
slug: der-mood-timescale
type: derived
status: conditional
depends:
  - def-mood
  - def-mismatch-signal
stage: draft
---

# Optimal Mood Time-Constant

The mood time-constant that minimizes steady-state regime-tracking error grows as the square root of the environment's autocorrelation timescale — so both too-fast and too-slow mood are strictly suboptimal, and the optimum is environment-matched but sublinearly.

## Formal Expression

Mood ( #def-mood) is a leaky integral $m_t = (1-\lambda)m_{t-1} + \lambda\, a_t$ with time-constant $\tau = 1/\lambda$, whose functional role is to estimate a slowly-varying regime from the noisy surprise stream. Model that role explicitly:

*[Assumption]* The regime is a stationary AR(1) latent $\theta_t = \phi\,\theta_{t-1} + \xi_t$, with $\phi = e^{-1/\tau_{\mathrm{env}}}$, $\xi_t \sim \mathcal{N}(0,\sigma_\xi^2)$, stationary variance $\sigma_\theta^2 = \sigma_\xi^2/(1-\phi^2)$, and autocorrelation $\operatorname{corr}(\theta_t,\theta_{t-k}) = e^{-k/\tau_{\mathrm{env}}}$. The surprise summary is $a_t = \theta_t + \eta_t$, $\eta_t \sim \mathcal{N}(0,r)$. Mood tracks $\theta_t$; the loss is steady-state MSE $J(\lambda) = \mathbb{E}[(m_t - \theta_t)^2]$.

*[Derived (steady-state MSE)]* In the slowly-drifting regime $\tau_{\mathrm{env}} \gg 2\sigma_\theta^2/r$, where the AR(1) increment variance is $q \equiv \operatorname{Var}(\Delta\theta_t) = 2\sigma_\theta^2(1-\phi) \approx 2\sigma_\theta^2/\tau_{\mathrm{env}}$ and the increment is uncorrelated with the prior error to leading order in $1/\tau_{\mathrm{env}}$,

$$J(\lambda) = \frac{\lambda^2 r + (1-\lambda)^2 q}{\lambda(2-\lambda)}.$$

The two terms are a bias–variance split: $\lambda^2 r$ is the noise-tracking cost, $(1-\lambda)^2 q$ the lag cost.

*[Derived (optimum)]* $J$ has an interior minimizer $\lambda^\ast_{\mathrm{exact}} = \dfrac{\sqrt{q(q+4r)}-q}{2r}$, with leading-order form

$$\lambda^\ast = \sqrt{q/r}, \qquad \tau^\ast = \sqrt{r/q}.$$

*[Derived (scaling law)]* Substituting $q \approx 2\sigma_\theta^2/\tau_{\mathrm{env}}$,

$$\tau^\ast = \sqrt{\tau_{\mathrm{env}}\cdot \frac{r}{2\sigma_\theta^2}} = \sqrt{\tau_{\mathrm{env}}}\cdot\sqrt{\frac{r}{2\sigma_\theta^2}}.$$

The optimal mood time-constant grows as the **square root** of the environmental autocorrelation time, scaled by the surprise noise-to-signal ratio $r/\sigma_\theta^2$. Self-consistency: $\tau^\ast/\tau_{\mathrm{env}} \to 0$, so $\tau^\ast \ll \tau_{\mathrm{env}}$ exactly where the leading-order step was taken.

## Epistemic Status

`Conditional` on the named premises: stationary AR(1) regime, additive Gaussian surprise noise, the slowly-drifting condition $\tau_{\mathrm{env}} \gg 2\sigma_\theta^2/r$ (equivalently $\lambda^\ast \ll 1$ and mood memory $\tau^\ast \gg 1$ step — one condition validating both the small-$\lambda$ reduction and the leaky-integrator regime), and quadratic loss. Under these, $J(\lambda)$ is exact and the scaling law follows; the boxed $\lambda^\ast = \sqrt{q/r}$ is the leading-order term of the exact minimizer given above, not itself exact. The optimum is derived *for mood's regime-estimator role*; its transfer to the modulator role ($m_t$ setting the fast gain $K_t$ — `#def-mood`'s actual use) is conjectured equal under certainty-equivalent calibration and remains the open two-layer composition item named below.

The derivation was independently refute-verified (2026-06-17): every algebraic step re-derived clean; the one approximation (dropping the mean-reversion cross-term) confirmed $O(\tau_{\mathrm{env}}^{-1/2})$ relative and self-consistently negligible.

Three claims at distinct tiers travel out of this: the **exact** steady-state MSE for the model; the **conditional** $\sqrt{\tau_{\mathrm{env}}}$ scaling law; and a **robust-qualitative** core — the optimum is interior and monotone-increasing in $\tau_{\mathrm{env}}$ — which is the generic bias–variance shape of any leaky integrator tracking a drifting source and does not depend on the Gaussian/AR(1) specifics. What would strengthen this: the exact closed form over the full AR(1) (not its random-walk limit); the two-layer composition where mood's estimate sets the fast gain $K$ rather than being the estimator directly. What would soften it: an estimator/loss outside the leaky-integrator–quadratic family (e.g. the Kalman/Wiener filter can track $\tau_{\mathrm{env}}$ more directly in some SNR regimes) — but `#def-mood` specifies the leaky integrator, so the $\sqrt{\cdot}$ law is the in-family answer.

## Discussion

The result corrects the naive expectation that mood inertia should simply "match" how fast the world changes. It is environment-matched, but **sublinearly**: a fourfold slower environment warrants only a twofold longer mood memory. The load-bearing qualitative content is that the optimum is *interior* — too-fast mood chases noise (the variance term dominates), too-slow mood lags genuine regime shifts (the bias term dominates) — so a mood with no inertia and a mood that never recovers are both strictly suboptimal, for the same reason at opposite ends.

This gives the clinical literature on **emotional inertia** a normative reading. The affect AR(1) coefficient is $1-\lambda$; inertia being maladaptive when high (Kuppens, Allen & Sheeber 2010, who formalize inertia as exactly this autocorrelation) corresponds to operating at $\lambda \lt \lambda^\ast$, i.e. $\tau \gg \tau^\ast(\text{environment})$ — the over-smoothing branch. The pathology the result names is not slowness as such but **slowness mismatched to a faster-changing-than-assumed environment**: the same $\tau$ is well-tuned in a slow world and pathological in a fast one. (The corroboration is directional, from an independent empirical literature; it is not load-bearing for the derivation.)

## Working Notes

- **Verification record.** Independent refute-posture re-derivation (2026-06-17) and the exact-minimizer expansion: `spikes/.integrated/spike-mood-timescale-matching-2026-06-17.md`.
- **Open — exact AR(1).** Drop the local-random-walk approximation for a closed form over the full AR(1); expected to shift constants, not the $\sqrt{\cdot}$ law.
- **Open — mood-sets-gain composition.** `#def-mood` has mood *modulating* $K$, not *being* the estimator; the two-layer version should confirm the same $\tau^\ast$ governs the mood layer. Likely a corollary.
- **Open — asymmetric loss.** Quadratic $J$ gives a symmetric optimum; the deaths-weighted vigilance asymmetry of the design memo (`msc/mood-layer-sovereignty-carve-2026-06-17.md`, F-asymmetry) would enter as an asymmetric loss and shift $\lambda^\ast$.
