# Reflection: result-persistence-condition

**Segment:** `#result-persistence-condition`

## What this does

The central inequality of the framework, fully stated with structural/task-adequacy decomposition:
- Structural persistence: α > ρ/R (Lyapunov exact under GA-2, GA-3)
- Task adequacy: R* < ‖δ_critical‖ (domain-specific constraint)

The linear operational form: 𝒯 > ρ/‖δ_critical‖ is exact for linear correction, approximate for mildly nonlinear.

Key: Two conditions, not one. Prior conflation produced category errors in domain transfer. The remedies for structural failure vs. task-adequacy failure are different (architectural change vs. increase 𝒯 or reduce ρ).

## Naming relevance

"Persistence condition" is the most important naming target. Row 84 in the tracker? Let me think — the card has already been searched and I've voted on row 352 (sector condition) and row 282 (adaptive reserve). The persistence condition itself is likely a separate row.

Key question: Should the formal name be "persistence condition" or something else? The segment title is "Persistence Condition" — this is the result. From the notation conventions: α > ρ/R (or 𝒯 > ρ/‖δ_critical‖ in linear form). The name is load-bearing: it connects to LEXICON's three-sense taxonomy (structural/operational/continuity persistence).

"Persistence condition" correctly names what it is: the condition for persistence. It does NOT name the sector condition (the assumption) or the sector condition stability (the result about stability given the sector condition). All three are distinct:
1. Sector condition: assumption on correction function F (points inward with efficiency α)
2. Sector condition stability: result given sector condition (mismatch remains bounded)
3. Persistence condition: the combined operational result (α > ρ/R, or 𝒯 > ρ/‖δ_critical‖)

## New naming targets surfaced

**Task adequacy**: Named concept "how wrong can the model be before the agent's actions become harmful?" Separate from structural persistence.

**Persistence cost**: "persistence has a cost, not just a threshold" — the information-rate bound from #deriv-persistence-cost (Ṙ ≥ nα/2 nats/time, Landauer analog). Named concept.

**Channel capacity prerequisite**: "C ≥ 𝒯/2" — a channel-capacity prerequisite the threshold condition alone doesn't name.

**δ_critical**: The domain tolerance threshold. This might be named in the tracker.

## What's excellent here

The Findings section brief is excellent: "Below this threshold the system doesn't merely degrade — it loses bounded behavior, the way a balance held just barely beneath a tipping point is qualitatively different from one well above it." This is the Feynman criterion being met.

The persistence-has-a-cost point is important: the threshold guarantees bounded mismatch but doesn't say how much effort is required to hold that bound. The information-rate floor Ṙ ≥ nα/2 is the Landauer analog — you can't get the guarantee for free.

The two-condition decomposition (structural vs task-adequacy) as the AAD-internal contribution: the structural-persistence Lyapunov part is standard Khalil; the task-adequacy split and the distinction between the two remedies is the synthesis.
