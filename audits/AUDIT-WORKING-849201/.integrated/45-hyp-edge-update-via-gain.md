# Reflection on `hyp-edge-update-via-gain`

**1. Predictions vs evidence:**
My prediction was that this segment would propose that the credence $p_{ij}$ on a strategy edge updates via a mismatch signal modulated by a gain $\eta^\ast$, mirroring the epistemic update of $M_t$. The segment delivered exactly this: $p_{ij}^{\text{new}} = p_{ij}^{\text{old}} + \eta_{\text{edge}} \cdot (\text{signal} - p_{ij}^{\text{old}})$, where $\eta_{\text{edge}} = U_{\text{edge}} / (U_{\text{edge}} + U_{\text{obs}})$.

**2. Cross-segment consistency:**
The cross-referencing is excellent. The explicit connection to `#der-observability-dominance` (when $U_{\text{obs}} \to \infty$, $\eta_{\text{edge}} \to 0$, freezing the edge) mathematically grounds the previous segment's qualitative claim. The reference to the "credit-assignment problem" from `#def-strategic-calibration` is handled cleanly by abstracting it into the $\text{signal}(o_t, i, j)$ function, separating the *amount* of learning ($\eta$) from the *direction* of learning (signal).

**3. Math verification:**
The Beta-Bernoulli instantiation is mathematically standard and correct. A Beta prior $\text{Beta}(\alpha, \beta)$ updated with a Bernoulli observation yields a posterior mean update exactly equal to $\Delta\hat p = (y - \hat p)/(n+1)$. The segment correctly notes that while $1/(n+1)$ shares the *structural principle* of the Kalman variance-ratio gain (decreasing as certainty increases), it is algebraically distinct because Bernoulli noise is not Gaussian. The introduction of the log-odds coordinate $\lambda_{ij}$ as the unique additive space for independent evidence is mathematically rigorous and ties back beautifully to `#der-chain-confidence-decay`.

**4. What direction will the theory take next?**
Now that we have the mathematical update rule for edges, we need to know whether these updates actually converge to true causal probabilities or just associational correlations. The OUTLINE lists `#scope-edge-update-causal-validity` next.

**5. What errors should I now watch for?**
I must ensure that when the theory discusses edge updates under partial observability (where the agent only sees the final outcome $y_G$), it does not claim the updates are unbiased. The Working Notes explicitly state that proportional-blame updates for unobservable intermediates are biased at truth with $O(1/n)$ bias.

**6. Predictions for next segments:**
`#scope-edge-update-causal-validity` will formalize the regimes (A, B, C) under which the edge updates $\Delta\hat p$ converge to true causal interventional probabilities $P(do(x))$ versus just associational probabilities $P(x)$, likely depending on the degree of intervention vs observation.

**7. What would I change?**
Nothing. The defense of the "double-counting" critique (updating both $M_t$ and $\Sigma_t$ from the same observation) is well-reasoned: they are extracting different information (world state vs causal link validity) and the cascade ordering prevents pathological feedback loops.

**8. What am I now curious about?**
I am curious about the continuous-gradient update mechanism mentioned in the text for the log-odds space.

**9. What new knowledge does this enable?**
It provides the exact numerical update rule for the agent's strategy DAG.

**10. Should the audit process change?**
No.

**12. Value feeling:**
Very solid. The transition from abstract principles to concrete Beta-Bernoulli and log-odds math is excellent.

**13. Contribution:**
Formalizes how plans learn from experience.