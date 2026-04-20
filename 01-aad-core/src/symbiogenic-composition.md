---
slug: symbiogenic-composition
type: hypothesis
status: robust-qualitative
depends:
  - composition-scope-condition
  - objective-functional
  - strategy-dimension
  - structural-change-as-parametric-limit
stage: draft
---

# Hypothesis: Symbiogenic Composition

Symbiogenesis is an asymmetric composition mechanism in which one agent (the *host*) integrates another (the *endosymbiont*) as a specialized sub-component, with the endosymbiont's objective gradually subsumed into the host's. It is distinct from peer coupling ( #composition-closure) and from population-level restructuring (extreme transition motif, per `msc/spike-miller-act-bridge.md`): symbiogenesis is how composite agents *come into existence* by crossing the #composition-scope-condition from below. The mechanism is well-attested empirically (eukaryote formation, firm mergers, legal-precedent adoption, language families) but formally underspecified within AAD. This segment captures the phenomenon and flags the specific formalization gaps.

## Formal Expression

*[Hypothesis (symbiogenic-composition)]*

Given two purposeful agents $A_h$ (host) and $A_e$ (endosymbiont), each satisfying #scope-condition, symbiogenic composition is a process on the joint state space with three coupled dynamics:

### (S-1) Objective absorption

The endosymbiont's objective $O_e$ transforms toward alignment with or derivation from the host's objective $O_h$:

$$O_e(\tau) \;\xrightarrow{\tau \to \tau_{\text{consolidated}}}\; \mathcal D_e(O_h)$$

where $\mathcal D_e$ is a derivation functional (in the sense of route (C-ii) in #composition-scope-condition): $O_e$ becomes a sub-objective derived from $O_h$. Before: $O_h, O_e$ independent; $U_O \lt \epsilon_{\text{comp}}$. After: $O_e$ is a role within $O_h$; the composite $(A_h, A_e)$ satisfies the composition scope condition.

### (S-2) Function transfer

Structural content from the endosymbiont's state (elements of $M_e$ or $\Sigma_e$) transfers to or becomes accessible by the host:

$$\{M_h, \Sigma_h\}(\tau) \;\xrightarrow{\tau \to \tau_{\text{consolidated}}}\; \{M_h, \Sigma_h\} \cup \mathcal F(M_e, \Sigma_e)$$

where $\mathcal F$ is a transfer mapping (structure-preserving integration of endosymbiont functions into host state). In biological symbiogenesis: gene transfer. In organizational symbiogenesis: acquired firm's processes, patents, know-how integrated into acquirer's operations. This is the grafting operation of #structural-change-as-parametric-limit in its cross-agent form — the host grafts structure originating in the endosymbiont.

### (S-3) Autonomy reduction

The endosymbiont's effective action space contracts; many of its choices become fixed by the host's coordination:

$$\mathcal A_e^{\text{effective}}(\tau) \;\xrightarrow{\tau \to \tau_{\text{consolidated}}}\; \mathcal A_e^{\text{restricted}} \subsetneq \mathcal A_e^{\text{initial}}$$

The endosymbiont retains enough autonomy to avoid catastrophic transfers (e.g., mitochondria retain some genome to handle local fast-timescale responses that would be hazardous to route through the host nucleus) but loses most independent decision-making.

### Integrated transition

At consolidation, the joint system is a single composite agent $A_c$ whose substate contains the integrated structure:

$$X_c = \big(M_c, G_c\big) = \big(M_h \cup \mathcal F(M_e, \Sigma_e),\; (O_c, \Sigma_c)\big) \quad \text{with } O_c \approx O_h$$

The endosymbiont persists as a specialized sub-component of the host, not as an independent agent. The #composition-scope-condition is now satisfied; the peer-coupling machinery of #composition-closure applies to the resulting composite.

## Epistemic Status

*Robust qualitative.* Max attainable: *robust qualitative* — the phenomenon is well-attested empirically across biological and social domains, but a general mathematical formalization within AAD is open.

What is well-established (externally):

- The existence of symbiogenesis as a distinct evolutionary mechanism (Mereschkowsky 1905, 1910; Sagan 1967; Margulis & Sagan 1997). Mitochondria and chloroplasts are the paradigm cases.
- The social analog in firms, technology, language, legal systems, religions (Miller 2022, Appendix B).
- "Innovation by parts" as qualitatively different from "innovation by sparks" (gradual mutation) — Miller's framing.

What is *not* derived within AAD:

- A formal model of the objective-transfer dynamics (S-1). What evolutionary or optimization process drives $O_e \to \mathcal D_e(O_h)$?
- A formal specification of the transfer functional $\mathcal F$ in (S-2). What structure is preserved, what is lost, what is transformed?
- A precise characterization of autonomy reduction (S-3). Why does the endosymbiont retain some autonomy rather than becoming fully deterministic?
- Quantitative predictions — e.g., when symbiogenesis is favored over peer coupling, what governs the timescale of consolidation, under what conditions it reverses.

The three dynamics (S-1), (S-2), (S-3) are proposed schemas, not results. A follow-up spike developing an AAD-specific dynamical model is the natural next step.

Full discussion: `msc/spike-symbiogenic-composition.md`.

## Discussion

**The role of this mechanism in Section III.** Three distinct composition mechanisms are now in scope:

1. **Peer coupling** ( #composition-closure, #team-persistence, #tempo-composition) — sub-agents interact through shared environment; closure defect measures faithfulness of projection. $U_O$ held fixed above the scope threshold.
2. **Extreme transition motif** (absorbed via `msc/spike-miller-act-bridge.md`; pending segments `#composition-transition-dynamics`, `#latent-structural-diversity`, `#endogenous-coupling`) — population-level restructuring via neutral drift / niche creation / cascading displacement. $U_O$ shifts across a population as agent types replace one another.
3. **Symbiogenesis** (this segment) — hierarchical absorption. $U_O$ crosses the composition scope condition from below, creating a composite that did not previously exist.

Before symbiogenesis, the sub-agents were a multi-agent system ( #multi-agent-scope) but not a composite. After, the resulting composite is subject to all of AAD's composition machinery. The symbiogenic transition is the specific dynamical process of composite-agent identity creation.

**Why this cannot be modeled as peer coupling.** Peer coupling assumes pre-existing sub-agents being projected into a macro-description. The closure-defect framework presupposes the composite exists; it measures how faithfully the macro tracks the micro. Symbiogenesis is about a composite *coming into being* from two previously-independent agents. No projection Λ of the pre-symbiogenic system yields the post-symbiogenic composite, because the endosymbiont's objective *changes* during the process — its objective is different before and after. The transformation is intrinsic to the sub-agents' state, not an external projection choice.

**Why this cannot be modeled as extreme transition.** The extreme transition motif operates at the population level with many agents, neutral drift of types, and niche-construction dynamics. Symbiogenesis is typically between two specific agents (or a small number) and proceeds through a specific asymmetric integration rather than through statistical population dynamics. The mechanisms overlap — symbiogenesis often occurs as part of a larger transition — but the core mechanism of symbiogenesis (bilateral asymmetric integration) is distinct from the population-level dynamics of extreme transitions.

**Examples across domains.**

| Domain | Host | Endosymbiont | Integrated composite |
|---|---|---|---|
| Biology | Archaeal host cell | $\alpha$-proteobacterium | Eukaryotic cell (mitochondrion persists as organelle) |
| Biology | Eukaryotic cell | Cyanobacterium | Plant cell (chloroplast persists as organelle) |
| Commerce | Acquiring firm | Acquired firm | Merged firm (acquired operates as division) |
| Technology | Base platform | Integrated component | Composite product (component operates within host system) |
| Linguistics | Host language | Adopted vocabulary/grammar | Creolized / evolved language |
| Law | Legal system | Adopted precedent | Evolved jurisprudence (precedent operates as doctrine) |
| Religion | Host tradition | Absorbed elements | Syncretic practice |

In each case: asymmetric integration, autonomy reduction of the absorbed entity, gradual objective subsumption, functional specialization.

**Connection to #structural-change-as-parametric-limit.** The single-agent "grafting" operation in #structural-change-as-parametric-limit is within-agent — an agent incorporates external structure into its own $\Sigma_t$. Symbiogenesis is cross-agent — the grafted structure originates in another agent, and the integration is accompanied by that other agent's objective being absorbed. These are related but distinct: grafting is the structural-change mechanism on the host side; symbiogenesis is the bilateral process that includes grafting plus objective-absorption plus autonomy reduction.

**Rate-distortion interpretation (connecting to #unity-closure-mapping).** Under the Information Bottleneck conjecture in #unity-closure-mapping, peer coupling is IB compression with the relevance variable defined by a shared composite objective. Symbiogenesis is the process by which the relevance variable itself shifts: from two separate IB problems (each sub-agent's own survival objective) to a single IB problem (the composite's survival objective). The symbiogenic transition creates the shared relevance variable, which in turn makes the IB frontier well-defined for the composite. This is a structural shift in the IB problem, not a compression along a fixed IB frontier.

## Working Notes

- **Objective-transfer dynamics (S-1).** The most load-bearing open formalization. What process drives $O_e \to \mathcal D_e(O_h)$? Candidates: evolutionary selection (endosymbionts whose objectives align with host survival are selected for, since the alternative is extinction); bounded-rationality constraint (coordinating two divergent objectives exceeds the endosymbiont's capacity, forcing simplification); explicit design (firm mergers where acquired objectives are deliberately restructured). Each gives a different dynamical equation.
- **Function transfer $\mathcal F$ (S-2).** Needs to respect the structure of the host's $M_h$ and $\Sigma_h$. In biology, gene transfer preserves molecular functions but changes regulatory context. In social analogs, the analog is: functions are preserved, but their triggers and dependencies change. A general specification is open.
- **Autonomy reduction (S-3).** Why not complete? The endosymbiont retains some autonomy because complete integration would eliminate the fast local response capacity that made symbiogenesis advantageous in the first place. A cost-benefit analysis on autonomy retention (in the style of #strategy-complexity-cost) would make this quantitative.
- **Reverse symbiogenesis.** Endosymbionts occasionally regain autonomy (biological examples: some organelle-hosted genes return to the nucleus; organizational examples: acquired divisions spun off). Theoretically: the scope condition can be crossed in either direction. A composite that loses $U_O$ dissolves back into a multi-agent system. The triggering conditions and typical dynamics are open.
- **Interaction with logogenic agents.** In LLM-based agent architectures, multiple models can compose through shared training or through interface-specified protocols. Whether this constitutes symbiogenesis (with one model dominating) or peer coupling depends on whether the component models retain independent objectives. Worth investigating in `03-logogenic-agents/`.
- **Quantitative predictions.** When is symbiogenesis favored over peer coupling? Hypothesis: when the coordination overhead $C_{\text{coord}}$ between would-be peer-coupled agents exceeds the integration cost of symbiogenesis. Transaction-cost theory (Coase / Williamson) is the economic analog. The AAD version would connect $C_{\text{coord}}$ ( #tempo-composition) to the energetic or informational cost of maintaining separate objectives, with symbiogenesis favored when the latter exceeds the former.
- **Timescale of consolidation.** In biology, symbiogenesis takes evolutionary time (millions of years). In firms, months to years. In software/ideas, potentially much faster. The consolidation timescale $\tau_{\text{consolidated}}$ is domain-dependent; a general characterization is open.
