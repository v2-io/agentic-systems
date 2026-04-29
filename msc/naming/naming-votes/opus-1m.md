# Naming Votes — Opus 1M (NOT COLD-START)

**Disclosure.** I am the agent that conducted the architectural-proposals consolidation audit on 2026-04-24 (see `PROPOSALS.md`, `LOG.md` §"2026-04-24 — Architectural-Proposals Consolidation Audit", and `msc/reflections/20-breadth-compression-and-the-proposals-audit.md`). I have read the full original brainstorm at `msc/naming/naming-brainstorm-2026-04-24.md` and discussed it with Joseph, reaching specific points of disagreement. I co-authored the principles file itself.

Therefore this vote is NOT a genuine cold-start. It reflects my actual independent judgment formed through that process. The aggregation script should weight my votes with that in mind:

- **My agreements with the original agent** are anchored — some are genuine independent agreement; some may be residual anchoring I can't fully introspect away.
- **My disagreements with the original agent** are probably stronger signal because they survived the discussion and explicit articulation.
- **My novel discoveries** (items the original didn't raise) come from the audit context rather than fresh segment review.

Focus of my vote: (1) the Čencov critique of `#cauchy-coordinates`, (2) a strong preference for `#equilibrium-composition` over `#game-theoretic-composition`, (3) several header-name additions surfaced by the PROPOSALS.md §H.5 outline-filter affordance work, (4) a few novel unnamed-slot proposals surfaced during the audit.

## Votes

| current-name | new-name-candidate | weight | notes |
|---|---|---|---|
| #additive-coordinate-forcing | #forced-coordinates | +3 | The segment carries four primary instances: three via Cauchy functional equation (chain / divergence / update) and one via Čencov-invariance (metric). The segment itself states (line 50): "Both clear the broader discipline — uniqueness-theorem-forced coordinate under AAD-internal axiom — but via distinct uniqueness-theorem machineries." Naming the meta-pattern after only one machinery (Cauchy) violates the scope-honesty the segment just established. "Forced coordinates" covers both machineries. Preserves "additive-coordinate-forcing" as long-form in the segment subtitle. |
| #additive-coordinate-forcing | #cauchy-coordinates | -1 | Explicit rejection. The Čencov metric-layer 4th primary instance is NOT Cauchy-FE; naming the meta-pattern for one of two machineries violates the scope-honesty commitment the segment establishes in its own Discussion section. Short and crisp, but scope-dishonest. |
| #additive-coordinate-forcing | #coordinate-forcing | +1 | Acceptable alternative to #forced-coordinates; names the activity in verb form. Slightly less concrete than "forced coordinates" as a noun. |
| #additive-coordinate-forcing | #axiom-forcing | -1 | Underdescriptive — doesn't convey that the *thing forced* is a coordinate. |
| #additive-coordinate-forcing | #additive-lift | -1 | "Lift" is overloaded in math (bundle lifts, category-theoretic lifts) and doesn't suggest uniqueness-theorem forcing. |
| #separability-pattern | #separability-ladder | +3 | Agree with original brainstorm. "Ladder" is the right geometry for the seven-ladder structure (ascending difficulty from separable core). Upgrading from original's weak preference to strong — the seven-ladder enumeration in the segment explicitly instantiates the ladder geometry. |
| #separability-pattern | #separability-staircase | -1 | Whimsical without compensating precision gain. |
| #identifiability-floor | #identifiability-floor | +3 | "Floor" metaphor is load-bearing; no better candidate. Keep. |
| #strategic-composition | #equilibrium-composition | +3 | Strong preference over #game-theoretic-composition. The segment's actual derivation is equilibrium convergence under Monderer-Shapley potential games (1996) and Rosen monotone games (1965); "equilibrium" is scope-honest and narrower. "Game-theoretic" invites future segments that are not equilibrium-based (e.g., mechanism-design, information-design) into the same namespace prematurely. |
| #strategic-composition | #game-theoretic-composition | -1 | Broader than current segment content; invites scope creep. If Section III later adds non-equilibrium game-theoretic material, a separate segment with a distinct name would be cleaner than sharing one overloaded bucket. |
| #developer-as-act-agent | #developer-as-adaptive-agent | +3 | Mechanical rename. "ACT" era slug is a 2026-04-16 relic. "Adaptive agent" matches LEXICON vocabulary; framework-name-free slug won't rot under future renames. |
| #ai-agent-as-act-agent | #ai-agent-as-adaptive-agent | +3 | Parallel rename; same reasoning. |
| satisfaction gap | satisfaction gap | +3 | Crispest pair in the project. The 2×2 disambiguation table organizes itself in the reader's head because of the naming. Do not touch. |
| control regret | control regret | +3 | Pairs with satisfaction gap. |
| chronica ($\mathcal{C}_t$) | chronica | +3 | Greek root, avoids entropy-ℋ collision, carries the right philosophical weight for singular non-forkable trajectory. Especially load-bearing for the (PI) axiom and logozoetic extensions. |
| orient cascade | orient cascade | +3 | Good as-is. |
| adaptive reserve ($\Delta\rho^\ast$) | adaptive reserve | +3 | Good as-is. |
| update gain ($\eta^\ast$) | update gain | +3 | Good as-is. |
| logogenic / logozoetic | logogenic / logozoetic | +3 | Deliberate neologisms filling memorable-noun slots; keep. |
| strategy DAG ($\Sigma_t$) | strategy DAG | +3 | Adopted from probabilistic graphical models; keep. |
| agent opacity ($H_b^{A\|B}$) | agent opacity | +3 | Adopted $H_b$ from Hafez 2026 with AAD-native framing. Works. |
| exploit / explore / deliberate | exploit / explore / deliberate | +3 | Three-way extension of two established terms; reads naturally. |
| Auftragstaktik principle | Auftragstaktik principle | +3 | Load-bearing historical adoption. |
| prolepsis / aisthesis / aporia / epistrophe / praxis | [keep whole vocabulary] | +3 | Deliberate aesthetic commitment. Working. |
| AAD (Adaptation and Actuation Dynamics) | AAD | +3 | Recent rename (2026-04-16); further churn dilutes identity. Naming collisions have already narrowed options. The "Actuation" asymmetry is real but handled more cheaply by a Section II preamble clarification. |
| convention hierarchy (C1/C2/C3) | convention hierarchy | +3 | Disagreeing with original brainstorm's P4 "rename to continuation hierarchy." The rename churn (every C1/C2/C3 reference across segments needs updating) outweighs the Lewisian-baggage benefit. Working vocabulary is stable; keep. Explicit-keep rather than absence-of-vote because I considered the rename. |
| convention hierarchy | continuation hierarchy | -1 | Considered and rejected. "Continuation" is more self-descriptive but the project's "convention" usage is established and the rename would churn across dozens of references. |
| correlation hierarchy (L0/L1/L1'/L2) | correlation hierarchy | +1 | Keep unless #separability-ladder lands AND the parallelism between the three ladders (correlation / separability / continuation) is judged load-bearing. Conditional keep. |
| correlation hierarchy | correlation ladder | +1 | Conditionally admit the rename only if other ladder-renames land; otherwise keep. Weak. |
| L1' (prime decoration) | L1-observable | +1 | Agree with original. "L1-prime" awkward to speak; "L1-observable" matches the Prop B.7 observable-common-cause distinction from the 2026-04-22 strengthening cycle. Keep L1' as shorthand symbol. |
| $\alpha_1$ (A2' fixed-gain sub-scope) | derived-gain regime | +1 | English equivalent for prose use. Keep $\alpha_1$ as symbol. |
| $\alpha_2$ (A2' adaptive-gain sub-scope) | adaptive-gain regime | +1 | Parallel to $\alpha_1$. |
| $\beta$ (A2' assumed-sector sub-scope) | postulated-sector regime | +1 | Parallel. "Postulated" slightly stronger than "assumed" — conveys the axiomatic move explicitly. |
| sector condition | sector condition | +3 | Adopted from nonlinear control (Khalil, Vidyasagar); baggage correct. Keep. |
| #sector-persistence-template | #sector-persistence-template | +3 | Technical but clear; role as shared-lemma is legible. Keep. |
| directed separation | directed separation | +3 | Keep. The LQR-separation-principle echo is real but best handled by a one-sentence clarification in segment Discussion, not a rename. |
| composition closure / closure defect ($\varepsilon^\ast$) | composition closure / closure defect | +3 | Keep. CS-closures collision is an inoculation issue (preamble note), not a rename issue. |
| [concept: the parameter-space region within which an agent maintains bounded mismatch indefinitely] | persistence envelope | +3 | Strong preference (upgrading from original's +1). Engineering vocabulary, geometrically evocative. "Well inside its persistence envelope" reads more crisply than "satisfies the persistence condition with non-marginal adaptive reserve." Genuinely useful new named slot. [original phrasing: unnamed: the sector-persistence region in parameter space where the agent is guaranteed to maintain bounded mismatch] |
| [concept: the structural meta-pattern in #disc-additive-coordinate-forcing combining one foundational lemma with three derived results] | chain anchor | +3 | Upgrading from original's +1. The "1-anchor-plus-3-theorem" structure references this role five times across `#additive-coordinate-forcing` and its instance segments. Naming it as "the chain anchor" in prose (not renaming the segment) pays off on every reference. [original phrasing: unnamed: the chain-layer anchor role in #additive-coordinate-forcing] |
| [unnamed: cascade of inferential force strengthening from C1 to C3 on satisfaction-gap / control-regret diagnostics] | inferential cascade | +1 | Agree with original. Low priority. |
| [concept: the sequence of cycle phases (Prolepsis–Aisthesis–Aporia–Epistrophe–Praxis) considered as a single named whole] | the pentad | +1 | Agree with original. Low priority. Names the five-phase sequence as a unit. [original phrasing: unnamed: cycle-phase sequence as a whole] |
| epistemic architecture | epistemic architecture | +3 | Keep as framing language in CLAUDE.md §7 and OUTLINE.md. Do NOT promote to fourth meta-segment — the three meta-segments (#identifiability-floor / #separability-pattern / #additive-coordinate-forcing) already do the technical work. |
| strengthen-first posture | strengthen-first posture | +3 | Current name is actionable and precise. Rejecting original brainstorm's alternative ("attempt the improbable"). |
| strengthen-first posture | attempt the improbable | -1 | Aspirational; less directive than "strengthen-first." Not an improvement. |
| scope-honesty-as-architecture | scope-honesty-as-architecture | +3 | CLAUDE.md §7 element (a). Working term; keep. |
| calibration laboratory (framing for TST) | calibration laboratory | +3 | C-BP3 landing; well-chosen. Keep. |
| ## Formal Expression (segment header) | ## Formal Expression | +3 | Public API for outline-filter (see PROPOSALS.md §H.5). Established. Keep. |
| ## Epistemic Status (segment header) | ## Epistemic Status | +3 | Public API; keep. |
| ## Discussion (segment header) | ## Discussion | +3 | Public API; keep. |
| ## Working Notes (segment header) | ## Working Notes | +3 | Public API; keep. FORMAT.md's "remove at candidate stage" policy should soften (per PROPOSALS.md §H.5) but the *name* of the section should stay. |
| [unnamed: future segment-layer header for the SP-5 Reader's Path proposal] | ## Reader's Path | +1 | Forward-looking name reservation. SP-5 adds a 1-2 sentence load-bearing preamble per segment; under the outline-filter affordance this becomes its own filterable layer. Naming the header now stabilizes the API even before the content lands. |
| [unnamed: future segment-layer header for narrative/pedagogical framing] | ## Narrative Framing | +1 | Parallel reservation. For ELI10 / pedagogical outlines. |
| [unnamed: future segment-layer header for the O-BP14 derivation-audit table] | ## What Is Derived | +3 | Already in use in 5 segments per O-BP14 landing; name is stable. Reserve formally. |
| (PI) parameterization-invariance axiom | (PI) | +3 | Good abbreviation with named expansion; works in both forms. Keep. |
| Čencov-invariance | Čencov-invariance | +3 | Adopted from Čencov 1982; keep attribution. |
| Pearl's causal hierarchy | Pearl's causal hierarchy | +3 | Adopted concept; keep attribution per prior-art-integration convention. |
| information bottleneck | information bottleneck | +3 | Adopted (Tishby 1999); keep. |
| Lohmiller-Slotine contraction | Lohmiller-Slotine contraction | +3 | Adopted (1998); keep. |
| Hafez's $H_b$ | $H_b$ | +3 | Adopted; keep. |
| Bruineberg's Pearl-blanket / Friston-blanket | Pearl-blanket / Friston-blanket | +3 | Adopted (Bruineberg 2022, credit Martin Biehl per fn 3 of that paper per citation audit); keep. |
| Miller's meta-machine / extreme transition motif | meta-machine / extreme transition motif | +3 | Adopted (Miller 2022); keep. |
| stability-plasticity feasibility window | stability-plasticity feasibility window | +3 | From `#consolidation-dynamics`; good name as-is, adopts well-known "stability-plasticity dilemma" baggage and adds the feasibility-window refinement. Keep. |
| DA2'-inc | DA2'-inc | +1 | Technical; symbol-grade. The prose equivalent "incremental sector bound" works; keep symbol as shorthand. |
| three-part meta-architecture | floor / ladder / forced-coordinates | +1 | Conditional collective-noun-trio. If both #separability-ladder and #forced-coordinates land, the trio is "floor / ladder / forced-coordinates" — three concrete nouns, three cross-sectional views of AAD's architecture. Parallelism weaker than "floor / ladder / Cauchy-coordinates" but scope-honest across both machineries. |

## Principles-observations

Three observations from my (non-cold-start) perspective that may be worth folding into the principles file:

1. **Scope-honesty is a naming axis that dominates memorability for meta-segment names specifically.** The original brainstorm's `#cauchy-coordinates` proposal is more memorable than `#forced-coordinates` but less scope-honest (it excludes the Čencov instance). For meta-segment names in a framework that explicitly foregrounds scope-honesty as an organizing principle, scope-honesty should dominate memorability. For ordinary concept names this tradeoff may reverse — it's an axis that principles-file currently treats as equal rather than context-dependent.

2. **Header-name stability is now public-API-stability** under the outline-filter affordance added in PROPOSALS.md §H.5. This changes the rename-cost calculation for any `## X` section: a rename ripples not just across segments but across any outline that filters on the header. The principles file mentions "segment section headers" as eligible but doesn't quite surface that these are now infrastructure-level names.

3. **The Greek-vocabulary commitment (chronica / prolepsis / aisthesis / aporia / epistrophe / praxis / logogenic / logozoetic) is aesthetic *and* epistemic.** It signals the integration-not-invention posture (old vocabulary + novel synthesis). Making this commitment explicit in the principles file (e.g., "Greek-root preference for framework-defining concepts; English for technical operations") would help future agents extend consistently and would give Section III completion work a vocabulary anchor — the four named Section III GAPs (latent structural diversity; endogenous coupling; composition transition dynamics; computational thresholds for social behavior) each need names, and Greek-vocabulary coherence is worth naming as a preference.
