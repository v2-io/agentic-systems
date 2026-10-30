# OUTLINE-accepted — accepted-by-design ordering violations (lint-outline whitelist)

This file is tool configuration for `bin/lint-outline`. Each row records one dependency-ordering violation in `OUTLINE.md` that is accepted *by design*, with its grounding. The tool still prints accepted violations (marked ✓) but exits green when only accepted ones remain; any ordering violation not listed here stays red and refuses the commit. Rows are keyed by the (segment, depends-on) slug pair, so they survive row moves; a row that no longer matches a violation is reported as stale, and should then be pruned.

To accept a new violation, add a row with the two slugs, the date, and the reason the placement is right. "It was already there" is not a reason. The format is the one `01-aat-core/OUTLINE-accepted.md` uses.

| segment | depends-on | accepted | reason |
| --- | --- | --- | --- |
| scope-eli | scope-moral-continuity | 2026-10-30 | The volume opens with the scope condition that names its object, as Volume 3's chapters open with theirs. `scope-eli` states the ELI by its constituents, which the next rows define, and neither constituent depends on it (checked 2026-10-30, objective I.2) |
| scope-eli | def-five-constitutive-factors | 2026-10-30 | Same placement: the scope's clause 3 ("all five constitutive factors present") cites the definition two rows below, which does not depend on it |
