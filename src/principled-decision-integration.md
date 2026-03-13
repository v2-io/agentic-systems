---
slug: principled-decision-integration
type: derived
status: conditional
depends:
  - temporal-optimality
  - dual-optimization
  - conceptual-alignment
  - changeset-size-principle
  - change-proximity-principle
---

# Derived: Principled Decision Integration

The optimal implementation choice minimizes total expected time across all probable future features, integrating all temporal factors simultaneously.

## Formal Expression

*[Derived (principled-decision-integration, from temporal-optimality)]*

For implementation choices $\mathbf{C}$ for the current feature:

$$C^* = \operatorname{argmin}_{C \in \mathbf{C}} \; E[T \mid C]$$

where total expected time given choice $C$ is:

$$E[T \mid C] = t_0(C) + \sum_{i} P(F_i) \cdot \left[ t_{\text{comp}}(F_i \mid C) + t_{\text{impl}}(F_i \mid C) \right]$$

This is the general form of #dual-optimization. Where dual-optimization uses a single "typical future feature" $F_{\text{typical}}$ with count $\hat n_{\text{future}}$, this integrates over the full distribution of possible future features $F_i$ with their individual probabilities $P(F_i)$.

Substituting the proportional relationships from #conceptual-alignment, #changeset-size-principle, and #change-proximity-principle:

$$E[T \mid C] = t_0(C) + \sum_{i} P(F_i) \cdot \left[ \frac{\alpha \cdot h(\text{disc}(F_i \mid C))}{\text{alignment}(C)} + \beta \cdot |\text{cs}(F_i \mid C)| \cdot g(\text{prox}(F_i \mid C)) \right]$$

where $\alpha, \beta$ are empirical proportionality constants, $h$ and $g$ encode the (possibly exponential, per #exponential-cognitive-load) cost relationships, and $\text{disc}$, $\text{cs}$, $\text{prox}$ are the discontinuity count, changeset size, and proximity for feature $F_i$ under choice $C$.

## Epistemic Status

*Derived* from #temporal-optimality — the optimization is the direct application of the least-time postulate to the full cost structure. *Conditional* on the proportional relationships from #conceptual-alignment (hypothesis), #changeset-size-principle (empirical), and #change-proximity-principle (conditional). The expanded form inherits the weakest epistemic status of its inputs: the alignment term is discussion-grade, the proximity cost function is uncertain in form. The integration structure itself is exact; the terms being integrated are approximate.

The full optimization is intractable in practice — it requires knowing the probability distribution of all future features and the exact impact of current decisions on future costs. The practical value is as a decision *framework* that structures the tradeoff space, not as a computable optimum.

## Discussion

**Relationship to dual-optimization.** This is the general case; #dual-optimization is the single-feature-type approximation. The approximation is good when future features are roughly homogeneous. When different feature types have very different cost profiles (e.g., a system that handles both UI changes and data pipeline changes), the full integration reveals tradeoffs the approximation misses — an architecture optimal for one feature type may be suboptimal for another.

**Dominant-factor analysis.** Perfect integration is impossible, but recognizing which factors dominate is usually tractable. Under high turnover, $t_{\text{comp}}$ dominates $t_{\text{impl}}$ (the #dual-optimization turnover multiplier). For a well-aligned codebase, alignment contributes little and changeset size dominates. For a highly modular system, proximity is less of an issue than for a monolith. Identifying the dominant factor reduces the full optimization to a simpler one.

## Working Notes

- TST T-11 includes a rich expanded form with empirical constants $\alpha$ and $\beta$ that convert proportionalities to equalities. These constants are codebase-specific and not derived. In practice, relative comparisons (architecture A vs B) may not need absolute constants — the proportionalities suffice for ordering.
- The summation over $P(F_i)$ assumes the feature distribution is known or estimable. In practice, this is where the agent's $M_t$ does the real work — predicting not just *how many* future features ( #change-expectation-baseline) but *what kind*. The quality of this prediction is bounded by the agent's model quality, connecting back to #model-sufficiency.
- This segment might be better positioned as a discussion/synthesis rather than a standalone derived claim, since it mostly assembles previously stated results into a composite objective. Its independent contribution is the explicit per-feature probability weighting, which dual-optimization elides.

*(Descended from TST T-11.)*
