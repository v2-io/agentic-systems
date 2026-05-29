# 22 — def-adaptive-tempo

*Type: definition. Status: exact. Stage: claims-verified. Depends: [emp-update-gain, form-event-driven-dynamics].*

## Predictions vs evidence
Predicted: $\mathcal{T} = \sum_k \nu^{(k)} \eta^{(k)*}$ as central capacity. Found: scalar form + tensor extension under Fisher-local invariance + per-dimension promotion to matrix-Loewner. Strong segment with explicit scope-vs-tensor caveats.

## Math verification
- Scalar tempo $\mathcal{T} = \sum_k \nu^{(k)} \eta^{(k)*}$. ✓
- Tensor form $\mathcal{T} = \sum_k \nu^{(k)} K^{(k)}$ with $K^{(k)} = (H_M + H_L^{(k)})^{-1} H_L^{(k)}$. Standard natural-gradient form. ✓
- Channel-independence inequality: $\mathcal{T} \leq \sum_k \nu^{(k)} \eta^{(k)*}$ with equality iff channels are informationally independent. **Correct** — additive measure on dependent variables overcounts. The redundancy penalty involves $I(e^{(1)}; e^{(2)} \mid M_{\tau^-})$.
- Matrix-Loewner per-dimension: $\Sigma_\infty \prec D_\delta = \text{diag}(\delta_{\text{critical},k}^2)$ with Lyapunov equation. Standard control-theoretic form.

## Anisotropic simulation claim (spot-check candidate)
Line 65: *[Empirical Claim]* "in an anisotropic 3D system (gain varying 5:1), scalar $\rho/\mathcal{T}$ overestimated by 72%, with the weak dimension accounting for 84% of total mismatch ( #obs-section-i-validation-simulations)." Specific empirical claim. Will spot-check when I reach the validation simulations appendix.

## Prose-coherence
- The "speed × quality" framing (line 50) and "observation noise gating" (line 52) are good pedagogical anchors.
- Channel-independence assumption flagged (line 60-64) — strong methodological care. The framework explicitly says the additive formula overcounts in correlated-channel cases. Honest.
- Scalar vs tensor scope explicitly delimited (line 46) — downstream results invoking scalar $\mathcal{T}$ implicitly assume scalar/isotropic/nonredundant; promotion to tensor form flagged as TODO.

## Cross-segment consistency
Dense forward-refs (12+ segments). Cross-component reference to `#der-code-quality-as-observation-infrastructure` in `02-tst-core/`. Coherent.

## Watch list
- Tensor extension and matrix-Loewner promotion are spot-check candidates from my predictions file. Both anchored here; will verify when I reach the deriv segments.

## Next-segment predictions
`#hyp-mismatch-dynamics`. Linear ODE preview: $d\|\delta\|/dt = -\mathcal{T}\|\delta\| + \rho$. Hypothesis tier (per OUTLINE). Will set up the persistence condition's heuristic form.

## Brief wandering
This is the segment where tempo becomes load-bearing. Everything downstream relies on $\mathcal{T}$ being well-defined under the appropriate scope. The framework's careful flagging of *scalar / isotropic / nonredundant-channel* assumptions and the explicit tensor extension is the right discipline — it tells readers exactly when the scalar form is exact and when they need the matrix form. Strong.
