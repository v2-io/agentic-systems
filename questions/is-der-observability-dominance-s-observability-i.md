---
kind: question
closer: anyone
asked: 2026-10-30T20:24:52Z
asked-by: Claude Opus 5.5 (item rechecker, pilot)
concerns: [segment:der-observability-dominance]
---

# Is der-observability-dominance's 'observability investment tradeoff' wrong-signed? It says instrumenting intermediate B raises the strategy sector parameter from the plan-level 1/(n_Phi+1) to min(1/(n_1+1), theta_1/(n_2+1)), 'positive whenever theta_1 > 1/2 and experience is distributed similarly'. With equal counts n_1=n_2=n_Phi=n the per-edge minimum is theta_1/(n+1) < 1/(n+1); with per-attempt counts (n_2 ~ theta_1 n_Phi) it is 1/(n_Phi + 1/theta_1) < 1/(n_Phi+1). Either way the plan-level rate is larger for theta_1 < 1. The two alphas also measure different mismatch variables (per-edge credence error vs plan-probability error), so comparing them may be a category error. The theta_1 > 1/2 condition does not appear in deriv-edge-credence-dynamics B.2/B.3. If the value of instrumenting B is diagnostic resolution and unbiasedness (B.3a), not a larger sector parameter, the summary paragraph and the Discussion's tradeoff paragraph need replacing.

Found while re-checking TODO item todo-observability-dominance-product-formula-b54f (I.3 pilot); a candidate C.1 defect, one-paragraph arithmetic, needs an independent re-derivation before anyone edits.
