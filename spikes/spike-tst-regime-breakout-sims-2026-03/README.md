# spike: TST regime-breakout simulations (2026-03; routed live 2026-07-16)

*The live half of the March-2026 TST simulation family (dead half: `spikes/.archived/`, MANIFEST-2026-07-16-tst-sims). Status: **unlanded knowledge, land-or-drop decision open** — the F2 verification (2026-07-16, refute-first challenged) confirmed the qualitative claim below is absent from canon and speaks directly to a gap canon itself flags (`#der-change-expectation-baseline` Working Notes: the finite$\to$unbounded velocity-inflection / compound-seeking investment question, "awaits proper formalization").*

## The unlanded claim (medium value, hypothesis/heuristic grade at best)

**Mortality-gated breakout:** under stochastic Lindy termination, compounding-tooling breakout becomes a race against project death — linear tooling cannot break out of a losing regime; success requires fast exponential compounding ($\beta_{\exp} \approx 3$–$5\%$) *and* survival luck. From `stochastic_regime_breakout.py` (1000 runs/cell, seed 42, hazard $1/(k+1)$ consistent with canon's Pareto(1) derivation). If judged canon-worthy: a discussion-grade/hypothesis segment in 02-tst-core, hazard tied to `#der-change-expectation-baseline`, with the ad-hoc model elements named as such (velocity $= \sqrt{0.1k}$, regime thresholds $0.8/1.2$, strategy fractions — all unmotivated; single seed).

## Load-bearing caveats (from the verification)

- **Hazard sensitivity:** `three_regimes_stochastic.py` uses an ad-hoc softened hazard $1/(k+5)$ (undeclared deviation from the derivation-consistent $1/(k+1)$) and its quantitative conclusions differ materially — the corpus never converged to a stable number. Treat *no* breakout percentage from either script as robust; only the qualitative shape is a landing candidate, jointly stated with this sensitivity.
- **No preserved run record:** results were stdout-only; the scripts' savefig paths point at a defunct tree. Any landing requires a fresh recorded run (per the `empirica/` RUNS contract) — do not transcribe numbers from memory or from this README.
