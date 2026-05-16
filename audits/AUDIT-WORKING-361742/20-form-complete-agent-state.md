# Reflection: form-complete-agent-state

**Segment:** `#form-complete-agent-state`

## What this does

Lifts the agent state from M_t alone to X_t = (M_t, G_t), separating epistemic content from purposeful content. Three motivations for the separation:
1. Backward compatibility (Section I machinery unchanged)
2. Different dynamics (epistemic and purposeful have distinct update sources/timescales)
3. Directed separation stateability (can only claim f_M is G_t-independent if the components are separated)

Action couples both: a_t = π(M_t, G_t). The policy is the single interaction point.

## Naming relevance

Row for "complete agent state" — this formulation names X_t. Let me check what alternatives exist.

"Complete agent state" is the right name: "complete" signals that X_t captures everything (epistemic + purposeful), unlike M_t alone. "Agent state" names what it is. The name pairs correctly with the prior "form-agent-model" (which defined M_t as the complete state in Section I scope) — X_t is the Section II extension.

## New naming targets surfaced

**Epistemic substate**: M_t's role within X_t. Named in the segment.

**Purposeful substate**: G_t's role within X_t. Named.

**Policy coupling**: The policy a_t = π(M_t, G_t) as the single point where epistemic and purposeful states interact. Named observation.

## What's excellent here

The backward compatibility argument is architecturally important: Section I machinery applies to M_t unchanged. The lift adds structure ALONGSIDE M_t, not within it. This prevents the pattern where extending a theory requires revising everything that came before.

The conjecture about alternative decompositions being structurally isomorphic to (M_t, G_t) is correctly labeled as a plausible structural claim, not a proof. The directed separation gives a canonical factorization — but alternatives that cross-cut the epistemic/purposeful boundary might be useful in practice while not being isomorphic.
