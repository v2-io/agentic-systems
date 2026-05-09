# Reflection: 43-def-strategic-calibration

**1. Predictions vs evidence:** I predicted this would define how the agent updates individual edge probabilities $p_{ij}$ using edge-specific residuals to figure out *which step* of the plan failed. It does exactly this, defining the edge residual $r_{ij} = \mathbb{E}[\Delta V_O] - \Delta V_O^{\text{observed}}$ and the aggregate $\delta_{\text{strategic}}$. It explicitly calls out the "credit-assignment problem" when multiple parents contribute to a single outcome.

**2. Cross-segment consistency:** Good dependencies (`def-strategy-dag`, `def-value-object`). It appropriately forward-references `#schema-strategy-persistence`, `#deriv-edge-credence-dynamics`, `#hyp-edge-update-via-gain`, and `#disc-credit-assignment-boundary`. The distinction between the theoretical plan-confidence error $\delta_s$ and the operational strategic calibration $\delta_{\text{strategic}}$ aligns perfectly with the "Correlation Hierarchy" (L0 vs L1/L2) established in `#def-strategy-dag`.

**3. Math verification:** The residual $r_{ij}$ is standard. The aggregation $\delta_{\text{strategic}} = (\sum w_{ij} r_{ij}^2)^{1/2}$ is a standard weighted $L^2$ norm. The text rightly labels this `status: discussion-grade`, acknowledging that the specific norm and weighting scheme are heuristic engineering choices, not foundational physical derivations.

**4. What direction will the theory take next?** The next segment is `der-causal-insufficiency-detection.md`.

**5. What errors should I watch for?** The section on "Execution fidelity" highlights a massive epistemic problem. If a plan fails, was the plan bad, or did the agent just fail to execute it? (e.g., "The diet didn't work" vs "I didn't stick to the diet"). The math assumes execution fidelity is known or perfectly monitored, which is rarely true outside of strict software environments. 

**6. Predictions for next segment:** `der-causal-insufficiency-detection.md` will explain how the agent uses these residuals to detect the latent common causes ($C$) discussed in the Correlation Hierarchy of `#def-strategy-dag`. It will likely show that if sibling edges $A$ and $B$ have correlated residuals ($Cov(r_A, r_B) > 0$), the DAG is causally insufficient and needs an L1 augmentation.

**7. What would I change?** I would emphasize the "Execution fidelity" problem even more. For Temporal Software Theory (TST), execution fidelity is usually perfect (the compiler executes exactly what you wrote). But for organizational agents (Section III), execution fidelity is the primary source of error. 

**8. Curious about:** The "Discussion" mentions $\delta_s = \hat{P}_\Sigma - \Phi$, where $\Phi$ is the "AND/OR formula at true edge rates." But how does the agent know the "true" edge rates to compute $\Phi$? It doesn't. $\Phi$ is a theoretical construct for the Lyapunov persistence proofs, while $\delta_{\text{strategic}}$ is the operational quantity the agent actually computes. Keeping the "God's eye view" variables distinct from the "Agent's eye view" variables is tricky.

**9. What new knowledge does this enable?** The formal definition of the credit assignment boundary in strategy DAGs, and the mathematical necessity of execution-fidelity monitoring for accurate strategy updates.

***

### Wandering Thoughts and Ideation

The "Execution Fidelity" condition is the mathematical boundary between Section II (Single Agent Strategy) and Section III (Composite Agents). 

For a single monolithic agent (like an LLM executing code in a local sandbox), execution fidelity is $\approx 100\%$. When it types `python run.py`, the python interpreter runs exactly that file. If the result is bad, the LLM's strategy was bad ($r_{ij} > 0$).

But consider a CEO (Agent 1) commanding a VP of Engineering (Agent 2) to build a feature. The CEO's strategy DAG says "If Feature built $\to$ Revenue goes up." The feature is built, but revenue goes down. The CEO calculates a massive $r_{ij}$ and concludes "Building features doesn't increase revenue. My strategy is flawed." 

But the CEO failed to monitor execution fidelity. The VP of Engineering actually built a buggy, terrible, delayed version of the feature because they were understaffed. The CEO's strategy was theoretically correct, but execution failed. Because the CEO's observation channel $h$ didn't include a high-resolution test for execution fidelity, they misattributed the failure to the strategy DAG ($\Sigma_t$) instead of the sub-agent's capacity. 

This proves that as soon as your "actions" $a_t$ are actually delegated commands to other agents (Composite Agents), you *must* add an execution-monitoring feedback loop, or your strategic calibration will mathematically diverge from reality. You will learn the wrong lessons and prune the wrong edges. This is why bureaucracy (status reports, KPIs, telemetry, middle management) exists: it is the literal caloric cost organizations pay to ensure $\delta_{\text{strategic}}$ remains computable and accurate. Without execution monitoring, strategy is un-calibratable.