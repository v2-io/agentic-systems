**KR3.1 (feeds KR3.3)** — objectives tree at `~/src/arch/asf/msc/inside-out-2026-10/INTENT.md`.

# Influx map — NeurIPS region (`~/src/neurips/`, `~/src/neurips-reviews-responses/`)

*Scout: Claude Opus 5.5, 2026-10-30. Region 5 of the drive-wide influx scout. Read-only pass; nothing outside this directory was written. Reviewer text is paraphrased, never quoted, because the venue reviews are confidential material and the umbrella repo deliberately keeps them untracked.*

## 0. What matters most (read this if nothing else)

1. **August's work went further than May's, and it has never touched ASF.** Between 2026-07-29 and 2026-08-03 the review-response cycle produced a verified layer of new mathematics: nine umbrella spikes, a three-layer verification cascade, per-paper `adjudicated/` claim trees, and a two-document "rhythm of survival" theory. Its own backport queue (`~/src/neurips/adjudicated-common/asf-backport-queue.md`) says *"None landed in ASF canon yet"*. I confirmed that is still true: the pickaxe search of all asf history since 2026-07-28 for the distinctive terms (decoy capture, convexity gap, rhythm of survival, Pukelsheim, Athans, $\Gamma_{\min}$, $D_{1/2}$, arccos form, corridor) returns nothing, and queue item 1 (the "iff" in `#deriv-causal-ib-lmi`) is still in the canon body at line 59.
2. **Part of it contradicts canon, so integration means replacing text, not appending it.** Canon `#deriv-causal-ib-lmi` frames its result as *scalar vs. matrix*: "the matrix Lagrangian distinguishes by direction, not just by magnitude". Its empirical signature says a scalar-Lagrangian agent succumbs to blank-wall traps. The August work, verified three times by the chain, shows that axis is the wrong one. The Paper-01 bonus $\mathrm{Tr}(\Lambda\,\mathcal I_o(a))$ with $\Lambda = c(P_t)\,\mathcal I_{\min}$ picks the same argmax as a fixed linear scalar. At $k=1$ drifting axis, a state-independent drift-projected scalar provably suffices. At $k \geq 2$, *no state-independent rule of any kind* (scalar or matrix, linear or not) survives every LMI-satisfiable configuration. State-dependent scalars are never insufficient. And about 1.8% of LMI-satisfiable configurations admit no surviving schedule at all. The honest boundary is state-independence, and the LMI is a *certificate*, not a behavioral necessity.
3. **The rhythm-of-survival layer is a new, coherent piece of AAT theory, with nothing like it in canon.** It covers per-axis information "rents", survival as rhythm rather than ranking, a corridor law, granularity and breadth replacing the buffer intuition, affordance ("who holds the record"), jump-to-drift reduction, an invariance map under un-narrowing, and a testable hypothesis that logogenic agents survive because their environment keeps the beat for them. Joseph co-developed it in dialog on 2026-08-01/02.
4. **One sentence from the 2026-08-03 revision outline says what AAT claims about agents more plainly than canon does.** *"agency is a narrowing of adaptation, not a departure from it"*. Every agent contains an adaptive tracking core, and its results inherit by containment. And "higher agency adds drifting axes … faster than it adds attention". This is O1 material as much as O3.
5. **Canon has two incompatible definitions of $\kappa_{\text{processing}}$ and two scaling laws.** Paper 3 and its reviewers exposed this. Details in §2.D. It is the one place where a reader of canon alone would be actively misled.
6. **Canon cites the unpublished NeurIPS papers in segment bodies.** The clearest case is the $\mathcal A_{\text{decay}}$ structural-class theorem, cited three times in `#deriv-strategic-persistence-hard-ceiling` (Discussion, Impact, Related Work) but never landed. Under the ratified D-1 rule (canon cites only canon and the published world) that is an integration debt. Nothing on disk records the NeurIPS decision (`~/src/ops/papers/SUBMISSIONS.md` was last updated 2026-08-02 and still lists all three as awaiting mid-September decisions). Paper 02's AC pre-signalled rejection, and its rebuttal meta carried a withdrawal preview.
7. **The reviews are an outside de novo audit, and one of them independently states Joseph's terminology complaint.** Reviewer zGVL (Paper 03, 2026-06-25) listed ASF house vocabulary as an obstacle to understanding: "operational shape", "empirical referent", "cascade", "load-bearing", "coupled-architecture", "goal-coupling-induced displacement". Paraphrased: they could parse perhaps five sentences of the paper. Every one of the three meta-reviews names accessibility.

## 1. The places, with freshness

| Place | Git state | Freshest content (mtime) | Notes |
|---|---|---|---|
| `~/src/neurips/` (umbrella, public, `v2-io/neurips`) | 129 commits; last `339fd7d` 2026-08-02 19:59 | `ac-guidelines.md` untracked, 2026-08-02 20:56; `.practica` 2026-10-27 | Umbrella spikes and rhythm docs are all committed. |
| `~/src/neurips/0{1,2,3}-*/` (three paper subrepos, public) | last commits all 2026-07-29 22:43 | **`adjudicated/` trees untracked in all three** (2026-08-02 19:49–19:57; Paper 01 `REVISION-OUTLINE.md` 2026-08-03 14:21); `response-prep/ISSUES.md` + `response-prep/math/*` modified (2026-08-01 21:32) | The parent commit `339fd7d` *says* "adjudicated/ package trees landed", but they sit uncommitted inside the subrepos. They exist only on this disk. |
| `~/src/neurips-reviews-responses/` (symlinked as `neurips/reviews`, gitignored from the public umbrella) | 5 commits, 2026-08-02 → `b12aff6` 2026-08-03 18:58 | 10 dirty: Paper 03 final rebuttals (5 untracked `final-rebuttal-*.md`, 3 modified), Paper 01 `followup-gHwS-drift-knowledge.md` untracked, **2026-08-03 23:35** (newest file in the region) | Holds `reviews.md` ×3, `asf-recon/` (2026-08-01), the 9,825-line dialog transcript `2026-08-02-164627-earlier-dialog-fable.txt`. |
| asf-side record of the May work | `spikes/neurips-back-integration-2026-05-08.md` (mtime 2026-07-16); Phase A commits `b2440d3d`, `61d53ea0` (2026-05-12) | — | The May map of Paper → segment correspondences. Its Phase B ("substantive segment-level absorption") was never run as a pass. The status of each item is in §3. |

*Stale inherited pointer:* the brief's `~/src/ops/PAPERS.md` does not exist. Per-paper records now live at `~/src/ops/papers/submitted/{tragedy-confident,rl-convergence,hallucination-bound}.md` (2026-07-09). That is region 6's territory.

**Checks I ran, so the "in canon?" column can be weighed.** I grepped all four `*/src/` trees, the five OUTLINEs and `FINDINGS.md` for distinctive terms. For each hit in a key segment I located it relative to `## Working Notes`: a pointer in the Working Notes is not absorption. I ran `git log --all -S` over asf history since 2026-07-28 for August terms, and read the full commit bodies of the umbrella repo. I read the relevant canon passages directly: `#deriv-causal-ib-lmi` (whole), `#deriv-causal-ib-exploration`, `#deriv-observation-ambiguity-bias-bound` §3–§4 and failure modes, `#der-loop-interventional-access` (C1)–(C3), `#deriv-strategic-persistence-hard-ceiling`, and the $\kappa$ definitions in `#der-directed-separation`, `#scope-channel-collapse` and `#scope-observation-ambiguity-modulation`. I did **not** re-run any numerics or re-derive any proof. Rungs below are the source chain's own tags, and I say so where it matters.

## 2. The material, item by item

Each item carries: where · kind · dates · in canon? (how checked, confidence) · what it would change in canon · arguments for setting it aside.

### A. Paper 01 boundary theorems: the scalar/matrix question re-cut (2026-07-29 → 08-03)

- **Where.** Spike `~/src/neurips/spikes/scalar-vs-matrix-survival/report.md` (346 lines, 2026-07-29 23:30) plus `num/exp1`–`exp7`, `redteam/redteam_checks.py` (2026-08-01), and five prior-art neighborhood files (sensor scheduling, index policies, design of excitation, viability reduction). Verification: `~/src/neurips-reviews-responses/neurips-2026/asf-recon/paper-01-asf-recon.md` + `paper-01-redteam.md` + `TRUTHIFIED.md` (2026-08-01 21:16–21:32). Claim segments: `~/src/neurips/01-tragedy-confident-agent/adjudicated/claims/` (12 files, 2026-08-02, untracked). Do-not-use list: `adjudicated/residue.md`.
- **Kind.** New derivations, no-gos and a critique of canon. Rungs as tagged by the chain:
  - $S_0$ (state-independent score) $\equiv$ constant action under a state-independent tie-break [PROVED].
  - $k=1$: a drift-projected scalar suffices under (S1)–(S5) [PROVED].
  - The $\Lambda$-bonus is argmax-equivalent to $\mathrm{Tr}(\mathcal I_{\min}\mathcal I_o(a))$ [PROVED].
  - The $k\geq 2$ state-independence no-go [PROVED + TESTED 3×].
  - State-dependent ($S_2$) rules are never insufficient, via feedback selection on the viability kernel [PROVED; Athans/Bertsekas attribution unverified by the chain].
  - Decoy capture defeats $-\lambda_{\max}(P^+)$; $-\log\det P^+ \equiv$ one-step information gain (Prop 10) and has explicit counterexamples [TESTED/PROVED].
  - LMI-satisfiable $\supsetneq$ survivable, $418/22{,}946 \approx 1.82\%$ [TESTED 3×; DFS negative rigorous; ensemble-robustness of the percentage flagged open].
  - The normalized-$\lambda_{\min}$ gate discriminates at perfect isotropy *only with* $\mathcal I_{\min} \succ 0$ (singular floors misclassify 29%) [PROVED + TESTED].
  - Depth-$d$ lookahead must reach $m$ drifting axes [TESTED, kill direction only; do not state as "iff"].
  - A process caution the chain flagged: the report's $m=6$ row is not reproducible from the scripts on disk.
- **In canon?** **No**, with high confidence. `#deriv-causal-ib-lmi` has none of it. Its body still makes the claims this material cuts against: line 19 ("complementary slackness … zeros out the bonus for blank-wall actions"), line 89 (bold: "distinguishes by direction, not just by magnitude"), the line 132 empirical signature (scalar agent succumbs), line 59 ("if and only if"). Its Working Note (line 168) still repeats the May framing that directional discrimination "rests on anisotropic drift", which the isotropy gate result removes.
- **What it would change.** A rewrite of `#deriv-causal-ib-lmi`, per integration-is-replacement:
  - The "iff" becomes "if". The paper's necessity analysis and the convexity gap show necessity fails in general, and rate-feasibility is not schedulability.
  - The scalar-vs-matrix headline is replaced by the state-independence boundary, with the LMI positioned as a certificate.
  - The decoy-capture mechanism is added beside the blank wall. It is distinct: it has the right directions at a sub-floor rate.
  - The anisotropy caveat is replaced by the gate result under $\mathcal I_{\min} \succ 0$.
  - The empirical-signature paragraph is restated as "direction-aware vs. direction-blind weighting at $k=1$", plus the $n \geq 3$, $k=2$ discriminating experiment, which is fully specified in the spike's §9.
  - The scalar-reduction paragraph's "properly subsumes" survives, but the claim that the matrix lift is *needed* does not.
  - Knock-on: `#deriv-causal-ib-exploration`, `#impl-orient-cascade` and `#causal-access-intro` all invoke the blank wall and should be re-read. The canon Findings Brief for the LMI also promises the wrong thing ("This result fixes the math by making the argument directional").
- **Set-aside arguments.** None for the core: it is verified and it corrects canon. The external attributions (Pukelsheim 1987, Athans 1972, Bertsekas 1972, Dance–Silander) were opened only by a July recon peer, never by the verification chain. An integrator should open them first-hand or carry the attribution as unverified. The red-team refuted one formulation, "no linear scalar of any weighting suffices at $k\geq2$" (`Tr(diag(P_t) I_o)` survives), so that sentence must not enter canon (`residue.md`).

### B. The rhythm-of-survival theory layer (2026-08-01 → 08-02)

- **Where.** `~/src/neurips/rhythm-of-survival-theory.md` (89 lines, technical, with epistemic tags on every claim), `rhythm-of-survival-notes.md` (67 lines, plain-language, Joseph + Claude dialog), and `rhythm-of-survival-implications-draft.md`, relocated to `01-tragedy-confident-agent/adjudicated/discussion/implications-driver-and-applications.md`. The spikes feeding it, all under `~/src/neurips/spikes/`: `buffer-interpolation/` (2026-08-02 03:02), `bresenham-curved-canvas/` (04:12), `jump-drift-unification/` (02:50), `corrected-world-agency/` (report 18:06; Sonnet audit `audit-sonnet.md` 18:39; fallible-alert follow-up `num/audit_followup_fallible_alerts.*`). The source dialog is lines ~760–960 onward of `~/src/neurips-reviews-responses/neurips-2026/2026-08-02-164627-earlier-dialog-fable.txt`.
- **Kind.** A mix that an integrator should keep separate:
  - **Exact or verified.** *Rent*: the per-axis floor $\iota_{\min} = q/(R^2(R^2+q))$ in the filtered convention, read as "the supply whose equilibrium sits at tolerance"; the predicted convention $q/(R^2(R^2-q))$ is a known hazard that bit twice. *Corridor law*: pathwise duty $d = \beta + (1-\beta)u$ with $\beta = q/(R^2+q)$, so no information rate buys out return time [PROVED]. *Jump-to-drift reduction*: in the linear-Gaussian model a rare-jump component is exactly extra drift, $q_{\text{eff}} = q + \lambda_J Q_J$ [exact]. *Absorption precision* $\iota_{\text{abs}} = 1/R^2$: a jump-prone axis charges an *amplitude* as well as a rate, and every rent is capped by $1/R^2$ [exact]. *Missed jumps*: these are an **observability** statement (incremental vs. absolute observation operator), not an information statement [exact, elementary]. *Restart vs. persistence*: the contrast is invisible to every linear filter [characterized numerically]. *Forecast collapse*: under known scalar dynamics, forecast ranking $\equiv$ tracking ranking, with per-axis rescaled tolerances in multi-axis form [PROVED, audit-corrected].
  - **Tested on one family or ensemble.** *Granularity*: sub-stepping the control clock closes the convexity gap for 83/83 truly rate-feasible configurations, and splits off a "discrete-bonus-only" class. *Breadth beats depth*: under re-purchasable capture and known laws, the survivable set is identical at every buffer length. *Pinwheel* is a one-way embedding. *Threshold rules* break at 4 axes ($T=(2,4,8,8)$).
  - **Framing and theory claims.** "Survival under drift is a rhythm, not a ranking": a rate is a fact about a trajectory, no instantaneous rule can enforce it, and $P_t$ is the per-axis "it's been a while" counter. *Affordance*: $q$ as record-decay rate; instrumentation as floor-lowering by buffer manufacture; safety channels sized against the worst-case allocation (per-action) rather than the average. *Invariance map*: un-narrowing the sterile world object by object, with the audited two-axis form "purchasability-now" and "map-known" replacing the over-unified H1–H4. *Certificate-can-lie*: believed rents below true rents kill through a valid-looking check; the error is asymmetric.
  - **Hypotheses.** Joseph's *environment-as-metronome* hypothesis: logogenic agents get away with almost no native rhythm because the chat loop keeps time for them. It predicts LLM-agent failures concentrate on continuous axes (stale facts, calibration, memory hygiene), and the counter-move is per-axis staleness counters with threshold refresh. The draft promotes it as a named testable claim. Joseph's live-stream/codec instance includes the claim that efficient encoding manufactures the irreducibility: conditional symbols are worthless to a desynced receiver, so the nonconvexity survives at zero switch cost.
- **In canon?** **No**, with high confidence. "rhythm" appears in canon only as an incidental word in two Working Notes. There are no hits for corridor, pinwheel, viability-kernel-in-this-sense, Bresenham or invariance map. The pickaxe search since July is empty.
- **What it would change.** This is where canon would grow, not be edited. The closest homes: `#result-persistence-condition` and `#result-per-dimension-persistence` (rents as the per-axis floor; equilibrium reading); `#deriv-causal-ib-lmi` (the policy-class ladder and the certificate reading); `#form-event-driven-dynamics` and `#deriv-update-detection-latency` (jumps, absorption amplitude, observability, event layers; the theory doc itself says to read the detection-latency segment first because it "may already be half of this"); `#def-adaptive-tempo`; and the 03-llm-core logogenic segments (`#impl-closed-loop-interiority`, `#der-logogenic-as-wrapping`) for the metronome hypothesis. The invariance-map method ("scope cascade run in reverse") is offered as a reusable canon pattern; it may belong beside the constructive-impossibility posture meta-segment.
- **Set-aside arguments.** Everything here lives in the diagonal linear-Gaussian "covariance game" with known laws. That scope is narrow, and an integrator must keep it explicit, not let the rhythm language travel unscoped. The non-commuting regime is open. Several numbers are one-geometry (the $\approx 6.5\times$ pathwise margin) or one-ensemble (1.82%), and their sources say not to quote them as portable. The Bresenham material was never digested into claim segments; the waterfall marks it [NEEDS-COORD], and Joseph called it "a mental-model stab" that can flow in later as discussion-level. The jump-drift spike *refuted* its own brief's J1 framing: the asymmetry does not "fall out of the same recursion". Any canon text must use the corrected form.

### C. "Agency is a narrowing of adaptation": the containment framing (2026-08-03)

- **Where.** `~/src/neurips/01-tragedy-confident-agent/adjudicated/REVISION-OUTLINE.md` (67 lines, 2026-08-03 14:21, untracked), opening "identity sentence" and §1.3. A sibling statement is in `~/src/neurips-reviews-responses/neurips-2026/01-tragedy-confident-agent/POST-READY/followup-gHwS-drift-knowledge.md` (2026-08-03 23:35, untracked, apparently written in Joseph's voice). It argues that known drift is the *favorable* case, so the impossibility results hold a fortiori without that knowledge, and unknown drift adds cost only on the constructive side. It also says estimation needs the same per-direction attention the certificate prices: "you can only detect drift on axes you glance at".
- **Kind.** A sharper statement of what the theory claims, plus a structural argument for why Part I results bind every agent.
- **In canon?** The *set inclusion* exists (agency scope ⊂ adaptive-system scope), and the outline says containment was "verified against AAT's scope definitions". The *sentence* and the *upward-inheritance claim* are not in canon: no hits for "narrowing of adaptation" or "tracking core". The claim that higher agency adds drifting axes (own calibration, goal relevance, models of others) faster than it adds attention is a theory claim, and I found no canon home for it. Medium-high confidence.
- **What it would change.** O1 framing: the introduction or OUTLINE preamble of 01-aat-core, `#scope-agency`, and possibly a discussion-grade segment for "the tragedy inherits upward with increasing force". The a-fortiori argument about unknown drift belongs in `#deriv-causal-ib-lmi` and `#deriv-causal-ib-exploration` Discussion.
- **Set-aside arguments.** The "increasing force" claim is asserted, not derived. Canon would need it at hypothesis or discussion tier.

### D. Paper 03 complex: the bias bound's large-information regime, and the $\kappa$ mismatch

- **Where.**
  - May: `~/src/neurips/03-llm-hallucinate-bound/src/re/` (12 files) and spikes `A6-extend-lemma-to-ssm-linear-attn/`, `A7-stuart-school-mapping/`, `A8-stuart-school-step1-gap/`, `O1-tighter-track2-constants/` (2026-05-06/07).
  - August: umbrella spikes `information-bound-saturation/report.md` (2026-07-29, Chernoff note corrected 2026-08-02) and `rate-reading-chernoff/report.md` (2026-08-02 18:37).
  - Claims: `03-llm-hallucinate-bound/adjudicated/claims/{vacuity-and-arccos,unconditional-saturation-nogo,sharpness-two-witnesses,d12-theorem-package,jsd-protocol-and-prediction}.md` and `residue.md` (untracked).
- **Kind.**
  - *Global bound and saturation no-go* [PROVED]. The global Track-2 bound is $\mathbb E\, d_{FR} \leq 2\arccos(e^{-I/2}) \leq \min(2\sqrt I, \pi)$, already in the paper's App D. **Every** bound $\mathbb E\, d_{FR} \leq F(I)$ must approach the diameter $\pi$: the partition witness attains $2\arccos(N^{-1/2})$ exactly at $I = \log N$, and a perturbed partition extends this to all real $I$. Together with the chart-rescaling no-go this forms a pincer: bounded invariant metrics saturate, and unbounded chart metrics admit no universal constant.
  - *$D_{1/2}$ Theorem A* [PROVED]. $\mathbb E_G[D_{1/2}(P_{M\mid G}\Vert P_M)] \leq I$, with equality on the partition family. It is unbounded in $I$, so it is the coordinate that stays informative in the adversarial regime, and it survives the $\kappa\times\mathcal A$ substitution.
  - *Refuted gloss* (residue). "$I/2$ caps the goal-identification exponent" is false; the partition family identifies perfectly at finite $I$.
  - *May O1*. Under (PI) alone the global constant is $2$, not $\pi/\sqrt2$; $\sqrt2$ is only local. A6: the attention-coupling lemma extends to linear attention, Mamba, RWKV, RetNet and long convolutions through a causally-aggregated-mixer abstraction. A7/A8: Stuart-school machinery embeds into Track 1's hypothesis space as the Class-1 specialization, qualitatively, with a constant overhead of at least $2$; A8 corrects A7's constant claim.
  - The JSD instantiation protocol and advance prediction (hypothesis): adversarial prompts will often exceed about 2.5 nats.
- **In canon?** **Partly**, checked against `#deriv-observation-ambiguity-bias-bound`:
  - Canon carries Track 2 as $\sqrt2\sqrt{\kappa I}(1+o(1))$ under (H4) small-information. Its own failure mode 4 (body, line 199) says a global Fisher–Rao statement is still needed. The arccos form and the saturation no-go **answer that open item** and are not in canon.
  - Canon's §4 "Implication" sentence says, unhedged, "under (PI), Fisher-Rao is the canonical norm and $C=\sqrt2$ is universal". Per O1 that overstates: $\sqrt2$ is the local constant and $2$ the global one.
  - Canon §4 does contain a chart-rescaling counterexample (the $\sigma$-parameterization), so the May map's "chart-rescaling no-go" item is partly landed. The F4 entry in `#disc-identifiability-floor` is not.
  - (R)/(K) axioms, (H4'), JSD: pointer-only in Working Notes.
  - A6 architecture coverage: pointer-only (`#scope-channel-collapse` WN line 83).
  - Stuart reduction: canon cites Stuart 2010 for Track 1 but carries neither the reduction nor A8's overhead correction.
- **The $\kappa$ mismatch** (verified by reading definitions; consequences not worked through):
  - Canon's master definition (`#der-directed-separation` line 85, reused in `#scope-channel-collapse` line 31) is $\kappa_{\text{processing}} = I(G;M_{\tau^+}\mid e,M_{\tau^-})/H(G\mid e,M_{\tau^-}) \in [0,1]$, asserted $\approx 1$ for transformers.
  - Paper 3 (`src/re/03-setup.md:29`) defines $\kappa_{\text{processing}} = I(G;M_{\tau^+}\mid\cdot)/I(G;\Omega_\tau\mid\cdot)$. Under that definition the factorization $\sqrt{\kappa\, I(G;\Omega)}$ is exact by substitution, and the parrot witness gives $\kappa=\infty$ for a Coupled architecture.
  - Canon also disagrees with itself on scaling. `#scope-observation-ambiguity-modulation` (lines 43 and 113) states the bias law as *linear*, $C\kappa I$, and claims novelty on that product form. The appendix it cites as its backing (`#deriv-observation-ambiguity-bias-bound`) derives $\sqrt{\kappa I}$.
  - So three segments carry two definitions and two scalings. With canon's $H(G)$ normalization, I do not think $\sqrt{\kappa\, I(G;\Omega)}$ follows, but I have not worked it through; an integrator should.
  - Reviewer RxU2's critique bears directly on this. Paraphrased: the chain-rule lemma is just the definition of conditional mutual information, so the bound relates two measures of the same quantity. The architecture-dependent factor is the only non-tautological content, and for transformers it is neither bounded nor estimated. On canon's definition it is simply asserted to be $\approx 1$.
- **What it would change.**
  - `#deriv-observation-ambiguity-bias-bound`: add the global arccos bound and the saturation no-go (closing failure mode 4); correct the "$\sqrt2$ universal" sentence to local $\sqrt2$ / global $2$; add Theorem A as the adversarial-regime coordinate; add the Stuart reduction with A8's overhead.
  - `#disc-identifiability-floor`: the F4 instance.
  - `#scope-channel-collapse` / `#der-directed-separation`: the architecture-family lemma.
  - One $\kappa$ definition across all segments, and one scaling law in `#scope-observation-ambiguity-modulation`.
  - A canon statement, in 03-llm-core, that the displacement bounds carry no information exactly in the jailbreak/persona regime the logogenic story cares about, with Theorem A as what survives there.
- **Set-aside arguments.** The JSD prediction is a belief, and the residue says to keep it separate. The binary-goal JSD protocol has $I \leq \log 2$, so it cannot reach the vacuity regime. The chain's residue also says that canon's $\hat\kappa$ estimator (distance-average vs. MI-ratio) has no consistency argument, so do not lean on it as an empirical avenue.

### E. Paper 02 complex: regret/TV conversions and the composition theorem

- **Where.**
  - May: `~/src/neurips/02-unified-convergence-rl/src/re/` (13 files) and archived spikes `_archive/spikes/{H1-forgetting-scaling,H2-bias-clipping,H4-bt-definition,H5-a1-base-learners,M2-loop-level2-proof,VT-unification}/report.md` (2026-05-06/07); prior-art `prior-art/{report,positioning}.md`.
  - August: umbrella spikes `occupancy-weighted-tv-regret/` (2026-07-29, plus `PARENT-VERIFICATION.md`) and `gamma-min-hypothesis/` (2026-08-02 18:42, with first-hand PDFs of Tirinzoni, Simchowitz–Jamieson and Domingues in `refs/`).
  - Claims: `02-unified-convergence-rl/adjudicated/claims/` (5 files) and `residue.md` (untracked).
- **Kind.**
  - (A5) is false as stated: the step-1 inequality was run backwards, and no $\Delta_{\min}$-free constant exists (Lattimore–Szepesvári Thm 15.2 shape).
  - The (A5v) gap-weighted repair is lossless, yet even repaired, the TV detour is weakly worse than a direct three-line argument.
  - $\Gamma_{\min}$ Theorem 1, $\Gamma(\pi) \geq \Gamma_{\min}\,\overline{\mathrm{TV}}(\pi)$ for every Markov policy and hence $\sum_k \overline{\mathrm{TV}}(\pi_k) \leq \mathrm{Regret}_K/\Gamma_{\min}$, is algorithm-independent [PROVED]. Its step-level sandwich is false (Prop 2 witness).
  - May: M2 found (C1)–(C3) over-decomposed for identification, with only (C2) doing work. H4: $B_T$ must count kernel-stationary segments, not optimum changes. H2: the bias term's $\log(1/q_0)$ factor came from a category error. VT: the $B_T$ and $V_T$ regimes share one per-round coordinate and differ only in aggregation.
- **In canon?** **Mostly not, and much of it may not belong.**
  - The BH point-mass identity is **already in canon body**: `#deriv-strategy-cost-regret-bound` §4, resolved 2026-04-24, which predates the paper. The May map's proposed new segment `#deriv-bh-pointmass-identity` rested on a misreading.
  - (C1)–(C3) landed in the `#der-loop-interventional-access` body on 2026-05-30, as the inherited memory says. The M2 refinement (only (C2) is load-bearing) did not; I read only M2's headline, so medium confidence on how far it should change canon.
  - The bottleneck-not-sum aggregator is in `#def-strategic-tempo`'s body, although a Working Note there still records that its headline defines $\mathcal T_\Sigma$ as a *sum*.
  - The $\mathcal A_{\text{decay}}$ gain-decay class theorem is cited from canon bodies (§0 point 6) but **not landed**.
  - The hard-ceiling convention item is **already handled canon-side**: `#deriv-strategic-persistence-hard-ceiling` carries the exact $(1-\lambda)/(2-\lambda)$ and treats $1-\lambda$ as the slow-forgetting asymptote. The convention debt is the paper's.
  - (A5), $\Gamma_{\min}$, $B_T$/$V_T$ and Wei–Luo are absent from canon (no hits for (A5), $B_T$ or occupancy in segment bodies).
- **What it would change.** The clear canon targets: land the $\mathcal A_{\text{decay}}$ theorem, which removes three body citations of an unpublished paper; and possibly extend `#deriv-strategy-cost-regret-bound`'s matching lower bound ($R \geq \Delta_{\min}(\cdots)$) to the occupancy-level $\Gamma_{\min}$ form. That extension is the MDP-level generalization of a fact canon already states for one step.
- **Set-aside arguments.** Most of Paper 02 is non-stationary-RL machinery, not theory of agents. Its own strategy file (`adjudicated/strategy.md`) lists "dissolve into AAT" as one of Joseph's options and puts the publishability of this paper near zero this cycle. The composition theorem in its submitted form carries the (A5) defect. Landing it in canon would need the (A5v) rewrite first, and its value to the arc of the theory is doubtful.

### F. Process and method material (for O5, not canon)

- **Truthification cascade.** `~/src/neurips/adjudicated-common/truthification-methodology.md` (2026-08-02) lays out four layers: spike → independent recon with canaries → adversarial red-team with its own adjudicator → parent verification. It keeps rung / provenance / residue as separate axes and includes a table of what each layer caught. It names itself a candidate ops/AAT SOP. This is directly about "a system of agentic truthification".
- **Lessons recorded in commit bodies.** From umbrella `b6eb2a0` and `f2168ee` (2026-07-29): two of three spike agents lost their report file (once to a harness policy block on a file named `report.md`, once to an API death at the write step). The standing lesson: verify that a report file *exists*. From `asf-recon/paper-01-asf-recon.md` §0: a same-evening spike answered a tracker's "open, nothing proved" item without the tracker knowing, so the convention is to check sibling `spikes/` mtimes before drafting from a tracker.
- **Voice and response craft.** `adjudicated-common/voice-and-tactics.md` (self-containment, the elevation rule, report-mode ban, …). AGENTS §3.1 (umbrella commits `3843d7d`, `b6d0a20`, 2026-05-06/07) adds "don't triage, route" and spike escalation as strengthening's next move. Those already reached global memory.
- **Bathtub vs. instance.** Joseph, verbatim, transcript line 912: *"The bathtub metaphor still really feels strained to me, although logogenic agents love it. The windshield metaphor for me is far, far more compelling (and isn't even a metaphor)"*. The agent's reply named the distinction: an analogy needs a dictionary the reader cannot check, while an instance is a member of the model class. This bears on `doc/sop/agents.sop.md`, which still names the bathtub gloss as the canonical Feynman exemplar, and on any `bathtub-scaffold` material. Backport queue item 4 carries it as open.
- **The driver-in-snow instance**, calibrated in that dialog: wiper = action-dependent $U_o(a)$; dashboard = blank wall; confident driver = collapsed gain. It is offered as the running example for Part I pedagogy (O4).

## 3. May Phase B status (from `spikes/neurips-back-integration-2026-05-08.md`), re-checked today

| May item | Proposed home | Status today | How checked |
|---|---|---|---|
| BH point-mass identity | new segment | **Already in canon before the paper** (`#deriv-strategy-cost-regret-bound` §4) | body read |
| Post-update chain-rule lemma | new segment | Not as named lemma; RxU2 judged it to be the definition of conditional MI, so arguably set aside | grep |
| Chart-rescaling no-go | new segment + M1 F4 | **Partly**: $\sigma$ counterexample in bias-bound §4; F4 entry absent | body read |
| (R)/(K) axioms, (H4') | bias-bound | Pointer only | WN location |
| Stuart-school reduction (A7, corrected by A8) | bias-bound | Not landed | grep |
| Architecture coverage (A6) | channel-collapse / directed-separation | Pointer only | WN location |
| JSD estimator | ambiguity-modulation | Pointer only | WN location |
| Gain-decay class theorem | strategy-persistence | **Cited from bodies, not landed** | body read |
| Bottleneck aggregator | strategic-tempo | In body | body read |
| ProST impulsive limit, Wei–Luo MASTER | strategy-persistence | Not landed (grep hits for "impulsive"/"master" are unrelated words) | grep |
| (C1)–(C3) | loop-interventional-access | **Landed 2026-05-30**; M2's "(C2) only" refinement not reflected | body read |
| F-A-G-P, KKT/LP-multiplier resolution, per-action LMI, $p_{\text{crit}}$, exit-time bound | causal-ib-lmi / -exploration | Pointer only; $p_{\text{crit}}$ is now superseded by the isotropy-gate result (§2.A) | WN location |
| OSS brittleness distinction, M2/M3 meta additions | meta-segments | Not landed | grep |

## 4. Canon flaws noticed in passing

1. `#deriv-causal-ib-lmi`: "if and only if" (line 59); the scalar-vs-matrix framing and the empirical signature (lines 19, 89, 132); the anisotropy dependence in its Working Notes. See §2.A.
2. $\kappa_{\text{processing}}$: two definitions and two scaling laws across `#der-directed-separation`, `#scope-channel-collapse`, `#scope-observation-ambiguity-modulation` and `#deriv-observation-ambiguity-bias-bound`. See §2.D.
3. `#deriv-observation-ambiguity-bias-bound` §4 states "$C=\sqrt2$ is universal" without the small-information qualifier its own boxed result carries.
4. Canon bodies cite the unpublished NeurIPS papers as the home of results: `#deriv-strategic-persistence-hard-ceiling` (×3, including Related Work), `#impl-strategy-dynamics` (line 68), `#impl-closed-loop-interiority` (line 58), `#disc-structural-imagination` (line 47), and `#disc-constructive-impossibility-posture` (line 41, table). About 30 more segments carry Working-Note pointers into `~/src/neurips/`. Body hits for "NeurIPS" in other segments are external published works (Cohen 2020, Skalse 2022, Bareinboim 2015, …) and are fine.
5. The drifting-environment literature the reviewers named has no canon presence: variable-forgetting-factor RLS / MMAE Kalman filters, change-detection non-stationary bandits, sensor scheduling and radar revisit rates. All have zero hits. They bear on `#result-persistence-condition`, `#deriv-causal-ib-exploration` and `#schema-strategy-persistence` related-work tables. The 08-03 revision outline sketches how each composes rather than competes.

## 5. The reviews as outside audit (paraphrased; files in `~/src/neurips-reviews-responses/neurips-2026/0{1,2,3}-*/reviews.md`, OpenReview dates 2026-05-30 → 07-23)

- **Paper 01**, three reviewers plus AC. All credited the core idea: survival-driven exploration at low uncertainty, original. The concerns:
  - The drift structure must be known.
  - The guarantee is expectation-level, not pathwise.
  - The scalar baseline is weak. One reviewer predicted that a posterior-dependent scalar would escape the blank wall, and §2.A shows they were right in substance.
  - The scope is linear-Gaussian.
  - Positioning against the literatures in §4.5 is missing.
  - A running physical example is missing.

  Each of these applies equally to canon's version of the result.
- **Paper 02.** The main complaints were density, undefined notation ($V_T$, $\mathcal T_\Sigma$, $\rho_\Sigma$, $R_\Sigma$), a novelty question, and (A5)'s applicability to UCRL2/UCBVI; that last point was confirmed false (§2.E). One reviewer singled out the $\mathrm{TV} = 1 - e^{-D_{\mathrm{KL}}}$ identity as elegant.
- **Paper 03.** The concerns: novelty beyond textbook inequalities; the LLM link ($\kappa$ unbounded and unestimated for transformers); bounds that are vacuous in the motivating adversarial regime; assumptions unverified for LLMs; and the terminology critique in §0.7. One reviewer credited the Čencov/(PI) argument, the chart no-go and the Separated/Partial/Coupled taxonomy as genuinely useful.
- **Joseph-voiced responses.** The response sets (`POST-READY/`, `RESPONSE-DRAFTS.md` with `.bak` revision history) are where Joseph's own late framings live. One example is the gHwS follow-up in §2.C.

## 6. Pointers into other regions

- `~/src/ops/papers/submitted/*.md` and `SUBMISSIONS.md`: venue status, with no NeurIPS decision recorded (region 6).
- `~/src/arch/asf/spikes/neurips-back-integration-2026-05-08.md` and `spikes/spike-strategic-persistence-hard-ceiling-convention-2026-05-31.md` are inside asf (KR3.2's territory). The May map's catalog-update section (§5) targets `msc/FINDINGS-RANKED-DRAFT.md`, which Joseph re-scoped on 2026-05-12 as premature until segments absorb.
- The umbrella `claude-memories/` (2026-05-07) is a frozen copy of project memories (abundance mentality, barrier vs. multiplier, spike-agent briefing, …). Most of it has already been promoted to global memory; I did not diff it against global memory.

## 7. What I did not read, so silence here is not evidence

- I did not read the three papers' `src/` trees in full. For the May content I relied on the May map plus spot checks (Paper 3 `03-setup.md` and `04-main-results.md` for $\kappa$).
- I did not read in full the bodies of the Bresenham, buffer, corrected-world and gamma-min reports, or the five scalar-vs-matrix prior-art files; I used their claim digests and the rhythm docs. The rate-reading report I read only as digested in the claim file.
- I read the May per-paper spikes at headline depth only.
- I read the 9,825-line dialog transcript only at the bathtub exchange. It is the source for Joseph's verbatim framings throughout the rhythm theory and is worth mining for them.
- I did not open `ac-guidelines.md` (2026-08-02, untracked), `PIPELINE-TODO.md`, `AUTHORING.md` or `OUTLINE-STRATEGY.md`. These are paper-pipeline and authoring docs and probably not influx, but `AUTHORING.md` (647 lines) may carry pedagogy rules relevant to O4.
