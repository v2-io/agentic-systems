# Definition D-05: Change Distance

The distance between two changes in a codebase, measured as:
- **Lexical distance:** Lines apart in the same file
- **File distance:** Directory traversals between files
- **Module distance:** Module boundaries crossed
- **Service distance:** Network boundaries crossed

# T-09: Change Proximity Principle (Derived)

Given two implementations producing identical change-set sizes, the one with changes closer together requires less implementation time.

## Formal Expression

$$\text{proximity}(\text{changeset}) = \frac{1}{\sum_{i,j} \text{distance}(\text{change}_i, \text{change}_j)}$$

$$\text{time}_{\text{implementation}} \propto \frac{1}{\text{proximity}(\text{changeset})}$$

Where distance follows the hierarchy: lexical < file < module < service.

## The Nature of Discontinuities

The exact relationship between discontinuities and time requires empirical validation. We observe that implementation time increases with scattered changes, but whether this relationship is linear, polynomial, or exponential remains to be determined.

## Hypothesis H-09.1: Exponential Cognitive Load

**If** cognitive task-switching compounds multiplicatively (as some cognitive science research suggests for human cognition), then:

$$\text{time}_{\text{actual}} = \text{time}_{\text{baseline}} \times k^{\text{discontinuities}}$$

Where $k \gt 1$ represents the compounding factor per context switch.

This hypothesis would explain why developers strongly prefer consolidated changes and why scattered changes feel disproportionately difficult. Even modest values of $k$ (such as 1.1 or 1.2) would create substantial differences when compounded across many discontinuities.

**Note**: This remains a hypothesis requiring validation. The actual relationship may be linear ($k = 1$ with additive cost per switch), sub-exponential, or vary based on factors like familiarity, cognitive load, and whether the implementer is human or AI.

## Derivation Der-09.1: How T-06 and T-09 Interact

From T-06, we accept cost $C$ now to save $S$ per future change when:

$$C \lt n_{\text{future}} \times S$$

If discontinuities compound with factor $k$, then restructuring to improve proximity becomes an investment decision. The cost of accepting more discontinuities now:

$$C = t_{\text{base}} \times [k^{d_{\text{restructure}}} - k^{d_{\text{current}}}]$$

The savings per future feature from better structure:

$$S = t_{\text{base}} \times [k^{d_{\text{old}}} - k^{d_{\text{new}}}]$$

The break-even point:

$$n_{\text{breakeven}} = \frac{C}{S} = \frac{k^{d_{\text{restructure}}} - k^{d_{\text{current}}}}{k^{d_{\text{old}}} - k^{d_{\text{new}}}}$$

What this reveals: Even if $k$ is only slightly greater than 1, the exponential nature means restructuring decisions become highly sensitive to:
- The difference in discontinuities between approaches
- The expected number of future changes
- The compounding factor $k$ itself

The precise decision depends on measuring $k$ for your specific context (human vs AI, familiar vs unfamiliar code, etc.)

## Observed Patterns

Same-sized change-sets can vary dramatically in implementation time based on proximity. A 100-line change in one location versus 10-line changes across 10 files represent the same |changeset| but vastly different cognitive load.

This mathematical relationship suggests why certain architectural patterns persist:
- Modules that group commonly co-changing code
- Layered architectures that localize changes to specific layers
- Domain boundaries that contain related changes
