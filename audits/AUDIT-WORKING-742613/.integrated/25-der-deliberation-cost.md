# 25 — der-deliberation-cost

Dependencies checked: `der-action-selection`, `emp-update-gain`, `def-adaptive-tempo`, and `form-event-driven-dynamics` already read.

## Reflection

This segment derives a local threshold:

$$\Delta\eta^\ast(\Delta\tau)\lVert\delta_{\text{post}}\rVert>\rho_{\text{delib}}\Delta\tau.$$

Dimensionally, the expression is coherent: gain improvement is dimensionless, mismatch magnitude has mismatch units, and $\rho_{\text{delib}}\Delta\tau$ has mismatch units.
The optional first-order correction when $\lVert\delta_{\text{post}}\rVert=\lVert\delta_0\rVert+\rho_{\text{delib}}\Delta\tau$ checks out:
the FOC becomes $\Delta\eta' \lVert\delta_{\text{post}}\rVert=(1-\Delta\eta)\rho_{\text{delib}}$.

Status:
`conditional` is appropriate.
The segment is clear that the derivation captures only the epistemic/gain benefit of deliberation and not direct action-value benefit.

Substantive concern, mostly scoped:
The prose starts by saying deliberation improves action quality through internal simulation, but the formal benefit term is improvement in update gain $\eta^\ast$.
Those are not the same object.
The Epistemic Status names this limitation, so I do not count it as a finding.
Still, this segment should be cited carefully: it is a threshold for deliberation-as-epistemic-gain improvement, not for all planning.

Dependency propagation:
The segment inherits the `der-action-selection` $M$-only policy issue in its implicit-action framing.
For Section II agents, the three-way exploit/explore/deliberate extension is the more appropriate home.

Open questions:
Again, a `claims-verified` segment contains reader-facing "Open questions."
This may be intentional scope honesty rather than Working Notes, but repeated open-question sections in verified segments blur the project convention slightly.

What this enables:
A tempo-aware reason why high-volatility environments favor fluency / implicit action and why deliberation is best in stable or high-mismatch scenarios.

Prediction for next segment:
`der-gain-sector-bridge` should connect the gain update rule to A2' directional fidelity.
Because of the score-sign issue and sector-condition dependence, this is a high-priority check.

Running report update:
- No new finding; segment is conditional and mostly honest.
