---
slug: comprehension-time
type: definition
status: axiomatic
depends:
  - feature-definition
  - software-scope
---

# Definition: Comprehension Time

The time from initial idea to first surviving change — the cost of understanding enough to act effectively.

## Formal Expression

*[Definition (comprehension-time)]*

For a feature $F$ ( #feature-definition) applied to system $S$:

$$t_{\text{comp}}(F, S) = \text{time from task assignment to first surviving modification of } S$$

This includes:
- Reading existing code to understand where to make changes
- Understanding why something was done a certain way
- Discovering hidden dependencies and side effects
- Building and validating a mental model of the relevant portions of $S$

## Epistemic Status

Definitional. The quantity is well-defined and measurable in principle (though rarely measured in practice). The interpretation in ACT terms (see Discussion) is structurally motivated but not formally derived.

## Discussion

**In ACT terms, comprehension is constructing $M_t$.** When a developer (or AI agent) begins work on a feature, they must build a model of the relevant portion of the codebase — its structure, dependencies, conventions, state. This is precisely the construction of $M_t$ ( #agent-model) from environmental observations. The time to comprehend is the time to build a model of sufficient quality ( #model-sufficiency) to support effective action.

**Comprehension cost compounds under turnover.** If the team has turnover rate $r$ and size $s$, the total comprehension cost across all readers is approximately $t_{\text{comp}} \times (1 + r) \times s$. With 100% context turnover per AI instance, every session pays the full comprehension cost. This makes comprehension time the dominant factor in AI-assisted development, not implementation time.

**The comprehension/implementation boundary is not always sharp.** Exploratory changes (make a modification, see what breaks, learn from the result) blend comprehension and implementation. In ACT terms, these are probe actions ( #causal-information-yield) — interventions whose purpose is to generate observations that improve $M_t$, not to advance toward the feature goal.

## Working Notes

- The claim that comprehension = $M_t$ construction is tempting but may be too simple. The developer is building a model of the code AND the domain AND the mapping between them (as T-07 conceptual alignment points out). Is this one $M_t$ or should it be decomposed? In ACT's current formulation, $M_t$ is the complete agent state — so it includes all of these. But the IB tradeoff ( #information-bottleneck) might have different $\beta$ for code-model vs domain-model.
- Can comprehension time be connected to $U_o$ and $\eta^\ast$? Well-written code (low $U_o$) should enable faster $M_t$ construction (higher $\eta^\ast$ per observation). The connection is qualitatively clear but quantitatively unformalized.
- The "surviving" qualifier is important — false starts that get reverted don't count. This means comprehension time is retrospectively defined, which creates measurement challenges.

*(Descended from TST D-02.)*
