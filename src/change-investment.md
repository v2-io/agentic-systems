---
slug: change-investment
type: derived
status: conditional
depends:
  - dual-optimization
  - change-expectation-baseline
---

# Derived: Change Investment

Accept higher initial implementation cost when the amortized savings across expected future changes exceed the upfront cost. This is the pairwise decision rule derived from #dual-optimization.

## Formal Expression

*[Derived (change-investment, from dual-optimization)]*

For two implementation choices $C_1, C_2$ of the current feature, where $C_1$ costs more now but saves time per future feature:

$$\text{Choose } C_1 \text{ when: } t_0(C_1) - t_0(C_2) \lt \hat{n}_{\text{future}} \times \left[\bar{t}(F \mid C_2) - \bar{t}(F \mid C_1)\right]$$

where $\bar{t}(F \mid C) = t_{\text{comp}}(F \mid C) + t_{\text{impl}}(F \mid C)$ is the per-feature time under choice $C$, and $\hat{n}_{\text{future}}$ is the median prediction from #change-expectation-baseline.

Equivalently: accept $X$ extra minutes now to save $Y$ minutes per future change when $X \lt \hat{n}_{\text{future}} \times Y$.

## Epistemic Status

*Derived* from #dual-optimization. The threshold form is the pairwise comparison obtained by requiring $C_1$ to have lower total median-predicted time than $C_2$ in the dual-optimization objective. It inherits the assumptions of #change-expectation-baseline (median prediction — not expectation, since the mean is undefined — and uniform feature rate) and #dual-optimization (single typical future feature approximation).

The **compound effects** discussed below are structurally motivated but not formally derived within ACT. They connect to the persistence condition ( #persistence-condition) but the formal link has not been established.

## Discussion

**The threshold as everyday heuristic.** The investment threshold is simple enough to apply in real time: a file modified 20 times in git history suggests $\hat{n}_{\text{future}} \approx 20$. Spending 5 extra minutes to save 15 seconds per future interaction is justified ($5 \lt 20 \times 0.25$). The threshold transforms "clean code" from aesthetic preference to temporal optimization with measurable inputs.

**Compound effects.** Implementation choices affect not just future feature time but also the cost of future implementation *choices*. Principled early choices make future principled choices easier (lower comprehension cost → better decisions); rushed early choices make future principled choices harder (higher comprehension cost → more pressure to rush). This creates positive and negative feedback loops that amplify over time. In ACT terms, this is the agent's actions at time $t$ modifying the environment's properties for time $t+1$ — the standard adaptive feedback loop applied to code quality. The connection to #persistence-condition is suggestive: if code quality degrades faster than the team can restore it ($\rho \gt \mathcal{T} \times \Vert\delta_{\text{critical}}\Vert$), the codebase enters a regime of accelerating decay. But this analogy has not been formalized.

## Working Notes

- The near-zero cost observation from TST T-06 ("principled implementation often requires nearly identical time as quick implementation") is empirically plausible but not derived. If true, it means the threshold is almost always satisfied — even small $\hat{n}_{\text{future}}$ justifies principled choices when the upfront cost difference is near zero. This would be worth establishing empirically but is not an ACT claim.
- The compound effects / virtuous-vicious cycle is listed in WORKBENCH.md as an ungrounded claim. The connection to persistence condition dynamics is the most promising formalization path: model code quality as a state variable subject to the mismatch ODE, with each implementation choice either reducing or increasing the effective disturbance rate $\rho$. But this requires defining "code quality" as an ACT quantity, which #code-quality-as-observation-infrastructure is meant to address.
- TST T-06's AI-specific guidance (computational advantages in temporal optimization) belongs in Section V, not here. The core mathematical claim is agent-general.
- This segment overlaps substantially with #dual-optimization. The threshold form here adds the concrete decision rule; the compound effects discussion adds the feedback loop observation. If these don't justify a separate segment, this could fold into #dual-optimization as a corollary and discussion extension.

*(Descended from TST T-06.)*
