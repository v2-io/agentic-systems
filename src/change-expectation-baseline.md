---
slug: change-expectation-baseline
type: derived
status: exact
depends:
  - software-scope
---

# Change Expectation Baseline

Absent specific information about a software system's future, the best prediction for remaining feature count equals the observed past feature count. This is not a heuristic — it is the mathematical consequence of maximum ignorance. Any deviation requires information that justifies it.

## Formal Expression

*[Derived (change-expectation-baseline, from Jeffrey's prior)]*

**Assumption.** The total lifetime $T$ of the system (measured in features or time) is unknown. We adopt Jeffrey's prior — the unique scale-invariant prior expressing maximum ignorance about a positive scale parameter:

$$\pi(T) \propto \frac{1}{T}$$

**Derivation.** After observing survival to age $t_0$ (or equivalently, $n_{\text{past}}$ features), Bayesian update gives:

$$\pi(T \mid T \gt t_0) = \frac{t_0}{T^2}, \quad T \gt t_0$$

This is a Pareto distribution with shape parameter $\alpha = 1$. The **median** remaining lifetime equals the current age:

$$\text{median}[T - t_0 \mid T \gt t_0] = t_0$$

Mapping to feature counts under approximately uniform feature arrival rate:

*[Derived (Conditional on uniform feature rate)]*

$$\hat{n}_{\text{future}} = n_{\text{past}}$$

where $\hat{n}_{\text{future}}$ denotes the median prediction.

**With additional information $I$, the baseline serves as the prior for Bayesian updating:**

*[Derived (change-expectation-baseline)]*

$$P(n_{\text{future}} \mid n_{\text{past}}, I) = \frac{P(I \mid n_{\text{future}}, n_{\text{past}}) \cdot P(n_{\text{future}} \mid n_{\text{past}})}{P(I \mid n_{\text{past}})}$$

The uninformed baseline is rarely used directly — almost all real code comes with domain knowledge that adjusts expectations. The baseline creates intellectual accountability: deviations from $\hat{n}_{\text{future}} = n_{\text{past}}$ require justification through evidence.

### Corollary: Investment Scaling

*[Derived (investment-scaling, from change-expectation-baseline)]*

Investment in abstraction and flexibility should scale with $n_{\text{past}}$, since the expected return period equals the observed lifetime. Systems with minimal feature history ($n_{\text{past}} \lt 3$) warrant minimal structural investment.

## Epistemic Status

The Bayesian derivation from Jeffrey's prior is *exact* — standard probability theory, not approximation. Two important qualifications:

**Median, not expectation.** For Pareto($\alpha = 1$), the mean is undefined (the integral diverges). The result $\hat{n}_{\text{future}} = n_{\text{past}}$ is a *median* prediction. TST's original statement as $E[n_{\text{future}} \mid n_{\text{past}}] = n_{\text{past}}$ uses "expected" loosely. This distinction matters when propagating the estimate through nonlinear functions — the median of a function is not generally the function of the median. Downstream claims ( #change-investment, #dual-optimization) that use $n_{\text{future}}$ should be understood as using the median prediction, not the mathematical expectation.

**Uniform feature rate assumption.** The derivation gives remaining *lifetime*, not remaining *feature count*. Mapping time to features requires that features arrive at an approximately uniform rate over the system's history. If feature arrival accelerates (common in growing products) or decelerates (common in mature products), the mapping introduces bias. This assumption should be stated explicitly whenever the result is applied.

The Laplace succession formula ($E[n_{\text{future}} \mid n_{\text{past}}] = n_{\text{past}} + 1$ for small $n_{\text{past}}$) comes from a different model (beta-binomial with uniform prior on the success rate). It is a reasonable complement for small sample sizes but is not derived from the same prior as the main result.

## Discussion

**Intellectual accountability.** The baseline transforms architectural discussions. "We should abstract this" becomes "what information justifies $\hat{n}_{\text{future}} \gt n_{\text{past}}$ for this component?" Without an answer, the abstraction is premature — mathematically, not aesthetically. This is the Bayesian framework working as intended: strong claims about the future require strong evidence.

**Domain knowledge as Bayesian update.** Specific information adjusts the baseline:
- "This is UI code" → higher change probability than algorithms
- "We're sunsetting next quarter" → $\hat{n}_{\text{future}} \to 0$
- "This connects to a volatile API" → $\hat{n}_{\text{future}}$ likely $\gt n_{\text{past}}$
- "This is a sorting algorithm" → $\hat{n}_{\text{future}} \to 0$ (approaching the stable-subsystem regime of #software-scope)

Each of these is an observation that updates the agent's model $M_t$ about the system's future. The gain applied to these updates ( #update-gain) depends on how reliable the information source is — a product roadmap from an engaged PM carries more weight ($\eta^*$ closer to 1) than a vague feeling about market direction.

**Connection to ACT.** The baseline is a statement about the agent's $M_t$ regarding the system's future change rate $\rho$. When the agent has observed $n_{\text{past}}$ changes over time $t_0$, and has no other information, the maximum-ignorance prediction is that $\rho$ will continue at approximately its observed rate. This is the null hypothesis — the starting point before any observations update it.

## Working Notes

- The median vs expectation issue is real and should be propagated carefully. Every downstream claim that uses $n_{\text{future}}$ (T-05 dual optimization, T-06 change investment, C-04.1 investment scaling) is technically using the median prediction. For symmetric distributions this doesn't matter, but Pareto(1) is heavily right-skewed. This means the true expected number of future changes is *larger than* the median prediction (in fact, undefined/infinite). The practical consequence: if anything, the baseline *underestimates* the case for investment.
- The uniform feature rate assumption is probably the weakest link. In practice, software systems often have phases: rapid early development, maturation, maintenance, decline. A more sophisticated model would use the observed feature *rate trajectory*, not just the count. This is an open refinement.
- TST's open question about velocity inflection (old-tst-04 discussion section) is interesting but unformalized: when $\hat{n}_{\text{future}}$ transitions from finite to effectively unbounded, the investment strategy may need to shift from linear to compound-seeking. This awaits proper formalization.
- The C-04.2 Bayesian updating corollary is structurally just restating Bayes' theorem applied to the baseline. It's not an independent claim — it's how all Bayesian updating works. I've folded it into the main exposition rather than making it a separate corollary.

*(Descended from TST T-04, C-04.1, C-04.2.)*
