# Cluster Reference: Causal Plan Graphs and Strategy DAGs

**Overview:** Models strategies as causal DAGs, proving that the action-perception loop inherently generates Pearl Level-2 interventional data, and bounds strategies by a triple depth penalty.

---

## Canonical Source Segments

### Source: `der-loop-interventional-access.md`

```yaml
---
slug: der-loop-interventional-access
type: derived
status: exact
depends:
  - der-causal-hierarchy-requirement
  - der-recursive-update
  - post-causal-structure
  - scope-agent-identity
stage: draft
---
```


# Derived: Loop Provides Interventional Data Access

An agent in the feedback loop generates interventional data by construction: the agent's action $a_t$ causally precedes the next observation $o_{t+1}$, and the mismatch conditioned on $a_t$ carries interventional information. This is how agents within AAT's **agency scope** ($\mathcal{S}_{\text{agency}}$, which requires $\lvert\mathcal{A}\rvert \geq 2$ and at least one action with causal effect) gain Level 2 access — not through internal architecture, but through the loop itself. Agents in the adaptive scope but outside agency scope (passive observers) lack the action contrasts needed for interventional data.

## Formal Expression

*[Derived (loop-interventional-access, from causal-structure + recursive-update)]*

By #post-causal-structure, the temporal ordering is constitutive: $a_t$ causally precedes $o_{t+1}$. The agent chose $a_t$; the environment responded with $o_{t+1}$. The feedback loop therefore generates **intervention-produced data** — data whose causal character differs from passive observation because the agent's action was a genuine cause of the subsequent observation.

The critical distinction: **"action-generated data" is not the same as "cleanly identified do-estimates."** The pair $(a_t, o_{t+1})$ is produced under intervention — the agent executed $a_t$, making it interventional in character rather than a passively observed association. But between intervention-produced data and a usable estimate of $P(o \mid do(a_t), \Omega_t)$ stand: (1) coverage — the agent must have tried diverse actions, not just one policy; (2) confounding within a time step — unobserved state variables that affect both action choice and outcome; (3) delay — consequences may appear much later than $t+1$; (4) partial observability — $o_{t+1}$ reveals only part of the outcome. The strength of causal identification from this data depends on the regime ( #scope-edge-update-causal-validity): strong in Regime A (intervention-rich domains like software and laboratory science), moderate in Regime B (partial intervention), weak in Regime C (observation-only). The claim here is about the *character* of the data (interventional, not observational), not about the agent's ability to extract clean causal estimates from it.

The mismatch signal conditioned on the agent's action:

$$\delta_t \mid a_t = o_{t+1} - \hat{o}_{t+1}(M_t, a_t)$$

carries interventional information: it tells the agent how the environment responded to its specific intervention $a_t$, relative to what the model predicted.

## Epistemic Status

*Exact.* This is a logical consequence of temporal ordering ( #post-causal-structure) and the feedback-loop structure ( #scope-agency). The claim is about **data availability**, not reasoning capacity — the loop *provides* interventional data whether or not the agent *exploits* it for Level 2 reasoning. Whether the agent uses this data to build causal models depends on its update mechanism and model class.

The precision is important: we claim the agent has *access to* interventional data, not that it *correctly identifies* interventional structure. Confounding within a single time step, delayed outcomes, and partial observability can all complicate the extraction of clean causal signals from the loop data.

## Discussion

**The loop as a Level 2 engine.** This is one of AAT's load-bearing results. The causal hierarchy theorem ( #der-causal-hierarchy-requirement) says Level 2 knowledge requires more than correlational data. This result says: the adaptive loop *is* the "more." An agent that acts and observes the consequences is generating interventional data — the same kind of data that a scientist generates through experiments. The loop is a perpetual experiment.

**Precision about what "interventional" means here.** The interventional interpretation is strongest when:
- The agent's action was the primary cause of the observed change (low confounding)
- The observation follows closely in time (short delay)
- The agent varied its action across episodes (not stuck on one policy)

When confounding is high, delays are long, or the agent follows a fixed policy, the interventional information in each $(a_t, o_{t+1})$ pair is weaker — still present, but harder to extract. This is why #def-causal-information-yield distinguishes between high-CIY actions (that reveal causal structure) and low-CIY actions (that don't).

**Even agents without explicit causal models benefit.** A Q-learning agent doesn't maintain an explicit causal model, but in the tabular case with sufficient exploration and no within-step confounding, its Q-values converge toward $\mathbb{E}[R \mid s, do(a)]$ rather than $\mathbb{E}[R \mid s, A=a]$ — precisely because the training data comes from the agent's own interventions. In the partially observed, confounded, or delayed-outcome cases (where the caveats above apply), the loop still provides intervention-generated data, but the Q-values may converge to biased estimates that reflect the confounding structure rather than clean interventional effects. The loop provides Level 2 data; whether that data yields *identified* causal quantities depends on the domain's confounding and observability structure.

**Honest credit to the action-perception-loop framing.** The substantive observation that the agent's actions cause its observations — and therefore that loop data is interventional in character — is implicit in any framework built around an action-perception loop, including active inference (Friston, FitzGerald, Rigoli, Schwartenbeck & Pezzulo 2017, "Active inference: a process theory," *Neural Computation* 29; Parr & Pezzulo 2022, *Active Inference*, MIT Press, ch. 3) and the broader cybernetic-and-control lineage (Wiener 1948, *Cybernetics*; Conant & Ashby 1970, "Every good regulator of a system must be a model of that system," *Int. J. Systems Sci.* 1). AAT's distinctive contribution is not the observation that loop data is interventional but the *explicit lift* of this observation to a load-bearing theorem connected to Pearl's causal hierarchy ( #def-pearl-causal-hierarchy) via Bareinboim, Correa, Ibeling & Icard (2022). Three specific moves AAT makes that the implicit treatments do not:

1. **The Bareinboim-hierarchy connection.** Active inference and the cybernetic lineage rest on Bayesian-network generative models (Pearl Level 1, associational). They do not invoke the causal-hierarchy theorem to argue that the loop's action-generated data is the substrate Level-2 queries require. AAT does — and the consequence is that $\Sigma_t$ is positioned as a *causal* DAG rather than a *Bayesian-network* DAG.
2. **Regime-indexed strength of causal identification.** Even granting that loop data is interventional in character, the strength of usable causal identification varies by domain. AAT partitions this into Regime A (intervention-rich, software/laboratory), B (partial intervention, organizational), C (observation-only — see #scope-edge-update-causal-validity). The AI literature treats causal identifiability uniformly within its modeling assumptions and does not surface the regime distinction at the segment level.
3. **Explicit scope honesty.** The Formal Expression above carefully distinguishes "data generated under intervention" from "cleanly identified do-estimates." The AI literature, as Bruineberg, Dolega, Dewhurst & Baltieri (2022) document in their Pearl-vs-Friston critique, sometimes elides this distinction — using the action-perception loop language to support stronger causal claims than the formal apparatus delivers. AAT's careful split is the conservative form.

The reframing here is rhetorical, not substantive: the headline result (the loop is a Level-2 engine) stays; what changes is the explicit acknowledgment that the observation about loop data being action-generated is shared with the broader literature. AAT's distinctive content sits in the three specific moves above. The companion architectural move on #der-directed-separation (Pearl-blanket vs. Friston-blanket form of Markov blanket; cf. Bruineberg et al. 2022) makes AAT's conservative-form positioning visible across both architectural and access-channel segments.

**Connection to the identifiability-floor pattern.** This segment is structurally load-bearing for the L0-causal-insufficiency-detection no-go ( #der-causal-insufficiency-detection): without the loop's interventional access, the no-go forbids detection entirely; the covariance test under joint sibling observability is the unique broadly-available violation of the no-go's "purely on-policy" scope. See #disc-identifiability-floor for the meta-pattern.

**Composite-layer extension.** `#disc-identifiability-floor` Instance 3 (the composition-layer no-go anchored in Liberzon 2003's common-Lyapunov nonexistence) establishes that composite contraction cannot in general be certified from component-level data alone — the coupling-sign bit distinguishing cooperative from adversarial regimes is unidentifiable from component marginals. One of the four structural escapes in Instance 3 is composite-extended loop-interventional-access: **interventions on sub-agent $A_j$ reveal $A_i$'s cross-coupling response**, which is a $do(\cdot)$-data distinction between the two coupled constructions. This is the composite-layer analog of the single-agent interventional-access-escape the present segment delivers for Instance 1; in the composite setting, the agent performs interventions on one sub-agent's action space and observes the effect on another sub-agent's mismatch trajectory, extracting the coupling sign that component marginals cannot. The load-bearing role of `#der-loop-interventional-access` therefore extends across two identifiability-floor instances (agent-internal and composite-layer), not one.

**Modes of deployment across `#disc-identifiability-floor` instances.** The shared load-bearing role — Level-2 data from interventional action under `#der-causal-hierarchy-requirement` supplying the unique broadly-available escape from an observational-equivalence no-go — manifests through **semantically distinct interventional mechanisms** at different layers. The modes share the Pearl-$do$ structure but differ in who performs the intervention and on what:

- **Mode 1 — agent-self-intervention (Instance 1, causal-structure layer).** The agent performs $do$-actions on its own action space as part of its ordinary adaptive loop. The intervention is *on the agent's own action*; the target is the environment's response, which reveals the latent common cause that Instance 1's on-policy L0-insufficiency-detection no-go (Bareinboim et al. 2022 CHT) makes unidentifiable. The agent-as-Level-2-data-generator property is intrinsic to the loop structure, not a capability that must be added.

- **Mode 2 — observer-on-sub-agent (Instance 3, composition layer).** An observer external to a composite performs $do$-interventions on one sub-agent $A_j$'s action space; the target is another sub-agent $A_i$'s mismatch-trajectory response, which reveals the cross-coupling sign that Instance 3's Liberzon-anchored no-go makes unidentifiable from component-marginal observation. The same Pearl-$do$ structure, but the intervening agent and the measured agent are distinct members of the composite.

Future instances of `#disc-identifiability-floor` at new layers may add further modes (see `#disc-identifiability-floor` Working Notes for the architecture-within-behavior-class layer currently under triage; the corresponding mode would be *observer-on-agent-input* at the candidate agent's observation channel). The three-mode-pattern observation is a structural regularity worth naming even though the specific Mode-3 instance has not promoted; the load-bearing content — Level-2 escape from observational-equivalence no-goes via loop-interventional access — remains shared across the deployment modes even when the specific interventional quantity varies. The unification is at the pattern level; the mechanism is semantically distinct per layer.

**Why the loop data is genuinely interventional — the singular-trajectory ground.** The interventional character of loop data is not a property of the feedback mechanism in isolation; it rests on the scope commitment in #scope-agent-identity that each agent is instantiated on a singular, non-forkable causal trajectory. When the agent executes $a_t$ and observes $o_{t+1}$, the observation is the response to *this* agent's intervention on *its* single trajectory $\mathcal C_t$. Replaying $a_t$ from a checkpointed $M_t$ against a different event stream would *not* constitute an intervention on $\mathcal C_t$ — it would be an intervention on a different trajectory $\mathcal C_t^{(2)}$ that happened to share a prefix. Pearl's $do$-operator presumes a definite causal system acted upon; AAT inherits this presumption via the singular-trajectory scope. Agents whose ontology is *type-like* (equivalence classes of copies) rather than *token-like* (singular trajectories) are outside AAT's formal scope; in particular, aggregate claims about "the model" across copies require additional machinery not provided here. This is the ontological ground that makes the "action-generated data is Level-2" claim honest rather than metaphorical.

## Working Notes

- This result establishes that all agents within AAT's **agency scope** ( #scope-agency, $\mathcal{S}_{\text{agency}}$) have access to interventional data, regardless of their internal architecture. Agents in the adaptive scope but outside agency scope (passive observers, nominal agents with $\lvert\mathcal{A}\rvert \lt 2$ or no causal effect) lack the action contrasts needed to generate interventional data — they observe but cannot intervene. This includes LLM agents operating through a tool-use loop — the LLM issues an action (tool call), observes the result, and updates. The loop gives it Level 2 data even though its internal architecture (transformer attention) is not designed for causal reasoning. The loop compensates for architectural limitations.
- The connection to #def-causal-information-yield: CIY quantifies *how much* interventional information a specific action provides. This segment establishes that interventional information is *available in principle*; CIY measures the *quantity per action*.
- **Cross-reference to NeurIPS Paper 2.** The Loop-as-Causal-Engine claim is formalized at theorem grade in NeurIPS 2026 Paper 2 ("A Unified Convergence Theory for Non-Stationary Reinforcement Learning", `~/src/neurips/02-unified-convergence-rl/`, §5 Lemma 5.3 / `#lem-loop-level2`) under the named **(C1) positivity / (C2) sequential-ignorability / (C3) known action-mechanism** triple. (C2) is the load-bearing structural condition: in mutilated-graph form, $a_t$ must be d-separated from $o_{t+1}$ given history $H_t$. *Goal-conditioned LLM policies violate (C2) by construction* — the goal influences action through the same forward pass that models the observation, breaking the conditional independence required for sequential ignorability — which is the bridge to Paper 3's Coupled-class formulation. The (C1)-(C3) triple makes explicit which structural commitments a Class 1 (Separated) tool-use loop satisfies for free that a Class 3 (Coupled) goal-conditioned policy does not. See `spikes/neurips-back-integration-2026-05-08.md` §1 Paper 2 entry 5.


---

### Source: `der-chain-confidence-decay.md`

```yaml
---
slug: der-chain-confidence-decay
type: derived
status: exact
depends:
  - def-strategy-dimension
stage: claims-verified
---
```


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

**AND-nodes amplify decay.** When multiple parent chains must all succeed (conjunctive combination), their confidences multiply. A node requiring $k$ parents each at depth $d$ with per-edge confidence $p$ has aggregate confidence $p^{k \cdot d}$, not $p^d$. Deep conjunctive strategies are exponentially more fragile than deep disjunctive ones. This asymmetry is formalized in the combination rules ( #def-strategy-dag).

**Connection to the persistence condition.** Chain decay makes long-horizon strategies inherently fragile, which increases the effective disturbance rate $\rho_\Sigma$ against strategy persistence. An agent pursuing a 20-step plan in a changing environment faces compound uncertainty from both chain decay (internal fragility) and environmental change (external disturbance). The interaction between these — how environmental change compounds through uncertain chains — is not yet formalized.

**Triple depth penalty.** Chain depth creates three independent penalties. This segment identifies the first: **confidence decay** — deeper chains have lower aggregate confidence because $\log P(\text{chain})$ accumulates negative terms. The two-edge strategic dynamics analysis ( #deriv-edge-credence-dynamics) identifies the second: **evidence starvation** — downstream edge $k$ in a chain is tested only when all upstream edges succeed, so its effective correction rate is attenuated by $\prod_{j\lt k}\theta_j$. #form-strategy-complexity-cost identifies the third: **cognitive cost** — deeper chains have higher description length, consuming more representational capacity. The three penalties compound independently: a deep edge has low confidence (decay), receives few observations (starvation), and costs more to maintain (complexity). The maximum useful chain depth $d^\ast$ is the minimum over three independent constraints — see #form-strategy-complexity-cost for the formal bound.

**Anchor role in the coordinate-forcing meta-pattern.** The log-of-product decomposition here anchors three further AAT uniqueness theorems that force coordinates at other layers: reverse-KL at the divergence level ( #deriv-strategy-cost-regret-bound §6.1), log-odds at the update level ( #deriv-edge-update-natural-parameter), and Fisher metric at the metric level ( #der-gain-sector-bridge "Fisher-metric cases under parameterization-invariance"). The first two theorems cite this chain-layer identity as the analog motivating their additivity axiom; the Fisher-metric theorem rests on a parameterization-invariance axiom motivated by `#scope-agent-identity`'s singular-trajectory scope, an adjacent-AAT-commitment rather than a direct chain-analog — the theorem clears the broader discipline (uniqueness-theorem-forced coordinate under AAT-internal axiom) without reducing to a log-additive form. The catalog and the precise anchor-plus-three-theorem characterization live in #disc-additive-coordinate-forcing.

**Section III corollaries (additional reach of the chain-layer identity).** The chain-rule identity has unsurfaced consequences at composition-related layers that are corollaries rather than new theorems:
- *Composition tower telescoping.* For a chain of nested sub-agents $(A_1, A_2, \ldots, A_\ell)$ with sub-agent-$k$ contraction factor $\kappa_k$, the tower contraction factor $\prod_\ell \kappa_\ell$ becomes log-additive: $\sum_\ell \log \kappa_\ell$. The closure-defect-along-tower quantity $\sum_\ell \log(\nu_\ell / \alpha_\ell)$ inherits the chain-rule identity's additivity.
- *Fisher information for multi-sample likelihoods.* $\log P(\mathbf y; \theta) = \sum_i \log P(y_i; \theta)$ is the chain-rule identity applied to multi-sample independent observations, producing the additive-Fisher-information decomposition standard in statistics.
- *Communication-tree aggregation.* Shared-intent compression across tree-structured agent communication channels inherits the chain-rule identity along the tree's branches, giving log-additive coordination-bit cost.

These are not independent uniqueness theorems — they are *corollaries* of the chain-layer identity applied to specific structural settings. Composition of structured multiplicative quantities inherits the log-additive decomposition whenever the chain-rule factorization applies. Cataloguing is in #disc-additive-coordinate-forcing's Working Notes; none rises to primary-instance status because none introduces a new AAT-internal axiom (they reuse the probability chain rule as their identity, not as motivation for a fresh axiom). A distinct meta-pattern for composition specifically — composition-monotonicity rather than chain-rule — may be warranted; see `#form-composition-closure`'s bridge-lemma / Tier 1/2/3 / (CM4) family as the candidate structural material.

## Working Notes

- The independent-edge assumption (used in the quantitative table) is optimistic for positively correlated failures (shared infrastructure → correlated failures make the actual confidence *lower* than independent calculation suggests). Correlation structure is unmodeled — acknowledged as a limitation.
- The additive log-confidence form is the robust result; $p^n$ is the special case for independent uniform edges. This distinction matters: the qualitative consequence (decay with depth) is robust; the specific rate depends on the conditional structure.


---

### Source: `def-strategy-dag.md`

```yaml
---
slug: def-strategy-dag
type: definition
status: conditional
depends:
  - scope-and-or
  - post-causal-structure
  - def-pearl-causal-hierarchy
  - form-objective-functional
  - def-strategy-dimension
stage: draft
---
```


# Definition: Strategy DAG

The strategy $\Sigma_t$ is a directed acyclic graph with probabilistic edges and AND/OR combination semantics. Each edge carries the agent's causal credence that completing the parent step advances the child step. The graph encodes the agent's theory of how its actions produce progress toward its objectives.

**Why a DAG.** The DAG structure is not a modeling convenience but a *consequence* of operational requirements on any causally-reasoning bounded agent — at the level of sufficiency, not yet necessity. #deriv-graph-structure-uniqueness proves that directed temporal order plus probabilistic uncertainty plus causal sufficiency *suffice* for a DAG-with-Markov-factorization representation (the necessity direction — no non-DAG structure could satisfy these postulates — is an open stronger result). Acyclicity is proved from temporal ordering over a finite horizon. What remains a formulation choice is the *parameterization within* the DAG structure: AND/OR combination with single-parameter edges is the AAT choice, motivated by parsimony and convergence across three independent formalism attempts, but alternative parameterizations (within the derived graphical structure) are legitimate research directions.

**Strategy-layer exactness contract.** All formal results in AAT's strategy layer — the sector condition transfer ( #deriv-edge-credence-dynamics, Prop B.5), the persistence schema ( #schema-strategy-persistence), the gradient-based credit assignment ( #disc-credit-assignment-boundary) — are proved under **L0 (independence)**: causally sufficient DAGs with independent edge outcomes. **L0 formal results transfer exactly to correctly constructed L1 DAGs (strict prerequisites, Prop B.6) and L1' DAGs (soft facilitators, Prop B.7) — provided the common cause is observable per trial.** When the common cause is unobservable, the per-conditional decomposition is *fundamentally* (not merely "openly") obstructed — the mixture parameters are non-identifiable from a single observation channel (Fisher rank deficiency / Cramér-Rao floor; see B.7 §"Refuted Under Unobservable $C$"), and the agent must either collect direct $C$-observations, run multi-child joint observations (Prop B.7 §"Repair routes"), or fall back to plan-level (L0-on-marginals) tracking. See the Correlation Hierarchy below for the full treatment.

## Formal Expression

*[Definition (strategy-dag)]*

$$\Sigma_t = (V_t, E_t, p_t, \gamma_t)$$

where:
- $V_t$: set of **propositional nodes** — each node represents a condition that could be true or false (including action-success propositions at the leaves)
- $E_t \subseteq V_t \times V_t$: directed causal edges
- $p_t : E_t \to [0,1]$: **causal credence** per edge — the agent's confidence that completing the parent advances the child
- $\gamma_t : V_t \to \{\text{AND}, \text{OR}\}$: combination rule per node ( #scope-and-or)

**Structural constraints:**

1. **Acyclicity.** $\Sigma_t$ is a DAG. This is *derived*, not assumed — see below.
2. **Rootedness.** Every node has a directed path to a unique root terminal $v_\text{root}$ — the single sink node (out-degree 0) of $\Sigma_t$. Compound objectives express their combination structure through the AND/OR machinery below $v_\text{root}$, consistent with scalar $V_{O_t}$ ( #form-objective-functional).
3. **Source constraint.** Leaf nodes are propositions about action success ("action $a$ succeeds at $\tau_v$") or observable conditions ("condition $C_v$ holds at $\tau_v$"). Both are propositional — the distinction is whether the proposition is within the agent's causal control (action) or not (condition).

**Leaf base credence.** For each leaf node $v \in V_t^{\text{leaf}}$, the base credence used in status propagation:

$$p_v(M_t) = \begin{cases} \Pr(\text{action } v \text{ succeeds at } \tau_v \mid M_t) & \text{if } v \text{ is an action node} \\[4pt] \Pr(C_v(\tau_v) \mid M_t) & \text{if } v \text{ is a condition node} \end{cases}$$

where $C_v$ is the propositional condition associated with node $v$ and $\tau_v$ is the node's temporal position (from the acyclicity structure). For action leaves, $p_v$ is *capability credence* — "can I execute this?" For condition leaves, $p_v$ is *state credence* — "will this hold?" Both are conditional on $M_t$ and update whenever $M_t$ updates. This is the mechanism by which Section I's adaptive machinery enters the strategy: $M_t$ changes → leaf credences change → status propagation produces new terminal credences.

**Edge semantics.** Each edge carries a single credence weight:

$$p_{ij} = \text{Cr}(j \text{ advances} \mid i \text{ completed},\, M_t)$$

This is the agent's credence that completing step $i$ advances step $j$, given its current model --- its **causal efficacy estimate** for the link. The agent treats $p_{ij}$ as a causal quantity for planning purposes (status propagation, strategy-plan-confidence scoring, action selection). Whether $p_{ij}$ is a *good* estimate of causal efficacy depends on the identification regime of the data that produced it ( #scope-edge-update-causal-validity):

- **Regime A** (intervention-rich: software, laboratory science). The agent's execution-observation pairs are genuine interventions with clean attribution. $p_{ij}$ approximates the interventional probability $P(j \mid do(i), M_t)$.
- **Regime B** (partial intervention: organizational, coordinated action). The agent acts but attribution is blurred by concurrent actions and self-selection. $p_{ij}$ is a partially identified causal estimate, typically biased upward.
- **Regime C** (observation-only: passive monitoring, intelligence analysis). The agent observes associations but does not intervene. $p_{ij}$ is an observational proxy for the causal quantity --- useful for planning but potentially confounded.

The identifiability coefficient $\iota_{ij}$ ( #scope-edge-update-causal-validity) quantifies the strength of the causal interpretation for each edge. When $\iota_{ij} \approx 1$, the agent's credence is well-identified causally. When $\iota_{ij} \approx 0$, the credence is associational. The single-parameter edge design is preserved: $p_{ij}$ is always the agent's working estimate, with $\iota_{ij}$ characterizing its causal warrant separately.

**Status propagation.** Forward pass in topological order, $O(\lvert V \rvert + \lvert E \rvert)$:

$$s_v = \begin{cases} p_v & \text{if } v \text{ is a leaf (base credence)} \\ \prod_{i \in \text{pa}(v)} p_{iv} \cdot s_i & \text{if } \gamma(v) = \text{AND} \\ 1 - \prod_{i \in \text{pa}(v)} (1 - p_{iv} \cdot s_i) & \text{if } \gamma(v) = \text{OR} \end{cases}$$

**Terminal satisfaction conditions.** The root terminal $v_\text{root}$ and any intermediate nodes near the top of the DAG carry **satisfaction conditions**: predicates on environment states/trajectories that the agent treats as operational success criteria for the objective. These conditions operationalize $O_t$ within $\Sigma_t$ — they are the agent's theory of what it means to satisfy the objective. $O_t$ itself lives outside $\Sigma_t$ ( #def-strategy-dimension); the terminal conditions are $\Sigma_t$'s internal encoding of what $O_t$ requires. When $O_t$ changes, terminal conditions must be reassessed and potentially replaced ( #form-structural-change-as-parametric-limit).

**Well-formedness.** $\Sigma_t$ is **$O_t$-well-formed** when the agent believes that achieving the terminal conditions yields a trajectory that satisfies the objective:

$$\Pr\!\left(O_t \text{ satisfied by } \tau \;\middle\vert\; \text{terminal conditions achieved},\; M_t\right) \geq 1 - \epsilon$$

where "$O_t$ satisfied" means $V_{O_t}(\tau)$ exceeds the objective's own satisfaction criterion (formalized as $V_{O_t}^{\min}$ in #def-satisfaction-gap). This is a constraint on the relationship between $\Sigma_t$ and $O_t$, not a separate state object. It is explicit and in-principle assessable, though evaluating it requires the same value-side machinery as $A_O$ — it is not a cheap structural test. Violation triggers terminal reassessment: either the terminals need revision (they don't operationalize $O_t$ correctly) or $O_t$ itself needs revision.

**Strategy self-assessment.** The root node's propagated status:

$$\hat{P}_\Sigma(M_t) = s_{v_\text{root}}$$

is the strategy's **strategy-plan-confidence score** — the DAG's own answer to "will this plan work?" This score is a correct probability only when the DAG is **causally sufficient** — when all common causes of strategy nodes are represented as nodes in the graph ( #deriv-graph-structure-uniqueness, Step 3). When the DAG is causally insufficient (the dominant real-world case — shared infrastructure, common-mode risks, correlated adversary actions introduce latent common causes), $\hat P_\Sigma$ systematically overestimates success likelihood because the AND/OR propagation treats joint failure probability as the product of marginals. See the **Correlation Hierarchy** below for the full treatment.

$\hat P_\Sigma$ is explicitly distinct from $A_O$ ( #def-satisfaction-gap), which optimizes over the entire policy class, and from $V_O(\pi_\text{current})$ ( #def-value-object), which evaluates the current policy. $\hat P_\Sigma$ is cheap to compute ($O(\lvert V\rvert + \lvert E\rvert)$ forward pass) and updates in real time as $M_t$ changes through leaf credences.

### Correlation Hierarchy

*[Discussion (correlation-hierarchy)]*

The AND/OR status propagation computes correct probabilities **if and only if** the strategy DAG is causally sufficient — that is, all common causes of any two strategy nodes are themselves represented as nodes. By the Causal Markov Condition theorem ( #deriv-graph-structure-uniqueness, Step 3), causal sufficiency guarantees independent exogenous noise, which guarantees the Markov factorization, which guarantees independent edge outcomes. **When causal sufficiency fails — the dominant case in complex, multi-stakeholder, or adversarial environments — edge outcomes are correlated and the independence model is biased.**

**Direction and magnitude of bias.** For two binary sibling nodes $X_1, X_2$ with marginal success probabilities $\theta_1, \theta_2$ and covariance $\rho = \text{Cov}(X_1, X_2) \gt 0$ (positive correlation from a latent common cause):

| Node type | True probability | Independence estimate | Bias |
|---|---|---|---|
| **AND** | $\theta_1\theta_2 + \rho$ | $\theta_1\theta_2$ | $+\rho$ (underestimates — conservative) |
| **OR** | $[1-(1-\theta_1)(1-\theta_2)] - \rho$ | $1-(1-\theta_1)(1-\theta_2)$ | $-\rho$ (overestimates — optimistic) |

The independence model error is exactly $\pm\text{Cov}(X_1, X_2)$, with sign determined by node type. AND-nodes are conservative because clustering of successes helps joint success. OR-nodes are optimistic because clustering of failures undermines the redundancy that OR-structure is supposed to provide. Same magnitude, opposite signs.

For strategies with OR-structure near the root (the typical case — multiple alternative paths to the objective), the net bias is overestimation: the agent believes it has more redundancy than it actually does. For AND-heavy strategies (all components must work, no alternatives), the net bias is underestimation. Mixed strategies depend on the graph topology, but OR-dominated roots are far more common than AND-dominated roots in practice.

Four regimes, in order of increasing realism:

| Level | Model | When correct | $\hat P_\Sigma$ status | Sector transfer status | Computation |
|---|---|---|---|---|---|
| **L0: Independence** | AND/OR propagation as-is | Causally sufficient DAG (all common causes explicit) | Correct probability | Prop B.5 (linear), B.5b (componentwise nonlinear): $\alpha_s = \alpha_c$ | $O(\lvert V\rvert + \lvert E\rvert)$ |
| **L1: Augmented DAG (strict prerequisites)** | Strict-prerequisite common-cause nodes added explicitly; AND/OR propagation on augmented graph | Augmented DAG is causally sufficient *and* every modeled common cause has $\theta_{\text{child}\mid\neg C} \approx 0$ | Correct for augmented graph | Prop B.6: $\alpha_\Sigma = \min(1/(n_C+1), \theta_C\pi_j/(n_j+1))$ — three-way gating | $O(\lvert V'\rvert + \lvert E'\rvert)$, larger graph |
| **L1': Mixture form (soft facilitators)** | Conditional sub-DAGs weighted by common-cause state: $\hat P_\Sigma = \theta_C P_\Sigma(G\mid C) + (1-\theta_C) P_\Sigma(G\mid\neg C)$ | Soft-facilitator common causes ($\theta_{\text{child}\mid\neg C} \gt 0$) **with $C$ observable per trial** | Correct for the weighted combination | Prop B.7: $\alpha_{L1'} = \min(1/(n_C+1), \theta_C\pi_{j\mid C}/(n_{j\mid C}+1), (1-\theta_C)\pi_{j\mid\neg C}/(n_{j\mid\neg C}+1))$ — five-way gating. **Refuted when $C$ unobservable** (Fisher rank-1; falls back to plan-level tracking or multi-child joint observation) | $O(\lvert V'\rvert + \lvert E'\rvert)$ per common cause; doubles parametric footprint for affected edges |
| **L2: Full correlation** | Arbitrary joint failure distribution over edges | Always (but requires specifying the full joint) | Correct | Reduces to L0 on the augmented joint state | Exponential in general |

**L0 (Independence)** is the tractable baseline. All formal results in AAT's strategy layer — the sector condition transfer (Prop B.5 in #deriv-edge-credence-dynamics), the persistence schema ( #schema-strategy-persistence), the gradient-based credit assignment ( #disc-credit-assignment-boundary) — are proved under L0. The strategy-plan-confidence error $\delta_s = \hat P_\Sigma - \Phi$ tracks calibration *within* the independence model; $\Phi = P_\Sigma(\boldsymbol\theta)$ is the AND/OR formula at true edge rates, not actual plan success probability.

**L1 (Augmented DAG)** is the practical sweet spot — *for strict-prerequisite common causes*. The agent models correlation structure explicitly by adding common-cause nodes to $\Sigma_t$ and restructuring the DAG so that the common cause is **factored above the correlation it creates**. The construction principle: place the common-cause node as an AND-prerequisite *above* the OR/AND structure whose children it correlates. This ensures that, conditional on the common cause being satisfied, the children are independent and standard AND/OR propagation is correct.

**Scope of the AND-prerequisite construction: strict prerequisites only.** The factoring-above principle requires that the common cause be a *strict* prerequisite — one for which $\theta_{\text{child} \mid \neg C} \approx 0$. Shared infrastructure going down, a required resource being absent, a gating permission being denied: in all of these, the correlated children fail when the common cause fails, so the AND-prerequisite correctly encodes the correlation. When the common cause is instead a *soft facilitator* — favorable market conditions, a supportive team culture, an enabling technology — children have $\theta_{\text{child} \mid \neg C} \gt 0$ and can succeed when the common cause is absent, just less reliably. The AND-prerequisite construction mathematically forces $P(\text{sub-plan} \mid \neg C) = 0$, which strictly understates success probability when $C$ is absent. Soft facilitators therefore fall outside L1's single-pass construction and require one of:

- **Mixture form (L1'):** split the sub-plan into two conditional structures and weight by $P(C)$:
$$\hat P_\Sigma = \theta_C \cdot P_{\Sigma}(G \mid C) + (1 - \theta_C) \cdot P_{\Sigma}(G \mid \neg C)$$
This keeps propagation polynomial but requires maintaining two parallel sub-DAGs per soft-facilitator node. Per-edge credences split into two regimes ($p_{ij \mid C}$ and $p_{ij \mid \neg C}$), doubling the parametric footprint for affected edges.
- **Explicit conditioning (L2 subcase):** $P_\Sigma(G) = \sum_c P(C = c) \cdot P_\Sigma(G \mid C = c)$, summing over common-cause states. For $k$ soft facilitators with binary states, this costs $O(2^k)$ in the number of common-cause states — the exponential blowup L2 was defined to name.

**The gap between L1 (strict) and L2 (arbitrary) was not previously named.** L1' (mixture form) fills this gap at linear cost per soft-facilitator node. The "L1 is the practical default" claim therefore applies most cleanly to strict prerequisites; for mixed environments (strict and soft common causes simultaneously), the correct construction mixes L1 factoring for strict prerequisites with L1' mixtures for soft facilitators. Treating all common causes as strict prerequisites systematically undervalues sub-plans that face soft facilitators (the opposite failure mode from L0's overestimation).

*Example — strict prerequisite* (see #example-L1 for full treatment): Two OR-alternatives sharing infrastructure dependency ($\theta_C = 0.8$, $\theta_{1\mid C} = 0.9$, $\theta_{2\mid C} = 0.7$, and implicitly $\theta_{1\mid\neg C} = \theta_{2\mid\neg C} = 0$ — infrastructure is a strict prerequisite). L0 computes $\hat P_\Sigma = 0.877$; actual is $0.776$ (overestimation = $\rho$, the covariance from shared infrastructure). Naive L1 (common cause as parent of both alternatives, alternatives remain OR-siblings) gives the *same* overestimate because the OR-propagation still treats siblings as marginally independent. Correct L1 ($G = \text{AND}(C, G_{\text{sub}})$ where $G_{\text{sub}} = \text{OR}(A_1, A_2)$) gives the exact answer because $A_1$ and $A_2$ are conditionally independent given $C$ *and because $\theta_{i \mid \neg C} = 0$, so the AND-prerequisite is the correct encoding*. The sector condition is verified (Prop B.6 in #deriv-edge-credence-dynamics) with $\alpha_\Sigma = \min(1/(n_C+1),\;\theta_C(1-\varepsilon)/(n_{A_1}+1),\;\theta_C \varepsilon/(n_{A_2}+1))$ — combining evidence-starvation and exploration-gating effects. B.5b transfers losslessly.

All L0 formal results transfer to correctly constructed L1 DAGs *for strict-prerequisite common causes* because the augmented DAG is a standard AND/OR DAG that satisfies causal sufficiency. For L1' (mixture form) with **observable common cause**, the formal results transfer through Prop B.7 ( #deriv-edge-credence-dynamics) — five-way gating with $\alpha_{L1'} = \min(1/(n_C+1), \theta_C\pi_{j\mid C}/(n_{j\mid C}+1), (1-\theta_C)\pi_{j\mid\neg C}/(n_{j\mid\neg C}+1))$. For L1' with **unobservable common cause**, the per-conditional decomposition is identifiability-obstructed by the Cramér-Rao floor — the per-trial Fisher matrix is rank 1 rather than rank $2K+1$, so no unbiased online estimator on the joint conditional vector admits a sector parameter $\alpha \gt 0$. This is not "open" but structurally refuted; the agent must augment $C$-observability, run multi-child joint observations, or fall back to L0-on-marginals (losing per-conditional diagnostics). The practical challenges are: (1) identifying which common causes matter enough to model explicitly, (2) classifying each identified common cause as strict or soft, (3) verifying $C$-observability for soft cases, (4) restructuring the DAG correctly for each. All four are modeling judgments, not mechanical procedures.

**L2 (Full correlation)** is a mathematical ideal. Specifying the full joint failure distribution over $m$ edges requires $O(2^m)$ parameters, which violates the bounded-cognition constraint that motivates the DAG representation in the first place. L2 is useful as a reference point for characterizing the L0/L1 approximation error, not as a practical representation.

**Choosing among L1, L1', and L2 requires classifying each common cause and verifying observability.** $\theta_{\text{child}\mid\neg C} \approx 0$ → L1 (factor above the correlation, B.6). $\theta_{\text{child}\mid\neg C} \gt 0$ with **$C$ observable** → L1' (B.7, five-way gating). $\theta_{\text{child}\mid\neg C} \gt 0$ with $C$ unobservable → L1' is identifiability-obstructed by the Cramér-Rao floor; either augment $C$-observability (preferred), use L2 explicit conditioning, or fall back to L0-on-marginals (losing per-conditional diagnostics). Mixed-classification environments (some strict, some soft, varying observability) combine L1 factoring for the strict and L1' mixtures for the soft observable. Treating all common causes as strict prerequisites under L1 alone systematically *understates* success on soft-facilitator branches (the symmetric failure mode to L0's overestimation); treating L0 as the default leads to systematic overconfidence — the agent believes it has more redundancy than it actually does (OR-nodes) or more fragility than it actually does (AND-nodes). L0 remains appropriate for domains with genuinely independent risks (independent parallel experiments, diversified portfolios with low correlation) and as a computational stepping stone during strategy construction.

**Detecting latent common causes.** An agent at L0 can detect causal insufficiency *under joint sibling observability generated by its own interventions* — not from on-policy traces alone. On-policy execution alone cannot distinguish the with-and-without-latent-common-cause worlds (the no-go in #der-causal-insufficiency-detection); the unique broadly-available escape is joint sibling observability under exploration, where the agent's interventions ( #der-loop-interventional-access) generate the joint outcome data the test requires. Persistent overestimation of plan success after edge credences have converged is the *signal* of insufficiency ( #result-structural-adaptation-necessity applied to the strategy layer); pairwise covariance among observed siblings is the *test* (positive covariance rejects independence and identifies where to add L1 nodes). Full treatment: #der-causal-insufficiency-detection; numerical instantiation: #example-L1. Summary references in dependent segments that elide the on-policy / interventional distinction should be treated with caution — the load-bearing scope is "joint sibling observability under exploration," not "from observational data alone."

**Scope of the terminal construction.** Terminal conditions as Boolean predicates with AND/OR aggregation work naturally for threshold, constraint, and composite objectives. For continuous-valued objectives without natural thresholds, the agent must set an operational threshold — introducing a discretization that is a practical proxy, not a lossless encoding of $V_O$. The primary $O_t$ ↔ theory interface remains $V_O$ through the value object ( #def-value-object); terminal conditions are $\Sigma_t$'s internal operational encoding.

**Single-parameter edges.** Each edge carries one number ($p_{ij}$), not two. An earlier formalism attempt used $(p_{ij}, \theta_{ij})$ where $\theta$ was "contribution magnitude." This was dropped because the AND/OR combination rules at nodes absorb $\theta$'s role — the complexity budget goes to one bit per node ($\gamma$) instead of one float per edge.

**Edge-credence presentation coordinates.** Each edge's single-number credence has two equivalent presentations: the *probability-space* coordinate $p_{ij} \in [0, 1]$ (convenient for AND/OR propagation and interpretation) and the *log-odds* coordinate $\lambda_{ij} = \log(p_{ij}/(1 - p_{ij})) \in \mathbb{R}$ (the unique additive-evidence coordinate forced by the evidential-additivity axiom; see #deriv-edge-update-natural-parameter). The two coordinates are related by the sigmoid $p_{ij} = \sigma(\lambda_{ij})$. AAT's AND/OR status propagation and Correlation Hierarchy algebra operate in probability space; the continuous-gradient update machinery in #disc-credit-assignment-boundary operates natively in log-odds and projects back to $[0, 1]$ via sigmoid at the readout interface. Props B.1–B.7 of #deriv-edge-credence-dynamics are stated in moment-parameter (probability-space) form; their sector-parameter content is Fisher-equivalent in either coordinate.

### Acyclicity is Derived

*[Derived (from causal-structure + finite planning horizon)]*

Each node in $\Sigma_t$ represents a future event or state with temporal position $\tau_i \gt t$. An edge $X_i \to X_j$ requires $\tau_i \lt \tau_j$ ( #post-causal-structure: causes precede effects). A cycle $X_i \to X_j \to \cdots \to X_i$ would require $\tau_i \lt \tau_j \lt \cdots \lt \tau_i$, which is impossible for a real-valued time index.

Strategies involving iteration ("try A, if fail try B, if fail try A again") are acyclic when time-indexed. The sequence unfolds as:

$$A_1 \to \text{check}_1 \to B_1 \to \text{check}_2 \to A_2 \to \ldots$$

Each attempt is a distinct node at a distinct time. The apparent cycle is a linear chain in the unrolled view.

Formally: a finite set with a strict partial order (future events ordered by time) is representable as a DAG. This is a standard result in order theory.

**Scope of the acyclicity result.** This applies to $\Sigma_t$ (the agent's strategy over the future), not to $M_t$'s model of the environment, which may include cyclic causal processes (feedback loops in the physical world, market dynamics, ecosystem interactions). The acyclicity is specific to the purposeful substate.

## Epistemic Status

*Conditional* on the #scope-and-or restriction. The DAG structure itself follows from operational postulates: temporal ordering (acyclicity — exact), probabilistic uncertainty (Cox's theorem — exact; Cox 1946, "Probability, Frequency and Reasonable Expectation," *American Journal of Physics* 14(1):1–13; Jaynes 2003, *Probability Theory: The Logic of Science*, Cambridge University Press, Chapter 2), and the Causal Markov Condition theorem under causal sufficiency (Markov factorization — proved conditional). The full argument is in #deriv-graph-structure-uniqueness: P1 + P2 + causal sufficiency → CMC → DAG with Markov property. The result is *conditional on causal sufficiency* of the strategy (no latent common causes among strategy nodes). Causal sufficiency is a modeling ideal — the agent designed the graph, so *intended* causal relationships are explicit, but environmental common causes routinely go unmodeled in complex domains. When causal sufficiency fails, the Markov factorization breaks down, edge outcomes become correlated, and $\hat P_\Sigma$ overestimates success. This is model inadequacy ( #result-structural-adaptation-necessity), repairable by adding the missing common-cause nodes (L1 augmentation). See the Correlation Hierarchy above for the practical framework.

**Causal sufficiency and edge independence.** The AND/OR status propagation is correct when the DAG is causally sufficient (all common causes represented as nodes) — this follows from the Causal Markov Condition theorem ( #deriv-graph-structure-uniqueness). In complex real-world systems, causal sufficiency is systematically violated: shared infrastructure, common-mode risks, supply chain dependencies, and correlated adversary actions introduce latent common causes. Correlated failure is the dominant case, not the exception. The Correlation Hierarchy (above) characterizes three levels: independence (L0, tractable baseline), augmented DAG (L1, practical sweet spot), and full correlation (L2, mathematical ideal). AAT's formal strategy-layer results are proved under L0 but transfer to L1 (which is just a larger L0-compliant DAG). The independence model remains the tractable foundation for formal analysis; L1 augmentation is the recommended practice for deployment.

The AND/OR parameterization is a parsimony-motivated formulation choice within the strongly motivated graphical structure, not a derived necessity ( #scope-and-or). The single-parameter edge convention is similarly a formulation choice motivated by convergence across three independent attempts.

## Discussion

**The graph structure is sufficient under causal sufficiency; the parameterization is chosen.** The DAG structure follows from temporal ordering (acyclicity — proved) and the Causal Markov Condition theorem under causal sufficiency (Markov factorization — proved conditional; see #deriv-graph-structure-uniqueness). This is a theorem-backed result, not a sketch: the CMC (Spirtes et al. 2000, Pearl 2009) proves that any causally sufficient causal DAG with independent exogenous noise satisfies the Markov factorization. The status is therefore: DAG-with-Markov-property is *sufficient* given operational postulates plus causal sufficiency — the desiderata are satisfied by this representation, but the necessity direction (whether some non-DAG structure could also satisfy them) is an open stronger result ( #deriv-graph-structure-uniqueness). AAT uses AND/OR parameterization within this strongly motivated structure because (a) AND/OR is the most parsimonious complete basis for binary combination, (b) the representation converged across three independent formalism attempts. Alternative parameterizations within the strongly motivated graphical structure are legitimate research directions.

**Combination assignment is principled but fallible.** The question "if I remove one parent, can $v$ still be achieved?" is derivable from $M_t$'s causal model — it's a principled assignment, not arbitrary. But the assignment can be wrong (false AND = pessimistic over-investment; false OR = optimistic under-investment), and should be updateable when evidence reveals a different structural relationship.

**Connection to Pearl's framework.** Under causal sufficiency, the strategy DAG is a causal Bayesian network in the sense of structural causal models, not merely a structural analog: #deriv-graph-structure-uniqueness proves that the operational postulates (P1, P2, P4) plus causal sufficiency yield the Markov factorization via the Causal Markov Condition theorem (Spirtes et al. 2000, Pearl 2009). Pearl's do-calculus therefore applies to status propagation and plan evaluation, with its causal content scoped by the identification regime of the data feeding the edge credences ( #scope-edge-update-causal-validity). In Regime A domains, where the agent performs genuine interventions and observes isolated outcomes, the DAG's edge credences approximate interventional probabilities and do-calculus yields clean causal estimates. In Regimes B and C, the edge credences are the agent's working causal beliefs, updated from data of weaker identification strength. The DAG remains useful for planning --- the agent must act on *some* causal model --- but the strategy-plan-confidence score $\hat P_\Sigma$ inherits the identification weaknesses of its constituent edges. An agent operating primarily in Regime C should treat $\hat P_\Sigma$ as a rough heuristic, not a calibrated probability. When causal sufficiency itself fails (latent common causes among strategy nodes), the Markov factorization is violated and the DAG is the agent's *intended* but uncalibrated causal model; the L1/L1' augmentation in the Correlation Hierarchy is the principled repair.

**Depth penalties on calibration.** Beyond the confidence decay that deeper DAGs suffer ( #der-chain-confidence-decay), the two-edge strategic dynamics analysis ( #deriv-edge-credence-dynamics (Props B.2-B.3)) shows that deeper edges are also harder to calibrate. Edge $k$ in a chain is tested only when all upstream edges succeed, so its effective correction rate is attenuated by $\prod_{j\ltk}\theta_j$ (the evidence-starvation effect). Deeper DAGs therefore face a double penalty: lower aggregate confidence AND slower convergence of edge credences toward truth. This reinforces the structural pressure toward shallow, observable strategies — deep plans require both high per-edge reliability and sustained observability at every intermediate level to remain calibratable.

**Edge independence is a consequence of causal sufficiency, not a separate assumption.** The Correlation Hierarchy (Formal Expression, above) establishes this precisely: the AND/OR propagation's correctness is not a matter of "assuming independence" — it is a consequence of whether the DAG is causally sufficient. The CMC theorem ( #deriv-graph-structure-uniqueness) proves that causal sufficiency → exogenous independence → Markov factorization → correct AND/OR propagation. The assumption is causal sufficiency; independence is the consequence.

*What L0 buys:* Tractable $O(\lvert V\rvert + \lvert E\rvert)$ status propagation; single-parameter edges; clean persistence proofs (the sector condition transfers from per-edge credence to plan value via the Jacobian — Prop B.5 in #deriv-edge-credence-dynamics).

*What L0 costs when the DAG is causally insufficient:* $\hat P_\Sigma$ systematically overestimates success. The strategy-plan-confidence error $\delta_s = \hat P_\Sigma - \Phi$ proved persistent by B.5 tracks calibration *within the L0 model* — $\Phi$ is the AND/OR formula at true edge rates, not actual plan success ( #def-strategic-calibration). Gradient-based credit assignment ( #disc-credit-assignment-boundary) inherits the same bias: the residual $(y_G - \hat P_\Sigma)$ conflates per-edge miscalibration with omitted correlation structure.

*The L1 remedy:* Add common-cause nodes and restructure the DAG so each common cause is factored above the correlation it creates (see Correlation Hierarchy above). The AND/OR propagation then applies correctly to the restructured DAG, and all L0 formal results transfer because the restructured DAG is itself L0-compliant. The key engineering challenge is twofold: identifying which common causes matter, and positioning them correctly in the graph topology.

### Relationship to Moore machines / finite-state automata — behavioral surface vs epistemic interior

The strategy DAG and the Moore machine $(S, A, \tilde A, \delta, \lambda, s_0)$ formalize different aspects of what "strategy" means; they are not competing representations of the same object but representations of *different* objects that both get called "strategy" in different literatures. The Moore machine encodes a *reactive policy* — given the current state and the other agent's last action, produce an output and transition; it captures a complete input-output mapping over an indefinite horizon. The strategy DAG encodes a *causal plan* — a theory of which conditions must hold (AND/OR) and with what credence for the objective to be achieved; it captures the agent's beliefs about the causal structure of its problem. **The Moore machine is the behavioral surface; the strategy DAG is the epistemic interior.**

**Moore machine to DAG (partial embedding).** A Moore machine with $n$ states unrolls over a finite horizon $H$ into a tree of depth $H$ with branching factor $\lvert \tilde A \rvert$. Each path is a sequence of (state, output) pairs — a scenario. The unrolled tree is a DAG (acyclic by construction, per `#deriv-graph-structure-uniqueness`), but it lacks credence weights and AND/OR semantics. To produce a strategy DAG, two pieces of external information must be supplied: (a) probabilities over opponent actions at each branch (from $M_t$); (b) AND/OR combination rules reflecting which branches the agent treats as jointly required vs. alternatively sufficient. The Moore machine does not contain this information — it is agnostic about which opponent responses are likely or which paths matter. The Moore-to-DAG map is *injective on skeletons* but requires external information to complete.

**DAG to Moore machine (lossy compilation).** A strategy DAG can be compiled into a reactive policy by enumerating leaves in topological order and defining a Moore machine state per action leaf that transitions on observed success/failure. This compilation *discards* three pieces of structure: (a) the credence weights (the compiled machine is deterministic); (b) the AND/OR structure (the machine commits to a fixed execution order); (c) the causal semantics (the machine has no representation of *why* actions are ordered this way). The compiled machine executes the plan but cannot reason about it — it cannot recompute plan-confidence when a leaf credence changes, which is exactly what status propagation (`#disc-credit-assignment-boundary`) provides for the strategy DAG.

**Neither representation is strictly more general; the two are *orthogonal*.** Moore machines can represent reactive strategies with no causal model (tit-for-tat, grim trigger) that have no natural DAG form — there is no plan to encode, just a response rule. Strategy DAGs can represent plans with rich conditional structure and uncertainty that would require exponentially many Moore-machine states (because the Moore machine must enumerate every possible observation sequence, while the DAG factors through conditional independence). The orthogonality is structural: behavioral surface vs epistemic interior. The DAG's acyclicity is not a restriction — it is a consequence of temporal indexing per `#deriv-graph-structure-uniqueness`; what looks like a Moore-machine cycle (revisiting state "cooperate" at $t=1$ and $t=5$) is two distinct nodes $v_{t=1}, v_{t=5}$ in the time-unrolled DAG. For finite horizons the two have equivalent expressive power over behavioral sequences, with the Moore machine exponentially more compact for repetitive strategies and the DAG exponentially more compact for plans factoring through conditional independence.

**Composition behaviour.** Miller's product-automaton construction gives *exact* composition: two Moore machines interacting produce a meta-machine with state space $S_1 \times S_2$ and deterministic transitions. AAT's composition closure (`#form-composition-closure`) uses an *approximate* dynamical homomorphism with closure defect $\varepsilon^\ast$. These address different questions. The product automaton asks "what behaviour does the pair produce?" — answer: another automaton, exactly. AAT asks "can this pair be described as a single AAT agent?" — answer: approximately, with bounded error. Even if strategies were Moore machines, composition of *behaviour* would become exact (product automaton) but composition of *agent descriptions* ($M_t, O_t, \Sigma_t$) would still require the approximate framework — the closure defect comes from projecting the joint internal state, not from composing the policy.

**Why AAT uses the DAG rather than the Moore machine.** The defining feature of an adaptive agent (`#scope-adaptive-system`) is that the agent revises its strategy when $M_t$ changes. Strategy revision requires the agent to know *why* it is doing something, not just *what*. A Moore machine specifies what to do but contains no theory of why this is the right thing to do — when $M_t$ changes, the Moore machine has no internal handle to revise from. The strategy DAG carries the causal semantics that strategy revision operates on (per `#disc-credit-assignment-boundary` and the gradient-based candidate signal); compiling to a Moore machine would discard the very structure adaptation requires.

### Composing heterogeneous strategy DAGs (causal-abstraction typing)

The composition-behaviour distinction above — that composing *agent descriptions* needs the approximate framework while composing *behaviour* does not — has a precise mechanism at the strategy layer, and it is order-theoretic, not a magnitude in team size. Composing strategy DAGs $\Sigma_1,\dots,\Sigma_N$ into one macro-strategy $\Sigma_c$ is the causal-model-abstraction question with the arrow reversed: not "when does one high-level model abstract one low-level model?" but "when does one high-level strategy DAG $\Sigma_c$ faithfully abstract the *joint* micro-strategy $\Sigma_1\times\cdots\times\Sigma_N$?" Since the strategy DAG is a causal Bayesian network under causal sufficiency (the "Connection to Pearl's framework" Discussion above), the right object is a *strategy $\tau$-abstraction* — a $\Sigma_c$ with a surjective node map $\tau$ and an intervention map under which the status-propagation diagram commutes — adopting the causal-abstraction framework of Rubenstein et al. (2017), Beckers & Halpern (2019), and Beckers, Eberhardt & Halpern (2020). The composition-closure defect $\varepsilon_\Sigma$ of `#form-composition-closure` and the Beckers–Eberhardt–Halpern approximate-abstraction error are the *same commuting-diagram family but not term-for-term*: the BEH error is a supremum over all interventions and contexts (interventional), $\varepsilon_\Sigma$ is an expectation over the reachable on-policy trajectory distribution (observational), so a $(\tau,\alpha)$-abstraction implies a bounded $\varepsilon_\Sigma$ but not conversely, and BEH leaves its high-level distance application-dependent — the norm-on-graphs choice remains AAT's. The adoption buys the correct type and a strictly-stronger optional target, not a closed defect formula.

**Exact composition is an order-compatibility condition, not a small-$N$ regime.** An exact $\Sigma_c$ ($\varepsilon_\Sigma=0$) exists *iff* the joint micro-strategy's interventional distribution factors through $\tau$ — equivalently, iff on shared nodes the sub-plans' temporal sub-orders are jointly acyclic *and* their AND/OR root semantics agree (the root combinator is dictated by the composite objective via `#scope-composite-agent`, not free). When these hold, $\Sigma_c$ is exact for *all* $N$: compatible heterogeneous strategy composition is dimension-free, the strategy-layer twin of the dimension-free state-composition regime. The agent count never enters. The complementary fixed-topology case — agents sharing one skeleton and disagreeing only on edge-credences — has its own exact closed-form defect ($\varepsilon_\Sigma^{\ast 2}=\lvert E\rvert\cdot\overline{\mathrm{Var}_i[\eta_{\Sigma,i}]}\cdot\mathrm{Var}[r]$, also $N$-free), landed as the strategy-layer instance of the structural-unity axis in `#result-unity-closure-mapping`.

**When shared sub-orders conflict, no exact single-DAG macro-strategy exists.** If shared nodes $S$ carry incompatible sub-orders (agent 1 plans $A\prec B$, agent 2 plans $B\prec A$ on shared $A,B$), the union of the per-agent partial orders is cyclic and this segment's derived-exact acyclicity ("Acyclicity is Derived", above) *forbids* an exact $\Sigma_c$ — non-existence, not a large defect. The minimal admissible $\Sigma_c$ is the **condensation** of the union-order graph by strongly connected components (the unique minimal acyclic quotient; Tarjan): each cyclically-entangled set of shared nodes collapses to one coarse macro-node the composite cannot temporally distinguish. The information destroyed by collapsing an SCC $C$ is exactly the total correlation among the collapsed status variables, so the irreducible composition defect is

$$\varepsilon_\Sigma^{\ast 2} \;=\; \sum_{C\,\in\,\mathrm{SCC}(G_\cup),\;\lvert C\rvert\gt 1}\mathrm{TC}\big(\{s_v\}_{v\in C}\big)\;\le\;\lvert S\rvert\log 2,$$

zero iff the collapsed statuses were independent (the order was spurious), maximal for a deterministic chain (the order was real) — the strategy-layer analog of the Mori–Zwanzig projection residual that governs state composition, with the SCC-condensation as the projection. The bound is **shared-plan-size-bounded and fully $N$-free**: redundant order-conflicts among many agents collapse to the same SCCs (the condensation is idempotent under implied constraints); only *fresh* shared nodes per agent grow the defect, and that growth is linear in plan overlap and attributable to plan design, never to the composition operator. When even the condensation over-coarsens past usefulness, the honest macro-object is a mixture over per-context conditional sub-DAGs — structurally the L1′ mixture form of the Correlation Hierarchy above — whose support (the number of incompatible order-contexts) is itself bounded by the SCC count $\le\lvert S\rvert$, not by $N$.

**Downstream corollary (a Brooks's-Law floor).** Because $\varepsilon_\Sigma^\ast$ is $\lvert S\rvert$-bounded and $N$-free, it cannot by itself flip the composite persistence inequality (CM2) of `#deriv-critical-mass-composition` at large $N$ (it enters only through $\rho_{\text{eff}}=\rho_{\text{ext}}+\varepsilon^\ast\nu_c$): strategy-topology heterogeneity *alone* cannot cause a Brooks's-Law collapse — only coordination overhead can — consistent with `#post-composition-consistency`'s Tier-1M closed form.

*Epistemic status of this subsection.* The $\tau$-abstraction typing is a prior-art adoption (high confidence on the type; the BEH-vs-$\varepsilon_\Sigma$ relation is BEH $\Rightarrow$ bound, with the supremum-vs-expectation / interventional-vs-observational reconciliation named and deliberately left open). The exactness-iff condition and the non-existence under cyclic shared sub-orders rest on this segment's own derived-exact acyclicity. The SCC-condensation total-correlation defect law is solid in structure (the condensation is the classical unique minimal acyclic quotient; total correlation is the collapse loss by the log-odds chain-rule identity) and *conditional on its constant*: whether the $\lvert S\rvert\log 2$ ceiling is tight when intra-SCC statuses are strongly but non-deterministically coupled is one named open sub-question (Working Notes). The subsection is therefore *conditional*, matching the `#form-composition-closure` row it makes concrete.

## Working Notes

- The Correlation Hierarchy (L0/L1/L2) is now first-class in the Formal Expression. The relationship between causal sufficiency, edge independence, and $\hat P_\Sigma$ accuracy is grounded by the CMC theorem. The main open question is practical: what heuristics help agents identify which common causes are worth modeling at L1? This is a domain-specific engineering question, not a theoretical gap.
- The graph-sufficiency argument (P1, P2, P4 + causal sufficiency ⟹ DAG with Markov property via CMC) is proved, not sketched. See #deriv-graph-structure-uniqueness for the full derivation and the parallel to Cox's theorem (Cox is necessary-and-sufficient; this argument is sufficient only). The DAG-with-Markov-property is sufficient given the postulates plus causal sufficiency; the AND/OR parameterization remains a formulation choice. strategy-dag stays typed as Definition because the *parameterization* is chosen, and the necessity of the *graphical structure* itself is an open stronger result.
- Health metrics (groundedness, observability coverage, weighted redundancy, bottleneck scores) are scaffold — engineering quantities for monitoring DAG health, not principled derivations. They may be useful for implementation but should not enter the theory's formal chain.
- **Satisfaction criterion.** $V_{O_t}^{\min}$ is now introduced in #form-objective-functional as a parameter of the objective — the minimum acceptable trajectory value. The well-formedness constraint references it from there, not from #def-satisfaction-gap. The satisfaction gap diagnostic builds on $V_{O_t}^{\min}$ but does not define it.
- **Terminal alignment error.** When the agent achieves its terminal conditions but evaluates $V_{O_t}(\tau) \lt V_{O_t}^{\min}$ on the actual trajectory, the well-formedness belief was wrong — the operational success criteria didn't capture what the objective actually required. This is detectable only through experience (achieve the terminals, evaluate $V_{O_t}$), not through a priori analysis. It triggers terminal reassessment — a structural change in $\Sigma_t$ driven by the $O_t$ ↔ terminal mismatch. Whether this should be formalized as a named diagnostic signal ($\delta_\text{align}$) alongside $\delta_\text{sat}$, $\delta_\text{regret}$, and $\delta_\text{strategic}$ is open.
- **Open (composition defect-constant tightness).** The SCC-condensation defect law in the composition subsection has a clean ceiling $\varepsilon_\Sigma^{\ast 2}\le\lvert S\rvert\log 2$; the *structure* (condensation + total-correlation collapse loss) is solid, but whether the ceiling is tight when intra-SCC status variables are strongly but non-deterministically coupled is not pinned. The closing instance is a two-shared-node worked case ($S=\{A,B\}$, agent 1 $A\prec B$, agent 2 $B\prec A$, Beta-Bernoulli credences) — the strategy-layer analog of the correlated-Kalman numerical instance. Moderate effort; resolving it lifts the defect-constant from conditional to exact. *(Indexed: `spikes/PROPOSED.md` Tier 1 — "SCC-defect-constant tightness (A1 Q1)".)*
- **Open (mixture-support dynamics).** When the SCC-condensation over-coarsens and the macro-object is the L1′-style mixture over incompatible order-contexts, its support is bounded by the SCC count $\le\lvert S\rvert$ *statically*. Whether that support can *grow under the Orient cascade* (agents revising shared sub-orders as $M_t$ changes — terminal reassessment, above) is the one place a genuine dynamical $N$-or-time effect could re-enter; the conjecture is that it stays SCC-count-bounded while the cascade reshuffles which nodes are shared. A follow-on, not a present claim. *(Indexed: `spikes/PROPOSED.md` Tier 2 — "Mixture-support dynamics under the Orient cascade (A1 Q2)".)*


---

### Source: `der-causal-insufficiency-detection.md`

```yaml
---
slug: der-causal-insufficiency-detection
type: derived
status: conditional
depends:
  - result-structural-adaptation-necessity
  - def-strategy-dag
  - der-loop-interventional-access
  - der-causal-hierarchy-requirement
  - def-pearl-causal-hierarchy
  - def-causal-information-yield
stage: draft
---
```


# Derived: Causal Insufficiency Detection

An agent operating at L0 of the Correlation Hierarchy ( #def-strategy-dag) faces a structural impossibility: under purely on-policy execution, no detection mechanism can distinguish an L0-insufficient world (latent common causes present) from an L0-sufficient world matched to the on-policy regime conditionals. This is a consequence of the causal hierarchy theorem ( #def-pearl-causal-hierarchy, #der-causal-hierarchy-requirement) — observational data does not in general identify interventional structure. Detection is therefore *only* possible by capabilities that violate the "purely on-policy" condition: joint sibling observability under exploration (the canonical AAT route, exploiting #der-loop-interventional-access), intermediate-state observability, structural priors, or direct intervention on the candidate latent. The pairwise sibling covariance test is the AAT-canonical detector; the L0 plan-level residual is a degenerate special case of the no-go.

## Formal Expression

### The No-Go Theorem: Purely On-Policy Detection Is Impossible

*[Derived (no-go-on-policy, from causal hierarchy theorem + observational equivalence under sequential short-circuit), conditional on (S1)–(S5) below]*

Let $\mathcal M_{L0}$ be the agent's L0 strategy model with sequential short-circuit AND/OR execution policy $\pi_{L0}$. Let $\mathcal W_{L1}$ be a world with a latent common cause $C$ acting on multiple sibling action propositions, and $\mathcal W_{L0}^\ast$ be an L0 world with edge probabilities $\{\theta_j^\ast\}$ matched to the on-policy regime conditionals of $\mathcal W_{L1}$. Let $\mathbb P_{\pi_{L0}}^{\text{obs}}[\cdot]$ denote the joint distribution over the agent's on-policy observable events under $\pi_{L0}$.

**Observational equivalence.** $\mathbb P_{\pi_{L0}}^{\text{obs}}[\mathcal W_{L1}] = \mathbb P_{\pi_{L0}}^{\text{obs}}[\mathcal W_{L0}^\ast]$.

**No-go conclusion.** Any function of the agent's on-policy observable history alone cannot distinguish $\mathcal W_{L1}$ from $\mathcal W_{L0}^\ast$. Therefore no purely on-policy detection mechanism — no test, statistic, or Bayesian comparison taking only the on-policy distribution as input — can detect L0 causal insufficiency.

**Scope conditions (S1)–(S5).**

- (S1) Pure on-policy execution; no off-policy sampling.
- (S2) Sequential short-circuit AND/OR evaluation.
- (S3) Censored sibling observation: short-circuited siblings are not observed.
- (S4) No interventional access to candidate latents.
- (S5) No structural priors positing specific common causes.

**Tier.** *Exact* for shallow strict-prerequisite cases (2-sibling OR or AND with binary common cause and $\theta_{j \mid \neg C} = 0$ — see #example-L1). *Robust qualitative* for general DAG topology, soft facilitators, and deeper structures: the structural argument transfers, but explicit $\mathcal W_{L0}^\ast$ construction has been carried out only for shallow cases.

**Construction of $\mathcal W_{L0}^\ast$.** For a 2-sibling OR with strict-prerequisite latent $C$, $P(C) = \theta_C$, conditional success rates $\theta_{j \mid C}$:

$$\theta_1^\ast = \theta_C \cdot \theta_{1 \mid C}, \qquad \theta_2^\ast = p_2^c = \frac{\theta_C\,(1 - \theta_{1 \mid C})\,\theta_{2 \mid C}}{1 - \theta_C\,\theta_{1 \mid C}}$$

Direct verification (see #example-L1) shows $\mathbb P_{\pi_{L0}}^{\text{obs}}[\mathcal W_{L1}] = \mathbb P_{\pi_{L0}}^{\text{obs}}[\mathcal W_{L0}^\ast]$ on the three on-policy observable events. The Bareinboim, Correa, Ibeling & Icard (2022) Causal Hierarchy Theorem then gives the no-go: any two SCMs that agree on Level 1 (associational) data cannot in general be distinguished on Level 2 (interventional) questions, and the L0/L1 distinction — whether siblings share a common cause — is precisely a Level 2 question about $P(A_2 \mid do(\neg A_1))$ versus $P(A_2 \mid \neg A_1)$.

**Why this matters.** The no-go is the structural reason the prior aggregate-residual mechanism collapses on-policy: the residual is a function of $\mathbb P_{\pi_{L0}}^{\text{obs}}$, which is identical between the two worlds, so the residual is identically zero under both. The collapse is not a quirk of the residual statistic — it is a special case of the no-go applied to that specific function. No replacement aggregate statistic can do better.

### The Detection Routes: What Circumvents the No-Go

*[Derived (boundary-routes, from no-go scope conditions)]*

The no-go's scope conditions (S1)–(S5) define "purely on-policy." Each condition's violation corresponds to an AAT capability that admits (partial) detection:

| Route | Scope violated | AAT capability | Detection strength |
|-------|----------------|----------------|--------------------|
| (a) $\varepsilon$-exploration | (S1) | SA3 exploration ( #deriv-edge-credence-dynamics Prop B.4) | Partial, scales with $\varepsilon$ |
| (b) Joint sibling observability | (S3) | Covariance test under SA3 + #der-loop-interventional-access | Strong |
| (c) Intermediate observability | (S3) at finer grain | Observability investment ( #der-observability-dominance) | Very strong when available |
| (d) Structural priors | (S5) | Hypothesized common-cause nodes in DAG construction | Prior-quality-dependent |
| (e) Direct intervention on latent | (S4) | Domain-specific latent control | Strongest when available |

The covariance test (route (b)) is the AAT-canonical detector: it uses only machinery the theory already requires (exploration via SA3, interventional data via the loop) and is available in the broadest range of domains. The remaining sections operationalize this primary mechanism.

### Primary Detection Mechanism: Pairwise Sibling Covariance Under Intervention

*[Derived (from loop-interventional-access + independence test, conditional on SA3 exploration providing joint observability)]*

Under L0 (the independence model in #def-strategy-dag's Correlation Hierarchy), sibling outcomes under a common parent are uncorrelated:

$$H_0:\;\operatorname{Cov}(Y_{A_i}, Y_{A_j}) = 0 \quad \forall\; i \neq j \;\text{siblings under the same parent}$$

Under causal insufficiency (latent common cause $C$ acting on multiple siblings), sibling outcomes are positively correlated:

$$H_1:\;\exists\; i \neq j \;\text{with}\; \operatorname{Cov}(Y_{A_i}, Y_{A_j}) \gt 0$$

The agent generates test data through the standard exploration mechanism (SA3 — $\varepsilon$-greedy or similar). On trials where both siblings are observable — the agent tries one and can also observe the other's outcome, or tries them in rapid succession before the environment state changes — it accumulates the empirical covariance:

$$\hat\rho_{ij} = \frac{1}{N}\sum_t (Y_{A_i,t} - \bar{Y}_{A_i})(Y_{A_j,t} - \bar{Y}_{A_j})$$

A significantly positive $\hat\rho_{ij}$ rejects the L0 independence hypothesis. Joint observability ( #der-loop-interventional-access supplies the interventional character; SA3 supplies the joint sampling) is precisely the violation of scope condition (S3) that admits the test under the no-go.

**Detection criterion.** A statistically significant positive $\hat\rho_{ij}$ at sample size $N$ sufficient for the desired test power, after per-edge credences have stabilized:

$$\hat\rho_{ij} \gt z_{1-\alpha}\,\hat\sigma_{\rho_{ij}} / \sqrt{N} \quad\implies\quad \text{DAG is causally insufficient between siblings } i, j$$

(Standard hypothesis-testing form; threshold and test power depend on application.)

**Preconditions for the covariance test.**

1. **Joint observability.** The agent can occasionally observe $(Y_{A_i}, Y_{A_j})$ pairs in the same environment state. Pure short-circuit execution censors one of each pair; SA3 exploration or simultaneous-attempt regimes provide uncensored pairs.
2. **Per-edge credence stabilization.** Edge credences $\hat p_i, \hat p_j$ have stopped drifting at the timescale of the covariance accumulation, so $\bar Y_{A_i}, \bar Y_{A_j}$ are well-defined empirical means.
3. **Approximate stationarity over the test window.** The latent common cause's frequency and the conditional success rates are not drifting faster than the test's accumulation timescale.

When these preconditions hold, $\hat\rho_{ij} \gt 0$ is diagnostic of a missing common cause acting on $(A_i, A_j)$. When they do not, the signal is ambiguous.

### The Aggregate Residual as a Degenerate Special Case of the No-Go

*[Derived (residual-degeneracy, as instance of no-go theorem)]*

A historically prominent diagnostic uses the L0 plan-level residual $\Phi^{L0}(\hat{\boldsymbol p}) - \bar y_G$ as a detection signal. The no-go theorem subsumes this as a special case: under pure on-policy execution, the residual is *identically zero* in both $\mathcal W_{L1}$ and $\mathcal W_{L0}^\ast$.

**Direct verification.** Under sequential short-circuit, the agent's empirical credences converge to the on-policy regime conditionals: $\hat p_j \to p_j^c$. Plugging these into the L0 arithmetic recovers the chain rule of probability (e.g., for OR: $1 - (1 - p_1^c)(1 - p_2^c) = 1 - P(\neg A_1, \neg A_2) = P(A_1 \cup A_2)$, which equals $\bar y_G$ under the executed policy). The residual is zero by algebraic identity.

This is *not* a separate finding from the no-go: it is the no-go's prediction for the specific aggregate-residual statistic. The no-go forbids *any* on-policy statistic from distinguishing $\mathcal W_{L1}$ from $\mathcal W_{L0}^\ast$; the residual evaluates to the same value (zero) in both, as expected.

**Off-policy boundary.** Under $\varepsilon$-exploration (route (a)), the residual scales as $O(\varepsilon)$ to leading order with sign matching the dominant node-type bias ($+$ for OR-heavy, $-$ for AND-heavy):

$$\Phi^{L0}(\hat{\boldsymbol p}) - \bar y_G = \varepsilon \cdot R + O(\varepsilon^2), \quad \operatorname{sign}(R) = \operatorname{sign}(\rho)$$

where $R$ is structure-dependent and recovers the marginal-limit $\rho$ at $\varepsilon = 1$. *[Heuristic]* The qualitative form is robust; the exact coefficient depends on the gap between conditional and marginal credences. The widely-quoted "$\varepsilon \cdot \rho$" scaling is correct as an order-of-magnitude statement. For a 2-sibling OR with conditional credences $p_j^c$, the exact two-OR formula is $\varepsilon R_1 - \varepsilon^2 R_2$ with $R_1 - R_2 = \rho$; the leading-order coefficient $R_1$ is structure-dependent and equals $\rho$ only at $\varepsilon = 1$.

The residual is therefore a *confirmatory* signal under route (a): when the agent has material off-policy exploration and the covariance test (route (b)) has localized a candidate latent, the residual sign confirms the bias direction. It is not a primary detector and cannot replace the covariance test.

### From Detection to L1 Construction

*[Derived (from positive covariance signal + L1 construction principle in #def-strategy-dag)]*

Once the agent detects $\hat\rho_{ij} \gt 0$ between siblings $A_i$ and $A_j$, it knows a latent common cause exists but not its identity. The construction process:

1. **Hypothesize** a common-cause node $C$ that explains the correlation.
2. **Estimate** $\theta_C$ from the pattern of joint outcomes. The joint failure rate $P(A_i\text{ fails}, A_j\text{ fails})$ exceeds $(1-\theta_i)(1-\theta_j)$ by $\hat\rho_{ij}$; the excess localizes the common cause's frequency.
3. **Restructure** the DAG: factor $C$ above the correlated siblings ( #def-strategy-dag, L1 construction principle: factor the common cause above the correlation it creates).
4. **Re-estimate** conditional edge credences $\theta_{k\mid C}$ from the data, conditioned on the inferred $C$ state.

This is structural adaptation ( #result-structural-adaptation-necessity) at the strategy level: the agent changes its model class from L0 to L1, adding representational capacity for a pattern the L0 model cannot express. The cost is the standard cost of structural change: temporary performance degradation while the new credences converge, and increased graph complexity. (Soft-facilitator common causes require L1' rather than L1 — see #def-strategy-dag and #example-L1 for the strict-prerequisite vs soft-facilitator distinction.)

### Diagnostic CIY

*[Discussion (diagnostic-ciy)]*

Which actions are most informative for detecting latent common causes? Under the no-go, only actions that violate one of (S1)–(S5) yield detection signal. The explore-exploit tradeoff extends with a third axis tied to the boundary characterization:

- **Exploit**: pursue the current best plan (no scope violation; no detection signal).
- **Explore**: test unknown edges for individual success rates (route (a); partial detection).
- **Diagnose**: test known edges for joint correlation structure (route (b); strong detection).

Diagnosis is a form of internal exploration — the agent probes its own model's structural assumptions by violating (S3) deliberately, generating joint sibling outcomes that the no-go forbids the agent to obtain on-policy. The information value of diagnostic actions is highest when:

- Edge credences have converged (the agent has good marginals/conditionals but unknown joint structure).
- Joint outcomes for sibling pairs are observable in the same environment state (the covariance test has data — route (b) is operational).
- The agent has sufficient off-policy budget that the secondary residual signal corroborates (route (a) is also operational).

## Epistemic Status

*Conditional* on the no-go's scope conditions (S1)–(S5) and on strategy-layer instantiation of #result-structural-adaptation-necessity. The **no-go theorem** is *exact* for shallow strict-prerequisite cases (2-sibling OR or AND, single binary common cause) by direct construction; *robust qualitative* for general DAG topology, soft facilitators, and deeper structures. The structural argument (observational equivalence of regime-conditional L0 and latent-cause L1) transfers to the general case; explicit construction of $\mathcal W_{L0}^\ast$ has been carried out only for shallow cases.

The **boundary characterization** (routes (a)–(e)) is *robust qualitative*: each route maps to a specific scope-condition violation and to existing AAT machinery, but the precise detection power of each route depends on domain particulars. Routes (a) and (b) have explicit AAT scaffolding ( #deriv-edge-credence-dynamics, #der-loop-interventional-access); routes (c)–(e) depend on domain capability.

The **primary detection mechanism** (pairwise sibling covariance) is *robust qualitative*: standard hypothesis testing applied to interventional data from the feedback loop, with explicit preconditions. Its sensitivity depends on how cleanly the agent can separate sibling-covariance signal from edge-credence noise at convergence; in adversarial or fast-drifting environments the test's effective sample size shrinks.

The **aggregate residual** as a confirmatory signal is *exact* for the on-policy collapse (no-go's prediction is direct); the off-policy mixed-regime scaling is *heuristic* (linear-in-$\varepsilon$ with structure-dependent coefficient).

The **detection-to-construction pipeline** is *discussion-grade*: the trigger is the (statistically rigorous) covariance signal, but the specific procedures for estimating $\theta_C$ and $\theta_{k\mid C}$ from correlated outcome data are domain engineering.

### What Cannot Be Detected

By the no-go and its boundary characterization, several latent structures remain undetectable by *any* AAT route:

- **Latents with no joint-observability route.** If the latent affects siblings that cannot be jointly observed (mutually exclusive with long horizons, no cause-indicator availability, no intervention capability, no informative prior), the no-go applies in full strength and detection is impossible.
- **Latents affecting only one edge.** By definition not common causes; appear as noise in individual edge credences.
- **Latents too rare to produce observable joint outcomes.** Even with route (b) operational, a latent with $\theta_C \approx 1$ rarely reveals itself — the agent needs enough $C = 0$ events to estimate the covariance.
- **Negatively-correlating latents.** The formulation assumes positive correlation from shared enabling factors. Negative correlation (competing for a shared resource) produces the opposite bias pattern and requires a different model.

These limitations parallel the information-theoretic underdetermination in #disc-credit-assignment-boundary: detection requires data with the right structure, and the no-go specifies precisely what "right structure" means.

## Discussion

**Why the no-go is a strengthening, not a softening.** The prior framing ("the residual mechanism collapses on-policy") was a local observation about one statistic. The no-go is the structural reason: any on-policy statistic must collapse, because the on-policy distribution is identical between L0 and L1 worlds matched on regime conditionals. The covariance test is not just *a* working detector — it is the unique broadly-available violation of the no-go's scope. This sharpens the load-bearing of `#der-loop-interventional-access`: without the loop's interventional data, the no-go forbids detection entirely; with it, route (b) is operational.

**Connection to Pearl's hierarchy.** The L0/L1 distinction is a Level 2 distinction in Pearl's framework — it concerns whether $P(A_2 \mid do(\neg A_1)) = P(A_2 \mid \neg A_1)$. The Causal Hierarchy Theorem (Bareinboim, Correa, Ibeling & Icard 2022, Theorem 1) proves that Level 2 distinctions are not in general identifiable from Level 1 (associational) data. The no-go is the AAT-specific instantiation: on-policy data is Level 1; the L0/L1 question is Level 2; therefore detection requires more than on-policy data. The five circumvention routes are all ways the agent obtains supra-Level-1 information.

**The censoring mechanism is the structural source.** Sequential short-circuit evaluation is what makes on-policy data Level 1 only — it censors the joint outcomes that would constitute Level 2 evidence. An agent that *did not* short-circuit would obtain joint sibling outcomes naturally, and the no-go would not apply. But short-circuit is forced by efficiency: testing $A_2$ when $A_1$ has already succeeded is wasted action. The no-go is therefore a tradeoff between execution efficiency (favoring short-circuit) and structural diagnosis (favoring joint observation). SA3 $\varepsilon$-exploration is the AAT compromise: short-circuit by default, occasional non-short-circuit excursions that pay the efficiency cost to maintain detection capability.

**Connection to the orient cascade.** The detection signal enters the orient cascade ( #der-orient-cascade) at step 4c (causal-sufficiency check). Step 4c's reference to "pairwise sibling covariance under an augmented test" aligns with the primary detection mechanism here. The no-go strengthens the cascade's load-bearing: step 4c is not "one possible diagnostic" but "the unique broadly-available diagnostic given the structural impossibility of purely on-policy detection."

**Connection to the broader identifiability-floor pattern.** The no-go is one of an emerging class of structural impossibility results in AAT — limits on what can be inferred from limited information, derived from external information-theoretic theorems. See #disc-identifiability-floor for the meta-pattern collecting this result alongside the L1' mixture-identifiability obstruction ( #deriv-edge-credence-dynamics Prop B.7) and the open causal-IB extension for interventional relevance variables.

**Domain instantiations.** The covariance test (route (b)) applies concretely in:
- **Software deployment**: two services sharing infrastructure fail together more often than independent failure rates predict → add infrastructure-health node.
- **Military operations**: two concurrent operations fail together under adverse weather → add weather-condition node.
- **Investment**: two positions lose value together during market stress → add market-regime node.
- **Organizational strategy**: two initiatives stall together during leadership transitions → add organizational-stability node.

In each, what makes detection feasible is the agent's ability to occasionally observe *both* sibling outcomes — the route (b) capability. Pure short-circuit ("only run service B if A is down") suppresses the joint-observation events the test relies on; some routine joint exposure is necessary. When joint observation is impossible (routes (b) and (c) both unavailable) and intervention on the candidate latent is impossible (route (e) unavailable), the agent must rely on structural priors (route (d)) — domain knowledge positing the common cause. This is the regime in which intuition-driven causal modeling is the only tractable approach.

## Findings

### On-Policy L0 Insufficiency Is Structurally Undetectable

**Brief:** An agent operating with a strategy model that assumes its action propositions are causally independent (an L0 model) faces a structural impossibility when its world contains a latent common cause acting on multiple of those actions: under purely on-policy execution, no test, statistic, or Bayesian comparison built from the agent's observable history can distinguish the latent-cause world from a no-latent-cause world whose edge probabilities are matched to the on-policy regime conditionals. The two worlds emit identical on-policy distributions. This is not a quirk of any particular diagnostic — it is the agent-theoretic instance of the Causal Hierarchy Theorem applied to the L0/L1 distinction, which is a Level-2 question being asked of Level-1 data. The agent that wants to discover its own model's structural insufficiency must source data the on-policy regime structurally cannot produce.

**Impact:** Reframes exploration from a discretionary diagnostic activity into a structural prerequisite for self-correction at the strategy layer. Each scope-condition violation (S1)–(S5) maps to a specific AAT capability that admits partial detection — most importantly, joint sibling observability under exploration, which lifts `#der-loop-interventional-access` from "useful machinery" to "the unique broadly-available violation of the no-go." Downstream, this hardens the orient cascade's causal-sufficiency check from "one possible diagnostic" to "the only widely-applicable diagnostic"; it explains why the prior aggregate-residual mechanism collapses on-policy (the residual is one statistic the no-go forbids, and *every* on-policy statistic is forbidden); and it gives a precise account of when L0→L1 escalation can and cannot be triggered from the agent's own data.

**Novelty Claim:** *Claim differentiation* on the framing of why structure-aware exploration is required. Causal bandit and causal MDP work under hidden confounding establishes that observational and interventional data are non-interchangeable and that intervention can be necessary for low-regret learning; this finding sharpens that line into a no-go for *self-diagnosis* under policy-perfect execution, tied to latent strategic correlation structure rather than to regret minimization, and characterizes five boundary routes by which AAT machinery escapes it.

**Related Work:**

| ASF concern | Prior-art language | Relationship / Positioning |
|---|---|---|
| Observational vs experimental data are non-equivalent under hidden confounding | Bareinboim, Forney & Pearl 2015, "Bandits with Unobserved Confounders" *NeurIPS* (published 2015, found 2026-04 via Undermind report) | *conceptual precursor* — the underlying observational/interventional asymmetry is shared; this finding recasts it as a no-go on agent self-diagnosis rather than a regret bound on action selection |
| Sequential extension to MDPs | Zhang & Bareinboim 2016, "Markov Decision Processes with Unobserved Confounders" (published 2016, found 2026-04) | *conceptual precursor* — sharpens the bandit asymmetry to sequential control; the present finding's L0/L1 distinction is the strategy-DAG analog at the structural-detection layer rather than the policy-optimality layer |
| Naive randomization can be insufficient under confounding | Forney, Pearl & Bareinboim 2017, "Counterfactual Data-Fusion for Online Reinforcement Learners" *ICML* (published 2017, found 2026-04) | *conceptual precursor* — narrows the gap between generic exploration and structure-aware experimentation; the present finding's covariance test under joint sibling observability is one such structure-aware mechanism, derived as the unique broadly-available violation of the no-go's scope conditions |
| Not all interventions are useful | Lee & Bareinboim 2018, "Structural Causal Bandits" *NeurIPS*; Lee & Bareinboim 2020, "Characterizing Optimal Mixed Policies" *NeurIPS* (published 2018/2020, found 2026-04) | *conceptual precursor* — closest formal neighborhood for "exploration design"; the present finding addresses a different question (when *any* on-policy diagnosis is impossible) but inherits the principle that not all interventional data carries equal structural-detection value |
| Exploration as epistemic-value drive | Friston, Rigoli, Ognibene, Mathys, FitzGerald & Pezzulo 2015, "Active inference and epistemic value" *Cognitive Neuroscience* 6:187–214 (published 2015, found 2026-04) | *adjacent literature* — weaker threat because EFE-based exploration reduces uncertainty under the generative model rather than Pearl-style observational equivalence under hidden common causes; the structural-undetectability claim does not arise in the EFE framework, which presumes a generative model expressive enough to represent the latent |
| Theorem the no-go imports | Causal Hierarchy Theorem: SCMs agreeing on Level 1 may disagree on Level 2 (Bareinboim, Correa, Ibeling & Icard 2022, in *Probabilistic and Causal Inference: The Works of Judea Pearl*; published 2022, found 2025) | *formal antecedent* — the no-go is the AAT-specific instantiation; the L0/L1 distinction is precisely a Level-2 question (concerns $P(A_2 \mid do(\neg A_1))$ vs $P(A_2 \mid \neg A_1)$) being asked of on-policy Level-1 data |

**Search Log:**

- 2026-04 (*nominally comprehensive*, via `ref/Novelty_defense_and_integration.md` Pillar 1): Undermind report on the causal-bandits-and-MDPs-under-hidden-confounding literature, plus active-inference epistemic-value exploration, established the prior-art landscape; verdict was *Conceptual Precursor* (High confidence). The closest formal neighborhood is the Bareinboim/Zhang/Forney/Lee line; no paper surveyed states the claim in the same form (no-go for self-diagnosis under policy-perfect execution tied to latent strategic correlation). The defense strategy positions ASF's increment narrowly: a no-go theorem on structural detection rather than a regret bound on action selection, with five explicit boundary routes mapped to existing AAT machinery.
- 2025 (*targeted*): Bareinboim, Correa, Ibeling & Icard 2022 identified as the formal antecedent for the Causal Hierarchy Theorem invocation; the segment's invocation of the CHT was already grounded in this source before the comprehensive Pillar-1 defense.

## Working Notes

- The general-topology construction is a structural argument; the explicit $\mathcal W_{L0}^\ast$ for arbitrary AND/OR DAGs with mixed common-cause patterns has not been carried out. For load-bearing application of the no-go to specific complex topologies, the construction should be specialized. Currently the load-bearing applications (orient-cascade step 4c, strategy-dag's L0/L1 escalation principle) reference shallow strict-prerequisite cases for which the no-go is exact.
- The boundary characterization's routes (c) and (e) depend on domain capability and are not formalized in AAT beyond cross-references to `#der-observability-dominance` and `#der-loop-interventional-access`. A future refinement could quantify "detection power" per route as a function of domain parameters (e.g., observability cost, intervention availability, prior strength).
- The no-go is asymmetric: it forbids on-policy *detection* of L1 from L0, but it does *not* forbid on-policy *parameter learning within L0*. The agent can learn its L0 conditionals to arbitrary precision on-policy; it just cannot determine whether those conditionals hide a latent. This distinction sharpens the diagnosis-vs-calibration split that #result-structural-adaptation-necessity makes at the parametric/structural boundary.
- The CHT (Bareinboim et al. 2022) is invoked as an external theorem. AAT inherits its conditions (well-defined SCMs over compatible variable sets); these are satisfied for the strategy-DAG setting by construction.


---

### Source: `deriv-graph-structure-uniqueness.md`

```yaml
---
slug: deriv-graph-structure-uniqueness
type: derivation
status: conditional
depends:
  - def-strategy-dag
  - der-chain-confidence-decay
  - norm-explicit-strategy-condition
  - post-causal-structure
stage: claims-verified
---
```


# Derivation: Graph Structure Uniqueness

Operational requirements on the agent's representation — directed temporal ordering, probabilistic uncertainty, and the ability to test strategy components — are *sufficient* for the strategy to be a directed acyclic graph with the Markov factorization property. The argument parallels Cox's theorem for probability in *form* but not yet in *strength*: Cox's theorem is necessary-and-sufficient (the only measure satisfying the desiderata is probability); this result is sufficient only (the desiderata guarantee DAG+Markov, but no one has shown a non-DAG structure cannot satisfy them). Acyclicity and directed edges are *proved* from temporal ordering over a finite horizon; the Markov factorization is *proved under causal sufficiency* via the Causal Markov Condition theorem (Spirtes–Glymour–Scheines, Pearl). A fourth postulate (observable intermediates) is required for localized strategic diagnosis but not for the representation or persistence results themselves.

**How far the Cox parallel goes.** Cox's theorem starts from desiderata on how a rational agent should quantify uncertainty (consistency, universality, continuous functional composition) and proves that the *only* measure satisfying them is probability — necessity. This segment starts from desiderata on how a bounded agent can represent its strategy under causal action (directed temporal order, probabilistic edge uncertainty, causal sufficiency of the chosen nodes) and proves that DAG+Markov *suffices* to satisfy them — sufficiency. The necessity direction — no non-DAG structure (factor graphs, junction trees with cyclic message schedules, chain graphs) can satisfy P1–P4 plus causal sufficiency — is not established here. In practical terms this gap is unimportant because the proved sufficiency gives a rigorous grounding for the DAG structure; claims that AAT's strategy *must* be a DAG should be read as "must-if-sufficient-via-this-route," not as a proved necessity. A stronger Cox-style result is open. The placement of the DAG structure on a footing comparable to probability — a consequence of operational requirements rather than a modeling convenience — holds in the sufficiency direction; the full parallel with Cox awaits a uniqueness argument.

## Formal Expression

### The Postulates

Four properties that a strategy representation must satisfy. Each is independently motivated from the adaptive-systems foundation.

#### P1: Directed Temporal Ordering

*[Derived (from #post-causal-structure)]*

If component $A$ of the strategy causally produces component $B$, then $A$ temporally precedes $B$. The strategy representation must respect this directionality — edges point from causes to effects, from actions to outcomes, from prerequisites to goals.

This is a consequence of the temporal postulate ( #post-causal-structure): the arrow of time is constitutive, not incidental. Reversing a causal edge would mean effects precede causes, which is physically impossible.

#### P2: Probabilistic Uncertainty

*[Derived (from Cox's theorem)]*

The agent's uncertainty about whether each step of the strategy will succeed must be quantified by a measure satisfying Cox's axioms (consistency, universality, non-negativity). The unique such measure is probability (Cox 1946, "Probability, Frequency and Reasonable Expectation," *American Journal of Physics* 14(1):1–13; modern exposition in Jaynes 2003, *Probability Theory: The Logic of Science*, Cambridge University Press, Chapter 2). The agent may use other representations internally (confidence scores, fuzzy logic), but these must be mappable to probability to be consistent.

#### P3: State-Local Revisability

*[Derived (from #der-chain-confidence-decay + bounded computation)]*

When the agent observes evidence about one component of its strategy (e.g., "step 3 succeeded" or "prerequisite 2 is blocked"), it must be able to update its beliefs about that component and its consequences without recomputing the entire strategy from scratch.

**Why this is forced, not chosen:**

*From fragility.* Additive log-confidence ( #der-chain-confidence-decay) means longer chains are exponentially less reliable. The agent will frequently encounter partial failures. Each partial failure requires re-evaluation of the affected portion of the strategy. If each re-evaluation requires full recomputation, the agent's planning tempo $T_\Sigma$ is catastrophically slow — potentially violating the strategy persistence condition.

*From bounded computation.* The agent has finite computational resources (the IB constraint applies to planning as well as model maintenance). Full recomputation of a strategy with $N$ components costs $O(N)$ or worse. Local revision costs $O(\lvert\text{affected}\rvert)$, which can be much smaller.

*From the persistence condition.* Strategy must be revised faster than the environment invalidates it. Local revision directly increases $T_\Sigma$ by reducing the per-update cost. An agent that must recompute everything on each update has lower $T_\Sigma$ and is more likely to fall below the persistence threshold.

#### P4: Observable Intermediates

*[Derived (from #der-chain-confidence-decay + monitoring requirement)]*

To support **localized strategic diagnosis and revision**, the strategy representation benefits from internal checkpoints — observable states between the initial action and the final goal — that the agent can monitor to detect partial failure.

Without intermediates, the agent cannot detect chain failure until the final outcome. By the time the final outcome reveals failure, all intermediate actions are wasted. With intermediates, the agent can detect failure at step $k$ and revise, saving the cost of steps $k+1$ through $n$. The value of early detection grows with chain length, because longer chains fail more often (P2 + #der-chain-confidence-decay).

**Observable intermediates are not required for strategy representation or persistence.** When intermediates are unobservable, plan-level tracking ( #schema-strategy-persistence, Case 3) preserves the sector condition at the cost of per-edge diagnostic resolution — the agent knows the plan is failing but cannot localize which step needs revision ( #der-observability-dominance). P4 is therefore a requirement for *strong diagnostics*, not for strategy representation per se. The observability investment tradeoff ( #der-observability-dominance) quantifies the payoff: making an intermediate observable improves the sector parameter from $1/(n_\Phi + 1)$ (plan-level) to $\min(1/(n_1+1),\; \theta_1/(n_2+1))$ (per-edge weakest-link).

### The Derivation

#### Step 1: P1 implies directed edges

Each component $X_i$ of the strategy has a set of direct causes $\text{Pa}(X_i)$ — the components whose outcomes directly influence $X_i$'s outcome. P1 requires that these causal relationships are directed: $\text{Pa}(X_i)$ temporally precedes $X_i$. This gives directed edges $\text{Pa}(X_i) \to X_i$.

#### Step 2: P2 implies probability distributions on edges

Each edge carries uncertainty: $P(X_i \mid \text{Pa}(X_i))$. By P2 (Cox), this is a probability distribution. The joint distribution over all strategy components is some $P(X_1, \ldots, X_n)$.

#### Step 3: Causal sufficiency implies the Markov condition (proved)

*[Derived (Conditional on causal sufficiency of $\Sigma_t$)]*

**Claim.** For a causally sufficient strategy DAG, the Markov factorization property is a theorem — a consequence of the Causal Markov Condition (CMC).

**The Markov factorization property.** Each variable $X_i$ is conditionally independent of its non-descendants given its parents:

$$X_i \perp \text{NonDesc}(X_i) \mid \text{Pa}(X_i)$$

Equivalently, the joint distribution factorizes as:

$$P(X_1, \ldots, X_n) = \prod_{i=1}^{n} P(X_i \mid \text{Pa}(X_i))$$

(The equivalence holds for positive distributions — Lauritzen 1996, Theorem 3.27.)

**The argument has five parts:**

**(a) The DAG is a causal model.** P1 establishes that edges represent causal relationships: completing a parent step causally advances the child step. P2 establishes probabilistic uncertainty over outcomes. Together: $\Sigma_t$ is a causal DAG in the sense of structural causal models (Pearl 2009, Definition 7.1.1) — each node's outcome is determined by its parents' outcomes (through the causal mechanism encoded in the edge credences) plus exogenous uncertainty specific to that step. Formally, each node admits a structural equation:

$$X_i = f_i(\text{Pa}(X_i), \varepsilon_i)$$

where $f_i$ is the local causal mechanism and $\varepsilon_i$ is the exogenous noise (the residual uncertainty at step $i$ not determined by its parents).

**(b) Causal sufficiency implies exogenous independence.** The exogenous terms $\varepsilon_i$ are mutually independent if and only if no unmodeled common cause affects two or more nodes in the graph. This is precisely the **causal sufficiency** assumption: every variable that is a direct common cause of two or more nodes in $\Sigma_t$ is itself a node in $\Sigma_t$.

For agent-constructed strategies, causal sufficiency is a **modeling ideal, not a typical condition**. The agent designed the graph, so all *intended* causal relationships are explicit — but environmental common causes (shared infrastructure, weather, market shifts, correlated adversary actions) routinely affect multiple strategy steps without appearing as nodes. In complex, multi-stakeholder, or adversarial environments, causal insufficiency is the dominant case ( #def-strategy-dag, Correlation Hierarchy). When an environmental factor is omitted, the exogenous terms become correlated and the Markov condition fails. This is model inadequacy ( #result-structural-adaptation-necessity), and the remedy is to add the missing common-cause node — but identifying which common causes matter is a modeling judgment, not a mechanical procedure ( #def-strategy-dag, L1 construction principle). The proof's conditional on causal sufficiency is therefore a condition on model quality: the result holds exactly when the DAG is well-constructed, approximately when it is close, and fails when major common causes are missing. The Correlation Hierarchy in #def-strategy-dag provides the practical framework: L0 (independence, this proof's assumption) gives tractable results; L1 (augmented DAG with explicit common-cause nodes) is the practical default in complex domains; L0 formal results transfer to correctly constructed L1 DAGs.

**(c) The Causal Markov Condition theorem.** For a DAG $G$ over variables $V = \{X_1, \ldots, X_n\}$ with structural equations $X_i = f_i(\text{Pa}(X_i), \varepsilon_i)$ where the $\varepsilon_i$ are mutually independent:

$$P(X_1, \ldots, X_n) = \prod_{i=1}^{n} P(X_i \mid \text{Pa}(X_i))$$

This is the **Causal Markov Condition** — a proved theorem, not a modeling assumption. The standard references are Spirtes, Glymour, and Scheines (2000, Theorem 3.4) and Pearl (2009, §1.4.1, Theorem 1.4.1). The proof applies the chain rule in topological order: $P(X_1, \ldots, X_n) = \prod_i P(X_i \mid X_1, \ldots, X_{i-1})$, then uses the independence of $\varepsilon_i$ to show that conditioning on all predecessors reduces to conditioning on parents only. Each non-parent predecessor's influence on $X_i$ is fully mediated through the parents — its direct contribution enters through the causal mechanism $f_i$, not through $\varepsilon_i$.

**(d) P3 as consequence.** State-local revisability (P3) was originally stated as an independent postulate. The CMC reveals it is a *consequence* of the causal structure under causal sufficiency: since $X_i \perp \text{NonDesc}(X_i) \mid \text{Pa}(X_i)$, updating beliefs about $X_i$ requires only $\text{Pa}(X_i)$ — local revision is automatically correct. No information from the rest of the graph changes the conditional distribution of $X_i$ given its parents. P3 was motivated as an operational requirement (agents *need* local revision for computational tractability, and the persistence condition demands it). The CMC shows the requirement is automatically satisfied by any causally sufficient causal DAG. The two arguments converge from different directions: P3 says local revision is *needed*; the CMC says it is *guaranteed* (under causal sufficiency).

**(e) Connection to edge independence.** The CMC's exogenous independence condition ($\varepsilon_i$ mutually independent) is precisely the **edge-independence assumption** in the AND/OR status propagation ( #def-strategy-dag). When exogenous noise terms are independent, edge outcomes are conditionally independent given parents, and the AND/OR formulas compute correct probabilities. When they are correlated (causal insufficiency — latent common causes), the AND/OR propagation systematically overestimates success because it treats joint failure probability as the product of marginals. The validity of the Markov factorization and the validity of the independence model are the *same condition*: causal sufficiency of $\Sigma_t$. See #def-strategy-dag for the full treatment of correlated failure as the primary case.

**Assembling (a)-(e).** P1-P2 establish that $\Sigma_t$ is a causal DAG with probabilistic uncertainty. Under causal sufficiency (exogenous independence), the CMC theorem proves the Markov factorization. P3 (local revisability) follows as a validated consequence. The Markov property is both operationally required (P3) and structurally guaranteed (CMC). When causal sufficiency fails, the Markov factorization is still the agent's *intended* factorization — the one its DAG represents — but it is wrong about the world. The gap between intended and actual factorization manifests as correlated failure and $\hat P_\Sigma$ overestimation, and the fix is structural: add the missing common-cause nodes to restore causal sufficiency.

#### Step 4: P1 + finite horizon implies acyclicity (proved)

This is the strongest piece of the argument. See the dedicated section below.

#### Step 5: Assembly

P1 (directed edges + causal interpretation) + P2 (probabilistic) + causal sufficiency (CMC → Markov factorization) + P4 (internal nodes) + finite horizon (acyclicity):

**The strategy representation must be representable as a directed acyclic graph with probability distributions at each node conditioned on its parents — a Bayesian network.** P3 (local revisability) is validated as a consequence of this structure, not required as a premise.

### Acyclicity Derivation

*[Derived (from #post-causal-structure + finite planning horizon)]*

This resolves a former known fragility in the theory. Acyclicity of $\Sigma_t$ is derived, not assumed.

**Result.** For a strategy representation over a finite future horizon, temporal ordering forces acyclicity.

**Derivation.**

1. Each node $X_i$ in $\Sigma_t$ represents a future event or state with temporal position $\tau_i \gt t$ (the future time at which the step occurs or the state is evaluated).
2. Each edge $X_i \to X_j$ requires $\tau_i \lt \tau_j$ (P1: causes temporally precede effects).
3. A cycle $X_i \to X_j \to \cdots \to X_i$ would require $\tau_i \lt \tau_j \lt \cdots \lt \tau_i$, which is impossible for a real-valued time index.
4. Therefore the graph is acyclic. $\square$

Formally: a finite set with a strict partial order (future events ordered by time) is representable as a DAG. This is a standard result in order theory — every finite partial order has a Hasse diagram, which is a DAG.

**The iteration objection resolved.** A strategy that says "try $A$, if fail try $B$, if fail try $A$ again" appears cyclic.

In the time-indexed representation:

$$A_1 \to \text{check}_1 \to B_1 \to \text{check}_2 \to A_2 \to \ldots$$

Each attempt is a distinct node at a distinct time. The apparent cycle is a linear chain in the unrolled view. Iteration "terminates" when either a node succeeds (remaining retry nodes become probability-zero), the agent exhausts its resource budget (a constraint truncating the chain), or the horizon ends. Any finite-horizon strategy, including those with "loops" in the informal sense, is acyclic when time-indexed.

**Scope.** This applies to $\Sigma_t$ (the agent's strategy over the future), not to $M_t$'s model of the environment. $M_t$ may include cyclic causal processes — feedback loops in the physical world, market dynamics, ecosystem interactions. The acyclicity is specific to the purposeful substate because $\Sigma_t$ represents planned future actions and the future is partially ordered by time. $M_t$'s model of environmental dynamics may need to represent cycles (via time-unrolled DBNs or other cyclic structures).

**Connection to Pearl.** Pearl's do-calculus is defined on DAGs. Extensions to cyclic structures exist (cyclic SCMs, equilibrium models) but are substantially more complex and lose some of do-calculus's clean properties. The temporal argument here shows that for strategy representations (future-looking plans), acyclicity is not a convenience restriction on Pearl's framework — it is a consequence of the temporal structure of planning.

### What Is Derived vs. What Is Chosen

| Property | Motivating postulate | Strength |
|---|---|---|
| Directed edges | Temporal ordering (P1, #post-causal-structure) | Proved |
| Probabilistic uncertainty | Cox's theorem (P2) | Proved |
| Acyclicity | Temporal ordering + finite horizon (P1) | Proved |
| Internal structure | Fragility + monitoring (P4, #der-chain-confidence-decay) | Derived |
| Markov factorization | Causal Markov Condition theorem (P1 causal interpretation + P2 probability + causal sufficiency) | Proved under causal sufficiency (CMC theorem) |
| **DAG with Markov property** | **P1 + P2 + causal sufficiency (CMC) + P4** | **Conditional on causal sufficiency — which is testable and repairable** |
| AND/OR parameterization | Boolean completeness + parsimony | Hypothesis (binary outcomes only) |
| Single-parameter edges | Parsimony / IB | Formulation choice |
| Specific node ontology | — | Formulation choice |

The dividing line: acyclicity and directed edges are proved; the full DAG-with-Markov-property is conditional on causal sufficiency. The parameterization (AND/OR, CPT form, edge semantics) is a formulation choice within the strongly motivated structure, motivated by parsimony and domain fit but not by mathematical necessity.

### Equivalence Class

**Within the DAG class.** Multiple DAGs can encode the same conditional independence relations, forming a Markov equivalence class identified by a CPDAG (completed partially directed acyclic graph). Two DAGs in the same equivalence class make identical probabilistic predictions but may differ in causal interpretation.

**Across representation types.** Factor graphs, junction trees, influence diagrams, and chain graphs are NOT simple presentational variants of DAGs:

- **Factor graphs** and **junction trees** preserve factorization and inference structure without necessarily preserving directed causal semantics.
- **Influence diagrams** add decision and utility nodes — a richer object, not an equivalent one.
- **Chain graphs** can express independence models that are not representable as DAGs at all.
- **Markov equivalence** is a statement within DAG classes, not across all graphical model types.

The correct claim is narrow: for a given factorized distribution, DAG and factor-graph representations can compute the same marginals. But causal semantics (do-calculus) are DAG-specific and do not transfer to undirected or mixed representations without additional structure.

**AAT's choice.** AAT uses DAG + AND/OR because: (a) AND/OR is the most parsimonious complete basis for binary combination ( #scope-and-or), (b) the DAG naturally supports causal/interventional reasoning (Pearl's do-calculus), and (c) the representation converged across three independent formalism attempts.

## Epistemic Status

The acyclicity derivation is *exact* — it follows from temporal ordering over a finite horizon via standard order theory. The individual postulates P1, P2, and P4 are each well-grounded (temporal structure, Cox's theorem, and chain fragility respectively).

The Markov property is now *proved under causal sufficiency* via the Causal Markov Condition theorem (Spirtes, Glymour & Scheines 2000, Theorem 3.4; Pearl 2009, Theorem 1.4.1). The previous sketch argument (P3 requires locality → P1 identifies parents → therefore Markov) has been replaced by a rigorous chain: P1-P2 establish the causal DAG structure, causal sufficiency guarantees exogenous independence, and the CMC theorem proves the factorization. P3 (local revisability) is now a *consequence* of the Markov property, not a premise — the CMC shows that local revision is automatically correct for causally sufficient DAGs, validating P3's operational requirement.

The conditioning on causal sufficiency is the right level of conditionality: it is a property of *strategy quality* (did the agent include all relevant common causes as nodes?), not of agent architecture. It is testable in principle (correlated residuals after convergence indicate missing common causes) and repairable in practice (add the common-cause node). When causal sufficiency fails, the Markov factorization fails, and this manifests as correlated failure and $\hat P_\Sigma$ overestimation ( #def-strategy-dag). The edge-independence assumption in AND/OR propagation and the causal sufficiency condition for the Markov property are the same condition viewed from different angles.

Max attainable: *exact* for acyclicity (already there). *Derived conditional* for the full DAG-with-Markov-property — the derivation is rigorous (invokes a proved theorem), and the remaining condition (causal sufficiency) is about model quality, not proof quality.

The AND/OR restriction is a *hypothesis* for binary outcomes, grounded in Boolean completeness and parsimony. For non-binary outcomes, it does not apply and richer parameterizations within the derived graphical structure are needed.

The parallel to Cox's theorem is now tighter than previously stated: Cox's theorem proves that consistency axioms force probability; the CMC theorem proves that causal structure under sufficiency forces the Markov factorization. Both are formal results, not analogies. The remaining gap: Cox's axioms are necessary and sufficient for probability; AAT's postulates are sufficient for DAG+Markov structure, but the necessity direction (could a non-DAG structure satisfy P1-P4?) is not established. For practical purposes this gap is unimportant — the proved sufficiency gives a rigorous foundation for the strategy representation.

## Discussion

**The contribution of this analysis.** The dividing line between derived/conditional structure and chosen parameterization is the key result. The agent community (and future researchers) know exactly what is proved (acyclicity, directed edges), what is conditional (Markov property, contingent on causal sufficiency), and what is a formulation choice (the parameterization within the graph). Alternative parameterizations can be explored without abandoning the theoretical foundation.

**Acyclicity deserves emphasis.** The existing theory previously flagged "DAG acyclicity is an assumption, not forced" as a known fragility. The derivation above resolves this: acyclicity of $\Sigma_t$ follows from temporal ordering over a finite planning horizon. This is specific to the strategy — $M_t$'s environment model is not restricted to acyclic structures.

**The causal sufficiency assumption.** The Markov condition assumes causal sufficiency — no hidden common causes within the strategy. Since the agent constructs $\Sigma_t$, there are no "hidden" variables internal to the strategy (the agent chose all the nodes). But environmental common causes that affect multiple strategy steps may violate the Markov condition within $\Sigma_t$. If so, latent variable models or causal graphs with hidden nodes would be needed. This connects to the edge identifiability problem noted in #def-strategy-dag.

## Working Notes

- **P3→Markov: resolved.** The previous gap (P3 could be satisfied by non-Markov sparse factorizations) is resolved by grounding the Markov property in the CMC theorem rather than in P3. The CMC proves the factorization from the causal structure (P1) and causal sufficiency (exogenous independence), making P3 a consequence rather than a premise. The alternative-factorization concern (factor graphs, junction trees) is now moot: the Markov property follows from the causal semantics, not from locality. P3 remains valuable as an *operational requirement* that the CMC-guaranteed factorization satisfies.
- **Parsimony theorem for AND/OR.** Is there a formal result that AND/OR (noisy-AND + noisy-OR) is the unique $O(k)$-parameter complete basis for binary nodes? This would strengthen #scope-and-or from formulation choice to derived. The Boolean completeness half is standard; the uniqueness-under-parsimony half is not established.
- **Non-binary outcome analogs.** For continuous or multi-valued outcomes, the natural analogs of AND/OR might be min/max or additive/multiplicative combination. Is there a completeness result for these? The current argument applies cleanly only to binary outcomes.
- **Environmental common causes and the CMC.** The CMC proof makes the failure mode precise: when unmodeled environmental dependencies (weather, shared infrastructure, market conditions) affect multiple strategy steps, the exogenous noise terms $\varepsilon_i$ become correlated, causal sufficiency fails, and the Markov factorization is violated. The consequence is exactly the correlated-failure phenomenon in #def-strategy-dag: $\hat P_\Sigma$ overestimates success because it treats joint failure probability as the product of marginals. The fix is structural: add the common-cause as a condition node in $\Sigma_t$, restoring causal sufficiency and the Markov property for the augmented DAG. This connects the graph-theoretic result (Markov property) to the strategy-layer result (independence model validity) through a single condition: causal sufficiency.
- **Promotion potential.** With the CMC-based proof, #def-strategy-dag's DAG structure claim is now strongly grounded: acyclicity is proved, the Markov property is proved under causal sufficiency. The remaining "definition" character of strategy-dag is about the *parameterization* (AND/OR, single-parameter edges), which is a formulation choice within the proved graphical structure.


---

