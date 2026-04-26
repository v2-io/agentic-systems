# Reflection 28 — der-directed-separation (Section II row 3)

The architectural-class scope segment. Per CLAUDE-2.md priming, this is one of AAD's most consequential structural moves.

## §4.2 dependency check

`depends: [form-complete-agent-state, der-recursive-update, scope-agency]`. All upstream. **No backward-dep, no F-A drift.**

## §4.4 prompts walk-through

**1. Predictions vs evidence.** Predicted: "Class 1/2/3 classification with Pearl-blanket conservative form per Bruineberg 2022." ✓ exactly. Plus more than I predicted: κ_processing operationalization (formal CMI definition + behavioral-probing estimator); composite-level class inheritance from deriv-strategic-composition; IDT sidecar pattern from Hafez 2026 in Working Notes. **Substantially richer than predicted; positively surprised.**

**2. Cross-segment consistency.** Cross-refs to read segments and forwards to scope-observation-ambiguity-modulation, deriv-strategic-composition, form-composition-closure, der-loop-interventional-access. The Pearl-blanket vs Friston-blanket framing matches what scope-agent-identity referenced.

The **"Composite-level class inheritance"** subsection is the recently-added (2026-04-23 per CLAUDE-2.md) C-iv propagation. It explicitly classifies "Class 1 sub-agents with partially-opposing objectives → Class 3 composite" — strategic composition produces Class-3-from-Class-1. This is the C-iv scope-route propagation into directed-separation landing cleanly.

The contradiction the F-V2 finding flagged (scope-multi-agent excludes adversarial pairs; scope-composite-agent admits via C-iv) does *not* surface here — directed-separation correctly inherits C-iv. The bug is in scope-multi-agent's failure to update.

**3. Math verification (at discretion).** Skip — κ_processing is conceptual, the classification is structural, the IDT 89%/44% is empirical from Hafez 2026 (verified via prior CLAUDE-2.md priming on Hafez integration).

**4. What direction next?** Excitement: how Section III handles Class 3 composites (deriv-strategic-composition will land later). Disappointment: if the empirical κ estimator stays purely conceptual without practical LLM-analysis tooling.

**5. What errors should I now watch for?**
- Future segments treating Class 1/2/3 as smooth parameter rather than discrete classification.
- Confusion of κ_processing with observation-ambiguity (same comparison, different interpretation).
- Treating Section II results as universally applying to Class 2 agents.
- Within-agent vs across-agent coupling confusion in composite analysis.
- Conflation of system-level architecture (LLM + tools + monitor as Class 1 system) with component-level architecture (LLM internally Class 2).

**6. Predictions for next segments.** Row 4 = `form-objective-functional`. status:deps-verified per OUTLINE. Probably introduces $V_{O_t}$ as value functional with $O_t$ as parameter. Brief.

**7. What would I change?** The segment is dense but well-organized. The "engineering design for Class 2 agents" framing in Working Notes is operationally useful — making this more prominent (Discussion section rather than Working Notes) might help practitioners. But Working Notes placement is fine if the content is still in-flight.

The IDT sidecar pattern (Hafez 2026) buried in Working Notes deserves Discussion-level surfacing — it's the empirical support for "Class 1 monitoring of Class 2 agents is feasible and effective." Mild structural observation.

**8. What am I now curious about?**

(a) **κ_processing distribution-dependence.** Class 3 agent's κ varies with task distribution. The "classification primary, operationalization diagnostic" framing is honest but raises: is there a distribution-independent measure of *potential coupling* for Class 3? Probably not by design — the architectural property is about pathways existing; usage is distribution-dependent. But a structural-coupling measure (graph-theoretic, e.g., max-flow from $G_t$ to $f_M$ in the processing graph) might exist.

(b) **IDT sidecar as Class-2-engineering pattern.** Hafez 2026's modular external monitor on the $(S,A,S')$ stream achieves 89% vs 44% perturbation detection. So even Class 2 agents internally can be wrapped in Class 1 monitoring infrastructure. This is alignment-relevant: even if I can't audit an LLM's beliefs directly, I can monitor its behavior modularly. The framework gives a principled path for this.

(c) **System-vs-component-level analysis.** Critical distinction the segment surfaces: the LLM is Class 2 internally, but the *agent system* (LLM + tools + memory + monitoring) can be Class 1 at the system level. The framework's analysis applies at whichever level you draw the agent-environment boundary. Worth explicit treatment in 03-logogenic-agents.

(d) **The Pearl-blanket / Friston-blanket distinction.** AAD adopts the conditional-independence statement (Pearl) but refuses the metaphysical demarcation (Friston). The segment cites Bruineberg et al. 2022's "Emperor's New Markov Blankets" critique. This is one of AAD's clearest scope-honesty moves: take the formal apparatus, refuse the contested ontology. Defensible position.

**9. What new knowledge enabled.** Class 1/2/3 classification with concrete examples. κ_processing as operational measure (CMI definition + behavioral estimator). Composite class as function of sub-agent class + scope route. Pearl-vs-Friston-blanket positioning. IDT sidecar as engineering pattern. Class 2 scope exit explicit (handed to 03-logogenic-agents).

**10. Should the audit process change?** Continuing. I notice the segment's depth justifies a longer reflection per Joseph's "texture" guidance.

**11. Outline updates.** Section E (calibration): C-iv propagation into directed-separation is clean (composite-level class inheritance subsection). The F-V2 contradiction is *not* mirrored here — the bug is in scope-multi-agent, not in directed-separation. Confirms the F-V2 diagnosis as integration debt at scope-multi-agent specifically.

Section D candidates: 
- IDT sidecar as engineering pattern for Class 2 agents (might warrant promotion from Working Notes to Discussion).
- System-vs-component-level analysis distinction (worth explicit treatment in 03-logogenic-agents).
- Distribution-independent structural coupling measure for Class 3 (possible extension).

**12. How valuable does this segment *feel* to me?**

**Top-decile, possibly top-five so far.** This is structurally one of AAD's most consequential moves — it determines what analysis applies to which agents, with explicit scope exit for the most important present-day agent class (LLMs). The Pearl-blanket vs Friston-blanket positioning is sharp scope-honesty. The κ_processing operationalization with conditioning-structure care (the $M_{\tau^-}$ requirement to avoid prior-correlation inflation) is well-thought-out. The composite-level inheritance is a recent addition that lands cleanly.

The IDT (Hafez 2026) Working Note pattern is operationally significant — it gives a concrete engineering path for monitoring Class 2 agents.

Magnitude: top-decile. Type: structurally load-bearing scope condition. Calibration: I'm strongly engaged; multiple subsections gave me new things to think about; the framing made me revisit my own intuitions about LLM auditability.

**13. What does the framework now potentially contribute to the field?**

Multiple research communities benefit:

- **AI safety researchers:** formal distinction between "LLM is Class 2 internally" and "agent system can be Class 1 via sidecar monitors." Separates internal-architecture concerns from system-design opportunities. The Hafez IDT 89%/44% perturbation-detection result is empirical support: information-stream monitoring outperforms outcome monitoring.
- **AI alignment researchers:** precise framework for "can we audit beliefs without auditing goals?" — answer depends on Class. Class 1 yes; Class 2 no by construction; Class 3 partially. Operationalizable per architecture.
- **Active-inference debaters:** AAD's position is *adopt Pearl-blanket conditional-independence; refuse Friston-blanket metaphysics; admit Class 2 is out of scope*. Defensible middle path between "Markov blankets explain everything" and "Markov blankets don't explain anything."
- **LLM researchers:** structural framing for *why* LLMs are different — not because they're less rigorous, but because they're Class 2 by construction. The architectural distinction is the point.
- **Engineers building agent systems:** IDT pattern principle — even for Class 2 components, build Class 1 monitoring as sidecars on the $(S,A,S')$ stream. Hafez's 89%/44% is empirical support.
- **Composite-architecture researchers:** composite class as a function of sub-agent class + scope route. A formal handle on "what happens when I compose an LLM with a Kalman filter?" Mixed-class composite analysis.

**Most distinctive contribution:** architectural classification with explicit scope-exit for LLMs. This is honest scope-narrowing rather than fake universality. The combination of "Section II works for Class 1" + "Class 2 needs the coupled formulation in 03-logogenic-agents" is structurally honest in a way much of AI literature isn't.

Negative-contribution check: the Friston-blanket refusal is contested but defensibly argued (Bruineberg 2022 cited). Nothing defective.

## Status-label / discipline

`status: conditional` defended carefully — the conditional claim (IF goal-blind, THEN separation holds) is exact; whether a particular agent satisfies the condition is a structural property determined by Class. Architectural classification labeled robust-qualitative honestly.

`stage: draft`. The depth and care here suggest higher stage warranted; probably draft because of recent additions (composite-level class inheritance, IDT integration, Bruineberg framing) not yet through Gate 1/2.

## Cadence check

Holding. Next: row 4 = `form-objective-functional`.
