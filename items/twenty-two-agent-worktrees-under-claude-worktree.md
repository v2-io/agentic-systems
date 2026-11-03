---
kind: item
owner: I.1
opened: 2026-11-03T01:55:18Z
opened-by: Claude Opus 5.5 (lead, 2026-11-02 session)
---

# Twenty-two agent worktrees under .claude/worktrees/ and their branches remain from the 2026-10-30 sprint. Checked by patch (git cherry -v main <branch>) on 2026-11-02: every commit they hold is on main except (a) 3f519917, owed to main (the I.9 item on it), and (b) b2a0abad and a1f7332c on worktree-agent-aa3da304f606428e9, the I.10 commits rebuilt on main as 16c90ad9 and c1588665 without data/sample-2026-10-30-places.tsv. b2a0abad still carries that file (file paths in private repos); it is not on origin, so removing the branch and pruning is what keeps it out. worktree-agent-a6f35eff1ab6cd9c4 is locked by agent pid 83096, which is gone. Also local branches tmp-new, guc-rename-2026-05-09, auto: check before deleting. Remove after (a) lands; git worktree remove, then git branch -D, then confirm with git worktree list.

stale worktrees hold one unmerged commit and one private-paths file, and make every branch listing noisy
