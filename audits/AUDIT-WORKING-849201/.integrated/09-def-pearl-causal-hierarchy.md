# Reflection on `def-pearl-causal-hierarchy`

**1. Predictions vs evidence:**
I predicted the segment would formally define Pearl's three levels (Association, Intervention, Counterfactual) and state that AAD agents require Level 2. It delivered exactly this, using standard $do$-calculus notation.

**2. Cross-segment consistency:**
The dependencies (`post-causal-structure`, `scope-agency`) are correct. The forward reference to TST's `obs-software-epistemic-properties` regarding `git checkout` is a brilliant cross-domain connection that justifies TST's existence.

**3. Math verification:**
The mathematical notation for the three levels ($P(y|x)$, $P(y|do(x))$, $P(y_{x'} | x, y)$) is standard and correctly applied to the agent's observation/action streams.

**4. What direction will the theory take next?**
The OUTLINE lists `#form-agent-model` next. We have finished defining the "raw materials" (the environment, the loop, the chronica, the causal structure) and are now moving to the agent's internal cognitive architecture: how it compresses the chronica into a usable state $M_t$.

**5. What errors should I now watch for?**
**CRITICAL FINDING POTENTIAL:** The segment explicitly cites the Causal Hierarchy Theorem (Bareinboim et al. 2022): Level 2 cannot be computed from Level 1 data alone. I must rigorously check any future claims about agents *learning* action consequences ($Q$-values, strategy DAG edges). If a derivation claims an agent learns $P(o \mid do(a))$ purely by passively observing another agent or a dataset (Level 1) without making strong causal assumptions, it violates this theorem.

**6. Predictions for next segments:**
`#form-agent-model` will define $M_t = \phi(\mathcal{C}_t)$, where $\phi$ is a compression function. It will likely state that an ideal model is a sufficient statistic for the predictive information in $\mathcal{C}_t$.

**7. What would I change?**
Nothing. The domain instantiation table at the bottom is extremely helpful for intuition.

**8. What am I now curious about?**
I am curious how the theory will handle the *cost* of accessing Level 3 in domains other than software, where simulation is required and therefore fidelity is uncertain.

**9. What new knowledge does this enable?**
It grounds abstract causal graphs in the physical, temporal reality of an embodied agent. The realization that `git checkout` is a literal, ground-truth Level 3 operation perfectly justifies why software is the privileged testbed for AAD.

**10. Should the audit process change?**
No.

**12. Value feeling:**
Very high. This connects AAD to a massive body of mature external math.

**13. Contribution:**
Bridges control theory (feedback loops) and causal inference (Pearl's hierarchy).