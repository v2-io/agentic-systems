# 59 - der-observability-dominance

Source: `01-aat-core/src/der-observability-dominance.md`

## First-pass understanding

This segment derives a strategy-layer version of the update-gain lesson: if a node or edge is effectively unobservable, the observation-noise term dominates and local edge updates freeze. Nominal confidence in a path is therefore not enough; the strategy remains epistemically alive only where the agent can observe enough intermediate outcomes to update the relevant edge beliefs.

The qualitative claim is solid and useful. The segment also distinguishes terminal plan-level learning from per-edge localization: if the intermediate node is unobservable, the agent may still learn that the whole plan fails, but it cannot identify which edge failed without additional structure.

## Diagram attempt

I represented observability as a switch between two learning geometries. With intermediate observation, the agent gets two local update loops. Without it, both edges collapse into a single terminal plan-level update: some learning remains, but diagnostic resolution is lost.

## Findings and watches

- F51 candidate: the discussion says an agent choosing between a strong-but-blind path and a weak-but-visible path should prefer the visible one. That is true for epistemic maintenance or long-run adaptivity, but not necessarily for the current value objective; high-stakes exploitation can rationally favor the blind path if expected value dominates information value.
- F52 candidate: "unobservable regions are absorbing" says frozen beliefs imply no mismatch signal and no reason to revise, but the later two-edge analysis says terminal plan-level aggregation can still reveal plan failure. The stronger claim should be narrowed to no local edge-level mismatch/localization signal.
- F53 candidate: the observability-investment tradeoff claims a positive improvement in `alpha_Sigma` whenever `theta_1 > 1/2` and experience is distributed similarly. This does not follow transparently from the displayed formulas: with similar counts, `min(1/(n_1+1), theta_1/(n_2+1))` is not obviously greater than `1/(n_Phi+1)`. The claim needs its counting convention and comparison baseline spelled out.
- Watch: `conf_obs(P)=conf(P)*obs(P)` is correctly labeled first-order; downstream claims should not treat it as derived.
- Watch: the discussion relies on `deriv-edge-credence-dynamics`, `hyp-communication-gain`, and a cross-component code-quality segment without declaring them as dependencies. That is acceptable as discussion if the formal burden stays in the local gain argument.

## Local verdict

The core dominance principle is robust: observability controls whether edge beliefs can move. The quantitative investment comparison and the normative "prefer visible" language need more careful scoping.
