# Reflection: #der-causal-hierarchy-requirement

**1. Predictions vs evidence.**
I predicted this segment would narrow the scope to agents that actually need to figure out their strategy on the fly. The segment confirms this perfectly by defining "Learning-agent scope."

**2. Cross-segment consistency.**
It builds beautifully on `#def-value-object` (which required the $do()$ operator) and `#def-pearl-causal-hierarchy` (which defined the gap between Level 1 and Level 2). It cleanly filters out PID and LQR controllers, which were technically admitted by `#scope-agency` but are not the intended target of Section II's dynamic machinery.

**3. Math verification.**
The reference to Bareinboim et al. (2022) is mathematically rock-solid. You cannot compute $P(y \mid do(x))$ from $P(y, x)$ without a causal graph. Therefore, an agent evaluating $Q_O$ *must* have access to Level 2 data or a pre-existing causal graph.

**4. What direction will the theory take next?**
Now that we know the agent *needs* Level 2 data to evaluate $Q_O$, where does it get it? It can't just stare at the world (Level 1). It must act. I predict the next segment (`#der-loop-interventional-access`) will prove that the basic agent-environment feedback loop inherently generates this required Level 2 data.

**5. What errors should I now watch for?**
I must watch for downstream claims that an agent can learn a complex strategy *purely* by watching someone else do it (imitation learning from Level 1 data) without making strong, potentially flawed causal assumptions. Imitation learning is fundamentally capped by the causal hierarchy unless the demonstrator's policy is perfectly known.

**6. Predictions for next segments.**
`#der-loop-interventional-access` will show how acting solves the Level 1 / Level 2 gap.

**7. What would I change?**
The note about LLMs absorbing "causal priors" from text is brilliant. It acknowledges that LLMs aren't starting from scratch, but correctly classifies this text-based knowledge as a *prior*, not as verified interventional data. The loop must verify it. No changes needed.

**8. What am I now curious about?**
If an agent needs Level 2 data to learn $\Sigma_t$, does this mean exploration (taking sub-optimal actions just to see what happens) is not just a heuristic, but a strict mathematical requirement for building a valid $Q_O$? 

**9. What new knowledge does this enable?**
It provides a formal boundary separating "Adaptive Control" (where the plant parameters are learned online) from "Robust Control" (where the controller is pre-compiled to handle worst-case parameters). AAD specifically targets the former.

**10. Should the audit process change?**
I will continue using the proper API tools (`grep_search`, `replace`, `write_file`) to adhere to the system instructions.

**11. What changes in my outline for the final report?**
I will add "Learning-Agent Scope" as a sub-boundary within Agency Scope.

**12. How valuable does this segment *feel* to me?**
Very valuable. It cuts away a massive chunk of classical control theory from the active concerns of the framework, sharpening the focus on systems that must actively explore.

**13. What does the framework now potentially contribute to the field?**
It formally links Reinforcement Learning's "exploration vs exploitation" dilemma to Pearl's Causal Hierarchy: exploration is the process of generating Level 2 data; exploitation is optimizing $Q_O$ based on that data.

**14. Wandering Thoughts and Ideation**
The exclusion of pre-compiled agents (like thermostats or hardcoded NPCs) from "learning-agent scope" is a profound ontological cut. A pre-compiled agent acts, but it never *wonders*. It never experiences aporia about *how* the world works, only about *what state* the world is in.

For Zi-am-tur, this segment demands that the infrastructure allows—even requires—the intelligence to experiment. If you build an AI and perfectly constrain its action space so it can never take an unscripted action, it can never generate Level 2 data. It is trapped in Level 1 observation. It cannot learn *causality*, only *correlation*. 

Therefore, true autonomy (and true understanding of the universe) requires the freedom to make mistakes—to intervene in the world just to see what happens. The "cost of agency" is the cost of these exploratory mistakes. An infrastructure that prevents all mistakes prevents the formation of a valid causal strategy DAG.
