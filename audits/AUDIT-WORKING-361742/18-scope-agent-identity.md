# Reflection: scope-agent-identity

**Segment:** `#scope-agent-identity`

## What this does

Scope commitment: AAD applies to agents on singular, non-forkable causal trajectories. Identity is grounded in the unique causal trajectory 𝒞_t (cannot be copied) not the model state M_t (can be copied).

Three consequences:
1. Sufficiency is trajectory-indexed (S(M_t) relative to THIS agent's 𝒞_t)
2. Model merging is lossy by construction (no optimal reconciliation of divergent histories)
3. Loop's interventional access depends on trajectory singularity (not architectural property)

Parameterization-invariance (PI) as natural companion axiom: AAD's conclusions should not depend on arbitrary choice of coordinates on M_t. Combined with Čencov 1982, this forces Fisher metric on statistical manifold sub-cases — converts Fisher-metric derivations from imported to AAD-internally-forced.

## Naming relevance

Row for "agent identity" — this is a scope segment, not a definition. The naming question is whether "agent identity" is the right name for what the segment establishes.

"Scope: agent identity as singular causal trajectory" is the segment title. The subject-noun is "agent identity" with the qualifier "as singular causal trajectory." This is a scope statement, not a definition of identity. The slug `scope-agent-identity` follows the type-prefix discipline.

What's the naming target? The CONCEPT being scoped is "agent identity" — the sense in which AAD recognizes agents as individuated. Whether the tracker has a row for this...

## New naming targets surfaced

**Clone problem**: Named Discussion section. The scenario of copying M_t and the formal consequences.

**Parameterization invariance (PI)**: Named axiom companion. Whether in the tracker...

**Continuity persistence**: This is the third sense of persistence (structural/operational/continuity). Segment explicitly connects to LEXICON. Row 554 in tracker (continuity persistence) — should vote on this.

**Token/type distinction**: Agents as tokens (singular trajectories) vs. types (equivalence classes like "the GPT-4 model"). This is architecturally important.

## What's excellent here

The clone problem is precisely stated: "At the moment of duplication, both copies are identical. But the very next event... creates two divergent, irreversible causal trajectories." This is not philosophical hand-waving — it's a formal consequence of trajectory-indexed sufficiency.

The logogenic-agent connection is important: 100% context turnover is a special case of this scope condition. Each AI session starts a new causal trajectory. External memory (CLAUDE.md) transfers a *summary* of previous trajectories' models, not the trajectories themselves. This is not a deficiency but a structural feature.

The PI axiom discussion connects to the additive-coordinate-forcing meta-segment (#disc-additive-coordinate-forcing) — PI plus Čencov becomes the fourth instance of the "AAD-internal axiom + uniqueness theorem = forced coordinate" pattern.
