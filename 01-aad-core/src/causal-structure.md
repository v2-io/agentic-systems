---
slug: causal-structure
type: postulate
status: axiomatic
depends:
  - agent-environment
stage: deps-verified
---

# Postulate: Causal Structure

The agent-environment interaction has irreducible causal structure grounded in the temporal ordering of events. Actions precede their consequences; observations follow from the state they observe. This ordering is constitutive of the feedback loop and holds independent of the magnitude of the agent's influence on the environment.

## Formal Expression

*[Postulate (causal-structure)]*

The interaction history $\mathcal C_t$ ( #chronica) is not merely a set of observations and actions — it is an *ordered sequence* in which temporal position carries meaning. $a_{t-1}$ was selected before $o_t$ was received. The agent could not have used $o_t$ to select $a_{t-1}$. This asymmetry — the arrow of time — is the foundation of causal structure in the theory.

We adopt the most primitive notion of causality: **event $A$ can be a cause of event $B$ only if $A$ temporally precedes $B$.** This is weaker than (and prior to) statistical notions of causality. It is a statement about the *structure of possible influence*, not about actual influence.

## Epistemic Status

This is a *postulate* — the temporal ordering of events is a physical fact about the universe that the theory takes as given. The second law of thermodynamics, the light-cone structure of relativity, and the arrow of psychological time all enforce it, but ACT does not derive it from any of these. It is simply noted as a precondition: the theory applies to agents embedded in a universe where time has a direction.

## Discussion

**Causality as temporal ordering is the most primitive notion.** Three levels of causal reasoning derive from this foundation ( #pearl-causal-hierarchy), but the temporal notion survives even when statistical influence is negligible. An agent passively observing a system with minimal intervention still has a causal history — the temporal ordering of its observations and actions structures what it can learn and when.

**Causal structure independent of coupling strength.** The causal structure of the feedback loop is preserved even when the agent's actions have minimal effect on the environment:

- **Strong coupling** ($a_t$ significantly affects $\Omega_{t+1}$): Robot manipulation, military action. Interventional information is rich.
- **Weak coupling** ($a_t$ marginally affects $\Omega_{t+1}$): Scientific observation, small financial trades. Interventional information is sparse but non-zero.
- **Nominal coupling** ($a_t$ negligibly affects $\Omega_{t+1}$, but the agent's *choice of what to observe* produces distinguishable observation distributions): Near-passive, but still within scope — the agent's query actions generate weak but nonzero interventional contrasts. The theory applies but the interventional information per action is sparse.
- **Zero coupling** ($T(\Omega_{t+1} \mid \Omega_t, a_t) = T(\Omega_{t+1} \mid \Omega_t)$ for all $a_t$ AND observation distributions are action-independent): Actions don't affect the environment or the observations. Level 2 access vanishes. The feedback "loop" collapses to a one-way channel. **Outside the agency scope** ( #scope-condition, conditions 3-4) — the causal-information, purposeful-agent, and composition results of Sections II and III do not apply. However, zero-coupling systems remain **within the adaptive scope** ( #scope-condition, conditions 1-2) if they observe under residual uncertainty: Section I's adaptive machinery (mismatch, gain, tempo, persistence) applies to passive estimators. The causal structure postulate still holds for such systems — temporal ordering of observations is constitutive — but without interventional contrasts, the causal *hierarchy* (Level 2, Level 3) is inaccessible.

The *agency-scope* results apply to any agent whose choices make a causal difference to what it can observe, from strong coupling (robot manipulation) through weak coupling (scientific observation) to query-only coupling (choosing which question to ask). The *adaptive-scope* results apply more broadly, including to passive observers whose actions have no causal effect.

**Consequences for the feedback loop.** The irreversibility of temporal ordering yields the core structure:

- The model update is **directed** — the model at time $t$ depends on prior events, never on future ones
- The mismatch signal $\delta_t$ ( #mismatch-signal) is **retrospective** — comparing a prediction (made before $o_t$) with an observation (arriving after)
- Action selection is **prospective** — using the current model to influence future events
- The chronica ( #chronica) is **monotonically growing** — events are added but never removed

**Implications for model updating.** The causal postulate constrains the update rule: the model should give more weight to observations that are *causally downstream* of the agent's actions than to observations that would have occurred regardless. Action-contingent observations carry interventional (Level 2) information; action-independent observations carry only associational (Level 1) information. The formal measure of this distinction — causal information yield (CIY) — is developed in #causal-information-yield.

**(Descended from TF-02.)**
