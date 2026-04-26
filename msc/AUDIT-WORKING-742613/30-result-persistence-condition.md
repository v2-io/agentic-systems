# 30 — result-persistence-condition

Dependencies checked: `def-adaptive-tempo`, `def-mismatch-signal`, `result-sector-condition-stability`, and `result-sector-persistence-template` already read.

## Reflection

This segment usefully separates structural persistence from task adequacy.
That is a strong conceptual repair against the common overreading "stable means good enough."

Deterministic Model D:
The structural threshold $\alpha>\rho/R$ and task threshold $\alpha>\rho/\lVert\delta_{\text{critical}}\rVert$ are sound under the sector-condition proof.

Model S:
The segment states the stochastic threshold as exact structural persistence under local sector assumptions.
This inherits finding J.
The RMS formula is exact in the global OU / global sector case, but under local sector condition plus Brownian noise it is not an exact persistence guarantee.
The segment should distinguish:
- mean-square typical scale under global assumptions,
- stopped/local bound before exit,
- finite-time probability of exceeding $R$,
- and infinite-horizon sector-region persistence, which nondegenerate Brownian noise cannot guarantee for finite $R$.

Candidate finding J therefore applies directly to `result-persistence-condition`, not only appendices.

Interaction with adaptive-tempo caveat:
The segment does include a "Channel independence and scalar tempo" caveat in Discussion, which helps with finding I.
But the linear operational forms remain prominently stated as forms "used throughout the theory."
Downstream users need to know these are scalar/additive proxies unless independence/isotropy/per-dimension conditions are satisfied.

Interaction with gradient-equivalence finding:
The relationship between $\alpha$ and $\mathcal T$ cites `der-gain-sector-bridge`.
It should be corrected once finding K is fixed: strong convexity is sufficient, not equivalent; one-point B1 is the bridge condition.

Status:
`status: exact` is appropriate for the deterministic and definition-level parts, but too broad for the mixed segment as currently written because Model S local persistence and per-dimension empirical extension are not exact in the same sense.
A "Derived vs. Chosen vs. Empirical" table could help, or the Model S claim could be scoped precisely enough to preserve exact status.

What this enables:
This is the central result of Section I.
Despite the Model S issue, the deterministic persistence inequality and structural/task distinction are valuable and appear salvageable.

Prediction for next segment:
`result-structural-adaptation-necessity` should say parametric updates fail when mismatch exceeds $R$ or model class fitness is too low.
I will watch whether it overclaims "necessity" versus alternative responses like changing objective or accepting task failure.

Running report update:
- Finding J has main-result impact through `result-persistence-condition`'s exact Model S persistence statement.
- Status of central persistence segment should be narrowed or internally tiered.
