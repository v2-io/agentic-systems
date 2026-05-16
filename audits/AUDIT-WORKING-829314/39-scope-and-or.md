# Reflection: 39-scope-and-or

**1. Predictions vs evidence:** I predicted this would formalize the difference between AND-nodes and OR-nodes to show how OR-nodes mitigate chain confidence decay. It does exactly this, providing the strict mathematical combination rules for AND (product of probabilities) and OR (complement of product of complements).

**2. Cross-segment consistency:** Good dependencies (`def-strategy-dimension`, `der-chain-confidence-decay`). It nicely motivates the restriction to an AND/OR basis via bounded cognition constraints (`#form-information-bottleneck`) and forward-references `#deriv-graph-structure-uniqueness`.

**3. Math verification:** The equations for AND and OR are the standard probabilistic definitions for independent events. The table showing the catastrophic failure of "Noisy-OR" to represent an AND-gate ($0.99995$ vs $0.846$) is a powerful, undeniable demonstration of why the formalism needed this scope narrowing.

**4. What direction will the theory take next?** The next segment is `def-strategy-dag.md`.

**5. What errors should I watch for?** The text defends the AND/OR basis by stating that "any Boolean combination can be decomposed into layers of AND/OR (disjunctive/conjunctive normal form)." While true in formal logic, the Working Notes acknowledge that doing so for a "k-of-n" threshold is incredibly verbose (requiring $\binom{n}{k}$ branches). If the agent is strictly bounded by Description Length ($DL$), forcing it to use verbose DNF for k-of-n logic might cause the strategy to exceed its cognitive capacity (e.g., an LLM context window). This is a tension between the parsimony of the *node taxonomy* and the parsimony of the *graph size*.

**6. Predictions for next segment:** `def-strategy-dag.md` will formally define $\Sigma_t$ as a Directed Acyclic Graph where nodes are subgoals/actions, edges are causal links with probabilities (credences), and each node is typed as AND or OR.

**7. What would I change?** I would elevate the "K-of-n thresholds" note from the Working Notes to the main Discussion. It is a severe practical limitation of the pure AND/OR basis when operating under strict MDL constraints.

**8. Curious about:** How does the agent update the topology of the DAG (adding/removing nodes) versus updating the edge probabilities ($p_{iv}$)? The text hints that $\gamma$ reclassification (switching a node from AND to OR) is rare and operates on a slower timescale.

**9. What new knowledge does this enable?** The explicit rejection of universal Noisy-OR (often used in Bayesian networks) in favor of a strict AND/OR dichotomy for purposeful strategy representation, preventing "illusory confidence" in sequential plans.

***

### Wandering Thoughts and Ideation

The rejection of Noisy-OR as a universal gate is a fascinating design choice that separates AAD from standard probabilistic graphical models. In many Bayesian networks (like medical diagnosis), Noisy-OR is used everywhere because it scales nicely ($O(k)$ parameters instead of $2^k$) and captures the intuition that "any of these diseases could independently cause this symptom." 

But as the segment brilliantly points out, if you use Noisy-OR to model a strategy where *all* prerequisites are strictly required (like "Get key" AND "Unlock door" to achieve "Open door"), the math breaks down catastrophically. If you are 90% sure you have the key and 95% sure you unlocked the door, a Noisy-OR gate calculates your chance of the door being open as $1 - (1-0.9)(1-0.95) = 0.995$. It makes you *more* confident than either prerequisite alone! This is mathematically suicidal for a planner. An AND gate correctly calculates $0.9 \times 0.95 = 0.855$. You are *less* confident.

This proves that strategies ($\Sigma_t$) are not just Bayesian belief networks ($M_t$) turned sideways. The logic of causation in a plan is much more brittle than the logic of evidence in a diagnosis. If one piece of evidence is missing, a diagnosis might still be highly probable. If one required step is missing, a plan fails with probability 1. 

The tension between node-type parsimony (only having 2 types, AND/OR) and graph-size parsimony ($DL$) is very real. If an agent wants to represent "I need 3 out of 5 servers to be healthy to launch," building that in pure AND/OR normal form requires $\binom{5}{3} = 10$ separate AND-branches feeding into a massive OR-node. That's a huge spike in description length $DL(\Sigma_t)$. I suspect that as AAD evolves, it will be forced to introduce a native "k-of-n" node type simply to satisfy the Information Bottleneck constraint derived in `#form-strategy-complexity-cost`. You cannot afford combinatorial explosion in your working memory.