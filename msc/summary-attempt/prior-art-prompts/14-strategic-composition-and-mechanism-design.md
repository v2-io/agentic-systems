Please conduct a deep prior-art search across academic literature. We are establishing scientific precedence for a theoretical framework of agency (AAT).

## The Core Idea / Claim
When sub-agents are individually *Class-1 Separated* (belief updates structurally independent of goals) but pursue *partially-opposing* objectives, the composite is necessarily *Class-3 Coupled* — **the architectural classification is not preserved under composition with goal divergence**. The framework lifts contraction analysis to equilibrium machinery via potential games (Monderer-Shapley 1996) and monotone games (Rosen 1965): under these conditions, the sector-persistence template transfers to the gradient of the joint potential, with AAT's persistence machinery recovering at the equilibrium layer (sub-scope α'). Outside this sub-scope (non-potential non-monotone games), only set-convergence to coarse correlated equilibria is available (Hart-Mas-Colell 2000 under no-regret dynamics, sub-scope β'). The result has consequential structure: **modular safety architectures fail by construction under goal divergence** between safety modules and the central planner — the composite acquires Class-3 dynamics regardless of each component's nominal modularity. Mechanism-design impossibility (Gibbard-Satterthwaite, Myerson-Satterthwaite, Arrow) is flagged as a candidate identifiability-floor instance — the equilibrium-selection layer requires structural priors that local data cannot supply.

## Boundaries of the Claim
- Domain: game theory, multi-agent reinforcement learning, mechanism design, AI safety (modular architectures, mesa-optimization), control theory (contraction analysis).
- Focus: the *bridge* from contraction analysis to equilibrium analysis when goals diverge across sub-agents, and the inheritance of architectural class under composition.

## What Kind of Match Counts
- Bridges from contraction analysis / Lyapunov stability to equilibrium analysis for multi-agent strategic dynamics.
- Potential-game / monotone-game derivations of stability for goal-divergent interaction with explicit sector-condition-style structure.
- Formal arguments that Class-1 modular components compose to Class-3 entangled systems under partial opposition (the architectural-class-inheritance result).
- Structural treatments of why "modular safety with central planner" fails under goal divergence between modules and planner (mesa-optimization framed structurally).
- Mechanism-design impossibility results re-framed as identifiability-floor-style no-gos with named escapes via specific machinery.
- Last-iterate vs time-average convergence distinctions in non-zero-sum games with explicit decision-theoretic consequences.
- Three-obstructions arguments to contraction analysis in strategic regimes (saddle-point fixed points / passivity universality failure / Daskalakis-style last-iterate non-convergence).

## What Would NOT Count
- Standard Nash equilibrium existence theorems without the contraction-to-equilibrium lift.
- General MARL papers on partial cooperation without the architectural-class-inheritance angle.
- Mechanism-design impossibility papers that establish impossibility without naming structural escapes via specific machinery.
- Single-tradition (game theory only or control theory only) papers — the framework's contribution is the bridge.

## Known Anchors
- Monderer & Shapley 1996 (potential games)
- Rosen 1965 (concave games, monotone dynamics)
- Hart & Mas-Colell 2000 (no-regret dynamics → CCE)
- Daskalakis, Ilyas, Syrgkanis, Zampetakis 2018 (last-iterate non-convergence)
- Slotine 2003 / Lohmiller & Slotine 1998 (contraction analysis, composition)
- Gibbard 1973 / Satterthwaite 1975 (mechanism-design impossibility)
- Myerson & Satterthwaite 1983 (efficient bilateral trade impossibility)
- Arrow 1951 (impossibility for dictator-free social welfare aggregation)
- Hubinger et al. 2019 (mesa-optimizers within modular systems)
- Foster & Vohra (calibrated learning and equilibrium)

## Search Scope
- Close mathematical matches (contraction-to-equilibrium bridges) and the broader mechanism-design-impossibility-as-identifiability-floor framing.
- Strictly academic papers (no patents/IP).
