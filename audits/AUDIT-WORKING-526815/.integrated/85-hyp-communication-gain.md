# 85 - hyp-communication-gain

Source: `01-aat-core/src/hyp-communication-gain.md`

## First-pass understanding

This segment generalizes the single-agent update-gain ratio into an inter-agent trust ratio. A received message is discounted not only by channel noise, but also by uncertainty about the sender's calibration and about whether the sender is aligned with the receiver's interests. The qualitative idea is useful: communication is not just observation through a wire; it carries model-of-source and model-of-relationship uncertainty.

The weak point is the additive denominator. Channel ambiguity can often be represented as observation noise, and source calibration can sometimes be estimated as residual dispersion, but strategic misalignment is not naturally a zero-mean variance term. It is a policy-dependent game variable: the sender may optimize the message against the receiver's trust rule. The segment acknowledges this, so the local verdict is not "wrong formula" so much as "clear heuristic, not optimal gain without strong common-scale and nonstrategic assumptions."

## Diagram attempt

I drew the gain formula as a message passing through three gates before it reaches the receiver's update rule. The diagram separates ordinary variance-like gates from the strategic-alignment loop, because deception changes the generation policy for the signal rather than merely widening an independent noise distribution.

## Findings and watches

- F167 candidate: the additive communication-gain denominator is only optimal under strong common-scale, independent, approximately zero-mean uncertainty assumptions. `U_o`, `U_src`, and especially `U_align` need a precise map onto the same predictive-dispersion units before the ratio can carry Bayesian-gain force.
- F168 candidate: treating teleological-unity uncertainty as an additive variance term under-models strategic deception. Misalignment can change the message policy adversarially as a function of the receiver's trust rule, not merely add noise to an otherwise truthful signal.
- F169 soft candidate: estimating `U_src + U_align` from residual variance minus channel noise is fragile. Residuals conflate sender calibration, relationship alignment, receiver model error, task nonstationarity, common shocks, and strategic regime changes; the subtraction can also go negative without a floor or model.
- F170 candidate: the distributed-tempo working note adds communication tempo contributions linearly. This repeats the earlier tempo-additivity concern: messages can be redundant, correlated, delayed, costly, or strategically selected, so additive effective tempo needs independence/nonredundancy and cost conditions.
- F171 soft candidate: the transitive-trust mixture formula collapses to the prior only if `P_0(s_j)` is explicitly uninformative about `theta_k` and normalized consistently. The scalar reliability `r_ji` also hides domain, calibration, and alignment dimensions that the segment otherwise separates.
- F172 watch: risk-asymmetric trust should be tied to an explicit loss function or decision rule. A conservative posterior quantile is plausible for high-impact downside, but it is not implied by Bayesian reliability estimation alone.

## Local verdict

Keep the formula as a trust-calibration heuristic unless a later segment supplies the common uncertainty scale, independence assumptions, and game-theoretic treatment needed to make strategic communication gain optimal.

