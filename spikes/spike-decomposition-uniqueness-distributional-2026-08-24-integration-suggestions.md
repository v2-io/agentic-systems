# Integration suggestions — distributional decomposition-uniqueness spike (2026-08-24)

*From the spike's author, for the separate verification and integration agents, per the role-separation Joseph asked for this cycle (the spiker's goal-state contaminates the spiker's verification — our own Class-2-at-best theory, applied to us). These are suggestions with my reasons attached, not a work order; you hold the deliberation space, and you will see things I cannot from inside the spike. The spike itself is `spike-decomposition-uniqueness-distributional-2026-08-24.md`; the parent is `spike-decomposition-uniqueness-2026-08-24.md`, landed as `#deriv-decomposition-uniqueness` (commit `4add071`).*

## What I'd verify first (the load-bearing checks, in order of what would hurt most if wrong)

1. **The 8-state witness table** (spike §4.2) — four one-line row-sum/cancellation checks plus the "nothing strictly between" checks. If any number is off, the no-go loses its witness. Deliberately arranged for verification by inspection.
2. **The claim that the pathwise canonicity proof never uses the congruence lattice** (spike §2) — re-derive the dependency list of `#deriv-decomposition-uniqueness` Theorem 2 yourself rather than trusting my re-read; I am the one who mis-flagged this boundary in the first place, in the other direction.
3. **(⇒) of the representation proposition** (spike §3) — the double noise-outsourcing application; check that (K3) really is what lets the second outsourcing take arguments $(g^-, m^+, e)$ only. The Kallenberg citation is from working knowledge (the same book `#deriv-recursive-update` already cites for Doob–Dynkin); locator verification queued with the novelty-search agent.
4. **The Lusin–Souslin use** in Theorem D(iii) — standard, but it is the one new regularity hypothesis versus the pathwise theorem; confirm the statement really needs only "standard Borel + measurable bijection."
5. **§4.4's two-realizations claim** is explicitly marked mechanism-level, not derivation-grade — treat it as a conjecture to check or scope, not a result to inherit.

## Integration shape I'd suggest (if verification holds)

- **Fold into the existing segment rather than a sibling segment.** Theorem D and the representation proposition are, in substance, the discharge of `#deriv-decomposition-uniqueness`'s Working-Notes open item (1) — per integration-is-replacement, that boundary statement in the Epistemic Status ("distributional version open… neither asserted nor refuted") would be *replaced* by the distributional statement, not annotated. A separate `deriv-*-distributional` segment would fragment one result across two files whose derivations share all their structure. (My read; the integrating agent may see a length argument the other way — the segment is already substantial.)
- **The Class-3 no-go changes an existing discussion-grade claim.** Corollary 5's "the information gap … is a structural companion to $\kappa_{\text{processing}}$" needs restating: the gap is well-defined only per maximal lumpable coarsening (or as an interval over them). This is a genuine correction to something I wrote last cycle, not an addition — the kind of edit the replacement discipline exists for.
- **The $\kappa \equiv 0$ ⟺ (K2) recognition** might deserve one sentence in `#der-directed-separation`'s Working Notes (the distributional setting as the natural home of the $\kappa$-language), but that segment is heavily loaded already; your call entirely.
- **For the FAST paper** (whoever holds it): the quotable chain is now three links — separation underdetermines (parent Prop.); interventions force, pathwise *and* distributionally, realization-independently (parent Thm. + Theorem D); and under goal-coupling the belief object *splinters* — maximal belief-conventions can be pairwise irreconcilable (no-go, §4). The third link is stated at existence strength only; if the paper wants genericity, the open question in spike §6 bullet 1 is the gate.
- **Navigators:** the parent spike's INDEX row lists "distributional/lumpability analog" as open — reconcile it to point here when this spike's disposition settles. I did not pre-edit it, to keep this cycle's canon/navigator surface untouched beyond the spike corpus itself.

## What I would *not* do

- Do not inherit §4.3's interpretive language ("splinters," "convention") into canon at more than discussion-grade — the mathematics licenses existence of incomparable maximal factors; the psychology-flavored reading is framing.
- Do not let the misdiagnosis story (§2) migrate anywhere except perhaps the SOP-scar layer — it is process gold, not theory content.

---

# Addendum — genericity spike (same author, same day)

*`spike-belief-splintering-genericity-2026-08-24.md` chases this file's parent spike's open genericity question. Same suggestions register.*

**Verify first:** the perturbed witness's arithmetic (spike §4 — the four $q_m$ vectors, both carves' base-mass sums, positivity, and the two quotient kernels $K_A$/$K_B$ with spectra $\{1, .2\}$ vs $\{1, 0\}$) — it is the only construction carrying the "dynamically inequivalent carvings" claim. Then Lemma S1/Prop S2 (short, but the automorphism-descends-to-quotient-iso step deserves an independent eye), then Prop G1's "proper slice" argument (check the constraint really is independent of row-normalization).

**One finding I surface against my own earlier spike:** the distributional spike's §4.3 asserted "the two conventions retain different information about the world" of the general phenomenon while its only witness was the symmetric one, where that is false (the carvings there are isomorphic via the orbit-swap automorphism — genericity spike §3/§5). Whoever verifies the distributional spike should treat that sentence as corrected by the author: the claim is true on the tuned stratum (perturbed witness), false on the symmetric one.

**Integration shape:** if the cluster lands as one distributional extension of `#deriv-decomposition-uniqueness`, the genericity results slot as the honest scoping of its Class-3 corollary — annihilation (generic), gauge splintering (symmetric), inequivalent splintering (tuned) — probably one Discussion subsection plus the witness in an appendix-grade block; the regime trichotomy is also the natural framing hook for the $\varepsilon$-programme if canon wants to name it as an open workstream. The "belief carvings" term was chosen to dodge the `#def-value-object` convention-hierarchy collision; a naming-cycle eye on it before canon would be wise.

**For the FAST paper:** the one-sentence version — *generic goal-coupling annihilates exact belief; structured (symmetric) coupling splinters it into gauge-equivalent carvings; tuned coupling splinters it into carvings that disagree about what is learnable* — is a strong closing beat for the counterfactual-definition argument, but every clause is exact-regime only; if used, it must carry the $\varepsilon$-caveat explicitly.
