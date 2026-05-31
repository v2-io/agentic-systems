# Reflection 17 — result-persistence-condition (Section I row 26)

## §4.2 dependency check

`depends: [def-adaptive-tempo, def-mismatch-signal, result-sector-condition-stability, result-sector-persistence-template]`. The last is Appendix A. **F-C7** noted; folded into pattern.

## §4.4 prompts walk-through

**1. Predictions vs evidence.** Predicted: "Central inequality. status:claims-verified. Probably adds cross-domain instantiation tables." Verification: 

- ✓ central inequality / claims-verified stage / status:exact
- ✗ on cross-domain tables — there's no multi-domain instantiation table here. There's one line about software in "Connections" but the rest is structural. My prediction was wrong; the cross-domain instantiations may live elsewhere (probably in the LEXICON or README that I read at the start).

What I didn't predict and is the segment's main move: the **structural persistence vs task adequacy split**. The segment explicitly separates "the machinery works" (Lyapunov-derived; $\alpha > \rho/R$) from "the machinery works *well enough*" (domain-specific; $R^* < \|\delta_{\text{critical}}\|$). This is more sophisticated than I expected and is exactly the kind of scope-honesty move CLAUDE-2.md flagged as distinctive.

**2. Cross-segment consistency.** Forward refs all clean. The "Persistence has a cost, not just a threshold" subsection is the recently-added (2026-04-23 per CLAUDE-2.md priming) #deriv-persistence-cost connection. Lands cleanly here. Good propagation of recent additions. The TST cross-reference (#der-code-quality-as-observation-infrastructure) is annotated explicitly as "cross-component reference, see 02-tst-core/" — good discipline.

The two-sense framing (structural vs task-adequacy) here is *not* the three-sense LEXICON taxonomy (structural / operational / continuity). The third (continuity) is correctly out of scope for this segment. Discipline holds.

**3. Math verification.**
- Structural Model D: $\alpha > \rho/R$. ✓
- Structural Model S: $\alpha > n\sigma_w^2/(2R^2)$. Derive: $R^*_S = \sigma_w\sqrt{n/(2\alpha)} < R \Leftrightarrow n/(2\alpha) < R^2/\sigma_w^2 \Leftrightarrow \alpha > n\sigma_w^2/(2R^2)$. ✓
- Linear operational Model D: $\mathcal T > \rho/\|\delta_{\text{critical}}\|$ — substituting $\alpha = \mathcal T$, $R \to \infty$, the binding becomes $R^* = \rho/\mathcal T < \|\delta_{\text{critical}}\|$. ✓
- Linear operational Model S: $\mathcal T > n\sigma_w^2/(2\|\delta_{\text{critical}}\|^2)$. ✓ Same derivation with the Model S RMS form.
- Per-dimension: dimensions decouple in linear case so the scalar threshold applies per-dimension. ✓

All four threshold forms check out. The 72% scalar-overestimate from anisotropy matches the def-adaptive-tempo claim.

**4. What direction next?** Excitement: row 27 = result-structural-adaptation-necessity (per OUTLINE). The structural-adaptation trigger condition. From CLAUDE-2.md priming, this is one of the inevitability-core segments. Disappointment: if "changing architecture" is hand-waved without mechanism.

**5. What errors should I now watch for?**
- Future segments using "persistence condition" without specifying structural vs task-adequacy. The segment is explicit they're different.
- The linear operational forms being used as if they capture the structural piece (they don't — structural is hidden by linearity since $R \to \infty$).
- Treating $\delta_{\text{critical}}$ as a theory output rather than a domain parameter.

**6. Predictions for next segments.** Row 27 = `result-structural-adaptation-necessity`. status:claims-verified. Probably depends `[def-model-class-fitness, def-mismatch-signal, result-sector-condition-stability]`. Says "when class fitness fails, parametric updates can't close mismatch floor; structural change required."

**7. What would I change?** The "Downstream segments that use the linear operational forms should be understood as expressing task adequacy, not structural stability" warning is in the Epistemic Status — a reader might miss it. Could be lifted to a more prominent location. Mild editorial; not a finding.

**8. What am I now curious about?**

(a) **Operationalization of $\delta_{\text{critical}}$ and $R$.** The framework explicitly defers these to domain. For software, what is $\delta_{\text{critical}}$? "How wrong can the developer's mental model of the codebase be before their changes become harmful?" This is operationalizable but non-trivial. TST's role.

(b) **The TST vicious-cycle hypothesis** ("persistence condition violated through the agent's own prior actions degrading future $\mathcal T$ via $U_o$") is explicitly "not yet formally derived within AAD." It's a hypothesis about how poor code quality (high $U_o$) collapses gain ($\eta^* = U_M/(U_M + U_o) \to 0$) which collapses tempo ($\mathcal T = \nu \eta^*$). The framework knows this isn't yet derived. Worth tracking whether TST tightens this.

(c) The persistence-cost connection ($\dot R \geq n\alpha/2$ nats/time) — Landauer-analog. This is genuinely interesting. AAD's persistence isn't just a threshold; there's a thermodynamic-style cost to maintain it. Two agents with identical persistence guarantees can have wildly different *running costs*. The threshold doesn't distinguish "dormant Kalman filter" from "running-hot adversarial agent." This is structural insight.

(d) The "qualitative transition" framing for structural-threshold violations: "mismatch is not merely large — it grows without effective bound (up to $R$, the sector-condition region). The correction machinery is overwhelmed. This is a qualitative transition, not a gradual degradation." This is a sharp claim about phase-transition-like behavior. Connects to extinction / organizational-collapse / control-instability framings. Worth seeing the empirical content downstream.

**9. What new knowledge enabled.** Persistence as a two-condition concept (structural + task-adequacy). Linear operational forms as task-adequacy expressions. Per-dimension extension. Persistence-cost (Landauer-analog) floor. Structural-adaptation trigger condition. The whole "rate machinery" of AAD lands here as testable inequalities.

**10. Should audit process change?** Continuing. The math-verification round caught the Model S threshold algebra cleanly.

**11. Outline updates.** F-C count: 7. Section E (calibration): the structural/task-adequacy split is one of the framework's clearest scope-honesty moves. Confirms the "epistemic architecture" reframe per CLAUDE-2.md priming. Worth highlighting in the report.

## Status-label / discipline

`status: exact` defended carefully — structural piece exact under stated assumptions; task adequacy exact as a definition; linear operational forms exact for linear correction. Tier-stratification within the segment is honest.

`stage: claims-verified`.

## Cadence check

Holding. Next: row 27 = `result-structural-adaptation-necessity`.
