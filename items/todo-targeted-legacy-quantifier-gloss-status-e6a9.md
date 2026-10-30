---
kind: item
provenance: imported
source: TODO.md:499
section: 'TODO — Miscellaneous & details › 2026-07-03 — Audit 731548 (Fable de-novo, Part I + impl-*) routing: remaining routed items'
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
rechecked: 2026-10-30T21:30:48Z by Claude Opus 5.5 (item rechecker, t2-todo)
owner: C.1
---

# Targeted-legacy quantifier/gloss/status-tag sweep (FINAL §F, Tier-3 #7). Grep result/discussion segments for `iff` / `only if` / `necessary` / `exactly` / `redu

Imported verbatim (relative links rebased) from `TODO.md` line 499, section *TODO — Miscellaneous & details › 2026-07-03 — Audit 731548 (Fable de-novo, Part I + impl-) routing: remaining routed items*. Not yet re-checked against HEAD: `vsect recheck item:todo-targeted-legacy-quantifier-gloss-status-e6a9 --outcome holds|stale|landed|not-an-item --why …`.

- [ ] **Targeted-legacy quantifier/gloss/status-tag sweep** (FINAL §F, Tier-3 #7). Grep result/discussion segments for `iff` / `only if` / `necessary` / `exactly` / `reducible` / `unique broadly-available` / `for free` / `structural, not` and attack each against the math it summarizes. Prioritize the *oldest, least-recently-reworked* prose — the audit's post-report spot-check verified the defects are legacy escapees (TFT-inherited language), not a systemic gap; recently-reworked segments pass impeccably. B-1/B-2 were both this species.

Also raised in (2026-10-30, audits drain): `audits/AUDIT-WORKING-731548/` reflections 19-25, the segments the September aux reports did not reach; instances still live at HEAD `dc2b262c`: (a) `#def-adaptive-tempo:13` calls tempo "the effective rate at which an agent acquires useful information", while its units are corrections per time and `:44` itself says "total corrective capacity"; the information rate is $\dot R$ in `#deriv-persistence-cost` (731548/23). (b) `#def-mismatch-signal:21` and `:65` normalize the innovation by the observation-noise covariance alone, although the segment now names $\delta_t$ the innovation, whose covariance is $U_M + U_o$ (the normalizer `#emp-update-gain` and the standard NIS test use); as written $\mathbb E\lVert\delta\rVert_\Sigma^2 \gt n$, so the "surprise-equivalent units" gloss is off (731548/19, ledger xlvii). (c) `#def-causal-information-yield`: CIY $=0$ for a passive observer is a convention (no comparator distribution when $\lvert\mathcal A\rvert\lt2$), and the policy-induced default makes CIY habit-relative; both are answered only in Working-Note gold (:76, :82), not in the body (731548/22). Reflections 01-18 bear on segments the aux reports re-audited; those items are carried by the influx drain via `msc/inside-out-2026-10/influx-scout/rewrites-aux-canon-check.md`.
