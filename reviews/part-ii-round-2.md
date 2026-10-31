---
kind: review
author:
  name: Claude Fable 5.1 (Part II round-2 integrator)
  role: integrator
sources:
  - msc/inside-out-2026-10/part-ii-check-1.md
  - reviews/part-ii-check-1.md
  - reviews/part-ii-check-1-identification.md
  - reviews/part-ii-check-1-distortion.md
  - reviews/part-ii-check-1-b1-records.md
  - empirica/part-ii-coupling-checks/RUNS.md
written: 2026-10-30
---

# Part II round 2: the integrator's record

KR **C.2** (C2 and C3 independently checked, then landed or refuted), **B.1** (Part II claim records) and **C.1** (every verified defect replaced by an integrator who re-ran the check, then by an independent verifier), under the top intent "Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself." The landing is commit `0fe0a498` on branch `worktree-agent-a6f35eff1ab6cd9c4` (rebased onto main at `3d17de13`), with its vsect record in `4b3bc56c`. Each check below names the check-1 finding it answers, so the next checker can run `vsect findings --answered --by-revision` against the revision of the named segment in `0fe0a498`. The account is `msc/inside-out-2026-10/part-ii-round-2.md`. The two peers' records are `reviews/part-ii-round-2-right-rung.md` and `reviews/part-ii-round-2-drains.md`.

What I did, so the record can be weighed. Ran, from `empirica/part-ii-coupling-checks/` after copying the scripts there: all eleven scripts (RUNS.md has the log and digests). Re-derived by hand: the recalibration identity; the goal-informativeness identity; the global Fisher–Rao constant; the V7 numbers; the C1-against-C3 direct comparison; the rectangularity argument; the g-formula step; the step-5a zero and the broken-tie instance; the (NWI) chain $G \perp \Omega \mid M^- \Rightarrow G \perp \Omega \mid (M^-, a, o)$ through canon's observation function. Read whole: the four check-1 records, the eight segments I edited, `#disc-identifiability-floor` :36–:125, `#def-observation-function`, the ledger's open items on each of the eight segments. Not opened: any cited literature.

## C1 (check)
- target: segment:der-directed-separation
- act: rederive
- line: derivation
- criterion: Answers `review:part-ii-check-1-distortion#C6/finding`, `#F3`, `review:part-ii-check-1#F11` and `question:kappa-processing-is-undefined-0-0-when-the-polic`: $\kappa_{\text{processing}}$ and causal discipline are defined under the probe law (goal drawn from $\rho$ at fixed inputs; denominator $H_\rho(G) \gt 0$), with the operating-law degeneracy stated as the reason, and the interior-action typing closes the redescription loophole.
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: K7 in `empirica/part-ii-coupling-checks/distortion-check-1.py` (operating law $0/0$ for a $0.762$-TV tilt; probe law $\kappa = 1$); by hand, a goal-chosen interior action at fixed external event varies $M^+$ with $G$ under the probe law

## C2 (check)
- target: segment:der-directed-separation
- act: instantiate
- line: derivation
- criterion: Answers `review:part-ii-check-1-distortion#C4/finding` and `#F1`: (NWI) stated as $G_t \perp \Omega_\tau \mid M_{\tau^-}$, the certificate scoped to it, the size of its failure stated as $I(G; \Omega_\tau \mid M_{\tau^-})$ with the restoration. Departure from the finding's text recorded: the form $G \perp \Omega \mid (M^-, a)$ is vacuous for injective policies and holds in K2b where the likelihood-only filter is miscalibrated.
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: K2 and K2b in `distortion-check-1.py` ($0.1927$; $0.1855$ with the action pinned; $0$ for the action-as-evidence update); by hand, with $a = G$ the weak form holds trivially

## C3 (check)
- target: segment:der-directed-separation
- act: rederive
- line: derivation
- criterion: Answers `review:part-ii-check-1-distortion#C3/finding` and `#F2`: clause 3, the degradation norm and Record 4 define the defect as miscalibration; the recalibration identity $\mathbb E S(M) - \mathbb E S(R(M)) = \mathrm{REL}(M)$, $\mathrm{RES}(R(M)) = \mathrm{RES}(M)$ is the directional fact; Record 4's falsifier no longer fires on encode-then-ignore.
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: K3 in `distortion-check-1.py` (encode-then-ignore REL $0$; tilt $0.3301 \to 0.2881$); by hand $P(\Omega \mid R(M)) = R(M)$

## C4 (check)
- target: segment:der-directed-separation
- act: rederive
- line: derivation
- criterion: Answers `review:part-ii-check-1-distortion#C2/finding`, `#F7` (clause 2's converse qualified to informative dropped content; sufficient not necessary) and `#F9` (the three "quality depends on $\kappa$" sites and the $\varepsilon(\kappa)$ phrases replaced by distortion plus the displacement bound).
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: K8 in `distortion-check-1.py`; grep the segment for `coupling scalar`, `varepsilon(\kappa)`: none

## C5 (check)
- target: segment:der-directed-separation
- act: read-check
- line: derivation
- criterion: Answers `review:part-ii-check-1-identification#F3` (its half in this segment) and `review:b1-part-ii-check-1#C5/finding`: Record 3's True-of consumes the zero and the event clause, neither the certificate, and names the $\kappa = 0$ action-dropping collider as why the zero alone is not enough; Record 1 carries the stochastic-$f_M$ proviso. Also `review:part-ii-check-1#F7`'s Working-Note Hafez paraphrase corrected.
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: read Records 1 and 3; `check-part-ii-check-1-kappa0-action-collider.py`

## C6 (check)
- target: segment:def-value-object
- act: run
- line: derivation
- criterion: Answers `review:part-ii-check-1-identification#C4/finding`, `#C6/finding`, `#F3`, `#F4`: one condition on $R_t$ with three routes; premise 1 is causal discipline with the event clause and the exact $\kappa = 0$ collider instance; "rides only on the zero" deleted; "exactly when" and "instrument" replaced.
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: `check-part-ii-check-1-kappa0-action-collider.py` ($0.820/0.180$ vs $0.500$; $H(G \mid e_1) = 0.469$ bits); by hand, $Y^{(a)} \perp R \mid M_t$ gives $a_t \perp Y^{(a)} \mid M_t$ in one step

## C7 (check)
- target: segment:def-value-object
- act: run
- line: derivation
- criterion: Answers `review:part-ii-check-1-identification#C3/finding` and `#F2` (this segment's carrier): the on-policy test is refutable and not confirmable under determinism; Record 1's falsifier is that test; canon's own learner fails it.
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: `check-part-ii-check-1-onpolicy-test-detects.py` ($0.189$–$0.805$ at $M_t = 7$, cells $n \gt 200$)

## C8 (check)
- target: segment:def-value-object
- act: rederive
- line: derivation
- criterion: Answers `review:part-ii-check-1-identification#C7/finding`, `#F5` (this segment's carriers), `review:part-ii-check-1-b1-records#C1/finding`, `#C2/finding`, `#F1` (this segment's carriers), `#F2` and `#F4`: the right rung carries (M) with (PC) or (SO) on the first-action reading; $A_O^{\text{B}} = \sup_a Q_O(a; \pi^\ast)$; rectangularity named; $\delta_{\text{sat}}^{\text{B}} \gt 0$ unconditional; Record 3 carries the C1-against-C3 direct comparison and both failing instances; the struck-through Working Notes deleted. The appendix and the other carriers are in `reviews/part-ii-round-2-right-rung.md`.
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: `check-part-ii-check-1-right-rung-rh-not-in-pi.py` ($15 \gt 6$ with (PC), (SO)); by hand, (PC): $\sup_a Q(a; \pi_{\text{cur}}) = \sup_a V(a \oplus \pi_{\text{cur}}) \leq \sup_\Pi V$; (SO): $Q(a; \pi_{\text{cur}}) \leq Q(a; \pi^\ast)$ per $a$

## C9 (check)
- target: segment:def-value-object
- act: read-check
- line: derivation
- criterion: Answers `review:b1-part-ii-check-1#C6/finding` and `review:part-ii-check-1-identification#F1`'s carrier here: Record 2's False-of rescoped to policies deterministic in what the environment can know, with the private-coin learner excluded from it; the function/true-law split kept.
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: read Record 2 against `check-part-ii-check-1-nogo-scope.py`

## C10 (check)
- target: segment:der-loop-interventional-access
- act: run
- line: derivation
- criterion: Answers `review:part-ii-check-1-identification#C2/finding` and `#F1`: the no-go is scoped to determinism in what the environment can know; the private-coin complement is stated and exact; (P) restated; the no-go and its complement are their own Claim Record; the two-SCM script's two-step reading is no longer leaned on.
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: `check-part-ii-check-1-nogo-scope.py` (16 vs 4 classes); the ignorability argument for the coin by hand ($Y^{(a)} \perp X_t \mid \mathcal C_t$ under canon's coupling; positivity while the coin is unpinned)

## C11 (check)
- target: segment:der-loop-interventional-access
- act: rederive
- line: derivation
- criterion: Answers `review:part-ii-check-1-identification#F2` (this carrier), `#F4(iv)` ($R \perp S \mid Z$ a sufficient condition; $Y^{(a)} \perp R \mid Z$ the weakest stated form), `#F7` (a)–(f) (environment-independent $X_0$; mediated access placed where used; Kalman + LQR moved to the no-go record; Q-learning's visitation hypothesis; Record 2 split) and `review:b1-part-ii-check-1#C8/finding`, `#F1`, `#F2` (the (C2) wording; already landed in round 1, confirmed still so).
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: read the Formal Expression; `check-feedback-1-lemma1b-pstream.py`; weak union then contraction for $R \perp S \mid Z \Rightarrow Y^{(a)} \perp R \mid Z$

## C12 (check)
- target: segment:der-loop-interventional-access
- act: read-check
- line: derivation
- criterion: The "unique broadly-available escape" across floor instances (from the Part I round-5 integrator via the lead) is scoped to Instances 1, 3 and 4, with Instance 2's observational escapes stated; the same shape in the segments I hold recurs only at `#der-orient-cascade` :54, scoped to Instance 1 and true.
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: `#disc-identifiability-floor` :42–:125 (the four instance escape menus); `#deriv-edge-credence-dynamics` :681–:682

## C13 (check)
- target: segment:scope-observation-ambiguity-modulation
- act: rederive
- line: derivation
- criterion: Answers `review:part-ii-check-1-distortion#C8/finding` and `#F4`: Bennett's lemma bound stated and tight; "exact" moved from the $\lambda \cdot \mathrm{sd}$ factorization to the bound; the support factor and the high-gain engineering statement.
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: K1 in `distortion-check-1.py` (ratio $1.0000$ over 20 000; $0.14872/0.06218/0.00708/0.00072$; $\lambda = 10$: $3.1266$); by hand $(e^{\lambda x} - 1 - \lambda x)/x^2$ nondecreasing

## C14 (check)
- target: segment:scope-observation-ambiguity-modulation
- act: rederive
- line: derivation
- criterion: Answers `review:part-ii-check-1-distortion#C9/finding`, `#C10/finding`, `#F6`, `#F9` (this segment's sites), `#F2` (this segment's $\pi$ as the recalibration) and `item:diff-voice-in-present-truth-surfaces-scope-obser` (this segment's half): the no-go on an ambiguity factor stated in the three laws; the identity $I(G; \Omega \mid \mathcal I)$ = goal-averaged per-goal reliability of the pooled report; the per-goal martingale screen; $\kappa = 1$ under the probe law; history narration removed. Departure recorded: F6(ii)'s "positive exactly when, in the probe law" is not so (the goal is independent of everything under the probe law); the quantity with that property is conditioned on $M_{\tau^-}$ alone.
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: K4 in `distortion-check-1.py` ($0.1855 \to 0$ with the action); by hand, $\sum_g P(g)\,\mathbb E_g \mathrm{KL}(P(\Omega \mid \mathcal I, g) \Vert P(\Omega \mid \mathcal I)) = I(G; \Omega \mid \mathcal I)$; V7 for the collider without the action

## C15 (check)
- target: segment:deriv-observation-ambiguity-bias-bound
- act: rederive
- line: derivation
- criterion: Answers `review:part-ii-check-1-distortion#C11/finding`, `#C12/finding`, `#F5` (a)–(d), `review:part-ii-check-1#F8` (a)–(c), `review:items-recheck-t1#F4`, `#F5`, and (b) of `item:bias-bound-lsi-constant-and-large-information-regime`: $d_{FR} := 2\arccos\mathrm{BC}$; global constant $2$ by Rényi monotonicity and $\log\cos\theta \leq -\theta^2/2$; $\sqrt 2$ sharp locally; Lipschitz factor for downstream functionals with $Q_O$'s constant named as unknown; §6's comparator the mixture; Step 1 the definition of mutual information; Paper 3's body citations moved to Working Notes; the history paragraph deleted; all laws under the probe law; the mixture-LSI question recorded as open.
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: K5 in `distortion-check-1.py` ($\arccos\mathrm{BC} \leq \sqrt{\mathrm{KL}}$ on 20 000 pairs); by hand $D_{1/2} \leq D_1$ and $(\log\cos)'' = -\sec^2 \leq -1$; §4's $\Delta\sigma \approx \sqrt 2\,\sigma$ at $d_{FR} = 2$

## C16 (check)
- target: segment:result-section-ii-survival
- act: read-check
- line: derivation
- criterion: Answers `review:part-ii-check-1#F2` (the primary site) and `#F1`'s Working-Note carrier here: $\Delta M_{\text{bias}}$ is only the displacement; the diagnostic error is bounded by the distortion $D_G$ against the calibrated belief; coupled-minus-goal-blind named as a third quantity and not used; the Epistemic Status and the Working Note carrier of the linear $C\kappa I$ form rewritten. The four downstream sites are the drains peer's.
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: grep the segment for `I(G;\Omega`, `f_X^M`: the first absent, the second only in the sentence that names the third quantity

## C17 (check)
- target: segment:der-orient-cascade
- act: rederive
- line: derivation
- criterion: Answers `review:part-ii-check-1-distortion#C13/finding`, `#F8` (5a's cost sentence carries the qualifier; the general iff), `review:part-ii-check-1#F4` (this segment's :91) and `review:b1-part-ii-check-1#C16/finding` (the body no longer says the ordering is forced), `#F9`'s :105 site.
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: K6 in `distortion-check-1.py` (cost on $a_1$: VOI $0$); the two-line zero by hand

## C18 (check)
- target: segment:def-model-sufficiency
- act: rederive
- line: derivation
- criterion: Answers `review:part-ii-check-1-identification#C8/finding`, `#F6` and `#F2` (this carrier), and `question:s-m-t-conditions-on-realized-future-actions-a-t`: the echo instance carries its second bit with the denominator reproducible; the condition is on $R_t$; interventional sufficiency relative to $\mathcal C_t$ with an environment-independent initial state; the one-sided test.
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: by hand, bits $c, c'$ with $M_t = c'$, $o_{t+1} = c$, $o_{t+2} = c'$, $a_{t+1} = o_{t+1}$: numerator $0$, denominator $1$ bit

## C19 (check)
- target: segment:causal-access-intro
- act: read-check
- line: reading
- criterion: Answers `review:part-ii-check-1-identification#C11`'s wording point and `#F7(e)`: "exactly when" → "when".
- committed: after
- at: 0fe0a498
- outcome: confirmed
- recheck: grep `exactly when it moved`: none

## C20 (check)
- target: segment:disc-partial-coupling-pathways
- act: read-check
- line: derivation
- criterion: Answers `review:part-ii-check-1-distortion#C16/finding` and the second site of `#F7`: the allocation row's "distortion when the drop decision depends on dropped content" is qualified to content that bears on the world given what was retained.
- committed: after
- at: d8248ca2
- outcome: confirmed
- recheck: K8 in `distortion-check-1.py`

## F1 (finding)
- target: segment:def-value-object

**$Q_O$'s Lipschitz constant in $M_t$ is stated nowhere, and the displacement bound's use on the value object needs it.** The appendix now says the goal-dependence of a downstream functional's expectation is $\mathrm{Lip}(F)$ times the displacement bound. For $Q_O$ the constant depends on the objective functional and the horizon, and no segment derives it; until one does, "this bound says by at most how much" is a bound with an unnamed factor. Owner C.4.

## F2 (finding)
- target: segment:deriv-observation-ambiguity-bias-bound

**The log-Sobolev constant of the goal-marginal mixture is itself goal-dependent beyond the small-separation limit.** Recorded in the Epistemic Status as open; not computed. Track 1's constant is therefore exact only where (H2) is checked for the mixture, and §6's $\rho_{\text{LSI}} \approx 1/\sigma^2$ is the $\beta \ll \sigma$ case. Owner C.4 (`item:bias-bound-lsi-constant-and-large-information-regime` (a)).

## F3 (finding)
- target: segment:der-loop-interventional-access

**The LQR closed-loop ridge script exited 0 and printed nothing in my environment.** `check-part-ii-check-1-lqr-closed-loop.py` was not copied into `empirica/`; no body leans on its result after this round (Kalman + LQR is a by-construction record and the no-go's True-of), but the identification checker's C9 reported a numerical ridge from it and that run is not reproduced here. Whoever next touches the Kalman + LQR instance should run it and either register it or drop the reference to the numerical evidence.
