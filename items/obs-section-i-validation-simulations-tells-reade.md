---
kind: item
owner: F.3
opened: 2026-10-31T02:16:13Z
opened-by: drain-influx-2-asffixes-r34-55
concerns: [segment:obs-section-i-validation-simulations]
---

# #obs-section-i-validation-simulations tells readers its evidence is unavailable when it is in the tree. At HEAD d058c25e the body says the simulation suite 'is maintained as the project's reproducibility supplement and will be released as a citable code artifact at publication' (:52) and repeats it in the Epistemic Status ('maintained as a reproducibility supplement to be released as a citable code artifact at publication', :84), and the segment never cites the suite's location. Since 1d65587a the suite is registered as empirica/track-b-nonlinear (MANIFEST.md, RUNS.md, 00-simulation-spec.md, sim1_*/sim2_* drivers and results, variants/), and empirica/INDEX.md lists this segment among the experiment's consumers; sibling consumers already point at it (e.g. #result-per-dimension-persistence:134 cites ../../empirica/track-b-nonlinear/variants/variant_ef_extensions.py). Fix: cite empirica:track-b-nonlinear (and the per-variant result files the tables rest on) in place of the release promise, keeping 'citable artifact at publication' only if a separate archival release is genuinely planned. Why it matters: an outside reader takes the canon sentence at its word; the AISI sweep-2 agent R41 relayed it as 'the 72% figure is currently unverifiable by an outside reader against source' (~/src/AISI-responses/influx/sweep-2-raw/report-41.md §3; ASF-FIXES-part3.md R41).
