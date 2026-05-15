---
slug: hyp-auftragstaktik-principle
type: hypothesis
status: discussion-grade
depends:
  - def-shared-intent
  - def-unity-dimensions
  - def-adaptive-tempo
stage: draft
---

# Hypothesis: Auftragstaktik Principle

For a composite agent with limited communication bandwidth, the optimal allocation prioritizes sharing objectives over strategies over models. This captures the structural insight of Auftragstaktik (mission-type tactics): investing communication bandwidth in shared purpose (teleological unity) while accepting lower epistemic and strategic unity, granting sub-agents autonomy to adapt locally. The model predicts the same priority ordering that military doctrine discovered empirically; whether the mechanism (IB-optimal bandwidth allocation) is the actual reason Auftragstaktik works is an open question.

## Formal Expression

*[Hypothesis (auftragstaktik-principle)]*

Let a composite agent's total inter-agent communication bandwidth be $B = B_O + B_\Sigma + B_M$, allocated across objective sharing ($B_O$), strategy coordination ($B_\Sigma$), and model synchronization ($B_M$).

The hypothesis: the allocation that maximizes composite tempo $\mathcal{T}_c$ (or equivalently, minimizes coordination overhead $C_{\text{coord}}$) prioritizes:

$$B_O \gt B_\Sigma \gt B_M$$

when:
- Objectives change slowly relative to strategies: $\nu_O \ll \nu_\Sigma$
- Strategies change slowly relative to models: $\nu_\Sigma \ll \nu_M$
- Sub-agents have sufficient local adaptive capacity: each $\mathcal{T}_i \gt \rho_i^{\text{local}} / \Vert\delta_{\text{critical}}^i\Vert$

The priority ordering follows from the IB framework ( #def-shared-intent): the bits with the longest shelf life and highest coordination value per bit should be transmitted first. Objectives change slowly and enable autonomous coordination (sub-agents who share objectives can independently choose compatible strategies). Models change fast and provide diminishing coordination value (two agents with the same model but different objectives still conflict).

## Epistemic Status

*Discussion-grade.* Max attainable: empirical. The priority ordering is a qualitative prediction grounded in the IB framework and supported by extensive military-organizational evidence (Bungay's analysis of Clausewitz, Wehrmacht doctrine, modern mission command). But it is not derived — the IB optimization would need to be solved explicitly with realistic cost functions to confirm the ordering, and the conditions under which the ordering reverses (e.g., when model synchronization is critical because the situation is genuinely ambiguous) are not characterized. The empirical evidence is strong but comes primarily from one domain (military command); generalization to software teams, AI agent swarms, and other settings is plausible but unverified.

## Discussion

**When the ordering reverses.** The prioritization $B_O \gt B_\Sigma \gt B_M$ assumes sub-agents can independently construct adequate local models. When the environment is genuinely ambiguous and local observations are insufficient (fog of war, novel codebase, unprecedented market conditions), model synchronization may be worth more than objective sharing — sub-agents who share the same wrong model at least err consistently, which is sometimes better than each having a different wrong model.

**Bungay's evidence.** In *The Art of Action*, Bungay documents that organizations consistently fail by inverting this priority: they over-invest in controlling *how* subordinates act (strategy sharing, $B_\Sigma$) rather than ensuring subordinates understand *why* (objective sharing, $B_O$). The result: subordinates who follow instructions precisely but cannot adapt when conditions change, because they lack the teleological context to improvise intelligently.

**The software team instantiation.** A well-functioning development team has:
- High $B_O$: clear product goals, understood by all (sprint goals, feature objectives)
- Moderate $B_\Sigma$: architectural decisions shared, implementation details autonomous
- Low $B_M$: each developer builds their own mental model of the code they touch; full codebase understanding is neither expected nor efficient

When this inverts (micromanagement of implementation details, unclear product goals), team tempo drops — consistent with the Auftragstaktik prediction.

**Connection to Conway's Law.** Conway's Law (system structure mirrors communication structure) is a consequence: when $B_\Sigma$ is low and $B_O$ is high, sub-agents coordinate through shared objectives rather than explicit action coordination, producing systems whose boundaries reflect objective decomposition rather than communication channels.

## Working Notes
- The formal IB derivation of the priority ordering would need: (1) a model of how each unity dimension contributes to composite tempo, (2) the rate of change of each shared quantity ($\nu_O$, $\nu_\Sigma$, $\nu_M$), (3) the communication cost per bit for each type. The qualitative argument is that objectives are compact and slow-changing (high bits-per-cost, long shelf life), while models are large and fast-changing (low bits-per-cost, short shelf life). Formalizing this is tractable but has not been done.
- The principle may need qualification for AI agent teams where model synchronization is cheap (shared vector databases, persistent memory) but objective alignment is hard (prompt engineering, RLHF). The cost structure differs from human organizations.
