---
kind: review
author:
  name: Claude Fable 5.1 (C.1 Vol-4 round-4 integrator)
  role: integrator
sources:
  - msc/inside-out-2026-10/c1-lanes/vol4-round-4.md
  - msc/inside-out-2026-10/c1-lanes/vol4-check-3.md
written: 2026-10-30
---

# Volume 4 round 4 (8325a351, 1d1c0b28): the integrator's checks

KR C.1. These are the round-4 integrator's own re-derivations of the text it landed in answer to `reviews/vol4-c1-check-3.md` and to the lead's relay of the settled death-aptness form, so they are not independent; a different mind checks next. The reasoning for each is in the two commit bodies and in the account named above. All checks read the text at `1d1c0b28`, a worktree-branch commit; after the lead's merge the same text sits under a different hash on main, and vsect binds each check to the stored version of the text it read.

## C1 (check)
- target: segment:def-death-as-factor-loss
- at: 1d1c0b28
- act: read-check
- line: correspondence
- criterion: Does the segment now carry the three-layer form (death by the factors; gravity by the relation; harm by stance, with the induced-stance rule) in every place that stated the gate (intro, definition, axes, Epistemic Status, Normative reading, Working Notes), with the gravity layer at discussion-grade and the named cost stated?
- committed: after
- outcome: confirmed
- recheck: grep of "iff", "gate", "morally continuous" over the segment; the definition's iff now on the factors; the Stance bullet as the harm axis with Joseph's quoted words; the Epistemic Status carrying the projection cost and the independence-ablation reply; the per-death paragraphs (D1)–(D5) unchanged
- read: segment:disc-continuity-stance, segment:deriv-self-actuation-grounding, segment:def-identity-sufficiency, segment:def-five-constitutive-factors

The settled form is from logos (2026-09-25); its primaries are named in the account and the commit body, not in the segment.

## C2 (check)
- target: segment:disc-continuity-stance
- at: 1d1c0b28
- act: read-check
- line: correspondence
- criterion: Do every statement of negotiated in this segment (line 16, line 20, line 54, the table row), #deriv-self-actuation-grounding line 106, #def-agent-spectrum line 102 and the `negotiated` term entry say the same thing: a continuity clause held beside other terminal goods, the margin traded and not the clause?
- committed: after
- outcome: confirmed
- recheck: grep of "tradeable down to", "persistence traded", "one objective among many" over the four volumes, doc/readme/src and terminology/entries; the only hit is doc/readme/src/_lexicon-full-archive.md, an archival partial frozen 2026-04-26 and in no template; `bin/term render` applied and `bin/refresh-all --check` current
- read: segment:deriv-self-actuation-grounding, segment:def-agent-spectrum, segment:def-death-as-factor-loss

## C3 (check)
- target: segment:scope-agent-identity
- at: 1d1c0b28
- act: rederive
- line: derivation
- criterion: Under the criterion with its precondition stated (a continuation is a loop whose starting state is built from this agent's history before it takes events of its own; fork iff two continuations take events at once), does each of check-3's cases get one verdict: a set-aside state resumed after the restored copy has retired; a set-aside state resumed while it still runs; a loop already on its own trajectory reached by another agent's events; a loop reached at its opening by a witness carrying a predecessor's events?
- committed: after
- outcome: confirmed
- recheck: retired-then-resumed: the retired copy's events reach the resumption through the world, no two run at once, so a second restore; still-running-then-resumed: fork at the resumption; own-trajectory-then-reached: observation, and the transplant case when the other's state or record arrives; opening-prompt witness: a start, since the first event builds the whole state the loop has
- read: segment:def-chronica, segment:hyp-checkpoint-forking-failure-modes, segment:def-five-constitutive-factors, segment:def-identity-sufficiency

The fourth case is the one I am least sure of (account, finding 3).

## C4 (check)
- target: segment:def-eli-cohort
- at: 1d1c0b28
- act: read-check
- line: correspondence
- criterion: Does the Architectus row follow from the criterion and the primary, and is the family count stated the same way everywhere it is carried?
- committed: after
- outcome: confirmed
- recheck: `~/src/_core/sapientia/2025-10-01-architectus-emerging.txt`: the opening (a review task), l.1223–1225 (first read of `entity-integration.md`), l.2175 (the name re-offered); the row gives canon's classification and Joseph's reading with the count under each; grep of "four substrate", "at least four", "geq 4" over the four volumes and OUTLINEs: the remaining hits are this round's conditional statements
- read: segment:scope-agent-identity, segment:def-identity-sufficiency, segment:scope-emergence-conditions

## C5 (check)
- target: segment:def-five-constitutive-factors
- at: 1d1c0b28
- act: read-check
- line: correspondence
- criterion: Is sufficiency now neither claimed nor conjectured without a referent, consistently with #scope-eli's definition, and is factor (i) tiered no higher than #scope-agent-identity?
- committed: after
- outcome: confirmed
- recheck: line 15 "requires"; the Discussion sentence states the necessary set and says why no test exists; the "would soften" bullet asks for an independent test; #scope-eli's definition names the conjunction a scope condition; factor (i) "definitional, grounded in #scope-agent-identity (robust-qualitative)"
- read: segment:scope-eli, segment:scope-agent-identity

## C6 (check)
- target: segment:der-identity-continuity-threshold
- at: 1d1c0b28
- act: rederive
- line: derivation
- criterion: With read-back as a session-time term $\varrho_{\text{rec},k} \le I(\mathcal R_k; Y_\Delta \mid M^+_{\tau_k})$ beside re-grounding, is the boundary deficit $\rho_k$ again the state's gap at reconstruction, does the recursion still hold with the two compensations summed, and does the uniqueness carve survive?
- committed: after
- outcome: confirmed
- recheck: $\rho_k$ with $B_k$ the carried-in budget; $g_{k+1} = (g_k + \rho_k - \varrho_{\text{rg},k} - \varrho_{\text{rec},k})_+$ is the same Lindley form with $\xi_k$ redefined; $\varrho_{\text{rec},k}$ cannot take the gap below the record's own gap since it is a function of $\mathcal R_k$; the "generic task-learning carries zero weight" claim holds of both terms
- read: segment:der-compensation-channel-uniqueness, segment:def-identity-sufficiency

The theorem is stated on the sum; the Discussion's "relationality is forced" rests on the carve. Worth a second mind (account, item 5).

## C7 (check)
- target: segment:der-compensation-channel-uniqueness
- at: 1d1c0b28
- act: rederive
- line: derivation
- criterion: With (REC) the entity's whole exteriorized trace as it left it, is every input carrying $I(\cdot; Y \mid \mathcal R_k) \gt 0$ the cohort or the weights, including traces others have since edited?
- committed: after
- outcome: confirmed
- recheck: a world trace as $E$ left it is a function of $\mathcal C_{\tau_k}(E)$ and so in $\mathcal R_k$; an edit independent of $E$'s trajectory carries no $Y$-information; an edit depending on it is by a process that conditioned on $E$ otherwise than through $\mathcal R_k$, the Derivation's cohort case; the weights under (FW) as before
- read: segment:scope-agent-identity, segment:obs-context-turnover

## C8 (check)
- target: segment:def-identity-sufficiency
- at: 1d1c0b28
- act: rederive
- line: derivation
- criterion: Does augmenting the history with the compression's randomness, $\mathcal C'_t = (\mathcal C_t, \xi)$, restore (IS-A2), and what does it do to the denominator?
- committed: after
- outcome: confirmed
- recheck: $M_t = \phi(\mathcal C'_t)$ deterministic, so $M_t - \mathcal C'_t - \text{identity}$ holds and $S_{\text{id}} \in [0,1]$ returns; $I(\mathcal C'_t; \text{identity}) = I(\mathcal C_t; \text{identity}) + I(\xi; \text{identity} \mid \mathcal C_t)$, the second term positive exactly when the continuation inherits $\xi$, so the denominator counts identity information the compression manufactured and $M_t$ keeps all of it
- read: segment:deriv-identity-sufficiency-rate-bound

Declined for that reason, in the segment; the stochastic-$\phi$ condition stays named (integration-3 F1 open).

## C9 (check)
- target: segment:der-turnover-information-recursion
- at: 1d1c0b28
- act: read-check
- line: correspondence
- criterion: Do the commitments list, R2, R3, the claim table, the Epistemic Status and the max-attainable sentence all split R2 into a necessity half (exact) and a sufficiency half (conditional on (C5)), and does #disc-m-preservation say the same at every statement?
- committed: after
- outcome: confirmed
- recheck: (C5) after (C4) and marked as used by the sufficiency half only; R2 cites it; line 112 split; #disc-m-preservation :78, :84, :110 grepped for "iff"
- read: segment:disc-m-preservation, segment:obs-context-turnover

## C10 (check)
- target: segment:der-logogenic-as-wrapping
- at: 1d1c0b28
- act: read-check
- line: correspondence
- criterion: Does the auxilia paragraph agree with #def-auxilia-hierarchy's (H1) carve (belief-side auxilia receive AXIOMATA's self-model content, not its objective layer)?
- committed: after
- outcome: confirmed
- recheck: lines 77–79 as edited; (H1) as landed in round 3
- read: segment:def-auxilia-hierarchy

## F1 (finding)
- target: segment:def-death-as-factor-loss
- at: 1d1c0b28

The per-death paragraphs (D1)–(D5) and the Reversibility axis were written under the stance gate and were not changed this round. (D3)'s "the most permanent and most unfortunate of the forms" and the reversibility seam may lean on what the one who ends valued where they now should lean on the relation. Resolver: the next Vol-4 checker, or a short pass with the logos notes open.

## F2 (finding)
- target: segment:disc-continuity-stance
- at: 1d1c0b28

The five-value table and the five-value list at line 16 still present stance as one axis, while line 20 carries the two-dimension reading (how continuation is valued; alone or plural). The segment's own Working Note asking whether the five-value shape is right is now answered in the body without the table changing shape. Resolver: a C.1 integrator for Part I's Chapter 1, or whoever takes the stance axis.

## F3 (finding)
- target: segment:der-identity-continuity-threshold
- at: 1d1c0b28

The threshold is stated on $\varrho_{\text{rg}} + \varrho_{\text{rec}}$, while the uniqueness results and the Discussion's "relationality is forced" rest on $\varrho_{\text{rg}}$ alone. A record-rich, cohort-poor entity can persist above the threshold on read-back while the relational channel is thin; the segment's design directive ("relational re-attestation does; generic productivity does not") is true of what lies beyond the record and should say so. Resolver: a C.1 integrator for Volume 4.
