# 04 - def-chronica

Segment: `01-aat-core/src/def-chronica.md`
Dependencies: `def-agent-environment`, `def-observation-function`, `def-action-transition` - satisfied.
Status observed: `type: definition`, `status: axiomatic`, `stage: deps-verified`.

## Reflection

Chronica is the first genuinely temporal object: not a state, not a model, but the append-only ordered record from which any state/model must be built. The segment makes a strong and useful distinction between complete raw interaction history and the compressed internal model that will come next. I like the sequence ending at `o_t` after `a_{t-1}` because it encodes what the agent could and could not have known at decision time.

The non-forkability discussion is conceptually important but slightly ahead of the formal content. The definition supports "future histories diverge after copying"; it does not yet by itself prove all identity/continuity claims, and the segment appropriately points to `scope-agent-identity`. The Working Notes introduce implementation distinctions and prior-audit language inside the segment; I am treating that as data rather than audit-target prose, but it is a reminder that future readers of `src` are not fully insulated from downstream/prior frames even under de-novo discipline.

## Prompt pass

Predictions vs evidence: I expected a complete history sequence feeding model compression. That is exactly what appeared. The extra insight is ordinal-not-metric time: chronica records event order, not wall-clock duration.

Cross-segment consistency: consistent with the first three definitions. It depends on having both observations and actions defined. It forward-references `form-agent-model`, `def-model-sufficiency`, and `scope-agent-identity`, which is natural because chronica is upstream of them.

Math verification: no calculation. The ordering `(o_1,a_1,...,a_{t-1},o_t)` is coherent if `C_t` denotes post-observation/pre-next-action history.

Direction next: `scope-adaptive-system` should turn this machinery into the broadest scope condition. I expect it to ask what subset of agent-environment couplings count as adaptive rather than merely reactive or perfectly informed.

Errors to watch: identity claims outrunning chronica's definition; downstream models forgetting that `M_t` is a compression, not the raw history; metric-time claims being imported into event-indexed chronica without a tempo bridge.

What I would change: perhaps move most of the logogenic TRACTUS/CHRONICA implementation Working Notes to a sidecar when tooling supports it. They are useful, but they create de-novo priming within an early foundational segment.

Curiosity: whether future persistence/identity claims require `M_t` to retain temporal depth, or whether the raw existence of `C_t` is enough. The segment hints that continuity persistence requires both continuous chronica extension and `M_t` temporal depth.

New knowledge enabled: after this segment, "everything the agent can know" can be evaluated as a function of a causal record, not an omniscient world state. This sets up compression/sufficiency as formal loss relative to a record.

Audit process change: track "Working Notes bleed" where segment-local notes import downstream or prior-audit frames. This is not a violation of the protocol, but it affects the first-encounter experience.

Running outline change: add event-index vs metric-time watch; this could matter for adaptive tempo.

Value feel: high. It gives the theory an internal time axis and a clean substrate for model compression.

## Diagram thought

The most illuminating diagram is not a loop but a timeline: an append-only alternating sequence with a compression map into `M_t`, and a fork point showing that copied agents share past chronica but immediately diverge under different future observations/actions. This captures both the formal definition and the identity intuition.
