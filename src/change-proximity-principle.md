---
slug: change-proximity-principle
type: derived
status: conditional
depends:
  - change-distance
  - changeset-size-principle
  - comprehension-time
---

# Derived: Change Proximity Principle

Given two implementations with identical changeset sizes, the one with changes closer together requires less time.

## Formal Expression

*[Derived (change-proximity-principle, from comprehension-time + change-distance)]*

For a changeset, define proximity as:

$$\text{proximity}(\text{changeset}) = \frac{1}{\sum_{i,j} d(c_i, c_j)}$$

where $d$ follows the boundary hierarchy in #change-distance. Then:

$$t_{\text{impl}} \propto \frac{1}{\text{proximity}(\text{changeset})}$$

at constant changeset size.

## Epistemic Status

The qualitative claim is *derived*: comprehension time ( #comprehension-time) includes the cost of constructing $M_t$ for the relevant code, and scattered changes require constructing $M_t$ across more contexts, each with a boundary-crossing cost from #change-distance.

The quantitative form (inverse proportionality) is a *hypothesis*. The actual relationship between distance and cost is not derived — it could be linear, logarithmic, or dependent on the type of boundaries crossed. The exponential hypothesis is separated into #exponential-cognitive-load.

*Conditional* on the change-distance hierarchy reflecting real cognitive costs, which is plausible but not formally grounded.

## Discussion

**Proximity predicts architectural preferences.** The principle is consistent with the persistence of certain patterns:
- Modules that group commonly co-changing code (maximize proximity)
- Layered architectures that localize changes to specific layers
- Domain boundaries that contain related changes ( #conceptual-alignment)

These patterns minimize the distance term for typical future features. Whether proximity minimization is the actual mechanism driving their adoption (versus convention, tooling constraints, or other forces) is an empirical question — but the structural alignment is suggestive.

**The size-proximity decomposition.** Together with #changeset-size-principle, this gives a two-factor model of implementation cost: *how much* changes (size) and *how spread out* the changes are (proximity). Size is the first-order term; proximity is the structure-dependent correction. A good architecture minimizes both: small changesets with concentrated changes.

## Working Notes

- The pairwise sum $\sum_{i,j} d(c_i, c_j)$ treats all pairs equally. In practice, some pairs matter more (changes that must be understood together to make sense) and some matter less (independent changes that happen to be in the same commit). A weighted version would be more accurate but harder to compute.
- TST's Der-09.1 shows how this interacts with #change-investment: restructuring to improve proximity is an investment decision with the same threshold form. The cost is the restructuring effort; the savings are per-feature proximity improvements across $\hat{n}_{\text{future}}$ future features.
- The principle is about the agent's *experienced* cost, which depends on the agent's tooling and navigation capabilities. An IDE with good "jump to definition" reduces effective file distance; AI agents that can hold more context may have different distance sensitivities than humans. The principle holds qualitatively (boundaries have nonzero cost) but the distance hierarchy's quantitative weights are agent-dependent.

*(Descended from TST T-09.)*
