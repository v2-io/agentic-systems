# TF-04: Event-Driven Dynamics (Formulation)

The coupling between agent and environment occurs through discrete **events** — observations arriving (*aisthesis*) and actions completing (*praxis*) — at potentially variable and heterogeneous rates.

**Epistemic status**: This is a *formulation choice*, not an axiom. The event-driven representation extends TF-02's recursive update to heterogeneous, asynchronous multi-channel interactions and handles real-world multi-rate systems without aliasing. The discrete-time form ($M_t = f(M_{t-1}, o_t, a_{t-1})$) is a special case sufficient for many formal analyses.

## Definitions

**Event** ($e$): An atomic unit of agent-environment interaction, typed as:
- **Observation event**: $e = (obs, k, o^{(k)})$ — a datum arriving on observation channel $k$
- **Action completion**: $e = (act, j, r^{(j)})$ — the result of action $j$ completing

**Event stream** ($\mathcal{E}$): The temporally ordered sequence of all events:

*[Definition]*
$$\mathcal{E} = \{(e_1, \tau_1), (e_2, \tau_2), \ldots\} \quad \text{where } \tau_1 \leq \tau_2 \leq \cdots$$

**Channel rate** ($\nu^{(k)}$): The characteristic event rate of channel $k$, which may vary over time.

## The Event-Driven Update

TF-02 derives the recursive update $M_{\tau^+} = f(M_{\tau^-}, e_\tau)$ from the temporal axiom and scope constraints. In the multi-channel setting, events are typed by channel, and the update function $f$ may be channel-specific.

## Why Events Rather Than Clock Ticks

The discrete-time notation $M_t = f(M_{t-1}, o_t, a_{t-1})$ presupposes a single clock synchronizing observations and actions. Real agents face:

- **Multiple observation channels** at different rates (a robot's camera at 30Hz, LIDAR at 10Hz, GPS at 1Hz; a human's vision, audition, proprioception)
- **Multiple action channels** with different latencies (a robot's wheel motors vs. arm actuators; an organization's operational decisions vs. strategic pivots)
- **Asynchronous arrival** — observations are not synchronized with each other or with action completions

The event-driven formulation handles all of these naturally. The discrete-time form $M_t = f(M_{t-1}, o_t, a_{t-1})$ (TF-02) is the special case where a single observation and a single action alternate at a fixed rate — a useful simplification for many formal analyses.

## Information Content of Events

Each event carries information about the environment, measured relative to the current model. The **event information content** is the mutual information between the event and the environment state, conditioned on the current model:

*[Definition]*
$$\mathcal{I}(e_\tau) \;=\; I(e_\tau;\, \Omega_\tau \mid M_{\tau^-})$$

where $I(\cdot;\cdot \mid \cdot)$ is conditional mutual information (TF-00). An event that the model already predicts carries little information ($\mathcal{I} \approx 0$). An event that surprises the model carries much information ($\mathcal{I} \gg 0$). The mismatch signal (TF-05) quantifies this surprise.

## Channel-Specific Reliability

Different observation channels have different noise characteristics:

*[Definition]*
$$U_o^{(k)} = \text{observation uncertainty of channel } k$$

A noisy channel (high $U_o^{(k)}$) provides lower-quality information per event. A reliable channel (low $U_o^{(k)}$) provides higher quality. The update gain (TF-06) should weight channels accordingly.

## Effective Adaptation Rate

The agent's overall capacity to track environmental changes is the sum of information gained across all channels per unit time:

*[Definition]*
$$\nu_{\text{eff}} = \sum_k \nu^{(k)} \cdot \eta^{(k)*}$$

where $\nu^{(k)}$ is channel $k$'s event rate and $\eta^{(k)\ast}$ is the effective gain on that channel (how much each event from that channel improves the model; see TF-06).

This quantity — **effective adaptation rate** — is a central measure of an agent's adaptive fitness, with consequences derived in TF-11.
