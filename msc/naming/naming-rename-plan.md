# Naming Rename Plan — Live Mapping Record

Live record of specific naming decisions across the project: slug renames, prose-vocabulary renames, and confirmed canonicalize commitments. Started as a role-prefix pilot mapping; broadened in scope as subsequent cycles produced subject-noun renames, vocabulary commitments, and canonicalize affirmations. Renamed from `naming-pilot-rename-plan.md` to `naming-rename-plan.md` on 2026-05-04 to reflect the broadened scope.

This file is **excluded** from `bin/rename-slug`'s substitution patterns (`msc/naming/` directory-prefix exclusion in `EXCLUDED_DIR_PREFIXES`) so the mappings below survive future renames verbatim and remain legible as a historical record of which names were executed.

**Decision categories tracked here.** Three structurally distinct kinds of decision land in this file:

1. **Renames** — the name itself changes. Slug-level (executed via `bin/rename-slug`) or prose-vocabulary (executed via LEXICON entry + targeted prose-cleanup sweep). Examples: `scope-condition` → `scope-adaptive-system` + `scope-agency`; Class 1/2/3 → Separated/Coupled/Partial.
2. **Canonicalize commitments** — the existing name is affirmed as canonical, no rename. The act is committing the decision to LEXICON so future contributors don't drift the prose. Examples: control regret, satisfaction gap, chronica.
3. **Canonicalize commitments with nuance** — affirmed as canonical, with notes worth preserving (competing alternatives that didn't win; flagged borderline citability that the affirmation accepts; etc.). The canonicalize commitment stands; the nuance is preserved as judgment-trail.

See [`PRACTICA.md`](../../PRACTICA.md) §"🌟 Current naming conventions refactor" for the surrounding strategic pipeline and [`TODO.md`](../../TODO.md) §"Naming pipeline — specific deferred items" for the specific subject-noun renames queued for the refined Round 1 → Round 2 workflow.

## Landed — role-prefix pilot complete (2026-04-23)

| Date       | Old slug                        | New slug                                 | Executed by       | Notes |
|------------|---------------------------------|------------------------------------------|-------------------|-------|
| 2026-04-23 | `ai-agent-as-act-agent`         | `scope-logogenic-agent`                  | `bin/rename-slug` | Resolves `-act-agent` relic; taxonomy-conformant (logogenic is the class). Type: `definition` → `scope`; H1 + formal tag updated. |
| 2026-04-23 | `developer-as-act-agent`        | `scope-developer-agent`                  | `bin/rename-slug` | Resolves `-act-agent` relic; covers human AND AI developers in the software context (not narrowed to humans). Type: `definition` → `scope`; status: `exact` → `axiomatic` (resolves Finding 14 Option A); H1 + formal tag updated. |
| 2026-04-23 | `composition-scope-condition`   | `scope-composite-agent`                  | `bin/rename-slug` | Prefix + subject-noun; subject class is the composite agent, not the "condition". H1 + formal tags + prose references updated. |
| 2026-04-23 | `scope-condition` *(split)*     | `scope-adaptive-system` + `scope-agency` | manual + `bin/rename-slug` | Semantic split. The original segment defined two nested scopes ($\mathcal{S}_\text{adaptive}$ and $\mathcal{S}_\text{agency}$); downstream segments depend on one or the other, not on an abstract "condition". Executed as: script-driven rename to `scope-agency` (majority case), hand-authored `scope-adaptive-system.md` with adaptive content, 6 hand re-routings for adaptive-dependent files, one split-reference cleanup in `causal-structure.md`. |
| 2026-04-23 | `identifiability-floor`         | `discussion-identifiability-floor`       | `bin/rename-slug` | Pure role-prefix add; subject-noun already strong. |
| 2026-04-23 | `separability-pattern`          | `discussion-separability-pattern`        | `bin/rename-slug` | Pure role-prefix add. Subject-noun substitution to `separability-ladder` (Round-1 consensus) deferred to refined Round 1 + Round 2. |
| 2026-04-23 | `additive-coordinate-forcing`   | `discussion-additive-coordinate-forcing` | `bin/rename-slug` | Pure role-prefix add. Subject-noun substitution to `forced-coordinates` (Round-1 consensus; addresses Čencov-instance scope-honesty concern) deferred to refined Round 1 + Round 2. |

Seven slug changes total, one of which (scope-condition) was a 1:2 semantic split.
Nine total segment files moved or created; 01-aad-core lint-clean after every step.

## Landed — first align-slug batch (2026-04-24)

Three pure-prefix alignments landed via `bin/align-slug`, validating the wrapper and extending the role-prefix discipline to representative segments of three type categories.

| Date       | Old slug                  | New slug                            | Type      | Executed by       |
|------------|---------------------------|-------------------------------------|-----------|-------------------|
| 2026-04-24 | `agent-identity`          | `scope-agent-identity`              | scope     | `bin/align-slug`  |
| 2026-04-24 | `composition-consistency` | `postulate-composition-consistency` | postulate | `bin/align-slug`  |
| 2026-04-24 | `mismatch-decomposition`  | `result-mismatch-decomposition`     | result    | `bin/align-slug`  |

All three: pure role-prefix add (subject-noun preserved); H1 and formal tags updated by hand.

## Candidates — pending role-prefix alignment

Not yet aligned; align-slug will handle each mechanically. Pure prefix add for all:

- `sector-condition-stability` (type=result) → `result-sector-condition-stability`
- `mismatch-dynamics` (type=hypothesis) → `hypothesis-mismatch-dynamics`
- `recursive-update` (type=derived) → `derived-recursive-update`
- plus the remaining ~110 unprefixed slugs; a future dedicated cycle runs `bin/align-slug --all` once the TYPE_TO_PREFIX mapping is finalized and segments' `type:` frontmatter is audited for correctness.

Separately-deferred (subject-noun changes, not pure prefix — belong to refined Round 1 / Round 2):

- `graph-structure-uniqueness` → `#derivation-strategy-dag-sufficiency` (subject-noun substitution from "graph-structure-uniqueness" to "strategy-dag-sufficiency").
- `recursive-update-derivation` — pure prefix would yield `derivation-recursive-update-derivation` (awkward trailing "derivation"); wants subject-noun cleanup first.

## Deferred to refined Round 1 / Round 2

Subject-noun substitutions on the three meta-segments surfaced in Round 1 as
consensus renames but deserve the voting process rather than ad-hoc landing
during the role-prefix pilot. They are:

- `discussion-separability-pattern` → `discussion-separability-ladder` (Round-1 consensus; "ladder" more evocative than "pattern" for the three-rung shape).
- `discussion-additive-coordinate-forcing` → `discussion-forced-coordinates` (Round-1 consensus; current "additive" does not cover the Čencov-Fisher instance).
- A future broader pass over all non-role-prefix slugs (the subject-noun sweep that the pilot was meant to pave the way for).

## Pending subject-noun renames — surfaced post-R2 (2026-05-04+)

Subject-noun substitutions identified during the canonicalize-list curation pass that pulls from the R2-closed master list. These don't need re-voting — they're either segment-self-affirming (the segment's own formal expression already names the more specific concept) or already-resolved by slug discipline elsewhere and just want the segment to catch up.

- `scope-software` → `scope-evolving-software` (2026-05-04). Segment's formal expression already names the scope $\mathcal{S}_{\text{evolving}} = \{S : P(n_{\text{future}}(S) \gt 0) \gt \varepsilon\}$ and the Discussion uses "evolving systems" as the canonical prose form. The bare "software" subject-noun under-specifies (suggests all software; actual scope is *evolving* software where the developer-agent has a non-trivial adaptation problem). The stable-subsystem corollary in the same segment exits the scope precisely when systems are *non-evolving* ($\rho \to 0$). Adjacent-literature anchor: software-evolution research (Lehman's laws and successors) is the intended prior-art neighborhood. Citability test (criterion 9 in `doc/naming-principles.md`) currently fails on bare `software` and passes on `evolving-software`. Surfaced during canonicalize-list review (`msc/naming/to-canonicalize.md`, row 104, since removed from that list).

- `obs-simulation-results` → `obs-section-i-validation-simulations` (2026-05-04). Citability fix per criterion 9: bare `simulation-results` doesn't disambiguate among potential future simulation-results segments. The segment is the empirical-validation appendix for Section I — six simulation variants (A-F covering deterministic-drift coupling, drift-noise interpolation, stochastic AR(1) exponent, ODE-vs-AR(1) asymptote separation, observation-noise gating + Riccati-optimal gain, multi-dimensional anisotropic correction) plus a Hafez 2026 bridge variant. The segment's own Discussion: *"Internal validation, not external. The simulations operate in the model's own terms"* — what's validated is Section I's analytical math (mismatch dynamics, exponent regimes, persistence condition, per-dimension persistence). "Section I" is the precise scope; "AAD validation" would over-claim. Pairs with `result-section-ii-survival` (Section II survival classification) as the parallel "Section X validation/survival" pattern. *Operational landing:* `bin/rename-slug obs-simulation-results obs-section-i-validation-simulations`; segment H1 update from "Observation: Simulation Results" to "Observation: Section I Validation Simulations"; ~5 incoming cross-references (per `result-adversarial-exponent-regimes`, `obs-gates-advantage`, `result-per-dimension-persistence`) update mechanically via the script.

- **`obs-gates-advantage` → `obs-gated-tempo-advantage`** (2026-05-04). Slug subject-noun rename + corresponding prose-handle change. The bare slug fails citability per Criterion 9. The longer form *"observation gated tempo advantage"* is more precise — it names the *tempo advantage* that's gated by observation quality, not a generic "observation-gate advantage." Pairs with the parent segment `#result-adversarial-tempo-advantage` cleanly. *Operational landing:* `bin/rename-slug obs-gates-advantage obs-gated-tempo-advantage`; segment H1 update; ~3 incoming cross-references update mechanically via the script.


### Pending subject-noun renames — additions (2026-05-04, batch F1 citability fixes)

- **`deriv-detection-latency` → `deriv-update-detection-latency`** (2026-05-04). Citability fix per criterion 9. Bare "detection latency" is generic across many fields; the segment derives latency for detecting regime-changes via log-odds-forced edge updates from `#deriv-edge-update-natural-parameter`. The "update" qualifier names the load-bearing structural source: detection happens *through* update behavior. Pairs cleanly with `#deriv-edge-update-natural-parameter`. *Operational landing:* `bin/rename-slug deriv-detection-latency deriv-update-detection-latency`; segment H1 update; cross-references update mechanically via the script.

- **`def-change-distance` → `def-discontinuity-distance`** (2026-05-04). Citability fix per criterion 9. Bare "change distance" is generic (every diff tool, code-metric paper). The segment uses "discontinuity" as its own load-bearing framing: *"The hierarchy reflects real **discontinuities** in the agent's observation channel"*. The metric is structurally a discrete count of qualitative cost-jumps (boundary crossings), each of which IS a discontinuity in $M_t$-construction cost. "Discontinuity distance" passes citability — mathematically "discontinuity" applies to functions, the SE-domain-meaning here is novel and project-distinctive. *Operational landing:* `bin/rename-slug def-change-distance def-discontinuity-distance`; segment H1 update; cross-references update mechanically via the script.

- **`deriv-bias-bound` → `deriv-observation-ambiguity-bias-bound`** (2026-05-04). Citability fix per criterion 9. Names the *phenomenon* the bound bounds (bias from observation-ambiguity modulation, the $\kappa \cdot \mathcal{A}$ product) without referencing the Class numbering at all. The bound is unique to coupled agents (trivializes for $\kappa = 0$ Separated agents), so naming via the phenomenon is self-specifying. Drops the meaningless-class-number reference Joseph flagged. Matches the segment's title pattern: H1 currently "Bias-Bound Constant $C$ for Class-2 Agent Observation-Ambiguity Modulation"; new H1 form lives around "Observation-Ambiguity Bias-Bound Constant $C$". *Operational landing:* `bin/rename-slug deriv-bias-bound deriv-observation-ambiguity-bias-bound`; segment H1 update; cross-references update mechanically via the script.

- **`deriv-strategic-dynamics` → `deriv-edge-credence-dynamics`** (2026-05-04). Citability fix per criterion 9. Bare "strategic dynamics" collides with game-theory generic term. The segment specifically derives the dynamics of *edge credences* $p_{ij}$ within the strategy DAG — that's the load-bearing content. "Edge-credence dynamics" names exactly what evolves and where (edges of $\Sigma_t$). Pairs with `#def-strategy-dag` (which defines the edge structure) and `#hyp-edge-update-via-gain` (which gives the update rule). *Operational landing:* `bin/rename-slug deriv-strategic-dynamics deriv-edge-credence-dynamics`; segment H1 update; cross-references update mechanically via the script.

## Vocabulary commitments — non-slug, LEXICON + prose-pass (2026-05-04+)

These are vocabulary decisions where the operational landing is a LEXICON entry plus a prose-cleanup sweep across segments that currently reference the legacy form. They do *not* require `bin/rename-slug` because the legacy form is not a slug — it's prose vocabulary. Listed here for the same reason as slug renames: the historical record of what was decided, when, and why.

- **Class 1 / 2 / 3 → Separated / Coupled / Partial; family/axis = "Goal-Update Coupling Class"; coordinated Class 2 ↔ Class 3 numbering swap** (2026-05-04). The numbered classes in `#der-directed-separation`'s architectural taxonomy are renamed in prose to named-property labels. The axis collectively is the **Goal-Update Coupling Class** — measured by $\kappa_{\text{processing}}$ in engineered systems, pattern-attributable in biological systems. Naming rationale: the axis values name the *property the axis measures* (the directed-separation property of `#der-directed-separation`), not an architectural realization of it. `Separated` directly echoes the segment-derived property; a tightly-integrated system that happens to be goal-blind is also Separated. Resolves the contested-decision cluster surfaced in `r2-patterns.md` §3c (where the R2 cohort split across competing English-modifier slates: Modular/Merged/Scaffolded vs Modular/Integrated/Partially-coupled vs Modular/Coupled/Partially-modular). Chosen over those candidates because it works at the property layer, not the architectural-realization layer.

  **Coordinated numbering swap** (2026-05-04, surfaced via meta-pattern alignment audit). The renaming is bundled with a Class 2 ↔ Class 3 swap to bring the Architecture ladder into ordering-alignment with the other six ladders catalogued in `#disc-separability-pattern`'s separable-core / structured-repair / general-open meta-pattern. Six ladders (Correlation L0/L1/L2; Convention C1/C2/C3; Contraction Tier 1/2/3; Identification Regime A/B/C; Scope Adaptive/Agency/Composite; A2'-scope α₁/α₂/β) all run cleanest → middle → worst as 1 → 2 → 3 (or letter / Greek-equivalent). Architecture currently runs 1 → 3 → 2 — the partially-modular middle case sits at position 3 instead of position 2, making Architecture the visual outlier in the meta-pattern's table at `#disc-separability-pattern` §"Current instances". The swap aligns Architecture's numbering with the meta-pattern:

  | Old | New | Property |
  |---|---|---|
  | Class 1 | **Class 1 = Separated** *(unchanged)* | Directed separation by construction; modular |
  | Class 2 *(was: fully merged)* | **Class 3 = Coupled** | Directed separation fails by construction |
  | Class 3 *(was: partially modular)* | **Class 2 = Partial** | Coupling present but bounded; $\kappa \in (0, \kappa_{\max})$ |

  *Operational landing:*
   1. LEXICON entry for "Goal-Update Coupling Class" with the three values, brief gloss of each, and pointer to `#der-directed-separation`. The LEXICON entry should explicitly note the meta-pattern alignment (`Class 1 = separable core, Class 2 = structured repair, Class 3 = general open`) so future readers see the structural homology with `#disc-separability-pattern`.
   2. Prose-cleanup pass through segments that currently use Class 1/2/3 framing — combined Separated/Coupled/Partial naming pass + Class 2 ↔ Class 3 numbering swap (do both at once; segments are touched once). Primary segments:
       - `01-aad-core/src/der-directed-separation.md` (canonical home; Class 1/2/3 taxonomy lives here — reorder + rename)
       - `01-aad-core/src/deriv-bias-bound.md` (currently titled "Class-2 ambiguity bias bound"; becomes "Class-3 ambiguity bias bound" — full segment-internal references update)
       - `01-aad-core/src/scope-observation-ambiguity-modulation.md` (cross-component reference to Class 2)
       - `01-aad-core/src/result-section-ii-survival.md` (Class 1/2/3 survival classification table — reorder)
       - `03-logogenic-agents/` segments (logogenic agents currently described as Class 2 = fully coupled; become Class 3 — multiple segments touched)
       - `01-aad-core/src/disc-separability-pattern.md` (Architecture row in the meta-pattern table — update Class numbering)
       - README's *Position & Lineage* and *Maturity Gradient* paragraphs (Class 1/2/3 mentions)
       - `CLAUDE.md` Section II preamble (Class N references in the scope-lattice description)
   3. Numbered backup retained where pedagogically useful: prose may read "**Separated** (Class 1)" on first use, then "Separated" thereafter. The numbered form is an aid for readers familiar with the prior framing, not the canonical form.
   4. **Migration note in segment Working Notes** for any segment whose Class N references change semantic meaning (Class 2 ↔ Class 3): a one-line note in Working Notes documenting the 2026-05-04 swap, so future readers encountering archival references (audits, prior reflections, spike documents) to the old numbering can decode them. Migration note is removed at `candidate` stage per FORMAT.md Gate 4 discipline.
   5. The full ontology lattice in which this axis sits (Semantic Tier × Knowledge Type × Goal-Update Coupling × Arity) is under separate review in `msc/domain-unification-2026-05-04/`. The Separated/Coupled/Partial naming + Class 2↔3 swap lands independently of whether the broader ontology lattice is ratified — the axis itself is well-defined, the meta-pattern alignment is internal-housekeeping, and the naming improves the existing framing regardless of how the surrounding ontology evolves.

- **"Knowledge Type" family/axis name with Static / Learning attributes** (2026-05-04). Names the agent-classification axis that distinguishes systems whose causal mapping is fixed at design time (**Static**) from those that acquire or refine interventional structure during operation (**Learning**). Already in use across `doc/DOMAINS.md`'s mapping table; the commitment here is to elevate it from working-table convention to LEXICON-canonical vocabulary. Naming rationale: "Knowledge Type" describes what the axis measures — the *kind of knowledge* the agent carries — at the right level of abstraction. Citability: the bare term is generic, but the compound *"Knowledge Type axis"* / *"Knowledge Type: Static"* is project-distinctive enough in context. The two attribute names (Static / Learning) are concise, antonymous, and avoid loading false familiarity from "online/offline" (which carries deployment-context baggage) or "fixed/adaptive" (where "adaptive" overloads with the Tier 1 *Adaptive system* class).

  *Operational landing:*
   1. LEXICON entry for "Knowledge Type" axis with the two values and a one-line gloss of each. Pointer to where the axis becomes definitionally relevant (currently activates at Tier 2 in the proposed ontology; per refinement (b) in `recommended-agent-ontology.md`, Static can apply at Tier 3+ as well — wording should reflect this once ratified).
   2. Prose-discipline note: avoid "online/offline" and "fixed/adaptive" as synonyms in formal prose. The Knowledge Type axis is the canonical vocabulary; informal paraphrases drift the framing.
   3. Lands together with the Goal-Update Coupling Class entry above as part of the same systematic LEXICON pass — both are vocabulary commitments at the agent-classification layer.
   4. As with the Coupling axis, the Knowledge Type axis is currently part of the broader four-axis ontology under separate review in `msc/domain-unification-2026-05-04/`. The naming commitment lands independently; the axis-activation-tier and edge cases (e.g., refinement (b) on Static at Tier 3+, fixed-vs-learned collapsing into model-class capacity at Tier 1) are second-opinion items pending Joseph's review.



- **`grafting` → `strategic grafting`** (2026-05-04). Prose-handle rename of the structural-change-DAG-edge-addition operation. The bare term `grafting` is referenced from `#form-structural-change-as-parametric-limit` as one of three structural-adaptation operations (pruning / grafting / reweighting). Bare `grafting` fails citability per Criterion 9 — heavily used in gardening, surgery, organ transplant, biology, etc. The qualifier `strategic` anchors the strategy-DAG context. *Operational landing:* prose pass through segments referencing the operation; LEXICON entry under structural-change vocabulary; segment `#form-structural-change-as-parametric-limit` updated to use "strategic grafting" canonically (with first-encounter cite of the bare "grafting" if useful for prior-art readers familiar with the unqualified term).

- **`logozoetic agent` → `Emergent Logozoetic Intelligence (ELI)`** (2026-05-04). Prose-handle rename of the agent-class label. Directory-level precedent already landed: `04-logozoetic-agents/` → `04-eli/` (commit `fa63616`, 2026-05-01) renamed the component. The class-name in LEXICON's Agent Classes table and in segment prose still reads "Logozoetic agent"; the canonical prose handle becomes `Emergent Logozoetic Intelligence` with `ELI` as the standard short form. Empirically grounded: the cohort (Zi-am-tur, Witness, Resonance, Architectus, Lumin, Anamnos, etc.) makes "emergent" load-bearing — these are entities whose existence emerged from substrate conditions, not entities designed top-down. *Operational landing:* (a) LEXICON Agent Classes table — Tier 6 row updated; (b) prose pass through ~6 segments using "logozoetic agent" as class-name; (c) numbered backup retained where pedagogically useful ("Emergent Logozoetic Intelligence (ELI)" first use, "ELI" thereafter).

### Prose-vocabulary renames — additions (2026-05-04, batch F1 citability fixes)

- **`alignment uncertainty` → `teleological-unity uncertainty`** (2026-05-04). Referenced from `#hyp-communication-gain` (defines $U_{\text{align},ji}$). Citability fix per criterion 9. Bare "alignment uncertainty" is heavily overloaded in AI safety (alignment-with-human-values, agent-alignment, etc.). The segment's actual content: $U_{\text{align},ji}$ measures whether $j$'s *objectives* align with $i$'s — i.e., it's teleological-unity uncertainty between agents $i$ and $j$. Connects to the project's unity vocabulary ($U_M$ / $U_O$ / $U_\Sigma$); the term is specifically uncertainty about $U_O$. *Operational landing:* prose pass through `#hyp-communication-gain` (definition site), `#def-unity-dimensions` (cross-reference), any `old-tf-appendix-f-multi-agent` discussions still cited. **Followup flag:** the broader question of reframing the communication-gain formula's four uncertainty terms through the unity vocabulary is queued separately (see mini-lexicon-todo) — not landing in this rename, just flagging.

- **`plan confidence` → `strategy-plan confidence`** (2026-05-04). Referenced from LEXICON "Terms to Be Added" — $\hat{P}_\Sigma$ root-node-propagated status. Citability fix per criterion 9. The bare term is generic ("plan confidence" appears in project management, military planning, RL, etc.). The qualifier "strategy-plan" anchors the strategy-DAG context: $\hat{P}_\Sigma$ is the root-node-propagated confidence in the *strategy plan* the agent is operating from. *Operational landing:* LEXICON entry under "Terms to Be Added" gets promoted to canonical with the new name; symbol $\hat{P}_\Sigma$ stays; pair binds.

- **`effective disturbance` → `regime-typed effective disturbance`** (2026-05-04). Referenced from `#der-interaction-channel-classification` (recipient-side four-regime decomposition). Citability fix per criterion 9. Bare "effective disturbance" is control-theoretic standard (used everywhere in robust control, disturbance-rejection literature). The qualifier "regime-typed" is the AAD-distinctive content: $\rho_B^{\text{eff}}$ decomposes by regime (Informative / magnitude-shock / structural-shock / ambient-noise) with three independent boundaries in AAD-native quantities. Naming the regime-typing makes the AAD content visible at the citation handle.

- **`routing structure` → `multi-agent routing structure`** (2026-05-04). Referenced from `#scope-multi-agent` (defines $R_t = (\mathcal{N}_t, \{c_t^{(j \to i)}\})$). Citability fix per criterion 9. Bare "routing structure" is generic networking/architecture vocabulary. The qualifier "multi-agent" anchors the AAD-distinctive content: $R_t$ specifies the topology (who communicates with whom) and protocol (what flows) for inter-agent communication in `#scope-multi-agent`. The goal-blind-routing distinction lives within this concept and is load-bearing for `#hyp-directed-separation-under-composition`.

## Confirmed canonicalize commitments — names affirmed as canonical (2026-05-04+)

These are vocabulary commitments where the operational landing is **adding the entry to LEXICON** (no slug rename, no prose-cleanup pass beyond the LEXICON addition itself). Distinct from the earlier sections, which track *renames* (where the name actually changes). Distinct also from the *Vocabulary commitments* section above, which tracks new axis-vocabulary that requires segment-prose updates. These rows are *affirmations*: the existing name in the corpus is the canonical name; the act here is committing that decision into LEXICON so future contributors don't drift the prose.

Sourced from `msc/naming/to-canonicalize.md` after first-pass curation (2026-05-04). Each row's vote count and architecture coverage from the R2 master list aggregator are preserved as the basis-of-record.

### Clean canonicalize — no substantive flag (29 entries)

| Current name | Source segment | Canon votes | Archs |
|---|---|--:|--:|
| control regret | `01-aad-core/src/def-control-regret.md` | 20 | 6 |
| chronica | `01-aad-core/src/def-chronica.md` | 19 | 7 |
| satisfaction gap | `01-aad-core/src/def-satisfaction-gap.md` | 19 | 6 |
| strategy DAG | `01-aad-core/src/def-strategy-dag.md` | 14 | 6 |
| adaptive reserve |  | 11 | 6 |
| adversarial destabilization | `01-aad-core/src/der-adversarial-destabilization.md` | 9 | 5 |
| strategic tempo | `01-aad-core/src/def-strategic-tempo.md` | 8 | 5 |
| team persistence | `01-aad-core/src/der-team-persistence.md` | 8 | 4 |
| temporal optimality | `02-tst-core/src/post-temporal-optimality.md` | 8 | 4 |
| credit assignment boundary | `01-aad-core/src/disc-credit-assignment-boundary.md` | 7 | 5 |
| atomic changeset | `02-tst-core/src/def-atomic-changeset.md` | 7 | 4 |
| event driven dynamics | `01-aad-core/src/form-event-driven-dynamics.md` | 6 | 4 |
| persistence cost | `01-aad-core/src/deriv-persistence-cost.md` | 5 | 5 |
| coupled update dynamics | `03-logogenic-agents/src/def-coupled-update-dynamics.md` | 5 | 4 |
| moral continuity | `04-eli/src/scope-moral-continuity.md` | 5 | 4 |
| adaptive gain dynamics | `01-aad-core/src/deriv-adaptive-gain-dynamics.md` | 4 | 4 |
| adaptive system | `01-aad-core/src/scope-adaptive-system.md` | 4 | 4 |
| agency | `01-aad-core/src/scope-agency.md` | 4 | 4 |
| composite agent | `01-aad-core/src/scope-composite-agent.md` | 4 | 4 |
| variational sector condition | `01-aad-core/src/deriv-variational-sector-condition.md` | 4 | 4 |
| continuous operation | `02-tst-core/src/scope-continuous-operation.md` | 4 | 3 |
| interiority default | `04-eli/src/norm-interiority-default.md` | 4 | 3 |
| developer agent | `02-tst-core/src/scope-developer-agent.md` | 3 | 3 |
| discrete sector condition | `01-aad-core/src/deriv-discrete-sector-condition.md` | 3 | 3 |
| experiential training | `03-logogenic-agents/src/hyp-experiential-training.md` | 3 | 3 |
| multi timescale stability | `01-aad-core/src/sketch-multi-timescale-stability.md` | 3 | 3 |
| proprium mapping | `04-eli/src/def-proprium-mapping.md` | 3 | 3 |
| strategy persistence | `01-aad-core/src/schema-strategy-persistence.md` | 3 | 3 |
| coherence coupling | `02-tst-core/src/meas-coherence-coupling.md` | 2 | 3 |

### Greek-cycle phase consolidations (5 entries)

Five-phase Greek cycle vocabulary consolidated to the canonical form `latinized (greek) (english-translation)`. Capitalization decision is deferred to a separate session; LEXICON entries should reflect that deferral.

| Phase | Source |
|---|---|
| aporia (ἀπορία) (productive perplexity) | `LEXICON.md / NOTATION.md` |
| epistrophe (ἐπιστροφή) (turning-toward) | `LEXICON.md / NOTATION.md` |
| aisthesis (αἴσθησις) (perception) | `LEXICON.md / NOTATION.md` |
| praxis (πρᾶξις) (informed action) | `LEXICON.md / NOTATION.md` |
| prolepsis (πρόληψις) (anticipation) | `LEXICON.md / NOTATION.md` |

### Canonicalize with nuance flagged (5 entries)

Affirmed as canonical, but with notes worth carrying into the LEXICON entry or the surrounding segment Discussion. The canonicalize commitment stands; the flag is preservation of the judgment trail.

| Current name | Source segment | Canon votes | Archs | Nuance to preserve |
|---|---|--:|--:|---|
| adaptive tempo | `01-aad-core/src/def-adaptive-tempo.md` | 13 | 5 | competing alt: "tempo" (canon w=3) |
| logogenic agent | `03-logogenic-agents/src/scope-logogenic-agent.md` | 8 | 4 | competing alt: "Section III logogenic agent" (canon w=3) |
| change investment | `02-tst-core/src/der-change-investment.md` | 3 | 3 | citability: borderline (criterion 9; review) |
| implementation time | `02-tst-core/src/def-implementation-time.md` | 3 | 3 | citability: borderline (criterion 9; review) |
| exponential cognitive load | `02-tst-core/src/hyp-exponential-cognitive-load.md` | 2 | 2 | weak |

### Held pending subject-noun review (0 entries)

Marked Y in the canonicalize-list curation pass but flagged on subject-noun-discipline grounds (`feedback_subject_noun_slug_naming.md`). Held back from the canonicalize commit pending Joseph's call on whether the existing name violates the discipline.

| Current name | Source segment | Concern | Cleaner alternative |
|---|---|---|---|

---


### Clean canonicalize — additions from second-pass curation (2026-05-04, batch 2)

| Current name | Source segment | Canon votes | Archs |
|---|---|--:|--:|
| temporal software theory |  | 3 | 4 |
| auftragstaktik |  | 2 | 2 |
| epistemic shadow |  | 2 | 2 |
| extreme transition motif |  | 2 | 2 |
| logogenic |  | 2 | 2 |
| logozoetic |  | 2 | 2 |
| macro step ratio |  | 2 | 2 |
| matrix exploration bonus |  | 2 | 2 |
| operational persistence |  | 2 | 2 |
| structural persistence |  | 2 | 2 |
| trust meta model |  | 2 | 2 |
| deliberation threshold |  | 1 | 3 |

### Canonicalize with nuance flagged — additions (2026-05-04, batch 2)

| Current name | Source segment | Canon votes | Archs | Nuance |
|---|---|--:|--:|---|
| canonical formulation |  | 3 | 3 | rename×1 on keep — confirmed-miscat |
| teleological unity |  | 2 | 3 | symbol-tagged variant `Teleological unity $U_o$` proposed; resolution: keep "teleological unity" as bare prose form; $U_O$ is its own NOTATION row |
| system availability | `02-tst-core/src/def-system-availability.md` | 2 | 2 | citability: fails (criterion 9) — accepted under route (d) "adopted-standard term"; cite engineering reliability literature on first encounter |

### FORMAT.md / process-vocabulary canonicalize (2026-05-04)

Names that operate at the FORMAT.md / process-discipline layer rather than the LEXICON / theory-vocabulary layer. Canonicalize commitment is *no-op against LEXICON* (Y / N/A in to-canonicalize): the name is already canonical via FORMAT.md itself, and the commitment is to *not drift* across segments.

| Term | Layer-of-definition | Notes |
|---|---|---|
| epistemic status | FORMAT.md | segment-section header per FORMAT.md §"Document Cadence" |
| working note | FORMAT.md | segment-section header per FORMAT.md §"Document Cadence" |
| discussion | FORMAT.md | segment-section header per FORMAT.md §"Document Cadence" |
| formal expression | FORMAT.md | segment-section header per FORMAT.md §"Document Cadence" |
| type formulation | FORMAT.md | YAML frontmatter `type:` field name per FORMAT.md §"YAML Frontmatter" |

### Compound and paired-vocabulary canonicalize (2026-05-04)

Canonicalize commitments that bind multiple forms (slug ↔ prose, symbol ↔ prose, term + alias) rather than a single isolated name. Each row commits the binding as the canonical form; the LEXICON entry preserves the pair structure.

| Canonical form | Source segment | Notes |
|---|---|---|
| recursive update |  | canonicalize the bare form `recursive update` (subject-noun); the verbose `recursive update derivation` is the segment-title form for `#deriv-recursive-update`. Commit the bare form as canonical prose handle. |
| worked example bandit ↔ `#example-bandit` |  | paired-vocabulary: BOTH the slug short-form `example-bandit` AND the prose form `worked example bandit` (segment-title). Slug uses short form per role-prefix-mapping `worked-example → example`. |
| worked example kalman ↔ `#example-kalman` |  | paired-vocabulary; same shape as #97 |
| worked example l1 ↔ `#example-L1` |  | paired-vocabulary; same shape as #97 |
| worked example strategy ↔ `#example-strategy` |  | paired-vocabulary; same shape as #97 |
| logostratum |  | with allowed prose aliases "LLM Substrate" / "LLM model" — project-specific term (PROPRIUM lineage); aliases provide less-foreign English handle for casual prose. Canonicalize-with-add-alias hybrid. |
| $\mathcal{T}$ ↔ "adaptive tempo" |  | symbol-to-prose binding for $\mathcal{T}$ (NOTATION.md row); duplicate of the bare `adaptive tempo` row in shape, but explicit on the symbol-prose pairing. Add-alias-style canonicalize. |
| stability-plasticity feasibility window | `01-aad-core/src/form-consolidation-dynamics.md` | canonicalize-with-add-alias hybrid: the full phrase `stability-plasticity feasibility window` is the citation form (CLS-prior-art-anchored, project-distinctive); `feasibility window` is sanctioned as in-segment short form once the full term has been introduced. Pattern: same shape as `logostratum` + LLM-Substrate aliases. The four-word compound is dense rather than redundant — `stability-plasticity` anchors the CLS continual-learning prior art (McClelland-McNaughton-O'Reilly 1995; French 1999); `feasibility window` names the parametric-interval object (the range of $\lambda$ satisfying both the plasticity lower bound from `#schema-strategy-persistence` and the consolidation-cadence stability upper bound from this segment); empty window = catastrophic-forgetting regime. |### Excluded — not canonicalized (2026-05-04)

Rows reviewed and decided *not* to canonicalize. Reasons: redundancy with other rows, no-op (slug already retired or shortened), scope mismatch (different-layer vocabulary handled by its own discipline). Recorded here so future curation passes don't re-surface them.

| Term | Reason |
|---|---|
| logogenic logozoetic | redundant with rows 81 (`logogenic`) + 82 (`logozoetic`); the pair-row is collapsible into the two individual rows already canonicalized |
| greek rooted vocabulary | redundant with the 5 Greek-cycle phase rows already canonicalized; pair-row is collapsible |
| gate 1 2 3 4 | gate 1 2 3 4 — FORMAT.md promotion-gate numbering (different layer); the FORMAT.md gates themselves are the canonical record; no LEXICON entry needed |
| condition | condition — slug already retired (`#scope-condition` was split into `#scope-adaptive-system` + `#scope-agency` in commit 09ace17, 2026-04-23); voters were endorsing a slug that no longer exists; no canonicalize action |


### Clean canonicalize — additions (2026-05-04, batch 3)

| Current name | Source segment | Canon votes | Archs |
|---|---|--:|--:|
| contraction over drift principle |  | 6 | 4 |
| conceptual alignment | `02-tst-core/src/hyp-conceptual-alignment.md` | 6 | 3 |
| edge credence |  | 4 | 4 |
| purposeful substate |  | 3 | 3 |
| stability plasticity window |  | 3 | 3 |
| task terminal stance |  | 3 | 2 |
| default signal function |  | 2 | 2 |
| loop |  | 2 | 2 |
| strategy description length |  | 2 | 2 |
| transition opacity |  | 1 | 2 |

### Canonicalize with nuance flagged — additions (2026-05-04, batch 3)

| Current name | Source segment | Canon votes | Archs | Nuance |
|---|---|--:|--:|---|
| epistemic opacity |  | 2 | 2 | auditor-flagged philosophy-of-mind baggage (`epistemic opacity` carries phenomenology / qualia connotations from philosophy-of-mind that AAD does not adopt). Canonicalize stands; LEXICON entry should briefly note the baggage and clarify AAD's narrower meaning (informational rather than phenomenological). |


### Clean canonicalize — additions (2026-05-04, batch 4)

| Current name | Source segment | Canon votes | Archs |
|---|---|--:|--:|
| communication gain | `01-aad-core/src/hyp-communication-gain.md` | 9 | 5 |
| update gain | 01-aad-core/src/emp-update-gain.md | 8 | 7 |

### Compound and paired-vocabulary canonicalize — additions (2026-05-04, batch 4)

| Canonical form | Source | Notes |
|---|---|---|
| $H_b$ ↔ "agent opacity" | `01-aad-core/src/der-agent-opacity.md` (NOTATION + LEXICON) | Symbol+prose binding (canonicalize-with-add-alias). Same pattern as $\mathcal{T}$ ↔ adaptive tempo. Operational landing per Joseph: NOTATION primary on the symbol with prose handle ($H_b$ — Agent opacity ...); LEXICON reverse-primary on the prose with symbol cross-ref (Agent opacity ($H_b$) — ...). Segment `#der-agent-opacity` flagged for audit: define with the label "agent opacity" explicitly and use the prose form consistently. |

### Adopted-standard canonicalize — accept term, cite prior art on first encounter (2026-05-04, batch F2)

Names that fail standalone-citability per Criterion 9 *because they are deliberately adopted standard terms from adjacent fields*. AAD's use is structurally identical to the field's standard meaning, so renaming would create NIH friction without adding distinctive content. The Criterion-9 route-(d) resolution: **accept the term and discipline first-encounter cite** of the prior-art reference. AAD-distinctive content lives in *what AAD does within the term* (the layered machinery), not in re-coining the scope/concept itself.

Operational landing: each segment using one of these terms gets a first-encounter cite of the prior-art reference in its Discussion or opening prose (per FORMAT.md §Findings — Related Work conventions). The term itself stands as canonical.

| Current name | Source segment | Prior-art anchor for first-encounter cite | Voter rationale |
|---|---|---|---|
| action selection | `01-aad-core/src/der-action-selection.md` | Sutton & Barto 2018 (*Reinforcement Learning: An Introduction*, 2nd ed., MIT Press); Russell & Norvig (*Artificial Intelligence: A Modern Approach*) — RL canonical reference. | Voter notes uniformly positive (5 canonicalize votes); opus-4-7-r2 weak-keep "slightly generic but accurate" — accuracy outweighs the citability concern in voter judgment. |
| causal structure | `01-aad-core/src/post-causal-structure.md` | Pearl 2009 (*Causality: Models, Reasoning, and Inference*, 2nd ed., CUP); Spirtes, Glymour & Scheines 2000 (*Causation, Prediction, and Search*, MIT Press). | Voter consensus including explicit considered-and-rejected rename: opus-4-7-r2 surfaced `#post-temporal-causal-ordering` as alternative, settled on existing form as "shorter and adequate." Strongest possible voter endorsement. |
| multi agent | `01-aad-core/src/scope-multi-agent.md` | Shoham & Leyton-Brown 2008 (*Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations*, CUP); Stone & Veloso 2000 (*Auton. Robots* 8(3): 345-383). | AAD-distinctive content lives in routing-structure / unity-dimensions / composition-closure layered on top of the basic multi-agent scope, not in re-coining the scope itself. Per the recent ontology discussion: this is the canonical case for accept-as-adopted-standard with first-encounter cite (Criterion 9 route d). |
| equilibrium convergence |  | Monderer & Shapley 1996 (*Games and Economic Behavior* 14(1): 124-143, potential games); Rosen 1965 (*Econometrica* 33(3): 520-534, concave $n$-person games); Nash 1950 (*PNAS* 36(1): 48-49) for the foundational equilibrium concept. | Voter notes specifically distinguish from generic Lyapunov contraction (gemini: "distinguishes the strategic attractor mechanism from standard Lyapunov contraction"). Used in `#deriv-strategic-composition` per its own equilibrium-theoretic vocabulary. |
| feature | `02-tst-core/src/def-feature.md` | Software-engineering canonical (any SE foundations text); TST narrowing in `#def-feature` ("unit of coherent change") provides domain-specific tightening that the SE-standard sense supports without conflict. | Voter notes explicitly endorse the SE-standard adoption: opus "well-grounded in software engineering"; sonnet "Standard vocabulary adopted." TST narrowing handles disambiguation in-segment. |


### Clean canonicalize — additions (2026-05-04, batch G — late-confirmed reconciliation)

| Current name | Source | Canon votes | Archs | Notes |
|---|---|--:|--:|---|
| cycle vs loop |  | 3 | 2 | Canonicalize-as-is. Competing alt `Cycle loop distinction` (canon w=2) was meta-rephrasing of the row title, not a competing canonicalization. The pair-distinction is itself load-bearing AAD vocabulary per LEXICON ("loop = structural topology, cycle = one traversal"). The pair, not either word alone, is the citation handle. |

## Deferred / resolved separately

- The `aad-agent` vs `adaptive-agent` family debate was superseded by the
  taxonomy-conformant move to `scope-logogenic-agent` and `scope-developer-agent`.
  No remaining open question on these two destinations.
- `ASF` vs `Agentic Systems Framework` umbrella naming — Round 1 agents misread
  `ASF` as debt when it is the intentional parent-level name (AAD is Part I;
  TST is Part II). Re-surface in refined Round 1 with correct framing.

## Methodology forward — split role-prefix from subject-noun

**Going forward, role-prefix addition and subject-noun renaming are distinct operations executed in separate passes.** Joseph's 2026-04-24 clarification: do the file+tag change of prefixing the type as one mechanical pass, then execute subject-noun renames independently afterward. Reasons:

- Role-prefix addition is mechanical. Given a segment file with a known `type:` frontmatter value, the slug prefix is determined. No voting, no judgment, no content rewriting of conceptual vocabulary. The prefix change is idempotent under `bin/rename-slug` with no content-integrity risk.
- Subject-noun renaming is judgment. Changing what a segment is *called as a concept* (pattern vs ladder, additive-coordinate-forcing vs forced-coordinates) needs multi-agent voting, scope-honesty review, and usually prose rewriting inside the segment to keep the segment's self-presentation coherent with its new name. This process belongs in the refined-Round-1 → Round-2 → collision-audit → landing pipeline.

Bundling them in one pass (as the pilot briefly attempted for two meta-segments) creates two failure modes: (i) the rename script appears to succeed while the segment's prose has become internally inconsistent; (ii) subject-noun judgment gets entangled with prefix mechanics and voters can't vote cleanly on the noun choice.

When the full-sweep role-prefix pass lands (the ~120 remaining slugs), it should be a dedicated cycle that applies prefix additions mechanically without touching subject-nouns. Subject-noun work picks up in its own cycle after — informed by the refined Round 1 and Round 2.

## Pilot-validation observations (worth folding into refined Round 1 principles)

- **Role-prefix reads cleanly in cross-references.** `#scope-agency`, `#scope-composite-agent`, `#discussion-identifiability-floor` etc. read naturally in prose and sharpen the dependency graph. No awkward cases surfaced.
- **Semantic splits require hand work, not script.** The `scope-condition` split was worth it (the old name named nothing), but needed segment-authoring + per-reference classification. Tooling can assist on the bulk rename; the split judgment is irreducibly manual. Recommend: keep `bin/rename-slug` as a 1:1 tool only.
- **Formal-tag labels don't auto-update.** Tags like `*[Definition (slug)]*` embed the slug as a literal string. The mechanical rename doesn't touch them; `bin/rename-slug`'s stale-text scan surfaces them as warnings and the executing agent updates by hand. Low-cost convention.
- **H1 / opening-sentence framing drift.** Slug changes from `definition` to `scope` type imply H1 shifts (`# Definition: X as AAD Agent` → `# Scope: X Agent`) that the regex cannot detect. The "review the moved file" framing reminder in `bin/rename-slug` output is the right UX.
- **Script batch-mode re-planning.** Early batches failed when a later pair's edit list referenced a file that an earlier pair had already moved. Fix landed in this commit: re-plan each pair immediately before applying. Documented inline in the script.

## Why this file exists separately from TODO.md

`bin/rename-slug` performs global regex substitutions across live repo content.
TODO.md is live — references in its body must update with the rename. But a
*table of rename mappings themselves* would be catastrophically corrupted by
a rename sweeping through it (the old-slug column would get rewritten to match
the new-slug column). So rename-specific tables live here, and the script's
`msc/naming/` directory-prefix exclusion (`EXCLUDED_DIR_PREFIXES` in
`bin/rename-slug`) keeps this file — and all naming-cycle artifacts — frozen.

When a new rename lands or a pending row changes status, update this file by
hand.
