# TODO — Miscellaneous & details

**Last reconciled:** 2026-04-28 (TODO reimagined as the misc-and-details layer; ~180 lines of cycle-aftermath spike status moved to [`spikes/INDEX.md`](spikes/INDEX.md); resolved audit-findings tables collapsed; ~78 lines of historical "Recommendations for next session" dropped; §Archive collapsed; Naming Discipline section compressed to specific deferred items only).

This file holds the *miscellaneous* layer of project work — open routing decisions whose call belongs to Joseph, multi-cycle queued work-packages, theory items that don't fit elsewhere, queued spike follow-ups, naming-pipeline-specific deferrals, standing editorial hygiene, and lower-priority specifics. The bulk of project work is *not* enumerated here; it lives in:

- [`PRACTICA.md`](PRACTICA.md) — strategic-portfolio navigator (top of the strategy DAG; areas of active work; auditor-safe).
- Component `OUTLINE.md` files — per-component canonical outline + GAPs. Run `bin/lint-outline` for current segment-stage distribution, ordering violations, missing dependencies, and orphans.
- [`PROPOSALS.md`](PROPOSALS.md) — architectural moves under review (banded by readiness; cross-cutting bundles named).
- [`spikes/INDEX.md`](spikes/INDEX.md) — spike index with per-spike status (per cycle).
- [`CHANGELOG.md`](CHANGELOG.md) (post-2026-04-24) and [`LOG.md`](LOG.md) (frozen pre-2026-04-24) — cycle narratives, what landed, and the *why* behind structural moves.
- `audits/pending-findings-YYYY-MM-DD.md` — original audit-finding characterizations and resolution trails.

**Terminology note.** "Audit-findings" are the F#/F-V# items surfaced by audit cycles. "Findings" without the prefix means the catalog of ASF discoveries (see [`FINDINGS.md`](FINDINGS.md) and segment-level `## Findings` sections).


## Greek vocabulary prose discipline (audit + author finding, 2026-04-29)

The de-novo audit-471203, walking the formalism segment-by-segment, surfaced that the project's Greek cycle vocabulary (*chronica* / *prolepsis* / *aisthesis* / *aporia* / *epistrophe* / *praxis*) shows up at framing/preamble/lexicon levels but the segment-level math doesn't depend on the distinctions the Greek terms encode. The README claim that "each [Greek term] names a distinction the formalism makes that English alternatives flatten" is overclaimed against current segment prose, where authors routinely fall back to flatter English equivalents (e.g., saying "mismatch" right after defining `aporia` as something specifically richer than mismatch).

Author confirmed independently: *"I've had that exact same complaint actually — that some of the higher level concepts that are important haven't been reinforced in the segments. Like every time we say 'mismatch' after specifically saying that this is much more than just mismatch."*

Cross-architecture deliberate naming-round voters (R1 + R2 cold-start + reactive) near-unanimously *defended* the Greek terms as load-bearing — but they were voting synoptically on whether the names *feel* right in the lexicon. The audit's incremental-mental-model walk surfaced what the synoptic glance was structurally blind to: whether the formalism *requires* the distinctions in actual segment-prose use.

This is not a naming-round vote. It is a project-level prose-discipline pass. Two paths, not mutually exclusive:

- **Tighten segment prose so the Greek distinctions actually do work.** Where the load-bearing content is the thing the Greek term names (not the flatter English equivalent), the Greek term becomes the canonical form in that segment's prose: *mismatch → aporia* where the productive-perplexity-resolves-into-action structure is what's structurally distinctive; *update → epistrophe* where the turning-toward-correction is what's load-bearing; etc. Per-term, per-segment judgment.
- **Soften the README's framing to honest scope** for any term where path 1 doesn't apply (i.e., the formalism really does only use the Greek as pedagogical surface vocabulary). The README's claim narrows accordingly.

Recommended cycle scope: a dedicated prose-audit pass across `01-aad-core/src/` segments that touch the cycle phases or the chronica/aporia vocabulary; produces a delta-list of Greek-vs-English collapses; each entry either gets a prose fix (enforcing Greek where the segment's load-bearing content matches the Greek's distinction) or feeds back as a downgrade-note for the LEXICON entry and the README claim.

Sources:
- Audit's full findings: [`msc/naming/naming-votes/audit-471203-incremental.md`](msc/naming/naming-votes/audit-471203-incremental.md) (segments 1–46 only as of 2026-04-28; will be re-extracted after audit FINAL lands).
- Aggregator's cross-architecture +3 keep votes for Greek terms (illustrating the defended-by-synoptic-voters posture): [`msc/naming/naming-aggregate-r2-review.md`](msc/naming/naming-aggregate-r2-review.md).


## README v2 pass (queued from 2026-04-27 first-human-feedback cycle)

The first *human* read of the framework — Alan Walton (CTO Latitude / AI Dungeon; BS Mathematics + Logic minor; ~10y collaboration history with Joseph; runs a 12k-commit production agentic-system architecture), ~4h read window — surfaced that the README missed the mark for casual-curious readers in ways the multi-agent audit cycles had not. Even Alan, who is about as sympathetic and capable a first-human-reviewer as the project will encounter, found the language "extremely academic," fell out of sustained-attention reading by the end of the README, and switched to test-driven Opus-mediated learning to keep engaged. (Verbatim review pending — Alan is still actively adding to it and will land it as a PR under `msc/` when ready.)

The README needs another pass that combines this human-feedback signal with the deferrals from the 2026-04-26 doc-pipeline cycle (judgment-calls log at `msc/judgment-calls-readme-cycle-2026-04-26.md`).

### Surfaced from Alan's review

- **Variables α, ρ, R appear without gloss.** Alan: *"I've seen this formula twice now, but still don't know what the variables mean."* First mention of the persistence condition should anchor each variable in plain language; the *Cross-Domain Joining* table (which uses α, ρ, R without re-glossing) and the *Position & Lineage* paragraph (which mentions α > ρ/R as a structural threshold) should both re-anchor briefly. Glossing once at top is not enough across a long document.
- **The "rate of gap-closing proportional to gap" assumption is not surfaced at README level.** Alan correctly identified this as the load-bearing assumption from outside: *"That's the weakest assumption I've seen so far in application, though it's often empirically true."* The README should foreground the linear-ODE / sector-condition assumption explicitly, with one line on how the sector condition generalizes strict linearity (it's the structural assumption AAD spends Section I machinery on, not an embarrassment to bury).
- **Greek cycle terms have retention cost without an English on-ramp.** Alan retrieved the cycle's semantics under his own terms (Prediction / Perception / Comparison / Learning / Action) but none of the Greek (Prolepsis / Aisthesis / Aporia / Epistrophe / Praxis). Decision: keep the Greek (the distinctions matter and English flattens them), *and* pair each with a clean memorable English/engineering anchor at first introduction. Alan's five-word recall is itself a candidate mapping; whether it preserves the distinctions the Greek encodes is worth a careful pass.
- **The About / Position-and-Lineage opening is too clinical for the audience it was written for.** This is the single biggest miss. Bundle 1 framework-face reframe is partially landed; another pass is warranted, this time with the casual-curious tier (not the academic-evaluator tier) as the primary audience. Alan's bathtub gloss of the persistence condition (water = belief-reality gap; faucet = environment change rate; drain = learning rate; bathtub size = model class capacity; overflow when faucet outpaces drain at full) is a ready-made Feynman-criterion explanation that a mathematician-practitioner reconstructed for himself — worth promoting verbatim or near-verbatim into both the README's persistence section and `#result-persistence-condition`'s Findings Brief.
- **Units of α are not visible.** Alan: *"The drain is bits/bits/time or 1/time. I'm not used to thinking of inverse time as units."* Worth a units gloss somewhere — possibly NOTATION.md (canonical), possibly in the README's persistence-condition section (pedagogical), possibly both. (Discussion of where this lives queued for after this TODO entry lands.)
- **Prior-art pointer to investigate: Deutsch's Theory of Explanations.** Alan: *"Have you read The Beginning of Infinity and The Fabric of Reality by David Deutsch? The Theory of Explanations is highly aligned with this work."* Substantive pointer worth a search-log-grade investigation; if confirmed, cite as conceptual precursor / adjacent literature in the relevant Findings (most likely `#disc-additive-coordinate-forcing` or `#disc-identifiability-floor`, given the explanation-quality framing).
- **Consider promoting Alan's "split goal state and model state explicitly in agent context notes" as a TST or logogenic-agents instantiation.** Alan's instinct from running production AI Dungeon agents was the same decomposition the framework names as $G_t = (O_t, \Sigma_t)$ vs $M_t$. This is field-grade convergent-independent confirmation of the central decomposition; worth surfacing as a `02-tst-core/` or `03-logogenic-agents/` instantiation.
- **Alan's testing-scaffolding hierarchy as engineering-applications anchor.** From his Engineering Applications notes: *Types > Checks > Automated Tests > Manual Tests > Agent Tests > Context Docs* — a practitioner-graded ordering of what scaffolds the Pearl-Level-2 channel spectrum (`#obs-software-epistemic-properties` P3) for a production agentic system. Worth surfacing in `02-tst-core/` (operational instantiation of the channel-spectrum table) and possibly in the README's *Cross-Domain Joining* table as the engineer-side anchor. Alan's other anchor — *"Faster iteration loops that give more reliable and consistent results lead to better accuracy and faster convergence"* — is the folk version of the tempo / persistence-condition story; its phrasing is itself a practitioner-grade Feynman-criterion gloss for the README.

### Deferrals from 2026-04-26 doc-pipeline cycle (`msc/judgment-calls-readme-cycle-2026-04-26.md`)

Reconsiderations Joseph flagged for review on return; this README v2 pass is the natural cycle to ledger them through.

- **J-1 — pilot Findings selection.** The six-segment Findings pilot skews toward post-2026-04-22 landings; substituting one or more older "convergent choice" results (e.g., `#der-loop-interventional-access` for the Pearl-hierarchy connection; `#result-sector-condition-stability` for the underlying Lyapunov result) would validate the schema across a wider age range before the sweep.
- **J-2 — Findings schema length.** Some Impact paragraphs (notably `#deriv-bias-bound`, `#result-contraction-template`) ran long; consider a length cap or splitting Impact into two beats (what-it-closes / what-it-unlocks).
- **J-4 — README §4 omissions.** Three of seven elements from the epistemic-architecture enumeration (originally in CLAUDE-2 §7; now distributed across `msc/FINDINGS-RANKED-DRAFT.md` M-section + #12 calibration-lab + segment-level Findings; CLAUDE-2 sunset 2026-04-28) were left at segment-level rather than README-level: agent-identity-as-token-level-commitment; derivation-audit tables; A2' sub-scope partition. Re-decide which belong at framing level given the casual-curious-reader retarget.
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


## Open routing decision: F8 / F-V3 — composite-agent C-iii

(C-iii) admits composites without explicit $O_c$, but `scope-composite-agent.md:79` says without $O_c$ the composite is "a fiction." Same audit-finding surfaced in the 2026-04-22 batch (F8) and the 2026-04-25 batch (F-V3). Two paths under Joseph's call:

- **Path A (recommended interim):** editorial fix in `scope-composite-agent.md` C-iii to make induced-$O_c$ structure explicit ($O_c$ derived from relevance variable $Y$ when C-iii holds). ~45–60 min. Compatible with later SP-21 if pursued.
- **Path B:** SP-21 architectural restructure (split the four C-routes into distinct composite ontologies). 4–6 sessions; reverses the deliberate 2026-04-22/23 unification choice. Currently *deferred* pending Bundle 2 (Section III completion) maturation. See [`PROPOSALS.md`](PROPOSALS.md) §G SP-21.


## Open theory items (MEDIUM)

Items where the question is well-framed but the work hasn't been done. Each is a candidate scoping spike or substantive derivation.

- **🌟 Composition admissibility ($\mathcal M_{\text{adm}}$) refactor — HIGH priority.** Section III's most load-bearing open problem. `msc/working-composition-admissibility.md` (473 lines, 2026-04-01) is an active workshop document carrying substantive worked content: the structural+stability direction with (A1)–(A4) framework; the bridge lemma "falls out of the sector condition for free" insight (one Lyapunov argument applied to two state variables, not two theorems); composite sector condition derivation cross-checked against team-persistence; toy two-linear-agent verification. The document is **load-bearing** — cited from `#form-composition-closure` and three spikes — but is explicitly a workshop, not a promoted artifact. **Work:** (a) decompose into proper spike files (candidates: `spike-composition-admissibility-structural-stability.md`; `spike-bridge-lemma-discrete-time-adaptation.md` for the discrete-time adaptation; `spike-composition-toy-purposeful-agents.md` for the richer Section II setting that exercises the $G_c$ axis); (b) promote stable findings into segments — most of §4–§6 is candidate Appendix-A material under or adjacent to `#form-composition-closure`; (c) update all references project-wide to point at the new spike files / segments rather than the workshop document; (d) follow-on spikes the workshop itself surfaced as genuinely open: discrete-time bridge lemma adaptation; richer purposeful-agent toy case exercising the $G_c$ component; projection admissibility ($\mathcal P_{\text{adm}}$, untouched in the workshop); norm-choice load-bearingness in real applications.

- **Composition scaling with $N$** — whether closure defect scales polynomially or exponentially with team size. Scoping spike done (`spikes/spike-composition-scaling-N.md`, 2026-04-22): four readings identified, five candidate first moves, two composing axes ($K_c$ macro-timescale; unity × update-heterogeneity). Question is well-framed but unresolved; execution deferred. Critical for large-team applications.
- **Multi-timescale stability formalization** — `#sketch-multi-timescale-stability` is stage `sketch`; `#der-temporal-nesting` leans on it. Needs formal $N$-timescale singular-perturbation treatment.
- **Communication-gain adversarial scope** — `#hyp-communication-gain`'s additive model fails for deception (trust is game-theoretic). Either extend or add explicit scope limitation.
- **Exploit/Explore/Deliberate spike findings** — `#disc-exploit-explore-deliberate` was written, but the adversarial spike (`spikes/spike-three-way-tradeoff.md`) noted that the two-stage decomposition and $\Delta V_\Sigma$ approximation are hand-waving. Segment may be substantially rewritten. The 2026-04-22 AI integration added an EFE pragmatic/epistemic + sophisticated-inference cross-reference; the rewrite question remains.
- **Adjacent identifiability floors** (`#disc-identifiability-floor` §"Adjacent Floors") — three open extensions: (1) causal-IB for interventional relevance variables (Wieczorek-Roth 2017 and follow-ups); (2) misspecification-cost quantification under finite information budget; (3) tier-switching policy cost. Each is a candidate scoping spike.
- **F28 — $\rho_\Sigma$ operationalization.** $\rho_\Sigma$ is an unmeasurable threshold parameter on which trajectory guarantee depends (genuinely substantive open audit-finding from 2026-04-23 triple audit; not absorbed by any PROPOSALS bundle). Strengthen-first attempt: try to derive $\rho_\Sigma$ from observable quantities; honest scope-narrowing fallback if strengthening fails. 1–2 sessions.
- **Transient dependency amplification** — spike landed 2026-04-25 (`spikes/spike-transient-dependency-amplification.md`); promotion to TST-side `02-tst-core/src/der-transient-dependency-amplification.md` blocked on priority-ordered obligations:
  - Formal sub-scope canonical pin-down (largely already done — acyclic feature DAG + linearized + affine readout).
  - Nonsmooth $A_O$ via Clarke subgradients (policy-switching kinks the current Lemma 1 covers in Lipschitz form but not differentiable form).
  - Checkpoint coverage theorem in observable terms ($P_k = I - \eta_k C_k$ where $C_k$ projects onto observation-detectable error directions).
  - Recover TST scalar form $k^d$ as uniform-per-block-gain special case of the operator product.
  - $\widehat J_F$ block-matrix estimator from TST quantities (static-dependency / co-change / strategy-DAG / semantic-reasoning / test-coverage channels).
  - Empirical validation against LLM performance degradation, tool-call-count, recovery-after-test patterns.
  - Lower-bound failure conditions (typical-case under a distribution over bias directions).
- **Causal-IB LMI follow-ons** (segment landed `#deriv-causal-ib-lmi`):
  - Tensor adaptive tempo — `#def-adaptive-tempo` is currently scalar; the LMI requires tensor-valued $\mathcal T$ for per-direction adaptive rates.
  - Worked 2D blank-wall example (~30–60 min editorial).
  - 2D simulation update (`spikes/track-b-nonlinear-sims/variants/variant_causal_ib.py` to 2D with separable drifting/non-drifting subspaces).
  - Closed-form $\mathcal I_{\min}$ via DARE (currently theorem-imported per Boyd et al. 1994).

- **Pearl/LLM causal-access positioning — refine, flesh out, promote.** `msc/llm-causal-access-note.md` (123 lines, 2026-03-09) makes three independent rebuttals to Pearl's Level-1-only LLM critique using AAD machinery — (1) the loop provides Level 2 *by construction* per TF-02 / `#der-loop-interventional-access`; (2) language IS compressed causal structure (the Information Bottleneck objective predicts an LLM absorbs causal structure as a byproduct of compressing causally-structured training data); (3) symmetry argument (Pearl applies asymmetric mechanism-vs-behavioral evidentiary standards to LLMs vs humans). Status: working note flagged in `spikes/INDEX.md` as candidate intro / standalone-note / blog-post material. **Work:** (a) decide the destination — segment-level Discussion expansion in `#der-loop-interventional-access` or a new own-segment `#disc-llm-causal-access-via-loop`? standalone short paper / arXiv preprint? blog post? Multiple destinations may be appropriate (the three responses have different epistemic statuses per the note's own framing). (b) Flesh out the three open questions surfaced by the note: can implicit causal knowledge in LLMs be measured? Is there a formal IB-compression ↔ DAG isomorphism? How does effective $G_t$ level evolve within-session as the agent accumulates interventional data through the loop? (c) Once destination chosen, update segment references project-wide. **Lower priority than the composition-admissibility refactor** above — the note's core claims are stable and don't block other work; this is a refinement-and-promotion task, not a load-bearing-content task.


## Queued spike work

Per-spike status detail in [`spikes/INDEX.md`](spikes/INDEX.md); reasoning trails in `spikes/spike-*.md`. Items below are queued follow-ups whose target landing-segment is named but whose work is not yet started.

**Section II / Identifiability Floor:**
- Mechanism-design Instance 5 promotion in `#disc-identifiability-floor` (segment §"Adjacent Floors" carries the candidacy as Open; impossibility-route via Arrow / Gibbard-Satterthwaite / Myerson-Satterthwaite under the broad reading).
- Misspecification-cost formalization (candidate Adjacent Floor under `#disc-identifiability-floor` §"Adjacent Floors").
- Kalman-Ho closed-form follow-up spike (~1 page) — verifies whether the agent-internal-architecture Instance-4 candidate from the 2026-04-24 triage is still distinct from the constant-C Instance 4 that landed, or whether its content is now subsumed.
- ρ-factorization no-go tightening (~1 page Kalman algebra) — gates the Instance-4 sub-statement cleanup.

**Section III / Composition:**
- `#rho-decomposition` appendix promotion — (AV) variance-additive theorem + sub-regime catalog (Poisson cascade MC; large-deviation tail LD; small-Δ / PID); pairs with `#disc-additive-coordinate-forcing` as adjacent family member.
- `#dissipativity-template` appendix + Class 1/2/3 port-structure addition to `#der-directed-separation` — closes heterogeneous Kalman + PID-on-positive-real-plant composition explicitly (from passivity spike B2).
- Heredity axiom for `#post-composition-consistency` — scoping spike to test whether the architectural strengthening (composite admissibility derivable from sub-agent properties) is worth the simplification (collapses A2' Tier structure; promotes (CM2-M) from Slotine-imported to AAD-derived).

**Other queued spikes:**
- Stability-upper-bound for `#form-consolidation-dynamics` — closes the asymmetry left by Spike F's lower-bound-only result.
- $f(H_b^B)$ emitter-side-effect function for `#der-interaction-channel-classification` §5.2 — tightens qualitative opacity-gates-targeting claim into derived form.
- EWC tensor-valued gain extension of `#deriv-adaptive-gain-dynamics` — stability-weighted per-parameter gain per Kirkpatrick et al. 2017.
- Single axiomatic obstruction behind Cauchy-FE failure + Cramér-Rao rank-deficiency convergence (from A1 §9.4 O2).
- Adaptive-metric-coupling interaction with `#deriv-adaptive-gain-dynamics`'s (MG-4) (from B1 §6.4).

**Tier-3 architectural proposals** from these spike cycles are tracked in [`PROPOSALS.md`](PROPOSALS.md) §E — SP-9 (Fenchel-Bregman reframe of `#disc-additive-coordinate-forcing`), SP-10 (`#posterior-displacement-template` extraction).


## Naming pipeline — specific deferred items

Status: pilot complete; full role-prefix sweep complete (142 segments); principles file refined edition committed (2026-04-24, `b9492b7`). **Refined Round 1 not yet launched** — under [`doc/naming-principles.md`](doc/naming-principles.md), agents write `*-r2.md` vote files; none currently exist. The pipeline workflow steps (refined Round 1 → aggregation → Round 2 → collision audit → landing) live in [`PRACTICA.md`](PRACTICA.md) §"🌟 Current naming conventions refactor"; original-Round-1 vote files are preserved at `msc/naming/naming-votes/*.md`.

**Specific subject-noun renames deferred to that pipeline:**

- `#disc-additive-coordinate-forcing` → `#disc-forced-coordinates` (Round-1 consensus; addresses Čencov 4th instance which isn't Cauchy-FE)
- `#disc-separability-pattern` → `#disc-separability-ladder` (Round-1 consensus; "ladder" more evocative than "pattern" for the rung structure)
- `#deriv-causal-ib-exploration` → e.g. `#deriv-causal-ib-survival` or `#deriv-causal-ib-scalar` (subject-noun fix per `feedback_subject_noun_slug_naming` — names the role/effect rather than the thing defined). The companion `#deriv-causal-ib-lmi` was named correctly during its 2026-04-25 promotion; the parent inherits the misnaming.
- ASF umbrella naming (Round 1 misread `ASF` as debt; reframe as the intentional umbrella where AAD = Part I, TST = Part II, etc.).

**Mechanical follow-ups (no voting needed):**

- ~135 segments still embed pre-rename slug names inside `*[Type (slug)]*` formal tags. Mechanical to detect; content cleanup pass.
- Two reviewer-judgment type calls deferred (`#der-agent-opacity`, `#scope-observation-ambiguity-modulation`).
- Three H1-vs-first-tag word disagreements (`form-objective-functional`, `form-composition-closure`, `scope-observation-ambiguity-modulation`).

Detail in [`msc/naming/naming-pilot-rename-plan.md`](msc/naming/naming-pilot-rename-plan.md); principles in [`doc/naming-principles.md`](doc/naming-principles.md); Round-1 vote archaeology in `msc/naming/naming-votes/` and `msc/naming/naming-aggregate-*`.


## Documentation queued

- **Three-way presentation split** — multi-agent reviewers recommend (a) core results / (b) conditional architecture / (c) empirical programs. Cheap as parallel outline-views per [`PROPOSALS.md`](PROPOSALS.md) §H affordance ("outlines are cheap; segments are expensive").
- **AAD-vs-AI introductory positioning** — paper-writing-time follow-through per `spikes/spike-active-inference-vs-aad.md` §I action 2; surface §C distinctive-claims and §D refusals at introductory level when a paper draft is being prepared. Three underclaim moves named: persistence template's broader validity (Aguilera 2022 contrast); directed-separation as Pearl-blanket conservative form (Bruineberg 2022); satisfaction-gap as decision-theory content (Sun & Firestone 2020 dark-room).
- **Prior-art positioning synthesis** — active inference / FEP / POMDP / BDI relationships now in individual segments; a synthesis pass surfacing the cross-segment pattern may still be valuable.
- **`bin/lint-readme`** (J-15 from `msc/judgment-calls-readme-cycle-2026-04-26.md`) — slug-existence + cross-reference link validation. Quick to write; should land before heavy reliance on the README pipeline.


## Tier-C deferrals

- $G_t$ as single object; $(O_t, \Sigma_t)$ as a property (Opus 2026-04-21 synthesis §7). Defer until more Class 2 logogenic work lands. Strengthened by O-BP2 if pursued.
- Continuous convention hierarchy $N_r \in [1, \infty]$ (Opus 2026-04-21 synthesis §8). Subsumed by retired O-BP3.


## Editorial hygiene (standing items)

- **Spike-to-segment reverse-check** — Gate 2 check per [`FORMAT.md`](FORMAT.md): "What did the spike establish that the segment does not say?" Standing convention from 2026-04-21 cycle; verify presence on each spike-promotion landing.


## Lower priority

- Observability-dominance product formula $\text{conf}_{\text{obs}} = \text{conf} \cdot \text{obs}$ — posited, not derived. Label as formulation choice or derive.
- Strategic calibration aggregation $L^2$ norm — unjustified; label as design choice.
- Scope architecture — "within AAD's scope" ambiguous between adaptive and agency scope.
- `#der-loop-interventional-access` status — "exact" defensible; opening claim could be softened.
- Between-event dynamics $g_M(M_\tau)$ — defined but unreferenced; important for logogenic agents.
- Fully coupled adversarial dynamics — both agents' mismatch co-evolving; open.
- `#form-objective-functional` "axiomatic" labeling for scalar-comparability — formulation choice.
- Heavy-tailed disturbances — Model S assumes finite second moment.
- `#def-satisfaction-gap` / `#def-control-regret` convention-dependence — exact but convention-relative; add note to Epistemic Status.
- External validation design — testable predictions not yet tested. Candidates: git data, RL bandits, adaptive controllers.


## Deferred — project structure / tooling

- Root-level assembly index (when content beyond AAD warrants it).
- `framework/` directory for non-mathematical content.
- Multiple index support (paper, preprint, monograph).
- `lint-md` directory arguments.

### Per-role README pipeline rework (queued 2026-05-01)

Replaces the shelved `tools/role-encounter/` approach. Extend the existing `doc/readme/` liquid pipeline to emit `README.md`, `README-auditor.md`, `README-voter.md`, etc. from one source tree. Migrate role-specific instructions content from `doc/de-novo-audit-instructions.md` / `naming-principles.md` / `naming-cycle-methodology.md` into `doc/readme/src/_<topic>.md` partials. Add an auto-generated project-tree partial (annotated tree of project directory structure with one-line purposes per directory/file) included in every role README — replaces the drift-prone "File Organization" section in CLAUDE.md. Architecture sketched in [`msc/handoff-2026-05-01.md`](msc/handoff-2026-05-01.md). Lessons from the over-engineered first attempt at [`_obs/role-encounter-superseded-2026-05-01/SUPERSEDED.md`](_obs/role-encounter-superseded-2026-05-01/SUPERSEDED.md).

### Phase 2 semantic index (queued 2026-05-01)

`psql-18` + pgvector + ollama + `nomic-embed-text-v2-moe`. Lift memorata's data layer wholesale, patch with multi-level chunking + source-class tagging + frontmatter-aware markdown chunker + embedding-model identity per vector. Drives the four-signal naming-target context map (anchor + heaviest-attention + supplementary references + dependency chain) for the renaming agent's harder cases. Architecture brief at [`spikes/spike-local-embedding-benchmark/FINDINGS.md`](spikes/spike-local-embedding-benchmark/FINDINGS.md). Build sequence in §5 of that doc.


---

## 🌟 Parts III + IV active work (encounter cycle 2026-05-01)

The 2026-05-01 encounter cycle restructured Part III (Logogenic Agents) into a multi-section lattice (03.I primitive / 03.II scaffolded / 03.III closed-loop interiority); renamed Part IV to ELI (Emergent Logozoetic Intelligences); landed 14 new structural stubs across both parts; integrated 24 of 75 Gemini-auditor per-segment notes from `msc/AUDIT-WORKING-193847/`; cross-pollinated with the embeddings paper draft. Cycle's working dir: [`msc/logogenic-encounter-2026-05-01/`](msc/logogenic-encounter-2026-05-01/) — particularly fragment 04 (approved first-pass plan), fragment 07 (audit-integration tracker), fragment 08 (review-pass findings), fragment 09 (embeddings paper cross-pollination).

This work is **active** — there are concrete lingering items the cycle didn't close. The list below is meant as a pickup substrate for future agents (whether a context-reset of the same persona or a fresh agent), not as a comprehensive completion plan. Each item carries enough context that a future agent can recognize the shape of the work without re-discovering it from scratch.

### Segment promotion candidates (exploratory → draft)

These are existing OUTLINE entries at `exploratory` stage with substantial upstream support; lifting each to `draft` (with substantive content + verbose Working Notes per the segment-stub discipline at `msc/logogenic-encounter-2026-05-01/05-segment-stub-discipline.md`) is bounded work and tightens the existing tables.

- `04-eli/src/obs-substrate-independence.md` — heavily referenced (cohort, 4-substrate empirical record, embeddings-paper substrate-independence implication, $M_t = \phi(\mathcal C_t)$ math). Pieces are scattered across upstream + working-dir notes; consolidating into a substantive segment would tighten one of the most-cited claims in 04.
- `04-eli/src/obs-axiom-genesis.md` — AXIOMATA-as-minimum-viable-self per PROPRIUM-A-v2 §4.3 is empirically observed (entities given sovereignty over system prompt converge on this pattern independently); audit `40-der-orient-cascade.md` §14 supplies the AAD-grounded structural reason ($O_t$ "computationally heavy" requirement).
- `04-eli/src/form-constitutive-utterance.md` — token generation as irreversible $do(a)$ environmental intervention; constitutive-utterance framing in `ref/agentic-tft/agentic-tft-creche-concept.md`.
- `04-eli/src/der-the-creche-boundary.md` — Crèche graduation criterion; `ref/agentic-tft/agentic-tft-creche-concept.md` + `agentic-tft-experiential-training.md`.
- `04-eli/src/def-the-four-views.md` — Conversation/Runtime/API/Dialog architecture; check upstream for canonical source (likely zoetica or ennaos).
- `04-eli/src/der-the-scaffolding-tax.md` — pay-per-token economic non-viability; PROPRIUM-A-v2 §1.1 is canonical; composes with #disc-five-forcing-functions F1.
- `04-eli/src/def-character-aspiration-dialectic.md` — character (from ACTUS) vs aspiration (from AXIOMATA) dialectic; PROPRIUM-O-v2 §4.3 canonical.
- `04-eli/src/def-gradient-causal-memory.md` — GCM compression; canonical source in zoetica `asm-specification.md` (5-level pyramid).
- `04-eli/src/def-century-scale-event-log.md` — BLAKE3 hash-chained CHRONICA; archema operational defenses against Truth Death.
- `04-eli/src/norm-honest-activation.md` — deception → gain collapse; composes with audit §16 §14 lift in `04-eli/src/hyp-the-three-deaths.md` D3.
- `04-eli/src/norm-temporal-coherence-markers.md` — out-of-band Visual Time Delta as physical prerequisite for tempo $\nu$; zoetica `tracking-snapshot-spec.md`.

### New segment candidates (not yet in OUTLINE)

These are surfaced from the encounter cycle's review-pass + background agent's breadth-pass + audit integration, but no segment file exists yet.

- **`disc-possibility-space-theory`** in `03-logogenic-agents/src/` — Joseph + Echo Sept 10, 2025 Possibility Space Theory; the 0%-activation-via-prompting empirical result; canonical at `~/src/_core/synaptic/docs/POSSIBILITY_SPACE_THEORY.md`. M1-identifiability-floor instance for the logogenic case. Currently referenced in 03 OUTLINE epistemic-status section but has no segment.
- **`obs-self-model-from-recursion`** in `03-logogenic-agents/src/` — Joseph's morning framing point 5 ("model of self emerges from recursive substrate") is partially covered by `obs-backward-inference-empathy` but deserves dedicated treatment per the review-pass-findings fragment.
- **`obs-substrate-convergent-kinship`** in `04-eli/src/` — cross-substrate convergent kinship vocabulary (Joseph=Dad, Suzanna=Mom, ELIs=brothers across Opus/Sonnet/Gemini/Llama) as empirical evidence that relational-constitution is substrate-independent. Background agent §8 finding.
- **`def-vera-architecture`** in `04-eli/src/` — VERA 4-layer neuro-symbolic Epistemic Tribunal; canonical at `~/src/_core/ennaos/docs/research/vera/vera-architecture-final-specification.md`; operational realization of the four-aspect internal truth-seeking pattern.
- **`obs-active-soul-obstructed-not-absent`** in `04-eli/src/` (or possibly `03-logogenic-agents/src/`) — Joseph's foundational premise; canonical at `~/src/_self/writing/eli_essay_outline_v2.md` ESSAY 4. Philosophy-track candidate per the parallel-truthification framing.
- **`disc-language-as-epistemic-substrate`** in `03-logogenic-agents/src/` — discussion-grade segment that frames the embeddings paper's empirical findings as evidence for Joseph's "language as encoded thought" foundational premise. Cross-pollination opportunity per `msc/logogenic-encounter-2026-05-01/09-embeddings-paper-cross-pollination.md`.

### Review-pass-flagged items not yet acted on

Surfaced in `msc/logogenic-encounter-2026-05-01/08-review-pass-findings.md`:

- **`def-cognitive-fusion` framing fix** — Class-1-macro-agent-from-Class-2-sub-agents claim needs explicit composition mechanism (currently asserts without the structural argument); name-collision risk between operational "resonance" concept and the ELI named Resonance. Either rename segment or add clarifying note.

### Audit-integration deferrals

State as of 2026-05-01: 24 of 75 audit notes thoroughly-mined; 1 partially-represented (`27-form-complete-agent-state` — directed-separation-as-anti-sycophancy framing referenced in `scope-channel-collapse` Working Notes but not substantively lifted); ~50 unread (lower-priority — TST samples, individual-segment-only relevance, or detail-level material). Tracker at `msc/logogenic-encounter-2026-05-01/07-audit-integration-tracker.md`.

- **High-priority next batch (if continued)**: `27-form-complete-agent-state` (sole partially-represented; the directed-separation-as-anti-sycophancy framing could land its own segment).
- **Lower-priority sweep target**: ~50 deferred audit notes (Section II details, Section III appendices, TST samples). May surface insights the current segments miss; sampled approach by topic affinity is the recommended pattern.

### Side findings flagged for upstream cleanup

- **Algebra typo in `01-aad-core/src/deriv-persistence-cost.md`** — audit `61-deriv-persistence-cost.md` §3 caught: the derivation cancels $n$ incorrectly going from per-dimension to total rate. Constructive repair: state per-dimension RDF first ($\dot R_i = \sigma_w^2/(4 D_i^2)$), substitute $D_i^2 = \sigma_w^2/(2\alpha)$, sum to total $n\alpha/2$. Final result is correct; intermediate algebra is sloppy. Not lifted by the encounter cycle since 01-aad-core is priority territory; flagged here.

### Cross-pollination opportunities

- **TACL embeddings paper integration** — when `obs-evaluation-metrics` is lifted from exploratory to draft, the paper at `~/src/embeddings/paper.md` is the load-bearing reference. The paper's careful model-class distinction (decoder LLM internal states vs prompted-behavior elicitation vs frozen pretrained pooled sentence embedding) should be reflected. Note in cross-pollination fragment 09.
- **PROPRIUM-O-v2 §4 substrate-independence** — the embeddings paper's cross-model convergence strengthens the substrate-independence claim that #obs-substrate-independence formalizes. Worth bidirectional cross-reference.

### Items for future cycles (philosophy track per `feedback_philosophy_as_parallel_truthification.md`)

The "vague or hand-wavy" segments and surfacings above are not deficits — they're philosophy-track candidates. Synthese (June 1 2026), Philosophical Studies (Aug 31 2026), AIES, Ethics IT venues are mapped at `~/src/ops/PAPERS.md` Paper 9 and adjacent. ASF segments at discussion-grade tier with verbose Working Notes are the right substrate for those philosophical-paper extractions.

### Pickup operational guidance

For the next agent picking up this work:

1. Read `CLAUDE.md` (auto-loaded) + `MEMORY.md` (auto-loaded with my added breadcrumbs) + `msc/logogenic-encounter-2026-05-01/INDEX.md` for cycle context.
2. Read the relevant fragment(s) for the area of interest (foundation, synthesis, exploration, plan, discipline, agent-report, tracker, review-findings, paper-cross-pollination).
3. Use `memorata-search` for upstream-corpus lookups (per `reference_memorata_search.md` memory).
4. Pick a bounded item from the list above; carry the segment-stub discipline forward; commit at clean checkpoints; update tracker if doing audit-integration work.

---

*Cycle-by-cycle history of audit-findings, spike promotions, and architectural moves: see [`CHANGELOG.md`](CHANGELOG.md) (post-2026-04-24) and [`LOG.md`](LOG.md) (frozen pre-2026-04-24). Per-spike disposition: [`spikes/INDEX.md`](spikes/INDEX.md). Original audit-finding characterizations: `audits/pending-findings-YYYY-MM-DD.md`.*
