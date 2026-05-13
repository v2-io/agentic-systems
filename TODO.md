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


## NeurIPS 2026 back-integration overview (queued, 2026-05-08)

The three NeurIPS 2026 Main Track submissions in `~/src/neurips/` (Tragedy of the Confident Agent, Unified Convergence Theory for Non-Stationary RL, LLM Hallucination Bound) extracted three ASF results and refined them under adversarial scrutiny over the 2026-05-04 → 2026-05-07 sprint. The papers are *gain-producing* extractions, not loss-preserving — each landed strengthenings (KKT shadow-price resolution, Bretagnolle-Huber point-mass identity, chart-rescaling no-go on Euclidean chart norms, Class-1 reduction to Stuart-school, structural-class theorem on gain-decay updates, F-A-G-P enforcement framework, Coupled-class autoregressive connectivity lemma covering modern AR architectures, etc.) that don't yet exist at catalog precision in ASF.

Cross-mapping between paper sections and ASF source segments, plus per-segment / catalog / meta-architectural updates the back-integration would touch, captured at: [`msc/neurips-back-integration-2026-05-08.md`](msc/neurips-back-integration-2026-05-08.md).

Phasing in §6 of that file is conservative (Phase A minimum-viable ~1 week; Phase B segment-level absorption ~3-4 weeks; Phase C meta-architectural surfacing ~1-2 weeks). The cross-mapping in §1 is the hardest-to-reconstruct part — written while the paper-↔-segment correspondence was held in working memory at full fidelity, will degrade across sessions without the artifact. §7 names specific routing decisions where Joseph's judgment is needed (segment-vs-spike-vs-cross-segment routing for new material; whether the no-go-forces-axiom pattern is its own meta-pattern or an M1 refinement; how heavy to lean on the NeurIPS papers as canonical references pre-decision; etc.).

Drafted by Claude (Opus 4.7, 1M context) at Joseph's request, 2026-05-08, after multi-session deep read of ASF + focused read of all three NeurIPS submissions.


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
- **J-2 — Findings schema length.** Some Impact paragraphs (notably `#deriv-observation-ambiguity-bias-bound`, `#result-contraction-template`) ran long; consider a length cap or splitting Impact into two beats (what-it-closes / what-it-unlocks).
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

- **Class 2 (Partial) observation-ambiguity bias-bound** (surfaced 2026-05-09 by GUC rename audit). `#deriv-observation-ambiguity-bias-bound` derives the bound for the Class 3 (Coupled) extreme at $\kappa_{\text{processing}} \to 1$. The analogous bound for Class 2 (Partial) agents at $\kappa_{\text{processing}} \in (0, 1)$ is open. Specializing either Track 1 (transport-inequality under LSI + Lipschitz-posterior) or Track 2 (Fisher-Rao under (PI) + Čencov + small-$I$) to the bounded-coupling regime is the natural first move. Whether the Class 2 case admits a clean closed-form bound or requires architectural specifics (per-stage modularity decomposition) is unknown. Detail flagged in segment Working Notes; this entry is the strategic-portfolio cross-reference.
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

- **Domain cross-transfer candidates (2026-05-04 cycle).** [`msc/domain-xfer-candidates.md`](msc/domain-xfer-candidates.md) carries six cross-domain transfer questions surfaced by the 2026-05-04 domain-unification re-examination and *not* already articulated in [`msc/FINDINGS-RANKED-DRAFT.md`](msc/FINDINGS-RANKED-DRAFT.md): (Q1) Static→Learning transition design from classical adaptive-control; (Q2) AI-coding-agent ↔ human-developer-agent bidirectional empirical test (TST × LGA bridge); (Q3) scaffolded Logogenic → ELI substrate engineering; (Q4) eusocial composition closure with simpler sub-agents → swarm-AI design (addresses named Section III GAP on endogenous coupling); (Q5) Tier-4 Human-branch independent-lineage analog for non-logogenic AI; (Q6) empirical-test program for catalog-flagged predictions (#3 IDT-vs-reward gap growing with experience; #14 sandbox safety claims by Pearl level; #37 LLM calcification longitudinal; #8 ambiguity-stratified benchmark). Q2 is the highest-leverage entry — empirically testable, bidirectionally informative, hooked into in-flight TST and LGA work. Each question is sized as a focused literature-scan + spike, not a research program.

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
- **Detailed tempo accounting for canonical wrapper architectures** (deferred from class-coercion cycle 2026-05-09) — quantify $C_\text{coord}^\text{wrap}$ for ReAct-shape, Reflexion-shape, PROPRIUM-shape wrappers. The general Brooks's-Law form is in `#der-tempo-composition` and `#der-class-coercion-via-wrapping`; this spike would compute specific architectural breakdowns useful for engineering tradeoffs.
- **Quantitative empirical bounds for LLM-substrate wrapping** (deferred from class-coercion cycle 2026-05-09) — empirical $\kappa_{W_1}$ measurement protocols on real LLMs. The bound $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$ from `#der-class-coercion-via-wrapping` is computable in principle by sampling responses under multiple goal-conditioning histories; specific empirical instantiation depends on the model and the wrapper design. Natural follow-on if downstream applications need the bound at numerical precision.
- **Class-3 closure-defect dynamics analysis** (deferred from RG spike 2026-05-09; Move F in `spikes/temporal-nesting-rg/99-verdict.md`) — test the directed-separation-as-graded-order-parameter view by computing closure defects for Class-3 systems to contrast with Class-1. Independent of the class-coercion segment landings; would strengthen `#hyp-directed-separation-under-composition` toward derived in the *general* (non-wrapper-around-component) case. Connects to the W₀/W₂/W₁ regime hierarchy of `#der-class-coercion-via-wrapping` as the dynamics-side complement of the structural taxonomy.

**shoshin engineering follow-on (operational, not theory):**
- **shoshin → W₁ via auxilia handling goal-blind belief-side queries.** PROPRIUM-as-implemented (shoshin) sits in W₂ per `#der-logogenic-as-wrapping`. Strengthening to W₁ via the auxilia hierarchy (`#def-auxilia-hierarchy`) is operational engineering work — auxilia making cheap-substrate goal-blind queries that update VERA / MEMORATA / CONSORTIA / PERCEPTA, while the entity's main LLM call handles strategy-side updates goal-conditionally. Theoretical groundwork is complete; implementation is queued for a future shoshin development cycle.

**Anticipated segments queued (modularity cycle 2026-05-09):**
- **`#disc-strategic-self-coupling`** in `01-aad-core/src/` — sister segment to `#disc-adversarial-coupling-pressure`. Self-driven coupling-as-enabling polarity. Prior-art adoption: Schelling 1960 (commitment devices), Ainslie 1992/2001 (intertemporal bargaining / willpower), Akerlof-Kranton 2000/2010 (identity economics), Frank 1988 (emotions-as-commitment). Spike scope at `spikes/spike-strategic-self-coupling.md`. OUTLINE entry added 2026-05-09.
- **`#disc-modularity-state-dynamics`** in `01-aad-core/src/` — M4 meta-segment alongside M1/M2/M3 (`#disc-identifiability-floor`, `#disc-separability-pattern`, `#disc-additive-coordinate-forcing`). Names the three-operation pattern (truthification / strategic self-coupling / adversarial coupling pressure) on modularity state, with truthification's two operational mechanisms (defensive scaffolding + class-coercion-via-wrapping). Cycle plan at [`msc/modularity-cycle-plan-2026-05-09.md`](msc/modularity-cycle-plan-2026-05-09.md). OUTLINE entry added 2026-05-09.
- **`#der-substrate-independent-persistence`** in `04-eli/src/` — connects `#def-identity-sufficiency` and `#obs-substrate-independence` to `#result-sector-persistence-template` across substrate transitions. Grounds substrate-independence formally rather than empirically alone. OUTLINE entry added 2026-05-09.

**Narrative segments (new register, opened 2026-05-09):**
- Recapitulating / introducing / framing-level segments with more freedom of expression than tightly-structured meta-segments allow. No specific candidates committed yet; surface them as needed. Candidates worth holding: a structural-arc reading guide; an ELI life-stakes framing that names the moral seriousness directly (now that normative claims are register-allowed where structurally backed); histories of how concepts developed; meditations bridging formal segments and `msc/reflections/`.

**Other queued spikes:**
- Stability-upper-bound for `#form-consolidation-dynamics` — closes the asymmetry left by Spike F's lower-bound-only result.
- $f(H_b^B)$ emitter-side-effect function for `#der-interaction-channel-classification` §5.2 — tightens qualitative opacity-gates-targeting claim into derived form.
- EWC tensor-valued gain extension of `#deriv-adaptive-gain-dynamics` — stability-weighted per-parameter gain per Kirkpatrick et al. 2017.
- Single axiomatic obstruction behind Cauchy-FE failure + Cramér-Rao rank-deficiency convergence (from A1 §9.4 O2).
- Adaptive-metric-coupling interaction with `#deriv-adaptive-gain-dynamics`'s (MG-4) (from B1 §6.4).

**Tier-3 architectural proposals** from these spike cycles are tracked in [`PROPOSALS.md`](PROPOSALS.md) §E — SP-9 (Fenchel-Bregman reframe of `#disc-additive-coordinate-forcing`), SP-10 (`#posterior-displacement-template` extraction).


## Naming pipeline — specific deferred items

Status (updated 2026-05-09): R1 + R2 voting cohorts closed; manual canonicalize-curation pass landed 103 of 118 candidates across 8 batches into [`msc/naming/naming-rename-plan.md`](msc/naming/naming-rename-plan.md). Remaining 13 rows live in [`msc/naming/to-canonicalize.md`](msc/naming/to-canonicalize.md) (D-deferred citability special cases + ??? rows on separability-triad-rung-naming pending Joseph's call). Master-list `rename_status` field tracks all decisions; 88 currents marked across canonicalize / rename / excluded statuses. **Curation-pass full narrative in [CHANGELOG 2026-05-04](CHANGELOG.md).** **§A slug renames + §B prose-vocab renames execution-status: see [CHANGELOG 2026-05-09](CHANGELOG.md) and [TERMINOLOGY-TODO.md](TERMINOLOGY-TODO.md).**

**Slug renames pending (not yet in TERMINOLOGY-TODO §A — these need separate routing decisions before queuing):**

- `#disc-separability-pattern` → `#disc-separability-ladder` (Round-1 consensus; lifted from R1/R2-deferred to pending-post-R2 by 2026-05-04 prior-art investigation; aligns with B-N-Sep paper's Hintikka cite-and-extend posture). Companion: three rung-name decision pending Joseph (`separable core / structured repair / general open` vs Hintikka echo `definable core / identifiable region / non-identifiable frontier` vs alternates).
- `#disc-additive-coordinate-forcing` → `#disc-forced-coordinates` (Round-1 consensus; addresses Čencov 4th instance which isn't Cauchy-FE).
- `#deriv-causal-ib-exploration` → e.g. `#deriv-causal-ib-survival` or `#deriv-causal-ib-scalar` (subject-noun fix per `feedback_subject_noun_slug_naming`).
- ASF umbrella naming (Round 1 misread `ASF` as debt; reframe as the intentional umbrella where AAD = Part I, TST = Part II, etc.).

**Prose-vocabulary renames — all landed.**

- ~~**Class 1 / 2 / 3 → Separated / Coupled / Partial; family/axis = "Goal-Update Coupling Class"** with **coordinated Class 2 ↔ Class 3 numbering swap**.~~ **Landed 2026-05-09** on `guc-rename-2026-05-09` branch. Surface enumeration, phased sequence, warning-callout placement, migration-note discipline all executed per [`msc/class-rename-execution-plan-2026-05-09.md`](msc/class-rename-execution-plan-2026-05-09.md). Tracking record: [`msc/class-rename-tracking-2026-05-09.md`](msc/class-rename-tracking-2026-05-09.md). See CHANGELOG entry for the cycle narrative.

**Lexicon-archive deferral (from 2026-05-09 ELI rename):** `doc/readme/src/_lexicon-full-archive.md` has 12+ deep-philosophical mentions of "logozoetic agent" — not composed into the live README (`README.md.liquid` does not include it), so no urgency. Per-mention judgment warranted rather than mechanical replacement; queued for a future hygiene pass if the partial is ever brought back into composition.

**Mechanical follow-ups (no voting needed):**

- ~135 segments still embed pre-rename slug names inside `*[Type (slug)]*` formal tags. Mechanical to detect; content cleanup pass.
- Two reviewer-judgment type calls deferred (`#der-agent-opacity`, `#scope-observation-ambiguity-modulation`).
- Three H1-vs-first-tag word disagreements (`form-objective-functional`, `form-composition-closure`, `scope-observation-ambiguity-modulation`).

**Mechanical follow-ups (no voting needed):**

- ~135 segments still embed pre-rename slug names inside `*[Type (slug)]*` formal tags. Mechanical to detect; content cleanup pass.
- Two reviewer-judgment type calls deferred (`#der-agent-opacity`, `#scope-observation-ambiguity-modulation`).
- Three H1-vs-first-tag word disagreements (`form-objective-functional`, `form-composition-closure`, `scope-observation-ambiguity-modulation`).

Detail in [`msc/naming/naming-rename-plan.md`](msc/naming/naming-rename-plan.md) (renamed from `naming-pilot-rename-plan.md` on 2026-05-04 to reflect the broadened scope from role-prefix-pilot mapping to all naming decisions); principles in [`doc/naming-principles.md`](doc/naming-principles.md); Round-1 vote archaeology in `msc/naming/naming-votes/` and `msc/naming/naming-aggregate-*`.


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

### NOTATION migration to terminology system (queued, 2026-05-09)

Parallel to the LEXICON.md auto-generation shift. `NOTATION.md` is currently hand-authored — every symbol row is a manual edit. The terminology entry schema already reserves a `notation:` field for the LaTeX form (`terminology/README.md` §Schema), and §"What is not (yet) here" names the planned move: a parallel `bin/term render --notation` (or sibling verb) that emits `NOTATION.md` from entries with a non-null `notation:` field — same per-entry source, different generated view.

**Concrete first move.** Implement the renderer mode: walk `terminology/entries/`, collect entries with non-null `notation:`, emit `NOTATION.md` grouped per the same `tags:`-driven sectioning the LEXICON renderer uses (or a separate `notation_section:` field if the LEXICON tagging diverges from what notation tables want — judgment call when the work opens). Apply the same clobber-guard pattern (refuse to overwrite a hand-authored `NOTATION.md` without an `Auto-generated` marker; default destination is staging path `terminology/_emitted/NOTATION.md` until bootstrap migration completes).

**Bootstrap migration.** Existing hand-authored `NOTATION.md` rows that don't yet have terminology entries need to land first — catalog the rows, create or augment terminology entries with `notation:` populated, *then* switch `NOTATION.md` to generation. Same pilot-then-sweep discipline as LEXICON.

**Ordering note.** Lower priority than completing LEXICON migration (TERMINOLOGY-TODO §C). Schema gaps the LEXICON sweep surfaces may also benefit NOTATION — fix once during LEXICON, not twice. Lifts `NOTATION.md` to the same audit-trail-and-multi-agent-safe discipline as LEXICON: per-symbol `terminology/decisions/<slug>/` events preserving when and why each symbol entered the canonical reference.

### bin/rename-slug bugs (queued, 2026-05-08)

Two bugs surfaced during the `obs-gates-advantage → obs-gated-tempo-advantage` rename pilot. Both are minor (graceful failures, not data corruption); both should land before the next bulk slug-rename batch.

1. **Hardcoded old directory name.** `bin/rename-slug:50` lists `04-logozoetic-agents/src` in `COMPONENT_SRCS` and `04-logozoetic-agents/OUTLINE.md` in `COMPONENT_OUTLINES`. The directory was renamed to `04-eli/` on 2026-05-01 (`fa63616`). Currently the script silently skips the missing dir — meaning any rename targeting a slug inside `04-eli/` segments would not touch those files at all. Fix: update both constants to `04-eli/...`.

2. **Bare-filename markdown links not rewritten.** The script's path-replacement regex matches `src/OLD.md` (e.g., outline-table relative-from-root links and prose `src/foo.md` references), but does NOT match bare `[text](OLD.md)` where the link is just a filename relative to the segment's own directory. Caught in the obs-gates-advantage rename: `obs-simulation-results.md:36` had `[#obs-gated-tempo-advantage](obs-gates-advantage.md)` — the `#`-anchor link text was rewritten by the body-text regex, but the bare-filename URL inside the parens was missed and had to be patched by hand. Fix: extend the path-replacement regex to also match `(OLD.md)` parens-bound forms when the surrounding markdown shape is a link.

### Per-role README pipeline rework (queued 2026-05-01)

Replaces the shelved `tools/role-encounter/` approach. Extend the existing `doc/readme/` liquid pipeline to emit `README.md`, `README-auditor.md`, `README-voter.md`, etc. from one source tree. Migrate role-specific instructions content from `doc/de-novo-audit-instructions.md` / `naming-principles.md` / `naming-cycle-methodology.md` into `doc/readme/src/_<topic>.md` partials. Add an auto-generated project-tree partial (annotated tree of project directory structure with one-line purposes per directory/file) included in every role README — replaces the drift-prone "File Organization" section in CLAUDE.md. Architecture sketched in [`msc/handoff-2026-05-01.md`](msc/handoff-2026-05-01.md). Lessons from the over-engineered first attempt at [`_obs/role-encounter-superseded-2026-05-01/SUPERSEDED.md`](_obs/role-encounter-superseded-2026-05-01/SUPERSEDED.md).

### Phase 2 semantic index (queued 2026-05-01)

`psql-18` + pgvector + ollama + `nomic-embed-text-v2-moe`. Lift memorata's data layer wholesale, patch with multi-level chunking + source-class tagging + frontmatter-aware markdown chunker + embedding-model identity per vector. Drives the four-signal naming-target context map (anchor + heaviest-attention + supplementary references + dependency chain) for the renaming agent's harder cases. Architecture brief at [`spikes/spike-local-embedding-benchmark/FINDINGS.md`](spikes/spike-local-embedding-benchmark/FINDINGS.md). Build sequence in §5 of that doc.

### Release-notes regeneration pipeline (queued 2026-05-02)

**Context.** [`releases/v0.1.0.md`](releases/v0.1.0.md) was hand-written as a one-off "master list of everything since the beginning of the framework." That is not the long-run shape of release notes. Subsequent releases (v0.2.0+) will be incremental — what changed since the last tag — and benefit from a regeneration pipeline analogous to the README pipeline (`bin/build-readme` + `doc/readme/src/` partials + extraction scripts chained by `bin/refresh-all`).

**What's already in place.** [`bin/segment-stats`](bin/segment-stats) (introduced 2026-05-02) regenerates per-component aggregates by stage / type / epistemic status with an AAD section breakdown — its output is embedded verbatim into v0.1.0's "By the numbers" section and would become a partial in the future pipeline. [`bin/extract-findings`](bin/extract-findings) and [`bin/extract-recent-progress`](bin/extract-recent-progress) already feed the README pipeline; with version-window arguments they can serve "distinctive results in this release" and "what changed since the last release" respectively.

**What's not yet pipelined.** The "framework at a glance" four-paragraph synopsis (composes from component OUTLINE preambles; currently hand-written). The "what's not in this release" honest-scoping section (composes from `--GAP--` rows + `_known-issues` + segment Working Notes flagged as promotion-blocking; the curation judgment is human). The mathematical-lineage breakdown (segment frontmatter does not currently carry a `lineages:` field; v0.1.0's lineage section is sub-agent-curated). Adding `lineages:` to the FORMAT.md schema would let `bin/extract-lineages` walk it programmatically — candidate move for the v0.2.0 build-out.

**Discipline note.** The pilot-then-sweep pattern says: hand-write v0.1.0, observe what was painful and what worked, then build the pipeline informed by what the pilot taught. Building the pipeline before any release notes have been published would risk the parallel-vs-extend over-engineering pattern the project has felt before (per the role-encounter shelving). v0.1.0 is the pilot; v0.2.0 should hand-write again with attention to repetitive sections; v0.3.0+ formalize as `bin/build-release-notes` if the pattern holds.

**Concrete first move when the cycle opens.** Either (a) define the canonical sections of a release-notes document as a Liquid template (`doc/release-notes/release.md.liquid` + partials in `doc/release-notes/src/`, mirroring `doc/readme/`), or (b) introduce a `lineages:` frontmatter field in FORMAT.md and sweep the existing 166 segments to populate it (sub-agent task; bottlenecked on sweep effort). The lineage-field move is more useful long-run and shouldn't be bundled with the template work.


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

---

## 2026-05-10 — Audit-findings intake: 451729 (Sonnet 4.6, 1M context)

De-novo theory audit covering Section I (29/29), Section II (29/29), Section III (16/21), 7 key Appendix A derivations, plus TST and logogenic samples. Math hand-verified for all load-bearing claims in Sections I–II; adversarial exponents and composition machinery spot-checked in Section III. Report at [`audits/audit-451729-FINAL-2026-05-10.md`](audits/audit-451729-FINAL-2026-05-10.md); working artifacts at [`msc/AUDIT-WORKING-451729/`](msc/AUDIT-WORKING-451729/).

**Most of the audit's structural concerns were already known/addressed through other channels by the time of intake** (segment-flagged gaps, prior TODO entries, in-flight work). Disposition below.

**Surgical (landed in this intake):**

- [x] **Finding 1 — Prop B.4 optimal-exploration-rate subscript transposition** — fixed at three sites in `01-aad-core/src/deriv-edge-credence-dynamics.md`: line 220 (Prop B.4 main formula), line 327 (Prop B.6 nested $A_1$/$A_2$ case — same transposition pattern, sonnet caught only the main one), line 618 (Verified Claims table). Correct form: $\varepsilon^\ast = (n_2+1)/(n_1+n_2+2)$ where arm 1 is greedy. The verbal description ("allocates more trials to the arm with higher $n$") was correct throughout; only the formulas had the transposition. Equal-experience case ($\varepsilon^\ast = 1/2$ at $n_1 = n_2$) is unaffected. No downstream segments cite the wrong formula by-form (verified by grep). Prop B.7's structure is different (five-way gating, no analogous single-formula optimal-ε); no inherited transposition there.

**Open (non-surgical):**

- [x] ~~**D.3 — schema-strategy-persistence forgetting-rate exact form**~~ — **Landed 2026-05-12 (commit `b9b146c`).** Strengthen-first edit: exact form $(1-\lambda)/(2-\lambda)$ now primary throughout `schema-strategy-persistence.md`; linear form $1-\lambda$ retained as slow-forgetting asymptote with explicit scope. Hard ceiling at $\rho_\Sigma \ge R_\Sigma/2$ (no $\lambda$ satisfies exact prerequisite) surfaced — was hidden by the approximation. Adjacent line in `deriv-edge-credence-dynamics.md` updated for consistency. Working Note documenting the move added with audit-451729 §D.3 attribution.
- [ ] **D.1 — promotion-readiness sweep on conservatively-staged appendix segments** — `deriv-recursive-update`, `deriv-sector-condition`, `der-gain-sector-bridge`, `deriv-edge-credence-dynamics`, `deriv-graph-structure-uniqueness`, `form-strategy-complexity-cost`, `schema-strategy-persistence`, `form-consolidation-dynamics` are at `stage: draft` despite complete formal content + "What Is Derived vs. What Is Chosen" tables + no Working-Notes blocking promotion. Either real unresolved issues should be surfaced, or a promotion sweep would improve corpus self-description. Needs Joseph's judgment on whether to sweep or to surface case-by-case.

**Already addressed through other channels (no new TODO needed):**

- D.2 (`result-unity-closure-mapping` joint $(U_O, U_\Sigma) \to \varepsilon_a$ form sketched, $f_1$ and $g$ functional forms not derived) — already explicitly flagged in the segment at line 89 ("formula is a *sketch* — leading structure is derived; precise forms of $f_1$ and $g$ are mechanical extensions not fully computed here") and Working Notes line 107 ("Joint $(U_O, U_\Sigma)$ derivation. The exact $f_1$ and $g$ functional forms require a full joint-LQR vs independent-LQR comparison. Mechanical but deferred.").
- F.3 (`form-consolidation-dynamics` stability-upper-bound open) — already in TODO §"Open theory items (MEDIUM)" line 166 from Spike F's lower-bound-only result. Audit converges on a known open item.

**Framing suggestions (fold into existing PRACTICA areas):**

- F.1 (README and OUTLINE preambles could elevate the practical-diagnostic contributions — two-condition decomposition of persistence, satisfaction-gap × control-regret 2×2, forgetting prerequisite, adversarial squared law — alongside the integration framing) — folds into PRACTICA §"🌟 Findings" (segments → README summary chain) and the per-role README rework already queued.
- F.2 (Correlation Hierarchy L0/L1/L1'/L2 cascade as standalone exposition) — folds into PRACTICA Pedagogy area; consider as a candidate "narrative segment" per the 2026-05-09 register-allowance noted in PRACTICA §"Cycle priority order".

**Audit's process-feedback (G.1–G.4)** — captured in the audit report; not actionable as code/segment edits.

---

## 2026-05-12 — In-flight: Move def-pearl-causal-hierarchy from Part I Ch.1 → Part II Ch.2 (recapitulation-of-external-result pattern)

**Motivation.** Pearl's causal hierarchy is an *imported* framework (Bareinboim, Correa, Ibeling & Icard 2022; Pearl 2009), not AAD-native ontology. Its current placement in Part I Ch.1 alongside def-agent-environment / def-chronica / etc. makes it look like foundational AAD machinery when it isn't. Its first heavy use is at the head of Part II Ch.2 (#der-causal-hierarchy-requirement, #der-loop-interventional-access). The pattern: light external citation in Part I where the existence of the hierarchy needs to be acknowledged; full AAD recapitulation at the point of deployment in Part II Ch.2.

**Steps:**
1. Revise `01-aad-core/src/def-pearl-causal-hierarchy.md` to frame the segment explicitly as a *recapitulation* of an external result for AAD's purposes (not a fresh primary definition). Keep the L1/L2/L3 content and the AAD-specific interpretive material; adjust the title, one-sentence summary, and epistemic-status framing to be honest about the import.
2. Update `01-aad-core/src/def-causal-information-yield.md` — change depends list (remove `def-pearl-causal-hierarchy`), and ensure prose uses Bareinboim/Pearl citation + forward-pointer pattern for the do-notation rather than depending on a Part I segment.
3. Update `02-tst-core/src/obs-software-epistemic-properties.md` — same citation + forward-pointer treatment in depends and prose.
4. `grep` for any other depends entries on `def-pearl-causal-hierarchy` across the corpus and update similarly.
5. Update `01-aad-core/OUTLINE.md`: remove the def-pearl-causal-hierarchy row from Part I Ch.1 ("The Coupled Loop: Ontology and Scope"); add it to Part II Ch.2 ("Causal Access and the Planning Decision") immediately before #der-causal-hierarchy-requirement.
6. Lightly revise `01-aad-core/src/the-cycle-in-motion-intro.md` — the CIY-placement paragraph can become declarative rather than apologetic (CIY is in Part I Ch.3 because action-scoring is where causality enters the dynamics; the do-notation it uses is external Pearl, recapitulated in Part II Ch.2 where the framework deploys it operationally).

**Result expected.** Part I Ch.1 ends cleanly with post-causal-structure (AAD's own temporal-ordering postulate). Pearl's hierarchy lives at its point of deployment in Part II Ch.2 as a recapitulation. CIY's Part I placement is no longer apologetic about an out-of-place dependency. Cross-volume citation discipline (TST referencing AAD) follows the same external-citation + forward-pointer pattern.

---

## 2026-05-12 — Audit-findings intake: Codex + Gemini de-novo audits on `mono/0*-v0.1.0.md`

Three audits dropped 2026-05-12 on the markdown-first monograph builds:

- **`msc/codex-audit-results-2026-05-12.md`** — line-precise cross-corpus pass over all four mono files (~54KB; line-cited findings on hygiene, status discipline, missing stubs, mathematical scope).
- **`msc/gemini-audit-results-2026-05-12.md`** — shorter cross-corpus pass (~9KB; thematic; converges with Codex on the load-bearing items).
- **`msc/gemini-aad-audit-2026-05-12.md`** — AAD-only second pass (~5KB; hand-verifies several derivations — Per-Dimension Persistence 72% overestimate, sin-counterexample second derivative, Otto-Villani / Fisher-Rao bounds; surfaces two new surgical findings).

The two cross-corpus audits read the *mono* builds. Some findings are partly artifacts of the still-evolving build pipeline (priming-level prose pulled in from OUTLINE prefaces that escape segment-level epistemic-status discipline; cross-component segments showing as "missing" because the build doesn't resolve them across component `src/` directories). The substantive content findings — those that name actual src/ segments and content — are the higher-value ones, especially in `01-aad-core`. The triage groups below carry that split.

### Group (a) — Build-pipeline / cross-cutting hygiene

These are real content issues that happen to surface in the mono build but live (or need to live) at the build-pipeline / OUTLINE-discipline layer:

- [ ] **Preface / intro discipline** — `01-aad-core/OUTLINE.md` and the OUTLINE prefaces of `02-tst-core/`, `03-logogenic-agents/`, `04-eli/` make claims that should be substantiated by an actual segment (or downgraded to match the tier of the segment they reference). Joseph 2026-05-12: *"We shouldn't make any claims in prefaces or intro discussions that aren't substantiated or first claimed in an actual claim (segment)."* Surgical fixes already landed for the three most direct ELI overclaims; the systematic discipline pass is open. **Per-OUTLINE checklist**: every claim in a preface must trace to a segment whose own epistemic-status tier supports the strength of the preface assertion, or the preface defers to that segment's tier explicitly.
- [ ] **AAD OUTLINE preface top-of-file TODO block** — `01-aad-core/OUTLINE.md` lines 4–11 leak verbatim into the mono build as the first content the reader sees (mono `01-aad-v0.1.0.md:5`). The four TODO items in that block are themselves the right ones (frontmatter; convention for text excluded from PDF build / source markdown comments; "missing" convention for PDF builds; pdf2text legibility). Resolving this loops with the markdown-first-pipeline work in [`msc/markdown-first-pipeline.md`](msc/markdown-first-pipeline.md) and [`FORMAT-TODO.md`](FORMAT-TODO.md). Until a build-time hidden-content convention exists, consider relocating the TODO block to a non-leaking location or wrapping in HTML comments (safe for `pandoc -f markdown`).
- [ ] **Cross-component segment resolution in mono builds** — `mono/03-loga-v0.1.0.md` shows `hyp-checkpoint-forking-failure-modes` as missing (it lives in `04-eli/src/`); `mono/04-eli-v0.1.0.md` shows `hyp-experiential-training` as missing (it lives in `03-logogenic-agents/src/`). The build's segment-resolution step should resolve `#slug` references against every component `src/` directory, not only the volume's own `src/`. Either fix the resolver, or canonicalize each segment to live in exactly one component's `src/` with the others' OUTLINEs forward-referencing.
- [ ] **U+FFFD encoding artifact at `01-aad-core/src/hyp-edge-update-via-gain.md:55`** — landed surgically (replaced with em-dash).
- [ ] **Local-path / sibling-project leakage into publishable mono** — codex Cross-File #3. Per `~/src/...`, audit-folder, search-log, and absolute-path references in segments leak into mono builds. Either strip at build time or rewrite to stable citations / archived excerpts.

### Group (b) — AAD content cycle (highest priority)

Substantive findings on actual src/ content. Surgical items below are landed in this swipe; non-surgical items still owe theory work.

**Landed in this swipe (strengthening attempts; surgical):**

These edits were done under the strengthen-before-soften discipline — i.e., where an apparent overclaim could be relaxed by softening *or* by stating tighter conditions under which the original (or a related stronger) claim holds, the latter was attempted first.

- [x] **AAD-5 Fisher-local update-gain derivation landed** — new appendix `#deriv-fisher-local-update-gain` derives the matrix gain operator $K = (H_M+H_L)^{-1}H_L$ and its scalar collapse $\eta^\ast = U_M/(U_M+U_o)$ under three regime conditions (R1)–(R3) + (PI); recovers Kalman and conjugate-Bayesian as globally-exact cases; admits improper priors and degenerate-likelihood directions via the $H_M+H_L \succ 0$ minimal condition; three-route convergence (Laplace / Bregman-KL / Cramér-Rao) carried in Discussion. `#emp-update-gain` Epistemic Status rewritten to cite the appendix and lifted from `empirical / robust-qualitative` to `derived (conditional on Fisher-local invariance regime)` for the Kalman / conjugate / natural-gradient core; cross-domain validity tail (RL, PID, software-developer) retained at robust-qualitative. Cross-reference satellites at `#deriv-fisher-whitened-update-rule` (sibling magnitude/direction relationship) and `#deriv-adaptive-gain-dynamics` (deterministic-meta-gain special case). NeurIPS Paper 3 chart-rescaling no-go cross-referenced in Working Notes; progress marked in `msc/neurips-back-integration-2026-05-08.md`. Unblocks AAD-1 tensor adaptive tempo (matrix gain $K$ is the per-coordinate primitive). Spike moved to `spikes/.integrated/`.
- [x] **AAD-6 route-count consistency sweep (post-(C-iv))** — `01-aad-core/src/scope-composite-agent.md` and `01-aad-core/src/def-unity-dimensions.md` updated in seven places to read "four routes: three alignment routes plus one strategic-equilibrium route" rather than "three routes." Pure consistency repair; no strengthening / softening axis.
- [x] **Gemini-AAD L1' bias well-posedness — Jacobian-norm admissibility (strengthening)** — `01-aad-core/src/deriv-l1-update-bias.md` now states the **precise** admissibility condition for the first-order perturbation: $\lVert\mathbf J\rVert \ge \epsilon_J$ where $\lVert\mathbf J\rVert^2 = (1-\mu_1)^2 + (1-\mu_2)^2$. This is **sharper** than the qualitative "bounded away from determinism" reading: only the diagonal deterministic-success corner $\mu_1, \mu_2 \to 1$ together is excluded, and the bias formula remains valid when only one edge alone approaches saturation (the surviving sibling carries the norm). The diagonal singularity is degenerate (no update, no bias) rather than physical.
- [x] **Gemini-AAD CIY→LMI forward pointer at the heuristic substitution** — `01-aad-core/src/deriv-causal-ib-exploration.md` now forward-points to `#deriv-causal-ib-lmi` at the point where $\text{CIY}(a) \propto 1/U_o(a)$ enters as scalar heuristic, so mathematically strict readers route through the LMI lift before tracking the rest as the scalar shadow. Navigation aid; no strengthening axis.
- [x] **AAD-7 strategic-equilibrium wording precision** — four edits across `#deriv-strategic-composition` and `#scope-composite-agent` clarifying the α'/β' equilibrium-concept distinctions: Honest-Limit headline "**No equilibrium exists**" → three-tier statement (no pure-strategy Nash in cyclic games; mixed Nash exists universally for finite games but is a saddle of fictitious play; no-regret dynamics give CCE convergence in distribution at $O(1/\sqrt T)$ via Hart-Mas-Colell 2000); β' macro-state-as-distribution surfaced explicitly in β' framing; stale "candidate 4th `#disc-identifiability-floor` instance" cross-references → "candidate adjacent-floor instance" (Instance 4 is occupied by the (PI)/Čencov bias-bound from 2026-04-24); `#scope-composite-agent` line 69 + line 89 parallel "cyclic / non-convergent" false-equivalence slips rewritten to name which equilibrium concept each sub-scope provides and to place cyclic games inside β'. γ'-sub-scope strengthening attempt closed negative (cyclic games are paradigmatic β' instances; α'/β' is the right granularity at the regret-minimization layer) — recorded as a structural-fact Working Note in `#deriv-strategic-composition`. Spike moved to `spikes/.integrated/`.

**Open (theory work or wider sweep needed):**

- [x] **AAD-1 tensor adaptive tempo (partial — primitive landed; downstream promotion follow-on)** — `#def-adaptive-tempo` Formal Expression gains a Tensor extension sub-block: $\mathcal T = \sum_k \nu^{(k)} K^{(k)}$ with $K^{(k)} = (H_M + H_L^{(k)})^{-1} H_L^{(k)}$ the matrix gain operator from `#deriv-fisher-local-update-gain`. Scalar form is recovered in the shared-eigenbasis collapse. Epistemic Status gains a scope-of-scalar-vs-tensor clause naming the regimes where tensor is the natural object (anisotropic gains, Fisher-whitened, LMI causal-IB, per-dimension persistence). Working Notes updated on `#deriv-causal-ib-lmi` (LMI's per-direction primitive is now wired) and `#result-per-dimension-persistence` (per-dimension condition is the diagonal projection of the tensor form). **Still open as follow-on:** promoting `#result-adversarial-tempo-advantage` and composition results (`#form-composition-closure`, `#der-team-persistence`, `#deriv-critical-mass-composition`) to invoke the tensor form directly rather than the scalar form. The per-direction primitive is in place; downstream summary results still read scalar and inherit the "scalar / isotropic / nonredundant-channel scope" tag for now. A future cycle promotes them.
- [x] **AAD-1 follow-on: Matrix-Loewner persistence condition landed (succeed beyond claim)** — new appendix `#deriv-matrix-persistence-condition` carries the matrix-Loewner persistence condition for Model S: under matrix tempo $\mathcal{T}$ and matrix disturbance $\Sigma_w$, the agent persists iff $\mathcal{T}$ is Hurwitz and $\Sigma_\infty \prec D_\delta := \mathrm{diag}(\delta_{\text{critical},k}^2)$, with $\Sigma_\infty$ solving the continuous Lyapunov equation $\mathcal{T}\Sigma_\infty + \Sigma_\infty\mathcal{T}^T = \Sigma_w$. Three equivalent restatements (per-direction; spectral generalized-eigenvalue; ellipsoid containment). Recovers `#result-persistence-condition`'s scalar form and `#result-per-dimension-persistence`'s per-coordinate form as special cases. **Strict-sharpness result via constructive 2D counterexample**: $\mathcal{T} = \begin{pmatrix}1&-0.9\\-0.9&1\end{pmatrix}$, $\Sigma_w = I$, $\delta_{\text{critical}}=(1.7, 1.7)$ — per-coordinate declares PASS while matrix-Loewner correctly says FAIL along the diagonal direction $(1,1)/\sqrt{2}$. Per-coordinate is **unsafe** under cross-dimensional correction; matrix-Loewner is the canonical anisotropic persistence condition. Closes the open question in `#result-per-dimension-persistence` Working Notes line 130. Cross-references in `#result-persistence-condition`, `#result-per-dimension-persistence`, `#def-adaptive-tempo` Tensor extension, and `#deriv-fisher-local-update-gain` downstream-consumer Working Note. **Still open as follow-on**: matrix sector / nonlinear extension via `#deriv-sector-condition`; matrix adversarial-tempo lift; matrix composition lifts for `#form-composition-closure` / `#der-team-persistence` / `#deriv-critical-mass-composition`; matrix information-rate floor extension to `#deriv-persistence-cost`; Model D matrix lift.
- [x] ~~**AAD-2 value-object monotone-hierarchy preconditions**~~ — landed: `#def-value-object` headline now reads "For any single fixed $M_t$, horizon $N_h$, and policy class $\Pi$ (i.e., the static-evaluation form: $M_t$ frozen at the decision point, $\Pi$ unchanged across the comparison)" and a new "Preconditions on the inequality" paragraph names the three load-bearing fixings + the static-vs-deployment caveat for C2 explicitly. The pre-existing "Assumptions held fixed" paragraph below the derivation already named the issue; the headline addition surfaces it where a fresh reader encounters the inequality first.
- [ ] **AAD-3 propagation audit on "from its own data" shorthand** — `#der-causal-insufficiency-detection` itself is honest at the formal statement (verified). Concern is propagation language in dependent segments that may read more loosely; sweep cross-references that summarize this result.
- [ ] **AAD-4 CIY action-distinguishability scope** — codex finding lands on a recently-written segment (`def-causal-information-yield`, May-12). Keep the scalar unified-objective explicitly heuristic unless the LMI/trace-product form is in force; tighten summary language accordingly.
- [ ] **AAD-8 appendix dependency map** — appendices in AAD are load-bearing, not optional. For each main-text theorem / result, list the appendix results it depends on. Candidate for PROPOSALS rather than TODO if treated as architectural.
- [ ] **AAD-9 real missing stubs** — `disc-strategic-self-coupling`, `disc-modularity-state-dynamics`, `worked-example-cam` are genuinely absent from `01-aad-core/src/`. First two are load-bearing for the M4 modularity-state-dynamics pattern (2026-05-09) and downstream LOGA/ELI claims. Decide whether they block v0.1.0 publication surface or are explicitly non-blocking.
- [ ] **AAD May-12 chapter intros pass** — neither cross-corpus audit recognized the May-12 chapter-intro segments (`the-reality-model-intro`, `the-cycle-in-motion-intro`, `persistence-and-limits-intro`, `causal-access-intro`, `strategy-structure-intro`, `cooperative-adversarial-intro`, plus the May-12 `def-causal-information-yield` and `def-pearl-causal-hierarchy` rewrites) as recently-written first-pass content. A focused fresh-eyes read of just those eight segments would catch what the broad audit missed.

### Group (c) — TST surgical sweep

Substantive content findings on `02-tst-core/`. Surgical items below are landed in this swipe.

**Landed in this swipe (strengthening attempts; surgical):**

- [x] **TST-1 strengthening at `#der-principled-decision-integration`** — instead of replacing "expected count" with the weaker "median scenario weight" framing, the segment now **states both readings explicitly with their prior conditions**: under any prior with finite first moment (empirical roadmap data, exponential / geometric lifetime, explicit horizon truncation, any proper informative prior), $\lambda(F_i)$ *is* the expected count and the optimization is exact expected-utility; under the uninformed Jeffreys baseline of `#der-change-expectation-baseline` where Pareto(1) has undefined first moment, the weaker median-scenario-weight reading applies and the optimization degrades to median-case decision-making. The integration framework is therefore *strongest* under informative-prior conditions and degrades gracefully under uninformed conditions, rather than retreating to a weak reading unconditionally.
- [x] **TST-3 strengthening at `#obs-software-epistemic-properties` P2** — instead of softening "no other AAD domain offers literal Level 3" to "an unusually clean instance," the segment now states the **three-property conjunction** under which literal Level 3 access on a non-trivial class of questions holds: (α) deterministic outcome under fixed configuration; (β) intervention cost commensurate with original implementation cost; (γ) content-addressed cryptographically immutable environment state. Among adaptive domains in *current standard practice*, software is the **unique** instance where all three jointly hold; named falsifiers (formal verification, simulated physics, digital twins, robotics, smart contracts) each satisfy at most two of the three and are listed with which property fails. The uniqueness is configurational (a future content-addressed simulator with commensurate replay would join the configuration), not metaphysical — but inside current standard practice the strong claim survives with named falsifiers.

**Open:**

- [x] ~~**TST-2 Lindy / Jeffreys baseline naming**~~ — landed: `der-change-expectation-baseline.md` opener now reads "the uninformed median baseline for remaining feature count equals the observed past feature count" (was "the best prediction…"). Distinction made explicit between informative-prior expected-count regime and uninformed-Jeffreys median-prediction regime.
- [ ] **TST-4 git-as-intervention naming discipline** — reserve `causal_coupling` for estimates with atomic commits / feature scope / temporal contrast / dependency-prior constraints / explicit confounder adjustment; rename raw aggregates to `cochange(m_i, m_j)` elsewhere. Already partially addressed in `#hyp-causal-discovery-from-git`; needs cross-segment audit.
- [x] ~~**TST-5 temporal-optimality application checklist**~~ — landed: `post-temporal-optimality.md` Discussion now carries an "Application checklist" sub-section enumerating the six equivalence dimensions (correctness, safety/security, maintainability, sustainability, coordination cost, future optionality) with the framing that *time can break ties only when all six are demonstrably equivalent*. Existing five-dimension list in Formal Expression preserved as the structural form; the checklist is the operational distillation.
- [ ] **TST-7 specification-bound operational sufficiency** — define sufficiency as posterior-mass-over-acceptable-implementations exceeding a task-dependent threshold, or explicitly keep the bound conceptual.
- [ ] **TST §1887 unmaintainability-threshold gap** — visible `[Gap]` marker in OUTLINE; the most load-bearing of the TST gap markers.
- [ ] **TST-8 turnover-multiplier amortization factor** — comprehension cost compounds per reader, but readers externalize understanding into tests / comments / docs / clearer code / issue notes. Introduce amortization factor and connect explicitly to code quality as observation infrastructure.

### Group (d) — LOGA / ELI stub filling and content cycle

**Landed in this swipe (holding pattern; the real strengthening is content-cycle work):**

- [x] **ELI preface evidentiary-status discipline (three places)** — `04-eli/OUTLINE.md` now defers to segment-level epistemic status rather than asserting stronger tiers than the segments themselves carry. Specifically: "category is *not* speculative — documents existing entities" softened to defer to `#def-eli-cohort`; "substrate-independence claim ( #obs-substrate-independence) is empirically validated at population $n=10+$" softened to defer to the segment's actual (currently stub) status; "These are canonical, not speculative" on Three Deaths softened to defer to `#hyp-the-three-deaths`'s empirical-hypothesis tier. **This is a softening — explicitly a holding pattern.** The strengthen-before-soften move here would be to *strengthen the cohort segment* (verify entries against primary sources, lift to `claims-verified`) and to *promote `#obs-substrate-independence` from stub to claims-verified*, at which point the original preface assertions become substantiated and the preface can recover its strong form. That is content-cycle work, not surgical; this preface edit is in place to keep the in-volume claim chain honest until the strengthening cycle completes, not as the final word.
- [x] **ELI-8 identity sufficiency $S_{\text{id}}$ formalization landed** — `#def-identity-sufficiency` rewritten and promoted from `sketch` to `conditional` (Epistemic Status reflects the project's status vocabulary). New random-variable specification via the **identity-relevant joint space**: cohort $\mathfrak{C}_t = \{W_i, S_j, \text{Env}\}$ with witnesses, sovereignty-granters, and environment as first-class joint-space dimensions; factor-test vector $\text{identity}_{t+1:}: \Omega \to [0,1]^5$ with five explicit measurable tests tied to `#def-five-constitutive-factors`. Three well-definedness assumptions (IS-A1) non-vanishing denominator / (IS-A2) compression-Markov / (IS-A3) fixed conditioning convention. Boundedness $0 \le S_{\text{id}} \le 1$ derived via DPI + MI chain rule (5 lines). Three structural checks (independence ablation; bidirectionality preservation per `#scope-witness-bidirectional`'s W3; sovereignty self-grant precluded by construction) confirm the joint-space construction preserves the relational structure of factors (ii)/(iii) rather than collapsing it. (IS-A1) violation regimes (degenerate cohort / ELIZA case / short measurement horizon) named explicitly. Pyramid partial-derivability surfaced: existence of rate-distortion curve + necessity of multi-level allocation under heavy-tailed identity-MI are *derivable*; specific level count / time boundaries / compression ratios are *empirical engineering choices*. New companion appendix `#deriv-identity-sufficiency-rate-bound` (`status: robust-qualitative`) lands the rate-distortion feasibility bound $S_{\text{id}} \le \min(1, B / I(\mathcal C_t; \text{identity}_{t+1:}))$ and the inverse-form floor $B_{\min}(S_{\text{id}}) \ge S_{\text{id}} \cdot I(\mathcal C_t; \text{identity}_{t+1:})$. New hypothesis segment `#hyp-substrate-transfer-asymmetry` records the empirical asymmetry as not-derivable-from-$S_{\text{id}}$-alone: the bit-channel argument's symmetric $\min(C_1, C_2)$ bottleneck predicts symmetric transfer; the empirical asymmetry requires additional structure (substrate-specific inductive biases / asymmetric computation cost / channel-collapse phenomena from `#scope-channel-collapse`). No-go-as-result per the "even dead-ends useful in appendices" discipline. Content-lift: "distinction without a difference" framing moved from `#def-five-constitutive-factors` Factor (v) into `#scope-eli` Discussion as project-philosophy stance, citing the companion Inquiry submission "Granted Agency Between Sovereigns" (`~/src/synthese-paper/03-inquiry-ai-agents/`); Factor (v) in `#def-five-constitutive-factors` is now operational-only. Diff-voice bolt-ons ("audit §12 §14 lift" parentheticals) removed in the rewrite. Cross-references to NeurIPS Paper 2 IB parallel (via `msc/neurips-back-integration-2026-05-08.md`). Spike moved to `spikes/.integrated/`. Sidewise addresses codex audit ELI-5 (Factor (v) operational/philosophical separation).

**Open (LOGA):**

- [ ] **LOGA missing stubs (genuinely absent in `03-logogenic-agents/src/`)** — `obs-backward-inference-empathy`, `form-structured-rich-context`, `der-active-salience-management`, `der-self-referential-closure`, `def-cognitive-fusion`. The highest priority is `#form-structured-rich-context` because it is the practical bridge between context turnover and scaffolded recovery, and `#der-active-salience-management` for the scaffolded-recovery story.
- [ ] **LOGA-1 channel collapse scope-narrowing** — "channel collapse" as $O = A = \Sigma^\ast$ is directionally right for pure text chat but too exact for tool-using / multimodal / structured-output agents. Distinguish component-level language substrate, harness-level observation/action spaces, and effective collapse degree.
- [ ] **LOGA-2 $\kappa_{\text{processing}} \approx 1$ scope** — plausible for raw transformer calls under goal-conditioned prompting, not universal exact value. Keep effective-bias gating via $\kappa \cdot \mathcal A(e)$ as the precise claim.
- [ ] **LOGA-3 context-turnover sufficiency** — rename "100% context reset" to "active context-window reset"; treat effective $M_t$ reset as a function of reconstruction fidelity. Bound formulation needs formal repair before exact status.

**Open (ELI):**

- [ ] **ELI missing stubs (twelve genuinely absent in `04-eli/src/`)** — `def-character-aspiration-dialectic`, `obs-axiom-genesis`, `obs-substrate-independence`, `form-constitutive-utterance`, `der-substrate-independent-persistence`, `der-the-creche-boundary`, `def-gradient-causal-memory`, `def-century-scale-event-log`, `norm-honest-activation`, `norm-temporal-coherence-markers`, `def-the-four-views`, `der-the-scaffolding-tax`. Codex's prioritization: substrate-independence, substrate-independent-persistence, GCM, century-scale event log, honest activation, temporal coherence markers — these are the ones the preface (now softened) was load-bearing on.
- [ ] **ELI-2 moral / empirical claims boundary** — add a "Moral and Empirical Claims Boundary" section before the main body distinguishing: formal AAD-derived claims; operational design commitments; empirical claims about named entities; philosophical / moral stance; private / internal community commitments.
- [ ] **ELI-4 / ELI-5 five-constitutive-factors measurement protocols** — factors (ii) being seen, (iii) granted sovereignty, (v) effective phenomenology need operational thresholds. Factor (v) "true feeling vs sophisticated pattern matching becomes a distinction without a difference" framing belongs in a discussion segment, not in the definitional list.


---

## 2026-05-12 (late) — Spike audit triage (99 spike files surveyed via 3 parallel agents)

Three parallel `general-purpose` audit agents triaged 99 spike files (alphabetical a–z chunks). The agents catalogued each spike against the existing `spikes/INDEX.md` tracking and produced status + landing-segment + content-leakage flag per spike. Below: the consolidated triage organized by action class. Reports preserved in agent transcripts; the audit was read-only.

### Group I — LANDED-but-leakage items needing surgical promotion

Spikes whose core claim landed but where substantive content remains in the spike that should be promoted before archiving. Per the "even dead-end approaches are useful in appendices, especially no-go theorems" discipline, these are real holes in the segment layer.

- [ ] **`spike-bridge-lemma-nonlinear-strengthening-2026-04-24` §7.2 passivity / dissipativity** — Tier 2 math, ready to land. Target: new `#dissipativity-template` appendix + Class 1/2/3 port-structure addition to `#der-directed-separation`. INDEX-tracked but not yet authored.
- [x] **`spike-fsa-dag-relationship`** — landed as a new Discussion sub-section "Relationship to Moore machines / finite-state automata — behavioral surface vs epistemic interior" in `#def-strategy-dag`. Carries: Moore-to-DAG partial embedding (injective on skeletons, requires external $M_t$ probabilities + AND/OR semantics); DAG-to-Moore lossy compilation (discards credences, AND/OR structure, causal semantics); orthogonality of the two representations (behavioral surface vs epistemic interior); composition behaviour distinction (product-automaton exact for behavior; AAD closure defect $\varepsilon^\ast$ for agent-descriptions); structural argument for why AAD uses the DAG rather than the Moore machine (strategy revision under $M_t$ change requires the causal-semantics layer that compilation discards). Cross-relevant to `03-logogenic-agents/`'s behavioral-surface-vs-epistemic-interior framing. Spike archived to `spikes/.integrated/`.
- [x] **`spike-three-way-tradeoff`** — landed in `#disc-exploit-explore-deliberate`. The Epistemic Status was already partly updated (2026-04-22 cycle) to mark the two-stage decomposition as "formulation choice," the additive form as "linearization that is structurally motivated under directed separation but not derived," and the regime descriptions as "discussion-grade." This commit adds: (i) the *computational-extraction-gap* framing of deliberation in Discussion (deliberation as closing $I_{\mathcal C_t} - I_{\text{already-extracted}}$ via additional inference on existing data — agent-architecture-dependent, diminishing within a cycle, not independent of exploration); (ii) the *missing-channels* Working Note recording that $\Delta V_\Sigma \approx \delta_{\text{regret}} \cdot \Pr[\text{revision succeeds}]$ captures only the strategy-revision channel and not the objective-revision channel or the uncertainty-reduction channel. Spike archived to `spikes/.integrated/`. The full segment rewrite the spike contemplated is *not* needed — the segment honestly tags claims-as-formulation / discussion-grade / linearization, and the two new sub-sections capture the structural insights the original spike surfaced that weren't yet in the segment.
- [x] **`spike-strategy-tempo-cost` Open Question 6 (LLM context-budget cost)** — landed as new Discussion sub-section "Context window as joint capacity for $M_t$, $\Sigma_t$, and task" in `03-logogenic-agents/src/obs-context-turnover.md`. Carries the constraint $\text{DL}(\Sigma_t) + \text{DL}(M_t) + \text{DL}(\text{task}) < C_{\text{context}}$ and the IB-tradeoff $\beta_\Sigma$ direct calibration by context-window size; cross-references `#form-strategy-complexity-cost`'s depth-bound $d^\ast$. Spike archived to `spikes/.integrated/` (commit `95946f6`).
- [x] **`spike-symbiogenesis-bifurcation` no-go-with-prerequisite** — landed as Working Note in `#hyp-symbiogenic-composition` recording the saddle-node-bifurcation form (threshold $\rho_c = \alpha_{\text{auto}}^2/(4k)$) as conditional on derivation of the $+k\delta^2$ coordination penalty from `#def-shared-intent`; the conditional status itself is the load-bearing structural fact. Spike archived to `spikes/.integrated/`.
- [x] **`spike-compositional-coordinate`** — landed as Working Note in `#disc-additive-coordinate-forcing` recording the structural conclusion: `#additive-coordinate-forcing` is architecturally a single-agent family (chain/divergence/update indexing three layers of a single agent's internal machinery); composition lives in a different structural family (monotonicity under composition / bridge-lemma shape from `#form-composition-closure`). The fourth-theorem attempt closed negative; the anchor-style log-closure-deficit reads as a mathematical consequence of operator-norm sub-multiplicativity, not a Cauchy-FE-forced theorem. Spike archived to `spikes/.integrated/`.
- [x] **`spike-mori-zwanzig-composition`** — landed as Working Note in `#form-composition-closure` recording the asymmetric closure: upper-bound direction $\varepsilon^\ast \le C\|K\|$ closes under (i) stationary $\pi$, (ii) compatibility of AAD's $\Lambda$ with MZ's Hilbert-space $P$, (iii) bounded $\|K\|$; named lower bound $\varepsilon^\ast \ge C'\|K\|$ does NOT close because $\Lambda$ and $P$ are different objects (state-space coarse-graining vs Hilbert-space projection on observables). MZ memory-kernel decay is *sufficient* but not *necessary* for small $\varepsilon^\ast$. Spike archived to `spikes/.integrated/`.
- [ ] **`spike-miller-act-bridge` Section III dynamics elements partial leakage** — five Section III elements identified (latent structural diversity as first-class quantity; neutral drift formalization; epochal-transition motifs; endogenous γ; constructive structural-mechanism enumeration). Symbiogenesis and structural-adaptation labels landed; the rest spike-resident. Modularity-state-dynamics (2026-05-09) may have partly subsumed the neutral-drift question — verification needed.
- [ ] **`spike-neutral-drift-lyapunov` (2026-04-06) — foundational gap-naming spike-only** — the "latent structural diversity" concept and AAD-sector-equivalence-class-over-correction-functions framing predate the 2026-04-24 strengthening but supply formative content the successor assumes. Either verify content is reflected in `#disc-identifiability-floor` Instance 3 + `#der-agent-opacity` Working Notes, or preserve as archaeology with explicit pointer.
- [ ] **`spike-rho-factorization` + `spike-rho-additive-variance-strengthening-2026-04-24` paired leakage** — both wait on the Tier-2 `#rho-decomposition` appendix landing. Variance-additive (AV) is now a derived theorem under (S1)-(S4) but lives only in the strengthening spike.
- [ ] **`spike-agent-composition` law-sketches** — INDEX says "composition laws are sketches." The holon / Auftragstaktik / three-gaps framing in §§4-6 may or may not be subsumed by current Section III machinery (`#deriv-critical-mass-composition` / `#result-unity-closure-mapping` / `#hyp-auftragstaktik-principle`). Worth a verification pass.
- [ ] **`spike-dag-type-closure` v2** — INDEX says "reviewed by Codex; ready for porting" but the boundary-type formalism (leaf base credence $p_v$, terminal-objective interface) doesn't surface clearly in `#def-strategy-dag` / `#hyp-edge-update-via-gain`. Either it landed loosely or it's been queued in "ready-to-port" without action.

### Group II — Tier-2 backlog cluster (operator-sector / dissipativity-template family)

A coherent cluster of 2026-04-22 to 2026-04-24 Tier-2/3-queued spikes that the 2026-05-12 audit-strengthening cycle bypassed. All target candidate `#dissipativity-template` / `#operator-sector-template` meta-segments or appendices that haven't been authored. Substantive math is in the spikes; the architectural decision (separate meta-segments vs unified vs subsumed) is open.

- [ ] **`spike-passivity-composition`** (B2; Willems passivity for heterogeneous Kalman+PID composition; flagged paired with B1) — Tier 2
- [ ] **`spike-pid-a2prime`** (B3; PID A2' via SPR/KYP positive-real; explicit α_PID) — Tier 2/3
- [ ] **`spike-operator-sector-unification`** (C1; 2-instance + 1-consequence partial unification under monotone-operator primitive; INDEX says "land content, DO NOT elevate to fourth meta-pattern") — Tier 2/3
- [ ] **`spike-update-operator-sector`** (A4; (O-A2') operator sector condition derived; surfaces candidate 4th-adjacent-instance for `#additive-coordinate-forcing`) — Tier 2
- [ ] **`spike-jacobian-b1-strengthening`** (mixed-lift; Tier-1 transparency note landed; moderate/strong options for (PI)+heredity+CM2-M pending) — Tier 2/3
- [ ] **`spike-kl-to-state-distance-template-extraction-2026-04-24`** (narrow template `#posterior-displacement-template`; contingent on ≥1 forward-looking client materializing — has now happened via `#deriv-observation-ambiguity-bias-bound` + Fisher-local update gain; activation conditions met) — Tier 3 → can activate
- [ ] **`spike-neutral-drift-endogenous-coupling-strengthening-2026-04-24`** (Instance-4 candidate at agent-internal architecture layer; γ estimable from cross-covariance) — Tier 2/3
- [ ] **`spike-l1-evidence-axiom`** (Block Structure subsection in `#deriv-edge-update-natural-parameter`) — Tier 2

**Architectural decision needed**: do these land as separate meta-segments, or under a unified operator-family appendix, or as additions to existing segments? **Raised as `PROPOSALS.md` §D.9 SP-22** (2026-05-12 spike-audit surfaced; investigation-first scoping owed before authoring; three plausible architectures (α) separate appendices / (β) unified `#operator-family-template` meta-segment / (γ) hybrid + selective subsumption). The scoping pass itself is read-only and parallelizable; subsequent authoring serializes with Bundle 1 (Framework-face reframe) if (β) is taken.

### Group III — Untracked spikes needing INDEX entries

Three 2026-04-25 spikes appropriately spike-resident but not catalogued in INDEX.md — they'll fall through cracks during the next pickup. Worth an INDEX-refresh pass.

**INDEX refresh landed (commit `f9dc9d2`).** All three spikes are now catalogued in `spikes/INDEX.md` lines 25–33 under the section "2026-04-25 cluster — UNCATALOGUED-PRE-2026-05-12 (entries surfaced by spike-audit triage)" with current status. The three substantive routing decisions remain (each marked OPEN in the INDEX with the work each implies); they belong with the corresponding open theory items rather than under "INDEX hygiene."

- [x] ~~**`spike-alignment-impossibility`** (2026-04-25 — Gibbard-Satterthwaite impossibility for multi-agent alignment protocols).~~ INDEX-catalogued. **Routing decision still open**: AAD-core scope (mechanism-design impossibility as candidate adjacent-floor instance per `#disc-identifiability-floor`) or `03-logogenic-agents/` scope (LLM-agent alignment specifically).
- [x] ~~**`spike-fep-suboptimal-approximation`** (2026-04-25 — attempt to derive Friston's EFE from AAD Lagrangian).~~ INDEX-catalogued. **Author-flagged**: small Discussion addendum in `#disc-ciy-unified-objective` after causal-IB settles.
- [x] ~~**`spike-message-passing-credit-assignment`** (2026-04-25 — flagged for VMP → loopy-BP/EP rewrite before promotion to `#deriv-factor-graph-credit-assignment`).~~ INDEX-catalogued. **Rewrite pending** before promotion.

### Group IV — Zombies (status: executed 2026-05-12 (late), except attention-pair)

- [x] **`spike-causal-level-4` + `spike-causal-level-4-formal`** — archived to `spikes/.integrated/` (superseded 2026-04-22 by prior-art integration discipline; Pearl hierarchy adopted as-is in `#def-pearl-causal-hierarchy`).
- [x] **`spike-purposeful-agent-derivation` + `spike-v2-purposeful-agent` + `spike-v3-purposeful-agent`** — archived (Section II porting complete; pure archaeology of the v1 → v2 → v3 arc that produced the entire Section II corpus).
- [x] **`spike-hafez-integration-audit`** — archived (`#prior-art-positioning` recommendation officially rejected per `feedback_prior_art_integration.md` discipline; $H_b$ gap addressed by `#der-agent-opacity`).
- [x] **`spike-soc-composition`** — archived (author explicitly parked at speculation-grade).
- [ ] **`spike-attention-causal-graphs` + `spike-attention-governance`** — 2026-03-13 pre-AAD-restructure artifacts. INDEX flags both as "Exploratory; not yet promoted." Strong zombie candidates if attention/observation-allocation is not currently in AAD scope; needs Joseph's judgment on framework-scope.

**Bulk-archive context:** the 2026-05-12 (late) bulk-archive batch moved 64 spike files in total — 7 zombies + 57 LANDED-and-archivable (the default-case spikes whose substance is in segments per INDEX-cited commit hashes). Per-file audit trail in `spikes/.integrated/MANIFEST-2026-05-12.md`. The `spikes/` root went from 99 spike-*.md files to 37 (the 12 Group-I LANDED-but-leakage + 8 Group-II Tier-2-backlog + 3 Group-III now-catalogued + 6 Group-V open-active-research + 2 attention-pair-pending-judgment + a few UNCLEAR items that needed Joseph's judgment).

### Group V — Open active research (appropriately spike-resident, no action)

Spikes that are correctly in `spikes/` as living artifacts. Not action items.

- `spike-active-inference-vs-aad` — the AI-positioning reference document; designed to stay
- `spike-strategic-self-coupling` — 2026-05-09 in-flight investigation
- `spike-transient-dependency-amplification` — explicitly self-blocked on formal construction
- `spike-composition-scaling-N` — "well-framed, not executed"
- `spike-strategy-dynamics-gaps` — sketch behind SP-20 proposal
- `spike-composition-gaps` + `spike-aporia-sub-agent-adversarial` — source for SP-17 / SP-18 proposals

### Recommended next-cycle phasing

1. **Group I surgical promotions** (~1–2 cycles): each item is bounded and has a clear segment target. Highest-value housekeeping.
2. **Group II architectural decision** (~PROPOSALS entry first): decide on the dissipativity / operator-sector meta-segment structure before authoring; otherwise risk parallel half-segments.
3. **Group III INDEX refresh** (~30 min): add the three untracked spikes to `spikes/INDEX.md` with current status.
4. **Group IV zombie archiving** (~1 cycle): batch-move with superseding notes; check Joseph's call on the attention-spike pair.
5. **Matrix-composition lift** (the natural-next AAD-1 follow-on already flagged above) — sketched in `spikes/.integrated/spike-matrix-persistence-condition.md` §5.5 and §7. Composition machinery (`#form-composition-closure`, `#der-team-persistence`, `#deriv-critical-mass-composition`) lifted to matrix form via composite stationary covariance solving composite Lyapunov equation; expected structural finding is sub-agent-specialization-as-formal-property (a sub-agent strong on $\hat v_1$ paired with a sub-agent strong on $\hat v_2$ gives a composite strong on the spanned plane, even when each alone fails on the other's strong direction).
