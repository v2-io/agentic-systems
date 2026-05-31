# 44 - der-causal-hierarchy-requirement

Source: `01-aat-core/src/der-causal-hierarchy-requirement.md`

## First-pass understanding

This segment applies the Pearl hierarchy to the value object. Since `Q_O` is explicitly conditioned on `do(a_t=a)`, evaluating it is a Level-2 query. By the strict causal hierarchy, Level-2 quantities cannot in general be recovered from Level-1 association alone, so a purposeful agent that must learn action consequences during operation needs Level-2 knowledge or access.

The segment also introduces a named learning-agent scope. Pre-compiled controllers may act with effect and therefore remain in agency scope, but they are outside this sub-scope because their action-consequence mapping is externally supplied rather than learned or revised by the agent. This is an important narrowing for the rest of Section II.

## Diagram attempt

I drew the derivation as a chain: `Q_O` contains `do(a)`, `do(a)` is Pearl Level 2, Level 2 does not collapse to Level 1, therefore learning purposeful agents need Level-2 knowledge. A side split separates pre-compiled agents from learning agents, because that scope cut is as important as the derivation itself.

## Findings and watches

- Watch carried forward from the previous two segments: the derivation is exact only for the requirement that `Q_O` is an interventional query. It does not show that ordinary loop data already estimates the query. That burden remains on the loop/interventional-access and admissibility-regime segments.
- Watch: "purely predictive models" should mean purely associational models. A model trained on randomized interventions or containing causal/action-transition structure can make predictions about `do(a)`; the problem is not prediction as such, but Level-1-only prediction.
- Watch: the learning-agent scope cut is load-bearing. Later Section II claims that mention PID, LQR, hardcoded controllers, or thermostats need to say whether they are illustrative agency-scope examples or inside learning-agent scope.
- Spot-check: the cited Hafez et al. 2026 bipredictability/IDT result appears to exist as arXiv `2603.01283`, and search metadata reports the same broad claim: IDT detects 89.3% of perturbations versus 44.0% for reward-based monitoring with 4.4x lower median latency. This supports the empirical citation's existence, but it is evidence for coupling-monitoring performance, not by itself proof that the loop supplies identified Level-2 causal effects.

## Local verdict

The core derivation is sound when stated narrowly: if action value is a `do` query, Level-1 association alone is insufficient in general. The main audit pressure is scope propagation and making sure "needs Level 2" does not become "the loop automatically gives identified Level 2."
