---
slug: der-change-investment
type: derived
status: conditional
depends:
  - der-dual-optimization
  - der-change-expectation-baseline
---

# Derived: Change Investment

Accept higher initial implementation cost when the amortized savings across expected future changes exceed the upfront cost. This is the pairwise decision rule derived from #der-dual-optimization.

## Formal Expression

*[Derived (change-investment, from dual-optimization)]*

For two implementation choices $C_1, C_2$ of the current feature, where $C_1$ costs more now but saves time per future feature:

$$\text{Choose } C_1 \text{ when: } t_0(C_1) - t_0(C_2) \lt \hat{n}_{\text{future}} \times \left[\bar{t}(F \mid C_2) - \bar{t}(F \mid C_1)\right]$$

where $\bar{t}(F \mid C) = t_{\text{comp}}(F \mid C) + t_{\text{impl}}(F \mid C)$ is the per-feature time under choice $C$, and $\hat{n}_{\text{future}}$ is the median prediction from #der-change-expectation-baseline.

Equivalently: accept $X$ extra minutes now to save $Y$ minutes per future change when $X \lt \hat{n}_{\text{future}} \times Y$.

## Epistemic Status

*Derived* from #der-dual-optimization. The threshold form is the pairwise comparison obtained by requiring $C_1$ to have lower total median-predicted time than $C_2$ in the dual-optimization objective. It inherits the assumptions of #der-change-expectation-baseline (median prediction — not expectation, since the mean is undefined — and uniform feature rate) and #der-dual-optimization (single typical future feature approximation).

The **compound effects** discussed below are structurally motivated but not formally derived within AAD. They connect to the persistence condition ( #result-persistence-condition) but the formal link has not been established.

## Discussion

**The threshold as everyday heuristic.** The investment threshold is simple enough to apply in real time: a file modified 20 times in git history suggests $\hat{n}_{\text{future}} \approx 20$. Spending 5 extra minutes to save 15 seconds per future interaction is justified ($5 \lt 20 \times 0.25$). The threshold transforms "clean code" from aesthetic preference to temporal optimization with measurable inputs.

**The near-zero cost observation.** *[Discussion — empirically plausible, not derived.]* In practice, the "principled" implementation often requires minimal additional time over the "quick" implementation. The decision is primarily about *which* organization, not *how much* additional effort. Examples at different cost scales:

- Choosing descriptive names over abbreviated ones (seconds)
- Placing related logic in the same module vs. scattering it (seconds)
- Extracting a function vs. duplicating a block (minutes)
- Choosing module boundaries that match domain concepts (near-zero incremental cost — the time is spent either way)

If the upfront cost difference $t_0(C_1) - t_0(C_2)$ is routinely near zero, the threshold is almost always satisfied: even $\hat{n}_{\text{future}} = 1$ justifies the principled choice. This would mean the investment decision reduces to a *prediction* problem (which organization will serve future changes?) rather than a *tradeoff* problem (how much extra time to invest?). This is an empirical hypothesis — measuring the actual distribution of $t_0(C_1) - t_0(C_2)$ across real decisions would establish whether the near-zero pattern holds generally or only for certain decision classes. One approach: instrument paired coding sessions where developers implement the same feature both ways, measuring time differences.

**Prediction under uncertainty.** When the threshold is satisfied (or near-zero), the remaining challenge is predicting *which* organization minimizes future time. This prediction operates under substantial uncertainty and draws on:

- *Pattern recognition*: What kinds of changes have occurred in this area before?
- *Domain knowledge*: What changes are typical in this problem space?
- *Strategic context*: What is on the roadmap or likely to be requested?
- *Optionality preservation*: When uncertainty is high, prefer choices that keep future options open over choices that optimize for a single predicted future

*[Discussion — the optionality principle is structurally related to AAD's strategy representation ( #def-strategy-dag): preserving optionality corresponds to maintaining multiple viable paths in the strategy DAG rather than committing to a single chain. This connection has not been formalized.]*

**Aggregation across scopes.** When a change affects multiple modules with different expected change frequencies:

*[Derived (change-investment, from dual-optimization applied per-module)]*

$$\text{net impact} = \sum_i P(\text{change in } m_i) \times \Delta\bar{t}(m_i)$$

A change that makes one module easier but another harder is justified only when the probability-weighted savings exceed the probability-weighted costs. This connects to #meas-coherence-coupling: high-coupling pairs make this calculation harder because changes propagate.

**Compound effects.** Implementation choices affect not just future feature time but also the cost of future implementation *choices*. Principled early choices make future principled choices easier (lower comprehension cost → better decisions); rushed early choices make future principled choices harder (higher comprehension cost → more pressure to rush). This creates positive and negative feedback loops that amplify over time. In AAD terms, this is the agent's actions at time $t$ modifying the environment's properties for time $t+1$ — the standard adaptive feedback loop applied to code quality. The connection to #result-persistence-condition is suggestive: if code quality degrades faster than the team can restore it ($\rho \gt \mathcal{T} \times \Vert\delta_{\text{critical}}\Vert$), the codebase enters a regime of accelerating decay. But this analogy has not been formalized.

*[Discussion — the compound effect is structurally motivated but not formally derived. Empirical validation could track a "code quality" proxy (e.g., the coherence/coupling ratio from #meas-coherence-coupling) over time in codebases with different early-stage investment patterns, testing whether the bifurcation into virtuous/vicious cycles is observable.]*

## Working Notes

- The near-zero cost observation is now in Discussion rather than Working Notes because it is load-bearing for practical application. But it remains empirically unvalidated. The most direct test: measure $t_0(C_1) - t_0(C_2)$ across a sample of real architectural decisions. If the distribution is concentrated near zero, the investment threshold is almost always satisfied and the theory's practical force comes primarily from prediction quality, not from investment calculus.
- The compound effects / virtuous-vicious cycle is listed in WORKBENCH.md as an ungrounded claim. The connection to persistence condition dynamics is the most promising formalization path: model code quality as a state variable subject to the mismatch ODE, with each implementation choice either reducing or increasing the effective disturbance rate $\rho$. But this requires defining "code quality" as an AAD quantity, which #der-code-quality-as-observation-infrastructure is meant to address.
- TST T-06's AI-specific guidance (computational advantages in temporal optimization) belongs in `03-logogenic-agents/`, not here. The core mathematical claim is agent-general.
- This segment overlaps substantially with #der-dual-optimization. The threshold form here adds the concrete decision rule; the compound effects discussion adds the feedback loop observation. If these don't justify a separate segment, this could fold into #der-dual-optimization as a corollary and discussion extension.
