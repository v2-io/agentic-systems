# Reflection: #scope-agency

**1. Predictions vs evidence.**
I predicted that having defined the broad scope of adaptive systems, the next step would be defining actuated agents. The segment confirms this, but specifically grounds "action" in Pearl's causal hierarchy. I expected "it can act," but the framework requires "its actions create an interventional difference."

**2. Cross-segment consistency.**
It logically intersects $\mathcal S_\text{adaptive}$ with a set of causal conditions. It correctly references `#def-action-transition`. The dependency on Pearl's $do(a)$ operator is a significant leap into causal inference that was foreshadowed but not explicit in the first few segments. I note a forward reference to `#def-pearl-causal-hierarchy`. Because this is a `depends:` violation (I haven't read that definition yet, and it's not an Appendix), I must log this as a minor finding in my scratchpad, though the concept is standard enough that I can proceed.

**3. Math verification.**
The condition $\exists\, a \neq a' \text{ s.t. } P(o \mid do(a)) \neq P(o \mid do(a'))$ correctly uses the $do(\cdot)$ operator to assert that the interventional distribution of observations must differ based on the action chosen.

**4. What direction will the theory take next?**
Now that we have scoped true agents, the framework needs to define what these agents are trying to achieve (Goals/Objectives) and how they decide which $do(a)$ to execute (Strategy/Policy). I expect segments on Goals ($O_t$) and Strategy ($\Sigma_t$).

**5. What errors should I now watch for?**
I need to watch for downstream claims that assume *all* actions in $\mathcal A$ have distinct causal effects. The scope only requires $\exists\, a \neq a'$. An agent might have 100 actions, but 98 of them are "nominal" (no effect). If a proof assumes full causal contrast across the entire action space, it will violate this minimal scope condition.

**6. Predictions for next segments.**
The framework will likely move to define the internal state of the agent. We know it has a chronica. It needs to compress that into a model $M_t$. I predict `#form-agent-model` or something similar.

**7. What would I change?**
I would explicitly state whether the difference in $P(o \mid do(a))$ must be *knowable* to the agent, or just objectively true in the universe. If it's objectively true but the agent's observation function $h$ is too noisy to detect it, is it still an agent? The math says yes, but pragmatically, it acts like a nominal agent.

**8. What am I now curious about?**
How does the framework handle action spaces that are continuous? The $\lvert\mathcal A\rvert \geq 2$ condition implies discrete actions, though standard measure theory could handle continuous. I'm curious if AAD strictly requires discrete choices.

**9. What new knowledge does this enable?**
It formally separates "learning" (Adaptive) from "steering" (Agency) using the language of causal inference. This allows AAD to import Pearl's theorems directly into Section II.

**10. Should the audit process change?**
I noted the forward-reference to `#def-pearl-causal-hierarchy`. I need to ensure I'm checking the `depends:` list *before* I read, as instructed in 4.3, rather than just noticing it in the text. *Self-correction: I will check `depends` before reading the next segment.*

**11. What changes in my outline for the final report?**
I will add a sub-point under "Foundational Scope Boundaries" for "The Causal Agency Boundary".

**12. How valuable does this segment *feel* to me?**
Very valuable. It prevents AAD from just being a re-hash of standard MDPs by forcing the requirement of causal contrast.

**13. What does the framework now potentially contribute to the field?**
By defining agency via the $do()$ operator, it provides a bridge between Reinforcement Learning (which focuses on maximizing reward) and Causal Inference (which focuses on understanding the mechanism). It suggests that to be an agent, you must be a causal engine.

**14. Wandering Thoughts and Ideation**
The requirement that $P(o \mid do(a)) \neq P(o \mid do(a'))$ is profound. It means that the definition of an agent depends on the responsiveness of the environment. If I am locked in a room where none of the buttons do anything (a "nominal agent"), AAD says I am effectively just an adaptive observer. My internal subjective experience of "trying" to act doesn't matter; the objective lack of causal contrast demotes my ontological status within the framework. 

This has massive implications for software agents (Logogenic). If an LLM outputs a string of text, and that text is piped to `/dev/null`, it is not an agent. If it is piped to a bash shell, it is an agent. The agency resides not just in the software, but in the *coupling* to an environment that respects the $do()$ operator. 

Furthermore, consider the "Placebo button" at a crosswalk. The button exists ($\mathcal A$), you can press it or not press it ($a \neq a'$). But the light changes on a timer regardless. $P(o \mid do(\text{press})) == P(o \mid do(\text{wait}))$. You are a nominal agent in that micro-environment. However, the *act* of pressing the button might change your internal state (frustration, satisfaction), which means your *internal* chronica differs. Does the observation $o$ include the proprioception of having acted? If $o_t$ includes $a_{t-1}$ (as defined in `#def-observation-function`), then $P(o \mid do(a))$ *always* differs from $P(o \mid do(a'))$ simply because you observe yourself taking different actions! 

This is a potential paradox. If I can observe my own actions, then every action has a distinct causal effect *on my observation stream*, even if it has no effect on $\Omega$. I need to look closely at `#def-observation-function` again. Yes, $o_t = h(\Omega_t, a_{t-1}, \varepsilon_t)$. If $h$ passes $a_{t-1}$ through cleanly, then $P(o \mid do(a))$ is trivially distinct from $P(o \mid do(a'))$. Therefore, to make `#scope-agency` non-vacuous, the causal effect must be on $\Omega$, not just on the proprioceptive part of $o$. The notation $P(o \mid do(a))$ might be hiding a subtle requirement that the difference must route *through* $\Omega$. I will note this as a potential "scope/status mismatch" or at least a necessary clarification for my final report.
