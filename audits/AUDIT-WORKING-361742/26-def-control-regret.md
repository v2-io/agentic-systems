# Reflection: def-control-regret

**Segment:** `#def-control-regret`

## What this does

δ_regret = A_O(M_t; Π, N_h) - V_O(M_t, π_current; N_h) ≥ 0

Always non-negative. Measures: could I do better right now with a different strategy?

The 2×2 diagnostic:
- δ_sat ≤ 0 + δ_regret ≈ 0 → Success
- δ_sat > 0 + δ_regret ≈ 0 → Capability limit (optimally pursuing unmet goal)
- δ_sat ≤ 0 + δ_regret >> 0 → Strategy problem
- δ_sat > 0 + δ_regret >> 0 → Both (strategy first, then reassess)

## Naming relevance

Row 139: "control regret" — already voted keep +2. This segment fully confirms.

The RL "regret" baggage is intentional and correct: control regret is precisely the RL regret concept (gap between current and optimal policy) applied in AAD's framework. The "control" prefix distinguishes it from other regret concepts (epistemological regret, decision regret).

## Key insight confirmed

"Regret approaching zero when optimally failing" is the key motivation for the two-gap split. A single δ_objective would conflate "bad strategy for achievable goal" (fix strategy) with "good strategy for infeasible goal" (fix goal). The split makes this distinction operational.

Convention hierarchy for δ_regret is OPPOSITE to δ_sat monotonicity direction: δ_regret^(1) ≤ δ_regret^RH ≤ δ_regret^B (C1 reveals least regret, C3 reveals most). This is correctly asymmetric — the two diagnostic quantities have different convention-monotonicity directions.
