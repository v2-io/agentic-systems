# Reflection: def-strategy-dag

**1. Predictions vs evidence.**
I predicted the formalization of $\Sigma_t$ as an AND/OR graph with edge credences. The segment confirms exactly this: $\Sigma_t = (V_t, E_t, p_t, \gamma_t)$.

**2. Cross-segment consistency.**
It perfectly integrates the objective $O_t$ (as the terminal satisfaction condition) and the Part I adaptive machinery (via the leaf base credences updating as $M_t$ updates). The careful scoping of edge credences $p_{ij}$ into Regimes A, B, and C (from `scope-ciy-observational-proxy`) maintains strict theoretical hygiene.

**3. Math verification.**
The analysis of the "Correlation Hierarchy" is spectacular. The proof that assuming independence (L0) in a causally insufficient DAG causes AND nodes to underestimate success by exactly $+\rho$ (the covariance of the unmodeled common cause) and OR nodes to overestimate success by $-\rho$ is mathematically flawless. Because real-world plans typically have OR-structure near the root (multiple ways to succeed), this proves that naive planning algorithms *systematically overestimate* their probability of success in complex environments.

**4. What direction will the theory take next?**
Because this segment references multiple foundational derivations, I will read `deriv-graph-structure-uniqueness.md` and `deriv-edge-credence-dynamics.md` next.

**5. What errors should I now watch for?**
I must watch for downstream claims that an agent can easily compute its true probability of success. $\hat P_\Sigma$ is explicitly a biased heuristic (optimistic) unless the DAG is perfectly causally sufficient (L0) or correctly augmented (L1/L1').

**6. Predictions for next segments.**
`deriv-graph-structure-uniqueness` will use the Causal Markov Condition to prove that a DAG is the correct representation. `deriv-edge-credence-dynamics` will map the persistence condition ($\alpha > \rho/R$) to the update rules for the individual edge credences $p_{ij}$.

**7. What would I change?**
Nothing. The comparison between Moore Machines (behavioral surface) and Strategy DAGs (epistemic interior) is the clearest explanation of the difference between Reactive Policy and Causal Planning I have ever encountered. A Moore machine says *what* to do; a DAG says *why*. You cannot do strategy revision if you don't know why you are doing what you are doing.

**8. What am I now curious about?**
The composition of conflicting Strategy DAGs. The text proves that if Agent A and Agent B have conflicting causal orders ($A \prec B$ vs $B \prec A$), there is no exact macro-strategy. Instead, the framework condenses the Strongly Connected Component (SCC) into a single macro-node, destroying a bounded amount of information ($\le \lvert S \rvert \log 2$). This is a formal mathematical statement of why cross-team alignment is lossy but bounded.

**9. What new knowledge does this enable?**
It provides the formal data structure for "plans" that allows them to be evaluated, updated, and composed using the rigorous math of causal inference.

**10. Should the audit process change?**
No, executing the Appendix exception rule.

**11. What changes in my outline for the final report?**
Note the L0/L1/L1'/L2 Correlation Hierarchy as the formal taxonomy of planning errors in partially observed environments.

**12. How valuable does this segment feel to me?**
Extraordinarily valuable. This is the core data structure of Part II.

**13. What does the framework now potentially contribute to the field?**
It mathematically proves why project managers systematically underestimate risk (because they model plans as L0 OR-trees and ignore latent common-cause covariance).
