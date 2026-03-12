---
slug: change-distance
type: definition
status: axiomatic
depends:
  - atomic-changeset
---

# Definition: Change Distance

The structural separation between two changes in a codebase, measured along a hierarchy of boundaries.

## Formal Expression

*[Definition (change-distance)]*

For changes $c_i, c_j$ within a changeset, distance follows a boundary hierarchy:

$$d_{\text{lexical}} \lt d_{\text{file}} \lt d_{\text{module}} \lt d_{\text{service}}$$

where:
- **Lexical distance**: lines apart in the same file
- **File distance**: directory traversals between files
- **Module distance**: module or package boundaries crossed
- **Service distance**: network or process boundaries crossed

Each boundary crossing represents a qualitative increase in the cost of maintaining context across the two changes.

## Epistemic Status

Definitional. The hierarchy is a structural observation about how software is organized, not a derived quantity. The claim that each boundary crossing increases cost is the separate claim in #change-proximity-principle.

## Discussion

Change distance operationalizes the intuition that "scattered changes are harder." The hierarchy reflects real discontinuities in the agent's observation channel: reading within a file is cheap (scrolling), reading across files requires navigation, reading across modules requires understanding interfaces, reading across services requires understanding protocols.

In ACT terms, each boundary crossing increases the cost of constructing the relevant portion of $M_t$ — the agent must load more context to hold both changes in working state simultaneously.

## Working Notes

- The hierarchy is discrete but the underlying cost may not be. Two changes 5 lines apart and 500 lines apart are both "lexical distance" but have different cognitive costs. A continuous distance metric might be more accurate, but the discrete hierarchy captures the dominant effect (boundary crossings).
- Service distance may need refinement for modern architectures (monorepo with service boundaries vs. polyrepo, serverless functions, etc.). The underlying quantity is "how much context must be loaded to reason about both changes together."

*(Descended from TST D-05.)*
