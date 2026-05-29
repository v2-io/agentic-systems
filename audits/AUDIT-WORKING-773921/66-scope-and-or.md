# Reflection: scope-and-or

**1. Predictions vs evidence.**
I predicted the segment would define the standard conjunctive and disjunctive probability rules for the Strategy DAG. The segment confirms this, explicitly defining the Noisy-AND and Noisy-OR formulas.

**2. Cross-segment consistency.**
It perfectly references the "Parsimony argument" from the appendices (`deriv-graph-structure-uniqueness`), maintaining the epistemically honest stance that AND/OR is a formulation choice (not a derived necessity) motivated by bounded cognition (Information Bottleneck). 

**3. Math verification.**
The Noisy-AND ($\prod p_i$) and Noisy-OR ($1 - \prod(1 - p_i)$) formulas correctly assume independence between parents. The table showing how applying Noisy-OR to a conjunctive constraint yields an absurdly optimistic $0.99995$ success probability instead of the correct $0.846$ is a pristine mathematical refutation of the earlier "clean-slate" formalisms that tried to get away with just one combination rule.

**4. What direction will the theory take next?**
The next segment is `impl-strategy-structure.md`, the concluding discussion segment for Chapter 3.

**5. What errors should I now watch for?**
The text notes that interaction effects (synergies, complementary goods) are excluded by this scope. I must watch for any downstream claims that AAT can easily model highly synergistic environments without additional mathematical lifting. 

**6. Predictions for next segments.**
`impl-strategy-structure` will synthesize the chapter's major theoretical beats: the AND/OR DAG structure, the Correlation Hierarchy (L0-L2), and the Diagnostic Split (Satisfaction Gap vs Control Regret).

**7. What would I change?**
Nothing. The insight in the Working Notes that the assignment $\gamma(v) \in \{\text{AND}, \text{OR}\}$ can itself be updated, but on a much slower timescale than the edge weights $p_{ij}$, is a brilliant callback to `der-temporal-nesting`. It frames "realizing a task has alternative paths" not as a parameter update, but as a structural paradigm shift.

**8. What am I now curious about?**
The "k-of-n thresholds" discussion. The theory says you can build them by nesting ANDs and ORs, but admits it's verbose. In practice, a threshold node might be a cleaner primitive. I'm curious if empirical applications of AAT will stick to strict AND/OR or invent a new "Threshold" primitive.

**9. What new knowledge does this enable?**
It completes the operational mechanics required to actually evaluate the value object $V_O$ over a strategy graph.

**10. Should the audit process change?**
No.

**11. What changes in my outline for the final report?**
Note the exclusion of strong interaction effects (synergy/complementarity) as a formal scope boundary.

**12. How valuable does this segment feel to me?**
Very. It provides the concrete arithmetic rules for the abstract strategy graph.

**13. What does the framework now potentially contribute to the field?**
It provides a minimal, boundedly-rational Boolean basis for calculating plan success probabilities.
