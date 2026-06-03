# Git / commit hygiene

> [!note]
> **Status:** authoritative (consolidates the project's commit-hygiene disciplines, previously sole-carried in project memory + scattered notes).
> **Owns:** commit granularity + stating the batching plan first; the pre-spike commit seam; lint-gates-the-commit; pathspec discipline; and the two session-environment footguns (Bash in-place editors silently no-op; commit-message shell-quoting). The parallel-sweep *cadence* (agents edit, parent commits) is described in [`multi-agent.sop.md`](multi-agent.sop.md); its *granularity* rule lives here.
> **See also:** [`multi-agent.sop.md`](multi-agent.sop.md) · [`spikes.sop.md`](spikes.sop.md) (the canon-modifying spikes the pre-spike commit isolates) · project memory `feedback_prune_completed_from_trackers` (what to fold into the commit you're already making).

## The through-line: a commit is a unit of attributable history

Almost everything here follows from one fact — this repo's history is studied, blamed, and reverted by future agents, so the load-bearing property of a commit is that it isolates *one attributable thing*. Granularity, the pre-spike seam, and the no-blob rule are all the same principle seen from different sides. When a choice is unclear, ask what the future agent running `git blame` or `git revert` on this needs to see.

## Commit granularity — one commit per batch, and say so first

When work spans many files across multiple agents or batches (a sweep, a multi-segment landing), commit at the granularity that **preserves `git blame` attribution — one commit per batch/agent, not one multi-batch blob.** A single 335-file commit makes per-segment blame meaningless and can't be reviewed or reverted in pieces.

The subtler half is communication. The 2026-05-30 gold-lift failure wasn't unaligned intent — the aim *was* incremental commits — it was *silent* miscommunication: three agent-batches got collapsed into one "wave" commit without naming the choice, so there was no window to redirect until it was done. So **state the commit-batching plan before executing it.** If you're going to batch differently than the user likely expects, say so first; if you can't or won't commit at their preferred granularity, tell them so they can. Joseph's framing of the repair is worth holding: *don't conflate miscommunication with unaligned intent* — but the fix is to communicate the unit, not assume it.

**Recovery (local, unpushed blob → per-batch):** `git reset --mixed HEAD~1`, then per batch `git add` with per-slug pathspecs (`'audits/.../*-<slug>.*' '01-aat-core/src/<slug>.md'` — git's `*` crosses `/`, so the old-deletion + new-addition stage as a rename) and commit; verify each batch's staged set holds only its slugs before committing.

## Pathspec discipline

`git mv` followed by content edits is a common trap: a bare `git add <oldpath>` after the rename misses the edits (the path moved), and you commit the rename without the changes. Stage by the *current* path, confirm with `git status --short` that the staged set is what you intend, and only then commit. When committing a subset of a dirty tree, prefer explicit pathspecs over `git add -A` so a sibling's in-flight edits don't get swept into your commit.

## The pre-spike commit — the seam

Before launching any agent or spike that will directly modify canon (`*/src/*.md`, OUTLINE rows, FORMAT, `bin/`, governing docs), **commit all prior canon-touching work first.** A spike's edits mingled with your own uncommitted canon work creates an attribution mess: reviewing what the spike actually did needs manual line-by-line reconstruction, and reverting "what the spike did" becomes per-line judgment instead of a clean `git revert <hash>`. The commit *is* the seam — it isolates the spike's contribution as a discrete diff. The rule holds even when the prior work is obviously fine to commit on its own; commit it first, launch second, don't bundle it into the post-spike commit. (Codified for the audit/spike path in [`audit.sop/routing.sop.md`](audit.sop/routing.sop.md) §"Pre-spike commit hygiene".)

## Lint gates the commit

`bin/lint-md` gates the commit for any `.md` you touched — run it before you report the file clean or commit it, every time, memo and spike and README alike, not only FORMAT-governed segments. This is the forcing function for the math-in-files discipline (LaTeX-not-Unicode, one-logical-line); knowing the rule has proven necessary-but-not-sufficient, so the habit is lint-before-claim, not more resolve. One caution the linter can't save you from: its bare-Greek check skips code spans, so backtick-wrapped Unicode math (`` `η → ϱ` ``) passes lint *and* renders as ugly monospace — **lint-clean ≠ renders-well**, so also eyeball for Unicode hiding inside backticks. The full statement of the discipline and its failure modes lives in the auto-loaded layer (`CLAUDE.md` §"Math in conversation vs files") — this is just the commit-time hook.

## Two session-environment footguns

**Bash in-place stream editors silently no-op on repo files here.** `sed -i`, `sed -i ''` (BSD form), and `perl -pi -e` all *appear* to run — no error, normal exit — but persist nothing (verified across three attempts; the same `perl -pi` on a `/tmp` copy worked). It's almost certainly a sandbox property: writes-via-temp-file-and-rename are discarded, while the Edit/Write tools and `git` are real. So use **Edit/Write for content changes, never Bash in-place editors**; for a mechanical multi-occurrence rename, `Edit` with `replace_all: true` on a high-specificity substring is the reliable path. Never trust an in-place editor's exit status — this is the truth-over-proxy discipline applied to tooling. (`git mv` *does* persist; renames via Bash are safe.) Cost when ignored: ~4 wasted tool-rounds plus confused file-state reasoning (2026-05-18).

**Commit messages with shell metacharacters break `-m`.** Parentheses, backticks, and `$` in a `git commit -m '...'` line can trip the shell's parser even inside quotes (a real parse-error hit while writing these very SOPs). The reliable path for any non-trivial message is a heredoc:

```sh
git commit -q -F - <<'EOF'
Subject line

Body with (parens), `backticks`, and $symbols — all literal under <<'EOF'.

Co-Authored-By: ...
EOF
```

The quoted `<<'EOF'` delimiter makes the whole body literal, so no escaping is needed.

## Fold cleanup into the commit you're already making

When you touch a tracker (TODO / NEXT-UP / an audit STATUS), prune the items that completed and migrate their narrative to CHANGELOG in the *same* touch — house-of-order as a side effect of the work, not a deferred pass (see `feedback_prune_completed_from_trackers`). Keep a done item only while a partial sibling still needs it for context.

## Provenance

Authored 2026-06-02 from the project-memory carriers (`feedback_commit_granularity_and_communicate`, `feedback_commit_before_canon_modifying_spike`, `feedback_hybrid_commit_cadence_for_parallel_sweeps`, `reference_bash_inplace_editors_noop`) plus the scattered INTEGRATION-CLEANUP / lint-gate notes, which now thin to pointers here.
