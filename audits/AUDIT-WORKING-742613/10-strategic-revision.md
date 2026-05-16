# Strategic Revision After 10 Segments

The initial prediction that Section I would be cleanest was too optimistic at the dependency-cadence level.
The conceptual hierarchy is clear, but the first ten segments show several early-order issues:

- `scope-adaptive-system` uses $\mathcal C_t$ before `def-chronica`.
- `scope-agency` uses `do(\cdot)` before `def-pearl-causal-hierarchy`.
- `post-composition-consistency` imports a large amount of downstream Section III machinery before its terms are available.

This does not mean the theory is mathematically wrong.
It means the current OUTLINE row order is not a clean topological linearization of the formal objects used in segment bodies.

The second pattern is scope-primitive drift:

- `def-agent-environment`, `def-action-transition`, and `def-chronica` are action-coupled.
- `scope-adaptive-system` and `post-causal-structure` explicitly include passive observers and zero-coupling adaptive systems.

The intended theory almost certainly wants an outer "adaptive system" primitive and a narrower "agent/agency" primitive.
The current naming makes the hierarchy harder to read and creates formal awkwardness.

Audit strategy change:
I will keep logging dependency/order issues, but I should avoid over-reporting every downstream reference as a finding.
The report-worthy cases are where a formal expression or asserted structural consequence requires a not-yet-defined object, not where Discussion merely forecasts later results.

Current high-priority candidate findings:

1. `scope-adaptive-system` is not well-typed in canonical order because it uses $\mathcal C_t$ before `def-chronica` and does not declare the dependency.
2. `scope-agency` is not well-typed in canonical order because it uses `do(\cdot)` before `def-pearl-causal-hierarchy`.
3. Early adaptive-scope primitives are action-coupled while the adaptive scope explicitly includes passive observers / zero-coupling systems.
4. `post-composition-consistency` is doing too much too early; it likely should be split into a lean postulate plus downstream Section III elaboration.

Open watch items:

- Whether known-$h$ / known-$T$ examples conflict with strong epistemic-opacity wording.
- Whether $M_t=\phi(\mathcal C_t)$ needs explicit $M_0$ / prior / pretrained structure.
- Whether PID / thermostat examples are consistently inside adaptive scope or treated as degenerate outside the main machinery.
- Whether composite scope has three routes here but four routes later.
