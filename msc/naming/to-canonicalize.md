# To-Canonicalize — First-Pass Curated List

**Generated:** 2026-05-04 (manual curation pass over `master-list-curated.json`, ~870 vote rows / 629 distinct currents).

## What this is

Existing framework names that should be **written into LEXICON.md** as canonical:

1. Already in use as current names in the corpus (`is_keep=true`)
2. Have at least one explicit `canonicalize` vote across R1+R2
3. No genuine rename pressure on alternatives (alt rename votes either rejected or absent)

Capitalization decisions are deferred. Cap-only variants in the corpus have been collapsed via `merged_variants`. Items with substantive `add-alias` proposals on alternatives are still included — the canonicalize decision is orthogonal to the add-alias decision (a parallel, later question).

## How to use

Scan the `Confirm` column. Mark `Y` / `N` / blank-to-defer. Rows with anything in `Flag` warrant a closer look. The act of canonicalization is adding/affirming the LEXICON.md entry; this list is the input, not the action.

## Notes on flags

- `weak` — only 1–2 voters, only 1–2 architectures (still passed the no-rename-pressure filter, but lower confidence).
- `competing alt: "..."` — an alternative candidate also has substantive `canonicalize` votes (≥2 weight, and not a pure formatting variant). Real competition; review the master list before confirming.
- `rename×N on keep (miscat)` — keep candidate has rename-category votes whose notes are actually keep-equivalent (e.g. "Keep."); flagged for transparency, not because the keep is contested.
- `possibly retired` — name appears to refer to a slug that has already been split or renamed.
- `slug already shortened` — current name is the verbose form of a slug that has already been shortened (e.g. `worked example bandit` vs. `#example-bandit`).
- `auditor-flagged baggage` — kept by voters but a reviewer noted philosophy-of-mind / external-field baggage.
- `FORMAT.md section header` / `different layer` — current is a process-vocabulary item rather than a theory-concept name.
- `Greek-phase consolidation` — bare and Greek-tagged forms folded into one row per the `latinized (greek) (english)` format.

---

## Table (13 entries — sync reconciliation 2026-05-04: 6 stale rows removed (already routed in batch E) + cycle-vs-loop landed as #61 confirmation)

| #   | Current name                                  | Source                                          | Canon votes | Archs | Flag                                                                                                                  | Confirm                                                      |
| --- | --------------------------------------------- | ----------------------------------------------- | ----------: | ----: | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| 22  | specification bound                           | `02-tst-core/src/result-specification-bound.md` |           6 |     3 | citability: fails (criterion 9)                                                                                       | D                                                            |
| 28  | adaptive cycle                                |                                                 |           5 |     3 | competing alt: "The cycle the adaptive cycle" (canon w=2); citability: fails (criterion 9)                            | D                                                            |
| 55  | operationalization                            | `01-aad-core/src/detail-operationalization.md`  |           3 |     3 | citability: fails (criterion 9)                                                                                       | D                                                            |
| 69  | "epistemic substate" / "purposeful substate"  |                                                 |           2 |     2 | weak                                                                                                                  | D                                                            |
| 70  | action fluency                                |                                                 |           2 |     2 | weak; citability: fails (criterion 9)                                                                                 | D                                                            |
| 71  | and or scope                                  |                                                 |           2 |     2 | weak                                                                                                                  | D                                                            |
| 87  | reactive system                               |                                                 |           2 |     2 | weak; citability: fails (criterion 9)                                                                                 | D                                                            |
| 90  | separable core structured repair general open |                                                 |           2 |     2 | weak                                                                                                                  | ???                                                          |
| 102 | coherence coupling measurement                |                                                 |           2 |     1 | weak; citability: fails (criterion 9)                                                                                 | D                                                            |
| 108 | "purpose" / "purposeful"                      |                                                 |           1 |     2 | weak; competing alt: "Purposeful" (canon w=3)                                                                         | D -- I like actuated better still                            |
| 109 | boundary condition                            |                                                 |           1 |     2 | weak; citability: fails (criterion 9)                                                                                 | D                                                            |
| 112 | log odds edge coordinate                      |                                                 |           1 |     2 | weak                                                                                                                  | D                                                            |
| 116 | escape route                                  |                                                 |           1 |     1 | weak; rename×1 on keep (note-check: miscat); one voter proposed rename; competing pressure                            | D                                                            |

---

## Notes — items folded or excluded for transparency

- **`aporia` / `prolepsis` / `aisthesis` / `epistrophe` / `praxis`** (bare) and **`aporia ἀπορία` / `prolepsis πρόληψις` / `aisthesis αἴσθησις` / `epistrophe ἐπιστροφή` / `praxis πρᾶξις`** (Greek-tagged) — folded into 5 consolidated phase rows in the table above.
- **`aporia prolepsis aisthesis epistrophe praxis`** (cluster row, 1 canon vote, "keep as a set") — redundant with the 5 individual phase rows.
- **`software scope`** (was row 104, removed 2026-05-04) — slug discipline already settled this: `scope-software` has subject-noun `software` (with role-prefix `scope`); the row's `software scope` form re-introduced the role-as-name pattern the slug discipline retired. Separately recommended: rename `scope-software` → `scope-evolving-software` to match the segment's own `\mathcal{S}_{\text{evolving}}` formal expression. Belongs in the rename-plan, not the canonicalize-list.

If anything in the **excluded** set above should actually be in the table, flag it back to me.
