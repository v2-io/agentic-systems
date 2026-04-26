# 07 — def-chronica

Dependencies checked: `def-agent-environment`, `def-observation-function`, and `def-action-transition` already read.

## Reflection

This segment defines $\mathcal C_t$ after it was already used in `scope-adaptive-system`.
That confirms candidate finding A as a real ordering/missing-dependency issue in current src/OUTLINE, not just my missing context.

The definition itself is straightforward for action-coupled agents:

$$\mathcal C_t=(o_1,a_1,o_2,a_2,\ldots,a_{t-1},o_t).$$

But because it depends on `def-action-transition` and includes actions by construction, it also reinforces the adaptive-scope tension.
Passive Bayesian learners would need a chronica with absent/null actions or an observation-only history.
The segment does not name that degenerate case.

Possible repair for the early scope issue:
- Define chronica before `scope-adaptive-system`, with optional/null action events permitted.
- Or split "chronica" into general event history for adaptive systems and action-observation chronica for agency.
- Or define $\mathcal C_t$ locally in `scope-adaptive-system` as observation history when action is absent.

New conceptual watch item:
"Everything the agent can ever know must be constructed from this sequence" may be too strong unless initial priors / innate structure / pretrained parameters are included in the agent's initial state or in $\mathcal C_0$.
This will matter for logogenic agents and for any model class whose structure is not learned from the current interaction history.
I expect `form-agent-model` to clarify whether $M_t=\phi(\mathcal C_t)$ includes an initial model / prior.

Status: definitional/axiomatic is appropriate.

What this enables: non-forkable causal trajectory and continuity persistence.
That is potentially a major bridge to logozoetic concerns, but currently appears in Discussion rather than formal expression.

Prediction for next segment: `post-causal-structure` should introduce irreducible causal structure.
I will watch whether it depends on `def-chronica` and whether it requires Pearl hierarchy before `def-pearl-causal-hierarchy` appears.

Running report update:
- Candidate finding A strengthened: `scope-adaptive-system` used $\mathcal C_t$ before this segment and did not declare dependency.
- Adaptive-scope/passive-observer issue now includes chronica shape, not just agent terminology.
