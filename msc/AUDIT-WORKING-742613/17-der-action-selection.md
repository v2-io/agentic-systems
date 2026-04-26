# 17 — der-action-selection

Dependencies checked: `form-agent-model` and `der-recursive-update` already read.

## Reflection

This segment derives action selection as $a_t=\pi(M_t)$ or $a_t\sim\pi(\cdot\mid M_t)$.
It is plausible for systems where $M_t$ is the complete action-relevant internal state.

But the segment's own Discussion says that for actuated agents, action selection involves $G_t=(O_t,\Sigma_t)$ and the policy becomes $\pi(M_t,G_t)$.
That creates a scope/status issue:
`form-agent-model` defined $M_t$ as epistemic substate, not complete agent state once goals and strategy exist.
So $a_t=\pi(M_t)$ is not exact for the broader AAD theory; it is exact only for agents whose non-epistemic purposeful state is absent, fixed, or folded into $M_t$.

Candidate finding G:
`der-action-selection` has `status: exact` and presents praxis as a function of $M_t$, but Section II's own planned state decomposition requires $\pi(M_t,G_t)$.
Repair options:
- Scope this segment explicitly to Section I / non-actuated adaptive-agent analysis.
- Write the exact statement as $a_t=\pi(X_t)$ for complete internal state, with $X_t=M_t$ in Section I and $X_t=(M_t,G_t)$ in Section II.
- Downgrade or mark the $a_t=\pi(M_t)$ form as conditional on fixed/absorbed goals.

This also interacts with earlier "agent" terminology:
Passive adaptive systems have no meaningful action, while actuated agents have action but not from $M$ alone.
The simple Section I policy form sits between those cases and needs its scope named.

Action fluency:
The qualitative implicit/explicit distinction is useful.
The proposed formal marker $\Delta\eta^\ast(\Delta\tau)\approx0$ may conflate update-gain improvement with action-quality improvement unless `der-deliberation-cost` defines deliberation as improving update gain / model quality rather than decision quality.
Watch item, not finding yet.

Dependency note:
If this segment is meant to apply only to agency, it should probably depend on `scope-agency`.
If it is meant to apply to any action-capable primitive agent, current dependencies are enough but the adaptive-scope passive cases remain outside the statement.

What this enables:
Defines policy and praxis, needed for causal information yield and Section II.
But I now expect Section II to need a repair route from $\pi(M)$ to $\pi(M,G)$.

Prediction for next segment:
`def-mismatch-signal` should define $\delta_t=o_t-\hat o_t$ with prediction from $M_{t-1}$ and prior action.
I will watch whether predictions require policy/action selection or only observation model.

Running report update:
- Serious candidate finding: `der-action-selection` exact $M$-only policy conflicts with later complete-agent state.
