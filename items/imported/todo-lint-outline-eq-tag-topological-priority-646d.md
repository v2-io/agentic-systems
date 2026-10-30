---
kind: item
provenance: imported
source: TODO.md:262
section: TODO — Miscellaneous & details › Editorial hygiene (standing items)
owner: ""
opened: 2026-10-30T20:17:41Z
opened-by: Claude Fable 5.1
---

# lint-outline eq-tag topological-priority (low priority, tooling). `bin/lint-outline` already checks "undeclared dependencies" (a `#slug` in body must be in `dep

Imported verbatim (relative links rebased) from `TODO.md` line 262, section *TODO — Miscellaneous & details › Editorial hygiene (standing items)*. Not yet re-checked against HEAD: `vsect recheck item:todo-lint-outline-eq-tag-topological-priority-646d --outcome holds|stale|landed|not-an-item --why …`.

- **lint-outline eq-tag topological-priority (low priority, tooling).** `bin/lint-outline` already checks "undeclared dependencies" (a `#slug` in body must be in `depends:`). Open question (gem-hunt 472913 GEM 6, deferred): does it also verify that eq-tag-cited sources (`*[Derived (… from #X …)]*`) are topologically *prior*, not merely present in `depends:`? If not, a small rule extension closes the forward-derivation-accretion class mechanically. Verify-then-extend; the motivating instance (F2) is already resolved by relocation, so this is general hygiene, not urgent.
