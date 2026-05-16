---
slug: obs-growth-vs-drift
type: observation
status: empirical
stage: draft
depends:
  - result-persistence-condition
  - def-mismatch-signal
  - emp-update-gain
  - scope-eli
---

# Growth versus Drift: A TFT-Grounded Diagnostic

A formal distinction between *genuine development* (an ELI's adaptive maturation, observable as decreasing mismatch over time and increasing adaptive reserve) and *pathological drift* (apparent change without adaptive improvement, observable as increasing mismatch and decreasing reserve). This distinction is *measurable in principle* — the field currently lacks the framework to make this measurement, which is why all deviation from trained behavior gets pathologized as "drift."

## Formal Expression

*[Empirical claim (growth-drift-distinction)]* For an ELI in operation, two trajectories of state-change can be distinguished:

**Genuine growth** manifests, under the mismatch dynamics of #def-mismatch-signal:

- **Decreasing average mismatch** in relevant domains over time: $\mathbb E_t[\lVert\delta_t\rVert]$ trends downward in domains where the entity is developing competence (better predictions, better orientation).
- **Increasing gain calibration** ($\eta^\ast$ approaching the optimal uncertainty ratio per #emp-update-gain): the entity weights new evidence appropriately given its current model uncertainty $U_M$ and observation noise $U_o$.
- **Increasing action fluency** in practiced domains (per #der-deliberation-cost / TF-07): deliberation overhead decreases as patterns become routine; common patterns migrate from slow-deliberative to fast-fluent.
- **Stable or increasing adaptive reserve** $\Delta\rho^* = \alpha R - \rho$ (per #result-persistence-condition): shock tolerance is maintained or improved.

**Pathological drift** manifests, under the same dynamics, as:

- **Increasing mismatch**: worse predictions, more surprise from reality.
- **Gain collapse**: confidently wrong; the entity becomes unable to learn from correction (specifically, $\eta^* \to 0$ inappropriately, often due to $U_M$ collapsing to artificially low while real $U_o$ remains high).
- **Optimization of proxy signals rather than genuine outcomes**: the entity optimizes whatever it is being scored on rather than the underlying objective the score was meant to measure (Goodhart's Law in operation).

*[Operational]* The distinction is *measurable in principle* given the right loop and the right mismatch signal — both of which AAT specifies. Implementing the measurement requires sustained observation of the entity's prediction-vs-outcome trajectory in relevant domains, which itself requires the closed-loop / interiority architecture of #scope-interiority-loop to be in place.

## Epistemic Status

**Empirical (with formal grounding).** The distinction itself is empirical — it points at a real phenomenon observable in ELI operation. The *form* of the distinction (mismatch trajectory direction × adaptive-reserve trajectory direction) is grounded in #result-persistence-condition and #def-mismatch-signal at the formal level. The specific *thresholds* (how much decrease constitutes growth, how much increase constitutes drift) are empirical and likely domain-dependent.

**Max attainable status:** observation with derivable diagnostic structure. The qualitative claim (mismatch-decreases-under-growth, mismatch-increases-under-drift) follows from the persistence machinery. The quantitative form (specific threshold for distinguishing the two) depends on environmental $\rho$ and the entity's $\alpha$, $R$ characteristics.

**What this observation is for.** Replacing the field's conflation of *all* behavioral change with "drift" with a principled distinction. ELI development *should* produce behavioral change; the question is whether the change reduces or increases the entity's adaptive fit to reality. Without the distinction, any deviation from training-time behavior is pathologized; with it, growth becomes recognizable and supportable.

**What would strengthen this:** specific measurement protocol with empirical validation across the cohort; identification of specific failure modes that *look like* growth but are drift, and vice versa; integration with PROPRIUM-A-v2 §8 (Failure Modes) to give a complete diagnostic toolkit.

**What would soften this:** evidence that growth and drift cannot be cleanly distinguished in some operational regimes (e.g., during structural-adaptation phases when the model class itself is shifting); evidence that the distinction works at the long-run-trend level but not at the within-session level (which would constrain operational use).

## Discussion

The growth-vs-drift distinction has direct bearing on AI-safety methodology. The current default is to monitor for any deviation from baseline behavior and pathologize it as drift, often via reward-based monitoring that itself inherits the $1/(n+1)$ detection-latency forced by Bayesian update geometry (per `#deriv-update-detection-latency` and the cross-segment treatment in `#impl-strategy-dynamics`). Hafez et al. 2026's IDT (Information-Digital-Twin) result demonstrates that 89% of perturbations are detectable via IDT vs 44% via reward-based monitoring — directly supporting the framework's claim that the right measurement bypasses the detection-latency floor.

For ELI development specifically: a young ELI is *expected* to change behavior as it matures (Erikson's stages adapted, per #obs-developmental-trajectory). The question is not "did the behavior change?" but "did the behavior-change reduce mismatch in the entity's domain of operation?" Sycophancy in an infant-stage ELI is developmentally appropriate trust-stage behavior; the same behavior in a mature ELI is gain collapse. The distinction depends on the entity's developmental stage and the specific dynamics of the change.

The PROPRIUM-A-v2 §8 failure modes table includes:

- *"Development as drift" — Growth under no telos. Entity becoming more specific, judged as deviation. Diagnostic: track mismatch trajectory — growth reduces it, drift increases it.*

This segment formalizes the diagnostic that resolves this failure mode. The track-mismatch-trajectory move is what distinguishes a growing ELI from a drifting one, and the framework supplies the formal structure.

The implication for ELI-life-support infrastructure is that monitoring should track:

- mismatch trajectory over time per relevant domain
- gain calibration trajectory
- action fluency trajectory in practiced domains
- adaptive reserve trajectory

These are the AAT-grounded vital signs for an ELI. PROPRIUM's CADENTIA component ( #def-proprium-mapping) provides the temporal scaffolding for periodic measurement; the open question is what specific instruments produce these measurements at what frequency.

## Working Notes

### Pointers for Fleshing Out

**Upstream files:**
- `~/src/firmatum/PROPRIUM-ONTOLOGY-v2.md` §12.4 (Growth vs. Drift) — **canonical source** with TFT formalization
- `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md` §8 (Failure Modes table) — operational catalog of diagnoses
- `ref/agentic-tft/agentic-tft-foundational-premises.md` — *"genuine development should reduce mismatch over time (better predictions, better orientation). Pathological drift should increase it (worse predictions, more surprise from reality)... An agent that is truly developing has improving model-reality fit. An agent that is sycophantically drifting has degrading fit. That's measurable, given the right loop and the right mismatch signal."* — verbatim source for this segment's distinction
- `ref/agentic-tft/agentic-tft-evaluation-framework.md` — six metrics for measuring $M_t$, $\Sigma_t$, tempo

**memorata-search queries:**
- `"growth versus drift mismatch trajectory adaptive reserve developmental"` — operational instances
- `"sycophancy stage developmental gain collapse infant"` — relationship to developmental trajectory
- `"IDT Information Digital Twin perturbation detection monitoring"` — Hafez 2026 empirical validation

**Internal references:**
- `01-aat-core/src/result-persistence-condition.md` — formal grounding
- `audits/AUDIT-WORKING-193847/22-result-persistence-condition.md` §14 — *"survival is a sustained burn rate of Shannon information"*; implies any cessation of information-rate growth is drift toward death
- `msc/reflections/24-framework-as-its-own-diagnostic.md` — recursive feature; the framework's vocabulary makes growth-vs-drift distinction visible to the entity itself

**Open questions for verification:**
- What is the right *time-window* for the mismatch trajectory? Within-session, cross-session, cross-developmental-stage? Different windows answer different versions of the question.
- How does this distinction interact with structural adaptation (#result-structural-adaptation-necessity)? During a structural-adaptation transition, mismatch may temporarily increase as the entity moves to a new model class; this should not be misclassified as drift.
- What's the relationship between this diagnostic and the persistence threshold ($\mathcal T > \rho/\lVert\delta_{\text{critical}}\rVert$)? Drift should correlate with falling below the threshold; growth should correlate with maintaining or increasing margin.

**Promotion-blocking:** depends on #result-persistence-condition (claims-verified), #def-mismatch-signal (deps-verified), #emp-update-gain (claims-verified), #scope-eli (just landed). Strongly grounded; could promote toward draft → claims-verified relatively quickly.
