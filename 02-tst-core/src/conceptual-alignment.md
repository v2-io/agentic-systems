---
slug: conceptual-alignment
type: hypothesis
status: discussion-grade
depends:
  - comprehension-time
  - change-investment
---

# Hypothesis: Conceptual Alignment

Comprehension time is inversely related to the alignment between code structure and the current domain model. When code mirrors the domain, the agent's $M_t$ construction is cheaper.

## Formal Expression

*[Hypothesis (conceptual-alignment)]*

$$t_{\text{comp}}(F, S) \propto \frac{1}{\text{alignment}(S, D)}$$

where $\text{alignment}(S, D)$ measures the structural correspondence between codebase $S$ and the current domain model $D$:
- Directory/module boundaries matching domain boundaries
- Names using current domain vocabulary
- Code relationships mirroring domain relationships
- Abstraction levels corresponding to domain concept hierarchies

### Corollary: Realignment as Feature

*[Derived (realignment-as-feature, from change-investment + conceptual-alignment)]*

When domain understanding evolves from $D_0$ to $D_1$, code written for $D_0$ accumulates a comprehension cost against $D_1$. By the #change-investment threshold, realignment is justified when:

$$T_{\text{align}} \lt \hat{n}_{\text{future}} \times \Delta t_{\text{comp}}$$

where $\Delta t_{\text{comp}}$ is the per-feature comprehension savings from alignment. Realignment is a feature with measurable ROI, not cleanup.

## Epistemic Status

*Hypothesis.* The qualitative claim (better alignment → faster comprehension) is nearly tautological — code that matches how the agent thinks about the domain is easier to understand. But the *functional form* (inverse proportionality) is not derived from AAD. The relationship could be logarithmic (diminishing returns from alignment), threshold-based (alignment matters only below a minimum), or dependent on agent type (human vs AI may have different alignment sensitivities). AAD does not currently predict the functional form.

The realignment corollary is *derived* from #change-investment — it is simply the investment threshold applied to alignment changes. Its epistemic status inherits from both the investment threshold (conditional) and the alignment hypothesis (discussion-grade); the weaker link governs.

## Discussion

**Alignment as observation channel quality.** In AAD terms, code structure is part of the agent's observation channel — it determines how efficiently the agent can extract the information needed to construct $M_t$. Well-aligned code delivers domain-relevant information in an organized form that matches the agent's needs. Misaligned code forces the agent to perform an additional mental translation (mapping between code vocabulary and domain vocabulary) on every observation. This translation cost is paid per comprehension event, making it subject to the turnover multiplier in #dual-optimization.

**The dual comprehension cost.** Comprehension isn't just understanding the code — it's understanding the code, the domain, and the *mapping between them*. When alignment is high, the mapping is trivial (code names = domain names, code structure = domain structure). When alignment is low, the mapping itself becomes a cognitive task.

**The startup pivot case.** After a significant domain model shift, the accumulated misalignment can dominate comprehension cost. A codebase still using "friends" and "posts" when the product has pivoted to "teammates" and "documents" forces translation on every interaction. The realignment corollary says: treat the rename/restructure as a feature, calculate its ROI, and prioritize it accordingly.

**Merge conflicts as alignment diagnostic.** *[Discussion — operationalizable but unmeasured.]* Unnecessary merge conflicts — conflicts between changes to conceptually independent features — are a signal of misalignment. If two features are conceptually independent but their implementations collide in the same files, the code structure doesn't match the domain structure. This suggests a measurable diagnostic:

$$\text{alignment\_quality} = 1 - \frac{\text{conflicts between conceptually independent features}}{\text{total conflicts}}$$

An alignment quality near 1 means the code structure successfully isolates independent concepts; near 0 means conceptual independence doesn't translate to implementation independence. This is measurable from git history (identify feature branches, classify which touch independent domain areas, count spurious conflicts) but requires a ground-truth classification of feature independence — which is itself a judgment call. An approximation: features assigned to different domain areas by the team that nonetheless produce merge conflicts when developed in parallel.

**Feature organization vs. type organization.** *[Discussion — architectural consequence of alignment hypothesis.]* The alignment hypothesis explains a long-standing architectural debate. Type-based organization (grouping by technical role: `controllers/`, `models/`, `services/`) forces every feature to scatter changes across multiple directories. Feature-based organization (grouping by domain concept: `billing/`, `auth/`, `notifications/`) consolidates changes for each feature into fewer locations. If alignment means code boundaries should match domain boundaries, feature-based organization is the default recommendation — it aligns code proximity with conceptual proximity.

But this is not unconditional. Technical concerns that genuinely cross domain boundaries (database access patterns, caching strategies, logging infrastructure) may need shared modules that don't correspond to any single domain concept. The resolution is #change-investment: choose the organization that minimizes total expected future time, including both within-feature comprehension (favors feature folders) and cross-cutting infrastructure changes (may favor shared modules). The question "which organization?" is an instance of the investment threshold, not a matter of convention.

**Domain tracking: refactoring priority.** *[Discussion — practical ordering derived from alignment + change-investment.]* When the domain model has drifted from the code model, alignment work should be prioritized by impact on future comprehension time:

1. *Terminology mismatches in high-traffic code* — renaming where $\hat{n}_{\text{future}}$ is highest has the largest ROI
2. *Scattered concepts now understood as one* — merging reduces comprehension discontinuities (#exponential-cognitive-load)
3. *Conflated concepts now understood as distinct* — splitting prevents future changes from tangling independent concerns (#system-coupling)
4. *Boundary shifts* — updating module boundaries to match new domain boundaries
5. *Technical improvements* — only after domain alignment, since misaligned technical improvements compound the translation cost

This ordering follows from the investment threshold applied per-item: each level addresses a comprehension cost multiplied by the usage frequency of the affected code. The ordering is a heuristic recommendation, not a derived result — the actual priority depends on specific $\hat{n}_{\text{future}}$ and $\Delta t_{\text{comp}}$ per item.

**The learning loop.** *[Discussion.]* Domain alignment is not a one-time activity. As the team's understanding of the domain evolves through use, feedback, and market learning, the code must track that evolution:

unclear domain → exploratory code → user feedback → clearer domain → realign code → faster iteration → more feedback → clearer domain...

The realignment corollary formalizes one pass through this loop. The loop itself is the agent's adaptive cycle ( #recursive-update) operating at the strategic level: the domain model is part of $M_t$, and the code's alignment with that model is part of the observation infrastructure that determines future #adaptive-tempo. Code that tracks domain evolution maintains tempo; code that freezes at an early domain model accumulates alignment debt that degrades tempo over time.

**Strategic test timing.** *[Discussion — practical consequence.]* Tests protect behavior during realignment refactors. But writing tests *before* domain understanding stabilizes locks in the wrong model — tests for "posts" and "friends" become obstacles when the domain pivots to "documents" and "teammates." The alignment hypothesis suggests: write thorough tests *when* refactoring for domain alignment (tests document the current understanding), not *before* the domain model has stabilized enough to warrant locking in.

## Working Notes

- The inverse proportionality may be too strong. If alignment is measured on a 0–1 scale, the claim says comprehension time goes to infinity as alignment approaches zero — but in practice, completely misaligned code is still comprehensible, just slow. A more realistic form might be $t_{\text{comp}} = t_{\text{base}} + c / \text{alignment}$ (baseline plus alignment penalty) or some saturating function. The functional form is an empirical question.
- For AI agents with 100% context turnover, alignment may matter *more* than for humans, because the agent cannot build up a mental mapping over repeated interactions — it must reconstruct the code↔domain mapping fresh each session. Or it may matter *less*, because AI agents can process misaligned names faster than humans can. The direction is empirically uncertain.
- Connection to #information-bottleneck: alignment might be formalized as the mutual information between code structure and domain structure, with misalignment as information that must be reconstructed rather than observed directly. This is speculative.
- TST T-07's "AI Inversion" observation (that well-aligned code teaches the domain, not just the implementation) is interesting but belongs in the Section V treatment of AI agents, not here.
- A **description-length or translation-cost framing** may be more natural than inverse alignment: comprehension time as a function of the translation cost between code structure and domain model ($t_{\text{comp}} \sim t_{\text{base}} + \text{cost}_{\text{translate}}(S, D)$). This avoids the $1/\text{alignment}$ singularity and connects more directly to information theory — the translation cost is the additional bits needed to decode code-structure observations through a misaligned mapping. Worth exploring if this segment gets promoted beyond discussion-grade.

*(Descended from TST T-07, C-07.1.)*
