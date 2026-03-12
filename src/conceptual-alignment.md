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

*Hypothesis.* The qualitative claim (better alignment → faster comprehension) is nearly tautological — code that matches how the agent thinks about the domain is easier to understand. But the *functional form* (inverse proportionality) is not derived from ACT. The relationship could be logarithmic (diminishing returns from alignment), threshold-based (alignment matters only below a minimum), or dependent on agent type (human vs AI may have different alignment sensitivities). ACT does not currently predict the functional form.

The realignment corollary is *derived* from #change-investment — it is simply the investment threshold applied to alignment changes. Its epistemic status inherits from both the investment threshold (conditional) and the alignment hypothesis (discussion-grade); the weaker link governs.

## Discussion

**Alignment as observation channel quality.** In ACT terms, code structure is part of the agent's observation channel — it determines how efficiently the agent can extract the information needed to construct $M_t$. Well-aligned code delivers domain-relevant information in an organized form that matches the agent's needs. Misaligned code forces the agent to perform an additional mental translation (mapping between code vocabulary and domain vocabulary) on every observation. This translation cost is paid per comprehension event, making it subject to the turnover multiplier in #dual-optimization.

**The dual comprehension cost.** Comprehension isn't just understanding the code — it's understanding the code, the domain, and the *mapping between them*. When alignment is high, the mapping is trivial (code names = domain names, code structure = domain structure). When alignment is low, the mapping itself becomes a cognitive task.

**The startup pivot case.** After a significant domain model shift, the accumulated misalignment can dominate comprehension cost. A codebase still using "friends" and "posts" when the product has pivoted to "teammates" and "documents" forces translation on every interaction. The realignment corollary says: treat the rename/restructure as a feature, calculate its ROI, and prioritize it accordingly.

## Working Notes

- The inverse proportionality may be too strong. If alignment is measured on a 0–1 scale, the claim says comprehension time goes to infinity as alignment approaches zero — but in practice, completely misaligned code is still comprehensible, just slow. A more realistic form might be $t_{\text{comp}} = t_{\text{base}} + c / \text{alignment}$ (baseline plus alignment penalty) or some saturating function. The functional form is an empirical question.
- For AI agents with 100% context turnover, alignment may matter *more* than for humans, because the agent cannot build up a mental mapping over repeated interactions — it must reconstruct the code↔domain mapping fresh each session. Or it may matter *less*, because AI agents can process misaligned names faster than humans can. The direction is empirically uncertain.
- Connection to #information-bottleneck: alignment might be formalized as the mutual information between code structure and domain structure, with misalignment as information that must be reconstructed rather than observed directly. This is speculative.
- TST T-07's "AI Inversion" observation (that well-aligned code teaches the domain, not just the implementation) is interesting but belongs in the Section V treatment of AI agents, not here.
- A **description-length or translation-cost framing** may be more natural than inverse alignment: comprehension time as a function of the translation cost between code structure and domain model ($t_{\text{comp}} \sim t_{\text{base}} + \text{cost}_{\text{translate}}(S, D)$). This avoids the $1/\text{alignment}$ singularity and connects more directly to information theory — the translation cost is the additional bits needed to decode code-structure observations through a misaligned mapping. Worth exploring if this segment gets promoted beyond discussion-grade.

*(Descended from TST T-07, C-07.1.)*
