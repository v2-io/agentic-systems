---
kind: item
provenance: imported
source: TODO.md:206
section: TODO — Miscellaneous & details › Queued spike work
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:form-consolidation-dynamics]
rechecked: 2026-10-30T21:18:39Z by Claude Opus 5.5 (item rechecker, t1-todo)
owner: C.1
restated: 'Open, and the label overclaims meanwhile. The stability upper bound (1-lambda) < phi(nu_consol, budget) is stated with phi undefined, yet the derivation table (line 94) and the body (line 76) call the stability-plasticity window''s ''existence'' Derived. A window exists only if rho_Sigma/R_Sigma < phi, which is what nobody has derived. What follows today is only: if a consolidation-limited upper bound exists, the admissible set of lambda is an interval, possibly empty. Strengthen first: derive phi for one concrete consolidation mechanism (a replay buffer of size B with offline budget B_offline, for instance); only if that fails, relabel the window as conditional on the unnamed phi. Also, the Working Note at line 162 calls phi ''the minimum forgetting rate'' that leaves enough signal; as an upper bound on (1-lambda) it is the maximum.'
---

# Stability-upper-bound for `#form-consolidation-dynamics` — closes the asymmetry left by Spike F's lower-bound-only result.

Imported verbatim (relative links rebased) from `TODO.md` line 206, section *TODO — Miscellaneous & details › Queued spike work*. Not yet re-checked against HEAD: `vsect recheck item:todo-stability-upper-bound-for-form-consolida-be13 --outcome holds|stale|landed|not-an-item --why …`.

- Stability-upper-bound for `#form-consolidation-dynamics` — closes the asymmetry left by Spike F's lower-bound-only result.
