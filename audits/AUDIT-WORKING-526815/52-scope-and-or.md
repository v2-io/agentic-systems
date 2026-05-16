# 52 - scope-and-or

Source: `01-aat-core/src/scope-and-or.md`

## First-pass understanding

This segment narrows strategy-node combination semantics to approximate AND and OR cases. AND means all parents are required; OR means any parent is sufficient. The motivation is parsimony: one edge parameter per parent rather than a full conditional table. The segment is honest that interactions, complementarity, substitutability, and richer thresholds are excluded or represented verbosely by nested structure.

The scope is plausible for many planning graphs, but the formulas assume more than just Boolean semantics: the AND and OR equations also assume a separable probability structure, roughly independent parent/path contributions unless later correlation machinery corrects it.

## Diagram attempt

The diagram separates three regions: pure AND, pure OR, and "outside current scope" for thresholds/interactions. I also show the parameter-count reason for the restriction: single-parameter edges are cheap, while full CPTs grow exponentially. The excluded region is important because it is not rare in real strategy work.

## Findings and watches

- Candidate finding: the assignment test "if I remove one parent, can `v` still be achieved? YES -> OR, NO -> AND" misclassifies threshold structures. For a 3-of-5 requirement, removing one parent may still leave success possible, but no single parent is sufficient. The test needs separate questions: are all parents necessary, is any one parent sufficient, or is this a threshold/interaction case outside pure AND/OR?
- Candidate finding: the parsimony discussion says AND/OR form a complete Boolean basis and are therefore the natural `O(k)`-parameter representation. Boolean functional completeness does not imply compact representation; arbitrary Boolean functions can require exponentially large AND/OR formulas or auxiliary nodes. The segment later acknowledges k-of-n verbosity, so the completeness claim should be softened.
- Watch: the displayed AND/OR probability formulas assume separable/independent parent contributions. Later correlation hierarchy must qualify these formulas under shared latent causes or correlated failures.
- Watch: continuous and multi-valued outcomes are explicitly open. Downstream strategy claims should not assume binary-node completeness outside this scope.

## Local verdict

The AND/OR restriction is a reasonable bounded-cognition modeling choice. It should be presented as a compact useful fragment, not as a compact representation of all Boolean strategy structure.
