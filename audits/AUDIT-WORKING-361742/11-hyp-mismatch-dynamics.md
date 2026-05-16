# Reflection: hyp-mismatch-dynamics

**Segment:** `#hyp-mismatch-dynamics`

## What this does

The linear ODE: d‖δ‖/dt = -𝒯·‖δ‖ + ρ(t). Explicitly a heuristic first-order approximation. The general nonlinear case is the sector-condition framework.

Key results within:
- Steady-state Model D: ‖δ‖_ss = ρ/𝒯
- Steady-state Model S (stochastic): ‖δ‖_rms = σ_w/√(2𝒯) — squared root scaling means correction less effective against noise than drift
- Adversarial coupling: superlinear scaling with exponent depending on disturbance model (D: squared, S: 3/2)

The bridging assumption (discrete→continuous via fluid limit) is quantified: zero gap for Model D, O(η*c_max) variance gap for Model S.

## Naming relevance

Tracker row for "mismatch dynamics" — the segment's title is what's being named. The key question: is this the right name for a heuristic that's superseded by the sector-condition framework?

"Mismatch dynamics" correctly names what this is: the dynamics of ‖δ‖ over time. It's not "error dynamics" (wrong register) or "adaptive dynamics" (too broad). The "linear mismatch hypothesis" or "mismatch dynamics (linear)" form might be clearer to distinguish from the nonlinear result, but the segment itself uses "mismatch dynamics" throughout.

## New naming targets surfaced

**Environment change rate ρ(t)**: Named as "the rate at which new mismatch is introduced by changes in Ω." Already in tracker row 43 (disturbance rate).

**Model D / Model S**: The two disturbance models (deterministic bounded / stochastic zero-mean). These are referenced across multiple segments.

**Adversarial coupling**: "When two agents are coupled (A's actions increase B's disturbance)". The γ_A coupling coefficient. This is related to tracker row 84 (adversarial edge targeting).

**Superlinear scaling**: The squared law (Model D) and 3/2 law (Model S) for adversarial tempo advantage. These are specific results.

## What's excellent here

The distinction between Model D (‖δ‖_ss ∝ 1/𝒯) and Model S (‖δ‖_rms ∝ 1/√𝒯) is important and correct. The stochastic case's correction is less effective than the deterministic case — this is a real result with implications for how hard it is to stay calibrated in noisy environments vs. drifting ones.

The adversarial coupling formula ρ_B = ρ_B,base + γ_A·𝒯_A is clean and explicit — tempo is now an attack surface.

The nonlinear reality Discussion is good epistemic work: it lists exactly the ways the linear model fails (saturation, threshold effects, structural breakdown) and correctly points to the sector-condition framework as the solution for all three.
