Please conduct a deep prior-art search across academic literature. We are establishing scientific precedence for a theoretical framework of agency (AAT).

## The Core Idea / Claim
Agent survival is modeled as a dynamical systems problem using Lyapunov stability. Rather than linear correction, the agent's mechanism is bounded by a "sector condition" (efficiency alpha). An agent persists only if its correction rate exceeds the environmental drift divided by its reserve. Crucially, tracking error scales differently based on the environment: mismatch scales as 1/alpha against deterministic drift, but 1/sqrt(alpha) against stochastic noise. Maintaining persistence against noise requires sustained Shannon information acquisition at a strict minimum rate (an information rate floor).

## Boundaries of the Claim
- Domain: Nonlinear control theory, robust control, cybernetics, information-theoretic control.
- Assumptions: Agents operating in environments with persistent external disturbances (drift or noise).

## What Kind of Match Counts
- Application of the Lure problem/sector conditions/absolute stability directly to cognitive mismatch, learning updates, or agent viability.
- Inequalities bounding tracking error/viability against environmental drift (persistence bounds).
- Papers proving the specific 1/rate (deterministic) vs 1/sqrt(rate) (stochastic) tracking error scaling dichotomy in agents/control systems.
- Proofs of a strict minimum Shannon channel capacity required for bounded tracking error (Bode integral extensions to RL).

## What Would NOT Count
- Standard Lyapunov stability of physical/mechanical systems without an information or learning component.
- Basic regret bounds in bandit problems or stationary RL (must address tracking a non-stationary/drifting environment).

## Known Anchors
- Mitter-Newton bounds
- Bode integral theorem extensions
- Viability Theory (Aubin)
- Lurie problem / Sector Conditions

## Search Scope
- Looking for close mathematical implementations and formal proofs of these bounds.
- Strictly academic papers (no patents/IP).