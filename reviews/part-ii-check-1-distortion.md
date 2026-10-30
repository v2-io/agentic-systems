---
kind: review
author:
  name: Claude Opus 5.5 (Part II independent check, allocation-vs-distortion side)
  role: checker
sources:
  - 01-aat-core/src/der-directed-separation.md
  - 03-llm-core/src/scope-observation-ambiguity-modulation.md
  - 01-aat-core/src/deriv-observation-ambiguity-bias-bound.md
  - 01-aat-core/src/der-orient-cascade.md
  - 01-aat-core/src/form-information-bottleneck.md
  - 01-aat-core/src/der-class-coercion-via-wrapping.md
  - 01-aat-core/src/disc-partial-coupling-pathways.md
  - spikes/spike-allocation-vs-distortion-coupling-2026-10-30/01-derivation.md
  - spikes/spike-allocation-vs-distortion-coupling-2026-10-30/de-novo-feedback-1.md
  - spikes/spike-allocation-vs-distortion-coupling-2026-10-30/sims/check.py
  - spikes/spike-allocation-vs-distortion-coupling-2026-10-30/sims/check-part-ii-check-1.py
  - reviews/part-ii-integration-1.md
  - msc/inside-out-2026-10/part-ii-integration.md
written: 2026-10-30
---

# Part II check 1: the allocation-vs-distortion side

KR **C.2** (C3: allocation vs distortion coupling, independently checked then landed or refuted), **C.1** (every verified defect replaced, re-checked by an independent verifier) and **B.1** (Part II claim records), under the top intent "Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself." Scope: the landing in `253d2bca`..`279b2699` on `#der-directed-separation` (Scope Condition, $\kappa_{\text{processing}}$, degradation norm, records), `#scope-observation-ambiguity-modulation`, `#deriv-observation-ambiguity-bias-bound`, and the rides-along in `#der-orient-cascade` 5a, `#form-information-bottleneck`, `#der-class-coercion-via-wrapping`, `#disc-partial-coupling-pathways`. The seven segments are unchanged between `279b2699` and the HEAD I read (`d037e0fc`; `git diff --stat` over all seven is empty).

How I worked, so the record can be weighed: I read the seven segments cold first (the three main ones in full; for the four smaller landings, the diff plus the surrounding paragraphs), wrote down what looked wrong, and only then read the integrator's account (`msc/inside-out-2026-10/part-ii-integration.md`, whole), the header and C1–C4 of its typed checks (`reviews/part-ii-integration-1.md`), and grep hits in the spike's `01-derivation.md` (§1.2, §5, §8) and in the verifier's `de-novo-feedback-1.md` (its lines 15, 29–53, 79, 97, 106: V4–V7, the per-goal-law section, the probe-law remark). I did not read either spike file end to end. **Ran:** the spike's `sims/check.py` (output byte-identical to the committed `check-output.txt`), and my own exact enumerations `spikes/spike-allocation-vs-distortion-coupling-2026-10-30/sims/check-part-ii-check-1.py` with output beside it in `check-part-ii-check-1-output.txt` (both uncommitted, placed beside the spike's sims as the integrator did with its C2 scripts; keep, move or drop as you see fit). Items below cite them as K1–K8. **Re-derived by hand:** every identity and inequality named in the checks. **Read only:** grep hits for Fisher–Rao / arc / chord in Paper 3's `README.md`, `meta.md` and `TODO.md` (not its `src/` proofs); none of the cited literature (Murphy, Bröcker, Gneiting–Raftery, Rubin, Otto–Villani, Bennett) was opened — the textbook statements I used are from recall and are marked where load-bearing. I did not check the Related Work tables, the Hafez/IDT wording, or the A4 dual-effect rows.

The short version. The core of the landing is right and is a real improvement: the three-way split (identification / goal-dependence / distortion), calibration as the invariant, the event pinned to include the action with the V7 collider, the model-free log-ratio bound, the fixed-gain hypothesis with its test, the retirement of $\mathcal A$ and the product law, the appendix re-anchored on the post-update law. Four things in canon are not true as written and each has a fix that strengthens rather than softens: **F1** the per-goal calibration criterion and the Class 1 certificate need the spike's (NWI) premise, which did not land; **F2** clause 3 and Claim Record 4 define the defect as *departure from the conditional law*, which calibrated coarsenings also do, so the record's own falsifier fires; **F3** once the event includes the action, every quantity conditioned on $(e_\tau, M_{\tau^-})$ under the operating law degenerates for injective policies — $\kappa_{\text{processing}}$, causal discipline, the appendix's bound — and the repair is to state them under the probe law the estimators already use; **F4** the tilt factorization is called exact where it is leading-order, and Bennett's lemma makes the sharpness dependence exact. F5–F9 are smaller.

## C1 (check)
- target: segment:der-directed-separation
- at: 279b2699
- act: rederive
- line: derivation
- criterion: Scope Condition, "What the event is": V7 — with $\Omega$ a fair bit, $a = G$, $e = \Omega \oplus a$, $P(G = 0) = 0.8$, the action-free goal-blind posterior is $0.2$ at $e = 0$ and $0.8$ at $e = 1$, pooled-calibrated and per-goal miscalibrated; per-goal calibration implies pooled calibration and not conversely; "calibrated iff conditional law given some sub-$\sigma$-field of the agent's information" by the tower property.
- committed: after
- outcome: confirmed
- recheck: by hand — $P(\Omega = 1, e = 0) = P(\Omega = 1, G = 1) = 0.1$, $P(e = 0) = 0.5$; $P(\Omega \mid m) = \sum_g P(g \mid m)\, P_g(\Omega \mid m)$

All three re-derive. The converse direction of the calibration characterization needs the report to be measurable with respect to the agent's information, which "a belief the agent reports" supplies. The verifier's per-goal reliabilities for V7 ($0.2231$ and $1.6094$ nats) I did not recompute; the pooled/per-goal asymmetry I did.

## C2 (check)
- target: segment:der-directed-separation
- at: 279b2699
- act: rederive
- line: derivation
- criterion: Clause 2 — an allocation whose retention pattern depends only on quantities the update conditions on (goal, prior state, action, retained content) yields a report calibrated under each goal's law; and the converse sentence at `:58`, "a mechanism that drops a feature because of what it showed … is allocation in form and distortion in effect."
- committed: after
- outcome: narrowed
- recheck: `check.py` N5; verifier's V6 in `de-novo-feedback-1.md` §3; K8 in `check-part-ii-check-1.py`

Sufficiency re-derives: with the pattern $R = r(g, Z)$ a function of the goal and retained content $Z$, under goal $g$'s law the event $\{R = r, Z = z\}$ is $\{e_r = z\}$, so the report $P(\Omega \mid e_r = z)$ is the conditional law given what the agent holds — calibrated, *given (NWI)* (F1). The converse sentence at `:58` is stated unconditionally and is false: the verifier's V6 (drop a feature independent of $\Omega$ on its own value) is content-dependent dropping with reliability $0$. The integrator's account says Prop A′ landed as sufficiency; the sufficiency did land, but this sentence carries the converse. See F7.

## C3 (check)
- target: segment:der-directed-separation
- at: 279b2699
- act: instantiate
- line: derivation
- criterion: Clause 3 (`:59`), the degradation norm (`:120`) and Claim Record 4 (`:205`, `:213`): "the conditional law given the agent's information is the unique minimizer of expected score among beliefs measurable with respect to that information, so a goal-dependent departure from it strictly worsens the reliability term"; the falsifier "a goal-dependent belief that departs from the conditional law … yet has reliability zero … impossible."
- committed: after
- outcome: broken
- recheck: K3 in `check-part-ii-check-1.py` (N3's world)

The inference is invalid and the falsifier fires. Unique minimization is a statement about total expected score; the score splits into uncertainty minus resolution plus reliability, and a departure can sit entirely in resolution. K3: an agent that encodes $(x_1, x_2)$ and, under goal $g_1$, reports $P(W \mid x_1)$ departs from $P(W \mid x_1, x_2)$, is goal-dependent, costs $0.0297$ nats of expected log score, and has reliability exactly $0$ (resolution $0.3849 \to 0.3552$). That agent is report-identical to N3's "allocate $x_1$ only" agent, so the segment's own boundary-independence argument (`:61`) requires them to be classified alike. See F2 for the fix and the directional fact that does hold.

## C4 (check)
- target: segment:der-directed-separation
- at: 279b2699
- act: instantiate
- line: derivation
- criterion: The Class 1 certificate (`:120`: "at $\kappa_{\text{processing}} = 0$, with the realized action reaching the update as an event and entering only through the likelihood, no goal-attributable reliability loss is possible, by inspection of the wiring"), the Scope Condition's "under the agent's own model the statements hold unconditionally" (`:61`), and per-goal calibration as the law of evaluation, when the goal carries world information — a case canon itself names (Record 4 False-of; `#def-value-object` record 1 False-of).
- committed: after
- outcome: narrowed
- recheck: K2 and K2b in `check-part-ii-check-1.py`

When the goal is evidence about the world, a goal-blind Bayes filter is per-goal miscalibrated: in N7β's world it has log-score reliability $0.1927$ nats under each goal's law (K2). With the action pinned in the event (principal-set goal, $a = G$, $e = (a, o)$), the likelihood-only filter has per-goal reliability $0.1855$ nats under each goal, and the goal-blind update that is per-goal calibrated is the one that treats the realized action as *evidence* about $\Omega$ — which the certificate's "entering only through the likelihood" excludes (K2b). So without a premise the certificate is both insufficient and too narrow. Under the spike's (NWI), $G \perp \Omega \mid (M_{\tau^-}, a_\tau)$, plus an observation kernel that sees the goal only through the action, the two coincide and the certificate holds. The premise did not land (`grep` for NWI / "world information" in the segment: none). See F1.

## C5 (check)
- target: segment:der-directed-separation
- at: 279b2699
- act: rederive
- line: derivation
- criterion: "What $\kappa_{\text{processing}}$ measures, and does not" (`:98`): $\kappa = 1$ for any deterministic injective goal-dependence at fixed $(e_\tau, M_{\tau^-})$ whatever its magnitude; a function of $\lambda / s$ under location noise; positive for allocation, for the goal-as-evidence Bayesian, and for lossy $M$ beside a richer $G$; $\hat\kappa$ is a displacement, not the mutual information.
- committed: after
- outcome: confirmed
- recheck: `check.py` N2, N8, N9

All re-derive *when $H(G \mid e_\tau, M_{\tau^-}) \gt 0$*. That proviso is not a corner case after the pin; C6.

## C6 (check)
- target: segment:der-directed-separation
- at: 279b2699
- act: instantiate
- line: derivation
- criterion: With $e_\tau$ including the realized action (the landing's pin) and a policy injective in $G_t$ at fixed $M_{\tau^-}$, which quantities defined by conditioning on $(e_\tau, M_{\tau^-})$ under the operating law remain meaningful: $\kappa_{\text{processing}}$, causal discipline ("the condition $\kappa_{\text{processing}} = 0$", `:116`), Claim Record 1's conditional independence, and the appendix's goal-conditional versus goal-marginal laws.
- committed: after
- outcome: broken
- recheck: K7 in `check-part-ii-check-1.py`; by hand — $G = \pi^{-1}(a, M_{\tau^-})$ is a function of the conditioning set

$G$ is a function of $(e_\tau, M_{\tau^-})$, so $H(G \mid e_\tau, M_{\tau^-}) = 0$ and $I(G; M_{\tau^+} \mid e_\tau, M_{\tau^-}) = 0$ for *every* $f_M$, distorting ones included (K7: a tilt whose goal-conditioned reports differ by $0.762$ in total variation reads numerator $0$ and denominator $0$). The segment notices the denominator (`:98`, "no convention is adopted here") and the Working Note notices the independence holding for every update (`:269`), but the consequence is wider than a $0/0$ convention: causal discipline as defined is undefined, or (read as numerator-zero) satisfied by every deterministic agent including Class 3; the appendix's bound reads $0 \leq 0$ (C11); and with coarse actions ($\lvert\mathcal A\rvert \lt \lvert\mathcal G\rvert$) the operating-law quantities see only goal-dependence orthogonal to what the action reveals, so a tilt toward the goal that also drives the action is invisible to them. The integrator's open question on the denominator (`vsect open`) is a symptom of this. See F3.

## C7 (check)
- target: segment:scope-observation-ambiguity-modulation
- at: 279b2699
- act: rederive
- line: derivation
- criterion: The log-ratio-range bound: $\mathrm{KL}(\pi \Vert M) = \log \mathbb E_\pi \tilde r - \mathbb E_\pi \log \tilde r$; Hoeffding gives $\mathrm{KL}(\pi \Vert M) \leq L^2/8$; the reverse direction via $\mathbb E_M e^{-X} = 1/\mathbb E_\pi e^X$; Pinsker gives $\mathrm{TV} \leq L/4$; the instance $\mathrm{KL}((0.99, 0.01) \Vert (0.5, 0.5)) = 0.637$ nats.
- committed: after
- outcome: confirmed
- recheck: three lines each by hand; `check.py` N1, N12

All re-derive as written, including the reverse Hoeffding step under $M$ for $-X$. The paragraph's reading of the bound ("by the size of the reweighting, and by nothing about the evidence") is exactly as strong as it should be.

## C8 (check)
- target: segment:scope-observation-ambiguity-modulation
- at: 279b2699
- act: rederive
- line: derivation
- criterion: Under the fixed-gain tilt, $\mathrm{KL}(\pi \Vert M) = \Lambda_\pi(\lambda) - \lambda \mathbb E_\pi u_G = \tfrac{\lambda^2}{2}\mathrm{Var}_\pi(u_G) + O(\lambda^3)$; the four values $0.120$, $0.059$, $0.0070$, $0.00072$ nats at $\lambda = 1$, $u = (0, 1)$; $8.9$ nats at $\lambda = 0.5/\mathrm{sd}_\pi(u)$, $\pi(\Omega = 1) = 0.001$; and the Epistemic Status claim (`:80`) "under it the factorization and the sharpness dependence are *exact* (cumulant expansion)."
- committed: after
- outcome: narrowed
- recheck: K1 in `check-part-ii-check-1.py`; the four values by hand ($\log(0.5 + 0.5e) - 0.5 = 0.1201$, etc.)

The identity, the expansion and all five numbers re-derive. The exactness claim does not: the exact quantity is the cumulant generating function, which depends on the whole law of $u_G$ under $\pi$, and $\lambda \cdot \mathrm{sd}$ is its leading order only. At $\lambda = 1$, $\pi(\Omega = 1) = 0.1$ the KL is $0.0586$ against $\tfrac{\lambda^2}{2}\mathrm{Var} = 0.045$, so the leading form is not even an upper bound there; across random instances the ratio reaches $9235$. The sharpness dependence *can* be made exact — F4.

## C9 (check)
- target: segment:scope-observation-ambiguity-modulation
- at: 279b2699
- act: rederive
- line: derivation
- criterion: The retirement of $\mathcal A(e_\tau)$ and the product law: $I(G; \Omega_\tau \mid e_\tau, M_{\tau^-}, a_\tau) = 0$ under $G \perp \Omega_\tau \mid (M_{\tau^-}, a_\tau)$; "positive exactly when the goal is evidence about the world," "demonstrated in the Discussion" (`:66`, `:84`); N7α and N7β numbers ($0.762$, $0.278$, $0.30$, $0.5004$, $0.6931$).
- committed: after
- outcome: narrowed
- recheck: `check.py` N7; K4 in `check-part-ii-check-1.py`

The zero re-derives, given also that the observation kernel depends on the goal only through the action (implicit in canon's setup; worth one clause). The N7 numbers reproduce. The "positive exactly when" half is not demonstrated in the setting the segment now uses: the Discussion's N7β computes without the action, while `:84` puts $a_\tau$ in the conditioning set. With the action in the event and an injective policy, the quantity is $0$ for an informative goal too (K4: $0.1855$ nats without the action, $0$ with it) — the verifier made this point (`de-novo-feedback-1.md` §5, "A strengthening the spike did not make") and it did not land. The retirement survives and in fact strengthens: under the pin, $\mathcal A \equiv 0$ for every injective-policy agent, informative goal or not. See F6, which also says what the retired numerator does measure.

## C10 (check)
- target: segment:scope-observation-ambiguity-modulation
- at: 279b2699
- act: read-check
- line: derivation
- criterion: Measurement paragraph — goal-probing cannot separate the processor factor from the observation factor; separating allocation from distortion needs outcomes or a reference posterior; the martingale screen; "$\kappa$ is $1$ for every $\lambda \gt 0$ with distinct $u_G$."
- committed: after
- outcome: narrowed
- recheck: read `:72` against C6

The identifiability statements are right. Two qualifications: the martingale screen has to be applied *per goal* (a goal-symmetric tilt — "ship" up, "correct" down — passes a goal-averaged screen); and "$\kappa = 1$" holds only under the probe law (C6, F3). Both are one-phrase fixes (F9).

## C11 (check)
- target: segment:deriv-observation-ambiguity-bias-bound
- at: 279b2699
- act: rederive
- line: derivation
- criterion: Track 1 — $\mathbb E_G \mathrm{KL}(P_{M^+ \mid G} \Vert P_{M^+}) = I(G; M^+ \mid e, M^-)$; Otto–Villani $W_2^2 \leq (2/\rho_{\text{LSI}})\mathrm{KL}$ with the goal-marginal post-update law as reference measure; no pushforward needed; §6's first-order tightness; and the bound's content under the operating law after the pin.
- committed: after
- outcome: narrowed
- recheck: by hand; §6 with $\mathrm{KL}(N(\beta, \sigma^2) \Vert N(0, \sigma^2)) = \beta^2/(2\sigma^2)$

The identity is the definition of mutual information as an expected KL (the citation to a chain-rule theorem is fine but it is simpler than that). Otto–Villani is applied with the right reference measure, and both laws compared are laws of the belief, so no pushforward is needed — confirmed. §6 is tight to first order; its comparator should be the mixture, not $N(0, \sigma^2)$ (same first order, but $W_2^2$ to the mixture is at least $\beta^2$ by the mean shift, so say "at least $\beta^2$"). Not confirmed, recorded as a question: (H2) is an LSI on a *mixture over goals*, and mixture LSI constants degrade with component separation, so $\rho_{\text{LSI}}$ itself carries goal-dependence beyond §6's $\beta \ll \sigma$ limit (from recall; not computed). Under the operating law with the pin and an injective policy, both sides are $0$ (C6). See F3, F5.

## C12 (check)
- target: segment:deriv-observation-ambiguity-bias-bound
- at: 279b2699
- act: rederive
- line: derivation
- criterion: Track 2 — the (H1) definition of $d_{FR}$ as "the Fisher–Rao spherical-arc distance … as points on the unit $L^2$-sphere of $\sqrt p$", Step 1 "$\mathrm{KL} = \tfrac12 d_{FR}^2 + O(d_{FR}^3)$", $C_{FR} = \sqrt 2$ under (H4), §6's Track-2 tightness, and Honest failure mode 4 (no global statement).
- committed: after
- outcome: narrowed
- recheck: K5 in `check-part-ii-check-1.py`; the three-line global derivation in F5

The definition and Step 1 are inconsistent by a factor of $2$ in distance: the arc $\theta = \arccos \int\!\sqrt{pq}$ on the unit sphere satisfies $\mathrm{KL} \approx 2\theta^2$ (K5: $\theta^2/\mathrm{KL} \to 0.5$), while $\mathrm{KL} \approx \tfrac12 d^2$ holds for $d = 2\theta$, the geodesic distance of the Fisher metric (K5: $(2\theta)^2/\mathrm{KL} \to 2$). §6 and the constant $\sqrt 2$ use $d = 2\theta$; Paper 3's TODO (`d_FR^2 = 16\arcsin^2(\mathrm{Hel}/\sqrt2)`) uses $2\theta$ too. With $d_{FR} := 2\theta$ the local result stands, and a global bound with constant $2$ follows in three lines without (H4) — F5.

## C13 (check)
- target: segment:der-orient-cascade
- at: 279b2699
- act: rederive
- line: derivation
- criterion: Step 5a — when every action in $D$ pays the same under infeasibility, $\mathrm{VOI}(\text{feasibility}) = 0$; an abandon action breaks this only when optimal under infeasibility and not under feasibility; "a pursuing action with a cost paid regardless of feasibility breaks it too."
- committed: after
- outcome: narrowed
- recheck: `check.py` N6, N10; K6 in `check-part-ii-check-1.py`

The zero re-derives in two lines: with $p(X) = P(\text{feasible} \mid X)$, $\max_a \mathbb E[u_a \mid X] = p(X)\max_a v_a(X) + (1 - p(X))\,c(X)$, which equals the expectation of $\max_a \mathbb E[u_a \mid X, F]$ over $F$. The abandon-action qualifier is right (N10). The cost sentence is stated without the same qualifier and is false as written: K6 puts the always-paid cost on the action that is *not* best under feasibility; the tie is broken and $\mathrm{VOI} = 0$ still (the verifier's V5, $0.06$, reproduces because its cost sits on the feasible-best action). See F8.

## C14 (check)
- target: segment:form-information-bottleneck
- at: 279b2699
- act: rederive
- line: derivation
- criterion: Policy-relative IB compression is allocation in clause 2's sense — the encoder is chosen from the policy, not from dropped content — so the model on the compressed state is calibrated for every policy; the crack is in the conditional-independence form only.
- committed: after
- outcome: confirmed
- recheck: clause 2 applied with the pattern a function of the policy and retained state

Confirmed, given (NWI): the policy depends on $(M_t, G_t)$, both of which the update conditions on, so the pattern is ignorable. Carries F1's premise like every other "calibrated" claim in the cluster.

## C15 (check)
- target: segment:der-class-coercion-via-wrapping
- at: 279b2699
- act: rederive
- line: derivation
- criterion: The new paragraph (`:161`) — a cue-reading tilt is a fixed function of $q_M$, so it satisfies (C3) as formalized at `:57`; $\kappa_{W_1}^{\text{sel}}$ mixes calibration-preserving query selection with cue-triggered distortion; the missing condition is the component's answer calibrated given the query.
- committed: after
- outcome: confirmed
- recheck: read `:55`–`:59` and `:75`

Confirmed, and sharper than the paragraph says: (C3)'s words ("does not depend on $G_W$ via inference from query patterns") exclude the cue-reading tilt, and its formula $P(A(q_M) \mid q_M, G_W) = P(A(q_M) \mid q_M)$ admits it, so the theorem's hypothesis in words is stronger than the hypothesis it proves from. "Calibrated given the query under each operator goal's law" again needs F1's premise. The integrator already logged the wrapping finding in `vsect open`; nothing new to open beyond that.

## C16 (check)
- target: segment:disc-partial-coupling-pathways
- at: 279b2699
- act: read-check
- line: derivation
- criterion: The rewritten "goal-directed attention / allocation" row: the boundary is representational and the verdict does not depend on it; ignorable allocation is calibrated; "the same goal-dependence at P1 is *distortion* when the drop decision depends on dropped content."
- committed: after
- outcome: narrowed
- recheck: as C2

The first two parts hold. The third is C2's unconditional converse again (F7).

## F1 (finding)
- target: segment:der-directed-separation
- at: 279b2699

**The per-goal calibration criterion and the Class 1 certificate need the spike's (NWI) premise, and it did not land.** Canon now evaluates calibration under each goal's law (`:61`) and lists "correct Bayesian use of a goal that carries world information" as benign (Record 4 False-of, `:211`). In that case a goal-blind Bayes filter is per-goal miscalibrated (K2: $0.1927$ nats under each goal in N7β's world). With the action pinned in the event, the likelihood-only filter is per-goal miscalibrated by $0.1855$ nats under each goal, while the per-goal-calibrated goal-blind update is the one that reads the realized action as evidence about $\Omega$ — which the certificate's "entering only through the likelihood" forbids (K2b). So the certificate at `:120` ("no goal-attributable reliability loss is possible, by inspection of the wiring"), the "unconditionally" at `:61`, and every "calibrated" in C2, C14, C15 hold only when the goal carries no world information beyond what the update conditions on.

What I would land, in the Scope Condition, right after "What the event is": a third pin, **(NWI) the goal carries no world information beyond the prior state and the realized action, $G_t \perp \Omega_\tau \mid (M_{\tau^-}, a_\tau)$, and the observation kernel depends on the goal only through the action.** Under (NWI) per-goal and pooled calibration of a goal-blind update coincide with the likelihood-only Bayes filter, and the certificate holds as written. When (NWI) fails — a goal set by a principal who knows more; canon's own $f_G(G^-, M^+, e)$ retaining what a lossy $M$ dropped — the restoration is the spike's §1.2: record the goal-setting (or the retained content) as an *event* the update conditions on; then (NWI) holds for the residual and no goal port is needed (K2's restoration line). It is the analog, for the world state, of the third premise `#def-value-object` already carries for outcomes ("the policy-relevant part of $G_t$ carries no outcome information beyond $M_t$"; I saw that premise through grep and the integrator's account, not a full read), so stating it here would make the two segments speak the same way. It also gives the certificate its exact scope: by inspection of the wiring, a Class 1 agent cannot *distort*; whether it is per-goal calibrated additionally depends on (NWI), which is a property of where its goals come from, not of its wiring. F6 gives the size of the failure when (NWI) does not hold.

Why the four hands missed it, as best I can tell: the spike stated (NWI) as a hypothesis at its §1 and every later result was conditional on it; the verifier then argued (rightly) for per-goal law over pooled; the integrator landed the per-goal law and the goal-as-evidence examples but not the premise that made them consistent. Each step was correct locally.

## F2 (finding)
- target: segment:der-directed-separation
- at: 279b2699

**The defect is miscalibration, not departure from the conditional law; clause 3, the degradation norm and Record 4 say "departure," and Record 4's own falsifier fires (C3, K3).** Sites: clause 3 at `:59` ("Given what it encoded, the update reports the conditional law … Any goal-dependent departure from that conditional … is the defect"); the norm at `:120` ("…unique minimizer…, so a goal-dependent departure from it strictly worsens the reliability term"); Record 4 Register `:205` and Falsifier `:213`. An encode-then-ignore report is a departure at fixed encoded information with reliability $0$, and it is report-identical to not encoding, which `:61`'s boundary-independence argument says must be classified the same. The same slip sits in `#scope-observation-ambiguity-modulation` `:22`–`:26`: with $\pi := P(\Omega \mid \mathcal H)$ for "the information the update conditions on," an encode-then-ignore report has $\mathrm{KL}(\pi \Vert M) \gt 0$ and reliability $0$, so "zero for every $G$ exactly when … allocation only" fails unless $\mathcal H$ is read as what the report is measurable with respect to.

What I would land. Clause 3: "**Distortion is forbidden.** The reported belief is calibrated under each goal's law — it is the conditional law of the world given *some* information the agent holds. A report that is not, under some goal — reweighting, tempering, tilting toward the goal — is the defect; giving up information the agent holds is allocation, priced in resolution." Norm and Record 4 Register: replace the "so" with the directional fact that does hold, which is stronger: writing $R(M) := P(\Omega \mid \sigma(M))$ for the report's recalibration, for any strictly proper score $\mathbb E\,S(M) - \mathbb E\,S(R(M)) = \mathrm{REL}(M) \geq 0$ with equality iff $M$ is calibrated, and $\mathrm{RES}(R(M)) = \mathrm{RES}(M)$ — distortion is exactly the score recoverable by recalibration, at no cost in information (K3: the N3 tilt scores $0.3301$, reliability $0.0420$, recalibrated $0.2881$ = full-information score; standard decomposition, Bröcker 2009 from recall). The "unique minimizer" sentence stays as the separate statement that any departure worsens total score, of which the reliability part is distortion and the resolution part is allocation. Record 4 Falsifier: drop "impossible by the characterization of proper scores" (it is a definition once the defect is miscalibration); keep the misspecification and deployed-comparison falsifiers. In the scope segment, define $\pi$ as the recalibration $P_G(\Omega \in \cdot \mid M^{(G)}_{\tau^+})$ — equal to $P(\Omega \mid \mathcal H)$ when the report is one-to-one in $\mathcal H$ — so per-event distortion is the reliability integrand; the range bound and the tilt hypothesis go through unchanged with this $\pi$ (an injective tilt of $\pi$ has recalibration $\pi$).

## F3 (finding)
- target: segment:der-directed-separation
- at: 279b2699

**After the pin, state $\kappa_{\text{processing}}$, causal discipline and the appendix's displacement under the probe law, not the operating law (C6, C10, C11, K7).** Under the operating law, $G$ is a function of $(e_\tau, M_{\tau^-})$ for an injective policy, so every goal quantity conditioned on them degenerates for every update. That leaves the noun Part II scopes to — causal discipline, "$\kappa_{\text{processing}} = 0$" (`:116`) — undefined, or satisfied by Class 3 agents; it is the quantity `#def-value-object`'s premise 1 consumes. It is not a $0/0$ convention question (the open `vsect` question on the denominator): the numerator is identically zero too.

What I would land: one definition, used in all three places. *Probe law:* draw $G$ from a reference law $\rho$ independent of $(M_{\tau^-}, e_\tau)$ and evaluate the update at fixed inputs, so the post-update law under goal $g$ is the law of $f(M_{\tau^-}, e_\tau, g, \xi)$ — the structural, interventional reading, with $\xi$ the update's own randomness. Then $\kappa_{\text{processing}} := I_\rho(G; M_{\tau^+} \mid e_\tau, M_{\tau^-}) / H_\rho(G)$, whose denominator is positive for any non-degenerate $\rho$; causal discipline is "the post-update law does not depend on $g$ under do$(G = g)$ at fixed inputs" (a no-port statement, which is what Class 1 has by signature and what the collider argument in `#def-value-object` needs); and the appendix's "goal-conditional" and "goal-marginal" laws are the probe-law ones. This is what the estimators already measure: $\hat\kappa$ "present[s] the same event $e$ … under two or more distinct goal states" (`:102`), and Paper 3's JSD estimator is this with $\rho$ uniform binary. The cost to state honestly: for a deterministic policy, $(e_\tau, g)$ with $g \neq \pi^{-1}(a_\tau)$ is off the operating support, so the probe quantity is a property of the update map, not of the data the agent generates — which is what "ports" (`:98`) means. Sites to touch: `:90`–`:96` (definition and bands), `:98` (replace the denominator sentence), `:116` (causal discipline), `:155` Epistemic Status ("well-defined" holds for the probe-law version only), `#deriv-observation-ambiguity-bias-bound` §1 (name the law), `#scope-observation-ambiguity-modulation` `:72` ("$\kappa$ is $1$" under the probe law). The Working Note at `:269` can then say why adding $a_t$ to the conditioning set is not the repair *and* what is. What rests on the definition (my grep for "$\kappa_{\text{processing}} = 0$" / "causal discipline" / "causally-disciplined" across `0*-*/src`, sites read in context but not re-derived): `#def-value-object` `:17`, `:55`, `:135` (premise 1, the collider argument, and the C2 simulations "at $\kappa_{\text{processing}} = 0$" — those are Class 1 by construction, so they survive under the probe-law definition unchanged); `#der-orient-cascade` `:105` (Record population); `#impl-orient-cascade` `:34`, `:50`; `#der-loop-interventional-access` `:83`; `#hyp-truth-serving-loophole` `:15`; `#der-logogenic-as-wrapping` `:65`. Each uses the zero as a no-port fact, which the probe-law reading supplies; none, as far as I read, needs the operating-law mutual information.

## F4 (finding)
- target: segment:scope-observation-ambiguity-modulation
- at: 279b2699

**Under the fixed-gain hypothesis the sharpness dependence is exact by Bennett's lemma; the $\lambda \cdot \mathrm{sd}$ factorization is its leading order (C8, K1).** Write $X = u_G - \mathbb E_\pi u_G$ and $b = \sup_{\mathrm{supp}\,\pi} u_G - \mathbb E_\pi u_G$. Since $(e^{\lambda x} - 1 - \lambda x)/x^2$ is nondecreasing in $x$, $e^{\lambda X} \leq 1 + \lambda X + X^2 \psi(\lambda b)/b^2$ with $\psi(x) = e^x - 1 - x$; take $\mathbb E_\pi$ and use $\log(1 + y) \leq y$:

$$\mathrm{KL}\big(\pi \,\Vert\, M_{\tau^+}^{(G)}\big) \;=\; \log \mathbb E_\pi e^{\lambda X} \;\leq\; \mathrm{Var}_\pi(u_G)\,\frac{e^{\lambda b} - 1 - \lambda b}{b^2}, \qquad \lambda \geq 0.$$

For a tilt against $u_G$ ($\lambda \lt 0$, a pessimistic tilt) apply the same lemma to $-X$, with $b$ the lower deviation $\mathbb E_\pi u_G - \inf_{\mathrm{supp}\,\pi} u_G$; the reverse divergence $\mathrm{KL}(M \Vert \pi)$ is not covered by this line and keeps the range bound. Exact for every gain, linear in $\mathrm{Var}_\pi(u_G)$, zero when the observation pins $u_G$, reducing to $\tfrac{\lambda^2}{2}\mathrm{Var}_\pi(u_G)$ as $\lambda b \to 0$, and tight (K1: ratio $1.0000$ over 20000 random instances; at $\lambda = 1$ the four segment values are bounded by $0.149$, $0.062$, $0.0071$, $0.00072$). (Bennett 1962 / Boucheron–Lugosi–Massart, from recall; the three lines above are self-contained.) This lets the Epistemic Status say "exact" honestly, about the bound. It also adds content to the domain table: the processor-and-support factor $\psi(\lambda b)/b^2$ depends on the *support* of $\pi$, not its sharpness, and grows exponentially in the gain. At $\lambda = 10$ an observation leaving $0.1\%$ on the desirable state ($\mathrm{sd} = 0.03$) still allows $3.13$ nats (K1). So for a high-gain processor "a test result pins $u_G$" has to mean the residual mass on high-$u_G$ states is *zero*, not small — a sharper and more useful engineering statement than the sd ordering, and one the regression test can see.

## F5 (finding)
- target: segment:deriv-observation-ambiguity-bias-bound
- at: 279b2699

**Fix the $d_{FR}$ convention; then adopt a global Track 2 with constant $2$, derived here; add the Lipschitz factor for downstream functionals (C11, C12, K5).** (a) Define $d_{FR}(p, q) := 2\arccos \int\!\sqrt{pq}$, the Fisher-metric geodesic distance, twice the unit-sphere arc; with that, Step 1's $\tfrac12 d^2$, the constant $\sqrt 2$ and §6 are consistent (as written, (H1)'s "spherical-arc distance" would make the local constant $1/\sqrt 2$). (b) Global bound, no (H4), no compactness: with $\theta = \arccos \mathrm{BC}$, Rényi monotonicity gives $-2\log \mathrm{BC} \leq \mathrm{KL}$, and $\log\cos\theta \leq -\theta^2/2$ on $[0, \pi/2)$ (the second derivative of $\log\cos$ is $-\sec^2 \leq -1$), so $\theta \leq \sqrt{\mathrm{KL}}$ and $d_{FR} \leq 2\sqrt{\mathrm{KL}}$; averaging over $G$ with Jensen, $\mathbb E_G\, d_{FR} \leq 2\sqrt{I(G; M_{\tau^+} \mid e_\tau, M_{\tau^-})}$ (K5: $\theta \leq \sqrt{\mathrm{KL}}$ on 20000 random pairs, ratio up to $1.0000$). This is the constant Paper 3 states and the appendix declined as "unread"; it is now independently derived (by me only — it wants a second mind). It closes Honest failure mode 4 and the matching Working Note, with $\sqrt 2$ as the sharp local constant. Note it bounds the ambient Fisher–Rao distance; a geodesic distance inside a parametric submanifold can be larger, and the goal-marginal mixture is generally outside the family, so the ambient reading is the right one. (c) `:150` and `:128` say any downstream functional of the belief inherits goal-dependence "bounded by $C\sqrt{\kappa H}$": that needs the functional's Lipschitz constant in the ground metric, $\lvert \mathbb E_\nu F - \mathbb E_\mu F\rvert \leq \mathrm{Lip}(F)\, W_1 \leq \mathrm{Lip}(F)\, W_2$, so "bounded by $\mathrm{Lip}(Q_O)\cdot C\sqrt{\kappa H}$," and $Q_O$'s Lipschitz constant in $M$ is not stated anywhere I found. (d) Open question, not a defect: (H2)'s LSI constant on a mixture over goals is itself goal-dependent beyond the $\beta \ll \sigma$ limit.

## F6 (finding)
- target: segment:scope-observation-ambiguity-modulation
- at: 279b2699

**State the retirement's dichotomy in the law where it holds, and say what the retired numerator does measure (C9, K2b, K4).** `:66` and `:84` say $I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$ is "positive exactly when the goal is evidence about the world," demonstrated by N7β; N7β omits the action, and with the action in the event and an injective policy the quantity is $0$ for an informative goal too (K4). What I would land: (i) under the pin and an injective policy the retired quantity is identically zero for *every* agent, which makes the retirement stronger, not weaker; (ii) the "positive exactly when" half holds in the probe law of F3, or for the update that conditions on the observation without the action; (iii) what the numerator measures, exactly: averaged over goals, the per-goal log-score reliability of a goal-blind report $P(\Omega \mid \mathcal I)$ equals $I(G; \Omega \mid \mathcal I)$ when the report is one-to-one in $\mathcal I$ — in K2b both are $0.1855$ nats. So the retired quantity is the size of the (NWI) violation of F1 — how much per-goal reliability a goal-blind filter loses by not using a goal that is evidence. That gives F1's premise a measure, and the retirement a demonstrated why: the quantity was never interpretive latitude; it is the price of ignoring an informative goal, which is zero exactly in the regime where goal-dependence is a defect.

## F7 (finding)
- target: segment:der-directed-separation
- at: 279b2699

**Clause 2's converse is stated unconditionally at `:58` and in `#disc-partial-coupling-pathways`'s allocation row; the verifier's V6 refutes it (C2, C16).** Replace "is allocation in form and distortion in effect: the drop pattern is evidence the update ignores" with "is distortion in effect whenever the dropped content is informative about the world given what was retained, since the drop pattern is then evidence the update ignores (N5); if the dropped content is uninformative the report stays calibrated (the verifier's V6), so Rubin's ignorability is sufficient, not necessary." Same qualifier in the partial-coupling row ("is *distortion* when the drop decision depends on dropped content *that bears on the world*"). The Rubin attribution is still from the bibliographic record, as the verifier noted.

## F8 (finding)
- target: segment:der-orient-cascade
- at: 279b2699

**Step 5a's cost sentence needs the qualifier the abandon sentence has (C13, K6).** Replace "and a pursuing action with a cost paid regardless of feasibility breaks it too (the spike verifier's V5)" with "and a pursuing action with a cost paid regardless of feasibility breaks it when the cost makes a different action optimal under infeasibility than under feasibility (the spike verifier's V5); in general feasibility evidence has positive value iff learning it changes the optimal action with positive probability." K6 is the instance where the tie is broken and the starvation persists.

## F9 (finding)
- target: segment:der-directed-separation
- at: 279b2699

**Residual carriers of "$\kappa$ indexes how good the approximation is," which the landing otherwise retired.** `:22` "Class 2 agents: the sequential cascade is an approximation whose quality depends on the coupling scalar" and `:125` "…whose quality depends on $\kappa_{\text{processing}}$": $\kappa$ saturates at any noiseless coupling (`:98`), so a Class 2 agent with an infinitesimal noiseless coupling reads $\kappa = 1$ while the cascade is essentially exact. Suggested: "whose quality depends on the agent's distortion (the reliability term) and, for goal-dependence of downstream quantities, on the probe-law displacement; $\kappa$ diagnoses where ports exist." `:155` "well-defined" → for the probe-law $\kappa$ (F3). The same carrier sits in `#der-orient-cascade` `:105` ("At $\kappa_{\text{processing}} \gt 0$ the sequential order approximates a simultaneous resolution, with the $\varepsilon(\kappa)$ degradation where derived"): the only $\kappa$-indexed degradation canon now has is the appendix's bound on goal-dependence, so either name it as that or drop the $\varepsilon(\kappa)$. And in `#scope-observation-ambiguity-modulation` `:72`, "the goal-averaged reported posterior should equal the prior" → "under each goal's law, the event-averaged reported posterior should equal the prior," since a goal-symmetric tilt passes the goal-averaged screen.

## Notes for the consolidator

Feedback on the brief: it worked for me — reading cold first was the right suggestion, and two of the four main findings (F2, F4) came from that cold read before I saw any spike text. F1, F3 and F6 sharpened once I read the verifier, because the verifier had already seen pieces of them (its §2 per-goal law, its §5 probe-law remark) and those pieces did not all land. So in this case the blind spot was not where all four agreed. It was in what dropped out between hands: a premise stated once at the top of the spike, and a verifier aside phrased as "a strengthening the spike did not make."

On the integration's framing: the three-quantity picture is right, and I would keep it as the spine. I would add a fourth line to it, because F1 and F6 together say there is a fourth quantity. *Goal informativeness*, $I(G; \Omega \mid \cdot)$, is not about the update at all. It is about where the goals came from, and it decides whether goal-blindness and per-goal calibration can coincide. The retired $\mathcal A$ was measuring that all along.

What would most change a verdict here: a second derivation of F5(b), the F6(iii) identity and the F2 recalibration identity (all mine, all short). The consumers of "$\kappa_{\text{processing}} = 0$" are listed under F3 from a grep and an in-context read; I did not re-derive any of them.

I'm available for follow-ups.
