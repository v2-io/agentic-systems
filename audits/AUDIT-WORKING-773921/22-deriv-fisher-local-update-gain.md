# Reflection: deriv-fisher-local-update-gain

**1. Predictions vs evidence.**
I predicted the segment would use Amari's natural gradients to prove the exactness of the gain formula $\eta^\ast = \frac{U_M}{U_M + U_o}$ for exponential family / Fisher-local models. The segment does exactly this, defining the gain operator as $K = (H_M + H_L)^{-1} H_L$.

**2. Cross-segment consistency.**
It correctly identifies its place relative to the previous appendix: this derivation is the "deterministic-meta-gain special case" where the agent's gain is read directly off the state (via the Hessian $H_M$) rather than learned via an innovation estimator. The references to `deriv-adaptive-gain-dynamics` and `emp-update-gain` are perfectly tight.

**3. Math verification.**
The math is rock solid. The decomposition of the precision matrix update into $K \cdot \tilde{\nabla}$ is standard Bayesian linear-Gaussian theory, but elegantly applied to the local tangent space of arbitrary smooth models via Information Geometry. The proof that the eigenvalues of $K$ are exactly $\frac{u_M}{u_M + u_o}$ is mathematically flawless. The boundary admissibility rules (handling improper priors and degenerate likelihoods) are correct.

**4. What direction will the theory take next?**
I am returning to the main sequence: `def-causal-information-yield.md`.

**5. What errors should I now watch for?**
The text notes that downstream matrix/tensor forms of tempo use Loewner ordering for persistence conditions (`deriv-matrix-persistence-condition`). I need to watch out for any matrix inequality that uses element-wise $\leq$ instead of the correct positive semi-definite ordering ($A \preceq B$).

**6. Predictions for next segments.**
`def-causal-information-yield` will formally define CIY as the difference in information gained when taking a specific action $a$ vs the information gained unconditionally, likely using Pearl's $do(a)$ operator.

**7. What would I change?**
Nothing. The explanation of why the "Natural-gradient direction" is chosen over the "Prior-curvature-rescaled direction" based on coordinate invariance (Čencov's theorem) is extremely satisfying.

**8. What am I now curious about?**
The "NeurIPS 2026 Paper 3" reference in the Working Notes. It implies AAT is generating (or reverse-engineering) papers about LLM hallucinations based on chart-rescaling no-go theorems. The lore and depth of this framework are staggering.

**9. What new knowledge does this enable?**
It mathematically guarantees that if an agent uses Natural Gradient Descent (or second-order optimization like K-FAC), it is automatically performing the optimal uncertainty-weighted update without needing an explicit adaptive Kalman filter loop.

**10. Should the audit process change?**
No, returning to the main sequence.

**11. What changes in my outline for the final report?**
Note the matrix extension of Adaptive Tempo ($K$ instead of $\eta^\ast$) as a critical feature for high-dimensional agents.

**12. How valuable does this segment feel to me?**
Very high. It proves that the empirical gain formula isn't just a heuristic, but a fundamental property of Riemannian geometry on statistical manifolds.

**13. What does the framework now potentially contribute to the field?**
It unifies Natural Gradient Descent (Information Geometry) with the Kalman Filter (Control Theory) under a single "Update Gain" operator $K$.
