---
slug: event-driven-dynamics
type: formulation
status: robust-qualitative
depends:
  - causal-structure
  - observation-function
  - action-transition
stage: deps-verified
---

# Formulation: Event-Driven Dynamics

The coupling between agent and environment occurs through discrete events — observations arriving and actions completing — at potentially variable and heterogeneous rates. Discrete-time notation is the special case of uniform-interval events on a single channel.

## Formal Expression

*[Formulation (event-driven-dynamics)]*

**Event** ($e$): An atomic unit of agent-environment interaction, typed as:
- **Observation event**: $e = (\text{obs}, k, o^{(k)})$ — a datum arriving on observation channel $k$
- **Action completion**: $e = (\text{act}, j, r^{(j)})$ — the result of action $j$ completing

**Event stream** ($\mathcal{E}$): The temporally ordered sequence of all events:

$$\mathcal{E} = \{(e_1, \tau_1), (e_2, \tau_2), \ldots\} \quad \text{where } \tau_1 \leq \tau_2 \leq \cdots$$

**Channel rate** ($\nu^{(k)}$): The characteristic event rate of channel $k$, which may vary over time.

**Event information content**: The mutual information between the event and the environment state, conditioned on the current model:

*[Definition (event-information-content)]*

$$\mathcal{I}(e_\tau) = I(e_\tau;\, \Omega_\tau \mid M_{\tau^-})$$

An event that the model already predicts carries little information ($\mathcal{I} \approx 0$). An event that surprises the model carries much ($\mathcal{I} \gg 0$). This connects directly to the mismatch signal ( #mismatch-signal).

**Channel-specific observation uncertainty**:

*[Definition (channel-uncertainty)]*

$$U_o^{(k)} = \text{observation uncertainty of channel } k$$

Different channels have different noise characteristics. A noisy channel (high $U_o^{(k)}$) provides lower-quality information per event. The update gain ( #update-gain) should weight channels accordingly.

## Epistemic Status

This is a *formulation choice*, not a postulate. The event-driven representation extends #causal-structure's recursive update to heterogeneous, asynchronous multi-channel interactions. The discrete-time form ($M_t = f(M_{t-1}, o_t, a_{t-1})$) from #recursive-update is a special case sufficient for many formal analyses — the event-driven formulation is needed only when multi-rate or asynchronous channels matter.

## Discussion

**Why events rather than clock ticks.** The discrete-time notation $M_t = f(M_{t-1}, o_t, a_{t-1})$ presupposes a single clock synchronizing observations and actions. Real agents face:

- **Multiple observation channels** at different rates (a robot's camera at 30Hz, LIDAR at 10Hz, GPS at 1Hz; a human's vision, audition, proprioception; a developer's compiler output, test results, and production telemetry)
- **Multiple action channels** with different latencies (a robot's wheel motors vs. arm actuators; an organization's operational decisions vs. strategic pivots)
- **Asynchronous arrival** — observations not synchronized with each other or with action completions

The event-driven formulation handles all of these naturally. The discrete-time form is the special case where a single observation and a single action alternate at a fixed rate.

**The effective adaptation rate.** The agent's overall capacity to track environmental changes is the sum of information gained across all channels per unit time:

$$\nu_{\text{eff}} = \sum_k \nu^{(k)} \cdot \eta^{(k)*}$$

This quantity — identical to adaptive tempo $\mathcal{T}$ ( #adaptive-tempo) — is the central measure of an agent's adaptive fitness.

**Software-specific channels.** In the software development domain, the event-driven formulation maps naturally to the developer's multi-rate observation channels:

| Channel $k$ | Rate $\nu^{(k)}$ | Noise $U_o^{(k)}$ |
|-------------|------------------|-------------------|
| Compiler/linter output | Per-save (high) | Very low |
| Unit test results | Per-run (medium) | Low |
| CI pipeline | Per-push (medium) | Low |
| Runtime telemetry | Continuous (variable) | Medium |
| Bug reports | Sporadic (low) | High |
| Code review feedback | Per-PR (low) | Medium-high |

The three-part tempo decomposition for software — $\mathcal T_{\text{obs}}$ (compiler, tests) + $\mathcal T_{\text{explore}}$ (code reading) + $\mathcal T_{\text{probe}}$ (test runs, staging) — is a direct application of multi-channel tempo. This decomposition is a Section IV gap (see the three-part tempo decomposition gap in `ACT-FULL.md`).

**(Descended from TF-04.)**
