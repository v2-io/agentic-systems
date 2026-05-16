# Batch 16 Reflection — Triage mode (deferred appendices + TST/logogenic samples)

**Segments covered:**
- `deriv-graph-structure-uniqueness` (Appendix A, stage: claims-verified, first 120 lines)
- `result-sector-persistence-template` (Appendix A, stage: draft, full)
- `post-temporal-optimality` (TST sample, stage: deps-verified)
- `result-section-ii-survival` (logogenic sample, stage: draft, first 60 lines)

---

## Key findings from this batch

**`deriv-graph-structure-uniqueness` — verified structure:**

The derivation establishes:
- P1 (directed temporal ordering) + finite horizon → acyclicity (exact, analogous to the chronica argument from Section I)
- P2 (Cox's theorem) → probabilistic edges
- P1 + P2 + causal sufficiency → CMC theorem → Markov factorization (exact conditional)
- P3 (local revisability) follows as a *consequence* of the CMC, not an independent postulate

The segment is honest about the sufficiency-not-necessity gap: "No non-DAG structure has been shown incapable of satisfying P1-P4; the necessity direction is open." This is a Cox parallel in form, not strength. The CMC theorem citation (Spirtes-Glymour-Scheines 2000, Pearl 2009) is correct and appropriate.

Status: `claims-verified` — the most advanced stage of any segment I've read. The claims appear well-verified. **No finding here.**

**`result-sector-persistence-template` — the abstract template:**

The six instantiations table (epistemic mismatch, strategic mismatch, sub-agent mismatch, trajectory error, composite mismatch, target-agent mismatch) cleanly summarizes how the single Lyapunov argument applies across all persistence-flavored results. The Model D ($1/\alpha$) vs Model S ($1/\sqrt{\alpha}$) scaling propagation to adversarial exponents $b=2$ vs $b=3/2$ is explicit.

The comparison with active inference's NESS-density argument is the most interesting content: AAD's sector-Lyapunov is broader (checked locally, not requiring NESS structure) and gives explicit ultimate-bound formulas. This is a genuine structural advantage.

**TST sample (`post-temporal-optimality`):** Clean and appropriate — similar quality to AAD foundational definitions. The equivalence precondition is correctly labeled as load-bearing. TST appears to maintain the same epistemic discipline as AAD.

**Logogenic sample (`result-section-ii-survival`):** The survival classification (16/24 exact, 5 approximate, 2 modify, 1 fails) is being derived by segment-by-segment analysis, which is the right approach. The GUC rename warning is present. `stage: draft` is appropriate given the ongoing work.

---

## Overall assessment at triage point

**Scope covered:** ~97 segments read (~65% of existing segments):
- Section I: complete (29 segments + 5 appendix)
- Section II: complete (29 segments + 5 appendix)
- Section III: ~16/21 segments (missing: der-adversarial-destabilization, der-interaction-channel-classification, deriv-strategic-composition, der-agent-opacity, obs-gated-tempo-advantage)
- Appendices: ~12/33 (key ones: deriv-sector-condition ✓, deriv-recursive-update ✓, deriv-edge-credence-dynamics ✓, deriv-edge-update-natural-parameter ✓, deriv-graph-structure-uniqueness ✓, result-sector-persistence-template ✓)
- TST: 1/25 (sample — post-temporal-optimality)
- Logogenic: 1/13 (sample — result-section-ii-survival)
- ELI: 0/14

**Summary findings:**
1. **Confirmed finding:** Prop B.4 optimal exploration rate has subscript transposition (medium severity — affects unequal-experience OR-node quantitative claims)
2. **Verified correct:** Adversarial scaling exponents b=2 (Model D) and b=3/2 (Model S) — analytically derived and simulation-confirmed
3. **Verified correct:** Recursive update uniqueness (Doob-Dynkin), mismatch decomposition, gain formula (Kalman), sector-condition (Lyapunov), persistence condition (both models), orient cascade ordering
4. **Minor observation:** Multiple mature appendix segments at `stage: draft` (deriv-recursive-update, deriv-sector-condition, der-gain-sector-bridge, etc.)
5. **Low-severity concerns:** scope-agency missing dep on def-pearl-causal-hierarchy; post-composition-consistency citing appendix without declaring dep; form-objective-functional `status: axiomatic` overstates for a formulation with substantive commitment

**Overall quality assessment:** Section I is mathematically rigorous and complete. Section II is architecturally sophisticated with one confirmed math error. Section III has strong results in adversarial dynamics (verified) and composition machinery (conditionally complete — bridge lemma requires DA2'-inc). TST and logogenic appear to maintain the same epistemic discipline. The framework's most distinctive contributions (persistence condition with two-condition decomposition, survival classification, adversarial squared-law, forgetting prerequisite) are all sound.

---

## Transition to report writing

Writing the final report now. All confirmed findings and key verifications are documented in the batch reflections.
