# 34 — disc-identifiability-floor (M1, boundary facet)

*Type: discussion. Status: discussion-grade. Stage: draft. Depends: [der-causal-insufficiency-detection, deriv-edge-credence-dynamics, der-causal-hierarchy-requirement, der-loop-interventional-access, der-architecture-noidentifiability].*

## Predictions vs evidence
Predicted: M1 with four floor instances + Sylvester rank-collapse argument. Found: that, plus a clearly-articulated five-element methodology shape (Setting → External Theorem → No-go → Boundary characterization → Strengthened consequence) + sister-cluster split into `#disc-value-functional-grounding-floor` and `#disc-implementation-impossibility` per actor-positioning.

## **Math verification**

Sylvester's law of inertia argument (lines 161-165): Fisher information reparameterization is congruence $\mathcal{G}_\varphi = S^T \mathcal{G}_\theta S$ for invertible $S$. Sylvester's law: congruence preserves inertia (number of positive/zero/negative eigenvalues invariant under congruence). Therefore rank-deficient Fisher is rank-deficient in every reparameterization. Escape requires rank-augmentation (new information), not re-mapping. **Mathematically sound.** ✓

Instance 2's Fisher rank-1 factorization $\mathcal{F} = uu^T/(\mu_j(1-\mu_j))$ — to verify when I reach `#deriv-edge-credence-dynamics` Prop B.7 in Appendix A.

Instance 3's symmetric-matched-Tier-1-scalar coupling-sign witness: cross-term $\gamma \mathcal{T} \cdot \text{sign}(\delta_{\bar i})$ is absorbed into total disturbance bound $\rho + |\gamma|\mathcal{T}$ regardless of sign → identical marginals → composite-level sign distinguishes them. Valid construction. ✓

Instance 4's similarity-fiber argument: $F' = TFT^{-1}$ for invertible $T \in GL(n)$; stationary covariance $\Pi' = T\Pi T^T$ (congruence); eigenvalues similarity-invariant; innovation spectrum $\det(i\omega I - F)$ similarity-invariant. Standard Kalman-Ho realization theory. ✓

## Prose-coherence — strong

- The five-element methodology shape (lines 16-22) is clean and reusable.
- Sister-cluster split with actor-positioning argument (lines 139-145): agent-frustrated vs principal-frustrated vs designer-frustrated. Methodologically precise.
- Naming-pattern discipline at slug depth: agent-side capacity-on-the-agent → `*-floor*`; designer-side task-of-the-designer → `*-impossibility*`.

## Findings (line 176+)

Two Findings:
1. **The Identifiability Floor as Cross-Cutting Meta-Pattern** — detective-analog Brief: "you cannot survey your way out of a blind spot by changing the units on the ruler; you have to look from a new vantage point." Decent Feynman-criterion target.
2. **The Rank-Collapse Floor's Irreducibility is Sylvester's Law of Inertia** — the same ruler-versus-vantage-point analog with sharpened mechanism. Sylvester 1852, Horn-Johnson Thm 4.5.8, Lehmann-Casella §2.5 cited as formal antecedents.

Novelty claims: *recognition* + *differentiation* — properly tiered. Aligned with `feedback_math_novelty_recognition.md` discipline.

## **Citation-honesty observation (worth noting positively in §E)**

Lines 230-236 explicitly name a *primary-source verification spike queued* for the BG2 second-pass Undermind citations (Mertikopoulos-Papadimitriou-Piliouras 2017, Bichler et al. 2025, Legacci-Mertikopoulos-Pradelski 2024, Pangallo et al. 2017, Anagnostides et al. 2022, Shi-Zhang 2019). Footnote `[^bg2-2026-05-21]` appended to each unverified citation. The softened "primary AAT-framework" qualifier in strengthened consequence #4 explicitly rests on this verdict.

This is exemplary citation-discipline:
- Mark citations not yet primary-verified.
- Explicitly name what claim hinges on the unverified citation.
- Queue verification with priority order.
- Soften the load-bearing claim in advance pending verification.

**Worth highlighting in §E as a model of citation honesty.**

## Cross-segment consistency
Forward-refs `#disc-stability-certificate` (the spine), `#disc-separability-pattern`, `#disc-additive-coordinate-forcing`, `#disc-value-functional-grounding-floor`, `#disc-implementation-impossibility`, `#disc-constructive-impossibility-posture`, `#disc-dynamic-regime-axis`, `#deriv-regime-marginal-indistinguishability`, plus all four instance segments. Coherent.

## Watch list
- Instance 3's broadening to coupling-topology bit (R0/R1/R2 regimes) is 2026-05-21 work. The escape (e) composite-level rate-class observation is the new structural escape. Working Notes records the integration-is-replacement landing of the 6th-instance candidate as the broadening. Good provenance.

## Next-segment predictions
`#disc-value-functional-grounding-floor`. M1's agent-side sister cluster. Two charter instances: Result G′ via `#deriv-self-actuation-grounding` (within-model) and Cohen-2022-strengthened via `#deriv-reward-channel-learning-no-go` (across-model).

## Brief wandering

**On the methodology-as-organizing-principle-not-generative-principle (Working Notes line 221).** The honest historical narrative is convergent: Instance 1 + 2 derived first; methodology shape recognized after both; Instance 3 + 4 added with the methodology in mind. The framework is honest about not claiming the methodology was generative from the start. Good record.

**On Instance 4's Sylvester-at-one-remove distinction.** The *generating* group action is state-space similarity $T(\cdot)T^{-1}$ — not metric congruence $S^T(\cdot)S$ that Sylvester governs. But the agent's *escape-side* freedom (reparameterization of observation model) still acts by congruence on the observed Fisher. So Sylvester preserves the inertia-on-escape-side. This is precision about *what* the Sylvester argument actually rules out (re-mapping the escape coordinate) vs what it doesn't (the generating similarity orbit on the realization manifold).

**On the discipline of softening claims pending verification.** The "primary AAT-framework" softening (vs "unique broadly-available") at strengthened consequence #4 is the kind of pre-emptive soften that lets the load-bearing claim survive if verification reveals nuance. Strong move.
