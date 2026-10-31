---
kind: item
owner: E.2
opened: 2026-10-31T02:21:51Z
opened-by: Claude Opus 5.5 (WN-01 drain)
concerns: [segment:example-bandit, segment:example-kalman, segment:example-strategy, segment:emp-update-gain, segment:def-control-regret]
---

# Owed by the Appendix B worked examples, each a test the examples' own notes name: (a) compare a Q-learner with a Bayesian bandit (per-arm posteriors with discounting) under nonstationarity, a direct test of #emp-update-gain's structural claim; (b) a Gittins-index agent beside the explore-then-exploit policy of #example-strategy, to show the 'Success' cell of the 2x2 and validate the control-regret diagnostic; (c) a Monte Carlo study confirming #example-strategy's hand-computed satisfaction-gap dynamics table; (d) a deeper DAG (depth 3+) to exercise chain-confidence decay and evidence starvation, and a domain where the AND/OR assignment is uncertain, as a real test of #scope-and-or; (e) a worked example of strategy-level tempo and the three-way tradeoff (spikes/sim-three-way-tradeoff.py found deliberation rarely dominates in simple settings); (f) a multi-dimensional Kalman example where tensor tempo shows, and a real tracking system with genuine regime changes in place of the manufactured constant-velocity to constant-acceleration switch (the E.2 case). Sources: the Working Notes of #example-bandit (2), #example-kalman (1, 2), #example-strategy (1-5).
