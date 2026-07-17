# MANIFEST — track-b-nonlinear (empirica founding entry, 2026-07-16)

*The Section-I validation-simulation suite: nonlinear mismatch dynamics + adversarial coupling + six variants. Migrated from `spikes/track-b-nonlinear-sims/` at the F2 disposition after per-artifact verification (verdicts: landed / partially-landed, all knowledge self-contained in canon; the one canon transcription defect it surfaced — the Regime-3 stochastic column — was fixed against this corpus's records in the same cycle). Provenance: Track B of the 2026-03 simulation program; spike history under that name in `spikes/INDEX.md` and git.*

**Vivarium-rerun status: planned** — this is exactly the corpus Joseph intends to rerun in-vivia; on rerun, RUNS entries gain vivium references and this python corpus becomes provenance.

**Publication disposition:** the reproducibility supplement — external archival citable object (DOI) at publication, per `#obs-section-i-validation-simulations`'s standing commitment.

## Experiments and claims (tier; consumers)

| Piece | Claims (one line) | Tier | Consuming segments |
|---|---|---|---|
| `sim1_nonlinear_mismatch.py` | Single-agent AR(1) mismatch under 5 correction functions: steady states, convergence, persistence threshold, distributions | empirical (validation of derived results) | `#obs-section-i-validation-simulations` |
| `sim2_adversarial_coupling.py` | Two-agent adversarial coupling; measured exponent $\approx 1.05$ — a non-coupling-dominant Model-S regime measurement, later diagnosed by the variants | empirical | `#obs-section-i-validation-simulations`, `#result-adversarial-exponent-regimes` (WN) |
| `variants/variant_ab_drift.py` (+ `variant_ab_results.md`) | Coupling as deterministic drift recovers $b \to 2.000$; drift-noise interpolation via $f = \mu/(\mu+\sigma)$ | empirical (validates derived $b=2$) | `#result-adversarial-exponent-regimes` |
| `variants/variant_cd_regimes.py` (+ `variant_cd_results.md`) | Stochastic AR(1) coupling asymptotes at $b = 3/2$, never 2 — forced the Model D / Model S split; root cause derived in-file | empirical (validates derived $b=3/2$) | `#result-adversarial-exponent-regimes` |
| `variants/variant_ef_extensions.py` (+ `variant_ef_results.md`) | E: observation noise collapses adversarial exponent; Riccati gain partially restores (52% mismatch reduction). F: per-dimension AR(1) exact to 4 sig figs; scalar condition overestimates by 72%; targeted attack +17% | empirical | `#obs-gated-tempo-advantage`, `#result-per-dimension-persistence`, `#obs-section-i-validation-simulations` |
| `variants/variant_causal_ib.py` (+ results md) | Greedy $\lambda = 0$: 0% survival (gain collapse); Lyapunov-bounded $\lambda \propto U_M/(R - R^\ast)$ survives with reward 92.08 | empirical (validates `#deriv-causal-ib-exploration`) | `#deriv-causal-ib-exploration`; `#deriv-causal-ib-lmi` (queued 2D generalization) |
| `variants/variant_hafez_bridge.py` (+ results md) | Hafez bi-predictability $P$ measures coupling architecture (scale-invariant, $P \approx 0.268$ across 10:1 tempo range) while mismatch measures performance (0.54→5.95) | empirical | `#obs-section-i-validation-simulations` §Hafez bridge |

Consumers cite this entry as `empirica:track-b-nonlinear`; per the bidirectionality contract, their Working-Notes paths were updated to this home at migration.
