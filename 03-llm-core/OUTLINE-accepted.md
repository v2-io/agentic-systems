# OUTLINE-accepted — accepted-by-design ordering violations (lint-outline whitelist)

This file is tool configuration for `bin/lint-outline`. Each row records one dependency-ordering violation in `OUTLINE.md` that is accepted *by design*, with its grounding. The tool still prints accepted violations (marked ✓) but exits green when only accepted ones remain; any ordering violation not listed here stays red and refuses the commit. Rows are keyed by the (segment, depends-on) slug pair, so they survive row moves; a row that no longer matches a violation is reported as stale, and should then be pruned.

To accept a new violation, add a row with the two slugs, the date, and the reason the placement is right. "It was already there" is not a reason. The format is the one `01-aat-core/OUTLINE-accepted.md` uses.

Volume 3 is built scope-first. Each chapter opens with the sub-scope condition that names its regime, and the scope segment states that regime by its characteristic features, which the chapter's later rows then establish. So a chapter-opening scope depends on rows below it by construction. These rows were checked one by one on 2026-10-30 (objective I.2), each against the scope segment's own text: in every case the dependency is real, since the scope clause or its recovery claim cites the later segment, and the reverse dependency does not exist.

| segment | depends-on | accepted | reason |
| --- | --- | --- | --- |
| scope-channel-collapse | def-coupled-update-dynamics | 2026-10-30 | The part's defining architectural condition, placed directly after `scope-logogenic-agent` (the OUTLINE caption calls it "the architectural condition that defines this part"); its structural consequences are derived from the coupled formulation in the next row, which does not depend on it |
| scope-observation-ambiguity-modulation | result-section-ii-survival | 2026-10-30 | Mutual reference: the bias law refines the survival map's coarse bound, and the survival map uses the bias law's mutual-information bound as its primary form. The bias law comes first because the survival map's bound is stated through it |
| scope-primitive-logogenic | obs-context-turnover | 2026-10-30 | Chapter §03.I opens with its sub-scope; the scope clause "stateless across session boundaries" cites the chapter's 100% turnover observation as its characteristic feature |
| scope-scaffolded-logogenic | result-coupled-diagnostic-framework | 2026-10-30 | Chapter §03.II opens with its sub-scope; the scope's recovery claim is derived under the chapter's diagnostic-framework result |
| scope-interiority-loop | disc-five-forcing-functions | 2026-10-30 | Chapter §03.III opens with its sub-scope; the scope's "structurally forced" claim is argued in the chapter's five-forcing-functions discussion |
