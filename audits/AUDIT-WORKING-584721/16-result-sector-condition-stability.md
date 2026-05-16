# Reflection 16 — result-sector-condition-stability (Section I row 25)

## §4.2 dependency check

`depends: [def-adaptive-tempo, def-mismatch-signal, deriv-sector-condition, result-sector-persistence-template]`. The latter two are Appendix A. **F-C5 and F-C6** noted; folding into the meta-pattern (per reflection 15's adjustment).

## §4.4 prompts walk-through

**1. Predictions vs evidence.** Predicted (in reflection 15): "Row 25 = result-sector-condition-stability. Lyapunov persistence theorem. status:claims-verified, depends deriv-sector-condition (Appendix A → F-C instance)." ✓ on all three; got two F-C instances rather than one.

**2. Cross-segment consistency.** Frame: this segment is "the single-agent epistemic instantiation of the sector-persistence template" (#result-sector-persistence-template, Appendix A). The template was — per CLAUDE-2.md priming — "factored out as shared lemma" and now multiple AAD persistence-flavored results are re-expressed as instances. So this segment was retrofitted to be one template-instance among several. Cross-segment consistency holds; the result here is a special case of a more general result.

**3. Math verification.**
- $R^* = \rho/\alpha$: setting $-\alpha\|\delta\| + \rho = 0$ gives $\|\delta\| = \rho/\alpha$. ✓
- Persistence: $\alpha > \rho/R$ ⟺ $R^* < R$ (steady state stays inside validity region). ✓
- Adaptive reserve $\Delta\rho^* = \alpha R - \rho$: amount by which $\rho$ can grow before $R^* > R$. ✓
- Model S: $R^*_S = \sigma_w\sqrt{n/(2\alpha)}$ — n-dim OU stationary variance trace = $n\sigma_w^2/(2\alpha)$, RMS = $\sigma_w\sqrt{n/(2\alpha)}$. ✓

The "$\alpha = \mathcal T$ exactly" claim for the linear case: in continuous-time linear ODE form $d\delta/dt = -\mathcal T \delta + w$, the sector inner product gives $\delta^T(-\mathcal T \delta) = -\mathcal T \|\delta\|^2$, so $\alpha = \mathcal T$. ✓

But wait — der-gain-sector-bridge uses $\alpha = \eta^* c_{\min}$. For linear-identity $g(\delta) = \delta$, $c_{\min} = 1$, so $\alpha = \eta^*$. And $\mathcal T = \nu \eta^*$. So $\alpha = \mathcal T / \nu$ at the per-event level vs $\alpha = \mathcal T$ at the continuous-time level. These reconcile through the fluid limit (deriv-discrete-sector-condition): the discrete-event-rate $\nu$ becomes implicit in the continuous-time form.

Not an inconsistency — two natural framings (continuous-time vs discrete-event-driven) joined by the fluid limit. But a casual reader might be confused about which $\alpha$-vs-$\mathcal T$ relationship is "the" relationship. Worth noting in Section E (calibration): the framework has two natural framings here that are joined by an Appendix A bridge — readers should know which they're in.

**4. What direction next?** Excitement: result-persistence-condition (next) as the central inequality formulation. Disappointment: if it's just a restatement of this segment's result without added structural content. From the OUTLINE / CLAUDE-2.md priming, I expect it to add the "α/T relationship verified across all correction function classes" content and the cross-domain instantiation tables.

**5. What errors should I now watch for?**
- Conflation of $\alpha$ (sector parameter) with $\mathcal T$ (adaptive tempo). They coincide in linear-correction-continuous-time framing; differ generally.
- Confusion of the continuous-time $\alpha$ with the discrete-event $\eta^* c_{\min}$. They reconcile via the fluid limit but are formally distinct.
- Future segments using "$\alpha = \mathcal T$ exactly" without the linear-correction caveat = finding.

**6. Predictions for next segments.** Row 26 = `result-persistence-condition`. Central inequality. status:claims-verified. Probably adds cross-domain instantiation tables (control / RL / orgs / software).

**7. What would I change?** The "$\alpha = \mathcal{T}$ exactly" line has the implicit "in the continuous-time linear case" qualifier; making it explicit would prevent reader confusion with the per-event $\alpha = \eta^*$ form from der-gain-sector-bridge. Mild editorial; not a finding.

**8. What am I now curious about?** Two threads:

(a) The "factored out as shared lemma" history of result-sector-persistence-template. Multiple persistence-flavored results were re-expressed as instances. Curious which other results (besides this one) instantiate it. CLAUDE-2.md mentions critical-mass composition, contraction template, etc. — Section III instances. So the template links Section I and Section III.

(b) Model D vs Model S as "domain question, not a theory question" — the Epistemic Status frames the choice as which disturbance model fits the application, not as a theory commitment. But the framework keeps both. This is an interesting scope-honesty move: the theory provides results for both, and the user picks which applies. Curious whether downstream uses commit to one or oscillate between them per context.

**9. What new knowledge enabled.** Persistence machinery formally derived from sector condition. Adaptive reserve as a measurable quantity. Model D / Model S split with explicit scaling differences ($1/\alpha$ vs $1/\sqrt\alpha$). Sets up result-persistence-condition.

**10. Should audit process change?** Continuing. The math-verification habit keeps surfacing reconciliations (this round: $\alpha = \mathcal T$ vs $\alpha = \eta^* c_{\min}$ as different framings) that I'd miss with charitable reading.

**11. Outline updates.** F-C count: 6. Section E (calibration): one more inevitability-core confirmation. Section E candidate: the "two-framing" issue ($\alpha = \mathcal T$ in continuous-time vs $\alpha = \eta^* c_{\min}$ in per-event) joined by fluid limit — readers should know which framing they're in. Probably worth a sentence in the report.

## Status-label / discipline

`status: exact` defended carefully; the "instantiation of template" framing makes the exactness inherited from the template's machinery. `stage: claims-verified`.

## Cadence check

Holding. Next: Section I row 26 = `result-persistence-condition`.
