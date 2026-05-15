# Refined Round 1 — Agent Launch Prompt

This is the kickoff prompt for spawning agents into the refined-Round-1 (cold-start) naming review for the Agentic Systems Framework. The canonical instructions live in [`doc/naming-principles.md`](../../doc/naming-principles.md); this file is a thin wrapper that fronts the cold-start clause, sets identity / output destination, and points each agent at the principles file.

Joseph launches Codex + Gemini agents externally (likely via web UI or another harness); Claude variants (Opus / Sonnet / Haiku) are launched from this session via the `Agent` tool. Use the prompt below verbatim for each — substitute only the `{your-agent-id}` field.

---

## Prompt (paste verbatim into each agent)

You are participating in a multi-agent naming review for the **Agentic Systems Framework (ASF)**. This is the *refined Round 1* of a multi-round naming-cycle. Your job is to vote on subject-noun renames, keeps, canonicalizations, aliases, and unnamed-thing namings, following [`doc/naming-principles.md`](doc/naming-principles.md) as your canonical instruction set.

### COLD-START INSTRUCTION — read first, before anything else

Do not read any of these files (or their contents via grep / find / cat / etc.) before voting. They would anchor your thinking and collapse the diversity this audit depends on:

- `msc/naming/naming-votes/*` — other agents' votes (Round 1 originals + any peer r2 files in flight)
- `msc/naming/naming-brainstorm-*.md` — Round 1 brainstorm
- `msc/naming/naming-aggregate-*` — Round 1 aggregations / consolidated review
- `msc/naming/naming-alias-*.md`, `msc/naming/naming-cleanup-*.md` — alias clusters / cleanup scans
- `msc/naming/naming-pilot-rename-plan.md` — landed-and-pending rename mappings (would directly anchor your votes)
- `msc/naming/_archive/*` — archived prior-round artifacts

The rule fires *first* — before `CLAUDE.md`, `TODO.md`, `OUTLINE.md`, `FORMAT.md`, segment files, or anything else. Earlier rounds discovered that even glancing at a `git status` showing one of those files disclosed enough to anchor an agent's votes.

If you've already read any of the excluded files in this session — including in any prior turn before this prompt — disclose it explicitly in your principles-observations section at the end. The contribution is still useful as long as it is marked.

### Your identity and output destination

Use a clear agent ID that identifies your model. Suggested form: `{model-name}-r2[-{variant}].md`. Examples:

- `opus-4-7-r2.md`
- `sonnet-4-6-r2.md`
- `haiku-4-5-r2.md`
- `gemini-2-5-pro-r2.md` (or `gemini-2-5-pro-r2-a.md` / `-b.md` if multiple instances of the same model)
- `codex-gpt-5-r2.md`

The `r2` suffix marks this as the refined-Round-1 contribution (distinct from the Round 1 originals already in the directory).

Write your votes to `msc/naming/naming-votes/{your-agent-id}.md` (create the file).

### Now read your canonical instructions

Read [`doc/naming-principles.md`](doc/naming-principles.md) end-to-end. It contains:

- The full cold-start instruction (consistent with the above; expanded with rationale)
- Architectural invariants you must work *within*, not against (role-prefix discipline, subject-noun-first, Greek-vocabulary commitment, separate passes for prefix vs. subject-noun)
- Source material to ground your votes in
- Why naming deserves a deliberate pass (the load-bearing argument)
- The five vote categories: `rename`, `keep`, `canonicalize`, `add-alias`, `name-unnamed`
- The eight evaluation criteria
- The naming-layer and eligible-category lists
- The weight scale (+3 / +2 / +1 / −1) — note +2 was added since Round 1 to break the +1/+3 collapse
- Table format and example votes (5 columns: current-name, new-name-candidate, category, weight, notes)
- Expected length: 60+ rows; under 20 means you haven't looked hard enough; approaching 200 means prioritize quality over count

Then ground your votes by reading the source material it names (`CLAUDE.md`, `TODO.md`, `OUTLINE.md`, `FORMAT.md`, `NOTATION.md`, `LEXICON.md`, `README.md`, `PROPOSALS.md`, segment files under `01-aat-core/src/`, `02-tst-core/src/`, `03-llm-core/src/`, `04-eli-core/src/`). Sample widely; do not just scan slugs.

### What "good" looks like for your output

- Header identifying your model + one-line summary of your approach
- The votes table (main content) — 60+ rows, every category represented where you have something to say, weights used deliberately (not all +3)
- Optional but encouraged: principles-observations section at the end naming any place the principles file felt under-specified, any criterion you used that isn't named there, and whether the cold-start instruction worked for you in practice

Vote *explicitly* for things you considered and chose to keep — absence is not a vote. The aggregation needs to distinguish "nobody thought about it" from "several agents looked and declined to change it."

Naming is irreducibly aesthetic; there is no derivation that settles it. Be confident where you are, honest where you are not, and let the multi-architecture aggregation do the convergence work.

---

## Notes for the launching human (not for the agent)

- **Agent slate this round:** 1× Codex, 2× Gemini (launched externally by Joseph); 1× Opus, 1× Sonnet, 1× Haiku (launched from the active session via the `Agent` tool). Total: 6 r2 votes.
- **Multi-architecture diversity is the point.** Same-architecture variants converge faster than cross-architecture; the round's epistemic value comes from the spread.
- **Don't paste the principles file inline** with the kickoff. The agent reads it directly so the file's structure (cold-start-first) is preserved as a reading discipline, not flattened into a brief.
- **If a Gemini run hits length limits** before reaching 60 rows, accept the partial — the principles file's lower-bound is a target, not a gate.
- **After all six land,** re-aggregate via `bin/naming-aggregate.rb` (it auto-detects the new `*-r2.md` files); then proceed to Round 2 (blind).
