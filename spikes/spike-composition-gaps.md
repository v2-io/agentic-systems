# Sketch: Composition Gaps (Section III)

**Status**: Working sketch for the two --GAP-- entries in Section III of `01-aad-core/OUTLINE.md`. These concern how single-agent properties behave under composition — specifically, whether directed separation survives and where adversarial attacks are most effective.

**Date**: 2026-04-01

**The two gaps:**
1. Does epistemic goal-blindness survive composition?
2. Which strategy edges are most valuable to attack?

Gap 1 is more fundamental — it concerns whether a core structural property of the theory holds at the composite level. Gap 2 is applied — it extends the adversarial dynamics to strategy-specific targeting.

---

## Gap 1: Does Epistemic Goal-Blindness Survive Composition?

### The question, precisely stated

Directed separation (#der-directed-separation) says: for a single agent, $M_{\tau^+} = f_M(M_{\tau^-}, e_\tau)$ — no $G_t$ argument. The epistemic update is goal-blind conditional on the realized event.

For a composite of agents $A_1, \ldots, A_N$ interacting through a shared environment: does the composite macro-agent $A_c$ satisfy directed separation? That is, is $f_M^c$ independent of $G_t^c$?

### The problem: goal-contaminated observations

Consider two agents, $A$ and $B$, each satisfying directed separation individually.

1. $A$'s policy couples all substates: $a_A = \pi_A(M_A, G_A)$. $A$'s actions depend on $A$'s goals.
2. $B$ observes $A$'s actions as part of its environment: $o_B = h^{(B)}(\Omega, a_A, \xi_B)$.
3. $B$'s observation therefore carries information about $A$'s goals — not because $B$ looked for it, but because $A$'s goal-driven behavior shaped the environment $B$ is observing.
4. $B$ processes this observation goal-blindly (individual directed separation holds). But the *event itself* has been contaminated by $A$'s goals.

At the composite level: the macro-observation $o_c$ includes the inter-agent information flow, which is shaped by individual agents' goals through their policies. The macro-update $f_M^c$ processes these observations — but the observations themselves are not goal-independent at the macro level.

### The key distinction: processing vs. selection

Directed separation is about **processing**, not **selection** (#der-directed-separation's scope condition makes this explicit). An individual agent's goals affect which events it seeks (through action selection), but not how it processes events that arrive.

In a composite, the same distinction applies at a different level:
- The macro-agent's goals (composite objective) may affect which *internal communications* occur (information routing)
- But each sub-agent processes its received observations goal-blindly

The question reduces to: **does the composite's information routing depend on $G_t^c$?**

### Three cases

*[Hypothesis — composition preserves directed separation conditionally]*

**Case 1: Fixed-topology communication.** Information routing between agents follows a fixed structure (org chart, communication protocol, defined interfaces). Agent $A$ always sends certain information to $B$, regardless of the composite's current objective. The routing does not depend on $G_t^c$.

*Result*: Directed separation **survives** at the composite level. Each agent processes goal-blindly; the routing is goal-blind; therefore the composite update is goal-blind. This is the modular architecture (Class 1) composed with itself — it's modular at every level.

**Case 2: Goal-dependent routing.** The composite's communication structure changes based on the composite objective. A military unit shares different intelligence products depending on the mission. A software team routes information differently when fixing a production incident vs. building a new feature. The routing function depends on $G_t^c$.

*Result*: Directed separation **fails** at the composite level. Even though each sub-agent processes observations goal-blindly, the *set of observations that reach each sub-agent* depends on $G_t^c$ through the routing function. The composite's effective observation function $h^c$ is goal-conditioned.

Formally: $o_c = h^c(\Omega, a_{\text{micro}}, G_t^c, \xi)$ — the composite observation function has a $G_t^c$ argument through the routing channel. Even if $f_M^c$ processes $o_c$ goal-blindly, the observation *itself* has been filtered by $G_t^c$. This is the same mechanism as individual goal-dependent attention — it just operates at the routing level instead of the attention level.

**Case 3: Emergent goal-conditioning.** No explicit goal-dependent routing, but agents' goal-driven actions create statistical dependencies between the composite's observations and goals. Agent $A$ acting on its objective creates environmental changes that are correlated with $A$'s goal content. $B$ observes these changes. Over time, $B$'s model $M_B$ accumulates information about $A$'s goals — not because $B$ sought it, but because it leaked through the environment.

*Result*: Directed separation holds **approximately** at the composite level, with a quantifiable goal-contamination term. The contamination depends on:
- Coupling strength ($\gamma_A$ from #der-adversarial-destabilization)
- Observability of $A$'s goal-driven behavior to $B$
- Number of agents (more agents → more contamination sources, but also more averaging)

### Formalizing the goal-contamination

For Case 3, define the **goal-information leakage**:

$$\mathcal{L}_{G \to M}^c = I(o_c\,;\, G_t^c \mid \Omega_t)$$

This is the mutual information between the composite observation and the composite goal, conditional on the true environment state. It measures how much the observations tell you about goals *beyond* what the environment state tells you.

- $\mathcal{L} = 0$: no goal contamination. Directed separation holds exactly.
- $\mathcal{L} > 0$: some goal information leaks into observations.

**When $\mathcal{L}$ is small** (loosely coupled agents, weak $\gamma$, independent observation channels): the composite is "approximately separated." The sequential orient cascade at the macro level is a good approximation. Section II's results apply approximately.

**When $\mathcal{L}$ is large** (tightly coupled agents, strong $\gamma$, shared observation channels): the composite's epistemic state is entangled with its goals. The orient cascade becomes a poor approximation. The coupled formulation is needed.

### What this means for the theory

The answer is: **directed separation survives composition under Case 1 (fixed routing), fails under Case 2 (goal-dependent routing), and approximately holds under Case 3 (emergent leakage) with quantifiable degradation.**

This is structurally parallel to the single-agent case:
- Class 1 (modular) agents satisfy directed separation by construction → composed modular agents with fixed routing satisfy it at the composite level
- Class 2 (merged) agents violate directed separation by construction → composed agents with goal-dependent routing violate it at the composite level
- Class 3 (partially modular) → composed agents with fixed routing but environmental coupling approximately satisfy it

The architectural classification (#der-directed-separation, working notes) **lifts to composition**. This is satisfying — the same structural distinction applies at every level, consistent with #post-composition-consistency's requirement.

### Implications for Section III

Segments in Section III (#scope-multi-agent through #result-per-dimension-persistence) should be understood as:
- **Exact** for Case 1 composites (fixed-routing, modular sub-agents)
- **Approximate** for Case 3 composites (the approximation quality depends on $\mathcal{L}$)
- **Inapplicable in their current form** for Case 2 composites (need coupled formulation)

This does not reduce the value of Section III — most real composites are Case 1 or Case 3. Military command structures, software development teams with defined processes, and multi-agent AI systems with protocol-defined communication are all Case 1. Case 2 (truly goal-dependent routing) is rarer and more fragile.

### Epistemic status

The three-case classification: **robust qualitative**. The reasoning is structural: fixed routing preserves separation, goal-dependent routing breaks it, environmental coupling degrades it. The goal-information leakage $\mathcal{L}$: **hypothesis** — the quantity is well-defined (mutual information is always well-defined), but computing it for specific composites requires knowing the joint distribution of observations, goals, and environment states. The claim that the architectural classification lifts to composition: **derived** from the structure of directed separation's scope condition.

### Open questions

1. **Is there a useful bound on $\mathcal{L}$ as a function of $N$ (number of agents)?** More agents means more goal-leakage sources, but also more noise (each agent's goal signal is diluted). The scaling may be sub-linear — or it may be linear in adversarial settings where an opponent deliberately amplifies goal leakage.

2. **Does trust estimation (#hyp-communication-gain's $U_{\text{align}}$) compensate?** If $B$ explicitly models its uncertainty about $A$'s intentions, and discounts observations accordingly, this reduces the effective $\mathcal{L}$ in $B$'s update. Trust-adjusted gain may be a natural mechanism for maintaining approximate directed separation.

3. **Case 2 composites: can they be treated as "merged" architectures?** If goal-dependent routing makes the composite structurally similar to a single merged agent (Class 2), then the logogenic treatment (coupled formulation from the start) may be the right approach for these composites too.

4. **Temporal dynamics of $\mathcal{L}$**: does goal contamination accumulate over time (as agents learn more about each other's behaviors and infer goals) or stabilize (as the novelty of each agent's behavior decays)?

---

## Gap 2: Which Strategy Edges Are Most Valuable to Attack?

### The setup

Agent $A$ is trying to degrade agent $B$'s strategy $\Sigma_B$. $B$'s strategy is a DAG with edges of varying importance, observability, and redundancy. $A$ has limited resources. Which edges should $A$ target?

### Two qualitatively distinct attack modes

The theory already provides the key ingredients. #der-observability-dominance says unobservable edges are frozen. #der-adversarial-destabilization says tempo advantage destabilizes. Combining them reveals two attack modes:

**Mode 1: Visible sabotage.** Attack highly observable, critical edges. $B$ detects the failure quickly (high $\sigma_v$ → fast feedback). The value to $A$: force $B$ to revise strategy, consuming $B$'s strategic tempo on repair instead of progress. This is a tempo-drain attack — it doesn't necessarily break $B$'s plan permanently, but it forces $B$ to spend maintenance resources.

**Mode 2: Silent undermining.** Attack poorly observable, critical edges. $B$ does not detect the failure (low $\sigma_v$ → frozen credence, no update). $B$ continues executing a plan that no longer works, wasting effort on a path that will fail. This is a confidence-corruption attack — $B$'s plan-confidence score $\hat{P}_\Sigma$ remains high while actual success probability drops.

Mode 2 is structurally more dangerous. It exploits #der-observability-dominance: $B$ literally cannot learn that the edge has been degraded because the update gain $\eta_{\text{edge}} \to 0$. $B$ will only discover the problem when it reaches the corrupted part of the plan and experiences unexpected failure — possibly after irreversible commitments.

### Edge vulnerability analysis

*[Hypothesis — edge vulnerability decomposition]*

The vulnerability of edge $(i, j)$ to adversarial attack depends on four factors:

**1. Criticality ($c_{ij}$)**: How much does the plan's success depend on this edge?

$$c_{ij} = \frac{\partial \hat{P}_\Sigma}{\partial p_{ij}}$$

This is the sensitivity of the plan-confidence score to changes in edge credence. Computable in $O(|V| + |E|)$ via automatic differentiation through the status propagation formula. High for edges on the critical path; low for redundant edges.

**2. Observability inversion ($1 - \sigma_{ij}$)**: How hard is it for $B$ to detect that this edge has been compromised?

$\sigma_{ij} = \min_{v \in \text{path}(i,j)} \sigma_v$ is the path observability from #der-observability-dominance. The *inversion* measures attack concealment — higher is better for the attacker.

**3. Coupling effectiveness ($\gamma_{ij}^A$)**: Can $A$ actually degrade this edge?

This depends on whether $A$'s actions can influence the conditions that edge $(i,j)$ depends on. In some cases, $A$ has direct access (can sabotage the infrastructure $B$'s plan relies on). In others, $A$ has no effective coupling to specific edges.

**4. Redundancy discount ($1/r_{ij}$)**: Does $B$ have alternative paths?

If node $j$ has multiple parents (OR combination), attacking one edge just redirects $B$ through an alternative path. The discount is inversely proportional to the number of viable alternative paths.

### The vulnerability ranking

*[Hypothesis — edge vulnerability score]*

$$V_{ij} = c_{ij} \cdot (1 - \sigma_{ij}) \cdot \gamma_{ij}^A \cdot \frac{1}{r_{ij}}$$

The product form means *all four factors must be nonzero* for an edge to be worth attacking. A critical but fully observable edge ($(1 - \sigma) = 0$) has zero vulnerability — $B$ will detect and adapt. A critical, unobservable edge with high redundancy has low vulnerability — $B$ has alternatives even if one path is corrupted. The attacker wants edges that are simultaneously critical, hard to observe, accessible, and non-redundant.

### Optimal attack allocation

Given a resource budget $\epsilon_A$ and a set of edges with vulnerability scores: the attacker allocates resources in descending vulnerability order, subject to $\sum \epsilon_{ij} \leq \epsilon_A$.

Under Mode 2 (silent undermining), the attacker's resource expenditure per edge is proportional to the effort needed to reduce $p_{ij}^{\text{true}}$ (the actual causal strength) below some threshold — without reducing $p_{ij}^{B}$ ($B$'s belief about the edge). The gap between actual and believed edge strength is the **confidence corruption**: $p_{ij}^B - p_{ij}^{\text{true}}$.

Under Mode 1 (visible sabotage), the attacker's expenditure buys tempo-drain for $B$. The value is $B$'s repair time per unit of disruption: the more revision $B$ must do (from #form-structural-change-as-parametric-limit), the more tempo $B$ loses.

### Strategic implications

**Defense against Mode 2 is an observability problem.** $B$'s best defense is to *increase observability* of critical, low-observability edges — instrument them, add monitoring, create early warning signals. This transforms Mode 2 attacks into Mode 1 attacks, which are less dangerous because $B$ can adapt.

This connects to #der-observability-dominance's core message: unobservable regions are absorbing. In the adversarial context, they're also *targetable*. An agent that invests in observability of its critical strategy edges is both better at learning and harder to undermine silently.

**The attacker's dilemma.** Attacking Mode 2 (silent) is more effective but requires the attacker to avoid triggering $B$'s detection. The attacker must model $B$'s observability landscape — which requires $A$ to have a model of $B$'s model. This is a higher-order epistemic requirement. If $A$ doesn't know which edges $B$ can observe, $A$ risks triggering Mode 1 when aiming for Mode 2.

**Correlated vs. independent edge attacks.** The #def-strategy-dag edge-independence caveat notes that real systems have correlated failures. An attacker exploiting correlations — attacking a shared infrastructure that multiple edges depend on — can degrade many edges with a single action. This is why attacks on infrastructure (shared libraries, communication channels, supply chains) are disproportionately effective: they induce correlated failure across multiple strategy edges.

### Connection to Gap 1

If directed separation breaks at the composite level (Gap 1, Case 2 or 3), then $B$'s epistemic state carries encoded information about the composite's goals. An adversary $A$ that is part of the composite (or observes it) can infer which edges are most critical by observing the goal-contaminated observations. This makes the vulnerability assessment *easier for the attacker* and *harder for the defender* — the defender's goal structure leaks into the shared information space.

Conversely, if directed separation holds (Case 1), the defender's goal structure is opaque to the attacker. The attacker must estimate criticality from external observation of $B$'s behavior, not from direct observation of $B$'s goal content.

### Epistemic status

The two attack modes (visible sabotage vs. silent undermining): **robust qualitative** — they follow directly from the observability-dominance mechanism. The vulnerability score: **hypothesis** — the four factors are well-motivated, but the multiplicative form and the specific choice of factors are a first pass. The optimal allocation: **discussion-grade** — the knapsack-style framing is standard optimization, but the input estimation (criticality, observability, coupling, redundancy for each edge) is domain-specific and potentially intractable.

### Open questions

1. **Can $B$ defend by randomizing its strategy?** If $B$ occasionally changes which edges are critical (by maintaining multiple strategies and switching between them), the attacker's vulnerability assessment becomes stale. This is the strategic analog of defensive deception.

2. **Cascade effects.** When a critical edge fails, does it trigger cascading failure downstream? The #def-strategy-dag status propagation is a forward pass — a failed edge at depth $k$ corrupts all downstream estimates. Does this mean shallow edges are more valuable to attack (more downstream impact) or deep edges (harder to detect)?

3. **Is there a game-theoretic equilibrium?** If both agents can observe each other's vulnerability landscapes, does the interaction converge to a Nash equilibrium? Or is the advantage always with the attacker (because silent undermining is structurally harder to detect)?

4. **Domain-specific vulnerability patterns.** In software: which strategy edges are most vulnerable? Infrastructure dependencies (shared libraries, databases) seem to be high-criticality, low-observability, low-redundancy — the maximally vulnerable pattern. In military: supply lines are the classic example. Can the theory predict vulnerability patterns for specific domains?

---

## Cross-Gap Connection

Gap 1 (goal-blindness under composition) and Gap 2 (edge vulnerability) interact through the observability of goals:

- If the composite preserves directed separation (Case 1): the attacker cannot observe the defender's goal structure through the shared epistemic state. The attacker must estimate edge criticality externally. Defense is easier.
- If the composite leaks goal information (Cases 2-3): the attacker can partially observe the defender's goal structure. Edge criticality becomes partially observable to the attacker. Vulnerability scores become more accurate for the attacker.

This creates a meta-strategic incentive: **agents benefit from compositions that preserve directed separation**, not just for epistemic hygiene but for adversarial robustness. Goal-blind composites are harder to attack because their goal structure is opaque.

## What Would Promotion to src/ Look Like?

| Gap | Candidate slug(s) | Type | Depends on |
|-----|-------------------|------|------------|
| 1 | `directed-separation-under-composition` | Derived + Scope | directed-separation, composition-closure, multi-agent-scope |
| 2 | `strategy-edge-vulnerability` | Hypothesis | observability-dominance, adversarial-destabilization, strategy-dag |

Both would enter at `draft`. Gap 1 is closer to promotable because the three-case structure follows from existing definitions. Gap 2 needs the vulnerability score validated (even in a toy case) before promotion.
