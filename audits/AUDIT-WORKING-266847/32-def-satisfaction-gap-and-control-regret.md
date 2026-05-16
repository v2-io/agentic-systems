# Reflection: def-satisfaction-gap and def-control-regret

## What the segments do

Two linked definitions that together form the 2×2 diagnostic system:

- Satisfaction gap δ_sat = V_O_min - A_O(M_t; Π, N_h): "can I achieve the goal from here?"
- Control regret δ_regret = A_O - V_O(M_t, π_current; N_h): "could I do better right now?"

The 2×2 table:
| | δ_sat ≤ 0 (attainable) | δ_sat > 0 (unmet) |
|---|---|---|
| δ_regret ≈ 0 (near-optimal) | Success | Capability limit → check M_t, Π, N_h, then O_t |
| δ_regret >> 0 (suboptimal) | Strategy problem → revise Σ_t | Both → revise Σ_t first, then reassess δ_sat |

## The key insight: orthogonal diagnostics

The previous formulation used a single δ_objective, which conflated "bad strategy" with "impossible goal." The split into satisfaction gap and control regret is the repair that makes the orient cascade actionable: each 2×2 cell prescribes a different corrective action.

The "regret approaching zero when optimally failing" observation is the crux: a single diagnostic shows "large gap" for both "bad strategy, achievable goal" AND "good strategy, impossible goal." Without the split, you can't distinguish them.

## The Active Inference contrast

The contrast with active inference's expected-free-energy (EFE) decomposition is important: AI's pragmatic + epistemic split supports policy ranking but doesn't separate "goal too hard" from "strategy too weak." Both increase EFE without distinguishing cause. AAD's split depends on V_{O_t} being a *value functional on trajectories*, not log-priors over outcomes (which would collapse the diagnostic, as Sun & Firestone 2020 argue about AI's preferences-as-priors form).

The dark-room critique (Sun & Firestone) diagnoses the preferences-as-priors collapse; AAD's value-functional reformulation is the architectural response to that diagnosis. This is a clean prior-art integration: cite the problem, name the fix.

## Convention dependence

Both diagnostics are convention-relative: δ_sat^B ≤ δ_sat^RH ≤ δ_sat^(1) (C1 most conservative, C3 strongest). The regret ordering reverses: δ_regret^(1) ≤ δ_regret^RH ≤ δ_regret^B (C3 reveals largest regret). Convention choice is part of the measurement, not the agent's architecture.

## Naming targets

"Satisfaction gap" and "control regret" are the two segment names. Both are likely in the tracker with several alternatives. "Objective attainability" A_O is also a named concept.

Looking at tracker rows 377 and 157 (already found earlier).

## Wandering thoughts

The disambiguation table in def-satisfaction-gap is genuinely load-bearing. It encodes the diagnostic procedure: check M_t first (epistemic update before attainability evaluation — this is why the orient cascade puts epistemic update first), then check Π and N_h, then consider revising O_t. Objective revision is the last resort. This is an architectural principle embedded in the diagnostic table.

The working note about V_O_min (the satisfaction threshold) being a property of the objective, not the agent: for utility-maximizing objectives, "good enough" threshold may need explicit modeling. This is an open problem — satisfaction gap is well-defined only when V_O_min exists.

How valuable: 10/10 for load-bearing (the two-gap system is Section II's primary diagnostic contribution), 9/10 for surprise (the 2×2 cellular structure and the AI contrast are both cleaner than I expected).
