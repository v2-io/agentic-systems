# 31 — result-structural-adaptation-necessity

Dependencies checked: `def-model-sufficiency`, `def-model-class-fitness`, `result-mismatch-decomposition`, and `emp-update-gain` already read.

## Reflection

This segment is more careful than I predicted.
It explicitly marks the alignment assumption needed to move from lost predictive information to one-step mean mismatch, and it offers proper-scoring regret as the more general fallback.
`status: conditional` is appropriate.

Substantive core:
If $\mathcal F(\mathcal M)<1-\varepsilon$, then no parameter choice inside $\mathcal M$ can reach full sufficiency.
That is almost definitional, but useful.
The "necessity" is conditional on the objective of reducing the relevant predictive/regret floor; an agent could also lower ambitions, alter objectives, accept failure, or change observation channels.
The segment's wording "requires changing $\mathcal M$" is acceptable in context because the target is reducing mismatch below the floor.

Minor mathematical precision:
Step 1 uses $M^\ast=\arg\sup_{M\in\mathcal M}S(M)$.
The supremum may not be attained.
Use approximate optimizer or assume compactness/attainment.
This is not a high-severity finding but is easy to fix.

Inherited issue:
Because `def-model-sufficiency` lacks the denominator-positive condition, this result also needs the no-predictive-information edge case handled.
If the denominator is zero, $\mathcal F$ and the structural inadequacy condition are not well-defined as currently written.

Format/provenance:
The Miller discussion cites `spikes/spike-miller-act-bridge.md` outside Working Notes.
This repeats the spike-reference convention issue.

What this enables:
Separates "update faster / tune gain" from "change representation."
The bidirectional adaptation discussion (expansion and compression) is valuable and prevents "always add complexity" as the default interpretation.

Prediction for next segment:
`der-temporal-nesting` should formalize timescale separation / singular perturbation.
I will watch whether it depends on appendix `sketch-multi-timescale-stability` and whether it claims exactness or sketch status.

Running report update:
- No major new finding; add minor precision item for arg-sup attainment if final space permits.
