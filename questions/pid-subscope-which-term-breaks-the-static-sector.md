---
kind: question
closer: anyone
asked: 2026-10-30T23:27:49Z
asked-by: drain-wn-01-gold-opus-5.5
concerns: [segment:form-sector-condition, segment:deriv-sector-condition]
---

# Is a fixed-gain proportional (or PD) controller in sub-scope alpha, with only the integral state (or human-judgment delay) forcing PID into sub-scope beta? #form-sector-condition:74 and :96 place PID in beta as 'tuning-dependent; not cocoercive generically'. Gemini (AUDIT-WORKING-193847, recorded in #deriv-sector-condition Working Notes line 453) says a well-tuned PD is strongly monotone on the error space and the stateful I term is what breaks the memoryless static-sector assumption. That is plausible for P. For PD it holds only on the augmented state (e, de/dt), so it needs checking before the operator-family row is sharpened.
