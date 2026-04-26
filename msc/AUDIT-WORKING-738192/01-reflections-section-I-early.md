# Reflection: Section I (Early Segments)

Segments read:
- `def-agent-environment.md`
- `def-observation-function.md`
- `def-action-transition.md`
- `scope-adaptive-system.md`
- `scope-agency.md`
- `post-composition-consistency.md`
- `def-chronica.md`
- `post-causal-structure.md`
- `def-pearl-causal-hierarchy.md`

## 1. Predictions vs Evidence
I predicted that the discrete vs continuous arrival of events might be glossed over. So far, the formulation is very clean. The `scope-agency` and `scope-adaptive-system` segments are very precise in their inclusion/exclusion criteria.

## 2. Cross-segment consistency
`post-composition-consistency.md` references Tier 1/2/3 agents and the composition bridge lemma. It states that for Tier 1, Section I/II results transfer exactly. This places a massive burden on `#form-composition-closure`. I need to watch closely when I read Section III to see if this transfer is genuinely exact or if it requires unstated assumptions (like perfect communication or zero latency).

## 3. Math verification (if applicable)
No heavy math yet, mostly definitions and scope.

## 4. Specific Finding / Concern: Level 3 Counterfactuals in Software
In `def-pearl-causal-hierarchy.md`, the text claims:
> "In software development, `git checkout` provides Level 3 access with ground-truth verification — the agent can literally execute the counterfactual. This is one of software's unique epistemic properties"

**Critique:** `git checkout` resets the *codebase state*, but it does not reset the *environment* perfectly. In Pearl's terms, a counterfactual is $P(y_{x'} \mid x, y)$. Running `git checkout` and trying $x'$ happens at time $t+k$, not time $t$. The developer's mind has changed (they learned from $x$), external dependencies might have changed, and time has passed. While software is highly reproducible (much more so than physics or biology), calling `git checkout` a "ground-truth verification" of a Level 3 counterfactual might be an overclaim. It is a highly reliable Level 2 intervention (reset state and do $x'$). It approaches Level 3 only if the entire testing environment and evaluator are purely deterministic and stateless. I should see if `02-tst-core/src/obs-software-epistemic-properties.md` nuances this. If it doesn't, this is a finding.

## 5. What errors should I watch for?
- Check if downstream segments conflate Level 2 reproducible interventions with true Level 3 counterfactuals.
- Watch for the exact conditions of "Tier 1" agents in composition.

## 6. Next steps
Read the next batch of Section I segments:
- `form-agent-model.md`
- `form-information-bottleneck.md`
- `def-model-sufficiency.md`
- `def-model-class-fitness.md`
- `form-event-driven-dynamics.md`
