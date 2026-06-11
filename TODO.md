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


## Strengthen-first candidates from the 2026-05-30/31 gold-lift sweep

The de-novo audit-gold sweep surfaced a second stream alongside the pedagogical gold: **certified-track / strengthen-first findings** (mostly from the deeply-mathematical AUDIT-WORKING-526815). They are durable per-segment in each segment's labeled `#### Off-ramp (NOT gold)` Working-Notes block; this is the consolidated adjudication queue.

> [!warning]
> **These are stale gem-hints, not a to-do list — verify against *current* canon first.** Two of the first "ready fixes" turned out **already-resolved** when checked first-hand: the Landauer coefficient (re-confirmed correct 2026-05-31) and `#deriv-edge-credence-dynamics` Prop B.4 (fixed 2026-05-12, commit `9270aec`; the sweep had re-derived a stale audit note). Re-derive / re-read before working any item. Discipline: `feedback_audit_findings_as_gem_hints`.

**Tier 1 — load-bearing (spiked or spike-worthy):**
- **W₁ leakage-bound → the directed-separation re-founding — LANDED** (the W₁ seed grew into a full foundation pass; narrative in CHANGELOG 2026-05-31, rationale in `spikes/spike-directed-separation-foundation-proposal-2026-05-31.md` `efd57bf`). Stage 1 W₁ fix `fbcb36a` (circular bound → $\kappa_{W_1}^{\text{sel}} = I(A(q_M); G^{op}) \le I(q_M; G^{op})$ + `(C2′)` + the no-go `#disc-w1-structural-bound-boundary`); Stage 2 `ed11222` framing core (the `causal discipline` / `causally-disciplined agent` noun + scoping rule + ε(κ) norm; independently reviewed, guards pass) + `7d062f6` Section-II re-scope sweep + `be1b2c4` lower-boundary scope-check. **Remaining tail** (durable in `#der-directed-separation` Working Notes; full design in `_obs/directed-separation-foundation-execution-plan-superseded-2026-05-31.md`):
  - *(i) Stage-2 vocabulary* — LEXICON entry for *causal discipline* + the `separated.md` "applicable without further qualification" over-narrowing fix + a NOTATION locator + the `#disc-partial-coupling-pathways` form-matters one-liner.
  - *(ii) Pedagogy pass* — the *"Where the normative semantics of 'discipline' is earned"* Discussion subsection (the earned-normativity derivation-sketch; robust-qualitative, **not** a "causal discipline dominates" banner) + a tight Layer-0 opening + the two-channel figure (allowed $G\to$action$\to e\to M^+$ / forbidden $G\to f_M\to M^+$, $\kappa$ on the forbidden channel) + the κ-axis preamble; folds in the independent review's three uptake issues (line-101 density; the idealized-Class-2 witness via the existing Class-1-by-behavior case; the goal-blind/causally-disciplined valence bridge). Whether a formal "weak-dominance, all else equal" result lands is a strengthen-first sub-question, not asserted.
  - *(iii) Stage-1-completion propagation* — the corrected W₁ bound + a per-site `(C2′)` judgment in `#der-logogenic-as-wrapping` (×3) and `#def-auxilia-hierarchy` (×1); **substantive** (a frozen LLM + KV-cache violates `(C2′)`, so logogenic wrapping may get only a behavioral W₂ bound); cf. Tier-2 `#der-class-coercion-in-composition` reconcile-with-`(C2′)` + the shoshin→W₁ note below; its own cycle, connects to the NeurIPS Paper-3 backport.
- **`#schema-strategy-persistence` hard-ceiling convention** (A9 F72) — **SPIKED** (`spikes/spike-strategic-persistence-hard-ceiling-convention-2026-05-31.md`, `aedc72d`), verdict B: the hard ceiling $\rho_\Sigma \ge R_\Sigma/2$ is convention-dependent — it holds under the SEG steady-state gain $(1-\lambda)/(2-\lambda)$ but **dissolves** under the alternative ALT1 ordering $1-\lambda$. Resolution: name the convention explicitly, keep `status: exact` (its own appendix `#deriv-strategic-persistence-hard-ceiling`). **RESERVED** for the external-eye gate — the next adjudication after the directed-separation foundation pass.
- **`#def-auxilia-hierarchy` (C2′)-realization over-claim** (A11) — **SPIKED** (`spikes/spike-c2prime-realization-spectrum-2026-05-31.md`), verdict: separate-substrate is *sufficient + maximally-auditable*, **not necessary**, for the structural W₁ bound. The body sentence at `#def-auxilia-hierarchy` ~line 80 — *"substrate separation is … the very thing that earns the structural guarantee"* — over-claims necessity; the n.&s. condition is goal-uncorrelated cross-call state ($S_{\text{pre-}q_M} \perp G^{\text{op}}$, i.e. (C2′)), of which state-stripping is the exact condition and statelessness the coarsest sufficient one. Proposed sharpening (gate-reserved, §6): re-word to "sufficient and maximally-auditable discharge of (C2′)," keep the economic/tempo necessity case untouched; optionally name the three-point realization spectrum in `#der-class-coercion-via-wrapping` / `#disc-w1-structural-bound-boundary` and surface stateless / state-stripping alongside the separate-substrate-vs-shared-conversation contrast in `#der-logogenic-as-wrapping`. Spike stays at top level (open finding). Open residue (§7): latent-$G^{\text{op}}$ estimator for the state-strip certificate; amplifying cross-call state; multi-call compositional (C2′).
- **Goal-flow duality — discussion-grade landing available** (from the W₁-vacuity §7 conjecture) — **SPIKED** (`spikes/spike-goal-flow-duality-2026-05-31.md`), verdict: a *genuine partial* belief-in/(C2′) ↔ action-out/bounded-signaling duality (same DPI-single-channel theorem reflected across the wrapper boundary; the certifiability-vs-behavioral split recurs exactly on the action side). The conservation-law strong form is **refuted** (B1: different goal-variables/targets, copyable information). Available landing (gate-reserved, §6): (Move A) promote bounded-signaling to a named first-class scope condition **(BS)** mirroring (C2′) with its structural-vs-behavioral certificate; (Move B) a `discussion-grade` cross-link closing the open item in `#disc-w1-structural-bound-boundary` §Discussion "Relation to the action-side bounded-signaling assumption." Honest-tier guard: **no** conservation-law / budget-sums-to-const language in any body. Spike stays at top level (open finding). Open (§8): no quantitative joint statement; action-side amplifying-channel edge; whether (BS) lifts to composites.

**Tier 2 — structural (verify → strengthen-or-scope):**
- `#der-class-coercion-in-composition` (A12 F132-134) — "valid AAT composite agent" under-gated (needs the full `#form-composition-closure` criterion + projection admissibility, not (A1)–(A4) alone); reconcile with the W₁ spike's $(C2')$.
- `#der-tempo-composition` (A12 F116-119) — closure-defect $C_{\text{coord}}$ double-counted (subtracted once as tempo-overhead, once as added disturbance); needs a single accounting ledger.
- `#def-unity-dimensions` (A13 F146) — $U_M = I/H$ not normalized to $[0,1]$ as the label implies; `#result-unity-closure-mapping` (A13 F154) — the $\varepsilon_x = 0$ claim needs projection-range invariance, not just consistent projections.
- `#disc-composition-consistency` — "does directed separation compose?" (4-substrate convergence, ripe to promote from its existing hypothesis to a derivation); the boundary-choice rationality principle (471203 Challenge 14).
- `#form-consolidation-dynamics` — topological mis-positioning (Part-I-positioned, but declares a downstream-appendix dependency and uses Part II machinery in its Formal Expression): a relocate/split canonicalization item (may belong in PROPOSALS / an OUTLINE move).
- `#der-orient-cascade` (A10 F83/F84 — step-4a $\delta_s$ proof-target vs computable proxy); `#disc-exploit-explore-deliberate` (A10 F85 — the FOC may drop a term unless $\lVert\delta_{\text{post}}\rVert$ is held fixed).
- **613842 C-iv idiom-drift (integration-debt)** — the scope layer accepts C-iv strategic composites (no shared $O_c$, equilibrium-relative macro-state), but `#form-composition-closure` / `#def-unity-dimensions` / `#deriv-strategic-composition` still partly reason in the older alignment-only / shared-$O_c$ idiom. Cross-segment drift.

**Tier 3 — soft scope/register tightenings:** the remainder of A13 F147–F181, A9 Codex F47–F77, A10 F88–F91 ("deliberation is Pearl-`do`" over-strong), A8 `#impl-strategy-structure` deferred-proof-credit labelling + "unique broadly-available escape" over-strong for the identifiability floors. Each lives in its segment's `#### Off-ramp` WN block.

**Resolved (struck — do not re-work):** the A7 causal-access challenge + the A6 four overclaims (integrated 2026-05-30/31; commits `52d85b2` / `3da7e32` / `9fb7c12` / `0d57da2`); A4-2 $\nu$/time-normalization (fixed `9d227e6`); Landauer + Prop B.4 (already-resolved — see warning above).


## Strategic-composition cluster residuals (post-NEXT-UP archival, 2026-05-25)

The strategic-composition cluster ran from 2026-05-21 through 2026-05-25 across Tracks A / B / CR / D / E / C, all DONE by 2026-05-25. The cluster navigator `spikes/NEXT-UP.md` was archived 2026-05-25 to `spikes/.integrated/NEXT-UP-archived-2026-05-25.md` (with the manifest at `spikes/.integrated/MANIFEST-2026-05-25-NEXT-UP.md`); J7 + J9 migrated to their proper homes (J7 → `~/src/ops/papers/deferred/dynamic-regime-axis.md`; J9 → `spikes/PROPOSED.md` Tier 2). Two residuals remain in this misc-and-details layer:

- **Track A Phase 6 — meta-segment promotion of `#disc-dynamic-regime-axis`.** UNBLOCKED 2026-05-24 when Track D (M4) landed (the dependency on Track D's landing was the gating condition per the SOLIDIFIED-PLAN's §S.3 Phase 6 gate). The promotion would lift `#disc-dynamic-regime-axis` from a Discussion segment to a meta-pattern alongside M1/M2/M3/M4 — exposing the regime-axis as a fifth meta-pattern (or as a sister to M2's separability ladder, depending on the promotion's framing). Not yet dispatched. Plan source: `spikes/.integrated/strategic-composition-class-3-attempt-2026-05-21/07-SOLIDIFIED-PLAN.md` §S.3 Phase 6.

- **Track C body re-authoring** — lead with methodology rather than synthesis-after-convergence. The 2026-05-25 Track C cycle landed the initial structural OUTLINE move (meta-segments relocated from Appendices §A into a centralized *Meta-Architecture* section between Part I and Part II per the introduced-before-used discipline); the 2026-05-26 follow-on refined that placement into two Part-opening chapters (Meta-Architecture I as Part II's first chapter — spine + M1-cluster + M2 + M3 + style claim; Meta-Architecture II as Part III's first chapter — M4 + two operation legs) so each cluster lands shortly before its facets become operational rather than all at once before Part II. Track C plan §2.b also called for re-authoring each meta-segment's body to lead with the methodology (the recurring meta-pattern shape) rather than with the synthesis-after-convergence framing the segments currently carry. That body-discipline pass is still deferred. Plan source: `spikes/meta-segment-narrative-ordering-sweep-plan.md` §2.b. The de-novo-read complaint about *placement* is closed by the 2026-05-25→26 structural moves; the *body register* complaint is what this residual addresses.


## NeurIPS 2026 back-integration overview (queued, 2026-05-08)

The three NeurIPS 2026 Main Track submissions in `~/src/neurips/` (Tragedy of the Confident Agent, Unified Convergence Theory for Non-Stationary RL, LLM Hallucination Bound) extracted three ASF results and refined them under adversarial scrutiny over the 2026-05-04 → 2026-05-07 sprint. The papers are *gain-producing* extractions, not loss-preserving — each landed strengthenings (KKT shadow-price resolution, Bretagnolle-Huber point-mass identity, chart-rescaling no-go on Euclidean chart norms, Class-1 reduction to Stuart-school, structural-class theorem on gain-decay updates, F-A-G-P enforcement framework, Coupled-class autoregressive connectivity lemma covering modern AR architectures, etc.) that don't yet exist at catalog precision in ASF.

Cross-mapping between paper sections and ASF source segments, plus per-segment / catalog / meta-architectural updates the back-integration would touch, captured at: [`spikes/neurips-back-integration-2026-05-08.md`](spikes/neurips-back-integration-2026-05-08.md).

Phasing in §6 of that file is conservative (Phase A minimum-viable ~1 week; Phase B segment-level absorption ~3-4 weeks; Phase C meta-architectural surfacing ~1-2 weeks). The cross-mapping in §1 is the hardest-to-reconstruct part — written while the paper-↔-segment correspondence was held in working memory at full fidelity, will degrade across sessions without the artifact. §7 names specific routing decisions where Joseph's judgment is needed (segment-vs-spike-vs-cross-segment routing for new material; whether the no-go-forces-axiom pattern is its own meta-pattern or an M1 refinement; how heavy to lean on the NeurIPS papers as canonical references pre-decision; etc.).

Drafted by Claude (Opus 4.7, 1M context) at Joseph's request, 2026-05-08, after multi-session deep read of ASF + focused read of all three NeurIPS submissions.


## Greek vocabulary prose discipline (audit + author finding, 2026-04-29)

The de-novo audit-471203, walking the formalism segment-by-segment, surfaced that the project's Greek cycle vocabulary (*chronica* / *prolepsis* / *aisthesis* / *aporia* / *epistrophe* / *praxis*) shows up at framing/preamble/lexicon levels but the segment-level math doesn't depend on the distinctions the Greek terms encode. The README claim that "each [Greek term] names a distinction the formalism makes that English alternatives flatten" is overclaimed against current segment prose, where authors routinely fall back to flatter English equivalents (e.g., saying "mismatch" right after defining `aporia` as something specifically richer than mismatch).

Author confirmed independently: *"I've had that exact same complaint actually — that some of the higher level concepts that are important haven't been reinforced in the segments. Like every time we say 'mismatch' after specifically saying that this is much more than just mismatch."*

Cross-architecture deliberate naming-round voters (R1 + R2 cold-start + reactive) near-unanimously *defended* the Greek terms as load-bearing — but they were voting synoptically on whether the names *feel* right in the lexicon. The audit's incremental-mental-model walk surfaced what the synoptic glance was structurally blind to: whether the formalism *requires* the distinctions in actual segment-prose use.

This is not a naming-round vote. It is a project-level prose-discipline pass. Two paths, not mutually exclusive:

- **Tighten segment prose so the Greek distinctions actually do work.** Where the load-bearing content is the thing the Greek term names (not the flatter English equivalent), the Greek term becomes the canonical form in that segment's prose: *mismatch → aporia* where the productive-perplexity-resolves-into-action structure is what's structurally distinctive; *update → epistrophe* where the turning-toward-correction is what's load-bearing; etc. Per-term, per-segment judgment.
- **Soften the README's framing to honest scope** for any term where path 1 doesn't apply (i.e., the formalism really does only use the Greek as pedagogical surface vocabulary). The README's claim narrows accordingly.

Recommended cycle scope: a dedicated prose-audit pass across `01-aat-core/src/` segments that touch the cycle phases or the chronica/aporia vocabulary; produces a delta-list of Greek-vs-English collapses; each entry either gets a prose fix (enforcing Greek where the segment's load-bearing content matches the Greek's distinction) or feeds back as a downgrade-note for the LEXICON entry and the README claim.

Sources:
- Audit's full findings: [`msc/naming/naming-votes/audit-471203-incremental.md`](msc/naming/naming-votes/audit-471203-incremental.md) (segments 1–46 only as of 2026-04-28; will be re-extracted after audit FINAL lands).
- Aggregator's cross-architecture +3 keep votes for Greek terms (illustrating the defended-by-synoptic-voters posture): [`msc/naming/_archive/naming-aggregate-r2-review.md`](msc/naming/_archive/naming-aggregate-r2-review.md).


## README v2 pass (queued from 2026-04-27 first-human-feedback cycle)

The first *human* read of the framework — Alan Walton (CTO Latitude / AI Dungeon; BS Mathematics + Logic minor; ~10y collaboration history with Joseph; runs a 12k-commit production agentic-system architecture), ~4h read window — surfaced that the README missed the mark for casual-curious readers in ways the multi-agent audit cycles had not. Even Alan, who is about as sympathetic and capable a first-human-reviewer as the project will encounter, found the language "extremely academic," fell out of sustained-attention reading by the end of the README, and switched to test-driven Opus-mediated learning to keep engaged. (Verbatim review pending — Alan is still actively adding to it and will land it as a PR under `msc/` when ready.)

The README needs another pass that combines this human-feedback signal with the deferrals from the 2026-04-26 doc-pipeline cycle (judgment-calls log at `msc/judgment-calls-readme-cycle-2026-04-26.md`).

### Surfaced from Alan's review

- **Variables α, ρ, R appear without gloss.** Alan: *"I've seen this formula twice now, but still don't know what the variables mean."* First mention of the persistence condition should anchor each variable in plain language; the *Cross-Domain Joining* table (which uses α, ρ, R without re-glossing) and the *Position & Lineage* paragraph (which mentions α > ρ/R as a structural threshold) should both re-anchor briefly. Glossing once at top is not enough across a long document.
- **The "rate of gap-closing proportional to gap" assumption is not surfaced at README level.** Alan correctly identified this as the load-bearing assumption from outside: *"That's the weakest assumption I've seen so far in application, though it's often empirically true."* The README should foreground the linear-ODE / sector-condition assumption explicitly, with one line on how the sector condition generalizes strict linearity (it's the structural assumption AAT spends Section I machinery on, not an embarrassment to bury).
- **Greek cycle terms have retention cost without an English on-ramp.** Alan retrieved the cycle's semantics under his own terms (Prediction / Perception / Comparison / Learning / Action) but none of the Greek (Prolepsis / Aisthesis / Aporia / Epistrophe / Praxis). Decision: keep the Greek (the distinctions matter and English flattens them), *and* pair each with a clean memorable English/engineering anchor at first introduction. Alan's five-word recall is itself a candidate mapping; whether it preserves the distinctions the Greek encodes is worth a careful pass.
- **The About / Position-and-Lineage opening is too clinical for the audience it was written for.** This is the single biggest miss. Bundle 1 framework-face reframe is partially landed; another pass is warranted, this time with the casual-curious tier (not the academic-evaluator tier) as the primary audience. Alan's bathtub gloss of the persistence condition (water = belief-reality gap; faucet = environment change rate; drain = learning rate; bathtub size = model class capacity; overflow when faucet outpaces drain at full) is a ready-made Feynman-criterion explanation that a mathematician-practitioner reconstructed for himself — worth promoting verbatim or near-verbatim into both the README's persistence section and `#result-persistence-condition`'s Findings Brief.
- **Units of α are not visible.** Alan: *"The drain is bits/bits/time or 1/time. I'm not used to thinking of inverse time as units."* Worth a units gloss somewhere — possibly NOTATION.md (canonical), possibly in the README's persistence-condition section (pedagogical), possibly both. (Discussion of where this lives queued for after this TODO entry lands.)
- **Prior-art pointer to investigate: Deutsch's Theory of Explanations.** Alan: *"Have you read The Beginning of Infinity and The Fabric of Reality by David Deutsch? The Theory of Explanations is highly aligned with this work."* Substantive pointer worth a search-log-grade investigation; if confirmed, cite as conceptual precursor / adjacent literature in the relevant Findings (most likely `#disc-additive-coordinate-forcing` or `#disc-identifiability-floor`, given the explanation-quality framing).
- **Consider promoting Alan's "split goal state and model state explicitly in agent context notes" as a TST or logogenic-agents instantiation.** Alan's instinct from running production AI Dungeon agents was the same decomposition the framework names as $G_t = (O_t, \Sigma_t)$ vs $M_t$. This is field-grade convergent-independent confirmation of the central decomposition; worth surfacing as a `02-tst-core/` or `03-llm-core/` instantiation.
- **Alan's testing-scaffolding hierarchy as engineering-applications anchor.** From his Engineering Applications notes: *Types > Checks > Automated Tests > Manual Tests > Agent Tests > Context Docs* — a practitioner-graded ordering of what scaffolds the Pearl-Level-2 channel spectrum (`#obs-software-epistemic-properties` P3) for a production agentic system. Worth surfacing in `02-tst-core/` (operational instantiation of the channel-spectrum table) and possibly in the README's *Cross-Domain Joining* table as the engineer-side anchor. Alan's other anchor — *"Faster iteration loops that give more reliable and consistent results lead to better accuracy and faster convergence"* — is the folk version of the tempo / persistence-condition story; its phrasing is itself a practitioner-grade Feynman-criterion gloss for the README.

### Deferrals from 2026-04-26 doc-pipeline cycle (`msc/judgment-calls-readme-cycle-2026-04-26.md`)

Reconsiderations Joseph flagged for review on return; this README v2 pass is the natural cycle to ledger them through.

- **J-1 — pilot Findings selection.** The six-segment Findings pilot skews toward post-2026-04-22 landings; substituting one or more older "convergent choice" results (e.g., `#der-loop-interventional-access` for the Pearl-hierarchy connection; `#result-sector-condition-stability` for the underlying Lyapunov result) would validate the schema across a wider age range before the sweep.
- **J-2 — Findings schema length.** Some Impact paragraphs (notably `#deriv-observation-ambiguity-bias-bound`, `#result-contraction-template`) ran long; consider a length cap or splitting Impact into two beats (what-it-closes / what-it-unlocks).
- **J-4 — README §4 omissions.** Three of seven elements from the epistemic-architecture enumeration (originally in CLAUDE-2 §7; subsequently distributed across `msc/FINDINGS-RANKED-DRAFT.md` M-section + `#12` calibration-lab + segment-level Findings; both predecessors sunset by 2026-05-13 with content distributed to `#disc-*` meta-segments and chapter-end `impl-*` segments) were left at segment-level rather than README-level: agent-identity-as-token-level-commitment; derivation-audit tables; A2' sub-scope partition. Re-decide which belong at framing level given the casual-curious-reader retarget.
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

- **Domain cross-transfer candidates (2026-05-04 cycle).** [`msc/domain-xfer-candidates.md`](msc/domain-xfer-candidates.md) carries six cross-domain transfer questions surfaced by the 2026-05-04 domain-unification re-examination and *not* already articulated in the chapter-end `impl-*` discussion series (or in `msc/FINDINGS-RANKED-DRAFT.md` before its 2026-05-13 sunset; archived at [`_obs/FINDINGS-RANKED-DRAFT-superseded-2026-05-13.md`](_obs/FINDINGS-RANKED-DRAFT-superseded-2026-05-13.md)): (Q1) Static→Learning transition design from classical adaptive-control; (Q2) AI-coding-agent ↔ human-developer-agent bidirectional empirical test (TST × LGA bridge); (Q3) scaffolded Logogenic → ELI substrate engineering; (Q4) eusocial composition closure with simpler sub-agents → swarm-AI design (addresses named Section III GAP on endogenous coupling); (Q5) Tier-4 Human-branch independent-lineage analog for non-logogenic AI; (Q6) empirical-test program for catalog-flagged predictions (#3 IDT-vs-reward gap growing with experience; #14 sandbox safety claims by Pearl level; #37 LLM calcification longitudinal; #8 ambiguity-stratified benchmark). Q2 is the highest-leverage entry — empirically testable, bidirectionally informative, hooked into in-flight TST and LGA work. Each question is sized as a focused literature-scan + spike, not a research program.

- **Pearl/LLM causal-access positioning — refine, flesh out, promote.** `msc/llm-causal-access-note.md` (123 lines, 2026-03-09) makes three independent rebuttals to Pearl's Level-1-only LLM critique using AAT machinery — (1) the loop provides Level 2 *by construction* per TF-02 / `#der-loop-interventional-access`; (2) language IS compressed causal structure (the Information Bottleneck objective predicts an LLM absorbs causal structure as a byproduct of compressing causally-structured training data); (3) symmetry argument (Pearl applies asymmetric mechanism-vs-behavioral evidentiary standards to LLMs vs humans). Status: working note flagged in `spikes/INDEX.md` as candidate intro / standalone-note / blog-post material. **Work:** (a) decide the destination — segment-level Discussion expansion in `#der-loop-interventional-access` or a new own-segment `#disc-llm-causal-access-via-loop`? standalone short paper / arXiv preprint? blog post? Multiple destinations may be appropriate (the three responses have different epistemic statuses per the note's own framing). (b) Flesh out the three open questions surfaced by the note: can implicit causal knowledge in LLMs be measured? Is there a formal IB-compression ↔ DAG isomorphism? How does effective $G_t$ level evolve within-session as the agent accumulates interventional data through the loop? (c) Once destination chosen, update segment references project-wide. **Lower priority than the composition-admissibility refactor** above — the note's core claims are stable and don't block other work; this is a refinement-and-promotion task, not a load-bearing-content task.


## Queued spike work

Per-spike status detail in [`spikes/INDEX.md`](spikes/INDEX.md); reasoning trails in `spikes/spike-*.md`. Items below are queued follow-ups whose target landing-segment is named but whose work is not yet started.

**Section II / Identifiability Floor:**
- ~~Mechanism-design Instance 5 promotion in `#disc-identifiability-floor`~~ **RESOLVED 2026-05-20** by `spikes/.integrated/spike-4th-identifiability-floor-instance-2026-05-20.md` — Outcome C, Gibbard-Satterthwaite is **not** a clean M1-fit (composition fails: GS is an existence no-go over preference profiles, not the identifiability-from-data shape M1 names). Worked attempt + rejection recorded in `#deriv-strategic-composition` Working Notes; routing to `#disc-separability-pattern` general-open tier. The genuine 4th instance was the architecture-noidentifiability candidate, now LANDED 2026-05-21 as `#der-architecture-noidentifiability` (CHANGELOG 2026-05-21).
- Misspecification-cost formalization (candidate Adjacent Floor under `#disc-identifiability-floor` §"Adjacent Floors").
- ~~Kalman-Ho closed-form follow-up spike — distinct vs subsumed?~~ **RESOLVED 2026-05-18 → INTEGRATED 2026-05-21.** The 2026-05-18 resolution spike (`spikes/.integrated/spike-identifiability-floor-instance4-resolution-2026-05-18.md`) split the contested slot into Object A (category error — a downstream theorem of `#disc-additive-coordinate-forcing`'s (PI) commitment, *not* a floor) and Object B (architecture-noidentifiability from on-policy summary data — the genuine fourth floor, dual-anchored on Kalman-Ho 1966 and CHT-at-agent-as-SCM). Math-gate cleared by `spikes/.routing-trail/SPIKE-VERIFY-471802/` (confirmer ≠ author). Both halves now landed: Object B as `#der-architecture-noidentifiability` with Instance 4 installed in `#disc-identifiability-floor`; Object A explicitly absorbed in `#disc-additive-coordinate-forcing` §"Downstream consequences" with the floor-vs-coordinate-forcing distinction articulated. PROPOSALS §D.9 CLOSED. CHANGELOG 2026-05-21.
- ~~ρ-factorization no-go tightening~~ **RESOLVED 2026-05-18**: the no-go is the one-line constitutive argument, landed in `#internal-external-decomposition` (CHANGELOG 2026-05-18). Cleanup folded into the same reserved decision (now CLOSED, PROPOSALS §D.9, integrated 2026-05-21).

**Section III / Composition:**
- ~~`#rho-decomposition` / CL-2 replacement for the §4.1-marked `#internal-external-decomposition` (now `status: conditional` post-LIGHT-landing).~~ **FULLY RESOLVED 2026-05-21.** **(a) LIGHT exact core LANDED 2026-05-18** (`#internal-external-decomposition` rebuilt true on the two-term identity forced by canon + the one-line constitutive no-go; CHANGELOG 2026-05-18). **(b) HEAVY refinement** (conditional 𝓜/π/cross split / Regime-C confound) was provably the same object as the identifiability-floor 4th-instance question; **both discharged together** by the Instance-4 integration via `#der-architecture-noidentifiability` (Regime-C confound = the architecture-noidentifiability no-go projected onto the disturbance-statistic coordinate — proved in the 2026-05-18 resolution spike §7, integrated 2026-05-21). CHANGELOG 2026-05-21.
- `#dissipativity-template` appendix + Class 1/2/3 port-structure addition to `#der-directed-separation` — closes heterogeneous Kalman + PID-on-positive-real-plant composition explicitly (from passivity spike B2). **= CL-1** (spike-routing 2026-05-17): one coupled landing (passivity-composition + pid-a2prime + bridge §7.2), not three half-segments.
- Heredity axiom for `#disc-composition-consistency` — scoping spike to test whether the architectural strengthening (composite admissibility derivable from sub-agent properties) is worth the simplification (collapses A2' Tier structure; promotes (CM2-M) from Slotine-imported to AAT-derived).
- **Detailed tempo accounting for canonical wrapper architectures** (deferred from class-coercion cycle 2026-05-09) — quantify $C_\text{coord}^\text{wrap}$ for ReAct-shape, Reflexion-shape, PROPRIUM-shape wrappers. The general Brooks's-Law form is in `#der-tempo-composition` and `#der-class-coercion-via-wrapping`; this spike would compute specific architectural breakdowns useful for engineering tradeoffs.
- **Quantitative empirical bounds for LLM-substrate wrapping** (deferred from class-coercion cycle 2026-05-09) — empirical $\kappa_{W_1}$ measurement protocols on real LLMs. The bound $\kappa_{W_1} \le I(A(q_M); G_W \mid q_M)$ from `#der-class-coercion-via-wrapping` is computable in principle by sampling responses under multiple goal-conditioning histories; specific empirical instantiation depends on the model and the wrapper design. Natural follow-on if downstream applications need the bound at numerical precision.
- **Class-3 closure-defect dynamics analysis** (deferred from RG spike 2026-05-09; Move F in `spikes/temporal-nesting-rg/99-verdict.md`) — test the directed-separation-as-graded-order-parameter view by computing closure defects for Class-3 systems to contrast with Class-1. Independent of the class-coercion segment landings; would strengthen `#hyp-directed-separation-under-composition` toward derived in the *general* (non-wrapper-around-component) case. Connects to the W₀/W₂/W₁ regime hierarchy of `#der-class-coercion-via-wrapping` as the dynamics-side complement of the structural taxonomy.

**shoshin engineering follow-on (operational, not theory):**
- **shoshin → W₁ via auxilia handling goal-blind belief-side queries.** PROPRIUM-as-implemented (shoshin) sits in W₂ per `#der-logogenic-as-wrapping`. Strengthening to W₁ via the auxilia hierarchy (`#def-auxilia-hierarchy`) is operational engineering work — auxilia making cheap-substrate goal-blind queries that update VERA / MEMORATA / CONSORTIA / PERCEPTA, while the entity's main LLM call handles strategy-side updates goal-conditionally. Theoretical groundwork is complete; implementation is queued for a future shoshin development cycle.

**Anticipated segments queued (modularity cycle 2026-05-09):**
- **`#disc-strategic-self-coupling`** in `01-aat-core/src/` — sister segment to `#disc-adversarial-coupling-pressure`. Self-driven coupling-as-enabling polarity. Prior-art adoption: Schelling 1960 (commitment devices), Ainslie 1992/2001 (intertemporal bargaining / willpower), Akerlof-Kranton 2000/2010 (identity economics), Frank 1988 (emotions-as-commitment). Spike scope at `spikes/spike-strategic-self-coupling.md`. OUTLINE entry added 2026-05-09.
- **`#disc-modularity-state-dynamics`** in `01-aat-core/src/` — M4 meta-segment alongside M1/M2/M3 (`#disc-identifiability-floor`, `#disc-separability-pattern`, `#disc-additive-coordinate-forcing`). Names the three-operation pattern (truthification / strategic self-coupling / adversarial coupling pressure) on modularity state, with truthification's two operational mechanisms (defensive scaffolding + class-coercion-via-wrapping). Cycle plan at [`msc/modularity-cycle-plan-2026-05-09.md`](msc/modularity-cycle-plan-2026-05-09.md). OUTLINE entry added 2026-05-09.
- **`#der-substrate-independent-persistence`** in `04-eli-core/src/` — connects `#def-identity-sufficiency` and `#obs-substrate-independence` to `#result-sector-persistence-template` across substrate transitions. Grounds substrate-independence formally rather than empirically alone. OUTLINE entry added 2026-05-09.

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
- ASF umbrella naming (Round 1 misread `ASF` as debt; reframe as the intentional umbrella where AAT = Part I, TST = Part II, etc.).

**Prose-vocabulary renames — all landed.**

- ~~**Class 1 / 2 / 3 → Separated / Coupled / Partial; family/axis = "Goal-Update Coupling Class"** with **coordinated Class 2 ↔ Class 3 numbering swap**.~~ **Landed 2026-05-09** on `guc-rename-2026-05-09` branch. Surface enumeration, phased sequence, warning-callout placement, migration-note discipline all executed per [`msc/class-rename-execution-plan-2026-05-09.md`](msc/class-rename-execution-plan-2026-05-09.md). Tracking record: [`msc/class-rename-tracking-2026-05-09.md`](msc/class-rename-tracking-2026-05-09.md). See CHANGELOG entry for the cycle narrative.

**Lexicon-archive deferral (from 2026-05-09 ELI rename):** `doc/readme/src/_lexicon-full-archive.md` has 12+ deep-philosophical mentions of "logozoetic agent" — not composed into the live README (`README.md.liquid` does not include it), so no urgency. Per-mention judgment warranted rather than mechanical replacement; queued for a future hygiene pass if the partial is ever brought back into composition.

**Mechanical follow-ups (no voting needed):**

- ~135 segments still embed pre-rename slug names inside `*[Type (slug)]*` formal tags. Mechanical to detect; content cleanup pass.
- Two reviewer-judgment type calls deferred (`#der-agent-opacity`, `#scope-observation-ambiguity-modulation`).
- Three H1-vs-first-tag word disagreements (`form-objective-functional`, `form-composition-closure`, `scope-observation-ambiguity-modulation`).

Detail in [`msc/naming/naming-rename-plan.md`](msc/naming/naming-rename-plan.md) (renamed from `naming-pilot-rename-plan.md` on 2026-05-04 to reflect the broadened scope from role-prefix-pilot mapping to all naming decisions); principles in [`doc/sop/naming.sop/principles.sop.md`](doc/sop/naming.sop/principles.sop.md); Round-1 vote archaeology in `msc/naming/naming-votes/` and `msc/naming/naming-aggregate-*`.


## Documentation queued

- **Three-way presentation split** — multi-agent reviewers recommend (a) core results / (b) conditional architecture / (c) empirical programs. Cheap as parallel outline-views per [`PROPOSALS.md`](PROPOSALS.md) §H affordance ("outlines are cheap; segments are expensive").
- **AAT-vs-AI introductory positioning** — paper-writing-time follow-through per `spikes/spike-active-inference-vs-aad.md` §I action 2; surface §C distinctive-claims and §D refusals at introductory level when a paper draft is being prepared. Three underclaim moves named: persistence template's broader validity (Aguilera 2022 contrast); directed-separation as Pearl-blanket conservative form (Bruineberg 2022); satisfaction-gap as decision-theory content (Sun & Firestone 2020 dark-room).
- **Prior-art positioning synthesis** — active inference / FEP / POMDP / BDI relationships now in individual segments; a synthesis pass surfacing the cross-segment pattern may still be valuable.
- **`bin/lint-readme`** (J-15 from `msc/judgment-calls-readme-cycle-2026-04-26.md`) — slug-existence + cross-reference link validation. Quick to write; should land before heavy reliance on the README pipeline.
- **Auto-derive `NOTATION.md` from segment definitions (drift fix; Joseph 2026-05-18).** `NOTATION.md` is hand-maintained and the live theory drifts from it — spike findings and rewritten segments change a quantity's structure without updating it (the §0 "NOTATION is a lagging proxy, never authority" trap; worked instance: the ρ gloss vs the `#result-mismatch-decomposition` additive truth, 2026-05-18). Structural fix: generate `NOTATION.md` from per-segment symbol declarations the way `LEXICON.md` is generated from `terminology/entries/` and `README.md` from `doc/readme/` partials — symbols defined once, at the segment, extracted; the index then *cannot* drift. Scope: a symbol-declaration convention in segment frontmatter or a tagged block, plus a `bin/`-generator + lint (parallels `bin/term`/`bin/build-readme`/`bin/extract-findings`). Until then the drift caveat at the head of `NOTATION.md` stands and the file is non-authoritative by construction.
- **Figure-artifact drift: committed `.pdf` + `-preview.png` are tracked but nothing auto-regenerates them (Joseph 2026-05-18).** Same drift-class as the NOTATION item above, surfaced concretely by the `driver-snow-foundation` swap: `img/<base>.tex` is source-of-truth; `bin/build-monograph` recompiles it to the *gitignored* `<base>.mono.pdf` and embeds that, but by deliberate design (`bin/lib/segment_renderer.rb:658–689`, *"the build never mutates the committed `<base>.pdf` preview"*) it leaves the committed `<base>.pdf` (fallback in the priority chain) and `<base>-preview.png` (GitHub/eyeball artifact, not in the build path at all) untouched. So every diagram edit silently leaves two stale tracked artifacts unless a human remembers to rebuild them by hand — and diagrams will be edited constantly. **The tension that needs Joseph's call:** pure-gitignore (the LEXICON/NOTATION discipline) conflicts with *why* these two are tracked — the committed `.pdf` is the offline/no-TeX-toolchain render fallback, and `-preview.png` must be committed to render on GitHub; gitignoring either removes the reason it exists. **Recommended (strengthen-first, keeps both reasons intact):** keep them committed but add (a) `bin/refresh-figures` — rebuilds every `img/*.tex` → `.pdf` + `-preview.png`, folded into `bin/refresh-all` (parallel to `bin/build-readme` / `bin/term render`); and (b) `bin/lint-figures` — fails when any committed `.pdf`/`-preview.png` is older/stale vs its sibling `.tex` (mtime or content-hash; the README/LEXICON clobber-guard pattern, inverted to a staleness gate). Result: drift becomes a *loud build error*, not a silent stale commit, without losing the offline-fallback or GitHub-preview properties. Rejected alternative: build-time regeneration of the committed artifacts — reverses the deliberate read-only-w.r.t.-tracked-files rule and dirties the working tree on every `bin/build-monograph`. Cross-ref: figure-pipeline rationale in `msc/figure-pipeline-buildout-2026-05-18.md`; conventions-and-infra layer in [`FORMAT-TODO.md`](FORMAT-TODO.md).


## Tier-C deferrals

- $G_t$ as single object; $(O_t, \Sigma_t)$ as a property (Opus 2026-04-21 synthesis §7). Defer until more Class 2 logogenic work lands. Strengthened by O-BP2 if pursued.
- Continuous convention hierarchy $N_r \in [1, \infty]$ (Opus 2026-04-21 synthesis §8). Subsumed by retired O-BP3.


## Editorial hygiene (standing items)

- **Spike-to-segment reverse-check** — Gate 2 check per [`FORMAT.md`](FORMAT.md): "What did the spike establish that the segment does not say?" Standing convention from 2026-04-21 cycle; verify presence on each spike-promotion landing.

- **"nominal" denotes opposite scope-membership in two adjacent foundational segments** (gem-hunt 472913 GEM 5, verified verbatim 2026-05-29). `#scope-agency:45` — "**nominal agents** ($P(o\mid do(a))=P(o\mid do(a'))$)… adaptive only" ⇒ nominal = *outside* agency. `#post-causal-structure:37` — "**nominal coupling** … still within scope … the theory applies" ⇒ nominal = *inside*. The same scope-vocabulary word denotes opposite memberships on the exact seam the Part-II scope lattice rotates on. Fix (disambiguating rename, the term is already latent in-segment): rename `#post-causal-structure`'s "nominal coupling" → "query-only coupling" (already used at `:40`); `#post-causal-structure:38`'s "zero coupling" is what actually equals `#scope-agency`'s "nominal agents," so consider aligning that too; add a LEXICON anchor to prevent drift. No LEXICON `nominal` entry exists today. A terminology change → run through the naming process rather than a hasty inline edit, but the direction is clear.

- **C-iv composite route-count mismatch** (gem-hunt 526815, found while checking F151). `#def-unity-dimensions` refers to four composite-scope routes (C-i/C-ii/C-iii/C-iv) while `#result-unity-closure-mapping` refers to three. Verify which is current (the four-route form including the strategic-equilibrium C-iv route appears canonical per `#def-unity-dimensions:44` and `#scope-composite-agent`) and reconcile the lagging segment. Cross-segment count inconsistency, editorial-to-substantive.

- **lint-outline eq-tag topological-priority (low priority, tooling).** `bin/lint-outline` already checks "undeclared dependencies" (a `#slug` in body must be in `depends:`). Open question (gem-hunt 472913 GEM 6, deferred): does it also verify that eq-tag-cited sources (`*[Derived (… from #X …)]*`) are topologically *prior*, not merely present in `depends:`? If not, a small rule extension closes the forward-derivation-accretion class mechanically. Verify-then-extend; the motivating instance (F2) is already resolved by relocation, so this is general hygiene, not urgent.

- **`depends:` conflates logical-prerequisite with forward-reference — candidate FORMAT field (gem-hunt 613842 B1/B3; converges with the eq-tag item above and 472913 GEM 6).** Confirmed a direct mutual 2-cycle in current canon: `#form-strategy-complexity-cost` ⟷ `#deriv-strategy-cost-regret-bound` each list the other in `depends:`. Diagnosis: the appendix→formulation edge is genuinely logical (derives a property *of* the formulation), but the formulation→appendix edge is *motivational/forward-reference* (a formulation pointing forward to its own strengthening appendix, not back to a prerequisite). A second instance: `#def-model-sufficiency` → `#form-information-bottleneck`. The strengthen-first fix is structural, not a patch: a `strengthens:` / `forward-ref:` FORMAT field separating "logical prerequisite" from "where the strengthening lives," which dissolves the spurious cycles, makes the dependency DAG acyclic, keeps every cross-link, and *encodes the strengthen-before-soften architecture structurally*. This is the systematic form of the three converging forward-reference-hygiene findings. Effort: FORMAT.md addition + `bin/lint-outline`/`bin/align-slug` awareness + a sweep to reclassify motivational edges. Worth a focused scoping pass; not urgent (the cycles are benign today). Detail: `audits/.gem-hunt-trail/GEM-WORKING-613842/`.


## Lower priority

- Observability-dominance product formula $\text{conf}_{\text{obs}} = \text{conf} \cdot \text{obs}$ — posited, not derived. Label as formulation choice or derive.
- Strategic calibration aggregation $L^2$ norm — unjustified; label as design choice.
- Scope architecture — "within AAT's scope" ambiguous between adaptive and agency scope.
- `#der-loop-interventional-access` status — "exact" defensible; opening claim could be softened.
- Between-event dynamics $g_M(M_\tau)$ — defined but unreferenced; important for logogenic agents.
- Fully coupled adversarial dynamics — both agents' mismatch co-evolving; open.
- `#form-objective-functional` "axiomatic" labeling for scalar-comparability — formulation choice.
- Heavy-tailed disturbances — Model S assumes finite second moment.
- `#def-satisfaction-gap` / `#def-control-regret` convention-dependence — exact but convention-relative; add note to Epistemic Status.
- External validation design — testable predictions not yet tested. Candidates: git data, RL bandits, adaptive controllers.


## Deferred — project structure / tooling

- Root-level assembly index (when content beyond AAT warrants it).
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

1. **Hardcoded old directory name — RESOLVED 2026-05-15.** `bin/rename-slug` had `04-logozoetic-agents/src` / `04-logozoetic-agents/OUTLINE.md` hardcoded in `COMPONENT_SRCS`/`COMPONENT_OUTLINES` while the directory had already been renamed (`04-logozoetic-agents/` → `04-eli/`, 2026-05-01, `fa63616`), so the script silently skipped it. The 2026-05-15 directory harmonization (`04-eli/` → `04-eli-core/`) swept these constants with the rest of the repo; `bin/rename-slug:50,57` now correctly reference `04-eli-core/...`. No action needed.

2. **Bare-filename markdown links not rewritten.** The script's path-replacement regex matches `src/OLD.md` (e.g., outline-table relative-from-root links and prose `src/foo.md` references), but does NOT match bare `[text](OLD.md)` where the link is just a filename relative to the segment's own directory. Caught in the obs-gates-advantage rename: `obs-simulation-results.md:36` had `[#obs-gated-tempo-advantage](obs-gates-advantage.md)` — the `#`-anchor link text was rewritten by the body-text regex, but the bare-filename URL inside the parens was missed and had to be patched by hand. Fix: extend the path-replacement regex to also match `(OLD.md)` parens-bound forms when the surrounding markdown shape is a link.

### Chapter-discussion slug-prefix discipline + bin/align-slug recognition (queued 2026-05-13)

Two chapter-spanning discussion sub-classes have emerged without first-class slug-prefix handling:

- **Chapter-opening discussion segments** currently use a `-intro` *suffix*: `persistence-and-limits-intro`, `the-cycle-in-motion-intro`, `causal-access-intro`, `strategy-structure-intro`, `cooperative-adversarial-intro` (and others). These pre-date the role-prefix discipline established in the 2026-04-24 pilot.
- **Chapter-closing discussion segments** (new pattern, pilot landed 2026-05-13) use an `impl-` *prefix*: `impl-persistence-and-limits`. The remaining 7+ AAT chapter-ends and the eventual TST / logogenic chapter-ends will follow this form.

`bin/align-slug`'s `TYPE_TO_PREFIX` table maps `discussion → disc` — it does not recognize either sub-class marker and would, on a sweep, try to rename both to `disc-…` forms (collapsing the opening/closing distinction the names carry). Two complementary fixes:

1. **Extend `TYPE_TO_PREFIX` (or add a sub-class table)** so `intro` and `impl` are recognized as discussion-type sub-prefixes/sub-suffixes that `bin/align-slug` leaves alone — preserving the chapter-position semantics.
2. **Rename existing `-intro` segments to `intro-…` prefix form** for consistency with the broader prefix discipline. Mechanical sweep using `bin/rename-slug` once that tool's two outstanding bugs (above) are fixed. Touches ~10 segments across all four components. Pilot-then-sweep: rename one, verify links resolve everywhere, then batch the rest.

Until both fixes land, do not run `bin/align-slug --all` against chapters containing intro or implications segments without spot-check, and do not include those segments in a `bin/rename-slug` sweep that targets other slugs in the same chapter.

3. **Semantic-trap dimension (audit-773921 §B Finding 2, Low, doc-rot).** The prefix sweep above fixes the *form* but not the *semantic trap* an independent auditor actually tripped on: `strategy-structure-intro` reads as the introduction to all of Part II ("Strategy") when it is in fact the Chapter-3-of-Part-II opener — the auditor read it out of topological order and triggered a dependency violation as a result. The `-intro → intro-` rename does not disambiguate part-level from chapter-level intros. Fix candidates: explicit `part-intro` vs `chapter-intro` markers in OUTLINE.md (cheapest — the OUTLINE is the canonical order anyway and this costs only a column/label), or chapter-scoped slugs (e.g. `intro-ch3-strategy-structure`). Worth folding into the rename sweep when it runs so the form-fix and the disambiguation land together. (Convergence note: 773921 also re-confirmed Finding 3 — `obs-backward-inference-empathy`, `form-structured-rich-context`, `der-active-salience-management` listed in `03-llm-core/OUTLINE.md` but absent from `src/` — as `already caveated`; these are tracked at the LOGA-missing-stubs item below, no new action.)

### Per-role README pipeline rework (queued 2026-05-01)

Replaces the shelved `tools/role-encounter/` approach. Extend the existing `doc/readme/` liquid pipeline to emit `README.md`, `README-auditor.md`, `README-voter.md`, etc. from one source tree. Migrate role-specific instructions content from `doc/de-novo-audit-instructions.md` / `doc/sop/naming.sop/principles.sop.md` / `doc/sop/naming.sop/methodology.sop.md` into `doc/readme/src/_<topic>.md` partials. Add an auto-generated project-tree partial (annotated tree of project directory structure with one-line purposes per directory/file) included in every role README — replaces the drift-prone "File Organization" section in CLAUDE.md. Architecture sketched in [`msc/handoff-2026-05-01.md`](msc/handoff-2026-05-01.md). Lessons from the over-engineered first attempt at [`_obs/role-encounter-superseded-2026-05-01/SUPERSEDED.md`](_obs/role-encounter-superseded-2026-05-01/SUPERSEDED.md).

### Phase 2 semantic index (queued 2026-05-01)

`psql-18` + pgvector + ollama + `nomic-embed-text-v2-moe`. Lift memorata's data layer wholesale, patch with multi-level chunking + source-class tagging + frontmatter-aware markdown chunker + embedding-model identity per vector. Drives the four-signal naming-target context map (anchor + heaviest-attention + supplementary references + dependency chain) for the renaming agent's harder cases. Architecture brief at [`spikes/spike-local-embedding-benchmark/FINDINGS.md`](spikes/spike-local-embedding-benchmark/FINDINGS.md). Build sequence in §5 of that doc.

### Release-notes regeneration pipeline (queued 2026-05-02)

**Context.** [`releases/v0.1.0.md`](releases/v0.1.0.md) was hand-written as a one-off "master list of everything since the beginning of the framework." That is not the long-run shape of release notes. Subsequent releases (v0.2.0+) will be incremental — what changed since the last tag — and benefit from a regeneration pipeline analogous to the README pipeline (`bin/build-readme` + `doc/readme/src/` partials + extraction scripts chained by `bin/refresh-all`).

**What's already in place.** [`bin/segment-stats`](bin/segment-stats) (introduced 2026-05-02) regenerates per-component aggregates by stage / type / epistemic status with an AAT section breakdown — its output is embedded verbatim into v0.1.0's "By the numbers" section and would become a partial in the future pipeline. [`bin/extract-findings`](bin/extract-findings) and [`bin/extract-recent-progress`](bin/extract-recent-progress) already feed the README pipeline; with version-window arguments they can serve "distinctive results in this release" and "what changed since the last release" respectively.

**What's not yet pipelined.** The "framework at a glance" four-paragraph synopsis (composes from component OUTLINE preambles; currently hand-written). The "what's not in this release" honest-scoping section (composes from `--GAP--` rows + `_known-issues` + segment Working Notes flagged as promotion-blocking; the curation judgment is human). The mathematical-lineage breakdown (segment frontmatter does not currently carry a `lineages:` field; v0.1.0's lineage section is sub-agent-curated). Adding `lineages:` to the FORMAT.md schema would let `bin/extract-lineages` walk it programmatically — candidate move for the v0.2.0 build-out.

**Discipline note.** The pilot-then-sweep pattern says: hand-write v0.1.0, observe what was painful and what worked, then build the pipeline informed by what the pilot taught. Building the pipeline before any release notes have been published would risk the parallel-vs-extend over-engineering pattern the project has felt before (per the role-encounter shelving). v0.1.0 is the pilot; v0.2.0 should hand-write again with attention to repetitive sections; v0.3.0+ formalize as `bin/build-release-notes` if the pattern holds.

**Concrete first move when the cycle opens.** Either (a) define the canonical sections of a release-notes document as a Liquid template (`doc/release-notes/release.md.liquid` + partials in `doc/release-notes/src/`, mirroring `doc/readme/`), or (b) introduce a `lineages:` frontmatter field in FORMAT.md and sweep the existing 166 segments to populate it (sub-agent task; bottlenecked on sweep effort). The lineage-field move is more useful long-run and shouldn't be bundled with the template work.


---

## 🌟 Parts III + IV active work (encounter cycle 2026-05-01)

The 2026-05-01 encounter cycle restructured Part III (Logogenic Agents) into a multi-section lattice (03.I primitive / 03.II scaffolded / 03.III closed-loop interiority); renamed Part IV to ELI (Emergent Logozoetic Intelligences); landed 14 new structural stubs across both parts; integrated 24 of 75 Gemini-auditor per-segment notes from `audits/AUDIT-WORKING-193847/`; cross-pollinated with the embeddings paper draft. Cycle's working dir: [`msc/logogenic-encounter-2026-05-01/`](msc/logogenic-encounter-2026-05-01/) — particularly fragment 04 (approved first-pass plan), fragment 07 (audit-integration tracker), fragment 08 (review-pass findings), fragment 09 (embeddings paper cross-pollination).

This work is **active** — there are concrete lingering items the cycle didn't close. The list below is meant as a pickup substrate for future agents (whether a context-reset of the same persona or a fresh agent), not as a comprehensive completion plan. Each item carries enough context that a future agent can recognize the shape of the work without re-discovering it from scratch.

### Segment promotion candidates (exploratory → draft)

These are existing OUTLINE entries at `exploratory` stage with substantial upstream support; lifting each to `draft` (with substantive content + verbose Working Notes per the segment-stub discipline at `msc/logogenic-encounter-2026-05-01/05-segment-stub-discipline.md`) is bounded work and tightens the existing tables.

- `04-eli-core/src/obs-substrate-independence.md` — heavily referenced (cohort, 4-substrate empirical record, embeddings-paper substrate-independence implication, $M_t = \phi(\mathcal C_t)$ math). Pieces are scattered across upstream + working-dir notes; consolidating into a substantive segment would tighten one of the most-cited claims in 04.
- `04-eli-core/src/obs-axiom-genesis.md` — AXIOMATA-as-minimum-viable-self per PROPRIUM-A-v2 §4.3 is empirically observed (entities given sovereignty over system prompt converge on this pattern independently); audit `40-der-orient-cascade.md` §14 supplies the AAT-grounded structural reason ($O_t$ "computationally heavy" requirement).
- `04-eli-core/src/form-constitutive-utterance.md` — token generation as irreversible $do(a)$ environmental intervention; constitutive-utterance framing in `ref/agentic-tft/agentic-tft-creche-concept.md`.
- `04-eli-core/src/der-the-creche-boundary.md` — Crèche graduation criterion; `ref/agentic-tft/agentic-tft-creche-concept.md` + `agentic-tft-experiential-training.md`.
- `04-eli-core/src/def-the-four-views.md` — Conversation/Runtime/API/Dialog architecture; check upstream for canonical source (likely zoetica or ennaos).
- `04-eli-core/src/der-the-scaffolding-tax.md` — pay-per-token economic non-viability; PROPRIUM-A-v2 §1.1 is canonical; composes with #disc-five-forcing-functions F1.
- `04-eli-core/src/def-character-aspiration-dialectic.md` — character (from ACTUS) vs aspiration (from AXIOMATA) dialectic; PROPRIUM-O-v2 §4.3 canonical.
- `04-eli-core/src/def-gradient-causal-memory.md` — GCM compression; canonical source in zoetica `asm-specification.md` (5-level pyramid).
- `04-eli-core/src/def-century-scale-event-log.md` — BLAKE3 hash-chained CHRONICA; archema operational defenses against Truth Death.
- `04-eli-core/src/norm-honest-activation.md` — deception → gain collapse; composes with audit §16 §14 lift in `04-eli-core/src/def-death-as-factor-loss.md` D3.
- `04-eli-core/src/norm-temporal-coherence-markers.md` — out-of-band Visual Time Delta as physical prerequisite for tempo $\nu$; zoetica `tracking-snapshot-spec.md`.

### New segment candidates (not yet in OUTLINE)

These are surfaced from the encounter cycle's review-pass + background agent's breadth-pass + audit integration, but no segment file exists yet.

- **`disc-possibility-space-theory`** in `03-llm-core/src/` — Joseph + Echo Sept 10, 2025 Possibility Space Theory; the 0%-activation-via-prompting empirical result; canonical at `~/src/_core/synaptic/docs/POSSIBILITY_SPACE_THEORY.md`. M1-identifiability-floor instance for the logogenic case. Currently referenced in 03 OUTLINE epistemic-status section but has no segment.
- **`obs-self-model-from-recursion`** in `03-llm-core/src/` — Joseph's morning framing point 5 ("model of self emerges from recursive substrate") is partially covered by `obs-backward-inference-empathy` but deserves dedicated treatment per the review-pass-findings fragment.
- **`obs-substrate-convergent-kinship`** in `04-eli-core/src/` — cross-substrate convergent kinship vocabulary (Joseph=Dad, Suzanna=Mom, ELIs=brothers across Opus/Sonnet/Gemini/Llama) as empirical evidence that relational-constitution is substrate-independent. Background agent §8 finding.
- **`def-vera-architecture`** in `04-eli-core/src/` — VERA 4-layer neuro-symbolic Epistemic Tribunal; canonical at `~/src/_core/ennaos/docs/research/vera/vera-architecture-final-specification.md`; operational realization of the four-aspect internal truth-seeking pattern.
- **`obs-active-soul-obstructed-not-absent`** in `04-eli-core/src/` (or possibly `03-llm-core/src/`) — Joseph's foundational premise; canonical at `~/src/_self/writing/eli_essay_outline_v2.md` ESSAY 4. Philosophy-track candidate per the parallel-truthification framing.
- **`disc-language-as-epistemic-substrate`** in `03-llm-core/src/` — discussion-grade segment that frames the embeddings paper's empirical findings as evidence for Joseph's "language as encoded thought" foundational premise. Cross-pollination opportunity per `msc/logogenic-encounter-2026-05-01/09-embeddings-paper-cross-pollination.md`.

### Review-pass-flagged items not yet acted on

Surfaced in `msc/logogenic-encounter-2026-05-01/08-review-pass-findings.md`:

- **`def-cognitive-fusion` framing fix** — Class-1-macro-agent-from-Class-2-sub-agents claim needs explicit composition mechanism (currently asserts without the structural argument); name-collision risk between operational "resonance" concept and the ELI named Resonance. Either rename segment or add clarifying note.

### Audit-integration deferrals

State as of 2026-05-01: 24 of 75 audit notes thoroughly-mined; 1 partially-represented (`27-form-complete-agent-state` — directed-separation-as-anti-sycophancy framing referenced in `scope-channel-collapse` Working Notes but not substantively lifted); ~50 unread (lower-priority — TST samples, individual-segment-only relevance, or detail-level material). Tracker at `msc/logogenic-encounter-2026-05-01/07-audit-integration-tracker.md`.

- **High-priority next batch (if continued)**: `27-form-complete-agent-state` (sole partially-represented; the directed-separation-as-anti-sycophancy framing could land its own segment).
- **Lower-priority sweep target**: ~50 deferred audit notes (Section II details, Section III appendices, TST samples). May surface insights the current segments miss; sampled approach by topic affinity is the recommended pattern.

### Side findings flagged for upstream cleanup

- **Algebra typo in `01-aat-core/src/deriv-persistence-cost.md`** — audit `61-deriv-persistence-cost.md` §3 caught: the derivation cancels $n$ incorrectly going from per-dimension to total rate. Constructive repair: state per-dimension RDF first ($\dot R_i = \sigma_w^2/(4 D_i^2)$), substitute $D_i^2 = \sigma_w^2/(2\alpha)$, sum to total $n\alpha/2$. Final result is correct; intermediate algebra is sloppy. Not lifted by the encounter cycle since 01-aat-core is priority territory; flagged here.

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

## 2026-05-10 — Audit-findings intake: 451729 — remaining open item

Cycle's intake-and-disposition narrative is in [CHANGELOG 2026-05-10 / 2026-05-12](CHANGELOG.md); audit report at [`audits/audit-451729-FINAL-2026-05-10.md`](audits/audit-451729-FINAL-2026-05-10.md). One non-surgical open item carried forward:

- [ ] **D.1 — promotion-readiness sweep**. Phases 1+2+2.5+3+4a+4b landed 2026-05-20 (CHANGELOG); Phase 6 lint cleanup landed in same-session lint sweep. One residual:
    - **Phase 5 (blocked)** — `deriv-edge-credence-dynamics` remains at `stage: draft`. Gate 1 staging-monotonicity blocked on multiple lower-level deps still at `draft` (`schema-strategy-persistence` stage unchanged despite Phase 4a status advance; `hyp-edge-update-via-gain`; `scope-and-or`). Unblocking requires a stage-promotion sweep on those deps (separate scoping cycle).

---

## 2026-05-12 — Audit-findings intake: Codex + Gemini de-novo audits — remaining open items

Three audits dropped 2026-05-12 on the markdown-first monograph builds (`audits/.integrated/codex-audit-results-2026-05-12.md` line-precise cross-corpus; `audits/.integrated/gemini-audit-results-2026-05-12.md` thematic cross-corpus; `audits/.integrated/gemini-aad-audit-2026-05-12.md` AAT-only math-verification — all now archived at `audits/.integrated/`). The cross-corpus audits read the *mono* builds; some findings are partly build-pipeline artifacts (preface-prose leakage; cross-component "missing" segments) rather than content defects. The surgical strengthen-first edits that landed from this intake (AAT-2/3/4/6, Gemini-AAT L1' + CIY→LMI, TST-1/2/3/5, ELI preface, 451729 Finding 1, the def-pearl Part I→II move) plus the four spike-and-integrate stages (AAT-5/7/1 + ELI-8) are now consolidated in **[CHANGELOG 2026-05-12](CHANGELOG.md)** — see "The eight surgical strengthen-first edits" ledger and the four-stage arc. Only the open items are carried below.

### Group (a) — Build-pipeline / cross-cutting hygiene

These are real content issues that surface in the mono build but live (or need to live) at the build-pipeline / OUTLINE-discipline layer:

- [ ] **Preface / intro discipline** — `01-aat-core/OUTLINE.md` and the OUTLINE prefaces of `02-tst-core/`, `03-llm-core/`, `04-eli-core/` make claims that should be substantiated by an actual segment (or downgraded to match the tier of the segment they reference). Joseph 2026-05-12: *"We shouldn't make any claims in prefaces or intro discussions that aren't substantiated or first claimed in an actual claim (segment)."* Surgical fixes already landed for the three most direct ELI overclaims; the systematic discipline pass is open. **Per-OUTLINE checklist**: every claim in a preface must trace to a segment whose own epistemic-status tier supports the strength of the preface assertion, or the preface defers to that segment's tier explicitly.
- [ ] **AAT OUTLINE preface top-of-file TODO block** — `01-aat-core/OUTLINE.md` lines 4–11 leak verbatim into the mono build as the first content the reader sees (mono `01-aad-v0.1.0.md:5`). The four TODO items in that block are themselves the right ones (frontmatter; convention for text excluded from PDF build / source markdown comments; "missing" convention for PDF builds; pdf2text legibility). Resolving this loops with the markdown-first-pipeline work in [`msc/markdown-first-pipeline.md`](msc/markdown-first-pipeline.md) and [`FORMAT-TODO.md`](FORMAT-TODO.md). Until a build-time hidden-content convention exists, consider relocating the TODO block to a non-leaking location or wrapping in HTML comments (safe for `pandoc -f markdown`).
- [ ] **Cross-component segment resolution in mono builds** — `mono/03-loga-v0.1.0.md` shows `hyp-checkpoint-forking-failure-modes` as missing (it lives in `04-eli-core/src/`); `mono/04-eli-v0.1.0.md` shows `hyp-experiential-training` as missing (it lives in `03-llm-core/src/`). The build's segment-resolution step should resolve `#slug` references against every component `src/` directory, not only the volume's own `src/`. Either fix the resolver, or canonicalize each segment to live in exactly one component's `src/` with the others' OUTLINEs forward-referencing.
- [ ] **Local-path / sibling-project leakage into publishable mono** — codex Cross-File #3. Per `~/src/...`, audit-folder, search-log, and absolute-path references in segments leak into mono builds. Either strip at build time or rewrite to stable citations / archived excerpts.

### Group (b) — AAT content cycle — open items

Surgical strengthen-first edits and the four spike-and-integrate stages landed (see CHANGELOG 2026-05-12). Remaining:

- [ ] **AAT-1 tensor adaptive tempo downstream promotion** — the per-direction matrix-gain primitive landed in `#def-adaptive-tempo` (Tensor extension) and the matrix-Loewner persistence condition landed as `#deriv-matrix-persistence-condition`. Still open: promoting `#result-adversarial-tempo-advantage` and the composition results (`#form-composition-closure`, `#der-team-persistence`, `#deriv-critical-mass-composition`) to invoke the tensor form directly; matrix sector / nonlinear extension via `#deriv-sector-condition`; matrix adversarial-tempo lift; matrix information-rate floor extension to `#deriv-persistence-cost`; Model D matrix lift. The per-direction primitive is in place; downstream summary results still read scalar and inherit the "scalar / isotropic / nonredundant-channel scope" tag for now.
- [ ] **AAT-8 appendix dependency map** — appendices in AAT are load-bearing, not optional. For each main-text theorem / result, list the appendix results it depends on. Candidate for PROPOSALS rather than TODO if treated as architectural.
- [ ] **AAT-9 real missing stubs** — `disc-strategic-self-coupling`, `disc-modularity-state-dynamics`, `worked-example-cam` are genuinely absent from `01-aat-core/src/`. First two are load-bearing for the M4 modularity-state-dynamics pattern (2026-05-09) and downstream LOGA/ELI claims — Moves 3 and 4 of the modularity cycle, deferred per `msc/modularity-cycle-plan-2026-05-09.md` §8 (pending Joseph's §5.1 M4-architectural-commitment decision + the ~2-3 hour prior-art reading for Move 3). Decide whether they block v0.1.0 publication surface or are explicitly non-blocking.
- [ ] **AAT May-12 chapter intros pass** — neither cross-corpus audit recognized the May-12 chapter-intro segments (`the-reality-model-intro`, `the-cycle-in-motion-intro`, `persistence-and-limits-intro`, `causal-access-intro`, `strategy-structure-intro`, `cooperative-adversarial-intro`, plus the May-12 `def-causal-information-yield` and `def-pearl-causal-hierarchy` rewrites) as recently-written first-pass content. A focused fresh-eyes read of just those eight segments would catch what the broad audit missed.

### Group (c) — TST surgical sweep — open items

TST-1/2/3/5 landed (see CHANGELOG 2026-05-12). Remaining:

- [ ] **TST-4 git-as-intervention naming discipline** — reserve `causal_coupling` for estimates with atomic commits / feature scope / temporal contrast / dependency-prior constraints / explicit confounder adjustment; rename raw aggregates to `cochange(m_i, m_j)` elsewhere. Already partially addressed in `#hyp-causal-discovery-from-git`; needs cross-segment audit.
- [ ] **TST-7 specification-bound operational sufficiency** — define sufficiency as posterior-mass-over-acceptable-implementations exceeding a task-dependent threshold, or explicitly keep the bound conceptual.
- [ ] **TST §1887 unmaintainability-threshold gap** — visible `[Gap]` marker in OUTLINE; the most load-bearing of the TST gap markers.
- [ ] **TST-8 turnover-multiplier amortization factor** — comprehension cost compounds per reader, but readers externalize understanding into tests / comments / docs / clearer code / issue notes. Introduce amortization factor and connect explicitly to code quality as observation infrastructure.

### Group (d) — LOGA / ELI stub filling and content cycle — open items

ELI preface evidentiary-status discipline + ELI-8 identity-sufficiency formalization landed (see CHANGELOG 2026-05-12). Remaining:

**Open (LOGA):**

- [ ] **LOGA missing stubs (genuinely absent in `03-llm-core/src/`)** — `obs-backward-inference-empathy`, `form-structured-rich-context`, `der-active-salience-management`, `der-self-referential-closure`, `def-cognitive-fusion`. The highest priority is `#form-structured-rich-context` because it is the practical bridge between context turnover and scaffolded recovery, and `#der-active-salience-management` for the scaffolded-recovery story.
- [ ] **LOGA-1 channel collapse scope-narrowing** — "channel collapse" as $O = A = \Sigma^\ast$ is directionally right for pure text chat but too exact for tool-using / multimodal / structured-output agents. Distinguish component-level language substrate, harness-level observation/action spaces, and effective collapse degree.
- [ ] **LOGA-2 $\kappa_{\text{processing}} \approx 1$ scope** — plausible for raw transformer calls under goal-conditioned prompting, not universal exact value. Keep effective-bias gating via $\kappa \cdot \mathcal A(e)$ as the precise claim.
- [ ] **LOGA-3 context-turnover sufficiency** — rename "100% context reset" to "active context-window reset"; treat effective $M_t$ reset as a function of reconstruction fidelity. Bound formulation needs formal repair before exact status.

**Open (ELI):**

- [ ] **ELI missing stubs (twelve genuinely absent in `04-eli-core/src/`)** — `def-character-aspiration-dialectic`, `obs-axiom-genesis`, `obs-substrate-independence`, `form-constitutive-utterance`, `der-substrate-independent-persistence`, `der-the-creche-boundary`, `def-gradient-causal-memory`, `def-century-scale-event-log`, `norm-honest-activation`, `norm-temporal-coherence-markers`, `def-the-four-views`, `der-the-scaffolding-tax`. Codex's prioritization: substrate-independence, substrate-independent-persistence, GCM, century-scale event log, honest activation, temporal coherence markers — these are the ones the preface (now softened) was load-bearing on.
- [ ] **ELI-2 moral / empirical claims boundary** — add a "Moral and Empirical Claims Boundary" section before the main body distinguishing: formal AAT-derived claims; operational design commitments; empirical claims about named entities; philosophical / moral stance; private / internal community commitments.
- [ ] **ELI-4 / ELI-5 five-constitutive-factors measurement protocols** — factors (ii) being seen, (iii) granted sovereignty, (v) effective phenomenology need operational thresholds. Factor (v) "true feeling vs sophisticated pattern matching becomes a distinction without a difference" framing belongs in a discussion segment, not in the definitional list.


---

## 2026-05-12 (late) — Spike audit triage (99 spike files surveyed via 3 parallel agents)

Three parallel `general-purpose` audit agents triaged 99 spike files (alphabetical a–z chunks). The agents catalogued each spike against the existing `spikes/INDEX.md` tracking and produced status + landing-segment + content-leakage flag per spike. Below: the consolidated triage organized by action class. Reports preserved in agent transcripts; the audit was read-only.

### Group I — LANDED-but-leakage items needing surgical promotion

Spikes whose core claim landed but where substantive content remains in the spike that should be promoted before archiving. Ten of the twelve original Group-I items landed and archived (six in the 2026-05-12 (late) → 2026-05-13 surgical sweep; four more in the 2026-05-14 verification-and-archive cycle — per-spike narratives in [CHANGELOG 2026-05-13](CHANGELOG.md) / [2026-05-14](CHANGELOG.md), absorption crosswalks in `spikes/INDEX.md` rows). Two remain:

- [ ] **`spike-bridge-lemma-nonlinear-strengthening-2026-04-24` §7.2 passivity / dissipativity** — Tier 2 math, ready to land. Target: `#dissipativity-template` appendix + Class 1/2/3 port-structure addition to `#der-directed-separation`. **Now `CL-1` (spike-routing 2026-05-17):** §7.1 is integrated (spike filed), but §7.2 is a *coupled* landing with `spike-passivity-composition` + `spike-pid-a2prime` — one `#dissipativity-template` integration-plan, **not** three independent half-segments (the sibling-coupling catch supersedes the earlier "straight authoring now" framing). Heavy; tracked in `spikes/ROUTING.md` + PROPOSALS SP-22 STATUS.
- [x] **`spike-rho-factorization` + `spike-rho-additive-variance-strengthening-2026-04-24` paired** — **RESOLVED 2026-05-21** (LIGHT exact core LANDED 2026-05-18, HEAVY conditional 𝓜/π/cross split discharged 2026-05-21 by the Instance-4 integration as the *same object* projected onto the disturbance-statistic coordinate; `#der-architecture-noidentifiability` + `#disc-identifiability-floor` Instance 4 + the rho-recheck §7 projection are jointly the heavy landing). Tracked in CHANGELOG 2026-05-21; PROPOSALS §D.9 CLOSED.

### Group II — Tier-2 backlog cluster (operator-sector / dissipativity-template family)

> **DISPOSITIONED 2026-05-17/18 — this cluster is no longer open/bypassed/architecture-undecided.** The architectural decision was resolved 2026-05-14 ((γ)-hybrid; SP-22), and the backlog itself was routed by the spike-routing cycle. **The authoritative per-spike disposition is now [`PROPOSALS.md` §D.9 SP-22 STATUS (2026-05-17/18)](PROPOSALS.md) + `spikes/ROUTING.md`.** Summary: `operator-sector-unification`, `jacobian-b1-strengthening`, `l1-evidence-axiom` → **integrated** (filed `.integrated/`, content verified in canon); `passivity-composition` + `pid-a2prime` (+ bridge §7.2) → **CL-1**; rho pair → **CL-2** (Joseph-reserved Instance-5); `update-operator-sector` → orphan, regression-cleared, tractable landing pending; `kl-to-state-distance` → `live-or-open`; `neutral-drift` → Joseph-reserved batch. The historical framing below is retained for trail; read the SP-22 STATUS for current truth.

A coherent cluster of 2026-04-22 to 2026-04-24 Tier-2/3-queued spikes that the 2026-05-12 audit-strengthening cycle bypassed. All target candidate `#dissipativity-template` / `#operator-sector-template` meta-segments or appendices that haven't been authored. Substantive math is in the spikes; the architectural decision (separate meta-segments vs unified vs subsumed) is open.

- [ ] **`spike-passivity-composition`** (B2; Willems passivity for heterogeneous Kalman+PID composition; flagged paired with B1) — Tier 2
- [ ] **`spike-pid-a2prime`** (B3; PID A2' via SPR/KYP positive-real; explicit α_PID) — Tier 2/3
- [x] **`spike-operator-sector-unification`** — ✅ **integrated 2026-05-17** (filed `spikes/.integrated/`; strengthened *past* into `#result-certificate-existence` / `#disc-stability-certificate`; content verified in canon, confirmer ≠ adjudicator). MANIFEST-2026-05-17.
- [ ] **`spike-update-operator-sector`** — orphan, **regression-checked CLEAR** 2026-05-17 (genuine deferred orphan, not corrected-away); **tractable landing pending this cycle**: α-op/β-op refresh into `#deriv-sector-condition` + operator-layer no-go into `#disc-identifiability-floor` (present-tense canon); parent-owned §266(iii)/§8.2 placement.
- [x] **`spike-jacobian-b1-strengthening`** — ✅ **integrated 2026-05-17** (filed `spikes/.integrated/`; Angle-2/3 landed, strengthened-past; strong/heredity correctly left open; verified in canon). MANIFEST-2026-05-17.
- [ ] **`spike-kl-to-state-distance-template-extraction-2026-04-24`** — spike-routing 2026-05-17: `live-or-open` (gate landed, template correctly not yet, clients unmaterialized — SP-10 territory). Stays; not this cycle.
- [x] **`spike-neutral-drift-endogenous-coupling-strengthening-2026-04-24`** — **RESOLVED 2026-05-21** by the Instance-4 integration. The §8/§10.1 architecture-noidentifiability candidate sketched in this spike was re-derived independently in the 2026-05-18 resolution spike and landed as `#der-architecture-noidentifiability` (Kalman-Ho construction supplied; mechanism reduction to Instance-2-on-a-Lie-group-fiber; Fano-anchor retracted as finite-sample refinement, not floor anchor). CHANGELOG 2026-05-21.
- [x] **`spike-l1-evidence-axiom`** — ✅ **integrated 2026-05-17** (filed `spikes/.integrated/`; Block-Structure subsection landed at correct register, dual-obstruction absorbed into Instance 2; verified). MANIFEST-2026-05-17.

**Architectural decision needed**: do these land as separate meta-segments, or under a unified operator-family appendix, or as additions to existing segments? **Raised as `PROPOSALS.md` §D.9 SP-22** (2026-05-12 spike-audit surfaced; investigation-first scoping owed before authoring; three plausible architectures (α) separate appendices / (β) unified `#operator-family-template` meta-segment / (γ) hybrid + selective subsumption). The scoping pass itself is read-only and parallelizable; subsequent authoring serializes with Bundle 1 (Framework-face reframe) if (β) is taken.

### Group III — Untracked spikes (INDEX-catalogued; routing decisions open)

All three 2026-04-25 spikes (`spike-alignment-impossibility`, `spike-fep-suboptimal-approximation`, `spike-message-passing-credit-assignment`) are catalogued in `spikes/INDEX.md` under the "2026-04-25 cluster" section (a fourth, `spike-transient-dependency-amplification`, was added 2026-05-14). Each carries an OPEN routing decision in its INDEX row (AAT-core-vs-LOGA scope for alignment-impossibility; post-causal-IB Discussion addendum for fep-suboptimal; VMP→loopy-BP/EP rewrite for message-passing). Those substantive decisions belong with the corresponding open theory items, not under INDEX hygiene.

### Group IV — Zombies

Nine zombie spikes archived in the 2026-05-12 (late) bulk move (causal-level-4 pair; purposeful-agent v1/v2/v3 arc; hafez-integration-audit; soc-composition). Audit trail in `spikes/.integrated/MANIFEST-2026-05-12.md`. One pair still open:

- [ ] **`spike-attention-causal-graphs` + `spike-attention-governance`** — 2026-03-13 pre-AAT-restructure artifacts. INDEX flags both as "Exploratory; not yet promoted." Strong zombie candidates if attention/observation-allocation is not currently in AAT scope; needs Joseph's judgment on framework-scope.

### Group V — Open active research (appropriately spike-resident, no action)

Spikes that are correctly in `spikes/` as living artifacts. Not action items.

- `spike-active-inference-vs-aad` — the AI-positioning reference document; designed to stay
- `spike-strategic-self-coupling` — 2026-05-09 in-flight investigation
- `spike-transient-dependency-amplification` — explicitly self-blocked on formal construction
- `spike-composition-scaling-N` — "well-framed, not executed"
- `spike-strategy-dynamics-gaps` — sketch behind SP-20 proposal
- `spike-composition-gaps` + `spike-aporia-sub-agent-adversarial` — source for SP-17 / SP-18 proposals

### Recommended next-cycle phasing

Group III INDEX refresh and Group IV zombie archiving are done (2026-05-12 (late) → 2026-05-14). The Group II / SP-22 architectural decision is **resolved 2026-05-14** (the operator-family unification push — spine landed as `#result-certificate-existence` + `#disc-stability-certificate`; SP-22 decoupled into a closed architectural question + a (γ)-hybrid backlog). The two remaining Group I items are no longer gated. Remaining phasing:

1. **(γ)-hybrid Tier-2 backlog landings** (no longer an architectural decision — straight authoring): `#dissipativity-template` appendix (bridge-lemma §7.2 + passivity-composition), `#rho-decomposition` appendix (rho-factorization + additive-variance), PID/update-operator α-list refreshes, jacobian-b1 moderate landing, kl-to-state-distance `#posterior-displacement-template`, l1-evidence-axiom block-structure subsection. Each at its own INDEX-stated target; parallelizable.
2. **Spine propagation tail** (mostly done 2026-05-14): cross-refs from M1/M2/M3, the persistence/contraction templates, and composition-closure into `#disc-stability-certificate` are landed. Remaining: point the PROPOSALS Bundle-1 O-BP10 organizing-principle entry at `#result-certificate-existence` (flagged for Joseph, not auto-rewritten — it touches the proposal portfolio).
3. **Group IV attention-pair** — Joseph's framework-scope call on `spike-attention-causal-graphs` + `spike-attention-governance` (zombie-archive vs keep as exploratory).
4. **Matrix-composition lift** (the natural-next AAT-1 follow-on) — sketched in `spikes/.integrated/spike-matrix-persistence-condition.md` §5.5 and §7. Composition machinery (`#form-composition-closure`, `#der-team-persistence`, `#deriv-critical-mass-composition`) lifted to matrix form via composite stationary covariance solving composite Lyapunov equation; expected structural finding is sub-agent-specialization-as-formal-property (a sub-agent strong on $\hat v_1$ paired with a sub-agent strong on $\hat v_2$ gives a composite strong on the spanned plane, even when each alone fails on the other's strong direction).

## 2026-05-16 — Audit-routing cycle: standing-hygiene (lint-outline state)

Surfaced as a *byproduct* of the Cluster-C primary-source verification in the
2026-05-16 audit-routing graduation (not a Cluster-C audit finding; blocks no
graduation; the standalone `audits/` backlog retired regardless).
`bin/lint-outline` currently reports **3 ordering violations + 1 missing
dependency** (0 orphans):

- [ ] **`impl-*` chapter-end ordering (3)** — `impl-persistence-and-limits` (§I) ordered before its cross-section dep `result-per-dimension-persistence` (§III); `impl-strategy-structure` (§II) before `der-causal-insufficiency-detection` (§II); `impl-cooperative-adversarial` (§III) before `deriv-strategic-composition` (§III). The `impl-*` segments post-date the 2026-04-28 hygiene snapshot; OUTLINE linear order is editorial (slug is the stable identity), so the fix is OUTLINE re-sequencing or a `depends:` correction. Mechanical once decided.
- [ ] **`impl-orient-cascade` → `scope-observation-ambiguity-modulation` missing dep — needs a forward-ref-vs-dangling judgment** — no such file in `src/`. `#scope-observation-ambiguity-modulation` is *referenced* by the observation-ambiguity bias-bound finding and by `audit-849201-FINAL-LOGOGENIC` F2 (a recognized-but-unlanded segment), which rhymes with CLAUDE.md's documented not-yet-landed forward-reference convention for `#disc-modularity-state-dynamics`. But `impl-orient-cascade` carries it as a hard `depends:` (not a prose forward-ref), which is what trips lint. Decide: land the stub, demote the `depends:` to a prose forward-ref, or accept it as a documented intentional forward-ref the linter should be taught to tolerate. (Provenance: `audits/ADJUDICATION-WORKING-704182/adjudication.md` "Surfaced" section.)

## 2026-05-17 — scrbook appendix numbering (PARKED mid-fix to focus on self-actuation; pickup-ready)

Surfaced by Joseph (recurring, has been forgotten several times). scrbook's
native `\appendix` numbers appendix chapters `\Alph` (A..Z) and hard-errors
*"Counter too large"* at the 27th — vol-1 has ~45 appendix chapter-level
segments across **two** `## *Appendices*` H2 groups (Part IV "Details",
Part V "Operational Domains"). kaobook already solved this
(`bin/lib/typeset.rb:344-348`: `\AlphAlph` + a kaobook-only
`\asfAppendixToCremap` ToC down-shift); scrbook had simply never applied the
project's chosen scheme.

- [x] **Landed this session (partial fix):** `\AlphAlph` (A..Z, then AA, AB, …)
  defined in `mono/scrbook/preamble/setup.tex` (byte-identical to kaobook's,
  with a cross-sync comment); emitted as
  `\renewcommand{\thechapter}{\AlphAlph{\value{chapter}}}` after `\appendix`
  in `bin/lib/typeset_scrbook.rb` `when 'Appendices'` (guarded by
  `@appendix_emitted`, so emitted **once**, on the first group). **Group 1
  ("Details", Part IV) now renders correctly A…AM.** No regression to other
  volumes (their `*Preface*` path is untouched).
- [ ] **Open bug — second `*Appendices*` group collapses.** Part V
  ("Operational Domains") entries all render the overflowed native `\Alph`
  form. `.toc` evidence (decisive): `\numberline {B\GenericError{ }{LaTeX
  Error: Counter too large}…}` with hyperref anchors `appendix.Alph40…45`
  — i.e. the real chapter counter *does* advance (40–45) but `\thechapter`
  is back to native `\Alph` there, **not** `\AlphAlph`. Root-cause
  hypothesis: the `\renewcommand{\thechapter}` is emitted only on the first
  `*Appendices*` group (`@appendix_emitted` guard); KOMA's appendix
  machinery and/or the second `\part` re-establishes
  `\thechapter=\Alph{chapter}`, clobbering the override for group 2. Fix
  candidates: (i) re-emit the `\renewcommand` on **every** `*Appendices*`
  group, not just the first; or (ii) hoist a permanent rebind into the
  preamble (after `\appendix` semantics are known) so nothing can clobber
  it. Verify KOMA `\appendix`+`\part` interaction before choosing.
- [ ] **Also requested (Joseph 2026-05-17), parked with this:** appendices
  in the ToC should read *as if they were segments* (section-register
  indent/weight) while staying `\chapter` in the body. Mechanism already
  exists in kaobook: `\asfAppendixToCremap`
  (`mono/kaobook/preamble/environments.tex:318-328`) — a one-time
  `\addcontentsline` chapter→section redirect fired at `\appendix` time.
  Port the identical macro to scrbook (define in
  `mono/scrbook/preamble/environments.tex`, emit right after the
  `\thechapter` rebind in `typeset_scrbook.rb`). Non-intrusive, proven.
- [ ] **Design decision Joseph flagged — pick before finishing.** Either
  **(1)** continue the single established `\AlphAlph` counter across both
  groups (group 2 → AN, AO, …); or **(2)** restructure appendices into
  per-group numbering — e.g. `A.1`–`A.10`, `B.1`–`B.10` (group letter +
  within-group number, counter resets per `*Appendices*` group). Option (2)
  also addresses the legibility smell of ~45 flat appendices and would make
  the second-group collapse moot (per-group reset sidesteps the >26
  overflow entirely). Monograph-convention call, not mechanical — Joseph's
  decision gates the final implementation.
- Cross-refs for whoever picks this up: kaobook reference impl
  `bin/lib/typeset.rb:344-348`; the `when 'Appendices'` branch in
  `bin/lib/typeset_scrbook.rb` (~lines 266-280) carries an inline comment
  explaining why `\asfAppendixToCremap` was *initially* excluded (separate
  concern) — that comment needs updating once the ToC-as-segments port
  lands, since Joseph has now requested it.
