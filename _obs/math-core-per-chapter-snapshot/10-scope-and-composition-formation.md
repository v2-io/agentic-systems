# Scope and Composition Formation


## Scope: Multi-Agent Scope

- **Slug**: `scope-multi-agent`
- **Type**: scope
- **Status**: axiomatic
- **Stage**: draft
- **Depends**: `scope-agency`, `post-composition-consistency`

Section III applies wherever multiple agents satisfying the scope condition interact through a shared environment. Each agent observes, acts, and faces uncertainty; their actions affect each other's environments. This is the general case for organizations, teams, ecosystems, and adversarial encounters. Independence (agents whose actions don't affect each other) is the special case requiring justification.

*[Scope (multi-agent-scope)]*

A multi-agent system consists of $N$ agents $\{A_1, \ldots, A_n\}$, each satisfying the scope condition ( #scope-agency), interacting through a shared environment with state $\Omega_t \in \mathcal{S}_{env}$:

- Each agent $A_i$ has state $X_t^{(i)} = (M_t^{(i)}, G_t^{(i)})$
- Each agent observes: $o_t^{(i)} = h^{(i)}(\Omega_t, a_t^{(\neg i)}, \xi_t^{(i)})$ — observations may depend on other agents' actions
- Each agent acts: $a_t^{(i)} = \pi^{(i)}(X_t^{(i)})$
- The environment evolves: $\Omega_{t+1} = T(\Omega_t, a_t^{(1)}, \ldots, a_t^{(n)}, \omega_t)$

The coupling is through the environment: agent $i$'s actions enter agent $j$'s observation function and the shared environment transition. Agents may also communicate directly (a special case of action-observation coupling with a dedicated channel).

### Observation decomposition and routing

*[Definition (observation-decomposition)]*

Each agent's observation decomposes into environmental and inter-agent components:

$$o_t^{(i)} = \left(o_{\text{env},t}^{(i)},\; \{m_{ji,t}\}_{j \in \mathcal N_t(i)}\right)$$

where:
- $o_{\text{env},t}^{(i)} = h_\text{env}^{(i)}(\Omega_t, \xi_t^{(i)})$: direct environmental observation (no inter-agent content)
- $\mathcal N_t(i) \subseteq \{1, \ldots, N\} \setminus \{i\}$: the **communication neighborhood** — which agents send messages to $i$ at time $t$
- $m_{ji,t} = c_t^{(j \to i)}(X_t^{(j)})$: message from $j$ to $i$, determined by the sender's full state and the communication protocol

*[Definition (multi-agent-routing-structure)]*

The **multi-agent routing structure** $R_t = (\mathcal N_t, \{c_t^{(j \to i)}\})$ specifies:
- The **topology** $\mathcal N_t$: who communicates with whom
- The **protocol** $c_t^{(j \to i)}$: the rule governing what class of information flows from $j$ to $i$

Note: the protocol $c_t^{(j \to i)}$ is a *rule* specifying the channel, not the specific content of any message. Individual messages reflect the sender's state $X_t^{(j)}$ — including their individual goals — through the sender's policy. What the routing structure governs is the *infrastructure*: which channels exist and what kind of information they carry. *Bare-prose shorthand: the term "routing structure" is sanctioned within this segment after the first compound-form introduction; cross-segment citation should use the full "multi-agent routing structure" form.*

*[Definition (goal-blind-routing)]*

Routing is **goal-blind** when neither the topology nor the protocol depends on the composite's goal state:

$$\mathcal N_t \perp G_t^c \qquad \text{and} \qquad c_t^{(j \to i)} \perp G_t^c \quad \forall\, j, i$$

This means the communication infrastructure does not change based on what the composite is trying to achieve. Individual messages naturally reflect individual agents' goals through their policies — this is action, not routing. The routing condition is about the *structure* of information flow, not the *content* of individual messages.

**Goal-dependent routing** occurs when either the topology or the protocol varies with $G_t^c$. Examples: activating crisis-specific communication channels, changing intelligence-sharing protocols based on the current mission, reassigning reporting chains based on the operational objective.

---



## Scope: Composite Agent

- **Slug**: `scope-composite-agent`
- **Type**: scope
- **Status**: robust-qualitative
- **Stage**: draft
- **Depends**: `scope-agency`, `scope-multi-agent`, `form-objective-functional`

A set of purposeful sub-agents, each satisfying #scope-agency, constitutes a *composite agent* only when their objectives exhibit sufficient teleological alignment to define a coherent composite purpose. Without this condition, the sub-agents form a multi-agent system ( #scope-multi-agent) that may still be analyzed — but the machinery of composition (closure defect, team persistence, composite tempo) does not apply because there is no composite agent whose quantities to compute. This parallels the single-agent #scope-agency: before asking how an agent adapts, one must check that an agent is present.

*[Scope (scope-composite-agent)]*

Given sub-agents $\{A_1, \ldots, A_N\}$ each satisfying #scope-agency, they constitute a *composite agent* iff there exists a common objective structure under at least one of the following routes:

### (C-i) Shared composite objective

There exists $O_c$ such that each sub-agent's effective policy is $\epsilon$-compatible with $O_c$-optimal:

$$\exists\, O_c : \;\forall i,\; D\big(\pi_i,\; \pi^{O_c}_i\big) \leq \epsilon$$

where $\pi^{O_c}_i$ is sub-agent $i$'s optimal policy under the shared objective and $D$ is an appropriate policy divergence. Strongest route; the sub-agents are all optimizing for the same thing, possibly with local decompositions.

### (C-ii) Hierarchical derivation

There exists a parent objective $O_c$ from which sub-objectives $\{O_i\}$ are derivable by decomposition consistent with #post-composition-consistency:

$$\{O_i\} = \mathcal D(O_c)$$

where $\mathcal D$ is a structure-preserving decomposition. Each sub-agent optimizes its own $O_i$, but all $O_i$ trace back to $O_c$. Military chain of command; corporate department structure. Sub-agents may not individually know $O_c$.

### (C-iii) Mutual-benefit alignment

There exists a relevance variable $Y$ such that the sub-agents' joint actions raise $\mathbb E[Y]$ above the non-cooperation baseline for each sub-agent:

$$\exists\, Y : \;\forall i,\; \mathbb E[Y \mid \text{joint}] \gt \mathbb E[Y \mid \text{non-coop}]$$

Weakest route. No explicit common objective, but interactions are positive-sum in some dimension. Symbiotic coexistence; commensal ecologies; trading partners who share no goals beyond mutual benefit.

### (C-iv) Equilibrium-convergent strategic interaction

There exists an equilibrium concept $\mathcal E$ (Nash, correlated, or coarse correlated) such that coupled best-response dynamics of $\{A_i\}$ converge to (or cycle within the support of) $\mathcal E$:

$$\exists\, \mathcal E : \; \text{coupled best-response dynamics converge to the support of } \mathcal E.$$

Qualitatively distinct from (C-i)–(C-iii): requires neither shared objectives, nor hierarchical derivation, nor mutual benefit. Requires only **structural convergence** of the strategic interaction in the game-theoretic sense. The sub-agents' objectives may be partially opposing, but the interaction admits a stable joint behaviour. Composites satisfying (C-iv) are **strategic composites**, distinguished from alignment composites (C-i, C-ii) and mutual-benefit composites (C-iii). The composite's macro-state is defined relative to the equilibrium structure $\mathcal E$ rather than relative to a shared target state. See `#deriv-strategic-composition` for the A2'-analog transfer of `#result-sector-persistence-template` under potential-game (Monderer-Shapley 1996) or monotone-game (Rosen 1965) conditions, the (SC-1)–(SC-3) existence/stability/convergence decomposition, and the honest sub-scope $\beta'$ scope exit for non-potential non-monotone games (VI existence + regret-minimization CCE set-convergence only).

### Disjunctive form

*[Scope (scope-composite-agent, disjunctive)]*

The scope condition is satisfied when **any** of (C-i), (C-ii), (C-iii), or (C-iv) applies. (C-i)–(C-iii) are progressively weaker qualitative requirements for what "teleological alignment sufficient to define a coherent composite purpose" means; (C-iv) covers strategic interaction with partially-opposing objectives via equilibrium convergence rather than alignment. The routes are *not* shown to reduce to a common scalar threshold. Each route carries its own operationalization and its own $N$-agent aggregation:

- (C-i) uses a value-function divergence $D(\pi_i, \pi^{O_c}_i)$ aggregated across sub-agents.
- (C-ii) uses decomposition consistency of a parent objective $O_c$ — a structural check, not a scalar.
- (C-iii) uses the existence of a relevance variable on which each sub-agent's marginal contribution is positive — a per-pair existential check, not a magnitude.
- (C-iv) uses existence of an equilibrium structure $\mathcal E$ under coupled best-response dynamics — a fixed-point check (Nash / VI / regret-minimization CCE), structurally distinct from the alignment checks in (C-i)–(C-iii).

The teleological unity measure $U_O$ from #def-unity-dimensions (pairwise value-correlation aggregated to the group) tracks one projection of alignment — primarily route (C-i) — but is not a reduction of all three routes to a single scalar. Downstream segments ( #result-unity-closure-mapping, #hyp-symbiogenic-composition, #der-team-persistence) describe quality *conditional on scope-satisfaction* without assuming a common threshold: they presume the scope condition holds via at least one route, then analyze composite quantities within that regime.

(C-i) gives the strongest alignment; (C-iii) gives the weakest that still qualifies. A composite may satisfy multiple routes simultaneously; only one is required for scope.

**What fails the scope condition:** sub-agents with orthogonal objectives that also fail to admit equilibrium convergence — no shared or derivable $O_c$, no relevance variable providing mutual benefit, and no equilibrium concept (pure Nash, mixed Nash, or CCE) whose support the coupled best-response or no-regret dynamics reach — or unclassifiable objective-structure coupling. Such systems remain within #scope-multi-agent but not #scope-composite-agent. Adversarial pairs that admit equilibrium convergence via (C-iv) — whether pure-strategy Nash under $\alpha'$ (potential / monotone games), mixed Nash under $\beta'$ (Nash 1950 existence for finite games), or CCE in distribution under $\beta'$ (Hart-Mas-Colell 2000) — DO satisfy composition-scope-condition as strategic composites. Cyclic games (rock-paper-scissors, matching pennies) lack a pure-strategy Nash but admit mixed Nash and CCE convergence; they fall within $\beta'$ and satisfy (C-iv). The narrow category that fails (C-iv) is games with no equilibrium concept whose support is reachable by any admissible dynamic — a genuinely small class within the standard game-theoretic landscape.

---



## Hypothesis: Symbiogenic Composition

- **Slug**: `hyp-symbiogenic-composition`
- **Type**: hypothesis
- **Status**: robust-qualitative
- **Stage**: draft
- **Depends**: `scope-composite-agent`, `form-objective-functional`, `def-strategy-dimension`, `form-structural-change-as-parametric-limit`

Symbiogenesis is an asymmetric composition mechanism in which one agent (the *host*) integrates another (the *endosymbiont*) as a specialized sub-component, with the endosymbiont's objective gradually subsumed into the host's. It is distinct from peer coupling ( #form-composition-closure) and from population-level restructuring (the extreme transition motif drawn from Miller 2022, discussed in #result-structural-adaptation-necessity): symbiogenesis is how composite agents *come into existence* by crossing the #scope-composite-agent from below. The mechanism is well-attested empirically (eukaryote formation, firm mergers, legal-precedent adoption, language families) but formally underspecified within AAT. This segment captures the phenomenon and flags the specific formalization gaps.

*[Hypothesis (symbiogenic-composition)]*

Given two purposeful agents $A_h$ (host) and $A_e$ (endosymbiont), each satisfying #scope-agency, symbiogenic composition is a process on the joint state space with three coupled dynamics:

### (S-1) Objective absorption

The endosymbiont's objective $O_e$ transforms toward alignment with or derivation from the host's objective $O_h$:

$$O_e(\tau) \;\xrightarrow{\tau \to \tau_{\text{consolidated}}}\; \mathcal D_e(O_h)$$

where $\mathcal D_e$ is a derivation functional (in the sense of route (C-ii) in #scope-composite-agent): $O_e$ becomes a sub-objective derived from $O_h$. Before: $O_h$ and $O_e$ are independent objectives, no route of #scope-composite-agent applies, and the pair is a multi-agent system ( #scope-multi-agent) rather than a composite. After: $O_e$ is a role within $O_h$; route (C-ii) applies; the composite $(A_h, A_e)$ satisfies the composition scope condition.

### (S-2) Function transfer

Structural content from the endosymbiont's state (elements of $M_e$ or $\Sigma_e$) transfers to or becomes accessible by the host:

$$\{M_h, \Sigma_h\}(\tau) \;\xrightarrow{\tau \to \tau_{\text{consolidated}}}\; \{M_h, \Sigma_h\} \cup \mathcal F(M_e, \Sigma_e)$$

where $\mathcal F$ is a transfer mapping (structure-preserving integration of endosymbiont functions into host state). In biological symbiogenesis: gene transfer. In organizational symbiogenesis: acquired firm's processes, patents, know-how integrated into acquirer's operations. This is the grafting operation of #form-structural-change-as-parametric-limit in its cross-agent form — the host grafts structure originating in the endosymbiont.

### (S-3) Autonomy reduction

The endosymbiont's effective action space contracts; many of its choices become fixed by the host's coordination:

$$\mathcal A_e^{\text{effective}}(\tau) \;\xrightarrow{\tau \to \tau_{\text{consolidated}}}\; \mathcal A_e^{\text{restricted}} \subsetneq \mathcal A_e^{\text{initial}}$$

The endosymbiont retains enough autonomy to avoid catastrophic transfers (e.g., mitochondria retain some genome to handle local fast-timescale responses that would be hazardous to route through the host nucleus) but loses most independent decision-making.

### Integrated transition

At consolidation, the joint system is a single composite agent $A_c$ whose substate contains the integrated structure:

$$X_c = \big(M_c, G_c\big) = \big(M_h \cup \mathcal F(M_e, \Sigma_e),\; (O_c, \Sigma_c)\big) \quad \text{with } O_c \approx O_h$$

The endosymbiont persists as a specialized sub-component of the host, not as an independent agent. The #scope-composite-agent is now satisfied; the peer-coupling machinery of #form-composition-closure applies to the resulting composite.

---
