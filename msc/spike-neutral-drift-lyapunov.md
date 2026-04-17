# Spike: Miller's Extreme Transition Motif in AAD's Lyapunov Framework

**Status**: Exploratory analysis -- mapping Miller's five-phase transition pattern onto AAD's sector-condition/persistence machinery. Honest assessment of what maps and what doesn't.

**Date**: 2026-04-06

---

## Phase Mapping

**Phase 1 (Stable epoch)** maps cleanly. Two populations each satisfy the persistence condition: $\alpha > \rho/R$, with positive adaptive reserve $\Delta\rho^* = \alpha R - \rho > 0$. Neither can invade the other because each agent's correction machinery outpaces the disturbance the other generates -- the adversarial destabilization threshold (#adversarial-destabilization) is not met in either direction: $\gamma_A \cdot \mathcal{T}_A < \Delta\rho^*_B$ and vice versa. Clean analog.

**Phase 2 (Neutral invasion)** is where the framework breaks. A variant $\nu$ appears that is *structurally different but behaviorally identical in the current context*. AAD has no concept for this. The sector condition cares only about $\alpha$, $\rho$, and $R$ -- observable behavioral parameters. Two agents with identical $(\alpha, \rho, R)$ are indistinguishable to the Lyapunov analysis regardless of their internal architecture. The variant $\nu$ has the same $\alpha$ and $R$ as the incumbent but a *different correction function* $F_\nu$ that happens to satisfy the same sector bound in the current disturbance regime. AAD's state space literally cannot see this agent. See "The Critical Gap" below.

**Phase 3 (Neutral drift)** is invisible to AAD. The population composition changes but all observable dynamics ($\dot{V}$, $R^*$, $\Delta\rho^*$) are unchanged. The system's *vulnerability* to future perturbation increases, but nothing in the Lyapunov function or the persistence condition tracks this. The adaptive reserve $\Delta\rho^*$ looks the same.

**Phase 4 (Niche creation + cascading displacement)** partially maps. Once $\nu$ reaches critical mass, it changes the effective environment -- creating new disturbance patterns that $\mu$ (in the subordinate population) can exploit. This looks like a coupled destabilization (#adversarial-destabilization) where the coupling coefficients $\gamma$ suddenly become nonzero or change sign. The self-reinforcing $\nu$/$\mu$ dynamic resembles the effects spiral, but *constructive*: $\nu$ increases $\mu$'s fitness, $\mu$'s success changes the environment in ways that favor $\nu$. The team-persistence decomposition (#team-persistence) captures the cooperative side: $\nu$ and $\mu$ effectively reduce each other's $\rho^{\text{eff}}$. But the *emergence* of this coupling from a previously zero state is not captured -- the framework treats $\gamma$ as given, not as something that appears when population composition crosses a threshold.

**Phase 5 (Consolidation)** maps cleanly to a new stable epoch with updated parameters. The structural-change-as-parametric-limit framework (#structural-change-as-parametric-limit) describes how the system settles into a simplified form -- the new regime's $\Sigma_t$ has been pruned of failed branches and stabilized.

## The Critical Gap: Behavioral Equivalence Classes

AAD's sector condition defines an *equivalence class* over correction functions: any $F$ satisfying $\delta^T F \geq \alpha \|\delta\|^2$ within $\|\delta\| \leq R$ is treated identically. Miller's motif depends on structure *within* this equivalence class -- two correction functions that are indistinguishable under the current disturbance regime $w(t)$ but respond differently to a disturbance regime $w'(t)$ that doesn't yet exist.

This is analogous to unused representational capacity in the model class. The variant $\nu$ has the same $R$ and $\alpha$ *for the current $w(t)$* but different behavior at the boundary or under novel disturbances. The sector condition is a worst-case bound within a region; it says nothing about *how* correction is achieved across that region. Two agents can share a sector bound while having very different correction landscapes.

The concept AAD needs: **latent structural diversity** -- variation in $F$ (or in model class $\mathcal{M}$, or in strategy DAG $\Sigma_t$) that is invisible to persistence analysis under current conditions but becomes consequential under regime change. This is not model capacity ($R$), not adaptive reserve ($\Delta\rho^*$), not mismatch -- it is a property of the *population's distribution over correction architectures*, not of any individual agent's dynamics.

## Can the Same Lyapunov Coupling Model Handle Both?

The adversarial effects spiral (#adversarial-destabilization) and the constructive $\nu$/$\mu$ cascade share the same formal structure: coupled dynamics where one agent's state change alters the other's parameters. The difference is sign -- destructive coupling increases $\rho$, constructive coupling decreases it. The team-persistence decomposition already has both terms. So *given* the coupling coefficients, yes, the same Lyapunov framework handles both.

The gap is that Miller's motif requires the coupling coefficients themselves to be *endogenous* -- emerging from population composition rather than given exogenously. The $\gamma$ in #adversarial-destabilization is a parameter; in Miller's motif it is a function of the population state. Formalizing this requires a population-level Lyapunov analysis where $\gamma(\text{composition})$ is itself a dynamical variable.

## Does the Sector Condition Need Extension?

Not exactly. The sector condition is doing its job -- it characterizes persistence given current parameters. What is missing is a *meta-level* analysis of how the *distribution of agents satisfying the sector condition* affects system robustness to regime change. During neutral drift, every individual agent's persistence analysis is unchanged, but the population's resilience profile shifts because architectural homogeneity is decreasing.

This is a composition-level concern (#composition-consistency), not a single-agent concern. The sector condition operates at the agent level. Miller's motif operates at the population level. AAD's composition framework (Section III) would need to track not just whether composite persistence holds, but how the *diversity of correction architectures* within a composite affects robustness to novel disturbance regimes. This connects to the open question of composition laws.

## Summary Assessment

| Phase | AAD Analog | Quality of Mapping |
|-------|-----------|-------------------|
| 1. Stable epoch | Persistence condition + adversarial threshold | Clean |
| 2. Neutral invasion | *None* -- invisible to sector condition | Gap |
| 3. Neutral drift | *None* -- no population-level diversity tracking | Gap |
| 4. Niche creation | Effects spiral (constructive) + team persistence | Partial -- coupling emergence missing |
| 5. Consolidation | Structural change as parametric limit | Clean |

The honest conclusion: AAD's single-agent Lyapunov machinery cleanly captures the *endpoints* (stable epochs) and partially captures the *crisis* (Phase 4 as coupled destabilization). It is structurally blind to the *setup* (Phases 2-3) because the sector condition is a behavioral bound, not an architectural fingerprint. Formalizing Miller's full motif would require extending AAD's composition framework to track latent structural diversity -- the distribution of correction architectures within a population, not just whether each agent individually satisfies the persistence condition.
