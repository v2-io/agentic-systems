# Comprehension Quiz — Batch 4 (through `def-causal-information-yield`)

*Coverage: cumulative through action selection, the mismatch signal and its decomposition, the update gain, and causal information yield.*

## (1) Critical Mental Model

### Q b04-1.1 [mental-model]
"An agent's prediction error can always be driven toward zero with a good enough model." Refute this precisely: how many distinct components does expected squared mismatch decompose into, which are reducible and by what means, and what are the *two different senses* of "irreducible" among the non-modeling terms?

### Q b04-1.2 [mental-model]
An agent's mismatch signal has been near zero for a long time. List the three distinct situations consistent with this, say which one is desirable, and name the mechanism the framework later introduces because of exactly this ambiguity.

### Q b04-1.3 [mental-model]
Define gain collapse and its two etiologies. Why do the two produce behaviorally identical agents, and what would you need access to (beyond behavior) to tell them apart?

### Q b04-1.4 [mental-model]
Trap: "Causal information yield measures how much an agent learns from taking an action." Correct this, give the canonical counterexample, and state the exact logical relationship between CIY and learning (necessary? sufficient? both?).

### Q b04-1.5 [mental-model]
What is action fluency, how is it formally characterized, and why is it *not* the same as model sufficiency? Give the segment's canonical example of high-sufficiency/low-fluency.

### Q b04-1.6 [mental-model]
The framework claims there is a structural pressure toward implicit (non-deliberative) action. State the mechanism of the pressure, the three conditions that strengthen it, and the conditions under which deliberation nonetheless remains essential.

## (2) Mathematics

### Q b04-2.1 [math]
Write the framework's three-term decomposition of expected squared mismatch, with the precise definitions of the two reference predictors involved ($\hat o_t^{\mathrm B}$ and $\bar o_t$). Which global assumption makes the cross-terms vanish, what does it assert, and is the vanishing an independence or an orthogonality argument?

### Q b04-2.2 [math]
In the mismatch decomposition (the three-term split of expected squared mismatch), the middle term is called a "floor." Floor for *whom*, exactly — which class of predictors does it bind, and what is the *only* route the framework names for moving it? Also: state the alignment qualifier — why is $H(\Omega_t\mid \mathcal C_t) \gt 0$ necessary but not sufficient for the floor to be positive.

### Q b04-2.3 [math]
Write the framework's optimal update-gain formula and the corresponding update rule. Then state the tier structure precisely: in what regime is the form *exact*, what theorem grounds that regime, and what exactly is preserved outside it?

### Q b04-2.4 [math]
The optimal update-gain formula needs $U_o$ (observation-noise uncertainty), but the noise distribution was declared unknowable to the agent. State the paradox and its resolution as the framework gives it (including what the gain becomes, structurally, under the resolution, and where the stability proof is deferred to).

### Q b04-2.5 [math]
Write the canonical definition of causal information yield (CIY), including the reference distribution, state AAT's default choice of that distribution, and explain one consequence of the choice (what does CIY partly measure under the policy-induced default, and what comparability property is lost across choices?).

### Q b04-2.6 [math]
For a Kalman filter at the steady-state optimum: what is the innovation variance, and how does it exhibit the mismatch decomposition's middle floor? (Identify which piece of $HP^-H^\top + R$ is which term.)

### Q b04-2.7 [math]
Exactly which claim in der-action-selection is `exact` and which part is explicitly discussion-grade? And what is the cleaner restatement of the exact claim that makes the Part I / Part II forms one statement?

## (3) Implications

### Q b04-3.1 [implications]
A monitoring team celebrates driving a production model's prediction error to nearly the noise floor and proposes further architecture work to eliminate the rest. Using the mismatch decomposition: what two things should you tell them, and what specific failure mode does "chasing the floors" produce (name and mechanism)?

### Q b04-3.2 [implications]
Post-causal-structure claimed agents should "give more weight to causally-downstream observations." Having now read the gain and CIY segments: through which mechanism does the framework actually deliver causal weighting — the update rule or somewhere else? Be precise about what the gain weights by, and where causal considerations actually enter.

### Q b04-3.3 [implications]
A veteran engineer dismisses a failing test as flaky; a new hire rewrites an architecture because one test failed. Cast both in gain vocabulary ($U_M$, $U_o$), state which is closer to optimal in which circumstances, and what the framework prescribes when either engineer moves to a radically new codebase — with the named failure mode if the prescription is ignored.

### Q b04-3.4 [implications]
Why is querying a trusted expert (or documentation, or a well-trained model) often overwhelmingly superior to probe-and-observe exploration, in the framework's terms? Name at least three structural properties of query actions, and the mirror-image risk that the same channel creates.

### Q b04-3.5 [implications]
The framework says an agent whose gain does not reset after environmental structural change "continues trusting a stale model." Connect this to the framework's model-class-fitness machinery (the diagnostic for when a model class itself has become structurally inadequate, not just locally mismatched): what observable signature should trigger the reset, and why does the reset requirement couple the gain machinery to structural adaptation rather than being a standalone heuristic?

### Q b04-3.6 [implications]
Confirmation bias is usually described as an irrationality. Restate it in the framework's vocabulary as a *rational update with a miscalibrated parameter*, and explain why epistemic opacity makes the condition potentially persistent (why can't the agent always detect it from inside?).
