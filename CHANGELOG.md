# CHANGELOG

The forward-going record of substantive changes to the framework. Entries are ordered most-recent-first, dated, and grouped by theme within a date.

## How this file relates to LOG.md, TODO.md §Archive, and git

- **CHANGELOG.md** *(this file)* — substantive changes from 2026-04-24 onward. Cycle-shape narratives ("what changed about how the theory thinks", structural moves, conventions adopted) go here. Entry granularity is the day; commit hashes appear inline for traceability.
- **[LOG.md](LOG.md)** — archaeology of cycles through 2026-04-24. Frozen at that date. Read it when the *origin* of a current commitment matters: whether a "settled" item rests on derivation or on a cycle's working consensus, or how an audit finding's prior status should shape current routing.
- **[TODO.md §Archive](TODO.md)** — commit-and-finding granularity record of landed work, kept inside the active TODO.
- **Git** — primary source for "what changed in code/segments." Use `git log --follow` for slug-renamed segments.

The split between CHANGELOG and TODO §Archive is intentional: CHANGELOG carries the *narrative shape* (what conventions changed, what disciplines emerged, what the cycle was about); TODO §Archive carries the *checklist trail* (which findings closed, which commits did what). They overlap in scope but serve different reading needs.

---

## 2026-04-24

### Role-prefix discipline: pilot → tooling → sweep

Project-wide adoption of the slug convention `{type-prefix}-{subject-noun}`, where the type prefix derives mechanically from each segment's `type:` frontmatter. Three landed pieces:

- **Pilot** (commits `09ace17`, `f6b8ae4`, `0b9cd24`): seven slug changes across four type categories, including the 1:2 semantic split of `#scope-condition` into `#scope-adaptive-system` + `#scope-agency` (the old name described the segment's role rather than the class it defined; downstream segments depend on one or the other, not on an abstract compound). Subject-noun-first slug naming validated as architectural invariant. Pilot-validation observations folded into the principles-file rewrite.
- **Tooling** (commits `981b291`, `3aa9e74`): `bin/align-slug` introduced as a one-segment wrapper over `bin/rename-slug`. Reads `type:` from frontmatter, computes the correct target slug under the project-wide `TYPE_TO_PREFIX` mapping, and invokes the mechanical rename only when not already aligned. `--all` for repo sweeps.
- **Full sweep** (commits `e6adf9e`, `f8bc46a`): `TYPE_TO_PREFIX` expanded from 1 entry to 14, collapsing FORMAT.md type tokens to compact natural-English forms (`postulate → post`, `definition → def`, `derivation → deriv`, etc.) so an `ls` of `src/` surfaces the kind-of-thing at a glance. Trailing-`-{type}` strip added: subject-nouns shouldn't carry the type word once the role-prefix lives in front (`bias-bound-derivation` → `deriv-bias-bound`). Sweep applied across 142 active segments; `01-aad-core/OUTLINE.md` lint-clean throughout.

Bug caught and fixed mid-arc: an early `bare_subject` used the full type vocabulary as candidate leading-prefixes, silently corrupting subject-nouns whose leading word coincided with a type token (`observation-function` → `def-function`, losing "observation"). Tightened to strip only the segment's own type forms. Two corrupted slugs (`def-function`, `scope-ambiguity-modulation`) restored.

### Methodology: separate-passes for role-prefix vs subject-noun

Going forward, role-prefix addition (mechanical) and subject-noun renaming (judgment-heavy) execute in separate cycles. Bundling creates two failure modes: the segment's prose drifts out of step with its new identity, and voters can't evaluate noun choices when the prefix is decided in the same cycle. Documented in `msc/naming-pilot-rename-plan.md` and the auto-memory.

### `FORMAT.md` segment-set principle

New "Segment-set principle (load-bearing for tooling)" subsection makes explicit what was previously implicit: every non-`old-*` file in `src/` is a segment that conforms to FORMAT (drafts and orphans included; stages are progress within FORMAT, not exemptions); `old-*` is the only exemption mechanism; other working material doesn't belong in `src/`. Tools (`bin/align-slug --all`, `bin/lint-outline`, `bin/build`) reference this principle.

### Refined naming-principles file

`msc/naming-principles.md` rewritten for the refined Round 1. Cold-start instruction moved to first paragraph (round-1 contamination evidence). New "Architectural invariants" section recording role-prefix discipline + subject-noun-first + Greek-vocabulary commitment + separate-passes methodology — these are no longer up for vote. New "Vote categories" section explicitly distinguishing rename / keep / canonicalize / add-alias / name-unnamed-thing. `+2` weight added; bands spelled out. Renamed-from-now-sounds-weird test added. Scope-honesty special-case for meta-segments documented.

### Side-resolutions

- **Finding 14 Option A** (`#scope-developer-agent` exact-status mismatch): closed by the type-frontmatter cleanup that landed in commit `0b9cd24` (`type: definition` → `scope`, `status: exact` → `axiomatic`).
- **`bin/lint-outline` PROOF → DERIV**: graphviz display label for `derivation` changed from "PROOF" to "DERIV", aligning with FORMAT.md's deliberate avoidance of proof terminology.

### Type-frontmatter audit (preflight for the sweep)

Opus general-purpose audit of all 142 active segments cleared the repo at 100% type-vocabulary conformance, zero stale tokens. Five type-vs-content mismatches surfaced; three clear cases corrected (`unity-dimensions`: discussion → definition; `simulation-results`: detail → observation; `tempo-composition`: sketch → derived). Two borderlines surfaced for reviewer judgment, not applied (`agent-opacity`, `observation-ambiguity-modulation`). 18 internal H1/tag-word inconsistencies catalogued; most are intentional setup-tag-before-main-tag patterns. Audit-recommended additional `TYPE_TO_PREFIX` mappings rejected as unnecessary or insufficient-frequency.

### Known follow-up

- **Formal-tag content cleanup**: ~135 segments still embed pre-rename slug names inside `*[Type (slug)]*` formal tags. Mechanical to detect, content to update; separate cycle.
- **Two reviewer-judgment type calls** from the audit (`agent-opacity`, `observation-ambiguity-modulation`).
- **Three H1/first-tag word disagreements** flagged by the audit (`objective-functional`, `composition-closure`, `ciy-observational-proxy`); content cleanup, any time.

---

*Prior cycle history: see [LOG.md](LOG.md). Prior commit/finding-level archive: see [TODO.md §Archive](TODO.md#archive--work-landed).*
