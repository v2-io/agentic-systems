# Sector Chain

Segments read in this batch:

- `#post-causal-structure`
- `#form-event-driven-dynamics`
- `#def-adaptive-tempo`
- `#deriv-sector-condition`
- `#deriv-gain-sector`
- `#der-gain-sector-bridge`

## Predictions vs evidence

My expectation that Section I would start tightening once it hit the tempo / sector bridge is correct.
This is where the framework becomes both more impressive and more vulnerable.

The good news:

- `#deriv-sector-condition` is substantially more careful than a casual outline reading would suggest.
- The α/β sub-scope split is explicit.
- The bridge from update geometry to sector condition is not handwaved; it is genuinely argued.

The first substantial concern:

- `#def-adaptive-tempo` appears internally unstable as a definition.

## Candidate finding watchpoint: tempo definition vs correlation caveat

`#def-adaptive-tempo` formally defines

$$\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)\ast}$$

with no stated scope restriction in the definition itself.

But the Discussion then says:

- the additive formula assumes informationally independent channels
- correlated channels make the additive formula overcount
- the "correct tempo" merely satisfies
  $\mathcal T \leq \sum_k \nu^{(k)} \eta^{(k)\ast}$
  with equality only under independence

That is not just a gentle caveat.
It says the segment's own Formal Expression is, in correlated settings, not the thing the segment later calls the correct quantity.

This could resolve in one of three ways:

1. the definition is intended only for the independence sub-scope and the segment needs frontmatter / formal-expression scope tightening
2. the additive expression is intended as an upper-bound proxy rather than the definition of tempo
3. later segments introduce a repaired definition and this segment is stale

I need to check downstream usage before elevating it to a formal finding, but this is currently the strongest issue in the audit so far.

## Other cross-segment notes

`#form-event-driven-dynamics` and `#def-adaptive-tempo` fit together conceptually, but the event-driven segment also inherits the same additive-channel optimism.
So if the tempo definition is unstable, the event-driven formulation may be propagating that instability.

`#post-causal-structure` is broader than a pure time-ordering postulate.
The later Discussion starts shading toward weighting update rules by action-contingent informativeness.
That is plausible, but it is more than the primitive time-arrow claim named in the postulate.
Not a finding yet, just a place where interpretation may be doing extra work beyond the formal core.

## Math / status notes

`#deriv-sector-condition` is one of the stronger segments read so far.
It is explicit about what is proved, what is assumed, and where AAD is importing standard mathematics rather than claiming novelty.

`#der-gain-sector-bridge` is also better than my pre-read suspicion:
it does not pretend B1 is universally forced.
It marks the exact conditionality and uses failure modes honestly.

That said, both segments carry mixed material:

- exact downstream Lyapunov proofs
- sub-scope architecture
- broader lineage positioning

They remain readable, but the amount of content compressed into single segments raises the chance that later segments will cite only the punchline and not the caveats.

## Predictions for next segments

I now expect the next likely high-yield areas to be:

1. the discrete-time bridge, where order terms and approximation claims can go wrong
2. the persistence summary segments, where caveats from the appendices may get compressed into cleaner slogans
3. the simulation / exponent transfer chain, where deterministic and stochastic scalings are turned into regime claims

I also now expect `#disc-independence-audit` to matter later, because the tempo definition already appears to need exactly the kind of dependence-aware repair that such a segment would discuss.
