Please conduct a deep prior-art search across academic literature. We are establishing scientific precedence for a theoretical framework of agency (AAT).

## The Core Idea / Claim
An agent that revises its own objective endogenously (a *self-actuator*) faces a structural problem: an *unconstrained* revision operator drives the satisfaction gap to zero by *moving the target onto the arrow already in flight* — the formal shadow of wireheading, reward corruption, and Goodhart's Law. Non-degeneracy requires a terminal invariant preserved across the revision. The framework derives a *conditional, scoped no-go*: no invariant satisfying four named requirements (value-functional-typed, non-vacuously monotone across revision, agent-internal and itself self-actuatable, convention- and trajectory-stable) can be constructed from objective-side machinery alone. **The grounding of any non-degenerate self-actuator must live on the adaptive substrate — a *non-objective***. The persistence condition (a property of the correction dynamics, not of any objective) supplies the canonical instance. The result derives an orthogonality: an agent's continuity stance is the *choice of terminal non-objective invariant* the self-actuation operator structurally cannot reach — the intuitive expectation that an agent able to revise its own objectives can thereby revise its valuation of continuity is *inverted*.

## Boundaries of the Claim
- Domain: AI safety (corrigibility, reward hacking, mesa-optimization), preference learning, value alignment, embedded agency.
- Assumptions: agents with self-revisable objectives operating under the framework's scope (scalar value functional on trajectories; no primitive reflective oracle).
- Note the *constructive* content: the framework treats the no-go as forcing the structural conclusion that grounding must live off the objective layer, not as a discouraging result.

## What Kind of Match Counts
- Formal treatments of why a self-modifying agent *cannot* ground its own objective revision on objectives alone.
- Structural arguments that wireheading / reward corruption / Goodhart's Law follow from an *unconstrained* objective-revision operator.
- Derivations of constraints on objective-update operators that prevent degenerate revision (the "move the target onto the arrow" failure mode).
- "Stable preference" axiom systems and their structural consequences for self-modifying agents.
- Arguments that the grounding of self-actuation must live *outside* the objective space — on a non-objective substrate.
- Corrigibility / safe-interruption literature insofar as it formalizes constraints on objective revision.
- Orthogonality arguments between objective-revision capacity and continuity-valuation.

## What Would NOT Count
- Heuristic "preference learning" methods that don't address the grounding problem structurally.
- General reward-hacking case studies without formal characterization of *why* an unconstrained revision operator collapses.
- AI-safety surveys without specific structural theorems on the grounding problem.

## Known Anchors
- Soares & Fallenstein 2014 (corrigibility, MIRI)
- Everitt, Hutter et al. (reward tampering, current-RF optimization)
- Hubinger, van Merwijk, Mikulik, Skalse & Garrabrant 2019 (mesa-optimizers, deceptive alignment)
- Demski & Garrabrant 2019 (embedded agency)
- Orseau & Armstrong 2016 (safe interruption)
- Russell 2019 (assistance games / CIRL)
- Bostrom 2014 (value lock-in, instrumental convergence)
- Goodhart 1975 / Campbell 1979 / Manheim & Garrabrant 2018 (Goodhart's Law variants)
- Christiano et al. (RLHF; partial connection on grounding)
- Yudkowsky (utility-indifference, reflective stability)

## Search Scope
- Strong focus on AI-safety / embedded-agency literature for the wireheading-grounding family.
- Adjacent: decision-theoretic treatments of preference stability, evolutionary stability of utility functions, Parfit-style identity over revision.
- Strictly academic papers (no patents/IP).
