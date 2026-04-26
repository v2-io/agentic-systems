# Reflection: Information Bottleneck and Volatility

Segments read:
- `form-agent-model.md`
- `form-information-bottleneck.md`
- `def-model-sufficiency.md`
- `def-model-class-fitness.md`
- `form-event-driven-dynamics.md`

## 1. Specific Finding: Conflation of IB $\beta$ parameter with environment volatility ($\rho$)

In `01-aad-core/src/form-information-bottleneck.md`, the Discussion/Formal Expression claims:
> **Dependence on volatility.** The trade-off $\beta$ depends on environment volatility $\rho$:
> - **Volatile environments** (high $\rho$): favor aggressive compression (low $\beta$). Old information decays in relevance quickly, so retaining it wastes capacity.
> - **Stable environments** (low $\rho$): favor dense retention (high $\beta$). Historical information remains predictive, so discarding it loses value.

**Critique:** This is a fundamental misunderstanding of the Information Bottleneck (IB) objective. The IB Lagrangian is:
$$ \min_{\phi} \left[ I(M_t; \mathcal{C}_t) - \beta I(M_t; o_{t+1:\infty}) \right] $$

The parameter $\beta$ determines the agent's *preference* trade-off between memory/computation cost (rate) and prediction accuracy (distortion).
When the environment becomes volatile (high $\rho$), the joint distribution $P(\mathcal{C}_t, o_{t+1:\infty})$ changes: past events in $\mathcal{C}_t$ simply have *less mutual information* with future observations $o_{t+1:\infty}$.
Because old information no longer helps predict the future, retaining it increases the complexity cost $I(M_t; \mathcal{C}_t)$ *without* yielding any benefit in the predictive term $I(M_t; o_{t+1:\infty})$.
Therefore, the optimal compression $\phi^*$ will *naturally* discard old information in a volatile environment, **even if $\beta$ remains strictly constant.**

Claiming that $\beta$ must be lowered when $\rho$ is high is double-counting the effect. You only lower $\beta$ if you want to shift the agent's fundamental preference curve (e.g. if memory becomes relatively more expensive). The volatility of the environment is entirely captured by the mutual information terms themselves, not by the hyperparameter $\beta$.

This is an epistemic mismatch: it's claimed as `robust-qualitative` but it is mathematically confused. The structural dependence on $\rho$ happens inside the expectation of the mutual information, not via $\beta$.

## 2. Model Sufficiency
`def-model-sufficiency.md` defines $S(M_t) = 1 - \frac{I(\mathcal{C}_t; o_{t+1:\infty} \mid M_t, a_{t:\infty})}{I(\mathcal{C}_t; o_{t+1:\infty} \mid a_{t:\infty})}$.
This correctly simplifies to $S(M_t) = \frac{I(M_t; o_{t+1:\infty} \mid a_{t:\infty})}{I(\mathcal{C}_t; o_{t+1:\infty} \mid a_{t:\infty})}$, which is the standard fraction of retained predictive information. The formulation is solid.

## 3. Next steps
I will add this finding to the running outline.
Then I will read the next batch of segments:
- `def-mismatch-signal.md`
- `emp-update-gain.md`
- `def-adaptive-tempo.md`
- `hyp-mismatch-dynamics.md`
- `result-persistence-condition.md`
- `result-sector-condition-stability.md`