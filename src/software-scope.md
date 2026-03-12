---
slug: software-scope
type: scope
status: axiomatic
depends:
  - scope-condition
  - temporal-optimality
---

# Scope: Software Scope

ACT's software domain applies to systems with non-negligible probability of future change.

## Formal Expression

*[Scope (software-scope)]*

$$\mathcal{S}_{\text{evolving}} = \{S : P(n_{\text{future}}(S) \gt 0) \gt \varepsilon\}$$

For $S \in \mathcal{S}_{\text{evolving}}$, the total time subject to optimization is:

*[Derived (software-scope, from temporal-optimality)]*

$$\text{time}_{\text{total}}(S) = \text{time}(F_0) + \sum_{i=1}^{n_{\text{future}}} \text{time}(F_i)$$

When $n_{\text{future}}$ is non-trivial, the sum dominates: $\sum_{i=1}^{n_{\text{future}}} \text{time}(F_i) \gg \text{time}(F_0)$. Under #temporal-optimality, this means optimizing lifecycle time, not initial implementation time.

### The stable-subsystem corollary

For any subsystem $s$ where $P(\text{change}(s)) \lt \varepsilon$:

*[Derived (software-scope, from scope definition)]*

$$\text{time}_{\text{future}}(s) \to 0$$

A subsystem with negligible change probability consumes zero future development time. In ACT terms: its environment change rate $\rho \to 0$, so from #persistence-condition, any nonzero tempo suffices — the subsystem is permanently adapted. No adaptive capacity needs to be allocated to it.

This justifies using stable, battle-tested libraries and frameworks: reimplementing `sort()` takes a subsystem at $\rho \approx 0$ and reintroduces it at finite $\rho$, consuming adaptive capacity that could be directed elsewhere.

## Epistemic Status

The scope restriction is definitional — we choose to analyze evolving systems. The consequence (lifecycle time dominates initial time) follows from #temporal-optimality applied to the scope. The stable-subsystem corollary follows directly from the scope definition. The connection to #persistence-condition ($\rho \to 0$ means trivially satisfied persistence) is a restatement in ACT's formal language, not a new derivation.

## Discussion

**The productive tension.** Stable cores should be identified and left alone (or adopted from external libraries). But premature extraction — treating a subsystem as stable when $P(\text{change})$ is actually non-negligible — loses the benefit. The estimation of $P(\text{change})$ is itself an act of model-building ( #agent-model): experienced developers are implicitly estimating $\rho$ per subsystem and allocating adaptive capacity accordingly.

**Initial implementation as initial conditions.** The scope reframes software development: we are not building a static artifact but establishing initial conditions for a temporal evolution. The quality of those initial conditions ( #change-investment) compounds through every subsequent feature. This is not a metaphor — it is the direct application of #temporal-optimality to a system with $n_{\text{future}} \gg 1$.

## Working Notes

- The $\varepsilon$ threshold is a parameter choice, not derived. What determines a sensible $\varepsilon$? Is it related to the team's ability to detect change (an observation threshold)?
- TST's original "infinite velocity" language is vivid but potentially misleading — velocity is undefined when there are zero changes. The ACT framing ($\rho \to 0$, persistence trivially satisfied) is more precise.
- The via-tft-mapping material has a much richer decomposition of the software "environment" (codebase, runtime behavior, user requirements, team knowledge, dependency ecosystem, infrastructure state). This scope segment doesn't need that detail, but #developer-as-act-agent or #software-epistemic-properties should incorporate it.
- The observation that software development = building systems that evolve efficiently is essentially the claim that software development is an adaptive process subject to ACT. This is what motivates the entire section, not just this scope narrowing.

*(Descended from TST T-03.)*
