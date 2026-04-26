# 10 — form-agent-model

Dependencies checked: `def-agent-environment`, `def-observation-function`, and `def-chronica` already read.

## Reflection

This segment defines $M_t=\phi(\mathcal C_t)$ as a modeling choice.
The status (`robust-qualitative`) and type (`formulation`) are honest: it explicitly says history-based alternatives exist.

The segment partially addresses the "everything known comes from chronica" concern by making $M_t$ the complete retained state from interaction history.
But it does not explicitly place initial priors, pretrained weights, innate model class structure, or inherited architecture.
Those can be hidden in $\phi$ and $\mathcal M$, but readers may need that said.
Otherwise, logogenic and biological cases look under-described: a current LLM's model quality is mostly in pretrained parameters, not only "context window contents plus retrieved memory."

Possible clarification, not a finding yet:
Define $M_t=\phi(M_0,\mathcal C_t)$ or state that $M_0$ / model class is absorbed into $\phi$ and $\mathcal M$.
This would make "complete epistemic substate" compatible with pretrained or innate structure.

Cross-segment consistency issue to watch:
The Discussion says a PID controller's $M_t$ is too impoverished "to support the adaptive dynamics of Section I."
But orientation material and earlier scope discussions include PID controllers / thermostats as adaptive examples.
Maybe "too impoverished" means it occupies a degenerate edge but still fits the machinery; the sentence reads stronger.
I will watch `def-agent-spectrum` and persistence segments.

Dependency note:
The segment references downstream `form-information-bottleneck`, `def-mismatch-signal`, `emp-update-gain`, and `def-agent-spectrum`, but the formal formulation itself is well-typed without them.
No dependency finding here.

What this enables:
Once $M_t$ exists as compressed history, recursive update, mismatch, sufficiency, and tempo can be stated.

Prediction for next segment:
`form-information-bottleneck` should formalize useful compression of $\mathcal C_t$ into $M_t$.
I expect it to be a formulation / objective, not exact claim about actual agents.

Running report update:
- Add possible clarification: include initial priors / pretrained structure in model formulation.
- Watch PID/adaptive-scope language.
