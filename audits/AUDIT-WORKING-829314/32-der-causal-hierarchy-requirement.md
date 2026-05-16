# Reflection: 32-der-causal-hierarchy-requirement

**1. Predictions vs evidence:** I predicted it would loop back to `#def-pearl-causal-hierarchy` and prove that evaluating $Q_O$ requires Level 2 (Intervention) access because of the $do()$ operator. It does exactly this, using the Causal Hierarchy Theorem to explicitly narrow the scope of the rest of Section II to "learning purposeful agents."

**2. Cross-segment consistency:** Strong dependencies on `#def-value-object`, `#def-pearl-causal-hierarchy`, and `#scope-agency`. It elegantly excludes pre-compiled agents (like PID or LQR) from the rest of Section II's dynamics, resolving the slight awkwardness of treating a thermostat as a strategic planner. 

**3. Math verification:** The logic is a direct, rigorous application of Bareinboim et al. (2022). If the objective requires computing $P(Y \mid do(X))$, and you only have observational data $P(Y \mid X)$, you mathematically cannot compute the objective. Therefore, you must acquire interventional data.

**4. What direction will the theory take next?** The next segment is `der-loop-interventional-access.md`.

**5. What errors should I watch for?** The text notes that LLMs absorb causal priors from text, but clearly distinguishes this from verified interventional structure. This means the framework must be careful not to treat an LLM's pre-trained knowledge as true Level 2 data. It is a simulated L2 prior based on L1 training.

**6. Predictions for next segment:** `der-loop-interventional-access.md` will prove that the standard agent-environment feedback loop naturally generates Level 2 data. Because the agent *causes* its own actions, the action is by definition an intervention (breaking upstream confounders), allowing the agent to measure $P(o \mid do(a))$ directly from its chronica $\mathcal{C}_t$.

**7. What would I change?** Nothing. The scope narrowing to "learning agents" is a very clean theoretical cut that protects the complexity of the upcoming strategy dynamics from trivial counterexamples.

**8. Curious about:** How does the framework handle agents that observe *other* agents acting? Is that Level 1 or Level 2 data? If I watch you touch a hot stove, do I gain Level 2 knowledge? In Pearl's terms, if I can assume your action was unconfounded with the stove's temperature, it acts like L2. But if you touched it *because* you knew it was cold, it's L1. This seems like a deep problem that Section III (Composites) will need to address.

**9. What new knowledge does this enable?** The explicit exclusion of pre-compiled controllers from the "learning-agent scope," confirming that strategy dynamics only apply to entities that must actively maintain or build their causal maps.

***

### Wandering Thoughts and Ideation

The claim that LLMs trained on text only have "causal priors" and not true Level 2 knowledge provides the exact mathematical reason why LLMs confidently hallucinate code that looks correct but fails to compile. 

In the training data (GitHub), the LLM sees code ($X$) and it sees passing tests ($Y$). It learns the conditional association $P(Y \mid X)$. But it never intervened. It never wrote bad code just to see what the compiler would do. It only saw the final, polished PRs that humans chose to upload (a massive selection bias). Therefore, its internal model of the compiler is entirely associational. When the LLM is deployed as an agent and generates its own novel code ($do(X_{\text{new}})$), it is stepping outside the associational distribution. Because the Causal Hierarchy Theorem proves you cannot reliably compute L2 from L1, the LLM is mathematically guaranteed to make structural errors that a true L2 agent (a human who has spent hours fighting the compiler) would not make.

However, the moment you put the LLM in an AAD feedback loop (where it writes code, runs the compiler, and reads the error itself), it crosses the epistemic boundary. It begins generating its own $do()$ data. Its chronica $\mathcal{C}_t$ begins to fill with genuine Level 2 information. The framework beautifully predicts that an LLM with a REPL is a fundamentally different class of epistemic entity than an LLM with only a chat interface. The REPL provides the interventional access required to verify and stabilize the fragile causal priors.

The exclusion of PID controllers and LQR from this scope is also very satisfying. It felt weird to say a thermostat "has a strategy." By defining a "learning-agent scope," AAD acknowledges that while a thermostat mathematically fits the $X_t = (M_t, G_t)$ formulation, it's a degenerate, frozen case. The interesting dynamics of Section II (the Orient Cascade, Strategic Calibration, CIY) only happen when $\Sigma_t$ is actually allowed to change in response to new data.