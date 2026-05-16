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
> No `pending-findings-*.md` references audit-id 471203 (nor, by the same
> structure, the other 2026-04-28 FINALs 829314 / 849201). The four
> ledgers cover the **2026-04-22 and 2026-04-23 de-novo intakes and the
> 2026-04-24 fresh-pass triad only**. The 2026-04-28 de-novo FINALs carry
> their **own SUPPLEMENT / §K–§L as their ledger**. Confirm each file's
> actual ledger first-hand; never infer it from the audit-id.

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
