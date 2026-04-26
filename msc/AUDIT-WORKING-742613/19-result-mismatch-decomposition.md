# 19 — result-mismatch-decomposition

Dependencies checked: `def-mismatch-signal`, `def-observation-function`, `form-agent-model`, and `scope-adaptive-system` already read.

## Reflection

This segment gives a standard bias/noise decomposition:

$$\mathbb E\lVert\delta_t\rVert^2=\mathbb E\lVert\hat o_t-\bar o_t\rVert^2+\mathbb E[\operatorname{Var}(o_t\mid\Omega_t,a_{t-1})].$$

The derivation is sound under the stated fresh-noise / orthogonality condition.
No math error found in the decomposition.

The sign error from `def-mismatch-signal` does not propagate here because this segment uses the vector prediction error $\delta_t=o_t-\hat o_t$, not the score-function mismatch.

Status:
`exact` is appropriate conditional on GA-1 / fresh noise.
The Epistemic Status names the condition, so I do not see a label problem.

Minor issue:
Step 1 invokes `scope-adaptive-system`'s residual uncertainty, but the decomposition itself does not require $H(\Omega_t\mid\mathcal C_t)>0`.
It requires only the prediction setup and noise orthogonality.
This is harmless, but the derivation could be cleaner by separating "within AAD scope" from the algebraic identity.

Substantive nuance:
The segment correctly avoids saying $S(M_t)<1$ always implies one-step mean error; it names the needed alignment assumption.
That is exactly the kind of scope honesty the framework is trying to practice.

Prediction for next segment:
`emp-update-gain` should use model uncertainty and observation uncertainty to derive / motivate $\eta^\ast=U_M/(U_M+U_o)$.
I will check whether it treats Kalman gain as exact only in Gaussian/linear scalar cases and whether the score-sign issue appears.

Running report update:
- Mismatch decomposition currently looks sound; no finding.
