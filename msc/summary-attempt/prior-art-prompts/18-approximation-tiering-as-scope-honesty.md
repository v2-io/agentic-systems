Please conduct a deep prior-art search across academic literature. We are establishing scientific precedence for a theoretical framework of agency (AAT).

## The Core Idea / Claim
The framework uses a recurring meta-pattern for handling intractability: introduce a *tiered hierarchy of approximations* with **proved monotonicity** between tiers and an explicit **diagnostic for ascending** when the current tier becomes binding. A successful tiering has four components: (1) a tractable baseline tier that gives meaningful results under stated scope; (2) a monotonicity result — ascending the hierarchy gives strictly stronger guarantees; (3) a diagnostic that tells the agent or analyst *when* the current tier is binding (when ascending would change the conclusion); (4) explicit cost accounting for ascending. Three such hierarchies exist in the framework: the **Correlation Hierarchy** (L0 independence baseline / L1 augmented DAG with strict-prerequisite common-cause nodes / L1' mixture form for soft facilitators with the Cramér-Rao floor under unobservable common cause / L2 full joint correlation, exponential) for causal structure in strategy DAGs; the **Convention Hierarchy** (C1 one-step improvement / C2 receding-horizon / C3 Bellman) for continuation policies in the value object, with a proved monotonicity result on the satisfaction-gap quantity; the **Tier 1/2/3 contraction taxonomy** in the composition-closure framework (Tier 1 exact contraction on class / Tier 2 local with bounded degradation / Tier 3 per-domain verification). The framework's posture: tiered approximation is what makes scope-honesty *operational* rather than merely rhetorical — a flat "this result holds under these conditions" leaves the user without a path forward; a tiered approximation says "this result holds at this tier; here is the diagnostic for whether you need to ascend; here is what ascending costs and buys."

## Boundaries of the Claim
- Domain: approximate dynamic programming, hierarchical Bayesian inference, causal inference under partial identifiability, control theory under tiered guarantees, scope-honesty methodology.
- Focus: the *methodological commitment* to tiered approximation as a scope-honesty toolkit rather than any single tiered approximation in isolation.

## What Kind of Match Counts
- Frameworks with explicit tiered approximation hierarchies plus monotonicity-between-tiers results plus diagnostic signals for ascending.
- Cheap-baseline-plus-known-repair-path as a scope-honesty methodology applied across multiple distinct inference problems within one framework.
- Multi-tier structures spanning causal inference, decision theory, control theory, or composition (across-layer rather than within-layer).
- Treatments of approximation hierarchies that explicitly state what *each tier* costs and what it buys.

## What Would NOT Count
- Single-tier approximations without ascension paths.
- Quality hierarchies without diagnostics for when the current tier is binding.
- "Just use a richer model" arguments without explicit monotonicity guarantees.
- PAC-Bayes-style bounds without the operational tiering pattern.

## Known Anchors
- Pearl's Correlation Hierarchy / interventional vs counterfactual identifiability tiers
- Receding-Horizon Control / Model Predictive Control (Mayne et al.)
- Approximate dynamic programming tiers (Powell, Bertsekas)
- PAC-MDP and approximation grades (Strehl, Littman et al.)
- Bareinboim et al. on identifiability under unobserved confounders
- Tishby's Information Bottleneck tiering
- Subramanian et al. (approximate information states with bounded loss)

## Search Scope
- Both methodological work on tiered scope-honesty AND specific frameworks that apply the pattern across multiple inference problems.
- Strictly academic papers (no patents/IP).
