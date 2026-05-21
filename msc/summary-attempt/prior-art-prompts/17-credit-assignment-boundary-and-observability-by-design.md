Please conduct a deep prior-art search across academic literature. We are establishing scientific precedence for a theoretical framework of agency (AAT).

## The Core Idea / Claim
Strategy revision requires assigning credit for observed outcomes to specific edges in the strategy DAG — "the plan partially worked; which step failed, which was irrelevant, which succeeded?" The framework characterizes the *boundary* between tractable and intractable cases via three independent barriers: (1) **computational intractability**: exact per-edge attribution in general AND/OR DAGs is #P-hard via reduction to Shapley-value computation for weighted voting games (Deng & Papadimitriou 1994); (2) **information-theoretic underdetermination**: when intermediates are unobservable, the identifiable subspace's dimension is bounded by the number of observable nodes, and per-edge attribution is *underdetermined* (not just hard) when fewer observable nodes exist than edges; (3) **posterior correlation barrier**: any factored representation (independent per-edge posteriors) necessarily discards the correlation introduced by failure at multi-parent nodes — the factored representation is an approximation by construction. Despite these barriers, the framework shows that **persistence does not require credit assignment**: the sector condition transfers from per-edge credence space to plan-confidence error via the Jacobian, credit-assignment-free. *Directional fidelity* is the minimal requirement on any credit-assignment scheme. Organizationally, the framework names **OKRs as observability-by-design**: the OKR discipline converts deep partially-unobservable strategy DAGs into ones with explicit observable intermediate nodes (Key Results), making credit assignment between actions and objectives *componentwise rather than intractable*. Common OKR failure modes (vanity metrics, too many Key Results, lagging indicators, Goodhart's Law) map to specific framework predictions about when the strategy machinery would fail.

## Boundaries of the Claim
- Domain: reinforcement learning (temporal credit assignment), reliability engineering, computational complexity, decision theory under partial observability, organizational design (OKR / Mission-by-Objectives).
- Focus: the *boundary* between tractable and intractable cases of credit assignment, the *minimal requirement* for persistence guarantees, and the *observability-by-design* organizational instantiation.

## What Kind of Match Counts
- Formal complexity-theoretic results on credit-assignment / contribution-attribution in compositional decision structures (Shapley-value #P-hardness; reductions from weighted voting games to AND/OR networks).
- Persistence / stability results that *do not* require credit assignment (transfer arguments via Jacobian or analogous machinery).
- Information-theoretic underdetermination treatments of attribution in partially-observable settings (identifiable subspace bounded by observable-node count).
- Organizational design literature formalizing OKR-style observability-by-design with rigorous tractability arguments.
- RL temporal credit assignment literature with explicit attention to compositional intractability.
- Three-barriers arguments (computational + information-theoretic + posterior-correlation) for why exact credit assignment is structurally hard.

## What Would NOT Count
- Standard TD-learning / eligibility-trace papers without complexity analysis.
- Shapley-value applications to feature attribution in ML interpretability without the agent-credit-assignment framing.
- General OKR / management-by-objectives literature without observability-by-design formalization.
- "Credit assignment" papers that propose specific schemes without characterizing the boundary of what is achievable.

## Known Anchors
- Deng & Papadimitriou 1994 (Shapley-value #P-completeness for weighted voting)
- Sutton 1988 (TD-learning, temporal credit assignment)
- Watkins (Q-learning, credit assignment in RL)
- Lundberg & Lee 2017 (SHAP, Shapley for ML attribution — adjacent)
- Pearl (causal credit assignment via interventions)
- Drucker 1954 (Management by Objectives — historical OKR antecedent)
- Doerr 2018 (Measure What Matters — modern OKR; more practitioner)
- Conway 1968 (Conway's Law, organizational-decomposition principle)
- Williams 1992 (REINFORCE; policy gradients as one credit-assignment scheme)
- Mnih et al. 2015 (DQN; deep RL credit assignment via experience replay)

## Search Scope
- Both close mathematical matches (complexity of credit assignment in compositional structures) and conceptual precursors (organizational observability-by-design).
- Strictly academic papers (no patents/IP).
