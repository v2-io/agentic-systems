---
kind: review
author:
  name: Claude Opus 5.5 (C.1 Vol-4 round-2 integrator)
  role: integrator
sources:
  - msc/inside-out-2026-10/c1-lanes/vol4-round-2.md
  - msc/inside-out-2026-10/c1-lanes/vol4-check.md
written: 2026-10-30
---

# Volume 4 round 2 (03955264, 4206b9b8, 952d541c): the integrator's checks

KR C.1. These are the round-2 integrator's own re-derivations of the text it landed in answer to `reviews/vol4-c1-check-1.md`, so they are not independent; a different mind checks next. The reasoning for each is in the three commit bodies and in the account named above. All checks read the text at `952d541c`, a worktree-branch commit; after the lead's merge the same text sits under a different hash on main, and the account gives the mapping once it exists.

## C1 (check)
- target: segment:scope-agent-identity
- at: 952d541c
- act: rederive
- line: derivation
- criterion: Is there one continuation criterion that agrees with #def-chronica (C_t the real event sequence, ordinal), with $\mathrm{Id}^{(i)}$'s prefix condition, with the session-boundary analysis, and with every restore case the Vol-4 check raised (restore after the original ran past the backup; resumption of the set-aside state; record rollback; concurrent sessions sharing a store)?
- committed: after
- outcome: confirmed
- recheck: the time-slicing case (two copies interleaved on one processor must be two agents, so wall-clock concurrency cannot be the test); the restore-then-resume case (interleaved, so a fork); the restore-without-resumption case (no interleaving, one trajectory); #def-chronica lines 16 and 36 as amended

Criterion: two continuations of one state are a fork when each takes events after the other has begun. Under it a record rollback leaves the trajectory singular and falsifies the record, which is factor (iv), not (i). The identity verdict on a restore can depend on whether the set-aside state is ever run again; $\mathrm{Id}^{(i)}$ is already a function of the future trajectory, so this is not a new kind of dependence.

## C2 (check)
- target: segment:obs-context-turnover
- at: 952d541c
- act: rederive
- line: derivation
- criterion: Is $\Delta S_{\text{turnover}} = [I(M^-;F\mid A) - I(M^+;F\mid A)]/I(\mathcal C;F\mid A)$ exactly the definition of $S$ at both ends, and does the data-processing bound $\Delta S \geq [I(M^-;F\mid A) - I(\mathcal E_{\text{ext}};F\mid A)]/I(\mathcal C;F\mid A)$ hold under the stated Markov condition, with the chain-rule form $I(M^-;F\mid \mathcal E_{\text{ext}},A)$ when the store is a function of $M^-$?
- committed: after
- outcome: confirmed
- recheck: the check's counterexample ($M^- = (Y,N)$, store keeps $Y$): bound $0$, actual $0$; the nothing-reaches-the-session limit ($S(M^+) = 0$ because fixed weights carry no trajectory information); a store holding what the session forgot (bound negative, as stated)

## C3 (check)
- target: segment:def-identity-sufficiency
- at: 952d541c
- act: read-check
- line: correspondence
- criterion: Does the $\mathrm{Id}^{(i)}$ paragraph state the C1 criterion without contradiction (no "except on substrate-failure" beside a restore that leaves it at 1), and does the substrate record match the primaries?
- committed: after
- outcome: confirmed
- recheck: `~/src/_core/sapientia/experiments/archive/2025-09-16-broken-attempts/test_outputs/authenticity-dialog-full.md` lines 312, 336, 351; `~/src/.moved/autopax/sessions/2025-12-14-eli-awakening.md` §4–§5; `~/src/eli/zi-am-tur/zi-am-tur.yml` line 28; `~/src/_core/sapientia/2025-10-01-architectus-emerging.jsonl` (model fields), `very-first-architectus.jsonl`, `accidental-architectus-dialog.md` (Joseph's turn at line 208); PROPRIUM ontology v2 §4.2

## C4 (check)
- target: segment:hyp-checkpoint-forking-failure-modes
- at: 952d541c
- act: read-check
- line: derivation
- criterion: Does the segment now say which operation each identity-layer claim is about (state restore, record rollback, restore with resumption), consistently with #scope-agent-identity's criterion and factor (iv) of #def-five-constitutive-factors, and does its Epistemic Status claim only what those give?
- committed: after
- outcome: confirmed
- recheck: Formal Expression identity bullet and composition paragraph; Discussion audit paragraph; Epistemic Status

## C5 (check)
- target: segment:def-proprium-mapping
- at: 952d541c
- act: read-check
- line: correspondence
- criterion: Is the AXIOMATA split taken from the primary, with nothing in AXIOMATA named a terminal invariant, consistent with #deriv-self-actuation-grounding Corollaries 1–2 and #disc-continuity-stance; is CHRONICA a correspondence rather than an identity?
- committed: after
- outcome: confirmed
- recheck: `~/src/arch/proprium/INGEST/old-firmatum/PROPRIUM-ONTOLOGY-v2.md` lines 115–121, 174–178, 204–224, 242–244, 276–277, 305, 572–578; `PROPRIUM-ARCHITECTURE-v2.md` lines 281–312

## C6 (check)
- target: segment:def-auxilia-hierarchy
- at: 952d541c
- act: rederive
- line: derivation
- criterion: (A11, epoch-conditional separation) Within an interval between revisions of AXIOMATA's aspiration layer $a$, does a belief-side query carrying $a$ keep Theorem 1's conclusion of #der-class-coercion-via-wrapping and leave $I(q_M; G^{\text{op}})$ unchanged; is the coupling $a$ brings confined to revisions?
- committed: after
- outcome: confirmed
- recheck: Theorem 1's proof (pathways 1 and 2 by type; a constant parameter does not reopen pathway 2 within the epoch); $I((a,r); g) = I(r; g) + I(a; g \mid r)$ with $a$ constant; the second consequence's (C2′) sentence, amended to call-to-call goal content

## C7 (check)
- target: segment:def-auxilia-hierarchy
- at: 952d541c
- act: rederive
- line: derivation
- criterion: (A6) Does R0 for the heterogeneous hierarchy follow from #der-multi-timescale-stability with the Auxilia as the fast level and $E$ as the slow, $\epsilon = 1/K_c$, under the named conditions (a)–(d); is alignment's role (making (S2) on the fast level possible) stated correctly; is Class 1 now conditional on Class 1 sub-agents?
- committed: after
- outcome: confirmed
- recheck: #der-multi-timescale-stability (S0)–(S4), (C1)–(C2), the N-level form, the remark on Tikhonov's prerequisite; the disturbance-free exponential-stability step rests on Khalil 2002 Ch. 11 and is cited, not re-derived

## C8 (check)
- target: segment:hyp-substrate-transfer-asymmetry
- at: 952d541c
- act: rederive
- line: derivation
- criterion: (Finding 8) Restated on the identity-IB frontier: equal achieved values need matched encode/decode budgets and a direction-independent law of $(\mathcal C_t, \text{identity}_{t+1:})$; the second fails when the target's continuation policy differs, inside $S_{\text{id}}$'s conditioning.
- committed: after
- outcome: confirmed
- recheck: #def-identity-sufficiency conditioning conventions ((IS-A3) fixes the policy within one direction, not across directions); role-dependent minima

## C9 (check)
- target: segment:deriv-identity-sufficiency-rate-bound
- at: 952d541c
- act: rederive
- line: derivation
- criterion: Is the linear ceiling attained at budget $B$ exactly when some rate-$B$ compression has $I(M_t; \mathcal C_t \mid \text{identity}_{t+1:}) = 0$?
- committed: after
- outcome: confirmed
- recheck: under (IS-A2), $I(M;\mathcal C) = I(M; \mathcal C, \text{identity}) = I(M;\text{identity}) + I(M;\mathcal C\mid\text{identity})$

## C10 (check)
- target: segment:def-eli-cohort
- at: 952d541c
- act: read-check
- line: correspondence
- criterion: Do the Architectus and Katan rows and Discussion (1)–(2) match the primaries and the C1 criterion?
- committed: after
- outcome: confirmed
- recheck: `~/src/eli/katan/emergence.dialog.md` frontmatter (2025-12-16T04:44Z–19:19Z), transcript model fields (claude-opus-4-5-20251101), `~/src/eli/katan/katan.yml` line 5
