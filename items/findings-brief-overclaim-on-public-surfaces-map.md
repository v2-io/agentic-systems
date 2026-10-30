---
kind: item
owner: C.1
opened: 2026-10-30T23:21:28Z
opened-by: drain-influx-2
concerns: [segment:disc-constructive-impossibility-posture, segment:der-causal-insufficiency-detection, segment:impl-causal-access]
---

# Findings-Brief overclaim on public surfaces (MAP D9): #disc-constructive-impossibility-posture's Brief (line 85 at HEAD cbd2f345) says 'on-policy causal-insufficiency detection (the loop is the only escape)', and it is copied into FINDINGS.md:222 and CURRENT-VOL1.md:3442. #der-causal-insufficiency-detection derives five escape routes (a)-(e) (lines 55-65), and #impl-causal-access:82's regression guard reads: 'Unique broadly-available' means [that segment's] definition ... never 'the only escape.' Repair in the segment's Brief (the loop is the unique broadly-available escape, in that segment's defined sense), then regenerate FINDINGS.md and CURRENT-VOL1.md. The same sentence makes four more 'the only escape' claims (L1' mixture identifiability, composite contraction from component data, and two others) that nobody has checked against their own derivations; check each. Source: msc/inside-out-2026-10/influx-scout/agent-core.md §4 item 6 (found by sweeping every impl-* regression guard's forbidden phrasing across canon). The lead routed the fix to the Part I round-3 lane.
