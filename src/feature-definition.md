---
slug: feature-definition
type: definition
status: axiomatic
depends:
  - software-scope
---

# Definition: Feature

A unit of functionality, as perceived by those who requested, implement, or use it, that coherently changes the codebase and/or running system.

## Formal Expression

*[Definition (feature-definition)]*

A **feature** $F$ is a deliberate change to a software system $S \in \mathcal{S}_{\text{evolving}}$ ( #software-scope) that:

1. Coherently modifies the codebase and/or running system behavior
2. Is perceived as a unit by at least one stakeholder (requester, implementer, or user)

**Included:**
- Changes to non-functional requirements (performance, security, accessibility)
- Infrastructure changes affecting system capabilities
- Documentation changes affecting stakeholder understanding
- Configuration changes and coordinated changes across coupled systems
- Refactoring: changes that alter future implementation time while preserving external behavior

**Excluded:**
- Pure no-ops (changes with no effect on behavior or future development cost)

Note: what practitioners call "no-op changes" are typically refactoring and fall under this definition.

## Epistemic Status

Definitional. This is a scoping choice about the unit of analysis, not a derived result. The definition is deliberately broad (refactoring counts as a feature) because under #temporal-optimality, any change that affects future time is subject to optimization.

## Discussion

**The refactoring inclusion matters.** By including changes that "alter future implementation time while preserving external behavior," the definition ensures that investments in code quality, naming, structure, and documentation are first-class features subject to the same temporal optimization as user-facing changes. This is not a value judgment about whether refactoring is good — it is a scope decision that brings refactoring under the theory's analysis.

**"As perceived by" is a level-of-description qualifier.** Different agents at different levels of composition ( #composition-consistency) may perceive the same change as different features. A single commit might be part of one feature for the developer and part of a different feature for the product manager. The definition does not privilege one level — the relevant decomposition depends on which agent's temporal optimization is being analyzed. This is consistent with ACT's scale-invariant scope condition.

**The atomic changeset ( #atomic-changeset) operationalizes this definition.** A feature is the conceptual unit; the changeset is its physical manifestation in the codebase.

## Working Notes

- In ACT terms, a feature is a deliberate intervention on the software environment — the agent choosing to $do(F)$ and observing the consequences. This connects to #pearl-causal-hierarchy (Level 2) and #causal-information-yield (the information gained from implementing F). But whether this connection adds analytical power or is just relabeling needs thought.
- The "as perceived by" qualifier creates a measurement problem: different stakeholders disagree about feature boundaries. Is there a principled way to resolve this, or is it inherently level-dependent?
- Refactoring as a feature that modifies the observation channel: well-named code reduces $U_o$ for future readers. This connects refactoring to #code-quality-as-observation-infrastructure, which is currently a gap. When that segment is written, the connection should be made explicit.

*(Descended from TST D-01.)*
