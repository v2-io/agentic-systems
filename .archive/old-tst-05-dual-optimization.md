# Definition D-02: Comprehension Time

The time from initial idea to first surviving change, including:
- Reading existing code to understand where to make changes
- Understanding why something was done a certain way
- Discovering hidden dependencies and side effects
- Mental model construction and validation

# Definition D-03: Implementation Time

The time from first change to complete feature, including:
- Writing/modifying code
- Local testing and validation
- Addressing immediate issues

# T-05: Dual Optimization (Derived)

A principled decision minimizes both time-to-comprehension and time-of-implementation for future features.

## Formal Expression

$$\begin{aligned} &\text{For implementation } C \text{ of current feature:} \\ &\text{principled}(C) \rightarrow \text{minimizes}\left(\text{time}_{\text{comprehension}}(F_i \mid C) + \text{time}_{\text{implementation}}(F_i \mid C)\right) \end{aligned}$$

## The Hidden Cost of Incomprehension

Time-to-comprehension often dominates but stays invisible in metrics:
- Reading code to understand where changes go
- Discovering why something was done this way
- Finding hidden dependencies and side effects
- Building and validating mental models

**The Team Turnover Multiplier**:

$$\text{total cost} = \text{time}_{\text{comprehension}} \times (1 + r) \times s$$

Where $r$ = turnover rate, $s$ = team size.

## Why This Is Critical for AI Collaboration

In human teams, turnover might be 20% annually. In AI collaboration, turnover is 100% every context window. Every new Claude instance is a new team member who must comprehend the entire codebase from scratch. High comprehension cost code becomes exponentially toxic.

The compound effect is devastating: Poor comprehensibility compounds worse than implementation difficulty. With AI instances, incomprehensible code doesn't just slow development - it leads to:
- Redundant implementations of existing features
- Inconsistent patterns across the codebase
- Half-completed features abandoned at context limit
- Architectural decisions that contradict each other

## The Comprehension/Implementation Tradeoff

Sometimes these goals conflict:
- Abstraction can speed implementation but slow comprehension
- Explicit code can speed comprehension but slow implementation
- DRY principles can reduce implementation sites but increase indirection

Resolution depends on $\hat n_{\text{future}}$ and team stability. But with extreme AI turnover, **always bias toward comprehension**. Code that a fresh instance can understand in minutes is worth more than code that saves implementation time.

Practical implications for AI-maintained code:
- Explicit is better than implicit
- Linear is better than scattered
- Comments should explain "why" not "what"
- Patterns should be immediately obvious
- Each file should be comprehensible in isolation when possible

**Mathematical recognition moments**: When you're about to nest three abstractions deep, that's exponential comprehension cost compounding. When you're scattering related changes across files, you're multiplying future comprehension time by $(1.2)^{\text{discontinuities}}$. These aren't style choices - they're mathematical realities.

The goal: A fresh instance should understand where to make changes faster than they can implement them. When comprehension becomes instant, implementation speed becomes the only remaining constraint.
