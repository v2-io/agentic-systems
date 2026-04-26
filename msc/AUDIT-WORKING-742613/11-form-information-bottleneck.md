# 11 — form-information-bottleneck

Dependencies checked: declared dependency `form-agent-model` already read.

## Reflection

This segment is careful in prose: IB-as-applied-theorem is exact, while volatility / policy dependence of $\beta$ is robust-qualitative.
That mixed-status explanation is good.

However, the frontmatter says `status: exact` for the entire segment.
Because the Formal Expression includes a "Dependence on volatility" subsection and the Discussion makes broader compression-operation claims, a reader scanning frontmatter may overread the whole segment as exact.
This is not necessarily a finding because the Epistemic Status paragraph explicitly disambiguates, but it is a status-label pressure point.
Possible repair: use `status: conditional` or `robust-qualitative`, or split the exact IB theorem binding from the qualitative $\beta(\rho,\pi)$ claims.

Dependency/order:
The formal IB objective is well-typed from `form-agent-model` plus standard information theory.
The volatility dependence uses $\rho$ before the environment-change-rate object has been introduced in the OUTLINE.
Because that claim is qualitative and not central to the IB theorem binding, I would not classify it as the same severity as $\mathcal C_t$ before `def-chronica`.
Still, if the volatility section remains in Formal Expression, adding a dependency on the segment defining $\rho$ or moving this discussion later would be cleaner.

Substantive check:
The Markov chain $Y-X-T$ with $X=\mathcal C_t$, $T=M_t$, $Y=o_{t+1:\infty}\mid a_{t:\infty}$ seems right if $M_t=\phi(\mathcal C_t)$ and future actions are treated as conditioned/exogenous.
The segment notices policy-relativity, which prevents a common overclaim.

Open concern:
If actions are generated from $M_t$, conditioning on an entire future action sequence is analytically convenient but not the same as the agent's endogenous future policy.
The segment handles this by saying the objective is defined relative to a generating policy.
This should connect later to `def-value-object`; not a defect yet.

External verification candidate:
Tishby et al. 1999 / rate-distortion link is a possible sample citation to verify in Phase 3.

What this enables:
Model sufficiency can now be defined as retained predictive information relative to the full chronica.
It also gives a unifying compression vocabulary that later segments may reuse for strategy and shared intent.

Prediction for next segment:
`def-model-sufficiency` should define a ratio comparing predictive power of $M_t$ to predictive power of $\mathcal C_t$.
I will watch denominator edge cases and policy/horizon conditioning.

Running report update:
- Add status-label watch: exact frontmatter on mixed exact/robust-qualitative IB segment.
