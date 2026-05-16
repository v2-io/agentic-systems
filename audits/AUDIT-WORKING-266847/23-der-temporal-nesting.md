# Reflection: der-temporal-nesting

## What the segment does

Derives the temporal nesting constraint: adjacent adaptive timescales must satisfy ν_(n+1) ≪ ν_n, and the faster level must approximately converge before the slower level acts. This is singular perturbation reasoning (Tikhonov 1952; Khalil 2002, Chapter 11).

The five-level table (reactive / parametric / consolidation / structural / architectural) is illustrative rather than exhaustive. The key claim is structural: slower processes must operate on quasi-steady-state output of faster ones, not transients.

## Naming targets surfaced

Looking for "temporal nesting" in the tracker...

The tracker will have an entry for "temporal nesting" as the segment name. The tracker should also surface "temporal stratification" and similar candidates.

The Discussion mentions "consolidation dynamics" (#form-consolidation-dynamics) as an intermediate timescale process. This is a reference to a segment I haven't read yet — consolidation dynamics is the redistribution of information within M_t's sub-state factorization toward the IB optimum.

## The singular perturbation connection

The epistemic status is honest: this is standard Tikhonov singular perturbation reasoning, not novel to AAD. The contribution is the *application* and *interpretation* in the adaptive-systems context: connecting the timescale hierarchy to the structural-adaptation result (conservatism toward structural change is a consequence of temporal nesting, not just inertia) and the deliberation-cost result.

The cross-reference to #der-deliberation-cost is precisely right: deliberation is a pause in the fastest-level process, and the cost is the mismatch accumulated during the pause. The same reasoning applies to structural adaptation but with a massive Δτ.

## The violation symptoms

"Micromanagement" as a violation of temporal nesting is a clean practical example. Strategic decisions at operational tempo (before operational adaptation has converged) produce oscillation — the strategic layer is updating based on transients in the operational layer. The Boyd connection is exact: OODA loop tempo hierarchy maps directly to the timescale table.

## Naming considerations

"Temporal nesting" is precise. The alternative would be "timescale stratification" (which is how the OUTLINE describes it: "Timescale stratification"). These are nearly synonymous — "nesting" emphasizes the hierarchical containment structure; "stratification" emphasizes the distinct layers. "Nesting" is slightly more evocative (each level contains the output of all faster levels), "stratification" is slightly more visually concrete.

## Cross-connect to consolidation

The consolidation level (intermediate timescale) references #form-consolidation-dynamics which I haven't read. This is the redistribution toward IB-optimum — the information-bottleneck principle applies not just to model class selection but to how information is organized within the model class at the consolidation timescale. This is the sleep/consolidation parallel from biology (memory consolidation operates at a slower timescale than online learning).

## The open problem flag

"Making this rigorous for AAD requires specifying dynamics at deeper adaptive levels — an open problem." This is honest. The multi-timescale stability result requires full compositional dynamics at each level, which isn't yet derived within AAD. The sketch segment (#sketch-multi-timescale-stability) carries the placeholder.

How valuable: 6/10 for surprise (the consolidation level as distinct from parametric is non-obvious; the singular perturbation grounding is important), 7/10 for load-bearing (nesting structure is a key organizational concept for Sections II and III).
