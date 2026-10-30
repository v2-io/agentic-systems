---
kind: item
owner: C.1
opened: 2026-10-30T23:24:28Z
opened-by: Claude Opus 5.5 (audits drain)
concerns: [segment:form-information-bottleneck]
closed: 2026-10-30 duplicate by Claude Opus 5.5 (audits drain) of item:influx-ib-beta-rho-and-exactness
---

# #form-information-bottleneck's exactness warrant has two halves that cannot both hold (checked at HEAD, Epistemic Status :38). It claims an exact application of Tishby-Pereira-Bialek 1999 with the Markov chain Y - X - T 'holding by construction'. The chain holds by construction only because phi is deterministic (sigma(M_t) within sigma(C_t)); but the cited theorem optimizes over stochastic encoders p(t|x), whose optimum is generically a kernel. For a stochastic encoder in a closed loop the chain fails: M_t carries randomness beyond C_t, future actions a_{t:inf} = pi(M_t, ...) depend on it, and Y inherits it. So either AAT restricts to deterministic encoders (then the displayed problem is the deterministic special case, not the theorem as cited; Strouse & Schwab 2017's deterministic IB is the matching citation) or it uses the kernel theorem under the pi_cont open-loop convention (then the body must connect the chain to that convention). Also: conditioning on the infinite endogenous a_{t:inf} wants directed information (Massey) under closed loop; the VFE-correspondence paragraph is untiered. Status: 'exact' fits the imported theorem, not the displayed equation as warranted; strengthen by stating the restriction and the convention, not by downgrading. Sources: audits/AUDIT-WORKING-731548/11-form-information-bottleneck.md §3 (Fable 5; ledger item xxiv); the deterministic-vs-kernel half is the segment's own WN gold at :81 (526815) and the two-encoder figure idea at :88. Legibility, same segment: 731548/11 and gold (829314, 613842) find the IT-MDP-lineage and VFE paragraphs are about 40% of the body as reviewer armour; they could move to #disc-compression-operations.
