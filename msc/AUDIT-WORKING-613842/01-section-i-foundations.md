# Section I Foundations

Segments read in this batch:

- `#def-agent-environment`
- `#def-action-transition`
- `#def-observation-function`
- `#def-chronica`
- `#form-agent-model`
- `#def-agent-spectrum`
- `#def-mismatch-signal`
- `#emp-update-gain`
- `#form-information-bottleneck`
- `#def-model-sufficiency`
- `#def-model-class-fitness`

## Predictions vs evidence

My initial prediction that the very bottom of Section I would be relatively clean is mostly holding.
The primitive definitions are short, legible, and mutually supportive.
No immediate contradiction has surfaced in the boundary / observation / transition / chronica layer.

My suspicion that `#form-information-bottleneck` might be overclaimed softened somewhat on read:
the segment is careful to distinguish "applied external theorem" from AAD-internal novelty.
That said, it still feels like a pressure point because the segment is doing two things at once:
stating the imported IB form exactly,
and adding qualitative claims about how $\beta$ varies with volatility and policy.
That mixed epistemic register is honest in prose but still slightly tense at the frontmatter level (`status: exact` on a segment whose own Epistemic Status paragraph contains a weaker subclaim).

## Cross-segment consistency notes

`#form-agent-model` is doing the expected representational work and cleanly signals that a complete state object is a modeling choice rather than a theorem.

`#def-mismatch-signal` introduces a useful ambiguity warning:
zero mismatch can mean adequacy, narrow sensing, or noisy blindness.
That warning may matter later if downstream segments read low mismatch too naively.

`#def-model-sufficiency` seems semantically more independent from IB than its frontmatter suggests.
The definition of a retained-predictive-information fraction does not appear to require `#form-information-bottleneck`; IB motivates why this quantity matters, but the quantity itself looks definable without first committing to the IB optimum.
This is not a final finding yet, but it is a watchpoint for dependency discipline vs genuine logical dependence.

## Math / status notes

`#emp-update-gain` is a good example of the framework's mixed-tier style:
frontmatter says `type: empirical`, `status: robust-qualitative`,
while the body honestly states "exact" for linear-Gaussian / conjugate cases and robust-qualitative more generally.
That feels directionally right.

The `#form-information-bottleneck` frontmatter may be slightly too flattened for the content:
there is an exact imported theorem core plus a robust-qualitative volatility claim.
Not necessarily wrong, but the segment compresses two epistemic tiers into one file.

## Predictions for next segments

I now expect the next bridge layer
`#post-causal-structure`,
`#form-event-driven-dynamics`,
`#def-adaptive-tempo`,
and the sector-condition derivation chain
to be where the framework begins either tightening or overextending.

Specific watchpoints:

- whether the event-driven and continuous-time framings line up without hidden assumptions
- whether the sector-condition machinery is explicit about which parts are derived vs assumed
- whether the clean Section I style survives once the theory starts translating between scalar intuition and matrix / nonlinear generality

## What I would change right now

If I were editing this layer for future auditors, I would consider separating `#form-information-bottleneck` into:

1. the exact imported IB statement as a pure formulation segment, and
2. the volatility / policy-relativity discussion as either a companion discussion segment or a visibly lower-tier subsection.

That would reduce the current "exact frontmatter, mixed-tier body" tension.
