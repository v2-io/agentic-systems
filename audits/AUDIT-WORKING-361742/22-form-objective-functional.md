# Reflection: form-objective-functional

**Segment:** `#form-objective-functional`

## What this does

Defines V_{O_t}: trajectories → ℝ as the sole interface between the objective O_t and the rest of the theory. The real-valued codomain is a genuine restriction (scalar comparability), grounded in revealed preference (choosing = implicit scalarization).

Three arguments for scalar comparability:
1. Revealed preference — choosing implicitly scalarizes
2. Approximation — most multi-objective problems admit scalarization
3. Timescale separation — objective conflict resolved at slower timescale than strategy revision

## Naming relevance

Row for "objective functional" — the formulation names O_t and its interface V_{O_t}. The naming question: is "objective functional" the right name?

"Objective functional" correctly names what this is: the functional form of the objective. "Objective" names O_t; "functional" names the mathematical type (V_{O_t}: trajectories → ℝ). This is standard functional-analysis vocabulary.

"Objective" alone would underspecify. "Value functional" would name the evaluation tool rather than the object being defined. "Objective functional" is precise.

## New naming targets surfaced

**Satisfaction threshold V_min**: The minimum trajectory value the agent treats as acceptable. Names the boundary condition for the satisfaction gap diagnostic.

**Scalar comparability**: The constraint that V_{O_t} is real-valued. This is the key scope restriction.

## What's excellent here

The revealed preference argument for scalar comparability is philosophically rigorous: "An agent that acts has implicitly scalarized: choosing action a over a' imposes a total ordering at the moment of choice." This is the von Neumann-Morgenstern lineage.

The AND-node workaround for hard constraints (each constraint becomes a terminal node in Σ_t with its own scalar test) is a concrete engineering solution to the multi-constraint problem.

The O_t vs. Σ_t split is clear: O_t evaluates ("is this trajectory satisfactory?"); Σ_t guides ("which action sequence produces a satisfactory trajectory?"). Chess: objective (win) is simple; strategy (how to win) is complex.
