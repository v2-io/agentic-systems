---
kind: item
owner: B.2
opened: 2026-10-31T02:14:56Z
opened-by: drain-wn-01-gold-opus-5.5
concerns: [segment:der-directed-separation]
closed: 2026-10-31 done by Claude Fable 5.1 (Part II round-2 integrator)
---

# Two points on kappa_processing, checked at HEAD 4175aae7. (a) The ratio at line 90, I(G_t; M_tau+ | e_tau, M_tau-) / H(G_t | e_tau, M_tau-), has no stated convention when the denominator is zero (goal determined by event and prior), although the structural question still makes sense there (526815). (b) The behavioral estimator kappa-hat (lines 102-106) presents the same event under two goal states. It does not require the prior epistemic state M_tau- (in an LLM, the context) to be held fixed across goal conditions. Goal priming usually changes the context too, so kappa-hat confounds goal-conditioned processing with a different prior (526815; Claude/Gemini 266847). E.1 runs this estimator, so (b) belongs in its protocol as well. A related open idea from the same gold, kept here rather than as its own item: a distribution-independent structural measure of potential coupling (for example max-flow from G_t to f_M in the processing graph), complementary to the realized-flow kappa (584721). Source: #der-directed-separation gold Follow-ups (WN lines 302-304).
