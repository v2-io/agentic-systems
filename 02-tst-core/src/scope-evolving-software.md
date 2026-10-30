---
slug: scope-evolving-software
type: scope
status: axiomatic
depends:
  - scope-agency
  - post-temporal-optimality
stage: draft
---

# Scope: Evolving Software

AAT's software domain applies to systems with non-negligible probability of future change.

## Formal Expression

*[Scope (scope-evolving-software)]*

$$\mathcal{S}_{\text{evolving}} = \{S : P(n_{\text{future}}(S) \gt 0) \gt \varepsilon\}$$

For $S \in \mathcal{S}_{\text{evolving}}$, the total time subject to optimization is:

*[Derived (scope-evolving-software, from temporal-optimality)]*

$$\text{time}_{\text{total}}(S) = \text{time}(F_0) + \sum_{i=1}^{n_{\text{future}}} \text{time}(F_i)$$

When $n_{\text{future}}$ is non-trivial, the sum dominates: $\sum_{i=1}^{n_{\text{future}}} \text{time}(F_i) \gg \text{time}(F_0)$. Under #post-temporal-optimality, this means optimizing lifecycle time, not initial implementation time.

### The stable-subsystem corollary

For any subsystem $s$ where $P(\text{change}(s)) \lt \varepsilon$:

*[Derived (scope-evolving-software, from scope definition)]*

$$\text{time}_{\text{future}}(s) \to 0$$

A subsystem with negligible change probability consumes zero future development time. In AAT terms: its environment change rate $\rho \to 0$, so from #result-persistence-condition, any nonzero tempo suffices — the subsystem is permanently adapted. No adaptive capacity needs to be allocated to it.

This justifies using stable, battle-tested libraries and frameworks: reimplementing `sort()` takes a subsystem at $\rho \approx 0$ and reintroduces it at finite $\rho$, consuming adaptive capacity that could be directed elsewhere.

## Epistemic Status

The scope restriction is definitional — we choose to analyze evolving systems. The consequence (lifecycle time dominates initial time) follows from #post-temporal-optimality applied to the scope. The stable-subsystem corollary follows directly from the scope definition. The connection to #result-persistence-condition ($\rho \to 0$ means trivially satisfied persistence) is a restatement in AAT's formal language, not a new derivation.

## Discussion

**What falls inside and outside.** Inside are systems whose requirements evolve with understanding, whose dependencies need updating, whose bugs and vulnerabilities surface through use, and whose markets shift. Outside are provably correct algorithms, write-once embedded firmware, prototypes built for disposal, and systems under a mandated freeze. The boundary is not sharp in consequence: the theory's prescriptions weaken continuously as $P(\text{change})$ falls toward $\varepsilon$, and non-temporal factors dominate below it.

**Lineage.** The scope is the domain of Lehman's laws of software evolution, whose first law (continuing change) states that a system used in the real world must be continually adapted or it becomes progressively less satisfactory (Lehman, Ramil, Wernick, Perry & Turski 1997, "Metrics and laws of software evolution — the nineties view," *Proc. 4th International Software Metrics Symposium*, 20–32). Lehman's E-type systems are, in this vocabulary, systems whose environment has $\rho \gt 0$.

**The productive tension.** Stable cores should be identified and left alone (or adopted from external libraries). But premature extraction — treating a subsystem as stable when $P(\text{change})$ is actually non-negligible — loses the benefit. The estimation of $P(\text{change})$ is itself an act of model-building ( #form-agent-model): experienced developers are implicitly estimating $\rho$ per subsystem and allocating adaptive capacity accordingly.

**Initial implementation as initial conditions.** The scope reframes software development: we are not building a static artifact but establishing initial conditions for a temporal evolution. The quality of those initial conditions ( #der-change-investment) compounds through every subsequent feature. This is not a metaphor — it is the direct application of #post-temporal-optimality to a system with $n_{\text{future}} \gg 1$. *[Empirical Claim.]* The weight of initial conditions has a measured counterpart. Across the histories of 200 open-source projects, most code-smell instances were present when the file was first added, not introduced by later decay (Tufano et al. 2015, "When and why your code starts to smell bad," *ICSE 2015*).

## Working Notes

- The $\varepsilon$ threshold is a parameter choice, not derived. What determines a sensible $\varepsilon$? Is it related to the team's ability to detect change (an observation threshold)?
- TST's original "infinite velocity" language is vivid but potentially misleading — velocity is undefined when there are zero changes. The AAT framing ($\rho \to 0$, persistence trivially satisfied) is more precise.
- The observation that software development = building systems that evolve efficiently is essentially the claim that software development is an adaptive process subject to AAT. This is what motivates the entire section, not just this scope narrowing.
