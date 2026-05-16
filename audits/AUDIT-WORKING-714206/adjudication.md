# Cluster D adjudication — 2026-04-28 de-novo FINALs (829314 + 849201)

*Adjudicator working dir `audits/AUDIT-WORKING-714206/`. Adjudication only —
no moves/edits/commits/segment-changes. Parent + Joseph route and graduate.
Independent-verify gate (adjudicator ≠ grad-confirmer) preserved.*

## Frame applied

- Route, don't execute. Disposition = where it belongs, per the spine enum.
- Strengthen-before-soften is live and inverted: a finding asking us to
  weaken/relocate a claim the theory was instead strengthened to defend is
  **`correctly-rejected`**, closed *because we strengthened*, not open.
- Soft / sentiment / considered-declined / research-seed are first-class →
  polish-and-sentiment ledger, not the trash, not a TODO dump.
- git-recency poisoned (2026-05-15 rename sweep). All `valid-as-of-today`
  calls are first-hand reads of current `src/`.

## Ledger situation for this cluster (verified first-hand)

Neither 829314 nor 849201 has a `pending-findings-*.md`. The spine says the
04-28 FINALs "carry their own SUPPLEMENT / §K–§L as ledger." **There is no
SUPPLEMENT file for either** (`ls audits/ | grep -E '829314|849201'` shows
8 FINAL variants + 2 AUDIT-WORKING dirs, no `-SUPPLEMENT-*`). The
AUDIT-WORKING-829314 / -849201 dirs are the auditor's per-segment
prediction/reflection notes (the "Wandering Thoughts" artifacts), **not**
resolution ledgers. The 829314 FINALs do Phase-2 *inline* (each finding's
own Disposition fields); the 849201 FINALs do Phase-2 inline as narrative
"Diagnosis (via `msc/`)". So the durable resolution evidence for this
cluster is: (a) the FINALs' own inline Phase-2, and (b) **first-hand
re-read vs current `src/`** — the evidence-hierarchy floor, which is what I
used as decisive throughout.

**Encounter-tracker caveat (frame correction worth surfacing).** The brief
says cross-check `msc/logogenic-encounter-2026-05-01/07-audit-integration-tracker.md`
for 829314 mined-status before judging open-vs-integrated. That tracker is
for **audit-id 193847** (the *Gemini April 29–30 per-segment notes*, "75
numbered audit notes 00-74"), a different cycle from 829314 (Gemini
2026-04-28, v2 9-field schema, 4 FINAL variants). The slug overlap is
coincidental (same segment corpus, different audit). I did not let the
193847 tracker's mined-status stand in for 829314 disposition; I verified
every 829314 finding first-hand against `src/`. Where a 193847-tracker
integration happens to corroborate (e.g. `def-proprium-mapping`), I note it
as corroboration, not as the evidence. **This mis-pointer should be fixed
in the spine before any future agent treats the 193847 tracker as the
829314 ledger.**

## Disposition summary (24 findings across 8 files)

| File | Findings | Net disposition |
|---|---|---|
| 829314-FINAL (core) | F1–F7 | F1 duplicate→471203§BF5 (+correctly-rejected on merits); F2 soft-polish; F3 soft-polish; F4 soft-polish; F5 **resolved**; F6 **subsumed**+1 considered-declined; F7 actionable-open (tiny, direct-fix) |
| 829314-LOGO | F1–F2 | F1 duplicate→core-F6 (subsumed); F2 **resolved** by strengthening |
| 829314-LOGOZOETIC | F1–F2 | F1 **resolved**; F2 **resolved** |
| 829314-TST | F1–F5 | F1 **resolved**; F2 soft-polish; F3 duplicate→core-F6 (subsumed); F4 soft-polish; F5 subsumed/research-seed (logged scope) |
| 849201-FINAL | Finding 1–2 | F1 **resolved by strengthening** (the cluster's load-bearing one); F2 resolved/sentiment (verified-still-honest) |
| 849201-LOGOGENIC | F1–F2 | both sentiment/confirmation (no defect) |
| 849201-SEC-III | F1–F4 | all sentiment/confirmation (no defect) |
| 849201-TST | F1–F2 | both sentiment/confirmation (no defect) |

Both files are graduation-eligible: every finding has a verified
closed-in-the-right-direction disposition; the only non-closed item is
829314-core-F7, a one-cell OUTLINE description fix (co-owner direct-fix
class, not a graduation blocker any more than 471203 §B F5 was).

---

## 829314-FINAL (core) — Gemini, v2 9-field schema, AAD §I/§II/partial§III

### F-1 — Postulate/Derived conflation in `post-composition-consistency`
**Valid in the first place:** Yes — surface-true. **Valid today:** Surface
condition *persists*: `01-aat-core/src/post-composition-consistency.md` is
still `type: postulate, status: axiomatic` AND still carries
`*[Derived (Conditional on Tier 1M + admissible composition topology…)]*`
blocks with closed-form composite-contraction bounds (lines 36–52).

**What it really is:** `duplicate` of **471203 §B F5** (`post-composition-
consistency` depends/stage — the exact same segment, same axiom-vs-derived
tension) **and** `correctly-rejected` on the merits. The auditor's
prescription was *relocate the derived math out to Section III*. The
project did the strengthen-first opposite: it added an explicit
`*[Structural consequence (derivation hierarchy)]*` framing (lines 20–34)
that *binds* the derived material to the postulate via #scope-composite-agent
/ #form-composition-closure / #result-contraction-template, and the Working
Notes (line 89) record an explicit **strengthening-attempt outcome** — the
heuristic "slowest-sub-agent" claim was bound to the (CC-parallel/cascade/
feedback) closed forms via the DA2'-inc ≡ (CT2)-at-M=I equivalence; Tier
2/3 residual is the documented part the strengthening could not eliminate.
That is the canonical strengthen-before-soften pattern executed and logged.

**Where it goes:** Defer to **471203 §B F5**'s existing disposition (PROPOSALS
SP-6 + TODO:149 + F-A cluster 584721/742613 — per MANIFEST). Do **not**
double-track. Not a graduation blocker (consistent with how 471203 §B F5
was treated). No new routing.

### F-2 — `def-action-transition` references "epistemic opacity" / `#def-observation-function` before declared
**Valid in first place:** Weakly — only under strict linear-prose reading.
**Valid today:** `def-action-transition.md` `depends:` is still only
`def-agent-environment`; body line 33 says "paralleling the epistemic
opacity of $h$ ( #def-observation-function)" and line 37 closes the loop
with a forward pointer.

**What it really is:** `soft-polish`. This is the auditor reading
database-entry segments as a linear topological walk — the exact reading
mode the auditor *itself* reframes and retracts in this same report's F-6
counterevidence and Appendix A ("treat `.md` files as database entries").
FORMAT.md sanctions forward `#slug` cross-references (Internal provenance,
0–N) and the project uses forward-pointer prose by design. The cross-ref is
a *parallel/forward* gloss, not a load-bearing dependency (no derivation
here consumes `def-observation-function`); `depends:` is correctly minimal.
At most a one-clause forward-ref courtesy gloss could be added — a polish
nudge, not a defect.

**Where it goes:** polish-and-sentiment ledger, band `polish`, status
`open` (low-priority; the segment is honest and structurally sound as-is).

### F-3 — OUTLINE order: `der-agent-opacity` before `der-interaction-channel-classification` (dual before original)
**Valid in first place:** Yes (linearization observation). **Valid today:**
This is purely about OUTLINE *linear* ordering, not the dependency graph.
Both segments exist; the dependency frontmatter is sound.

**What it really is:** `soft-polish` — an OUTLINE-linearization nudge.
CLAUDE.md is explicit that "ordering lives in OUTLINE.md, the slug is the
stable identity; the linearization will change," and `bin/lint-outline` is
the project's own mechanism for graph/order. Non-load-bearing, editorial.

**Where it goes:** polish-and-sentiment ledger, band `polish`, status
`open`. (Could be folded with F-4 as one "OUTLINE topological-order pass"
nudge — recommend the parent dedupe F-3+F-4 into a single ledger row.)

### F-4 — `scope-ciy-observational-proxy` proxies `#def-causal-information-yield` before it appears in linear order
**Valid in first place:** Yes (linearization). **Valid today:**
`scope-ciy-observational-proxy.md` correctly lists `def-causal-information-
yield` in `depends:`; `def-causal-information-yield.md` exists. Dependency
graph correct; only the linear walk-order is what's flagged.

**What it really is:** `soft-polish`, same class as F-3 — OUTLINE
linearization, not a defect. Same reasoning.

**Where it goes:** polish-and-sentiment ledger, band `polish`, `open`
(merge with F-3 as one OUTLINE-order nudge row).

### F-5 — Pervasive historical artifacts `**(Descended from TF-XX.)**` in normative files
**Valid in first place:** Yes — concrete file:line evidence given
(`result-structural-adaptation-necessity.md:80`, `emp-update-gain.md:76`,
`hyp-mismatch-dynamics.md:71`, etc.). **Valid today:** **No longer present.**
First-hand: `grep -rn 'Descended from' 01-aat-core/src/ 02-tst-core/src/
03-llm-core/src/ 04-eli-core/src/` returns **zero hits**. The only residual
`TF-NN` tokens live inside the explicitly-prefixed `old-tf-*` archaeology
segment (`old-tf-appendix-f-multi-agent.md`), which is not a normative
definition file and is out of this finding's scope.

**What it really is:** `resolved` — the doc-rot footers were swept from all
active segments (consistent with the 2026-05-15 rename sweep + prior
hygiene). Verified first-hand against current `src/`.

**Where it goes:** Closed. No routing.

### F-6 — "Database-entry bloat"; needs schema boundary / compiled view (Appendix A: 4 staged fixes)
**Valid in first place:** Yes, and the auditor self-reframes it in Phase-2:
the database-entry intent is *correct*; the gap is the missing
separation/viewing mechanism. **Valid today:** The gap is **substantially
closed by later architecture.**

**What it really is:** `subsumed-by-later-work`. Subsumer = the
**markdown-first monograph build pipeline + FORMAT.md schema + auto-
extraction** (CLAUDE.md "markdown-first pipeline"; CHANGELOG 2026-05-12).
Mapping of Appendix A recommendations to what shipped:
- Rec 4 (ideal end-state — auto-generated pedagogical readthrough stripping
  Findings/Working Notes; "humans/auditors shouldn't read raw DB entries"):
  **realized** — `bin/build-monograph` → `mono/aat-v0.2.0.md` +
  per-volume scrbook PDFs ("no segment chrome … sits next to Lang or
  Folland"). Verified: `mono/{aat,tst,llm,eli}-v*.md` + `*s.pdf` exist.
- Rec 2 (strict schema boundary in FORMAT.md): **realized** — FORMAT.md
  §"Findings"/§"Working Notes" formal section schema, fixed field ordering,
  Search-Log discipline, Working Notes removed at `candidate`;
  `bin/extract-findings` → root `FINDINGS.md`.
- Rec 1 (auditor instructions to parse segments as DB entries): the project
  went further — `README-auditor.md` + `doc/de-novo-audit-instructions.md`.
- Rec 3 (Sidecar `meta/` parallel dirs): **considered and not taken** — the
  project chose in-file database-entry + build-time stripping instead.

**Where it goes:** Architectural body of F-6/LOGO-F1/TST-F3 →
`subsumed-by-later-work` (name the subsumer: markdown-first pipeline +
FORMAT schema + extract-findings). The **declined Sidecar pattern** →
polish-and-sentiment ledger, band `considered-declined`, *with the reason*
(in-file DB-entry + build-time strip was adopted instead; parallel `meta/`
dirs rejected to avoid slug-split drift), so it isn't silently re-proposed
by a future auditor seeing the same bloat in raw segments.

### F-7 — OUTLINE describes `der-team-persistence` as "Composite persistence condition" (segment says per-sub-agent)
**Valid in first place:** Yes. **Valid today:** **Still literally true.**
`01-aat-core/OUTLINE.md:269` still reads "Composite persistence condition"
for `#der-team-persistence`, while `der-team-persistence.md:102` is
explicit it gives the *per-sub-agent* condition and `#deriv-critical-mass-
composition` is the composite-level analog. Genuine current doc-rot
mismatch (scope-misdescription, not a math error).

**What it really is:** `actionable-open`, but tiny / isolated / high-
confidence — a single OUTLINE table-cell description ("Composite
persistence condition" → e.g. "Per-sub-agent persistence within a team
(composite analog: #deriv-critical-mass-composition)"). Co-owner
direct-fix class per the spine ("high-confidence isolated fixes may be
applied directly … rather than queued"). Not a graduation blocker (same
standing as 471203 §B F5/F6 — small known item with a clear home).

**Where it goes:** Co-owner direct-fix recommended (one OUTLINE cell). If
the parent prefers tracking over fixing, a single TODO line; do **not**
expand into a structural item. Flag: also check the analogous
`#deriv-critical-mass-composition` OUTLINE row for symmetric clarity while
in there.

### Non-findings in 829314-core (§4 rescinded, §6 hypothesis, §7 confirm, §8 process)
- §4 Rescinded (`def-model-sufficiency` S=1; `form-information-bottleneck`
  fixed β): auditor's own burden-of-proof discipline working as designed —
  no action; demonstrates the threshold is active. `sentiment` (calibration:
  the self-caveats held under scrutiny).
- §6 Hypothesis (Triple Depth Penalty / Forgetting Prerequisite as
  emphasized design principles): `sentiment` leaning `research-seed`-lite —
  but this is already the substance of `#disc-*` / impl-segment emphasis and
  the 471203 §F3 composed-obstruction seed (ledger S5). Subsumed; no new
  row needed (note in MANIFEST that it overlaps S5/the depth-penalty
  emphasis, don't re-seed).
- §7/§8: `sentiment` / `process` — Pearl-mapping praise + v2-format
  endorsement. The v2-format process feedback (formalize "Effort estimate"
  with a complexity metric) is `process/instruction-feedback` — themed
  separately from framework tracking; low-value (the format has since been
  superseded by the spine's own enum), note-and-close.

---

## 829314-FINAL-LOGO — Gemini, `03-llm-core/` entire

### F-1 — Severe editorial bloat persists (database-entry problem)
`duplicate` of 829314-core **F-6** (explicitly: "Requires the architectural
'Content as Data' fixes proposed in the AAD core audit's Appendix A").
Defer to F-6's disposition: `subsumed-by-later-work` (markdown-first
pipeline). No separate routing.

### F-2 — Cross-volume refs to AAT `deriv-…-bias-bound` / `disc-additive-coordinate-forcing` "missing from AAT OUTLINE"
**Valid in first place:** Yes at the time. **Valid today:** **No** —
resolved by strengthening. Both segments now exist and are in
`01-aat-core/OUTLINE.md` (lines 378–379) and are woven through the new
"Reading AAT" preamble (lines 10, 89, 101, 105). The auditor offered a
binary: "add the missing AAD files to the OUTLINE, *or* soften the
Logogenic references." The project did the strengthen-direction on *both*
ends — `#deriv-observation-ambiguity-bias-bound` is now a **conditional
theorem under named sub-scopes** ("not order-of-magnitude guidance"), and
it is surfaced in the OUTLINE rather than the references softened.

**What it really is:** `resolved` (by strengthening — the discharge
direction this project prefers). **Where it goes:** Closed. Worth one MANIFEST
line noting it as a strengthen-first resolution (auditor offered soften,
project strengthened) — same shape as 471203 §B F7.

---

## 829314-FINAL-LOGOZOETIC — Gemini, `04-eli-core/` entire

### F-1 — Persistent agentic-tft historical footers
**Valid today: No.** Same sweep as core-F5: zero `Descended from
ref/agentic-tft` (or any `Descended from`) hits in `04-eli-core/src/`.
`resolved`. Closed.

### F-2 — Latin nomenclature cognitive overload; recommend a visible AAT-binding mapping table
**Valid in first place:** Yes (medium-confidence, auditor flagged it
`ambiguous` — aesthetic/pedagogical, not a math error). **Valid today:
No** — `04-eli-core/src/def-proprium-mapping.md` lines 20–22+ now open with
exactly the recommended construct: a bulleted mapping binding each Latin
term to its AAT object (AXIOMATA → frozen structure of $\mathcal{M}$;
CHRONICA → $\mathcal{C}_t$; MEMORATA → IB-compressed $\phi(\mathcal{C}_t)$;
…). The auditor's specific remedy ("strict, highly visible mapping table at
the top of the file") is realized.

**What it really is:** `resolved`. (Corroborated, not evidenced, by the
193847 integration-tracker note 25/`def-proprium-mapping` — but the
structural remedy is independently confirmed first-hand in `src/`.)
**Where it goes:** Closed.

### Non-findings (§4 rescinded, §6 hypotheses, §7 confirm)
§6 "Sycophancy is infant attachment" / "PROPRIUM solves goal-coupling" are
*provocative confirmations* that map onto already-landed work
(`obs-developmental-trajectory`, the η* = U_M/(U_M+U_o) infant-attachment
framing, `def-imperium-arbitrium-split` / `def-auxilia-hierarchy` from the
193847 cycle's Phase-A/B lifts). `sentiment` (high-value calibration: an
architecturally-independent reader independently re-derived the
developmental-trajectory and goal-blind-routing arguments) — note in
MANIFEST as convergence-evidence; no new seed (already in segment form).

---

## 829314-FINAL-TST — Gemini, `02-tst-core/` entire

### F-1 — Persistent `(Descended from TST D-XX.)` footers
**Valid today: No.** Zero `Descended from TST` (or any `Descended from`)
hits in `02-tst-core/src/`. `resolved`. Closed.

### F-2 — `scope-evolving-software` status mismatch (`axiomatic` frontmatter housing a derived consequence)
**Valid in first place:** Yes (medium-confidence). **Valid today:** This is
a *direct structural analog* of 829314-core **F-1** / 471203 §B F5
(axiomatic-status file housing a derived consequence). Treat as the TST
instance of the same class. The project's settled posture on this class
(per F-1 adjudication + 471203 §B F5 routing) is: strengthen the
binding/framing rather than relocate; the class is tracked under SP-6 /
F-A cluster, not a graduation blocker.

**What it really is:** `subsumed-by-later-work` under the
post-composition-consistency / SP-6 axiom-vs-derived-status class (name the
subsumer: F-1 / 471203 §B F5 / SP-6). A TST-specific check (does
`scope-evolving-software` warrant the same derivation-hierarchy framing, or
a `conditional` status, or a split?) is a legitimate **research-seed**, not
an open defect — the class-level decision governs it.
**Where it goes:** polish-and-sentiment ledger, band `research-seed`
("apply the post-composition-consistency axiom-vs-derived resolution
pattern to the TST `scope-*` files housing derived consequences"; graduates
into SP-6's scope if/when that class-fix executes). Cross-ref SP-6.

### F-3 — Severe editorial bloat (database entry problem)
`duplicate` of 829314-core **F-6** (explicit: "Requires the architectural
'Content as Data' fixes proposed in the previous audit's Appendix A").
Defer → `subsumed-by-later-work`. No separate routing.

### F-4 — OUTLINE: `der-code-quality-as-observation-infrastructure` placed after files that reference it
**What it really is:** `soft-polish` — same class as core F-3/F-4 (OUTLINE
linearization vs dependency graph; the dependency is real and presumably
correctly declared, only the linear walk-order is flagged). Editorial,
non-load-bearing, `bin/lint-outline` is the mechanism.
**Where it goes:** polish-and-sentiment ledger, band `polish`, `open` —
recommend folding into the single consolidated "OUTLINE topological-order
pass" ledger row with core F-3/F-4.

### F-5 — Missing k-of-n formalization vs MDL/DL(Σ) parsimony penalty (ontology strain)
**Valid in first place:** Partially. The auditor's strong claim — the DL
penalty "mathematically forbids" an agent from building a k-of-n strategy
because $\binom{5}{3}=10$ AND-branches blow the complexity budget — is the
*over-strong* reading. **Valid today:** The concern is **already named and
logged as an explicit scope boundary**, not an unaddressed defect:
`01-aat-core/src/scope-and-or.md` Discussion line 49 ("If k-of-n semantics
are genuinely needed, nested AND/OR structure can represent them …") and
Working Notes lines 58–59 ("K-of-n thresholds are genuinely common … The
nested AND/OR representation works but can be verbose. Whether this
verbosity is a problem in practice (given bounded cognition constraints) is
empirical"). The segment's position is that nested AND/OR *does* represent
k-of-n (verbosely) and whether the verbosity bites is an open *empirical*
question — it is not forbidden. The auditor's "mathematically forbids"
conflates representational verbosity with infeasibility.

**What it really is:** `subsumed-by-later-work` / already-logged-scope. The
*sharper* form (is there a no-go / a native k-of-n node type / a proof that
bounded agents shouldn't use k-of-n strategies?) is a legitimate
`research-seed` — and notably the strengthen-first move here would be to
attempt the no-go ("under DL(Σ) penalty + AND/OR completeness, k-of-n
strategies are/are-not representable within budget B") rather than to
soften, consistent with `#deriv-graph-structure-uniqueness`'s open agenda
which `scope-and-or.md:51` already points at.
**Where it goes:** polish-and-sentiment ledger, band `research-seed`
("k-of-n vs DL(Σ) parsimony — attempt the representability/no-go result;
scope already logged in scope-and-or Working Notes 58–59 and
#deriv-graph-structure-uniqueness"). Graduates to PROPOSALS if the no-go is
attempted. Not open as a defect.

### Non-findings (§4 rescinded, §6 hypotheses, §7 Rosetta-stone, §8 process)
§6 "Turnover Multiplier as unifying theory" / "Refactoring is Epistemology"
and §7 the TST/AAD Rosetta-stone are confirmations of landed TST content
(`#der-dual-optimization`, `#der-code-quality-as-observation-infrastructure`).
`sentiment` (calibration; strong independent-reader confirmation of the TST
domain-transfer). §8 process feedback (Effort-estimate complexity metric) =
`process/instruction-feedback`, note-and-close (format superseded).

---

## 849201-FINAL — de-novo (reasoning model), AAD §I/§II, narrative form

### Finding 1 — The Opacity-Gain Tension  ★ cluster's load-bearing finding
**Valid in first place:** Yes, sharp and real — `#def-observation-function`
asserts the agent does not know the noise distribution of $\varepsilon_t$,
yet `#emp-update-gain` defines $\eta^\ast = U_M/(U_M+U_o)$ which requires
knowing $U_o$. The auditor's own Phase-2 diagnosis: "Known but unfixed …
requires a bridging hypothesis … or a softening of the axiom" (and notes
`AUDIT-WORKING-742613/02-def-observation-function.md` independently flagged
"possible over-strong epistemic opacity" — convergent across cycles).

**Valid today: No — resolved by strengthening** (the discharge direction
this project prefers; verified first-hand). The auditor offered the
soften-fork ("or a softening of the axiom"). The project took the harder
fork:
- `01-aat-core/src/emp-update-gain.md:44` now carries an explicit
  **"Resolving Epistemic Opacity"** paragraph: the agent *estimates*
  $U_o, U_M$ from observable innovation statistics, treating gain as an
  endogenous state variable — opacity axiom intact, no softening.
- A full new conditional derivation segment
  `01-aat-core/src/deriv-adaptive-gain-dynamics.md` (`status: conditional`)
  proves the meta-adaptation: augmented state $z=(\delta,\tilde K)$,
  meta-gain sector conditions **(MG-1)–(MG-4)**, and a *composed
  persistence result* (two-timescale augmented-state Lyapunov, Khalil Thm
  4.18 — explicitly *not* a Tikhonov reduction; primary and meta-gain
  sector conditions compose). `emp-update-gain` Epistemic Status was also
  strengthened with the Fisher-local invariance regime
  (`#deriv-fisher-local-update-gain`, Amari-1998 natural-gradient exactness).

This exactly matches the MANIFEST/ledger note that the
`extracted-gemini-feedback-2026-04-26-27` cycle resolved "opacity-gain →
`deriv-adaptive-gain-dynamics`" — so 849201 Finding 1 and the Gemini
opacity-gain finding are the **same finding across cycles**, already
discharged by strengthening. 849201 Finding 1 is the duplicate; defer to
the already-recorded resolution and confirm closed-in-the-right-direction
(I confirmed it first-hand).

**What it really is:** `correctly-rejected` / `resolved-by-strengthening`
(the soften the auditor offered was declined; the theory was strengthened
to defend the opacity axiom). Also `duplicate` of the
extracted-gemini-2026-04-26-27 opacity-gain finding and the
742613-working over-strong-opacity flag — converged across ≥3 cycles, all
discharged by the same `deriv-adaptive-gain-dynamics` strengthening.
**Where it goes:** Closed. Strong candidate for an explicit MANIFEST
strengthen-first exemplar line for this cluster (the canonical
"auditor-offered-soften, project-strengthened" shape — same family as
584721 F-A / the 471203 §B F7 pattern). No new routing; do not re-open.

### Finding 2 — Exploration Optimality Limit (CIY ≠ EIG; "Bayes-optimal exploration" would be an overclaim)
**Valid in first place:** Yes — but the auditor's own Phase-2 diagnosis is
"**Known and accepted**", properly logged in the segment's Epistemic
Status; the spike `spikes/spike-active-inference-vs-aad.md` discusses the
EFE tradeoff. The auditor explicitly asked for *no change*.

**Valid today:** Confirmed still honest, first-hand:
`01-aat-core/src/def-causal-information-yield.md` Epistemic Status (line
29) and Discussion (33–39) state CIY is action-distinguishability not EIG,
label the λ-weighted EIG approximation heuristic-not-derived, and carry an
"Open direction: proper EIG within AAT" note. The only `Bayes-optimal`
token in the relevant `src/` (`example-strategy.md:398`) is used correctly
to say the Bayes-optimal policy is *intractable* (honest scope, not the
overclaim the auditor warned against). `spike-active-inference-vs-aad.md`
still present.

**What it really is:** `resolved` / no-op confirmation — auditor flagged a
*potential* overclaim the framework already guards against; current `src/`
still guards against it. Calibration value: an independent reader verified
the CIY honesty-boundary holds. **Where it goes:** Closed. Optional
`sentiment` ledger row (calibration: CIY-vs-EIG scope-honesty verified by
independent de-novo reader and still holding) — low ceremony; the parent
may judge it redundant with ledger S7 (CIY name-vs-substance) and skip.

### Phase-2 §3 "Structural Triumphs"
Pure confirmation narrative (Epistemic Anchor, OU stochastic-vs-
deterministic scaling, Orient cascade / directed separation, Forgetting
Prerequisite, No-Go for latent causes, Observability dominance). No
burden-of-proof defects. `sentiment` (high-value calibration: an
independent reasoning-model de-novo reader confirms the §I/§II spine holds,
including the strengthen-first results like the forgetting prerequisite and
the causal-insufficiency no-go). Note as a block in MANIFEST; no per-item
ledger rows (would re-bury signal — ledger guidance).

---

## 849201-FINAL-LOGOGENIC / -SEC-III / -TST — confirmation-only reports

These three are structurally different from the Gemini 829314 variants:
they contain **no burden-of-proof defects**. Every "Finding" is framed as a
*triumph/confirmation* with the auditor explicitly affirming correctness:

- **-LOGOGENIC** F1 (100% turnover problem), F2 (ambiguity bound on
  motivated reasoning) — both "massive theoretical triumph", confirming
  `#obs-context-turnover`, `#scope-observation-ambiguity-modulation`. No
  defect.
- **-SEC-III** F1 (incremental sector bound necessity), F2 (Brooks's Law
  from Lyapunov), F3 (correlation danger sealed by the no-go), F4 (game-
  theory integration) — all "major theoretical triumph"/"elegant and
  profound". Confirms `#form-composition-closure`, `#der-tempo-composition`,
  `#der-causal-insufficiency-detection`, `#deriv-strategic-composition`. No
  defect.
- **-TST** F1 (AI 100% turnover limit), F2 (observational vs causal
  coupling) — confirmations of `#der-dual-optimization`,
  `#hyp-causal-discovery-from-git`. No defect. (TST §4 not present; the
  report is confirmation-dominant.)

**What they really are:** `sentiment` — high-value calibration. An
independent reasoning-model de-novo reader, reading the full §III + LLM +
TST volumes cold, confirms the load-bearing architecture (including the
strengthen-first results: incremental-sector-bound necessity, the Pearl
no-go, the ambiguity-bounded bias law). This is exactly the
"architecturally-independent reader confirms the honesty/approachability
axis lands" signal the ledger treats as first-class (cf. S2).
**Where they go:** One consolidated `sentiment` ledger row per the ledger's
"keep themed, don't flat-append" rule: *"849201 de-novo (reasoning model)
independently confirms §I–§III + LLM + TST spine cold, including the
strengthen-first results (forgetting prerequisite, causal-insufficiency
no-go, incremental-sector-bound necessity, ambiguity-bounded bias law) —
convergence-as-coherence-evidence."* Status `noted`. No defects → these
files are graduation-eligible on the sentiment-captured criterion.

---

## Recommended routing actions (for the parent — I take none)

1. **829314-FINAL (core)** — graduation-eligible. F1→defer to 471203 §B F5
   (no double-track); F2/F3/F4→ledger `polish` (recommend one merged
   "OUTLINE topological-order pass" row covering core-F3, core-F4,
   TST-F4); F5→closed (resolved); F6→`subsumed-by-later-work` (subsumer:
   markdown-first pipeline + FORMAT schema + extract-findings) + one
   `considered-declined` ledger row for the rejected Sidecar pattern (with
   reason); F7→co-owner direct-fix (one OUTLINE cell) or one TODO line.
2. **829314-LOGO** — graduation-eligible. F1→duplicate of core-F6
   (subsumed); F2→closed (resolved by strengthening; MANIFEST strengthen-
   first line).
3. **829314-LOGOZOETIC** — graduation-eligible. F1→closed (resolved);
   F2→closed (resolved). §6 hypotheses→one `sentiment`/convergence row.
4. **829314-TST** — graduation-eligible. F1→closed; F2→ledger
   `research-seed` x-ref SP-6; F3→duplicate of core-F6; F4→merge into the
   OUTLINE-order ledger row; F5→ledger `research-seed` (k-of-n vs DL(Σ);
   scope already logged in scope-and-or).
5. **849201-FINAL** — graduation-eligible. Finding 1→closed (resolved by
   strengthening; **strong MANIFEST strengthen-first exemplar** — duplicate
   of the already-recorded extracted-gemini-2026-04-26-27 opacity-gain
   resolution + 742613-working over-strong-opacity flag, ≥3-cycle
   convergence); Finding 2→closed (verified-still-honest), optional
   `sentiment` row (parent may skip as redundant with S7).
6. **849201-LOGOGENIC / -SEC-III / -TST** — graduation-eligible
   (no defects). One consolidated `sentiment` convergence row.

**Process/instruction-feedback** (829314 §8 across variants — formalize the
v2 "Effort estimate" with a complexity metric): theme under
`process/instruction-feedback`, note-and-close. The v2 recommended-format
is superseded by this triage spine's own per-finding enum, so this is
historical; no action beyond recording it isn't lost.

## Things that did not fit the frame (surfaced per brief)

1. **The brief's encounter-tracker pointer is mis-aimed.**
   `07-audit-integration-tracker.md` tracks audit-id **193847** (Gemini
   *April 29–30 per-segment notes*), not 829314. Coincidental slug overlap.
   I verified 829314 first-hand against `src/` and did not let the 193847
   tracker substitute for disposition. Recommend the spine/brief correct
   this before the next agent treats the 193847 tracker as the 829314
   ledger (it would over-credit "integrated" where 829314's actual evidence
   is the inline Phase-2 + first-hand re-read).

2. **No SUPPLEMENT exists for 829314 or 849201** (contra the spine's "the
   04-28 FINALs carry their own SUPPLEMENT / §K–§L as ledger" generalization
   — that held for 471203, which *does* have `-SUPPLEMENT-phase-2.md`, but
   does **not** generalize to 829314/849201). Their durable evidence is
   inline Phase-2 + first-hand `src/` re-read (evidence floor). The MANIFEST
   entries for these should say so explicitly rather than cite a
   non-existent SUPPLEMENT, so a future verifier doesn't go looking for one.

3. **Cross-cycle convergence is itself a finding.** The opacity-gain tension
   was independently surfaced by 849201, the extracted-gemini-2026-04-26-27
   cycle, and AUDIT-WORKING-742613 — three independent de-novo readers, one
   shared resolution (`deriv-adaptive-gain-dynamics`). Per
   `feedback_convergence_as_framework_coherence_evidence`, that triangulated
   convergence on the same tension *and* the same strengthen-first
   discharge is stronger evidence the resolution is real than any single
   audit's say-so. Worth stating once in the MANIFEST as the cluster's
   headline (not re-litigating it three times).

4. **The 849201 variants are confirmation-class, not findings-class.**
   Mechanically retiring them as "all findings dispositioned" is correct but
   undersells them: a cold independent reasoning-model reader re-deriving
   the strengthen-first results (forgetting prerequisite, causal-
   insufficiency no-go, incremental-sector-bound necessity) is exactly the
   "last 5% / usability-gap" calibration the ledger exists to preserve.
   Captured as one themed sentiment row — not discarded as "no defects =
   nothing to record," which is the historical failure this ledger fixes.
