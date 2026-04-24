---
slug: chain-confidence-decay
type: derived
status: exact
depends:
  - strategy-dimension
stage: claims-verified
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

**Triple depth penalty.** Chain depth creates three independent penalties. This segment identifies the first: **confidence decay** — deeper chains have lower aggregate confidence because $\log P(\text{chain})$ accumulates negative terms. The two-edge strategic dynamics analysis ( #strategic-dynamics-derivation) identifies the second: **evidence starvation** — downstream edge $k$ in a chain is tested only when all upstream edges succeed, so its effective correction rate is attenuated by $\prod_{j\lt k}\theta_j$. #strategy-complexity-cost identifies the third: **cognitive cost** — deeper chains have higher description length, consuming more representational capacity. The three penalties compound independently: a deep edge has low confidence (decay), receives few observations (starvation), and costs more to maintain (complexity). The maximum useful chain depth $d^\ast$ is the minimum over three independent constraints — see #strategy-complexity-cost for the formal bound.

**Anchor role in the coordinate-forcing meta-pattern.** The log-of-product decomposition here anchors three further AAD uniqueness theorems that force coordinates at other layers: reverse-KL at the divergence level ( #strategy-cost-regret-bound §6.1), log-odds at the update level ( #edge-update-natural-parameter), and Fisher metric at the metric level ( #gain-sector-bridge "Fisher-metric cases under parameterization-invariance"). The first two theorems cite this chain-layer identity as the analog motivating their additivity axiom; the Fisher-metric theorem rests on a parameterization-invariance axiom motivated by `#scope-agent-identity`'s singular-trajectory scope, an adjacent-AAD-commitment rather than a direct chain-analog — the theorem clears the broader discipline (uniqueness-theorem-forced coordinate under AAD-internal axiom) without reducing to a log-additive form. The catalog and the precise anchor-plus-three-theorem characterization live in #discussion-additive-coordinate-forcing.

**Section III corollaries (additional reach of the chain-layer identity).** The chain-rule identity has unsurfaced consequences at composition-related layers that are corollaries rather than new theorems:
- *Composition tower telescoping.* For a chain of nested sub-agents $(A_1, A_2, \ldots, A_\ell)$ with sub-agent-$k$ contraction factor $\kappa_k$, the tower contraction factor $\prod_\ell \kappa_\ell$ becomes log-additive: $\sum_\ell \log \kappa_\ell$. The closure-defect-along-tower quantity $\sum_\ell \log(\nu_\ell / \alpha_\ell)$ inherits the chain-rule identity's additivity.
- *Fisher information for multi-sample likelihoods.* $\log P(\mathbf y; \theta) = \sum_i \log P(y_i; \theta)$ is the chain-rule identity applied to multi-sample independent observations, producing the additive-Fisher-information decomposition standard in statistics.
- *Communication-tree aggregation.* Shared-intent compression across tree-structured agent communication channels inherits the chain-rule identity along the tree's branches, giving log-additive coordination-bit cost.

These are not independent uniqueness theorems — they are *corollaries* of the chain-layer identity applied to specific structural settings. Composition of structured multiplicative quantities inherits the log-additive decomposition whenever the chain-rule factorization applies. Cataloguing is in #discussion-additive-coordinate-forcing's Working Notes; none rises to primary-instance status because none introduces a new AAD-internal axiom (they reuse the probability chain rule as their identity, not as motivation for a fresh axiom). A distinct meta-pattern for composition specifically — composition-monotonicity rather than chain-rule — may be warranted; see `#composition-closure`'s bridge-lemma / Tier 1/2/3 / (CM4) family as the candidate structural material.

## Working Notes

- The independent-edge assumption (used in the quantitative table) is optimistic for positively correlated failures (shared infrastructure → correlated failures make the actual confidence *lower* than independent calculation suggests). Correlation structure is unmodeled — acknowledged as a limitation.
- The additive log-confidence form is the robust result; $p^n$ is the special case for independent uniform edges. This distinction matters: the qualitative consequence (decay with depth) is robust; the specific rate depends on the conditional structure.
