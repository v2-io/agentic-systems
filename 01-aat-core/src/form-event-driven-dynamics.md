---
slug: form-event-driven-dynamics
type: formulation
status: robust-qualitative
depends:
  - post-causal-structure
  - def-observation-function
  - def-action-transition
  - form-agent-model
stage: deps-verified
---

# Formulation: Event-Driven Dynamics

The agent-environment interaction is formulated at a finer grain than discrete clock ticks: as a stream of atomic **events** — observation arrivals and action completions — at potentially variable and heterogeneous rates across multiple channels. Discrete-time notation, where a single observation and a single action alternate at a fixed rate, becomes the special case of uniform-interval events on a single channel. The motivation is realism: real agents face multiple observation channels at different rates (a robot's camera at $30\text{Hz}$, LIDAR at $10\text{Hz}$, GPS at $1\text{Hz}$; a human's vision, audition, proprioception; a developer's compiler output, test results, and production telemetry), multiple action channels with different latencies, and asynchronous arrivals. The event-driven formulation handles all of these natively.

Two new measurable quantities are introduced alongside the event stream. **Event information content** $\mathcal{I}(e_\tau)$ measures, for any individual event, the mutual information it carries about the environment state conditioned on the agent's current model — an event the model already predicts carries little information; an event that surprises the model carries much. This anticipates the mismatch signal ( #def-mismatch-signal). **Channel-specific observation uncertainty** $U_o^{(k)}$ measures the noise characteristic of each channel separately — a noisy channel provides lower-quality information per event, and any sensible update rule must weight channels accordingly. From these the chapter's *effective adaptation rate* falls out immediately as the sum across channels of channel-rate times optimal gain — the adaptive tempo construct ( #def-adaptive-tempo) that the framework will lift to first-class status, presented here as the natural multi-channel generalization the discrete-time formulation cannot easily express.

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

An event that the model already predicts carries little information ($\mathcal{I} \approx 0$). An event that surprises the model carries much ($\mathcal{I} \gg 0$). This connects directly to the mismatch signal ( #def-mismatch-signal).

**Channel-specific observation uncertainty**:

*[Definition (channel-uncertainty)]*

$$U_o^{(k)} = \text{observation uncertainty of channel } k$$

Different channels have different noise characteristics. A noisy channel (high $U_o^{(k)}$) provides lower-quality information per event. The update gain ( #emp-update-gain) should weight channels accordingly.

## Epistemic Status

This is a *formulation choice*, not a postulate. The event-driven representation extends #post-causal-structure's recursive update to heterogeneous, asynchronous multi-channel interactions. The discrete-time form ($M_t = f(M_{t-1}, o_t, a_{t-1})$) from #der-recursive-update is a special case sufficient for many formal analyses — the event-driven formulation is needed only when multi-rate or asynchronous channels matter.

## Discussion

**Why events rather than clock ticks.** The discrete-time notation $M_t = f(M_{t-1}, o_t, a_{t-1})$ presupposes a single clock synchronizing observations and actions. Real agents face:

- **Multiple observation channels** at different rates (a robot's camera at 30Hz, LIDAR at 10Hz, GPS at 1Hz; a human's vision, audition, proprioception; a developer's compiler output, test results, and production telemetry)
- **Multiple action channels** with different latencies (a robot's wheel motors vs. arm actuators; an organization's operational decisions vs. strategic pivots)
- **Asynchronous arrival** — observations not synchronized with each other or with action completions

The event-driven formulation handles all of these naturally. The discrete-time form is the special case where a single observation and a single action alternate at a fixed rate.

**The effective adaptation rate.** The agent's overall capacity to track environmental changes is the sum of information gained across all channels per unit time:

$$\nu_{\text{eff}} = \sum_k \nu^{(k)} \cdot \eta^{(k)*}$$

This quantity — identical to adaptive tempo $\mathcal{T}$ ( #def-adaptive-tempo) — is the central measure of an agent's adaptive fitness.

**Software-specific channels.** In the software development domain, the event-driven formulation maps naturally to the developer's multi-rate observation channels:

| Channel $k$ | Rate $\nu^{(k)}$ | Noise $U_o^{(k)}$ |
|-------------|------------------|-------------------|
| Compiler/linter output | Per-save (high) | Very low |
| Unit test results | Per-run (medium) | Low |
| CI pipeline | Per-push (medium) | Low |
| Runtime telemetry | Continuous (variable) | Medium |
| Bug reports | Sporadic (low) | High |
| Code review feedback | Per-PR (low) | Medium-high |

The three-part tempo decomposition for software — $\mathcal{T}_{\text{obs}}$ (compiler, tests) + $\mathcal{T}_{\text{explore}}$ (code reading) + $\mathcal{T}_{\text{probe}}$ (test runs, staging) — is a direct application of multi-channel tempo. The formal development of this decomposition is a TST-side question (open GAP in `02-tst-core/OUTLINE.md`).
