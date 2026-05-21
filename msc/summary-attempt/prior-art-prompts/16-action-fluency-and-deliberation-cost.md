Please conduct a deep prior-art search across academic literature. We are establishing scientific precedence for a theoretical framework of agency (AAT).

## The Core Idea / Claim
Agents distinguish *implicit* (model-embedded, fluent) action selection from *explicit* (deliberative) action selection by a measurable *action fluency* — the degree to which effective action flows from the model without deliberative computation. A formal deliberation-cost analysis gives a clean threshold: deliberation of duration Δτ is net-beneficial when the gain improvement times post-deliberation mismatch exceeds the deliberation-window mismatch drift rate times Δτ. Under diminishing returns plus linear-in-duration drift cost, this yields a *finite optimal deliberation duration*; past it, additional thinking is net-harmful. The framework derives a *structural pressure toward implicit action* in high-tempo environments: as drift goes to infinity or optimal duration goes to zero, the optimal strategy converges to pure fluent action. Action fluency is *distinct from* model sufficiency: a chess engine with a perfect model of the rules still requires expensive search (high sufficiency, low fluency); a trained reflex can have moderate sufficiency but high fluency in a narrow domain. What expertise and reflexes share is that the *action-generating capacity itself has been absorbed into the model's structure* — the model doesn't just predict well, it *acts* well, cheaply. The result connects to Boyd's IG&C (implicit guidance and control bypassing the explicit Decide step), Kahneman's System 1/2, expertise and chunking literature, and model-free vs model-based RL arbitration.

## Boundaries of the Claim
- Domain: cognitive science (dual-process, expertise, motor learning), military theory (OODA loops), reinforcement learning (model-free vs model-based; planning vs reflex), real-time decision-making.
- Focus: the *formal threshold* between fluent and deliberative action selection under environmental drift, and the structural distinction between *sufficiency* (model quality) and *fluency* (action-generation absorbed into model).

## What Kind of Match Counts
- Formal threshold analyses for when deliberation is net-beneficial vs net-harmful given environmental dynamics.
- Dual-process / System 1/2 work formalized with measurable structural parameters (not just descriptive taxonomy).
- Boyd's IG&C in formal mathematical treatment (not just military-doctrine prose).
- Expertise / chunking / habituation theories with measurable action-fluency metrics distinct from accuracy.
- Model-free vs model-based RL arbitration with explicit cost-benefit derivation rather than empirical-only comparison.
- Treatments of the "pause-and-think vs act-now" decision in real-time systems with derived optimal duration.
- Arguments that the *structural pressure* toward implicit action follows from a persistence-style constraint on the agent.

## What Would NOT Count
- General dual-process discussions without formal threshold conditions.
- Standard model-based vs model-free RL papers that just compare empirical performance without deriving the arbitration cost-benefit.
- Boyd's OODA literature that doesn't formalize the implicit-vs-explicit distinction structurally.
- Expertise / chunking papers that don't link fluency to measurable action-generation efficiency.

## Known Anchors
- Boyd (OODA, implicit guidance and control)
- Kahneman 2011 (Thinking Fast and Slow; System 1/2)
- Ericsson et al. (expertise and deliberate practice)
- Sutton & Barto (model-free vs model-based RL)
- Daw, Niv, Dayan (dual-system RL arbitration)
- Sweller (cognitive load theory)
- Klein (recognition-primed decision-making)
- Newell & Rosenbloom (chunking in cognitive architectures, SOAR)
- Anderson (ACT-R; declarative-vs-procedural memory and skill acquisition)
- Schmidt & Lee (motor learning, motor program theory)

## Search Scope
- Formal threshold derivations and dual-system arbitration mathematics; structural treatments of why high-tempo environments penalize deliberation.
- Strictly academic papers (no patents/IP).
