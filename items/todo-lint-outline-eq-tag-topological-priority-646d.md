---
kind: item
provenance: imported
source: TODO.md:262
section: TODO — Miscellaneous & details › Editorial hygiene (standing items)
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
rechecked: 2026-10-30T21:53:23Z by Claude Opus 5.5 (item rechecker, t1-todo)
owner: I.4
restated: 'The premise is false: no tool checks that a #slug cited in a body is declared in depends: (grep of bin/ for an undeclared-dependency check finds none; lint-outline checks that declared deps exist and are ordered). Measured at HEAD: of 43 eq-tag citations of existing segments (*[Derived (... #X ...)]* and kin, Working Notes excluded), 3 are not in depends: #result-persistence-condition cites #deriv-sector-condition and #result-per-dimension-persistence; #disc-composition-consistency cites #result-contraction-template. This matters for I.4: vsect binds a check to the depends: chain, so a check on #result-persistence-condition would not lapse when #deriv-sector-condition changes. The fix is a check (an eq-tag source must be in depends:) run where vsect check runs, plus the three declarations.'
---

# lint-outline eq-tag topological-priority (low priority, tooling). `bin/lint-outline` already checks "undeclared dependencies" (a `#slug` in body must be in `dep

Imported verbatim (relative links rebased) from `TODO.md` line 262, section *TODO — Miscellaneous & details › Editorial hygiene (standing items)*. Not yet re-checked against HEAD: `vsect recheck item:todo-lint-outline-eq-tag-topological-priority-646d --outcome holds|stale|landed|not-an-item --why …`.

- **lint-outline eq-tag topological-priority (low priority, tooling).** `bin/lint-outline` already checks "undeclared dependencies" (a `#slug` in body must be in `depends:`). Open question (gem-hunt 472913 GEM 6, deferred): does it also verify that eq-tag-cited sources (`*[Derived (… from #X …)]*`) are topologically *prior*, not merely present in `depends:`? If not, a small rule extension closes the forward-derivation-accretion class mechanically. Verify-then-extend; the motivating instance (F2) is already resolved by relocation, so this is general hygiene, not urgent.
