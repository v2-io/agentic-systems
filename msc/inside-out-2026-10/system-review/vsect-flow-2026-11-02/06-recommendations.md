**KR I.3 / I.4.** Part of `README.md`'s set.

# What I would change, in order

Each item says what, why from the record, the cost as I estimate it, and what would show it was wrong. Items 1–4 are tool work that needs no process decision; 5–8 are process-and-tool together; 9–11 are the verdicts Joseph and the lead asked for.

## 1. Make the tree agree with the record, and check it

`vsect check` gains two rules: a record whose frontmatter `closed:` / `rechecked:` / `owner:` line disagrees with the trail (189 today), and a `close --by-commit` whose commit the durable ref does not carry (17 of 18 today). `vsect sync` (or `check --fix`) rewrites the frontmatter from the trail, idempotently. `close` refuses a commit not on the durable ref, as `take … at:` already warns for versions, and `anchors` learns commits as well as versions. Cost: a day. Refuted if the frontmatter lines are read by nobody, in which case delete them and let `vsect open` be the only view, which the design preferred.

## 2. Close the commit seam

Every writing verb ends "commit them by path"; the lanes dropped half the paths. Either `vsect commit` (designed, `vsect.md` §3.11: a git commit of exactly what the verb wrote, refusing over un-revised edits) or the pre-commit hook refusing a commit that adds an event whose record file has an uncommitted change. The second is smaller and catches the case that happened. Refuted if the lanes' habit was the only cause and a brief fixes it; the record says four briefs did not.

## 3. Individuate `item`

Joseph: *"'kind: item' is a worrisome sign to me."* It is the fused composite RC1 names (part claim-defect, part authoring, part judgment, adjudicable as none). Proposal, in two steps so the 631 open items need not all be reclassified by hand:

- Add a required field at `note` time, `closes-by:` (or a `kind:` sub-field), drawn from the acts that can close it: `revision` (a defect in a named claim; should usually be a finding with a target instead), `authoring` (a record to write), `derivation` (a strengthening or spike to attempt), `citation`, `measurement`, `naming`, `tooling`, `process`, `disposal` (a recorded judgment, closed on being read). `close` then demands the matching evidence: a `revision` closes with a commit touching the segment and a check by another mind on the new text; a `derivation` with a review; a `measurement` with an `empirica/` run; a `disposal` with nothing but a reader's name.
- Run RC1's founding questions on the 45-item sample in `scripts/census3.py`'s output before fixing the vocabulary; the sample is already drawn.

Refuted if, after a landing wave, `close` events show one evidence shape serving every item; then the kinds were a distinction without a repair difference.

## 4. Separate self-recorded from independent evidence

Compute, on every securing event, whether its actor is among the revisers of the target version (the design's §5.6 in its cheapest form: same recorded name, or same session where the harness gives one). Show the dashboard's evidence lines in two columns, and `read` marks `✓` only for the independent one; the author's own record is the design's `assert` and sits on the lowest rung. Cost: a day. Refuted if independent and self-recorded checks turn out to find defects at similar rates on `run` and `read-check` lines once the rounds are no longer adversarial; today they do not (`02-measures.md` §2), and the derivation line is the one that matters.

### 4a. Identity: what a mind can see of itself, checked from a subagent's shell

Joseph's assumption, relayed by the lead on 2026-11-02: the harness session id is the durable identity of a mind, and `--by` references it, inferred and checked rather than typed. Today `--by` is typed free text (74 distinct actor names in the trail, "Claude Opus 5.5 (A.1 check 7)" and "Claude Opus 5.5 (A.1 check 7, bare brief)" among them), 5 of 2,259 events carry a `session` field, and every commit since the tag is authored by Joseph with a trailer naming only the model. I ran `env | grep -i -E 'CLAUDE_CODE|AGENT'` in this subagent's own shell (Claude Code 2.1.316, Agent-tool launch, background):

- `CLAUDE_CODE_SESSION_ID` is set, and it is the **parent's** session id (`31b7e6c1-…`, the lead's session, whose transcript directory is `~/.claude/projects/<project>/<session>/`).
- `CLAUDE_CODE_CHILD_SESSION=1` says this shell belongs to a subagent, and `AI_AGENT=claude-code_2-1-316_agent` names the harness; neither names which subagent.
- No variable carries the agent id. The id exists only as the transcript filename under the parent session, `<session>/subagents/agent-a60563e71ac9dedba.jsonl`, beside a `.meta.json` holding the agent type, the spawning tool-use id, the depth and the model, and no id field inside.

So a subagent can infer its parent's session exactly and its own identity only by inference: list `<session>/subagents/`, and if one transcript is there it is you; with parallel lanes there are several and the newest or the one still growing is a guess. For vsect that gives a three-level answer: `VSECT_SESSION` can default to `$CLAUDE_CODE_SESSION_ID` today with no typing (session-grain identity, which already makes "same mind as the reviser" checkable for lanes launched from different sessions); subagent-grain identity needs the harness to export an agent id (one line in Claude Code's environment, worth asking for through `/feedback`, which Joseph encourages), or vsect to take the transcript filename as a declared claim; and the design is right that below the substrate's grain the actor is a recorded claim (`core.md` §15), so the depth of the inference should be written on the event (`identity: harness-session | declared | inferred-from-transcript`) rather than hidden. Cost of the first level: a default plus one field on every event. Refuted if the lead's lanes are launched from one session, in which case session-grain identity cannot tell two lanes apart and the second level is the one that matters.

## 5. Make `--read` the default question, and carve the records that lapse for nothing

`take` without a read set warns and records "whole basis, undeclared"; `confirm` lists undeclared-read checks first, since those are the ones that cost the confirmer. Separately, move the `## Claim Record` sections to a sidecar the build folds in (reflection 31 item 12 already asks this for other reasons), so a record edit stops lapsing derivation checks; 13 of 36 lapsed pairs in the one confirm pass were this. Refuted if the carving spike (design Q10, five segments) shows the records and the derivations share a fate often enough that lapsing is right.

## 6. A `source` record kind with `cross` outcomes, seeded from the drains

`04-sunset.md` has the state set. Build order: the kind and the `cross` verb; an importer that reads one drain file's bolded verdicts as units (hand-check that one file first, as the items pilot did); then the rest; then `check` enforces the delete-test on `.integrated/`. Only then delete `drain/`. Refuted if the imported dispositions turn out too coarse to key (path-level where the claim was one sentence); I.10's spot-check found exactly that for one of eight, so expect a residue and record it as `needs-review`, which the design already has.

## 7. `vsect flows`: print the state machine from the trail

Joseph asked whether vsect could output a probabilistic finite-state diagram and what it would illuminate. It can, with no new recording: `scripts/fsm.py` does it in 150 lines from events already there, and `01-flows.md` §2 is its output. As a verb: `vsect flows [--kind item|finding|check|segment] [--since <rev>] [--format text|mermaid|dot|json]`, nodes labelled with their stock, edges with counts and the rate out of the source node. It is a descriptive projection over acts, not standing, so it does not run into the design's "no standing until projections are declared" rule.

What it illuminated here: the stocks nobody looks at (467 `note`d items with no act since; 182 findings with one exit; 336 lapsed checks), the two-percent `done` sink, the 47% re-find rate at the drains' edge, and the one cycle whose gain was above one (check → finding → revise → lapse → check), with the quantity that measures the gain (edit mass per round) sitting beside it. The "probabilistic" reading is honest only as frequencies over one regime; print the window the counts come from on the diagram.

What it would not show without items 3 and 4: which item kinds drain and which pool (all are `item`), and which checks are evidence (all are checks).

## 8. Smaller, each a line

- `vsect open` header: distinct counts per kind ("631 items, 182 findings, 52 questions, 336 lapsed checks, 12 upstream-unread"), and `--kind` to pick one.
- `ask --closer anyone` requires `--why`, or defaults to the asker's KR; 61 of 64 questions are for nobody.
- `findings --dispose` gets used, and the dashboard shows rejected and known-defect counts, so a wrong finding has a door.
- The `narrowed` register on the dashboard (reflection 31 item 11): "narrowed by a check" is not "known broken".
- `note --owner` refuses a non-KR string, as `recheck --owner` already does; 20 free-text forms today.
- Decisions: record the retrospective's twelve corrections as `decision` records (the kind is built in, unused), each with its reopen condition, before the next phase treats them as rules.
- Edit mass per revise on the dashboard's "At work now" and in `why`.

## 9. The second coordinator

Joseph is considering a second agent, reporting to the lead, that relays asynchronous reports, merges and commits, so the lead keeps to direction. From the record: the lead's 113 commits in the sprint were mostly those mechanical acts; the two places the record drifted (the event/file seam; the dead commit citations) are inside exactly those acts; and the confirm pass and `vsect check --strict` after each merge are second-mind work that a mind other than the author must do anyway. So the role has real content. Two cautions. First, define its duties as the list of things the tools cannot yet do (items 1, 2, 5 shrink the list), so the role does not become the place a missing verb is replaced by a habit; the drains show what a habit does under load. Second, the reactive agent must not become the integrator of last resort: the retrospective's "a new integrator each round" began as relaying. If it owns the merge, it owns the `unchecked` word in the merge commit and the refusal when a landing names nothing it retires; it does not own the fix.

## 10. The frame

Joseph's picture of this as a document-processing state machine with sources, sinks and feedback loops holds, with one adjustment that the record forces: the states are not the kinds. The same `review` kind carries an author's record and an independent check; the same `item` kind carries six repairs; the same `open` list carries five waits. The machine's states are (kind × who acted × what act), and once the actor is a column the kinds mostly fall out. That is also the design's own position ("a kind earns its place when it fails differently and is repaired differently"); the sprint founded the store without running that test, which was the right trade for a day and is the first thing the next phase should pay back.

## 11. What I would not change

The strict lapse rule (low precision, right recall; scope it, do not loosen it). Event files one per act, content-addressed, never edited: the 135 `correct` events are the system working. The bare-brief independent check: it is where all the information came from. Items closed by commits: keep, once the commits are real.
