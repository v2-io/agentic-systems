---
kind: item
owner: C.4
opened: 2026-10-31T02:15:12Z
opened-by: drain-wn-01-gold-opus-5.5
concerns: [segment:der-deliberation-cost, segment:der-action-selection]
---

# Deliberation's formal benefit is improvement in update gain, but the prose, the examples and the fluency definition are about action quality (checked at HEAD 4175aae7). #der-deliberation-cost:15 says explicit deliberation 'can improve action quality by using the model for internal simulation'. Its formal benefit term (line 39) is Delta eta* (update gain), and its examples (MCTS, MPC, war-gaming, reading code before editing) improve action selection. #der-action-selection:17 defines action fluency through Delta eta*(Delta tau) ~ 0. The Epistemic Status names the gap, so the segment is honest, but it is cited as a general thinking-versus-acting threshold. Strengthen first: derive the action-value benefit channel, so the threshold covers planning. Failing that, call the result an epistemic (gain-improving) deliberation threshold where it is cited. The same gold asks that the counterfactual baseline in 'Net = Delta eta* ||delta_post|| - rho_delib Delta tau' be made explicit (471203). Sources: gold Follow-ups of #der-deliberation-cost (WN lines 120-121; 526815, 742613) and #der-action-selection (WN line 91).
