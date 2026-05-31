# 19 - der-action-selection

Segment: `01-aat-core/src/der-action-selection.md`
Dependencies: `form-agent-model`, `der-recursive-update` - satisfied.
Status observed: `type: derived`, `status: exact`, `stage: deps-verified`.

## Reflection

This segment directly answers the earlier concern about action depending on `M_t` alone. It says the Section I form works because, in that scope, `M_t` is the complete internal state; for purposeful agents the state is lifted to `X_t=(M_t,G_t)` and action becomes `pi(M_t,G_t)`. That is the right structural resolution: action depends on complete internal state, not necessarily on epistemic model alone.

The cost is that the resolution imports Section II machinery before its outline position. The formal expression and epistemic status cite `form-complete-agent-state`, and discussion cites Pearl hierarchy, deliberation cost, persistence, agent spectrum, directed separation, and TST temporal optimality. The core derivation only needs completeness plus policy mapping; the action-fluency theory is valuable but is carrying a lot of downstream load in an early Section I segment.

## Prompt pass

Predictions vs evidence: I expected this segment to either confirm or fix the `M_t`-only action issue. It fixed it cleanly by distinguishing Section I complete state from Section II lifted state.

Cross-segment consistency: consistent with `der-recursive-update`: complete retained state is enough for next update and action. It also protects `def-model-sufficiency` from being forced to include goals by moving purposeful state into `G_t` later.

Math verification: deterministic and stochastic policy forms are standard. The "formal characterization of action fluency" using `Delta eta^*(Delta tau)` is less clearly typed, because `eta^*` has so far been previewed as update gain rather than action value or expected outcome quality. This may be resolved in `der-deliberation-cost`, but it is a notation watch.

Direction next: `def-mismatch-signal` should return to prediction error and should clarify whether mismatch is an observed scalar, vector, norm, or information-theoretic surprise.

Errors to watch: action fluency accidentally conflating update gain with action quality; Section II concepts doing formal work before their definitions; "model acts" language making `M_t` too broad unless the Section I/II split is kept explicit.

What I would change: keep the early formal result as `a_t ~ pi(. | X_t)` with a Section I specialization `X_t=M_t`, then make action fluency a forward-linked discussion box.

Curiosity: the implicit/explicit distinction is useful; it gives a bridge from OODA and RL planning to tempo without claiming all action is deliberation.

New knowledge enabled: the framework's answer is "complete-state policy," not "epistemic-state-only policy." That rescinds the strongest version of my earlier action-selection worry.

Audit process change: the diagram should show two layers: an exact policy derivation at the top and a lower fluency axis as a qualitative add-on.

Value feel: high for conceptual clarity; medium for local outline hygiene.

## Diagram thought

The fastest clear representation is a scope-switch diagram. In Section I, `X_t=M_t`, so policy reads `M_t`. In Section II, `X_t=(M_t,G_t)`, so policy reads both model and purpose. Under that, a separate fluency axis can show implicit action as cheap policy evaluation and explicit action as policy plus deliberative search.
