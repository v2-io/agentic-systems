---
kind: item
owner: C.1
opened: 2026-10-30T23:27:14Z
opened-by: drain-wn-01-gold-opus-5.5
concerns: [segment:obs-gated-tempo-advantage]
---

# #obs-gated-tempo-advantage uses 'tempo' for event rate, re-read at HEAD 86489b0b. Lines 14 and 42 say a faster agent with noisy observations gets nearly zero advantage ('faster tempo with noisy observations ... gives nearly zero advantage'). By #def-adaptive-tempo, T = nu * eta*, and high observation noise drives eta* toward 0, so the sentence is either a tautology (zero tempo gives zero advantage) or uses 'tempo' to mean the event rate nu, which is what the simulation varies. The sharper and correct thesis is that the advantage of a higher event rate is gated by observation quality: you cannot recover lost T by cycling a noisy sensor faster. This is the theory's departure from naive OODA, so the wording matters. It is a register fix, not a math error. Source: the segment's Working Notes Off-ramp (line 82), Gemini AUDIT-WORKING-193847 poke. A different defect on line 16 is item:t1-gated-tempo-one-sided-noise-prescription.
