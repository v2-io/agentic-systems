# 06 - scope-agency

Segment: `01-aat-core/src/scope-agency.md` (`#scope-agency`)

Dependencies: `scope-adaptive-system`, `def-action-transition`, both read. Dependency-order check passes.

## Segment Read

This segment narrows adaptive systems to agency by adding choice and causal effect. The formal condition is: at least two actions and at least one pair of distinct actions with different interventional outcome distributions. In plain terms, the agent must be able to do something that makes a difference.

The key move is that agency is not purpose yet. It is interventional capacity: the loop can generate Pearl-Level-2 data. Purposeful-agent machinery comes later and depends on this scope, but the agency boundary itself is causal contrast.

## Predictions Vs Evidence

I predicted this segment would separate adaptive from agentic by adding Pearl-Level-2 action. That is exactly what it does. The name "agency" is therefore narrower than ordinary language in one dimension and broader in another: a thermostat with causally efficacious actions qualifies; a rich passive observer does not.

The segment also confirms that `passive observers` and `nominal agents` are meaningful exclusion names, but they remain local taxonomy unless later segments reuse them.

## Cross-Segment Consistency

This is a clean restriction of `#scope-adaptive-system`: keep observations and residual uncertainty, then add binary choice and interventional contrast. It also uses `#def-action-transition` correctly: actions are only agency-relevant if the transition implications differ in observable outcome distribution.

No contradiction. The reference to `#def-pearl-causal-hierarchy` is a forward dependency in prose but not in `depends:`. Because `do(\cdot)` appears in the formal expression and `def-pearl-causal-hierarchy` is later in the OUTLINE, this is worth noting. The segment is currently `claims-verified`, but by the audit dependency rule, a formal expression using Pearl's `do` operator may need the Pearl hierarchy definition upstream or in `depends:`. It may be treated as standard notation from outside AAD, but the segment itself says "see #def-pearl-causal-hierarchy." For naming work I will not route an audit finding, but this is a real ordering/dependency smell to remember.

## Naming Notes

`agency` is the right scope noun if the project consistently teaches its technical meaning: causal action with interventional contrast, not consciousness or goal autonomy. It is a high-baggage word, but the baggage is unavoidable and the segment's formal condition disciplines it.

`interventional contrast` feels like an important prose handle. It may be a better gloss than "causal effect" in contexts where the point is learnability from distinct actions. I should wait for the causal-information-yield segment before voting strongly on CIY aliases, but this segment already makes `interventional contrast` attractive.

`nominal agents` is a good exclusion name: systems that appear to choose but whose choices have no causal contrast. It is useful, though I need to see whether it recurs before voting.

## What This Enables

This segment enables the loop-as-intervention story, causal information yield, the causal hierarchy requirement, purposeful-agent state, orient cascade, and composition. It is the first point where the adaptive loop becomes epistemically active rather than merely receptive.

For naming, it makes "agentic" dangerous if used casually. In this framework, agency has a formal minimum; later classes add objective, strategy, self-actuation, language, or moral continuity.

## Watchlist

- Downstream use of "agent" or "agency" when only adaptive scope is available.
- Whether `do(\cdot)` dependency is considered standard imported notation or should have been declared through `#def-pearl-causal-hierarchy`.
- Whether `interventional contrast` becomes the natural alias for causal information yield.

## Wandering Thoughts

The distinction between choice and causal effect is a useful cleanup of ordinary agency language. A menu with two buttons is not agency if both buttons do the same thing. That simple condition prevents a lot of anthropomorphic drift.

The segment also shows why Pearl vocabulary is not ornamental in AAD. It is doing boundary work. The agent's action must be a `do`, not just an observation of itself choosing. That will matter later when the framework tries to get from feedback loops to Level 2 data.

For naming, this segment is one of the places where common words are unavoidable but must be domesticated by formal conditions. `Agency` is too central to replace with an invented term, but it should usually be introduced as "agency scope" or "causal-action agency" in explanatory contexts.

I am also noticing that "nominal agent" has good rhetorical force: it names the false friend. It may help readers understand why AAD's agency is not just "a system with possible outputs." If the term appears as a target, I will likely keep it once I see enough recurrence.
