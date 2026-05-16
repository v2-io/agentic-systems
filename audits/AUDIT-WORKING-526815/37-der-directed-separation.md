# 37 - der-directed-separation

Source: `01-aat-core/src/der-directed-separation.md`

## First-pass understanding

This segment introduces directed separation as a conditional architectural property of the complete agent state `X_t = (M_t, G_t)`: once an event `e_tau` is realized, the epistemic update `M_{tau+} = f_M(M_{tau-}, e_tau)` is goal-blind, while the goal update may depend on the new model, `G_{tau+} = f_G(G_{tau-}, M_{tau+}, e_tau)`, and policy still depends on both `M_t` and `G_t`. The important distinction is between goal-conditioned event selection, which is allowed because goals influence policy/action and thus which events occur, and goal-conditioned event processing, which is outside Class 1 separation.

The piece is unusually honest about scope: Class 1 has estimator/planner separation, Class 2 has partial coupling, and Class 3 has coupled epistemic-purposeful mechanisms such as many LLM agents. That helps protect earlier Section I quantities: model update, mismatch, sufficiency, and tempo can still be meaningful when separation fails, but the clean sequential orient cascade and factorized update do not carry automatically. The segment also surfaces a bounded-signaling assumption: it assumes goal state reaches the world through action, with limited goal leakage through behavior. That assumption matters a lot for humans, rich robots, and prompted LLMs.

## Diagram attempt

The clearest diagram is a conditional-dependence graph with two channels. The allowed channel is `G -> policy/action -> event -> M+`: goals may shape which evidence arrives. The forbidden channel is `G -> f_M -> M+` after conditioning on `e_tau` and `M_{tau-}`. I tried to make the visual diagnostic `kappa_processing` sit directly on the forbidden channel so that the diagram does not accidentally imply that all goal/evidence dependence is leakage.

## Findings and watches

- Candidate finding: the headline directed-separation equations should be phrased as conditional on the directed-separation scope. The segment marks `status: conditional` and later says Class 3 agents fail the condition, but the opening formulation can still read as though goal-blind `f_M` has been derived for complete agents in general.
- Candidate finding: `kappa_processing = I(G_t; M_{tau+} | e_tau, M_{tau-}) / H(G_t | e_tau, M_{tau-})` needs a support condition or convention for cases where the denominator is zero. If the goal is already known after conditioning on event and prior model, the ratio is undefined even though the structural question remains meaningful.
- Watch: the behavioral estimator needs to hold prior epistemic state fixed when varying goals. In prompt-based or recurrent agents, changing the goal often changes the context and thus `M_{tau-}`, which would confound goal-conditioned processing with a different prior model state.
- Watch: the bounded-signaling assumption should probably become an explicit scope condition rather than remaining an acknowledged implicit assumption. Without it, goal state can leak through latency, style, attention, tool choices, or other rich behavior even when nominal action channels look coarse.

## Local verdict

The core distinction is useful and seems conceptually load-bearing: selection dependence is not processing dependence. The strongest audit pressure is not on that distinction, but on the exact status of the theorem-like language and the operational diagnostic. The segment is strongest when it presents directed separation as a classifying assumption/property; it is weaker when it sounds like a consequence of merely decomposing `X_t` into `M_t` and `G_t`.
