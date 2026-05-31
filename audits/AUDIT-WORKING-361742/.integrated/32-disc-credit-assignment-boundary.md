# Reflection: disc-credit-assignment-boundary

**Segment:** `#disc-credit-assignment-boundary`

## What this does

Characterizes the boundary between tractable and intractable credit assignment for strategy DAG edge updates. Key results:

1. **What the theory can guarantee WITHOUT solving credit assignment**:
   - Persistence is credit-assignment-free (Prop B.5): sector condition transfers via Jacobian J = ∇_p P_Σ. Persistence of δ_s (plan-confidence error) requires no per-edge attribution.
   - Plan-level diagnostics (δ_sat, δ_regret, orient cascade) operate on aggregate value, not per-edge quantities.
   - Observability-dominance identifies the tractable edges.

2. **Tractable cases**: All intermediates observable (decoupled Beta-Bernoulli updates), binary outcomes in linear chains (proportional blame = exact marginal Bayesian), tree DAGs with observable leaves (belief propagation).

3. **Three independent intractability barriers**:
   - #P-hardness: exact attribution via Shapley values for monotone Boolean functions
   - Information-theoretic underdetermination: dim(I(V_obs)) ≤ |V_obs|
   - Posterior correlation barrier: factored representation loses correlation

4. **Design requirement**: Directional fidelity per edge is the ONLY formal requirement — expected correction is non-positively correlated with current error.

5. **Four-level credit assignment hierarchy**: Level 0 (none/plan-level) to Level 3 (exact/#P-hard). Formal guarantees require only Level 0; adaptive behavior requires Level 1.

The **default signal function** (gradient-based attribution in log-odds):
λ_k_new = λ_k + η_edge · ι_k · J_k(y_G - P̂_Σ)/‖J‖²

This closes the historical mechanical break (probability-space presentation could push p outside [0,1] when ‖J‖² → 0). Log-odds coordinate has domain ℝ; sigmoid projection guarantees p ∈ (0,1).

**OKRs as observability-by-design**: Key Results are intermediate nodes with σ_v ≈ 1 by construction, converting intractable credit assignment to componentwise updates (Prop B.2). Goodhart's Law maps to terminal-condition misalignment with O_t.

## Naming relevance

**Row 560 (credit assignment boundary)**: Segment fully confirms. "Credit assignment boundary" — both words are load-bearing: "credit assignment" names the class of problem; "boundary" names what the segment characterizes (the tractable/intractable boundary). Strong keep. "Credit assignment frontier" is acceptable alternative but "boundary" is more precise (it's a limit/threshold, not a geographic frontier).

**Row 490 (default signal function)**: Confirmed. The gradient-based attribution in log-odds IS the default signal function. The segment defines it explicitly as "AAD's default implementation, analogous to η* = U_M/(U_M + U_o) being the default gain." Strong canonicalize.

**Row 588 (directional fidelity)**: Confirmed by this segment. The design requirement IS directional fidelity — E[(signal(o_t,i,j) - p_ij)(p_ij - θ_ij)] ≤ 0. Strong keep. "Corrective alignment" rejected for AI-safety baggage. "Pointing condition" is accurate but loses the engineering register ("fidelity" as in signal fidelity/control fidelity).

**Row 603 (instrumented intermediate / forced observability node)**: Confirmed. The OKR analysis demonstrates that making intermediates observable converts intractable credit assignment to tractable componentwise updates. "Forced observability node" is the stronger name — it names the MECHANISM (forcing observability) and the RESULT (#P-hard → O(1)). "Instrumented intermediate" is descriptive but doesn't capture the forcing/consequence.

## Key insight

The observability lever is more powerful than the algorithm lever: designing strategy with observable intermediates sidesteps intractability entirely. This makes observability investment (row 626) and the epistemic dead zone (row 405) adjacent concepts: dead zones are the consequence of failing to make observability investment.
