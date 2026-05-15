# Spike: Agent Composition and the Holon Principle

**Status**: Exploratory spike — pushing on whether AAD's framework *requires* compositional consistency across agent boundaries, and what that consistency requirement looks like formally.

**Date**: 2026-03-10

**The driving intuition**: Almost every agentic system of interest can be studied at multiple boundary levels. A development team is an agent (from the stakeholder's view) composed of agent-developers. A military division is an agent composed of agent-battalions composed of agent-companies. A company is an agent in a market composed of agent-departments. If AAD applies at every level — and the scope condition (#050) doesn't restrict which level — then the theory must give *consistent* answers regardless of where we draw the boundary. This consistency requirement may not be optional. It may be a mathematical imperative: you cannot cleanly define an agent of interest without this property holding.

**What this spike explores**:
1. Why composition consistency is a requirement, not a feature
2. The formal conditions under which a group composes into a single agent
3. Degrees of unity and what happens when composition is imperfect
4. Whether this simplifies the multi-agent treatment (Section III)
5. Connection to holons, Clausewitz's three gaps, Auftragstaktik

---

## 1. The Consistency Argument

### 1.1 Boundary arbitrariness

AAD's scope condition (#050) says the theory applies where:
- Observations exist
- The agent has at least binary choice (|A| ≥ 2)
- Residual uncertainty persists: H(Ω_t | C_t) > 0

Nothing in this restricts the *level* at which the boundary is drawn.
Consider a software development team:

**Boundary A** (individual): Developer Alice is the agent. Her environment includes the codebase, teammates, stakeholders.
- M_t^A = Alice's understanding of the codebase and task
- O_t^A = her assigned subtask
- Σ_t^A = her implementation plan
- Scope condition satisfied? Yes.

**Boundary B** (team): The team {Alice, Bob, Carol} is the agent. The environment is the codebase, stakeholders, other teams.
- M_t^B = the team's collective understanding
- O_t^B = the feature they're building together
- Σ_t^B = their coordinated implementation strategy
- Scope condition satisfied? Yes.

**Boundary C** (organization): The engineering department is the agent.
The environment is the market, users, infrastructure.
- M_t^C = organizational knowledge of technology and market
- O_t^C = product roadmap objectives
- Σ_t^C = the department's technical strategy
- Scope condition satisfied? Yes.

AAD claims to apply at all three levels. If it does, the predictions at each level must be *compatible*:

- The team's tempo T^B must relate to the individuals' tempos T^A_i through some composition law
- The team's persistence condition must be derivable from individual persistence conditions plus their coordination structure
- The team's mismatch dynamics must be consistent with the aggregate of individual mismatch dynamics

### 1.2 Why this is a requirement, not a feature

If the predictions are NOT compatible, AAD has a genuine problem:

**Scenario**: AAD predicts the team (boundary B) will persist because T^B > ρ/δ_critical. But when we analyze the individuals (boundary A), we find each A_i has T^A_i < ρ_i/δ_critical_i — each individual is below their persistence threshold. Is the team persisting or not?

If the theory gives contradictory answers at different boundaries, the theory is *inconsistent*. The boundary choice is a modeling decision, not a physical fact — the same physical system is being described. Consistency requires that the predictions at different levels are compatible (not necessarily identical — different levels see different quantities — but non-contradictory).

This is analogous to the requirement in physics that laws be consistent across scales. The renormalization group in statistical mechanics formalizes exactly this: the requirement that the same physics holds at different scales constrains the form of the theory. Our composition principle is AAD's version of this constraint.

### 1.3 The imperative, stated precisely

*[Hypothesis — structural argument, not yet a theorem]*

**Claim**: For AAD to be internally consistent, the following must hold:

For any system S satisfying the scope condition (#050), and any decomposition of S into subsystems ${S_1, ..., S_n}$ where each $S_i$ also satisfies the scope condition:

1. **Tempo composition**: $T_S$ must be expressible as a function of ${T_{S_i}}$ and the coordination structure among them
2. **Persistence compatibility**: If S persists ($T_S \gt ρ_S/δ_{crit}$), this must be derivable from the sub-agents' individual persistence conditions plus coordination
3. **Mismatch consistency**: $δ_S$ must be derivable from ${δ_{S_i}}$ and their interaction structure

If these don't hold, the theory's predictions depend on an arbitrary modeling choice (where to draw the boundary), which would undermine the theory's claims to generality.

---

## 2. Formal Composition

### 2.1 The composite agent

Given sub-agents A_1, ..., A_n interacting through a shared environment and inter-agent channels, define the composite agent A_c:

*[Definition (composite-agent)]*

The composite agent A_c is defined by:

**Observations**: The union of all sub-agents' observation channels.
$$o_t^c = (o_t^{(1)}, \ldots, o_t^{(n)})$$

subject to inter-agent observability — A_c "sees" everything that any sub-agent sees, but individual sub-agents may not see each other's observations without communication.

**Actions**: The joint action space.
$$a_t^c = (a_t^{(1)}, \ldots, a_t^{(n)}) \in A_1 \times \cdots \times A_n$$

**State**: The composite state.
$$X_t^c = (M_t^c, G_t^c)$$

where $M_t^c$ and $G_t^c$ are defined by the degree of internal unity (§3 below).

### 2.2 When composition is trivial

**Perfect unity**: If the sub-agents have:
- Identical models: $M_t^{(i)} = M_t$ for all $i$
- Identical objectives: $O_t^{(i)} = O_t$ for all $i$
- A jointly optimized policy: $\pi^c(M_t, G_t) = (\pi^{(1)}, \ldots, \pi^{(n)})$ where the individual policies are computed jointly
- Instantaneous, lossless internal communication

Then $A_c$ is trivially a single agent. Its state is $X_t^c = (M_t, G_t)$ and all of AAD applies directly. The "multiple agents" are just effectors and sensors of a single cognitive entity.

This is the limiting case. It describes, roughly:
- A single brain controlling multiple limbs
- A perfectly synchronized team with full information sharing
- A hive mind (science fiction, but the formal limit)

### 2.3 Composition of tempo

This is where the first interesting result should emerge.

*[Derived — sketch, needs verification]*

**Claim (tempo composition)**: Under perfect communication and model-sharing, the composite tempo is:

$$\mathcal{T}_c = \sum_{i=1}^{n} \sum_k \nu_k^{(i)} \cdot \eta_k^{(i)*}$$

That is, tempos ADD across sub-agents when they share a common model and their observation channels are independent. Each sub-agent contributes its channels' event rates weighted by optimal gain.

**Why this should hold**: Tempo is the rate of useful information acquisition. If sub-agents observe different aspects of the environment (independent channels) and share their updates into a common M_t, the composite acquires information at the sum of the individual rates. No information is wasted or double-counted because the channels are independent.

**When channels overlap**: If sub-agents share observation channels (they see the same things), the composite tempo is LESS than the sum. Redundant observations don't add information — they only reduce U_o on the shared channel (averaging multiple noisy observations of the same signal). The gain:

$$\mathcal{T}_c = \sum_{\text{unique channels}} \nu_k \cdot \eta_k^* + \sum_{\text{shared channels}} \nu_k \cdot \eta_k^{*(\text{combined})}$$

where $\eta_k^{\ast(\text{combined})}$ reflects the improved gain from multiple observers of the same channel (lower effective U_o).

**Communication overhead**: Imperfect communication SUBTRACTS from the composite tempo. If sub-agent A_i observes something but can communicate it to the group only after delay Δτ, the information is stale by Δτ — its value is reduced by the environment's rate of change over that interval. Define:

$$\mathcal{T}_c = \sum_{i} \mathcal{T}_i^{\text{local}} + \sum_{i \neq j} \mathcal{T}_{i \to j}^{\text{shared}} - C_{\text{coord}}$$

where $C_{\text{coord}}$ is the coordination overhead — the tempo cost of sharing information, resolving conflicts, and maintaining coherence.

**The composition gap**:
$$\Delta\mathcal{T} = \sum_i \mathcal{T}_i - \mathcal{T}_c \geq 0$$

This quantity measures the "cost of being multiple." It is zero for perfectly coordinated agents with independent channels, and increases with communication cost, channel overlap, and coordination complexity.

### 2.4 Composition of persistence

*[Derived — sketch]*

**Claim**: The composite agent persists iff:

$$\mathcal{T}_c \gt \frac{\rho_c}{\Vert\delta_{\text{critical}}^c\Vert}$$

where $\rho_c$ is the rate of environment change AS SEEN BY THE COMPOSITE (which may differ from what individuals see — the team faces macro-level change while individuals face micro-level change within the team's allocation of work).

**Why teams persist where individuals can't**: The composite tempo $\mathcal T_c$ can exceed any individual $\mathcal T_i$ because:
1. More total observation channels → higher sum of information rates
2. Diverse perspectives → better coverage of multi-dimensional ρ (addresses the per-dimension persistence bottleneck, #460)
3. Shared processing → each sub-agent can specialize (reducing individual computational load, improving individual η*)

But $\rho_c$ may also be larger than individual $\rho_i$ — the team takes on challenges that no individual would face. The persistence advantage is:

$$\frac{\mathcal{T}_c}{\rho_c / \Vert\delta_{\text{critical}}^c\Vert} \gt \frac{\mathcal{T}_i}{\rho_i / \Vert\delta_{\text{critical}}^i\Vert}$$

which holds when the tempo gains from composition outweigh the increased challenge.

**The team persistence theorem** (proposed):

A team of n sub-agents, each below individual persistence threshold ($\mathcal T_i \lt \rho_i / \delta_i^{\text{crit}}$), can persist as a composite if:

$$\sum_i \mathcal{T}_i - C_{\text{coord}} \gt \frac{\rho_c}{\Vert\delta_{\text{critical}}^c\Vert}$$

This gives a *formal reason* why coordination matters: the coordination overhead $C_{\text{coord}}$ directly subtracts from the composite's persistence margin. A team with high individual tempos but terrible coordination can fall below persistence threshold.

### 2.5 Composition of directed separation

Does directed separation (#250) compose? That is, if each sub-agent's $f_M^{(i)}$ is $G_t^{(i)}$-independent, is the composite's $f_M^c$ independent of $G_t^c$?

*[Hypothesis — I believe yes, but with a subtlety]*

If each sub-agent updates its model goal-blindly (processes events without reference to purpose), then the composite's model update is the aggregation of goal-blind updates. Goal-blindness composes.

**The subtlety**: Coordination itself may break directed separation.
If the team's communication structure depends on the shared objective (you share different information depending on what the team is trying to achieve), then the composite's effective observation function is goal-dependent — WHICH events reach the composite M_t^c depends on G_t^c through the communication routing.

This is the organizational analog of the LLM scope restriction in v3 §8: goal-conditioned attention affects which events arrive, even if event processing is goal-blind.

---

## 3. Four Dimensions of Unity

The interesting theory is in the partial cases. I identify four dimensions along which a composite agent can be more or less unified. These dimensions are substantially independent — a group can have high unity on one and low on another.

### 3.1 Epistemic unity (shared model)

*How much of the reality model is shared across sub-agents?*

**Full**: $M_t^{(i)} = M_t$ for all $i$. Single shared model.
**High**: Large shared component, small individual residuals.
  $M_t^{(i)} = M_t^{\text{shared}} \oplus M_t^{(i,\text{local})}$
**Low**: Models overlap only on coarse structure.
**None**: Independent models.

*[Definition (epistemic unity)]*

$$U_M = \frac{I(M_t^{(1)}; \ldots; M_t^{(n)})}{H(M_t^{(1)}, \ldots, M_t^{(n)})}$$

The fraction of total model information that is shared. $U_M = 1$ for identical models; $U_M = 0$ for independent models. (This is a multi-information / total-correlation ratio.)

**What epistemic unity buys**: Consistent predictions across sub-agents. When A_i and A_j share M_t, their predictions about the environment agree. Actions based on shared predictions are implicitly coordinated — you don't need to communicate "I think X will happen" because your partner already knows.

**What its absence costs**: Prediction conflicts → coordination failures. A_i acts based on M_t^(i) which contradicts M_t^(j); their actions interfere. The composite mismatch δ^c includes an *internal* component from model disagreement, not just external environment mismatch.

### 3.2 Teleological unity (shared objective)

*How aligned are the sub-agents' objectives?*

**Full**: $O_t^{(i)} = O_t$ for all $i$. Identical objectives.
**Hierarchical**: $O_t^{(i)}$ are local instantiations of a shared
  $O_t$, chosen to decompose the shared objective into achievable sub-tasks. (Auftragstaktik structure.)
**Compatible**: $O_t^{(i)}$ are different but non-conflicting —
  there exists a joint policy that makes progress on all simultaneously.
**Conflicting**: $O_t^{(i)}$ are actively opposed on at least some
  dimensions. (Internal adversarial dynamics.)

*[Definition (teleological unity — sketch)]*

For a pair of sub-agents, teleological alignment could be measured by the correlation of their value functions evaluated on shared trajectories:

$$U_O^{(i,j)} = \text{corr}(V_{O_t^{(i)}}(\tau), V_{O_t^{(j)}}(\tau))$$

over the distribution of trajectories the composite is likely to encounter. $U_O = 1$ for identical objectives; $U_O = -1$ for perfectly opposed objectives; $U_O = 0$ for orthogonal objectives.

The composite teleological unity is some aggregation over all pairs.

**What teleological unity buys**: Aligned incentives. Sub-agents don't need to be *told* to coordinate — they independently choose actions that serve the shared objective. This is the deepest form of coordination because it doesn't require communication bandwidth.

**What its absence costs**: Strategic friction. Sub-agents pursue conflicting sub-goals; effort is wasted or actively counterproductive. In the extreme (adversarial sub-agents), the composite may have zero or negative effective tempo toward any external objective.

### 3.3 Strategic unity (coordinated action)

*How coordinated is the joint policy?*

**Full**: Centrally optimized joint policy $\pi^c(X_t^c)$.
**Protocolic**: Agreed-upon coordination protocol (roles, procedures,
  handoff mechanisms) without central control.
**Communicative**: Sub-agents share intentions and negotiate in real
  time, adapting to each other.
**Independent**: Each sub-agent acts on its own policy without
  coordination.

*[Definition (strategic unity — sketch)]*

$$U_\Sigma = 1 - \frac{D_{\text{KL}}(\pi^c_{\text{actual}} \Vert \pi^c_{\text{optimal}})}{D_{\text{KL}}(\pi^c_{\text{independent}} \Vert \pi^c_{\text{optimal}})}$$

where $\pi^c_{\text{optimal}}$ is the jointly optimal policy, $\pi^c_{\text{actual}}$ is what the sub-agents actually produce, and $\pi^c_{\text{independent}}$ is what they'd produce without any coordination. $U_\Sigma = 1$ when actual = optimal; $U_\Sigma = 0$ when actual = independent.

**What strategic unity buys**: Non-redundant action. Sub-agents don't duplicate effort or leave gaps. The joint action covers the action space efficiently.

**What its absence costs**: Wasted effort, gaps, interference. Two sub-agents both fix the same bug while a critical bug goes unnoticed. Three soldiers advance on the same position while the flank is unguarded.

### 3.4 Perceptual unity (shared observation)

*How much of the observation stream is shared?*

**Full**: All sub-agents observe everything.
**Broadcast**: One sub-agent observes, broadcasts to all.
**Selective**: Observations shared based on relevance (filtered
  by the sender's judgment of what matters to the recipient).
**None**: Private observations only.

*[Definition (perceptual unity)]*

$$U_O^{\text{obs}} = \frac{|\text{channels visible to all sub-agents}|}{|\text{total unique channels}|}$$

More precisely, using information: the fraction of total observation information that reaches all sub-agents.

**What perceptual unity buys**: Consistent situational awareness.
Enables epistemic unity without explicit model-sharing — if everyone sees the same things and processes them similarly, their models converge naturally.

**What its absence costs**: Information silos. Sub-agent A_i observes a critical signal but doesn't share it (doesn't know it's relevant to A_j, or can't communicate it in time). The composite "knows" the information (some sub-agent has it) but can't act on it coherently.

---

## 4. The Clausewitz Connection

Clausewitz identified three fundamental gaps in warfare (as systematized by Bungay in *The Art of Action*):

1. **Knowledge gap**: The difference between what we would like to know and what we actually know.
2. **Alignment gap**: The difference between what we want people to do and what they actually do.
3. **Effects gap**: The difference between what we expect our actions to achieve and what they actually achieve.

These map precisely to our four unity dimensions:

| Clausewitz Gap | AAD Unity Dimension | Formal Quantity |
|---|---|---|
| Knowledge gap | Epistemic unity ($U_M$) | $1 - U_M$: fraction of model not shared |
| Alignment gap | Teleological unity ($U_O$) | $1 - U_O$: objective misalignment |
| Effects gap | Strategic + Perceptual unity | $1 - U_\Sigma$ + coordination overhead |

**Bungay's Auftragstaktik solution**: Accept the knowledge gap (don't try for full epistemic unity — it's too expensive). Minimize the alignment gap (invest heavily in shared intent — teleological unity). Allow the effects gap to be managed locally (grant strategic autonomy — accept imperfect strategic unity in exchange for adaptability).

In AAD terms: Auftragstaktik optimizes for *teleological unity* while accepting lower epistemic and strategic unity. The IB-compressed shared intent (#410) IS the mechanism: communicate enough of O_t to align objectives, not so much that you constrain local adaptation of Σ_t.

**The formal Auftragstaktik principle** (proposed):

For a composite agent facing environment change rate ρ_c, there exists an optimal allocation of communication bandwidth across the three unity dimensions:

$$\text{bandwidth} = B_M + B_O + B_\Sigma$$

where $B_M$ is bandwidth spent sharing model updates, $B_O$ is bandwidth for objective alignment, and $B_\Sigma$ is bandwidth for action coordination.

*[Hypothesis]* The optimal allocation prioritizes $B_O$ (teleological unity) over $B_\Sigma$ (strategic coordination) over $B_M$ (model sharing), because:
- Teleological unity enables autonomous coordination (doesn't require ongoing bandwidth after initial alignment)
- Strategic coordination requires ongoing bandwidth but can adapt to local conditions
- Model sharing requires the most bandwidth (models are large, change fast) and provides the least marginal coordination benefit if objectives are already aligned

This is Bungay's empirical observation (from studying military history) formalized as an information-theoretic optimization. The IB framework (#100) applied to inter-agent communication predicts exactly this prioritization if we assume objectives change slowly (low ν_O), strategies change moderately (medium ν_Σ), and models change fast (high ν_M).

---

## 5. The Holon: Formal Definition

Koestler (1967) introduced "holon" for entities that are simultaneously wholes and parts. The concept was subsequently buried under layers of mysticism (Wilber's integral theory, holarchy, etc.) that have no formal content. The structural observation, however, is precise and useful. Let us rescue it.

*[Definition (holon)]*

An **agent holon** (or simply **holon**) $H$ is an agent satisfying AAD's scope condition (#050) such that:

1. **Whole**: $H$ can be described as a single agent with state $X_t^H = (M_t^H, G_t^H)$, observations $o_t^H$, and actions $a_t^H$, interacting with an external environment $\Omega^{\text{ext}}$.

2. **Parts**: $H$ can be decomposed into sub-agents $\{A_1, \ldots, A_n\}$ where each $A_i$ satisfies the scope condition with respect to an environment that includes other sub-agents and the external environment: $\Omega^{(i)} = \Omega^{\text{ext}} \cup \{A_j : j \neq i\}$

3. **Composition consistency**: The dynamics of $X_t^H$ (as predicted by AAD at the holon level) are compatible with the aggregate dynamics of $\{X_t^{(i)}\}$ (as predicted by AAD at the sub-agent level plus inter-agent dynamics).

4. **Recursive applicability**: Each sub-agent $A_i$ may itself be a holon, decomposable into further sub-agents, with the same consistency requirement at every level.

Property 3 is the load-bearing one. "Compatible" means: the holon- level quantities ($\mathcal T_H$, $\rho_H$, $\delta^H$) can be expressed as functions of the sub-agent-level quantities plus inter-agent coordination structure. No information is lost or contradicted by changing the level of analysis.

### 5.1 What the holon definition buys us

**Theoretical economy**: AAD's machinery (Sections I and II) is developed ONCE, for a single agent. The holon principle says it applies at every level of composition. Section III (multi-agent) becomes: "Here are the composition conditions and the analysis of what happens when composition is imperfect." The core theory doesn't need to be re-derived for teams, organizations, or ecosystems.

**Principled boundary drawing**: Instead of "where should we draw the agent boundary?", the answer is: "anywhere you like — the theory is consistent across boundaries." The choice of boundary is a modeling convenience (what questions are you asking?), not a theoretical commitment.

**The inner/outer duality**: Every holon admits two complementary analyses:
- **Exogenic (black-box)**: Treat $H$ as a single agent. Measure its tempo, persistence, mismatch, strategy. This is the view from outside — the stakeholder's view of the team, the market's view of the company, the general's view of the division.
- **Endogenic (glass-box)**: Look inside at the sub-agents, their individual states, their coordination, the gaps between intended and actual collective behavior. This is where organizational dynamics, friction, trust, and coordination failure live.

The theory connects the two: the exogenic quantities are DERIVED from the endogenic ones through the composition laws.

### 5.2 What makes this different from "just systems theory"

General systems theory (von Bertalanffy, Ashby, etc.) asserts that systems have hierarchical structure and emergent properties. This is true but vague — it doesn't tell you how to compute anything.

AAD's holon principle is specific: it provides *composition laws* for definite quantities (tempo, persistence, mismatch, gain). It makes testable predictions: "a team with these individual tempos and this coordination structure will have this composite tempo and will persist / not persist against this rate of change." The composition laws are the formal content that generic systems theory lacks.

---

## 6. Implications for AAD's Structure

### 6.1 Section III reconceived

If the holon principle holds, Section III is not "multi-agent dynamics" as a separate body of theory. It becomes:

**Section III: Composition and Coordination**

- The holon definition and composition consistency requirement
- Composition laws for tempo, persistence, gain, mismatch
- The four unity dimensions and their interactions
- What happens when unity is imperfect (Clausewitz's gaps)
- The Auftragstaktik principle as IB-optimal communication
- Adversarial dynamics as the case where teleological unity is negative ($U_O \lt 0$)

The adversarial tempo advantage (#430) becomes a CONSEQUENCE of composition theory: two opposing holons, each with their own composite tempo, and the superlinear advantage arises from the same persistence mathematics applied at the holon level.

### 6.2 Section V reconceived

AI agent teams are holons. A multi-agent coding system (orchestrator + specialized sub-agents) is a holon whose unity dimensions can be measured:
- Epistemic: shared codebase understanding (do the agents agree on what the code does?)
- Teleological: shared task objective (are they all working toward the same goal?)
- Strategic: coordinated action (do they avoid conflicts, cover gaps?)
- Perceptual: shared observations (do they all see test results, error messages?)

The 100% context turnover problem (#710) is an *epistemic unity* problem: each agent session starts with $U_M \approx 0$ relative to previous sessions. The M_t preservation mechanisms (#720) are technologies for maintaining epistemic unity across time.

### 6.3 Possible restructuring of the theory

If this principle is truly load-bearing, it might belong BETWEEN Sections I and II, or as part of Section I:

- Section I: Adaptive systems (single agent OR holon treated as one)
- Section I-bis: The holon principle (composition, consistency, inner/outer duality)
- Section II: Purposeful agency (applies at any holon level)
- Section III: Coordination failure (what happens when composition is imperfect) — subsumes adversarial dynamics
- Section IV–V: Domain instantiations

This would mean the composition principle is a *foundational* claim, not a multi-agent extension. It's part of what it means to define an agent within the theory.

---

## 7. What's Forced vs. What's Chosen

### Forced (by consistency requirement)

- Composition laws MUST EXIST. If AAD applies at multiple levels and the scope condition doesn't restrict level, then the predictions must be compatible. This is not optional.

- Tempo must compose ADDITIVELY (or nearly so) for independent channels. This follows from tempo being an information rate — mutual information rates from independent sources add. (More precisely, they add when the sources provide information about different aspects of the environment. When they overlap, diminishing returns apply.)

- Persistence must compose MONOTONICALLY in the number of sub-agents, for fixed coordination overhead. Adding a sub-agent with positive tempo can only help (or at worst not hurt) the composite's persistence, IF the coordination cost of adding them is bounded.

### Not forced (formulation choices)

- The specific form of the coordination overhead $C_{\text{coord}}$.
  This likely depends on the communication protocol, the coordination mechanism, and the strategic unity structure.

- The specific metrics for unity dimensions ($U_M$, $U_O$, $U_\Sigma$, $U_O^{\text{obs}}$). The definitions above are proposals. Other information-theoretic measures could serve.

- Whether the unity dimensions are truly independent. There may be coupling: high epistemic unity might enable high strategic unity (shared models enable coordination without explicit planning).

### Open (genuine questions)

1. **Is there a minimum unity for composition to be meaningful?**
   At some point, a group of agents is NOT usefully described as a single composite. When $U_M$, $U_O$, $U_\Sigma$ are all near zero, the "composite agent" is a fiction — the sub-agents are just coexisting. Is there a phase transition, or is it continuous?

2. **Does the composition gap $\Delta\mathcal{T}$ have a lower bound?**
   Is there an irreducible cost of being multiple, even with perfect coordination? (Analogous to: entropy of a mixture ≥ sum of component entropies.) If so, this explains why organizations have overhead that can't be eliminated, only minimized.

3. **Can adversarial dynamics be fully subsumed?** The claim that adversarial dynamics = negative teleological unity is appealing but needs verification. Adversarial agents may have coupled dynamics that don't reduce to "a holon with $U_O \lt 0$."

4. **Does the Auftragstaktik principle (prioritize $B_O$ over $B_\Sigma$ over $B_M$) actually follow from IB optimization?** This needs a formal derivation, not just the qualitative argument that objectives change slowly.

5. **How does this interact with directed separation?** If the composite's observation function is goal-dependent (because communication routing depends on G_t), the composite violates directed separation even if each sub-agent satisfies it individually. This is an important scope restriction.

6. **Infinite regress?** If every agent is a holon, and every holon is composed of sub-agents that are holons... where does it bottom out? Presumably at atomic agents — agents that satisfy the scope condition but cannot be meaningfully decomposed further. These are agents whose "inner" dynamics are not usefully described by AAD (neurons, transistors, irreducible mechanisms). The scope condition provides the floor: below the level where observations, actions, and uncertainty exist, AAD doesn't apply.

---

## 8. A Possible Theorem

Assembling the above, the central theorem of composition might look like:

*[Proposed Theorem Schema (agent-composition)]*

**Given**: Sub-agents $A_1, \ldots, A_n$, each satisfying the scope condition, with:
- Individual states $X_t^{(i)} = (M_t^{(i)}, G_t^{(i)})$
- Individual tempos $\mathcal T_i$
- Inter-agent communication at rate $\nu_{\text{comm}}$ with bandwidth $B$
- Unity measures $(U_M, U_O, U_\Sigma, U_{\text{obs}})$

**Then**: There exists a composite agent $A_c$ with:

$$\mathcal{T}_c = f(\{\mathcal{T}_i\}, U_{\text{obs}}, \nu_{\text{comm}}, B) \leq \sum_i \mathcal{T}_i$$

with equality when channels are independent and communication is lossless and instantaneous. The composite persists iff:

$$\mathcal{T}_c \gt \frac{\rho_c}{\Vert\delta_{\text{critical}}^c\Vert}$$

and the composite's mismatch dynamics satisfy the same sector- condition framework as individual agents, with an additional *coordination mismatch* term proportional to $(1 - U_M)(1 - U_\Sigma)$ that represents the cost of inconsistent models producing uncoordinated actions.

**Corollary (team persistence)**: A group of sub-agents, each below individual persistence threshold, persists as a composite when:
$$\sum_i \mathcal{T}_i - C_{\text{coord}}(U_M, U_\Sigma, U_{\text{obs}}) \gt \frac{\rho_c}{\Vert\delta_{\text{critical}}^c\Vert}$$

This is the formal statement of "teams persist where individuals can't" — provided coordination overhead doesn't consume the tempo gains.

---

## 9. Structural Revisions (from discussion, 2026-03-10)

Key realizations that should reshape this spike and the theory's structure on the next pass:

### 9.1 Composition as early axiom, not multi-agent extension

The composition principle belongs near the scope condition (#050), stated as a Cox-like axiom BEFORE the single-agent results. This way, every subsequent result (persistence, gain, tempo, mismatch decomposition) is automatically understood to hold at every level of composition. No separate "multi-agent theory" needed — just a theory of agents that compose.

The axiom is roughly: "Any system satisfying the scope condition may be composed of subsystems that themselves satisfy the scope condition. The theory applies identically at every level."

When a result has composition-specific nuance (e.g., directed separation may break at the composite level due to goal-dependent communication routing), note it AT THAT RESULT rather than deferring to a separate section.

### 9.2 Section III becomes "Composition Dynamics"

With the composition axiom in Section I, Section III no longer needs to re-derive any results. It becomes all new ground: coordination structure, unity ranges, oppositionality, breakdown modes. Essentially a synonym for "multi-agent dynamics" but framed as the study of inner composition.

### 9.3 The 2-3 agent base case

Composition laws should be proved for 2 agents (and 3 where pairwise interactions don't capture everything). The n-agent case follows by induction / recursive composition. Any n-agent scenario decomposes into nested 2-agent compositions:
- The rogue 1/100 subagent = {the 99} vs {the 1}, with slightly negative teleological unity
- A team with a communication bottleneck = {subgroup A} + {subgroup B} with limited perceptual unity between them
- An organization with conflicting departments = composition at the department level with mixed teleological unity

### 9.4 The "trivial" composition case needs fixing

§2.2 currently requires "instantaneous, lossless internal communication" for the trivial case. This is wrong — it smuggles in a physically impossible idealization. The actual trivial case is: if a composite already satisfies the scope condition as a whole, AAD applies to it as one, *regardless of internal mechanism*. The internal communication quality affects the composite's effective quantities (tempo, gain), not whether it counts as an agent.

A Rube Goldberg machine that satisfies the scope condition is an agent. A team communicating via carrier pigeon is an agent. Their internals affect their fitness, not their status.

### 9.5 "Actuated" as the adjective for Section II agents

From the same discussion: "Actuated Adaptive Agents" for Section II (goal-oriented agents), vs. "Adaptive Agents" for Section I. Clean, mechanical, avoids consciousness connotations of "purposeful." "Self-actuated" reserved for future distinction (agents that set their own objectives vs. externally-supplied objectives).

### 9.6 The teleological unity scalar

The cooperation-opposition spectrum as a single scalar per objective dimension:
- +1: fully unified (effectively a single agent on this axis)
-  0: indifferent (interact but don't try to affect each other)
- -1: fully adversarial (existential opposition)

This applies per-dimension of the objective space. Most real organizations have mixed teleological unity — cooperative on some axes, competitive on others. The adversarial case is just one end of the scalar, not a separate theory.

---

## 10. Status Assessment

**What's promising here:**
- The consistency argument (§1) is strong. If AAD claims level- independence, composition laws ARE required, not optional.
- The tempo composition (§2.3) seems straightforwardly derivable from information theory — information rates from independent sources add.
- The Clausewitz mapping (§4) provides grounding in 200+ years of organizational experience and gives the unity dimensions empirical content.
- The Auftragstaktik principle as IB-optimal communication is a testable prediction.

**What needs work:**
- The unity metrics (§3) are sketches. Need formal definitions with well-defined properties.
- The coordination overhead term $C_{\text{coord}}$ is hand-waved.
  Need to formalize what coordination costs in terms of tempo.
- The "adversarial = negative teleological unity" claim (§6.1) needs careful checking — adversarial dynamics may not reduce so cleanly.
- Composition of directed separation (§2.5) has a real subtlety with goal-dependent communication routing.
- The infinite regress question (§7, item 6) needs the "atomic agent" concept to be made precise.

**What's genuinely novel:**
- The consistency argument: that composition isn't a feature of AAD but a *requirement* for its coherence.
- The formal holon definition with the composition consistency property.
- The four unity dimensions as independent axes with Clausewitz grounding.
- The Auftragstaktik principle as IB optimization.
- Team persistence as a corollary of composition + persistence condition.

**Epistemic status of this spike**: The structural argument (AAD requires composition consistency) is strong — Hypothesis verging on Derived. The specific composition laws are Sketch. The unity metrics are Discussion-grade. The Clausewitz/Auftragstaktik formalization is Hypothesis.
