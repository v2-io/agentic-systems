# Reflection 13 — hyp-mismatch-dynamics (Section I row 22)

## §4.2 dependency check — CRITICAL FINDING (second instance)

`depends: [def-adaptive-tempo, def-mismatch-signal, deriv-sector-condition]`.

- `def-adaptive-tempo`: row 21 ✓
- `def-mismatch-signal`: row 17 ✓
- **`deriv-sector-condition`: Appendix A — DOWNSTREAM of Section I.** Not yet read.

**F-C2:** Second instance of the §4.2 critical-finding pattern. Section I segment depends on Appendix A derivation. Same structural shape as F-C1 (der-recursive-update → deriv-recursive-update). The two-instance count strengthens the case that this is a *recurring pattern* — main-section claims back-pointing to appendix derivations — not an isolated OUTLINE error.

Reading the segment with the gap noted. Without `deriv-sector-condition`, I see the linear-ODE form and its consequences but not the proof of the nonlinear sector-condition extension.

## §4.4 prompts walk-through

**1. Predictions vs evidence.** Predicted: "$d\|\delta\|/dt = -\mathcal T \|\delta\| + \rho$. status:hypothesis. Depends on def-mismatch-signal, def-adaptive-tempo, GA-5." Verification: ✓ ODE form. status:heuristic (close enough to hypothesis). ✓ on first two depends. The third dep is `deriv-sector-condition` — F-C2.

**2. Cross-segment consistency.** The "bridging assumption" paragraph references `#deriv-discrete-sector-condition` for the variance gap form $O(\eta^* c_{\max})$. Per CLAUDE-2.md priming, this is the F-V1-corrected form (was previously wrongly stated as $O((\eta^*)^2)$). The current segment's text uses the corrected form ✓ — F-V1 fix has propagated here.

**3. Math verification.**
- Steady state: $\mathcal T \|\delta\|_{ss} = \rho \Rightarrow \|\delta\|_{ss} = \rho/\mathcal T$. ✓
- Transient: $\|\delta(t)\| = \|\delta_0\| e^{-\mathcal T t} + (\rho/\mathcal T)(1 - e^{-\mathcal T t})$. Standard linear ODE with constant input. ✓
- Model S RMS: $dX = -\theta X\, dt + \sigma\, dW$ is OU; stationary variance $\sigma^2/(2\theta)$; RMS $= \sigma/\sqrt{2\theta}$. With $\theta = \mathcal T$, $\sigma = \sigma_w$: ✓ matches the segment.
- Multi-dim: $\sigma_w \sqrt{n/(2\mathcal T)}$ — for n-dim OU with isotropic noise, $\text{tr}(\Sigma_\infty) = n \sigma_w^2 / (2\mathcal T)$, so $\|\delta\|_{rms} = \sigma_w \sqrt{n/(2\mathcal T)}$. ✓

The adversarial exponents (squared law for D, 3/2 for S) — I'll defer detailed verification to when I read `#result-adversarial-tempo-advantage`. The form is consistent: under Model D, $\|\delta\| \propto 1/\mathcal T$, so a comparison ratio $\|\delta_A\|/\|\delta_B\|$ involving coupling has $\mathcal T$ entering in numerator and denominator → squared. Under Model S, $\|\delta\| \propto 1/\sqrt{\mathcal T}$, so the same comparison gives 3/2. Plausible at the structural level.

**4. What direction next?** Excitement: the rigorous sector-condition treatment (which I'll see in deriv-sector-condition / result-sector-condition-stability) that replaces this heuristic linear ODE. Also the per-dimension extension. Disappointment: if the linear-ODE intuitions fail to generalize (sector condition restricting the nonlinearities is exactly what handles this).

**5. Errors to watch for.**
- Future segments using the linear ODE as if exact (it's heuristic).
- Confusing Model D with Model S in adversarial contexts.
- The "$\rho/\mathcal T$" steady-state form has dimensional caveat per NOTATION.md ("the persistence condition $\mathcal T > \rho/\|\delta_{\text{critical}}\|$ is dimensionally consistent; the shorthand '$\mathcal T > \rho$' is valid only when $\|\delta_{\text{critical}}\|$ is normalized to 1"). Future segments using the shorthand without acknowledging the normalization = potential finding.

**6. Predictions for next segments.** Row 23 = `der-deliberation-cost`. Think-vs-act tradeoff. status:derived (per OUTLINE table, claims-verified stage). Probably uses GA-4 (local deliberation drift).

**7. What would I change?** Move the F-C2 issue (deriv-sector-condition in depends despite being downstream in OUTLINE) — or accept that main-result→appendix-derivation back-pointers are an OUTLINE-order exception. This is the same architectural decision as F-C1.

**8. What am I now curious about?** The Model D vs Model S distinction has a sharp formal consequence: $1/\mathcal T$ vs $1/\sqrt{\mathcal T}$ scaling. "Correction is less effective against noise than against drift." This is testable — in domains where the dominant disturbance is noise-like (high-frequency, zero-mean), tempo-doubling cuts mismatch by $\sqrt 2$, not 2. In drift-dominated domains, tempo-doubling cuts mismatch by 2. Worth tracking whether downstream domain instantiations honor this distinction or treat the scaling generically.

**9. What new knowledge enabled.** Steady-state mismatch ratios; persistence threshold definability; exponential transient; adversarial-tempo-exponent foundation; bridging assumption to discrete dynamics with quantified gap.

**10. Should audit process change?** Continuing. F-C-class findings now at 2 instances; pattern is firming up. I should keep flagging each instance but emphasize the *pattern* in the eventual report rather than treating each as independent.

**11. Outline updates.** Adding F-C2 to Section B. The F-C series and F-A series are both pattern-level findings; the report should treat them as such, with individual instances catalogued under each pattern.

## Status-label / discipline

`status: heuristic` for the linear ODE — appropriate. The general nonlinear treatment is deferred to result-sector-condition-stability. The within-segment `*[Derived (...)]*` tags on the steady-state forms are tier-stratified honestly: derived from the linear hypothesis (so derivations are exact *given the linear form*, not exact in general).

`stage: deps-verified`.

## Cadence check

Holding.

Next: Section I row 23 = `der-deliberation-cost`.
