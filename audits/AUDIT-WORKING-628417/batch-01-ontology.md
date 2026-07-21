# Batch 1 — Ontology of the Coupling
Segments: `#def-agent-environment`, `#def-action-transition`, `#def-observation-function`, `#def-chronica`, `#scope-adaptive-system`

## What I hadn't anticipated

**Double opacity, not single.** I came in expecting "partial observability" as the main move. The action-transition segment is sharper: *joint* opacity of $h$ and $T$ is what makes adaptation necessary rather than mere optimization. Known $T$ → planner; known $h$ with unknown $T$ is different again. The dual is load-bearing and I had flattened it to one slogan.

**Markov-of-$\Omega$ as breadth commitment, with asymmetry vs $M_t$.** The move "extend $\Omega$ until Markov" is free for the environment (unbounded). Later, the same form for $M_t$ will *not* be free — capacity wall. That parallel-form / asymmetric-cost point is pedagogically excellent and was not in my initial predictions.

**Adaptive scope admits pure observers.** Part I is deliberately about Kalman-with-no-control and passive Bayesian learners. Epistemic-first, actuation-second. I had mentally started with "agents that act"; the cascade is more careful.

**Chronica is the spine, model is compression.** I knew this abstractly; reading it in sequence after $h$ and $T$ makes the *ordering* claim land: action committed before next observation is physical, not notational. Non-forkability is about trajectories, not byte-copyable representations — and that distinction is already the Three-Deaths seed, not a later add-on.

## Wandering thoughts

- **Loss as constitutive refusal.** Drawing the boundary so perfect information is *out of scope* rather than a limit case you "handle carefully" is a methodological personality. It buys that no theorem can be trivialized by "but if the agent saw everything…". Feels related to how ACA refuses upper-bound certification from below — same family of honesty about vantage.
- **God's-eye $H(\Omega_t \mid \mathcal{C}_t) > 0$.** The residual-uncertainty condition is *not* the agent's self-assessed uncertainty. A delusionally confident agent with true residual entropy is still in scope — and about to eat a mismatch. That split (modeler's predicate vs agent's $U_M$) is the engine; pedagogically it should be foregrounded early when teaching.
- **What is "internal state" at this stage?** The coupling names it, but state is still almost empty — not yet $M_t$, not yet $X_t$. The chronica is the only substance so far. Curious that identity-substance (chronica) arrives *before* epistemic substance (model). That's deliberate and strange relative to standard POMDP textbooks (which start with beliefs).
- **Pedagogy of the five:** environment boundary → close the action loop → formalize the lossy aperture → name the irreversible history → draw the open region. Each step makes the previous non-decorative. Active perception's $a_{t-1}$ in $h$ is already promising pragmatic vs epistemic actions.

## Questions that open

1. Temporal quantifier on residual uncertainty: forever? generically? Does an agent that fully identifies a static world *exit* AAT into pure computation/control?
2. Computational irreducibility with perfect perceptual access — is that inside the information-loss boundary or a sibling case?
3. Boundary integrity: can $\Omega$ edit the agent's internal registers? (If yes, is it still a coupling?)
4. $M_0$ / phylogenetic prior — chronica as *only* raw material is strong empiricism; pretrained weights?
5. Passive-observer chronica without actions — is $\mathcal{C}_t$ just $(o_1, o_2, \ldots)$? Degenerate form not yet written.

No appendices interleaved this batch (no `deriv-*` first-references requiring them).
