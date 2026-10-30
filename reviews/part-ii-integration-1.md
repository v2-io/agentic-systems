---
kind: review
author:
  name: Claude Fable 5.1 (Part II integrator)
  role: integrator
sources:
  - spikes/spike-loop-identification-decision-state-2026-10-30/01-derivation.md
  - spikes/spike-loop-identification-decision-state-2026-10-30/de-novo-feedback-1.md
  - spikes/spike-allocation-vs-distortion-coupling-2026-10-30/01-derivation.md
  - spikes/spike-allocation-vs-distortion-coupling-2026-10-30/de-novo-feedback-1.md
  - reviews/b1-part-ii-check-1.md
  - msc/inside-out-2026-10/owner-review/integrator-items.md
written: 2026-10-30
---

# Part II integration: the re-derivations behind what landed

KR **C.2** (C2, C3), **B.1** (Part II records), **C.1** (A4, A5), under the top intent "Complete 'in-place' refactor of ASF — meta, all artifacts, and theory itself." Each check below is a re-derivation I did before writing the sentence it concerns, against the text as it now stands in this worktree (uncommitted at the time of writing; `committed: before`). The spikes' and verifiers' proposals were inputs; where I declined one it is said in the free text. The account for a reader who has not seen the spikes is `msc/inside-out-2026-10/part-ii-integration.md`.

## C1 (check)
- target: segment:der-loop-interventional-access
- act: rederive
- line: derivation
- criterion: Ignorability at the policy's own inputs under mediated access and (P); the coin-retention clause under a shared coin source; the deterministic no-go for an unrestricted environment class; the general $R \perp S \mid Z$ adjustment condition; positivity at $X_t$ (not $Z$) for the on-policy/interventional sufficiency coincidence; consistency as intention-to-treat.
- committed: before
- outcome: confirmed
- recheck: run `python3 -I` on `check-feedback-1-lemma1b-pstream.py` and `check-integration-1-deterministic-nogo.py` in the C2 spike dir; re-derive the $R \perp S \mid Z$ factorization in three lines

Re-derived from the graph: every parent of $a_t$ but $U_t$ is in $X_t$, so $X_t$ blocks every back-door path; with a shared coin source a past action is a collider between coin and environment, so retaining actions alone does not suffice (the verifier's two-step enumeration reproduces). The spike's Proposition 4 as written was ill-formed (it indexed $T$ by the agent's state); the replacement I derived and checked is: in an environment class unrestricted apart from mediated access, two environments — one recording history in $\Omega_t$ — agree on-policy and differ on every untaken action's effect at a visited $X_t$. Exact enumeration in `check-integration-1-deterministic-nogo.py`; the same script shows outcome-sufficiency of the coarsening is exactly what the second environment violates. The verifier's "positivity at some outcome-sufficient set" is therefore stated as a class restriction, untestable on-policy under determinism (Lemma 3's coincidence needs positivity at $X_t$; checked that the proof uses the $X_t$ form). Declined: the spike's "iff" in Proposition 5 (the $R \perp S \mid Z$ condition is strictly more permissive, derived by the verifier and re-derived here); the spike's claim that LLM policies violate (C2) (the goal is a parent of the action). Lettered (C1)–(C3) replaced by the standard names positivity / sequential ignorability / consistency; I checked that canon's (C3) ("executed value read as the intervened value") is the consistency assumption of Hernán & Robins and that #def-value-object's old (C3) ("$M_t$ encodes the mechanism") is a different thing, now stated separately as the by-construction route.

## C2 (check)
- target: segment:def-value-object
- act: rederive
- line: derivation
- criterion: The $G_t$-independence of $Q_O$ as a function is definitional; the contentful true-law claim needs three premises; canon's strategy learner violates the third at $\kappa = 0$; identification at $X_t$ then averaging over $P(G_t \mid M_t)$; the gate is "mechanism by construction, or positivity + ignorability from data"; the right rung of convention monotonicity needs closure of $\Pi$.
- committed: before
- outcome: confirmed
- recheck: re-run `sim-strategy-counts-confound.py` and `check-feedback-1-singular-trajectory.py`; compute the three-state two-policy instance by hand ($A^{\text{RH}} = 100$, $A^{\text{B}} = 10$)

The function $Q_O(M_t, a; \pi_{\text{cont}}, N_h)$ has no $G_t$ argument, so the record's former falsifier ("a disciplined agent whose $Q_O$ varies with $G_t$") could not fire — the B.1 checker's point, confirmed. The true-law claim $\mathbb E[V \mid M_t, G_t, do(a)] = \mathbb E[V \mid M_t, do(a)]$ fails on three separate routes, each checked: the collider at $M_t$ when $\kappa \gt 0$ (`check-feedback-1-kappa-collider.py`), unbounded signaling, and outcome statistics in $\Sigma_t$ read by the policy (the spike's and verifier's simulations, re-run; gaps $+0.09$ to $+0.21$). The spike's resolution (c) — identify at $X_t$, average over $P(G_t \mid M_t)$ — landed; its pointer to the "$0.59$ column" as that average was wrong (the verifier is right that it is the $n_1$-weighted on-policy conditional) and was not landed. The B.1 checker's gate composition ("(C3) by construction, or (C1)+(C2) from data") re-derived and landed; Kalman + LQR moved from the first record (learning-agent scope excludes it) to the second (by construction). The B.1 corrections sub-agent's right-rung counterexample checked by hand and landed with the closure hypothesis in all seven carriers.

## C3 (check)
- target: segment:der-directed-separation
- act: rederive
- line: derivation
- criterion: The observation is a collider of goal and world when the action depends on the goal, so an action-free goal-blind update is per-goal miscalibrated (V7); calibration iff conditional-law-given-some-sub-$\sigma$-field (tower property); distortion strictly increases reliability under every strictly proper score under the agent's model, and under the world's law only when well-specified (N4); $\kappa$ is positive for allocation and saturates for noiseless couplings (N2, N8, N9); the stochastic-$f_M$ proviso on the factorization; the A4 rows against the Bar-Shalom–Tse and Derpich–Yüksel abstracts.
- committed: before
- outcome: confirmed
- recheck: V7 by hand (pooled $P(\Omega = 1 \mid e = 0) = 0.2$; per-goal truth $0$ and $1$); `sims/check.py` N2, N4, N8, N9; abstracts in `ref/Prior_art_for_AAT_directed_separation.md` :217–221 and :508–511

V7 recomputed by hand; the collider is real and canon's event stream already includes action completions (#form-event-driven-dynamics :25), so the landing is a pin (the event includes the action; it enters only through the likelihood), not a new argument. Declined, with the verifier: the spike's L0 (adding $a_t$ to the conditional independence) — vacuous under injective policies and it zeroes $\kappa$'s denominator; the spike's claim that the verbal classification and $\kappa$ disagree because $\kappa$ is boundary-invariant — canon's `:56` did not pin $e_\tau$, so the pin is part of the landing. The calibration criterion, the resolution/reliability split, Prop A′ as sufficiency (the verifier's V6 breaks the "iff"), the access condition, the three benign sources of positive $\kappa$, strategically chosen ignorance as a third case (V2), and the certificate's efference-copy condition all landed. The degradation norm's "less coupling tracks reality strictly better" is now stated as true of distortion (reliability term) and silent on allocation; the B.1 record R4 rewritten accordingly, R1 given the shared-PRNG proviso, R2's falsifier scoped to the magnitude claim, R3's exemplar replaced. A4: both abstracts read; the dual effect is the control's effect on state uncertainty (selection), and Derpich–Yüksel's abstract states the counterexample to CE $\Rightarrow$ NDE; the two rows rewritten. The 1974 full text remains unread by anyone.

## C4 (check)
- target: segment:scope-observation-ambiguity-modulation
- act: rederive
- line: derivation
- criterion: $I(G; \Omega_\tau \mid e_\tau, M_{\tau^-}, a_\tau) = 0$ under $G \perp \Omega_\tau \mid (M_{\tau^-}, a_\tau)$ and positive exactly when the goal is evidence (N7α, N7β); the Jensen-gap identity and both Hoeffding directions for any mutually absolutely continuous pair; the model-free bound does not deliver sharpness dependence; the fixed-gain cumulant expansion does, and a gain scaling with $1/\mathrm{sd}$ defeats it.
- committed: before
- outcome: confirmed
- recheck: `sims/check.py` N1, N7, N12; the four KL values at $\lambda = 1$, $u = (0,1)$ by hand; $\mathrm{KL}((0.99, 0.01) \Vert (0.5, 0.5)) = 0.637$ nats

The identity is universal (any $M^+ \ll\gg \pi$ is a multiplicative reweighting), so the spike's "model class" scope was not a restriction — the verifier's §5, re-derived. The verifier's own first suggestion (land the universal form as settling "sharp observations leave no room") was corrected by the verifier on main (aa7f2423) before I landed; I checked the correction by computing the four KL values and the $0.637$ example and agree: the universal bound is in the size of the reweighting, and sharpness dependence is exactly the fixed-gain hypothesis. Landed accordingly: identity and range bounds exact; the fixed-gain tilt as a hypothesis with the regression test; the domain table conditional on it; $\mathcal A$ and $\kappa \cdot \mathcal A$ deleted, with the zero demonstrated in Discussion (integration is replacement); the $\hat{\mathcal A}$ estimator retired (it measures the interpreter's goal-dependence; the segment's own `:77` caveat conceded this). Also recorded the identifiability of $(\lambda, u_G)$ only up to the product, and that $\pi$ is the posterior given the agent's *allocated* information, so the law is not estimable from goal-probing alone.

## C5 (check)
- target: segment:deriv-observation-ambiguity-bias-bound
- act: rederive
- line: derivation
- criterion: The chain rule on the post-update law gives $I(G; M_{\tau^+} \mid e, M^-)$; Otto–Villani applied with the goal-marginal post-update law as reference needs LSI on that law and no pushforward step; $I = \kappa_{\text{processing}} H(G \mid e, M^-)$ by the definition of $\kappa$; the two-goal Gaussian example is tight to first order in both tracks; the former Step 4 introduced $\kappa$ by assertion and the former chain rule related true laws to the agent's belief.
- committed: before
- outcome: confirmed
- recheck: Paper 3 `03-setup.md` :1–31 and `04-main-results.md` :55–78 (read); the two-goal example: $\mathrm{JSD} \approx \beta^2 / (2\sigma^2)$, $\sqrt{2I} = \beta/\sigma$, actual arc $\approx \beta/\sigma$; $W_2^2(N(\pm\beta,\sigma^2), N(0,\sigma^2)) = \beta^2$

Read Paper 3's setup and main results as both verifiers and the advisor asked; its bias quantity and chain-rule lemma are the present form, re-derived here rather than transcribed. The old Track 1 had a Lipschitz-pushforward step from world-state to belief; with the chain rule on the post-update law both compared laws are laws of the belief and the step disappears, so (H3) is gone and (H2) moves to the goal-marginal post-update law. Track 2's identity $\mathrm{KL} \approx \tfrac12 d_{FR}^2$ holds for any nearby densities on the same space, so it applies to the two post-update laws directly. The κ factor is now an identity, not a hypothesis; I recorded that it saturates for noiseless couplings (Prop 3.3) and that the bound is about goal-dependence, not distortion, in the Epistemic Status. The old §6 Gaussian example set the *true* goal-conditional law to the agent's shifted belief; replaced by the two-goal symmetric example, checked by hand to first order. Paper 3's global $C = 2$ and its architectural corollary are not adopted (the corollary's denominator is the retired quantity; its Class 1 CI excludes the goal-as-evidence Bayesian — the C3 verifier's V4, recomputed: $I(G; M^+ \mid \Omega, e) = H(G \mid \Omega, e) \gt 0$).

## C6 (check)
- target: segment:der-orient-cascade
- act: rederive
- line: derivation
- criterion: A VOI-optimal allocator at fixed capacity never encodes a feature whose only payoff effect is to make every action in its decision set tie under infeasibility; the hypothesis is the tie, not the absence of a revise option (N10: revise present but never optimal, VOI still $0$; V5: pursue-only set with an always-paid cost, VOI $0.06 \gt 0$); the 4c trigger's residual is identically zero under on-policy short-circuit execution (#der-causal-insufficiency-detection); the "forced" carriers in Epistemic Status, Working Notes, OUTLINE and format.sop.
- committed: before
- outcome: confirmed
- recheck: `sims/check.py` N6, N10; V5 by hand ($\mathrm{VOI} = 0.06$ at $P(\text{feasible}) = 0.6$); grep "forced by information" across `01-aat-core/`, `doc/sop/`

The spike's and README's "iff the decision set lacks the revise option" is false both ways (the spike's own N10 one way, the verifier's V5 the other); landed as the tie hypothesis with the remedies as design claims and the test named. The B.1 checker's C16 carriers drained (two sentences in Epistemic Status, the convention paragraph, the Working Note, the OUTLINE row, the impl heading, `format.sop.md` :558); the 4c precondition added.

## C7 (check)
- target: segment:def-model-sufficiency
- act: rederive
- line: derivation
- criterion: The two-bit echo agent has $S(M_t) = 1$ with the one-step model insufficient by one bit; the comparison class for identification is $X_t$, not $\mathcal C_t$; the on-policy sufficiency test coincides with the interventional one only under positivity at $X_t$, so determinism is where $S$ says least.
- committed: before
- outcome: confirmed
- recheck: the echo example by hand (numerator $0$, denominator $1$ bit)

Checked by hand. Declined: the spike's clause that the echo agent's $M_t$-conditioned effect estimates are confounded (the example gives $a_t$ no mechanism, so there is no contrast to confound — the verifier's point) and the spike's redefinition of the formula with $do(a_{t:\infty})$ (underspecified: a mutual information "given do" needs a distribution or supremum over sequences). The formula is left as is; the Discussion now says it reads the actions as realized and names the open-loop reading the causal use needs; the question is in `vsect open`.

## C8 (check)
- target: segment:der-causal-hierarchy-requirement
- act: read-check
- line: derivation
- criterion: The "generic for any agent with internal state" sentence; the RL bullet's reason (stationarity, not the policy's signature); the Hafez figures at abstract granularity.
- committed: before
- outcome: confirmed
- recheck: arXiv 2603.01283 abstract (the B.1 checker read it; I did not re-fetch): 89.3% of coupling degradations vs 44.0%, 21 continuous-control agents

Both sentences corrected per C1's result (conditioning on the decision state blocks the selection; a learning agent's policy reads its value table, and stationarity is what makes that harmless). Hafez wording changed from "detects perturbations at 89% accuracy" to the abstract's "detects 89.3% of coupling degradations" in this segment and #impl-causal-access in `af518dd5`, and — after the completion check found the first pass had not reached them — in #der-directed-separation (two sites; the third is a quoted auditor line), #deriv-update-detection-latency, #der-agent-opacity and #der-architecture-noidentifiability (which had attributed the IDT paper to the "Mathematical Theory" authors) in the follow-up commit; the Working-Note verification item removed as resolved at abstract granularity. Not re-fetched by me; the checker's reading is what the body now reports.

## F1 (finding)
- target: segment:hyp-substrate-transfer-asymmetry

`04-eli-core/src/hyp-substrate-transfer-asymmetry.md` :79 and :95 restate the retired product law ("different $\kappa$ values per substrate, different $\mathcal A$"; "asymmetric $\kappa \cdot \mathcal A$ on the same decompression"). The ambiguity factor $\mathcal A$ and the product are retired by #scope-observation-ambiguity-modulation (the factor measured the goal's evidential value about the world); the quantities that replace them are the goal-dependence displacement bound (in $\kappa H(G \mid e, M^-)$) and the distortion bound (gain times residual spread, under the fixed-gain hypothesis). Left to the Volume 4 round-2 integrator, who holds the file; whichever branch merges second should re-word the two sites.

## F2 (finding)
- target: segment:der-class-coercion-via-wrapping

The W₁ selection-channel term $\kappa_{W_1}^{\text{sel}}$ mixes calibration-preserving query selection with cue-triggered distortion by the component, and (C3) as formalized is satisfied by a fixed function of $q_M$ that decodes goal cues and tilts; the condition the wrapping theorems lack is calibration of the component's answer given the query. Landed as a Discussion paragraph (this segment); the structural bound is now described as a bound on goal information reaching $M_W$, not on $M_W$'s reliability. Whether Theorem 2's KL-leakage weakening can be restated as a calibration condition is open.

## F3 (finding)
- target: segment:obs-growth-vs-drift

`04-eli-core/src/obs-growth-vs-drift.md` :50 carries the old Hafez wording ("89%" perturbation-detection framing). The abstract of Hafez, Reid & Nazeri 2026 (arXiv 2603.01283) reports 89.3% of coupling degradations detected against 44.0% for reward-based monitoring, across 21 trained continuous-control agents; the body's "accuracy" and "perturbations" are not the paper's words. Left to the Volume 4 lane.
