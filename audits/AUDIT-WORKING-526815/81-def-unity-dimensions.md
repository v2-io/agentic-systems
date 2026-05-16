# 81 - def-unity-dimensions

Source: `01-aat-core/src/def-unity-dimensions.md`

## First-pass understanding

This segment defines composition quality along two axes: content unity and update-rule homogeneity. The content axis tracks shared model, objective, strategy, and observations; the structural axis `U_f` tracks whether sub-agents update in the same way. The useful conceptual correction is that shared content alone is not enough: identical beliefs can still diverge under different update rules.

The scope discipline is good. The segment explicitly says unity metrics are quality parameters conditional on `scope-composite-agent`, not a universal scalar gate for composite status. The main problems are metric-level: several proposed formulas are sketches, and `U_M` as written does not have the stated range.

## Diagram attempt

I drew closure defect as a rate-distortion surface controlled by two independent-ish inputs: content unity and structural homogeneity. The diagram marks the normalization warning on the content side, because bad metric normalization would make the surface misleading before any later derivation begins.

## Findings and watches

- F146 candidate: the epistemic-unity formula `U_M = I(M1;...;Mn) / H(M1,...,Mn)` is not normalized as claimed. If all `n` variables are identical with entropy `H`, total correlation is `(n-1)H` and joint entropy is `H`, so the ratio is `n-1`, not `1`. The metric needs a different normalization or a capped/rescaled redundancy measure.
- F147 candidate: teleological unity as pairwise correlation of value functions over encountered trajectories is distribution- and policy-dependent, can be undefined for zero-variance value functions, and may miss group-level/nontransitive alignment. It needs support, variance, and aggregation conventions.
- F148 candidate: the strategic-unity formula `1 - KL(pi_actual || pi_optimal) / KL(pi_independent || pi_optimal)` needs support and denominator conditions. The denominator can be zero, KL can be infinite, and the result can be negative or otherwise leave `[0,1]` without clipping or a bounded divergence.
- F149 soft candidate: `U_obs` is described as the fraction of observation information reaching all sub-agents, but many useful composites rely on complementary private observations plus sufficient routing, not identical broadcast. The metric should distinguish common observation, routed observation, and synergistic private observation.
- F150 soft candidate: `U_f = 1 - d(f_M^1,...,f_M^n)` assumes a normalized distance `d in [0,1]`, but the candidate operator/Fisher/IB distances do not automatically share that range or interpretation. The normalization is part of the definition, not a detail.
- Watch: the two-axis content/structure distinction is valuable and appears motivated by the heterogeneous-Kalman case, but proof credit is deferred to `result-unity-closure-mapping`.

## Local verdict

The conceptual taxonomy is useful; the metrics need formal repair before they can carry quantitative claims. `U_M` in particular is mathematically wrong under the stated boundary condition.
