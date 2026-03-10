---
slug: adaptive-tempo
type: definition
status: definitional
depends:
  - update-gain
  - event-driven-dynamics
---

# Adaptive Tempo

The adaptive tempo is the effective rate at which an agent acquires useful information and reduces model-reality mismatch. It is the product of how often the agent acts/observes and how effectively it updates its model from those observations.

## Formal Expression

*[Definition (adaptive-tempo)]*

$$\mathcal{T} = \sum_k \nu^{(k)} \cdot \eta^{(k)*}$$

where:
- $\mathcal{T}$ is the adaptive tempo.
- $k$ indexes the agent's distinct observation channels.
- $\nu^{(k)}$ is the event rate on channel $k$ (frequency of observation/action cycles).
- $\eta^{(k)*}$ is the optimal update gain on channel $k$ (#update-gain).

In the single-channel special case, this reduces to:
$$\mathcal{T} = \nu \cdot \eta^*$$

## Epistemic Status

This is a *definition*. It establishes the scalar (or vector, in the per-dimension extension) quantity that characterizes an agent's total corrective capacity, combining both the speed of the loop ($\nu$) and the epistemic quality of the update ($\eta^*$).

## Discussion

**Speed-Quality Substitutability.** The formulation $\mathcal{T} = \nu \cdot \eta^*$ formally captures the substitutability of speed and quality. An agent can achieve the same adaptive tempo by running a fast, noisy loop (high $\nu$, low $\eta^*$) or a slower, highly calibrated loop (low $\nu$, high $\eta^*$). 
- Improving *both* is multiplicative: a 50% increase in speed and a 50% increase in gain yields a $1.5 \times 1.5 = 2.25\times$ improvement in adaptive tempo.
- This grounds Boyd's emphasis on "Orient" quality: out-pacing an adversary isn't purely about cyclic speed ($\nu$); a superior model (yielding better $\eta^*$) can generate higher $\mathcal{T}$ even with slower physical reflexes.

**Observation Noise Gating.** Because $\eta^* = U_M / (U_M + U_o)$, high observation noise ($U_o$) depresses the gain, effectively collapsing the adaptive tempo regardless of how fast the agent's loop runs. You cannot outrun a bad observation channel just by iterating faster. 

**Centrality to Persistence.** Adaptive tempo is the core capacity metric of ACT. It forms the left side of the persistence condition (#persistence-condition), counterbalancing the rate of environmental disturbance $\rho$. If $\mathcal{T}$ falls below the normalized disturbance rate, the agent loses contact with reality.