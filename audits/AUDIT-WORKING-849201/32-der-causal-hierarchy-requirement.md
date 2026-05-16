# Reflection on `der-causal-hierarchy-requirement`

**1. Predictions vs evidence:**
My prediction was that this segment would formally connect planning ($\Sigma_t$) to Pearl's Causal Hierarchy, stating that an agent cannot construct a valid $\Sigma_t$ unless its model $M_t$ supports Level 2 (interventional) queries: $P(o \mid do(a))$. The segment confirmed this exactly, explicitly relying on the Causal Hierarchy Theorem (Bareinboim et al. 2022).

**2. Cross-segment consistency:**
The dependencies are solid. It explicitly narrows the scope of Section II to "learning purposeful agents," explicitly excluding pre-compiled agents like PID controllers or pure LQR. This is a very clean theoretical move, ensuring that the rest of Section II doesn't have to constantly add asterisks for agents that don't actually learn causal structures.

**3. Math verification:**
The mathematical reliance on the Causal Hierarchy Theorem is correct. You cannot compute $P(y \mid do(x))$ from observational data $P(x,y)$ without making strong, untestable causal assumptions (like the absence of unobserved confounders). Therefore, an agent that evaluates $Q_O$ from experience *must* have a mechanism for acquiring Level 2 data.

**4. What direction will the theory take next?**
Now that the theory has proven that the agent *needs* Level 2 data to evaluate its strategy, it must explain *how* the agent gets that data. The OUTLINE lists `#der-loop-interventional-access` next.

**5. What errors should I now watch for?**
I must watch for any claims that an agent can learn its strategy DAG purely by passively watching other agents or reading static text, unless it is explicitly acknowledged that this requires importing external causal priors (as mentioned in the Working Notes regarding LLMs).

**6. Predictions for next segments:**
`#der-loop-interventional-access` will prove that the standard agent-environment feedback loop naturally provides Level 2 data because the agent's own actions are, by definition, interventions. The agent controls $a_t$, severing the back-door paths that would normally confound observational data.

**7. What would I change?**
Nothing. The explanation of why $Q(s,a)$ in RL is an interventional query $\mathbb{E}[R \mid s, do(a)]$ rather than an observational one $\mathbb{E}[R \mid s, A=a]$ is one of the clearest explanations of RL's causal foundations I have read.

**8. What am I now curious about?**
How does the agent know if its action actually caused the outcome, vs a simultaneous environmental shift ($\rho$)?

**9. What new knowledge does this enable?**
It formally defines why learning a strategy is fundamentally harder (and requires different data) than just building a predictive model of the world.

**10. Should the audit process change?**
No.

**12. Value feeling:**
Extremely satisfying integration of Pearl's causality.

**13. Contribution:**
Proves that planning requires interventional capability.