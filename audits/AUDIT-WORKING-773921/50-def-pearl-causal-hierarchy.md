# Reflection: def-pearl-causal-hierarchy

**1. Predictions vs evidence.**
I predicted the segment would formally import Pearl's three levels (Associational, Interventional, Counterfactual). It does exactly this, cleanly separating what AAT borrows (the hierarchy) from what AAT contributes (the application to agent architecture).

**2. Cross-segment consistency.**
The Working Notes explain that this segment was moved from Part I to Part II on 2026-05-12. This perfectly explains the anomaly I noticed back in `scope-agency.md` (which was in Part I but referenced this segment as living in Part II). The framework's internal cross-referencing is remarkably healthy. 

**3. Math verification.**
The notation $P(o_t \mid \mathcal{C}_{\lt t})$, $P(o_t \mid do(a_{t-1}), M_{t-1})$, and $P(o_t^{a'} \mid a_{t-1} = a, o_t = o)$ is standard and correct. The invocation of Bareinboim et al. 2022 (The Causal Hierarchy Theorem) is the load-bearing step: L2 cannot be derived from L1 data alone.

**4. What direction will the theory take next?**
The next segment is `der-causal-hierarchy-requirement.md`, which will formalize the implication of the CHT for agent planning.

**5. What errors should I now watch for?**
I must ensure that downstream derivations don't claim to compute regret (Level 3) without explicitly having a mechanism for counterfactual simulation.

**6. Predictions for next segments.**
`der-causal-hierarchy-requirement` will prove that because $Q_O$ (from `def-value-object`) requires the $do(\cdot)$ operator, an agent cannot learn to plan purely by passively observing a confounded environment. It *must* act to generate L2 data.

**7. What would I change?**
Nothing. The insight that `git checkout` provides *literal Level 3 counterfactuals* for software development is one of the most profound domain-transfer insights in the whole framework. In the real world, L3 requires a mental model (simulation). In software, L3 can be run on the actual physical substrate.

**8. What am I now curious about?**
How does the agent estimate $P(o_t \mid do(a))$ when it's just starting out and has no interventional data? Does it assume L1 $\approx$ L2 as a heuristic until proven wrong?

**9. What new knowledge does this enable?**
It provides the formal vocabulary for why passive prediction (like next-token prediction in base LLMs) is mathematically insufficient for optimal decision-making in confounded environments.

**10. Should the audit process change?**
No.

**11. What changes in my outline for the final report?**
Note the Causal Hierarchy Theorem (CHT) as the mathematical barrier between observing and planning.

**12. How valuable does this segment feel to me?**
Very. It correctly scopes AAT's use of causality as an imported tool rather than an invented one.

**13. What does the framework now potentially contribute to the field?**
It maps Pearl's hierarchy onto practical agent capabilities (Kalman vs RL vs Software Dev).
