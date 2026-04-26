# 23 — hyp-mismatch-dynamics

Dependencies checked: `def-adaptive-tempo` and `def-mismatch-signal` already read.
Declared dependency `deriv-sector-condition` is an Appendix derivation not yet read; applying the appendix-back-pointer exception and reading it next.

## Reflection

The linear mismatch ODE is clearly labeled heuristic:

$$\frac{d\lVert\delta\rVert}{dt}=-\mathcal T\lVert\delta\rVert+\rho(t).$$

This is the right status posture.
The segment distinguishes deterministic bounded disturbance (steady ratio $\rho/\mathcal T$) from stochastic OU disturbance (RMS $\sigma_w/\sqrt{2\mathcal T}$), which prevents a common overgeneralization.

Math spot-check:
For scalar OU $d\delta=-\mathcal T\delta\,dt+\sigma_w\,dW_t$, stationary variance is $\sigma_w^2/(2\mathcal T)$, so RMS is $\sigma_w/\sqrt{2\mathcal T}$.
That checks out.
The deterministic transient solution for constant $\rho$ also checks out for the scalar norm ODE.

Dependency issue:
The Epistemic Status says the fluid limit is formally justified by `#deriv-discrete-sector-condition`, including deterministic zero gap and stochastic variance gap.
That segment is not declared in `depends:`.
Because the fluid-limit justification is part of the Epistemic Status, this is more than a casual forward reference.
Potential repair: add `deriv-discrete-sector-condition` as an appendix dependency, or move the detailed fluid-limit claim to a downstream note.

Broken-link / slug issue:
The markdown link is `[#deriv-discrete-sector-condition](discrete-sector-condition.md)`, but the outline filename is `deriv-discrete-sector-condition.md`.
This appears mechanically wrong.

Status:
`type: hypothesis`, `status: heuristic` is appropriate.
The segment is a good example of honest approximation if the dependency/link issue is fixed.

Interaction with adaptive-tempo issue:
The ODE inherits the scalar/additive tempo caveats from `def-adaptive-tempo`.
The segment does not repeat independence/isotropy assumptions in the Formal Expression, but its heuristic status reduces the severity.
Downstream exact persistence results need to carry the sector/per-dimension conditions.

Prediction for appendix:
`deriv-sector-condition` should prove boundedness under sector-bounded correction and probably support `result-sector-condition-stability`.
I will check whether it depends on the score-gradient sign convention or only on abstract inward-pointing correction.

Running report update:
- Candidate missing dependency / broken link: `deriv-discrete-sector-condition` in fluid-limit claim.
