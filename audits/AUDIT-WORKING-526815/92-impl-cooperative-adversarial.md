# 92 - impl-cooperative-adversarial

Source: `01-aat-core/src/impl-cooperative-adversarial.md`

## First-pass understanding

This chapter-end segment packages the signed-coupling story: cooperative and adversarial interactions share the same disturbance ledger, recipient-side regimes determine repair paths, tempo advantage is superlinear under coupling-dominant assumptions, and contraction-style machinery hands off to equilibrium machinery for strategic cases. As a map, it is helpful.

The audit issue is again synthesis pressure. The component segments were fairly careful about modeling choices, dependency gaps, and conditional exponents. This implications segment sometimes turns those caveats into stronger operational prescriptions: ambient noise is treated as zero rather than reserve-draining variance, high observation noise is described as helping the defender, contraction is said to fail for strategic/adversarial regimes as a class, and signed coupling is mapped directly back into trust calibration.

## Diagram attempt

I drew the chapter-end as four lanes feeding the Ch.5 hand-off: signed coupling, recipient regimes, tempo exponents, and contraction limits. Each lane carries a caveat tag because the implications segment is organizing results rather than strengthening them.

## Findings and watches

- F222 candidate: `impl-cooperative-adversarial` repeats the "canonical catalog home" pattern and should preserve the weakest status of each imported claim. The synthesis uses conditional and discussion-grade pieces from several files plus forward Ch.5 material.
- F223 candidate: the repair mapping for magnitude shocks drifts. The classification segment ties II-a to sector radius/capacity and sustained-rate destabilization; this implications segment says magnitude shocks respond to gain investment/lower `U_o`. That may help some cases, but it is not the same repair axis.
- F224 candidate: ambient noise is described as contributing "zero" and not calling for response, but `der-interaction-channel-classification` says Regime III contributes to variance and slowly drains reserve. The implication should say filtering or infrastructure response may be appropriate when aggregate ambient load is material.
- F225 candidate: the regime-typed effective-disturbance description here ("informative updates contribute to ordinary tempo demand; magnitude shocks to peak-load demand; structural shocks to adaptation cadence; ambient noise to zero") no longer matches the displayed `rho_eff` formula in the classification file.
- F226 candidate: the claim that cheap noise injection into the defender's observation channel helps the defender against a high-tempo attacker is one-sided. Higher observation noise may gate adversarial events, but it also degrades the defender's real observations, update gain, and ordinary persistence.
- F227 soft candidate: "highly-noisy environments produce more cooperative-game-like dynamics" is an unsupported cross-domain claim in this segment. It needs a model distinguishing adversarial-channel noise from shared task/environment noise.
- F228 candidate: "inside the opponent's loop means `T_A > T_B/k`" is not the threshold delivered by the preceding derivations. The destabilization threshold depends on `gamma_A T_A`, base disturbance, `alpha_B`, and `R_B`; the tempo ratio result depends on coupling-dominant symmetric assumptions.
- F229 candidate: the contraction-obstruction section overstates the method boundary. "Contraction-metric machinery cannot handle strategic/adversarial regimes" is too broad unless scoped to the particular attracting-fixed-point/contraction template; specialized contraction/monotone-operator tools may apply in some games.
- F230 soft candidate: the passivity claim "adversarial inputs drive any storage function" is too sweeping as written. It needs the specific input/output passivity assumptions and adversarial input class.
- F231 soft candidate: "cooperative coupling that is too strong can produce equilibrium-stability failures" is plausible but not derived from this chapter's signed-disturbance model; it belongs with the future equilibrium machinery unless formalized locally.
- F232 candidate: the final trust bridge repeats the too-direct mapping from observed cooperative/adversarial coupling to `U_align -> 0` or large. Trust uncertainty should update from evidence under a model; coupling sign is evidence, not identical to alignment certainty.
- F233 watch: `deriv-strategic-composition`, Ch.5 exponent regimes, agent opacity, 16-cell targeting, and matrix-Loewner persistence are heavy forward references. Keep them as bridge material until their own AAT segments are read.

## Local verdict

The chapter synthesis is useful if it remains a map. It should not be used as independent support for the regime repair prescriptions, observation-noise defense claim, contraction no-go, or trust-calibration mapping without routing back through the more qualified component segments.

