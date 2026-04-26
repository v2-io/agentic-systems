# Reflection 21 — result-sector-persistence-template (Appendix A; cited from rows 25, 26)

The template that the framework's persistence-flavored results instantiate. Last cited appendix from the main-section walk.

## §4.2 dependency check

`depends: [deriv-sector-condition]`. Upstream (just read). **No backward-dep finding.**

## §4.4 prompts walk-through

**1. Predictions vs evidence.** Predicted: "abstract template for sector-persistence with state variable / correction function / disturbance model; six instantiations CLAUDE-2.md flagged." Verification: ✓ exactly. Six instantiations listed:
- result-persistence-condition (epistemic mismatch $\delta$)
- schema-strategy-persistence (strategic mismatch $\delta_\Sigma$)
- der-team-persistence (sub-agent mismatch $\delta_i$)
- form-composition-closure (trajectory error $e_m$)
- der-tempo-composition (composite mismatch $\delta_c$)
- der-adversarial-destabilization (target-agent mismatch $\delta_B$)

Plus #deriv-critical-mass-composition referenced as a closed-form variant.

**2. Cross-segment consistency.** Multiple recently-added pieces (per CLAUDE-2.md priming) propagate here:
- Monotone-operator lineage (Rockafellar 1970, Bauschke-Combettes 2017): "External mathematical lineage" subsection acknowledging AAD as specialization, with five distinctives named.
- FEP-flow comparison (Friston 2019/2023, Aguilera 2022): "Comparison with FEP-flow" subsection positions AAD's Lyapunov approach as broader-validity alternative.
- Information-rate floor (deriv-persistence-cost): "Cost complement" subsection.
- Contraction-template generalization to non-Euclidean metrics (result-contraction-template): "(CT2) at $M=I$ equivalent to DA2'-inc" — the structural-transparency lift.

All propagate cleanly. ✓

**3. Math verification (at discretion).** The template's mathematical content is mostly inherited from deriv-sector-condition (already verified). The new content is the parameter-free formulation and the direct-substitution claim that proofs transfer. I'll skip recomputation — Joseph's "spot-check at discretion" framing applies; this segment is organizational over computational.

**4. What direction next?** Returning to OUTLINE walk at row 27 = result-structural-adaptation-necessity. Excitement: the structural-adaptation trigger formalized — when does parametric adaptation fail? Disappointment: if the trigger is hand-waved without geometric content. Per CLAUDE-2.md priming, this is one of the inevitability-core segments, so I expect a sharp result.

**5. What errors should I now watch for?**
- Future segments invoking the template without verifying (T1)–(T3) for their specific instantiation. Schema-strategy-persistence is honest about $\alpha_\Sigma$ time-variation; other instantiations may not be.
- The template's "exact" status presupposes (T1)–(T3) hold. Downstream that uses the template's bound without acknowledging the conditional nature = finding.
- Conflation of Euclidean sector (T2) with non-Euclidean contraction (CT2) when the natural coordinate is non-Euclidean.

**6. Predictions for next segments.** Row 27 = `result-structural-adaptation-necessity`. status:claims-verified per OUTLINE. Probably depends [def-model-class-fitness, def-mismatch-signal, result-sector-condition-stability]. Per priming: "when class fitness $\mathcal F(\mathcal M) < 1 - \varepsilon$, no parametric update closes mismatch floor; structural change required."

**7. What would I change?** The "External mathematical lineage" and "Comparison with FEP-flow" subsections are substantial positioning content that sits a bit awkwardly with the template's abstract core. Could be moved to a positioning segment. But they're substantive and worth keeping — judgment call. The 6-row instantiation table is exemplary pedagogy.

**8. What am I now curious about?**

(a) The **signed-coupling pattern across instantiations**: every effective $\rho_\xi$ is "environmental disturbance + cross-agent contribution with sign encoding cooperative vs adversarial coupling." Team-persistence, composition-closure, tempo-composition, adversarial-destabilization, composite-critical-mass — *all* instances of this signed-coupling structure. This is a meta-pattern *within* the template's instantiations. Could be elevated as a meta-segment ("signed coupling as Section III's organizing principle"). **Section D candidate.**

(b) **$\alpha_\Sigma = 1/(n+1)$ decays with experience.** Schema-strategy-persistence requires experience discounting at rate $(1-\lambda) > \rho_\Sigma/R_\Sigma$ to recover constant-$\alpha$. This is non-trivial: agents accumulating experience without discounting eventually fall below the strategy-revision persistence threshold. Connects to gain-collapse / stability-induced myopia / detection-latency-blowup — multiple threads converging on "experience discounting / forgetting / consolidation as architectural primitive." **Section D candidate.**

(c) **Brooks's Law as a template instance.** "Adding agents increases $\sum_i \mathcal T_i$ but may increase $\varepsilon^* \nu_c$ faster, pushing $\rho_c^{\text{eff}}$ above $\alpha_c R_c$." Beautiful unification of an engineering observation with the framework's machinery — Brooks's Law is the persistence-condition-violation regime for the composition-closure instantiation.

(d) The **AAD-vs-FEP-flow comparison** — explicit, naming the Aguilera 2022 "FEP-flow narrow parameter regime" critique and arguing AAD's Lyapunov approach has broader validity. This is a strong positioning move. Worth verifying when I do citation spot-checks: does Aguilera 2022 actually say what AAD claims (FEP-flow validity narrow)? CLAUDE-2.md says it does ("Aguilera 2022 FEP-narrow-validity claim exactly matches AAD's usage"), based on prior citation audit. So this should hold.

(e) The "1-anchor anchoring at the equilibrium" framing for AAD's specialization of monotone-operator theory: AAD's sector condition is one-point at the target, not full two-point monotonicity. This admits agent classes (PID-bounded-plant, variational-approximate) where full monotonicity fails but persistence-at-the-target is available. Useful structural observation.

**9. What new knowledge enabled.** Six AAD persistence-flavored results unified as one template. Clear specification of what each instantiation must verify. Recognition of monotone-operator-theory lineage with AAD-distinctive content named explicitly. FEP-flow comparison positions AAD as broader-validity alternative. Information-rate cost as parametric follow-on.

**10. Should the audit process change?** Reading the cited appendices in-context per the §4.2 exception was the right move — I now have a much firmer grasp of the framework's persistence machinery than strict OUTLINE-walk would have produced. Returning to OUTLINE walk now (row 27).

**11. Outline updates.** Section E (calibration): substantial confirmation of the framework's persistence machinery. Three Section D (bigger-picture pondering) candidates surfaced this round:
- Signed-coupling pattern as Section III's organizing principle.
- Experience discounting / forgetting / consolidation as architectural primitive across multiple convergent threads.
- The "expected-value bridge + stochastic-disturbance composition" meta-pattern.

## Status-label / discipline

`status: exact` defended carefully — exact at the template level; instantiations inherit conditionally on their (T1)-(T3) verification. `stage: draft` — substantial content; Gate 1/2 may not have re-run since recent additions.

## Cadence check

All cited appendices read. Returning to OUTLINE walk. Next: Section I row 27 = `result-structural-adaptation-necessity`.
