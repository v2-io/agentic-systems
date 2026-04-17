# Operationalizing κ via Hafez's H_b: A Tighter Analysis

**Status**: Working through a specific formal connection from the regime spike. Trying to move from Pattern to Hypothesis.

**Date**: 2026-03-13 (overnight session)

**Depends on**: `spike-kappa-regimes.md` for context; Hafez 2026 for the P/ΔH framework; `src/directed-separation.md` for the current formulation.

---

## The Idea

Directed separation says: f_M(M_τ⁻, e_τ) — no G_t argument. The epistemic update is goal-blind. Hafez's backward predictive uncertainty H_b measures how many internal states and actions are consistent with an observed outcome. Applied to the epistemic-purposeful boundary:

    H_b(epistemic-purposeful) = H(G_t | M_τ⁺, e_τ)

"Given the updated epistemic state and the triggering event, how much uncertainty remains about the agent's goal?"

If directed separation holds perfectly, knowing M_τ⁺ and e_τ tells you nothing about G_t beyond the prior — so H_b = H(G_t). If directed separation fails completely, the updated M_τ⁺ uniquely identifies G_t — so H_b = 0.

**Candidate operationalization:**

    κ = 1 - H(G_t | M_τ⁺, e_τ) / H(G_t)

This gives:
- κ = 0 when M_τ⁺ reveals nothing about G_t (perfect separation)
- κ = 1 when M_τ⁺ fully determines G_t (complete coupling)
- κ ∈ (0,1) for partial coupling

This is exactly the normalized mutual information between G_t and M_τ⁺ given e_τ:

    κ = I(G_t ; M_τ⁺ | e_τ) / H(G_t)

Let me verify: I(G_t ; M_τ⁺ | e_τ) = H(G_t | e_τ) - H(G_t | M_τ⁺, e_τ). Normalizing by H(G_t) (or by H(G_t | e_τ) if the event itself is informative about the goal — more on this below).

## Important Subtlety: The Event Channel

Here's where it gets interesting. The event e_τ can itself be informative about G_t, even under perfect directed separation, because:

    G_t → π → a_t → e_τ

The agent's goal influences which events arrive (through action selection). So H(G_t | e_τ) < H(G_t) in general — the event already "leaks" some information about the goal.

But this is the *selection* channel, not the *processing* channel. AAD's directed separation is about processing, not selection. So the right normalization might be:

    κ_processing = I(G_t ; M_τ⁺ | e_τ) / H(G_t | e_τ)

This conditions on the event (removing the selection-channel information) and asks: "given that this specific event arrived, does the way it was processed reveal additional information about the goal?"

- κ_processing = 0: The processing was goal-blind. Given the event, knowing the updated model tells you nothing more about the goal.
- κ_processing > 0: The processing was goal-conditioned. The way the event was integrated into the model reveals something about what the agent wanted.

This is the precise formal content of directed separation, expressed in information-theoretic terms.

## Two Kinds of κ

This analysis naturally produces two separate coupling measures:

1. **κ_selection = I(G_t ; e_τ) / H(G_t)**: How much does the goal influence which events arrive? This is the coupling through the action channel. AAD already accounts for this (it's part of the processing/selection distinction). This coupling is *expected* and *fine*.

2. **κ_processing = I(G_t ; M_τ⁺ | e_τ) / H(G_t | e_τ)**: How much does the goal influence how events are processed? This is the coupling that violates directed separation. This is the problematic one.

**Directed separation ≡ κ_processing = 0.**

For LLM agents, κ_selection is high (the prompt determines what queries are issued) AND κ_processing is high (the prompt determines how responses are interpreted). The selection coupling is fine; the processing coupling is the problem.

For a Kalman filter with an LQR controller, κ_selection might be moderate (the controller influences which states are visited, changing what events arrive) but κ_processing = 0 exactly (the Kalman filter's update equations don't reference the control objective). This is LQG separation.

## Why This Matters

If κ_processing can be measured (or at least estimated) from the agent's interaction stream, then:

1. **The directed-separation scope condition becomes quantitative**, not binary. Instead of "does f_M depend on G_t? (yes/no)" we have "how much does f_M depend on G_t? (bits)."

2. **The regime boundary becomes empirically identifiable.** You can measure κ_processing for a specific agent-task pair and determine whether it's in the laminar or turbulent regime.

3. **The approximation error of the sequential cascade** should be bounded by something involving κ_processing. In the laminar regime: error ≤ f(κ_processing) for some increasing function. Finding this function is the key theoretical result.

4. **Agent design becomes prescriptive.** To keep an agent in the laminar regime, minimize κ_processing. Concrete design implications: modular architecture (separate estimator and planner), explicit interfaces (pass state estimates, not raw observations), epistemic discipline (update based on evidence quality, not goal alignment).

## Challenges

### Measurement
For a real agent, computing I(G_t ; M_τ⁺ | e_τ) requires access to the joint distribution over goals, updated models, and events. For an LLM agent, this might require running the same event under different goals and seeing how the model update differs. This is feasible in simulation but hard in practice.

### The G_t representation problem
κ_processing as defined requires a well-defined distribution over G_t. For agents with complex, structured goals (like AAD's O_t + Σ_t), the entropy H(G_t) might be hard to compute. You might need to compute κ_processing for specific projections of G_t rather than the full goal state.

### Does κ_processing vary by model region?
Probably yes. An LLM agent might process factual observations about code structure nearly goal-blindly (low κ_processing for that region of M_t) but process ambiguous error messages in a highly goal-conditioned way (high κ_processing for that region). This suggests κ_processing should be indexed by region of M_t, not just a single scalar.

If κ_processing varies by region, then directed separation might hold *locally* for some regions of M_t while failing for others. The stability of the sequential cascade would depend on whether the high-κ_processing regions are the ones that matter for the current strategy (the ∂Σ/∂M sensitivity that came up in conversation).

## Connection to the Regime Spike

The "Reynolds number" from the regime spike would be something like:

    Re_eff ∝ κ_processing × (strategy sensitivity to this model region) / (architectural damping)

This combines:
- κ_processing: the raw coupling strength
- ∂Σ/∂M: how much the strategy cares about this model region
- μ: how well the architecture damps coupling (modular → high μ, transformer → low μ)

The product κ_processing × ∂Σ/∂M captures the intuition that coupling only matters when it occurs in a region the strategy is sensitive to. An LLM might process irrelevant background information in a goal-conditioned way (high κ_processing) but if the strategy doesn't depend on that information (low ∂Σ/∂M), the effective coupling is negligible.

## Where This Sits Epistemically

**What feels solid:**
- The decomposition into κ_selection and κ_processing (this is a clean formal distinction that maps exactly to AAD's processing/selection distinction)
- The information-theoretic operationalization using conditional mutual information
- The connection to Hafez's H_b

**What needs work:**
- Whether κ_processing actually characterizes a regime boundary (sharp transition) vs. just an approximation error (smooth degradation)
- The region-dependence of κ_processing and how to aggregate it into a useful scalar or vector
- Whether the approximation error bound (error ≤ f(κ_processing)) has a useful form

**What I'm guessing at:**
- The specific functional form of Re_eff
- Whether the regime transition is sharp enough to be useful (if the "turbulent" regime starts at κ_processing = 0.01, almost everything is turbulent and the theory doesn't help)
- Whether biological IDT mechanisms actually compute something like κ_processing

---

*This is tighter than the regime spike but still at the hypothesis level. The candidate operationalization κ = I(G_t ; M_τ⁺ | e_τ) / H(G_t | e_τ) is the most concrete output. Whether it characterizes a regime boundary requires either proof or simulation.*
