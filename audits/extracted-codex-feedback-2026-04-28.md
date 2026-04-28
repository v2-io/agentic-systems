# Extracted Codex Feedback — 2026-04-28 (post-cleanup recheck)

**Source model:** OpenAI Codex
**Date:** 2026-04-28
**Session UUID:** `8bbf6820-fddc-441d-b568-ef532f7b1284`
**Record UUID:** `52ef195e-d437-4b1e-a740-9624e7b0aac9` (line 1058, ts `2026-04-28T18:24:11Z`)
**Topic:** Quick Codex re-check after the link-and-file-hygiene-findings cleanup pass. Three remaining stale-default / stale-path items in `bin/naming-aggregate.rb` and `msc/naming/naming-pilot-rename-plan.md`. Confirms `bin/build-readme --check` and `bin/lint-outline` pass; CHANGELOG.md/TODO.md/LEXICON/PRACTICA/FORMAT all corrected.

## Context

This was a targeted Codex re-check immediately after Joseph applied the link-and-file-hygiene cleanup pass (per the working file `audits/link-and-file-hygiene-findings.md`). The check confirms the pass landed cleanly except for three small remaining items related to the naming-vote tooling's default arguments and a pilot plan's stale prose about the rename-protection mechanism.

## Disposition

Pending — these three items are very minor stale defaults / stale prose, not theory issues. They sit in the project hygiene queue but don't appear to have been addressed yet (verifying would require a current `bin/naming-aggregate.rb` inspection, beyond the scope of this archaeological extraction).

## Verbatim feedback Joseph relayed

> Excellent work. Codex just did another quick check:
>
> • I rechecked the prior findings. Most of the attempted cleanup landed cleanly.
>
>   Remaining items I'd still fix:
>
>   1. `bin/naming-aggregate.rb:342` still defaults to the old vote directory:
>       - Current default: `msc/naming-votes`
>       - Current repo path: `msc/naming/naming-votes`
>       - Running `ruby bin/naming-aggregate.rb` now fails with `No vote files found in msc/naming-votes`.
>       - Running `ruby bin/naming-aggregate.rb --votes-dir=msc/naming/naming-votes --format=json` succeeds, so the parser itself is fine; the default/config/help text is stale.
>   2. `bin/naming-aggregate.rb:7` and `bin/naming-aggregate.rb:293` still refer Round 2 users to `msc/naming-principles.md`.
>       - Current path is `doc/naming-principles.md`.
>       - The generated Round 2 prompt does correctly write votes to `msc/naming/naming-votes/{your-agent-id}.md`, so only the principles path is stale there.
>   3. `msc/naming/naming-pilot-rename-plan.md:5` and `msc/naming/naming-pilot-rename-plan.md:97` still say the rename-protection mechanism is the old `msc/naming-*.md` exclusion glob.
>       - The actual current tool excludes the whole `msc/naming/` directory at `bin/rename-slug:65`.
>       - `bin/rename-slug:71` already documents that the directory move subsumed the older per-file globs.
>       - So this is just stale prose in the pilot plan, not a tool failure.
>
>   Everything else from the prior audit looks resolved or intentionally historical:
>
>   - `bin/build-readme --check` passes.
>   - `bin/lint-outline` is clean: no ordering violations, no orphan segments.
>   - The old broken CHANGELOG.md project/session links are no longer clickable broken links; they are plain code-styled historical labels now.
>   - The old TODO.md Archive references are gone from active navigation/instructions; the remaining matches are historical LOG.md/dated CHANGELOG.md prose.
>   - The stale role-prefix segment links I flagged no longer show up.
>   - LEXICON.md, PRACTICA.md, FORMAT.md, `03-logogenic-agents/OUTLINE.md`, and the audit instructions look corrected.
>   - A narrow generated-output/root-doc link and anchor pass found 0 active issues across the checked active docs; README partial false positives remain only if checked in raw partial context, which matches the tooling note already in TODO.
