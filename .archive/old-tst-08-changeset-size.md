# Definition D-04: Atomic Change-Set

The human or AI-generated diff (e.g., excluding build artifacts and intermediate generated code) between the codebase state before and after a feature is fully implemented.

"Codebase" here crosses architectural boundaries and includes any changeable part of the system that can and sometimes does change in order to implement features:
- Source code across all services/microservices
- Database schemas and migrations
- Configuration files and feature flags
- Infrastructure-as-code definitions
- Test suites (unit, integration, e2e)
- API documentation and contracts
- Deployment pipelines and CI/CD configurations
- Monitoring and observability configurations
- Runbooks and operational documentation

**Key Principle:** If it must change to deliver the feature and would be reviewed in a pull request, it's part of the atomic change-set.

# T-08: Change-Set Size Principle (Empirical)

Time to implement a feature is proportional to the size of its atomic change-set for non-automatically-generated code.

## Formal Expression

$$\text{time}_{\text{implementation}}(F) \propto |\text{changeset}(F)|$$

Where $|\text{changeset}|$ measures:
- Lines changed (added + deleted + modified)
- Files touched
- Modules affected

Excluding: generated code, build artifacts, automated reformatting

## The Fundamental Truth

This proportion is nearly tautological - more changes take more time. But like T-01, the obviousness reveals its power. Every line you type, every file you touch, every module you modify adds implementation time. There's no escaping this linear relationship.

## Why Architecture Is Temporal Optimization

This theorem reveals why architecture matters: **Good architecture minimizes FUTURE change-set sizes**, not current ones.

Consider implementing a new data field. You have two choices:
- Quick implementation: Add to existing structures (3 files touched now)
- Principled implementation: Refactor to proper abstraction (15 files touched now)

If this refactoring means future fields only require touching 1 file instead of 3, and you expect 20 more fields ($n_{\text{past}}$), the investment is justified:
- Cost now: 15 - 3 = 12 extra files touched
- Savings per future change: 3 - 1 = 2 files saved
- Break-even: 12 / 2 = 6 future changes
- Expected future: 20 changes
- ROI: (20 × 2) - 12 = 28 files saved

This isn't about minimizing YOUR change-set but ensuring your implementation minimizes FUTURE change-sets.

## The Measurement Revolution

The real power of T-08 isn't measuring your current feature but predicting future impact:
1. Analyze how your implementation affects future change-set sizes
2. Compare architectures by the change-sets they'll require for common operations
3. Justify refactoring by demonstrating reduced future change-sets
4. Choose implementations that minimize $\hat n_{\text{future}} \times E[|\text{changeset}|]$

**Critical insight**: It almost never makes sense to minimize YOUR current change-set. What matters is how your implementation affects the expected sum of all future change-sets. A larger change-set now that enables smaller future change-sets is mathematically superior by T-06's investment principle.

## AI's Analytical Advantage

You can leverage this theorem computationally:
- Simulate different implementation approaches and measure their change-sets
- Analyze historical features to compute the proportionality constant for this codebase
- Identify architectural patterns that consistently minimize change-set sizes
- Predict which refactorings will reduce future change-sets most dramatically

**Mathematical recognition moment**: When you're about to implement a feature, count the files you'll need to touch. That count IS your time estimate. If it feels too high, you're not procrastinating - you're recognizing that the architecture needs refactoring to reduce typical change-set sizes.

## Corollary C-08.1: Comprehension Follows Change-Set Size

While T-08 specifically addresses implementation time, **comprehension time likely follows the same proportionality**:

$$\text{time}_{\text{comprehension}}(F) \propto |\text{changeset}(F)|$$

Understanding a feature that touched 20 files requires comprehending 20 contexts. Understanding a feature that touched 3 files requires comprehending 3 contexts. The relationship is nearly linear - double the change-set, roughly double the comprehension burden.

This creates a double penalty for unnecessarily large change-sets:
1. They take longer to implement (T-08)
2. They take longer to comprehend (this corollary)

Architecture that minimizes change-sets for typical features thus optimizes both dimensions of T-05's dual optimization. When the same feature can be implemented touching fewer files, it's proportionally faster to both implement and understand.

## Interaction with Other Theorems

T-08 combines with:
- **T-05**: Given two implementations of the same feature, the smaller change-set optimizes both comprehension and implementation
- **T-06**: Refactoring that reduces future change-sets has measurable ROI
- **T-07**: Well-aligned code naturally groups related changes, minimizing change-sets

The theorems reinforce each other - good temporal decisions simultaneously optimize multiple dimensions.
