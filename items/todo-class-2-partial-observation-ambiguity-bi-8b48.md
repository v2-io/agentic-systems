---
kind: item
provenance: imported
source: TODO.md:161
section: TODO — Miscellaneous & details › Open theory items (MEDIUM)
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:deriv-observation-ambiguity-bias-bound]
rechecked: 2026-10-30T21:20:29Z by Claude Opus 5.5 (item rechecker, t1-todo)
owner: C.1
restated: 'Misframed as a new derivation. The body already states the Class 2 bound: the boxed Track 1 and Track 2 results carry kappa_processing x I(G;Omega|e,M) and are tagged Derived. But the step that introduces kappa (§2 Step 4, §3 Step 3) is an assertion, so the work is to derive it or retag it. A direct route exists from kappa''s own definition (normalized output information): E KL = I(G;M+|e,M-) = kappa H(G|e,M-), which gives a kappa-linear Fisher-Rao bound against H(G|.) for every class; whether the product with I(G;Omega|.) also holds is the real open question. Note #der-directed-separation:113 rests its one ''earned directional fact'' on this bound.'
---

# Class 2 (Partial) observation-ambiguity bias-bound (surfaced 2026-05-09 by GUC rename audit). `#deriv-observation-ambiguity-bias-bound` derives the bound for th

Imported verbatim (relative links rebased) from `TODO.md` line 161, section *TODO — Miscellaneous & details › Open theory items (MEDIUM)*. Not yet re-checked against HEAD: `vsect recheck item:todo-class-2-partial-observation-ambiguity-bi-8b48 --outcome holds|stale|landed|not-an-item --why …`.

- **Class 2 (Partial) observation-ambiguity bias-bound** (surfaced 2026-05-09 by GUC rename audit). `#deriv-observation-ambiguity-bias-bound` derives the bound for the Class 3 (Coupled) extreme at $\kappa_{\text{processing}} \to 1$. The analogous bound for Class 2 (Partial) agents at $\kappa_{\text{processing}} \in (0, 1)$ is open. Specializing either Track 1 (transport-inequality under LSI + Lipschitz-posterior) or Track 2 (Fisher-Rao under (PI) + Čencov + small-$I$) to the bounded-coupling regime is the natural first move. Whether the Class 2 case admits a clean closed-form bound or requires architectural specifics (per-stage modularity decomposition) is unknown. Detail flagged in segment Working Notes; this entry is the strategic-portfolio cross-reference.
