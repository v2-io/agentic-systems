# 53 - def-strategy-dag

Source: `01-aat-core/src/def-strategy-dag.md`

## First-pass understanding

This is the main formal strategy representation. `Sigma_t = (V_t,E_t,p_t,gamma_t)` is a time-unrolled causal DAG of propositional strategy nodes, single-parameter edge credences, and AND/OR node semantics. Leaf credences come from `M_t`; status propagation pushes those credences upward; the root status `P_hat_Sigma` is the plan's cheap self-assessment. The segment also separates this score from `A_O` and `V_O(pi_current)`, which is important for the later diagnostic split.

The strongest part is the correlation hierarchy. L0 independence is tractable but fragile; L1 augments strict common causes; L1' handles observable soft facilitators through mixtures; L2 is the full joint distribution and is generally too large. The segment is also careful about time-unrolling cycles and about the distinction between strategy DAGs and Moore machines: DAGs encode causal-plan interior, while automata encode behavioral surface.

## Diagram attempt

The useful diagram is a split view: the main DAG propagation path on one side and the correlation hierarchy on the other. I added a warning at the bridge from causal sufficiency to AND/OR propagation, because the segment sometimes treats causal sufficiency as enough for the product formulas. Causal sufficiency supports a Markov factorization, but the local AND/OR/noisy-edge parameterization is still an additional modeling choice.

## Findings and watches

- Candidate finding: the segment says AND/OR propagation is correct iff the strategy DAG is causally sufficient, and that causal sufficiency guarantees independent edge outcomes. Causal sufficiency/CMC gives conditional independence and a Markov factorization over variables, not the specific noisy-AND/noisy-OR product formulas or independent per-edge contribution model. Correct propagation also requires the local AND/OR parameterization to be true.
- Candidate finding: several places say causal insufficiency makes `P_hat_Sigma` systematically overestimate success. The correlation table itself shows this is topology-dependent: positive covariance makes OR estimates optimistic but AND estimates conservative. The blanket overestimation claim should be limited to OR-dominated redundancy structures.
- Update to earlier acyclicity concern: this segment properly states the time-unrolled/event-token condition for DAG acyclicity, including retry loops. The concern remains only for summary/intro wording that omits that condition.
- Watch: the single-root constraint fits scalar objective thresholds, but vector/Pareto or genuinely multi-terminal objectives need the earlier scalarization/AND-terminal workaround.
- Watch: L1' unobservable-common-cause rank/Cramer-Rao claims are proof-bearing and delegated to appendix/proposition material not yet read in outline order.

## Local verdict

This is a strong representation segment, and it handles several caveats directly. The main mathematical tightening is to distinguish three layers: causal sufficiency gives a causal Bayesian network factorization; AND/OR gives a chosen compact local parameterization; correlation hierarchy repairs violations of the independence assumptions in that compact parameterization.
