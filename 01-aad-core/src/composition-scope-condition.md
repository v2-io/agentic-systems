---
slug: composition-scope-condition
type: scope
status: robust-qualitative
depends:
  - scope-condition
  - multi-agent-scope
  - objective-functional
stage: draft
---

# Scope: Composition Scope Condition

A set of purposeful sub-agents, each satisfying #scope-condition, constitutes a *composite agent* only when their objectives exhibit sufficient teleological alignment to define a coherent composite purpose. Without this condition, the sub-agents form a multi-agent system ( #multi-agent-scope) that may still be analyzed — but the machinery of composition (closure defect, team persistence, composite tempo) does not apply because there is no composite agent whose quantities to compute. This parallels the single-agent #scope-condition: before asking how an agent adapts, one must check that an agent is present.

## Formal Expression

*[Scope (composition-scope-condition)]*

Given sub-agents $\{A_1, \ldots, A_N\}$ each satisfying #scope-condition at agency level, they constitute a *composite agent* iff there exists a common objective structure under at least one of the following routes:

### (C-i) Shared composite objective

There exists $O_c$ such that each sub-agent's effective policy is $\epsilon$-compatible with $O_c$-optimal:

$$\exists\, O_c : \;\forall i,\; D\big(\pi_i,\; \pi^{O_c}_i\big) \leq \epsilon$$

where $\pi^{O_c}_i$ is sub-agent $i$'s optimal policy under the shared objective and $D$ is an appropriate policy divergence. Strongest route; the sub-agents are all optimizing for the same thing, possibly with local decompositions.

### (C-ii) Hierarchical derivation

There exists a parent objective $O_c$ from which sub-objectives $\{O_i\}$ are derivable by decomposition consistent with #composition-consistency:

$$\{O_i\} = \mathcal D(O_c)$$

where $\mathcal D$ is a structure-preserving decomposition. Each sub-agent optimizes its own $O_i$, but all $O_i$ trace back to $O_c$. Military chain of command; corporate department structure. Sub-agents may not individually know $O_c$.

### (C-iii) Mutual-benefit alignment

There exists a relevance variable $Y$ such that the sub-agents' joint actions raise $\mathbb E[Y]$ above the non-cooperation baseline for each sub-agent:

$$\exists\, Y : \;\forall i,\; \mathbb E[Y \mid \text{joint}] \gt \mathbb E[Y \mid \text{non-coop}]$$

Weakest route. No explicit common objective, but interactions are positive-sum in some dimension. Symbiotic coexistence; commensal ecologies; trading partners who share no goals beyond mutual benefit.

### Unified form

All three routes express a single underlying requirement: *teleological alignment sufficient to define a coherent composite purpose*. The teleological unity measure $U_O$ introduced in #unity-dimensions provides a convenient unified scalar — the scope condition can be restated as $U_O \geq \epsilon_{\text{comp}}$ for an appropriate route-dependent operationalization. (C-i) gives the strongest alignment; (C-iii) gives the weakest that still qualifies.

**What fails the scope condition:** sub-agents with orthogonal objectives (no shared or derivable $O_c$, no relevance variable providing mutual benefit), adversarial objectives (actively opposed purposes), or unclassifiable objective-structure coupling. Such systems remain within #multi-agent-scope but not #composition-scope-condition.

## Epistemic Status

*Robust-qualitative.* Max attainable: *robust-qualitative*. The scope condition is a structural proposal paralleling #scope-condition. Unlike the single-agent scope condition (which is axiomatic — the minimal conditions for adaptive machinery to be non-vacuous), the composition scope condition is a theoretical choice: we could admit low-$U_O$ groups as composites (via the closure-defect framework alone) and separately track whether their composite objective is meaningful. The proposal here is that this separate tracking is better done as a scope restriction: composition quantities are defined for systems above the threshold, not defined for systems below it.

The three alternative routes are not exhaustive but cover the well-understood cases. Practical $\epsilon_{\text{comp}}$ thresholds, and the relationship between the routes (whether they partition or overlap), are open.

Full discussion of the motivation and consequences: `msc/spike-symbiogenic-composition.md`.

## Discussion

**Why this is a scope condition, not merely a quality metric.** The existing #composition-closure framework treats any group admitting a low-$\varepsilon^\ast$ projection as a composite. This is mechanically defensible but runs into a category problem: a composite's purposeful substate $G_c = (O_c, \Sigma_c)$ requires a well-defined composite objective $O_c$. If the sub-agents' objectives do not align under any common $O_c$, then $G_c$ is ill-defined and the composite is a fiction. Closure defect can be computed (as a projection property), but calling the result a "composite agent" strains the term. Making this a scope condition resolves the category issue: composition applies where $G_c$ is well-defined.

**Relationship to #scope-condition.** The parallel is tight. #scope-condition says: before asking whether an agent persists, check that it is an agent (observations exist, uncertainty persists, actions have effects). #composition-scope-condition says: before asking whether a composite persists, check that it is a composite (teleological alignment sufficient to define $O_c$). In both cases, the scope condition precedes the quantitative machinery.

**Relationship to #unity-dimensions.** $U_O$ in #unity-dimensions has a dual role: (i) scope condition for composition to exist, via this segment's threshold; (ii) quality parameter for action-closure $\varepsilon_a$, via #unity-closure-mapping. The two roles are not in tension: once the scope threshold is crossed, further variation in $U_O$ modulates action-compressibility. Below the threshold, composition does not apply and the "quality" role is vacuous.

**Three routes, one condition.** The three routes (C-i), (C-ii), (C-iii) differ in how directly the sub-agents share purpose. All satisfy the same underlying requirement — $U_O \geq \epsilon_{\text{comp}}$ — but under different operationalizations of $U_O$. (C-i) uses value-correlation directly; (C-ii) uses hierarchical decomposition consistency; (C-iii) uses marginal benefit existence. A composite can satisfy multiple routes simultaneously (a well-aligned team satisfies both (C-i) and (C-ii)); what matters for scope is that at least one route holds.

**Miller's IAM definition.** Miller (2022, *Ex Machina*, Ch 1) proposes that social behavior requires Interaction, Agency, and Mutual benefit (IAM). The mutual-benefit requirement in (C-iii) is the AAD analog of Miller's third element. Miller treats IAM as the definition of social behavior; the proposal here treats alignment as the scope condition for composite-agent analysis. The two align substantively: Miller's mutual benefit is a minimum teleological unity.

**Multi-agent systems without composite status.** Adversarial pairs ( #adversarial-destabilization, #adversarial-tempo-advantage) are a central example: they satisfy #multi-agent-scope but fail #composition-scope-condition. The existing segments for adversarial dynamics correctly treat them as multi-agent-level phenomena, not as composite phenomena. Making this scope distinction explicit clarifies what was previously implicit.

**How composites come into being: symbiogenesis.** The formal mechanism by which $U_O$ crosses the composition threshold from below is described in the pending segment on symbiogenic composition. Briefly: in biological and social symbiogenesis, a host integrates an endosymbiont; the endosymbiont's objective is subsumed into the host's; the combined entity's objective $O_c$ emerges where two independent objectives stood. This is the dynamical process of composite-agent identity creation; the scope condition here describes its result.

## Working Notes

- **Operational form of $\epsilon_{\text{comp}}$.** A sharp threshold is likely artificial. More plausible: smooth transition from "not-quite-composite" to "composite," with composition-dependent quantities (closure defect, team persistence) degrading gracefully in the low-$U_O$ regime. The threshold may be a phase transition — at some coupling, composite analysis becomes well-posed; above, it sharpens. This needs formalization before promotion to `claims-verified`.
- **Asymmetric unity.** Routes (C-i) and (C-ii) implicitly assume symmetric alignment (sub-agents equally represented in $O_c$). Symbiogenesis, firm acquisitions, and hierarchical delegation all feature *asymmetric* unity (host dominates; endosymbiont subordinate). The scope condition should accommodate asymmetric alignment; the current (C-ii) hierarchical form partially covers it, but an explicit treatment of role-asymmetric composites is open.
- **Interaction with Class 2 (fully merged) architectures.** #directed-separation's architectural classification (Class 1 modular, Class 2 fully merged, Class 3 partial) applies to individual agents. Composites of Class 2 agents — e.g., multi-LLM systems — may satisfy this scope condition via shared training rather than shared explicit objective. Whether (C-i)-(C-iii) cover this adequately, or whether a fourth route for implicit alignment is needed, is open.
- **Transitivity.** If $A_1, A_2$ align and $A_2, A_3$ align, do $A_1, A_3$? Probably yes via (C-ii) if there is a common parent; not necessarily via (C-i) without a shared objective. Transitivity would make composite formation more robust; non-transitivity would explain why coalition-building requires explicit alignment work.
- **Promotion dependencies.** Before `claims-verified`: operationalize $\epsilon_{\text{comp}}$ (first bullet); audit whether any existing Section III segment implicitly assumes this scope without naming it (likely yes for team-persistence, tempo-composition, closure-based results).
