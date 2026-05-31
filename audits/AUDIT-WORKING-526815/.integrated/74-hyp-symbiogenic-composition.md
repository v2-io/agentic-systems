# 74 - hyp-symbiogenic-composition

Source: `01-aat-core/src/hyp-symbiogenic-composition.md`

## First-pass understanding

This segment proposes symbiogenesis as an asymmetric way composites come into being: a host absorbs another agent, transfers useful structure into the host, and reduces the absorbed entity's autonomy until its objective becomes a derived role inside the host objective. It is explicitly hypothesis-tier, and it helpfully separates objective absorption, function transfer, and autonomy reduction.

The conceptual contribution is strong because it describes a state-transforming process, not merely a projection of a fixed multi-agent system. The hard parts are all typing questions: whether the absorbed entity remains an AAT sub-agent, whether the examples are actually agents, and whether the final object is objective-based composition or just a single agent with an internal component.

## Diagram attempt

I drew the process as three simultaneous contractions across time: objective absorption, function grafting, and autonomy reduction. The output is deliberately shown as a typed ambiguity: either a composite with a subordinate agent, or a host system with an integrated component if agency falls below the scope threshold.

## Findings and watches

- F102 candidate: after symbiogenesis, the endosymbiont is said to persist as a specialized sub-component "not as an independent agent," while `scope-composite-agent` was defined over sub-agents each satisfying `scope-agency`. If autonomy reduction takes the absorbed entity below agency scope, the result is not clearly a composite agent under the preceding segment; it may be a single agent with an internal component.
- F103 candidate: several listed examples do not obviously start with two purposeful agents satisfying `scope-agency`. Adopted vocabulary, grammar, legal precedent, and religious elements can be structures, not agents with observations/actions/objectives. These are useful analogies, but the formal example class should distinguish agent absorption from structure grafting.
- F104 soft candidate: S-1 assumes `O_e -> D_e(O_h)` and the integrated objective `O_c approx O_h`. That covers host-dominant absorption, but not cases where the composite objective emerges by mutual transformation of both parties. If "symbiogenesis" is meant broadly, the host-dominance assumption should be explicit.
- F105 candidate: S-2 uses set union `M_h, Sigma_h union F(M_e, Sigma_e)` across model and strategy structures. The operation needs a typed merge/grafting semantics with conflict resolution, interface mapping, and possible overwriting; ordinary union is too weak for integrated state.
- F106 soft candidate: the claim that no pre-symbiogenic projection `Lambda` can yield the post-symbiogenic composite because `O_e` changes is too strong. A static projection of the pre-state cannot, but a dynamical transition or time-indexed projection could represent the change. The distinction should be state transformation versus fixed projection, not projection impossibility in general.
- F107 candidate: the segment imports future composition and appendix homes (`form-composition-closure`, `result-structural-adaptation-necessity`, `result-unity-closure-mapping`, `deriv-critical-mass-composition`, `def-shared-intent`) beyond declared dependencies. The text often labels these as open or conditional, which is good, but proof credit should remain deferred.
- Watch: the saddle-node threshold is appropriately marked conditional on deriving the `+k delta^2` coordination penalty. Keep it as formulation until that derivation exists.

## Local verdict

The mechanism is worth keeping, but it needs a sharper type distinction: absorbing an agent into a component, forming a hierarchical composite of still-agentive sub-agents, and grafting non-agentic structure are different transitions.
