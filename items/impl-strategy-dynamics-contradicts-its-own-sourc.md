---
kind: item
owner: C.1
opened: 2026-10-30T23:21:28Z
opened-by: drain-influx-2
concerns: [segment:impl-strategy-dynamics, segment:der-causal-insufficiency-detection, segment:impl-strategy-structure]
---

# #impl-strategy-dynamics contradicts its own source and a sibling guard (MAP D8). (1) Line 42 calls (S1)-(S5) 'five boundary routes' and gives them route content ('(S1) joint sibling observability under exploration, (S2) instrumental variation, ...'). In #der-causal-insufficiency-detection (S1)-(S5) are the no-go's scope conditions (lines 35-41: '(S1) Pure on-policy execution' ... '(S5) No structural priors') and the escape routes are (a)-(e) (lines 55-65), mapped (a)->(S1), (b)->(S3), (c)->(S3) finer, (d)->(S5), (e)->(S4); 'instrumental variation' and 'cross-episode covariance under structural breaks' are not routes there at all. (2) Line 44 ends 'with #der-loop-interventional-access as the shared escape mechanism' for Instances 1 and 2; #impl-strategy-structure:72 regression guard (2) says 'Instance 1 and Instance 2 do not share an escape; ... the shared content is rank augmentation', and #impl-strategy-structure:57 says the same. Rewrite line 42 from the derivation's table and line 44 to the rank-augmentation form. Source: agent-core strategy-dag-engineering note §8 (2026-10-07), relayed in msc/inside-out-2026-10/influx-scout/agent-core.md §4 items 1-2; both re-read at HEAD cbd2f345.
