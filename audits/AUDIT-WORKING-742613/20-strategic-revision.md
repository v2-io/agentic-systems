# Strategic Revision After 20 Reflection Files

The second ten segments shifted the audit from mostly dependency/order concerns to one real math issue and one scope/status issue.

Highest-confidence issue now:

- `def-mismatch-signal` has a sign error in the score-function mismatch definition or interpretation.
Under Gaussian prediction, $\nabla_M\log P(o\mid M)=\delta/\sigma^2$; the segment defines $-\nabla_M\log P$ but says it points in the update/increased-likelihood direction and coincides with $\delta$.

Scope/status issue strengthened:

- `der-action-selection` exact $a_t=\pi(M_t)$ conflicts with Section II's own statement that actuated agents require $\pi(M_t,G_t)$.
The likely repair is to state action selection over complete state $X_t$ and recover $\pi(M_t)$ as the Section I / fixed-goal special case.

The recursive-update proof checked out under its own constraints.
It is not a math finding, but status language should harmonize "exact", "conditional", and the continuous-coupling caveat.

Model sufficiency has a small but real mathematical edge-case:

- $S(M_t)$ requires denominator $I(\mathcal C_t;o_{t+1:\infty}\mid a_{t:\infty})>0$.
Without it, boundary claims are undefined in no-predictive-information regimes.

Audit strategy:

- Continue canonical order through at least Section I, because the sign error may propagate into gain-sector / gradient bridge.
- Keep separating high-value findings from editorial drift.
- For final report, group the early dependency/order problems as one "canonicalization integrity" finding rather than many small findings, unless individual cases demand separate repairs.
