# 73 - scope-composite-agent

Source: `01-aat-core/src/scope-composite-agent.md`

## First-pass understanding

This segment narrows multi-agent systems to composite agents. The central idea is that closure, composite tempo, and team-persistence quantities should only be computed when there is a coherent composite-level target: a shared objective, a parent objective decomposed into sub-objectives, a mutual-benefit alignment, or a strategic equilibrium macro-state.

The strongest clarifying move is the disjunctive form. The segment explicitly refuses to collapse all routes into one scalar threshold, and it distinguishes alignment composites from strategic composites. The risk is that the prose still often describes composite status as if it always means a shared `O_c`, while route C-iv deliberately admits systems whose macro-state is an equilibrium structure instead.

## Diagram attempt

I drew the segment as a gate from multi-agent scope into four separate routes, with a split output: C-i through C-iii yield an objective-based composite, while C-iv yields an equilibrium-based strategic composite. The diagram keeps the two target types visually separate because later machinery must know which object it is computing over.

## Findings and watches

- F97 candidate: the segment repeatedly grounds composite-agent status in a well-defined composite objective `O_c`, but route C-iv explicitly requires no shared objective and defines the macro-state relative to an equilibrium structure `E`. The scope condition should either generalize `G_c` beyond `(O_c, Sigma_c)` or keep strategic composites under a distinct non-`O_c` composition interface.
- F98 candidate: C-iv risks over-admitting ordinary finite games as composite agents. Because mixed Nash and CCE existence/convergence are widely available under broad dynamics, the failure class becomes very small, and "composite agent" can collapse into "multi-agent system with reachable equilibrium support." The segment needs an additional reason why equilibrium support is enough to define composite quantities, not just game-theoretic behavior.
- F99 candidate: C-iii's mutual-benefit route uses a relevance variable `Y` with `E[Y | joint] > E[Y | non-coop]` for each sub-agent, but `Y` is not linked to each agent's objective, utility, or participation constraint. A common variable increasing is not enough for mutual benefit unless it is valued by each agent or mapped into each `O_i`.
- F100 soft candidate: C-i depends on an "appropriate policy divergence" and epsilon-compatibility with `O_c`-optimal policies. Because optimal policies may be nonunique and policy divergence can be behaviorally or distributionally defined, the route should specify the equivalence class or occupancy measure over which compatibility is judged.
- F101 candidate: this scope segment imports several future proof or framework homes (`def-unity-dimensions`, `result-unity-closure-mapping`, `deriv-strategic-composition`, `disc-identifiability-floor`, `hyp-symbiogenic-composition`) while declaring only three dependencies. That is acceptable for discussion, but those references should not be treated as locally verified support.
- Watch: the disjunctive route design is probably the right architecture. Later Section III results need to say whether they apply to alignment composites, strategic composites, or both.

## Local verdict

The scope restriction is an important guardrail against computing composite-agent quantities for arbitrary groups. The main fix is to keep objective-based composition and equilibrium-based composition typed separately so the formal state and downstream guarantees do not silently switch targets.
