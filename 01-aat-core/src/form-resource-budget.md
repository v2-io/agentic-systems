---
slug: form-resource-budget
type: formulation
status: conditional
depends:
  - def-adaptive-tempo
  - def-strategy-dimension
stage: draft
---

# Formulation: Resource Budget

A depletable scalar reservoir whose drain rate rises with mismatch and whose level gates correction capacity — the minimal structure that makes "a degrading model is more expensive to run" a dynamical statement rather than an informal one.

The construction is minimal: a scalar resource budget $\mathcal B_t$ evolving under drain-versus-replenishment, with two introduced structural posits — **(A-cost)** the drain rate $c(\lVert\delta\rVert)$ is non-decreasing in mismatch (degrading models cost more to run), and **(A-gate)** the sector parameter is resource-gated via $\alpha(\mathcal B) = \alpha^{\max}\psi(\mathcal B)$ with $\psi(0)=0$ (the depleted agent loses corrective capacity entirely). Hard-budget regime has zero replenishment ($r_{\mathcal B}=0$, a finite pool that only depletes); regenerative regime has $r_{\mathcal B}\gt 0$.

This segment is *exploratory off-spine*: no Section I/II/III result depends on it; it opens a resource-structure axis #def-strategy-dimension explicitly records as an open scope item. The formulation is *conditional by nature* — (A-cost) and (A-gate) are modeling assertions about an agent's physical realization, not derivations from core machinery, so the formulation's epistemic ceiling stays at `conditional` regardless of downstream development. The companion derivation #der-resource-bounded-destabilization uses this formulation to close #der-adversarial-destabilization's Effects-Spiral by an alternative mechanism (agent's own correction-rate decay rather than adversary coupling growth).

## Formal Expression

AAT's core machinery is resource-blind: the policy $\pi(M_t, G_t)$ acts at no modeled cost, and correction capacity (tempo $\mathcal T$, #def-adaptive-tempo) does not deplete. #def-strategy-dimension records this as an explicit open scope item — for resource-constrained agents (embodied controllers under torque/battery/episode-length limits; teams under headcount; any agent whose every corrective action spends an exhaustible pool) the formalism carries no state for the pool and no coupling from model quality to its drain. This formulation introduces the minimal such structure.

*[Definition (resource-budget)]*

A scalar **resource budget** $\mathcal B_t \geq 0$ (calligraphic-scalar by the NOTATION convention exception, as for $\mathcal T$; distinct from the agent label $B$ of #der-adversarial-destabilization and from the strategy-edge set $E$). Its evolution:

$$\frac{d\mathcal B}{dt} \;=\; -\,c\big(\lVert\delta\rVert\big) \;+\; r_{\mathcal B}$$

where $\delta$ is the agent's mismatch ( #def-mismatch-signal), $c(\cdot)\geq 0$ is the **correction-cost rate**, and $r_{\mathcal B}\geq 0$ is the **replenishment rate**. The hard-budget regime is $r_{\mathcal B}=0$ (a finite pool that only depletes — a combat episode's battery, a fixed torque-integral, a bounded step count); the regenerative regime is $r_{\mathcal B}\gt 0$.

The formulation is fixed by two structural posits — introduced, not derived from existing AAT.

*[Assumption (A-cost: cost rises with mismatch)]*

$c$ is non-decreasing in $\lVert\delta\rVert$, with $c(0)\gt 0$ (running the loop at all costs something) and $c$ strictly increasing where $\lVert\delta\rVert\gt 0$. Minimal concrete form:

$$c\big(\lVert\delta\rVert\big) \;=\; c_0\big(1 + \beta_{\mathcal B}\,\lVert\delta\rVert\big), \qquad c_0\gt 0,\ \beta_{\mathcal B}\geq 0.$$

*Motivation, not derivation:* a model that is wrong by $\delta$ actuates partly in wrong directions — the agent pays for the corrective action *and* for the wasted component, and re-observes more often to recover. Degradation is literally more expensive to carry. $\beta_{\mathcal B}=0$ recovers the resource-blind special case (cost independent of model quality).

*[Assumption (A-gate: tempo is resource-gated)]*

The sector/correction rate the persistence machinery uses — $\alpha$ in #result-sector-persistence-template, equal to $\mathcal T$ in the canonical epistemic instantiation ( #def-adaptive-tempo, #result-persistence-condition) — is throttled by available resource:

$$\alpha(\mathcal B) \;=\; \alpha^{\max}\,\psi(\mathcal B), \qquad \psi:\mathbb{R}_{\geq 0}\to[0,1]\ \text{non-decreasing},\ \ \psi(0)=0,\ \ \psi(\mathcal B)\to 1\ \text{as}\ \mathcal B\to\infty.$$

*Motivation, not derivation:* with the pool exhausted the agent cannot run its observe–update–actuate loop at full rate (fewer sensor sweeps, slower control cycle, fewer remaining episode steps). $\psi\equiv 1$ recovers the resource-blind special case (constant $\alpha$, exactly today's template).

Together: $\mathcal B_t$ is the new state; (A-cost) couples model quality *into* its drain; (A-gate) couples its level *into* correction capacity. These two couplings are exactly what close the otherwise-open feedback in #der-adversarial-destabilization's Effects-Spiral corollary — the consequence is derived in #der-resource-bounded-destabilization.

## Epistemic Status

*Conditional.* This is a representational choice (`type: formulation`) — several resource models would fit (per-action cost vectors, capacity constraints on the action set, queueing-theoretic service limits); $\mathcal B_t$ with (A-cost)/(A-gate) is the *minimal* one that makes the model-quality → drain → capacity loop dynamical with one added scalar and two monotone couplings. The defined objects ($\mathcal B_t$, the depletion law) are well-posed; the *content* is the two posits, which are introduced premises, honest as modeling commitments and not consequences of any prior segment. Anything downstream is conditional on them.

**Max attainable: `conditional`.** This ceiling is intrinsic: (A-cost) and (A-gate) are claims about a particular agent's physical realization, not about the formalism, so no amount of derivation promotes the formulation itself beyond conditional. A *specific* agent class can satisfy them by construction (e.g. a controller whose actuation energy is measured and whose control-loop frequency is power-throttled), at which point downstream results inherit that class's tighter status — but the formulation as stated stays conditional by nature, the same way #def-strategy-dimension's other scope items do.

This segment is an exploratory branch: it opens a resource-structure axis AAT has deliberately lacked. No spine segment depends on it; it is not a prerequisite of any Section I/II/III result.

## Discussion

**What the two posits buy, minimally.** Everything load-bearing downstream uses only *monotonicity*: (A-cost) that drain is non-decreasing in mismatch, (A-gate) that capacity is non-decreasing in budget with $\psi(0)=0$. The explicit linear $c$ and the shape of $\psi$ are illustrative; the qualitative consequences in #der-resource-bounded-destabilization survive any $(c,\psi)$ obeying the monotonicity and the endpoint $\psi(0)=0$. The endpoint matters: $\psi(0)=0$ encodes "an empty pool cannot correct at all," which is what makes exhaustion *terminal* rather than merely *slowing*.

**Why a new scalar rather than folding into $\rho$ or $\mathcal T$.** Resource is not disturbance: $\rho$ is mismatch injected by the world, independent of how well the agent is doing; $\mathcal B_t$ drains *because* the agent is doing badly (A-cost). Nor is it tempo: $\mathcal T$ is a rate the agent has; $\mathcal B_t$ is a stock it spends to exercise that rate. Collapsing resource into either erases the very coupling that makes the Effects-Spiral close — a degrading model raising its own future cost is a stock-flow statement, not a rate statement. The new scalar is the minimum that keeps stock and flow distinct.

**Relationship to the adaptive reserve $\Delta\rho^\ast$.** #result-sector-persistence-template's adaptive reserve $\Delta\rho^\ast=\alpha R-\rho$ is a *margin* (how much extra disturbance the agent can absorb at its current rate); $\mathcal B_t$ is a *fuel* (how much correction it can still afford to perform). They are independent: an agent can have comfortable margin and an almost-empty pool, or ample fuel and zero margin. The resource-bounded result is precisely about a system that is margin-safe at full fuel and still dies as the fuel drains the margin away — see #der-resource-bounded-destabilization.

**Domain instances.** Embodied combat/contested control under a battery or torque-integral budget (the case that motivated this branch); a development team under a fixed person-hour pool where a worsening codebase model raises rework cost; an incident-response org whose escalating confusion burns the on-call budget faster. In each, the resource-blind special case ($\beta_{\mathcal B}=0$, $\psi\equiv 1$) is the agent for whom the pool is effectively infinite relative to the engagement — and there the existing constant-$\alpha$ machinery is exactly right, which is the honest boundary of this branch's relevance.

## Working Notes

- The regenerative regime $r_{\mathcal B}\gt 0$ with $\mathcal B_t$ bounded above (a finite-capacity rechargeable pool) is the genuinely open dynamical case — it is a time-varying-$\alpha$ template instantiation in full and may be quasi-stationary-distribution / absorbing-barrier-flavored (cf. the open second no-go in the continuity-persistence reasoning trail). #der-resource-bounded-destabilization treats only $r_{\mathcal B}=0$ rigorously; the regenerative case is flagged there and not attempted.
- Reasoning trail: `spikes/fight/03-energy-bound-effects-spiral.md` (the Φ-prompted derivation attempt that produced this branch) and `spikes/fight/99-verdict.md` §3.
- Open: whether $\mathcal B_t$ should be vector-valued (distinct pools — energy vs compute vs attention — with distinct $c,\psi$). Scalar is the minimal first cut; the persistence machinery it feeds is itself scalar-default with a tensor extension ( #def-adaptive-tempo), so a vector $\mathcal B$ would compose with that tensor form. Not pursued here.
- A NOTATION.md entry for $\mathcal B_t$ is added under a resource section; per the NOTATION drift caveat the segment, not the index, is ground truth.
