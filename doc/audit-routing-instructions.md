# Audit-Routing Instructions

*The governing process for taking audit findings and routing each to where it belongs — including, at its heart, what happens when strengthening a claim yields a **no-go**.*

> This document is mostly **current ops** (defined below): we have to choose
> *something*, and this is the current choice, refined live. It governs how
> findings are dispositioned — but it is **not above truth**. If you are at
> the front line and a rule here confuses you because it contradicts the
> reality in front of you, that confusion is not noise to suppress. It is the
> primary signal that this document needs re-truthification. Read
> [§7 The meta-stance](#7-the-meta-stance-this-filter-is-itself-unpurified)
> before you conclude you have an exception — and before you conclude you
> *don't*.

---

## 0. Why this exists, and the one phrase that names the failure

Audit findings are not a to-do list. **The job is not to do what the audit said — the job is to take each finding, decide what is and is not valid
(valid *in the first place*, and valid *as of today's* `src/`), and route it to the right home** so the audit can be honestly retired without losing signal.

The recurring, seductive failure has one shape. An auditor (often well-meaning) finds something wrong in a claim marked `exact` and says, in effect: *"this isn't a weakening — it's just fixing an epistemic typo;
downgrade `exact` → `hypothesis`."* That framing is **the trap**, not the fix. Changing one word makes the task disappear and the paper strictly honest — irresistibly easy, to everyone involved. But the assertion was made for a reason; the mental picture that produced it was usually pointing at something real. Our methodology is: **attempt to make the claim true before you agree it is false.** Most of the time the strengthening *succeeds*; a meaningful fraction of the time it fails into a **no-go** that exposes the domain more sharply than success would have. Either outcome is worth more than the word-swap.

> *"A ship in harbour is safe, but that is not what ships are built for."*
> The `establish`-instead-of-`prove` move is honest about the local
> mismatch and dishonest about the aspiration. Discharge the inconsistency
> in the right direction; carry the cargo. — Joseph, paraphrased from the
> 2026-05-14 strengthen-first exchange (`~/.claude/memory/epistemic-discipline/strengthen-before-soften.md`).

This document is the protocol for carrying it.

---

## 1. The classification every rule here carries

*(This scheme is **current ops**. Joseph supplied four buckets and flagged them explicitly non-MECE — "initial thoughts for you to refine." What follows is the refinement; cut it back if it has over-built.)*

A rule is not a flat category. It lives on two axes, and it **moves** along them as experience accrues — every authoritative rule was once somebody's provisional one, and every authoritative rule can be unseated when the substrate shifts under it.

**Axis A — groundedness (why the rule exists):**

- *provisional* — we must choose something to coordinate at all; this is the current choice, defensible but not load-bearing on first principles.
- *coordination* — low-stakes, somewhat arbitrary, but a shared convention prevents real confusion or harm (filenames, term choices, directory prefixes). The content is arbitrary; the *consistency* is not.
- *hard-won* — refined by a painful experience. The rationale lives in the scar; the scar is documented (footnote, `msc/reflections/`, a memory, a CHANGELOG entry) so the rule is never re-litigated from zero.
- *mission-grounded* — derived from the project's purpose, attested by Joseph with rationale and accumulated wisdom. The canon's honesty is the product; rules protecting it sit here.

**Axis B — the posture you owe the rule:**

- *revisit-freely* — question and change it the moment it stops serving.
- *obey-first-then-ask* — follow it, gain the experience of following it,
  and bring *that experience* back as the evidence for an exception. Do not pre-empt the experience with a plausible-sounding exception. ("Get experience following the rule before you think you have an exception, then ask" — Joseph.)

The four operational tags used throughout this doc, defined on those axes:

| Tag | Groundedness | Posture | Meaning when you see it |
|---|---|---|---|
| **current ops** | provisional | revisit-freely *with a heads-up* | "We had to pick; this is the pick. Improve it, but tell the others." |
| **convention SOP** | coordination | revisit-freely *but coordinate the change* | "Arbitrary-ish; the value is that we all do the same thing. Change it deliberately, not unilaterally." |
| **evolved ops** | hard-won | obey-first-then-ask; the scar is linked | "This shape exists because a specific thing went wrong. Read the scar before you 'simplify' it." |
| **authoritative SOP** | mission-grounded | obey-first-then-ask | "Joseph-attested, purpose-derived. Follow it; question it *with* front-line evidence, not against it in the abstract." |

**The dynamic that makes the scheme honest:** front-line confusion is not a challenge to authority — it is the **re-truthification channel** for it.
"Obey-first-then-ask" is the mechanism: you follow the rule, the following produces the observation, and the observation — not a prior guess — is what you escalate. Authority and defeasibility live together. Full treatment,
including the role-asymmetry this implies (who may treat the rule as authoritative and who may not), in
[§7](#7-the-meta-stance-this-filter-is-itself-unpurified).

---

## 2. The strengthen-first reflex (authoritative SOP)

> Groundedness: mission-grounded. Posture: obey-first-then-ask. Source:
> `CLAUDE.md` §"Strengthen before softening", global
> `~/.claude/memory/epistemic-discipline/strengthen-before-soften.md`,
> Joseph 2026-04-22 / 2026-05-14, repeatedly.

When a finding proposes a softening — scope-narrowing, status-downgrade,
"this is heuristic", "just an epistemic typo" — **the strengthening attempt is made first, regardless of how the auditor justified the easy path.** The auditor's framing of their own finding ("this isn't a weakening") carries no weight on the discharge direction; strengthen-before-soften governs that regardless of the ledger's evidence tier.

Effort, time, and risk-of-getting-stuck are **false constraints** here —
not merely irrelevant but truth-obscuring: they produce orderings exactly inverted from value. Do not rank repairs by effort. Do not propose smallest-first. Do not defer the substantive move to "discuss first" when the substantive move *is* the strengthening attempt.

---

## 3. The spike (current ops on the mechanics; authoritative on the obligation)

Launch a spike with a **broad** directive: push the math and the thinking as far as they go, until the claim yields or until you uncover, *with specificity*, why it cannot. Not "try the obvious fix" — "find the truth here, whatever it is."

A spike returns one of four completion-states. The frequency ordering is Joseph's observed prior (using `exact` as the illustrative status; the pattern generalizes across statuses) — **current ops, will refine with data**:

- **(A) Strengthened to the claim** *(most often)*. A path is found that makes the asserted epistemology true; the math is upgraded to fit it.
- **(B) Strengthened past the claim** *(second)*. The spike exceeds the claim *and* its own initial skepticism — a uniqueness theorem where a bound was asked, a no-go boundary that is itself a stronger result.
- **(C) A no-go** *(third)*. A theorem that **falsifies** the claim and, in falsifying it, exposes the domain more clearly. This document's centre of gravity — see [§4](#4-the-no-go-protocol-c-evolved-ops).
- **(D) "Strengthen failed"** *(fourth, rare)*. The agent reports failure
  *without* a no-go and *without* exhaustive effort. This is not a result.
  Re-spike de novo; find out why the structure didn't yield insight;
  escalate to Joseph; run simulations; revisit prerequisites. Only
  *maybe*, and only with **Joseph's explicit consent**, a temporary downgrade. (D) is never a quiet landing; it is an alarm.

> Calibration, recorded so it is not inherited as bias: peer-agent
> confidence that a strengthening *will* succeed is as unreliable as
> pessimism that it will fail. A cluster adjudication confidently predicted
> the Model-S maximal-inequality strengthening "is standard textbook, should
> not fail." The hard spike disconfirmed it (→ a no-go). The prediction is
> recorded as disconfirmed in the spike and the segment Working Notes so it
> is not re-attempted on the strength of the optimism. *Run the hard spike;
> do not relay the optimism.*

---

## 4. The no-go protocol (C) (evolved ops)

> Groundedness: hard-won. Posture: obey-first-then-ask. Scar: the
> over-rotation corrected in [§6](#6-the-ghost-the-correction-to-the-inherited-filter);
> articulated by Joseph 2026-05-16, this session.

A no-go collapses **two** things at once, and missing the second is the error this section exists to prevent:

1. The segment's claim (e.g. `exact`-shows-`abc`) is now **false**.
2. **The auditor's suggested fix is *also* false.** Their proposed downgrade (`exact` → `hypothesis`) presumed a weaker-but-true residue.
   The no-go says there is none *in that form*. The probability wave has collapsed to zero. **There is no downgrade option.**

The steps, in order. Steps 4.1–4.4 are committed **before** the audit finding is routed (4.5); routing a no-go-bearing finding while the segment still lies about itself is the cardinal sin.

**4.1 — The invariant, stated once and absolute.** *A segment must never lie about its own status, even transiently.* Tracking files carry the delta, the why, the inner process. **Segments carry only present truth with correct bounds and accurate epistemology, at all times.** Whether a claim is true, whether the model is useful, within the degrees we have defined —
the canon is *always honest about itself*. This is **authoritative SOP**;
everything below serves it.

**4.2 — Mark the segment immediately if the fix is not obvious; gate the fast-path if it is.** If the correct new form is genuinely obvious and a few targeted edits away, you may skip the `FALSE`-marking *interval* and the brainstorm-plan and move toward the replacement — **but not unsupervised.**
"Obvious" is itself the failure-conviction word here: a softened ghost is a
*wording* failure, and [§8](#8-operational-reference-the-routing-mechanics)
is explicit that the wording class is exactly where "I see it clearly" is the thing that fails. So the obvious-fast-path still routes the drafted replacement *wording*, verbatim, to an external eye (Joseph, or a fresh independent confirmer per the §8 gate) before the durable write. It buys you out of the interval and the plan; it never buys you out of the external eye on the wording. Otherwise — *before figuring out next steps takes any time at all* — set the segment's epistemic status to **`FALSE`** (or the cascade-appropriate `unlikely in current form`), **in the segment**, with a link to the spike / discussion, and a visible `TODO: FIXME`. Not a quiet note in tracking. In the segment. A reader encountering it mid-repair must see that it is known-broken, not be misled for the duration of our uncertainty.

**The falsified claim does not lie alone (cascade closure).** Directed separation means a no-go upstream propagates: *every dependent of the falsified claim must be found and either cascade-marked (`unlikely in current form`) or re-derived.* This is an obligation with a verification step, not the old parenthetical "the cascade matters" — an un-marked dependent of a falsified claim is the same "segment lies about itself"
failure, one hop away. The closure is *verified done* before routing (4.5),
not left implicit.

**4.3 — Write the integration plan.** `spikes/<slug>-spike-integration-plan.md`
*(filename: convention SOP)*. The spike file/dir stays where it is and stays editable. The plan explores what the no-go means for truth in the big picture: which segments are **certainly** affected, which **might** be,
what the new shape of the theory probably is. Unknowns are fine — brainstorm.
A weak first plan is acceptable; an absent one is not.

**4.4 — Surface it in PRACTICA.** The integration plan is referenced from one of PRACTICA's active to-do lists. A no-go that is not on the strategy DAG is a no-go that will be silently dropped.

**4.5 — Only now route the audit finding.** With 4.2–4.4 committed **and the cascade closure verified** — every dependent of the falsified claim found and marked-or-re-derived, not left implicit — the finding's disposition is `resolved-by-strengthening-then-no-go` (state 3), recorded in the routing tracker / MANIFEST *as present-tense fact*, per
[§5](#5-how-the-prior-truth-is-mentioned-the-ghost-forms).

**4.6 — You now have the best context to implement the replacement.** Often the spike agent (or you) is best-placed to do — or delegate — the edit that
*replaces old truth with new present-tense truth*. Tracking/CHANGELOG describe the change, the delta, the process. The segment becomes the new present truth.

---

## 5. How the prior truth is mentioned: the ghost-forms (evolved ops)

When the spike is integrated, the prior claim's "ghost" takes one of these forms. **Frequency-ordered (current ops); the ordering is the correction in
[§6](#6-the-ghost-the-correction-to-the-inherited-filter).**

- **(A) Its own no-go theorem, in an appendix** *(most often)*. Especially if the result is surprising, counter-intuitive, or — critically — *an approach a competent reader would assume we simply missed if we did not address it*. This is canon. It establishes the path we *do* take and illuminates the field. (Worked example: the Model-S containment dichotomy → `#deriv-stochastic-non-exit` + Corollary A.1S.1.)
- **(B) A quick no-go proof in the most relevant section** *(sometimes)*.
  When small and local enough that a full appendix would be ceremony. (No need for "we establish that building a logozoetic intelligence on a deterministic finite automaton is a no-go" — proportionality applies.)
- **(C) Disappears to a CHANGELOG entry and *maybe* a Working-Notes line**
  *(very rarely)*. **Only** when the failed approach was nonstandard, would predictably fail, and is something *no one would attempt under our current understanding* — a wrong direction with no instructive residue.
- **(D) Something else.** We cannot enumerate what we have not seen. If a ghost does not fit A–C, that is information; describe it and ask.

**The hard rule on phrasing the prior.** *How* you mention a superseded ground truth **is part of the truth-seeking posture, not a lapse from it.**
There will almost always be *some* canonical record of the disposition of something that was once sincerely a core part of the theory — even if only to show why the naive approach fails. What is forbidden is narrow and absolute:

- Pretending the wrong segment can simply be **softened**.
- Leaving **any** canon asserting the old epistemology (`exact`, or anything softer-but-still-positive) instead of strictly false / no-go.
- Writing the no-go in **project-autobiographical / defensive voice** in the canon ("the framework previously held…", "this is not a weakening,
  we already…"). The *domain* statement ("no such bound exists; the natural route provably fails") belongs in canon; the *process history* ("we used to claim X; an audit flagged it; we strengthened") belongs in CHANGELOG / routing tracker / Working Notes. When the domain statement is already canonical, the autobiographical restatement is redundant and goes to the history layer. When it is *not* yet canonical, write the domain statement *as canon* — do not let the history layer be the only place the truth lives.

---

## 6. The ghost: the correction to the inherited filter (evolved ops — read the scar)

The filter that was meant to enforce all of the above was **itself over-rotated**, and a lead agent who applies it as written will get this wrong. This is the documented scar.

The inherited `integration-is-replacement` discipline said, in effect:
*"the ghost disappears; segment body + FINDINGS = present-truth only; the history lives **only** in CHANGELOG/Working-Notes; the urge to write 'not a weakening' is the tell the ghost isn't deleted."* Applied as a rule, this produces the instruction "find the ghost in the body and **delete** it,
high confidence."

**That over-generalizes the rare case (5C) into the default.** A no-go is
**present-tense canonical truth** — "we establish X is impossible because Y" is a true statement that *belongs in the canon* (5A/5B), especially when the failed approach is one a reasonable person would try. Exiling it to archaeology is itself a **loss of truth-content**. The "not a weakening"
body-signal is real, but it fires specifically against **soften-disguised-as-typo**
and **defensive process-voice in canon** — *not* against all mention of a superseded ground truth.

> **Worked example — `deriv-sector-condition.md:294` (a genuine ghost,
> handled per the *corrected* rule).** The Model-S no-go *is* canon and is
> done right (Cor A.1S.1 + the `#deriv-stochastic-non-exit` appendix —
> textbook 5A). The defect at `:294` is narrow: the cell reads
> "**Proved** — new exact result; *the framework previously held a false
> interpolating non-exit bound here*." The no-go content is already stated
> canonically — *and already clean of ghost-defense* — at the two loci the
> prior honesty-cleanup did purge: the Epistemic Status sentence ("Corollary
> A.1S.1 is itself an exact result") and the Cor A.1S.1 `## Findings` entry.
> `:294`'s Summary-table cell is the lone straggler; its trailing clause is
> the *autobiographical phrasing of a truth already stated cleanly at those
> two loci* — that redundancy is what earns the "demote it" verdict (the
> load-bearing word is *redundant*; naming the loci makes it checkable, not
> asserted). The fix is **not** "delete the ghost" — it is "the redundant
> project-history voice moves to the history layer; the canonical no-go
> stays." The over-rotated filter said "delete, high confidence"; that
> confidence was the filter talking, not the theory.

> **Worked example — `result-sector-persistence-template.md:88` (NOT a ghost
> at all — the category error to avoid).** Same surface phrase ("this is
> not a weakening"), entirely different disease. There was **no status
> transition**: the template is `exact`, was `exact`, stays `exact`. The
> "(T2) $\alpha/\beta$ sub-scoping" is a *true present-truth scope statement*. Its
> provenance is most likely a Codex "you say it but it's easy to miss"
> request answered in defensive register — *not* a disproved-proof scar.
> The repair is **register, not status**: kill the defensive voice, keep
> the truth-serving reader-orientation, make it *unmissable* rather than
> *defended*:
>
> > **Important, and easy to miss: this is not what carries forward
> > universally.** For sub-scope $\beta$ instantiations (e.g. a team with a
> > rule-based sub-agent) (T2) is an *empirical precondition, verified
> > per-instantiation*, not derived. That distinction scopes
> > which instantiations satisfy (T2) by which route; it does not touch
> > the template's exactness, which is the conditional "(T1)–(T3) ⟹
> > persistence" — anything satisfying (T2) by either route inherits the
> > exact result.
>
> The teaching: **same surface phrase ≠ same disease.** Check provenance
> (disproved-proof scar vs. auditor-clarity response). In *both* the repair
> de-defensivizes; but a status case touches epistemology and a clarity
> case touches only register, and conflating them — as "same discipline,
> lower urgency" did — is itself the failure.

The synthesis, which is sharper than either the over-rotated rule or its naive negation: **the no-go is not a ghost to exile — it is truth to canonize. What gets demoted to the history layer is only the project-autobiography, and only when it is redundant with the canonical statement of the truth.** Strengthen-not-delete is the through-line.

---

## 7. The meta-stance: this filter is itself unpurified (authoritative SOP)

> Joseph, 2026-05-16: the spine / routing tracker, several memories, and
> CLAUDE.md directives meant to be a purifying filter on the project are
> "simultaneously in just as much need of refinement and truthification
> from the ground-current-reality that they're checking."

A new agent reading the instructions has **no way of knowing with certainty which parts are hard-won lessons and which were first-draft plausible conscription** that may not serve the project. This produces an obligation that is *asymmetric by role*:

- **A subagent** you launch may treat this document as authoritative and need not carry the meta-question. That is correct and a feature — it lets them work within the frame without paralysis.
- **The lead / parent agent cannot.** You must hold "are we *sure* this process is right here? I don't know if it came from Joseph, or, if it did, what his actual intent was" — and you must be able to *stop and ask him to illuminate it*, rather than resolve the ambiguity silently in the convenient direction.

Both failure directions are real and named:

- **Disregarding hard-won lessons** because "the filter is unpurified" —
  e.g. pretending a weakening isn't one because the strengthening spike seems improbable or overwhelming. This installs a de-facto exception regime and lets large errors propagate. Forbidden.
- **Treating the filter as sacred** when it is propagating an embedded error — applying it as a rule against the theory's own ground truth (the
  `:294` "delete, high confidence" instinct). Equally forbidden.

The resolution is the classification in [§1](#1-the-classification-every-rule-here-carries)
plus its dynamic: obey-first on authoritative SOP, *gain the experience of following it*, and bring the front-line observation back as the evidence for refinement. Front-line confusion is the channel, not the noise.
`CLAUDE.md`'s own closing note already says it: *"This file is not sacred …
if the disposition-language reads as ornamental, that is information about the writing, not about you. Edit it."* This document inherits that stance about itself.

---

## 8. Operational reference (the routing mechanics)

The mechanics below are the working procedure for an audit-routing cycle.
Tags mark groundedness; treat untagged items as **current ops**.

**Naming** *(convention SOP)*. The **routing tracker** is the evergreen [`audits/STATUS.md`](../audits/STATUS.md) — the live index of where each audit stands (routed vs. graduated, what remains open). It is *not* "the spine" — "spine" is reserved for the theory's critical path (the longest core-claim dependency chain). (History: the routing-tracker role was first carried by the one-cycle working file `msc/audit-backlog-triage-2026-05-15.md`; that file completed its 2026-05-15/16 cleanup pass and was retired to [`audits/.integrated/audit-backlog-triage-2026-05-15.md`](../audits/.integrated/audit-backlog-triage-2026-05-15.md) as reasoning-trail archaeology on 2026-05-28, with the live role moved to `STATUS.md`. The deferred path-rename it flagged is thereby discharged.)

**Route, don't execute** *(authoritative SOP)*. A finding's disposition is
*where it belongs*, not *whether we did what it asked*. Strengthen-before-
soften is live and inverted-from-naive: a finding asking us to weaken a claim the theory was instead strengthened to defend is **correctly-rejected
/ closed**, not open.

**Soft / sentiment / considered-declined / research-seed are first-class**
*(authoritative SOP — Joseph: "the last 5% of polish provides 50–90% of the usability-gap coverage")*. They get a durable home (the
`audits/polish-and-sentiment-ledger.md`), not the trash and not a TODO dump. An audit is retired as *fully accounted for* only once its soft findings are mirrored or routed. `TODO.md` is **not** the sink:
high-confidence isolated fixes may be applied directly; architectural moves go to `PROPOSALS.md`; only genuinely actionable, non-duplicate, tracked work goes to TODO.

**Per-finding disposition enum** *(evolved ops — expanded across the
2026-05-15/16 cycle)*: `resolved` · `resolved-by-strengthening` ·
`resolved-by-strengthening-then-no-go` (state 3, §4) · `correctly-rejected`
(soften declined *because the theory was strengthened*) ·
`architectural`→PROPOSALS · `subsumed-by-later-work` (name the subsumer;
distinct from `duplicate`) · `duplicate` · soft bands
(`soft-polish`/`sentiment`/`considered-declined`/`research-seed`) ·
`process/instruction-feedback` · `actionable-open`→TODO or co-owner direct-fix.

Three enum refinements the fan-out surfaced, folded here *(evolved ops)*:
1. `duplicate` — **the more precise characterization governs the dedup.** A
   "harmless summary-compression" framing of a real defect is itself a methodology-flagged soften and must not win.
2. A ledger's recorded *recommended-repair* is an auditor suggestion,
   **not a binding.** Strengthen-before-soften overrides a ledger-recorded soften regardless of the ledger's tier-1 evidence status.
3. The self-disposed-extract fast-path extends to transcript files that declare their downstream ledger targets in a purpose header.

**The whole evidence hierarchy is proxy; truth is the arbiter**
*(authoritative SOP — Joseph 2026-05-18; full statement
`doc/spike-routing.md` §0).* Every entry in the hierarchy below — and the ledgers, CHANGELOG, INDEX, `NOTATION.md`, the segment's own assertion, the auditor's framing, and even multi-agent convergence — is a **mild proxy** that *drifts*. It locates and cheap-screens a question;
it never settles it. Settle by the mathematics re-derived independently
(constitutive structure + forced identities + elementary steps), not by what any artifact says. Two named traps: `NOTATION.md` is a *lagging*
index — the live theory drifts from it; never cite it as authority. And a `[Verified]` whose object is "what file F says" rather than "the derivation holds" is proxy in verification's clothes. The hierarchy is for *screening order*, not for *deciding truth*.

**Evidence hierarchy** *(evolved ops — screening order only, never the arbiter; see above)*, decreasing reliability:
`pending-findings-*.md` resolution ledgers ≻ CHANGELOG cycle narratives ≻
open-`[ ]` backlinks in TODO/PROPOSALS/PRACTICA (sufficient for NOT-integrated; *absence is not* sufficient for integrated) ≻ first-hand re-read vs current `src/`. **`git`-*recency* is poisoned** by rename sweeps (AAD→AAT 2026-05-15, role-prefix 2026-04-24) — recency ordering cannot stand in for the content check. But **git *provenance* is a valid,
encouraged, non-destructive investigative technique** (Joseph 2026-05-17,
directed into both SOPs): pickaxe `git log -S'<string>' -- '*/src/'` for when/whether content entered a segment, `git blame`, `git log --follow`
across the renames, and dates read in context. Don't infer status from the log's *recency*; do use the log's *provenance*.

**The regression check is central, not optional** (Joseph 2026-05-17,
directed into both SOPs; full treatment `doc/spike-routing.md` §2a).
Before re-introducing *any* result, and before confirming any "already integrated" claim, the provenance investigation must distinguish
*never-landed-and-valid* / *current-corrected-truth* from
*landed-then-deliberately-corrected-away* / *regression-restoration over a later fix*. The scenario: a result was integrated, an audit found a flaw, the theory was fixed — and the now-clean-looking prior result gets restored *because it looks better*. The corrected theory is usually
**messier** than the claim it replaced, so "it looks better" is the body-signal (the reverse-direction sibling of strengthen-before-soften;
the enforcement teeth of integration-is-replacement). Instruments:
pickaxe `-S` for an *add-then-delete* of the result-string (find the deleting commit, read *why*), `blame`/`log` on the locus against the CHANGELOG/LOG correction timeline, and the `pending-findings-*` /
audit trail. If corrected-away: `correctly-superseded`, never reopened.
A prior integration that was itself a regression-restoration is a §4.1 canon-lie to mark.

**Independent-verify gate** *(authoritative SOP)*: **adjudicator ≠
grad-confirmer.** Before any `git mv` into `.integrated/`, the load-bearing graduation-gating claims are primary-source spot-checked by an agent *other than* the one who adjudicated them — open the actual `src/`-or-ledger source, not the agent summary. The gate lives in the state machine, not in branch isolation. It has repeatedly caught real errors (a self-certified
"fully clean" honesty-sweep that wasn't; a stale disposition; a tracker-id confusion) — it is load-bearing precisely because the conviction that you don't need it is the failure it catches.

**The seam / checkpoint discipline** *(evolved ops)*: verification spot-checks and ledger *design* are **pre-decisional** — reversible by not committing, they lock nothing in. MANIFEST writes, the consolidated-ledger write, and `git mv` are the **durable batch**. The checkpoint sits at the
*seam* between them, not at an arbitrary "first cluster." For the
**wording-failure class** (e.g. a softened-ghost MANIFEST entry), the defense is not vigilance — "I see it clearly" is exactly what fails here —
it is **routing the specific drafted artifact, verbatim, to an external eye** (Joseph, or a fresh independent confirmer per the gate) before the durable write.

**Pre-spike commit hygiene for canon-modifying agents** *(evolved ops —
Joseph 2026-05-20)*: before launching any agent or spike that will directly modify canon segments (`*/src/*.md`, OUTLINE rows, FORMAT,
`bin/`, governing docs), **commit all prior canon-touching work first**.
This isolates the spike's contribution as a discrete diff — easy to inspect, easy to revert, easy to attribute. A spike whose edits mingle with this-session uncommitted canon work creates an attribution mess:
reviewing what the spike actually did requires manual reconstruction
(which lines were mine, which theirs?), and a revert of "what the spike did" becomes per-line judgment instead of a clean `git revert <hash>`.
The rule applies even when the prior work is obviously-fine-to-commit on its own — commit it first; launch the spike second. The commit *is*
the seam — it locks attribution.

**Consolidated-ledger anti-fragmentation** *(evolved ops)*: soft findings are mirrored in **one curated pass across all clusters**, themed and deduplicated — *not* per-cluster as each graduates (that re-buries the signal, the exact failure the ledger exists to prevent). Recurring sentiments ("Section I is the strongest", "the epistemic honesty is extraordinary") become **one attributed row each**, not one per file. A stale-but-safe-direction disposition is written **corrected**, not mirrored.

**Directory-prefix invariant** *(convention SOP, but errors here are silent and corrupting)*: the six-digit ID is identity; the prefix is the class. `ADJUDICATION-WORKING-<id>/` = this program's adjudication workspaces (six moved: 583046, 704218, 628401, 704182, 714206, 472914).
`AUDIT-WORKING-<id>/` = de-novo auditors' first-encounter cognition. **Never blanket-rewrite one to the other**; recover class from the routing-tracker partition / git history, never by string substitution. The frozen
`adjudication.md` deliverables' stale internal paths are not edited.

**Working-directory lifecycle** *(authoritative SOP — Joseph-attested
2026-05-16, with rationale)*: a working directory, **once it has served its purpose (fully integrated — nothing of value lives only there), is cleared out of the live tree**, into `.integrated/` (or `.archive` / `_obs`). It is
*not* "retained in place." Leaving served-purpose working dirs in `audits/`
or `src/` or anywhere live is not cost-neutral: it taxes discoverability on every `ls` / `rg`, is a decision point and cognitive load on every encounter, and — worst — breeds the "it's not done, but I'll leave it here because that's what we do, someone will get to it later" rot. The disposition of a served-purpose working dir is therefore *clear it*, not catalogue an
(a)/(b) location framework. **Boundary:** this covers dirs whose purpose is
*spent*; it does **not** override the gold standing gate below — a directory whose disposition is *itself* an open decision (the de-novo
`AUDIT-WORKING-*`) has not "served its purpose" in this sense and is governed by that gate, not by this line.

**The de-novo `AUDIT-WORKING-*` "gold" standing gate** *(authoritative SOP)*: those dirs are first-encounter cognition / "Wandering Thoughts" —
value largely orthogonal to theory-fix triage. **Before any processing,
mining, summarization, `.integrated/` move, or deletion, consult Joseph and decide _with him_.** Separate from the consolidated graduation pass; does not cover `ADJUDICATION-WORKING-*`.

---

## 9. Phenomenology is load-bearing (a note on this document's voice)

This document keeps its lived texture — the failure-prediction register,
the body-signals, the worked examples told as what actually happened, the Joseph quotes in his voice — **by design, not as ornament.** The spine's own hardest-won lesson is that *principles restated do not prevent the failures they name; pre-registered specifics plus an early external catch do.* A checklist SOP would be a *less true* document, because it would predict its own compliance and be wrong. The voice is the binding mechanism.

If a future agent finds this language ornamental or the rules dismissable — that is information about the writing, to be edited, in this document's own spirit (§7). But edit it *toward* more lived specificity,
not toward flatter abstraction. Do not sand off the experiences that give it life; they are why it works.

---

*Living document. Started 2026-05-16, this session, from Joseph's articulation of the no-go protocol and the meta-stance. Iterate it as the process is exercised; record each refinement's scar so the next reader inherits the reason, not just the rule.*

*Refinement 1 (2026-05-16, same session — scar recorded per the rule above):
an independent fidelity review, solicited specifically because a freshly written correction-to-an-over-rotation is itself the highest-risk over-rotation candidate, caught (a) §4.2's "obvious → straight to replacement" fast-path escaping the §8 wording-failure external-eye gate —
the one genuine loosening, since a softened ghost is a wording failure and
"obvious" is the failure-conviction word; (b) a missing cascade-closure gate
(a falsified upstream claim with un-marked dependents lies one hop away);
plus two tightenings (§1 prose triplication; §6 ex-1 naming the loci that earn "redundant"). Folded before any downstream batch was built on the doc.
The transferable scar: check the new filter externally before building on it — the conviction that the correction is clean is the same conviction the doc says fails.*

*Refinement 2 (2026-05-17, Joseph-directed via the spike-routing cycle —
the shared core's first refinement from its second corpus). §8's
"`git`-recency is poisoned … use ledgers, not the log" was too blunt: it correctly killed *recency-as-status-proxy* but, read literally, suppressed
*provenance investigation* (pickaxe `-S`, `blame`, `log --follow`, dates in context) — a valid, non-destructive, often-sharpest decisive-test instrument. Split the two explicitly. Surfaced from spike-routing
(`doc/spike-routing.md` §7 / Refinement 2) and folded into the shared core because the evidence-hierarchy is corpus-agnostic. This is the §7 meta-stance working as intended: a second corpus exercising the shared core re-truthified it; the refinement landed here, not in a fork.*

*Refinement 3 (2026-05-17, Joseph-directed — pre-emptive). The regression check (don't re-land a corrected-away result; don't confirm an integration that is a regression-restoration over a fix) is elevated to a **central** investigation element, not a side gate, on every disposition including already-integrated ones. Body-signal: "it looks better than canon" — because the corrected truth is usually messier.
Full worked treatment + the disposition `correctly-superseded` in
`doc/spike-routing.md` §2a / its Refinement 5. Same §7-meta-stance landing: surfaced in the spike corpus, folded into the shared core.*

*Refinement 4 (2026-05-18, Joseph-directed — the foundational stance,
made explicit and supreme over all the proxy-mechanics in this doc).
Care about the theory's **truth** above everything; provenance,
ledgers, CHANGELOG, INDEX, `NOTATION.md`, segment/spike assertions,
audit findings, and multi-agent convergence are *mild proxies that drift* — screening, never settling. Settle by re-derived mathematics.
Two named traps folded into the evidence-hierarchy preamble above:
`NOTATION.md` lags the live theory (never authority); a `[Verified]`
tag whose object is "what a file says" is proxy wearing verification's clothes. Caught on a live lead-agent slip (a $\rho$-factorization judgment that cited NOTATION as a verified pillar — the real argument was
*stronger* without it). Canonical statement: `doc/spike-routing.md`
§0. This Refinement sits above Refinements 1–3: they are proxy-
discipline; §0 is what proxy-discipline is *for*.*

*Refinement 5 (2026-05-18, Joseph-directed — the counterweight to Refinement 4). §0 + the gates, without this, drive a
**verification-regress** where honest incompleteness reads as unfinished duty. They prevent *false confidence*, never forbid honest "not yet."
Duty is fully discharged when, at current understanding, the artifact carries its **honest tier** + Working Notes state **what is open and what would close it** + the remainder is **released to the standing cycle**;
then stop. A live gate is legitimate only when the artifact would
*assert false confidence* without it (a canon landing, a status elevation), not as a precondition for *releasing an honestly lower-tiered* item. Canonical statement + the self-check:
`doc/spike-routing.md` §0c / its Refinement 8.*
