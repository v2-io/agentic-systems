# Adjudication — pilot slice (audit-471203 FINAL + SUPPLEMENT, extracted-gemini-2026-04-26-27)

**Adjudicator:** Claude Opus 4.7 (1M context), pilot agent
**Date:** 2026-05-15
**Working dir:** `audits/AUDIT-WORKING-583046/`
**Slice:** `audits/audit-471203-FINAL-2026-04-28.md` +
`audits/audit-471203-SUPPLEMENT-phase-2.md` +
`audits/extracted-gemini-feedback-2026-04-26-27.md`

**Standing rule applied:** route, don't execute. Disposition = *where each
finding belongs*, not *whether we did what it asked*. Strengthen-before-soften
is live: a finding asking us to weaken a claim we instead strengthened is
**correctly closed**. Soft / sentiment findings are first-class — they get a
durable home, not the trash and not a TODO dump. No segment / tracking file
was edited; verification was first-hand against current `src/` (git-recency
poisoned by the 2026-05-15 rename sweep, so I read the files, not the log).

**Headline:** all three files in this slice are **fully accounted for and
ready to graduate to `audits/.integrated/`**, with one routing action
outstanding (Finding 7 — a trivial citation fix that is *not yet applied* in
current `src/`) and two architecture-class findings that are *correctly
parked in PROPOSALS* under different IDs. Nothing in this slice is lost; one
small thing is genuinely still open.

A frame correction is recorded in §4 (the brief/partition's claim that 471203
"has a `pending-findings` ledger" is **false** — no `pending-findings-*.md`
references audit-id 471203; its durable ledger is the SUPPLEMENT itself). This
does not change any disposition but it changes how the evidence hierarchy
applies to this file and to the partition's Group-L assumptions generally.

---

## 1. audit-471203-FINAL + SUPPLEMENT — the six §B findings + Finding 7

The FINAL raised 6 §B findings. The SUPPLEMENT (same day, same auditor,
Joseph-authorized fixes) resolved 1–4 directly, surfaced Finding 7, and left
5 / 6 / 7 pending architectural / policy / trivial-fix decisions. The
SUPPLEMENT *is* this cycle's resolution ledger (it carries per-finding
status, landing edits, the §N comprehensive-sweep record, and a verification
table). I re-verified every disposition against today's `src/`.

### Finding 1 — stale `#deriv-directional-survival-exploration` xref in `disc-ciy-unified-objective`
- **Valid in the first place?** Yes — verified real. Segment was demoted to
  `spikes/` 2026-04-28; xref not propagated.
- **Valid as of today?** **No — resolved.** `disc-ciy-unified-objective.md:44`
  now reads `(see #deriv-causal-ib-lmi)`; no `deriv-directional-survival-exploration`
  hit anywhere in `01-aat-core/src/`. Landed per SUPPLEMENT §H.1.
- **What it really is:** defect (doc-rot / cross-segment integration debt),
  **resolved by strengthening the right xref into place** (not a softening).
- **Route:** **closed — record in MANIFEST as resolved-per-SUPPLEMENT-§H.1.**
  No further action.

### Finding 2 — status-label / type / Epistemic-Status mismatch, same segment
- **Valid in the first place?** Yes (layered; defensible-reading existed).
- **Valid as of today?** **No — resolved.** Line 44 leads
  *"Discussion-grade summary; underlying derivation is exact."*; line 50
  carries the explicit two-layer Max-attainable framing. This is the
  *cleaner* pattern the FINAL asked for, applied. Landed per SUPPLEMENT §H.1.
- **What it really is:** defect (scope/status mismatch), resolved correctly
  (the layered framing is a strengthening of the segment's honesty, not a
  weakening of any claim).
- **Route:** **closed — resolved-per-SUPPLEMENT-§H.1.**

### Finding 3 — implicit-Markov-of-Ω never named downstream
- **Valid in the first place?** Yes — genuine scope-honesty leak; no prior
  audit footprint (confirmed new, SUPPLEMENT §K).
- **Valid as of today?** **No — resolved.** `def-action-transition.md:41`
  carries the "Markov-of-Ω as a modeling commitment" paragraph, almost
  verbatim the FINAL's suggested text, with the agent-side/world-side
  independence stated. Landed per SUPPLEMENT §H.2.
- **What it really is:** defect (scope-honesty leak), resolved by *adding*
  the missing scope declaration — i.e. the framework's discipline extended to
  cover the world side. This is the project's signature move; correctly
  closed.
- **Route:** **closed — resolved-per-SUPPLEMENT-§H.2.**

### Finding 4 — TF-XX diff-voice annotations (13 segments → 49 total)
- **Valid in the first place?** Yes — verified by grep; concurrently flagged
  in `audit-829314-FINAL-2026-04-28` (4 of the 13).
- **Valid as of today?** **No — resolved, comprehensively.** SUPPLEMENT §H.3
  cleaned the 13; §N (Joseph-authorized broader sweep) removed 49 trailers
  across all four components + 7 inline reframes. I re-ran the §N.2
  verification grep: zero `TF-[0-9]` hits in non-`old-tf` `01-aat-core/src/`;
  the single surviving "descended from" hit
  (`deriv-strategy-cost-regret-bound.md:214`) is the **correctly preserved**
  Shannon-rate-distortion-lineage theoretical claim, exactly as §N.2
  documented — *not* a TFT breadcrumb. Disposition holds.
- **What it really is:** defect (voice-discipline / doc-rot), resolved and
  over-delivered (the FINAL found 13; the cycle cleaned the whole corpus).
- **Route:** **closed — resolved-per-SUPPLEMENT-§H.3+§N.** The §I.1 "wider
  TFT-lineage pattern" sub-observation is **also closed** — it was the
  trigger for the §N sweep that resolved it; §N.3's broader scan confirms no
  surviving lineage breadcrumbs. Nothing from Finding 4 or its §I.1 extension
  remains open.

### Finding 5 — depends-list incompleteness in `#post-composition-consistency`
- **Valid in the first place?** Yes. **Valid as of today? Yes — still real,
  unresolved.** Verified first-hand: frontmatter still `depends: [scope-agency]`
  and `stage: deps-verified`, while the Formal Expression's Block 3
  (`*[Derived (Conditional on Tier 1M ..., from #result-contraction-template
  (CC-parallel)/(CC-cascade)/(CC-feedback))]*`, line 36) plus prose
  (lines 14, 30–44, 75–90) materially uses `#result-contraction-template`,
  `#scope-composite-agent`, `#form-composition-closure`, `#der-tempo-composition`,
  `#der-team-persistence`, `#result-persistence-condition`,
  `#der-temporal-nesting` — none in `depends:`.
- **What it really is:** **architectural** (the FINAL's option (a) extend-deps-
  and-downgrade-stage vs (b) split-segment is a structural judgment), AND a
  **new instance of a well-tracked known pattern** — SUPPLEMENT §K records it
  as a new instance of the F-A finding-cluster (7 instances rooted at F-A0,
  `audit-584721-FINAL-2026-04-25.md:54–88`; also `audit-742613-FINAL:273+`).
  This is *not* a strengthen-vs-soften case; it is a real Gate-1-criterion-4
  violation the project acknowledges.
- **Route:** **NOT closed — but already routed.** Two live homes confirmed:
  (i) **PROPOSALS.md SP-6** ("composition-closure consolidation (residue)",
  line 98) explicitly names `#post-composition-consistency` scope adjustment
  as remaining scope; (ii) **TODO.md:149** "Heredity axiom for
  `#post-composition-consistency`" scoping-spike item. The depends-discipline
  side of this is *the F-A cluster*, which lives in the 584721/742613
  ledgers, not here. **Recommendation: this finding does NOT block 471203's
  graduation** — it is fully captured in PROPOSALS SP-6 + TODO:149 + the F-A
  cluster ledgers. Record in MANIFEST as *routed to SP-6 / TODO:149 / F-A
  cluster (584721, 742613)*; the architectural (a)-vs-(b) decision is
  Joseph's and lives in PROPOSALS, which is its correct home.

### Finding 6 — Pearl-`do` in `#scope-agency` before `#def-pearl-causal-hierarchy`
- **Valid in the first place?** Yes (mild; notation-not-derivation). **Valid
  as of today? Yes — textually unchanged.** Verified: `scope-agency.md:19`
  still uses `P(o \mid do(a))` in the Formal Expression; `depends:` is
  `[scope-adaptive-system, def-action-transition]` — `def-pearl-causal-hierarchy`
  not declared. SUPPLEMENT §K notes this is the **identical finding, verbatim
  wording**, already recorded at `audit-742613-FINAL-2026-04-25.md:254`.
- **What it really is:** **duplicate of a prior (742613) audit's finding** +
  a **FORMAT-policy question** (is Pearl-`do`/Shannon-`H`/`E[·]` "standard
  math notation" exempt from depends-tracking?). I checked: **no
  standard-notation exemption policy exists in FORMAT.md, TODO.md, or
  PROPOSALS.md** today. The mitigant is real but partial — `scope-agency.md:24`
  *does* carry an inline parenthetical "(where $do(\cdot)$ is Pearl's
  intervention operator; see #def-pearl-causal-hierarchy)", so a reader is not
  stranded; the unresolved part is purely the depends-graph-hygiene/FORMAT-
  policy question.
- **Route:** **duplicate — defer to 742613's ledger; do not double-track.**
  This finding should be closed *for 471203* with a MANIFEST note "duplicate
  of `audit-742613-FINAL:254`; disposition follows 742613." The underlying
  FORMAT-policy decision is genuinely open but is **not 471203's to carry** —
  it belongs wherever the F-A cluster / 742613 disposition routes the
  standard-notation-exemption question. *Surfacing for the parent:* there is
  currently **no tracked home for the FORMAT standard-notation-exemption
  policy decision itself** — if 742613's disposition also punts it, it risks
  falling through the cracks. Flagged in §3 below.

### Finding 7 — Tishby-Zaslavsky 2015 miscitation in `#form-information-bottleneck`
- **Valid in the first place?** Yes — Phase-2 web verification (SUPPLEMENT §J,
  §L) established Tishby-Zaslavsky 2015 is IB-applied-to-DNNs; the IB↔VFE
  bridge is Alemi et al. 2017 (arXiv:1612.00410) + Achille-Soatto. High
  confidence; this is a real citation error, not a strengthen-vs-soften.
- **Valid as of today? YES — STILL OPEN, NOT FIXED.** Verified first-hand:
  `form-information-bottleneck.md:50` "Connection to variational free energy"
  paragraph **still reads** *"...related under the Markov-chain factorization
  $Y - X - T$ (Tishby & Zaslavsky 2015, ... makes the deep-learning
  instantiation explicit)."* The Alemi-2017 / Achille-Soatto attribution the
  SUPPLEMENT §L recommended has **not been applied**. (Note: lines 32 and 48
  correctly cite Tishby-Pereira-Bialek 1999 and the IT-MDP lineage — those
  are fine; the defect is localized to the line-50 VFE-bridge parenthetical
  exactly as Finding 7 anchored it.)
- **What it really is:** **defect — open, trivial, isolated, high-confidence,
  unapplied.** Severity Medium (the IB↔VFE specialization is load-bearing for
  the "AAT takes IB form without active-inference's normative stance"
  positioning). SUPPLEMENT §O item 4 explicitly lists it as "Apply Finding 7
  fix (trivial citation update)" — i.e. the cycle's own ledger flags it as
  the one substantive thing still owed.
- **Route:** **ACTIONABLE — this is the single genuinely-open item in the
  entire slice.** Per the triage spine's "high-confidence isolated fixes may
  be applied directly (co-owner's call) rather than queued," this is a
  textbook direct-fix candidate: one-parenthetical edit, no architectural
  judgment, citation verified by Phase-2 web check. **Recommended routing:
  parent applies the §L suggested edit directly** (replace the line-50
  parenthetical with the SUPPLEMENT §L text adding Alemi et al. 2017 +
  Achille-Soatto and re-scoping Tishby-Zaslavsky to the deep-learning
  instantiation), *then* 471203 graduates clean. Do **not** put this in
  TODO — it is below the architectural bar and TODO is explicitly not the
  sink. If the parent prefers not to edit `src/` in this cycle, the
  fallback home is a single tracked TODO line, but direct-fix is the
  spine-sanctioned and better call.

### §B.1 rescinded candidates (FINAL lines 182–190)
The FINAL itself withdrew four candidates under burden of proof
(`#der-recursive-update` status, Definition-vs-Scope tags, cycle-phase
formal-distinction overclaim, CIY-name-vs-substance). **No routing needed —
the auditor self-disposed these.** Two have downstream life that is *already
tracked elsewhere* (see §2): the cycle-phase overclaim → TODO.md §"Greek
vocabulary prose discipline"; CIY-name → §F8 naming-brainstorm, mined into
naming-cycle. Recording here only so MANIFEST can assert nothing was dropped.

### §D hypothesis-tier observations (FINAL lines 212–222) — 4 items
Loose-grade, auditor-marked `Hypothesis`. Not defects, not asks. These are
**soft/architectural-seed material**. Spot-check: the linear-Gaussian-regime
hypothesis and the adversarial-tempo-bilateral-coupling hypothesis are
substantive structural observations. **Route: polish-and-sentiment ledger**
(the soft-findings home the spine provisionally specifies), themed under
"framework-scope observations," attributed to 471203 §D. None rises to a
PROPOSALS entry on its own; none is a TODO item. Low ceremony, recoverable.

### §F bigger-picture observations (FINAL lines 242–304) — 8 items
This is the audit's self-described "most distinctive contribution." Triage:

- **F1 — fourth meta-segment `#disc-theorem-import-architecture`:**
  architectural. **Route: PROPOSALS.** Verify-first result: there is a
  meta-segment-family conversation in PROPOSALS (SP-11 composition-monotonicity
  fourth-meta-segment; the operator-family-template β-option at line 264 with
  its "DO NOT elevate to fourth meta-pattern" INDEX recommendation). The
  *theorem-import* meta-segment specifically is **not** an existing PROPOSALS
  entry — F1 is a genuinely additive architectural proposal that does **not**
  yet have a home. **Recommendation: surface F1 to the parent as a candidate
  new PROPOSALS entry** (it is the kind of bigger-picture move the audit-cycle-
  handling discipline says deserves first-class treatment, not Tier-C defer).
- **F2 — (PI)-as-the-surprising-convergence + uniqueness-of-coherent-
  statistical-geometry:** architectural/research-seed, explicitly
  "Speculative." **Route: polish-and-sentiment ledger** under "research
  seeds," with a pointer that the uniqueness conjecture could graduate to
  PROPOSALS if pursued. Not strong enough yet for a PROPOSALS schema entry.
- **F3 — composed obstructions / composition theorem for impossibilities:**
  architectural research direction. **Route: polish-and-sentiment ledger
  "research seeds"**; flag to parent as PROPOSALS-candidate-if-pursued (it is
  a clean extension of `#disc-identifiability-floor`).
- **F4 — hysteresis in persistence:** architectural extension. Same routing
  as F3 (ledger research-seed; PROPOSALS-candidate-if-pursued).
- **F5 — Class 2 (LLM) agents and engineering guidance:** this is **already
  the live core of the project** — the wrapping construction
  (`#der-class-coercion-via-wrapping`, `#der-logogenic-as-wrapping`), GUC
  Class taxonomy, shoshin W₁/W₂ work, and the TODO "shoshin engineering
  follow-on" + "Detailed tempo accounting for canonical wrapper architectures"
  items all post-date and **subsume** this observation. **Route: closed —
  subsumed by post-2026-04-28 class-coercion cycle work** (CLAUDE.md "Known
  Fragilities" wrapping-construction paragraph; TODO §III/Composition shoshin
  items). Record in MANIFEST as subsumed; no new tracking.
- **F6 — 04-eli-core OUTLINE-vs-present gap:** this is **already a tracked
  open discipline item** — TODO.md:386 "Preface / intro discipline" (Joseph
  2026-05-12: no preface claims unsubstantiated by a segment) and TODO.md
  notes the ELI surgical fixes already landed. **Route: duplicate-of-later-
  tracked-item** → TODO.md:386 preface-discipline pass. No new tracking;
  MANIFEST note "subsumed by TODO preface-discipline item."
- **F7 — commitment-state $C_t$ extension to $G_t$:** architectural.
  **Route: already in PROPOSALS — SP-12** ("Commitment / resource / temporal
  DAG extensions," D.4, line 192; "commitment state (BDI-style desire $D_t$ /
  committed intent $I_t$)"). Exact match. **Closed — routed to SP-12.**
  MANIFEST note "F7 = PROPOSALS SP-12."
- **F8 — naming-brainstorm seeds (14-row table):** soft/naming. **Route:
  naming-cycle artifacts** — the FINAL's working dir
  (`msc/AUDIT-WORKING-471203/`) is already cited project-wide as
  Brief-authoring / naming-brainstorm raw material, and TODO.md:44 points the
  naming-cycle at `msc/naming/naming-votes/audit-471203-incremental.md`. The
  consolidated §F8 table should be **mirrored into the polish-and-sentiment
  ledger** (themed "naming seeds") so it is recoverable independent of the
  working-dir, and cross-referenced to the naming-cycle. Nothing lost; the
  CIY / directed-separation / "two parallel exploration drives" seeds are
  exactly the 5%-polish signal the spine protects.

### §G process feedback on audit instructions (FINAL lines 306–322) — 7 items
Feedback on the *de-novo audit instructions themselves* (break-protocol
guidance, wandering-thoughts prompt value, Phase-2 quick-grep recipe,
Phase-2-verification-candidate logging, periodic phenomenological check-ins).
Plus one framework-content item embedded (cycle-phase Greek overclaim, line
314 — see below). **Route: polish-and-sentiment ledger themed "audit-process
/ instruction improvements"**, attributed to 471203 §G. These are durable,
actionable-eventually instruction refinements; they are not framework
findings and must not be lost into the framework TODO. The cycle-phase
overclaim sub-item is **separately and already tracked** — TODO.md §"Greek
vocabulary prose discipline (audit + author finding, 2026-04-29)" is *built
on this exact 471203 finding* (cites `audit-471203-incremental.md`, records
the author's independent confirmation). **That sub-item: closed for 471203,
subsumed by the live TODO Greek-vocabulary item.** I verified the README /
LEXICON "distinction English alternatives flatten" claim is *still present*
(`doc/readme/src/_overview-concepts.md:7`, `_lexicon-full-archive.md:54`,
`README-auditor.md:96`) — so the underlying issue is genuinely still open,
but it is **correctly and richly tracked** in the TODO Greek-vocabulary
section; 471203 carries no residual obligation for it.

---

## 2. extracted-gemini-feedback-2026-04-26-27 — soft-finding-heavy, self-disposed

This file is structurally different from a findings audit: it is a relayed-
feedback extract that **already carries its own `## Disposition` section**
(lines 16–25) authored at intake. Every item is dispositioned in-file:

| Gemini item | In-file disposition | My adjudication |
|---|---|---|
| Strengthening spikes to promote (bias-bound C; additive-coordinate-forcing; bridge-lemma nonlinear) | "all landed during the 2026-04-26..27 cycle" | **Verified plausible — closed.** `disc-additive-coordinate-forcing` is a landed meta-segment (referenced live in CLAUDE.md §7); the bias-bound and bridge-lemma strengthenings match CHANGELOG-class strengthen-first work. Disposition stands. |
| Opacity-gain tension → `spike-adaptive-gain-dynamics` promoted to `deriv-adaptive-gain-dynamics` | "promoted ... during this cycle" | **Trust in-file ledger** (Gemini-relay, contemporaneous, specific). Closed. |
| Findings-schema: "Domain-transfer" novelty kind | "not added — project kept kind-list compact (Synthesis/Adopted-and-extended)" | **Correctly-rejected design call.** This is the soft-finding analog of strengthen-before-soften: a proposal *considered and declined with a recorded reason*. Closed, not open. |
| Findings-schema: formal-antecedent vs conceptual-precursor split | "ADOPTED in schema; visible in `## Findings` Prior-art search" | Closed — adopted. |
| Findings-schema: literature-search date/depth capture | "captured in schema `Prior-art search` block" | Closed — adopted. |
| Undermind summary → README claim strategy | "directly shaped README Position & Lineage" | Closed — integrated. |
| README feedback items 1–3 (surface Tier-1 findings; add equations to persistence-three-senses; break Position&Lineage density) | "all addressed in same session" | **Soft-polish, in-file-closed.** These are exactly the 5%-polish register the spine protects; they were *acted on* contemporaneously. Closed. |

- **Valid in the first place?** The feedback was substantive and well-aimed
  (Gemini's epistemic-hygiene praise + the three concrete README refinements
  are high-quality soft findings).
- **Valid as of today?** The dispositions are all *closure-direction-correct*
  and contemporaneous. The one I'd flag for the parent's spot-check: the
  README has since been through the v2 / Alan-Walton-feedback cycle
  (TODO.md §"README v2 pass"), so the specific 2026-04-27 README line-edits
  may have been superseded by later README work — but "superseded by later
  README cycle" is still *closed in the right direction* (the signal was
  absorbed then iterated past, not lost).
- **What it really is:** a **self-disposed soft-feedback extract**, not an
  open findings file. Its value going forward is as **sentiment/soft-signal
  archaeology** — Gemini's "most powerful piece of exposition," "masterful,"
  "removes the implicit arrogance" sentiment is exactly the first-class
  qualitative signal the spine says past agents wrongly discarded.
- **Route:** **graduate to `audits/.integrated/` directly.** Mirror the
  three concrete README refinements + the schema decisions into the
  **polish-and-sentiment ledger** (themed "README / schema soft-findings,"
  attributed Gemini 2026-04-26..27) **with the in-file dispositions carried
  over verbatim** and a "verify-not-superseded-by-README-v2" flag on the
  three line-edits. Sentiment quotes preserved in the ledger as register-
  calibration material. Nothing here is open; nothing should go to TODO.

---

## 3. Genuinely-open items extracted from this slice (the short list)

Everything in this slice is accounted for. What is *actually still open*:

1. **Finding 7 — Tishby-Zaslavsky→Alemi citation fix, `form-information-bottleneck.md:50`.**
   Verified unapplied in current `src/`. Trivial, isolated, high-confidence,
   Phase-2-web-verified. **Spine-sanctioned direct-fix; recommend parent
   applies §L's exact suggested text, then 471203 graduates clean.** This is
   the one thing in the slice that fails "closed in the right direction"
   today.
2. **Finding 5 — `#post-composition-consistency` depends/stage.** Real,
   architectural, **but already routed** to PROPOSALS SP-6 + TODO:149 + the
   F-A cluster (584721/742613 ledgers). Does not block graduation; record the
   cross-refs in MANIFEST. The (a)-vs-(b) structural decision is Joseph's,
   correctly living in PROPOSALS.
3. **F1 — `#disc-theorem-import-architecture` fourth-meta-segment proposal.**
   Genuinely additive, **no existing PROPOSALS home** (distinct from SP-11 /
   the operator-family β-option). Surface to parent as a candidate new
   PROPOSALS entry per the audit-cycle-handling discipline.
4. **(Surfaced, not 471203's to carry) FORMAT standard-notation-exemption
   policy** (Finding 6's real residue). No tracked home anywhere today. If
   742613's disposition also punts it, it falls through the cracks — flag
   for the parent to give it *a* home (FORMAT-TODO or a PROPOSALS entry)
   independent of which audit graduates.

Everything else: closed-in-the-right-direction (resolved / correctly-
rejected-design-call / subsumed-by-later-work / duplicate-of-tracked-item) or
soft/sentiment → polish-and-sentiment ledger.

---

## 4. Frame diagnostics (candid — refines the spine before fan-out)

**(a) The "471203 has a `pending-findings` ledger" claim is false — and it
matters for the partition.** Both the brief and `msc/audit-backlog-triage-
2026-05-15.md` Group L list 471203 as a ledgered cycle. It is not:
`grep -ln 471203 audits/pending-findings-*.md` returns nothing; no
`pending-findings-*.md` covers audit-id 471203. The four ledgers cover the
2026-04-21/22/23 intakes and the **2026-04-24 fresh-pass triad** (the
2026-04-25 ledger) — *not* the 2026-04-28 de-novo cycle. **471203's durable
ledger is its own SUPPLEMENT** (`audit-471203-SUPPLEMENT-phase-2.md`), which
is functionally a pending-findings record (per-finding status, landing edits,
§N sweep, verification table). The evidence-hierarchy still resolves cleanly
(SUPPLEMENT ≈ tier-1-equivalent for this cycle; I first-hand-verified every
disposition against `src/` regardless), so no disposition changes. **But the
Group-L partition assumption "disposition should be readable from
`pending-findings-2026-04-2{1,2,3,5}.md`" is wrong for at least 471203 and
plausibly for the other 2026-04-28 FINALs (829314, and 849201 if same
shape).** Recommend the spine add a tier-1-equivalent: *"a FINAL's own
same-id `-SUPPLEMENT` carrying per-finding status + landing record counts as
the cycle's ledger."* And re-audit which Group-L files actually have a
`pending-findings` record vs. a SUPPLEMENT vs. neither — the partition
currently conflates these.

**(b) Self-disposed extract files are a distinct species the state machine
doesn't name.** `extracted-gemini-feedback-2026-04-26-27.md` arrives with its
own `## Disposition` written at intake. The state machine
(`unexamined → adjudicated → routed → integrated`) implicitly assumes the
adjudicator *generates* dispositions. For self-disposed extracts the
adjudicator's job is *verify-the-in-file-disposition-is-closure-direction-
correct + mirror-soft-signal-to-the-ledger*, which is faster and lower-risk.
Worth a named fast-path in the spine: "**self-disposed extract**: verify
in-file dispositions against `src/`/CHANGELOG, mirror soft/sentiment to
ledger, graduate." Several Group-L `extracted-*` files likely share this
shape — a quick triage of which carry a `## Disposition` section would let
the parent route a whole sub-class cheaply.

**(c) "Finding" granularity is uneven and the routing dimensionality is
higher than the brief's enum.** 471203 alone produced: 6 §B burden-of-proof
findings, 4 §B.1 self-rescinded, 4 §D hypotheses, 8 §F bigger-picture
(spanning closed-subsumed / new-PROPOSALS / research-seed / duplicate), 7 §G
process-feedback. The brief's disposition enum (defect / correctly-rejected /
architectural / soft-polish / sentiment / duplicate / already-resolved)
mostly held, but I needed three additional real categories: **subsumed-by-
later-work** (F5, F6 — distinct from "duplicate," which implies a peer audit;
this is "the project moved past it"), **research-seed** (F2/F3/F4 — softer
than architectural-PROPOSALS-entry, harder than sentiment; a real tier the
polish-ledger should theme separately), and **process/instruction-feedback**
(§G — not about the framework at all; needs its own ledger theme or it
pollutes framework tracking). Recommend the spine name these three explicitly
before fan-out — otherwise different agents will route §F-class items
inconsistently (some to PROPOSALS, some to TODO, some dropped), which is
exactly the signal-loss the cycle exists to prevent.

**(d) The polish-and-sentiment ledger needs ~4 themes, not a flat list.**
From this one slice the ledger would need: *framework-scope observations*
(§D), *research seeds* (§F2/3/4), *naming seeds* (§F8), *audit-process /
instruction improvements* (§G), *README/schema soft-findings + sentiment*
(Gemini file). A flat append-only list would re-bury the signal. The
provisional ledger decision is sound; recommend it ship with a small fixed
theme set + an attribution column + a "superseded-by?" column (the Gemini
README edits need exactly this — closed-then-iterated-past is a real status
distinct from open and from cleanly-closed).

**(e) Strengthen-before-soften had low bite on this specific slice — worth
calibrating expectations for fan-out.** The brief foregrounds the
"correctly-rejected-because-we-strengthened" category as the live
counterintuitive one. In *this* slice it barely fired: Findings 1–4 were
defects-resolved-by-strengthening (the framework's discipline *extended*, not
a claim weakened-then-defended), and the one clean "considered-and-declined"
was a soft *design* call (Gemini's Domain-transfer novelty-kind), not a math
weakening. The genuine strengthen-vs-soften rejections likely concentrate in
the **math-heavy ledgered cycles** (584721 F-A cluster, 742613, the
2026-04-25 fresh-pass triad with its P-V1/P-V2/P-V3 framing-too-strong
findings) — *not* in process/hygiene-heavy de-novo cycles like 471203 or in
soft-feedback extracts like the Gemini file. Recommend the fan-out brief
flag this: *the strengthen-before-soften reframe is load-bearing for
math/framing findings; hygiene-and-soft slices will mostly be defect-
resolved / subsumed / soft-routed, and that's correct, not a missed
rejection.* Otherwise fan-out agents may over-hunt for rejections that
aren't there in their slice and under-trust clean defect-resolutions.

**(f) One concrete spine bug:** the triage doc §"Evidence hierarchy" and the
MANIFEST both say the four ledgers are "**Decisive for the cycles they
cover** (the 2026-04-21/22/23/25 intakes: 471203 / 584721 / 613842 /
742613)" — this line **misattributes audit-ids to ledger dates**. 471203 is
2026-04-28 (no ledger); 584721/613842/742613 are 2026-04-25 FINALs covered by
context, but the `pending-findings-2026-04-25.md` is specifically the
*2026-04-24 fresh-pass triad* ledger, not a 584721/613842/742613 ledger. The
audit-id→ledger mapping in the spine is not reliable and should be rebuilt
from first-hand inspection before fan-out agents lean on it as tier-1
evidence. (This is the generalized form of finding (a).)

---

## 5. Recommended dispositions summary (for the parent's routing actions)

| Source | Disposition | Action owner |
|---|---|---|
| 471203 F1 | closed — resolved (SUPPLEMENT §H.1) | MANIFEST note |
| 471203 F2 | closed — resolved (SUPPLEMENT §H.1) | MANIFEST note |
| 471203 F3 | closed — resolved (SUPPLEMENT §H.2) | MANIFEST note |
| 471203 F4 (+§I.1) | closed — resolved comprehensively (SUPPLEMENT §H.3+§N) | MANIFEST note |
| 471203 F5 | **open-but-routed** → PROPOSALS SP-6 + TODO:149 + F-A cluster (584721/742613); does not block graduation | MANIFEST cross-ref |
| 471203 F6 | duplicate of `audit-742613-FINAL:254`; disposition follows 742613 | MANIFEST note + flag §3.4 |
| 471203 F7 | **OPEN — actionable direct-fix** (`form-information-bottleneck.md:50`, §L text) | **parent applies edit** |
| 471203 §B.1 | self-rescinded by auditor; downstream tracked elsewhere | MANIFEST note |
| 471203 §D (4) | soft → polish-and-sentiment ledger ("framework-scope observations") | parent → ledger |
| 471203 §F1 | **architectural — candidate new PROPOSALS entry** (no existing home) | parent decision |
| 471203 §F2/F3/F4 | research-seeds → ledger; PROPOSALS-candidates-if-pursued | parent → ledger |
| 471203 §F5 | closed — subsumed by class-coercion cycle | MANIFEST note |
| 471203 §F6 | closed — subsumed by TODO:386 preface-discipline | MANIFEST note |
| 471203 §F7 | closed — = PROPOSALS SP-12 | MANIFEST note |
| 471203 §F8 | soft/naming → ledger ("naming seeds") + naming-cycle xref | parent → ledger |
| 471203 §G (7) | process-feedback → ledger ("audit-process improvements"); cycle-phase sub-item closed-subsumed by TODO Greek-vocab item | parent → ledger |
| extracted-gemini-2026-04-26-27 | **self-disposed extract — graduate to `.integrated/`**; mirror soft/sentiment to ledger w/ in-file dispositions + "superseded-by-README-v2?" flag | parent → ledger + git mv |

**Graduation readiness:** `extracted-gemini-feedback-2026-04-26-27.md` is
ready now (self-disposed, verified closure-direction-correct).
`audit-471203-FINAL` + `-SUPPLEMENT` are ready to graduate **once Finding 7's
one-line citation fix is applied** (everything else closed-in-the-right-
direction or routed-to-a-live-home); the SUPPLEMENT is itself the durable
per-finding ledger and stays as the audit-trail record.

— Claude Opus 4.7 (1M context), pilot, 2026-05-15
