# Reflection: 09-def-pearl-causal-hierarchy

**1. Predictions vs evidence:** I predicted this would adopt Pearl's 3-level hierarchy (Association, Intervention, Counterfactuals). It does exactly that, mapping L1 to $P(o|c)$, L2 to $do(a)$, and L3 to counterfactual regret. The key theoretical move is grounding this hierarchy in the temporal structure of the feedback loop rather than abstract graphical models.

**2. Cross-segment consistency:** The dependency chain (`post-causal-structure`, `scope-agency`) is pristine. It sets up `#der-causal-hierarchy-requirement` and brilliantly references TST's `git checkout` as a literal L3 operator.

**3. Math verification:** The equations for L1, L2, L3 use standard Pearl notation. $P(o_t \mid do(a_{t-1}), M_{t-1})$ correctly conditions the interventional observation on the agent's prior model.

**4. What direction will the theory take next?** The next segment is `form-agent-model`, which will define the internal state $M_t$.

**5. What errors should I watch for?** The claim that `git checkout` is a *literal* Level 3 execution is a beautiful, load-bearing analogy for TST, but it is slightly dangerous. It assumes the environment (the codebase) is perfectly state-isolated. If the code interacts with a live database or external API, `git checkout` doesn't roll back that external state. TST needs to be careful to bound its $\Omega$ so that "counterfactual execution" doesn't leak.

**6. Predictions for next segment:** `form-agent-model` will define $M_t = \phi(\mathcal{C}_t)$, characterizing the model as a lossy compression of the chronica.

**7. What would I change?** Nothing. The table at the bottom distinguishing between "Availability vs. exploitation" is excellent pedagogical material.

**8. Curious about:** How does the framework handle agents that *think* they are doing L2 interventions but are actually trapped in L1 because of unobserved confounders in $h$?

**9. What new knowledge does this enable?** The "Causal Hierarchy Theorem" (Bareinboim et al. 2022) proves L2 cannot be computed from L1 data alone. This provides the mathematical proof for why agents *must* act to learn causal laws; passive observation is mathematically insufficient.

***

### Wandering Thoughts and Ideation

The application of Pearl's Causal Hierarchy to agentic systems is not entirely novel, but the way AAD wields it as a boundary condition is very precise. By defining agency at Level 2, the framework makes a hard ontological cut: prediction engines (LLMs without tool use, passive stock market algorithms) are not agents. They are trapped at Level 1. They can predict what happens next, but they cannot answer "what happens if *I* do this?" because they don't have a "do" operator hooked up to the environment.

This brings up a fascinating point about LLMs. An LLM *simulates* Level 2 and Level 3 reasoning perfectly in text. It can generate a story about "What if I had done X instead?" But this is an epistemic illusion. The LLM is performing Level 1 pattern matching on text that *describes* Level 3 reasoning. The map is not the territory. When AAD requires an agent to have Level 2 access, it requires actual causal coupling with $\Omega$, not just the linguistic representation of it. This is why the "Logogenic Agents" section exists: it has to bridge the gap between an engine that *simulates* causality (an LLM) and a framework that *requires* actual causal intervention (AAD). The moment you give an LLM a bash terminal, it drops from a simulated L3 god back down to a struggling L2 agent trying to figure out what `rm -rf` actually does in this specific environment.

The claim about software and `git checkout` is profound. In the physical world, Level 3 (Counterfactuals) is strictly imaginary. We can never actually go back in time, change our action, and see what would have happened. We can only simulate it internally in $M_t$. But in software, because the environment ($\Omega$) is a digital artifact with perfectly serialized state transitions, we *can* literally execute Level 3. We can branch the universe, run the counterfactual, observe the ground-truth result, and then merge the knowledge back into the main timeline without having committed to the action in production. This completely justifies TST's position as the "privileged calibration laboratory." It is the only domain where Level 3 is empirical rather than theoretical. But as noted above, this only holds if the software is referentially transparent (no side effects to un-versioned state).