# 09 — def-pearl-causal-hierarchy

Dependencies checked: `post-causal-structure` and `scope-agency` already read.

## Reflection

This segment defines Pearl Levels 1/2/3 and gives AAD's interpretation.
It retroactively supplies the `do(\cdot)` machinery that `scope-agency` already used, confirming candidate finding C as an ordering/dependency issue.

The definition is conceptually sound and the `status: axiomatic` / definitional framing is mostly appropriate.
The hierarchy is adopted prior art; AAD's contribution is mapping it onto the feedback loop.

Important nuance:
The segment distinguishes "availability vs exploitation", which is valuable.
It prevents the framework from saying every action-coupled agent actually reasons at Level 2/3.

Potential future risk:
Level 2 access is said to require that "the agent chose the action (it was not determined by the same causes that determine the observation)."
In real adaptive agents, actions are chosen from $M_t$, and $M_t$ is shaped by the same history/environment that shapes observations.
Structural action-taking is not automatically randomized intervention or identifiable causal data.
I expect `der-loop-interventional-access` and `scope-ciy-observational-proxy` to carry this distinction.
If they do not, the loop-to-Level-2 bridge may overclaim.

Cross-segment consistency:
- Strengthens `scope-agency`'s causal contrast.
- Clarifies that Level 1 remains available to passive observers.
- Still relies on a general "agent" vocabulary that is broader in practice than the first primitive definition.

External verification:
The Bareinboim et al. strict hierarchy claim is a candidate for sample citation verification later.
I will not web/ref-check it before finishing the current segment pass, per source-ordering discipline.

TST watch item:
"`git checkout` provides Level 3 access with ground-truth verification" is plausible for code behavior under tests, but not necessarily for product/user outcome counterfactuals.
If this appears as a canonical TST claim, it may need scope narrowing.

Prediction for next segment: `form-agent-model` should define $M_t=\phi(\mathcal C_t)$ and may reveal whether initial priors/model class are included.
I will watch the "everything known comes from chronica" issue.

Running report update:
- Candidate C confirmed: `do(\cdot)` is defined here after it is used formally in `scope-agency`.
