# Reflection: hyp-edge-update-via-gain

**1. Predictions vs evidence.**
I predicted the segment would generalize the exact Beta-Bernoulli update rules from the appendices into a schema for arbitrary strategy edges. It does exactly this, proposing the form $p_{ij}^{\text{new}} = p_{ij}^{\text{old}} + \eta_{\text{edge}} \cdot \left(\text{signal}(o_t, i, j) - p_{ij}^{\text{old}}\right)$.

**2. Cross-segment consistency.**
It perfectly integrates the empirical gain principle (`emp-update-gain`) and the observability constraints (`der-observability-dominance`). The Working Notes provide a fascinating glimpse into the framework's internal dependency management (the 2026-05-11 removal of the `deriv-edge-update-natural-parameter` dependency to break a cycle), which speaks to the incredible rigor of the build process.

**3. Math verification.**
The epistemic status is "Hypothesis" because while the *gain* is known ($\eta = U/(U+U_o)$), the *signal* function requires solving the credit-assignment problem. The explicit acknowledgment that Marginal Bayesian updates provide the correct mean but violate the sector bound (SA1) due to $O(1/n)$ bias is a profound warning against naive Bayesianism in deep structures. The gradient-based signal candidate is structurally sound.

**4. What direction will the theory take next?**
The next segment in the OUTLINE sequence is `scope-edge-update-causal-validity.md`.

**5. What errors should I now watch for?**
I must ensure that downstream literature does not treat the `signal` function as trivially computable (e.g., $y - p$) for anything other than single-parent, fully observable nodes. Multi-parent OR/AND nodes require complex credit assignment.

**6. Predictions for next segments.**
`scope-edge-update-causal-validity` will formalize the $\iota_{ij}$ (identifiability coefficient) mentioned in the appendices, defining when an agent's observation actually provides valid causal information about a specific strategy edge.

**7. What would I change?**
Nothing. The resolution to the "double counting" objection (updating $M_t$ and $\Sigma_t$ from the same observation) is pristine philosophy of science: $M_t$ asks "what does this say about the world?", $\Sigma_t$ asks "what does this say about my causal link?". They are orthogonal questions asked of the same data.

**8. What am I now curious about?**
The log-odds ($\lambda$) coordinate. The text states it is the *unique* parameterization on which Bayesian independent-evidence accumulation is additive. This links back to the `disc-additive-coordinate-forcing` meta-pattern. I am eager to see how log-odds gradients perform compared to probability-space gradients in deep planning structures.

**9. What new knowledge does this enable?**
It provides the exact update rule required to make a Strategy DAG "learn" from experience, connecting planning to reinforcement learning.

**10. Should the audit process change?**
No.

**11. What changes in my outline for the final report?**
Note the "Signal vs Gain" split in strategy updates (Gain is solved; Signal is domain-specific / requires credit assignment).

**12. How valuable does this segment feel to me?**
Very high. It translates abstract regret into concrete DAG modifications.

**13. What does the framework now potentially contribute to the field?**
It formalizes why Bayesian updating is safe for leaves, but requires gradient-based backpropagation for hidden nodes to maintain Lyapunov stability.
