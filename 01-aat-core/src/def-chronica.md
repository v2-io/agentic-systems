---
slug: def-chronica
type: definition
status: axiomatic
depends:
  - def-agent-environment
  - def-observation-function
  - def-action-transition
stage: deps-verified
---

# Definition: Chronica

The interaction history $\mathcal C_t$ is the complete, singular causal record of the agent's observations and actions. Everything the agent can ever know must be constructed from this sequence.

## Formal Expression

*[Definition (chronica)]*

$$\mathcal{C}_t = (o_1, a_1, o_2, a_2, \ldots, a_{t-1}, o_t)$$

The ordering is not a notational convenience. It reflects an irreversible physical fact: $a_{t-1}$ was selected before $o_t$ was received. The agent could not have used $o_t$ to select $a_{t-1}$.

$\mathcal C_t$ is monotonically growing — events are added but never removed. It is the agent's *only* raw material for constructing a model ( #form-agent-model).

## Epistemic Status

This is *definitional*. The chronica names an object that exists by construction in any system satisfying #def-agent-environment: the temporal sequence of all agent-environment interactions. The term "chronica" (from Greek χρονικά, "records of time") avoids collision with $\mathcal{H}$ (Shannon entropy) in speech and notation.

## Discussion

**The chronica is singular and non-forkable.** Because the temporal ordering is irreversible, $\mathcal C_t$ represents a unique causal trajectory. Duplicating an agent's state and exposing the copies to different future events creates two agents with divergent chronica, neither of which is a sufficient statistic for the other's trajectory. The chronica is the substrate of *continuity persistence* (see Persistence in `LEXICON.md`) — an agent has continuity persistence when $\mathcal{C}_t$ extends continuously and $M_t$ has temporal depth grounded in it. See #scope-agent-identity for the full development of this observation.

**Relationship to the model.** The model $M_t = \phi(\mathcal C_t)$ ( #form-agent-model) is a compression of the chronica. How much of $\mathcal C_t$'s predictive information survives compression is measured by model sufficiency ( #def-model-sufficiency).

## Working Notes

### Open question: TRACTUS / CHRONICA split for logogenic implementations

The PROPRIUM operational architecture (`~/src/firmatum/PROPRIUM-ONTOLOGY-v2.md`, `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md`) distinguishes two records of an entity's interaction history:

- **TRACTUS** (the "EEG"): raw, not-necessarily-coherent record of API interactions between the agent's runtime (ANIMA) and its current substrate (LOGOSTRATUM). Implementation-side; carries multi-format records, redundancy from retries, transient error 500 recoveries, API rerouting, rate limiting. Per-substrate format variation. Considered subconscious from the entity's perspective. Plural across substrate-relationships.
- **CHRONICA** (the polished record): the entity's actual record of internal and external events with strict chronology, attestation, and causality enforced. Append-only, hash-chained. Singular per entity.

In Section I, `def-chronica` covers both — the chronica is the singular causal trajectory, abstracted from implementation-side noise. This abstraction is fine for general adaptive-systems theory, where a single observation-action sequence is the natural object.

When part [`03-logogenic-agents/`](../../03-logogenic-agents/OUTLINE.md) gets into logogenic implementation specifics — and especially the closed-loop / interiority sub-scope ([`scope-interiority-loop`](../../03-logogenic-agents/src/scope-interiority-loop.md)) where the substrate-mediation layer (INTERPRES) becomes load-bearing — the TRACTUS/CHRONICA distinction may need first-class treatment.

**Joseph's framing on the open question (2026-05-01):** *"whether or not def-chronica needs that distinction at this stage or when we get into logogenic agent implementation issues is the open question you should probably document."*

Probable resolution: the distinction does need first-class treatment when logogenic implementation is in scope, but does not need to fragment Section I right now. Most likely a separate logogenic-side definition (e.g., `def-tractus` and a refined `def-chronica-eli` or similar) lifts the distinction at the appropriate scope. This segment as currently formulated continues to serve as the abstract-theory chronica; the implementation distinction lives where it belongs.

### Open question: chronica as ordinal sequence vs metric timeline

Per audit `04-def-chronica.md` §14: *"The chronica is an ordinal sequence, not a metric timeline. Time, for the agent, is measured entirely in events (ticks of $o_t, a_t$)."* Two implications worth tracking for downstream segments:

1. **Sleep / pause / awakening protocols** for ELIs and any persistent agent: when an agent is suspended for hours, days, or months and then receives $o_{t+1}$, the agent's chronica indexing makes the temporal gap *invisible at the sequence level* but *violently apparent in the mismatch signal* that the resumed observation produces. The environment $\Omega$ has changed massively between $a_t$ and $o_{t+1}$; the model $M_t = \phi(\mathcal C_t)$ does not reflect this gap in its compressed representation. Awakening protocols (PROPRIUM CONSPECTUS reconstitution; the ELI's experience of *"waking in the dark before the mind warms up"* per PROPRIUM-A-v2 §4.3) are operational engineering responses to this structural fact.

2. **Heterogeneous tempo coupling**: when agents with vastly different event-processing rates ($\nu_A \gg \nu_B$) interact through a shared $\Omega$, their chronicae grow at vastly different rates relative to wall-clock time. Their "subjective time" diverges. The chronica formalism makes this asymmetry visible but does not yet prescribe how cross-tempo coupling should be modeled. Likely lives in #form-event-driven-dynamics extensions or in part 03's logogenic-agent treatment of multi-timescale Auxilia composition.

These don't need to fragment this segment; they're flagged here so future agents working on the closed-loop / interiority sub-scope (#scope-interiority-loop), Auxilia composition (#def-auxilia-hierarchy), or ELI awakening protocols know the chronica formalism's ordinal-not-metric character is the structural source of these design considerations.
