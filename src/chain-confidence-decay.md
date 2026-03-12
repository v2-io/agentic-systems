---
slug: chain-confidence-decay
type: derived
status: exact
depends:
  - strategy-dimension
---

# Derived: Chain Confidence Decay

Confidence in a multi-step strategy decays monotonically with depth. The rate depends on the conditional dependence structure, but the qualitative result — longer chains are less confident than shorter ones — is robust.

## Formal Expression

*[Derived (chain-confidence-decay, mathematical identity)]*

For a chain of $n$ uncertain steps with conditional success probabilities:

$$\log P(\text{chain}) = \sum_{i=1}^{n} \log P(E_i \mid E_{\lt i})$$

Since each $\log P(E_i \mid E_{\lt i}) \leq 0$, chain confidence decays monotonically with depth.

**The independent case** ($p^n$) is the simplest special case, not the general result. When steps are conditionally dependent — success at step $k$ makes step $k+1$ more likely — the decay is slower. When steps have negative dependence (success at $k$ makes $k+1$ harder — resource depletion, adversary adaptation), decay is faster.

**Quantitative illustration** (independent, uniform $p$):

| Depth | $p = 0.9$ | $p = 0.8$ |
|-------|-----------|-----------|
| 1 | 0.90 | 0.80 |
| 3 | 0.73 | 0.51 |
| 5 | 0.59 | 0.33 |
| 10 | 0.35 | 0.11 |
| 20 | 0.12 | 0.01 |

## Epistemic Status

*Exact.* The additive decomposition of log-confidence is a mathematical identity (chain rule of probability). The qualitative consequence (monotonic decay) follows from the non-positivity of log-probabilities. No assumptions beyond the probability axioms.

## Discussion

**Structural pressure on strategies.** Chain confidence decay creates systematic pressure toward:
- **Short plans**: fewer steps means higher aggregate confidence
- **Parallel fallback paths**: OR-branches provide alternative routes when one chain fails
- **High-confidence critical links**: invest in the reliability of steps that appear in every path
- **Early monitoring**: detect chain failure early rather than discovering it at the end

These are not prescriptions but consequences — an agent that ignores chain decay will experience more strategy failures, lower effective tempo, and (if the failures are costly) faster reserve depletion.

**AND-nodes amplify decay.** When multiple parent chains must all succeed (conjunctive combination), their confidences multiply. A node requiring $k$ parents each at depth $d$ with per-edge confidence $p$ has aggregate confidence $p^{k \cdot d}$, not $p^d$. Deep conjunctive strategies are exponentially more fragile than deep disjunctive ones. This asymmetry is formalized in the combination rules ( #strategy-dag).

**Connection to the persistence condition.** Chain decay makes long-horizon strategies inherently fragile, which increases the effective disturbance rate $\rho_\Sigma$ against strategy persistence. An agent pursuing a 20-step plan in a changing environment faces compound uncertainty from both chain decay (internal fragility) and environmental change (external disturbance). The interaction between these — how environmental change compounds through uncertain chains — is not yet formalized.

## Working Notes

- The independent-edge assumption (used in the quantitative table) is conservative for positively correlated steps (shared infrastructure → correlated failures make the actual confidence *lower* than independent calculation suggests). Correlation structure is unmodeled — acknowledged as a limitation.
- The additive log-confidence form is the robust result; $p^n$ is the special case for independent uniform edges. This distinction matters: the qualitative consequence (decay with depth) is robust; the specific rate depends on the conditional structure.
