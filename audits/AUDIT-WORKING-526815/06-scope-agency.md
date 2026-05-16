# 06 - scope-agency

Segment: `01-aat-core/src/scope-agency.md`
Dependencies: `scope-adaptive-system`, `def-action-transition` - satisfied.
Status observed: `type: scope`, `status: axiomatic`, `stage: claims-verified`.

## Reflection

This segment is clean as a scope definition: agency is adaptive scope plus at least binary choice plus at least one Pearl-style interventional contrast. The passive/nominal distinction is especially useful: a system can observe, model, and update under uncertainty without being an agent in the Section II/III sense. This is exactly the layered structure I wanted after `scope-adaptive-system`.

It also hardens the earlier terminology issue. `def-agent-environment` defined an agent as action-bearing, but this segment says passive observers are adaptive-only and still inside AAT's broadest scope. That means the word "Agent" in the formal set `(Agent, Omega)` is overloaded: sometimes it means the broad epistemic system in Section I, sometimes it means action-with-effect agency. The substantive theory seems coherent; the problem is the first definition's wording is too narrow for the scope lattice now being asserted.

## Prompt pass

Predictions vs evidence: I predicted this would clarify agency as a causally contrastive subset. It did, and it confirmed F1 rather than dissolving it.

Cross-segment consistency: F1 remains live. `scope-agency.md:38-39` explicitly names passive and nominal agents as adaptive-only; `def-agent-environment.md:19-23` requires actions affecting `Omega` in the base agent definition. There is also a possible hidden dependency on Pearl machinery: `scope-agency.md:19` and `:24` use `do(a)` and refer to `def-pearl-causal-hierarchy`, which is downstream. The local prose may be sufficient, so I am only watching it.

Math verification: no calculation. The set definition is crisp. One subtlety: using `P(o | do(a))` rather than an outcome over `Omega` makes agency observation-relative, not world-effect-relative. That may be intentional ("make a difference to what it can observe"), but it excludes unobservable causal effects unless later causal-information-yield handles them.

Direction next: `post-composition-consistency` is next in the outline and was already flagged "possibly out of place." I expect it to assert scale invariance before composition machinery exists, which may be acceptable as a postulate but likely introduces downstream vocabulary early.

Errors to watch: downstream "agent" references need scope qualifiers. Also watch whether action effects are defined over observations, environment states, objectives, or some mix.

What I would change: introduce a neutral term like "adaptive system" or "agent-candidate" in `def-agent-environment`, reserve "agency" for this segment, and let "agent" be explicitly overloaded only if the text wants that.

Curiosity: whether thermostats belong in agency because two setpoint-driven actions produce different observations, even if they do not learn causal structure. The segment says yes for actions with causal effect; Part II learning-agent scope may later exclude precompiled controllers.

New knowledge enabled: the audit now has a clear scope gate for Section II/III claims: if a result relies on acting-with-effect, it should depend on `scope-agency`.

Audit process change: keep F1 as a candidate for final report unless a later segment or Phase-2 material shows it is already tracked/resolved.

Running outline change: strengthen F1 and add a Pearl-forward-reference watch.

Value feel: high. The segment itself is strong; it exposes the earlier terminology defect precisely because its own scope boundary is clear.

## Diagram thought

The best diagram is a two-axis classifier: adaptive uncertainty on one axis and causal action contrast on the other. Passive observers and nominal agents sit in adaptive-only; agency appears only where both uncertainty and contrast hold. This avoids the overloaded "agent" word entirely.
