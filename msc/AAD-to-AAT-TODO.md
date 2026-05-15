# AAD → AAT Rename + Volume-Directory Harmonization Plan

*(Filename is AAD-centric for findability — Joseph's requested name — but
scope is broader; see §1.2.)*

**Status:** planned — not yet executing.
**Author:** drafted 2026-05-15 with Joseph, after exploration and orientation.
**Scope:** two orthogonal but co-executed transformations on one branch:
1. **Name rename** — the mathematical core from *Adaptation and Actuation
   Dynamics (AAD)* to *Adaptation and Actuation Theory (AAT)* (prose +
   metadata + acronym).
2. **Volume-directory harmonization** — all four component directories to
   a uniform `NN-{slug}-core` pattern with short build slugs (§1.2). This
   is pure path/slug restructuring; it carries no display-name change for
   Parts 2–4.

They share the same path-sweep machinery, so doing them in one cycle is
strictly less total work and risk than two; see the message-thread
rationale. Kept as *distinct commits within the branch* (name-driven vs
harmonization) for bisectability.
**Precedent:** this plan deliberately mirrors the structure of the prior
`msc/naming/name-transition-aad.md` (the ACT → AAD transition) — same
branch / per-stage-commit / staged-verification discipline — but the
*archaeology policy is inverted* (see §2) and the *generated-vs-source
discipline* is now load-bearing (see §3). Read those two sections before
running anything; do not pattern-match blindly off the ACT → AAD plan.

> **Why this file keeps "AAD" literal throughout.** This document is a
> name-decision record: "AAD" here is the *object being transitioned away
> from*. It is on the exemption list (§2.3) and must never be swept.

---

## 1. What is changing, and why

The mathematical core (Part 1) has been **Adaptation and Actuation
Dynamics (AAD)** since the 2026-04-16 ACT → AAD rename. It becomes
**Adaptation and Actuation Theory (AAT)**.

| Role | Old | New | Acronym |
|---|---|---|---|
| Part 1 — mathematical core | Adaptation and Actuation **Dynamics** | Adaptation and Actuation **Theory** | **AAD → AAT** |

Effectively: the last word changes (*Dynamics → Theory*) and the acronym's
last letter changes (*D → T*). The compound "Adaptation and Actuation"
and the conjunction "and" are unchanged in the canonical/default form.

**Rationale (Joseph, 2026-05-15 — verbatim, for the CHANGELOG entry at
Stage 8):** *"Upgrading terminology to Theory now that it has
substantial claims and novelty, allowing the term Adaptation and
Actuation Dynamics to be freed up for a very dry and generic
textbook."* — Note the forward-looking half: "Adaptation and Actuation
Dynamics" is being *freed*, not retired, for possible reuse as a
plain-textbook title. The exemption-kernel rationale (§2.3) and the
HISTORICAL-CONTEXT lineage note (§2.4) should not imply the old phrase
is dead — it is vacated, deliberately.

### 1.1 The conjunction: "and" is the default; "&" is a print style

Decision (Joseph, 2026-05-15): **"and" is the canonical/default form
everywhere.** The ampersand "&" is a *typographic style choice reserved
for the PDF title page / front-matter*, where the title is set as designed
display type — not something written out in running prose.

Concretely, the **only** places that carry `Adaptation & Actuation
Theory` (ampersand) are:

- `01-aat-core/mono-meta.yaml` → `title:` (this string *is* the PDF
  title-page title)
- `01-aat-core/OUTLINE.md` line 1 → `# *Volume* …` (the build's
  `outline_walker` reads this line as the volume/title-page title)
- the cover SVGs — **already done** in commit `398c708`; their tspans
  already render `Adaptation` `&` `Actuation` `Theory`. Only the
  *filenames* and the `cover_svg:` reference change (§ Stage 2).

Everywhere else — segment prose, README body, CLAUDE.md, NOTATION,
`CITATION.cff`, `.zenodo.json`, all discussion text — uses the default
**"Adaptation and Actuation Theory"**.

> Judgment call to confirm at execution: `CITATION.cff` and `.zenodo.json`
> are machine-readable citation/deposit metadata rendered as plain
> citations, not a designed title page. This plan puts them in the
> **"and"** bucket. Override at Stage 1 if you want "&" in the deposit
> title.

### 1.2 Volume-directory harmonization (co-executed; orthogonal to the name change)

All four component directories move to a uniform `NN-{slug}-core`
pattern with short build slugs. This is **pure path/slug
restructuring** — *no* display-name change for Parts 2–4 (Logogenic
Agents stays "Logogenic Agents"; ELI stays "Emergent Logozoetic
Intelligences").

| # | Old dir | New dir | slug (old→new) | short_title | `title:` (display) |
|---|---|---|---|---|---|
| 01 | `01-aad-core` | `01-aat-core` | `aad`→`aat` | `AAD`→`AAT` | `AAT: Adaptation & Actuation Theory` *(styled `&`)* |
| 02 | `02-tst-core` | `02-tst-core` *(unchanged — already conforms)* | `tst` | `TST` | `TST: Temporal Software Theory` *(unchanged)* |
| 03 | `03-logogenic-agents` | `03-llm-core` | `loga`→`llm` | `LogA`→`LLM` | `Logogenic Agents` *(unchanged)* |
| 04 | `04-eli` | `04-eli-core` | `eli` *(unchanged)* | `ELI` | `Emergent Logozoetic Intelligences (ELI)` *(unchanged)* |

- **`03` slug = `llm`** (Joseph confirmed 2026-05-15) despite "LLM"
  appearing ~1,774× in-repo as *Large Language Model* and the sibling
  NeurIPS path `~/src/neurips/03-llm-hallucinate-bound/`. Accepted
  because it is *internal-only* (dir + build slug; the citable display
  name stays "Logogenic Agents") and the pun is apt (logogenic agents
  *are* LLM-substrate). Recorded here so the choice is on the record,
  per this project's collision-sensitive naming history.
- **Old build aliases kept as accepted-but-secondary** so existing
  scripts / muscle-memory don't break: `bin/build-monograph` and
  `bin/output-version` keep `loga`/`logogenic` (→ `03-llm-core`). The
  `aad` alias is **dropped** (the name itself changed — a stale `aad`
  alias would be a silent foot-gun).
- **Stale `04-logozoetic-agents`** (pre-2026-05-01 name; 138 occ / 60
  files, e.g. `bin/lint-md:858`) is *dangling* — the dir is already
  `04-eli`. Fold its cleanup into this cycle: `04-logozoetic-agents`
  → `04-eli-core`. Opportunistic, in-scope, leaves the tree honest.

**ASF (the umbrella) is untouched.** The April-2026 transition renamed
the *core* ACT→AAD *and* concurrently named the *umbrella* Agentic
Systems Framework (ASF). AAD→AAT renames only the core; ASF and the
`agentic-systems` repo name stay. Stated explicitly because the
ASF/AAD layering is an easy cross-wire.

---

## 2. Scope policy

### 2.1 What changes

Rename everything live/working; freeze pure archaeology/journal;
disclose-don't-rename two low-value archive trees. Decision is Joseph's
**2026-05-15 refined disposition** (verbatim priority table below — the
key correction over the earlier "rename everything": **`spikes/` is
mostly *active* — only `spikes/.integrated/` is archaeology** — the
non-integrated spikes still require integration into the theory, so
they must speak current vocabulary; and `msc/reflections/` is the
author's journal, frozen like `_obs/`).

### 2.2 Disposition by tree (Joseph 2026-05-15, priority-ordered)

| Tree | Priority to rename | Action |
|---|---|---|
| `spikes/**/*.md` (≠ `.integrated`) | **HIGH** — active, awaiting theory integration | **RENAME** |
| `msc/*.md` toplevels + active subdirs (`domain-unification-*`, `logogenic-encounter-*`) | **HIGH** — active working docs | **RENAME** |
| `spikes/.integrated/**` | fine either way | **FREEZE** (absorbed reasoning-trails; archived-spikes-not-live discipline) |
| `audits/**` (incl. `.integrated/`) | medium (big backlog; many processed) | **DISCLOSE, don't rename** — note in new `audits/README.md` |
| `msc/naming/**` | low (naming-cycle archive) | **DISCLOSE, don't rename** — note in new `msc/naming/README.md` (subsumes the old §2.3 kernel — name-decision records stay literal here by construction) |
| `msc/AUDIT-WORKING-*/**` | low (per-cycle audit intermediates) | **FREEZE** (history; git has it) |
| `msc/reflections/**` | best not | **FREEZE** (author's philosophical journal) |
| `_obs/`, `releases/` | best not | **FREEZE** (superseded / tagged-release snapshots) |
| `msc/AAD-to-AAT-TODO.md` | n/a | **KERNEL** — literal-AAD always (this plan) |

Approx volumes (in-scope `\bAAD\b`, 2026-05-15): RENAME ≈ live/canonical
~302 + `spikes`(non-`.integrated`) ~1,335 + `msc` active ~1,300; FREEZE/
DISCLOSE retains AAD legitimately in `_obs` 1,306 · `msc/naming` 5,939 ·
`spikes/.integrated` 1,201 · `audits` 460 · `msc/AUDIT-WORKING-*` ~600 ·
`msc/reflections` 91 · `releases` 40. These are *expected residual*, not
defects (see Stage 10 — verification is scoped to the RENAME set only).

Other counts pinned for verification (2026-05-15):

- full phrase `Adaptation and Actuation Dynamics` = **172 matching
  lines / 206 raw occurrences** (a line may carry it twice; use the
  same counting flag at verify-time — `-o` for occurrences)
- `AAT` currently present = **0** (clean target namespace)
- directory path-tokens to sweep (harmonization, §1.2):
  - `01-aad-core` → `01-aat-core`: **4,536** occ / **292** files
  - `03-logogenic-agents` → `03-llm-core`: **844** occ / **226** files
  - `04-eli` → `04-eli-core`: **372** occ / **97** files
  - `04-logozoetic-agents` (stale) → `04-eli-core`: **138** occ / **60** files
  - `02-tst-core`: **1,116** occ / 164 files — **no change** (already
    conforms; do *not* sweep)
- target dir namespace (`01-aat-core` / `03-llm-core` / `04-eli-core`)
  verified clean — the `03-llm` greps were all the unrelated NeurIPS
  sibling path `03-llm-hallucinate-bound/`, not a collision.

**Verification mechanics (learned at Stage 0 — apply at every grep/sweep):**

- **Always exclude the NON-RENAME set** from sweeps *and*
  count-verification (per §2.2: frozen + disclosed + kernel). *Use the
  `:(exclude)` LONG form* — the `:!path` short form **fails** with
  "Unimplemented pathspec magic" on this git (verified 2026-05-15).
  For sweeps prefer the `git ls-files -z | grep -zvE | xargs -0`
  builder (below) with this ERE; for git-grep verification use the
  matching `:(exclude)` pathspecs. Canonical NON-RENAME ERE
  (anchored at path start), verbatim:
  ```
  ^(_obs/|releases/|LOG\.md$|audits/|msc/naming/|msc/reflections/|msc/AUDIT-WORKING-|spikes/\.integrated/|msc/AAD-to-AAT-TODO\.md$)
  ```
  git-grep form:
  ```
  ':(exclude)_obs' ':(exclude)releases' ':(exclude)LOG.md' ':(exclude)audits' ':(exclude)msc/naming' ':(exclude)msc/reflections' ':(exclude)msc/AUDIT-WORKING-*' ':(exclude)spikes/.integrated' ':(exclude)msc/AAD-to-AAT-TODO.md'
  ```
  (`msc/naming` not-renamed subsumes the old §2.3 kernel —
  `name-transition-aad.md` / `collision-check-brief.md` stay literal by
  construction; `_obs` subsumes the old hypothetical-theory-choice
  entry. `audits` whole subsumes `audits/.integrated`. **`LOG.md`**
  added 2026-05-15 — pre-2026-04-24 frozen archaeology, like `_obs/`;
  `HISTORICAL-CONTEXT.md` is *not* here, it gets the Stage-8 manual
  lineage edit.)

  > **Stage-coverage gaps found & closed during execution (record so a
  > re-run doesn't repeat them):** (1) *sibling `.aux`* — Stage 2 named
  > only `aad.aux`; `tst.aux`/`loga.aux`/`eli.aux` git-rm'd in Stage 4.
  > (2) *`doc/`, `ref/`, `CHANGELOG.md`* — no stage's explicit file list
  > covered them though §2.2 bucketed them "rename"; swept under Stage 6
  > before regeneration (the unswept `doc/readme/src/` partials had
  > caused 16 AAD in a prematurely-regenerated README). Lesson: the
  > §2.2 buckets are the source of truth for *what*; the per-stage
  > file lists must be checked against them, not trusted to be
  > exhaustive. (3) *`mono/` is gitignored* — monograph PDFs/md are
  > build artifacts, never committed; the build verifies clean but
  > produces nothing to stage. (4) *`bin/build-monograph --all` does
  > not repopulate tracked `<vol>/<slug>.aux`* — they were tracked
  > before; flagged for Joseph (regenerable xr artifacts; whether to
  > re-track or gitignore is his call, out of rename scope).
  >
  > **Generated files are verified by `AAD==0` + "regenerated by its
  > tool", NOT by diff-purity** (a regenerator legitimately rewrites
  > whole sections): `README*.md`, `FINDINGS.md`, `LEXICON.md`,
  > `doc/readme/src/_findings-summary.md` / `_recent-progress.md` /
  > `_known-issues.md`. Diff-purity applies to *source* only.
- **Sweep file-list builder — zsh-safe + NUL-safe + slurp.** zsh does
  *not* word-split unquoted `$vars` (bash does); never `for f in $LIST`.
  Build the list and pipe; never interpolate a space-joined string as
  one arg:
  ```
  git ls-files -z -- '<DIR-or-glob>' \
   | grep -zvE '^(_obs/|releases/|msc/AAD-to-AAT-TODO\.md$|msc/naming/name-transition-aad\.md$|msc/naming/collision-check-brief\.md$)' \
   | xargs -0 perl -0777 -i -pe 's/(Adaptation\s+and\s+Actuation\s+)Dynamics/${1}Theory/g; s/\bAAD\b/AAT/g'
  ```
  (`-0777` slurp is mandatory for the wrapped-phrase reason in Rule 1;
  `\bAAD\b` is single-token so slurp-safe too.)
- **Word-boundary regex:** `git grep -o '\bAAD\b'` (POSIX basic) is
  reliable; `git grep -oE '\bAAD\b'` silently returns **0** (git `-E`
  does not honor `\b`). Never verify AAD/AAT residue with `-E \b`.
- **Phrase verification is slurp-aware** (per-line `grep` false-0s on
  wrapped phrase — Rule 1): verify with
  `perl -0777 -ne 'print scalar(()=/Adaptation\s+and\s+Actuation\s+Dynamics/g)'`
  plus a stray-`Actuation\s+Dynamics` check, never a bare line `grep`.
- **Diff-purity is the verification invariant, NOT count-comparison.**
  Planning-time counts (AAD 14,388; dir-tokens 4,536/844/372/138/1,116)
  are *superseded after Stage 1* — the repo legitimately changes each
  stage (commits, generated-artifact deletions, the plan doc itself),
  so a count mismatch is expected and is *not* a defect signal. The
  real correctness check, run every content stage: take the stage diff
  (FROZEN+KERNEL excluded) and confirm **every** changed `+`/`-` line
  is explained by the stage's intended token flip(s) plus an
  enumerated short list of targeted edits — zero non-conforming lines.
  This caught nothing-bad and *proved* Stages 2a/2b clean where a
  count delta would have raised a false alarm. Pattern:
  ```
  git diff <FROZEN+KERNEL excludes> | grep -E '^[+-]' \
   | grep -vE '^(\+\+\+|---)' | grep -vE '<intended tokens>' \
   | grep -vE '<enumerated targeted-edit lines>' \
   | grep -vE '^[+-]\s*$'        # must be empty
  ```

### 2.3 Kernel — collapsed into §2.2

The earlier "name-decision kernel" (`name-transition-aad.md`,
`collision-check-brief.md`, the original hypothetical-theory-choice
note) is **subsumed by the §2.2 disposition**: `msc/naming/` is
not-renamed (disclosed), so those records stay literal-AAD by
construction; `_obs/` is frozen. The only surviving explicit kernel is
**`msc/AAD-to-AAT-TODO.md` (this plan)** — literal-AAD always, since it
documents the transition. No separate eyeball-confirm step is needed
(the structural exclusion handles it); the discipline reason is
preserved here: sweeping a name-decision record would make it falsely
read "ACT → AAT", which never happened.

### 2.4 Manual-edit exceptions (mechanical pass would produce a falsehood)

- **`HISTORICAL-CONTEXT.md` line 92.** Currently:
  *"…founded in March 2026 (initially under the name Agentic Cycle
  Theory, renamed to AAD in April 2026 to resolve a collision with 'AI
  Consciousness Test' …)"*. A mechanical `AAD → AAT` makes this read
  "renamed to AAT in April 2026" — **false**: the April-2026 rename was
  to AAD; AAT is the May-2026 rename. Replace this clause *manually* with
  the brief lineage note Joseph asked for, e.g.:

  > *…founded in March 2026 (initially Agentic Cycle Theory; renamed to
  > Adaptation and Actuation Dynamics in April 2026 to resolve the
  > "AI Consciousness Test" collision; refined to **Adaptation and
  > Actuation Theory (AAT)** in May 2026 — see CHANGELOG).*

  This single clause is the **only** place the old "AAD" name survives in
  live prose, and it is deliberate (the "very very brief note in
  HISTORICAL-CONTEXT" from the brief).

- **`CHANGELOG.md`** — add a new cycle entry narrating the rename (scope,
  the exemption kernel, the styled-`&` decision, what regenerated). This
  is the second sanctioned place "AAD" appears as the prior name.

### 2.5 Out-of-repo touch-points (handled, but flagged separately)

- **Project auto-memory** — `~/.claude/projects/-Users-josephwecker-v2-src-agentic-systems/memory/`:
  32 files + `MEMORY.md` reference AAD. Separate stage (Stage 9), outside
  git. Preserve each memory's intent; only the name changes.
- **Global `~/.claude/CLAUDE.md`** references AAD heavily but is
  cross-project and curated through the memorata workshop, *not* this
  repo. **Do not silently rewrite it.** Flag for Joseph to update in the
  global-memory substrate; out of scope for this plan's git work.

---

## 3. Generated-vs-source discipline (load-bearing — new since ACT → AAD)

Several "files" are build outputs. **Hand-editing them is wrong** — the
next build overwrites the edit and (worse) a stale hand-edit masks a
source that still says AAD. For each, edit the *source* and *regenerate*:

| Generated artifact | Source of truth | Regenerate with |
|---|---|---|
| `README.md`, `README-auditor.md` | `doc/readme/src/_*.md` partials + `doc/readme/*.liquid` | `bin/build-readme` (or `bin/refresh-all`) |
| auto-partials `_findings-summary.md`, `_recent-progress.md`, `_known-issues.md` | segment `## Findings` / OUTLINE / Known-Fragilities | `bin/refresh-all` |
| `LEXICON.md` | `terminology/entries/<slug>.md` (+ `decisions/`) | `bin/term render` |
| `FINDINGS.md` | segment-level `## Findings` sections | `bin/extract-findings` |
| Monograph builds (`aad-v0.2.0.{md,s.pdf}`) **and ALL per-volume `.aux`** (`01-*/aad.aux`, `02-tst-core/tst.aux`, `03-llm-core/loga.aux`, `04-eli-core/eli.aux`) | volume segments + `OUTLINE.md` + `mono-meta.yaml` | **`bin/build-monograph --all`** (after Stage 2 slug change) — and `git rm` the stale ones first |
| dependency-graph SVGs (`01-aat-core/src/img/*` if present) | OUTLINE + `bin/lint-outline` | `bin/lint-outline` (regen) |

Rule: in any stage that *would* touch a generated file, instead touch its
source and add the regenerate command to that stage's actions.

> **`.aux` files — purpose and why `--all` (Joseph, 2026-05-15).** The
> per-volume `<slug>.aux` are committed deliberately: they carry the
> LaTeX label table that enables **cross-monograph linking** (one
> volume's PDF referencing another's theorems/sections via `xr`). They
> are *generated* and "super easy to regenerate via
> `bin/build-monograph --all`" — but the regen **must be `--all`**, not
> a single volume: cross-volume xr resolves only when every volume's
> `.aux` is rebuilt together, so a one-volume build would leave stale /
> missing sibling `.aux` and broken cross-references. *Stage-2 plan gap
> (corrected):* Stage 2a only named `01-*/aad.aux`; the siblings
> (`tst.aux`, `loga.aux`→`llm.aux`, `eli.aux`) were `git rm`'d in
> Stage 4 when the residual surfaced. `_obs/act-core-test.aux` stays
> frozen. (Whether `.aux` should be git-tracked at all vs gitignored is
> a separate question, out of this rename's scope.)

---

## 4. Substitution rules (exact)

Rules 1–3 + 5 are the **name** change (AAD→AAT). Rule 4 is the
**directory harmonization** (orthogonal; §1.2). There is **no**
standalone `Dynamics → Theory`.

1. **Full phrase** `Adaptation and Actuation Dynamics`
   → `Adaptation and Actuation Theory`.
   *Safety result (verified 2026-05-15):* every standalone "Dynamics"
   token in the repo that refers to the theory is the tail of this exact
   phrase. So phrase-only replacement is provably safe and a blanket
   `s/Dynamics/Theory/` is **forbidden** (would wreck "dynamical
   systems", "learning dynamics", "strategy dynamics",
   "modularity-state-dynamics", "adversarial dynamics", …).

   > ⚠️ **MUST be slurp-mode, whitespace-preserving (Stage-1 lesson,
   > 2026-05-15).** The phrase wraps across lines in justified prose
   > (`…Actuation\n  Dynamics…`). A per-line `perl -pe 's/Adaptation
   > and Actuation Dynamics/…/'` silently **misses every wrapped
   > occurrence**, and since the acronym sub *does* fire you get the
   > self-contradiction *"Adaptation and Actuation Dynamics (AAT)"*.
   > Canonical command for the phrase, every stage:
   > ```
   > perl -0777 -i -pe 's/(Adaptation\s+and\s+Actuation\s+)Dynamics/${1}Theory/g' FILES…
   > ```
   > `\s+` between *all* words tolerates a wrap at any gap; the capture
   > preserves the exact original whitespace (newline+indent) so line
   > layout is undisturbed; case-sensitive matches only the proper
   > noun; idempotent (already-fixed text has no "Dynamics" after
   > "Actuation"). **Verification must also be slurp-aware:** a
   > per-line `grep` for the phrase reports a false 0 on wrapped
   > instances — verify with
   > `perl -0777 -ne 'print scalar(()=/Adaptation\s+and\s+Actuation\s+Dynamics/g)'`
   > **and** a stray-`Actuation\s+Dynamics` check.

2. **Acronym** (case-sensitive, all-caps): `\bAAD\b` → `AAT`. This covers
   `AAD's`, `AAD-internal`, `AAD-core`, `(AAD)`.

3. **Acronym, glued edge-cases** `\bAAD\b` misses — handle explicitly:
   - `AAD/` (e.g. "AAD/TST" in tables) → `AAT/` (~10 live hits)
   - `AAD_Dependencies` (`bin/lint-outline:316` graphviz id) →
     `AAT_Dependencies`
   - Verification grep for residual `AAD` after the pass catches any
     other glued form.

4. **Path / slug tokens** — *enumerated, not blanket* (a blanket
   `s/aad/aat/` or `s/eli/eli-core/` would corrupt hashes / prose /
   content slugs). Two groups:

   **(4a) Directory path-tokens** — literal, global (§2.2 counts):
   - `01-aad-core` → `01-aat-core`
   - `03-logogenic-agents` → `03-llm-core`
   - `04-eli` → `04-eli-core` — *path-segment-anchored only* (`04-eli/`
     and `04-eli` as a path component); never the bare word "eli" or
     `#…-eli-…` content slugs/anchors
   - `04-logozoetic-agents` → `04-eli-core` (stale-name cleanup)
   - `02-tst-core` — **no change**

   **(4b) Build / metadata slug points** — targeted, per file:
   - `01-aat-core/mono-meta.yaml`: `slug: aat`, `short_title: AAT`
   - `03-llm-core/mono-meta.yaml`: `slug: llm`, `short_title: LLM`
     (`title: "Logogenic Agents"` unchanged)
   - `04-eli-core/mono-meta.yaml`: slug/title unchanged (only dir moved)
   - `bin/build-monograph` id_aliases (107–110):
     `{ dir:'01-aat-core', id_aliases:%w[01 aat] }`,
     `{ dir:'03-llm-core', id_aliases:%w[03 llm loga logogenic] }`,
     `{ dir:'04-eli-core', id_aliases:%w[04 eli] }` (02 unchanged)
   - `bin/output-version` map (24–27): update dir values; add
     `'llm' => '03-llm-core'`; keep `'loga'`/`'logogenic'` →
     `03-llm-core` (back-compat); **drop** the `'aad'` key
   - `bin/lint-md:858` list →
     `['01-aat-core','02-tst-core','03-llm-core','04-eli-core']`
     (this also fixes the stale `'04-logozoetic-agents'` on that line)
   - artifact basenames: `aad-v0.2.0.{md,s.pdf}`, `01-aad-core/aad.aux`,
     `AAD-cover{,-master}.svg` → AAT equivalents; any committed
     `loga-v*` monograph artifact → `llm-v*` (regenerate, `git rm` old)

5. **Styled `&` (title-page sources only — §1.1):** at the two
   title-page source lines, the *new* string is
   `Adaptation & Actuation Theory` (not "and"). Apply this **after** the
   default phrase pass, as a targeted re-edit of exactly those two lines.

---

## 5. Staged procedure

Branch `rename/aad-to-aat`; per-stage commit; `--no-ff` merge to `main`
at the end. Each stage independently reviewable and revertible
(`git checkout main -- <path>` per file, or abandon the branch).

macOS `sed`: use `sed -i ''` or Homebrew `gsed`. Prefer scripted
substitution **plus a per-file diff review** for prose stages.

### Stage 0 — Preflight
- `git checkout -b rename/aad-to-aat`; verify clean tree.
- Re-run the §2.2 inventory; confirm all pinned counts (name tokens +
  the four dir path-tokens; AAT=0; target dirs clean). If materially
  off, stop and re-orient.
- Baseline build: `bin/build-monograph aad` and keep the PDF/`.md` for
  before/after comparison (segment-count and structural parity check at
  Stage 10).
- Write nothing else; commit not needed (no changes yet).

### Stage 1 — Top-level docs + publication metadata
Scope: `CLAUDE.md`, `OUTLINE.md`, `NOTATION.md`, `FORMAT.md`,
`FORMAT-TODO.md`, `PRACTICA.md`, `TODO.md`, `PROPOSALS.md`,
`TERMINOLOGY-TODO.md`, `CITATION.cff`, `.zenodo.json`.
- Rules 1–3, default "and".
- **Do not edit** `README.md` / `README-auditor.md` / `LEXICON.md` /
  `FINDINGS.md` here — regenerated in Stage 6 from sources.
- `HISTORICAL-CONTEXT.md`: defer the line-92 clause to Stage 8 (manual);
  sweep the rest here.
- Verify: `grep -cE '\bAAD\b|Adaptation and Actuation Dynamics' <file>`
  → 0 per file (except the deferred HISTORICAL-CONTEXT clause).
- Commit: `Rename AAD→AAT: top-level docs + publication metadata`

### Stage 2 — Directory + slug + artifacts (all four volumes; two commits)

Two coherent, independently-revertible commits within the branch
(name-driven vs harmonization), so a bisect can isolate either.

**Stage 2a — name-driven (volume 01, AAD→AAT):**
- `git mv 01-aad-core 01-aat-core`
- Global path-token replace `01-aad-core` → `01-aat-core` (Rule 4a;
  4,536 occ / 292 files — links, segment `depends:`, configs, JSON).
- `01-aat-core/mono-meta.yaml`: `slug: aat`, `short_title: AAT`,
  `title: "AAT: Adaptation & Actuation Theory"` (**styled `&`**),
  `cover_svg: AAT-cover.svg`.
- `git mv` the cover SVGs `AAD-cover{,-master}.svg` →
  `AAT-cover{,-master}.svg`; update `sodipodi:docname` inside each
  (cosmetic) — visible tspans already correct, no "AAD"/"Dynamics"
  text remains (verified).
- `git rm 01-aad-core/aad.aux` (regenerated as `01-aat-core/aat.aux` in
  Stage 6); `git rm aad-v0.2.0.md aad-v0.2.0s.pdf` (regenerated as
  `aat-v0.2.0.*` in Stage 6).
- Commit: `Rename AAD→AAT: dir 01-aad-core→01-aat-core, slug, cover/artifacts`

**Stage 2b — directory harmonization (volumes 03, 04; 02 untouched):**
- `git mv 03-logogenic-agents 03-llm-core`; `git mv 04-eli 04-eli-core`
- Global path-token replace (Rule 4a): `03-logogenic-agents` →
  `03-llm-core`; `04-eli` → `04-eli-core` (path-segment-anchored — do
  *not* touch bare "eli" or `#…eli…` content slugs); stale
  `04-logozoetic-agents` → `04-eli-core`.
- `03-llm-core/mono-meta.yaml`: `slug: llm`, `short_title: LLM`
  (`title` unchanged). `04-eli-core/mono-meta.yaml`: slug/title
  unchanged (only the dir moved). Sibling `mono-meta.yaml` comments
  referencing `01-aad-core/` → `01-aat-core/`.
- `git rm` any committed `loga-v*` monograph artifact (regenerated as
  `llm-v*` in Stage 6).
- Verify: `git grep -lE '01-aad-core|03-logogenic-agents|04-eli/|04-logozoetic-agents'`
  → only §2.3 kernel files (acceptable).
- Commit: `Harmonize volume dirs: 03→03-llm-core, 04→04-eli-core; drop stale 04-logozoetic-agents`

### Stage 3 — `01-aat-core/` segments
- Every `01-aat-core/src/*.md` + `01-aat-core/OUTLINE.md`.
- Rules 1–3, default "and". Slugs/anchors are content-based — unchanged
  (verified: no slug contains "aad").
- `01-aat-core/OUTLINE.md` line 1 `# *Volume* …`: apply the **styled
  `&`** form → `# *Volume* Adaptation & Actuation Theory (AAT)`.
- Verify per file: `grep -cE '\bAAD\b|Actuation Dynamics' <file>` → 0.
- Commit: `Rename AAD→AAT: Part 1 (01-aat-core) segments`

### Stage 4 — Prose cross-references in Parts 2–4
- Post-Stage-2 dirs: `02-tst-core/`, `03-llm-core/`, `04-eli-core/`
  (segments + OUTLINEs). The path-token sweep already happened in
  Stage 2; this stage is the **prose** AAD→AAT name rename (Rules 1–3)
  in cross-references — "grounded by AAD", "AAD's Section II result",
  `AAD/` glued forms in OUTLINE tables.
- Commit: `Rename AAD→AAT: prose cross-references in Parts 2–4`

### Stage 5 — Terminology source
- `terminology/entries/*.md`, `terminology/decisions/**`,
  `terminology/README.md` (Rules 1–3).
- Append a `terminology/decisions/<aat-slug>/<ts>-joseph-rename.md`
  event recording AAD→AAT per the `bin/term decide` convention
  (action: `rename`), if an AAD/AAT term entry exists; else note in the
  CHANGELOG only.
- Regenerate: `bin/term render` → `LEXICON.md`. Verify
  `bin/term lint` clean.
- Commit: `Rename AAD→AAT: terminology entries + LEXICON re-render`

### Stage 6 — Build scripts + regeneration
- Scripts — Rule 4b (all four `id_aliases`, the `output-version` map,
  the `lint-md` component list) + comment prose (Rules 1–3):
  `bin/build-monograph`, `bin/output-version`, `bin/lint-outline`
  (incl. `AAD_Dependencies` → `AAT_Dependencies`), `bin/lint-md`,
  `bin/extract-findings`, `bin/extract-known-issues`, `bin/build-tex`,
  `bin/align-slug`, `bin/lib/*.rb` (comments referencing AAD /
  `01-aad-core` / old dir names).
- Regenerate, in order:
  - `bin/refresh-all` → `README.md`, `README-auditor.md`,
    auto-partials, `FINDINGS.md`
  - **`bin/build-monograph --all`** (regenerates every volume so all
    `.aux` rebuild together for cross-monograph xr — see §3 note) →
    `aat-v0.2.0.{md,s.pdf}` + `01-aat-core/aat.aux`,
    `02-tst-core/tst.aux`, `03-llm-core/llm.aux`, `04-eli-core/eli.aux`;
    visually confirm the **PDF title page shows the styled "Adaptation &
    Actuation Theory"** and the renamed cover renders.
  - dependency-graph SVGs if the build emits them.
- Verify: `bin/lint-md` and `bin/lint-outline` pass; built `aat-v0.2.0.md`
  has no `\bAAD\b` (except none expected).
- Commit: `Rename AAD→AAT: build scripts + regenerate README/LEXICON/FINDINGS/monograph`

### Stage 7 — Active spikes + active msc sweep (refined scope, Joseph 2026-05-15)
- **RENAME (Rules 1–3 name + 4a dir-tokens):**
  - `spikes/**/*.md` and `spikes/*.md` **except** `spikes/.integrated/`
    (HIGH — active spikes awaiting theory integration)
  - `msc/*.md` toplevels **and** active subdirs
    (`msc/domain-unification-*/`, `msc/logogenic-encounter-*/`) — HIGH
  - Builder: `git ls-files -z -- 'spikes/*.md' 'spikes/**/*.md' 'msc/*.md' 'msc/**/*.md' | grep -zvE '^(spikes/\.integrated/|msc/naming/|msc/reflections/|msc/AUDIT-WORKING-|msc/AAD-to-AAT-TODO\.md$)' | xargs -0 perl -0777 -i -pe '<Rule1+2+3 subs>'`
- **DISCLOSE, don't rename** — create two small READMEs (new files,
  written in current AAT voice) so an agent reading the archive
  mentally substitutes:
  - `audits/README.md` — "the framework was renamed AAD→AAT 2026-05-15;
    this audit corpus is historical and retains 'AAD' as written at the
    time — read it as 'AAT'. Canonical record: CHANGELOG /
    HISTORICAL-CONTEXT / CLAUDE.md."
  - `msc/naming/README.md` — same stanza (also explicitly: the
    name-decision records here, esp. `name-transition-aad.md`, *must*
    stay literal-AAD — renaming would falsely read "ACT→AAT").
- **FREEZE (no edit):** `spikes/.integrated/`, `msc/AUDIT-WORKING-*`,
  `msc/reflections/`, `_obs/`, `releases/` — canonical record is
  CHANGELOG/HISTORICAL-CONTEXT/CLAUDE.md; no per-tree note needed.
- Verify (diff-purity + slurp-aware) over the RENAME set only; the
  NON-RENAME ERE (§2.2) is the allowed-residual boundary.
- Commits: (a) `Rename AAD→AAT: active spikes + active msc working docs (Stage 7)`; (b) `Disclose AAD→AAT rename in audits/ and msc/naming/ READMEs (archive trees not swept)`

### Stage 8 — Lineage (CLAUDE.md + HISTORICAL-CONTEXT) + CHANGELOG
The lineage must be **baseline knowledge for all agents** (Joseph
2026-05-15) — so three places, not two:
- **`CLAUDE.md` *Naming note*** (~the line that currently records only
  ACT→AAD, 2026-04-16): extend to the full chain — ACT → (AAD, Apr
  2026, AI-Consciousness-Test collision) → **AAT (May 2026)**; keep the
  pointer to `msc/naming/name-transition-aad.md`. This is the
  agent-facing baseline.
- **`HISTORICAL-CONTEXT.md`** line-92 clause: manual replacement per
  §2.4 (the brief multi-hop lineage note).
- **`CHANGELOG.md`**: new cycle entry — scope (the §2.2 disposition),
  the styled-`&` title-page decision, `.aux`/`--all` regeneration, the
  two disclosure READMEs, and Joseph's verbatim rationale (recorded in
  §1: *"Upgrading terminology to Theory now that it has substantial
  claims and novelty, … freeing 'Adaptation and Actuation Dynamics' for
  a very dry and generic textbook."*).
- Commit: `Rename AAD→AAT: lineage in CLAUDE.md + HISTORICAL-CONTEXT + CHANGELOG entry`

### Stage 9 — Auto-memory (outside git)
- `~/.claude/projects/-Users-josephwecker-v2-src-agentic-systems/memory/*.md`
  + `MEMORY.md` (32 files): Rules 1–3, preserve each memory's intent.
- Flag (do not edit) global `~/.claude/CLAUDE.md` for Joseph's
  memory-curation substrate.
- Not a git commit (memory is out-of-repo).

### Stage 10 — Final verification + merge
1. Grep clean **under the canonical FROZEN+KERNEL pathspec** (§2.2;
   `_obs/`/`releases/`/kernel legitimately retain AAD and are excluded
   by pathspec, not expected to be 0 within them). Use **basic** regex
   (`-o`/`-n` without `-E`) — `-E '\bAAD\b'` silently returns 0:
   - `git grep -n 'Adaptation and Actuation Dynamics' -- <pathspec>` →
     empty (HISTORICAL-CONTEXT lineage clause + CHANGELOG prior-name
     mentions are the *only* sanctioned survivors, and they are written
     to read correctly, not as the bare phrase).
   - `git grep -n '\bAAD\b' -- <pathspec>` → empty.
   - `git grep -nE '01-aad-core|03-logogenic-agents|04-eli/|04-logozoetic-agents' -- <pathspec>`
     → empty (no stale dir tokens; `-E` is fine here, no `\b`).
   - `bin/build-monograph aat` / `llm` / `eli` all resolve;
     `git grep -n 'build-monograph aad'` → no stale invocations.
2. `bin/build-monograph --all` end-to-end (all volumes, so every `.aux`
   regenerates for cross-monograph xr); AAT PDF title page shows styled
   "Adaptation & Actuation Theory"; cover renders; sibling volumes still
   build and cross-reference AAT correctly.
3. `bin/lint-md`, `bin/lint-outline`, `bin/term lint` pass.
4. Segment-count / structural parity vs the Stage 0 baseline (nothing
   deleted, ordering intact).
5. `git checkout main && git merge --no-ff rename/aad-to-aat`; delete
   branch.

---

## 6. Risks & mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Blanket `Dynamics→Theory` corrupts "dynamical systems" / "strategy dynamics" / "modularity-state-dynamics" | Would be severe | **Forbidden.** Phrase-only replacement; §4 safety result verified |
| Hand-edit a generated file; source still says AAD; build later reverts it | Medium | §3 discipline — edit source, regenerate; Stage 6 ordering; Stage 10 grep of *built* `aat-v0.2.0.md` |
| Glued `AAD/`, `AAD_Dependencies` missed by `\bAAD\b` | Medium | Explicit §4.3 patterns + residual-`AAD` grep at Stage 10 |
| Kernel file swept → false historical record ("ACT→AAT") | Low | §2.3 kernel excluded from Stage 7; eyeball-confirm with Joseph first |
| HISTORICAL-CONTEXT line 92 mechanically becomes "renamed to AAT in April 2026" (false) | Certain if not handled | §2.4 manual exception; deferred out of Stage 1 to Stage 8 |
| Broken internal links after directory rename | Medium | Stage 2 path-token sweep (4,536); Stage 10 lint catches broken relative links |
| Styled `&` leaks into LaTeX body and breaks the build | Low | `&` confined to two title-page *source* lines; `mono-meta` title is a quoted string; the typeset layer escapes the title-page title; Stage 6 build is the check |
| `&` accidentally used in running prose | Low | Default is "and"; `&` is an explicit two-line targeted re-edit, not a global sub |
| Memory/repo split-vocabulary | Low | Stage 9 explicit; global CLAUDE.md flagged not auto-edited |
| `04-eli`→`04-eli-core` over-matches bare "eli" / `#…eli…` content slugs | Medium | Rule 4a path-segment-anchored, never bare-word; Stage 2b verify grep + Stage 10 lint |
| Dropping the `aad` build alias breaks a script / muscle-memory mid-flight | Low | Intentional (stale alias = foot-gun); `aat`/`01`/numeric still resolve; Stage 10 greps `build-monograph aad` |
| `llm` slug ↔ "Large Language Model" / `03-llm-hallucinate-bound` confusion for future readers | Accepted | Internal-only (display name stays "Logogenic Agents"); recorded §1.2; Joseph-confirmed 2026-05-15 |
| Name change + harmonization entangled in one commit (hard to bisect) | Low | Stage 2 split into 2a (name) / 2b (harmonization); 02 untouched |

---

## 7. Estimated effort

Mechanical scope exceeds the prior ACT→AAD transition: ~4,536 + 844 +
372 + 138 ≈ **5,890 directory path-tokens** plus the 14,388 `AAD` name
tokens across 947 files (incl. archaeology). Substitution rules stay
simple (ASF/umbrella untouched; the only judgment surfaces are the
§2.3 kernel and the styled-`&`). Scripted subs + per-stage
diff review + regeneration: roughly a focused half-day, dominated by the
Stage 1/3/4 prose diff reviews and the Stage 6 build/regenerate
verification. Effort is not a planning constraint here — correctness and
the clean final state are. The staging exists so any stage is
independently revertible, not to ration the work.
