# 09 - def-pearl-causal-hierarchy

Segment: `01-aat-core/src/def-pearl-causal-hierarchy.md` (`#def-pearl-causal-hierarchy`)

Dependencies: `post-causal-structure`, `scope-agency`, both read. Dependency-order check passes. This segment resolves the forward references to Pearl/do-notation in the prior two scope/postulate segments.

## Segment Read

This segment imports Pearl's causal hierarchy into AAD's feedback-loop setting: Level 1 association, Level 2 intervention, Level 3 counterfactual. AAD's local contribution is not renaming the hierarchy; it grounds the hierarchy in temporal agent-environment structure and makes Level 2 structurally available once agency scope holds.

The availability/exploitation distinction is important. A system can structurally have Level 2 access without using it for dual-control-style information gathering. Software is framed as unusually rich because version control can make counterfactuals executable.

## Predictions Vs Evidence

My prior notes expected Pearl machinery to formalize the action-with-effect boundary. This segment confirms that and clarifies why the earlier `scope-agency` use of `do(\cdot)` was forward-looking rather than conceptually loose.

The part I underpredicted is the distinction between structural availability and exercised reasoning level. That will matter for names like `Pearl L3`, `Level 2 access`, and `causal information yield`: a name must not imply an agent actively reasons at a level just because the loop gives access to that level.

## Cross-Segment Consistency

This segment completes the chain:

- `#post-causal-structure` gives temporal possible-influence.
- `#scope-agency` requires action choice with interventional contrast.
- `#def-pearl-causal-hierarchy` names the levels of epistemic access that this structure makes available.

No contradiction. It also retrospectively explains the do-operator references that appeared before the formal Pearl definition. I still think fresh readers may feel the ordering strain, but it is now locally resolved.

## Naming Notes

`Pearl's Causal Hierarchy` should be kept. This is adopted prior-art terminology; inventing an AAD-specific replacement would obscure provenance.

For abbreviated targets, I will prefer `Pearl Level 1/2/3` or `Pearl L1/L2/L3` over generic `Reasoning` labels, because "reasoning" loses the strict hierarchy and prior-art anchor. However, the prose names association/intervention/counterfactual are essential for first encounter.

`Level 3 access` in software probably needs care. Executable counterfactuals via `git checkout` are a domain instantiation, not a claim that every software task gets perfect Level 3 reasoning.

## What This Enables

This defines the causal hierarchy requirement, loop interventional access, CIY, regret, and TST's tests/deploys/git claims. It also gives the naming pass a provenance discipline: external theorem/standard terms keep their standard names when used faithfully.

## Watchlist

- Candidates that rename Pearl's hierarchy without preserving Pearl.
- Names that collapse availability into exploitation.
- Software counterfactual names that overclaim exactness outside versioned/replayable code paths.

## Wandering Thoughts

This segment is a good example of AAD integrating rather than inventing. The hierarchy is Pearl's; AAD's move is to show where it lives inside the adaptive loop. The right name therefore needs to signal adoption and local grounding, not novelty.

The availability/exploitation distinction feels especially important for language agents. LLMs may have textual access to counterfactual reasoning patterns, but whether their architecture exercises Level 3 in an AAD-relevant way is a separate question. A name like `Pearl L3` carries enough rigor to resist loose anthropomorphic readings.

I also like how software appears here as a concrete counterfactual laboratory. `git checkout` is not a metaphor; it actually lets a developer re-enter an alternate code state and run tests. That may explain why TST is the calibration laboratory rather than just another domain example.

For voting, this segment tells me to be conservative: standard causal-inference names are not places to be cute. The project gains credibility by importing them cleanly and naming its own contribution around the integration boundary.
