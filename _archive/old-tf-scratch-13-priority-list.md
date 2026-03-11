# Integrated Improvement Priorities
**Sources:** Opus re-review (scratch/12), Codex (scratch/TFT-full-feedback), Gemini (scratch/12-gemini-tft-comprehensive-feedback)
**Date:** 2026-02-27

Items already resolved in this session or earlier revisions are omitted.

---

## Tier 1 — Precision Hardening (high ROI, tractable edits)

### 1. Proposition 5.1 proof: add explicit measurability assumption
**Source:** Codex C
**Where:** TF-05, lines 37-42
**Issue:** The cross-term vanishing argument uses orthogonality via the tower
property. This is correct but relies on an assumption that isn't stated: that
$\hat{o}_t - \bar{o}_t$ is $\Omega_t$-measurable (i.e., the model prediction
error is a deterministic function of $\Omega_t$ once $M_{t-1}$ and $a_{t-1}$
are fixed). Technical readers will notice the gap.
**Fix:** Add one line to the proof making this explicit. Small edit.

### 2. Unified policy objective: acknowledge unit incommensurability
**Source:** Codex B, Gemini A (related)
**Where:** TF-08, lines 9-12
**Issue:** $\mathbb{E}[\text{value}(a)] + \lambda \cdot \mathbb{E}[\text{CIY}(a)]$
adds value-units to information-units. Without normalization, $\lambda$ is
doing dimensional work that isn't acknowledged.
**Fix:** Add a note after the objective stating that $\lambda$ must absorb
the conversion between value and information units, and that the objective
is structural (it identifies the *form* of the trade-off) rather than directly
computable without domain-specific normalization. State that it is normative
(a design criterion), not descriptive. Add a brief Kalman dual-control or
bandit instantiation showing how units resolve in a specific case.

### 3. $\mathcal{T} > \rho$ shorthand: use normalized form in formal statements
**Source:** Codex D
**Where:** TF-11 (throughout), Appendix A references
**Issue:** The shorthand $\mathcal{T} > \rho$ appears in or near formal
propositions where the normalized form
$\mathcal{T} > \rho / |\delta_{\text{critical}}|$ is what's actually meant.
TF-11 line 7 already explains this, but the shorthand still appears in
formal passages without local annotation.
**Fix:** In Proposition 11.1's persistence condition and the adversarial
dynamics section, use the full normalized form at least once per formal
statement. Keep the shorthand in prose with a parenthetical "(normalized)."

### 4. Appendix A: acknowledge bounded-disturbance limitation
**Source:** Gemini D
**Where:** Appendix A, after Proposition A.1 or in a new "Limitations" note
**Issue:** $\|w(t)\| \leq \rho$ assumes bounded disturbance. Real systems
(financial markets, warfare, ecological shocks) face heavy-tailed
disturbances where this bound is violated.
**Fix:** Add a brief note: "The bounded-disturbance assumption excludes
heavy-tailed (power-law) shocks where $\|w(t)\|$ can exceed any finite bound
with non-negligible probability. For such environments, stochastic Lyapunov
methods (martingale stability, input-to-state stability in probability) would
be needed. The bounded case captures the typical operating regime; extreme
tail events may require structural adaptation (TF-10) rather than parametric
correction." ~3 sentences.

---

## Tier 2 — Structural Improvements (moderate effort, real value)

### 5. Derived vs. discussion transition markers
**Source:** Codex E
**Where:** TF-07, TF-08, TF-11 adversarial section
**Issue:** Some passages transition from formally derived claims to
interpretive/analogical claims without clear markers. Risk of perceived
over-claiming.
**Fix:** Add brief markers like "**Derived consequence:**" vs.
"**Interpretive implication:**" at key transition points. Moderate effort
(requires careful re-reading of mixed sections).

### 6. TF-09 deliberation cost: note resource costs in formal section
**Source:** Gemini C
**Where:** TF-09, near Proposition 9.1
**Issue:** Deliberation cost is modeled as purely temporal ($\rho \cdot \Delta\tau$).
Open Question #1 already notes resource costs exist. But the formal result
doesn't mention them, which could mislead.
**Fix:** Add one sentence after Proposition 9.1: "This captures the temporal
cost; real agents also incur computational/energetic costs $C(\Delta\tau)$
that are additive with the mismatch cost and would tighten the threshold
further (see Open Question #1)." Small edit.

### 7. CIY: regime-qualify downstream references
**Source:** Codex A
**Where:** TF-08 (unified objective), TF-06 (CIY connection section)
**Issue:** CIY is used in equations without noting which admissibility
regime applies. The regimes are defined in TF-02 but not referenced at
point of use.
**Fix:** Add "(Regime A)" parenthetical after CIY terms in TF-08's
objective and TF-06's connection section, or add a note: "The CIY term
assumes the agent operates in Regime A (randomized interventions) or
Regime B (with causal assumptions); see TF-02."

### 8. README: fix TOC table visual break
**Source:** Codex (doc note)
**Where:** README.md, around TF-08/TF-09 row
**Issue:** There's a blank line in the TOC table between TF-08 and TF-09
that breaks the table visually in some renderers.
**Fix:** Remove the blank line. Trivial.

---

## Tier 3 — Extensions and Completeness (lower urgency, future work)

### 9. Multi-model agents as known limitation
**Source:** Opus
**Where:** TF-03 or README
**Note:** TF-03 treats "the model" as singular. Ensembles, mixture-of-experts,
red teams, and organizational sub-models are not addressed. Worth a note.

### 10. Post-fork initialization quality
**Source:** Opus
**Where:** TF-02, temporal continuity section
**Note:** How much model value survives forking? Relevant for LLM context
management and organizational spinoffs.

### 11. Scalar vs. vector mismatch: centralize reduction assumptions
**Source:** Codex (medium #1), Gemini B
**Where:** New subsection in TF-00 or TF-11
**Note:** The scalar/vector tension appears in multiple places. A single
"reduction assumptions" paragraph would reduce repetition.

### 12. TF-04 status resolution
**Source:** Opus
**Where:** TF-04, README
**Note:** Commit to event-driven as primary or fold into TF-00/TF-06.

### 13. Falsifiability note
**Source:** Opus
**Where:** README
**Note:** What observations would challenge TFT? Worth enumerating.

### 14. Channel correlation in additive tempo
**Source:** Opus
**Where:** TF-11 or TF-04
**Note:** $\sum_k \nu^{(k)} \cdot \eta^{(k)*}$ overestimates when channels
provide redundant information.

### 15. TF-06 domain validation nuance
**Source:** Opus
**Where:** TF-06, after Kalman validation
**Note:** Kalman/Bayes cases are derived-from-optimality, not independent
empirical validations.

### 16. Operational trigger candidates for structural change
**Source:** Codex (TF-10 note)
**Where:** TF-10
**Note:** Residual autocorrelation test, validation drift, etc. as
implementable signals.

### 17. Heavy-tail / stochastic stability extension
**Source:** Gemini D
**Where:** Appendix A (future work)
**Note:** Full stochastic Lyapunov treatment for unbounded disturbances.

### 18. Trust calibration: minimal formal update equation
**Source:** Codex (TF-08 note)
**Where:** TF-08
**Note:** Trust in query sources should have at least a sketch of a
formal update rule (Bayesian trust update on source reliability).

---

## Suggested Execution Order

**Batch 1 (can do now, ~30 min):**
Items 1, 3, 4, 6, 7, 8 — all are small, focused edits to existing text.

**Batch 2 (requires more thought, ~1 hr):**
Item 2 (policy objective normalization) — needs a concrete instantiation.
Item 5 (derived vs. discussion markers) — requires careful re-reading.

**Batch 3 (future sessions):**
Items 9-18 — extensions and completeness work.
