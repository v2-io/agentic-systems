# Audit-backlog triage — live spine (started 2026-05-15)

The working spine for retiring the `audits/` standalone backlog. Output
audit-trail is [`audits/.integrated/MANIFEST.md`](../audits/.integrated/MANIFEST.md);
this file is the in-flight rendezvous (multi-agent cadence: a modifying
pass and an *independent* verifying pass meet here; state machine below).

## The job (Joseph's framing, 2026-05-15)

> *"The job isn't to do what the audit said to do — the job is to take the
> findings, figure out what is and what is not valid (especially 'valid as
> of today' — but valid in the first place), and route it to the right
> place."*

Consequences that shape every decision here:

- **Route, don't execute.** A finding's disposition is *where it belongs*,
  not *whether we did what it asked*.
- **Strengthen-before-soften is live and inverted-from-naive.** We *often
  reject* auditor findings — especially ones asking us to weaken a claim
  the theory was instead strengthened to defend. A rejected-because-we-
  strengthened finding is **correctly closed**, not open. (See
  `~/.claude/memory/epistemic-discipline/strengthen-before-soften.md`.)
- **Soft / idea / sentiment findings are first-class.** The "this is good —
  here's what would make it better" register (Gemini especially) and
  qualitative sentiment ("§X is delightful; §Y confused me") have been
  systematically discarded by past agents as noise. Joseph: *"the last 5%
  of polish provides 50–90% of the usability-gap coverage."* These get a
  durable home (below), not the trash and not a TODO dump.
- **`TODO.md` is not the sink.** It already trends toward unwieldy →
  duplicate → runaway. High-confidence isolated fixes may be applied
  directly (co-owner's call) rather than queued; architectural moves go to
  `PROPOSALS.md`; soft/sentiment goes to the ledger below; only genuinely
  actionable, non-duplicate, tracked work goes to TODO.

## Soft-findings / sentiment home — decision (co-owner call; provisional)

Joseph deferred the organization of soft findings/ideas/sentiment to me.
Decision: a dedicated low-ceremony curated ledger
**`audits/polish-and-sentiment-ledger.md`** — themed, deduplicated,
attributed, with a routed-status column. Rationale: `PROPOSALS.md`'s
heavy schema (thesis/merits/scope/…) is right for architectural moves but
would lose lightweight polish nudges and sentiment; a curated ledger keeps
the 5%-polish signal recoverable so an audit can be retired as *fully
accounted for*. Genuinely-architectural soft findings still graduate to
PROPOSALS; tiny high-confidence ones may just be fixed. **Created
2026-05-15** as [`audits/polish-and-sentiment-ledger.md`](../audits/polish-and-sentiment-ledger.md)
after pilot 583046 validated the design and surfaced the schema: bands
`polish` / `sentiment` / `considered-declined` (the reason is the
payload — declined ideas must not be silently re-dropped) / `research-seed`
(graduates to PROPOSALS if it matures); status vocab includes
`superseded-by` — the closed-then-iterated-past status the pilot flagged
would otherwise mis-read as still-open — and `→ SP-NN` for graduation.

## Evidence hierarchy

See the MANIFEST §"Evidence hierarchy". Summary: `pending-findings-*.md`
ledgers ≻ CHANGELOG narratives ≻ open-`[ ]` TODO/PROPOSALS backlinks
(sufficient for NOT-integrated; absence not sufficient for integrated) ≻
first-hand re-read vs current `src/`. **`git`-recency is poisoned** by the
2026-05-15 rename sweep — do not use it.

## Partition (hypotheses — to be VERIFIED, not assumed)

51 top-level files in `audits/`. Grouped by *what evidence is expected to
govern them*, not by presumed status. Status starts `unexamined` for all.

> **Corrected 2026-05-15 (pilot 583046, primary-source-verified).** The
> audit-id→ledger-date mapping is NOT reliable and must not be assumed.
> No `pending-findings-*.md` references audit-id 471203. The four
> ledgers cover the **2026-04-22 and 2026-04-23 de-novo intakes and the
> 2026-04-24 fresh-pass triad only**.
>
> **Re-corrected 2026-05-16 (fan-out cluster D, primary-source-verified).**
> "2026-04-28 FINALs carry their own SUPPLEMENT as ledger" held **only
> for 471203**. `829314` and `849201` have **no SUPPLEMENT and no
> `pending-findings` file** — durable evidence is the FINAL's own inline
> Phase-2 / §K notes + first-hand re-read of current `src/`. Confirm each
> file's actual ledger first-hand; never infer it from the audit-id, and
> never assume a SUPPLEMENT exists. Also: the encounter tracker
> `msc/logogenic-encounter-2026-05-01/07-audit-integration-tracker.md`
> tracks audit-id **193847**, not 829314 (coincidental digit overlap) —
> not a 829314 integration record.

- **Group L — ledgered cycles (2026-04-22 → 25 intakes).** Disposition
  readable from the cycle's *actual* ledger (a `pending-findings-*.md`
  for the 04-22/23/24-fresh-pass intakes; the cycle's own SUPPLEMENT for
  the 04-28 FINALs) + CHANGELOG, then spot-checked first-hand. Files: the
  four `pending-findings-*` (the
  ledgers themselves — these *stay*, they are the durable record),
  `audit-471203-FINAL` + `-SUPPLEMENT-phase-2`, `audit-584721-FINAL`,
  `audit-613842-FINAL`, `audit-742613-FINAL` + `-SUPPLEMENT-PHASE-2-TRIAGE`,
  `audit-849201-FINAL*` (4), `opus-audit-2026-04-21`,
  `audit-2026-04-24-fresh-pass`, `audit-final-reports-candidate-extraction-2026-04-25`,
  `extracted-audits-2026-04-2{1,2-morning,5}`, `audits-2026-04-22-evening`,
  `extracted-codex-feedback-2026-04-2{2-r2,6-bridge-spike,8}`,
  `extracted-claude-feedback-2026-04-22-*` (4),
  `extracted-gemini-feedback-2026-04-26-27`, `link-and-file-hygiene-findings`.
- **Group R — recent, separately tracked.** `audit-451729-FINAL-2026-05-10`
  (TODO §2026-05-10 carries its one residual open item D.1 — *routed, not
  yet fully integrated*); `audit-829314-FINAL-2026-04-28{,-LOGO,-LOGOZOETIC,-TST}`
  (fed the Parts III/IV encounter cycle — tracked by TODO §"Parts III+IV"
  + `msc/logogenic-encounter-2026-05-01/07-audit-integration-tracker.md`,
  which records 24/75 mined).
- **Group O — pre-ledger, old (≤2026-04-06 + March).** No
  `pending-findings` record. `2026-03-13-feedback`,
  `2026-03-14-fresh-eyes-assessment`, `feedback-2026-03`,
  `opus-analysis-2026-03-09`, `analysis-2026-04-0{1,1-remaining,2-comprehensive,2-round2,2-synthesis,6}`,
  `extracted-codex-feedback-2026-04-0{1,2,3,6}`,
  `extracted-claude-feedback-2026-04-02-deep-reviews`. Disposition rests on
  first-hand re-read + corpus-redundancy safety net.
- **Special.** `extracted-claude-session-6da0db68-2026-04-24-audit-instructions-lineage`
  is a lineage/provenance doc, not a findings file — likely a direct
  `.integrated`/retain decision, not adjudication.

## State machine (per top-level file)

`unexamined → adjudicated (per-finding dispositions written) → routed
→ integrated (MANIFEST entry written, git mv) | open (stays, backlink
live)`. An *independent* pass verifies `adjudicated → routed` before
`integrated`. Reversible via `git mv`.

**Per-finding disposition enum** (expanded 2026-05-15 from pilot 583046 —
the original three were under-dimensioned):

- `resolved` — addressed in current `src/`, verified first-hand
  (especially: by *strengthening*, the discharge direction this project
  prefers).
- `correctly-rejected` — finding asked us to weaken a claim the theory
  was instead strengthened to defend; closed *because we strengthened*,
  not open. Concentrates in the math-heavy ledgered cycles (584721 F-A
  cluster, 742613, the 2026-04-25 P-V1/2/3 triad) — *not* in
  hygiene/process/soft-feedback slices. Fan-out agents told where to
  expect these so they neither over-hunt nor under-trust clean
  defect-resolutions.
- `architectural` → `PROPOSALS.md` (first-class entry, full schema — not
  a TODO one-liner).
- `subsumed-by-later-work` — the project moved past it; *distinct from*
  `duplicate` (a verbatim peer-audit repeat). Name the subsumer.
- `duplicate` — verbatim/near-verbatim repeat of another audit's finding;
  defer to that one's disposition; don't double-track.
- `soft-polish` / `sentiment` / `considered-declined` / `research-seed`
  → polish-and-sentiment ledger.
- `process/instruction-feedback` — not about the framework (audit-process
  or instruction-set feedback); themed separately so it doesn't pollute
  framework tracking.
- `actionable-open` → TODO (only genuinely actionable, non-duplicate) or
  a co-owner direct-fix (high-confidence isolated).

**Self-disposed-extract fast-path.** Several `extracted-*` files carry
their own `## Disposition`. There the job is *verify-and-mirror*, not
generate: confirm the dispositions are closure-direction-correct against
current `src/`, mirror any soft/sentiment to the ledger, graduate. A
cheap pre-scan (`grep -l '## Disposition' audits/extracted-*.md`) routes
this whole sub-class fast.

## Delegation design

Parent (me, with Joseph) owns: the partition, primary-source spot-checks
of agent output, all routing **actions** (PROPOSALS/TODO/ledger edits,
`git mv`, MANIFEST entries, commits). Agents own: first-hand per-finding
adjudication and recommended routing — **report only, no moves/edits/
commits/segment-changes** (destructive/structural decisions are the
parent's; constrain by framing since Bash can't be fully withheld from a
reasoning agent, and verify state after).

Cadence: **two-shot pilot first** (one agent on a representative slice,
also reporting what about the frame was unclear → refines this spine →
fresh fan-out agents on the refined frame; the pilot's *output* refines
the *prompt*, it is not fed to the fan-out agents). Then parallel
fan-out by group/slice, independent-verify pass, parent routes + moves +
commits per batch.

### Pilot brief (authored deliberately; this is the artifact, launched as-is)

> You're a co-owner adjudicating part of this theory project's audit
> backlog. The standard to hold: every finding ends up *where it
> belongs* so an audit can be honestly retired without losing signal —
> including the soft "this is good, here's what'd make it better" and
> sentiment findings, which this project treats as first-class (the last
> 5% of polish is most of the usability gap), not as noise to discard.
>
> Orient on `CLAUDE.md`, `audits/.integrated/MANIFEST.md`, and
> `msc/audit-backlog-triage-2026-05-15.md` (the second has the evidence
> hierarchy and the strengthen-before-soften reframe — the live, slightly
> counterintuitive one: this project *often rejects* auditor findings,
> and a finding asking us to weaken a claim we instead strengthened the
> theory to defend is *correctly closed*, not open).
>
> Slice for you: `audits/audit-471203-FINAL-2026-04-28.md` +
> `audits/audit-471203-SUPPLEMENT-phase-2.md` (a central de-novo cycle
> with a `pending-findings` ledger) and
> `audits/extracted-gemini-feedback-2026-04-26-27.md` (Gemini-register,
> soft-finding-heavy). For each finding: is it valid (in the first place,
> and as of *today's* `src/`)? what is it really (defect / correctly-
> rejected-because-strengthened / architectural / soft-polish / sentiment
> / duplicate-of-a-later-audit)? where should it go? Write your
> adjudication to a file in `audits/AUDIT-WORKING-<your six digits>/`.
> Don't move/edit/commit anything — the routing actions are the parent's;
> your deliverable is the adjudication and your judgment.
>
> Your judgment may exceed mine and you'll see context I can't from here;
> "what most benefits the project" overrides "what conforms to this
> brief." This is also a frame-diagnostic run: when you reach the point
> where you know what you'll do — or hit what's genuinely unclear or
> underspecified about the frame — report back. What you surface refines
> the brief before more agents run.

## Log

- **2026-05-15 (a)** — Housekeeping committed (`c1c80a9`): audit working
  dirs consolidated `msc/`→`audits/`; de-novo instructions + ripple
  repointed. Spine + MANIFEST seeded (`e303034`). Recon: git-recency
  poisoned by rename sweep; ledgers decisive.
- **2026-05-15 (b)** — Pilot 583046 (two-shot diagnostic) on the 471203
  cycle + extracted-gemini-2026-04-26-27. Caught a real frame defect
  (audit-id→ledger mapping wrong — corrected above) and under-dimensioned
  enum (expanded above). Both consequential claims primary-source-verified
  by parent (no-ledger fact; F1 stale-xref genuinely resolved in `src/`).
  Adjudication: `audits/AUDIT-WORKING-583046/adjudication.md`.
  - **471203 §B F1–F4 resolved** (F1 spot-checked: `deriv-directional-
    survival-exploration` absent from `src/`; segment now cites
    `#deriv-causal-ib-lmi`). **F7 (Tishby-Zaslavsky→Alemi miscitation)**
    was the SUPPLEMENT's one open item — applied as a *strengthening*
    (option b: kept T-Z for the DL instantiation, added the
    web-verified Alemi et al. 2017 / arXiv:1612.00410 for the IB↔VFE
    variational bridge). F5→post-composition-consistency already routed
    (SP-6 / TODO:149 / F-A cluster). F6 (Pearl-`do` before declaration)
    ≡ 742613:254 → recorded under FORMAT-TODO **C12** (its existing home;
    not homeless as the pilot thought, not a new item).
  - **471203 §F:** F1→**PROPOSALS SP-23** (new, full-schema,
    theorem-import meta-segment); F7≡**SP-12** (already in PROPOSALS
    §D.4 — exact match); F5→class-coercion-via-wrapping subsumed;
    F6→TODO:386 (preface/README-honesty discipline); F2/F3/F4/F8→ledger
    (S4–S7).
  - **extracted-gemini-2026-04-26-27**: self-disposed; dispositions
    verified closure-direction-correct against `src/`; soft/sentiment
    mirrored to ledger (S1–S3).
  - **Graduated** to `audits/.integrated/` (per-finding-justified in
    MANIFEST): `audit-471203-FINAL-2026-04-28.md`,
    `audit-471203-SUPPLEMENT-phase-2.md`,
    `extracted-gemini-feedback-2026-04-26-27.md`.
  - **Not yet fanned out** — frame just corrected; deliberate parallel
    fan-out on the corrected frame is the next action.
- **2026-05-16** — Cycle 1 merged to `main` (Joseph). Branch-vs-main
  decided: `main` (the verification-cadence branch discipline is
  calibrated for whole-corpus refactors; this is independent, additive,
  per-file-reversible work — the real safeguard is the independent-verify
  gate, baked into the state machine, not branch isolation). Fan-out
  launched on the corrected frame — 5 parallel adjudication agents,
  adjudication-only (parent + Joseph route/graduate/commit; the
  independent-verify gate = adjudicator ≠ grad-confirmer holds):
  - **A — self-disposed extracts (verify-and-mirror, 13):**
    `extracted-audits-2026-04-{21,22-morning,25}`,
    `extracted-claude-feedback-2026-04-22-{6d858f28,3546217a,bf945f78}`,
    `extracted-codex-feedback-2026-04-{01,02,03,06,22-r2,26-bridge-spike,28}`.
  - **B — math-heavy ledgered (strengthen-before-soften bite):**
    `audit-584721-FINAL`, `audit-613842-FINAL`, `audit-742613-FINAL` +
    `-SUPPLEMENT-PHASE-2-TRIAGE`, `opus-audit-2026-04-21`,
    `audits-2026-04-22-evening`, `audit-738192-FINAL`
    (ledgers: `pending-findings-2026-04-21/22/23`).
  - **C — 2026-04-24/25 + hygiene + portfolio:**
    `audit-2026-04-24-fresh-pass`,
    `audit-final-reports-candidate-extraction-2026-04-25`,
    `link-and-file-hygiene-findings`,
    `extracted-claude-feedback-2026-04-22-25-portfolio-reviews`
    (ledger: `pending-findings-2026-04-25`).
  - **D — 2026-04-28 FINALs (own-SUPPLEMENT-as-ledger; encounter-linked):**
    `audit-829314-FINAL-2026-04-28{,-LOGO,-LOGOZOETIC,-TST}`,
    `audit-849201-FINAL{,-LOGOGENIC,-SEC-III,-TST}`.
  - **E — pre-ledger old + 451729 + lineage doc:**
    `2026-03-13-feedback`, `2026-03-14-fresh-eyes-assessment`,
    `feedback-2026-03`, `opus-analysis-2026-03-09`,
    `analysis-2026-04-0{1,1-remaining,2-comprehensive,2-round2,2-synthesis,6}`,
    `extracted-claude-feedback-2026-04-02-deep-reviews`,
    `extracted-claude-session-…-audit-instructions-lineage`,
    `audit-451729-FINAL-2026-05-10`.
  - The four `pending-findings-2026-04-2X.md` are durable
    ledgers/infrastructure — read as evidence, never graduated.
- **2026-05-16 (fan-out returned).** All 5 clusters returned deep,
  cross-corroborating first-hand adjudications (token spend 158k–287k
  each; convergence across clusters is itself coherence-evidence — the
  opacity-gain strengthening independently verified in A/D/B; "strengthen-
  before-soften passed loudly" in B/C/D/E; the corpus-redundancy net held
  completely in E). Adjudications:
  `audits/AUDIT-WORKING-{704218(A),628401(B),704182(C),714206(D),472914(E)}/adjudication.md`.
  - **A** — 13 self-disposed extracts, all closure-direction-correct,
    graduation-eligible. Catches: `extracted-codex-feedback-2026-04-28`
    disposition is stale ("Pending" → actually resolved in
    `bin/naming-aggregate.rb`; MANIFEST writes the *corrected*
    disposition, not "Pending"); `bf945f78` ≡ the Opus section of
    another file (note non-independence in MANIFEST); two files are
    primary sources for *live* CLAUDE.md conventions (provenance value);
    proposed ledger rows S8–S15 incl. **S8 POMDP-collapse family**
    (4 declined Gemini big-picture, `considered-declined` with the full
    reason as payload — recurs as an attractive simplification).
  - **B** — 7 math-heavy; ~25/30 resolved, the majority *by
    strengthening*, several beyond what the audit asked. All
    graduation-eligible **except** `742613-FINAL` + `-SUPPLEMENT` which
    carry the **Model-S non-exit defect** forward as the open
    strengthening item → spike launched (see below). Frame surfacings
    folded into the enum/fast-path refinements above.
  - **C** — 4 files graduation-eligible. Two parent actions: **SN-3** —
    upstream `def-pearl-causal-hierarchy.md:53` (+ table row) still
    carries the bald `git checkout` Level-3 overclaim while the
    downstream TST segment `obs-software-epistemic-properties.md` P2
    already strengthened it (the correct language exists verbatim to
    mirror; ~15 min co-owner direct-fix). **F-V3/F8** is correctly
    *open* (Joseph-call Path A vs PROPOSALS SP-21, already triple-tracked
    — graduate with it living there; do not double-track). Byproduct
    (not a Cluster-C finding): fresh `bin/lint-outline` state — 3
    `impl-*` ordering violations + a missing dep
    (`impl-orient-cascade` → nonexistent
    `scope-observation-ambiguity-modulation`: dangling vs. documented
    forward-ref — needs judgment). → standing-hygiene TODO; blocks no
    graduation.
  - **D** — 8 files (829314 ×4, 849201 ×4) graduation-eligible; one tiny
    OUTLINE table-cell fix (`829314-core-F7`, co-owner-direct). Forced
    the spine corrections above (no SUPPLEMENT for 829314/849201; the
    193847-not-829314 tracker fact). Opacity-gain resolved-by-
    strengthening, converging across three independent cycles — the
    cluster's strengthen-first exemplar for the MANIFEST.
  - **E** — 12 graduate-ready; `audit-451729-FINAL-2026-05-10` stays
    *open* on its single residual (D.1, already first-class in TODO
    §2026-05-10 — routed, not homeless). The March + April-01/02 review
    files → `subsumed-by-later-work` (the April-01/02 chain supersedes
    itself in a documented nested-revision lineage); both `extracted-*`
    → `retain-as-history`. **Cross-cluster:** the
    `…-6da0db68-…-audit-instructions-lineage` doc embeds a full audit
    whose findings belong to **Cluster C / `pending-findings-2026-04-25`**
    — de-dup at routing so the same findings aren't double-tracked;
    `analysis-2026-04-02-synthesis` is a curated/raw pair with the
    deep-reviews extract (same content, *not* `diff`-duplicates).

**Enum refinements (from fan-out, fold into the enum above when next
edited):** (1) `duplicate` — *the more precise characterization governs*;
a "harmless summary-compression" framing of a real defect is itself a
methodology-flagged soften and must not win the dedup. (2) A ledger's
recorded *recommended-repair* is an auditor suggestion, **not a binding**
— strengthen-before-soften overrides a ledger-recorded soften regardless
of the ledger's tier-1 evidence status. (3) Widen the self-disposed-
extract fast-path to transcript files that declare their downstream
ledger targets in a purpose header (`audits-2026-04-22-evening` is one).
(4) **Fan-out brief defect (root-caused):** my cluster briefs omitted
"pick a *fresh* six-digit `AUDIT-WORKING-` dir; if it exists pick other
digits" — cluster E collided into the pre-existing tracked `472913`
archaeology (contained: only the new `adjudication.md` was untracked, no
prior file disturbed; relocated to `472914`). Future fan-out briefs must
carry that line.

- **2026-05-16 — Model-S non-exit strengthening spike launched
  (background, Opus, three-completion-states).** Locus
  primary-source-verified by parent (NOT taken from B's summary, which
  was directionally right but imprecise): `deriv-sector-condition.md`
  Prop A.1S (iii) — the Prop statement (~L194) and Epistemic Status
  (~L282) justify the infinite-horizon `P(τ_R<∞)` bound via "the Markov
  tail bound" (the fixed-time-vs-ever-exit conflation), while the proof
  (~L242) gestures at the correct supermartingale/Doob tool. 742613-
  SUPPLEMENT + 613842 recommend the *wrong* (soften) direction. Spike
  brief built from the parent read.
- **2026-05-16 — Model-S spike RETURNED. Completion-state (3): a sharp
  no-go + a corrected-true dichotomy. Strengthening honestly exhausted,
  NOT a soften.** Spike: `spikes/spike-stochastic-non-exit-strengthening-2026-05-16.md`.
  Parent independently verified the core math from theory (not relayed):
  under the SDE, `LV ≤ −2αV + ½nσ²` is *positive* for `V < nσ²/4α`, so
  `V(δ_{t∧τ_R})·𝟙` is a submartingale near the origin — **not** the
  supermartingale lines 242/282 invoke; and the process is OU-ergodic so
  `P(sup_{t<∞}‖δ‖>R)=1`. Findings:
  - The Doob/Ville strengthening **genuinely fails for a precise
    structural reason** (no nonnegative supermartingale; additive-noise
    generator has no bounded non-constant harmonic function). The
    audits' core observation `P(τ_R<∞)=1` is **correct**; no
    horizon-independent non-exit bound `<1` exists (proven + EM-sim, not
    asserted).
  - The constant `nσ_w²/(2αR²)` is **right as the fixed-time/stationary
    tail** (exactly what `spike-disturbance-model-split.md:159`
    established). The defect is the probabilistic *object*
    (ever-exit vs fixed-time), not the constant.
  - The corrected statement is **itself a result**: Model-D →
    pathwise/forever containment (positive invariance); Model-S
    structurally cannot — additive forcing changes the *kind* of
    guarantee (pathwise→distributional), not just the rate. Sharpens
    the hand-off into `#result-structural-adaptation-necessity`;
    candidate `## Findings` entry.
  - **Calibration:** Cluster B's confident substantive prediction (the
    sup-over-all-time object "is bounded ... and *stronger*") was
    **mathematically disconfirmed**. Peer-agent optimism that a
    strengthening *will succeed* is as unreliable as pessimism that it
    will fail; the hard spike was necessary. Recorded in the spike so
    the optimism isn't inherited.
  - **Recommended disposition (spike §6) — NOT landed; gated on
    Joseph.** Restate (iii)→(iii′) fixed-time tail (keep constant); add
    (iv) finite-horizon Khasminskii sup-bound (the honest sample-path
    companion that *does* survive — a genuine strengthening over a bare
    fixed-time tail, flagged horizon-growing); fix proof + Epistemic
    Status (Prop A.1S "exact" claim on (iii) is currently false as
    stated); add the Model-D/Model-S kind-of-guarantee dichotomy to
    Discussion + a `## Findings` entry; propagate the one-object
    correction downstream (closes 613842-F2 integration debt).
    742613-SUPPLEMENT §2 + 613842-F2 are **valid and resolved by this
    spike** (resolution reached *after* strengthening exhausted). This
    is a core-proposition epistemic-status change **plus a new
    no-go/dichotomy result entering the canonical surface** → surfaced
    to Joseph, who greenlit the full package while fresh.
- **2026-05-16 — Model-S package LANDED (Joseph greenlit the whole
  package).** `deriv-sector-condition.md`: (iii)→(iii′) fixed-time tail
  + new (iv) finite-horizon sup-bound; proof "Stopping-time
  localization" + summary table + "What Is Derived" row + Epistemic
  Status corrected (the false "exact" on the infinite-horizon non-exit
  removed; (i)/(ii)/(iii′)/(iv) each exact). **New exact result
  landed as labeled `Corollary A.1S.1` (Disturbance-Model Containment
  Dichotomy):** $P(\tau_R<\infty)$ is exactly $\{0,1\}$ — 0 under
  Model D, 1 under Model S — categorical and $\alpha$-invariant
  (Joseph's probe: "do we not have an exact result that is new?" —
  yes; it had been under-framed as "a no-go," the
  strengthen-the-characterization correction). Discussion's "Kind of
  guarantee" para now points at the Corollary; `## Findings` entry
  re-led on it (novelty: *Synthesis* of classical components into an
  exact $\alpha$-invariant framework dichotomy — honest that the SDE
  math is classical); Working Notes carry the
  landing-provenance + four flagged low-confidence flashes (the
  dichotomy likely generalizes to other bounded/stochastic pairs →
  candidate SP-23 / identifiability-floor instance; sharper
  ELI/LLM-persistence consequence; the no-go signature as a reusable
  diagnostic; a downstream b=3/2 check to confirm-not-assume).
  Downstream 613842-F2 one-object correction landed at
  `result-sector-persistence-template.md:90` (the other two named
  targets carried no wrong-object phrasing). Lint: the 2 raw-math
  issues I introduced fixed; remaining α/β hits are pre-existing
  (FORMAT-sweep C18), not mine. Spike registered in `spikes/INDEX.md`;
  CHANGELOG strengthen-first worked-example entry added.
  **Audit-finding disposition:** 742613-SUPPLEMENT §2 and 613842-F2 are
  **resolved by strengthening-then-no-go** (state 3), not by soften —
  to be recorded in the MANIFEST when 742613/613842 graduate in the
  consolidated pass. Cluster B's prediction that the strengthening
  would *succeed* is recorded (segment Working Notes + spike) as
  disconfirmed.
- **2026-05-16 — honesty-cleanup of the landing (Joseph's three
  principles).** Joseph named three: (1) spike-integration *replaces*
  the truth-state — the false claim disappears or survives only as a
  genuinely-different narrower true statement, never as a softened
  ghost-with-pointer; (2) the epistemic label tracks *current
  truth-status*, not provenance/continuity — labelling a known-exact
  result less-than-exact because it's new/different is a category
  error *and* false ("exact" already means *defeasible-if-someone-
  finds-a-mistake*, so defeasibility is no reason to pre-downgrade);
  (3) a softening of a claim *after* it's shown to be a no-go is
  dishonest unless softened all the way to "false" — in which case it
  has no place in the spine at all. Self-audit against these caught
  real residue in my own just-committed work: the Summary-table cell
  "both halves exact in the linear case" (mis-scoped exactness →
  fixed: states linear-case *recovery*, exactness general); a
  retrospective "previously carried a false bound / not weakened"
  clause in Epistemic Status and the Findings catalog
  lead/Impact/Novelty (provenance-defense-against-the-ghost in
  body+external-catalog → removed; the false-past narrative lives
  *only* in the history layers — Working Notes, this spine, CHANGELOG).
  Honest spine sweep (all live `src/`): **no softened-false residue of
  the old infinite-horizon non-exit claim survives** — the phrase
  exists only in the corrected source segment, stating the no-go as
  present truth. Discipline going forward: segment body + FINDINGS
  catalog = present-truth only; CHANGELOG/spine/Working-Notes = the
  history layer that carries "this replaced a false claim."

## Next actions (gated; the cycle is not the taxonomy)

The independent-verify gate I named to Joseph as load-bearing
(adjudicator ≠ grad-confirmer) means graduations are **not yet done** —
they are gated on a focused parent primary-source spot-check of each
cluster's graduation-gating claims (the gate already caught: B's Model-S
summary imprecision; the spine's wrong 04-28-SUPPLEMENT generalization;
the 193847/829314 tracker confusion; the A-stale-disposition). Next
focused turn, as **one consolidated pass** (the agents explicitly warned
that per-cluster ledger fragments re-bury the soft signal):

1. Per-cluster independent spot-check of the load-bearing graduation
   claims (cheap given cross-corroboration; A self-disposed, E
   redundancy-traced, D opacity-gain triangulated).
2. Co-owner direct-fixes (high-confidence isolated): SN-3 upstream
   Pearl-`do`/`git checkout` language; `829314-core-F7` OUTLINE cell;
   the `hyp-mismatch-dynamics.md:54` F-V1 micro-residual.
3. One consolidated ledger pass: S8–S15+ from A, plus D/E soft items,
   with the recurring "epistemic honesty is extraordinary" sentiment as
   *one attributed row* (not per-file) and the considered-declined
   reasons as payload.
4. Grouped MANIFEST graduation (E's routing-economy: the April-01/02
   consolidation chain as one entry with a shared redundancy table, not
   13 near-identical justifications), with the A-stale-disposition
   *corrected* (not mirrored), the bf945f78 non-independence noted, and
   742613/613842 held until the Model-S spike returns.
5. Lint-state + F-V3/F8-routing-confirmation → standing-hygiene TODO
   (single entries, not duplicates of existing tracking).

## 2026-05-16 (cont.) — SN-3 landed; consolidated pass set up; honest checkpoint

- **Model-S no-go LANDED** (Cor A.1S.1 exact + `#deriv-stochastic-non-exit`
  appendix + integration-is-replacement memory curation, commits through
  `153c41e`). This **unblocks Cluster B**: 742613-F2 / 613842-F2 are now
  resolved by strengthening-then-no-go (state 3) — they graduate in the
  consolidated pass with the MANIFEST recording that disposition.
- **SN-3 RESOLVED** (`3072667` + follow-up `2666eca`): Cluster-C's one
  live defect, primary-source-verified. `def-pearl-causal-hierarchy`
  carried a bald unscoped "git checkout → literal Level 3" in both the
  prose and the comparison-table "Software developer" L3 cell, while
  downstream `#obs-software-epistemic-properties` P2 had the scoped
  truth; both corrected to present-truth, deferring the α/β/γ conjunction
  to its canonical downstream home (not duplicated). Cluster C now
  graduation-ready (F-V3/F8 correctly-open + triple-tracked — don't
  double-track; lint-state → standing-hygiene TODO).
- **Discipline slip, named:** the SN-3 commit briefly introduced 3 lint
  issues into a clean segment because I committed on the lint *count*
  without inspecting the *list*. Caught post-commit by the inspection
  habit, fixed in follow-up `2666eca` (recorded in history, not amended),
  memory sharpened (forcing function = inspect the issues; generalizes
  past inline-math).
- **Honest checkpoint (per the continuation commitment).** Remaining is
  the one *consolidated* graduation pass: A–E + now-unblocked B
  (742613/613842) + the soft-finding ledger (S8–S15+, consolidated to
  avoid re-burying) + grouped MANIFEST + `git mv`. It is the largest,
  most fragmentation- and integration-is-replacement-sensitive unit of
  the program, fully set up and resumable from this spine. Per the
  commitment "checkpoint rather than push past good work," this is the
  natural fresh-focus boundary — the consolidated pass wants a focused
  instance (this one continued, or a fresh one with this spine + the new
  memory), not the tail of a very long session with a rising rate of
  small (all-caught) slips. Surfaced to Joseph as a checkpoint.
