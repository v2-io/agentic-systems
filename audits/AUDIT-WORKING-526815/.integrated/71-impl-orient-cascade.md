# 71 - impl-orient-cascade

Source: `01-aat-core/src/impl-orient-cascade.md`

## First-pass understanding

This segment closes Part II by making the orient cascade the organizing claim for strategy dynamics: mismatch reaches local epistemic state, then edge confidence, then strategy topology, then policy. The useful synthesis is that exploration is driven from both sides. Uncertainty asks for information where the model knows it is weak, while persistent overconfidence or drift asks for exploration precisely where the model thinks it is already settled.

The chapter is also where the AAT story becomes explicitly architectural. Class 3 substrates are treated as needing scaffolded loops because representation, attention, and self-revision are coupled; the scaffold supplies the separation, logging, replay, and directed exploration needed to recover the cascade. That is plausible as an AAT-guarantee story, but the local chapter imports much of its warrant from deferred appendix/proof homes.

## Diagram attempt

I drew the chapter as a three-zone proof-flow diagram: local anchors already read, deferred proof homes not yet read, and architectural prescriptions. The most important visual decision was to route the strongest claims through the deferred homes rather than directly from the local synthesis.

## Findings and watches

- F88 candidate: `impl-orient-cascade` is discussion-grade but presents several proof-bearing claims as if settled by the chapter: survival-imperative exploration, causal-IB LMI structure, bias-bound constants, Section II survival counts, and the scaffolding requirement. These may be supported later, but proof credit should remain with the declared future homes.
- F89 candidate: the claim that scaffolded loops are structurally necessary for Class 3 substrates is too broad if read literally. The local argument supports a narrower claim: scaffolding is needed to recover AAT-grade cascade guarantees under coupled representation, attention, memory, and action channels.
- F90 candidate: saying deliberation is "Pearl-do on a simulated trajectory" is conceptually evocative but too strong. Pearl's `do` operator is an intervention in an SCM; simulated deliberation is better described as model-internal counterfactual intervention or policy/model simulation.
- F91 candidate: the statement that deliberation does not relax the bandwidth floor and leaves total Shannon rate unchanged needs scope. Internal computation cannot replace external information indefinitely, but better policies, sensing, compression, and model selection can change the effective disturbance, allocation, or required rate.
- F92 soft candidate: the dual exploration laws `lambda_info proportional U_M` and `lambda_surv proportional 1/U_M` depend on future derivation homes. Keep them as a synthesis target until `deriv-causal-ib-exploration` and related segments are read.
- Watch: the claim that prompt engineering reduces ambiguity `A` and therefore bias fits the narrative, but the quantitative status depends on the future observation-ambiguity bias-bound derivation.
- Watch: the Section II transfer/survival counts are useful if real, but they should not be used as evidence until `result-section-ii-survival` is read.

## Local verdict

The segment works well as a chapter-end map. Its strongest engineering recommendation is probably sound in bounded form: if a system has coupled opaque channels, add instrumentation and scaffolded loops to recover directional correction. The audit risk is that the summary voice sometimes outruns the proof homes it cites.
