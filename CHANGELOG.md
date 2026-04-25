# CHANGELOG

The forward-going record of substantive changes to the framework. Entries are ordered most-recent-first, dated, and grouped by theme within a date.

## How this file relates to LOG.md, TODO.md §Archive, and git

- **CHANGELOG.md** *(this file)* — substantive changes from 2026-04-24 onward. Cycle-shape narratives ("what changed about how the theory thinks", structural moves, conventions adopted) go here. Entry granularity is the day; commit hashes appear inline for traceability.
- **[LOG.md](LOG.md)** — archaeology of cycles through 2026-04-24. Frozen at that date. Read it when the *origin* of a current commitment matters: whether a "settled" item rests on derivation or on a cycle's working consensus, or how an audit finding's prior status should shape current routing.
- **[TODO.md §Archive](TODO.md)** — commit-and-finding granularity record of landed work, kept inside the active TODO.
- **Git** — primary source for "what changed in code/segments." Use `git log --follow` for slug-renamed segments.

The split between CHANGELOG and TODO §Archive is intentional: CHANGELOG carries the *narrative shape* (what conventions changed, what disciplines emerged, what the cycle was about); TODO §Archive carries the *checklist trail* (which findings closed, which commits did what). They overlap in scope but serve different reading needs.

---

## 2026-04-25

### Audit-extraction cycle: 2026-04-24 fresh-pass results captured

The 2026-04-24 fresh-pass audit (an Opus-4.7 primary pass + independent Gemini and Codex re-audits in the same session) produced findings, an architectural proposal candidate, and a meta-lesson about audit failure modes. The primary pass had initially returned "zero findings"; Gemini and Codex independently surfaced five-plus real findings (math errors in worked examples, cross-segment contradictions around the recently-added C-iv route, integration debt between TST and `03-logogenic-agents/`). The audit's "Reading-mode failures" post-mortem became the foundation for the substantially improved `msc/de-novo-audit-instructions.md` (separate cycle, also 2026-04-24/25).

This cycle was extraction-only: no segment-text changes, no architectural decisions made — purely surfacing the audit's substantive content into the durable tracking documents (TODO.md, PROPOSALS.md, pending-findings-2026-04-25.md) so the source `msc/audit-2026-04-24-fresh-pass.md` could scroll into obscurity without losing signal. The next audit cycle, running with the improved instructions, will inevitably re-discover some of this batch's findings — capture-first protects the existing batch's signal against that overlap.

**What landed:**
- `msc/pending-findings-2026-04-25.md` — burden-of-proof writeups for 5 verified findings (F-V1 discrete-variance-gap math error; F-V2 scope-multi-agent vs scope-composite-agent contradiction; F-V3 C-iii vs $G_c$ requirement, = F8 from 2026-04-22 batch; F-V4 sign error in zero-sum worked example; F-V5 TST↔logogenic integration debt) and 3 partial findings (P-V1, P-V2, P-V3). Each finding verified first-hand by the integrating agent against current src text. F-V1's math re-derived independently via Taylor expansion of segment's own DA.1S; F-V4's NE re-checked via Monderer-Shapley derivative test ($\Phi = a_A - a_B$ wrong, correct is $\Phi = a_A + a_B$, NE $(1,1)$ not $(1,-1)$). External-citation spot-checks (Bretagnolle-Huber, Otto-Villani 2000) confirmed accurate.
- `TODO.md` "Active — Pending Findings" — 2026-04-25 batch table; F-V3↔F8 cross-reference; two decisions explicitly marked deferred (F-V3 routing Path A vs SP-21; SP-21 timing).
- `PROPOSALS.md` §G — **SP-21** (composite-agent scope-route ontology split) added with full schema. Critically: SP-21 *reverses* the deliberate 2026-04-22/23 unification reasoning (the disjunctive C-i ∨ C-ii ∨ C-iii ∨ C-iv form with explicit "preferred reading: treat as a different type within the same scope condition, via (C-iv)" in `msc/spike-strategic-composition.md`). Entry includes the prior-reasoning paper trail (8 dependent segments, the spike-level decision SP-21 would undo) and recommends *deferral* until Bundle 2 (Section III completion) matures the substrate. Reversal-with-paper-trail discipline is a precedent worth preserving for future audits.
- Mechanical fix bundle (F-V1, F-V2, F-V4, F-V5, P-V1, P-V3) delegated as a single Task agent with strict instructions to re-derive math rather than paste, read both TST and logogenic-agents segments before F-V5, and not auto-commit.

**What didn't land (deferred for Joseph):**
- F-V3 / F8 narrow editorial fix (Path A: induce $O_c$ from relevance variable $Y$ for C-iii). ~45–60 min.
- SP-21 architectural restructure (Path B / SP-21). 4–6 sessions; recommended for deferral.

**Convention surfaced this cycle.** When audit cycles produce both local findings AND architectural-restructure candidates that reverse recent deliberate decisions, the proposal should land in PROPOSALS.md with the *prior-reasoning paper trail explicit* — quoted spike passages, downstream rework cost, the specific decision-point being reversed. Joseph's question "is there prior reasoning that illuminates what will be undone?" is the right diagnostic for any restructure proposal; the answer should be in the proposal entry, not buried in the audit document.

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
