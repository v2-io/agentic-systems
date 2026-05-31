# Reflection: def-satisfaction-gap

**Segment:** `#def-satisfaction-gap`

## What this does

δ_sat = V_min - A_O(M_t; Π, N_h) — the distance between what the objective requires and what the best available policy can deliver.

Convention dependence:
- C1 (one-step): most conservative, may show false "unattainable"
- C2 (receding-horizon): captures recovery paths invisible to C1
- C3 (Bellman): strongest — δ_sat > 0 means no policy can achieve the objective

Monotonicity: δ_sat^B ≤ δ_sat^RH ≤ δ_sat^(1)

Disambiguation table is load-bearing: δ_sat > 0 does NOT automatically mean the goal is wrong. It means goal is unmet given current (M_t, Π, N_h).

## Naming relevance

Row 315: "satisfaction gap" — already voted keep +2 from orientation. This segment fully confirms that vote.

Key: "satisfaction gap" names the right thing. "Attainability shortfall" (the rejected alternative) would be technically accurate but loses the paired relationship with "control regret" that makes the 2×2 diagnostic work.

## Active inference positioning

The segment explicitly distinguishes from AI's expected-free-energy decomposition: EFE doesn't separate "goal is unattainable" (δ_sat) from "strategy is suboptimal" (δ_regret). The 2×2 cell map gives four diagnoses the orient cascade acts on differently.

The preferences-as-priors collapse in active inference (making "wanting o" and "expecting o" formally the same operation) is the Sun & Firestone dark-room critique. AAD's value-functional reformulation is AAD's response to that critique — a deliberate divergence.

## New concepts surfaced

**Objective attainability A_O**: The supremum over policy class. Named quantity.

**Convention hierarchy**: C1/C2/C3 monotonicity — already voted on in row for value object. This segment confirms.

**Disambiguation table**: Load-bearing diagnostic procedure (check M_t adequacy first, then Π and N_h, then consider O_t revision). Named structure.
