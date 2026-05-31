# 08 — post-causal-structure

Dependencies checked: `def-agent-environment` and `def-chronica` already read.

## Reflection

This segment cleanly grounds causal structure in temporal order.
The postulate itself is modest: possible influence requires temporal precedence.
`status: axiomatic` is appropriate.

It also gives the clearest prose repair so far for the adaptive-vs-agency hierarchy:
zero-coupling systems are outside agency but inside adaptive scope if they observe under residual uncertainty.
This confirms the framework's intent and makes the earlier primitive issue sharper rather than dissolved.
The theory intends passive estimators to be in Section I, but its first primitive segment and chronica definition are action-shaped.

Cross-segment consistency:
- Consistent with `scope-agency`'s interventional-contrast condition.
- In tension with `def-agent-environment`'s "produces actions that affect the environment" if that is read literally.
- In tension with `def-action-transition`'s phrasing "Actions affect the environment" for zero-coupling adaptive systems.

Dependency check:
The formal postulate is well-typed from declared dependencies.
Discussion references future segments (`def-pearl-causal-hierarchy`, `def-mismatch-signal`, `def-causal-information-yield`) but mostly as downstream consequences.
I would not call those missing dependencies for this segment's core claim.

Substantive watch item:
"The model should give more weight to observations that are causally downstream of the agent's actions" may overstate the relationship between interventional status and evidential reliability.
Action-contingent observations can be high-CIY, but they can also be noisy or biased.
This sentence probably becomes true only when weighted by CIY / uncertainty, not merely causal downstreamness.
I will check `def-causal-information-yield` and `emp-update-gain` before deciding whether this is just informal shorthand.

Prediction for next segment: `def-pearl-causal-hierarchy` should define Level 1/2/3 and `do`.
This will retroactively explain `scope-agency`, but the ordering issue remains because `scope-agency` already used the operator formally.

Running report update:
- Candidate primitive/scope issue now has direct supporting text from current src: passive estimators are explicitly in adaptive scope despite action-affecting primitives.
