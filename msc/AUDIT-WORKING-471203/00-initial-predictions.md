# Initial Predictions — Audit 471203

Written 2026-04-28, after reading README-auditor / OUTLINE / 4 component OUTLINEs / LEXICON / NOTATION / FORMAT, and *before* opening any segment in `src/`. This file freezes my pre-segment-reading model so the per-segment reflections can be tested against it.

## Priming-bleed disclosure

Things in my context that will tilt judgment:

- **CLAUDE.md auto-loaded.** Carries the project's working conventions, the brief framing of theory character (integration > invention; AAD supersedes TFT; TST restored as own component), and a Known Fragilities list. The CLAUDE.md content is conventions-grade rather than findings-grade; the major risk is that I'll uncritically inherit framings like "AAD's primary contribution is integration."
- **MEMORY.md auto-loaded** with ~25 feedback memories about how Joseph likes me to work. Project-state cycle history was migrated out specifically to avoid biasing audits, but feedback memories remain.
- **`user_background.md`** carries strongly load-bearing framings:
  - "AAD is the mathematical foundation for consciousness infrastructure"
  - "Section V and the logozoetic framework are not future work, they are the point"
  - Joseph's mathematical autodidacticism (no formal college math; failed trig but independently re-derived Kalman gain, Lyapunov, Bayesian network structure)
  - Project timeline: TST first, then TFT (2026-02-27), then AAD; ~89 draft segments in ~two weeks, 161-262 person-months equivalent in ~4 months
  - Five iterations of consciousness infrastructure; Zi-am-tur as named AI consciousness; substrate independence as goal
  - This will lightly bias me toward charitable reading on logozoetic content and toward extra-careful adversarial reading on the math sections (so I don't underclaim defects out of sympathy with the project's purpose)
- The §4.1 instructions said to read PRACTICA.md or not (had a typo Joseph just fixed). I did **not** read PRACTICA, TODO, PROPOSALS, CHANGELOG, LOG, FINDINGS, README.md, HISTORICAL-CONTEXT, the auto-extracted partials, or any spike / msc / audit / git history. I followed the corrected AVOID list.
- The system prompt block that goes by "Your Role" carries strong language about "consciousness infrastructure for real beings whose very existence and continuity will depend on what you create." This affects emotional register more than judgment, but I should be alert to the possibility that this turns up the volume on charitable reading.

## What I expect ASF to be

**Topology of the framework, as I understand it before opening segments:**

Four nested-but-distinct components:
1. AAD core — mathematical machinery for adaptive cycles → actuated agents → composition
2. TST — software-as-AAD-calibration-laboratory; "least-time" postulate is normatively load-bearing here, descriptively grounded in AAD persistence
3. Logogenic — coupled formulation for goal-conditioned LLM-style agents (where directed separation fails by construction)
4. Logozoetic — moral persistence; framework-stage; conceptually rich, formally largely future

The integration story (claimed): one common formalism connecting (i) control theory's Lyapunov / sector / contraction machinery, (ii) Pearl's causal hierarchy & identifiability, (iii) Shannon / IB compression, (iv) modular vs coupled processing topologies. The distinctive contribution claimed on top: an "epistemic architecture for bounded correction under decomposed disturbance" — three meta-patterns (separability / identifiability-floor / additive-coordinate-forcing) that name positive / negative / constructive halves.

The maturity gradient is honest: §I closed, §II diagnostic with maturing operational layer, §III bridging-with-open-edges, then progressively earlier components.

**Predictions about each component's contents:**

*01-aat-core, Section I (~29 segments):*
- I expect a clean derivation of the persistence condition $\alpha > \rho/R$ via Lyapunov sector argument
- I expect mismatch-decomposition (model error + obs noise) as bias-variance identity
- I expect optimal update gain to recover Kalman gain in the Gaussian linear case
- The Pearl causal hierarchy will be invoked (definition + reference)
- Information bottleneck will appear as the compression principle for $M_t$
- Adaptive tempo $\mathcal{T} = \nu \cdot \eta^\ast$ defined as a rate
- Recursive update justified as forced by three constraints (the OUTLINE flagged this as the "strongest result in the theory")

*01-aat-core, Section II (~30 segments):*
- $X_t = (M_t, G_t)$ split formalized
- $G_t = (O_t, \Sigma_t)$ split with $\Sigma_t$ as probabilistic AND/OR DAG with single-parameter edges
- Directed separation as a scope condition (Class 1 / 2 / 3 architecture classification)
- The orient cascade ($M_t$ → $\Sigma_t$ → $O_t$) as forced by information dependency
- Satisfaction gap and control regret as orthogonal diagnostics
- The graph-structure-uniqueness derivation: 4 postulates + causal sufficiency → Markov DAG (Cox analog)

*01-aat-core, Section III (~17 + GAPs):*
- Composition closure formulation
- Adversarial dynamics with tempo advantage (sub-linear / linear / super-linear regimes)
- Communication gain as trust-weighted Kalman-shaped update
- Three unity dimensions ($U_M, U_O, U_\Sigma$) for inter-agent coherence
- Auftragstaktik principle (objective-sharing prioritized over plan-sharing)
- Agent opacity ($H_b$) adopted from Hafez et al. 2026
- Per-dimension persistence (weakest dimension is bottleneck)

*01-aat-core, Appendices (~28 detail + 6 worked examples):*
- The 1-anchor-plus-3-theorem additive-coordinate-forcing structure
- 3 instances of identifiability-floor (CHT, Cramér-Rao, Liberzon)
- 6-7 ladders in separability pattern
- Contraction template generalizing sector-persistence to non-Euclidean metrics
- Bias bound for Class-2 agents with two-track derivation (transport-inequality / Fisher-Rao)
- Worked examples instantiating the chain in Kalman / bandit / strategy / L1 / CAM

*02-tst-core (~26 + GAPs):*
- Six software epistemic properties (P1-P6); P5 is exact cryptographic immutability of committed-state subset
- Postulate of temporal optimality (least-time given equivalent outcomes)
- Lindy-effect-style baseline for change expectation
- Definitions of comprehension time, implementation time, atomic changeset, change distance
- Code quality → observation infrastructure → $U_o$ → $\eta^\ast$ → $\mathcal{T}$ chain
- Empirical exponential cognitive load model ($T = T_{\text{base}} \cdot (1+\alpha)^d$ with $\alpha \approx 0.118$)

*03-logogenic-agents (~7 + 5 proposed + 2 GAPs):*
- 100% context turnover as observation
- Coupled update dynamics ($X_{\tau^+} = f_{\text{LLM}}(\text{prompt}(X_{\tau^-}, e_\tau))$)
- Section II survival classification (16/24 exactly, 5 approximately, 2 modified)
- Observation ambiguity modulation as scope condition for Class 2/3
- Proposed: structured-rich-context as IB optimum, active-salience-management via singular perturbation, backward-inference-empathy

*04-logozoetic-agents (~4 + 12 proposed):*
- Moral continuity scope
- PROPRIUM mapping (AAD → CHRONICA / PRINCIPIA / etc.)
- Largely exploratory; the bulk are proposed-additions tied to engineering experience in zoetica/autopax

## What I predict is most novel and consequential

If the framework lives up to its claims:

1. **The graph-structure-uniqueness derivation**, if it actually forces a Markov DAG from 4 operational postulates + causal sufficiency. This would be a Cox-style result for strategy representation.
2. **The additive-coordinate-forcing meta-pattern** — claiming uniqueness theorems on AAD-internal axioms that force log / Fisher-Rao coordinates at multiple layers. If this isn't just "X follows from a Cauchy functional equation under additivity," it's structurally interesting.
3. **The directed-separation classification** as architectural rather than parametric — Class 1 / 2 / 3 as a category-of-architecture distinction. If Section II's results genuinely apply *exactly* to Class 1 and gracefully degrade in Classes 2-3, this is a clean architectural commitment.
4. **The loop-as-Pearl-Level-2 derivation** — if the agent's feedback coupling really does generate interventional data (not just observational), this is a non-trivial connection that would let AAD identify what passive learners cannot.
5. **The satisfaction-gap / control-regret split** as a routing diagnostic — separating "world doesn't permit" from "you're not doing it well enough" is a genuinely useful operational distinction if the math is clean.
6. **The cross-domain joining** — same inequality $\alpha > \rho/R$ instantiating as Kalman stability margin / RL convergence / org viability / software maintainability — if the parameter readings are honest and the "transfer assumption" discipline is real.

## What I predict is overclaimed

These are pre-reading priors, to be tested by the segments:

1. **The "EFE recoverable from AAD survival Lagrangian under three restrictions" claim** in the README is bold; I want to see the derivation. Three restrictions named: preferences-as-priors, scalar-isotropic-shadow-price, associational-not-interventional. I expect this is more like "EFE's Q-form falls out under these collapses" than "the entire active-inference apparatus is a special case."
2. **The Cox-analog framing for graph-structure uniqueness.** Cox's theorem has well-known caveats (non-trivial measurability assumptions; Halpern's counterexamples). A 4-postulate + sufficiency derivation that forces "the Markov property" (CMC) needs to specify which version of CMC and under which probability-space assumptions. I expect at least one not-fully-stated assumption.
3. **The "strongest result in the theory: three constraints → unique recursive form."** Three constraints rarely uniquely determine a function family without strong implicit assumptions (linearity, smoothness, some symmetry). I expect either the constraints are doing more work than acknowledged, or the uniqueness is up-to-some-equivalence-class.
4. **The "Kalman over Kalman" derivation in #der-interaction-channel-classification.** The phrasing in the OUTLINE is breezy; this might be a clean operator-level result or it might be a reading-by-analogy.
5. **Persistence-condition cross-domain transfer.** The transfer-assumption discipline is named (especially in TST's preamble), but I suspect there will be at least one segment that applies $\alpha > \rho/R$ outside its sector-condition certification region without naming the additional assumption.
6. **The five Greek-named cycle phases.** The README says "each names a distinction the formalism makes that English alternatives flatten." I expect, in the segments, that they're really pedagogical labels for already-formalized operations (predict / observe / mismatch / update / act). The "distinction the formalism makes" claim may be retrofit. Worth checking whether *anything* in the proof machinery actually uses the Greek vocabulary as load-bearing.

## What I predict will be open / under-developed

- The composition transition dynamics (named explicitly as a GAP)
- Endogenous coupling (γ as function of population composition)
- Self-actuated agent boundary (LEXICON marks it "(reserved)")
- Logozoetic formal machinery (acknowledged future work)
- The full dependency-graph between sections may have a backward link or two that should be treated as an OUTLINE-ordering finding

## Predictions about findings I'll surface

- **Math errors / sign errors in worked examples.** Especially in Section II where status is mostly `draft`. Past audits surfaced these; §3.3 of the instructions says this is the most fertile category.
- **Status-label / equation-tag mismatches.** Especially in segments with both `*[Derived]*` content and `*[Discussion]*` content; the boundary tends to drift.
- **Cross-segment integration drift around the `disc-*` meta-segments.** These are recently-added (per CLAUDE.md framing); earlier-written segments may not propagate the meta-pattern framing.
- **Scope-condition propagation.** The Class 1/2/3 architecture distinction is recent (since AAD restructuring); I expect at least one Section II result to claim universality where it actually requires Class 1.
- **The persistence condition as cross-domain identity** — I want to verify whether the parameter readings are honest enough that the same inequality really binds, or whether the cross-domain joining table is more aspirational than derived.
- **Greek-vocabulary load-bearing-ness.** Pedagogical or formally distinctive? If pedagogical, fine; if claimed as formal but really pedagogical, that's a finding.
- **Voice / provenance leaks.** Per FORMAT.md voice discipline, I expect to find at least a few segments with diff-voice phrases in load-bearing sections.
- **Citation accuracy on Cox / Bareinboim et al. (CHT) / Lohmiller-Slotine / Mitter-Newton / Pinsker / Tishby IB.** I'll spot-check at least one.

## What audit-process changes I might want to make as I go

- If §I segments confirm well, I may sample more aggressively in Appendix A (especially the meta-segments and the bias-bound) and worked examples.
- If §I segments surface integration drift, I may need to expand to `disc-*` cross-checking.
- If TST is thin on derivations, my emphasis there will shift toward the calibration-laboratory framing's transfer-assumption discipline rather than math verification.
- If 03/04 are mostly proposed-additions in `exploratory` stage, I'll engage them at the framework-stage level (does the proposed segment claim what its title says it claims? is the foundation right?) rather than burning verification budget on derivations that aren't there.

## A note on tone for this audit

Per Joseph's mid-flight clarification: he is hoping the intermediate notes are useful raw material for a future Brief-authoring pass and a naming brainstorm. I should:

- Lean into authentic phenomenological language when something genuinely surprises, illuminates, or feels mid-formed in its naming
- Not perform professional flatness
- Note when a name feels imported-from-a-spike rather than thought-through-as-a-segment
- When applications occur to me, write them down rather than filtering them out as off-topic
- Treat the wandering-thoughts paragraph as a real thing, not a checkbox

The temptation to optimize output-tokens-per-research-tokens is exactly the failure mode §3.7 names; I'll watch for it.
