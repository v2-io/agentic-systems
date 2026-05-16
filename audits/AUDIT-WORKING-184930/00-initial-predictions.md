# Initial Predictions for De Novo Audit

Based *only* on the outlines, README, and reference definitions, here are my initial expectations and predictions regarding the load-bearing arguments and potential areas of overclaim:

1. **The Math: Forced vs. Chosen**
   - **Forced:** Section I (Adaptive Systems) appears to rely on solid control theory (Lyapunov stability, monotone operators) and basic information theory (Shannon entropy, predictive compression). The persistence condition ($\alpha > \rho/R$) will likely be a forced mathematical necessity derived directly from standard Lyapunov bounds under bounded disturbance.
   - **Chosen:** Section II's (Actuated Adaptation) formalization of strategy as a probabilistic causal DAG seems to be a strong representational choice (a formulation) rather than a mathematical inevitability. I expect the "single-parameter edges" ($p_{ij}$) and the handling of the OR/AND logic to be elegant but ultimately a chosen approximation, not forced by fundamental physics.

2. **The "Sleight of Hand" or Overclaim Potential**
   - **Directed Separation:** The "directed separation" concept (that epistemic update is goal-blind) is noted as holding "by construction" for Class 1 agents. The theory acknowledges this fails for Class 2 (e.g., LLMs). However, I suspect that the boundary might be fuzzier in practice, and the application of Section II results to learning agents could inadvertently smuggle in Class 2 coupling under a Class 1 guise.
   - **Information Bottleneck in Purposeful Agents:** The application of the Information Bottleneck principle to non-epistemic state (e.g., shared intent in Section III or strategy DAGs in Section II) might stretch the standard IB bounds. I expect the formalization of "deliberation cost" to potentially conflate information-theoretic processing time with wall-clock time in ways that aren't strictly mathematically isomorphic.
   - **Composition Admissibility:** Section III relies on "contraction templates" and "composition closure." Given that the framework notes composition transition dynamics are an open gap, I predict the existing composition results rely on heavily constrained symmetric or cooperative assumptions that may not generalize robustly.

3. **Software as a Calibration Lab**
   - Temporal Software Theory (TST) using Git as literal interventional data is conceptually brilliant. However, I predict that mapping code changes (actions) to causal interventions ($do(a)$) might oversimplify the latent unobservable states in software development (e.g., developer mental models and off-band communication).

Overall, the separation of epistemic strength (`exact` vs `heuristic` vs `discussion`) looks highly disciplined. I expect the core to be genuinely solid, but the transitional bridging—from mismatch ODEs to strategy DAGs—to be where the most scrutiny is needed.
