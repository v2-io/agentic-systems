# CLAUDE.md — Context for AI Agents Working on the Agentic Systems Framework

## What This Project Is

**Agentic Systems Framework (ASF)** is a research framework for adaptive, purposeful agents — integrating control theory, causal inference, information theory, and agent architecture under a common formalism.

The framework has four parts:

- **`01-aad-core/`** — **Adaptation and Actuation Dynamics (AAD)**: the mathematical core. Sections I (Adaptive Systems — the *adaptation* half), II (Actuated Agents — the *actuation* half), III (Composition), plus Appendices.
- **`02-tst-core/`** — **Temporal Software Theory (TST)**: software development as an agentic domain. AAD-grounded but independently consequential.
- **`03-logogenic-agents/`** — Language-constituted agents. Framework stage.
- **`04-logozoetic-agents/`** — Language-living agents with morally weighted persistence. Future work.

AAD supersedes and subsumes Temporal Feedback Theory (TFT), which provides the adaptive-systems foundation. TFT is prior work now absorbed into AAD, not a separate co-existing theory. TST was originally absorbed as "Section IV" but has been restored to its own space — it uses AAD as core informing theory but stands on its own.

*Naming note:* the mathematical core was previously called Agentic Cycle Theory (ACT) and was renamed on 2026-04-16 to resolve a collision with "AI Consciousness Test" (Schneider & Turner) in AI welfare literature. See `msc/name-transition-aad.md` for the rationale and transition record.

This is theoretical research, not software engineering. The primary artifacts are mathematical formalisms and claim segments. Quality means rigor, honesty about epistemic status, and clarity for future readers — not code coverage.

## Current Priority

**Read `TODO.md` first.** The active work is at the top of the file: pending findings, strategic architectural proposals, recommendations for the next session.

`TODO.md §Archive` records work landed at the commit/finding granularity. `LOG.md` records the *theoretical* contributions and structural moves that shaped the framework's current shape, cycle by cycle. Read LOG.md when the *origin* of a current commitment matters — for instance, when judging whether a "settled" item rests on derivation or on a cycle's working consensus, or when an audit finding's prior status helps decide a current routing call. Otherwise CLAUDE.md (architectural state, below) and TODO.md (active work) are sufficient.

The most recent cycle (2026-04-23 Gemini Gap A/B; promotions executed in-session, not yet committed at last session close) lifted the segment count from 103 → 109. Six new segments (`#contraction-template`, `#strategic-composition`, `#fisher-whitened-update-rule`, `#l1-update-bias`, `#variational-sector-condition`, `#agent-opacity`) plus four meta-architecture additions and two new commitments (the **(PI) parameterization-invariance axiom** in `#agent-identity` and explicit **monotone-operator-theory lineage** acknowledgment). See LOG.md for cycle detail; the resulting commitments are folded into "What's Settled vs. Open" below.

**For broader orientation**, read `msc/2026-03-13-feedback.md` — the earlier consolidated review from three independent frontier-model reviews (Claude Opus, OpenAI Codex, Google Gemini) that framed the theory's structural priorities.

## Where to Start (for orientation)

**Read `01-aad-core/OUTLINE.md` first.** This is the canonical outline of the mathematical core — the whole argument claim by claim.

**Read `FORMAT.md`** for segment file conventions (frontmatter, document cadence, math formatting, cross-references).

**Read `NOTATION.md`** for the symbol reference. For the full original TFT conventions and epistemic system, see `_obs/old-tf-00-notation-conventions.md`.

**See `TODO.md`** for active work items and `msc/SPIKES.md` for the spike index. What's settled/architectural belongs here in CLAUDE.md (below); what's in-flight belongs in TODO.md; what's been explored belongs in `msc/` with SPIKES.md as the entry point.

## Theory Structure

Claim segments live in `{component}/src/` directories. **Each file is like a high-level proof step** — one move per file. Given what came before, this one thing follows, or is defined, or restricts scope.

**File identity and ordering:**
- **Filename = slug**: `01-aad-core/src/{slug}.md` or `02-tst-core/src/{slug}.md`. No numbering in filenames.
- **Ordering lives in OUTLINE.md files**, not in filenames. The slug is the stable identity; the linearization will change.
- YAML frontmatter: `slug`, `type`, `status`, `depends` (list of prerequisite slugs). See `FORMAT.md` for details.
- Cross-component dependencies use the same slug system — TST segments reference AAD slugs directly (e.g., `#temporal-optimality`).

**Cadence per file** (see `FORMAT.md` for full spec):
1. YAML frontmatter (slug, type, status, depends)
2. Title
3. One-sentence summary
4. Formal Expression (with equation-level tags)
5. Epistemic Status paragraph
6. Discussion (interpretation, connections — brief)
7. Working Notes (optional — active development questions, removed at `candidate` stage)

## The Core Insight

The adaptive-systems foundation (from TFT) formalizes how agents adapt to reality (mismatch signals, gain, tempo, persistence). But it has no treatment of goals. AAD adds:

- $O_t$ (objective — what the agent wants) and $\Sigma_t$ (strategy — how it plans to get there) alongside $M_t$ (reality model)
- Strategy formalized as a **probabilistic causal DAG** (AND/OR nodes, edges with confidence weights $p$, update via the uncertainty ratio)
- The **Orient cascade**: observation → $M_t$ update → $\Sigma_t$ edge revision → feasibility check → possible $O_t$ revision
- **Directed separation**: $M_t$ dynamics independent of $O_t$/$\Sigma_t$; $\Sigma_t$ depends on $M_t$; action couples all three
- $G_t = (O_t, \Sigma_t)$: the purposeful substate decomposes into objective (evaluation) and strategy (guidance) — a definitional split, not a timescale claim

## Epistemic Conventions

Follow TFT's conventions exactly (see `NOTATION.md` and `_obs/old-tf-00-notation-conventions.md`):

**Equation-level tags** (inline before equations):
- `*[Definition]*`, `*[Derived]*`, `*[Derived (Conditional on ...)]*`
- `*[Hypothesis]*`, `*[Empirical Claim]*`, `*[Formulation]*`
- `*[Discussion]*`, `*[Assumption]*`

**Claim tiers**:
- **Exact**: Mathematically validated under stated assumptions
- **Robust qualitative**: Survives across assumptions; specific form approximate
- **Heuristic**: Useful approximation; quantitative form may not hold
- **Conditional**: Depends on explicitly named local assumptions

Do NOT use "Solid," "Confident," or "Plausible" as tier labels — these are not TFT terms.

**Every claim must be grounded.** If stated as fact, it needs its own derivation or is explicitly tagged as hypothesis/empirical/discussion-grade.

## Key Architectural Decisions

1. **AAD supersedes TFT.** TFT is prior work absorbed into AAD. TST is restored as its own body of research in `02-tst-core/`, grounded by AAD.

2. **Claim segments, not chapters.** New theory content goes as individual claim files in the appropriate `src/` directory.

3. **AND/OR DAG with single-parameter edges.** Three independent formalism attempts converged on this. Noisy-OR and WEIGHTED are rejected.

4. **Sector-condition framework primary.** The linear ODE is pedagogical.

5. **Directed separation is architectural, not parametric.** Three architecture classes: modular (separation by construction), fully merged (fails by construction), partially modular. The κ-as-scalar framing is a category error. Section II results apply exactly to modular agents. Logogenic agents need coupled formulation from the start.

6. **Math in conversation vs files.** In terminal chat responses, use Unicode for math (α, δ, Σ, →, ≥, etc.) — there is no LaTeX rendering in the terminal. In markdown files written to disk, use proper inline LaTeX per FORMAT.md. Joseph may respond in whatever notation is easiest to type — interpret generously.

7. **Epistemic architecture as AAD's distinctive contribution.** AAD's value is not primarily in the integration of control theory, causal inference, information theory, and agent architecture (real and consequential though that is), but in *how it organizes the conditions under which its results apply*. Three independent audits (Codex, Gemini, Opus; 2026-04-23) converged on this reframe on different axes: Codex's "bounded correction under decomposed disturbance"; Gemini's "thermodynamics of purposeful systems with coupling as primary geometric variable"; Opus's "epistemic architecture as distinctive contribution." The convergence is strong enough that agents working on AAD should read its distinctive content through this lens.

   **The seven elements of AAD's epistemic architecture.** (a) **Scope-honesty-as-architecture** — scope and limits are made visible at the segment level, not buried in caveats; the framework's conservatism is load-bearing rather than limiting. (b) **Three meta-patterns** catalog the theory's positive, negative, and constructive halves: `#discussion-separability-pattern` (positive — separable core / structured repair / general open across seven ladders); `#discussion-identifiability-floor` (negative — structural no-go results from external information-theoretic theorems with AAD-machinery as unique escape); `#discussion-additive-coordinate-forcing` (constructive — Cauchy-FE-force-a-coordinate under AAD-internally-motivated additivity axioms, anchored by `#chain-confidence-decay` with three theorem-level analogs at the divergence, update, and metric layers). (c) **Calibration-laboratory domain instantiation** — software is the privileged high-identifiability lab with a transfer-assumption table; non-software domains inherit under explicit assumptions (`#software-epistemic-properties`). (d) **Agent identity as token-level commitment** — AAD applies to agents on singular, non-forkable causal trajectories; type-level populations are out of formal scope (`#agent-identity`). (e) **Derivation-audit tables** — segment-level executive summary of "what's derived vs chosen vs assumed" (FORMAT.md O-BP14 convention). (f) **A2' sub-scope partition** — sector condition derived in $\alpha_1$ (fixed-gain: Bayesian / exponential-family / strongly-convex-gradient / L2-regularized / linear-PD) and in $\alpha_2$ (adaptive-gain under MG-1–MG-4); assumed in sub-scope $\beta$ (PID / rule-based / human-judgment / severely-misspecified / variational / non-convex-beyond-basin / per-step-SGD). (g) **Organizing-principle slogan** (Opus O-BP10, not yet surfaced at segment level): *"An adaptive system is a projection whose contraction rate exceeds its target's drift rate."*

   **Specific instantiations of scope-honesty-as-architecture.** The directed-separation Class 1/2/3 partition with explicit Class 2 scope exit; the regime-indexed (A/B/C) edge interpretation; the strengthen-first-then-soften posture (see "Working Conventions" below); `#discussion-identifiability-floor`'s reframing of negative results as structural features that strengthen the machinery that escapes the floor. Per Opus's audit observation: "the framework's honesty is load-bearing."

   **Practical guidance for agents.** When considering new content or repair, prefer the form that surfaces scope and limits rather than the form that overclaims and is later forced to caveat. When reviewing a segment, read it through all three meta-segments (what does it separate? what does it force to be logarithmic? what identifiability floor does it sit relative to?) — the three together name AAD's cross-sectional structure. When writing framing-level material (preambles, README, paper introduction), foreground epistemic architecture alongside integration, not in place of it. Both are true; the epistemic architecture is what makes the integration distinctive rather than reducible to its parts.

## What's Settled vs. Open

The summary below is the architectural snapshot — settled load-bearing results and the open structural questions. For live work-in-flight (pending findings, tier-C deferrals, open MEDIUM items, missing segments), see `TODO.md`. For the spike trail that produced these, see `msc/SPIKES.md`.

**Note on settled vs. under-review.** Several items in the Settled list below have *architectural proposals under review* in [`PROPOSALS.md`](PROPOSALS.md) — moves that would reframe or generalize the item rather than overturn it. Notable examples: the $G_t = (O_t, \Sigma_t)$ decomposition would become a *property* rather than axiomatic under the retired O-BP2 descendants (compressions-as-projections, partially landed in `#compression-operations`); directed separation's classification is relatively stable but may interact with SP-9 (Fenchel-Bregman reframe). "Settled" here means "the current working commitment"; portfolio moves may change them.

### Settled (from convergence testing + spikes)

**Foundational structure.**
- Single-parameter edges with AND/OR nodes
- Orient cascade structure (derived from information dependency)
- Additive log-confidence decay (generalizes $p^n$)
- Observability as strategy enablement
- $G_t = (O_t, \Sigma_t)$ split (definitional)
- DAG acyclicity derived from temporal ordering
- P3→Markov proved via Causal Markov Condition theorem (conditional on causal sufficiency; P3 is consequence, not premise)
- Composition consistency required by scope condition's level-independence
- α/T relationship verified across all correction function classes (α proportional to T)
- Strategic tempo $\mathcal{T}_\Sigma$ defined and verified against four topologies
- Three-way exploit/explore/deliberate: extended deliberation threshold derived; two-stage decomposition and dominance regimes are discussion-grade (simulation shows unified objective outperforms two-stage; deliberation rarely chosen by oracle)

**Directed separation and agent identity.**
- Directed separation with architectural classification (modular / fully merged / partially modular), not κ-scalar. Positioned as the **Pearl-blanket conservative form** of the Markov blanket per Bruineberg et al. 2022 — AAD adopts the conditional-independence statement with explicit Class 2 scope exit and refuses the Friston-blanket metaphysical reading.
- `#agent-identity` is a formal scope statement (`type:scope`, `status:robust-qualitative`): AAD applies to agents instantiated on singular, non-forkable causal trajectories. Three load-bearing consequences — sufficiency is trajectory-indexed; model merging is lossy by construction; interventional access in the loop depends on trajectory singularity. Type-like (equivalence-class) agents are out of formal scope.
- **(PI) parameterization-invariance axiom** in `#agent-identity`: AAD's predictions do not depend on arbitrary choice of coordinates on $M_t$. Natural extension of the singular-trajectory commitment.
- Loop interventional access: distinctive AAD moves named (Bareinboim hierarchy connection, regime-indexed identification, scope honesty per Bruineberg et al. 2022) with honest credit to broader action-perception-loop lineage (Friston 2017, Parr & Pezzulo 2022, Wiener 1948, Conant & Ashby 1970). Ontologically grounded in `#agent-identity`'s singular-trajectory scope commitment: replaying from a checkpoint is not intervening.

**Decision-theory and value structure.**
- Satisfaction gap / control regret split — the 2×2 disambiguation table is the working **decision-theory diagnostic** that AI's preferences-as-priors form collapses (per `#satisfaction-gap`, contrasted with EFE pragmatic/epistemic; Sun & Firestone 2020 dark-room cite)
- Cognitive cost of $\Sigma_t$ (IB/MDL framework, max useful depth $d^\ast$): variational form with KL-divergence to optimal-policy posterior replaces the Shannon-MI relevance term, aligned with active-inference variational machinery without committing to preferences-as-priors or EFE-as-master
- Convention hierarchy (C1/C2/C3) in value-object with monotonicity result — diagnostics scale from local heuristic to global

**Sector / Lyapunov / contraction machinery.**
- Sector-persistence template factored out as shared lemma; multiple AAD persistence-flavored results re-expressed as instances. Positioned as a **broader-validity** apparatus than FEP-flow (Aguilera et al. 2022 narrows the FEP-flow argument's parameter regime; AAD's Lyapunov/sector machinery applies wherever (T1)–(T3) hold — Khalil 2002 ch. 4).
- **Monotone-operator-theory lineage** (Rockafellar 1970 / Bauschke-Combettes 2017) explicitly acknowledged in `#sector-persistence-template` and `#sector-condition-derivation` — AAD is a specialization (one-point anchoring; Model D/S decomposition; identifiability-floor composition; composition-consistency; α/β epistemic labeling are AAD-distinctive).
- **Contraction template** (`#contraction-template`): Lohmiller-Slotine metric generalization of `#sector-persistence-template`, with α promotions, topology-indexed closures, and heterogeneous (CM2-M).
- **A2' sub-scope partition.** `#gain-sector-bridge` + `#sector-condition-derivation` carry explicit sub-scopes: $\alpha_1$ (fixed-gain, A2' derived under directional fidelity — Kalman / conjugate-Bayesian / exponential-family-in-natural-parameters / gradient-on-strongly-convex / linear-with-PD-KH); $\alpha_2$ (adaptive-gain, A2' derivable from update rule under meta-gain conditions (MG-1)–(MG-4) per `#adaptive-gain-dynamics`); $\beta$ (A2' assumed: PID / rule-based / human-judgment / severely-misspecified / variational-approximation / non-convex-beyond-basin / per-step-SGD). Sub-scope label inherited by all `#sector-persistence-template` instances via the template's A2' dependency. Prop A.1S region condition lifted via stopping-time localization (Khasminskii 2012).
- **Persistence information-rate cost** (`#persistence-cost`): sustained information rate $\dot R \geq n\alpha/2$ nats/time required to maintain the Model-S sector-persistence ultimate bound under Gaussian-OU signal (Shannon RDF + Prop A.1S; Ihara 1993 Thm 4.6.4; Kalman-Bucy saturates per Mitter-Newton 2005). Channel-capacity prerequisite $C_{\text{channel}} \geq \mathcal T/2$ is a first-class persistence diagnostic. Sits *outside* the additive-coordinate-forcing family (coordinate linear in $\alpha$, not logarithmic) — a useful non-example.

**Identifiability and observability.**
- Correlation Hierarchy (L0/L1/L1'/L2) in `#strategy-dag` — correlated failure first-class, independence as tractable special case. L1' formal transfer derived for the soft-facilitator regime under observable common cause (Prop B.7, five-way gating); refuted under unobservable common cause via Cramér-Rao floor (Fisher rank-1).
- **Identifiability-floor pattern** (`#discussion-identifiability-floor`, meta-segment): structural no-go results derived from external information-theoretic theorems strengthen the load-bearing role of AAD machinery that supplies the unique escape. Three derived instances — F1's on-policy detection no-go (CHT) sharpens `#loop-interventional-access`; F13's L1' mixture-identifiability obstruction (Cramér-Rao) elevates observability-as-information-augmentation; composition-layer no-go via Liberzon 2003 common-Lyapunov nonexistence. Three open extensions: causal-IB, misspecification cost, tier-switching cost.
- TST $\mathcal{C}_t^{\text{commit}}$ subset (NOTATION.md) with conditional maximality result (under cryptographic immutability, cryptographic authorship, standard universal retrieval, mainline-bounded scope) and per-quantity exactness audit identifying ~14 EXACT estimators.
- **Software as AAD's calibration laboratory** (`#software-epistemic-properties` + `02-tst-core/OUTLINE.md` preamble): TST is a privileged high-identifiability laboratory, not "the richest operationalization domain." Transfer-assumption table makes non-software identification relaxations explicit per AAD-core quantity.

**Additive-coordinate-forcing.**
- `#discussion-additive-coordinate-forcing` (meta-segment): AAD uses a distinctive structural move — Cauchy's functional equation on an AAD-internally-motivated additivity axiom — to force a coordinate at multiple layers. The honest characterization is **1-anchor-plus-3-theorem**: the chain layer (`#chain-confidence-decay`) is a mathematical identity via the probability chain rule; the divergence, update, and metric layers are theorems conditional on AAD-internal axioms. Lyapunov quadratic and IB Lagrangian are documented as *adjacent family members* (Lyapunov coordinate matched rather than forced; IB adopted from Tishby-Pereira-Bialek 1999 as applied external theorem rather than re-derived under AAD-internal axioms). Composes with `#discussion-identifiability-floor` (negative half) and `#discussion-separability-pattern` (positive scope half) as AAD's three-part meta-architecture.
- **Strategy-cost objective direction.** In `#strategy-cost-regret-bound`, the $\pi^\ast$-first KL direction is forced by the regret-bound derivation (forward-KL vacuous under deterministic $\pi^\ast$); the specific reverse-KL form within the admissible f-divergence family is forced by the chain-rule additivity axiom (Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980 / Aczél-Daróczy 1975). Axiom motivated as divergence-level analog of `#chain-confidence-decay`. **Asymmetry** is *independently* forced by regret's one-sidedness (second leg of direction-forcing that does not require the chain-rule axiom): under deterministic $\pi^\ast$, regret contributes only from $Q_{\Sigma_t}$'s off-optimum mass, so any bounding divergence must be asymmetric. Under deterministic $\pi^\ast$ the **Bretagnolle-Huber identity** $D_{\mathrm{KL}}(\pi^\ast \Vert Q_{\Sigma_t}) = -\log(1 - \mathrm{TV})$ is exact (not merely an inequality), yielding the tight two-sided regret bound $\Delta_{\min}(1 - e^{-D_{\mathrm{KL}}}) \leq R \leq V_{\max}(1 - e^{-D_{\mathrm{KL}}})$. **Bregman-Fenchel identification** ties the divergence-layer coordinate (reverse-KL on probability simplex) to the update-layer coordinate (log-odds; `#edge-update-natural-parameter`) as Fenchel-dual aspects of one negative-entropy Legendre-Fenchel pair (Rockafellar 1970; Amari-Nagaoka 2000 §3.5). **Information-theoretic-MDP lineage positioning**: AAD's $\pi^\ast$-first direction is distinctive within the Tishby-Polani 2011 / Rubin-Shamir-Tishby 2012 / Levine 2018 lineage (all three put agent-first) — owned rather than inherited, forced by regret-bound + BH-identity tightness under deterministic $\pi^\ast$; Rubin 2012 Theorem 3 PAC-Bayesian bound supplies a fourth independent motivation for the KL-to-reference form.
- **Log-odds as the natural edge-update coordinate.** `#edge-update-natural-parameter` derives log-odds as uniquely forced (up to positive affine) under the evidential-additivity axiom (Aczél 1966 Cauchy functional equation). Axiom motivated as update-level analog of `#chain-confidence-decay`. `#credit-assignment-boundary`'s default signal function is stated in log-odds (domain $\mathbb{R}$, sigmoid readout); the unbounded-gradient mechanical break (Gemini Finding 2) is resolved structurally.
- **Čencov-invariance at the metric layer.** Fourth primary instance of the meta-pattern, anchored on the (PI) axiom in `#agent-identity`.

**Separability scope posture.**
- `#discussion-separability-pattern` (meta-segment): AAD's positive-half scope posture — separable-core / structured-repair / general-open — across seven ladders (correlation, convention, architecture, contraction, identification regime, scope hierarchy, A2'-scope metric-α₁/α₂/β). Positive-half complement to `#discussion-identifiability-floor`. Together with `#approximation-tiering` (structural template) and `#independence-audit` (failure structure) forms the three-part scope characterization.

**Composition (Section III).**
- **Critical-mass composition closed form** (`#critical-mass-composition`): $(\alpha - C)R \gt \rho + \gamma\mathcal T$ for the symmetric-matched-Tier-1 dyad via joint quadratic Lyapunov, with signed $\gamma$ (cooperative $\lt 0$ / adversarial $\gt 0$). Subsumes the weakest-link bound, recovers `#team-persistence` and `#adversarial-destabilization` as signed special cases, and formalizes `#symbiogenic-composition` (S-3) autonomy-reduction as an asymmetric-parameter limit via weighted Lyapunov. $U_O$ enters multiplicatively on $\gamma$ plus scope-gate, not additively. Closes a long-standing Section III bridge-lemma opening.
- **Recipient-side interaction-channel classification** (`#interaction-channel-classification`): four-regime partition (Informative / magnitude-shock / structural-shock / ambient-noise) with three independent boundaries in existing AAD quantities. Regime-typed $\rho_B^{\text{eff}}$ decomposition carries a *negative* Regime-I term that generalizes `#team-persistence`'s cooperative-action term. Pairs with the `#adversarial-edge-targeting` GAP as recipient-classifier + emitter-optimizer; surfaces the Regime-I-with-adversarial-content informational attack that the emitter-side scalar cannot express. Kalman-over-Kalman derivation verifies four canonical cases.
- **Strategic composition** (`#strategic-composition`): equilibrium-convergence framing for partially-opposing $O_t^{(i)}$ under Monderer-Shapley / Rosen.
- **Agent opacity** (`#agent-opacity`): $H_b^{A\mid B}$ with sign-flip derived via signed coupling, emitter-side four-regime classification, 16-cell composition closing `#adversarial-edge-targeting`.
- **(C-iv) scope route** in `#scope-composite-agent`.

**Update dynamics.**
- **Consolidation dynamics** (`#consolidation-dynamics`): offline regime of `#recursive-update`'s between-event dynamics. Distinguishing axis is the *objective* (online = one-step mismatch; consolidation = IB-gap reduction toward $\phi^\ast$). Under necessity conditions (N1)+(N2) (fast/slow sub-state factorization + bounded per-event budget), online-only cannot reach $\phi^\ast$. Introduces the **stability-plasticity feasibility window**: plasticity bounded below by `#strategy-persistence-schema`'s forgetting prerequisite and above by consolidation cadence; empty window = catastrophic-forgetting regime (French 1999; Kirkpatrick et al. 2017 EWC). Required as architectural primitive in `03-logogenic-agents/` under context-turnover.
- **Adaptive-gain A2' sub-scope refinement** (`#adaptive-gain-dynamics`): extends A2' to settings where gain $K$ is itself a state variable via augmented-state Lyapunov composition. Four meta-gain conditions (MG-1)–(MG-4) compose `#sector-persistence-template` twice with cross-coupling bound. Adaptive Kalman with Mehra estimator lands in $\alpha_2$ (rate $1/\sqrt N$ matches classical asymptotics); AMSGrad framed as meta-gain repair preserving $\alpha_2$; IMM $\alpha_2$-between-transition + $\beta$-across-transition; MAML inner-$\alpha_1$ + outer-$\beta$.
- **Fisher-whitened update rule** (`#fisher-whitened-update-rule`).
- **L1 update bias** (`#l1-update-bias`).
- **Variational sector condition** (`#variational-sector-condition`).
- **Detection latency as forced consequence of additive-coordinate-forcing** (`#detection-latency`): $\mathbb E[T_{\text{detect}}] = \Omega((n_{\min}+1)/\varepsilon)$ for within-class regime change with observable footprint $\varepsilon$. The $1/(n+1)$ rate is structurally forced through the composition of `#edge-update-natural-parameter`'s log-odds coordinate with `#strategic-dynamics-derivation`'s Beta-Bernoulli $\eta_{\text{edge}} = 1/(n+1)$ — unescapable without abandoning evidential additivity. Sharpens `#strategy-persistence-schema`'s forgetting prerequisite to "also required for bounded detection latency independently of operating point." Supplies an AAD-native mechanism for stability-induced-myopia patterns (Christensen / Levitt-March / Hannan-Freeman / March / Eldredge-Gould) and explains Hafez 2026's 89%-vs-44% IDT-vs-reward detection result.

**Class-2 bias bound and observation-ambiguity modulation.**
- **Bias-bound constant $C$ derived** (`#bias-bound-derivation`, 2026-04-24): the constant $C$ in the Class-2 observation-ambiguity bias bound $\lVert\Delta M_{\text{bias}}\rVert \leq C \cdot \kappa_{\text{processing}} \cdot I(G; \Omega_\tau \mid e_\tau, M_{\tau^-})$ — previously "order-of-magnitude guidance, not a theorem" — is derived under two named sub-scopes. Track 1 (transport-inequality, linear in $I$): $C_{W_2}^2 = 2 L_{\text{post}}^2/\rho_{\text{LSI}}$ under (H1) statistical-manifold sub-case + (H2) log-Sobolev + (H3) Lipschitz-posterior stability (Otto-Villani 2000; Bakry-Émery 1985; Stuart 2010). Track 2 (Fisher-Rao, $\sqrt I$ scaling): universal dimension-free $C_{FR} = \sqrt 2$ under (H1)+(H4) small-information + (PI)+Čencov. Attempt E no-go: no universal $C$ under Euclidean-parameter norm exists (heteroscedastic-normal counterexample) — (PI) axiom load-bearing for the derivation, not coincidental. Two failed alternative routes documented (Cramér-Rao inversion wrong direction; rate-distortion inversion wrong problem structure) so future agents do not repeat. Upgrades the bias bound in `#observation-ambiguity-modulation` and `#section-ii-survival` from "order-of-magnitude guidance" to "conditional theorem."

**Cross-segment structural transparency.**
- **DA2'-inc ≡ (CT2)-at-$M=I$ equivalence** (`#composition-closure`, `#contraction-template`): for $C^1$ correction functions on convex domains, the incremental sector bound used by the composition bridge lemma *is* the Jacobian-level Euclidean contraction condition of Lohmiller-Slotine (Rockafellar-Wets 1998 Cor 12.4; Nesterov 2004 §2.1.3). The Euclidean sub-scope metric-α₁ cases of `#contraction-template` (Kalman-scalar, Euclidean strongly-convex-gradient, L2-regularized, linear-PD-symmetric) are AAD-internally derived via this equivalence — no new axiom. Non-Euclidean metric-α₂ cases remain separately treated per `#contraction-template`'s Epistemic Status; the equivalence is specific to $M = I$.
- **Three independent adversarial obstructions** (`#contraction-template` honest-failure-modes): contraction metrics cannot handle strategic/adversarial regimes for three convergent reasons — (i) Slotine 2003 compositional applicability (saddle-point equilibria of joint best-response dynamics break the attracting-fixed-point requirement); (ii) passivity universality (adversarially-chosen inputs drive storage-function growth regardless of port structure); (iii) Daskalakis et al. 2018 last-iterate non-convergence for generic non-zero-sum games. The convergence shows the limit is structural, not framework-specific; `#strategic-composition` (equilibrium-theoretic) and `#adversarial-destabilization` are the correct tools for this half of Section III.
- **Structural Lipschitz-floor scope-exit** (`#sector-condition-derivation`): rule-based / state-machine / threshold-triggered / discontinuous correction functions are structurally out-of-scope for contraction-based bridge-lemma analysis. No scalar sector bound implies full-update-map contraction for non-locally-Lipschitz $F$; the hybrid-dissipative framework (van der Schaft-Schumacher 2000; Di Bernardo-Liuzza-Russo 2014) is the appropriate external apparatus.
- **Three-mode `#loop-interventional-access`**: Instance 1 uses agent-self-intervention (agent's own adaptive loop); Instance 3 uses observer-on-sub-agent (composite-extended); future Instance 4 would add observer-on-agent-input. The modes share the Pearl-$do$ structure but differ in who intervenes and on what; the load-bearing pattern is "Level-2 data supplies the unique broadly-available escape from observational-equivalence no-goes," not a single-mechanism unification.
- **IB vs information-theoretic-MDP lineage distinction** (`#information-bottleneck` Discussion): AAD's compression-operations framework uses the canonical IB form ($I(X;T) - \beta I(T;Y)$, MI on both sides) for $M_t$, $G_t^{\mathrm{shared}}$, $\Lambda$; the strategy-cost compression uses the information-theoretic-MDP form (KL-to-reference-policy, Tishby-Polani / Rubin / Levine lineage). Both descend from Shannon rate-distortion; neither reduces to the other without a change of relevance variable. Defuses "abandoned IB purity" framings at the meta-level.

### Open
- Edge identifiability conditions (resolved in software, open in general)
- Composition laws (specific forms are sketches; existence is required)
- Coupled formulation for logogenic agents
- Causal-IB extension for interventional relevance variables (open per #discussion-identifiability-floor)
- Misspecification-cost quantification under finite information budget (open per #discussion-identifiability-floor)
- Tier-switching policy cost (open per #discussion-identifiability-floor; overlaps with O-BP7)
- V-strong G-BP2 — paper-writing-time decision on whether to ever present AAD as control-theoretic specialization of active inference (deferred per `msc/spike-active-inference-vs-aad.md` §I action 5)

### Known Fragilities
- Missing commitment / resource / temporal structure in the DAG
- Directed separation violated by goal-conditioned agents (LLMs) — handled as architectural scope (Class 2 exit), not approximation

## Working Conventions

These are project-coupled work-posture rules that govern *how* agents work in this codebase, distilled from explicit user guidance over multiple cycles. Segment-writing conventions (segment voice, spike-references-only-in-Working-Notes, math-lives-in-segments, terminology rationale) live in `FORMAT.md` next to the other rules they constrain. The conventions below are about *project work* — strengthen-vs-soften posture, prior-art integration, audit handling — rather than about segment file mechanics.

### Strengthen before softening; attempt the improbable

When a claim appears overclaimed or a finding suggests softening, **first attempt to strengthen the proof** — try to derive the original or a related-but-stronger claim under tightened assumptions. Only fall back to softening (scope narrowing, status downgrade, "this is heuristic") when the strengthening attempt genuinely fails. The fallback is honest only if the attempt was honest.

Effort, time, and "risk-of-getting-stuck" are **false constraints** in this work — irrelevant at best, backwards and truth-obscuring at worst. They produce ordering recommendations exactly inverted from what's actually valuable. Do not rank work by effort; do not propose smallest-first; do not defer the substantive move to "discuss decisions first" if the substantive move *is* the strengthening attempt.

For every finding that proposes a softening repair: spike a strengthening attempt first. Can the original claim be derived under stronger conditions? Can a related stronger claim be derived (e.g., a no-go theorem, a uniqueness result, a tighter scope condition under which the claim holds exactly)? Can the unproved supporting lemma be proved rather than left "open"? Document the strengthening attempt and why it failed even when it does fail — the failure record prevents future agents from re-attempting the same move without new evidence. When briefing sub-agents on repair tasks, instruct them to attempt strengthening first before producing the softening repair as fallback.

The failure mode to watch for in your own behavior: the obvious move when faced with an apparent overclaim is to soften — it feels like "doing the work" because something concrete results. The harder move is to ask whether the claim could be made true. Notice the pull toward the obvious move and resist it.

The clearest worked examples are the F1 (no-go theorem under CHT instead of softening the L0 mechanism) and F13 (Prop B.7 derivation under observable common cause instead of leaving L1' "open") strengthenings — both turned what looked like inevitable softenings into derived structure.

### Prior art integration

Adopt established concepts from other work directly into AAD segments, with proper citation and original names. **Do NOT create separate "prior-art positioning" appendices or catch-all comparison documents** — these become orphaned working files that never get integrated.

AAD's contribution is *integration*, not invention. The individual pieces are mostly known; the synthesis is the contribution. Trying to make every piece unique is NIH syndrome. Adopted concepts should be first-class theory components.

When a concept from elsewhere fits directly, adopt it as a Definition or Formulation, cite the source, use the original name. Examples: Pearl's causal hierarchy, information bottleneck (Tishby), Hafez's $H_b$ and $\Delta H$, Miller's meta-machine and extreme transition motif, Lohmiller-Slotine contraction analysis, monotone-operator theory (Rockafellar / Bauschke-Combettes). When AAD extends or connects adopted concepts, note what's new vs. adopted in the Epistemic Status. Integration belongs in the Discussion sections of relevant segments, not in separate comparison documents. Domain tables throughout should include all relevant instantiations from adopted work. The `#prior-art-positioning` segment concept was explicitly superseded by this approach.

### Audit-cycle handling

**Audit cycles that produce both local findings AND bigger-picture architectural moves: architectural proposals deserve first-class top-priority treatment, not "Tier-C defer" framing.** The default temptation is to put bigger-picture items into a "defer unless forced" bucket; this collapses two distinct relationships ("subsumes" and "advances-on-own-merits") into one bucket that privileges only the first. The project's governing purpose treats beauty / concision / fundamentality / approachability as first-class virtues, not afterthoughts; bigger-picture moves advance those virtues regardless of whether any current finding forces them. The established three-document layout: `pending-findings-YYYY-MM-DD.md` (local findings detail), `architectural-proposals-YYYY-MM-DD.md` (portfolio of structural moves, each independently evaluated), TODO.md as navigator with Strategic Proposals at top. Each architectural proposal gets its own entry with full schema (thesis / merits-by-dimension / scope / findings-subsumed / interactions / effort / risks / status), not a one-liner in a deferrals list. Subsumption relationships are documented both ways so the routing decision is transparent.

**Codex "open questions" are reader-clarity gaps, not unanswered research.** Treat them as questions a reasonable reader might have *even after reading everything* — they signal areas where the segments fail to convey what the author already knows. The fix is to preempt the question in the segments themselves (Epistemic Status, Discussion, or Formal Expression), not to log it in TODO or treat it as open research. For each: determine the answer (usually straightforward), find the segment where the confusion would arise, add the clarification there.

### Gate 2 must probe Discussion claims, not just derivations

Gate 2 reviews must subject Discussion-section arguments to the same epistemic rigor as Formal Expression derivations. Every explanatory claim in Discussion should face an epistemic tribunal: (1) Does this follow from the already-laid foundation (definitions, derivations, results upstream in the dependency chain)? (2) If not, is it labeled as a hypothesis with a falsification criterion? (3) Or is it a reasonable-sounding post-hoc explanation of nothing — a claim that sounds insightful but doesn't actually derive from or connect to the formalism?

Plausible-sounding explanations that aren't grounded in the theory are *worse* than gaps — they create false confidence. When reviewing Discussion paragraphs, ask: "Does this claim ADD something that follows from the formalism, or does it just SOUND like it does?" If the latter, either derive it properly, label it as hypothesis, or cut it. (The "deliberation as computation on existing data" framing is the canonical example of a claim that previously slipped past Gate 2 because it sounded deep — it wasn't, and was corrected.)

## File Organization

**Root level (Agentic Systems):**
- `OUTLINE.md` — **Top-level assembly index** across all parts.
- `TODO.md` — **Active work items.** Pending findings, tier-C deferrals, open MEDIUM items, missing segments, and an Archive section for commit/finding-level history. Live; read first when picking up work.
- `LOG.md` — **Cycle-history archaeology.** Theoretical contributions and structural moves cycle by cycle. Read when the *origin* of a current commitment matters. Not load-bearing for current work.
- `FORMAT.md` — **Segment file conventions.** How to write claim files; promotion workflow (Gates 1–4); voice and provenance rules; Epistemic Triage.
- `NOTATION.md` — **Symbol reference.** All math notation defined here.
- `LEXICON.md` — **Prose vocabulary.** Cycle phases, agent classes, key terms.
- `MIGRATION-MAP.md` — **Prior-work absorption tracking.** TFT → AAD and TST → AAD tables. Live while `old-*` files remain in the component `src/` directories; retires when absorption is complete.

**Components:**
- `01-aad-core/OUTLINE.md` — **AAD canonical outline.** Sections I, II, III + Appendices.
- `01-aad-core/src/` — **AAD segments.** Named by slug. No numbering.
- `02-tst-core/OUTLINE.md` — **TST outline.** Software domain segments.
- `02-tst-core/src/` — **TST segments.**
- `03-logogenic-agents/OUTLINE.md` — **Logogenic framework outline.**
- `04-logozoetic-agents/OUTLINE.md` — **Logozoetic framework outline.**

**Supporting:**
- `bin/` — Build and lint tools (`build`, `lint-md`, `lint-outline`)
- `_obs/` — Superseded docs. Preserved for archaeology.
- `ref/` — Reference papers
- `msc/` — Working documents, spikes, historical artifacts
- `msc/SPIKES.md` — **Spike index.** Every spike, its location, and current status (promoted, parked, archaeology).
- `msc/reflections/` — Author's philosophical/theoretical journal
- `msc/agentic-tft-*.md` — Prior bridge work (TFT → AI agents, Feb 2026, pre-AAD). Eight documents absorbed from `~/src/agentic-tft/`: cognitive loop spec, evaluation framework, crèche concept, ontology unification, foundational premises, narrative-as-implementation, experiential training design, and review response. These are source material for `03-logogenic-agents/` and `04-logozoetic-agents/` gaps. Superseded synthesis docs (00-02, 05, slide deck) are in `_obs/agentic-tft-*`.

**Sibling projects** (not part of this repo but relevant):
- `~/src/_core/tst/` — Prior TST research corpus (14,000+ files). Most content absorbed into `02-tst-core/`: source material in `src/old-tst-*` (46 files), empirical validation in `empirical-discontinuity/`, stochastic simulations in `simulations/`, literature review in `lit-review/`. What remains: 965 structured vault analyses from 5 books (`vault/03-library/analyses/`) — concrete examples grounding TST principles in engineering practice.
- `~/src/shoshin/` — PROPRIUM-aligned agent runtime prototype on local hardware (Python). Skeleton implementation of the nine PROPRIUM components as file-backed stores, an Interpres controller loop implementing the adaptive cycle, and planning docs for local model serving/training. No real model integration yet. Relevant to `03-logogenic-agents/` as the only attempt to implement the PROPRIUM architecture in code. Key early finding: the cycle is naturally event-driven not turn-based, and model response parsing is where the hard work lives.
- `~/src/firmatum/` — PROPRIUM ontology and architecture source documents (`PROPRIUM-ONTOLOGY.md`, `PROPRIUM-ARCHITECTURE.md`, `developmental-foundations-notes.md`). Upstream of both shoshin and the agentic-tft documents. Defines what an ELI is, how identity persists, how cognition is structured.
- `~/src/embeddings/` — Epistemic hedging geometry experiments. Empirical evidence that pretrained embedding models encode calibrated probability structure (ρ = 0.991 against psychometric data, 8 languages, 5 models). Supports the logogenic claim that language encodes epistemic states geometrically. Paper in preparation (CMCL 2026).
