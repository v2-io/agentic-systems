# T-03: Evolving Systems Scope (Scope Definition)

This theorem restricts TST's domain to systems with non-negligible probability of future change, establishing that for such systems, optimization must consider total lifecycle time rather than initial implementation alone.

## Formal Expression

$$\begin{aligned} &\mathcal{S}_{\text{evolving}} = \{S : P(n_{\text{future}}(S) \gt 0) \gt \varepsilon\} \\ &\text{Domain}(\text{TST}) = \mathcal{S}_{\text{evolving}} \end{aligned}$$

For $S \in \mathcal S_{\text{evolving}}$:

$$\text{time}_{\text{total}}(S) = \text{time}(F_0) + \sum_{i=1}^{n_{\text{future}}} \text{time}(F_i)$$

In practice: $\sum_{i=1}^{n_{\text{future}}} \text{time}(F_i) \gg \text{time}(F_0)$$

## The Infinite Velocity Insight

For any subsystem $s$ where $P(\text{change}(s)) \lt \varepsilon$:
$$\text{time}_{\text{future}}(s) \to 0 \implies \text{velocity}(s) \to \infty$$

Stable components operate at infinite velocity - they never consume future development time. This mathematically justifies using battle-tested libraries: reimplementing `sort()` takes something at infinite velocity and drags it back into finite time.

The paradigm shift: We're not building software, we're building *systems that evolve efficiently*. Initial implementation is just establishing initial conditions for a temporal evolution that will play out over years.

This creates productive tension - identify stable cores for infinite velocity, but premature extraction (when $P(\text{change}) \gt \varepsilon$) loses that benefit. Experienced developers implicitly compute $P(\text{change})$ to identify what belongs in libraries.
