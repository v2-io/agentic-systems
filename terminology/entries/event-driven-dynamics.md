---
slug: event-driven-dynamics
schema_version: 1
term: event driven dynamics
name: Event-Driven Dynamics
notation:
brief: The formulation of agent-environment coupling as discrete typed events (observation arrivals, action completions) at variable, heterogeneous rates — the generalization of uniform-clock discrete time.
layer: framing-vocabulary
status: canon
tags: [structural_concepts, core_quantities]
source_type: asf
primary_source: 01-aad-core/src/form-event-driven-dynamics.md
first_asf_mention: 01-aad-core/src/form-event-driven-dynamics.md
see_also: [tempo, adaptive-system, chronica, developer-agent]
aliases: []
do_not_confuse: []
---

Standard discrete-time notation $M_t = f(M_{t-1}, o_t, a_{t-1})$ presupposes a single clock
synchronizing all observations and actions. Real agents face multiple observation channels at
different rates and multiple action channels with different latencies. The event-driven
formulation handles this naturally.

An **event** $e$ is typed as either an observation event $(\text{obs}, k, o^{(k)})$ or an action
completion $(\text{act}, j, r^{(j)})$. The **event stream** is the temporally ordered sequence of
all events. **Channel rate** $\nu^{(k)}$ is the characteristic event rate of channel $k$.

The agent's overall adaptive capacity is:

$$\nu_{\text{eff}} = \sum_k \nu^{(k)} \cdot \eta^{(k)*}$$

— identical to adaptive tempo $\mathcal{T}$, emerging naturally from the multi-channel structure.
Discrete-time notation is the special case where a single observation and action alternate at
a fixed rate. The event-driven formulation is needed when multi-rate or asynchronous channels
matter — e.g., a developer with compiler output at per-save rates, CI at per-push rates, and
production telemetry continuously.

Defined in [`#form-event-driven-dynamics`](../../01-aad-core/src/form-event-driven-dynamics.md).
