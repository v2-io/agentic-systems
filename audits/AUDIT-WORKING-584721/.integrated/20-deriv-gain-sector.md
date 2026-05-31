# Reflection 20 — deriv-gain-sector (Appendix A; cited from der-gain-sector-bridge)

The proofs and numerical validation for the bridge theorem.

## §4.2 dependency check

`depends: [emp-update-gain, deriv-sector-condition]`. Both upstream (and just read for deriv-sector-condition). **No backward-dep finding.**

## §4.4 prompts walk-through

**1. Predictions vs evidence.** Predicted: "Prop B.3 (gain-sector bridge), Prop B.4 (gradient-sector equivalence), counterexample FM-1, simulation validation tables." Verification: ✓ all four. Plus Props B.1 (scalar Kalman) and B.2 (matrix Kalman) at the front, which I didn't predict. The matrix Kalman case in $(P^-)^{-1}$-weighted norm is more substantive than I expected.

**2. Cross-segment consistency.** Cross-refs to emp-update-gain (read), deriv-sector-condition (just read), and forward refs to der-observability-dominance, result-structural-adaptation-necessity, result-per-dimension-persistence. The Prop B.4 gradient-equivalence connects to the Nesterov 2004 Theorem 2.1.10 (gradient-monotonicity characterization of strong convexity) — standard convex-optimization reference.

**3. Math verification (at discretion — exercising it on the matrix-Kalman case since it's the new material I haven't checked).**

Prop B.2 matrix Kalman:
- Inner-product weighted by $(P^-)^{-1}$: $\langle e, KH\, e \rangle_{P^-} = e^T (P^-)^{-1} KH\, e$.
- Substitute $K = P^- H^T S^{-1}$: $(P^-)^{-1} \cdot P^- H^T S^{-1} \cdot H = H^T S^{-1} H$. ✓
- $S = HP^- H^T + R_{\text{obs}} \succ 0$, so $S^{-1} \succ 0$, so $H^T S^{-1} H \succeq 0$. With null space $\ker(H)$. ✓
- Kalman covariance identity: $P = (I - KH) P^-$, giving $KH = I - P(P^-)^{-1}$. ✓
- Eigenvalues of $KH$ in $(P^-)^{-1}$-sense are $1 - \lambda_i(P(P^-)^{-1})$, all in $[0, 1]$ since $0 \preceq P \preceq P^-$. So $\alpha = 1 - \lambda_{\max}(P(P^-)^{-1}) \geq 0$. ✓

Prop B.4 gradient equivalence:
- Forward: GA-3 ($\delta^T F \geq \alpha\|\delta\|^2$) divided by $\eta$ gives $\delta^T \nabla L(M^* + \delta) \geq (\alpha/\eta)\|\delta\|^2$. With $\nabla L(M^*) = 0$, this is gradient monotonicity at $\mu = \alpha/\eta$, equivalent to $\mu$-strong convexity (Nesterov 2.1.10). ✓
- Reverse: $\mu$-strong convexity gives gradient monotonicity, multiply by $\eta$, recover GA-3 with $\alpha = \eta\mu$. ✓

**Math is sound.** Standard Kalman algebra and standard convex-optimization machinery applied correctly to the AAD framing.

**4. What direction next?** Reading result-sector-persistence-template next — the abstract template that this segment's specific results instantiate. I expect: state-variable / correction-function / disturbance-model abstraction with multiple AAD-instantiation rows (Section I single-agent, Section III composition, etc.).

**5. What errors should I now watch for?**
- Future segments using the bridge theorem without acknowledging B1 is conditional.
- Confusion of "global" cases (exponential family, L2-regularized) with "local" cases (logistic, non-convex).
- Treating non-convex agents within a basin as if globally persistent.
- Future Discussion claims about "reserve" or "robustness" without using the $\alpha = \eta\mu$ factorization.

**6. Predictions for next segments.** Reading next: `result-sector-persistence-template`. Abstract template segment. Probably status:draft per OUTLINE table. Likely depends on def-mismatch-signal, def-adaptive-tempo, deriv-sector-condition. Should have multiple instantiation rows (this segment, der-team-persistence, etc.).

**7. What would I change?** The "Loss Function Classification" table is a clean exemplar — concrete loss classes with their sector parameters, basin radii, and exact-vs-local status. Could be a model for other segments. The simulation summary section is well-disciplined: results stated, code/traces deferred to msc/spike. No padding.

**8. What am I now curious about?**

(a) The "fluid-limit gap" Working Note: expected-value analysis at the bridge layer (Prop B.3); stochastic per-step gives effective disturbance $\|K\|\sigma_\varepsilon$, which enters as Model S disturbance under Prop A.1S. So expected-bridge + stochastic-disturbance compose: the framework is consistent across deterministic-mean and stochastic-noise treatments. Nice structural property.

(b) The α factorization $\alpha = \eta\mu$ — separates agent-design (gain) from environment-structure (curvature). Adaptive reserve $\Delta\rho^* = \eta\mu R - \rho$. Three controllable factors. Robustness comes from $\eta\mu R \gg \rho$. This is operationally useful: an agent designer has $\eta$ to tune; environment gives $\mu, R$; persistence demands $\rho$. The ratio is the diagnostic.

(c) The "basin boundary = structural adaptation trigger" framing has appeared in three segments now (here, deriv-sector-condition, der-gain-sector-bridge). It's a load-bearing geometric picture: convexity basins as the parametric-adaptation regime; basin exit as structural-change trigger. Curious whether result-structural-adaptation-necessity formalizes this geometrically or qualitatively.

(d) The "fully observable diagonal case" (Prop B.2) gives $\alpha = \min_i K_i$ — the bottleneck dimension determines persistence. This matches result-per-dimension-persistence. The 72% scalar-overestimate from def-adaptive-tempo's anisotropy claim presumably comes from averaging where minimization is the right operation.

**9. What new knowledge enabled.** Bridge theorem closes the gap from "GA-3 assumed" to "GA-3 derived" for sub-scope α. The α factorization $\alpha = \eta\mu$ separates agent-design from environment-structure. Loss-function classification gives concrete examples. Simulation validation across six classes. The whole sector-condition machinery is now grounded.

**10. Should the audit process change?** Continuing. Math verification was useful — caught the elegance of the matrix-Kalman weighted-norm derivation.

**11. Outline updates.** Section E (calibration) gets a substantial confirmation. Section D candidate: the "expected-value bridge + stochastic-disturbance composition" as a meta-pattern (the framework's expected-bridge results compose cleanly with Model S noise treatments). Worth surfacing.

## Status-label / discipline

`status: conditional` for the bridge (correctly conditional on B1). Tier-stratification within the segment: Props B.1, B.2 exact; Prop B.3 conditional; Prop B.4 exact equivalence. `stage: deps-verified`.

## Cadence check

Next: `result-sector-persistence-template` (last cited appendix from the main-section read so far).
