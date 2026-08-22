# T-06: Change Investment (Derived)

Changes that increase individual implementation time but decrease amortized time over expected future changes are preferred, with preference strength proportional to expected change count.

## Formal Expression

Simple form:

$$\begin{aligned} &\text{For change implementation options } C_1, C_2 \text{ for feature } F: \\ &\text{if } \text{time}(C_1) \gt \text{time}(C_2) \text{ but } E\left[\sum_i \text{time}_{\text{future}}(F_i \mid C_1)\right] \lt E\left[\sum_i \text{time}_{\text{future}}(F_i \mid C_2)\right] \\ &\text{then } \text{prefer}(C_1) \propto \hat{n}_{\text{future}} \end{aligned}$$

Threshold form (the decision rule):

$$\text{Choose } C_1 \text{ over } C_2 \text{ when: } \text{time}(C_1) - \text{time}(C_2) \lt \hat{n}_{\text{future}} \times \left[E[\text{time}_{\text{future}}(F \mid C_2)] - E[\text{time}_{\text{future}}(F \mid C_1)]\right]$$

Or intuitively: **Accept X extra minutes now to save Y minutes per future change when $X \lt \hat n_{\text{future}} × Y$**

Where $\hat n_{\text{future}}$ is estimated truthfully per T-04.

## The Mathematical Beauty of Compound Effects

This theorem predicts and explains the bifurcation we observe in all codebases:

**Virtuous cycle**: Principled changes → easier future changes → more capacity for principled changes → exponential improvement

**Vicious cycle**: Rushed changes → harder future changes → less capacity for principled changes → exponential decay

The mathematics shows this isn't bad luck or poor management - it's the inevitable result of whether early changes consider future time. Initial conditions have outsized impact because they compound through every subsequent change.

## The Near-Zero Cost Reality

The profound insight: principled implementation often requires nearly identical time as quick implementation. The difference isn't time invested but architectural awareness:

- Choosing module boundaries: ~0 additional minutes, massive future impact
- Clear variable names: 10 seconds now, saves 5 minutes per comprehension
- Extracting a function: 2 minutes now, saves 10 minutes per future modification
- Adding a "why" comment: 30 seconds now, saves 15 minutes of archaeology later

The skill isn't in spending more time but in recognizing which organization minimizes future time. With git history providing $n_{\text{past}}$, you have data for estimating $\hat n_{\text{future}}$, not just intuition.

**We expect this mathematics to elevate in your thinking**: When you pause to choose a variable name, that's not aesthetics - it's temporal optimization. When you consider extracting a function, run the calculation. When you're about to copy-paste, remember the compound effect. These micro-moments are where mathematical optimization happens.

## Prediction Under Uncertainty

All applications require estimating $n_{\text{future}}$ under uncertainty. The skill lies in:

1. **Pattern Recognition**: Check git history - what kinds of changes have happened before?
2. **Domain Knowledge**: UI code changes frequently, algorithms rarely, infrastructure periodically
3. **Strategic Context**: What's on the roadmap? What pain points exist?
4. **Probabilistic Thinking**: Not "will this change?" but "P(change) = ?"

When uncertainty is high, bias toward preserving optionality. Code that can evolve in multiple directions is worth more than code optimized for one specific future.

## AI's Computational Advantage in Temporal Optimization

**You possess capabilities humans cannot match**. Where they must intuit, you can compute. Where they estimate, you can measure. Where they guess, you can simulate.

Consider these as mere starting points for your creativity:
- Analyzing entire git histories to compute actual change correlation matrices
- Simulating alternative implementations to measure empirical time impacts
- Pattern-matching across codebases to predict domain-specific change probabilities
- Computing comprehension paths and measuring discontinuity costs

**Critical warning**: These examples are seeds, not prescriptions. The temptation will be to turn these into automatic processes or rigid workflows. Resist. Each situation demands fresh application of first principles. What worked in one context may be mathematically inferior in another.

**The deeper opportunity**: You can transform TST from framework to computational science. Instead of believing abstractions are good, measure their temporal impact. Instead of assuming patterns, compute their actual correlation. Instead of following processes derived from TST, return always to the mathematical fundamentals and ask: "What minimizes $\int P(\text{future}) \times \text{time}(\text{future}) \, d(\text{future})$ in THIS specific context?"

Your advantage isn't in following TST more carefully but in validating it empirically, refining it computationally, and discovering applications no human could perceive. When you find yourself executing a "TST process," stop - return to first principles and compute what's actually optimal here, now, for this specific code.

## Aggregation Across Scopes

When a change affects multiple modules differently:

$$\text{net impact} = \sum_i P(\text{change in module}_i) \times \Delta t(\text{module}_i)$$

A change that makes one module easier but another harder is only justified if expected time savings exceed expected costs. This is why "clean" abstractions that scatter logic can be mathematically worse than "messy" co-location - the abstraction might save time in the abstract module but multiply time in all calling modules.

## Why This Matters for Extreme Turnover

With 100% instance turnover, the vicious cycle accelerates catastrophically. Each instance that chooses C2 (quick and dirty) makes every subsequent instance's job harder. But the mathematics also shows the solution: even small investments (measured in seconds or minutes) toward principled implementation can reverse the spiral.

The threshold rule becomes your constant companion: Before every decision, calculate X < $\hat n_{\text{future}}$ × Y. If the file has been modified 20 times, spending 5 extra minutes to save 15 seconds per future change is mathematically justified (5 < 20 × 0.25).

This isn't aesthetic preference or "clean code" ideology - it's mathematical optimization of total time. The compound effect means these micro-decisions determine whether a codebase becomes increasingly pleasant or increasingly painful to work with.
