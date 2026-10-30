---
kind: item
owner: F.4
opened: 2026-10-30T23:22:17Z
opened-by: drain-influx-2
concerns: [segment:deriv-update-detection-latency, segment:def-mood, segment:deriv-edge-update-natural-parameter, segment:schema-strategy-persistence]
---

# lambda names at least five objects in canon, and one derivation uses two of them. #deriv-update-detection-latency uses lambda as the edge log-odds coordinate (lines 29-43: Delta lambda_detect, lambda_k^new) and as the forgetting retention factor (lines 63-88: n_eff = 1/(1-lambda)) in the same derivation (re-read at HEAD cbd2f345). Across canon: mood integration rate (#def-mood, #der-mood-timescale), retention factor (#schema-strategy-persistence, #form-consolidation-dynamics, #deriv-update-detection-latency), log-odds natural parameter (#deriv-edge-update-natural-parameter; lambda_k in #der-interaction-channel-classification, #disc-credit-assignment-boundary), generalized eigenvalue (#deriv-matrix-persistence-condition), lambda_surv (#disc-anti-collapse), lambda_ij (#def-strategic-tempo), exploration weight (#def-causal-information-yield). NOTATION.md lists only the last (line 116). The retention use matches recursive least squares' forgetting-factor convention (canon already cites Ljung at #schema-strategy-persistence), so the mood rate and the log-odds coordinate are the likelier renames. Any derivation that composes mood with the forgetting machinery should be rechecked after the rename. Sources: agent-core memory corpus (research/asf_bridge.md; msc/15 reading note), relayed in msc/inside-out-2026-10/influx-scout/agent-core-memory.md B1 and agent-core.md §4 item 7.
