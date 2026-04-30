---
slug: der-principled-decision-integration
type: derived
status: conditional
depends:
  - post-temporal-optimality
  - der-dual-optimization
  - hyp-conceptual-alignment
  - emp-changeset-size-principle
  - der-change-proximity-principle
---

# Derived: Principled Decision Integration

The optimal implementation choice minimizes total expected time across all probable future features, integrating all temporal factors simultaneously.

## Formal Expression

*[Derived (principled-decision-integration, from temporal-optimality)]*

For implementation choices $\mathbf{C}$ for the current feature:

$$C^* = \operatorname{argmin}_{C \in \mathbf{C}} \; E[T \mid C]$$

where total expected time given choice $C$ is:

$$E[T \mid C] = t_0(C) + \sum_{i} \lambda(F_i) \cdot \left[ t_{\text{comp}}(F_i \mid C) + t_{\text{impl}}(F_i \mid C) \right]$$

Here $\lambda(F_i)$ is the *expected count* of feature type $F_i$ over the relevant horizon — an intensity, not a probability. The total expected feature count is $\sum_i \lambda(F_i) = \hat n_{\text{future}}$ (the median prediction from #der-change-expectation-baseline), so $\hat n_{\text{future}}$ is an emergent property of the feature-type decomposition, not a separate multiplier.

This is the general form of #der-dual-optimization. Where dual-optimization uses a single "typical future feature" $F_{\text{typical}}$ with count $\hat n_{\text{future}}$, this decomposes that count across feature types:

$$\sum_i \lambda(F_i) \cdot t(F_i \mid C) \;=\; \hat n_{\text{future}} \cdot \mathbb E_{F \sim \lambda/\hat n_{\text{future}}}\big[\,t(F \mid C)\,\big]$$

Dual-optimization is recovered in the single-type limit where $\lambda$ concentrates on $F_{\text{typical}}$ with mass $\hat n_{\text{future}}$. The integration gains information whenever feature types have heterogeneous cost profiles: heavy-tailed costs on rare feature types, different alignment sensitivities per type, or regime-dependent proximity structure.

Substituting the proportional relationships from #hyp-conceptual-alignment, #emp-changeset-size-principle, and #der-change-proximity-principle:

$$E[T \mid C] = t_0(C) + \sum_{i} \lambda(F_i) \cdot \left[ \frac{\alpha \cdot h(\text{disc}(F_i \mid C))}{\text{alignment}(C)} + \beta \cdot \lvert\text{cs}(F_i \mid C)\rvert \cdot g(\text{prox}(F_i \mid C)) \right]$$

where $\alpha, \beta$ are empirical proportionality constants, $h$ and $g$ encode the (possibly exponential, per #hyp-exponential-cognitive-load) cost relationships, and $\text{disc}$, $\text{cs}$, $\text{prox}$ are the discontinuity count, changeset size, and proximity for feature $F_i$ under choice $C$.

## Epistemic Status

*Derived* from #post-temporal-optimality — the optimization is the direct application of the least-time postulate to the full cost structure. *Conditional* on the proportional relationships from #hyp-conceptual-alignment (hypothesis), #emp-changeset-size-principle (empirical), and #der-change-proximity-principle (conditional). The expanded form inherits the weakest epistemic status of its inputs: the alignment term is discussion-grade, the proximity cost function is uncertain in form. The integration structure itself is exact; the terms being integrated are approximate.

The full optimization is intractable in practice — it requires knowing the probability distribution of all future features and the exact impact of current decisions on future costs. The practical value is as a decision *framework* that structures the tradeoff space, not as a computable optimum.

## Discussion

**Relationship to dual-optimization.** This is the general case; #der-dual-optimization is the single-feature-type approximation. The approximation is good when future features are roughly homogeneous. When different feature types have very different cost profiles (e.g., a system that handles both UI changes and data pipeline changes), the full integration reveals tradeoffs the approximation misses — an architecture optimal for one feature type may be suboptimal for another.

**Dominant-factor analysis.** Perfect integration is impossible, but recognizing which factors dominate is usually tractable. Under high turnover, $t_{\text{comp}}$ dominates $t_{\text{impl}}$ (the #der-dual-optimization turnover multiplier). For a well-aligned codebase, alignment contributes little and changeset size dominates. For a highly modular system, proximity is less of an issue than for a monolith. Identifying the dominant factor reduces the full optimization to a simpler one.

**From patterns to principled decisions.** *[Discussion.]* This framework transforms how architectural decisions are evaluated. The traditional approach evaluates patterns against authority or convention ("use this pattern because it's a best practice"). The principled approach evaluates any pattern against the temporal objective: does it minimize expected future time for the likely feature distribution?

Every pattern, practice, and paradigm can be re-evaluated through this lens. The practical process for each decision:

1. Estimate the current implementation cost difference between options
2. List the probable future changes and their rough probabilities
3. Assess which option produces smaller changesets for those futures ( #emp-changeset-size-principle)
4. Assess which option keeps future changes more proximate ( #der-change-proximity-principle)
5. Assess which option creates fewer comprehension discontinuities ( #hyp-exponential-cognitive-load)
6. Choose the option that minimizes the weighted sum

*[Discussion — this process is a heuristic approximation of the formal objective. Experienced developers do this intuitively. The framework's contribution is making the intuition explicit and auditable — when a decision feels wrong, the framework identifies which factor was misjudged.]*

**The humanistic convergence.** *[Discussion — an observation about where temporal optimization leads.]* A striking consequence of optimizing for time is that it converges on human-centered design. The causal chain:

minimize total time → minimize comprehension time (because it dominates under turnover) → optimize for human cognitive patterns → match human mental models → use domain language → express domain concepts clearly

This means "good code" in the temporal sense is code that:
- Teaches the domain to the reader (because comprehension is the dominant cost)
- Uses names that a domain expert would recognize (because alignment eliminates translation cost)
- Places related logic together (because proximity reduces comprehension discontinuities)
- Tells a linear story (because narrative structure minimizes context-switching)

The convergence is not an aesthetic claim. It follows from the dual-optimization turnover multiplier: when code is read many times by many agents, the properties that minimize per-reader comprehension time are the properties that minimize total time. Those properties are, empirically, the ones developers describe as "readable," "clean," and "well-organized" — which are fundamentally properties of human cognitive accessibility.

*[Discussion — this convergence is structurally argued, not empirically demonstrated in full. The individual links (turnover multiplier → comprehension dominance → alignment matters → domain language is optimal) each have their own epistemic status documented in the respective segments. The chain as a whole is plausible but not independently validated. An empirical test: measure total development time on codebases ranked by "human-centeredness" (e.g., domain vocabulary coverage, naming clarity, narrative flow) and check whether the temporal ranking matches.]*

## Working Notes

- TST T-11 includes a rich expanded form with empirical constants $\alpha$ and $\beta$ that convert proportionalities to equalities. These constants are codebase-specific and not derived. In practice, relative comparisons (architecture A vs B) may not need absolute constants — the proportionalities suffice for ordering.
- The summation over $\lambda(F_i)$ assumes the feature intensity profile is known or estimable. In practice, this is where the agent's $M_t$ does the real work — predicting not just *how many* future features ($\hat n_{\text{future}}$ from #der-change-expectation-baseline) but *what kind*, decomposing the total count into per-type intensities. The quality of this prediction is bounded by the agent's model quality, connecting back to #def-model-sufficiency. The #der-change-expectation-baseline heavy-tailed prediction applies component-wise: each $\lambda(F_i)$ is itself a median prediction with Pareto-style tail behavior on the per-type count.
- This segment might be better positioned as a discussion/synthesis rather than a standalone derived claim, since it mostly assembles previously stated results into a composite objective. Its independent contribution is the explicit per-feature probability weighting, which dual-optimization elides.
