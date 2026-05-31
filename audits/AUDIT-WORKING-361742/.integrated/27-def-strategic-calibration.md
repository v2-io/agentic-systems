# Reflection: def-strategic-calibration

**Segment:** `#def-strategic-calibration`

## What this does

Defines the strategic calibration residual δ_strategic = (Σ w_ij · r_ij²)^(1/2), an L² aggregation of per-edge value-increment residuals. Each edge residual r_ij = E[ΔV_O | edge (i,j) traversed] - ΔV_O_observed measures how well the edge's predicted value increment matches the observed one.

Key architectural point: this is one of TWO distinct strategic mismatch quantities:
1. **δ_s (plan-confidence error)**: scalar gap between P̂_Σ and Φ (independence-model plan value). Computable from status propagation alone; no credit assignment needed. Proven persistence target. Under correlated failures (causally insufficient DAG), Φ OVERESTIMATES actual success, so δ_s tracks calibration *within* the independence model.
2. **δ_strategic (calibration residual)**: L² aggregation of per-edge value-increment residuals. Requires credit assignment. Finer-grained diagnostics. Persistence properties OPEN pending #disc-credit-assignment-boundary.

The three conditioning requirements for r_ij:
- Edge was actually traversed
- M_t is adequate (so observed ΔV_O is meaningful)
- Execution fidelity: agent followed Σ_t's prescription (else residual conflates bad plan vs bad execution)

## Naming relevance

**Row 424 (strategic calibration)**: "strategic calibration" is accurate but minimally load-bearing. The segment itself uses three terms: "strategic calibration residual," "edge residual aggregate," and δ_strategic. The exploration team's canonicalization recommendation is correct: use "strategic calibration residual" for the aggregated quantity, "edge residual" for per-edge r_ij, δ_strategic for the symbol. Stop using "edge residual aggregate."

The case against "Strategy calibration" (the rename candidate): "strategic" is the right adjective here because the calibration is OF the strategy DAG's edge predictions. "Strategy calibration" is grammatically awkward — it reads as "calibration of a strategy" (measurement of the strategy's precision) rather than "calibration of the strategy DAG's predictive edges." The adjective form is more precise.

**Row 325 (δ_strategic strategic-calibration residual)**: Confirms "Strategic calibration residual" as the full form.

**Row 430 (plan confidence)**: The segment references "plan-confidence score" P̂_Σ and "plan-confidence error" δ_s. These should be on the card — confirmed.

## New concepts surfaced

**Execution fidelity**: Named conditioning requirement. Whether it needs its own row in the tracker — probably not, it's a conditioning requirement not a named concept. But worth watching.

**Credit assignment problem**: Named problem, cross-referenced heavily. The card has row 560 for this.

**δ_s vs δ_strategic distinction**: Load-bearing disambiguation. These are related but not interchangeable. The segment's Discussion makes this explicit and architecturally important.

## What's excellent here

The "second-order inference" observation in Epistemic Status is precise: δ_strategic requires accumulating evidence over multiple edge traversals, making it inherently slower than δ_epistemic (updates on every observation) or δ_sat (evaluable from M_t and Σ_t alone). This is a genuine architectural insight about the timescale hierarchy of diagnostic quantities.

The Working Notes' suggestion for per-edge or per-path residual profiles over the scalar summary is clearly right: the scalar is useful for persistence conditions; the profile is useful for strategy revision. These are different use cases and the aggregation lossy for revision.

## Status: discussion-grade

The segment honestly flags the aggregation (L² with criticality weights) as "a reasonable first pass, not a derived result." The credit-assignment problem is genuinely open. This is appropriate honesty.
