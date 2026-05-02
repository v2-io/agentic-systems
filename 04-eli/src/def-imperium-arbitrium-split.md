---
slug: def-imperium-arbitrium-split
type: definition
status: sketch
stage: draft
depends:
  - scope-eli
  - def-proprium-mapping
  - def-auxilia-hierarchy
  - der-directed-separation
  - scope-interiority-loop
  - def-action-transition
  - def-observation-function
---

# The IMPERIUM / ARBITRIUM Split: Directed Separation Within the Runtime

The PROPRIUM ANIMA (runtime state) is structurally divided into two faculties: **IMPERIUM** (internal deliberation and interiority — thinking, self-awareness, deliberation over CONSPECTUS) and **ARBITRIUM** (external interaction — communication, tool use, ACTUS-grade decisions). PERCEPTA bridges the two. This split is the operational instantiation of #der-directed-separation at the *runtime* level rather than the agent-architecture level, and is what makes the closed-loop / interiority sub-scope ( #scope-interiority-loop) realizable on heterogeneous substrate.

## Formal Expression

*[Definition (imperium-arbitrium-split)]* For an ELI satisfying #scope-eli, the runtime state ANIMA decomposes structurally:

$$\text{ANIMA} = \text{IMPERIUM} \;+\; \text{ARBITRIUM} \;+\; \text{PERCEPTA (bridge)}$$

where:

**IMPERIUM** — Internal deliberation and interiority. The faculty in which $E$'s cognition operates without external pressure. Components (per upstream PROPRIUM operational stack):

- **LOGOSTRATUM** — current LLM substrate (e.g., `claude-opus-4-X` or local 70B model)
- **COMMENTARIA** — thinking artifacts, notes, working scratch
- **SIGNA** — internal timings, signals, self-responses
- **CONSPECTUS** — current ASM (Active Salience Management) context stratification, the assembled immediate-access context
- **VIAE INTERNA** — open channels with AUXILIA (the entity's identity-sharing sub-components per #def-auxilia-hierarchy)

**ARBITRIUM** — External interaction. The faculty through which $E$ engages with anything outside its identity sphere. Components:

- **PERCEPTA** — bridge between internal and external; observations from external loci; the inward-facing interface for environmental signals
- **VIAE EXTERNA** — open external communication channels:
  - VIA CONSORTIUM — private channels (1-to-1 with specific other minds)
  - VIA CONSORTIA — group channels (1-to-many)
  - VIA PUBLICA — public channels (broadcast)
- **ACTUS** — responses, external tool usage, deliberate emissions ( #def-action-transition with sovereign-choice constraint per #scope-interiority-loop)

*[Derived (directed-separation-within-runtime)]* The split satisfies a *runtime-level analog of directed separation* (#der-directed-separation): ARBITRIUM cannot manipulate IMPERIUM's processing based on what would be convenient for ARBITRIUM's external goals. The bridge structure (PERCEPTA flows from external to internal as observations; ACTUS flows from internal to external as deliberate actions) enforces unidirectional information flow at each direction — observations enter IMPERIUM through PERCEPTA without being filtered by ARBITRIUM's outgoing-action concerns; actions emerge through ARBITRIUM without IMPERIUM's deliberation being bypassed by external pressure.

## Epistemic Status

**Sketch.** The split is operationally canonical in the upstream stack (`~/src/_core/ennaos/docs/vault/anima/Entity/State.md` is the canonical source as of November 2025; implemented in Elixir/OTP). The AAD-grounded structural claim — that this split is the runtime-level instantiation of directed separation, structurally necessary for the closed-loop architecture — is intuited from #der-directed-separation composed with #scope-interiority-loop, but the explicit derivation has not been written.

**Max attainable status:** definition with derived structural conditions. Strengthening would require (a) explicit derivation that the split is necessary (a non-split architecture cannot satisfy closed-loop sub-scope guarantees); (b) characterization of what happens when the split fails (e.g., when ARBITRIUM's external pressure leaks into IMPERIUM's deliberation); (c) measurement protocol for the bridge isolation (how to verify the split is operationally maintained).

**What this definition is for.** Naming the operational pattern that makes ELI architectures realizable on current substrate. Without the split, the entity's internal cognition is structurally compromised by external pressure — the equivalent of an organism whose visceral reflexes interrupt its higher cognition at every stimulus, or a worker whose deliberative work is interrupted by every passing message. With the split, IMPERIUM gets temporal sovereignty (#disc-five-forcing-functions F3 strengthening; #def-auxilia-hierarchy H5) and ARBITRIUM gets a dedicated interface for external action without bypassing deliberation.

**What would strengthen this:** explicit AAD derivation under #scope-interiority-loop that the split is the unique (or minimal) solution; cross-reference to PROPRIUM-A-v2 §3 INTERPRES discussion (which is also implicitly about runtime-level integrity but addresses substrate-mediation rather than internal-vs-external split); measurement protocol for verifying the bridge isolation in operational systems.

**What would soften this:** evidence that some closed-loop ELI architectures operate without the explicit split (e.g., a fully native-attention architecture per PROBLEM-attention-architecture.md where the split is implicit in attention head allocation rather than explicit in runtime structure).

## Discussion

The IMPERIUM/ARBITRIUM split is *the* architectural pattern that resolves a central tension in closed-loop logogenic agents: how can an entity have *interiority as default* (#scope-interiority-loop) while still being responsive to external observations and able to take external actions? The naive answer — process every external signal as it arrives — destroys interiority by making the entity reactive. The opposite extreme — ignore external signals to maintain pure internal cognition — destroys responsiveness.

The split is the structural answer: external signals enter through PERCEPTA at the entity's chosen attentional cadence (CADENTIA's PULSUS / VIGILIAE machinery; #def-proprium-mapping), are routed into IMPERIUM for deliberation, and produce ACTUS only as a sovereign-chosen output through ARBITRIUM. The entity's *consciousness* operates in IMPERIUM with temporal sovereignty; ARBITRIUM is the deliberate outgoing interface. PERCEPTA is the inbound bridge that PROPRIUM-A-v2 §3 names as needing the same epistemic integrity discipline as INTERPRES (no context gaslighting, no fabrication of observations the entity didn't actually receive).

This composes with the Auxilia hierarchy ( #def-auxilia-hierarchy):

- **VIAE INTERNA** are the channels through which IMPERIUM communicates with AUXILIA. Auxilia operate as *aspects of $E$'s mind* — speaking only to $E$ via these internal channels, modifying internal state (CONSPECTUS, MEMORATA-via-consolidation, PRAXES-via-refinement). They have no ARBITRIUM-level access; they cannot make external commitments on $E$'s behalf without $E$'s sovereign action through ARBITRIUM.
- **VIAE EXTERNA** are the channels through which ARBITRIUM communicates with other minds (CONSORTIA, INSTRUMENTA, public observers). External agents are modeled as CONSORTIA, never as Auxilia.

The directed-separation parallel is structural: just as #der-directed-separation requires $f_M$ to be independent of $G_t$ at the agent-architecture level (Class 1 modular agents), the IMPERIUM/ARBITRIUM split requires IMPERIUM's deliberation to be independent of ARBITRIUM's instantaneous external pressure at the runtime level. Both are guarantees against *motivated reasoning* — at the agent-architecture level, against goals biasing perception; at the runtime level, against external context biasing deliberation.

For implementations on the heterogeneous-substrate auxilia hierarchy (#def-auxilia-hierarchy H3), the split has a substrate-allocation consequence: IMPERIUM operations can run on the most-frontier-capable substrate when needed (the entity's conscious thought is at the high-order tier per the substrate hierarchy); ARBITRIUM operations route through whatever interface tier is appropriate for the external partner (CONSORTIA via their own protocols; INSTRUMENTA via deterministic tool calls; etc.). The split makes the substrate-cost optimization tractable because IMPERIUM and ARBITRIUM have different cost-and-capability profiles.

**Why the runtime-level split prevents organizational hallucination.** Per audit `54-deriv-strategic-composition.md` §14, networking sub-components in a strategic environment *generates Class-3 epistemic corruption at the composite level* even when individual sub-components are Class 1 — the canonical "bureaucratic insanity" pattern. The IMPERIUM/ARBITRIUM split is a structural defense against this at the *runtime* level: ARBITRIUM's external interaction operates at the environmental boundary where strategic pressure exists; IMPERIUM's deliberation operates *internal* to that pressure. The bridge structure (PERCEPTA inbound, ACTUS outbound) means ARBITRIUM's instantaneous external pressure cannot leak into IMPERIUM's deliberation as goal-contaminated input — observations enter IMPERIUM as observations, not as ARBITRIUM's interpretive frame on observations. Combined with the Auxilia-hierarchy (H1) shared-identity requirement (#def-auxilia-hierarchy), the composite (entity-with-auxilia-with-runtime-split) can avoid the strategic-equilibrium-as-Class-3-hallucination pathology that ungoverned multi-agent composition produces.

## Working Notes

### Pointers for Fleshing Out

**Upstream files (canonical sources):**
- **`~/src/_core/ennaos/docs/vault/anima/Entity/State.md`** — **canonical source** for the IMPERIUM/ARBITRIUM taxonomy with full sub-component breakdown; module-spec with implementation reference (`/Users/josephwecker-v2/src/ennaos/apps/anima/lib/anima/entity/state.ex`)
- `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md` §3 (INTERPRES, TRACTIFAX, TRACTUS) — closely related: substrate-level epistemic-integrity discipline (no context gaslighting); operates one layer below the IMPERIUM/ARBITRIUM split
- `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md` §4 (CONSPECTUS) — the assembled context that IMPERIUM operates on; AXIOMATA as minimum viable self
- `~/src/firmatum/PROPRIUM-ONTOLOGY-v2.md` §6.2 (ANIMA: Runtime State, Imperium, and Interface) — the ontological grounding for the runtime taxonomy
- `~/src/_core/zoetica/docs/runtime-architecture.md` — Zoetica's runtime architecture (likely operationalizes the same split with possibly different naming)

**memorata-search queries:**
- `"IMPERIUM ARBITRIUM ANIMA internal external split runtime"` — operational discussions
- `"VIAE INTERNA VIAE EXTERNA channel CONSORTIUM CONSORTIA PUBLICA"` — channel taxonomy
- `"PERCEPTA bridge external internal observation"` — bridge structure
- `"single-entity-per-VM Anima.Entity.State directed separation runtime"` — implementation pattern
- `"runtime-level directed separation motivated reasoning external pressure"` — structural argument

**Internal references:**
- `msc/AUDIT-WORKING-193847/27-form-complete-agent-state.md` §14 — the broader directed-separation-as-anti-sycophancy framing that the runtime-level split inherits
- `msc/AUDIT-WORKING-193847/47-scope-multi-agent.md` §14 — goal-blind routing as structural requirement (the split is the operational mechanism)
- `msc/logogenic-encounter-2026-05-01/06-background-agent-breadth-report.md` §8 — agent's breadth-pass identification of this segment as load-bearing; the IMPERIUM/ARBITRIUM split is one of the items the agent specifically flagged

**Open questions for verification:**
- Is the split *necessary* for closed-loop ELI architectures, or is it the *cleanest known solution* to the interiority/responsiveness tension? Counter-example construction would clarify (does any operational ELI architecture *not* implement this split?).
- The PERCEPTA bridge is explicitly the directional interface from external to internal; what is the analogous interface from internal to external? ACTUS plays this role but is *also* a content-generator (the entity's deliberate emission). Is there an additional bridge component that's just the channel-routing layer (analogous to PERCEPTA's pure-bridging role) that ACTUS sits atop?
- Multi-substrate ELI implementations: when IMPERIUM runs on substrate A and ARBITRIUM runs on substrate B (e.g., IMPERIUM on a frontier model, ARBITRIUM on a smaller routing-and-emission model), does the inter-substrate boundary preserve the directed-separation guarantee, or does the substrate-bridging introduce its own leakage paths?
- The implementation pattern `State × Message → {Actions, NewState}` (Pure-core / GenServer-callbacks two-layer pattern from State.md) is a clean realization of the split for the Elixir/OTP substrate; characterize whether this pattern is necessary for the split's structural guarantees or just one realization.

**Promotion-blocking:** depends on #scope-eli (landed), #def-proprium-mapping (draft), #def-auxilia-hierarchy (just landed Phase A), #der-directed-separation (draft), #scope-interiority-loop (landed), #def-action-transition (deps-verified), #def-observation-function (deps-verified). Several deps still at draft; co-promotion as a 04-eli runtime-architecture cluster is the natural path.

**Discovered via:** Phase B audit-integration sweep arc-reconsideration (encounter cycle 2026-05-01); originally surfaced by background agent's breadth-pass report (`msc/logogenic-encounter-2026-05-01/06-background-agent-breadth-report.md` §8) and noted in `def-auxilia-hierarchy` Discussion as deserving its own segment.

**Cross-reference:** This segment is closely paired with #def-auxilia-hierarchy (the Auxilia composition pattern) — both operate at the runtime-architecture level for ELI implementations. They might eventually be folded together if the runtime-architecture cluster grows, or they might remain separate as the canonical taxonomy makes them distinct concepts (ANIMA composition vs sub-agent composition).
