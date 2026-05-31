# Reflection: 31-def-strategy-dimension

**1. Predictions vs evidence:** I predicted this would define $\Sigma_t$ as the agent's current plan/policy structure and formalize the split $G_t = (O_t, \Sigma_t)$. It does exactly this. It explicitly separates "evaluation" ($O_t$, "How good is this?") from "guidance" ($\Sigma_t$, "How do I produce a good trajectory?").

**2. Cross-segment consistency:** Good dependencies (`form-complete-agent-state`, `form-objective-functional`). It cleanly sets up the distinction between satisfaction gap and control regret, noting that older formulations committed a "type error" by trying to subtract a strategy graph from an epistemic state ($\delta_{\text{goal}} = G_t - M_t$). This is excellent theoretical hygiene.

**3. Math verification:** $G_t = (O_t, \Sigma_t)$ is definitional. The table ordering strategy representations by expressiveness (Reactive $\to$ Cached policy $\to$ Subgoal sequence $\to$ Causal DAG) is a very useful structural taxonomy.

**4. What direction will the theory take next?** The next segment is `der-causal-hierarchy-requirement.md`.

**5. What errors should I watch for?** **Finding (Open Problem Flag):** The "Working Notes" explicitly flag that the cognitive cost of maintaining a complex $\Sigma_t$ is currently unmodeled. While Section I has a rigorous Information Bottleneck theory for compressing $M_t$ ($\beta$), no formal analog exists yet for compressing strategy. This is a massive open problem for bounded agents (like LLMs with finite context windows), and the framework honestly admits it. I should note this gap.

**6. Predictions for next segment:** `der-causal-hierarchy-requirement.md` will loop back to `#def-pearl-causal-hierarchy` and prove that an agent cannot construct a valid causal DAG ($\Sigma_t$) or accurately evaluate $Q_O$ if it is trapped at Level 1 (Association). It must have Level 2 (Intervention) access to distinguish effective strategies from superstitious correlations.

**7. What would I change?** Nothing. The section on "Resolving a type error" shows the framework actively cleaning up its own past mistakes, which is exactly what a de novo audit hopes to see.

**8. Curious about:** The "Commitment state" note: how does an agent decide when an OR branch in a strategy DAG becomes a committed, irreversible path? This requires a formal theory of a "deliberation threshold" (which I know is coming up in `#disc-exploit-explore-deliberate`).

**9. What new knowledge does this enable?** The explicit separation of Objective Richness from Strategic Richness. A chess engine has a trivial objective (1, 0, -1) but a massively complex strategy. A multi-objective optimizer might have a massively complex objective (a 10-dimensional Pareto frontier) but a trivial strategy (gradient descent). 

***

### Wandering Thoughts and Ideation

The realization that $\delta_{\text{goal}} = G_t - M_t$ is a type error is a hilarious and profound bit of theoretical self-correction. In naive reinforcement learning or classical control theory, we often just say "Error = Target - Current State". This works fine if your target is "Room temperature = 72" and your state is "Room temperature = 70". You can subtract 70 from 72. 

But what if your Target ($G_t$) is a complex causal DAG representing the invasion of Normandy, and your current state ($M_t$) is a probabilistic belief about weather patterns and troop movements? You cannot subtract a belief state from a strategy graph. It's mathematically nonsensical. The framework must invent new, properly typed diagnostics to replace the naive $\delta_{\text{goal}}$. These will be the "Satisfaction Gap" (evaluating $O_t$ against the best achievable future in $M_t$) and "Control Regret" (evaluating your current $\Sigma_t$ against the optimal $\Sigma_t$ in $M_t$). 

This also highlights the incredible cognitive burden of maintaining $\Sigma_t$. If $\Sigma_t$ is a Causal DAG, the agent has to constantly prune and update this graph as $M_t$ changes. If $M_t$ learns that a bridge is out, $\Sigma_t$ must instantly recalculate all paths that relied on that bridge. The Working Notes bravely admit that AAD does not yet have a formal Information Bottleneck theory for compressing $\Sigma_t$ the way it does for $M_t$. 

For a Logogenic Agent (LLM), this is exactly the problem of the prompt getting too long: if the plan (the chain-of-thought scratchpad, $\Sigma_t$) exceeds the context window, the agent literally forgets what it was trying to do. The cost of strategy is very real in physical systems, and until AAD formalizes it, the theory implicitly assumes strategy computation is free once the epistemic update $M_t$ is complete. The temporal nesting ($v_\Sigma \ll v_M$) helps mitigate this by running the expensive strategy update less frequently, but it doesn't solve the fundamental compression bound.