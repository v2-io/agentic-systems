# Reflection: 46-hyp-edge-update-via-gain

**1. Predictions vs evidence:** I predicted it would propose that the update mechanism used for the epistemic model $M_t$ (gain-scaled mismatch) applies to the probabilities $p_{ij}$ on the strategy edges. It does exactly this: $p_{ij}^{\text{new}} = p_{ij}^{\text{old}} + \eta_{\text{edge}} \cdot (\text{signal} - p_{ij}^{\text{old}})$.

**2. Cross-segment consistency:** Excellent dependencies (`def-strategy-dag`, `emp-update-gain`, `def-mismatch-signal`). It correctly references `#der-observability-dominance`, `#def-strategic-calibration`, and `#disc-credit-assignment-boundary`. It integrates perfectly with the log-confidence decay (`#der-chain-confidence-decay`).

**3. Math verification:** The Beta-Bernoulli conjugate update $\Delta\hat{p} = (y - \hat{p})/(n+1)$ is mathematically exact for binomial data. The log-odds formulation $\lambda_{ij}^{\text{new}} = \lambda_{ij}^{\text{old}} + \ell(y)$ is the exact Bayesian update for independent evidence (the log-likelihood ratio update). The connection between these two coordinate systems (probability space vs log-odds space via the sigmoid function) is rigorous and standard in statistics.

**4. What direction will the theory take next?** The next segment is `scope-edge-update-causal-validity.md`.

**5. What errors should I watch for?** The text mentions a "gradient-based candidate" for the signal function: $\text{signal}_k = p_k + J_k \cdot (y_G - \hat{P}_\Sigma) / \|J\|^2$. This looks like standard backpropagation through the DAG. I must watch how `#disc-credit-assignment-boundary` handles the non-differentiable nature of discrete AND/OR logic when applying this gradient.

**6. Predictions for next segment:** `scope-edge-update-causal-validity.md` will define exactly when it is safe to interpret the updated edge probability $p_{ij}$ as a true causal effect $P(j \mid do(i))$, tying back into Regimes A, B, and C from earlier segments.

**7. What would I change?** The writing in the "Parallel log-odds presentation" is slightly dense but extremely precise. I wouldn't change the math, but a simple numerical example of a log-odds update would ground it better for non-statisticians.

**8. Curious about:** The Working Notes mention that the problem of "$M_t$/edge evidence double-counting" was analyzed in a spike and found to be "mostly unfounded" because the two updates extract different information from the same observation. This is a very subtle point of epistemic hygiene.

**9. What new knowledge does this enable?** The realization that the "obvious" proportional blame heuristic for unobservable intermediate failures is actually exactly the optimal marginal Bayesian update, but that this optimal marginal update is inherently biased when plugged back into an independent-edge DAG.

***

### Wandering Thoughts and Ideation

The realization that the optimal marginal Bayesian update is biased under unobservability is a devastating mathematical truth for bounded agents.

Imagine a 2-step plan ($A \to B \to G$). You try the plan, and it fails at the end ($G=0$). You couldn't observe $B$. Whose fault was it? $A$ or $B$? 
- A naive engineer might say: "Let's blame them proportionally based on their prior failure rates."
- A sophisticated statistician might say: "Let's compute the exact posterior marginal probability of $A$ and $B$ failing given $G=0$, and use those as our new point estimates."

AAD points out that *these are the exact same thing*, and furthermore, that *they are both structurally biased*. When $G$ fails, $A$ and $B$ become anti-correlated in the true posterior ("explaining away": if I know $A$ definitely failed, $B$ is off the hook). If you just extract the new marginal point estimates for $A$ and $B$ and plug them back into your independent-edge DAG ($\Sigma_t$), you have violently discarded that anti-correlation. Your new DAG is now structurally wrong (an $O(1/n)$ bias). 

This proves that bounded agents (who must compress their complex joint beliefs into simple DAGs with independent scalar edges to save $DL$) are mathematically doomed to mis-calibrate when learning from delayed or unobservable outcomes. You simply cannot compress a joint posterior into independent marginals without leaking truth. The only cure is to physically change the world so you can observe $B$ (`#der-observability-dominance`). You cannot math your way out of bad sensors.

This also provides strong theoretical justification for why modern neural networks use backpropagation (which computes exact gradients over the full joint structure) rather than local Hebbian learning or marginal Bayesian updates. To do credit assignment correctly without observability, you must preserve the joint correlation structure (the gradients). If you treat the nodes independently, you accumulate $O(1/n)$ bias on every step until the network freezes.