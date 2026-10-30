---
kind: item
provenance: imported
source: TODO.md:152
section: TODO — Miscellaneous & details › Open theory items (MEDIUM)
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
concerns: [segment:form-composition-closure]
rechecked: 2026-10-30T21:16:11Z by Claude Opus 5.5 (item rechecker, t1-todo)
owner: B.1
restated: 'Most of this landed and the tracker never caught up. (A1)-(A4), (P1)-(P3), the macro-step bridge lemma (discrete time, contraction factor lambda_eff) and the two-Kalman toy are in #form-composition-closure. No canon segment cites the workshop any more; the G2 relink (9099e588) cleared those citations. The workshop''s ''bridge lemma falls out of the sector condition for free'' (its §7) was overtaken on 2026-04-06: canon proves the bridge needs the strictly stronger incremental sector bound (DA2''a-inc), with a witness. What is genuinely open: a toy composite of purposeful agents with strategy DAGs and a shared objective that exercises (A1)''s G_c (the Beta-Bernoulli single-edge case does not, and its ''grows without bound'' line is wrong: reviews/items-recheck-t1.md C1); a norm choice for non-estimation domains; principled eps_I. Owner B.1 because the toy is the true-instance a Part III record for (A1) needs.'
---

# 🌟 Composition admissibility ($\mathcal M_{\text{adm}}$) refactor — HIGH priority. Section III's most load-bearing open problem. `msc/working-composition-admissi

Imported verbatim (relative links rebased) from `TODO.md` line 152, section *TODO — Miscellaneous & details › Open theory items (MEDIUM)*. Not yet re-checked against HEAD: `vsect recheck item:todo-composition-admissibility-mathcal-m-text-10c4 --outcome holds|stale|landed|not-an-item --why …`.

- **🌟 Composition admissibility ($\mathcal M_{\text{adm}}$) refactor — HIGH priority.** Section III's most load-bearing open problem. `msc/working-composition-admissibility.md` (473 lines, 2026-04-01) is an active workshop document carrying substantive worked content: the structural+stability direction with (A1)–(A4) framework; the bridge lemma "falls out of the sector condition for free" insight (one Lyapunov argument applied to two state variables, not two theorems); composite sector condition derivation cross-checked against team-persistence; toy two-linear-agent verification. The document is **load-bearing** — cited from `#form-composition-closure` and three spikes — but is explicitly a workshop, not a promoted artifact. **Work:** (a) decompose into proper spike files (candidates: `spike-composition-admissibility-structural-stability.md`; `spike-bridge-lemma-discrete-time-adaptation.md` for the discrete-time adaptation; `spike-composition-toy-purposeful-agents.md` for the richer Section II setting that exercises the $G_c$ axis); (b) promote stable findings into segments — most of §4–§6 is candidate Appendix-A material under or adjacent to `#form-composition-closure`; (c) update all references project-wide to point at the new spike files / segments rather than the workshop document; (d) follow-on spikes the workshop itself surfaced as genuinely open: discrete-time bridge lemma adaptation; richer purposeful-agent toy case exercising the $G_c$ component; projection admissibility ($\mathcal P_{\text{adm}}$, untouched in the workshop); norm-choice load-bearingness in real applications.
