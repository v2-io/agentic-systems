---
slug: loop-interventional-access
type: derived
status: exact
depends:
  - causal-hierarchy-requirement
  - recursive-update
  - causal-structure
---

# Derived: Loop Provides Interventional Data Access

An agent in the feedback loop generates interventional data by construction: the agent's action $a_t$ causally precedes the next observation $o_{t+1}$, and the mismatch conditioned on $a_t$ carries interventional information. This is how agents within ACT's scope gain Level 2 access — not through internal architecture, but through the loop itself.

## Formal Expression

*[Derived (loop-interventional-access, from causal-structure + recursive-update)]*

By #causal-structure, the temporal ordering is constitutive: $a_t$ causally precedes $o_{t+1}$. The agent chose $a_t$; the environment responded with $o_{t+1}$. This is an intervention — the agent varied its action and observed the result.

Formally: the pair $(a_t, o_{t+1})$ is generated under an intervention policy — the agent executed $a_t$, making it a genuine intervention rather than a passively observed association. The data *contains interventional signal*: it was produced by a do-operation, not by conditioning on a naturally occurring value of $A_t$.

However, this does not mean the agent automatically has access to a clean estimate of $P(o \mid do(a_t), \Omega_t)$. Between the interventional act and a usable interventional distribution stand: (1) coverage — the agent must have tried diverse actions, not just one policy; (2) confounding within a time step — unobserved state variables that affect both action choice and outcome; (3) delay — consequences may appear much later than $t+1$; (4) partial observability — $o_{t+1}$ reveals only part of the outcome. The claim is about the *character* of the data (interventional, not observational), not about the agent's ability to extract clean causal estimates from it.

The mismatch signal conditioned on the agent's action:

$$\delta_t \mid a_t = o_{t+1} - \hat{o}_{t+1}(M_t, a_t)$$

carries interventional information: it tells the agent how the environment responded to its specific intervention $a_t$, relative to what the model predicted.

## Epistemic Status

*Exact.* This is a logical consequence of temporal ordering ( #causal-structure) and the feedback-loop structure ( #scope-condition). The claim is about **data availability**, not reasoning capacity — the loop *provides* interventional data whether or not the agent *exploits* it for Level 2 reasoning. Whether the agent uses this data to build causal models depends on its update mechanism and model class.

The precision is important: we claim the agent has *access to* interventional data, not that it *correctly identifies* interventional structure. Confounding within a single time step, delayed outcomes, and partial observability can all complicate the extraction of clean causal signals from the loop data.

## Discussion

**The loop as a Level 2 engine.** This is one of ACT's load-bearing results. The causal hierarchy theorem ( #causal-hierarchy-requirement) says Level 2 knowledge requires more than correlational data. This result says: the adaptive loop *is* the "more." An agent that acts and observes the consequences is generating interventional data — the same kind of data that a scientist generates through experiments. The loop is a perpetual experiment.

**Precision about what "interventional" means here.** The interventional interpretation is strongest when:
- The agent's action was the primary cause of the observed change (low confounding)
- The observation follows closely in time (short delay)
- The agent varied its action across episodes (not stuck on one policy)

When confounding is high, delays are long, or the agent follows a fixed policy, the interventional information in each $(a_t, o_{t+1})$ pair is weaker — still present, but harder to extract. This is why #causal-information-yield distinguishes between high-CIY actions (that reveal causal structure) and low-CIY actions (that don't).

**Even agents without explicit causal models benefit.** A Q-learning agent doesn't maintain an explicit causal model, but its Q-values converge toward $\mathbb{E}[R \mid s, do(a)]$ rather than $\mathbb{E}[R \mid s, A=a]$ precisely because the training data comes from the agent's own interventions. The loop provides Level 2 data; the agent's learning algorithm determines whether that data is used effectively.

## Working Notes

- This result establishes that ALL agents within ACT's scope ( #scope-condition) have access to interventional data, regardless of their internal architecture. This includes LLM agents operating through a tool-use loop — the LLM issues an action (tool call), observes the result, and updates. The loop gives it Level 2 data even though its internal architecture (transformer attention) is not designed for causal reasoning. The loop compensates for architectural limitations.
- The connection to #causal-information-yield: CIY quantifies *how much* interventional information a specific action provides. This segment establishes that interventional information is *available in principle*; CIY measures the *quantity per action*.
