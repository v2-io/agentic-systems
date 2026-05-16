# 05 — scope-agency

Dependencies checked: `scope-adaptive-system` and `def-action-transition` already read.

## Reflection

This segment does what predicted: agency is adaptive scope plus at least binary action choice and at least one Pearl-level-2 interventional contrast.
Conceptually this is a clean narrowing and it clarifies passive observers vs nominal agents.

It partially resolves the previous passive-system tension at the prose level: adaptive scope includes passive observers; agency excludes them.
But the formal object still uses `(Agent, Ω)`, inheriting the possible mismatch from `def-agent-environment`.
If `Agent` already means action-affecting entity, then `scope-adaptive-system` and this segment's "passive observers" branch are semantically awkward.
The framework's intended hierarchy is clear; the primitive name/definition is what is misaligned.

Second dependency/order issue: the formal expression uses Pearl's `do(a)` operator and explicitly says "see #def-pearl-causal-hierarchy", but `def-pearl-causal-hierarchy` has not been read yet and is not in `depends:`.
This is not merely a downstream explanatory reference; `P(o\mid do(a))` is in the scope condition itself.
`do(\cdot)` could be treated as standard notation, but FORMAT says dependencies should include prior objects that make the claim well-typed.
Given the project has its own `def-pearl-causal-hierarchy` segment, this looks like another missing upstream dependency / ordering issue.

Candidate finding C:
`scope-agency` uses Pearl intervention notation before the corpus defines Pearl levels and without declaring `def-pearl-causal-hierarchy`.
Repair options: move `def-pearl-causal-hierarchy` earlier, add it as a dependency and reorder, or define `do(\cdot)` locally with the later segment as elaboration.

Status: `axiomatic` is appropriate for a scope boundary.

Math verification: none beyond checking the set expression.
The condition uses observation distributions $P(o\mid do(a))$ rather than state transitions $P(\Omega_{t+1}\mid do(a))$.
That choice is defensible because AAD is observation-mediated, but it means actions that affect hidden state without any observation contrast are outside agency for AAD's purposes.
That may be intended; if not, downstream causal machinery should clarify "observable causal effect" vs "environmental causal effect."

Prediction for next segment: `post-composition-consistency` likely depends on adaptive scope and maybe agency.
I will watch whether it inherits "Agent" terminology problems and whether it requires a projection/abstraction map not yet defined.

Running report update:
- Candidate hidden dependency on `def-pearl-causal-hierarchy`.
- Add nuance: agency is defined by observable interventional contrast, not necessarily all environmental causal effect.
