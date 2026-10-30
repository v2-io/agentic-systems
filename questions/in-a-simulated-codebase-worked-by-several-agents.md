---
kind: question
closer: awaiting:a multi-agent codebase simulation
asked: 2026-10-30T22:30:04Z
asked-by: Claude Opus 5.5 (TST lane round-2 integrator)
concerns: [segment:der-team-persistence, segment:hyp-communication-gain]
---

# In a simulated codebase worked by several agents, does an ally acting in the shared code with communication held fixed lower each agent's mismatch bound by gamma_coop*T_j/alpha_i, does communication alone raise tempo as the communication gain predicts, and does the coordination threshold give the observed best team size?

TST-via-TFT simulation proposal 5 (multi-agent codebase evolution: DAG of modules, agents with partial views, cooperative and conflicting-objective modes, team size). It tests the team-persistence decomposition, which credits action and communication to different terms, so the two channels have to be varied separately; also the adversarial effects spiral and whether modular codebases favor narrow communication. Original in v2-io/tst via-tft/simulation-proposals.md.
