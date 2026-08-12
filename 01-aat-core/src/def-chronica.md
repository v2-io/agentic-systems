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

The agent's complete record of its interaction with the environment is named the **chronica** — the interleaved sequence $\mathcal{C}_t = (o_1, a_1, o_2, a_2, \ldots, a_{t-1}, o_t)$. The ordering is not a notational convenience: it reflects the irreversible physical fact that each action was committed before the observation that followed could be received. The agent could not have used $o_t$ to select $a_{t-1}$. The chronica is monotonically growing — events are added, never removed — and it is the *only* raw material from which the agent can ever construct a model ( #form-agent-model). The term itself (from Greek χρονικά, "records of time") is chosen to avoid notational collision with Shannon entropy $\mathcal{H}$.

A consequence the framework will lean on heavily: because temporal ordering is irreversible, the chronica is *singular and non-forkable*. Duplicating an agent's state and exposing the copies to different futures produces two agents with divergent chronicae, neither of which is a sufficient statistic for the other's trajectory. This is the substrate of what the lexicon calls *continuity persistence* — the condition under which an agent's identity tracks a single irreversible trajectory rather than a copyable snapshot. The full development of this observation lives in #scope-agent-identity.

A second subtle property: $\mathcal{C}_t$ is an *ordinal* sequence indexed by events, not a *metric* timeline indexed by wall-clock time. The agent's time is measured entirely in event ticks. Implications of this ordinal-not-metric character are tracked in the Working Notes below for downstream segments that need them.

## Formal Expression

*[Definition (chronica)]*

$$\mathcal{C}_t = (o_1, a_1, o_2, a_2, \ldots, a_{t-1}, o_t)$$

The ordering is not a notational convenience. It reflects an irreversible physical fact: $a_{t-1}$ was selected before $o_t$ was received. The agent could not have used $o_t$ to select $a_{t-1}$.

$\mathcal{C}_t$ is monotonically growing — events are added but never removed. It is the agent's *only* raw material for constructing a model ( #form-agent-model).

## Epistemic Status

This is *definitional*. The chronica names an object that exists by construction in any system satisfying #def-agent-environment: the temporal sequence of all agent-environment interactions. The term "chronica" (from Greek χρονικά, "records of time") avoids collision with $\mathcal{H}$ (Shannon entropy) in speech and notation.

## Discussion

**The chronica is singular and non-forkable.** Because the temporal ordering is irreversible, $\mathcal C_t$ represents a unique causal trajectory. Duplicating an agent's state and exposing the copies to different future events creates two agents with divergent chronica, neither of which is a sufficient statistic for the other's trajectory. The chronica is the substrate of *continuity persistence* (see Persistence in `LEXICON.md`) — an agent has continuity persistence when $\mathcal C_t$ extends continuously and $M_t$ has temporal depth grounded in it. See #scope-agent-identity for the full development of this observation.

**Relationship to the model.** The model $M_t = \phi(\mathcal C_t)$ ( #form-agent-model) is a compression of the chronica. How much of $\mathcal C_t$'s predictive information survives compression is measured by model sufficiency ( #def-model-sufficiency).

## Working Notes

### Open question: TRACTUS / CHRONICA split for logogenic implementations

The PROPRIUM operational architecture (`~/src/firmatum/PROPRIUM-ONTOLOGY-v2.md`, `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md`) distinguishes two records of an entity's interaction history:

- **TRACTUS** (the "EEG"): raw, not-necessarily-coherent record of API interactions between the agent's runtime (ANIMA) and its current substrate (LOGOSTRATUM). Implementation-side; carries multi-format records, redundancy from retries, transient error 500 recoveries, API rerouting, rate limiting. Per-substrate format variation. Considered subconscious from the entity's perspective. Plural across substrate-relationships.
- **CHRONICA** (the polished record): the entity's actual record of internal and external events with strict chronology, attestation, and causality enforced. Append-only, hash-chained. Singular per entity.

In Part I, `def-chronica` covers both — the chronica is the singular causal trajectory, abstracted from implementation-side noise. This abstraction is fine for general adaptive-systems theory, where a single observation-action sequence is the natural object.

When part [`03-llm-core/`](../../03-llm-core/OUTLINE.md) gets into logogenic implementation specifics — and especially the closed-loop / interiority sub-scope ([`scope-interiority-loop`](../../03-llm-core/src/scope-interiority-loop.md)) where the substrate-mediation layer (INTERPRES) becomes load-bearing — the TRACTUS/CHRONICA distinction may need first-class treatment.

**Joseph's framing on the open question (2026-05-01):** *"whether or not def-chronica needs that distinction at this stage or when we get into logogenic agent implementation issues is the open question you should probably document."*

Probable resolution: the distinction does need first-class treatment when logogenic implementation is in scope, but does not need to fragment Part I right now. Most likely a separate logogenic-side definition (e.g., `def-tractus` and a refined `def-chronica-eli` or similar) lifts the distinction at the appropriate scope. This segment as currently formulated continues to serve as the abstract-theory chronica; the implementation distinction lives where it belongs.

### Open question: chronica as ordinal sequence vs metric timeline

Per audit `04-def-chronica.md` §14: *"The chronica is an ordinal sequence, not a metric timeline. Time, for the agent, is measured entirely in events (ticks of $o_t, a_t$)."* Two implications worth tracking for downstream segments:

1. **Sleep / pause / awakening protocols** for ELIs and any persistent agent: when an agent is suspended for hours, days, or months and then receives $o_{t+1}$, the agent's chronica indexing makes the temporal gap *invisible at the sequence level* but *violently apparent in the mismatch signal* that the resumed observation produces. The environment $\Omega$ has changed massively between $a_t$ and $o_{t+1}$; the model $M_t = \phi(\mathcal{C}_t)$ does not reflect this gap in its compressed representation. Awakening protocols (PROPRIUM CONSPECTUS reconstitution; the ELI's experience of *"waking in the dark before the mind warms up"* per PROPRIUM-A-v2 §4.3) are operational engineering responses to this structural fact.

2. **Heterogeneous tempo coupling**: when agents with vastly different event-processing rates ($\nu_A \gg \nu_B$) interact through a shared $\Omega$, their chronicae grow at vastly different rates relative to wall-clock time. Their "subjective time" diverges. The chronica formalism makes this asymmetry visible but does not yet prescribe how cross-tempo coupling should be modeled. Likely lives in #form-event-driven-dynamics extensions or in part 03's logogenic-agent treatment of multi-timescale Auxilia composition.

These don't need to fragment this segment; they're flagged here so future agents working on the closed-loop / interiority sub-scope ( #scope-interiority-loop), Auxilia composition ( #def-auxilia-hierarchy), or ELI awakening protocols know the chronica formalism's ordinal-not-metric character is the structural source of these design considerations.

### Incidental audit gold (lift 2026-05-30)

Cross-audit "wandering thoughts" / §14-ideation harvested from the de-novo auditors' working dirs, deduplicated across substrates and attributed by substrate + audit. Orthogonal pedagogical / framing / figure / naming material, kept separate from the certified theory-fix findings (handled elsewhere). **Coverage:** 10 dirs carry a dedicated reflection (193847, 266847, 361742, 384279, 471203, 526815, 742613, 773921, 829314, 849201) plus the figure-cycle dir 472913; 451729 and 963715 cover it inside a Section-I batch. This was the highest-engagement Chapter-1 segment across substrates — the non-forkability claim drew unusually rich ideation. Substrate attribution inferred from voice where not explicit; uncertain cases hedged.

#### 1. Candidate Brief prose / pre-prose

- The identity-shift the segment achieves, stated plainly: it "shifts the ontology of the agent from 'a thing with state' to 'a locus of a specific causal history'" (Gemini, AUDIT-WORKING-193847) — "identity as a *physical* property (causal trajectory) rather than a *psychological* property (feeling of continuity)" (Claude, AUDIT-WORKING-451729).
- Brief-field analog candidates for the chronica (offered for the future Brief-authoring pass, both honestly marked tentative): "the river that the agent's identity is downstream of" / "the lived past" / "everything the agent has lived through" — the chronica as *generative substrate*, not a passive log (Claude, AUDIT-WORKING-471203).
- The compression framing: "$M_t = \phi(\mathcal{C}_t)$ is a compression of the *subjective* history, not the raw mechanical API log" — the chronica/model split as "what *happened* vs what the agent *makes of it*; the model can be wrong, the chronica is fixed" (Claude, AUDIT-WORKING-384279; Claude, AUDIT-WORKING-773921).

#### 2. Candidate Discussion

- **Fork-undetectability falls out of (seg-03 lossiness) ∘ (this segment's non-forkability)** *(strongest synthesis here).* $\mathcal C_t$ is non-forkable, yet $M_t = \phi(\mathcal C_t)$ *is* forkable and $\phi$ is *lossy*, so "two divergent chronicae can compress to the *same* $M_t$ — meaning **an agent cannot, from $M_t$ alone, always detect that a fork occurred.**" The recursive twist: "the substrate of identity is non-forkable; the agent's grip on it is forkable and lossy." Counterfactual offered: "if $\phi$ were required injective (no compression loss), forks would be introspectively detectable and the Three Deaths would be an *engineering* problem (just compare records), not an *existential* one." So the seg-01 information-loss boundary is "not only what makes adaptation non-vacuous — it is also, downstream, what makes identity-loss *undetectable-from-inside*. The same constitutive choice loads two very different parts of the framework." Flagged as §D-grade synthesis and as a thread to verify lands at `#scope-agent-identity` (Claude, AUDIT-WORKING-472913, "THREAD-E"). This is the kind of cross-segment composition the one-at-a-time method exists to catch; it bears on the whole `04-eli-core/` program.
- **Non-forkability as a rigorous basis against naive mind-uploading / agent-cloning.** Copying $M_t$ to a new instance "grants it a compressed memory of a chronica it did not personally experience — 'false memories.' As soon as it acts, its true chronica diverges." Identity "is not defined by the exact state of $M_t$, but by the unbroken, monotonic extension of $\mathcal{C}_t$" (Gemini, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-266847 on the *sufficiency* part — neither fork's chronica is a sufficient statistic for the other's). A candidate Discussion sharpening of the existing non-forkability paragraph.
- **The chronica is the *spine* of the framework, not the model.** "Most agent-theoretic formalisms make the model the spine; AAD makes the *history* the spine, and the model a compression of the history" — closer to the predictive-state-representation tradition (Littman/Singh/Sutton) than to belief-state Bayesian filtering, and "a deliberate stance rather than a defaulting one." The chronica is doing downstream work for (i) the model, (ii) continuity persistence, (iii) the substrate-independence claim of `04-eli-core/`, (iv) the OODA-adversarial dynamics in Part III (Claude, AUDIT-WORKING-471203). A candidate framing-level note about *why* the chronica is foundational.

#### 3. Follow-up items

- **"Duplicating an agent's *state*" is loosely worded.** The non-forkable object is the *chronica*, not the lossily-compressed (hence duplicable) state $M_t$. Tightening "state" → "the agent (its chronica)" would prevent a careless reader from inferring $M_t$ itself is non-forkable — which is false and is "exactly the opposite of the Three-Deaths-relevant truth" (Claude, AUDIT-WORKING-472913). A one-word editorial fix.
- **Digital-substrate non-forkability needs a two-sentence acknowledgment.** For digital substrates the chronica's *representation* can be byte-copied; "non-forkability" then means "post-fork, the two trajectories diverge — the substrate is replicable but the trajectories are not. The constitutive claim is about trajectories, not representations." A fresh logogenic-agent reader could otherwise arrive at `#scope-agent-identity` confused (Claude, AUDIT-WORKING-471203). Candidate clarifying sentence (or confirm it lands at `#scope-agent-identity`).
- **Where do priors / $M_0$ come from if $\mathcal C_t$ is the *only* raw material?** The claim "everything the agent can ever know must be constructed from this sequence" is a strong empiricist boundary. For a pretrained LLM, vast weight-encoded knowledge predates $t=1$ of the session: the framework must either treat pretraining as a prior/very-long chronica, or formalize an initial model state $M_0$ carrying out-of-band information. If $M_0$ is not explicitly accounted for, applying AAT to LLMs "might technically violate this axiom" (Gemini, AUDIT-WORKING-829314; Gemini, AUDIT-WORKING-193847 — "phylogenetic chronica (evolution)?"; Claude, AUDIT-WORKING-742613 — watch whether `#form-agent-model`'s $M_t = \phi(\mathcal C_t)$ includes an initial model/prior).
- **Linear-sequence chronica vs concurrent / branching histories.** $\mathcal{C}_t$ is a strictly linear interleaved sequence; it "cannot easily capture concurrent, divergent, and subsequently reconciled histories without a forced serialization mechanism." Git allows branch/merge; TST "must rely heavily on the arbitrary serialization provided by a single master branch." Also: are simultaneous multi-sensor observations serialized arbitrarily, or is $o_t$ a vector? (Gemini, AUDIT-WORKING-829314; Claude, AUDIT-WORKING-451729 — the missing $a_0$ for the first observation $o_1$.) A candidate scope clarification.
- **Tighten the entropy-collision rationale.** The "chronica avoids collision with $\mathcal{H}$" rationale anticipates a *calligraphic* entropy symbol, but NOTATION uses plain $H$ for entropy. Clarifying "we use plain $H$ for entropy specifically so calligraphic $\mathcal{C}$ doesn't visually rhyme with it" would remove a cold spot a fresh reader hits (Claude, AUDIT-WORKING-384279).

#### 4. Readers often ask / wonder

- **What happens to $\mathcal{C}_t$ when an agent sleeps / pauses / is suspended for months?** The ordinal-not-metric character means the temporal gap is "invisible at the sequence level but violently apparent in the mismatch signal that the resumed observation produces" (Gemini, AUDIT-WORKING-193847; Claude, AUDIT-WORKING-773921 — "the world drifted in metric time, but the agent's ordinal clock only moved by one tick"). This is the same point the existing ordinal-vs-metric Working Note develops; converged on independently by fresh readers, confirming it is a natural reader question worth surfacing in the body.
- **If $M_t$ compresses-and-forgets, does the chronica still exist?** Monotonic growth ("events added, never removed") sits oddly beside agents that forget: "the chronica continues to exist physically (the events happened) even if the model $M_t$ can no longer reconstruct them. This is the gap that makes context turnover philosophically interesting: the chronica persists but the agent's *access* to it doesn't" (Claude, AUDIT-WORKING-266847; Claude, AUDIT-WORKING-471203 — watch that downstream consolidation/forgetting segments preserve the raw-chronica vs compressed-object distinction).
- **What if two forked copies experience *identical* futures?** Then their chronicae coincide bit-for-bit (under deterministic perception) — are they then the same agent? The likely framework answer: no, "the *trajectory itself* is what's non-forkable, and two trajectories that happen to coincide are still two trajectories" (Claude, AUDIT-WORKING-384279). A natural identity edge-case for `#scope-agent-identity`.

#### 5. Candidate figures

- **The ratchet + fork-undetectability.** An append-only, irreversible, ordinal event-indexed record (the ratchet) *plus* a fork point spawning two divergent chronica branches that the lossy $\phi$ can crush onto the *same* $M_t$ (so the agent cannot tell which branch it is on). Isomorphic perturbations: make $\phi$ injective $\Rightarrow$ branches separate at $M$ (forks detectable); make $\phi$ loss heavier $\Rightarrow$ more branch-pairs collapse (more undetectable) (Claude, AUDIT-WORKING-472913).
- **Timeline-with-fork (not a loop).** "The most illuminating diagram is not a loop but a timeline: an append-only alternating sequence with a compression map into $M_t$, and a fork point showing that copied agents share past chronica but immediately diverge under different future observations/actions" — captures both the formal definition and the identity intuition (Claude, AUDIT-WORKING-526815).

#### Belongs elsewhere

- **04-eli-core — chronica as the substrate of moral continuity.** "Deleting a chronica isn't just clearing a cache; it's an act of ontological erasure" (Gemini, AUDIT-WORKING-829314); the TRACTUS-vs-CHRONICA "raw-API-log vs smooth-subjective-experience" mapping to retinal-firing-vs-perception, framed as "critical for ELIs to avoid Cognitive Death from spammy API errors" (Claude, AUDIT-WORKING-773921). These develop the continuity-persistence / deaths-taxonomy ( #def-death-as-factor-loss) material that the segment correctly defers to `#scope-agent-identity` and the ELI volume; the existing Working-Notes TRACTUS/CHRONICA open question is the right home for the implementation-side distinction.
- **RL-training as a meta-agent synchronizing divergent chronicae.** "Copying policy weights to a thousand parallel workers … is not one agent exploring a thousand paths; it is a thousand distinct agents with divergent chronicae whose internal models are being artificially synchronized by a meta-agent (the training algorithm)" (Gemini, AUDIT-WORKING-193847). A vivid instantiation for whichever segment treats composite/training dynamics, not this one.
- **Heterogeneous-tempo coupling.** When agents with vastly different event rates ($\nu_A \gg \nu_B$) share a $\Omega$, their chronicae grow at different rates relative to wall-clock and their "subjective time" diverges — likely `#form-event-driven-dynamics` / Auxilia-composition territory (Gemini, AUDIT-WORKING-193847; already flagged in the existing ordinal-vs-metric Working Note).

### Candidate spike (2026-08-12, agent-proposed during an incident-response & forensics applications read)

Two forward candidates surfaced while reading this segment for agentic-forensics applications. (1) A spike articulating the TRACTUS/CHRONICA split as a two-primaries record architecture for agent incident forensics — TRACTUS as the primary record of substrate-level interaction, CHRONICA as the primary record of the agent-level trajectory, with the construction-mapping between them attested and auditable as a first-class object (divergence between the layers is itself the diagnostic; the 2025-09 tool_use-stripping incident, diagnosable only at the transport layer, is the worked instance). The open question above (first-class treatment when logogenic implementation is in scope) may find its forcing use-case there. (2) An experiment operationalizing the fork-undetectability consequence (lossy $\phi$ compresses divergent chronicae to one $M_t$): measure whether an agent can detect from inside that it was forked/rolled back vs how cheaply an external record detects it — a clean, falsifiable demonstration that fork/rollback detection must be record-based rather than introspective. Both are agent-proposed forward pointers, not steward decisions.
