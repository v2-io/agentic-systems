# 20 — emp-update-gain

*Type: empirical. Status: robust-qualitative (frontmatter); body says "*Derived* under Fisher-local invariance regime." Depends: [def-mismatch-signal, def-observation-function].*

## Predictions vs evidence
Predicted: $\eta^* = U_M/(U_M+U_o)$, canonical Bayesian/Kalman form. Found: that, plus careful epistemic-tiering (Fisher-local exact / general robust-qualitative) and the epistemic-opacity-resolution argument.

## Math verification
- $\eta^* = U_M / (U_M + U_o)$. Derives directly from Bayesian posterior-mean update with Gaussian uncertainties: $\Delta\theta = (H_M + H_L)^{-1} H_L \delta$ with $H_M = U_M^{-1}, H_L = U_o^{-1}$. Scalar collapse: $(U_M^{-1} + U_o^{-1})^{-1} U_o^{-1} = U_M / (U_M + U_o)$. ✓
- Update rule $M_t = M_{t-1} + \eta^* g(\delta_t)$ — additive-with-gain form. Standard.
- Domain table cross-validates (Kalman scalar exact; conjugate Bayesian incremental $1/(n+\kappa)$ also standard).

## Status-tagging observation
Frontmatter `empirical/robust-qualitative` vs body `Derived under Fisher-local regime`. Less of a drift than der-recursive-update — here the segment has *multi-tier content* (Fisher-local exact + general robust-qualitative), and the frontmatter picks the broader claim. Defensible choice. Watch list note, not finding.

## Cross-segment consistency
Forward-refs `#deriv-fisher-local-update-gain` (appendix), `#deriv-adaptive-gain-dynamics` (appendix), `#def-adaptive-tempo`, `#result-mismatch-decomposition`, `#result-structural-adaptation-necessity`. Coherent.

## Prose-coherence
- The epistemic-opacity-resolution (line 50) is a clean tension-handling: agent needs to know $U_o$ but $\varepsilon_t$ distribution is opaque; resolution is dynamic self-estimation from observable innovations, with `#deriv-adaptive-gain-dynamics` providing the formal proof of Lyapunov-stable meta-adaptation.
- Gain collapse / Boyd's "incestuous amplification" connection (line 19, 52, 61) named consistently.
- Simulation validation claim (line 77): "Riccati-optimal gain reduced steady-state mismatch by 52% compared to fixed gain when observation noise was moderate." Specific number; will spot-check when I reach `#obs-section-i-validation-simulations`.

## Next-segment predictions
`#def-causal-information-yield`. CIY = information-from-interventions. Pearl-level-2 quantity. Probably exact under named scope, robust-qualitative more broadly.

## Brief wandering
The framework's careful Fisher-local-vs-general epistemic tiering (line 42-44) is a model of how to handle "this is exact for the cases I named, approximately right outside them" without overclaim or underclaim. Worth noting positively in §E.

The "$\eta$ too high overfits to noise; $\eta$ too low underfits to genuine error" overfitting characterization (line 63) is the framework's first explicit handling of overfitting and lands cleanly via the mismatch decomposition.
