# HANDOFF — for the lead's successor

What only the lead knows: what it has actually read, what it holds only on another agent's word, and what is in flight. Findings are not restated here; they live in the documents named below. Updated at every checkpoint (last: 2026-10-30 evening MDT).

## Resume

Read `INTENT.md`, then this file. Joseph's governing words are in `README.md`. For history, read the commit bodies (`git log` on `msc/inside-out-2026-10/` and canon). The SendMessage handles for running agents live in the session, not here. If they're lost, the agents' directories are the record.

## Read-ledger

**Read whole by the lead**

- *This effort*
  - `internal-surfaces/00-cross-surface-map.md`
  - `influx-scout/MAP.md`. Its regional files are for integrators and are not read by the lead.
  - `owner-review/00-review.md` (final v2), `owner-review/integrator-items.md`
  - `system-review/00-system.md`. Its counts are in `measurements.md`, which is unread; the review lists each command.
  - `owner-review/history/{2026-03-04,2026-05,2026-06-10}.md`
  - `spikes/spike-strategic-persistence-hard-ceiling-convention-2026-05-31-verify-1.md`. Its central gain claim was re-run by the lead.
  - The F72 landing diff (`5e621256`, `97179f6f`), reviewed whole, including the new `#deriv-evidence-allocation-ceiling`.
- *asf*
  - `PRACTICA.md`
  - `audits/STATUS.md`
  - `msc/decision-briefs-2026-07-15.md` (since folded into the ledger and deleted, 924e70f9)
  - `ref/prior-art-analysis/agentic-systems-landscape-2026-08-22.md`
  - `doc/sop/agents.sop.md`
- *aat-v3*
  - `msc/00-orientation-log.md`
  - `msc/40-emerging-picture.md`
  - `msc/maps/aat-refactored.md`
  - `msc/maps/asf-audits-and-spikes.md`
  - `msc/vsect/{README,model,vsect}.md`
- *aat-refactored*
  - `spikes/fresh-view-2026-09-29/census-findings.md`
  - `HANDOFF.md`, through "Do next"
- *arch*
  - `SUBAGENT-INSTRUCTIONS-notes.md`
  - `AGENTIC-DELEGATION.md`
  - `firmatum/utils/vsect/README.md`, plus the bodies of commits `aecd7ac`, `59436b7` and `d84ffbc`. The Rust source was not read: the evidence for it is its tests and its behavior on the asf store.
  - `firmatum/utils/md-press/FEEDBACK-2026-10-30.md`
- *asf, this effort's commits*: every commit through `612bcb65`. `801feaec` was read after it was pushed.

**Partial**

- `~/src/arch/SPIKE-PROMPT.template.md`: lines were cut at 400 characters. Read it whole before filling it.
- The first ~25 lines only of each of these:
  - `ref/enrichment-candidates-2026-05-21.md`
  - `ref/prior-art-analysis/00-impact-meta-summary.md`
  - `02-tst-core/lit-review/next-research*.md`

**Held only on another agent's word**

- Explorer findings the owner review relayed in its messages. The explorer files themselves are unread.
- Everything in `influx-scout/MAP.md` that is relayed from regional scouts. Only its `[coordinator-verified]` rows were checked at HEAD.

**Not read**

- `owner-review/explorers/*`, `owner-review/verified-at-HEAD.md`. The review carries their claims with its own verification rows; read the explorer files themselves before landing anything from them.
- `influx-scout/` regional files
- the six per-surface maps in `internal-surfaces/`
- aat-refactored's `scratch/PROPOSAL-2026-09-29-foundation-and-sops.md`
- vsect's `core`, `storage`, `session-aat`, `open`
- almost every segment body
- `CHANGELOG.md`: a log, not a source

**Verified by the lead at the primary**

- The segment and file counts in `README.md` (246 segments, 44 `old-*` files, the commit split, WN counts).
- `core.hooksPath` was dead.
- The "Reading AAT" preamble was removed in `feccd0d2`.
- relata holdings and segment uptake for the landscape survey's key works.

## In flight

- **Running:** see INTENT's "Who is on what". Agents commit by explicit path without pushing; the lead reviews, then pushes the reviewed SHA. B.1 is in its own worktree, so its branch is merged after review. Spikes get an independently briefed verifier (bare brief) before any integrator.
- **Waiting on Joseph: nothing.** Resolve uncertainty rather than route it. Two items that used to wait on him are now ordinary work:
  - Canon citing the gitignored `msc/joseph-working-notes.md` (F.3). Lift any theory content those citations need into canon, then remove the citations.
  - The 08-22 cleanup items (I.3).
- **Next for the lead.**
  1. As each agent lands, read its documents whole, then review and push by SHA.
  2. Spikes: commission a verifier with the template's bare brief, then a separate integrator.
  3. A.2, the front door, once the round-3 integrations land: B.1's Part II records now exist, so headline sentences can trace to retyped registers. Headline 2's Kalman-gain sentence is in the Part I round-3 integrator's hands.
  4. The vsect store migration (normalizer), once no checker or integrator is writing records; the vsect builder is on the line for it.
  5. When a subagent slot frees (the session caps at 20): a sixth independent read of `#scope-adaptive-system` and its two new definitions at ed2b07e4.
  - Rebuild `CURRENT-VOL1` after each canon landing, using the biber workaround in memory.

## The lead's rhythm

Joseph: *"regularly take a beat-- let all agents finalize so you have some quiet time, and rethink from the very top w/ the highest level ideation and thinking... To keep you from becoming task-oriented and missing the big picture of the *system* in service of *truth*."*

At each beat, nothing is running. The lead re-reads INTENT from the top intent down. It asks what the system (the machinery, the clutter, the methodology, the tools) needs in order to serve truth. Only then does it launch the next work. Healing the system is the lead's part, done with agents, possibly including a Fable focused on the system as the owner review was focused on the theory.

## The lead's known hazards

- **Building on relay.** Agents' chat claims get adopted faster than their documents get read. Read first, then build.
- **Intent bloat.** INTENT accretes evidence, credits and history. Joseph: *"It will get bloated and if it is not corrected immediately, it will be just yet another thing to integrate."* Correct it at the moment it bloats.
- **Narrative regeneration.** Summaries written from memory drift from the record. That is why this file only points.
- **A push sends the whole branch.** In a shared tree, the lead's `git push` carried the integrators' local commits out before review. A.1's landing went out with "Independent check: pending". Before every push, run `git log origin/main..HEAD` as its own command, read every commit that isn't yours, and push only in a later command. Chaining the list and the push in one line repeated the defect: `f4a4a334` went out unread. Separate commands did not close the race either: `801feaec` was committed between the lead's listing and its push, and went out unread. So push the reviewed SHA, not the branch: `git push origin <sha>:main`. Better still, give future parallel integrators their own worktree or branch (Agent `isolation: "worktree"`), so the lead merges what it has reviewed.
- **Rebasing a worktree branch across a reorganization.** Git's directory-rename detection can move a branch's new file into a directory it never touched. The vsect migration emptied `.vsect/objects/26/` while `items/imported/*` moved to `items/`, so a rebase carried a new object into `items/`. asf's local config now sets `merge.directoryRenames=false`, which worktrees share. A fresh clone lacks it, but only branches made before the migration cross that seam.
- **Checking a replacement against only the defect it replaced.** Two independent checkers (B.1's and Volume 4's) found the same pattern: an integrator checks its new sentence against the defect it fixes, not against the segments the new content now touches, and old wordings survive in files no record points to. Every integration brief should ask for both: a repo-wide pickaxe on each replaced phrase, and a read of the new claim against its neighbors.
- **The landing cycle that works, and its cost.** Integrator in its own worktree → the lead reads its account whole → rebase in the worktree with `merge.directoryRenames=false` → checks run there → fast-forward main → push the reviewed SHA → an independent checker with a bare brief → a round-2 integrator (a mind other than the one being checked) → the checker again. Each merge lapses checks recorded on other branches, so a second-mind confirmer pass follows merge waves (`msc/inside-out-2026-10/confirm-2026-10-30.md` has the method and its cost: about 3 in 120 bindings were actually touched).
- **A criterion that says "as stated" inherits the text's hypotheses.** Five readers confirmed `#scope-adaptive-system`'s (g′), (h) and non-vacuity "as stated"; the parenthetical "fresh noise" carried an independence no definition stated, and the sixth reader built a world that satisfies the definitions and breaks all three. Ask checkers and integrators to write criteria that name the hypotheses each step uses ("from the definitions and GA-1 as worded"). The integrator that landed check 6 added a second habit: for any counterexample, ask what its twin is on the other kernel. Check 6's repair covered only the observation side, and the mirror world (memory kept outside $\Omega$ on the transition side) was found a round later.
- **Finding work only near the last landing.** Until I.9, every task came from the owner review's ranked lists or from the previous round's checker, so the loop closed on itself while the backlog (24 audit dirs, 56 spikes, the influx regional files, Working Notes, `msc/`) went undrained. Of eleven outside-found canon defects spot-checked at HEAD, six were still present. Joseph: *"How are you currently even finding what to fix? If not draining all of the influx, audits, spikes, and so forth?"*, and: *"don't be surprised if they're just 'finding' stuff that is already waiting to be integrated-- and it will make it that much noisier and more difficult to check and integrate those influxes later."* Point every lane at the influx rows for its segments before it starts.
- **Breadcrumbs.** History and finished items accumulate in working files because writing them feels safe. Joseph: *"It does [do harm]. That's what changelog is for."* Nothing in this directory records what is finished.
