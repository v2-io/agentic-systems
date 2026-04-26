# 20 — emp-update-gain

Dependencies checked: `def-mismatch-signal` and `def-observation-function` already read.

## Reflection

The gain principle appears as predicted:

$$\eta^\ast=\frac{U_M}{U_M+U_o}.$$

The segment is honest at the frontmatter level: `type: empirical`, `status: robust-qualitative`.
The Epistemic Status further distinguishes exact linear-Gaussian / conjugate Bayesian cases from broader robust-qualitative analogy.

Math/status:
The scalar limiting behavior is correct.
The Kalman scalar mapping is exact.
I am less certain about the blanket "conjugate Bayesian systems" exactness because incremental update weights vary by family and parameterization, but the qualitative count/prior-strength ratio is standard.
Not a finding.

Overclaim watch:
"Any optimal adaptation process must approximate this functional dependence" is strong.
It is plausible in spirit but would need a definition of optimality and uncertainty in non-Bayesian, non-quadratic systems.
The segment's robust-qualitative status and open questions soften this enough for now.

Dependency:
The discussion relies on `result-mismatch-decomposition` for overfitting/gain calibration but does not declare it.
Because that is discussion support rather than the gain formula's definition, I would not elevate it to a finding.
If the overfitting paragraph becomes formal, add the dependency.

Score-sign issue:
This segment uses $g(\delta_t)$ rather than $\tilde\delta_t$, so the `def-mismatch-signal` score sign error does not directly propagate here.
But downstream gradient-equivalence segments likely will.

Open questions in a `claims-verified` segment:
The `Open questions` section is not under `Working Notes`, so this may be intended as reader-facing scope honesty.
It is not a candidate issue unless project convention requires open development questions to live in Working Notes.

What this enables:
Adaptive tempo as rate times correction quality.
Gain collapse also gives a useful mechanistic account of confirmation bias / reality decoupling.

Prediction for next segment:
`def-causal-information-yield` should define information from action interventions.
I will watch whether it depends on Pearl hierarchy and whether it overstates intervention identifiability from action-conditioned observations.

Running report update:
- No new finding, but keep overclaim watch on universal optimality of the uncertainty-ratio principle.
