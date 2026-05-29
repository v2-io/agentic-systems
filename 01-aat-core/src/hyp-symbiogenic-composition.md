---
slug: hyp-symbiogenic-composition
type: hypothesis
status: robust-qualitative
depends:
  - scope-composite-agent
  - form-objective-functional
  - def-strategy-dimension
  - form-structural-change-as-parametric-limit
stage: draft
---

# Hypothesis: Symbiogenic Composition

Symbiogenesis is an asymmetric composition mechanism in which one agent (the *host*) integrates another (the *endosymbiont*) as a specialized sub-component, with the endosymbiont's objective gradually subsumed into the host's. It is distinct from peer coupling ( #form-composition-closure) and from population-level restructuring (the extreme transition motif drawn from Miller 2022, discussed in #result-structural-adaptation-necessity): symbiogenesis is how composite agents *come into existence* by crossing the #scope-composite-agent from below. The mechanism is well-attested empirically (eukaryote formation, firm mergers, legal-precedent adoption, language families) but formally underspecified within AAT. This segment captures the phenomenon and flags the specific formalization gaps.

## Formal Expression

*[Hypothesis (symbiogenic-composition)]*

Given two purposeful agents $A_h$ (host) and $A_e$ (endosymbiont), each satisfying #scope-agency, symbiogenic composition is a process on the joint state space with three coupled dynamics:

### (S-1) Objective absorption

The endosymbiont's objective $O_e$ transforms toward alignment with or derivation from the host's objective $O_h$:

$$O_e(\tau) \;\xrightarrow{\tau \to \tau_{\text{consolidated}}}\; \mathcal{D}_e(O_h)$$

where $\mathcal{D}_e$ is a derivation functional (in the sense of route (C-ii) in #scope-composite-agent): $O_e$ becomes a sub-objective derived from $O_h$. Before: $O_h$ and $O_e$ are independent objectives, no route of #scope-composite-agent applies, and the pair is a multi-agent system ( #scope-multi-agent) rather than a composite. After: $O_e$ is a role within $O_h$; route (C-ii) applies; the composite $(A_h, A_e)$ satisfies the composition scope condition.

### (S-2) Function transfer

Structural content from the endosymbiont's state (elements of $M_e$ or $\Sigma_e$) transfers to or becomes accessible by the host:

$$\{M_h, \Sigma_h\}(\tau) \;\xrightarrow{\tau \to \tau_{\text{consolidated}}}\; \{M_h, \Sigma_h\} \cup \mathcal{F}(M_e, \Sigma_e)$$

where $\mathcal{F}$ is a transfer mapping (structure-preserving integration of endosymbiont functions into host state). In biological symbiogenesis: gene transfer. In organizational symbiogenesis: acquired firm's processes, patents, know-how integrated into acquirer's operations. This is the grafting operation of #form-structural-change-as-parametric-limit in its cross-agent form — the host grafts structure originating in the endosymbiont.

### (S-3) Autonomy reduction

The endosymbiont's effective action space contracts; many of its choices become fixed by the host's coordination:

$$\mathcal{A}_e^{\text{effective}}(\tau) \;\xrightarrow{\tau \to \tau_{\text{consolidated}}}\; \mathcal{A}_e^{\text{restricted}} \subsetneq \mathcal{A}_e^{\text{initial}}$$

The endosymbiont retains enough autonomy to avoid catastrophic transfers (e.g., mitochondria retain some genome to handle local fast-timescale responses that would be hazardous to route through the host nucleus) but loses most independent decision-making.

### Integrated transition

At consolidation, the joint system is a single composite agent $A_c$ whose substate contains the integrated structure:

$$X_c = \big(M_c, G_c\big) = \big(M_h \cup \mathcal{F}(M_e, \Sigma_e),\; (O_c, \Sigma_c)\big) \quad \text{with } O_c \approx O_h$$

The endosymbiont persists as a specialized sub-component of the host, not as an independent agent. The #scope-composite-agent is now satisfied; the peer-coupling machinery of #form-composition-closure applies to the resulting composite.

## Epistemic Status

*Robust qualitative.* Max attainable: *robust qualitative* — the phenomenon is well-attested empirically across biological and social domains, but a general mathematical formalization within AAT is open.

What is well-established (externally):

- The existence of symbiogenesis as a distinct evolutionary mechanism (Mereschkowsky 1905, 1910; Sagan 1967; Margulis & Sagan 1997). Mitochondria and chloroplasts are the paradigm cases.
- The social analog in firms, technology, language, legal systems, religions (Miller 2022, Appendix B).
- "Innovation by parts" as qualitatively different from "innovation by sparks" (gradual mutation) — Miller's framing.

What is *not* derived within AAT:

- A formal model of the objective-transfer dynamics (S-1). What evolutionary or optimization process drives $O_e \to \mathcal{D}_e(O_h)$?
- A formal specification of the transfer functional $\mathcal{F}$ in (S-2). What structure is preserved, what is lost, what is transformed?
- A precise characterization of autonomy reduction (S-3). Why does the endosymbiont retain some autonomy rather than becoming fully deterministic?
- Quantitative predictions — e.g., when symbiogenesis is favored over peer coupling, what governs the timescale of consolidation, under what conditions it reverses.

The three dynamics (S-1), (S-2), (S-3) are proposed schemas, not results. A follow-up development of an AAT-specific dynamical model is the natural next step.

## Discussion

**The role of this mechanism in Part III.** Three distinct composition mechanisms are now in scope:

1. **Peer coupling** ( #form-composition-closure, #der-team-persistence, #der-tempo-composition) — sub-agents interact through shared environment; closure defect measures faithfulness of projection. Presumes scope-satisfaction via at least one route of #scope-composite-agent (not a scalar $U_O$ threshold).
2. **Extreme transition motif** (Miller 2022; introduced in #result-structural-adaptation-necessity; pending dedicated segments for composition-transition dynamics, latent structural diversity, and endogenous coupling) — population-level restructuring via neutral drift / niche creation / cascading displacement. $U_O$ shifts across a population as agent types replace one another.
3. **Symbiogenesis** (this segment) — hierarchical absorption. $U_O$ crosses the composition scope condition from below, creating a composite that did not previously exist.

Before symbiogenesis, the sub-agents were a multi-agent system ( #scope-multi-agent) but not a composite. After, the resulting composite is subject to all of AAT's composition machinery. The symbiogenic transition is the specific dynamical process of composite-agent identity creation.

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

**Connection to #form-structural-change-as-parametric-limit.** The single-agent "grafting" operation in #form-structural-change-as-parametric-limit is within-agent — an agent incorporates external structure into its own $\Sigma_t$. Symbiogenesis is cross-agent — the grafted structure originates in another agent, and the integration is accompanied by that other agent's objective being absorbed. These are related but distinct: grafting is the structural-change mechanism on the host side; symbiogenesis is the bilateral process that includes grafting plus objective-absorption plus autonomy reduction.

**Rate-distortion interpretation (connecting to #result-unity-closure-mapping).** Under the Information Bottleneck conjecture in #result-unity-closure-mapping, peer coupling is IB compression with the relevance variable defined by a shared composite objective. Symbiogenesis is the process by which the relevance variable itself shifts: from two separate IB problems (each sub-agent's own survival objective) to a single IB problem (the composite's survival objective). The symbiogenic transition creates the shared relevance variable, which in turn makes the IB frontier well-defined for the composite. This is a structural shift in the IB problem, not a compression along a fixed IB frontier.

## Working Notes

- **Objective-transfer dynamics (S-1).** The most load-bearing open formalization. What process drives $O_e \to \mathcal{D}_e(O_h)$? Candidates: evolutionary selection (endosymbionts whose objectives align with host survival are selected for, since the alternative is extinction); bounded-rationality constraint (coordinating two divergent objectives exceeds the endosymbiont's capacity, forcing simplification); explicit design (firm mergers where acquired objectives are deliberately restructured). Each gives a different dynamical equation.
- **Function transfer $\mathcal{F}$ (S-2).** Needs to respect the structure of the host's $M_h$ and $\Sigma_h$. In biology, gene transfer preserves molecular functions but changes regulatory context. In social analogs, the analog is: functions are preserved, but their triggers and dependencies change. A general specification is open.
- **Autonomy reduction (S-3).** Why not complete? The endosymbiont retains some autonomy because complete integration would eliminate the fast local response capacity that made symbiogenesis advantageous in the first place. A cost-benefit analysis on autonomy retention (in the style of #form-strategy-complexity-cost) would make this quantitative.
- **(S-3) as weighted-Lyapunov limit (sketch-level).** #deriv-critical-mass-composition's asymmetric limit $\alpha_2 \to 0$ under weighted Lyapunov $V_\mu(\xi) = \tfrac12(\lVert\delta_1\rVert^2 + \mu\lVert\delta_2\rVert^2)$ with $\mu \to 0$ formalizes (S-3): the endosymbiont's autonomous correction dynamics are weighted out of the joint stability argument, leaving the host's sector condition as the composite's persistence condition. This is a smooth deformation of the peer-coupling (CM4) inequality, not a discontinuous regime change — symbiogenesis and peer coupling are parameter-limits of the same weighted-Lyapunov analysis. The sketch is promotable to derived once (S-2) function transfer is formalized in this segment (the weighted Lyapunov limit does not address what happens to $M_h$ when structure from $M_e$ is inherited).
- **Reverse symbiogenesis.** Endosymbionts occasionally regain autonomy (biological examples: some organelle-hosted genes return to the nucleus; organizational examples: acquired divisions spun off). Theoretically: the scope condition can be crossed in either direction. A composite that loses $U_O$ dissolves back into a multi-agent system. The triggering conditions and typical dynamics are open.
- **Interaction with logogenic agents.** In LLM-based agent architectures, multiple models can compose through shared training or through interface-specified protocols. Whether this constitutes symbiogenesis (with one model dominating) or peer coupling depends on whether the component models retain independent objectives. Worth investigating in `03-llm-core/`.
- **Quantitative predictions.** When is symbiogenesis favored over peer coupling? Hypothesis: when the coordination overhead $C_{\text{coord}}$ between would-be peer-coupled agents exceeds the integration cost of symbiogenesis. Transaction-cost theory (Coase / Williamson) is the economic analog. The AAT version would connect $C_{\text{coord}}$ ( #der-tempo-composition) to the energetic or informational cost of maintaining separate objectives, with symbiogenesis favored when the latter exceeds the former.
- **Timescale of consolidation.** In biology, symbiogenesis takes evolutionary time (millions of years). In firms, months to years. In software/ideas, potentially much faster. The consolidation timescale $\tau_{\text{consolidated}}$ is domain-dependent; a general characterization is open.

- **Saddle-node bifurcation analysis — quantitative threshold form, conditional on a nonlinear coordination penalty.** Under the *hypothesis* that aggregate multi-agent mismatch $\delta$ obeys $\dot\delta = \rho_{\text{env}} - \alpha_{\text{auto}}\delta + k\delta^2$ with a nonlinear coordination penalty $+k\delta^2$ ($k \gt 0$) capturing compounding coordination failure between misaligned autonomous sub-agents, the steady-state fixed points $\delta^\ast = (\alpha_{\text{auto}} \pm \sqrt{\alpha_{\text{auto}}^2 - 4k\rho_{\text{env}}})/(2k)$ exist only for $\rho_{\text{env}} \le \rho_c := \alpha_{\text{auto}}^2/(4k)$. Above $\rho_c$ the two fixed points collide in a *saddle-node bifurcation* and disappear: $\dot\delta \gt 0$ everywhere, and the autonomous multi-agent system has no stable equilibrium. The symbiogenic escape route is structural: the composite merges sub-agent objectives and state ($\mu \to 0$), eliminating the coordination-penalty term and recovering linear dynamics on the merged state. The bifurcation analysis therefore predicts symbiogenesis as a *mathematically forced phase transition* at critical environmental volatility $\rho_c$ rather than as a contingent organizational choice. **Status: conditional on derivation of the $+k\delta^2$ coordination penalty from `#def-shared-intent`.** The $+k\delta^2$ form is currently stipulated rather than derived; making it rigorous requires showing that compounding coordination failure between agents with mismatch $\delta_A, \delta_B$ produces an aggregate-mismatch dynamics with this specific quadratic-in-$\delta$ structure under named conditions on the shared-intent quantity. Without that derivation, the threshold $\rho_c = \alpha_{\text{auto}}^2/(4k)$ is a *formulation*, not a theorem; with it, the threshold form is exact under the named hypothesis. The closed-negative result here — that the bifurcation derivation is conditional on a derivation step not yet attempted — is itself load-bearing: any future strengthening of `#hyp-symbiogenic-composition` from hypothesis-tier to derived-result-tier must produce the missing derivation of the coordination penalty from a more fundamental AAT construct (the natural candidate is shared-intent mutual information between sub-agent models $M_t^{(A)}$ and $M_t^{(B)}$ under coupled-evidence regimes).

- **Dynamic-regime placement (added 2026-05-21 per Phase 5 cross-segment ripple).** Symbiogenic absorption is the **canonical structural mechanism for the R1 → R0 transition** on the dynamic-regime axis (per `#disc-dynamic-regime-axis` §"Transition asymmetry: descent is the default, ascent costs more"): pre-absorption, the composite operates in R1 equilibrium-regime under partially-opposing objectives between host and endosymbiont; post-absorption, the merged composite operates in R0 contraction-regime under the unified objective surface, with the (CM2) closed-form of `#deriv-critical-mass-composition` applying at the asymmetric-parameter limit. Symbiogenesis is therefore the self-driven *ascending* move on the dynamic-regime axis — paying the structural cost of objective-merger to exit the equilibrium-regime failure modes (saddle-Nash, multi-equilibria, last-iterate non-convergence) for the R0 contraction-regime guarantees. The saddle-node bifurcation analysis above ($\rho_c$ threshold) is what makes the ascent *forced* rather than optional above critical environmental volatility.

- **Track E surface-back of catalog citations (2026-05-22) — Szathmáry 2015 major-transitions framework.** Adjacent literature surfaced 2026-05-22 from Track E catalog at `ref/prior-art-analysis/08-composite-agency.md` (Pillar 3): Szathmáry, E. (2015), *Toward major evolutionary transitions theory 2.0* (PNAS 112:10104)[^cat-2026-05-22]. Substantial conceptual ancestry for the symbiogenic-absorption mechanism this segment formalizes: Szathmáry's major-evolutionary-transitions (MET) framework names lower-level units becoming constrained by a higher-level unit, with progressively-reduced autonomy and "de-Darwinized" sub-units — exactly the asymmetric-parameter-limit structure (CM2)'s closed form formalizes mathematically. AAT does not claim to have discovered asymmetric absorption; the contribution is the *mathematical form* (the asymmetric-parameter limit reading of `#deriv-critical-mass-composition` + the dynamic-regime-axis R1 → R0 transition reading) that makes the symbiogenic process predictable rather than purely empirical. Other named conceptual ancestors (Maynard Smith & Szathmáry 1995 *The Major Transitions in Evolution*, Cambridge; Margulis 1981 *Symbiosis in Cell Evolution* — the canonical biological instance) are textbook/well-known and inherited from general scientific literacy rather than catalog-attributed.

[^cat-2026-05-22]: Citation surfaced 2026-05-22 from the Track E catalog at `ref/prior-art-analysis/` (intermediate work artifacts that captured Pillar-style prior-art searches). Catalog has more verification support than raw Undermind synthesis but less than full primary-source reading. Verification queued with the BG2 cluster — see `#disc-identifiability-floor` Working Notes for the verification-targets list.
