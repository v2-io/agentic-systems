Please conduct a deep prior-art search across academic literature. We are establishing scientific precedence for a theoretical framework of agency (AAT).

## The Core Idea / Claim
Agents diagnose failure by orthogonally splitting "Satisfaction Gap" (is the goal achievable at all?) from "Control Regret" (is my current strategy optimal?). This forces an "Orient Cascade"—a strict update order: update model -> check satisfaction -> check regret -> revise strategy -> revise goal. Furthermore, exploration is driven not just by epistemic uncertainty, but by a Lyapunov survival drive: an agent in a drifting world *must* explore to refresh observations to satisfy its persistence sector condition. Lastly, this tracking strictly requires exponential forgetting; without it, confidence calcifies and the agent fails.

## Boundaries of the Claim
- Domain: Decision theory, non-stationary RL, active inference, cognitive architectures.
- Assumptions: Agents in non-stationary environments where goals might become physically unachievable.

## What Kind of Match Counts
- Diagnostic frameworks that explicitly separate goal-feasibility (satisfaction) from policy-suboptimality (regret) into a 2x2 matrix or distinct signals.
- Strict, mathematically-forced orderings of internal cognitive updates (analogous to the Orient Cascade).
- Derivations of exploration drives motivated by survival/viability against environmental drift (not just maximizing information gain).
- Proofs that bounded memory or "forgetting" is formally required to track non-stationary environments and prevent confidence calcification.

## What Would NOT Count
- Standard UCB or epsilon-greedy exploration that assumes stationary environments and seeks only to minimize regret.
- Regret bounds that assume the goal is always achievable (ignoring the satisfaction gap).
- General OODA loop papers that do not provide mathematical dependency-forcing for the cascade order.

## Known Anchors
- Satisfaction vs Regret in decision theory
- Viability-driven exploration
- Non-stationary RL forgetting factors
- Bounded effective sample size in Bayesian tracking

## Search Scope
- Close implementations and conceptual framing.
- Strictly academic papers (no patents/IP).