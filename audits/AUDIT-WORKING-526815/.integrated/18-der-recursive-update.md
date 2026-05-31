# 18 - der-recursive-update

Segment: `01-aat-core/src/der-recursive-update.md`
Dependencies: `form-agent-model`, `form-event-driven-dynamics`, `deriv-recursive-update` - first two satisfied; `deriv-recursive-update` not yet reached in outline order.
Status observed: `type: derived`, `status: conditional`, `stage: claims-verified`.

## Reflection

The core derivation is sound in the definitional sense the segment itself states: if `M_t` is the complete retained model state, then updating from `M_{\tau^-}` and the incoming event is sufficient by construction. Any counterexample that consults retained history outside `M_t` just shows that `M_t` was too narrow. This is a useful clarification because it keeps the recursion claim from pretending to be an empirical discovery about all agents.

The main issue is order/dependency discipline. The segment declares `deriv-recursive-update` as a dependency, but that proof artifact is not yet in the AAT outline position I have reached. It also imports `form-consolidation-dynamics`, `schema-strategy-persistence`, and stability-plasticity language inside the between-event discussion. The formal core does not need those later concepts; the consolidation paragraph feels like downstream enrichment embedded in an early derived result.

## Prompt pass

Predictions vs evidence: I expected the pre/post event update equation from the prior formulation. The segment gives that equation and adds autonomous between-event dynamics `dM/dtau = g_M(M_tau)`.

Cross-segment consistency: consistent with `form-agent-model` if `M_t` is treated as complete retained state. It reinforces the earlier "anything retained must be in `M_t`" principle. It also helps the chronica distinction: the full chronica is not reprocessed unless compressed into the current model.

Math verification: the event update is a definitional Markovization. The between-event ODE is plausible, but `g_M(M_tau)` may need explicit allowance for elapsed time, scheduled actions, or in-flight commitments unless those are included in `M_tau`.

Direction next: `der-action-selection` should show whether the same complete-state logic is being applied to action, and whether goals/policies are in `M_t` or a separate agent state.

Errors to watch: claiming recursion as substantive necessity when it is mostly definitional; relying on the later proof artifact before it appears; importing consolidation results into the local chapter before their scope has been established.

What I would change: split the consolidation paragraph into a short forward pointer and keep the early segment focused on event recursion and autonomous state evolution.

Curiosity: the phrase "epistrophe" adds conceptual flavor, but the operative theorem is really state completeness -> Markov update. The theory may benefit from keeping that theorem visually simple.

New knowledge enabled: I now understand `M_t` as a compression boundary: outside-history access is not forbidden, it is reclassified as part of state if retained.

Audit process change: for this segment the diagram should expose a hidden-variable test: if the update needs raw chronica, then the missing memory must be folded into `M_t`.

Value feel: medium-high. The local result is strong as a definition, while the dependency hygiene is weaker than the math.

## Diagram thought

The best diagram is not a generic loop; it is a compression-boundary picture. Full chronica feeds the current complete model. Once that compression has happened, the next event only touches the model state. A dashed forbidden edge from raw chronica to the update can show the counterexample case: if that edge is real, the information belongs inside `M_t`.
