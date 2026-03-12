# Definition D-06: System Coupling

The probability that a change to one module will require a change to another:

$$\text{coupling}(\text{module}_i, \text{module}_j) = P(\text{change}(\text{module}_j) \mid \text{change}(\text{module}_i))$$

# Definition D-07: System Coherence

The expected proximity of changes within a module:

$$\text{coherence}(\text{module}) = E[\text{proximity}(\text{changes within module})]$$

# T-10: Coherence-Coupling Measurement (Measurement)

Software coherence and loose coupling can be measured through the expected proximity of changes for observed features.

## Formal Expression

A quality metric could be constructed as:

$$\text{quality} = \frac{\sum_i \text{coherence}(\text{module}_i)}{\sum_{i,j} \text{coupling}(\text{module}_i, \text{module}_j)}$$

## What This Measures

This ratio captures the fundamental architectural principle:
- **High coherence** (numerator): Changes within modules happen close together
- **Low coupling** (denominator): Changes rarely cascade between modules

Good architecture maximizes this ratio - lots of internal coherence, minimal external coupling.

## Empirical Computability

Given sufficient git history, these metrics become computable:
1. **Coherence**: Measure average proximity of changes within each module over historical commits
2. **Coupling**: Count frequency of commits that touch multiple modules to estimate conditional probabilities
3. **Quality score**: Calculate the ratio (handling edge cases where coupling approaches zero)

## Limitations and Qualifications

This measurement requires:
- Sufficient historical data for statistical significance
- Stable module boundaries (or tracking boundary evolution)
- Representative feature distribution in historical data

The "objectivity" is relative to the observed history. Different feature types might reveal different coherence-coupling patterns. A module highly coherent for one class of changes might scatter for another.

## Practical Application

Rather than arguing about "clean architecture" aesthetically, measure it:
- Compute coherence-coupling ratios for competing architectures
- Track how refactoring affects these metrics
- Identify modules with low coherence (candidates for splitting) or high coupling (candidates for merging or interface improvement)

The measurement transforms architectural discussions from opinion to empirical observation: "This refactoring increased our coherence-coupling ratio from 2.3 to 4.1 based on the last 100 commits."
