---
kind: item
owner: C.1
opened: 2026-10-31T02:14:56Z
opened-by: drain-wn-01-gold-opus-5.5
concerns: [segment:def-chronica, segment:scope-agent-identity]
---

# #def-chronica:16 and :36 say 'Duplicating an agent's state and letting both copies run on ... produces two agents with divergent chronicae'. The non-forkable object is the trajectory, not the state M_t (which, being a lossy compression, is copyable), and not the chronica as a stored record (also copyable). #scope-agent-identity:15-40 indexes sufficiency to 'this agent's chronica' and its clone discussion ('copying LLM weights gives same M_t, same causal history') runs the record and the trajectory together. Proposed: name the causal-trajectory token separately from the record (526815/742613 suggest a symbol such as gamma_t), index sufficiency and non-forkability to the token, and say the record is the copyable artifact along it. Also from the same gold: whether simultaneous observations are serialized or o_t is a vector, and the missing a_0 before o_1 (#def-chronica WN line 88, Gemini 829314; Claude 451729). The 'no generally optimal merge' claim (#scope-agent-identity:31) depends on the optimality criterion (526815/742613, its WN line 93). Checked at HEAD 4175aae7. Sources: #def-chronica gold Follow-ups (WN lines 85, 88); #scope-agent-identity gold Follow-ups (WN lines 92, 93).
