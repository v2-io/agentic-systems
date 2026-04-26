# Reflection 10 — emp-update-gain (Section I row 19)

## §4.2 dependency check

`depends: [def-mismatch-signal, def-observation-function]`. Both upstream. **No backward-dependency finding.** Depends list appears complete for the Formal Expression's symbols ($M_t$ reached via def-mismatch-signal → form-agent-model). **No F-A drift.**

## §4.4 prompts walk-through

**1. Predictions vs evidence.** Predicted (in reflection 09): "$\eta^* = U_M / (U_M + U_o)$ (Kalman-type), status:exact for Bayesian + robust-qualitative for general." ✓ exactly correct.

**2. Cross-segment consistency.** References to read segments (def-mismatch-signal, def-observation-function, result-mismatch-decomposition) are clean. Forward refs to def-adaptive-tempo, result-structural-adaptation-necessity, der-gain-sector-bridge. Internal consistency.

**3. Math verification.** Scalar Kalman gain in 1D: posterior variance = $U_M U_o / (U_M + U_o)$; posterior mean update weight $K = U_M / (U_M + U_o)$. ✓ matches the segment's claim.

**4. What direction next?** Excitement: how the gain interacts with adaptive tempo to land the persistence condition. Also how the recently-added #deriv-adaptive-gain-dynamics extends this to settings where $K$ is itself a state variable (per CLAUDE-2.md priming). Disappointment: if the gain stays empirical-tier forever without sharper bounds for non-Bayesian agents.

**5. Errors to watch for.**
- Conflating scalar $\eta^*$ with matrix Kalman gain in multi-dim cases.
- "Gain collapse" claims not tied back to $U_M \to 0$ or $U_o \to \infty$ mechanism.
- Future segments using $\eta^*$ as if always exact (it's empirical/robust-qualitative).

**6. Predictions for next segments.** Row 20 = `def-causal-information-yield`. CIY definition. Probably definition-type, status:axiomatic. Cites #def-pearl-causal-hierarchy.

**7. What would I change?** The "Open questions" block at the end (1: non-parametric models; 2: matrix vs scalar) is structurally unusual — most segments use Working Notes for open questions. Could move there. Mild style; not a finding.

**8. What am I curious about?** "Gain collapse — epistrophe failure" is a beautifully-named pathology: aporia still arrives, but the corrective phase is hollow. This connects to **stability-induced-myopia** (per CLAUDE-2.md priming, the #deriv-detection-latency content): when $U_M$ artificially collapses (overconfidence), $\eta^* \to 0$, observations get ignored, regime-change detection latency blows up. So gain-collapse and detection-latency-blowup are two angles on the same agent pathology. Whether the segments actually surface this connection is something to track.

**9. What new knowledge enabled.** $\eta^*$ feeds into adaptive tempo $\mathcal T = \nu \cdot \eta^*$, the sector-condition bridge, the persistence condition. Empirical-tier framing keeps the claim honest about scope.

**10. Should audit process change?** Math-verification habit confirmed: when there's a closed-form claim, run it. Continuing.

**11. Outline updates.** No new findings. Section E (calibration) gets one more confirmation: an empirical-tier segment labeled honestly with ✓ math under Bayesian/Kalman case + scope-acknowledged-as-robust-qualitative for general. Discipline holding.

## Status-label / discipline

`status: robust-qualitative` and `type: empirical` for the broad claim, with `*[Empirical Claim (uncertainty-ratio-principle)]*` tag specifically attached to the formula. The Epistemic Status carefully says "Exact for linear-Gaussian and conjugate Bayesian; robust qualitative for general." Tier-stratified honestly within the segment.

`stage: claims-verified` — appropriate.

## Cadence check

One Read → 11 prompts → reflection → next. Holding.

Next: Section I row 20 = `def-causal-information-yield`.
