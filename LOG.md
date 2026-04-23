# LOG.md — Cycle History

This file records cycle-by-cycle narrative for completed audit/strengthening/brainstorm cycles. **It is archaeology, not load-bearing for current work.** Fresh agents should read `CLAUDE.md` (architectural state) and `TODO.md` (active work) first; come here only when the *origin* of a current commitment matters — for instance, when judging whether a "settled" item rests on derivation or on a cycle's working consensus, or when an audit finding's prior status helps decide a current routing call.

`TODO.md §Archive` records work landed at the commit/finding granularity; this file records the *theoretical* contributions and structural moves that shaped the framework's current shape. The two are complementary: TODO.md says *what shipped*, LOG.md says *what changed about how the theory thinks*.

Entries are ordered most-recent-first.

---

## 2026-04-23 — Naming Pilot: Role-Prefix Discipline + Scope Split

**What changed about how the theory thinks.** Two structural moves landed alongside the mechanical pilot.

*Scope is now two first-class scopes, not one nested condition.* The old `#scope-condition` named nothing — "condition" is a filler word that described the segment's role (stating some condition) rather than the thing being defined. The segment actually defined two nested scopes in one file: $\mathcal{S}_\text{adaptive}$ (observations exist + residual uncertainty — Section I's applicability) and $\mathcal{S}_\text{agency}$ (adaptive + at least binary choice + Pearl-level-2 causal contrast — Section II/III's applicability). Downstream segments referenced `#scope-condition` to mean whichever scope they actually needed, with the prose having to compensate. The split into `#scope-adaptive-system` + `#scope-agency` makes each dependency precise: segments that need only observation-under-uncertainty point at the outer scope; segments that need action-with-effect point at the inner. The dependency graph sharpens; prose that had to qualify "conditions 1-2" vs "conditions 3-4" becomes direct xref; the `scope-condition` name retires. Conditions 1-2 live in `scope-adaptive-system.md`; conditions 3-4 live in `scope-agency.md` with `scope-adaptive-system` as its own scope-prerequisite dependency.

*Role-prefix discipline: slug = `{type}-{meaningful-unique-name}`.* The pilot validated that front-loading the segment's type (from the FORMAT.md type vocabulary) in its slug reads cleanly in cross-references and sharpens the dependency graph. `#scope-logogenic-agent`, `#scope-developer-agent`, `#scope-composite-agent`, `#scope-adaptive-system`, `#scope-agency`, `#discussion-identifiability-floor`, `#discussion-separability-pattern`, `#discussion-additive-coordinate-forcing` all read naturally. The meaningful-unique-name half of the rule is enforced: "condition", "pattern" as subject-nouns are placeholders and fail the rule; "adaptive system", "agency", "identifiability floor" do not. Pilot observation: compound renames (changing subject-noun) require hand content-work beyond the mechanical rename; the two such compound moves Round-1 had surfaced (`separability-pattern` → `-ladder`; `additive-coordinate-forcing` → `-forced-coordinates`) are deferred to refined Round 1 / Round 2, which is the appropriate process for subject-noun judgment.

**Artefacts landed.** `bin/rename-slug` (Ruby, deterministic regex rename with pre/post safety checks, stale-text scan, framing reminder, merge-confirmation, post-check lint); `msc/naming-pilot-rename-plan.md` (frozen rename-mapping record, glob-excluded from future rename sweeps); seven slug changes including one 1:2 semantic split; H1, formal-tag, type-field, status-field and prose cleanups on the seven segments; OUTLINE, CLAUDE, TODO, LEXICON, MIGRATION-MAP, FORMAT consistency. Side-resolution: Finding 14 Option A (`#scope-developer-agent` status downgrade) closed by the type: `definition` → `scope` + status: `exact` → `axiomatic` change that the rename's identity shift implies.

**Next.** Principles-file rewrite folding in the 11 Round-1 insights + pilot-validation observations; refined Round 1; aggregation + Round 2 + collision audit + landing. Role-prefix is now an architectural invariant for the refined rounds, not a vote target.

---

## 2026-04-24 — Architectural-Proposals Consolidation Audit

**No new theoretical content.** Breadth-compression pass on `msc/architectural-proposals-2026-04-22.md` after three depth-heavy cycles (2026-04-22/23 cascading strengthening; 2026-04-23 Gap A/B; 2026-04-24 Gemini pressure-point) produced ~30+ proposal entries in one 1034-line document that was no longer navigable. Six parallel cluster agents audited the portfolio plus all segment Working Notes plus the pending-findings / joseph-working-notes / reflections loci, producing a consolidated replacement at top-level `PROPOSALS.md` with the old file moved to `_obs/`.

**Portfolio triage:**

- **Eight proposals retired as fully absorbed.** O-BP14 (derivation-audit table convention, commit `c1d9fcf`), C-BP2 (master separability pattern, commit `72ca532`), C-BP3 (software as calibration laboratory, commit `d0373fc`), O-BP6 (agent-identity promotion, commit `2980327`; subsequently extended with (PI) axiom during 2026-04-23 Gap A/B cycle), G-BP1 (natural-parameter / logit reparameterization, commit `a39dfb7`; produced the `#edge-update-natural-parameter` uniqueness theorem that became a third primary instance of `#additive-coordinate-forcing`), G-BP2 V-medium (variational strategy-cost framing, commit `a14682e`; plus cascading-strengthening enrichments in `0a772d2` / `f70fb68` / `b76ee67`), SP-1 + SP-2 (three-layer additive-coordinate-forcing pattern, commit `7456ec3`; plus Čencov 4th primary instance from Gap A/B cycle), and the closing meta-observation on "framework's honesty is load-bearing" (now CLAUDE.md §7 element (a)). All eight are listed with landing-location pointers in PROPOSALS.md §A.

- **Six proposals retired as superseded or absorbed-distributed.** O-BP2 (four compressions as one hierarchy — split into three descendants across 2026-04-21 / 2026-04-24 / SP-9), O-BP7 (known structural absences meta-proposal — distributed into `#discussion-identifiability-floor` §Adjacent Floors and `#approximation-tiering` Working Notes), O-BP3 (continuous-parameter approximation tiering — materially depends on G-BP3 which is itself hollowed out), O-BP4 (continuous-valued strategy DAG — dedicated scoping spike has been queued without progress since 2026-04-22; AND/OR convergence counterweight is real; retire and reopen only if a specific domain forces it), O-BP5 (orient cascade as recursive AAD — absorbs naturally into Bundle 1 framework-face reframe), SP-5 (Reader's Path — deferred behind Bundle 1 stabilization).

- **Two cross-cutting bundles surfaced as the portfolio's highest-leverage organizing moves.** **Bundle 1 "framework-face reframe"** (SP-7 + O-BP1 + O-BP10 + O-BP8 + SP-3 + SP-4 + SP-8): seven proposals converging on a coordinated reframing pass where three independent frontier-model audits converged on shifting AAD's self-presentation from "integration of four disciplines" to "epistemic architecture with three-part meta-structure plus integrating content." Value **+9 framework / +10 paper**. README still reads integration-first at line 10; CLAUDE.md §7 and OUTLINE.md "Reading AAD" preamble already carry the new framing — coordinated pass would catch the public-facing surface up to the internal framing. **Bundle 2 "Section III completion"** (O-BP16 + O-BP9 + SP-6-residue + SP-11 + SP-17): five proposals closing all four named Section III OUTLINE GAPs (latent structural diversity; endogenous coupling γ emergence; composition transition dynamics per Miller 2022; computational thresholds for social behavior per Miller 2022 ICE) plus F26 and F8. Value **+7 framework completeness**. Addresses AAD's explicitly-acknowledged structural weakest section.

- **Six new architectural candidates surfaced from segment Working Notes + reflections + brainstorm documents** that the prior portfolio never captured. **SP-11 Composition-monotonicity meta-segment** — the most load-bearing unpromoted item; the C2 spike's honest-negative-result explicitly produced material for a fourth Section-III-native meta-segment parallel to the existing three-part epistemic architecture (`#additive-coordinate-forcing` / `#discussion-identifiability-floor` / `#discussion-separability-pattern`); never promoted past a TODO bullet. **SP-12 Commitment / resource / temporal DAG extensions** — named in CLAUDE.md "Known Fragilities" but homeless in portfolio until now. **SP-13 Emergence conditions as formal primitive** — named across three reflections as "the next section I would write if truly owning this project," absent from prior portfolio entirely; prerequisite for `04-logozoetic-agents/`. **SP-14 Observation-channel capacity $C^{(k)}$** — `#persistence-cost` Working Note self-labels "biggest architectural opening from this theorem." **SP-15 Template-family naming (sector / contraction / dissipativity trio)**, **SP-17 Goal-information-leakage $\mathcal{L}_{G \to M}^c$ as first-class Section-III quantity**, **SP-19 Naming consolidation pass (Cauchy-coordinates / separability-ladder)** round out the newly-surfaced candidates. Cluster-F agent identified these against the full proposals doc to rule out duplication.

- **Per-proposal independence-of-execution markers added** on Joseph's request. High/medium/low rating indicating whether a proposal can be worked on in parallel with other active proposals without merge or semantic conflict. Intended as a practical scheduling aid: bundles that parallelize safely can be run concurrently; low-independence proposals (naming passes, cross-cutting convention applications, meta-segment rewrites) must serialize.

**Structural observations from the audit:**

- **Portfolio bloat was genuine.** 33 proposals → 8 absorbed-retirement + 6 superseded-retirement + 15 active (including 6 newly-surfaced) + 3 wait-gated = 24 active and near-active entries. Absorption + retirement rate: 14/33 = 42%.

- **Three proposals were *strengthened* by subsequent landings that the entry didn't reflect.** O-BP10 (projection-contraction slogan) became mathematically defensible after the 2026-04-24 DA2'-inc ≡ (CT2)-at-$M=I$ equivalence landed in `#composition-closure`. O-BP6 (agent-identity scope promotion) was used as foundation for the (PI) axiom subsequently added. G-BP1 (logit reparameterization) produced a strengthened uniqueness theorem that became a primary instance of `#additive-coordinate-forcing`. This "strengthen-underneath" pattern is structurally inevitable in a project alternating depth and breadth-compression cycles; future audits should surface it as a first-class condition.

- **One proposal had its portfolio *expanded* underneath it.** O-BP11 (observability as master variable) predates `#agent-opacity`, `#interaction-channel-classification`, and `#discussion-identifiability-floor` Instance 3, all of which added observability structure the original entry doesn't anticipate. Scoping is now mandatory before any landing decision — the instance list and effort estimate are stale.

- **Section III is structurally under-represented in the portfolio.** The OUTLINE names four explicit GAPs in Section III (lines 145–148); only two prior proposals (O-BP16, SP-6) addressed them; the 2026-04-24 audit added three (SP-11, SP-17, plus the O-BP9 repositioning as Section-III-completion). Bundle 2 now carries the correct Section III weight.

- **The depth/breadth alternation discipline is showing.** Three depth-heavy cycles produced enough new work that the breadth-compression audit could meaningfully consolidate. The pattern observed in prior consolidation — that naming + organizing passes produce disproportionate value — held. PROPOSALS.md's new structure preserves this by bundling ("what the real work-items are") rather than cataloging ("what proposals exist in order of submission").

**Process output:** `PROPOSALS.md` at repository root (replaces `msc/architectural-proposals-2026-04-22.md`). Old file moved to `_obs/architectural-proposals-2026-04-22.md` with supersession header. TODO.md §"Active — Strategic Architectural Proposals" updated to point at PROPOSALS.md. Reflection in `msc/reflections/20-breadth-compression-and-the-proposals-audit.md` captures the synthesis trail.

---

## 2026-04-24 — Gemini Pressure-Point Cycle

External Gemini audit via `msc/joseph-working-notes.md` flagged five pressure points against AAD's Section II/III content: (#1) composition bridge lemma verified only for linear-Kalman; (#2) IB purity — Shannon-zero / Forward-KL-infinity / reverse-KL fix framed as "abandoned IB purity"; (#3) multiplicative $\rho$-factorization failed; (#4) neutral-drift blindness under $(\alpha, \rho, R)$-only state-space; (#5) missing constant $C$ in Class-2 bias bound. #6 (directed separation fails for LLMs) was skipped as a known structural scope-exit. Five parallel strengthening spikes launched (one per pressure point) plus four cross-cutting follow-up spikes (Instance-4 triage; Fenchel-Bregman reframe of `#additive-coordinate-forcing`; KL-to-state-distance template extraction; Path 1 PDF-verification addendum against newly-acquired TP2011 / Rubin 2012 / Levine 2018). **All nine spikes respected the strengthen-first posture; none softened.**

**Tier 1 landed (commits `6102a93` reasoning trail + `b76ee67` theory landing). Six bundled items:**

1. **`#strategy-cost-regret-bound` bundled update** (one segment, seven sub-moves): §4 refactored so that the **Bretagnolle-Huber identity** $D_{\mathrm{KL}}(\pi^\ast \Vert Q) = -\log(1 - \mathrm{TV})$ exact under deterministic $\pi^\ast$ replaces Pinsker as primary bound with matching lower bound $\Delta_{\min}(1 - e^{-D_{\mathrm{KL}}})$; §5 adds **asymmetry-from-one-sidedness** paragraph as second leg of direction-forcing independent of chain-rule; §6.3 **Bregman-Fenchel identification** ties reverse-KL (divergence layer) to log-odds (update layer, `#edge-update-natural-parameter`) as Fenchel-dual coordinates of one negative-entropy Legendre-Fenchel pair; §6.4 new subsection **"Information-theoretic-MDP lineage and AAD's direction choice"** positions AAD's $\pi^\ast$-first direction as distinctive within TP2011 / Rubin 2012 / Levine 2018 lineage (all three put agent-first; AAD's optimum-first is forced by regret-bound + BH-identity tightness); Rubin 2012 Theorem 3 PAC-Bayesian generalization bound added as fourth independent motivation for KL-to-reference form; §6.1 Shore-Johnson / Sanov / Hobson structural-equivalence note; Bishop-vs-AAD "reverse-KL" naming-collision footnote.

2. **Structural-transparency lift** across three segments: `#composition-closure` Discussion explicitly states **DA2'-inc ≡ (CT2)-at-$M=I$ equivalence** for $C^1$ $F$ on convex domains (Rockafellar-Wets 1998 Cor 12.4; Nesterov 2004 §2.1.3), making Euclidean metric-α₁ cases AAD-internally-derived without new axiom; `#contraction-template` honest-failure-modes sharpens adversarial-half statement to name **three independent convergent obstructions** (Slotine 2003 compositional applicability / passivity universality / Daskalakis et al. 2018 last-iterate non-convergence); `#sector-condition-derivation` sub-scope β entry for rule-based/discontinuous sharpened to **structural Lipschitz-floor scope-exit** with constructive counterexample, citing hybrid-dissipative framework (van der Schaft-Schumacher 2000).

3. **New appendix `#bias-bound-derivation`**: derives the constant $C$ in the Class-2 observation-ambiguity bias bound under two named sub-scopes. Track 1 (transport-inequality, linear in $I$) under (H1) statistical-manifold + (H2) log-Sobolev + (H3) Lipschitz-posterior (Stuart 2010) gives $C_{W_2}^2 = 2L_{\mathrm{post}}^2/\rho_{\mathrm{LSI}}$. Track 2 (Fisher-Rao, $\sqrt I$ scaling) under (H1)+(H4) small-information + (PI)+Čencov gives universal dimension-free $C_{FR} = \sqrt 2$. Attempt E no-go: universal-$C$ under Euclidean-parameter norm fails (heteroscedastic-normal counterexample) — **(PI) axiom is load-bearing** for the derivation, not coincidental. Two failed alternative routes documented (Cramér-Rao inversion wrong direction; rate-distortion inversion wrong problem structure). Gaussian worked example with explicit numerical constants. Upgrades `#observation-ambiguity-modulation` and `#section-ii-survival` from "order-of-magnitude guidance" to "conditional theorem (exact under H1-H3 or H1+H4)."

4. **`#information-bottleneck` cross-reference paragraph**: distinguishes canonical IB lineage (MI-to-observable) from information-theoretic-MDP lineage (KL-to-reference-policy) as sibling forms descended from Shannon rate-distortion, neither reducible to the other without change of relevance variable. Pre-empts "abandoned IB purity" framings at the meta-segment level.

5. **`#loop-interventional-access` two-mode deployment subsection**: names Mode 1 agent-self-intervention (Instance 1, causal-structure layer) and Mode 2 observer-on-sub-agent (Instance 3, composition layer) as semantically-distinct Pearl-$do$ deployments sharing the unification at *pattern* level (Level-2 escape from observational-equivalence no-goes) but not at *mechanism* level. Positions for Mode 3 (observer-on-agent-input) when Instance 4 promotes.

6. **`ref/INDEX.md` TP2011 title correction**: "The Information Theory of Decision and Action" (singular — corrected from plural "Information theory of decisions and actions" which had been back-propagated from Rubin 2012's reference [10]). Three new PDFs acquired in `ref/` with canonical names and page/equation-level INDEX entries.

**What Gemini's pressure points look like post-Tier-1:**
- #1 bridge lemma → closed (structural transparency lift + sharp scope exits via N1 Lipschitz floor + N2 adversarial three-obstruction convergence).
- #2 IB purity → closed (BH identity + Fenchel-Bregman duality + info-theoretic-MDP-lineage reframe + PAC-Bayesian motivation).
- #5 constant $C$ → closed (two theorem tracks + no-go justifying (PI) as load-bearing).
- #3 ρ-factorization → Tier 2 (awaits `#rho-decomposition` appendix with (AV) variance-additive theorem + sub-regime catalog).
- #4 neutral drift → Tier 2/3 (awaits Instance-4 Kalman-Ho closed-form follow-up spike).

**Path 1 PDF verification found one contradicted attribution and strengthened the lineage reframe.** The spike's Claim A — that TP2011 presents the objective $\max_\pi \mathbb E[R] - \beta^{-1}I(\Pi;X)$ with $I(\Pi;X)$ as expected KL-to-reference policy — was contradicted at formula level. TP2011's actual central quantity is *Information-to-Go* $\mathfrak{I}^\pi$, the multi-information of the entire future trajectory (Eq. 15 p. 19); the KL-to-reference form the spike attributed is Rubin-Shamir-Tishby 2012's (Eq. 3 p. 4). Path 1's rhetorical centerpiece "reverse-KL IS IB under the right relevance variable" does not survive PDF scrutiny; the reframed landing — "AAD's $\pi^\ast$-first direction is distinctive within the info-theoretic-MDP lineage, owned rather than inherited, forced by regret-bound + BH identity" — is weaker rhetorically but PDF-defensible and still closes Gemini's "abandoned IB purity" framing. Bonus: Rubin 2012 Theorem 3 PAC-Bayesian bound was surfaced as a fourth independent motivation for the KL-to-reference form that the original spike did not identify.

**Cross-spike structural discoveries (follow-up spikes):**

- **Instance-4 triage** resolved the multi-candidate question as two-genuine-new-primary-instances + one-sub-statement + one-redirect: Candidate 2 agent-internal-architecture layer (dual-anchored by CHT-at-agent-as-SCM and Kalman-Ho canonical-form non-uniqueness) as genuine Instance 4; Candidate 4 mechanism-design (Arrow / Gibbard-Satterthwaite / Myerson-Satterthwaite) as genuine Instance 5 under broad reading with honest implementability-vs-identifiability theorem-family labeling; Candidate 1 ρ-factorization projects onto Candidate 2 at disturbance-statistic layer (cross-reference, not standalone); Candidate 3 constant-$C$ is a downstream theorem of `#additive-coordinate-forcing`'s fourth primary instance, not a floor instance (fails E4 single-escape criterion). Meta-segment capacity is bounded, not unbounded: tighter criterion "each instance elevates distinct load-bearing machinery" supplies principled termination. Projected stable endpoint 6-8 instances.

- **Fenchel-Bregman reframe** verified Path 7's duality computation as exact (standard Legendre-Fenchel on categorical-distribution simplex with negative-entropy potential). Honest framing stronger than either extreme: **"one geometric object (exponential-family Legendre-Fenchel on categorical distributions) + four independently-motivated AAD-internal axioms converging on it + four segment manifestations"** — richer than both the naive Path-7 reframe (which under-unifies by collapsing axiom independence) and the current 1-anchor-plus-3-theorem framing (which over-separates by treating four layer-surfaces as parallel). The three theorem-level axioms (chain-rule additivity / evidential additivity / parameterization-invariance) are logically independent despite producing Fenchel-dual coordinates. Bonus: classifies candidate Instance-4 floor-candidates by Bregman geometry — (AV) ρ-factorization lives on *squared-norm* Bregman (parallel meta-pattern), not on negative-entropy; architecture/constant-$C$ fall outside the Fenchel structure entirely. The reframe is proposed as a Tier-3 architectural move (deserves its own proposal entry); the local Bregman-Fenchel identification landed in `#strategy-cost-regret-bound` §6.3 at Tier 1.

- **KL-to-state-distance template extraction** recommended Option B (narrow `#posterior-displacement-template` on the Otto-Villani + Lipschitz-posterior cascade) over Option A (unified template subsuming both clients) and Option C (no extraction). The shared machinery across `#variational-sector-condition` and the proposed `#bias-bound-derivation` is *only Pinsker's first step*, not the full cascade; `#variational-sector-condition` belongs as adjacent family member, not primary instance. Template execution contingent on `#bias-bound-derivation` landing first (now done) + at least one of three forward-looking clients (causal-IB, misspecification-cost, composition-scope-robustness) materializing. Tier 3.

**Ancillary session work** (not theory content but relevant to cycle state): outline ordering violations cleared (four initial violations; two resolved via OUTLINE row moves, two via bidirectional-frontmatter-dependency cleanup on `chronica.depends` and `value-object.depends`); naming strategic sweep brainstorm paper written (`msc/naming-brainstorm-2026-04-24.md`) opening the naming-sweep conversation.

Segment count: 109 → 110. Nine spike files retained in `msc/` as reasoning trails. Tier 2 items (`#rho-decomposition`, `#dissipativity-template`, Instance 4 / Instance 5 promotions, `#posterior-displacement-template`, Fenchel-Bregman meta-segment reframe) queued for future cycles.

---

## 2026-04-23 — Gemini Gap A/B Cycle

Twelve parallel research spikes against two gaps surfaced in Gemini's audit: (A) default signal function validation under correlated failures (L1'/L2); (B) contraction assumptions verified only for linear Kalman-type, needing extension to broader agent classes. A follow-up spike (Jacobian-level B1 strengthening) tested whether B1's metric-α₂ derivations could be made AAD-internal rather than theorem-imported; its mixed-lift three-layer result became load-bearing for the landing epistemic labeling. An H_b agent-opacity spike (from Hafez 2026) closed the long-flagged `#adversarial-edge-targeting` Section III gap.

**Six new segments landed:**
- `#contraction-template` — Lohmiller-Slotine metric generalization of `#sector-persistence-template` with 5 α promotions, topology-indexed closures, heterogeneous (CM2-M)
- `#strategic-composition` — equilibrium-convergence framing for partially-opposing $O_t^{(i)}$ under Monderer-Shapley / Rosen
- `#fisher-whitened-update-rule`
- `#l1-update-bias`
- `#variational-sector-condition`
- `#agent-opacity` — $H_b^{A\mid B}$ with sign-flip derived via signed coupling, emitter-side four-regime classification, 16-cell composition closing adversarial-edge-targeting

**Four structural additions to existing meta-architecture:**
- Instance 3 in `#discussion-identifiability-floor` (composition-layer no-go via Liberzon 2003 common-Lyapunov nonexistence)
- Fourth primary instance in `#additive-coordinate-forcing` (Čencov-invariance at metric layer under the new (PI) axiom in `#agent-identity`; 1-anchor-plus-2-theorem → 1-anchor-plus-3-theorem)
- Seventh ladder in `#discussion-separability-pattern` (A2'-scope metric-α₁/α₂/β)
- (C-iv) scope route in `#scope-composite-agent`

**Two new commitments:**
- **(PI) parameterization-invariance axiom** adopted as natural extension of `#agent-identity`'s singular-trajectory commitment: AAD's predictions should not depend on arbitrary choice of coordinates on $M_t$.
- **Monotone-operator-theory lineage** (Rockafellar 1970 / Bauschke-Combettes 2017) explicitly acknowledged in `#sector-persistence-template` and `#sector-condition-derivation` — AAD is a specialization (one-point anchoring; Model D/S decomposition; identifiability-floor composition; composition-consistency; α/β epistemic labeling are AAD-distinctive).

Segment count: 103 → 109. Thirteen spike files retained in `msc/` as reasoning trails.

**Cross-segment reverse-check** (Gate-3-sidebar per `FORMAT.md`) on the six newly-promoted segments is flagged in TODO as future-session work — the spike-to-segment compression should be verified against the original spike content to confirm no over-aggressive compression. Each spike is preserved in `msc/spike-*.md` per `feedback_math_lives_in_segments`.

---

## 2026-04-23 — Brainstorm Cycle

Seven commits: `0d7b987`, `591e8b6`, `13fe242`, `b48cdee`, `77a9bde`, `0bd859e`, `a739e9a`. Seven parallel research spikes prompted by an external-framework comparison (GAA Baigozin 2025) as a brainstorming exercise. Six of the seven promoted to new segments; one (internal-external decomposition) was deferred after the $\rho$-factorization spike returned an honest obstruction. Segment count: 96 → 103.

**Substantive theoretical contributions:**

1. **`#critical-mass-composition`** — closed-form composite sector constant $(\alpha-C)R \gt \rho + \gamma\mathcal T$ for the symmetric-matched-Tier-1 dyad via joint quadratic Lyapunov. Sign-sensitive refinement of the weakest-link bound; recovers `#team-persistence` (cooperative $\gamma \lt 0$) and `#adversarial-destabilization` (adversarial $\gamma \gt 0$) as signed special cases; formalizes `#symbiogenic-composition` (S-3) autonomy-reduction as asymmetric-parameter weighted-Lyapunov limit. Closes long-standing Section III bridge-lemma opening.

2. **`#interaction-channel-classification`** — four-regime recipient-side theory (Informative / magnitude-shock / structural-shock / ambient-noise) with boundaries in existing AAD quantities. Regime-typed $\rho_B^{\text{eff}}$ decomposition with negative Regime-I term generalizes cooperative-action coupling. Pairs with the `#adversarial-edge-targeting` Section III GAP as recipient-classifier + emitter-optimizer. Surfaces the Regime-I-with-adversarial-content informational attack that the emitter-side scalar cannot express.

3. **`#consolidation-dynamics`** — offline regime of `#recursive-update`'s between-event dynamics with IB-gap-reduction objective. Names the **stability-plasticity feasibility window** that closes an asymmetry in `#strategy-persistence-schema` (plasticity lower bound only, no stability upper bound). Required as architectural primitive in `03-logogenic-agents/` under context-turnover.

4. **`#persistence-cost`** — sustained information rate $\dot R \geq n\alpha/2$ nats/time under Model S + Gaussian-OU (Shannon RDF + Prop A.1S; Kalman-Bucy saturates per Mitter-Newton 2005). Channel-capacity prerequisite $C \geq \mathcal T/2$ opens as first-class persistence diagnostic.

5. **`#adaptive-gain-dynamics`** — A2' sub-scope partition refined from $\alpha$/$\beta$ to $\alpha_1$/$\alpha_2$/$\beta$ via augmented-state Lyapunov composition under meta-gain conditions (MG-1)–(MG-4). Adaptive Kalman, AMSGrad, IMM, MAML classified.

6. **`#detection-latency`** — within-class regime-change detection latency $\Omega((n_{\min}+1)/\varepsilon)$ **structurally forced** by composition of `#edge-update-natural-parameter`'s Aczél-Cauchy-FE log-odds with Beta-Bernoulli $\eta_{\text{edge}} = 1/(n+1)$. Sharpens the forgetting prerequisite to "also required for bounded detection latency."

7. **Spike H ($\rho$-factorization, in flight)** returned honest outcome (C) obstruction: multiplicative $\rho = \rho_{\text{external}} \cdot f(\mathcal M) \cdot g(\pi)$ is NOT derivable; native structure is variance-additive $\rho^2 = \rho_{\text{irr}}^2 + \Delta_{\mathcal M}^2 + \Delta_\pi^2 + \text{cross}$. Internal-external decomposition (Spike E) deferred pending variance-additive reframe.

---

## 2026-04-22/23 — Cascading Strengthening Cycle

Nine commits: `0a772d2`, `c1d9fcf`, `2980327`, `f70fb68`, `80b40d2`, `d0373fc`, `72ca532`, `e777f01`, `a39dfb7`. Executed Phases 1–5 and 7 of the post-evening-audit proposed sequence plus two in-flight strengthening spikes.

**Substantive theoretical contributions:**

1. **Three Cauchy-functional-equation uniqueness theorems**, each forcing a logarithmic coordinate via an AAD-internally-motivated additivity axiom: (a) F20 regret-bound derivation → reverse-KL direction forced under deterministic $\pi^\ast$; (b) reverse-KL chain-rule uniqueness under chain-rule additivity axiom (Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980 / Aczél-Daróczy 1975); (c) log-odds evidential-additivity uniqueness (Aczél 1966 Cauchy-functional-equation argument). Landed in new appendix segments `#strategy-cost-regret-bound` and `#edge-update-natural-parameter`.

2. **Discovered structural pattern** (§SP-1 in `msc/architectural-proposals-2026-04-22.md`): the three theorems share a common shape — products of independent factors become additive sums on log-scale coordinates, with each coordinate uniquely forced by an AAD-internally-motivated additivity axiom. Promoted 2026-04-23 to `#additive-coordinate-forcing` meta-segment with the honest **1-anchor-plus-2-theorem** characterization (chain layer = mathematical identity; divergence + update = theorems; Lyapunov + IB Lagrangian documented as adjacent family members). Composes with `#discussion-identifiability-floor` + `#discussion-separability-pattern` as AAD's three-part meta-architecture.

3. **A2' scope partition**: α sub-scope (Kalman/conjugate-Bayesian/gradient-strongly-convex — A2' derived under #gain-sector-bridge directional fidelity) vs β sub-scope (PID/rule-based/human-judgment — A2' assumed). Prop A.1S region condition lifted via stopping-time localization (Khasminskii 2012).

4. **New meta-segment `#discussion-separability-pattern`**: positive-half complement to `#discussion-identifiability-floor`, six ladders enumerated (L0/L1/L1'/L2, C1/C2/C3, Class 1/3/2, Tier 1/2/3, Regime A/B/C, Adaptive/Agency/Composite) under separable-core / structured-repair / general-open shape.

5. **Citation audit** (completed 2026-04-23 in commits `7456ec3`, `6567914`, `f61e62f`): three wrong attributions in the reverse-KL work were corrected (Csiszár 1972 / Amari 2009 Theorem 1 / Amari-Cichocki 2010 Prop 3.2 → Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980 / Aczél-Daróczy 1975). Project-wide audit subsequently ran across all AAD and TST segments — **zero confirmed attribution errors found elsewhere**; reverse-KL's 20-25% rate was a local concentration, not representative. PDF-level verification confirmed Bruineberg 2022's "Pearl-blanket vs Friston-blanket" is verbatim terminology (not AAD paraphrase), Bareinboim CHT = Theorem 1 p.22 of 2022 ACM Books chapter, Aguilera 2022's FEP-narrow-validity claim exactly matches AAD's usage. 5 missing-citation gaps hardened (Tikhonov, Chechik full, Doob-Dynkin, Cox, Cramér). 26 PDFs acquired and canonically named in `ref/`, then **excluded from git** (redistribution rights); `ref/INDEX.md` is the tracked bibliography.

6. **Additional framing moves**: `#agent-identity` promoted to formal scope statement (Section II scope commitment grounds `#loop-interventional-access`); TST reframed as "privileged high-identifiability calibration laboratory" (not "richest operationalization domain"); O-BP14 derivation-table convention landed with applications to five derivation segments.

---

## 2026-04-22 — Strengthening Cycle (Findings 1, 7, 10, 13 + AI integration)

Five commits: `14a6095`, `b6134c2`, `4d050c8`, `b91493c`, `a14682e`. Executed strengthen-first repairs for Findings 1, 7, 10, 13 from the audit-trio batch plus the AI integration pass.

**Landmark contributions:**
- A no-go theorem for on-policy L0-insufficiency detection (Pearl/Bareinboim CHT applied) — `#causal-insufficiency-detection`.
- A derived L1' sector transfer for soft-facilitators under observable common cause (Prop B.7 with facilitator monotonicity) plus Cramér-Rao refutation for the unobservable case — `#strategic-dynamics-derivation`.
- Per-quantity exactness audit for git-derived TST estimators with conditional maximality — `#software-epistemic-properties` + $\mathcal{C}_t^{\text{commit}}$ in NOTATION.md.
- The `#discussion-identifiability-floor` meta-segment naming the structural-no-go pattern.

---

## 2026-04-22 — Audit-Trio + Codex Round-2

Morning audit trio (Gemini, Codex round-1, Opus) and afternoon Codex round-2 audit produced the 15-finding pending list and 14 architectural proposals (`msc/architectural-proposals-2026-04-22.md`). The strengthening cycle that followed resolved 4 findings directly, 3 partially, and 1 by V-medium G-BP2.

This was the cycle that established the three-document pattern (findings doc + proposals doc + TODO navigator) per `feedback_architectural_proposals_vs_findings`.

---

## Earlier History (pointer-only)

- **2026-04-21 audit cycle** (commits `6d3f219`, `98179f9`, `70c306d`, `ba2597c`, `499afa3`, `1c3a2d9`, `853888c`) — IB unification + sector-Lyapunov template factoring landed; six AAD persistence-flavored results re-expressed as instances of `#sector-persistence-template`. See `TODO.md §Archive` for commit-level detail.

- **2026-04-20** — SOC/renormalization speculation (parked in `msc/speculation-soc-composition.md`); Section III unity-closure investigation (`msc/spike-unity-closure-mapping.md`, `msc/spike-mori-zwanzig-composition.md`) finding two-axis closure structure exposing gap in `#unity-dimensions`.

- **2026-04-16** — ACT → AAD rename to resolve collision with "AI Consciousness Test" (Schneider & Turner). See `msc/name-transition-aad.md`.

- **2026-04-02** — edge semantics resolved as regime-indexed interpretation (causal efficacy estimate with A/B/C regime classification); `_obs/old-tf-*` files preserved.

- **2026-03-14** — α/T relationship resolved (α proportional to T verified across all correction function classes).

- **2026-03-13** — Three-model consolidated review (Claude Opus, OpenAI Codex, Google Gemini) framed the theory's structural priorities. See `msc/2026-03-13-feedback.md`. Of those: directed-separation scope decision (resolved as architectural classification), α/T relationship (resolved 2026-03-14), composition-closure bridge lemma (tier-specific contraction structure promoted; remaining moves landed in 2026-04-21 cycle).

- **2026-03-11** — TST conversion. The original monolithic TFT documents split into segment files; `02-tst-core/` reorganized with slug filenames and an explicit OUTLINE.md.

- **March 2026** — Spike-driven foundation: `msc/spike-purposeful-agent-derivation.md`, `msc/spike-v3-purposeful-agent.md` (definitive), `msc/spike-graph-uniqueness.md` (DAG with Markov property forced from four operational postulates; acyclicity derived from temporal ordering), `msc/spike-agent-composition.md` (Section III "Composition Dynamics" framed). Codex three-round review established the X_t lift, Level 2 scoping, satisfaction gap / control regret split, directed separation scope condition.

- **March 2026 — terminology rename**: axiom→postulate, theorem→result, proof→derivation; `first-principled` status label → `axiomatic`. See `feedback_terminology_rename.md` in agent memory; the rationale ("avoid physics-envy framing") and the migration applied across all then-existing segments.

- **February 2026** — `msc/agentic-tft-*.md` bridge work absorbed from `~/src/agentic-tft/`: cognitive loop spec, evaluation framework, crèche concept, ontology unification, foundational premises, narrative-as-implementation, experiential training design, review response. Source material for `03-logogenic-agents/` and `04-logozoetic-agents/`.
