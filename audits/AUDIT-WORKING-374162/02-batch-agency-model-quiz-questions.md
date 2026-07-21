# Comprehension Quiz — Batch 2 (through `form-information-bottleneck`)

*Coverage: cumulative through Chapter 2's first two segments (agency scope, causal-structure postulate, reality-model chapter intro, agent model, information bottleneck). Cumulative questions may draw on batch-1 material.*

## (1) Critical Mental Model

### Q b02-1.1 [mental-model]
State the two conditions the agency scope adds to the adaptive scope, in plain language. Then the trap: why is "the agent has at least two actions to choose from" *not sufficient* for agency, even with genuine free choice among them?

### Q b02-1.2 [mental-model]
AAT postulates causal structure. Is AAT's causal postulate (a) Pearl's structural-causal-model framework, (b) statistical causal influence, or (c) something weaker than both? State the postulate in one sentence and explain its relationship to the Pearl hierarchy (which comes first, and why they are not identical).

### Q b02-1.3 [mental-model]
An agent whose every action is `git status`-like — pure queries that change nothing in the world but determine what it observes next: is it inside or outside the agency scope? Now the harder version: an agent whose actions *do* change the world, but whose effects never surface through its observation channel. Inside or outside? Explain the principle that decides both cases.

### Q b02-1.4 [mental-model]
"The model $M_t$ is whatever the agent believes about the world, one component of its internal state." What does the completeness assumption actually say, why is it stronger than this paraphrase, and what makes the assumption honest rather than sleight-of-hand (where does its cost get paid)?

### Q b02-1.5 [mental-model]
Explain why the framework says forgetting old information in a volatile environment is *not* evidence that the agent has tightened its compression preferences. What single mathematical fact does this rest on?

### Q b02-1.6 [mental-model]
The reality-model chapter introduction distinguishes two "adequacy questions" about an agent's model. Name both, and state which one, when it comes back bad, cannot be fixed by any amount of learning — and what the prescribed remedy is instead.

## (2) Mathematics

### Q b02-2.1 [math]
Write the agency-scope membership condition formally (the full set expression, including what it intersects). What does the existential quantifier range over, and what asymmetry does it permit (an agent with 100 actions of which how many must be effective)?

### Q b02-2.2 [math]
Write the IB objective as the segment states it, with AAT's specific bindings of Tishby's $X$, $T$, $Y$. Which variable is the relevance target — and why is it *not* $\Omega$?

### Q b02-2.3 [math]
The information-bottleneck segment carries `type: formulation` and `status: exact` simultaneously. Reconcile these — precisely which element has formulation status and which content is exact?

### Q b02-2.4 [math]
The Markov chain $Y - X - T$ is said to hold "by construction" under AAT's bindings. Spell out why (what structural fact about $M_t$ makes it hold), and name one downstream agent class for which a prior auditor flagged it might fail.

### Q b02-2.5 [math]
Trap: "In a high-volatility environment, the optimal agent lowers $\beta$ to compress more aggressively." Diagnose the error using the objective's structure: through *which mathematical object* does volatility $\rho$ actually enter, and what is $\beta$'s correct interpretation?

### Q b02-2.6 [math]
In post-causal-structure's coupling taxonomy, write the formal condition for *zero coupling*, and state exactly which scopes a zero-coupling system falls inside/outside of, and which parts of the theory still apply to it.

### Q b02-2.7 [math]
Given that the reality-model compression $\phi$ is many-to-one, is $I(M_t; \mathcal C_t) \leq H(\mathcal C_t)$ an inequality the IB objective *needs* to impose, or is it automatic? What does the compression-cost term $I(M_t;\mathcal C_t)$ measure in words?

## (3) Implications

### Q b02-3.1 [implications]
A frontier lab claims their tool-using LLM agent "operates at Pearl Level 2 because its tool calls are interventions." Using the structural-availability vs exploitation distinction, and the observation-mediated boundary, give the two separate questions you would ask to evaluate the claim.

### Q b02-3.2 [implications]
Why is the *nominal agent* (choices with no causal contrast) a category worth naming at all — what does its visibility buy for analysis of, say, a "boxed" AI whose only outputs go to a log nobody reads? Which parts of AAT still describe that system?

### Q b02-3.3 [implications]
In the information-bottleneck segment's Formal Expression, the β-vs-ρ paragraph is announced as the first instance of a named recurring discipline. Name the discipline, state its general form (what it refuses to do and why), and explain what "routes to a different repair" means using the β/ρ instance: if an agent is failing in a volatile world, which knob does the framework say to reach for, and which not?

### Q b02-3.4 [implications]
Terminology hazard question: the word "nominal" appears in both scope-agency and post-causal-structure. Explain the collision precisely — what does each usage denote, and are the two referents inside or outside the agency scope? (An agent that answers this cleanly has read both segments; a summary cannot supply it.)

### Q b02-3.5 [implications]
Policy-relativity of the IB objective means predictive information depends on what the agent will do. Give one substantive consequence of this for (a) generalist vs specialist agents, and (b) the coming directed-separation story — why does policy-relativity create at least apparent tension with "epistemic update is goal-blind"?

### Q b02-3.6 [implications]
The framework claims each scope narrowing "buys" results. For the agency narrowing specifically: name the *mechanism* by which the narrowing pays (what kind of data becomes available that adaptive-scope systems structurally lack, and which single scope condition is responsible).
