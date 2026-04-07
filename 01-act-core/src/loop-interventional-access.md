---
slug: loop-interventional-access
type: derived
status: exact
depends:
  - causal-hierarchy-requirement
  - recursive-update
  - causal-structure
stage: draft
---

# Derived: Loop Provides Interventional Data Access

An agent in the feedback loop generates interventional data by construction: the agent's action $a_t$ causally precedes the next observation $o_{t+1}$, and the mismatch conditioned on $a_t$ carries interventional information. This is how agents within ACT's **agency scope** ($\mathcal{S}_{\text{agency}}$, which requires $\lvert\mathcal{A}\rvert \geq 2$ and at least one action with causal effect) gain Level 2 access — not through internal architecture, but through the loop itself. Agents in the adaptive scope but outside agency scope (passive observers) lack the action contrasts needed for interventional data.

## Formal Expression

*[Derived (loop-interventional-access, from causal-structure + recursive-update)]*

By #causal-structure, the temporal ordering is constitutive: $a_t$ causally precedes $o_{t+1}$. The agent chose $a_t$; the environment responded with $o_{t+1}$. The feedback loop therefore generates **intervention-produced data** — data whose causal character differs from passive observation because the agent's action was a genuine cause of the subsequent observation.

The critical distinction: **"action-generated data" is not the same as "cleanly identified do-estimates."** The pair $(a_t, o_{t+1})$ is produced under intervention — the agent executed $a_t$, making it interventional in character rather than a passively observed association. But between intervention-produced data and a usable estimate of $P(o \mid do(a_t), \Omega_t)$ stand: (1) coverage — the agent must have tried diverse actions, not just one policy; (2) confounding within a time step — unobserved state variables that affect both action choice and outcome; (3) delay — consequences may appear much later than $t+1$; (4) partial observability — $o_{t+1}$ reveals only part of the outcome. The strength of causal identification from this data depends on the regime ( #edge-update-causal-validity): strong in Regime A (intervention-rich domains like software and laboratory science), moderate in Regime B (partial intervention), weak in Regime C (observation-only). The claim here is about the *character* of the data (interventional, not observational), not about the agent's ability to extract clean causal estimates from it.

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

**Even agents without explicit causal models benefit.** A Q-learning agent doesn't maintain an explicit causal model, but in the tabular case with sufficient exploration and no within-step confounding, its Q-values converge toward $\mathbb{E}[R \mid s, do(a)]$ rather than $\mathbb{E}[R \mid s, A=a]$ — precisely because the training data comes from the agent's own interventions. In the partially observed, confounded, or delayed-outcome cases (where the caveats above apply), the loop still provides intervention-generated data, but the Q-values may converge to biased estimates that reflect the confounding structure rather than clean interventional effects. The loop provides Level 2 data; whether that data yields *identified* causal quantities depends on the domain's confounding and observability structure.

## Working Notes

- This result establishes that all agents within ACT's **agency scope** ( #scope-condition, $\mathcal{S}_{\text{agency}}$) have access to interventional data, regardless of their internal architecture. Agents in the adaptive scope but outside agency scope (passive observers, nominal agents with $\lvert\mathcal{A}\rvert \lt 2$ or no causal effect) lack the action contrasts needed to generate interventional data — they observe but cannot intervene. This includes LLM agents operating through a tool-use loop — the LLM issues an action (tool call), observes the result, and updates. The loop gives it Level 2 data even though its internal architecture (transformer attention) is not designed for causal reasoning. The loop compensates for architectural limitations.
- The connection to #causal-information-yield: CIY quantifies *how much* interventional information a specific action provides. This segment establishes that interventional information is *available in principle*; CIY measures the *quantity per action*.
