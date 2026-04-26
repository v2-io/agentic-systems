# 01 — def-agent-environment

Dependencies: none.

## Reflection

First segment confirms the primitive boundary: environment $\Omega$, lossy observation, internal state, action channel.
The segment is intentionally definitional and its `status: axiomatic` is appropriate.

The first surprise is terminological.
The outline and README frame Section I as applying to "adaptive systems" including passive observers and systems that may not have meaningful action effects, while this first segment defines an **agent** as satisfying an action-channel condition: it "produces actions that affect $\Omega$".
That is compatible if Section I uses "agent" as one side of a general agent-environment decomposition and then separately broadens / narrows scope, but it creates a possible early ambiguity: are passive adaptive systems outside this primitive definition until later repaired, or are "actions" allowed to be null / ineffective at this stage?

This is not a finding yet.
I expect `def-action-transition`, `scope-adaptive-system`, and `scope-agency` to clarify whether Section I primitives intentionally start with action-capable systems and then distinguish effective agency later.
If `scope-adaptive-system` includes passive observers without revisiting this definition, this may become a scope-consistency issue.

The information-loss boundary is crisp: perfect access to $\Omega_t$ makes AAD vacuous.
This enables the rest of the theory by making model state, mismatch, and gain necessary rather than decorative.

Prediction for next segment: `def-observation-function` should formalize the lossy observation map $h$ and noise $\varepsilon_t$.
I will watch whether it permits action-dependent observations (active sensing) before action-transition has been introduced, and whether lossiness is probabilistic, many-to-one, noisy, or all of those.

Running report update: add a watch item for "adaptive-system breadth vs primitive agent action requirement."
