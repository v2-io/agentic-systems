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
PROPOSALS; tiny high-confidence ones may just be fixed. **Provisional** —
the pilot agent's encounter with real soft-finding volume/shape will
stress-test this before the ledger is created for real.

## Evidence hierarchy

See the MANIFEST §"Evidence hierarchy". Summary: `pending-findings-*.md`
ledgers ≻ CHANGELOG narratives ≻ open-`[ ]` TODO/PROPOSALS backlinks
(sufficient for NOT-integrated; absence not sufficient for integrated) ≻
first-hand re-read vs current `src/`. **`git`-recency is poisoned** by the
2026-05-15 rename sweep — do not use it.

## Partition (hypotheses — to be VERIFIED, not assumed)

51 top-level files in `audits/`. Grouped by *what evidence is expected to
govern them*, not by presumed status. Status starts `unexamined` for all.

- **Group L — ledgered cycles (2026-04-21 → 25 intakes).** Disposition
  should be readable from `pending-findings-2026-04-2{1,2,3,5}.md` +
  CHANGELOG, then spot-checked. Files: the four `pending-findings-*` (the
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
(soft→ledger, arch→PROPOSALS, actionable→TODO/direct-fix, rejected/closed
recorded) → integrated (MANIFEST entry written, git mv) | open (stays,
backlink live)`. An *independent* pass verifies `adjudicated → routed`
before `integrated`. Reversible via `git mv`.

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

- **2026-05-15** — Housekeeping committed (`c1c80a9`, branch
  `audit-backlog-cleanup`): audit working dirs consolidated `msc/`→
  `audits/`; de-novo instructions + ripple repointed. Recon done:
  git-recency poisoned by rename sweep; ledgers are decisive. Spine +
  MANIFEST seeded. Pilot launching next.
