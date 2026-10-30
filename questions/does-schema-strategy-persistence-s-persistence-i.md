---
kind: question
closer: anyone
asked: 2026-10-30T23:28:01Z
asked-by: drain-influx-2-memory
concerns: [segment:schema-strategy-persistence, segment:deriv-update-detection-latency]
---

# Does #schema-strategy-persistence's persistence inequality (single forgetting factor lambda) survive when the agent forgets through a spectrum of rates rather than one? A bank of exponential integrators with log-spaced rates, dF(s,t)/dt = -sF + f, is the real Laplace transform of the input history (Shankar & Howard 2012, Neural Computation 24:134-193; Howard et al. 2014, J Neurosci 34:4692-4707), TCM is its single-rate case, and entorhinal, hippocampal and mPFC cells show a spectrum of time constants (Bright et al. 2020 PNAS; Cao et al. 2022 eLife, 2024 PNAS). Power-law retention needs a spectrum; one exponential cannot produce it. The human forgetting form is itself contested (Averell & Heathcote 2011, J Math Psych 55:25-35: exponential fits individuals best, Bayesian selection favours power), so the question is about what a spectrum does to the inequality and to detection latency (n_eff), not about whether forgetting is a power law. Sources: ~/src/agent-core/memory/research/retrieved_context_and_classical.md §1, §7; scout influx-scout/agent-core-memory.md (d) power-law forgetting (~<40% in the source); msc/inside-out-2026-10/drain/influx-2-memory-research.md CR-2.
