---
slug: form-agent-model
type: formulation
status: robust-qualitative
depends:
  - def-agent-environment
  - def-observation-function
  - def-chronica
stage: deps-verified
---

# Formulation: The Reality Model

The agent's internal representation of how the world works is committed to a specific form: $M_t = \phi(\mathcal C_t)$ — a many-to-one compression of the chronica into a model space $\mathcal M$. This is named honestly as a formulation choice rather than a derived result: alternative formulations exist (history-based policies that map $\mathcal C_t$ directly to actions without an explicit model state), but AAT commits to analyzing agents as carrying a state object $M_t$ that mediates between history and future action. $M_t$ is the substrate of prolepsis — the object from which predictions are generated and against which observations are compared.

The compression is many-to-one *by design*: multiple distinct histories may produce the same model state, and that is the essential function of the model — retaining what matters and discarding what does not. The formalism is deliberately agnostic about *how* an agent realizes $M_t$: a Kalman filter holds a state estimate plus covariance matrix; a reinforcement-learning agent holds a value function; a developer holds a mental model of a codebase; a language-model agent holds its context-window contents plus retrieved memory. The formalism asks only that $M_t$ exist as a well-defined object that the agent's policy can condition on.

The load-bearing commitment carried by the notation is the **completeness assumption**: by writing $M_t = \phi(\mathcal C_t)$, AAT assumes $M_t$ captures *everything* the agent retains from its history. Anything not in $M_t$ is, by construction, lost to the agent. This is what makes $M_t$ the complete epistemic substate rather than merely one component of a richer internal representation. Whether $M_t$ retains *enough* information for adaptive work is a separate question, taken up in #def-model-sufficiency. The formalism accommodates degenerate cases by allowing $\mathcal M$ to range from trivial (a PID controller's $M_t$ retains only error signal and its integral/derivative, with no predictive capability) to rich (full world model). The impoverished end of this range lands in the "blind seeker" region of the agent spectrum ( #def-agent-spectrum).

## Formal Expression

*[Formulation (agent-model)]*

$$M_t = \phi(\mathcal{C}_t)$$

where:
- $\phi: \mathcal{C}^\ast \to \mathcal{M}$ maps interaction history to model space $\mathcal{M}$
- $\mathcal C_t = (o_1, a_1, \ldots, o_t)$ is the chronica ( #def-chronica) — the complete record of agent-environment interaction
- $\mathcal{M}$ is the space of possible models the agent can hold

The mapping $\phi$ is a many-to-one compression: multiple distinct histories may produce the same model state. This is not a deficiency — it is the essential function of the model: retaining what matters and discarding what does not.

## Epistemic Status

*Robust qualitative.* This is a *formulation* — a representational commitment, not a derived result. We choose to analyze agents as maintaining a state object $M_t$ that mediates between history and future action. Alternative formulations exist (e.g., history-based policies that map $\mathcal C_t$ directly to actions without an explicit model). The formulation is justified by its analytical utility: it enables the information bottleneck analysis ( #form-information-bottleneck), the mismatch decomposition ( #def-mismatch-signal), and the gain principle ( #emp-update-gain). The formulation is robust — any agent that conditions its actions on retained information can be described this way — but the specific commitment to a complete, compressed state $M_t$ is a modeling choice, not a derivation.

## Discussion

**$M_t$ is the epistemic substate.** It captures "what the agent believes about reality." Different agents realize $M_t$ differently: a Kalman filter holds a state estimate and covariance matrix; an RL agent holds a value function; a developer holds a mental model of codebase architecture; an LLM agent holds its context window contents plus retrieved memory. The formalism is agnostic to the realization — it asks only that $M_t$ exist as a well-defined object that the agent's policy can condition on.

**Completeness assumption.** By writing $M_t = \phi(\mathcal C_t)$, we assume that $M_t$ captures everything the agent retains from its history. Any information not in $M_t$ is lost to the agent. This is what makes $M_t$ the complete epistemic substate, not merely one component of a richer internal representation. Whether $M_t$ retains *enough* information is the subject of #def-model-sufficiency.

**Degenerate cases.** A PID controller's $M_t$ is degenerate — it retains only the error signal and its history (integral, derivative), with no predictive capability beyond extrapolating recent trends. It occupies the "blind seeker" region of the agent spectrum ( #def-agent-spectrum): its $O_t$ (setpoint) is clear but its $M_t$ is too impoverished to support the adaptive dynamics of Section I. The formalism accommodates this by allowing $\mathcal{M}$ to range from trivial (scalar) to rich (full world model).
