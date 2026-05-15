# 03 - def-observation-function

Segment: `01-aat-core/src/def-observation-function.md` (`#def-observation-function`)

Dependencies: `def-agent-environment`, `def-action-transition`, both read. Dependency-order check passes.

## Segment Read

This segment installs the observation-side function $h$: observations are generated from environment state, prior action, and perceptual noise or limitation. The agent does not know either $h$ or the distribution of $\varepsilon_t$ exactly. It gives the observation boundary a concrete function while preserving the first segment's lossiness commitment.

The segment explicitly glosses observations as `aisthesis`, "raw contact with reality." That Greek phase vocabulary appears here before the full cycle is likely formalized. The formal target, however, is the observation function and the agent-relative opacity of that function.

## Predictions Vs Evidence

The evidence continues to match my prediction that Section I starts with plain primitives. I expected a lossy observation channel. The nuance is action-dependence: $a_{t-1}$ enters $h$, so observation is not purely passive. This matters for later causal information yield and for TST, where tooling choices alter what can be observed.

## Cross-Segment Consistency

This composes with the first two segments cleanly:

- `#def-agent-environment` establishes the information-loss boundary.
- `#def-action-transition` defines opaque action effects through $T$.
- `#def-observation-function` defines opaque observation generation through $h$.

The name `epistemic opacity` now appears as an observation-side cousin of `transition opacity`. I need to watch overload, because `agent opacity` and other opacity terms appear later in the outline. The modifier is doing essential work; bare `opacity` will not be safe.

## Naming Notes

`observation function` is ordinary and correct. I would likely keep it if targeted. It is standard enough not to need invention.

`epistemic opacity` is stronger as a named concept but may be broad. In this segment it specifically means the agent does not know $h$ or the noise distribution. Later segments may use "epistemic" for model uncertainty more generally, so I should verify whether this term is meant to remain local to observations or broaden to all hidden epistemic machinery.

`aisthesis` is introduced as the phase name for raw observation. I should not vote on it from this segment alone unless the target is simply the cycle phase vocabulary; the defining cycle segment may give the term its full role.

## What This Enables

This defines $\mathcal O$, $o_t$, $h$, and $\varepsilon_t$, which the mismatch signal and update-gain machinery will need. It also makes active perception possible because the previous action can shape the next observation.

For naming, it introduces a useful channel distinction: not every observation term should be named as if observations are passive readings. Some later TST/logogenic targets about observation design, prompt ordering, or ambiguity reduction likely depend on this active-observation allowance.

## Watchlist

- Whether `epistemic opacity` is consistently scoped to observation-function ignorance or becomes a broader umbrella.
- Whether `observation channel` and `observation function` are used interchangeably; they are adjacent but not identical.
- Whether action-dependent observation is picked up later as a design lever rather than treated as a footnote.

## Wandering Thoughts

This segment makes the first segment's boundary operational. The information-loss boundary is not a philosophical slogan; it is the many-to-one, noisy, partly action-conditioned map from world to observation. That is the right order: boundary first, function second.

The phrase "raw contact with reality" is doing more affective work than the equation. It explains why `aisthesis` might be worth the Greek register: it is not just a datum, it is contact. But the segment also refuses naive realism: contact is mediated by $h$ and noise. The name has to carry both immediacy and loss.

I am starting to see a possible good naming pattern across the primitives: ordinary standard terms for the formal machinery (`transition function`, `observation function`), memorable AAD-specific terms for the agent-relative epistemic properties (`transition opacity`, perhaps `epistemic opacity`), and Greek phase names for cycle roles. Mixing those layers would create noise.

For votes, this means I should be willing to keep a boring formal name at +1 or +2 and save stronger aesthetic judgment for the prose handles. Boring is sometimes exactly right when the term is a typed mathematical object.
