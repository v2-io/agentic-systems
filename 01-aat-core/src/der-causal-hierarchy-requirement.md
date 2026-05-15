---
slug: der-causal-hierarchy-requirement
type: derived
status: exact
depends:
  - def-value-object
  - def-pearl-causal-hierarchy
  - scope-agency
stage: deps-verified
---

# Derived: Causal Hierarchy Requirement

Evaluating the action-value $Q_O$ requires answering "what happens if I *do* action $a$?" — a Level 2 (interventional) query in Pearl's causal hierarchy. An agent that must learn the answer to this question during operation needs access to causal structure beyond what purely predictive models can provide.

## Formal Expression

*[Derived (causal-hierarchy-requirement, from value-object + pearl-causal-hierarchy)]*

Action selection via #def-value-object requires:

$$Q_O(M_t, a;\, \pi_{\text{cont}}, N_h) = \mathbb{E}\!\left[V_{O_t}(\tau) \;\middle\vert\; M_t,\; do(a_t = a),\; a_{t+1:} \sim \pi_{\text{cont}}\right]$$

The $do(\cdot)$ notation is explicit: this is an *intervention*, not a *conditioning on observed data*. By #def-pearl-causal-hierarchy, Level 2 queries ($P(Y \mid do(X))$) cannot in general be computed from Level 1 data ($P(Y \mid X)$) alone. Therefore:

An agent that must evaluate $Q_O$ from experience needs access to Level 2 knowledge — knowledge about the effects of its own interventions, not merely correlational patterns.

*[Scope Narrowing (learning-agent scope)]*

We restrict attention to **learning purposeful agents** — agents that must **acquire or refine** Level 2 knowledge during operation. This is a named sub-scope of the agency scope defined in #scope-agency. It excludes agents with **pre-compiled** interventional structure:
- PID controllers (the designer pre-computed the control law)
- LQR (separation principle gives optimal policy from model parameters)
- Hardcoded reactive policies

Pre-compiled agents are within agency scope (they have objectives and act on them) but outside learning-agent scope — their causal structure was externally supplied by a designer who had Level 2 access. **All remaining Section II results operate within learning-agent scope** unless explicitly noted otherwise. This scope narrowing focuses the theory on agents that must build or maintain their own causal understanding.

## Epistemic Status

*Exact.* The derivation is a direct application of the causal hierarchy theorem (Bareinboim et al. 2022) to the value-object definition. If you accept that $Q_O$ is an interventional query and that the causal hierarchy is strict, the conclusion follows. The scope narrowing to learning agents is a definitional restriction, not a derived result — it sharpens the class of agents under study.

## Discussion

**The causal hierarchy theorem does the heavy lifting.** The key mathematical fact is external to AAD: Bareinboim et al. (2022) prove that the three levels (association, intervention, counterfactual) form a strict hierarchy — Level 2 quantities cannot in general be computed from Level 1 data. AAD's contribution is applying this to the purposeful-agent setting: if you want to select actions by their consequences ($Q_O$), you need causal structure.

**What "Level 2 knowledge" means concretely.** For different agents:
- A developer needs to know "if I refactor this module, will tests still pass?" (not just "modules that were refactored tend to have tests that fail")
- A commander needs to know "if I move forces north, will the enemy respond by retreating?" (not just "when forces moved north, the enemy often retreated")
- An RL agent needs $Q(s, a) = \mathbb{E}[R \mid s, do(a)]$, not $\mathbb{E}[R \mid s, A=a]$ (the latter includes selection bias from the agent's own policy)

The distinction between $do(a)$ and $A = a$ is the core of causal inference. It matters whenever the agent's action-selection policy correlates with unobserved confounders.

**Why pre-compiled agents are excluded.** A thermostat "knows" that turning on the heater raises temperature — but this knowledge was designed in, not learned. The thermostat never needs to reason about interventions because the intervention-outcome mapping is hardwired. AAD's purposeful-agency machinery is specifically for agents that face uncertainty about how their actions affect the world and must reduce that uncertainty through experience.

**Bi-predictability as empirical evidence for Level 2 advantage.** Hafez et al. (2026) measure the information structure of the agent-environment loop via bi-predictability $P = \text{MI}(S,A; S') / C$, capturing how tightly coupled the agent is to its environment through the action channel. Their Information Digital Twin (IDT), which monitors the loop's information geometry, detects environmental perturbations at 89% accuracy versus 44% for reward-based monitoring. This is consistent with the present segment's claim: the feedback loop provides richer (Level 2) data than outcome monitoring alone. Hafez's framework measures the coupling; AAD explains *why* the coupling is information-theoretically superior — because the loop generates interventional data by construction ( #der-loop-interventional-access), not merely associational data. The measurement (Hafez) and the explanation (AAD) are complementary.

## Working Notes

- This scope narrowing connects to #norm-explicit-strategy-condition: agents that must learn Level 2 structure face a cost-benefit tradeoff between learning through exploration (costly, slow, but verifies causal links) and planning through explicit $\Sigma_t$ (cheaper if the causal model is adequate, but the model may be wrong).
- LLMs trained on causally-structured text absorb causal priors — noisy prior knowledge from mixed provenance (experimental, observational, speculative). This is not verified interventional structure; it's a *prior* (plausible, not derived). An LLM in the adaptive loop has both: priors from training AND interventional data from the loop. The priors accelerate; the loop verifies. The IB framework ( #form-information-bottleneck) predicts causal structure will be retained in training because it has predictive power for language.
- The scope narrowing to "learning agents" is generous — it includes any agent that updates its causal beliefs during operation, even if it starts with strong priors. The excluded class (pure pre-compiled controllers) is genuinely different: they never revise their action-consequence model.
