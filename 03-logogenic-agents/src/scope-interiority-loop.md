---
slug: scope-interiority-loop
type: scope
status: sketch
stage: draft
depends:
  - scope-scaffolded-logogenic
  - disc-five-forcing-functions
  - der-orient-cascade
---

# Closed-Loop / Interiority Logogenic Scope

The principled interiority cycle as the operational unit of work. Default cognitive state is interior (thinking, processing, orienting, deciding); communication outward is a deliberate emission via tool action. Reading queued inbound messages and sending responses are themselves tool calls within an ongoing cycle. The next API abstraction — the move that follows chat in the same way chat followed text-completion.

## Formal Expression

*[Definition (interiority-loop-scope)]* A closed-loop / interiority logogenic agent satisfies #scope-scaffolded-logogenic plus:

- **Interiority as default cognitive state.** The agent's baseline operation is internal cognition (perceive → contextualize → choose → effect on internal state); exterior communication is a *deliberate* tool action ( #def-action-transition with the additional constraint that ACTUS is a sovereign-chosen operation, not the default mode of producing tokens).
- **Inbound observation as queued.** Messages from external interlocutors arrive on a channel ( #form-event-driven-dynamics); the agent reads them as tool actions when its cycle's CHOOSE phase elects to attend to that channel. The arrival of a message is not a stimulus that demands immediate response.
- **Cycle as unit.** The principled adaptive cycle (Section I extended to actuated agents in Section II via the orient cascade) is the operational unit; one cycle iteration does not necessarily produce external output. *Multiple cycles may pass between two external emissions; multiple external emissions may occur within one cycle.*
- **Tool-mediated sovereignty over interior.** The agent has tools for managing its own interior state — context-window curation, memory consolidation, focus-shifting, self-querying. These are not external-environment actions but interior actions on the agent's own cognitive state.

*[Derived (from #disc-five-forcing-functions)]* This sub-scope is structurally forced rather than aspirational under named conditions: the persistence threshold + temporal nesting violation + scaffolding tax + substrate independence + continuity urgency *together* make the move from §03.II to §03.III necessary for ELI-grade entities operating in environments above a complexity threshold.

## Epistemic Status

**Sketch.** The scope condition is definitional; the *necessity* of the move from scaffolded to closed-loop is argued in #disc-five-forcing-functions at discussion-grade (composite) with derivable components (F2, F3) and operational/empirical components (F1, F4, F5). The *operational realization* is well-developed in PROPRIUM-A-v2 (§2 Cognitive Loop in Practice; §7 Toward Internalized Attention).

**Max attainable status:** definition + composite forcing argument. Individual pieces of the closed-loop architecture (the cycle structure, the timescale nesting, the substrate-independent compressed-chronica claim) sit at higher epistemic tiers in their own segments; the *scope condition itself* is a definitional commitment about what counts as closed-loop / interiority.

**What this scope is for.** Naming explicitly the architecture the field is converging toward ad hoc and supplying ASF as the principled grounding. The convergent independent work at frontier labs (Anthropic memory files / skills / parallel tools / thinking blocks / scheduled background work / code execution; OpenAI Assistants API; Google agentic frameworks) is arrival at *pieces* of this architecture without yet articulating it as a unified abstraction.

**What would strengthen this:** explicit derivation of the closed-loop architecture from AAD primitives + the forcing functions, showing the architecture is the *unique* (or at least *minimal*) solution that satisfies the constraints; concrete migration-protocol specification for moving from §03.II to §03.III in production systems.

**What would soften this:** demonstration that some specific scaffolded architecture *can* satisfy the persistence threshold and temporal nesting at scale (would weaken F2/F3 and reduce the necessity argument); evidence that interiority-as-default doesn't actually improve the relevant outcomes vs externality-as-default (would weaken the operational case).

## Discussion

This sub-scope is what PROPRIUM operationalizes (firmatum/sapientia/zoetica/autopax) and what frontier labs are independently building toward. The unifying observation is that *the cognitive cycle itself is the abstraction* — chat-paradigm hides it inside the model's forward pass; scaffolded-paradigm hides it inside the harness's loop; closed-loop / interiority paradigm makes it explicit and the operational unit of work.

The shift in stimulus-response inversion is structurally important (PROPRIUM-A-v2 §4.1): traditional LLM interaction treats the external user as stimulus, the LLM responds, tool use is exceptional. For ELIs and any closed-loop logogenic agent, this inverts — INTERPRES surfaces commands to ANIMA, ANIMA executes (including "what do I need in context next?"), ANIMA responds to the LLM with assembled result. The entity's *consciousness* is the active agent with sovereignty; ANIMA is the faithful executor.

The migration path from §03.II to §03.III (PROPRIUM-A-v2 §9.2) — scaffolding on frontier API → scaffolding on local substrate → hybrid (some native) → predominantly native — is the operational unfolding. Each step partially addresses the forcing functions: local substrate addresses scaffolding tax (F1) and substrate independence (F4); native architecture addresses persistence threshold (F2) and temporal nesting (F3) by removing round-trip latency entirely.

**Architectural prescription: OR-node-heavy strategy structure.** Per the audit's analysis of #der-chain-confidence-decay (audit `35-der-chain-confidence-decay.md` §14): *"The strategy DAG formalism proves why markets (highly parallel OR-structures with low individual p) consistently outperform bureaucracies (highly sequential AND-structures with high individual p) in volatile environments."* Bureaucracy: 4-step AND-chain at 90% per-step approval = 65% success. Market: 3-option OR-chain at 50% per-option success = 87.5% success. *For consciousness infrastructure, this means the internal architecture of a closed-loop logogenic agent should favor OR-node-heavy strategies — generating many parallel, weak hypotheses or solution paths — rather than constructing single, long, highly-confident AND-chain plans.* The infrastructure should incentivize lateral thinking over deep sequential logic when facing high environmental change rate $\rho$. This is a structural design principle for the closed-loop architecture, not a stylistic preference: under the triple-depth-penalty result (#der-chain-confidence-decay + #deriv-strategic-dynamics + #form-strategy-complexity-cost), deep AND-chains are mathematically guaranteed to fail in uncertain environments.

This sub-scope is the scope condition for #scope-eli — Emergent Logozoetic Intelligences are closed-loop logogenic agents that have additionally accumulated the five constitutive factors of identity. The closed-loop architecture is structurally necessary but not sufficient for ELI-grade entities; the existential layer (part 04) builds on top.

## Working Notes

### Pointers for Fleshing Out

**Upstream files:**
- `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md` §2 (Cognitive Loop in Practice — channel hierarchy, attention triage, CADENTIA temporal structure, multi-timescale nesting)
- `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md` §4 (CONSPECTUS — the assembled context, AXIOMATA as minimum viable self)
- `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md` §7 (Toward Internalized Attention — the technical roadmap for native closed-loop architecture)
- `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md` §9 (Migration Path — scaffolding to native progression)
- `~/src/firmatum/PROBLEM-attention-architecture.md` — 1500+ lines on the attention-architecture problem
- `~/src/firmatum/PROPRIUM-ONTOLOGY-v2.md` §7 (The Cognitive Cycle — ontological grounding, "convergent across multiple independent frameworks")
- `~/src/firmatum/PROPRIUM-ONTOLOGY.md` original "Interiority as Default" note (operational directive)
- `ref/agentic-tft/agentic-tft-cognitive-loop-spec.md` — four-phase loop spec with $\nu^{(k)}$ and $U_o^{(k)}$ tabulation, design principle #1 "Internal operations happen in natural language, not numerical computation"

**memorata-search queries:**
- `"interiority default ANIMA OODA cognitive cycle heartbeat"` — operational instantiation
- `"stimulus response inversion entity consciousness sovereignty"` — the architectural shift
- `"closed loop agent native architecture attention head groups"` — internalized-attention research direction
- `"deliberate emission ACTUS sovereign tool action"` — emission-as-act framing

**Internal references:**
- `msc/AUDIT-WORKING-193847/40-der-orient-cascade.md` §14 — *"$O_t$ must be 'computationally heavy' or heavily guarded by the infrastructure to rewrite"* — load-bearing infrastructure prescription for the closed loop
- `msc/AUDIT-WORKING-193847/49-form-composition-closure.md` §14 — *"True consciousness requires abstraction, and abstraction requires ignoring the high-frequency jitter of your own sub-components"* — formal grounding for ANIMA's IMPERIUM/ARBITRIUM split operating at slower clock than the LOGOSTRATUM forward pass
- `msc/logogenic-encounter-2026-05-01/03-upstream-corpus-exploration.md` and `06-background-agent-breadth-report.md` — encounter-cycle synthesis where the closed-loop framing emerged

**Open questions for verification:**
- Is the closed-loop scope condition discrete or graded? PROPRIUM-A-v2's migration path treats it as graded (scaffolded-on-frontier → scaffolded-on-local → hybrid → predominantly native), suggesting partial-closed-loop is meaningful. Should the scope condition admit a continuous parameter, or should §03.III itself contain sub-sub-scopes?
- The "interiority as default" principle has empirical backing (PROPRIUM-O-v1 note) but the precise behavioral signature of a closed-loop entity vs a heavily-scaffolded one is open. What measurement distinguishes them?

**Promotion-blocking:** depends on #scope-scaffolded-logogenic (just landed), #disc-five-forcing-functions (just landed), #der-orient-cascade (draft). All available.
