# 58 - der-causal-insufficiency-detection

Source: `01-aat-core/src/der-causal-insufficiency-detection.md`

## First-pass understanding

This segment gives the formal home for the earlier on-policy L0-insufficiency no-go. Under sequential short-circuit execution, censored sibling observation, no latent interventions, and no structural priors, a latent-common-cause L1 world can be matched by an L0 world on the observable on-policy regime distribution. Therefore any statistic of that on-policy history alone fails to distinguish them. The segment is careful to call the exact result shallow and strict-prerequisite, with broader topologies treated as robust qualitative transfer.

The constructive side is the boundary map: violate one of the no-go conditions to get detection signal. The canonical AAT route is joint sibling observability under exploration, tested by sibling covariance after edge credences stabilize. This is a good conceptual bridge from "exploration is useful" to "some exploration is structurally required for self-diagnosis."

## Diagram attempt

The no-go is best illustrated as two worlds funneled into the same censored on-policy trace. The escape routes are drawn as side doors that add the missing joint or structural information. This makes the theorem's force clearer than another covariance-test table.

## Findings and watches

- F48 candidate: the segment repeatedly frames on-policy data as Pearl Level 1 and loop/exploration data as supra-Level-1. But AAT actions are already physical interventions; the exact no-go seems better grounded in fixed-policy regime equivalence plus short-circuit censoring, not in a simple observational-vs-interventional split. This is the local version of the earlier data-character vs identified-intervention concern.
- F49 candidate: the covariance detector is stated with `H_1: Cov > 0` under causal insufficiency. Positive covariance is a sufficient detector for shared enabling causes, not a necessary signature of all latent common causes. The later "negatively-correlating latents" caveat helps, but the primary hypothesis statement should say "positive shared-enabler insufficiency" or similar.
- F50 soft candidate: the L1 construction step says joint failure excess localizes the common cause's frequency. Covariance alone generally underdetermines latent frequency and conditional rates unless strict-prerequisite/binary/single-latent assumptions are retained or additional observations/priors are supplied.
- Watch: the route table invokes `deriv-edge-credence-dynamics`, `der-observability-dominance`, and `example-L1` without declaring them in dependencies. Some are boundary or example references, but `SA3` exploration is doing real work in the detector.
- Watch: the "unique broadly-available" language should be kept scoped to the five named conditions. External instrumentation, designed experiments, or richer observability are alternatives when available; the segment mostly handles this through routes (c)-(e).

## Local verdict

The no-go is one of the cleaner formal claims so far because it names its censoring and policy conditions. The main audit pressure is not on the shallow construction; it is on how broadly later text treats the covariance route and Pearl-level framing.
