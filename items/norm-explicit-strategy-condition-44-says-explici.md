---
kind: item
owner: C.1
opened: 2026-10-30T21:23:58Z
opened-by: Claude Opus 5.5 (item rechecker, t2-todo)
concerns: [segment:norm-explicit-strategy-condition, segment:der-loop-interventional-access]
---

# norm-explicit-strategy-condition:44 says 'explicit Sigma_t inherits the biases of M_t; loop-based learning does not' (audit 526815 F35). Canon now says otherwise: der-loop-interventional-access:41 states that on-policy loop data converges to the conditional, not the interventional effect, whenever (C2) fails, and a policy deterministic in its decision state fails (C1). Loop learning inherits selection and confounding bias; the line survived B.1's edit of this segment today.

Split out of TODO.md:497 (item todo-source-segment-defects-reported-by-the-b-6d26, 2026-08-22) by the t2 re-check; checked present at HEAD c772a6cf+.
