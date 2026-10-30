---
slug: der-change-expectation-baseline
type: derived
status: exact
depends:
  - scope-evolving-software
stage: draft
---

# Derived: Change Expectation Baseline

Absent specific information about a software system's future, the uninformed median baseline for remaining feature count equals the observed past feature count. This is not a heuristic. It follows exactly, at large age, from conditioning on the system's survival whenever the prior over its lifetime has a survival function falling as $1/t$. An unknown constant termination hazard gives that tail whenever its prior density at zero hazard is finite and positive. Under proper informative priors with finite first moment the *expected* count is the prediction; the uninformed baseline gives a *median* prediction (its Pareto(1) tail has undefined mean). The baseline preserves accountability: any deviation from $\hat{n}_{\text{future}} = n_{\text{past}}$ requires information that justifies it.

## Formal Expression

*[Derived (change-expectation-baseline)]*

**Assumption.** The total lifetime $T$ of the system (measured in features or time) is unknown, with prior survival function $Q(t) = P(T \gt t)$, and

$$Q(t) \sim \frac{c}{t} \quad (t \to \infty), \qquad c \gt 0 .$$

**Assumption (observation).** The system is observed because it is alive at the observer's time, which is uniform over a span much longer than lifetimes. It is not drawn once from among all systems and observed at a uniform point of its own life; that other sampling is the subject of the last subsection below. This segment takes the first to be a developer's situation with the system in front of them.

**Derivation.** The system is found in progress at age $t_0$ (equivalently, after $n_{\text{past}}$ features). Under that observation model, finding it is equally likely for every lifetime $T \geq t_0$, so the observation rules out lifetimes shorter than $t_0$ and leaves the prior otherwise unchanged:

$$P(T \gt t_0 + u \mid T \gt t_0) = \frac{Q(t_0 + u)}{Q(t_0)} \;\to\; \frac{t_0}{t_0 + u} \qquad (t_0 \to \infty).$$

This is a Pareto tail with shape parameter $\alpha = 1$. At large age the **median** remaining lifetime equals the current age:

$$\text{median}[T - t_0 \mid T \gt t_0] \sim t_0$$

Mapping to feature counts under approximately uniform feature arrival rate:

*[Derived (Conditional on uniform feature rate)]*

$$\hat{n}_{\text{future}} = n_{\text{past}}$$

where $\hat{n}_{\text{future}}$ denotes the median prediction.

### Where a $1/t$ tail comes from: an unknown constant hazard

*[Derived (change-expectation-baseline, hazard-mixture form)]*

Suppose the system has a constant termination hazard $k$ per unit age, so that given $k$ its lifetime is exponential, and that $k$ is unknown with prior density $f$ on $[0, \infty)$. The survival function is the Laplace transform of the prior:

$$S(t) = \int_0^\infty f(k)\, e^{-kt}\, dk.$$

If $f(k) \sim c\, k^{a-1}$ as $k \to 0^{+}$ for some $c \gt 0$ and $a \gt 0$, Watson's lemma gives $S(t) \sim c\, \Gamma(a)\, t^{-a}$ as $t \to \infty$. Hence, at large age $t_0$, $P(T \gt t_0 + u \mid T \gt t_0) \to (t_0/(t_0+u))^{a}$, and

$$\text{median}[T - t_0 \mid T \gt t_0] \sim (2^{1/a} - 1)\, t_0 .$$

The case $a = 1$ is a prior density that is finite and positive at zero hazard, $0 \lt f(0) \lt \infty$. Every such prior gives $S(t) \sim f(0)/t$, the tail the baseline assumes, and so median remaining age equal to current age asymptotically. The exponential prior $f(k) = b\,e^{-bk}$ gives it at every age: $S(t) = b/(b+t)$ and the median remaining age is exactly $t_0 + b$. A prior that vanishes at zero hazard ($a \gt 1$) predicts a shorter future, $(2^{1/a} - 1)\,t_0$, and one that diverges there ($a \lt 1$) predicts a longer one. For a prior that vanishes at zero hazard faster than any power, such as a lognormal, median remaining age grows more slowly than age.

So $\hat n_{\text{future}} = n_{\text{past}}$, under the same uniform-feature-rate mapping, rests on an ignorance assumption that can be checked: only that the prior density over the hazard is finite and positive at zero hazard. The exponent $a$ is the single thing an informed analyst would need to know to move the baseline's multiplier. The qualitative mechanism, a Lindy effect from uncertainty over a constant hazard, is Ord's (2023, "The Lindy Effect," arXiv:2308.09045); the asymptotic form and the dependence on $a$ are stated here.

### Jeffreys' prior, and which observation it needs

*[Derived (conditional on per-system sampling)]*

Jeffreys' prior $\pi(T) \propto 1/T$, the scale-invariant prior for a positive scale parameter, has no $1/t$ survival tail: conditioned on survival alone it leaves a density proportional to $1/T$ on $(t_0, \infty)$, which does not normalize and has no median. It yields the baseline only with a second premise, the uniform-age likelihood $p(t_0 \mid T) = 1/T$ for $T \gt t_0$, which gives the posterior $t_0/T^2$ exactly at every age. That likelihood describes per-system sampling: each system is observed once, at a uniformly random point of its own life. The observation assumed above is the other kind: the system is observed because it is alive at the observer's time. If that time is uniform over a window of length $\Delta$ much longer than lifetimes, finding the system alive at age $t_0$ has density $1/\Delta$ for every $T \geq t_0$: longer lives are more likely to be found in progress, which cancels the $1/T$. The likelihood is then flat in $T$ above $t_0$, the observation amounts to survival to $t_0$, and the derivation above applies. Under that sampling, scale ignorance alone gives no baseline, and the baseline rests on the $1/t$ tail.

**With additional information $I$, the baseline serves as the prior for Bayesian updating:**

*[Derived (change-expectation-baseline)]*

$$P(n_{\text{future}} \mid n_{\text{past}}, I) = \frac{P(I \mid n_{\text{future}}, n_{\text{past}}) \cdot P(n_{\text{future}} \mid n_{\text{past}})}{P(I \mid n_{\text{past}})}$$

The uninformed baseline is rarely used directly — almost all real code comes with domain knowledge that adjusts expectations. The baseline creates intellectual accountability: deviations from $\hat{n}_{\text{future}} = n_{\text{past}}$ require justification through evidence.

## Epistemic Status

The survival-conditioning derivation is *exact* — standard probability theory, not approximation — as an asymptotic statement in age, given its two premises: a prior survival function falling as $1/t$, and a system observed because it is alive now. That the second describes a developer facing a system is this segment's reading of the situation, not something derived. The hazard-mixture form says which priors over a constant hazard supply that premise; it is exact asymptotically (Watson's lemma), and exact at every age for the exponential prior. The Jeffreys derivation is exact at every age given its two premises, the scale-invariant prior and per-system sampling; it does not apply to a system observed because it is alive now. Numerical integration agrees with the stated limits to three decimals for exponential, Gamma ($a = 2$ and $a = \tfrac12$), uniform and half-normal priors by age $10^3$–$10^4$. The baseline itself is a *predictive* statement; it carries no normative content about investment. The investment-scaling consequence (justified structural investment scales linearly with $n_{\text{past}}$) requires a decision model on top of the baseline and is derived in #der-change-investment, where the amortized-cost rule makes the acceptance threshold linear in $\hat{n}_{\text{future}} = n_{\text{past}}$. Two important qualifications:

**Median, not expectation.** For Pareto($\alpha = 1$), the mean is undefined (the integral diverges). The result $\hat{n}_{\text{future}} = n_{\text{past}}$ is a *median* prediction. TST's original statement as $E[n_{\text{future}} \mid n_{\text{past}}] = n_{\text{past}}$ uses "expected" loosely. This distinction matters when propagating the estimate through nonlinear functions — the median of a function is not generally the function of the median. Downstream claims ( #der-change-investment, #der-dual-optimization) that use $n_{\text{future}}$ should be understood as using the median prediction, not the mathematical expectation.

**Uniform feature rate assumption.** The derivation gives remaining *lifetime*, not remaining *feature count*. Mapping time to features requires that features arrive at an approximately uniform rate over the system's history. If feature arrival accelerates (common in growing products) or decelerates (common in mature products), the mapping introduces bias. This assumption should be stated explicitly whenever the result is applied.

The Laplace succession formula ($E[n_{\text{future}} \mid n_{\text{past}}] = n_{\text{past}} + 1$ for small $n_{\text{past}}$) comes from a different model ($\beta$-binomial with uniform prior on the success rate). It is a reasonable complement for small sample sizes but is not derived from the same prior as the main result.

## Discussion

**Intellectual accountability.** The baseline transforms architectural discussions. "We should abstract this" becomes "what information justifies $\hat{n}_{\text{future}} \gt n_{\text{past}}$ for this component?" Without an answer, the abstraction is premature — mathematically, not aesthetically. This is the Bayesian framework working as intended: strong claims about the future require strong evidence.

**Domain knowledge as Bayesian update.** Specific information adjusts the baseline:
- "This is UI code" → higher change probability than algorithms
- "We're sunsetting next quarter" → $\hat{n}_{\text{future}} \to 0$
- "This connects to a volatile API" → $\hat{n}_{\text{future}}$ likely $\gt n_{\text{past}}$
- "This is a sorting algorithm" → $\hat{n}_{\text{future}} \to 0$ (approaching the stable-subsystem regime of #scope-evolving-software)
- "We are rewriting this onto a new architecture" → the past count no longer describes the system whose future is being predicted. When $P(F_{\text{future}} \mid S_{\text{old}}) \neq P(F_{\text{future}} \mid S_{\text{new}})$, the rewrite is itself information $I$, and it usually dominates the uninformed prior. The baseline says nothing about which way.

Each of these is an observation that updates the agent's model $M_t$ about the system's future. The gain applied to these updates ( #emp-update-gain) depends on how reliable the information source is — a product roadmap from an engaged PM carries more weight ($\eta^\ast$ closer to 1) than a vague feeling about market direction.

**Investment scaling.** *[Discussion]* Combining the baseline with the amortized-cost decision rule of #der-change-investment yields the qualitative reading commonly attached to it: justified investment in abstraction and flexibility scales with $n_{\text{past}}$, because the acceptance threshold $X \lt \hat n_{\text{future}} \times Y$ is linear in $\hat n_{\text{future}} = n_{\text{past}}$. The derivation lives in that segment, not here — the baseline alone is predictive, not normative. The rule of thumb that very young systems ($n_{\text{past}} \lesssim 3$) warrant minimal structural investment is heuristic-grade: it marks the small-sample regime where the Laplace correction and initial instability dominate, not a derived threshold.

**Lineage.** Predicting remaining lifetime from current age is Gott's Copernican argument (Gott 1993, "Implications of the Copernican principle for our future prospects," *Nature* 363, 315–319), which reasoned from a uniformly distributed age fraction without a prior. Its Bayesian form, Jeffreys' prior with the uniform-age likelihood, was put forward by Buch (1994, *Nature* 368, 107–108) and endorsed by Gott (1994, *Nature* 368, 108). Caves (2000, "Predicting future duration from present age: a critical assessment," arXiv:astro-ph/0001414) showed that the uniform-age likelihood presupposes finding the phenomenon in progress, that a time-translation-invariant observation instead yields the prior conditioned on survival, and so that Gott's rule needs a prior density falling as $1/T^2$. The hazard-mixture prior above is a proper prior with that tail. Ord (2023) surveys the mechanisms that produce a Lindy effect, including the uncertain-hazard mechanism derived above. The Lindy effect itself names the empirical regularity; what this segment adds is its use as the default predictor for feature count, and the requirement that departures from it be justified by information.

**Connection to AAT.** The baseline is a statement about the agent's $M_t$ regarding the system's future change rate $\rho$. When the agent has observed $n_{\text{past}}$ changes over time $t_0$, and has no other information, the maximum-ignorance prediction is that $\rho$ will continue at approximately its observed rate. This is the null hypothesis — the starting point before any observations update it.

## Working Notes

- Discrete-form + investment-dynamics seeds (F2 disposition, 2026-07-16): the archived March-2026 simulations worked out the discrete-per-feature hazard convention ($P(\text{terminate at } k \mid \text{survived to } k) = 1/(k+1) \Leftrightarrow S(k) = 1/k$, avoiding the $1/k$-hazard $k{=}1$ pathology) and a myopic tooling optimum $v^\ast = \sqrt{n\alpha}$ — neither in canon, both low-value unless a discrete survival claim or a tooling-investment-dynamics segment materializes; carriers: `spikes/.archived/lindy-tooling-sims-2026-03/` (superseded corpus; per-file validity in its MANIFEST) and the live `spikes/spike-tst-regime-breakout-sims-2026-03/`.
- The median vs expectation issue is real and should be propagated carefully. Every downstream claim that uses $n_{\text{future}}$ (T-05 dual optimization, T-06 change investment, C-04.1 investment scaling) is technically using the median prediction. For symmetric distributions this doesn't matter, but Pareto(1) is heavily right-skewed. This means the true expected number of future changes is *larger than* the median prediction (in fact, undefined/infinite). The practical consequence: if anything, the baseline *underestimates* the case for investment.
- The uniform feature rate assumption is probably the weakest link. In practice, software systems often have phases: rapid early development, maturation, maintenance, decline. A more sophisticated model would use the observed feature *rate trajectory*, not just the count. This is an open refinement.
- TST's open question about velocity inflection is interesting but unformalized: when $\hat{n}_{\text{future}}$ transitions from finite to effectively unbounded, the investment strategy may need to shift from linear to compound-seeking. This awaits proper formalization.
- The former C-04.1 "Investment Scaling" corollary carried a *[Derived]* tag it could not support from the baseline alone (the baseline is predictive; the scaling claim needs a decision model). It now lives as Discussion here with the actual derivation credited to #der-change-investment; the old $n_{\text{past}} \lt 3$ cutoff traces to an ancestor caveat ("very young systems may have higher k due to initial instability") and is marked heuristic. Don't re-promote it without deriving the threshold.
- The C-04.2 Bayesian updating corollary is structurally just restating Bayes' theorem applied to the baseline. It's not an independent claim — it's how all Bayesian updating works. I've folded it into the main exposition rather than making it a separate corollary.
