# 14 - def-model-class-fitness

Segment: `01-aat-core/src/def-model-class-fitness.md`
Dependencies: `def-model-sufficiency` - satisfied.
Status observed: `type: definition`, `status: axiomatic`, `stage: deps-verified`.

## Reflection

The definition is simple and useful: class fitness is the supremum of model sufficiency over the representable model class. This cleanly separates "this instance is bad" from "this representational family cannot do the job," which is exactly the bridge needed for structural adaptation later.

The caveat I expected is now concrete. `def-model-sufficiency` made `S(M_t)` policy-relative and trajectory-relative; this segment defines `F(Mclass)` as if it were a property of the class alone. Formally, the dependency should carry the relativity through: class fitness is the ceiling of a class on a specific prediction task, under a policy/continuation convention, along a trajectory or data-generating distribution. This may be obvious by inheritance, but because structural adaptation will be load-bearing, I want the segment itself to say it.

## Prompt pass

Predictions vs evidence: I expected a supremum over sufficiency and a structural-inadequacy condition. That is exactly what appeared.

Cross-segment consistency: mostly consistent with `def-model-sufficiency`, but it under-propagates sufficiency's policy/trajectory relativity. The prose says "represent reality," while the formal object measures retained predictive information about future observations.

Math verification: no computation. The supremum definition is straightforward. If `S` is undefined in prediction-vacuous regimes, `F` should also be undefined there by inheritance; the segment does not restate this.

Direction next: the next chapter should move from static representation into event-driven dynamics. I expect `M_t` to become recursively updated, and the completeness assumption will matter.

Errors to watch: later structural-adaptation claims treating low class fitness as an objective fact about architecture independent of policy, trajectory, horizon, or observation target.

What I would change: define something like `F(M; C_t, pi_cont)` or add one sentence: "All policy/trajectory/well-definedness clauses from `S` are inherited." Also replace "represent reality" with "retain predictive information for the task" when precision matters.

Curiosity: whether an agent can detect low `F` or only infer it from persistent mismatch under assumptions about adequate learning. The segment names the latter, which will need careful assumptions later.

New knowledge enabled: structural adaptation can be framed as hitting a class ceiling rather than merely failing to optimize parameters.

Audit process change: add a candidate/watch item for caveat propagation from definitions to derived results.

Running outline change: add F4 candidate only as a soft scope-propagation candidate pending `result-structural-adaptation-necessity`.

Value feel: high. The definition is compact but load-bearing for the whole "wrong kind of model" branch.

## Diagram thought

The diagram should show models as points with different sufficiency heights under a class ceiling. Parameter learning climbs within the class; structural change moves to a different class with a higher ceiling.
