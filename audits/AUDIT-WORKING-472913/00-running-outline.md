# 00 — Running Outline for the FINAL report

*Living document. Updated at §4.5 strategic-loop checkpoints and after any
segment that changes my sense of report emphasis. Cycle 472913.*

## Current best guess at FINAL structure

Front matter: audit_id 472913, auditor Claude Opus 4.7 (1M ctx), date TBD,
status (full|partial TBD), audit_type de-novo-theory, coverage_summary,
priming_bleed (point at 00-initial-predictions §0 — heavy CLAUDE.md/MEMORY.md
+ OUTLINE-preamble meta-architectural priming; per-segment math still de-novo).

- **§A — Scope and method.** AAT volume only (Joseph's scope mod). OUTLINE row
  order, one segment at a time, per-segment reflection + isomorphic diagram.
  No reading delegation. Diagram modification described.
- **§B — Findings under burden of proof.** [accumulating]
- **§B.1 — Rescinded candidates.** [accumulating — the gate visibly working]
- **§C — Coverage statement.** Which segments first-hand, which math run,
  which citations checked. Grade bets B1–B7 here or §E.
- **§D — Hypothesis-tier observations.** [accumulating]
- **§E — What holds.** Where I pushed hard and the discipline held. (Important
  given heavy priming — calibration for the reader.)
- **§F — Bigger-picture observations.** [accumulating — Phase 3]
- **§G — Process feedback on the instructions** (and on the diagram
  experiment as a comprehension instrument).

## Findings ledger (working — not yet burden-of-proof filtered)

| # | seg | type | sev | conf | status | one-line |
|---|-----|------|-----|------|--------|----------|
| ~~F1~~ | scope-agency | ~~dependency-graph~~ | — | — | **RESCINDED seg 14 → §B.1** | Dissolved by the framework's own stated convention (revealed in `the-cycle-in-motion-intro` Working Notes + CIY-¶): `do(·)` = **externally-cited Pearl notation** (NOTATION.md global; external-citation machinery), `def-pearl-causal-hierarchy` = **operational recapitulation in Part II, NOT the definitional slug**. Gate-1 cond-4 ("quantity *defined elsewhere by a slug*") therefore does not bind. `scope-agency`'s parenthetical is *compliant* with the convention. Retained only as §D Hypothesis-tier *quality nicety* (Part-I self-containment in $T,h$ is cleaner — not a defect). Full reasoning: `14-the-cycle-in-motion-intro.md`. |
| F2 | post-composition-consistency | dependency-graph / scope-status / structural-placement | **High** | High (fact & against own bar) | still real — **sharpened seg 14** (NOT covered by the external-notation convention: source is an *internal* AAT slug `#result-contraction-template`, named by the segment's own `*[Derived]*` tag; the framework's careful external-notation convention makes this internal forward-derivation a *clearer* deviation) | Ch.1 *postulate* carries a `*[Derived (Conditional on Tier 1M … from #result-contraction-template …)]*` quantitative result; that source (Appendix A) + chained Section-III slugs (`form-composition-closure`, `der-team-persistence`, `der-tempo-composition`, `scope-composite-agent`) are absent from `depends:` (= `[scope-agency]` only). Gate-1 cond-4 fails at a `deps-verified` segment; `*[Derived]*` premises are downstream not prior (tag inversion); OUTLINE's own "*(possibly out of place)*" understates it. Math spot-checked sound — purely structural. Strengthen-fix: **split** — postulate stays Ch.1; migrate the Derived λ_c result to Section III/appendix where premises are prior (also discharges the OUTLINE self-flag). Full workup: `07-post-composition-consistency.md`. |
| F3 | scope-agency ↔ post-causal-structure | cross-segment-contradiction / doc-rot (terminology) | Medium-Low | High | still real | "**nominal**" denotes *opposite* scope-membership across segs 06↔08: `scope-agency` "nominal agents" = excluded from agency; `post-causal-structure` "Nominal coupling" = within agency (its "Zero coupling" is the true equivalent of scope-agency's "nominal agents"). Plus within-08 drift: bullet "Nominal coupling" vs prose "query-only coupling" = same concept. Collision sits on the load-bearing agency/adaptive seam (cf. F1). Strengthen-fix: rename bullet→"query-only coupling" (already in-08-prose); align/zero-couple `scope-agency`; consider LEXICON anchor (no canonical "nominal" entry exists). Workup: `08-post-causal-structure.md`. |
| F4 | def-chronica ↔ form-event-driven-dynamics ↔ form-agent-model | cross-segment / integration-debt / doc-rot | **Low** | Med-High | still real (Known-unintegrated; def-chronica WN) | Ordinal-state vs metric-tempo seam: $\mathcal C_t$/$M_t$ ordinal (segs 04/10 published); $\mathcal E$ metric $\tau$ + $\nu$/$\mathcal T$ metric (seg 15 + NOTATION); the relationship ($\mathcal C_t$=ordinal content of $\mathcal E$) and consequence ($M_t$ $\tau$-blind by construction; persistence inequality metric-analyst-frame while state is subjective-ordinal; sleeping/pause agents) live ONLY in `def-chronica` Working Notes + partial NOTATION $t/\tau$ cover — absent from all *published* sections where load-bearing. Strengthen-fix: lift WN→published one paragraph. THREAD-D closed into this. Also §F candidate (first-class ordinal/metric duality would sharpen persistence+chronica+Three-Deaths in one ¶). Workup: `15-form-event-driven-dynamics.md`. |
| TG1 | (tooling) | tooling-gap (recommendation) | Medium | High | open | `bin/lint-outline`/dep-checker enforces `depends:`-list topology but NOT eq-tag-cited sources: a `*[Derived (… from #X …)]*` tag whose `#X` is absent from `depends:` (or not topologically-prior) passes. A lint rule on eq-tag-cited slugs would mechanically catch the F1/F2 class. → §F / CHANGELOG-or-new-lint. |

## Rescinded / dissolved-on-search ledger

| candidate | why it dissolved |
|---|---|
| **F1** (seg 06 → rescinded seg 14) | `scope-agency` Pearl-`do` "missing dep". Dissolved by the framework's stated convention (`do` = external Pearl notation, NOT a slug-defined quantity; `def-pearl-causal-hierarchy` = Part-II operational *recapitulation* not definitional source). Honestly flagged "Phase-2 pending" at seg-06; dissolved by *in-order* de-novo reading of the convention-stating segment (seg-14). Gate self-correcting as designed. Lesson recorded → KNOWN CONVENTION below. |
| **THREAD-B** (seg 02 → dissolved seg 12) | Worry: bounded-$M_t$ Markov-by-completeness cost unnamed/under-tracked vs unbounded-$\Omega$ WLOG (seg-02 "independence" claim). Dissolved: `def-model-sufficiency` *quantifies the exact residual* as $1-S(M_t)=$ (predictive info lost by compression)/(total). Relocation target named segs 09/10/11, delivered seg 12. seg-02 "independence" retro-justified. **Foreground in FINAL §B.1 as the exemplar of the burden-of-proof gate working** (concern carried 10 segs, not inflated, dissolved on evidence). |

## §E positive calibration (where discipline demonstrably holds — for reader weighting)

- segs 01–05: foundation *strengthens* constitutive intuitions into
  operational predicates (loss→$H(\Omega\mid\mathcal C)>0$); precise
  dependency hygiene (05 deliberately omits action-transition).
- seg 08 `post-causal-structure`: textbook-clean Ch.1 postulate (axiomatic,
  no `*[Derived]*`, honest Epistemic Status, legitimate Discussion
  forward-refs) — the **in-corpus standard** F2 should be held to; its
  existence sharpens F2 (deviation, not house style).
- My F1 is correctly scoped (Formal-Expression use only), confirmed by *not*
  flagging seg-08's legitimate Discussion Pearl forward-ref.

## Working hypothesis (Phase-3 seed, Hypothesis-tier)

**Sharpened (seg 10): every finding so far is an UNSTATED RELOCATION TARGET,
not wrong content.** AAT legitimately and pervasively discharges objections
*by definition* (loss constitutive; Markov-by-breadth; completeness
tautological). Honesty = whether the relocated cost's new home is *named
in-text*. Named ⇒ exemplary (seg-10 forwards to def-model-sufficiency).
Unnamed ⇒ finding: **F1** (do-semantics' home absent from deps), **F2**
(derived-result's home downstream-unstated in deps/stage), **F3** ("nominal"'s
scope-home ambiguous across segs), **THREAD-B** (seg-02 relocation target was
unnamed → chased 8 segs → resolved once seg-10 named it). Unifying shape:
*defects are unnamed relocation targets, not wrong math.* → integration-debt
not theory-gap. **Now actively seeking disconfirmation: a genuinely wrong
*content* finding (bad math/derivation), not an unnamed relocation.** This is
the candidate §F spine.

THREAD-E upgraded: seg-10 Formal Expression states "$\phi$ many-to-one:
multiple distinct histories → same model state" *in the theory's own voice* ⇒
fork-undetectability is the framework's own unconnected consequence (→
integration debt, not auditor import). Still verify `scope-agent-identity`
carries the consequence.

**Sharpened again (seg 11): BIMODAL.** Not "integration uniformly slipping."
The *formulation/bridge layer* (segs 09,10,11) is **exemplary** —
relocation-targets named, claims tiered, downstream burdens disclaimed
by-name (seg-11 is the anti-F2). Defects (F1,F2) cluster specifically at
**forward-pressured load-bearing foundational hinges** (where AAT's strongest
results "want" to be visible early). §F headline candidate: *defects =
forward-pressure on early load-bearing segments*, remedy = the split
discipline + TG1 lint. **Disconfirmation log:** hard-checked seg-11's β-vs-ρ
double-counting claim (the one non-trivial derivable Discussion claim) — it
*holds*. 11 segs in, zero *content/math* defects found; every finding is
structural/relocational; every hard-checked claim holds. Still hunting a
content defect (intellectual honesty requires finding-or-failing-to-find one).
**Candidate distinctive-novelty pattern to watch:** AAT repeatedly does
*"disambiguation of which parameter responds to which cause"* (β=internal
cost not volatility; cf. predicted sat-gap/control-regret split) — may be the
framework's real novelty signature beyond "integration not invention". → §F.

## Live cross-segment threads (open — must be resolved before FINAL)

### KNOWN FRAMEWORK CONVENTIONS (do not re-flag — learned seg 14)

- **External-notation / recapitulation-vs-source.** Externally-cited notation
  (Pearl `do(·)`, Tishby IB, Lyapunov, Cox, Bareinboim, etc.) used in a
  Formal Expression does **not** require a `depends:` edge to the AAT segment
  that *recapitulates* that external result. `depends:`/Gate-1-cond-4 binds
  only on **slug-defined internal quantities**. AAT segments like
  `def-pearl-causal-hierarchy` are *operational recapitulations of external
  results*, not the definitional source. ⇒ Do NOT raise F1-type findings for
  external-notation forward-use. (F2 is unaffected: its source is an
  *internal* slug named by its own `*[Derived]*` tag.)

- **THREAD-A** (from seg 02; **decisive test set seg 14**).
  `the-cycle-in-motion-intro` promises `der-recursive-update` /
  `der-action-selection` are "**derived, not chosen**" *from*
  `form-agent-model`'s completeness — but seg-10 framed that completeness as a
  *formulation choice* (`type: formulation`, robust-qualitative). **Decisive
  test at `der-recursive-update`/`deriv-recursive-update`:** derivation
  honestly *conditional on the formulation-choice completeness* (correct,
  matches seg-02) — or presented as *unconditional* forcing (→ §B
  scope/status: inevitability frame on a formulation premise)? Also the
  hardest audit of FORMAT.md's "strongest result in the theory /
  inevitability-core" claim for these. initial-prediction B-cluster live.
- **THREAD-B** (from seg 02; advanced seg 09). M_t-side
  Markov-by-completeness cost vs Ω-side WLOG asymmetry. Seg-09 intro
  *foregrounds* boundedness ("finite agents compress"; "anything not in $M_t$
  lost by construction") — partially reassuring. **Sharp test localized to
  segs 10–13:** does `form-agent-model` state completeness as a modeling
  commitment *with named residual cost* (consistent w/ seg-02's
  def-action-transition framing) and does `def-model-sufficiency` quantify
  that residual? If neither does, candidate §B scope-honesty (cost discharged
  by definition, relocated cost under-tracked).

- **THREAD-C** (seg 03, low). $\varepsilon_t$ introduced; GA-1 fresh-noise
  constrains its conditional independence. Verify at
  `result-mismatch-decomposition` that GA-1 is flagged as the cross-term-
  killing assumption, not silently absorbed. (= seg-01's mismatch-decomp
  prediction, mechanism now named.)
- ~~**THREAD-D**~~ → **closed into F4** (seg 15). It was the open question;
  F4 is the finding it became.
- **THREAD-E** (seg 04, med). Non-forkable $\mathcal C_t$ + lossy forkable
  $M_t=\phi(\mathcal C_t)$ ⇒ fork introspectively undetectable when $\phi$
  not injective. §D synthesis (03⊕04). Verify `scope-agent-identity`
  carries the $\phi$-injectivity caveat; if it asserts fork-detectability
  without it → §B scope/status.

- **THREAD-F** (seg 05; refined seg 13). Two strands: (i) `scope-adaptive-
  system` $H(\Omega_t\mid\mathcal C_t)>0$ has no temporal quantifier — verify
  at persistence/identifiability results (likely GA-2 $\rho>0$ dissolves).
  (ii) predictively-non-vacuous scope (seg-12): seg-12 forward-named it to
  def-model-class-fitness & structural-adaptation-necessity; 12→13 inheritance
  is *correct* (auto-mathematical + named at source, NOT a finding). **Both
  strands converge on one high-priority check: does
  `#result-structural-adaptation-necessity` (Ch.4, FORMAT.md
  inevitability-core) carry its scope, or assert the trigger universally?**
- **TOP PART-I TARGET (from segs 09/13).** `#result-structural-adaptation-
  necessity` must pay an *inevitability-grade* promissory note (seg-09:
  "one of the framework's central results"; seg-13 deferred the substantive
  claim to it). FORMAT.md puts it in the ~15 inevitability core (bar:
  mathematical inevitability — no alternative formulation escapes). Highest-
  value Part-I verification; also the THREAD-F load-bearing test. Do full
  math-check + Gate-2 there; it is the Ch.2/Ch.4 keystone.

- **THREAD-G** (seg 07, med). Does directed separation *compose*? Working
  Notes hypothesize goal-blindness composes but coordination routing can
  break it (organizational analog of the LLM scope restriction). Verify at
  `der-directed-separation`, `hyp-directed-separation-under-composition`,
  `der-class-coercion-*`.
- **THREAD-H** (seg 07, low). Working Notes claim timescale-separation "is
  essentially the singular perturbation argument from `#der-temporal-nesting`."
  Verify at `der-temporal-nesting` that this holds / isn't over-stated.
- **DETECTOR** (standing, from F2): flag any early/foundational segment with a
  forward-`*[Derived]*` eq-tag whose cited source slug is downstream / absent
  from `depends:`. Suspected to be a *class*, not isolated.

## Recently-added structural moves to watch for cross-segment drift (§5.2)

- AAT rename (AAD→AAT) **2026-05-15 — 0 days old.** Stale "AAD" / historical-
  naming residue in non-frozen segments is a live prediction (B6).
- GUC class renumber **2026-05-09.** Pre-tag content uses old numbering.
- M4 `disc-modularity-state-dynamics` — **missing file**, forward-refed.
- `result-certificate-existence` spine — recent framing; watch local→global
  drift (B1, highest-value single check).
- Chapter-end `impl-*` segments — catalog-grade, recent distribution from the
  sunset FINDINGS-RANKED-DRAFT (2026-05-13). Watch for impl claims outrunning
  their source segments.

## Strategic-loop checkpoints log (§4.5)

- [x] **CHECKPOINT 1 (after seg 08, 2026-05-15).** Re-read 00-initial-
  predictions. Model drift assessment:
  - *Predictions holding:* B7 (OUTLINE order — no `depends:`-listed backward
    violation yet, 8/8). Finding-class mix as predicted: dependency-graph
    (F1,F2) + terminology drift (F3) leading, exactly the predicted top-2
    classes. The "priming as falsifiable promissory note" inversion is the
    single highest-yield stance (F1/F2 both found *because* I knew Pearl/
    composition were meant to be downstream).
  - *Surprise:* findings arrived **far earlier and more structural** than
    predicted — F2 (High) at seg 7, on a Chapter-1 segment the OUTLINE made
    look minor (§3.5 confirmed live). I predicted math/scope drift; the
    actual richest vein so far is *dependency/epistemic-tag honesty vs the
    framework's own Gate-1 discipline*.
  - *Plan adjustment:* (a) **DETECTOR** (forward-`*[Derived]*` in early
    segments) promoted to a standing per-segment check — F2 suggests a class.
    (b) Increase weight on **status-label / Gate-1-vs-stage** consistency
    (the `deps-verified`/`claims-verified` stamp vs actual Gate-1 cond-4) —
    this axis is paying out and is under-predicted in 00-initial-predictions.
    (c) Hold the integration-debt>theory-gap hypothesis as the Phase-3 spine
    candidate; actively seek disconfirming (a real *theory* gap, not just
    unintegrated-but-present repair).
  - *Diagram process:* two-layer vertical template + 300dpi + epistemic
    grammar stabilized at seg 07–08; per-segment diagram cost now ~1
    iteration not 3. Survey feedback delivered; conventions locked.
  - *Coverage standing:* 8 / ~130 AAT segments (Part I Ch.1 nearly done).
    Pace sustainable; no budget-gate pressure; durable resumability verified
    (ledger + numbered reflections + conventions doc on disk).
- [ ] after ~seg 18
- [ ] after ~seg 20
- [ ] after ~seg 30
- [ ] ... (continue)

## Diagram convention (locked 2026-05-15)

Joseph decided **two-layer (anchor + skeleton)**, doubling as monograph
respectful-pedagogy drafts, + epistemic-status visual grammar mirroring
FORMAT.md eq-tags + strict cross-segment colour legend + caption-blind gate +
small-multiples for dynamics. Full spec: `00-diagram-conventions.md`. Binds
seg 06→. Segs 01–05 = v1 single-layer (sound skeletons; optional end-budget
retrofit, documented). Survey feedback delivered to Joseph; gap identified
(survey is pedagogy-of-settled-content only; audit needs an epistemic-status
channel → adopted as the visual grammar).

## CADENCE CHANGE — seg 12 onward (Joseph, 2026-05-15)

"Continue. Lighter reflections, and only attempt diagrams when you really
feel they would be more useful — maybe one or two per chapter."

- **Reflections:** lighter. Walk all 14 §4.4 prompts *mentally* every
  segment; write prose **only where a prompt surfaces something** (finding,
  thread, cross-segment, prediction hit/miss, §E datum, Phase-3). No padding;
  a light segment may be a few lines. Findings still get full burden-of-proof
  workup. Ledger/threads still updated durably (the "if I dropped dead" test
  is unchanged).
- **Diagrams:** ~1–2 per *chapter*, not per segment. Make one only when it
  genuinely illuminates — a load-bearing/surprising segment, a finding worth
  seeing, or a chapter-capstone synthesis. Default = no diagram; note in the
  reflection when one was deliberately skipped and why.
- Segs 01–11 keep their diagrams (done). Chapter-1 (segs 01–08) fully
  diagrammed (v1/v2); Chapter-2 has 09–11; remaining Ch-2 segs likely get a
  single capstone if any.
- Sanctioned deviation from verbatim §4.4 (instructions are advisory;
  "what most benefits the project" governs; Joseph is authority).

## Notes to self

- Per CLAUDE.md: when something looks overclaimed, *attempt strengthening
  first*; only record a softening if strengthening honestly fails, and record
  the failed strengthening attempt too.
- Per §3.6: no "zero findings as discipline-confirmation" — if zero, list the
  places I might be missing things.
- The priming is the opportunity: treat the OUTLINE preamble's confident
  framing as falsifiable promissory notes; check the segments pay them.
