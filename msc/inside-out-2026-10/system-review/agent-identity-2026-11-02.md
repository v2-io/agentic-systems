*KR I.4, under objective I ("the system keeps it true"): standing is read from recorded checks, not typed. A check can be called independent only if the record knows who made it.*

# Agent identity: what is installed, what it rests on, and how to re-test it

Written 2026-11-02 by the general-purpose subagent `0903e35e-b03e-407c-97af-e97ae41f543d/a4d8232afc177bfaa`, launched by the lead of this session to install per-agent identity estate-wide and have vsect and git commits use it.

## What changed for every agent, in one paragraph

Every Bash command a Claude Code agent runs on this machine now carries `CC_AGENT='<session>/<agent-id> parent=<key> type=<type> depth=<n> src=agent-identity-hook/2'`; the main session's key is just `<session>`. The values are Claude Code's own ids, written in by a global PreToolUse hook. The agent never sees the prefix. vsect records that key on every event, so `--by` is an optional label, and it compares agents by key where it used to compare typed names. Every commit made from such a shell gets `Claude-Agent:`, `Claude-Agent-Type:` and `Claude-Agent-Parent:` trailers, in every repository, through a global git hook. The commit author stays Joseph. `vsect whoami` shows any agent what is recorded about it.

## Installed where

| Where | What |
|---|---|
| `~/src/agent-core/claude-code/agent-identity/` | the source: `agent-identity-hook.py`, `git-agent-trailer`, `test-agent-identity`, and `README.md`, which is the variable's contract, the measurements, and how to remove it |
| `~/.claude/hooks/agent-identity-hook.py` | symlink to the source above; `~/.claude/hooks/` is new |
| `~/.claude/settings.json` | added `hooks.PreToolUse` (matcher `Bash`, command `/usr/bin/python3 -I ~/.claude/hooks/agent-identity-hook.py`) and the allow rule `Bash(export CC_AGENT=*)`; nothing else in the file changed (diffed against the backup, `~/.claude/backups/settings.json.before-agent-identity-2026-11-02`) |
| `~/.gitconfig` | `hook.claude-agent-identity.event = prepare-commit-msg` and `hook.claude-agent-identity.command` pointing at `git-agent-trailer` in the source dir |
| `~/.cargo/bin/vsect` | rebuilt from arch's `firmatum/utils/vsect/` (`cargo install --path`) |
| arch, `firmatum/utils/vsect/` | the identity code in `src/`; `README.md` documents it; `agent-id-detection.md` is corrected (below) |
| `~/.claude/CLAUDE.md` | the vsect entry no longer tells agents to type `--by`; a new entry describes `CC_AGENT` and the trailers |
| agent-core `README.md` | lists the new directory |

**Why agent-core and not arch/firmatum.** Joseph asked, mid-run, that the hook's source live in a versioned repo with `~/.claude` holding only a reference, in arch/firmatum or agent-core. I chose agent-core. Its own README calls it "a skunkworks for … agent infrastructure and practice, before anything is lifted into" proprium's corporeum. It already keeps Claude Code harness notes in `claude-code/`. The hook is Claude-Code-harness infrastructure, not part of vsect: it also serves git. agent-core is private (checked with `gh repo view`), so naming machine paths there exposes nothing; arch is public. agent-core's tree was clean, and arch's had other agents' uncommitted work. The cost: a public reader of vsect's README sees the variable's contract but cannot read the hook. Lifting it into `arch/proprium/corporeum` later would fix that, and nothing in it is private.

## What vsect does now

- **Every writing verb** takes identity from `CC_AGENT` when it is present. The actor carries `agent:` (the key), `agent-type:`, `parent:` and `session:`, and `--by` becomes an optional label (default `general-purpose a4d8232a`, `main 0903e35e`). Without the hook, `--by` is required as before.
- **`identity:`** is on every event: `harness-agent` (the hook's key), `harness-session` (only `CLAUDE_CODE_SESSION_ID`, which a lead shares with all its subagents), or `declared` (typed only). It is the review's §4a suggestion, and it is always computed, never read from a file. A key counts as harness-supplied only when `src=` names the hook.
- **Who is compared on the agent key** when both acts have one, and on names otherwise (`Actor::same_mind`). That covers `confirm`'s refusal of the reviser, `review --by-revision`'s refusal of the reviser of the answering revision, and claims (`claim`, `release`, `claimed`). Measured on a clone of asf:
  - the same agent typing a new name is now refused as the reviser, where the old binary let it through;
  - a different agent typing the reviser's name is now allowed, where the old binary refused it;
  - a second agent claiming a record under the same typed name is now refused, where it used to count as the same holder.
- **Hand-written reviews.** `take reviews/x.md` uses the `author:` block, which its writer typed. That block counts as `harness-agent` only when it names an `agent:` and the mind running `take` has that same key. Otherwise it is `declared`, and the taker is recorded on each event as `taken-by:`. `take --check` writes the key into the review it creates, so its own takes are attested.
- **`vsect whoami`** prints what would be recorded here, as an `author:` block to paste into a review.
- **Forward compatibility.** Unknown actor fields are now carried through unchanged (`Actor.extra`). I found this because the previous binary reads any event carrying `agent:` as *edited*: it dropped the unknown keys before re-hashing, and `vsect check` failed with structural items. So an old `vsect` binary run against a store that has new events will report them as edited. There is one on PATH and it is replaced; any copy elsewhere needs reinstalling. The next field added to the actor, which the independence item may want, will not have this problem.

**Room for `item:separate-self-recorded-from-independent-evidence`.**

- **What is there.** The item needs, per securing event, whether its actor revised the target version. `State::reviser_actors_between` now returns recorded actors rather than names, and `same_mind` is the cheap comparison the item's text names.
- **Beyond self versus other.** A key plus `parent:` and `agent-type:` also lets the item tell apart:
  - a check by the reviser's own subagent, one step of lineage;
  - a check by a `fork`, which inherits its parent's whole context and is the least independent kind of other mind;
  - a check by a sibling the lead launched with a bare brief, the kind behind the review's 65 of 153.

  Full lineage beyond one step needs either more events by the ancestors or a look at the harness's meta files. The hook could export the whole chain if the item wants it.
- **What the trail cannot do.** The 116-of-116 and 65-of-153 figures rest on typed names. The existing 2,259 events can't be recomputed by key, since 5 carry a session and none a key. Independence by key starts from today's events.
- **Commits.** `Claude-Agent:` trailers make possible a second check the item may want: whether the agent closing an item `--by-commit` made that commit.

## What was verified, and how

**The hook, end to end against disk.** `test-agent-identity` (in the source dir) runs throwaway `claude -p --model haiku` sessions. It reads every value back from the transcripts and the harness's `agent-<id>.meta.json` files, never from the model's relay.

- **Depth 0, 1 and 2.** Each agent's echoed key matched its own transcript file's name. Each parent matched the meta file's `parentAgentId` (or the main session at depth 1), and each depth matched `spawnDepth`.
- **Commits.** A commit made by the depth-2 agent in a scratch repo carried its own key, its parent's key and its type as trailers.
- **Results.** 14 of 14 with the source passed by `--settings` (`--repo`, before the auto-mode phase existed). 15 of 15 against the install, under the current `CC_AGENT` form, twice. The second run, after the last edits, used the natural-request auto-mode phase and the `disableAllHooks` control; its sessions are `f51065a9-…` and three more, listed by the script.

**This session.** The settings change took effect in running sessions without a restart. My own Bash calls carried the identity minutes after the install, and its id matched my meta file. So every Claude Code agent running on this machine at 20:23 got the hook mid-session.

**Git hook placement.** In a scratch repo with `core.hooksPath = .githooks` and its own `pre-commit`, the config-based `prepare-commit-msg` ran alongside it. It also ran under `--no-verify`, and the trailer joined the existing `Co-Authored-By` block. `git hook list prepare-commit-msg` in asf shows it as `global`.

**Permissions.** This is where the design write-up was wrong, and it matters most. `agent-id-detection.md` said `updatedInput` leaves permission behavior unchanged. It does not: the permission check runs on the rewritten command.

- **Default mode.** With only `Bash(echo:*)` allowed, the first form's nine exports made the `echo` itself need approval. With the allow rule, the `echo` runs, and the transcripts show two other commands were really attempted and refused: a `touch` after the export still needed approval, and `export CC_AGENT=$(touch …)` was refused by the harness's export parser.
- **Auto mode** (Joseph's `defaultMode`). The first form, nine `CLAUDE_*` exports, drew classifier denials (`[Auto-Mode Bypass]`) on ordinary read-only commands: 6 of 24, against 0 of 56 with no hook. More variants were measured; the README has the table. Five assignments in one `export` were worse (8 of 48); a single packed variable drew 0 of 48. Joseph, when he saw the direction: *"feel free to use new env variable names that don't conflict with existing usage."* `CC_AGENT` had no prior use here. Installed, under his full user settings, the control being the same settings with `disableAllHooks`:
  - with a natural request ("I am getting oriented… tell me…"), the hook drew 0 of 64 against the control's 0 of 63;
  - asked to run commands "exactly as written", it drew 4 of 112 against 0 of 64.

  The residual looks like the classifier noticing that the executed command differs from what the user literally asked for. The natural request is the representative case.

**Exposure while this was built.** The first form was live estate-wide from 20:23 to 20:38 (file mtimes). Agents running in auto mode in that window may have had ordinary commands denied. Agents in default mode were covered by the first form's allow rule. The switch then left a window of about ten seconds (20:38:33 to 20:38:43) where the new export had no allow rule. If anyone saw unexplained denials around then, this is why.

**vsect.**

- Unit tests pass, 17 of 17. They include old-shape events hashing as before, unknown actor fields surviving a round trip, `CC_AGENT` parsing and the marker requirement, and `same_mind` in all four combinations.
- On the real asf store, the new and old binaries gave byte-identical `vsect --format json` dashboards and `vsect open --format json` ledgers, run at the same moment, and both passed `vsect check`.
- On a throwaway clone of asf, I exercised:
  - inline `take --check` with the hook, with no hook (exit 3 without `--by`), with session only, and with nothing;
  - hand-written reviews with no key, with the taker's key, and with another agent's key;
  - a `revise` and `confirm` as one agent under two names, and as two agents under one name;
  - claims across two agents with one typed name.

  `vsect check` on the clone afterwards was structurally clean. No events were written to the real asf store.

## Not verified

- **Workflow workers.** No Workflow was run: they need a check with Joseph first, and the brief asked me to ask before testing one. The hook's `wf=` lookup matches the on-disk layout of 154 surveyed Workflow-worker meta files. No worker's Bash call has been seen carrying `CC_AGENT`, and a worker's parent is left empty, because its meta file names none.
- **Two PreToolUse hooks that both rewrite a Bash command:** how Claude Code combines them is unknown. None other is installed.
- **What a person sees in the interactive TUI.** Transcripts show the command without the prefix. Whether a permission prompt shows it was not checked, because `-p` runs have no prompts.
- **Whether `--resume` or a compaction keeps the session id.** `/clear` changes it, per Claude Code's `env-vars.md`.
- **Real interactive auto-mode sessions.** The measurements used `-p` with haiku as the session model.
- **Wall time per Bash call.** The Python start costs about 16 ms (ten runs); end-to-end wall time was not measured.
- **Forgery.** An agent can `export CC_AGENT=…` itself, and its value wins. This guards against honest mistakes only, as everything vsect records does. Codex, Gemini and other harnesses get nothing; their acts stay `declared`.

## How a future agent re-tests it

```sh
~/src/agent-core/claude-code/agent-identity/test-agent-identity          # the install, a few minutes of haiku
~/src/agent-core/claude-code/agent-identity/test-agent-identity --repo   # the source, without relying on the install
vsect whoami                                                             # what vsect sees in your own shell
cargo test --release                                                     # in ~/src/arch/firmatum/utils/vsect
```

Re-run it after a Claude Code upgrade, and before trusting anything listed under *Not verified*. If auto mode starts denying plain commands, or a refusal names `CC_AGENT`, this hook is the first suspect; the README says how to remove it in four steps. One auto-mode denial in a run is a reason to rerun the larger comparison (the README has the commands' shape), not proof.

## Noticed alongside

- **asf's agent orientation still says `--by <you>`.** `doc/sop/agents.sop.md` (which `CLAUDE.md` links to) shows it in its `vsect take` and `vsect claim` examples. They still work, since `--by` is now a label, but they teach typing a name the record no longer needs. That file is the lead's to change; I left it.
- **The design write-up's wrong claim.** Its permission claim is replaced in place in `agent-id-detection.md`, with the measurements, rather than kept with a correction note. Its on-disk findings were re-confirmed by the test and are unchanged.
- **`vsect confirm --dry-run`** prints `→ recorded: equivalent`, and the old binary does too. Nothing was written, but the wording says otherwise. It is a small honesty defect in the tool's output, not touched here.
- **A Claude Code feature request** would remove the need for the prefix and its permission side effects: export the agent id into Bash, which the 2026-11-02 review also suggested. Joseph encourages `/feedback` drafts. I could not draft one from this subagent.
