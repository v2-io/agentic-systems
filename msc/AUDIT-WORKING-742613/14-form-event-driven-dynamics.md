# 14 — form-event-driven-dynamics

Dependencies checked: `post-causal-structure`, `def-observation-function`, and `def-action-transition` already read.

## Reflection

This segment introduces asynchronous event streams, channel rates, event information, and channel-specific observation uncertainty.
The formulation is useful and fits the framework's event-driven ambitions.

Dependency issue:
The event-information definition uses $M_{\tau^-}$ but the segment does not depend on `form-agent-model`.
Because $M_t$ has already been introduced immediately upstream, this is an easy missing-dependency fix.
It is less severe than `scope-adaptive-system` using chronica before it exists, but still a Gate 1 dependency miss.

Candidate finding F:
`form-event-driven-dynamics` should declare `form-agent-model` because its formal expression conditions event information on $M_{\tau^-}` and discusses model prediction.

Potential semantic issue:
The segment equates event information content with mutual information $I(e_\tau;\Omega_\tau\mid M_{\tau^-})`, then says surprising events carry much information.
Mutual information is an expected reduction in uncertainty, not the realized surprise of a particular event.
The intuition is close, but if the framework later treats $\mathcal I(e_\tau)$ as realized information content, it may need pointwise information / surprisal rather than MI.
Watch `def-adaptive-tempo`.

Stale integration note:
The software discussion says the three-part tempo decomposition is "a Section IV gap" and refers to `AAD-FULL.md`.
The current repo has TST as `02-tst-core`, not AAD Section IV, and I have not seen `AAD-FULL.md` in root orientation.
This looks like stale migration language.
It may not be final-report-worthy unless TST integration issues accumulate.

Status: `robust-qualitative` is honest for an event-driven formulation.

What this enables:
Adaptive tempo can be stated as a sum over channel rates weighted by update quality.
It also gives logogenic/software agents a natural multi-channel representation.

Prediction for next segment:
`der-recursive-update` should derive $M_{\tau^+}=f(M_{\tau^-},e_\tau)$ or discrete $M_t=f(M_{t-1},o_t,a_{t-1})$ from compression constraints.
I will watch whether it depends on this event-driven formulation or remains discrete.

Running report update:
- Candidate missing dependency: `form-agent-model` for event information.
- Stale "Section IV / AAD-FULL.md" language noted.
