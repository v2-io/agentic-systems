---
kind: item
owner: C.1
opened: 2026-10-30T23:24:42Z
opened-by: drain-influx-2
concerns: [segment:form-structural-change-as-parametric-limit, segment:def-strategy-dag]
---

# #form-structural-change-as-parametric-limit's operations table (line 31, HEAD cbd2f345) defines 'Objective revision | Change terminal nodes', but #def-strategy-dag puts the terminal satisfaction conditions inside Sigma_t and relates them to O_t only through O_t-well-formedness (lines 62-68: a constraint on the relationship, not the same object). So the table conflates two operations: revising the terminal conditions of Sigma_t while O_t stands (a re-plan of what counts as done) and revising O_t itself. Split the row, or state that the row means the second and the first is a structural Sigma_t edit. A source tag (principal vs agent) was also proposed; settle first whether the table lists the agent's own operations, in which case a principal's correction of a mis-sent instruction is an M_t observation, not an operation, which is the de novo review's objection to the motivating instance. Sources: ~/src/agent-core/tools/asf-transcribe/feedback-and-proposals.md §2.1 and §3.6, contested in de-novo-review-1.md §5 (both 2026-10-07); relayed in influx-scout/agent-core.md §2.C, P8.
