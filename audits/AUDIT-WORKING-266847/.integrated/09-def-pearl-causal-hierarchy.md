# Reflection: def-pearl-causal-hierarchy

## What the segment does

Defines Pearl's three-level causal hierarchy in the context of the feedback loop:
- L1: Association (pattern recognition over chronica)
- L2: Intervention ($do(\cdot)$ — "what if I do this?")
- L3: Counterfactual ("what if I had done differently?")

Key move: AAD grounds the hierarchy in temporal structure of the feedback loop, not just abstract graphical models. This is the "adopted and integrated" pattern — Pearl's framework is first-class here, not relegated to a positioning appendix.

## Naming targets surfaced

Row 89: "causal information yield | CIY..." — this segment doesn't define CIY but mentions it will be defined later. Still not ready to vote.

Looking for "causal hierarchy" in tracker... I don't see it as a separate target. The naming is "Pearl's causal hierarchy" which canonicalizes the adoption.

The domain instantiations table is notable — it includes "Scientific method" and "Military (Boyd)" and "Immune system." The cross-domain instantiation is the framework's integrative move.

## The "availability vs. exploitation" distinction

The Discussion's most important conceptual move is separating structural availability from actual exploitation. A Kalman + LQR system has Level 2 access *structurally* (its innovation is conditioned on prior action) but doesn't *exploit* it — the separation principle means control policy doesn't affect estimation quality. Only dual control exercises Level 2 deliberately.

This is an important distinction for the framework's breadth claims: AAD says the feedback loop provides Level 2 access, but this doesn't mean every agent within scope is using it. The claim is about what's structurally available, not about what's implemented.

## The `git checkout` insight

The claim that `git checkout` provides Level 3 counterfactual access with ground-truth verification is striking. It's exactly right: in software, you can literally execute the counterfactual by checking out an earlier commit, applying a different change, and running the same tests. No simulation required — the counterfactual outcome is observable.

This is why software is "uniquely rich" for the hierarchy. In most domains, Level 3 requires simulation; in software, it's literal. This is a genuine insight.

## Cross-segment notes

The segment imports Pearl's hierarchy with attribution (Pearl 2009; Bareinboim et al. 2022). The Bareinboim et al. theorem about strict hierarchy is cited as "load-bearing for Section II." Good epistemic practice — citing the external theorem rather than claiming it.

## The Kalman filter row in the domain table

The domain table notes that a Kalman filter with LQR "has Level 2 access structurally present but the separation principle guarantees estimation quality is invariant to control policy." The table entry is "Innovation conditioned on action" (Level 2) and "Not typically exercised" (Level 3). This matches the Discussion note about the separation principle.

But: the Level 2 entry says "innovation conditioned on action" — this is standard Kalman filter behavior. The innovation (prediction error) depends on what the controller was doing. Is this Level 2 in Pearl's sense? It's not quite $do(a_{t-1})$ because the action itself was determined by the control law, not by a deliberate intervention. The distinction between "the action was causally prior" and "the action was an intervention in Pearl's sense" matters here.

Actually the segment handles this: conditions for Level 2 include "(2) the agent chose the action (it was not determined by the same causes that determine the observation)." For Kalman+LQR, the action *is* determined by the same causal system (it's the LQR policy applied to the estimated state). So strictly speaking, Kalman+LQR might not have Level 2 access in Pearl's sense for the control actions — the action is endogenous to the estimation system. This could be a nuanced gap.

## Wandering thoughts

The three levels of causal reasoning have different learning-theoretic consequences. Level 1 data is available from passive observation but only captures correlations. Level 2 requires randomization or deliberate intervention. Level 3 requires a structural causal model.

For AI agents (logogenic agents), the interesting question is: what level of causal reasoning can a language model exercise? LLMs are typically trained on Level 1 data (text is associational). They can simulate Level 2 and Level 3 reasoning in language (predicting what would happen if X, reasoning about counterfactuals) but the *ground truth verification* is absent. An LLM reasoning about "what would happen if I do X" is exercising something that looks like Level 2 but is actually Level 1 data about what typically happens when people do X. This is the fundamental epistemic limitation of language-only agents.

This connects to the directed separation failure for goal-conditioned LLMs — they can't cleanly separate epistemic update from goal-directed reasoning because both happen in the same representational substrate. The Pearl hierarchy makes this limitation precise.

How valuable: 7/10 for surprise (the git checkout insight and the Kalman+LQR availability-vs-exploitation distinction), 9/10 for load-bearing (grounds all of Section II's causal claims).
