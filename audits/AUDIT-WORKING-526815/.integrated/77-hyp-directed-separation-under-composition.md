# 77 - hyp-directed-separation-under-composition

Source: `01-aat-core/src/hyp-directed-separation-under-composition.md`

## First-pass understanding

This segment asks whether directed separation survives composition. The answer is organized around routing: if sub-agents process observations goal-blindly and the communication topology/protocol is goal-blind, the composite is intended to remain separated; if routing depends on composite goals, the composite becomes coupled because goal content shapes the information pathway.

The routing/content distinction from `scope-multi-agent` is doing useful work here. The main caveat is that composition adds a projection layer. A macro-agent update is not just sub-agent processing plus routing; it is those processes as seen through an admissible coarse-graining. That coarse-graining also has to avoid goal-conditioned information selection if the composite-level `f_M^c` is to be goal-blind.

## Diagram attempt

I drew directed separation under composition as a three-gate pipeline: sub-agent processing, routing infrastructure, and macro projection/update. The segment explicitly discusses the first two; the diagram marks the third as the missing condition needed for the Case 1 conclusion.

## Findings and watches

- F122 candidate: Case 1 concludes that individual goal-blind processing plus goal-blind routing implies `f_M^c` is independent of `G_t^c`. That also requires the macro projection/coarse-graining and macro update interface to be goal-blind. A goal-conditioned `Lambda`, goal-conditioned aggregation window, or goal-conditioned macro observation definition can reintroduce coupling even when sub-agent processing and routing are clean.
- F123 candidate: Case 2 treats goal-dependent routing as a directed-separation failure, but some routing changes can be goal-driven event selection or sensing policy, which directed separation explicitly allows at the single-agent level. The segment needs a sharper criterion separating allowed goal-dependent selection of what to observe from forbidden goal-dependent processing/infrastructure that changes how evidence is interpreted or admitted.
- F124 candidate: the LLM-composite discussion says a fixed-API multi-agent LLM system can be Case 1 at the composite level even though each LLM agent is individually Class 3. That contradicts the formal setup, which assumes each `A_i` satisfies directed separation individually. This may be a valid wrapper/coercion claim, but it belongs under the wrapper-derived special case, not the general Case 1 hypothesis as stated.
- F125 soft candidate: the segment inherits the earlier `R_t perp G_t^c` issue: for deterministic routing infrastructure, independence notation should be invariance or a random routing-selection condition.
- F126 soft candidate: "most composites of interest are Case 1" is plausible for some designed systems but overbroad. Military task organization, incident response, feature-team formation, and multi-agent AI orchestration often change channels and protocols by mission.
- Watch: the goal-information leakage distinction is valuable. Observations carrying information about goals through ordinary action-environment coupling should remain separate from directed-separation failure.

## Local verdict

The two-case taxonomy is useful, but the Case 1 theorem shape should become: goal-blind sub-agent processing, goal-blind routing, and goal-blind projection/update together preserve composite-level directed separation.
