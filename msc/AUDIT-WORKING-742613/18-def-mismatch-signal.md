# 18 — def-mismatch-signal

Dependencies checked: `form-agent-model` and `def-observation-function` already read.

## Reflection

This segment defines the core aporia signal:

$$\hat o_t=\mathbb E[o_t\mid M_{t-1},a_{t-1}],\qquad \delta_t=o_t-\hat o_t.$$

The primary vector-space definition is straightforward.
The zero-aporia ambiguity discussion is good and prevents "low mismatch = good model" overclaim.

Math/sign finding:
The score-function mismatch is defined as

$$\tilde\delta_t=-\nabla_M\log P(o_t\mid M_{t-1},a_{t-1}),$$

then described as pointing "in the direction the model should move to increase the likelihood" and as coinciding with $\delta_t$ up to scaling under Gaussian models.
For the standard Gaussian observation model $o\sim\mathcal N(M,\sigma^2)$:

$$\log P(o\mid M)=-\frac{(o-M)^2}{2\sigma^2}+c,$$

so

$$\nabla_M\log P(o\mid M)=\frac{o-M}{\sigma^2}=\frac{\delta}{\sigma^2}.$$

The direction that increases likelihood is $+\nabla_M\log P$, not $-\nabla_M\log P$.
The segment's definition gives $-\delta/\sigma^2$, the opposite direction.

Candidate finding H:
`def-mismatch-signal` has a sign error in the score-function mismatch definition or its interpretation.
Repair: either define $\tilde\delta_t=\nabla_M\log P(o_t\mid M_{t-1},a_{t-1})$ if it is meant to be an ascent/update direction, or keep $-\nabla\log P$ but call it the negative-log-likelihood gradient and ensure downstream update rules subtract it.

This is likely high-impact because `emp-update-gain`, gain-sector bridge, and gradient equivalence may rely on score direction.
I will track whether downstream segments use $\tilde\delta$ directly or only the vector $\delta$.

Dependency note:
The segment uses prior action $a_{t-1}$ but `def-observation-function` already introduced action-conditioned observations, so dependency is adequate.

Prediction for next segment:
`result-mismatch-decomposition` should decompose $\delta_t$ into model error plus observation noise.
I will check whether the sign convention propagates there.

Running report update:
- High-priority candidate finding: score mismatch sign is reversed under Gaussian model.
