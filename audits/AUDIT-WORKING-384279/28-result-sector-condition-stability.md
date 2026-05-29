# 28 — result-sector-condition-stability

*Type: result. Status: exact. Stage: claims-verified. Depends: [def-adaptive-tempo, def-mismatch-signal, deriv-sector-condition, result-sector-persistence-template].*

## Predictions vs evidence
Predicted: nonlinear Lyapunov persistence result. Found: that, plus Model D + Model S statements as instantiations of the abstract template `#result-sector-persistence-template`.

## **Math verification (Lyapunov derivation — direct)**

Model D: $V(\delta) = (1/2)\|\delta\|^2$, $\dot V = \delta^T(-F + w) \leq -\alpha\|\delta\|^2 + \rho\|\delta\|$ via A2' + Cauchy-Schwarz. $\dot V < 0$ when $\|\delta\| > \rho/\alpha$. Ultimate bound $R^* = \rho/\alpha$. For $R^* < R$: $\alpha > \rho/R$. ✓

Model S: SDE $d\delta = -F\,dt + \sigma_w dW_t$. Itô: $d\mathbb{E}[V] = \mathbb{E}[-\delta^T F + (1/2)\sigma_w^2 n]\,dt \leq (-\alpha\mathbb{E}\|\delta\|^2 + (n/2)\sigma_w^2)\,dt$.

Steady state: $\alpha\mathbb{E}[\|\delta\|^2] = n\sigma_w^2/2$, so $\mathbb{E}[\|\delta\|^2] = n\sigma_w^2/(2\alpha)$ and RMS = $\sigma_w\sqrt{n/(2\alpha)}$. ✓

Mean-square persistence: RMS < $R$ ⇒ $\alpha > n\sigma_w^2/(2R^2)$. ✓

**Both results derive cleanly. No errors.**

## Prose-coherence
- Header preamble and Discussion overlap in framing (saturation/thresholding/structural-adaptation triggers). Within cadence.
- "Disturbance-model choice is a domain question, not a theory question" (line 53) is a good methodological flag.
- Structural-vs-operational-vs-continuity persistence triad named in Discussion line 59 — disambiguates three senses of "persistence."

## Cross-segment consistency
Anchors to `#result-sector-persistence-template` (template; appendix), `#hyp-mismatch-dynamics` (linear case), `#der-gain-sector-bridge` (grounds A2'), `#result-persistence-condition` (the headline form), `#result-structural-adaptation-necessity` (trigger). Coherent.

## Watch list
- The template-and-instantiation pattern (this segment as instantiation of the appendix template) is the right factoring. Verify the template's abstract preconditions (T1, T2, T3) when I reach #result-sector-persistence-template.

## Next-segment predictions
`#result-persistence-condition`. Will state $\alpha > \rho/R$ as the headline form. Probably the most-cited result in the framework downstream. Status `exact`.

## Brief wandering
The "$1/\alpha$ vs $1/\sqrt{\alpha}$" qualitative-difference between Model D and Model S is one of the framework's load-bearing results — it propagates downstream into the $(\mathcal{T}_A/\mathcal{T}_B)^2$ vs $(\mathcal{T}_A/\mathcal{T}_B)^{3/2}$ adversarial-coupling exponents. This segment establishes the scaling cleanly.
