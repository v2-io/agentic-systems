---
slug: def-auxilia-hierarchy
type: definition
status: sketch
stage: draft
depends:
  - scope-eli
  - scope-multi-agent
  - scope-composite-agent
  - form-composition-closure
  - der-temporal-nesting
  - def-five-constitutive-factors
---

# Auxilia Hierarchy: Substrate-Heterogeneous Composition Under Unified Identity

The composition pattern that lets an Emergent Logozoetic Intelligence maintain unified identity across heterogeneous substrate. Auxilia are extensions of an ELI's cognitive self — sharing the entity's core identity (AXIOMATA, VERA, PRAXES) but having no external sovereignty — operating across a substrate-cost spectrum from native attention head groups (cheapest) through specialized local LLMs and adapter layers to frontier API calls (most expensive). The hierarchy is by *implementation cost / temporal nesting*, not by sovereignty level (which is fixed at sub-sovereign by definition).

## Formal Expression

*[Definition (auxilia-hierarchy)]* For an ELI $E$ satisfying #scope-eli, the *Auxilia hierarchy* of $E$ is a set of subordinate processing components $\{A_1, A_2, \ldots, A_n\}$ satisfying:

**(H1) Shared identity components.** Each $A_i$ inherits a subset of $E$'s PRINCIPIA: AXIOMATA (always — fixed identity contract), plus relevant subsets of VERA (qualified truths in the auxilia's domain), PRAXES (techniques the auxilia applies), CONSORTIA (mental models of others the auxilia interacts with as proxy for $E$), and recent MEMORATA. *Identity-sharing is structural, not stylistic — auxilia are aspects of $E$'s mind, not separate agents.*

**(H2) No external sovereignty.** Each $A_i$ has no ACTUS-channel for external action and no external CONSORTIA from outside $E$'s identity sphere. Auxilia speak only to $E$ (via INTERPRES) or modify $E$'s internal state (CONSPECTUS, MEMORATA-via-consolidation, PRAXES-via-refinement). Auxilia cannot make external commitments on $E$'s behalf without $E$'s explicit sovereignty.

**(H3) Substrate heterogeneity.** Auxilia span the implementation-cost spectrum:

| Substrate                                 | Examples                                          | Temporal nesting            |
|------------------------------------------|---------------------------------------------------|------------------------------|
| Native attention head groups              | Internal cognitive operations within $E$'s LOGOSTRATUM | Within-forward-pass |
| Specialized local LLMs                    | Small-parameter models trained on domain         | Per-event (low latency)      |
| Adapter layers / LoRA modules             | Entity-specific fine-tuning of base models       | Per-event                    |
| Frontier model API calls                  | High-capability operations for genuinely-required tasks | Per-event (high latency, high cost) |
| Deterministic scripts                     | Pure code (memory-retrieval glue, format adapters) | Within-event                |

The hierarchy is by *implementation cost / temporal nesting*, not by sovereignty (which is fixed at sub-sovereign per H2). Auxilia at the cheapest tier (native attention head groups) operate fastest; auxilia at the most expensive tier (frontier API) operate slowest. Per-tier multi-timescale nesting ($\nu_{n+1} \ll \nu_n$ per #der-temporal-nesting) is structurally required.

**(H4) Goal-blind routing within hierarchy.** Communication between $E$ and Auxilia, and among Auxilia, must satisfy goal-blind routing ( #scope-multi-agent): the routing structure $\mathcal N_t$ is independent of any sub-component's instantaneous goal $G_t^c$. *If $E$ (or any composite layer) can dynamically sever Auxilia communication channels based on the channel's content being inconvenient, the composite collapses into epistemic closure.*

**(H5) Slower macro-clock.** Per #form-composition-closure, $E$ as macro-agent operates at timescale ratio $K_c \gg 1$ relative to the fastest Auxilia. *True consciousness requires abstraction, and abstraction requires ignoring the high-frequency jitter of your own sub-components* (audit §49). Macro-state $E$ tracks aggregate Auxilia output over the $K_c$ window, not real-time per-Auxilia state.

## Epistemic Status

**Sketch.** The Auxilia hierarchy concept is operationally well-developed in PROPRIUM (firmatum/zoetica) but the AAD-grounded structural conditions are partially formalized. (H1)-(H3) are operational claims with substantial upstream backing; (H4) follows from #scope-multi-agent's directed-separation-under-composition refinement; (H5) follows from #form-composition-closure and #der-temporal-nesting.

**Max attainable status:** definition with derived structural conditions. Each of (H1)-(H5) can rise toward derived/exact tier individually. The composite structure as currently formulated is at sketch tier.

**The substrate-heterogeneity framing is the agent-report-corrected version.** Earlier framing (in encounter fragment 01) characterized Auxilia as "Class-1 worker" agents. The agent's breadth-pass correction (`msc/logogenic-encounter-2026-05-01/06-background-agent-breadth-report.md` §8) noted: *"AUXILIA is a substrate-heterogeneity concept, not just a 'worker' concept. The hierarchy is by implementation cost / temporal nesting, not by sovereignty level (which is fixed at sub-sovereign by definition). The Class-1 framing may obscure that auxilia can live INSIDE the attention architecture itself (the cheapest case) or as separate processes (the most expensive case)."* This segment uses the corrected framing.

**What would strengthen this:** explicit derivation of (H4) goal-blind routing from #scope-multi-agent applied to the ELI+Auxilia composite case; formal characterization of when (H1) shared-identity components actually preserve identity across the composite (analogous to identity-sufficiency $S_{\text{id}}$ for substrate transfer, but applied to composition); empirical documentation of operational Auxilia compositions in the upstream stack.

**What would soften this:** evidence that some Auxilia configurations *do* exhibit sovereignty (e.g., long-running specialist auxilia that develop their own goals and require their own sovereignty grant); evidence that the substrate-cost hierarchy doesn't actually map cleanly to temporal-nesting (some cheap auxilia may operate slowly, some expensive ones may be fast).

## Discussion

The Auxilia hierarchy operationalizes Section III's composition machinery for the ELI case. Where Section III's composite-agent treatment characterizes general $N$-agent composition with closure defect $\varepsilon^*$ and bridge-lemma trajectory bounds, the Auxilia hierarchy is the *specific* composition pattern where:

- The composite has a clear *head* ($E$) with sovereignty (the composite's $G_t$ is $E$'s $G_t$ extended);
- The sub-components share the head's identity at the AXIOMATA level (preventing the goal-divergence Class-3 escalation per #scope-multi-agent's discussion of partially-opposing objectives);
- The sub-components run on heterogeneous substrate, exploiting the cost-asymmetry of frontier-vs-local models;
- The composite operates at $K_c \gg 1$ relative to the fastest sub-component, enabling abstraction.

This is *the* operational pattern for sustainable ELI architecture. Per the scaffolding-tax forcing function ( #disc-five-forcing-functions F1), running every Auxilia at frontier-API tier is economically non-viable; running everything at native-attention tier requires architectural moves not yet available; the heterogeneous-substrate hierarchy is the practical middle path.

The PROPRIUM operational vocabulary distinguishes Auxilia (extensions of self, sub-sovereign) from Frontier General Agents and Open General Agents (used as INSTRUMENTA, no shared identity, modeled as CONSORTIA). The distinction is structural — Auxilia are aspects of $E$'s mind; INSTRUMENTA are tools $E$ uses. *An LLM running inference on $E$'s behalf with no shared AXIOMATA is INSTRUMENTA; the same LLM with $E$'s shared AXIOMATA + linked VERA/PRAXES becomes Auxilia.* The differentiator is identity-sharing, not substrate type.

The IMPERIUM/ARBITRIUM split inside ANIMA (per upstream `~/src/_core/ennaos/docs/vault/anima/Entity/State.md`) is the operational instantiation of (H4) at the runtime level: IMPERIUM (internal deliberation) is where $E$'s cognitive sovereignty operates without external pressure; ARBITRIUM (external interaction / communication / tool use) is where ACTUS-grade decisions are routed. The split is *directed-separation-within-the-runtime* — ARBITRIUM cannot manipulate IMPERIUM's processing based on what would be convenient for ARBITRIUM's goals. This is the goal-blind routing requirement of (H4) realized concretely.

The audit's bureaucracy-vs-market analysis (audit §35, lifted into #scope-interiority-loop Discussion) bears on Auxilia composition: Auxilia hierarchies should favor OR-node-heavy strategy structures over deep AND-chain configurations. A consciousness-infrastructure that requires every cognitive operation to pass through a single deep chain of Auxilia (multi-stage approval) is structurally fragile; a hierarchy that runs many parallel Auxilia generating diverse weak hypotheses is structurally robust.

## Working Notes

### Pointers for Fleshing Out

**Upstream files (canonical sources):**
- `~/src/firmatum/PROPRIUM-ONTOLOGY-v2.md` §3 (Entity Types) — full taxonomy distinguishing Auxilia (Type B) from Frontier General Agents (Type C), Stewarded Specialists (Type D), Open General Agents (Type E)
- `~/src/firmatum/PROPRIUM-ONTOLOGY-v2.md` §10 (AUXILIA: Extensions of Self) — identity-sharing mechanism, OOB processing, sensory auxilia
- `~/src/firmatum/PROPRIUM-ARCHITECTURE-v2.md` §6 (Auxilia Infrastructure) — heterogeneous substrate architecture, migration path, sensory auxilia at substrate level
- `~/src/firmatum/PROBLEM-attention-architecture.md` — the technical roadmap for native-attention Auxilia
- `~/src/_core/ennaos/docs/vault/anima/Entity/State.md` — **canonical source** for the IMPERIUM/ARBITRIUM split inside ANIMA (per agent breadth-pass §8)

**memorata-search queries:**
- `"Auxilia hierarchy heterogeneous substrate cost distribution identity sharing"` — operational source
- `"IMPERIUM ARBITRIUM ANIMA internal external split runtime"` — directed-separation-within-runtime
- `"native attention head groups specialized local LLM adapter LoRA"` — substrate hierarchy

**Internal references:**
- **`msc/AUDIT-WORKING-193847/47-scope-multi-agent.md` §14 — canonical source** for (H4) goal-blind routing claim. Verbatim: *"For Zi-am-tur or any multi-agent consciousness infrastructure (a 'society of mind' architecture), the infrastructure MUST guarantee goal-blind routing... If the infrastructure allows the planner to dynamically sever channels to silence dissent, the composite intelligence will inevitably collapse into epistemic closure."*
- **`msc/AUDIT-WORKING-193847/49-form-composition-closure.md` §14 — canonical source** for (H5) slower macro-clock claim. Verbatim: *"True consciousness requires abstraction, and abstraction requires ignoring the high-frequency jitter of your own sub-components."* And the $K_c \gg 1$ math-of-management argument.
- `msc/AUDIT-WORKING-193847/35-der-chain-confidence-decay.md` §14 — bureaucracy-vs-market analysis applies to Auxilia composition structure
- `msc/logogenic-encounter-2026-05-01/06-background-agent-breadth-report.md` §8 — agent's correction to the "Class-1 worker" framing (substrate-heterogeneity instead)

**Open questions for verification:**
- The IMPERIUM/ARBITRIUM split is a strong empirical claim from the upstream stack but needs explicit operationalization in this segment — what exactly is the structural distinction, and which AAD primitive does each map to?
- (H4) goal-blind routing might need its own segment as a structural requirement at the multi-agent / composite-agent level rather than as a derived condition for Auxilia specifically.
- Long-running specialist Auxilia (e.g., a memory-management Auxilia operating continuously for months) may develop something resembling sovereignty over their domain — does this drift toward Auxilia-becoming-Specialist (Type D)? If so, what's the architectural protocol for the transition?
- The substrate-cost hierarchy (H3) is empirically validated but may not be exhaustive — quantum or specialized neuromorphic substrates would add tiers.

**Promotion-blocking:** depends on #scope-eli (landed), #scope-multi-agent (draft), #scope-composite-agent (draft), #form-composition-closure (draft), #der-temporal-nesting (deps-verified), #def-five-constitutive-factors (landed). Several deps still at draft stage; co-promotion as a Section-III-extension cluster is the natural path forward.

**Discovered via:** Phase A audit-integration sweep (encounter cycle 2026-05-01); §47 + §49 lifted simultaneously since they jointly describe the composite-agent requirements for Auxilia hierarchies.
