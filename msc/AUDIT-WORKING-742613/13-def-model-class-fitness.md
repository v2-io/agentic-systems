# 13 — def-model-class-fitness

Dependencies checked: `def-model-sufficiency` already read.

## Reflection

This segment defines $\mathcal F(\mathcal M)=\sup_{M\in\mathcal M}S(M)$.
The definition is natural and the `status: axiomatic` label is appropriate, subject to the same well-definedness caveat from `def-model-sufficiency`.

The segment inherits the denominator-zero issue from $S(M)$.
If $S$ is undefined for no-predictive-information histories, then $\mathcal F$ is also undefined unless the scope excludes those cases or supplies a convention.

Substantive nuance:
`S(M_t)` was trajectory- and policy-relative.
This segment writes $\mathcal F(\mathcal M)$ without displaying that relativity.
That is probably acceptable as notation once established, but for clarity the segment could say "relative to the same chronica, horizon, and generating policy as $S$."
Otherwise, "best achievable within a model class" can be misread as an intrinsic property of the class independent of environment/task.

Potential overstatement:
"The gap ... cannot be closed by better parameter estimation, more data, or longer training within the current class" is true if $\mathcal F$ is defined against the true data-generating process / asymptotic information available to the class.
If $\mathcal F$ is computed relative to the current finite chronica, more data can change the relevant predictive-information landscape.
This is probably resolved downstream by `result-structural-adaptation-necessity`, but the definition itself would benefit from distinguishing current empirical estimate from asymptotic class ceiling.

What this enables:
The framework can separate parametric update failure from structural model-class failure.
This will be load-bearing for structural adaptation and possibly for logogenic memory/context limits.

Prediction for next segment:
`form-event-driven-dynamics` should shift from discrete $t$ to event timestamps $\tau$ and define event rate $\nu$.
I will watch whether event streams include passive-observation-only cases and whether event information uses $M_{\tau^-}$ consistently.

Running report update:
- Candidate E now propagates to model-class fitness.
- Add clarity recommendation: make $\mathcal F$'s trajectory/policy/horizon relativity explicit.
