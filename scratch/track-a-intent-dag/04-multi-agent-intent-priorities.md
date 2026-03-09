# Multi-Agent Intent Propagation: Priority Questions

**Status**: Direction-setting notes. The single-agent DAG formalism is necessary
scaffolding but the uniquely valuable predictions should come from multi-agent
intent dynamics. These questions should guide the next phase of Track A work.

## Priority Questions

### 1. Intent Decomposition

How does a commander's high-level intent DAG get decomposed into sub-DAGs
assigned to subordinate agents? The decomposition is a *cut* through the DAG
that assigns nodes and edges to agents. Where you cut matters:

- Cut through high-confidence, well-observed edges → loosely coupled sub-DAGs
  (subordinates can operate independently; coordination is low-cost)
- Cut through uncertain, unobservable edges → tightly coupled sub-DAGs
  (subordinates must coordinate constantly; fragile)

**Prediction**: The optimal decomposition minimizes the uncertainty on
inter-agent edges (the edges that span the cut). This is a graph-partitioning
problem with edge weights as the partitioning criterion.

### 2. Directed Opportunism as Constrained Local Grafting

When a subordinate's M_t update reveals a new edge, they graft it locally.
But this graft might change the inter-agent coordination contract. The question:
how much can a subordinate's local G_t diverge from the commander's intended
decomposition before the team's aggregate DAG becomes incoherent?

The Auftragstaktik IB principle: shared intent should compress to exactly the
constraints that keep inter-agent edges viable while leaving intra-agent edges
free for local adaptation. Over-specified: subordinate can't graft. Under-
specified: subordinate's grafts may break coordination.

### 3. Adversarial Dynamics on DAGs

An adversary targets specific edges in the opponent's intent DAG. The most
valuable targets are:
- High-centrality edges (cut these and the DAG fragments)
- Inter-agent coordination edges (fragment the team's coherence)
- Edges to observables (blind the opponent to progress/failure)

The effects spiral becomes: pruning the opponent's DAG faster than they can
graft replacements. The tempo advantage has structural interpretation: the
faster agent can identify and target critical edges in the slower agent's DAG.

### 4. Team Persistence via DAG Redundancy

Appendix F's "teams persist where individuals can't" gets structural
explanation: the team's aggregate DAG has:
- More paths to objectives (higher redundancy → R_w closer to 1)
- More observation channels (higher observability coverage)
- Ability to re-route around failed edges (reassign sub-DAGs between agents)
- Collective grafting capacity (agent j discovers a path that agent i
  didn't know about → communication gain from Appendix F)

### 5. Trust and Intent Communication

From the goal formalism sketch §7.1, intent communication has gain:

    eta_intent = U_G_i / (U_G_i + U_channel + U_authority + U_alignment)

In DAG terms: what's being communicated isn't just "here's the goal" but
"here's my sub-DAG, here are the edges I'm confident about, here are the
ones I'm uncertain about." The trust model becomes: do I believe this agent's
reported edge weights? An adversary could communicate a DAG with inflated
edge weights to induce the recipient to commit to paths that will fail.

## Evaluation Criterion for DAG Formalism Alternatives

The alternative formalism experiments (02-alt-clean-slate, 03-alt-and-or-dag)
should be evaluated partly on how naturally they extend to multi-agent settings.
A formalism that handles single-agent strategy cleanly but doesn't extend to
multi-agent intent propagation is missing the most important use case.
