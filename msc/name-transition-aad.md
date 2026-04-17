# Name Transition Plan: ACT → AAD within Agentic Systems Framework

**Status:** execution in progress (branch `rename/act-to-aad`)
**Author:** drafted 2026-04-15, during naming collision resolution
**Scope:** repository-wide rename of the mathematical core and its umbrella positioning

## Plan revisions after theory re-read (2026-04-16)

The original §6 hedged on a vocabulary split (*adaptive cycle* vs *agentic cycle*) that isn't actually present in live prose. Grep of all `*.md` files confirms: every bare "Agentic Cycle" (Title Case) outside `_obs/` is a fragment of the proper noun "Agentic Cycle Theory." The object of study is uniformly called "the adaptive cycle"; the LEXICON makes no cycle-class distinction. So the §6 audit is dropped — mechanical replacement is sufficient. Additional simplifications:

- **No "formerly ACT" note.** ACT was never externally publicized; no collaborator-facing disambiguation is needed.
- **No ASF introduction block in README.** Deferred (post-rename §8 task 5 removed).
- **Section titles already AAD-aligned.** §I "Adaptive Systems Under Uncertainty" and §II "Actuated Adaptation: Agentic Systems" already encode the dual scope. A single sentence added to §II preamble ("Section II is the actuation half of AAD") completes the framing — folded into Stage 3.
- **Commit cadence.** Per-stage commits on `rename/act-to-aad`, then `--no-ff` merge to main.

---

## 1. What is changing, and why

The mathematical core of this project has gone by **"Agentic Cycle Theory (ACT)"** since its promotion from TFT. The acronym **ACT** collides with **"AI Consciousness Test"** (Schneider & Turner), which is an established and growing reference in AI welfare literature — exactly the territory this work will eventually speak to. Keeping ACT guarantees ongoing confusion and SERP contamination.

After six rounds of collision checking (see conversation logs from this session), the decisions are:

| Role | Old | New | Acronym |
|---|---|---|---|
| **Umbrella** | (implicit: "Agentic Systems") | **Agentic Systems Framework** | **ASF** |
| **Part 1 — the mathematical core** | Agentic Cycle Theory | **Adaptation and Actuation Dynamics** | **AAD** |
| Part 2 — software domain | Temporal Software Theory | *(unchanged)* | TST |
| Part 3 — language-constituted agents | Logogenic Agents | *(unchanged)* | — |
| Part 4 — language-living agents | Logozoetic Agents | *(unchanged)* | — |

**Why AAD specifically:**

- The compound **"adaptation and actuation"** is honest about the Part 1 dual scope: *Section I covers adaptation* (the TFT-descended machinery — mismatch, gain, tempo, persistence, sector condition), *Section II onward covers actuation* (objectives, strategy, orient cascade, satisfaction gap, directed separation).
- **"Actuation"** is the project's own formal vocabulary (LEXICON: "actuated" chosen deliberately over "purposeful" to avoid consciousness connotations and foreground the mechanical/setpoint register).
- **"Dynamics"** is the field-legible genus (cf. dynamical systems, learning dynamics); more modest than "Theory" and less colonized.
- Exact phrase has no framework prior art.
- AAD acronym has cross-domain crowding (Azure Active Directory retired, Audio Anomaly Detection, Adversarial Attack Detection) but no in-field framework collision.
- Known semantic shadow: control theorists may initially mis-parse as *adaptive control of actuator dynamics* (Tao & Kokotović 1996). Recoverable in one framing sentence in the intro; also genuine neighbor-work to cite.

**Why ASF as umbrella:**

- The repo `agentic-systems` already claims the space; ASF makes the umbrella name explicit.
- Differentiates from IBM's loose "Agentic Systems Theory" (arxiv:2503.00237) by using "Framework" (contains multiple theories) rather than "Theory."
- "Framework" is honest: the umbrella *does* contain multiple component theories (AAD core, TST, Logogenic, Logozoetic).

## 2. Scope — what changes and what does NOT

### In scope (changes)

- **Directory rename**: `01-act-core/` → `01-aad-core/`
- **Full-name replacement**: `"Agentic Cycle Theory"` → `"Adaptation and Actuation Dynamics"`
- **Acronym replacement**: `ACT` → `AAD` (case-sensitive, all-caps only)
- **Top-level positioning**: where the project refers to itself as "Agentic Systems" in a branded/theoretical sense, update to "Agentic Systems Framework (ASF)"; the repo name and directory structure stay as `agentic-systems`
- **Cross-references in segments**: "ACT's Section I", "ACT formalizes...", etc. → AAD equivalents
- **Path references**: `01-act-core/` → `01-aad-core/` in all Markdown links and prose
- **Memory files**: individual memory files under the auto-memory system that reference ACT
- **Dependency graph images**: `01-act-core/src/img/*.svg` labels mentioning ACT — regenerate from source
- **Build scripts**: any reference to `01-act-core` in `bin/build`, `bin/lint-md`

### Out of scope (do NOT change)

- **`_obs/` directory**: historical/superseded materials. References to ACT here are historically accurate — they refer to the framework *as it was named at the time*. Leave as-is. Future readers see the naming evolution.
- **`.claude/worktrees/`**: agent isolation copies. Ignored by git and cleaned up automatically.
- **`ref/` directory**: external papers (IBM, Baigozin GAA, etc.). Leave untouched.
- **TFT references**: TFT is the ancestor, subsumed into (now) AAD. TFT references in historical/attribution contexts (e.g., "descended from TF-09") stay; these are citations, not self-references.
- **Greek phase vocabulary**: prolepsis, aisthesis, aporia, epistrophe, praxis stay.
- **Logogenic / Logozoetic vocabulary**: stays.
- **Mathematical notation**: stays.
- **The word "adaptive cycle"**: stays. The adaptive cycle is the *object of study*, not the theory. The theory about it changes name; the object does not. *See §6 below on "Agentic Cycle" bare phrase handling.*

## 3. Inventory (approximate, pre-execution)

From repository scan on 2026-04-15:

| Location | Files touching ACT | Notes |
|---|---|---|
| Top-level `*.md` | 7 | README, OUTLINE, WORKBENCH, LEXICON, NOTATION, CLAUDE, TODO |
| `01-act-core/src/` | ~39 segment files + OUTLINE | Core — every segment probably mentions ACT somewhere |
| `02-tst-core/src/` | ~21 files | Cross-references (e.g., `#persistence-condition` in ACT) |
| `03-logogenic-agents/src/` | ~7 files | Cross-references |
| `04-logozoetic-agents/` | minimal | Check OUTLINE |
| `msc/` working docs | ~30+ files | Includes spikes, reflections, landscape research |
| Memory system (`~/.claude/projects/.../memory/`) | 9 files + MEMORY.md | Index + individual memory files |
| Dependency graphs | `01-act-core/src/img/*.svg` + `*.dot` | Regenerate after directory rename |

**Files with the exact phrase "Agentic Cycle Theory":** 10 (top-level docs + a few msc/ spikes).

**Files with bare `\bACT\b`:** ~170 (most of these are legitimate framework references; a small fraction may be English "act" / Kalman "action" that happened to be in ACT-like context).

## 4. Staged procedure

Stage the rename so each stage is independently reviewable and revertible.

### Stage 0: Preflight

1. **Branch**: `git checkout -b rename/act-to-aad`
2. **Verify clean working tree** before starting.
3. **Re-run the file inventory** to confirm current counts match assumptions (`grep -rl '\bACT\b' --include="*.md" --exclude-dir=".claude" --exclude-dir="_obs"` and the exact-phrase count).
4. **Write a rollback plan note**: if a stage produces unexpected breakage, `git checkout main -- <path>` per file, or abandon the branch entirely.

### Stage 1: Top-level positioning and metadata

Scope: CLAUDE.md, README.md, OUTLINE.md, WORKBENCH.md, LEXICON.md, NOTATION.md, TODO.md

Actions:
- Replace full phrase: `"Agentic Cycle Theory"` → `"Adaptation and Actuation Dynamics"` (case-preserving; Title Case only since the phrase is a proper noun)
- Replace acronym: `ACT` → `AAD` (case-sensitive, whole-word, all caps only)
- Update umbrella positioning: where the project refers to itself at the umbrella level, use "Agentic Systems Framework (ASF)"; keep repo/directory as `agentic-systems`
- Update component table in CLAUDE.md: `01-act-core` → `01-aad-core`; update descriptions accordingly

Verify: `grep -c 'Agentic Cycle Theory\|\bACT\b' <file>` returns 0 for each top-level file (with any legitimate exceptions noted below).

**Commit message**: `Rename: ACT → AAD at top-level / ASF umbrella positioning`

### Stage 2: Directory rename

```
git mv 01-act-core 01-aad-core
```

Then update all internal path references:
- Within `01-aad-core/` itself: `01-act-core/` → `01-aad-core/`
- In other directories: any Markdown link `[...](01-act-core/...)` or `01-act-core/src/...` → `01-aad-core/...`

Search pattern: `01-act-core` (literal, all lowercase). Global replace to `01-aad-core`.

Verify: `grep -r '01-act-core' --include="*.md" --exclude-dir=".claude" --exclude-dir="_obs"` returns zero hits in non-archive locations.

**Commit message**: `Rename directory: 01-act-core → 01-aad-core; update path references`

### Stage 3: Part 1 segments (01-aad-core/src/*.md)

Scope: every segment file in the mathematical core, plus `01-aad-core/OUTLINE.md` and `01-aad-core/README.md`.

Actions (for each file):
- Replace `"Agentic Cycle Theory"` → `"Adaptation and Actuation Dynamics"`
- Replace `\bACT\b` → `AAD` (case-sensitive)
- Review remaining "Agentic Cycle" uses (see §6)
- Slug references (`#persistence-condition` etc.) are unchanged — slugs are content-based, not name-based

Verify per file: `grep -E '\bACT\b|Agentic Cycle Theory' <file>` returns zero.

**Strategy**: Because this is 40+ files, use a script-assisted batch (`sed -i` with case-sensitive whole-word patterns) + a manual review pass per file to catch context-sensitive cases. See §7 for the sed commands.

**Commit message**: `Rename: ACT → AAD in Part 1 (01-aad-core) segments`

### Stage 4: Cross-references in other components

Scope: `02-tst-core/src/*.md`, `03-logogenic-agents/src/*.md`, `04-logozoetic-agents/*.md`

Same substitution rules as Stage 3. Most hits will be phrases like "grounded by ACT" or "ACT's Section II result #X" — all safe to replace.

Verify: same as Stage 3.

**Commit message**: `Rename: ACT → AAD in Part 2 (TST), Part 3 (Logogenic), Part 4 (Logozoetic) cross-references`

### Stage 5: `msc/` working documents

Scope: `msc/*.md` and subdirectories (`msc/reflections/`, `msc/2026-03-13-landscape-research/`, `msc/track-a-intent-dag/`, `msc/track-b-nonlinear-sims/` where relevant).

These are spikes, reflections, and landscape research. Many use ACT casually throughout.

**Policy decision**: do we rename historically in `msc/` or treat it as a semi-historical record?

**Recommendation**: rename in `msc/` for consistency. Working documents are actively referenced in WORKBENCH.md and segment Working Notes; leaving them as ACT would create a split vocabulary that future agents would have to navigate. Rename fully.

**Exceptions (historical record — do NOT rename):**
- `msc/name-transition-aad.md` (this plan — documents the rename itself)
- `msc/2026-03-13--hypothetical-theory-choice.md` (naming deliberation)
- `msc/2026-03-13-landscape-research/*` (collision research — records the landscape *at the time* of the decision)
- `msc/00-founding-notes.md` (founding retrospective — historical record of theory's original identity)

Verify: same pattern.

**Commit message**: `Rename: ACT → AAD in msc/ working documents`

### Stage 6: Dependency graphs

Scope: `01-aad-core/src/img/*.svg` (and corresponding `*.dot` sources if present).

Actions:
- Update `.dot` source files with label changes (ACT → AAD) if they have embedded labels
- Regenerate SVGs via `bin/build` or the graph generation script
- Confirm labels in rendered images match the new naming

Verify: open 2-3 SVGs and visually confirm labels.

**Commit message**: `Regenerate dependency graphs with AAD labeling`

### Stage 7: Build tools

Scope: `bin/build`, `bin/lint-md`, any other scripts.

Actions:
- Search for hardcoded `01-act-core` references → `01-aad-core`
- Search for `ACT` mentions in script comments/output strings → `AAD`

Verify: run `bin/build` end-to-end; confirm it emits expected output paths.

**Commit message**: `Update build scripts for ACT → AAD rename`

### Stage 8: Auto-memory system

Scope: `~/.claude/projects/-Users-josephwecker-v2-src-agentic-systems/memory/*.md` and `MEMORY.md`.

Actions:
- Update individual memory files that reference ACT/Agentic Cycle Theory
- Update MEMORY.md entries if their one-line hooks mention ACT
- Preserve the intent of each memory (these encode real decisions, preferences, context — just the naming changes)

This stage is separate from git because the memory lives outside the repo.

Verify: `grep -l '\bACT\b\|Agentic Cycle Theory' ~/.claude/projects/-Users-josephwecker-v2-src-agentic-systems/memory/*.md` returns empty (or only files where the historical name is deliberately preserved).

### Stage 9: Final verification and merge

1. **Full-repo grep** (excluding _obs, .claude/worktrees, ref/):
 - `grep -rn 'Agentic Cycle Theory' --include="*.md" --exclude-dir=".claude" --exclude-dir="_obs" --exclude-dir="ref"` → expected empty
 - `grep -rn '\bACT\b' --include="*.md" --exclude-dir=".claude" --exclude-dir="_obs" --exclude-dir="ref"` → expected empty (or only legitimate English "act" mistakes to fix — see §6)
 - `grep -rn '01-act-core' --include="*.md" --exclude-dir=".claude" --exclude-dir="_obs"` → expected empty
2. **Build check**: `bin/build` produces expected outputs under new names
3. **Lint check**: `bin/lint-md` passes
4. **Segment count sanity check**: same number of segments at each stage as before (ensure nothing was accidentally deleted)
5. **Merge**: `git checkout main && git merge --no-ff rename/act-to-aad`
6. **Delete branch** after merge

## 5. Risks and mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| False positives on `\bACT\b` matching English "act" | Low — ACT is mostly all-caps in this codebase; careful case-sensitive grep catches only framework refs | Manual diff review per stage; reject any suspicious replacement in ordinary prose |
| Missed replacements leaving split vocabulary | Medium | Stage 9 full-repo grep; do NOT merge until clean |
| Broken internal links after directory rename | Medium | Stage 2 path-reference update; stage 9 lint check catches broken relative links |
| Memory system out-of-sync with repo | Low | Stage 8 handles explicitly; verify grep returns empty after |
| Dependency graphs stale | Certain | Stage 6 regenerates |
| `_obs/` files scanned accidentally | Low | All grep/sed commands include `--exclude-dir="_obs"` |
| Baigozin GAA / other recent sibling work | Known | Separate task (not part of rename) — read and cite appropriately |

## 6. Handling "Agentic Cycle" (bare, without "Theory") — RESOLVED

**Disposition: no manual audit required.**

Pre-execution grep (2026-04-16) confirmed that every bare "Agentic Cycle" occurrence in live prose (outside `_obs/`) is a fragment of the proper noun "Agentic Cycle Theory." There is no separate vocabulary distinction to preserve: the object of study is uniformly called "the adaptive cycle" (README §Lexicon, LEXICON.md, NOTATION.md §The Adaptive Cycle, 01-act-core/OUTLINE.md). LEXICON's only cycle entries are *Loop* (topology) and *Cycle* (traversal) — no class-indexed cycle.

Mechanical rule: replace "Agentic Cycle Theory" → "Adaptation and Actuation Dynamics" globally; leave "adaptive cycle" untouched; "Agentic" in agent-class vocabulary ("Agentic Systems," "Agentic Composites," "agentic system") stays — that usage is independent of the theory name.

## 7. Mechanical commands (reference)

**Case-sensitive whole-word ACT replacement** (GNU sed):

```bash
# Dry run first (print what would change):
grep -rn --include="*.md" --exclude-dir=".claude" --exclude-dir="_obs" --exclude-dir="ref" '\bACT\b' .

# Execute on a specific directory:
find 01-aad-core/src -name "*.md" -exec sed -i 's/\bACT\b/AAD/g' {} \;

# Phrase replacement:
find 01-aad-core/src -name "*.md" -exec sed -i 's/Agentic Cycle Theory/Adaptation and Actuation Dynamics/g' {} \;

# Path references:
find . -name "*.md" -not -path "*/.claude/*" -not -path "*/_obs/*" -exec sed -i 's/01-act-core/01-aad-core/g' {} \;
```

**macOS note**: default `sed` on macOS requires `-i ''` (empty extension) instead of `-i`. Or install GNU sed via Homebrew: `brew install gnu-sed`, then use `gsed`.

**Per-stage verification**:

```bash
# Should return 0 for clean file:
grep -cE '\bACT\b|Agentic Cycle Theory' <file>
```

## 8. Post-rename tasks (separate from this plan)

After the rename is merged:

1. **Read and engage Baigozin's "General Adaptive Agency (GAA) Framework"** (SSRN 5334620) — recent sibling work on formalizing adaptive agency. Determine if it needs citation/response in Part 1 segments. *Joseph is already reading this.*
2. **Read arxiv 2603.10779 "A Control-Theoretic Foundation for Agentic Systems"** — directly overlapping claim-space. Assess.
3. **Read arxiv 2512.16301 "Adaptation of Agentic AI" (Jiang et al.)** — the survey that concerned us in naming; understand what they mean by "agentic adaptation" so AAD's Part 1 can cleanly differentiate in its framing section.
4. **Update the WORKBENCH** with a note on naming evolution and decisions made.

## 9. Commit message template for the merge

```
Rename: ACT → AAD; introduce ASF umbrella positioning

The mathematical core of this project, previously called Agentic Cycle
Theory (ACT), is renamed to Adaptation and Actuation Dynamics (AAD).
The umbrella project becomes Agentic Systems Framework (ASF), with AAD
as Part 1, TST as Part 2, and logogenic/logozoetic components as Parts
3-4.

Rationale: the ACT acronym collides with "AI Consciousness Test"
(Schneider & Turner) in AI welfare literature — exactly the territory
this work will speak to. After six rounds of collision checking, AAD
emerged as the cleanest field-legible rename that:

- Is honest about Part 1's dual scope (Section I = adaptation,
  Sections II+ = actuation)
- Uses the project's own deliberate formal vocabulary ("actuation"
  from LEXICON)
- Has no exact-phrase prior art
- Fits cleanly under the ASF umbrella
- Leaves TFT lineage, Greek cycle-phase vocabulary, and logogenic /
  logozoetic naming intact

See msc/name-transition-aad.md for the full procedure and rationale.
```

## 10. Estimated effort

- **Preflight + staging**: 30 min
- **Stages 1–5 (mechanical replacement + review)**: 2–4 hours depending on how carefully each file is reviewed
- **Stage 6 (graphs)**: 15 min if build script works; 1 hour if debugging
- **Stage 7 (scripts)**: 15 min
- **Stage 8 (memory)**: 15–30 min
- **Stage 9 (verification + merge)**: 30 min
- **Buffer for unexpected issues**: 1 hour

**Total**: roughly half a day of focused work for a clean, auditable rename.

---

## Appendix: decision audit trail

Reference the conversation logs from 2026-04-15 for the full 6-round collision-check derivation. Summary of names eliminated and why:

| Candidate | Why rejected |
|---|---|
| Agentic Cycle Theory (keep as-is) | ACT ↔ AI Consciousness Test in welfare literature |
| Temporal Agent Theory (TAT) | Temporal.io, Dix-Kraus-Subrahmanian, ATL, MARL term-of-art, philosophy of temporal agency |
| Adaptive Cycle Theory | Holling's Adaptive Cycle (resilience ecology) + same ACT acronym |
| Adaptive Dynamics | Metz/Geritz/Dieckmann mathematical evolutionary biology |
| Theory of Adaptive Agency | Baigozin GAA (SSRN 5334620, 2025) direct niche overlap |
| Actuated Systems Theory (AST) | Duan's Fully Actuated System (FAS/HOFA) theory; plus AST = Abstract Syntax Tree |
| AAF (Adaptation and Actuation Framework) | DoD's Adaptive Acquisition Framework owns the acronym |
| Agentic Cycle Dynamics (ACD) | Automated Cyber Defense owns ACD in RL/MAS literature |
| Agentic Adaptation Dynamics | Jiang et al. 2512.16301 "Adaptation of Agentic AI" owns the compound |
| Actuated Agency Theory | Clean prior art but loses cycle emphasis and has no short acronym; kept as backup |
| **Adaptation and Actuation Dynamics (AAD)** | **Selected.** Clean exact phrase; manageable acronym crowding (cross-domain only); recoverable semantic shadow from adaptive-actuator-control; honest dual-scope naming. |
