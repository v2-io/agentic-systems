# 24 - def-adaptive-tempo

Segment: `01-aat-core/src/def-adaptive-tempo.md`
Dependencies: `emp-update-gain`, `form-event-driven-dynamics` - satisfied.
Status observed: `type: definition`, `status: exact`, `stage: claims-verified`.

## Reflection

This segment is unusually self-aware about the scalar formula's limits. It defines tempo as rate times gain, then immediately supplies tensor tempo, shared-eigenbasis collapse, redundancy penalty, scalar/vector caveats, and downstream scope warnings. The additivity and anisotropy limitations I had been watching are explicitly acknowledged rather than hidden.

The remaining conceptual pressure is whether `nu * eta` is really "rate of useful information acquisition." `eta` is an update gain or correction fraction; it is not itself event information content. Earlier `form-event-driven-dynamics` defined `I(e_tau; Omega_tau | M_tau-)`, but this definition does not include a per-event information magnitude or Fisher-information payload except indirectly in the tensor discussion through `H_L`. As written, two channels with the same event rate and gain but very different event payloads get the same scalar tempo. That may be acceptable if tempo is "effective correction rate" rather than information rate, but the wording should be tightened.

## Prompt pass

Predictions vs evidence: I expected `T=sum nu eta` and a simple speed-quality story. The segment gave that plus substantial tensor and redundancy machinery.

Cross-segment consistency: consistent with `emp-update-gain` and `form-event-driven-dynamics`, except for the unused event-information-content definition. The tensor form helps repair the common-metric issue from update gain by using precision/Fisher objects.

Math verification: dimensions are coherent if `eta` is dimensionless and `nu` is events per time, giving correction opportunities per time. Calling that information per time needs either normalized unit-information events or an information-per-event multiplier. The matrix sum has units of inverse time for each direction.

Direction next: `hyp-mismatch-dynamics` should reveal whether tempo is used as a correction-rate coefficient in an ODE; if so, "correction tempo" may be more accurate than raw information acquisition.

Errors to watch: downstream scalar persistence conditions relying on an upper-bound tempo when channels are redundant or anisotropic; using scalar tempo where the matrix-Loewner condition is required; equating gain-weighted event rate with bits/sec.

What I would change: define scalar tempo as "quality-adjusted correction event rate" unless multiplied by expected event information content; alternatively add a normalized-event assumption.

Curiosity: the redundancy penalty is a strong conceptual addition because it prevents "more telemetry" from automatically counting as more adaptation.

New knowledge enabled: tempo is an upper-bound scalar unless channel independence and isotropy hold; the tensor form is the real object in high-dimensional settings.

Audit process change: the diagram should be a capacity funnel: raw channel rates enter, gain gates them, redundancy subtracts overlap, and anisotropy means the weakest direction may dominate persistence.

Value feel: high. This is a central definition and it carries many of its own caveats, though the information-rate wording remains loose.

## Diagram thought

A clear visual is an upper-bound funnel. Multiple channels contribute `nu_k eta_k`, but overlapping channels create a redundancy penalty before the effective tempo. Then a split into scalar and tensor outputs shows why a single number can overstate weak directions.
