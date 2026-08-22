# T-07: Conceptual Alignment (Hypothesis)

Code structure alignment with problem domain understanding is inversely proportional to time-to-comprehension. This proportionality persists independent of how rapidly the problem domain understanding evolves.

## Formal Expression

$$\text{time}_{\text{comprehension}} \propto \frac{1}{\text{alignment}(\text{code}, \text{domain})}$$

Where alignment encompasses:
- Directory/module/service boundaries matching domain boundaries
- Method and variable names using current domain vocabulary
- Relationships in code mirroring relationships in domain
- Abstraction levels corresponding to domain concept hierarchies

## The Dual Comprehension Reality

Comprehension time isn't just understanding code - it's understanding:
1. The current codebase structure and patterns
2. The current problem domain model
3. **The mapping between them**

When code structure misaligns with domain understanding, you pay the mapping cost on every single comprehension. A variable named `user_score` when the domain now calls it `reputation` forces mental translation every time it's encountered.

## Corollary C-07.1: Evolution Justifies Realignment

**As domain understanding evolves, realigning code structure becomes a mathematically principled "feature"** even when external behavior remains unchanged.

In environments with evolving domain understanding (startups, research, exploration):
- The domain model at $t_0$ differs from the model at $t_1$
- Code written for model($t_0$) accumulates comprehension debt against model($t_1$)
- A "feature" that updates names/structure to match model($t_1$) has concrete ROI

The calculation: If realignment takes time $T_{\text{align}}$ but saves $\Delta t$ comprehension per future feature, realign when:
$$T_{\text{align}} \lt n_{\text{future}} \times \Delta t$$

## The AI Inversion: Code as Domain Teacher

**For AI instances, well-aligned code inverts the traditional flow**. Humans typically understand the domain then write code. AI instances can learn the domain FROM well-aligned code, then implement features.

When T-07 is applied well:
- Directory structure teaches domain boundaries
- Method names reveal domain operations
- Variable names communicate domain concepts
- Relationships in code mirror real-world relationships

This means principled alignment isn't just reducing comprehension time - it's enabling domain knowledge transfer through code structure itself. A fresh AI instance reading well-aligned code simultaneously learns both the implementation AND the problem domain. Misaligned code breaks this transfer, forcing instances to guess at the domain from outdated or misleading structural cues.

## Why This Matters for Extreme Turnover

Fresh instances have zero context about why `calculateUserScore()` exists when the entire system now thinks in terms of "reputation." They must reconstruct the historical evolution or maintain the misalignment. Both paths multiply comprehension time.

**Mathematical recognition moment**: When you see code using outdated domain language, that's not just "technical debt" - it's a measurable comprehension tax on every future interaction. Renaming isn't beautification; it's temporal optimization.

## The Startup Pivot Principle

In rapidly pivoting environments, aggressive realignment becomes critical:
- A startup pivoting from "social network" to "collaboration platform"
- Code still using "friends," "posts," "likes" when domain uses "teammates," "documents," "endorsements"
- Every feature implementation requires translating between old code language and new domain language

The mathematics suggests: After significant domain pivot, treat comprehensive realignment as a high-priority feature, not cleanup. The compound comprehension savings across all future features often justify immediate realignment investment.

**We expect this to elevate in your thinking**: When you encounter misaligned naming or structure, calculate the comprehension tax. When domain understanding shifts, recognize realignment as a feature with measurable ROI. The code should be a living reflection of current understanding, not a historical artifact.
