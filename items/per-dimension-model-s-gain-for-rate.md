---
kind: item
owner: C.1
opened: 2026-10-31T02:16:39Z
opened-by: Claude Opus 5.5 (audits drain)
concerns: [segment:result-persistence-condition, segment:result-per-dimension-persistence]
---

# #result-persistence-condition:81 states the per-dimension Model S condition as eta_k > c rho_k^2 / delta_critical,k^2, with eta_k (an update gain, dimensionless per event) where every surrounding persistence statement compares a correction rate (T_k or alpha, units 1/time) against rho. Either eta_k here is a per-dimension rate and needs renaming, or the inequality mixes units. Checked present at HEAD dc2b262c; #result-per-dimension-persistence is the home to reconcile against. Source: audits/AUDIT-WORKING-526815/00-running-outline.md F15 (2026-05-15). The Part I lane edits this segment today, so it may fold this in.
