# 11 - form-agent-model

Segment: `01-aat-core/src/form-agent-model.md`
Dependencies: `def-agent-environment`, `def-observation-function`, `def-chronica` - satisfied.
Status observed: `type: formulation`, `status: robust-qualitative`, `stage: deps-verified`.

## Reflection

This segment cleanly commits to `M_t = phi(C_t)` as a modeling choice rather than a theorem. I appreciate the status honesty: it does not claim every agent literally stores an explicit "model" object, only that any retained history relevant to future behavior can be represented as a complete epistemic substate. That makes the formulation broad without pretending to be uniquely forced.

The completeness assumption is the load-bearing move: anything not in `M_t` is lost to the agent. External memory, retrieved documents, or a context window can still be included if they are available to policy/update at time `t`, but the formalism has to count them inside `M_t` rather than as an extra hidden reservoir. The only small concern is notation drift: the chronica is written as `(o_1, a_1, ..., o_t)`, less precise than the earlier `(o_1,a_1,o_2,...,a_{t-1},o_t)`. Probably harmless shorthand, but worth watching because decision-time order matters.

## Prompt pass

Predictions vs evidence: I expected `M_t = phi(C_t)` and a completeness assumption. Both appeared. The segment is more careful than feared about formulation vs derivation.

Cross-segment consistency: consistent with `def-chronica` and the reality-model intro. It still uses "agent" in broad Section I mode, inheriting F1 vocabulary pressure but not worsening it.

Math verification: no computation. The mapping type is schematic; many-to-one compression is plausible. It says "multiple distinct histories may produce the same model state," which leaves room for identity compression as a degenerate no-compression case.

Direction next: `form-information-bottleneck` should specify the target variable for optimal compression. I expect future observations to be the target, and I will watch whether "purpose" leaks in too early.

Errors to watch: hidden retained information outside `M_t`; history-based policies being dismissed despite the segment admitting them; treating PID's impoverished model as both inside and outside Section I adaptive machinery without scope clarity.

What I would change: use the exact chronica ordering in the bullet to avoid weakening the temporal-order discipline so soon after `def-chronica`.

Curiosity: whether `M_t` includes the update algorithm/architecture or only its current epistemic content. Class fitness later may need the model class/architecture separate from the state instance.

New knowledge enabled: sufficiency can now be formalized as retained predictive content in `M_t` relative to `C_t`, and mismatch can be a comparison between predictions generated from `M_t` and later observations.

Audit process change: add notation-drift watch for chronica shorthand.

Running outline change: external memory watch mostly resolved if all accessible memory is included in `M_t`; keep an eye on model state vs model class.

Value feel: high. This is the representation hinge for nearly all later dynamics.

## Diagram thought

The useful picture is a many-to-one map from several chronicae into one model state, surrounded by a boundary: everything retained is inside `M_t`; anything outside no longer participates in the agent's update/policy unless reintroduced by observation or retrieval and therefore counted in the current state.
