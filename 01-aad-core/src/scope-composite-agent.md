---
slug: scope-composite-agent
type: scope
status: robust-qualitative
depends:
  - scope-agency
  - multi-agent-scope
  - objective-functional
stage: draft
---

# Scope: Composite Agent

A set of purposeful sub-agents, each satisfying #scope-agency, constitutes a *composite agent* only when their objectives exhibit sufficient teleological alignment to define a coherent composite purpose. Without this condition, the sub-agents form a multi-agent system ( #multi-agent-scope) that may still be analyzed — but the machinery of composition (closure defect, team persistence, composite tempo) does not apply because there is no composite agent whose quantities to compute. This parallels the single-agent #scope-agency: before asking how an agent adapts, one must check that an agent is present.

## Formal Expression

*[Scope (scope-composite-agent)]*

Given sub-agents $\{A_1, \ldots, A_N\}$ each satisfying #scope-agency, they constitute a *composite agent* iff there exists a common objective structure under at least one of the following routes:

### (C-i) Shared composite objective

There exists $O_c$ such that each sub-agent's effective policy is $\epsilon$-compatible with $O_c$-optimal:

$$\exists\, O_c : \;\forall i,\; D\big(\pi_i,\; \pi^{O_c}_i\big) \leq \epsilon$$

where $\pi^{O_c}_i$ is sub-agent $i$'s optimal policy under the shared objective and $D$ is an appropriate policy divergence. Strongest route; the sub-agents are all optimizing for the same thing, possibly with local decompositions.

### (C-ii) Hierarchical derivation

There exists a parent objective $O_c$ from which sub-objectives $\{O_i\}$ are derivable by decomposition consistent with #postulate-composition-consistency:

$$\{O_i\} = \mathcal D(O_c)$$

where $\mathcal D$ is a structure-preserving decomposition. Each sub-agent optimizes its own $O_i$, but all $O_i$ trace back to $O_c$. Military chain of command; corporate department structure. Sub-agents may not individually know $O_c$.

### (C-iii) Mutual-benefit alignment

There exists a relevance variable $Y$ such that the sub-agents' joint actions raise $\mathbb E[Y]$ above the non-cooperation baseline for each sub-agent:

$$\exists\, Y : \;\forall i,\; \mathbb E[Y \mid \text{joint}] \gt \mathbb E[Y \mid \text{non-coop}]$$

Weakest route. No explicit common objective, but interactions are positive-sum in some dimension. Symbiotic coexistence; commensal ecologies; trading partners who share no goals beyond mutual benefit.

### (C-iv) Equilibrium-convergent strategic interaction

There exists an equilibrium concept $\mathcal E$ (Nash, correlated, or coarse correlated) such that coupled best-response dynamics of $\{A_i\}$ converge to (or cycle within the support of) $\mathcal E$:

$$\exists\, \mathcal E : \; \text{coupled best-response dynamics converge to the support of } \mathcal E.$$

Qualitatively distinct from (C-i)–(C-iii): requires neither shared objectives, nor hierarchical derivation, nor mutual benefit. Requires only **structural convergence** of the strategic interaction in the game-theoretic sense. The sub-agents' objectives may be partially opposing, but the interaction admits a stable joint behaviour. Composites satisfying (C-iv) are **strategic composites**, distinguished from alignment composites (C-i, C-ii) and mutual-benefit composites (C-iii). The composite's macro-state is defined relative to the equilibrium structure $\mathcal E$ rather than relative to a shared target state. See `#strategic-composition` for the A2'-analog transfer of `#sector-persistence-template` under potential-game (Monderer-Shapley 1996) or monotone-game (Rosen 1965) conditions, the (SC-1)–(SC-3) existence/stability/convergence decomposition, and the honest sub-scope $\beta'$ scope exit for non-potential non-monotone games (VI existence + regret-minimization CCE set-convergence only).

### Disjunctive form

*[Scope (scope-composite-agent, disjunctive)]*

The scope condition is satisfied when **any** of (C-i), (C-ii), (C-iii), or (C-iv) applies. (C-i)–(C-iii) are progressively weaker qualitative requirements for what "teleological alignment sufficient to define a coherent composite purpose" means; (C-iv) covers strategic interaction with partially-opposing objectives via equilibrium convergence rather than alignment. The routes are *not* shown to reduce to a common scalar threshold. Each route carries its own operationalization and its own $N$-agent aggregation:

- (C-i) uses a value-function divergence $D(\pi_i, \pi^{O_c}_i)$ aggregated across sub-agents.
- (C-ii) uses decomposition consistency of a parent objective $O_c$ — a structural check, not a scalar.
- (C-iii) uses the existence of a relevance variable on which each sub-agent's marginal contribution is positive — a per-pair existential check, not a magnitude.
- (C-iv) uses existence of an equilibrium structure $\mathcal E$ under coupled best-response dynamics — a fixed-point check (Nash / VI / regret-minimization CCE), structurally distinct from the alignment checks in (C-i)–(C-iii).

The teleological unity measure $U_O$ from #definition-unity-dimensions (pairwise value-correlation aggregated to the group) tracks one projection of alignment — primarily route (C-i) — but is not a reduction of all three routes to a single scalar. Downstream segments ( #unity-closure-mapping, #symbiogenic-composition, #team-persistence) describe quality *conditional on scope-satisfaction* without assuming a common threshold: they presume the scope condition holds via at least one route, then analyze composite quantities within that regime.

(C-i) gives the strongest alignment; (C-iii) gives the weakest that still qualifies. A composite may satisfy multiple routes simultaneously; only one is required for scope.

**What fails the scope condition:** sub-agents with orthogonal objectives that also fail to admit equilibrium convergence (no shared or derivable $O_c$, no relevance variable providing mutual benefit, no equilibrium structure the strategic dynamics converge to — e.g., cyclic games with no pure Nash), or unclassifiable objective-structure coupling. Such systems remain within #multi-agent-scope but not #scope-composite-agent. Adversarial pairs that admit Nash / CCE convergence via (C-iv) DO satisfy composition-scope-condition as strategic composites; adversarial pairs in cyclic / non-convergent regimes do not.

## Epistemic Status

*Robust-qualitative.* Max attainable: *robust-qualitative*. The composite-agent scope is a structural proposal paralleling the single-agent scopes ( #scope-adaptive-system and #scope-agency, both axiomatic — the minimal conditions for adaptive and purposeful machinery to be non-vacuous). Unlike them, #scope-composite-agent is a theoretical choice: we could admit teleologically misaligned groups as composites (via the closure-defect framework alone) and separately track whether their composite objective is meaningful. The proposal here is that this separate tracking is better done as a scope restriction: composition quantities are defined for systems satisfying at least one of (C-i)–(C-iv), not for systems satisfying none.

The three alternative routes are not exhaustive but cover the well-understood cases. The relationship between the routes (whether they partition or overlap) and whether there is a single underlying scalar that reduces them all is open; the disjunctive form above is chosen because no such reduction has been demonstrated.

## Discussion

**Why this is a scope condition, not merely a quality metric.** The existing #composition-closure framework treats any group admitting a low-$\varepsilon^\ast$ projection as a composite. This is mechanically defensible but runs into a category problem: a composite's purposeful substate $G_c = (O_c, \Sigma_c)$ requires a well-defined composite objective $O_c$. If the sub-agents' objectives do not align under any common $O_c$, then $G_c$ is ill-defined and the composite is a fiction. Closure defect can be computed (as a projection property), but calling the result a "composite agent" strains the term. Making this a scope condition resolves the category issue: composition applies where $G_c$ is well-defined.

**Relationship to the single-agent scopes.** The parallel is tight. The single-agent scopes ( #scope-adaptive-system + #scope-agency) together say: before asking whether an agent persists, check that it is an agent (it observes under residual uncertainty, and at least one action has causal effect). #scope-composite-agent says: before asking whether a composite persists, check that it is a composite (teleological alignment sufficient to define $O_c$). In both cases, the scope precedes the quantitative machinery.

**Relationship to #definition-unity-dimensions.** $U_O$ in #definition-unity-dimensions has a dual role: (i) scope tracking — primarily the (C-i) route, where value-correlation is the operationalization; (ii) quality parameter for action-closure $\varepsilon_a$, via #unity-closure-mapping. The two roles are not in tension, but they are also not identical across routes: scope-satisfaction via (C-ii) or (C-iii) does not directly correspond to a $U_O$ value, so $U_O$ is best read as a quality metric *conditional on scope*, not as the defining scope variable.

**Three routes, qualitatively ordered.** The three routes (C-i), (C-ii), (C-iii) differ in how directly the sub-agents share purpose. They are progressively weaker qualitative requirements — (C-i) strongest, (C-iii) weakest — but they are not shown to reduce to a single scalar. (C-i) uses value-correlation directly; (C-ii) uses hierarchical decomposition consistency; (C-iii) uses marginal benefit existence. A composite can satisfy multiple routes simultaneously (a well-aligned team satisfies both (C-i) and (C-ii)); what matters for scope is that at least one route holds.

**Miller's IAM definition.** Miller (2022, *Ex Machina*, Ch 1) proposes that social behavior requires Interaction, Agency, and Mutual benefit (IAM). The mutual-benefit requirement in (C-iii) is the AAD analog of Miller's third element. Miller treats IAM as the definition of social behavior; the proposal here treats alignment as the scope condition for composite-agent analysis. The two align substantively: Miller's mutual benefit is a minimum teleological unity.

**Multi-agent systems with and without composite status.** Adversarial pairs partition along a finer line than alignment / non-alignment. Adversarial pairs that admit equilibrium convergence (potential or monotone strategic games per `#strategic-composition`) satisfy the scope condition via (C-iv) as strategic composites; adversarial pairs in cyclic or non-convergent regimes do not satisfy any of (C-i)–(C-iv) and remain within `#multi-agent-scope` only. The asymmetric case — one agent as exogenous attacker, one as target — is a `#multi-agent-scope` phenomenon handled by `#adversarial-destabilization`; it does not form a composite in either (C-i)–(C-iii) or (C-iv) senses because the attacker is treated as a parameter rather than a sub-agent running its full AAD loop. Symmetric strategic composition under partially-opposing objectives is covered by (C-iv) and forms a strategic composite with equilibrium-based macro-state.

**Load-bearing enabling role under `#discussion-identifiability-floor` Instance 3.** The composition-layer identifiability-floor instance establishes a no-go: composite contraction $\kappa_c > 0$ is not in general certifiable from component-level data alone — the coupling-sign bit distinguishing cooperative from adversarial regimes is unidentifiable from component marginals. Four structural escapes are available (observable coupling topology; matched Tier at composite level; passivity certificate; common contraction metric). Scope-satisfaction via at least one of (C-i)–(C-iv) in this segment is the **enabling condition** for any of these escapes: without scope-satisfaction, the "composite" is ill-defined ($O_c$ does not exist under (C-i)–(C-iii); equilibrium structure $\mathcal E$ does not exist under (C-iv); $R_c$ is ill-typed), and the escapes have no coherent target to certify. The scope condition is therefore load-bearing apparatus that the composition-layer floor depends on — scope-satisfaction is what distinguishes a composite whose contraction or equilibrium convergence can be certified (under some escape) from a multi-agent system whose "composite contraction" is not a well-defined object.

**How composites come into being: symbiogenesis.** The formal mechanism by which a group passes from failing all three routes to satisfying at least one is described in #symbiogenic-composition. Briefly: in biological and social symbiogenesis, a host integrates an endosymbiont; the endosymbiont's objective is subsumed into the host's; the combined entity's objective $O_c$ emerges where two independent objectives stood. After the transition, (C-ii) applies: the endosymbiont's objective is a sub-objective of $O_c$. This is the dynamical process of composite-agent identity creation; the scope condition here describes its result.

## Working Notes

- **Whether a common scalar exists.** The current form treats the three routes as a disjunction of qualitatively distinct conditions rather than as instances of a unified threshold. Whether there is a single scalar that reduces all three — and whether such a scalar would have a phase-transition structure (a sharp threshold beyond which composite analysis becomes well-posed) — is open. If such a scalar exists, $U_O$ is one candidate but covers only (C-i) directly; (C-ii) and (C-iii) would require separate operationalization and then an aggregation across routes.
- **Asymmetric unity.** Routes (C-i) and (C-ii) implicitly assume symmetric alignment (sub-agents equally represented in $O_c$). Symbiogenesis, firm acquisitions, and hierarchical delegation all feature *asymmetric* unity (host dominates; endosymbiont subordinate). The scope condition should accommodate asymmetric alignment; the current (C-ii) hierarchical form partially covers it, but an explicit treatment of role-asymmetric composites is open.
- **Interaction with Class 2 (fully merged) architectures.** #directed-separation's architectural classification (Class 1 modular, Class 2 fully merged, Class 3 partial) applies to individual agents. Composites of Class 2 agents — e.g., multi-LLM systems — may satisfy this scope condition via shared training rather than shared explicit objective. Whether (C-i)-(C-iii) cover this adequately, or whether a fourth route for implicit alignment is needed, is open.
- **Transitivity.** If $A_1, A_2$ align and $A_2, A_3$ align, do $A_1, A_3$? Probably yes via (C-ii) if there is a common parent; not necessarily via (C-i) without a shared objective. Transitivity would make composite formation more robust; non-transitivity would explain why coalition-building requires explicit alignment work.
- **Promotion dependencies.** Before `claims-verified`: settle whether the three routes reduce to a common scalar or remain an honest disjunction (first bullet); audit whether any existing Section III segment implicitly assumes this scope without naming it (likely yes for team-persistence, tempo-composition, closure-based results) and update each to reference #scope-composite-agent for scope-satisfaction explicitly.
