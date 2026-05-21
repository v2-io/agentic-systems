---
slug: obs-gated-tempo-advantage
type: observation
status: empirical
depends:
  - der-adversarial-destabilization
  - emp-update-gain
  - def-adaptive-tempo
stage: draft
---

# Observation: Gated Tempo Advantage

Observation noise *gates* the adversarial tempo advantage from the prior result. When agents observe their mismatch through a noisy channel, the faster agent's additional corrections become noisy, partially offsetting its tempo advantage. The mechanism is direct: a faster attacker makes more corrections per unit time, each noisy because of observation noise; the *additional* corrections add proportional noise, partially canceling the additional speed. Simulation confirms this — at observation noise comparable to or larger than process noise, the steady-state mismatch-ratio exponent drops dramatically (fixed-gain agents lose nearly all of the squared scaling; optimal-gain agents matched to the noise level recover *some* but not all of it).

The framework's prescription: the optimal-gain principle ( #emp-update-gain) partially restores the advantage but cannot fully recover the noise-free level. The Riccati gain mitigates the loss by *reducing the gain to match the noise level* — correcting less aggressively but more accurately. *Gated* names the regime structure: the squared scaling that defines `#result-adversarial-tempo-advantage` applies cleanly only in the low-noise regime, while higher noise pushes the system into the non-coupling-dominant regime of `#result-adversarial-exponent-regimes` where the exponent collapses to linear or sub-linear. The defender-side payoff is concrete: noise on the defender's observation channel reduces the attacker's superlinear advantage without altering tempo or gain, which is the structural reason cheap noise injection into the defender's channel is a viable defense against a high-tempo attacker.

## Formal Expression

*[Observation (obs-gated-tempo-advantage, from track-b Variant E)]*

In a two-agent adversarial system with observation noise $\sigma_{\text{obs}}$ added to each agent's mismatch signal:

| $\sigma_{\text{obs}}$ | Exponent (fixed $\eta$) | Exponent (optimal $\eta^\ast$) |
|:---:|:---:|:---:|
| 0.00 | 1.04 | 1.04 |
| 0.10 | 1.00 | 0.97 |
| 0.20 | 0.92 | 0.94 |
| 0.50 | 0.60 | 0.63 |
| 1.00 | 0.18 | 0.40 |

At $\sigma_{\text{obs}} = 1.0$ (10x the process noise), the fixed-gain adversarial exponent drops from $\sim 1.0$ to $\sim 0.2$ — tempo advantage nearly vanishes. The Riccati-optimal gain restores it to $\sim 0.4$, more than doubling the advantage but not recovering the noise-free level.

**The mechanism.** When observation noise is high, each correction step adds noise to the mismatch estimate. The faster agent makes more corrections per unit time, each noisy, partially offsetting the benefit of higher tempo. The optimal gain mitigates this by reducing $\eta$ to match the noise level — correcting less aggressively but more accurately.

## Epistemic Status

*Empirical.* Max attainable: derived (the mechanism is analytically tractable via Riccati analysis of noisy AR(1) processes). The observation that noise degrades advantage is confirmed by simulation. The optimal gain's partial restoration is consistent with the uncertainty ratio principle ( #emp-update-gain: $\eta^\ast = U_M / (U_M + U_o)$). The quantitative degradation curve ($b$ vs. $\sigma_{\text{obs}}$) is empirical at these parameters; a general analytical expression would require solving the coupled noisy-AR(1) system.

## Discussion

**Observation quality gates tempo advantage.** Boyd insisted that the quality of Orient (observation processing) matters more than raw OODA speed. The simulation results show a formal analog of this pattern: faster tempo with noisy observations ($\sigma_{\text{obs}}$ high) gives nearly zero advantage over a slower agent with equally noisy observations. The tempo advantage is gated by observation quality — consistent with Boyd's emphasis, though the model captures a specific mechanism (noisy correction steps) rather than the full richness of Orient processing.

**The optimal gain helps most in the moderate-noise regime.** At $\sigma_{\text{obs}} = 0.05$ (observation noise half of process noise), the optimal gain cuts steady-state mismatch by 52% compared to fixed gain. At very high noise, the improvement is less dramatic in absolute terms but more important relatively (0.40 vs. 0.18 exponent).

**Practical implication.** An agent facing an adversary with superior tempo should invest in degrading the adversary's observation quality rather than trying to match their speed. Conversely, an agent with superior tempo should protect its observation channels — the tempo advantage is only as good as the observation quality that supports it.

**Connection to code quality.** In the software domain ( #der-code-quality-as-observation-infrastructure — cross-component reference, see `02-tst-core/`), code quality IS observation infrastructure. A well-structured codebase provides low-noise observations (clear tests, readable code, explicit interfaces). A poorly structured codebase adds observation noise to every development cycle, degrading the developer's effective tempo regardless of how fast they work.

**Recipient-side mechanism.** High $U_{o,B}$ pushes adversarial events below the observability floor (boundary (I-c) in #der-interaction-channel-classification). Events that would otherwise land in Regime II (destabilizing) instead fall into Regime III (ambient noise): they contribute to $\sigma_{w,B}^2$ without producing destabilizing mismatch. The tempo-advantage exponent drops because the *fraction* of $A$'s events landing in Regime II shrinks — $A$'s tempo still matters, but more of it is dissipated into the noise floor. This is the recipient-side expression of the rate boundary.

## Working Notes
- The finding that fixed $\eta = 0.1$ is "remarkably robust" to observation noise (42% degradation at $\sigma_{\text{obs}} = 10 \times q_{\text{env}}$) suggests that conservative gains are a reasonable default for environments with unknown noise levels. The cost of being slightly below optimal is much less than the cost of being above optimal (overcorrection amplifies noise).
- The interaction between observation noise and adversarial exponent regime (drift vs. stochastic) has not been tested. The Variant E results use stochastic coupling only. Whether observation noise degrades the deterministic-drift exponent ($b = 2$) by the same proportion is an open question.
- Simulation code: `../../spikes/track-b-nonlinear-sims/variants/variant_ef_extensions.py`. Results: `variant_ef_results.md`.
