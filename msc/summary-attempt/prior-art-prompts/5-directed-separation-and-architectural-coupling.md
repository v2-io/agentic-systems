Please conduct a deep prior-art search across academic literature. We are establishing scientific precedence for a theoretical framework of agency (AAT).

## The Core Idea / Claim
Agent architectures can be categorized by "Directed Separation." Class 1 architectures (e.g., Kalman + LQR) strictly separate their belief updates (epistemic state) from their goals (purposeful state). Class 3 architectures (e.g., LLMs, end-to-end RL) entangle goals and observations. Furthermore, Class 3 systems can be coerced into Class 1 by enclosing them in an external scaffold that strictly segregates belief-queries from goal-queries, achieving modularity at the cost of execution tempo (a cognitive analog to Brooks's Law).

## Boundaries of the Claim
- Domain: AI safety, cognitive architectures, systems engineering for ML, active inference.
- Assumptions: The distinction between "what is true" (epistemic) and "what is desired" (teleological) in agent state.

## What Kind of Match Counts
- Architectural taxonomies that formally categorize AI based on the causal separation vs entanglement of perception and goal-seeking.
- Discussions of "Friston blankets" vs "Pearl blankets" (e.g., Bruineberg) specifically regarding goal-entangled perception.
- Theoretical treatments of "Scaffolding" or "Wrapping" end-to-end models (like LLMs) to enforce strict separation of concerns (belief vs planning).
- Analyses of the tempo/speed trade-off when modularizing entangled cognitive systems.

## What Would NOT Count
- Generic software engineering modularity papers that do not specifically address the epistemic vs teleological divide in AI agents.
- Standard active inference papers that take entangled perception as a given, without comparing it to strictly separated architectures or discussing scaffolding.

## Known Anchors
- Bruineberg et al. (Friston vs Pearl blankets)
- Cognitive Architectures (SOAR, ACT-R) vs End-to-End RL
- LLM Scaffolding / Agentic Wrappers

## Search Scope
- Broad conceptual precursors and recent AI architectural taxonomies.
- Strictly academic papers (no patents/IP).