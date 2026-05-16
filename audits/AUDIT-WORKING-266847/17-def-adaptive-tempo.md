# Reflection: def-adaptive-tempo

## What the segment does

Defines adaptive tempo $\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)*}$ as the product of observation frequency and update quality, summed across channels. The key claim: high noise depresses gain, so you can't outrun a bad observation channel by iterating faster.

## Naming targets surfaced

"adaptive tempo" is probably a voting target — it's one of the core terms. Let me check the tracker... I don't see "adaptive tempo" as a row directly. But row 22 is "tempo composition" and row 94 is "extreme transition motif." And row 26 was "cadentia" which is the channel rate.

Looking at the overall card structure — adaptive tempo ($\mathcal{T}$) might be treated as a settled term rather than a voting target, since it appears in the LEXICON as a key quantity. Worth checking.

## The channel independence assumption

The segment explicitly flags that the additive formula overcounts when channels are correlated: $\mathcal{T} \leq \sum_k \nu^{(k)} \cdot \eta^{(k)*}$ with equality iff channels are independent. This is an honest scope condition on the additive formula — it's an *upper bound*, not an exact formula, when channels overlap.

The redundancy penalty involves mutual information between channel event streams. This is mathematically precise but practically difficult to compute. The segment acknowledges this is an open problem (not yet a tracked result).

## The per-dimension persistence point

The closing observation about scalar vs vector tempo: in anisotropic systems, scalar $\mathcal{T}$ overestimates effective adaptation along weak dimensions. The simulation shows 72% overestimation with 5:1 gain variation. This is a significant practical concern for the persistence condition's applicability.

The per-dimension persistence result (`#result-per-dimension-persistence`) is referenced — this appears to be a tracked result, but it's not in the Section I OUTLINE I've read. Let me note this as potentially a Section I result that I should encounter when walking further.

## The Boyd connection

"You cannot outrun a bad observation channel by iterating faster" — this grounds Boyd's emphasis on Orient quality over raw OODA speed. The tempo formulation makes this precise: $\eta^*$ is the quality term, and high $U_o$ collapses $\eta^*$ regardless of $\nu$.

The military domain instantiation is frequent and useful in this segment. Boyd's OODA loop is a natural analog, and the formalization adds precision.

## Naming thoughts

"Adaptive tempo" is a good name:
- "Adaptive" — it's the rate at which adaptation occurs
- "Tempo" — musical rhythm of the cycle, borrowed from military/music usage

The name is established and appears widely. The relationship to musical tempo (beats per minute) and to military tempo (pace of operations) is apt. No obvious collision issues. This is probably a keep.

## Wandering thoughts

The speed-quality substitutability is interesting strategically: an agent can achieve the same tempo through either fast/noisy or slow/careful approaches. This has implications for system design — if you have high observation noise, increasing cycle speed is wasted effort; improving observation quality (or model quality) is the correct intervention.

The redundancy penalty for correlated channels is underappreciated. In practice, most real systems have correlated observation channels: weather sensors near each other, multiple team members observing the same situation, repeated reports from the same source. The additive formula is taught as the formula, but it's actually an upper bound that can significantly overstate effective correction capacity.

For multi-agent systems, this creates a design problem: adding more agents to a composite doesn't linearly increase tempo if they're observing the same environment from similar positions. The diversity of observation perspective matters, not just the count of observers.

How valuable: 6/10 for surprise (the channel independence caveat and per-dimension concerns are more explicit than expected), 8/10 for load-bearing.
