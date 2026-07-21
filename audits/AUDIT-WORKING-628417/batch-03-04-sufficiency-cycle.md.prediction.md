# Prediction: batch-03-04-sufficiency-cycle.md
*Pre-compact; ~3.6KB. High plausibility — cycle is the Part I engine I still "know" conceptually from spine + appendices.*

# Batches 03–04 — Sufficiency, Fitness, Cycle

Segments: model-class fitness / sufficiency, cycle, events, recursive update (+deriv appendix), action selection, mismatch signal, mismatch decomposition, update gain.

## Core claims
- Fitness of model class ℱ(ℳ); structural adaptation when class unfit (not more gain).
- Event-driven cycle: observation → mismatch δ → update with gain η → action.
- Recursive update forced (no free one-shot global recompute of M from full C each time).
- Mismatch decomposition (internal/external / mechanism pieces — details fuzzy).
- Optimal gain η* ~ U_M / (U_M + U_o) uncertainty-ratio form (Kalman-like).

## Surprises
- Recursive-update appendix as early exactness island.
- Gain as structural object, not hyperparameter.
- "You cannot outrun bad U_o" seed.

## Wandering
- Decomposition coordinates will matter for later floors and residual diagnostics.
