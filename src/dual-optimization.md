---
slug: dual-optimization
type: derived
status: conditional
depends:
  - temporal-optimality
  - comprehension-time
  - implementation-time
  - change-expectation-baseline
  - software-scope
---

# Derived: Dual Optimization

A principled implementation decision minimizes both comprehension time and implementation time for future features, weighted by how many future features are expected.

## Formal Expression

*[Derived (dual-optimization, from temporal-optimality + software-scope)]*

For implementation choice $C$ of the current feature, the time-optimal choice minimizes total median-predicted future time:

$$C^* = \operatorname{argmin}_{C} \left[ t_0(C) + \hat{n}_{\text{future}} \cdot \left( t_{\text{comp}}(F_{\text{typical}} \mid C) + t_{\text{impl}}(F_{\text{typical}} \mid C) \right) \right]$$

where $t_0(C)$ is the immediate cost of choice $C$, and $\hat{n}_{\text{future}}$ is the median prediction from #change-expectation-baseline.

This follows from #temporal-optimality (minimize total time) applied to the lifecycle cost structure of #software-scope (future costs dominate), with the feature time decomposition from #comprehension-time and #implementation-time.

### The turnover multiplier

*[Derived (Conditional on turnover rate)]*

When $k$ distinct agents (human developers or AI instances) will each need to comprehend the code:

$$\text{total comprehension cost} \approx t_{\text{comp}} \times k$$

where $k = (1 + r) \times s$ for team size $s$ and turnover rate $r$ over the relevant horizon. With 100% AI context turnover, $k$ equals the number of sessions that touch the relevant code. Comprehension cost compounds per-reader; implementation cost does not.

## Epistemic Status

*Conditional* on #temporal-optimality and #change-expectation-baseline. The derivation is straightforward: if you accept that total time should be minimized (postulate) and that future feature count is predicted by the baseline (derived), then the dual optimization follows by applying the postulate to the decomposed cost structure. The turnover multiplier follows from the observation that comprehension is per-reader while implementation (of a specific feature) is per-feature.

The quantitative form inherits the assumptions of #change-expectation-baseline: median prediction (not expectation — the mean is undefined for Pareto($\alpha = 1$)), uniform feature rate. The median-case optimization is conservative: the true expected future cost is *larger* than the median prediction (in fact, unbounded), so if anything this underestimates the case for investment.

## Discussion

**When comprehension and implementation conflict.** Sometimes they pull in opposite directions:
- Abstraction can speed implementation but slow comprehension (indirection cost)
- Explicit code can speed comprehension but slow implementation (more code to write)
- DRY principles can reduce implementation sites but increase comprehension indirection

The resolution depends on $\hat{n}_{\text{future}}$ and the turnover rate. Under high turnover (especially 100% context turnover per AI instance), comprehension cost dominates — bias toward comprehensibility. Code that a fresh agent can understand in minutes is worth more than code that saves implementation time.

**Practical implications for AI-maintained code.** When $k$ is very large (many AI sessions touching the code), the comprehension term dominates overwhelmingly. This is not a style preference — it is the mathematical consequence of the turnover multiplier. Explicit code, linear control flow, local comprehensibility, and intent-revealing names are temporal optimizations.

## Working Notes

- The "typical future feature" $F_{\text{typical}}$ is an idealization. Real futures have a distribution of feature types, and the optimal choice $C^\ast$ may depend on which features are more likely. #principled-decision-integration addresses this with the full probabilistic formulation. This simpler form is the single-feature-type approximation.
- TST's original T-05 includes a rich discussion of the AI turnover problem (redundant implementations, inconsistent patterns, half-completed features abandoned at context limit). These are real failure modes but they're consequences of high comprehension cost, not independent claims. They belong in worked examples or the Section V treatment of AI agents, not here.
- The turnover multiplier assumes each reader pays the full comprehension cost independently. In practice, good documentation and code structure can amortize comprehension across readers (each reader benefits from the last reader's improvements). This is the #code-quality-as-observation-infrastructure feedback loop — but it's not formalized yet.
- Connection to #information-bottleneck: the turnover multiplier means that for AI-maintained code, the IB tradeoff should favor retention (high $\beta$) — keep the model detailed and explicit, because the cost of re-deriving compressed information is paid by every future session.

*(Descended from TST T-05.)*
