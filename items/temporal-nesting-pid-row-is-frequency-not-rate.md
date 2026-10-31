---
kind: item
owner: C.1
opened: 2026-10-31T02:16:00Z
opened-by: drain-wn-01-gold-opus-5.5
concerns: [segment:der-temporal-nesting]
---

# #der-temporal-nesting:51 maps a PID controller's D, P and I terms onto fast, current and slow levels of the timescale ladder. A standard parallel PID runs all three on the same clock tick. The nesting is in the frequency content each term responds to, not in update rate, unlike a cascade loop whose inner loop ticks faster. Half a sentence keeps the analogy and stops control-theory readers from tripping (829314). Checked at HEAD 4175aae7. Source: gold Follow-up (WN line 77).
