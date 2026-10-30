---
kind: item
owner: G.2
opened: 2026-10-30T23:24:18Z
opened-by: Claude Opus 5.5 (spike drain fork D)
concerns: [segment:der-class-coercion-via-wrapping, segment:der-tempo-composition]
---

# OTP supervision as a worked instance of #der-class-coercion-via-wrapping (restart strategies, the stash partition, restart intensity, let-it-crash) and the ETS resolution (the W axis is type-of-bound, shared regions are wrapped components) are in no segment; two of the spike's claims are stated above their warrant and should land lower: the "theorem-grade" wrapper persistence inequality and the "must" of crash-early.

Checked at cbd2f345: no segment mentions supervision trees, restart strategies, restart intensity, the stash pattern or ETS (grep of all four `src/`). #scope-continuous-operation :42 already carries the time-optimality half of let-it-crash (recover fast when $T_\text{recovery} \ll T_\text{defensive}$); what is missing is the wrapping reading.

Sources: `spikes/tst-ideas-cycle-2026-05-21/spike-class-coercion-via-supervision.md` §1–§4, §7; `spike-ets-as-third-w-regime.md` §5; `spike-substrate-modifying-actions.md` §5 (macro hygiene as the same pattern at the language layer, an analogy by its own §7(c)); mining substrate `spikes/tst-mining-2026-05-21/04-elixir-composite-mining.md` A1–A5, A10, A11, `01-release-it-mining.md` A3, A5, `03-pragmatic-mining.md` #10, #11, #14; synthesis `TST-IDEAS.md` §9 (which calls the inequality "the headline result" and "theorem-grade").

What looks landable, at discussion grade, cited to Armstrong 2003 and Gray & Tate 2019 under their own names: restart strategies (`:one_for_one` / `:rest_for_one` / `:one_for_all`) as three widths of one structural commitment, with the composite's leakage per restart bounded by the sum over the restart set; the stash pattern as a second partition axis (essential vs ephemeral) orthogonal to belief vs goal; ETS and other shared regions as additional wrapped components whose class follows from their API, so no new regime is needed (the W axis is structural-by-type-signature vs behavioral-by-compliance); BEAM as the case where wrapper instantiation cost goes to zero and the remaining cost is coordination, for #der-tempo-composition.

Where the spike outruns its warrant, so the integrator re-derives rather than transcribes:

- **The wrapper persistence inequality** $1/T_\text{restart} \gt \rho_\text{child} \lVert\delta_\text{failure}\rVert / \lVert\delta_\text{critical}^\text{wrapper}\rVert$ (§3, "theorem-grade") is a substitution into #result-persistence-condition: tempo is *defined* as $1/T_\text{restart}$ and disturbance as failure rate times damage, without showing that reset-to-$S_0$ dynamics satisfy the sector premise the persistence condition needs, or what "mismatch" a reset corrects. As it stands it is a heuristic dimensional analogy with `max_restarts / max_seconds` as a plausible estimator, not a derived result. Strengthen first: write the reset dynamics as a renewal process and ask what is actually bounded.
- **Crash-early as a necessity** (§7: recovery code inside the component "must be goal-conditioned"). Recovery need not consult the goal: restoring an invariant or resetting local state inside the component is goal-blind. What the argument supports is the narrower claim that *goal-aware* recovery inside a wrapped component breaks (C3), so let-it-crash is a sufficient way to keep recovery goal-blind, not the only one. The trust-boundary paragraph (validate-and-reject at the input layer) is sound as stated.

Related open item: item:todo-detailed-tempo-accounting-for-canonical-e0c9 (tempo accounting for ReAct, Reflexion and PROPRIUM wrappers); the BEAM cost decomposition would feed it.
