# Reflection: emp-update-gain

**1. Predictions vs evidence.**
I predicted the exact formula $\eta^\ast = \frac{U_M}{U_M + U_o}$ scaling the mismatch. The segment confirms this and also explicitly notes that the update happens in Tangent Space via the transform $g(\delta_t)$, directly validating my thoughts from `def-mismatch-signal`.

**2. Cross-segment consistency.**
The segment explicitly raises the apparent contradiction between this optimal gain formula (which requires knowing $U_o$) and the `def-observation-function` (which states $h$ and noise are completely opaque to the agent). The resolution is that the agent estimates these from the mismatch sequence itself. The forward references to the appendices that prove this (`deriv-adaptive-gain-dynamics` and `deriv-fisher-local-update-gain`) are structurally excellent.

**3. Math verification.**
The mapping to the Kalman Filter ($K_t$) and Bayesian Conjugate updates is exactly correct. The "Representation note" acknowledging that updates must happen on the proper manifold (like natural parameter space or rotation groups) prevents the naive error of just adding raw gradients.

**4. What direction will the theory take next?**
Because this segment depends on two major derivations, I will read the appendices `deriv-adaptive-gain-dynamics.md` and `deriv-fisher-local-update-gain.md` next.

**5. What errors should I now watch for?**
The "Gain collapse" failure mode is critical. If an agent's estimated $U_M$ goes to 0 (overconfidence), it stops learning. I should watch for any part of the theory that assumes an agent *automatically* resets its gain when the environment changes. The text notes that this is something the agent *should* do, but a brittle agent might not.

**6. Predictions for next segments.**
`deriv-adaptive-gain-dynamics` will likely use the variance of the innovation sequence (the squared mismatches) to estimate the total uncertainty $U_M + U_o$. Since the agent knows its own $U_M$ (via the Hessian of its model), it can back out $U_o$ from the observed variance of $\delta_t$.

**7. What would I change?**
Nothing. The table validating the gain form against 5 different domains (including Software Developer) is brilliant.

**8. What am I now curious about?**
How does the agent know if the environment changed structurally (requiring a gain reset)? Persistent mismatch was mentioned in `def-model-class-fitness` as the signature for structural inadequacy. I assume it's the same here: a moving average of $\delta_t$ that refuses to go to zero triggers a reset of $U_M$.

**9. What new knowledge does this enable?**
It mathematically unifies learning rate annealing, Kalman gain, and human confidence.

**10. Should the audit process change?**
Continuing the Appendix exception rule.

**11. What changes in my outline for the final report?**
Note the "Gain collapse" failure mode as a key dynamic.

**12. How valuable does this segment feel to me?**
Extremely valuable. It is the heart of the "learning" process.

**13. What does the framework now potentially contribute to the field?**
It formalizes why "overconfidence" is mathematically disastrous for an agent in a non-stationary world.
