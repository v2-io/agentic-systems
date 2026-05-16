# 01 - def-agent-environment

Segment: `01-aat-core/src/def-agent-environment.md`
Read after: outline-only orientation.
Dependencies: `[]` - satisfied.
Status observed: `type: definition`, `status: axiomatic`, `stage: deps-verified`.

## Reflection

This is a clean opening move: AAT begins from boundary plus mediated contact, not from purpose. The important commitment is not "there is an agent" in a folk sense, but "there is a decomposition under which an internal state is coupled to an inaccessible external state through observation and action channels." The loss boundary is doing most of the work. It makes mismatch and model-sufficiency non-vacuous before those terms exist.

The one thing I want to track is a possible naming/scope tension: this definition says an agent produces actions that affect the environment, while the outline later has `scope-agency` as a narrowing to action with Pearl-level-2 contrast. So "agent" here may mean "coupled adaptive entity with an action channel," while "agency" later means "action channel with causally contrastive/planning-relevant force." That can be fine, but future segments need to keep the two-level use crisp.

## Prompt pass

Predictions vs evidence: I expected a minimal boundary definition and got one. I did not expect the action channel to appear this strongly in the very first definition; I expected pure observer/model first and actuation second.

Cross-segment consistency: none yet. Future consistency watch: reconcile this with `scope-agency` and with any adaptive systems that observe/update but do not act.

Math verification: not applicable.

Direction next: I expect `def-action-transition` to sharpen "actions affect Omega" into a transition relation or kernel. It should probably avoid smuggling objectives or strategy into the action channel.

Errors to watch: conflating "has an action output" with "has agency under Pearl Level 2"; treating perfect-state controllers as outside all analysis rather than outside the uncertainty-bearing AAT scope; treating the agent-environment boundary as ontological rather than modeling-relative.

What I would change: possibly rename the three-condition entity here as an "agent-environment coupling" or "AAT agent candidate" if later `scope-agency` needs a narrower sense of agency. Too early to call this a finding.

Curiosity: whether AAT handles passive adaptive estimators as outside scope or as degenerate agents whose "actions" are null/internal updates. That matters because many control/inference results begin from observers before actuators.

New knowledge enabled: the audit can now ask of every later theorem whether it depends on lossy mediated observation, action effect, internal state, or all three.

Audit process change: keep a terminology watch list for `agent`, `agency`, `adaptive system`, and `actuated agent`.

Running outline change: add possible "agent/agency terminology tension" to candidate watch list only, not as a finding.

Value feel: high for framing, low for direct risk. It is foundational enough that a small ambiguity here would propagate widely.

## Diagram thought

The quickest representation is a two-box directed coupling with a deliberately narrowed observation aperture: environment is large and structurally unconstrained, agent is internal state, and the observation arrow passes through a lossy boundary while the action arrow pushes back into environment. I want the picture to emphasize asymmetry: actions affect Omega, but observations never reveal Omega directly.
