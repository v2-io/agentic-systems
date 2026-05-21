Please conduct a deep prior-art search across academic literature. We are establishing scientific precedence for a theoretical framework of agency (AAT).

## The Core Idea / Claim
Agent plans/strategies are modeled as Causal DAGs with probabilistic AND/OR nodes. Crucially, the standard agent action-perception loop intrinsically generates Pearl Level-2 (interventional) data simply because acting breaks natural causal symmetries. As strategies deepen, they suffer a "triple depth penalty" (probabilistic decay, delayed credit/evidence starvation, and maintenance cost). When sibling actions share a latent common cause (causal insufficiency), agents must use a "Correlation Hierarchy" to augment the DAG and avoid failure.

## Boundaries of the Claim
- Domain: Causal RL, automated planning, reliability engineering, decision theory.
- Constraints: Plans where edges represent single-parameter credences (probability of step success), not full conditional probability tables.

## What Kind of Match Counts
- Epistemological proofs or claims that an active agent's interaction loop inherently constitutes a `do()` intervention (Pearl L2) on a singular trajectory.
- Modeling plans as AND/OR DAGs with probabilistic decay.
- Formalizations of the "triple depth penalty" or compounding fragility in deep hierarchical planning.
- Use of causal interventional data to detect latent common causes (causal insufficiency) in agent strategies.

## What Would NOT Count
- Standard Bayesian Networks that require full conditional probability tables (CPTs) instead of single-parameter step credences.
- Standard MDP value iteration or deep RL planning that does not explicitly construct causal DAGs of the strategy.
- Papers just using Pearl's hierarchy without applying it to an agent's internal plan validation.

## Known Anchors
- Judea Pearl (Causal Hierarchy, do-calculus)
- Causal Reinforcement Learning
- AND/OR graphs in automated planning

## Search Scope
- Looking for both exact mechanism matches and broader conceptual overlaps.
- Strictly academic papers (no patents/IP).