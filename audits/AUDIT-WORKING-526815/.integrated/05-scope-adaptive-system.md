# 05 - scope-adaptive-system

Segment: `01-aat-core/src/scope-adaptive-system.md`
Dependencies: `def-agent-environment`, `def-observation-function`, `def-chronica` - satisfied.
Status observed: `type: scope`, `status: axiomatic`, `stage: claims-verified`.

## Reflection

This segment does what I expected the broadest scope to do: it defines Section I around observation under residual uncertainty, not around goals or interventions. The formal scope is admirably small: observations exist and `H(Omega_t | C_t) > 0`. This also resolves part of my earlier worry about `def-observation-function`: passive Bayesian learners and Kalman filters are explicitly included, so AAT is not trying to be only an action/control theory at the adaptive-system layer.

But that resolution creates a sharper cross-segment tension with the first definition. `def-agent-environment` says an agent must produce actions that affect `Omega`; this segment says adding causal action narrows to agency and explicitly includes passive observers/no-control Kalman filters. Those cannot both be literally true unless the first definition's "agent" is broader than its condition 3, or passive systems have a null/nominal action channel that does not affect `Omega`, which would violate the wording "actions that affect." This is the first candidate finding I can defend from first-hand segment text, though it may be resolved by `scope-agency` or later terminology.

## Prompt pass

Predictions vs evidence: I predicted a broad uncertainty/observation scope and got it. I also predicted the agent/agency terminology tension, and this segment confirms it more strongly than expected.

Cross-segment consistency: candidate inconsistency with `def-agent-environment`. Anchor passages: `def-agent-environment.md:19-23` requires action effect; `scope-adaptive-system.md:14`, `:27`, and `:35` say causal action is a narrowing and passive observers are included.

Math verification: no calculation. The entropy condition is conceptually clear but will need later compatibility checks. For instance, if a learner eventually reaches `H(Omega_t | C_t)=0` at some times but remains adaptive under future drift, does it exit scope instantaneously? Probably the framework later handles non-stationarity, but this is worth watching.

Direction next: `scope-agency` should clarify whether agency is a subset of adaptive systems with causally contrastive actions. If it does, the first definition likely needs to be rephrased from "agent" to "coupled system" or make action optional/degenerate at Section I scope.

Errors to watch: downstream Section I claims saying "agent action" when they mean "adaptive-system update"; passive examples quietly relying on action-transition definitions; causal information yield applied to adaptive-scope systems without the agency narrowing.

What I would change: revise `def-agent-environment` so the broad Section I entity receives observations and maintains internal state, with an optional action channel introduced by `def-action-transition` and activated by `scope-agency`.

Curiosity: whether `scope-agency` treats nominal actions/no causal effect as outside agency but still inside adaptive scope. The final sentence here says yes, which strengthens the need for a more neutral term than "agent" in the broad scope formula.

New knowledge enabled: AAT's outermost layer can analyze passive learning. That matters because persistence/mismatch/update gain are not hostage to actuation.

Audit process change: promote the agent/action tension from watch list to live finding candidate pending `scope-agency`.

Running outline change: add candidate finding F1.

Value feel: very high. This is where the scope lattice starts, and it materially changes how the earlier definitions should be read.

## Diagram thought

The clearest diagram is a nesting mismatch: this segment wants `adaptive systems` as the outer set and `agency` as the action-bearing subset, while `def-agent-environment` made action-bearing part of the outer agent definition. A Venn/set diagram exposes the issue faster than prose.
