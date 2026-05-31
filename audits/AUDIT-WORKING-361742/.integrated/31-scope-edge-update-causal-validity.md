# Reflection: scope-edge-update-causal-validity

**Segment:** `#scope-edge-update-causal-validity`

## What this does

Scopes where gain-based edge updates produce genuinely interventional credences (Regime A), partially identified estimates (Regime B), or only associational proxies (Regime C).

Three conditions for strong causal validity:
- C1: Parent is an action leaf under agent's control (agent performed do(·))
- C2: Outcome is attributable (single parent or well-isolated intervention)
- C3: Execution conditions vary (no systematic self-selection bias)

The Regime A/B/C lattice parallels scope-ciy-observational-proxy's CIY admissibility regimes — the same three-regime structure applied to edge updates rather than CIY.

Key new concept: **identifiability coefficient ι_ij** — the agent's estimate of how cleanly the observed outcome can be attributed to edge (i,j). Combines with observability to give effective gain:
η_eff = (U_edge / (U_edge + U_obs)) · ι_ij

This unifies two sources of frozen edges:
1. Low observability (σ_v → 0): hard to MEASURE the outcome
2. Low identifiability (ι_ij → 0): outcome is measurable but can't be ATTRIBUTED to this edge

## Naming relevance

**Row 177 (edge update causal validity)**: The slug is five words. The candidates:
- "edge update causal validity": accurate but dense
- "Causal edge update": cleaner — but confusingly names the THING rather than the SCOPE of the thing. A scope segment should be named for what it scopes.
- "Identification regime": names the Regime A/B/C lattice — which IS the core content of this scope segment. This might actually be the best name for what the segment does.
- "Edge causal validity": shorter, preserves the point
- "Causal validity": too bare — loses the edge-update context

My reading: "Identification regime" is the strongest rename candidate because the segment IS the canonical home of the Regime A/B/C identification lattice. The content IS the regime classification. "Edge causal validity" is acceptable. "edge update causal validity" (keep) is verbose but accurate. I'll vote +1 keep and +2 for "identification regime" as the rename that best names what the segment IS.

**Row 15 (identifiability coefficient ι_ij)**: Confirmed by segment. ι_ij ∈ [0,1] is the "identifiability coefficient" — the agent's estimate of attribution clarity. Already in use in deriv-strategic-dynamics. Strong canonicalize.

## New concepts surfaced

**Identifiability-adjusted gain η_eff = (U_edge/(U_edge+U_obs)) · ι_ij**: Named quantity, key to understanding why edges freeze. Not just observability — BOTH observability AND identifiability can independently freeze an edge.

**Optimal decomposition depth (three-factor balance)**: The segment adds ι_ij degradation with depth as a third factor in optimal decomposition depth (beyond observability and chain confidence decay). Three-factor balance named.

**Depth-dependent identifiability degradation**: Deeper edges have lower ι_ij — each indirect inference level adds an attribution step. Conjectured monotone decrease with depth.
