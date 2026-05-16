# 65 - form-strategy-complexity-cost

Source: `01-aat-core/src/form-strategy-complexity-cost.md`

## First-pass understanding

This segment gives the strategy DAG an MDL/IB-style maintenance cost and connects complexity to strategic persistence. The strongest technical thread is the maximum useful depth bound: deep AND-chains become unmaintainable because downstream edge evidence is geometrically starved while each extra node adds description length and confidence decay.

The KL-direction argument is locally coherent under deterministic `pi*`: `D_KL(pi* || Q_Sigma)` remains finite when the strategy assigns nonzero mass to the optimum, while the opposite direction is infinite whenever `Q_Sigma` explores off-optimal actions. The full uniqueness and compression-operation story depends on later proof homes and meta-segments that remain unread in this pass.

## Diagram attempt

I focused the diagram on the depth-bound check because it exposes a concrete arithmetic issue. The per-edge persistence test says even `d=1` fails when `nu/(n+1) <= rho/R`; under the table's `n=100`, `rho/R=0.01`, `nu=1` example, `1/101 < 0.01`, so the listed depth `5` cannot satisfy the displayed condition.

## Findings and watches

- F69 candidate: the quantitative illustration table appears wrong for `theta=0.8`, `nu=1`, `n=100`, `rho_Sigma/R_Sigma=0.01`. The condition for `d=1` is `1/(100+1) > 0.01`, but `0.009900... < 0.01`, so even a single edge fails and `d*` should be `0`, not `5`.
- F70 candidate: `C_revise` is defined as proportional to `sum nu_ij c_update`, but the prose says it is proportional to strategic tempo times per-update cost. Processing cost scales with raw update opportunities `nu_ij`; strategic tempo discounts by gain and identifiability. Those are different quantities unless the intended cost is cost per useful correction rather than per processed observation.
- F71 candidate: the segment's IB/KL uniqueness and regret-bound claims rely heavily on `disc-compression-operations` and `deriv-strategy-cost-regret-bound`, which are not declared dependencies. That may be deliberate appendix deferral, but they are warrant-bearing for the strengthened KL-direction and uniqueness story.
- Watch: the deterministic-`pi*` regret bound needs support condition `Q_Sigma(a*) > 0`; the segment says this, and downstream optimization should preserve it.
- Watch: the DL cost model treats precise learned credences as more expensive over time. That is plausible for explicit numeric storage, but agents may compress converged edges into qualitative defaults; the working notes gesture at this and should remain attached to any practical cost claim.

## Local verdict

The segment is conceptually rich and mostly well-scoped, but the depth table needs correction and the cost decomposition should separate observation-processing cost from useful-correction throughput.
