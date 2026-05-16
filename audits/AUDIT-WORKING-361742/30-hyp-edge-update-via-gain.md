# Reflection: hyp-edge-update-via-gain

**Segment:** `#hyp-edge-update-via-gain`

## What this does

Extends the uncertainty-ratio gain principle (emp-update-gain) from M_t epistemic updates to strategy-edge updates. Edge credences p_ij update via:

p_ij_new = p_ij_old + η_edge · (signal(o_t, i, j) - p_ij_old)

where η_edge = U_edge / (U_edge + U_obs) — same structure as the M_t gain, applied to edges.

Key distinction: the Beta-Bernoulli gain 1/(n+1) is derived from CONJUGATE analysis, not from literal substitution of the variance-ratio formula. The uncertainty-ratio formula is a structural PRINCIPLE (conservative updating proportional to relative uncertainty), not a universal algebraic formula. The Beta-Bernoulli case satisfies the principle but derives it differently.

Log-odds representation: λ_ij_new = λ_ij_old + ℓ(y), where ℓ(y) is the per-observation log-likelihood ratio. Log-odds is the unique parameterization on which independent-evidence accumulation is additive (forced by evidential-additivity axiom from deriv-edge-update-natural-parameter).

Status: Hypothesis. The signal function is now characterized at theory level by disc-credit-assignment-boundary:
- Persistence does NOT require per-edge credit assignment (Prop B.5)
- Any signal function with directional fidelity suffices for persistence
- Exact attribution is #P-hard in general
- Gradient-based signal_k satisfies directional fidelity for monotone DAGs

## Naming relevance

**Row 357 (edge update via gain)**: The segment fully confirms the name. "Via gain" is the mechanism — the hypothesis IS about extending the gain principle. The name accurately frames what's hypothesized: applying the gain mechanism to strategy edges (not just model updates). "Gain-based edge update" is acceptable prose variation but "via gain" emphasizes the EXTENSION from the established gain principle, which is the hypothesis's claim.

Strong keep for "edge update via gain."

**Signal function vocabulary**: The segment introduces "signal function" as the named concept for signal(o_t, i, j). The card has row 490 for "default signal function." No new voting needed here beyond what's already covered.

**Log-odds / natural parameter**: Row 598 covers the "edge update natural parameter" name. The segment uses both forms extensively. The name question is live: "natural parameter" emphasizes information geometry; "log-odds update" emphasizes what's derived. The segment DERIVES log-odds as the natural parameter, so "natural parameter" is what results from the derivation, but "log-odds update" is what you DO.

**Directional fidelity**: Row 588 covers this. Confirmed: the correction must point at-least-roughly toward reality — the geometric formulation (δ^T H g(δ) ≥ c|δ|²) is what "directional fidelity" names.

## Key insight: conservative by design

The uncertainty ratio is STRUCTURALLY conservative: well-established edges (high n) resist revision; newly hypothesized edges (low n) are easily moved. This is the correct posture for causal beliefs under uncertainty. The segment makes this explicit as a design property, not an incidental consequence.

## M_t/edge evidence double-counting

Confirmed from Working Notes spike: mostly unfounded. M_t update extracts "what does o_t say about the world?"; edge update extracts "what does o_t say about causal link i→j?" Different information from the same observation. Self-correcting under the gain mechanism.
