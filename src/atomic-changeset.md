---
slug: atomic-changeset
type: definition
status: axiomatic
depends:
  - feature-definition
---

# Definition: Atomic Changeset

The complete diff between the codebase state before and after a feature is fully implemented, excluding generated artifacts.

## Formal Expression

*[Definition (atomic-changeset)]*

For a feature $F$ ( #feature-definition) applied to system $S$:

$$\text{changeset}(F) = S_{\text{after}} \ominus S_{\text{before}}$$

where $\ominus$ denotes the human- or agent-authored diff, excluding build artifacts, generated code, and automated reformatting.

"Codebase" crosses architectural boundaries — source code, schemas, configuration, infrastructure-as-code, tests, API contracts, deployment pipelines, monitoring configuration. If it must change to deliver the feature, it is part of the changeset.

**Size measures** (not mutually exclusive):
- Lines changed (added + deleted + modified)
- Files touched
- Modules affected

## Epistemic Status

Definitional. The boundary choice (excluding generated artifacts) is a pragmatic convention, not derived — but it aligns with measuring the decisions the agent actually makes, which is what #temporal-optimality optimizes.

## Discussion

The changeset is the observable trace of an implementation decision. It is to software what the action $a_t$ is to the general agent: the intervention in the environment. The size and structure of the changeset are what #changeset-size-principle and #change-proximity-principle operate on.

## Working Notes

- The exclusion of generated code is pragmatically motivated but theoretically interesting. Generated code represents an amplification of the agent's action — small input, large output. The *decision* cost is in the input; the *environment effect* is in the output. Should the changeset measure decision cost or environment effect? For temporal optimization of agent time, decision cost is right. For understanding system coupling, environment effect matters.
- The definition is implicitly per-feature, but features aren't always cleanly isolated in practice. Overlapping changesets, partial features, and incremental delivery blur the boundary. #feature-definition already notes this ambiguity.

*(Descended from TST D-04.)*
