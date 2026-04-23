# TODO — Open Work Items

**Last reconciled:** 2026-04-24 (post-Gemini-pressure-point cycle Tier 1 landing; commits `6102a93` reasoning trail + `b76ee67` theory landing; six Tier 1 items landed across eight segments + one new appendix; segment count 109 → 110). This file is the living action list.

**Cycle history (most recent first).**
- **2026-04-24 Gemini pressure-point cycle — Tier 1 landing** (commits `6102a93`, `b76ee67`). Six Tier 1 items landed: (1) `#strategy-cost-regret-bound` bundled update — §4 BH identity $D_{\mathrm{KL}} = -\log(1 - \mathrm{TV})$ replaces Pinsker as primary bound with matching lower bound; §5 asymmetry-from-one-sidedness paragraph; §6.1 Shore-Johnson/Sanov/Hobson structural-equivalence note; §6.3 Bregman-Fenchel identification; §6.4 information-theoretic-MDP lineage positioning with AAD-outlier-on-KL-direction ownership + Rubin 2012 PAC-Bayesian motivation; Bishop-vs-AAD naming-collision footnote. (2) Structural-transparency lift — `#composition-closure` DA2'-inc ≡ (CT2)-at-$M=I$ equivalence with Rockafellar-Wets citation; `#contraction-template` honest-failure-modes adversarial three-obstruction convergence; `#sector-condition-derivation` rule-based/discontinuous sub-scope-β as structural Lipschitz-floor scope-exit with van der Schaft-Schumacher 2000 reference. (3) New appendix `#bias-bound-derivation` — Track 1 transport-inequality + Track 2 Fisher-Rao + Attempt E no-go + failed-attempt record + Gaussian worked example; updates `#observation-ambiguity-modulation` and `#section-ii-survival` from "order-of-magnitude guidance" to "conditional theorem." (4) `#information-bottleneck` IB-lineage vs. information-theoretic-MDP-lineage cross-reference. (5) `#loop-interventional-access` "Modes of deployment across `#identifiability-floor` instances" subsection (Mode 1 agent-self-intervention / Mode 2 observer-on-sub-agent; positions for Mode 3 when I4 lands). (6) `ref/INDEX.md` TP2011 title correction ("The Information Theory of Decision and Action" singular) — also done in reasoning-trail commit. Lint clean: 0 ordering violations, 0 missing deps, 0 orphans. **Net effect:** Gemini pressure points #1 (bridge lemma), #2 (IB purity), #5 (constant $C$) closed outright at Tier 1; #3 (ρ factorization) and #4 (neutral drift) await Tier 2 landings.
- **2026-04-24 Gemini pressure-point cycle — reasoning trail** (commit `6102a93`). External Gemini audit via `msc/joseph-working-notes.md` flagged five pressure points: (#1) composition bridge lemma — contraction assumption verified only for linear Kalman-type; (#2) IB purity — Shannon-zero / Forward-KL-infinity / reverse-KL fix framed as "abandoned IB purity"; (#3) multiplicative ρ factorization failed; (#4) neutral-drift blindness — agent state space only sees $(\alpha, \rho, R)$; (#5) missing constant $C$ in bias bound. Five parallel strengthening spikes launched (skipping #6 directed-separation-fails-for-LLMs as known structural scope-exit), four follow-up spikes launched on cross-cutting issues. **Headline outcomes:** (1) Bridge lemma **partially addressed** by post-2026-04-23 `#contraction-template` landing — DA2'-inc ≡ (CT2)-at-$M=I$ equivalence shows Euclidean metric-α₁ was AAD-internally-derived all along (structural transparency); passivity/dissipativity route with Class 1/2/3 port-structure reading of `#directed-separation`; iISS global lift for Tier 2M; two sharp no-gos (non-smooth Lipschitz floor; adversarial three-obstruction convergence). (2) IB purity **mischaracterization refuted**: Path 5 **Bretagnolle-Huber identity** (under deterministic $\pi^*$, $D_{\mathrm{KL}} = -\log(1 - \mathrm{TV})$ exactly — strictly sharper than Pinsker); Path 7 Fenchel-Bregman (reverse-KL is Bregman divergence of negative-entropy; log-odds is Fenchel-dual natural coordinate); Path 6 asymmetry forced by regret's one-sidedness (second leg of direction-forcing independent of chain-rule axiom); Path 1 **PDF-verified and reframed**: "reverse-KL IS IB" demoted per TP2011/Rubin 2012/Levine 2018 page-by-page verification; AAD is outlier on KL direction (all three lineage frameworks put agent-first, reference-second; AAD's optimum-first is forced by regret-bound). Bonus from PDFs: Rubin 2012 Theorem 3 PAC-Bayesian generalization bound — fourth independent motivation for KL-to-reference form. (3) **(AV) variance-additive decomposition** derivable as theorem under (S1)-(S4) via information-geometric Pythagorean projection; three sub-regimes where multiplicative is native (Poisson cascade MC; large-deviation tail LD; small-$\Delta$ / PID). (AV) classified as adjacent to `#additive-coordinate-forcing` (Bienaymé's identity, not Cauchy-FE). (4) **Neutral-drift gap narrower than framed** post-2026-04-23; `#agent-opacity` + `#interaction-channel-classification` + `#identifiability-floor` Instance 3 together address most of it; candidate **Instance 4** (agent-internal architecture layer) with dual CHT-at-agent-as-SCM + Kalman-Ho canonical-form anchoring; $\gamma$ estimable from cross-covariance in matched-symmetric-Tier-1 scope. (5) **Two bias-bound theorem tracks**: Track 1 transport-inequality $C_{W_2}^2 = 2L_{\mathrm{post}}^2/\rho_{\mathrm{LSI}}$ linear in $I$ (Otto-Villani under LSI + Stuart 2010 Lipschitz-posterior); Track 2 Fisher-Rao $C_{FR} = \sqrt{2}$ universal dimension-free under (PI)+Čencov + small-$I$; Attempt E no-go (universal-$C$ under Euclidean-parameter norm fails) **justifies (PI) as load-bearing**, not coincidental. **Follow-up outcomes:** (i) **Instance-4 triage** — 4 candidates → 2 genuine new primary instances (I4 agent-internal; I5 mechanism-design under broad reading with honest theorem-family labeling) + 1 sub-statement (Candidate 1 ρ-factorization projects onto I4 at disturbance-statistic layer) + 1 redirect (Candidate 3 constant-$C$ is downstream theorem of `#additive-coordinate-forcing` 4th instance, not floor instance — fails E4 single-escape criterion); three-layer `#loop-interventional-access` chain real at pattern level but non-uniform at mechanism level (agent-self / observer-on-subagent / observer-on-agent-input). (ii) **Fenchel-Bregman reframe** — Path 7 duality verified exact; stronger framing emerges: *one geometric object (exponential-family Legendre-Fenchel on categorical distributions) + four independently-motivated AAD-internal axioms converging on it + four segment manifestations*, richer than both naive Path-7 reframe and current 1-anchor-plus-3-theorem. Bonus: classifies the 4-candidate Instance-4 jam by Bregman geometry (ρ-factorization lives on squared-norm Bregman — parallel meta-pattern; coupling/constant-$C$ fall outside). (iii) **KL-to-state-distance template extraction** — Option B recommended: narrow `#posterior-displacement-template` on Otto-Villani+Lipschitz-posterior cascade with `#bias-bound-derivation` as primary instance + 3 forward-looking clients (causal-IB, misspecification-cost, composition-scope-robustness); `#variational-sector-condition` positioned as adjacent family (Pinsker shared; post-Pinsker cascade not). Contingent on `#bias-bound-derivation` landing first. (iv) **Path 1 PDF-verification extension** (§12 of IB spike, 273 lines appended) — Claim A contradicted at formula level (TP2011's actual quantity is Information-to-Go multi-information, not KL-to-reference form the spike attributed — that's Rubin 2012's); Claims B/C/D partially verified with direction-flip and terminology-collision flags. Bonus: AAD-is-outlier-on-KL-direction observation (forced by regret-bound + Path 5). Title correction: TP2011 = "The Information Theory of Decision and Action" (singular). **Ancillary session work:** naming brainstorm paper (`msc/naming-brainstorm-2026-04-24.md`); four outline ordering violations cleared (two via OUTLINE row moves; two via frontmatter dependency cleanup — `chronica.depends` no longer anticipates `causal-structure`; `value-object.depends` no longer forward-references `causal-hierarchy-requirement`); orient-cascade moved to proper §II position. Nine spike files in `msc/` (five primary + four follow-up); three new PDFs in `ref/` (`tishby-polani-2011-info-decision-action.pdf`, `rubin-2012-trading-value-info-mdps.pdf`, `levine-2018-rl-control-as-inference.pdf`) with INDEX.md entries.
- **2026-04-23 Gemini Gap A/B promotion sequence** (seven commit-scoped landings, not yet committed to git as of session end; awaiting review + commit). Six new segments promoted: **#contraction-template** (Appendix A result; B1 metric generalization with 5 α promotions, topology-indexed closures, (CM2-M)); **#strategic-composition** (Section III derivation; equilibrium-convergence framing with potential/monotone-game A2'-analogs); **#fisher-whitened-update-rule** (A3 Fisher-whitened under (PI)/Čencov); **#l1-update-bias** (A2 closed-form bias with Monte Carlo); **#variational-sector-condition** (B4 ε-fidelity); **#agent-opacity** (H_b closing #adversarial-edge-targeting). Four structurally load-bearing additions to existing segments: **Instance 3** (composition-layer no-go via Liberzon 2003) in `#identifiability-floor`; **4th primary instance** (Čencov-invariance at metric layer; 1-anchor-plus-2-theorem → 1-anchor-plus-3-theorem) in `#additive-coordinate-forcing`; **seventh ladder** (A2'-scope via contraction metrics) in `#separability-pattern`; **(C-iv) scope route** (equilibrium-convergent strategic interaction) in `#composition-scope-condition`. (PI) parameterization-invariance axiom added to `#agent-identity` as natural extension of singular-trajectory scope commitment. Monotone-operator-theory lineage explicitly acknowledged in `#sector-persistence-template` and `#sector-condition-derivation` (Rockafellar 1970 / Bauschke-Combettes 2017; one-point anchoring / Model D-S decomposition / identifiability-floor composition / composition-consistency / α-β epistemic labeling as AAD-distinctive content). Satellite cross-refs in `#critical-mass-composition`, `#composition-closure`, `#loop-interventional-access`, `#adversarial-destabilization`, `#directed-separation`, `#gain-sector-bridge`, `#edge-update-natural-parameter`, `#chain-confidence-decay`. Thirteen spike files retained in `msc/` as reasoning trails.
- **2026-04-23 Gemini Gap A/B parallel-spike cycle** (thirteen spikes written to `msc/`). Twelve parallel research spikes launched against Gemini's two flagged structural gaps, plus one follow-up spike (Jacobian-level B1 strengthening) spawned mid-cycle and completed. (A) default signal function needs validation under correlated failures (L1'/L2); (B) contraction assumptions verified only for linear Kalman-type. **Headline outcomes:** **B1** lifts Section III from linear-Kalman-centric to broadly-nonlinear-cooperative via Lohmiller-Slotine metric + Slotine 2003 compositional theorems (5 α-class promotions, heterogeneous (CM2-M), topology-indexed bridge lemma); **B5** derives Instance 3 of `#identifiability-floor` with closed-form §3.3 counterexample (Liberzon 2003 + Dayawansa-Martin 1999 as external anchors) — B1 + B5 compose as Section III completion with positive/negative halves; **B6** covers partially-opposing $O_t^{(i)}$ via equilibrium-convergence (Monderer-Shapley + Rosen 1965), proposes (C-iv) scope route, provides formal home for the effects spiral; **C1** gives partial unification honestly (2-instance-plus-1-consequence), recasts A2' α/β as Bauschke-Combettes operator-family classification. **Default-signal robustness confirmed** (A3: angle ≤ 45° at any finite ρ; A2: closed-form bias with MC). **F13 Instance 2 confirmed via four independent obstruction routes** (A1/A2/A3/A4) — not a new floor instance but strengthening of the existing one. **Jacobian-level B1 spike (completed mid-cycle) produces a mixed-lift three-layer result that materially changes B1's architectural picture:** (i) **transparency win** — DA2'-inc ≡ (CT2) at $M=I$, so Euclidean metric-α₁ cases are AAD-internally derived without any new axiom (AAD already carries the Jacobian-level condition under the name DA2'-inc); (ii) **parameterization-invariance + Čencov** — adopting a (PI) axiom (natural extension of `#agent-identity`'s token-level commitment) lifts two metric-α₂ cases (Fisher exp-family, info-metric Kalman) to AAD-internally-derived via Čencov 1982 uniqueness, and **candidate fourth primary instance of `#additive-coordinate-forcing`** under broadened "uniqueness-theorem on AAD-internal axiom" discipline; (iii) **remaining three metric-α₂ cases** (Hessian, Lyapunov-linear-Hurwitz, Lyapunov-PID) stay theorem-imported with honest labeling. **The (PI)/Čencov 4th-meta-pattern candidate supersedes C1's operator-sector candidate** as the structurally tighter fourth-meta-pattern move — derives from within AAD's meta-pattern discipline rather than recognizing external mathematical lineage. Thirteen spike files: `msc/spike-l1-evidence-axiom.md`, `-l1-update-bias.md`, `-fisher-whitened-update.md`, `-update-operator-sector.md`, `-contraction-metric-generalization.md`, `-passivity-composition.md`, `-pid-a2prime.md`, `-variational-a2prime.md`, `-composition-no-go.md`, `-strategic-composition.md`, `-operator-sector-unification.md`, `-compositional-coordinate.md`, `-jacobian-b1-strengthening.md`.
- **2026-04-23 brainstorm-cycle promotion sequence** (commits `591e8b6`, `13fe242`, `b48cdee`, `77a9bde`, `0bd859e`). Five promotions landed from the 2026-04-23 brainstorm cycle: `#interaction-channel-classification` (recipient-side four-regime theory closing the `#adversarial-edge-targeting` GAP); `#consolidation-dynamics` (Section I regime naming with stability-plasticity feasibility window); `#persistence-cost` (sustained information rate $\dot R \geq n\alpha/2$ with channel-capacity $\geq \mathcal T/2$ prerequisite); `#adaptive-gain-dynamics` (A2' sub-scope refinement $\alpha_1/\alpha_2/\beta$ via augmented-state Lyapunov); `#detection-latency` (R1 $\Omega((n_{\min}+1)/\varepsilon)$ bound sharpening forgetting prerequisite). Spike H (ρ-factorization) completed with outcome (C) honest obstruction — the multiplicative factorization $\rho = \rho_{\text{external}} \cdot f(\mathcal M) \cdot g(\pi)$ is NOT derivable; native structure is variance-additive. Segment count: 98 → 103. Spike E (internal-external decomposition) deferred pending variance-additive reframe.
- **2026-04-23 critical-mass composition promotion + brainstorm-spike landing** (commit `0d7b987`). Seven parallel research spikes launched from an external-framework comparison prompt (GAA Baigozin 2025) as a brainstorming exercise. One closed cleanly and promoted: `#critical-mass-composition` derives the composite sector constant in closed form for the symmetric-matched-Tier-1 dyad, subsuming the weakest-link bound, recovering `#team-persistence` and `#adversarial-destabilization` as signed special cases, and formalizing `#symbiogenic-composition` (S-3) as an asymmetric-parameter limit. Cross-segment strengthening to `#composition-closure`, `#team-persistence`, `#symbiogenic-composition`, `#unity-closure-mapping`, `#sector-persistence-template`. Six companion spikes landed in `msc/` ready-for-review (persistence-cost; interaction-channel classification; adaptive-gain dynamics; internal-external decomposition; consolidation dynamics; stability-induced myopia). Segment count: 97 → 98.
- **2026-04-23 SP-2 + citation audit cycle** (three commits: `7456ec3`, `6567914`, `f61e62f`). Executed Tier 1 item 1 (SP-2 meta-segment promotion) + partial Tier 1 item 2 (framing pass — CLAUDE.md §7 + OUTLINE preamble) + full citation audit project-wide. SP-2 landed as `#additive-coordinate-forcing` with the honest 1-anchor-plus-2-theorem characterization after in-flight verification narrowed Opus's 5-instance conjecture. Citation audit ran 4 parallel first-pass batches + 4 follow-up batches + 2 PDF-level Tier 1 verification agents + 1 missing-citation audit; produced 26 verified PDFs in `ref/` and zero confirmed attribution errors project-wide (reverse-KL's 20-25% rate was a local concentration in one spike, not a project-wide pattern). Segment count: 96 → 97.
- **2026-04-23 triple audit** (Codex / Gemini / Opus, post-cycle). 10 consolidated findings (F22–F31) across the three audits plus 7 session-discovered architectural proposals (SP-2 through SP-8, extending SP-1 from the strengthening cycle). ~25% of candidate findings rejected as already-adequately-caveated. See `msc/pending-findings-2026-04-23.md` and `_obs/architectural-proposals-2026-04-22.md` §"Post-2026-04-23-audit architectural extensions."
- **2026-04-22/23 cascading strengthening cycle** (nine commits: `0a772d2`, `c1d9fcf`, `2980327`, `f70fb68`, `80b40d2`, `d0373fc`, `72ca532`, `e777f01`, `a39dfb7`; plus session-close `2fc829b`). Executed Phases 1–5 + 7; landed three Cauchy-functional-equation uniqueness theorems; discovered the three-layer additive-decomposition pattern (SP-1). See Archive for per-commit detail.
- **2026-04-22 strengthening cycle** (commits `14a6095`, `b6134c2`, `4d050c8`, `b91493c`, `a14682e`). Executed strengthen-first repairs for Findings 1, 7, 10, 13 and the AI integration pass.
- **2026-04-22 triple audit (evening)**. Six findings F16–F21 (all resolved by the cascading cycle) plus nine new architectural proposals O-BP8 through O-BP16 (four of which — O-BP14, O-BP6, C-BP3, C-BP2 — landed in the cascading cycle; C-BP3 and C-BP2 were added to the portfolio in the evening batch).

The three audit cycles together mark the transition from finding-driven repair work to consolidation-and-reframing work. See §"Recommendations for next session" below for the post-2026-04-23 recommended ordering.

## Active — Pending-Review Spikes (2026-04-24 Gemini pressure-point cycle)

Nine spikes completed against five Gemini-flagged pressure points plus four cross-cutting follow-ups. All nine respect strengthen-first posture; none softened. Cross-spike convergence productive (see cycle-history entry above). No segment-level changes yet — Tier 1 landing plan drawn up and ready to execute.

### Primary spikes (five flagged pressure points)

| Spike | Location | Status |
|-------|----------|--------|
| Bridge lemma (pressure #1) | `msc/spike-bridge-lemma-nonlinear-strengthening-2026-04-24.md` | **§7.1 minimal → Tier 1**; §7.2 passivity → Tier 2; §7.3 iISS global → Tier 3 |
| IB purity (pressure #2) | `msc/spike-ib-purity-strategy-cost-strengthening-2026-04-24.md` (incl. §12 PDF-verification addendum) | **Path 5 + Path 6 + Path 7 elementary + reframed Path 1 + Path 4 note → Tier 1**; Fenchel meta-segment reframe → Tier 3 |
| ρ-factorization (pressure #3) | `msc/spike-rho-additive-variance-strengthening-2026-04-24.md` | **New `#rho-decomposition` appendix → Tier 2**; no-go Kalman tightening ~1 page → follow-up |
| Neutral drift (pressure #4) | `msc/spike-neutral-drift-endogenous-coupling-strengthening-2026-04-24.md` | **I4 promotion → Tier 2/3** (needs Kalman-Ho closed-form follow-up spike); segment addenda → Tier 2 |
| Constant C (pressure #5) | `msc/spike-bias-bound-constant-C-strengthening-2026-04-24.md` | **New `#bias-bound-derivation` appendix (Track 1 + Track 2 + Attempt E) → Tier 1** |

### Follow-up spikes (cross-cutting)

| Spike | Location | Status |
|-------|----------|--------|
| Instance-4 triage | `msc/spike-identifiability-floor-instance-triage-2026-04-24.md` | **Three-mode `#loop-interventional-access` subsection → Tier 1**; I4/I5 promotions → Tier 2/3 |
| Fenchel-Bregman reframe | `msc/spike-fenchel-bregman-reframe-additive-coordinate-forcing-2026-04-24.md` | **Local Bregman-Fenchel identification → Tier 1** (folded into IB bundled update); meta-segment reframe (7 items per §7.3) → Tier 3 architectural proposal |
| KL-to-state-distance template | `msc/spike-kl-to-state-distance-template-extraction-2026-04-24.md` | **Tier 3**: Option B (narrow `#posterior-displacement-template`) contingent on `#bias-bound-derivation` landing + ≥1 forward-looking client materializing |
| Path 1 PDF-verification | Appended §12 to IB spike | **Subsumed into Tier 1** `#strategy-cost-regret-bound` bundled update (§6.3 new subsection) |

### Tier 1 — LANDED 2026-04-24 (commits `6102a93`, `b76ee67`)

All six items landed in commit `b76ee67`. See cycle-history entry at top of file for the itemized summary. Section retained below for traceability / future-agent orientation; items marked ✅ in-place.



1. **`#strategy-cost-regret-bound` bundled update** (one segment, seven sub-moves):
   - §4 refactor: Bretagnolle-Huber identity $D_{\mathrm{KL}} = -\log(1 - \mathrm{TV})$ replaces Pinsker as primary bound (Path 5); matched lower bound $\Delta_{\min}(1 - e^{-D_{\mathrm{KL}}})$; Pinsker demoted to weaker-form remark.
   - §5 addition: "Asymmetry is forced by regret's one-sidedness" paragraph (Path 6) — second leg of direction-forcing independent of chain-rule axiom.
   - §6 new short subsection: Bregman-Fenchel identification (Path 7 elementary, local to segment) — reverse-KL as Bregman divergence of negative-entropy; log-odds as Fenchel-dual natural coordinate; cross-reference to `#edge-update-natural-parameter`.
   - §6.1 Discussion: Shore-Johnson 1980 / Hobson 1969 / Sanov 1957 structural-equivalence note (Path 4) — all factor through independence-on-sub-problems.
   - §6.3 new subsection "Information-theoretic-MDP lineage and AAD's direction choice" (reframed Path 1 per §12.5 SD1): TP2011 Information-to-Go context; Rubin 2012 control-information with explicit direction note; Levine 2018 control-as-inference positioning; AAD-is-outlier-on-KL-direction ownership paragraph; Rubin 2012 Theorem 3 PAC-Bayesian generalization bound as one item.
   - Footnote: Bishop-vs-AAD "reverse-KL" naming-collision clarification.
   - Working Notes cross-reference to `ref/INDEX.md` for corrected TP2011 title.

2. **Spike 1 §7.1 structural-transparency lift** (four paragraph-scale edits across three segments):
   - `#composition-closure` Discussion: DA2'-inc ≡ (CT2)-at-$M=I$ equivalence for $C^1$ $F$ on convex domains (Rockafellar-Wets 1998 Cor 12.4 / Nesterov 2004 §2.1.3).
   - `#contraction-template` Epistemic Status: Euclidean metric-α₁ reclassified "AAD-internally derived via DA2'-inc equivalence" (not theorem-imported).
   - `#contraction-template` Honest-failure-modes: sharpen adversarial-half statement to name three independent obstructions (Slotine-applicability / passivity-universality / contraction-metric-attractor requirement); cross-ref `#strategic-composition`.
   - `#sector-condition-derivation` sub-scope β discussion: sharpen "rule-based / discontinuous" as structurally out-of-scope for contraction-based bridge-lemma (Lipschitz floor); cross-ref hybrid-dissipative framework (van der Schaft-Schumacher 2000).

3. **New appendix `#bias-bound-derivation`** (substantial new segment, self-contained):
   - Track 1: W₂ transport-inequality theorem under (H1) statistical-manifold sub-case + (H2) LSI + (H3) Lipschitz-posterior; $C_{W_2}^2 = 2L_{\mathrm{post}}^2/\rho_{\mathrm{LSI}}$ linear in $I$.
   - Track 2: Fisher-Rao theorem under (H1) + (H4) small-information regime + (PI)/Čencov; universal dimension-free $C_{FR} = \sqrt{2}$, $\sqrt{I}$ scaling.
   - Attempt E no-go: heteroscedastic-normal family counterexample shows universal-$C$ under Euclidean-parameter norm fails — justifies (PI) adoption as load-bearing.
   - Honest failure record: Cramér-Rao inversion (wrong direction), rate-distortion inversion (wrong problem structure) — documented so future agents do not repeat.
   - Gaussian worked example: $\rho_{\mathrm{LSI}} = 1/\sigma^2$ under Gaussian observation; conjugate-Gaussian prior gives explicit $L_{\mathrm{post}}$.
   - Updates: `#section-ii-survival` and `#observation-ambiguity-modulation` — "Without the constant, the bound is order-of-magnitude guidance, not a theorem" replaced with cross-reference to the new appendix; bias-bound tier upgraded to "conditional (exact under H1-H3 or H1+H4)".
   - Deps: `section-ii-survival`, `observation-ambiguity-modulation`, `agent-identity`, `additive-coordinate-forcing`, `directed-separation`.

4. **`#information-bottleneck` cross-reference paragraph** (§12.5 SD3): distinguish the canonical IB instance ($(X, T, Y)$ with Shannon MI on both sides) from the information-theoretic-MDP-lineage instance (KL-to-reference-policy at strategy-cost layer). Pre-empts "why isn't the strategy-cost term a mutual information like the others?" at the meta-segment level.

5. **`#loop-interventional-access` two-mode deployment subsection** (triage spike §4.2): name the two currently-live modes — *agent-self-intervention* (Instance 1: agent does do-actions in its own loop) and *observer-on-sub-agent* (Instance 3: observer intervenes on $A_j$ to reveal $A_i$'s cross-coupling response). Positions the segment for extension to three modes when Instance 4 promotes (observer-on-agent-input). Surfaces already-implicit structure; no new content.

6. **`ref/INDEX.md` TP2011 title correction** — DONE 2026-04-24 (filename updated `tishby-polani-2011-info-decision-action.pdf`; entry corrected to singular "The Information Theory of Decision and Action").

### Tier 2 (after Tier 1 lands)

- **Spike 3 `#rho-decomposition`** new appendix — (AV) theorem + sub-regime catalog (MC/LD/PID) + no-go at discussion-grade. Unblocks deferred `#internal-external-decomposition` spike from 2026-04-23 brainstorm cycle.
- **Spike 1 §7.2 `#dissipativity-template`** new appendix + Class 1/2/3 port-structure reading addition to `#directed-separation`. Closes heterogeneous Kalman + PID-on-positive-real-plant composition case explicitly.
- **Instance 4 promotion** (agent-internal architecture) — requires **follow-up spike** for Kalman-Ho closed-form no-go construction (~1 page of algebra). Dual-anchored by CHT-at-agent-as-SCM + Kalman-Ho canonical-form non-uniqueness.
- **Instance 5 promotion** (multi-agent-aggregation mechanism-design) — Arrow / Gibbard-Satterthwaite / Myerson-Satterthwaite; broad reading of meta-pattern with honest "implementability vs. identifiability" theorem-family labeling.

### Tier 3 (architectural proposals)

- **`#additive-coordinate-forcing` Fenchel-Bregman reframe**: move from "1-anchor + 3 theorems" to "one geometric object + four independently-motivated axioms converging on it + four segment manifestations." Seven-item rewrite per Fenchel spike §7.3. Preserves axiom-independence while naming geometric convergence. Substantial. **Now tracked as SP-9 in [`PROPOSALS.md`](PROPOSALS.md) §E.3** (wait-gated on Amari-Nagaoka 2000 PDF verification + Bundle 1 framework-face reframe landing first).
- **`#posterior-displacement-template` extraction (Option B)**: narrow template on Otto-Villani + Lipschitz-posterior cascade. Contingent on `#bias-bound-derivation` landing + ≥1 forward-looking client materializing.
- **Spike 1 §7.3 `#iISS-contraction`**: global Tier-2M lift under uniform Jacobian conditioning. Optional; lower urgency than §7.1 / §7.2.

### Follow-up spikes queued

- **Kalman-Ho closed-form for Instance 4** — ~1 page. Gates Instance 4 promotion.
- **ρ-factorization no-go tightening** — ~1 page Kalman algebra for Scenarios A/B counterexample. Gates Instance-4-sub-statement cleanup.
- **Mechanism-design Instance 5 formalization** — under broad reading; clean citations.
- ~~**Fenchel-Bregman reframe architectural proposal write-up**~~ — **DONE 2026-04-24**: landed as SP-9 in [`PROPOSALS.md`](PROPOSALS.md) §E.3.


## Active — Pending-Review Spikes (2026-04-23 brainstorm cycle — five promoted, one deferred)

### Landed in this cycle
Six of the seven brainstorm-cycle spikes have now been promoted. Summary with commit hashes:

- **Spike B → `#critical-mass-composition`** (appendix-A derivation). Commit `0d7b987`. Closed-form composite sector-constant under symmetric-matched-Tier-1 dyad; subsumes weakest-link bound.
- **Spike C → `#interaction-channel-classification`** (Section III derived). Commit `591e8b6`. Four-regime recipient-side theory; closes `#adversarial-edge-targeting` GAP as emitter-side optimizer to recipient-side classifier pairing.
- **Spike F → `#consolidation-dynamics`** (Section I formulation). Commit `13fe242`. Regime of $g_M$ with IB-gap-reduction objective; stability-plasticity feasibility window sharpens the asymmetric forgetting-only story.
- **Spike A → `#persistence-cost`** (appendix-A derivation). Commit `b48cdee`. $\dot R \geq n\alpha/2$ nats/time under Model S + Gaussian-OU; Kalman-Bucy saturates; channel-capacity $\geq \mathcal T/2$ floor.
- **Spike D → `#adaptive-gain-dynamics`** (appendix-A derivation). Commit `77a9bde`. (MG-1)–(MG-4) meta-gain conditions; augmented-state Lyapunov composition; A2' refined into $\alpha_1$/$\alpha_2$/$\beta$.
- **Spike G → `#detection-latency`** (appendix-A derivation). Commit `0bd859e`. R1 within-class drift bound $\Omega((n_{\min}+1)/\varepsilon)$ structurally forced by Aczél-FE log-odds; sharpens `#strategy-persistence-schema` forgetting prerequisite.

### Deferred pending reframe

- **Spike E — Internal-external decomposition** (`msc/spike-internal-external-decomposition.md`). **Deferred.** Spike H (ρ-factorization) completed with outcome (C) honest obstruction: the multiplicative factorization $\rho = \rho_{\text{external}} \cdot f(\mathcal M) \cdot g(\pi)$ is NOT derivable from AAD-internal quantities. Native structure is variance-additive $\rho^2 = \rho_{\text{irr}}^2 + \Delta_{\mathcal M}^2 + \Delta_\pi^2 + \text{cross}$; the log-multiplicative form is a small-$\Delta$ Taylor approximation. Impact: coarse decomposition $\mathcal V = \log\lVert\delta_{\text{crit}}\rVert - \log\rho + \log\alpha$ survives at exact tier; fine decomposition needs reframing to variance-additive form; `#identifiability-floor` Instance 3 status survives; `#separability-pattern` seventh-ladder status *strengthened* (structured-repair ring now has concrete mediation-analysis content on cross terms).
  - **Two promotion paths** — choose at next session:
    - **(Path 1, smaller):** Land only the coarse form as a paragraph in `#persistence-condition` Discussion noting the internal-external rearrangement on log-scale; develop TST rotation-experiment diagnostic separately (operationalization section). Keep variance-additive reframe in `msc/` pending.
    - **(Path 2, full):** Rewrite Spike E in variance-additive form with explicit cross-term handling (mediation-analysis framework), then promote as appendix segment `#internal-external-decomposition` at *conditional* (sub-scope $\alpha$ + small-$\Delta$ or variance-Pythagorean) / *heuristic* (general) tiers. Requires ~1 session of rewrite work + 1-2 sessions of cross-term derivation.

### Template-augmentation composition (observation)

Spikes B, A, and D together constitute a *template-augmentation triad* under `#sector-persistence-template`. Each persistence-flavored segment now inherits:
- a threshold condition (existing template instantiation),
- a cost-rate bound $\dot R \geq n\alpha/2$ via #persistence-cost,
- a meta-gain contraction condition via #adaptive-gain-dynamics when the gain itself is adaptive,
- a closed-form critical-mass formula via #critical-mass-composition for composite instantiations.

This is a candidate meta-segment if the pattern firms up — naming the augmentation structure explicitly. Not yet warranted (four instances across three segments is thin for a meta-segment). Worth flagging and re-visiting after the next strengthening cycle.

### Future spikes opened by this cycle

- **Misspecification-cost formalization** — Regime II-b of `#interaction-channel-classification` is a candidate Instance 3 for `#identifiability-floor`'s "Misspecification-cost quantification" open extension. Would sharpen the floor pattern's coverage.
- **Stability-upper-bound derivation for consolidation** — `#consolidation-dynamics`'s feasibility window has a well-posed lower bound (existing forgetting prerequisite) but the upper bound's functional form is open. Derivation would tighten the window and sharpen the catastrophic-forgetting scope claim.
- **Channel-capacity as first-class AAD quantity** — biggest architectural opening from `#persistence-cost`. Lift Shannon capacity $C^{(k)}$ into NOTATION.md and relate to $U_o$ via standard capacity-from-noise transform; connect to the tempo framework. Converts "needs more bandwidth" observations into specific dimensional requirements.
- **$f(H_b^B)$ emitter-side-effect function** — tightens `#interaction-channel-classification` §5.2 qualitative opacity-gates-targeting claim into derived form.
- **Variance-additive reframe for Spike E** — prerequisite for Path 2 promotion of internal-external decomposition.
- **EWC tensor-valued gain extension of `#adaptive-gain-dynamics`** — stability-weighted per-parameter gain per Kirkpatrick et al. 2017. Adapts MG-1-MG-4 to tensor form.


## Active — Pending-Review Spikes (2026-04-23 Gemini Gap A/B cycle)

Twelve parallel research spikes launched against Gemini's two flagged structural gaps. Each self-contained; promotion decisions require independent review before landing in segments. One follow-up spike (Jacobian-level B1 strengthening) is in flight; its outcome affects B1's landing epistemic status.

**The two gaps (from Gemini 2026-04-23 audit):**
- **Gap A** — Section II default signal function (log-odds credit-assignment update via `#edge-update-natural-parameter`) needs validation under *correlated failures* (L1'/L2 correlation hierarchy).
- **Gap B** — Section III composition contraction assumptions verified only for linear-Kalman-type agents; sub-scope β (PID / rule-based / variational / non-convex-beyond-basin / strategic / heterogeneous) uncovered.

### Completed follow-up (2026-04-23) — affects B1 landing

- **Jacobian-level B1 strengthening** (`msc/spike-jacobian-b1-strengthening.md`). **Completed with mixed-lift three-layer result, not binary.** Spawned mid-cycle after B1 spike surfaced that metric-α₂ derivations are theorem-imports from Lohmiller-Slotine (spike §8.2 item 1; §9 question 1). Outcome structurally changes the B1 landing picture:
  - **Transparency win (Angle 2 clean).** `#composition-closure`'s DA2'-inc ≡ Lohmiller-Slotine (CT2) at $M=I$ for $C^1$ $F$ on convex domains (standard Rockafellar-Wets / Nesterov). AAD has been carrying the Jacobian-level Euclidean contraction condition at the composite level all along under the name DA2'-inc. All Euclidean metric-α₁ cases (Kalman-scalar, Euclidean strongly-convex, L2-regularized, linear-PD-symmetric) lift to AAD-internally-derived *without any new axiom*. **This is the under-advertised find — AAD's existing commitment is already stronger than it reads.**
  - **Parameterization-invariance + Čencov (Angle 3) clears the 1-anchor-2-theorem discipline.** Introduce axiom (PI) as extension of `#agent-identity`'s token-level commitment: AAD's predictions should not depend on arbitrary choice of coordinates. Čencov 1982 uniqueness theorem forces Fisher metric uniquely on statistical manifolds under (PI). **Structurally parallel to Cauchy-FE → log-coordinate, but via Čencov-invariance rather than Cauchy-FE.** Promotes **two of five** metric-α₂ cases (Fisher exp-family, information-metric Kalman) to AAD-internally-derived. **Candidate fourth primary instance of `#additive-coordinate-forcing`** — if adopted, broadens the meta-pattern from "Cauchy-FE on additivity axiom → logarithmic coordinate" to "uniqueness theorem on AAD-internal structural axiom → forced geometric coordinate" (Cauchy-FE + Čencov as distinct uniqueness-theorem machinery both clearing the same discipline bar).
  - **Heredity-under-composition-consistency (Angle 1) works but requires architectural commitment.** Agent-level B1 alone is insufficient for composite-level DA2'-inc under parallel composition (rotating-inward counterexample). Under a *heredity* axiom (composite admissibility derivable from sub-agent properties — legitimate AAD-internal extension of `#composition-consistency`), agent-level B1* is forced. This is an architectural strengthening of `#composition-consistency`, not a uniqueness-theorem-style derivation.
  - **Three of five metric-α₂ cases remain theorem-imported with honest labeling.** Hessian-metric strongly-convex (Hessian chosen to match loss); Lyapunov-metric linear-Hurwitz-non-symmetric (Lyapunov equation from plant); Lyapunov-metric PID-bounded-plant (same); basin-chart non-convex-within-basin (domain-specific). No AAD-internal axiom cleanly forces these metric choices.
  - **Key structural clarification.** The 1-anchor-2-theorem discipline in `#additive-coordinate-forcing` is *broader* than "Cauchy-FE on additivity." Shared core: "uniqueness-theorem-forced coordinate under AAD-internally-motivated axiom." Čencov-invariance instance sits cleanly within this broader reading; Angles 1/2/4/5 sit in adjacent-family territory (converse-Lyapunov / compositional-closure / matched-coordinate mechanisms — AAD-internal but not uniqueness-theorem-forced).
  - **Three landing options (§11).** Minimal (structural transparency note on DA2'-inc ≡ (CT2) + honest labeling in `#contraction-template`); moderate (adopt (PI), add fourth primary instance to `#additive-coordinate-forcing`, add B1* to `#gain-sector-bridge`); strong (adopt (PI) + heredity, collapse Tier structure, promote (CM2-M) from Slotine-imported to AAD-derived). Choice is architectural, not mathematical — all three are internally consistent.

### Completed (pending review) — Gap A (4 spikes)

| Spike | Location | Outcome |
|-------|----------|---------|
| A1 L1' evidence axiom (block-structured Cauchy FE) | `msc/spike-l1-evidence-axiom.md` | Observable-$C$: $(2K+1)$-dim coordinate forced per-factor Aczél. Unobservable-$C$: Cauchy FE **structurally inconsistent** with Bayesian mixture updates (responsibility reweighting is nonlinear). Classified as *generalization-in-scope* of existing `#edge-update-natural-parameter`, **not a new theorem in `#additive-coordinate-forcing`**. Unobservable branch converges with F13 Cramér-Rao at same boundary — dual-obstruction confirmation of existing Instance 2, not new instance. Minimal landing: Block Structure subsection in `#edge-update-natural-parameter`. |
| A2 L1' update bias formula | `msc/spike-l1-update-bias.md` | Closed-form bias $B_k(\rho) = -\iota_k(1-\mu_{\bar k})\rho / [(n_k+1)((1-\mu_1)^2 + (1-\mu_2)^2)]$ at matched-marginal IC. AND-root counterpart (opposite sign). Monte Carlo (400 trials × 5000 cycles) confirms closed form. **L1'-induced biased fixed point**: edges converge to wrong values matching L1' root-prob. Observable-$C$: Prop B.7 eliminates bias exactly. Unobservable-$C$: Cramér-Rao floor $\propto \rho/(1-\lambda)$. **Dual forgetting-rate requirement** derived; admissibility window may be empty → augmentation required. Candidate landing: new appendix `#l1-update-bias` (quantitative numerical-floor companion to F13). |
| A3 Fisher-whitened edge update | `msc/spike-fisher-whitened-update.md` | **LO-vs-NG angle never exceeds 45° under finite correlation** — B1 is never actively violated, only degraded by factor $\sqrt{1-r^2}$. Fisher whitening **AAD-internally derivable** via two convergent axiom paths: (a) B1-parameterization-invariance; (b) Lyapunov-coordinate-matching via `#additive-coordinate-forcing`'s adjacent-family framework. Both vacuous at L0, force Fisher whitening at L1'/L2. New sub-scope $\alpha_3$ (correlated evidence + Fisher-whitened + Bayesian coherence → A2' derived). Connects to `#adaptive-gain-dynamics` as meta-gain special case $K_t = \mathcal I^{-1}(\lambda_t)$. Candidate landing: new segment `#fisher-whitened-update-rule` + touches to `#gain-sector-bridge`, `#credit-assignment-boundary`. |
| A4 Update-operator sector condition | `msc/spike-update-operator-sector.md` | (O-A2') operator sector condition derives for the log-odds update with closed-form constant $\alpha_{\text{op}}^{\text{comp}} = \min_k (1/(n_k+1))\iota_k (J_k^2/\|\mathbf J\|^2)\sigma'(\lambda_k^*)$. Sub-scope α/β transfers structurally from `#gain-sector-bridge`. Step-size condition lifts for free under Beta-Bernoulli. L1' observable-$C$: graceful degradation; L1' unobservable-$C$: structural break via Fisher-rank-1 (**confirms F13 Instance 2 at operator layer, not a new instance**). Sequential composition is log-additive in $\alpha_{\text{op}}$ — adjacent-family addition at operator-composition layer for `#additive-coordinate-forcing`. Candidate landing: new appendix `#update-operator-sector` (or subsumed into C1's operator-sector-template if that path is taken). |

### Completed (pending review) — Gap B (6 spikes)

| Spike | Location | Outcome |
|-------|----------|---------|
| B1 Contraction-metric generalization | `msc/spike-contraction-metric-generalization.md` | **(CT1)–(CT3) template derived** (Lohmiller-Slotine metric formulation of `#sector-persistence-template`). Five α promotions: Kalman info-metric (no $\kappa(P^-)$ penalty), exp-family Fisher-metric, Hessian-metric ill-conditioned, linear-Hurwitz-non-symmetric (new coverage), PID-bounded-plant (β→metric-α₂). Heterogeneous (CM2-M) generalizing matched-symmetric `#critical-mass-composition`. **Topology-indexed bridge lemma** via Slotine 2003 (parallel / cascade / feedback). Seventh ladder for `#separability-pattern` (A2'-scope → metric-α₁ / metric-α₂ / metric-β). **Honest limit:** metric-α₂ currently *theorem-imported* from Lohmiller-Slotine; Jacobian-level B1 strengthening spike in flight tests whether this becomes AAD-internal. Adversarial composition structurally outside — hands to B6. Candidate landing: new meta-segment `#contraction-template` + 8 segment-level edits. |
| B2 Passivity / dissipativity composition | `msc/spike-passivity-composition.md` | AAD sector condition recognized as scalar-SISO-quadratic-storage special case of Willems 1972 dissipativity. Heterogeneous (Kalman + PID-on-positive-real-plant) composition delivers $\mathcal L_2$-stability with composite storage $S = S_1 + S_2$ — reaches Tier-3 heterogeneity that `#critical-mass-composition` cannot. Port-structure reading of Class 1/2/3 (third axis). PID-on-positive-real-plant → α'' (third independent route, same scope boundary as B3/B1). Candidate landing: new meta-segment `#dissipativity-template` as generalization of `#sector-persistence-template`. **Architectural question with B1:** do `#contraction-template` and `#dissipativity-template` sit as siblings, or is one the parent? C1 suggests both are instances of operator-sector primitive (strongly-monotone / cocoercive in different inner products). |
| B3 PID A2' derivation | `msc/spike-pid-a2prime.md` | **Classical result recast in AAD form.** SPR condition ↔ B1 directional fidelity; $\alpha_{\text{PID}} = \omega_c \sin(\varphi_m)/\kappa(P)$ with phase margin as sector constant. IMC / lambda / SIMC tuning → α; Ziegler-Nichols aggressive → β. Cascade-PID composition instantiation with timescale-separation bound. Composes with adaptive-gain-dynamics as special case (gain-scheduled PID). PID is the dominant industrial controller — promotion is order-of-magnitude scope expansion in applicable agent population. Candidate landing: minimal (α list refresh in `#sector-condition-derivation`) or full appendix (`#pid-sector-derivation`). |
| B4 Variational approximate A2' | `msc/spike-variational-a2prime.md` | Under $\mathrm{KL}(q\|p) \leq \varepsilon$: **ε-fidelity B1 derived at $O(\sqrt\varepsilon)$ rate (Pinsker-tight)**. Regime A/B structure: sector bound clean on annulus $\mathcal B_R \setminus \mathcal B_{2\delta_0}$; approximation-dominated floor $\delta_0 = O(\sqrt\varepsilon)$. Natural-gradient VI + exp-family recovers FULL α (not ε-degraded). Mean-field VI is workhorse α' case. Amortized VI: errors compose additively. Partition expansion from {α, β} to {α, α', β}. Rule-based / diffusion-posterior / uncontrolled-ε stay β. Candidate landing: new appendix `#variational-sector-condition` + A2' partition update in `#sector-condition-derivation`. |
| B5 Composition identifiability floor | `msc/spike-composition-no-go.md` | **Instance 3 of `#identifiability-floor` derived** (Liberzon 2003 Theorem 2.1 + Dayawansa-Martin 1999 as external anchor). **Closed-form §3.3 counterexample**: two coupled scalar symmetric-matched-Tier-1 systems with identical marginal component distributions but opposite composite-contraction signs — the single bit of coupling-sign is unidentifiable from component marginals, and that bit is exactly what `#critical-mass-composition`'s CM2 needs. Load-bearing test §7.1 passes: removing `#critical-mass-composition` reduces certification to weakest-link bound (blind to coupling sign); removing composite-extended `#loop-interventional-access` leaves coupling sign unidentifiable. Three-layer completeness (F1 + F13 + Instance 3). Class-2 merged correctly *rejected* as floor instance (belongs to `#separability-pattern`'s architecture ladder per scope-honesty). Candidate landing: primary = Instance 3 in `#identifiability-floor`; secondary cross-references in `#critical-mass-composition`, `#loop-interventional-access`, `#composition-scope-condition`, `#separability-pattern`. |
| B6 Strategic composition via equilibrium | `msc/spike-strategic-composition.md` | Replaces contraction-to-shared-truth with equilibrium-convergence for partially-opposing $O_t^{(i)}$. **Potential-game A2'-analog** (Monderer-Shapley 1996) exact transfer of `#sector-persistence-template` to joint $\nabla\Phi$. **Monotone-game A2'-analog** (Rosen 1965) weighted-norm version. Sub-scope α' (potential/monotone/strongly-monotone derived) vs β' (VI existence only; regret-minimization CCE set-convergence only). Zero-sum scalar worked example fully derived at $\alpha = 1$, $R = 2\sqrt 2$. **Formal home for `#adversarial-destabilization`'s effects spiral**: joint-Jacobian eigenvalue condition at candidate equilibria. Strategic composition produces **Class 3 composites from Class 1 sub-agents** — refinement of `#directed-separation`. Mechanism-design impossibility (Gibbard-Satterthwaite / Arrow / Myerson-Satterthwaite) flagged as candidate fourth `#identifiability-floor` instance. Candidate landing: new Section III segment `#strategic-composition` + (C-iv) route in `#composition-scope-condition` + seven additional satellite edits. |

### Completed (pending review) — Cross-cutting (2 spikes)

| Spike | Location | Outcome |
|-------|----------|---------|
| C1 Operator-sector unification | `msc/spike-operator-sector-unification.md` | **Partial unification, honestly reported.** Continuous-time sector template ($\Phi_h$ flow), discrete update map ($T_d$), and composite macro-update ($T_c$) all fit one operator-sector primitive $\langle (I-T)(x), x-x^\ast\rangle \geq \kappa \|x-x^\ast\|^2$ (one-point reduction of Rockafellar / Bauschke-Combettes strong monotonicity). **Coarse-graining projection $\Lambda$ does NOT fit** (heterogeneous spaces, three independent P1/P2/P3 admissibility conditions). Honest picture: **2-instance-plus-1-consequence, not symmetric 3-instance**. Load-bearing gain: **A2'/DA2' α/β recasts as operator-family classification** (α ↔ proximal / firmly-nonexpansive / cocoercive / strongly-monotone-gradient / linear-PD — exactly Bauschke-Combettes classical classes). AAD-distinctive content over monotone-operator theory: one-point anchoring, Model D/S decomposition, identifiability-floor composition, composition-consistency postulate, α/β epistemic labeling — AAD is *specialization + repurposing*, not strict generalization. Pairs naturally with Opus O-BP10 slogan. Candidate landings (three options): R1 new fourth meta-pattern `#operator-sector-template`; R2 minimal segment edits; R3 archive as positional document. |
| C2 Compositional coordinate forcing | `msc/spike-compositional-coordinate.md` | **Honest negative result with structural insight.** Five candidate axioms examined; **no fourth theorem exists at composition layer** in the `#additive-coordinate-forcing` sense. **Structural reason:** Cauchy-FE operates on *functional-form families* (f-divergences, credence reparameterizations); composition-layer quantities present as *coupling-pattern choices*, not functional-form families. `#additive-coordinate-forcing` is architecturally single-agent. Log-closure-deficit along composition tower lands as **fourth *anchor*** (mathematical identity), not fourth theorem — honest framing becomes 2-anchor-plus-2-theorem. Fisher-info / identifiability / communication-tree / composition-tower all corollaries of `#chain-confidence-decay` (**unsurfaced Section III reach** — cheap surfacing opportunity). Composition admits its own structural family — **monotonicity-under-composition** (bridge-lemma, Tier 1/2/3, CM4) — candidate future Section III meta-segment, parallel to but NOT reducible to `#additive-coordinate-forcing`. Candidate landing: light Working Note to `#additive-coordinate-forcing`; substantive Discussion to `#chain-confidence-decay`; follow-on spike for composition-monotonicity meta-segment. |

### Co-owner landing recommendation (2026-04-23 — EXECUTED; retained below for reasoning trail)

*Joseph authorized promotion; seven commit-scoped landings executed in-session. See cycle-history entry at file top for summary of what landed. The recommendation below is retained as the in-session reasoning record.*



*Framed by field impact, not by effort or low-risk hedging. Revised after the Jacobian-level B1 spike completed — the outcome changes the architectural calculus materially.*

**The picture the Jacobian-level B1 spike reveals.** The B1 landing splits cleanly into three layers rather than landing under a single epistemic label:
1. **Euclidean metric-α₁ cases** (Kalman-scalar, Euclidean strongly-convex, L2-regularized, linear-PD-symmetric) — AAD-internally derived without any new axiom via DA2'-inc ≡ (CT2) at $M=I$. Transparency win: the theory already carries this commitment at the composite level; B1 landing surfaces it at the single-agent level.
2. **Fisher-metric metric-α₂ cases** (Fisher-metric exp-family, information-metric Kalman) — AAD-internally derived *if* the parameterization-invariance axiom (PI) is adopted. Čencov 1982 forces the Fisher metric uniquely under (PI). (PI) extends `#agent-identity`'s token-level commitment AAD-internally. **Candidate fourth primary instance of `#additive-coordinate-forcing`** under a broadened 1-anchor-2-theorem reading (Cauchy-FE and Čencov as distinct uniqueness-theorem machinery both clearing the same AAD-internal-axiom discipline).
3. **Remaining three metric-α₂ cases** (Hessian, Lyapunov-linear-Hurwitz, Lyapunov-PID) — stay theorem-imported with honest labeling. No AAD-internal axiom cleanly forces these metric choices.

**Tier 1 — Section III completion push (B1 + B5 land together, with the three-layer B1 picture).** B1 and B5 remain exact complements; my prior analysis stands. What changes is B1's landing structure: not "metric-α₂ is theorem-imported" flat, but the three-layer split above. Euclidean cases are AAD-internal transparency wins; Fisher cases depend on (PI) adoption decision; remaining cases carry honest theorem-import labels. B5 (Instance 3 composition floor with closed-form §3.3 counterexample) lands unchanged and reframes `#critical-mass-composition` as the unique broadly-available escape.

**Tier 1 — Strategic composition (B6 lands in parallel).** Unchanged. Covers partially-opposing $O_t^{(i)}$ via potential/monotone games; formal home for the effects spiral; Class-3-from-Class-1-sub-agents refinement of `#directed-separation`.

**Tier 1-ARCHITECTURAL DECISION — (PI) axiom adoption.** The Jacobian-level B1 spike surfaces a substantive architectural choice that was previously hidden: whether to adopt (PI) as an AAD axiom.
- *Adoption route.* `#agent-identity`'s token-level commitment already says AAD is about agents on singular causal trajectories. Extending to "AAD's predictions should not depend on arbitrary choice of coordinates" is a natural AAD-internal move. Under (PI), Fisher metric is uniquely forced (Čencov 1982), and Fisher-metric α₂ cases become AAD-internally derived. This also opens the fourth-primary-instance promotion of `#additive-coordinate-forcing` under the broadened "uniqueness-theorem-forced coordinate" reading.
- *Non-adoption route.* Fisher-metric α₂ cases stay theorem-imported like the Hessian / Lyapunov cases. Cleaner but leaves identified structural machinery on the table.
- **Recommendation:** adopt (PI). The axiom is naturally motivated by existing `#agent-identity`, Čencov is an established uniqueness theorem, and the fourth-primary-instance promotion tightens `#additive-coordinate-forcing`'s architectural role. The case is structurally analogous to the chain-rule-additivity and evidential-additivity axioms already adopted at the divergence and update layers — natural-from-adjacent-AAD-commitment and uniqueness-theorem-forced.

**Tier 1-DELIBERATE — revised C1 decision.** My previous recommendation ("do not elevate operator-sector to fourth meta-pattern") now sits alongside an alternative fourth-meta-pattern candidate: the Čencov-invariance-via-(PI) extension of `#additive-coordinate-forcing`. Of the two candidates, **the (PI)/Čencov extension is the stronger fourth-meta-pattern move** because it derives from within AAD's existing meta-pattern discipline (uniqueness theorems on AAD-internal axioms) rather than recognizing an external mathematical lineage (monotone-operator theory). If the choice is "one fourth meta-pattern addition," pick (PI)/Čencov. C1's operator-sector content still lands (A2'/DA2' α/β recasting as operator-family classification; one-point anchoring as AAD-distinctive), just as *content* in `#sector-condition-derivation` and `#sector-persistence-template` rather than as a peer meta-pattern.

**Tier 2 — Content additions (unchanged).** A3 (Fisher-whitened update — now composes with (PI)/Čencov story cleanly since Fisher whitening follows from (PI)), A2 (L1' bias formula with MC), B3 (PID derivation — three independent routes still converge), B4 (variational α' via Pinsker), A4 (update-operator sector). Each lands cleanly; each composes with Tier 1.

**Tier 3 — Working Notes only (unchanged).** A1 (block-evidence generalization); C2 (honest negative result surfacing `#chain-confidence-decay`'s Section III reach and the candidate composition-monotonicity meta-segment).

**Strong-option possibility — heredity axiom.** The Jacobian-level B1 spike's Angle 1 shows that under a *heredity* axiom (composite admissibility derivable from sub-agent properties), agent-level B1* is forced. This is a legitimate AAD-internal architectural strengthening of `#composition-consistency`. If adopted alongside (PI), metric-α₂ Tier structure collapses and (CM2-M) promotes from Slotine-imported to AAD-derived. This is the most ambitious reading; I would not lead with it, but flag it as a future-session architectural decision worth its own scoping spike.

**Future spikes this cycle opens (revised):**
- **Fourth primary instance of `#additive-coordinate-forcing` via (PI)/Čencov** — if (PI) adoption is accepted, the meta-segment's 1-anchor-2-theorem characterization broadens to 1-anchor-3-theorem (chain anchor; divergence + update Cauchy-FE theorems; Fisher-metric Čencov-invariance theorem). This is now the recommended Phase-B follow-on after B1+B5 land.
- **Heredity axiom for `#composition-consistency`** — scoping spike to test whether the architectural commitment is worth the simplification it enables (Tier collapse + CM2-M AAD-derived).
- **Mechanism-design impossibility as fourth `#identifiability-floor` instance** (from B6 §6).
- **Composition-monotonicity meta-segment** (from C2 §10 failure branch — distinct-from-`#additive-coordinate-forcing` Section III structural family).
- **Single axiomatic obstruction behind Cauchy-FE failure + Cramér-Rao rank-deficiency** (from A1 §9.4 O2).
- **Adaptive-metric-coupling** interaction with `spike-adaptive-gain-dynamics`'s (MG-4) (from B1 §6.4).

### Reverse-check flagged (FORMAT.md Gate-3-sidebar)

Per FORMAT.md's standing spike-to-segment reverse-check convention: the six brainstorm-cycle promotions should be verified against the original spike content to confirm no over-aggressive compression. Each spike remains in `msc/spike-*.md` as reasoning trail per `feedback_math_lives_in_segments.md`. Specific items to check on next touch:

- **Spike A / `#persistence-cost`** — did the "channel-capacity as biggest architectural opening" framing survive? (Retained in Working Notes.) Did the Model-D-adversarial-analog flag survive? (Yes, in Working Notes.)
- **Spike B / `#critical-mass-composition`** — did the (UO-mult) discussion-grade labeling survive? (Yes, per derivation-audit table.) Did the obstruction analysis §6 survive? (Yes, in Working Notes + derivation-audit rows.)
- **Spike C / `#interaction-channel-classification`** — did the Regime-I-with-adversarial-content attack survive? (Yes, in Discussion.) Did the $\mathcal I_{\max}$ heuristic caveat survive? (Yes, in Working Notes with sufficient-statistics-span alternative.)
- **Spike D / `#adaptive-gain-dynamics`** — did the honest "imported machinery" acknowledgment survive? (Yes, in Epistemic Status.) Did the MAML case's honest classification-not-derivation label survive? (Yes, in derivation-audit table.)
- **Spike F / `#consolidation-dynamics`** — did the R2 sub-case (C1 blindness under model-class inadequacy) survive? (Flagged as discussion-level in Working Notes.) Did the stability-upper-bound "pending derivation" flag survive? (Yes, in Epistemic Status + Working Notes.)
- **Spike G / `#detection-latency`** — did the R2/R3 sub-cases survive compression? (R2 as Working Notes one-evening-spike flag; R3 as reference to #identifiability-floor Instance 1 without re-deriving.) Did the IDT-bypass prediction survive? (Yes, in Discussion.) Did the honest "not novel mathematically; novelty is AAD-framing" survive? (Yes, in Epistemic Status.)

Probably ~30 minutes of focused reading per spike; can be done in a dedicated editorial pass at next session start.

## Highest-priority cleanups — LANDED (Phase 1 of strengthen-first cycle)

All four cleanups landed. F20 strengthened rather than softened; the others were mechanical cross-segment updates. Detail in Archive section below.

- ~~**F18** — `#worked-example-L1` said L1' transfer was "open"~~ — **LANDED.** Updated to cite Prop B.7 (observable-$C$ with five-way gating under facilitator monotonicity) and the Cramér-Rao refutation for unobservable-$C$ single-channel; three repair routes named.
- ~~**F19** — `#section-ii-survival` bias bound in entropy form~~ — **LANDED.** Replaced with MI form from `#observation-ambiguity-modulation`; triple-zero boundary structure made explicit (bias vanishes at $\kappa=0$ OR $\mathcal{A}=0$ OR factually-sharp observation, not just the first).
- ~~**F20** — KL-direction degeneracy in `#strategy-complexity-cost` variational form~~ — **LANDED as strengthening** (not softening). New appendix segment **#strategy-cost-regret-bound** hosts the full derivation: TV bound via bounded value range, Pinsker-KL bound, direction-forcing argument (forward-KL is vacuous under deterministic $\pi^\ast$), admissible-divergence family analysis (TV tight but non-differentiable; reverse-KL canonical-not-unique on gradient-tractability + variational-inference + Fisher-geometry + MDL-coding grounds), and the linear-vs-square-root $\beta_\Sigma$ trade-off (linear preserves IB-shape alignment; square-root would give $\beta_\Sigma \propto V_{\max}$ global naturalization). Segment-level cross-refs updated in `#compression-operations`, `#exploit-explore-deliberate`, `#ciy-unified-objective`. `msc/spike-f20-kl-direction-strengthening.md` retained as the reasoning trail only; framework is complete without it.
- ~~**F21** — `#identifiability-floor` frontmatter status conflicts with internal text~~ — **LANDED.** Frontmatter `status:` changed to `discussion-grade`; Epistemic Status rewritten to cleanly separate the meta-pattern (discussion-grade presentational principle) from individual instances (F1's no-go: *exact* for shallow / *robust qualitative* for general; F13's L1' refutation: *exact*).

## Active — 2026-04-23 triple audit findings and session-discovered proposals

**10 consolidated findings** from three independent de novo audits (Codex 5 + Gemini 4 + Opus 6, with cross-audit overlap on 5 of them). Full detail in `msc/pending-findings-2026-04-23.md`. Summary table:

| # | Finding | Source(s) | Severity | Subsumption |
|---|---------|-----------|----------|-------------|
| 22 | README-level scope framing outruns Section II exact theorem scope | Codex 1 + Gemini 4 partial | High | Partial by O-BP8 + SP-7 |
| 23 | "16/24 exact survival" headline compresses three distinct layer-claims | Codex 2 | High | Partial by C-BP1 |
| 24 | Strategy-edge semantics not harmonized with identifiability machinery; DAG-forced framing overclaims | Codex 3 + Opus F + Gemini 2 | High | msc/spike-edge-semantics-resolution.md "causal efficacy credence" framing is the integration target |
| 25 | `#coupled-diagnostic-framework` slides from defined to runtime-computable | Codex 4 | High | Directly by C-BP1 |
| 26 | Section III composition-closure reads more closed than self-aware status supports; Tier 3 prevalence not characterized | Codex 5 + Gemini 1 + Opus D | Medium-high | SP-6 (composition-closure consolidation) |
| 27 | Scalar tempo overcounting — foundational metric structurally additive | Gemini 3 | (already caveated; retained for visibility) | Partial by O-BP3 |
| 28 | $\rho_\Sigma$ is unmeasurable threshold parameter on which trajectory guarantee depends | Opus A | High (gap); medium (substantive vs. honest-open) | None — genuinely unaddressed |
| 29 | Update-rule heterogeneity integration debt in `#unity-dimensions` | Opus B | High (pure integration debt) | None — mechanical work |
| 30 | Stacked scope narrowings (Class 1 + learning-agent) only Class 1 visible at OUTLINE | Opus C | High | Directly by O-BP8 |
| 31 | Orient cascade 4c's signal-to-noise sensitivity not surfaced where step prescribed | Opus E | Medium | None — 30min editorial fix |

**7 session-discovered architectural proposals** (SP-2 through SP-8) in `_obs/architectural-proposals-2026-04-22.md` §"Post-2026-04-23-audit architectural extensions":

- ~~**SP-2** — Additive-coordinate-forcing meta-pattern, 5-instance (not 3).~~ **LANDED 2026-04-23** as `#additive-coordinate-forcing` meta-segment (`01-aad-core/src/additive-coordinate-forcing.md`, `type: discussion`, `status: discussion-grade`). The 5-instance conjecture was tested and narrowed to a **1-anchor-plus-2-theorem** characterization: chain layer is a mathematical identity (not a Cauchy-FE theorem); divergence and update layers are the two theorems conditional on AAD-internally-motivated axioms. Lyapunov and IB Lagrangian classified as *adjacent family members* with explicit reasoning (Lyapunov coordinate matched not forced; IB adopted from external theorem not re-derived). Cross-refs added in instance and adjacent segments. SP-1 entry in proposals doc was silently truncated; it has been replaced with a promotion pointer.
- **SP-3** — Calibration-laboratory template as prescription. Generalize #software-epistemic-properties' transfer-assumption table to a `domain-instantiation-template.md` for all domains.
- **SP-4** — Agent identity elevation from scope to architectural postulate: "AAD is a theory of token-level adaptation under causal embedding, not type-level agent populations."
- **SP-5** — Two-tier "Reader's Path" presentation. Short load-bearing preamble per segment, preceding the formal apparatus.
- **SP-6** — Composition-closure consolidation pass. Scope bridge lemma explicitly to linear-Gaussian + exponential-family cases; adopt "AAD-shaped reduction" as the honest general claim. Repairs F26.
- **SP-7** — Epistemic architecture as the framework's distinctive contribution. All three audits converge on this reframe: AAD's value is in how it organizes scope, not in which results it integrates. Partially closes F22; composes with SP-3, SP-4, O-BP10, O-BP8 as the framework-reframing cluster.
- **SP-8** — Dual-edged identifiability-floor + separability-pattern reading. Both meta-segments present the positive half (strengthened machinery); foreground the negative half (bounded reach) equally.

**Convergent big-picture reframe** (Codex + Gemini + Opus): move the framework's center of mass from "integration of four disciplines" to "organization-of-scope under a master principle" — Codex's "bounded correction under decomposed disturbance," Gemini's "thermodynamics of purposeful systems with coupling as primary geometric variable," Opus's "epistemic architecture as distinctive contribution." These are not the same proposal but they are on the same axis.

### Actionable from the audit batch

- **F29** (unity-dimensions two-axis integration) — **pure mechanical work**, 45–90 min. Should land first in next session as a confidence-building cleanup.
- **F31** (orient cascade 4c sensitivity note) — 30 min editorial. Small cleanup.
- **F25** (coupled-diagnostic-framework runtime vs. analytical) — 60–90 min editorial *or* wait for C-BP1 landing and handle together.
- **F30** (OUTLINE scope lattice) — 20–40 min editorial; composes naturally with O-BP8 if Phase C framing pass is pursued.

### Requires scoping or substantive work

- **F22 + SP-7** — README + CLAUDE.md + OUTLINE preamble rewrite as a coordinated framing pass. 1–2 sessions. Incorporates the convergent big-picture reframe.
- **F24** — Promote `msc/spike-edge-semantics-resolution.md`'s "causal efficacy credence" framing to segments; soften `#strategy-dag`'s "DAG-forced" language; foreground causal sufficiency as scope condition. 1 session.
- **F26 + SP-6** — Composition-closure consolidation pass. 2–3 sessions + optional scoping spike.
- **F28** ($\rho_\Sigma$) — Strengthen-first spike attempting to derive $\rho_\Sigma$ from observable quantities; honest scope-narrowing fallback if strengthening fails. 1–2 sessions.
- **F23** — "16/24 exact survival" per-layer breakdown. Coordinate with C-BP1 three-layer separation to avoid redoing work. 1 session.

### Supersedes prior planning

~~SP-2 supersedes the three-instance meta-segment promotion (Phase B in the prior recommended sequence).~~ **Phase B is closed.** The meta-segment landed with honest 3-primary + 2-adjacent characterization. Future extensions on this axis live in `#additive-coordinate-forcing` Working Notes (candidate future layers at credit-assignment, composition-closure-defect, shared-intent compression; each would require its own AAD-internal axiom + Cauchy-FE derivation).

SP-7 + SP-3 together partially fulfill Phase C (framing pass), which is now deepened rather than replaced — the OUTLINE/CLAUDE.md rewrite should incorporate the convergent reframe at the same time as it adds the scope lattice (O-BP8) and the template-as-organizing-principle (O-BP1) content.


## Recommendations for next session (updated post-2026-04-24 Gemini pressure-point cycle)

**2026-04-24 Tier 1 landing is the immediate next work.** See `## Active — Pending-Review Spikes (2026-04-24 Gemini pressure-point cycle)` §"Tier 1 landing plan" above. Six bundled items across `#strategy-cost-regret-bound`, `#composition-closure`, `#contraction-template`, `#sector-condition-derivation`, `#information-bottleneck`, `#loop-interventional-access`, plus one new appendix `#bias-bound-derivation`. All items are elementary / textbook-grade; none requires new machinery.

Sections below are prior recommendations from earlier cycles; consult once the 2026-04-24 Tier 1 is complete.

---

What follows is one agent's prioritization after the 2026-04-23 audit. Joseph's call which to follow.

### Session gains (what landed; refresh of session character)

The 2026-04-22/23 cycle ran Phases 1–5 + 7 of the proposed sequence, plus two unplanned in-flight strengthening spikes surfaced during the work. Nine commits delivered:

- **Three new uniqueness theorems**, each forcing a logarithmic coordinate via a Cauchy-functional-equation argument on an AAD-internally-motivated additivity axiom: (i) F20 regret-bound derivation (reverse-KL direction forced); (ii) reverse-KL chain-rule uniqueness (Csiszár 1991 / Shore-Johnson 1980 / Hobson 1969, under chain-rule-additivity axiom); (iii) evidential-additivity uniqueness of log-odds (Aczél 1966 Cauchy-functional-equation argument, under evidential-additivity axiom).
- **Discovered structural pattern** — the three theorems share a common shape. Documented as SP-1 during the cycle; **promoted to `#additive-coordinate-forcing` meta-segment 2026-04-23** with honest 1-anchor-plus-2-theorem characterization (chain layer = mathematical identity; divergence, update = theorems conditional on AAD-internal additivity axioms; Lyapunov + IB Lagrangian classified as adjacent family members with explicit reasoning).
- **Scope partitions sharpened.** A2' α/β sub-scope (Kalman/conjugate-Bayesian/gradient-strongly-convex = α derived; PID/rule-based/human-judgment = β assumed). Prop A.1S region condition lifted via stopping-time localization (Khasminskii 2012).
- **Three new meta-segments or promotions.** `#separability-pattern` (positive-half complement to `#identifiability-floor`, six ladders enumerated); `#agent-identity` promoted to formal scope (type: scope, status: robust-qualitative); `#edge-update-natural-parameter` (uniqueness theorem + scope condition).
- **O-BP14 derivation-table convention** landed in `FORMAT.md` with tables applied to five derivation segments.
- **C-BP3 TST reframing** as calibration laboratory with transfer-assumption table.
- **Citation audit** ran on the reverse-KL uniqueness work: three wrong attributions (Csiszár 1972 / Amari 2009 Theorem 1 / Amari-Cichocki 2010 Prop 3.2 — none contain the chain-rule uniqueness theorem) corrected to Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980 / Aczél-Daróczy 1975 with PDFs saved to `ref/`. Eguchi 1983 venue corrected. Three-layer-pattern discovery now rests on defensible citations.

Segment count: 93 → 96 (added `#identifiability-floor` before this cycle; `#strategy-cost-regret-bound`, `#separability-pattern`, `#edge-update-natural-parameter` this cycle). Stage distribution: ~13 claims-verified, ~23 deps-verified, ~59 draft.

### Recommended sequence for next session (updated 2026-04-23)

**Phase α — Quick wins first (1 session total).** Confidence-builders and pure integration debts:
- **F29** — `#unity-dimensions` two-axis integration (45–90 min). Pure mechanical work landing `msc/spike-unity-closure-mapping.md`'s Option C into Formal Expression.
- **F31** — `#orient-cascade` step 4c practical-sensitivity note (30 min).
- **F21-follow-up / F24** — Promote `msc/spike-edge-semantics-resolution.md`'s "causal efficacy credence" framing to `#strategy-dag`; soften "DAG-forced" language to match `#graph-structure-uniqueness`'s sufficiency-only content (1 session).

**Phase A — CLOSED 2026-04-23.** Project-wide citation audit completed across 3 commits (`7456ec3`, `6567914`, `f61e62f`). Zero confirmed attribution errors. 26 PDFs in `ref/`. 5 missing-citation gaps hardened. See §"Citations Audit — COMPLETE 2026-04-23" above for detail.

**Phase B — CLOSED 2026-04-23.** The `#additive-coordinate-forcing` meta-segment landed with the honest 1-anchor-plus-2-theorem characterization. Opus's 5-instance conjecture was tested and narrowed: Lyapunov and IB Lagrangian are documented as *adjacent family members* rather than primary instances, with explicit reasoning (Lyapunov's quadratic coordinate is a formulation choice matched to the sector condition, not forced by it; IB is adopted from Tishby-Pereira-Bialek 1999 as applied external theorem rather than re-derived under AAD-internal axioms). Cross-refs added in five home segments; SP-1 entry in proposals doc promoted from truncated-table to promotion-pointer.

**Phase C — Coordinated framing + reframe pass (PARTIAL 2026-04-23; 1-2 sessions remaining).** Part 1 landed in commit `7456ec3`: CLAUDE.md §7 expanded from "Honesty as architectural principle" to "Epistemic architecture as AAD's distinctive contribution" with the convergent Codex/Gemini/Opus reframe and the seven elements of AAD's epistemic architecture explicitly named; `01-aad-core/OUTLINE.md` acquired a new "Reading AAD" paragraph framing the theory at both integration and distinctive levels with the three meta-segments as cross-sectional structure.

**Part 2 (remaining) — segment-level moves:**
- **SP-7** (epistemic architecture foregrounding): README.md public-facing reframe incorporating the convergent audit observation. Partially closes F22.
- **O-BP10** (projection-contraction slogan): "adaptive system = projection whose contraction exceeds target's drift." Promote to segment-level content in `#sector-persistence-template` or a new organizing-principle segment.
- **O-BP1** (template as organizing principle): OUTLINE preambles get refreshed framing around disturbance decomposition at scales. Composes with O-BP10 and the additive-coordinate-forcing meta-segment.
- **O-BP8** (explicit scope lattice): name the adaptive → agency → learning-purposeful → Class-1-modular → coupled/logogenic lattice once as a scope-lattice segment or canonical paragraph in `#scope-condition`. Closes F16 and F30.
- **SP-3** (calibration-laboratory template generalization): write `domain-instantiation-template.md` or FORMAT.md section prescribing the transfer-assumption table format. Composes with O-BP8.
- **SP-4** (agent identity to architectural postulate): elevate `#agent-identity` frontmatter from scope to postulate; rewrite Formal Expression to state the commitment ("AAD is a theory of token-level adaptation under causal embedding, not type-level agent populations").

Estimated 1-2 sessions for Part 2. Tracked as task #8.

**Phase D — Composition-closure consolidation (SP-6; 2–3 sessions).** Repairs F26. Scope the bridge lemma explicitly to linear-Gaussian + exponential-family Tier-1 cases; adopt "composite agents are AAD agents iff effective dynamics admit an AAD-shaped reduction" as the honest general claim. Scoping spike valuable first. Downstream of Phase A (citation audit; especially on `#composition-closure`'s Khalil/Khasminskii citations).

**Phase E — Substantive spikes (choose by priority):**
- **F28 strengthening spike** ($\rho_\Sigma$ operationalization, 1–2 sessions). Attempt to derive $\rho_\Sigma$ from observable quantities; honest scope-narrowing fallback if strengthening fails. Addresses the deepest substantive finding in this audit batch.
- **O-BP11 observability master-variable falsification spike** (deepest structural insight from the earlier cycle; not yet attempted).
- **Phase 2.5 B.5d uniqueness spike** (potential additional instance of SP-2 pattern).
- **Phase 9 C-BP1 + C-BP4 epistemic separation** (three-layer separation + claim-level statuses; partially addresses F23 and F25; composes with O-BP14 tables).

**Phase F — SP-5 "Reader's Path" two-tier presentation (1–4 sessions).** After Phase C framing pass stabilizes. Short load-bearing preamble per segment; incremental application.

**Phase G — SP-8 dual-edged floor/separability reading (1 session).** Framing touch on `#identifiability-floor` + `#separability-pattern`. Composes with SP-7.

### What to defer

- **G-BP3 (Fisher-information unification)** — large multi-session rewrite. Gemini's Riemannian-manifold reaffirmation strengthened the case but did not change the scoping cost. G-BP1 partial execution (Path B uniqueness theorem landed) reduces the remaining G-BP3 scope somewhat.
- **G-BP2 V-strong** (full reformulation as variational free energy) — paper-writing-time decision per `msc/spike-active-inference-vs-aad.md` §I action 5. Not theoretical-development work.
- **O-BP4, O-BP5, O-BP15, O-BP16** — substantial structural work each.
- **O-BP12 (resource budget $B_t$)** — interesting but piecewise treatment currently works.
- **O-BP13 (Cox-necessity)** — worth a 1–2 session spike but not high-priority.
- **Full Props B.1–B.7 restatement in log-odds** — the G-BP1 spike showed this is not required for Finding 2 (Fisher-equivalent in moment parameters). Deferred to a future G-BP3 Fisher-unification session.

### Strategic observation (updated)

The 2026-04-22/23 cycle ran at a different depth than the prior cycle. The prior cycle was 3:1 promoting-to-creating (per CLAUDE.md's "convergent depth over generative breadth" principle). This cycle was closer to 2:1 — six framing/consolidation moves (cleanups, O-BP14 tables, C-BP3 calibration lab, C-BP2 separability pattern, O-BP6 identity promotion, citation audit) plus three genuinely-new derivations (F20 regret bound, reverse-KL chain-rule uniqueness, log-odds evidential-additivity uniqueness). The denser output is acceptable because the three new derivations were not independent — they share the Cauchy-functional-equation structure, and discovering the shared structure was itself a consolidation move.

The recommended next session should rebalance toward consolidation: Phase A (citation audit) is pure consolidation; Phase B (three-layer meta-segment) is naming-the-obvious; Phase C (framing pass) is editorial. Phase D opens to substantive structural work only after the consolidation layer is stable.

The pattern becoming visible: AAD's strengthening cycles alternate between *depth* (new theorems) and *breadth-compression* (consolidation and naming). This cycle was depth-heavy; the next should be breadth-compression-heavy. If this alternation continues, it may itself be a project-level discipline worth naming in CLAUDE.md.


## Citations Audit — COMPLETE 2026-04-23

**Result: zero confirmed attribution errors project-wide.** The reverse-KL audit's 3-wrong-out-of-16 rate was a local concentration in that one spike's citations; the broader corpus is clean. Three commits closed the audit project:

- `7456ec3` — SP-2 landing + framing-pass subset (initial SP-1 truncation fix in proposals doc)
- `6567914` — Tier 1 verification: 3 framing refinements + Morozova-Chentsov completion + ref/ rename hygiene
- `f61e62f` — Missing-citation hardening: Tikhonov / Chechik / Doob-Dynkin / Cox / Cramér added

**What was audited.** Four first-pass Explore batches covered every `*[Derived]*`, `*[Proved]*`, and external-theorem citation across 01-aad-core and 02-tst-core. Four follow-up agents with curl-into-ref/ workflow closed the E-verdict backlog. Two PDF-level Tier 1 verification agents confirmed the highest-risk attributions (Bruineberg's "Pearl-blanket vs Friston-blanket" terminology is VERBATIM, with credit to Martin Biehl in footnote 3; Bareinboim CHT = Theorem 1 p.22 of the 2022 ACM Books chapter; Aguilera's FEP-narrow-validity claim exactly matches AAD's usage).

**26 PDFs in `ref/`.** Canonically named (`{author}-{year}-{short}.pdf`). Load-bearing external theorems covered: Khalil 2002, Khasminskii 2012, Nesterov 2004, Pearl 2009, Lauritzen 1996, Spirtes-Glymour-Scheines 2000, Bareinboim 2022, Cover-Thomas 2006 (textbook), Tishby 1999, Chechik 2005, Csiszár 1991, Shore-Johnson 1980, Hobson 1969, Eguchi 1983, Aczél & Daróczy, Ay et al. 2017, all Friston lineage (2010/2013/2017/2019/2023), Da Costa 2020, Sajid 2021, Parr-Pezzulo 2022, Aguilera 2022, Bruineberg 2022, Sun-Firestone 2020, Clark 2013, Wiener 1948, Hafez 2026, Miller 2022. Amari 2009 and Amari-Cichocki 2010 already retained from the reverse-KL audit.

**Framing refinements landed** (commit `6567914`): (1) Eguchi 1983 attribution is now "the differential-geometric framework in Eguchi 1983" not "Eguchi's theorem" (Theorem 3 is about estimator efficiency; the f-divergence/Fisher-metric result is in §2 contrast-function machinery); (2) Sun & Firestone 2020 direction-of-inference clarified (they diagnose, AAD responds); (3) Friston 2023 labeled as the path-integral methodological extension; Friston 2019 named as the primary NESS source.

**Missing-citation hardening landed** (commit `f61e62f`): Tikhonov 1952 + Khalil 2002 Ch 11 (singular perturbation) to `#temporal-nesting` and `#multi-timescale-stability`; Chechik 2005 full citation to `#compression-operations`; Kallenberg 2002 footnote in `#recursive-update-derivation` (Doob-Dynkin); Cox 1946 + Jaynes 2003 in `#graph-structure-uniqueness` and `#strategy-dag`; Cramér 1946 in `#identifiability-floor` and `#strategic-dynamics-derivation`.

**Spike-to-segment promotion fix** (commit `6567914`): Morozova & Chentsov 1991 citation completed in `#strategy-cost-regret-bound` §6.2 by importing the full form from `msc/spike-reverse-kl-uniqueness.md` ("Markov invariant geometry on state manifolds," *Itogi Nauki i Tekhniki*, translated in *J. Sov. Math.* 56(5):2648-2669).

**Residue (acceptable):** 3 emphasis-vulnerable linter warnings in `#strategic-dynamics-derivation` on dense table-row math (lines 346, 501, 507) — fixing requires math restructuring that exceeds citation-hardening scope. Miller 2022 `Ex_Machina` specific chapter/section/table loci (§3.3, Ch 1, Table 12.2) not independently PDF-verified; book is in `ref/miller-2022-ex-machina.pdf` if a future spot-check is desired.


## Active — Strategic Architectural Proposals

**See [`PROPOSALS.md`](PROPOSALS.md) at the repository root.** The 2026-04-22/23/24 portfolio was consolidated 2026-04-24 from 33 enumerated proposals into a banded, verified structure with cross-cutting bundles (framework-face reframe; Section III completion), ~6 newly-surfaced candidates from segment Working Notes, and per-proposal independence-of-execution markers. The prior portfolio doc is in `_obs/architectural-proposals-2026-04-22.md` for provenance.

**Top-of-file pointers for immediate decision-making:**

- **Bundle 1 — Framework-face reframe** (SP-7 + O-BP1 + O-BP10 + O-BP8 + SP-3 + SP-4 + SP-8). Highest-leverage single move: **+9 framework / +10 paper**. 2–3 coordinated sessions. README still reads integration-first; segment-level infrastructure already landed. See PROPOSALS.md §Cross-cutting view.
- **Bundle 2 — Section III completion** (O-BP16 + O-BP9 + SP-6-residue + SP-11 + SP-17). Closes all four named Section III OUTLINE GAPs + F26 + F8. **+7 framework completeness.** 6–10 sessions as a program; SP-11 (newly-surfaced meta-segment) is the shortest entry point.
- **Ready-now independent items:** O-BP13 (Cox-necessity win/win theorem spike), C-BP1+C-BP4 bundle (epistemic separation framework), SP-14 (channel-capacity notation), O-BP15 (comprehensive worked example — soon after Bundle 1 stabilizes).

The larger reorganizations (O-BP11 observability-master, O-BP12 resource-budget, O-BP13 Cox-necessity, O-BP15 comprehensive-worked-example, O-BP16 population-Lyapunov, G-BP2 V-strong, G-BP3 Fisher-unification, O-BP3 continuous-tiering, O-BP4 continuous-DAG, O-BP5 recursive-AAD, O-BP2 four-compressions full) remain longer-term scoping work. **O-BP11 (observability as master variable) deserves first attention among these** as the deepest available structural insight — even if not pursued, the scoping spike would surface what AAD's observability machinery actually is across the theory.


## Active — Pending Findings

The 2026-04-22 batch had 15 findings; the strengthening cycle resolved 4 directly and resolves several others through subsumption. Updated table below; see `msc/pending-findings-2026-04-22.md` for the original characterizations.

### 2026-04-22 batch — current status

| # | Finding | Status |
|---|---------|--------|
| 1 | L0 residual under on-policy execution | **RESOLVED** by strengthening (commit 14a6095): no-go theorem in #causal-insufficiency-detection |
| 2 | Unbounded gradient in credit-assignment signal | **RESOLVED** by G-BP1 scoping + partial execution (`msc/spike-gbp1-logit-scoping.md`): Path B evidential-additivity uniqueness theorem landed in new appendix segment #edge-update-natural-parameter (parallel to reverse-KL uniqueness under chain-rule axiom); #credit-assignment-boundary default signal function restated in log-odds (domain = ℝ, no mechanical break); #strategy-dag and #edge-update-via-gain carry parallel-presentation notes; #strategic-dynamics-derivation Props B.1-B.7 retained in moment-parameter form (Fisher-equivalent). Full G-BP1 sweep deferred; current scope narrow + strengthened |
| 3 | Degenerate MI in strategy IB objective | **RESOLVED** by V-medium G-BP2 (commit a14682e): KL-form replaces Shannon-MI in #strategy-complexity-cost |
| 4 | Section II silent scope narrowing (agency → learning) | Open. 45–60 min reconciliation. Coordinate with Finding 9 for combined Section II preamble pass (or absorb both into O-BP1 framing pass) |
| 5 | Loop framing overstates Level 2 access | **RESOLVED** by O-BP6 identity promotion (commit 2980327): #agent-identity now a formal scope statement (type: scope, status: robust-qualitative); #loop-interventional-access depends on it and carries an explicit singular-trajectory-ground paragraph. F5 closed end-to-end |
| 6 | Composition timescale heuristic outruns bridge conditions | Open. 30–45 min scope-narrowing in #composition-consistency |
| 7 | TST overstates git as complete chronica | **RESOLVED** by strengthening (commit b6134c2): per-quantity exactness audit + conditional maximality + $\mathcal{C}_t^{\text{commit}}$ in #software-epistemic-properties |
| 8 | (C-iii) mutual-benefit vs (A1) decomposable $G_c$ gap | Open. 45–60 min scope-reconciliation; involves Joseph's Option A vs Option B decision |
| 9 | Section II preamble framing understates survival | Open; absorbed if O-BP1 framing pass executed. 30 min standalone |
| 10 | `#information-bottleneck` status mismatches unification role | **RESOLVED** (commit a14682e): status reclassified from discussion-grade to exact (applied external theorem) |
| 11 | Orient cascade step 4c convergence in non-stationary envs | **PARTIALLY RESOLVED** by F1 strengthening: #causal-insufficiency-detection no-go reframes step 4c as the unique broadly-available diagnostic. Step-4c sanity edit in #orient-cascade itself remains optional cleanup |
| 12 | Section II survival slides from statement-level to operational | Open. Subsumed by C-BP1 (three-layer epistemic separation) |
| 13 | `#strategy-dag` L1-as-default overgeneralizes beyond strict-prerequisite | **RESOLVED** by strengthening (commit 4d050c8): Prop B.7 derives L1' transfer for observable $C$ with five-way gating; refutes unobservable-$C$ via Cramér-Rao floor; #strategy-dag headline + Correlation Hierarchy table updated |
| 14 | `#developer-as-act-agent` exact-status mismatch (human vs AI regimes) | Open. Option A (15–30 min status downgrade) is straightforward regardless of C-BP4 |
| 15 | Software "richest operationalization domain" headline overclaims | **RESOLVED** by C-BP3 calibration-lab reframing (commit d0373fc): #software-epistemic-properties headline rewritten; 02-tst-core/OUTLINE preamble updated; transfer-assumption table makes non-software identification relaxations explicit |

### Actionable now (independent of remaining portfolio decisions)

- **Finding 4 + 9 coordinated pass** — Section II preamble + scope-narrowing. 60–90 min combined; or absorbed by O-BP1.
- **Finding 6** — composition-consistency scope-narrowing. 30–45 min.
- **Finding 8** — (C-iii) Option A vs Option B decision needed before edit.
- **Finding 14 Option A** — `#developer-as-act-agent` status downgrade. 15–30 min.

### 2026-04-22 evening batch — six new findings (all resolved)

Three independent de novo audits (Codex, Gemini, Opus) ran *after* the morning strengthening cycle and surfaced six new findings. The 2026-04-22/23 strengthening cycle resolved all six (F18-F21 in the Phase 1 cleanup commit; F16 partial, F17 partial). Status table:

| # | Finding | Source | Severity | Status |
|---|---------|--------|----------|--------|
| 16 | Section II scope lattice underspecified across segments | Codex F1 (evening) | Medium | Open; subsumed by O-BP8 in future Phase C framing pass |
| 17 | `#coupled-diagnostic-framework` operational-computability overclaim | Codex F4 (evening) | Medium-high | Open; subsumed by C-BP1 three-layer separation (future Phase 9) |
| 18 | `#worked-example-L1` says L1' transfer "open" — STALE after F13 strengthening | Gemini F1 (evening) | Medium | **RESOLVED** (commit 0a772d2): updated with Prop B.7 + Cramér-Rao refutation + three repair routes; facilitator monotonicity surfaced as load-bearing |
| 19 | `#section-ii-survival` bias bound in entropy form, stale after 2026-04-21 Finding B | Gemini F3 (evening) | Medium | **RESOLVED** (commit 0a772d2): MI form + triple-zero boundary structure made explicit |
| 20 | KL-direction degeneracy in `#strategy-complexity-cost` variational form (introduced by V-medium) | Opus F1 (evening) | High | **RESOLVED AS STRENGTHENING** (commits 0a772d2, f70fb68, e777f01): new appendix #strategy-cost-regret-bound with regret-bound derivation (direction forced) + chain-rule uniqueness theorem (specific divergence uniquely forced) + corrected citations |
| 21 | `#identifiability-floor` frontmatter status conflicts with internal text | Opus F3 (evening) | Low | **RESOLVED** (commit 0a772d2): status → discussion-grade; Epistemic Status rewritten cleanly separating meta-pattern from instances |

**Reaffirmed (not new):** Codex F2 evening reaffirms F6 (composition timescale heuristic); Codex F3 evening reaffirms F8 ((C-iii) gap); Opus F2 evening reaffirms F14 (developer-as-act-agent status). Several other candidate findings were *rescinded* by the audits themselves on in-segment counterevidence — see `msc/pending-findings-2026-04-22.md` and the audit transcripts for the transparency tables.

### 2026-04-21 batch — both RESOLVED 2026-04-22 (historical, from earlier in the day)

Finding A (composition-closure temporal coarse-graining) and Finding B (observation-ambiguity-modulation architecture-contamination) — both closed in the morning's audit-trio commits before the strengthening cycle. See `msc/pending-findings-2026-04-21.md` for the closed-out resolution notes.


## Active — Tier-C Deferrals

- **$G_t$ as single object; $(O_t, \Sigma_t)$ as a property** (Opus 2026-04-21 synthesis §7). Touches Section II scaffolding. **Defer until more Class 2 logogenic work lands.** Strengthened by O-BP2 (compressions-as-projections); if O-BP2 is pursued, this item converges with it.
- **Continuous convention hierarchy** $N_r \in [1, \infty]$ (Opus 2026-04-21 synthesis §8). Subsumed by O-BP3 (continuous-parameter tiering) — handled there if O-BP3 is pursued.


## Active — Genuinely Open MEDIUM Items

- **Composition scaling with $N$.** Whether closure defect scales polynomially or exponentially with team size. **Scoping spike done** (`msc/spike-composition-scaling-N.md`, 2026-04-22): four readings identified, five candidate first moves, two composing axes ($K_c$ macro-timescale; unity × update-heterogeneity). Question is well-framed but unresolved; execution deferred. Critical for large-team applications.

- **Multi-timescale stability formalization.** `#multi-timescale-stability` is stage `sketch`; `#temporal-nesting` leans on it. Needs formal $N$-timescale singular perturbation treatment. Partially overlaps with the 2026-04-21 Finding A repair path if Option 2 (Tikhonov) is later chosen.

- **Communication-gain adversarial scope.** `#communication-gain`'s additive model fails for deception (trust is game-theoretic). Either extend or add explicit scope limitation.

- **Exploit/Explore/Deliberate spike findings.** `#exploit-explore-deliberate` was written, but the adversarial spike (`msc/spike-three-way-tradeoff.md`) noted that the two-stage decomposition and $\Delta V_\Sigma$ approximation are hand-waving. Segment may be substantially rewritten. The 2026-04-22 AI integration added an EFE pragmatic/epistemic + sophisticated-inference cross-reference; the rewrite question remains.

- **Adjacent identifiability floors** (`#identifiability-floor` §"Adjacent Floors", added 2026-04-22). Three open extensions: (1) causal-IB for interventional relevance variables (Wieczorek-Roth 2017 and follow-ups); (2) misspecification-cost quantification under finite information budget; (3) tier-switching policy cost. Each is a candidate scoping spike. Overlaps with O-BP7 (known structural absences) — both surface from the same observation that the theory has gaps in its tier-switching/misspecification machinery.

- **V-strong G-BP2 — paper-writing-time decision.** Whether to ever present AAD as a control-theoretic specialization of active inference. The V-medium move keeps both options open. Per `msc/spike-active-inference-vs-aad.md` §I action 5, defer to the right rhetorical moment.


## Active — Missing Segments

### AAD Core (`01-aad-core/`)

| Slug | Section | Type | Description |
|------|---------|------|-------------|
| `adversarial-edge-targeting` | III | Derived? | Which strategy edges most valuable to attack — the Section III gap |
| `intent-dag-development` | A | Aside | Convergence history of AND/OR + single-$p$ (archaeological record) |
| `worked-example-cam` | A | Worked example | Coevolving automata (Miller 2022): AAD ↔ Moore machine mapping, meta-machine as $\varepsilon^\ast = 0$ composition. Planned in `#composition-closure` Discussion. |

### Section III — Composition Dynamics gaps (from Miller + Hafez integration)

- Latent structural diversity
- Endogenous coupling — $\gamma$ as function of population composition
- Composition transition dynamics (Miller 2022 extreme-transition motif)
- Computational thresholds for social behavior (Miller 2022 ICE framework)
- Agent opacity (Hafez et al. 2026 backward predictive uncertainty $H_b$)


## Active — Presentation

- **Three-way presentation split.** All reviewers recommend: (a) core results, (b) conditional architecture, (c) empirical programs. Single highest-leverage presentation change. Not yet executed.

- **AAD-vs-AI introductory positioning.** Per `msc/spike-active-inference-vs-aad.md` §I action 2: when a paper draft is being prepared, surface the §C distinctive-claims and §D refusals at the introductory level (CLAUDE.md, OUTLINE.md preambles). The 2026-04-22 segment-level integration sets the foundation; introductory-level surfacing is the paper-writing-time follow-through. Three underclaim moves named: persistence template's broader validity (Aguilera 2022 contrast); directed-separation as Pearl-blanket conservative form (Bruineberg 2022 contrast); satisfaction-gap as decision-theory content (Sun & Firestone 2020 dark-room contrast).

- **Prior-art positioning synthesis.** Active inference / FEP / POMDP / BDI relationships now in individual segments (substantially expanded 2026-04-22). A synthesis pass that surfaces the pattern across segments may still be valuable.


## Active — Naming Discipline (paused pre-pilot 2026-04-24)

**Status: paused mid-workstream.** Round 1 of a distributed multi-agent naming-sweep is complete but not landed. Before running Round 2 — and before executing any rename decisions from Round 1 — we're piloting a **role-prefix discipline** on a narrow set of specific renames, and after that pilot we'll rewrite the principles file incorporating the converging insights from all 10 Round-1 agents and rerun Round 1 with the refined instructions.

### What exists (artifacts)

- `msc/naming-principles.md` — shared principles + voting format + instructions given to all Round-1 agents.
- `msc/naming-brainstorm-2026-04-24.md` — the original single-agent brainstorm that seeded the work (one agent's voice; preserved as historical reference).
- `msc/naming-votes/*.md` — 10 Round-1 vote files: `agent1-original-brainstorm.md`, `opus-1m.md`, `opus-4-7.md`, `opus-4-7-b.md`, `sonnet-4-6.md`, `haiku-4-5.md`, `codex-1.md`, `codex-2.md`, `gemini-1.md`, `gemini-2.md`. ~1,073 total vote rows across 7 model architectures (Claude ×5, Codex ×2, Gemini ×2).
- `msc/naming-alias-clusters-codex-2.md`, `msc/naming-cleanup-scan-codex-2.md` — supplementary analyses from Codex-2 (not vote files; human-judgment overlays).
- `bin/naming-aggregate.rb` — Ruby aggregation script. Parses vote tables, sums weights per `(current, candidate)` pair, emits three formats:
  - `--format=review` (grouped by current-name, tallies + notes);
  - `--format=round2` (blind input for Round 2, tallies withheld, notes retained);
  - `--format=json` (machine-readable).
  Handles multi-table files with repeated headers (for resumed-append incremental files), deduplicates exact-match rows silently, flags near-duplicate current-names, warns on weight-conflicts.
- `msc/naming-aggregate-{review,round2,votes.json}` — aggregated outputs from Round 1.

### Why paused

The Round-1 outputs surface a set of converging insights that suggest the principles file is significantly under-specified relative to what agents actually needed. Rather than run Round 2 on the current principles and compound the mismatch, we're pausing to refine. Key converging insights across agents, worth folding in before Round 2:

1. **Weight scale too coarse.** The +1 / +3 / −1 granularity collapses "acceptable keep" and "load-bearing keep" into the same bucket. Multiple agents (haiku, opus-4-7-b) explicitly flagged this; others drifted to `+2` informally. Round 2 should include `+2`.
2. **Greek-vocabulary commitment is implicit but undocumented.** Chronica, prolepsis, aisthesis, aporia, epistrophe, praxis, logogenic, logozoetic form a coherent aesthetic-epistemic commitment that no one stated as principle. Four agents (agent1, opus-1m, opus-4-7-b, gemini-2) flagged this independently. Making it explicit would help future agents extend consistently.
3. **Scope-honesty should dominate memorability for meta-segment names specifically.** The `#additive-coordinate-forcing → #cauchy-coordinates` vs `#forced-coordinates` decision — memorability loses to scope-honesty because the Čencov 4th instance isn't Cauchy-FE. Principle worth calling out by case.
4. **Canonicalize vs. keep vs. rename are three distinct moves.** The principles conflate "keep status quo" with "keep, and now canonicalize — stop paraphrasing, reference by this name." Deserves its own weight category or flag.
5. **Name-unnamed-thing ≠ rename.** Proposing a name for a currently-paraphrased recurring pattern is architecturally different from renaming an established segment. Both currently share the vote format.
6. **Symbol-to-English parity is a third category.** Adding an English alias alongside a symbol (α₁ → derived-gain regime) is neither rename nor keep — it's "add alias." May deserve its own notation.
7. **Cold-start instruction must be the first paragraph of the principles file.** Opus-4-7-b openly disclosed accidental contamination from `git status` showing a modified brainstorm file. The instruction needs to fire before agents start any orientation reading.
8. **Subject-noun preference for slug naming.** Name segments by the *thing* they define, not by the *role* the segment plays. `#scope-condition` → `#adaptive-system` is the canonical case. Round 1 surfaced this via Sonnet-4-6's "objects over proof-devices" observation; Joseph confirmed as general principle.
9. **Acronym discipline underspecified.** Multiple agents flagged that every new acronym carries cost; no principle governs when adding one is worth it.
10. **Three / four naming layers need explicit governance.** Formal slugs / prose defaults for symbols / framing-posture vocabulary / public-API headers. Friction comes from mixing these.
11. **"Renamed-from-now-sounds-weird" test.** Opus-4-7-b's implicit criterion: imagine the project six months from now; does the old name sound quaint or does the new name sound forced? Worth making explicit.

### The role-prefix discipline (proposed, not yet ratified)

Emerging from Joseph's own read of Round 1 + opus-1m's subject-noun conversation: rename segments to use `{role-type}-{subject-noun}` pattern, using FORMAT.md's existing type vocabulary. This front-loads the segment's epistemic character in the slug itself, which is read repeatedly in cross-references across the repo. Examples:

- `#scope-condition` → `#scope-adaptive-system`
- `#composition-scope-condition` → `#scope-composite-agent`
- `#agent-identity` → `#scope-agent-identity`
- `#composition-consistency` → `#postulate-composition-consistency`
- `#sector-condition-stability` → `#result-sector-condition-stability`
- `#mismatch-dynamics` → `#hypothesis-mismatch-dynamics`
- `#mismatch-decomposition` → `#result-mismatch-decomposition`
- `#graph-structure-uniqueness` → `#derivation-strategy-dag-sufficiency`
- `#recursive-update` → `#derivation-recursive-update` (or `#result-recursive-update` depending on claim-type)

Type prefix vocabulary (from FORMAT.md): `#scope-`, `#definition-`, `#postulate-`, `#derivation-`, `#derived-`, `#result-`, `#formulation-`, `#hypothesis-`, `#discussion-`, `#sketch-`, `#empirical-`, `#observation-`.

### Pilot plan

Before cascading to all ~130 slugs, pilot the prefix discipline on a narrow set of specific renames that were already surfacing from Round 1 as consensus moves. Specifically:

- `#scope-condition` → `#scope-adaptive-system`
- `#composition-scope-condition` → `#scope-composite-agent`
- `#developer-as-act-agent` → `#scope-human-developer-agent` (also resolves the `-act-agent` relic)
- `#ai-agent-as-act-agent` → `#scope-logogenic-agent` (also resolves the `-act-agent` relic; also resolves the "ai-agent is not a taxonomy rung" issue)
- Possibly `#separability-pattern` → `#discussion-separability-ladder` (compound move: prefix + Round-1 consensus rename)
- Possibly `#additive-coordinate-forcing` → `#discussion-forced-coordinates` (same)
- Possibly `#identifiability-floor` → `#discussion-identifiability-floor` (pure prefix; name already strong)

Pilot goal: see how role-prefix reads in context across the repo (dependency declarations, OUTLINE tables, segment cross-references, prose citations). If it reads well, cascade to the remaining ~120 slugs as a coordinated pass. If it reads awkwardly, retreat to unprefixed slugs and absorb the lessons.

### Post-pilot plan

Assuming the pilot validates the approach:

1. **Refine `msc/naming-principles.md`** based on (a) all 11 insights above, (b) the role-prefix discipline as an invariant (not a vote target — the prefix is architectural), (c) clarify "canonicalize" as a distinct move from "keep", (d) make the Greek-vocabulary commitment explicit as a preference principle, (e) move cold-start instruction to the first paragraph, (f) name `+2` explicitly and spell out weight bands, (g) separate name-unnamed-thing from rename categories in the format, (h) add subject-noun preference as principle, (i) flag the "renamed-from-now-sounds-weird" test.
2. **Rerun Round 1 cold-start with the refined principles.** 5–8 fresh agents across architectures; same cold-start discipline; instructions note that prefix is invariant and only the subject-noun is vote-target-able.
3. **Quick "import anything of unique value from the original Round 1"** — before aggregating the new Round 1, scan the existing 10 vote files for proposals that the new batch might not have surfaced (deeper unnamed-pattern discoveries, edge-case rejections, etc.) and add them to the new aggregation as supplementary items.
4. **Aggregate, then run Round 2** (blind, using the existing `bin/naming-aggregate.rb --format=round2`).
5. **Collision audit** on the top finalists after Round 2 (per earlier discussion — web search for external conflicts à la the ACT → AI Consciousness Test precedent that forced the 2026-04-16 rename).
6. **Final judgment pass and landing.**

### Known deferred items that will resume after the pilot

- **The `aad-agent` vs `adaptive-agent` split for `-act-agent` destination slugs** — resolved by the taxonomy-conformant rename to `#scope-human-developer-agent` and `#scope-logogenic-agent` (neither of the original options). Pilot will validate; no longer an open vote.
- **The `ASF` vs `Agentic Systems Framework` umbrella naming** — surfaced in Round 1 but voted under incomplete framing (agents thought "Agentic Systems Framework" was debt rather than the intentional parent-level name). Defer to post-pilot Round 1 with correct framing: "ASF is the umbrella; AAD is Part I; TST is Part II; etc. Do you want to rename the umbrella, change the acronym, or keep?"
- **The converging Round-1 consensus renames** (`#equilibrium-composition`, `#separability-ladder`, `#forced-coordinates`, symbol-to-English α-regime names, `persistence envelope` and other unnamed-thing proposals) will re-surface in the refined Round 1 under the subject-noun + role-prefix discipline. Not pre-deciding; let the refined vote reconfirm.

### Resume trigger

This workstream resumes when the pilot rename pass lands cleanly and we have confidence in the role-prefix discipline reading well in the repo. Post-pilot, the principles rewrite is the next piece of work; then refined Round 1; then aggregation + Round 2 + collision audit + landing.


## Active — Editorial Hygiene

- **Spike-to-segment reverse-check.** Standing Gate 2 check per `FORMAT.md`: "What did the spike establish that the segment does not say?" — added in Session C.5 of 2026-04-21 cycle; verify it's still present and visible.

- **Segment counts in CLAUDE.md "What's Settled" summary** — refreshed 2026-04-22 (post-strengthening): now 93 AAD core segments. Refresh opportunistically.


## Active — Promotion Pipeline

**Current state (2026-04-22, post-strengthening):** 93 AAD core segments. Several segments reset to `draft` for re-review after the strengthening cycle: `#causal-insufficiency-detection` (full rewrite), `#strategy-dag` (Correlation Hierarchy substantially reworked), `#strategic-dynamics-derivation` (new Prop B.7), `#information-bottleneck` (status upgrade + VFE cross-ref), `#directed-separation` (Bruineberg integration), `#satisfaction-gap`/`#control-regret` (EFE-collapse contrast), `#strategy-complexity-cost` (V-medium variational form), `#compression-operations` (variational + hierarchical-generative-model credit), `#sector-persistence-template` (Aguilera contrast), `#loop-interventional-access` (honest-credit + identifiability-floor cross-ref).

The new `#identifiability-floor` segment is at `draft`; it would benefit from a Gate 1 dependency audit on the next promotion pass.

Recommended next promotion candidates remain the ones from the prior round: `#sector-condition-derivation`, `#recursive-update-derivation`, `#mismatch-decomposition`, `#chain-confidence-decay`, `#persistence-condition`, `#gain-sector-bridge`, `#worked-example-kalman`, `#discrete-sector-condition`, `#graph-structure-uniqueness`. (`#satisfaction-gap` and `#control-regret` were on this list pre-strengthening; they are now back at draft after the EFE-contrast addition and need re-promotion.)


## Active — Lower Priority

- **Observability-dominance product formula.** $\text{conf}_{\text{obs}} = \text{conf} \cdot \text{obs}$ posited, not derived. Label as formulation choice or derive.
- **Strategic calibration aggregation.** $L^2$ norm unjustified. Label as design choice.
- **Scope architecture.** "Within AAD's scope" ambiguous between adaptive and agency scope.
- **`loop-interventional-access` status.** "exact" defensible; opening claim could be softened. (Note: AI integration sharpened the distinctive-AAD-moves framing 2026-04-22.)
- **Between-event dynamics.** $g_M(M_\tau)$ defined but unreferenced. Important for logogenic agents.
- **Fully coupled adversarial dynamics.** Both agents' mismatch co-evolving. Open.
- **`objective-functional` labeling.** "axiomatic" for scalar-comparability is a formulation choice.
- **Heavy-tailed disturbances.** Model S assumes finite second moment.
- **`satisfaction-gap`/`control-regret` convention-dependence.** "exact" but convention-relative diagnostics. Add note to Epistemic Status. (Note: EFE-contrast was added 2026-04-22; convention-dependence note not yet.)
- **External validation design.** Testable predictions not yet tested. Candidates: git data, RL bandits, adaptive controllers.


## Deferred — Project Structure

- Root-level assembly index (when content beyond AAD warrants it)
- `framework/` directory for non-mathematical content
- Multiple index support (paper, preprint, monograph)
- Section IV standalone paper outline (draft at `msc/2026-03-14-section-iv-paper-outline.md`)


## Deferred — Tooling

- `lint-md` directory arguments


## Archive — Work landed

Detailed historical items moved out of the active list. Kept here so that future agents can find what was done.

### 2026-04-22/23 strengthening cycle — COMPLETE (commits `0a772d2`, `c1d9fcf`, `2980327`, `f70fb68`, `80b40d2`, `d0373fc`, `72ca532`, `e777f01`, `a39dfb7`)

Nine commits delivering six proposal executions, three Cauchy-functional-equation uniqueness theorems, and one citation-audit cleanup. The cycle's distinctive pattern: three independent strengthenings all forced logarithmic coordinates via Cauchy-functional-equation arguments, which on retrospect comprise a three-layer additive-decomposition pattern (documented as §SP-1 in `_obs/architectural-proposals-2026-04-22.md`).

- **Phase 1 cleanups (F18-F21) + F20 regret-bound strengthening** (commit `0a772d2`). F18 (worked-example-L1 stale L1' open claim), F19 (section-ii-survival entropy→MI bias bound), F21 (identifiability-floor frontmatter). F20 strengthened as regret-bound derivation: the π*-first KL direction is forced because forward-KL is vacuous under deterministic π*. New appendix segment `#strategy-cost-regret-bound`.
- **Phase 2: O-BP14 derivation-table convention** (commit `c1d9fcf`). FORMAT.md convention + tables applied to 5 derivation segments. Surfaced A2' α/β ambiguity (→ A2' strengthening spike) and B.5d minimal-scheme claim (parked Phase 2.5).
- **Phase 3: O-BP6 identity promotion** (commit `2980327`). `#agent-identity` promoted to type:scope/status:robust-qualitative with three explicit consequences. Closes F5.
- **Reverse-KL uniqueness theorem** (commit `f70fb68`, citations corrected in `e777f01`). Under the chain-rule additivity axiom (Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980 / Aczél-Daróczy 1975), reverse-KL is uniquely forced within the direction-forced f-divergence family. Axiom AAD-internally motivated as divergence-level analog of #chain-confidence-decay. Concrete χ² counterexample exhibited.
- **A2' strengthening** (commit `80b40d2`). Sub-scope partition α (A2' derived) vs β (A2' assumed). Prop A.1S region condition lifted via stopping-time localization (Khasminskii 2012). Sub-scope label inherited by sector-persistence-template instances.
- **Phase 4: C-BP3 calibration laboratory** (commit `d0373fc`). TST reframed as "privileged high-identifiability calibration laboratory" with transfer-assumption table for five AAD-core quantities. Closes F15.
- **Phase 7: C-BP2 separability pattern** (commit `72ca532`). New meta-segment `#separability-pattern` (six ladders enumerated; positive-half complement to `#identifiability-floor`). Three-part meta-segment family: #independence-audit + #approximation-tiering + #separability-pattern.
- **Citation audit of reverse-KL work** (commit `e777f01`). Three wrong attributions corrected (Csiszár 1972, Amari 2009 Theorem 1, Amari-Cichocki 2010 Prop 3.2 do not contain the claimed chain-rule uniqueness theorem); Eguchi 1983 venue corrected. Audit trail preserved in-segment. Three PDFs saved to `ref/`.
- **Phase 5: G-BP1 logit scoping — partial execution** (commit `a39dfb7`). Third Cauchy-functional-equation uniqueness theorem: under the evidential-additivity axiom (Bayesian independent-evidence updates add in a fixed coordinate), log-odds is uniquely forced up to positive affine. Axiom AAD-internally motivated as update-level analog of #chain-confidence-decay. New appendix segment `#edge-update-natural-parameter`. Finding 2 (unbounded gradient mechanical break in #credit-assignment-boundary) resolved by restating default signal in log-odds (domain ℝ, no mechanical break). Props B.1-B.7 retained in moment-parameter form (Fisher-equivalent); full restatement deferred to future G-BP3.
- **New meta-pattern discovered** (cascaded observation, commit `a39dfb7` and prior). Three independent uniqueness theorems (chain-confidence-decay, reverse-KL, log-odds) share structural shape: Cauchy-functional-equation argument on an AAD-internally-motivated additivity axiom forces logarithmic coordinates. Documented as §SP-1 in `_obs/architectural-proposals-2026-04-22.md`; candidate for promotion to explicit meta-segment (`#additive-decomposition-pattern`) in a future session.

### 2026-04-22 strengthening cycle — COMPLETE (commits `14a6095`, `b6134c2`, `4d050c8`, `b91493c`, `a14682e`)

Followed Joseph's strengthen-first-before-soften posture (`feedback_strengthen_before_soften.md`): for each finding with a softening repair on file, attempted the strengthening first; only fell back to softening if strengthening failed. Outcomes:

- **F1 — strengthening succeeded.** No-go theorem: under purely on-policy execution with sequential short-circuit, no detection mechanism can distinguish an L0-insufficient world from an L0-sufficient world matched on regime conditionals. Tier: *exact* for shallow strict-prerequisite cases; *robust qualitative* for general DAG topology. Five boundary routes characterized. The covariance test under joint sibling observability is now the unique broadly-available violation of the no-go's scope — sharpening the load-bearing role of `#loop-interventional-access`. Predecessor softening repair retained as historical fallback.

- **F7 — strengthening succeeded.** Per-quantity exactness audit: ~14 AAD-relevant estimators in three blocks (TST operational, causal-discovery substrate, multi-agent observable structure) are exact functions of $\mathcal{C}_t^{\text{commit}}$. Conditional maximality: under cryptographic immutability, cryptographic authorship, standard universal retrieval, and mainline-bounded scope, $\mathcal{C}_t^{\text{commit}}$ is the unique maximal exteriorized subset of $\mathcal{C}_t$. Estimator-of-AAD-quantity bias separated as a third Consequence clause. $\mathcal{C}_t^{\text{commit}}$ added to NOTATION.md.

- **F10 — strengthening (status upgrade).** `#information-bottleneck` reclassified from `discussion-grade` to `exact` (applied external theorem: Tishby, Pereira & Bialek 1999), with three-paragraph Epistemic Status rewrite naming the AAD binding ($X = \mathcal{C}_t$, $T = M_t$, $Y =$ future-obs) and the Markov-chain factorization holding by construction.

- **F13 — strengthening succeeded for observable-$C$; refuted for unobservable-$C$.** New Prop B.7 in `#strategic-dynamics-derivation` derives the L1' sector transfer with five-way gating $\alpha_{L1'} = \min(1/(n_C+1), \min_j \theta_C \pi_{j\mid C}/(n_{j\mid C}+1), \min_j (1-\theta_C)\pi_{j\mid \neg C}/(n_{j\mid \neg C}+1))$ under observable common cause and facilitator monotonicity. Reduces correctly to B.6 in the strict-prerequisite limit. The unobservable-$C$ single-channel case is *refuted* by the Cramér-Rao floor (Fisher information matrix is rank 1 with factorization $\mathcal{F} = uu^T/(\mu\bar\mu)$ where $u = (\Delta_j, \theta_C, 1-\theta_C)$). Repair routes: augment $C$-observability, run multi-child joint observation, or fall back to plan-level marginal tracking. `#strategy-dag` Correlation Hierarchy extended to four rows.

- **New meta-segment `#identifiability-floor`.** Names the emerging pattern of structural no-go results in AAD — limits derived from external information-theoretic theorems (Pearl/Bareinboim CHT for F1; Cramér-Rao for F13). Three adjacent open extensions surfaced: causal-IB for interventional relevance, misspecification-cost quantification, tier-switching policy cost.

- **AI integration pass (Phases A–D).** Implemented the AAD-vs-Active-Inference positioning spike's §H Overlap+Underclaim findings:
  - Phase A: G-BP2 V-medium executed — variational form replaces Shannon-MI in `#strategy-complexity-cost` (closes Gemini Finding 2/3); related cross-refs in `#compression-operations`, `#exploit-explore-deliberate`, `#ciy-unified-objective`.
  - Phase B: Honest credit to action-perception-loop framing (Friston 2017, Parr & Pezzulo 2022, Wiener 1948, Conant & Ashby 1970) in `#loop-interventional-access` with three distinctive AAD moves named; honest credit to hierarchical-generative-model lineage (Friston 2008/2010, Clark 2013, Hohwy 2013) in `#compression-operations` with three structural additions named.
  - Phase C: Aguilera 2022 FEP-flow narrowing contrast in `#sector-persistence-template`; Bruineberg 2022 Pearl-blanket vs Friston-blanket distinction in `#directed-separation` (AAD as conservative form); Sun & Firestone 2020 dark-room contrast in `#satisfaction-gap`/`#control-regret`.
  - Phase D: VFE accuracy-complexity equivalence in `#information-bottleneck` (Friston 2010/2017, Parr & Pezzulo 2022, Tishby & Zaslavsky 2015).

### 2026-04-22 audit-trio + Codex round-2 cycle — COMPLETE (commits before strengthening)

The morning's audit trio (Gemini, Codex round-1, Opus) and the afternoon Codex round-2 audit produced the 15-finding pending list and 14 architectural proposals (`_obs/architectural-proposals-2026-04-22.md`). The strengthening cycle resolved 4 directly + 3 partially + 1 by V-medium G-BP2; remaining are listed in the Pending Findings section above.

### 2026-04-21 audit cycle — COMPLETE (commits `6d3f219`, `98179f9`, `70c306d`, `ba2597c`, `499afa3`, `1c3a2d9`, `853888c`)

Session plan derived from `msc/opus-audit-2026-04-21.md`. Summary of what landed:

- **Session A** — `#sector-persistence-template` factored out as shared lemma; six persistence-flavored segments re-expressed as template instances. Four honesty fixes.
- **Session B** — `#graph-structure-uniqueness` reframed as Cox-analog; two new meta-segments: `#independence-audit` and `#approximation-tiering`.
- **Session C** — Scope gates in `#composition-closure`, `#unity-dimensions` lead rewritten, `#software-epistemic-properties` P1 codebase-vs-environment scoping, `section-ii-survival` statement-level-vs-operational distinction, FORMAT.md promotion-workflow reverse-check.
- **Session D** — Scoping spike `msc/spike-ib-unification-plan.md` delivered; execution absorbed into `#compression-operations` segment with three integration edits.
- **Late-cycle Gemini batch** — L1 soft-facilitator gap handled; Finding A and Finding B (composition-closure temporal coarse-graining; observation-ambiguity-modulation architecture-contamination) both closed 2026-04-22.

### 2026-04-02 Codex round-2 findings — COMPLETE

All numbered items from the round-2 review resolved in segments. Full history in `msc/analysis-2026-04-02-round2.md`.

### 2026-03-13 consolidated review — mostly COMPLETE

Top issues (1) directed-separation architectural classification, (2) $\alpha$-vs-$\mathcal{T}$ distinction, (3) composition-closure bridge lemma, (4) graph uniqueness at theorem strength, (6) assorted formal issues — all landed. Remaining: (5) `#causal-discovery-from-git` now written; TST overstatement of causal status of git data is covered within that segment.
