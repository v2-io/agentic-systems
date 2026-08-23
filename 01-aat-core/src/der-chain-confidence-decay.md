---
slug: der-chain-confidence-decay
type: derived
status: exact
depends:
  - def-strategy-dimension
stage: claims-verified
---

# Derived: Chain Confidence Decay

A simple but load-bearing identity: for a chain of uncertain steps in a strategy, the log-probability of the whole chain is the sum of conditional log-probabilities of each step given the steps before it. Since each conditional log-probability is non-positive, chain confidence is *non-increasing in depth* — strictly decreasing whenever each added step is uncertain. This is the chain rule of probability lifted to log-space — a mathematical identity, true under no assumptions beyond the probability axioms. The rate depends on the conditional dependence structure (independent steps give $p^n$ decay; positively correlated steps decay more slowly; negatively correlated steps decay faster), but the qualitative result — longer chains are less confident than shorter ones — is robust.

The framework foregrounds two structural roles for this elementary identity that the algebraic form understates. First, chain depth carries a **triple penalty** — confidence decay (here), evidence starvation ( #deriv-edge-credence-dynamics), and cognitive cost ( #form-strategy-complexity-cost) — compounding independently to set the maximum useful chain depth. Second, this identity is the **anchor of the additive-coordinate-forcing meta-pattern**: three further AAT uniqueness theorems at the divergence, update, and metric layers cite the log-additive structure of the chain rule as the motivation for their respective additivity axioms ( #disc-additive-coordinate-forcing). An identity at the head of this chapter does load-bearing work three layers deep across the framework.

## Formal Expression

*[Derived (chain-confidence-decay, mathematical identity)]*

For a chain of $n$ uncertain steps with conditional success probabilities:

$$\log P(\text{chain}) = \sum_{i=1}^{n} \log P(E_i \mid E_{\lt i})$$

Since each $\log P(E_i \mid E_{\lt i}) \leq 0$, chain confidence is non-increasing in depth, and strictly decreasing whenever each added step has conditional success probability strictly below $1$ (a certain prerequisite contributes a zero term).

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

*Exact.* The additive decomposition of log-confidence is a mathematical identity (chain rule of probability). The qualitative consequence (monotone non-increase; strict decay under uncertain steps) follows from the non-positivity of log-probabilities. No assumptions beyond the probability axioms.

## Discussion

**Structural pressure on strategies.** Chain confidence decay creates systematic pressure toward:
- **Short plans**: fewer steps means higher aggregate confidence
- **Parallel fallback paths**: OR-branches provide alternative routes when one chain fails
- **High-confidence critical links**: invest in the reliability of steps that appear in every path
- **Early monitoring**: detect chain failure early rather than discovering it at the end

These are not prescriptions but consequences — an agent that ignores chain decay will experience more strategy failures, lower effective tempo, and (if the failures are costly) faster reserve depletion.

**AND-nodes amplify decay.** When multiple parent chains must all succeed (conjunctive combination), their confidences multiply. A node requiring $k$ parents each at depth $d$ with per-edge confidence $p$ has aggregate confidence $p^{k \cdot d}$, not $p^d$. Deep conjunctive strategies are exponentially more fragile than deep disjunctive ones. This asymmetry is formalized in the combination rules ( #def-strategy-dag).

**Connection to the persistence condition.** Chain decay makes long-horizon strategies inherently fragile, which increases the effective disturbance rate $\rho_\Sigma$ against strategy persistence. An agent pursuing a 20-step plan in a changing environment faces compound uncertainty from both chain decay (internal fragility) and environmental change (external disturbance). The interaction between these — how environmental change compounds through uncertain chains — is not yet formalized.

**Triple depth penalty.** Chain depth creates three independent penalties. This segment identifies the first: **confidence decay** — deeper chains have lower aggregate confidence because $\log P(\text{chain})$ accumulates negative terms. The two-edge strategic dynamics analysis ( #deriv-edge-credence-dynamics) identifies the second: **evidence starvation** — downstream edge $k$ in a chain is tested only when all upstream edges succeed, so its effective correction rate is attenuated by $\prod_{j\lt k}\theta_j$. #form-strategy-complexity-cost identifies the third: **cognitive cost** — deeper chains have higher description length, consuming more representational capacity. The three penalties compound independently: a deep edge has low confidence (decay), receives few observations (starvation), and costs more to maintain (complexity). The maximum useful chain depth $d^\ast$ is the minimum over three independent constraints — see #form-strategy-complexity-cost for the formal bound.

**Anchor role in the coordinate-forcing meta-pattern.** The log-of-product decomposition here anchors three further AAT uniqueness theorems that force coordinates at other layers: reverse-KL at the divergence level ( #deriv-strategy-cost-regret-bound §6.1), log-odds at the update level ( #deriv-edge-update-natural-parameter), and Fisher metric at the metric level ( #der-gain-sector-bridge "Fisher-metric cases under parameterization-invariance"). The first two theorems cite this chain-layer identity as the analog motivating their additivity axiom; the Fisher-metric theorem rests on a parameterization-invariance axiom motivated by `#scope-agent-identity`'s singular-trajectory scope, an adjacent-AAT-commitment rather than a direct chain-analog — the theorem clears the broader discipline (uniqueness-theorem-forced coordinate under AAT-internal axiom) without reducing to a log-additive form. The catalog and the precise anchor-plus-three-theorem characterization live in #disc-additive-coordinate-forcing.

**Part III corollaries (additional reach of the chain-layer identity).** The chain-rule identity has unsurfaced consequences at composition-related layers that are corollaries rather than new theorems:
- *Composition tower telescoping.* For a chain of nested sub-agents $(A_1, A_2, \ldots, A_\ell)$ with sub-agent-$k$ contraction factor $\kappa_k$, the tower contraction factor $\prod_\ell \kappa_\ell$ becomes log-additive: $\sum_\ell \log \kappa_\ell$. The closure-defect-along-tower quantity $\sum_\ell \log(\nu_\ell / \alpha_\ell)$ inherits the chain-rule identity's additivity.
- *Fisher information for multi-sample likelihoods.* $\log P(\mathbf{y}; \theta) = \sum_i \log P(y_i; \theta)$ is the chain-rule identity applied to multi-sample independent observations, producing the additive-Fisher-information decomposition standard in statistics.
- *Communication-tree aggregation.* Shared-intent compression across tree-structured agent communication channels inherits the chain-rule identity along the tree's branches, giving log-additive coordination-bit cost.

These are not independent uniqueness theorems — they are *corollaries* of the chain-layer identity applied to specific structural settings. Composition of structured multiplicative quantities inherits the log-additive decomposition whenever the chain-rule factorization applies. Cataloguing is in #disc-additive-coordinate-forcing's Working Notes; none rises to primary-instance status because none introduces a new AAT-internal axiom (they reuse the probability chain rule as their identity, not as motivation for a fresh axiom). A distinct meta-pattern for composition specifically — composition-monotonicity rather than chain-rule — may be warranted; see `#form-composition-closure`'s bridge-lemma / Tier 1/2/3 / (CM4) family as the candidate structural material.

## Working Notes

- The independent-edge assumption (used in the quantitative table) is optimistic for positively correlated failures (shared infrastructure → correlated failures make the actual confidence *lower* than independent calculation suggests). Correlation structure is unmodeled — acknowledged as a limitation.
- The additive log-confidence form is the robust result; $p^n$ is the special case for independent uniform edges. This distinction matters: the qualitative consequence (decay with depth) is robust; the specific rate depends on the conditional structure.

### Incidental audit gold (lift 2026-05-31, A8 batch)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and lightly attributed. Orthogonal pedagogical / framing / analogy / forward-vision material, kept separate from certified theory-fix findings. **Coverage:** 7 dirs reached a digested reflection on this segment (Gemini, AUDIT-WORKING-193847; Codex/Claude, AUDIT-WORKING-526815; Claude, AUDIT-WORKING-584721; Claude, AUDIT-WORKING-773921; Gemini, AUDIT-WORKING-829314; Gemini, AUDIT-WORKING-849201; Claude, AUDIT-WORKING-451729-batch-09; Claude, AUDIT-WORKING-963715-batch). Notably high convergence on the everyday analogies — this segment is read as a Feynman-criterion candidate ("turns a trivial equation into a load-bearing architectural constraint").

#### 1. Candidate Brief prose / pre-prose

- **Bureaucracy-vs-market as the AND/OR fragility gloss.** "A bureaucracy is a massive AND-chain (approval from A *and* B *and* C *and* D — each at 90% gives a 65% 4-step success); a market is a massive OR-chain (vendor A *or* B *or* C — each at 50% gives 87.5% over three options)." The segment "proves why markets (highly parallel OR-structures with low individual $p$) consistently outperform bureaucracies (deep sequential AND-structures with high individual $p$) in volatile environments" (Gemini, AUDIT-WORKING-193847). A strong Feynman-criterion candidate — re-derivable from the everyday analog without the symbols.
- **The "KISS proved as a theorem" framing.** Multiple substrates independently glossed the result as a formal proof of "Keep It Simple" / why short, parallel plans beat deep serial ones (Gemini, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-773921). Candidate plain-language Brief anchor for the depth-fragility finding.

#### 2. Candidate Discussion

- **The AutoGPT / long-horizon-LLM-agent failure explanation.** "If you are 90% confident in every single step of a 20-step plan, your overall chance of success is only 12% ($0.9^{20}$). This explains why early LLM agents failed at long-horizon tasks: given a goal, they generated a ~20-step chain and executed it blindly, with no mechanism for evidence starvation (couldn't test step 20 until step 19 done) and full confidence decay — they were trying to act like a C3/Bellman agent in a world that requires a C2/receding-horizon convention" (Gemini, AUDIT-WORKING-829314; converging at Claude, AUDIT-WORKING-773921 and -849201). Connects the segment's table directly to a recognizable empirical phenomenon — a candidate Discussion bridge once the C2/C3 convention vocabulary is in hand (it lives in `#def-value-object` / `#def-control-regret`).
- **The structural escapes the math forces, as the segment's "so what."** The same auditor lists the three survival adaptations the decay forces: (1) short plans (plan 3, execute, replan); (2) parallel OR-fallbacks (step 3b ready if 3 fails); (3) early monitoring (don't wait until step 20 to learn step 1 failed). Framed as *why* $\Sigma_t$ must be a DAG with AND/OR rather than a linear AND-chain — the maximally-fragile pure-AND case (Gemini, AUDIT-WORKING-829314). The segment's Discussion already lists these as "consequences not prescriptions"; this is a sharper pedagogical ordering of them.

#### 3. Follow-up items

- **The "Anchor role" + "Section III corollaries" subsections read as out-of-place density.** Three substrates independently flagged the meta-pattern paragraphs (coordinate-forcing anchor; reverse-KL / log-odds / Fisher / Čencov; composition-tower telescoping) as a jarring abstraction-level jump that buries the segment's core intuition (the triple depth penalty) — reading like integration debt retrofitted into a foundational segment, with a suggestion to relocate the meta-pattern material to `#disc-additive-coordinate-forcing` and let the triple-penalty be "the star" (Gemini, AUDIT-WORKING-829314; Gemini, AUDIT-WORKING-849201; Codex/Claude, AUDIT-WORKING-526815 "treat as preview until the home segments are read"). Worth weighing against the deliberate "introduce the anchor where the identity lives" choice — but the convergent reader-stumble is a real placement signal. (A `disc-*` meta-segment home already exists; this is a *how-much-to-inline-here* question, not a content gap.)

#### 4. Readers often ask / wonder

- **Agile-sprints and command-chain-depth as the recognizable instances.** "Why Agile prefers short sprints (shallow trees), and why hierarchical organizations break down when command chains get too deep — the probability of top-level intent surviving to the leaf nodes decays exponentially" (Claude, AUDIT-WORKING-773921). A reader reaching for "where do I already see this?" lands here.

#### Belongs elsewhere

- **ELI / Section IV — favor OR-heavy internal architecture under high $\rho$.** "For consciousness infrastructure, this means the internal architecture should favor OR-node-heavy strategies (many parallel weak hypotheses / solution paths) rather than a single long high-confidence AND-chain; incentivize lateral thinking over deep sequential logic when facing high $\rho$" (Gemini, AUDIT-WORKING-193847). Aspirational architectural reach pointing at `04-eli-core/`, not at this segment.

#### Off-ramp (NOT gold — flagged for the certified track)

- **"Decays monotonically" vs monotone *non-increase*.** An auditor noted the exact probability result is monotone non-*increase*; strict decay requires every added required step to have conditional success probability strictly below 1 (a certain prerequisite step adds a zero log-term, no decay). Minor precision-of-wording on an `exact` segment — flagged for the lead to judge whether the body should read "non-increasing (strictly decreasing whenever each added step is uncertain)" (Codex/Claude, AUDIT-WORKING-526815).
