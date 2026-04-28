# TODO — Open Work Items

**Last reconciled:** 2026-04-25 (cleanup-cycle archival pass; landed F11/F31, F25, F29 editorial repairs in commits `7e2e074`, `aa1fb15`; consolidated 2026-04-25 mechanical-fix bundle, 2026-04-22/23 Phase 1 cleanups, and 2026-04-23 citations audit into §Archive). New `CHANGELOG.md` is the forward-going cycle record (replacing LOG.md for entries from 2026-04-24 onward). This file is the living action list.

**Cycle history (most recent first).**
- **2026-04-24 Gemini pressure-point cycle — Tier 1 landing** (commits `6102a93`, `b76ee67`). Six Tier 1 items landed: (1) `#deriv-strategy-cost-regret-bound` bundled update — §4 BH identity $D_{\mathrm{KL}} = -\log(1 - \mathrm{TV})$ replaces Pinsker as primary bound with matching lower bound; §5 asymmetry-from-one-sidedness paragraph; §6.1 Shore-Johnson/Sanov/Hobson structural-equivalence note; §6.3 Bregman-Fenchel identification; §6.4 information-theoretic-MDP lineage positioning with AAD-outlier-on-KL-direction ownership + Rubin 2012 PAC-Bayesian motivation; Bishop-vs-AAD naming-collision footnote. (2) Structural-transparency lift — `#form-composition-closure` DA2'-inc ≡ (CT2)-at-$M=I$ equivalence with Rockafellar-Wets citation; `#result-contraction-template` honest-failure-modes adversarial three-obstruction convergence; `#deriv-sector-condition` rule-based/discontinuous sub-scope-β as structural Lipschitz-floor scope-exit with van der Schaft-Schumacher 2000 reference. (3) New appendix `#deriv-bias-bound` — Track 1 transport-inequality + Track 2 Fisher-Rao + Attempt E no-go + failed-attempt record + Gaussian worked example; updates `#scope-observation-ambiguity-modulation` and `#result-section-ii-survival` from "order-of-magnitude guidance" to "conditional theorem." (4) `#form-information-bottleneck` IB-lineage vs. information-theoretic-MDP-lineage cross-reference. (5) `#der-loop-interventional-access` "Modes of deployment across `#disc-identifiability-floor` instances" subsection (Mode 1 agent-self-intervention / Mode 2 observer-on-sub-agent; positions for Mode 3 when I4 lands). (6) `ref/INDEX.md` TP2011 title correction ("The Information Theory of Decision and Action" singular) — also done in reasoning-trail commit. Lint clean: 0 ordering violations, 0 missing deps, 0 orphans. **Net effect:** Gemini pressure points #1 (bridge lemma), #2 (IB purity), #5 (constant $C$) closed outright at Tier 1; #3 (ρ factorization) and #4 (neutral drift) await Tier 2 landings.
- **2026-04-24 Gemini pressure-point cycle — reasoning trail** (commit `6102a93`). External Gemini audit via `msc/joseph-working-notes.md` flagged five pressure points: (#1) composition bridge lemma — contraction assumption verified only for linear Kalman-type; (#2) IB purity — Shannon-zero / Forward-KL-infinity / reverse-KL fix framed as "abandoned IB purity"; (#3) multiplicative ρ factorization failed; (#4) neutral-drift blindness — agent state space only sees $(\alpha, \rho, R)$; (#5) missing constant $C$ in bias bound. Five parallel strengthening spikes launched (skipping #6 directed-separation-fails-for-LLMs as known structural scope-exit), four follow-up spikes launched on cross-cutting issues. **Headline outcomes:** (1) Bridge lemma **partially addressed** by post-2026-04-23 `#result-contraction-template` landing — DA2'-inc ≡ (CT2)-at-$M=I$ equivalence shows Euclidean metric-α₁ was AAD-internally-derived all along (structural transparency); passivity/dissipativity route with Class 1/2/3 port-structure reading of `#der-directed-separation`; iISS global lift for Tier 2M; two sharp no-gos (non-smooth Lipschitz floor; adversarial three-obstruction convergence). (2) IB purity **mischaracterization refuted**: Path 5 **Bretagnolle-Huber identity** (under deterministic $\pi^*$, $D_{\mathrm{KL}} = -\log(1 - \mathrm{TV})$ exactly — strictly sharper than Pinsker); Path 7 Fenchel-Bregman (reverse-KL is Bregman divergence of negative-entropy; log-odds is Fenchel-dual natural coordinate); Path 6 asymmetry forced by regret's one-sidedness (second leg of direction-forcing independent of chain-rule axiom); Path 1 **PDF-verified and reframed**: "reverse-KL IS IB" demoted per TP2011/Rubin 2012/Levine 2018 page-by-page verification; AAD is outlier on KL direction (all three lineage frameworks put agent-first, reference-second; AAD's optimum-first is forced by regret-bound). Bonus from PDFs: Rubin 2012 Theorem 3 PAC-Bayesian generalization bound — fourth independent motivation for KL-to-reference form. (3) **(AV) variance-additive decomposition** derivable as theorem under (S1)-(S4) via information-geometric Pythagorean projection; three sub-regimes where multiplicative is native (Poisson cascade MC; large-deviation tail LD; small-$\Delta$ / PID). (AV) classified as adjacent to `#disc-additive-coordinate-forcing` (Bienaymé's identity, not Cauchy-FE). (4) **Neutral-drift gap narrower than framed** post-2026-04-23; `#der-agent-opacity` + `#der-interaction-channel-classification` + `#disc-identifiability-floor` Instance 3 together address most of it; candidate **Instance 4** (agent-internal architecture layer) with dual CHT-at-agent-as-SCM + Kalman-Ho canonical-form anchoring; $\gamma$ estimable from cross-covariance in matched-symmetric-Tier-1 scope. (5) **Two bias-bound theorem tracks**: Track 1 transport-inequality $C_{W_2}^2 = 2L_{\mathrm{post}}^2/\rho_{\mathrm{LSI}}$ linear in $I$ (Otto-Villani under LSI + Stuart 2010 Lipschitz-posterior); Track 2 Fisher-Rao $C_{FR} = \sqrt{2}$ universal dimension-free under (PI)+Čencov + small-$I$; Attempt E no-go (universal-$C$ under Euclidean-parameter norm fails) **justifies (PI) as load-bearing**, not coincidental. **Follow-up outcomes:** (i) **Instance-4 triage** — 4 candidates → 2 genuine new primary instances (I4 agent-internal; I5 mechanism-design under broad reading with honest theorem-family labeling) + 1 sub-statement (Candidate 1 ρ-factorization projects onto I4 at disturbance-statistic layer) + 1 redirect (Candidate 3 constant-$C$ is downstream theorem of `#disc-additive-coordinate-forcing` 4th instance, not floor instance — fails E4 single-escape criterion); three-layer `#der-loop-interventional-access` chain real at pattern level but non-uniform at mechanism level (agent-self / observer-on-subagent / observer-on-agent-input). (ii) **Fenchel-Bregman reframe** — Path 7 duality verified exact; stronger framing emerges: *one geometric object (exponential-family Legendre-Fenchel on categorical distributions) + four independently-motivated AAD-internal axioms converging on it + four segment manifestations*, richer than both naive Path-7 reframe and current 1-anchor-plus-3-theorem. Bonus: classifies the 4-candidate Instance-4 jam by Bregman geometry (ρ-factorization lives on squared-norm Bregman — parallel meta-pattern; coupling/constant-$C$ fall outside). (iii) **KL-to-state-distance template extraction** — Option B recommended: narrow `#posterior-displacement-template` on Otto-Villani+Lipschitz-posterior cascade with `#deriv-bias-bound` as primary instance + 3 forward-looking clients (causal-IB, misspecification-cost, composition-scope-robustness); `#deriv-variational-sector-condition` positioned as adjacent family (Pinsker shared; post-Pinsker cascade not). Contingent on `#deriv-bias-bound` landing first. (iv) **Path 1 PDF-verification extension** (§12 of IB spike, 273 lines appended) — Claim A contradicted at formula level (TP2011's actual quantity is Information-to-Go multi-information, not KL-to-reference form the spike attributed — that's Rubin 2012's); Claims B/C/D partially verified with direction-flip and terminology-collision flags. Bonus: AAD-is-outlier-on-KL-direction observation (forced by regret-bound + Path 5). Title correction: TP2011 = "The Information Theory of Decision and Action" (singular). **Ancillary session work:** naming brainstorm paper (`msc/naming-brainstorm-2026-04-24.md`); four outline ordering violations cleared (two via OUTLINE row moves; two via frontmatter dependency cleanup — `chronica.depends` no longer anticipates `causal-structure`; `value-object.depends` no longer forward-references `causal-hierarchy-requirement`); orient-cascade moved to proper §II position. Nine spike files in `msc/` (five primary + four follow-up); three new PDFs in `ref/` (`tishby-polani-2011-info-decision-action.pdf`, `rubin-2012-trading-value-info-mdps.pdf`, `levine-2018-rl-control-as-inference.pdf`) with INDEX.md entries.
- **2026-04-23 Gemini Gap A/B promotion sequence** (seven commit-scoped landings, not yet committed to git as of session end; awaiting review + commit). Six new segments promoted: **#result-contraction-template** (Appendix A result; B1 metric generalization with 5 α promotions, topology-indexed closures, (CM2-M)); **#deriv-strategic-composition** (Section III derivation; equilibrium-convergence framing with potential/monotone-game A2'-analogs); **#deriv-fisher-whitened-update-rule** (A3 Fisher-whitened under (PI)/Čencov); **#deriv-l1-update-bias** (A2 closed-form bias with Monte Carlo); **#deriv-variational-sector-condition** (B4 ε-fidelity); **#der-agent-opacity** (H_b closing #adversarial-edge-targeting). Four structurally load-bearing additions to existing segments: **Instance 3** (composition-layer no-go via Liberzon 2003) in `#disc-identifiability-floor`; **4th primary instance** (Čencov-invariance at metric layer; 1-anchor-plus-2-theorem → 1-anchor-plus-3-theorem) in `#disc-additive-coordinate-forcing`; **seventh ladder** (A2'-scope via contraction metrics) in `#disc-separability-pattern`; **(C-iv) scope route** (equilibrium-convergent strategic interaction) in `#scope-composite-agent`. (PI) parameterization-invariance axiom added to `#scope-agent-identity` as natural extension of singular-trajectory scope commitment. Monotone-operator-theory lineage explicitly acknowledged in `#result-sector-persistence-template` and `#deriv-sector-condition` (Rockafellar 1970 / Bauschke-Combettes 2017; one-point anchoring / Model D-S decomposition / identifiability-floor composition / composition-consistency / α-β epistemic labeling as AAD-distinctive content). Satellite cross-refs in `#deriv-critical-mass-composition`, `#form-composition-closure`, `#der-loop-interventional-access`, `#der-adversarial-destabilization`, `#der-directed-separation`, `#der-gain-sector-bridge`, `#deriv-edge-update-natural-parameter`, `#der-chain-confidence-decay`. Thirteen spike files retained in `msc/` as reasoning trails.
- **2026-04-23 Gemini Gap A/B parallel-spike cycle** (thirteen spikes written to `msc/`). Twelve parallel research spikes launched against Gemini's two flagged structural gaps, plus one follow-up spike (Jacobian-level B1 strengthening) spawned mid-cycle and completed. (A) default signal function needs validation under correlated failures (L1'/L2); (B) contraction assumptions verified only for linear Kalman-type. **Headline outcomes:** **B1** lifts Section III from linear-Kalman-centric to broadly-nonlinear-cooperative via Lohmiller-Slotine metric + Slotine 2003 compositional theorems (5 α-class promotions, heterogeneous (CM2-M), topology-indexed bridge lemma); **B5** derives Instance 3 of `#disc-identifiability-floor` with closed-form §3.3 counterexample (Liberzon 2003 + Dayawansa-Martin 1999 as external anchors) — B1 + B5 compose as Section III completion with positive/negative halves; **B6** covers partially-opposing $O_t^{(i)}$ via equilibrium-convergence (Monderer-Shapley + Rosen 1965), proposes (C-iv) scope route, provides formal home for the effects spiral; **C1** gives partial unification honestly (2-instance-plus-1-consequence), recasts A2' α/β as Bauschke-Combettes operator-family classification. **Default-signal robustness confirmed** (A3: angle ≤ 45° at any finite ρ; A2: closed-form bias with MC). **F13 Instance 2 confirmed via four independent obstruction routes** (A1/A2/A3/A4) — not a new floor instance but strengthening of the existing one. **Jacobian-level B1 spike (completed mid-cycle) produces a mixed-lift three-layer result that materially changes B1's architectural picture:** (i) **transparency win** — DA2'-inc ≡ (CT2) at $M=I$, so Euclidean metric-α₁ cases are AAD-internally derived without any new axiom (AAD already carries the Jacobian-level condition under the name DA2'-inc); (ii) **parameterization-invariance + Čencov** — adopting a (PI) axiom (natural extension of `#scope-agent-identity`'s token-level commitment) lifts two metric-α₂ cases (Fisher exp-family, info-metric Kalman) to AAD-internally-derived via Čencov 1982 uniqueness, and **candidate fourth primary instance of `#disc-additive-coordinate-forcing`** under broadened "uniqueness-theorem on AAD-internal axiom" discipline; (iii) **remaining three metric-α₂ cases** (Hessian, Lyapunov-linear-Hurwitz, Lyapunov-PID) stay theorem-imported with honest labeling. **The (PI)/Čencov 4th-meta-pattern candidate supersedes C1's operator-sector candidate** as the structurally tighter fourth-meta-pattern move — derives from within AAD's meta-pattern discipline rather than recognizing external mathematical lineage. Thirteen spike files: `msc/spike-l1-evidence-axiom.md`, `-l1-update-bias.md`, `-fisher-whitened-update.md`, `-update-operator-sector.md`, `-contraction-metric-generalization.md`, `-passivity-composition.md`, `-pid-a2prime.md`, `-variational-a2prime.md`, `-composition-no-go.md`, `-strategic-composition.md`, `-operator-sector-unification.md`, `-compositional-coordinate.md`, `-jacobian-b1-strengthening.md`.
- **2026-04-23 brainstorm-cycle promotion sequence** (commits `591e8b6`, `13fe242`, `b48cdee`, `77a9bde`, `0bd859e`). Five promotions landed from the 2026-04-23 brainstorm cycle: `#der-interaction-channel-classification` (recipient-side four-regime theory closing the `#adversarial-edge-targeting` GAP); `#form-consolidation-dynamics` (Section I regime naming with stability-plasticity feasibility window); `#deriv-persistence-cost` (sustained information rate $\dot R \geq n\alpha/2$ with channel-capacity $\geq \mathcal T/2$ prerequisite); `#deriv-adaptive-gain-dynamics` (A2' sub-scope refinement $\alpha_1/\alpha_2/\beta$ via augmented-state Lyapunov); `#deriv-detection-latency` (R1 $\Omega((n_{\min}+1)/\varepsilon)$ bound sharpening forgetting prerequisite). Spike H (ρ-factorization) completed with outcome (C) honest obstruction — the multiplicative factorization $\rho = \rho_{\text{external}} \cdot f(\mathcal M) \cdot g(\pi)$ is NOT derivable; native structure is variance-additive. Segment count: 98 → 103. Spike E (internal-external decomposition) deferred pending variance-additive reframe.
- **2026-04-23 critical-mass composition promotion + brainstorm-spike landing** (commit `0d7b987`). Seven parallel research spikes launched from an external-framework comparison prompt (GAA Baigozin 2025) as a brainstorming exercise. One closed cleanly and promoted: `#deriv-critical-mass-composition` derives the composite sector constant in closed form for the symmetric-matched-Tier-1 dyad, subsuming the weakest-link bound, recovering `#der-team-persistence` and `#der-adversarial-destabilization` as signed special cases, and formalizing `#hyp-symbiogenic-composition` (S-3) as an asymmetric-parameter limit. Cross-segment strengthening to `#form-composition-closure`, `#der-team-persistence`, `#hyp-symbiogenic-composition`, `#result-unity-closure-mapping`, `#result-sector-persistence-template`. Six companion spikes landed in `msc/` ready-for-review (persistence-cost; interaction-channel classification; adaptive-gain dynamics; internal-external decomposition; consolidation dynamics; stability-induced myopia). Segment count: 97 → 98.
- **2026-04-23 SP-2 + citation audit cycle** (three commits: `7456ec3`, `6567914`, `f61e62f`). Executed Tier 1 item 1 (SP-2 meta-segment promotion) + partial Tier 1 item 2 (framing pass — CLAUDE.md §7 + OUTLINE preamble) + full citation audit project-wide. SP-2 landed as `#disc-additive-coordinate-forcing` with the honest 1-anchor-plus-2-theorem characterization after in-flight verification narrowed Opus's 5-instance conjecture. Citation audit ran 4 parallel first-pass batches + 4 follow-up batches + 2 PDF-level Tier 1 verification agents + 1 missing-citation audit; produced 26 verified PDFs in `ref/` and zero confirmed attribution errors project-wide (reverse-KL's 20-25% rate was a local concentration in one spike, not a project-wide pattern). Segment count: 96 → 97.
- **2026-04-23 triple audit** (Codex / Gemini / Opus, post-cycle). 10 consolidated findings (F22–F31) across the three audits plus 7 session-discovered architectural proposals (SP-2 through SP-8, extending SP-1 from the strengthening cycle). ~25% of candidate findings rejected as already-adequately-caveated. See `msc/pending-findings-2026-04-23.md` and `_obs/architectural-proposals-2026-04-22.md` §"Post-2026-04-23-audit architectural extensions."
- **2026-04-22/23 cascading strengthening cycle** (nine commits: `0a772d2`, `c1d9fcf`, `2980327`, `f70fb68`, `80b40d2`, `d0373fc`, `72ca532`, `e777f01`, `a39dfb7`; plus session-close `2fc829b`). Executed Phases 1–5 + 7; landed three Cauchy-functional-equation uniqueness theorems; discovered the three-layer additive-decomposition pattern (SP-1). See Archive for per-commit detail.
- **2026-04-22 strengthening cycle** (commits `14a6095`, `b6134c2`, `4d050c8`, `b91493c`, `a14682e`). Executed strengthen-first repairs for Findings 1, 7, 10, 13 and the AI integration pass.
- **2026-04-22 triple audit (evening)**. Six findings F16–F21 (all resolved by the cascading cycle) plus nine new architectural proposals O-BP8 through O-BP16 (four of which — O-BP14, O-BP6, C-BP3, C-BP2 — landed in the cascading cycle; C-BP3 and C-BP2 were added to the portfolio in the evening batch).

The three audit cycles together mark the transition from finding-driven repair work to consolidation-and-reframing work. See §"Recommendations for next session" below for the post-2026-04-23 recommended ordering.

## Active — README v2 pass (queued from 2026-04-27 first-human-feedback cycle)

The first *human* read of the framework — Alan Walton (CTO Latitude / AI Dungeon; BS Mathematics + Logic minor; ~10y collaboration history with Joseph; runs a 12k-commit production agentic-system architecture), ~4h read window — surfaced that the README missed the mark for casual-curious readers in ways the multi-agent audit cycles had not. Even Alan, who is about as sympathetic and capable a first-human-reviewer as the project will encounter, found the language "extremely academic," fell out of sustained-attention reading by the end of the README, and switched to test-driven Opus-mediated learning to keep engaged. Verbatim review at [`msc/alan-walton-feedback-2026-04-27.md`](msc/alan-walton-feedback-2026-04-27.md).

The README needs another pass that combines this human-feedback signal with the deferrals from the 2026-04-26 doc-pipeline cycle (judgment-calls log at `msc/judgment-calls-readme-cycle-2026-04-26.md`).

### Surfaced from Alan's review

- **Variables α, ρ, R appear without gloss.** Alan: *"I've seen this formula twice now, but still don't know what the variables mean."* First mention of the persistence condition should anchor each variable in plain language; the *Cross-Domain Joining* table (which uses α, ρ, R without re-glossing) and the *Position & Lineage* paragraph (which mentions α > ρ/R as a structural threshold) should both re-anchor briefly. Glossing once at top is not enough across a long document.
- **The "rate of gap-closing proportional to gap" assumption is not surfaced at README level.** Alan correctly identified this as the load-bearing assumption from outside: *"That's the weakest assumption I've seen so far in application, though it's often empirically true."* The README should foreground the linear-ODE / sector-condition assumption explicitly, with one line on how the sector condition generalizes strict linearity (it's the structural assumption AAD spends Section I machinery on, not an embarrassment to bury).
- **Greek cycle terms have retention cost without an English on-ramp.** Alan retrieved the cycle's semantics under his own terms (Prediction / Perception / Comparison / Learning / Action) but none of the Greek (Prolepsis / Aisthesis / Aporia / Epistrophe / Praxis). Decision: keep the Greek (the distinctions matter and English flattens them), *and* pair each with a clean memorable English/engineering anchor at first introduction. Alan's five-word recall is itself a candidate mapping; whether it preserves the distinctions the Greek encodes is worth a careful pass.
- **The About / Position-and-Lineage opening is too clinical for the audience it was written for.** This is the single biggest miss. Bundle 1 framework-face reframe is partially landed; another pass is warranted, this time with the casual-curious tier (not the academic-evaluator tier) as the primary audience. Alan's bathtub gloss of the persistence condition (water = belief-reality gap; faucet = environment change rate; drain = learning rate; bathtub size = model class capacity; overflow when faucet outpaces drain at full) is a ready-made Feynman-criterion explanation that a mathematician-practitioner reconstructed for himself — worth promoting verbatim or near-verbatim into both the README's persistence section and `#result-persistence-condition`'s Findings Brief.
- **Units of α are not visible.** Alan: *"The drain is bits/bits/time or 1/time. I'm not used to thinking of inverse time as units."* Worth a units gloss somewhere — possibly NOTATION.md (canonical), possibly in the README's persistence-condition section (pedagogical), possibly both. (Discussion of where this lives queued for after this TODO entry lands.)
- **Prior-art pointer to investigate: Deutsch's Theory of Explanations.** Alan: *"Have you read The Beginning of Infinity and The Fabric of Reality by David Deutsch? The Theory of Explanations is highly aligned with this work."* Substantive pointer worth a search-log-grade investigation; if confirmed, cite as conceptual precursor / adjacent literature in the relevant Findings (most likely `#disc-additive-coordinate-forcing` or `#disc-identifiability-floor`, given the explanation-quality framing).
- **Consider promoting Alan's "split goal state and model state explicitly in agent context notes" as a TST or logogenic-agents instantiation.** Alan's instinct from running production AI Dungeon agents was the same decomposition the framework names as $G_t = (O_t, \Sigma_t)$ vs $M_t$. This is field-grade convergent-independent confirmation of the central decomposition; worth surfacing as a `02-tst-core/` or `03-logogenic-agents/` instantiation.

### Deferrals from 2026-04-26 doc-pipeline cycle (`msc/judgment-calls-readme-cycle-2026-04-26.md`)

Reconsiderations Joseph flagged for review on return; this README v2 pass is the natural cycle to ledger them through.

- **J-1 — pilot Findings selection.** The six-segment Findings pilot skews toward post-2026-04-22 landings; substituting one or more older "convergent choice" results (e.g., `#der-loop-interventional-access` for the Pearl-hierarchy connection; `#result-sector-condition-stability` for the underlying Lyapunov result) would validate the schema across a wider age range before the sweep.
- **J-2 — Findings schema length.** Some Impact paragraphs (notably `#deriv-bias-bound`, `#result-contraction-template`) ran long; consider a length cap or splitting Impact into two beats (what-it-closes / what-it-unlocks).
- **J-4 — README §4 omissions.** Three of seven elements from CLAUDE-2 §7's epistemic-architecture enumeration were left at segment-level rather than README-level: agent-identity-as-token-level-commitment; derivation-audit tables; A2' sub-scope partition. Re-decide which belong at framing level given the casual-curious-reader retarget.
- **J-5 — non-specialist tone calibration.** Joseph's preference among naive-curious / undergraduate-numerate / post-doc-other-field as the target audience sets the right level for the Findings "Brief" fields and the README §1–§4 prose. Alan's read places the *naive-curious* tier as the right floor — not the only audience, but the audience the framing must reach without losing.
- **J-7 — Known-Issues surfacing depth.** PROPOSALS §B/§C/§D currently surfaces 15 entries; trimming to §B-only with §C/§D summarized would right-size the Known Issues section for the casual-curious target.
- **PROPOSALS Bundle 1 status update.** README rewrite is now landed; several Bundle 1 elements partially addressed; an entry-level status-update on what landed vs what remains is overdue and is a natural part of this cycle's housekeeping.
- **`bin/lint-readme` deferred** (J-15) — slug-existence + cross-reference link validation. Quick-to-write tool; should land before heavy reliance on the pipeline. Independent of the README content pass; can land in parallel.

### Convention to apply

The **Feynman-criterion** aspiration for plain-language briefs (newly stated in `CLAUDE.md` §Working Conventions and `FORMAT.md` §Findings — Brief, 2026-04-27) governs this pass. Alan's bathtub is the canonical worked example. Reach for the analog whose physics is isomorphic to the load-bearing structure, not merely evocative — the test is whether a thoughtful non-specialist can re-derive the qualitative claim from the analog alone.

### Suggested ordering for the cycle

This is a single-cycle pass, not a multi-session arc. Suggested order:
1. Re-do README's *About* / *Position & Lineage* with the casual-curious tier as primary audience (the academic-evaluator tier still has to be served, but not at the cost of the casual reader hitting the limit Alan hit).
2. Anchor variables (α, ρ, R, $\delta_t$, $\eta^*$, $\mathcal T$, $M_t$, $G_t = (O_t, \Sigma_t)$) on first mention with one-line plain-language glosses; re-anchor in the *Cross-Domain Joining* table and any later use.
3. Greek + English pairing for the cycle phases, with the English form chosen to preserve the distinction the Greek encodes (not merely the closest one-word approximation).
4. Surface the linear-ODE / sector-condition assumption as the load-bearing structural assumption, with one line on the sector-condition generalization.
5. Promote Alan's bathtub gloss into `#result-persistence-condition`'s Findings Brief; consider a similar-grade gloss for the persistence section of the README itself.
6. Ledger-style work through judgment-calls J-1 / J-2 / J-4 / J-5 / J-7; update PROPOSALS Bundle 1 status.
7. Investigate the Deutsch / *Theory of Explanations* prior-art pointer; route per FORMAT §Findings — Related Work / Search Log conventions.

`bin/lint-readme` (J-15) and the units-comprehension question (location TBD per the units discussion that follows this TODO entry) can land independently of the main README rewrite cycle.

## Active — Pending-Review Spikes (2026-04-24 Gemini pressure-point cycle)

Nine spikes completed against five Gemini-flagged pressure points plus four cross-cutting follow-ups. All nine respect strengthen-first posture; none softened. Cross-spike convergence productive (see cycle-history entry above). No segment-level changes yet — Tier 1 landing plan drawn up and ready to execute.

### Primary spikes (five flagged pressure points)

| Spike | Location | Status |
|-------|----------|--------|
| Bridge lemma (pressure #1) | `msc/spike-bridge-lemma-nonlinear-strengthening-2026-04-24.md` | **§7.1 minimal → Tier 1**; §7.2 passivity → Tier 2; §7.3 iISS global → Tier 3 |
| IB purity (pressure #2) | `msc/spike-ib-purity-strategy-cost-strengthening-2026-04-24.md` (incl. §12 PDF-verification addendum) | **Path 5 + Path 6 + Path 7 elementary + reframed Path 1 + Path 4 note → Tier 1**; Fenchel meta-segment reframe → Tier 3 |
| ρ-factorization (pressure #3) | `msc/spike-rho-additive-variance-strengthening-2026-04-24.md` | **New `#rho-decomposition` appendix → Tier 2**; no-go Kalman tightening ~1 page → follow-up |
| Neutral drift (pressure #4) | `msc/spike-neutral-drift-endogenous-coupling-strengthening-2026-04-24.md` | **I4 promotion → Tier 2/3** (needs Kalman-Ho closed-form follow-up spike); segment addenda → Tier 2 |
| Constant C (pressure #5) | `msc/spike-bias-bound-constant-C-strengthening-2026-04-24.md` | **New `#deriv-bias-bound` appendix (Track 1 + Track 2 + Attempt E) → Tier 1** |

### Follow-up spikes (cross-cutting)

| Spike | Location | Status |
|-------|----------|--------|
| Instance-4 triage | `msc/spike-identifiability-floor-instance-triage-2026-04-24.md` | **Three-mode `#der-loop-interventional-access` subsection → Tier 1**; I4/I5 promotions → Tier 2/3 |
| Fenchel-Bregman reframe | `msc/spike-fenchel-bregman-reframe-additive-coordinate-forcing-2026-04-24.md` | **Local Bregman-Fenchel identification → Tier 1** (folded into IB bundled update); meta-segment reframe (7 items per §7.3) → Tier 3 architectural proposal |
| KL-to-state-distance template | `msc/spike-kl-to-state-distance-template-extraction-2026-04-24.md` | **Tier 3**: Option B (narrow `#posterior-displacement-template`) contingent on `#deriv-bias-bound` landing + ≥1 forward-looking client materializing |
| Path 1 PDF-verification | Appended §12 to IB spike | **Subsumed into Tier 1** `#deriv-strategy-cost-regret-bound` bundled update (§6.3 new subsection) |

### Tier 1 — LANDED 2026-04-24 (commits `6102a93`, `b76ee67`)

All six items landed. See Archive entry "2026-04-24 Gemini pressure-point Tier 1" and cycle-history bullet at top of file for itemized summary.

### Tier 2 (after Tier 1 lands)

- **Spike 3 `#rho-decomposition`** new appendix — (AV) theorem + sub-regime catalog (MC/LD/PID) + no-go at discussion-grade. Unblocks deferred `#internal-external-decomposition` spike from 2026-04-23 brainstorm cycle.
- **Spike 1 §7.2 `#dissipativity-template`** new appendix + Class 1/2/3 port-structure reading addition to `#der-directed-separation`. Closes heterogeneous Kalman + PID-on-positive-real-plant composition case explicitly.
- **Instance 4 promotion** (agent-internal architecture) — requires **follow-up spike** for Kalman-Ho closed-form no-go construction (~1 page of algebra). Dual-anchored by CHT-at-agent-as-SCM + Kalman-Ho canonical-form non-uniqueness.
- **Instance 5 promotion** (multi-agent-aggregation mechanism-design) — Arrow / Gibbard-Satterthwaite / Myerson-Satterthwaite; broad reading of meta-pattern with honest "implementability vs. identifiability" theorem-family labeling.

### Tier 3 (architectural proposals)

- **`#disc-additive-coordinate-forcing` Fenchel-Bregman reframe**: move from "1-anchor + 3 theorems" to "one geometric object + four independently-motivated axioms converging on it + four segment manifestations." Seven-item rewrite per Fenchel spike §7.3. Preserves axiom-independence while naming geometric convergence. Substantial. **Now tracked as SP-9 in [`PROPOSALS.md`](PROPOSALS.md) §E.3** (wait-gated on Amari-Nagaoka 2000 PDF verification + Bundle 1 framework-face reframe landing first).
- **`#posterior-displacement-template` extraction (Option B)**: narrow template on Otto-Villani + Lipschitz-posterior cascade. Contingent on `#deriv-bias-bound` landing + ≥1 forward-looking client materializing.
- **Spike 1 §7.3 `#iISS-contraction`**: global Tier-2M lift under uniform Jacobian conditioning. Optional; lower urgency than §7.1 / §7.2.

### Follow-up spikes queued

- **Kalman-Ho closed-form for Instance 4** — ~1 page. Gates Instance 4 promotion.
- **ρ-factorization no-go tightening** — ~1 page Kalman algebra for Scenarios A/B counterexample. Gates Instance-4-sub-statement cleanup.
- **Mechanism-design Instance 5 formalization** — under broad reading; clean citations.
- ~~**Fenchel-Bregman reframe architectural proposal write-up**~~ — **DONE 2026-04-24**: landed as SP-9 in [`PROPOSALS.md`](PROPOSALS.md) §E.3.


## Active — Pending-Review Spikes (2026-04-23 brainstorm cycle — five promoted, one deferred)

### Landed in this cycle
Six of the seven brainstorm-cycle spikes have now been promoted. Summary with commit hashes:

- **Spike B → `#deriv-critical-mass-composition`** (appendix-A derivation). Commit `0d7b987`. Closed-form composite sector-constant under symmetric-matched-Tier-1 dyad; subsumes weakest-link bound.
- **Spike C → `#der-interaction-channel-classification`** (Section III derived). Commit `591e8b6`. Four-regime recipient-side theory; closes `#adversarial-edge-targeting` GAP as emitter-side optimizer to recipient-side classifier pairing.
- **Spike F → `#form-consolidation-dynamics`** (Section I formulation). Commit `13fe242`. Regime of $g_M$ with IB-gap-reduction objective; stability-plasticity feasibility window sharpens the asymmetric forgetting-only story.
- **Spike A → `#deriv-persistence-cost`** (appendix-A derivation). Commit `b48cdee`. $\dot R \geq n\alpha/2$ nats/time under Model S + Gaussian-OU; Kalman-Bucy saturates; channel-capacity $\geq \mathcal T/2$ floor.
- **Spike D → `#deriv-adaptive-gain-dynamics`** (appendix-A derivation). Commit `77a9bde`. (MG-1)–(MG-4) meta-gain conditions; augmented-state Lyapunov composition; A2' refined into $\alpha_1$/$\alpha_2$/$\beta$.
- **Spike G → `#deriv-detection-latency`** (appendix-A derivation). Commit `0bd859e`. R1 within-class drift bound $\Omega((n_{\min}+1)/\varepsilon)$ structurally forced by Aczél-FE log-odds; sharpens `#schema-strategy-persistence` forgetting prerequisite.

### Deferred pending reframe

- **Spike E — Internal-external decomposition** (`msc/spike-internal-external-decomposition.md`). **Deferred.** Spike H (ρ-factorization) completed with outcome (C) honest obstruction: the multiplicative factorization $\rho = \rho_{\text{external}} \cdot f(\mathcal M) \cdot g(\pi)$ is NOT derivable from AAD-internal quantities. Native structure is variance-additive $\rho^2 = \rho_{\text{irr}}^2 + \Delta_{\mathcal M}^2 + \Delta_\pi^2 + \text{cross}$; the log-multiplicative form is a small-$\Delta$ Taylor approximation. Impact: coarse decomposition $\mathcal V = \log\lVert\delta_{\text{crit}}\rVert - \log\rho + \log\alpha$ survives at exact tier; fine decomposition needs reframing to variance-additive form; `#disc-identifiability-floor` Instance 3 status survives; `#disc-separability-pattern` seventh-ladder status *strengthened* (structured-repair ring now has concrete mediation-analysis content on cross terms).
  - **Two promotion paths** — choose at next session:
    - **(Path 1, smaller):** Land only the coarse form as a paragraph in `#result-persistence-condition` Discussion noting the internal-external rearrangement on log-scale; develop TST rotation-experiment diagnostic separately (operationalization section). Keep variance-additive reframe in `msc/` pending.
    - **(Path 2, full):** Rewrite Spike E in variance-additive form with explicit cross-term handling (mediation-analysis framework), then promote as appendix segment `#internal-external-decomposition` at *conditional* (sub-scope $\alpha$ + small-$\Delta$ or variance-Pythagorean) / *heuristic* (general) tiers. Requires ~1 session of rewrite work + 1-2 sessions of cross-term derivation.

### Template-augmentation composition (observation)

Spikes B, A, and D together constitute a *template-augmentation triad* under `#result-sector-persistence-template`. Each persistence-flavored segment now inherits:
- a threshold condition (existing template instantiation),
- a cost-rate bound $\dot R \geq n\alpha/2$ via #deriv-persistence-cost,
- a meta-gain contraction condition via #deriv-adaptive-gain-dynamics when the gain itself is adaptive,
- a closed-form critical-mass formula via #deriv-critical-mass-composition for composite instantiations.

This is a candidate meta-segment if the pattern firms up — naming the augmentation structure explicitly. Not yet warranted (four instances across three segments is thin for a meta-segment). Worth flagging and re-visiting after the next strengthening cycle.

### Future spikes opened by this cycle

- **Misspecification-cost formalization** — Regime II-b of `#der-interaction-channel-classification` is a candidate Instance 3 for `#disc-identifiability-floor`'s "Misspecification-cost quantification" open extension. Would sharpen the floor pattern's coverage.
- **Stability-upper-bound derivation for consolidation** — `#form-consolidation-dynamics`'s feasibility window has a well-posed lower bound (existing forgetting prerequisite) but the upper bound's functional form is open. Derivation would tighten the window and sharpen the catastrophic-forgetting scope claim.
- **Channel-capacity as first-class AAD quantity** — biggest architectural opening from `#deriv-persistence-cost`. Lift Shannon capacity $C^{(k)}$ into NOTATION.md and relate to $U_o$ via standard capacity-from-noise transform; connect to the tempo framework. Converts "needs more bandwidth" observations into specific dimensional requirements.
- **$f(H_b^B)$ emitter-side-effect function** — tightens `#der-interaction-channel-classification` §5.2 qualitative opacity-gates-targeting claim into derived form.
- **Variance-additive reframe for Spike E** — prerequisite for Path 2 promotion of internal-external decomposition.
- **EWC tensor-valued gain extension of `#deriv-adaptive-gain-dynamics`** — stability-weighted per-parameter gain per Kirkpatrick et al. 2017. Adapts MG-1-MG-4 to tensor form.


## Active — Pending-Review Spikes (2026-04-23 Gemini Gap A/B cycle)

Twelve parallel research spikes launched against Gemini's two flagged structural gaps. Each self-contained; promotion decisions require independent review before landing in segments. One follow-up spike (Jacobian-level B1 strengthening) is in flight; its outcome affects B1's landing epistemic status.

**The two gaps (from Gemini 2026-04-23 audit):**
- **Gap A** — Section II default signal function (log-odds credit-assignment update via `#deriv-edge-update-natural-parameter`) needs validation under *correlated failures* (L1'/L2 correlation hierarchy).
- **Gap B** — Section III composition contraction assumptions verified only for linear-Kalman-type agents; sub-scope β (PID / rule-based / variational / non-convex-beyond-basin / strategic / heterogeneous) uncovered.

### Completed follow-up (2026-04-23) — affects B1 landing

- **Jacobian-level B1 strengthening** (`msc/spike-jacobian-b1-strengthening.md`). **Completed with mixed-lift three-layer result, not binary.** Spawned mid-cycle after B1 spike surfaced that metric-α₂ derivations are theorem-imports from Lohmiller-Slotine (spike §8.2 item 1; §9 question 1). Outcome structurally changes the B1 landing picture:
  - **Transparency win (Angle 2 clean).** `#form-composition-closure`'s DA2'-inc ≡ Lohmiller-Slotine (CT2) at $M=I$ for $C^1$ $F$ on convex domains (standard Rockafellar-Wets / Nesterov). AAD has been carrying the Jacobian-level Euclidean contraction condition at the composite level all along under the name DA2'-inc. All Euclidean metric-α₁ cases (Kalman-scalar, Euclidean strongly-convex, L2-regularized, linear-PD-symmetric) lift to AAD-internally-derived *without any new axiom*. **This is the under-advertised find — AAD's existing commitment is already stronger than it reads.**
  - **Parameterization-invariance + Čencov (Angle 3) clears the 1-anchor-2-theorem discipline.** Introduce axiom (PI) as extension of `#scope-agent-identity`'s token-level commitment: AAD's predictions should not depend on arbitrary choice of coordinates. Čencov 1982 uniqueness theorem forces Fisher metric uniquely on statistical manifolds under (PI). **Structurally parallel to Cauchy-FE → log-coordinate, but via Čencov-invariance rather than Cauchy-FE.** Promotes **two of five** metric-α₂ cases (Fisher exp-family, information-metric Kalman) to AAD-internally-derived. **Candidate fourth primary instance of `#disc-additive-coordinate-forcing`** — if adopted, broadens the meta-pattern from "Cauchy-FE on additivity axiom → logarithmic coordinate" to "uniqueness theorem on AAD-internal structural axiom → forced geometric coordinate" (Cauchy-FE + Čencov as distinct uniqueness-theorem machinery both clearing the same discipline bar).
  - **Heredity-under-composition-consistency (Angle 1) works but requires architectural commitment.** Agent-level B1 alone is insufficient for composite-level DA2'-inc under parallel composition (rotating-inward counterexample). Under a *heredity* axiom (composite admissibility derivable from sub-agent properties — legitimate AAD-internal extension of `#post-composition-consistency`), agent-level B1* is forced. This is an architectural strengthening of `#post-composition-consistency`, not a uniqueness-theorem-style derivation.
  - **Three of five metric-α₂ cases remain theorem-imported with honest labeling.** Hessian-metric strongly-convex (Hessian chosen to match loss); Lyapunov-metric linear-Hurwitz-non-symmetric (Lyapunov equation from plant); Lyapunov-metric PID-bounded-plant (same); basin-chart non-convex-within-basin (domain-specific). No AAD-internal axiom cleanly forces these metric choices.
  - **Key structural clarification.** The 1-anchor-2-theorem discipline in `#disc-additive-coordinate-forcing` is *broader* than "Cauchy-FE on additivity." Shared core: "uniqueness-theorem-forced coordinate under AAD-internally-motivated axiom." Čencov-invariance instance sits cleanly within this broader reading; Angles 1/2/4/5 sit in adjacent-family territory (converse-Lyapunov / compositional-closure / matched-coordinate mechanisms — AAD-internal but not uniqueness-theorem-forced).
  - **Three landing options (§11).** Minimal (structural transparency note on DA2'-inc ≡ (CT2) + honest labeling in `#result-contraction-template`); moderate (adopt (PI), add fourth primary instance to `#disc-additive-coordinate-forcing`, add B1* to `#der-gain-sector-bridge`); strong (adopt (PI) + heredity, collapse Tier structure, promote (CM2-M) from Slotine-imported to AAD-derived). Choice is architectural, not mathematical — all three are internally consistent.

### Completed (pending review) — Gap A (4 spikes)

| Spike | Location | Outcome |
|-------|----------|---------|
| A1 L1' evidence axiom (block-structured Cauchy FE) | `msc/spike-l1-evidence-axiom.md` | Observable-$C$: $(2K+1)$-dim coordinate forced per-factor Aczél. Unobservable-$C$: Cauchy FE **structurally inconsistent** with Bayesian mixture updates (responsibility reweighting is nonlinear). Classified as *generalization-in-scope* of existing `#deriv-edge-update-natural-parameter`, **not a new theorem in `#disc-additive-coordinate-forcing`**. Unobservable branch converges with F13 Cramér-Rao at same boundary — dual-obstruction confirmation of existing Instance 2, not new instance. Minimal landing: Block Structure subsection in `#deriv-edge-update-natural-parameter`. |
| A2 L1' update bias formula | `msc/spike-l1-update-bias.md` | Closed-form bias $B_k(\rho) = -\iota_k(1-\mu_{\bar k})\rho / [(n_k+1)((1-\mu_1)^2 + (1-\mu_2)^2)]$ at matched-marginal IC. AND-root counterpart (opposite sign). Monte Carlo (400 trials × 5000 cycles) confirms closed form. **L1'-induced biased fixed point**: edges converge to wrong values matching L1' root-prob. Observable-$C$: Prop B.7 eliminates bias exactly. Unobservable-$C$: Cramér-Rao floor $\propto \rho/(1-\lambda)$. **Dual forgetting-rate requirement** derived; admissibility window may be empty → augmentation required. Candidate landing: new appendix `#deriv-l1-update-bias` (quantitative numerical-floor companion to F13). |
| A3 Fisher-whitened edge update | `msc/spike-fisher-whitened-update.md` | **LO-vs-NG angle never exceeds 45° under finite correlation** — B1 is never actively violated, only degraded by factor $\sqrt{1-r^2}$. Fisher whitening **AAD-internally derivable** via two convergent axiom paths: (a) B1-parameterization-invariance; (b) Lyapunov-coordinate-matching via `#disc-additive-coordinate-forcing`'s adjacent-family framework. Both vacuous at L0, force Fisher whitening at L1'/L2. New sub-scope $\alpha_3$ (correlated evidence + Fisher-whitened + Bayesian coherence → A2' derived). Connects to `#deriv-adaptive-gain-dynamics` as meta-gain special case $K_t = \mathcal I^{-1}(\lambda_t)$. Candidate landing: new segment `#deriv-fisher-whitened-update-rule` + touches to `#der-gain-sector-bridge`, `#disc-credit-assignment-boundary`. |
| A4 Update-operator sector condition | `msc/spike-update-operator-sector.md` | (O-A2') operator sector condition derives for the log-odds update with closed-form constant $\alpha_{\text{op}}^{\text{comp}} = \min_k (1/(n_k+1))\iota_k (J_k^2/\|\mathbf J\|^2)\sigma'(\lambda_k^*)$. Sub-scope α/β transfers structurally from `#der-gain-sector-bridge`. Step-size condition lifts for free under Beta-Bernoulli. L1' observable-$C$: graceful degradation; L1' unobservable-$C$: structural break via Fisher-rank-1 (**confirms F13 Instance 2 at operator layer, not a new instance**). Sequential composition is log-additive in $\alpha_{\text{op}}$ — adjacent-family addition at operator-composition layer for `#disc-additive-coordinate-forcing`. Candidate landing: new appendix `#update-operator-sector` (or subsumed into C1's operator-sector-template if that path is taken). |

### Completed (pending review) — Gap B (6 spikes)

| Spike | Location | Outcome |
|-------|----------|---------|
| B1 Contraction-metric generalization | `msc/spike-contraction-metric-generalization.md` | **(CT1)–(CT3) template derived** (Lohmiller-Slotine metric formulation of `#result-sector-persistence-template`). Five α promotions: Kalman info-metric (no $\kappa(P^-)$ penalty), exp-family Fisher-metric, Hessian-metric ill-conditioned, linear-Hurwitz-non-symmetric (new coverage), PID-bounded-plant (β→metric-α₂). Heterogeneous (CM2-M) generalizing matched-symmetric `#deriv-critical-mass-composition`. **Topology-indexed bridge lemma** via Slotine 2003 (parallel / cascade / feedback). Seventh ladder for `#disc-separability-pattern` (A2'-scope → metric-α₁ / metric-α₂ / metric-β). **Honest limit:** metric-α₂ currently *theorem-imported* from Lohmiller-Slotine; Jacobian-level B1 strengthening spike in flight tests whether this becomes AAD-internal. Adversarial composition structurally outside — hands to B6. Candidate landing: new meta-segment `#result-contraction-template` + 8 segment-level edits. |
| B2 Passivity / dissipativity composition | `msc/spike-passivity-composition.md` | AAD sector condition recognized as scalar-SISO-quadratic-storage special case of Willems 1972 dissipativity. Heterogeneous (Kalman + PID-on-positive-real-plant) composition delivers $\mathcal L_2$-stability with composite storage $S = S_1 + S_2$ — reaches Tier-3 heterogeneity that `#deriv-critical-mass-composition` cannot. Port-structure reading of Class 1/2/3 (third axis). PID-on-positive-real-plant → α'' (third independent route, same scope boundary as B3/B1). Candidate landing: new meta-segment `#dissipativity-template` as generalization of `#result-sector-persistence-template`. **Architectural question with B1:** do `#result-contraction-template` and `#dissipativity-template` sit as siblings, or is one the parent? C1 suggests both are instances of operator-sector primitive (strongly-monotone / cocoercive in different inner products). |
| B3 PID A2' derivation | `msc/spike-pid-a2prime.md` | **Classical result recast in AAD form.** SPR condition ↔ B1 directional fidelity; $\alpha_{\text{PID}} = \omega_c \sin(\varphi_m)/\kappa(P)$ with phase margin as sector constant. IMC / lambda / SIMC tuning → α; Ziegler-Nichols aggressive → β. Cascade-PID composition instantiation with timescale-separation bound. Composes with adaptive-gain-dynamics as special case (gain-scheduled PID). PID is the dominant industrial controller — promotion is order-of-magnitude scope expansion in applicable agent population. Candidate landing: minimal (α list refresh in `#deriv-sector-condition`) or full appendix (`#pid-sector-derivation`). |
| B4 Variational approximate A2' | `msc/spike-variational-a2prime.md` | Under $\mathrm{KL}(q\|p) \leq \varepsilon$: **ε-fidelity B1 derived at $O(\sqrt\varepsilon)$ rate (Pinsker-tight)**. Regime A/B structure: sector bound clean on annulus $\mathcal B_R \setminus \mathcal B_{2\delta_0}$; approximation-dominated floor $\delta_0 = O(\sqrt\varepsilon)$. Natural-gradient VI + exp-family recovers FULL α (not ε-degraded). Mean-field VI is workhorse α' case. Amortized VI: errors compose additively. Partition expansion from {α, β} to {α, α', β}. Rule-based / diffusion-posterior / uncontrolled-ε stay β. Candidate landing: new appendix `#deriv-variational-sector-condition` + A2' partition update in `#deriv-sector-condition`. |
| B5 Composition identifiability floor | `msc/spike-composition-no-go.md` | **Instance 3 of `#disc-identifiability-floor` derived** (Liberzon 2003 Theorem 2.1 + Dayawansa-Martin 1999 as external anchor). **Closed-form §3.3 counterexample**: two coupled scalar symmetric-matched-Tier-1 systems with identical marginal component distributions but opposite composite-contraction signs — the single bit of coupling-sign is unidentifiable from component marginals, and that bit is exactly what `#deriv-critical-mass-composition`'s CM2 needs. Load-bearing test §7.1 passes: removing `#deriv-critical-mass-composition` reduces certification to weakest-link bound (blind to coupling sign); removing composite-extended `#der-loop-interventional-access` leaves coupling sign unidentifiable. Three-layer completeness (F1 + F13 + Instance 3). Class-2 merged correctly *rejected* as floor instance (belongs to `#disc-separability-pattern`'s architecture ladder per scope-honesty). Candidate landing: primary = Instance 3 in `#disc-identifiability-floor`; secondary cross-references in `#deriv-critical-mass-composition`, `#der-loop-interventional-access`, `#scope-composite-agent`, `#disc-separability-pattern`. |
| B6 Strategic composition via equilibrium | `msc/spike-strategic-composition.md` | Replaces contraction-to-shared-truth with equilibrium-convergence for partially-opposing $O_t^{(i)}$. **Potential-game A2'-analog** (Monderer-Shapley 1996) exact transfer of `#result-sector-persistence-template` to joint $\nabla\Phi$. **Monotone-game A2'-analog** (Rosen 1965) weighted-norm version. Sub-scope α' (potential/monotone/strongly-monotone derived) vs β' (VI existence only; regret-minimization CCE set-convergence only). Zero-sum scalar worked example fully derived at $\alpha = 1$, $R = 2\sqrt 2$. **Formal home for `#der-adversarial-destabilization`'s effects spiral**: joint-Jacobian eigenvalue condition at candidate equilibria. Strategic composition produces **Class 3 composites from Class 1 sub-agents** — refinement of `#der-directed-separation`. Mechanism-design impossibility (Gibbard-Satterthwaite / Arrow / Myerson-Satterthwaite) flagged as candidate fourth `#disc-identifiability-floor` instance. Candidate landing: new Section III segment `#deriv-strategic-composition` + (C-iv) route in `#scope-composite-agent` + seven additional satellite edits. |

### Completed (pending review) — Cross-cutting (2 spikes)

| Spike | Location | Outcome |
|-------|----------|---------|
| C1 Operator-sector unification | `msc/spike-operator-sector-unification.md` | **Partial unification, honestly reported.** Continuous-time sector template ($\Phi_h$ flow), discrete update map ($T_d$), and composite macro-update ($T_c$) all fit one operator-sector primitive $\langle (I-T)(x), x-x^\ast\rangle \geq \kappa \|x-x^\ast\|^2$ (one-point reduction of Rockafellar / Bauschke-Combettes strong monotonicity). **Coarse-graining projection $\Lambda$ does NOT fit** (heterogeneous spaces, three independent P1/P2/P3 admissibility conditions). Honest picture: **2-instance-plus-1-consequence, not symmetric 3-instance**. Load-bearing gain: **A2'/DA2' α/β recasts as operator-family classification** (α ↔ proximal / firmly-nonexpansive / cocoercive / strongly-monotone-gradient / linear-PD — exactly Bauschke-Combettes classical classes). AAD-distinctive content over monotone-operator theory: one-point anchoring, Model D/S decomposition, identifiability-floor composition, composition-consistency postulate, α/β epistemic labeling — AAD is *specialization + repurposing*, not strict generalization. Pairs naturally with Opus O-BP10 slogan. Candidate landings (three options): R1 new fourth meta-pattern `#operator-sector-template`; R2 minimal segment edits; R3 archive as positional document. |
| C2 Compositional coordinate forcing | `msc/spike-compositional-coordinate.md` | **Honest negative result with structural insight.** Five candidate axioms examined; **no fourth theorem exists at composition layer** in the `#disc-additive-coordinate-forcing` sense. **Structural reason:** Cauchy-FE operates on *functional-form families* (f-divergences, credence reparameterizations); composition-layer quantities present as *coupling-pattern choices*, not functional-form families. `#disc-additive-coordinate-forcing` is architecturally single-agent. Log-closure-deficit along composition tower lands as **fourth *anchor*** (mathematical identity), not fourth theorem — honest framing becomes 2-anchor-plus-2-theorem. Fisher-info / identifiability / communication-tree / composition-tower all corollaries of `#der-chain-confidence-decay` (**unsurfaced Section III reach** — cheap surfacing opportunity). Composition admits its own structural family — **monotonicity-under-composition** (bridge-lemma, Tier 1/2/3, CM4) — candidate future Section III meta-segment, parallel to but NOT reducible to `#disc-additive-coordinate-forcing`. Candidate landing: light Working Note to `#disc-additive-coordinate-forcing`; substantive Discussion to `#der-chain-confidence-decay`; follow-on spike for composition-monotonicity meta-segment. |

### Co-owner landing recommendation (2026-04-23 — EXECUTED; retained below for reasoning trail)

*Joseph authorized promotion; seven commit-scoped landings executed in-session. See cycle-history entry at file top for summary of what landed. The recommendation below is retained as the in-session reasoning record.*



*Framed by field impact, not by effort or low-risk hedging. Revised after the Jacobian-level B1 spike completed — the outcome changes the architectural calculus materially.*

**The picture the Jacobian-level B1 spike reveals.** The B1 landing splits cleanly into three layers rather than landing under a single epistemic label:
1. **Euclidean metric-α₁ cases** (Kalman-scalar, Euclidean strongly-convex, L2-regularized, linear-PD-symmetric) — AAD-internally derived without any new axiom via DA2'-inc ≡ (CT2) at $M=I$. Transparency win: the theory already carries this commitment at the composite level; B1 landing surfaces it at the single-agent level.
2. **Fisher-metric metric-α₂ cases** (Fisher-metric exp-family, information-metric Kalman) — AAD-internally derived *if* the parameterization-invariance axiom (PI) is adopted. Čencov 1982 forces the Fisher metric uniquely under (PI). (PI) extends `#scope-agent-identity`'s token-level commitment AAD-internally. **Candidate fourth primary instance of `#disc-additive-coordinate-forcing`** under a broadened 1-anchor-2-theorem reading (Cauchy-FE and Čencov as distinct uniqueness-theorem machinery both clearing the same AAD-internal-axiom discipline).
3. **Remaining three metric-α₂ cases** (Hessian, Lyapunov-linear-Hurwitz, Lyapunov-PID) — stay theorem-imported with honest labeling. No AAD-internal axiom cleanly forces these metric choices.

**Tier 1 — Section III completion push (B1 + B5 land together, with the three-layer B1 picture).** B1 and B5 remain exact complements; my prior analysis stands. What changes is B1's landing structure: not "metric-α₂ is theorem-imported" flat, but the three-layer split above. Euclidean cases are AAD-internal transparency wins; Fisher cases depend on (PI) adoption decision; remaining cases carry honest theorem-import labels. B5 (Instance 3 composition floor with closed-form §3.3 counterexample) lands unchanged and reframes `#deriv-critical-mass-composition` as the unique broadly-available escape.

**Tier 1 — Strategic composition (B6 lands in parallel).** Unchanged. Covers partially-opposing $O_t^{(i)}$ via potential/monotone games; formal home for the effects spiral; Class-3-from-Class-1-sub-agents refinement of `#der-directed-separation`.

**Tier 1-ARCHITECTURAL DECISION — (PI) axiom adoption.** The Jacobian-level B1 spike surfaces a substantive architectural choice that was previously hidden: whether to adopt (PI) as an AAD axiom.
- *Adoption route.* `#scope-agent-identity`'s token-level commitment already says AAD is about agents on singular causal trajectories. Extending to "AAD's predictions should not depend on arbitrary choice of coordinates" is a natural AAD-internal move. Under (PI), Fisher metric is uniquely forced (Čencov 1982), and Fisher-metric α₂ cases become AAD-internally derived. This also opens the fourth-primary-instance promotion of `#disc-additive-coordinate-forcing` under the broadened "uniqueness-theorem-forced coordinate" reading.
- *Non-adoption route.* Fisher-metric α₂ cases stay theorem-imported like the Hessian / Lyapunov cases. Cleaner but leaves identified structural machinery on the table.
- **Recommendation:** adopt (PI). The axiom is naturally motivated by existing `#scope-agent-identity`, Čencov is an established uniqueness theorem, and the fourth-primary-instance promotion tightens `#disc-additive-coordinate-forcing`'s architectural role. The case is structurally analogous to the chain-rule-additivity and evidential-additivity axioms already adopted at the divergence and update layers — natural-from-adjacent-AAD-commitment and uniqueness-theorem-forced.

**Tier 1-DELIBERATE — revised C1 decision.** My previous recommendation ("do not elevate operator-sector to fourth meta-pattern") now sits alongside an alternative fourth-meta-pattern candidate: the Čencov-invariance-via-(PI) extension of `#disc-additive-coordinate-forcing`. Of the two candidates, **the (PI)/Čencov extension is the stronger fourth-meta-pattern move** because it derives from within AAD's existing meta-pattern discipline (uniqueness theorems on AAD-internal axioms) rather than recognizing an external mathematical lineage (monotone-operator theory). If the choice is "one fourth meta-pattern addition," pick (PI)/Čencov. C1's operator-sector content still lands (A2'/DA2' α/β recasting as operator-family classification; one-point anchoring as AAD-distinctive), just as *content* in `#deriv-sector-condition` and `#result-sector-persistence-template` rather than as a peer meta-pattern.

**Tier 2 — Content additions (unchanged).** A3 (Fisher-whitened update — now composes with (PI)/Čencov story cleanly since Fisher whitening follows from (PI)), A2 (L1' bias formula with MC), B3 (PID derivation — three independent routes still converge), B4 (variational α' via Pinsker), A4 (update-operator sector). Each lands cleanly; each composes with Tier 1.

**Tier 3 — Working Notes only (unchanged).** A1 (block-evidence generalization); C2 (honest negative result surfacing `#der-chain-confidence-decay`'s Section III reach and the candidate composition-monotonicity meta-segment).

**Strong-option possibility — heredity axiom.** The Jacobian-level B1 spike's Angle 1 shows that under a *heredity* axiom (composite admissibility derivable from sub-agent properties), agent-level B1* is forced. This is a legitimate AAD-internal architectural strengthening of `#post-composition-consistency`. If adopted alongside (PI), metric-α₂ Tier structure collapses and (CM2-M) promotes from Slotine-imported to AAD-derived. This is the most ambitious reading; I would not lead with it, but flag it as a future-session architectural decision worth its own scoping spike.

**Future spikes this cycle opens (revised):**
- **Fourth primary instance of `#disc-additive-coordinate-forcing` via (PI)/Čencov** — if (PI) adoption is accepted, the meta-segment's 1-anchor-2-theorem characterization broadens to 1-anchor-3-theorem (chain anchor; divergence + update Cauchy-FE theorems; Fisher-metric Čencov-invariance theorem). This is now the recommended Phase-B follow-on after B1+B5 land.
- **Heredity axiom for `#post-composition-consistency`** — scoping spike to test whether the architectural commitment is worth the simplification it enables (Tier collapse + CM2-M AAD-derived).
- **Mechanism-design impossibility as fourth `#disc-identifiability-floor` instance** (from B6 §6).
- **Composition-monotonicity meta-segment** (from C2 §10 failure branch — distinct-from-`#disc-additive-coordinate-forcing` Section III structural family).
- **Single axiomatic obstruction behind Cauchy-FE failure + Cramér-Rao rank-deficiency** (from A1 §9.4 O2).
- **Adaptive-metric-coupling** interaction with `spike-adaptive-gain-dynamics`'s (MG-4) (from B1 §6.4).

### Reverse-check flagged (FORMAT.md Gate-3-sidebar)

Per FORMAT.md's standing spike-to-segment reverse-check convention: the six brainstorm-cycle promotions should be verified against the original spike content to confirm no over-aggressive compression. Each spike remains in `msc/spike-*.md` as reasoning trail per `feedback_math_lives_in_segments.md`. Specific items to check on next touch:

- **Spike A / `#deriv-persistence-cost`** — did the "channel-capacity as biggest architectural opening" framing survive? (Retained in Working Notes.) Did the Model-D-adversarial-analog flag survive? (Yes, in Working Notes.)
- **Spike B / `#deriv-critical-mass-composition`** — did the (UO-mult) discussion-grade labeling survive? (Yes, per derivation-audit table.) Did the obstruction analysis §6 survive? (Yes, in Working Notes + derivation-audit rows.)
- **Spike C / `#der-interaction-channel-classification`** — did the Regime-I-with-adversarial-content attack survive? (Yes, in Discussion.) Did the $\mathcal I_{\max}$ heuristic caveat survive? (Yes, in Working Notes with sufficient-statistics-span alternative.)
- **Spike D / `#deriv-adaptive-gain-dynamics`** — did the honest "imported machinery" acknowledgment survive? (Yes, in Epistemic Status.) Did the MAML case's honest classification-not-derivation label survive? (Yes, in derivation-audit table.)
- **Spike F / `#form-consolidation-dynamics`** — did the R2 sub-case (C1 blindness under model-class inadequacy) survive? (Flagged as discussion-level in Working Notes.) Did the stability-upper-bound "pending derivation" flag survive? (Yes, in Epistemic Status + Working Notes.)
- **Spike G / `#deriv-detection-latency`** — did the R2/R3 sub-cases survive compression? (R2 as Working Notes one-evening-spike flag; R3 as reference to #disc-identifiability-floor Instance 1 without re-deriving.) Did the IDT-bypass prediction survive? (Yes, in Discussion.) Did the honest "not novel mathematically; novelty is AAD-framing" survive? (Yes, in Epistemic Status.)

Probably ~30 minutes of focused reading per spike; can be done in a dedicated editorial pass at next session start.

## Active — 2026-04-23 triple audit findings and session-discovered proposals

**10 consolidated findings** from three independent de novo audits (Codex 5 + Gemini 4 + Opus 6, with cross-audit overlap on 5 of them). Full detail in `msc/pending-findings-2026-04-23.md`. Summary table:

| # | Finding | Source(s) | Severity | Subsumption |
|---|---------|-----------|----------|-------------|
| 22 | README-level scope framing outruns Section II exact theorem scope | Codex 1 + Gemini 4 partial | High | Partial by O-BP8 + SP-7 |
| 23 | "16/24 exact survival" headline compresses three distinct layer-claims | Codex 2 | High | Partial by C-BP1 |
| 24 | Strategy-edge semantics not harmonized with identifiability machinery; DAG-forced framing overclaims | Codex 3 + Opus F + Gemini 2 | High | msc/spike-edge-semantics-resolution.md "causal efficacy credence" framing is the integration target |
| 25 | `#result-coupled-diagnostic-framework` slides from defined to runtime-computable | Codex 4 | High | **RESOLVED** 2026-04-25 cleanup cycle: verb-precision pass throughout (computed → defined/reconstructed); definedness vs operational extractability separated; cross-ref to `#result-section-ii-survival` instrumentation-boundary discussion |
| 26 | Section III composition-closure reads more closed than self-aware status supports; Tier 3 prevalence not characterized | Codex 5 + Gemini 1 + Opus D | Medium-high | SP-6 (composition-closure consolidation) |
| 27 | Scalar tempo overcounting — foundational metric structurally additive | Gemini 3 | (already caveated; retained for visibility) | Partial by O-BP3 |
| 28 | $\rho_\Sigma$ is unmeasurable threshold parameter on which trajectory guarantee depends | Opus A | High (gap); medium (substantive vs. honest-open) | None — genuinely unaddressed |
| 29 | Update-rule heterogeneity integration debt in `#def-unity-dimensions` | Opus B | High (pure integration debt) | **RESOLVED** 2026-04-25 cleanup cycle: two-axis structure (content unities + structural $U_f$) elevated from Working-Notes caveat to definitional commitment in `def-unity-dimensions` and `result-unity-closure-mapping` per `msc/spike-unity-closure-mapping.md` Option C |
| 30 | Stacked scope narrowings (Class 1 + learning-agent) only Class 1 visible at OUTLINE | Opus C | High | Directly by O-BP8 |
| 31 | Orient cascade 4c's signal-to-noise sensitivity not surfaced where step prescribed | Opus E | Medium | **RESOLVED** 2026-04-25 cleanup cycle: bundled with F11 in single "Practical sensitivity" paragraph at end of step 4c |

**7 session-discovered architectural proposals** (SP-2 through SP-8) in `_obs/architectural-proposals-2026-04-22.md` §"Post-2026-04-23-audit architectural extensions":

- ~~**SP-2** — Additive-coordinate-forcing meta-pattern, 5-instance (not 3).~~ **LANDED 2026-04-23** as `#disc-additive-coordinate-forcing` meta-segment (`01-aad-core/src/disc-additive-coordinate-forcing.md`, `type: discussion`, `status: discussion-grade`). The 5-instance conjecture was tested and narrowed to a **1-anchor-plus-2-theorem** characterization: chain layer is a mathematical identity (not a Cauchy-FE theorem); divergence and update layers are the two theorems conditional on AAD-internally-motivated axioms. Lyapunov and IB Lagrangian classified as *adjacent family members* with explicit reasoning (Lyapunov coordinate matched not forced; IB adopted from external theorem not re-derived). Cross-refs added in instance and adjacent segments. SP-1 entry in proposals doc was silently truncated; it has been replaced with a promotion pointer.
- **SP-3** — Calibration-laboratory template as prescription. Generalize #obs-software-epistemic-properties' transfer-assumption table to a `domain-instantiation-template.md` for all domains.
- **SP-4** — Agent identity elevation from scope to architectural postulate: "AAD is a theory of token-level adaptation under causal embedding, not type-level agent populations."
- **SP-5** — Two-tier "Reader's Path" presentation. Short load-bearing preamble per segment, preceding the formal apparatus.
- **SP-6** — Composition-closure consolidation pass. Scope bridge lemma explicitly to linear-Gaussian + exponential-family cases; adopt "AAD-shaped reduction" as the honest general claim. Repairs F26.
- **SP-7** — Epistemic architecture as the framework's distinctive contribution. All three audits converge on this reframe: AAD's value is in how it organizes scope, not in which results it integrates. Partially closes F22; composes with SP-3, SP-4, O-BP10, O-BP8 as the framework-reframing cluster.
- **SP-8** — Dual-edged identifiability-floor + separability-pattern reading. Both meta-segments present the positive half (strengthened machinery); foreground the negative half (bounded reach) equally.

**Convergent big-picture reframe** (Codex + Gemini + Opus): move the framework's center of mass from "integration of four disciplines" to "organization-of-scope under a master principle" — Codex's "bounded correction under decomposed disturbance," Gemini's "thermodynamics of purposeful systems with coupling as primary geometric variable," Opus's "epistemic architecture as distinctive contribution." These are not the same proposal but they are on the same axis.

### Actionable from the audit batch

- ~~**F29**, **F31**, **F25**~~ — **landed 2026-04-25 cleanup cycle.**
- **F30** (OUTLINE scope lattice) — 20–40 min editorial; composes naturally with O-BP8 if Phase C framing pass is pursued.

### Requires scoping or substantive work

- **F22 + SP-7** — README + CLAUDE.md + OUTLINE preamble rewrite as a coordinated framing pass. 1–2 sessions. Incorporates the convergent big-picture reframe.
- **F24** — Promote `msc/spike-edge-semantics-resolution.md`'s "causal efficacy credence" framing to segments; soften `#def-strategy-dag`'s "DAG-forced" language; foreground causal sufficiency as scope condition. 1 session.
- **F26 + SP-6** — Composition-closure consolidation pass. 2–3 sessions + optional scoping spike.
- **F28** ($\rho_\Sigma$) — Strengthen-first spike attempting to derive $\rho_\Sigma$ from observable quantities; honest scope-narrowing fallback if strengthening fails. 1–2 sessions.
- **F23** — "16/24 exact survival" per-layer breakdown. Coordinate with C-BP1 three-layer separation to avoid redoing work. 1 session.

### Supersedes prior planning

~~SP-2 supersedes the three-instance meta-segment promotion (Phase B in the prior recommended sequence).~~ **Phase B is closed.** The meta-segment landed with honest 3-primary + 2-adjacent characterization. Future extensions on this axis live in `#disc-additive-coordinate-forcing` Working Notes (candidate future layers at credit-assignment, composition-closure-defect, shared-intent compression; each would require its own AAD-internal axiom + Cauchy-FE derivation).

SP-7 + SP-3 together partially fulfill Phase C (framing pass), which is now deepened rather than replaced — the OUTLINE/CLAUDE.md rewrite should incorporate the convergent reframe at the same time as it adds the scope lattice (O-BP8) and the template-as-organizing-principle (O-BP1) content.


## Recommendations for next session (updated post-2026-04-24 Gemini pressure-point cycle)

**2026-04-24 Tier 1 landing is the immediate next work.** See `## Active — Pending-Review Spikes (2026-04-24 Gemini pressure-point cycle)` §"Tier 1 landing plan" above. Six bundled items across `#deriv-strategy-cost-regret-bound`, `#form-composition-closure`, `#result-contraction-template`, `#deriv-sector-condition`, `#form-information-bottleneck`, `#der-loop-interventional-access`, plus one new appendix `#deriv-bias-bound`. All items are elementary / textbook-grade; none requires new machinery.

Sections below are prior recommendations from earlier cycles; consult once the 2026-04-24 Tier 1 is complete.

---

What follows is one agent's prioritization after the 2026-04-23 audit. Joseph's call which to follow.

### Session gains (what landed; refresh of session character)

The 2026-04-22/23 cycle ran Phases 1–5 + 7 of the proposed sequence, plus two unplanned in-flight strengthening spikes surfaced during the work. Nine commits delivered:

- **Three new uniqueness theorems**, each forcing a logarithmic coordinate via a Cauchy-functional-equation argument on an AAD-internally-motivated additivity axiom: (i) F20 regret-bound derivation (reverse-KL direction forced); (ii) reverse-KL chain-rule uniqueness (Csiszár 1991 / Shore-Johnson 1980 / Hobson 1969, under chain-rule-additivity axiom); (iii) evidential-additivity uniqueness of log-odds (Aczél 1966 Cauchy-functional-equation argument, under evidential-additivity axiom).
- **Discovered structural pattern** — the three theorems share a common shape. Documented as SP-1 during the cycle; **promoted to `#disc-additive-coordinate-forcing` meta-segment 2026-04-23** with honest 1-anchor-plus-2-theorem characterization (chain layer = mathematical identity; divergence, update = theorems conditional on AAD-internal additivity axioms; Lyapunov + IB Lagrangian classified as adjacent family members with explicit reasoning).
- **Scope partitions sharpened.** A2' α/β sub-scope (Kalman/conjugate-Bayesian/gradient-strongly-convex = α derived; PID/rule-based/human-judgment = β assumed). Prop A.1S region condition lifted via stopping-time localization (Khasminskii 2012).
- **Three new meta-segments or promotions.** `#disc-separability-pattern` (positive-half complement to `#disc-identifiability-floor`, six ladders enumerated); `#scope-agent-identity` promoted to formal scope (type: scope, status: robust-qualitative); `#deriv-edge-update-natural-parameter` (uniqueness theorem + scope condition).
- **O-BP14 derivation-table convention** landed in `FORMAT.md` with tables applied to five derivation segments.
- **C-BP3 TST reframing** as calibration laboratory with transfer-assumption table.
- **Citation audit** ran on the reverse-KL uniqueness work: three wrong attributions (Csiszár 1972 / Amari 2009 Theorem 1 / Amari-Cichocki 2010 Prop 3.2 — none contain the chain-rule uniqueness theorem) corrected to Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980 / Aczél-Daróczy 1975 with PDFs saved to `ref/`. Eguchi 1983 venue corrected. Three-layer-pattern discovery now rests on defensible citations.

Segment count: 93 → 96 (added `#disc-identifiability-floor` before this cycle; `#deriv-strategy-cost-regret-bound`, `#disc-separability-pattern`, `#deriv-edge-update-natural-parameter` this cycle). Stage distribution: ~13 claims-verified, ~23 deps-verified, ~59 draft.

### Recommended sequence for next session (updated 2026-04-23)

**Phase α — Quick wins first (1 session total).** Confidence-builders and pure integration debts:
- ~~**F29** — `#def-unity-dimensions` two-axis integration~~ — landed 2026-04-25.
- ~~**F31** — `#der-orient-cascade` step 4c practical-sensitivity note~~ — landed 2026-04-25.
- **F21-follow-up / F24** — Promote `msc/spike-edge-semantics-resolution.md`'s "causal efficacy credence" framing to `#def-strategy-dag`; soften "DAG-forced" language to match `#deriv-graph-structure-uniqueness`'s sufficiency-only content (1 session).

**Phase A — CLOSED 2026-04-23.** Project-wide citation audit completed across 3 commits (`7456ec3`, `6567914`, `f61e62f`). Zero confirmed attribution errors. 26 PDFs in `ref/`. 5 missing-citation gaps hardened. See §"Citations Audit — COMPLETE 2026-04-23" above for detail.

**Phase B — CLOSED 2026-04-23.** The `#disc-additive-coordinate-forcing` meta-segment landed with the honest 1-anchor-plus-2-theorem characterization. Opus's 5-instance conjecture was tested and narrowed: Lyapunov and IB Lagrangian are documented as *adjacent family members* rather than primary instances, with explicit reasoning (Lyapunov's quadratic coordinate is a formulation choice matched to the sector condition, not forced by it; IB is adopted from Tishby-Pereira-Bialek 1999 as applied external theorem rather than re-derived under AAD-internal axioms). Cross-refs added in five home segments; SP-1 entry in proposals doc promoted from truncated-table to promotion-pointer.

**Phase C — Coordinated framing + reframe pass (PARTIAL 2026-04-23; 1-2 sessions remaining).** Part 1 landed in commit `7456ec3`: CLAUDE.md §7 expanded from "Honesty as architectural principle" to "Epistemic architecture as AAD's distinctive contribution" with the convergent Codex/Gemini/Opus reframe and the seven elements of AAD's epistemic architecture explicitly named; `01-aad-core/OUTLINE.md` acquired a new "Reading AAD" paragraph framing the theory at both integration and distinctive levels with the three meta-segments as cross-sectional structure.

**Part 2 (remaining) — segment-level moves:**
- **SP-7** (epistemic architecture foregrounding): README.md public-facing reframe incorporating the convergent audit observation. Partially closes F22.
- **O-BP10** (projection-contraction slogan): "adaptive system = projection whose contraction exceeds target's drift." Promote to segment-level content in `#result-sector-persistence-template` or a new organizing-principle segment.
- **O-BP1** (template as organizing principle): OUTLINE preambles get refreshed framing around disturbance decomposition at scales. Composes with O-BP10 and the additive-coordinate-forcing meta-segment.
- **O-BP8** (explicit scope lattice): name the adaptive → agency → learning-purposeful → Class-1-modular → coupled/logogenic lattice once as a scope-lattice segment or canonical paragraph in `#scope-agency`. Closes F16 and F30.
- **SP-3** (calibration-laboratory template generalization): write `domain-instantiation-template.md` or FORMAT.md section prescribing the transfer-assumption table format. Composes with O-BP8.
- **SP-4** (agent identity to architectural postulate): elevate `#scope-agent-identity` frontmatter from scope to postulate; rewrite Formal Expression to state the commitment ("AAD is a theory of token-level adaptation under causal embedding, not type-level agent populations").

Estimated 1-2 sessions for Part 2. Tracked as task #8.

**Phase D — Composition-closure consolidation (SP-6; 2–3 sessions).** Repairs F26. Scope the bridge lemma explicitly to linear-Gaussian + exponential-family Tier-1 cases; adopt "composite agents are AAD agents iff effective dynamics admit an AAD-shaped reduction" as the honest general claim. Scoping spike valuable first. Downstream of Phase A (citation audit; especially on `#form-composition-closure`'s Khalil/Khasminskii citations).

**Phase E — Substantive spikes (choose by priority):**
- **F28 strengthening spike** ($\rho_\Sigma$ operationalization, 1–2 sessions). Attempt to derive $\rho_\Sigma$ from observable quantities; honest scope-narrowing fallback if strengthening fails. Addresses the deepest substantive finding in this audit batch.
- **O-BP11 observability master-variable falsification spike** (deepest structural insight from the earlier cycle; not yet attempted).
- **Phase 2.5 B.5d uniqueness spike** (potential additional instance of SP-2 pattern).
- **Phase 9 C-BP1 + C-BP4 epistemic separation** (three-layer separation + claim-level statuses; partially addresses F23 and F25; composes with O-BP14 tables).

**Phase F — SP-5 "Reader's Path" two-tier presentation (1–4 sessions).** After Phase C framing pass stabilizes. Short load-bearing preamble per segment; incremental application.

**Phase G — SP-8 dual-edged floor/separability reading (1 session).** Framing touch on `#disc-identifiability-floor` + `#disc-separability-pattern`. Composes with SP-7.

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


## Active — Strategic Architectural Proposals

**See [`PROPOSALS.md`](PROPOSALS.md) at the repository root.** The 2026-04-22/23/24 portfolio was consolidated 2026-04-24 from 33 enumerated proposals into a banded, verified structure with cross-cutting bundles (framework-face reframe; Section III completion), ~6 newly-surfaced candidates from segment Working Notes, and per-proposal independence-of-execution markers. The prior portfolio doc is in `_obs/architectural-proposals-2026-04-22.md` for provenance.

**Top-of-file pointers for immediate decision-making:**

- **Bundle 1 — Framework-face reframe** (SP-7 + O-BP1 + O-BP10 + O-BP8 + SP-3 + SP-4 + SP-8). Highest-leverage single move: **+9 framework / +10 paper**. 2–3 coordinated sessions. README still reads integration-first; segment-level infrastructure already landed. See PROPOSALS.md §Cross-cutting view.
- **Bundle 2 — Section III completion** (O-BP16 + O-BP9 + SP-6-residue + SP-11 + SP-17). Closes all four named Section III OUTLINE GAPs + F26 + F8. **+7 framework completeness.** 6–10 sessions as a program; SP-11 (newly-surfaced meta-segment) is the shortest entry point.
- **Ready-now independent items:** O-BP13 (Cox-necessity win/win theorem spike), C-BP1+C-BP4 bundle (epistemic separation framework), SP-14 (channel-capacity notation), O-BP15 (comprehensive worked example — soon after Bundle 1 stabilizes).

The larger reorganizations (O-BP11 observability-master, O-BP12 resource-budget, O-BP13 Cox-necessity, O-BP15 comprehensive-worked-example, O-BP16 population-Lyapunov, G-BP2 V-strong, G-BP3 Fisher-unification, O-BP3 continuous-tiering, O-BP4 continuous-DAG, O-BP5 recursive-AAD, O-BP2 four-compressions full) remain longer-term scoping work. **O-BP11 (observability as master variable) deserves first attention among these** as the deepest available structural insight — even if not pursued, the scoping spike would surface what AAD's observability machinery actually is across the theory.


## Active — Pending Findings

### 2026-04-25 batch — F-V3 routing decision + F-V4 follow-up review

**Source:** `msc/audit-2026-04-24-fresh-pass.md` (one Opus-4.7 fresh pass + Gemini and Codex re-audits in the same session). Findings detail in `msc/pending-findings-2026-04-25.md`. The audit's primary pass produced "zero findings" and was corrected by independent Gemini/Codex re-audits; the resulting failure-mode analysis is folded into `doc/de-novo-audit-instructions.md` for the next audit posture.

Mechanical fix bundle (F-V1, F-V2, F-V4, F-V5, P-V1, P-V2, P-V3) landed in commit `a6b61fb` — see Archive. Two items remain Active:

**Decision deferred — F-V3 routing (Joseph's call):**

F-V3 = C-iii admits composites without explicit $O_c$ but `scope-composite-agent.md:79` says without $O_c$ composite is "a fiction." **Same finding as F8** from 2026-04-22 batch.

- **Path A (recommended interim):** Edit `scope-composite-agent.md` C-iii to make induced-$O_c$ structure explicit ($O_c$ derived from relevance variable $Y$ when C-iii holds). Preserves the unified disjunctive scope reasoning; resolves the "fiction" contradiction. ~45–60 min. Compatible with later SP-21 if pursued.
- **Path B (SP-21 restructure):** Split (C-i)–(C-iv) into distinct composite ontologies. **Reverses the deliberate 2026-04-22/23 unification choice** — see PROPOSALS.md §G SP-21 entry for the prior reasoning, downstream rework (8 dependent segments), and the explicit spike-level decision that SP-21 would undo. 4–6 sessions. SP-21 currently recommended for *deferral* — re-evaluate after Bundle 2 (Section III completion) matures the substrate.

**F-V4 follow-up review required (added 2026-04-25).** The F-V4 fix to `deriv-strategic-composition.md` zero-sum worked example introduced a *quadratic action-cost regularization* with parameter $c$ to enable interior-NE sector-template instantiation. This was a substantive judgment call (the corrected unregularized linear $\Phi$ with NE at corner $(1,1)$ has no interior contraction, so the original sector-template instantiation can't be salvaged without modification). **Accepted as interim form 2026-04-25; explicit follow-up review required:**
1. Double-check the regularization algebra ($F(\xi) = c\xi$; $R = (1-1/c)\sqrt 2$ disturbance bound).
2. Attempt a Cournot-style linear-quadratic substitution (interior NE without ad-hoc regularization; genuine economic content).
3. Brainstorm other alternatives (LQR-coupled-state, Monderer-Shapley §3, network-coordination, public-goods).
4. Look for unnoticed implications of the corrected NE-at-(1,1) interpretation: §"Honest Limits" failure-regime classification, `#scope-composite-agent` C-iv pedagogical entry-point, project-wide grep for "opposite directions" / "push" near zero-sum framings.

Detail in `deriv-strategic-composition.md` Working Notes §"Zero-sum example regularization." ~1–2 hours of careful follow-up work; should land before the segment is re-promoted to candidate stage. Worth scheduling in the next strengthening cycle.

**B7 → SP-21 (architectural proposal).** The audit's bigger-picture observation B7 (split composite-agent scope routes into distinct ontologies) is captured as **SP-21** in `PROPOSALS.md` §G. SP-21 reverses recent (2026-04-22/23) deliberate unification reasoning; its entry includes the prior-reasoning paper trail and recommends deferral pending Bundle 2 maturation.

**B1–B6 (audit's other big-picture observations).** Mostly confirmation that existing portfolio is on track. Mapped: B1 (form-shaping framing) → additive to SP-7; B5 (Bregman-Fenchel reframe) → already SP-9; B6 (channel-capacity prominence) → already SP-14. B2/B3/B4 are pedagogical/orientation, not separate proposals. Captured in `msc/pending-findings-2026-04-25.md` for orientation; no new portfolio entries needed.

---

### 2026-04-22 batch — current status

The 2026-04-22 batch had 15 findings; the strengthening cycle resolved 4 directly and resolves several others through subsumption. Updated table below; see `msc/pending-findings-2026-04-22.md` for the original characterizations.

**F8 note (added 2026-04-25):** F-V3 from the 2026-04-25 batch is the same finding as F8 below, re-surfaced by the 2026-04-24 fresh-pass audit. F8's "Joseph's Option A vs Option B decision" overlaps with F-V3's Path A vs SP-21 routing. F8 / F-V3 should be resolved as one decision.

| # | Finding | Status |
|---|---------|--------|
| 1 | L0 residual under on-policy execution | **RESOLVED** by strengthening (commit 14a6095): no-go theorem in #der-causal-insufficiency-detection |
| 2 | Unbounded gradient in credit-assignment signal | **RESOLVED** by G-BP1 scoping + partial execution (`msc/spike-gbp1-logit-scoping.md`): Path B evidential-additivity uniqueness theorem landed in new appendix segment #deriv-edge-update-natural-parameter (parallel to reverse-KL uniqueness under chain-rule axiom); #disc-credit-assignment-boundary default signal function restated in log-odds (domain = ℝ, no mechanical break); #def-strategy-dag and #hyp-edge-update-via-gain carry parallel-presentation notes; #deriv-strategic-dynamics Props B.1-B.7 retained in moment-parameter form (Fisher-equivalent). Full G-BP1 sweep deferred; current scope narrow + strengthened |
| 3 | Degenerate MI in strategy IB objective | **RESOLVED** by V-medium G-BP2 (commit a14682e): KL-form replaces Shannon-MI in #form-strategy-complexity-cost |
| 4 | Section II silent scope narrowing (agency → learning) | Open. 45–60 min reconciliation. Coordinate with Finding 9 for combined Section II preamble pass (or absorb both into O-BP1 framing pass) |
| 5 | Loop framing overstates Level 2 access | **RESOLVED** by O-BP6 identity promotion (commit 2980327): #scope-agent-identity now a formal scope statement (type: scope, status: robust-qualitative); #der-loop-interventional-access depends on it and carries an explicit singular-trajectory-ground paragraph. F5 closed end-to-end |
| 6 | Composition timescale heuristic outruns bridge conditions | Open. 30–45 min scope-narrowing in #post-composition-consistency |
| 7 | TST overstates git as complete chronica | **RESOLVED** by strengthening (commit b6134c2): per-quantity exactness audit + conditional maximality + $\mathcal{C}_t^{\text{commit}}$ in #obs-software-epistemic-properties |
| 8 | (C-iii) mutual-benefit vs (A1) decomposable $G_c$ gap | Open. 45–60 min scope-reconciliation; involves Joseph's Option A vs Option B decision |
| 9 | Section II preamble framing understates survival | Open; absorbed if O-BP1 framing pass executed. 30 min standalone |
| 10 | `#form-information-bottleneck` status mismatches unification role | **RESOLVED** (commit a14682e): status reclassified from discussion-grade to exact (applied external theorem) |
| 11 | Orient cascade step 4c convergence in non-stationary envs | **RESOLVED** by F31 sensitivity-paragraph landing (2026-04-25 cleanup cycle): single italicized "Practical sensitivity" paragraph at end of step 4c covers SNR sensitivity (F31) and non-stationarity caveat (F11), cross-referencing #der-causal-insufficiency-detection. F1 strengthening's reframing of step 4c remains the upstream no-go context |
| 12 | Section II survival slides from statement-level to operational | Open. Subsumed by C-BP1 (three-layer epistemic separation) |
| 13 | `#def-strategy-dag` L1-as-default overgeneralizes beyond strict-prerequisite | **RESOLVED** by strengthening (commit 4d050c8): Prop B.7 derives L1' transfer for observable $C$ with five-way gating; refutes unobservable-$C$ via Cramér-Rao floor; #def-strategy-dag headline + Correlation Hierarchy table updated |
| 14 | `#scope-developer-agent` exact-status mismatch (human vs AI regimes) | **RESOLVED** by naming-pilot cleanup (2026-04-23): segment type: `definition` → `scope` and status: `exact` → `axiomatic` to match other domain-scope declarations (#scope-software, #scope-multi-agent). The `exact` rating never fit a representational-mapping segment. |
| 15 | Software "richest operationalization domain" headline overclaims | **RESOLVED** by C-BP3 calibration-lab reframing (commit d0373fc): #obs-software-epistemic-properties headline rewritten; 02-tst-core/OUTLINE preamble updated; transfer-assumption table makes non-software identification relaxations explicit |

### Actionable now (independent of remaining portfolio decisions)

- **Finding 4 + 9 coordinated pass** — Section II preamble + scope-narrowing. 60–90 min combined; or absorbed by O-BP1.
- **Finding 6** — composition-consistency scope-narrowing. 30–45 min.
- **Finding 8** — (C-iii) Option A vs Option B decision needed before edit.

### 2026-04-22 evening batch — six new findings (all resolved)

Three independent de novo audits (Codex, Gemini, Opus) ran *after* the morning strengthening cycle and surfaced six new findings. The 2026-04-22/23 strengthening cycle resolved all six (F18-F21 in the Phase 1 cleanup commit; F16 partial, F17 partial). Status table:

| # | Finding | Source | Severity | Status |
|---|---------|--------|----------|--------|
| 16 | Section II scope lattice underspecified across segments | Codex F1 (evening) | Medium | Open; subsumed by O-BP8 in future Phase C framing pass |
| 17 | `#result-coupled-diagnostic-framework` operational-computability overclaim | Codex F4 (evening) | Medium-high | Open; subsumed by C-BP1 three-layer separation (future Phase 9) |
| 18 | `#example-L1` says L1' transfer "open" — STALE after F13 strengthening | Gemini F1 (evening) | Medium | **RESOLVED** (commit 0a772d2): updated with Prop B.7 + Cramér-Rao refutation + three repair routes; facilitator monotonicity surfaced as load-bearing |
| 19 | `#result-section-ii-survival` bias bound in entropy form, stale after 2026-04-21 Finding B | Gemini F3 (evening) | Medium | **RESOLVED** (commit 0a772d2): MI form + triple-zero boundary structure made explicit |
| 20 | KL-direction degeneracy in `#form-strategy-complexity-cost` variational form (introduced by V-medium) | Opus F1 (evening) | High | **RESOLVED AS STRENGTHENING** (commits 0a772d2, f70fb68, e777f01): new appendix #deriv-strategy-cost-regret-bound with regret-bound derivation (direction forced) + chain-rule uniqueness theorem (specific divergence uniquely forced) + corrected citations |
| 21 | `#disc-identifiability-floor` frontmatter status conflicts with internal text | Opus F3 (evening) | Low | **RESOLVED** (commit 0a772d2): status → discussion-grade; Epistemic Status rewritten cleanly separating meta-pattern from instances |

**Reaffirmed (not new):** Codex F2 evening reaffirms F6 (composition timescale heuristic); Codex F3 evening reaffirms F8 ((C-iii) gap); Opus F2 evening reaffirms F14 (`#scope-developer-agent` status — now RESOLVED 2026-04-24). Several other candidate findings were *rescinded* by the audits themselves on in-segment counterevidence — see `msc/pending-findings-2026-04-22.md` and the audit transcripts for the transparency tables.

### 2026-04-21 batch — both RESOLVED 2026-04-22 (historical, from earlier in the day)

Finding A (composition-closure temporal coarse-graining) and Finding B (observation-ambiguity-modulation architecture-contamination) — both closed in the morning's audit-trio commits before the strengthening cycle. See `msc/pending-findings-2026-04-21.md` for the closed-out resolution notes.


## Active — Tier-C Deferrals

- **$G_t$ as single object; $(O_t, \Sigma_t)$ as a property** (Opus 2026-04-21 synthesis §7). Touches Section II scaffolding. **Defer until more Class 2 logogenic work lands.** Strengthened by O-BP2 (compressions-as-projections); if O-BP2 is pursued, this item converges with it.
- **Continuous convention hierarchy** $N_r \in [1, \infty]$ (Opus 2026-04-21 synthesis §8). Subsumed by O-BP3 (continuous-parameter tiering) — handled there if O-BP3 is pursued.


## Active — Genuinely Open MEDIUM Items

- **Composition scaling with $N$.** Whether closure defect scales polynomially or exponentially with team size. **Scoping spike done** (`msc/spike-composition-scaling-N.md`, 2026-04-22): four readings identified, five candidate first moves, two composing axes ($K_c$ macro-timescale; unity × update-heterogeneity). Question is well-framed but unresolved; execution deferred. Critical for large-team applications.

- **Multi-timescale stability formalization.** `#sketch-multi-timescale-stability` is stage `sketch`; `#der-temporal-nesting` leans on it. Needs formal $N$-timescale singular perturbation treatment. Partially overlaps with the 2026-04-21 Finding A repair path if Option 2 (Tikhonov) is later chosen.

- **Communication-gain adversarial scope.** `#hyp-communication-gain`'s additive model fails for deception (trust is game-theoretic). Either extend or add explicit scope limitation.

- **Exploit/Explore/Deliberate spike findings.** `#disc-exploit-explore-deliberate` was written, but the adversarial spike (`msc/spike-three-way-tradeoff.md`) noted that the two-stage decomposition and $\Delta V_\Sigma$ approximation are hand-waving. Segment may be substantially rewritten. The 2026-04-22 AI integration added an EFE pragmatic/epistemic + sophisticated-inference cross-reference; the rewrite question remains.

- **Adjacent identifiability floors** (`#disc-identifiability-floor` §"Adjacent Floors", added 2026-04-22). Three open extensions: (1) causal-IB for interventional relevance variables (Wieczorek-Roth 2017 and follow-ups); (2) misspecification-cost quantification under finite information budget; (3) tier-switching policy cost. Each is a candidate scoping spike. Overlaps with O-BP7 (known structural absences) — both surface from the same observation that the theory has gaps in its tier-switching/misspecification machinery.

- **V-strong G-BP2 — paper-writing-time decision.** Whether to ever present AAD as a control-theoretic specialization of active inference. The V-medium move keeps both options open. Per `msc/spike-active-inference-vs-aad.md` §I action 5, defer to the right rhetorical moment.

- **Transient dependency amplification — spike landed 2026-04-25 (`msc/spike-transient-dependency-amplification.md`); promotion blocked.** The spike derives a candidate bridge from `#result-coupled-diagnostic-framework`'s logogenic Lipschitz constant $L_A$ to a feature-local finite-horizon dependency-operator scaling. Five claims exact in the affine sub-scope: sup-Lipschitz lemma; linearized $L_A$ bound by $\sup_\pi \lVert B_\pi J_{\pi,d-1}\cdots J_{\pi,0} P_F\rVert$; branching $(|g|\sqrt{B})^d$ transient growth (nilpotent operator with exponential finite-horizon gain); checkpoint product bound; singular-subspace coverage formula $\lVert P_{\eta,r} G\rVert = \max(\eta\sigma_1, \sigma_{r+1})$. Plus a checkpoint-frequency threshold $h < \log(1/\eta)/\log\Gamma$. Working Note pointers in `#result-coupled-diagnostic-framework` (logogenic side) and `#hyp-exponential-cognitive-load` (TST side); catalog entry as #3 in `msc/advanced-spike-proposals.md`. The spike now also draws the AAD-internal natural-metric connection (Fisher metric via (PI)/Čencov, parallel to `#deriv-causal-ib-lmi`'s matrix-form survival bound). Promotion to a TST-side derived segment (`02-tst-core/src/der-transient-dependency-amplification.md`) is blocked on priority-ordered obligations:
  - **Formal sub-scope.** Largely already done (acyclic feature DAG + linearized + affine readout); needs canonical pin-down.
  - **Nonsmooth $A_O$ via Clarke subgradients.** The supremum-of-policies has policy-switching kinks that the current Lemma 1 covers in the Lipschitz form but not in the differentiable form. Substantive next-pass math.
  - **Checkpoint coverage theorem in observable terms.** Define $P_k = I - \eta_k C_k$ where $C_k$ projects onto observation-detectable error directions; relate left-singular vectors of $G$ to test-coverage / interface / type-constraint structure.
  - **Recover TST scalar form $k^d$.** Show `#hyp-exponential-cognitive-load`'s $k^{\text{discontinuities}}$ as a uniform-per-block-gain special case of the operator product. Closes the count-vs-structure open question listed in that hypothesis's Working Notes.
  - **$\widehat J_F$ estimator from TST quantities.** Block-matrix construction with separate channels for static-dependency / co-change / strategy-DAG / semantic-reasoning / test-coverage. Substantive design work.
  - **Empirical validation.** Compare proxy operator-norm measures against LLM performance degradation, tool-call-count, recovery-after-test patterns. Empirical / discussion-grade.
  - **Lower-bound failure conditions.** Currently only upper-bound + worst-case-construction. A typical-case failure theorem (under a distribution over bias directions) would be stronger.

  Provenance: Gemini wrote two initial passes; Codex's pass (overwriting rather than adding to Gemini's after a scope misunderstanding — the new spike builds on but cannot directly reference Gemini's earlier content) produced the substantive math-grounded version landed.

- **Causal-IB LMI generalization — LANDED 2026-04-25.** The multidimensional repair of `#deriv-causal-ib-exploration`'s scalar formulation is now in `#deriv-causal-ib-lmi`: LMI on the Fisher Information Matrix with PSD matrix Lagrange multiplier $\Lambda$; exploration bonus $\text{Tr}(\Lambda \cdot \mathcal I_o(a))$ resolves the blank-wall attack by complementary slackness on direction. Spike trail: `msc/spike-causal-information-bottleneck.md` §7 and `msc/spike-causal-ib-lmi-repair.md`. **Follow-on items** opened by the LMI landing:
  - **Tensor adaptive tempo.** `#def-adaptive-tempo` is currently scalar; the LMI requires tensor-valued $\mathcal{T}$ for per-direction adaptive rates aligned with the matrix machinery in `#deriv-fisher-whitened-update-rule` and `#deriv-adaptive-gain-dynamics`. Composes with the adaptive-gain tensor extension flagged in the 2026-04-23 brainstorm cycle's "Future spikes opened by this cycle." Bounded scoping spike.
  - **Worked 2D example for blank-wall resolution.** Concrete 2D drift environment showing $\text{Tr}(\Lambda \mathcal{I}_o)$ distinguishing wall-channel from drift-channel actions. ~30–60 min editorial / worked example.
  - **2D simulation update.** Generalize `msc/track-b-nonlinear-sims/variants/variant_causal_ib.py` to 2D with separable drifting/non-drifting subspaces; show LMI agent passes where scalar-Lagrangian agent succumbs to blank-wall trap. Bounded simulation work.
  - **Closed-form $\mathcal{I}_{\min}$ via DARE.** Standard control-theory machinery (Boyd et al. 1994; Anderson-Moore 1979) gives $\mathcal{I}_{\min}(Q_\rho, A, R^2)$ explicitly. Currently theorem-imported in the segment; explicit derivation worth doing for the AAD reader who hasn't met DARE.


## Active — Missing Segments

### AAD Core (`01-aad-core/`)

| Slug | Section | Type | Description |
|------|---------|------|-------------|
| `adversarial-edge-targeting` | III | Derived? | Which strategy edges most valuable to attack — the Section III gap |
| `intent-dag-development` | A | Aside | Convergence history of AND/OR + single-$p$ (archaeological record) |
| `worked-example-cam` | A | Worked example | Coevolving automata (Miller 2022): AAD ↔ Moore machine mapping, meta-machine as $\varepsilon^\ast = 0$ composition. Planned in `#form-composition-closure` Discussion. |

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


## Active — Naming Discipline (role-prefix sweep complete 2026-04-24; refined Round 1 pending)

**Status: full role-prefix sweep complete.** All 142 active segments are now in `[type-prefix]-[subject-noun]` form. The sweep was: pilot (seven slug changes including the `scope-condition` semantic split) → tooling (`bin/align-slug` over `bin/rename-slug`) → audit (opus general-purpose verified 100% type-vocabulary conformance, surfaced 5 type-vs-content mismatches, three corrected) → expanded `TYPE_TO_PREFIX` mapping (14 entries collapsing long FORMAT.md tokens to compact natural-English prefixes) → trailing-`-{type}` strip → full sweep. Pilot landings, sweep details, and deferrals are tabulated in [`msc/naming-pilot-rename-plan.md`](msc/naming-pilot-rename-plan.md). Cycle narrative in [`CHANGELOG.md`](CHANGELOG.md) entry for 2026-04-24. The workstream's next piece of work is the principles-file rewrite — *already done in this cycle* (refined edition committed) — followed by a refined Round 1 cold-start that votes on subject-nouns only (role-prefix is now architectural invariant).

**Known follow-ups:** ~135 segments still embed pre-rename slug names inside `*[Type (slug)]*` formal tags (mechanical to detect, content cleanup pass). Two reviewer-judgment type calls deferred (`#der-agent-opacity`, `#scope-observation-ambiguity-modulation`). Three H1-vs-first-tag word disagreements surfaced (`form-objective-functional`, `form-composition-closure`, `scope-ciy-observational-proxy`). All three are bounded content-cleanup work, not blocking the next cycle.

### What exists (artifacts)

- `doc/naming-principles.md` — shared principles + voting format + instructions given to all Round-1 agents (moved from `msc/` 2026-04-26 as part of the doc-pipeline cycle).
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
3. **Scope-honesty should dominate memorability for meta-segment names specifically.** The `#disc-additive-coordinate-forcing → #cauchy-coordinates` vs `#forced-coordinates` decision — memorability loses to scope-honesty because the Čencov 4th instance isn't Cauchy-FE. Principle worth calling out by case.
4. **Canonicalize vs. keep vs. rename are three distinct moves.** The principles conflate "keep status quo" with "keep, and now canonicalize — stop paraphrasing, reference by this name." Deserves its own weight category or flag.
5. **Name-unnamed-thing ≠ rename.** Proposing a name for a currently-paraphrased recurring pattern is architecturally different from renaming an established segment. Both currently share the vote format.
6. **Symbol-to-English parity is a third category.** Adding an English alias alongside a symbol (α₁ → derived-gain regime) is neither rename nor keep — it's "add alias." May deserve its own notation.
7. **Cold-start instruction must be the first paragraph of the principles file.** Opus-4-7-b openly disclosed accidental contamination from `git status` showing a modified brainstorm file. The instruction needs to fire before agents start any orientation reading.
8. **Subject-noun preference for slug naming.** Name segments by the *thing* they define, not by the *role* the segment plays. The canonical case — `#scope-condition` split into `#scope-adaptive-system` + `#scope-agency` — removed "condition" (a filler word) in favour of the subject-class each scope delimits. Round 1 surfaced this via Sonnet-4-6's "objects over proof-devices" observation; Joseph confirmed as general principle.
9. **Acronym discipline underspecified.** Multiple agents flagged that every new acronym carries cost; no principle governs when adding one is worth it.
10. **Three / four naming layers need explicit governance.** Formal slugs / prose defaults for symbols / framing-posture vocabulary / public-API headers. Friction comes from mixing these.
11. **"Renamed-from-now-sounds-weird" test.** Opus-4-7-b's implicit criterion: imagine the project six months from now; does the old name sound quaint or does the new name sound forced? Worth making explicit.

### The role-prefix discipline (proposed, not yet ratified)

Rename segments to use `{role-type}-{subject-noun}` pattern, using FORMAT.md's existing type vocabulary (with `TYPE_TO_PREFIX` in `bin/align-slug` collapsing long type tokens — currently `worked-example → example` — see CLAUDE.md §"Slug role-prefix mapping"). This front-loads the segment's epistemic character in the slug itself, read repeatedly in cross-references across the repo.

Tooling: `bin/align-slug SLUG` aligns a single segment's slug to its frontmatter `type:` (no-op if already aligned). `bin/align-slug --all` sweeps the repo. The operation is mechanical; subject-noun renames are a separate cycle. Landed renames and remaining candidates are tracked in [`msc/naming-pilot-rename-plan.md`](msc/naming-pilot-rename-plan.md).

### Pilot outcome (2026-04-23, landed)

The specific rename mappings (landed, deferred) live in [`msc/naming-pilot-rename-plan.md`](msc/naming-pilot-rename-plan.md) — a frozen details file that is excluded from `bin/rename-slug`'s substitution patterns (otherwise a rename pass would corrupt the mapping table itself). Keep that file as the source of truth for what-renames-to-what; keep this TODO section as the source of truth for the surrounding strategic plan (insights, principles, post-pilot workstream).

Seven slug changes landed in this pilot: the two `-act-agent` relics (`scope-logogenic-agent`, `scope-developer-agent`), the composite rename (`scope-composite-agent`), the `scope-condition` 1:2 semantic split into `scope-adaptive-system` + `scope-agency`, and pure role-prefix additions on the three meta-segments (`discussion-identifiability-floor`, `discussion-separability-pattern`, `discussion-additive-coordinate-forcing`). 01-aad-core lint-clean after every step.

Pilot validation observations (full list in the details file): role-prefix reads cleanly in cross-references and sharpens the dependency graph; formal-tag labels need hand-update (the mechanical rename can't reclassify prose-embedded slug strings); H1/opening-sentence framing shifts require a human pass; `bin/rename-slug` gained a stale-text scan and a framing reminder to surface those. Recommend cascading to the remaining ~120 slugs as a coordinated pass — after the refined Round 1 settles the subject-noun vote.

### Post-pilot plan

Assuming the pilot validates the approach:

1. **Refine `doc/naming-principles.md`** based on (a) all 11 insights above, (b) the role-prefix discipline as an invariant (not a vote target — the prefix is architectural), (c) clarify "canonicalize" as a distinct move from "keep", (d) make the Greek-vocabulary commitment explicit as a preference principle, (e) move cold-start instruction to the first paragraph, (f) name `+2` explicitly and spell out weight bands, (g) separate name-unnamed-thing from rename categories in the format, (h) add subject-noun preference as principle, (i) flag the "renamed-from-now-sounds-weird" test.
2. **Rerun Round 1 cold-start with the refined principles.** 5–8 fresh agents across architectures; same cold-start discipline; instructions note that prefix is invariant and only the subject-noun is vote-target-able.
3. **Quick "import anything of unique value from the original Round 1"** — before aggregating the new Round 1, scan the existing 10 vote files for proposals that the new batch might not have surfaced (deeper unnamed-pattern discoveries, edge-case rejections, etc.) and add them to the new aggregation as supplementary items.
4. **Aggregate, then run Round 2** (blind, using the existing `bin/naming-aggregate.rb --format=round2`).
5. **Collision audit** on the top finalists after Round 2 (per earlier discussion — web search for external conflicts à la the ACT → AI Consciousness Test precedent that forced the 2026-04-16 rename).
6. **Final judgment pass and landing.**

### Known deferred items that will resume after the pilot

Slug-specific deferrals (the `aad-agent` vs `adaptive-agent` family debate, ASF umbrella naming, and the list of Round-1 consensus candidates that will re-surface under the subject-noun + role-prefix discipline in refined Round 1) are tracked in [`msc/naming-pilot-rename-plan.md`](msc/naming-pilot-rename-plan.md). Strategic framing:

- **Deferrals that are slug-specific** — re-evaluate per-candidate after the pilot validates role-prefix reading. No pre-deciding; let the refined vote reconfirm.
- **`ASF` umbrella naming** — Round 1 voted under incomplete framing (agents misread `ASF` as debt rather than the intentional parent-level name). Re-surface in refined Round 1 with correct framing: `ASF` is the umbrella; `AAD` is Part I; `TST` is Part II; etc.
- **`#deriv-causal-ib-exploration` rename queued.** The slug names the *role/effect* (exploration as action-selection consequence) rather than the *thing defined* (the survival-imperative bound on observation noise via Lyapunov persistence). The companion segment `#deriv-causal-ib-lmi` was named correctly during its 2026-04-25 promotion; the parent inherits the misnaming from Gemini's earlier promotion. Per `feedback_subject_noun_slug_naming.md`, candidate replacements: `#deriv-causal-ib-survival` (clearest), `#deriv-survival-bound`, or `#deriv-causal-ib-scalar` (paired naming with `#deriv-causal-ib-lmi` as scalar-vs-matrix forms). Resolve as part of next naming-discipline cycle alongside other subject-noun decisions.

### Next step

Pilot has landed. The next piece of work is the principles-file rewrite (folding in the 11 Round-1 insights above plus the pilot-validation observations in the details file), then refined Round 1, then aggregation + Round 2 + collision audit + landing.


## Active — Editorial Hygiene

- **Spike-to-segment reverse-check.** Standing Gate 2 check per `FORMAT.md`: "What did the spike establish that the segment does not say?" — added in Session C.5 of 2026-04-21 cycle; verify it's still present and visible.

- **Segment counts in CLAUDE.md "What's Settled" summary** — refreshed 2026-04-24 (post-naming-pilot) at 111 AAD core segments. Current count 2026-04-25 is 114 (Gemini's `#internal-external-decomposition` + `#deriv-causal-ib-exploration`; Claude's `#deriv-causal-ib-lmi`). The "What's Settled" summary lives in `CLAUDE-2.md` (off-limits during audits); refresh opportunistically when next out of audit-mode work.


## Active — Promotion Pipeline

**Current state (2026-04-25, post-Causal-IB-LMI + transient-amplification):** 114 AAD core segments. Stage distribution per `bin/lint-outline`: 14 claims-verified, 23 deps-verified, 76 draft, 1 unknown. The 2026-04-25 cycle added three new draft segments — `#internal-external-decomposition` (Gemini), `#deriv-causal-ib-exploration` (Gemini), `#deriv-causal-ib-lmi` (Claude). Segments from the 2026-04-22 strengthening cycle remain reset to `draft` pending re-review: `#der-causal-insufficiency-detection`, `#def-strategy-dag`, `#deriv-strategic-dynamics`, `#form-information-bottleneck`, `#der-directed-separation`, `#def-satisfaction-gap`, `#def-control-regret`, `#form-strategy-complexity-cost`, `#disc-compression-operations`, `#result-sector-persistence-template`, `#der-loop-interventional-access`. The 2026-04-23 Gap A/B cycle added six new draft segments; the 2026-04-24 pressure-point cycle added `#deriv-bias-bound` (draft); the 2026-04-24 naming pilot added `#scope-adaptive-system` and rewrote `#scope-agency` (both claims-verified).

The new `#disc-identifiability-floor` segment is at `draft`; it would benefit from a Gate 1 dependency audit on the next promotion pass.

Recommended next promotion candidates remain the ones from the prior round: `#deriv-sector-condition`, `#deriv-recursive-update`, `#result-mismatch-decomposition`, `#der-chain-confidence-decay`, `#result-persistence-condition`, `#der-gain-sector-bridge`, `#example-kalman`, `#deriv-discrete-sector-condition`, `#deriv-graph-structure-uniqueness`. Plus: `#deriv-causal-ib-exploration` and `#deriv-causal-ib-lmi` (paired Causal-IB cluster, naturally promoted together) and `#internal-external-decomposition`. (`#def-satisfaction-gap` and `#def-control-regret` were on this list pre-strengthening; they are now back at draft after the EFE-contrast addition and need re-promotion.)


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

### 2026-04-25 cleanup cycle — COMPLETE (commits `7e2e074`, `aa1fb15`)

Three small editorial repairs landed in parallel as background-agent work, plus TODO/CHANGELOG archival housekeeping. Lint-clean.

- **F11 + F31** — `01-aad-core/src/der-orient-cascade.md`: single italicized "Practical sensitivity" paragraph at end of step 4c covering both SNR sensitivity (F31) and non-stationarity caveat (F11), cross-referencing `#der-causal-insufficiency-detection`.
- **F25** — `03-logogenic-agents/src/result-coupled-diagnostic-framework.md`: verb-precision pass throughout (computed → defined / reconstructed); new sentence separating definedness from operational extractability; cross-reference to `#result-section-ii-survival`'s instrumentation-boundary discussion.
- **F29** — `01-aad-core/src/def-unity-dimensions.md` and `01-aad-core/src/result-unity-closure-mapping.md`: two-axis structure (content unities + structural $U_f$) elevated from Working-Notes caveat to definitional commitment per `msc/spike-unity-closure-mapping.md` Option C.

Pattern noted (CHANGELOG entry for the day): small independent editorial repairs delegated to parallel background agents while a separate cycle (Gemini-driven Section III spike-promotion) ran concurrently in `01-aad-core/src/`. Cleanup stayed clear of composition-closure and additive-coordinate-forcing territory.

### 2026-04-25 audit-extraction mechanical fix bundle — COMPLETE (commit `a6b61fb`)

The 2026-04-25 audit-extraction cycle's mechanical fix bundle landed (uncommitted at extraction-time, committed in `a6b61fb` "2026-04-25 audit extraction: pending-findings, mechanical fixes, SP-21"). Each finding verified first-hand against current src; lint-clean.

- **F-V1** — Discrete-to-continuous Model S variance gap math correction in `deriv-discrete-sector-condition.md` and `detail-linear-ode-approximation.md` (asymptotic claim corrected $O((\eta^*)^2) \to O(\eta^*) = O(1/\nu)$ via Taylor expansion of segment's own DA.1S; numerical sanity check confirmed).
- **F-V2** — `scope-multi-agent.md` Discussion: adversarial-pairs paragraph split between non-equilibrium-convergent (excluded) and equilibrium-convergent (admitted via C-iv).
- **F-V4** — Sign error in zero-sum worked example in `deriv-strategic-composition.md` corrected ($\Phi = a_A + a_B$, NE $(1,1)$). Quadratic action-cost regularization introduced as substantive judgment call to enable interior-NE sector-template instantiation; flagged for follow-up review (still Active).
- **F-V5** — Cross-component pass on `02-tst-core/src/scope-developer-agent.md` integrating Class 2 caveats from `03-logogenic-agents/`.
- **P-V1** — `result-adversarial-tempo-advantage.md` Working Notes edit (bundled with F-V1).
- **P-V2** — `result-unity-closure-mapping.md` punchline tightened with invariance condition + cross-reference to `#form-composition-closure`'s Mori-Zwanzig zero-lag bound.
- **P-V3** — `hyp-causal-discovery-from-git.md` one-sentence softening of the temporal-ordering-as-causal-direction claim.
- **B7 → SP-21** — Captured in `PROPOSALS.md` §G with full prior-reasoning paper trail. Reverses 2026-04-22/23 deliberate disjunctive-C-iv unification reasoning; recommended for deferral until Bundle 2 (Section III completion) matures the substrate.
- **F-V3** routing decision (Path A vs SP-21) and **F-V4** follow-up review remain Active.

### 2026-04-22/23 evening Phase 1 cleanups (F18-F21) — COMPLETE (commit `0a772d2`)

Highest-priority cleanups from the 2026-04-22 evening triple audit, executed strengthen-first per Joseph's posture; F20 strengthened rather than softened; the others were mechanical cross-segment updates. (Subsumed within the broader 2026-04-22/23 cascading strengthening cycle Archive entry below; itemized here for cross-reference.)

- **F18** — `#example-L1` updated with Prop B.7 (observable-$C$ five-way gating) + Cramér-Rao refutation for unobservable-$C$; three repair routes named.
- **F19** — `#result-section-ii-survival` bias bound replaced with MI form; triple-zero boundary structure ($\kappa=0$ OR $\mathcal{A}=0$ OR factually-sharp observation) made explicit.
- **F20** — landed as strengthening: new appendix segment `#deriv-strategy-cost-regret-bound` with TV bound, Pinsker-KL, direction-forcing, admissible-divergence family analysis, and linear-vs-square-root $\beta_\Sigma$ trade-off. `msc/spike-f20-kl-direction-strengthening.md` retained as reasoning trail only.
- **F21** — `#disc-identifiability-floor` frontmatter `status:` corrected to `discussion-grade`; Epistemic Status rewritten cleanly separating meta-pattern (discussion-grade) from individual instances (F1: exact/robust qualitative; F13 L1': exact).

### 2026-04-23 citations audit — COMPLETE (commits `7456ec3`, `6567914`, `f61e62f`)

Project-wide citation audit ran across 3 commits and concluded with **zero confirmed attribution errors**: the reverse-KL audit's 3-wrong-out-of-16 rate was a local concentration in that one spike's citations; the broader corpus is clean.

- `7456ec3` — SP-2 landing + framing-pass subset (initial SP-1 truncation fix in proposals doc).
- `6567914` — Tier 1 verification: 3 framing refinements (Eguchi 1983 framework not theorem; Sun & Firestone direction-of-inference; Friston 2023 path-integral / Friston 2019 NESS) + Morozova-Chentsov full citation completion in `#deriv-strategy-cost-regret-bound` §6.2 + ref/ rename hygiene.
- `f61e62f` — Missing-citation hardening: Tikhonov 1952 + Khalil 2002 Ch 11 to `#der-temporal-nesting` and `#sketch-multi-timescale-stability`; Chechik 2005 to `#disc-compression-operations`; Kallenberg 2002 (Doob-Dynkin) in `#deriv-recursive-update`; Cox 1946 + Jaynes 2003 in `#deriv-graph-structure-uniqueness` and `#def-strategy-dag`; Cramér 1946 in `#disc-identifiability-floor` and `#deriv-strategic-dynamics`.

26 PDFs in `ref/` (canonically named `{author}-{year}-{short}.pdf`) covering load-bearing external theorems. Two PDF-level Tier 1 verification agents confirmed highest-risk attributions (Bruineberg "Pearl-blanket vs Friston-blanket" terminology is VERBATIM with credit to Martin Biehl; Bareinboim CHT = Theorem 1 p.22 of 2022 ACM Books chapter; Aguilera FEP-narrow-validity claim exactly matches AAD's usage). Residue: 3 emphasis-vulnerable linter warnings in `#deriv-strategic-dynamics` on dense table-row math; Miller 2022 chapter/section/table loci not independently PDF-verified (book in `ref/miller-2022-ex-machina.pdf`).

### 2026-04-24 naming pilot — COMPLETE (commit `09ace17`)

Role-prefix discipline validation + `scope-condition` semantic split. Seven slug changes: (a) `#ai-agent-as-act-agent` → `#scope-logogenic-agent` (type: definition → scope); (b) `#developer-as-act-agent` → `#scope-developer-agent` (type: definition → scope; status: exact → axiomatic, resolving Finding 14 Option A); (c) `#composition-scope-condition` → `#scope-composite-agent`; (d) `#scope-condition` 1:2 split into `#scope-adaptive-system` + `#scope-agency` (the old name described the segment's role rather than what it defined; downstream segments actually need one of two distinct scopes); (e)–(g) pure role-prefix adds on `#disc-identifiability-floor`, `#disc-separability-pattern`, `#disc-additive-coordinate-forcing`.

Compound subject-noun substitutions (Round-1 consensus for `separability-ladder` and `forced-coordinates`) deferred to refined Round 1 / Round 2 — subject-noun judgment belongs to the voting process, not ad-hoc pilot landing. Going forward, file+tag role-prefix changes should be done as distinct mechanical passes, with subject-noun renames executed independently afterward.

Infrastructure: `bin/rename-slug` (deterministic Ruby rename with pre/post safety checks, stale-text scan, framing reminder, merge-confirmation, batch-mode per-pair re-planning); `msc/naming-pilot-rename-plan.md` (frozen rename-mapping record, glob-excluded via `msc/naming-*.md`). 01-aad-core lint-clean after every step. Segment count 110 → 111 (net +1 from the 1:2 split).

### 2026-04-22/23 strengthening cycle — COMPLETE (commits `0a772d2`, `c1d9fcf`, `2980327`, `f70fb68`, `80b40d2`, `d0373fc`, `72ca532`, `e777f01`, `a39dfb7`)

Nine commits delivering six proposal executions, three Cauchy-functional-equation uniqueness theorems, and one citation-audit cleanup. The cycle's distinctive pattern: three independent strengthenings all forced logarithmic coordinates via Cauchy-functional-equation arguments, which on retrospect comprise a three-layer additive-decomposition pattern (documented as §SP-1 in `_obs/architectural-proposals-2026-04-22.md`).

- **Phase 1 cleanups (F18-F21) + F20 regret-bound strengthening** (commit `0a772d2`). F18 (worked-example-L1 stale L1' open claim), F19 (section-ii-survival entropy→MI bias bound), F21 (identifiability-floor frontmatter). F20 strengthened as regret-bound derivation: the π*-first KL direction is forced because forward-KL is vacuous under deterministic π*. New appendix segment `#deriv-strategy-cost-regret-bound`.
- **Phase 2: O-BP14 derivation-table convention** (commit `c1d9fcf`). FORMAT.md convention + tables applied to 5 derivation segments. Surfaced A2' α/β ambiguity (→ A2' strengthening spike) and B.5d minimal-scheme claim (parked Phase 2.5).
- **Phase 3: O-BP6 identity promotion** (commit `2980327`). `#scope-agent-identity` promoted to type:scope/status:robust-qualitative with three explicit consequences. Closes F5.
- **Reverse-KL uniqueness theorem** (commit `f70fb68`, citations corrected in `e777f01`). Under the chain-rule additivity axiom (Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980 / Aczél-Daróczy 1975), reverse-KL is uniquely forced within the direction-forced f-divergence family. Axiom AAD-internally motivated as divergence-level analog of #der-chain-confidence-decay. Concrete χ² counterexample exhibited.
- **A2' strengthening** (commit `80b40d2`). Sub-scope partition α (A2' derived) vs β (A2' assumed). Prop A.1S region condition lifted via stopping-time localization (Khasminskii 2012). Sub-scope label inherited by sector-persistence-template instances.
- **Phase 4: C-BP3 calibration laboratory** (commit `d0373fc`). TST reframed as "privileged high-identifiability calibration laboratory" with transfer-assumption table for five AAD-core quantities. Closes F15.
- **Phase 7: C-BP2 separability pattern** (commit `72ca532`). New meta-segment `#disc-separability-pattern` (six ladders enumerated; positive-half complement to `#disc-identifiability-floor`). Three-part meta-segment family: #disc-independence-audit + #disc-approximation-tiering + #disc-separability-pattern.
- **Citation audit of reverse-KL work** (commit `e777f01`). Three wrong attributions corrected (Csiszár 1972, Amari 2009 Theorem 1, Amari-Cichocki 2010 Prop 3.2 do not contain the claimed chain-rule uniqueness theorem); Eguchi 1983 venue corrected. Audit trail preserved in-segment. Three PDFs saved to `ref/`.
- **Phase 5: G-BP1 logit scoping — partial execution** (commit `a39dfb7`). Third Cauchy-functional-equation uniqueness theorem: under the evidential-additivity axiom (Bayesian independent-evidence updates add in a fixed coordinate), log-odds is uniquely forced up to positive affine. Axiom AAD-internally motivated as update-level analog of #der-chain-confidence-decay. New appendix segment `#deriv-edge-update-natural-parameter`. Finding 2 (unbounded gradient mechanical break in #disc-credit-assignment-boundary) resolved by restating default signal in log-odds (domain ℝ, no mechanical break). Props B.1-B.7 retained in moment-parameter form (Fisher-equivalent); full restatement deferred to future G-BP3.
- **New meta-pattern discovered** (cascaded observation, commit `a39dfb7` and prior). Three independent uniqueness theorems (chain-confidence-decay, reverse-KL, log-odds) share structural shape: Cauchy-functional-equation argument on an AAD-internally-motivated additivity axiom forces logarithmic coordinates. Documented as §SP-1 in `_obs/architectural-proposals-2026-04-22.md`; candidate for promotion to explicit meta-segment (`#additive-decomposition-pattern`) in a future session.

### 2026-04-22 strengthening cycle — COMPLETE (commits `14a6095`, `b6134c2`, `4d050c8`, `b91493c`, `a14682e`)

Followed Joseph's strengthen-first-before-soften posture (`feedback_strengthen_before_soften.md`): for each finding with a softening repair on file, attempted the strengthening first; only fell back to softening if strengthening failed. Outcomes:

- **F1 — strengthening succeeded.** No-go theorem: under purely on-policy execution with sequential short-circuit, no detection mechanism can distinguish an L0-insufficient world from an L0-sufficient world matched on regime conditionals. Tier: *exact* for shallow strict-prerequisite cases; *robust qualitative* for general DAG topology. Five boundary routes characterized. The covariance test under joint sibling observability is now the unique broadly-available violation of the no-go's scope — sharpening the load-bearing role of `#der-loop-interventional-access`. Predecessor softening repair retained as historical fallback.

- **F7 — strengthening succeeded.** Per-quantity exactness audit: ~14 AAD-relevant estimators in three blocks (TST operational, causal-discovery substrate, multi-agent observable structure) are exact functions of $\mathcal{C}_t^{\text{commit}}$. Conditional maximality: under cryptographic immutability, cryptographic authorship, standard universal retrieval, and mainline-bounded scope, $\mathcal{C}_t^{\text{commit}}$ is the unique maximal exteriorized subset of $\mathcal{C}_t$. Estimator-of-AAD-quantity bias separated as a third Consequence clause. $\mathcal{C}_t^{\text{commit}}$ added to NOTATION.md.

- **F10 — strengthening (status upgrade).** `#form-information-bottleneck` reclassified from `discussion-grade` to `exact` (applied external theorem: Tishby, Pereira & Bialek 1999), with three-paragraph Epistemic Status rewrite naming the AAD binding ($X = \mathcal{C}_t$, $T = M_t$, $Y =$ future-obs) and the Markov-chain factorization holding by construction.

- **F13 — strengthening succeeded for observable-$C$; refuted for unobservable-$C$.** New Prop B.7 in `#deriv-strategic-dynamics` derives the L1' sector transfer with five-way gating $\alpha_{L1'} = \min(1/(n_C+1), \min_j \theta_C \pi_{j\mid C}/(n_{j\mid C}+1), \min_j (1-\theta_C)\pi_{j\mid \neg C}/(n_{j\mid \neg C}+1))$ under observable common cause and facilitator monotonicity. Reduces correctly to B.6 in the strict-prerequisite limit. The unobservable-$C$ single-channel case is *refuted* by the Cramér-Rao floor (Fisher information matrix is rank 1 with factorization $\mathcal{F} = uu^T/(\mu\bar\mu)$ where $u = (\Delta_j, \theta_C, 1-\theta_C)$). Repair routes: augment $C$-observability, run multi-child joint observation, or fall back to plan-level marginal tracking. `#def-strategy-dag` Correlation Hierarchy extended to four rows.

- **New meta-segment `#disc-identifiability-floor`.** Names the emerging pattern of structural no-go results in AAD — limits derived from external information-theoretic theorems (Pearl/Bareinboim CHT for F1; Cramér-Rao for F13). Three adjacent open extensions surfaced: causal-IB for interventional relevance, misspecification-cost quantification, tier-switching policy cost.

- **AI integration pass (Phases A–D).** Implemented the AAD-vs-Active-Inference positioning spike's §H Overlap+Underclaim findings:
  - Phase A: G-BP2 V-medium executed — variational form replaces Shannon-MI in `#form-strategy-complexity-cost` (closes Gemini Finding 2/3); related cross-refs in `#disc-compression-operations`, `#disc-exploit-explore-deliberate`, `#disc-ciy-unified-objective`.
  - Phase B: Honest credit to action-perception-loop framing (Friston 2017, Parr & Pezzulo 2022, Wiener 1948, Conant & Ashby 1970) in `#der-loop-interventional-access` with three distinctive AAD moves named; honest credit to hierarchical-generative-model lineage (Friston 2008/2010, Clark 2013, Hohwy 2013) in `#disc-compression-operations` with three structural additions named.
  - Phase C: Aguilera 2022 FEP-flow narrowing contrast in `#result-sector-persistence-template`; Bruineberg 2022 Pearl-blanket vs Friston-blanket distinction in `#der-directed-separation` (AAD as conservative form); Sun & Firestone 2020 dark-room contrast in `#def-satisfaction-gap`/`#def-control-regret`.
  - Phase D: VFE accuracy-complexity equivalence in `#form-information-bottleneck` (Friston 2010/2017, Parr & Pezzulo 2022, Tishby & Zaslavsky 2015).

### 2026-04-22 audit-trio + Codex round-2 cycle — COMPLETE (commits before strengthening)

The morning's audit trio (Gemini, Codex round-1, Opus) and the afternoon Codex round-2 audit produced the 15-finding pending list and 14 architectural proposals (`_obs/architectural-proposals-2026-04-22.md`). The strengthening cycle resolved 4 directly + 3 partially + 1 by V-medium G-BP2; remaining are listed in the Pending Findings section above.

### 2026-04-21 audit cycle — COMPLETE (commits `6d3f219`, `98179f9`, `70c306d`, `ba2597c`, `499afa3`, `1c3a2d9`, `853888c`)

Session plan derived from `msc/opus-audit-2026-04-21.md`. Summary of what landed:

- **Session A** — `#result-sector-persistence-template` factored out as shared lemma; six persistence-flavored segments re-expressed as template instances. Four honesty fixes.
- **Session B** — `#deriv-graph-structure-uniqueness` reframed as Cox-analog; two new meta-segments: `#disc-independence-audit` and `#disc-approximation-tiering`.
- **Session C** — Scope gates in `#form-composition-closure`, `#def-unity-dimensions` lead rewritten, `#obs-software-epistemic-properties` P1 codebase-vs-environment scoping, `section-ii-survival` statement-level-vs-operational distinction, FORMAT.md promotion-workflow reverse-check.
- **Session D** — Scoping spike `msc/spike-ib-unification-plan.md` delivered; execution absorbed into `#disc-compression-operations` segment with three integration edits.
- **Late-cycle Gemini batch** — L1 soft-facilitator gap handled; Finding A and Finding B (composition-closure temporal coarse-graining; observation-ambiguity-modulation architecture-contamination) both closed 2026-04-22.

### 2026-04-02 Codex round-2 findings — COMPLETE

All numbered items from the round-2 review resolved in segments. Full history in `msc/analysis-2026-04-02-round2.md`.

### 2026-03-13 consolidated review — mostly COMPLETE

Top issues (1) directed-separation architectural classification, (2) $\alpha$-vs-$\mathcal{T}$ distinction, (3) composition-closure bridge lemma, (4) graph uniqueness at theorem strength, (6) assorted formal issues — all landed. Remaining: (5) `#hyp-causal-discovery-from-git` now written; TST overstatement of causal status of git data is covered within that segment.
