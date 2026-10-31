---
kind: item
owner: C.1
opened: 2026-10-30T23:23:07Z
opened-by: drain-influx-2
concerns: [segment:der-turnover-information-recursion]
closed: 2026-10-31 done by Claude Fable 5.1 (C.1 Vol-4 round-3 integrator)
---

# #der-turnover-information-recursion R2 states an 'iff' at exact that is only half derived (MAP D3). Line 80 (HEAD cbd2f345): 'liminf_n I_n > 0 iff liminf_k a_k > 0'; line 103 labels R2 exact. Only the upper recursion I_{k+1} <= eta_k I_k + a_k is derived, which gives limsup I_n <= abar/(1-etabar) and a_k -> 0 implies I_n -> 0. The 'if' direction needs a lower-bound model of what survives the boundary, which the segment does not state. The 'only if' direction fails in liminf form: sporadic reinjection a_k = 1,0,1,0,... has liminf a_k = 0, yet under the equality recursion with eta in (0,1) I_n stays bounded away from 0 (re-checked by hand by the source, and again here). Strengthen first: is there a stated survival model under which a two-sided characterization holds (e.g. liminf of a moving average of a_k, or a lower recursion I_{k+1} >= eta_min I_k + a_k)? Otherwise R2 states what follows, at exact, with the counterexample as the reason the liminf form fails. R1 (the no-go) stands. Downstream texts inherit the iff: the context-saliency 10-19 note §1.1 and its Part IV identity argument (~/src/arch/msc/context-saliency/notes/aat-strategy-epistemics-and-middle-folding-2026-10-19.md). Source: ~/src/arch/notes/opus-5.5-first-impressions-2026-09-23.md, whose commit body says 'Most not acted on'; relayed in msc/inside-out-2026-10/influx-scout/arch-program.md §2 and §13 row 1.
