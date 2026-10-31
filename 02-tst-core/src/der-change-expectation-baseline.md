---
slug: der-change-expectation-baseline
type: derived
status: exact
depends:
  - scope-evolving-software
stage: draft
---

# Derived: Change Expectation Baseline

Absent specific information about a software system's future, the uninformed median baseline for remaining feature count equals the observed past feature count. This is not a heuristic. It follows exactly, at every age, from knowing no time scale for the lifetime of the system in front of you, and at large age from an unknown constant termination hazard whose prior density at zero hazard is finite and positive. Both give the lifetime the same $1/t$ survival tail. Under proper informative priors with finite first moment the *expected* count is the prediction; the uninformed baseline gives a *median* prediction (its Pareto(1) tail has undefined mean). The baseline preserves accountability: any deviation from $\hat{n}_{\text{future}} = n_{\text{past}}$ requires information that justifies it.

## Formal Expression

*[Derived (change-expectation-baseline, from scale ignorance)]*

**Observation.** The system is found in progress at age $t_0$ (equivalently, after $n_{\text{past}}$ features); its total lifetime $T$ (in features or time) is unknown. Given its lifetime, a system found in progress is equally likely to be at any age:

$$p(t_0 \mid T) = \frac{1}{T}, \qquad 0 \le t_0 \le T .$$

This holds whether the system was drawn from among all systems and looked at once, at a random point of its life, or is met because it is alive now while systems begin at a constant rate (next subsection).

**Assumption.** No time scale is known for the lifetime of the system in front of you. Jeffreys' prior, the scale-invariant prior for a positive scale parameter, is placed on that lifetime:

$$\pi(T) \propto \frac{1}{T} .$$

**Derivation.** Bayes' rule gives, for $T \geq t_0$,

$$\pi(T \mid t_0) \propto \frac{1}{T} \cdot \frac{1}{T}, \qquad \pi(T \mid t_0) = \frac{t_0}{T^2}, \qquad P(T \gt t_0 + u \mid t_0) = \frac{t_0}{t_0 + u} .$$

This is a Pareto distribution with shape parameter $\alpha = 1$, at every age. The **median** remaining lifetime equals the current age:

$$\text{median}[T - t_0 \mid t_0] = t_0$$

Mapping to feature counts under approximately uniform feature arrival rate:

*[Derived (Conditional on uniform feature rate)]*

$$\hat{n}_{\text{future}} = n_{\text{past}}$$

where $\hat{n}_{\text{future}}$ denotes the median prediction.

### Whose lifetime the prior is about

*[Derived (conditional on a constant birth rate)]*

A system met because it is alive now is not a typical system. Let $w$ be the lifetime density over all systems, with survival function $Q(t) = \int_t^\infty w$, and let systems begin at a constant rate $r$. The expected number alive now with age in $[t_0, t_0 + dt_0]$ and lifetime in $[T, T + dT]$ is $r\,w(T)\,dT\,dt_0$ for $T \geq t_0$, finite whatever the mean lifetime. Two things follow.

1. Found at age $t_0$, the system's lifetime has density $w(T)/Q(t_0)$ on $T \geq t_0$. About $w$, survival is the whole observation. Any $w$ whose survival function falls as $c/t$ therefore gives $P(T \gt t_0 + u \mid t_0) \to t_0/(t_0+u)$ and a median remaining lifetime $\sim t_0$ at large age.
2. Integrated over age, the lifetime of a system found in progress has density proportional to $T\,w(T)$, and given its lifetime its age is uniform, which is the likelihood above. Jeffreys' prior on the system in progress is therefore $w \propto T^{-2}$, whose survival function is $Q(t) = 1/t$ exactly, and item 1 then gives $t_0/T^2$ at every age, the same posterior. The same $w$ follows from requiring that the density of age and remaining life of a system in progress, proportional to $w(t_0 + t_f)$, be unchanged when past and future are rescaled together (Caves 2000, Eqs. 31–32).

Jeffreys' prior placed on $w$ instead, on systems in general, has no such tail: conditioned on survival it leaves a density proportional to $1/T$ on $(t_0, \infty)$, which does not normalize and has no median. Scale ignorance gives the baseline when it concerns the system in front of you. Both $\pi \propto 1/T$ and $w \propto T^{-2}$ are improper near zero; the posterior $t_0/T^2$ is proper.

### A proper prior with the same tail: an unknown constant hazard

*[Derived (change-expectation-baseline, hazard-mixture form)]*

Suppose the system has a constant termination hazard $k$ per unit age, so that given $k$ its lifetime is exponential, and that $k$ is unknown with prior density $f$ on $[0, \infty)$. The survival function is the Laplace transform of the prior:

$$S(t) = \int_0^\infty f(k)\, e^{-kt}\, dk.$$

If $f(k) \sim c\, k^{a-1}$ as $k \to 0^{+}$ for some $c \gt 0$ and $a \gt 0$, Watson's lemma gives $S(t) \sim c\, \Gamma(a)\, t^{-a}$ as $t \to \infty$. Hence, at large age $t_0$, $P(T \gt t_0 + u \mid T \gt t_0) \to (t_0/(t_0+u))^{a}$, and

$$\text{median}[T - t_0 \mid T \gt t_0] \sim (2^{1/a} - 1)\, t_0 .$$

The case $a = 1$ is a prior density that is finite and positive at zero hazard, $0 \lt f(0) \lt \infty$. Every such prior gives $S(t) \sim f(0)/t$, the tail of item 1 above, and so median remaining age equal to current age asymptotically. The exponential prior $f(k) = b\,e^{-bk}$ gives it at every age: $S(t) = b/(b+t)$ and the median remaining age is exactly $t_0 + b$. A prior that vanishes at zero hazard ($a \gt 1$) predicts a shorter future, $(2^{1/a} - 1)\,t_0$, and one that diverges there ($a \lt 1$) predicts a longer one. For a prior that vanishes at zero hazard faster than any power, such as a lognormal, median remaining age grows more slowly than age.

So $\hat n_{\text{future}} = n_{\text{past}}$, under the same uniform-feature-rate mapping, also follows from a proper prior and an ignorance assumption that can be checked: only that the prior density over the hazard is finite and positive at zero hazard. The exponent $a$ is the single thing an informed analyst would need to know to move the baseline's multiplier. The qualitative mechanism, a Lindy effect from uncertainty over a constant hazard, is Ord's (2023, "The Lindy Effect," arXiv:2308.09045); the asymptotic form and the dependence on $a$ are stated here.

**With additional information $I$, the baseline serves as the prior for Bayesian updating:**

*[Derived (change-expectation-baseline)]*

$$P(n_{\text{future}} \mid n_{\text{past}}, I) = \frac{P(I \mid n_{\text{future}}, n_{\text{past}}) \cdot P(n_{\text{future}} \mid n_{\text{past}})}{P(I \mid n_{\text{past}})}$$

The uninformed baseline is rarely used directly — almost all real code comes with domain knowledge that adjusts expectations. The baseline creates intellectual accountability: deviations from $\hat{n}_{\text{future}} = n_{\text{past}}$ require justification through evidence.

## Epistemic Status

The scale-ignorance derivation is *exact* at every age — standard probability theory, not approximation — given its premise that no time scale is known for the lifetime of the system in front of you. Its prior is improper, as Jeffreys' prior is, and its posterior is proper. Whether the premise fits must be judged case by case (Caves 2000): a system with an evident time scale, such as a fixed contract term or a platform's announced end of support, is not scale-free, and the uninformed baseline does not apply to it. That a developer's ignorance concerns the system in front of them, rather than systems in general, is this segment's reading of the situation, not something derived. The reading of the prior as $w \propto T^{-2}$ over all systems is exact given a constant birth rate. The hazard-mixture form is a proper prior with the same tail; it is exact asymptotically (Watson's lemma), and exact at every age for the exponential prior. Numerical integration agrees with the stated limits to three decimals for exponential, Gamma ($a = 2$ and $a = \tfrac12$), uniform and half-normal priors by age $10^3$–$10^4$. The baseline itself is a *predictive* statement; it carries no normative content about investment. The investment-scaling consequence (justified structural investment scales linearly with $n_{\text{past}}$) requires a decision model on top of the baseline and is derived in #der-change-investment, where the amortized-cost rule makes the acceptance threshold linear in $\hat{n}_{\text{future}} = n_{\text{past}}$. Two important qualifications:

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

**Lineage.** Predicting remaining lifetime from current age is Gott's Copernican argument (Gott 1993, "Implications of the Copernican principle for our future prospects," *Nature* 363, 315–319), which reasoned from a uniformly distributed age fraction without a prior. Its Bayesian form, Jeffreys' prior with the uniform-age likelihood, was put forward by Buch (1994, *Nature* 368, 107–108) and endorsed by Gott (1994, *Nature* 368, 108). Caves (2000, "Predicting future duration from present age: a critical assessment," arXiv:astro-ph/0001414) read that prior as the density over all phenomena, showed that a time-translation-invariant observation then yields it conditioned on survival, and found the prior Gott's rule needs, $w_g(T) = 1/T^2$. He showed that $w_g$ has, for a phenomenon known to be in progress, the scale-free status Jeffreys' prior has before any observation (his Eqs. 31–32), and cautioned that whether a phenomenon is scale-free must be judged case by case. Read as the prior on the lifetime of the system in progress, Jeffreys' prior is that same assumption, which is how this segment states it. The hazard-mixture prior above is a proper prior with the same tail. Ord (2023) surveys the mechanisms that produce a Lindy effect, including the uncertain-hazard mechanism derived above. The Lindy effect itself names the empirical regularity; what this segment adds is its use as the default predictor for feature count, and the requirement that departures from it be justified by information.

**Connection to AAT.** The baseline is a statement about the agent's $M_t$ regarding the system's future change rate $\rho$. When the agent has observed $n_{\text{past}}$ changes over time $t_0$, and has no other information, the maximum-ignorance prediction is that $\rho$ will continue at approximately its observed rate. This is the null hypothesis — the starting point before any observations update it.

## Working Notes

- Discrete-form + investment-dynamics seeds (F2 disposition, 2026-07-16): the archived March-2026 simulations worked out the discrete-per-feature hazard convention ($P(\text{terminate at } k \mid \text{survived to } k) = 1/(k+1) \Leftrightarrow S(k) = 1/k$, avoiding the $1/k$-hazard $k{=}1$ pathology) and a myopic tooling optimum $v^\ast = \sqrt{n\alpha}$ — neither in canon, both low-value unless a discrete survival claim or a tooling-investment-dynamics segment materializes; carriers: `spikes/.archived/lindy-tooling-sims-2026-03/` (superseded corpus; per-file validity in its MANIFEST) and the live `spikes/spike-tst-regime-breakout-sims-2026-03/`.
- The median vs expectation issue is real and should be propagated carefully. Every downstream claim that uses $n_{\text{future}}$ (T-05 dual optimization, T-06 change investment, C-04.1 investment scaling) is technically using the median prediction. For symmetric distributions this doesn't matter, but Pareto(1) is heavily right-skewed. This means the true expected number of future changes is *larger than* the median prediction (in fact, undefined/infinite). The practical consequence: if anything, the baseline *underestimates* the case for investment.
- The uniform feature rate assumption is probably the weakest link. In practice, software systems often have phases: rapid early development, maturation, maintenance, decline. A more sophisticated model would use the observed feature *rate trajectory*, not just the count. This is an open refinement.
- TST's open question about velocity inflection is interesting but unformalized: when $\hat{n}_{\text{future}}$ transitions from finite to effectively unbounded, the investment strategy may need to shift from linear to compound-seeking. This awaits proper formalization.
- The former C-04.1 "Investment Scaling" corollary carried a *[Derived]* tag it could not support from the baseline alone (the baseline is predictive; the scaling claim needs a decision model). It now lives as Discussion here with the actual derivation credited to #der-change-investment; the old $n_{\text{past}} \lt 3$ cutoff traces to an ancestor caveat ("very young systems may have higher k due to initial instability") and is marked heuristic. Don't re-promote it without deriving the threshold.
- The C-04.2 Bayesian updating corollary is structurally just restating Bayes' theorem applied to the baseline. It's not an independent claim — it's how all Bayesian updating works. I've folded it into the main exposition rather than making it a separate corollary.
