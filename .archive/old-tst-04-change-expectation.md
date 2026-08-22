# T-04: Change Expectation Baseline (Fundamental)

Absent specific information about a software system's future, the expected number of future feature additions equals the observed number of past features added. With additional information, this serves as the baseline to adjust from.

## Formal Expression

$$\begin{aligned} &\text{With no information: } E[n_{\text{future}} \mid n_{\text{past}}] = n_{\text{past}} \\ &\text{With information } I: E[n_{\text{future}} \mid n_{\text{past}}, I] = n_{\text{past}} \times \text{adjustment}(I) \end{aligned}$$

For small $n_{\text{past}}$ (Laplace succession):
$$E[n_{\text{future}} \mid n_{\text{past}}] = n_{\text{past}} + 1$$

**Notational Convention**: Throughout this document, $n\_\text{future}$ denotes the actual (unknown) number of future features, while $\hat n_{\text{future}}$ denotes our estimate/expectation used for decision-making. In practice, $\hat n_{\text{future}} = E[n_{\text{future}} \mid \text{available information}]$.$

## Mathematical Foundation (Not Empirical!)

This emerges from Bayesian inference with Jeffrey's prior - the unique scale-invariant prior expressing maximum ignorance:

$$\rho(T) \propto \frac{1}{T}$$

After observing survival to time $t_0$, Bayesian update yields:

$$\rho(T|T \gt t_0) = \begin{cases} 0 & \text{if } T \leq t_0 \\ \frac{t_0}{T^2} & \text{if } T \gt t_0 \end{cases}$$

This is Pareto distribution with $\alpha = 1$, giving:

$$\text{Median[remaining lifetime]} = \text{current age} = t_0$$

## Why This Isn't a Heuristic

When you assume anything OTHER than $n_{\text{future}} = n_{\text{past}}$, you're claiming knowledge you don't possess. This is the mathematical consequence of honest ignorance - the null hypothesis of temporal prediction.

Any deviation requires information:
- "This is UI code" → Higher change probability than algorithms
- "We're sunsetting next quarter" → $n_{\text{future}} \to 0$
- "This connects to volatile API" → $n_{\text{future}}$ likely $\gt n_{\text{past}}$
- "This is a sorting algorithm" → $n_{\text{future}} \to 0$, infinite velocity!

The framework creates intellectual accountability. When someone says "we should abstract this," the response becomes: "What information justifies $n_{\text{future}} \gt n_{\text{past}}$?" Without an answer, the abstraction is premature.

## Corollary C-04.1: Investment Scaling with Observed History

Investment in abstraction and flexibility should scale proportionally with $n_{\text{past}}$, as the expected return period equals the observed lifetime. Systems with minimal feature history (e.g., $n_{\text{past}} \lt 3$) warrant minimal structural investment, as the expected future is similarly brief.

## Corollary C-04.2: Bayesian Updating from Baseline

With specific information $I$, the baseline serves as the prior for Bayesian updating:
$$P(n_{\text{future}} | n_{\text{past}}, I) = \frac{P(I | n_{\text{future}}, n_{\text{past}}) \cdot P(n_{\text{future}} | n_{\text{past}})}{P(I | n_{\text{past}})}$$

The uninformed baseline is rarely used directly - almost all real code comes with domain knowledge that adjusts expectations ("UI changes frequently," "this is a sorting algorithm," "we're exploring product-market fit"). The baseline creates intellectual accountability: deviations from $n_{\text{future}} = n_{\text{past}}$ require justification.

## Discussion: Open Question - The Velocity Inflection

When projects transition from finite to effectively unbounded $\hat n_{\text{future}}$ (however that manifests - validation, investment, mandate), a critical dynamic emerges that warrants future investigation.

Exploratory simulations suggest a structural tension: as features accumulate, some form of complexity-driven resistance appears to grow (call it entropy, though this needs formalization). Linear improvements in tooling/refactoring may be insufficient to maintain velocity against this resistance. The simulations hint that only compound improvements - where current investment amplifies future investment effectiveness - maintain velocity long-term.

This creates a potential inflection point: when $\hat n_{\text{future}}$ shifts from finite to unbounded, the investment strategy may need to shift from linear to compound-seeking. The timing appears cruel - external pressures for feature velocity often peak precisely when aggressive technical investment becomes most necessary.

While we lack mathematical grounding for these dynamics (what is entropy's functional form? when do compound returns become necessary rather than merely beneficial?), future instances facing rapid $\hat n_{\text{future}}$ growth should consider: are your improvements producing compound returns? The structure suggests this question may be more critical than the amount invested.

See ~/src/temporal-software-theory/vault/03-library/analyses/planning/simulations/ for preliminary explorations. These dynamics await proper theoretical foundation.
