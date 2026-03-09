# Strategic Intent as a Weighted Causal Graph

**Status**: Alternative formalization. Clean-slate treatment of the same problem as 00, preserving the principled core but making different design choices.
**Date**: March 2026
**Depends on**: TF-05, TF-06, TF-11

---

## 0. What We Are Formalizing

An adaptive agent maintains a model $M_t$ of reality (TFT's concern). But a
*purposeful* agent also maintains a **theory of its own future effectiveness**
-- a structured belief about which sequences of actions will cause reality to
move toward states the agent values. Call this structure the agent's
**strategic intent**, $G_t$.

The critical observation: $G_t$ is not a point in state space or a utility
function. It is a **causal graph** -- the agent's hypothesis about which
interventions produce which effects, chained toward valued outcomes. A PID
setpoint is the degenerate case. This document develops $G_t$ as a formal
object, differing from the previous treatment (00) in several ways:

- **No fixed node taxonomy.** Continuous properties replace discrete types.
- **Single-parameter edges.** One weight $p \in [0,1]$ instead of $(p, \theta)$.
- **AND/OR structure** replaces universal noisy-OR.
- **Fewer metrics, sharper predictions.** Quantities connect directly to TFT.

The principled core (Section 0.1) is preserved exactly.

### 0.1 The Principled Core (Constraints)

These are not design choices. They are consequences of TFT that any
formalization must satisfy.

**P1. Edges as probabilistic causal beliefs.** Each link in the strategy is a
hypothesis: "if I do X, it will cause Y." The weight is a subjective
probability, explicitly interventional (Pearl's Level 2):
$p_{ij} = P(j \text{ achieved} \mid do(i), M_t)$.

**P2. Edge updates use TFT's uncertainty ratio.** When evidence arrives about
an edge, the update gain mirrors TF-06:
$$\eta_{\text{edge}} = \frac{U_{\text{edge}}}{U_{\text{edge}} + U_{\text{obs}}}$$
High uncertainty about the link + reliable observation = large update.

**P3. The Orient cascade.** Observation $\to$ $M_t$ update $\to$ strategy
revision $\to$ feasibility check $\to$ possible goal revision. This is not
optional architecture; it is what Boyd's Orient *means*, formalized.

**P4. Compound probability decay.** A chain of $n$ probabilistic links has
end-to-end confidence $\leq \prod_i p_i$. Depth is fragility.

**P5. Structural change IS extreme parametric update.** Adding a link =
raising its weight from $\approx 0$. Removing = dropping to $\approx 0$.
The parametric/structural boundary dissolves.

**P6. Directed separation.** $M_t$ can be designed independently of $G_t$,
but $G_t$ depends on $M_t$. You need to understand reality before you can
judge whether your strategy is feasible.

**P7. Observability as strategy enablement.** An unobservable causal link is
epistemically dead -- the agent can never update its confidence. Observable
paths are worth more than nominally better but unobservable ones.

---

## 1. The Graph

### 1.1 Nodes as Propositions

Every node $v \in V$ represents a **proposition about the future state of the
world** that the agent cares about for strategic reasons. A node is not
inherently an "objective" or an "action" or an "observable" -- it is a
statement like "the auth endpoint returns valid tokens" or "the enemy's
supply line is cut" or "the user clicks the signup button."

Each node carries continuous properties:

$$v = (\phi_v,\; \sigma_v,\; \omega_v,\; \lambda_v)$$

where:

- $\phi_v \in [0,1]$: **Agency** -- the degree to which the agent can
  directly cause this proposition to become true through its own action.
  $\phi_v = 1$: fully under the agent's control (e.g., "write the code").
  $\phi_v = 0$: not controllable at all (e.g., "the market shifts in our
  favor"). Most nodes live in between.

- $\sigma_v \in [0,1]$: **Observability** -- how well the agent can determine
  whether this proposition is true. $\sigma_v = 1$: perfectly observable
  (e.g., "the test passes"). $\sigma_v = 0$: completely unobservable.
  Formally, $\sigma_v$ is related to the inverse of the observation noise
  on the best available channel for this proposition:
  $\sigma_v \approx 1 / (1 + U_o^{(v)})$ where $U_o^{(v)}$ is the
  observation uncertainty on the channel that would confirm $v$.

- $\omega_v \in \mathbb{R}_{\geq 0}$: **Value** -- how much the agent cares
  about this proposition being true, independent of its role in the strategy.
  Sink nodes (terminal objectives) have high $\omega$. Intermediate nodes
  have $\omega \geq 0$ (they may have intrinsic value or only instrumental
  value).

- $\lambda_v \in \mathbb{R}_{\geq 0} \cup \{\infty\}$: **Horizon** -- the
  time remaining before this node becomes irrelevant. A deadline. $\infty$
  means no temporal constraint.

**Why not discrete types?** The previous treatment's four types create
boundary cases. With continuous properties, an "action" is a node with
high $\phi$, an "observable" has high $\sigma$, an "objective" has high
$\omega$. The taxonomy is recovered as regions in property space, not
categorical labels.

**Status tracking.** Each node also has a time-varying status estimate:

$$s_v(t) \in [0,1]$$

representing the agent's current belief that proposition $v$ is true (or
will become true within horizon $\lambda_v$). For nodes with high $\sigma$,
$s_v$ is updated directly from observations. For nodes with low $\sigma$,
$s_v$ is inferred from the status of connected nodes and the edge weights.

### 1.2 Edges as Causal Beliefs

A directed edge $e = (i, j) \in E$ represents the agent's belief that
**achieving proposition $i$ causally contributes to achieving proposition
$j$**. Each edge carries a single weight:

$$p_{ij} \in [0, 1]$$

This is the agent's subjective probability that $i$'s achievement will
contribute to $j$'s achievement, conditional on the current reality model:

$$p_{ij} = P(j \text{ advances toward true} \mid do(i), M_t)$$

This is explicitly interventional. The agent believes that *doing* (or
*achieving*) $i$ causes progress on $j$, not merely that $i$ and $j$ are
correlated.

**Why a single parameter?** The previous treatment's $(p, \theta)$ pair
collapses into $p \cdot \theta$ for most computations, and the update
dynamics for $\theta$ alone are unclear. Instead, contribution magnitude
is handled through **graph structure**: a node needing multiple partial
contributions has multiple parents, and the combination rule (Section
1.3) determines interaction. Edges stay simple; complexity lives in
the topology.

### 1.3 Combination Rules: AND/OR Structure

When a node $j$ has multiple parents, how do their contributions combine?
The previous treatment used noisy-OR universally. This handles disjunctive
causes ("any one of these could work") but fails for conjunctive causes
("both A AND B are needed").

Instead, each node $j$ with parents $\text{pa}(j)$ has a **combination
type**:

$$\text{comb}(j) \in \{\text{AND},\; \text{OR},\; \text{WEIGHTED}\}$$

**AND combination.** All parents must succeed for $j$ to succeed. The
effective confidence in $j$ given its parents is:

$$P(j \mid \text{pa}(j)) = \prod_{i \in \text{pa}(j)} p_{ij}$$

This is appropriate when $j$ represents something like "the full feature
works," which requires both the backend endpoint ($i_1$) AND the frontend
UI ($i_2$). Failure of any parent kills the node.

**OR combination.** Any parent succeeding is sufficient for $j$. The
effective confidence is:

$$P(j \mid \text{pa}(j)) = 1 - \prod_{i \in \text{pa}(j)} (1 - p_{ij})$$

This is appropriate when $j$ represents something like "we have a working
auth solution," achievable through library X ($i_1$) OR raw implementation
($i_2$). This is the noisy-OR from the previous treatment, now applied
selectively.

**WEIGHTED combination.** Parents contribute proportionally, and $j$'s
confidence is a weighted sum:

$$P(j \mid \text{pa}(j)) = \min\!\left(1,\; \sum_{i \in \text{pa}(j)} \alpha_{ij} \cdot p_{ij}\right)$$

where $\alpha_{ij} \geq 0$ are combination weights satisfying $\sum_i
\alpha_{ij} = 1$. This handles the partial-contribution case: each parent
contributes a fraction of what $j$ needs. This is where the previous
treatment's $\theta$ parameter lives -- but now as a property of the
combination rule at the receiving node, not as a property of each edge
independently.

**Why this matters.** Making combination rules explicit distinguishes
"I need plan B because A might fail" (OR: hedging) from "I need both
backend AND frontend" (AND: sequencing) -- radically different strategic
situations that the previous noisy-OR conflated.

### 1.4 The Full Object

**Definition (Strategic Intent Graph).** The agent's strategic intent at
time $t$ is:

$$G_t = (V_t,\; E_t,\; p_t,\; \text{props}_t,\; \text{comb}_t)$$

where:
- $V_t$ is the set of propositional nodes
- $E_t \subseteq V_t \times V_t$ is the set of directed causal edges
- $p_t : E_t \to [0,1]$ assigns causal confidence to each edge
- $\text{props}_t : V_t \to (\phi, \sigma, \omega, \lambda, s)$ assigns
  properties and status to each node
- $\text{comb}_t : V_t \to \{\text{AND}, \text{OR}, \text{WEIGHTED}\}$
  assigns combination rules (with weights $\alpha_{ij}$ for WEIGHTED nodes)

**Structural requirement: acyclicity.** $G_t$ must be a DAG. Causal chains
are temporally ordered; an event cannot be both cause and effect of the same
outcome. This is a consequence of Pearl's causal framework, not a modeling
choice.

**Structural requirement: rootedness.** Every node must have a directed path
to at least one **terminal node** (a node with $\omega_v > 0$ and no
outgoing edges). Nodes disconnected from all valued outcomes are strategic
dead weight.

### 1.5 Degenerate Cases

**PID controller.** Single node ($\omega > 0, \sigma = 1$), no edges.
Trivial graph; TFT's point-in-$S$ model suffices. **LQR/LQG.** Two nodes,
one edge with $p = 1$. **Single-step lookup.** Two nodes, one edge with
$p < 1$ -- the simplest non-trivial case. The formalism earns its keep
when $|V| > 3$ and the graph has branching, AND-nodes, or unobservable
intermediaries.

---

## 2. Dynamics: How $G_t$ Evolves

$G_t$ is not static. It changes as the agent acts, observes, and learns.
The dynamics of $G_t$ are where the principled core (P1--P7) does its
heaviest lifting.

### 2.1 Edge Confidence Update (P2 in Action)

**Trigger.** An observation $o_t$ arrives that is informative about whether
a causal link $(i,j)$ holds.

**Mechanism.** The causal confidence $p_{ij}$ updates via an approximation
to Bayesian updating that mirrors TFT's gain structure:

$$p_{ij}^{\text{new}} = p_{ij}^{\text{old}} + \eta_{\text{edge}} \cdot
\bigl(\text{signal}(o_t, i, j) - p_{ij}^{\text{old}}\bigr)$$

where:

- $\text{signal}(o_t, i, j) \in [0, 1]$ is the evidential content of
  the observation with respect to the causal hypothesis $(i,j)$. In the
  simplest case this is binary: did the expected consequence of $i$
  materialize at $j$, or not? More generally it can be a graded signal
  reflecting partial confirmation.

- $\eta_{\text{edge}} = U_{\text{edge}} / (U_{\text{edge}} +
  U_{\text{obs}})$ is the update gain, with:
  - $U_{\text{edge}}$: the agent's uncertainty about this specific causal
    link. Formally, if the agent models $p_{ij}$ as
    $\text{Beta}(\alpha_{ij}, \beta_{ij})$, then
    $U_{\text{edge}} = \text{Var}[\text{Beta}(\alpha, \beta)] =
    \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$.
  - $U_{\text{obs}}$: the observation noise on the channel confirming
    this link. This is the node-level $\sigma_v$ property of the
    downstream node $j$, inverted: $U_{\text{obs}} \propto 1/\sigma_j$.

**Interpretation.** This is TFT's epistrophe applied to a strategic
hypothesis. Novel edges (low $\alpha + \beta$, high $U_{\text{edge}}$)
update fast; well-established edges (high $\alpha + \beta$) resist
individual observations. Same convergence dynamic as TF-06: edges
"harden" as evidence accumulates.

**Connection to P7.** When $\sigma_j \approx 0$: $U_{\text{obs}} \to
\infty$, $\eta_{\text{edge}} \to 0$. The edge is epistemically frozen
at its prior. The strategy cannot adapt downstream of unobservable nodes.

### 2.2 Node Status Propagation

When edge weights or leaf-node statuses change, the effects propagate
through the graph. For a node $j$ with parents $\text{pa}(j)$:

**AND-node:**
$$s_j = \prod_{i \in \text{pa}(j)} p_{ij} \cdot s_i$$

**OR-node:**
$$s_j = 1 - \prod_{i \in \text{pa}(j)} (1 - p_{ij} \cdot s_i)$$

**WEIGHTED-node:**
$$s_j = \min\!\left(1,\; \sum_{i \in \text{pa}(j)} \alpha_{ij} \cdot p_{ij} \cdot s_i\right)$$

Status propagation is a forward pass in topological order: $O(|V| + |E|)$.
The graph IS the agent's theory of how current progress translates into
eventual success.

### 2.3 The Orient Cascade (P3 Formalized)

The full update cycle when an observation arrives:

**Stage 1: Reality update (TFT proper).**
$$M_t = M_{t-1} + \eta^* \cdot g(\delta_t)$$
This is TFT's standard epistrophe. The agent's model of reality updates.

**Stage 2: Edge revision.**
For each edge $(i,j) \in G_t$, check whether the updated $M_t$ changes
the evidential status of the causal hypothesis:
- If $o_t$ is informative about $(i,j)$: apply the edge update rule
  (Section 2.1).
- If $M_t$'s update implies that the causal mechanism behind $(i,j)$ no
  longer holds (e.g., the agent learns that the API it was relying on
  has been deprecated): drop $p_{ij}$ sharply, possibly to $\approx 0$.
- If $M_t$'s update reveals a new causal possibility (e.g., the agent
  discovers an existing utility that provides a shortcut): graft a new
  edge with a prior weight $p_{\text{prior}}$.

**Stage 3: Status propagation.**
Run the forward propagation (Section 2.2) to update all node statuses
given the revised edge weights.

**Stage 4: Feasibility check.**
For each terminal node (objective) $v$ with $\omega_v > 0$: is $s_v$
still above a viability threshold? Formally:

$$\text{viable}(v) \iff s_v > s_{\min}(v)$$

where $s_{\min}(v)$ is the minimum acceptable probability of achieving
$v$, given its value $\omega_v$ and the cost of the strategy subtree
beneath it.

**Stage 5: Goal revision (rare).**
If $s_v < s_{\min}$, the agent may: (a) graft new edges, (b) lower
$s_{\min}$, (c) modify the objective, or (d) abandon it ($\omega_v = 0$).
Options (c)-(d) are **goal revision** -- TF-10's structural adaptation
at the intent level.

**Timescale separation.** $\nu_{\text{edge update}} \gg
\nu_{\text{prune/graft}} \gg \nu_{\text{goal revision}}$.
Violating this ordering produces strategic thrashing -- the temporal
nesting constraint (TF-11) predicts this failure mode.

### 2.4 Structural Operations as Weight Extremes (P5)

**Pruning** = $p_{ij}$ drops to $\approx 0$; below threshold $p_{\min}$,
the edge is not used for planning (Beta distribution preserved).
**Grafting** = new edge introduced at prior weight $p_{\text{prior}}$,
sourced from updated $M_t$. **Cascade pruning**: disconnected subgraphs
become dead weight. No separate "structural adaptation" module is needed
-- weight updates, pruning, and grafting are movements along a single
continuum of edge confidence.

---

## 3. What the Graph Predicts

The formalism earns its keep by making predictions that go beyond "have a
plan and update it." This section derives consequences from the graph's
structure.

### 3.1 Path Confidence and Compound Decay (P4)

For a directed path $P = (v_1, v_2, \ldots, v_n)$ through the graph, the
**path confidence** is the probability that the entire causal chain holds:

$$\text{conf}(P) = \prod_{k=1}^{n-1} p_{v_k, v_{k+1}}$$

This assumes independent links; correlated failures make the actual
confidence lower. Even with $p = 0.9$ per edge:

| Path length | Confidence |
|:-----------:|:----------:|
| 1           | 0.90       |
| 2           | 0.81       |
| 3           | 0.73       |
| 5           | 0.59       |
| 10          | 0.35       |
| 20          | 0.12       |

Each step costs a factor of $p$. A 10-step chain at $p=0.9$ is half as
reliable as a 3-step chain. The prescription: break chains at observable
nodes so failures are detected early. The cost of depth is confidence;
the remedy is observability.

### 3.2 Effective Reach

Define the **effective reach** of a source node $v_s$ (typically a node
with high agency $\phi$) to a terminal node $v_t$ (high value $\omega$):

$$R(v_s, v_t) = \max_{P \in \text{paths}(v_s, v_t)} \text{conf}(P)$$

This is the maximum-confidence path from action to objective. The maximum
is taken over all paths because the agent can choose which route to
pursue.

The **aggregate reach** $R_{\text{agg}}(v_t)$ combines source-level reaches
via OR ($1 - \prod(1 - R_i)$) or AND ($\prod R_i$) according to the
combination rules. When $R_{\text{agg}}$ is low despite high individual
edge weights, the graph diagnoses the problem: too many serial AND-
dependencies. Redundancy (more OR-alternatives) or shortening would help.

### 3.3 Observability Index

For a given path $P$, define the **observability index**:

$$\text{obs}(P) = \min_{v \in P} \sigma_v$$

This is the worst-case observability along the path -- the darkest point
in the causal chain. The significance: a path with $\text{obs}(P) \approx
0$ contains at least one node where the agent cannot tell whether
progress is being made. Every edge touching that node has
$\eta_{\text{edge}} \approx 0$ and cannot be updated.

**The observability-adjusted confidence** accounts for the epistemic
quality of a path, not just its nominal strength:

$$\text{conf}_{\text{obs}}(P) = \text{conf}(P) \cdot f(\text{obs}(P))$$

where $f : [0,1] \to [0,1]$ is an increasing function with $f(0) = 0$
and $f(1) = 1$. A simple choice is $f(\sigma) = \sigma$, giving:

$$\text{conf}_{\text{obs}}(P) = \text{conf}(P) \cdot \min_{v \in P} \sigma_v$$

This captures a prediction that follows from P7: **an unobservable path
has zero strategic value** regardless of its nominal confidence, because
the agent can never learn whether it is working. A path with $p_{ij} =
0.95$ everywhere but one node with $\sigma = 0$ is worse than a path with
$p_{ij} = 0.7$ everywhere and $\sigma = 0.8$ everywhere, because the
latter can be corrected and the former cannot.

When choosing between strategies, **prefer the one you can see**, even
if it looks nominally weaker.

### 3.4 The Strategic Tempo

TFT defines adaptive tempo as $\mathcal{T} = \sum_k \nu^{(k)} \cdot
\eta^{(k)*}$ -- the rate at which the agent reduces model-reality
mismatch (TF-11). We need an analogous quantity for the intent graph:
how fast is the agent reducing the gap between its current state and
its objectives?

Define the **strategic tempo** for terminal node $v_t$:

$$\mathcal{T}_G(v_t) = \sum_{v \in V} \nu_v \cdot \eta_v \cdot
\frac{\partial s_{v_t}}{\partial s_v}$$

where:
- $\nu_v$ is the rate at which the agent receives observations about
  node $v$ (how often it gets evidence about whether $v$ is true)
- $\eta_v$ is the effective update gain at node $v$ (how much each
  observation shifts the status estimate)
- $\partial s_{v_t} / \partial s_v$ is the sensitivity of the
  objective's status to changes in node $v$'s status, computed from
  the combination rules (Section 2.2)

This is a weighted sum of update rates, where each node's contribution
is scaled by its influence on the objective. A node that is frequently
observed, strongly updated, and highly influential on the objective
contributes heavily to strategic tempo. A node that is rarely observed,
weakly updated, or loosely connected contributes little.

**Bottleneck identification.** The node with the lowest
$\nu_v \cdot \eta_v \cdot (\partial s_{v_t} / \partial s_v)$ on the
critical path is the **strategic bottleneck**. Prescription: invest in
observability or action frequency at the bottleneck.

**Connection to TFT.** $\mathcal{T}$ (TF-11) is epistemic tempo;
$\mathcal{T}_G$ is strategic tempo. They are coupled: high
$\mathcal{T}_G$ requires adequate $\mathcal{T}$ (understanding reality
to make progress), but high $\mathcal{T}$ alone does not guarantee
high $\mathcal{T}_G$.

### 3.5 Strategic Persistence

By analogy with TFT's mismatch dynamics (TF-11), the evolution of
strategic "mismatch" (distance from objectives) can be approximated:

$$\frac{d\Delta_G}{dt} = -\mathcal{T}_G \cdot \Delta_G + \rho_G(t)$$

where:
- $\Delta_G = \sum_{v_t} \omega_{v_t} \cdot (1 - s_{v_t})$ is the
  value-weighted distance from all objectives
- $\mathcal{T}_G$ is the aggregate strategic tempo
- $\rho_G(t)$ is the rate at which progress is undone -- by environment
  changes, adversary actions, or decay of achieved intermediate states

In steady state:
$$\Delta_{G,ss} = \frac{\rho_G}{\mathcal{T}_G}$$

The **strategic persistence condition** is:
$$\mathcal{T}_G > \frac{\rho_G}{\Delta_{G,\text{critical}}}$$

If the environment undermines the agent's strategic progress faster than
the agent can advance, the strategy degenerates. This is the intent-level
analog of TF-11's persistence threshold.

**What $\rho_G$ includes.** Environmental drift eroding achieved states,
adversarial action targeting the agent's progress, and decay of
unmaintained intermediate achievements. In adversarial settings, $\rho_G$
is partially opponent-controlled, creating TF-11's coupled dynamics.

---

## 4. The $M_t$-$G_t$ Interface (P6 Formalized)

### 4.1 Two Distinct Structures

$M_t$ (reality model): descriptive, self-contained, updated from
observations via TFT. $G_t$ (intent graph): prescriptive, depends on
$M_t$, updated via the Orient cascade. The relationship is asymmetric
(P6): $M_t$'s update rule does not depend on $G_t$, but every edge
$p_{ij}$ in $G_t$ is a claim about reality's causal structure that may
become untenable or newly viable when $M_t$ changes.

**Coupling strength scales with uncertainty.** When edges are near 0 or
1, $G_t$ is nearly independent of $M_t$. When edges are near 0.5, $G_t$
is tightly coupled -- every $M_t$ update could shift the strategy. An
uncertain strategist needs a better world model than a confident one.

### 4.2 Consistency and What $M_t$ Provides

For each edge $(i,j)$ with $p_{ij} > p_{\min}$, $M_t$ should assign
non-negligible probability to the underlying causal mechanism. An edge
contradicting $M_t$ is a **strategic delusion**. Inconsistencies arise
from update lag (normal), compartmentalization (pathological), or
untested grafts (normal exploration).

$G_t$ draws four things from $M_t$: (1) causal structure -- which
interventions produce which effects; (2) transition probabilities --
initial $p_{ij}$ estimates; (3) observability information -- which
channels can confirm which propositions ($\sigma_v$ values); (4)
feasibility constraints -- what is physically possible. This is why
P6 holds: the intent graph is built from materials the reality model
provides.

---

## 5. Predictions and Non-Obvious Consequences

The formalism should produce insights that go beyond common sense. Here
are the strongest candidates.

### 5.1 Observability Dominates Nominal Confidence

**Prediction.** Given two paths to the same objective with equal nominal
confidence $\text{conf}(P_1) = \text{conf}(P_2)$, the agent should
prefer the path with higher observability: $\text{obs}(P_1) >
\text{obs}(P_2)$ implies $P_1$ is strategically superior.

**Why this is non-obvious.** Standard planning evaluates paths by
expected success probability. Two paths with equal probability seem
interchangeable. But the path with higher observability allows the agent
to *update* -- to detect failure early and redirect. The unobservable
path locks the agent into its prior beliefs.

**Quantitative argument.** Two paths, each at initial confidence 0.7.
Path A has $\sigma = 0.9$ (clear feedback); Path B has $\sigma = 0.1$
(near-blind). After one attempt, Path A yields $\eta_{\text{edge}}$
large -- the agent quickly learns whether the path works and either
succeeds or redirects. Path B yields $\eta_{\text{edge}}$ tiny -- the
agent is still guessing after $n$ attempts. The value of observability
compounds: faster learning on each edge cascades into better decisions
at every subsequent step.

### 5.2 AND-Nodes Create Fragility Cliffs

**Prediction.** Strategies with AND-nodes (conjunctive dependencies)
are disproportionately fragile compared to strategies with OR-nodes,
in a way that simple confidence metrics miss.

**Why.** An AND-node with $k$ parents, each at confidence $p$, has
effective confidence $p^k$. An OR-node with $k$ parents has effective
confidence $1 - (1-p)^k$. The asymmetry is dramatic:

| Parents ($k$) | AND conf ($p=0.8$) | OR conf ($p=0.8$) |
|:---:|:---:|:---:|
| 1 | 0.80 | 0.80 |
| 2 | 0.64 | 0.96 |
| 3 | 0.51 | 0.99 |
| 5 | 0.33 | 1.00 |

Adding parents to an AND-node *destroys* confidence. Adding parents to
an OR-node *creates* confidence. The strategic implication: when the
agent encounters an AND-dependency ("I need all of A, B, and C"), it
should invest heavily in raising each parent's confidence, because the
weakest link dominates. When it encounters an OR-dependency ("any of A,
B, or C would work"), it should invest in diversity (more alternatives)
rather than in perfecting any single one.

Natural language disguises AND-dependencies. "Ship the feature" decomposes
into backend AND frontend AND tests AND deployment -- $0.9^4 = 0.66$
even at 90% per component.

### 5.3 The Unobservability Trap is an Absorbing State

**Prediction.** Once a significant fraction of the agent's strategy
operates through unobservable nodes, the strategy becomes self-
reinforcing in its blindness.

**Mechanism.** Unobservable nodes ($\sigma \approx 0$) have frozen beliefs
(Section 2.1). Frozen beliefs generate no mismatch signal, so the agent
has no reason to change this part of the strategy and no evidence that
it needs observability investment.

This is an **absorbing state**: the agent cannot learn and cannot
recognize that it cannot learn. Escape requires: (1) external shock
revealing the blind spot indirectly, (2) proactive observability
investment independent of current evidence, or (3) another agent whose
observations cover the blind spot.

**Practical prescription.** Periodically audit the graph for low-$\sigma$
nodes and invest in observability *before* problems manifest. In software:
instrument before you build. In military: reconnaissance before you
commit. In business: measure before you optimize.

### 5.4 Depth-Observability Tradeoff

**Prediction.** There is an optimal decomposition depth balancing
incremental confirmation against compound decay and modeling cost.

Decomposing a chain into $n$ observable segments lets the agent detect
failure after each segment (faster redirect). But each segment adds
a separate causal hypothesis the agent must formulate and maintain, and
more segments mean more uncertain links to estimate. The optimal $n$
minimizes total expected cost (wasted effort on failed paths + modeling
overhead), subject to the constraint that each segment must be genuinely
observable. In practice: decompose as finely as your observation
channels allow, but no finer.

### 5.5 Strategic Tempo Predicts Success Better Than Confidence

**Prediction.** Two agents with equal initial $R_{\text{agg}}$ but
different $\mathcal{T}_G$ will have systematically different outcomes.
The higher-tempo agent succeeds more often because it corrects errors
faster. This follows from the persistence condition: what matters is
the *rate* of strategy adaptation, not the initial plan quality. An
agent with a mediocre strategy but high $\mathcal{T}_G$ outperforms
a brilliant strategy with low $\mathcal{T}_G$ -- the intent-graph
analog of Boyd's Orient-over-speed insight.

---

## 6. Worked Example: Software Feature Delivery

An agent implementing OAuth authentication. The graph:

**Nodes.** Objective $v_O$: "Users authenticate via OAuth" ($\omega=1$,
AND-node). Intermediates: $v_1$ "Token endpoint works" (OR-node, $\sigma=0.95$),
$v_2$ "Sessions persist" ($\sigma=0.9$), $v_3$ "Existing tests pass"
($\sigma=1.0$). Actions: $a_1$ "Use library X" ($\phi=1$), $a_2$
"Use raw HTTP" (hedge, $\phi=1$), $a_3$ "Add session middleware" ($\phi=1$).

**Edges.** $(a_1, v_1): p=0.8$, $(a_2, v_1): p=0.6$, $(a_3, v_2): p=0.85$,
$(v_1, v_O): p=0.95$, $(v_2, v_O): p=0.90$, $(v_3, v_O): p=0.99$.

**Analysis.** $v_1$'s OR-confidence: $1-(1-0.8)(1-0.6)=0.92$. Since $v_O$
is AND: $s_{v_O} = 0.95 \cdot 0.92 \cdot 0.90 \cdot 0.85 \cdot 0.99 = 0.66$.
Bottleneck: $v_2$ has no hedge (single parent, $0.85 \times 0.90 = 0.77$
path contribution). Prescription: graft a second edge into $v_2$.
All $\sigma \geq 0.85$ -- no observability traps.

**After a failure.** Library X doesn't support the required flow.
$p_{a_1,v_1}$ drops from 0.8 to $\approx 0.32$ (with $\eta_{\text{edge}}
\approx 0.6$ given clear test failure). $v_1$'s OR-confidence falls to
$1-(1-0.32)(1-0.6)=0.73$, and $s_{v_O}$ drops to $\approx 0.52$.

Without the hedge ($a_2$), $v_1$ would drop to 0.32 and $v_O$ to $\approx
0.24$. The hedge bought 28 percentage points of robustness. Meanwhile,
$M_t$ updates ("library X doesn't support this"), potentially triggering
grafts (alternative libraries) and making $a_2$ the primary path.

---

## 7. Honest Assessment

### 7.1 What Works

1. **The continuous-property node model** avoids the taxonomic boundary
   problems of the previous treatment. There's no debate about whether
   a node is an "action" or a "key result" -- it has a position in
   $(\phi, \sigma, \omega, \lambda)$ space, and the formalism treats it
   accordingly.

2. **Explicit AND/OR structure** is a genuine improvement over the
   universal noisy-OR. Many real strategies have conjunctive
   dependencies, and making them visible changes the analysis
   materially (Section 5.2).

3. **Single-parameter edges** are simpler and arguably more honest.
   The previous treatment's $\theta$ (contribution magnitude) was hard
   to estimate independently and collapsed into $p \cdot \theta$ for
   most computations anyway. Pushing contribution structure into the
   graph topology (via WEIGHTED combination rules) is cleaner.

4. **The observability-adjusted confidence** (Section 3.3) and the
   unobservability trap analysis (Section 5.3) are the strongest
   non-obvious consequences. They derive from P7 but produce concrete
   prescriptions that genuinely differ from naive expected-value
   reasoning.

5. **Strategic tempo** (Section 3.4) connects the intent graph to TFT's
   dynamics in a way that produces quantitative predictions (strategic
   persistence, bottleneck identification) rather than just qualitative
   analogies.

### 7.2 What Doesn't Work (or Isn't Settled)

1. **WEIGHTED combination weights $\alpha_{ij}$** are the previous
   treatment's $\theta$ in disguise, relocated from edge to node. The
   estimation problem is not solved, just moved.

2. **Strategic tempo** requires differentiating through combination rules.
   AND-nodes produce numerically unstable gradients when any parent
   has $s \approx 0$. The mixed AND/OR case may produce sensitivity
   landscapes that are hard to reason about.

3. **The strategic persistence ODE** is TF-11's linear hypothesis
   transplanted, with all the same caveats. Treat quantitative
   predictions as heuristics.

4. **Failure correlation** is unmodeled. The product formula for path
   confidence assumes independent edges. Correlated failures (shared
   root causes) make redundancy less valuable than the formalism predicts.

5. **$M_t$-$G_t$ consistency** is a stated requirement, not a computable
   test. "Assign non-negligible probability to a causal mechanism" needs
   operationalization.

6. **Cognitive cost** of maintaining $G_t$ is unmodeled. A capacity
   constraint (parallel to TF-03's $\beta$) should eventually penalize
   graph complexity.

### 7.3 Comparison with Previous Treatment (00)

| Dimension | Previous (00) | This Treatment (02) | Assessment |
|-----------|---------------|---------------------|------------|
| Node types | 4 categorical (O/K/A/X) | Continuous properties | 02 is more flexible, 00 is more intuitive |
| Edge weights | 2-parameter $(p, \theta)$ | 1-parameter $p$ | 02 is simpler but pushes $\theta$ into combination rules |
| Combination | Noisy-OR everywhere | AND/OR/WEIGHTED per node | 02 handles conjunctions; 00 cannot |
| Health metrics | 5 specific + aggregate | 3 derived quantities | 02 is leaner; unclear which has more predictive power |
| Dynamics | Orient cascade + 6 named operations | Orient cascade + edge updates | Structurally similar; 02 is more parsimonious |
| Predictions | 9 numbered predictions | 5 thematic predictions | 00 is more thorough; 02 is more focused |
| Weaknesses | Noisy-OR assumption; $\theta$ estimation | WEIGHTED weights; failure correlation | Different weaknesses; neither is clearly superior |

**What converged.** Both treatments reach the same qualitative conclusions:
Orient cascade structure, compound decay, observability dominance,
structural-parametric continuity, directed separation. The principled
core (P1--P7) constrains design choices enough that different scaffolding
converges.

**What diverged.** AND/OR structure is a genuine difference -- the
previous noisy-OR cannot represent conjunctive dependencies, which
enables the fragility-cliff analysis (Section 5.2). The single-parameter
edge loses the "risky but complete" vs. "safe but partial" distinction
but gains clarity about update dynamics.

### 7.4 Open Questions

1. **Is AND/OR/WEIGHTED sufficient?** Real strategies have $k$-of-$n$
   dependencies, conditional dependencies, and nonlinear interactions.
   A factor-graph generalization would handle these at the cost of
   complexity.

2. **Action selection.** How does the agent use $G_t$ to decide what to
   do next? The natural criterion is value-of-information (strategic
   advancement + observability gain), but formalizing this is deferred.

3. **Counterfactual structure.** Should $G_t$ represent rejected
   alternatives and contingency plans, or only the current strategy?

4. **Multi-agent interaction.** Multiple agents' intent graphs interact
   through the adversarial tempo mechanism (TF-11), but this has not
   been formalized at the $G_t$ level.

5. **Empirical validation.** The strongest testable claim: observability-
   adjusted confidence predicts project outcomes better than nominal
   confidence. Testable on historical data where strategy structure and
   milestone observability are known.

---

## 8. Formal Summary

**Object.** $G_t = (V, E, p, \text{props}, \text{comb})$ -- a weighted
DAG of propositions, causal beliefs, and combination rules.

**Dynamics.** Orient cascade: $M_t$ update $\to$ edge revision $\to$
status propagation $\to$ feasibility check $\to$ goal revision. Stages
respect temporal nesting (TF-11).

**Predictions.** (1) Depth is fragile (P4). (2) AND-nodes create
fragility cliffs. (3) Unobservable nodes are absorbing traps (P7).
(4) Strategic tempo predicts success better than static confidence.
(5) Timescale violations produce strategic thrashing.

**Principled.** P1--P7, the Orient cascade, compound decay,
observability-frozen edges, directed separation.

**Scaffold.** Continuous node properties, AND/OR/WEIGHTED rules,
strategic tempo form, linear persistence ODE.

---

## Appendix: Notation Summary

| Symbol | Meaning |
|--------|---------|
| $G_t$ | Strategic intent graph at time $t$ |
| $V_t, E_t$ | Node set, edge set |
| $p_{ij}$ | Causal confidence: $P(j \text{ advances} \mid do(i), M_t)$ |
| $\phi_v$ | Agency: degree of agent control over $v$ |
| $\sigma_v$ | Observability: quality of feedback about $v$ |
| $\omega_v$ | Value: how much the agent cares about $v$ |
| $\lambda_v$ | Horizon: time remaining before $v$ expires |
| $s_v(t)$ | Status: current belief that $v$ is true |
| $\text{comb}(v)$ | Combination rule: AND, OR, or WEIGHTED |
| $\alpha_{ij}$ | Combination weights (for WEIGHTED nodes) |
| $\eta_{\text{edge}}$ | Edge update gain: $U_{\text{edge}} / (U_{\text{edge}} + U_{\text{obs}})$ |
| $\text{conf}(P)$ | Path confidence: $\prod p_{ij}$ along $P$ |
| $R(v_s, v_t)$ | Effective reach: max-confidence path from $v_s$ to $v_t$ |
| $\text{obs}(P)$ | Observability index: $\min_{v \in P} \sigma_v$ |
| $\text{conf}_{\text{obs}}(P)$ | Observability-adjusted confidence |
| $\mathcal{T}_G(v_t)$ | Strategic tempo for objective $v_t$ |
| $\Delta_G$ | Value-weighted distance from objectives |
| $\rho_G$ | Strategic disturbance rate |
