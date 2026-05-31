# Reflection: causal-access-intro

**1. Predictions vs evidence.**
I predicted the segment would introduce the necessity of Pearl Level 2 (Interventional) data for planning, and argue that the agent's feedback loop generates this data. The introduction perfectly confirms this, establishing it as a load-bearing architectural claim.

**2. Cross-segment consistency.**
It ties together `def-value-object` ($Q_O$ requiring $do(a)$) and the mismatch mechanics from Part I. The connection back to earlier TST lessons ("confidence can indicate limitation") is a beautiful example of cross-volume coherence.

**3. Math verification.**
The unified policy objective $\pi^\ast = \arg\max [\text{Value} + \lambda \cdot \text{CIY}]$ is stated, but immediately qualified as a heuristic that is vulnerable to the "blank-wall attack" (maximizing scalar information in directions orthogonal to environmental drift). The mention of the Matrix-LMI strengthening to fix this shows the framework is mathematically mature enough to spot and plug holes in classic RL exploration bonuses.

**4. What direction will the theory take next?**
The next segment is `def-pearl-causal-hierarchy.md`, which will formally import Pearl's three levels.

**5. What errors should I now watch for?**
I must watch for downstream claims that assume on-policy learning is unbiased. The text explicitly names "confounded positive feedback" (superstition, gambling addiction, survivorship bias) as a structural failure mode of AAT agents: because a confounded *win* reduces uncertainty $U_M$, it drops the update gain $\eta^\ast$, cementing the false belief permanently. The agent only learns from errors (aporia); it never questions successes.

**6. Predictions for next segments.**
`def-pearl-causal-hierarchy` will be a direct import of external theory, defining $P(y|x)$ (L1), $P(y|do(x))$ (L2), and $P(y_{x'}|x,y)$ (L3).

**7. What would I change?**
Nothing. The "acts but never wonders" description of pre-compiled controllers (like a thermostat or LQR) is the perfect intuitive boundary for the "Learning-Agent Scope". It separates agents that *have* a strategy from agents that *form* a strategy.

**8. What am I now curious about?**
The Matrix-LMI strengthening (`deriv-causal-ib-lmi`). If an agent must maximize CIY specifically in the subspace where $\rho$ (drift) is high, it needs a matrix representation of both CIY and $\rho$. This perfectly parallels the matrix-Loewner persistence condition from Chapter 4.

**9. What new knowledge does this enable?**
It grounds the exploration/exploitation tradeoff not as an ad-hoc heuristic, but as a structural necessity arising from the Causal Hierarchy Theorem.

**10. Should the audit process change?**
No.

**11. What changes in my outline for the final report?**
Note the "Tragedy of Agency" (confounded wins causing permanent false beliefs due to gain decay) as a major finding of the framework.

**12. How valuable does this segment feel to me?**
Very high. It's the best philosophical justification for RL exploration I have encountered.

**13. What does the framework now potentially contribute to the field?**
It formalizes why "superstition" is not a bug in animal psychology, but an inevitable mathematical consequence of fast learning in partially confounded environments.
