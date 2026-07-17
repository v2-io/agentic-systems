# .archived MANIFEST — 2026-07-16 TST simulation corpus (F2 disposition)

*The March-2026 `02-tst-core/simulations/` corpus, routed per the G2/F2 per-artifact verification (13 agents, refute-first challenge stage; full verdicts in the 2026-07-16 F2 cycle record, CHANGELOG). Content deliberately not canon — this bucket's truth-claim. The corpus's former README claimed a file reorganization ("moved to invalid_no_termination/") and five PNG outputs that never existed; this MANIFEST replaces it as the accurate routing record. No run outputs were ever preserved (scripts wrote to a defunct `~/planning/simulations/` path); results existed as stdout only. No canon claim cites or depends on any file here.*

## `lindy-tooling-sims-2026-03/` — one March-2026 exploration, six files

- `lindy_math_verification.py`, `lindy_corrected.py`, `lindy_stochastic.py`, `lindy_gaussian_start.py` — **superseded**: discrete Lindy hazard ($1/(k+1)$, $S(k) = 1/k$) + Monte-Carlo confirmation (20k runs, seed 42). Canon's `#der-change-expectation-baseline` (Jeffreys $\to$ Pareto(1), *exact*) is strictly stronger and corrects these sims' own headline framing — "$E[\text{additional}] \approx k$" is a truncation artifact ($\max_k = 500$); Pareto(1) has no mean; the median statement is the right one. Valid per the old README's triage; superseded by the analytic derivation.
- `lindy_simple.py`, `lindy_tooling.py` — **superseded + invalid** (old README's own triage: no termination model, mathematically invalid for Lindy analysis): the myopic $v^\ast = \sqrt{n\alpha}$ tooling-investment model, an abandoned early formalization; canon took the cleaner amortized-threshold route (`#der-change-investment`, `#der-dual-optimization`).
- Retained seeds (one WN line at `#der-change-expectation-baseline`): the discrete hazard convention; the $\sqrt{n\alpha}$ optimum. Both would need fresh derivation segments to land — never a citation to these files.

## `tst-regime-sims-2026-03/` — the dead half of the regime family

- `three_regimes.py` — **nothing-to-land**: deterministic $\beta/\gamma$ regime trichotomy largely built into its own exponential-complexity premise (illustrates its assumptions more than tests them); old README's triage: invalid (no termination).
- `regime_transitions.py` — **superseded** by `spikes/spike-tst-regime-breakout-sims-2026-03/stochastic_regime_breakout.py` (same $\beta_{\exp}$ sweep and strategies with the mortality model added; the successor's results materially revise its thresholds — the deterministic conclusions were mortality-blind).

The family's *live* half (the two stochastic-termination scripts, carrying the unlanded mortality-gated-breakout claim) is NOT here — it stays a live spike at `spikes/spike-tst-regime-breakout-sims-2026-03/` per its INDEX row.
