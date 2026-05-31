# Reflection: scope-agency

**1. Predictions vs evidence.**
I predicted this segment would formalize the Pearl-level-2 contrast requirement mentioned in `scope-adaptive-system`. It does exactly this, defining $\mathcal{S}_\text{agency}$ by requiring $\lvert\mathcal{A}\rvert \geq 2$ and $\exists a \neq a'$ such that $P(o \mid do(a)) \neq P(o \mid do(a'))$. 

**2. Cross-segment consistency (FINDING REINFORCED).**
This segment reinforces the contradiction I found in `scope-adaptive-system`. It explicitly defines "Passive observers" and "Nominal agents" as being *inside* the adaptive scope but *outside* agency. But `def-agent-environment` defined an "Agent" as requiring action. If a "Passive observer" has no actions, it isn't an "Agent" under the first definition, so it can't be in the adaptive scope if the adaptive scope consists of "Agents." The terminology "Nominal agents" further confuses things by using the word "agent" for something explicitly excluded from "agency." The integration debt around the word "Agent" is clear.

**3. Math verification.**
The use of the $do()$ operator is standard Pearl causal inference. The condition $P(o \mid do(a)) \neq P(o \mid do(a'))$ is the correct formalization of an action having a measurable interventional consequence.

**4. What direction will the theory take next?**
The next segment is `post-causal-structure.md`, which is the final segment of Chapter 1. I expect it to postulate that the underlying environment $\Omega$ (or at least the agent's model of it) is governed by causal mechanisms, completing the bridge to Pearl's framework.

**5. What errors should I now watch for?**
The classic error in causal inference is conflating interventional distributions $P(y \mid do(x))$ with observational distributions $P(y \mid x)$. I must watch closely when the framework uses $do()$ vs simple conditioning. The segment notes that the feedback loop generates interventional data, but only if the agent is actually intervening.

**6. Predictions for next segments.**
`post-causal-structure` will assert that $\Omega$ can be modeled as a structural causal model (SCM) or similar construct.

**7. What would I change?**
I would resolve the terminology contradiction. A clean fix: 
- Rename `def-agent-environment` to `def-entity-environment`. An "Entity" observes and has state. 
- In `scope-agency`, define an "Agent" as an Entity that meets the agency scope conditions (action + contrast).

**8. What am I now curious about?**
The forward reference to the Pearl Causal Hierarchy (CHT) says AAT uses it as "machinery rather than referencing it as vocabulary". The OUTLINE mentioned this under the "constructive impossibility posture". I'm curious to see the actual proof where CHT is used as a hard floor that forces a specific architectural choice.

**9. What new knowledge does this enable?**
It mathematically distinguishes "doing things that matter" from "doing things that don't matter" (Nominal agents) and "not doing things" (Passive observers). 

**10. Should the audit process change?**
No.

**11. What changes in my outline for the final report?**
Update the "Phase 1 - Findings" node to include the "Nominal agents" terminology clash as part of the integration debt.

**12. How valuable does this segment feel to me?**
Very. It bridges AAT to Pearl's causal inference, which is a major, load-bearing move for the rest of the theory.

**13. What does the framework now potentially contribute to the field?**
It grounds the philosophical concept of "agency" in strict, observable Pearl-level-2 interventional contrast.
