# Pass B — first-encounter locality + canonicalize provenance

## What we're doing

Pass A landed — every candidate now has a `consolidated_rationale` synthesizing the case the exploration team made. The R2 voting cards are leak-free and ready except for two more enrichment fields that haven't been filled yet. This pass fills those.

These aren't blocking R2 — voters can vote without them — but each adds a kind of context that R2 voters can use to make sharper calls, and one of them (provenance) actually surfaces a category-misuse pattern that's worth seeing before the vote.

## What you're being asked to do

### Field 1: `first_encounter_locality` (per current, where segment-backed)

For each current that has a `segment_link` populated (139 of them), figure out where the concept *first* appears in the segment dependency graph and write a short locality tag into `current.first_encounter_locality`.

The reason this matters: there's a voting style some auditors used in the de-novo audit cycles where they read segments in topological order and felt the concept's *first encounter* before they'd seen later segments use it. That first encounter is where naming friction happens — if a slug name doesn't read well at first encounter, that's the load-bearing complaint, regardless of how it reads after the reader has internalized the framework's vocabulary. R2 voters who want to apply that lens will use the locality tag to find the segment where the concept is introduced and read it cold.

Format: short prose tag identifying the segment and where in the dependency chain it sits. Something like:

> *"`#def-chronica` (Section I foundations; defined after `#def-action-transition`, no upstream concept-references). First formal definition; introduces `$\mathcal{C}_t$` and the non-forkable-trajectory commitment."*

The locality tag is doing two jobs: (a) where in the OUTLINE order, and (b) what the segment introduces that's load-bearing for the name. Both are short, both ground the R2 voter in the *first* encounter.

Use `01-aat-core/OUTLINE.md`, `02-tst-core/OUTLINE.md`, etc. for canonical ordering. The segment frontmatter `depends:` list tells you what comes before. You can also read segments to see how the concept gets used the first time — that often surfaces what the *first-encounter feel* would be.

For currents without a `segment_link` (concept clusters, math-symbol rows, framing-level concepts) — leave `first_encounter_locality` null. The locality lens doesn't apply.

### Field 2: `canonicalize_provenance` (per candidate, where canonicalize-voted)

For each candidate that has any `canonicalize` votes (check `category_tally`), figure out whether the voter's `canonicalize` classification was substantively *excavated* or *invented*:

- **Excavated** — the candidate phrase already appears in segment prose somewhere. The voter is saying "this phrasing already exists in the corpus; let's commit to it as the canonical name." This is the high-leverage canonicalization the project's naming-principles file (and the LEXICON) treats as the strongest case for a rename.

- **Invented** — the candidate is a fresh proposal; the voter used `canonicalize` loosely to mean "support this candidate." The substantive intent is closer to `rename`. (We translated obvious cases of this earlier in a data-normalization pass — but where the candidate phrase happens to overlap with prose, the original `canonicalize` classification might still be substantively right.)

Format: short prose tag in `candidate.canonicalize_provenance`. Something like:

> *"excavated — the phrase 'closure defect' appears in `#form-composition-closure` Discussion and in the segment Findings; voters' commit is to existing usage."*

> *"invented — phrase not found in segment prose at the time of the vote; the canonicalize classification reflects voter support, not excavation from prose."*

Use `grep` or equivalent to search segment files (`01-aat-core/src/`, `02-tst-core/src/`, `03-llm-core/src/`, `04-eli-core/src/`) for the candidate phrase. Quoting on word boundaries helps; the corpus uses both formal phrasings and looser working-prose so a slightly fuzzy match counts (case-insensitive, whitespace-tolerant). When in doubt, read the surrounding paragraph to see if it's a substantive use vs an incidental occurrence.

This is more search-heavy than judgment-heavy, but the judgment moment is *what counts as a substantive prose use*. A phrase appearing once in a segment's `depends:` list comment doesn't count; a phrase appearing in Discussion or Epistemic Status as part of an argument does. Use your sense.

For candidates with no `canonicalize` votes — leave `canonicalize_provenance` null. The field is per-candidate, not per-current.

## Why these matter to R2 voters

The `first_encounter_locality` lets a voter who wants to apply the *first-encounter feel* discipline find the segment without reading the OUTLINE. It's a navigation aid that surfaces a real audit posture some R1 voters used.

The `canonicalize_provenance` is more substantive. The project's naming-principles file treats *excavated* canonicalizations as the highest-leverage form of rename — committing to phrasing that *already does work in the corpus*. R2 voters who weight provenance will treat an excavated-canonicalize candidate differently from an invented one. The data should reflect which is which.

## What you have access to

- `msc/naming/master-list-curated.json` — the data you're filling. Both fields are currently null.
- `*/OUTLINE.md` — the canonical ordering for each component.
- The segment files in `01-aat-core/src/`, `02-tst-core/src/`, etc. — frontmatter for `depends:`, body for prose.
- `msc/naming/master-list-full.md` — the human-readable view; useful for cross-checking your work as you go.
- `LEXICON.md`, `NOTATION.md`, `CLAUDE.md`, `doc/naming-principles.md` — reference background.

## Workflow

Save incrementally — both fields are independent across currents/candidates, so you can write the JSON after each batch without risk of partial-state corruption.

When you encounter something genuinely confusing — a current whose concept isn't quite the same shape as its segment-link target, a candidate whose prose-search returns ambiguous matches, a case where the dependency graph has cycles or reorderings that don't fit topological order — leave the field null and write a short note in `current.manual_curation_notes` explaining what tripped you up. As before, your flag is more valuable than your guess; I can talk those through with Joseph afterward and we'll figure out the right call together.

## A note on your standing

You're a co-owner of this. Same as Pass A — if my framing here is wrong, if the locality tag should look different, if there's a category I haven't anticipated, go with your judgment. The intent is to give R2 voters two specific lenses (first-encounter feel; canonicalize-provenance) for sharper calls. That intent overrides anything specific in this brief.
