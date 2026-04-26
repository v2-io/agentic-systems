# Reflection 11 — def-causal-information-yield (Section I row 20)

## §4.2 dependency check

`depends: [def-pearl-causal-hierarchy, der-action-selection, def-mismatch-signal]`. All upstream. **No backward-dep finding.** Transitive closure covers all symbols. **No F-A drift.**

## §4.4 prompts walk-through

**1. Predictions vs evidence.** Predicted: "CIY definition. Probably definition-type, status:axiomatic. Cites #def-pearl-causal-hierarchy." Result: ✓ definition + Pearl reference. **Off on status** — actual is `status: exact`, not axiomatic. The segment defends "the definition is well-grounded; the quantity itself is standard (expected KL under do-calculus)" — `exact` for a definition is unusual but not crazy here.

**2. Cross-segment consistency.** Cross-refs are clean. The "old-tf-appendix-f-multi-agent.md" reference at the end points to source material in old-* set; not a finding (old-* files are deliberately preserved per FORMAT.md). Internal consistency holds.

**3. Math verification.** $\text{CIY} = \mathbb E_{a' \sim q}[D_{\mathrm{KL}}(P(o|do(a)) \| P(o|do(a')))]$ is non-negative by construction (KL ≥ 0; expectation of non-negatives ≥ 0). CIY = 0 iff outcome distributions are equal across actions iff actions don't distinguish. ✓ Trivially correct.

**4. What direction next?** Excitement: a downstream derivation that actually *uses* CIY in policy selection — does it become central or peripheral? Also: how the EIG-vs-CIY distinction plays out in #disc-ciy-unified-objective. Disappointment: if CIY remains a definitional nice-idea that doesn't drive derivations.

**5. What errors should I now watch for?**
- Future segments conflating CIY (action-distinguishability) with EIG (expected information gain). The segment is explicit they're distinct.
- The $\lambda$ weighting is *heuristic* per the Epistemic Status; future segments treating it as derived = finding.
- "CIY measures learning value" claims are *wrong* per this segment.

**6. Predictions for next segments.** Row 21 = `def-adaptive-tempo`. Definition of $\mathcal T$, likely $\mathcal T = \sum_k \nu^{(k)} \eta^{(k)*}$ (per NOTATION.md and form-event-driven-dynamics). status:axiomatic or definition-grade.

**7. What would I change?** The "Open direction: proper EIG within AAD" paragraph honestly admits CIY is a surrogate for EIG. The Epistemic Status correctly tier-stratifies (definition exact; surrogacy heuristic). Could perhaps move the "Open direction" paragraph to Working Notes since it's about future work; not a finding.

**8. What am I curious about?**

- The "Query actions" subsection — queries to other agents have qualitatively different information density. "Single well-targeted query can carry CIY orders of magnitude higher than individual environment probes." This is essentially the logogenic-agents foundation — language as a high-CIY channel. Whether the formal treatment lives downstream or whether it's a real gap is something to track when I reach 03-logogenic.

- The "adversarial mirror" subsection: deception produces positive CIY but drives mismatch *up*. So high-CIY + low-trust = anti-learning. This is a surprisingly clean unification of "deception" with the formal apparatus — adversarial disturbance injected through the observation channel with coupling $\gamma_A$ from trust level. Worth tracking how the formalism handles this in #der-adversarial-destabilization.

**9. What new knowledge enabled.** CIY as quantitative action-causal-impact measure. Distinguishes Level 2-using from Level 1-only actions. Inputs to unified policy objective. Enables formal treatment of queries and of adversarial deception.

**10. Should audit process change?** Continuing.

**11. Outline updates.** No new findings. Section E (calibration) gets confirmation of within-segment tier-stratification (definition exact + EIG-surrogacy heuristic, in the same segment).

## Status-label / discipline

`status: exact` for the definition (defended carefully); `stage: deps-verified`. Within-segment tier-stratification is honest.

## Cadence check

One Read → 11 prompts → reflection → next. Holding.

Next: Section I row 21 = `def-adaptive-tempo`.
