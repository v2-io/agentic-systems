# 89 - der-adversarial-destabilization

Source: `01-aat-core/src/der-adversarial-destabilization.md`

## First-pass understanding

This segment cleanly casts adversarial destabilization as the negation of the sector persistence condition. In Model D, the adversary adds deterministic disturbance `gamma_A T_A`; in Model S, it adds stochastic unpredictability. The important correction to the intro-level intuition is that tempo alone is not the weapon: the operative input is coupled tempo, `gamma_A T_A`, compared against the target's remaining reserve.

The file is also honest about the effects spiral. The threshold results are conditional and exact under the coupling assumptions; the spiral is only discussion-grade until `gamma_A(||delta_B||)` is formalized. The new audit pressure points are mostly in the coupling models themselves: how stochastic amplitudes combine, what happens when the target is already unstable, and how opacity affects coupling effectiveness.

## Diagram attempt

I drew the result as a reserve gauge. Baseline disturbance consumes part of `B`'s reserve, and adversarial coupled tempo consumes the rest. Crossing the threshold leaves the invariant region. A side loop shows the effects spiral as an extra feedback assumption, not part of the base threshold theorem.

## Findings and watches

- F183 resolved/formalized: the segment gives the correct product threshold `T_A > (alpha_B R_B - rho_base)/gamma_A`; the intro should use this product framing rather than "speed" alone.
- F185 resolved as caveated: the effects spiral explicitly assumes `gamma_A` increases with `||delta_B||` and is marked discussion-grade. Keep the intro's "mathematics of panic" wording tied to that caveat.
- F195 candidate: the Model D threshold should explicitly split the already-unstable case. If `alpha_B R_B - rho_base <= 0`, `B` already fails baseline persistence, so the adversarial tempo threshold is vacuous or zero rather than a meaningful positive threshold.
- F196 candidate: Model S adds adversarial stochastic coupling as `sigma_B = sigma_base + gamma_A T_A`. For independent stochastic sources, variance/power often combines in quadrature or covariance addition, not amplitude addition; this needs a noise convention.
- F197 candidate: the Model S scalar threshold inherits the earlier stochastic-sector convention issue around `sigma`, `n`, and covariance units. The file says scalar `n=1`, but downstream multidimensional uses need the full covariance/norm convention.
- F198 candidate: "mixed cases are handled by decomposing drift and noise components and applying both bounds additively" needs a combined Lyapunov bound. Deterministic drift and stochastic diffusion do not generally combine by simply adding threshold tests.
- F199 soft candidate: the claim that the decoupled analysis is "conservative" should state the beneficiary. Treating `T_A` as exogenous is best-case for the attacker and worst-case for the target, but not conservative for all uses.
- F200 candidate: the qualitative opacity formula `gamma_A proportional to 1/H_b(A) * 1/H_b(B)` appears sign-ambiguous. Low target opacity `H_b(B)` plausibly helps `A`, but high adversary opacity `H_b(A)` can also make `A` harder for `B` to anticipate, increasing effective disruption rather than decreasing `gamma_A`.
- F201 soft candidate: the effects-spiral text says `gamma_A(||delta_B||)` makes disturbance grow superlinearly and `dot V_B > 0` increasing. That requires conditions on the functional form and current state; monotone `gamma` alone is not enough.
- F202 watch: the statement that adversarial/strategic composition lies outside contraction-metric frameworks may be too broad. It is plausible for this asymmetric disturbance model, but saddle/monotone-game dynamics can sometimes be handled with specialized contraction-like tools.

## Local verdict

The base destabilization threshold is a useful conditional result. The final audit should separate that result from the more speculative opacity and effects-spiral material, and require explicit stochastic-combination and coupled-dynamics conventions before using the Model S or mixed-case claims quantitatively.

