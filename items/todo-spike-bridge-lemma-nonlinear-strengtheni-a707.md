---
kind: item
provenance: imported
source: TODO.md:469
section: TODO — Miscellaneous & details › 2026-05-12 (late) — Spike audit triage (99 spike files surveyed via 3 parallel agents)
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:der-directed-separation]
rechecked: 2026-10-30T21:14:07Z by Claude Opus 5.5 (item rechecker, t2-todo)
owner: G.2
restated: 'CL-1: land the dissipativity template (passivity-composition + pid-a2prime + bridge §7.2) as one coupled landing, after a regression check. Before it lands: der-gain-sector-bridge:76 already states alpha_PID as Derived with no derivation in canon and contradicts :108; the honest content is that any linear PID loop with an exponentially stable closed loop is in sub-scope alpha in a P-norm (converse Lyapunov + Cauchy-Schwarz), while the phase-margin formula for the constant is a heuristic until derived.'
---

# `spike-bridge-lemma-nonlinear-strengthening-2026-04-24` §7.2 passivity / dissipativity — Tier 2 math, ready to land. Target: `#dissipativity-template` appendix

Imported verbatim (relative links rebased) from `TODO.md` line 469, section *TODO — Miscellaneous & details › 2026-05-12 (late) — Spike audit triage (99 spike files surveyed via 3 parallel agents)*. Not yet re-checked against HEAD: `vsect recheck item:todo-spike-bridge-lemma-nonlinear-strengtheni-a707 --outcome holds|stale|landed|not-an-item --why …`.

- [ ] **`spike-bridge-lemma-nonlinear-strengthening-2026-04-24` §7.2 passivity / dissipativity** — Tier 2 math, ready to land. Target: `#dissipativity-template` appendix + Class 1/2/3 port-structure addition to `#der-directed-separation`. **`CL-1` (spike-routing 2026-05-17):** §7.1 is integrated (spike filed), but §7.2 is a *coupled* landing with `spike-passivity-composition` + `spike-pid-a2prime` — one `#dissipativity-template` integration-plan, **not** three independent half-segments. Heavy; tracked in `spikes/ROUTING.md` + PROPOSALS SP-22 STATUS.
