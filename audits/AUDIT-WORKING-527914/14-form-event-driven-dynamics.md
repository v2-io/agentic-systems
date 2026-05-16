# 14 - form-event-driven-dynamics

Segment: `01-aat-core/src/form-event-driven-dynamics.md` (`#form-event-driven-dynamics`)

Dependencies: `post-causal-structure`, `def-observation-function`, `def-action-transition`, `form-agent-model`, all read. Dependency-order check passes. The discussion references `#der-recursive-update` and `#def-adaptive-tempo` downstream, but the event formulation is locally understandable.

## Segment Read

This segment formulates agent-environment coupling as an asynchronous stream of typed events rather than synchronized clock ticks. Events can be observation arrivals or action completions; channels have rates and uncertainty; event information content is mutual information with the environment conditioned on the current model.

The core move is that discrete time is a special case. Real agents have multiple channels with heterogeneous rates and latencies, so event-driven dynamics is the more general formulation.

## Predictions Vs Evidence

I predicted early Section I would build toward tempo and gain. This segment introduces the event-rate side of that machinery before adaptive tempo is formally defined.

The software channel table is more concrete than I expected this early. It reinforces why TST is a natural calibration domain: compiler, tests, CI, telemetry, bug reports, and review feedback are visibly multi-rate observation channels.

## Cross-Segment Consistency

The segment uses causal temporal ordering from `#post-causal-structure` and observation/action functions from the opening definitions. It extends $M_t$ to $M_{\tau^-}$ around events, which is consistent with the model-state formulation.

No contradiction. One notation issue: it writes $\eta^{(k)*}$ in display text rather than `\eta^{(k)\ast}`; that is formatting rather than naming, and not my current task.

## Naming Notes

`event-driven dynamics` is accurate and should probably be kept. It names the representational choice: events are the primitive update triggers, not clock ticks.

`event stream` is also strong and standard. It should not need invention.

`event information content` is descriptive but a bit long. It is probably fine because it names a formal quantity $\mathcal I(e_\tau)$ and is unlikely to be a conversational centerpiece.

`channel uncertainty` may need disambiguation later because $U_o^{(k)}$ is specifically observation uncertainty per channel. If the card has a target, I would prefer "channel-specific observation uncertainty" as first-use gloss and "channel uncertainty" after context is clear.

## What This Enables

This segment enables adaptive tempo as information gained per unit time across channels, multi-timescale analysis, software observation-channel decomposition, and logogenic context/turnover analysis where events arrive asynchronously.

For naming, it reinforces that tempo terms should distinguish rate, quality, and uncertainty. "Fast channel" is not enough if $U_o$ is high and gain should be low.

## Watchlist

- Whether `event-driven dynamics` remains formulation-level or gets mistaken for a claim that all agents explicitly operate event loops.
- Names that conflate channel rate $\nu^{(k)}$ with adaptive tempo $\mathcal T$ before gain/quality weighting.
- Software tempo decomposition targets should wait for TST defining segments.

## Wandering Thoughts

The event-driven framing feels necessary for the framework to handle real systems. Clock ticks are convenient for math, but actual agents are interrupted by the world. Events arrive when they arrive, with different noise profiles and different action latencies.

This is also a good bridge between abstract AAD and the experience of using software tools. A compiler error, a test failure, a production alert, and a code review comment are all observations, but they differ radically in rate and uncertainty. Naming them all as channels makes the analogy precise rather than metaphorical.

`Event-driven dynamics` is not flashy, but it is exactly the right kind of engineering-math phrase. It tells a reader what changes in the formulation without pretending the idea is novel in itself.

The segment also foreshadows why "tempo" has to be more than speed. Fast noisy events can produce little useful update; slow reliable events can matter more. Names around tempo should preserve the product of rate and update quality.
