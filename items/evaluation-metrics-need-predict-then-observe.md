---
kind: item
owner: E.1
opened: 2026-10-31T02:13:52Z
opened-by: Claude Opus 5.5 (audits drain)
concerns: [segment:obs-evaluation-metrics]
---

# #obs-evaluation-metrics treats the mismatch delta_t of a logogenic agent as measurable, but a language model's prediction is not legible unless the scaffold makes it commit to one before the observation arrives: predict, then observe, then update, as separate recorded steps. Without that ordering the 'prediction' read off afterwards is contaminated by the observation, and the gain and sycophancy (eta* to 1) / rigidity (eta* to 0) diagnostics in the segment cannot be computed. The segment should state the protocol as a precondition of its metrics. Bears directly on E.1, which estimates a processor gain on LLM families and needs exactly this ordering in its RUNS contract. Source: audits/AUDIT-WORKING-773921/106-obs-evaluation-metrics.md §8 (Gemini 2.5 Pro, 2026-05-28); working-dirs map §3.6.
