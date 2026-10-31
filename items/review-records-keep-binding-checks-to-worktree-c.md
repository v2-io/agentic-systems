---
kind: item
owner: I.4
opened: 2026-10-31T02:53:15Z
opened-by: Claude Opus 5.5 (TST lane checker 3)
concerns: [review:tst-lane-round-3-integration]
---

# Review records keep binding checks to worktree commits that no branch contains (tst-lane-round-2 at 2cd1ad0c, tst-lane-round-3 at 0bc90f7d, and the first lane before them), so each later checker annotates every item by hand. vsect take could refuse or warn on an at: that no branch contains, or integrators could take their records after rebasing onto main.

Raised by the third TST check (msc/inside-out-2026-10/c1-lanes/tst-check-3.md, Observations).
