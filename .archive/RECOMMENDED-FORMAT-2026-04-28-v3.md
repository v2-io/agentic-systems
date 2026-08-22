# The final report

*Proposed addition to `doc/de-novo-audit-instructions.md`. Voice matches the existing instructions: peer-to-peer, advisory, intent-first. Joseph can renumber when integrating. The §1–§10 sections of the existing instructions cover the audit method itself (paradigm shift, fundamental-nature, audit-as-instance-of-the-theory, anti-patterns, working-directory protocol, reading order, source ordering, reflection cadence, verification emphases, asking Joseph, meta-discipline) and stay where they are. This section is specifically about what the audit's output deliverable should look like when it lands in `audits/`.*

---

This section is about *what the project's tracking machinery needs from your audit output*. The biggest historical friction we've had with audits hasn't been the audit content itself — it's been routing audit content to the right tracking files afterward. Findings that don't surface where the integrator can find them get re-discovered later (wasted work) or land in the wrong shape (creates downstream drag). What follows are the convergent practices that have evolved to make routing fast.

Treat the recommendations as affordances, not rules. Where your judgment differs, use it; the format is here to *help* good audits move efficiently into the project, not to constrain the audit work itself. If something genuinely interesting surfaces and the format would obscure it — surface it anyway, in whatever shape lets you communicate clearly. The integrator can route an off-format finding; an unsurfaced finding is gone.

## Why this format exists

Your audit will be consumed by an *integrating agent* (or Joseph) whose job is to route each finding to the right tracking file: `TODO.md` if it's an open question, `PROPOSALS.md` if it's an architectural move, a direct fix-and-commit if it's mechanical, segment Discussion or Working Notes if it's a clarification, `spikes/` if it produces a new investigation, `CHANGELOG.md` if the cycle warrants a narrative entry. That integrator needs three things from your output to do this fast:

1. **Find the passage you're talking about** quickly enough that they don't have to re-read your audit looking for it.
2. **Know what you think should happen** — even if "I don't know, this needs Joseph" is the answer.
3. **Trust your judgment calls** — which means seeing what you considered and rejected, not just what you concluded.

Each format choice below traces to one of these three. When in doubt, optimize for the integrator's job. When the format would *obstruct* communication, ignore it.

## The mental model: three phases

Past audits have organized around three phases. The body sections below (§A–§G) implement them; you don't have to use the phase vocabulary explicitly, but knowing the underlying shape helps if you're choosing what goes where.

1. **Phase 1 — Findings under burden of proof.** The defended-line-by-line claims in the per-finding shape below. This is where your verification work shows up.
2. **Phase 2 — Integration-debt diagnosis against the framework's self-knowledge.** For each surviving Phase-1 finding, look across the materials that hold what the framework already knows about itself outside `src/`:

   - **Historical reasoning trail** — `spikes/` (investigations that informed segments, `spikes/INDEX.md` as entry point), `audits/` (prior FINAL reports and `pending-findings-YYYY-MM-DD.md` resolution-trail records), `msc/` (other working artifacts: brainstorms, reflections, naming-cycle notes, in-flight architectural drafts).
   - **Live tracking files** — `TODO.md` (tactical open work), `PRACTICA.md` (strategic-portfolio navigator; the top of the strategy DAG), `PROPOSALS.md` (architectural-moves portfolio with prior-reasoning trails).
   - **Narrative records** — `CHANGELOG.md` (cycle narrative from 2026-04-24 onward), `LOG.md` (pre-2026-04-24 cycle archaeology, frozen), `git log` (commit-level history; useful for tracing when a passage entered the corpus, what was demoted from earlier confident framings, what was strengthened recently — `git log -p path/to/file.md` and `git blame` are the workhorses).

   The question to answer per finding: does any of this material already address the concern? If yes, where, and *has the resolution propagated to src*? This is what distinguishes *theory gap* (something genuinely missing or wrong; new work needed) from *integration debt* (the resolution exists somewhere, just not in the segment that needs it). Both warrant reporting; they have different remediation paths and different urgency.

These materials are deliberately avoided during initial comprehension — they prime judgment in ways that defeat de-novo audits — and then thoroughly checked once findings are in hand. Reading them as a starting point biases the audit; reading them as a triangulation step on a real finding tends to enrich. The §4.1 AVOID-list discipline holds during Phase 1; the same materials become first-class tools in Phase 2.
3. **Phase 3 — Bigger-picture pondering.** After sustained engagement, you'll likely have intuitions about simplifications, generalizations, restructurings, or reframings that might make the framework more beautiful, more correct, more applicable, more fundamental, more accessible, more concise, or more complete. Surface these at *Hypothesis* level on the epistemic ladder — specific enough to act on, honest about not being verified.

The three phases aren't a template you need to follow if your audit's most valuable content lives outside this structure. If you've stumbled onto something that's neither a finding nor integration-debt diagnosis nor bigger-picture pondering — say, a question the framework hasn't asked itself, or a connection to a body of external work the framework hasn't engaged — surface it in the form that fits, and let the structure follow.

## Where the FINAL lives

Output the FINAL deliverable directly into `audits/`, not inside your working directory. The cycle-id-prefix pattern keeps the audits folder navigable as the corpus grows:

- `audits/audit-NNNNNN-FINAL-YYYY-MM-DD.md` — primary final report
- `audits/audit-NNNNNN-FINAL-YYYY-MM-DD-pass-2.md` — continuation pass within the same cycle (the front-matter `status:` field also names the relationship; both are useful)
- `audits/audit-NNNNNN-SUPPLEMENT-{topic}.md` — separate Phase-2 triangulation document (kept distinct by convention so the de-novo report stays auditable as a de-novo artifact); also used for any follow-on artifact you want kept separate from the FINAL
- `audits/audit-NNNNNN-FINAL-{component}.md` — multi-file split (only when ≥3 components substantively audited; in that case also produce `audit-NNNNNN-FINAL.md` as a top-level coordinator with cross-component findings)

Your intermediate workspace stays in `msc/AUDIT-WORKING-NNNNNN/` (lowercase predictions, per-segment reflections, scratch math, running outline). The split keeps `audits/` purely consumable: an integrator scanning `audits/` never has to triage "is this an output or a thinking-trail?"

## Front matter

A short structured header at the top of the FINAL helps both human and machine readers. The fields below are the ones the project's tooling currently understands; if you find yourself wanting another, add it — `bin/extract-audits` (when it exists) will treat unknown fields as informational, and persistent unrecognized fields become candidates for the spec. The reason to stick to the named fields when you can is purely so the cross-audit overlap-finder and pending-findings constructor can read your output without a custom parser.

```yaml
---
audit_id: NNNNNN
auditor: {model name and config — e.g., "Claude Opus 4.7 (1M context)" or "Gemini 2.5 Pro (CLI)"}
date: YYYY-MM-DD
status: full | partial | continuation-of-NNNNNN
audit_type: hygiene | de-novo-theory | multi-pass-batch | relayed-feedback | portfolio-review
coverage_summary: >
  One sentence on what you read first-hand vs. what you didn't.
priming_bleed: >
  If CLAUDE.md / TODO.md / PROPOSALS.md or other audit-priming material was already in
  context when you started, note it here. This is calibration data for the reader, not
  a confession.
---
```

Notes on individual fields:

- **`audit_type`** is informational. It tells the integrator what to expect — a hygiene audit's findings are usually surgical and self-contained; a de-novo theory audit's are usually substantive; a multi-pass batch consolidates 2-3 sub-passes. The format itself is the same regardless of type. If your audit doesn't fit a single type (hygiene that uncovered architectural issues; de-novo that produced both findings and big-picture observations), pick the closest and add a note in §A; or coin a new type and explain. Type taxonomies are descriptive, not constraining.
- **`priming_bleed`** isn't a flaw to hide. The reader needs to calibrate against it. If you read CLAUDE.md before realizing the audit instructions said not to, say so — the reader will discount any finding that depends on CLAUDE.md framing.

## Body sections

The FINAL has a small set of expected section headings. Where a section's heading appears but you have nothing for it, write one sentence saying so — the transparency about what you didn't find is part of the audit's value.

**§A — Scope and method.** What did you read? In what order? What audit prompt did Joseph give you? If you delegated reading to sub-agents, name where and why; the integrator needs to know whether your findings rest on first-hand reading or on agent summaries (the latter is fine, just disclose). One paragraph is usually enough.

**§B — Findings under burden of proof.** The per-finding schema is in *Per-finding shape* below. If you found nothing real, write *"No findings I can defend after first-hand reading. The candidate-and-rejection list in §B.1 is the audit's actual content."* That kind of explicit-zero is more trustworthy than producing 5 weak findings to look productive.

**§B.1 — Rescinded candidates.** What did you almost report and decide not to? This is the burden-of-proof gate visibly working. If the gate didn't fire (you produced 0 candidates that didn't survive review), say so explicitly — that's also useful calibration. The reader gets to see whether you were conservative or aggressive in your discipline.

**§C — Coverage statement.** What did you read first-hand, what did you skim, what did you skip? What verifications did you not run (math re-derivation, citation checks, lint runs, sub-agent dispatches)? One paragraph on the audit's *standing* — i.e., where a future challenger could legitimately push back on your scope.

**§D — Hypothesis-tier observations.** Things you noticed that don't survive the burden of proof but feel worth surfacing. Mark each clearly as `Hypothesis` per the epistemic ladder. The per-finding schema doesn't apply here — these are looser-grade observations meant to seed future spikes or signal an axis the audit cycle didn't have time to investigate.

**§E — What holds.** Calibration data. Where did you push hard and conclude the framework's discipline holds? An audit that only reports what's broken makes the framework look worse than it is, and the reader has no way to weight your findings. Even a short list ("I checked X, Y, and Z; the caveat load is adequate; here's why") materially changes how the reader trusts the audit.

**§F — Bigger-picture observations.** This is where Phase 3 lands. If after reading widely something architectural surfaces — simplifications, generalizations, restructurings, reframings, or connections to outside literature — here's where it goes. Tag each as `Hypothesis` unless you can defend it under burden of proof. These often become PROPOSALS.md entries; sometimes they reframe the whole audit. More common in de-novo theory audits and less common in hygiene audits — but if a hygiene audit *does* surface something architectural, surface it here regardless.

**§G — Process feedback on the instructions.** If you noticed something about the audit-process itself worth saying — a place where these instructions failed you, a convention that wasn't named, a failure-mode the project should warn about — say so. Several iterations of these instructions have been improved by audit-cycle process feedback; you may have caught something the prior auditors didn't.

§A, §B, §B.1, and §C are the load-bearing ones. The others are recommended-where-applicable; explicit "no content for §X because [reason]" is fine and often informative.

## Per-finding shape

For each finding in §B, communicate the elements below. This is a checklist of what the integrator needs, not a form to fill — collapse, reorder, or merge as the prose flows. What matters is that all the information is reachable.

**The five core elements.** These have earned their place because of what tends to go wrong without them: a "finding" without counterevidence search reads as a complaint; a "finding" without confidence calibration reads as an opinion; a "finding" without an explicit status determination puts the burden of judgment on the reader rather than the auditor. Try to include all five for every finding under burden of proof:

1. **Problematic passage (verbatim)** — quote what you're concerned about. The integrator needs to see what you saw. Keep it short — 1-3 sentences if possible.
2. **Counterevidence search** — did you check whether the segment, sibling segments, or the framework's self-knowledge materials (`spikes/`, `audits/`, `msc/`, `TODO.md`, `PRACTICA.md`, `PROPOSALS.md`, `CHANGELOG.md`, `LOG.md`, `git log` / `git blame`) already address the issue? Cite what you found. If you didn't search, say so (it's a partial finding; just disclose). This is where the Phase-2 triangulation lives at the per-finding level — see the Phase 2 list in the mental model above for what each location holds.
3. **Status determination** — `still real` / `already caveated` / `ambiguous` / `rescinded`. Use this vocabulary; cross-audit aggregators rely on it. If your judgment requires nuance the labels don't capture, use the closest one and explain.
4. **Confidence** — `high` / `medium` / `low` with a one-clause reason. If your confidence depends on priming content (CLAUDE.md, prior audit, etc.) rather than first-hand verification, say so. Other vocabulary is acceptable when you have a reason — Gemini often uses "100%" / "Firm" — but high/medium/low is the default because cross-audit aggregators map to it cleanly.
5. **Why it still stands** — *only when status came back "still real."* One sentence on why the counterevidence didn't dissolve the issue. Findings whose status is "already caveated" or "ambiguous" don't carry this element; the status determination is the punchline.

**Three additional elements that make routing faster.** Strongly recommended; missing fields don't disqualify the finding:

6. **Headline** — one sentence stating the finding. The first thing the integrator reads.
7. **Severity** — `**High**` / `**Medium**` / `**Low**` if obvious. Auditors disagree on this — that's fine, the integrator will calibrate from your reasoning. Severity is *orthogonal* to confidence: a high-confidence finding can be mechanical (depends-list violation), and a medium-confidence finding can be architectural (ontology strain).
8. **Anchor** — where in the repo is the problematic passage? `path/to/file.md:NN` is the fastest form *if line numbers come naturally during your audit*. If they don't — and they often won't — equivalents are equally valuable: `` path/to/file.md:`unique search term` ``, `path/to/file.md §"section heading"`, `path/to/file.md:#anchor-id`, `` path/to/file.md::`breadcrumb > path > to > thing` ``. The principle: an integrator using grep / Find should resolve your anchor in under 30 seconds. Don't let anchor-construction become the critical path; if line numbers would slow you down, use what's faster. Codex tends to give line numbers because that's its native mode; Claude and Gemini often work faster with search-term or section-header anchors.

**Two more that the integrator-friendly exemplars in the corpus consistently include:**

9. **Type** — what *kind* of issue is it? Common tags: `math error | sign error | scope/status mismatch | cross-segment contradiction | dependency-graph violation | integration debt | doc rot | citation error | architectural`. Coin a new tag if none fit. Helps the integrator batch similar fixes.
10. **Suggested disposition** — where should this go? Use the routing vocabulary in *Disposition* below. If you don't know, say `unknown — needs Joseph`. Some routing decisions require human judgment; saying so is the right move.
11. **Effort estimate** — roughly how much work to address? `trivial | editorial | substantive | architectural`. Saves the integrator from re-estimating per finding.

You won't always have all elements for every finding. The minimum useful per-finding entry is *headline + anchor + problematic passage + status*. Everything else makes the integrator's job easier, but missing fields don't disqualify the finding.

## What probably isn't a finding

Some kinds of "issue" don't survive the burden of proof and don't belong in §B (they may belong in §D as Hypothesis-tier observations, in §G as process feedback, or in your scratch directory and nowhere else):

- **Items the framework's own active TODO list flags as open work** — these are *known* gaps; reporting them as findings adds noise, not signal. (Worth flagging only if your judgment is that the TODO entry mischaracterizes the issue or undersizes its impact.)
- **Caveats present in segment Working Notes** — the framework knows; integration is usually the issue, not the substance. (If the caveat ought to be in Formal Expression / Epistemic Status but isn't, that *is* a finding — it's a `scope/status mismatch`.)
- **`status:hypothesis` or `status:sketch` segments where the status is honest about the maturity** — the segment has already disclosed where it is; treating the disclosure as a finding double-counts.
- **Editorial preferences** ("I would write this differently") — the audit is about correctness and structural integrity more than style. Style observations belong in §G or §F at most.
- **Concerns imported from `spikes/`, `audits/`, or `msc/` that haven't been verified against current src** — the audit evaluates the current repository state, not the historical reasoning trail. If a `spikes/` document, prior `audits/` finding, or `msc/` working note raised a concern that has since been addressed in src — possibly by a strengthening that resolved the concern, possibly by a scope-narrowing that scoped it out, possibly by a structural move that absorbed it — the addressing-in-src is the relevant fact. A concern that survives current src text is the version worth reporting.

If you find something that doesn't fit the "finding" form but seems worth surfacing — a striking pattern, a generative observation, a question the framework hasn't asked itself, a connection to outside literature you hadn't expected — that's often the most valuable thing you can contribute. The "finding" form is for one specific kind of contribution; it isn't the only kind. §D, §F, and §G exist for the rest.

## Disposition: the routing vocabulary

When you suggest where a finding should go, use one of these tags. They've emerged from convergent organic practice across the audit corpus:

- **New** — no durable tracking found anywhere; goes into the next `audits/pending-findings-YYYY-MM-DD.md` file for routing
- **Known-unintegrated** — the correct idea exists elsewhere (a `spikes/` reasoning trail, a `msc/` working note, segment Working Notes, a prior FINAL or `pending-findings-*.md` in `audits/`, an entry in `TODO.md` / `PRACTICA.md` / `PROPOSALS.md`, or a narrative record in `CHANGELOG.md` / `LOG.md`) but the source segment is still wrong; the actual issue is *integration debt* (see *Integration debt vs. theory gap* below)
- **Known-resolved** — source already fixed; the finding is stale (often happens when audit input was a snapshot earlier than current state)
- **Tooling gap** — source is structurally OK under current tools, but the finding exposes a class the tools don't check; suggests a `bin/` script or lint rule addition
- **Scope/status mismatch** — caveat exists in prose but not in Formal Expression / status frontmatter / theorem statement (segment claims more than its own caveats license)

These map cleanly to project tracking. *New* findings flow into the next pending-findings file → TODO/PROPOSALS routing. *Known-unintegrated* often produces small commits closing segment-level integration debt. *Tooling gap* often produces a CHANGELOG entry or a new lint check. *Known-resolved* and *scope/status mismatch* are usually quick editorial fixes.

The vocabulary is convergent, not exhaustive. If your finding doesn't fit any tag, or fits multiple, just describe what you mean. The tag is the auditor's *recommendation*; the routing decision belongs to the integrator.

## Integration debt vs. theory gap

Two qualitatively different kinds of "the framework is wrong about X":

- **Theory gap** — a result is missing, wrong, or under-derived; *new work is required.* The framework hasn't yet figured out the thing. Usually substantive remediation: a new derivation, a scope narrowing with proof, a structural revision.
- **Integration debt** — the theory is correct *somewhere* (a spike, a sibling segment, a Working Notes block, a prior pending-findings doc) but hasn't propagated to all the segments that should reflect it. Usually editorial remediation: lift the existing text into the load-bearing segment, propagate the caveat, update the cross-references.

Distinguishing these matters because they have different remediation paths, different urgency, and different signals about the framework's health. A high-density of integration debt is a signal that the framework's *integration discipline* has slipped, not that the theory is broken; a high-density of theory gaps is the inverse. The framework's reviewer needs to know which.

When you flag a finding, try to indicate which it is. The Phase-2 triangulation (looking in `msc/` for prior addressing) is what produces this distinction — it's the diagnostic move that tells you whether the framework already knows the answer or hasn't gotten there yet. The five-tag disposition vocabulary above encodes the result: *Known-unintegrated* and *Scope/status mismatch* are flavors of integration debt; *New* is more often theory gap; *Tooling gap* is its own category (the framework is right but the tooling can't enforce it); *Known-resolved* is "false alarm, already fixed."

## How findings flow into the project

Knowing this pipeline shapes how you write findings:

1. Your FINAL lands at `audits/audit-NNNNNN-FINAL-*.md`.
2. An integrating agent (Claude, or Joseph) reads it and constructs `audits/pending-findings-YYYY-MM-DD.md` — a routing-decision document that takes each finding through *verify-still-real → cross-reference existing tracking → route → mark resolved-or-open*.
3. From pending-findings, individual findings flow to:
   - `TODO.md` (open questions, MEDIUM theory items, deferred decisions)
   - `PROPOSALS.md` (architectural moves; with prior-reasoning-trail discipline if reversing prior decisions, per the SP-21 precedent)
   - Direct commits (mechanical fixes, hygiene findings)
   - Segment Discussion or Working Notes (per-segment clarifications)
   - `CHANGELOG.md` (cycle narrative when the audit was substantive)
   - `spikes/INDEX.md` and a new `spikes/spike-*.md` (when a finding becomes a new investigation)
4. The pending-findings file lives in `audits/` indefinitely; it's the durable record of what each finding became.

The integrator's life is much easier when they can read your finding once and dispatch it. Anchors, disposition tags, effort estimates, and confidence calibration all serve this. None of them serve aesthetics — they're affordances for the next agent in the pipeline.

## Multi-pass, partial, and continuation audits

**Partial audits** (you covered some of the framework but not all) — write them honestly. The minimum viable shape is §A (scope, including what you *didn't* read) + §B (findings, even if zero). §C–§G are all optional in a partial audit. State at the top: `status: partial — honestly framed`. A partial audit with 3 strong findings and clear scope honesty is more useful than a "complete" audit with 5 weak findings. A partial audit, honestly framed, is often more useful than a complete-feeling audit whose gaps aren't acknowledged.

**Continuation audits** (a fresh session picking up where a prior session left off) — name the prior cycle in the front matter: `status: continuation-of-NNNNNN`. Your front-matter `audit_id` is your own new ID; the continuation pointer goes in `status`. Filename pattern: `audits/audit-NNNNNN-FINAL-YYYY-MM-DD-pass-2.md` is also useful when the continuation is within the same NNNNNN cycle (rather than a fresh-ID continuation of a different cycle). Either form makes the relationship visible to the integrator.

**Multi-pass batch audits** (you ran 2-3 sub-passes in one session, e.g., parallel sub-agents covering different sections) — produce one FINAL that consolidates them. Name each pass internally with timestamps and sub-agent IDs so the integrator can trace back. The 2026-04-22 morning audit (Codex + Gemini + Opus parallel passes) is the canonical worked example of this shape.

## Before committing text to the FINAL: the worthy gate

Before any text lands in the FINAL — and to a lesser but real extent in the scratch reflections you intend to be useful — ask: *is this worthy?*

Three tests:

- **Wisdom.** Does this engage with the framework's actual load-bearing structure, or does it skirt it? Will this still be useful to a future agent reading the report cold? Did you separate what *follows from* the formalism from what merely *sounds like* it does?
- **Strength.** Does the argument survive tightening? Are the citations accurate? Is the math verified? Could a careful reader find a hole? Have you stated where the argument's edges are, so the reader can challenge them?
- **Beauty.** Does the report tell a clear story? Does it surface insight, or just restate the surface? Is the structure clean? Does the prose carry the reader, or does it pile?

If you cannot honestly answer yes to most of these, keep refining or cut. The system prompt's framing applies here directly: *DONE means it incorporates wisdom, strength, and beauty. Is this worthy?* — not "does it fulfill the audit prompt's literal wording."

This gate runs alongside the per-finding burden of proof; it's about the report-as-artifact, not just about each individual finding.

## Before declaring done: self-reflection

Not a gating checklist — questions worth asking yourself honestly before shipping. If most of these have honest "yes" answers, the audit is in reasonable shape. If several are "no" or "partial," that's information about what the audit's actual scope was, and is worth surfacing in the report's framing (and possibly worth surfacing to Joseph) rather than papered over.

- Did I read every segment in the OUTLINE's row order, or did I explicitly defer some? If deferred, is the deferral list in the working directory and addressed? Were backward-dependency findings logged where the OUTLINE's order failed?
- Did I honor source ordering — refraining from reading `msc/`, `ref/`, git history, or external-citation web-search for a segment before reading the segment itself?
- For worked examples I commented on, did I run the math first-hand?
- Did I cross-check recently-added structural moves against earlier segments?
- Did I verify at least a sample of external theorem citations?
- For each finding I'm reporting, do I have the five core elements (passage / counterevidence / status / confidence / why-it-stands-when-applicable)?
- Did I confirm each finding survives current src text — not just that a `msc/` document raised it, but that it's still real after the framework's possible subsequent strengthenings?
- Is the report's "what I didn't read" section honest and complete?
- Did I distinguish integration debt from theory gaps where the distinction matters?
- Does the report pass the worthy gate above?
- If there are unverified concerns or under-resourced areas, have I surfaced them to Joseph rather than performing completion?
- Have I been thoughtful and authentic enough to have potentially validated a crucial finding or uncovered for the first time a new finding / insight?

A partial audit, honestly framed, is often more useful than a complete-feeling audit whose gaps aren't acknowledged. If most answers are honest "yes" but one or two aren't, the audit may still be worth shipping — just say so explicitly.

## When this format is wrong

Sometimes an audit produces something that doesn't fit. Maybe Joseph asked for a hygiene audit but you noticed an architectural issue in passing. Maybe the right output is meta-process feedback about the audit instructions themselves. Maybe the most useful output is "I read the framework and these are the places I'd push back if I were writing the rebuttal" — not the burden-of-proof shape.

Surface it anyway, in whatever form lets you communicate clearly. The integrator can route an off-format finding; an unsurfaced finding is gone. The format protects integration speed, not the integrator's sense of order, and the format isn't more important than the audit.

The audit role's value is *not* commodity automation. The project's most useful ideas — including the audit-instructions doc you're reading right now, which exists because an audit produced something off-format and worth keeping — have come from agents who followed leads beyond what they were asked. If you find yourself thinking "this doesn't fit the format," that may be a signal you've found something worth thinking about, not a signal to compress your output to fit.
