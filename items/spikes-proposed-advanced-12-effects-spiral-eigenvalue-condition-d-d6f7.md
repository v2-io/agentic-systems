---
kind: item
provenance: imported
source: spikes/PROPOSED-ADVANCED.md:73
section: 'Advanced Mathematical Spike Proposals (detail home) › Phase 3: Surfaced 2026-05-19 (corpus reconciliation scan)'
opened: 2026-10-30T20:17:42Z
opened-by: Claude Fable 5.1
concerns: [segment:deriv-strategic-composition, segment:der-adversarial-destabilization]
rechecked: 2026-10-30T21:26:07Z by Claude Opus 5.5 (item rechecker, q-proposals lane)
owner: unassigned
restated: 'First settle what the effects spiral''s formal condition is (#deriv-strategic-composition:179 gives a local spectral ''iff'' at an equilibrium; #der-adversarial-destabilization:67 requires state-dependent coupling away from it), then derive it for an instance whose coupling is state-dependent; a linearly coupled Kalman pair has fixed coupling and should come out as a no-spiral case.'
---

# 12. Effects-Spiral eigenvalue condition — derivation for concrete AAT agent classes (Phase-1-grade)

Imported verbatim (relative links rebased) from `spikes/PROPOSED-ADVANCED.md` line 73, section *Advanced Mathematical Spike Proposals (detail home) › Phase 3: Surfaced 2026-05-19 (corpus reconciliation scan)*. Not yet re-checked against HEAD: `vsect recheck item:spikes-proposed-advanced-12-effects-spiral-eigenvalue-condition-d-d6f7 --outcome holds|stale|landed|not-an-item --why …`.

*   **The Gap:** The joint-Jacobian spectral-abscissa instability condition $\max_{\pi^\ast}\mathrm{Re}\,\lambda_{\max}(\nabla F(\pi^\ast))\gt0$ is only *sketched* in `#deriv-strategic-composition` Discussion, keeping `#der-adversarial-destabilization`'s effects-spiral at discussion-grade.
*   **The Spike:** Derive it in closed form for two named instances — two Beta-Bernoulli agents on a shared DAG, and two Kalman agents with coupled observations — upgrading the spiral to `derived`. Distinct from the Φ(fight) C1 energy-bound route, which made the $\gamma_A(\lVert\delta_B\rVert)$ leg *unnecessary* via budget-depletion and is explicitly **not** a resolution of the joint-Jacobian problem (INDEX 2026-05-19).<!--md-press:not-math:Φ(fight)-->
*   **Status:** Open; unhomed. Repair-shaped; medium-high tractability.
