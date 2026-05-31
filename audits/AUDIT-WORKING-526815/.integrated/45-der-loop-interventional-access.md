# 45 - der-loop-interventional-access

Source: `01-aat-core/src/der-loop-interventional-access.md`

## First-pass understanding

This segment carries the burden left open by the causal-hierarchy requirement. It argues that an agent in an action-perception loop produces intervention-character data: the agent executes an action, the world responds, and mismatch conditioned on that action tells the agent something about how the environment responded relative to the model. The segment is careful to distinguish this from cleanly identified `do` estimates; coverage, confounding, delay, and partial observability all stand between loop data and a valid estimate of `P(o | do(a), M_t)`.

The strongest version of the claim is "availability, not exploitation or identification." Agency scope supplies action contrasts in principle; model class and update rules determine whether the agent uses them; domain/admissibility conditions determine whether usable causal estimates are identifiable. The discussion is long and imports many later identifiability-floor and composite-layer connections, but the local core is the availability/identification split.

## Diagram attempt

The useful diagram is a gate diagram. Agency scope gives action contrast and physical intervention. That yields intervention-character experience. Then separate gates determine identification: coverage/positivity, sequential ignorability or adjustment, delay attribution, and observability. This diagram makes the exact part smaller and the regime-dependent part explicit.

## Findings and watches

- Candidate finding: `status: exact` overstates the formal expression unless the exact claim is narrowed to "agency scope gives access to possible action-generated data." The text often reads as though every loop pair `(a_t,o_{t+1})` contains interventional information, but agency scope only requires at least one action with causal effect. Specific actions can be no-ops, effects can be delayed beyond `t+1`, and exogenous observations can dominate the next observation.
- Candidate finding: theorem-grade conditions are displaced into Working Notes and a NeurIPS cross-reference: positivity, sequential ignorability, and known action mechanism. Those are precisely the assumptions needed to move from action-generated loop data to identified Level-2 estimates. If this segment is to remain exact, those conditions, or a deliberately weaker exact claim, should appear in the Formal Expression/Epistemic Status rather than only in Working Notes.
- Watch: the phrase "mismatch conditioned on `a_t` carries interventional information" is safer here than in the Pearl recapitulation because the segment adds caveats, but it still needs the low-CIY/no-effect case: the amount of information may be zero or practically unusable.
- Watch: the singular-trajectory grounding imports the earlier chronica/token issue. It helps avoid copy-averaging ambiguities, but it should not imply that replay/simulation is useless; it is just a different trajectory or model-based counterfactual, not the original token's intervention.

## Local verdict

This is the best version of the loop-as-Level-2 claim so far because it explicitly names the identification gap. The fix is mostly status and assumption placement: either weaken the exact claim to data-character availability, or promote the theorem-grade conditions into the formal body.
