# How ASF records what it knows: working notes toward an in-place repair

**Feeds: KR5.1** (`../INTENT.md`, O5: the machinery tells the truth about itself).

*To Joseph, and to whichever agent picks up the "meta" part of the goal. Written 2026-10-30 by the lead coordinator (Claude Opus 5.5) while the owner review and the two maps run. These are working notes and hypotheses, not a plan. The owner review may move them. Everything cited I read whole today unless marked.*

Joseph named "a system of agentic truthification about agentic theory" as wholly worthy work. This file asks a narrower piece of it. ASF already has machinery for saying how sure it is of each claim: `type:`, `status:`, `stage:`, equation-level tags, Epistemic Status paragraphs, the audit and spike routing SOPs. Where does that machinery tell the truth about the theory, where does it not, and what is the smallest in-place change that would make it tell the truth?

## What has been measured about the machinery

The primary is a census of ASF itself: `~/src/aat-refactored/spikes/fresh-view-2026-09-29/census-findings.md`, written 2026-09-29 at asf `a3db02e`, by an Opus 5.5 census agent. It parsed all 246 segments and the whole `status:` history over 1,166 commits, and read 25 Epistemic Status sections. I have not re-run its scripts. Its counts for `status:` and `stage:` match my own frontmatter counts taken this morning at `4ee2b895` (see `../README.md`). The theory trees haven't moved since 2026-08-24, so its line-level findings very likely still hold.

- **`status:` mixes three different things in one word:**
  - form: `conditional`, `robust-qualitative`, `heuristic`;
  - ground: `axiomatic`, `empirical`, `discussion-grade`;
  - attainment, meaning how far the argument has been carried: `exact` ("the derivation closes") and `sketch` ("unfinished").
- **The same evidence produced different labels from different reviewers.** A review's four status rulings were committed as four different values (0 of 4). `der-recursive-update` flipped exact → conditional → exact over an Epistemic Status paragraph that never changed. An audit-flagged overclaim took 80 days to reach the frontmatter.
- **For proof-bearing segments, the only live information in `status:` is the exact/conditional bit, and that bit is a fact about premises.** It asks whether every premise is established upstream or stated only locally. It went wrong because people judged it by hand. Once premises are things that can be pointed at, it can be computed.
- **Securing acts are not recorded anywhere a reader or tool can see them.** Re-derivations, independent verifications and Joseph's ratifications appear only in Epistemic Status prose, in 4 of the 25 sections read. The frontmatter never encodes them. Not one status change in seven months cites "someone re-derived it and it held."
- **Refutation had no slot.** The one time a claim was refuted, the field got `status: false`, a value outside the vocabulary, and the next day it got `conditional`.
- **`stage:` stalled:** 203 of 246 segments are `draft`. Joseph ruled on 2026-07-14 that `status:` is the live tier. The few gate passes that did happen tracked something real: no `sketch` segment ever reached `claims-verified`.

## What the earlier failures add

- **aat-refactored**, per its own record and aat-v3's map of it: "a surface claims more than what's under it." The sharpest instance is commit `d60c511`. It landed 23 seconds after an independent verifier and dropped the verifier's qualifier, so the integrity clause contradicted itself and a hypothesis got relabelled "now exact." A mapper named the third failure class: looseness *in the checking itself*. Checks were run against one member of a counterexample family, and examples were treated as a checklist rather than as a class.
- **ASF's own audits.** The newest full FINAL (731548) found every correctness finding to be "a statement-layer defect sitting on correct algebra." The May gem-hunt found "unnamed relocation, not wrong math." Both say the machinery that *says what is claimed* is where truth leaks.

## The principles worth importing, from aat-v3's `vsect` design

Source: `~/src/aat-v3/msc/vsect/{README,model,vsect}.md`, a draft revised after three de novo audits; nothing in it is decided. These are the ideas that bear on an in-place repair, stated without vsect's vocabulary:

1. **One fate, one atom**, Joseph-endorsed 2026-08-31. A claim's formal statement, gloss and defending discussion share one fate. Two claims in one file that could fail separately are two things. ASF segments routinely hold several. The aat-refactored census found six of eight accepted review findings against one segment landing on sentences with no name.
2. **Author the inputs, compute the headline.** Authors declare form, premises and ground. Standing is computed from recorded acts and never typed. Until it can be computed, show the raw evidence.
3. **Evidence belongs to the text it examined.** A check binds to the exact version it read. Edit the text, or redefine something it leans on, and the check stops counting until someone else confirms the change didn't touch it. This is the landing rule `d60c511` needed.
4. **A decline is an event.** "I looked and chose not to lift this" is recorded, so that "no record" keeps meaning "nobody looked." ASF's ~5,500 lines of Working Notes cannot currently distinguish "considered and set aside" from "never seen."
5. **A refuted statement carries a visible mark in its own file**, and so does everything resting on it, until it is replaced.
6. **Teaching narrates, never supports.** Intros, `impl-*` segments and Findings Briefs describe claims. When what they describe changes, they go stale. aat-v3's reading of verisectorium's conclusion: the statement layer is where the defects sit, so audit those rows hardest.

## What an in-place version could be (hypotheses, each with what would refute it)

ASF need not wait for a tool to stop lying about itself. Each of these could land in the existing files with today's tooling:

- **H-a. Retire hand-set `status:` as a headline; keep the declared inputs.**
  - The equation-level tags (`*[Derived (Conditional on …)]*`) already sit next to the math and declare form and premises per claim.
  - A small script could compute each segment's exact/conditional bit from `depends:` plus locally named premises, and report disagreements with the frontmatter.
  - *Refuted if* the tags turn out too inconsistent to compute from without first being rewritten. Then the rewrite *is* the repair, and its size is the real cost.
- **H-b. Make securing acts recorded events, using git as the store.** Commit trailers (`Role:`, `Read-at: <sha>`, `Checks: <slug>#<claim>`) plus a reader script would show, per claim, who checked which version.
  - This is cheap because every commit already carries a `Role:` habit in this effort.
  - *Refuted if* checks routinely span many claims in ways trailers can't name. That would point back to naming claims inside segments (H-c) as the prerequisite.
- **H-c. Name the independently-failable claims inside segments**, giving them stable anchors. Do it lazily: only where a finding, check or premise needs to point at one.
  - *Refuted if* a sample of ~20 segments shows claims too entangled to name without rewriting the segment. That would be a theory finding in itself, about where ASF's statements aren't yet separate thoughts.
- **H-d. Working Notes get a disposition marker when someone looks**: lifted, declined with reason, or still open. That turns the WN mass into something readable as a backlog.
  - *Refuted if* the owner review or the internal-surfaces map shows most WN content is better moved wholesale than marked in place.

A cross-pollination worth naming. aat-v3's planned first test of its record model is "re-marking five ASF Part I segments into statements and checking where their existing findings fall" (`open.md` Q7, as recorded in its orientation log). This effort could run that test *on live ASF*, in place. That would give aat-v3 evidence from a real corpus and give ASF its first named claims. Both experiments would gain from it. Whether to do it is a coordination question for Joseph and the aat-v3 coordinator, not mine to decide.

## Where this sits against Joseph's frame

The frame says *not procedure, not methodology, not pedantry*. Everything above is machinery, so it earns its place only if it changes what the theory truthfully says and how well that reaches a reader. The test I'd hold it to: after the change, could a newcomer tell from the files alone which claims are established, by what, and which are not, without trusting whoever wrote them? Today they cannot. The census shows that even careful readers projected the same text differently. If a proposed change doesn't move that, it's tidiness and should be dropped.
