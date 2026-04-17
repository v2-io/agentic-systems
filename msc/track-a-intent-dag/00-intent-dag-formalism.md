# Intent as Probabilistic Causal DAG: First Formal Treatment

**Status**: Working document. First formal sketch of the core novel object in AAD.
**Date**: March 2026
**Depends on**: TF-00 through TF-11, Appendix E (TFT Core), 03-goal-formalism-sketch.md

> The goal-formalism sketch (03) established that G_t should not be a point in
> state space but a **structured network of expected causal chains from actions
> to sub-goals to objectives**. This document develops that insight into a
> formal mathematical object.

---

## 0. Motivation and Framing

TFT formalizes the reality model M_t as a compression of the interaction
history: M_t = phi(C_t). The mismatch dynamics, gain, tempo, and persistence
machinery all operate on M_t. The goal-formalism sketch (03, Section 9)
argued that the agent's intent G_t should not be modeled as a point in the
same state space as M_t (though this is a valid degenerate case), but as a
**probabilistic causal DAG** encoding the agent's theory of how its actions
will produce goal-achievement.

The key insight: **an agent's intent is not "where I want reality to be" but
"what I believe I must do, in what order, to make reality become what I want,
and how I will know it's working."** The PID setpoint is the degenerate case
where the entire DAG collapses to a single node. Real agency requires richer
structure.

This document develops the DAG as a formal mathematical object, defines
operations on it, derives health metrics, and connects it to M_t and the
rest of TFT's machinery.

**What this formalism should buy us (the non-triviality test):**
If the DAG formalism only produces insights any competent project manager
already has ("have a plan, check progress, adapt when things change"), it has
dithered into impotence. The formalism earns its keep if it:
1. Makes structural predictions about when strategies will fail
2. Quantifies the tradeoff between robustness and efficiency in strategy design
3. Reveals non-obvious failure modes (fragility, unobservability traps)
4. Connects cleanly to TFT's dynamics (tempo, persistence, adversarial advantage)
5. Generates different prescriptions for different DAG topologies

We will track this throughout.

**Principled vs. scaffold — a guide to reading this document.**
Not everything here has equal epistemic standing. Some elements are
*first-principled* — they follow necessarily from AAD's foundations (TFT's
feedback dynamics, Pearl's causal hierarchy, the goal/intent gap analysis).
Others are *scaffold-engineering* — reasonable modeling choices that structure
the formalism but could legitimately be different. The distinction:

*First-principled (emphasize — these are load-bearing):*
- Edges as probabilistic causal beliefs with Bayesian update (§2.1)
- The Orient cascade: M_t update → G_t edge revision → feasibility (§4.3)
- Compound probability decay of deep causal chains (§3.5)
- Dissolution of parametric/structural boundary (§2.7)
- Directed separation: M_t independent, G_t depends on M_t (§4.4)
- Observability as strategy enablement, not just verification (§3.3)

*Scaffold-engineering (useful but acknowledge as formulation choices):*
- The four node types O/K/A/X — a taxonomy, not derived (§1.1)
- The five structural constraints — design choices (§1.3)
- The two-parameter edge weight (p, theta) — theta may not be needed in
  the core; p alone may suffice for the essential structure (§1.2)
- The noisy-OR combination rule — one independence assumption among
  several possible; breaks for conjunctive causes (§1.2)
- Specific health metric definitions — the *concept* that DAG structure
  predicts strategy quality is principled; the *specific metrics* are
  design choices (§3)
- The aggregate health score — a placeholder (§3.6)

---

## 1. Formal Definitions

### 1.1 Node Types

**[SCAFFOLD — taxonomy choice, not derived.]** The four node types below
are a reasonable decomposition for many domains, but other decompositions
are possible. What IS principled is the *distinction* between nodes the
agent can act on (actions), nodes the agent can observe (observables),
and nodes the agent is trying to achieve (objectives/key results). The
specific four-way split is a formulation choice.

[Confident for the distinction; the specific types are a modeling choice]

The intent DAG contains four types of nodes. Each node v in V has a type
tau(v) in {O, K, A, X} and a set of associated properties.

**Definition 1.1 (Objective node).** An objective node v with tau(v) = O
represents a high-level desired state of the world. Properties:

    v_O = (s_target, U_target, priority)

where:
- s_target in S is the target region in state space (what the agent wants
  reality to look like with respect to this objective)
- U_target >= 0 is the agent's uncertainty about the target itself (how
  precisely the agent knows what it wants here -- specification ambiguity)
- priority in R_+ is the relative importance of this objective

Objective nodes have no outgoing edges within the DAG (they are sinks --
everything flows toward them). They may have incoming edges from Key Result
nodes or from other Objective nodes (sub-objective structure).

**Definition 1.2 (Key Result node).** A key result node v with tau(v) = K
represents an observable, confirmable sub-goal. Properties:

    v_K = (criterion, deadline, status)

where:
- criterion is a predicate on observables: criterion(o) in {true, false}
  (the condition under which this key result is "achieved")
- deadline in R_+ union {infinity} is the temporal horizon (after which the
  key result becomes irrelevant or the branch should be pruned)
- status in {pending, confirmed, failed, expired} tracks the current state

Key result nodes are the **critical interface** between the intent DAG and
the observation stream. They are where delta_goal becomes empirically
assessable. A key result without a well-defined criterion is an
unobservable sub-goal -- a known fragility (see Section 3.3).

**Definition 1.3 (Action node).** An action node v with tau(v) = A
represents an intervention the agent can perform. Properties:

    v_A = (action, cost, reversibility)

where:
- action in A is the specific action (or action template/class)
- cost >= 0 is the expected resource expenditure
- reversibility in [0, 1] measures how easily the action's effects can be
  undone (0 = irreversible, 1 = freely reversible)

Action nodes are sources in the DAG (or near-sources -- they may have
incoming edges from other actions representing prerequisite ordering).
They represent the agent's **causal intervention points** -- where the
agent's praxis meets the world.

**Definition 1.4 (Observable node).** An observable node v with tau(v) = X
represents a confirmation signal -- an observation the agent expects to
see if a causal chain is working. Properties:

    v_X = (channel, latency, noise)

where:
- channel identifies the observation channel (which of TFT's observation
  channels k will carry this signal)
- latency >= 0 is the expected delay between cause and observable effect
- noise >= 0 is the expected observation uncertainty U_o on this channel
  for this signal

Observable nodes attach to Key Result nodes (providing the evidentiary
basis for status updates) and to Action nodes (providing feedback on
whether the action was executed successfully). They are the **empirical
grounding** of the intent DAG -- where strategy meets aisthesis.

### 1.2 Edge Definition

[Confident]

**Definition 1.5 (Causal intent edge).** A directed edge e = (i, j) in E
represents the agent's belief that achieving/executing node i contributes
causally to achieving node j. Each edge carries:

    w(i,j) = (p_ij, theta_ij)

where:
- p_ij in [0, 1] is the **causal confidence weight**: the agent's
  subjective probability that node i's achievement/execution will
  contribute to node j's achievement, conditional on the agent's
  current reality model M_t

  Formally: p_ij = P(j achieved | do(i), M_t)

  This is explicitly interventional (Pearl's Level 2), not merely
  associational. The agent believes that *doing* i causes j, not
  merely that i and j co-occur.

- theta_ij in [0, 1] is the **contribution magnitude**: given that the
  causal link holds, what fraction of j's achievement does i account for?

  When theta_ij = 1, i is sufficient for j (given the causal link holds).
  When theta_ij < 1, i is a partial contributor -- other nodes must also
  contribute to j for j to be achieved.

The product p_ij * theta_ij gives the expected marginal contribution of
i to j. The expected total contribution to node j from all its parents is:

    E[contribution to j] = 1 - product_{i in parents(j)} (1 - p_ij * theta_ij)

**[SCAFFOLD — independence assumption, handle with care.]** This assumes
approximate independence of parent contributions — a noisy-OR model. This
is a significant simplification. It handles disjunctive causes well ("any
one of these actions could achieve the sub-goal") but conjunctive causes
badly ("both A AND B are needed"). In practice, many strategies have
conjunctive structure ("the feature works only if BOTH the backend endpoint
AND the frontend UI are implemented"). A more principled treatment would
use factor graphs or explicit AND/OR structure in the DAG. For this first
sketch, the noisy-OR is a starting point; the limitation should be
front-of-mind when applying the formalism to domains with strong action
interdependencies.

**Why not just p_ij?** The two-parameter weight (p, theta) captures two
distinct uncertainties: "will this causal link work at all?" (p) and "if
it works, how much of the job does it do?" (theta). A risky action that,
if successful, completely achieves the sub-goal has (low p, high theta).
A safe action that only partially contributes has (high p, low theta).
These have very different strategic implications -- the first calls for
hedging (parallel paths), the second calls for combination (multiple
partial contributors).

### 1.3 The DAG

[Confident]

**Definition 1.6 (Intent DAG).** The agent's intent at time t is:

    G_t = (V_t, E_t, w_t, tau_t)

where:
- V_t is the node set (objectives, key results, actions, observables)
- E_t subset V_t x V_t is the directed edge set (expected causal links)
- w_t : E_t -> [0,1] x [0,1] assigns weights (p, theta) to each edge
- tau_t : V_t -> {O, K, A, X} assigns types to nodes

**Structural constraints** (what makes it a well-formed intent DAG):
1. **Acyclicity**: G_t is a DAG (no cycles in the causal direction).
   Rationale: causal chains must be well-ordered in time. An action
   cannot be both a cause and an effect of the same outcome.
2. **Sink constraint**: All maximal-depth paths terminate at an Objective
   node (tau = O). Everything flows toward objectives.
3. **Source constraint**: All minimal-depth paths originate at an Action
   node (tau = A) or an Observable node (tau = X). The DAG is grounded
   in things the agent can do or observe.
4. **Observability attachment**: Every Key Result node has at least one
   Observable node as a child (or is itself directly observable through
   its criterion). Unobservable key results are permitted but flagged as
   a fragility (Section 3.3).
5. **Type ordering**: Edges respect a partial type ordering. The
   *typical* flow is A -> K -> O, with X nodes attached to K and A
   nodes. Edges from O to O (sub-objective structure), K to K
   (sub-goal decomposition), and A to A (action prerequisites) are
   permitted. Edges from O to A (objective directly prescribing an
   action) are permitted but unusual -- they represent fully specified,
   non-decomposed intent.

**The DAG evolves over time.** G_t at time t may differ from G_{t-1} in
any component: nodes may be added or removed, edges may be added or
removed, weights may change, even node types may be reclassified (a key
result might be promoted to an objective, or an objective decomposed into
key results). The evolution of G_t is the subject of Section 2.

**Notation**: When the time subscript is clear from context, we write
G = (V, E, w, tau). When discussing a specific edge, we write
e_{ij} = (i, j) with weight w_{ij} = (p_{ij}, theta_{ij}).

### 1.4 The Degenerate Cases

[Confident]

**PID controller**: V = {v_O} with s_target = r_t (setpoint). No key
results, no actions modeled, no observables modeled. The "DAG" is a single
node. All of TFT's PID instantiation lives here. This is why the
point-in-S model of G_t works for PID -- the DAG is trivial.

**LQG controller**: V = {v_A, v_O} with a single edge from the control
action to the reference state. w = (1, 1) -- the agent is certain the
control law works and that it completely addresses the objective. The DAG
is a single edge. Separation principle holds because the DAG is so simple
that its structure doesn't interact with M_t.

**Thermostat**: Even simpler than PID -- no explicit model, no explicit
actions in the DAG. The thermostat's "intent" is a reflex, not a strategy.
Arguably below the threshold of having a DAG at all.

These degenerate cases confirm that the DAG formalism properly subsumes
the point-in-S model as a special case. The formalism adds value precisely
when the DAG has non-trivial structure -- multiple paths, uncertainty,
contingencies.

---

## 2. DAG Operations (Strategy Maintenance)

[Plausible]

The intent DAG is not static. It evolves as the agent acts, observes, and
updates its beliefs. This section formalizes the operations that constitute
**strategy maintenance** -- the ongoing care and feeding of the intent DAG.

The central insight from 03-goal-formalism-sketch, Section 9.4:
**structural change IS extreme parametric update.** In a probabilistic DAG,
adding an edge is equivalent to raising its weight from 0. Removing an
edge is equivalent to dropping its weight to 0. The distinction between
"parametric" and "structural" change, which seems sharp in deterministic
frameworks, dissolves in the probabilistic setting. This does not mean
the distinction is useless -- there are computational and cognitive
differences between small weight adjustments and the introduction of
entirely new causal hypotheses -- but the mathematical treatment can be
unified.

### 2.1 Edge Weight Update (Bayesian Causal Confidence Revision)

**Trigger**: An observation o_t arrives that is informative about whether
a causal link (i, j) holds.

**Mechanism**: The causal confidence p_ij updates via Bayes' rule on the
causal hypothesis:

*[Formulation (edge-weight-update)]*

    p_ij^{new} = P(i -> j | o_t, M_t)
               = P(o_t | i -> j, M_t) * p_ij^{old}
                 / P(o_t | M_t)

where "i -> j" denotes the causal hypothesis that executing/achieving i
contributes to achieving j.

In practice, the agent rarely has the full posterior. A useful
approximation mirrors TFT's uncertainty ratio:

*[Hypothesis (edge-gain-approximation)]*

    p_ij^{new} = p_ij^{old} + eta_edge * (signal - p_ij^{old})

where:
- signal in {0, 1} is the binarized observation (did the expected
  confirmation arrive or not?)
- eta_edge = U_edge / (U_edge + U_obs) mirrors TFT's gain structure

  U_edge is the agent's uncertainty about this particular causal link
  (high for novel/untested links, low for well-established ones)

  U_obs is the observation noise on the confirmation channel

This is a beta-Bernoulli update in disguise. If p_ij is modeled as
Beta(alpha_ij, beta_ij), then observing a success (signal = 1) yields
alpha_ij -> alpha_ij + 1, and observing a failure yields
beta_ij -> beta_ij + 1. The point estimate p_ij = alpha/(alpha + beta)
and the uncertainty U_edge = alpha*beta / ((alpha+beta)^2 * (alpha+beta+1))
both update naturally. The eta_edge approximation is the first-order
Taylor expansion of this.

**Connection to TFT [FIRST-PRINCIPLED — this is load-bearing]**: This is
TFT's epistrophe applied to a single edge of the intent DAG rather than
to M_t as a whole. The mismatch signal is "I expected this causal link to
produce this observable, and it did/didn't." The gain is calibrated by the
same uncertainty ratio principle (TF-06). The key difference: the "model"
being updated is not M_t (the reality model) but a specific causal
hypothesis within G_t (the intent model).

This is what makes AAD more than BDI-with-dynamics. BDI says agents have
beliefs and desires but provides no mechanism for desire revision. AAD says:
desires (G_t edges) are updated by the SAME uncertainty-ratio machinery as
beliefs (M_t), applied to causal hypotheses about goal-achievement rather
than to predictions about reality. The gain structure is universal — it
applies whenever an agent holds a probabilistic belief and receives evidence.
The distinction between "updating beliefs about reality" (TFT) and "updating
beliefs about strategy" (AAD Part II) is a distinction in *what* is being
updated, not in *how*.

**[Prediction 1]**: The rate at which edge weights converge should follow
the same dynamics as TFT's mismatch reduction: exponential convergence
toward the true value at a rate determined by the observation frequency
and gain on the relevant channel. Edges observed through high-frequency,
low-noise channels (e.g., compiler output for a software action) should
converge faster than edges observed through low-frequency, high-noise
channels (e.g., user behavior for a product objective). This is testable.

### 2.2 Pruning

**Trigger**: An edge weight p_ij drops below a threshold p_min, or a
node's status becomes "failed."

**Operation**: Remove the edge (or set p_ij = 0, which is equivalent in
the probabilistic setting). If removing the edge disconnects a subtree
from any objective, the entire subtree is pruned (its nodes and edges
are removed or set to zero weight).

*[Formulation (pruning-condition)]*

    Prune edge (i,j) when: p_ij < p_min

    Cascade: for all v in descendants(i) that have no remaining path
    to any objective node, remove v and all edges incident to v.

**The threshold p_min is a design parameter.** A low p_min means the agent
holds onto unlikely causal hypotheses longer (exploratory, hedging). A
high p_min means the agent abandons hypotheses quickly (decisive,
risk of premature commitment).

**Connection to TFT**: Pruning is the intent-DAG analog of TF-10's
structural adaptation. In TF-10, the model class M is replaced when
F(M) < 1 - epsilon. Here, a causal hypothesis within G_t is abandoned
when its confidence drops below threshold. The difference: TF-10's
structural adaptation is catastrophic (replace the entire model class),
while DAG pruning is local (remove one branch). This is one of the
advantages of the DAG representation -- it supports **graceful
degradation** of strategy rather than all-or-nothing model replacement.

**[Prediction 2]**: Agents (human or artificial) that prune too slowly
(low p_min) will waste resources on dead-end paths. Agents that prune
too aggressively (high p_min) will abandon viable paths prematurely. The
optimal p_min should depend on the cost of continuing a dead-end path
versus the cost of abandoning a viable one -- i.e., on the relative costs
of false persistence and premature abandonment. In domains where actions
are cheap and reversible (software: delete the code and try again), p_min
should be higher (prune faster). In domains where actions are expensive
and irreversible (military: troops committed to an axis of advance),
p_min should be lower (hold onto the hypothesis longer). This maps to
known strategic wisdom but derives it from a formal parameter.

### 2.3 Grafting

**Trigger**: The agent discovers a new causal hypothesis -- a potential
link between an existing (or new) action and an existing (or new)
sub-goal. Sources: exploration of M_t reveals a causal pathway the agent
didn't know about; analogy from a different domain; communication from
another agent; creative recombination.

**Operation**: Add a new edge (and possibly new nodes) to the DAG.

*[Formulation (grafting)]*

    G_t^{new} = G_t^{old} union {new nodes, new edges}

    New edge (i', j') is initialized with:
    - p_{i'j'} = p_prior (the agent's prior confidence in untested
      causal hypotheses, typically low -- 0.1 to 0.3)
    - theta_{i'j'} estimated from M_t (how much would this contribute
      if it worked?)

**Connection to TFT**: Grafting is driven by the reality model M_t. The
agent's understanding of how the world works (M_t) generates hypotheses
about new causal paths to goals. This is the M_t -> G_t interaction
identified in the goal-formalism sketch (Section 9.5) and in the
goal-intent gap analysis (Section 2.5): Orient is where M_t meets G_t,
and grafting is one product of that meeting. Specifically: when M_t
updates (epistrophe), the agent may recognize new causal possibilities
that weren't apparent before. This recognition IS grafting.

**[Prediction 3]**: The rate of grafting should correlate with the rate
of M_t update. When the agent is learning rapidly about reality (high
epistemic tempo T), it should also be discovering new strategic
possibilities at a higher rate. This predicts that **comprehension
enables strategy** -- you can't graft new causal hypotheses if you don't
understand the causal structure of reality. This formally justifies the
"comprehend before you plan" heuristic and extends TST's T-05 ("bias
toward comprehension"): comprehension doesn't just improve execution,
it enables strategy discovery.

### 2.4 Reweighting

**Trigger**: Updated edge weights change the relative expected
contribution of different paths to the same objective.

**Operation**: Resource allocation shifts toward higher-confidence paths.

This is NOT a separate operation on G_t -- the DAG's weights already
encode the relative confidence. Reweighting is an **implication** of
weight updates for action selection. Given the current DAG G_t, the
agent should allocate resources (time, compute, attention, personnel)
to action paths in proportion to their expected contribution to
objectives, adjusted for cost:

*[Formulation (resource-allocation)]*

    For each action node a_i, the allocation priority is:

    priority(a_i) = sum_{o in Objectives} [
        priority(o) * PathContribution(a_i, o) / cost(a_i)
    ]

where PathContribution(a_i, o) is the expected contribution of a_i to
objective o, computed by propagating edge weights along all paths from
a_i to o:

    PathContribution(a_i, o) = sum_{paths P from a_i to o} [
        product_{(j,k) in P} p_jk * theta_jk
    ]

This is a standard DAG path-weight computation and can be done in O(|V| + |E|)
time via topological sort. The propagation gives each action node a
**derived priority** that reflects its position in the full intent
structure.

**Non-obvious implication**: An action with a high-confidence, high-
contribution edge to a low-priority objective may be deprioritized
relative to an action with a moderate-confidence edge to a high-priority
objective. The DAG's structure mediates between action confidence and
objective importance in a way that flat priority lists cannot. This is
a concrete advantage of the DAG over simpler representations.

### 2.5 Parallel Hedging

**Trigger**: Multiple action paths exist toward the same sub-goal or
objective, and the agent is uncertain which will succeed.

**Operation**: Pursue multiple paths simultaneously, allocating resources
according to a portfolio optimization criterion.

*[Formulation (hedging-criterion)]*

    For paths {P_1, ..., P_n} toward sub-goal k:

    Let s_i = PathContribution(P_i, k) -- expected success contribution
    Let c_i = cost(P_i) -- resource cost of pursuing path i
    Let x_i in {0, 1} -- pursue path i or not

    Minimize: sum_i c_i * x_i + lambda_fail * P(k not achieved | {x_i})

    where P(k not achieved | {x_i}) = product_{i : x_i = 1} (1 - s_i)

The penalty lambda_fail represents the cost of failing to achieve sub-goal
k. When lambda_fail is high (the sub-goal is critical), the agent hedges
more aggressively -- pursuing redundant paths whose individual expected
value doesn't justify their cost, but whose portfolio value does.

**When to hedge vs. when to commit**: The optimal number of parallel
paths depends on:
1. The confidence spread: if one path has p >> all others, commit to it
2. The cost ratio: if paths are cheap relative to failure, hedge broadly
3. The correlation: if path failures are correlated (same root cause),
   hedging provides less value
4. The reversibility: if committed resources can be recovered on path
   failure, sequential exploration may dominate parallel hedging

**[Prediction 4]**: Agents should hedge more in early stages (when edge
confidences are all uncertain, estimated from priors) and commit more in
later stages (when observations have differentiated path confidences).
This matches the explore-then-exploit pattern but derives it from the
DAG's weight structure rather than from a separate exploration bonus.
The transition from hedging to commitment should be driven by the
**variance of path confidences**: when all paths have similar confidence,
hedge; when one dominates, commit.

This also predicts that **agents with lower-noise observation channels
should commit earlier** -- they can distinguish viable from non-viable
paths faster. A developer with fast, reliable tests (low U_obs on action
outcomes) should converge on a strategy faster than one with slow,
unreliable tests. Testable.

### 2.6 Objective Revision

**Trigger**: Discovery that an objective should change -- infeasibility,
discovered opportunity, external mandate, or re-evaluation of priorities.

**Operation**: Modify an Objective node's s_target, priority, or remove/
replace the objective entirely.

*[Formulation (objective-revision)]*

    Three sub-types:

    (a) Priority reweighting: priority(o) changes.
        Trigger: new information about relative importance.
        Effect: downstream resource allocation shifts via Section 2.4.

    (b) Target revision: s_target(o) changes.
        Trigger: discovered infeasibility (delta_feasibility signal from
        03-goal-formalism-sketch Section 2.3) or discovered opportunity.
        Effect: all edges pointing toward o must be re-evaluated -- the
        causal hypotheses were about reaching the OLD target.

    (c) Objective replacement: remove o, add o'.
        Trigger: fundamental strategic reframe (directed opportunism).
        Effect: all subtrees rooted at o must be re-evaluated or pruned.
        This is the closest analog to TF-10's structural adaptation --
        not just adjusting the strategy but changing what success means.

**Connection to Boyd's Orient**: Objective revision IS Orient applied to
intent, as identified in the goal-intent gap analysis (Section 2.5).
The agent doesn't just update its model of reality (TFT's epistrophe);
it reframes what it's trying to achieve. Formally: the observation o_t
first updates M_t (epistrophe), then the updated M_t triggers a revision
of G_t (objective revision). The causal chain is:

    o_t -> delta_epistemic -> M_t update -> M_t x G_t interaction
        -> delta_feasibility or opportunity recognition -> G_t revision

This two-stage process -- reality update followed by intent revision --
is the formal content of Boyd's Orient -> Orient self-loop, which the
goal-intent gap analysis identified as "the most important arrow in
Boyd's diagram, and the one TFT couldn't capture."

**Directed opportunism** is the specific case where objective revision
is triggered by opportunity rather than infeasibility. The agent's
updated M_t reveals that a better objective is available -- one that
was not apparent before the model improved. The Auftragstaktik
commander who encounters an undefended bridge doesn't just update
their model ("the bridge is undefended"); they revise their intent
("take the bridge" instead of the original objective) because the
new M_t reveals a causal path to a higher-priority outcome.

### 2.7 The Continuity of Strategic Adaptation

[Plausible]

The six operations above form a continuum, not discrete categories:

| Operation | Edge weight change | Node change | Scope |
|-----------|-------------------|-------------|-------|
| Weight update | p_ij shifts by small delta | None | Single edge |
| Reweighting | Multiple edges shift | None | Path-level |
| Pruning | p_ij -> ~0 | Status -> failed | Branch |
| Grafting | 0 -> p_prior | New nodes possible | Branch |
| Hedging | Resource allocation shifts | None | Portfolio |
| Objective revision | All edges to o re-evaluated | o modified/replaced | Subtree |

The first four are **parametric** in the sense that they adjust the
DAG's weights. Grafting and objective revision are **structural** in
that they change the DAG's topology. But because the DAG is
probabilistic, the boundary is soft: an edge at p = 0.001 is
"structurally absent" for practical purposes, and an edge at p = 0.01
that rises to p = 0.5 is "structurally new."

This continuity resolves TF-10's sharp distinction between parametric
and structural adaptation. In the intent DAG, there is no discrete
"panic" event (TF-10's destruction-creation cycle) except as the
limiting case where ALL edge weights simultaneously collapse and
the entire DAG must be rebuilt. That limiting case is rare in practice
-- most strategic adaptation operates through local pruning, grafting,
and reweighting, not through global reconstruction.

**[Prediction 5]**: The frequency distribution of strategic changes
should follow a power law: many small weight adjustments, fewer
branch-level changes (pruning/grafting), rare subtree-level changes
(objective revision), very rare total reconstruction. This is
testable in project management data (frequency of task adjustments
vs. milestone changes vs. project pivots vs. complete restarts).

---

## 3. DAG Health Metrics

[Plausible]

What distinguishes a good strategy from a fragile one? The intent DAG's
topology and weight distribution encode structural properties that
predict robustness, efficiency, and failure modes.

### 3.1 Connectivity (Groundedness)

**Definition 3.1 (Objective reachability).** An objective node o is
**grounded** if there exists at least one directed path from some action
node a to o such that every edge on the path has p_ij > p_min.

    Grounded(o) = exists path (a, ..., o) with min_{(i,j) in path} p_ij > p_min

**Definition 3.2 (DAG groundedness).** The intent DAG is **grounded** if
every objective node is grounded.

    Groundedness(G_t) = |{o in V : tau(o) = O and Grounded(o)}| / |{o in V : tau(o) = O}|

A DAG with Groundedness < 1 contains objectives that the agent has no
credible plan to achieve -- aspirations disconnected from action. This
is not always pathological (long-term vision may be intentionally
ungrounded as a direction-setter), but for operational objectives it is
a failure of planning.

**Single points of failure**: An objective that is grounded through only
ONE path has a single point of failure. If any edge on that path fails,
the objective becomes ungrounded. The minimum edge weight on the unique
path gives the bottleneck confidence:

    Bottleneck(o) = min_{(i,j) in unique_path_to(o)} p_ij

### 3.2 Redundancy (Strategic Robustness)

**Definition 3.3 (Path redundancy).** For an objective o, the path
redundancy R(o) is the number of edge-disjoint paths from action nodes
to o with all edge weights above p_min:

    R(o) = |{P_1, ..., P_k : edge-disjoint, min-weight paths to o}|

**Definition 3.4 (Weighted redundancy).** Path redundancy counts paths
but ignores their quality. The weighted redundancy accounts for path
contributions:

    R_w(o) = 1 - product_{paths P to o} (1 - PathContribution(P, o))

This is the probability that at least one path succeeds, under the
independence assumption. R_w(o) near 1 means the objective is robustly
achievable through diverse paths. R_w(o) near the contribution of a
single dominant path means the agent is effectively committed to one
approach.

**[Prediction 6]**: For a given total resource budget, there exists an
**optimal redundancy level** that balances robustness against cost. Too
little redundancy: one failure cascades to objective failure. Too much
redundancy: resources are spread too thin, every path is under-resourced,
and none succeeds. The optimal level should depend on:
- Edge confidence variance (high variance -> more redundancy valuable)
- Path correlation (correlated failures -> redundancy less valuable)
- Resource constraints (tighter constraints -> less redundancy affordable)
- Objective criticality (higher criticality -> more redundancy warranted)

This is portfolio theory applied to strategy, but the DAG structure
provides the correlations that financial portfolio theory has to estimate
statistically.

### 3.3 Observability Coverage

**Definition 3.5 (Observability coverage).** The fraction of Key Result
nodes that have at least one Observable child with adequate quality:

    ObsCoverage(G_t) = |{k in V : tau(k) = K and exists x in children(k)
                         with tau(x) = X and noise(x) < noise_max}|
                       / |{k in V : tau(k) = K}|

**The unobservability trap**: A Key Result without observable confirmation
is dangerous. The agent cannot update the edge weights leading to or from
this node because it has no evidence about whether the node has been
achieved. The node's status remains "pending" indefinitely, its parent
edges never get the confirmatory or disconfirmatory evidence they need,
and the agent continues to allocate resources based on stale priors.

*[Formulation (unobservability-trap)]*

    For key result k with no observable children:

    - p_ij for edges incident to k cannot be updated (no evidence)
    - Resources allocated to action paths through k are based on
      prior confidence alone, never empirically corrected
    - The agent may invest heavily in a path that has already failed
      or already succeeded, without knowing which

**[Prediction 7]**: Strategies with low observability coverage should
show higher variance in outcomes (sometimes they work, sometimes they
don't, but the agent can't tell which paths are working until very
late). Strategies with high observability coverage should show lower
variance and faster convergence to either success or failure recognition.

This formally justifies the engineering practice of "observability-first
design" -- instrument before you build. And it extends to military
doctrine: the emphasis on reconnaissance and intelligence (making the
battlespace observable) is not just about building M_t; it's about
making G_t's causal hypotheses testable.

**Non-obvious implication [FIRST-PRINCIPLED — connects directly to TFT's
observation channel machinery]**: An agent should sometimes prefer a
**lower-confidence but more observable** path over a higher-confidence
but unobservable one. The observable path allows edge weight updates,
enabling faster learning about strategy viability. The unobservable
path, even if nominally more promising, is an epistemic black hole
that prevents strategic adaptation. The value of observability is
not just in knowing whether you've succeeded -- it's in the ability
to **update the rest of the strategy** based on what you learn.

### 3.4 Edge Confidence Distribution

**Definition 3.6 (Confidence entropy).** The entropy of the edge weight
distribution:

    H_conf(G_t) = - sum_{(i,j) in E} [
        p_ij * log(p_ij) + (1 - p_ij) * log(1 - p_ij)
    ] / |E|

High H_conf means edge weights are concentrated near 0.5 -- maximum
uncertainty about each causal link. Low H_conf means edge weights are
near 0 or 1 -- the agent has strong beliefs (correct or not) about
which links work.

**Strategic implications of the confidence distribution:**

- **High H_conf, early stage**: Normal. The agent hasn't tested its
  causal hypotheses yet. Prescription: explore, test paths, gather
  evidence to differentiate. Hedging is warranted.
- **High H_conf, late stage**: Pathological. The agent has been acting
  but not learning about strategy viability. Check observability
  coverage (Section 3.3) -- the agent may be in an unobservability
  trap.
- **Low H_conf, high-weight concentration**: Committed. The agent
  believes it knows which paths work. Risk: overconfidence. Check
  whether the high-weight edges have actually been tested or merely
  assumed.
- **Low H_conf, low-weight concentration**: Depleted. Most causal
  hypotheses have been tested and found wanting. The agent is running
  out of options. Prescription: graft new hypotheses (Section 2.3)
  or revise objectives (Section 2.6).

### 3.5 Depth (Strategic Fragility)

**Definition 3.7 (DAG depth).** The maximum length of any path from an
action node to an objective node:

    Depth(G_t) = max_{a in Actions, o in Objectives} |longest_path(a, o)|

**Definition 3.8 (Weighted depth).** Depth adjusted for edge confidence:

    Depth_w(P) = - sum_{(i,j) in P} log(p_ij)

This treats each edge as a probability gate. The weighted depth of a
path is the negative log-probability of the entire causal chain
succeeding. Deeper paths (more intermediate steps) accumulate more
uncertainty even if each step is high-confidence.

**The fragility of depth**: A path of length n where each edge has
confidence p has an end-to-end confidence of p^n. Even with p = 0.9
per edge:

| Path length | End-to-end confidence |
|-------------|----------------------|
| 1           | 0.90                 |
| 3           | 0.73                 |
| 5           | 0.59                 |
| 10          | 0.35                 |
| 20          | 0.12                 |

**[Prediction 8]**: Strategies with deep causal chains (many intermediate
sub-goals between action and objective) should fail more often than
strategies with shallow chains, even controlling for individual edge
confidence. This is non-obvious in practice because deep strategies
*feel* more thorough -- they decompose the problem into more steps,
which seems like careful planning. But each step is a probability
gate, and the compound probability decays exponentially with depth.

The prescription is not "avoid decomposition" but "keep each sub-chain
short and well-observed." Decompose the objective into key results, but
ensure each key result is achievable through short, high-confidence
action chains with good observability. Long, multi-step action chains
should be broken into independently confirmable segments.

### 3.6 Aggregate Health Score

[Speculative]

A composite health metric for the intent DAG:

*[Formulation (DAG-health)]*

    Health(G_t) = Groundedness * ObsCoverage * (1 - Fragility)

where:
    Fragility = 1 - min_o R_w(o) * exp(-Depth_w(critical_path(o)))

This is deliberately crude -- a placeholder for a more principled
aggregation. The point is that DAG health is a function of structural
properties (connectivity, redundancy, observability, depth), not just
a function of how close the agent is to its objectives.

**Two agents can have the same delta_goal (same distance from their
objectives) but very different DAG health.** One has a robust,
well-observed, shallow strategy. The other has a fragile, poorly-
observed, deep strategy. The formalism predicts the first will succeed
more reliably -- not because it's closer to the goal, but because its
strategy structure is more robust.

---

## 4. Interaction with M_t (Reality Model)

[Confident for the basic interaction; Speculative for the dynamics]

The intent DAG's edges are hypotheses about the causal structure of
reality. They assert: "if I do action i, it will contribute to achieving
sub-goal j." These hypotheses live in the intersection of G_t and M_t --
they are **claims about the world** embedded in a **structure of intent**.

### 4.1 The Two-DAG Architecture

The agent's state contains two causal structures:

1. **M_t's causal model**: The agent's beliefs about how reality works.
   "If X happens, Y follows." Descriptive. Updated by observation
   (TFT's epistrophe). Edges represent believed causal relationships
   in the environment.

2. **G_t's intent DAG**: The agent's strategy for changing reality.
   "If I do X, then Y will happen, and that will advance objective Z."
   Prescriptive. Updated by strategy maintenance (Section 2). Edges
   represent intended causal interventions.

**The critical relationship**: G_t's edges are a SUBSET of M_t's causal
beliefs, projected onto the agent's action space and filtered through
the agent's objectives. Every edge in G_t asserts a causal claim that
should be consistent with M_t. Formally:

*[Formulation (intent-reality-consistency)]*

    For every edge (i, j) in G_t with p_ij > p_min:

    M_t should assign non-negligible probability to the causal
    mechanism by which i's achievement would contribute to j's
    achievement.

    If M_t assigns near-zero probability to i -> j, then G_t's
    p_ij is based on a causal hypothesis that the reality model
    rejects. This is an **intent-reality inconsistency**.

### 4.2 M_t Update Triggers G_t Revision

When M_t updates (an observation arrives, epistrophe occurs), three
things can happen to G_t:

**(a) Edge weights update (routine).** The observation confirms or
disconfirms a causal hypothesis used by G_t. The relevant edge weight
p_ij is revised per Section 2.1. This is the normal, continuous
interaction between M_t and G_t.

Example: A developer writes code (action), runs tests (observation),
and the tests pass (confirmation). The edge weight from "implement
feature X" to "feature X works" increases. M_t updated ("the code
now includes X"), and this update provides evidence for G_t's causal
hypothesis ("writing that code will make X work").

**(b) Edges become untenable (pruning trigger).** M_t's update reveals
that a causal link in G_t doesn't hold -- the mechanism the agent was
relying on doesn't work the way the agent thought.

Example: A developer discovers that the middleware framework doesn't
support the session management approach they planned. M_t updates
("the framework works differently than I thought"), and this
invalidates G_t's edge from "add session middleware" to "sessions
persist." The edge weight drops, potentially below p_min, triggering
pruning.

**(c) New edges become apparent (grafting trigger).** M_t's update
reveals a causal pathway the agent didn't know about. A new edge
can be grafted into G_t.

Example: While investigating a test failure, a developer discovers
an existing utility function that does exactly what they need for
their feature. M_t updates ("this utility exists and does Y"), and
this enables a new edge in G_t from "use existing utility Z" to
"sub-goal Y achieved." This is directed opportunism at the
tactical level.

### 4.3 The Orient Cycle Formalized

**[FIRST-PRINCIPLED — this is AAD's central contribution.]**

The three interactions above constitute the formal content of Boyd's
Orient. This is what TFT was missing and what AAD adds: the cascade from
reality-model update to strategy revision to goal reframing.

TFT formalizes observation → model update (aisthesis → epistrophe). AAD
extends the chain: observation → model update → strategy update →
feasibility check → goal revision. Each stage is principled — it follows
from the previous stage via the intent-reality consistency requirement
(§4.1). The cascade is not a design choice; it's a necessary consequence
of having strategy edges that are hypotheses about reality.

*[Formulation (orient-cycle)]*

    Aisthesis: o_t arrives
    Aporia (epistemic): delta_epistemic = o_t - hat{o}_t
    Epistrophe: M_t updates (TFT's standard machinery)

    --- M_t x G_t interaction (Boyd's Orient proper) ---

    Aporia (strategic): For each edge (i,j) in G_t,
        evaluate consistency of p_ij with updated M_t

    Epistrophe (strategic):
        (a) Update edge weights where evidence arrived
        (b) Prune edges that M_t now rejects
        (c) Graft edges that M_t now enables

    Aporia (feasibility): Evaluate whether objectives remain
        achievable given updated G_t

    Epistrophe (goal): If feasibility check fails,
        trigger objective revision (Section 2.6)

This is a cascade: observation -> reality model update -> strategy
update -> feasibility check -> possible goal revision. Each stage
depends on the output of the previous one. The cascade runs from
the most routine (edge weight adjustment) to the most disruptive
(objective revision), and most of the time it terminates at stage (a)
-- edge weight adjustment is the normal case, objective revision is
rare.

**Connection to temporal nesting (TF-11)**: The Orient cascade
respects the timescale separation principle. Edge weight updates
(fast, continuous) are nested within pruning/grafting decisions
(slower, less frequent), which are nested within objective revision
(slowest, rarest). If the slower processes act before the faster
ones have converged -- e.g., revising objectives before edge weights
have stabilized from the latest observation -- the agent oscillates
strategically.

    nu_{weight-update} >> nu_{prune/graft} >> nu_{objective-revision}

Violation of this ordering is a known pathology: "strategic thrashing,"
where the agent constantly changes its high-level goals before giving
any strategy a chance to work. The temporal nesting constraint formally
predicts this failure mode.

### 4.4 The Separation Question Revisited

The goal-formalism sketch (Section 5) noted that M_t and G_t have an
asymmetric separation: M_t can be updated independently of G_t, but
G_t depends on M_t. The intent DAG formalism makes this precise:

- **M_t is updated from observations alone** (TFT's machinery is
  complete and self-contained for this).
- **G_t is updated from observations PLUS M_t** (the orient cycle
  above). Every G_t update depends on M_t for evaluating whether
  causal hypotheses hold.
- **Action selection depends on both** (the extended policy objective
  from 03-goal-formalism-sketch Section 4.1).

The separation fails exactly at the point where the intent DAG's edges
are hypotheses about reality. If the edges were certainties (all p_ij
in {0, 1}), the strategy would be fixed and independent of M_t. The
more uncertain the strategy (high H_conf from Section 3.4), the more
tightly coupled G_t and M_t become. This gives a precise meaning to
"the uncertain strategist needs a better reality model than the certain
one" -- uncertainty in G_t amplifies the dependency on M_t.

---

## 5. OKR Mapping (Motivating Example)

**[SCAFFOLD — domain instantiation, not core theory.]** The OKR mapping
demonstrates the formalism captures real strategic practice and provides
a concrete vocabulary for the abstract definitions. The failure-mode
diagnostics (§5.2) are where the formalism earns value beyond standard
OKR wisdom. The structural mapping (§5.1) and extended example (§5.3) are
illustrations.

[Confident]

The OKR (Objectives and Key Results) framework, originally developed by
Andy Grove at Intel and popularized by John Doerr, provides a natural
mapping to the intent DAG that demonstrates the formalism captures
real strategic practice.

### 5.1 Structural Mapping

| OKR Concept | DAG Element | Formal Properties |
|-------------|-------------|-------------------|
| **Objective** | Objective node (tau = O) | s_target, U_target, priority |
| **Key Result** | Key Result node (tau = K) | criterion, deadline, status |
| **Initiative** | Action node (tau = A) or subgraph of A nodes | action, cost, reversibility |
| **KR confidence** | Edge weight from Initiative to KR | p_ij (will this initiative achieve this KR?) |
| **KR measurement** | Observable node (tau = X) attached to KR | channel, latency, noise |
| **OKR alignment** | Edges from KR to Objective | p_ij (will this KR contribute to this Objective?) |
| **OKR health** | DAG health metrics (Section 3) | Groundedness, Redundancy, Obs. Coverage, Depth |
| **OKR review** | Orient cycle (Section 4.3) | Weight update, prune, graft, objective revision |
| **Stretch goal** | Low-confidence edge to high-priority objective | p_ij low, priority(o) high |
| **Committed goal** | High-confidence edge to critical objective | p_ij high, priority(o) high |

### 5.2 What the Formalism Adds to OKR Practice

Standard OKR practice has well-known failure modes. The DAG formalism
provides formal diagnostics for each:

**Failure mode 1: Vanity KRs.** Key Results that can be "achieved" without
actually contributing to the Objective. In DAG terms: the edge from KR to O
has theta_ij near 0 -- even if the KR is achieved, it doesn't advance the
objective. The DAG makes this visible through the PathContribution
computation (Section 2.4): a KR with high status "confirmed" but low
theta to any objective is contributing nothing.

**Failure mode 2: Unobservable KRs.** "Improve customer satisfaction" with
no measurement attached. In DAG terms: ObsCoverage < 1 (Section 3.3).
The formalism identifies this as a structural fragility: the agent cannot
update edge weights through this KR because there's no observable
confirmation.

**Failure mode 3: Linear dependency chains.** One initiative feeds one KR
feeds one Objective, with no redundancy. In DAG terms: R(o) = 1 (Section
3.2) -- a single point of failure. If the initiative fails, the entire
chain collapses.

**Failure mode 4: OKR overload.** Too many objectives, too many KRs,
insufficient action capacity. In DAG terms: the agent's action capacity
(total resource budget) is less than the sum of costs on the minimum set
of actions needed to ground all objectives. Formally:

    sum_{a in min_action_set} cost(a) > budget

where min_action_set is the minimum-cost set of actions that provides at
least one path to every objective.

**Failure mode 5: Quarterly rigidity.** OKRs are set quarterly and not
revised, even when reality changes. In DAG terms: the Orient cycle
(Section 4.3) is disabled. Edge weights never update, pruning never
happens, grafting never happens. The agent pursues a stale strategy.
The temporal nesting constraint (Section 4.3) predicts that edge
weight updates (which should happen continuously) are being throttled
to the same frequency as objective revision (quarterly) -- a severe
timescale violation.

### 5.3 Example: A Software Product OKR

    Objective: "Users can authenticate via OAuth by end of Q2"
    priority = high, U_target = low (clear spec)

    KR1: "OAuth flow returns valid token in < 500ms"
    criterion: test_oauth_token_flow passes AND p95_latency < 500ms
    deadline: Week 8

        Initiative A: Implement token endpoint using auth library X
        cost: 3 dev-days, reversibility: 0.7
        Edge A -> KR1: p = 0.8 (library X is well-documented)
                        theta = 0.9 (covers most of the KR)

        Initiative B (hedge): Implement token endpoint using raw HTTP
        cost: 5 dev-days, reversibility: 0.8
        Edge B -> KR1: p = 0.6 (more manual work, more room for error)
                        theta = 1.0 (covers the full KR)

        Observable X1: test_oauth_token_flow result
        channel: CI pipeline, latency: minutes, noise: low

    KR2: "Sessions persist across requests for 24 hours"
    criterion: test_session_persistence passes
    deadline: Week 10

        Initiative C: Add session middleware
        cost: 2 dev-days, reversibility: 0.9
        Edge C -> KR2: p = 0.85, theta = 1.0

        Observable X2: test_session_persistence result
        channel: CI pipeline, latency: minutes, noise: low

    KR3: "Existing auth test suite remains green"
    criterion: all existing auth tests pass
    deadline: continuous

        (No initiative needed -- this is a monitoring KR)

        Observable X3: existing auth test results
        channel: CI pipeline, latency: minutes, noise: very low

    Edges KR1 -> O: p = 0.95, theta = 0.5
    Edges KR2 -> O: p = 0.90, theta = 0.3
    Edges KR3 -> O: p = 0.99, theta = 0.2

**DAG health assessment:**
- Groundedness: 1.0 (all objectives reachable from actions)
- Redundancy: R(O) via KR1 = 2 (two initiatives), via KR2 = 1 (single point of failure)
- ObsCoverage: 1.0 (every KR has an observable)
- Depth: 3 (action -> KR -> objective)
- Confidence entropy: moderate (mix of 0.6-0.95 edges)

**The formalism's prescription**: KR2 is a single point of failure (one
initiative, no hedge). If the session middleware approach fails, there's
no fallback. A cautious agent would either add a hedging initiative for
KR2 or lower the confidence that KR2 is achievable, which would trigger
earlier feasibility investigation.

---

## 6. Domain Instantiations

[Plausible]

### 6.1 Comparison Table

| Property | PID Controller | Software Development | Military Operations | AI Agent Task |
|----------|---------------|---------------------|--------------------|----|
| **Objective nodes** | 1 (setpoint) | 1-5 (features/milestones) | 1-3 (mission objectives) | 1-3 (task completion) |
| **KR nodes** | 0 (implicit) | 3-20 (acceptance criteria) | 5-30 (phase lines, conditions) | 2-10 (sub-task completion) |
| **Action nodes** | 1 (control output) | 10-100 (code changes) | 10-1000 (unit actions) | 5-50 (tool calls) |
| **Observable nodes** | 1 (sensor) | 5-50 (test results, metrics) | 5-100 (intel reports, recon) | 3-30 (output checks) |
| **Typical depth** | 1 | 2-4 | 3-6 | 2-4 |
| **Typical redundancy** | 1 (no hedging) | 1-3 (some hedging) | 2-5 (deliberate redundancy) | 1-2 (limited hedging) |
| **ObsCoverage** | 1.0 (direct sensor) | 0.5-0.9 (incomplete testing) | 0.3-0.7 (fog of war) | 0.6-0.9 (output validation) |
| **Edge confidence range** | ~1.0 (known physics) | 0.3-0.95 (varying familiarity) | 0.1-0.8 (high uncertainty) | 0.4-0.9 (tool reliability) |
| **Pruning frequency** | Never | Weekly | Hourly-daily | Per-step |
| **Grafting frequency** | Never | Weekly | Daily | Per-step |
| **Objective revision** | External only | Sprint/quarter boundaries | As intel requires | Rare (task is given) |
| **Primary fragility** | None (trivial DAG) | Low obs coverage | Low obs coverage + depth | Low redundancy |

### 6.2 Domain Narratives

**PID controller.** The trivial case. G_t = single objective node
(setpoint). No DAG structure to speak of. The formalism correctly
identifies this as the degenerate case where the point-in-S model
suffices and the DAG machinery adds no value. This is consistent
with Section 1.4.

**Software development.** A rich DAG with moderate depth, variable
observability, and significant opportunity for grafting (discovering
better implementation approaches as comprehension deepens). The
primary fragility is observability coverage: aspects of the system
that lack tests are unobservable sub-goals, creating the
unobservability trap (Section 3.3). The formalism predicts that
**test-first development** (writing tests before code) is not just
a quality practice but a **strategy enablement** practice -- it
raises ObsCoverage before action, enabling faster edge-weight
convergence and earlier failure detection. This is a formal
justification for TDD that doesn't depend on quality arguments but
on strategic adaptability.

Specific to software: the code itself, once written, becomes part
of M_t (the reality model). So a software action simultaneously
advances G_t (closes delta_goal) and modifies M_t (the codebase
is now different). This tight coupling between action and model
means the separation principle fails strongly: every action that
changes the code also changes the reality the agent is modeling,
which may change the viability of other edges in the intent DAG.
This formally captures the well-known phenomenon of "plan
disruption" in software: implementing feature A changes the
codebase in ways that affect the viability of the plan for
feature B.

**Military operations.** The deepest and most uncertain DAGs. Many
layers of sub-objectives (strategic -> operational -> tactical),
high uncertainty on most edges (fog of war), deliberate redundancy
(military doctrine prescribes multiple axes of advance), and very
low observability coverage (intel is always incomplete). The
formalism predicts:

1. Military doctrine should emphasize redundancy (it does:
   "two is one, one is none")
2. Reconnaissance should be prioritized as strategy enablement,
   not just situation awareness (it is: intel drives the plan)
3. Plans should be shallow where possible (military principle of
   simplicity: fewer intermediate objectives = less compound
   uncertainty)
4. Objective revision should be enabled at every level
   (Auftragstaktik: subordinates can revise intermediate objectives
   to serve commander's intent)

The fit between the formalism's predictions and existing military
doctrine is encouraging but insufficient as validation -- the
doctrine might just be encoding common sense that any formalism
would recover. The stronger test would be: does the formalism
predict something about military strategy that is NOT already in
doctrine? (See Open Questions, Section 7.)

**AI agent task execution.** A medium-depth DAG with fast pruning
and grafting cycles (the agent tests hypotheses in seconds, not
weeks). The distinctive feature: the agent's reality model M_t is
rebuilt from scratch at each session (100% context turnover), but
G_t may persist across sessions (via task description, CLAUDE.md,
conversation context). This means:

- The agent must graft its entire M_t -> G_t connection layer at
  session start (the "cold start" problem: re-establishing which
  causal hypotheses in G_t are supported by the current reality)
- G_t's STRUCTURE may persist (the task decomposition is similar
  session to session) even though the edge WEIGHTS must be
  re-estimated (the agent doesn't remember which approaches
  worked last time)
- The value of G_t persistence (via CLAUDE.md and similar
  artifacts) is precisely the cost savings of not having to
  re-derive the DAG structure from scratch -- the agent inherits
  a topology and only needs to re-estimate weights

**[Prediction 9]**: AI agents with access to persistent intent
artifacts (well-written task descriptions, CLAUDE.md with strategic
guidance, documented decision history) should converge faster than
agents that must derive intent from scratch. The value of these
artifacts should be proportional to the complexity of the intent
DAG they encode -- simple tasks (shallow DAG) benefit less from
persistent intent than complex tasks (deep DAG with many branches).

---

## 7. Open Questions

### 7.1 Interaction Terms Between Parent Edges

[Speculative]

Section 1.2 assumed approximate independence of parent contributions
to a node. This breaks when:
- Two actions synergize (doing both produces more than the sum)
- Two actions conflict (doing both produces less than the sum, or
  one undermines the other)
- There are ordering constraints (A must complete before B starts)

A richer model would use interaction terms or a factor graph
representation. But this may be over-engineering for a first
treatment. The independence assumption is a reasonable default that
can be relaxed in domain-specific instantiations.

**How important is this?** Possibly very. In software, ordering
constraints and conflicts between actions are pervasive (you can't
integrate the auth library until the dependency manager is configured).
In military operations, synchronization and sequencing are
fundamental (the air campaign must degrade air defenses before
ground forces advance). If the formalism can't represent these
interactions, it's missing something essential.

### 7.2 How Should p_min Be Set?

[Speculative]

The pruning threshold p_min appears in multiple definitions but is
treated as a free parameter. What determines the right value?

One approach: p_min should be set so that the expected cost of
continuing a branch below p_min exceeds the expected cost of
abandoning it:

    p_min = cost_of_continuing / (cost_of_continuing + cost_of_abandoning)

This is a simple decision-theoretic derivation. But "cost of
abandoning" includes the option value of the branch -- a low-confidence
branch might become viable later if new evidence arrives. Accounting
for option value makes p_min lower (hold onto branches longer).

### 7.3 Computational Tractability

[Speculative]

For small DAGs (the PID, the OKR example), the operations in Sections
2-3 are trivially computable. For large DAGs (a military campaign with
thousands of nodes, or a complex software project), path contribution
computations, redundancy calculations, and portfolio optimizations may
become expensive. Are there efficient approximations?

The DAG structure helps: topological sort enables single-pass forward
propagation of contributions. The bottleneck is likely the portfolio
optimization (Section 2.5), which is NP-hard in general. But in
practice, the branching factor at each node is small (an action
typically has 1-3 intended effects, not 100), so exact computation
may be feasible for realistic DAG sizes.

### 7.4 Does the Formalism Produce Non-Obvious Predictions?

The critical self-test. Candidate non-obvious predictions generated so
far:

1. **Observability as strategy enablement** (Section 6.2, software):
   TDD is not just a quality practice but a strategic adaptation
   enabler. This is a novel framing -- existing TDD justifications
   focus on defect prevention, not on strategic adaptability.

2. **Optimal redundancy depends on edge confidence variance** (Section
   3.2, Prediction 6): When edge confidences are homogeneous, less
   redundancy is needed. When they are heterogeneous, more is needed.
   This is not standard portfolio theory (which focuses on return
   variance, not probability-of-success variance).

3. **Depth as fragility** (Section 3.5, Prediction 8): Compound
   probability decay makes deep strategies exponentially fragile. The
   prescription "short chains with frequent confirmation" is stronger
   than the intuition "break it into steps" because it quantifies the
   cost of each additional step.

4. **Comprehension enables strategy discovery** (Section 2.3, Prediction
   3): The rate of grafting (new strategic possibilities) should
   correlate with epistemic tempo. This connects TFT's epistemic
   machinery to strategic capability in a way that the existing
   formalism (TFT without G_t) cannot express.

5. **Strategic thrashing as timescale violation** (Section 4.3):
   Premature objective revision (before edge weights stabilize) is
   predicted to degrade performance. This gives a formal explanation
   for the common management failure of "pivoting too often" that goes
   beyond the intuition "be patient."

6. **The value of persistent intent artifacts scales with DAG
   complexity** (Section 6.2, Prediction 9): Simple tasks don't
   benefit much from CLAUDE.md or detailed specs. Complex tasks
   benefit enormously. This predicts where to invest in documentation.

Are these truly non-obvious, or are they formalizations of what
practitioners already know? Probably a mix. The depth-as-fragility
result (compound probability decay) is genuinely quantitative -- it
tells you that a 10-step plan with 90% per-step confidence has only
35% end-to-end confidence, which many people would not intuit. The
observability-as-strategy-enablement framing is a genuine re-framing
of TDD. The strategic-thrashing result gives a formal timescale
criterion that goes beyond "be patient" to "how long should you wait?"

The formalism has not (yet) dithered into impotence, but it hasn't
produced a truly surprising prediction either. The strongest test
would be: can the formalism predict the outcome of a known strategic
situation that was NOT obvious to the participants at the time?

### 7.5 How Does the DAG Connect to TFT's Dynamics?

[Speculative]

The goal-formalism sketch (Section 6) defined goal tempo T_goal as the
rate at which the agent closes delta_goal. In DAG terms, this becomes:

    T_goal = rate at which pending nodes transition to "confirmed"
             weighted by their contribution to objectives

But the dynamics are more complex than a single rate. Different parts
of the DAG may progress at different rates. An agent might have high
goal tempo on one sub-goal (fast progress on KR1) and low goal tempo
on another (stuck on KR2). A scalar T_goal loses this structure, just
as TF-11 Open Question #4 notes that scalar tempo T loses the
anisotropy of epistemic adaptation.

A goal-tempo tensor, parallel to the tempo tensor mentioned in TF-11,
would capture directional goal progress. But this may be over-
formalization for the current stage of development.

### 7.6 Goal Uncertainty U_G in the DAG Setting

The goal-formalism sketch defined U_G as uncertainty about what the
agent wants. In the DAG formalism, U_G decomposes into:

1. **Objective uncertainty**: U_target on each objective node (how
   precisely does the agent know what it wants?)
2. **Structural uncertainty**: Is the DAG topology right? Are the
   right edges present? (This is meta-uncertainty about the strategy.)
3. **Weight uncertainty**: How reliable are the p_ij estimates?
   (Captured by the beta-distribution parameters alpha_ij, beta_ij.)

Components 1 and 3 are well-handled by the formalism. Component 2 --
structural uncertainty, the possibility that the DAG is missing
critical edges or contains spurious ones -- is harder. It's the
intent-level analog of TF-10's model class fitness: is the strategy
structure itself adequate, or does the agent need a fundamentally
different plan?

### 7.7 When Does the DAG Formalism Not Apply?

Where should we NOT expect the intent DAG to be useful?

1. **Pure reactive agents** (no planning horizon): Reflexive systems
   that don't maintain any representation of future goals. The DAG
   has zero nodes. TFT's M_t-only formalism is complete.

2. **Single-step goals** (trivial DAG): The PID setpoint, the
   thermostat temperature. The DAG formalism adds no value over the
   point-in-S model.

3. **Continuous optimization without discrete sub-goals**: Gradient
   descent on a loss function has a "goal" (minimize loss) but no
   sub-goal structure. The action at each step is determined by the
   gradient, not by a causal plan. There's no DAG -- just a
   direction in parameter space.

4. **Goals that are fundamentally non-decomposable**: "Be creative."
   "Find something interesting." Goals that resist decomposition into
   sub-goals and action plans. These might be better modeled as
   search over DAGs (what strategy could achieve this vague
   objective?) rather than maintenance of a fixed DAG structure.

The formalism's scope is: **agents with non-trivial, decomposable goals
that persist across multiple action steps and can be assessed through
intermediate observations.** This is a meaningful scope -- it covers
project management, military operations, software development, multi-
step AI agent tasks, and organizational strategy. But it does not cover
all agency, and the formalism should not claim to.

---

## 8. Relationship to Existing Work

### 8.1 vs. Hierarchical Task Networks (HTN)

HTN planning decomposes tasks into subtasks with ordering constraints.
The intent DAG resembles an HTN but differs in:
- **Probabilistic edges**: HTN methods and operators are deterministic;
  the intent DAG's edges have confidence weights
- **Observability**: HTN doesn't model how the agent knows whether a
  subtask succeeded; the intent DAG has explicit observable nodes
- **Continuous maintenance**: HTN plans are typically generated once
  and executed; the intent DAG is continuously updated during execution
- **Bayesian updates**: HTN has no mechanism for edge weight updates
  from observation; the intent DAG has explicit Bayesian revision

The intent DAG can be viewed as a "probabilistic HTN with observability
constraints and continuous replanning."

### 8.2 vs. Influence Diagrams and Decision Networks

Influence diagrams (Howard & Matheson, 1984) are DAGs with decision
nodes, chance nodes, and utility nodes. The structural similarity is
clear. Differences:
- **Purpose**: Influence diagrams model a single decision under
  uncertainty. The intent DAG models an ongoing strategy with
  multiple decisions over time.
- **Dynamics**: Influence diagrams are static (one-shot decision).
  The intent DAG evolves continuously.
- **The "intent" aspect**: Influence diagrams describe what the agent
  should decide. The intent DAG describes what the agent is TRYING
  TO DO -- its theory of how actions produce outcomes. This is a
  prescriptive plan, not a decision model.

### 8.3 vs. Active Inference (Prior Preferences)

Active inference includes "prior preferences" (a distribution over
desired observations). The intent DAG's objectives correspond to prior
preferences, but the DAG adds:
- **Strategy structure**: Active inference doesn't represent HOW the
  agent expects to achieve its preferences, just what they are
- **Causal edges**: Active inference's generative model encodes causal
  beliefs, but the *strategic use* of those beliefs (which causal
  paths to exploit for goal achievement) is implicit in policy
  selection, not represented as a first-class object
- **Observability design**: Active inference doesn't distinguish
  between observations that inform the world model and observations
  that confirm strategy progress

### 8.4 vs. Partially Observable Markov Decision Processes (POMDPs)

POMDPs provide the formal framework within which the intent DAG lives.
The POMDP's reward function encodes the objective; the POMDP's
transition model encodes the causal structure; the POMDP's observation
model encodes observability. The intent DAG is a **structured
representation of a (partial) POMDP policy** -- it describes which
states the agent is trying to reach, through which intermediate states,
using which actions, with which expected observations along the way.

The DAG formalism adds value over a raw POMDP solution in the same way
that a plan adds value over a policy: it makes the strategic structure
explicit, inspectable, communicable (for shared intent), and locally
modifiable (for strategy maintenance). You can't prune a branch of a
POMDP policy because a POMDP policy doesn't have branches -- it has
state-conditioned actions. The intent DAG's structure is the bridge
between the POMDP's formal correctness and human (or agent) strategic
reasoning.

---

## 9. Summary and Assessment

### 9.1 What the Formalism Provides

1. **A formal object for intent**: G_t = (V, E, w, tau), with typed
   nodes, weighted edges, and structural constraints.

2. **Operations on intent**: Weight update, pruning, grafting,
   reweighting, hedging, objective revision -- all formalized as
   mathematical operations on the DAG.

3. **Health metrics**: Groundedness, redundancy, observability
   coverage, confidence distribution, depth -- structural properties
   that predict strategy robustness independently of how close the
   agent is to its goals.

4. **M_t interaction formalized**: The Orient cycle as a cascade from
   observation through reality model update through strategy revision,
   with timescale constraints.

5. **Domain mapping**: The formalism applies to PID (degenerate),
   software development, military operations, and AI agent tasks,
   with domain-specific predictions.

6. **Continuity of structural change**: The soft boundary between
   parametric and structural adaptation, resolving TF-10's sharp
   distinction.

### 9.2 Epistemic Status

| Component | Status | Confidence |
|-----------|--------|------------|
| Node types and edge definition | [Confident] | Natural and well-motivated |
| DAG structure and constraints | [Confident] | Standard graph theory |
| Edge weight update (Bayesian) | [Plausible] | Mirrors TFT's proven mechanism |
| Pruning/grafting operations | [Plausible] | Descriptively correct, thresholds uncertain |
| Health metrics | [Plausible] | Well-defined but untested |
| Orient cycle cascade | [Plausible] | Structurally compelling, dynamics unproven |
| OKR mapping | [Confident] | Natural bijection |
| Domain predictions | [Speculative] | Need empirical testing |
| Aggregate health score | [Speculative] | Placeholder, needs principled aggregation |
| Computational tractability | [Speculative] | Seems OK for realistic sizes, unverified |

### 9.3 The Non-Triviality Verdict

Has the formalism dithered into impotence? Partially. Many of its
predictions (plan ahead, check progress, adapt when things change) are
things any competent practitioner knows. But several predictions are
genuinely quantitative or structural:

- **Compound probability decay** makes the cost of depth precise
- **Observability-as-strategy-enablement** reframes TDD and recon
- **Optimal redundancy as a function of edge variance** goes beyond
  "have a backup plan"
- **Strategic thrashing as timescale violation** gives a formal
  criterion for when to stop changing course
- **Comprehension-enables-strategy** connects epistemic tempo to
  strategic capability in a formally trackable way

The formalism has earned its right to exist but has not yet produced
a truly surprising result. The strongest path to non-triviality is
likely: derive a quantitative prediction about DAG health metrics that
can be tested against real project outcome data. If the formalism
predicts project success/failure better than simpler models (e.g., just
delta_goal magnitude), it has demonstrated genuine value.

### 9.4 Next Steps

1. **Formalize the goal tempo** in DAG terms and connect to TFT's
   persistence condition. Under what conditions does goal persistence
   fail in the DAG framework?

2. **Work the LQG case** through the DAG formalism to verify it
   reproduces the known separation principle as a degenerate case.

3. **Develop the beta-Bernoulli edge update** more carefully and
   connect to TFT's gain structure.

4. **Find a domain where the formalism makes a surprising prediction.**
   The best candidate is likely software engineering, where we have
   access to detailed project data (commits, tests, timelines) that
   could ground the DAG metrics empirically.

5. **Investigate interaction terms** (Section 7.1) -- are they
   essential or can the independence assumption survive for a useful
   range of applications?

6. **Connect to shared intent**: How does one agent communicate a
   DAG to another? The IB compression of shared intent (from the
   goal-formalism sketch, Section 7.2) should operate on the DAG:
   compress the DAG to the minimum structure that enables the
   recipient to exercise directed opportunism. What does this
   compression look like formally?
