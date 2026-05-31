# 22 - emp-update-gain

Segment: `01-aat-core/src/emp-update-gain.md`
Dependencies: `def-mismatch-signal`, `def-observation-function` - satisfied.
Status observed: `type: empirical`, `status: robust-qualitative`, `stage: claims-verified`.
External spot-check: Amari 1998 exists as `Natural Gradient Works Efficiently in Learning`, Neural Computation 10(2), 251-276, DOI `10.1162/089976698300017746`; available summaries describe natural gradient as steepest direction under information geometry and Fisher-efficient online learning.

## Reflection

The conceptual principle is strong: update gain should rise when the model is uncertain and fall when the observation channel is noisy. The segment also handles several important caveats: scalar gain versus matrix gain, additive updates in appropriate coordinates, opacity resolved by estimating uncertainty from innovations, and overfitting as excessive gain against irreducible noise.

The main precision issue is dimensional. The formula `eta*=U_M/(U_M+U_o)` is meaningful only when `U_M` and `U_o` are comparable uncertainty quantities in the same space/metric: scalar variances in the same observation coordinate, aligned Fisher curvatures, or covariances mapped through the observation operator. The prose says `U_M` may be "predictive variance or entropy" and `U_o` is irreducible observation noise; variance and entropy cannot simply be added. The segment later gestures at the matrix/general-coordinate version, but the headline formula should probably say "in a common uncertainty metric."

## Prompt pass

Predictions vs evidence: I expected a Kalman-like gain ratio. The segment gives that, adds Fisher-local/natural-gradient justification, and then treats the ratio as the quality factor in tempo.

Cross-segment consistency: the update rule respects `def-mismatch-signal` by including a correction map `g(delta_t)`. It also uses `result-mismatch-decomposition` correctly to explain why high gain overfits noise. However, this segment depends heavily on later `deriv-fisher-local-update-gain`, `deriv-adaptive-gain-dynamics`, structural adaptation, and tempo material not in its declared dependencies.

Math verification: scalar Kalman gain reduces to prior variance over prior-plus-observation variance when the observation is direct/aligned. The matrix Kalman form in the table is standard. Amari 1998 supports natural gradient/Fisher efficiency, but the spot-check does not by itself verify this segment's specific scalar-collapse theorem; that burden belongs to the later derivation.

Direction next: `def-causal-information-yield` should distinguish passive observation value from intervention-generated information, and should clarify whether gain-weighted update information and causal information yield are commensurable.

Errors to watch: adding heterogeneous uncertainty measures; treating scalar gain as globally exact in high-dimensional or nonlinear settings; relying on future proof artifacts while frontmatter lists only mismatch and observation function.

What I would change: state the headline ratio as "scalar/common-metric form" and move Fisher-local exactness to a theorem dependency that is declared in frontmatter.

Curiosity: gain collapse is a useful diagnostic vocabulary; it ties confirmation bias and sensor distrust to the same mathematical failure mode.

New knowledge enabled: adaptive tempo now has a clear multiplicative decomposition: event rate is speed, gain is usable correction quality.

Audit process change: the diagram should be a gate/balance, not a pipeline: two uncertainty inputs compete to set the fraction of mismatch admitted into the model.

Value feel: high but risky. The qualitative principle is load-bearing and plausible; the exactness claims require more dependency support than the local segment provides.

## Diagram thought

A good representation is a calibrated gate. Mismatch approaches the model, but the gate aperture is set by the ratio of model uncertainty to total comparable uncertainty. A side warning should show that if `U_M` and `U_o` are not in the same metric, the gate setting is undefined rather than merely approximate.
