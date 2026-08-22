# Definition D-01: Feature

A unit of functionality, as perceived by those who requested, implement, or use it, that coherently changes the codebase and/or running system, including fixes through to full intended functionality.

**Key aspects:**
- Includes changes to non-functional requirements (performance, security, accessibility)
- Includes infrastructure changes that affect system capabilities
- Includes documentation changes that affect stakeholder understanding
- May include configuration changes and coordinated changes across multiple codebases or coupled systems
- Excludes pure no-op changes but includes changes that alter future implementation time while preserving external behavior
- Note that what are often called "no-op changes" are typically attempts at refactoring that fall under this definition

# T-02: Implementation Time Lower Bound (First Principle)

The theoretical minimum time to implement a deliberate feature is bounded below by the time required to specify it with sufficient detail, where detail required is inversely proportional to shared context.

## Formal Expression

$$\begin{aligned} &\forall \text{ feature } F: \\ &\text{time}_{\min}(F) \geq \min(\text{time}_{\text{specify}}(F, \text{context}), \text{time}_{\text{demo}}(F)) \\ &\text{where } \text{time}_{\text{specify}} \propto 1/\text{shared-context} \end{aligned}$$

## Why This Changes Everything

You cannot implement what you haven't specified. This isn't technological limitation but information-theoretic necessity. Even with infinite coding speed, you're bounded by specification time, which depends on:
- Information content of what you're specifying (Shannon entropy)
- Shared context between specifier and implementer (compression ratio)
- Communication channel bandwidth

This explains why LLMs are transformative - not just faster coding but massive shared context. "Make it like Twitter but for dogs" leverages petabytes of training as compressed understanding. A DSL is crystallized shared context enabling minimal specification.

The practical insight: As AI approaches instant implementation, software engineering becomes specification engineering. The highest leverage improvements come from:
1. Better specification languages
2. Increased human-AI shared context
3. Clearer intent communication
4. Domain-specific abstractions reducing specification complexity

Historical validation: Putnam (1978) empirically discovered implementation time bounds that may approximate $t_{\min} \approx (\text{time}_{\text{specify}})^{3/4}$, suggesting specification time was always the fundamental limit, experienced through imperfect communication technology.

# Corollary C-02.1: Communication as Limiting Factor

As actual implementation time approaches this lower bound, the communication speed and quality of specifications becomes the limiting factor. When coding becomes instantaneous, software development becomes specification engineering.
