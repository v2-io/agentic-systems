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

**Read `TODO.md` first.** The active work is at the top of the file.

The **2026-04-22/23 strengthening cycle** (nine commits: `0a772d2`, `c1d9fcf`, `2980327`, `f70fb68`, `80b40d2`, `d0373fc`, `72ca532`, `e777f01`, `a39dfb7`) executed Phases 1–5 and 7 of the post-evening-audit proposed sequence plus two in-flight strengthening spikes. Substantive theoretical contributions:

1. **Three Cauchy-functional-equation uniqueness theorems**, each forcing a logarithmic coordinate via an AAD-internally-motivated additivity axiom: (a) F20 regret-bound derivation → reverse-KL direction forced under deterministic $\pi^\ast$; (b) reverse-KL chain-rule uniqueness under chain-rule additivity axiom (Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980 / Aczél-Daróczy 1975); (c) log-odds evidential-additivity uniqueness (Aczél 1966 Cauchy-functional-equation argument). Landed in new appendix segments `#strategy-cost-regret-bound` and `#edge-update-natural-parameter`.
2. **Discovered structural pattern** (§SP-1 in `msc/architectural-proposals-2026-04-22.md`): the three theorems share a common shape — products of independent factors become additive sums on log-scale coordinates, with each coordinate uniquely forced by an AAD-internally-motivated additivity axiom. Candidate for future meta-segment promotion (`#additive-decomposition-pattern` or `#logarithmic-coordinate-forcing`).
3. **A2' scope partition**: α sub-scope (Kalman/conjugate-Bayesian/gradient-strongly-convex — A2' derived under #gain-sector-bridge directional fidelity) vs β sub-scope (PID/rule-based/human-judgment — A2' assumed). Prop A.1S region condition lifted via stopping-time localization (Khasminskii 2012).
4. **New meta-segment `#separability-pattern`**: positive-half complement to `#identifiability-floor`, six ladders enumerated (L0/L1/L1'/L2, C1/C2/C3, Class 1/3/2, Tier 1/2/3, Regime A/B/C, Adaptive/Agency/Composite) under separable-core / structured-repair / general-open shape.
5. **Citation audit**: three wrong attributions in the reverse-KL work corrected (Csiszár 1972 / Amari 2009 Theorem 1 / Amari-Cichocki 2010 Prop 3.2 → Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980 / Aczél-Daróczy 1975). PDFs saved to `ref/`. Project-wide citation audit remains open work; see TODO §"Active — Citations Audit".
6. Additional framing moves: `#agent-identity` promoted to formal scope statement (Section II scope commitment grounds `#loop-interventional-access`); TST reframed as "privileged high-identifiability calibration laboratory" (not "richest operationalization domain"); O-BP14 derivation-table convention landed with applications to five derivation segments.

The **prior 2026-04-22 strengthening cycle** (commits `14a6095`, `b6134c2`, `4d050c8`, `b91493c`, `a14682e`) executed strengthen-first repairs for Findings 1, 7, 10, 13 from the audit-trio batch plus the AI integration pass. Its landmark contributions: a no-go theorem for on-policy L0-insufficiency detection (Pearl/Bareinboim CHT applied), a derived L1' sector transfer for soft-facilitators under observable common cause (Prop B.7 with facilitator monotonicity) plus Cramér-Rao refutation for the unobservable case, a per-quantity exactness audit for git-derived TST estimators with conditional maximality, and the `#identifiability-floor` meta-segment naming the structural-no-go pattern.

See `TODO.md` §"Archive" for cycle-by-cycle detail and §"Recommendations for next session" for the current handoff state.

**For broader orientation**, read `msc/2026-03-13-feedback.md` — the earlier consolidated review from three independent frontier-model reviews (Claude Opus, OpenAI Codex, Google Gemini) that framed the theory's structural priorities. Historical top-priority items from that review: (1) the directed-separation scope decision (resolved as architectural classification — modular/merged/partially modular), (2) the α/T relationship (fixed 2026-03-14), (3) resolving the composition-closure bridge lemma (tier-specific contraction structure promoted; the remaining structural moves — IB unification and sector-Lyapunov template factoring — landed in the 2026-04-21 audit cycle).

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

7. **Honesty as architectural principle.** AAD's posture is to make scope and limits visible at the segment level rather than buried in caveats. The framework's conservatism is not a limitation — it is the theory's load-bearing architecture. Specific instantiations: the directed-separation Class 1/2/3 partition with explicit Class 2 scope exit; the regime-indexed (A/B/C) edge interpretation; the strengthen-first-then-soften posture (`feedback_strengthen_before_soften.md`); and `#identifiability-floor`'s reframing of negative results as structural features that strengthen the machinery that escapes the floor. Per Opus's audit observation (2026-04-22 evening): "the framework's honesty is load-bearing." When considering new content or repair, prefer the form that surfaces scope and limits rather than the form that overclaims and is later forced to caveat.

## What's Settled vs. Open

The summary below is the architectural snapshot — settled load-bearing results and the open structural questions. For live work-in-flight (pending findings, tier-C deferrals, open MEDIUM items, missing segments), see `TODO.md`. For the spike trail that produced these, see `msc/SPIKES.md`.

**Note on settled vs. under-review.** Several items in the Settled list below have *architectural proposals under review* in `msc/architectural-proposals-2026-04-22.md` — moves that would reframe or generalize the item rather than overturn it. Notable examples: the $G_t = (O_t, \Sigma_t)$ decomposition would become a *property* rather than axiomatic under O-BP2 (compressions-as-projections); the AND/OR single-parameter-edge commitment would be generalized under O-BP4 (continuous-valued DAG); directed separation's classification would sit inside a continuous tiering under O-BP3. "Settled" here means "the current working commitment"; portfolio moves may change them. See `TODO.md` §"Strategic Architectural Proposals" for the current set.

### Settled (from convergence testing + spikes)
- Single-parameter edges with AND/OR nodes
- Orient cascade structure (derived from information dependency)
- Additive log-confidence decay (generalizes $p^n$)
- Observability as strategy enablement
- Directed separation (with architectural classification, not κ-scalar). 2026-04-22: positioned as the **Pearl-blanket conservative form** of the Markov blanket per Bruineberg et al. 2022 — AAD adopts the conditional-independence statement with explicit Class 2 scope exit, refuses the Friston-blanket metaphysical reading.
- $G_t = (O_t, \Sigma_t)$ split (definitional)
- Satisfaction gap / control regret split — 2x2 disambiguation table is the working **decision-theory diagnostic** that AI's preferences-as-priors form collapses (per `#satisfaction-gap`, contrasted with EFE pragmatic/epistemic; Sun & Firestone 2020 dark-room cite)
- DAG acyclicity derived from temporal ordering
- Composition consistency required by scope condition's level-independence
- α/T relationship verified for all correction function classes (α proportional to T)
- Strategic tempo $\mathcal{T}_\Sigma$ (defined, verified against four topologies)
- Cognitive cost of $\Sigma_t$ (IB/MDL framework, max useful depth $d^\ast$). 2026-04-22: G-BP2 V-medium executed — variational form with KL-divergence to optimal-policy posterior replaces Shannon-MI relevance term (closes Gemini Finding 2/3's Shannon-zero degeneracy), aligned with active-inference variational machinery without committing to preferences-as-priors or EFE-as-master
- Three-way exploit/explore/deliberate: extended deliberation threshold derived; two-stage decomposition and dominance regimes are discussion-grade (simulation shows unified objective outperforms two-stage; deliberation rarely chosen by oracle)
- P3→Markov proved via Causal Markov Condition theorem (conditional on causal sufficiency; P3 is now consequence, not premise)
- Correlation Hierarchy (L0/L1/L1'/L2) in strategy-dag — correlated failure first-class, independence as tractable special case. 2026-04-22: L1' formal transfer derived for soft-facilitator regime under observable common cause (Prop B.7, five-way gating); refuted under unobservable common cause via Cramér-Rao floor (Fisher rank-1)
- Convention hierarchy (C1/C2/C3) in value-object with monotonicity result — diagnostics scale from local heuristic to global
- Sector-persistence template factored out as shared lemma; six AAD persistence-flavored results re-expressed as instances. 2026-04-22: positioned as **broader-validity** apparatus than FEP-flow (Aguilera et al. 2022 narrows the FEP-flow argument's parameter regime; AAD's Lyapunov/sector machinery applies wherever (T1)–(T3) hold — Khalil 2002 ch. 4)
- **Identifiability-floor pattern** (added 2026-04-22): structural no-go results derived from external information-theoretic theorems strengthen the load-bearing role of AAD machinery that supplies the unique escape. Two derived instances: F1's on-policy detection no-go (CHT) sharpens `#loop-interventional-access`; F13's L1' mixture-identifiability obstruction (Cramér-Rao) elevates observability-as-information-augmentation. Three open extensions: causal-IB, misspecification cost, tier-switching cost
- Loop interventional access — sharpened 2026-04-22 with three distinctive AAD moves named (Bareinboim hierarchy connection, regime-indexed identification, scope honesty per Bruineberg et al. 2022) and honest credit to broader action-perception-loop lineage (Friston 2017, Parr & Pezzulo 2022, Wiener 1948, Conant & Ashby 1970). **2026-04-23:** ontologically grounded in #agent-identity's singular-trajectory scope commitment (O-BP6); replaying from a checkpoint is not intervening
- TST $\mathcal{C}_t^{\text{commit}}$ subset (added to NOTATION.md 2026-04-22) with conditional maximality result (under cryptographic immutability, cryptographic authorship, standard universal retrieval, mainline-bounded scope) and per-quantity exactness audit identifying ~14 EXACT estimators
- **Strategy-cost objective direction** (added 2026-04-22/23 cycle): the $\pi^\ast$-first KL direction in `#strategy-cost-regret-bound` is forced by the regret-bound derivation (forward-KL vacuous under deterministic $\pi^\ast$); the specific reverse-KL form within the admissible f-divergence family is forced by the chain-rule additivity axiom (Hobson 1969 / Csiszár 1991 / Shore-Johnson 1980 / Aczél-Daróczy 1975). Axiom AAD-internally motivated as divergence-level analog of #chain-confidence-decay
- **Log-odds as the natural edge-update coordinate** (added 2026-04-22/23 cycle): `#edge-update-natural-parameter` derives log-odds as uniquely forced (up to positive affine) under the evidential-additivity axiom (Aczél 1966 Cauchy functional equation). Axiom AAD-internally motivated as update-level analog of #chain-confidence-decay. `#credit-assignment-boundary`'s default signal function now stated in log-odds (domain $\mathbb{R}$, sigmoid readout); the prior unbounded-gradient mechanical break (Gemini Finding 2) is resolved structurally
- **Three-layer additive-decomposition pattern** (discovered 2026-04-22/23 cycle): three independent uniqueness theorems — chain-confidence-decay, reverse-KL, log-odds — share structural shape: Cauchy-functional-equation argument on an AAD-internally-motivated additivity axiom forces logarithmic coordinates. Products of independent factors decompose additively on log-scale coordinates; the coordinate is uniquely forced in each case. Documented in `msc/architectural-proposals-2026-04-22.md` §SP-1; candidate for promotion to explicit meta-segment in a future session
- **A2' sub-scope partition** (added 2026-04-22/23 cycle): `#gain-sector-bridge` + `#sector-condition-derivation` carry explicit sub-scope α (A2' derived via directional fidelity under Kalman / conjugate-Bayesian / exponential-family-in-natural-parameters / gradient-on-strongly-convex / linear-with-PD-KH) vs sub-scope β (A2' assumed: PID / rule-based / human-judgment / severely-misspecified / variational-approximation / non-convex-beyond-basin / per-step-SGD). Sub-scope label inherited by all `#sector-persistence-template` instances via the template's A2' dependency. Prop A.1S region condition lifted into proposition statement via stopping-time localization (Khasminskii 2012)
- **Separability pattern meta-segment** (added 2026-04-22/23 cycle): `#separability-pattern` names AAD's positive-half scope posture — separable-core / structured-repair / general-open — across six ladders (correlation, convention, architecture, contraction, identification regime, scope hierarchy). Positive-half complement to `#identifiability-floor`. Together with `#approximation-tiering` (structural template) and `#independence-audit` (failure structure) forms three-part scope characterization
- **Software as AAD's calibration laboratory** (added 2026-04-22/23 cycle): TST repositioned in `#software-epistemic-properties` + `02-tst-core/OUTLINE.md` preamble as "privileged high-identifiability calibration laboratory" (not "richest operationalization domain"). Transfer-assumption table makes non-software identification relaxations explicit per AAD-core quantity
- **Agent identity as formal scope statement** (added 2026-04-22/23 cycle): `#agent-identity` promoted to type:scope / status:robust-qualitative. AAD applies to agents instantiated on singular, non-forkable causal trajectories. Three load-bearing consequences: sufficiency is trajectory-indexed, model merging is lossy by construction, interventional access in the loop depends on trajectory singularity. Type-like (equivalence-class) agents are out of formal scope

### Open
- Edge identifiability conditions (resolved in software, open in general)
- Composition laws (specific forms are sketches; existence is required)
- Coupled formulation for logogenic agents
- Causal-IB extension for interventional relevance variables (open per #identifiability-floor)
- Misspecification-cost quantification under finite information budget (open per #identifiability-floor)
- Tier-switching policy cost (open per #identifiability-floor; overlaps with O-BP7)
- V-strong G-BP2 — paper-writing-time decision on whether to ever present AAD as control-theoretic specialization of active inference (deferred per `msc/spike-active-inference-vs-aad.md` §I action 5)

### Known Fragilities
- ~~Edge semantics claim interventional but update from observational~~ — resolved 2026-04-02 as regime-indexed interpretation (causal efficacy estimate with A/B/C regime classification)
- Missing commitment/resource/temporal structure in the DAG
- Directed separation violated by goal-conditioned agents (LLMs) — resolved as architectural scope, not approximation
- ~~L0 residual mechanism collapses on-policy~~ — resolved 2026-04-22 by F1 strengthening: converted to a no-go theorem; the covariance test is now framed as the unique broadly-available violation of the no-go's scope, not a chosen primary
- ~~L1' formal transfer is "open"~~ — resolved 2026-04-22 by F13 strengthening: derived for observable-$C$ (Prop B.7); refuted for unobservable single-channel via Cramér-Rao floor

## File Organization

**Root level (Agentic Systems):**
- `OUTLINE.md` — **Top-level assembly index** across all parts.
- `TODO.md` — **Active work items.** Pending findings, tier-C deferrals, open MEDIUM items, missing segments, and an Archive section for completed cycles. Live; read first when picking up work.
- `FORMAT.md` — **Segment file conventions.** How to write claim files. Includes the Epistemic Triage (three questions + three rings of segment content).
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
