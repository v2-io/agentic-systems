# 91 - result-adversarial-tempo-advantage

Source: `01-aat-core/src/result-adversarial-tempo-advantage.md`

## First-pass understanding

This result gives the clean algebra behind the "inside the loop" claim. In deterministic coupling, the faster agent benefits twice: its own mismatch is divided by its tempo, and the target's disturbance is multiplied by that same tempo. In the coupling-dominant symmetric limit, those factors multiply into a squared mismatch ratio. In stochastic coupling, the target's RMS mismatch only shrinks with the square root of its own tempo, yielding the `3/2` exponent instead.

The derivation is locally coherent once the assumptions are accepted. Most of the remaining audit pressure is inherited: scalar tempo must really equal sector correction rate, stochastic coupling must really add to the noise amplitude, and the coupling model must keep tempo exogenous. The result is exact conditional algebra, not an empirical universal about adversarial systems.

## Diagram attempt

I drew the squared advantage as a two-factor product: faster correction on the attacker's side and faster disturbance generation against the target. The stochastic branch replaces one full correction factor with a square-root averaging factor, making the `3/2` exponent visually distinct.

## Findings and watches

- F215 candidate: the derivation assumes `alpha = T` exactly. This inherits the tempo-to-sector-rate bridge issue from earlier segments; without that bridge the exponent algebra is formally about `alpha` ratios, not raw adaptive tempo ratios.
- F216 candidate: Model S inherits the additive-noise-scale assumption `sigma_eff = sigma_base + gamma T`. The `3/2` exponent is exact for that amplitude model, but different stochastic-combination conventions could change prefactors or scaling.
- F217 candidate: declared dependencies omit some proof sources used in the segment, especially `result-sector-persistence-template` / `deriv-sector-condition` for the steady-state formulas and `def-adaptive-tempo` for scalar tempo.
- F218 soft candidate: the non-coupling-dominant stochastic limit is `b -> 1/2`, while the chapter intro's broad prose said the exponent approaches `1`. The intro should distinguish deterministic and stochastic non-coupling limits.
- F219 candidate: simulation validation is deferred to `result-adversarial-exponent-regimes`, which is not a declared dependency and has not yet been read in this outline order. Keep simulation-backed statements provisional until that file is reached.
- F220 soft candidate: the asymmetric-coupling note says `gamma_A/gamma_B` shifts the ratio without changing the exponent. This is true for constant gammas under the displayed model; it fails if coupling effectiveness depends on tempo, state, opacity, or regime assignment.
- F221 watch: the finite-`nu` correction formula in Working Notes references `deriv-discrete-sector-condition` and carries a nontrivial expression. Treat it as appendix/proof-home material unless the dependency path exposes it.

## Local verdict

This is one of the cleaner conditional results: the exponent follows by algebra from the displayed steady-state model. Its strength should be reported as "exact under alpha-equals-tempo and the chosen coupling/noise models," with the stochastic and simulation qualifications kept separate.

